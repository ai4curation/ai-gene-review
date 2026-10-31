# loqs PF vs PB indel location (re-review, 2026-10-20)

Script: `compare_sequences_rereview.py` (reads the cached UniProt flat files `loqs-uniprot.txt` and
`loqs-reference-Q9VJY9-uniprot.txt`); output: `results/rereview.json`.

X2J5X6 (loqs-PF, 464 aa) equals Q9VJY9 (loqs-PB, 465 aa) except for a single-residue deletion of PB Lys384; the placement is unambiguous (no equivalent shifted position). The earlier RESULTS.md text gives the position as 383, which is an off-by-one: PB Gln383 is retained and Lys384 is the residue absent from PF.

PB position 384 is the first residue after the 338..383 segment that differs in isoforms PA and PC, and isoform PC diverges from 384 onward, so the deletion sits at an exon junction. This is consistent with alternative use of an adjacent splice acceptor, but splice-site sequence was not examined here.

The deleted lysine lies two residues after the LLKL 379..382 motif whose mutation strongly reduces Dcr-1 activity (PubMed:26769856), within the curated region 340..465 necessary for Dcr-1 interaction, and eight residues before DRBM 3 (393..461). All three DRBMs, the pre-miRNA-binding residues 308..309 and the Dcr-1-binding C-terminus are intact. Whether the missing lysine changes Dcr-1 binding or activity has not been tested; the function of PF is therefore inferred from PB, not measured.
