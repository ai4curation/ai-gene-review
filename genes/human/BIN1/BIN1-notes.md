# BIN1 curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human BIN1 --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, PANTHER family, and publication evidence.
- BIN1 encodes amphiphysin II, a BAR-domain and SH3-domain membrane remodeling/adaptor protein with major brain and skeletal-muscle isoforms. UniProt frames the core function as control of plasma membrane curvature, membrane shaping/remodeling, T-tubule formation, vesicle sorting, BACE1 trafficking, and actin remodeling.
- The BAR-domain membrane-curvature function is the core molecular function. BAR domains "generate and sense membrane curvature" by binding negatively charged membranes [PMID:18658220 "BAR domains generate and sense membrane curvature"], and BIN1 N-BAR disease mutants impair membrane tubulation in vivo and in vitro [PMID:24755653 "two mutants showed impaired membrane tubulation both in vivo and in vitro"].
- Muscle T-tubule and neuronal endocytic-domain localization are well supported. Amphiphysin II/BIN1 is concentrated around T tubules in skeletal muscle and beneath the plasma membrane at axon initial segments and nodes of Ranvier in brain [PMID:9182667 "In skeletal muscle, amphiphysin II is concentrated around T tubules, while in brain it is concentrated in the cytomatrix beneath the plasmamembrane of axon initial segments and nodes of Ranvier"].
- The SH3-domain adaptor function is core for endocytosis and muscle membrane remodeling. BIN1 mutations can disrupt DNM2 interaction and membrane tubule recruitment, supporting dynamin/GTPase-binding annotations [PMID:17676042 "the functional interaction between BIN1 and DNM2 is necessary for normal muscle function and positioning of nuclei"].
- BACE1 trafficking and amyloid-beta production annotations are real but non-core. The cached abstract says BIN1 depletion increases BACE1 by impaired endosomal trafficking and reduced lysosomal degradation [PMID:27179792 "the depletion of BIN1 increases cellular BACE1 levels through impaired endosomal trafficking and reduces BACE1 lysosomal degradation"], which supports cargo trafficking rather than direct aspartic protease inhibitor activity.
- Tau binding is supported and Alzheimer-relevant, but I kept it non-core because it is a context-specific disease/pathology interaction rather than the primary BAR-domain membrane remodeling role [PMID:25051234 "BIN1 interacts with the microtubule-associated protein Tau"].
- Nuclear/MYC/transcription/cell-cycle/apoptosis annotations are retained as non-core because they represent tumor-suppressor or isoform-specific literature rather than the main membrane-remodeling function.
- Generic `protein binding` annotations are over-annotated; more informative binding terms such as phospholipid binding, clathrin binding, GTPase binding, and actin filament binding are retained where supported.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for BIN1 membrane-curvature/BAR-domain evidence, disease-mutant membrane tubulation evidence, DNM2 interaction evidence, BIN1-BACE1 trafficking, and BIN1/tau/clusterin Alzheimer-context interaction evidence. No annotation action changes were needed: BIN1 remains curated primarily as a BAR/SH3 membrane-remodeling and endocytic adaptor, with BACE1/tau/Alzheimer outputs retained as non-core context rather than the defining molecular function.

## Falcon deep research integration (2026-06-21)

A Falcon (Edison) deep-research report is now in `BIN1-deep-research-falcon.md`; it broadly corroborates the existing review's framing of BIN1 as a BAR/SH3 membrane-curvature and endocytic-adaptor protein with non-core muscle T-tubule, cancer/MYC, and Alzheimer roles, adding mechanistic and cardiac detail but no findings that contradict the current annotations. The Falcon-sourced citations below are not yet independently verified against full text.

New or refined findings beyond the existing notes/review:

- Domain-to-exon architecture mapped explicitly (20 exons): N-BAR exons 1-10, PI domain exon 11, PS linker exon 12, CLAP exons 13-16, MYC-binding domain exons 17-18, SH3 exons 19-20 [Spooner & Dixon, Am J Physiol Heart Circ Physiol 2025, doi:10.1152/ajpheart.00198.2025].
- Autoinhibition mechanism refined: the PI domain (and exon-13 CLAP segment) binds intramolecularly to the SH3 domain to lock a closed state; PI(4,5)P2 engagement or proline-rich partner binding releases the active open conformation, spatially restricting membrane sculpting [Spooner & Dixon 2025].
- Quantitative membrane-remodeling detail: tubulation plateaus near ~3% PI(4,5)P2 and depends on cholesterol; Lys164/165/166 in the BAR region anchor acidic phospholipids and their charge-reversal abolishes tubulation [Spooner & Dixon 2025].
- Cardiac excitation-contraction-coupling role and partners are new vs the existing notes: BIN1 anchors microtubules via the BAR-CLIP-170 interaction to deliver CaV1.2 to T-tubules and scaffolds RyR2 at dyads; BIN1 loss mislocalizes CaV1.2/RyR2 and underlies heart failure [Spooner & Dixon 2025]. (Existing YAML already KEEPs cardiac ISS terms GO:1904878, GO:1903946, GO:0086091, GO:1901380 as non-core; this provides the mechanistic basis.)
- N-WASP recruited via SH3 to drive ARP2/3 actin polymerization linking T-tubules to cytoskeleton, giving a mechanistic basis for the existing actin-polymerization (GO:0030838) and actin-filament-binding annotations [Spooner & Dixon 2025].
- MTM1/myotubularin cooperates with BIN1 (favored in the open conformation) to grow elongated muscle tubules, coupling phosphoinositide homeostasis to tubulation [Spooner & Dixon 2025].
- Alzheimer mechanism refined: legumain cleaves neuronal BIN1 at N277/N288 to produce a BIN1(1-277) fragment found in AD brain that binds tau, accelerates tau aggregation, and promotes transcellular tau spread by enhancing clathrin-mediated endocytosis [Zhang et al., PLOS Biology 2024, doi:10.1371/journal.pbio.3002470]; SH3 binds the tau 216-PTPP-219 proline-rich motif, modulated by tau phosphorylation [Lasorsa et al., Biochemistry 2023, doi:10.1021/acs.biochem.2c00717].
- AD isoform imbalance refined: shift toward shorter glial isoforms and loss of longer neuronal (CLAP+) isoforms is implicated in pathology [Saha & Karati, Egypt J Med Hum Genet 2025, doi:10.1186/s43042-025-00759-8; Hu et al., bioRxiv 2025, doi:10.1101/2025.03.31.646439].
- New neuron-specific interactor: RIN2 recruits BIN1 to RAB5-positive early endosomes (neuronal interactome), an AD-relevant endosomal-targeting mechanism [Wei et al., bioRxiv 2026, doi:10.64898/2026.03.14.711835] (0 citations, preprint — treat as preliminary).
- Centronuclear myopathy genotype-mechanism split reaffirmed: BAR-domain mutations abolish membrane remodeling, whereas SH3 truncations selectively abolish DNM2 recruitment while preserving tubulation [Zambo et al., eLife 2024, doi:10.1101/2023.02.14.528471].

Discrepancies / annotations to revisit:

- No contradictions with existing annotations were found; the report reinforces the current MODIFY of GO:0019828 (aspartic-type endopeptidase inhibitor activity) toward trafficking terms, since Falcon also frames the BACE1/amyloid effect as trafficking-mediated, not direct protease inhibition.
- Optional refinement to consider (not required): the BAR-CLIP-170 and SH3-N-WASP/ARP2/3 mechanisms could justify more informative MF terms (e.g. microtubule-anchoring / actin-related), but these are cardiac/muscle-context roles and current non-core framing remains adequate; defer pending full-text verification.
