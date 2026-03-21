import requests
import json
import re
from PIL import Image
import io
import base64
import numpy as np
import torch

from .lumina_data import (
    BRAND_VALUES, BRAND_SYSTEMS, BRAND_DELIVERABLES, BRAND_GRAPHICS,
    LOGO_INDUSTRIES # 复用之前的行业数据
)

class LuminaBrandNode:
    """
    v80.0 Lumina Brand Director (The Full Case Study)
    Generates comprehensive Brand Identity System prompts based on strategy and multimodal inputs.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        industries = sorted(list(LOGO_INDUSTRIES.keys()))
        values = sorted(list(BRAND_VALUES.keys()))
        systems = sorted(list(BRAND_SYSTEMS.keys()))
        deliverables = sorted(list(BRAND_DELIVERABLES.keys()))
        graphics = sorted(list(BRAND_GRAPHICS.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 品牌定义 (Strategy)
                "brand_name": ("STRING", {"default": "NEXUS", "placeholder": "Brand Name..."}),
                "industry": (industries, {"default": "💻 Tech & AI [科技/AI]"}),
                "core_value": (values, {"default": "🚀 Innovation & Future [创新/未来]"}),
                
                # 2. 视觉系统 (Visual System)
                "design_system": (systems, {"default": "📐 Swiss International (Grid) [瑞士国际主义]"}),
                "graphic_style": (graphics, {"default": "🎨 Data Visualization [数据可视化]"}),
                
                # 3. 输出载体 (Mockup)
                "deliverable": (deliverables, {"default": "💼 Full VI Case Study [VI全案展示]"}),
                
                # 4. 控制
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.7}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                # --- 多模态灵感 ---
                "image_input": ("IMAGE",), # 情绪板 (Moodboard) 参考
                "video_frames": ("IMAGE",), # 动态品牌参考 (Motion Branding)
                "audio_input": ("AUDIO",), # 品牌声音基因 (Sonic Branding)
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Case_Study_Prompts", "🧠 Brand_Strategy", "🎨 Color_Palette_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_brand_case"
    CATEGORY = "Lumina_AI/Advisors"

    # --- 视觉处理逻辑 ---
    def process_visual_input(self, image_tensor):
        try:
            if not isinstance(image_tensor, torch.Tensor): return None, "Invalid"
            batch_size = image_tensor.shape[0]
            if batch_size == 1:
                pil_img = self._tensor_to_pil(image_tensor[0])
                return self._pil_to_base64(pil_img), "Moodboard Image"
            else:
                # 蒙太奇处理视频
                indices = np.linspace(0, batch_size - 1, 4, dtype=int)
                frames = [self._tensor_to_pil(image_tensor[i]) for i in indices]
                w, h = frames[0].size
                grid = Image.new('RGB', (w * 2, h * 2))
                grid.paste(frames[0], (0, 0)); grid.paste(frames[1], (w, 0))
                grid.paste(frames[2], (0, h)); grid.paste(frames[3], (w, h))
                grid.thumbnail((1024, 1024))
                return self._pil_to_base64(grid), "Motion Graphic Reference"
        except: return None, "Error"

    def _tensor_to_pil(self, tensor):
        return Image.fromarray(np.clip(255. * tensor.cpu().numpy(), 0, 255).astype(np.uint8))

    def _pil_to_base64(self, pil_img):
        buf = io.BytesIO()
        pil_img.save(buf, format="JPEG", quality=85)
        return base64.b64encode(buf.getvalue()).decode("utf-8")

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def generate_brand_case(self, ollama_connection, brand_name, industry, core_value, design_system, graphic_style, deliverable, prompt_count, temperature, seed, image_input=None, video_frames=None, audio_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']

        # 多模态上下文
        img_b64, vis_type = None, "None"
        vis_ctx, aud_ctx = "", ""

        if video_frames is not None:
            img_b64, vis_type = self.process_visual_input(video_frames)
            vis_ctx = f"[Visual Input: A video sequence ({vis_type}) provided. Use this to determine the 'Motion Branding' style (speed, easing, transition).]"
        elif image_input is not None:
            img_b64, vis_type = self.process_visual_input(image_input)
            vis_ctx = "[Visual Input: A Moodboard image provided. Extract the color palette and texture from this image.]"
            
        if audio_input is not None:
            aud_ctx = "[Audio Input: Sonic Branding provided. If the sound is energetic, make the design bold/loud. If soft, make it minimal/pastel.]"

        # 知识检索
        val_info = BRAND_VALUES.get(core_value, "")
        sys_info = BRAND_SYSTEMS.get(design_system, "")
        del_info = BRAND_DELIVERABLES.get(deliverable, "")
        gra_info = BRAND_GRAPHICS.get(graphic_style, "")

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Chief Creative Officer (CCO) at a top design agency (e.g., Pentagram, Collins).
        You are designing a complete Visual Identity System (VIS) for a client.
        
        [CLIENT BRIEF]
        - Brand Name: "{brand_name}"
        - Industry: {industry}
        - Core Value: {core_value} ({val_info})
        {vis_ctx} {aud_ctx}
        
        [DESIGN DIRECTION]
        1. Design System: {design_system} ({sys_info})
        2. Supergraphics: {graphic_style} ({gra_info})
        3. Output Format: {deliverable} ({del_info})
        
        [TASK]
        Generate {prompt_count} highly detailed prompts for Stable Diffusion/Midjourney.
        - The goal is to generate a "Case Study Mockup" image.
        - Describe the layout, lighting, materials, and how the logo/typography is applied to objects.
        - Use terms like: "branding mockup", "stationery set", "high angle", "studio lighting", "octane render".
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "strategy_brief": "A short paragraph explaining the brand concept and creative direction.",
            "color_palette": "List 5 Hex codes and color names.",
            "prompts": ["Prompt 1...", "Prompt 2...", ...],
            "negative": "Negative prompt (e.g. 'low res, messy, blurry, text error')."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"💼 Lumina Brand: Creating case study for '{brand_name}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            
            try:
                res = json.loads(clean)
                p = res.get("prompts", [])
                s = res.get("strategy_brief", "")
                c = res.get("color_palette", "")
                n = res.get("negative", "")
            except:
                p = self.manual_extract(clean, "prompts")
                s = self.manual_extract(clean, "strategy_brief")
                c = "Error"
                n = "low quality"
                if not p: p = ["Error"]

            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            
            return (final_p, str(s), str(c), str(n), clean)

        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")