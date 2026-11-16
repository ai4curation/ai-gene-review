"""Check scoped follow-up preservation and exact local source quotations."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import yaml

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if (p / "pyproject.toml").exists())
BASE = OUT.parent / "baseline.json"
GENES = [("BORPE", f"BP{n}") for n in range(3757, 3762)] + [("PSEAE", "ttg2D")]
OWNED = {f"genes/{org}/{gene}/{gene}-ai-review.yaml" for org, gene in GENES}
EXPECTED = {
    "genes/BORPE/BP3761/BP3761-ai-review.yaml": [("GO:0008429", "IDA", "enables")],
    "genes/PSEAE/ttg2D/ttg2D-ai-review.yaml": [("GO:0005543", "IDA", "enables"), ("GO:0030288", "IDA", "located_in")],
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def normalized(text):
    return " ".join(text.split())


def source(rid):
    if rid.startswith("PMID:"):
        return ROOT / "publications" / (rid.replace(":", "_") + ".md")
    if rid.startswith("file:"):
        relative = rid[5:]
        candidates = [ROOT / "genes" / relative, ROOT / relative]
        return next((p for p in candidates if p.is_file()), candidates[-1])
    return None


def evidence(obj, inherited=None):
    if isinstance(obj, dict):
        rid = obj.get("reference_id", obj.get("id", inherited))
        if "supporting_text" in obj:
            yield rid, obj["supporting_text"]
        for value in obj.values():
            yield from evidence(value, rid)
    elif isinstance(obj, list):
        for value in obj:
            yield from evidence(value, inherited)


def main():
    base = json.loads(BASE.read_text())
    rows = []
    originals = historical = added = active = retired = 0
    for path, prior in base["rows"].items():
        current = yaml.safe_load((ROOT / path).read_text()).get("existing_annotations") or []
        assert len(current) >= len(prior), path
        assert [payload(r) for r in current[:len(prior)]] == [payload(r) for r in prior], path
        for old, new in zip(prior, current):
            assert new["review"]["action"] == old["review"]["action"], path
            if old["review"]["action"] == "NEW":
                historical += 1
                assert new == old, f"Historical NEW row changed: {path}"
        authored = current[len(prior):]
        assert [(r["term"]["id"], r["evidence_type"], r.get("qualifier")) for r in authored] == EXPECTED.get(path, []), path
        assert all(r["review"]["action"] == "NEW" and not r.get("retired", False) for r in authored), path
        for row in current:
            if row["review"]["action"] == "NEW":
                retired += bool(row.get("retired", False))
                active += not row.get("retired", False)
        if path not in OWNED:
            assert digest(ROOT / path) == base["review_sha256"][path], path
        rows.append({"path": path, "original_rows": len(prior), "current_rows": len(current), "added": len(authored)})
        originals += len(prior)
        added += len(authored)
    for group in ["protected_sha256", "prior_receipts_sha256"]:
        for path, value in base[group].items():
            assert digest(ROOT / path) == value, path
    entry = json.loads((OUT / "entry-snapshot.json").read_text())
    for path, value in entry["prior_artifacts"].items():
        assert digest(ROOT / path) == value, path
    quotes = []
    dependencies = {}
    for path in sorted(OWNED):
        doc = yaml.safe_load((ROOT / path).read_text())
        for ref in doc["references"]:
            p = source(ref["id"])
            if p:
                assert p.exists(), p
                dependencies[str(p.relative_to(ROOT))] = digest(p)
        for rid, text in evidence(doc):
            p = source(rid)
            assert p and p.exists(), (path, rid)
            assert not p.name.endswith("-goa.tsv"), p
            assert normalized(text) in normalized(p.read_text()), (path, rid, text[:80])
            dependencies[str(p.relative_to(ROOT))] = digest(p)
            quotes.append({"review": path, "source": str(p.relative_to(ROOT)), "quote_sha256": hashlib.sha256(text.encode()).hexdigest()})
    source_lineage = {}
    for path, value in dependencies.items():
        old = subprocess.check_output(["git", "show", f"{base['head']}:{path}"], cwd=ROOT)
        assert hashlib.sha256(old).hexdigest() == value, path
        source_lineage[path] = {"sha256": value, "identical_to_published_head": True}
    new_members = ROOT / "analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/new-member-consultation"
    raw = (ROOT / "genes/BORPE/BP3761/BP3761-uniprot.txt").read_text()
    seq = "".join(re.findall("[A-Z]+", raw.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//")[0]))
    structures = []
    for pdb, ligand_id in [("11HY", "4"), ("11IF", "3")]:
        polymer_path = new_members / f"{pdb}-polymer_entity.json"
        polymer = json.loads(polymer_path.read_text())
        if isinstance(polymer, list):
            polymer = polymer[0]
        construct = polymer["entity_poly"]["pdbx_seq_one_letter_code_can"].replace("\n", "")
        assert construct == "MAHHHHHH" + seq[26:207]
        ligand_path = new_members / f"{pdb}-nonpolymer_entity-{ligand_id}.json"
        ligand = json.loads(ligand_path.read_text())
        assert "DI-PALMITOYL-3-SN-PHOSPHATIDYLETHANOLAMINE" in json.dumps(ligand)
        for path in [polymer_path, ligand_path]:
            relative = str(path.relative_to(ROOT))
            old = subprocess.check_output(["git", "show", f"{base['head']}:{relative}"], cwd=ROOT)
            assert hashlib.sha256(old).hexdigest() == digest(path), relative
            source_lineage[relative] = {"sha256": digest(path), "identical_to_published_head": True}
        structures.append({"pdb": pdb, "construct_length": len(construct), "target_interval": [27, 207], "exact_match": True, "ligand": "DPPE", "polymer_sha256": digest(polymer_path), "ligand_sha256": digest(ligand_path)})
    result = {"baseline": str(BASE.relative_to(ROOT)), "baseline_sha256": digest(BASE), "published_head": base["head"], "original_rows": originals, "historical_new_unchanged": historical, "authored_new": added, "current_rows": originals + added, "active_new": active, "retired_new": retired, "protected_sources": len(base["protected_sha256"]), "prior_receipts": len(base["prior_receipts_sha256"]), "rows": rows, "quotes_checked": len(quotes), "quotes": quotes, "source_dependencies": source_lineage, "structures": structures, "pass": True}
    (OUT / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"rows", "quotes", "source_dependencies", "structures"}}, indent=2))


if __name__ == "__main__":
    main()
