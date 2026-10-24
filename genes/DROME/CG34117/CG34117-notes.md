# CG34117 (Q0KI97) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file was opened or used in this re-review.

### Identity
- Q0KI97 is the only polypeptide of CG34117 (FBgn0083953). FlyBase reports one transcript and one
  unique polypeptide. The sequence is 101 aa, sequence version 1, UniProt TrEMBL, PE 3.
- It is not a fragment, isoform or alternative gene model. It aligns collinearly over its whole length
  with human FMC1 (Q96HJ9, 113 aa), at 40.6% identity over 101 positions, and carries the conserved
  C-terminal block (HGxGERSV...LVGxKLP). See `CG34117-bioinformatics/RESULTS-rereview.md`.

### Evolutionary grounding (the main correction)
- CG34117 and human FMC1 are both in PANTHER PTHR31716:SF1. The PAINT node is PTN001271866.
- Yeast Fmc1 (P40491) is in PANTHER **PTHR28015**, a different family. Human FMC1 was characterized
  in [PMID:28719601 "these short human and yeast proteins have no sequence homology detectable via BLASTP"].
  The animal and yeast proteins share only the Pfam Complex1_LYR_2 assignment.
- The previous version of this review used yeast Fmc1 as its main support. The re-review rebuilds the
  support on human FMC1:
  - mitochondrion: [PMID:28719601 "First, we confirmed mitochondrial localization (Fig 6A) by immunostaining with antibodies to endogenous C7orf55"]
  - complex V assembly by knockout and rescue: [PMID:28719601 "in the absence of C7orf55 we observed a specific destabilization of the mitochondrial complex V using three assays"]
  - binding to ATPAF2: [PMID:28719601 "In two replicates, we observed only a single high-abundance endogenous binding partner: ATPAF2"]

### Annotation decisions
- GO:0003674 ND: ACCEPT. There is no informative MF, and ATPAF2 binding would map only to bare
  protein binding.
- GO:0005739 IBA: ACCEPT. The donor is in-subfamily, with IDA evidence.
- GO:0005759 ISS (with P40491): changed from ACCEPT to **UNDECIDED**. The donor is from another
  family. Matrix localization is plausible because FMC1 binds ATPAF2, which works on the matrix side,
  but no PTHR31716 member has been placed in the matrix. A WRONG_WITH_FROM source defect (CHECK)
  was recorded for FlyBase.
- GO:0033615 IBA and ISS (both with Q96HJ9): ACCEPT. These form the core function.
- No NEW terms were added.

### Family review and modules
- `interpro/panther/PTHR31716/PTHR31716-review.yaml` describes the family mainly through yeast Fmc1
  (PMID:11096112). That conflicts with PANTHER placing yeast Fmc1 in PTHR28015, and the review does
  not cite the human FMC1 experimental paper (PMID:28719601). There is no disagreement about subfamily
  placement: CG34117 is in SF1, as is human FMC1.
- Module: `modules/dmel_respiratory_complex_assembly_factors.yaml` (part `complex_v_assembly_cg34117`).

### Relative to review next
- Human FMC1 (Q96HJ9) is the in-subfamily ortholog and is experimentally characterized. The repo has
  no `genes/human/FMC1` review.
