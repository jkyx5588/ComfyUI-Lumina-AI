import requests
import json
import re
from PIL import Image
import io
import base64
import numpy as np

# 导入全量数据 (包含 v40 新增的 Conflict, Dialogue, Devices)
from .lumina_data import (
    STORY_STRUCTURES,
    CHARACTER_ARCHETYPES,
    DRAMATIC_CONFLICTS, # New
    DIALOGUE_STYLES,    # New
    NARRATIVE_DEVICES,  # New
    ENDING_TYPES,       # New
    SCRIPT_FORMATS,
    STORY_TONES
)

class LuminaScreenwriterNode:
    """
    v40.0 Lumina Showrunner (God Mode)
    Integrates Conflict Engine, Dialogue Stylization, and Narrative Devices.
    The ultimate storytelling machine.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        # 排序所有列表
        structures = sorted(list(STORY_STRUCTURES.keys()))
        archetypes = sorted(list(CHARACTER_ARCHETYPES.keys()))
        conflicts = sorted(list(DRAMATIC_CONFLICTS.keys()))
        dialogues = sorted(list(DIALOGUE_STYLES.keys()))
        devices = sorted(list(NARRATIVE_DEVICES.keys()))
        endings = sorted(list(ENDING_TYPES.keys()))
        formats = sorted(list(SCRIPT_FORMATS.keys()))
        tones = sorted(STORY_TONES)

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 核心灵感
                "core_idea": ("STRING", {"default": "A detective realizes he is an AI", "multiline": True, "placeholder": "Logline / Idea..."}),
                
                # 2. 剧作骨架 (Skeleton)
                "narrative_structure": (structures, {"default": "📖 Save the Cat (Blake Snyder) [救猫咪/好莱坞经典]"}),
                "protagonist_archetype": (archetypes, {"default": "👤 The Anti-Hero [反英雄]"}),
                "dramatic_conflict": (conflicts, {"default": "⚔️ Man vs. Self (Internal) [内心冲突/救赎]"}),
                
                # 3. 风格与技法 (Style & Technique)
                "dialogue_style": (dialogues, {"default": "🗣️ Hemingway (Iceberg) [冰山理论/极简]"}),
                "narrative_device": (devices, {"default": "🧩 Chekhov's Gun [契诃夫之枪]"}),
                
                # 4. 基调与结局 (Tone & Resolution)
                "story_tone": (tones, {"default": "🧠 Psychological / Cerebral [心理/烧脑]"}),
                "ending_type": (endings, {"default": "🏁 Twist Ending [反转结局]"}),
                
                # 5. 输出控制
                "script_format": (formats, {"default": "📜 Standard Screenplay [标准电影剧本]"}),
                "creativity": ("FLOAT", {"default": 0.8, "min": 0.1, "max": 1.0}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "image_input": ("IMAGE",), 
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📜 Full_Script", "📝 Logline_OneSheet", "👤 Character_Profile", "🧩 Plot_Beat_Sheet", "⚙️ Raw_JSON")
    
    FUNCTION = "write_script" 
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

    def write_script(self, ollama_connection, core_idea, narrative_structure, protagonist_archetype, dramatic_conflict, dialogue_style, narrative_device, story_tone, ending_type, script_format, creativity, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']

        # 视觉灵感
        img_b64 = None
        vis_ctx = ""
        if image_input is not None:
            img_b64 = self.tensor_to_base64(image_input)
            vis_ctx = "[Visual Inspiration: An image is provided. Use its visual elements (lighting, setting, objects) as key plot points.]"
            print(f"📝 Showrunner: Analyzing image for story inspiration...")

        # 检索知识
        struct_info = STORY_STRUCTURES.get(narrative_structure, {})
        arch_info = CHARACTER_ARCHETYPES.get(protagonist_archetype, "")
        conflict_info = DRAMATIC_CONFLICTS.get(dramatic_conflict, "")
        dialogue_info = DIALOGUE_STYLES.get(dialogue_style, "")
        device_info = NARRATIVE_DEVICES.get(narrative_device, "")
        ending_info = ENDING_TYPES.get(ending_type, "")

        # 构建“王牌制作人” System Prompt
        system_prompt = f"""
        [SYSTEM ROLE]
        You are a Legendary Showrunner and Screenwriter (Oscar-winning level).
        You construct stories with deep psychological conflict, subtext, and structural precision.
        
        [CORE CONCEPT]
        "{core_idea}"
        {vis_ctx}
        
        [DRAMATIC CONFIGURATION (THE ENGINE)]
        1. Structure: {narrative_structure}
           *Beats*: {struct_info.get('steps')}
        2. Protagonist: {protagonist_archetype}
        3. Core Conflict: {dramatic_conflict}
           *Focus*: {conflict_info}
        
        [STYLISTIC EXECUTION]
        4. Dialogue Voice: {dialogue_style}
           *Rule*: {dialogue_info}
        5. Tone: {story_tone}
        6. Narrative Device: {narrative_device} ({device_info})
           *Instruction*: You MUST integrate this specific device into the plot.
        
        [RESOLUTION]
        7. Ending: {ending_type}
        
        [TASK]
        Generate a comprehensive script package.
        - The Script must show, not just tell. Use subtext.
        - Ensure the conflict drives the scene.
        - Incorporate the visual inspiration if provided.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "logline": "A killer one-sentence summary (Netflix style).",
            "character_sheet": "Name, Physical Appearance, Fatal Flaw, Goal.",
            "beat_sheet": "A bullet point list of the major plot beats (Setup, Catalyst, etc.).",
            "script_content": "The actual script in {script_format} format. Include Scene Headings, Action, Dialogue.",
            "analysis": "Notes on how you applied the conflict and narrative device."
        }}
        """

        payload = {
            "model": model,
            "prompt": system_prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": creativity, "seed": seed, "num_ctx": 16384} # 增加上下文以支持长剧本
        }
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"📝 Lumina Showrunner: Developing '{core_idea}'...")
            r = requests.post(url, json=payload, timeout=300)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                logline = res.get("logline", "")
                char = res.get("character_sheet", "")
                beats = res.get("beat_sheet", "")
                script = res.get("script_content", "")
                # 处理 beat_sheet 可能是列表的情况
                if isinstance(beats, list): beats = "\n".join([f"- {b}" for b in beats])
            except:
                print(f"⚠️ JSON Rescue Active")
                logline = self.manual_extract(clean, "logline")
                char = self.manual_extract(clean, "character_sheet")
                script = self.manual_extract(clean, "script_content")
                beats = "Error parsing beats"
            
            return (script, logline, char, beats, clean)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")