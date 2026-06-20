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
