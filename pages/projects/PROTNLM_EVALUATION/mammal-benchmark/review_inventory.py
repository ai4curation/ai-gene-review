# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML>=6,<7"]
# ///
"""Audit the frozen horse cohort against review artifacts; never assign biological verdicts."""
from pathlib import Path
from collections import Counter
import csv
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent

def normalized(text):
    return re.sub(r"\s+", " ", text).strip()

def inventory():
    with (DATA / "horse40.csv").open() as handle:
        cohort = list(csv.DictReader(handle))
    with (DATA / "horse40-predictions.csv").open() as handle:
        original = list(csv.DictReader(handle))
    records, errors = [], []
    for row in cohort:
        gene, accession = row["gene_symbol"], row["accession"]
        item = {"order": int(row["review_order"]), "gene": gene, "horse_accession": accession}
        for organism in ("human", "HORSE"):
            folder = ROOT / "genes" / organism / gene
            main_path = folder / f"{gene}-ai-review.yaml"
            if not main_path.exists():
                errors.append(f"Missing {main_path.relative_to(ROOT)}")
                continue
            main = yaml.safe_load(main_path.read_text())
            if organism == "HORSE" and main["id"] != accession:
                errors.append(f"Horse accession mismatch: {gene}")
            actions = Counter(a.get("review", {}).get("action", "MISSING") for a in main.get("existing_annotations", []))
            if actions["PENDING"] or actions["MISSING"]:
                errors.append(f"Unassessed annotations: {organism}/{gene}")
            reports = sorted(p.name for p in folder.glob(f"{gene}-deep-research*.md"))
            if organism == "human" and not reports:
                errors.append(f"Missing human research: {gene}")
            item[organism] = {"status": main.get("status"), "actions": dict(actions), "research": reports}
        source_go = [r for r in original if r["accession"] == accession and r["type"] == "GO"]
        pred_path = ROOT / "genes/HORSE" / gene / f"{gene}-protnlm-predictions-review.yaml"
        predictions = yaml.safe_load(pred_path.read_text()).get("predictions", []) if pred_path.exists() else []
        expected = Counter((r["id"], r["text"][2:]) for r in source_go)
        observed = Counter((p["predicted_term"]["id"], p["predicted_term"]["label"]) for p in predictions)
        if expected != observed:
            errors.append(f"Original GO predictions differ or are missing: {gene}")
        verdicts = Counter(p.get("review", {}).get("assessment", "MISSING") for p in predictions)
        if verdicts["MISSING"]:
            errors.append(f"Unassessed predictions: {gene}")
        item["GO"] = {"expected": len(source_go), "reviewed": len(predictions), "assessments": dict(verdicts)}
        narratives = [r for r in original if r["accession"] == accession and r["type"] == "function"]
        narrative_path = pred_path.with_name(f"{gene}-protnlm-function-review.md")
        text = normalized(narrative_path.read_text().replace("> ", "")) if narrative_path.exists() else ""
        for narrative in narratives:
            if normalized(narrative["text"]) not in text:
                errors.append(f"Original narrative absent/altered: {gene}")
        item["function_paragraphs"] = len(narratives)
        records.append(item)
    return {"cohort": "horse40", "genes": records, "errors": errors}

if __name__ == "__main__":
    report = inventory()
    target = DATA / "review-inventory.json"
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{len(report['genes'])} pairs; {len(report['errors'])} inventory errors; {target.relative_to(ROOT)}")
    for error in report["errors"]:
        print(error)
    raise SystemExit(bool(report["errors"]))
