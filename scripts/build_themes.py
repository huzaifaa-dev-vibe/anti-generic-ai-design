#!/usr/bin/env python3
"""Generator for data/themes-100.json — 100 curated design themes."""
import json
from pathlib import Path

T = []  # themes list


def add(**kw):
    T.append(kw)


# ---------------------------------------------------------------------------
# 1-12: Editorial / Publication
# ---------------------------------------------------------------------------
add(
    id="t001",
    name="Editorial Dark",
    voice="premium, precise, cinematic",
    best_for=["saas", "portfolio", "agency"],
    palette={"bg": "#0A0A0B", "surface": "#18181B", "text": "#E4E4E7", "accent": "#F59E0B", "muted": "#A1A1AA"},
    type={"display": "Fraunces", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle-grain + glass-on-dark",
    motion_energy="measured",
    corner_radius="mixed (sharp images, 12px cards, pill buttons)",
    shadow_style="layered, low-opacity, no harsh edges",
    references=["linear.app", "vercel.com", "resend.com"],
    rationale="Dark editorial reads as premium without being cold. Warm amber accent (vs. the AI-default indigo) signals confidence and craft. Fraunces in the hero gives an editorial moment; Inter handles the UI. Subtle grain keeps the dark from feeling flat. Motion is restrained — only product UI animates.",
    anti_patterns=["indigo-violet gradients", "pure black bg", "pure white text", "fade-in-up everywhere"],
)

add(
    id="t002",
    name="Editorial Off-White",
    voice="considered, literary, warm",
    best_for=["media", "docs", "personal"],
    palette={"bg": "#FAF9F6", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#B8341B", "muted": "#6B6B6B"},
    type={"display": "Fraunces", "body": "Source Serif 4", "mono": "JetBrains Mono"},
    texture="paper-grain at 4% opacity",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — rely on rules and type weight",
    references=["nytimes.com", "theverge.com", "makemediagreat.com"],
    rationale="Off-white paper background reads as printed page, not screen. Oxblood accent gives editorial gravitas without being funereal. Fraunces display + Source Serif body makes the whole page feel like one continuous voice. Avoid shadows entirely; let typography and horizontal rules do the structural work.",
    anti_patterns=["drop shadows on cards", "rounded corners", "sans-serif body", "blue link color"],
)

add(
    id="t003",
    name="Newsprint Cream",
    voice="nostalgic, dense, journalistic",
    best_for=["media", "personal", "docs"],
    palette={"bg": "#F5F1E8", "surface": "#FFFFFF", "text": "#1C1C1A", "accent": "#2D5016", "muted": "#6B675E"},
    type={"display": "Playfair Display", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="heavy paper grain + faint ink mottle",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none",
    references=["bloomberg.com", "theatlantic.com", "longreads.com"],
    rationale="Cream simulates aged newsprint and lowers eye strain for long-form reading. Deep olive accent evokes old masthead ink without being literal. Serif pairing keeps columns justified and readable. Use heavy paper grain only on hero surfaces, never on body text.",
    anti_patterns=["bright white bg", "sans-serif headlines", "rounded card corners", "gradient overlays"],
)

add(
    id="t004",
    name="Newspaper Columnar",
    voice="authoritative, dense, civic",
    best_for=["media", "docs", "nonprofit"],
    palette={"bg": "#F8F6F0", "surface": "#FFFFFF", "text": "#111111", "accent": "#9B1C1C", "muted": "#595959"},
    type={"display": "Crimson Pro", "body": "Source Serif 4", "mono": "Source Code Pro"},
    texture="column rules + thin baseline grid",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — column rules separate content",
    references=["nytimes.com", "ft.com", "propublica.org"],
    rationale="Multi-column flow with vertical rules mimics broadsheet layout and increases reading speed. Crimson Pro display holds its weight at large sizes while Source Serif body keeps body legible. Restrict accent to masthead, pull quotes, and datelines only — never decorative.",
    anti_patterns=["single-column hero", "card grids", "drop shadows", "saturated accents"],
)

add(
    id="t005",
    name="Publication Serif",
    voice="scholarly, refined, patient",
    best_for=["media", "docs", "personal"],
    palette={"bg": "#FBFAF7", "surface": "#FFFFFF", "text": "#1F1B16", "accent": "#7C2D12", "muted": "#6B6258"},
    type={"display": "Newsreader", "body": "Newsreader", "mono": "IBM Plex Mono"},
    texture="matte, no grain",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none",
    references=["aeon.co", "3quarksdaily.com", "harpers.org"],
    rationale="One serif family across display and body creates the unified voice of a literary journal. Newsreader's optical sizing gives display warmth without body muddiness. Restrained palette keeps focus on prose. Use generous leading (1.7) and a 66-character measure.",
    anti_patterns=["mixed type families", "background images", "auto-play motion", "drop caps larger than 3 lines"],
)

add(
    id="t006",
    name="Magazine Glossy",
    voice="aspirational, bold, photographic",
    best_for=["media", "marketing", "agency"],
    palette={"bg": "#0D0D0F", "surface": "#1A1A1E", "text": "#F5F5F5", "accent": "#E0245E", "muted": "#9A9A9A"},
    type={"display": "Bricolage Grotesque", "body": "Inter", "mono": "JetBrains Mono"},
    texture="high-contrast full-bleed photography + duotone",
    motion_energy="cinematic",
    corner_radius="sharp 0px",
    shadow_style="hard photographic shadow under overlays",
    references=["kus.tea", "mrmagazine.com", "dazeddigital.com"],
    rationale="Full-bleed imagery with oversized type creates the rhythm of a print fashion spread. Magenta accent punches through black without going neon. Bricolage display gives the cover energy; Inter handles captions and credits. Motion is cinematic — slow fades, parallax, scroll-driven reveals.",
    anti_patterns=["centered text on photos", "small body type over images", "soft rounded cards", "pastel palette"],
)

add(
    id="t007",
    name="Long-Form Reader",
    voice="quiet, focused, generous",
    best_for=["docs", "personal", "media"],
    palette={"bg": "#FFFEFB", "surface": "#FFFFFF", "text": "#232323", "accent": "#3B5BA5", "muted": "#737373"},
    type={"display": "Lora", "body": "Lora", "mono": "Spline Sans Mono"},
    texture="none — pure flat",
    motion_energy="calm",
    corner_radius="soft 6px",
    shadow_style="none",
    references=["readwise.io/spaced-repetition", "martinfowler.com", "paulgraham.com"],
    rationale="Maximum reading comfort is the only goal. Single serif family, wide measure (38em), 1.7 leading. Indigo-blue accent for links and footnotes only. No images in body, no callouts, no shadows — nothing competes with the prose.",
    anti_patterns=["sidebar widgets", "autoloading popups", "marketing CTAs in body", "decorative dividers"],
)

add(
    id="t008",
    name="Cinematic Noir",
    voice="dramatic, austere, late-night",
    best_for=["media", "portfolio", "agency"],
    palette={"bg": "#08080A", "surface": "#141418", "text": "#EDEDED", "accent": "#C49B3C", "muted": "#888888"},
    type={"display": "DM Serif Display", "body": "Inter", "mono": "JetBrains Mono"},
    texture="vignette + film grain at 6%",
    motion_energy="cinematic",
    corner_radius="sharp 0px",
    shadow_style="deep falloff, single direction",
    references=["a24.com", "criterion.com", "mubi.com"],
    rationale="Noir uses deep blacks (not zinc-950) and a single antique-gold accent to evoke 35mm film. DM Serif Display gives the hero the weight of a title card. Film grain and vignette carry the cinematic feeling without animation. Use sparingly — too much grain and it becomes parody.",
    anti_patterns=["neon accents", "rounded corners", "cheerful color", "fade-in-up reveals"],
)

add(
    id="t009",
    name="Documentary Mono",
    voice="forensic, sober, factual",
    best_for=["media", "nonprofit", "docs"],
    palette={"bg": "#F2F2F2", "surface": "#FFFFFF", "text": "#111111", "accent": "#C0392B", "muted": "#666666"},
    type={"display": "Archivo Black", "body": "IBM Plex Sans", "mono": "IBM Plex Mono"},
    texture="none — flat with hard 1px rules",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — rules only",
    references=["propublica.org", "icij.org", "reuters.com"],
    rationale="Documentary design treats every element as evidence. Monospace data, hard horizontal rules, black-on-white photos. Accent red is reserved for warnings, sources, and corrections — never decoration. Avoid animation: it implies editorializing.",
    anti_patterns=["decorative motion", "rounded corners", "soft shadows", "color photography"],
)

add(
    id="t010",
    name="Journal Minimal",
    voice="quiet, contemplative, daily",
    best_for=["personal", "docs", "media"],
    palette={"bg": "#FDFCFA", "surface": "#FFFFFF", "text": "#222222", "accent": "#3F6212", "muted": "#7A7A7A"},
    type={"display": "Spectral", "body": "Spectral", "mono": "IBM Plex Mono"},
    texture="none",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none",
    references=["maggieappleton.com", "martinfowler.com", "jvns.ca"],
    rationale="The personal-journal aesthetic: one type family, one accent, generous whitespace, and dated entries. Spectral's open forms read warmly at body sizes. Olive-green accent suggests growth without being literal. No CTAs, no cards — just dated prose.",
    anti_patterns=["hero banners", "newsletter modals", "feature card grids", "colored backgrounds"],
)

add(
    id="t011",
    name="Zine Brutalist",
    voice="rebellious, raw, hand-made",
    best_for=["personal", "media", "agency"],
    palette={"bg": "#FFFF00", "surface": "#FFFFFF", "text": "#000000", "accent": "#FF0066", "muted": "#555555"},
    type={"display": "Anton", "body": "Work Sans", "mono": "Space Mono"},
    texture="xerox noise + visible halftone",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard offset 6px 6px #000",
    references=["are.na", "tumblr.com/zines", "noisey.vice.com"],
    rationale="Zine aesthetics intentionally break polish rules: yellow bg, black hard shadows, mismatched type sizes, halftone images. The point is energy, not refinement. Use only for genuinely subcultural work — corporate zine-washing reads as cringe.",
    anti_patterns=["gentle gradients", "soft shadows", "rounded corners", "considered spacing"],
)

add(
    id="t012",
    name="Print Companion",
    voice="tactical, archival, secondary",
    best_for=["docs", "media", "nonprofit"],
    palette={"bg": "#EFEAE0", "surface": "#FFFFFF", "text": "#1B1B1B", "accent": "#7A4A1F", "muted": "#6B6258"},
    type={"display": "IBM Plex Serif", "body": "IBM Plex Sans", "mono": "IBM Plex Mono"},
    texture="subtle paper grain",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none",
    references=["archives.gov", "smithsonianmag.com", "nypl.org"],
    rationale="The print-companion aesthetic treats the web as a printed supplement: condensed type, ruled sections, footnoted references. The single Plex family across serif/sans/mono gives unified voice without licensing cost. Accent is reserved for citation markers.",
    anti_patterns=["large hero imagery", "video backgrounds", "rounded card corners", "saturated accent colors"],
)

# ---------------------------------------------------------------------------
# 13-22: Swiss / Minimalist / Brutalist
# ---------------------------------------------------------------------------
add(
    id="t013",
    name="Swiss Minimalist White",
    voice="rigorous, mathematical, neutral",
    best_for=["portfolio", "agency", "docs"],
    palette={"bg": "#FFFFFF", "surface": "#F4F4F4", "text": "#0A0A0A", "accent": "#DC2626", "muted": "#737373"},
    type={"display": "Space Grotesk", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — pure flat",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="none — 1px rules",
    references=["interface-design.studio", "oliver.im", "stuffandnonsense.co.uk"],
    rationale="Swiss minimalism lives and dies by the 8-column grid. Single accent (red) for emphasis, everything else is grayscale. Space Grotesk gives the heading a slightly geometric edge over generic Inter. No images unless they're informational.",
    anti_patterns=["decorative gradients", "rounded corners", "drop shadows", "more than one accent color"],
)

add(
    id="t014",
    name="Helvetica Grid",
    voice="clean, technical, unsentimental",
    best_for=["saas", "docs", "dashboard"],
    palette={"bg": "#FFFFFF", "surface": "#FAFAFA", "text": "#111111", "accent": "#0044CC", "muted": "#737373"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="none — borders only",
    references=["apple.com", "designsystems.com", "ibm.com/design"],
    rationale="The grid is the design. Inter at tight tracking with strict 8px baseline. Blue accent for interactive elements only. No imagery, no decoration — typography and rules carry the whole composition. The kind of design that survives translation into 40 languages.",
    anti_patterns=["hero photography", "color gradients", "rounded corners", "decorative motion"],
)

add(
    id="t015",
    name="Bauhaus Primary",
    voice="geometric, playful, theoretical",
    best_for=["portfolio", "agency", "marketing"],
    palette={"bg": "#F5F2EA", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#E63946", "muted": "#3D405B"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "Space Mono"},
    texture="flat with hard-edged geometric overlays",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard offset shadows (4px 4px solid color)",
    references=["bauhaus.de", "designmuseum.org", "tate.org.uk"],
    rationale="Bauhaus uses primary colors as structural elements, not decoration. Red accent + indigo muted + cream bg gives the period palette without being costume. Geometric type (Bricolage + DM Sans) carries the angular energy. Hard offset shadows reinforce the geometric vocabulary.",
    anti_patterns=["soft gradients", "rounded corners", "realistic photography", "muted pastels"],
)

add(
    id="t016",
    name="Modernist Grid",
    voice="ordered, archival, international",
    best_for=["docs", "media", "nonprofit"],
    palette={"bg": "#FBFAF8", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#1D4ED8", "muted": "#6B6B6B"},
    type={"display": "Archivo", "body": "Public Sans", "mono": "IBM Plex Mono"},
    texture="none — strict baseline grid visible at 2% opacity",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none",
    references=["moma.org", "guggenheim.org", "designmuseum.org"],
    rationale="Modernism is the grid made visible. Archivo's condensed display + Public Sans body creates the institutional voice of a museum wayfinder. Blue accent used only for navigation state and section markers. The baseline grid is the rhythm — never break it.",
    anti_patterns=["asymmetric layouts", "decorative imagery", "rounded corners", "color gradients"],
)

add(
    id="t017",
    name="Studio Portfolio Bold",
    voice="confident, oversized, direct",
    best_for=["portfolio", "agency"],
    palette={"bg": "#0E0E0E", "surface": "#1A1A1A", "text": "#FFFFFF", "accent": "#E6FF3D", "muted": "#9A9A9A"},
    type={"display": "Bricolage Grotesque", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with high-contrast photography",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="none",
    references=["ueno.co", "basic.agency", "hyperakt.com"],
    rationale="Studio portfolios need a confident voice to compete. Acid yellow accent on near-black says 'we have a point of view.' Oversized Bricolage headlines (10vw+) carry the work; photography does the rest. Motion only on hover — let the work speak.",
    anti_patterns=["small body type", "centered everything", "pastel palette", "drop shadows"],
)

add(
    id="t018",
    name="Architectural Drawing",
    voice="technical, measured, drafted",
    best_for=["portfolio", "docs", "agency"],
    palette={"bg": "#F4F1EA", "surface": "#FFFFFF", "text": "#1C1C1A", "accent": "#B8541F", "muted": "#7A736A"},
    type={"display": "Space Grotesk", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle blueprint grid at 6% opacity",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — rules and annotations only",
    references=["oma.eu", "big.dk", "snohetta.com"],
    rationale="Architects communicate in plans, sections, and annotations. This theme treats the web page like a drawing sheet: cream bg, blueprint grid, ruled annotations, terra-cotta accent for callouts. No photography dominates — diagrams and drawings do.",
    anti_patterns=["glossy renderings", "rounded corners", "soft shadows", "decorative motion"],
)

add(
    id="t019",
    name="Museum Wall",
    voice="spacious, reverent, labeled",
    best_for=["portfolio", "media", "nonprofit"],
    palette={"bg": "#F5F4F0", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#5B2C6F", "muted": "#767676"},
    type={"display": "Cormorant", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="matte flat — gallery white",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — labels and rules",
    references=["moma.org", "tate.org.uk", "guggenheim.org"],
    rationale="The museum wall is generous negative space, captioned works, and one accent for the wall label. Cormorant display gives exhibition-catalog gravitas; Inter handles the wayfinder. Avoid drop shadows on imagery — they break the gallery illusion.",
    anti_patterns=["drop shadows on artwork", "rounded image corners", "marketing CTAs", "colorful backgrounds"],
)

add(
    id="t020",
    name="Clinical White",
    voice="sterile, legible, trust-first",
    best_for=["saas", "docs", "dashboard"],
    palette={"bg": "#FFFFFF", "surface": "#F7F9FA", "text": "#0F172A", "accent": "#0E7C7B", "muted": "#64748B"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — pure flat",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="very subtle 0 1px 2px rgba(0,0,0,0.04)",
    references=["verity.com", "carbonhealth.com", "doximity.com"],
    rationale="Clinical contexts need maximum legibility and minimum decoration. Teal accent signals health without the cliché medical blue. Inter at all sizes keeps the reading speed high. Shadows are nearly invisible — depth comes from 1px borders.",
    anti_patterns=["dark mode default", "vibrant gradients", "rounded pill buttons", "decorative imagery"],
)

add(
    id="t021",
    name="Brutalist Mono",
    voice="raw, structural, unstyled",
    best_for=["portfolio", "personal", "docs"],
    palette={"bg": "#FFFFFF", "surface": "#FFFFFF", "text": "#000000", "accent": "#FF3B00", "muted": "#737373"},
    type={"display": "Space Mono", "body": "Space Mono", "mono": "Space Mono"},
    texture="none — 1px borders everywhere",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="none — borders and rules",
    references=["brutalistwebsites.com", "ivy.studio", "hellothisisfield.com"],
    rationale="Brutalism exposes structure as style. One monospace family, 1px borders, default link colors, no shadows, no rounding. The orange accent is the only intentional design move. Use only when the audience understands the reference — otherwise it looks broken.",
    anti_patterns=["rounded corners", "drop shadows", "smooth animations", "decorative gradients"],
)

add(
    id="t022",
    name="Tech Brutalist",
    voice="industrial, dense, intentional",
    best_for=["saas", "portfolio", "agency"],
    palette={"bg": "#0A0A0A", "surface": "#161616", "text": "#EDEDED", "accent": "#FF4D00", "muted": "#7A7A7A"},
    type={"display": "Space Grotesk", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — visible borders and grid",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard 2px 2px 0 #FF4D00 on hover",
    references=["vercel.com", "linear.app", "supabase.com"],
    rationale="Tech brutalism is brutalist with intent: dark bg, sharp edges, visible borders, hard accent shadow. Space Grotesk display + Inter body is the modern dev-tool combo. Orange accent (instead of the AI-default violet) reads as engineer taste.",
    anti_patterns=["soft drop shadows", "rounded corners > 4px", "pastel palette", "decorative motion"],
)

# ---------------------------------------------------------------------------
# 23-32: Warm / Organic
# ---------------------------------------------------------------------------
add(
    id="t023",
    name="Mid-Century Warm",
    voice="nostalgic, optimistic, geometric",
    best_for=["portfolio", "marketing", "agency"],
    palette={"bg": "#E8DCC4", "surface": "#F2EAD8", "text": "#2A1F14", "accent": "#C0392B", "muted": "#7A6A4F"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "IBM Plex Mono"},
    texture="flat with subtle paper grain",
    motion_energy="measured",
    corner_radius="mixed (0px images, 4px cards, pill buttons)",
    shadow_style="soft 0 4px 12px rgba(42,31,20,0.08)",
    references=["dwell.com", "atomic-ranch.com", "eichlerhomes.com"],
    rationale="Mid-century palette: cream, ochre, rust, walnut. Bricolage display echoes period signage; DM Sans body keeps it readable. Geometric layouts (asymmetric grids, oversized numbers) reference the era. Motion is gentle — fades and slow slides only.",
    anti_patterns=["neon colors", "high-contrast shadows", "sharp 0px everything", "decorative gradients"],
)

add(
    id="t024",
    name="Scandinavian Muted",
    voice="calm, hygge, restrained",
    best_for=["portfolio", "ecommerce", "personal"],
    palette={"bg": "#F5F2EC", "surface": "#FFFFFF", "text": "#1F1F1D", "accent": "#3A5A40", "muted": "#8C8579"},
    type={"display": "Fraunces", "body": "Inter", "mono": "JetBrains Mono"},
    texture="soft matte with subtle paper grain",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="very soft, low-opacity",
    references=["muuto.com", "normann-copenhagen.com", "hAY.dk"],
    rationale="Scandinavian design is restrained warmth: muted greens, off-whites, walnut browns. Fraunces display + Inter body is the modern Nordic pairing. Generous whitespace, soft corners, gentle shadows. Motion only on hover, never on scroll.",
    anti_patterns=["high-contrast accents", "tight grids", "drop shadows", "auto-play motion"],
)

add(
    id="t025",
    name="Wabi-Sabi Organic",
    voice="imperfect, handmade, quiet",
    best_for=["portfolio", "personal", "ecommerce"],
    palette={"bg": "#EDE7DB", "surface": "#F4EFE6", "text": "#2B2620", "accent": "#8B6F47", "muted": "#8A7F6E"},
    type={"display": "Cormorant", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="heavy paper grain + visible brush strokes",
    motion_energy="calm",
    corner_radius="organic irregular (4-16px)",
    shadow_style="soft, warm-toned, low-opacity",
    references=["ienotemari.com", "kitcouture.com", "sawsasee.com"],
    rationale="Wabi-sabi finds beauty in imperfection. Cormorant display + Lora body gives the hand-set feel. Slightly irregular corner radii and visible brush textures signal craft. Accent colors are earth tones, never saturated. Motion is barely perceptible — slow, organic.",
    anti_patterns=["perfect geometric grids", "neon accents", "drop shadows", "fade-in-up reveals"],
)

add(
    id="t026",
    name="Cottagecore",
    voice="whimsical, pastoral, romantic",
    best_for=["ecommerce", "personal", "media"],
    palette={"bg": "#F8F3E9", "surface": "#FFFFFF", "text": "#3B2A1A", "accent": "#9B4D2A", "muted": "#8B7355"},
    type={"display": "Cormorant", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="subtle botanical illustration overlay",
    motion_energy="calm",
    corner_radius="soft 12px",
    shadow_style="soft, warm-toned",
    references=["fawn-shop.com", "shopterrain.com", "floretflowers.com"],
    rationale="Cottagecore romanticizes rural life: cream backgrounds, sepia photography, hand-drawn florals. Cormorant + Lora gives the period-novel feel. Botanical illustrations as decorative elements (not stock photos). Motion is gentle — never energetic.",
    anti_patterns=["neon accents", "geometric grids", "drop shadows on cards", "tech-brutalist type"],
)

add(
    id="t027",
    name="Terracotta Earth",
    voice="warm, grounded, sun-baked",
    best_for=["portfolio", "ecommerce", "media"],
    palette={"bg": "#E8DDC9", "surface": "#F2EBD9", "text": "#3A2718", "accent": "#B65A3C", "muted": "#8A6F52"},
    type={"display": "Fraunces", "body": "DM Sans", "mono": "JetBrains Mono"},
    texture="subtle plaster texture",
    motion_energy="calm",
    corner_radius="soft 10px",
    shadow_style="warm soft shadow",
    references=["andrianna-shamarla.com", "roman-and-williams.com", "goodeeworld.com"],
    rationale="Terracotta's baked-earth palette evokes the Mediterranean. Fraunces display has the warmth of carved signage. Plaster texture (not paper grain) keeps the material reference consistent. Accent is reserved for hand-painted callouts.",
    anti_patterns=["cool blue accents", "pure white bg", "geometric sans display", "tight grid layouts"],
)

add(
    id="t028",
    name="Library Reading Room",
    voice="scholarly, leather-bound, hushed",
    best_for=["docs", "personal", "media"],
    palette={"bg": "#1F1A14", "surface": "#2A2419", "text": "#E8DDC9", "accent": "#C8A05A", "muted": "#9A8B70"},
    type={"display": "Crimson Pro", "body": "Source Serif 4", "mono": "IBM Plex Mono"},
    texture="subtle leather grain",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — gold rules only",
    references=["jstor.org", "britannica.com", "oxfordacademic.com"],
    rationale="The reading-room aesthetic is dark walnut, leather, and brass — translated to web as warm darks and a gold accent. Crimson Pro display + Source Serif body is the academic-press pairing. Restrict gold to rules, section markers, and folio numbers.",
    anti_patterns=["bright accents", "sans-serif display", "rounded corners", "decorative motion"],
)

add(
    id="t029",
    name="Workshop Wood",
    voice="craftsman, tactile, honest",
    best_for=["portfolio", "ecommerce", "agency"],
    palette={"bg": "#EAE0D0", "surface": "#F2EAD9", "text": "#2B1F14", "accent": "#6B3410", "muted": "#7A6A4F"},
    type={"display": "Archivo Black", "body": "Public Sans", "mono": "IBM Plex Mono"},
    texture="subtle wood grain + visible joinery lines",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="hard 2px 2px 0 #6B3410",
    references=["hammerandhand.com", "lostcraftsmen.com", "nakashimawoodworkers.com"],
    rationale="Workshop aesthetic celebrates visible joinery: hard shadows, sharp corners, wood-grain texture. Archivo Black display gives signage-on-crate weight. Brown accent (not red) for marks and labels. Motion is mechanical — linear easing, no bounce.",
    anti_patterns=["soft pastels", "rounded corners", "decorative gradients", "smooth easing"],
)

add(
    id="t030",
    name="Linen Natural",
    voice="soft, breathable, gentle",
    best_for=["ecommerce", "personal", "portfolio"],
    palette={"bg": "#F1EBE0", "surface": "#FAF5EC", "text": "#2B2620", "accent": "#6F8F6A", "muted": "#9A9183"},
    type={"display": "Fraunces", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="visible linen weave at 8% opacity",
    motion_energy="calm",
    corner_radius="soft 6px",
    shadow_style="soft, low-opacity, warm-toned",
    references=["eileenfisher.com", "smallable.com", "toast.co.uk"],
    rationale="Linen is the most neutral natural textile — beige, breathable, undyed. Fraunces + Lora gives the slow-fashion voice. Visible weave texture (only on backgrounds) makes the metaphor literal. Olive-green accent suggests plant dye, not synthetics.",
    anti_patterns=["neon accents", "high-contrast shadows", "drop shadows on cards", "geometric sans display"],
)

add(
    id="t031",
    name="Olive Branch",
    voice="peaceful, organic, restrained",
    best_for=["nonprofit", "docs", "media"],
    palette={"bg": "#F0EDE3", "surface": "#FAF8F2", "text": "#1F2419", "accent": "#5C6E3B", "muted": "#7A7A6E"},
    type={"display": "Newsreader", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="none — flat",
    motion_energy="calm",
    corner_radius="soft 6px",
    shadow_style="very soft, low-opacity",
    references=["nature.org", "slowfood.com", "treehugger.com"],
    rationale="Olive green is the peace color — used here for nonprofit and environmental work. Newsreader display + Inter body balances editorial and UI. Restrained palette and minimal shadows keep the focus on mission content.",
    anti_patterns=["bright primary colors", "drop shadows on imagery", "rounded pill buttons", "decorative motion"],
)

add(
    id="t032",
    name="Persian Rug Warm",
    voice="opulent, patterned, heritage",
    best_for=["ecommerce", "media", "portfolio"],
    palette={"bg": "#3B1F1A", "surface": "#4A2A22", "text": "#F0E5D2", "accent": "#C49B3C", "muted": "#A0836B"},
    type={"display": "Cormorant", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="subtle geometric pattern overlay",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="deep, warm, low-opacity",
    references=["the-saleroom.com", "nazmiyalantiquerugs.com", "novocustom.com"],
    rationale="Persian rugs teach restrained opulence: deep red ground, gold accent, dense pattern. Cormorant + Lora gives the antiquarian-catalog voice. Geometric pattern overlays (only on hero surfaces) reinforce the heritage reference without overwhelming.",
    anti_patterns=["bright primary colors", "rounded corners", "drop shadows on imagery", "modern sans-serif body"],
)

# ---------------------------------------------------------------------------
# 33-44: Cultural / Historical
# ---------------------------------------------------------------------------
add(
    id="t033",
    name="Art Deco Gold",
    voice="glamorous, geometric, 1925-Manhattan",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#0D0D0D", "surface": "#1A1A1A", "text": "#F5EBC6", "accent": "#D4AF37", "muted": "#9A8B6E"},
    type={"display": "Cormorant", "body": "Cormorant", "mono": "IBM Plex Mono"},
    texture="subtle geometric line patterns",
    motion_energy="cinematic",
    corner_radius="sharp 0px",
    shadow_style="deep, warm, low-opacity gold falloff",
    references=["theghosthotel.com", "chryslerbuilding.com", "theplaza.com"],
    rationale="Art Deco uses gold on black as a statement of intent. Cormorant throughout gives the engraved-marquee feel. Geometric line patterns (chevrons, sunbursts) as decoration. Motion is slow and cinematic — fades, not slides.",
    anti_patterns=["sans-serif display", "rounded corners", "pastel palette", "playful motion"],
)

add(
    id="t034",
    name="Memphis Playful",
    voice="exuberant, postmodern, rebellious",
    best_for=["marketing", "portfolio", "ecommerce"],
    palette={"bg": "#F5F5F0", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#FF4D8D", "muted": "#5C5C5C"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "Space Mono"},
    texture="scattered geometric shapes + dot patterns",
    motion_energy="energetic",
    corner_radius="mixed (0px shapes, 8px cards, pill buttons)",
    shadow_style="hard offset shadows in accent color",
    references=["memphis-milano.com", "sullivantwomey.com", "filson-cases.com"],
    rationale="Memphis Design (1981) was postmodern rebellion: clashing colors, geometric shapes, mismatched patterns. Bricolage display has the era's playfulness. Use sparingly — Memphis without restraint becomes kindergarten.",
    anti_patterns=["monochrome palette", "soft gradients", "rounded everything", "restrained motion"],
)

add(
    id="t035",
    name="Vaporwave",
    voice="nostalgic, surreal, late-90s digital",
    best_for=["portfolio", "personal", "marketing"],
    palette={"bg": "#1A0B2E", "surface": "#2D1450", "text": "#FDE2FF", "accent": "#FF71CE", "muted": "#9A8BB5"},
    type={"display": "Syne", "body": "Outfit", "mono": "Space Mono"},
    texture="grid horizon + marble texture overlay",
    motion_energy="energetic",
    corner_radius="mixed (sharp images, 4px cards)",
    shadow_style="neon glow shadows",
    references=["seancode.com/vaporwave", "134340.cc", "aesthetics.fandom.com"],
    rationale="Vaporwave is the late-90s digital aesthetic: deep purple, hot pink, cyan grid horizons, marble busts. Syne display has the era's stretched geometry. Use ironically or for genuinely retro-digital work — corporate vaporwave reads as pandering.",
    anti_patterns=["realistic photography", "restrained palette", "soft shadows", "sans-serif humanist body"],
)

add(
    id="t036",
    name="Y2K Cyber",
    voice="metallic, futuristic, turn-of-millennium",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#0A0E1A", "surface": "#131826", "text": "#D6E8FF", "accent": "#00E5FF", "muted": "#6A7A95"},
    type={"display": "Outfit", "body": "Inter", "mono": "Space Mono"},
    texture="chrome reflections + grid overlays",
    motion_energy="energetic",
    corner_radius="mixed (sharp cards, pill buttons)",
    shadow_style="neon glow + chrome highlights",
    references=["apple.com/quicktime", "spacejam.com", "geocities-archive"],
    rationale="Y2K aesthetic was optimism about technology: chrome, cyan, magenta, futuristic UI. Outfit display has the era's geometric confidence. Chrome reflections on key surfaces reinforce the metallic reference. Use only for genuinely retro-futurist work.",
    anti_patterns=["earthy palette", "rounded soft corners", "decorative serif display", "calm motion"],
)

add(
    id="t037",
    name="Cyberpunk Neon",
    voice="nocturnal, gritty, dystopian",
    best_for=["media", "portfolio", "marketing"],
    palette={"bg": "#05050A", "surface": "#0D0D18", "text": "#E0E0E8", "accent": "#FF2079", "muted": "#7A7A8C"},
    type={"display": "Unbounded", "body": "Inter", "mono": "JetBrains Mono"},
    texture="rain-soaked street reflections + scanlines",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="neon glow shadows (pink + cyan)",
    references=["cyberpunk.net", "rive.com", "philips-hue.com"],
    rationale="Cyberpunk is rain, neon, and broken UI. Deep black (not zinc), magenta-pink accent, occasional cyan secondary. Unbounded display has the corporate-dystopia weight. Scanlines and glow shadows carry the dystopian feel. Use only for genuinely cyberpunk work.",
    anti_patterns=["warm palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t038",
    name="Risograph Print",
    voice="tactile, limited-ink, indie-press",
    best_for=["portfolio", "media", "marketing"],
    palette={"bg": "#F4EFE2", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#1B3A6B", "muted": "#9A7A4F"},
    type={"display": "Anton", "body": "Work Sans", "mono": "Space Mono"},
    texture="visible risograph dot pattern + ink misalignment",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="none — overlay misalignment only",
    references=["hato-press.com", "tanandtompson.com", "mecoboriso.com"],
    rationale="Risograph printing uses 1-3 fluorescent inks with intentional misregistration. Blue ink + ochre overprint gives the indie-press palette. Anton display + Work Sans body mimics the era's screenprinted posters. Dot pattern texture (only on color areas) makes the metaphor literal.",
    anti_patterns=["CMYK gradients", "soft shadows", "rounded corners", "realistic photography"],
)

add(
    id="t039",
    name="Letterpress Workshop",
    voice="hand-set, ink-heavy, tactile",
    best_for=["portfolio", "media", "personal"],
    palette={"bg": "#EDE6D6", "surface": "#F4EFE2", "text": "#1A1614", "accent": "#6B2C2C", "muted": "#7A6E5A"},
    type={"display": "Playfair Display", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="heavy paper grain + ink bleed",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — ink-bleed only",
    references=["heavy planet press", "tinderpress.com", "boxcarpress.com"],
    rationale="Letterpress is ink-on-paper at human scale: deep impression, slight overprint, paper grain visible. Playfair + Lora gives the wood-type catalog voice. Deep red accent is printer's ink. Heavy grain (only on text backgrounds) makes the impression visible.",
    anti_patterns=["high-contrast shadows", "rounded corners", "geometric sans display", "decorative motion"],
)

add(
    id="t040",
    name="Woodblock Ukiyo-e",
    voice="traditional, layered, pictorial",
    best_for=["media", "portfolio", "marketing"],
    palette={"bg": "#E8D9B8", "surface": "#F2E5C7", "text": "#2B1810", "accent": "#B33A3A", "muted": "#7A6240"},
    type={"display": "Cormorant", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="visible wood grain + ink-line texture",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — flat layered illustration",
    references=["mfa.org/collections/ukiyo-e", "metmuseum.org/ukiyo-e", "ukiyoe.org"],
    rationale="Ukiyo-e woodblock prints teach layered color: cream paper, black ink lines, restrained reds and blues. Cormorant + Lora gives the antiquarian-catalog voice. Visible wood grain (only on hero surfaces) reinforces the print reference. Avoid photography — illustration only.",
    anti_patterns=["photographic imagery", "decorative gradients", "rounded corners", "neon accents"],
)

add(
    id="t041",
    name="Pop Art Bold",
    voice="punchy, mass-produced, ironic",
    best_for=["marketing", "portfolio", "media"],
    palette={"bg": "#FFEE00", "surface": "#FFFFFF", "text": "#0A0A0A", "accent": "#E63946", "muted": "#3D405B"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "Space Mono"},
    texture="visible halftone dots + thick black outlines",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard offset shadows in solid colors",
    references=["warhol.org", "lhsershgallery.com", "tate.org.uk/pop-art"],
    rationale="Pop Art is mass-media color at billboard scale: yellow, red, blue, thick outlines. Bricolage display + DM Sans body has the silkscreen-poster weight. Halftone imagery (not photography) carries the reference. Use only for genuinely playful brand work.",
    anti_patterns=["muted palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t042",
    name="Constructivist Red",
    voice="revolutionary, geometric, propaganda-loud",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#EAE2D0", "surface": "#F2EBD9", "text": "#1A1A1A", "accent": "#C1272D", "muted": "#3D3D3D"},
    type={"display": "Archivo Black", "body": "Archivo", "mono": "IBM Plex Mono"},
    texture="paper grain + visible diagonal grid",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="none — hard geometric blocks",
    references=["themorgan.org/constructivism", "tate.org.uk/constructivism", "moma.org/constructivism"],
    rationale="Russian Constructivism used red as structural element, not decoration. Archivo Black display has the propaganda-poster weight. Diagonal compositions, oversized numbers, and limited palette reinforce the reference. Use sparingly — overuse trivializes the history.",
    anti_patterns=["soft gradients", "rounded corners", "muted palette", "decorative motion"],
)

add(
    id="t043",
    name="Art Nouveau Flowing",
    voice="organic, decorative, botanical",
    best_for=["portfolio", "media", "marketing"],
    palette={"bg": "#F0E6D2", "surface": "#F7EFDC", "text": "#2B1F14", "accent": "#6B8E23", "muted": "#7A6A4F"},
    type={"display": "Cormorant", "body": "Cormorant", "mono": "IBM Plex Mono"},
    texture="flowing line illustrations + botanical motifs",
    motion_energy="calm",
    corner_radius="organic irregular (8-24px)",
    shadow_style="soft, warm, low-opacity",
    references=["muchafoundation.org", "tate.org.uk/art-nouveau", "victorianweb.org/artnouv"],
    rationale="Art Nouveau is the whiplash curve: botanical lines, asymmetry, peacock colors. Cormorant throughout gives the period-illustration feel. Flowing line illustrations (only as decoration, never as content) carry the reference. Organic corner radii reinforce the curve vocabulary.",
    anti_patterns=["geometric grids", "neon accents", "sharp corners", "decorative motion"],
)

add(
    id="t044",
    name="De Stijl",
    voice="geometric, primary, theoretical",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#F5F2EA", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#E63946", "muted": "#1D3557"},
    type={"display": "Archivo Black", "body": "Archivo", "mono": "IBM Plex Mono"},
    texture="none — pure flat geometric blocks",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="none — black grid lines",
    references=["thedesignmuseum.com", "moma.org/de-stijl", "tate.org.uk/de-stijl"],
    rationale="De Stijl (Mondrian, van Doesburg) used primary colors + black grid as universal visual language. Red accent + indigo muted + cream bg keeps the palette. Archivo Black display has the period-poster weight. Black grid lines (not shadows) carry structure.",
    anti_patterns=["soft gradients", "rounded corners", "decorative imagery", "asymmetric layouts"],
)

# ---------------------------------------------------------------------------
# 45-58: SaaS / Dev / Enterprise
# ---------------------------------------------------------------------------
add(
    id="t045",
    name="Dev Tool Dark",
    voice="engineer-first, dense, terminal-fluent",
    best_for=["saas", "docs", "dashboard"],
    palette={"bg": "#0D0F12", "surface": "#161A20", "text": "#E4E7EB", "accent": "#10B981", "muted": "#6B7785"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with subtle borders",
    motion_energy="measured",
    corner_radius="soft 6px",
    shadow_style="subtle 0 1px 2px rgba(0,0,0,0.3)",
    references=["linear.app", "vercel.com", "supabase.com"],
    rationale="Dev tools optimize for dense information and rapid scanning. Dark bg (not pure black) reduces eye strain for long sessions. Green accent (vs. AI-default violet) signals success and code output. Mono everywhere data appears; sans for UI chrome only.",
    anti_patterns=["light mode default", "vibrant gradients", "decorative motion", "rounded pill buttons"],
)

add(
    id="t046",
    name="Fintech Trust Blue",
    voice="credible, institutional, calm",
    best_for=["saas", "dashboard", "ecommerce"],
    palette={"bg": "#FFFFFF", "surface": "#F7F9FC", "text": "#0F1B2D", "accent": "#1E40AF", "muted": "#5A6B82"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="very subtle 0 1px 3px rgba(15,27,45,0.06)",
    references=["stripe.com", "mercury.com", "ramp.com"],
    rationale="Fintech needs institutional credibility without looking bank-stuffy. Deep navy accent (not the AI-default indigo) reads as established. Inter throughout maintains legibility at all sizes. Tabular numerals in mono for any monetary value. Motion only on confirmations.",
    anti_patterns=["neon accents", "playful motion", "rounded pill buttons", "decorative gradients"],
)

add(
    id="t047",
    name="Linear Product Dark",
    voice="fast, opinionated, keyboard-first",
    best_for=["saas", "dashboard", "docs"],
    palette={"bg": "#08090A", "surface": "#101113", "text": "#ECEDEE", "accent": "#5E6AD2", "muted": "#8A8F98"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with 1px borders",
    motion_energy="energetic",
    corner_radius="soft 6px",
    shadow_style="subtle 0 1px 2px rgba(0,0,0,0.4)",
    references=["linear.app", "raycast.com", "cron.com"],
    rationale="The Linear aesthetic is engineered density: near-black bg, refined indigo accent, 1px borders, dense layouts. Inter throughout for unified voice. Motion is fast (120ms) and precise — never decorative. Keyboard shortcuts are first-class UI.",
    anti_patterns=["slow easing curves", "rounded pill everything", "decorative gradients", "bright accent colors"],
)

add(
    id="t048",
    name="Vercel Mono Dark",
    voice="performance-first, minimal, terminal",
    best_for=["saas", "docs", "portfolio"],
    palette={"bg": "#000000", "surface": "#0A0A0A", "text": "#EDEDED", "accent": "#FFFFFF", "muted": "#737373"},
    type={"display": "Geist", "body": "Geist", "mono": "Geist Mono"},
    texture="none — flat",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="subtle 0 1px 2px rgba(255,255,255,0.04)",
    references=["vercel.com", "nextjs.org", "geist.com"],
    rationale="Vercel's aesthetic is mono on black: terminal confidence, zero decoration. Geist family throughout (sans + mono) gives unified voice. White-on-black with no accent color except in conversion states. Pure black bg only works with carefully calibrated text gray.",
    anti_patterns=["bright accent colors", "rounded corners", "decorative gradients", "soft shadows"],
)

add(
    id="t049",
    name="Stripe Modern",
    voice="polished, technical, gradient-aware",
    best_for=["saas", "marketing", "docs"],
    palette={"bg": "#FFFFFF", "surface": "#F6F9FC", "text": "#0A2540", "accent": "#635BFF", "muted": "#425466"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle gradient mesh on hero only",
    motion_energy="measured",
    corner_radius="soft 8px",
    shadow_style="soft 0 4px 12px rgba(15,27,45,0.06)",
    references=["stripe.com", "www.stripe.dev", "stripe.press"],
    rationale="Stripe's aesthetic is technical polish: navy text, soft surfaces, restrained gradients. Indigo accent (Stripe's brand) is acceptable here as the canonical use. Inter throughout for unified voice. Gradient mesh only on hero — never on cards or backgrounds.",
    anti_patterns=["dark mode default", "vibrant neon accents", "decorative motion", "rounded pill buttons"],
)

add(
    id="t050",
    name="Notion Neutral",
    voice="document-first, calm, emoji-friendly",
    best_for=["docs", "saas", "personal"],
    palette={"bg": "#FFFFFF", "surface": "#F7F6F3", "text": "#1F1F1F", "accent": "#2383E2", "muted": "#787774"},
    type={"display": "Inter", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="none — flat with subtle paper tone",
    motion_energy="calm",
    corner_radius="soft 4px",
    shadow_style="subtle 0 1px 2px rgba(0,0,0,0.04)",
    references=["notion.so", "coda.io", "craft.do"],
    rationale="Notion's aesthetic treats the web page as a document, not an app. Warm off-white surfaces (not pure gray) reduce eye strain. Inter throughout with mono for code blocks. Restrained blue accent for links and selection states only. Motion only on hover.",
    anti_patterns=["dark mode default", "vibrant accent colors", "rounded pill buttons", "decorative motion"],
)

add(
    id="t051",
    name="Clinical Healthcare",
    voice="trustworthy, legible, patient-first",
    best_for=["saas", "docs", "dashboard"],
    palette={"bg": "#FFFFFF", "surface": "#F4F8FA", "text": "#0F1B2D", "accent": "#0E7C7B", "muted": "#5A6B82"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — pure flat",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="very subtle 0 1px 2px rgba(15,27,45,0.04)",
    references=["verity.com", "doximity.com", "simplepractice.com"],
    rationale="Healthcare design demands maximum legibility and minimum decoration. Teal accent signals health without the cliché medical blue. Inter throughout for unified voice. Strict 4.5:1 contrast minimum on all text. Avoid motion that could trigger vestibular issues.",
    anti_patterns=["dark mode default", "decorative motion", "rounded pill everything", "vibrant gradients"],
)

add(
    id="t052",
    name="Legal Gravitas",
    voice="authoritative, conservative, trustworthy",
    best_for=["saas", "docs", "nonprofit"],
    palette={"bg": "#FBFAF7", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#7A1C1C", "muted": "#5C5C5C"},
    type={"display": "Source Serif 4", "body": "Source Serif 4", "mono": "IBM Plex Mono"},
    texture="none — flat",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — rules only",
    references=["scholar.google.com", "courtlistener.com", "law.cornell.edu"],
    rationale="Legal design is intentionally conservative to signal authority. Source Serif throughout (display + body) gives the case-reporter voice. Deep burgundy accent for citation markers. No decoration, no shadows, no rounded corners — every element is structural.",
    anti_patterns=["modern sans-serif body", "rounded corners", "decorative motion", "bright accent colors"],
)

add(
    id="t053",
    name="E-commerce Crisp",
    voice="shoppable, clean, conversion-aware",
    best_for=["ecommerce", "marketing", "saas"],
    palette={"bg": "#FFFFFF", "surface": "#F7F7F5", "text": "#1A1A1A", "accent": "#C8102E", "muted": "#6B6B6B"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with crisp product photography",
    motion_energy="measured",
    corner_radius="soft 4px",
    shadow_style="soft 0 2px 8px rgba(0,0,0,0.06)",
    references=["everlane.com", "outdoorvoices.com", "allbirds.com"],
    rationale="E-commerce needs clean product photography to dominate. Inter throughout for unified voice. Red accent for sale, urgency, and CTA only — never decorative. Soft 4px corners feel modern without being playful. Motion only on cart and confirmation states.",
    anti_patterns=["dark mode default", "vibrant gradient backgrounds", "rounded pill everything", "decorative motion"],
)

add(
    id="t054",
    name="Marketing Bold Gradient",
    voice="energetic, modern, conversion-driven",
    best_for=["marketing", "saas", "media"],
    palette={"bg": "#0A0A0B", "surface": "#18181B", "text": "#FAFAFA", "accent": "#A855F7", "muted": "#A1A1AA"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle gradient mesh + grain",
    motion_energy="energetic",
    corner_radius="soft 12px",
    shadow_style="glow shadows on CTAs",
    references=["framer.com", "webflow.com", "vizow.com"],
    rationale="Marketing sites need energy and conversion focus. Dark bg with gradient-mesh hero creates the modern SaaS look. Purple accent (intentional, not the AI default) drives CTA clicks. Inter throughout for unified voice. Motion on scroll reveals and CTAs.",
    anti_patterns=["light mode default", "decorative serif display", "sharp 0px corners", "no motion"],
)

add(
    id="t055",
    name="Documentation Calm",
    voice="helpful, hierarchical, scannable",
    best_for=["docs", "saas", "nonprofit"],
    palette={"bg": "#FFFFFF", "surface": "#F8F9FA", "text": "#1A1A1A", "accent": "#2563EB", "muted": "#6B7280"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat",
    motion_energy="calm",
    corner_radius="soft 6px",
    shadow_style="none — borders only",
    references=["developer.mozilla.org", "docs.github.com", "stripe.com/docs"],
    rationale="Documentation needs maximum scannability. Inter throughout for unified voice at all sizes. Blue accent for links and code references only. Mono for code blocks. Generous whitespace, strict heading hierarchy. No decorative motion — readers need stillness.",
    anti_patterns=["decorative motion", "vibrant gradients", "rounded pill everything", "decorative serif display"],
)

add(
    id="t056",
    name="Dashboard Dense",
    voice="information-rich, controlled, operational",
    best_for=["dashboard", "saas"],
    palette={"bg": "#F8F9FA", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#2563EB", "muted": "#6B7280"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat",
    motion_energy="measured",
    corner_radius="soft 6px",
    shadow_style="very subtle 0 1px 2px rgba(0,0,0,0.04)",
    references=["vercel.com/dashboard", "linear.app", "datadog.com"],
    rationale="Dashboards optimize for information density and operational clarity. Light bg with white surfaces creates depth without shadows. Inter throughout with tabular numerals for all metrics. Blue accent for primary actions only. Motion only on data updates.",
    anti_patterns=["dark mode default", "vibrant gradients", "rounded pill buttons", "decorative motion"],
)

add(
    id="t057",
    name="Onboarding Friendly",
    voice="approachable, encouraging, progress-aware",
    best_for=["saas", "marketing"],
    palette={"bg": "#FFFFFF", "surface": "#F7F4FF", "text": "#1A1A2E", "accent": "#6D28D9", "muted": "#6B7280"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "JetBrains Mono"},
    texture="subtle gradient overlays on hero",
    motion_energy="measured",
    corner_radius="soft 12px",
    shadow_style="soft 0 4px 12px rgba(109,40,217,0.08)",
    references=["linear.app/onboarding", "notion.so/help", "cron.com"],
    rationale="Onboarding needs warmth without losing professionalism. Bricolage display + DM Sans body feels approachable. Lavender accent (intentional, not default) guides progress. Generous corners (12px) feel friendly. Motion only on progress transitions.",
    anti_patterns=["sharp 0px corners", "decorative gradients everywhere", "high-contrast shadows", "playful motion"],
)

add(
    id="t058",
    name="B2B Enterprise Solid",
    voice="credible, institutional, no-nonsense",
    best_for=["saas", "marketing", "dashboard"],
    palette={"bg": "#FFFFFF", "surface": "#F4F6F8", "text": "#0F1B2D", "accent": "#1E3A8A", "muted": "#475569"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat",
    motion_energy="measured",
    corner_radius="soft 4px",
    shadow_style="subtle 0 1px 3px rgba(15,27,45,0.06)",
    references=["workday.com", "salesforce.com", "servicenow.com"],
    rationale="Enterprise B2B needs to feel established and risk-free. Deep navy accent (not bright blue) reads as institutional. Inter throughout for unified voice. Strict 4px corners and subtle shadows feel professional without being playful. Motion only on confirmations.",
    anti_patterns=["vibrant gradient backgrounds", "rounded pill everything", "decorative motion", "playful color palette"],
)

# ---------------------------------------------------------------------------
# 59-68: Dark / Mood
# ---------------------------------------------------------------------------
add(
    id="t059",
    name="Midnight Indigo",
    voice="calm, deep, contemplative",
    best_for=["saas", "media", "personal"],
    palette={"bg": "#0B0F1E", "surface": "#131933", "text": "#E2E8F0", "accent": "#818CF8", "muted": "#7A85A8"},
    type={"display": "Fraunces", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle radial glow",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="soft, low-opacity, blue-tinted",
    references=["refactoringui.com", "tailwindcss.com", "updraftplus.com"],
    rationale="Midnight indigo uses deep blue-blacks (not zinc) for warmth. Soft accent indigo for interactive elements. Fraunces display + Inter body is the modern editorial combo. Subtle radial glow (only on hero) creates depth without gradient abuse.",
    anti_patterns=["pure black bg", "neon accents", "sharp 0px corners", "decorative motion everywhere"],
)

add(
    id="t060",
    name="Carbon Performance",
    voice="technical, fast, motorsport-precise",
    best_for=["saas", "media", "dashboard"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#EDEDED", "accent": "#FF3B00", "muted": "#7A7A7A"},
    type={"display": "Space Grotesk", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle carbon-fiber weave on hero only",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard 2px 2px 0 #FF3B00",
    references=["mclaren.com", "polestar.com", "tesla.com"],
    rationale="Carbon-performance aesthetic treats the screen like a HUD: dark, fast, precise. Orange accent (not red) reads as motorsport, not warning. Space Grotesk display has the engineering-poster weight. Hard shadows on hover reinforce the technical vocabulary.",
    anti_patterns=["soft pastel palette", "rounded corners", "decorative motion", "decorative serif display"],
)

add(
    id="t061",
    name="Terminal Green",
    voice="hacker, retro-computing, monochrome",
    best_for=["portfolio", "personal", "docs"],
    palette={"bg": "#0A0E0A", "surface": "#101510", "text": "#A8E6A8", "accent": "#3DDC84", "muted": "#6A8A6A"},
    type={"display": "JetBrains Mono", "body": "JetBrains Mono", "mono": "JetBrains Mono"},
    texture="subtle scanlines + glow",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="neon glow on accent text",
    references=["jvns.ca", "drewdevault.com", "akkartik.name"],
    rationale="Terminal aesthetic pays homage to phosphor-green CRT monitors. JetBrains Mono throughout (display + body) reinforces the metaphor. Restrained green palette (not pure neon) reduces eye strain. Scanlines and glow on accent only — never on body text.",
    anti_patterns=["sans-serif body", "rounded corners", "decorative gradients", "bright accent colors"],
)

add(
    id="t062",
    name="Cinematic Letterbox",
    voice="cinematic, austere, photographic",
    best_for=["media", "portfolio", "agency"],
    palette={"bg": "#000000", "surface": "#0A0A0A", "text": "#EDEDED", "accent": "#D4AF37", "muted": "#7A7A7A"},
    type={"display": "DM Serif Display", "body": "Inter", "mono": "JetBrains Mono"},
    texture="film grain + letterbox bars",
    motion_energy="cinematic",
    corner_radius="sharp 0px",
    shadow_style="none — flat with grain",
    references=["a24.com", "mubi.com", "criterion.com"],
    rationale="Cinematic letterbox uses fixed top/bottom bars (8vh each) to evoke film aspect ratio. Pure black bg + film grain (5%) carries the cinema reference. DM Serif Display gives title-card weight. Gold accent reserved for opening credits only.",
    anti_patterns=["rounded corners", "bright accent colors", "decorative motion everywhere", "soft shadows"],
)

add(
    id="t063",
    name="Photography Black",
    voice="minimal, gallery-quiet, image-first",
    best_for=["portfolio", "media", "agency"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#EDEDED", "accent": "#FFFFFF", "muted": "#7A7A7A"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with photography as primary surface",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — borders only",
    references=["magnumphotos.com", "mo.photography", "criterion.com"],
    rationale="Photography portfolios need the page to disappear and let images dominate. Pure black bg + zero chrome + Inter throughout = gallery wall. White accent for hover states only. No shadows on images — borders separate frames. Motion only on transitions.",
    anti_patterns=["decorative gradients", "rounded corners", "drop shadows on imagery", "decorative serif display"],
)

add(
    id="t064",
    name="Music Streaming Dark",
    voice="rhythmic, immersive, night-mode",
    best_for=["media", "saas", "dashboard"],
    palette={"bg": "#0E0E0F", "surface": "#18181B", "text": "#EDEDED", "accent": "#1DB954", "muted": "#A1A1AA"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with subtle blur on player",
    motion_energy="measured",
    corner_radius="soft 8px",
    shadow_style="soft 0 4px 12px rgba(0,0,0,0.4)",
    references=["spotify.com", "tidal.com", "soundcloud.com"],
    rationale="Music apps need darkness to make album art pop. Green accent (Spotify-style) is acceptable here as the canonical use. Inter throughout for unified voice. Soft 8px corners feel modern without being playful. Motion only on play/pause transitions.",
    anti_patterns=["light mode default", "rounded pill everything", "decorative gradients everywhere", "decorative serif display"],
)

add(
    id="t065",
    name="Game UI Dark",
    voice="energetic, immersive, HUD-styled",
    best_for=["media", "portfolio", "marketing"],
    palette={"bg": "#0A0A14", "surface": "#13131F", "text": "#EDEDED", "accent": "#FFC53D", "muted": "#6A6A82"},
    type={"display": "Outfit", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle scanlines + corner brackets",
    motion_energy="energetic",
    corner_radius="mixed (sharp panels, pill buttons)",
    shadow_style="glow shadows on accent",
    references=["playstation.com", "xbox.com", "riotgames.com"],
    rationale="Game UI treats the screen as a HUD: sharp panels, glow accents, corner brackets. Outfit display has the futuristic-game confidence. Yellow-gold accent (not neon green) reads as game currency, not warning. Motion is fast and snappy — never slow.",
    anti_patterns=["soft pastel palette", "rounded everything", "decorative serif display", "slow easing curves"],
)

add(
    id="t066",
    name="Crypto Neon",
    voice="speculative, futuristic, web3-coded",
    best_for=["saas", "marketing", "portfolio"],
    palette={"bg": "#05050A", "surface": "#0D0D18", "text": "#E0E0E8", "accent": "#A855F7", "muted": "#7A7A8C"},
    type={"display": "Unbounded", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle gradient mesh + grain",
    motion_energy="energetic",
    corner_radius="mixed (sharp panels, pill buttons)",
    shadow_style="glow shadows on accent",
    references=["coinbase.com", "opensea.io", "etherscan.io"],
    rationale="Crypto design signals futurism without substance abuse. Deep black (not zinc) + purple accent (vs. AI-default indigo) + glow shadows. Unbounded display has the corporate-dystopia weight. Gradient mesh only on hero — never on cards.",
    anti_patterns=["light mode default", "rounded pill everything", "decorative serif display", "soft pastel palette"],
)

add(
    id="t067",
    name="Synthwave Sunset",
    voice="retro-futuristic, dreamy, neon-drenched",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#1A0B2E", "surface": "#2D1450", "text": "#FDE2FF", "accent": "#FF6B9D", "muted": "#9A8BB5"},
    type={"display": "Syne", "body": "Outfit", "mono": "Space Mono"},
    texture="grid horizon + sunset gradient",
    motion_energy="energetic",
    corner_radius="mixed (sharp panels, pill buttons)",
    shadow_style="neon glow shadows (pink + cyan)",
    references=["synthwave.com", "outrun aesthetic", "newretrowave.com"],
    rationale="Synthwave is sun-drenched neon nostalgia: deep purple, hot pink, cyan grid horizons. Syne display has the era's stretched geometry. Sunset gradient (only on hero) carries the reference. Use sparingly — overuse becomes pastiche.",
    anti_patterns=["earthy palette", "soft shadows", "rounded soft corners", "decorative serif display"],
)

add(
    id="t068",
    name="Forest Night",
    voice="earthy, mysterious, deep-wood",
    best_for=["media", "portfolio", "nonprofit"],
    palette={"bg": "#0A1410", "surface": "#13201A", "text": "#D9E8DC", "accent": "#9CCC65", "muted": "#7A8A7A"},
    type={"display": "Fraunces", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle organic noise",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="soft, low-opacity, green-tinted",
    references=["nature.org", "wwf.org", "patagonia.com"],
    rationale="Forest night uses deep green-blacks (not zinc) for organic warmth. Light green accent (not neon) for interactive elements. Fraunces display + Inter body is the editorial-nature combo. Subtle organic noise (only on hero) suggests dappled light.",
    anti_patterns=["pure black bg", "neon accents", "sharp 0px corners", "decorative motion everywhere"],
)

# ---------------------------------------------------------------------------
# 69-78: Light / Airy
# ---------------------------------------------------------------------------
add(
    id="t069",
    name="Cloud Soft",
    voice="gentle, friendly, accessible",
    best_for=["saas", "marketing", "personal"],
    palette={"bg": "#F8FAFC", "surface": "#FFFFFF", "text": "#1E293B", "accent": "#0EA5E9", "muted": "#64748B"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — pure flat with soft gradient overlays",
    motion_energy="calm",
    corner_radius="soft 12px",
    shadow_style="soft 0 4px 12px rgba(15,23,42,0.05)",
    references=["linear.app", "cron.com", "raycast.com"],
    rationale="Cloud soft uses airy backgrounds and gentle shadows to feel approachable. Sky-blue accent (vs. AI-default indigo) reads as sky, not corporate. Inter throughout for unified voice. Generous 12px corners feel modern without being playful. Motion only on hover.",
    anti_patterns=["dark mode default", "vibrant gradient backgrounds", "sharp 0px corners", "decorative motion"],
)

add(
    id="t070",
    name="Pastel Whisper",
    voice="soft, dreamy, gentle",
    best_for=["personal", "media", "ecommerce"],
    palette={"bg": "#FBF5F7", "surface": "#FFFFFF", "text": "#3D2B2F", "accent": "#D4A5C9", "muted": "#8A7A82"},
    type={"display": "Fraunces", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="subtle gradient overlays",
    motion_energy="calm",
    corner_radius="soft 16px",
    shadow_style="soft, warm, low-opacity",
    references=["joandjudy.com", "sawsasee.com", "fawn-shop.com"],
    rationale="Pastel whisper uses cream-pink bg + dusty-rose accent for soft, dreamy feel. Fraunces display + Inter body is the editorial combo. Generous 16px corners feel approachable. Motion only on hover — never on scroll.",
    anti_patterns=["dark mode default", "vibrant neon accents", "sharp 0px corners", "high-contrast shadows"],
)

add(
    id="t071",
    name="Spring Garden",
    voice="fresh, optimistic, botanical",
    best_for=["ecommerce", "marketing", "media"],
    palette={"bg": "#F4F8F1", "surface": "#FFFFFF", "text": "#1F2A1A", "accent": "#6F8F4A", "muted": "#7A8A6E"},
    type={"display": "Fraunces", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="subtle botanical illustration overlay",
    motion_energy="calm",
    corner_radius="soft 12px",
    shadow_style="soft, low-opacity, green-tinted",
    references=["floretflowers.com", "thesill.com", "burpee.com"],
    rationale="Spring garden uses pale green bg + leaf-green accent for botanical freshness. Fraunces display + Inter body is the editorial combo. Botanical illustrations (only as decoration) reinforce the reference. Motion only on hover.",
    anti_patterns=["dark mode default", "neon accent colors", "sharp 0px corners", "high-contrast shadows"],
)

add(
    id="t072",
    name="Bakery Warm",
    voice="artisanal, hand-made, comforting",
    best_for=["ecommerce", "marketing", "personal"],
    palette={"bg": "#F5EAD2", "surface": "#FAF1DA", "text": "#3A2718", "accent": "#B65A3C", "muted": "#8A6F52"},
    type={"display": "Fraunces", "body": "DM Sans", "mono": "IBM Plex Mono"},
    texture="subtle paper grain",
    motion_energy="calm",
    corner_radius="soft 12px",
    shadow_style="soft, warm, low-opacity",
    references=["tartinebakery.com", "zachysbakery.com", "milkbarstore.com"],
    rationale="Bakery aesthetic uses wheat-cream bg + terracotta accent for warmth. Fraunces display + DM Sans body feels hand-painted. Paper grain (only on backgrounds) reinforces the artisanal reference. Motion only on hover.",
    anti_patterns=["cool blue accents", "pure white bg", "geometric sans display", "tight grid layouts"],
)

add(
    id="t073",
    name="Coffee Shop Muted",
    voice="cozy, neighborhood, slow",
    best_for=["ecommerce", "personal", "media"],
    palette={"bg": "#EFE5D5", "surface": "#F5EDDB", "text": "#2B1F14", "accent": "#6B3410", "muted": "#7A6A4F"},
    type={"display": "Fraunces", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="subtle paper grain + coffee ring overlay",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="soft, warm, low-opacity",
    references=["bluebottlecoffee.com", "stumptowncoffee.com", "onyxcoffeelab.com"],
    rationale="Coffee shop aesthetic uses coffee-cream bg + walnut-brown accent for warmth. Fraunces display + Inter body is the editorial combo. Paper grain (only on backgrounds) reinforces the artisanal reference. Motion only on hover.",
    anti_patterns=["cool blue accents", "pure white bg", "geometric sans display", "tight grid layouts"],
)

add(
    id="t074",
    name="Beach Holiday",
    voice="relaxed, sun-bleached, vacation",
    best_for=["ecommerce", "marketing", "media"],
    palette={"bg": "#F4F1EA", "surface": "#FFFFFF", "text": "#1F2B30", "accent": "#0E7C7B", "muted": "#7A8A8C"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "IBM Plex Mono"},
    texture="subtle paper grain",
    motion_energy="calm",
    corner_radius="soft 16px",
    shadow_style="soft, low-opacity, blue-tinted",
    references=["outsurf.com", "patagonia.com", "roxy.com"],
    rationale="Beach holiday uses sand-cream bg + sea-teal accent for relaxed feel. Bricolage display + DM Sans body has the playful energy without being childish. Generous 16px corners feel approachable. Motion only on hover — never on scroll.",
    anti_patterns=["dark mode default", "neon accent colors", "sharp 0px corners", "high-contrast shadows"],
)

add(
    id="t075",
    name="Children's Book",
    voice="playful, warm, illustrated",
    best_for=["ecommerce", "marketing", "media"],
    palette={"bg": "#FFF8E7", "surface": "#FFFFFF", "text": "#2B1F14", "accent": "#E63946", "muted": "#5C5C5C"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "Space Mono"},
    texture="visible hand-drawn illustrations",
    motion_energy="energetic",
    corner_radius="mixed (0px illustrations, 12px cards)",
    shadow_style="hard offset shadows in accent color",
    references=["lovevery.com", "lottiefiles.com", "tinybop.com"],
    rationale="Children's book aesthetic uses warm cream bg + bright primary accents for playful feel. Bricolage display + DM Sans body has the picture-book energy. Hand-drawn illustrations (only as decoration) reinforce the reference. Motion is playful — bounce easing allowed.",
    anti_patterns=["monochrome palette", "soft gradients", "rounded everything", "restrained motion"],
)

add(
    id="t076",
    name="Watercolor Wash",
    voice="artistic, flowing, hand-painted",
    best_for=["portfolio", "media", "personal"],
    palette={"bg": "#FBF7F0", "surface": "#FFFFFF", "text": "#2B1F2A", "accent": "#7A4A8C", "muted": "#7A7A82"},
    type={"display": "Cormorant", "body": "Lora", "mono": "IBM Plex Mono"},
    texture="visible watercolor washes on hero",
    motion_energy="calm",
    corner_radius="organic irregular (8-24px)",
    shadow_style="soft, low-opacity, purple-tinted",
    references=["saatchiart.com", "etsy.com/art", "saatchi.com"],
    rationale="Watercolor aesthetic uses cream bg + soft purple accent for artistic feel. Cormorant display + Lora body is the painterly combo. Watercolor washes (only on hero surfaces) reinforce the reference. Organic corner radii reinforce the hand-painted feel.",
    anti_patterns=["geometric grids", "neon accents", "sharp corners", "decorative motion everywhere"],
)

add(
    id="t077",
    name="Stationery Store",
    voice="crisp, paper-loving, organized",
    best_for=["ecommerce", "portfolio", "personal"],
    palette={"bg": "#F8F6F0", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#1D3557", "muted": "#6B6B6B"},
    type={"display": "Fraunces", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="subtle paper grain",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — borders and rules only",
    references=["paperchase.com", "muji.us", "gouletpens.com"],
    rationale="Stationery aesthetic treats the page as a paper catalog: cream bg, sharp corners, ruled separators. Fraunces display + Inter body is the editorial combo. Navy accent for category markers. Paper grain (only on backgrounds) reinforces the reference.",
    anti_patterns=["dark mode default", "rounded corners", "decorative gradients", "high-contrast shadows"],
)

add(
    id="t078",
    name="Wedding Suite",
    voice="elegant, romantic, hand-lettered",
    best_for=["personal", "media", "marketing"],
    palette={"bg": "#FAF6F0", "surface": "#FFFFFF", "text": "#2B1F2A", "accent": "#A8324A", "muted": "#7A6A6E"},
    type={"display": "Cormorant", "body": "Cormorant", "mono": "IBM Plex Mono"},
    texture="subtle paper grain + gold foil accents",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="soft, warm, low-opacity",
    references=["magnoliabloom.com", "weddingpaperdivas.com", "zazzle.com/wedding"],
    rationale="Wedding suite uses cream bg + burgundy accent + gold foil for elegant feel. Cormorant throughout (display + body) gives the engraved-invitation voice. Sharp corners (not rounded) feel formal. Gold foil (only on small accents) reinforces the reference.",
    anti_patterns=["dark mode default", "rounded corners", "decorative gradients everywhere", "playful motion"],
)

# ---------------------------------------------------------------------------
# 79-90: Bold / Expressive
# ---------------------------------------------------------------------------
add(
    id="t079",
    name="Sports Energy",
    voice="dynamic, competitive, high-contrast",
    best_for=["marketing", "media", "portfolio"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#FFFFFF", "accent": "#FF5C00", "muted": "#7A7A7A"},
    type={"display": "Anton", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with high-contrast photography",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="none — bold borders and rules",
    references=["nike.com", "underarmour.com", "espys.espn.com"],
    rationale="Sports energy uses pure black + bright orange + condensed type for high-impact feel. Anton display has the scoreboard-stretch weight. Inter body keeps UI legible. Motion is fast and decisive — never slow.",
    anti_patterns=["pastel palette", "rounded soft corners", "decorative serif display", "slow easing curves"],
)

add(
    id="t080",
    name="Festival Loud",
    voice="exuberant, layered, summer-music",
    best_for=["marketing", "media", "portfolio"],
    palette={"bg": "#0A0A14", "surface": "#13131F", "text": "#FDE2FF", "accent": "#FF2079", "muted": "#9A8BB5"},
    type={"display": "Unbounded", "body": "Inter", "mono": "Space Mono"},
    texture="layered geometric shapes + grain",
    motion_energy="energetic",
    corner_radius="mixed (sharp panels, pill buttons)",
    shadow_style="glow shadows on accent",
    references=["coachella.com", "tomorrowland.com", "glastonburyfestivals.co.uk"],
    rationale="Festival loud uses dark bg + hot pink + geometric overlays for summer-music feel. Unbounded display has the festival-poster weight. Glow shadows on accent reinforce the night-concert reference. Motion is energetic — never calm.",
    anti_patterns=["earthy palette", "soft shadows", "rounded soft corners", "decorative serif display"],
)

add(
    id="t081",
    name="Streetwear Drop",
    voice="hype, limited, no-frills",
    best_for=["ecommerce", "marketing", "portfolio"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#FFFFFF", "accent": "#FFFF00", "muted": "#7A7A7A"},
    type={"display": "Anton", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with raw product photography",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard 4px 4px 0 #FFFF00",
    references=["supremenewyork.com", "stussy.com", "kith.com"],
    rationale="Streetwear drop uses pure black + acid yellow + condensed type for hype feel. Anton display has the stencil-poster weight. Hard yellow shadows on hover reinforce the street-tag reference. Motion is fast — countdown-driven.",
    anti_patterns=["pastel palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t082",
    name="Sneaker Culture",
    voice="athletic, collector, drop-culture",
    best_for=["ecommerce", "marketing", "portfolio"],
    palette={"bg": "#F4F4F4", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#FF3B00", "muted": "#6B6B6B"},
    type={"display": "Bricolage Grotesque", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with crisp product photography",
    motion_energy="energetic",
    corner_radius="soft 4px",
    shadow_style="soft 0 4px 16px rgba(255,59,0,0.08)",
    references=["nike.com/snkrs", "footlocker.com", "goat.com"],
    rationale="Sneaker culture uses light bg + bright orange + bold type for athletic feel. Bricolage display has the energy without being childish. Crisp product photography dominates. Motion is fast — drop countdowns drive the rhythm.",
    anti_patterns=["dark mode default", "decorative serif display", "rounded pill everything", "decorative motion everywhere"],
)

add(
    id="t083",
    name="Skate Punk",
    voice="rebellious, hand-cut, photocopied",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#FFFF00", "surface": "#FFFFFF", "text": "#0A0A0A", "accent": "#FF2079", "muted": "#5C5C5C"},
    type={"display": "Anton", "body": "Work Sans", "mono": "Space Mono"},
    texture="xerox noise + visible halftone",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard offset 6px 6px #000",
    references=["thrashermagazine.com", "transworldskateboarding.com", "vice.com/skate"],
    rationale="Skate punk uses yellow bg + black hard shadows + mismatched type for photocopied feel. Anton display has the band-poster weight. Halftone imagery (not photography) carries the reference. Motion is fast and rough — never smooth.",
    anti_patterns=["gentle gradients", "soft shadows", "rounded corners", "considered spacing"],
)

add(
    id="t084",
    name="Comic Book Halftone",
    voice="punchy, illustrated, four-color",
    best_for=["marketing", "media", "portfolio"],
    palette={"bg": "#FFF8E1", "surface": "#FFFFFF", "text": "#0A0A0A", "accent": "#E63946", "muted": "#3D405B"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "Space Mono"},
    texture="visible halftone dots + thick black outlines",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard offset shadows in solid colors",
    references=["marvel.com", "dccomics.com", "imagecomics.com"],
    rationale="Comic book halftone uses cream bg + primary colors + thick outlines for four-color feel. Bricolage display has the comic-title weight. Halftone imagery (not photography) carries the reference. Hard offset shadows reinforce the inky reference.",
    anti_patterns=["muted palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t085",
    name="Graffiti Urban",
    voice="street, raw, layered",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#FFFFFF", "accent": "#FF2079", "muted": "#7A7A7A"},
    type={"display": "Unbounded", "body": "Inter", "mono": "Space Mono"},
    texture="layered spray-paint texture + tags",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard spray-glow shadows",
    references=["instagram.com/streetart", "woostercollective.com", "1amsf.com"],
    rationale="Graffiti urban uses dark bg + neon pink + layered texture for street feel. Unbounded display has the marker-tag weight. Spray-paint texture (only on hero surfaces) reinforces the reference. Motion is fast — never smooth.",
    anti_patterns=["pastel palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t086",
    name="Retro Arcade",
    voice="8-bit, playful, late-70s-arcade",
    best_for=["marketing", "portfolio", "media"],
    palette={"bg": "#0A0A14", "surface": "#13131F", "text": "#FDE2FF", "accent": "#FFC53D", "muted": "#9A8BB5"},
    type={"display": "Press Start 2P", "body": "Inter", "mono": "Press Start 2P"},
    texture="scanlines + pixelated imagery",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard pixel shadows",
    references=["80sarcadegames.com", "nintendo.com", "arcade-museum.com"],
    rationale="Retro arcade uses dark bg + 8-bit type + scanlines for late-70s feel. Press Start 2P throughout (display + mono) reinforces the reference. Pixelated imagery (not photography) carries the reference. Motion is stepped — never smooth.",
    anti_patterns=["photographic imagery", "decorative gradients", "rounded corners", "decorative serif display"],
)

add(
    id="t087",
    name="Disco Glam",
    voice="glamorous, glittery, 1977-Manhattan",
    best_for=["marketing", "media", "portfolio"],
    palette={"bg": "#0D0D0D", "surface": "#1A1A1A", "text": "#F5EBC6", "accent": "#D4AF37", "muted": "#9A8B6E"},
    type={"display": "Syne", "body": "Inter", "mono": "Space Mono"},
    texture="disco-ball shimmer + geometric overlays",
    motion_energy="energetic",
    corner_radius="mixed (sharp panels, pill buttons)",
    shadow_style="glow shadows on accent",
    references=["studio54.com", "thebeegees.com", "disco-museum.com"],
    rationale="Disco glam uses black + gold + shimmer for 1977 feel. Syne display has the era's stretched geometry. Disco-ball shimmer (only on hero surfaces) reinforces the reference. Motion is rhythmic — never slow.",
    anti_patterns=["earthy palette", "soft shadows", "rounded soft corners", "decorative serif display"],
)

add(
    id="t088",
    name="Motorcycle Chrome",
    voice="industrial, masculine, american-made",
    best_for=["portfolio", "ecommerce", "marketing"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#EDEDED", "accent": "#C49B3C", "muted": "#7A7A7A"},
    type={"display": "Anton", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle chrome reflections + grain",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="hard offset shadows in accent color",
    references=["harley-davidson.com", "indianmotorcycle.com", "triumphmotorcycles.com"],
    rationale="Motorcycle chrome uses black + antique gold + condensed type for industrial feel. Anton display has the engine-badge weight. Chrome reflections (only on key surfaces) reinforce the reference. Motion is mechanical — never decorative.",
    anti_patterns=["pastel palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t089",
    name="Boxing Gym",
    voice="physical, no-frills, sweat-equity",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#FFFFFF", "accent": "#DC2626", "muted": "#7A7A7A"},
    type={"display": "Anton", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — flat with high-contrast photography",
    motion_energy="energetic",
    corner_radius="sharp 0px",
    shadow_style="hard offset shadows in accent color",
    references=["titleboxing.com", "ringside.com", "everlast.com"],
    rationale="Boxing gym uses pure black + bright red + condensed type for physical feel. Anton display has the gym-banner weight. High-contrast photography (not decoration) carries the reference. Motion is fast — never slow.",
    anti_patterns=["pastel palette", "soft shadows", "rounded corners", "decorative serif display"],
)

add(
    id="t090",
    name="Tattoo Studio",
    voice="artisanal, dark, hand-drawn",
    best_for=["portfolio", "marketing", "media"],
    palette={"bg": "#0A0A0A", "surface": "#141414", "text": "#EDEDED", "accent": "#B33A3A", "muted": "#7A7A7A"},
    type={"display": "Unbounded", "body": "Inter", "mono": "Space Mono"},
    texture="subtle ink-texture overlay",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="hard offset shadows in accent color",
    references=["bangbangforever.com", "memorialtattoo.com", "threechtattoo.com"],
    rationale="Tattoo studio uses dark bg + deep red + hand-drawn type for artisanal feel. Unbounded display has the tattoo-flash weight. Ink-texture overlay (only on hero surfaces) reinforces the reference. Motion is mechanical — never decorative.",
    anti_patterns=["pastel palette", "soft shadows", "rounded corners", "decorative serif display"],
)

# ---------------------------------------------------------------------------
# 91-100: Specialized
# ---------------------------------------------------------------------------
add(
    id="t091",
    name="Nonprofit Human",
    voice="warm, mission-driven, hopeful",
    best_for=["nonprofit", "media", "marketing"],
    palette={"bg": "#FAF7F2", "surface": "#FFFFFF", "text": "#1F1F1F", "accent": "#C8102E", "muted": "#6B6B6B"},
    type={"display": "Fraunces", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="subtle paper grain",
    motion_energy="measured",
    corner_radius="soft 8px",
    shadow_style="soft, low-opacity",
    references=["charitywater.org", "againstmalaria.com", "givedirectly.org"],
    rationale="Nonprofit design needs warmth to drive mission without losing credibility. Cream bg + warm red accent feels human, not corporate. Fraunces display + Inter body is the editorial combo. Photography (real beneficiaries, never stock) drives the message.",
    anti_patterns=["dark mode default", "vibrant gradients", "rounded pill everything", "decorative motion everywhere"],
)

add(
    id="t092",
    name="Education Friendly",
    voice="approachable, structured, encouraging",
    best_for=["saas", "docs", "marketing"],
    palette={"bg": "#FFFFFF", "surface": "#F7F9FC", "text": "#1A1A2E", "accent": "#5B21B6", "muted": "#6B7280"},
    type={"display": "Bricolage Grotesque", "body": "DM Sans", "mono": "JetBrains Mono"},
    texture="subtle gradient overlays on hero",
    motion_energy="measured",
    corner_radius="soft 12px",
    shadow_style="soft 0 4px 12px rgba(91,33,182,0.08)",
    references=["duolingo.com", "khanacademy.org", "coursera.org"],
    rationale="Education design needs approachability without losing structure. Bricolage display + DM Sans body feels friendly. Purple accent (intentional, not default) drives engagement. Generous 12px corners feel approachable. Motion only on progress transitions.",
    anti_patterns=["dark mode default", "vibrant gradients everywhere", "sharp 0px corners", "decorative serif display"],
)

add(
    id="t093",
    name="Real Estate Premium",
    voice="luxurious, spacious, photographic",
    best_for=["ecommerce", "marketing", "portfolio"],
    palette={"bg": "#FAF7F2", "surface": "#FFFFFF", "text": "#1F1B16", "accent": "#7A4A1F", "muted": "#7A6E5A"},
    type={"display": "Cormorant", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="none — flat with crisp architectural photography",
    motion_energy="measured",
    corner_radius="soft 4px",
    shadow_style="very subtle 0 2px 8px rgba(31,27,22,0.06)",
    references=["compass.com", "zillow.com", "sothebysrealty.com"],
    rationale="Real estate premium uses warm cream bg + brown accent for luxurious feel. Cormorant display + Inter body is the property-brochure combo. Crisp architectural photography dominates. Motion only on image transitions — never on scroll.",
    anti_patterns=["dark mode default", "vibrant accent colors", "rounded pill everything", "decorative motion everywhere"],
)

add(
    id="t094",
    name="Restaurant Menu",
    voice="appetizing, hand-set, evening-warm",
    best_for=["media", "marketing", "personal"],
    palette={"bg": "#1A1410", "surface": "#241B14", "text": "#F5EBC6", "accent": "#C49B3C", "muted": "#9A8B6E"},
    type={"display": "Cormorant", "body": "Cormorant", "mono": "IBM Plex Mono"},
    texture="subtle paper grain + foil accents",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — gold rules only",
    references=["elevenmadisonpark.com", "willowroad.com", "tartinefactory.com"],
    rationale="Restaurant menu uses warm dark bg + gold accent for evening-warm feel. Cormorant throughout (display + body) gives the printed-menu voice. Gold rules (not shadows) carry structure. Photography only on hero — menus are typography.",
    anti_patterns=["bright primary colors", "sans-serif body", "rounded corners", "decorative motion"],
)

add(
    id="t095",
    name="Travel Magazine",
    voice="aspirational, photographic, editorial",
    best_for=["media", "marketing", "portfolio"],
    palette={"bg": "#FBFAF7", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#C8102E", "muted": "#6B6B6B"},
    type={"display": "Playfair Display", "body": "Source Serif 4", "mono": "IBM Plex Mono"},
    texture="none — flat with full-bleed photography",
    motion_energy="cinematic",
    corner_radius="sharp 0px",
    shadow_style="none — rules only",
    references=["cntraveler.com", "condenasttraveler.com", "natgeotravel.com"],
    rationale="Travel magazine uses cream bg + red accent + serif type for editorial feel. Playfair display + Source Serif body is the print-magazine combo. Full-bleed photography dominates. Motion is cinematic — slow fades, parallax, scroll-driven reveals.",
    anti_patterns=["dark mode default", "vibrant gradients everywhere", "rounded card corners", "sans-serif body"],
)

add(
    id="t096",
    name="Government Plain",
    voice="official, accessible, no-nonsense",
    best_for=["nonprofit", "docs", "saas"],
    palette={"bg": "#FFFFFF", "surface": "#F4F6F8", "text": "#1A1A1A", "accent": "#1A4480", "muted": "#5C5C5C"},
    type={"display": "Public Sans", "body": "Public Sans", "mono": "IBM Plex Mono"},
    texture="none — pure flat",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — borders only",
    references=["usa.gov", "designsystem.digital.gov", "gov.uk"],
    rationale="Government design prioritizes accessibility and trust over aesthetics. Public Sans throughout (US Web Design System) for unified voice. Navy accent for official markers. Strict WCAG AAA contrast. No motion that could distract from content.",
    anti_patterns=["decorative motion", "vibrant gradients", "rounded pill everything", "decorative serif display"],
)

add(
    id="t097",
    name="Aerospace Engineering",
    voice="technical, precise, blueprint-clear",
    best_for=["saas", "docs", "marketing"],
    palette={"bg": "#0A0F1A", "surface": "#131A2E", "text": "#E2E8F0", "accent": "#3B82F6", "muted": "#7A85A8"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle blueprint grid at 4% opacity",
    motion_energy="measured",
    corner_radius="sharp 0px",
    shadow_style="none — borders and rules only",
    references=["spacex.com", "blueorigin.com", "lockheedmartin.com"],
    rationale="Aerospace uses dark bg + bright blue + visible grid for engineering feel. Inter throughout for technical legibility. Blueprint grid (only at 4% opacity) reinforces the reference without overwhelming. Motion only on data — never decorative.",
    anti_patterns=["decorative motion", "vibrant gradients everywhere", "rounded pill everything", "decorative serif display"],
)

add(
    id="t098",
    name="Biotech Clean",
    voice="scientific, sterile, hopeful",
    best_for=["saas", "marketing", "docs"],
    palette={"bg": "#FFFFFF", "surface": "#F4F8FA", "text": "#0F1B2D", "accent": "#0E7C7B", "muted": "#5A6B82"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="none — pure flat",
    motion_energy="calm",
    corner_radius="soft 8px",
    shadow_style="very subtle 0 1px 2px rgba(15,27,45,0.04)",
    references=["23andme.com", "color.com", "cerna.com"],
    rationale="Biotech needs scientific credibility and hope. Teal accent signals health without cliché medical blue. Inter throughout for unified voice. Strict 4.5:1 contrast on all text. Avoid motion that could trigger vestibular issues.",
    anti_patterns=["dark mode default", "decorative motion", "rounded pill everything", "vibrant gradients"],
)

add(
    id="t099",
    name="Architecture Firm",
    voice="precise, technical, material-aware",
    best_for=["portfolio", "media", "agency"],
    palette={"bg": "#F4F1EA", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#B8541F", "muted": "#6B6258"},
    type={"display": "Inter", "body": "Inter", "mono": "JetBrains Mono"},
    texture="subtle blueprint grid at 6% opacity",
    motion_energy="calm",
    corner_radius="sharp 0px",
    shadow_style="none — borders and rules only",
    references=["oma.eu", "big.dk", "snohetta.com"],
    rationale="Architecture firms communicate in plans and renderings. Cream bg + terra-cotta accent feels material-aware. Inter throughout for technical legibility. Blueprint grid (only at 6% opacity) reinforces the reference. Drawings dominate — not photography.",
    anti_patterns=["decorative motion", "vibrant gradients", "rounded corners", "decorative serif display"],
)

add(
    id="t100",
    name="Luxury Fashion",
    voice="refined, photographic, restrained",
    best_for=["ecommerce", "portfolio", "marketing"],
    palette={"bg": "#FAF7F2", "surface": "#FFFFFF", "text": "#1A1A1A", "accent": "#1A1A1A", "muted": "#7A7A7A"},
    type={"display": "Cormorant", "body": "Inter", "mono": "IBM Plex Mono"},
    texture="none — flat with full-bleed editorial photography",
    motion_energy="cinematic",
    corner_radius="sharp 0px",
    shadow_style="none — borders only",
    references=["the-row.com", "bottegaveneta.com", "celine.com"],
    rationale="Luxury fashion uses extreme restraint: cream bg, monochrome palette, zero decoration. Cormorant display + Inter body is the lookbook combo. Full-bleed editorial photography dominates. Motion is cinematic — slow fades only, never on scroll.",
    anti_patterns=["vibrant accent colors", "rounded corners", "decorative gradients", "decorative motion everywhere"],
)

# ---------------------------------------------------------------------------
# Validate & write
# ---------------------------------------------------------------------------
assert len(T) == 100, f"Expected 100 themes, got {len(T)}"
ids = [t["id"] for t in T]
assert ids == [f"t{i:03d}" for i in range(1, 101)], "ID sequence is off"

for t in T:
    assert set(t.keys()) == {
        "id", "name", "voice", "best_for", "palette", "type",
        "texture", "motion_energy", "corner_radius", "shadow_style",
        "references", "rationale", "anti_patterns",
    }, f"Schema mismatch in {t['id']}"
    assert set(t["palette"].keys()) == {"bg", "surface", "text", "accent", "muted"}
    assert set(t["type"].keys()) == {"display", "body", "mono"}
    assert t["motion_energy"] in {"calm", "measured", "energetic", "cinematic"}
    assert 2 <= len(t["references"]) <= 3
    assert 3 <= len(t["anti_patterns"]) <= 4
    assert set(t["best_for"]).issubset({
        "saas", "portfolio", "agency", "ecommerce", "media",
        "dashboard", "docs", "marketing", "nonprofit", "personal",
    })
    assert len(t["voice"].split(",")) == 3
    # hex validity
    import re
    for c in t["palette"].values():
        assert re.match(r"^#[0-9A-Fa-f]{6}$", c), f"Bad hex {c} in {t['id']}"

out = Path("/home/z/my-project/ai-design-skill/data/themes-100.json")
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", encoding="utf-8") as f:
    json.dump({"themes": T}, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Wrote {out}")
print(f"Themes: {len(T)}")
print(f"Motion energy distribution: {sorted(set(t['motion_energy'] for t in T))}")
print(f"Best-for tags used: {sorted(set(tag for t in T for tag in t['best_for']))}")
