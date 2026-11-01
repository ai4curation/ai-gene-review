"""Offline cache-progress and diagnostic regression tests; no upstream calls."""

import http.client
import importlib.util
import io
import json
import subprocess
import sys
import urllib.error
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


@pytest.fixture(autouse=True)
def no_backoff_sleep(monkeypatch):
    monkeypatch.setattr(validator, "_sleep", lambda _seconds: None)


ATTEMPTS = len(validator.FETCH_BACKOFF_SECONDS) + 1


def test_preserve_download_before_later_failure(tmp_path, monkeypatch):
    cache_dir = tmp_path / "cache"
    before = manifest_module.manifest(cache_dir)
    calls = []

    def fetch(req, timeout):
        calls.append((req.full_url, timeout))
        if len(calls) == 1:
            return io.BytesIO(json.dumps({
                "sequence": {"value": "MACDEFGHIK"},
                "entryAudit": {"sequenceVersion": 2},
            }).encode())
        raise urllib.error.HTTPError(req.full_url, 503, "unavailable", {}, None)

    monkeypatch.setattr(validator.urllib.request, "urlopen", fetch)
    cache = validator.SequenceCache(cache_dir)
    assert cache.get("UniProtKB:P12345") == "MACDEFGHIK"
    with pytest.raises(RuntimeError, match="P54321.*https://rest.uniprot.org/uniprotkb/P54321.json") as caught:
        cache.get("P54321")
    assert isinstance(caught.value.__cause__, urllib.error.HTTPError)
    assert len(calls) == 1 + ATTEMPTS  # the 503 is retried, then gives up
    assert not (cache_dir / "P54321.seq").exists()
    after = manifest_module.manifest(cache_dir)
    changed, digest = manifest_module.generation(before, after)
    assert changed and len(digest) == 64
    assert set(after) == {"P12345.seq", "P12345.sv"}
    assert (cache_dir / "P12345.seq").read_bytes() == b"MACDEFGHIK"
    # Reusing the saved generation does not fetch or create another generation.
    assert validator.SequenceCache(cache_dir).get("P12345") == "MACDEFGHIK"
    assert len(calls) == 1 + ATTEMPTS
    assert manifest_module.generation(after, after)[0] is False


@pytest.mark.parametrize("error", [TimeoutError("read timed out"), urllib.error.URLError("DNS unavailable")])
def test_failure_context_keeps_original_cause(tmp_path, monkeypatch, error):
    calls = []

    def fail(req, timeout):
        calls.append((req.full_url, timeout))
        raise error

    monkeypatch.setattr(validator.urllib.request, "urlopen", fail)
    with pytest.raises(RuntimeError, match="Q12345.*https://") as caught:
        validator.SequenceCache(tmp_path).get("Q12345")
    assert caught.value.__cause__ is error
    assert len(calls) == ATTEMPTS and all(timeout == 60 for _, timeout in calls)
    assert not list(tmp_path.iterdir())


def uniprot_record(sequence="MACDEFGHIKLM", *, declared=None, version_line=True):
    """A minimal UniProt text record whose SQ line declares ``declared`` (default: the truth)."""
    length, crc = (len(sequence), validator._crc64(sequence)) if declared is None else declared
    dt = "DT   21-MAR-2012, sequence version 3.\n" if version_line else ""
    return (
        "ID   TEST_CAEEL              Unreviewed;        12 AA.\n"
        "AC   Q12345; A0A000;\n"
        "DT   21-MAR-2012, integrated into UniProtKB/TrEMBL.\n"
        f"{dt}"
        "DT   02-SEP-2026, entry version 88.\n"
        f"SQ   SEQUENCE   {length} AA;  1300 MW;  {crc} CRC64;\n"
        f"     {sequence[:10]} {sequence[10:]}\n"
        "//\n"
    )


def unavailable(calls, error=None):
    def fetch(req, timeout):
        calls.append(req.full_url)
        raise error or urllib.error.HTTPError(
            req.full_url, 500, "Internal Server Error", {}, None
        )
    return fetch


def committed(tmp_path, text=None):
    record = tmp_path / "TEST-uniprot.txt"
    record.write_text(text or uniprot_record())
    return record


@pytest.mark.parametrize("path,crc", [
    ("genes/worm/pnk-1/pnk-1-uniprot.txt", "9BD2BF7375C370AB"),
    ("genes/human/SEPHS1/SEPHS1-uniprot.txt", "E9636E38146D926D"),
])
def test_crc64_matches_the_value_uniprot_prints(path, crc):
    record = validator.read_uniprot_flat_file(ROOT / path)
    assert record.declared_crc64 == crc
    assert validator._crc64(record.sequence) == crc and record.intact


def test_flat_file_parses_accessions_sequence_and_version(tmp_path):
    record = validator.read_uniprot_flat_file(committed(tmp_path))
    assert record.accessions == ["Q12345", "A0A000"]
    assert record.sequence == "MACDEFGHIKLM" and record.sequence_version == 3
    assert record.declared_length == 12 and record.intact


def test_transient_failure_recovers_on_retry(tmp_path, monkeypatch):
    calls, waits = [], []
    monkeypatch.setattr(validator, "_sleep", waits.append)

    def flaky(req, timeout):
        calls.append(req.full_url)
        if len(calls) == 1:
            raise urllib.error.HTTPError(req.full_url, 503, "unavailable", {}, None)
        return io.BytesIO(json.dumps({"sequence": {"value": "MACD"}}).encode())

    monkeypatch.setattr(validator.urllib.request, "urlopen", flaky)
    assert validator.SequenceCache(tmp_path).get("Q12345") == "MACD"
    assert len(calls) == 2 and waits == [validator.FETCH_BACKOFF_SECONDS[0]]
    assert (tmp_path / "Q12345.seq").read_text() == "MACD"


def test_not_found_is_not_retried_and_ignores_committed_record(tmp_path, monkeypatch):
    calls = []

    def missing(req, timeout):
        calls.append(req.full_url)
        raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, None)

    monkeypatch.setattr(validator.urllib.request, "urlopen", missing)
    cache = validator.SequenceCache(tmp_path / "cache")
    cache.add_local_record(committed(tmp_path))
    with pytest.raises(RuntimeError) as caught:
        cache.get("Q12345")
    assert not isinstance(caught.value, validator.UniProtUnavailable)
    assert len(calls) == 1


@pytest.mark.parametrize("make_error", [
    lambda: None,  # the default 500
    lambda: http.client.IncompleteRead(b'{"sequence": {"val'),  # body cut off mid-transfer
])
def test_outage_falls_back_to_committed_record(tmp_path, monkeypatch, capsys, make_error):
    calls = []
    monkeypatch.setattr(validator.urllib.request, "urlopen", unavailable(calls, make_error()))
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    cache_dir = tmp_path / "cache"
    cache = validator.SequenceCache(cache_dir)
    assert cache.add_local_record(committed(tmp_path)) == "Q12345"
    assert cache.get("UniProtKB:Q12345") == "MACDEFGHIKLM"
    assert cache.sequence_version("Q12345") == 3
    assert len(calls) == ATTEMPTS  # the version came from the same record
    assert "::warning::UniProt unavailable for Q12345" in capsys.readouterr().out
    assert cache.fallbacks == ["Q12345"] and "Q12345" in cache.fallback_note()
    # A fallback is not persisted, so the next run fetches the live record.
    assert not cache_dir.exists() or not list(cache_dir.iterdir())


def test_record_without_version_does_not_refetch(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(validator.urllib.request, "urlopen", unavailable(calls))
    cache = validator.SequenceCache(tmp_path / "cache")
    cache.add_local_record(committed(tmp_path, uniprot_record(version_line=False)))
    assert cache.get("Q12345") == "MACDEFGHIKLM"
    assert cache.sequence_version("Q12345") is None
    assert len(calls) == ATTEMPTS


def test_secondary_accession_is_not_registered(tmp_path, monkeypatch):
    monkeypatch.setattr(validator.urllib.request, "urlopen", unavailable([]))
    cache = validator.SequenceCache(tmp_path / "cache")
    cache.add_local_record(committed(tmp_path))
    with pytest.raises(validator.UniProtUnavailable):
        cache.get("A0A000")


@pytest.mark.parametrize("declared", [
    (20, "0000000000000000"),  # truncated: shorter than its SQ line says
    (12, "0000000000000000"),  # edited: right length, wrong checksum
])
def test_record_failing_its_own_sq_line_is_not_used(tmp_path, monkeypatch, capsys, declared):
    calls = []
    monkeypatch.setattr(validator.urllib.request, "urlopen", unavailable(calls))
    cache = validator.SequenceCache(tmp_path / "cache")
    cache.add_local_record(committed(tmp_path, uniprot_record(declared=declared)))
    with pytest.raises(validator.UniProtUnavailable):
        cache.get("Q12345")
    assert "does not match the length and CRC64" in capsys.readouterr().err
    assert cache.fallbacks == []


def test_fallback_can_be_switched_off(tmp_path, monkeypatch):
    monkeypatch.setattr(validator.urllib.request, "urlopen", unavailable([]))
    monkeypatch.setenv(validator.FALLBACK_ENV, "0")
    cache = validator.SequenceCache(tmp_path / "cache")
    cache.add_local_record(committed(tmp_path))
    with pytest.raises(validator.UniProtUnavailable):
        cache.get("Q12345")


def test_outage_without_committed_record_still_fails(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(validator.urllib.request, "urlopen", unavailable(calls))
    cache = validator.SequenceCache(tmp_path)
    with pytest.raises(validator.UniProtUnavailable, match="P54321") as caught:
        cache.get("P54321")
    assert isinstance(caught.value.__cause__, urllib.error.HTTPError)
    assert len(calls) == ATTEMPTS
    # Within the run, the same accession does not pay for another round of retries.
    with pytest.raises(validator.UniProtUnavailable):
        cache.sequence_version("P54321")
    assert len(calls) == ATTEMPTS


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
