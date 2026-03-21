import requests
import json
import re
from PIL import Image
import io
import base64
import torch
import numpy as np

class LuminaDeconstructorNode:
    """
    v90.0 Lumina Deconstructor (Reverse Engineering)
    Takes an input image and reverse-engineers its aesthetic DNA, 
    mapping it back to Lumina's specific styles, mediums, and prompts.
    REQUIRES A VISION MODEL (e.g., llava, llama3.2-vision, qwen-vl).
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "image_input": ("IMAGE",), # 必须输入图片
                "temperature": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 1.0, "tooltip": "Lower temperature for more accurate analytical extraction."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "custom_focus": ("STRING", {"default": "", "multiline": True, "placeholder": "E.g., Focus specifically on the lighting setup, or the brushstroke technique..."}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Reconstructed_Prompt", "🧬 Aesthetic_DNA", "🎨 Color_Palette", "🎛️ Lumina_Parameters", "⚙️ Raw_JSON")
    FUNCTION = "deconstruct_image"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image_tensor):
        try:
            if not isinstance(image_tensor, torch.Tensor): return None
            # 取第一帧
            i = 255. * image_tensor[0].cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=85) # 压缩以加快推理
            return base64.b64encode(buf.getvalue()).decode("utf-8")
        except Exception as e:
            print(f"Image Encode Error: {e}")
            return None

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def deconstruct_image(self, ollama_connection, image_input, temperature, seed, custom_focus=""):
        url, model = ollama_connection['url'], ollama_connection['model']
        
        img_b64 = self.tensor_to_base64(image_input)
        if not img_b64:
            return ("Error: No valid image provided.", "", "", "", "")

        focus_instruction = f"Additional Focus: {custom_focus}" if custom_focus else ""

        # 核心 System Prompt: 强制模型像艺术史学家和 CG 总监一样思考
        system_prompt = f"""
        [SYSTEM ROLE]
        You are a Master Art Forger, CG Supervisor, and Art Historian.
        Your supreme ability is to look at an image and REVERSE-ENGINEER its exact aesthetic DNA and technical parameters to recreate it using text-to-image AI.

        [TASK]
        Analyze the provided image deeply. Deconstruct it into specific, professional prompt engineering parameters.
        {focus_instruction}[DECONSTRUCTION FRAMEWORK]
        1. Subject & Composition: What is the focal point? What is the camera angle/lens?
        2. Aesthetic Movement: Is this Cyberpunk? Baroque? Ukiyo-e? Bauhaus? Be highly specific.
        3. Technical Medium: Was this shot on 35mm film? Rendered in Octane? Impasto oil painting? Polaroid?
        4. Lighting & Color: Chiaroscuro? Neon rim light? Complementary colors?
        5. The 'Soul' (MBTI Vibe): What is the psychological vibe? (e.g., INTJ cold logic, INFP dreamy melancholy, ESTP high-octane action).

        [OUTPUT FORMAT - STRICTLY JSON]
        {{
            "reconstructed_prompt": "A dense, highly detailed text-to-image prompt (comma separated tags or rich prose) that would perfectly recreate this image.",
            "aesthetic_dna": "A brief analysis of the Art Style, Lighting, and Vibe.",
            "color_palette": "List the dominant 5 Hex color codes and their visual names.",
            "lumina_parameters": "Suggest the best mapping for our system (e.g., Style:[Arch] Brutalism, Medium: [3D] Octane Render, MBTI: INTJ)."
        }}
        """

        payload = {
            "model": model,
            "prompt": system_prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": temperature, "seed": seed, "num_ctx": 4096},
            "images": [img_b64]
        }

        try:
            print(f"👁️ Lumina Deconstructor: Analyzing visual DNA with {model}...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw_text = r.json().get("response", "").strip()
            clean_text = re.sub(r'^```json\s*|```\s*$', '', raw_text).strip()
            
            try:
                res = json.loads(clean_text)
                prompt = res.get("reconstructed_prompt", "")
                dna = res.get("aesthetic_dna", "")
                colors = res.get("color_palette", "")
                params = res.get("lumina_parameters", "")
            except json.JSONDecodeError:
                print(f"⚠️ JSON Rescue Active in Deconstructor...")
                prompt = self.manual_extract(clean_text, "reconstructed_prompt")
                dna = self.manual_extract(clean_text, "aesthetic_dna")
                colors = self.manual_extract(clean_text, "color_palette")
                params = self.manual_extract(clean_text, "lumina_parameters")
                if not prompt: prompt = "Error parsing response."

            # 格式化美观输出
            formatted_dna = f"🧬 AESTHETIC DNA:\n{dna}"
            formatted_params = f"🎛️ SUGGESTED SETTINGS:\n{params}"

            return (str(prompt), formatted_dna, str(colors), formatted_params, clean_text)

        except Exception as e:
            return (f"Error: {str(e)}", "Err", "Err", "Err", "Err")