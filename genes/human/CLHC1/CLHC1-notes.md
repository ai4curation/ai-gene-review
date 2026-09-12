# CLHC1 review notes

## Review scope and evidence acquisition

- Review initiated 2026-07-18 for human CLHC1 (UniProtKB Q8NHS4; HGNC:26453).
- `just deep-research-falcon human CLHC1 --fallback perplexity-lite` was run as required. Falcon failed with HTTP 402 (payment required), and the perplexity-lite fallback failed with HTTP 401 (quota exhausted). Neither provider produced a research report. No provider-named deep-research file was created manually.
- `just fetch-gene-pmids human CLHC1` successfully checked the sole PMID referenced by GOA, PMID:25416956; its cached record has full text available.
- The shared cache also contains PMID:15489334, which UniProt cites for the two CLHC1 cDNA isoforms. It is abstract-only and describes the broad Mammalian Gene Collection rather than CLHC1 function. [PMID:15489334, "The status, quality, and expansion of the NIH full-length cDNA project: the Mammalian Gene Collection (MGC)."]
- The local UniProt record, all three GOA rows, both cached publications, PANTHER family data, and public database pages were inspected. The function-oriented literature search did not identify a CLHC1-specific mechanistic study.

## Identity, sequence, and domain architecture

CLHC1 encodes a reviewed 586-aa human protein, clathrin heavy chain linker domain-containing protein 1. UniProt records two splice isoforms; isoform 2 lacks residues 1-122 of the canonical sequence. [UniProtKB:Q8NHS4, "Reviewed;         586 AA."] [UniProtKB:Q8NHS4, "Named isoforms=2"] [UniProtKB:Q8NHS4, "VAR_SEQ         1..122"]

The protein has a predicted coiled-coil at residues 174-232 and database assignments to an ARM-type fold, clathrin heavy-chain linker domain, CLHC1 family, and TSNAXIP1_N domain. These are architectural/family assignments, not evidence that CLHC1 forms clathrin coats or participates in vesicle trafficking. [UniProtKB:Q8NHS4, "COILED          174..232"] [UniProtKB:Q8NHS4, "InterPro; IPR016024; ARM-type_fold."] [UniProtKB:Q8NHS4, "InterPro; IPR012331; Clathrin_H-chain_linker."] [UniProtKB:Q8NHS4, "InterPro; IPR032755; TSNAXIP1_N."]

The relevant PANTHER family is PTHR10292, but CLHC1 occupies the mammalian CLHC1-specific subfamily PTHR10292:SF11. The PAINT family file places functional annotations on other ancestral nodes, not on the CLHC1 subfamily, and UniProt explicitly reports zero PAN-GO annotations for Q8NHS4. This argues against transferring canonical clathrin heavy-chain functions merely from the broad family membership. [file:interpro/panther/PTHR10292/PTHR10292-entries.csv, "Q8NHS4,Clathrin heavy chain linker domain-containing protein 1,protein,9606,Homo sapiens,Homo sapiens (Human),CLHC1,586,PTHR10292:SF11"] [UniProtKB:Q8NHS4, "PAN-GO; Q8NHS4; 0 GO annotations based on evolutionary models."]

## Existing GO annotations and interaction evidence

GOA contains three IPI rows for GO:0005515 `protein binding`, all assigned by IntAct from PMID:25416956. The partners are LMO2 (P25791), SGF29 (Q96ES7), and CEP170P1 (Q96L14). [file:human/CLHC1/CLHC1-goa.tsv, "PMID:25416956\tUniProtKB:P25791"] [file:human/CLHC1/CLHC1-goa.tsv, "PMID:25416956\tUniProtKB:Q96ES7"] [file:human/CLHC1/CLHC1-goa.tsv, "PMID:25416956\tUniProtKB:Q96L14"]

UniProt independently exposes the same three binary-interaction records, each with `NbExp=3`. [UniProtKB:Q8NHS4, "Q8NHS4; Q96L14: CEP170P1; NbExp=3"] [UniProtKB:Q8NHS4, "Q8NHS4; P25791: LMO2; NbExp=3"] [UniProtKB:Q8NHS4, "Q8NHS4; Q96ES7: SGF29; NbExp=3"]

PMID:25416956 is a full-text, proteome-scale human binary-interactome study rather than a focused CLHC1 functional study. The extracted article body does not contain the strings CLHC1, C2orf63, or Q8NHS4; the gene-specific pairs are represented in the associated interaction dataset and propagated through IntAct/GOA/UniProt. [PMID:25416956, "A proteome-scale map of the human interactome network."] [PMID:25416956, "By systematically screening half of the interactome space with minimal inspection bias"]

Decision: retain the three partner-level interaction observations as useful evidence, but mark the consolidated generic `protein binding` annotation as `MARK_AS_OVER_ANNOTATED`. `Protein binding` does not describe a specific molecular activity, the three partners do not define a coherent known complex or binding class, and no more informative GO molecular-function replacement is currently justified.

## Expression and localization leads (not asserted as function)

Public Human Protein Atlas data report low tissue specificity, enrichment in early spermatids, and a single-cell expression cluster associated with ciliated cells. The same resource reports antibody-based localization to the centrosome and nucleolar fibrillar center. These observations motivate experiments, but expression correlation and unvalidated cell-atlas imaging do not establish a ciliary, centrosomal, nucleolar, or clathrin-trafficking function. [HPA:ENSG00000162994, "Cell type enriched (Testis - Early spermatids)"] [HPA:ENSG00000162994, "Ciliated cells - Cilia assembly & function (mainly)"] [HPA:ENSG00000162994, "Localized to the Nucleoli fibrillar center, Centrosome"]

NCBI Gene provides the standard identity and broad expression summary but no gene-specific functional summary. Mouse MGI likewise reports no experimental biological-process annotation. [NCBI-Gene:130162, "Broad expression in testis (RPKM 1.3), thyroid (RPKM 0.8) and 24 other tissues"] [MGI:1920574, "No experimental evidence to support Biological Process annotation"]

## Functional synthesis and limits

No direct biochemical activity, physiological process, stable native complex, or functionally relevant cellular location has been established for CLHC1. The current evidence supports only that it is an expressed, clathrin-heavy-chain-linker/ARM-fold protein with several high-throughput binary interactions. A core GO-CAM-like molecular-function unit therefore cannot yet be grounded without speculation.

The most useful next steps are endogenous localization with knockout-controlled reagents, interactome mapping in CLHC1-expressing ciliated/testis-derived contexts, and loss-of-function/rescue assays that directly test cilium/flagellum phenotypes. The two splice isoforms should be compared because isoform 2 lacks the N-terminal 122 residues, overlapping much of the TSNAXIP1_N domain assignment.
