// Renderer ringan: menampilkan adegan sesuai waktu t (detik).
// Adegan dibaca dari window.SCENES: { mulai, selesai, jenis, judul, nilai, tanggal, teks, sumber, label }.
(function () {
  const panggung = document.getElementById("panggung");
  const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function buatAdegan(a, i) {
    const el = document.createElement("div");
    el.className = "scene";
    el.dataset.idx = i;
    let isi = "";
    if (a.jenis === "kartu_angka") {
      isi = `<div class="kartu"><div class="angka">${esc(a.nilai)}</div><div class="tanggal">${esc(a.tanggal)}</div><div class="garis"></div><div class="teks">${esc(a.teks)}</div></div>`;
    } else if (a.jenis === "kartu_teks") {
      isi = `<div class="kartu"><div class="teks">${esc(a.teks)}</div></div>`;
    } else if (a.jenis === "tipografi") {
      isi = `<div class="kartu"><div class="teks">${esc(a.teks)}</div></div>`;
    } else {
      isi = `<div class="kartu"><div class="teks">${esc(a.teks)}</div></div>`;
    }
    const judul = a.judul ? `<div class="judul">${esc(a.judul)}</div>` : "";
    const sumber = a.sumber ? `<div class="sumber">Sumber: ${esc(a.sumber)}</div>` : "";
    const label = a.label ? `<div class="label">${esc(a.label)}</div>` : "";
    el.innerHTML = judul + isi + sumber + label;
    return el;
  }

  const adegan = (window.SCENES || []);
  adegan.forEach((a, i) => panggung.appendChild(buatAdegan(a, i)));
  window.totalDurasi = adegan.length ? Math.max(...adegan.map((a) => a.selesai)) : 0;

  // Dipanggil per frame oleh perekam: tampilkan adegan yang aktif pada waktu t.
  window.renderAt = function (t) {
    const els = panggung.querySelectorAll(".scene");
    els.forEach((el) => {
      const a = adegan[Number(el.dataset.idx)];
      el.classList.toggle("on", t >= a.mulai && t < a.selesai);
    });
    return true;
  };
})();
