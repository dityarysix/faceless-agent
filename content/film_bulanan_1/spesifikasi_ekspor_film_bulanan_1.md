# Spesifikasi ekspor dan subtitle: film bulanan 1

Status: disetujui pengguna (loudness -14 LUFS, sample rate 48.000 Hz, pola nama berkas, serta CRF 20 dan yuv420p sesuai pilot v9).

## Video
- Resolusi: 1920×1080, rasio 16:9.
- Frame rate: 25 fps.
- Codec: H.264 (libx264), pixel format yuv420p, CRF 20 (sesuai pilot v9).
- Latar dan kartu: tidak ada bingkai hitam di awal atau akhir.

## Audio
- Codec: AAC, 192 kbps, stereo.
- Sample rate: 48.000 Hz.
- Loudness: target -14 LUFS terintegrasi, true peak maksimum -1 dBTP.
- Narasi dominan. Musik sekitar 20 dB di bawah narasi, SFX di bawah musik.

## Subtitle
- Format: SRT, UTF-8, Bahasa Indonesia.
- Maksimal 2 baris per entri, sekitar 42 karakter per baris.
- Waktu mengikuti data waktu kata dari TTS, bukan perkiraan manual.
- Subtitle tidak menutupi sumber di layar atau label "ilustrasi, tokoh fiktif".

## Label dan sumber di layar
- Label "ilustrasi, tokoh fiktif" tampil untuk setiap ilustrasi Rudi, Roni, dan tokoh pendamping.
- Klaim berstatus Sebagian menampilkan sumbernya di layar di jenis kartu apa pun (kartu, tipografi, timeline, peta).
- Penjelasan umum diberi label "Penjelasan umum, bukan klaim peristiwa" jika tidak berupa klaim.

## Nama berkas
- Pola: `jejak_krismon_bab{N}_{versi}.mp4` dan `jejak_krismon_bab{N}_{versi}.srt`.
- Contoh: `jejak_krismon_bab1_v9.mp4`.
- Pilot memakai nomor bab 0 dan {versi} `pilot_v9`: `jejak_krismon_bab0_pilot_v9.mp4`. {versi} boleh berisi kata `pilot`.
