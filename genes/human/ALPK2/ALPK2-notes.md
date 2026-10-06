# ALPK2 (Q86TB3) review notes

## 2026-10-04: PAINT/affinage review

**Affinage trust gate:** a blocking "symbol collision" gate fired because the narrative opens with zebrafish. I quarantined the output with --out and read it. It describes ALPK2 (hESC, zebrafish and mouse studies of the same gene), so I wrote it with --force and recorded this in reference_review.

The cardiogenesis role is contested across species:
- **hESCs and zebrafish:** [PMID:29888752 "Using antisense knockdown and CRISPR/Cas9 mutagenesis in hESCs and zebrafish, we demonstrate that ALPK2 promotes cardiac function and cardiomyocyte differentiation."]
- **Mouse knockouts:** [PMID:32383995 "We found that Alpk2-gKO mice exhibited normal cardiac function and morphology up to one year of age."]
- **UniProt** carries a CAUTION on the same point.

Decisions:
- **Kinase, Ser kinase and ATP binding (IEA): ACCEPT.**
- **All cardiac IMP and IEA rows: KEEP_AS_NON_CORE.** The curator's hESC evidence is not overruled, but the role is not established for the mammalian organism.
- **Colon 3D-culture rows** (apoptosis, gene expression; PMID:22641666) and **variant-study rows** (polarity, basolateral membrane; PMID:28668886): KEEP_AS_NON_CORE.
- **No NEW.** No GO row covers the TPM1/diastolic role, but it rests on a single mouse study.

## Round 1 (PR #3986 review)

- **TPM1 was understated as "indirect".** PMID:39556326 has four converging lines:
  - phosphoproteomics (15 ALPK2-dependent sites);
  - dose-dependent Ser283 phosphorylation by the catalytic domain in NIH3T3 cells;
  - loss of endogenous Ser283 phosphorylation in Alpk2-null cardiomyocytes;
  - gain with overexpression.
  The core MF is now GO:0106310 protein serine kinase activity. The caveat is that no purified-component assay exists.
- **GO:0010468** (siRNA lowering DNA repair mRNA in one cell line): MARK_AS_OVER_ANNOTATED.
- **Epicardium morphogenesis:** verified as a zebrafish tcf21:DsRed assay in the full text.


## Follow-up after merge (PR #3986 approving review)

Applied the reviewer's non-blocking items, two of which were factual errors:
- **Retained-row count:** the boundary said "11 retained process rows". Recounted from the file after this change: seven BP rows are KEEP_AS_NON_CORE.
- **Phosphosite count:** the question now says "14 other phosphosites" beyond TPM1.
- **Human constructs:** the TPM1 Ser283 reconstitution used human ALPK2 catalytic domain and human TPM1 (Methods), and the description now says so.
- **GO:0030010** now matches its reason: MARK_AS_OVER_ANNOTATED.
