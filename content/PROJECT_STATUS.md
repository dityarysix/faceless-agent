# Status proyek: Jejak Menuju Kaya (faceless-agent)

Ringkasan ini untuk sesi baru. Jangan pernah menulis token, secret, atau nilai kredensial apa pun di file ini atau di chat.

## Aturan
- Tampilkan diff sebelum mengubah file. Terapkan hanya setelah disetujui pengguna.
- Jangan posting atau mengunggah video tanpa persetujuan eksplisit pengguna untuk video itu.
- Sumber konten adalah `content/calendar.md`, siklus 28 hari.
- Setiap perubahan file lewat `implementer`, dan ditinjau `reviewer` (Opus) sebelum dilaporkan selesai.

## Status
- **Hari 1:** sudah tayang (diposting manual).
- **Hari 2:** sudah diposting manual di YouTube dan Instagram. Paket ada di `content/hari2/` (branch `hari2-content`): `hari2_v4.mp4`, `PAKET_HARI2.md` (naskah, judul, deskripsi, caption), `render4.py`, `vo_hari2.mp3`.
- **Hari 3:** belum dibuat. Topik di kalender: "Kisah kekayaan: kisah yang dimulai dari Rp10.000 sehari yang dicatat dan ditabung". Video, cerita, dan persetujuan dari pengguna masih menunggu. Jadwal yang diinginkan: 26 November 2026, 06.00 WIB (= 25 November 2026, 23.00 UTC).

## YouTube (sudah siap)
- Project Google Cloud: `faceless-agent-yt`. YouTube Data API v3 aktif. Scope: `youtube.upload`.
- Consent screen: **In production**. Privacy policy: `https://github.com/dityarysix/faceless-agent/blob/privacy-policy/PRIVACY.md`.
- Project belum diverifikasi Google. Video dari API kemungkinan hanya bisa diunggah sebagai **private** sampai audit selesai. Jadwal publik perlu dicek ulang setelah audit.
- Environment: **faceless-agent (YouTube)**. Variabel yang dibutuhkan: `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`. Hanya namanya yang boleh diperiksa, nilainya tidak.
- Tes upload sudah berhasil dari awal sampai selesai (video tes private, lalu dihapus manual oleh pengguna). Tidak ada video tes yang tersisa.

## Instagram (dilewati)
- Pengguna mengunggah manual. Tidak ada integrasi Instagram API yang disiapkan.

## Catatan teknis
- Hook "unpushed commits" kadang keliru karena ref pelacak lokal `origin/<branch>` belum dibuat. Kalau muncul, cek `git ls-remote origin <branch>` dan bandingkan dengan `git rev-parse HEAD`. Jika sama, buat ref dengan `git fetch origin <branch>:refs/remotes/origin/<branch>`.
- Creative Claw untuk voice-over (Hope, ElevenLabs, `language_code: id`). Host CDN Creative Claw sudah diizinkan di environment.
