const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.homemcr.org/theatre');

  const data = await page.evaluate(() => {
    const shows = document.getElementsByClassName('meta-section');
    console.log(shows);
    

    return shows;

  })

  console.log(typeof(data));
  
  await browser.close();
  
  return data;

})();
