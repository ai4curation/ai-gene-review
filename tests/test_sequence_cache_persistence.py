"""Offline cache-progress and diagnostic regression tests; no upstream calls."""

import http.client
import http.server
import importlib.util
import io
import json
import ssl
import subprocess
import sys
import threading
import urllib.error
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_file(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


manifest_module = load_file("sequence_cache_manifest", ".github/scripts/sequence_cache_manifest.py")
validator = load_file(
    "sequence_cache_validator_under_test",
    "src/ai_gene_review/validation/family_residue_validator.py",
)


@pytest.fixture
def retry_sleeps(monkeypatch):
    """Record retry waits without making offline tests sleep."""
    waits = []
    monkeypatch.setattr(validator.time, "sleep", waits.append)
    return waits


def test_preserve_download_before_later_failure(tmp_path, monkeypatch, retry_sleeps):
    cache_dir = tmp_path / "cache"
    before = manifest_module.manifest(cache_dir)
    calls = []
    errors = []

    def fetch(req, timeout):
        calls.append((req.full_url, timeout))
        if len(calls) == 1:
            return io.BytesIO(json.dumps({
                "sequence": {"value": "MACDEFGHIK"},
                "entryAudit": {"sequenceVersion": 2},
            }).encode())
        error = urllib.error.HTTPError(req.full_url, 503, "unavailable", {}, None)
        errors.append(error)
        raise error

    monkeypatch.setattr(validator.urllib.request, "urlopen", fetch)
    cache = validator.SequenceCache(cache_dir)
    assert cache.get("UniProtKB:P12345") == "MACDEFGHIK"
    with pytest.raises(RuntimeError, match="P54321.*https://rest.uniprot.org/uniprotkb/P54321.json") as caught:
        cache.get("P54321")
    assert isinstance(caught.value.__cause__, urllib.error.HTTPError)
    assert len(calls) == 4  # successful accession, then three failed attempts
    assert retry_sleeps == [2, 4]
    assert caught.value.__cause__ is errors[-1]
    assert not (cache_dir / "P54321.seq").exists()
    assert not (cache_dir / "P54321.sv").exists()
    after = manifest_module.manifest(cache_dir)
    changed, digest = manifest_module.generation(before, after)
    assert changed and len(digest) == 64
    assert set(after) == {"P12345.seq", "P12345.sv"}
    assert (cache_dir / "P12345.seq").read_bytes() == b"MACDEFGHIK"
    # Reusing the saved generation does not fetch or create another generation.
    assert validator.SequenceCache(cache_dir).get("P12345") == "MACDEFGHIK"
    assert len(calls) == 4
    assert manifest_module.generation(after, after)[0] is False


@pytest.mark.parametrize("error", [TimeoutError("read timed out"), urllib.error.URLError("DNS unavailable")])
def test_failure_context_keeps_original_cause(tmp_path, monkeypatch, error, retry_sleeps):
    calls = []

    def fail(req, timeout):
        calls.append((req.full_url, timeout))
        raise error

    monkeypatch.setattr(validator.urllib.request, "urlopen", fail)
    with pytest.raises(RuntimeError, match="Q12345.*https://") as caught:
        validator.SequenceCache(tmp_path).get("Q12345")
    assert caught.value.__cause__ is error
    assert len(calls) == 3 and all(timeout == 60 for _, timeout in calls)
    assert retry_sleeps == [2, 4]
    assert not list(tmp_path.iterdir())


def test_version_optional_or_independent_and_order_stable(tmp_path):
    (tmp_path / "Q12345.seq").write_bytes(b"MACD\n")
    (tmp_path / "P12345.sv").write_bytes(b"3")
    before = manifest_module.manifest(tmp_path)
    assert len(before) == 2
    assert manifest_module.generation({}, before) == manifest_module.generation({}, dict(reversed(list(before.items()))))
    (tmp_path / "Q12345.sv").write_bytes(b"1")
    assert manifest_module.generation(before, manifest_module.manifest(tmp_path))[0]


@pytest.mark.parametrize("name,content", [
    ("Q12345.seq", b""), ("Q12345.seq", b"{error:503}"),
    ("Q12345.seq", b"MACD*"), ("Q12345.sv", b"0"),
    ("Q12345.sv", b"two"), ("unexpected.txt", b"MACD"),
])
def test_invalid_files_are_not_saved(tmp_path, name, content):
    (tmp_path / name).write_bytes(content)
    with pytest.raises(ValueError):
        manifest_module.manifest(tmp_path)
    assert (tmp_path / name).read_bytes() == content


def test_symlinks_are_not_cached(tmp_path):
    target = tmp_path / "target"
    target.mkdir()
    (target / "P12345.seq").write_text("MACD")
    link = tmp_path / "link"
    link.symlink_to(target, target_is_directory=True)
    with pytest.raises(ValueError):
        manifest_module.manifest(link)
    (target / "Q12345.seq").symlink_to(target / "P12345.seq")
    with pytest.raises(ValueError):
        manifest_module.manifest(target)


@pytest.mark.parametrize("after", [{}, {"P12345.seq": "changed"}])
def test_restored_sequence_deletion_or_replacement_refuses_save(after):
    with pytest.raises(ValueError, match="changed or disappeared"):
        manifest_module.generation({"P12345.seq": "original"}, after)


def test_cli_does_not_write_save_outputs_on_invalid_data(tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()
    snapshot = tmp_path / "before.json"
    output = tmp_path / "output"
    script = ROOT / ".github/scripts/sequence_cache_manifest.py"
    common = ["--cache-dir", str(cache), "--snapshot", str(snapshot)]
    subprocess.run([sys.executable, str(script), "before", *common], check=True)
    (cache / "P12345.seq").write_text("error503")
    failed = subprocess.run([sys.executable, str(script), "after", *common, "--output", str(output)], capture_output=True)
    assert failed.returncode != 0 and not output.exists()
    assert b"::warning::Sequence cache saving disabled:" in failed.stdout
    assert (cache / "P12345.seq").read_text() == "error503"


def test_workflow_retains_failure_and_isolates_cache_saving_from_tests():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    steps = workflow["jobs"]["validation"]["steps"]
    by_name = {step["name"]: step for step in steps}
    family = by_name["Validate family reviews (scoped)"]
    assert family["run"] == "just validate-families"
    assert "continue-on-error" not in family
    after = by_name["Inspect downloaded UniProt sequences"]
    save = by_name["Save downloaded UniProt sequences"]
    assert "!cancelled()" in after["if"] and "before.outcome == 'success'" in after["if"]
    assert "!cancelled()" in save["if"] and "after.outcome == 'success'" in save["if"]
    assert "outputs.changed == 'true'" in save["if"]
    assert save["uses"] == "actions/cache/save@v6"
    assert "outputs.digest" in save["with"]["key"]
    assert steps.index(family) < steps.index(after) < steps.index(save)
    suite_steps = workflow["jobs"]["suite"]["steps"]
    assert not any(step.get("run") == "just test" for step in steps)
    assert any(step.get("run") == "just test" for step in suite_steps)
    # Test fixtures may mutate restored data; only the validation runner saves it.
    for step in suite_steps:
        if step.get("uses", "").startswith("actions/cache"):
            assert step["uses"] == "actions/cache/restore@v6"
    restore = by_name["Restore UniProt sequences"]
    assert restore["uses"] == "actions/cache/restore@v6"
    assert restore["if"] == "github.event_name != 'schedule' && github.event_name != 'workflow_dispatch'"
    # Cold full passes still snapshot an empty directory and save valid progress.
    assert "if" not in by_name["Snapshot restored UniProt sequences"]
    assert "event_name" not in after["if"] and "event_name" not in save["if"]
    assert restore["with"]["path"] == save["with"]["path"] == ".cache/uniprot_seq"
    assert "uniprot-seq-${{ runner.os }}-" in restore["with"]["restore-keys"]


@pytest.mark.parametrize("name", ["P12345.seq", "unexpected%file\r\n::error::injected.txt"])
def test_before_refusal_warns_without_changing_files_or_outputs(tmp_path, name):
    cache = tmp_path / "cache"
    cache.mkdir()
    invalid = cache / name
    invalid.write_bytes(b"")
    snapshot = tmp_path / "before.json"
    output = tmp_path / "output"
    script = ROOT / ".github/scripts/sequence_cache_manifest.py"
    failed = subprocess.run([
        sys.executable, str(script), "before", "--cache-dir", str(cache),
        "--snapshot", str(snapshot), "--output", str(output),
    ], capture_output=True, text=True)
    assert failed.returncode != 0
    assert not snapshot.exists() and not output.exists()
    assert list(cache.iterdir()) == [invalid] and invalid.read_bytes() == b""
    assert failed.stdout.startswith("::warning::Sequence cache saving disabled:")
    assert len(failed.stdout.splitlines()) == 1
    assert failed.stderr == ""  # no unescaped filename in a traceback
    if "%" in name:
        assert "unexpected%25file%0D%0A::error::injected.txt" in failed.stdout


@pytest.fixture
def uniprot_server(monkeypatch):
    """Exercise real urllib against deterministic local HTTP responses."""
    @contextmanager
    def serve(responses):
        requests = []

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                index = len(requests)
                requests.append((self.path, self.headers.get("User-Agent")))
                if index >= len(responses):
                    self.send_error(500, "unexpected extra request")
                    return
                status, body, declared_length = responses[index]
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(
                    len(body) if declared_length is None else declared_length
                ))
                self.end_headers()
                self.wfile.write(body)
                self.wfile.flush()
                self.close_connection = True

            def log_message(self, format, *args):
                pass

        with http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
            thread = threading.Thread(
                target=server.serve_forever, kwargs={"poll_interval": 0.01}, daemon=True
            )
            thread.start()
            url = f"http://127.0.0.1:{server.server_port}/uniprotkb/{{acc}}.json"
            monkeypatch.setattr(validator, "UNIPROT_JSON", url)
            try:
                yield requests, url
            finally:
                server.shutdown()
                thread.join(timeout=5)
                assert not thread.is_alive()
    return serve


VALID_RECORD = b'{"sequence":{"value":"MACD"},"entryAudit":{"sequenceVersion":7}}'


@pytest.mark.parametrize("status", [408, 429, 500, 502, 503, 504])
def test_transient_http_recovers_and_populates_cache(tmp_path, uniprot_server, status):
    with uniprot_server([(status, b"temporary failure", None), (200, VALID_RECORD, None)]) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        assert cache.get("P12345") == "MACD"
        assert cache.sequence_version("P12345") == 7
        assert requests == [("/uniprotkb/P12345.json", "ai-gene-review")] * 2
        assert (tmp_path / "P12345.seq").read_text() == "MACD"
        assert (tmp_path / "P12345.sv").read_text() == "7"
        assert cache.get("P12345") == "MACD"
        assert validator.SequenceCache(tmp_path).get("P12345") == "MACD"
        assert validator.SequenceCache(tmp_path).sequence_version("P12345") == 7
        assert len(requests) == 2


def test_transient_http_exhaustion_preserves_final_cause(tmp_path, uniprot_server):
    with uniprot_server([(503, b"first", None), (503, b"second", None), (504, b"final", None)]) as (requests, url):
        with pytest.raises(RuntimeError, match="P12345.*http://127.0.0.1") as caught:
            validator.SequenceCache(tmp_path).get("P12345")
        cause = caught.value.__cause__
        assert isinstance(cause, urllib.error.HTTPError)
        assert cause.code == 504 and cause.url == url.format(acc="P12345")
        try:
            assert cause.read() == b"final"
        finally:
            cause.close()
        assert len(requests) == 3
        assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("status", [400, 401, 403, 404, 501])
def test_permanent_http_failure_is_not_retried(tmp_path, uniprot_server, status):
    with uniprot_server([(status, b"permanent failure", None)]) as (requests, _):
        with pytest.raises(RuntimeError, match="P12345.*http://127.0.0.1") as caught:
            validator.SequenceCache(tmp_path).get("P12345")
        cause = caught.value.__cause__
        assert isinstance(cause, urllib.error.HTTPError) and cause.code == status
        cause.close()
        assert len(requests) == 1
        assert not list(tmp_path.iterdir())


def test_invalid_json_fails_without_retry_or_cache(tmp_path, uniprot_server):
    with uniprot_server([(200, b"<html>not JSON</html>", None)]) as (requests, _):
        with pytest.raises(RuntimeError, match="P12345.*http://127.0.0.1") as caught:
            validator.SequenceCache(tmp_path).get("P12345")
        assert isinstance(caught.value.__cause__, json.JSONDecodeError)
        assert len(requests) == 1
        assert not list(tmp_path.iterdir())


def test_truncated_response_recovers(tmp_path, uniprot_server):
    with uniprot_server([(200, b'{"sequence":', 100), (200, VALID_RECORD, None)]) as (requests, _):
        assert validator.SequenceCache(tmp_path).get("P12345") == "MACD"
        assert len(requests) == 2
        assert (tmp_path / "P12345.seq").read_text() == "MACD"
        assert (tmp_path / "P12345.sv").read_text() == "7"


def test_cached_sequence_stays_offline_and_version_fetch_retries(tmp_path, uniprot_server):
    (tmp_path / "P12345.seq").write_bytes(b"MACD\n")
    with uniprot_server([(503, b"temporary", None), (200, VALID_RECORD, None)]) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        assert cache.get("P12345") == "MACD"
        assert requests == []
        assert cache.sequence_version("P12345") == 7
        assert len(requests) == 2
        assert (tmp_path / "P12345.seq").read_bytes() == b"MACD\n"
        assert validator.SequenceCache(tmp_path).sequence_version("P12345") == 7
        assert len(requests) == 2


@pytest.mark.parametrize("error, retry", [
    (TimeoutError("read timed out"), True),
    (ConnectionResetError("connection reset"), True),
    (http.client.IncompleteRead(b"partial", 100), True),
    (urllib.error.URLError("DNS unavailable"), True),
    (ssl.SSLCertVerificationError("certificate invalid"), False),
    (urllib.error.URLError(ssl.SSLCertVerificationError("certificate invalid")), False),
    (PermissionError("not a transient network failure"), False),
])
def test_network_exception_classification(error, retry):
    assert validator._retryable_uniprot_error(error) is retry
