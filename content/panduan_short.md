# Panduan Produksi Short: Jejak Menuju Kaya

## Aturan gambar latar
- Minimal 5 gambar per short (kira-kira 1 gambar per 10 detik, dan selalu sesuai narasi): 2 dari lisensi bebas dan 3 dari AI.
- Jika membutuhkan 6 gambar: 3 dari lisensi bebas dan 3 dari AI.
- Setiap gambar diberi label "ilustrasi" di layar, dan kredit di bawah layar. Gambar AI dicatat sebagai "gambar AI (Creative Claw)".
- Gambar lisensi bebas diambil dari sumber dengan lisensi jelas (CC0, domain publik, CC BY-SA), dan dicatat di `scratchpad/assets/asset_log.md`.

## Urutan kerja per short
1. Naskah: tulis di `content/shorts/`, lalu tinjauan Opus sebagai satu paket.
2. Persetujuan pengguna untuk naskah.
3. Narasi TTS (suara Hope, bahasa id, mp3 44,1 kHz), lalu normalisasi ke -14 LUFS.
4. Waktu awal tiap kata dari TTS, disimpan sebagai `hari{N}_wordstarts.json`.
5. Pilih latar per beat sesuai aturan gambar di atas, lalu atur `BEATS` di skrip render.
6. Render 1080x1920, lalu periksa frame dan sinkronisasi subtitle.
7. Tinjauan Opus, lalu kirim ke pengguna untuk dicek.
8. Unggah sebagai private hanya setelah persetujuan eksplisit untuk video itu.

## Lokasi berkas
- Naskah: `content/shorts/hari4-7.md` (dan berkas hari berikutnya)
- Kalender short: `content/calendar.md` (cabang `content-calendar`)
- Jadwal video panjang: `content/jadwal_rilis.md`
- Skrip render: `tools/render_short.py`. Path di dalamnya masih menunjuk ke `scratchpad/`, karena aset, narasi, dan waktu kata ada di sana.
- Narasi dan waktu kata: `scratchpad/voice_shorts/`
- Aset gambar: `scratchpad/assets/`
