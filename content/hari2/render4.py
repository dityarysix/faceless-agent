import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TOTAL = 40.0

H_HOOK = "Stres →\ncheckout?"
H_MID = "Stres → cari lega lewat belanja"
H_PAY = "Jadi kebiasaan?\nTagihan + nyesel"
H_TUNDA = "Tunda 10 menit,\ntulis perasaanmu"
H_CTA = "Hari 3:\nKisah kekayaan\nkebiasaan kecil"

# (start_seconds, headline, subtitle chunk, background)
timeline = [
    (0.0,  H_HOOK,  "Habis hari yang berat…", "bg/s0.jpg"),
    (1.2,  H_HOOK,  "tiba-tiba udah checkout aja.", "bg/s0.jpg"),
    (3.4,  H_HOOK,  "Pernah?", "bg/s0.jpg"),
    (4.0,  H_MID,   "Itu bukan kebetulan.", "bg/s1.jpg"),
    (5.9,  H_MID,   "Saat stres, banyak dari kita", "bg/s1.jpg"),
    (6.95, H_MID,   "belanja buat cari rasa lega yang cepat.", "bg/s1.jpg"),
    (10.3, H_MID,   "Dan memang, rasanya jadi sedikit lebih enak.", "bg/s1.jpg"),
    (13.5, H_PAY,   "Masalahnya, kalau jadi kebiasaan,", "bg/s2.jpg"),
    (16.0, H_PAY,   "yang datang belakangan bisa jadi tagihan paylater atau kartu kredit,", "bg/s2.jpg"),
    (19.9, H_PAY,   "plus rasa nyesel.", "bg/s2.jpg"),
    (21.6, H_PAY,   "Padahal sumber stresnya belum selesai.", "bg/s2.jpg"),
    (24.4, H_TUNDA, "Coba ini: waktu dorongan belanja muncul,", "bg/s3.jpg"),
    (27.2, H_TUNDA, "tunda dulu sepuluh menit.", "bg/s3.jpg"),
    (28.6, H_TUNDA, "Tulis apa yang sebenarnya kamu rasain.", "bg/s3.jpg"),
    (31.1, H_TUNDA, "Kalau setelah itu masih butuh, baru beli.", "bg/s3.jpg"),
    (33.9, H_CTA,   "Besok:", "bg/s4.jpg"),
    (34.7, H_CTA,   "kisah kekayaan yang dimulai dari kebiasaan kecil.", "bg/s4.jpg"),
    (37.9, H_CTA,   "Follow, ya!", "bg/s4.jpg"),
]

f_brand = ImageFont.truetype(BOLD, 40)
f_label = ImageFont.truetype(REG, 44)
f_big = ImageFont.truetype(BOLD, 76)
f_sub = ImageFont.truetype(REG, 50)

def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def background(path):
    bg = Image.open(path).convert("RGB")
    scale = max(W / bg.width, H / bg.height)
    bg = bg.resize((int(bg.width * scale) + 1, int(bg.height * scale) + 1), Image.LANCZOS)
    left, top = (bg.width - W) // 2, (bg.height - H) // 2
    bg = bg.crop((left, top, left + W, top + H)).filter(ImageFilter.GaussianBlur(6))
    veil = Image.new("RGB", (W, H), (10, 16, 28))
    return Image.blend(bg, veil, 0.40).convert("RGBA")

CX = 510  # center of the 70..950 cards, keeps the right side clear for platform buttons

def frame(headline, sub, bgpath, out):
    img = background(bgpath)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # brand block moved down, out of the top ~10% platform UI zone
    d.text((CX, 240), "JEJAK MENUJU KAYA", font=f_brand, fill=(240, 180, 90, 255), anchor="mm")
    d.text((CX, 295), "Hari 2 dari 28", font=f_label, fill=(200, 210, 225, 255), anchor="mm")
    # headline card, text centered inside it
    lh = 102
    hl = [ln for part in headline.split("\n") for ln in wrap(d, part, f_big, W - 260)]
    total = len(hl) * lh
    y0 = 560 - total // 2 + lh // 2
    d.rounded_rectangle((70, y0 - lh//2 - 40, 950, y0 - lh//2 + total + 40), radius=36, fill=(8, 12, 22, 170))
    y = y0
    for ln in hl:
        d.text((CX, y), ln, font=f_big, fill=(255, 255, 255, 255), anchor="mm")
        y += lh
    # subtitle card, bottom edge kept above the 20% platform caption zone
    sl = wrap(d, sub, f_sub, 780)
    sh = len(sl) * 66
    sy = 1240
    d.rounded_rectangle((70, sy - sh//2 - 40, 950, sy + sh//2 + 40), radius=28, fill=(8, 12, 22, 190))
    y = sy - (len(sl) - 1) * 33
    for ln in sl:
        d.text((CX, y), ln, font=f_sub, fill=(235, 240, 248, 255), anchor="mm")
        y += 66
    Image.alpha_composite(img, ov).convert("RGB").save(out)

concat = []
for i, (start, hl, sub, bgp) in enumerate(timeline):
    end = timeline[i+1][0] if i + 1 < len(timeline) else TOTAL
    dur = round(end - start, 3)
    frame(hl, sub, bgp, f"x{i}.png")
    out = f"x{i}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", f"x{i}.png", "-t", str(dur),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "18", out], check=True)
    concat.append(f"file '{out}'")
open("list4.txt", "w").write("\n".join(concat) + "\n")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "list4.txt", "-c", "copy", "silent_v4.mp4"], check=True)
import json, re
meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", "vo_hari2.mp3", "-af",
                       "loudnorm=I=-14:TP=-1:LRA=7:print_format=json", "-f", "null", "-"],
                      capture_output=True, text=True).stderr
j = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", meas).group(0))
ln = (f"loudnorm=I=-14:TP=-1:LRA=7:measured_I={j['input_i']}:measured_LRA={j['input_lra']}"
      f":measured_TP={j['input_tp']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true,apad=whole_dur=40")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "silent_v4.mp4", "-i", "vo_hari2.mp3",
                "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                "-af", ln, "-t", "40", "-movflags", "+faststart", "hari2_v4.mp4"], check=True)
print("done")
