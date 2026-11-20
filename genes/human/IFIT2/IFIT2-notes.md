# IFIT2 notes

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

- Rows: GO:0005783 IEA (GO_REF:0000044) and IDA (PMID:21190939), both KEEP_AS_NON_CORE; no ER sub-compartment row.
- The IEA maps UniProt's curated location [file:human/IFIT2/IFIT2-uniprot.txt "Endoplasmic reticulum {ECO:0000269|PubMed:21190939}"], so both rows rest on one paper.
- PMID:21190939: the cached file (and PMC3044982 via the PubMed MCP and NCBI efetch) lacks the results, so the localization assay (marker, tagged vs endogenous) could not be checked. The discussion places the function in the cytoplasm/mitochondria [PMID:21190939 "ISG54 triggers cell death via a mitochondrial response that appears to initiate in the cytoplasm."].
- IFIT2 is a soluble TPR protein with no signal peptide or TM segment: any ER pool is a cytosolic-face association, stays at root.
- Outcome: root; both rows KEEP_AS_NON_CORE (curator deferred to); MARK_AS_OVER_ANNOTATED would be the alternative if the ER pattern proves to be an overexpression artefact.
