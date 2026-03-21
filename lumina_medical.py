import requests
import json
import re
from PIL import Image
import io
import base64
import torch
import numpy as np

# 导入医学数据库
from .lumina_data import (
    MED_SYSTEMS,
    MED_IMAGING,
    MED_STYLES,
    MED_SCALES
)

class LuminaMedicalNode:
    """
    v140.0 Lumina Medical & Anatomy Expert
    Generates highly professional bio-medical illustrations, CGI renderings, and anatomical sketches.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        systems = sorted(list(MED_SYSTEMS.keys()))
        imaging = sorted(list(MED_IMAGING.keys()))
        styles = sorted(list(MED_STYLES.keys()))
        scales = sorted(list(MED_SCALES.keys()))

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 科研/解剖主题
                "medical_concept": ("STRING", {"default": "A virus attacking a healthy cell", "multiline": True, "placeholder": "Describe the medical, biological, or anatomical subject..."}),
                
                # 2. 专业参数
                "anatomical_system": (systems, {"default": "🧬 Cellular & Molecular [细胞与分子]"}),
                "imaging_technique": (imaging, {"default": "🔬 3D Bio-Render (CGI) [3D生物渲染]"}),
                "illustration_style": (styles, {"default": "🎨 Classic Textbook (Netter) [经典教科书插画]"}),
                "scale_focus": (scales, {"default": "🔍 Microscopic (Tissue/Cell) [微观/细胞组织]"}),
                
                # 3. 控制
                "prompt_count": ("INT", {"default": 3, "min": 1, "max": 10}),
                "temperature": ("FLOAT", {"default": 0.6, "min": 0.1, "max": 1.0, "tooltip": "Keep slightly lower for scientific accuracy"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "image_input": ("IMAGE",), # 可上传真实的X光片或草图让AI分析
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Medical_Prompts", "🧠 Scientific_Rationale", "🧪 Rendering_Specs", "📝 Negative", "⚙️ Raw_JSON")
    FUNCTION = "generate_medical"
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

    def generate_medical(self, ollama_connection, medical_concept, anatomical_system, imaging_technique, illustration_style, scale_focus, prompt_count, temperature, seed, image_input=None):
        
        url, model = ollama_connection['url'], ollama_connection['model']
        
        # 视觉参考
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: A reference scan or diagram is provided. Integrate its core visual geometry into the prompt.]" if img_b64 else ""

        # 知识提取
        sys_info = MED_SYSTEMS.get(anatomical_system, "")
        img_info = MED_IMAGING.get(imaging_technique, "")
        sty_info = MED_STYLES.get(illustration_style, "")
        scl_info = MED_SCALES.get(scale_focus, "")

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Chief Medical Illustrator (CMI) and a Scientific Visualization Expert.
        You specialize in creating hyper-accurate, visually stunning prompts for anatomical, biological, and medical imagery.
        
        [SCIENTIFIC BRIEF]
        Subject: "{medical_concept}"
        {vis_ctx}
        
        [VISUALIZATION PARAMETERS]
        1. System: {anatomical_system} ({sys_info})
        2. Imaging Technique: {imaging_technique} ({img_info})
        3. Artistic Style: {illustration_style} ({sty_info})
        4. Scale: {scale_focus} ({scl_info})
        
        [TASK]
        Generate {prompt_count} detailed image generation prompts for AI (like Stable Diffusion/Midjourney).
        - Use accurate clinical and biological terminology (e.g., myocardium, lipid bilayer, volumetric scattering).
        - Explicitly describe the TEXTURE (e.g., wet, porous, glowing, metallic) and LIGHTING.
        - NEVER use double quotes (") inside the prompt string. Use single quotes instead.
        
        [OUTPUT FORMAT - JSON ONLY]
        {{
            "analysis": "Brief scientific and aesthetic rationale for the prompt.",
            "render_specs": "Technical renderer settings (e.g., SSS, Octane, Electron beam logic).",
            "prompts":["Prompt 1...", "Prompt 2...", ...],
            "negative": "Negative prompt (e.g., 'bad anatomy, text, labels, watermark, cartoon, inaccurate')."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            print(f"🧬 Lumina Medical: Visualizing '{medical_concept}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                prompts = res.get("prompts",[])
                analysis = res.get("analysis", "N/A")
                tech = res.get("render_specs", "N/A")
                neg = res.get("negative", "bad anatomy, mutated, unrealistic")
            except:
                print(f"⚠️ JSON Rescue Active")
                prompts = self.manual_extract(clean, "prompts")
                analysis = self.manual_extract(clean, "analysis")
                tech = self.manual_extract(clean, "render_specs")
                neg = self.manual_extract(clean, "negative")
                if not prompts: prompts = ["Error: Please check console."]

            if isinstance(prompts, str): prompts = [prompts]
            final_p = "\n\n".join([f"[{i+1}] {str(p)}" for i, p in enumerate(prompts)])
            
            return (final_p, str(analysis), str(tech), str(neg), clean)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")