import requests
import json
import re
import torch
import numpy as np
from PIL import Image
import io
import base64

from .lumina_data import (
    CONCEPT_VIEWS, CONCEPT_STYLES, CONCEPT_MATERIALS, SHOOTING_SUBJECTS
)

class LuminaConceptNode:
    """
    v51.0 Lumina Concept Artist (Visual Edition)
    - Can take a rough sketch (Image Input) and generate a refined concept prompt.
    - Generates Material Breakdowns.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        views = sorted(list(CONCEPT_VIEWS.keys()))
        styles = sorted(list(CONCEPT_STYLES.keys()))
        mats = sorted(list(CONCEPT_MATERIALS.keys()))
        
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "character_desc": ("STRING", {"default": "A mech warrior", "multiline": True}),
                
                "view_type": (views, {"default": "📐 Orthographic Turnaround [正交三视图]"}),
                "art_style": (styles, {"default": "🖌️ Thick Paint / Impasto [厚涂/油画感]"}),
                "primary_material": (mats, {"default": "🛠️ Cybernetic / Hard Surface [硬表面/机械]"}),
                
                "add_background": (["White Background", "Simple Gradient", "Contextual"], {"default": "White Background"}),
                "temperature": ("FLOAT", {"default": 0.6}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "image_input": ("IMAGE",), # 草图输入
                "video_frames": ("IMAGE",), # 动态参考
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Concept_Prompt", "🧠 Design_Notes", "🛠️ Material_Callouts", "⚙️ Raw_JSON")
    FUNCTION = "generate_concept"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image_tensor):
        try:
            if not isinstance(image_tensor, torch.Tensor): return None
            i = 255. * image_tensor[0].cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=85)
            return base64.b64encode(buf.getvalue()).decode("utf-8")
        except: return None

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def generate_concept(self, ollama_connection, character_desc, view_type, art_style, primary_material, add_background, temperature, seed, image_input=None, video_frames=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        
        img_b64 = None
        vis_ctx = ""
        if image_input is not None:
            img_b64 = self.tensor_to_base64(image_input)
            vis_ctx = "[Visual Input: A rough sketch provided. Maintain the pose and silhouette, but refine the details to professional quality.]"
        elif video_frames is not None:
            img_b64 = self.tensor_to_base64(video_frames)
            vis_ctx = "[Visual Input: Dynamic reference provided. Capture the motion.]"

        view_info = CONCEPT_VIEWS.get(view_type, "")
        style_info = CONCEPT_STYLES.get(art_style, "")
        mat_info = CONCEPT_MATERIALS.get(primary_material, "")

        sys_prompt = f"""
        [ROLE] Lead Concept Artist.
        [TASK] Create a Stable Diffusion prompt for a Character/Asset Design Sheet.
        
        [INPUT] "{character_desc}" {vis_ctx}
        
        [SPECS]
        1. View: {view_type} ({view_info})
        2. Style: {art_style} ({style_info})
        3. Material Focus: {primary_material} ({mat_info})
        4. BG: {add_background}
        
        [INSTRUCTIONS]
        - If input is a sketch, describe the lines as 'clean, refined'.
        - Include 'reference sheet, character design, concept art' tags.
        - Describe materials explicitly (e.g., 'worn leather', 'polished steel').
        
        [OUTPUT JSON]
        {{
            "prompt": "Full prompt...",
            "analysis": "Design choices logic...",
            "material_notes": "List of textures to emphasize (e.g. 'Rusty metal, glowing LED')."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}, "images": [img_b64] if img_b64 else []}
        
        try:
            r = requests.post(url, json=payload, timeout=120)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p, a, m = res.get("prompt", ""), res.get("analysis", ""), res.get("material_notes", "")
            except:
                p = self.manual_extract(clean, "prompt")
                a, m = "Error", "Error"
            return (p, a, m, clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err")