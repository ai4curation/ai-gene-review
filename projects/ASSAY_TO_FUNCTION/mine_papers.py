#!/usr/bin/env python3
"""Mine the cached-paper corpus for assay/readout usage and correlate with how
the resulting annotations were curated.

Unit of analysis: ``(annotation, readout_class)`` where the readout class is
detected in the **source paper** named by ``original_reference_id`` (a PMID),
not in the curator's summary. This is the design the review-prose miner
(``mine_readouts.py``) motivated: assay vocabulary lives in papers' methods, not
in curation synthesis.

For each PMID-backed annotation we:
  1. resolve the cached paper ``publications/PMID_<id>.md`` and read its text,
  2. detect which readout classes the paper uses (regex catalog),
  3. look up the annotation's GO aspect (MF/BP/CC) from the GOA TSVs,
  4. flag *thematic alignment* -- the annotation's GO term is about the same
     process the readout reports (GO id in ``commonly_overmapped_to`` or GO
     label matches ``aligned_label_regex``).

The strongest signal is the action distribution for **aligned** annotations:
those are the cases where the readout plausibly *drove* the annotation.

Usage:
    uv run python projects/ASSAY_TO_FUNCTION/mine_papers.py
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

HARD_DOWNGRADE = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
SOFT_DOWNGRADE = {"KEEP_AS_NON_CORE", "MODIFY"}
NOT_REVIEWED = {"UNREVIEWED", "UNDECIDED", "PENDING"}

ASPECT_SHORT = {
    "molecular_function": "MF",
    "biological_process": "BP",
    "cellular_component": "CC",
}

# Fast literal pre-screen per readout class: a *necessary superset* of tokens
# (lowercase). If none appears in the paper, no pattern in that class can match,
# so we skip the (relatively expensive) IGNORECASE regex entirely. Over-
# inclusive is fine -- the precise regex confirms; only false negatives (a real
# match the screen misses) would be a bug, so keep these broad enough to cover
# every pattern. Must stay in sync with readout_catalog.yaml patterns.
SCREEN: dict[str, tuple[str, ...]] = {
    "UPR_ER_STRESS": ("upre", "erse", "xbp1", "erai", "grp78", "chop",
                      "atf4", "atf6", "bip"),
    "OXIDATIVE_STRESS_ROS": ("cellrox", "dcf", "mitosox", "dihydroethidium",
                             "dhe", "rogfp", "hyper", "amplex"),
    "APOPTOSIS_CASPASE": ("cellevent", "caspase", "annexin", "tunel", "parp",
                          "devd"),
    "AUTOPHAGY_FLUX": ("lc3", "autophag", "p62", "sqstm1"),
    "MITO_MEMBRANE_POTENTIAL": ("tmrm", "tmre", "jc-1",
                                "mitochondrial membrane potential",
                                "mitotracker"),
    "CALCIUM_FLUX": ("fluo", "fura", "gcamp", "calcium", "ca2+"),
    "pH_PROBE": ("phrodo", "phluorin", "snarf", "bcecf"),
    "IRON_PROBE": ("ferhonox", "labile iron", "calcein"),
    "TRANSCRIPTIONAL_REPORTER": ("reporter", "luciferase"),
    "VIABILITY_PROLIFERATION": ("mtt", "mts ", "cck", "resazurin", "alamar",
                                "cell viability", "colony formation", "brdu",
                                "edu", "ki67", "ki-67"),
    "IN_VITRO_ENZYME": ("in vitro", "purified", "specific activity", "kcat",
                        "km", "enzymatic assay", "reconstitut"),
    "DIRECT_BINDING": ("isothermal", "itc", "surface plasmon", "spr",
                       "crystal", "cryo"),
}


def load_catalog(path: Path) -> dict[str, dict[str, Any]]:
    data = yaml.safe_load(path.read_text())
    catalog = data["readouts"]
    for name, spec in catalog.items():
        pats = spec.get("patterns", []) or []
        spec["_compiled"] = re.compile("|".join(f"(?:{p})" for p in pats),
                                       re.IGNORECASE) if pats else None
        spec["_screen"] = SCREEN.get(name, ())
        if pats and not spec["_screen"]:
            raise ValueError(f"readout class {name!r} has patterns but no SCREEN "
                             "entry; add a necessary-superset literal screen")
        alr = spec.get("aligned_label_regex")
        spec["_aligned"] = re.compile(alr, re.IGNORECASE) if alr else None
        spec["_overmapped"] = set(spec.get("commonly_overmapped_to", []) or [])
    return catalog


def build_aspect_map(genes_dir: Path) -> dict[str, str]:
    """Map GO id -> aspect (MF/BP/CC) by scanning every *-goa.tsv once."""
    aspect: dict[str, str] = {}
    for tsv in genes_dir.rglob("*-goa.tsv"):
        try:
            with tsv.open(newline="") as fh:
                reader = csv.DictReader(fh, delimiter="\t")
                for row in reader:
                    go_id = (row.get("GO TERM") or "").strip()
                    asp = (row.get("GO ASPECT") or "").strip()
                    if go_id and asp and go_id not in aspect:
                        aspect[go_id] = ASPECT_SHORT.get(asp, asp)
        except (OSError, csv.Error):
            continue
    return aspect


class PubCache:
    """Read each cached paper once and memoize (readout_classes, has_full_text).

    Detection depends only on the paper text, not on the annotation, so we run
    the ~80 regexes once per unique PMID rather than once per annotation (many
    annotations share a PMID). ``None`` means the paper is not cached.
    """

    def __init__(self, pubs_dir: Path, catalog: dict[str, dict[str, Any]]):
        self.pubs_dir = pubs_dir
        self.catalog = catalog
        self._cache: dict[str, tuple[set[str], bool] | None] = {}

    def detect(self, pmid: str) -> tuple[set[str], bool] | None:
        if pmid in self._cache:
            return self._cache[pmid]
        path = self.pubs_dir / f"PMID_{pmid}.md"
        if not path.exists():
            self._cache[pmid] = None
            return None
        # Keep original case (the HyPer pattern is case-sensitive); screen on a
        # lowercased copy with cheap substring tests, run the precise regex only
        # when the screen passes.
        text = path.read_text()
        low = text.lower()
        classes: set[str] = set()
        for name, spec in self.catalog.items():
            rx = spec["_compiled"]
            if rx is None:
                continue
            if any(lit in low for lit in spec["_screen"]) and rx.search(text):
                classes.add(name)
        result = (classes, "full_text_available: true" in low)
        self._cache[pmid] = result
        return result


def pmid_from_ref(ref: Any) -> str | None:
    if isinstance(ref, str) and ref.startswith("PMID:"):
        return ref.split(":", 1)[1].strip()
    return None


def iter_annotations(genes_dir: Path):
    for path in sorted(genes_dir.rglob("*-ai-review.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        rel = path.relative_to(genes_dir)
        organism = rel.parts[0] if rel.parts else ""
        gene = doc.get("gene_symbol") or (rel.parts[1] if len(rel.parts) > 1 else "")
        for ann in doc.get("existing_annotations", []) or []:
            if isinstance(ann, dict):
                yield organism, gene, ann


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument("--pubs-dir", type=Path, default=Path("publications"))
    ap.add_argument("--catalog", type=Path,
                    default=Path("projects/ASSAY_TO_FUNCTION/readout_catalog.yaml"))
    ap.add_argument("--out-dir", type=Path,
                    default=Path("projects/ASSAY_TO_FUNCTION/reports"))
    args = ap.parse_args()

    catalog = load_catalog(args.catalog)
    aspect_map = build_aspect_map(args.genes_dir)
    pubs = PubCache(args.pubs_dir, catalog)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    n_ann = n_pmid = n_resolved = 0
    missing_pmids: set[str] = set()

    import sys
    print(f"GO->aspect map: {len(aspect_map)} entries. Scanning annotations...",
          file=sys.stderr, flush=True)
    for organism, gene, ann in iter_annotations(args.genes_dir):
        n_ann += 1
        if n_ann % 5000 == 0:
            print(f"  ...{n_ann} annotations, {len(pubs._cache)} papers read",
                  file=sys.stderr, flush=True)
        pmid = pmid_from_ref(ann.get("original_reference_id"))
        if not pmid:
            continue
        n_pmid += 1
        detected = pubs.detect(pmid)
        if detected is None:
            missing_pmids.add(pmid)
            continue
        n_resolved += 1
        readout_classes, full_text = detected

        review = ann.get("review") or {}
        action = (review.get("action") or "").strip() or "UNREVIEWED"
        term = ann.get("term") or {}
        go_id = term.get("id", "")
        go_label = term.get("label", "") or ""
        aspect = aspect_map.get(go_id, "?")

        for name in readout_classes:
            spec = catalog[name]
            aligned = bool(
                go_id in spec["_overmapped"]
                or (spec["_aligned"] and spec["_aligned"].search(go_label))
            )
            rows.append({
                "organism": organism, "gene": gene, "pmid": pmid,
                "go_id": go_id, "go_label": go_label, "aspect": aspect,
                "evidence_type": ann.get("evidence_type", ""),
                "negated": str(bool(ann.get("negated", False))),
                "action": action, "readout_class": name,
                "proximity": spec.get("proximity", ""),
                "convergence": spec.get("convergence", ""),
                "aligned": str(aligned),
                "full_text": str(full_text),
            })

    # --- write match rows ---
    fields = ["organism", "gene", "pmid", "go_id", "go_label", "aspect",
              "evidence_type", "negated", "action", "readout_class",
              "proximity", "convergence", "aligned", "full_text"]
    matches_tsv = args.out_dir / "paper_readout_matches.tsv"
    with matches_tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    actions_order = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY",
                     "MARK_AS_OVER_ANNOTATED", "REMOVE", "UNDECIDED",
                     "UNREVIEWED", "NEW", "PENDING"]
    seen = {r["action"] for r in rows}
    actions_order = [a for a in actions_order if a in seen]
    for a in sorted(seen):
        if a not in actions_order:
            actions_order.append(a)

    def metrics(counts: Counter) -> tuple[int, int, str, str]:
        reviewed = sum(c for a, c in counts.items() if a not in NOT_REVIEWED)
        hard = sum(counts.get(a, 0) for a in HARD_DOWNGRADE)
        soft = sum(counts.get(a, 0) for a in SOFT_DOWNGRADE)
        pct_hard = f"{100*hard/reviewed:.0f}%" if reviewed else "-"
        pct_any = f"{100*(hard+soft)/reviewed:.0f}%" if reviewed else "-"
        return sum(counts.values()), reviewed, pct_hard, pct_any

    def write_crosstab(out: Path, subset: list[dict[str, str]], title: str):
        ct: dict[str, Counter] = defaultdict(Counter)
        for r in subset:
            ct[r["readout_class"]][r["action"]] += 1
        with out.open("w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["readout_class", "proximity", "convergence",
                        "total", "reviewed"] + actions_order
                       + ["pct_removed_or_overann", "pct_any_downgrade"])
            for name, spec in catalog.items():
                counts = ct.get(name)
                if not counts:
                    continue
                total, reviewed, pct_hard, pct_any = metrics(counts)
                w.writerow([name, spec.get("proximity", ""),
                            spec.get("convergence", ""), total, reviewed]
                           + [counts.get(a, 0) for a in actions_order]
                           + [pct_hard, pct_any])
        print(f"\n## {title}")
        print(f"{'readout_class':<26}{'prox':<11}{'conv':<6}"
              f"{'rev':>5}{'rm/OA%':>8}{'anyDn%':>8}")
        print("-" * 64)
        for name, spec in catalog.items():
            counts = ct.get(name)
            if not counts:
                continue
            _, reviewed, pct_hard, pct_any = metrics(counts)
            print(f"{name:<26}{spec.get('proximity',''):<11}"
                  f"{spec.get('convergence',''):<6}"
                  f"{reviewed:>5}{pct_hard:>8}{pct_any:>8}")

    aligned_rows = [r for r in rows if r["aligned"] == "True"]

    print(f"Annotations: {n_ann}; PMID-backed: {n_pmid}; "
          f"paper resolved: {n_resolved}; missing cached papers: "
          f"{len(missing_pmids)}.")
    print(f"GO->aspect map entries: {len(aspect_map)}.")
    print(f"Readout matches (paper mentions): {len(rows)}; "
          f"thematically aligned: {len(aligned_rows)}.")

    write_crosstab(args.out_dir / "paper_action_crosstab_all.tsv",
                   rows, "ALL paper mentions (weak link)")
    write_crosstab(args.out_dir / "paper_action_crosstab_aligned.tsv",
                   aligned_rows,
                   "ALIGNED only (readout matches the annotated process)")

    print("\n## Aspect of ALIGNED annotations (per readout class)")
    asp_ct: dict[str, Counter] = defaultdict(Counter)
    for r in aligned_rows:
        asp_ct[r["readout_class"]][r["aspect"]] += 1
    for name in catalog:
        counts = asp_ct.get(name)
        if counts:
            parts = ", ".join(f"{k}:{v}" for k, v in counts.most_common())
            print(f"  {name:<26} {parts}")

    print(f"\nWrote matches + 2 crosstabs to {args.out_dir}")


if __name__ == "__main__":
    main()
