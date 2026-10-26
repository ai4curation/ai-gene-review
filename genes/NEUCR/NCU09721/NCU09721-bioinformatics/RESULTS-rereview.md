# NCU09721 (Q7S2Q5) beta-adaptin placement: re-review analysis (2026-10-21)

Script: `beta_adaptin_phylogeny_rereview.py` (PEP 723; run with `uv run --script`; needs MAFFT on PATH).
Raw output: `beta_adaptin_phylogeny_rereview.out.txt`; tree: `beta_adaptins_rereview.nwk`;
alignment: `beta_adaptins_rereview.aln.fasta`.

## Question

N. crassa has two PTHR11134 non-AP-3 beta-adaptins of near-identical length: NCU09721 (Q7S2Q5, 749 aa)
and NCU05232 (Q7S8H6, 748 aa). Dikarya have separate AP-1 beta (Apl2) and AP-2 beta (Apl1) genes, so
which paralog is NCU09721? UniProt reports only the family PTHR11134 (no subfamily) for Q7S2Q5.

## Method

16 sequences (N. crassa NCU09721, NCU05232, NCU06569 AP-3 beta; S. cerevisiae APL2/APL1; S. pombe apl2/apl1;
A. nidulans AN3029/AN5950; F. graminearum three PTHR11134 proteins; human AP1B1, AP2B1, AP3B1; Dictyostelium
ap1b1) were aligned with MAFFT --auto; a BLOSUM62-distance neighbour-joining tree was rooted on human AP3B1,
with 100 column-bootstrap replicates.

## Results

- NCU09721 clusters with F. graminearum V6RKE4 (100/100) and A. nidulans AN3029 (100/100), then with
  S. pombe apl2, the AP-1 beta subunit (96/100). The support for including S. cerevisiae APL2 is weaker (40/100),
  which is consistent with the long budding-yeast branch.
- NCU05232 instead clusters with A. nidulans AN5950, F. graminearum V6RQ48, S. pombe apl1 and S. cerevisiae
  APL1 (the AP-2 beta clade). NCU06569 groups with the AP-3 beta proteins.
- Target identity: 83.4% to Fusarium V6RKE4, 79.4% to A. nidulans AN3029, 49.1% to S. pombe apl2, and
  40.6% to its own paralog NCU05232.
- A. nidulans AN3029 has LLDID at 653 and LLNGF at 730. These are the two C-terminal motifs that the
  Aspergillus AP-1 study reported at positions 630 and 707. The 77-residue spacing is the same, so the
  constant 23-residue offset is an N-terminal gene-model difference. AN3029 is therefore the
  experimentally studied A. nidulans AP-1 beta.
- NCU09721 retains LLDID (629-633) and has a terminal LLGLF (745-749), but has no LLNGF. Like other Dikarya
  beta1 subunits, it lacks the beta-appendage domain (the C-terminal 30 aa are a Pro/Gly-rich tail).
- At 749 aa, NCU09721 is a complete, full-length product: the trunk domain starts near residue 18 (PANTHER
  hit 18-604) and the length matches its Fusarium (747) and Aspergillus (766) orthologs. It is not a fragment.

## Interpretation

NCU09721 is the N. crassa AP-1 beta (Apl2 ortholog) and not the AP-2 beta, which is NCU05232. AP-1
functions shown for A. nidulans and F. graminearum AP-1 transfer within this ortholog group. AP-2-specific
functions such as plasma-membrane endocytosis do not.

Limitations: the tree is a distance tree with only 16 taxa. The deep beta1/beta2 split is not cleanly
resolved relative to metazoan beta1/2. Within the fungal AP-1 beta clade, placement is strongly supported.
