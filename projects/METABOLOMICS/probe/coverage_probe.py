#!/usr/bin/env python3
"""Coverage probe: how much does protonation-state normalization recover when
bridging metabolomics metabolites to GO via Rhea + rhea2go?

Pipeline tested (the metabolomics -> GO bridge):

    metabolite name / ChEBI (neutral, as a repository reports it)
        -> ChEBI protonation family (all charge states)            [chebi.py]
        -> Rhea reactions using any family member                  [rhea.py]
        -> GO molecular-function terms via rhea2go                 [rhea.py]

For each metabolite we compare:

* EXACT      : match the single reported (neutral) ChEBI id against Rhea.
* NORMALIZED : match ANY member of its protonation family against Rhea.

The gap between the two is the value of protonation normalization. Everything is
computed live (OLS4 + Rhea REST + GO rhea2go) and cached under ``.cache/``; no
results are hardcoded. A run with no Rhea/OLS access will fail loudly rather than
fabricate numbers.

Usage:
    uv run python coverage_probe.py                 # built-in demo metabolite set
    uv run python coverage_probe.py --names-file f  # one metabolite name per line
    uv run python coverage_probe.py --chebi-file f  # one ChEBI:xxxx per line (real study)
    uv run python coverage_probe.py --write-results # also (re)write RESULTS.md
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import chebi
import rhea

# A stand-in for a typical untargeted-metabolomics readout: central-carbon,
# amino-acid, nucleotide and cofactor metabolites. Given as NAMES (not ids) so
# the script resolves + verifies every ChEBI id live (no guessed identifiers),
# and so the demo mirrors how repositories report compounds by neutral name.
DEMO_METABOLITES = [
    "citric acid", "cis-aconitic acid", "isocitric acid", "2-oxoglutaric acid",
    "succinic acid", "fumaric acid", "(S)-malic acid", "oxaloacetic acid",
    "pyruvic acid", "L-lactic acid", "D-glucose", "D-glucose 6-phosphate",
    "D-fructose 6-phosphate", "phosphoenolpyruvic acid", "3-phospho-D-glyceric acid",
    "L-glutamic acid", "L-aspartic acid", "L-alanine", "glycine", "L-serine",
    "ATP", "ADP", "AMP", "NAD(+)", "acetyl-CoA", "succinyl-CoA",
]


@dataclass
class Row:
    name: str
    seed: str | None
    seed_label: str
    seed_charge: float | None
    family_size: int
    exact_rhea: bool
    norm_rhea: bool
    exact_go: int      # GO MF terms via exact seed
    norm_go: int       # GO MF terms via whole family
    matched_forms: list[str]   # which family members are Rhea participants
    example_go: list[str]


def resolve_seed(token: str) -> tuple[str | None, chebi.ChebiTerm | None]:
    if token.upper().startswith("CHEBI:"):
        t = chebi.get_term(token)
        return (token, t)
    t = chebi.search_neutral(token)
    return ((t.curie if t else None), t)


def probe_metabolite(token: str, idx: rhea.RheaIndex) -> Row:
    seed_curie, seed_term = resolve_seed(token)
    if seed_curie is None or seed_term is None:
        return Row(token, None, "(unresolved)", None, 0, False, False, 0, 0, [], [])

    family = chebi.protonation_family(seed_curie)
    exact_rxns = idx.reactions_for(seed_curie)
    exact_go = idx.go_terms_for(seed_curie)

    norm_rxns: set[str] = set()
    norm_go: set[tuple[str, str]] = set()
    matched_forms: list[str] = []
    for cid, term in family.items():
        rxns = idx.reactions_for(cid)
        if rxns:
            matched_forms.append(f"{term.label} ({cid}, q={_fmt_charge(term.charge)})")
        norm_rxns |= rxns
        norm_go |= idx.go_terms_for(cid)

    example_go = [f"{go} {lab}" for go, lab in sorted(norm_go)][:3]
    return Row(
        name=token,
        seed=seed_curie,
        seed_label=seed_term.label,
        seed_charge=seed_term.charge,
        family_size=len(family),
        exact_rhea=bool(exact_rxns),
        norm_rhea=bool(norm_rxns),
        exact_go=len(exact_go),
        norm_go=len(norm_go),
        matched_forms=matched_forms,
        example_go=example_go,
    )


def _fmt_charge(c: float | None) -> str:
    if c is None:
        return "?"
    return str(int(c)) if float(c).is_integer() else str(c)


def run(tokens: list[str]) -> list[Row]:
    print(f"Loading Rhea network + rhea2go ...", file=sys.stderr)
    idx = rhea.RheaIndex()
    print(f"  {len(idx.reaction_to_participants)} reactions, "
          f"{len(idx.participant_to_reactions)} participant ChEBIs, "
          f"{len(idx.reaction_to_go)} rhea2go GO mappings", file=sys.stderr)
    rows: list[Row] = []
    for tok in tokens:
        row = probe_metabolite(tok, idx)
        rows.append(row)
        flag = ""
        if row.seed and not row.exact_rhea and row.norm_rhea:
            flag = "  <- recovered ONLY by protonation normalization"
        print(f"  {tok:28s} seed={row.seed or '-':14s} q={_fmt_charge(row.seed_charge):>3s} "
              f"fam={row.family_size:2d} exact_rhea={row.exact_rhea!s:5s} "
              f"norm_rhea={row.norm_rhea!s:5s} GO {row.exact_go}->{row.norm_go}{flag}",
              file=sys.stderr)
    return rows


def summarize(rows: list[Row]) -> dict[str, int]:
    resolved = [r for r in rows if r.seed]
    return {
        "n": len(rows),
        "resolved": len(resolved),
        "exact_rhea": sum(r.exact_rhea for r in resolved),
        "norm_rhea": sum(r.norm_rhea for r in resolved),
        "exact_go": sum(r.exact_go > 0 for r in resolved),
        "norm_go": sum(r.norm_go > 0 for r in resolved),
        "recovered": sum(r.norm_rhea and not r.exact_rhea for r in resolved),
    }


def write_results(rows: list[Row], s: dict[str, int]) -> None:
    out = Path(__file__).parent / "RESULTS.md"
    lines: list[str] = []
    lines.append("---")
    lines.append('title: "Metabolomics->GO Bridge: Protonation-Normalization Coverage Probe"')
    lines.append("---\n")
    lines.append("# Metabolomics → GO Bridge: protonation-normalization coverage probe\n")
    lines.append("Generated by [`coverage_probe.py`](coverage_probe.py) — all numbers computed")
    lines.append("live from OLS4 (ChEBI), the Rhea REST API, and the GO `rhea2go` mapping.")
    lines.append("Re-run with `uv run python coverage_probe.py --write-results`.\n")
    lines.append("## Why this probe exists\n")
    lines.append("Metabolomics repositories report metabolites as their **neutral** species;")
    lines.append("Rhea writes reaction participants in their **major protonation state at**")
    lines.append("**pH 7.3**. Matching the reported ChEBI id directly against Rhea therefore")
    lines.append("misses the bridge. We expand each metabolite over ChEBI's")
    lines.append("`is_protonated_form_of` / `is_deprotonated_form_of` relations (its")
    lines.append("*protonation family*) and re-check. The EXACT vs NORMALIZED gap is the")
    lines.append("value added by protonation normalization.\n")
    lines.append("## Headline\n")
    lines.append(f"- Metabolites probed: **{s['n']}** (resolved to ChEBI: {s['resolved']})")
    lines.append(f"- In a Rhea reaction — **exact: {s['exact_rhea']}/{s['resolved']}**, "
                 f"**normalized: {s['norm_rhea']}/{s['resolved']}**")
    lines.append(f"- Reaching a GO MF term (rhea2go) — **exact: {s['exact_go']}/{s['resolved']}**, "
                 f"**normalized: {s['norm_go']}/{s['resolved']}**")
    lines.append(f"- **Recovered only by protonation normalization: {s['recovered']} "
                 f"metabolite(s)**\n")
    lines.append("## Per-metabolite\n")
    lines.append("| Metabolite (reported) | Seed ChEBI | q | Family | Exact→Rhea | Norm→Rhea | GO MF (exact→norm) | Rhea-matched form |")
    lines.append("|---|---|---:|---:|:--:|:--:|:--:|---|")
    for r in rows:
        matched = r.matched_forms[0] if r.matched_forms else "—"
        lines.append(
            f"| {r.name} | {r.seed or '—'} | {_fmt_charge(r.seed_charge)} | {r.family_size} | "
            f"{'✓' if r.exact_rhea else '·'} | {'✓' if r.norm_rhea else '·'} | "
            f"{r.exact_go}→{r.norm_go} | {matched} |"
        )
    lines.append("\n## Example GO molecular functions reached\n")
    for r in rows:
        if r.example_go and not r.exact_rhea and r.norm_rhea:
            lines.append(f"- **{r.name}** ({r.seed}) → " + "; ".join(r.example_go))
    residual = [r for r in rows if r.seed and not r.norm_rhea]
    if residual:
        lines.append("\n## Residual misses (a *different* mismatch class)\n")
        lines.append("These resolved to ChEBI but matched no Rhea reaction even after")
        lines.append("protonation normalization. They expose a second ID-mismatch class that")
        lines.append("protonation expansion does **not** fix — **stereochemistry / anomer** and")
        lines.append("**generic-vs-structurally-specific** ChEBI mismatch (e.g. Rhea uses a")
        lines.append("stereospecific or anomer-specific form, or a structurally-defined child of")
        lines.append("a generic 2D parent). Fixing these needs tautomer/enantiomer/`has parent")
        lines.append("hydride` traversal or structure-skeleton (InChIKey) matching — a follow-up.\n")
        for r in residual:
            lines.append(f"- **{r.name}** ({r.seed}, family size {r.family_size})")
    lines.append("\n## Method / reproducibility\n")
    lines.append("- ChEBI access + protonation traversal: [`chebi.py`](chebi.py) (OLS4).")
    lines.append("- Rhea network + rhea2go: [`rhea.py`](rhea.py) (Rhea REST, GO external2go).")
    lines.append("- Caches under `.cache/` (gitignored); delete to force a fresh pull.")
    lines.append("- This is a **coverage** probe (does the bridge connect?), not yet a")
    lines.append("  statistical enrichment; GO-BP lift + ORA are the next step (see the")
    lines.append("  [project page](../../METABOLOMICS.md)).")
    out.write_text("\n".join(lines) + "\n")
    print(f"\nWrote {out}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--names-file", type=Path, help="one metabolite name per line")
    ap.add_argument("--chebi-file", type=Path, help="one CHEBI:xxxxx id per line")
    ap.add_argument("--write-results", action="store_true", help="write RESULTS.md")
    args = ap.parse_args()

    if args.chebi_file:
        tokens = [l.strip() for l in args.chebi_file.read_text().splitlines() if l.strip()]
    elif args.names_file:
        tokens = [l.strip() for l in args.names_file.read_text().splitlines() if l.strip()]
    else:
        tokens = DEMO_METABOLITES

    rows = run(tokens)
    s = summarize(rows)
    print("\n== SUMMARY ==", file=sys.stderr)
    print(f"  metabolites probed : {s['n']} (resolved {s['resolved']})", file=sys.stderr)
    print(f"  in Rhea  exact={s['exact_rhea']}  normalized={s['norm_rhea']}", file=sys.stderr)
    print(f"  GO MF    exact={s['exact_go']}  normalized={s['norm_go']}", file=sys.stderr)
    print(f"  recovered ONLY by protonation normalization: {s['recovered']}", file=sys.stderr)

    if args.write_results:
        write_results(rows, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
