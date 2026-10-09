"""Merge the remapping of every experimental GO:0014029 / regulation-term annotation
into remapping.tsv: the four reviewed batches in remap/*.tsv plus rows for genes
already reviewed in this repo, whose decisions are read from their review YAML.

Usage: uv run python projects/NEURAL_CREST_FORMATION_OBSOLETION/merge_remap.py
"""
import csv
import glob
import pathlib
import yaml

BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[1]
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}
REVIEWED = {"pax3-a": "XENLA", "zic1": "XENLA", "hes4-a": "XENLA", "id3-a": "XENLA",
            "sox8": "XENLA", "sox9-a": "XENLA", "sox10": "XENLA"}
COLS = ["group", "gene_product_id", "symbol", "taxon_id", "go_term", "evidence", "qualifier", "reference",
        "assigned_by", "proposed_action", "replacement_ids", "replacement_labels", "rationale",
        "supporting_reference", "supporting_text", "source_checked"]


def reviewed_rows():
    inv = list(csv.DictReader(open(BASE / "annotations.tsv"), delimiter="\t"))
    out, seen = [], set()
    for r in inv:
        sym = r["SYMBOL"]
        if r["GO TERM"] != "GO:0014029" or r["GO EVIDENCE CODE"] not in EXPERIMENTAL or sym not in REVIEWED \
                or r["TAXON ID"] != "8355":
            continue
        key = (r["GENE PRODUCT ID"], r["REFERENCE"], r["GO EVIDENCE CODE"], r["QUALIFIER"])
        if key in seen:
            continue
        seen.add(key)
        doc = yaml.safe_load(open(ROOT / f"genes/{REVIEWED[sym]}/{sym}/{sym}-ai-review.yaml"))
        negated = "NOT" in r["QUALIFIER"]
        match = None
        for a in doc.get("existing_annotations") or []:
            if a["term"]["id"] in ("GO:0014029", "NTR") or a["term"].get("label") == "neural crest formation":
                if a.get("original_reference_id") == r["REFERENCE"] and bool(a.get("negated")) == negated:
                    match = a
                    break
        if match is None:
            continue
        rv = match.get("review") or {}
        repl = rv.get("proposed_replacement_terms") or []
        action = {"MODIFY": "REPLACE", "UNDECIDED": "UNDECIDED", "REMOVE": "REMOVE"}.get(rv.get("action"), "REPLACE")
        quote = next((s for s in rv.get("supported_by") or [] if str(s.get("reference_id", "")).startswith("PMID:")), {})
        out.append({
            "group": "R_reviewed_in_repo", "gene_product_id": r["GENE PRODUCT ID"], "symbol": sym,
            "taxon_id": r["TAXON ID"], "go_term": r["GO TERM"], "evidence": r["GO EVIDENCE CODE"],
            "qualifier": r["QUALIFIER"], "reference": r["REFERENCE"], "assigned_by": r["ASSIGNED BY"],
            "proposed_action": action,
            "replacement_ids": ";".join(t["id"] for t in repl) if action == "REPLACE" else "",
            "replacement_labels": ";".join(t["label"] for t in repl) if action == "REPLACE" else "",
            "rationale": f"Decision taken in the full gene review genes/{REVIEWED[sym]}/{sym}/ ({rv.get('action')}).",
            "supporting_reference": quote.get("reference_id", ""), "supporting_text": quote.get("supporting_text", ""),
            "source_checked": "GENE_REVIEW",
        })
    return out


def main():
    rows = []
    for f in sorted(glob.glob(str(BASE / "remap/*.tsv"))):
        if f.endswith(".input.tsv"):
            continue
        grp = pathlib.Path(f).name.split(".")[0]
        for r in csv.DictReader(open(f), delimiter="\t"):
            r["group"] = grp
            rows.append(r)
    rows += reviewed_rows()
    with open(BASE / "remapping.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows")


if __name__ == "__main__":
    main()
