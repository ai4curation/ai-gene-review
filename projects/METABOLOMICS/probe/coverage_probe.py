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
    norm_rhea: bool      # protonation-normalized
    struct_rhea: bool    # structure (skeleton) normalized
    exact_go: int        # GO MF terms via exact seed
    norm_go: int         # GO MF terms via protonation family
    struct_go: int       # GO MF terms via skeleton family
    matched_forms: list[str]    # protonation-family members that are Rhea participants
    struct_forms: list[str]     # extra skeleton-family members that are Rhea participants
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
        return Row(token, None, "(unresolved)", None, 0, False, False, False,
                   0, 0, 0, [], [], [])

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

    # Structure (skeleton) tier: only computed when protonation did not already
    # connect, since it is the more permissive (stereo/charge-blind) fallback.
    struct_rxns: set[str] = set(norm_rxns)
    struct_go: set[tuple[str, str]] = set(norm_go)
    struct_forms: list[str] = []
    if not norm_rxns:
        sfam = chebi.structural_family(seed_curie)
        for cid, term in sfam.items():
            if cid in family:
                continue
            rxns = idx.reactions_for(cid)
            if rxns:
                struct_forms.append((term.label, f"{term.label} ({cid}, q={_fmt_charge(term.charge)})"))
            struct_rxns |= rxns
            struct_go |= idx.go_terms_for(cid)
        # Skeleton matching is stereo-blind; for the representative form prefer a
        # non-D-prefixed (typically L / biological) label over its enantiomer.
        struct_forms = [s for _, s in sorted(struct_forms, key=lambda x: (x[0].startswith("D-"), x[0]))]

    example_go = [f"{go} {lab}" for go, lab in sorted(struct_go)][:3]
    return Row(
        name=token,
        seed=seed_curie,
        seed_label=seed_term.label,
        seed_charge=seed_term.charge,
        family_size=len(family),
        exact_rhea=bool(exact_rxns),
        norm_rhea=bool(norm_rxns),
        struct_rhea=bool(struct_rxns),
        exact_go=len(exact_go),
        norm_go=len(norm_go),
        struct_go=len(struct_go),
        matched_forms=matched_forms,
        struct_forms=struct_forms,
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
            flag = "  <- recovered by PROTONATION normalization"
        elif row.seed and not row.norm_rhea and row.struct_rhea:
            flag = "  <- recovered by STRUCTURE (skeleton) normalization"
        print(f"  {tok:26s} seed={row.seed or '-':14s} q={_fmt_charge(row.seed_charge):>3s} "
              f"exact={row.exact_rhea!s:5s} proton={row.norm_rhea!s:5s} "
              f"struct={row.struct_rhea!s:5s} GO {row.exact_go}->{row.norm_go}->{row.struct_go}{flag}",
              file=sys.stderr)
    return rows


def summarize(rows: list[Row]) -> dict[str, int]:
    resolved = [r for r in rows if r.seed]
    return {
        "n": len(rows),
        "resolved": len(resolved),
        "exact_rhea": sum(r.exact_rhea for r in resolved),
        "norm_rhea": sum(r.norm_rhea for r in resolved),
        "struct_rhea": sum(r.struct_rhea for r in resolved),
        "exact_go": sum(r.exact_go > 0 for r in resolved),
        "norm_go": sum(r.norm_go > 0 for r in resolved),
        "struct_go": sum(r.struct_go > 0 for r in resolved),
        "recovered_proton": sum(r.norm_rhea and not r.exact_rhea for r in resolved),
        "recovered_struct": sum(r.struct_rhea and not r.norm_rhea for r in resolved),
    }


def write_results(rows: list[Row], s: dict[str, int], out: Path | None = None,
                  title: str | None = None, source: str | None = None,
                  rel_prefix: str = "") -> None:
    out = out or (Path(__file__).parent / "RESULTS.md")
    title = title or "Metabolomics → GO Bridge: protonation-normalization coverage probe"
    lines: list[str] = []
    lines.append("---")
    lines.append(f'title: "{title}"')
    lines.append("---\n")
    lines.append(f"# {title}\n")
    if source:
        lines.append(f"**Input:** {source}\n")
    lines.append(f"Generated by [`coverage_probe.py`]({rel_prefix}coverage_probe.py) — all numbers")
    lines.append("computed live from OLS4 (ChEBI), the Rhea REST API, and the GO `rhea2go` mapping.\n")
    lines.append("## Why this probe exists\n")
    lines.append("Reported metabolite ChEBI ids rarely match Rhea participants directly,")
    lines.append("for two reasons we test as successive normalization tiers:\n")
    lines.append("1. **Protonation** — Rhea writes participants in their major protonation")
    lines.append("   state at pH 7.3 (`citrate(3-)`, `ATP(4-)`); repositories report neutral")
    lines.append("   forms. We expand over ChEBI `is_protonated_form_of` /")
    lines.append("   `is_deprotonated_form_of` (the *protonation family*).")
    lines.append("2. **Structure / skeleton** — a study reports a generic, non-stereospecific")
    lines.append("   compound (`isoleucine`) while Rhea uses the stereospecific zwitterion")
    lines.append("   (`L-isoleucine zwitterion`). We expand over the broader structural")
    lines.append("   relations (+ tautomer/enantiomer + generic→specific `children`), bounded")
    lines.append("   to the seed's **InChIKey skeleton**. This tier is stereo/charge-blind, so")
    lines.append("   it is reported separately as the more permissive fallback.\n")
    lines.append("## Headline\n")
    lines.append(f"- Metabolites probed: **{s['n']}** (resolved to ChEBI: {s['resolved']})")
    lines.append(f"- In a Rhea reaction — **exact: {s['exact_rhea']}/{s['resolved']}** → "
                 f"**+protonation: {s['norm_rhea']}/{s['resolved']}** → "
                 f"**+structure: {s['struct_rhea']}/{s['resolved']}**")
    lines.append(f"- Reaching a GO MF term (rhea2go) — **exact: {s['exact_go']}** → "
                 f"**+protonation: {s['norm_go']}** → **+structure: {s['struct_go']}** "
                 f"(of {s['resolved']})")
    lines.append(f"- Recovered by **protonation**: {s['recovered_proton']}; additionally by "
                 f"**structure/skeleton**: {s['recovered_struct']}\n")
    def dname(r: Row) -> str:
        # Prefer the verified ChEBI label when the input was a bare id.
        if r.name.upper().startswith("CHEBI:") and r.seed_label and r.seed_label != "(unresolved)":
            return r.seed_label
        return r.name

    lines.append("## Per-metabolite\n")
    lines.append("Tier reached: `exact` < `proton` (protonation) < `struct` (skeleton) < `—` (miss).\n")
    lines.append("| Metabolite | Seed ChEBI | q | Tier | GO MF (exact→proton→struct) | Rhea-matched form |")
    lines.append("|---|---|---:|:--:|:--:|---|")
    for r in rows:
        if r.exact_rhea:
            tier = "exact"
        elif r.norm_rhea:
            tier = "proton"
        elif r.struct_rhea:
            tier = "struct"
        else:
            tier = "—"
        matched = (r.matched_forms or r.struct_forms or ["—"])[0]
        lines.append(
            f"| {dname(r)} | {r.seed or '—'} | {_fmt_charge(r.seed_charge)} | {tier} | "
            f"{r.exact_go}→{r.norm_go}→{r.struct_go} | {matched} |"
        )
    lines.append("\n## Recovered by structure (skeleton) normalization\n")
    struct_only = [r for r in rows if r.seed and r.struct_rhea and not r.norm_rhea]
    if struct_only:
        lines.append("Generic / stereochemistry mismatches the protonation tier could not fix,")
        lines.append("recovered by InChIKey-skeleton expansion:\n")
        for r in struct_only:
            form = r.struct_forms[0] if r.struct_forms else "—"
            lines.append(f"- **{dname(r)}** ({r.seed}) → {form}")
    else:
        lines.append("_(none in this set)_")
    lines.append("\n## Example GO molecular functions reached\n")
    for r in rows:
        if r.example_go and not r.exact_rhea and (r.norm_rhea or r.struct_rhea):
            lines.append(f"- **{dname(r)}** ({r.seed}) → " + "; ".join(r.example_go))
    residual = [r for r in rows if r.seed and not r.struct_rhea]
    if residual:
        lines.append("\n## Residual misses (after both normalization tiers)\n")
        lines.append("Resolved to ChEBI but matched no Rhea reaction even after protonation and")
        lines.append("skeleton normalization — typically derivatives Rhea represents only in a")
        lines.append("conjugated/acylated form, or compounds genuinely absent from Rhea.\n")
        for r in residual:
            lines.append(f"- **{dname(r)}** ({r.seed}, family size {r.family_size})")
    lines.append("\n## Method / reproducibility\n")
    lines.append(f"- ChEBI access + protonation traversal: [`chebi.py`]({rel_prefix}chebi.py) (OLS4).")
    lines.append(f"- Rhea network + rhea2go: [`rhea.py`]({rel_prefix}rhea.py) (Rhea REST, GO external2go).")
    lines.append("- Caches under `.cache/` (gitignored); delete to force a fresh pull.")
    lines.append("- This is a **coverage** probe (does the bridge connect?), not yet a")
    lines.append(f"  statistical enrichment; GO-BP lift + ORA are the next step (see the")
    lines.append(f"  [project page]({rel_prefix}../../METABOLOMICS.md)).")
    out.write_text("\n".join(lines) + "\n")
    print(f"\nWrote {out}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--names-file", type=Path, help="one metabolite name per line")
    ap.add_argument("--chebi-file", type=Path, help="one CHEBI:xxxxx id per line (# comments ok)")
    ap.add_argument("--write-results", action="store_true", help="write RESULTS.md")
    ap.add_argument("--out", type=Path, help="results path (default RESULTS.md); implies --write-results")
    ap.add_argument("--title", help="title for the generated results page")
    ap.add_argument("--source", help="provenance note for the results page (e.g. study accession)")
    args = ap.parse_args()

    def _read_tokens(path: Path) -> list[str]:
        # Skip blank lines and '#' comments; take the first whitespace-delimited
        # field so "CHEBI:30769  # citrate" yields "CHEBI:30769".
        toks: list[str] = []
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            toks.append(line.split()[0].split("\t")[0])
        return toks

    if args.chebi_file:
        tokens = _read_tokens(args.chebi_file)
    elif args.names_file:
        tokens = _read_tokens(args.names_file)
    else:
        tokens = DEMO_METABOLITES

    rows = run(tokens)
    s = summarize(rows)
    print("\n== SUMMARY ==", file=sys.stderr)
    print(f"  metabolites probed : {s['n']} (resolved {s['resolved']})", file=sys.stderr)
    print(f"  in Rhea  exact={s['exact_rhea']}  proton={s['norm_rhea']}  struct={s['struct_rhea']}",
          file=sys.stderr)
    print(f"  GO MF    exact={s['exact_go']}  proton={s['norm_go']}  struct={s['struct_go']}",
          file=sys.stderr)
    print(f"  recovered by protonation: {s['recovered_proton']}  "
          f"+ by structure(skeleton): {s['recovered_struct']}", file=sys.stderr)

    if args.write_results or args.out:
        rel_prefix = "../" if args.out and args.out.parent.name == "studies" else ""
        write_results(rows, s, out=args.out, title=args.title, source=args.source,
                      rel_prefix=rel_prefix)
    return 0


if __name__ == "__main__":
    sys.exit(main())
