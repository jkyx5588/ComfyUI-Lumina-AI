# ==============================================================================
# 🧠 LUMINA DATA WAREHOUSE (灵光·数据仓库)
# ==============================================================================
# 包含：16型人格、160+美学流派、70+技术媒介、视频类型、镜头语言等

# --- 1. MBTI 创作者人格 ---
MBTI_AESTHETICS = {
    "✨ None (Neutral) [无倾向]": {"vibe": "Neutral, Objective", "keywords": "", "composition": "Standard balanced"},
    "🧠 INTJ [建筑师] - Structural": {"vibe": "Cold, Calculated, Visionary", "keywords": "fractal geometry, master plan, isolation, deep perspective, monochromatic, perfectionism", "composition": "Symmetrical, hierarchical, top-down"},
    "🧠 INTP [逻辑学家] - Abstract": {"vibe": "Experimental, Analytical", "keywords": "wireframe, blueprint overlay, exposed mechanisms, glitch artifacts, theoretical physics", "composition": "Complex, layered, detailed chaos"},
    "🧠 ENTJ [指挥官] - Dominant": {"vibe": "Dominant, High-Contrast", "keywords": "imposing scale, brutalist structures, sharp suits, gold and marble, spotlight, power", "composition": "Low angle, leading lines"},
    "🧠 ENTP [辩论家] - Chaotic": {"vibe": "Provocative, Satirical", "keywords": "steampunk gears, impossible objects, mashup styles, optical illusions, clashing colors", "composition": "Asymmetrical, dynamic movement"},
    "❤️ INFJ [提倡者] - Mystical": {"vibe": "Ethereal, Symbolic", "keywords": "nebula, galaxy, ancient runes, fog, hidden meaning, soft glow, spiritual", "composition": "Framing within framing, depth of field"},
    "❤️ INFP [调停者] - Dreamy": {"vibe": "Whimsical, Nostalgic", "keywords": "fairy tale forest, watercolor bleed, soft pastel clouds, cozy bedroom, magic realism", "composition": "Soft focus, wandering eye, intimate"},
    "❤️ ENFJ [主人公] - Radiant": {"vibe": "Warm, Inspiring", "keywords": "sunrise, beaming light, diverse crowds, harmony, vibrant warm colors, theatrical", "composition": "Radial symmetry, open arms"},
    "❤️ ENFP [竞选者] - Vibrant": {"vibe": "Explosive, Psychedelic", "keywords": "rainbow explosion, confetti, balloons, glitter, surreal collage, kaleidoscope, joy", "composition": "Scattered, flying elements, chaotic energy"},
    "🛡️ ISTJ [物流师] - Realistic": {"vibe": "Reliable, Historical", "keywords": "dust particles, weathered texture, library archives, clockwork, sepia tone, high fidelity", "composition": "Rule of thirds, grid-like"},
    "🛡️ ISFJ [守卫者] - Gentle": {"vibe": "Cozy, Domestic", "keywords": "home interior, porcelain texture, soft fabrics, baking, warm candlelight, vintage aesthetic", "composition": "Balanced, eye-level, approachable"},
    "🛡️ ESTJ [总经理] - Formal": {"vibe": "Structured, Corporate", "keywords": "steel and glass, uniform, clean lines, high contrast, documentary style, efficiency", "composition": "Formal balance, straight lines"},
    "🛡️ ESFJ [执政官] - Social": {"vibe": "Festive, Polished", "keywords": "party lights, fashion editorial, high saturation, clear faces, pop culture references", "composition": "Group shots, centered, inviting"},
    "⚡ ISTP [鉴赏家] - Technical": {"vibe": "Mechanical, Raw", "keywords": "garage tools, metal sparks, carbon fiber, grease, cyberpunk tech, weapon details", "composition": "Detail-oriented, dutch angle"},
    "⚡ ISFP [探险家] - Artisanal": {"vibe": "Artistic, Textural", "keywords": "oil paint texture, indie vibe, lo-fi aesthetic, nature textures, bohemian, sensory", "composition": "Asymmetrical balance, flowing lines"},
    "⚡ ESTP [企业家] - Action": {"vibe": "Action, Risky", "keywords": "sports car, motion blur, explosion, lens flare, high contrast, brand logos, neon", "composition": "Dynamic diagonals, frozen action"},
    "⚡ ESFP [表演者] - Glamorous": {"vibe": "Spotlight, Trendy", "keywords": "glitter, stage lights, sequins, superstar, disco ball, vivid pinks, fashion", "composition": "Center stage, bokeh background"}
}

# --- 2. 全量美学流派库 (v21 Omni-Culture) ---
PROFESSIONAL_KNOWLEDGE_BASE = {
    "✨ None (Pure Prompting) [无风格/纯描述]": {"desc": "No specific style filter.", "markers": "neutral representation", "lighting": "Balanced", "colors": "Natural"},
    
    # 🌍 [Global]
    "🌍 [Global] Afro-Futurism [非洲未来主义]": {"desc": "African diaspora tech.", "markers": "tribal patterns, vibranium, neon tribalism", "lighting": "Bioluminescent", "colors": "Purple, Gold, Black"},
    "🌍 [Global] Nordic Minimalism [北欧极简]": {"desc": "Scandinavian coziness.", "markers": "light wood, clean lines, hygge", "lighting": "Soft diffused", "colors": "White, Beige, Sage"},
    "🌍 [Global] Islamic Geometric [伊斯兰几何]": {"desc": "Mathematical symmetry.", "markers": "tessellation, star patterns, calligraphy", "lighting": "Dappled light", "colors": "Turquoise, Gold"},
    "🌍 [Global] Mexican Muralism [墨西哥壁画]": {"desc": "Social realism.", "markers": "bold figures, calla lilies, Rivera style", "lighting": "Sun-drenched", "colors": "Earth tones, Maize"},
    "🌍 [Global] Slavic Folklore [斯拉夫民俗]": {"desc": "Eastern fairy tales.", "markers": "embroidery, wooden huts, spirits", "lighting": "Firelight", "colors": "Red, Snow White, Green"},
    "🌍 [Global] Indian Kitsch [印度卡车艺术]": {"desc": "Maximalist folk art.", "markers": "floral motifs, eyes, typography", "lighting": "Bright tropical", "colors": "Neon Orange, Pink"},

    # 💎 [Digital]
    "💎 [Digital] Claymorphism [黏土拟物]": {"desc": "Soft 3D shapes.", "markers": "inflated shapes, matte plastic, cute", "lighting": "Softbox", "colors": "Pastel Macaron"},
    "💎 [Digital] Glassmorphism [毛玻璃]": {"desc": "Translucent UI.", "markers": "frosted glass, blur, floating layers", "lighting": "Backlit glow", "colors": "White transparency"},
    "💎 [Digital] Low Fidelity (Lo-Fi) [低保真]": {"desc": "Cozy imperfect.", "markers": "grainy, messy desk, chill vibes", "lighting": "Dim lamp", "colors": "Muted Indigo"},
    "💎 [Digital] Glitch Art [故障艺术]": {"desc": "Digital error.", "markers": "pixel sorting, chromatic aberration", "lighting": "Strobing", "colors": "RGB split, Static"},
    
    # 📷 [Photo]
    "📷 [Photo] Street Photography [街头摄影]": {"desc": "Candid urban life.", "markers": "decisive moment, motion blur", "lighting": "Natural harsh sunlight", "colors": "High contrast B&W"},
    "📷 [Photo] Fashion Editorial [时尚大片]": {"desc": "High-end fashion.", "markers": "bold poses, avant-garde", "lighting": "Studio strobe", "colors": "Trendy palettes"},
    "📷 [Photo] Ansel Adams [亚当斯风光]": {"desc": "Masterful landscape.", "markers": "f/64 sharp focus, texture detail", "lighting": "Dramatic natural", "colors": "Deep B&W Zone System"},
    "📷 [Photo] Cinematic Staged [电影叙事]": {"desc": "Elaborately staged.", "markers": "frozen moment, lonely figures", "lighting": "Twilight artificial", "colors": "Cool blue, warm tungsten"},
    "📷 [Photo] Minimalist [极简摄影]": {"desc": "Art of less.", "markers": "negative space, geometry", "lighting": "Flat, shadowless", "colors": "Pastel, High key"},
    "📷 [Photo] Lomography [LOMO风格]": {"desc": "Low-fi analog.", "markers": "vignetting, light leaks", "lighting": "Direct flash", "colors": "Cross-processed"},
    "📷 [Photo] Cyanotype [蓝晒印相]": {"desc": "Early photographic printing.", "markers": "photogram silhouettes, botanical shapes", "lighting": "UV exposure look", "colors": "Monochromatic Prussian Blue"},
    "📷 [Photo] Magnum Documentary [马格兰纪实]": {"desc": "Raw photojournalism.", "markers": "raw emotion, grit", "lighting": "Available light", "colors": "Realistic, desaturated"},
    "📷 [Photo] Infrared [红外摄影]": {"desc": "False color.", "markers": "white foliage, black sky", "lighting": "High contrast", "colors": "Bubblegum pink, Crimson"},
    "📷 [Photo] Astrophotography [天文摄影]": {"desc": "Deep space.", "markers": "milky way, nebulae, star trails", "lighting": "Starlight", "colors": "Deep Space Black"},
    "📷 [Photo] Underwater [水下摄影]": {"desc": "Submerged.", "markers": "weightlessness, refraction, bubbles", "lighting": "Sun rays", "colors": "Aqua, Coral"},
    "📷 [Photo] Tilt-Shift [移轴微缩]": {"desc": "Miniature world.", "markers": "extreme blur, high angle, toy-like", "lighting": "Bright sunny", "colors": "High saturation"},

    # 🏛️ [Arch]
    "🏛️ [Arch] Deconstructivism [解构主义]": {"desc": "Fragmented shapes.", "markers": "fluid curves, zero gravity", "lighting": "Futuristic LED", "colors": "White, Concrete"},
    "🏛️ [Arch] Metabolism [代谢派]": {"desc": "Biological megastructures.", "markers": "capsules, modular units", "lighting": "Overcast", "colors": "Rusty concrete"},
    "🏛️ [Arch] Gothic Revival [哥特复兴]": {"desc": "Medieval verticality.", "markers": "spires, stained glass", "lighting": "Dim candle", "colors": "Stone, Deep Red"},
    "🏛️ [Arch] Brutalism [粗野主义]": {"desc": "Raw concrete.", "markers": "massive volumes, fortress-like", "lighting": "Harsh shadows", "colors": "Grey"},
    "🏛️ [Arch] Parametricism [参数化主义]": {"desc": "Computational.", "markers": "voronoi, organic mesh", "lighting": "Global illumination", "colors": "White, Chrome"},

    # 👗 [Fashion]
    "👗 [Fashion] Alexander McQueen [暗黑浪漫]": {"desc": "Savage beauty.", "markers": "feathers, skulls, latex", "lighting": "Runway spotlight", "colors": "Black, Red, Gold"},
    "👗 [Fashion] Techwear [机能风]": {"desc": "Futuristic functional.", "markers": "straps, buckles, matte fabric", "lighting": "Neon night", "colors": "Matte Black, Olive"},
    "👗 [Fashion] Harajuku Decora [原宿风]": {"desc": "Excessive accessories.", "markers": "hair clips, layers", "lighting": "Flat bright", "colors": "Neon Rainbow"},
    "👗 [Fashion] Haute Couture [高级定制]": {"desc": "High-end.", "markers": "impossible volumes, silk", "lighting": "Softbox", "colors": "Elegant textures"},

    # 🖊️ [Comic]
    "🖊️ [Comic] Moebius [墨比斯]": {"desc": "Surreal sci-fi.", "markers": "desert, Ligne Claire", "lighting": "Flat desert sun", "colors": "Pale pastel, Cyan"},
    "🖊️ [Comic] Junji Ito [伊藤润二]": {"desc": "Body horror.", "markers": "spirals, ink lines", "lighting": "Stark B/W", "colors": "Black Ink"},
    "🖊️ [Comic] Frank Miller [罪恶之城]": {"desc": "High contrast noir.", "markers": "silhouettes, rain", "lighting": "Pure Black/White", "colors": "B/W + Red"},
    "🖊️ [Comic] Ligne Claire [清晰线条]": {"desc": "Tintin style.", "markers": "uniform line weight, flat colors", "lighting": "Flat", "colors": "Primary colors"},

    # 🌐 [Net]
    "🌐 [Net] Frutiger Aero [千禧拟物]": {"desc": "2000s tech.", "markers": "glossy, fish, bubbles", "lighting": "Bloom", "colors": "Cyan, Lime"},
    "🌐 [Net] Dreamcore [梦核]": {"desc": "Unsettling nostalgia.", "markers": "eyes, amateur flash", "lighting": "Harsh flash", "colors": "Oversaturated"},
    "🌐 [Net] Poolcore [池核]": {"desc": "Liminal pools.", "markers": "tiles, water, emptiness", "lighting": "Caustics", "colors": "Cyan, White"},
    "🌐 [Net] Vaporwave [蒸汽波]": {"desc": "80s nostalgia.", "markers": "statues, glitches", "lighting": "Neon sunset", "colors": "Pink, Purple"},
    "🌐 [Net] Traumacore [伤痛核]": {"desc": "Trauma.", "markers": "Sanrio, medical equipment", "lighting": "Hazy", "colors": "Pastel Pink, Red"},

    # 🔬 [Sci]
    "🔬 [Sci] Electron Microscope [扫描电镜]": {"desc": "Microscopic.", "markers": "monochromatic, extreme texture", "lighting": "Occlusion", "colors": "Greyscale"},
    "🔬 [Sci] Thermal Imaging [热成像]": {"desc": "Heat signature.", "markers": "heat map", "lighting": "Emissive", "colors": "Rainbow gradient"},
    "🔬 [Sci] Kirlian Photography [气场摄影]": {"desc": "High voltage.", "markers": "coronal discharge, aura", "lighting": "Bio-electric", "colors": "Electric Blue"},
    "🔬 [Sci] X-Ray [X光]": {"desc": "Internal structure.", "markers": "skeletal, transparency", "lighting": "Backlit", "colors": "Blue-tint monochrome"},
    "🔬 [Sci] Ferrofluid [磁流体]": {"desc": "Magnetic liquid.", "markers": "spiky, metallic", "lighting": "Specular", "colors": "Jet Black"},

    # 💀 [Dark]
    "💀 [Dark] Zdzisław Beksiński [贝克辛斯基]": {"desc": "Dystopian.", "markers": "skeletal, cobwebs", "lighting": "Apocalyptic orange", "colors": "Rotten Orange, Grey"},
    "💀 [Dark] H.R. Giger [吉格尔]": {"desc": "Biomechanical.", "markers": "flesh/machine, ribbed tubes", "lighting": "Cold slime", "colors": "Grey, Black, Green"},
    "💀 [Dark] SCP Foundation [SCP档案]": {"desc": "Clinical paranormal.", "markers": "redacted, containment", "lighting": "Clinical", "colors": "Sterile White, Black"},
    "🏛️ [History] Byzantine [拜占庭]": {"desc": "Religious.", "markers": "gold leaf, halos", "lighting": "Divine", "colors": "Gold, Purple"},
    "🏛️ [History] Soviet Constructivism [苏联构成]": {"desc": "Propaganda.", "markers": "geometric shapes, diagonals", "lighting": "Graphic", "colors": "Red, Black, White"},
    "🏛️ [History] Aztec Codex [阿兹特克]": {"desc": "Mesoamerican.", "markers": "flat profile, glyphs", "lighting": "Flat", "colors": "Ochre, Turquoise"},

    # 🎬 [Cinema]
    "🎬 [Cinema] Film Noir [黑色电影]": {"desc": "Crime drama.", "markers": "blinds, smoke", "lighting": "Low-key", "colors": "B/W"},
    "🎬 [Cinema] Wes Anderson [韦斯安德森]": {"desc": "Symmetrical.", "markers": "symmetry, flat lay", "lighting": "Flat", "colors": "Pastel"},
    "🎬 [Cinema] Wong Kar-wai [王家卫]": {"desc": "Mood.", "markers": "step-printing, intimacy", "lighting": "Neon ambient", "colors": "Green/Yellow tint"},
    "🎬 [Cinema] Blade Runner [银翼杀手]": {"desc": "Cyberpunk noir.", "markers": "rain, holograms", "lighting": "Neon", "colors": "Blue, Orange"},
    "🎬 [Cinema] Jodorowsky [佐杜洛夫斯基]": {"desc": "Surreal ritual.", "markers": "tarot, deserts", "lighting": "Desert sun", "colors": "Rainbow, Gold"},
    "🎬 [Cinema] Giallo [铅黄电影]": {"desc": "70s horror.", "markers": "black gloves, knives", "lighting": "Gel lighting (Red/Green)", "colors": "Blood Red, Acid Green"},
    "🎬 [Cinema] Tarkovsky [塔可夫斯基]": {"desc": "Poetic.", "markers": "rain inside, fog", "lighting": "Diffused", "colors": "Muted Earth"},

    # 🏮 [Eastern]
    "🏮 [China] Song Dynasty Ink [宋代水墨]": {"desc": "Zen.", "markers": "negative space, mist", "lighting": "Diffused", "colors": "Black ink"},
    "🏮 [China] Dunhuang Mural [敦煌壁画]": {"desc": "Religious cave.", "markers": "flying apsaras, peeling paint", "lighting": "Dim candle", "colors": "Malachite, Gold"},
    "🏮 [China] C-Cyberpunk [中式赛博]": {"desc": "Neon China.", "markers": "neon kanji, pagodas", "lighting": "Neon", "colors": "Cyan, Red"},
    "🏮 [China] Wuxia Fantasy [武侠仙侠]": {"desc": "Martial arts.", "markers": "flowing robes, swords", "lighting": "Moonlight", "colors": "Cyan, White"},
    "🏮 [China] Cloisonné [景泰蓝]": {"desc": "Enamel art.", "markers": "gold wire, enamel filling", "lighting": "Metallic", "colors": "Blue, Gold"},
    "🏮 [Japan] Ukiyo-e [浮世绘]": {"desc": "Floating world.", "markers": "bold outlines, flat", "lighting": "Flat", "colors": "Prussian Blue"},
    
    # 🎎 [Anime]
    "🎎 [Anime] Makoto Shinkai [新海诚]": {"desc": "Scenery.", "markers": "clouds, lens flare", "lighting": "Radiant", "colors": "Blue, Purple"},
    "🎎 [Anime] Ghibli Style [吉卜力]": {"desc": "Nostalgic.", "markers": "lush nature", "lighting": "Sunny", "colors": "Green, Blue"},
    "🎎 [Anime] 90s Cel Style [90年代赛璐璐]": {"desc": "Vintage.", "markers": "film grain, chromatic aberration", "lighting": "Hard shadows", "colors": "Pastel"},
    "🎮 [Game] Elden Ring [魂系暗黑]": {"desc": "Gothic.", "markers": "ruins, erdtree", "lighting": "Golden gloom", "colors": "Gold, Grey"},
    "🎮 [Game] Cyberpunk 2077 [赛博朋克]": {"desc": "High-tech.", "markers": "implants, neon", "lighting": "Neon", "colors": "Yellow, Cyan"},
    "🎮 [Game] Pixel Art [像素艺术]": {"desc": "Retro.", "markers": "visible pixels", "lighting": "Simple", "colors": "Limited"},

    # 🎨 [Classic]
    "🎨 [Art] Renaissance [文艺复兴]": {"desc": "Harmony.", "markers": "sfumato, triangle", "lighting": "Soft", "colors": "Red, Gold"},
    "🎨 [Art] Baroque [巴洛克]": {"desc": "Drama.", "markers": "swirling, contrast", "lighting": "Chiaroscuro", "colors": "Dark, Gold"},
    "🎨 [Art] Impressionism [印象派]": {"desc": "Light.", "markers": "visible strokes", "lighting": "Natural", "colors": "Vibrant"},
    "🎨 [Art] Art Nouveau [新艺术]": {"desc": "Organic.", "markers": "curves, flowers", "lighting": "Soft", "colors": "Muted Green"},
    "🎨 [Art] Surrealism [超现实]": {"desc": "Dream.", "markers": "melting clocks", "lighting": "Eerie", "colors": "Vivid"},
    "🎨 [Art] Pointillism [点彩派]": {"desc": "Dots.", "markers": "stippling, no lines", "lighting": "Shimmering", "colors": "Pastel"},
    "🎨 [Art] Fauvism [野兽派]": {"desc": "Wild.", "markers": "unnatural colors, rough strokes", "lighting": "Flat", "colors": "Clashing"},
    "🎨 [Art] Dadaism [达达主义]": {"desc": "Absurd.", "markers": "photomontage, newspaper", "lighting": "Collage", "colors": "Sepia, Black"},
    "🎨 [Art] Cubism [立体主义]": {"desc": "Geometric.", "markers": "fragmentation, planes", "lighting": "Multidirectional", "colors": "Brown, Grey"},
    
    # 🚀 [Subculture]
    "🚀 [Subculture] Solarpunk [太阳朋克]": {"desc": "Green.", "markers": "plants, glass", "lighting": "Sunny", "colors": "Green, Gold"},
    "🚀 [Subculture] Steampunk [蒸汽朋克]": {"desc": "Steam.", "markers": "gears, brass", "lighting": "Sepia", "colors": "Bronze"},
    "🚀 [Subculture] Cthulhu [克苏鲁]": {"desc": "Cosmic horror.", "markers": "tentacles, madness", "lighting": "Murky gloom", "colors": "Deep sea green"},
    "📘 [Philosophy] Hauntology [幽灵学]": {"desc": "Lost futures.", "markers": "crackling vinyl, brutalism", "lighting": "Flickering", "colors": "Grey, Faded Orange"}
}

# --- 3. 全量技术媒介 (v21 Omni-Media) ---
TECHNICAL_MEDIA = {
    # Photo
    "📷 [Photo] Digital Photography (DSLR) [数码单反]": "Shot on Sony A7R IV, 8k, ultra-sharp",
    "📷 [Photo] Analog Film (Kodak Portra) [彩色胶片]": "Shot on Kodak Portra 400, film grain, warm tones",
    "📷 [Photo] Analog Film (Tri-X B&W) [黑白胶片]": "Shot on Kodak Tri-X 400, high contrast B&W, grainy",
    "📷 [Photo] Fujifilm Velvia 50 [风景反转片]": "Ultra high saturation, deep blacks, vivid colors",
    "📷 [Photo] Polaroid SX-70 [拍立得]": "Soft focus, vintage border, chemical artifacts, lo-fi",
    "📷 [Photo] Wet Plate Collodion [湿版摄影]": "19th century, imperfections, chemical stains, shallow depth of field",
    "📷 [Photo] Leica M6 Summilux [徕卡街拍]": "35mm lens, f/1.4, street aesthetic, sharp center",
    "📷 [Photo] Hasselblad Medium Format [中画幅]": "6x6 square format, insane detail, studio quality",
    "📷 [Photo] Drone / Aerial [航拍]": "Top-down view, geometric patterns, DJI Mavic aesthetic",
    "📷 [Photo] Pinhole Camera [针孔相机]": "Infinite depth of field, soft blurry edges, vignetting",
    "📷 [Photo] Double Exposure [双重曝光]": "Superimposed images, ghosting, silhouette overlay",
    # Sci
    "🔬 [Sci] Scanning Electron Microscope [电子显微镜]": "Greyscale, nanometer detail, crystalline texture",
    "🔬 [Sci] Thermal / FLIR [热成像]": "Heat map, predator vision, rainbow gradients",
    "🔬 [Sci] X-Ray [X光]": "Inverted luminosity, skeletal transparency, blue/white",
    "🔬 [Sci] Schlieren Photography [纹影摄影]": "Visualizing air density, fluid dynamics, scientific",
    "🔬 [Sci] Kirlian Photography [气场摄影]": "Coronal discharge, electrical aura, sparks",
    "🔬 [Sci] Ferrofluid [磁流体]": "Magnetic liquid, spiky texture, metallic sheen",
    # 3D
    "💻 [3D] Unreal Engine 5 (Lumen) [UE5实时]": "Real-time GI, Nanite geometry, high fidelity",
    "💻 [3D] Octane Render (Path Tracing) [OC光追]": "Physically correct light, caustics, cinematic",
    "💻 [3D] Blender Cycles [Blender]": "Open source 3D aesthetic, principled BSDF",
    "💻 [3D] Low Poly [低多边形]": "Sharp edges, flat shading, minimal geometry",
    "💻 [3D] Voxel Art [体素]": "3D cubes, Minecraft style, orthographic",
    "💻 [3D] Point Cloud Scan [点云扫描]": "LiDAR scan data, particle dots, digital ghost",
    "💻 [3D] PS1 Retro Graphics [PS1复古]": "Jittering vertices, affine texture mapping, low res",
    # Paint
    "🖌️ [Paint] Impasto Oil [厚涂油画]": "Thick paint, palette knife texture, 3D brushstrokes",
    "🖌️ [Paint] Watercolor [水彩]": "Wet-on-wet, bleeding, transparent layers, soft edges",
    "🖌️ [Paint] Ink Wash [水墨]": "Calligraphic strokes, varying ink density, rice paper",
    "🖌️ [Paint] Alcohol Ink [酒精墨水]": "Fluid art, swirling metallic pigments, vibrant cells",
    "🖌️ [Paint] Charcoal / Pencil [素描]": "Graphite texture, hatching, shading, monochromatic",
    # Illustration
    "✒️ [Illustration] Risograph Print [孔版印刷]": "Grainy dither, misaligned layers, neon spot colors",
    "✒️ [Illustration] Vector Art [矢量插画]": "Adobe Illustrator, clean bezier curves, flat colors",
    "✒️ [Illustration] Technical Blueprint [工程蓝图]": "White lines on blue paper, schematic, isometric",
    "✒️ [Illustration] Collage / Mixed Media [拼贴]": "Cut-out paper, mixed textures, dadaist composition",
    "✒️ [Illustration] Papercut [剪纸]": "Layered paper shadows, depth, intricate cutting",
    "✒️ [Illustration] Ukiyo-e Woodblock [木刻版画]": "Carved wood texture, flat colors, outlines"
}

# --- 4. 导演分镜参数 (Director's Cut) ---
VIDEO_TYPES = {
    "🎬 Cinematic Feature [电影正片]": {"desc": "Narrative driven, 24fps.", "keywords": "cinematic lighting, anamorphic lens flare"},
    "📺 TV Commercial (TVC) [商业广告]": {"desc": "High key, glossy.", "keywords": "studio lighting, product shot, slow motion"},
    "📹 Social Media Reel [短视频]": {"desc": "Fast paced, viral.", "keywords": "high contrast, dynamic movement, trending"},
    "🎵 Music Video (MV) [音乐录影带]": {"desc": "Stylized, rhythmic.", "keywords": "dreamlike, fast cuts, motion blur, neon"},
    "🦁 Nature Documentary [自然纪录片]": {"desc": "Observational.", "keywords": "telephoto lens, natural sunlight, 8k"},
    "👻 Horror/Thriller [恐怖/惊悚]": {"desc": "Unsettling.", "keywords": "dutch angle, chiaroscuro, scary atmosphere"},
    "🤖 Sci-Fi / Cyberpunk [科幻/赛博]": {"desc": "Futuristic.", "keywords": "volumetric lighting, neon ambience, CGI"}
}

CAMERA_MOVEMENTS = {
    "🎥 Static / Fixed [固定镜头]": "No movement, stability.",
    "🎥 Slow Pan [缓慢摇镜]": "Horizontal scan.",
    "🎥 Tilt Up/Down [俯仰镜头]": "Vertical reveal.",
    "🎥 Dolly Zoom (Vertigo) [滑动变焦]": "Psychological tension.",
    "🎥 Tracking / Follow [跟随镜头]": "Following subject.",
    "🎥 Handheld / Shaky [手持晃动]": "Realism, chaos.",
    "🎥 Drone Flyover [无人机飞越]": "Aerial view.",
    "🎥 Rack Focus [移焦]": "Shift focus foreground/background.",
    "🎥 FPV Drone [第一人称无人机]": "Fast, acrobatic.",
    "🎥 Bullet Time [子弹时间]": "Frozen time."
}

LENS_CHOICES = {
    "👁️ 16mm (Ultra Wide) [超广角]": "Expansive, distortion.",
    "👁️ 35mm (Classic Wide) [人文广角]": "Storytelling, environmental.",
    "👁️ 50mm (Standard) [人眼视角]": "Natural look.",
    "👁️ 85mm (Portrait) [人像长焦]": "Flattering, compression.",
    "👁️ 200mm (Telephoto) [超长焦]": "Extreme compression, voyeuristic.",
    "👁️ Macro Lens [微距]": "Microscopic details."
}

SHOOTING_SUBJECTS = [
    "👤 Human Character [人物角色]",
    "📦 Product / Object [产品/静物]",
    "🏔️ Landscape / Environment [风景/环境]",
    "🚗 Vehicle / Mech [载具/机甲]",
    "👾 Creature / Monster [怪物/生物]"
]

FRAMING_OPTIONS = [
    "Wide Angle (Environmental) [大广角/环境]", 
    "Medium Shot (Waist Up) [中景/半身]", 
    "Close-up (Face/Detail) [特写/细节]", 
    "Extreme Close-up (Macro) [微距特写]",
    "Low Angle (Heroic) [低角度/仰视]", 
    "High Angle (Vulnerable) [高角度/俯视]", 
    "Dutch Angle (Dynamic) [倾斜构图]", 
    "Over-the-shoulder [过肩镜头]",
    "Isometric (God View) [等轴/上帝视角]",
    "Fisheye Lens (Distorted) [鱼眼镜头]",
    "Knolling (Flat Lay) [平铺直叙]",
    "Symmetrical (Center) [中心对称]"
]

DETAIL_LEVELS = [
    "High (Complex/Intricate) [高细节/繁复]", 
    "Medium (Balanced) [中等/平衡]", 
    "Low (Minimalist/Clean) [低细节/极简]"
]

# -----------------------------------------------------------------------------
# 🔠 THE GRAND TYPOGRAPHY MATRIX (字体设计核心矩阵 - v26 完整版)
# -----------------------------------------------------------------------------

# 1. 字体家族 (Font Family) - 风格的基调
TYPO_FONT_FAMILIES = {
    # --- 🇨🇳 东方书法 (Eastern Calligraphy) ---
    "🖌️ [CN] Oracle Bone [甲骨文]": "Knife-carved texture, sharp angles, pictographic roots, ancient bone texture, primitive lines.",
    "🖌️ [CN] Small Seal [小篆]": "Elongated vertical structure, perfect symmetry, rounded curves, iron-wire strokes, balanced.",
    "🖌️ [CN] Clerical Script [隶书]": "Flat structure, horizontal stress, silkworm head and swallow tail strokes, stone stele aesthetic.",
    "🖌️ [CN] Regular Script (Yan) [颜体楷书]": "Muscular strokes, square structure, facing inward, thick vertical lines, majestic, heavy ink.",
    "🖌️ [CN] Slender Gold [瘦金体]": "Razor-sharp lines, metallic hook strokes, thin and rigid, orchid-leaf pauses, noble elegance.",
    "🖌️ [CN] Wild Cursive [狂草]": "Continuous flowing stroke, chaotic speed, ink splatters, flying white (Fei Bai), emotional explosion.",
    "🖌️ [CN] Folk Vernacular [民间招牌字]": "Hand-painted, idiosyncratic balance, playful distortion, heavy brush, wet market aesthetic.",

    # --- 🏮 中国近代美术字 (Vintage Chinese) ---
    "🏮 [Vintage] Shanghai Art Deco [上海摩登]": "Elongated geometric Hanzi, decorative parallel lines, Gatsby orientalism, 1930s luxury.",
    "🏮 [Vintage] Revolution Bold [革命黑体]": "Super bold blocky font, negative space compression, aggressive angles, stencil propaganda, 1960s.",
    "🏮 [Vintage] Book Cover Style [民国书帧]": "Scattered composition, geometric collage, hand-drawn serif, rough paper texture, scholarly minimalist.",

    # --- 🇪🇺 西方经典 (Western Classic) ---
    "🅰️ Humanist Serif (Garamond) [人文衬线]": "Calligraphic roots, diagonal axis, organic stroke modulation, warm, traditional.",
    "🅰️ Transitional Serif (Baskerville) [过渡衬线]": "Sharper serifs, vertical axis, high contrast, rational, elegant.",
    "🅰️ Modern Didone (Bodoni) [现代衬线]": "Extreme thick/thin contrast, unbracketed hairline serifs, vertical stress, fashion luxury.",
    "🅰️ Slab Serif (Rockwell) [粗衬线]": "Heavy rectangular serifs, monoline weight, industrial strength, western, bold.",
    "🅰️ Neo-Grotesque (Helvetica) [新哥特/瑞士]": "Neutral, objective, uniform width, closed aperture, corporate cleanliness, modern.",
    "🅰️ Geometric Sans (Futura) [几何无衬线]": "Based on circle/square/triangle, modernist, bauhaus logic, architectural.",
    "🅰️ Blackletter (Textura) [哥特黑体]": "Medieval density, fractured strokes, diamond shapes, religious, heavy metal aesthetic.",

    # --- ✨ 现代与装饰 (Display & Modern) ---
    "✨ Graffiti Wildstyle [街头涂鸦]": "Interlocking letters, arrows, drips, spray paint texture, bubble letters, rebellious.",
    "✨ Pixel / 8-bit [像素字体]": "Aliased edges, grid-based, retro computing, blocky construction.",
    "✨ Kinetic / Distorted [动态扭曲]": "Melting text, wavy distortion, speed lines, psychedelic flow, glitch.",
    "✨ None (Pure Material) [纯材质]": "No specific font skeleton, focus purely on material effects."
}

# 2. 造字逻辑 (Construction) - 基于《The Stroke》
TYPO_CONSTRUCTION = {
    "✒️ Translation (Broad Nib) [平头笔平移]": "Contrast caused by fixed pen angle (translation). Thick verticals, thin diagonals.",
    "✒️ Expansion (Pointed Nib) [尖头笔膨胀]": "Contrast caused by pressure (expansion). Swelling strokes, copperplate style.",
    "✒️ Geometric / Drafting [尺规作图]": "Constructed with compass and ruler. Perfect circles, straight lines, mechanical.",
    "✒️ Modular / Grid [模块化/网格]": "Built from pre-set shapes (bricks/pixels). Lego-like, digital, systematic.",
    "✒️ Incised / Carved [刀刻/凿刻]": "Removed material. V-cut chiseled edges, sharp terminations, stone texture.",
    "✒️ Gestural / Handwritten [手势书写]": "Speed and movement driven. Organic inconsistency, human touch."
}

# 3. 重心控制 (Gravity / Visual Center) - NEW! 决定姿态
TYPO_GRAVITY = {
    "⬆️ High Center (Elegant) [高重心/修长]": "Visual center raised, elongated legs, elegant, spiritual, fragile, Art Nouveau vibe.",
    "⬇️ Low Center (Stable/Cute) [低重心/敦实]": "Visual center lowered, bottom-heavy, stable, cute, childish, retro cartoon vibe.",
    "⏺️ Geometric Center [绝对居中]": "Mathematically centered, balanced, neutral, Swiss style.",
    "↔️ Wide / Extended [扁平/宽展]": "Horizontally stretched, cinematic, architectural stability, low profile."
}

# 4. 中宫与负空间 (Counter / Zhonggong) - NEW! 决定松紧
TYPO_COUNTER = {
    "🕸️ Tight / Condensed [中宫紧凑/内敛]": "Small counters, strokes gathered at center, tense, sharp, traditional (Ou Style).",
    "👐 Wide / Open [中宫宽绰/舒展]": "Large counters, open aperture, strokes pushed to edges, modern, relaxed, legible.",
    "⚖️ Balanced [中宫适中]": "Standard readability, neutral spacing.",
    "💥 Exploded / Scattered [解构/离散]": "Parts separated, negative space dominating, abstract, deconstructivist."
}

# 5. 比例与法度 (Proportion) - 基于《字体设计艺术》
TYPO_PROPORTIONS = {
    "📐 Golden Ratio (1:1.618) [黄金分割]": "Divine proportion, organic spiral composition, classical beauty.",
    "📐 Renard Series [雷诺数序列]": "Industrial standardization, logical hierarchy, mathematical sizing.",
    "📐 Symmetrical / Axial [中轴对称]": "Formal, stable, religious or monumental composition, static balance.",
    "📐 Asymmetrical / Dynamic [动态非对称]": "Tension, movement, white space activation, modern Swiss style."
}

# 6. 材质与渲染 (Material Skin)
TYPO_MATERIALS = {
    "💡 Neon / Light Painting [霓虹光绘]": "Glowing tubes, cyberpunk, long exposure trails.",
    "💡 Bioluminescent [生物发光]": "Organic glow, deep sea, pulsing veins.",
    "💡 Chrome / Liquid Metal [液态铬]": "Highly reflective, mercury, fluid dynamics.",
    "💡 Holographic / Glitch [全息故障]": "Iridescent spectrum, chromatic aberration.",
    "🩸 Cinnabar & Gold [朱砂金粉]": "Red mineral pigment, gold flecks, royal paper.",
    "💧 Ink & Water [水墨晕染]": "Bleeding edges, wet-on-wet, wash effect.",
    "🗿 Stone / Concrete [碑刻/混凝土]": "Eroded texture, heavy, brutalist, architectural.",
    "🔥 Fire / Ember [火焰余烬]": "Burning letters, smoke, cracking lava.",
    "🌱 Organic / Overgrown [藤蔓共生]": "Vines, flowers, moss, reclaiming nature.",
    "✒️ Vector / Flat [平面矢量]": "Solid colors, clean edges, illustrator style.",
    "🎈 Inflatable / Soft [3D充气]": "Plastic sheen, rounded, claymorphism.",
    "🧊 Glass / Refraction [玻璃折射]": "Caustics, dispersion, crystal clear."
}

# 7. 应用场景 (Context)
TYPO_CONTEXTS = {
    "📢 Brand Identity (Logo) [品牌标志]": "Minimalist, scalable, recognition focus.",
    "🎬 Movie Poster (Title) [电影海报]": "Cinematic, atmospheric, dramatic scale.",
    "📰 Editorial (Magazine) [书籍画册]": "Readable, grid-based, elegant hierarchy.",
    "📱 UI Interface [界面设计]": "Functional, clean, legible.",
    "🏷️ Packaging Design [包装标签]": "Shelf impact, ornate or sterile.",
    "🎸 Album Cover [唱片封面]": "Experimental, abstract, expressive.",
    "🚧 Signage / Wayfinding [导视系统]": "High legibility, industrial materials.",
    "📜 Traditional Art [书法作品]": "Rice paper, seals, vertical layout."
}

# 8. 融合模式 (Fusion Alchemy)
TYPO_FUSIONS = {
    "⚗️ None (Pure Style) [纯粹风格]": "Strict adherence to selected parameters.",
    "⚗️ Cyber-Cursive [赛博狂草]": "Wild Cursive Script + Neon/Chrome.",
    "⚗️ Industrial Seal [工业篆刻]": "Small Seal + Concrete/Rust.",
    "⚗️ Neon Stone [霓虹碑林]": "Ancient Stone + Glowing Light.",
    "⚗️ Geometric Ink [几何水墨]": "Ink Wash + Bauhaus Geometry.",
    "⚗️ Organic Tech [生物科技]": "Circuit boards + Calligraphy."
}


# ==============================================================================
# 🎵 PART 6: THE MUSIC MASTER DATA (音乐核心库 - 双语汉化版)
# ==============================================================================

# 1. 音乐流派 (Genre)
MUSIC_GENRES = {
    # --- 🏛️ Classical & Orchestral (古典与管弦) ---
    "🎻 [Class] Baroque (Bach) [巴洛克时期]": "Harpsichord, counterpoint, fugue, intricate ornamentation, 60-80 BPM, chamber string.",
    "🎻 [Class] Romantic (Chopin/Liszt) [浪漫主义]": "Expressive piano, rubato, wide dynamic range, emotional swells, chromatic harmony.",
    "🎻 [Class] Impressionist (Debussy) [印象派]": "Whole-tone scale, fluid rhythm, harp textures, woodwinds, dreamlike atmosphere.",
    "🎻 [Class] Minimalist (Glass/Reich) [极简主义]": "Repetitive patterns, phasing, gradual evolution, arpeggios, hypnotic, pulse.",
    "🎻 [Cine] Epic Trailer (Hans Zimmer) [史诗预告片]": "Massive percussion, braams, ostinato strings, crescendo, heroic, hybrid orchestral.",
    "🎻 [Cine] Horror Avant-Garde [前卫恐怖配乐]": "Cluster chords, screeching strings, atonal, silence, sudden stabs, psychological tension.",

    # --- 🎹 Electronic & Dance (电子与舞曲) ---
    "🎹 [Elec] Techno (Berlin Industrial) [柏林Techno]": "125-135 BPM, 4/4 kick, dark atmosphere, mechanical textures, reverb kick, repetitive.",
    "🎹 [Elec] House (Chicago/Deep) [深邃浩室]": "120-126 BPM, soulful vocals, M1 organ bass, warm chords, groovy percussion.",
    "🎹 [Elec] Drum & Bass (Liquid) [液态鼓与贝斯]": "170-175 BPM, fast breakbeats, heavy sub-bass, atmospheric pads, soulful vocals.",
    "🎹 [Elec] Dubstep (Old School) [早期回响贝斯]": "140 BPM, half-time beat, sub-bass wobble, dark atmosphere, spacious reverb.",
    "🎹 [Elec] Synthwave / Retrowave [合成器波]": "80-100 BPM, analog synths, gated reverb drums, neon nostalgia, driving bassline.",
    "🎹 [Elec] IDM / Glitch [智能舞曲]": "Complex polyrhythms, granular synthesis, digital artifacts, Aphex Twin style.",
    "🎹 [Elec] Hyperpop (PC Music) [超流行]": "Distorted bass, pitched-up vocals, metallic textures, chaotic maximalism, bubblegum melody.",
    "🎹 [Elec] Ambient / Drone [环境长音]": "No rhythm, evolving textures, paulstretch, deep space reverb, meditation.",

    # --- 🎸 Rock, Metal & Punk (摇滚与金属) ---
    "🎸 [Rock] Classic Rock (70s) [经典摇滚]": "Overdriven guitar riffs, blues scale, Hammond organ, stadium drums, anthemic vocals.",
    "🎸 [Rock] Shoegaze [自赏/盯鞋]": "Wall of sound, heavy distortion/fuzz, drowned vocals, ethereal feedback, dream pop.",
    "🎸 [Rock] Math Rock [数学摇滚]": "Odd time signatures (7/8, 5/4), clean tapping guitar, complex structure, polyphonic.",
    "🎸 [Rock] Post-Rock [后摇]": "Long build-ups, tremolo picking, crescendo, lack of vocals, atmospheric to explosive.",
    "🎸 [Rock] Psychedelic Rock [迷幻摇滚]": "Phaser/Flanger effects, long jams, sitar influence, surreal lyrics, 60s vibe.",
    "🎸 [Metal] Thrash Metal [鞭挞金属]": "Fast tempo, aggressive palm-muted riffs, double kick drum, shouting vocals.",
    "🎸 [Metal] Black Metal [黑金属]": "Tremolo picking, blast beats, lo-fi production, high-pitched shrieking, cold atmosphere.",
    "🎸 [Metal] Doom / Sludge [毁灭金属]": "Extremely slow tempo, heavy fuzz, downtuned guitars, crushing wall of sound.",

    # --- 🎷 Jazz, Blues & Soul (爵士与蓝调) ---
    "🎷 [Jazz] Cool Jazz (Miles Davis) [酷派爵士]": "Relaxed tempo, trumpet mute, walking bass, brush drums, sophisticated harmony.",
    "🎷 [Jazz] Bebop [比波普]": "Fast tempo, complex chord changes, virtuoso improvisation, chaotic energy.",
    "🎷 [Jazz] Fusion [融合爵士]": "Electric instruments, funk rhythm, complex time signatures, synthesizer solos.",
    "🎷 [Blues] Delta Blues [三角洲蓝调]": "Slide guitar, acoustic, raw vocals, 12-bar progression, foot stomping.",
    "🎷 [Soul] Neo-Soul [新灵魂乐]": "Laid-back groove, drunk drums (Dilla beat), rhodes piano, smooth vocals.",

    # --- 🎤 Hip-Hop & Urban (嘻哈与都市) ---
    "🎤 [HipHop] Boom Bap (90s) [黄金年代]": "90 BPM, sampled drum breaks, heavy kick/snare, jazz samples, scratching.",
    "🎤 [HipHop] Trap (Atlanta) [陷阱音乐]": "140 BPM, 808 sub-bass, rattling hi-hats, triplet flow, dark melody.",
    "🎤 [HipHop] Lo-Fi Hip Hop [低保真嘻哈]": "70-90 BPM, vinyl crackle, swing drums, nostalgic piano, study vibes.",
    "🎤 [HipHop] Drill (UK/NY) [钻头音乐]": "Sliding 808 bass, dark piano, syncopated hi-hats, ominous atmosphere.",

    # --- 🌍 World & Folk (世界与民谣) ---
    "🌍 [World] Reggae / Dub [雷鬼/回响]": "Off-beat rhythm (skank), deep bass, space echo, delay effects, relaxed.",
    "🌍 [World] Bossa Nova [波萨诺瓦]": "Samba rhythm, nylon guitar, whispering vocals, shaker, beach vibe.",
    "🌍 [World] Flamenco [弗拉明戈]": "Spanish guitar, palmas (hand clapping), cajon, passionate vocals, Phrygian scale.",
    "🌍 [World] East Asian Traditional [东亚国风]": "Guzheng, Erhu, Pentatonic scale, nature sounds, zen garden atmosphere.",
    "🌍 [World] Celtic / Irish [凯尔特民谣]": "Fiddle, tin whistle, bodhran drum, jig rhythm, pastoral, lively.",
    "🌍 [World] Afrobeat [非洲节拍]": "Polyrhythmic percussion, horn section, funky guitar, high energy, danceable."
}

# 2. 配器与音色 (Instruments)
MUSIC_INSTRUMENTS = {
    # --- 传统 ---
    "🎻 Orchestral Full Ensemble [全管弦乐团]": "String section, Brass section, Woodwinds, Timpani, Harp.",
    "🎻 String Quartet [弦乐四重奏]": "Two violins, viola, cello, intimate, chamber sound.",
    "🎹 Grand Piano (Solo) [独奏三角钢琴]": "Steinway sound, reverberant, dynamic velocity, classical or jazz.",
    "🎸 Acoustic Guitar (Fingerstyle) [指弹吉他]": "Steel string, intimate mic, fret noise, harmonics, warm.",
    
    # --- 电子 ---
    "🎹 Analog Synths (Moog/Prophet) [模拟合成器]": "Warm saw waves, filter sweeps, lush pads, fat basslines.",
    "🎹 TB-303 Acid [酸性贝斯]": "Resonant filter, squelchy sound, distorted bass, hypnotic.",
    "🎹 FM Synthesis (Yamaha DX7) [FM合成]": "Bell-like tones, glassy electric piano, 80s crystal sound.",
    "🥁 Drum Machine (TR-808/909) [传奇鼓机]": "Deep kick, crispy clap, sizzling hi-hats, robotic groove.",
    
    # --- 乐队 ---
    "🎸 Rock Band Setup [摇滚配置]": "Distorted Electric Guitar, Bass Guitar, Drum Kit.",
    "🎷 Jazz Combo [爵士组合]": "Double Bass, Piano, Drum Kit (Brushes), Saxophone/Trumpet.",
    
    # --- 民族与实验 ---
    "🎎 Traditional Asian [传统民乐]": "Guzheng, Shakuhachi, Erhu, Taiko Drums.",
    "🧬 Modular Eurorack [模块化实验]": "Bleeps, blobs, random voltage, granular texture, sine waves.",
    "🎤 Choir (Epic/Gothic) [史诗合唱]": "Massive choir, Latin chanting, soprano soaring, apocalyptic."
}

# 3. 结构与节奏 (Structure)
MUSIC_STRUCTURES = {
    "🎼 Loop / Seamless [无缝循环]": "Continuous repetition, background music, game loop, steady energy.",
    "🎼 Build-up & Drop [铺垫与爆发]": "EDM structure, rising tension followed by explosive release.",
    "🎼 Crescendo (Epic) [渐强/高潮]": "Slow start, gradually getting louder and fuller, emotional peak.",
    "🎼 A-B-A (Classical) [三部曲式]": "Theme A, contrasting Theme B, return to Theme A.",
    "🎼 Free Improvisation [即兴/自由]": "No fixed structure, wandering, jazz-like, evolving."
}

# 4. 制作技术 (Production)
MUSIC_PRODUCTION = {
    "🎛️ High Fidelity (Studio) [高保真]": "Crystal clear, wide stereo width, mastering quality, perfect separation.",
    "🎛️ Lo-Fi / Vintage Tape [磁带低保真]": "Tape saturation, wow and flutter, reduced high-end, hiss noise.",
    "🎛️ Vinyl Sampling [黑胶采样]": "Crackling noise, warm mid-range, sampled texture, MPC style.",
    "🎛️ Spatial / 8D Audio [空间音频]": "Binaural panning, 3D reverb, immersive atmosphere, surround sound.",
    "🎛️ Wall of Sound [音墙]": "Dense layering, heavy reverb, overwhelmed senses, shoegaze style.",
    "🎛️ Dry / Intimate [干声/贴耳]": "No reverb, close-mic recording, ASMR-like presence, bedroom pop."
}

# 5. 情绪与氛围 (Mood) - 列表形式
MUSIC_MOODS = [
    "🔥 Energetic / Adrenaline [激情/肾上腺素]", 
    "💧 Melancholic / Sad [忧伤/孤独]", 
    "🌿 Peaceful / Zen [宁静/禅意]", 
    "👻 Eerie / Scary [诡异/恐怖]", 
    "💖 Romantic / Sentimental [浪漫/深情]", 
    "🚀 Uplifting / Heroic [激昂/史诗]",
    "🌌 Mysterious / Ethereal [神秘/空灵]", 
    "🤖 Robotic / Cold [机械/冷酷]"
]


# ==============================================================================
# 🎤 PART 7: THE LYRICIST DATA (作词核心库 - v30 新增)
# ==============================================================================

# 1. 歌曲结构模版 (Song Structure)
LYRIC_STRUCTURES = {
    "🎼 Standard Pop [标准流行]": {
        "desc": "Radio hit formula.",
        "format": "Intro -> Verse 1 -> Pre-Chorus -> Chorus -> Verse 2 -> Pre-Chorus -> Chorus -> Bridge -> Chorus -> Outro"
    },
    "🎼 Rap / Hip-Hop Flow [说唱流]": {
        "desc": "Bar-heavy focus.",
        "format": "Intro -> Hook -> Verse 1 (16 bars) -> Hook -> Verse 2 (16 bars) -> Hook -> Outro"
    },
    "🎼 Ballad / Storytelling [民谣叙事]": {
        "desc": "Linear storytelling.",
        "format": "Verse 1 -> Chorus -> Verse 2 -> Chorus -> Verse 3 -> Chorus -> Outro (Fade)"
    },
    "🎼 EDM / Dance Structure [电子舞曲]": {
        "desc": "Focus on the Drop.",
        "format": "Intro -> Verse -> Build-up -> DROP (Minimal Vocals) -> Verse -> Build-up -> DROP -> Outro"
    },
    "🎼 TikTok Viral Short [短视频热歌]": {
        "desc": "Immediate hook.",
        "format": "Chorus (Hook) -> Verse -> Pre-Chorus -> Chorus -> Outro"
    },
    "🎼 AABA (Jazz Standard) [爵士标准]": {
        "desc": "Classic 32-bar form.",
        "format": "Verse A -> Verse A -> Bridge B -> Verse A"
    },
    "🎼 Progressive Odyssey [前卫史诗]": {
        "desc": "Evolving journey, Bohemian Rhapsody style.",
        "format": "Intro -> Ballad Section -> Opera Section -> Heavy Rock Section -> Outro"
    },
    "🎼 Call and Response [启应形式]": {
        "desc": "Gospel/Folk tradition.",
        "format": "Leader Line -> Group Response -> Leader Line -> Group Response (Repeat)"
    }
}

# 2. 韵脚方案 (Rhyme Scheme)
RHYME_SCHEMES = {
    "📝 AABB (Couplets) [双句押韵]": "Lines 1-2 rhyme, Lines 3-4 rhyme. Simple, nursery rhyme or pop feel.",
    "📝 ABAB (Alternate) [交叉押韵]": "Line 1 rhymes with 3, Line 2 rhymes with 4. Balanced and lyrical.",
    "📝 AAAA (Monorhyme) [单押]": "Every line ends with the same rhyme sound. Intense, often used in Rap/Trap.",
    "📝 XAXA (Simple) [隔行押韵]": "Only lines 2 and 4 rhyme. Natural, conversational, less constrained.",
    "📝 AABCCB (Limerick) [五行打油诗]": "Specific rhythm for limericks or playful songs.",
    "📝 Internal Rhyme [句内押韵]": "Rhymes occur within the line, not just at the end. Complex flow (Rap).",
    "📝 Slant Rhyme [斜韵/不完美押韵]": "Words sound similar but don't rhyme perfectly. Indie/Alternative feel.",
    "📝 Free Verse [自由诗]": "No strict rhyme scheme. Focus on imagery, emotion, and prose-like flow."
}

# 3. 歌词主题与语境 (Themes)
LYRIC_THEMES = {
    # --- 情感 ---
    "💖 Love & Romance [爱情/浪漫]": "Heartbreak, first love, longing, devotion, toxic relationship.",
    "💧 Melancholy & Loss [忧伤/失去]": "Grief, nostalgia, missing someone, rainy days, loneliness.",
    
    # --- 态度 ---
    "🔥 Empowerment / Hustle [励志/奋斗]": "Overcoming obstacles, winning, grinding, success, underdog story.",
    "🤬 Rebellion / Angst [叛逆/愤怒]": "Fighting the system, punk spirit, teenage angst, breaking rules.",
    "😎 Flex / Braggadocio [炫耀/自信]": "Luxury, fashion, confidence, party lifestyle (Rap/Pop).",
    
    # --- 场景 ---
    "🌃 Urban / Nightlife [城市/夜生活]": "Neon lights, driving at night, clubbing, insomnia, city skyline.",
    "🌿 Nature / Folk [自然/民谣]": "Mountains, rivers, wandering, seasons, rustic life, campfire.",
    "🚀 Sci-Fi / Cyber [科幻/未来]": "Space travel, AI, dystopia, virtual reality, neon future.",
    
    # --- 哲学 ---
    "🧘 Inner Self / Reflection [内省/思考]": "Depression, anxiety, growth, existential questions, mental health.",
    "⚔️ Story / Epic [故事/史诗]": "Myths, battles, legends, historical events, hero's journey."
}

# 4. 语言风格 (Language Style)
LYRIC_LANGUAGES = [
    "🇺🇸 English (Modern Pop) [现代英语]",
    "🇺🇸 English (Old School HipHop) [街头英语]",
    "🇺🇸 English (Shakespearean) [古典英语]",
    "🇨🇳 Chinese (Mandarin Pop) [华语流行]",
    "🇨🇳 Chinese (Classical/Gufeng) [古风辞藻]",
    "🇨🇳 Chinese (Rap Flow) [中文说唱]",
    "🇯🇵 Japanese (Anime/J-Pop) [日语]",
    "🇰🇷 Korean (K-Pop) [韩语]",
    "🇫🇷 French (Chanson) [法语香颂]",
    "🇪🇸 Spanish (Reggaeton) [西语/雷鬼顿]",
    "🌍 Mixed (English + Native) [混合双语]"
]


# ==============================================================================
# 📝 PART 8: THE SHOWRUNNER ARSENAL (编剧天花板库 - v40 史诗级扩容)
# ==============================================================================

# 1. 叙事结构 (保留 v39)
STORY_STRUCTURES = {
    "📖 Save the Cat (Blake Snyder) [救猫咪/商业片]": {"desc": "Commercial standard.", "steps": "Setup -> Catalyst -> Fun & Games -> All is Lost -> Finale"},
    "📖 The Hero's Journey [英雄之旅/史诗]": {"desc": "Mythological.", "steps": "Call -> Threshold -> Abyss -> Atonement -> Return"},
    "📖 Kishotenketsu [起承转合/东方]": {"desc": "No conflict focus.", "steps": "Intro -> Development -> Twist -> Conclusion"},
    "📖 Three-Act Structure [经典三幕式]": {"desc": "Aristotelian.", "steps": "Setup -> Confrontation -> Resolution"},
    "📖 Non-Linear / Pulp Fiction [非线性/乱序]": {"desc": "Time jump.", "steps": "End -> Beginning -> Middle -> End (Reveal)"},
    "📖 Dan Harmon's Circle [故事环/美剧]": {"desc": "TV logic.", "steps": "Comfort -> Want -> Go -> Search -> Find -> Take -> Return -> Change"},
    "📖 Rashomon Effect [罗生门/多视角]": {"desc": "Subjective truth.", "steps": "Perspective A -> Perspective B -> Perspective C -> Ambiguous Truth"},
    "📖 Viral Short Loop [短视频闭环]": {"desc": "Designed for TikTok/Reels retention.","steps": "Visual Hook (0-3s) -> Value Prop -> Twist/reveal -> Call to Action -> Loop back to start"},
    "📖 In Media Res [从中间开始]": {"desc": "Starting in the middle of action.","steps": "Climax/Action -> Flashback (How we got here) -> Resolution"},
}

# 2. 角色原型 (保留 v39)
CHARACTER_ARCHETYPES = {
    "👤 The Hero / Warrior [英雄/战士]": "Courageous, sacrificing.",
    "👤 The Mentor / Sage [导师/智者]": "Wise, guiding.",
    "👤 The Trickster [捣蛋鬼/混乱]": "Chaos agent, comic relief.",
    "👤 The Shadow / Villain [阴影/反派]": "Dark reflection of hero.",
    "👤 The Anti-Hero [反英雄]": "Flawed, morally grey, reluctant.",
    "👤 The Femme Fatale [蛇蝎美人]": "Seductive, dangerous, manipulative.",
    "👤 The Caregiver [守护者]": "Altruistic, protecting.",
    "👤 The Creator [创造者]": "Imaginative, perfectionist."
}

# --- 🔥 NEW: 冲突引擎 (The Conflict Engine) ---
DRAMATIC_CONFLICTS = {
    "⚔️ Man vs. Self (Internal) [内心冲突/救赎]": "The battle is within. Addiction, trauma, moral dilemma, identity crisis. (e.g. Fight Club)",
    "⚔️ Man vs. Man (Interpersonal) [人际冲突/博弈]": "Direct antagonism. Protagonist vs Antagonist. Rivalry, revenge. (e.g. The Dark Knight)",
    "⚔️ Man vs. Society (Dystopia) [社会冲突/反乌托邦]": "Individual against the system, laws, or culture. (e.g. 1984, Joker)",
    "⚔️ Man vs. Nature (Survival) [自然冲突/求生]": "Surviving against elements, beasts, or disasters. (e.g. The Revenant)",
    "⚔️ Man vs. Technology (Sci-Fi) [科技冲突/奇点]": "AI, robots, or unchecked science threatening humanity. (e.g. Ex Machina)",
    "⚔️ Man vs. Supernatural [超自然冲突/灵异]": "Ghosts, demons, gods, or cosmic horror. (e.g. The Exorcist)",
    "⚔️ Man vs. Fate (Tragedy) [命运冲突/悲剧]": "Fighting a destined outcome, prophecy, or time loop. (e.g. Oedipus, Tenet)"
}

# --- 🗣️ NEW: 对白风格 (Dialogue Stylization) ---
DIALOGUE_STYLES = {
    "🗣️ Sorkin-esque (Snappy) [索尔金式/快节奏]": "Walk and talk, rapid fire, witty, intellectual, overlapping, high information density.",
    "🗣️ Tarantino-esque (Pop) [塔伦蒂诺式/话痨]": "Long digressions, pop culture references, mundane conversations before violence, cool.",
    "🗣️ Hemingway (Iceberg) [冰山理论/极简]": "Minimalist, subtext-heavy, short sentences, what is unsaid is more important.",
    "🗣️ Shakespearean (Poetic) [莎翁式/诗意]": "Monologues, metaphors, heightened language, archaic rhythm, dramatic.",
    "🗣️ Nolan-esque (Exposition) [诺兰式/解说]": "Complex concepts explained through dialogue, philosophical, time-focused.",
    "🗣️ Mumblecore (Natural) [自然主义/碎碎念]": "Improvisational feel, stammering, overlapping, realistic, awkward."
}

# --- 🧩 NEW: 叙事诡计 (Narrative Devices) ---
NARRATIVE_DEVICES = {
    "🧩 Chekhov's Gun [契诃夫之枪]": "Setup an object early that must be used later.",
    "🧩 Red Herring [红鲱鱼/误导]": "A misleading clue to distract the audience from the truth.",
    "🧩 Deus Ex Machina [机械降神]": "Sudden, unexpected intervention to save the day (use carefully).",
    "🧩 In Media Res [半路杀出]": "Start the scene in the middle of action, explain later.",
    "🧩 Breaking the 4th Wall [打破第四面墙]": "Characters address the audience directly (Deadpool style).",
    "🧩 Unreliable Narrator [不可靠叙述者]": "The storyteller is lying or insane.",
    "🧩 Irony (Dramatic) [戏剧反讽]": "The audience knows something the characters don't."
}

# --- 🔚 NEW: 结局类型 (Ending Types) ---
ENDING_TYPES = {
    "🏁 Twist Ending [反转结局]": "Shocking reveal that recontextualizes the whole story.",
    "🏁 Ambiguous / Open [开放式结局]": "Left to interpretation (e.g. Inception top).",
    "🏁 Bittersweet [苦乐参半]": "Victory at a heavy cost (e.g. La La Land).",
    "🏁 Cliffhanger [悬念结局]": "Unresolved tension setup for a sequel.",
    "🏁 Circular [循环结局]": "Ending right where it began.",
    "🏁 Deus Ex Machina [大团圆]": "Happy ending against all odds."
}

SCRIPT_FORMATS = {
    "📜 Standard Screenplay [标准电影剧本]": "Scene Headings (INT./EXT.), Action, Dialogue, Parentheticals.",
    "📜 AV Script (Commercial) [AV分栏脚本]": "Two columns: Audio (Dialogue/SFX) vs Visual (Shot description).",
    "📜 Novel / Short Story [小说/短篇]": "Prose format, focusing on internal monologue and sensory details.",
    "📜 TikTok / Reel Script [短视频脚本]": "Time-coded, fast-paced, visual cues, sound effects notes.",
    "📜 Game Dialogue Tree [游戏对话树]": "Branching options, player choices, NPC responses."
}

STORY_TONES = [
    "🌑 Dark / Gritty [黑暗/粗粝]", "🌟 Hopeful / Wholesome [希望/治愈]", 
    "🤣 Satirical / Absurd [讽刺/荒诞]", "🧠 Psychological / Cerebral [心理/烧脑]", 
    "💖 Romantic / Melodramatic [浪漫/煽情]", "⚡ High-Octane / Thriller [紧张/动作]",
    "👻 Eerie / Lovecraftian [诡异/克苏鲁]", "🤖 Hard Sci-Fi [硬科幻]"
]


# ==============================================================================
# 🛡️ PART 9: THE ULTIMATE LOGO DATA (标志设计核心库 - v42 终极版)
# ==============================================================================

# 1. 标志类型 (Logo Types) - 细分
LOGO_TYPES = {
    "🛡️ Pictorial Mark (Icon) [具象图形标]": "Literal image (Apple, Twitter). Recognizable, clear representation.",
    "🛡️ Abstract Mark [抽象图形标]": "Geometric conceptual shape (Nike, Pepsi). Ambiguous, metaphorical.",
    "🛡️ Monogram / Lettermark [字母标]": "Initials/Acronyms (IBM, HP, LV). Typographic structure, focus on font.",
    "🛡️ Wordmark (Logotype) [字标]": "Full brand name text only (Google, Coca-Cola). Custom typography.",
    "🛡️ Emblem / Badge [徽章/纹章]": "Text inside symbol (Starbucks, Harvard). Traditional, authoritative, contained.",
    "🛡️ Mascot [吉祥物]": "Character based (KFC, Pringles). Friendly, personified, illustrative.",
    "🛡️ Combination Mark [图文组合]": "Icon + Text. Versatile, standard commercial usage.",
    "🛡️ Dynamic / Fluid [动态/流体标]": "Changing shapes (MTV). Adaptable, organic, digital-first."
}

# 2. 设计风格 (Design Aesthetics)
LOGO_STYLES = {
    "🎨 Swiss Minimalist [瑞士极简]": "Paul Rand style. No gradients, solid colors, geometric, timeless.",
    "🎨 Geometric Grid [几何网格]": "Built with circles/squares, golden ratio, mathematically perfect.",
    "🎨 Negative Space [负空间]": "Hidden shapes in empty space (FedEx arrow). Clever, intellectual.",
    "🎨 Line Art / Monoline [单线条]": "Consistent stroke weight, airy, modern hipster, elegant.",
    "🎨 Gradient / Glass [渐变毛玻璃]": "Vibrant transitions, soft shadows, tech startup, iOS icon style.",
    "🎨 Vintage / Badge [复古徽章]": "Textured, stamp effect, rough edges, 19th-century etching style.",
    "🎨 3D Isometric [3D等轴]": "Depth, blocky, architectural, tech-focused, impossible shapes.",
    "🎨 Hand-Drawn / Organic [手绘有机]": "Imperfect lines, ink bleed, human touch, artisanal.",
    "🎨 Glitch / Cyber [故障赛博]": "Distorted, pixelated, digital noise, futuristic."
}

# 3. 几何构建逻辑 (Geometry & Gestalt) - NEW! 专业核心
LOGO_GEOMETRY = {
    "📐 Golden Ratio Circles [黄金圆切]": "Constructed using Fibonacci circles. Perfect curves, organic balance (e.g. Twitter bird).",
    "📐 Boolean Operations [布尔运算]": "Union, Subtract, Intersect. Sharp cuts, clean geometric logic.",
    "📐 Gestalt: Closure [格式塔:闭合]": "Incomplete shapes that the eye completes (e.g. WWF Panda).",
    "📐 Gestalt: Figure-Ground [格式塔:正负形]": "Ambiguous relationship between object and background.",
    "📐 Symmetrical Balance [对称平衡]": "Mirror image, stability, formality, traditional authority.",
    "📐 Asymmetrical Dynamic [动态非对称]": "Motion, tension, modernism, forward-looking.",
    "📐 Impossible Geometry [不可能图形]": "Escher-like optical illusions, penrose triangle, dimensional play."
}

# 4. 色彩心理学 (Color Psychology) - NEW!
LOGO_COLORS = {
    "🎨 Trust & Security (Blue) [信任/安全]": "Navy, Azure. Tech, Banks, Medical. Calm, professional.",
    "🎨 Passion & Urgency (Red) [激情/紧迫]": "Crimson, Scarlet. Food, Sports, Clearance. Energy, hunger.",
    "🎨 Luxury & Authority (Black/Gold) [奢华/权威]": "Matte Black, Foil Gold. Fashion, Cars. Sophistication.",
    "🎨 Growth & Health (Green) [生长/健康]": "Leaf, Emerald. Eco, Finance, Wellness. Balance, money.",
    "🎨 Creative & Friendly (Orange/Yellow) [创意/友好]": "Tangerine, Sunflower. Kids, Art, Food. Optimism.",
    "🎨 Innovation & Wisdom (Purple) [创新/智慧]": "Violet, Lavender. Creative agency, Spiritual. Royal.",
    "🎨 Minimalist (B&W) [极简黑白]": "Stark contrast. High fashion, Architecture. Timelessness."
}

# 5. 行业应用 (Industry)
LOGO_INDUSTRIES = {
    "💻 Tech & SaaS [科技软件]": "Nodes, clouds, pixels, circuit, abstract connectivity.",
    "🍔 Food & Beverage [餐饮食品]": "Appetizing shapes, steam, organic curves, warm vibes.",
    "👗 Fashion & Luxury [时尚奢华]": "Monogram, serif font, thin lines, crests, minimalist.",
    "🏥 Medical & Wellness [医疗健康]": "Crosses, hearts, leaves, DNA, clean curves, sterile.",
    "🎮 Gaming & Esports [游戏电竞]": "Mascots, shields, sharp angles, aggressive strokes, glow.",
    "🏡 Real Estate [房产建筑]": "Roofs, pillars, skylines, geometric stability, keyholes.",
    "🚀 Crypto & Web3 [加密/Web3]": "Blocks, chains, coins, futuristic nodes, abstract currency.",
    "🎓 Education [教育]": "Books, torches, owls, shields, open doors, growth."
}

# 6. 品牌原型 (Brand Archetypes)
BRAND_ARCHETYPES = {
    "🧠 The Sage [智者]": "Truth, knowledge. (Google). Clean, Serif.",
    "👑 The Ruler [统治者]": "Power, control. (Rolex). Crests, Symmetry.",
    "⚡ The Hero [英雄]": "Mastery, courage. (Nike). Angular, Bold.",
    "👶 The Innocent [天真者]": "Safety, purity. (Dove). Soft, Rounded.",
    "🎨 The Creator [创造者]": "Innovation. (Lego). Colorful, Dynamic.",
    "❤️ The Lover [爱人]": "Intimacy. (Chanel). Elegant, Script.",
    "🤡 The Jester [小丑]": "Joy. (M&M's). Playful, Mascot.",
    "🌍 The Explorer [探险家]": "Freedom. (Jeep). Rugged, Earthy.",
    "🧙‍♂️ The Magician [魔法师]": "Transformation. (Disney). Sparkles, Fluid.",
    "🤠 The Outlaw [叛逆者]": "Revolution. (Harley). Rough, Grunge."
}


# ==============================================================================
# 🎨 PART 10: COLOR SCIENCE & GRADING (调色师核心库 - v50 新增)
# ==============================================================================

# 1. 色彩和声 (Color Harmony) - 基于色彩轮理论
COLOR_HARMONIES = {
    "🎨 Complementary (Teal/Orange) [互补色/青橙]": "Opposite colors on the wheel. High contrast, dynamic, cinematic standard (Blockbuster look).",
    "🎨 Analogous (Harmonious) [类似色/和谐]": "Colors next to each other. Serene, comfortable, nature-like (e.g., Green/Blue/Teal).",
    "🎨 Triadic (Vibrant) [三等分/活跃]": "Three colors evenly spaced. Balanced but colorful, cartoon/pop art vibe.",
    "🎨 Monochromatic (Mood) [单色系/情绪]": "Single hue with varying saturation/brightness. Atmospheric, focused, nostalgic.",
    "🎨 Split-Complementary [分裂互补]": "Base color + two adjacent to its opposite. High contrast but less tension than complementary.",
    "🎨 Tetradic (Double Comp) [矩形/双互补]": "Two pairs of complementary colors. Rich, complex, hard to balance, colorful."
}

# 2. 电影调色风格 (Cinematic Looks) - 工业级LUTs
CINEMATIC_LOOKS = {
    "🎞️ Teal & Orange (Blockbuster) [好莱坞青橙]": "Push shadows to teal, highlights to orange. Separates skin tones from background.",
    "🎞️ Bleach Bypass (War/Gritty) [漂白跳过/银留]": "High contrast, low saturation. Metallic, harsh, gritty (Saving Private Ryan).",
    "🎞️ Technicolor (Vintage) [特艺彩色/复古]": "Hyper-saturated, vibrant reds and greens, 1950s Hollywood aesthetic (Wizard of Oz).",
    "🎞️ Cyberpunk Neon [赛博霓虹]": "High contrast black crush, emissive cyan/magenta/purple, night city vibe.",
    "🎞️ Matrix Green [黑客帝国绿]": "Green tint in shadows and midtones, sickness, digital, unnatural.",
    "🎞️ Wes Anderson Pastel [韦斯安德森粉]": "High key, low contrast, warm pastel pinks/yellows/blues, storybook feel.",
    "🎞️ Kodak 2383 Print [柯达胶片感]": "Rich blacks, warm highlights, slight grain, the 'standard' film look.",
    "🎞️ Noir B&W [黑色电影/黑白]": "High contrast black and white, deep shadows, rim light, silver screen look."
}

# 3. 胶片与色彩空间 (Film Stocks & Color Space)
COLOR_SPACES = {
    "📼 Kodak Portra 400 [人像王]": "Excellent skin tones, fine grain, warm and natural saturation.",
    "📼 Fujifilm Velvia 50 [风景王]": "High saturation, high contrast, deep blacks, vivid nature colors.",
    "📼 Cinestill 800T [夜景王]": "Tungsten balanced, halation around lights (red glow), moody night shots.",
    "📼 Ilford HP5 Plus [纪实黑白]": "Classic B&W, medium contrast, visible grain, documentary feel.",
    "💻 Rec.709 (Standard) [标准广播级]": "Standard dynamic range, realistic, TV broadcast look.",
    "💻 ACEScg (CGI) [线性工作流]": "Ultra-wide gamut, photorealistic rendering, distinct highlight roll-off."
}

# ==============================================================================
# 👤 PART 11: CONCEPT ARTIST DATA (概念设计库 - v50 新增)
# ==============================================================================

# 1. 视图类型 (View Types) - 资产标准化
CONCEPT_VIEWS = {
    "📐 Character Sheet (Full) [角色设定图]": "Full body front, side, back views, plus accessories breakdown.",
    "📐 Orthographic Turnaround [正交三视图]": "T-Pose or A-Pose, Front/Side/Back, flat lighting, for 3D modeling.",
    "📐 Expression Sheet [表情集]": "Headshots showing different emotions (Joy, Anger, Sadness, Surprise).",
    "📐 Dynamic Action Pose [动态姿势]": "Character in combat or motion, foreshortening, dramatic angle.",
    "📐 Asset Breakdown [资产拆解]": "Close-up of weapons, jewelry, or shoes, showing material details.",
    "📐 Environment Mood Shot [环境概念]": "Wide shot establishing atmosphere, scale, and lighting."
}

# 2. 设计风格 (Art Styles for Concept)
CONCEPT_STYLES = {
    "🖌️ Anime Lineart (Cel) [日系线稿/赛璐璐]": "Clean lines, flat shading, distinct shadows, Ghibli/Design document style.",
    "🖌️ Thick Paint / Impasto [厚涂/油画感]": "Visible brushstrokes, rich colors, Riot Games / Blizzard splash art style.",
    "🖌️ Photobash / Matte Painting [照片合成]": "Realistic textures mixed with painting, cinematic realism, high detail.",
    "🖌️ Sketch / Blueprint [素描/蓝图]": "Pencil or blue lines, rough, construction lines visible, technical feel.",
    "🖌️ 3D Render (Clay) [3D白模]": "Ambient occlusion, grey clay material, focus on volume and silhouette."
}

# ==============================================================================
# 🧐 PART 12: ART CRITIC CRITERIA (艺术评论标准 - v50 新增)
# ==============================================================================

CRITIC_CRITERIA = {
    "🧐 Composition & Balance [构图与平衡]": "Rule of thirds, guiding lines, visual weight distribution.",
    "🧐 Anatomy & Proportion [人体结构]": "Correct hands, limbs, facial proportions, realistic posing.",
    "🧐 Lighting & Shadow [光影]": "Contrast, light source consistency, volumetric atmosphere.",
    "🧐 Color Harmony [色彩和谐]": "Palette consistency, saturation balance, color storytelling.",
    "🧐 Fidelity & Texture [画质与纹理]": "Sharpness, noise level, material realism (skin, metal).",
    "🧐 Aesthetics & Style [美学风格]": "Adherence to the requested style (e.g. Cyberpunk, Oil Paint)."
}

# ==============================================================================
# 🎨 PART 13: ADVANCED INDUSTRIAL DATA (v51 深度扩容)
# ==============================================================================

# 1. 胶片颗粒与质感 (Film Grain & Texture)
FILM_GRAIN_TYPES = {
    "📼 Fine / Digital Clean [细腻/数码洁净]": "Noiseless, smooth, glossy, commercial look (Sony/Canon).",
    "📼 16mm Vintage Grain [16mm复古颗粒]": "Visible fuzz, soft edges, nostalgic, indie movie vibe.",
    "📼 35mm Cinematic Grain [35mm电影颗粒]": "Balanced texture, organic warmth, Kodak Vision3 standard.",
    "📼 8mm Home Video [8mm家用录像带]": "Heavy grain, scratches, dust, low fidelity, memory-like.",
    "📼 VHS Tape Artifacts [VHS磁带干扰]": "Scanlines, chromatic noise, tracking errors, retro 80s/90s.",
    "📼 Bleach Bypass Grit [漂白跳过/粗粝]": "High contrast, metallic texture, desaturated, war movie feel."
}

# 2. 概念设计：材质拆解 (Material Breakdown)
CONCEPT_MATERIALS = {
    "🛠️ PBR Realistic [PBR物理写实]": "4K textures, leather pores, metal scratches, fabric weave.",
    "🛠️ Hand-Painted (Stylized) [手绘风格化]": "Baked lighting, brush strokes, Blizzard/League of Legends style.",
    "🛠️ Cel-Shaded (Anime) [赛璐璐/二次元]": "Flat colors, hard shadows, outline (rim line), clean.",
    "🛠️ Ethereal / Spirit [灵体/能量]": "Translucent, glowing, sub-surface scattering, particle effects.",
    "🛠️ Cybernetic / Hard Surface [硬表面/机械]": "Carbon fiber, brushed steel, emissive LEDs, joints and bolts."
}

# 3. 审稿：对比维度 (Comparison Criteria)
CRITIC_MODES = {
    "🧐 Fidelity Check [画质/崩坏检查]": "Check for bad hands, extra limbs, blur, distortions.",
    "🧐 Style Consistency [风格一致性]": "Does the image match the reference style? (e.g. Is it truly Cyberpunk?)",
    "🧐 Composition & Lighting [构图与光影]": "Rule of thirds, depth, contrast, volumetric atmosphere.",
    "🧐 Concept Accuracy [题意相符度]": "Does the image actually show what the prompt asked for?",
    "🧐 Color Grading [调色分析]": "Saturation, white balance, harmony, emotional impact."
}


# ==============================================================================
# 🌍 PART 14: THE DEMIURGE DATA (世界构建核心库 - v61 极限专业版)
# ==============================================================================

# 1. 文明等级 (Kardashev Scale & Society)
CIVILIZATION_LEVELS = {
    "🌍 Type 0: Pre-Industrial [前工业文明]": "Feudalism, agrarian, swords and castles, low tech, high superstition.",
    "🌍 Type I: Planetary [行星文明]": "Cyberpunk, megacities, control of weather, internet of things, fusion power.",
    "🌍 Type II: Stellar (Dyson Sphere) [恒星文明]": "Space colonization, dyson spheres, star harvesting, post-scarcity.",
    "🌍 Type III: Galactic [星系文明]": "Warp drive, time manipulation, cosmic horror, god-like entities.",
    "🌍 Post-Apocalyptic [后启示录]": "Scavenger economy, tribalism amidst ruins, lost technology, survival."
}

# 2. 魔法/科技体系 (Magic & Tech Systems) - 基于 Sanderson 定律
MAGIC_SYSTEMS = {
    "🔮 Hard Magic (Rule-Based) [硬魔法体系]": "Strict rules, equivalent exchange, runes, alchemy, scientific approach to magic.",
    "🔮 Soft Magic (Mystical) [软魔法体系]": "Sense of wonder, undefined limits, Gandalf-style, spiritual, miraculous.",
    "🔮 Magitech / Hextech [魔导科技]": "Magic powering machines, crystals, steampunk with spells, artificers.",
    "🔮 Bio-Punk / Genetic [生物改造]": "Genetic engineering as magic, mutations, flesh-crafting, organic ships.",
    "🔮 Psionics / The Force [灵能/原力]": "Mind over matter, telekinesis, mental connection, cosmic energy."
}

# 3. 地理与生态 (Geography & Biomes)
WORLD_GEOGRAPHY = {
    "🗺️ Arcology / Mega-City [巨型生态城]": "Vertical cities, neon canyons, layered society (Upper/Lower city).",
    "🗺️ Floating Islands [浮空岛]": "Anti-gravity rocks, waterfalls into void, airships, celestial atmosphere.",
    "🗺️ Subterranean / Underdark [地底世界]": "Bioluminescent caves, fungal forests, ancient ruins, claustrophobic.",
    "🗺️ Wasteland / Desert [废土荒原]": "Dunes, rusted wrecks, toxic storms, scarcity, Mad Max aesthetic.",
    "🗺️ Cyber-Jungle [赛博丛林]": "Overgrown ruins, synthetic plants, robotic animals, nature reclaiming tech."
}

# 4. 政治与派系 (Politics & Factions)
WORLD_POLITICS = {
    "👑 Theocracy / Cult [神权统治]": "Religious leaders, sacred laws, rituals, inquisition, fanatical aesthetics.",
    "👑 Corporatocracy [企业极权]": "Ruled by mega-corps, branding everywhere, private security, profit over life.",
    "👑 Feudal Kingdom [封建王国]": "Kings, knights, houses, banners, castles, rigid hierarchy.",
    "👑 Anarcho-Syndicalism [无政府主义]": "Tribes, gangs, decentralized, chaotic, punk aesthetic.",
    "👑 AI Singularity [AI 统辖]": "Cold logic, hive mind, perfectly ordered, sterile, surveillance."
}

# 5. 世界类型 (World Archetypes)
WORLD_TYPES = {
    "🌍 High Fantasy (Tolkien) [史诗奇幻]": "Elves, dwarves, magic, medieval politics, ancient ruins, maps.",
    "🌍 Hard Sci-Fi (The Expanse) [硬科幻]": "Physics-based, space colonization, zero-g, realistic tech, politics.",
    "🌍 Cyberpunk Dystopia [赛博反乌托邦]": "Mega-corps, high tech low life, neon, rain, hacking, implants.",
    "🌍 Post-Apocalyptic (Fallout) [废土末世]": "Scavenging, radiation, mutants, ruins of civilization, survival.",
    "🌍 Steampunk / Gaslamp [蒸汽/煤气灯]": "Victorian aesthetics, steam power, gears, brass, alchemy, occult.",
    "🌍 Eldritch Horror (Lovecraft) [克苏鲁/古神]": "Cosmic madness, tentacles, forbidden tomes, cults, foggy harbors.",
    "🌍 Solar Punk [太阳朋克]": "Eco-friendly, sustainable tech, green cities, bright future, art nouveau."
}

# 6. 设定元素 (World Elements)
WORLD_ELEMENTS = {
    "🗺️ Map & Geography [地图/地理]": "Top down map, coastlines, mountain ranges, biomes, borders.",
    "🏰 Factions & Culture [派系/文化]": "Clothing style, banners, architecture, social hierarchy, rituals.",
    "⚔️ Weaponry & Artifacts [武器/圣物]": "Legendary swords, energy blasters, ancient rings, magical tomes.",
    "🐉 Flora & Fauna [生物/植被]": "Bestiary, alien plants, monsters, mounts, ecosystems.",
    "🔮 Magic / Tech System [魔法/科技]": "Runes, spell effects, holograms, warp drives, UI design."
}

# ==============================================================================
# 🔌 PART 15: THE PROMPT ENGINEER DATA (模型适配核心库 - v61 极限专业版)
# ==============================================================================

# 针对不同模型的底层逻辑优化
TARGET_MODELS = {
    "🎨 FLUX.1 [T5 Encoder Logic]": {
        "desc": "Best at natural language & text rendering.",
        "strategy": "Use descriptive sentences. Mention text content explicitly (e.g. 'text saying \"HELLO\"'). Detail spatial relationships (left of, behind)."
    },
    "🎨 Midjourney v6 [摄影艺术流]": {
        "desc": "Focus on lighting, composition, and 'vibe'.",
        "strategy": "Use artistic keywords. Append parameters like '--ar 16:9 --v 6.0 --stylize 250'. Avoid 'hands' or structural details (it handles them well)."
    },
    "🎨 Pony Diffusion V6 (SDXL) [二次元标签流]": {
        "desc": "Danbooru tag based, requires score tags.",
        "strategy": "MUST start with 'score_9, score_8_up, score_7_up, source_anime'. Use Danbooru tags (e.g., '1girl, solo, looking_at_viewer')."
    },
    "🎨 Stable Diffusion 1.5 [传统标签流]": {
        "desc": "Keyword stuffing, quality boosters.",
        "strategy": "Comma-separated. Start with '(masterpiece), (best quality), 4k'. Heavy use of parentheses for weighting."
    },
    "🎨 DALL-E 3 [精准语义流]": {
        "desc": "Literal interpretation, censorship sensitive.",
        "strategy": "Write exactly what you want to see. Subject + Action + Context. Avoid artist names (copyright filter)."
    }
}

# ==============================================================================
# 📦 PART 16: PACKAGING DESIGN DATA (包装设计核心库 - v70 新增)
# ==============================================================================

# 1. 包装形态 (Container Types)
PACK_TYPES = {
    "📦 Box / Rigid Box [精装礼盒]": "Sharp edges, thick cardboard, magnetic closure, luxury unboxing experience.",
    "📦 Bottle (Glass/Dropper) [滴管/玻璃瓶]": "Serum bottle, essential oil, pharmaceutical vibe, translucent.",
    "📦 Tube (Squeeze) [软管]": "Toothpaste/cream style, plastic or aluminum, crimped end, matte finish.",
    "📦 Pouch / Doypack [自立袋]": "Flexible packaging, ziplock, foil lined, snack/coffee beans.",
    "📦 Can / Tin [马口铁罐]": "Beverage can, tea tin, metallic reflection, cylindrical.",
    "📦 Blister Pack [吸塑包装]": "Plastic shell backing, pharmaceutical or toy retail, transparency.",
    "📦 Shopping Bag [手提袋]": "Paper or fabric, twisted handles, retail shopping vibe.",
    "📦 Wrapper / Bar [卷膜/条装]": "Chocolate bar style, foil wrapper, crinkled texture."
}

# 2. 包装材质 (Materials)
PACK_MATERIALS = {
    "🛠️ Kraft Paper (Eco) [牛皮纸/环保]": "Brown, textured, fibrous, recycled look, organic, sustainable.",
    "🛠️ Frosted Glass [磨砂玻璃]": "Matte, semi-transparent, diffuse light, premium, heavy.",
    "🛠️ Brushed Aluminum [拉丝铝]": "Metallic grain, industrial, cold, tech/beverage feel.",
    "🛠️ Glossy Plastic [亮面塑料]": "High reflection, vibrant colors, mass market, FMCG.",
    "🛠️ Matte Cardstock [哑光卡纸]": "Soft touch, non-reflective, elegant, premium paper.",
    "🛠️ Textured Washi [和纸/特种纸]": "Rough fiber texture, Japanese style, artisanal, organic."
}

# 3. 印刷工艺 (Printing Finishes)
PACK_FINISHES = {
    "✨ Foil Stamping (Gold/Silver) [烫金/烫银]": "Metallic heat press, highly reflective contrast, luxury detail.",
    "✨ Embossing / Debossing [激凸/压凹]": "Raised or recessed surface, tactile texture, 3D effect on paper.",
    "✨ Spot UV [局部UV]": "Glossy coating on specific areas (logo) against matte background.",
    "✨ Letterpress [凸版印刷]": "Indented ink, vintage feel, tactile quality, heavy paper.",
    "✨ Holographic Foil [镭射烫]": "Rainbow spectrum reflection, cyberpunk/Y2K vibe.",
    "✨ Minimalist Screen Print [丝网印]": "Thick ink layer, vibrant solid colors, handcrafted feel."
}

# 4. 产品类别 (Product Category)
PACK_CATEGORIES = {
    "💄 Cosmetics / Skincare [美妆护肤]": "Clean, sterile, pastel or luxury colors, serif fonts.",
    "🍔 Food / Snacks [食品零食]": "Appetizing, warm colors, bold typography, ingredient illustration.",
    "☕ Coffee / Tea [咖啡/茶饮]": "Earth tones, artisanal aesthetic, cultural elements, texture focus.",
    "📱 Tech / Gadgets [数码科技]": "Black/White, sleek, grid layout, specs list, futuristic.",
    "🍷 Alcohol / Spirits [酒类]": "Heavy glass, intricate labels, foil stamping, heritage vibe.",
    "💊 Supplements / Pharma [保健/医药]": "Clinical, white space, sans-serif, Swiss grid, trust."
}

# 5. 展示视角 (Mockup View)
PACK_VIEWS = {
    "📷 Front Studio Shot [正面特写]": "Symmetrical, hero shot, perfect lighting, white background.",
    "📷 Isometric Group [等轴组合]": "Multiple items, arranged in grid or scattered, 3D perspective.",
    "📷 Floating / Gravity [悬浮展示]": "Product floating in air, dynamic shadows, surreal, magical.",
    "📷 In-Hand / Lifestyle [手持/生活]": "Held by a hand, blurred background, realistic context.",
    "📷 Wet / Condensation [带水珠]": "Cold drink look, fresh water droplets, mist, refreshing."
}

# ==============================================================================
# ⚔️ PART 17: THE WUXIA MASTER DATA (武侠宗师核心库 - v80 封神版)
# ==============================================================================

# 1. 武侠电影流派 (Cinematic Styles)
WUXIA_STYLES = {
    "🎥 Shaw Brothers Classic (Hardcore) [邵氏硬桥硬马]": "1970s Hong Kong style, clear movements, long takes, studio set, theatrical lighting, kung fu realism.",
    "🎥 Tsui Hark New Wave (Wire-fu) [徐克新派/威亚]": "Rapid editing, defying gravity, flying swords, exaggerated flowing robes, chaotic energy (e.g. Swordsman II).",
    "🎥 Zhang Yimou (Color Theory) [张艺谋/色彩美学]": "Monochromatic visual dominance, visual spectacle, symmetric composition, wuxia as dance (e.g. Hero, House of Flying Daggers).",
    "🎥 Wong Kar-wai (Mood) [王家卫/写意]": "Ashes of Time style. Motion blur, solitude, desert texture, impressionistic combat, focus on emotion over moves.",
    "🎥 King Hu (Zen) [胡金铨/禅意]": "Bamboo forests, Peking Opera percussion, interplay of stillness and motion, spiritual confrontation (e.g. A Touch of Zen).",
    "🎥 Stephen Chow (Gritty) [周星驰/功夫]": "Hyper-realistic slums mixed with anime-style physics, Buddha's Palm, exaggerated impact.",
    "🎥 Xianxia / Fantasy [仙侠/玄幻]": "High magic, flying on swords, glowing energy blasts, divine beasts, ethereal atmosphere (e.g. Jade Dynasty).",
    "🎥 Realistic Wushu [实战武术]": "Donnie Yen / Jet Li style. MMA influence, joint locking, speed, physical impact, grounded."
}

# 2. 江湖身份 (Character Archetypes)
WUXIA_ROLES = {
    "👤 Wandering Swordsman (Ronin) [浪子/游侠]": "Unkempt hair, holding a wine gourd, straw rain cape (Suo Yi), lonely, melancholic.",
    "👤 Sect Leader / Grandmaster [掌门/宗师]": "Long white beard, flowing Taoist robes, hands behind back, aura of invincibility.",
    "👤 Assassin / Ninja [刺客/死士]": "Black veiled hat (Wei Mao), masked face, tight night-ops gear, hidden weapons, shadows.",
    "👤 Eunuch / Court Official [东厂/锦衣卫]": "Embroidered uniform (Feiyu Fu), pale face, sinister smile, double swords, authoritative.",
    "👤 Shaolin Monk [少林武僧]": "Bald head, Buddhist beads, cassock (Kasaya), staff or bare hands, golden skin.",
    "👤 Beggar Sect [丐帮弟子]": "Ragged patchwork clothes, holding a green bamboo stick, rough texture, fierce eyes.",
    "👤 Sword Maiden [侠女]": "Elegant Hanfu, long ribbon hair accessories, sharp gaze, holding a Jian, duality of beauty and lethality."
}

# 3. 绝世武功与动作 (Martial Arts & Moves)
WUXIA_MOVES = {
    "👊 Qinggong / Lightness Skill [轻功/踏雪无痕]": "Defying gravity, stepping on bamboo leaves/water, weightless suspension, flowing fabrics.",
    "👊 Tai Chi / Internal Force [太极/内功]": "Slow motion, yin-yang circular hand movements, manipulating air/water/leaves, spiritual aura.",
    "👊 Drunken Fist [醉拳]": "Off-balance posture, leaning swaying, holding wine jar, deceptive unpredictability.",
    "👊 Wing Chun (Wooden Dummy) [咏春/木人桩]": "Close quarters, fast chain punches, centerline theory, rapid blocks.",
    "👊 Sword Qi / Energy Blast [剑气/剑意]": "Invisible shockwaves cutting through air/water, glowing aura around blade, destruction at a distance.",
    "👊 Dim Mak / Acupressure [点穴]": "Precision finger strike, frozen opponent, focused macro shot on contact point.",
    "👊 Palm Strike (Buddha) [如来神掌]": "Giant hand energy projection, crushing impact, dust clouds, epic scale.",
    "👊 Wire-Fu Combat [威亚打斗]": "Mid-air clash, crossing swords, rotating bodies, hyper-dynamic angles."
}

# 4. 神兵利器 (Legendary Weapons)
WUXIA_WEAPONS = {
    "⚔️ Straight Sword (Jian) [君子剑]": "Double-edged, elegant, tassel attached, symbol of nobility.",
    "⚔️ Broadsword (Dao) [大刀]": "Single-edged, heavy, curved, red scarf on handle, brutal chopping power.",
    "⚔️ Green Dragon Guandao [青龙偃月刀]": "Long polearm, heavy blade, intricate dragon engraving, general's weapon.",
    "⚔️ Flying Guillotine [血滴子]": "Clockwork mechanism, chained ranged weapon, deadly, steampunk-wuxia.",
    "⚔️ Embroidery Needles [绣花针]": "Invincible East style. Tiny, almost invisible threads, precision killing.",
    "⚔️ Twin Hooks / Daggers [护手钩/双刺]": "Exotic specialized weapons, catching blades, close combat.",
    "⚔️ Zither / Guqin (Sonic) [古琴音波]": "Weaponized music, sound waves cutting rocks, seated combat."
}

# 5. 服装与材质 (Costume & Material)
WUXIA_CLOTHING = {
    "👗 Ming Dynasty Flying Fish Robe [明代飞鱼服]": "Intricate embroidery, armored shoulders, official police aesthetic.",
    "👗 Coarse Linen / Patchwork [粗麻布衣]": "Realistic texture, worn edges, historical peasant look, wabi-sabi.",
    "👗 Flowing Silk Hanfu [飘逸丝绸]": "Translucent layers, long sleeves, water-like movement, celestial vibe.",
    "👗 Bamboo Hat & Rain Cape [斗笠蓑衣]": "Straw texture, rain-soaked, mysterious, hidden face.",
    "👗 Battle Armor (General) [山文甲/明光铠]": "Mountain pattern scales, gold/silver finish, heavy weight, battle-worn."
}

# 6. 场景意境 (Atmospheric Settings)
WUXIA_SCENES = {
    "🏔️ Bamboo Forest Battle [竹林决战]": "Crouching Tiger style. Green mist, falling leaves, vertical lines, swaying stalks.",
    "🏔️ Desert Inn [龙门客栈/大漠]": "Sandstorms, wooden structure, sunset, isolation, wine flags fluttering.",
    "🏔️ Rainy Night Alley [雨夜长街]": "Blue mood, reflections on wet stone, rain slicing through light, noir wuxia.",
    "🏔️ Snowy Mountain Peak [华山论剑]": "Pure white background, solitary pine tree, cold mist, high contrast.",
    "🏔️ Peach Blossom Island [桃花岛]": "Pink petals falling, romantic, soft focus, dreamlike.",
    "🏔️ Forbidden City Roofs [紫禁之巅]": "Yellow glazed tiles, moonlit night, high architecture, stealth."
}

# ==============================================================================
# 💼 PART 18: BRAND DIRECTOR DATA (品牌全案核心库 - v80 封神版)
# ==============================================================================

# 1. 品牌核心价值 (Core Values / Archetypes Extension)
BRAND_VALUES = {
    "💎 Luxury & Heritage [奢华/传承]": "Timeless, exclusive, serif typography, gold/black, minimalism, high status (e.g. Hermes).",
    "🚀 Innovation & Future [创新/未来]": "Tech-forward, neon, gradients, sans-serif, motion blur, disruption (e.g. OpenAI).",
    "🌿 Sustainability & Organic [环保/有机]": "Earth tones, textured paper, raw materials, botanical illustrations, kindness (e.g. Aesop).",
    "⚡ Energy & Rebellion [能量/叛逆]": "High contrast, bold distortion, acid graphics, street culture, loud (e.g. Red Bull).",
    "🤝 Trust & Corporate [信任/专业]": "Blue/Grey palette, grid systems, clean layout, stability, authority (e.g. McKinsey).",
    "🧸 Playful & Gen-Z [趣味/Z世代]": "Dopamine colors, 3D claymorphism, rounded shapes, stickers, irony (e.g. Duolingo).",
    "🧘 Wellness & Zen [身心/禅意]": "Soft pastels, negative space, airy layout, fluid gradients, balance (e.g. Lululemon)."
}

# 2. 设计系统与排版策略 (Design Systems)
BRAND_SYSTEMS = {
    "📐 Swiss International (Grid) [瑞士国际主义]": "Strict mathematical grids, Helvetica, asymmetry, objective photography, clean hierarchy.",
    "📐 Dynamic Identity (Fluid) [动态识别系统]": "A logo that changes shape/content, generative patterns, motion-first design.",
    "📐 Atomic Design (Modular) [原子化/模块化]": "Building blocks, repetitive geometric patterns, scalable UI components, systematic.",
    "📐 Maximalist Collage [极繁主义拼贴]": "Layers of texture, mixed media, typography overload, anti-design, chaotic energy.",
    "📐 Minimalist Essentialism [本质极简主义]": "Extreme reduction, monochrome, heavy whitespace, focus on material quality."
}

# 3. 交付物展示形式 (Deliverables / Mockups)
BRAND_DELIVERABLES = {
    "💼 Full VI Case Study [VI全案展示]": "Behance style layout. Overhead shot containing business cards, letterhead, phone mockup, and swatch.",
    "📱 Digital Product (UI/UX) [数字化产品]": "iPhone 15 mockup, floating screens, app interface, glassmorphism, dark mode.",
    "🛍️ Retail & Spatial [实体店/空间]": "Storefront signage, interior wall graphics, wayfinding, packaging on shelf, architectural visualization.",
    "👕 Merch & Apparel [周边/服饰]": "Hoodie mockup, tote bag, stickers, embroidery detail, streetwear look.",
    "🚗 Livery & Outdoor [车体/户外广告]": "Billboard in city, vinyl car wrap, bus stop poster, massive scale."
}

# 4. 辅助图形风格 (Supergraphics)
BRAND_GRAPHICS = {
    "🎨 Abstract Geometry [抽象几何]": "Bauhaus shapes, circles and squares, interacting forms.",
    "🎨 Organic Fluidity [有机流体]": "Liquid gradients, lava lamp shapes, smooth transitions.",
    "🎨 Data Visualization [数据可视化]": "Dot matrix, lines, nodes, code snippets, tech texture.",
    "🎨 Typography Pattern [文字纹理]": "Repeating brand name, kinetic type, warp text as background."
}

# ==============================================================================
# 🏛️ PART 19: INTERIOR & SPATIAL DESIGN DATA (室内与空间架构库 - v110 新增)
# ==============================================================================

# 1. 空间美学风格 (Spatial Styles)
INTERIOR_STYLES = {
    "🏛️ Japandi (Zen Modern) [侘寂/北欧禅宗]": "Minimalist, wabi-sabi elements, natural wood, muted earth tones, low furniture, zen atmosphere.",
    "🏛️ Mid-Century Modern[世纪中叶现代]": "Teak wood, organic curves, clean lines, vintage 50s-60s furniture, mustard yellow/olive accents.",
    "🏛️ Industrial Brutalism [工业粗野风]": "Exposed pipes, raw concrete walls, rusted steel, large warehouse windows, moody.",
    "🏛️ Cyber-Dystopian Loft [赛博末世公寓]": "Neon lights bleeding through blinds, high-tech monitors mixed with clutter, dark alleys, moody.",
    "🏛️ French Haussmann [法式奥斯曼]": "Intricate wall moldings, herringbone parquet floors, large marble fireplaces, high ceilings, Parisian elegance.",
    "🏛️ Biophilic Design[亲自然设计]": "Seamless indoor-outdoor transition, living walls, abundant foliage, natural sunlight, organic shapes."
}

# 2. 空间类型 (Space Types)
ROOM_TYPES = {
    "🛋️ Living Room / Lounge [客厅/休息室]": "Sofa, coffee table, rug, focus on comfort and social layout.",
    "🛏️ Bedroom / Sanctuary [卧室/私密空间]": "Bed, soft linens, intimate lighting, relaxing atmosphere.",
    "🛁 Spa Bathroom [浴室/水疗]": "Freestanding tub, stone tiles, water reflections, steam.",
    "🛍️ Luxury Retail Store [奢侈品买手店]": "Display pedestals, spot lighting, premium materials, sparse products.",
    "🖼️ Art Gallery / Museum [画廊/美术馆]": "White walls, track lighting, spacious, focus on exhibits.",
    "☕ Artisan Cafe [精品咖啡馆]": "Espresso machine, cozy seating, warm lighting, ambient chatter vibe."
}

# 3. 建筑材质 (Surface Materials)
SURFACE_MATERIALS = {
    "🧱 Micro-cement & Travertine [微水泥/洞石]": "Seamless matte texture, porous stone, warm grey/beige, tactile.",
    "🧱 Terrazzo & Plaster [水磨石/灰泥]": "Speckled patterns, artisan plaster walls, Mediterranean vibe.",
    "🧱 Dark Walnut & Brass [黑胡桃木/黄铜]": "Rich dark wood grain, brushed golden metal, mid-century luxury.",
    "🧱 Glass Block & Steel[玻璃砖/不锈钢]": "Translucent distortion, reflective, cold, modern, 80s revival.",
    "🧱 Bouclé & Velvet (Soft) [圈绒/天鹅绒]": "Textured curly fabric, plush, luxurious, soft light absorption."
}

# 4. 建筑光度学 (Architectural Lighting)
ARCH_LIGHTING = {
    "💡 Golden Hour / Sunbeams [自然光/丁达尔]": "Long dramatic shadows, warm volumetric rays coming through windows.",
    "💡 Cove Lighting & LEDs [暗槽光/洗墙灯]": "Indirect lighting, glowing edges, modern, soft diffusion.",
    "💡 IES Spotlights / Track[IES射灯/轨道灯]": "Focused beams, wall grazing, dramatic highlight on objects, museum style.",
    "💡 Moody / Overcast[阴天/散射光]": "Soft, shadowless, melancholic, natural softbox effect.",
    "💡 Cinematic Neon / Rim [霓虹/轮廓光]": "High contrast color gels, cyberpunk vibe, glowing silhouettes."
}


# ==============================================================================
# 👗 PART 20: FASHION & TEXTILE ENGINEERING (高定服装与布料库 - v110 新增)
# ==============================================================================

# 1. 服装美学与年代 (Fashion Aesthetics)
FASHION_STYLES = {
    "👗 Haute Couture (Avant-Garde) [前卫高定]": "Sculptural forms, impossible silhouettes, runway drama, Iris van Herpen style.",
    "👗 Dark Avant-Garde / Gothic [暗黑先锋]": "Rick Owens/Yohji Yamamoto style. Draped black fabrics, asymmetric, apocalyptic.",
    "👗 Y2K / Cyber-Fairy [千禧/赛博废土]": "Metallic crop tops, low-rise pants, strappy details, holographic, 2000s nostalgia.",
    "👗 Techwear / Urban Ninja[机能/都市忍者]": "Acronym style. Tactical vests, cargo pockets, waterproof zippers, functional.",
    "👗 Renaissance Revival [复古文艺复兴]": "Corsets, puffed sleeves, intricate lace, romanticism, historical fusion.",
    "👗 Minimalist Luxury [极简奢华]": "The Row style. Clean lines, perfect tailoring, neutral palette, stealth wealth."
}

# 2. 布料物理与纹理 (Fabric Physics & Textures)
FABRIC_PROPERTIES = {
    "🧵 Iridescent Silk / Satin[流光丝绸]": "High sheen, fluid draping, liquid-like reflections, catches light dynamically.",
    "🧵 Heavy Canvas / Denim [重磅帆布/丹宁]": "Stiff, structured, rigid folds, raw texture, workwear aesthetic.",
    "🧵 Translucent PVC / Latex [透明PVC/乳胶]": "Glossy, reflective, transparent, futuristic, skin-tight, cyberpunk.",
    "🧵 Distressed Leather [做旧做破皮革]": "Scratches, matte finish, heavy, rebel aesthetic, vintage.",
    "🧵 Intricate Lace / Tulle [繁复蕾丝/薄纱]": "Semi-transparent, delicate floral patterns, layered, romantic, ethereal.",
    "🧵 Holographic Mylar[全息反光膜]": "Rainbow reflections, stiff, crinkled, sci-fi."
}

# 3. 剪裁与版型 (Garment Construction)
GARMENT_CUTS = {
    "✂️ Asymmetrical Draping [不对称垂坠]": "Fabric cascading unevenly, dynamic lines, ancient Greek inspiration.",
    "✂️ Tailored Slim Fit [极致修身剪裁]": "Sharp shoulders, cinched waist, perfect fit, authoritative.",
    "✂️ Oversized Boxy [Oversize/廓形]": "Dropped shoulders, exaggerated volume, streetwear silhouette.",
    "✂️ Deconstructed [解构拼接]": "Exposed seams, inside-out look, multiple garments sewn together, punk."
}

# 4. 秀场与展示呈现 (Presentation Context)
FASHION_PRESENTATION = {
    "📸 High-Fashion Runway [高定大秀]": "Walking model, dynamic motion, dramatic spotlights, blurred audience background.",
    "📸 Studio Lookbook[影棚Lookbook]": "Static pose, clean infinity cove background, perfect rim lighting, focus on details.",
    "📸 Street Snaps [街拍/日常]": "Candid, urban background, natural daylight, movement, trendy.",
    "📸 Editorial Fantasy [杂志概念大片]": "Surreal background, levitating fabrics, wind machine effect, highly stylized."
}

# ==============================================================================
# ✂️ PART 21: HAUTE COIFFURE & BEAUTY DATA (顶奢发型与造型库 - v120 新增)
# ==============================================================================

# 1. 基础剪裁与轮廓 (Haircut Styles)
HAIR_STYLES = {
    "✂️ Classic Bob / Lob [经典波波头/长波波]": "Blunt cut, chin or shoulder length, precise geometry, Vidal Sassoon style, sharp and chic.",
    "✂️ Textured Wolf Cut / Shag[纹理狼尾/碎发]": "Heavy layers, messy fringe, rock n' roll vibe, mullet elements, rebellious and wild.",
    "✂️ Elegant Updo / Chignon [优雅盘发/发髻]": "Pinned up, intricate twists, loose tendrils framing the face, bridal or red carpet ready.",
    "✂️ Buzz Cut / Fade[极简寸头/渐变推白]": "Extremely short, shaved sides, strong facial structure focus, modern high-fashion.",
    "✂️ Flowing Rapunzel Length [超长瀑布发]": "Waist-length or longer, continuous flow, mythological or fantasy aesthetic.",
    "✂️ Avant-Garde Sculptural [前卫雕塑发型]": "Gravity-defying, stiffened with product, geometric or animalistic shapes, runway showstopper.",
    "✂️ Pixie Cut [精灵短发]": "Short back and sides, slightly longer on top, gamine, delicate yet edgy."
}

# 2. 质感与物理形态 (Hair Textures & Physics)
HAIR_TEXTURES = {
    "🧬 Glass Hair / Sleek Straight [镜面直发/极致顺滑]": "Zero frizz, intense reflective shine, flat ironed, liquid-like surface, anisotropic highlights.",
    "🧬 Beach Waves / Tousled [微醺海浪卷/慵懒]": "Loose, S-shaped waves, salt spray texture, effortless, lived-in look.",
    "🧬 Coily / 4C Afro [极度卷曲/非裔爆炸头]": "Tight Z-pattern coils, immense volume, natural crown, rich dense texture, defiant gravity.",
    "🧬 Wet Look / Gel [湿发造型/高级凝胶感]": "Drenched appearance, combed back, distinct separated strands clinging to skin, sultry.",
    "🧬 Voluminous Blowout [蓬松吹风/复古大卷]": "90s supermodel volume, bouncy, rounded ends, airy roots, glamorous.",
    "🧬 Frizzy / Static[毛躁/静电炸毛]": "Deliberate flyaways, unkempt, ethereal backlit halo effect, emotional or raw."
}

# 3. 染发工艺与色彩 (Color & Dye Techniques)
HAIR_COLORS = {
    "🎨 Seamless Balayage [无痕画染/渐层扫染]": "Hand-painted highlights, soft transition from dark roots to light ends, sun-kissed dimension.",
    "🎨 Platinum Ice Blonde [极地冰金/漂白]": "Stark white/silver blonde, totally lifted pigment, icy, ethereal, high maintenance.",
    "🎨 Cyber-Neon Split Dye [赛博霓虹/阴阳染]": "Two starkly contrasting colors (e.g., black and neon green) split down the middle, e-girl/cyberpunk.",
    "🎨 Deep Brunette & Highlights [深邃棕与高光]": "Rich espresso base with caramel or honey ribbons, depth and warmth, classic.",
    "🎨 Pastel Holographic[柔和全息/马卡龙色]": "Iridescent blend of lavender, mint, and peach, translucent unicorn aesthetic.",
    "🎨 Vivid Copper / Ginger [炽热红铜/橘发]": "Bright fiery orange-red, freckles complement, Celtic or pre-Raphaelite vibe."
}

# 4. 展示与拍摄视角 (Presentation & Photography)
HAIR_PRESENTATION = {
    "📸 Editorial Beauty Portrait [美妆大片特写]": "Ring light/beauty dish, pristine skin pores, absolute focus on hair framing the face.",
    "📸 Salon Turnaround (Back/Side) [沙龙多角度展示]": "Showing the cut from the back or profile, neck and shoulders visible, technical display.",
    "📸 Macro Strand Detail [发丝微距特写]": "Extreme close-up of hair strands, showing color transition and cuticle health, shallow depth of field.",
    "📸 Dynamic Wind Blown [风吹动态捕捉]": "Hair floating mid-air, frozen action, dramatic movement, high shutter speed.",
    "📸 Cinematic Silhouette [电影级逆光轮廓]": "Backlit by strong light, creating a glowing 'halo' effect around the hair edges, moody."
}

# ==============================================================================
# 🎁 PART 22: CULTURAL & CREATIVE DESIGN DATA (文创与潮玩设计库 - v130 新增)
# ==============================================================================

# 1. 文创产品形态 (Product Formats)
CULTURAL_PRODUCTS = {
    "🎁 Art Toy / Blind Box [潮玩盲盒公仔]": "Chibi style, cute proportions, standing on a circular base, collectible toy figure.",
    "🎁 Enamel Pin / Badge[烤漆珐琅金属徽章]": "Flat graphic design, thick metallic outlines, pinned on a card backing, highly collectible.",
    "🎁 Traditional Folding Fan [折扇/团扇]": "Bamboo or wood ribs, stretched silk or rice paper, elegant composition, flat lay.",
    "🎁 Porcelain / Ceramic Tea Set [精美陶瓷茶具]": "Teapot and cups, elegant curves, smooth glaze, cultural lifestyle product.",
    "🎁 Intricate Paper Diorama[立体多层纸雕]": "Layered cut paper, 3D depth, warm backlighting shining through layers, fairytale vibe.",
    "🎁 Embroidered Silk Pouch [刺绣香囊/丝带]": "Fabric texture, intricate stitching threads, traditional textile souvenir.",
    "🎁 Museum Canvas Tote Bag [美术馆帆布袋]": "Canvas fabric texture, flat printed graphic, minimalist museum souvenir style.",
    "🎁 Acrylic Standee [二次元亚克力立牌]": "Clear transparent acrylic border, 2D character printed on thick plastic, desk decoration."
}

# 2. 文化主题与IP (Cultural Themes & IP)
CULTURAL_THEMES = {
    "⛩️ Imperial Palace (Forbidden City) [故宫/宫廷美学]": "Red walls, golden glazed tiles, auspicious clouds, dragons, royal elegance, traditional Chinese.",
    "🏜️ Dunhuang Mythology [敦煌飞天/神话]": "Flying apsaras, nine-colored deer, weathered mineral pigments (green/ochre), Buddhist murals.",
    "🎍 Zen Landscape (Shanshui) [写意山水/禅意]": "Mountains and rivers, minimalist, negative space, pine trees, cranes, poetic and serene.",
    "🏮 Modern Guochao (Cyber-Folk) [赛博国潮]": "Traditional lions/dragons mixed with neon lights, mecha elements, vibrant clash of old and new.",
    "🏛️ Western Classical Museum [西方古典博物]": "Marble busts, renaissance motifs, oil painting textures, vintage botanical illustrations.",
    "🎭 Intangible Heritage [非遗民俗]": "Paper cutting, shadow puppetry, Peking opera masks, vibrant folk art colors."
}

# 3. 材质与制造工艺 (Material & Craftsmanship)
CULTURAL_CRAFTS = {
    "🛠️ Glossy PVC / Vinyl [高光PVC/搪胶材质]": "Smooth plastic, highly reflective, subsurface scattering, premium designer toy feel.",
    "🛠️ Cloisonné / Soft Enamel[景泰蓝/软珐琅]": "Raised gold/silver metal lines, filled with vibrant glossy paint, tactile surface.",
    "🛠️ Matte Celadon / White Jade [哑光青瓷/白玉]": "Subtle semi-translucent glaze, smooth to the touch, celadon green or pure jade white.",
    "🛠️ Laser Engraved Wood[激光雕刻原木]": "Burnt wood edges, natural grain, precise geometric etching, organic feel.",
    "🛠️ Gold Foil Stamping [烫金/洒金工艺]": "Metallic gold leaf applied to surfaces, highly reflective against matte backgrounds.",
    "🛠️ Flocked / Velvet Texture [植绒/天鹅绒质感]": "Fuzzy, soft light absorption, premium tactile toy or box interior."
}

# 4. 展示视角与布光 (Merch Presentation)
MERCH_PRESENTATION = {
    "📸 Studio Product Shot[影棚白底/纯色底特写]": "Clean solid pastel background, softbox lighting, sharp focus, commercial e-commerce look.",
    "📸 Lifestyle Context [生活化场景陈列]": "Placed on a wooden desk with tea/coffee props, soft sunlight, warm and inviting.",
    "📸 Mystery Box Packaging[盲盒带包装展示]": "Toy standing next to its beautifully designed cardboard blind box, retail ready.",
    "📸 Macro Craft Detail [微距工艺特写]": "Extreme close-up focusing on the texture of the enamel, print, or material."
}

# ==============================================================================
# 🧬 PART 23: MEDICAL & ANATOMY VISUALIZATION (医学科研与人体结构库 - v140 新增)
# ==============================================================================

# 1. 解剖系统与生理焦点 (Anatomical Systems)
MED_SYSTEMS = {
    "🧠 Central Nervous System [中枢神经系统]": "Brain, spinal cord, glowing synapses, neural networks, electrical impulses, dendrites.",
    "🫀 Cardiovascular System [心血管系统]": "Heart, beating, pumping blood, glowing red/blue veins, arteries, red blood cells.",
    "🦴 Skeletal & Orthopedic [骨骼与骨科]": "Skulls, ribcages, joints, bone marrow, porous calcium texture, spine, structural integrity.",
    "💪 Muscular System [肌肉系统]": "Striated muscle fibers, tendons, anatomical ecorché, red and white muscle groups, tension.",
    "🫁 Respiratory & Digestive [呼吸与消化]": "Lungs, alveoli, stomach, intestines, soft wet tissue, organ cross-sections.",
    "🧬 Cellular & Molecular [细胞与分子]": "DNA double helix, RNA, proteins, mitochondria, virus membranes, lipid bilayer.",
    "👁️ Sensory Organs [感觉器官]": "Detailed eye structure, retina, iris macro, auditory canal, optic nerve."
}

# 2. 医学成像与可视化技术 (Medical Imaging Modalities)
MED_IMAGING = {
    "🔬 3D Bio-Render (CGI) [3D生物渲染]": "Cinematic medical illustration, subsurface scattering (SSS), wet tissue material, highly detailed CG.",
    "🔬 MRI / fMRI Scan [核磁共振/功能性核磁]": "Magnetic resonance, false-color brain activity, slice views, neon heatmaps on black background.",
    "🔬 X-Ray Radiography [X光造影]": "Monochrome, inverted luminosity, translucent tissue, high-contrast bone structure, clinical blue tint.",
    "🔬 SEM (Electron Micro) [扫描电子显微镜]": "Nanoscale, extreme depth of field, grey or false-color (gold/purple), particulate textures.",
    "🔬 Fluorescence Microscopy [荧光显微摄影]": "Glowing neon cells, GFP (Green Fluorescent Protein), DAPI blue nuclei, pitch black void.",
    "🔬 Ultrasound / Sonogram [超声波成像]": "Grainy, cone-shaped field, sound wave reflection, organic acoustic texture, fetal view.",
    "🔬 Holographic Medical UI [全息医疗影像]": "Floating blue/cyan wireframes, glowing tech interface, futuristic diagnostic display, sci-fi."
}

# 3. 医学插画与艺术风格 (Illustration Styles)
MED_STYLES = {
    "🎨 Classic Textbook (Netter)[经典教科书插画]": "Frank Netter style, watercolor/gouache feel, clear educational labels, bright distinct colors, sterile.",
    "🎨 Da Vinci Sketch [达芬奇解剖手稿]": "Sepia parchment, ink and pen hatching, Renaissance anatomical study, mirrored handwriting.",
    "🎨 Dark Fantasy / Body Horror [暗黑生化/肉体恐怖]": "Giger-esque, biomechanical mutation, corrupted tissue, visceral, terrifying mutations.",
    "🎨 Cybernetic Augmentation[赛博义体改造]": "Flesh meeting metal, robotic prosthetics, carbon fiber bones, LED implants, surgical precision.",
    "🎨 Minimalist Vector [极简矢量信息图]": "Flat design, infographic style, solid pastel colors, UI/UX medical app aesthetic."
}

# 4. 观测尺度 (Scale Focus)
MED_SCALES = {
    "🔍 Macroscopic (Full Body/Organ) [宏观/全身体视角]": "Focus on anatomical relationship, organ placement, full silhouette.",
    "🔍 Microscopic (Tissue/Cell) [微观/细胞组织]": "Cell walls, blood flow, pathogens, microscopic landscape.",
    "🔍 Nanoscale (Molecular) [纳米/分子级]": "Atoms, chemical bonds, protein folding, infinite void background."
}

# ==============================================================================
# 🛠️ PART 24: INDUSTRIAL DESIGN & CMF DATA (工业设计与CMF核心库 - v150 新增)
# ==============================================================================

# 1. 产品类别 (Product Categories)
ID_CATEGORIES = {
    "📻 Consumer Electronics [消费电子]": "Smartphones, speakers, cameras, laptops. Focus on sleekness, interfaces, and tech integration.",
    "🪑 Furniture & Homeware [家具家居]": "Chairs, lamps, tables. Focus on ergonomics, scale, comfort, and interior harmony.",
    "🚗 Transportation / Vehicles [交通载具]": "Cars, ebikes, drones, scooters. Focus on aerodynamics, chassis, mobility, and stance.",
    "⚙️ Tools & Equipment [工具与装备]": "Power tools, medical devices, kitchen appliances. Focus on utility, grip, safety, and ruggedness.",
    "⌚ Wearables & Accessories[穿戴设备]": "Smartwatches, VR headsets, headphones. Focus on skin-contact materials, micro-details, and fashion.",
    "🤖 Robotics / Mecha [机器人/机甲]": "Bipedal robots, robotic arms, smart home bots. Focus on joints, sensors, friendly or aggressive forms."
}

# 2. 顶级设计语言 (Design Languages & Philosophies)
ID_DESIGN_LANGUAGES = {
    "📏 Dieter Rams / Braun Style [博朗极简/迪特·拉姆斯]": "'Less but better'. Functional, unobtrusive, geometric perfection, subtle color accents (orange/green buttons), timeless.",
    "🍏 Apple / Jony Ive Style [苹果现代主义]": "Seamless unibody, chamfered edges, strict corner radii, obsessive minimalism, premium feel.",
    "🎛️ Teenage Engineering [TE潮酷极客风]": "Playful, bright accent colors on grey/white, grid-based buttons, synths, retro-tech, utilitarian but fun.",
    "🛸 Retro-Futurism / Y2K [复古未来/千禧风]": "Translucent plastics, blobby curves, iMac G3 aesthetic, optimistic, colorful tech.",
    "🦇 Bionic / Organic Form[仿生/有机流线]": "Luigi Colani or Zaha Hadid style. Bio-morphism, sweeping curves, aerodynamic, lacking straight lines.",
    "🪖 Tactical / Rugged [战术/三防机能]": "Military-grade, exposed screws, shock-absorbing bumpers, matte finishes, G-Shock aesthetic.",
    "📻 Streamline Moderne [流线型时代]": "1930s industrial age, teardrop shapes, parallel horizontal lines, chrome and bakelite."
}

# 3. CMF 材质与表面处理 (Colors, Materials, Finishes)
ID_MATERIALS_CMF = {
    "🛠️ Matte Polycarbonate & Silicone[哑光PC与硅胶]": "Soft touch, zero reflection, friendly, durable, pastel or neutral colors.",
    "🛠️ Anodized Aluminum & Glass [阳极氧化铝与玻璃]": "Cold, premium, brushed texture, high tolerance fit, specular highlights.",
    "🛠️ Translucent Resin / Frosted [半透明树脂/磨砂]": "Light bleeding through, exposing internal components, frosted ice texture.",
    "🛠️ Carbon Fiber & Titanium [碳纤维与钛金属]": "Woven composite texture, dark metallic sheen, high-performance, lightweight aerospace vibe.",
    "🛠️ Natural Wood & Fabric (Nordic) [原木与织物]": "Ash/Oak grain, Kvadrat wool fabric, warm, sustainable, Bang & Olufsen style.",
    "🛠️ Injection Molded Plastic (Glossy) [高光注塑]": "Mass-produced, shiny, vibrant solid colors, distinct parting lines."
}

# 4. 工业渲染展示方式 (Presentation & Render Styles)
ID_PRESENTATION = {
    "📸 Hero Studio Shot[影棚白底特写]": "Perfect softbox lighting, solid white/grey background, subtle floor reflection, commercial catalog look.",
    "💥 Exploded View [零件拆解图]": "Components separated on a single axis, hovering in mid-air, showcasing internal engineering.",
    "📐 CAD Wireframe / Blueprint [CAD线框/蓝图]": "Technical drawing, isometric projection, blue/white lines, measurement annotations, engineering focus.",
    "🔍 Macro CMF Detail[微距材质特写]": "Extreme close-up on a dial, button, or material transition, shallow depth of field, focus on texture.",
    "🛋️ Lifestyle Context [生活化场景]": "Product placed in its natural environment (e.g. kitchen, desk), warm lighting, blurred background."
}