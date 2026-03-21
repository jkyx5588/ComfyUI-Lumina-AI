import requests
import json
import re

# ==============================================================================
# 🌌 PART 1: ASCENSION DATA KNOWLEDGE (超维知识库)
# ==============================================================================

# 🧬 异星生物学 (Xenobiology)
BIO_BASES = {
    "🧬 Carbon-based (Earth-like) [碳基生命]": "Organic, fleshy, cellular structures, recognizable DNA helix motifs, moisture, respiration.",
    "💎 Silicon-based (Litho-life) [硅基生命]": "Crystalline structures, glass-like skin, geometric growth, high-temperature resilience, rocky carapaces.",
    "⚡ Plasma/Energy-based [等离子/能量生命]": "Formless, contained magnetic fields, glowing core, shifting light patterns, ethereal.",
    "🍄 Fungal/Mycelial Network [真菌/孢子网络]": "Interconnected webs, bioluminescent spores, parasitic growth, hive mind structure."
}
GRAVITY_ADAPTATIONS = {
    "🪐 Hyper-Gravity (Dense)[超高重力]": "Squat, broad, hyper-muscular, multi-legged for stability, thick armor plates.",
    "🪐 Micro-Gravity (Ethereal) [微重力/失重]": "Elongated, spindly limbs, fragile bone structures, gas-filled bladders for floating, wingless flight.",
    "🪐 Aquatic/High-Pressure [深海高压]": "Streamlined, bioluminescent lures, transparent flesh revealing organs, flexible cartilage."
}

# 🌀 四维空间与非欧几何 (Spatial & Non-Euclidean)
SPATIAL_GEOMETRY = {
    "🌀 Non-Euclidean (Lovecraftian) [非欧几何]": "Impossible angles, curves that act like straight lines, mind-bending perspective, M.C. Escher style.",
    "🌀 Tesseract / 4D Hypercube [超立方体/四维展开]": "Structures folding into themselves, transparent overlapping dimensions, infinite recursion.",
    "🌀 360° Equirectangular HDRI [360全景环境]": "Panoramic projection, extreme wide field of view, warped top and bottom edges, VR ready.",
    "🌀 Gaussian Splatting Seed [高斯溅射点云]": "Countless floating colored particles forming a cohesive 3D structure, fuzzy edges, neural rendering look."
}

# 👁️‍🗨️ 神经美学与通感 (Neuro-Aesthetics)
SYNESTHESIA_MODES = {
    "🔊 Cymatics (Sound to Shape) [克拉尼图形/声音显形]": "Perfect geometric sand/water patterns formed by frequency resonance, vibration waves.",
    "🔢 Fractal Mathematics [分形数学可视化]": "Mandelbrot sets, infinite zoom capability, mathematical perfection, chaotic yet ordered.",
    "🧠 Brainwave / EEG Mapping[脑电波视觉化]": "Synaptic flashes, neural network branches, abstract emotion maps, glowing nodes."
}

# ⏳ 量子时空与熵 (Quantum Weaver)
TIMELINE_DIVERGENCES = {
    "⏳ Entropy / Heat Death [熵增/热寂]": "Decay, rust, loss of energy, fading light, scattering particles, inevitable end.",
    "⏳ Technological Singularity [科技奇点]": "Over-optimization, grey goo, absolute artificial order, dyson spheres.",
    "⏳ Bio-Convergence [生态归一]": "Nature reclaiming everything, hyper-evolution, organic hive mind taking over."
}


# ==============================================================================
# 🚀 PART 2: THE ASCENSION NODES (飞升节点逻辑)
# ==============================================================================

class LuminaXenobiologistNode:
    """v200.0 Xenobiologist: Generates scientifically grounded speculative evolution."""
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "creature_concept": ("STRING", {"default": "An apex predator", "multiline": True}),
                "biological_base": (sorted(list(BIO_BASES.keys())),),
                "environmental_gravity": (sorted(list(GRAVITY_ADAPTATIONS.keys())),),
                "temperature": ("FLOAT", {"default": 0.75}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("📄 Bio_Prompt", "🧬 Evolutionary_Lore", "⚙️ Raw")
    FUNCTION = "generate"
    CATEGORY = "Lumina_AI/Advisors"

    def generate(self, ollama_connection, creature_concept, biological_base, environmental_gravity, temperature, seed):
        url, model = ollama_connection['url'], ollama_connection['model']
        sys_prompt = f"""[ROLE] Chief Astrobiologist & Scientific Illustrator.
        [TASK] Design a scientifically plausible alien lifeform based on extreme environmental constraints.
        [INPUT] Concept: "{creature_concept}"
        [DNA BASE] {biological_base} ({BIO_BASES[biological_base]})
        [ENVIRONMENT] {environmental_gravity} ({GRAVITY_ADAPTATIONS[environmental_gravity]})
        
        Generate a highly detailed prompt for generating a "scientific textbook illustration" or "hyper-realistic macro photography" of this creature.
        Format as JSON: {{"prompt": "...", "lore": "Brief evolutionary explanation..."}}
        """
        try:
            r = requests.post(url, json={"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}}, timeout=120)
            res = json.loads(re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip())
            return (res.get("prompt", ""), res.get("lore", ""), r.text)
        except Exception as e: return (str(e), "Error", "Error")


class LuminaSpatialArchitectNode:
    """v200.0 Spatial Architect: Generates VR/XR and non-Euclidean environments."""
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "spatial_concept": ("STRING", {"default": "A library holding all the universe's knowledge", "multiline": True}),
                "geometry_law": (sorted(list(SPATIAL_GEOMETRY.keys())),),
                "temperature": ("FLOAT", {"default": 0.7}),
                "seed": ("INT", {"default": 0}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("📄 XR_Prompt", "⚙️ Raw")
    FUNCTION = "generate"
    CATEGORY = "Lumina_AI/Advisors"

    def generate(self, ollama_connection, spatial_concept, geometry_law, temperature, seed):
        url, model = ollama_connection['url'], ollama_connection['model']
        sys_prompt = f"""
        [ROLE] Spatial Computing Engineer & 4D Architect.
        [INPUT] Concept: "{spatial_concept}"
        [PHYSICS ENGINE] {geometry_law} ({SPATIAL_GEOMETRY[geometry_law]})
        
        Generate a prompt that defies normal 3D logic. If 360/HDRI is selected, force a panoramic distortion. If Non-Euclidean, describe paradoxical architecture.
        Format as JSON: {{"prompt": "..."}}
        """
        try:
            r = requests.post(url, json={"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}}, timeout=120)
            res = json.loads(re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip())
            return (res.get("prompt", ""), r.text)
        except Exception as e: return (str(e), "Error")


class LuminaSynestheteNode:
    """v200.0 Synesthete: Transforms invisible data/sound/emotion into geometry."""
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "abstract_input": ("STRING", {"default": "The feeling of remembering a forgotten dream", "multiline": True}),
                "translation_mode": (sorted(list(SYNESTHESIA_MODES.keys())),),
                "temperature": ("FLOAT", {"default": 0.8}),
                "seed": ("INT", {"default": 0}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("📄 Abstract_Prompt", "⚙️ Raw")
    FUNCTION = "generate"
    CATEGORY = "Lumina_AI/Advisors"

    def generate(self, ollama_connection, abstract_input, translation_mode, temperature, seed):
        url, model = ollama_connection['url'], ollama_connection['model']
        sys_prompt = f"""
        [ROLE] Neuro-Aesthetic Artist & Data Visualizer.
        [INPUT] Abstract Concept/Feeling: "{abstract_input}"
        [SYNTHESIS PROTOCOL] {translation_mode} ({SYNESTHESIA_MODES[translation_mode]})
        
        Translate the invisible abstract input into a pure, visually stunning physical form (geometry, light, particles). No literal representations (no humans, no regular objects).
        Format as JSON: {{"prompt": "..."}}
        """
        try:
            r = requests.post(url, json={"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}}, timeout=120)
            res = json.loads(re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip())
            return (res.get("prompt", ""), r.text)
        except Exception as e: return (str(e), "Error")


class LuminaQuantumWeaverNode:
    """v200.0 Quantum Weaver: Generates timeline divergences and multiverse states."""
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "base_event": ("STRING", {"default": "A bustling futuristic metropolis", "multiline": True}),
                "divergence_path": (sorted(list(TIMELINE_DIVERGENCES.keys())),),
                "temperature": ("FLOAT", {"default": 0.75}),
                "seed": ("INT", {"default": 0}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("📄 Multiverse_Prompt", "⚙️ Raw")
    FUNCTION = "generate"
    CATEGORY = "Lumina_AI/Advisors"

    def generate(self, ollama_connection, base_event, divergence_path, temperature, seed):
        url, model = ollama_connection['url'], ollama_connection['model']
        sys_prompt = f"""
        [ROLE] Temporal Physicist & Multiverse Observer.
        [INPUT] Base Reality: "{base_event}"
        [QUANTUM SHIFT] {divergence_path} ({TIMELINE_DIVERGENCES[divergence_path]})
        
        Take the base reality and fast-forward it thousands of years into the selected timeline divergence. Describe the resulting landscape in epic cinematic detail.
        Format as JSON: {{"prompt": "..."}}
        """
        try:
            r = requests.post(url, json={"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed}}, timeout=120)
            res = json.loads(re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip())
            return (res.get("prompt", ""), r.text)
        except Exception as e: return (str(e), "Error")