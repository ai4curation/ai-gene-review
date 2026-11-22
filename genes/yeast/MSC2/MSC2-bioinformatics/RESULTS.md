# MSC2 bioinformatics: CDF transmembrane zinc-binding site A

Script: `zinc_site_check.py` (run with `uv run --script zinc_site_check.py`; needs MAFFT on PATH).
Inputs: UniProt FASTA for the proteins listed below (`cdf_sequences.fasta`).
Alignment: MAFFT L-INS-i (`cdf_alignment.fasta`). Output table: `zinc_site_check.tsv`.

## Question

Cation diffusion facilitator (CDF) transporters move Zn2+ through a transmembrane
binding site (site A) formed by two residues on TM2 and two on TM5. In E. coli YiiP
(P69380) these are D45, D49, H153 and D157 (UniProt BINDING features,
PubMed:19749753). Msc2 forms a heteromer with Zrg17, and its human counterpart ZnT5
pairs with ZnT6. Does Msc2 keep the site, and does its partner?

## Result (residues aligned to YiiP site A)

| Protein | YiiP D45 | YiiP D49 | YiiP H153 | YiiP D157 |
|---|---|---|---|---|
| YiiP_ECOLI P69380 (reference) | D45 | D49 | H153 | D157 |
| Msc2_YEAST Q03455 (target) | H420 | D424 | H531 | D535 |
| Cis4_SCHPO Q9HGQ3 | H382 | D386 | H589 | D593 |
| ZnT5_HUMAN Q8TAD4 | H451 | D455 | H595 | D599 |
| Zrg17_YEAST P53735 | F261 | D265 | T386 | N390 |
| ZnT6_HUMAN Q6NXT4 | L66 | D70 | F201 | D205 |
| Zrc1_YEAST P20107 (vacuolar CDF control) | H41 | D45 | H238 | D242 |

## Interpretation

Msc2 has a complete His-Asp-His-Asp site A, the same as its PTHR45755:SF4 relatives
Cis4 and ZnT5, and the same as the zinc-transporting vacuolar CDF Zrc1. Its partner
Zrg17 has lost three of the four ligands (F/D/T/N), as has ZnT6 (L/D/F/D). This fits a
model in which Msc2 is the subunit that binds and moves zinc in the Msc2-Zrg17
heteromer and Zrg17 is a structural or modulatory partner without its own substrate
site. The analysis is a sequence prediction. It shows that the site is retained, not
that it is used: no direct zinc-flux assay of Msc2 or of the Msc2-Zrg17 complex has
been reported.
