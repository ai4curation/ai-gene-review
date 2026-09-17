"""Real-browser transport checks; run with pytest -m integration after playwright install chromium."""

import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import pytest
from playwright.sync_api import sync_playwright

from ai_gene_review.export.browser_payload import encode_browser_data_js
from ai_gene_review.tools.pages_compaction import compact_browser_data, compact_gene_page

pytestmark = pytest.mark.integration


@pytest.mark.parametrize('content_encoding', [False, True])
def test_loaders_accept_raw_and_browser_decoded_gzip(tmp_path, content_encoding):
    content = '<p>Supporting evidence with λ and exact spacing.</p>' * 100
    gene = tmp_path / 'gene.html'
    gene.write_text('<html><body><h1>ABC</h1><div class="markdown-content">' + content + '</div></body></html>')
    compact_gene_page(tmp_path, gene)
    app = tmp_path / 'app'
    app.mkdir()
    rows = [{'gene_symbol': 'λABC', '__proto__': 'safe', 'negated': False}] * 100
    (app / 'data.js').write_text(encode_browser_data_js(rows))
    (app / 'index.html').write_text('<html><body><script src="data.js"></script></body></html>')
    compact_browser_data(tmp_path)

    class Handler(SimpleHTTPRequestHandler):
        def end_headers(self):
            if content_encoding and self.path.endswith('.gz'):
                self.send_header('Content-Encoding', 'gzip')
            super().end_headers()

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Handler, directory=str(tmp_path)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                page = browser.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                base = f'http://127.0.0.1:{server.server_port}'
                page.goto(base + '/gene.html')
                page.evaluate('window.pagesContentReady')
                assert page.locator('.markdown-content').inner_html() == content
                page.goto(base + '/app/index.html')
                page.wait_for_function('window.searchData !== undefined')
                assert json.loads(page.evaluate('JSON.stringify(window.searchData)')) == rows
                assert errors == []
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
