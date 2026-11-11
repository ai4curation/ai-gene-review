# At3g08840 (A0A1I9LPE3): conservation of D-Ala-D-Ala ligase catalytic residues

## Method

`catalytic_residues.py` (run: `uv run --project /home/user/ai-gene-review python catalytic_residues.py > results.txt`)
fetches, at run time, the UniProt sequences of At3g08840 (A0A1I9LPE3), the moss
*Physcomitrium patens* DDL (Q3LHI3; genetically shown to act as a D-Ala:D-Ala ligase in
PMID:27325639) and E. coli DdlB (P07862) / DdlA (P0A6J8). It:

1. scans each plant protein with the PROSITE D-Ala-D-Ala ligase signatures PS00843 and
   PS00844 (patterns fetched from PROSITE at run time);
2. locally aligns E. coli DdlB/DdlA (BLOSUM62) to each of the two Ddl modules of the plant
   proteins, and reports the plant residue at every single-residue `Active site` and
   `Binding site` (Mg2+) position in the E. coli UniProt feature tables.

Raw output: `results.txt`.

## Results (from results.txt)

- At3g08840 consists of two tandem Ddl modules (DdlB aligns to residues ~79-454 and
  ~486-908; 35% and 41% identity over the aligned regions). The moss DDL has the same
  two-module architecture.
- **Module 2 (C-terminal) of At3g08840 carries both PROSITE D-Ala-D-Ala ligase signatures**
  (PS00843 at 631 `HGGIGEDGTLQG`; PS00844 at 872, ending in the Mg2+-binding `E-x-N-T-x-P-G`
  motif `EVNTVPG`). It retains the DdlB active-site Glu15 equivalent (E497) and all three
  Mg2+ ligands (D881, E895, N897). Two DdlB active-site serines are substituted
  (Ser150 -> Cys723 in a `GCSTG` loop; Ser281 -> Thr906, alignment in this region is less
  certain).
- **Module 1 (N-terminal)** retains the Glu15 (E90) and Ser150 (S261, `GSSIG`) equivalents
  but has a diverged Mg2+-binding loop (`ARIDGWY...IFTDINL`, DdlB E270 -> D419 in one
  alignment; E. coli DdlA alignment places a gap/different residues here), and does not
  match PS00844.
- **The moss DDL shows the same pattern**: module 1 has the diverged Mg-binding loop
  (`IFSDINL`), module 2 has the canonical `EANTVPG` motif plus the same Ser150 -> Cys
  (`GCSTG`) substitution. Moss DDL matches PS00843 in module 1 and PS00844 in module 2.

## Interpretation

The Arabidopsis protein shows no lineage-specific loss of catalytic or Mg2+-binding
residues relative to the moss DDL, whose D-Ala:D-Ala ligase function is supported by
knockout, D-Ala accumulation and D-Ala-D-Ala dipeptide rescue (PMID:27325639). The
substitutions that differ from E. coli DdlB are shared by the functional moss enzyme, so
they cannot by themselves be read as evidence of inactivation. This analysis does **not**
demonstrate activity: no biochemical assay of the Arabidopsis protein is published, and
residue conservation is consistent with, but does not prove, retained ligase activity.

Limitations: pairwise local alignments only (no structural model, no multiple alignment
across angiosperms); positions near alignment gaps (e.g. DdlB Ser281, Glu270 in module 1)
are uncertain.
