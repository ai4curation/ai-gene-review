# PIGY (Q3MUY2) review notes

## Summary of gene function

PIGY / PIG-Y (phosphatidylinositol N-acetylglucosaminyltransferase subunit Y, HGNC:28213,
UniProtKB:Q3MUY2) is a small (71 aa), two-transmembrane-domain ER membrane protein that is
the seventh identified component of the glycosylphosphatidylinositol N-acetylglucosaminyl-
transferase (GPI-GnT) complex. This complex catalyses the first, committed step of GPI-anchor
biosynthesis: transfer of GlcNAc from UDP-GlcNAc onto phosphatidylinositol to give GlcNAc-PI.

- Defining paper: Murakami et al. 2005 (PMID:16162815), abstract-only in cache
  (`full_text_available: false`).
  - [PMID:16162815 "Here, we report that human GPI-GnT requires another component, termed
    PIG-Y, a 71 amino acid protein with two transmembrane domains."]
  - [PMID:16162815 "PIG-Y appeared to be directly associated with PIG-A, implying that PIG-Y
    is the key molecule that regulates GPI-GnT activity by binding directly to the catalytic
    subunit PIG-A."]
  - [PMID:16162815 "We did not obtain evidence for a functional linkage between GPI-GnT and ras
    GTPases in mammalian cells as has been reported for yeast cells."] -> explicitly argues
    against a Ras/GTPase functional role.
  - [PMID:16162815 "A complex of six components was formed without PIG-Y."] -> PIG-Y is a
    required accessory/regulatory subunit, not part of the catalytic minimal core assembly.

- UniProt (Q3MUY2):
  - FUNCTION: "Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT)
    complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to
    phosphatidylinositol and participates in the first step of GPI biosynthesis... May act by
    regulating the catalytic subunit PIGA."
  - SUBUNIT: "Component of the ... (GPI-GnT) complex composed at least by PIGA, PIGC, PIGH, PIGP,
    PIGQ, PIGY and DPM2. Interacts directly with PIGA; this interaction regulates ... activity.
    Does not interact with Ras proteins."
  - SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane; Multi-pass membrane protein."
  - Topology: cytoplasmic 1-3, TM 4-26, lumenal 27-44, TM 45-65, cytoplasmic 66-71.
  - DISEASE: HPMRS6 (Hyperphosphatasia with impaired intellectual development syndrome 6),
    MIM:616809; variant L46P (PMID:26293662).
  - PATHWAY: Glycolipid biosynthesis; GPI-anchor biosynthesis (UniPathway UPA00196).

- Disease: Ilkovski et al. 2015 (PMID:26293662; not cached) established PIGY variants cause an
  inherited GPI-deficiency disorder (GPIBD) in the hyperphosphatasia / epileptic encephalopathy
  spectrum. L46P diminishes protein expression/stability and reduces cell-surface expression of
  GPI-anchored proteins CD55 and CD59.

## Annotation-by-annotation notes

GOA (`PIGY-goa.tsv`) carries 15 data rows across these terms:

- GO:0000506 GPI-GnT complex (CC, part_of): IBA (GO_REF:0000033), IPI (PMID:16162815, ComplexPortal),
  IDA (PMID:16162815, MGI). All ACCEPT — core, directly established.
- GO:0006506 GPI anchor biosynthetic process (BP): IBA (GO_REF:0000033, involved_in), IEA
  (GO_REF:0000041 UniPathway, involved_in), IDA (PMID:16162815, acts_upstream_of_or_within). ACCEPT
  — core BP.
- GO:0005789 endoplasmic reticulum membrane (CC, located_in): IEA (GO_REF:0000044 SubCell), IDA
  (PMID:16162815 x2, ComplexPortal + MGI), TAS (Reactome R-HSA-162730). ACCEPT — core location.
- GO:0017176 phosphatidylinositol N-acetylglucosaminyltransferase activity (MF, contributes_to):
  IDA (PMID:16162815, BHF-UCL). ACCEPT — PIGY is non-catalytic but `contributes_to` correctly
  captures its required contribution to the complex's catalytic activity.
- GO:0005515 protein binding (MF, enables): IPI, PMID:16162815 (PIGA/P37287) and PMID:32296183
  (HuRI: TMEM72/A0PK05, ERG28/Q9UKR5). Uninformative bare `protein binding` per curation policy ->
  MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPI). The PIGA interaction is biologically the
  key one (direct, regulatory) but the GO term itself conveys nothing; the informative MF is captured
  by contributes_to GO:0017176. HuRI interactors (TMEM72, ERG28) are high-throughput Y2H hits without
  established biological meaning for PIGY.
- GO:0005886 plasma membrane (CC, located_in): IDA (PMID:16162815, MGI). PIGY is an ER-membrane GPI
  biosynthesis subunit; the abstract localises it to ER. Plasma membrane is inconsistent with an ER
  GPI-GnT subunit and with the UniProt SUBCELLULAR LOCATION (ER membrane only). This IDA likely
  reflects a transfected/overexpression artefact or mislocalisation readout. Full text not in cache
  (abstract-only), so per policy do NOT REMOVE an experimental annotation whose full text is
  unverifiable -> MARK_AS_OVER_ANNOTATED (not core; ER is the established site).

## Core functions
- MF: contributes_to phosphatidylinositol N-acetylglucosaminyltransferase activity (GO:0017176) as a
  required non-catalytic subunit of the GPI-GnT complex.
- BP: GPI anchor biosynthetic process (GO:0006506).
- CC / complex: ER membrane (GO:0005789); part of GPI-GnT complex (GO:0000506).

## Provenance
- No falcon deep-research file (falcon out of credits, HTTP 402). Review grounded in UniProt
  (`PIGY-uniprot.txt`), GOA (`PIGY-goa.tsv`), cached PMID:16162815 abstract, Reactome R-HSA-162730,
  and PMID:32296183 (HuRI) metadata.
