"""Offline cache-progress and diagnostic regression tests; no upstream calls."""

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
    assert len(calls) == 2  # one request per accession, no retry
    assert not (cache_dir / "P54321.seq").exists()
    after = manifest_module.manifest(cache_dir)
    changed, digest = manifest_module.generation(before, after)
    assert changed and len(digest) == 64
    assert set(after) == {"P12345.seq", "P12345.sv"}
    assert (cache_dir / "P12345.seq").read_bytes() == b"MACDEFGHIK"
    # Reusing the saved generation does not fetch or create another generation.
    assert validator.SequenceCache(cache_dir).get("P12345") == "MACDEFGHIK"
    assert len(calls) == 2
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
    assert len(calls) == 1 and calls[0][1] == 60
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


def test_workflow_retains_failure_and_saves_only_valid_growth_before_tests():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    steps = workflow["jobs"]["test"]["steps"]
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
    assert steps.index(family) < steps.index(after) < steps.index(save) < steps.index(by_name["Run test suite"])
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
