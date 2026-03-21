import requests
import json
import re
import numpy as np
from PIL import Image
import io
import base64

# 导入数据库
from .lumina_data import (
    PROFESSIONAL_KNOWLEDGE_BASE, 
    TECHNICAL_MEDIA, 
    MBTI_AESTHETICS, 
    VIDEO_TYPES, 
    CAMERA_MOVEMENTS, 
    LENS_CHOICES, 
    SHOOTING_SUBJECTS,
    FRAMING_OPTIONS, 
    DETAIL_LEVELS
)

# -----------------------------------------------------------
# 🔌 NODE 1: OLLAMA CONNECTION LOADER
# -----------------------------------------------------------
class OllamaConnectionLoader:
    def __init__(self): pass
    @classmethod
    def INPUT_TYPES(s):
        models = ["llava", "llama3", "mistral", "qwen2.5"]
        try:
            r = requests.get("http://127.0.0.1:11434/api/tags", timeout=1)
            if r.status_code == 200: models = sorted([m['name'] for m in r.json().get('models', [])])
        except: pass
        return {
            "required": {
                "ollama_url": ("STRING", {"default": "http://127.0.0.1:11434/api/generate"}),
                "model_selector": (models,),
            },
            "optional": {"manual_model_entry": ("STRING", {"default": ""})}
        }
    RETURN_TYPES = ("OLLAMA_DICT",)
    RETURN_NAMES = ("🔌 Ollama_Connection",)
    FUNCTION = "create_connection"
    CATEGORY = "Lumina_AI/Utils"

    def create_connection(self, ollama_url, model_selector, manual_model_entry):
        model = manual_model_entry if manual_model_entry.strip() else model_selector
        print(f"🔌 Lumina Linked: {model}")
        return ({"url": ollama_url, "model": model},)

# -----------------------------------------------------------
# 🌌 NODE 2: AESTHETIC ADVISOR (ULTIMATE)
# -----------------------------------------------------------
class LuminaAestheticNode:
    def __init__(self): pass
    @classmethod
    def INPUT_TYPES(s):
        styles = sorted(list(PROFESSIONAL_KNOWLEDGE_BASE.keys()))
        media = sorted(list(TECHNICAL_MEDIA.keys()))
        mbti = sorted(list(MBTI_AESTHETICS.keys()))
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "user_idea": ("STRING", {"default": "", "multiline": True}),
                "creator_personality": (mbti, {"default": "✨ None (Neutral) [无倾向]"}),
                "aesthetic_style": (styles,),
                "technical_medium": (media,),
                "framing": (FRAMING_OPTIONS,),
                "detail_level": (DETAIL_LEVELS,),
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.6}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {"image_input": ("IMAGE",)}
        }
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Prompts_List", "🧠 Analysis", "🧪 Tech_Specs", "📝 Negative", "⚙️ Raw")
    FUNCTION = "generate"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image):
        try:
            i = 255. * image[0].cpu().numpy()
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

    def generate(self, ollama_connection, user_idea, creator_personality, aesthetic_style, technical_medium, framing, detail_level, prompt_count, temperature, seed, image_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        style_data = PROFESSIONAL_KNOWLEDGE_BASE.get(aesthetic_style, {})
        tech_kw = TECHNICAL_MEDIA.get(technical_medium, "")
        mbti = MBTI_AESTHETICS.get(creator_personality, {})
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None

        sys_prompt = f"""
        [ROLE] World-Class Art Director & Prompt Engineer.
        [INPUT] Concept: "{user_idea}"
        [PERSONA] {creator_personality} | Vibe: {mbti.get('vibe')} | Logic: {mbti.get('composition')}
        [STYLE] {aesthetic_style} | Markers: {style_data.get('markers')} | Light: {style_data.get('lighting')} | Color: {style_data.get('colors')}
        [MEDIUM] {technical_medium} ({tech_kw}) | Frame: {framing} | Detail: {detail_level}
        [TASK] Generate {prompt_count} distinct prompts.
        [CONSTRAINTS] Output valid JSON. Single quotes only inside strings.
        [FORMAT] {{ "analysis": "...", "technical_specs": "...", "prompts": ["..."], "negative": "..." }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"🌌 Lumina Aesthetic: Generating...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            try:
                res = json.loads(clean)
                p, a, t, n = res.get("prompts", []), res.get("analysis", ""), res.get("technical_specs", ""), res.get("negative", "")
            except:
                p = self.manual_extract(clean, "prompts")
                a, t, n = "Error", "Error", "Error"
                if not p: p = ["Error"]
            
            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            return (final_p, str(a), str(t), str(n), clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")

# -----------------------------------------------------------
# 🎬 NODE 3: STORYBOARD DIRECTOR
# -----------------------------------------------------------
class LuminaDirectorNode:
    def __init__(self): pass
    @classmethod
    def INPUT_TYPES(s):
        styles = sorted(list(PROFESSIONAL_KNOWLEDGE_BASE.keys()))
        video = sorted(list(VIDEO_TYPES.keys()))
        lenses = sorted(list(LENS_CHOICES.keys()))
        moves = sorted(list(CAMERA_MOVEMENTS.keys()))
        mbti = sorted(list(MBTI_AESTHETICS.keys()))
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "script_content": ("STRING", {"default": "", "multiline": True}),
                "character_profile": ("STRING", {"default": "", "multiline": True}),
                "video_type": (video,),
                "lens_choice": (lenses,),
                "camera_movement": (moves,),
                "shooting_subject": (SHOOTING_SUBJECTS,),
                "aesthetic_style": (styles,),
                "creator_personality": (mbti,),
                "total_duration": ("FLOAT", {"default": 5.0}),
                "frame_count": ("INT", {"default": 4}),
                "temperature": ("FLOAT", {"default": 0.7}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {"char_ref_image": ("IMAGE",)}
        }
    RETURN_TYPES = ("STRING", "LIST", "STRING", "STRING")
    RETURN_NAMES = ("🎞️ Batch_Prompts", "📋 Prompts_List", "🎬 Director_Notes", "⚙️ Raw")
    FUNCTION = "generate_storyboard"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image):
        # Same as above...
        try:
            i = 255. * image[0].cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            return base64.b64encode(buf.getvalue()).decode("utf-8")
        except: return None

    def generate_storyboard(self, ollama_connection, script_content, character_profile, video_type, lens_choice, camera_movement, shooting_subject, aesthetic_style, creator_personality, total_duration, frame_count, temperature, seed, char_ref_image=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        genre = VIDEO_TYPES.get(video_type, {})
        style = PROFESSIONAL_KNOWLEDGE_BASE.get(aesthetic_style, {})
        mbti = MBTI_AESTHETICS.get(creator_personality, {})
        img_b64 = self.tensor_to_base64(char_ref_image) if char_ref_image is not None else None
        
        pace = total_duration / frame_count
        pacing = "Fast" if pace < 1.5 else "Slow"

        sys_prompt = f"""
        [ROLE] Expert Film Director & DP.
        [INPUT SCRIPT] "{script_content}"
        [CHAR] "{character_profile}"
        [STYLE] {aesthetic_style} | Markers: {style.get('markers')}
        [DIRECTOR] {creator_personality} | Vibe: {mbti.get('vibe')}
        [TECH] {video_type} | Lens: {lens_choice} | Move: {camera_movement}
        [TIMING] {total_duration}s ({frame_count} frames, {pace:.1f}s/shot) -> {pacing}
        [TASK] Generate {frame_count} sequential prompts. Start each with Char Profile.
        [FORMAT] {{ "director_notes": "...", "frames": ["Frame 1...", "Frame 2..."] }}
        """

        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"🎬 Lumina Director: Action!")
            r = requests.post(url, json=payload, timeout=300)
            r.raise_for_status()
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            try:
                res = json.loads(clean)
                frames = res.get("frames", [])
                notes = res.get("director_notes", "")
            except:
                # 简单提取
                match = re.search(r'\[.*\]', clean, re.DOTALL)
                frames = json.loads(match.group(0)) if match else []
                notes = "Error parsing notes"
            
            if isinstance(frames, str): frames = [frames]
            batch = "\n".join([f"{f}" for f in frames])
            return (batch, frames, f"Notes: {notes}\nPace: {pace:.1f}s", clean)
        except Exception as e:
            return (str(e), [], "Error", "Error")