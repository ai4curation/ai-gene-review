"""Triage ligand gap check failures, using the other species as comparators.

For a failing (organism, pathway term P):
  O / G   per-organism curator flag from curated/organism_flags.yaml
  X / Y   term-level curator label from curated/term_labels.yaml (no host protein ligand expected)
otherwise donor ligands are collected from (a) species of the same lineage where P passes and
(b) curated/expected_ligands.yaml, and the same-symbol gene in the failing organism is looked up
(case-insensitive; zebrafish a/b/.1/.2 paralog suffixes allowed):
  C  donor's counterpart is in P but has no receptor ligand activity MF
  B  donor's counterpart is on a related pathway term (shares a specific is_a ancestor with P;
     ancestors with >= 40 pathway descendants count as generic), not on P
  A  donor's counterpart is annotated in the GAF but not to P or a related term
  N  no same-symbol gene is annotated in the GAF (absent, unannotated, or a naming mismatch)
  U  no donor available
Lineages: vertebrate (human, mouse, rat, zebrafish) vs non-vertebrate (fly, yeast, pombe);
symbols are not matched across lineages.

Writes results/triage.json and results/RESULTS.md.

Usage (after ligand_gap_check.py):
  uv run python projects/LIGANDS_IN_SIGNALING/scripts/triage.py \
      --data .cache/ligands_in_signaling --results projects/LIGANDS_IN_SIGNALING/results
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from go_ontology import GO  # noqa: E402
from ligand_gap_check import (  # noqa: E402
    CELL_SURFACE,
    GPCR,
    LIGAND_ACTIVITY,
    ORGANISMS,
    SIGNAL_TRANSDUCTION,
    read_gaf,
)

VERTEBRATE = {"human", "mouse", "rat", "zebrafish"}
CURATED = Path(__file__).resolve().parent.parent / "curated"
CATEGORY_LABELS = {
    "A": "ligand counterpart not on the pathway",
    "B": "ligand counterpart only on a related pathway term",
    "C": "ligand counterpart on the pathway but lacks a ligand-activity MF",
    "N": "no same-symbol ligand counterpart annotated",
    "U": "no donor ligand available",
    "X": "no protein ligand expected (small molecule, light, microbial)",
    "Y": "antigen, contact or ligand-independent",
    "O": "suspect over-annotation",
    "G": "misapplied or generic term",
}
ORDER = ["A", "B", "C", "N", "U", "X", "Y", "O", "G"]


def gene_index(go: GO, gaf: Path) -> dict:
    idx = collections.defaultdict(lambda: {"ligand_mf": False, "bp": set()})
    for c in read_gaf(gaf):
        sym, qual, term, aspect = c[2], c[3], c[4], c[8]
        rec = idx[sym]
        if aspect == "F" and qual == "enables" and LIGAND_ACTIVITY in go.ancestors(term):
            rec["ligand_mf"] = True
        elif aspect == "P" and qual == "involved_in":
            rec["bp"].add(term)
    return idx


def counterparts(org: str, donor: str, idx: dict) -> list[str]:
    key = donor.lower()
    out = []
    for sym in idx:
        s = sym.lower()
        if s == key or (org == "zebrafish" and s in (key + "a", key + "b", key + ".1", key + ".2")):
            out.append(sym)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=Path(".cache/ligands_in_signaling"))
    ap.add_argument("--results", type=Path, required=True)
    ap.add_argument("--orgs", nargs="*", default=list(ORGANISMS))
    args = ap.parse_args()

    go = GO(args.data / "go-basic.obo")
    pathways = go.descendants_of_any({CELL_SURFACE, GPCR})
    n_desc = collections.Counter(a for t in pathways for a in go.ancestors(t) if a != t)
    generic = {t for t, c in n_desc.items() if c >= 40} | {CELL_SURFACE, GPCR, SIGNAL_TRANSDUCTION}

    with (CURATED / "term_labels.yaml").open() as fh:
        labels = {r["term"]: r for r in yaml.safe_load(fh)["term_labels"]}
    with (CURATED / "expected_ligands.yaml").open() as fh:
        expected = {
            lineage: {r["term"]: r["expected_ligands"] for r in rows}
            for lineage, rows in yaml.safe_load(fh)["expected_ligands"].items()
        }
    with (CURATED / "organism_flags.yaml").open() as fh:
        flags = {
            org: {r["term"]: r for r in rows}
            for org, rows in yaml.safe_load(fh)["organism_flags"].items()
        }

    checks = {o: json.loads((args.results / f"gapcheck-{o}.json").read_text()) for o in args.orgs}
    by_term = collections.defaultdict(dict)
    for o, res in checks.items():
        for r in res["rows"]:
            by_term[r["term"]][o] = r
    idx = {o: gene_index(go, args.data / f"{ORGANISMS[o]}.gaf.gz") for o in args.orgs}

    triaged = []
    for term, per_org in by_term.items():
        passing = {o: r for o, r in per_org.items() if r["n_ligand_genes"] > 0}
        for org, r in per_org.items():
            if r["n_ligand_genes"] > 0:
                continue
            rec = dict(org=org, term=term, name=r["name"], n_genes=r["n_genes"], genes=r["genes"],
                       binding_only_genes=r["binding_only_genes"], passes_in=sorted(passing), lookups=[])
            flag = flags.get(org, {}).get(term)
            if flag:
                rec.update(category=flag["category"], note=flag.get("note", ""))
            elif term in labels:
                rec.update(category=labels[term]["category"], note=labels[term].get("reason", ""))
            else:
                lineage = "vertebrate" if org in VERTEBRATE else ("fly" if org == "fly" else None)
                donors = collections.defaultdict(list)
                for porg, pr in passing.items():
                    if (org in VERTEBRATE) == (porg in VERTEBRATE):
                        for s in pr["ligand_genes"]:
                            donors[s.upper()].append(porg)
                for s in expected.get(lineage, {}).get(term, []):
                    donors[s.upper()].append("expected_ligands.yaml")
                anc_p = go.ancestors(term) - {term} - generic
                best, priority = None, {"C": 0, "B": 1, "A": 2, "N": 3}
                for donor, sources in sorted(donors.items()):
                    hits = counterparts(org, donor, idx[org])
                    if not hits:
                        rec["lookups"].append(dict(donor=donor, sources=sources, result="N"))
                        best = best or "N"
                        continue
                    for sym in hits:
                        bp = idx[org][sym]["bp"]
                        in_p = any(term in go.ancestors(t, True) for t in bp)
                        related = sorted({go.name[t] for t in bp if t in pathways and (go.ancestors(t) & anc_p)})
                        result = "C" if in_p else ("B" if related else "A")
                        rec["lookups"].append(dict(
                            donor=donor, sources=sources, symbol=sym, result=result,
                            ligand_mf=idx[org][sym]["ligand_mf"], related_terms=related[:3],
                            signaling_terms=sorted({go.name[t] for t in bp
                                                    if SIGNAL_TRANSDUCTION in go.ancestors(t, True)})[:3]))
                        if best is None or priority[result] < priority[best]:
                            best = result
                rec.update(category=best or "U", note="")
            triaged.append(rec)

    triaged.sort(key=lambda r: (args.orgs.index(r["org"]), ORDER.index(r["category"]), -r["n_genes"]))
    (args.results / "triage.json").write_text(json.dumps(triaged, indent=1))

    counts = collections.Counter((r["org"], r["category"]) for r in triaged)
    go_version = next(iter(checks.values()))["go_version"]
    lines = [
        "---",
        'title: "Ligand gap check: results"',
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Ligand gap check: results",
        "",
        "Generated by `scripts/ligand_gap_check.py` and `scripts/triage.py`; do not edit by hand.",
        f"GO version: {go_version}. GAFs: current.geneontology.org at run time.",
        "",
        "## Pathway terms per organism",
        "",
        "| Organism | Pathway terms used | No ligand gene | Ligand-activity genes | Ligand genes in no signaling term |",
        "|---|---|---|---|---|",
    ]
    for o, res in checks.items():
        n = len(res["rows"])
        f = sum(1 for r in res["rows"] if r["n_ligand_genes"] == 0)
        lines.append(f"| {o} | {n} | {f} | {res['n_ligand_activity_genes']} | "
                     f"{len(res['ligand_genes_not_in_any_signaling'])} |")
    lines += ["", "## Failures by triage category", "",
              "| Category | " + " | ".join(args.orgs) + " |", "|---|" + "---|" * len(args.orgs)]
    for c in ORDER:
        lines.append(f"| {c}: {CATEGORY_LABELS[c]} | " + " | ".join(str(counts[(o, c)]) for o in args.orgs) + " |")
    lines += ["", "## Curation candidates (categories A, B, C)", "",
              "| Organism | Term | Category | Ligand lookups |", "|---|---|---|---|"]
    for r in triaged:
        if r["category"] not in ("A", "B", "C"):
            continue
        looks = "; ".join(
            f"{x.get('symbol') or x['donor']}: {x['result']}"
            + (" (ligand MF)" if x.get("ligand_mf") else "")
            + (f" on {x['related_terms'][0]}" if x.get("related_terms") and x["result"] == "B" else "")
            for x in r["lookups"] if x["result"] in ("A", "B", "C"))
        lines.append(f"| {r['org']} | {r['name']} ({r['term']}) | {r['category']} | {looks} |")
    lines += ["", "## Ligand-activity genes in no signaling term", ""]
    for o, res in checks.items():
        lines.append(f"- **{o}**: {', '.join(res['ligand_genes_not_in_any_signaling']) or 'none'}")
    (args.results / "RESULTS.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:30]))


if __name__ == "__main__":
    main()
