const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const puppeteer = require("puppeteer");

const root = path.resolve(__dirname, "..");
const output = "/Users/stareudy/Library/Mobile Documents/com~apple~CloudDocs/STDT Outputs/Tuvok/hero_board_full.png";
const types = {
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".css": "text/css",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
  ".ttf": "font/ttf",
};

async function main() {
  const server = http.createServer((req, res) => {
    const pathname = decodeURIComponent(new URL(req.url, "http://127.0.0.1").pathname);
    const file = path.resolve(root, `.${pathname}`);

    if (!file.startsWith(root + path.sep)) {
      res.writeHead(403).end("Forbidden");
      return;
    }

    fs.readFile(file, (err, data) => {
      if (err) {
        res.writeHead(404).end("Not found");
        return;
      }
      res.writeHead(200, {
        "Content-Type": types[path.extname(file).toLowerCase()] || "application/octet-stream",
      });
      res.end(data);
    });
  });

  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  const browser = await puppeteer.launch({ headless: true });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 4500, height: 2700, deviceScaleFactor: 1 });
    await page.goto(
      `http://127.0.0.1:${server.address().port}/Heroes/Tuvok/hero_board.svg`,
      { waitUntil: "networkidle0" }
    );

    await page.evaluate(async () => {
      await document.fonts.ready;
      const svg = document.querySelector("svg");
      if (!svg) throw new Error("SVG root not found");
      svg.setAttribute("width", "4500px");
      svg.setAttribute("height", "2700px");
    });

    fs.mkdirSync(path.dirname(output), { recursive: true });
    await page.screenshot({
      path: output,
      clip: { x: 0, y: 0, width: 4500, height: 2700 },
      omitBackground: true,
    });
    console.log(`Saved ${output} (4500 × 2700 px)`);
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
