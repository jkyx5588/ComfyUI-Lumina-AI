import requests
import json
import re
from PIL import Image
import io
import base64

# 导入数据库
from .lumina_data import (
    PACK_TYPES,
    PACK_MATERIALS,
    PACK_FINISHES,
    PACK_CATEGORIES,
    PACK_VIEWS
)

class LuminaPackagingNode:
    """
    v70.0 Lumina Packaging Designer
    Generates professional product mockups with specific materials and printing finishes.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        types = sorted(list(PACK_TYPES.keys()))
        mats = sorted(list(PACK_MATERIALS.keys()))
        finishes = sorted(list(PACK_FINISHES.keys()))
        cats = sorted(list(PACK_CATEGORIES.keys()))
        views = sorted(list(PACK_VIEWS.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 产品核心
                "product_name": ("STRING", {"default": "Essence of Void", "placeholder": "Product Name..."}),
                "category": (cats, {"default": "💄 Cosmetics / Skincare [美妆护肤]"}),
                
                # 2. 包装结构与材质
                "package_type": (types, {"default": "📦 Bottle (Glass/Dropper) [滴管/玻璃瓶]"}),
                "material_base": (mats, {"default": "🛠️ Frosted Glass [磨砂玻璃]"}),
                
                # 3. 工艺与视角
                "print_finish": (finishes, {"default": "✨ Foil Stamping (Gold/Silver) [烫金/烫银]"}),
                "view_angle": (views, {"default": "📷 Front Studio Shot [正面特写]"}),
                
                # 4. 控制
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.6}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "image_input": ("IMAGE",), # Logo 或 纹理参考
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Prompts_List", "🧠 Design_Brief", "🛠️ Material_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_packaging"
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

    def generate_packaging(self, ollama_connection, product_name, category, package_type, material_base, print_finish, view_angle, prompt_count, temperature, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']
        
        # 视觉参考
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A Logo/Pattern is provided. Apply this design onto the packaging surface.]" if img_b64 else ""

        # 知识
        cat_info = PACK_CATEGORIES.get(category, "")
        type_info = PACK_TYPES.get(package_type, "")
        mat_info = PACK_MATERIALS.get(material_base, "")
        fin_info = PACK_FINISHES.get(print_finish, "")
        view_info = PACK_VIEWS.get(view_angle, "")

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Senior Packaging Designer and 3D Rendering Specialist.
        Your goal is to create hyper-realistic product mockup prompts.
        
        [PRODUCT BRIEF]
        - Product: "{product_name}"
        - Category: {category} ({cat_info})
        {vis_ctx}
        
        [TECHNICAL SPECS]
        1. Form: {package_type} ({type_info})
        2. Material: {material_base} ({mat_info})
        3. Finish: {print_finish} ({fin_info})
        4. Shot: {view_angle} ({view_info})
        
        [TASK]
        Generate {prompt_count} distinct prompts.
        - Focus on "Materiality": How light hits the glass/foil/paper.
        - Use CGI terms: "Octane render", "Raytracing", "Studio lighting", "Product photography".
        - Describe the Label Design relative to the container.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Design rationale based on category and material.",
            "material_specs": "Detailed texture and lighting keywords.",
            "prompts": ["Prompt 1...", "Prompt 2...", ...],
            "negative": "Negative prompt (e.g. 'bad quality, distorted logo, messy')."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}}
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"📦 Kaleido Packaging: Designing '{product_name}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                prompts = res.get("prompts", [])
                analysis = res.get("analysis", "N/A")
                tech = res.get("material_specs", "N/A")
                neg = res.get("negative", "low quality")
            except:
                print(f"⚠️ JSON Rescue Active")
                prompts = self.manual_extract(clean, "prompts")
                analysis = self.manual_extract(clean, "analysis")
                tech = self.manual_extract(clean, "material_specs")
                neg = self.manual_extract(clean, "negative")
                if not prompts: prompts = [f"Error: {clean}"]

            if isinstance(prompts, str): prompts = [prompts]
            final_p = "\n\n".join([f"[{i+1}] {str(p)}" for i, p in enumerate(prompts)])
            
            return (final_p, str(analysis), str(tech), str(neg), clean)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")