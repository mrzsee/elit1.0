import json
import os
from pathlib import Path

# Paths
BASE_DIR = Path(r"c:\Users\Zsolt\Desktop\HTMLAI\RestasRenata")
CONTENT_MAP_PATH = BASE_DIR / "content_map.json"

SAMPLE_PROPERTIES = [
    {
        "city": "Szeged", "type": "Ház", "price": 89000000, "area": 120, 
        "title": "Szeged – Belváros, elegáns családi ház", 
        "image": "assets/images/hero_slideshow_1.png",
        "desc": "Kiváló állapotú, polgári jellegű családi ház Szeged szívében. Tágas terek, eredeti fa nyílászárók és modern gépészet találkozása.",
        "details": ["4 szoba", "Gáz-cirkó fűtés", "Garázs", "Kertkapcsolat"]
    },
    {
        "city": "Szeged", "type": "Lakás", "price": 45000000, "area": 65, 
        "title": "Modern tágas lakás eladó", 
        "image": "assets/images/hero_slideshow_2.png",
        "desc": "Frissen felújított, harmadik emeleti lakás liftes házban. Fiatalos design, beépített konyha és klíma.",
        "details": ["2 szoba", "Amerikai konyha", "Klíma", "Alacsony rezsi"]
    },
    {
        "city": "Ásotthalom", "type": "Ház", "price": 32000000, "area": 90, 
        "title": "Nyugodt környezetű tanya jellegű ház", 
        "image": "assets/images/hero_slideshow_3.png",
        "desc": "Természetközeli környezetben fekvő, folyamatosan karbantartott ingatlan. Ideális hétvégi háznak vagy gazdálkodásra.",
        "details": ["3 szoba", "Víz, villany van", "Melléképületek", "Nagy telek"]
    },
    {
        "city": "Szeged", "type": "Ház", "price": 125000000, "area": 200, 
        "title": "Luxus villa panorámával", 
        "image": "assets/images/hero_slideshow_4.jpg",
        "desc": "Minden igényt kielégítő luxusvilla csendes utcában. Szauna, medence és fűtött garázs.",
        "details": ["5 szoba", "Hőszivattyús fűtés", "Medence", "Okosotthon"]
    },
    {
        "city": "Szeged", "type": "Lakás", "price": 58000000, "area": 75, 
        "title": "Belvárosi felújított ékszerdoboz", 
        "image": "assets/images/hero_slideshow_5.jpg",
        "desc": "Elegáns stílusban felújított nagypolgári lakás. Nagy belmagasság, stukkók és prémium burkolatok.",
        "details": ["3 szoba", "Padlófűtés", "Galériázható", "Belvárosi elhelyezkedés"]
    },
    {
        "city": "Budapest", "type": "Lakás", "price": 95000000, "area": 85, 
        "title": "Duna-parti penthouse lakás", 
        "image": "assets/images/hero_slideshow_2.png",
        "desc": "Pazar kilátás a Dunára, hatalmas terasz és modern belsőépítészet. 24 órás portaszolgálat.",
        "details": ["3 szoba", "Terasz (30 m²)", "Teremgarázs", "Portaszolgálat"]
    }
]

MASTER_TEMPLATE = """<!DOCTYPE html>
<html lang="hu" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <meta name="description" content="{{ description }}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        background: '#0F1113',   /* Architectural Onyx */
                        surface: '#1A1D20',      /* Dark Slate/Zinc */
                        primary: '#94A3B8',      /* Steel Blue / Cool Gray */
                        'primary-dark': '#64748B', 
                        text: '#F8FAFC',         /* Ghost White */
                        'text-muted': '#94A3B8', 
                        divider: '#2D3339',      /* Deep Slate Divider */
                    },
                    fontFamily: {
                        sans: ['Montserrat', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                    },
                    borderRadius: {
                        'DEFAULT': '0', // Sharp architectural edges
                    },
                    animation: {
                        'float': 'float 6s ease-in-out infinite',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-10px)' },
                        }
                    }
                }
            }
        }
    </script>
    
    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <style>
        [x-cloak] { display: none !important; }
        .glass-nav {
            background-image: url('{{ asset_prefix }}assets/images/architectural_menu_bg.png');
            background-size: cover;
            background-position: center;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
            position: relative;
        }
        .glass-nav::before {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(15, 17, 19, 0.85); /* Overlay to keep text readable */
            z-index: -1;
        }
        .reveal {
            opacity: 0;
            transform: translateY(20px);
            transition: all 1s ease-out;
        }
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
        
        .luxury-texture {
            background-image: url('{{ asset_prefix }}assets/images/bg_texture.png');
            background-repeat: repeat;
            background-size: 600px;
            opacity: 0.03;
            pointer-events: none;
            mix-blend-mode: overlay;
        }

        .logo-card-transition {
            transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .scroll-nav-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(148, 163, 184, 0.3);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .scroll-nav-dot.active {
            background: #94A3B8;
            transform: scale(1.5);
            box-shadow: 0 0 15px rgba(148, 163, 184, 0.4);
        }
        .scroll-indicator-container {
            position: fixed;
            right: 40px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 100;
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding: 20px 10px;
            background: rgba(15, 17, 19, 0.4);
            backdrop-filter: blur(8px);
            border-radius: 100px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            opacity: 0;
            visibility: hidden;
            transition: all 0.6s ease;
        }
        .scroll-indicator-container.visible {
            opacity: 1;
            visibility: visible;
        }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #0F1113; }
        ::-webkit-scrollbar-thumb { background: #2D3339; }
        ::-webkit-scrollbar-thumb:hover { background: #94A3B8; }
    </style>
</head>
<body class="bg-background text-text font-sans antialiased selection:bg-primary/30 selection:text-white relative"
      x-data="{ scrollY: 0 }" 
      @scroll.window="scrollY = window.scrollY">
    
    <!-- Global Texture Overlay -->
    <div class="fixed inset-0 z-0 luxury-texture"></div>

    <!-- Scroll Indicator Dots -->
    <div id="scroll-indicator" class="scroll-indicator-container hidden md:flex">
        <!-- Dots will be injected by JS -->
    </div>

    <!-- Sticky Header -->
    <header class="fixed w-full top-0 z-50 transition-all duration-300 glass-nav h-24 flex items-center"
            x-data="{ mobileMenuOpen: false }">
        <div class="max-w-7xl mx-auto px-8 w-full flex items-center justify-between relative">
            
            <!-- Dynamic Logo Card Container -->
            <div class="relative z-50">
                <div :class="scrollY > 50 ? 'w-16 h-12' : 'w-48 h-1'"></div>
                <a href="{{ asset_prefix }}index.html" 
                   class="absolute left-0 logo-card-transition flex items-center justify-center bg-white shadow-2xl overflow-hidden"
                   :class="scrollY > 50 
                        ? 'top-1/2 -translate-y-1/2 w-16 h-16 rounded-sm' 
                        : 'top-2 translate-y-2 w-48 h-40 rounded-sm animate-float'">
                    <img src="{{ asset_prefix }}assets/images/logo3.png" 
                         alt="Restás Renáta Logo" 
                         class="w-full h-full object-contain transition-all duration-500"
                         :class="scrollY > 50 ? 'scale-90 p-2' : 'scale-110 p-6'">
                </a>
            </div>

            <!-- Desktop Nav -->
            <nav class="hidden md:flex items-center space-x-10 pl-20">
                <a href="{{ asset_prefix }}index.html" class="text-text hover:text-primary font-medium uppercase tracking-[0.2em] text-xs transition-all nav-link relative group">
                    Kezdőlap
                    <span class="absolute -bottom-2 left-0 w-0 h-px bg-primary transition-all group-hover:w-full"></span>
                </a>
                <a href="{{ asset_prefix }}ingatlanok/index.html" class="text-text hover:text-primary font-medium uppercase tracking-[0.2em] text-xs transition-all nav-link relative group">
                    Ingatlanok
                    <span class="absolute -bottom-2 left-0 w-0 h-px bg-primary transition-all group-hover:w-full"></span>
                </a>
                <a href="{{ asset_prefix }}rolunk/index.html" class="text-text hover:text-primary font-medium uppercase tracking-[0.2em] text-xs transition-all nav-link relative group">
                    Rólam
                    <span class="absolute -bottom-2 left-0 w-0 h-px bg-primary transition-all group-hover:w-full"></span>
                </a>
                <a href="{{ asset_prefix }}kapcsolat/index.html" class="text-text hover:text-primary font-medium uppercase tracking-[0.2em] text-xs transition-all nav-link relative group">
                    Kapcsolat
                    <span class="absolute -bottom-2 left-0 w-0 h-px bg-primary transition-all group-hover:w-full"></span>
                </a>
                
                <div class="flex items-center gap-6 ml-6 pl-6 border-l border-divider/50">
                    <a href="https://www.facebook.com/restasrenata" target="_blank" class="text-text/60 hover:text-primary transition-colors">
                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg>
                    </a>
                    <a href="https://www.tiktok.com/@restasrenataingatlanok" target="_blank" class="text-text/60 hover:text-primary transition-colors">
                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-1.01V19a8.13 8.13 0 0 1-8.13 8.13c-4.49 0-8.12-3.63-8.12-8.13 0-4.41 3.51-8.01 7.89-8.12l.02 4.01c-2.22.12-4.01 1.95-3.9 4.17.11 2.21 2.02 3.94 4.23 3.82 2.2-.12 3.94-2.01 3.82-4.21V0l.27.02z"/></svg>
                    </a>
                </div>
            </nav>

            <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden p-2 text-text focus:outline-none relative z-50">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" x-show="!mobileMenuOpen" d="M4 6h16M4 12h16M4 18h16"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" x-show="mobileMenuOpen" x-cloak d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
        </div>

        <div x-show="mobileMenuOpen" x-transition.opacity
             class="md:hidden absolute top-0 left-0 w-full h-screen bg-background shadow-xl pt-32" x-cloak>
            <div class="flex flex-col p-8 space-y-8 text-center uppercase tracking-widest text-xs">
                <a href="{{ asset_prefix }}index.html" class="py-4 border-b border-divider/30">Kezdőlap</a>
                <a href="{{ asset_prefix }}ingatlanok/index.html" class="py-4 border-b border-divider/30">Ingatlanok</a>
                <a href="{{ asset_prefix }}rolunk/index.html" class="py-4 border-b border-divider/30">Rólam</a>
                <a href="{{ asset_prefix }}kapcsolat/index.html" class="py-4">Kapcsolat</a>
            </div>
        </div>
    </header>

    <main class="relative z-10 pt-24 min-h-screen">
        {{ content_body }}
    </main>

    <footer class="relative z-10 bg-surface text-text py-20 mt-24 border-t border-divider">
        <div class="max-w-7xl mx-auto px-8 grid md:grid-cols-3 gap-16 relative">
            <div class="space-y-6">
                <img src="{{ asset_prefix }}assets/images/logo3.png" alt="Logo" class="h-16 grayscale opacity-80 mb-4">
                <h3 class="text-2xl font-serif text-text tracking-widest uppercase">Restás<span class="font-light italic">Renáta</span></h3>
                <p class="text-text/50 leading-loose font-light text-sm">
                    Építészeti szemléletű ingatlanközvetítés. Professzionális megoldások az ingatlanpiacon.
                </p>
            </div>
            <div>
                <h4 class="text-xs uppercase tracking-[0.3em] mb-8 text-primary font-bold">Navigáció</h4>
                <ul class="space-y-4 text-xs tracking-widest">
                    <li><a href="{{ asset_prefix }}rolunk/index.html" class="text-text/60 hover:text-white transition-all">Rólam</a></li>
                    <li><a href="{{ asset_prefix }}ingatlanok/index.html" class="text-text/60 hover:text-white transition-all">Ingatlanok</a></li>
                    <li><a href="{{ asset_prefix }}kapcsolat/index.html" class="text-text/60 hover:text-white transition-all">Kapcsolat</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-xs uppercase tracking-[0.3em] mb-8 text-primary font-bold">Kapcsolat</h4>
                <div class="space-y-4 text-text/60 text-sm font-light">
                    <p>✉ hello@restasrenata.hu</p>
                    <p>📞 +36 70 384 5025</p>
                    <p>📍 Szeged és környéke</p>
                </div>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-8 mt-16 pt-8 border-t border-divider text-center text-text/30 text-[10px] tracking-[0.4em] uppercase">
            <p>&copy; 2025 Restás Renáta. Architectural Real Estate.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const reveals = document.querySelectorAll('.reveal');
            const revealOnScroll = () => {
                const windowHeight = window.innerHeight;
                reveals.forEach((reveal) => {
                    const elementTop = reveal.getBoundingClientRect().top;
                    if (elementTop < windowHeight - 100) reveal.classList.add('active');
                });
            };
            window.addEventListener('scroll', revealOnScroll);
            revealOnScroll();

            // Scroll Indicator Logic
            const sections = Array.from(document.querySelectorAll('section, footer'));
            const indicator = document.getElementById('scroll-indicator');
            let scrollTimeout;

            // Create dots
            sections.forEach((_, index) => {
                const dot = document.createElement('div');
                dot.className = 'scroll-nav-dot';
                dot.onclick = () => {
                    sections[index].scrollIntoView({ behavior: 'smooth' });
                };
                indicator.appendChild(dot);
            });

            const updateScrollIndicator = () => {
                const dots = document.querySelectorAll('.scroll-nav-dot');
                let currentSection = 0;
                
                sections.forEach((section, index) => {
                    const rect = section.getBoundingClientRect();
                    if (rect.top < window.innerHeight / 2) {
                        currentSection = index;
                    }
                });

                dots.forEach((dot, index) => {
                    dot.classList.toggle('active', index === currentSection);
                });

                // Visibility logic
                indicator.classList.add('visible');
                clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(() => {
                    indicator.classList.remove('visible');
                }, 2000);
            };

            window.addEventListener('scroll', updateScrollIndicator);
            updateScrollIndicator();

            const currentPath = window.location.pathname.split('/').pop() || 'index.html';
            document.querySelectorAll('.nav-link').forEach(link => {
                if(link.getAttribute('href').includes(currentPath)) {
                    link.classList.add('text-primary');
                    link.querySelector('span')?.classList.add('w-full');
                }
            });
        });
    </script>
</body>
</html>"""

def load_content_map():
    with open(CONTENT_MAP_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_home_content(data, asset_prefix):
    sections = data["sections"]
    # Using the new Architectural Gray Hero image
    hero_image = f"{asset_prefix}assets/images/architectural_hero_gray.png"
    
    slideshow_images = [
        f"{asset_prefix}assets/images/hero_slideshow_1.png",
        f"{asset_prefix}assets/images/hero_slideshow_2.png",
        f"{asset_prefix}assets/images/hero_slideshow_3.png",
        f"{asset_prefix}assets/images/hero_slideshow_4.jpg",
        f"{asset_prefix}assets/images/hero_slideshow_5.jpg"
    ]
    
    return f"""
    <section class="relative min-h-[95vh] flex items-center overflow-hidden px-4 md:px-0 pt-20"
             x-data='{{ 
                activeSlide: 0, 
                slides: {json.dumps(slideshow_images)},
                init() {{
                    setInterval(() => {{
                        this.activeSlide = (this.activeSlide + 1) % this.slides.length;
                    }}, 2000);
                }}
             }}'>
        
        <!-- Background Ambient Slideshow (Blurred) -->
        <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
            <template x-for="(slide, index) in slides" :key="'bg-' + index">
                <div x-show="activeSlide === index"
                     x-transition:enter="transition ease-out duration-1000"
                     x-transition:enter-start="opacity-0 scale-125"
                     x-transition:enter-end="opacity-40 scale-100"
                     x-transition:leave="transition ease-in duration-1000"
                     x-transition:leave-start="opacity-40 scale-100"
                     x-transition:leave-end="opacity-0 scale-110"
                     class="absolute inset-0 bg-cover bg-center blur-[120px] saturate-150"
                     :style="'background-image: url(' + slide + ')'">
                </div>
            </template>
        </div>

        <!-- Opal Glass Layer / Frost Effect -->
        <div class="absolute inset-0 z-1 bg-background/60 backdrop-blur-3xl border-b border-white/5"></div>
        <div class="absolute inset-0 z-1 bg-white/[0.02] mix-blend-overlay"></div>

        <div class="max-w-7xl mx-auto px-8 relative z-10 w-full grid md:grid-cols-2 gap-20 items-center">
            <!-- Text Content on left -->
            <div class="space-y-10 reveal">
                <div class="inline-flex items-center gap-4">
                    <span class="h-px w-8 bg-primary"></span>
                    <span class="text-primary tracking-[0.4em] uppercase text-[10px] font-bold">Exkluzív Ingatlanok</span>
                </div>
                <h1 class="text-3xl md:text-5xl font-serif text-text leading-[1.1] drop-shadow-sm">{sections['hero']['headline']}</h1>
                <p class="text-sm md:text-base text-text/70 max-w-lg leading-relaxed font-light border-l border-primary/20 pl-8">{sections['hero']['subheadline']}</p>
                
                <!-- Quick Search integrated into Hero -->
                <div class="pt-10 space-y-6" x-data="{{ quickSearch: '' }}">
                    <div class="bg-white/5 backdrop-blur-xl border border-white/10 p-2 flex items-center max-w-md shadow-2xl">
                        <input type="text" x-model="quickSearch" @keyup.enter="window.location.href = '{asset_prefix}ingatlanok/index.html?search=' + encodeURIComponent(quickSearch)" placeholder="Város (pl. Szeged)..." 
                               class="bg-transparent border-none outline-none px-6 py-3 text-sm text-text/80 placeholder:text-text/30 flex-grow font-light">
                        <button @click="window.location.href = '{asset_prefix}ingatlanok/index.html?search=' + encodeURIComponent(quickSearch)"
                           class="bg-primary hover:bg-white text-background px-8 py-3 text-[10px] uppercase tracking-[0.2em] font-bold transition-all">
                           Keresés
                        </button>
                    </div>
                    <div class="flex gap-4">
                        <a href="{asset_prefix}ingatlanok/index.html?type=Lakás" class="text-[10px] uppercase tracking-[0.2em] text-text/40 hover:text-primary transition-colors">#Lakás</a>
                        <a href="{asset_prefix}ingatlanok/index.html?type=Ház" class="text-[10px] uppercase tracking-[0.2em] text-text/40 hover:text-primary transition-colors">#Ház</a>
                        <a href="{asset_prefix}ingatlanok/index.html?type=Telek" class="text-[10px] uppercase tracking-[0.2em] text-text/40 hover:text-primary transition-colors">#Telek</a>
                    </div>
                </div>
            </div>

            <!-- Sharp Slideshow on right -->
            <div class="relative reveal delay-200">
                <div class="relative z-10">
                     <div class="relative aspect-[4/5] bg-surface overflow-hidden shadow-[0_40px_100px_-20px_rgba(0,0,0,0.9)] border border-white/10">
                        <template x-for="(slide, index) in slides" :key="'sharp-' + index">
                            <div x-show="activeSlide === index"
                                 x-transition:enter="transition ease-out duration-700"
                                 x-transition:enter-start="opacity-0 scale-110"
                                 x-transition:enter-end="opacity-100 scale-100"
                                 x-transition:leave="transition ease-in duration-700"
                                 x-transition:leave-start="opacity-100 scale-100"
                                 x-transition:leave-end="opacity-0 scale-95"
                                 class="absolute inset-0 bg-cover bg-center"
                                 :style="'background-image: url(' + slide + ')'">
                                <div class="absolute inset-0 bg-gradient-to-t from-background/40 to-transparent"></div>
                            </div>
                        </template>
                     </div>
                     <div class="absolute -top-10 -right-10 w-full h-full border border-primary/10 -z-10"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- My Mission Section -->
    <section class="py-40 relative border-y border-divider">
        <div class="max-w-5xl mx-auto px-8 relative z-10">
            <div class="grid md:grid-cols-[1.2fr_2fr] gap-24 items-start reveal">
                <div class="space-y-8">
                    <span class="text-primary tracking-[0.4em] uppercase text-[10px] font-bold block">Küldetésem</span>
                    <h2 class="text-3xl md:text-4xl font-serif text-text italic leading-tight">Bízd rám ingatlanod eladását / kiadását!</h2>
                </div>
                <div class="space-y-10">
                    <p class="text-xl md:text-2xl text-text/90 font-serif leading-relaxed italic border-l-2 border-primary/40 pl-10">
                        "Rájöttem, hogy a valódi hivatásom az, hogy levegyem az Ügyfelek vállairól a terhet, ami egy ingatlan eladása / kiadása / vétele / bérlése jelent!"
                    </p>
                    <p class="text-sm md:text-base text-text/50 font-light leading-loose tracking-wide">
                        Biztos vagyok abban, hogy a munkád, és a napi kötelezettségeid mellett Neked is kevés időd van a számodra fontos és kellemes dolgokkal foglalkozni, ezért ne áldozd az értékes időd hirdetésekre, telefonálásra... 
                        <span class="text-white font-medium">Bízd az ingatlanoddal kapcsolatos ügyeid rám!</span>
                    </p>
                </div>
            </div>
        </div>
    </section>

    <section class="py-32 relative bg-surface/30">
        <div class="max-w-7xl mx-auto px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 reveal">
                {"".join([f'<div class="p-10 border border-white/5 group hover:border-primary/40 transition-all"><p class="text-4xl font-serif text-text mb-4 group-hover:text-primary transition-colors">{s["value"]}</p><p class="text-text/40 text-[10px] tracking-[0.3em] uppercase">{s["label"]}</p></div>' for s in sections['stats']])}
            </div>
        </div>
    </section>

    <section class="py-40 relative">
        <div class="max-w-7xl mx-auto px-8">
            <div class="grid md:grid-cols-3 gap-1 reveal">
                {"".join([f'<div class="group relative bg-surface p-12 border border-white/5 hover:bg-white/5 transition-all duration-700 min-h-[400px] flex flex-col justify-end"><div class="absolute top-12 left-12 w-10 h-px bg-primary/40 group-hover:w-20 transition-all"></div><h3 class="text-2xl font-serif mb-6 text-text">{svc["title"]}</h3><p class="text-text/40 leading-relaxed font-light text-sm">{svc["desc"]}</p></div>' for svc in sections['services']])}
            </div>
        </div>
    </section>
    """

def load_about_image():
    return "https://restasrenata.hu/themes/ingatlan2/assets/images/rolam2.webp"

def generate_about_content(data, asset_prefix):
    return f"""
    <div class="py-40 text-center relative overflow-hidden border-b border-divider">
        <div class="relative z-10 max-w-4xl mx-auto px-8">
            <span class="text-primary tracking-[0.4em] uppercase text-[10px] font-bold block mb-10">Bemutatkozás</span>
            <h1 class="text-3xl md:text-5xl font-serif text-text italic reveal leading-tight">Üdvözöllek az oldalamon!</h1>
        </div>
    </div>

    <div class="max-w-7xl mx-auto px-8 py-40">
        <div class="grid md:grid-cols-2 gap-32 items-start">
             <div class="reveal sticky top-40">
                <div class="relative group">
                    <div class="relative z-10 p-0 shadow-2xl rotate-2 group-hover:rotate-0 transition-transform duration-1000">
                        <img src="{load_about_image()}" alt="Restás Renáta" class="w-full h-auto">
                    </div>
                </div>
             </div>

             <div class="reveal delay-200 space-y-12">
                <div class="prose prose-lg prose-invert font-light text-text/70 leading-relaxed max-w-none">
                    <p class="text-text/90 italic font-serif text-2xl mb-10">"Az ingatlan az elhivatottságom."</p>
                    <p>Az ingatlanértékesítéssel még nagyon fiatalon, 2009-ben találkoztam először. Már kezdőként kirajzolódott bennem, hogy tetszik az, amit ez a szakma nyújthat nekem, valahogy mégsem találtam a helyem.</p>
                    <p class="text-white">Végül <span class="border-b border-primary/50 pb-1">2018. január 5-én</span> lettem vállalkozó szinten is ingatlanközvetítő!</p>
                    <p>Rájöttem, hogy a valódi hivatásom az, hogy levegyem az ügyfelek vállairól a terhet...</p>
                    
                    <div class="py-12 px-12 border border-white/5 bg-surface/50 space-y-8">
                        <h3 class="text-xs uppercase tracking-[0.4em] text-primary font-bold">Amiben számíthatsz rám</h3>
                        <ul class="space-y-4 text-sm tracking-wide list-none pl-0 font-light opacity-80">
                            <li>- Jogi háttér ellenőrzése</li>
                            <li>- Dokumentáció beszerzése</li>
                            <li>- Marketing és hirdetéskezelés</li>
                            <li>- Profi megtekintések leszervezése</li>
                        </ul>
                    </div>

                    <p class="text-xl italic font-serif text-text/80">Sikeres szerződéskötés után minden résztvevő boldogan távozik.</p>
                </div>
                
                <div class="pt-16 border-t border-divider flex flex-col gap-6">
                    <a href="mailto:hello@restasrenata.hu" class="text-2xl font-serif text-text hover:text-primary transition-colors">hello@restasrenata.hu</a>
                    <a href="tel:+36703845025" class="text-2xl font-serif text-text hover:text-primary transition-colors">+36 70 384 5025</a>
                </div>
             </div>
        </div>
    </div>
    """

def generate_standard_content(data, asset_prefix):
    return f"""
    <div class="py-40 text-center border-b border-divider">
        <h1 class="text-3xl md:text-5xl font-serif text-text italic reveal leading-tight">{data.get('h1')}</h1>
    </div>
    <div class="max-w-4xl mx-auto px-8 py-32 reveal">
        <div class="prose prose-lg prose-invert font-light text-text/50 leading-loose">{data.get('content', '')}</div>
    </div>
    """

def generate_properties_content(data, asset_prefix):
    return f"""
    <div class="py-40 text-center relative overflow-hidden">
        <div class="absolute inset-0 z-0 bg-background/40 backdrop-blur-3xl"></div>
        <div class="relative z-10 max-w-4xl mx-auto px-8">
            <span class="text-primary tracking-[0.4em] uppercase text-[10px] font-bold block mb-10">Kínálatunk</span>
            <h1 class="text-3xl md:text-5xl font-serif text-text italic reveal leading-tight">Válogasson exkluzív ingatlanainkból</h1>
        </div>
    </div>

    <section class="pb-40 relative px-8" x-data='{{ 
        search: "", 
        type: "Mindegy", 
        minPrice: 0, 
        maxPrice: 300,
        properties: {json.dumps(SAMPLE_PROPERTIES)},
        modalOpen: false,
        selectedP: null,
        init() {{
            const params = new URLSearchParams(window.location.search);
            if (params.get("search")) this.search = params.get("search");
            if (params.get("type")) this.type = params.get("type");
        }},
        openDetail(p) {{
            this.selectedP = p;
            this.modalOpen = true;
            document.body.style.overflow = "hidden";
        }},
        closeDetail() {{
            this.modalOpen = false;
            document.body.style.overflow = "auto";
        }}
    }}'>
        <!-- Filter Bar -->
        <div class="max-w-7xl mx-auto mb-24 reveal">
            <div class="bg-surface/50 backdrop-blur-3xl border border-white/5 p-8 md:p-12 shadow-2xl grid md:grid-cols-4 gap-8">
                <div class="space-y-4">
                    <label class="text-[10px] uppercase tracking-[0.4em] text-text/30">Város</label>
                    <input type="text" x-model="search" placeholder="Pl. Szeged" 
                           class="w-full bg-transparent border-b border-white/10 py-2 focus:border-primary outline-none transition-all font-light text-text/80">
                </div>
                <div class="space-y-4">
                    <label class="text-[10px] uppercase tracking-[0.4em] text-text/30">Típus</label>
                    <select x-model="type" class="w-full bg-transparent border-b border-white/10 py-2 focus:border-primary outline-none transition-all font-light text-text/80 appearance-none">
                        <option value="Mindegy" class="bg-surface">Mindegy</option>
                        <option value="Lakás" class="bg-surface">Lakás</option>
                        <option value="Ház" class="bg-surface">Ház</option>
                        <option value="Telek" class="bg-surface">Telek</option>
                    </select>
                </div>
                <div class="space-y-4">
                    <label class="text-[10px] uppercase tracking-[0.4em] text-text/30">Min. ár (M Ft)</label>
                    <input type="number" x-model="minPrice" placeholder="0" 
                           class="w-full bg-transparent border-b border-white/10 py-2 focus:border-primary outline-none transition-all font-light text-text/80">
                </div>
                <div class="space-y-4">
                    <label class="text-[10px] uppercase tracking-[0.4em] text-text/30">Max. ár (M Ft)</label>
                    <input type="number" x-model="maxPrice" placeholder="300" 
                           class="w-full bg-transparent border-b border-white/10 py-2 focus:border-primary outline-none transition-all font-light text-text/80">
                </div>
            </div>
        </div>

        <!-- Property Grid -->
        <div class="max-w-7xl mx-auto">
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-1 reveal group/grid">
                <template x-for="p in properties.filter(i => 
                    (search === '' || i.city.toLowerCase().includes(search.toLowerCase())) &&
                    (type === 'Mindegy' || i.type === type) &&
                    (i.price >= minPrice * 1000000) &&
                    (i.price <= maxPrice * 1000000)
                )" :key="p.title">
                    <div class="group relative bg-surface border border-white/5 transition-all duration-700 hover:scale-[1.02] hover:z-20 hover:shadow-[0_40px_100px_-20px_rgba(0,0,0,0.8)] overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img :src="'{asset_prefix}' + p.image" class="w-full h-full object-cover transition-transform duration-[2s] group-hover:scale-110">
                        </div>
                        <div class="p-8 space-y-6">
                            <div class="flex justify-between items-start">
                                <span class="text-[10px] uppercase tracking-[0.4em] text-primary font-bold" x-text="p.type"></span>
                                <span class="text-[10px] uppercase tracking-[0.4em] text-text/30" x-text="p.city"></span>
                            </div>
                            <h3 class="text-xl font-serif text-text leading-tight group-hover:text-primary transition-colors h-14" x-text="p.title"></h3>
                            <div class="pt-6 border-t border-white/5 flex justify-between items-center">
                                <p class="text-xl font-serif text-text/90" x-text="(p.price/1000000).toFixed(1) + ' M Ft'"></p>
                                <p class="text-[10px] uppercase tracking-[0.4em] text-text/30" x-text="p.area + ' m²'"></p>
                            </div>
                            <div class="pt-4">
                                <div @click="openDetail(p)" class="w-full text-center py-4 border border-white/10 uppercase text-[10px] tracking-[0.4em] font-bold hover:bg-white hover:text-background transition-all cursor-pointer">
                                    Részletek
                                </div>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
        </div>

        <!-- Property Detail Modal -->
        <div x-show="modalOpen" 
             x-transition:enter="transition ease-out duration-300"
             x-transition:enter-start="opacity-0"
             x-transition:enter-end="opacity-100"
             x-transition:leave="transition ease-in duration-200"
             x-transition:leave-start="opacity-100"
             x-transition:leave-end="opacity-0"
             class="fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-8" x-cloak>
            
            <!-- Backdrop -->
            <div class="absolute inset-0 bg-background/90 backdrop-blur-xl" @click="closeDetail()"></div>
            
            <!-- Modal Content -->
            <div class="relative w-full max-w-6xl bg-surface border border-white/10 shadow-2xl overflow-hidden flex flex-col md:flex-row max-h-[90vh]"
                 @click.away="closeDetail()">
                
                <!-- Close Button -->
                <button @click="closeDetail()" class="absolute top-6 right-6 z-50 text-white/50 hover:text-white transition-colors">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>

                <!-- Image Gallery (Simplified) -->
                <div class="w-full md:w-1/2 bg-black flex items-center justify-center relative group">
                    <img :src="'{asset_prefix}' + selectedP?.image" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                    <div class="absolute bottom-8 left-8 text-white">
                        <p class="text-[10px] uppercase tracking-[0.4em] text-primary font-bold mb-2" x-text="selectedP?.type"></p>
                        <h2 class="text-2xl md:text-3xl font-serif" x-text="selectedP?.title"></h2>
                    </div>
                </div>

                <!-- Detail Text -->
                <div class="w-full md:w-1/2 p-12 overflow-y-auto bg-surface relative">
                    <div class="space-y-10">
                        <section class="grid grid-cols-2 gap-8 border-b border-white/5 pb-10">
                            <div class="space-y-2">
                                <p class="text-[10px] uppercase tracking-[0.4em] text-text/30">Irányár</p>
                                <p class="text-3xl font-serif text-primary" x-text="(selectedP?.price/1000000).toFixed(1) + ' M Ft'"></p>
                            </div>
                            <div class="space-y-2">
                                <p class="text-[10px] uppercase tracking-[0.4em] text-text/30">Alapterület</p>
                                <p class="text-3xl font-serif text-text" x-text="selectedP?.area + ' m²'"></p>
                            </div>
                        </section>

                        <section class="space-y-6">
                            <h4 class="text-[10px] uppercase tracking-[0.4em] text-primary font-bold">Leírás</h4>
                            <p class="text-text/70 leading-relaxed font-light" x-text="selectedP?.desc"></p>
                        </section>

                        <section class="space-y-6">
                            <h4 class="text-[10px] uppercase tracking-[0.4em] text-primary font-bold">Jellemzők</h4>
                            <div class="grid grid-cols-2 gap-4">
                                <template x-for="detail in selectedP?.details" :key="detail">
                                    <div class="flex items-center gap-3 text-sm text-text/50 font-light">
                                        <span class="w-1 h-1 bg-primary"></span>
                                        <span x-text="detail"></span>
                                    </div>
                                </template>
                            </div>
                        </section>

                        <section class="pt-10 border-t border-white/5 space-y-8">
                            <div class="flex items-center gap-6">
                                <img src="{asset_prefix}assets/images/logo3.png" class="h-12 w-auto opacity-50">
                                <div>
                                    <p class="text-xs font-serif text-text tracking-widest uppercase">Restás <span class="font-light italic">Renáta</span></p>
                                    <p class="text-[10px] text-text/30 uppercase tracking-[0.2em] mt-1">Ingatlanközvetítő</p>
                                </div>
                            </div>
                            <div class="flex flex-col md:flex-row gap-6">
                                <a href="tel:+36703845025" class="flex-grow text-center py-5 bg-white text-background uppercase text-[10px] tracking-[0.3em] font-bold hover:bg-primary transition-all">
                                    Hívás: +36 70 384 5025
                                </a>
                                <a href="mailto:hello@restasrenata.hu" class="flex-grow text-center py-5 border border-white/20 uppercase text-[10px] tracking-[0.3em] font-bold hover:bg-white hover:text-background transition-all">
                                    Email küldése
                                </a>
                            </div>
                        </section>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

def generate_contact_content(data, asset_prefix):
    contact = data['contact_info']
    return f"""
    <div class="max-w-7xl mx-auto px-8 py-40 min-h-[80vh] flex flex-col justify-center">
        <div class="grid md:grid-cols-2 gap-32 items-start">
            <div class="reveal">
                <span class="text-primary tracking-[0.4em] uppercase text-[10px] font-bold block mb-10">Kapcsolat</span>
                <h1 class="text-4xl md:text-6xl font-serif text-text mb-12 italic leading-none">{data.get('h1')}</h1>
                <div class="space-y-10">
                    <a href="tel:{contact['phone']}" class="text-2xl md:text-3xl font-serif text-text block hover:text-primary transition-colors tracking-tight">{contact['phone']}</a>
                    <a href="mailto:{contact['email']}" class="text-xl md:text-2xl font-serif text-text/50 block hover:text-white transition-colors">{contact['email']}</a>
                </div>
            </div>
            <div class="reveal delay-200 border border-white/5 p-16">
                <form class="space-y-12">
                    <div class="space-y-4 border-b border-white/10 pb-4"><label class="text-[10px] uppercase tracking-[0.4em] text-text/30">Név</label><input type="text" class="w-full bg-transparent border-none focus:outline-none focus:ring-0 p-0 text-xl font-light"></div>
                    <div class="space-y-4 border-b border-white/10 pb-4"><label class="text-[10px] uppercase tracking-[0.4em] text-text/30">Email</label><input type="email" class="w-full bg-transparent border-none focus:outline-none focus:ring-0 p-0 text-xl font-light"></div>
                    <button class="w-full border border-white py-6 uppercase text-[10px] tracking-[0.4em] font-bold hover:bg-white hover:text-background transition-all">Üzenet Küldése</button>
                </form>
            </div>
        </div>
    </div>
    """

def main():
    pages = load_content_map()
    for page in pages:
        filename = page["filename"]
        if "/" in filename: os.makedirs(BASE_DIR / os.path.dirname(filename), exist_ok=True)
        file_path = BASE_DIR / filename
        depth = filename.count("/")
        asset_prefix = "../" * depth if depth > 0 else ""
        
        if page["content_type"] == "home":
            content_body = generate_home_content(page, asset_prefix)
        elif page["content_type"] == "about":
            content_body = generate_about_content(page, asset_prefix)
        elif page["content_type"] == "contact":
            content_body = generate_contact_content(page, asset_prefix)
        elif page["content_type"] == "properties":
            content_body = generate_properties_content(page, asset_prefix)
        else:
            content_body = generate_standard_content(page, asset_prefix)
            
        final_html = MASTER_TEMPLATE.replace("{{ title }}", page["title"]).replace("{{ description }}", page["description"]).replace("{{ content_body }}", content_body).replace("{{ asset_prefix }}", asset_prefix)
        with open(file_path, "w", encoding="utf-8") as f: f.write(final_html)
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main()
