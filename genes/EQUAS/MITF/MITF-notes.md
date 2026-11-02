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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used in this re-review.

### Deep research
- `just deep-research-falcon EQUAS MITF --fallback perplexity-lite` failed: falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient_quota. No deep-research file was produced. Literature was read directly from cached publications instead (PMID:9647758, PMID:23401004, PMID:16822840, PMID:36608670 and the human UniProt record O75030).

### Identity of the benchmark accession (alternative gene model)
- [file:EQUAS/MITF/MITF-bioinformatics/RESULTS-rereview.md "human isoform A1 residues 1-20 (MQSESGIVPDFEVGEEFHEE) found in donkey at 1-based position: 116"]. From residue 116 onwards the model is an isoform A-type product.
- Residues 1-115 make up an Arg/Pro/Gly/Ser-rich extension ("R+P+G+S fraction: 0.55") with no counterpart among the 12 human isoforms in O75030. It is probably translated 5' UTR from an upstream in-frame start, i.e. a gene-model artefact, but that has not been shown.
- It lacks the X1-type ACIFPT insert (so it is X2/A2-like) and a 25-residue segment matching human A1 138-162 (QVKQYLSTTLANKHANQVLSLPCPN).
- Donkey has 5 TrEMBL MITF models (A0A8C4PGB1 641 aa, A0A9L0IUI7 504, A0A9L0JHX8 419 = M-length, A0A9L0KEI8 519, A0A9L0JBN5 610), all from Ensembl gene ENSEASG00005002172.2. None is reviewed, so there is no canonical Swiss-Prot product of the same gene to review. bHLH-Zip and C-terminal regions are intact (RESULTS.md, bHLH 54/54 identical).

### Evolutionary grounding
- UniProt places this model in PANTHER PTHR45776:SF4 (MICROPHTHALMIA-ASSOCIATED TRANSCRIPTION FACTOR), the same subfamily as human O75030, mouse Q08874 and rat O88368 (interpro/panther/PTHR45776/PTHR45776-entries.csv). The task header said no PANTHER id was listed, but the UniProt record does list one.
- PAINT (interpro/panther/PTHR45776/PTHR45776-paint.tsv): GO:0000978, GO:0000981, GO:0006357 and GO:0005634 are IBDs at the MiT/TFE root PTN005248237. GO:0030318 melanocyte differentiation is an IBD on the MITF lineage only: PTN000000820 (Tetrapoda, seed MGI:104554 Mitf) and PTN000000863 (teleost mitfa/mitfb). That makes it subfamily-specific, and SF4 membership justifies transferring it. TreeGrafter transferred all four GOA TreeGrafter rows from PTN000000842.
- There is no disagreement between this placement and the PANTHER family files. No family review YAML exists for PTHR45776 (only entries/metadata/paint files).

### Decisions (changes from the previous review)
- GO:0006357: ACCEPT -> MODIFY to GO:0045944 positive regulation of transcription by RNA polymerase II. The term is correct but general; MITF-A activates TYR/TYRP1 [PMID:9647758 "transient cotransfection assays suggested that MITF-A activated transcription of the tyrosinase and tyrosinase-related protein 1 genes"].
- GO:0006355: TOO_GENERAL -> MODIFY to GO:0045944, for the same reason.
- core_functions: directly_involved_in now uses GO:0045944 in place of GO:0006357.
- Unchanged: GO:0000978, GO:0000981, GO:0005634 and GO:0030318 ACCEPT; GO:0005737 and GO:0046983 KEEP_AS_NON_CORE. Support was strengthened with PAINT node rows and with Rag/14-3-3 localization papers [PMID:23401004 "expression of inactive Rags caused accumulation of MITF-1 into the nucleus"].
- Lysosome localization (Rag recruitment) was not proposed as NEW, because it is a regulatory sequestration site and not a site of function.

### Relative
- Human MITF O75030 is an ortholog in the same PANTHER subfamily SF4 (PAINT seed for the root IBDs). There is no genes/human/MITF review, so it needs review. The only existing MITF-family reviews are zebrafish mitfa/mitfb (genes/DANRE/).
- Modules: none found in modules/ that model MITF. It is mentioned only in prose in diadenosine_tetraphosphate_turnover.yaml and in kit_signaling deep research.
