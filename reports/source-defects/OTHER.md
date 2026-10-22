# Source-record defects for OTHER

3 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR047151
- **Subject:** UniProtKB:Q9BQ52
- **Field:** metadata.literature.PUB00102035.PMID
- **Change:** check PMID:2159360 (alternatives in the explanation)
- **Recorded in:** `genes/human/ELAC2/ELAC2-ai-review.yaml`

InterPro IPR047151 uses description citation PUB00102035 for mitochondrial tRNA processing, but that literal literature entry identifies PMID:2159360 and a cerebral-blood-flow/NMDA-receptor study unrelated to ELAC2 or tRNase Z. Check the intended citation in the InterPro record; no replacement identifier is established here. The target family match and GO:0042781 mapping agree with independent human enzymatic evidence and are retained.

## 2. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9Y6C2 part_of GO:0034668 integrin alpha4-beta1 complex (IMP, PMID:18463100)
- **Field:** GO_ID
- **Change:** check GO:0034668 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EMILIN1/EMILIN1-ai-review.yaml`

Assigned-by resource: CAFA. QuickGO record UniProtKB:Q9Y6C2!118992744 assigns human EMILIN1 part_of the integrin alpha4-beta1 complex by IMP from PMID18463100. The current term denotes the alpha4/beta1 receptor heterodimer. The operative original characterizes human EMILIN1 gC1q as an extracellular ligand whose mutants affect receptor-dependent adhesion; it does not identify EMILIN1 as either receptor subunit. Please reconcile the complex-membership record with the supported ligand interaction, retaining the independent binding/adhesion annotations rather than treating them as absent.

- **Evidence reference:** PMID:18463100

- **Evidence reference:** file:human/EMILIN1/EMILIN1-source-guide.md

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9Y6C2 involved_in GO:0045766 positive regulation of angiogenesis (IEA, GO_REF:0000107)
- **Field:** GO_ID
- **Change:** check GO:0045766 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EMILIN1/EMILIN1-ai-review.yaml`

Assigned-by resource: Ensembl. QuickGO record UniProtKB:Q9Y6C2!118992709 transfers positive regulation of angiogenesis from Q99K41/ENSMUSP00000031055. The current donor has opposite signed annotations from PMID25056700, including BHF-UCL IMP negative and ComplexPortal IDA positive records. The actual knockout phenotype is increased angiogenesis after Emilin1 loss. Please reconcile the source sign and orthology transfer with the contextual negative-regulation interpretation; no defect in orthology or universal antiangiogenic claim is inferred.

- **Evidence reference:** PMID:25056700

- **Evidence reference:** file:human/EMILIN1/EMILIN1-source-guide.md
