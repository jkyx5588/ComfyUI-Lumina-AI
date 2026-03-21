import requests
import json
import re
import torch
import numpy as np
from PIL import Image
import io
import base64

from .lumina_data import (
    COLOR_HARMONIES, CINEMATIC_LOOKS, COLOR_SPACES, FILM_GRAIN_TYPES
)

class LuminaColorNode:
    """
    v51.0 Lumina Color Grader (Visual Edition)
    - Can analyze an input Image/Video to extract its Color Grade (LUT).
    - Can analyze Audio to determine the emotional color palette.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        harmonies = sorted(list(COLOR_HARMONIES.keys()))
        looks = sorted(list(CINEMATIC_LOOKS.keys()))
        stocks = sorted(list(COLOR_SPACES.keys()))
        grains = sorted(list(FILM_GRAIN_TYPES.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "base_image_desc": ("STRING", {"default": "A rainy street at night", "multiline": True}),
                
                # 专业调色参数
                "cinematic_look": (looks, {"default": "🎞️ Teal & Orange (Blockbuster) [好莱坞青橙]"}),
                "film_stock": (stocks, {"default": "📼 Kodak Portra 400 [人像王]"}),
                "grain_texture": (grains, {"default": "📼 35mm Cinematic Grain [35mm电影颗粒]"}),
                "color_harmony": (harmonies, {"default": "🎨 Complementary (Teal/Orange) [互补色/青橙]"}),
                
                "temperature": ("FLOAT", {"default": 0.6}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                # 多模态接口：提取参考图的色调
                "image_input": ("IMAGE",), 
                "video_frames": ("IMAGE",),
                "audio_input": ("AUDIO",),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("🎨 Color_Prompt_Suffix", "🧠 Grading_Report", "🍭 Hex_Palette", "⚙️ Raw_JSON")
    FUNCTION = "generate_grading"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image_tensor):
        try:
            if not isinstance(image_tensor, torch.Tensor): return None
            # Take middle frame if video, or first frame
            idx = image_tensor.shape[0] // 2
            i = 255. * image_tensor[idx].cpu().numpy()
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

    def generate_grading(self, ollama_connection, base_image_desc, color_harmony, cinematic_look, film_stock, grain_texture, temperature, seed, image_input=None, video_frames=None, audio_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        
        # 多模态上下文
        img_b64 = None
        vis_ctx = ""
        aud_ctx = ""

        if video_frames is not None:
            img_b64 = self.tensor_to_base64(video_frames)
            vis_ctx = "[Visual Ref: Video frame provided. Extract the lighting mood and color grading from this frame.]"
        elif image_input is not None:
            img_b64 = self.tensor_to_base64(image_input)
            vis_ctx = "[Visual Ref: Image provided. Match this color palette and contrast.]"
            
        if audio_input is not None:
            aud_ctx = "[Audio Ref: Music provided. Suggest colors that match the emotion of this sound (e.g. Sad=Blue, Energetic=Red).]"

        # 知识
        harm_info = COLOR_HARMONIES.get(color_harmony, "")
        look_info = CINEMATIC_LOOKS.get(cinematic_look, "")
        stock_info = COLOR_SPACES.get(film_stock, "")
        grain_info = FILM_GRAIN_TYPES.get(grain_texture, "")

        sys_prompt = f"""
        [ROLE] Professional Colorist (Digital Intermediate).
        [TASK] Generate specific prompt keywords for Color Grading, Lighting, and Texture.
        
        [INPUT] Scene: "{base_image_desc}"
        [CONTEXT] {vis_ctx} {aud_ctx}
        
        [GRADING PARAMETERS]
        1. Look: {cinematic_look} ({look_info})
        2. Stock: {film_stock} ({stock_info})
        3. Grain: {grain_texture} ({grain_info})
        4. Harmony: {color_harmony} ({harm_info})
        
        [INSTRUCTIONS]
        - If Visual Ref is provided, analyze its histogram/mood and clone it.
        - Combine the Parameters into a dense prompt suffix.
        - Suggest 5 specific Hex colors.
        
        [OUTPUT JSON]
        {{
            "grading_prompt": "Keywords for SD (e.g. 'color graded, teal shadows, film grain, ...').",
            "analysis": "Why this grading fits the input.",
            "hex_palette": "#..., #..., #..., #..., #..."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}, "images": [img_b64] if img_b64 else []}
        
        try:
            r = requests.post(url, json=payload, timeout=120)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p = res.get("grading_prompt", "")
                a = res.get("analysis", "")
                h = res.get("hex_palette", "")
            except:
                p = self.manual_extract(clean, "grading_prompt")
                a = "Error"
                h = "#000000"
            return (p, a, h, clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err")