# FOXRED1 source and evidence guide

FOXRED1 is supported as a mitochondrial complex I assembly factor. Its predicted oxidoreductase fold and similarity-based cofactor annotation motivate a biochemical hypothesis; the inspected evidence does not identify a FOXRED1 catalytic reaction or demonstrate FOXRED1-bound FAD.

## Original annotations and historical assertions

The active review retains all ten inherited GOA contexts: nine ACCEPT and one KEEP_AS_NON_CORE. Two historical author-proposed molecular-function assertions are retired from the active annotation list. Their complete original objects, the prior review text and every inherited quotation remain in [the source-context archive](FOXRED1-source-contexts.json). No experimental annotation is removed. The original UniProt and GOA files remain unchanged.

The current official ten-row snapshot joins one-to-one to the inherited ten rows. The UniProt subcellular-location IEA date changed from 2026-07-06 to 2026-07-27; this is recorded without rewriting the inherited export. Three omitted donor-bearing support lists are restored from exact original provenance, including the legitimate FOXRED1 self-donor in both IBA records and the SL-0168 location mapping.

## Selected primary evidence

| Source | Access and precise locator | Supported conclusion and limit |
| --- | --- | --- |
| [PMID:20858599](https://pmc.ncbi.nlm.nih.gov/articles/PMC4560042/) | Original Results on complementation/silencing and subcellular/submitochondrial localization; Figures 5–7 captions and selected Discussion. Normal cache remains abstract-only. | Rescue and knockdown support complex I involvement. C-terminal fusion and fractionation support mitochondrial localization, including inner-membrane association and soluble signal. No figure pixels were read; tag placement and the precursor-processing interpretation remain distinct. |
| [PMID:25678554](https://pubmed.ncbi.nlm.nih.gov/25678554/) | Authentic abstract; full original publisher retrieval was unsuccessful. | Null-cell and complementation results plus co-immunoprecipitation support productive complex I assembly. The curated localization annotation is retained with independent localization corroboration. Approximate intermediate masses and stage assignments are source-specific. |
| [PMID:27215383](https://pmc.ncbi.nlm.nih.gov/articles/PMC4968213/) | Original Methods on immunoprecipitation; Results and Figures 2–6 captions on rescue, depletion, complex profiles and SDHA flavination; Discussion. | Complex I partners/intermediates provide physical assembly evidence. Myoblast complex II loss and rescue are contextual; no complex II partner or altered SDHA flavination was identified. The fluorescence assay measures SDHA-bound FAD, not FOXRED1-bound cofactor. No pixels or supplementary tables were inspected. |
| [PMID:25765152](https://pubmed.ncbi.nlm.nih.gov/25765152/) | Official identity and original publisher abstract/selected snippets; not full Methods. | Structural modeling suggests a pocket and potential oxygen-binding site. This is a mechanistic hypothesis, not an enzyme or binding measurement. |
| [PMID:40859035](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489013/) | FOXRED1-specific complexome Results around Figure 4 and Discussion of late complex I assembly. | RTN4IP1 perturbation alters FOXRED1 association with intermediates. Detergent-specific co-migration does not demonstrate binary contact or catalytic cooperation. No complete supplement or figure-pixel reading is claimed. |
| [PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) | Genuine full normal cache; exact FOXRED1 supplementary record remains unresolved. | Retain the curated mitochondrial HTP assignment with independent corroboration. The inherited paper-title excerpt identifies the source but does not prove the gene-level result. A mismatched supplemental workbook and HTML challenges were rejected. |

The original papers' quotations are retained verbatim even when their historical specificity language is narrower than the later evidence. In particular, the 2010 complex-I-specific wording is scoped to that study; the 2016 myoblast phenotype prevents universal exclusivity. An assembly-only core is used because its biological process is established while the molecular activity remains unresolved. No complex II process assertion is newly proposed.

## Official identity, products and phylogeny

[UniProt Q96CU9](https://www.uniprot.org/uniprotkb/Q96CU9/entry) declares three natural products. Deriving the two alternative sequences from the exact VAR_SEQ features and comparing the authentic isoform-inclusive FASTA gives 486, 275 and 472 residues. This sequence check does not establish product-specific function or localization. Reported matrix-face association and predicted transmembrane topology remain incompletely reconciled.

The dated [PANTHER19 PTHR13847 family files](https://data.pantherdb.org/PANTHER19.0/books/PTHR13847/) contain 862 tree/MSA nodes. The human AN651/PTN002493132 sequence exactly matches the 486-residue displayed sequence. Incoming cytoplasm and complex I assembly IBA assertions map to the actual target path and literal IBD records at PTN000354057 and PTN001419340, respectively. Original donor sets, including target self evidence, are preserved; family-wide activities are not transferred automatically to FOXRED1.

## Source access and preservation

The [evidence map](FOXRED1-source-evidence.yaml) separates normal-cache availability from separately inspected original sections. Eighteen qualified normal sources comprise fifteen publication caches and three existing family files. Existing source bytes are immutable; newly fetched files retain the genuine fetcher's content and availability flags. Auxiliary sequence/database references in that source inventory do not imply additional gene-specific functional assays.

The inherited research-provider credential limitation remains unresolved. No provider retry or provider-named research output was used; the review relies on the documented manual primary and official-source checks.
