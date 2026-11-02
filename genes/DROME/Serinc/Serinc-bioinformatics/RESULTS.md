# Serinc (M9PCT1) isoform and structure-residue analysis

Inputs: `serinc_isoforms_and_TMS1.fasta` (UniProt REST, retrieved 2026-10-21): the six FlyBase
Serinc products (PA Q9VV58, PB M9PI80, PC M9PCT1, PD M9PFH8, PE M9PFW5, PF M9PFR2) and yeast
TMS1 (Q12116, same PANTHER subfamily PTHR10383:SF9).

## Isoform comparison (`compare_isoforms.py`, output in `compare_isoforms_output.txt`)

- M9PCT1 (isoform C, 458 aa) is identical to isoform A (Q9VV58, 465 aa) except that it lacks a
  7-residue segment in the cytosolic loop between TM8 and TM9 (PA 360-375 DNSEKRVLTEALSDTE vs
  PC 360-368 DNSEKRDTE).
- Isoforms B, D and E differ from C only by short insertions/deletions at the same position (~366).
- Isoform F (M9PFR2, 467 aa; the FlyBase/UniProt gene-centric canonical and AlphaFold entry) shares
  M9PCT1 residues 1-412 and has an alternative C-terminal segment (from ~413), covering the last
  transmembrane helices.
- M9PCT1 is therefore a complete, native alternative-splice product of the single fly SERINC gene,
  not a fragment.

## Structure-residue mapping (`check_structure_residues.py`, output in `check_structure_residues_output.txt`)

- The residue numbering of the DmSERINC cryo-EM structure (PMID:31907454, PDB 6SP2) matches isoform A
  exactly (18/18 named residues, including disulphides C71-C95 and C238-C299).
- M9PCT1 carries all 18 named residues: 13 at identical positions and the five C-terminal ones
  (Y395, H401, T414, W418, K438 in isoform A numbering) at position minus 7 (Y388, H394, T407, W411, K431).
  The isoform-C deletion lies in a loop the paper modelled rather than resolved.
- So the experimental structure and lipid-binding data for DmSERINC apply to the M9PCT1 sequence,
  apart from the 7-residue loop difference.

## Limits

- No experiment tested isoform C specifically. Phobius predicts 9 TM segments for M9PCT1; the cryo-EM
  structure resolves 10.
- Identity to yeast TMS1 is low (141 identical positions in a global alignment). Do not transfer
  yeast-specific phenotypes.
