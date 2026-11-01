# CbcL (GEOSL, UniProtKB:Q74GH2) — CXXCH motif scan

## Purpose

The review's `GO:0020037` (heme binding) reason uses the number of CXXCH c-type
heme-binding motifs in the sequence as corroboration for the nine c-type hemes
measured on the purified periplasmic domain. This is the reproducible artifact
behind that count, replacing an asserted number with a checkable one.

The IDA evidence (pyridine hemochromogen quantitation, UV-vis/CD/NMR on the
purified 30–279 construct) carries that annotation on its own; this scan is
corroboration only, and a motif count is a sequence prediction, not a
measurement of bound heme.

## Method

`cxxch_scan.py` reads the amino-acid sequence from the committed UniProt flat
file `genes/GEOSL/cbcL/cbcL-uniprot.txt` and reports every match of the regular
expression `C..CH`, using a lookahead so overlapping motifs (which can share a
cysteine in multiheme cytochromes) are not lost. Standard library only, no
network access. Run from the repository root:

```
python genes/GEOSL/cbcL/cbcL-bioinformatics/cxxch_scan.py
```

**The sequence is pinned.** The script recomputes the UniProt CRC64 of the
residues it parsed and exits non-zero unless the sequence is **619 aa, CRC64
`12CE553CC08B6BA0`** — the values below were produced against that sequence. A
refetch that changes the entry therefore fails loudly instead of leaving this
table, and the review `description`'s motif-span claim, silently stale. When
that happens, re-run the script and rewrite this section and the pins from its
output; do not edit the table to match.

## Result

Verbatim output of the run that produced this section:

```
sequence length: 619 (pinned 619)
sequence CRC64: 12CE553CC08B6BA0 (pinned 12CE553CC08B6BA0)
CXXCH motifs found: 9
  35	CLGCH
  58	CTSCH
  83	CERCH
  106	CADCH
  130	CIQCH
  159	CNDCH
  187	CLKCH
  230	CADCH
  258	CAKCH
motif span: residues 35-262
```

Nine CXXCH motifs, at the 1-based position of the first cysteine:

| Position | Motif |
|---------:|-------|
| 35  | CLGCH |
| 58  | CTSCH |
| 83  | CERCH |
| 106 | CADCH |
| 130 | CIQCH |
| 159 | CNDCH |
| 187 | CLKCH |
| 230 | CADCH |
| 258 | CAKCH |

The motifs span residues 35-262, from the first cysteine of the first motif to
the histidine of the last, which is the span the review's `description` states.

## Interpretation

All nine motifs lie N-terminal to the first predicted transmembrane helix
(Phobius 286–314), i.e. in the periplasmic multiheme *c* domain. The count of
nine agrees with the nine c-type hemes reported for that domain, and no CXXCH
motif falls in the membrane domain — consistent with its two hemes being b-type
(non-covalently bound) rather than c-type.

The scan says nothing about the b-type hemes, which are inferred from the
NarI/FdnI-type diheme cytochrome *b* fold and remain unmeasured for this
protein.
