import requests
import json
import re
from PIL import Image
import io
import base64

# 导入浩瀚的武侠数据库
from .lumina_data import (
    WUXIA_STYLES, WUXIA_ROLES, WUXIA_MOVES, 
    WUXIA_WEAPONS, WUXIA_CLOTHING, WUXIA_SCENES,
    FRAMING_OPTIONS  # 复用构图库
)

class LuminaWuxiaNode:
    """
    v80.0 Lumina Wuxia Master (Martial Arts Director)
    Specialized in Chinese Martial Arts aesthetics, choreography, and costume.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        styles = sorted(list(WUXIA_STYLES.keys()))
        roles = sorted(list(WUXIA_ROLES.keys()))
        moves = sorted(list(WUXIA_MOVES.keys()))
        weapons = sorted(list(WUXIA_WEAPONS.keys()))
        clothes = sorted(list(WUXIA_CLOTHING.keys()))
        scenes = sorted(list(WUXIA_SCENES.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 剧情核心
                "scene_concept": ("STRING", {"default": "A final duel in the rain", "multiline": True, "placeholder": "Describe the scene..."}),
                
                # 2. 风格与角色
                "wuxia_style": (styles, {"default": "🎥 Wong Kar-wai (Mood) [王家卫/写意]"}),
                "character_role": (roles, {"default": "👤 Wandering Swordsman (Ronin) [浪子/游侠]"}),
                
                # 3. 动作与装备 (核心)
                "martial_art": (moves, {"default": "👊 Sword Qi / Energy Blast [剑气/剑意]"}),
                "weapon": (weapons, {"default": "⚔️ Straight Sword (Jian) [君子剑]"}),
                "clothing": (clothes, {"default": "👗 Bamboo Hat & Rain Cape [斗笠蓑衣]"}),
                
                # 4. 环境与构图
                "environment": (scenes, {"default": "🏔️ Rainy Night Alley [雨夜长街]"}),
                "framing": (FRAMING_OPTIONS, {"default": "Wide Angle (Environmental) [大广角/环境]"}),
                
                # 5. 动态控制
                "action_dynamic": (["Static Pose [静止]", "Slow Motion [慢动作]", "High Speed Blur [高速模糊]", "Freeze Frame [定格]"], {"default": "Freeze Frame [定格]"}),
                
                "prompt_count": ("INT", {"default": 4, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.7}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "image_input": ("IMAGE",), # 参考姿势或构图
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Prompts_List", "🎬 Choreography_Note", "👗 Costume_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_wuxia"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image_tensor):
        try:
            i = 255. * image_tensor[0].cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            return base64.b64encode(buf.getvalue()).decode("utf-8")
        except: return None

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def generate_wuxia(self, ollama_connection, scene_concept, wuxia_style, character_role, martial_art, weapon, clothing, environment, framing, action_dynamic, prompt_count, temperature, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']
        
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: Use this image as a pose/composition reference.]" if img_b64 else ""

        # 检索知识
        style_info = WUXIA_STYLES.get(wuxia_style, "")
        role_info = WUXIA_ROLES.get(character_role, "")
        move_info = WUXIA_MOVES.get(martial_art, "")
        weapon_info = WUXIA_WEAPONS.get(weapon, "")
        cloth_info = WUXIA_CLOTHING.get(clothing, "")
        scene_info = WUXIA_SCENES.get(environment, "")

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Legendary Martial Arts Director (Yuen Woo-ping level) and Costume Designer (Tim Yip level).
        You specialize in Chinese Wuxia aesthetics, historical accuracy, and action choreography.
        
        [SCENE BRIEF]
        Concept: "{scene_concept}"
        {vis_ctx}
        
        [PRODUCTION DESIGN]
        1. Film Style: {wuxia_style} ({style_info})
           *Visual Tone*: Apply this director's color theory and mood.
        2. Character: {character_role} ({role_info})
           *Costume*: {clothing} ({cloth_info})
           *Weapon*: {weapon} ({weapon_info})
        3. Environment: {environment} ({scene_info})
        
        [ACTION CHOREOGRAPHY]
        4. Move/Skill: {martial_art} ({move_info})
        5. Dynamics: {action_dynamic}
        6. Framing: {framing}
        
        [TASK]
        Generate {prompt_count} distinct image prompts.
        - Focus on the "Flow" (Qi) of the cloth and hair.
        - Describe the specific martial arts pose accurately.
        - Use terms like "wuxia", "martial arts", "chinese painting style" where appropriate.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "choreography_note": "Director's note on the action and mood.",
            "costume_specs": "Detailed description of the fabric, accessories, and historical elements.",
            "prompts": ["Prompt 1...", "Prompt 2...", ...],
            "negative": "Negative prompt (e.g. 'western armor, guns, japanese katana, modern buildings')."
        }}
        """

        payload = {
            "model": model,
            "prompt": sys_prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}
        }
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"⚔️ Wuxia Master: Choreographing '{scene_concept}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                prompts = res.get("prompts", [])
                note = res.get("choreography_note", "N/A")
                costume = res.get("costume_specs", "N/A")
                neg = res.get("negative", "low quality")
            except:
                prompts = self.manual_extract(clean, "prompts")
                note = self.manual_extract(clean, "choreography_note")
                costume = self.manual_extract(clean, "costume_specs")
                neg = self.manual_extract(clean, "negative")
                if not prompts: prompts = ["Error"]

            if isinstance(prompts, str): prompts = [prompts]
            final_p = "\n\n".join([f"[{i+1}] {str(p)}" for i, p in enumerate(prompts)])
            
            return (final_p, str(note), str(costume), str(neg), clean)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")