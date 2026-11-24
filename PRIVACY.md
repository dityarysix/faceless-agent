# Kebijakan Privasi: faceless-agent

Aplikasi ini digunakan oleh pemilik channel YouTube untuk mengunggah video pendek ke channelnya sendiri.

## Data yang digunakan
- Token OAuth Google (client ID, client secret, dan refresh token) yang diberikan pemilik channel.
- Hanya izin `youtube.upload` yang diminta, untuk mengunggah video.

## Penggunaan data
- Token hanya dipakai untuk mengunggah video ke channel pemilik.
- Aplikasi tidak mengumpulkan data pengguna lain, tidak menjual data, dan tidak membagikannya ke pihak ketiga.

## Penyimpanan
- Token disimpan sebagai variabel environment di layanan yang dipakai pemilik channel. Hanya pemilik yang bisa mengaksesnya.

## Penghapusan akses
- Pemilik dapat mencabut akses kapan saja di https://myaccount.google.com/permissions, atau dengan menghapus client OAuth di Google Cloud Console.

## Kontak
- Pertanyaan tentang kebijakan ini bisa diajukan lewat issue di https://github.com/dityarysix/faceless-agent/issues.
