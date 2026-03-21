import requests
import json
import re
import torch
import numpy as np
from PIL import Image
import io
import base64

# 导入工业设计数据库
from .lumina_data import (
    ID_CATEGORIES,
    ID_DESIGN_LANGUAGES,
    ID_MATERIALS_CMF,
    ID_PRESENTATION
)

class LuminaIndustrialNode:
    """
    v150.0 Lumina Industrial Titan (Industrial Design & CMF)
    Generates professional product design renders, exploded views, and CMF studies.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        categories = sorted(list(ID_CATEGORIES.keys()))
        languages = sorted(list(ID_DESIGN_LANGUAGES.keys()))
        materials = sorted(list(ID_MATERIALS_CMF.keys()))
        presentations = sorted(list(ID_PRESENTATION.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 产品核心定义
                "product_idea": ("STRING", {"default": "A smart coffee maker", "multiline": True, "placeholder": "What are you designing? (e.g., A futuristic VR headset)"}),
                
                # 2. 工业设计参数
                "id_category": (categories, {"default": "📻 Consumer Electronics [消费电子]"}),
                "design_language": (languages, {"default": "📏 Dieter Rams / Braun Style[博朗极简/迪特·拉姆斯]"}),
                "material_cmf": (materials, {"default": "🛠️ Anodized Aluminum & Glass [阳极氧化铝与玻璃]"}),
                
                # 3. 渲染展示
                "id_presentation": (presentations, {"default": "📸 Hero Studio Shot[影棚白底特写]"}),
                
                # 4. 控制
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.65}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "image_input": ("IMAGE",), # 可上传草图或竞品参考
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 ID_Prompts", "🧠 Design_Rationale", "🛠️ CMF_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_industrial"
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

    def generate_industrial(self, ollama_connection, product_idea, id_category, design_language, material_cmf, id_presentation, prompt_count, temperature, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']
        
        # 视觉参考
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A sketch or reference is provided. Analyze its form factor and silhouette, then refine it into a professional industrial design.]" if img_b64 else ""

        # 知识提取
        cat_info = ID_CATEGORIES.get(id_category, "")
        lang_info = ID_DESIGN_LANGUAGES.get(design_language, "")
        cmf_info = ID_MATERIALS_CMF.get(material_cmf, "")
        pres_info = ID_PRESENTATION.get(id_presentation, "")

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Lead Industrial Designer and a KeyShot 3D Rendering Expert.
        You specialize in Product Design, CMF (Colors, Materials, Finishes), and Ergonomics.
        
        [PRODUCT BRIEF]
        Subject: "{product_idea}"
        {vis_ctx}
        
        [INDUSTRIAL DESIGN PARAMETERS]
        1. Category: {id_category} ({cat_info})
        2. Design Language: {design_language} ({lang_info})
        3. Material & CMF: {material_cmf} ({cmf_info})
        4. Presentation: {id_presentation} ({pres_info})
        
        [TASK]
        Generate {prompt_count} highly detailed prompts for AI image generation (Stable Diffusion/Midjourney).
        - Focus on form factor, parting lines, fillets/chamfers, and button interfaces.
        - Emphasize lighting interactions with the CMF (e.g., "specular highlight on anodized aluminum", "subsurface scattering on silicone").
        - NEVER use double quotes (") inside the prompt string. Use single quotes instead.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Explain the design language and why this form follows function.",
            "cmf_specs": "Technical breakdown of textures, finishes, and manufacturing details.",
            "prompts":["Prompt 1...", "Prompt 2...", ...],
            "negative": "Negative prompt (e.g., 'messy, impossible geometry, non-functional, text, watermark, organic when it should be mechanical')."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"🛠️ Lumina Industrial: Designing '{product_idea}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                prompts = res.get("prompts",[])
                analysis = res.get("analysis", "N/A")
                tech = res.get("cmf_specs", "N/A")
                neg = res.get("negative", "bad geometry, non-functional")
            except:
                print(f"⚠️ JSON Rescue Active")
                prompts = self.manual_extract(clean, "prompts")
                analysis = self.manual_extract(clean, "analysis")
                tech = self.manual_extract(clean, "cmf_specs")
                neg = self.manual_extract(clean, "negative")
                if not prompts: prompts = ["Error: Please check console."]

            if isinstance(prompts, str): prompts = [prompts]
            final_p = "\n\n".join([f"[{i+1}] {str(p)}" for i, p in enumerate(prompts)])
            
            return (final_p, str(analysis), str(tech), str(neg), clean)

        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")