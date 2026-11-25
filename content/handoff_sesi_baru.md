# Prompt serah-terima: Jejak Menuju Kaya

Salin isi bagian "PROMPT" ke pesan pertama di sesi baru.

## PROMPT

```
Kamu melanjutkan proyek kanal "Jejak Menuju Kaya" (video edukasi keuangan dan sejarah ekonomi, bahasa Indonesia).

BACA DULU (sebelum mengerjakan apa pun):
1. content/panduan_short.md (cabang claude/eloquent-mccarthy-r5cuoa)
2. content/shorts/hari4-7.md (cabang claude/eloquent-mccarthy-r5cuoa)
3. content/jadwal_rilis.md (cabang claude/eloquent-mccarthy-r5cuoa)
4. content/calendar.md (cabang content-calendar)
5. tools/render_short.py (cabang claude/eloquent-mccarthy-r5cuoa)
6. content/handoff_sesi_baru.md (cabang claude/eloquent-mccarthy-r5cuoa)

ATURAN KERJA (wajib):
- Setiap perubahan berkas: tunjukkan diff lengkap dulu, tunggu persetujuan eksplisit, baru tulis.
- Commit dan push hanya jika saya minta secara eksplisit.
- Setiap naskah, render, dan perubahan besar ditinjau reviewer (Opus) sebelum dianggap final. Hanya tunjukkan ke saya yang sudah APPROVE.
- Tidak ada unggahan atau posting ke YouTube/Instagram tanpa persetujuan eksplisit untuk video itu. Unggahan selalu private dulu. Penjadwalan dan rilis saya lakukan sendiri di YouTube Studio.
- Jangan sebut model dalam commit, PR, atau artefak repo.
- Durasi short: target 52–57 detik. Sampai 59 detik diterima. Jangan tanya lagi soal durasi.
- Jangan tampilkan token atau key di chat.

STATUS SAAT INI:
- Short Hari 1 (Gaji cepat habis?): selesai, tayang 24 Nov 2026.
- Short Hari 2 (Kenapa kita sering belanja pas lagi stres?): selesai, tayang 25 Nov 2026.
- Short Hari 3 (Sepuluh ribu sehari, jadi berapa setahun?): dijadwalkan tayang 26 Nov 2026. ID video belum tercatat di repo. Cek di YouTube Studio.
- Short Hari 4 (Cara sederhana mencatat pengeluaran harian): dijadwalkan Jumat 27 Nov 2026 pukul 06.00 WIB. ID BxOg765MVto (tercatat di content/calendar.md). File master: scratchpad/render/short_hari4_v3.mp4.
- Short Hari 5 (Kebutuhan, keinginan, dan belanja impulsif): dijadwalkan Sabtu 28 Nov 2026 pukul 06.00 WIB. ID KGR1-bMB27k (tercatat di content/calendar.md). File master: scratchpad/render/short_hari5_v4.mp4 (APPROVE reviewer).
- Short Hari 6 dan 7: naskah sudah disetujui pengguna (content/shorts/hari4-7.md). Belum ada latar, render, atau unggahan.
  - Narasi Hari 6: scratchpad/voice_shorts/hari6_narasi.mp3 (52,5 detik). Loudness-nya -14,8 LUFS, perlu dinormalisasi ulang dengan prosedur yang sama seperti Hari 4 dan 5 (dua tahap loudnorm, lalu penyesuaian volume agar -14 LUFS).
  - Narasi Hari 7: scratchpad/voice_shorts/hari7_narasi.mp3 (50,7 detik, di bawah target 52). Sesi baru yang menentukan cara menanganinya (terima, tambah kalimat, atau TTS ulang). Usulkan pilihan ke pengguna sebelum TTS ulang. Setelah itu normalisasi ulang seperti Hari 6.
  - wordstarts Hari 6 dan 7 belum ada. TTS perlu diambil ulang lewat job ID Creative Claw bila masih tersedia (search_assets/check_job); kalau tidak, buat ulang TTS.
- Short Hari 8–28: belum dibuat. Kalender: Hari 14 = polling anggaran; Hari 21 = pembahasan hasil tantangan Hari 7.
- Jadwal rutin: short setiap hari pukul 06.00 WIB; video mingguan 10–15 menit setiap Rabu pukul 16.00 WIB; produksi video mingguan dimulai setiap Minggu pukul 10.00 WIB; video bulanan 35–45 menit (jadwal belum ditentukan).
- Video mingguan minggu 1: "Kisah Dua Orang Super Kaya: Mansa Musa dan Rockefeller", ID hNcfWMeHtkg, private, tayang Rabu 25 Nov 2026 pukul 16.00 WIB (dijadwalkan manual). Playlist "Cerita Sejarah dan Pelajaran Keuangan" (Public) sudah dibuat pengguna.
- Video mingguan minggu 2: tayang Rabu 2 Des 2026 pukul 16.00 WIB; judul belum ditentukan; produksi mulai Minggu 29 Nov 2026 pukul 10.00 WIB.

PERBAIKAN YANG HARUS DIKERJAKAN DI AWAL SESI BARU (masing-masing dengan diff dulu):
1. tools/render_short.py: path ROOT masih menunjuk ke folder sesi lama (baris 7). Ganti ke path scratchpad sesi baru, sebaiknya lewat variabel lingkungan. Logo dibaca dari <ROOT>/images/20.jpg di luar scratchpad; salin logo ke scratchpad/assets/ atau minta pengguna mengirim ulang.
2. tools/render_short.py: tambahkan BEATS[6] dan BEATS[7], dan perbarui SHORT[6] dan SHORT[7] (judul, kredit yang jujur sesuai latar yang dipakai). SHORT[6] dan SHORT[7] saat ini masih placeholder lama dengan kredit yang keliru.
3. Log aset: scratchpad/assets/asset_log.md belum mencatat aset Hari 4 (cma_purse_1944.283.jpg, cma_coin_1999.226.jpg, gen4_b2/b3/b4.jpg) dan gambar AI Hari 5 (gen5_b2/b4/b6.jpg). Lengkapi dulu, lalu usulkan diff untuk menyimpan salinannya di content/asset_log.md di repo agar tidak hilang bersama scratchpad.
4. Sumber lisensi bebas: gunakan semua, yaitu CMA (CC0), AIC (domain publik), dan Wikimedia Commons (CC BY-SA dengan atribusi). Pastikan setiap gambar dari Wikimedia Commons diverifikasi lisensinya di halaman berkas dan dicatat di asset_log.
5. Suara: Hope (voice_id tnSpp4vdxKPjI9w0GnoV), language_code "id", mp3_44100_128.

PIPELINE SHORT (sudah teruji):
1. Naskah: content/shorts/hari{N}-... disetujui pengguna, ditinjau Opus sebagai paket mingguan.
2. Narasi TTS: ElevenLabs v4 lewat Creative Claw (speech/elevenlabs-v4), satu per satu, lalu check_job sampai completed.
3. wordTimings dari check_job disimpan ke scratchpad/voice_shorts/hari{N}_wordstarts.json (array starts per kata; jumlahnya harus sama dengan jumlah kata naskah).
4. Normalisasi narasi ke -14 LUFS (dua tahap loudnorm dengan measured values, lalu penyesuaian volume jika perlu). Simpan sebagai hari{N}_narasi_norm14.mp3.
5. Latar: minimal 5 gambar per short (sekitar 1 gambar per 10 detik, selalu sesuai narasi). 5 gambar = 2 lisensi bebas + 3 AI. 6 gambar = 3 lisensi bebas + 3 AI. Gambar AI: image/nano-banana-2, aspect_ratio 9:16, sekitar 12 kredit per gambar. Setiap gambar diberi label "ilustrasi" di layar. Kredit di bawah layar harus jujur.
6. Render: python3 tools/render_short.py HARI OUT.mp4 (setelah perbaikan 1–2). Subtitle mengikuti waktu kata. Logo tampil 3 detik terakhir.
7. Cek: ffprobe (1080x1920, 30 fps, durasi), ebur128 (sekitar -14 LUFS, peak aman), beberapa frame, dan sinkronisasi subtitle.
8. Tinjauan Opus (reviewer). Kirim ke saya hanya jika APPROVE.
9. Unggah private: YouTube Data API v3 resumable, env YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN. Judul mengandung #Shorts. containsSyntheticMedia true. Hanya setelah persetujuan eksplisit. Skrip unggah belum ada di repo; buat diff dulu.
10. Kalender: tandai status lewat diff, lalu commit ke content-calendar hanya jika diminta.

KALENDER: worktree scratchpad/wt_calendar mungkin sudah tidak ada di sesi baru. Jalankan git worktree prune, lalu buat worktree baru dari origin/content-calendar bila perlu.

VIDEO BULANAN (riset dan rancangan, 35–45 menit):
- Target 35–40 menit, tema peristiwa ekonomi besar.
- Kandidat tema: Global Tech Boom and Burst, Krisis Asia 1998 (krismon), Great Depression 1930-an.
- Peringkat sementara: krismon di posisi 1 (keyakinan sedang sampai tinggi). Dot-com dan Great Depression di posisi 2–3, keyakinan rendah.
- Riset krismon: video berbahasa Indonesia yang sudah ada (Ngomongin Uang, Kompas TV, video Habibie) tanpa data views. Perlu cek YouTube langsung.
- Cara akses YouTube: API key lewat pengaturan lingkungan (Network secrets, host www.googleapis.com, header x-goog-api-key, prefix kosong). Atau pengguna mengekspor data secara manual.
- Benchmark struktur: Inside Job (Oscar; lima bagian: How We Got Here, The Bubble, The Crisis, Accountability, Where We Are Now; sekitar 108 menit) sebagai acuan utama. Money as Debt: klaim 40 juta views belum terverifikasi, ada masalah akurasi. Di Balik Kilang dan Ferry Irwandi: data belum lengkap.
- Estimasi kredit film 35–40 menit: dasar sekitar 1.400–2.400 kredit; dengan revisi 2x sekitar 3.200–5.300 kredit. Saldo saat rancangan dibuat sekitar 605 kredit. Harga sekitar $0,01 per kredit (5.000 kredit sekitar $50, atau sekitar Rp800.000 dengan asumsi kurs Rp16.000 per dolar).
- Riset ini belum tersimpan di repo. Usulkan diff ke content/riset_video_bulanan.md bila pengguna setuju.

LANGKAH BERIKUTNYA (urut):
0. Pastikan scratchpad lama masih ada. Jika tidak, pulihkan narasi dan aset dari Creative Claw dan dari repo sebelum langkah 1.
1. Kerjakan perbaikan 1–5 di atas, masing-masing dengan diff dan persetujuan.
2. Tangani narasi Hari 7 (usulkan pilihan ke pengguna), normalisasi ulang Hari 6 dan 7, lalu buat wordstarts.
3. Pilih latar Hari 6 dan Hari 7 (sesuai aturan 5+ gambar, 3 lisensi bebas + 3 AI untuk 6 gambar), tunjukkan ke pengguna untuk persetujuan sebelum membuat gambar AI.
4. Render, tinjauan Opus, lalu tunjukkan ke pengguna.
5. Tanyakan persetujuan sebelum unggah private.
6. Setelah kalender berjalan, lanjutkan riset krismon di YouTube (judul, views, umur, kanal, durasi) dan rancangan video bulanan.

Mulai dengan membaca file-file di atas, lalu beri tahu saya ringkasan status dan langkah pertama yang akan kamu kerjakan. Jangan mengubah apa pun sebelum saya setujui.
```
