# USH2A (usherin, O75445) — curation notes

## 2026-09-04 — annotation review pass (all GOA lines)

### Gene overview (wild-type function)

- USH2A encodes usherin, a very large protein with two principal isoforms: a short
  ~1546-aa secreted/extracellular form (isoform A; UniProt isoform 2, "Secreted")
  and a long ~5202-aa single-pass type I transmembrane form (isoform b; UniProt
  isoform 1, displayed). The long isoform carries a huge ectodomain (laminin
  N-terminal, laminin EGF-like, laminin G-like and ~35 fibronectin III repeats), a
  single TM segment, and a short cytoplasmic tail ending in a class-I PDZ-binding
  motif (DTHL) [PMID:36964137 "both USH2A and ADGRV1 are transmembrane adhesion proteins that form extracellular linkages"].
- Core function 1 (inner ear): component of the transient ankle links that connect
  the basal regions of stereocilia in DEVELOPING cochlear hair bundles; part of the
  ankle-link/USH2 complex with ADGRV1, WHRN and PDZD7. Ankle links exist only
  transiently during bundle development in mouse (~P2–P12) [PMID:36964137 "Temporally, they only exist during the P2 to P12 stages during stereociliary development"]
  and the four proteins form the ankle link complex [PMID:36964137 "WHRN, PDZD7, ADGRV1 and USH2A have been identified to form the so-called ankle link complex (ALC)"].
  Assembly is driven by PDZ/PBM multivalent interactions and liquid–liquid phase
  separation [PMID:36964137 "WHRN and PDZD7 orchestrate ADGRV1 and USH2A to assemble the ALC through liquid-liquid phase separation (LLPS)"].
- Core function 2 (retina): the long isoform localizes to the periciliary membrane
  compartment of the photoreceptor apical inner segment, surrounding the connecting
  cilium, as part of the same USH2 complex; loss causes retinitis pigmentosa, i.e.
  failure of photoreceptor maintenance (UniProt CC FUNCTION, from mouse Q2QI47;
  human IMP from USH2A patients, e.g. 2314delG [PMID:10090909 title]).
- USH2 quaternary complex biochemistry: WHRN and PDZD7 are both required to
  assemble USH2A and GPR98/ADGRV1 into a quaternary complex; WHRN preferentially
  binds USH2A [PMID:25406310 "both WHRN and PDZD7 are required for the complex formation with USH2A and GPR98. In this USH2 quaternary complex, WHRN prefers to bind to USH2A"].
- PDZ-scaffold binding by the cytoplasmic tail: whirlin directly associates with
  USH2A isoform b [PMID:16434480 "whirlin directly associates with USH2A isoform b and VLGR1b"];
  PDZD7 PDZ1/PDZ2 co-immunoprecipitate with USH2A and the interaction requires the
  C-terminal PDZ-binding motif [PMID:20440071 "the first and second PDZ domains of PDZD7 interact with USH2A by coimmunoprecipitation studies"; "A truncated version of USH2A without the C-terminal PDZ-binding motif showed reduced interaction"].
  These IPI "protein binding" annotations are better captured as GO:0030165 PDZ
  domain binding.
- Basement membrane pool (largely the short secreted isoform A): usherin was
  originally described as a basement membrane protein of many epithelia and of
  Bruch's membrane [PMID:12433396 "Usherin is a basement membrane protein encoded by the USH2A gene"],
  and its laminin EGF (LE) domain binds the 7S domain of collagen IV with 1:1
  stoichiometry; USH2A missense mutations in LE loop b abolish binding
  [PMID:14676276 "binding occurs between the LE domain of usherin and the 7S domain of type IV collagen"].
  The matrisome proteomics resource lists usherin among ECM/basement-membrane
  glycoproteins (HDA, PMID:22159717; USH2A itself is only in the supplementary
  matrisome lists, not the cached body text). I treat the basement-membrane /
  collagen-binding annotations as real but NON-CORE relative to the ankle-link /
  periciliary functions that explain the Usher 2A phenotype.
- Disease: biallelic USH2A variants cause Usher syndrome type 2A (congenital
  moderate hearing loss + RP) and nonsyndromic RP39. Human IMP annotations for
  sensory perception of sound/light from patient studies (e.g. PMID:10090909,
  abstract-only cache — a letter reporting high prevalence of 2314delG with
  deaf-blind phenotype) are acceptable.

### Publication-access notes

- Abstract-only caches: PMID:10090909 (letter; no abstract text beyond title),
  PMID:14676276, PMID:12433396, PMID:16434480, PMID:15671307, PMID:31644917.
- Full text cached: PMID:20440071, PMID:22159717, PMID:25406310, PMID:36964137.
- PMID:31644917 (He/Li/Zhang 2019 Cell Rep, LLPS of MYO7A/MYO7B–USH1C–ANKS4B/USH1G
  tip-link density complexes) is cited by BHF-UCL for three USH2A annotations
  (stereocilia ankle link IDA, apical plasma membrane TAS, myosin binding IPI with
  MYO7B/Q6PIF6). The cached abstract does not mention USH2A and no PMC full text
  exists (no PMCID). Per project policy I do not overrule the curator from an
  abstract: the asserted location (ankle link) and activity class (myosin binding
  via the MyTH4-FERM interaction surface; UniProt SUBUNIT lists a MYO7A MyTH4-FERM
  interaction by similarity) are consistent with everything else known about
  usherin, so these are ACCEPTed with the caveat recorded in the review reasons.
- PMID:22159717 (matrisome) cached full text does not name USH2A (it is in the
  supplementary tables), so no verbatim supporting quote is attached to the HDA
  annotation.

### Term-level judgments made

- GO:0005515 protein binding (IPI x2) → MODIFY to GO:0030165 PDZ domain binding
  (both papers map the interaction to PDZ domains ↔ USH2A PBM).
- GO:0048496 maintenance of animal organ identity (IMP, PMID:15671307) → MODIFY to
  GO:0045494 photoreceptor cell maintenance. The paper documents progressive
  photoreceptor disease ("thinning of the outer nuclear layer") in USH2A patients;
  "organ identity" is a developmental-identity concept that does not describe
  retinal degeneration. Legacy term choice, not evidence problem.
- GO:0045184 establishment of protein localization (ISS from mouse) → MODIFY to
  GO:0072659 protein localization to plasma membrane (usherin is required for
  normal localization/retention of its USH2 partners at the stereociliary base and
  periciliary membrane; the generic parent is uninformative).
- GO:0032391 photoreceptor connecting cilium, located_in (IEA) → MODIFY toward
  GO:1990075 periciliary membrane compartment: usherin surrounds the connecting
  cilium in the periciliary membrane of the apical inner segment rather than being
  part of the ciliary shaft; the ISS annotation with colocalizes_with qualifier is
  appropriately hedged and is ACCEPTed as-is.
- GO:0042802 identical protein binding (IEA via Ensembl from mouse) →
  MARK_AS_OVER_ANNOTATED: no human evidence for a functionally meaningful
  homomeric interaction; uninformative term.
- GO:0005737 cytoplasm (IDA, PMID:16434480) → MARK_AS_OVER_ANNOTATED: usherin is a
  type I membrane / secreted protein; cytoplasmic staining in that study most
  plausibly reflects biosynthetic/vesicular pools or heterologous expression, and
  "cytoplasm" carries no functional information for this protein.
- GO:0043025 neuronal cell body, GO:0043195 terminal bouton (ISS colocalizes_with)
  → KEEP_AS_NON_CORE: derived from van Wijk 2006-era synaptic colocalization
  [PMID:16434480 "These proteins co-localize with whirlin at the synaptic regions of both photoreceptor cells and outer hair cells in the cochlea"];
  later KO-validated localization studies of the mouse USH2 complex concentrate on
  ankle links and the periciliary membrane, so the synaptic pool is kept but not
  treated as core.
- GO:0036064 ciliary basal body (IEA from mouse) → KEEP_AS_NON_CORE: periciliary /
  basal-body-adjacent localization reported for USH2 proteins in photoreceptors;
  not the defining compartment.
- Basement-membrane cluster (GO:0005604 IEA+IDA, GO:0140144 HDA, GO:0005576 IEA,
  GO:0005518 collagen binding IEA+IDA) → KEEP_AS_NON_CORE (see above; strongest
  relevance to secreted isoform A/Bruch's membrane; GO:0005576 maps to the
  UniProt "Secreted" annotation of isoform 2).
- Everything ankle-link / USH2 complex / periciliary / hair-bundle-development /
  sensory-perception related → ACCEPT as core.

### Open questions

- Whether human photoreceptors depend on the same ADGRV1–PKA–WHRN–WDSUB1
  regulation of USH2A stability described in mouse cochlea (Guan et al. 2023,
  Adv Sci; see deep research).
- Physiological role of secreted isoform A in basement membranes, and whether the
  collagen IV interaction contributes to the sensory phenotypes at all.
