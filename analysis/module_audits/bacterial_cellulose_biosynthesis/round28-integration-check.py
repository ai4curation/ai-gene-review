"""Verify the approved cellulose science and metadata-only integration receipt.

Run from repository root with uv run python <this path>. No files are written.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

import yaml

ROOT = Path(__file__).resolve().parents[3]
PROOF = ROOT / "analysis/module_audits/bacterial_cellulose_biosynthesis/round28-main-integration.json"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    proof = json.loads(PROOF.read_text())
    approved, incoming = proof["approved_head"], proof["incoming_main"]
    shared = set(proof["shared_exclusions"])
    for path, expected in proof["preserved_files_sha256"].items():
        data = (ROOT / path).read_bytes()
        assert sha(data) == expected, path
        assert data == git("show", f"{approved}:{path}"), path
    assert len(proof["preserved_files_sha256"]) == 288
    for path in proof["incoming_changed_paths"]:
        if path not in shared:
            assert (ROOT / path).read_bytes() == git("show", f"{incoming}:{path}"), path
    inv = "projects/MODULE_TAXON_AUDIT/inventory.json"
    original = json.loads(git("show", f"{approved}:{inv}"))
    upstream = json.loads(git("show", f"{incoming}:{inv}"))
    current = json.loads((ROOT / inv).read_text())
    om = {row["module"]: row for row in original["modules"]}
    im = {row["module"]: row for row in upstream["modules"]}
    cm = {row["module"]: row for row in current["modules"]}
    assert om.keys() == im.keys() == cm.keys()
    assert current["module_count"] == len(cm) == 777
    assert all(row == im[key] for key, row in cm.items() if key != "bacterial_cellulose_biosynthesis")
    assert all(row == cm[key] for key, row in om.items() if row["audit_status"] == "COMPLETE")
    assert cm["osmoregulated_periplasmic_glucan_biosynthesis"]["audit_status"] == "COMPLETE"
    assert cm["bacterial_flavonoid_degradation"] == im["bacterial_flavonoid_degradation"]
    assert dict(Counter(row["audit_status"] for row in cm.values())) == proof["inventory_status_counts"]
    assert (ROOT / inv).read_bytes() == (ROOT / "pages" / inv).read_bytes()
    md = (ROOT / "projects/MODULE_TAXON_AUDIT.md").read_text()
    html = (ROOT / "pages/projects/MODULE_TAXON_AUDIT.html").read_text()
    front = yaml.safe_load(md.split("---", 2)[1])
    assert "pins" in front["autolink_exclude"]
    assert "genes/DROME/pins/pins-ai-review.html" not in html
    assert proof["rendered_ledger_snapshot"] in md
    assert proof["rendered_ledger_snapshot"][6:] in html
    assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", md, re.M)
    status = next(line for line in md.splitlines() if line.startswith("- [ ] `bacterial_cellulose_biosynthesis`:"))
    assert incoming[:10] in status and "round28-main-integration.json" in status
    # Preserve every dated journal chunk from both parents verbatim.
    for ref in (approved, incoming):
        old = git("show", f"{ref}:projects/MODULE_TAXON_AUDIT.md").decode()
        for chunk in re.split(r"(?=^## )", old, flags=re.M)[1:]:
            if re.match(r"## \d{4}-\d{2}-\d{2}", chunk):
                assert chunk.strip() in md, (ref, chunk.splitlines()[0])
    for path, expected in proof["preexisting_untracked_files_sha256"].items():
        assert sha((ROOT / path).read_bytes()) == expected, path
    assert sha((ROOT / proof["history"]["path"]).read_bytes()) == proof["history"]["sha256"]
    assert all(result["exit_code"] == 0 for result in proof["focused_checks"].values())
    print(json.dumps({"result": "PASS", "approved_nonshared": 288,
                      "completed_rows_retained": 34, "rows": 777,
                      "untracked_preserved": len(proof["preexisting_untracked_files_sha256"])}))


if __name__ == "__main__":
    main()
