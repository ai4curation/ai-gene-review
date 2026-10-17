"""Verify bounded source retries against a real local HTTP service."""

from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import pytest
import requests

from ai_gene_review.tools.build_browser_hierarchies import download_source


@pytest.fixture
def source_server():
    """Serve a transient error, a persistent error, and a missing resource."""
    counts = Counter()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            counts[self.path] += 1
            status = 200
            if self.path == "/missing":
                status = 404
            elif self.path == "/outage" or counts[self.path] < 3:
                status = 503
            self.send_response(status)
            self.end_headers()
            self.wfile.write(b"source content")

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    worker = Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}", counts
    finally:
        server.shutdown()
        server.server_close()
        worker.join()


def test_transient_download_recovers(source_server):
    url, counts = source_server
    assert download_source(url + "/transient", timeout=2) == b"source content"
    assert counts["/transient"] == 3


def test_persistent_download_failure_has_bounded_attempts(source_server):
    url, counts = source_server
    with pytest.raises(requests.RequestException):
        download_source(url + "/outage", timeout=2)
    assert counts["/outage"] == 4


def test_missing_source_is_not_retried(source_server):
    url, counts = source_server
    with pytest.raises(requests.HTTPError):
        download_source(url + "/missing", timeout=2)
    assert counts["/missing"] == 1
