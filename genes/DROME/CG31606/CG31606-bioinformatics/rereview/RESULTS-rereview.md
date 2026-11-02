# CG31606 (Q8IPG8) independent homology re-review (2026-10-20)

Script: `homology_rereview.py` (raw output in `homology_rereview.json`). Run with
`uv run --no-project --with requests python homology_rereview.py`.

## Identity

Q8IPG8 is the only UniProtKB entry cross-referenced to FlyBase FBgn0051606 and is 197 aa.
OMA marks it as the main isoform. Two cDNA-derived TrEMBL fragments from the same gene
(G2J5W9, FI15332p1, 198 aa, 100% identity over residues 1-197; D9PTT6, MIP24303p, 142 aa,
100% identity over residues 56-197) confirm that the locus is transcribed. They are not
alternative products with different domain content. Q8IPG8 is therefore the canonical,
full-length product of CG31606 and not a fragment or alternative gene model.

## Family and domain signals

InterPro reports 0 integrated entries for Q8IPG8, and UniProt lists no PANTHER family.
The only feature is the SignalP-predicted signal peptide (residues 1-18).

## Phylogenetic distribution

- OMA HOG HOG:F0656038 is defined only at the levels "Drosophila melanogaster",
  "melanogaster subgroup" and "melanogaster group". The OMA orthologs are 1:1 in
  D. sechellia, D. simulans, D. erecta, D. yakuba (145 aa, N-terminally truncated model),
  D. ananassae (FBpp0118694), D. bipectinata and D. suzukii.
- blastp (EBI NCBI-BLAST, E <= 1e-3) against UniProtKB/Swiss-Prot returned **no hits**.
  Against UniProtKB Eukaryota, all 17 hits are from *Drosophila*. Strong hits (E <= 1e-16)
  come only from melanogaster-group species. Weak hits (E 1e-6 to 1e-3) cover parts of the
  sequence in other *Drosophila* genes: D. melanogaster CG42763 (M9MRG9; E = 4.3e-4,
  33.7% identity over query residues 3-88), and D. ananassae GF15502 and D. yakuba GE27627,
  which are annotated as "Protein TsetseEP domain-containing protein".

## Interpretation

CG31606 is a taxonomically restricted gene of the *D. melanogaster* species group. It has
no characterised ortholog in any model organism or in human, no PANTHER subfamily and no
PAINT node. Its nearest detectable relatives are uncharacterised *Drosophila* proteins,
some carrying a TsetseEP-type domain label, and they match at marginal E-values over part
of the sequence. That relationship is too weak, and the relatives too poorly characterised,
to support transferring any function. The results do not support the unnamed "vertebrate
homolog" flag reported in one expression-table source (see deep-research file).
