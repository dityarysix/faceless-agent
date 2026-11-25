# Pra-produksi: film bulanan 1

Status: pra-produksi. Belum ada naskah, narasi, atau render. Jadwal rilis belum ditetapkan.

## Lingkup
- Format: film bulanan, 35–45 menit (maksimal 45). Terpisah dari video mingguan 10–15 menit (Rabu 16.00 WIB).
- Topik kandidat: krisis moneter 1998 (krismon), dengan sudut ekonomi. Belum diputuskan.
- Tanggal rilis: belum ditentukan. Jadwal film bulanan dibatalkan (keputusan pengguna, 25 November 2026).

## Riset topik (ringkasan)
- Sampel YouTube: 8 pencarian dan 97 video, diurutkan views. Ini sampel, bukan data lengkap.
- Krismon: permintaan Indonesia terbukti dan konsisten. Contoh video ekonomi berbahasa Indonesia: "Benarkah IMF Menjebak Indonesia" (3,1 juta views, sekitar 103 ribu views per bulan), dan "Memahami 1998 dalam satu jam" (4,7 juta views, sekitar 174 ribu per bulan, tetapi mencakup sisi politik).
- Great Depression: permintaan global tinggi, tetapi bukti berbahasa Indonesia tipis.
- Tech/AI bubble: kecepatan views tinggi pada 2026, hampir semuanya berbahasa Inggris.
- Tinjauan Opus atas riset pertama: REQUEST CHANGES. Perbaikan dilakukan, dan kesimpulan krismon sebagai rekomendasi sementara masih dengan catatan.

## Jam tayang
- Jadwal harian: short setiap hari 06.00 WIB. Mingguan: Rabu 16.00 WIB.
- Usulan Jumat 19.00 WIB (pekan terakhir setiap bulan) dicabut bersama pembatalan jadwal.
- Pertimbangan libur: Jumat 25 Desember 2026 (Hari Natal) dan Jumat 1 Januari 2027 (Tahun Baru) berada di periode libur. Pengguna ingin mengejar penonton libur akhir tahun. Tidak ada bukti data bahwa pola ini kuat di kanal ini.

## Estimasi biaya (Rp18.325/USD, sekitar Rp174 per kredit)
| Komponen | Rendah | Menengah | Tinggi |
|---|---|---|---|
| Narasi ElevenLabs v4 (±41.000 karakter), dengan pengambilan ulang 1x / 1,5x / 2x | 860 | 1.290 | 1.720 |
| Motion graphics lokal (Chrome + ffmpeg) | 0 | 0 | 0 |
| `render_html_video` satu render penuh (belum diuji) | 0 | 0 | 360 |
| Pembuka dan judul bab (`generate_html_video`, 1–2 turn) | 200 | 300 | 400 |
| Ilustrasi AI 15–25 gambar × 12 kredit | 180 | 240 | 300 |
| Pilot 3–5 menit | 0 | 150 | 250 |
| Musik dan SFX | belum diestimasi | belum diestimasi | belum diestimasi |
| Total (kredit) | 1.240 | 1.980 | 3.030 |
| Total (rupiah, perkiraan) | ≈ Rp216.000 | ≈ Rp346.000 | ≈ Rp529.000 |

- Saldo saat catatan dibuat: 605 kredit.
- Paket: 1.000 kredit = $10 (≈ Rp183.000). 5.000 kredit = $50 untuk 5.250 kredit (≈ Rp916.000).
- Video mingguan memakai narasi dan gambar juga: perkiraan sekitar 600 kredit per video (≈ Rp105.000), dan empat video per bulan sekitar 2.400 kredit. Ini perlu masuk ke anggaran bulanan.
- Estimasi belum terbukti. Perlu pilot untuk memastikan.

## Pendekatan produksi
- Visual: templat HTML/JS buatan sendiri, digerakkan per frame dari timestamp kata, dirender lokal dengan Chrome headless dan ffmpeg per bab. Tidak memakai kredit.
- Pembuka dan judul bab: `generate_html_video`, 1–2 turn saja.
- Narasi: ElevenLabs v4 per bab, dengan kamus pelafalan untuk singkatan dan angka.
- Ilustrasi: sebagian besar grafik data, peta, timeline, dan tipografi. Gambar AI hanya ilustrasi non-fotorealistis dan diberi label.
- Musik dan SFX: belum diputuskan dan belum diestimasi.

## Risiko lisensi
- Foto 1998 (kerusuhan, demo, tokoh) umumnya milik kantor berita dan bukan CC0. Jangan pakai berkas Wikimedia tanpa cek riwayat lisensi.
- Koleksi museum CC0 (CMA, AIC) tidak memuat foto 1998.
- Gambar AI yang mirip foto asli bisa menyesatkan dan perlu pengungkapan konten sintetis di YouTube.
- Setiap berkas CC BY-SA harus dicatat lengkap: judul, pembuat, lisensi, tautan, dan perubahan.
- Log aset harus disimpan di repo. Log lama di scratchpad sudah hilang.

## Masalah yang sudah diketahui
- `tools/render_short.py` masih menunjuk ke scratchpad sesi lama (baris ROOT). Belum diperbaiki.
- Log aset Hari 4–5 hilang dan belum direkonstruksi.
- Estimasi render `render_html_video` dan batas durasinya belum diuji.
- Waktu render lokal 45 menit diperkirakan 1–2,5 jam, belum diukur.

## Keputusan yang masih terbuka
1. Topik final: krismon 1998 atau yang lain.
2. Tanggal dan jam rilis pertama.
3. Persetujuan pilot 3–5 menit dengan saldo yang ada.
4. Pembelian kredit dan jumlahnya.
5. Pendekatan lisensi visual, dan apakah musik perlu diestimasi.

## Langkah berikutnya (usulan)
1. Tetapkan topik dan tanggal rilis pertama.
2. Jalankan pilot 3–5 menit untuk mengukur biaya nyata dan waktu render.
3. Perbaiki `render_short.py` dan simpan log aset di repo.
4. Hitung ulang estimasi setelah pilot, lalu putuskan pembelian kredit.

## Keputusan pra-produksi

### Disetujui
- Topik besar: Krisis Moneter 1998 (krismon).
- Kebijakan visual (disetujui pengguna, 25 November 2026): tanpa foto arsip 1998, dan tanpa gambar AI yang mirip foto asli. Visual utama berupa grafik data, peta, timeline, dan tipografi. Gambar AI hanya untuk ilustrasi non-fotorealistis dan diberi label.

### Usulan (belum disetujui)
- Pertanyaan sentral: "Siapa yang menang dan siapa yang kalah dari Krisis 1998, dan apa yang bisa kita pelajari dari kisah mereka?"
- Format tokoh: pasangan tokoh komposit fiktif dari kelompok sosial yang sama, yang diberi label sebagai ilustrasi berdasarkan fakta. Contoh: dua pengusaha dalam bidang yang sama. Yang satu menerima pendapatan dolar (menang saat rupiah jatuh), yang satu menerima pendapatan rupiah (kalah). Perbedaan nasib dijelaskan oleh jenis pendapatan dan utang, bukan oleh karakter.
- Tidak memakai nama pribadi nyata. Setiap fakta yang dipakai tokoh bersumber sesuai aturan sumber, termasuk klaim bahwa pendapatan dolar diuntungkan oleh depresiasi rupiah.
- Batas cakupan: fokus pada ekonomi dan keuangan. Politik 1998 hanya sebagai konteks. Kerusuhan Mei 1998 tidak menjadi adegan utama, dan korban tidak dijadikan objek visual.
- Sensitivitas: nama pejabat dan tokoh hidup disebut hanya dengan rujukan kebijakan publik atau sumber primer. Klaim sebab-akibat harus bersumber.

### Belum diputuskan
- Sensitivitas: persetujuan usulan di atas, atau revisi.
- Plafon kredit untuk film ini.
