"""Rank human genes where IBA is *too conservative* for core molecular function.

For each human gene review this asks: if IBA were the only evidence used, which
``core_functions`` **molecular functions** would be lost? A core-function MF is
the curator's distilled, highly-weighted judgement of what the gene *does*, so a
core MF that no IBA annotation grounds (even via is_a/part_of closure) is a place
where phylogenetic propagation under-calls the biology.

Low-information ``binding`` molecular functions (descendants of GO:0005488,
including ``protein binding``) are excluded -- they say little about mechanism.

The LOST determination is delegated to the shared
:class:`SubtractionReporter` (keep-only IBA + ``exclude_branches={GO:0005488}``)
so it stays consistent with the CLI; this script adds the evidence-code
enrichment (which the flat report does not carry) and the ranking.

Run::

    uv run python projects/IBA_REVIEW/iba_too_conservative_core_mf.py

Writes ``reports/iba-too-conservative-core-mf.md`` and prints the top genes.
"""

from __future__ import annotations

import glob
from collections import defaultdict
from pathlib import Path

import yaml

from ai_gene_review.analysis.subtraction_report import (
    SubtractionFilter,
    SubtractionReporter,
    effective_term_ids,
    make_go_ancestor_fn,
)

BINDING_ROOT = "GO:0005488"
CORE_MF_SLOTS = ("molecular_function", "contributes_to_molecular_function")
# Experimental / author-statement evidence codes (strongest non-IBA support).
EXPERIMENTAL = {
    "EXP", "IDA", "IMP", "IPI", "IGI", "IEP",
    "HDA", "HMP", "HGI", "HEP", "HTP",
    "TAS", "IC",
}


def grounding_evidence(
    review: dict, core_term: str, ancestors
) -> list[tuple[str, str]]:
    """Return (evidence_type, reference_id) for non-IBA annotations that ground
    ``core_term`` (the annotation's effective term is core_term or a descendant).
    """
    out: list[tuple[str, str]] = []
    for ann in review.get("existing_annotations") or []:
        if ann.get("evidence_type") == "IBA" or ann.get("negated"):
            continue
        for eff in effective_term_ids(ann):
            if core_term in ancestors(eff):
                out.append(
                    (ann.get("evidence_type") or "?", ann.get("original_reference_id") or "")
                )
                break
    return out


def main() -> None:
    files = sorted(glob.glob("genes/human/*/*-ai-review.yaml"))
    ancestors = make_go_ancestor_fn()
    reporter = SubtractionReporter(
        ancestors=ancestors, exclude_branches=frozenset({BINDING_ROOT})
    )
    filt = SubtractionFilter.create(
        evidence_codes=["IBA"], reference_ids=["GO_REF:0000033"], complement=True
    )

    # gene -> list of (term_id, label, has_experimental, evidence_codes)
    per_gene: dict[str, list[tuple[str, str, bool, list[str]]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()

    for path in files:
        with open(path) as fh:
            review = yaml.safe_load(fh)
        if not isinstance(review, dict):
            continue
        result = reporter.analyze_review(review, filt)
        gene = result.gene_symbol or result.protein_id or Path(path).stem
        for cov in result.core_function_coverage:
            if cov.slot not in CORE_MF_SLOTS or cov.status != "LOST":
                continue
            key = (gene, cov.term_id)
            if key in seen:
                continue
            seen.add(key)
            evs = grounding_evidence(review, cov.term_id, ancestors)
            ev_codes = sorted({e for e, _ in evs})
            has_exp = any(e in EXPERIMENTAL for e in ev_codes)
            per_gene[gene].append(
                (cov.term_id, cov.term_label or "", has_exp, ev_codes)
            )

    # Rank: genes by (# experimentally-grounded core MF lost, # core MF lost).
    ranked = sorted(
        per_gene.items(),
        key=lambda kv: (
            sum(1 for t in kv[1] if t[2]),
            len(kv[1]),
            kv[0],
        ),
        reverse=True,
    )

    n_terms = sum(len(v) for v in per_gene.values())
    n_exp_terms = sum(1 for v in per_gene.values() for t in v if t[2])

    lines: list[str] = []
    lines.append("# IBA is too conservative: core molecular functions IBA alone would miss")
    lines.append("")
    lines.append(
        "Non-`binding` (GO:0005488 excluded) **core_functions molecular functions** "
        "that are grounded only by non-IBA evidence — i.e. if IBA were the sole "
        "evidence source, these curated core activities would be lost. Closure "
        "(is_a + part_of) is applied, so an IBA call to a more general parent does "
        "**not** count as grounding a specific activity."
    )
    lines.append("")
    lines.append(
        f"- Core MF terms IBA alone would miss: **{n_terms}** across "
        f"**{len(per_gene)}** genes"
    )
    lines.append(
        f"- Of those, grounded by experimental/author evidence (IDA/IMP/IPI/EXP/TAS/IC...): "
        f"**{n_exp_terms}**"
    )
    lines.append("")
    lines.append("## Genes ranked by curated core activities IBA misses")
    lines.append("")
    lines.append("| Gene | # core MF (★ experimental) | Example activities IBA misses |")
    lines.append("|------|----------------------------|-------------------------------|")
    for gene, terms in ranked[:60]:
        n_exp = sum(1 for t in terms if t[2])
        # show the experimentally-grounded ones first
        terms_sorted = sorted(terms, key=lambda t: (not t[2], t[1]))
        examples = "; ".join(
            f"{('★' if t[2] else '')}{t[1]}" for t in terms_sorted[:3]
        )
        lines.append(f"| {gene} | {len(terms)} ({n_exp}★) | {examples} |")
    lines.append("")
    lines.append("## Detail (top 30 genes)")
    lines.append("")
    for gene, terms in ranked[:30]:
        lines.append(f"### {gene}")
        for tid, label, has_exp, evs in sorted(terms, key=lambda t: (not t[2], t[1])):
            star = "★ " if has_exp else ""
            lines.append(f"- {star}{tid} {label} — evidence: {', '.join(evs) or 'non-IBA'}")
        lines.append("")

    out = Path("reports/iba-too-conservative-core-mf.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"Wrote {out}")
    print(f"{n_terms} core MF terms ({n_exp_terms} experimental) across {len(per_gene)} genes")
    print("\nTop 15 genes:")
    for gene, terms in ranked[:15]:
        n_exp = sum(1 for t in terms if t[2])
        print(f"  {gene:12} {len(terms)} core MF ({n_exp} experimental)")


if __name__ == "__main__":
    main()
