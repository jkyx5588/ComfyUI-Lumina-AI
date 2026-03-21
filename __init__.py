from .lumina_core import OllamaConnectionLoader, LuminaAestheticNode, LuminaDirectorNode
from .lumina_typography import LuminaTypographyNode
from .lumina_music import LuminaMusicNode
from .lumina_lyrics import LuminaLyricsNode
from .lumina_screenwriter import LuminaScreenwriterNode
from .lumina_logo import LuminaLogoNode
from .lumina_color import LuminaColorNode
from .lumina_concept import LuminaConceptNode
from .lumina_critic import LuminaCriticNode
from .lumina_world import LuminaWorldNode
from .lumina_adapter import LuminaAdapterNode
from .lumina_packaging import LuminaPackagingNode
from .lumina_wuxia import LuminaWuxiaNode
from .lumina_brand import LuminaBrandNode
from .lumina_agent import LuminaAgentNode
from .lumina_deconstructor import LuminaDeconstructorNode
from .lumina_verticals import LuminaInteriorNode, LuminaFashionNode, LuminaHairDesignNode, LuminaCulturalDesignNode
from .lumina_ascension import (
    LuminaXenobiologistNode, 
    LuminaSpatialArchitectNode, 
    LuminaSynestheteNode, 
    LuminaQuantumWeaverNode
)
from .lumina_oracle import LuminaOracleNode
from .lumina_medical import LuminaMedicalNode # <--- 新增导入
from .lumina_industrial import LuminaIndustrialNode # <--- 新增导入

NODE_CLASS_MAPPINGS = {
    "OllamaConnectionLoader": OllamaConnectionLoader,
    "LuminaAestheticNode": LuminaAestheticNode,
    "LuminaDirectorNode": LuminaDirectorNode,
    "LuminaTypographyNode": LuminaTypographyNode,
    "LuminaMusicNode": LuminaMusicNode,
    "LuminaLyricsNode": LuminaLyricsNode,
    "LuminaScreenwriterNode": LuminaScreenwriterNode,
    "LuminaLogoNode": LuminaLogoNode,
    "LuminaColorNode": LuminaColorNode,
    "LuminaConceptNode": LuminaConceptNode,
    "LuminaCriticNode": LuminaCriticNode,
    "LuminaWorldNode": LuminaWorldNode,
    "LuminaAdapterNode": LuminaAdapterNode,
    "LuminaPackagingNode": LuminaPackagingNode,
    "LuminaWuxiaNode": LuminaWuxiaNode,
    "LuminaBrandNode": LuminaBrandNode,
    "LuminaAgentNode": LuminaAgentNode,
    "LuminaDeconstructorNode": LuminaDeconstructorNode,
    "LuminaInteriorNode": LuminaInteriorNode,
    "LuminaFashionNode": LuminaFashionNode,
    "LuminaHairDesignNode": LuminaHairDesignNode,
    "LuminaCulturalDesignNode": LuminaCulturalDesignNode,
    "LuminaXenobiologistNode": LuminaXenobiologistNode,
    "LuminaSpatialArchitectNode": LuminaSpatialArchitectNode,
    "LuminaSynestheteNode": LuminaSynestheteNode,
    "LuminaQuantumWeaverNode": LuminaQuantumWeaverNode,
    "LuminaOracleNode": LuminaOracleNode,
    "LuminaMedicalNode": LuminaMedicalNode,
    "LuminaIndustrialNode": LuminaIndustrialNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OllamaConnectionLoader": "🔌 Lumina Loader (Ollama)",
    "LuminaAestheticNode": "🌌 Lumina Aesthetic Advisor",
    "LuminaDirectorNode": "🎬 Lumina Storyboard Director",
    "LuminaTypographyNode": "🔠 Lumina Typography Alchemist",
    "LuminaMusicNode": "🎵 Lumina Music Composer",
    "LuminaLyricsNode": "🎤 Lumina Songwriter (Lyrics)",
    "LuminaScreenwriterNode": "📝 Lumina Showrunner (Story)",
    "LuminaLogoNode": "🛡️ Lumina Logo Master",
    "LuminaColorNode": "🎨 Lumina Color Grader",
    "LuminaConceptNode": "👤 Lumina Concept Artist",
    "LuminaCriticNode": "🧐 Lumina Art Critic (Vision)",
    "LuminaWorldNode": "🌍 Lumina World Builder",
    "LuminaAdapterNode": "🔌 Lumina Prompt Adapter",
    "LuminaPackagingNode": "📦 Lumina Packaging (Product)",
    "LuminaWuxiaNode": "⚔️ Lumina Wuxia Master",
    "LuminaBrandNode": "💼 Lumina Brand Director (Full Case)",
    "LuminaAgentNode": "🤖 Lumina Archon (Auto-Agent)",
    "LuminaDeconstructorNode": "👁️ Lumina Deconstructor (Reverse Eng)",
    "LuminaInteriorNode": "🏛️ Lumina Interior Architect",
    "LuminaFashionNode": "👗 Lumina Fashion Designer",
    "LuminaHairDesignNode": "✂️ Lumina Hair Stylist",
    "LuminaCulturalDesignNode": "🎁 Lumina Cultural Merch (Design)",
    "LuminaXenobiologistNode": "🧬 Lumina Xenobiologist (Life)",
    "LuminaSpatialArchitectNode": "🌀 Lumina Spatial Architect (XR)",
    "LuminaSynestheteNode": "👁️‍🗨️ Lumina Synesthete (Neuro-Art)",
    "LuminaQuantumWeaverNode": "⏳ Lumina Quantum Weaver (Time)",
    "LuminaOracleNode": "👁️ Lumina Oracle (Transcendence)",
    "LuminaMedicalNode": "🧬 Lumina Medical & Anatomy",
    "LuminaIndustrialNode": "🛠️ Lumina Industrial Design",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]