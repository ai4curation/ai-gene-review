# MESK2 re-review: isoform identity and NDRG pseudo-active site

Script: `pseudo_active_site_rereview.py` (run with `uv run python pseudo_active_site_rereview.py`
from the repository environment; fetches sequences live from UniProt REST).
Raw output: `rereview-output.txt` (reproduced verbatim below).

## Interpretation

- Q8T0V2 (447 aa; cDNA clones GH02495/GH02835) is sequence-identical to A4UZR7, the
  reference-proteome (UP000000803) record for MESK2 isoforms A/E/F. It is a full-length
  alternative isoform, not a fragment.
- The UniProt gene-centric canonical for MESK2 is Q7KVN0 (isoform I, 485 aa), sequence-identical
  to the cDNA record Q9GU50, which is the accession that carries the gene's GOA rows.
- Q8T0V2 residues 83-420 are identical to Q7KVN0 residues 1-338. This shared block contains the
  whole Ndr (PF03096) alpha/beta-hydrolase-fold domain. Q8T0V2 adds an 82-residue N-terminal
  extension (MobiDB-lite disordered regions 1-27 and 67-87) and ends in a 27-residue isoform-specific C-terminus; isoform I
  instead has a 147-residue C-terminal tail rich in polar/Gly residues.
- At the nucleophile-elbow position that carries the catalytic serine of active alpha/beta
  hydrolases, MESK2 has Gly (Q8T0V2 G234; Q7KVN0 G152) within a GxGxG-type elbow
  (IGFGVGAGANI), matching the Gly146 of human NDRG2 (Gly132 in the numbering of PMID:21247902).
  Neither MESK2 isoform therefore carries a serine nucleophile at the canonical position.
  The two C-terminal triad positions fall in a region where the global alignment is less reliable
  (MESK2 S/L versus NDRG2 A/G); neither is the Asp/His expected of an active triad, but these two
  mappings should be read as provisional.

## Verbatim output

```
Q8T0V2 == A4UZR7 (sequence identical): True
Q8T0V2 proteomes: none
A4UZR7 proteomes: UP000000803: Chromosome 2R
Q7KVN0 proteomes: UP000000803: Chromosome 2R
Q9GU50 proteomes: none
Q8T0V2 length 447; Q7KVN0 length 485; Q9GU50 length 485
Q7KVN0 == Q9GU50: True
Q7KVN0 residues 1-40 found in Q8T0V2 at position 83
Identical shared block: Q8T0V2 83-420 == Q7KVN0 1-338
Q8T0V2-specific N-terminus: 1-82 (82 aa)
Q8T0V2-specific C-terminus: 421-447 (27 aa)
Q7KVN0-specific C-terminus: 339-485 (147 aa)
hNDRG2 Q9UN36 length 371; residues at 146/265/293: 146:G, 265:A, 293:G
Q8T0V2 vs hNDRG2: identity over aligned columns 0.39
  hNDRG2 146G -> Q8T0V2 (234, 'G')
  hNDRG2 265A -> Q8T0V2 (369, 'S')
  hNDRG2 293G -> Q8T0V2 (397, 'L')
  Q8T0V2 context around nucleophile-elbow position: IGFGVGAGANI
  hNDRG2 context: IGVGVGAGAYI
Q7KVN0 vs hNDRG2: identity over aligned columns 0.38
  hNDRG2 146G -> Q7KVN0 (152, 'G')
  hNDRG2 265A -> Q7KVN0 (287, 'S')
  hNDRG2 293G -> Q7KVN0 (315, 'L')
  Q7KVN0 context around nucleophile-elbow position: IGFGVGAGANI
  hNDRG2 context: IGVGVGAGAYI
```
