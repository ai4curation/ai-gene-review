# ABCA7 notes

## Review status

- First-pass review completed on 2026-06-19.
- `just fetch-gene-pmids human ABCA7` completed successfully; all 7 PMID-backed publication caches were present after refresh.
- Falcon deep research was attempted with `timeout 180 just deep-research-falcon human ABCA7 --fallback perplexity-lite`, but the process timed out and no provider deep-research artifact was written. These notes rely on cached UniProt, GOA, and publication files.
- `just validate human ABCA7` passes cleanly.

## Functional synthesis

ABCA7 is an ATP-binding cassette subfamily A lipid transporter. The most direct biochemical evidence supports ATP-coupled phospholipid translocation/floppase activity, especially phosphatidylserine export: [PMID:24097981 "ABCA7 preferentially exported phosphatidylserine"] The same study connects lipid movement to ATPase activity: [PMID:24097981 "The same phospholipids stimulated the ATPase activity of these ABCA transporters"] and to apolipoprotein loading: [PMID:24097981 "activity is an essential step in the loading of apoA-1 with phospholipids for HDL formation."]

ABCA7 also binds apolipoproteins and supports apoA-I-dependent phospholipid efflux. One early study found [PMID:12917409 "ABCA7 has the ability to bind apolipoproteins and promote efflux of cellular phospholipids without cholesterol"], while another found apoA-I-dependent cholesterol and phospholipid release in overexpression systems [PMID:14570867 "Time-dependent release of cholesterol and phospholipid by apolipoprotein A (apoA)-I was parallel both with ABCA1 and with ABCA7"]. Later substrate work supports choline-phospholipid and lysoPC export in brain-relevant cells: [PMID:28373057 "ABCA7 exported choline phospholipids in the presence of apoA-I and apoE"] and [PMID:28373057 "lysoPC export may be a physiologically important function of ABCA7 in the brain."]

For Alzheimer-relevant biology, ABCA7 should be framed as a lipid transporter that affects membrane trafficking, phagocytosis, and amyloid processing rather than as a direct amyloid receptor. A full-text cached study states [PMID:26260791 "ABCA7 has been shown to mediate phagocytosis and affect membrane trafficking"] and reports that loss of ABCA7 increases amyloidogenic processing: [PMID:26260791 "Suppression of endogenous ABCA7 in several different cell lines resulted in increased β-secretase cleavage and elevated Aβ."] Mechanistically, the same paper links this to endocytosis: [PMID:26260791 "more rapid endocytosis of APP in ABCA7 knock-out cells that is mechanistically consistent with the increased Aβ production"] and discusses amyloid uptake/clearance as a plausible parallel mechanism: [PMID:26260791 "uptake and clearance of aggregated Aβ plaques and aggregates"].

## Annotation decisions

- Accepted ATP binding, ATP hydrolysis, ABC transporter activity, ATPase-coupled intramembrane lipid transporter activity, floppase activity, phosphatidylserine/phosphatidylcholine floppase activity, phospholipid transfer/efflux/translocation, apoA-I receptor activity, and core membrane locations.
- Accepted positive regulation of phagocytosis, apoptotic-cell engulfment, amyloid-beta clearance, negative regulation of amyloid-beta formation, APP catabolic-process regulation, and negative regulation of endocytosis as ABCA7-linked membrane-trafficking outputs.
- Kept cholesterol efflux, positive regulation of cholesterol efflux, and HDL particle assembly as non-core because human overexpression evidence exists but phospholipid/lysoPC export is more consistently supported as the core substrate activity.
- Modified undirected `amyloid-beta formation` annotations to directional regulation terms, and modified `apolipoprotein A-I-mediated signaling pathway` to apoA-I receptor/lipid-efflux terms.
- Marked generic `protein binding` and inferred protein localization to nucleus as over-annotated.

Final action distribution: 55 ACCEPT, 20 KEEP_AS_NON_CORE, 4 MODIFY, 2 MARK_AS_OVER_ANNOTATED.

## Knowledge gaps and experiments

- The major mechanistic gap is whether Alzheimer-associated ABCA7 variants impair ATP-coupled phospholipid transport directly, disrupt apoA-I interaction, or mainly alter phagocytic/endocytic membrane organization.
- Cholesterol efflux should be treated cautiously until endogenous-cell evidence separates ABCA7 from ABCA1-like overexpression behavior.
- Useful experiments would combine endogenous ABCA7 variant knock-ins in human microglia/macrophages with phospholipid/lysoPC transport assays, apoA-I efflux assays, phagocytic-cup recruitment, LRP1/APP endocytosis imaging, and amyloid-beta uptake/clearance assays.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for ABCA7 phospholipid efflux, apolipoprotein binding, reconstituted phospholipid transport, lysophosphatidylcholine export, and loss-of-function effects on APP/amyloid processing. No annotation action changes were needed: ABCA7 remains curated primarily as an ATP-driven phospholipid transporter with phagocytic/endocytic and amyloid-processing consequences, while cholesterol efflux is retained cautiously as non-core where the supporting evidence comes from overexpression or broader ABCA-family behavior.

## Falcon deep research integration (2026-06-21)

The Falcon (Edison) report (`ABCA7-deep-research-falcon.md`) broadly corroborates the existing review's core framing of ABCA7 as a plasma-membrane, ATP-driven phospholipid translocator/exporter coupled to phagocytosis, membrane trafficking, and amyloid biology, and adds structural and mitochondrial detail not in the current notes. (All Falcon-sourced citations below are not yet independently verified against full text.)

New or refined findings beyond the existing notes/review:

- Structural mechanism: 2023 cryo-EM structures of human ABCA7 (3.6-4.0 A) capture open and ATP-bound closed states and support a "bellows-like" lipid-translocation mechanism; the ATP-bound closed state was captured with the hydrolysis-deficient E965Q/E1951Q double mutant, with a small extracellular lipid exit pocket lined by basic residues (R475/K478/R482/R548/K1407) [Le et al., EMBO J 2023, doi:10.15252/embj.2022111065] (not yet independently verified against full text).
- Lipid-environment modulation of ATPase: activity highest in PE and PS nanodiscs, lower in PC, and inhibited by cholesterol; ECD basic-residue mutants (ABCA7-AAA) reduce ATPase activity [Le et al., EMBO J 2023, doi:10.15252/embj.2022111065] (not yet independently verified). This refines (does not contradict) the existing PS/PC floppase framing.
- Mitochondrial lipid metabolism (genuinely new pathway): ABCA7 knockout in human iPSC cortical organoids/neurons lowers phosphatidylglycerol and cardiolipin, causing abnormal mitochondrial morphology, reduced ATP synthase activity/respiration, raised ROS, and synaptic dysfunction; rescued by phosphatidylglycerol or NMN, and recapitulated in neuron-specific Abca7 KO mouse synaptosomes [Kawatani et al., Mol Psychiatry 2024, doi:10.1038/s41380-023-02372-w] (not yet independently verified). Not represented in current annotations.
- Disease-variant mechanism / localization: AD-associated missense variants cause plasma-membrane exclusion with ER retention rather than loss of expression; p.G1820S co-segregated with AD in a pedigree [Bossaerts et al., Acta Neuropathol Commun 2022, doi:10.1186/s40478-022-01346-3] (not yet independently verified). This supports keeping ER (GO:0005783) localization as a real, disease-relevant compartment, not merely non-core noise.
- Regulation: SREBP-dependent negative regulation links ABCA7 to host defense; cholesterol depletion downregulates ABCA7 in microglia/astrocytes but not neurons, and IL-1beta/TNFalpha downregulate it in microglia (cell-type-specific) [Abe-Dohmae & Yokoyama, Gene 2021, doi:10.1016/j.gene.2020.145316; Duchateau et al., Alzheimer's Dement 2024, doi:10.1002/alz.13805] (not yet independently verified).
- Interaction partner: LRP1 co-relocalizes with ABCA7 to the plasma membrane in the presence of apoptotic cells, consistent with the curated phagocytic-cup/engulfment role [Dib et al., Int J Mol Sci 2021, doi:10.3390/ijms22094603] (not yet independently verified).
- Disease genetics refinement: ancestry-specific effect sizes (PTC OR ~1.4-5.3; stronger burden in African/African American cohorts, e.g. 44-bp deletion rs142076058 p.R578fs), VNTR expansion, and the c.5570+5G>C splice variant [Duchateau et al., Alzheimer's Dement 2024, doi:10.1002/alz.13805; Stepler et al., J Alzheimers Dis 2022, doi:10.3233/jad-215306] (not yet independently verified).

Discrepancies / annotations to revisit:

- No direct contradiction with the existing review or its actions. The Falcon report agrees that cholesterol efflux is weaker than ABCA1 and secondary to phospholipid export, supporting the existing KEEP_AS_NON_CORE on the cholesterol-efflux terms.
- Potential gap (consider, do not auto-apply): the mitochondrial phospholipid (phosphatidylglycerol/cardiolipin) phenotype from Kawatani 2024 is not captured by any current GO term in the review; this is a downstream organismal/cellular consequence and may warrant a non-core process annotation or a suggested_question rather than a core function. No specific well-fitting GO term was confirmed via OLS here, so flagging only.
- The existing review already handles amyloid biology with directional terms (GO:1902430, GO:1902991, GO:1900223, GO:0150094); Falcon's APP/amyloid material reinforces these and the GO:0034205 MODIFY decisions, so no change recommended.
