# GATAD2B manual source guide

GATAD2B/p66β is a noncatalytic nuclear NuRD regulator. The reviewed evidence supports chromatin association, MBD and histone interactions, and a contribution to transcriptional repression and remodeling. Human p66β is not assigned the ATPase activity of CHD proteins or the deacetylase activity of HDAC subunits. One core unit represents this chromatin-regulatory role.

This is a manually authored literature and provenance guide. The original-context archive, actual cache access and selected reading scopes are distinguished below. The histone-binding amendment adds one MF assertion and preserves the earlier decisions. Affected target validation, strict GOA matching and computed-status checks passed; the review status is COMPLETE.

## Original contexts and products

The review retains all 74 official annotation contexts and their 74 distinct genuine seed keys. The [compact evidence table](GATAD2B-source-evidence.yaml) preserves every original field, including evidence, original references, partners, assignment source, dates and qualifiers. Its raw-to-forecast and actual-native joins are explicit; all 16 export columns and all genuine seed machine fields match the original projection. The current decisions are 33 ACCEPT, 22 REMOVE, 11 MODIFY, seven UNDECIDED and one KEEP_AS_NON_CORE, plus two NEW assertions for transcription corepressor activity and histone binding (76 stored rows total).

Raw 0 retains its literal `contributes_to` relationship for nucleosomal DNA binding. The source concerns a complex-level activity; it does not establish autonomous binding or catalytic activity of isolated p66β. Raw 3, 6 and 28 each retain one `occurs_in GO:0005634` atom, represented by a flat BFO:0000066 extension. There are no disjunctions or manufactured duplicate originals.

The reviewed official Q8WXI9 record and direct FASTA specify a displayed 593-residue product, with no declared alternative-product block. The private identity record and evidence table retain its exact sequence hash. No `-1` suffix or functional isoform class is invented. Tagged constructs, deletion constructs and the 122-residue worm DCP-66 EMSA reagent remain experimental reagents. GATAD2A/p66α is a separate paralog.

## Human NuRD function and inherited DNA recognition

[PMID:16415179](https://pubmed.ncbi.nlm.nih.gov/16415179/) supplies human p66β reporter, depletion and histone-tail interaction evidence. Gal4 provides targeting in tethered assays. Alpha K149R mutagenesis and detailed alpha domain tests are not relabeled beta experiments. Its early suggestion of A/B co-occupancy is distinguished from later separate-assembly evidence.

[PMID:33283408](https://pubmed.ncbi.nlm.nih.gov/33283408/) describes actual human nuclear NuRD cross-link topology, with mixed paralog populations and shared-peptide limitations. Direct domain-deletion tests use GATAD2A. Together with beta-specific biochemical evidence, the study supports a conserved noncatalytic structural role; it does not establish a fixed beta stoichiometry or beta-specific purified bridge assay. [PMID:28977666](https://pubmed.ncbi.nlm.nih.gov/28977666/) and [PMID:16428440](https://pubmed.ncbi.nlm.nih.gov/16428440/) independently identify p66β in human NuRD preparations.

The actual PTHR13455 tree has 114 nodes, 58 leaves and a 1,917-column alignment. Exact Q8WXI9 maps to AN16/PTN002491641 and descends from AN0/PTN001003231. Four literal IBD assertions and their donor mappings are retained in the evidence table; no target-path negative assertion was found. Human self-donor entries are legitimate experimental grounding. Donor count is not used to grade support.

The DNA-binding transcription-factor IBD is grounded in worm DCP-66. Selected original [PMID:16159881](https://pubmed.ncbi.nlm.nih.gov/16159881/) Methods, Results, Figure 3 caption and Discussion show yeast one-hybrid recognition, competitive EMSA in reticulocyte lysate and a reporter/genomic-rescue relationship. The EMSA construct is a 122-residue fragment. This supports the ancestral inference while leaving the human recognition sequence and endogenous loci unresolved. Human Gal4-tethered repression alone would not establish that function. The retained electronic sequence-specific DNA-binding claim is not replaced through a nonexistent GO:0000981-to-GO:0043565 ontology path.

The added GO:0042393 assertion records the directly tested histone-binding mechanism. The existing single corepression unit remains sufficient; nucleosomal DNA binding is a distinct qualified complex activity.

The added GO:0003714 assertion rests on human repression and recruitment experiments. Its molecular-function subtype hierarchy contains no existing reviewed assertion or replacement; cross-aspect activity-to-process links do not duplicate this MF.

The complete [PMID:11756549 Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC139742/#sec12) argues against canonical GATA-sequence recognition because required residues differ from GATA transcription factors. It then leaves recognition of a similar DNA sequence or association with a DNA-binding protein open. That comparator is canonical GATA factors, not the worm p66 donor recognizing Ex-1. The experiments use human KIAA1150/AB032976 plus 5′ RACE, yielding 593-residue p66; current Q8WXI9 links KIAA1150 and AF411836. Exact historical-construct alignment was not repeated. This paper and PMID:16415179 are not positive DNA-recognition evidence and are removed from those support lists. The IEA domain mapping is considered separately from independent PAINT grounding. ACCEPT retains the inferred transcriptional recognition facet; the core synthesis highlights direct human corepression, without implying that every retained MF requires a separate core unit.

## Interaction evidence and partner-class refinements

Positive screen interactions are preserved even where the generic protein-binding annotation is removed. Original HuRI and 2014 S2G target rows were joined to exact positive IntAct records with source-specific gene, accession and clone limits. A positive pair does not establish purified affinity, endogenous stoichiometry or a physiological effect. Conversely, a verified pair plus an independently established partner class can support a specific binding term without requiring the same screen to reproduce the partner’s regulatory outcome.

Three MBD3 contexts refine to transcription coregulator binding. MBD3’s NuRD coregulator role is supported independently; weak DNA association is not denied or equated with sequence-specific TF identity. The original MBD3–GATAD2B pull-down in [PMID:25123934](https://pubmed.ncbi.nlm.nih.gov/25123934/) is explicit in the authentic structured abstract; full original Methods remain uninspected.

The HuRI FHL2 source uses Q14192-1, the displayed 279-residue product. Selected original [PMID:15692560](https://pubmed.ncbi.nlm.nih.gov/15692560/) human FHL2/FOXO1/SIRT1 experiments establish a coregulator class independently of the GATAD2B pair. No GATAD2B–FHL2 physiological mechanism is claimed.

The ZGPAT source is literal Q8N5A5-2. [PMID:19644445](https://pubmed.ncbi.nlm.nih.gov/19644445/) tests a 511-residue human ZIP/BC032612 product with sequence-selective CASTing and site-dependent repression. AAH32612.1 and current Isoform 2 share the splice architecture but differ exactly at the documented source R61/current S61 natural variant. They are not identical sequences. Isoform 2 is not the non-DNA-binding short Isoform 4. The GATAD2B interaction is independently positive in HuRI, supporting DNA-binding transcription-factor binding.

The LRF/ZBTB7A interaction is supported by selected original [PMID:26816381](https://pubmed.ncbi.nlm.nih.gov/26816381/) human interaction assays and independent LRF DNA occupancy/repressor evidence. DISC1 fragment and cell-type contexts, the CSB anti-Myc positive versus anti-Flag negative result, and the BRAF mutant assay contexts remain separately qualified in their individual reasons and reference assessments.

## Compartment and process limits

Nuclear puncta do not by themselves establish splicing-factor speckles. Selected original [PMID:11756549](https://pubmed.ncbi.nlm.nih.gov/11756549/) Methods/Results/Discussion and textual captions were read: human FLAG/GFP p66 forms puncta in NIH3T3, with mouse MBD3 redistribution and no identified splicing marker. [PMID:12183469](https://pubmed.ncbi.nlm.nih.gov/12183469/) remains abstract-only after failed publisher routes. Four nuclear-speckle contexts remain UNDECIDED, without asserting absence or wrong-gene attribution.

Selected original [PMID:22560079](https://pubmed.ncbi.nlm.nih.gov/22560079/) establishes genuine NuRD-dependent pluripotency-gene control and lineage effects in mouse Mbd3/Mbd3b experiments. [PMID:19927129](https://pubmed.ncbi.nlm.nih.gov/19927129/) establishes positive as well as negative transcriptional effects through FOG1 motifs, MTA depletion and primary mouse cells. Selected original text and the complete source-reading receipts were inspected. The inspected experiments do not resolve p66β-specific participation, and detailed supplements were not recovered. Fate specification, stem-cell differentiation and positive transcription therefore remain unresolved at the GATAD2B-specific level. Negative Pol II regulation is independently supported by human beta experiments and can be refined accordingly.

Telomeric p66β recruitment in [PMID:25150861](https://pubmed.ncbi.nlm.nih.gov/25150861/) is retained as a non-core ALT-cell localization. The source’s selected indexed original text was inspected independently of the abstract-only normal cache; images and supplemental target tables were not inspected. [PMID:27732854](https://pubmed.ncbi.nlm.nih.gov/27732854/) contains actual p66β assembly/chromatin observations despite its alpha-focused DNA-damage recruitment mechanism. Those distinct scopes are retained.

All 14 incoming Reactome location events have actual target chains to human Q8WXI9 residues 1–593 in nucleoplasm. The SUMOylation event directly contains GATAD2B and its SUMO1-K33 product. Other chains pass through the alternative-member SUMO-GATAD2A/B set, without implying A/B co-occupancy. The remodeling and deacetylation reactions identify CHD and HDAC catalytic roles. In R-HSA-9941683, an MBD3 word in the first summation sentence is distinguished from the actual MBD2-containing objects.

## Neurodevelopmental and provenance references

[PMID:23644463](https://pubmed.ncbi.nlm.nih.gov/23644463/) directly links human loss of function to a recognizable neurodevelopmental disorder and separately reports neuronal fly-ortholog phenotypes. The molecular route to those phenotypes remains unresolved. [PMID:23033978](https://pubmed.ncbi.nlm.nih.gov/23033978/) supplies the earlier cohort context; its abstract alone does not identify the target patient. The added assessments distinguish these disease sources from the partial-cDNA provenance of PMID:10574461 and large-scale HeLa identification in PMID:17924679. All four current caches are abstract-only.

## Typed specificity and current provenance

| Proposed term | Verified relation to original |
| --- | --- |
| GO:0001221 transcription coregulator binding | is_a GO:0008134, is_a GO:0005515 |
| GO:0140297 DNA-binding transcription factor binding | is_a GO:0008134, is_a GO:0005515 |
| GO:0000122 negative regulation of transcription by RNA polymerase II | is_a GO:0045892; paths to GO:0006355 through GO:0045892 or GO:0006357 |
| GO:0000785 chromatin | part_of GO:0005694 chromosome |
| GO:0016581 NuRD complex | is_a GO:0005667, is_a GO:0032991 |

All 53 cited references have manual assessments. A full-text availability flag does not imply every section was read: the PMID35512704 cache contains only selected sections, while several abstract-only caches were supplemented by authentic external originals. The compact ledger identifies five short active excerpts without repeating their text. All five current quote locators identify genuine repository cache paths, hashes and byte offsets. The earlier PMID16159881 external-abstract locator remains explicitly historical in the ledger; it is not labeled as a cache offset.

The bounded 74-source union contains 45 PMIDs, 26 Reactome paths and three existing family files. At actual base 1ca4cad1d67742cbba1467027237ef615744a0d8, 53 existing source objects were reused byte-exactly, R-HSA-9976102 was reused from the exact published GATA3 commit c07cbe8655d55b30fdccfa1a4f186cef5923ecad, and eight missing publications plus twelve missing Reactome entries were acquired natively. The original 71-path qualification and the three-source addendum are both retained. The genuine 74-row seed is preserved separately. Native acquisition adds a full-text PMID:11756549 cache already covered by the selected original reading; PMID:12183469 remains abstract-only. Availability does not imply additional sections or images were inspected. Existing source files were not overwritten.
## Follow-up checks

Target validation passed without annotation advisories, and strict GOA matching passed for all 74 original contexts plus the declared NEW row. Computed review status is COMPLETE; seven source-specific UNDECIDED judgments remain. Genuine EDIT history and private render/link/whitespace checks accompany the amendment. These completed checks apply to published amendment a19cd551. The histone-binding amendment has a separate completed validation record in source evidence. All 74 source objects and the term cache remain unchanged.
