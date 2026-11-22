"""Sweep the trusted-cutoff check, with a whole-library scan, over bacterial reviews.

For every live (not retired) IEA/IBA molecular-function row whose GO term maps to a
complete EC number, in the P. putida KT2440 and E. coli reviews, this scores the
protein against the NCBIfam families that carry the activity (filters off, as in the
check) and against its closest families from a scan of the whole function-level
library. The reviewer's action is read from the review and is never an input to the
verdict.

Rows are then sorted into the disagreements worth a curator's time:

* ``kept_but_fits_other``: the row is kept (ACCEPT or KEEP_AS_NON_CORE), the protein
  fails its target families, it passes a function-level family for another reaction,
  and its UniProt record does not state the annotated EC.
* ``kept_family_lacks_ec``: as above, but the gene's own UniProt record states the
  annotated EC, so the passing family is usually the protein's own family and its
  release-table EC list is narrower than the protein (a secondary or partial reaction).
* ``kept_below_cutoff``: kept, fails its target families, no competing family passes.
  The closest family is listed, since this is often a sister family (ptxD's case).
* ``removed_but_passes``: the row was removed or marked over-annotated, yet a
  function-level target family passes its trusted cutoff with no competitor.

    uv run python projects/ENZYME_SPECIFICITY/cutoff-check/sweep/run_sweep.py
    uv run python projects/ENZYME_SPECIFICITY/cutoff-check/sweep/run_sweep.py --rerender

Writes sweep_results.yaml and DISAGREEMENTS.md next to this script. Network access to
QuickGO, UniProt and the NCBI HMM site is needed on first run; everything is cached.
"""

from __future__ import annotations

import json
import re
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
EC_RE = re.compile(r"EC=(\d+\.\d+\.\d+\.n?\d+)")
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


def review_paths() -> dict[str, Path]:
    """Review file for each UniProt accession in the swept organisms."""
    paths = {}
    for org in ORGANISMS:
        for path in sorted((REPO / "genes" / org).glob("*/*-ai-review.yaml")):
            paths[yaml.safe_load(path.read_text())["id"]] = path
    return paths


def uniprot_ecs(review: Path) -> set[str]:
    """EC numbers the gene's own UniProt record states (names and catalytic activities)."""
    record = review.parent / f"{review.parent.name}-uniprot.txt"
    return set(EC_RE.findall(record.read_text())) if record.exists() else set()


def classify(row: dict) -> str | None:
    """Which disagreement list a row belongs to, if any."""
    if row["action"] in KEPT and row["verdict"] in {"BTC", "SFA", "NO_TARGET_HIT"}:
        if not row["better_fitting_families"]:
            return "kept_below_cutoff"
        if row["ec_on_uniprot_record"]:
            return "kept_family_lacks_ec"
        return "kept_but_fits_other"
    if (
        row["action"] in REMOVED
        and row["verdict"] == "ABOVE_TC"
        and not row["better_fitting_families"]
    ):
        return "removed_but_passes"
    return None


def annotate(results: list[dict]) -> None:
    """Add the UniProt-record EC check and the disagreement list to each result."""
    paths = review_paths()
    ecs = {acc: uniprot_ecs(path) for acc, path in paths.items()}
    for r in results:
        r["ec_on_uniprot_record"] = bool(set(r["ec"]) & ecs.get(r["accession"], set()))
        b = r["best_target"]
        r["target_matched_by"] = (
            None
            if not b
            else "ec"
            if set(r["ec"]) & set(b["ec_numbers"])
            else "go_only"
        )
        r["disagreement"] = classify(r)


def summary(score: FamilyScore) -> dict:
    """The fields of a family score worth recording, with the model's metadata."""
    return {
        "family": f"{score.accession} {score.product_name}",
        "family_type": score.family_type,
        "ec_numbers": score.ec_numbers,
        "go_terms": score.go_terms,
        "score": score.seq_score,
        "domain_score": score.dom_score,
        "trusted_cutoff": score.tc[0],
        "domain_trusted_cutoff": score.tc[1],
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
        results.append(result)
        if i % 100 == 0:
            print(f"{i}/{len(rows)}", file=sys.stderr)

    annotate(results)
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

    def cell(s: dict) -> str:
        """Family, score and cutoff; the best-domain score too when it is what fails."""
        text = f"{s['family']} ({s['score']} / {s['trusted_cutoff']}"
        if s["score"] is not None and s["score"] >= s["trusted_cutoff"]:
            text += f"; best domain {s['domain_score']} / {s['domain_trusted_cutoff']}"
        return text + ")"

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
            "| organism | gene | term | action | best target (score / TC) | matched by "
            "| other families |"
        )
        lines.append("|---|---|---|---|---|---|---|")
        for r in rows:
            b = r["best_target"]
            target = cell(b) if b else "no hit"
            other = "; ".join(r["better_fitting_families"]) or "; ".join(
                cell(c) for c in r["closest_families"][:1]
            )
            lines.append(
                f"| {r['organism']} | {r['gene']} | {r['go']} {r['label']} | {r['action']} | {target} | {r['target_matched_by'] or ''} | {other} |"
            )

    section(
        "kept_but_fits_other",
        "Kept rows whose protein fits another reaction's family",
        "The strongest leads: the protein fails every family carrying the term, passes a "
        "function-level family for a different reaction, and its own UniProt record does "
        "not state the annotated EC.",
    )
    section(
        "kept_family_lacks_ec",
        "Kept rows the protein's own record supports, though its family lacks the EC",
        "Usually not a conflict: the gene's UniProt record states the annotated EC, and the "
        "passing family is the protein's own, whose release-table EC list is narrower "
        "(a secondary or partial reaction). Worth a look only where that activity is doubtful.",
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
        "overlapping family or experimental evidence can still justify the removal. "
        "Where the family qualified as a target only through its GO metadata (`go_only`), "
        "check that metadata against the family's name: it is sometimes the sister reaction's term. "
        "Subunit models of a complex carry the complex's EC number, so a passing subunit model "
        "does not show the subunit catalyses the reaction.",
    )
    return "\n".join(lines) + "\n"


def rerender() -> None:
    """Re-derive the lists and DISAGREEMENTS.md from saved scores, without rescanning."""
    saved = yaml.safe_load((HERE / "sweep_results.yaml").read_text())
    annotate(saved["rows"])
    (HERE / "sweep_results.yaml").write_text(
        yaml.safe_dump(saved, sort_keys=False, width=120)
    )
    (HERE / "DISAGREEMENTS.md").write_text(render(saved["meta"], saved["rows"]))


if __name__ == "__main__":
    if sys.argv[1:] == ["--rerender"]:
        rerender()
    else:
        main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
