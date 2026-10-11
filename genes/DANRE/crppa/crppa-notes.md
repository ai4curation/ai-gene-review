# Notes for DANRE crppa

- Core function is CDP-ribitol production for dystroglycan-linked O-mannosyl glycosylation [file:DANRE/crppa/crppa-uniprot.txt "Catalyzes the formation of CDP-ribitol"].
- The old isoprenoid-biosynthetic-process annotation is removed because the MEP pathway context is absent in vertebrates [PMID:22522421 "MEP) pathway, which is absent in vertebrates"].
- Brain and muscle development annotations are retained as non-core phenotypic consequences of defective alpha-dystroglycan glycosylation.

## Re-review 2026-09-28

Full re-review of all 20 GOA rows against the cached primary literature; the earlier
templated summaries ("consistent with the synthesized gene function") were replaced with
row-specific arguments.

- Added two primary references that define the enzyme: Gerin et al. 2016 (PMID:27194101,
  full text) showing recombinant mammalian ISPD is a CDP-ribitol pyrophosphorylase with no
  activity on the MEP substrate [PMID:27194101 "No activity was observed in the presence of
  UTP, or in the presence of CTP and 2-C-methyl-D-erythritol-4-P, which is the substrate
  utilized in related enzymes in the mevalonate pathway."] and that FKTN/FKRP use the
  product [PMID:27194101 "both recombinant fukutin (FKTN) and fukutin-related protein
  (FKRP) can transfer a ribitol phosphate group from CDP-ribitol to α-dystroglycan"]; and
  Riemersma et al. 2015 (PMID:26687144, abstract only) for cytosolic localization and the
  cytidyltransferase domain of human ISPD [PMID:26687144 "Functional studies demonstrated
  cytosolic localization of hISPD, and cytidyltransferase activity toward pentose
  phosphates"]. A first attempt to cache the Riemersma paper hit a wrong PMID (26055709 is a
  PDE12 paper); the correct id was found by PubMed search and only 26687144 is cited.
- Three PENDING rows resolved: GO:0009101 glycoprotein biosynthetic process (IEA, ARBA)
  -> MODIFY to GO:0035269, the specific descendant already carried by IBA/IMP; the second
  GO:0010559 IGI row (ispd MO1 x fkrp MO) -> MODIFY to GO:0035269, matching the fktn IGI
  and IMP rows; the second GO:0055001 IMP row (ispd MO2) -> KEEP_AS_NON_CORE, matching
  the MO1 row [PMID:22522421 "Injection of ispd MO2 (3 ng) caused similar morphological
  abnormalities, assuring the specificity of both MOs"].
- The three GO:0010559 "regulation of glycoprotein biosynthetic process" rows stay MODIFY
  -> GO:0035269: the definition of GO:0010559 is a process that modulates the rate of
  glycoprotein biosynthesis, whereas crppa is a pathway enzyme that performs a step
  (donor synthesis), so the evidence supports participation, not regulation
  [PMID:22522421 "These results support a cooperative interaction between ispd and
  fktn/fkrp in αDG glycosylation."].
- GO:0008299 isoprenoid biosynthetic process (IEA, InterPro) stays REMOVE, now with the
  direct enzymatic exclusion from Gerin 2016 in addition to the absence of the MEP pathway
  in vertebrates [PMID:22522421 "In plants, protozoa and some bacteria, ISPD belongs to
  the non-mevalonate isoprenoid biosynthesis (MEP) pathway, which is absent in
  vertebrates"].
- Brain morphogenesis and muscle cell development IMP rows stay KEEP_AS_NON_CORE: the
  phenotypes are penetrant and specific but downstream of alpha-dystroglycan
  hypoglycosylation [PMID:22522421 "loss of Ispd function in zebrafish results in αDG
  hypoglycosylation and compromised sarcolemma integrity, preceding muscle fiber
  degeneration"].
- Cytosol rows (IBA/IEA/ISS) are now supported by the human localization experiment rather
  than the FUNCTION line. Protein homodimerization (ISS) remains KEEP_AS_NON_CORE with only
  the by-similarity SUBUNIT line as support.
- Description rewritten as standalone biology; reference_review added to every PMID;
  core_functions re-supported with primary quotes; two suggested questions and
  experiments added (direct assay of zebrafish Crppa; ribitol rescue in a mutant line).
- Validation: zero errors.
