"""Sweep the trusted-cutoff check, with a whole-library scan, over bacterial reviews.

For every live (not retired) IEA/IBA molecular-function row whose GO term maps to a
complete EC number, in the P. putida KT2440 and E. coli reviews, this scores the
protein against the NCBIfam families that carry the activity (filters off, as in the
check) and against its closest families from a scan of the whole function-level
library. The reviewer's action is read from the review and is never an input to the
verdict.

Rows are then sorted into the disagreements worth a curator's time:

* ``kept_but_fits_other``: the row is kept (ACCEPT or KEEP_AS_NON_CORE), the protein
  fails its target families, and it passes a function-level family that is neither
  named for it nor carries an EC its UniProt record states, or one that carries a record
  EC while the record does not state the annotated EC.
* ``kept_other_model``: as above, but every passing family is named for the protein:
  another NCBIfam model of its own family, which the term is not mapped to.
* ``kept_record_states_ec``: every passing family is named for the protein or carries
  an EC its UniProt record states, and the record states the annotated EC too (often
  a secondary or partial reaction).
* ``kept_no_model_fits_other``: kept, no family carries the term, and the protein
  passes another function-level family.
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
    Family,
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
NAME_RE = re.compile(
    r"^DE\s+(?:RecName|AltName|SubName|Contains|Includes)?:?\s*Full=([^{;]+?)\s*[{;]",
    re.M,
)
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


def collect_rows() -> tuple[list[dict], list[dict]]:
    """Live electronic rows that map to a complete EC number, one per protein and term.

    Proposed (``NEW``) rows are not GOA rows and are skipped. Where two electronic rows
    on one protein and term carry different actions (in one review, or in two review
    folders for the same accession), the first is kept and the pair is returned as a
    conflict naming both folders.
    """
    raw = []
    for org in ORGANISMS:
        for path in sorted((REPO / "genes" / org).glob("*/*-ai-review.yaml")):
            review = yaml.safe_load(path.read_text())
            for ann in review.get("existing_annotations") or []:
                if ann.get("retired") or ann.get("evidence_type") not in ELECTRONIC:
                    continue
                review_block = ann.get("review") or {}
                if review_block.get("action") == "NEW":
                    continue
                raw.append(
                    {
                        "organism": org,
                        "gene": review["gene_symbol"],
                        "folder": path.parent.name,
                        "accession": review["id"],
                        "go": ann["term"]["id"],
                        "label": ann["term"]["label"],
                        "action": review_block.get("action"),
                    }
                )
    xrefs = ec_xrefs({r["go"] for r in raw})
    rows: list[dict] = []
    first: dict[tuple[str, str], dict] = {}
    conflicts = []
    for r in raw:
        if not xrefs.get(r["go"]):
            continue
        key = (r["accession"], r["go"])
        if key in first:
            if r["action"] != first[key]["action"]:
                conflicts.append(
                    {k: r[k] for k in ("organism", "accession", "go", "label")}
                    | {
                        "rows": [
                            f"{first[key]['folder']}: {first[key]['action']}",
                            f"{r['folder']}: {r['action']}",
                        ]
                    }
                )
            continue
        first[key] = r
        rows.append(r | {"ec": xrefs[r["go"]]})
    return rows, conflicts


def review_paths() -> dict[str, list[Path]]:
    """Review files for each UniProt accession in the swept organisms.

    Normally one; a few accessions have two review folders, which the sweep reports.
    """
    paths: dict[str, list[Path]] = {}
    for org in ORGANISMS:
        for path in sorted((REPO / "genes" / org).glob("*/*-ai-review.yaml")):
            paths.setdefault(yaml.safe_load(path.read_text())["id"], []).append(path)
    return paths


def duplicate_accessions() -> list[dict]:
    """Accessions with more than one review folder."""
    return [
        {"accession": acc, "folders": [str(p.parent.relative_to(REPO)) for p in ps]}
        for acc, ps in sorted(review_paths().items())
        if len(ps) > 1
    ]


def uniprot_record(review: Path) -> tuple[set[str], set[str]]:
    """EC numbers and protein names the gene's own UniProt record states."""
    record = review.parent / f"{review.parent.name}-uniprot.txt"
    if not record.exists():
        return set(), set()
    text = record.read_text()
    names = {n.lower() for n in NAME_RE.findall(text)}
    return set(EC_RE.findall(text)), names


def gene_token(gene: str) -> str:
    """The gene symbol as it appears in a family name: ``puuA-II`` -> ``puua``.

    Paralog numbering (``-II``, a trailing digit, a prime) is dropped, so ``cheB1``
    matches a family named for CheB.

    >>> gene_token("puuA-II"), gene_token("pyrC'"), gene_token("nuoG"), gene_token("cheB1")
    ('puua', 'pyrc', 'nuog', 'cheb')
    """
    return re.sub(r"(-[IVX]+|'|\d+)$", "", gene).lower()


def relation(
    family: Family, gene: str, target_name: str | None, names: set[str], ecs: set[str]
) -> str:
    """How a passing non-target family relates to the protein.

    ``named``: the family is named for the protein (its gene symbol, the best target's
    product name, or a protein name on the UniProt record), so it is another model of
    the protein's own family. ``record_ec``: it carries an EC the record states.
    ``other``: neither.
    """
    product = family.product_name.lower()
    if (
        re.search(rf"\b{re.escape(gene_token(gene))}\b", product)
        or product == (target_name or "").lower()
        or product in names
    ):
        return "named"
    if set(family.ec_numbers) & ecs:
        return "record_ec"
    return "other"


def classify(row: dict) -> str | None:
    """Which disagreement list a row belongs to, if any."""
    if row["action"] in KEPT and row["verdict"] == "NO_MODEL":
        return "kept_no_model_fits_other" if row["better_fitting_families"] else None
    if row["action"] in KEPT and row["verdict"] in {"BTC", "SFA", "NO_TARGET_HIT"}:
        relations = set(row["better_fitting_relations"].values())
        if not relations:
            return "kept_below_cutoff"
        if row["ec_on_uniprot_record"] and "other" not in relations:
            return "kept_record_states_ec"
        if relations == {"named"}:
            return "kept_other_model"
        return "kept_but_fits_other"
    if (
        row["action"] in REMOVED
        and row["verdict"] == "ABOVE_TC"
        and not row["better_fitting_families"]
    ):
        return "removed_but_passes"
    return None


def annotate(results: list[dict], db: NCBIfam) -> None:
    """Add the UniProt-record checks, competitor relations and disagreement list."""
    records = {}
    for acc, paths in review_paths().items():
        parts = [uniprot_record(p) for p in paths]
        records[acc] = (
            set().union(*(e for e, _ in parts)),
            set().union(*(n for _, n in parts)),
        )
    by_accession = {f.accession: f for f in db.families}
    for r in results:
        ecs, names = records.get(r["accession"], (set(), set()))
        r["ec_on_uniprot_record"] = bool(set(r["ec"]) & ecs)
        b = r["best_target"]
        target_name = b["family"].split(" ", 1)[1] if b else None
        r["better_fitting_relations"] = {
            entry: relation(
                by_accession[entry.split()[0]], r["gene"], target_name, names, ecs
            )
            for entry in r["better_fitting_families"]
        }
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
    rows, conflicts = collect_rows()
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

    annotate(results, db)
    meta = {
        "ncbifam_release": db.release(),
        "organisms": ORGANISMS,
        "rows": len(results),
        "conflicting_actions": conflicts,
        "duplicate_accessions": duplicate_accessions(),
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

    conflicts = meta.get("conflicting_actions") or []
    lines += [
        "",
        f"## Electronic rows on one protein and term with different actions ({len(conflicts)})",
        "",
        "The sweep keeps one row per protein and term (the first folder in sort order). "
        "These pairs disagree; each names the review folder it comes from.",
        "",
    ]
    lines += [
        f"- {c['organism']} {c['accession']} {c['go']} {c['label']}: {' vs '.join(c['rows'])}"
        for c in conflicts
    ]
    dups = meta.get("duplicate_accessions") or []
    lines += [
        "",
        f"## Accessions with more than one review folder ({len(dups)})",
        "",
        "Their rows are merged in this sweep. Each pair needs a decision on whether both "
        "folders should exist.",
        "",
    ]
    lines += [f"- {d['accession']}: {', '.join(d['folders'])}" for d in dups]

    def cell(s: dict) -> str:
        """Family, score and cutoff; the best-domain score too when it is what fails."""
        text = f"{s['family']} ({s['score']} / {s['trusted_cutoff']}"
        if (
            s["status"] != "ABOVE_TC"
            and s["score"] is not None
            and s["score"] >= s["trusted_cutoff"]
        ):
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
            other = "; ".join(
                f"{f} [{rel}]" for f, rel in r["better_fitting_relations"].items()
            ) or "; ".join(cell(c) for c in r["closest_families"][:1])
            lines.append(
                f"| {r['organism']} | {r['gene']} | {r['go']} {r['label']} | {r['action']} | {target} | {r['target_matched_by'] or ''} | {other} |"
            )

    section(
        "kept_but_fits_other",
        "Kept rows whose protein passes a family for another activity",
        "The strongest leads. The protein fails every family mapped to the term. It passes "
        "a function-level family that is neither named for it nor carries an EC its UniProt "
        "record states, or one carrying a record EC while the record does not state the "
        "annotated EC. Each passing family is tagged: `[named]` is named for the protein, "
        "`[record_ec]` carries an EC its UniProt record states (often the protein's own "
        "reaction), `[other]` is neither.",
    )
    section(
        "kept_other_model",
        "Kept rows where another model of the protein's own family passes",
        "Every passing family is named for the protein (its gene symbol, the best target's "
        "product name, or a name on its UniProt record), but NCBIfam maps the term to a "
        "different model. Usually a gap in the release table's EC/GO mapping, not a doubt "
        "about the row.",
    )
    section(
        "kept_record_states_ec",
        "Kept rows whose annotated EC the protein's UniProt record states",
        "Every passing family is named for the protein or carries an EC its UniProt record "
        "states, and the record also states the annotated EC. Often a secondary or partial "
        "reaction the family's EC list leaves out. Check where the record's support for "
        "the annotated EC is weak.",
    )
    section(
        "kept_no_model_fits_other",
        "Kept rows no family is mapped to, though the protein passes another family",
        "No NCBIfam family carries the term, and the protein passes a function-level family "
        "for something else. Check whether the passing family's name or EC fits the term: "
        "if it does, the release table is missing the term (purT's case).",
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
    db = NCBIfam(CACHE / "ncbifam")
    if saved["meta"]["ncbifam_release"] != db.release():
        raise SystemExit(
            f"saved results are from NCBIfam {saved['meta']['ncbifam_release']}, the cache "
            f"holds {db.release()}: rerun the sweep instead of --rerender"
        )
    annotate(saved["rows"], db)
    (HERE / "sweep_results.yaml").write_text(
        yaml.safe_dump(saved, sort_keys=False, width=120)
    )
    (HERE / "DISAGREEMENTS.md").write_text(render(saved["meta"], saved["rows"]))


if __name__ == "__main__":
    if sys.argv[1:] == ["--rerender"]:
        rerender()
    else:
        main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
