# GALNT3 source guide

GALNT3 is a Golgi membrane enzyme that transfers GalNAc from UDP-GalNAc onto protein serine/threonine residues. Human enzyme and cell experiments support this catalytic core and its role in O-GalNAc glycosylation. FGF23 is an important substrate, but the enzyme also acts on mucin-sequence acceptors. The core therefore describes the chemistry without restricting every GALNT3 activity to FGF23.

## Human experiments and engineered constructs

The [1996 cloning/expression study](https://doi.org/10.1074/jbc.271.29.17006) tested a human GALNT3 construct lacking its membrane anchor, expressed in Sf9 cells. Selected original Methods, Results and Table I were read through the retained author-indexed original. The assay used culture supernatants and radiolabeled UDP-GalNAc incorporation into synthetic Muc2, Muc5c and HIV-V3 acceptors with controls. It supports enzyme activity, not physiological HIV infection or activity of a naturally short splice product.

The [1997 purified-enzyme study](https://doi.org/10.1074/jbc.272.38.23503) characterized soluble human GALNT1/2/3 produced in insect cells. Selected original Methods and Results were read through the author-indexed original; source figure images were not independently inspected. Its manganese-replacement experiment used 5, 10 or 20 mM calcium or magnesium with Muc2 substrate and reported no detectable activity with either substitute. This supports manganese-dependent catalysis. It does not demonstrate that calcium cannot bind, so the calcium-binding annotation remains UNDECIDED. Manganese binding is retained as a cofactor property within the catalytic mechanism, not as a second core function.

The [2006 FGF23 study](https://pubmed.ncbi.nlm.nih.gov/16638743/) is available as an authentic abstract and selected indexed original human transfection/peptide sections; complete original figure inspection was not achieved. Its title's secretion wording is interpreted with the later mechanistic study. The [2007 HHS study](https://doi.org/10.1359/jbmr.061105) was read at abstract level and in selected author-uploaded original Methods/Results and captions: human HOS-TE85 cells, GALNT3 siRNAs and FGF23 constructs connect GALNT3 depletion to altered FGF23 processing. CHO-produced substrate preparations and human-cell silencing are distinct experimental systems. No source images or raw MS measurements were independently reanalyzed.

The [2020 mechanistic study](https://pubmed.ncbi.nlm.nih.gov/31932717/) has complete native cached text. Selected Methods, Results and discussion support human enzyme assays, CHO-cell experiments, AFM/SAXS and cooperation between catalytic and lectin domains. The complex crystal structures instead use **zebra finch** GALNT3; the human crystallization attempts failed. The human 92–633 and finch 91–631 soluble proteins are engineered constructs. They are not the natural short human product. The short pulse-labeling experiment did not show a marked increase in FGF23 secretion, and the later excess of intact extracellular hormone was attributed mainly to stability after secretion. This distinction replaces the inherited unconditional secretion-rate interpretation.

## Location and extracellular-vesicle evidence

The [human HeLa localization study](https://doi.org/10.1242/jcs.111.1.45) is currently accessible here as an authentic complete abstract, not full original Methods/images. It explicitly reports endogenous and tagged human GALNT1/2/3 localization by fractionation, immunofluorescence and immunoelectron microscopy. GALNT3 occurs in Golgi stacks, preferentially in their medial portion. This supports the Golgi/cisterna location without exclusivity. The current [HPA GALNT3 page](https://www.proteinatlas.org/ENSG00000115339-GALNT3/subcellular) lists supported Golgi apparatus localization; individual images were not independently scored.

The [ocular epithelial study](https://doi.org/10.1167/iovs.02-0181) remains abstract-only after restricted publisher and author-access attempts. GALNT3 epithelial distribution is explicit, but the abstract's supranuclear statement concerns GALNT2. The specific GALNT3 perinuclear panel remains unresolved. This does not establish a curator paralog error. Independent human data establish the general Golgi location, while the source-specific perinuclear claim remains UNDECIDED.

For [PMID:18570454](https://doi.org/10.1021/pr800225z), the normal repository cache is abstract-only, but an authentic [author-hosted original PDF](https://chem.yonsei.ac.kr/~mhmoon/pdf/Papers/81_JPR_exosome.pdf) was already retained. Methods/Results were read and Table 2 on printed page 3478 was visually inspected. The portable target-row facts are:

| Table locator | Historical identifier | Reported matched peptides | Fraction |
|---|---|---:|---:|
| Table 2, UDP-GalNAc:polypeptide N-acetylgalactosaminyltransferase entry | GI1617312 | 1 | 3 |

The official [NCBI protein record CAA63371.1](https://www.ncbi.nlm.nih.gov/protein/CAA63371.1) resolves the historical identifier to human GALNT3/Q14435. The original PDF is 1,005,190 bytes, SHA256 `7d3b945b98a6696ca6146956da71378304b2de9f40867ee86729248a395372fc`. The study uses HB1.F3 conditioned medium, flow field-flow fractionation, electron microscopy and LC-MS/MS. It permits a limited non-core vesicle-fraction association, preserving the neural-stem-cell extension. A single matched peptide and fractionation do not independently establish fraction purity, membrane orientation, active extracellular catalysis or exosome biogenesis. The attempted supplementary URL returned challenge HTML and is excluded from evidence.

## Reactome target chains

The immutable repository summaries were retained. Successful official [ContentService](https://reactome.org/ContentService/) records were read privately to resolve the direct event/catalyst/member chains; no primary-paper assay is inferred merely from the model.

| Source record | Verified GALNT3 chain and scope |
|---|---|
| [8851619](https://reactome.org/content/detail/R-HSA-8851619) | Catalyst 8851625 → entity 913620 → human Q14435, at Golgi membrane; UDP-GalNAc-dependent FGF23 modification. The substrate and enzyme compartments are distinguished. |
| [913675](https://reactome.org/content/detail/R-HSA-913675) | Catalyst 913697 → set 913644 → GALNT3 913620 as an explicit `hasMember`, supporting the normal mucin GalNAc-transfer reaction without identical specificity across all GALNTs. |
| [913709](https://reactome.org/content/detail/R-HSA-913709) | Mucin O-glycosylation pathway directly includes normal reaction 913675. |
| [5096537](https://reactome.org/content/detail/R-HSA-5096537) | FailedReaction with GALNT3 C574G, Q592*, R162* and T272K variants; `normalReaction` is 913675. Mutant catalytic failure is not positive wild-type activity evidence. |
| [5083625](https://reactome.org/content/detail/R-HSA-5083625) | Disease pathway contains failed reaction 5096537. The successful external official record was read; its native disease-pathway summary is now also cached. |
| [190372](https://reactome.org/content/detail/R-HSA-190372) | Includes upstream GALNT3/FGF23 glycosylation 8851619 before secretion, receptor binding and receptor phosphorylation. Target membership is genuine. |

The last pathway membership does not establish execution of the receptor-triggered molecular signals defined by GO:0008543. GALNT3's upstream chemistry and regulatory relevance are preserved while the signaling annotation is marked over-annotated. No replacement or NEW process assertion is added.

## Products, phylogeny and term precision

The official [Q14435 record](https://www.uniprot.org/uniprotkb/Q14435/entry), direct product FASTAs and variation reconstruction agree on the 633-residue canonical and 192-residue short products. The short product changes canonical residues 173–192 and lacks 193–633, removing most of the catalytic region and the lectin domain. Its function is unresolved. Predicted topology and zebra-finch-derived human site features are identified by their actual evidence classes rather than called direct human structural observations.

Actual PTHR11675 tree, alignment and IBD records place human GALNT3 at AN993/PTN002481705, with exact canonical sequence identity. The two catalytic/process assertions originate at AN1/PTN004287905; the Golgi assertion originates at AN11/PTN000187024. All are on the target lineage, with no target-path negative placement. Incoming and literal retained IBD donor sets agree. Target self-evidence is valid descendant grounding. No family label or node was inferred from donor counts.

The six refinements use verified relationships: GO:0016266 `is_a` GO:0006493 (four process contexts); GO:0000139 `is_a` GO:0098588 `is_a` GO:0031090 `is_a` GO:0016020 (membrane); and GO:0005794 `part_of` GO:0005737 (cytoplasm). Cytoplasm includes organelles and is not cytosol. The informative Golgi organelle annotations remain ACCEPT. The Golgi cisterna claim is independently supported; the retained query did not establish a typed GO:0032580 → GO:0000139 path, and no such path is invented.

## Access, quotation and preservation scope

There are 35 current contexts, two products, one catalytic core and 22 manually assessed references. No NEW annotation is proposed. The action tally is 24 ACCEPT, 6 MODIFY, 2 KEEP_AS_NON_CORE, 2 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED. All raw provenance and the two FGF23-input atoms plus one neural-stem-cell atom remain explicit. The actual native parser omits these atoms; the review restores the literal two has_input atoms and one part_of atom without adding a scientific assertion.

The 24 normal sources include unused UniProt bibliography entries without implying that every paper was manually read. Native acquisition reused all 19 existing sources and fetched only three missing publications, one Reactome summary and the single-family PAINT slice from retained upstream data. All 35 exporter/parser contexts, both products, 15 assessed source titles and six exact excerpt byte ranges reconciled. Individual scientific reading limits remain unchanged. Target validation and strict GOA matching pass; the computed status is DRAFT with two UNDECIDED judgments. One advisory retains the unused historical falcon artifact. Native history validation and private rendering pass.

The [compact source evidence](GALNT3-source-evidence.yaml) preserves all current raw fields, literal atoms and product sequences, with immutable Git locators for the whole old 35-row review, all 48 original quotation occurrences, complete old notes and prior provider/history artifacts. Expanded private originals remain intact; a duplicate full old-review JSON is not republished. Twenty-two snippets match the old source literally and twenty-six differ only in whitespace. The initial four unmatched results were a file-reference routing diagnostic: all four were found exactly in the immutable UniProt record after the source route was corrected. That initial diagnostic remains retained. No old quote is silently repaired or presented as newly read evidence.

Six short current excerpts appear only in the review/core. Repeated occurrences are counted per source: 10 words for PMID:9295285, 18 for PMID:31932717, 8 for PMID:17129170, 10 for PMID:8663203 and 11 for PMID:9394011. The ledger contains offsets, hashes and locations without duplicating text. Current source-specific reference notes distinguish native cache availability from successful external selected reading. Notes and this guide paraphrase the biology rather than repeat the quotations.
