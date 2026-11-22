#!/usr/bin/env python3
"""Reproduce the initial project Markdown from the adjacent ClinGen CSV snapshot.

Uses only the Python standard library. Writes to stdout; compare with the current
project before replacing it, so later review progress and notes are preserved.
"""

import csv
import hashlib
import io
import json
import sys
from collections import Counter, defaultdict
from contextlib import redirect_stdout
from pathlib import Path


SOURCE_URL = "https://search.clinicalgenome.org/kb/gene-validity/download"
LEVELS = ("Definitive", "Strong", "Moderate", "Limited")
NEGATIVE = {"Disputed", "Refuted", "No Known Disease Relationship"}
MODES = {"AD", "AR", "XL", "SD", "MT", "UD"}
HERE = Path(__file__).resolve().parent


def main():
    source = HERE / "clingen-gene-disease-validity.csv"
    raw = source.read_bytes()
    records = list(csv.reader(raw.decode("utf-8-sig").splitlines()))
    header_index = next(i for i, row in enumerate(records) if row[0] == "GENE SYMBOL")
    header = records[header_index]
    rows = []
    for row in records[header_index + 1:]:
        if not row or row[0].startswith("+++"):
            continue
        if len(row) != len(header):
            raise ValueError(f"Malformed source row: {row!r}")
        record = dict(zip(header, row))
        if record["CLASSIFICATION"] not in set(LEVELS) | NEGATIVE:
            raise ValueError(f"Unrecognized classification: {record!r}")
        if record["MOI"] not in MODES:
            raise ValueError(f"Unrecognized inheritance: {record!r}")
        if not record["GENE ID (HGNC)"].startswith("HGNC:"):
            raise ValueError(f"Missing HGNC identifier: {record!r}")
        rows.append(record)

    date = next(r[0].split(": ", 1)[1] for r in records if r[0].startswith("FILE CREATED:"))
    positive = [r for r in rows if r["CLASSIFICATION"] in LEVELS]
    genes = defaultdict(list)
    for row in positive:
        genes[row["GENE ID (HGNC)"]].append(row)
    hgnc_records = json.loads((HERE / "hgnc-symbols.json").read_text())
    symbols = {r["hgnc_id"]: r["symbol"] for r in hgnc_records["genes"]}
    if set(symbols) != set(genes):
        raise ValueError("HGNC snapshot and ClinGen positive set differ")
    if len(set(symbols.values())) != len(genes):
        raise ValueError("HGNC symbol collision")
    locus = {r["hgnc_id"]: r for r in hgnc_records["genes"]}
    rna = {h for h in genes if locus[h]["locus_group"] == "non-coding RNA"}
    other = {h for h in genes if locus[h]["locus_group"] == "other"}
    if any(r["locus_group"] not in {"protein-coding gene", "non-coding RNA", "other"}
           for r in locus.values()):
        raise ValueError("Unrecognized HGNC locus group")
    strongest = {
        hgnc: min((r["CLASSIFICATION"] for r in rs), key=LEVELS.index)
        for hgnc, rs in genes.items()
    }
    nuclear = {h for h, rs in genes.items() if any(r["MOI"] in {"AD", "AR", "XL", "SD"} for r in rs)}
    mitochondrial = {h for h, rs in genes.items() if h not in nuclear and any(r["MOI"] == "MT" for r in rs)}
    undetermined = set(genes) - nuclear - mitochondrial
    classes = Counter(r["CLASSIFICATION"] for r in rows)

    print('---\ntitle: "ClinGen Mendelian Disease Genes"\nmaturity: SCOPING\ntags: [BIOLOGY_DOMAIN]\nspecies: [human]\nautolink_gene_symbols: false\ngenes:')
    for symbol in sorted(symbols.values()):
        print(f"  - {json.dumps('human/' + symbol)}")
    print(f'''---

# ClinGen Mendelian Disease Genes

## Overview

Seed a human gene-function review project from ClinGen's published Gene–Disease
Validity curations. Review the molecular functions, cellular roles, and GO
annotations of these gene products; disease association alone does not establish
a GO molecular function or participation in a biological process.

## Source and scope

- Source: [ClinGen Gene–Disease Validity download]({SOURCE_URL}), linked from the
  [official downloads page](https://search.clinicalgenome.org/kb/downloads).
- Snapshot file date and retrieval date: **{date}**.
- Archived, unmodified source: [ClinGen CSV](CLINGEN_MENDELIAN/clingen-gene-disease-validity.csv).
- SHA-256: `{hashlib.sha256(raw).hexdigest()}`.
- Select every gene with at least one **Definitive, Strong, Moderate, or Limited**
  association. Limited associations are candidates, not established causation.
- Deduplicate by HGNC ID and normalize to approved symbols using the
  [HGNC complete set]({hgnc_records['source_url']}); the
  [archived HGNC subset](CLINGEN_MENDELIAN/hgnc-symbols.json) records the mappings,
  retrieval timestamp, and full-download checksum. Preserve every
  qualifying disease, inheritance mode, classification, and report link below.
- Disputed, Refuted, and No Known Disease Relationship rows do not qualify a
  gene. A gene with another positive association remains included; its presence
  does not endorse its excluded associations. All rows remain in the CSV.
- The main Mendelian list uses AD, AR, XL, or SD inheritance. Mitochondrial
  genes are included separately for comprehensive inherited-disease coverage;
  mitochondrial inheritance is not classical Mendelian inheritance.
- Genes supported only by undetermined inheritance are a separate follow-up
  list, not confirmed Mendelian genes. Individual UD associations on otherwise
  included genes are also explicitly labeled.
- This is the complete positive set **within this ClinGen export**, not a census
  of every Mendelian disease gene. Dosage Sensitivity, Clinical Actionability,
  and ClinVar variant assertions are not substituted for Gene–Disease Validity.

## Seed summary

| Measure | Count |
|---|---:|
| Source curations | {len(rows)} |
| Source unique genes (HGNC IDs) | {len({r['GENE ID (HGNC)'] for r in rows})} |
| Included positive associations | {len(positive)} |
| Total genes in this project, including follow-up lists | {len(genes)} |
| Nuclear Mendelian genes (AD / AR / XL / SD) | {len(nuclear)} |
| Additional mitochondrial genes | {len(mitochondrial)} |
| Additional genes with undetermined inheritance only | {len(undetermined)} |
| HGNC protein-coding genes (across all inheritance groups) | {len(genes) - len(rna) - len(other)} |
| Non-coding RNA genes (separate workflow) | {len(rna)} |
| Other HGNC locus types (separate identifier triage) | {len(other)} |

| ClinGen classification | Source associations | Genes whose strongest positive association is this level |
|---|---:|---:|''')
    counts = Counter(strongest.values())
    for level in (*LEVELS, "Disputed", "Refuted", "No Known Disease Relationship"):
        print(f"| {level} | {classes[level]} | {counts[level] if level in LEVELS else 'Excluded'} |")
    print(f'''
The classification table counts all genes, including mitochondrial and
undetermined inheritance. Inheritance-group and locus-group counts are two
different partitions of the same inventory. Each individual association retains
its own classification in the checklist. RNA and other locus types have separate
checklist sections, so nuclear protein-coding headings exclude those genes.

## Status

- [x] Acquire and archive ClinGen source data.
- [x] Seed the complete gene inventory and preserve association provenance.
- [ ] Triage existing human reviews and prioritize new reviews by evidence level.
- [ ] Fetch missing gene records, research, review annotations, and validate.

All gene checkboxes start unchecked: they track assessment for this project,
not whether a review happens to exist elsewhere in the repository. The seed step
does not fetch or complete thousands of individual gene reviews. The {len(rna)}
RNA genes remain in scope and use RNA-specific identifiers, sequences, and
functional literature rather than UniProt-dependent fetching. The {len(other)}
other HGNC loci (readthrough or immune-receptor genes) require identifier/product
triage; an HGNC group of "other" does not imply absence of a protein product.

## Reproducing the seed

The [seed script](CLINGEN_MENDELIAN/seed_project.py) uses only Python's standard library:

```bash
python3 projects/CLINGEN_MENDELIAN/seed_project.py > /tmp/CLINGEN_MENDELIAN.md
diff -u projects/CLINGEN_MENDELIAN.md /tmp/CLINGEN_MENDELIAN.md
```

It generates a fresh seed from the archived CSV and HGNC subset, including locus
types. Differences in maturity, campaign status, progress links, checkbox states,
and notes are expected once the campaign starts. Compare before replacing the
project so that authored campaign state is preserved. For a future
refresh, download the official CSV again, record its actual retrieval date,
inspect membership changes, and add a new project history record.

## Gene checklist

AD = autosomal dominant; AR = autosomal recessive; XL = X-linked;
SD = semidominant; MT = mitochondrial; UD = undetermined.
Each linked disease opens its ClinGen evidence report. Parentheses give the
MONDO ID, inheritance mode, and association-specific evidence classification.
''')

    def emit(group, heading):
        print(f"\n### {heading} ({len(group)} genes)\n")
        for hgnc in sorted(group, key=symbols.get):
            symbol = symbols[hgnc]
            reports = []
            for r in sorted(genes[hgnc], key=lambda r: (r["DISEASE LABEL"], r["MOI"], r["CLASSIFICATION"], r["ONLINE REPORT"])):
                label = r["DISEASE LABEL"].replace("[", "\\[").replace("]", "\\]")
                mode = r["MOI"] if r["MOI"] != "UD" else "UD — inheritance undetermined"
                reports.append(f"[{label}]({r['ONLINE REPORT']}) ({r['DISEASE ID (MONDO)']}; {mode}; {r['CLASSIFICATION']})")
            aliases = sorted({r["GENE SYMBOL"] for r in genes[hgnc]} - {symbol})
            alias_note = f" (ClinGen source symbol: {', '.join(aliases)})" if aliases else ""
            type_note = f" [{locus[hgnc]['locus_type']}]" if hgnc in rna | other else ""
            print(f"- [ ] **{symbol}** — {hgnc}{alias_note}{type_note}; " + "; ".join(reports) + ".")

    for level in LEVELS:
        emit({h for h in nuclear - rna - other if strongest[h] == level}, f"Nuclear Mendelian protein-coding genes: {level}")
    emit(mitochondrial - rna - other, "Additional mitochondrial protein-coding disease genes")
    emit(rna, "RNA genes: dedicated RNA-function review workflow")
    emit(other, "Other HGNC locus types: identifier and product triage")
    emit(undetermined - rna - other, "Follow-up: undetermined inheritance only")
    print(f"\n## Notes\n\n### {date}\n\nInitial source-based seed only. No gene-level curation sign-offs were made.\n")


if __name__ == "__main__":
    # Validate the complete output before publishing any of it to stdout. Braces
    # are not part of this Markdown format and usually reveal a missed f-string.
    output = io.StringIO()
    with redirect_stdout(output):
        main()
    rendered = output.getvalue()
    if "{" in rendered or "}" in rendered:
        raise ValueError("Unexpected braces in generated Markdown; check for unexpanded template expressions")
    sys.stdout.write(rendered)
