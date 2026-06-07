#!/usr/bin/env python3
"""Stage OpenScientist (or any deep-research) hypothesis prompts from the
ASSAY_TO_FUNCTION flagged-candidate worklist.

This is the "human gate" generator the project's workflow calls for: it turns
selected rows of ``reports/flagged_candidates.tsv`` into committed, frontmatter-
free ``prompt.md`` files under ``genes/<org>/<gene>/<gene>-hypotheses/<slug>/``
and prints the exact submit command for each -- but it NEVER submits a job.
A human reviews the staged prompts and runs the printed command(s) to spend a
(paid, ~15-30 min) deep-research job only on candidates worth a cited literature
adjudication.

It reuses the canonical record/template machinery in
``scripts/gene_hypothesis_deep_research.py`` so staged prompts are identical to
what that tool would submit, then specializes the seed hypothesis to the
readout-driven "core function vs downstream/context-dependent consequence?"
question that this project is about.

Usage (stage, do not submit):
    uv run python projects/ASSAY_TO_FUNCTION/stage_hypotheses.py \
        --discriminator indirect_ligand --max 5
    uv run python projects/ASSAY_TO_FUNCTION/stage_hypotheses.py \
        --gene STAT3 --go-id GO:0030335

Then a human submits a staged prompt:
    uv run deep-research-client research \
        --input-file <dir>/prompt.md --provider openscientist \
        --output <dir>/openscientist.md \
        --separate-citations <dir>/openscientist.md.citations.md
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "templates" / "gene_hypothesis_deep_research.md"
DEFAULT_FLAGS = Path("projects/ASSAY_TO_FUNCTION/reports/flagged_candidates.tsv")


def _load_generator_module() -> Any:
    """Import scripts/gene_hypothesis_deep_research.py as a module."""
    path = ROOT / "scripts" / "gene_hypothesis_deep_research.py"
    spec = importlib.util.spec_from_file_location("aigr_hypothesis_gen", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod  # needed for dataclass type resolution
    spec.loader.exec_module(mod)
    return mod


GEN = _load_generator_module()


def render_prompt(template_text: str, variables: dict[str, str]) -> str:
    """Brace-safe token substitution: replace each literal ``{key}`` token.

    Plain ``str.format`` would choke on the literal braces inside the
    ``source_context_yaml`` fenced block, so substitute key by key instead.
    """
    out = template_text
    for key, value in variables.items():
        out = out.replace("{" + key + "}", value)
    return out


def seed_hypothesis(gene: str, go_label: str, go_id: str, aspect: str,
                    readout: str, reason: str, action: str) -> str:
    return (
        f"The existing {gene} GO annotation to {go_label} ({go_id}) is currently "
        f"action {action} and was flagged by the ASSAY_TO_FUNCTION readout class "
        f"{readout}. Decide whether this {aspect} term is a CORE function of "
        f"{gene} (a primary process the gene product evolved to drive) versus a "
        f"DOWNSTREAM, secondary, or context-dependent consequence of its core "
        f"molecular activity that is better captured as non-core. Distinguish a "
        f"'real, documented effect' (which may not be in question) from a 'core "
        f"function'. Flag rationale: {reason}"
    )


def select_flag_rows(flags_path: Path, *, tier: str | None, discriminator: str | None,
                     readout_class: str | None, gene: str | None, go_id: str | None,
                     action: str | None, organism: str | None,
                     max_rows: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with flags_path.open(newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if tier and r.get("tier") != tier:
                continue
            if discriminator and r.get("discriminator") != discriminator:
                continue
            if readout_class and r.get("readout_class") != readout_class:
                continue
            if gene and r.get("gene") != gene:
                continue
            if go_id and r.get("go_id") != go_id:
                continue
            if action and (r.get("action") or "").upper() != action.upper():
                continue
            if organism and r.get("organism") != organism:
                continue
            rows.append(r)
    # Dedupe per (organism, gene, go_id) -- the flagger already does this, but a
    # gene may legitimately have the same term flagged via two readout classes.
    seen: set[tuple[str, str, str]] = set()
    deduped: list[dict[str, str]] = []
    for r in rows:
        key = (r["organism"], r["gene"], r["go_id"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    return deduped[:max_rows] if max_rows else deduped


def record_for_flag(flag: dict[str, str]) -> Any:
    """Build the canonical GeneHypothesisRecord for a flagged annotation, then
    specialize its seed hypothesis to the readout-driven core-vs-downstream
    question."""
    organism, gene, go_id = flag["organism"], flag["gene"], flag["go_id"]
    records = GEN.candidate_records(Path("genes"), organism, gene)
    matches = [
        rec for rec in records
        if rec.source_selector.startswith("existing_annotations[")
        and isinstance(rec.source_context.get("term"), dict)
        and str(rec.source_context["term"].get("id") or "") == go_id
    ]
    if not matches:
        raise ValueError(
            f"no existing_annotations record for {organism}/{gene} {go_id}; "
            "is the gene review present and the term still annotated?")
    base = matches[0]
    new_text = seed_hypothesis(
        gene=base.gene_symbol, go_label=flag.get("go_label", go_id), go_id=go_id,
        aspect=flag.get("aspect", "BP"), readout=flag.get("readout_class", ""),
        reason=flag.get("reason", ""), action=flag.get("action", "UNREVIEWED"))
    # rebuild with the specialized hypothesis_text and a readout-tagged slug
    slug = GEN.slugify(f"readout-{GEN.term_slug(base.source_context.get('term'))}")
    return GEN.make_record(
        organism=base.organism, gene=base.gene, gene_symbol=base.gene_symbol,
        taxon_id=base.taxon_id, taxon_label=base.taxon_label,
        focus_type="existing_go_annotation_decision", slug=slug,
        hypothesis_text=new_text, term_context=base.term_context,
        reference_ids=GEN.reference_ids_from_context(base.reference_context),
        source_file=base.source_file, source_selector=base.source_selector,
        source_context=base.source_context)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--flags", type=Path, default=DEFAULT_FLAGS)
    ap.add_argument("--tier")
    ap.add_argument("--discriminator", help="e.g. indirect_ligand")
    ap.add_argument("--readout-class")
    ap.add_argument("--gene")
    ap.add_argument("--go-id")
    ap.add_argument("--action", help="filter by standing action, e.g. UNDECIDED")
    ap.add_argument("--organism")
    ap.add_argument("--provider", default="openscientist")
    ap.add_argument("--max", type=int, default=0, help="cap staged prompts (0=all)")
    ap.add_argument("--overwrite", action="store_true",
                    help="overwrite an existing prompt.md")
    args = ap.parse_args()

    if not args.flags.exists():
        print(f"error: {args.flags} not found; run flag_candidates.py first",
              file=sys.stderr)
        return 2
    template_text = TEMPLATE.read_text(encoding="utf-8")

    flags = select_flag_rows(
        args.flags, tier=args.tier, discriminator=args.discriminator,
        readout_class=args.readout_class, gene=args.gene, go_id=args.go_id,
        action=args.action, organism=args.organism, max_rows=args.max)
    if not flags:
        print("No flagged rows matched the filters.", file=sys.stderr)
        return 1

    print(f"# Staging {len(flags)} hypothesis prompt(s) "
          f"(human gate: NOTHING is submitted)\n")
    staged = 0
    for flag in flags:
        try:
            record = record_for_flag(flag)
        except ValueError as err:
            print(f"  SKIP {flag['organism']}/{flag['gene']} {flag['go_id']}: {err}")
            continue
        out_dir = GEN.output_dir_for(record, Path("genes"), record.organism,
                                     record.gene)
        prompt_path = out_dir / "prompt.md"
        if prompt_path.exists() and not args.overwrite:
            print(f"  EXISTS {prompt_path} (use --overwrite)")
        else:
            out_dir.mkdir(parents=True, exist_ok=True)
            prompt_path.write_text(
                render_prompt(template_text, GEN.template_vars(record)),
                encoding="utf-8")
            staged += 1
            print(f"  STAGED {prompt_path}")
        out_md = out_dir / f"{GEN.normalize_provider(args.provider)}.md"
        print("    submit (human runs this to spend a job):")
        print(f"      uv run deep-research-client research \\")
        print(f"        --input-file {prompt_path} --provider {args.provider} \\")
        print(f"        --output {out_md} \\")
        print(f"        --separate-citations {out_md}.citations.md\n")

    print(f"# Staged {staged} new prompt(s). Review them, then submit the ones "
          f"worth a paid adjudication. Keep the annotation UNDECIDED and post the "
          f"verdict to the expert issue; verify cited PMIDs before folding into YAML.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
