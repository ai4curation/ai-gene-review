#!/usr/bin/env python3
"""Substrate-specificity and reaction-chaining check for a module YAML.

For every reaction annoton in a ModuleReview document this script:

1. reads the annoton's GO molecular-function term;
2. resolves that GO MF -> RHEA reaction(s) using the **local OAK** GO adapter
   (``sqlite:obo:go`` sssom mappings) -- NOT a web service;
3. fetches each RHEA reaction's balanced equation (substrate specificity) from
   the local OAK RHEA adapter (``sqlite:obo:rhea``);
4. for each ``PRECEDES`` connection between steps, checks whether a CoA-bearing
   product of the upstream reaction also appears as a substrate of the
   downstream reaction (i.e. the output of one reaction matches the input of
   the next).

Nothing here is hard-coded: the RHEA ids and equations are pulled live from the
local ontology databases, so the check reflects the current GO<->RHEA mapping.
A step may legitimately have no clean match (RHEA master reactions are written
in a single canonical direction and one GO MF can map to several RHEA variants);
such cases are reported, not silently passed.

Usage:
    uv run python modules/fatty_acid_beta_oxidation/rhea_chaining_check.py \
        modules/fatty_acid_beta_oxidation.yaml
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable, Optional

import yaml
from oaklib import get_adapter

GO = get_adapter("sqlite:obo:go")
RHEA = get_adapter("sqlite:obo:rhea")

# Chain-length qualifiers we strip so that, e.g., "a very-long-chain (2E)-enoyl-CoA"
# and "a medium-chain (2E)-enoyl-CoA" both normalize to "(2E)-enoyl-CoA". This is
# deliberate: the chaining question is about the reaction-intermediate identity,
# while chain-length specificity is reported separately from the raw equation.
CHAIN_QUALIFIERS = [
    "very-long-chain",
    "long-chain",
    "medium-chain",
    "short-chain",
    "2,3-saturated",
    "4-saturated",
]


def strip_article(token: str) -> str:
    token = token.strip()
    token = re.sub(r"^(a|an)\s+", "", token)
    # drop leading stoichiometric coefficient, e.g. "2 acetyl-CoA"
    token = re.sub(r"^\d+\s+", "", token)
    return token.strip()


def normalize_species(token: str) -> str:
    """Canonicalize a participant name for cross-reaction comparison.

    RHEA names the same backbone several ways ('a long-chain (3S)-3-hydroxy
    fatty acyl-CoA' vs 'a (3S)-3-hydroxyacyl-CoA'). We strip chain-length and
    'fatty' qualifiers, then reduce to alphanumerics so naming variants of the
    *same* intermediate collapse, while genuinely different species (e.g.
    (2E)- vs (3E)-enoyl-CoA) stay distinct.
    """
    t = strip_article(token).lower()
    for q in CHAIN_QUALIFIERS:
        t = t.replace(q, "")
    t = t.replace("fatty", "")
    t = re.sub(r"[^a-z0-9]", "", t)  # drop spaces, hyphens, parens
    return t


def parse_equation(equation: str) -> tuple[list[str], list[str]]:
    """Split a RHEA equation 'L = R' into (left, right) participant lists."""
    if "=" not in equation:
        return [], []
    left, right = equation.split("=", 1)
    lhs = [strip_article(x) for x in left.split(" + ") if x.strip()]
    rhs = [strip_article(x) for x in right.split(" + ") if x.strip()]
    return lhs, rhs


def coa_species(participants: Iterable[str]) -> set[str]:
    """CoA-bearing species (the carbon carriers that thread the spiral)."""
    return {normalize_species(p) for p in participants if "coa" in p.lower()}


def go_to_rhea(go_id: str) -> list[str]:
    """All RHEA ids mapped from a GO term via the local OAK GO adapter."""
    out: list[str] = []
    for m in GO.sssom_mappings([go_id]):
        obj = str(getattr(m, "object_id", ""))
        if obj.startswith("RHEA:") and obj not in out:
            out.append(obj)
    return out


def pick_generic(rhea_ids: list[str]) -> Optional[str]:
    """Pick a representative class-level reaction.

    Prefer a reaction whose equation uses a generic acyl-CoA class (contains
    'acyl-coa') over chain-specific instances (e.g. 'hexadecanoyl-CoA'); among
    candidates, prefer the lowest numeric id (the RHEA master reaction).
    """
    def key(rid: str) -> int:
        return int(rid.split(":")[1])

    generic = []
    for rid in rhea_ids:
        label = RHEA.label(rid) or ""
        if "acyl-coa" in label.lower():
            generic.append(rid)
    pool = generic or rhea_ids
    return sorted(pool, key=key)[0] if pool else None


def iter_reaction_annotons(doc: dict):
    """Yield (step_id, order, annoton) for every reaction annoton, in order.

    Walks parts -> node -> (annotons | variant_sets -> variants -> annotons).
    """
    module = doc.get("module", {})
    for part in sorted(module.get("parts", []), key=lambda p: p.get("order", 0)):
        node = part.get("node", {})
        step_id = node.get("id")
        order = part.get("order")
        # direct annotons
        for ann in node.get("annotons", []) or []:
            yield step_id, order, None, ann
        # variant annotons
        for vs in node.get("variant_sets", []) or []:
            for variant in vs.get("variants", []) or []:
                for ann in variant.get("annotons", []) or []:
                    yield step_id, order, variant.get("id"), ann


def main(path: str) -> int:
    doc = yaml.safe_load(Path(path).read_text())
    module = doc.get("module", {})

    # step_id -> list of {variant, go_id, go_label, rhea, equation, lhs, rhs}
    steps: dict[str, list[dict]] = {}
    order_of: dict[str, int] = {}

    print(f"# RHEA substrate-specificity & chaining check for {path}\n")
    print("## Per-step grounding (GO MF -> RHEA via local OAK go.db)\n")

    for step_id, order, variant_id, ann in iter_reaction_annotons(doc):
        fn = ann.get("function") or {}
        term = fn.get("term") or {}
        go_id = term.get("id")
        go_label = term.get("label")
        if not go_id:
            continue
        order_of[step_id] = order
        rhea_ids = go_to_rhea(go_id)
        chosen = pick_generic(rhea_ids)
        equation = RHEA.label(chosen) if chosen else None
        lhs, rhs = parse_equation(equation) if equation else ([], [])
        rec = {
            "variant": variant_id,
            "go_id": go_id,
            "go_label": go_label,
            "rhea_all": rhea_ids,
            "rhea": chosen,
            "equation": equation,
            "lhs": lhs,
            "rhs": rhs,
        }
        steps.setdefault(step_id, []).append(rec)
        print(f"- **{step_id}** / {variant_id or '(direct)'}")
        print(f"    - GO MF: {go_id} {go_label}")
        print(f"    - RHEA mapped: {', '.join(rhea_ids) if rhea_ids else 'NONE'}")
        print(f"    - representative: {chosen or 'NONE'}")
        if equation:
            print(f"    - equation: {equation}")
        print()

    # Chaining check over PRECEDES connections
    print("## Reaction chaining check (PRECEDES: does an upstream CoA product"
          " feed a downstream CoA substrate?)\n")
    conns = [c for c in module.get("connections", [])
             if c.get("connection_type") == "PRECEDES"]
    if not conns:
        print("No PRECEDES connections found.\n")

    exit_code = 0
    for c in conns:
        src, tgt = c.get("source"), c.get("target")
        src_recs, tgt_recs = steps.get(src, []), steps.get(tgt, [])
        # CoA species across all variants of each step, both sides of the
        # (direction-agnostic) RHEA master equation.
        src_species: set[str] = set()
        for r in src_recs:
            src_species |= coa_species(r["lhs"]) | coa_species(r["rhs"])
        tgt_species: set[str] = set()
        for r in tgt_recs:
            tgt_species |= coa_species(r["lhs"]) | coa_species(r["rhs"])
        shared = src_species & tgt_species
        verdict = "OK" if shared else "NO SHARED CoA INTERMEDIATE"
        if not shared:
            exit_code = 1
        print(f"- {src} (#{order_of.get(src)}) -> {tgt} (#{order_of.get(tgt)}): "
              f"**{verdict}**")
        print(f"    - upstream CoA species: {sorted(src_species)}")
        print(f"    - downstream CoA species: {sorted(tgt_species)}")
        if shared:
            print(f"    - shared intermediate(s): {sorted(shared)}")
        print()

    print("## Notes\n")
    print("- A 'NO SHARED CoA INTERMEDIATE' verdict does not necessarily mean the")
    print("  pathway is wrong: one GO MF can map to several RHEA variants, and the")
    print("  representative chosen here is the lowest-id generic reaction. RHEA")
    print("  master equations are written in one canonical direction, so the carbon")
    print("  carrier may appear on either side. Inspect the equations above before")
    print("  concluding a real gap.")
    return exit_code


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else \
        "modules/fatty_acid_beta_oxidation.yaml"
    raise SystemExit(main(target))
