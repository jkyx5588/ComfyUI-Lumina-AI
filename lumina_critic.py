import requests
import json
import re
import torch
import numpy as np
from PIL import Image
import io
import base64

from .lumina_data import CRITIC_MODES

class LuminaCriticNode:
    """
    v51.0 Lumina Art Critic (Director Mode)
    - Compares 'generated_image' vs 'reference_image'.
    - Provides specific fixes for SD prompts.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        modes = sorted(list(CRITIC_MODES.keys()))
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "generated_image": ("IMAGE",), # 必须连接
                "original_prompt": ("STRING", {"default": "", "multiline": True}),
                "critique_mode": (modes, {"default": "🧐 Fidelity Check [画质/崩坏检查]"}),
                "temperature": ("FLOAT", {"default": 0.5}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "reference_image": ("IMAGE",), # 目标参考图（可选）
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("✨ Refined_Prompt", "🧐 Critique_Report", "⭐ Score (0-10)", "⚙️ Raw_JSON")
    FUNCTION = "critique_image"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image):
        try:
            if not isinstance(image, torch.Tensor): return None
            i = 255. * image[0].cpu().numpy()
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

    def critique_image(self, ollama_connection, generated_image, original_prompt, critique_mode, temperature, seed, reference_image=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        
        gen_b64 = self.tensor_to_base64(generated_image)
        if not gen_b64: return ("Error", "No Image", "0", "Err")
        
        # 图片列表：[生成图, 参考图(如果有)]
        images_list = [gen_b64]
        ref_ctx = ""
        
        if reference_image is not None:
            ref_b64 = self.tensor_to_base64(reference_image)
            if ref_b64:
                images_list.append(ref_b64)
                ref_ctx = "[COMPARISON MODE]: Image 1 is the Generated Result. Image 2 is the Target Reference. Compare them!"

        mode_info = CRITIC_MODES.get(critique_mode, "")

        sys_prompt = f"""
        [ROLE] Ruthless Art Director.
        [TASK] Critique the image(s) and fix the prompt.
        
        [INPUTS]
        - Original Prompt: "{original_prompt}"
        - Mode: {critique_mode} ({mode_info})
        {ref_ctx}
        
        [INSTRUCTIONS]
        1. Look at Image 1. Does it match the prompt? Is it broken (bad hands, artifacts)?
        2. (If Ref exists) Does Image 1 match the style/vibe of Image 2?
        3. Score it (0-10).
        4. WRITE A BETTER PROMPT to fix the issues.
           - If blurry -> add 'sharp focus, 8k'.
           - If style mismatch -> add specific style keywords found in the Reference.
        
        [OUTPUT JSON]
        {{
            "critique": "Detailed feedback...",
            "score": "7/10",
            "refined_prompt": "The optimized prompt..."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}, "images": images_list}
        
        try:
            r = requests.post(url, json=payload, timeout=240)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                rp = res.get("refined_prompt", "")
                cr = res.get("critique", "")
                sc = res.get("score", "")
            except:
                rp = self.manual_extract(clean, "refined_prompt")
                cr = self.manual_extract(clean, "critique")
                sc = "N/A"
            return (rp, cr, sc, clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err")