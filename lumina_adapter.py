import requests
import json
import re

from .lumina_data import TARGET_MODELS

class LuminaAdapterNode:
    """
    v61.0 Lumina Prompt Adapter (Polyglot)
    Translates prompts for specific architectures (Pony, Flux, MJ, SDXL).
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        targets = sorted(list(TARGET_MODELS.keys()))
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "original_prompt": ("STRING", {"default": "A girl sitting in a cyber cafe", "multiline": True}),
                "target_model": (targets, {"default": "🎨 FLUX.1 [通顺描述流]"}),
                
                # 增强控制
                "stylize_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "tooltip": "Adjust style intensity params (e.g. --s in MJ)"}),
                "temperature": ("FLOAT", {"default": 0.4}), 
                "seed": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("✨ Adapted_Prompt", "🧠 Logic_Explanation", "⚙️ Raw_JSON")
    FUNCTION = "adapt_prompt"
    CATEGORY = "Lumina_AI/Utils"

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def adapt_prompt(self, ollama_connection, original_prompt, target_model, stylize_strength, temperature, seed):
        url, model = ollama_connection['url'], ollama_connection['model']
        
        target_info = TARGET_MODELS.get(target_model, {})
        
        sys_prompt = f"""
        [ROLE] Senior Prompt Engineer.
        [TASK] Rewrite the input prompt perfectly for the TARGET MODEL architecture.
        
        [INPUT PROMPT]
        "{original_prompt}"
        
        [TARGET MODEL]
        Model: {target_model}
        Description: {target_info.get('desc')}
        STRATEGY: {target_info.get('strategy')}
        
        [ADJUSTMENT]
        Stylize Strength: {stylize_strength} (If MJ, adjust --s. If SD, adjust weight brackets).
        
        [INSTRUCTIONS]
        1. If Pony: Add 'score_9, score_8_up, score_7_up' at the start. Use tags.
        2. If Flux: Rewrite as a natural, detailed paragraph. Describe position/lighting.
        3. If Midjourney: Add '--v 6.0' at end.
        
        [OUTPUT JSON]
        {{
            "adapted_prompt": "The final prompt string ready for copy-paste...",
            "logic": "Why you made these changes (e.g. 'Added score tags for Pony')."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}}
        
        try:
            r = requests.post(url, json=payload, timeout=120)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p = res.get("adapted_prompt", "")
                l = res.get("logic", "")
            except:
                p = self.manual_extract(clean, "adapted_prompt")
                l = "Error"
            return (p, l, clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err")