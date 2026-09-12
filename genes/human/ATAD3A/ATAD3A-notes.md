# ATAD3A notes

- 2026-06-03: Initialized ATAD3A for the Proteostasis PN batch with `just fetch-gene human ATAD3A`.
- 2026-06-03: Falcon deep research was requested using `just deep-research-falcon human ATAD3A --fallback perplexity-lite`. Falcon timed out after 600 seconds and the configured Perplexity fallback failed with an insufficient-quota 401 error, so I completed a manual synthesis in `ATAD3A-deep-research-manual.md`.

## Functional synthesis

- ATAD3A is best reviewed as a mitochondrial inner-membrane AAA+ ATPase/scaffold that acts at inner/outer membrane contact and nucleoid-adjacent regions. UniProt summarizes it as "Essential for mitochondrial network organization, mitochondrial metabolism and cell growth at organism and cellular level" and places it in the mitochondrial inner membrane and mitochondrial nucleoid region.
- The strongest core evidence is mitochondrial organization, membrane/contact-site positioning, and ATPase activity: the ATAD3A domain study reports that "The N-terminal domain interacts with the OM" and that a "central transmembrane segment (TMS) anchors the protein in the IM" [PMID:20154147].
- Nucleoid involvement is supported by D-loop/nucleoid evidence: "human ATAD3 is a component of many, but not all, mitochondrial nucleoids" and ATAD3 RNAi "altered the structure of mitochondrial nucleoids" [PMID:17210950].
- Mitochondrial translation support is well supported but not currently a GOA annotation for ATAD3A: "Both proteins are demonstrated to be required for mitochondrial protein synthesis in human cultured cells, and the major binding partner of ATAD3 is the mitochondrial ribosome" [PMID:22453275].
- The PERK interaction is real but context-specific. During ER stress, "ATAD3A interacted with protein kinase RNA-like endoplasmic reticulum kinase (PERK)" and "PERK-ATAD3A interactions increased during ER stress, forming mitochondria-ER contact sites" [PMID:39116259]. I therefore kept the PERK inhibitor/contact-site/UPR annotations as non-core rather than core.
- The mtDNA-break paper supports stress signaling from damaged mitochondrial genomes, not a broad DNA repair role. It reports that mtDSBs triggered ISR signaling through DELE1-HRI and identified ATAD3A as "potentially pivotal in relaying signals from impaired genomes to the inner mitochondrial membrane" [PMID:37832546].

## PN projection review

- The Proteostasis PN projection proposes ATAD3A -> GO:0000423 mitophagy from the "Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway" category in `projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv`.
- I did not add GO:0000423 mitophagy. The available ATAD3A literature supports mitochondrial morphology, mtDNA/nucleoid organization, mitochondrial protein synthesis, mitochondrial contact-site signaling, and secondary stress responses. I did not find direct evidence that endogenous ATAD3A marks mitochondrial cargo, recruits PINK1/PRKN machinery, functions as a mitophagy receptor, or otherwise executes mitophagy.
- The neurodegeneration paper mentions mutant/pathology-linked mitochondrial fragmentation and mitophagy context, but its direct ATAD3A evidence is Drp1 interaction, ATAD3A oligomerization, fragmentation, mtDNA lesion, and bioenergetic defects [PMID:30914652 "ATAD3A plays a key role in neurodegeneration by linking Drp1-induced mitochondrial fragmentation to defective mtDNA maintenance"]. This is insufficient for a direct mitophagy process annotation.

## Annotation review notes

- Accepted core terms: ATP binding, ATP hydrolysis activity, mitochondrial inner membrane, mitochondrion, mitochondrial nucleoid, and mitochondrion organization.
- Marked generic protein binding annotations as over-annotated. ATAD3A interactions with ATAD3B/HSPD1, DNM1L/Drp1, and CLPB/MAVS-related complexes are biologically informative in context, but GO:0005515 protein binding alone does not capture ATAD3A function.
- Kept as non-core: PERK inhibition/mitochondria-ER contact site/negative regulation of PERK-mediated UPR, antiviral innate immune response, cell growth regulation, and anti-apoptotic process in lung adenocarcinoma.
- Modified the broad DNA damage response annotation from PMID:37832546 toward the more specific integrated stress response and HRI-mediated signaling terms because the paper supports mtDNA-break-triggered signaling rather than DNA repair.
