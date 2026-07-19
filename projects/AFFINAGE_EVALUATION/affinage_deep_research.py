#!/usr/bin/env python3
"""Emit an Affinage record as an AIGR deep-research source file (HUMAN ONLY).

Affinage (affinage.wi.mit.edu) precomputes a citation-anchored mechanistic
narrative for every human protein-coding gene. The AIGR review workflow already
picks up any ``genes/<sp>/<GENE>/<GENE>-deep-research-*.md`` file, so "wiring in"
Affinage needs no pipeline change: this tool fetches the record and writes
``<GENE>-deep-research-affinage.md`` in the same shape as the other providers.

This is the ONLY Affinage integration the evaluation endorses — a *free precomputed
first pass for the human backlog* (see ../results/narrative-vs-go.md). It is gated by
the two cheap checks that evaluation identified:

  1. HUMAN ONLY. Affinage covers only human; the tool refuses any other species.
  2. Entity-collision / trust gates. It surfaces Affinage's own ``evaluation.pairwise``
     self-signal (win/tie/loss) and compares the record's UniProt accession to the
     local ``<GENE>-uniprot.txt`` (and scans the narrative's opening for a non-human
     organism token) — the ADA-style symbol-collision failure. Any tripped gate is
     written as a prominent ⚠️ CAUTION banner at the top of the file, never hidden.

The file is genuinely Affinage-sourced (not authored here); provenance — source URL,
Affinage run date, and the gate results — is recorded in the frontmatter so a curator
treats it as external preliminary research, exactly like a falcon/perplexity report.

Usage:
    python affinage_deep_research.py human GPX4                 # print to stdout
    python affinage_deep_research.py human GPX4 --write         # -> genes/human/GPX4/GPX4-deep-research-affinage.md
    python affinage_deep_research.py human ADA                  # gate trips -> CAUTION banner
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


def run_gates(gene: str, data: dict, expected_acc: str | None) -> list[str]:
    """Return a list of human-readable CAUTION strings (empty = all clear)."""
    cautions: list[str] = []
    up = (data.get("prefetch_data") or {}).get("uniprot") or {}
    aff_acc = up.get("accession")
    ev = data.get("evaluation") or {}
    pairwise = ev.get("pairwise")
    narr = (data.get("narrative") or {}).get("mechanistic_narrative", "") or ""
    model = (data.get("timeline") or {}).get("current_model", "") or ""

    if pairwise and pairwise != "win":
        cautions.append(
            f"Affinage's own head-to-head self-evaluation scored this record "
            f"`pairwise = {pairwise}` (not `win`) vs the curated UniProt reference — "
            f"treat the narrative with extra scepticism.")
    if expected_acc and aff_acc and expected_acc != aff_acc:
        cautions.append(
            f"Accession mismatch: local review uses `{expected_acc}` but the Affinage "
            f"record's prefetch UniProt accession is `{aff_acc}`.")
    opening = (model[:220] + " " + narr[:220]).lower()
    hit = next((t for t in NONHUMAN_TOKENS if t in opening), None)
    if hit:
        cautions.append(
            f"Possible symbol collision: the narrative's opening names a non-human "
            f"context (\"{hit}\") despite a human record — verify the narrative "
            f"describes human {gene} and not a same-symbol protein (cf. the ADA case).")
    return cautions


def render(species: str, gene: str, data: dict, expected_acc: str | None) -> str:
    tl = data.get("timeline") or {}
    nar = data.get("narrative") or {}
    up = (data.get("prefetch_data") or {}).get("uniprot") or {}
    ev = data.get("evaluation") or {}
    mp = nar.get("mechanism_profile") or {}
    disc = tl.get("discoveries") or []
    cautions = run_gates(gene, data, expected_acc)

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
    L.append(f"gates_passed: {not cautions}")
    L.append("note: >-")
    L.append("  Machine-fetched from the Affinage API (Cheeseman Lab). This is external")
    L.append("  precomputed research to be treated as a preliminary source, NOT a curated")
    L.append("  annotation. Affinage is human-only and LLM-generated; verify claims against")
    L.append("  the cited PMIDs before use.")
    L.append("---")
    L.append("")
    L.append(f"# Affinage mechanistic annotation for {gene} ({species})")
    L.append("")

    if cautions:
        L.append("> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**")
        for c in cautions:
            L.append(f">")
            L.append(f"> - {c}")
        L.append("")

    L.append("## Current model (mechanistic narrative)")
    L.append("")
    L.append(nar.get("mechanistic_narrative") or tl.get("current_model") or "*(none provided)*")
    L.append("")

    # mechanism profile (Affinage's own GO/Reactome grounding — recorded, not trusted)
    def terms(key):
        out = [f"{e.get('term_id')} {e.get('term_label')}" for e in (mp.get(key) or [])]
        return ", ".join(out) if out else "*(none)*"
    L.append("## Affinage mechanism profile (its own GO/Reactome grounding)")
    L.append("")
    L.append("_Recorded for reference. The AIGR evaluation found this grounding is coarse "
             "(collapses to general parents) and can contradict the narrative — do not import "
             "these GO ids directly; re-ground from the narrative + PMIDs._")
    L.append("")
    L.append(f"- **molecular_activity:** {terms('molecular_activity')}")
    L.append(f"- **localization:** {terms('localization')}")
    L.append(f"- **pathway (Reactome):** {terms('pathway')}")
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
    doc = render(args.species, args.gene, data, expected)

    if args.out:
        Path(args.out).write_text(doc)
        print(f"wrote {args.out}")
    elif args.write:
        dest = REPO / "genes" / args.species / args.gene / f"{args.gene}-deep-research-affinage.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(doc)
        print(f"wrote {dest}")
    else:
        print(doc)


if __name__ == "__main__":
    main()
