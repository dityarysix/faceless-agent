# render_short.py: short vertikal 1080x1920 untuk hari 4–14.
# Pemakaian: python3 render_short.py HARI OUT.mp4
# Variabel lingkungan: SHORT_ROOT (folder sesi, berisi scratchpad/assets dan scratchpad/voice_shorts), SHORT_LOGO (berkas logo).
import os, re, subprocess, sys, json
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

DAY, OUT = int(sys.argv[1]), sys.argv[2]
ROOT = os.environ.get("SHORT_ROOT", "/tmp/claude-0/-home-user-faceless-agent/a5bcb3d8-8708-5776-b322-d351f45b0e25/")
LOGO = os.environ.get("SHORT_LOGO", ROOT + "images/20.jpg")
ASSETS = ROOT + "scratchpad/assets/"
VOICE = ROOT + f"scratchpad/voice_shorts/hari{DAY}_narasi_norm14.mp3"
TEXTS = ROOT + "scratchpad/voice_shorts/texts.json"
W, H, FPS = 1080, 1920, 30
# tata letak dalam zona aman Reels/Shorts: kosongkan sekitar 270 px atas dan 670 px bawah
HEAD_Y, TITLE_Y, SUB_TOP, CREDIT_Y, LOGO_Y = 290, 540, 900, 1130, 400
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
NAVY, AMBER, WHITE, GREY = (11, 18, 32), (240, 180, 90), (240, 244, 248), (170, 180, 195)
F = {"t": ImageFont.truetype(BOLD, 74), "s": ImageFont.truetype(REG, 44), "k": ImageFont.truetype(REG, 30)}

# judul, gambar latar (aset CC0/PD yang sudah diunduh), dan kredit per hari
SHORT = {
    4: ("Cara sederhana mencatat pengeluaran harian", "", "CMA CC0 dan gambar AI (Creative Claw)"),
    5: ("Kebutuhan, keinginan, dan belanja impulsif", "", "AIC (domain publik) dan gambar AI (Creative Claw)"),
    6: ("Menabung dari uang lembur", "ref_cma_solidus_justinian.jpg", "Cleveland Museum of Art, CC0"),
    7: ("Tantangan 7 hari", "ref_caravan_sahara_cc0.jpg", "Asfour hamza, CC0, Wikimedia Commons"),
    8: ("Dana darurat: mulai dari berapa?", "", "Cleveland Museum of Art (CC0) dan gambar AI (Creative Claw)"),
    9: ("Pengaruh lingkungan pada kebiasaan belanja", "", "Cleveland Museum of Art (CC0) dan gambar AI (Creative Claw)"),
    10: ("Gaji sama, hasil berbeda", "", "Cleveland Museum of Art (CC0) dan gambar AI (Creative Claw)"),
    11: ("Paylater dan kartu kredit: aman atau jebakan?", "", "Cleveland Museum of Art (CC0), Wikimedia Commons (CC0), dan gambar AI (Creative Claw)"),
    12: ("Dari jeda 10 menit ke aturan 24 jam", "", "Cleveland Museum of Art (CC0) dan gambar AI (Creative Claw)"),
    13: ("Jatuh bangun soal uang", "", "Cleveland Museum of Art (CC0) dan gambar AI (Creative Claw)"),
    14: ("Polling: bagian anggaran paling sulit dijaga", "", "Cleveland Museum of Art (CC0) dan gambar AI (Creative Claw)"),
}

# latar per beat: (indeks kalimat awal, file gambar di scratchpad/assets/)
BEATS = {
    4: [(0, "cma_purse_1944.283.jpg"), (2, "gen4_b2.jpg"), (4, "gen4_b3.jpg"), (6, "gen4_b4.jpg"), (8, "cma_coin_1999.226.jpg")],
    5: [(0, "aic_basket_apples.jpg"), (2, "gen5_b2.jpg"), (4, "aic_womens_shoes.jpg"), (5, "gen5_b4.jpg"), (8, "aic_wall_clock.jpg"), (10, "gen5_b6.jpg")],
    8: [(0, "gen8_a1.jpg"), (4, "f8_1.jpg"), (6, "gen8_a2.jpg"), (9, "f8_2.jpg"), (11, "gen8_a3.jpg")],
    9: [(0, "gen9_a1.jpg"), (3, "f9_1.jpg"), (6, "gen9_a2.jpg"), (8, "f9_2.jpg"), (11, "gen9_a3.jpg")],
    10: [(0, "gen10_a1.jpg"), (3, "f10_1.jpg"), (6, "gen10_a2.jpg"), (10, "f10_2.jpg"), (12, "gen10_a3.jpg")],
    11: [(0, "gen11_a1.jpg"), (2, "f11_1.jpg"), (4, "gen11_a2.jpg"), (5, "f11_2.jpg"), (7, "gen11_a3.jpg")],
    12: [(0, "gen12_a1.jpg"), (4, "f12_1.jpg"), (7, "gen12_a2.jpg"), (9, "f12_2.jpg"), (13, "gen12_a3.jpg")],
    13: [(0, "gen13_a1.jpg"), (3, "f13_1.jpg"), (6, "gen13_a2.jpg"), (9, "f13_2.jpg"), (12, "gen13_a3.jpg")],
    14: [(0, "gen14_a1.jpg"), (3, "f14_1.jpg"), (5, "gen14_a2.jpg"), (7, "f14_2.jpg"), (10, "gen14_a3.jpg")],
}

def dur(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).decode().strip())

PROBE = ImageDraw.Draw(Image.new("RGB", (10, 10)))

def wrap(text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if PROBE.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def build_subs(text, D, starts):
    # halaman dimulai pada waktu kata pertamanya dari TTS; halaman satu kata digabung ke halaman sebelumnya dalam kalimat yang sama
    sents = [x for x in re.split(r"(?<=[.?!])\s+", text.strip()) if x]
    pages, wi, sent_starts = [], 0, []
    for x in sents:
        sent_starts.append(starts[wi])
        lines = wrap(x, F["s"], W - 200)
        sent_pages = []
        for i in range(0, len(lines), 2):
            p = lines[i:i + 2]
            if len(" ".join(p).split()) == 1 and sent_pages:
                merged = " ".join(sent_pages[-1][1] + p)
                sent_pages[-1][1] = wrap(merged, F["s"], W - 200)
                wi += 1
                continue
            sent_pages.append([wi, list(p)])
            wi += len(" ".join(p).split())
        pages.extend(sent_pages)
    subs = []
    for k, (idx, p) in enumerate(pages):
        t0 = starts[idx]
        t1 = starts[pages[k + 1][0]] if k + 1 < len(pages) else D
        subs.append((t0, t1, p))
    return subs, sent_starts

@lru_cache(maxsize=None)
def load_logo(size):
    im = ImageOps.exif_transpose(Image.open(LOGO)).convert("RGB").resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    im = im.convert("RGBA")
    im.putalpha(mask)
    return im

@lru_cache(maxsize=None)
def base_image(path):
    im = ImageOps.fit(ImageOps.exif_transpose(Image.open(ASSETS + path)).convert("RGB"), (W, H))
    im = im.filter(ImageFilter.GaussianBlur(10))
    return Image.blend(im, Image.new("RGB", (W, H), NAVY), 0.8)

def frame(t, D, title, beat_times, credit, subs):
    z = 1 + 0.03 * (t / D)                       # zoom pelan pada latar
    cw, ch = W / z, H / z
    cx, cy = (W - cw) / 2, (H - ch) / 2
    img_name = [f for tt, f in beat_times if tt <= t][-1]
    img = base_image(img_name).resize((W, H), Image.BILINEAR, box=(cx, cy, cx + cw, cy + ch))
    d = ImageDraw.Draw(img)
    d.text((80, HEAD_Y), "JEJAK MENUJU KAYA", font=F["k"], fill=AMBER)
    label = f"Hari {DAY} dari 28"
    d.text((W - 80 - d.textlength(label, font=F["k"]), HEAD_Y), label, font=F["k"], fill=GREY)
    tag = "ilustrasi"
    d.text((W - 80 - d.textlength(tag, font=F["k"]), HEAD_Y + 50), tag, font=F["k"], fill=GREY)
    if t < D - 3:
        y = TITLE_Y
        for line in wrap(title, F["t"], W - 160):
            d.text((80, y), line, font=F["t"], fill=WHITE)
            y += 92
    else:
        logo = load_logo(480)
        img.paste(logo, ((W - 480) // 2, LOGO_Y), logo)
    ly = CREDIT_Y
    for line in wrap("Gambar: " + credit, F["k"], W - 160):
        d.text((80, ly), line, font=F["k"], fill=GREY)
        ly += 38
    for t0, t1, lines in subs:
        if t0 <= t < t1:
            top = SUB_TOP
            lh = 62
            bw = max(d.textlength(l, font=F["s"]) for l in lines) + 60
            d.rounded_rectangle((W / 2 - bw / 2, top - 16, W / 2 + bw / 2, top + lh * len(lines) + 16), radius=14, fill=(5, 8, 16))
            for i, l in enumerate(lines):
                d.text(((W - d.textlength(l, font=F["s"])) / 2, top + i * lh), l, font=F["s"], fill=WHITE)
            break
    return img.tobytes()

title, img_name, credit = SHORT[DAY]
texts = json.load(open(TEXTS, encoding="utf-8"))
D = dur(VOICE)
starts = json.load(open(ROOT + f"scratchpad/voice_shorts/hari{DAY}_wordstarts.json", encoding="utf-8"))["starts"]
subs, sent_starts = build_subs(texts[f"Hari {DAY}"], D, starts)
beat_times = [(sent_starts[k], f) for k, f in BEATS[DAY]]
CMD = ["ffmpeg", "-y", "-loglevel", "error",
       "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-i", VOICE, "-map", "0:v", "-map", "1:a", "-t", f"{D:.3f}",
       "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
       "-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
       "-movflags", "+faststart", OUT]
ff = subprocess.Popen(CMD, stdin=subprocess.PIPE)
frames = int(D * FPS)
for f in range(frames):
    ff.stdin.write(frame(f / FPS, D, title, beat_times, credit, subs))
ff.stdin.close()
rc = ff.wait()
print("done" if rc == 0 else f"gagal rc={rc}", OUT, "frames", frames)
