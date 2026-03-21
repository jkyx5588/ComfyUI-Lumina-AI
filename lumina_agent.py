import requests
import json
import re

# 导入所有之前的知识库和逻辑类
from .lumina_data import *
from .lumina_screenwriter import LuminaScreenwriterNode
from .lumina_core import LuminaDirectorNode, LuminaAestheticNode
from .lumina_music import LuminaMusicNode

class LuminaAgentNode:
    """
    v100.1 Lumina Archon (Autonomous Agent)
    Fixed NameError: user_idea -> user_goal
    """
    def __init__(self):
        # 实例化子模块能力
        self.screenwriter = LuminaScreenwriterNode()
        self.director = LuminaDirectorNode()
        self.aesthetic = LuminaAestheticNode()
        self.musician = LuminaMusicNode()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "user_goal": ("STRING", {"default": "Make a 15s commercial for a futuristic energy drink called 'Zap'", "multiline": True}),
                "creativity": ("FLOAT", {"default": 0.7, "min": 0.1, "max": 1.0}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    # 一次性输出全流程所需的所有 Prompt
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("🧠 Agent_Plan", "📜 Script", "🎬 Visual_Prompts", "🎵 Audio_Prompts", "🔠 Text_Overlay", "⚙️ JSON_Config")
    
    FUNCTION = "execute_agent"
    CATEGORY = "Lumina_AI/Advisors"

    def execute_agent(self, ollama_connection, user_goal, creativity, seed):
        url, model = ollama_connection['url'], ollama_connection['model']

        print(f"🤖 Kaleido Archon: Analyzing goal '{user_goal}'...")

        # --- STEP 1: 规划与参数决策 (The Brain) ---
        # 让 LLM 决定该用什么风格、什么镜头、什么音乐类型
        plan_prompt = f"""
        [SYSTEM ROLE]
        You are Kaleido Archon, an autonomous AI Creative Director.
        Your goal is to configure a complete AIGC production pipeline based on a user request.
        
        [USER GOAL]
        "{user_goal}" 
        
        [AVAILABLE TOOLS]
        - Screenwriter (Script, Character)
        - Director (Shots, Lens, Camera)
        - Aesthetic (Style, Medium, Color)
        - Music (Genre, Mood)
        
        [TASK]
        Analyze the goal and AUTO-SELECT the best parameters from your internal knowledge.
        
        [OUTPUT JSON ONLY]
        {{
            "thought_process": "Brief reasoning...",
            "project_type": "Video / Image / Design",
            "screenwriter_config": {{ "structure": "...", "tone": "..." }},
            "aesthetic_config": {{ "style": "...", "medium": "..." }},
            "director_config": {{ "video_type": "...", "lens": "..." }},
            "music_config": {{ "genre": "...", "mood": "..." }}
        }}
        """
        
        # 调用 LLM 获取计划
        payload = {"model": model, "prompt": plan_prompt, "stream": False, "format": "json", "options": {"temperature": creativity, "seed": seed}}
        try:
            r = requests.post(url, json=payload, timeout=120)
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            plan_data = json.loads(clean)
        except Exception as e:
            return (f"Error Planning: {e}", "", "", "", "", "{}")

        # 提取智能体决定的参数
        thought = plan_data.get("thought_process", "Thinking...")
        print(f"🤖 Archon Thought: {thought}")
        
        # --- STEP 2: 执行编剧 (Execute Story) ---
        # 自动调用 Screenwriter 逻辑
        # 注意：这里我们使用默认值填充非核心参数，让 Screenwriter 自己发挥
        try:
            script_res = self.screenwriter.write_script(
                ollama_connection, 
                user_goal, # 使用 user_goal 作为 core_idea
                plan_data.get("screenwriter_config", {}).get("structure", "📖 Save the Cat [救猫咪]"),
                "👤 The Hero [英雄]", # 默认原型
                "⚔️ Man vs. Self [内心]", # 默认冲突
                "🗣️ Sorkin [快节奏]", # 默认对白
                "🧩 Chekhov's Gun [契诃夫枪]", 
                plan_data.get("screenwriter_config", {}).get("tone", "🌟 Hopeful [治愈]"), 
                "🏁 Twist [反转]", "📜 Standard Screenplay [剧本]", creativity, seed
            )
            final_script = script_res[0]
        except Exception as e:
            final_script = f"Script Error: {e}"

        
        # --- STEP 3: 执行导演与视觉 (Execute Visuals) ---
        try:
            storyboard_res = self.director.generate_storyboard(
                ollama_connection,
                final_script, # 传入刚生成的剧本
                "Main Character", # 简化
                plan_data.get("director_config", {}).get("video_type", "🎬 Cinematic Feature [电影正片]"),
                plan_data.get("director_config", {}).get("lens", "👁️ 35mm [人文]"),
                "🎥 Static [固定]", "👤 Character [人物]",
                plan_data.get("aesthetic_config", {}).get("style", "✨ None [无风格]"),
                "✨ None (Neutral) [无倾向]", 10.0, 4, creativity, seed
            )
            visual_prompts = storyboard_res[0]
        except Exception as e:
            visual_prompts = f"Visual Error: {e}"

        # --- STEP 4: 执行音乐 (Execute Audio) ---
        try:
            music_res = self.musician.generate_music(
                ollama_connection,
                user_goal,
                plan_data.get("music_config", {}).get("genre", "🎻 [Cine] Epic Trailer [史诗预告]"),
                "🎻 Orchestral [管弦]", 
                plan_data.get("music_config", {}).get("mood", "🔥 Energetic [激情]"),
                "120 BPM", "🎛️ High Fidelity [高保真]", "🎼 Loop [循环]", 1, creativity, seed
            )
            audio_prompts = music_res[0]
        except Exception as e:
            audio_prompts = f"Audio Error: {e}"

        # --- STEP 5: 汇总输出 ---
        return (
            thought,
            final_script,
            visual_prompts,
            audio_prompts,
            f"Title: {user_goal}", 
            json.dumps(plan_data, indent=2)
        )