# NPHP4 (nephrocystin-4 / nephroretinin, O75161) review notes

## Deep research status
- Falcon was run with `--fallback perplexity-lite` (600 s; fallback not available here), then rerun with `--timeout 2400`; the outcome is at the bottom of this file. The review rests on cached primary literature.

## Key literature
- Gene identification [PMID:12244321 "We identified five different mutations in one of these genes, designated NPHP4, in unrelated individuals with nephronophthisis."]; [PMID:12205563 "NPHP4 encodes a novel protein, nephroretinin, that is conserved in evolution"].
- Basal body/centrosome [PMID:15661758 "nephrocystin-4 also localizes to the primary cilia in polarized epithelial tubular cells, particularly at the basal bodies"].
- Bridge/adaptor in the 1-4-8 module [PMID:21565611 "We find that NPHP4 directly binds both NPHP1 and NPHP8 in vitro, and can bridge the interaction between NPHP1 and NPHP8, whereas NPHP1 and NPHP8 do not appear to bind directly"].
- Distal TZ barrier (Chlamydomonas) [PMID:25150219 "NPHP4 is stably incorporated into the distal part of the flagellar transition zone, close to the membrane and distal to CEP290"]; [PMID:25150219 "NPHP4 functions at the transition zone as an essential part of a barrier that regulates both membrane and soluble protein composition of flagella."].
- Worm TZ assembly with the MKS module [PMID:21422230 "mks-6;nphp-4 and mks-5;nphp-4 double mutants exhibit mispositioned and disrupted TZ regions, with clear disconnections between the BB/TZ region and membrane, accompanied by missing Y-links"].
- Upstream of NPHP1 [PMID:26982032 "NPHP-1 requires NPHP-4 for assembly at the TZ"]; [PMID:21357692 "NPHP4 acts upstream of NPHP1 and regulates the localization of NPHP1 at the ciliary base."].
- Mouse: retinal degeneration and male infertility, no cysts [PMID:28401750 "an NPHP4 mutant mouse developed retinal degeneration but not kidney cysts nor severe ciliogenesis defects"].
- Wnt [PMID:22654112 "NPHP4 and Jade-1 additively inhibit canonical Wnt signaling"]; Hippo (not in GOA) [PMID:21555462 "(c) NPHP4 enhances the activity of the transcriptional coactivators TAZ and YAP."]; actin [PMID:26644512 title "The polarity protein Inturned links NPHP4 to Daam1 to control the subapical actin network in multiciliated cells."].
- Photoreceptors: RPGRIP1-dependent targeting [PMID:22825473 "Selective loss of RPGRIP1-dependent ciliary targeting of NPHP4, RPGR and SDCCAG8 underlies the degeneration of photoreceptor neurons."].
- Newer: VZV restriction factor [PMID:40739040 "Rare variant analysis in patients with VZV CNS infection identifies a mutation in the restriction factor NPHP4."]. Not annotated; raised as a question.

## Curation decisions (62 GOA rows + 1 NEW)
- Protein binding: 2 MODIFY (Sang et al. NPHP1 and RPGRIP1L rows) to GO:0030674 protein-macromolecule adaptor activity; 23 REMOVE.
- NAS rows citing PMID:12006559 (an NPHP1-only paper): structural molecule activity REMOVE; actin cytoskeleton organization KEEP_AS_NON_CORE (independently supported by PMID:26644512); cell-cell adhesion MARK_AS_OVER_ANNOTATED. Visual behavior NAS REMOVE; signal transduction MARK_AS_OVER_ANNOTATED.
- Ribbon synapse (IEA from mouse): UNDECIDED. The source mouse paper is not cached.
- Wnt (IBA/IDA/IEA), junctions, nucleus, centrosome: KEEP_AS_NON_CORE.
- NEW GO:1905349 (ISS from worm/Chlamydomonas data, PMID:21422230).

## HPA cilium atlas vs module role
- HPA (member_evidence.md): no cilium/centrosome call; HPA main location "Nucleoplasm". Hansen et al. 2025 atlas [PMID:41005307 "We found that 69% of the ciliary proteome is cell-type specific, and 78% exhibited single-cilia heterogeneity."]. The HPA antibody did not detect NPHP4 at cilia in the three atlas cell lines. The nucleoplasm call is interesting given the reported nuclear pool (JADE1, TAZ; PMID:22654112, PMID:21555462), but it may also be antibody background. Absence of a ciliary call does not contradict the strong TZ evidence across species (low-abundance TZ proteins are often missed).
- Module role: NPHP module component; "transition zone scaffold"; TZ assembly. Among the NPHP-module genes NPHP4 fits the scaffold label best (adaptor that bridges NPHP1 and RPGRIP1L; needed for NPHP1 TZ recruitment; with the MKS module needed for Y-links). core_functions follow the module, with protein-macromolecule adaptor activity as the MF and GO:1905349 as the process.
