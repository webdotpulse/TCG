const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const testUrl = async (url, name) => {
    console.log(`Testing ${name} at ${url}`);
    await page.goto(url, { waitUntil: 'networkidle' });

    // Take a screenshot
    await page.screenshot({ path: `${name}.png`, fullPage: true });

    // Check for font
    const fontFamily = await page.evaluate(() => {
      return window.getComputedStyle(document.body).fontFamily;
    });
    console.log(`Body font family for ${name}: ${fontFamily}`);

    // Check for badges
    const badgesText = await page.evaluate(() => {
        const els = Array.from(document.querySelectorAll('.fas.fa-shield-alt, .fas.fa-globe-europe'));
        return els.map(el => el.parentElement.textContent.trim());
    });
    console.log(`Badges found in ${name}: ${badgesText}`);
  }

  try {
      await testUrl('http://localhost:3000/premium-components.html', 'premium-components');
      await testUrl('http://localhost:3000/faq.html', 'faq');
      await testUrl('http://localhost:3000/knowledge-base.html', 'knowledge-base');
      await testUrl('http://localhost:3000/jobs.html', 'jobs');
  } catch(e) {
      console.error("Test failed", e);
  } finally {
      await browser.close();
  }
})();
