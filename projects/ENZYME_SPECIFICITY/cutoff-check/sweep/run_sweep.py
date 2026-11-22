"""Sweep the trusted-cutoff check, with a whole-library scan, over bacterial reviews.

For every live (not retired) IEA/IBA molecular-function row whose GO term maps to a
complete EC number, in the P. putida KT2440 and E. coli reviews, this scores the
protein against the NCBIfam families that carry the activity (filters off, as in the
check) and against its closest families from a scan of the whole function-level
library. The reviewer's action is read from the review and is never an input to the
verdict.

Rows are then sorted into the disagreements worth a curator's time:

* ``kept_but_fits_other``: the row is kept (ACCEPT or KEEP_AS_NON_CORE), the protein
  fails its target families, and it passes a function-level family for another reaction.
* ``kept_below_cutoff``: kept, fails its target families, no competing family passes.
  The closest family is listed, since this is often a sister family (ptxD's case).
* ``removed_but_passes``: the row was removed or marked over-annotated, yet a
  function-level target family passes its trusted cutoff with no competitor.

    uv run python projects/ENZYME_SPECIFICITY/cutoff-check/sweep/run_sweep.py

Writes sweep_results.yaml and DISAGREEMENTS.md next to this script. Network access to
QuickGO, UniProt and the NCBI HMM site is needed on first run; everything is cached.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

from ai_gene_review.validation.enzyme_family_cutoff import (
    FamilyScore,
    NCBIfam,
    _read_with_retry,
    is_complete_ec,
    rank_closest,
    scan_library,
    score_families,
    verdict_for,
)
from ai_gene_review.validation.family_residue_validator import SequenceCache

HERE = Path(__file__).parent
REPO = HERE.parents[3]
CACHE = Path(".cache")
ORGANISMS = ["PSEPK", "ECOLI"]
ELECTRONIC = {"IEA", "IBA"}
KEPT = {"ACCEPT", "KEEP_AS_NON_CORE"}
REMOVED = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/xrefs"


def ec_xrefs(go_ids: set[str]) -> dict[str, list[str]]:
    """Complete EC numbers for each GO term, from QuickGO in batches, cached on disk."""
    cache_path = CACHE / "quickgo_ec_xrefs.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    missing = sorted(go_ids - cache.keys())
    for start in range(0, len(missing), 50):
        batch = missing[start : start + 50]
        req = urllib.request.Request(
            QUICKGO.format(ids=",".join(batch)), headers={"Accept": "application/json"}
        )
        results = json.loads(_read_with_retry(req))["results"]
        for go in batch:
            cache[go] = []
        for r in results:
            cache[r["id"]] = [
                x["dbId"]
                for x in r.get("xRefs", [])
                if x["dbCode"] == "EC" and is_complete_ec(x["dbId"])
            ]
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, indent=0, sort_keys=True))
    return cache


def collect_rows() -> list[dict]:
    """Live electronic MF rows that map to a complete EC number, one per protein and term."""
    raw = []
    for org in ORGANISMS:
        for path in sorted((REPO / "genes" / org).glob("*/*-ai-review.yaml")):
            review = yaml.safe_load(path.read_text())
            for ann in review.get("existing_annotations") or []:
                if ann.get("retired") or ann.get("evidence_type") not in ELECTRONIC:
                    continue
                review_block = ann.get("review") or {}
                raw.append(
                    {
                        "organism": org,
                        "gene": review["gene_symbol"],
                        "accession": review["id"],
                        "go": ann["term"]["id"],
                        "label": ann["term"]["label"],
                        "action": review_block.get("action"),
                    }
                )
    xrefs = ec_xrefs({r["go"] for r in raw})
    rows, seen = [], set()
    for r in raw:
        key = (r["accession"], r["go"])
        if xrefs.get(r["go"]) and key not in seen:
            seen.add(key)
            rows.append(r | {"ec": xrefs[r["go"]]})
    return rows


def classify(row: dict) -> str | None:
    """Which disagreement list a row belongs to, if any."""
    if row["action"] in KEPT and row["verdict"] in {"BTC", "SFA", "NO_TARGET_HIT"}:
        return (
            "kept_but_fits_other"
            if row["better_fitting_families"]
            else "kept_below_cutoff"
        )
    if (
        row["action"] in REMOVED
        and row["verdict"] == "ABOVE_TC"
        and not row["better_fitting_families"]
    ):
        return "removed_but_passes"
    return None


def summary(score: FamilyScore) -> dict:
    """The fields of a family score worth recording, with the model's metadata."""
    return {
        "family": f"{score.accession} {score.product_name}",
        "family_type": score.family_type,
        "ec_numbers": score.ec_numbers,
        "score": score.seq_score,
        "trusted_cutoff": score.tc[0],
        "status": score.status,
    }


def main(limit: int | None = None) -> None:
    """Run the sweep and write the results; ``limit`` caps proteins for a timing run
    (its output overwrites the full results, so rerun without it before committing)."""
    db = NCBIfam(CACHE / "ncbifam")
    rows = collect_rows()
    if limit:
        keep = sorted({r["accession"] for r in rows})[:limit]
        rows = [r for r in rows if r["accession"] in keep]
    print(
        f"{len(rows)} rows on {len({r['accession'] for r in rows})} proteins",
        file=sys.stderr,
    )
    seqs = SequenceCache(CACHE / "uniprot_seq")
    sequences = {acc: seqs.get(acc) for acc in sorted({r["accession"] for r in rows})}
    closest = scan_library(sequences, db, top=5)

    results = []
    for i, row in enumerate(rows, 1):
        targets = db.targets_for(row["ec"], [row["go"]])
        target_ids = {f.accession for f in targets}
        target_scores = score_families(
            sequences[row["accession"]],
            row["accession"],
            targets,
            target_ids,
            db,
        )
        others = [
            s
            for s in closest.get(row["accession"], [])
            if s.accession not in target_ids
        ]
        verdict, note, better = verdict_for(target_scores + others)
        best_target = rank_closest(target_scores, 1)
        result = row | {
            "verdict": verdict,
            "note": note,
            "best_target": summary(best_target[0]) if best_target else None,
            "better_fitting_families": better,
            "closest_families": [summary(s) for s in others[:3]],
        }
        result["disagreement"] = classify(result)
        results.append(result)
        if i % 100 == 0:
            print(f"{i}/{len(rows)}", file=sys.stderr)

    meta = {
        "ncbifam_release": db.release(),
        "organisms": ORGANISMS,
        "rows": len(results),
    }
    (HERE / "sweep_results.yaml").write_text(
        yaml.safe_dump({"meta": meta, "rows": results}, sort_keys=False, width=120)
    )
    (HERE / "DISAGREEMENTS.md").write_text(render(meta, results))


def render(meta: dict, results: list[dict]) -> str:
    """DISAGREEMENTS.md, built only from the computed results."""
    by_action = Counter((r["verdict"], r["action"]) for r in results)
    actions = sorted({a for _, a in by_action if a})
    verdicts = sorted({v for v, _ in by_action})
    lines = [
        "# Cutoff-check sweep: disagreements with the reviews",
        "",
        "Generated by `run_sweep.py`; do not edit by hand. Raw output: `sweep_results.yaml`.",
        f"NCBIfam release {meta['ncbifam_release']}; {meta['rows']} live electronic enzyme rows "
        f"in {', '.join(meta['organisms'])} reviews.",
        "",
        "These are leads for a curator, not verdicts on the reviews. A score below a family's",
        "cutoff says only that the protein is not in that family; see the cutoff-check",
        "RESULTS.md for how to read each case.",
        "",
        "## Verdict by reviewer action",
        "",
        "| verdict | " + " | ".join(actions) + " |",
        "|---" * (len(actions) + 1) + "|",
    ]
    lines += [
        f"| {v} | " + " | ".join(str(by_action[(v, a)]) for a in actions) + " |"
        for v in verdicts
    ]

    def section(kind: str, title: str, explain: str) -> None:
        rows = [r for r in results if r["disagreement"] == kind]

        def ratio(r: dict) -> float:
            b = r["best_target"]
            return (b["score"] or 0) / b["trusted_cutoff"] if b else 0.0

        rows.sort(key=ratio, reverse=(kind == "removed_but_passes"))
        lines.extend(["", f"## {title} ({len(rows)})", "", explain, ""])
        if not rows:
            return
        lines.append(
            "| organism | gene | term | action | best target (score / TC) | other families |"
        )
        lines.append("|---|---|---|---|---|---|")
        for r in rows:
            b = r["best_target"]
            target = (
                f"{b['family']} ({b['score']} / {b['trusted_cutoff']})"
                if b
                else "no hit"
            )
            other = "; ".join(r["better_fitting_families"]) or "; ".join(
                f"{c['family']} ({c['score']} / {c['trusted_cutoff']})"
                for c in r["closest_families"][:1]
            )
            lines.append(
                f"| {r['organism']} | {r['gene']} | {r['go']} {r['label']} | {r['action']} | {target} | {other} |"
            )

    section(
        "kept_but_fits_other",
        "Kept rows whose protein fits another reaction's family",
        "The strongest leads: the protein fails every family carrying the term and passes a "
        "function-level family for a different reaction.",
    )
    section(
        "kept_below_cutoff",
        "Kept rows below cutoff with no competing family",
        "Weaker leads. The last column is the closest family; if it is a sister family the "
        "protein narrowly misses, the row may be fine.",
    )
    section(
        "removed_but_passes",
        "Removed rows whose protein passes the family",
        "The family supports the activity. Check the review's reason: a pseudoenzyme, an "
        "overlapping family or experimental evidence can still justify the removal.",
    )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
