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

## Tokoh

Pertanyaan sentral: "Siapa yang menang dan siapa yang kalah dari Krisis 1998, dan apa yang bisa kita pelajari dari kisah mereka?"

Ketiga tokoh adalah tokoh komposit fiktif yang diberi label sebagai ilustrasi berdasarkan fakta. Tidak ada nama pribadi nyata. Tokoh ketiga mewakili kelompok dan mekanisme, bukan satu orang.

### Tokoh 1: pengusaha dengan pendapatan dolar
- Latar: pengusaha ekspor atau jasa yang menerima pendapatan dalam dolar. Keuntungan dari depresiasi rupiah belum bersumber dan tidak dipakai di naskah sampai ada baris ledger.
- Konflik: pendapatan dolar tidak sama dengan lindung nilai. Jika utang dalam dolar lebih besar dari pendapatan, atau bahan baku dan kredit tiba-tiba hilang, usaha tetap bisa kalah.
- Yang harus diverifikasi sebelum naskah: data pendapatan dan utang dolar kelompok ekspor-jasa pada 1997–98, dan dampak penarikan kredit bank terhadap usaha kecil dan menengah. Sumber dan status: belum dicari.

### Tokoh 2: pengusaha dengan pendapatan rupiah
- Latar: pengusaha yang melayani pasar domestik dan membayar bahan baku atau utang dalam rupiah atau dolar.
- Konflik: harga bahan baku naik, daya beli turun, dan kredit bank macet. Usahanya tertekan ketika biaya naik lebih cepat daripada pendapatan (alur fiksi).
- Yang harus diverifikasi: data inflasi dan daya beli 1998, serta dampak kredit macet terhadap usaha domestik. Sumber dan status: belum dicari. Angka inflasi puncak sudah dalam ledger (C4): 82,4% pada September 1998.

### Tokoh 3: mekanisme bantuan likuiditas BI (BLBI)
- Makna dalam cerita: mekanisme bantuan likuiditas dari Bank Indonesia dan penerimanya. Dalam sebagian penyelesaian, penerima memperoleh klausul *Release and Discharge* (R-1): tagihan dinyatakan lunas dan pemerintah tidak menuntut pidana atas pelanggaran bank. Kekuatan hukumnya diperdebatkan (R-1).
- Temuan audit: BPK 2000 mencatat potensi kerugian negara sekitar Rp138,442 triliun dari penyaluran sekitar Rp144,536 triliun ke 48 bank per 29 Januari 1999. Sumber yang terbaca: CNBC Indonesia (2021, mengutip Kemenkeu), Tempo, dan Seknas FITRA. Dokumen BPK asli belum bisa diakses (403).
- Status hukum: Muliana (2024) membahas kasus korupsi BLBI melalui putusan pengadilan negeri hingga kasasi. Dibaca langsung oleh pengguna (halaman dikonfirmasi pengguna).
- Rumusan untuk naskah: "Dalam sebagian penyelesaian BLBI, tagihan penerima dinyatakan lunas lewat klausul *Release and Discharge*. Terpisah, audit BPK 2000 mencatat potensi kerugian negara sekitar Rp138 triliun (sumber di layar: Kemenkeu via CNBC Indonesia, 2021)."
- Larangan: jangan menulis "tidak membayar dan merugikan negara" sebagai fakta mutlak. Itu klaim hukum yang perlu putusan atau sumber resmi.

### Sumber tambahan yang perlu dicari
- Dokumen BPK 2000 (bpk.go.id, belum bisa diakses).
- Muliana (2024): halaman dikonfirmasi pengguna.
- Data kredit macet dan kebangkrutan usaha kecil-menengah 1997–98 untuk tokoh 1 dan 2.

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
- Format tokoh: pasangan tokoh komposit fiktif dari kelompok sosial yang sama, yang diberi label sebagai ilustrasi berdasarkan fakta. Contoh: dua pengusaha dalam bidang yang sama. Yang satu menerima pendapatan dolar, yang satu menerima pendapatan rupiah. Perbedaan nasib dijelaskan oleh jenis pendapatan dan utang, bukan oleh karakter.
- Tidak memakai nama pribadi nyata. Setiap fakta yang dipakai tokoh bersumber sesuai aturan sumber, termasuk klaim bahwa pendapatan dolar diuntungkan oleh depresiasi rupiah.
- Batas cakupan: fokus pada ekonomi dan keuangan. Politik 1998 hanya sebagai konteks. Kerusuhan Mei 1998 tidak menjadi adegan utama, dan korban tidak dijadikan objek visual.
- Sensitivitas: nama pejabat dan tokoh hidup disebut hanya dengan rujukan kebijakan publik atau sumber primer. Klaim sebab-akibat harus bersumber.

### Belum diputuskan
- Sensitivitas: persetujuan usulan di atas, atau revisi.
- Plafon kredit untuk film ini.

## Struktur 41 menit 30 detik

Durasi target: sekitar 41–42 menit (peta durasi 41:30). Tokoh T1 dan T2 adalah pengusaha komposit fiktif berlabel ilustrasi. T3 adalah mekanisme BLBI, tanpa wajah dan tanpa nama.

| Babak | Menit | Durasi | Isi | Peran tokoh | Visual dan jeda |
|---|---|---|---|---|---|
| 1. Pembuka | 0:00–6:30 | 6:30 | Hook dan pertanyaan sentral (0:00–0:30). Kenaikan harga minyak (K-1, sumber di layar: Federal Reserve History) dan Pakto 1988 (0:30–2:30). Memasuki krisis: rupiah melemah, pinjaman luar negeri swasta jangka pendek, sebagian besar tanpa lindung nilai (2:30–4:00). Perkenalan T1 dan T2 secara lengkap (4:00–6:30). | T1 dan T2 diperkenalkan dengan pembeda pendapatan sebelum krisis. T3 belum disebut. | Teks dan peta kenaikan harga minyak (tanpa grafik seri), penerimaan migas (Pelita III 66,9%). Jeda di 6:30. |
| 2. Rupiah Runtuh | 6:30–14:00 | 7:30 | Agustus 1997: fasilitas likuiditas BI mulai. 3 September: instruksi kepada Menteri Keuangan dan Gubernur BI (T-5). Rupiah melemah lebih dari 30% dalam tiga bulan. 1 November: 16 bank ditutup. 5 November: persetujuan stand-by IMF (IMF, siaran pers; sumber ditampilkan di layar; belum dicocokkan dengan PDF asli). Akhir 1997: SBPUK Rp36,5 triliun kepada 28 bank. | T1 menghadapi tekanan kredit (alur fiksi). T2 kehilangan akses kredit (alur fiksi, tanpa klaim data). T3 diperkenalkan sebagai mekanisme respons. | Peta waktu Agustus–Desember 1997. Kartu angka 16 bank. Jeda di 14:00. |
| 3. Puncak 1998 | 14:00–21:00 | 7:00 | Rupiah menyentuh Rp16.500 pada pertengahan Juni. Inflasi tahunan puncak 82,4% (September). PDB −13,7%. | Usaha T1 dan T2 runtuh (alur fiksi). | Grafik kurs dan inflasi berdampingan. Kartu PDB. Jeda di 21:00. |
| 4. Mesin BLBI | 21:00–28:30 | 7:30 | Mekanisme BLBI: bantuan likuiditas, klausul *Release and Discharge*, dan pelunasan ke BI. Nilai sekitar Rp148 triliun pada akhir 1998. Potensi kerugian negara dalam audit BPK 2000 sekitar Rp138 triliun (sumber di layar: Kemenkeu via CNBC Indonesia, 2021; audit BPK asli belum dibaca). Pertanyaan "siapa menang" dijawab sebagai mekanisme. | T1 dan T2 menagih harapan. T3 dijelaskan sebagai mekanisme; tagihan sebagian penerima dinyatakan lunas lewat R&D (R-1). | Diagram aliran dana BLBI. Peta mekanisme. Jeda di 28:30. |
| 5. Pembenahan dan Tagihan | 28:30–36:00 | 7:30 | BPPN dibubarkan 2004. LPS berdiri 2004–2005. IMF dilunasi 2006 (pokok SDR 11,1 miliar, bunga dan biaya SDR 2,1 miliar). BLBI ke BI Rp218,3 triliun (2026), tetapi penagihan obligor belum selesai. | Nasib akhir T1 dan T2 dalam satu adegan masing-masing. T3 tetap terbuka. | Timeline 2004–2026. Kartu angka pelunasan dengan sumber di layar untuk P5, P6, P7 (dengan P13), P9, dan P10. Jeda di 36:00. |
| 6. Penutup | 36:00–41:30 | 5:30 | Tiga kalimat fakta (IMF, BLBI, pembenahan; tampilkan sumber di layar untuk P6, P9, P10, P13), lalu pertanyaan terbuka: siapa yang menanggung akibat mekanisme ini, dan siapa yang belum selesai ditagih. | T1 dan T2 sebagai bukti. T3 sebagai fakta yang belum selesai. | Layar tipografi penuh untuk tiga kalimat penutup. |
| Total | | 41:30 | | | |

Catatan:
- Babak 2 memuat satu-satunya perkenalan T3, karena mekanisme BLBI dimulai Agustus 1997.
- Angka tambahan sudah tercatat di ledger (T-1 sampai T-5). Nasib T1 dan T2 adalah bagian fiktif berlabel ilustrasi.
