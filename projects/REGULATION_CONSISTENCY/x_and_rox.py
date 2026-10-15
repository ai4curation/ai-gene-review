#!/usr/bin/env python3
"""Dissect genes annotated both to a process X and to regulation of X.

For every (gene, X) pair in a GAF where the gene has a participant annotation
(X itself, or a non-regulation is_a/part_of descendant) and a regulation-of-X
annotation, record features that bear on which reading is right:

- ``signs``: regulation signs present (+, -, 0 = unsigned).
- ``x_direct``: participant annotation is to X itself, not a descendant.
- ``domain``: coarse branch of X (signaling, metabolism, development, ...).
- ``same_reference``: the participant and regulation rows share a reference
  (one paper produced both, so the curator asserted both readings at once).
- ``part_evidence`` / ``reg_evidence``: experimental / perturbation /
  phylogenetic / electronic / other evidence class on each side.
- ``gocam``: what GO-CAM models say about the gene's activity: ``part_of_x``
  (an activity whose BP is X or a descendant), ``regulates_x`` (BP is a
  regulation of X), ``both``, ``elsewhere`` or ``absent``.
- ``reviewed``: reviewer actions on both sides, when a gene review exists.

Pairs are assigned to an ordered pattern (``classify_pair``), and pattern
counts are tabulated against GO-CAM placement and reviewer actions.

Usage::

    python projects/REGULATION_CONSISTENCY/x_and_rox.py --obo go.obo \\
        --gaf goa_human.gaf.gz --gocam-index gocams/index.tsv --genes-dir genes \\
        --species-dir human --out-dir projects/REGULATION_CONSISTENCY/results
"""

from __future__ import annotations

import argparse
import csv
import gzip
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from regulation_triage import (
    BROAD_TARGET_DESCENDANTS,
    EXPERIMENTAL,
    PERTURBATION,
    PHYLO,
    REGULATOR_MF,
    Ontology,
    write_tsv,
)

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader  # type: ignore[assignment]

CATALYTIC = "GO:0003824"
METABOLIC = "GO:0008152"
DOMAINS = [  # first match wins
    ("GO:0007165", "signal_transduction"),
    ("GO:0002376", "immune_system_process"),
    ("GO:0007049", "cell_cycle"),
    ("GO:0012501", "programmed_cell_death"),
    ("GO:0032502", "developmental_process"),
    ("GO:0010467", "gene_expression"),
    ("GO:0051179", "localization_transport"),
    ("GO:0008152", "metabolic_process"),
    ("GO:0016043", "cellular_component_organization"),
    ("GO:0050896", "response_to_stimulus"),
]


def ev_class(codes: set[str]) -> str:
    """Strongest evidence class among a set of codes.

    >>> ev_class({"IEA", "IMP"}), ev_class({"IBA"}), ev_class({"IDA", "IMP"})
    ('perturbation', 'phylogenetic', 'direct')
    """
    if codes & (EXPERIMENTAL - PERTURBATION):
        return "direct"
    if codes & PERTURBATION:
        return "perturbation"
    if codes & PHYLO:
        return "phylogenetic"
    if "IEA" in codes and len(codes) == 1:
        return "electronic"
    return "other"


def classify_pair(
    signs: str,
    same_ref: bool,
    part_ev: str,
    reg_ev: str,
    regulator_mf: bool,
    own_step: bool = False,
) -> str:
    """Ordered pattern for an X + regulation-of-X pair.

    ``own_step`` means the gene's own activity is a step of X: either one of its
    MF annotations reaches X via is_a/part_of, or (because go.obo has few
    MF-to-BP part_of links) it has catalytic activity and X is a metabolic
    process, including protein modification. The participant reading is then
    grounded in what the gene product does.

    >>> classify_pair("+", True, "direct", "direct", False, own_step=True)
    'own_activity_is_step_of_x'
    >>> classify_pair("+", True, "direct", "direct", False)
    'same_paper_both_readings'
    >>> classify_pair("-", False, "direct", "perturbation", True)
    'inhibitor_also_participant'
    >>> classify_pair("+", False, "phylogenetic", "perturbation", False)
    'mixed_sources'
    """
    if own_step:
        return "own_activity_is_step_of_x"
    if same_ref:
        return "same_paper_both_readings"
    if "-" in signs and "+" not in signs:
        return "inhibitor_also_participant"
    if {part_ev, reg_ev} & {"phylogenetic", "electronic"} and part_ev != reg_ev:
        return "mixed_sources"
    if regulator_mf:
        return "activator_with_regulator_activity"
    return "component_as_activator"


def load_gaf(path: Path, onto: Ontology) -> tuple[dict, dict]:
    """symbol -> term -> [(evidence, reference)]; symbol -> UniProt id."""
    rows: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    ids: dict[str, str] = {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 15 or "NOT" in f[3].split("|"):
                continue
            t = onto.canon(f[4])
            if t in onto.name:
                rows[f[2]][t].append((f[6], f[5]))
                ids[f[2]] = f"{f[0]}:{f[1]}"
    return rows, ids


def load_gocam(path: Path) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    with path.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["biological_process"]:
                out[r["gene_product"]].add(r["biological_process"])
    return out


def load_reviews(
    genes_dir: Path, species: str, onto: Ontology
) -> dict[str, dict[str, set[str]]]:
    out: dict[str, dict[str, set[str]]] = {}
    for p in sorted((genes_dir / species).glob("*/*-ai-review.yaml")):
        try:
            d = yaml.load(p.read_text(encoding="utf-8"), Loader=Loader)
        except yaml.YAMLError:
            continue
        if not isinstance(d, dict):
            continue
        acts: dict[str, set[str]] = defaultdict(set)
        for a in d.get("existing_annotations") or []:
            if isinstance(a, dict) and not a.get("negated"):
                t = (a.get("term") or {}).get("id")
                act = (a.get("review") or {}).get("action")
                if t and act:
                    acts[onto.canon(t)].add(act)
        out[p.parent.name] = acts
    return out


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--obo", type=Path, required=True)
    ap.add_argument("--gaf", type=Path, required=True)
    ap.add_argument("--gocam-index", type=Path, default=Path("gocams/index.tsv"))
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument("--species-dir", default="human")
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()

    onto = Ontology.from_obo(args.obo)
    bp = [t for t in onto.name if onto.namespace[t] == "biological_process"]
    n_desc: Counter = Counter(a for t in bp for a in onto.ancestors(t))
    reg_mf = {t for t in onto.name if any(r in onto.ancestors(t) for r in REGULATOR_MF)}
    catalytic_mf = {t for t in onto.name if CATALYTIC in onto.ancestors(t)}
    gaf, ids = load_gaf(args.gaf, onto)
    gocam = load_gocam(args.gocam_index)
    reviews = load_reviews(args.genes_dir, args.species_dir, onto)

    rows = []
    for gene, terms in sorted(gaf.items()):
        bp_terms = {
            t: v
            for t, v in terms.items()
            if onto.namespace.get(t) == "biological_process"
        }
        regulator = any(t in reg_mf for t in terms)
        mf_terms = [t for t in terms if onto.namespace.get(t) == "molecular_function"]
        catalytic = any(t in catalytic_mf for t in mf_terms) and not regulator
        part_by_anc: dict[str, set[str]] = defaultdict(set)
        for t in bp_terms:
            if not onto.is_reg(t):
                for a in onto.ancestors(t):
                    part_by_anc[a].add(t)
        reg_by_target: dict[str, dict[str, list[str]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for t in bp_terms:
            for sign, x in onto.reg_targets(t):
                reg_by_target[x][sign].append(t)
        cam_bps = gocam.get(ids.get(gene, ""), set())
        for x, by_sign in reg_by_target.items():
            parts = part_by_anc.get(x, set())
            if n_desc[x] > BROAD_TARGET_DESCENDANTS:
                parts = parts & {x}
            if not parts:
                continue
            reg_terms = {t for ts in by_sign.values() for t in ts}
            part_rows = [r for p in parts for r in bp_terms[p]]
            reg_rows = [r for t in reg_terms for r in bp_terms[t]]
            refs_p = {r[1] for r in part_rows if not r[1].startswith("GO_REF")}
            refs_r = {r[1] for r in reg_rows if not r[1].startswith("GO_REF")}
            same_ref = bool(refs_p & refs_r)
            part_ev = ev_class({r[0] for r in part_rows})
            reg_ev = ev_class({r[0] for r in reg_rows})
            signs = "".join(sorted(by_sign))
            domain = next(
                (lab for root, lab in DOMAINS if root in onto.ancestors(x)), "other"
            )
            if not cam_bps:
                cam = "absent"
            else:
                on_x = any(
                    x in onto.ancestors(b) and not onto.is_reg(b) for b in cam_bps
                )
                reg_x = any(
                    any(tx == x for _, tx in onto.reg_targets(b)) for b in cam_bps
                )
                cam = (
                    "both"
                    if on_x and reg_x
                    else "part_of_x"
                    if on_x
                    else "regulates_x"
                    if reg_x
                    else "elsewhere"
                )
            own_steps = sorted(m for m in mf_terms if x in onto.ancestors(m))
            enzyme_in_x = catalytic and METABOLIC in onto.ancestors(x)
            rev = reviews.get(gene)
            reviewed = ""
            if rev:
                pa = sorted(set().union(*(rev.get(p, set()) for p in parts)))
                ra = sorted(set().union(*(rev.get(t, set()) for t in reg_terms)))
                if pa and ra:
                    reviewed = f"part={'/'.join(pa)};reg={'/'.join(ra)}"
            rows.append(
                {
                    "gene": gene,
                    "x": x,
                    "x_label": onto.name[x],
                    "domain": domain,
                    "signs": signs,
                    "x_direct": "yes" if x in parts else "no",
                    "participant_terms": ",".join(sorted(parts)[:4]),
                    "regulation_terms": ",".join(sorted(reg_terms)[:4]),
                    "same_reference": "yes" if same_ref else "no",
                    "shared_refs": ",".join(sorted(refs_p & refs_r)[:3]),
                    "part_evidence": part_ev,
                    "reg_evidence": reg_ev,
                    "regulator_mf": "yes" if regulator else "no",
                    "own_mf_step_of_x": ",".join(own_steps[:3]),
                    "enzyme_in_metabolic_x": "yes" if enzyme_in_x else "no",
                    "gocam": cam,
                    "pattern": classify_pair(
                        signs,
                        same_ref,
                        part_ev,
                        reg_ev,
                        regulator,
                        bool(own_steps) or enzyme_in_x,
                    ),
                    "reviewed": reviewed,
                }
            )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_tsv(args.out_dir / "x_and_rox_pairs.tsv", rows)

    def tab(*keys: str) -> dict:
        c = Counter(tuple(r[k] for k in keys) for r in rows)
        return {"|".join(k): n for k, n in c.most_common()}

    def review_split(key: str) -> dict:
        out: dict[str, Counter] = defaultdict(Counter)
        for r in rows:
            if not r["reviewed"]:
                continue
            part, reg = r["reviewed"].split(";")
            p_keep = any(a in part for a in ("ACCEPT", "KEEP_AS_NON_CORE"))
            r_keep = any(a in reg for a in ("ACCEPT", "KEEP_AS_NON_CORE"))
            verdict = {
                (True, True): "both_kept",
                (True, False): "participant_kept_only",
                (False, True): "regulation_kept_only",
                (False, False): "neither_kept",
            }[(p_keep, r_keep)]
            out[r[key]][verdict] += 1
        return {k: dict(v.most_common()) for k, v in out.items()}

    summary = {
        "pairs": len(rows),
        "genes": len({r["gene"] for r in rows}),
        "x_direct": tab("x_direct"),
        "signs": tab("signs"),
        "domain": tab("domain"),
        "same_reference": tab("same_reference"),
        "evidence_part_vs_reg": tab("part_evidence", "reg_evidence"),
        "pattern": tab("pattern"),
        "pattern_by_signs": tab("pattern", "signs"),
        "pattern_by_domain": tab("pattern", "domain"),
        "gocam": tab("gocam"),
        "pattern_by_gocam": tab("pattern", "gocam"),
        "reviewed_pairs": sum(1 for r in rows if r["reviewed"]),
        "review_verdict_by_pattern": review_split("pattern"),
        "review_verdict_by_signs": review_split("signs"),
        "review_verdict_by_gocam": review_split("gocam"),
        "top_x": dict(
            Counter(f"{r['x']} {r['x_label']}" for r in rows).most_common(30)
        ),
    }
    (args.out_dir / "x_and_rox_summary.yaml").write_text(
        yaml.safe_dump(summary, sort_keys=False, width=100)
    )
    print(yaml.safe_dump(summary, sort_keys=False, width=100))


if __name__ == "__main__":
    main()
