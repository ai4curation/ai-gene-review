#!/usr/bin/env python3
"""Emit an Affinage record as an AIGR deep-research source file (HUMAN ONLY).

Affinage (affinage.wi.mit.edu) precomputes a citation-anchored mechanistic
narrative for every human protein-coding gene. The AIGR review workflow already
picks up any ``genes/<sp>/<GENE>/<GENE>-deep-research-*.md`` file, so "wiring in"
Affinage needs no pipeline change: this tool fetches the record and writes
``<GENE>-deep-research-affinage.md`` in the same shape as the other providers.

This is the ONLY Affinage integration the evaluation endorses — a *free precomputed
first pass for the human backlog* (see ../results/narrative-vs-go.md).

DESIGN PRINCIPLE — the file is a faithful, unedited rendering of the provider record,
nothing more. A ``<GENE>-deep-research-*.md`` file reproduces what the external provider
returned (like a falcon/perplexity report): the mechanistic narrative, Affinage's own
GO/Reactome ``mechanism_profile`` grounding, the dated discoveries, and the citations.
(A few emitted fields are mechanical derivations of that content rather than provider
fields — ``citation_count`` and the ``## Citations`` list are the union of the discovery
PMIDs and the ``PMID:NNN`` tokens in the narrative, and ``n_discoveries`` is a count —
but nothing is edited, summarised or adjudicated.) It carries **no AIGR interpretation**
— no CAUTION banners, no "these GO terms are coarse, do not import them" advice, no
adjudication of trust. That curatorial judgment is the reviewer's, and it belongs in the
gene review's ``references[].reference_review`` (relevance / correctness / review_notes)
and ``findings`` — NOT in this source file. Mixing the two would launder AIGR's own
opinion into something that looks like the provider said it.

The tool still HELPS the curator form that judgment: it is HUMAN ONLY (Affinage
covers only human, so any other species is refused), and it runs two cheap trust
checks — Affinage's own ``evaluation.pairwise`` self-signal (win/tie/loss), and an
accession/organism cross-check against the local ``<GENE>-uniprot.txt`` for the
ADA-style symbol-collision failure. Those gate results are printed to **stderr** as a
reminder to record them in the review's ``reference_review``; they are deliberately
kept OUT of the written file so the file stays a faithful provider record. Only
factual provenance (source URL, run date, accession, Affinage's own self-eval numbers)
is recorded in the frontmatter.

Because the written file no longer carries an in-file warning, the safety check lives in
the TOOL instead: the two *wrong-protein* gates (accession mismatch, non-human organism
token) are **blocking** — writing such a record into the live ``genes/`` tree is refused
with a non-zero exit unless ``--force`` is passed — since a file in a gene folder is
ingested by a later review of that gene. The soft ``pairwise`` signal never blocks; it is
already in the frontmatter as ``self_evaluation_pairwise``.

Usage:
    python affinage_deep_research.py human GPX4                 # print to stdout
    python affinage_deep_research.py human GPX4 --write         # -> genes/human/GPX4/GPX4-deep-research-affinage.md
    python affinage_deep_research.py human ADA --write          # blocking gate -> refuses to write (use --force)
    python affinage_deep_research.py human ADA                  # stdout is never gated; warning goes to stderr
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
API = "https://affinage.wi.mit.edu/api/gene/{sym}"

# Cheap heuristic tokens: if the narrative opens by naming one of these while the
# record is keyed to a human accession, it is probably a symbol collision (cf. ADA,
# whose narrative opens on "The E. coli Ada protein…").
NONHUMAN_TOKENS = [
    "e. coli", "escherichia", "s. cerevisiae", "saccharomyces", "yeast",
    "s. pombe", "schizosaccharomyces", "drosophila", "c. elegans", "caenorhabditis",
    "arabidopsis", "zebrafish", "danio", "bacterial", "in bacteria", "in plants",
    "mycobacterium", "salmonella", "bacillus",
]


def fetch(sym: str) -> dict:
    raw = subprocess.run(
        ["curl", "-sS", "--max-time", "60", API.format(sym=sym)],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(raw)


def local_accession(species: str, gene: str) -> str | None:
    """Best-effort read of the reviewed UniProt accession from the gene folder."""
    up = REPO / "genes" / species / gene / f"{gene}-uniprot.txt"
    if not up.exists():
        return None
    m = re.search(r"^AC\s+(\S+?);", up.read_text(), re.MULTILINE)
    return m.group(1) if m else None


def _in_gene_tree(dest: Path) -> bool:
    """True if ``dest`` lands inside the live ``genes/`` tree (where a later review of that
    gene would ingest it), as opposed to a scratch/results path."""
    try:
        dest.resolve().relative_to(REPO / "genes")
    except ValueError:
        return False
    return True


def run_gates(gene: str, data: dict, expected_acc: str | None) -> list[tuple[bool, str]]:
    """Compute trust-gate warnings for the OPERATOR (printed to stderr, never written
    into the file). Returns ``(blocking, message)`` pairs (empty = all clear).

    ``blocking`` marks the two *wrong-protein* gates (accession mismatch, non-human
    organism token): a record that describes a different protein must not land in a gene
    folder, where a later review would ingest it. The ``pairwise`` self-signal is a soft
    signal already present in the frontmatter, so it never blocks.

    These are AIGR's judgment of the record, not Affinage's output — so they are
    surfaced to the reviewer as a prompt to record the assessment in the gene review's
    references[].reference_review, and are deliberately kept out of the provider file.
    """
    cautions: list[tuple[bool, str]] = []
    up = (data.get("prefetch_data") or {}).get("uniprot") or {}
    aff_acc = up.get("accession")
    ev = data.get("evaluation") or {}
    pairwise = ev.get("pairwise")
    narr = (data.get("narrative") or {}).get("mechanistic_narrative", "") or ""
    model = (data.get("timeline") or {}).get("current_model", "") or ""

    if pairwise and pairwise != "win":
        cautions.append((False,
            f"Affinage's own head-to-head self-evaluation scored this record "
            f"`pairwise = {pairwise}` (not `win`) vs the curated UniProt reference — "
            f"treat the narrative with extra scepticism."))
    if expected_acc and aff_acc and expected_acc != aff_acc:
        cautions.append((True,
            f"Accession mismatch: local review uses `{expected_acc}` but the Affinage "
            f"record's prefetch UniProt accession is `{aff_acc}`."))
    opening = (model[:220] + " " + narr[:220]).lower()
    hit = next((t for t in NONHUMAN_TOKENS if t in opening), None)
    if hit:
        cautions.append((True,
            f"Possible symbol collision: the narrative's opening names a non-human "
            f"context (\"{hit}\") despite a human record — verify the narrative "
            f"describes human {gene} and not a same-symbol protein (cf. the ADA case)."))
    return cautions


def render(species: str, gene: str, data: dict) -> str:
    """Render the Affinage record as a deep-research source file.

    This is a faithful, unedited rendering of what Affinage returned — provider metadata,
    the mechanistic narrative, Affinage's own GO/Reactome grounding, dated findings,
    and citations. It does no trust work and carries no AIGR interpretation by design
    (see module docstring): trust-gate judgment is surfaced separately (stderr) and
    recorded by the reviewer in the gene review's ``references[].reference_review``.
    """
    tl = data.get("timeline") or {}
    nar = data.get("narrative") or {}
    up = (data.get("prefetch_data") or {}).get("uniprot") or {}
    ev = data.get("evaluation") or {}
    mp = nar.get("mechanism_profile") or {}
    disc = tl.get("discoveries") or []

    all_pmids = sorted({p for d in disc for p in (d.get("pmids") or [])}
                       | set(re.findall(r"PMID:(\d+)", nar.get("mechanistic_narrative", "") or "")))

    L: list[str] = []
    L.append("---")
    L.append("provider: affinage")
    L.append("model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)")
    L.append(f"source_url: {API.format(sym=gene)}")
    L.append(f"affinage_run_date: {data.get('run_date', '')}")
    L.append(f"uniprot_accession: {up.get('accession', '')}")
    L.append(f"self_evaluation_pairwise: {ev.get('pairwise', '')}")
    L.append(f"faith_pct: {ev.get('faith_pct', '')}")
    L.append(f"n_discoveries: {len(disc)}")
    L.append(f"citation_count: {len(all_pmids)}")
    L.append("note: >-")
    L.append("  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),")
    L.append("  reproduced as-is as an external deep-research source (like a")
    L.append("  falcon/perplexity report). It is Affinage-authored, LLM-generated, and")
    L.append("  human-only. Curatorial assessment of this record — relevance, correctness,")
    L.append("  trust gates, whether to import its GO grounding — is the reviewer's and")
    L.append("  belongs in the gene review's references[].reference_review, not in this file.")
    L.append("---")
    L.append("")
    L.append(f"# Affinage mechanistic annotation for {gene} ({species})")
    L.append("")

    L.append("## Current model (mechanistic narrative)")
    L.append("")
    L.append(nar.get("mechanistic_narrative") or tl.get("current_model") or "*(none provided)*")
    L.append("")

    # mechanism profile: Affinage's own GO/Reactome grounding, reproduced verbatim
    def terms(key, prefix=None):
        out = [f"{e.get('term_id')} {e.get('term_label')}" for e in (mp.get(key) or [])
               if prefix is None or str(e.get("term_id", "")).startswith(prefix)]
        return ", ".join(out) if out else "*(none)*"
    L.append("## Affinage mechanism profile (Affinage's own GO/Reactome grounding)")
    L.append("")
    L.append(f"- **molecular_activity:** {terms('molecular_activity')}")
    L.append(f"- **localization:** {terms('localization')}")
    L.append(f"- **pathway (Reactome):** {terms('pathway', 'R-')}")
    L.append(f"- **partners:** {', '.join(mp.get('partners') or []) or '*(none)*'}")
    L.append(f"- **complexes:** {', '.join(mp.get('complexes') or []) or '*(none)*'}")
    L.append("")

    # dated, confidence-graded discoveries
    L.append("## Dated findings (citation-anchored)")
    L.append("")
    L.append("| Year | Confidence | Finding | PMIDs | Journal |")
    L.append("|------|-----------|---------|-------|---------|")
    for d in disc:
        pm = ", ".join(f"PMID:{p}" for p in (d.get("pmids") or [])) or "—"
        finding = (d.get("finding") or "").replace("|", "\\|").replace("\n", " ")
        L.append(f"| {d.get('year','')} | {d.get('confidence','')} | {finding} | {pm} | {d.get('journal','')} |")
    L.append("")

    L.append("## Citations")
    L.append("")
    for p in all_pmids:
        L.append(f"- PMID:{p}")
    L.append("")
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description="Emit an Affinage record as an AIGR deep-research file (human only).")
    ap.add_argument("species")
    ap.add_argument("gene")
    ap.add_argument("--accession", help="Expected UniProt accession (else read from the gene's uniprot.txt)")
    ap.add_argument("--write", action="store_true",
                    help="Write to genes/<species>/<GENE>/<GENE>-deep-research-affinage.md")
    ap.add_argument("--out", help="Explicit output path (overrides --write location)")
    ap.add_argument("--force", action="store_true",
                    help="Write even if a blocking trust gate (accession mismatch / non-human "
                         "organism token) trips. Use only when you have verified the record "
                         "really does describe this gene.")
    args = ap.parse_args()

    if args.species.lower() != "human":
        sys.exit(f"❌ Affinage is HUMAN ONLY; refusing species '{args.species}'. "
                 f"Use a multi-species provider (perplexity/falcon/openai) instead.")

    try:
        data = fetch(args.gene)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        sys.exit(f"❌ fetch failed for {args.gene}: {e}")
    if not (data.get("narrative") or data.get("timeline")):
        sys.exit(f"❌ no Affinage record content for {args.gene}")

    expected = args.accession or local_accession(args.species, args.gene)
    doc = render(args.species, args.gene, data)

    # Trust gates are a reminder to the reviewer, printed to stderr — never written into
    # the provider file. Record the resulting judgment in the gene review's
    # references[].reference_review (relevance / correctness / review_notes).
    cautions = run_gates(args.gene, data, expected)
    if cautions:
        print(f"⚠️  {args.gene}: trust gate(s) tripped — record this in the review's "
              f"reference_review, NOT in the deep-research file:", file=sys.stderr)
        for blocking, c in cautions:
            print(f"    - {'[BLOCKING] ' if blocking else ''}{c}", file=sys.stderr)
    else:
        print(f"✓  {args.gene}: trust gates clear "
              f"(still record your own reference_review in the review).", file=sys.stderr)

    if args.out:
        dest = Path(args.out)
    elif args.write:
        dest = REPO / "genes" / args.species / args.gene / f"{args.gene}-deep-research-affinage.md"
    else:
        print(doc)
        return

    # The written file carries no in-file warning, so the wrong-protein gates are enforced
    # here instead: a record describing a different protein must not land in a gene folder,
    # where a later review of that gene would ingest it as a source.
    blocking = [c for is_blocking, c in cautions if is_blocking]
    if blocking and _in_gene_tree(dest) and not args.force:
        sys.exit(
            f"❌ refusing to write {dest}: {len(blocking)} blocking trust gate(s) tripped "
            f"(see stderr above). This record may describe a different protein, and a file in "
            f"a gene folder is ingested by a later review of that gene. Verify the record "
            f"first; pass --force to write anyway, or --out <path> to keep it outside genes/."
        )

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc)
    if blocking:
        print(f"⚠️  wrote {dest} despite {len(blocking)} blocking gate(s) (--force)", file=sys.stderr)
    print(f"wrote {dest}")


if __name__ == "__main__":
    main()
