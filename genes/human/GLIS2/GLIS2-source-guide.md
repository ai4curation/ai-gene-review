# GLIS2 source and product guide

This guide records evidence boundaries for the accompanying review. Incoming annotations and their literal contexts are preserved in [GLIS2-evidence.json](GLIS2-evidence.json).

## Products and source scope

The official human product is Q9BZE0, 524 residues; the mouse donor is Q8VDL9, 521 residues. No alternative human product is declared in the inspected record. Host-cell identity is kept separate from construct origin. No historical fragment is assigned a modern splice-isoform identifier.

## Mouse localization and construct boundaries

The 2002 original Methods identify a mouse kidney clone. Its EGFP localization and deletion-reporter experiments were inspected separately. Full-length Gal4-Glis2 inactivity in that assay does not turn deletion-dependent activation into full-length activity. Nuclear puncta do not, by themselves, identify a marker-defined splicing-factor compartment. [PMID:11741991](https://pubmed.ncbi.nlm.nih.gov/11741991/)

## Promoter-specific functional source

Abstract only.

Source: [PMID:21127075](https://pubmed.ncbi.nlm.nih.gov/21127075/). The exact abstract excerpts are in the core function; they are not repeated here.

## Corepressor and cytoplasmic context

The original CtBP1/HDAC3 work supports a repression mechanism. Its localization Results explicitly include tagged Glis2 in a mixed nuclear/cytoplasmic subset of CHO cells. This is positive contextual evidence, not proof of constitutive endogenous human cytoplasmic residence. [PMID:16326862](https://pmc.ncbi.nlm.nih.gov/articles/PMC1301595/)

## Beta-catenin recognition

Original co-precipitation, two-hybrid and pull-down experiments support the specific binding refinement. Historical 520/522-residue construct references remain separate from the current 524-residue human sequence. The supplement was not recovered, and human host cells do not settle tagged-construct species. [PMID:17289029](https://pmc.ncbi.nlm.nih.gov/articles/PMC1838965/)

## Ciliary localization

The institutional original Figure 2, Results and Methods document axonemal immunostaining in MDCK-II cells and a GFP/P100 experiment in HEK293T cells. These observations support contextual localization. They do not determine a ciliary molecular activity or establish every construct as human. The accessible PDF text was read; no microscopic pixel analysis is claimed. [PMID:17618285 original](https://www.mdc-berlin.de/system/files/migrated_files/fiona/Attanasio_NatGen_2007.pdf)

## Methyl-SELEX uncertainty

The original methods cover recombinant transcription-factor preparations and methylated/unmethylated DNA selections. The exact GLIS2 entry in supplemental tables S1–S6 was not recovered. Construct length, expression host and methylation preference therefore remain unassigned for this row. UNDECIDED preserves the curator assertion while making the access boundary explicit. [PMID:28473536](https://pmc.ncbi.nlm.nih.gov/articles/PMC8009048/)

## HuRI physical evidence

HuRI tests human ORFs in yeast using complementary two-hybrid configurations. Its pairwise retesting supports physical contacts. Current IntAct records contain all 39 literal partners, including the annotated isoforms. Historical downloadable records retain several different accession labels and omit two current pairs; those differences are preserved without declaring clone equivalence. The contacts remain evidence, but these assays do not assign a particular physiological molecular role to GLIS2. Removing the generic GO label therefore does not reject the reported binding.

Sources: [PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) and [IntAct GLIS2 / publication query](https://www.ebi.ac.uk/intact/ws/psicquic/intact/webservices/current/search/query/identifier:Q9BZE0%20AND%20pubid:32296183?format=tab27). Literal partner and assay records are summarized in [GLIS2-evidence.json](GLIS2-evidence.json); they are data, not additional functional assignments.

## Historical PAINT placement

The incoming ancestral assertions resolve in PANTHER19 PTHR19818, whereas current UniProt reports PTHR45718:SF8. The actual historical tree contains 712 nodes and 413 leaves across 8,709 alignment columns. Human Q9BZE0 is AN233/PTN002500402, with its ungapped 524-residue sequence identical to the official product. Three rows descend from AN0/PTN001803442 and two from AN224/PTN008571319. Each literal donor set matches its IBD assertion; all donors resolve inside the appropriate clade, and the three recorded loss annotations are outside the target path. No GLI3-tree proof or guessed family file is substituted. These checks support inheritance, together with the primary donor evidence; donor count is not a quality score.

The exact source URLs and hashes for the historical tree, alignment and attributes are in [GLIS2-evidence.json](GLIS2-evidence.json). The current family designation is preserved literally.

## Additional reference boundaries

The remaining references retain their individual access and relevance judgments in the review. Sequence catalogs are background. Developmental perturbation and renal-deficiency findings do not automatically create new process annotations. No NEW annotation is proposed. Private reading notes are not substituted for unavailable primary text.

## Native source reconciliation

The native machine inputs and all 71 reviewed contexts now match. The normal caches for PMID:11741991 and PMID:17618285 contain abstracts; their independent original-text readings remain documented above. The five short excerpts in the review match the actual normal caches, with whitespace normalization only. The preceding private-preparation notes are retained as provenance.
