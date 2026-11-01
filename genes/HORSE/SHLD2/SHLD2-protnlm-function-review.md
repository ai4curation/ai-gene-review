# SHLD2 ProtNLM function-description review

Target: horse A0A9L0RGD6. Source: frozen ProtNLM2 API snapshot2026-09-08, exact output in `projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv`. This is an external prediction, separate from GOA.

## Original prediction

> Component of the shieldin complex, which plays an important role in repair of DNA double-stranded breaks (DSBs). During G1 and S phase of the cell cycle, the complex functions downstream of TP53BP1 to promote non-homologous end joining (NHEJ) and suppress DNA end resection. Mediates various NHEJ-dependent processes including immunoglobulin class-switch recombination, and fusion of unprotected telomeres

## Claim assessment

| Claim | Assessment | Evidence and limitation |
|---|---|---|
| Shieldin-complex component | COR | The sequence is a close SHLD2-family match, including the long-form insertion; this supports family/complex identity. Complex recruitment alone does not demonstrate an intact DNA-binding module. |
| Downstream of TP53BP1 in DNA-break repair | UNC for the exact horse model | Human primary studies place shieldin downstream of 53BP1. The selected horse C-terminal OB region is divergent/gapped; biological family membership and functional repair are distinct claims. |
| Promotes NHEJ and suppresses end resection | UNC for the exact horse model | GOA carries positive regulation of NHEJ and negative regulation of HR for the gene, on the canonical product A0A9L0TUF0, so these claims are not novel. For A0A9L0RGD6 they are unresolved: it keeps OB folds A and B and the OB-fold-C zinc ribbon, but its conservation ends after horse residue ~811, losing the rest of OB fold C and the distal half of the SHLD1-interacting region. The human short splice product can assemble/localize yet fail to suppress homologous recombination, and no experiment has tested this truncation. |
| G1/S-phase activity | UNC | The human pathway provides a cell-cycle context, but the specified timing and repair competence have not been resolved for this horse model. |
| Immunoglobulin class switching | UNC | A demonstrated mammalian shieldin-dependent NHEJ outcome requires a functioning end-protection module; that transfer remains uncertain. |
| Fusion of unprotected telomeres | UNC | The mammalian pathway result is plausible at gene-family level but remains conditional on the exact horse protein's repair function. |

The principal sources are [Noordermeer et al., PMID:30022168](https://pubmed.ncbi.nlm.nih.gov/30022168/), DOI [10.1038/s41586-018-0340-7](https://doi.org/10.1038/s41586-018-0340-7), and [Dev et al., PMID:29789392](https://pubmed.ncbi.nlm.nih.gov/29789392/). See [sequence and isoform analysis](SHLD2-bioinformatics/RESULTS.md) and [review notes](SHLD2-notes.md). Neither the human AI review text nor ARBA agreement supplies independent validation.

A0A9L0RGD6 is a non-canonical alternative Ensembl model of horse SHLD2; the gene's GOA rows sit on the canonical product A0A9L0TUF0 ([gene-model comparison](SHLD2-bioinformatics/RESULTS-rereview.md)). COR for shieldin-complex membership means that the claim is biologically supported for this product, which keeps the N-terminal SHLD3-MAD2L2 recruitment segment, and that no product of the horse gene carries a shieldin-complex GO term in GOA or among the GO terms of the curated reviews, although the curated review describes shieldin scaffold membership in its prose. It is not proof of absence from training data. The paragraph is retained separately because the PredictionReview schema currently represents GO/EC terms rather than narrative claims.
