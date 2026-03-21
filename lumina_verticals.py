import requests
import json
import re
from PIL import Image
import io
import base64
import torch
import numpy as np

# 导入垂直领域数据库
from .lumina_data import (
    INTERIOR_STYLES, ROOM_TYPES, SURFACE_MATERIALS, ARCH_LIGHTING,
    FASHION_STYLES, FABRIC_PROPERTIES, GARMENT_CUTS, FASHION_PRESENTATION,
    DETAIL_LEVELS, CAMERA_MOVEMENTS # 复用一些基础字典
)

# -----------------------------------------------------------------------------
# 🏛️ 1. 室内与空间架构大师 (Interior & Spatial Designer)
# -----------------------------------------------------------------------------
class LuminaInteriorNode:
    """
    v110.0 Interior & Spatial Designer
    Generates ArchViz (Architectural Visualization) level prompts.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        styles = sorted(list(INTERIOR_STYLES.keys()))
        rooms = sorted(list(ROOM_TYPES.keys()))
        mats = sorted(list(SURFACE_MATERIALS.keys()))
        lights = sorted(list(ARCH_LIGHTING.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "space_concept": ("STRING", {"default": "A quiet reading corner", "multiline": True}),
                "room_type": (rooms, {"default": "🛋️ Living Room / Lounge[客厅/休息室]"}),
                "interior_style": (styles, {"default": "🏛️ Japandi (Zen Modern) [侘寂/北欧禅宗]"}),
                "surface_material": (mats, {"default": "🧱 Micro-cement & Travertine [微水泥/洞石]"}),
                "arch_lighting": (lights, {"default": "💡 Golden Hour / Sunbeams [自然光/丁达尔]"}),
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.65}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": { "image_input": ("IMAGE",) } # 支持看参考图定材质
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 ArchViz_Prompts", "📐 Spatial_Analysis", "🧪 Material_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_interior"
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

    def generate_interior(self, ollama_connection, space_concept, room_type, interior_style, surface_material, arch_lighting, prompt_count, temperature, seed, image_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A spatial reference provided. Extract lighting, layout, and materiality from it.]" if img_b64 else ""

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Pritzker-winning Architect and a Master ArchViz (Architectural Visualization) Artist.
        You generate highly photorealistic interior design prompts for Unreal Engine / Corona Render.
        
        [DESIGN BRIEF]
        Space: "{space_concept}"
        {vis_ctx}
        
        [ARCHITECTURAL PARAMETERS]
        1. Room Type: {room_type} ({ROOM_TYPES.get(room_type, "")})
        2. Aesthetic Style: {interior_style} ({INTERIOR_STYLES.get(interior_style, "")})
        3. Core Materiality: {surface_material} ({SURFACE_MATERIALS.get(surface_material, "")})
        4. Lighting Design: {arch_lighting} ({ARCH_LIGHTING.get(arch_lighting, "")})
        
        [TASK]
        Generate {prompt_count} CG-level image prompts.
        - Emphasize "Global Illumination", "Raytracing", "Photorealism".
        - Describe how light interacts with the specific surface materials (e.g. caustics, diffuse reflection).
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Explain the interior layout and mood.",
            "material_specs": "Technical ArchViz renderer settings.",
            "prompts": ["Prompt 1...", "Prompt 2..."],
            "negative": "ugly, deformed, mutated, unrealistic, bad geometry..."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            r = requests.post(url, json=payload, timeout=240)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p, a, t, n = res.get("prompts",[]), res.get("analysis", ""), res.get("material_specs", ""), res.get("negative", "low quality")
            except:
                p = self.manual_extract(clean, "prompts")
                a, t, n = "Error", "Error", "Error"
                if not p: p = ["Error"]
            
            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            return (final_p, str(a), str(t), str(n), clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")


# -----------------------------------------------------------------------------
# 👗 2. 高定服装与布料解构师 (Fashion & Textile Engineer)
# -----------------------------------------------------------------------------
class LuminaFashionNode:
    """
    v110.0 Fashion & Textile Engineer
    Generates high-fashion lookbooks with accurate fabric physics.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        styles = sorted(list(FASHION_STYLES.keys()))
        fabrics = sorted(list(FABRIC_PROPERTIES.keys()))
        cuts = sorted(list(GARMENT_CUTS.keys()))
        pres = sorted(list(FASHION_PRESENTATION.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "garment_concept": ("STRING", {"default": "A dress inspired by deep sea creatures", "multiline": True}),
                "fashion_style": (styles, {"default": "👗 Haute Couture (Avant-Garde) [前卫高定]"}),
                "fabric_physics": (fabrics, {"default": "🧵 Iridescent Silk / Satin [流光丝绸]"}),
                "tailoring_cut": (cuts, {"default": "✂️ Asymmetrical Draping [不对称垂坠]"}),
                "presentation": (pres, {"default": "📸 High-Fashion Runway [高定大秀]"}),
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.65}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": { "image_input": ("IMAGE",) } # 换装参考
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Fashion_Prompts", "🧠 Couture_Analysis", "🧵 Textile_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_fashion"
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

    def generate_fashion(self, ollama_connection, garment_concept, fashion_style, fabric_physics, tailoring_cut, presentation, prompt_count, temperature, seed, image_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A fashion reference provided. Emulate its drape and silhouette.]" if img_b64 else ""

        sys_prompt = f"""[SYSTEM ROLE]
        You are the Creative Director of a luxury fashion house (like Margiela or Balenciaga) and an expert Textile Engineer.
        
        [DESIGN BRIEF]
        Concept: "{garment_concept}"
        {vis_ctx}
        
        [HAUTE COUTURE PARAMETERS]
        1. Fashion Style: {fashion_style} ({FASHION_STYLES.get(fashion_style, "")})
        2. Fabric & Physics: {fabric_physics} ({FABRIC_PROPERTIES.get(fabric_physics, "")})
        3. Tailoring & Cut: {tailoring_cut} ({GARMENT_CUTS.get(tailoring_cut, "")})
        4. Presentation: {presentation} ({FASHION_PRESENTATION.get(presentation, "")})
        
        [TASK]
        Generate {prompt_count} hyper-detailed prompts for AI generation.
        - You MUST heavily describe how the FABRIC folds, stretches, shines, or drapes over the body.
        - Use professional fashion terms (e.g. silhouette, hemline, bodice, pleats, specular highlight).[OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Design philosophy and silhouette intent.",
            "textile_specs": "Technical details of how the material reacts to light.",
            "prompts":["Prompt 1...", "Prompt 2..."],
            "negative": "ugly, deformed, bad anatomy, flat texture, casual wear..."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] =[img_b64]

        try:
            r = requests.post(url, json=payload, timeout=240)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p, a, t, n = res.get("prompts",[]), res.get("analysis", ""), res.get("textile_specs", ""), res.get("negative", "low quality")
            except:
                p = self.manual_extract(clean, "prompts")
                a, t, n = "Error", "Error", "Error"
                if not p: p = ["Error"]
            
            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            return (final_p, str(a), str(t), str(n), clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")

# 导入美发相关数据
from .lumina_data import (
    HAIR_STYLES, HAIR_TEXTURES, HAIR_COLORS, HAIR_PRESENTATION
)

# -----------------------------------------------------------------------------
# ✂️ 3. 顶奢发型与造型师 (Haute Coiffure & Hair Design)
# -----------------------------------------------------------------------------
class LuminaHairDesignNode:
    """
    v120.0 Haute Coiffure Designer
    Generates high-end beauty editorials and specific hair structure prompts.
    Focuses on strand physics, anisotropic reflection, and dye techniques.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        styles = sorted(list(HAIR_STYLES.keys()))
        textures = sorted(list(HAIR_TEXTURES.keys()))
        colors = sorted(list(HAIR_COLORS.keys()))
        presentations = sorted(list(HAIR_PRESENTATION.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "subject_desc": ("STRING", {"default": "A high fashion model with sharp cheekbones", "multiline": True, "placeholder": "Describe the character's face/vibe..."}),
                
                # 核心美发参数
                "hair_cut": (styles, {"default": "✂️ Classic Bob / Lob[经典波波头/长波波]"}),
                "hair_texture": (textures, {"default": "🧬 Glass Hair / Sleek Straight [镜面直发/极致顺滑]"}),
                "dye_technique": (colors, {"default": "🎨 Seamless Balayage [无痕画染/渐层扫染]"}),
                
                # 摄影与展示
                "presentation": (presentations, {"default": "📸 Editorial Beauty Portrait[美妆大片特写]"}),
                
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.65}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": { "image_input": ("IMAGE",) } # 支持看参考图模仿发型
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Beauty_Prompts", "🧠 Styling_Notes", "🧬 Physics_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_hair"
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

    def generate_hair(self, ollama_connection, subject_desc, hair_cut, hair_texture, dye_technique, presentation, prompt_count, temperature, seed, image_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A reference image provided. Pay close attention to how the hair behaves and captures light in this image, and incorporate that vibe.]" if img_b64 else ""

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Celebrity Hairstylist (like Chris Appleton) and an Elite Beauty Editorial Photographer.
        You specialize in generating hyper-realistic text-to-image prompts focusing on hair architecture, strand physics, and beauty lighting.
        
        [SUBJECT BRIEF]
        Character: "{subject_desc}"
        {vis_ctx}
        
        [SALON SPECIFICATIONS]
        1. Cut & Silhouette: {hair_cut} ({HAIR_STYLES.get(hair_cut, "")})
        2. Texture & Physics: {hair_texture} ({HAIR_TEXTURES.get(hair_texture, "")})
        3. Color & Technique: {dye_technique} ({HAIR_COLORS.get(dye_technique, "")})
        4. Photography: {presentation} ({HAIR_PRESENTATION.get(presentation, "")})
        
        [TASK]
        Generate {prompt_count} CG-level or Editorial-level image prompts.
        - **MANDATORY**: Use advanced rendering/photography terms for hair: "anisotropic highlights", "strand scattering", "individual hair details", "flyaways", "subsurface scattering on skin".
        - Describe how the color catches the light based on the Dye Technique.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Explain the aesthetic synergy between the cut, texture, and color.",
            "physics_specs": "Technical keywords describing light interaction with the hair strands.",
            "prompts":["Prompt 1...", "Prompt 2..."],
            "negative": "ugly, bald, helmet hair, plastic hair, merged strands, flat lighting, bad anatomy..."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            r = requests.post(url, json=payload, timeout=240)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p, a, t, n = res.get("prompts",[]), res.get("analysis", ""), res.get("physics_specs", ""), res.get("negative", "low quality")
            except:
                p = self.manual_extract(clean, "prompts")
                a, t, n = "Error", "Error", "Error"
                if not p: p = ["Error"]
            
            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            return (final_p, str(a), str(t), str(n), clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")

# 导入文创设计相关数据
from .lumina_data import (
    CULTURAL_PRODUCTS, CULTURAL_THEMES, CULTURAL_CRAFTS, MERCH_PRESENTATION
)

# -----------------------------------------------------------------------------
# 🎁 4. 博物馆艺术总监与潮玩设计师 (Cultural Merch & Art Toy Designer)
# -----------------------------------------------------------------------------
class LuminaCulturalDesignNode:
    """
    v130.0 Cultural Merch & Art Toy Designer
    Generates prompts for Blind Boxes, Enamel Pins, Museum Souvenirs, and Guochao products.
    Focuses on material craftsmanship (PVC, Enamel, Porcelain) and IP integration.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        formats = sorted(list(CULTURAL_PRODUCTS.keys()))
        themes = sorted(list(CULTURAL_THEMES.keys()))
        crafts = sorted(list(CULTURAL_CRAFTS.keys()))
        presentations = sorted(list(MERCH_PRESENTATION.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "ip_concept": ("STRING", {"default": "A cute tiger drinking boba tea", "multiline": True, "placeholder": "The core character or object..."}),
                
                # 核心文创参数
                "product_format": (formats, {"default": "🎁 Art Toy / Blind Box [潮玩盲盒公仔]"}),
                "cultural_theme": (themes, {"default": "🏮 Modern Guochao (Cyber-Folk)[赛博国潮]"}),
                "material_craft": (crafts, {"default": "🛠️ Glossy PVC / Vinyl [高光PVC/搪胶材质]"}),
                
                # 摄影与展示
                "merch_presentation": (presentations, {"default": "📸 Studio Product Shot[影棚白底/纯色底特写]"}),
                
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.65}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": { "image_input": ("IMAGE",) } # 支持看参考图/Logo生成周边
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Merch_Prompts", "🧠 IP_Strategy", "🛠️ Craft_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_merch"
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

    def generate_merch(self, ollama_connection, ip_concept, product_format, cultural_theme, material_craft, merch_presentation, prompt_count, temperature, seed, image_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A reference IP image or pattern is provided. Apply this visual identity to the merchandise.]" if img_b64 else ""

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Top-tier Museum Art Director and a Lead Product Designer at Pop Mart.
        You specialize in turning cultural concepts and IPs into highly desirable commercial merchandise, art toys, and souvenirs.
        
        [IP / CONCEPT BRIEF]
        Idea: "{ip_concept}"
        {vis_ctx}
        
        [MERCHANDISE SPECIFICATIONS]
        1. Product Format: {product_format} ({CULTURAL_PRODUCTS.get(product_format, "")})
        2. Cultural Theme: {cultural_theme} ({CULTURAL_THEMES.get(cultural_theme, "")})
        3. Material & Craft: {material_craft} ({CULTURAL_CRAFTS.get(material_craft, "")})
        4. Presentation: {merch_presentation} ({MERCH_PRESENTATION.get(merch_presentation, "")})
        
        [TASK]
        Generate {prompt_count} CG-level or macro-photography image prompts for Stable Diffusion/Midjourney.
        - **MANDATORY**: Accurately describe the physical limitations and textures of the format (e.g., if it's an Enamel Pin, describe the raised metal lines; if it's a Blind Box, describe the chibi proportions and base).
        - Blend the Cultural Theme seamlessly with the Concept.[OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Explain how the cultural theme was commercialized into this specific product format.",
            "craft_specs": "Technical keywords describing the material rendering (e.g., Octane render, SSS, metallic reflection).",
            "prompts":["Prompt 1...", "Prompt 2..."],
            "negative": "ugly, deformed, messy, abstract, flat painting, bad anatomy..."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            r = requests.post(url, json=payload, timeout=240)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p, a, t, n = res.get("prompts",[]), res.get("analysis", ""), res.get("craft_specs", ""), res.get("negative", "low quality")
            except:
                p = self.manual_extract(clean, "prompts")
                a, t, n = "Error", "Error", "Error"
                if not p: p = ["Error"]
            
            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            return (final_p, str(a), str(t), str(n), clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")