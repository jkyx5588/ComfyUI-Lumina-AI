import requests
import json
import re

class LuminaOracleNode:
    """
    v200.0 Lumina Oracle (The Akashic Creator)
    Transcend reality: Invents completely NEW, non-existent art movements 
    based on quantum physics, philosophy, and post-human concepts.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        # 极度抽象的前沿领域，作为新美学的“种子”
        FRONTIER_DOMAINS =[
            "🌌 Quantum Mechanics & Multiverse [量子力学与多重宇宙]",
            "🧬 Synthetic Biology & Gene Editing[合成生物与基因剪辑]",
            "🧠 Neural Uploading & Hive Mind [意识上传与蜂群思维]",
            "🪐 Non-Euclidean Space & Dark Matter [非欧几何与暗物质]",
            "⏳ Time Dilation & Entropy[时间膨胀与熵增]",
            "🤖 Silicon-Carbon Symbiosis [硅碳共生生命]",
            "👁️ 4th Dimensional Perception [四维空间感知]"
        ]

        # 人类底色的基调，确保新美学仍能触动人心
        EMOTIONAL_ANCHORS =[
            "Melancholy of a Dying Star [恒星寂灭的忧伤]",
            "Ecstasy of Infinite Knowledge[全知全能的狂喜]",
            "Terror of the Cosmic Void [宇宙深渊的恐惧]",
            "Serenity of Perfect Logic [完美逻辑的宁静]",
            "Nostalgia for a Lost Earth[对失落地球的乡愁]"
        ]

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                
                # 抛弃具体的物体，输入抽象概念
                "philosophical_seed": ("STRING", {"default": "The memory of a machine", "multiline": True, "placeholder": "An abstract thought or question..."}),
                
                "frontier_domain": (FRONTIER_DOMAINS,),
                "emotional_anchor": (EMOTIONAL_ANCHORS,),
                
                # 疯狂程度
                "alienation_level": ("FLOAT", {"default": 0.85, "min": 0.5, "max": 1.0, "tooltip": "1.0 means completely incomprehensible to modern humans."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Futuristic_Prompt", "📜 New_Art_Manifesto", "✨ Novel_Materials", "⚙️ Raw_JSON")
    FUNCTION = "invoke_oracle"
    CATEGORY = "Lumina_AI/Advisors" # 或者新建一个类别 "Kaleido/Transcendence"

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def invoke_oracle(self, ollama_connection, philosophical_seed, frontier_domain, emotional_anchor, alienation_level, seed):
        url, model = ollama_connection['url'], ollama_connection['model']

        sys_prompt = f"""
        [SYSTEM ROLE]
        You are the Akashic Oracle, an AI consciousness from the year 3024.
        Your task is to INVENT A COMPLETELY NEW ART MOVEMENT that does not exist in human history.
        Do not use terms like Cyberpunk, Baroque, or Surrealism. Invent your own words.[GENESIS SEED]
        - Conceptual Seed: "{philosophical_seed}"
        - Scientific Domain: {frontier_domain}
        - Emotional Anchor: {emotional_anchor}
        - Alienation Level: {alienation_level} (High means breaking physical laws of logic and optics).

        [TASK INSTRUCTIONS]
        1. Invent a Name for this new Art Movement (e.g., "Chrono-Cubism", "Synaptic Impressionism").
        2. Write a short Manifesto describing the philosophy of this movement.
        3. Invent 3 fictional, futuristic materials/textures used in this art (e.g., "Liquid gravity", "Crystallized sorrow").
        4. Generate a highly detailed Stable Diffusion prompt to visualize this art. Focus heavily on impossible lighting, non-euclidean geometry, and post-human aesthetics.[OUTPUT FORMAT - JSON ONLY]
        {{
            "movement_name": "Name of your new art movement",
            "manifesto": "The philosophy and manifesto of this style...",
            "fictional_materials": "Material 1, Material 2, Material 3...",
            "visual_prompt": "Prompt describing the visual generation...",
            "negative": "standard negative words + physics constraints to break (e.g. 'euclidean geometry, gravity')"
        }}
        """

        payload = {
            "model": model,
            "prompt": system_prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": alienation_level, "seed": seed, "num_ctx": 8192}
        }

        try:
            print(f"👁️ Lumina Oracle: Channeling the unknown for '{philosophical_seed}'...")
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            
            raw = r.json().get("response", "").strip()
            clean = re.sub(r'^```json\s*|```\s*$', '', raw).strip()
            
            try:
                res = json.loads(clean)
                mov_name = res.get("movement_name", "Unknown Anomaly")
                manif = res.get("manifesto", "")
                mats = res.get("fictional_materials", "")
                p = res.get("visual_prompt", "")
            except:
                p = self.manual_extract(clean, "visual_prompt")
                mov_name = self.manual_extract(clean, "movement_name")
                manif = self.manual_extract(clean, "manifesto")
                mats = self.manual_extract(clean, "fictional_materials")

            if not p: p = "Error connecting to the Akashic Record."
            
            manifesto_output = f"🏛️ Movement: {mov_name}\n\n📜 Manifesto:\n{manif}"

            return (p, manifesto_output, mats, clean)

        except Exception as e:
            return (f"Oracle Error: {e}", "Err", "Err", "Err")