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

### Tokoh 1: pengusaha dengan pendapatan dolar (kalah)
- Latar: pengusaha ekspor atau jasa yang menerima pendapatan dalam dolar. Secara umum, depresiasi rupiah menguntungkan kelompok ini, tetapi keuntungannya bergantung pada utang dan biaya.
- Konflik: pendapatan dolar tidak sama dengan lindung nilai. Jika utang dalam dolar lebih besar dari pendapatan, atau bahan baku dan kredit tiba-tiba hilang, usaha tetap bisa kalah.
- Yang harus diverifikasi sebelum naskah: data pendapatan dan utang dolar kelompok ekspor-jasa pada 1997–98, dan dampak penarikan kredit bank terhadap usaha kecil dan menengah. Sumber dan status: belum dicari.

### Tokoh 2: pengusaha dengan pendapatan rupiah (kalah)
- Latar: pengusaha yang melayani pasar domestik dan membayar bahan baku atau utang dalam rupiah atau dolar.
- Konflik: harga bahan baku naik, daya beli turun, dan kredit bank macet. Kalah karena biaya naik lebih cepat daripada pendapatan.
- Yang harus diverifikasi: data inflasi dan daya beli 1998, serta dampak kredit macet terhadap usaha domestik. Sumber dan status: belum dicari. Angka inflasi puncak sudah dalam ledger (C4), dengan koreksi ke 82,4% pada September 1998 menurut BI.

### Tokoh 3: pemilik bank penerima BLBI (menang)
- Makna dalam cerita: kelompok yang menerima bantuan likuiditas dari Bank Indonesia. Kewajiban BLBI mereka kemudian dihapus lewat klausul *Release and Discharge* yang dikeluarkan BPPN, sehingga pemerintah tidak menuntut pidana atas pelanggaran bank (Muliana, *Jurist-Diction* 2024, hal. 360).
- Temuan audit: BPK 2000 mencatat potensi kerugian negara sekitar Rp138,442 triliun dari penyaluran sekitar Rp144,536 triliun ke 48 bank per 29 Januari 1999. Sumber yang terbaca: Hukumonline (cuplikan) dan CNBC Indonesia (2021, mengutip Kemenkeu). Dokumen BPK asli belum bisa diakses (403).
- Status hukum: Muliana (2024) membahas kasus korupsi BLBI melalui putusan pengadilan negeri hingga kasasi. Hanya hal. 1–5 yang sudah dibaca. Hal. 6–16 belum dibaca, dan putusan akhirnya harus diverifikasi sebelum naskah.
- Rumusan untuk naskah: "Kewajiban BLBI dihapus lewat klausul *Release and Discharge*, dan audit BPK mencatat potensi kerugian negara sekitar Rp138 triliun."
- Larangan: jangan menulis "tidak membayar dan merugikan negara" sebagai fakta mutlak. Itu klaim hukum yang perlu putusan atau sumber resmi.

### Sumber tambahan yang perlu dicari
- Dokumen BPK 2000 (bpk.go.id, belum bisa diakses).
- Muliana (2024), hal. 6–16, untuk putusan pengadilan dan kasasi.
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
- Format tokoh: pasangan tokoh komposit fiktif dari kelompok sosial yang sama, yang diberi label sebagai ilustrasi berdasarkan fakta. Contoh: dua pengusaha dalam bidang yang sama. Yang satu menerima pendapatan dolar (menang saat rupiah jatuh), yang satu menerima pendapatan rupiah (kalah). Perbedaan nasib dijelaskan oleh jenis pendapatan dan utang, bukan oleh karakter.
- Tidak memakai nama pribadi nyata. Setiap fakta yang dipakai tokoh bersumber sesuai aturan sumber, termasuk klaim bahwa pendapatan dolar diuntungkan oleh depresiasi rupiah.
- Batas cakupan: fokus pada ekonomi dan keuangan. Politik 1998 hanya sebagai konteks. Kerusuhan Mei 1998 tidak menjadi adegan utama, dan korban tidak dijadikan objek visual.
- Sensitivitas: nama pejabat dan tokoh hidup disebut hanya dengan rujukan kebijakan publik atau sumber primer. Klaim sebab-akibat harus bersumber.

### Belum diputuskan
- Sensitivitas: persetujuan usulan di atas, atau revisi.
- Plafon kredit untuk film ini.

## Struktur 40 menit

Durasi target: sekitar 40 menit. Tokoh T1 dan T2 adalah pengusaha komposit fiktif berlabel ilustrasi. T3 adalah mekanisme BLBI, tanpa wajah dan tanpa nama.

| Babak | Menit | Durasi | Isi | Peran tokoh | Visual dan jeda |
|---|---|---|---|---|---|
| 1. Pembuka | 0:00–6:00 | 6:00 | Hook dan pertanyaan sentral (0:00–0:30). Oil boom dan Pakto 1988 (0:30–2:30). Memasuki krisis: rupiah melemah, utang dolar jangka pendek tanpa lindung nilai (2:30–4:00). Perkenalan T1 dan T2 secara lengkap (4:00–6:00). | T1 dan T2 diperkenalkan dengan pembeda nasib sebelum krisis. T3 belum disebut. | Grafik minyak dunia, penerimaan migas (Pelita III 66,9%), dan utang luar negeri. Jeda di 6:00. |
| 2. Rupiah Runtuh | 6:00–13:30 | 7:30 | Agustus 1997: fasilitas likuiditas BI mulai. 3 September: instruksi kepada pemerintah dan BI. Rupiah melemah lebih dari 30% dalam tiga bulan. 1 November: 16 bank ditutup. Akhir 1997: SBPUK Rp36,5 triliun kepada 28 bank. | T1 menghadapi kredit dan pembiayaan dagang macet. T2 kehilangan akses kredit. T3 diperkenalkan sebagai mekanisme respons. | Peta waktu Agustus–Desember 1997. Kartu angka 16 bank. Jeda di 13:30. |
| 3. Puncak 1998 | 13:30–20:30 | 7:00 | IMF stand-by SDR 7,3 miliar tidak langsung menenangkan pasar. Rupiah menyentuh Rp16.500 pada pertengahan Juni. Inflasi tahunan puncak 82,4% (September). PDB −13,7%. Tabungan ditarik dari bank. | Usaha T1 dan T2 runtuh. | Grafik kurs dan inflasi berdampingan. Kartu PDB. Jeda di 20:30. |
| 4. Mesin BLBI | 20:30–28:00 | 7:30 | Mekanisme BLBI: bantuan likuiditas, klausul *Release and Discharge*, dan pelunasan ke BI. Nilai sekitar Rp148 triliun (revisi Rp144,54 triliun, Februari 1999). Potensi kerugian negara dalam audit BPK 2000 sekitar Rp138 triliun. Pertanyaan "siapa menang" dijawab sebagai mekanisme. | T1 dan T2 menagih harapan. T3 dijelaskan sebagai kelompok penerima yang kewajibannya dihapus. | Diagram aliran dana BLBI. Peta mekanisme. Jeda di 28:00. |
| 5. Pembenahan dan Tagihan | 28:00–35:00 | 7:00 | BPPN dibubarkan 2004. LPS berdiri 2004–2005. IMF dilunasi 2006 (pokok SDR 11,1 miliar, bunga SDR 2,1 miliar). BLBI ke BI Rp218,3 triliun (2026), tetapi penagihan obligor belum selesai. | Nasib akhir T1 dan T2 dalam satu adegan masing-masing. T3 tetap terbuka. | Timeline 2004–2026. Kartu angka pelunasan. Jeda di 35:00. |
| 6. Penutup | 35:00–40:00 | 5:00 | Jawaban pertanyaan sentral dengan tiga kalimat: IMF, BLBI, dan pembenahan. Pertanyaan terbuka: penagihan belum tuntas. | T1 dan T2 sebagai bukti. T3 sebagai fakta yang belum selesai. | Layar tipografi penuh untuk tiga kalimat penutup. |
| Total | | 40:00 | | | |

Catatan:
- Babak 2 memuat satu-satunya perkenalan T3, karena mekanisme BLBI dimulai Agustus 1997.
- Angka yang belum ada di ledger tercantum di treatment. Nasib T1 dan T2 adalah bagian fiktif berlabel ilustrasi.
