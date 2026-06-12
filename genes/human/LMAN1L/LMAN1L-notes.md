# LMAN1L (Q9HAT1) — review notes

## Summary

LMAN1L (gene synonym ERGL; "Protein ERGIC-53-like" / "Lectin mannose-binding 1-like"; ORFNames UNQ2784/PRO7174) is a human paralog of LMAN1/ERGIC-53. It is a 526-aa single-pass type I membrane glycoprotein of the L-type lectin family. It was originally cloned by Yerushalmi et al. as a novel gene related to ERGIC-53 that is highly expressed in normal and neoplastic prostate [PMID:11255007, via file:human/LMAN1L/LMAN1L-uniprot.txt "ERGL, a novel gene related to ERGIC-53 that is highly expressed in normal and neoplastic prostate and several other tissues."].

**Key caveat for the review:** There is essentially NO experimental functional characterization of LMAN1L's lectin activity or transport role in human (or any organism). UniProt evidence level is PE 2 ("Evidence at transcript level"). Almost all GO annotations are IBA (phylogenetic/PANTHER-propagated from the L-type lectin / ERGIC-53 family) or IEA (electronic: InterPro, UniProtKB-SubCell, ARBA). The single experimental annotation is an HDA mass-spectrometry detection in an extracellular-matrix proteomics dataset.

## Domain / family architecture (UniProt, file:human/LMAN1L/LMAN1L-uniprot.txt)

- Family / lectin assignment via domains:
  - DOMAIN 31..252 "L-type lectin-like" (ECO:0000255|PROSITE-ProRule:PRU00658)
  - InterPro IPR013320 ConA-like_dom_sf; IPR005052 Lectin_leg; IPR051136 Intracellular_Lectin-GPT
  - Pfam PF03388 Lectin_leg-like; PROSITE PS51328 L_LECTIN_LIKE
  - PANTHER PTHR12223 "VESICULAR MANNOSE-BINDING LECTIN" / subfamily SF31 "PROTEIN ERGIC-53-LIKE"
  - Keyword "Lectin"
- Topology: SIGNAL 1..25; TOPO_DOM 26..462 Lumenal; TRANSMEM 463..483 Helical; TOPO_DOM 484..526 Cytoplasmic — i.e. a single-pass type I membrane protein with a lumenal lectin domain and short cytoplasmic tail, consistent with a cargo-receptor topology like ERGIC-53.
- N-glycosylation site at N75; disulfide 176..215. Keyword "Glycoprotein".

These domain features are the defensible basis for inferring a **mannose-binding L-type lectin** function by homology — but no direct sugar-binding assay exists for LMAN1L.

## Subcellular location (UniProt, by similarity)

- SUBCELLULAR LOCATION: "Endoplasmic reticulum-Golgi intermediate compartment membrane" {ECO:0000250}; "Single-pass type I membrane protein" {ECO:0000250}.
- ECO:0000250 = inferred by sequence/structural similarity (not experimental). So the ERGIC membrane localization is a homology inference from ERGIC-53/LMAN1, not direct evidence for this paralog.

## Tissue specificity (UniProt; PMID:11255007)

- TISSUE SPECIFICITY: "Highly expressed in normal and neoplastic prostate. Also expressed in cardiac atrium, salivary gland, spleen and selective cells in the CNS." {ECO:0000269|PubMed:11255007}.
- HPA: "Group enriched (brain, heart muscle, lymphoid tissue, prostate, salivary gland)." Consistent with a tissue-restricted (prostate/testis-style) paralog rather than the ubiquitous LMAN1.

## Pathway / interaction context (UniProt cross-refs, not direct functional evidence)

- Reactome R-HSA-204005 "COPII-mediated vesicle transport"; R-HSA-5694530 "Cargo concentration in the ER" — these are family/pathway placements consistent with an ERGIC-53-like cargo receptor, but are inference-based.
- PAN-GO: "6 GO annotations based on evolutionary models" — i.e. the GO function set is phylogenetic.

## Extracellular matrix proteomics (only experimental annotation)

- GO:0031012 extracellular matrix, HDA, PMID:28675934 (BHF-UCL).
- In Naba et al. 2017, LMAN1L was detected only in the urea-insoluble pellet fraction of decellularized TNBC-adjacent breast tissue: [PMID:28675934 "only four proteins were detected solely in the pellet and not in either urea-soluble or crude ECM preparations (namely, AMBP and LMAN1L, which is, in fact, a transmembrane protein in TNBC-adjacent breast tissue and COL6A5 and MFAP2 in TNBC samples)"].
- The authors explicitly note LMAN1L "is, in fact, a transmembrane protein" — i.e. it is a contaminant/peripheral co-isolate of an ECM-enrichment protocol, not a bona fide secreted ECM component. This supports KEEP_AS_NON_CORE (peripheral proteomics detection), not a core extracellular function.

## Review disposition rationale

- D-mannose binding (GO:0005537, IBA): homology/IBA-based only; the L-type lectin domain is present, but no direct binding assay for LMAN1L → KEEP_AS_NON_CORE.
- ER-to-Golgi transport machinery localizations (ERGIC, ERGIC membrane, ER membrane, Golgi membrane, COPII vesicle; IBA/IEA): plausible by homology to ERGIC-53 but unverified for this paralog → KEEP_AS_NON_CORE; UniProt SUBCELLULAR LOCATION (ECO:0000250) supports the ERGIC membrane localization specifically.
- ER-to-Golgi vesicle-mediated transport (GO:0006888, IBA, BP): same — homology-plausible, unverified → KEEP_AS_NON_CORE.
- Generic membrane (GO:0016020, IEA) and endomembrane system (GO:0012505, IEA): uninformative parents → MARK_AS_OVER_ANNOTATED.
- Extracellular matrix (GO:0031012, HDA): peripheral proteomics co-isolate → KEEP_AS_NON_CORE.

No catalytic (mannosidase) activity should be assigned — LMAN1L is a lectin (carbohydrate-binding), not a glycosidase.

## Core function (cautious)

The only defensible synthesized statement is a homology-based prediction: LMAN1L is predicted to be a mannose-binding L-type lectin / ERGIC-resident type I membrane cargo receptor of the ERGIC-53/LMAN1 family, likely acting in ER-to-Golgi (COPII) cargo transport, but this is entirely inferred from family membership and domain architecture; direct functional evidence is lacking.

## Falcon deep-research findings (incorporated 2026-06)

The Falcon (Edison Scientific) deep-research report for LMAN1L returned **no gene-specific experimental literature**; it explicitly states "direct experimental studies on human LMAN1L/Q9HAT1 were not accessible" and that "no primary study directly characterizes LMAN1L's cargo, binding partners, or subcellular localization." All mechanistic content is **paralog-inferred from LMAN1/ERGIC-53**. No new LMAN1L-specific references were added to the review.

- **(Paralog-inferred, NOT LMAN1L-specific)** Family-membership framing: LMAN1L is named as a distinct member of the animal L-type lectin family (LMAN1/ERGIC-53, LMAN1L, LMAN2/VIP36, LMAN2L/VIPL) [Baines & Zhang 2007, DOI:10.1016/j.tibs.2007.06.006 "LMAN1L ... animal L-type lectin family"]. This is consistent with the existing review's family/domain inference; adds nothing new.
- **(Paralog-inferred)** Recent mechanistic framework for cargo receptors (Ca2+/pH-dependent glycan capture/release across the ER→ERGIC→Golgi gradient) is drawn entirely from LMAN1 [Zhang, Srivastava & Zhang 2023, DOI:10.1042/bst20220713]. Not direct LMAN1L evidence; supports the existing homology-based "predicted mannose-binding cargo receptor" framing only.
- **(Paralog-inferred)** 2024 cryo-EM structure of full-length ERGIC-53/LMAN1 in complex with MCFD2 (tetramer, clover-like head, coiled-coil stalk) [Watanabe et al. 2024, Nat Commun, DOI:10.1038/s41467-024-46747-1] is offered only as a *structural analog* for LMAN1L; it does not contain LMAN1L data.
- **(Database-level only, not promoted)** Falcon cites OpenTargets trait associations for LMAN1L (hypertension, alcohol drinking, osteoarthritis, hip OA, pregnancy-induced hypertension). These are aggregated GWAS/association signals, hypothesis-generating only, with no mechanistic link to LMAN1L function; NOT added as references or annotations.
- **Net effect on review:** none. Falcon reaffirms that LMAN1L remains characterized at the transcript level only (PE 2), with all functional roles homology-inferred. No YAML changes; existing KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED dispositions stand.
