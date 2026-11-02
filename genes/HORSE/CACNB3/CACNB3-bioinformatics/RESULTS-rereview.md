# CACNB3 (horse A0A5F5PZM5): paralog and gene-model re-review

Script: `compare_paralogs_rereview.py` (fetches sequences live from UniProt; raw output in `results-rereview.json`).
Reproduce with `uv run python genes/HORSE/CACNB3/CACNB3-bioinformatics/compare_paralogs_rereview.py`.

## Identity of the gene model

A0A5F5PZM5 is 517 residues. Its conserved core (from the SYTSRPS motif at residue 53 to the C-terminus, 465 residues) is preceded by a 49-residue N-terminal segment, MAQGAKVSLRTNLSVELEGPRRFFPSLVRRQGLLQGKSGAAACPHIHQG, that is not present in human P54284 isoform 1 (whose N-terminal exon is MYDDSYVPGFEDSEA).

All five horse CACNB3 UniProt entries are products of one Ensembl gene, ENSECAG00000012018, and share an identical core with A0A5F5PZM5 (100% identity over the core). They differ in the first exon: A0A3Q2HUK8 begins MSFSDSSATFLLNE (as human isoform 4), F6SZ27 and A0A5F5PX04 begin MYDDSYVPGFEDSEA (as human isoform 1), A0A5F5PR94 begins MGRLRRRVPGTLRG, and A0A5F5PZM5 begins with the 49-residue segment above. A0A5F5PZM5 is therefore an alternative N-terminal (first-exon) gene model of horse CACNB3, not a fragment; the SH3 domain, HOOK region, guanylate-kinase-like domain and the C-terminal region are complete. None of the horse entries is a reviewed Swiss-Prot entry.

## Paralog placement

Over the shared core, A0A5F5PZM5 is 99.78% identical to human CACNB3 (P54284; 464/465 paired residues), against 63.36% to CACNB1 (Q02641), 65.09% to CACNB2 (Q08289) and 74.14% to CACNB4 (O00305). Together with the beta3-specific signatures in the horse record (InterPro IPR008079 VDCC_L_b3su, PRINTS PR01696 LCACHANNELB3, CDD cd12042 SH3_CACNB3) and VGNC orthology (VGNC:15992), this places the horse protein in the beta3 lineage (PANTHER PTHR11824:SF8 for human P54284), so beta3-specific functional evidence from human applies.

This is a pairwise identity comparison across the four paralogs, not a formal phylogeny; the gap between 99.78% and 74% is large enough that the beta3 assignment is unambiguous.
