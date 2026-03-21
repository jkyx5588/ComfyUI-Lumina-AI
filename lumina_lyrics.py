import requests
import json
import re
from PIL import Image
import io
import base64
import numpy as np
import torch

from .lumina_data import (
    LYRIC_STRUCTURES, RHYME_SCHEMES, LYRIC_THEMES, LYRIC_LANGUAGES
)

class LuminaLyricsNode:
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        structures = sorted(list(LYRIC_STRUCTURES.keys()))
        rhymes = sorted(list(RHYME_SCHEMES.keys()))
        themes = sorted(list(LYRIC_THEMES.keys()))
        langs = sorted(LYRIC_LANGUAGES)

        # 智能默认值函数
        def safe_get(options, preferred_key):
            return preferred_key if preferred_key in options else options[0]

        return {
            "required": {
                "ollama_connection": ("OLLAMA_DICT",),
                "song_topic": ("STRING", {"default": "Memories of the past", "multiline": True}),
                
                # 🔴 修复：默认值使用全称
                "structure_preset": (structures, {"default": safe_get(structures, "🎼 Standard Pop [标准流行结构]")}),
                "rhyme_scheme": (rhymes, {"default": safe_get(rhymes, "📝 AABB (Couplets) [双句押韵]")}),
                "theme_vibe": (themes, {"default": safe_get(themes, "🌃 Urban / Nightlife [城市/夜生活]")}),
                "language": (langs, {"default": safe_get(langs, "🇺🇸 English (Modern Pop) [现代英语]")}),
                
                "prompt_count": ("INT", {"default": 3}),
                "creativity": ("FLOAT", {"default": 0.7, "min": 0.1, "max": 1.0}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "image_input": ("IMAGE",), 
                "video_frames": ("IMAGE",), 
                "audio_input": ("AUDIO",), 
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("📜 Full_Lyrics_Text", "🎵 Chorus_Hook_Only", "🎼 Structure_Info", "⚙️ Raw_JSON")
    FUNCTION = "generate_lyrics" 
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
                return self._pil_to_base64(grid), f"Video Montage ({batch_size} frames)"
        except: return None, "Error"

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

    def generate_lyrics(self, ollama_connection, song_topic, structure_preset, rhyme_scheme, theme_vibe, language, creativity, seed, image_input=None, video_frames=None, audio_input=None, **kwargs):
        
        # 兼容旧接口
        if video_frames is None and 'video_input' in kwargs:
            video_frames = kwargs['video_input']

        url, model = ollama_connection['url'], ollama_connection['model']
        
        img_b64, vis_type, vis_ctx, aud_ctx = None, "None", "", ""

        if video_frames is not None:
            img_b64, vis_type = self.process_visual_input(video_frames)
            vis_ctx = f"[Visual: {vis_type}]"
        elif image_input is not None:
            img_b64, vis_type = self.process_visual_input(image_input)
            vis_ctx = "[Visual: Image]"
            
        if audio_input is not None: aud_ctx = "[Audio: Ref]"

        struct_info = LYRIC_STRUCTURES.get(structure_preset, {})
        
        sys_prompt = f"""
        [ROLE] Pro Songwriter.
        [TOPIC] "{song_topic}"
        [CONFIG] Theme: {theme_vibe} | Lang: {language}
        [TECH] Struct: {structure_preset} ({struct_info.get('format')}) | Rhyme: {rhyme_scheme}
        [CONTEXT] {vis_ctx} {aud_ctx}
        [TASK] Write full lyrics.
        [FORMAT] {{ "title": "...", "lyrics": "...", "chorus": "...", "analysis": "..." }}
        """
        
        payload = {"model": model, "prompt": sys_prompt, "stream": False, "format": "json", "options": {"temperature": creativity, "seed": seed, "num_ctx": 8192}}
        if img_b64: payload["images"] = [img_b64]

        try:
            r = requests.post(url, json=payload, timeout=240)
            r.raise_for_status()
            clean = re.sub(r'^```json\s*|```\s*$', '', r.json().get("response", "").strip()).strip()
            try:
                res = json.loads(clean)
                t, l, c, a = res.get("title", ""), res.get("lyrics", ""), res.get("chorus", ""), res.get("analysis", "")
            except:
                l = self.manual_extract(clean, "lyrics")
                c = self.manual_extract(clean, "chorus")
                a, t = "Error", "Error"
            
            return (f"Title: {t}\n\n{l}", c, f"Info: {a}", clean)
        except Exception as e:
            return (f"Error: {e}", "Err", "Err", "Err")