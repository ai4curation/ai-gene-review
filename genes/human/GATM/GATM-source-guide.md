# GATM source guide

GATM is a mitochondrial amidinotransferase with one principal creatine-synthesis activity. This guide records selected evidence and its limits. The [review](GATM-ai-review.yaml) contains all 37 current context decisions; the [source evidence](GATM-source-evidence.yaml) preserves the original machine fields and sequences.

## Catalytic and product evidence

The current reference assessments distinguish purified human enzyme and recombinant constructs. Both broad amidinotransferase annotations retain measured acceptor breadth as non-core. The InterPro assignment is independently corroborated by the human acceptor panel; the family mapping alone does not establish its full substrate range. The glycine reaction remains the single physiological core. PMID:9218780, PMID:9266688 and PMID:3800397 were read at authentic abstract scope. Selected original Methods/Results for [PMID:36543883](https://pubmed.ncbi.nlm.nih.gov/36543883/) were inspected; its assay and construct limits are in the reference assessment, and its short anchor is centralized there.

[PMID:9148748](https://pubmed.ncbi.nlm.nih.gov/9148748/) was read through the [indexed original PDF](https://scispace.com/pdf/recombinant-expression-and-isolation-of-human-l-arginine-panc9v3rdq.pdf), pp. 771–775, including construct preparation, activity assay and cysteine-mutant results. No figure pixels were inspected. The original [ENA X86401.1 record](https://www.ebi.ac.uk/ena/browser/view/X86401.1) has CDS 506–1681 / CAA60153.1, matching the 391-residue product 2. This sequence record contains no localization assay. The natural-product and engineered-fragment distinctions are stated in the review rather than inferred from length alone.

The three direct [UniProt P50440 product sequences](https://rest.uniprot.org/uniprotkb/P50440.fasta?includeIsoform=true) are 423, 391 and 391 residues. The two shorter sequences differ. Product 3's altered C terminus is not a measured loss-of-activity result. The source evidence retains complete sequences and hashes.

## Binding evidence and informative partner classes

The [PMID:32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/) original supplementary workbook, `1-s2.0-S2211124720310354-mmc3.xlsx`, identifies GATM by GeneID 2628. Its NN1.0 and NN1.0ext sheets contain all thirteen gene pairs below; the overlapping sheets are not independent replications. Exact splice accessions come from the current UniProt/IntAct record, not a sequence-resolved workbook clone. The paper describes an integrated interaction network, so each pair is not automatically assigned the same assay implementation.

| Raw context | Partner accession | Gene | NN1.0 row | NN1.0ext row |
| --- | --- | --- | --- | --- |
| 1 | P11684 | SCGB1A1 | 9536 | 21623 |
| 2 | Q13322-4 | GRB10 | 3925 | 8674 |
| 3 | Q13352 | ITGB3BP | 4651 | 10202 |
| 4 | Q13829 | TNFAIP1 | 11730 | 25751 |
| 5 | Q14457 | BECN1 | 929 | 1780 |
| 6 | Q14693 | LPIN1 | 6072 | 13754 |
| 7 | Q6UY14-3 | ADAMTSL4 | 112 | 214 |
| 8 | Q6ZMY6-2 | WDR88 | 12807 | 28474 |
| 9 | Q8NFB2 | TMEM185A | 11603 | 25585 |
| 10 | Q96CM3 | RPUSD4 | 9340 | 21285 |
| 11 | Q9P1W8 | SIRPG | 9850 | 22335 |
| 12 | Q9UI10 | EIF2B4 | 2952 | 6342 |
| 13 | Q9Y6G5 | COMMD10 | 2259 | 4905 |

The source workbook is available with the [original article](https://doi.org/10.1016/j.celrep.2020.108050); the retained original has SHA-256 `8022031dc6c71bd15b149e2768fe510c45057f3921921b2c658ced53cb77f8bb` (1,828,047 bytes). No additional PPP3R2 table pair is turned into a new annotation.

Four partner classes permit specific binding refinements. The review cites the interaction paper and the actual UniProt partner record separately. These describe the bound protein's class, not a catalytic or regulatory activity of GATM; an independent orthogonal assay or native physiological role is not claimed:

| Partner | Independent class evidence | Binding refinement |
| --- | --- | --- |
| ITGB3BP / Q13352 | [UniProt FUNCTION](https://rest.uniprot.org/uniprotkb/Q13352.json): transcriptional coregulator. Nuclear-receptor coactivation is product-1-specific and is not generalized. | GO:0001221 transcription coregulator binding |
| LPIN1 / Q14693 | [UniProt FUNCTION/CATALYTIC ACTIVITY](https://www.uniprot.org/uniprotkb/Q14693/entry): phosphatidate phosphatase. | GO:0019902 phosphatase binding, not protein-phosphatase binding |
| RPUSD4 / Q96CM3 | [UniProt FUNCTION/CATALYTIC ACTIVITY](https://rest.uniprot.org/uniprotkb/Q96CM3.json): RNA pseudouridylation enzyme. | GO:0019899 enzyme binding |
| EIF2B4 / Q9UI10 | [UniProt FUNCTION](https://www.uniprot.org/uniprotkb/Q9UI10/entry): translation-initiation-factor regulatory subunit. | GO:0031369 translation initiation factor binding |

All four terms have actual `is_a` ancestry to protein binding. GO:0001221 passes through GO:0008134; GO:0019902 passes through GO:0019899. The retained Q13352 and Q96CM3 JSON hashes are `145245a83e74b2e903c8a23724e0067e16fc095f447f5deb939299396f1cfc8f` and `ecbf4b09e9591a4f1232c585398a552c9cd0644549eff771cd10ffbcb4a46129`. Other positive pairs remain recorded without inventing a class or physiological mechanism from a name.

## Location evidence

The [UniProt location record](https://www.uniprot.org/uniprotkb/P50440/entry) qualifies inner-membrane attachment as probable and peripheral. The cytoplasm assertion retains the explicit product-2 database context. Its unqualified GOA row is not rewritten as an isoform-specific annotation; the experimental basis of product-2 localization remains unresolved.

[PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) Table S1 (`mmc2.xlsx`), sheets A row 400 / B row 362, gives P50440 / GATM / GeneID 2628 as `NotID_412`. MitoCoP membership and literature pool 4 are marked; new dataset identification and experimental validation are not. The linked literature identifier is 16120363, whose experiments were not read here. Supplement hash: `10690847c50567e11055d474fbe265fe5d699384f38437acd95734f0a87a9183` (13,872,555 bytes). Original header definitions were inspected; no raw spectra were read.

[PMID:23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/) original SI Table 2 row 796 identifies P50440/GATM. Unique-peptide columns are 0/0 for the cancer pool and 2/2 for duplicate non-cancer pooled analyses. Selected original Methods and contamination caveats were inspected. Supplement hash: `6c76b1cd34e709839d8353a5c1584118f0a0c99d8edbfaf361bd1f275f896a70` (211,902 bytes). This supports occurrence in the preparation, not a product-specific assignment or vesicle function.

The official [Reactome 71275 event](https://reactome.org/ContentService/data/query/71275) names its GATM dimer catalyst and compartment. The dependent 71274 request failed with HTTP 403; no full accession-resolved physical-entity chain is claimed. The event JSON hash is `dc6683d1a7a3b2b54220880f710e13537d79957438c940b628411b9799189f32`. HPA target images were not independently inspected.

## Clinical and physiological source access

The [original PMID:26490222 PDF](https://arpi.unipi.it/retrieve/18df80f1-e87d-43e4-8090-263eff7c82e9/1-s2.0-S1096719215300615-main.pdf), main pp. 253–258 and Table 1, was read for the cognitive and biopsy evidence discussed in the current reasons. Its SHA-256 is `aab39cd01fb58cba980788db560cc7423611635a21d8642ba084bda905561927`. The cognitive and biopsy observations are retained as deficiency phenotypes; neither establishes GATM as an executor of the corresponding learning/memory or atrophy process. PMID:27233232 remains authentic-abstract scope; no current product is assigned to its unspecified novel transcript.

Selected original Methods/Results of [PMID:28844881](https://pubmed.ncbi.nlm.nih.gov/28844881/) were read, with cold and adrenergic-rescue endpoints distinguished in the reasons. [PMID:28978428](https://pubmed.ncbi.nlm.nih.gov/28978428/) is the linked erratum, also reproduced in the [coauthor institutional record](https://mayoclinic.elsevierpure.com/en/publications/erratum-genetic-depletion-of-adipocyte-creatine-metabolism-inhibi/). It corrects one Introduction verb from suppresses to supports. The original normal cache stays unchanged; this is not a remapping or retraction.

Selected original main Methods/Results and captions from [PMID:29654216](https://pmc.ncbi.nlm.nih.gov/articles/PMC6050927/) support the distinct dominant renal aggregation disease. Observed deposits are distinguished from the modeled additional interaction interface. Mutant-cell matrix localization does not reassign normal wild-type topology. Supplements and images were not inspected. The already-present normal cache remains abstract-only and unchanged.

## Phylogenetic provenance and preservation

The actual PANTHER19.0 [tree](https://data.pantherdb.org/PANTHER19.0/books/PTHR10488/tree.tree), [alignment](https://data.pantherdb.org/PANTHER19.0/books/PTHR10488/tree.mia), [sequences](https://data.pantherdb.org/PANTHER19.0/books/PTHR10488/cluster.fasta) and [node attributes](https://data.pantherdb.org/PANTHER19.0/books/PTHR10488/attr.tab) were replayed. Human AN19/PTN002470987 has the exact canonical 423-residue sequence and descends from AN3/PTN000826384 for all three assertions. No retained negative placement blocks that path. The human self-donor supplies experimental grounding. The tree, alignment and IBD information serve distinct roles; a PAINT assertion table alone is not proof of sequence or topology.

The [baseline review](https://github.com/ai4curation/ai-gene-review/blob/1ca4cad1d67742cbba1467027237ef615744a0d8/genes/human/GATM/GATM-ai-review.yaml), journal and two history records remain available at immutable Git locators in the source evidence. The old 37 GOA rows were summarized into 25 review keys; the current review keeps all 37 original contexts. All fifteen old quote associations are preserved privately and historically: six literal cache matches and nine whitespace-only matches. They are not automatically promoted to fresh support. Current short excerpts are attached to the relevant experimental claims and core, with reference-only links retained where another occurrence would add repetition. The source evidence records exact cache offsets and per-source totals, counting repeated quotations; old journal text remains unchanged.

Initial native validation at commit `03a5e9c4`: genuine force/no-seed refresh reproduced all 37 original/native contexts and all three sequences while preserving the inherited review until manual transfer. All 35 planned source records are present: 21 unchanged reused objects and 14 missing-only acquisitions. Every reference title and all three excerpts match the native sources. The caches for PMIDs 9148748 and 28978428 are abstract-only; external original reading is identified separately above. Default validation and strict GOA matching passed with zero annotation advisories. Native status computation sets COMPLETE. The initial report-only mismatch is preserved privately; all 35 source bytes and the ontology cache remain unchanged.

## Review follow-up at bd33ed28

The published UniProt text is byte-identical to the separately retained official flat-file response from 2026-11-04 (SHA-256 `0a5211a817f1b64ecf8c764a063a4de8a17c6be1ef8a4df2bff98d7792a8c37e`). Removed release fields were not manually stripped. The existing PDB links are preserved as database assertions; no structure-identity correction follows from their appearance alone. This amendment changes four annotation decisions, adds direct evidence anchors and partner-record citations, and restores biological description and substrate detail. The 37 original machine contexts, three products, normal source bytes and earlier journal are unchanged.

Validation at bd33ed28: Default validation, strict GOA matching, computed-status audit, genuine EDIT history validation and private rendering pass. Computed review status remains COMPLETE, with zero annotation advisories. The only diagnostic is a dependency deprecation notice. All 35 normal source objects and the ontology cache remain unchanged. All fifteen current quote occurrences match unchanged source bytes; repeated occurrences stay within the aggregate budget.

## Historical readiness follow-up at d1283f06: measured acceptor breadth

The IDA parent retains its experimental scope, while the family-based IEA refinement remains unchanged. Default validation and strict matching of all 37 GOA contexts pass. One intentional same-term action-consistency advisory remains: the experimental broad activity is non-core while the family mapping is refined. Computed status is DRAFT. History validation, status audit, rendering and preservation checks pass; all 35 source objects, the ontology cache and 15 quote occurrences remain unchanged. The preceding COMPLETE outcomes remain historical.

## Gene-level breadth follow-up

The broad IEA assertion now retains the same measured secondary chemistry as the IDA row, superseding the source-specific refinement above. Default validation and strict matching of all 37 GOA contexts pass with zero annotation advisories. Computed status is COMPLETE. History validation, final status audit, private rendering and preservation checks pass; all 35 source objects, the ontology cache and 15 aggregate quote occurrences remain unchanged. Preceding DRAFT and COMPLETE outcomes remain historical.
