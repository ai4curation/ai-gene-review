"""Build the data file for the Ligand gap check artifact from the committed results.

Reads results/gapcheck-<org>.json, results/triage.json, results/ligand_survey.json and the
curated files, and writes one JSON object that the artifact page loads as data.json:

  orgs     per organism: total pathway terms, failing terms with triage category, lookups and
           category source, and passing terms with their ligand genes
  orphans  ligand-activity genes in no signaling term, per organism
  survey   textbook ligands and their involved_in annotations to their own pathway

Category source ("src") comes from triage.json: "manual" (organism_flags.yaml), "term"
(term_labels.yaml) or "lookup" (the cross-species or expected-ligand symbol lookup).

Usage:
  uv run python projects/LIGANDS_IN_SIGNALING/scripts/export_artifact_data.py --out data.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ligand_gap_check import ORGANISMS  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
RESULTS = HERE / "results"
SRC = {"organism_flag": "manual", "term_label": "term", "lookup": "lookup"}
SURVEY_ORG = {"9606": "human", "7227": "fly", "284812": "pombe", "4896": "pombe"}


def check_entry(lookup: dict) -> dict:
    """Convert one triage lookup into the page's ligand-check record.

    >>> check_entry({"donor": "NTN1", "result": "N"})
    {'sym': 'NTN1', 'present': False, 'ligmf': [], 'inP': False, 'above': False, 'sig': []}
    >>> check_entry({"donor": "IL34", "symbol": "Il34", "result": "C", "ligand_mf": False,
    ...              "signaling_terms": ["x"]})["inP"]
    True
    """
    found = lookup["result"] != "N"
    return {
        "sym": lookup.get("symbol") or lookup["donor"],
        "present": found,
        "ligmf": ["receptor ligand activity"] if lookup.get("ligand_mf") else [],
        "inP": lookup["result"] == "C",
        "above": lookup["result"] == "B",
        "sig": lookup.get("signaling_terms", []),
    }


def build() -> dict:
    """Assemble the artifact data object from the committed results."""
    triage = json.loads((RESULTS / "triage.json").read_text())
    by_key = {(r["org"], r["term"]): r for r in triage}
    out: dict = {"orgs": [], "orphans": {}, "survey": []}
    names: dict[str, str] = {}
    for org in ORGANISMS:
        path = RESULTS / f"gapcheck-{org}.json"
        if not path.exists() or not any(k[0] == org for k in by_key):
            continue
        res = json.loads(path.read_text())
        miss, ok = [], []
        for row in res["rows"]:
            names[row["term"]] = row["name"]
            if row["n_ligand_genes"]:
                ok.append({"id": row["term"], "name": row["name"], "n": row["n_genes"],
                           "nlig": row["n_ligand_genes"], "ligs": row["ligand_genes"][:6]})
                continue
            t = by_key[(org, row["term"])]
            miss.append({"id": row["term"], "name": row["name"], "n": row["n_genes"],
                         "genes": row["genes"], "bind": row["binding_only_genes"], "ev": row["evidence"],
                         "cat": t["category"], "note": t.get("note", ""),
                         "check": [check_entry(x) for x in t["lookups"]],
                         "src": SRC[t["source"]]})
        out["orgs"].append({"org": org, "total": len(res["rows"]), "miss": miss, "ok": ok,
                            "nlig": res["n_ligand_activity_genes"]})
        out["orphans"][org] = {"n": res["n_ligand_activity_genes"],
                               "genes": res["ligand_genes_not_in_any_signaling"]}
    for s in json.loads((RESULTS / "ligand_survey.json").read_text()):
        if s.get("role") != "ligand" or s["taxon"] not in SURVEY_ORG:
            continue
        ev = s.get("pathway_involved_in_evidence", {})
        out["survey"].append({"gene": s["gene"], "org": SURVEY_ORG[s["taxon"]], "path": (names.get(s["cognate_pathway"], s["cognate_pathway"])
                                       if s["cognate_pathway"] else "pheromone signaling (no current pathway term)"),
                              "exp": ev.get("experimental", 0), "other": ev.get("other", 0),
                              "reg": s.get("counts", {}).get("regulation", 0)})
    return out


def main() -> None:
    """Command-line entry point."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    data = build()
    args.out.write_text(json.dumps(data, separators=(",", ":")))
    print(f"{len(data['orgs'])} organisms, "
          f"{sum(len(o['miss']) for o in data['orgs'])} failing terms -> {args.out}")


if __name__ == "__main__":
    main()
