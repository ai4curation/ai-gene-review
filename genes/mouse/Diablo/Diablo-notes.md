

## 2026-10-26 systematic mammalian apoptosis audit

Reviewed every seeded annotation from the review YAML, preserving every original machine-sourced field and adding no NEW rows. Original terms, evidence, references, relationship fields and supporting entities are unchanged. The gene-level assessment includes functions outside the apoptosis module. Existing source-specific evidence guides and prior history records remain intact.

The review and annotation-reviewer workflow was applied. Default Falcon research and normal publication caching were launched in parallel. Falcon and the perplexity-lite fallback failed for all four targets (provider access errors; command logs under `.cache/module-audit-logs/execution-deep-*`). `fetch-gene-pmids` completed successfully for each. No provider-branded research file was fabricated. This manual notebook and the normal primary publication/UniProt caches supply the research trail.

Preserved the established DIABLO evidence guide, isoform/construct cautions, positive-regulatory refinements and independently supported BIR-domain binding. Mature DIABLO antagonizes IAPs rather than cleaving caspases. PMID:10929712 is the mouse-linked discovery source in curated UniProt; PMID:10972280 contains human SMAC reconstitution with assay-specific human or mouse XIAP reagents, and is not relabeled as an all-mouse experiment. PMID:14512414 establishes cooperative BIR2/BIR3 antagonism: the isolated BIR2 fragment can remain in a ternary caspase/SMAC complex, so a simple universal competitive-blockade cartoon is inadequate.

PMID:14623868 explicitly reports that “the release of endogenous Smac was not sufficient to overcome the XIAP resistance” in sympathetic neurons. Exogenous SMAC plus cytochrome c and the motif control support conditional participation; they do not establish universally sufficient endogenous release. PMID:16085184 supports peroxide-associated mitochondrial redistribution and reciprocal expression/antisense effects in mouse C2C12 cells. PMID:20614026 identifies native SMAC in activated CD40 receptor assemblies in mouse B cells; preserve co-complex presence without claiming direct CD40 binding or a receptor-signaling core.

Mature mitochondrial IMS residence is distinct from the canonical human membrane-processing intermediate. Mouse refinement to IMS is supported by import/release and compartment-marker studies (PMID:15814844; PMID:18385140). The latter full text uses SMAC as an IMS marker while studying phosphatases; a paper foregrounding another protein is not irrelevant. Human PARL evidence (PMID:28288130) is not promoted to a directly demonstrated native mouse processing route. Mouse centriole and sperm midpiece/principal/end-piece ISO assertions list human Q9NR28, but those exact donor measurements were not recovered in the current human review; leave them UNDECIDED rather than deleting a plausible localization.

Current generic-binding policy supersedes the earlier human DIABLO task-specific/ClinGen retention decision for this audit. Bare GO:0005515 rows lacking a supported specific functional refinement are REMOVE only because uninformative. Their actual measured associations, isoforms, and experimental limitations remain in reasons and the source guide; no interaction is declared false. Supported specific refinements, including BIR-domain binding and verified partner-class interactions, are preserved. This supersession is recorded in a new append-only helper-generated history rather than rewriting historical decisions. Mouse BIR binding is independently supported in the core; no redundant annotation is created merely to silence a coverage advisory.


## PR #5558 follow-up: retain mitochondrial assertions (2026-10-26)

Restored 10 existing GO:0005739 rows to ACCEPT under the informative root-organelle exception. Each rationale now identifies the original evidence scope; separate IMS annotations are unchanged. Organelle localization is not defective because a finer compartment is also supported. No original annotation payload, processing/isoform qualifier, or source file was changed. Direct localization, comparative transfer and inventory evidence remain distinct; abstract-only sources are not represented as full-text topology assays.

- Row 3: This HDA annotation comes from the mouse mitochondrial proteomic survey across brain, heart, kidney and liver. The cached source is abstract-only, so no new target-specific peptide or topology claim is made from it. Retain the curator-supported mitochondrial detection, corroborated independently by mouse SMAC localization/release and import experiments.

- Row 4: The MitoCarta study combines mass spectrometry, GFP tagging and integrative evidence across 14 mouse tissues to establish a mitochondrial inventory. Its organelle-resolution annotation is consistent with independent mouse SMAC localization/import evidence; inventory inclusion does not itself resolve IMS topology.

- Row 5: The PAINT mitochondrial inference at PTN001283560 is supported by mouse and human experimental grounding and agrees with direct mouse localization/release studies. Inclusion of the target among descendant sources is legitimate, not circular. There is no evidence here of loss of mitochondrial targeting or a misplaced ancestral assertion.

- Row 6: Full-text Figure 7 in PMID:14623868 shows punctate mitochondrial endogenous Smac staining in mouse sympathetic neurons and loss of that staining after H2O2 treatment. This directly supports mitochondrial localization and stimulus-dependent release. The failure of released endogenous Smac to overcome XIAP in this neuronal setting limits its functional sufficiency, not its localization.

- Row 7: PMID:15814844 explicitly uses full-length mouse DIABLO in import/processing experiments, including a heterologous yeast system. The study supports mitochondrial targeting and processing with an IMS mature pool; the historical IMP-processing model is not treated as proof that every native mammalian context uses the same protease.

- Row 8: The cached abstract of PMID:15882989 reports mitochondrial Smac/Diablo release and explicitly includes mouse embryonic fibroblast experiments on MEKK1-dependent release. Retain the experimental organelle assignment. The abstract does not provide submitochondrial topology or justify a new universal signaling mechanism.

- Row 9: PMID:16085184 explicitly reports Western-blot detection of Smac/DIABLO translocation from mitochondria to cytoplasm in C2C12 myogenic cells after H2O2 treatment. This supports mitochondrial residence and stimulus-dependent release; the abstract-only cache does not independently resolve IMS topology.

- Row 10: The InterPro Smac/DIABLO family and fold mappings plus UniProt mitochondrial location mapping are consistent with directly characterized mouse targeting and release. These independent target observations support the organelle claim without treating an electronic location line as its own experimental evidence.

- Row 11: Transfer from characterized human DIABLO Q9NR28 is consistent with conserved mitochondrial targeting and independent mouse localization/import experiments. Retain the correct mitochondrial orthology inference; source-specific subcompartment and processing details are assessed separately.

- Row 12: The full text of PMID:18385140 uses SMAC as a mitochondrial and IMS marker during rat kidney mitochondrial purification and subfractionation. This is comparative localization evidence, not a direct mouse assay; its conserved organelle assignment agrees with independent mouse SMAC targeting and release experiments. The paper’s main focus on DSP18/DSP21 does not negate the assayed SMAC marker.

This bounded follow-up reused the prior genuine research-provider attempts and cached/source-analysis evidence; provider failure logs remain in `.cache/module-audit-logs/execution-deep-mouse-Diablo.log`. Independent annotation-reviewer consultation agreed with retaining root-organelle claims and their separate finer localization evidence.
