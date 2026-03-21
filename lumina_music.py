import requests
import json
import re
from PIL import Image
import io
import base64
import numpy as np
import torch

from .lumina_data import (
    MUSIC_GENRES, MUSIC_INSTRUMENTS, MUSIC_STRUCTURES, 
    MUSIC_PRODUCTION, MUSIC_MOODS
)

class LuminaMusicNode:
    """
    v37.0 Lumina Music (Dynamic Safety)
    - Fixes 'Value not in list' errors by dynamically validating default values.
    """
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        # 1. 获取排序后的列表
        genres = sorted(list(MUSIC_GENRES.keys()))
        inst = sorted(list(MUSIC_INSTRUMENTS.keys()))
        struct = sorted(list(MUSIC_STRUCTURES.keys()))
        prod = sorted(list(MUSIC_PRODUCTION.keys()))
        moods = sorted(MUSIC_MOODS)

        # 2. 安全获取默认值的辅助函数
        # (如果指定的默认值 key 不在列表中，自动回退到列表第0项，防止报错)
        def safe_get(options, preferred_key):
            return preferred_key if preferred_key in options else options[0]

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "user_idea": ("STRING", {"default": "Chase scene", "multiline": True}),
                
                # 使用动态安全默认值
                "music_genre": (genres, {"default": safe_get(genres, "🎹 [Elec] Synthwave [合成器波]")}),
                "instrumentation": (inst, {"default": safe_get(inst, "🎹 Analog Synths [模拟合成器]")}),
                "mood_vibe": (moods, {"default": safe_get(moods, "🔥 Energetic [激情]")}),
                
                "bpm_tempo": ("STRING", {"default": "120 BPM"}),
                
                "production_quality": (prod, {"default": safe_get(prod, "🎛️ High Fidelity [高保真]")}),
                "structure": (struct, {"default": safe_get(struct, "🎼 Loop [循环]")}),
                
                "prompt_count": ("INT", {"default": 3}),
                "temperature": ("FLOAT", {"default": 0.7}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "image_input": ("IMAGE",), 
                "video_frames": ("IMAGE",), 
                "audio_input": ("AUDIO",), 
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("🎵 Audio_Prompts", "🎼 Analysis", "🎹 Specs", "📝 Negative", "⚙️ Raw")
    FUNCTION = "generate_music"
    CATEGORY = "Lumina_AI/Advisors"

    def process_visual_input(self, image_tensor):
        try:
            if not isinstance(image_tensor, torch.Tensor): return None, "Invalid"
            batch_size = image_tensor.shape[0]
            if batch_size == 1:
                pil_img = self._tensor_to_pil(image_tensor[0])
                return self._pil_to_base64(pil_img), "Single Image"
            else:
                indices = np.linspace(0, batch_size - 1, 4, dtype=int)
                frames = [self._tensor_to_pil(image_tensor[i]) for i in indices]
                w, h = frames[0].size
                grid = Image.new('RGB', (w * 2, h * 2))
                grid.paste(frames[0], (0, 0)); grid.paste(frames[1], (w, 0))
                grid.paste(frames[2], (0, h)); grid.paste(frames[3], (w, h))
                grid.thumbnail((1024, 1024))
                return self._pil_to_base64(grid), f"Video Montage ({batch_size}f)"
        except Exception as e:
            return None, "Error"

    def _tensor_to_pil(self, tensor):
        return Image.fromarray(np.clip(255. * tensor.cpu().numpy(), 0, 255).astype(np.uint8))

    def _pil_to_base64(self, pil_img):
        buf = io.BytesIO()
        pil_img.save(buf, format="JPEG", quality=85)
        return base64.b64encode(buf.getvalue()).decode("utf-8")

    def manual_extract(self, text, key):
        pattern = rf'"{key}"\s*:\s*(.*?)(?:,\n|,\s*"|}}$)'
        match = re.search(pattern, text, re.DOTALL)
        if match: return match.group(1).strip().strip('"').strip("'")
        return None

    def generate_music(self, ollama_connection, user_idea, music_genre, instrumentation, mood_vibe, bpm_tempo, production_quality, structure, prompt_count, temperature, seed, image_input=None, video_frames=None, audio_input=None, **kwargs):
        
        # 兼容旧参数
        if video_frames is None and 'video_input' in kwargs:
            video_frames = kwargs['video_input']

        url, model = ollama_connection['url'], ollama_connection['model']
        
        img_b64 = None
        vis_ctx = ""
        aud_ctx = ""

        if video_frames is not None:
            img_b64, t = self.process_visual_input(video_frames)
            vis_ctx = f"[Visual: {t}]"
        elif image_input is not None:
            img_b64, t = self.process_visual_input(image_input)
            vis_ctx = "[Visual: Image]"
            
        if audio_input is not None:
            aud_ctx = "[Audio: Reference]"

        # 从字典获取完整描述（防止 key 变更导致获取不到）
        genre_desc = MUSIC_GENRES.get(music_genre, "")
        inst_desc = MUSIC_INSTRUMENTS.get(instrumentation, "")
        struct_desc = MUSIC_STRUCTURES.get(structure, "")
        prod_desc = MUSIC_PRODUCTION.get(production_quality, "")

        sys_prompt = f"""
        [ROLE] Music Producer.
        [INPUT] "{user_idea}" {vis_ctx} {aud_ctx}
        [GENRE] {music_genre} ({genre_desc})
        [INST] {instrumentation} ({inst_desc}) | Mood: {mood_vibe}
        [TECH] {bpm_tempo} | {production_quality} ({prod_desc}) | {structure} ({struct_desc})
        [TASK] Generate {prompt_count} prompts.
        [FORMAT] {{ "analysis": "...", "technical_specs": "...", "prompts": ["..."], "negative": "..." }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": temperature, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                p = res.get("prompts", [])
                a = res.get("analysis", "")
                t = res.get("technical_specs", "")
                n = res.get("negative", "")
            except:
                p = self.manual_extract(clean, "prompts")
                a, t, n = "Error", "Error", "Error"
                if not p: p = ["Error"]
            
            if isinstance(p, str): p = [p]
            final_p = "\n\n".join([f"[{i+1}] {str(x)}" for i, x in enumerate(p)])
            
            return (final_p, str(a), str(t), str(n), clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err", "Err")