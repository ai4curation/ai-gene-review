# FBXL4 notes

Literature review was done manually from cached PubMed records; the falcon deep-research report (FBXL4-deep-research-falcon.md) completed afterwards and was skimmed for consistency with the review decisions; no conflicts were found.

- SCF-FBXL4 is an outer-membrane E3 ligase degrading BNIP3 and NIX [PMID:36896912 "We determined that FBXL4 functions as an integral outer-membrane protein that forms an SCF-FBXL4 ubiquitin E3 ligase complex."; "SCF-FBXL4 ubiquitinates BNIP3 and NIX to target them for degradation."].
- Independent confirmation [PMID:37161784 "FBXL4 actively suppresses mitophagy by preventing NIX and BNIP3 accumulation"; PMID:37102372 "FBXL4 restricts NIX and BNIP3 levels via direct interaction and protein destabilization"].
- PPTC7 is an adaptor linking BNIP3/NIX to FBXL4 [PMID:38992176].
- In vivo: Bnip3 or Nix deletion rescues Fbxl4-/- mice [PMID:36896912 "knockout of either Bnip3 or Nix rescues metabolic derangements and viability of the Fbxl4-/- mice"].
- The 2013 intermembrane-space localization [PMID:23993194] conflicts with later outer-membrane data; left UNDECIDED.
- 'autophagy of mitochondrion' and 'regulation of mitophagy' annotations modified to GO:1901525 negative regulation of mitophagy.


## 2026-10-26 — primary evidence and direct annotation follow-up

Read the [primary evidence guide](FBXL4-direct-source-guide.md), [direct decisions](FBXL4-direct-decisions.yaml), [binding records](FBXL4-binding-records.yaml) and [MitoCoP target records](FBXL4-mitocop-records.yaml) for stable article/table locators. The original provider report and artifacts remain exact; no substitute report was authored.

The direct evidence supports SCF substrate recognition and negative regulation of mitophagy through BNIP3/BNIP3L turnover. PPTC7-assisted receptor recruitment is distinct from FBXL4–SKP1/CUL1 assembly. PMID38992176 and PMID40025034 report different D78A and overexpression outcomes in different cellular/treatment contexts; no reconciliation, universal dose response or proven simultaneous ternary occupancy is asserted. The contextual PMID21757720 KDM4A turnover observations are retained with their lysate/co-IP limits.

The 2013 intermembrane-space assignment has actual positive protection/fractionation experiments. It remains undecided against later outer-membrane observations because the preparation and protease conditions differ and the earlier paper prints conflicting trypsin units. MitoCoP independently supports mitochondrion; its target membrane-association result is ambiguous and is not converted into an exact topology measurement.

Original PMID32814053 supplements and six matching IntAct records establish TPP1–FBXL4 and DNM2–FBXL4 two-hybrid pairs. Official definitions support specific protease-binding and GTPase-binding refinements. The original clone IDs and empty construct-feature fields do not resolve insert boundaries or a mature TPP1 state; no partner catalytic activity, physiological substrate relationship or new binding core is inferred.

All 29 source annotation objects/order, 60 inherited quotation paths/text/reference associations, 27 inherited reference identities/findings, zero product objects, and the original core/description remain intact in this direct-lane proposal. Twelve direct reviews and fourteen complete primary-reference assessments are proposed; the latter include two genuinely acquired additions, PMID21757720 and PMID40025034. Four independently read shared database scopes are included once. A separate, unapplied synthesis outline preserves the six inherited core quotations for later combined review. No new annotations or quotations were added.

## 2026-10-26 — integrated primary and database synthesis

Combined the two evidence lanes into 29 reviewed annotations: 8 ACCEPT, 5 TOO_GENERAL, 1 KEEP_AS_NON_CORE, 4 MODIFY and 11 UNDECIDED. The historical lane entries above and the separate database notes retain their original scope; the present integrated review applies the substrate-adaptor core and two bounded biology gaps/experiments. The older broad suggested questions and proposed rescue experiment are preserved in the immutable preimage and replaced here by the two specific, source-grounded investigations.

The single core is SCF-FBXL4 substrate recognition at the mitochondrial outer membrane, linked to receptor turnover and mitophagy restraint. Protease/GTPase binding observations remain specific interaction refinements without separate binding cores. HPA nuclear-speck evidence remains contextual; modeled Reactome cytosol and the older intermembrane-space interpretation retain source-specific uncertainty. These do not negate the positive mitochondrial pool or establish exclusivity.

All 60 inherited quotation associations, including six core quotations, remain exact. The core adds only a bare PMID40025034 citation. All 27 inherited reference identities/titles/findings and all 29 source objects/order remain exact. Two genuine additional publications are included, and the four shared database primary scopes occur once in the complete primary assessments. No NEW annotation, natural product, invented provider report or new quotation was introduced. The original provider report and artifacts remain unchanged.

See the [integrated source guide](FBXL4-source-guide.md) for the primary/database evidence links and explicit source limits.

## 2026-10-26 — feedback adjudication

The ten Reactome cytosol rows now use MARK_AS_OVER_ANNOTATED. Their actual routes and explicit target-entity cytosol field remain recorded; the issue is overextension of a generic ligase-set compartment model, not missing target membership or proof that FBXL4 can never occupy a cytosolic pool. DefinedSet 976085, CandidateSet 976075 and SCF Complex 976110 retain their actual types. The historical intermembrane-space source remains UNDECIDED.

The TPP1 and DNM2 binding refinements remain MODIFY. Their official definitions concern binding itself, without effector/regulatory or physiological claims. Original Table S2 and six positive IntAct records support the exact pairs; the inherited abstract quotations are retained unchanged as study context and are not presented as pair-specific support. Missing target DULIP confirmation, unresolved insert boundaries and the lack of a mapped mature TPP1 chain remain explicit.

The two still-open questions on additional SCF-FBXL4 substrates and direct-versus-secondary DRP1/fission effects are restored verbatim from the original review. Description/core prose now states biology directly, including the curated MTDPS13 context and the already-supported mouse Bnip3/Nix rescue. All source objects, reference objects and 60 inherited quotations retain exact paths/text/reference associations. The prior journal remains intact. Status remains DRAFT because of the inherited provider-citation advisory; this is not a new incomplete scientific task or a fabricated provider citation.
