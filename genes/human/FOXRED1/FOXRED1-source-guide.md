# FOXRED1 source and evidence guide

FOXRED1 is supported as a mitochondrial complex I assembly factor. Its predicted oxidoreductase fold and similarity-based cofactor annotation motivate a biochemical hypothesis; the inspected evidence does not identify a FOXRED1 catalytic reaction or demonstrate FOXRED1-bound FAD.

## Original annotations and historical assertions

The active review retains all ten inherited GOA contexts: nine ACCEPT and one TOO_GENERAL. Two historical author-proposed molecular-function assertions are retired from the active annotation list. Their complete original objects, the prior review text and every inherited quotation remain in [the source-context archive](FOXRED1-source-contexts.json). No experimental annotation is removed. The original UniProt and GOA files remain unchanged.

The current official ten-row snapshot joins one-to-one to the inherited ten rows. The UniProt subcellular-location IEA date changed from 2026-07-06 to 2026-07-27; this is recorded without rewriting the inherited export. Three omitted donor-bearing support lists are restored from exact original provenance, including the legitimate FOXRED1 self-donor in both IBA records and the SL-0168 location mapping.

## Selected primary evidence

| Source | Access and precise locator | Supported conclusion and limit |
| --- | --- | --- |
| [PMID:20858599](https://pmc.ncbi.nlm.nih.gov/articles/PMC4560042/) | Original Results on complementation/silencing and subcellular/submitochondrial localization; Figures 5–7 captions and selected Discussion. Normal cache remains abstract-only. | Rescue and knockdown support complex I involvement. C-terminal fusion and fractionation support mitochondrial localization, including inner-membrane association and soluble signal. No figure pixels were read; tag placement and the precursor-processing interpretation remain distinct. |
| [PMID:25678554](https://pubmed.ncbi.nlm.nih.gov/25678554/) | Authentic abstract; full original publisher retrieval was unsuccessful. | Null-cell and complementation results plus co-immunoprecipitation support productive complex I assembly. The curated localization annotation is retained with independent localization corroboration. The abstract reports failure of a late ~815-kDa intermediate and breakdown to ~475 kDa; original full Methods remain inaccessible. |
| [PMID:27215383](https://pmc.ncbi.nlm.nih.gov/articles/PMC4968213/) | Original Methods on immunoprecipitation; Results and Figures 2–6 captions on rescue, depletion, complex profiles and SDHA flavination; Discussion. | Co-immunoprecipitation identifies AIFM1, ACAD9 and complex I subunits. The study models a ~370/315-to-550-kDa mid-assembly step. Its Discussion leaves intermediate-versus-breakdown identity and possible BN-PAGE calibration differences from 2015 unresolved. Myoblast complex II loss and rescue are contextual; no complex II partner or altered SDHA flavination was identified. The fluorescence assay measures SDHA-bound FAD, not FOXRED1-bound cofactor. No pixels or supplementary tables were inspected. |
| [PMID:25765152](https://pubmed.ncbi.nlm.nih.gov/25765152/) | Official identity and original publisher abstract/selected snippets; not full Methods. | Structural modeling suggests a pocket and potential oxygen-binding site. This is a mechanistic hypothesis, not an enzyme or binding measurement. |
| [PMID:40859035](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489013/) | FOXRED1-specific complexome Results around Figure 4 and Discussion of late complex I assembly. | RTN4IP1 perturbation alters FOXRED1 association with intermediates. Detergent-specific co-migration does not demonstrate binary contact or catalytic cooperation. No complete supplement or figure-pixel reading is claimed. |
| [PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) | Genuine full normal cache; exact FOXRED1 supplementary record remains unresolved. | Retain the curated mitochondrial HTP assignment with independent corroboration. Both inherited paper-title excerpts are archived as source identification, with reference-only support in the active review. A mismatched supplemental workbook and HTML challenges were rejected. |

The original papers' quotations are retained verbatim even when their historical specificity language is narrower than the later evidence. In particular, the 2010 complex-I-specific wording is scoped to that study; the 2016 myoblast phenotype prevents universal exclusivity. An assembly-only core is used because its biological process is established while the molecular activity remains unresolved. No complex II process assertion is newly proposed.

## Official identity, products and phylogeny

[UniProt Q96CU9](https://www.uniprot.org/uniprotkb/Q96CU9/entry) declares three natural products. Deriving the two alternative sequences from the exact VAR_SEQ features and comparing the authentic isoform-inclusive FASTA gives 486, 275 and 472 residues. This sequence check does not establish product-specific function or localization. Reported matrix-face association and predicted transmembrane topology remain incompletely reconciled.

The dated [PANTHER19 PTHR13847 family files](https://data.pantherdb.org/PANTHER19.0/books/PTHR13847/) contain 862 tree/MSA nodes. The human AN651/PTN002493132 sequence exactly matches the 486-residue displayed sequence. Incoming cytoplasm and complex I assembly IBA assertions map to the actual target path and literal IBD records at PTN000354057 and PTN001419340, respectively. Original donor sets, including target self evidence, are preserved; family-wide activities are not transferred automatically to FOXRED1.

## Source access and preservation

The [evidence map](FOXRED1-source-evidence.yaml) separates normal-cache availability from separately inspected original sections. Eighteen qualified normal sources comprise fifteen publication caches and three existing family files. Existing source bytes are immutable; newly fetched files retain the genuine fetcher's content and availability flags. Auxiliary sequence/database references in that source inventory do not imply additional gene-specific functional assays.

The inherited research-provider credential limitation remains unresolved. No provider retry or provider-named research output was used; the review relies on the documented manual primary and official-source checks.

## Evidence refinements after review

The broad cytoplasm annotation is TOO_GENERAL because the already retained inner-membrane localization entails it through the official typed path [GO:0005743](https://www.ebi.ac.uk/QuickGO/term/GO:0005743) is_a GO:0031966 part_of GO:0005739 part_of GO:0005737 (checked 2026-10-31). The four mitochondrion annotations remain ACCEPT, and all source fields and donor lists remain unchanged.

The UniProt FAD cofactor annotation with ECO:0000250 is a manual similarity inference, not an automatic label to dismiss. Pfam PF01266, InterPro IPR006076/IPR036188 and SUPFAM SSF51905 support a flavin/nicotinamide-binding oxidoreductase-like fold. Together with the structural model, these provide meaningful hypotheses. They do not distinguish a demonstrated FOXRED1-bound cofactor or substrate reaction from the inferred fold in the inspected evidence. The historical authored MF proposals remain archived; the assembly core remains without an assigned molecular activity, and no catalytic inactivity is asserted.

The dated family tree places GO:0008718 at AN299/PTN008552203, GO:0047865 at AN401/PTN002302648, GO:0008480 at AN446/PTN001014783 and GO:0004808 at AN245/PTN001015057. None lies on the verified FOXRED1 AN651/PTN002493132 ancestor path. This prevents transfer of those four particular activities through the tree; lack of a propagated MF is not evidence of a negative function or absent FAD binding.

Ten inherited quotation occurrences remain active and six are historical. The archived protein-name excerpt and both PMID:34800366 title occurrences retain their original reference and section associations in the complete original review and explicit occurrence ledger. They are no longer presented as active biological evidence. The historical GO_REF:0000043 metadata is retained to identify the provenance of the two retired authored assertions.

The [campaign quotation policy](https://github.com/ai4curation/ai-gene-review/blob/2d709bc35f6e447f56da0a528b8ef2173e1048f3/projects/CLINGEN_MENDELIAN.md#L2980-L2987) requires reference-only citations for newly used evidence. PMID:27215383 and PMID:40859035 therefore remain reference-only supports with the original URLs and selected Methods/Results/Discussion locators above. Normal-cache availability and separately read original sections remain distinct; this does not claim that unquoted evidence passed a verbatim-quotation check.
