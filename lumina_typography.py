import requests
import json
import re
import numpy as np
from PIL import Image
import io
import base64
import torch

# 导入全量数据 (v26版)
from .lumina_data import (
    TYPO_FONT_FAMILIES,
    TYPO_CONSTRUCTION,
    TYPO_GRAVITY,
    TYPO_COUNTER,
    TYPO_PROPORTIONS,
    TYPO_MATERIALS,
    TYPO_CONTEXTS,
    TYPO_FUSIONS
)

class LuminaTypographyNode:
    """
    v27.0 Typography Vision Edition
    - Added Image Input for visual reference analysis.
    - Uses Vision Models (LLaVA/Qwen-VL) to extract color/texture/mood.
    - Integrates with Micro-Surgery parameters.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        # 排序所有列表
        fonts = sorted(list(TYPO_FONT_FAMILIES.keys()))
        constructions = sorted(list(TYPO_CONSTRUCTION.keys()))
        gravities = sorted(list(TYPO_GRAVITY.keys()))
        counters = sorted(list(TYPO_COUNTER.keys()))
        proportions = sorted(list(TYPO_PROPORTIONS.keys()))
        materials = sorted(list(TYPO_MATERIALS.keys()))
        contexts = sorted(list(TYPO_CONTEXTS.keys()))
        fusions = sorted(list(TYPO_FUSIONS.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 核心内容
                "text_content": ("STRING", {"default": "Design", "placeholder": "Text/Character..."}),
                
                # 2. 骨架与基因
                "font_family": (fonts, {"default": "🅰️ Helvetica / Neo-Grotesque [新哥特/瑞士]"}),
                "construction_logic": (constructions, {"default": "✒️ Geometric / Drafting [尺规作图]"}),
                
                # 3. 微观整形 (Micro-Surgery)
                "structure_gravity": (gravities, {"default": "⏺️ Geometric Center [绝对居中]"}),
                "structure_counter": (counters, {"default": "⚖️ Balanced [中宫适中]"}),
                
                # 4. 空间与皮肤
                "proportion_rule": (proportions, {"default": "📐 Golden Ratio (1:1.618) [黄金分割]"}),
                "material_fx": (materials, {"default": "✒️ Vector / Flat [平面矢量]"}),
                
                # 5. 上下文与融合
                "design_context": (contexts, {"default": "📢 Brand Identity (Logo) [品牌标志]"}),
                "fusion_mode": (fusions, {"default": "⚗️ None (Pure Style) [纯粹风格]"}),
                
                # 6. 控制
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.6}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                # --- NEW: 图像输入接口 ---
                "image_input": ("IMAGE",), 
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Prompts_List", "🧠 Design_Rationale", "🧪 Structure_Specs", "📝 Negative", "⚙️ Raw_JSON")
    
    FUNCTION = "generate_typography" 
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image_tensor):
        try:
            # ComfyUI Image is [Batch, H, W, C]
            # Take the first image in the batch
            i = 255. * image_tensor[0].cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode("utf-8")
        except Exception as e:
            print(f"Image Encode Error: {e}")
            return None

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def generate_typography(self, ollama_connection, text_content, font_family, construction_logic, structure_gravity, structure_counter, proportion_rule, design_context, material_fx, fusion_mode, prompt_count, temperature, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']

        # 1. 处理图像
        image_b64 = None
        has_image = False
        if image_input is not None:
            image_b64 = self.tensor_to_base64(image_input)
            if image_b64: has_image = True

        # 2. 检索知识
        font_info = TYPO_FONT_FAMILIES.get(font_family, "")
        construct_info = TYPO_CONSTRUCTION.get(construction_logic, "")
        gravity_info = TYPO_GRAVITY.get(structure_gravity, "")
        counter_info = TYPO_COUNTER.get(structure_counter, "")
        prop_info = TYPO_PROPORTIONS.get(proportion_rule, "")
        mat_info = TYPO_MATERIALS.get(material_fx, "")
        ctx_info = TYPO_CONTEXTS.get(design_context, "")
        fusion_info = TYPO_FUSIONS.get(fusion_mode, "")

        # 3. 构建“视觉设计总监” System Prompt
        system_prompt = f"""
        [SYSTEM ROLE]
        You are a Master Typography Designer and Visual Art Director.
        You integrate theoretical type design (Structure/Gravity/Counter) with visual analysis.
        
        [INPUT DATA]
        - Text Content: "{text_content}"
        - Visual Reference Provided: {'YES' if has_image else 'NO'}
        
        [VISUAL ANALYSIS INSTRUCTION]
        If a visual reference is provided:
        1. Analyze its Color Palette, Texture, and Mood.
        2. Adapt the typography prompts to MATCH or COMPLEMENT this visual style.
        3. Example: If image is a rusty wall, suggest "rusted metal texture" or "eroded edges".
        
        [MICRO-STRUCTURE CONFIGURATION]
        1. SKELETON: {font_family} ({font_info})
        2. GENESIS: {construction_logic} ({construct_info})
        3. GRAVITY: {structure_gravity} ({gravity_info})
        4. COUNTER: {structure_counter} ({counter_info})
        
        [DESIGN EXECUTION]
        5. MATERIAL: {material_fx} ({mat_info})
        6. CONTEXT: {design_context} ({ctx_info})
        7. FUSION: {fusion_mode} ({fusion_info})
        
        [TASK]
        Generate {prompt_count} detailed image generation prompts.
        Combine the Visual Reference (if any) with the Typography Theory.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Explain how you integrated the reference image (if provided) with the structure settings.",
            "structure_specs": "Technical description of the font anatomy and visual integration.",
            "prompts": ["Prompt 1...", "Prompt 2...", ...],
            "negative": "Negative prompt."
        }}
        """

        # 4. API Payload
        payload = {
            "model": model,
            "prompt": system_prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}
        }
        if has_image: 
            payload["images"] = [image_b64]
            print(f"👁️ Lumina Vision: Analyzing reference image with {model}...")

        try:
            print(f"🔠 Typo Vision: Designing '{text_content}' with Gravity:{structure_gravity}...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                prompts = res.get("prompts", [])
                analysis = res.get("analysis", "N/A")
                tech = res.get("structure_specs", "N/A")
                neg = res.get("negative", "low quality")
            except:
                print(f"⚠️ JSON Rescue Active")
                prompts = self.manual_extract(clean, "prompts")
                analysis = self.manual_extract(clean, "analysis")
                tech = self.manual_extract(clean, "structure_specs")
                neg = self.manual_extract(clean, "negative")
                if not prompts: prompts = [f"Error: {clean}"]

            if isinstance(prompts, str): prompts = [prompts]
            final_p = "\n\n".join([f"[{i+1}] {str(p)}" for i, p in enumerate(prompts)])
            
            return (final_p, str(analysis), str(tech), str(neg), clean)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")