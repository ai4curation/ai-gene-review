#!/usr/bin/env python3
"""Extract UniProt CAUTION comment notes from cached *-uniprot.txt records.

A UniProt flat-file record may carry one or more free-text CAUTION comments:

    CC   -!- CAUTION: <free text, possibly spanning multiple lines>
    CC       ... continuation ...   {ECO:0000305|PubMed:NNNN}.

These flag warnings the curator wants a reader to heed: contested/controversial
functions, retracted supporting papers, mis-attributed activities, sequence
artifacts, "was initially believed to be ..." reclassifications, etc.

This is distinct from the structured `-!- SEQUENCE CAUTION:` block (erroneous
initiation / frameshift / etc.), which we deliberately EXCLUDE here.

Usage:
    python extract_caution_notes.py [--genes-dir genes] [--out report]

Writes:
    caution_notes.tsv  - one row per CAUTION note (gene, organism, uniprot id, text, pmids)
    caution_notes.md   - human-readable grouped report

Never hardcodes results; if no notes are found it reports zero.
"""
from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

PMID_RE = re.compile(r"(?:PubMed|PMID):(\d+)", re.IGNORECASE)


@dataclass
class CautionNote:
    organism: str
    gene: str
    uniprot_id: str
    text: str
    pmids: list[str] = field(default_factory=list)

    @property
    def retracted(self) -> bool:
        return "retract" in self.text.lower()

    @property
    def curation_relevant(self) -> bool:
        return self.category not in ("wgs-preliminary", "lacks-conserved-residue")

    @property
    def category(self) -> str:
        t = self.text.lower()
        # automatic / boilerplate notes (low curation value)
        if "whole genome shotgun" in t or "wgs" in t:
            return "wgs-preliminary"
        if "lacks conserved residue" in t:
            return "lacks-conserved-residue"
        # curation-meaningful notes
        if "retract" in t:
            return "retracted-reference"
        if ("lacks" in t and any(w in t for w in ("active site", "catalytic", "conserved",
                                                  "heme-binding", "phospho-accepting",
                                                  "essential", "required"))) \
                or ("although" in t and "lacks" in t) \
                or "probably not" in t or "may not be functional" in t:
            return "degenerate-domain"
        if "was initially" in t or "was originally" in t or "was reported" in t or "previously" in t:
            return "reclassified-function"
        if "artifact" in t or "artefact" in t:
            return "possible-artifact"
        if any(w in t for w in ("controvers", "uncertain", "in contrast", "however",
                                "may not", "could be", "disput", "remains to be",
                                "not clear", "unclear", "questioned")):
            return "contested-function"
        return "other"


def parse_record(path: Path) -> tuple[str | None, list[CautionNote]]:
    """Parse one *-uniprot.txt file. Returns (uniprot_id, notes)."""
    organism = path.parts[-3] if len(path.parts) >= 3 else ""
    gene = path.parent.name
    uniprot_id = None
    notes: list[CautionNote] = []

    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

    current: list[str] | None = None  # accumulating CAUTION text lines

    def flush():
        nonlocal current
        if current:
            text = " ".join(current).strip()
            # drop the trailing {ECO...} evidence braces for readability,
            # but keep PMIDs (extracted separately from the raw text first).
            pmids = sorted(set(PMID_RE.findall(text)), key=int)
            clean = re.sub(r"\{ECO:[^}]*\}", "", text).strip()
            clean = re.sub(r"\s+", " ", clean).rstrip(". ").strip()
            notes.append(CautionNote(organism, gene, uniprot_id or "", clean, pmids))
        current = None

    for line in lines:
        if uniprot_id is None and line.startswith("AC "):
            uniprot_id = line[5:].split(";")[0].strip()

        if line.startswith("CC   -!- CAUTION:"):
            flush()
            current = [line[len("CC   -!- CAUTION:"):].strip()]
        elif current is not None and line.startswith("CC       "):
            current.append(line[len("CC       "):].strip())
        elif current is not None:
            # any other CC topic / non-CC line ends the note
            flush()

    flush()
    return uniprot_id, notes


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genes-dir", default="genes")
    ap.add_argument("--out", default="projects/UNIPROT_CAUTION_NOTE")
    args = ap.parse_args()

    genes_dir = Path(args.genes_dir)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    all_notes: list[CautionNote] = []
    files_with = 0
    for path in sorted(genes_dir.glob("*/*/*-uniprot.txt")):
        _, notes = parse_record(path)
        if notes:
            files_with += 1
            all_notes.extend(notes)

    # TSV
    tsv_path = out_dir / "caution_notes.tsv"
    with tsv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["organism", "gene", "uniprot_id", "category", "retracted", "pmids", "text"])
        for n in sorted(all_notes, key=lambda x: (x.category, x.organism, x.gene)):
            w.writerow([n.organism, n.gene, n.uniprot_id, n.category, n.retracted,
                        ";".join(n.pmids), n.text])

    # Markdown summary
    by_cat: dict[str, list[CautionNote]] = {}
    for n in all_notes:
        by_cat.setdefault(n.category, []).append(n)

    md = out_dir / "caution_notes.md"
    with md.open("w", encoding="utf-8") as fh:
        fh.write("---\ntitle: \"UniProt CAUTION Notes — Extracted Data\"\n---\n\n")
        fh.write("# UniProt CAUTION Notes — Extracted Data\n\n")
        fh.write("Auto-generated by `extract_caution_notes.py`. Do not edit by hand.\n\n")
        n_relevant = sum(n.curation_relevant for n in all_notes)
        fh.write(f"- Records with >=1 CAUTION note: **{files_with}**\n")
        fh.write(f"- Total CAUTION notes: **{len(all_notes)}**\n")
        fh.write(f"- Curation-relevant notes (excludes WGS/lacks-conserved boilerplate): **{n_relevant}**\n")
        fh.write(f"- Retracted-reference notes: **{sum(n.retracted for n in all_notes)}**\n\n")
        fh.write("## Notes by category\n\n")
        for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
            fh.write(f"### {cat} ({len(by_cat[cat])})\n\n")
            for n in sorted(by_cat[cat], key=lambda x: (x.organism, x.gene)):
                pmids = (" [PMIDs: " + ", ".join(n.pmids) + "]") if n.pmids else ""
                fh.write(f"- **{n.organism}/{n.gene}** ({n.uniprot_id}): {n.text}{pmids}\n")
            fh.write("\n")

    print(f"records_with_caution={files_with} total_notes={len(all_notes)}")
    print(f"wrote {tsv_path} and {md}")


if __name__ == "__main__":
    main()
