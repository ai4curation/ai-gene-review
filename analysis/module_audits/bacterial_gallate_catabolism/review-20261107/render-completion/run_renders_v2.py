"""Sequential production rendering with atomic HTML writes and prior-seal guards."""
import hashlib
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
GENES = [("PSEPK", "galA"), ("PSEPK", "galB"), ("PSEPK", "galC"), ("PSEPK", "galD"), ("PSEPK", "galP"), ("BURL3", "Bcep18194_C7570"), ("SPHSK", "ligK")]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic(path, text):
    assert shutil.disk_usage(ROOT).free > 256 * 1024 * 1024, "STOP: headroom below 256 MiB"
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".gallate-render-", delete=False) as stream:
        stream.write(text.encode())
        stream.flush()
        os.fsync(stream.fileno())
        temporary = stream.name
    os.replace(temporary, path)


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    assert not (HERE / "run-state-v2.json").exists(), "Recorded render run exists; do not restart"
    frozen = {}
    seals = []
    for name in ("science-consultation", "coverage-successor"):
        path = HERE.parent / name / "handoff.json"
        doc = json.loads(path.read_text())
        frozen.update(doc["files"])
        frozen.update(doc["source_dependencies"])
        frozen[str(path.relative_to(ROOT))] = sha(path)
        seals.append({"path": str(path.relative_to(ROOT)), "sha256": sha(path)})
    for path, expected in frozen.items():
        assert sha(ROOT / path) == expected, path
    targets = [(f"genes/{org}/{gene}/{gene}-ai-review.yaml", f"genes/{org}/{gene}/{gene}-ai-review.html") for org, gene in GENES]
    targets.append(("modules/bacterial_gallate_catabolism.yaml", "pages/modules/bacterial_gallate_catabolism.html"))
    original_before = json.loads((HERE / "before.json").read_text())
    before = original_before["html"]
    assert original_before["seals"] == seals
    assert original_before["frozen_inputs"] == frozen
    for source, target in targets:
        assert before[target]["source_sha256"] == sha(ROOT / source)
    histories = json.loads((HERE.parent / "science-consultation/histories.json").read_text())
    schema_path = HERE.parent / "science-consultation/schema-checks.json"
    checks = json.loads(schema_path.read_text())
    check = next(c for c in checks if c["target_class"] == "HistoryRecord")
    assert check["exit_code"] == 0
    assert set(histories) <= set(check["command"])
    history_targets = {yaml.safe_load((ROOT / path).read_text())["target"]["path"] for path in histories}
    assert {source for source, _ in targets} <= history_targets
    history_receipt = {"status": "COVERED_BY_PRIOR_VALIDATION", "record_count": len(histories), "schema_receipt": str(schema_path.relative_to(ROOT)), "schema_receipt_sha256": sha(schema_path), "record_hashes": {p: sha(ROOT / p) for p in histories}, "uncovered_targets": []}
    assert json.loads((HERE / "history-coverage.json").read_text()) == history_receipt
    state = {"status": "RUNNING", "started": now(), "renders": [], "initial_free_bytes": shutil.disk_usage(ROOT).free, "command": [".venv/bin/python", "-B", str(Path(__file__).relative_to(ROOT))]}
    atomic(HERE / "run-state-v2.json", json.dumps(state, indent=2) + "\n")
    from ai_gene_review.render import render_gene_review
    from ai_gene_review.render_modules import render_module

    expected_outputs = {(ROOT / target).resolve() for _, target in targets}
    original_write_text = Path.write_text
    written = set()

    def atomic_production_write(path, text, encoding=None, errors=None, newline=None):
        # Same production-rendered text and destination; only persistence changes.
        resolved = path.resolve()
        if resolved in expected_outputs:
            assert encoding in (None, "utf-8") and errors is None and newline is None
            atomic(resolved, text)
            written.add(resolved)
            return len(text)
        return original_write_text(path, text, encoding=encoding, errors=errors, newline=newline)

    Path.write_text = atomic_production_write
    try:
        for source, target in targets:
            free = shutil.disk_usage(ROOT).free
            assert free > 256 * 1024 * 1024
            print(json.dumps({"rendering": source, "free_bytes": free}), flush=True)
            start = now()
            if source.startswith("genes/"):
                destination = ROOT / target
                temporary = destination.with_name("." + destination.name + ".render-tmp")
                assert not temporary.exists()
                temporary_output = render_gene_review(ROOT / source, output_path=temporary)
                assert temporary_output == temporary
                with temporary.open("rb") as stream:
                    os.fsync(stream.fileno())
                os.replace(temporary, destination)
                output = destination
                written.add(destination.resolve())
                warnings = []
                function = "ai_gene_review.render.render_gene_review"
            else:
                output, warnings = render_module(Path(source))
                function = "ai_gene_review.render_modules.render_module"
            assert output.resolve() == (ROOT / target).resolve()
            assert (ROOT / target).resolve() in written
            text = (ROOT / target).read_text()
            assert "<html" in text.lower() and "</html>" in text.lower()
            assert sha(ROOT / source) == before[target]["source_sha256"]
            state["renders"].append({"source": source, "source_sha256": sha(ROOT / source), "html": target, "before_sha256": before[target]["sha256"], "after_sha256": sha(ROOT / target), "renderer_function": function, "started": start, "finished": now(), "warnings": warnings, "bytes": (ROOT / target).stat().st_size, "free_bytes_before": free, "free_bytes_after": shutil.disk_usage(ROOT).free})
            atomic(HERE / "run-state-v2.json", json.dumps(state, indent=2) + "\n")
            print(json.dumps({"rendered": target, "warnings": warnings}), flush=True)
    finally:
        Path.write_text = original_write_text
    assert written == expected_outputs
    for path, expected in frozen.items():
        assert sha(ROOT / path) == expected, path
    state["status"] = "PASS"
    state["finished"] = now()
    state["frozen_inputs_unchanged"] = len(frozen)
    atomic(HERE / "run-state-v2.json", json.dumps(state, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "render_count": len(targets), "frozen_inputs": len(frozen), "history_targets_uncovered": 0}), flush=True)


if __name__ == "__main__":
    main()
