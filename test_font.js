const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:3000/premium-components.html', { waitUntil: 'networkidle' });

  // Wait a bit just in case
  await page.waitForTimeout(1000);

  const bodyStyle = await page.evaluate(() => {
    return window.getComputedStyle(document.body).fontFamily;
  });
  console.log(`Computed font: ${bodyStyle}`);

  const classList = await page.evaluate(() => {
    return document.body.className;
  });
  console.log(`Body classes: ${classList}`);

  await browser.close();
})();
