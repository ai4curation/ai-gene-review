# OLFML2A (Piliocolobus tephrosceles, A0A8C9H9A8): ortholog comparison

Script: `compare_orthologs.py` (run with `uv run --no-project --with biopython --with requests python compare_orthologs.py`).
Raw output: `results.json`. Sequences and PANTHER cross-references were fetched live from UniProt REST on 2026-10-21.

## Method

Global pairwise alignment (BLOSUM62, gap open -10, extend -0.5, free end gaps) of the target against
human OLFML2A (Q68BL7), mouse Olfml2a/photomedin-1 (Q8BHP7) and the shorter red colobus entry from the
same Ensembl gene (A0A8C9H4D2). Identity is computed over aligned (non-gap) columns. Cysteines in the
target olfactomedin domain (residues 397-655, PROSITE PS51132) were checked for conservation. The
target was also scanned for the N-terminal CXCXCX9C motif described for photomedins.

## Results

| Comparison | Length | PANTHER subfamily | Identity (aligned cols) | Target coverage | OLF-domain Cys conserved |
|---|---|---|---|---|---|
| A0A8C9H9A8 vs human Q68BL7 | 652 | PTHR23192:SF29 | 97.5% (636/652) | 99.5% | 3/3 |
| A0A8C9H9A8 vs mouse Q8BHP7 | 681 | PTHR23192:SF29 | 84.0% (547/651) | 99.4% | 3/3 |
| A0A8C9H9A8 vs A0A8C9H4D2 | 439 | PTHR23192:SF29 | 98.4% (432/439) | 67.0% | 3/3 |

- The target has a predicted signal peptide (1..27, SignalP), as does human Q68BL7 (1..27) and mouse
  Q8BHP7 (1..32).
- Two CXCXCX9C motifs are present in the target N-terminal region, at residues 47 (CRCKCIMRPLSKDAC)
  and 86 (CRCSCTAPPSSLNPC).
- All four proteins are classified in the same PANTHER subfamily, PTHR23192:SF29 (OLFACTOMEDIN-LIKE
  PROTEIN 2A).

## Interpretation

The target is the red colobus ortholog of human OLFML2A and mouse photomedin-1: same PANTHER
subfamily, near-full-length alignment, high identity, a predicted signal peptide, the photomedin
N-terminal cysteine motifs and conserved olfactomedin-domain cysteines. This supports transfer of the
subfamily-level properties that were established experimentally for mouse photomedin-1 (secretion,
disulfide-linked dimerization, binding to chondroitin sulfate E and heparin). No experiment has been
performed on the red colobus protein itself.

The identity to A0A8C9H4D2 computed here (98.4% over 439 aligned columns) differs slightly from the
99.8% figure supplied with the task; the difference likely reflects alignment parameters around the
region where the shorter model diverges, and was not investigated further.
