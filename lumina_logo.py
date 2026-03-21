import requests
import json
import re
from PIL import Image
import io
import base64

# 导入全量数据
from .lumina_data import (
    LOGO_TYPES,
    LOGO_STYLES,
    LOGO_GEOMETRY, # New
    LOGO_COLORS,   # New
    BRAND_ARCHETYPES,
    LOGO_INDUSTRIES
)

class LuminaLogoNode:
    """
    v42.0 Lumina Symbol Master (Ultimate Logo)
    Integrates Geometry, Color Psychology, and Gestalt Principles.
    Generates professional, vector-ready logo prompts.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        types = sorted(list(LOGO_TYPES.keys()))
        styles = sorted(list(LOGO_STYLES.keys()))
        geoms = sorted(list(LOGO_GEOMETRY.keys()))
        colors = sorted(list(LOGO_COLORS.keys()))
        archetypes = sorted(list(BRAND_ARCHETYPES.keys()))
        industries = sorted(list(LOGO_INDUSTRIES.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 品牌简报 (The Brief)
                "brand_name": ("STRING", {"default": "Lumina", "placeholder": "Brand Name..."}),
                "brand_industry": (industries, {"default": "💻 Tech & SaaS [科技软件]"}),
                "brand_archetype": (archetypes, {"default": "🎨 The Creator [创造者]"}),
                
                # 2. 设计策略 (The Strategy)
                "logo_type": (types, {"default": "🛡️ Pictorial Mark (Icon) [具象图形标]"}),
                "design_style": (styles, {"default": "🎨 Swiss Minimalist [瑞士极简]"}),
                
                # 3. 深度构造 (The Construction - Professional)
                "geometry_logic": (geoms, {"default": "📐 Golden Ratio Circles [黄金圆切]"}),
                "color_psychology": (colors, {"default": "🎨 Trust & Security (Blue) [信任/安全]"}),
                
                # 4. 控制
                "prompt_count": ("INT", {"default": 4, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.6}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "image_input": ("IMAGE",), # 草图/参考图
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Prompts_List", "🧠 Design_Rationale", "🧪 Vector_Specs", "📝 Negative", "⚙️ Raw_JSON")
    
    FUNCTION = "generate_logo" 
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

    def generate_logo(self, ollama_connection, brand_name, brand_industry, logo_type, design_style, geometry_logic, color_psychology, brand_archetype, prompt_count, temperature, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']

        # 1. 视觉参考
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A sketch or reference provided. Refine this shape into a professional vector logo.]" if img_b64 else ""

        # 2. 检索知识
        type_info = LOGO_TYPES.get(logo_type, "")
        style_info = LOGO_STYLES.get(design_style, "")
        geom_info = LOGO_GEOMETRY.get(geometry_logic, "")
        color_info = LOGO_COLORS.get(color_psychology, "")
        arch_info = BRAND_ARCHETYPES.get(brand_archetype, "")
        ind_info = LOGO_INDUSTRIES.get(brand_industry, "")

        # 3. System Prompt (强调矢量、几何、格式塔)
        system_prompt = f"""
        [SYSTEM ROLE]
        You are a Chief Design Officer (Pentagram/Landor level).
        You specialize in creating timeless, scalable, and geometrically perfect logos.
        
        [BRAND BRIEF]
        - Brand: "{brand_name}"
        - Industry: {brand_industry} ({ind_info})
        - Archetype: {brand_archetype} ({arch_info})
        {vis_ctx}
        
        [DESIGN PARAMETERS]
        1. Type: {logo_type} ({type_info})
        2. Style: {design_style} ({style_info})
        3. Geometry: {geometry_logic} ({geom_info})
           *Crucial*: Apply this geometric rule to the shape construction.
        4. Color: {color_psychology} ({color_info})
        
        [TASK]
        Generate {prompt_count} distinct logo generation prompts.
        
        [CRITICAL CONSTRAINTS FOR AI GENERATION]
        1. MANDATORY: "white background", "vector style", "flat design", "2d", "minimalist", "clean lines".
        2. FORBIDDEN: "photorealistic", "shading", "complex details", "3d render" (unless Style is 3D), "text" (unless Wordmark).
        3. FORMAT: "A [Type] logo for [Brand], [Subject], [Geometry/Style keywords], [Color], white background, vector."
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Explain the concept, focusing on how geometry and archetype meet.",
            "technical_specs": "Vector settings (e.g. Adobe Illustrator, SVG, Hex Colors, Grid).",
            "prompts": ["Prompt 1...", "Prompt 2...", ...],
            "negative": "Specific negative prompt (e.g. 'realistic, photo, complex, shadow')."
        }}
        """

        payload = {
            "model": model,
            "prompt": system_prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}
        }
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"🛡️ Lumina Logo v42: Designing '{brand_name}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                prompts = res.get("prompts", [])
                analysis = res.get("analysis", "N/A")
                tech = res.get("technical_specs", "N/A")
                neg = res.get("negative", "low quality, watermark, text, realistic, photo")
            except:
                print(f"⚠️ JSON Rescue Active")
                prompts = self.manual_extract(clean, "prompts")
                analysis = self.manual_extract(clean, "analysis")
                tech = self.manual_extract(clean, "technical_specs")
                neg = self.manual_extract(clean, "negative")
                if not prompts: prompts = ["Error"]

            if isinstance(prompts, str): prompts = [prompts]
            final_p = "\n\n".join([f"[{i+1}] {str(p)}" for i, p in enumerate(prompts)])
            
            return (final_p, str(analysis), str(tech), str(neg), clean)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")