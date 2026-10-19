# MITF (donkey, A0A9L0JBN5) - review notes

DONKEY40 cohort. 8 IEA GOA rows (TreeGrafter x4, InterPro2GO x2, subcellular-location mapping, combined).

## Sequence
- [file:EQUAS/MITF/MITF-bioinformatics/RESULTS.md "98.38% identity over 495 paired residues"]; bHLH ["54 of 54 human residues in this span are identical"]. Donkey residues 1-115 have no partner in human canonical O75030 (isoform/first-exon difference); human 138-162 and 293-298 absent in donkey model.

## Function (human UniProt O75030)
- [file:EQUAS/MITF/MITF-bioinformatics/human-O75030-uniprot.txt "Transcription factor that acts as a master regulator of melanocyte survival and differentiation as well as melanosome biogenesis"]
- ["Binds to M-boxes (5'-TCATGTG-3') and symmetrical DNA sequences (E-boxes) (5'-CACGTG-3') found in the promoter of pigmentation genes, such as tyrosinase (TYR)"]
- Localization regulated by mTORC1: ["Conversely, inhibition of mTORC1, starvation and lysosomal disruption, promotes dephosphorylation and translocation to the nucleus"]; [PMID:36608670 "The TFE3 and MITF master transcription factors maintain metabolic homeostasis by regulating lysosomal, melanocytic, and autophagy genes."]

## Decisions
- Accept DNA binding, RNAPII TF activity, nucleus, regulation of transcription by RNAPII, melanocyte differentiation. Cytoplasm and dimerization non-core. GO:0006355 too general.
- ProtNLM2 GO:0006355: correct but less precise than GOA GO:0006357 (LSP).
