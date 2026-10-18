
## 2026-09-21 full-gene evidence re-review

All original source assertions were read and preserved, including source term IDs and evidence. Actual PTHR45640 v19 topology places both targets below PTN000897708: P02515 ends at PTN000163333, P02516 at PTN000163334. Current IBDs for nucleus, cytoplasm, heat response and refolding were recovered, with no loss on either target path. The obsolete unfolded-protein-binding IBD is absent from the current extract; that version difference does not establish functional loss. Exact paths, current node assertions and response hashes are stored in the project audit artifacts.

Full PMID:16572729 demonstrates purified client protection, client-small-Hsp complexes and recovery after addition of ATP-supplemented reticulocyte lysate. Exact Results excerpt: “Altogether, these results demonstrate that Hsp22, Hsp23, Hsp26, and Hsp27 can maintain heat-treated luciferase in a refoldable state, from which it can be refolded by other chaperones into an active enzyme.” Luciferase recovery was54.9±2.8% with Hsp22 and30.7±6.7% with Hsp23. Hsp23 required higher concentrations for comparable aggregation suppression. Hsp23 purification used urea; parallel Hsp22 purification controls support the comparison. The holding step is actual work in refolding, even when other chaperones drive later recovery.

Live GO:0140309 is active and named unfolded protein holdase activity. Its definition allows delivery to an acceptor molecule or to a location, so the previous inter-compartment-only interpretation was false. GO:0044183 does not require ATP hydrolysis; its comment distinguishes folding from holding a client unfolded. Existing obsolete source assertions remain untouched, with specific active replacements. No new redundant annotations or ontology terms were added. Core descriptions now use the active molecular function and contain biological content rather than a pending-ontology workflow.

Full PMID:26705243 distinguishes heat-induction qPCR, cellular refolding, and HSP70-knockdown experiments. The qPCR includes both genes, cellular refolding excludes Hsp22, and HSP70 knockdown tests Hsp27 and CG14207. An Hsp23-specific requirement for HSP70 was not directly tested. Full PMID:19715580 supports insect sHsp sequence relationships rather than a new biochemical assay.

Nuclear localization is supported conditionally rather than rejected from cytoplasmic predominance. Full [PMID:6801431 published paper, UNIGE](https://access.archive-ouverte.unige.ch/access/metadata/180c1f36-730f-4d84-b087-8d650473d717/download) reports salivary-gland nuclear IF immediately after37C1h heat shock, with preimmune and recovery controls (Fig5); selective Hsp23 immunoprecipitation tests antibody specificity (Fig4). Its abstract states “Immunofluorescence microscopy showed the presence of hsp 23 preferentially in nuclei after heat shock”. Fixation and preparation limit interpretation; these are nevertheless direct positive observations.

Full [Duband et al.1986 DOI:10.1139/g86-152, author copy](https://www.researchgate.net/publication/237187480_Expression_and_localization_of_hsp-23_in_unstressed_and_heat-shocked_Drosophila_cultured_cells) reports predominantly cytoplasmic granules with “the nucleoli, which were intensively stained” after37C1h heat shock in Kc cells. Nucleolar signal largely disappears during recovery. Methods report stronger Hsp23 than Hsp26/27 recognition and improved specificity with anti-IgG detection; Discussion explicitly leaves possible cross-reaction in IF unresolved. This supports a contextual nuclear IBA with an honest specificity caveat, not a constitutive nuclear core assignment. PMID:3109982 is whole-insect soluble/particulate partitioning; a pellet alone is not a nuclear-location test.

Full PMID:32437379 establishes Hsp23/Hsp26 co-IP and CNS/bouton imaging, supporting the heat-shock-protein-binding replacement. Synapse-number effects vary with Hsp23 alone versus joint Hsp23/Hsp26 dosage; no new synaptogenesis assertion is added. CalexA/NFAT nuclear translocation is a reporter and must not be mistaken for Hsp23 import. PMID:9514881 independently identifies Ubc9 two-hybrid/co-IP binding, supporting ubiquitin-like-protein-conjugating-enzyme binding without assigning SUMO catalysis to Hsp23. The source DPIM2 abstract does not independently verify a specific pair, although the targeted2020 study does.

Full PMID:19401761 distinguishes Hsp23 P-element expression/survival data from Hsp70 excision and tissue-specific transgene tests. Hsp23 survival was55% versus31% control under constant hypoxia; the detailed Hsp70 controls are not transferred. Source PMID:16313561 explicitly identifies Hsp23 cold-hardening expression, but full target-specific mechanism remains unavailable. Both environmental response contexts are retained noncore.

The existing Falcon report was read completely. Its direct-biochemistry gap overlooks PMID:16572729 and its compartment summary omits the older nuclear papers. Its muscle-protection lead was independently checked in full PMID:27483356: perinuclear ubiquitinated clients lie on the cytoplasmic sarcoplasmic-reticulum surface, so those images do not establish Hsp23 nucleoplasm localization. Young hsp23 mutants still resist degeneration but alter P62-positive aggregate clearance, illustrating context-dependent compensation. Actin/microtubule binding claims based on unspecified syntheses remain research leads, not new annotations.


## Recovery PR follow-up (2026-09-22)

Restored readable GO/PMID/PTN identifiers in curation prose. For DCV1, core
localization cites the recorded UniProt topology and SGD-attributed observation;
the unrelated Rim101 report sentence no longer supports plasma-membrane location.
For YAR1, unanswered report questions are not positive evidence. For SSQ1, the
located Nop1 association remains recorded while its generic binding label is removed.
The annotation changes apply only to the relevant gene; no inherited location is
rejected solely from its best-characterized compartment.
