#!/usr/bin/env python3
"""Select the propagation-ready SAFE subset of cazy2go and write cazy2go.safe.sssom.yaml.

From the full reproducible derivation (CAZy family -> EC -> ec2go -> GO MF), keep only rows that are
SAFE to propagate at the family level and that genuinely add over interpro2go:

  1. MONO-SPECIFIC family: the family's ECs resolve (after generic-parent filtering) to exactly ONE
     GO MF term  -> safe to attribute to the whole family (skos:exactMatch).
  2. SPECIFIC term: that term is not itself a generic parent (glycosyltransferase activity, etc.).
  3. REAL GAIN vs interpro2go: under GO is_a closure the term is ALTITUDE_GAIN (InterPro gives only a
     generic ancestor) or TRUE_GAP (InterPro silent) -- not exact/descendant-masked.

Object labels are taken from the local GO ontology (oaklib sqlite:obo:go), so the emitted SSSOM
passes linkml-term-validator label checks exactly. This file is the curated, propagation-ready
companion to the hand-annotated cazy2go.sssom.yaml seed and the full cazy2go.generated.sssom.yaml.

Usage:  uv run python projects/GLYCOBIOLOGY/select_cazy2go_safe.py \
            -o projects/GLYCOBIOLOGY/cazy2go.safe.sssom.yaml
"""

from __future__ import annotations

import argparse
import datetime
import sys
from collections import Counter

import yaml

sys.path.insert(0, "projects/GLYCOBIOLOGY")
from build_cazy2go import GENERIC_PARENTS, load_ec2go  # noqa: E402
from compare_cazy_interpro import (  # noqa: E402
    cazy_go_for_family,
    load_cazy_ec_interpro,
    load_interpro2go,
)

from oaklib import get_adapter  # noqa: E402
from oaklib.datamodels.vocabulary import IS_A  # noqa: E402

# Families backed by a completed gene review in this project (manual provenance + reference).
REVIEW_BACKED = {
    "GT13": "MGAT1 (P26572) review",
    "GT65": "POFUT1 (Q9H488) review",
}

# Hand-review (cazy2go-truegap-review.md) found systematic artifacts to exclude from the SAFE set:
#  * CBM* families are non-catalytic carbohydrate-binding modules -- any EC on a member belongs to its
#    appended catalytic domain, not the CBM. Skip all CBM families.
#  * A CAZyme family mapping to a PEPTIDASE MF (GO:0008233 descendants) is multidomain bleed-through
#    (e.g. GT44 clostridial-toxin autoprotease domain), not the family's activity. Drop.
#  * GO:0016837 (carbon-oxygen lyase acting on polysaccharides) is reached only via the partial
#    EC 4.2.2.- and is too generic for a safe family-level row; treat as a generic parent.
PEPTIDASE_ROOT = "GO:0008233"
SAFE_EXTRA_GENERIC = {"GO:0016837"}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", default="projects/GLYCOBIOLOGY/cazy2go.safe.sssom.yaml")
    args = ap.parse_args()

    print("Loading ec2go, interpro2go, UniProt, GO closure ...", file=sys.stderr)
    ec2go = load_ec2go()
    ipr2go = load_interpro2go()
    fam_ec, fam_ipr, fam_mem = load_cazy_ec_interpro()
    go = get_adapter("sqlite:obo:go")
    _anc: dict[str, set[str]] = {}

    def anc(c: str) -> set[str]:
        if c not in _anc:
            a = set(go.ancestors(c, predicates=[IS_A]))
            a.discard(c)
            _anc[c] = a
        return _anc[c]

    rows = []
    stats = Counter()
    for fam in sorted(fam_ec, key=lambda f: (f[:2], int("".join(filter(str.isdigit, f)) or 0))):
        if fam.startswith("CBM"):
            stats["dropped_cbm_noncatalytic"] += 1
            continue  # non-catalytic binding module (hand-review artifact class)
        cazy_go = cazy_go_for_family(fam_ec[fam], ec2go)
        if len(cazy_go) != 1:
            continue  # not mono-specific
        go_id, _ec2go_label = next(iter(cazy_go.items()))
        if go_id in GENERIC_PARENTS or go_id in SAFE_EXTRA_GENERIC:
            stats["dropped_generic"] += 1
            continue  # term too generic to be a useful family mapping
        if PEPTIDASE_ROOT in anc(go_id):
            stats["dropped_peptidase_artifact"] += 1
            continue  # CAZyme family -> peptidase MF = multidomain bleed-through (e.g. GT44)
        # closure classification vs interpro2go
        ipr_go = set()
        for ipr in fam_ipr[fam]:
            ipr_go |= ipr2go.get(ipr, set())
        if go_id in ipr_go or any(go_id in anc(i) for i in ipr_go):
            stats["dropped_masked"] += 1
            continue  # exact- or descendant-masked: InterPro already gives >= specific
        cls = "altitude_gain" if any(i in anc(go_id) for i in ipr_go) else "true_gap"
        stats[cls] += 1

        ecs = sorted({e for e in fam_ec[fam] if any(g == go_id for g, _ in ec2go.get(e, []))})
        label = go.label(go_id) or _ec2go_label  # authoritative current GO label
        backing = REVIEW_BACKED.get(fam)
        comment = (
            f"Mono-specific family -> single GO MF (skos:exactMatch). "
            f"Closure class vs interpro2go: {cls.upper().replace('_', ' ')} "
            f"({'InterPro gives only a generic ancestor' if cls == 'altitude_gain' else 'InterPro silent on this branch'}). "
            f"Via EC {','.join(ecs)} (ec2go). {len(fam_mem[fam])} reviewed Swiss-Prot member(s)."
        )
        if backing:
            comment += f" Review-backed: {backing}."
        rows.append({
            "subject_id": f"CAZy:{fam}",
            "subject_label": fam,
            "predicate_id": "skos:exactMatch",
            "predicate_label": "exact match",
            "object_id": go_id,
            "object_label": label,
            "mapping_justification": (
                "semapv:ManualMappingCuration" if backing else "semapv:CompositeMatching"
            ),
            "comment": comment,
        })

    header = (
        "# CAZy family -> GO molecular-function: SAFE propagation set (SSSOM) -- GENERATED\n"
        "#\n"
        "# Auto-selected by projects/GLYCOBIOLOGY/select_cazy2go_safe.py: families that are (1) MONO-\n"
        "# specific (ECs resolve to a single GO MF), (2) the term is specific (not a generic parent),\n"
        "# and (3) a closure-confirmed GAIN over interpro2go (altitude_gain or true_gap). These are\n"
        "# safe to propagate at the family level (skos:exactMatch). Poly-specific families are NOT\n"
        "# here -- they need subfamily resolution and live in cazy2go.generated.sssom.yaml.\n"
        "# Object labels are taken from the GO ontology (oaklib) so term validation passes.\n"
        f"# Generated: {datetime.date.today().isoformat()} | rows={stats['altitude_gain'] + stats['true_gap']} "
        f"(altitude_gain={stats['altitude_gain']}, true_gap={stats['true_gap']}); "
        f"dropped: generic_term={stats['dropped_generic']}, interpro_masked={stats['dropped_masked']}\n"
    )
    doc = {
        "curie_map": {
            "CAZy": "http://www.cazy.org/",
            "GO": "http://purl.obolibrary.org/obo/GO_",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "semapv": "https://w3id.org/semapv/vocab/",
            "sssom": "https://w3id.org/sssom/",
        },
        "mapping_set_id": "https://w3id.org/ai4curation/ai-gene-review/mappings/cazy2go-safe",
        "mapping_set_title": "CAZy family -> GO molecular function (safe propagation set)",
        "mapping_set_description": (
            "Curated, propagation-ready CAZy-family -> GO MF mappings: mono-specific families whose "
            "single specific GO MF term is a closure-confirmed gain over interpro2go. Safe to "
            "propagate at family level. Companion to cazy2go.sssom.yaml (hand seed) and "
            "cazy2go.generated.sssom.yaml (full derivation)."
        ),
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator_label": ["AI Gene Review project (select_cazy2go_safe.py)"],
        "mappings": rows,
    }
    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(header)
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100)
    print(f"Wrote {args.output}: {dict(stats)} ({len(rows)} rows)", file=sys.stderr)


if __name__ == "__main__":
    main()
