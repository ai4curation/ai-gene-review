# MASTL (Greatwall kinase, Q96GX5) - curation notes

## Identity
- HGNC symbol MASTL; aliases GW, GWL, hGWL, THC2, FLJ14813. Atypical AGC-family Ser/Thr kinase
  (879 aa) with a >500-residue insertion splitting the catalytic domain; AGC C-terminal domain
  836-879; ATP-binding 41-49/Lys62; catalytic Asp156 [file:human/MASTL/MASTL-uniprot.txt].
- Established as the functional human Greatwall orthologue by two 2010 RNAi studies
  [PMID:20538976 "Here we show that the functional human ortholog of Greatwall protein kinase (Gwl) is the microtubule-associated serine/threonine kinase-like protein, MAST-L."]
  [PMID:20818157 "Here, we describe the human orthologue of Gwl called microtubule-associated serine/threonine kinase-like (MASTL)."].
- Not to be confused with MAST1-4 (PDZ-domain MAST kinases), Drosophila MAST/Orbit, or yeast Rim15
  (a divergent family member with nutrient-stress roles) - see deep research identity section.

## Core mechanism (high confidence)
- Activated at mitotic entry by cyclin B-CDK1 (Thr741; UniProt "Phosphorylation at Thr-741 by CDK1 during M phase activates its kinase activity") and autophosphorylation (Ser875, Reactome R-HSA-2465910).
- Substrates: ENSA Ser67 and ARPP19 Ser62. Phospho-endosulfines bind and inhibit PP2A-B55
  [PMID:21164014 "We identified cyclic adenosine monophosphate-regulated phosphoprotein 19 (Arpp19) and α-Endosulfine as two substrates of Gwl that, when phosphorylated by this kinase, associate with and inhibit PP2A, thus promoting mitotic entry."]
  [PMID:21164013 "This converts Ensa into a potent and specific inhibitor of PP2A-B55δ."]
  [PMID:38123684 "This inhibition results in the full activation of mitotic kinases, including MASTL, which phosphorylates ARPP19 on Ser62 (pS62-ARPP19)."].
- Cryo-EM of PP2A:B55-pARPP19 (2024) shows pSer62 occupying the catalytic site ("unfair competition"
  substrate-inhibitor); ARPP19 "strictly requires phosphorylation by MASTL kinase to inhibit PP2A:B55" [PMID:38123684].
- Consequence in human cells: full depletion -> G2 arrest; partial depletion -> prometaphase delay,
  premature CDK substrate dephosphorylation, SAC failure, cytokinesis defects; rescued by PP2A
  co-depletion or okadaic acid
  [PMID:20538976 "The complete depletion of Gwl by siRNA arrests human cells in G2."]
  [PMID:20538976 "These phenotypes appear to be mediated by PP2A, as they could be rescued by either a double Gwl/PP2A knockdown or by the inhibition of this phosphatase with okadaic acid."]
  [PMID:20818157 "Cells strongly depleted of MASTL by RNAi delay in G(2) phase and reveal slow chromosome condensation."]
  [PMID:20818157 "This causes chromatin to be trapped in the cleavage furrow, which may lead to the formation of 4N G(1) cells by cytokinesis failure."].
- Reactome models the two human reactions (R-HSA-2168079 ARPP19 S62; R-HSA-2430535 ENSA S67) and the
  pathway R-HSA-2465910. The repository module `modules/g2_m_transition.yaml` carries the
  Greatwall-endosulfine axis as an optional part; this review is consistent with it.

## Localization
- Interphase: nuclear [PMID:20818157 "We found that MASTL localizes to the nucleus in interphase and re-localizes in part to centrosomes in mitosis, when it is active."]
  [PMID:19460416 "The MASTL kinase protein, both wildtype and mutant forms, appears to localize within the nucleus of these BHK cells (Figure 6, Panels A & B) as determined by co-localization with the DNA counterstain, TO-PRO-3."]; HPA IF: nucleoplasm.
- After NEBD: cytoplasm and centrosomes; mitotic exit: cleavage furrow
  [file:human/MASTL/MASTL-uniprot.txt "During interphase is mainly nuclear, upon nuclear envelope breakdown localizes at the cytoplasm and during mitosis at the centrosomes. Upon mitotic exit moves to the cleavage furrow."].
- Added a NEW cytoplasm (GO:0005737) annotation because the endosulfine phosphorylation that matters
  for mitosis happens in the mitotic cytoplasm, and no existing CC term covers it.

## Secondary / context-dependent roles
- DNA damage checkpoint recovery: Xenopus Gwl is inhibited by the DDR and promotes recovery
  (source of the human ISS to GO:0006974); UniProt: "Following DNA damage, it is also involved in checkpoint recovery by being inhibited." Kept as non-core: it is the same G2/M-promoting activity applied after checkpoint release.
- Thrombocytopenia (THC2): E167D segregates with autosomal dominant thrombocytopenia in one pedigree;
  zebrafish morpholino knockdown reduces thrombocytes
  [PMID:19460416 "A transient knockdown of MASTL in zebrafish results in deficiency of circulating thrombocytes."].
  Mouse E166D knock-in (Hurtado et al. 2018, JCI; summarised in deep research) behaves as a
  gain-of-PP2A-suppression allele affecting platelet actin dynamics. Not annotated in GOA; no NEW proposed.
- Kinase-independent MRTF-A/SRF contractility signalling (Taskinen et al. 2020, JCB; deep research)
  - single-lab, cell-based; not proposed as an annotation.

## Annotation decisions (summary)
- ACCEPT: G2/M transition (IMP x2), Ser/Thr kinase activity (IBA/IDA/IEA/TAS x2), protein kinase
  activity and protein serine kinase activity (IEA), ATP binding, nucleus (EXP/IBA/IDA x2/IEA),
  nucleoplasm (IDA/TAS x2), centrosome (IDA/IEA), regulation of mitotic cell cycle (IBA/TAS),
  microtubule cytoskeleton (IBA), cleavage furrow (IDA x2/IEA).
- MODIFY: GO:0016301 kinase activity (IDA) -> GO:0004674; GO:0051726 regulation of cell cycle (IMP)
  -> GO:0007346 regulation of mitotic cell cycle (all phenotypes are mitotic).
- KEEP_AS_NON_CORE: GO:0006974 DNA damage response (ISS from Xenopus); GO:0035556 intracellular
  signal transduction (deep AGC-node IBA; true but generic).
- MARK_AS_OVER_ANNOTATED: GO:0051721 protein phosphatase 2A binding (ISS from Xenopus co-IP data that
  predate the endosulfine mechanism; UniProt: MASTL "does not directly inhibit PP2A but acts by
  mediating phosphorylation and subsequent activation of ARPP19 and ENSA").
- REMOVE: GO:0044325 transmembrane transporter binding (IEA, Ensembl Compara from mouse Mastl IPI with
  Slc12a6/KCC3; the mouse source paper PMID:27782176 is listed as retracted on PubMed; no human
  evidence, no connection to known biology).
- NEW: GO:0005737 cytoplasm (IDA, PMID:20818157 via UniProt subcellular location note).

## Open questions
- Whether human MASTL binds PP2A-B55 directly (vs. via phospho-endosulfines).
- Whether E167D acts via altered ENSA/ARPP19 phosphorylation in megakaryocytes.
- Whether any direct mitotic substrates beyond ENSA/ARPP19 exist in human cells.
