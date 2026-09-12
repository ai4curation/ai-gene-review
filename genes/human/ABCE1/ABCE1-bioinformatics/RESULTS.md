# ABCE1 (P61221) — sequence-level bioinformatics analysis

Reproducible support for three curation decisions in `ABCE1-ai-review.yaml`.
All numbers below are produced by `analyze.py`, which parses the curated
UniProt record `../ABCE1-uniprot.txt` at run time. Nothing is hardcoded.

## How to reproduce

```bash
cd genes/human/ABCE1/ABCE1-bioinformatics
python3 analyze.py            # pure standard library, no dependencies
# or, for a pinned environment:
uv run python analyze.py
```

## Methods

- **Input:** UniProt/Swiss-Prot record P61221 (`ABCE1-uniprot.txt`), 599 aa.
- **Transmembrane assessment:**
  1. Count of curated `TRANSMEM` feature keys in the UniProt feature table
     (authoritative line of evidence).
  2. Confirmatory Kyte–Doolittle (1982) hydropathy scan, sliding window 19,
     flagging any window whose mean hydropathy reaches the conventional
     transmembrane-helix threshold of 1.6.
- **Nucleotide-binding domains:** Walker A / P-loop consensus `[AG]-x(4)-G-K-[ST]`
  and a strict Walker B pattern `[ILVFM]{3,4}-D-E`.
- **Iron–sulfur architecture:** cysteine inventory and `CxxC` motifs in the
  N-terminal 80 residues, compared against the two UniProt-annotated
  `4Fe-4S ferredoxin-type` domains.

These are heuristics. The Kyte–Doolittle scan and the regular-expression motif
searches are corroborating, not definitive; the curated UniProt feature table
and the experimental literature cited in the review remain the primary evidence.

## Results

### 1. No transmembrane region — ABCE1 is a soluble cytosolic protein

The curated UniProt feature table for P61221 lists zero TRANSMEM features, and an independent Kyte-Doolittle scan (window 19) finds no window reaching the 1.6 transmembrane-helix threshold (global maximum 1.54 at residue 64), confirming ABCE1 has no transmembrane region and is a soluble cytosolic protein.

| Metric | Value |
|--------|-------|
| UniProt `TRANSMEM` features | **0** |
| Max 19-residue Kyte–Doolittle window mean | **1.54** (centered on residue 64) |
| Windows at/above the 1.6 TM-helix threshold | **0** |

The modest hydropathy peak at residue 64 lies inside the N-terminal Fe–S
ferredoxin fold (domain 2, residues 46–75), i.e. it is a buried hydrophobic
core, not a candidate membrane-spanning helix. This is consistent with the
UniProt subcellular location (`Cytoplasm`) and with the UniProt note that
*"The ABC transporter domains seem not to be functional"* — ABCE1 is an
ABC-family **ATPase that acts on cytosolic ribosomes**, not a membrane
transporter. This supports `REMOVE` of `GO:0016020` (membrane) and the
broader interpretation that transporter/membrane-style annotations are
over-annotations driven by the misleading "ABC sub-family E" name.

### 2. Two nucleotide-binding domains (Walker A / Walker B)

Two Walker A / P-loop motifs were found, at exactly the two ATP-binding sites
annotated by UniProt (`BINDING 110..117` and `BINDING 379..386`):

| NBD | Walker A position | Motif | Matches UniProt ATP `BINDING` |
|-----|-------------------|-------|-------------------------------|
| NBD1 | 110–117 | `GTNGIGKS` | 110–117 ✓ |
| NBD2 | 379–386 | `GENGTGKT` | 379–386 ✓ |

A canonical Walker B (`IFMFDE`, residues 237–242) is present in NBD1. NBD2's
Walker B (preceding residue ~486) carries an aromatic residue in its
hydrophobic run and so is not captured by the strict `[ILVFM]{3,4}DE` pattern —
consistent with the well-documented asymmetry/degeneracy of the two ABCE1 NBDs.
Together these confirm two intact nucleotide-binding domains, supporting the
`ATP binding` (GO:0005524) and `ATP hydrolysis activity` (GO:0016887)
annotations retained in the review.

### 3. N-terminal di-cluster [4Fe-4S] (ferredoxin) architecture

The N-terminal region (residues 1-80) contains nine cysteines arranged across the two UniProt-annotated 4Fe-4S ferredoxin-type domains (7-37 and 46-75), consistent with coordination of two [4Fe-4S] clusters rather than mononuclear iron.

| Metric | Value |
|--------|-------|
| Cysteines in residues 1–80 | **9** (positions 16, 21, 25, 29, 38, 55, 58, 61, 65) |
| `CxxC` motif starts | 55, 58 |
| UniProt ferredoxin domains | 7–37, 46–75 |
| UniProt/InterPro support | SUPFAM SSF54862 "4Fe-4S ferredoxins"; keyword `4Fe-4S` |

Eight cysteines are sufficient to coordinate two [4Fe-4S] clusters
(four per cluster); nine are observed. This supports the review's `MODIFY` of
`GO:0005506` (iron ion binding) to the more informative
`GO:0051539` (4 iron, 4 sulfur cluster binding).

## Limitations

- Kyte–Doolittle with a fixed window/threshold is a coarse predictor; a
  dedicated tool (DeepTMHMM, Phobius) would be more sensitive. Here it only
  corroborates the curated `TRANSMEM = 0`, which is the authoritative result.
- Motif regular expressions can miss divergent sites (as seen for NBD2 Walker B)
  and can in principle produce incidental matches; positions were cross-checked
  against the UniProt feature table.
- Cysteine counting does not prove cluster occupancy; it is consistent with,
  not proof of, two [4Fe-4S] clusters. Cluster occupancy is established
  experimentally and by structure in the cited literature.
