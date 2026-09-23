# BIRC6 notes

## 2026-05-29 PROTEOSTASIS PN review pass

- The valid PN-derived candidate for BIRC6 is `GO:0061630 ubiquitin protein ligase activity`, from the `Ubiquitin Proteasome System > E3 ubiquitin and UBL ligases > E3 with intrinsic E2 > BIR repeat` node. This is a more specific child for the already reviewed broad `GO:0004842 ubiquitin-protein transferase activity` row, and is supported by the core BIRC6 E3 evidence. [PMID:15200957 "BRUCE has the distinctive property of functioning as a chimeric E2/E3 ubiquitin ligase with Smac being a substrate."; file:human/BIRC6/BIRC6-deep-research-falcon.md "BIRC6 (Q9NR09) is a giant dual-function E2/E3 ubiquitin enzyme"]
- The earlier PN ALP concern should not be read as evidence that BIRC6 is a lysosome-autophagosome SNARE or docking/fusion factor. The supported autophagy connection is LC3 engagement and LC3 K51 mono-ubiquitination, which suppresses autophagy and participates in apoptosis-autophagy crosstalk. [file:human/BIRC6/BIRC6-deep-research-falcon.md "BIRC6 mono-ubiquitinates LC3 at K51 in cooperation with UBA6, suppressing autophagy."]
- The `GO:0005634 nucleus` IBA row is not supported for human BIRC6. The GOA with/from column points to UBE2Z, while human BIRC6 localization evidence and UniProt support trans-Golgi network/endosome/cytosol and mitotic structures rather than nucleus. [file:human/BIRC6/BIRC6-goa.tsv "PANTHER:PTN000799330|UniProtKB:Q9H832"; file:human/BIRC6/BIRC6-uniprot.txt "In interphase cells, localizes to the trans-Golgi network membrane and endosomes."]


## 2026-09-20 IBA re-review

Restored nuclear localization as non-core using direct human nuclear fractionation and BRUCE-USP8-BRIT1 complex evidence. Withdrew phosphorylation-process removal pending the original full text; updated biological description.

Evidence inspected: [PMID:25733871](https://pubmed.ncbi.nlm.nih.gov/25733871/), [PMID:18329369](https://pubmed.ncbi.nlm.nih.gov/18329369/).

Remaining questions:

- Inspect PMID:18329369 full text for any direct BIRC6 contribution to phosphorylation; being phosphorylated is not participation.

The project audit records all changed row indices and decisions in `projects/IBA_REVIEW/rereview-2026-09-20/localization.yaml`.
