import requests
import json
import re
from PIL import Image
import io
import base64

# 导入全量数据
from .lumina_data import (
    CIVILIZATION_LEVELS,
    MAGIC_SYSTEMS,
    WORLD_GEOGRAPHY,
    WORLD_POLITICS,
    WORLD_ELEMENTS,
    WORLD_TYPES,
)

class LuminaWorldNode:
    """
    v61.0 Lumina World Builder (Demiurge Edition)
    Generates Lore, Geography, and Asset prompts based on deep world-building theory.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        # 排序
        civs = sorted(list(CIVILIZATION_LEVELS.keys()))
        magics = sorted(list(MAGIC_SYSTEMS.keys()))
        geos = sorted(list(WORLD_GEOGRAPHY.keys()))
        pols = sorted(list(WORLD_POLITICS.keys()))
        elements = sorted(list(WORLD_ELEMENTS.keys()))
        
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 1. 创世核心
                "world_concept": ("STRING", {"default": "A floating steampunk empire running out of coal", "multiline": True, "placeholder": "The core idea..."}),
                
                # 2. 宏观设定 (Macro)
                "civilization_level": (civs, {"default": "🌍 Type 0: Pre-Industrial [前工业文明]"}),
                "geography_biome": (geos, {"default": "🗺️ Floating Islands [浮空岛]"}),
                "power_system": (magics, {"default": "🔮 Magitech / Hextech [魔导科技]"}),
                "political_structure": (pols, {"default": "👑 Theocracy / Cult [神权统治]"}),
                
                # 3. 微观产出 (Micro)
                "asset_focus": (elements, {"default": "🗺️ Map & Geography [地图/地理]"}),
                
                "temperature": ("FLOAT", {"default": 0.75}), # Higher temp for creativity
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "image_input": ("IMAGE",), # 视觉灵感
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Asset_Prompt", "📜 World_Bible (Lore)", "🧠 Design_Notes", "⚙️ Raw_JSON")
    FUNCTION = "build_world"
    CATEGORY = "Lumina_AI/Advisors"

    def tensor_to_base64(self, image):
        try:
            i = 255. * image[0].cpu().numpy()
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

    def build_world(self, ollama_connection, world_concept, civilization_level, geography_biome, power_system, political_structure, asset_focus, temperature, seed, image_input=None):
        url, model = ollama_connection['url'], ollama_connection['model']
        
        img_b64 = self.tensor_to_base64(image_input) if image_input is not None else None
        vis_ctx = "[Visual Input: Image provided. Extract architectural style and mood for the world.]" if img_b64 else ""

        # 检索知识
        civ_info = CIVILIZATION_LEVELS.get(civilization_level, "")
        geo_info = WORLD_GEOGRAPHY.get(geography_biome, "")
        magic_info = MAGIC_SYSTEMS.get(power_system, "")
        pol_info = WORLD_POLITICS.get(political_structure, "")
        elem_info = WORLD_ELEMENTS.get(asset_focus, "")

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are a Legendary World Builder and Game Designer (Tolkien/Kojima level).
        
        [WORLD SEED]
        Concept: "{world_concept}"
        {vis_ctx}
        
        [MACRO SETTINGS]
        1. Civ Level: {civilization_level} ({civ_info})
        2. Geography: {geography_biome} ({geo_info})
        3. Power/Magic: {power_system} ({magic_info})
        4. Politics: {political_structure} ({pol_info})
        
        [TASK]
        1. Synthesize these elements into a cohesive "World Bible" excerpt.
        2. Generate a high-fidelity image prompt for the requested ASSET FOCUS: {asset_focus}.
           - If Map: Top-down, parchment/hologram style.
           - If Item: Isometric, isolated, detailed texture.
           - If Location: Wide shot, atmospheric.
        
        [OUTPUT JSON]
        {{
            "lore": "Flavor text describing the world history/setting...",
            "asset_prompt": "Visual generation prompt for the asset...",
            "design_notes": "Logic behind the combination of magic, tech, and politics."
        }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}, "images": [img_b64] if img_b64 else []}
        
        try:
            r = requests.post(url, json=payload, timeout=120)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p, l, n = res.get("asset_prompt", ""), res.get("lore", ""), res.get("design_notes", "")
            except:
                p = self.manual_extract(clean, "asset_prompt")
                l = self.manual_extract(clean, "lore")
                n = "Error"
            return (p, l, n, clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err")