const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/index.html');
  for (const t of [2, 7, 12]) {
    await p.evaluate((x) => window.renderAt(x), t);
    await p.screenshot({ path: __dirname + '/frame_' + t + '.png' });
  }
  console.log('durasi total', await p.evaluate(() => window.totalDurasi));
  await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
