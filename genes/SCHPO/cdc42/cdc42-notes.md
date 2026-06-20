# cdc42 (Q01112, SPAC110.03) — S. pombe — review notes

## Overview
Cdc42 is an essential Rho-family small GTPase, the master regulator of cell polarity and
polarized (tip) growth in fission yeast. It cycles between GDP- and GTP-bound states,
activated by GEFs Scd1 and Gef1, inactivated by GAPs (Rga4, etc.). GTP-Cdc42 binds
effectors (scaffold Scd2, PAK kinases Shk1/Pak1 and Shk2/Pak2, formin For3) to organize
actin, exocytosis, and polarity. It is geranylgeranylated at the C-terminal CAAX for
plasma-membrane/cell-tip localization.

## Key evidence

- Essential gene; null cells arrest as small round dense cells; site-specific mutants
  (G12V, Q61L, D118A) give large misshapen cells -> controls polarized growth.
  [PMID:8289788 "We have disrupted the cdc42+ gene and shown that it is essential for growth. The cdc42 null phenotype is an arrest as small, round, dense cells"]
  [PMID:8289788 "the cdc42 mutants did exhibit an abnormal morphological phenotype of large, misshapen cells, suggesting that S. pombe Cdc42p is involved in controlling polarized cell growth"]
  Fractionates to soluble and particulate pools (cytosolic + membrane).
  [PMID:8289788 "The Cdc42p protein fractionates to both soluble and particulate fractions, suggesting that it exists in two cellular pools"]

- GTP/GDP switch; intrinsic GTPase hydrolysis stimulated by GAP.
  [PMID:21849474 "They have intrinsic GTPase activity and can hydrolyze GTP to GDP, but this hydrolysis is usually inefficient. It is facilitated when the small GTPase binds to a GTPase-activating protein (GAP)"]
  GTP-Cdc42 binds CRIB-domain effectors incl PAKs and WASp.
  [PMID:18328707 "the GTP-bound form of Cdc42 binds and activates a group of proteins with the CRIB (Cdc42/Rac-interactive binding) domain. The CRIB-domain proteins include p21-activated kinases (PAKs) and WASp"]

- Active GTP-Cdc42 concentrated at growing cell tips (CRIB-GFP reporter); GAP Rga4 excluded
  from tips; Pom1 ensures bipolar Cdc42 activation.
  [PMID:18328707 "GTP-bound, active Cdc42 is concentrated to growing cell ends accompanied by developed F-actin structures, where the Rga4 GAP is excluded"]

- Cdc42-GTP gradient at cell tip plasma membrane sets cell width (GEF Scd1 at tips, GAP Rga4
  at sides).
  [PMID:21849474 "We propose that the GAP Rga4 and the GEF Scd1 establish a gradient of activated Cdc42 within the cellular tip plasma membrane, and it is this gradient that determines cell growth-zone size and normal cell width"]

- Functional Cdc42-mCherrySW localizes to cell tips, division site, nuclear membrane;
  trafficked on exocytic vesicles.
  [PMID:25837586 "Cdc42-mCherrySW was enriched at the cell tips and division sites... localization to nuclear membrane... and on internal membranes including the nuclear and presumably vacuolar membranes"]
  [PMID:25837586 "In cells depleted of the exocyst member Sec8, in which exocytic vesicles accumulate but fail to fuse at the cell tip, Cdc42-mCherrySW accumulated sub-apically, confirming that Cdc42 is trafficked on exocytic vesicles"]
  Membrane targeting (CAAX prenylation) essential.
  [PMID:25837586 "removal of the CAAX sequence yielded a diffuse, non-functional Cdc42 allele unable to complement the cdc42-1625 temperature-sensitive mutant"]
  Cdc42-GTP slower mobility than GDP at membrane (positive-feedback accumulation).

- Cytokinesis / division site: GFP-Cdc42p at medial cell-division site during cytokinesis,
  dependent on actin and the actomyosin ring.
  [PMID:10961446 "GFP-Cdc42p was observed at the medial region of the cell at the cell-division site early in cytokinesis and remained there through cell separation"]
  [PMID:10961446 "medial GFP-Cdc42p localization was eliminated in a number of cytokinesis mutants, including strains defective in assembling the medial actinomyosin ring"]
  Two GEFs give a spatiotemporal Cdc42 activation pattern in cytokinesis (Gef1 before, Scd1 after ring constriction).
  [PMID:26941334 "Before cytokinetic ring constriction, Cdc42 activation, is Gef1 dependent, and after ring constriction, it is Scd1 dependent"]
  Cdc42 (via Pak1) prevents precocious Rho1 activation during cytokinesis.
  [PMID:37039135 "We show that Cdc42 prevents early Rho1 activation during fission yeast cytokinesis"]
  Hob3p recruits/concentrates Cdc42 to division site.
  [PMID:17363901 "Hob3p is required for the concentration of Cdc42p to the division area"]

- Membrane traffic / exocytosis: cdc42L160S has secretion + vesicle/vacuole defects;
  exocyst mislocalized.
  [PMID:21899677 "a thermosensitive strain carrying the cdc42L160S allele has membrane traffic defects independent of the actin cable defects. This strain has decreased acid phosphatase (AP) secretion, intracellular accumulation of vesicles and fragmentation of vacuoles. In addition, the exocyst is not localized to the tips"]
  Required for transport/recycling of glucan synthases Bgs1/Bgs4 to PM.
  [PMID:23060961 "Cdc42 is required for the correct transport/recycling to the plasma membrane of the glucan synthases Bgs1 and Bgs4"]

- Mating / cell fusion: Cdc42 explores cell periphery for mate selection; dynamic active
  zones with Scd1/Scd2.
  [PMID:23200991 "low-level pheromone signaling promotes a novel polarization state, where active Cdc42, its GEF Scd1, and scaffold Scd2 form colocalizing dynamic zones that sample the periphery of the cell"]
  Cdc42 required for cell-cell fusion; mating needs higher Cdc42 levels than mitotic growth.
  [PMID:41855172 "Cdc42 also functions in cell-cell fusion during Schizosaccharomyces pombe sexual reproduction"]
  [PMID:41855172 "mating and cell fusion require higher Cdc42 protein levels than mitotic polarized growth"]
  Ras1-GTP hydrolysis coordinates Cdc42 into single growth zone during mating.
  [PMID:24147005 "they die due to their failure to coordinate active Cdc42 into a single growth zone resulting in disorganized actin deposition"]

- Effectors / complex: Scd1, Scd2, Cdc42, Ras1-GTP cooperatively form a complex.
  [PMID:7923372 "scd1, scd2, cdc42sp, and ras1, in its GTP-bound state, act cooperatively to form a protein complex"]
  Shk1/Pak1 PAK binds Cdc42 (Ras/Cdc42 signaling module).
  [PMID:7597098 "We provide genetic evidence for physical and functional interaction between Shk1 and the Cdc42 GTP-binding protein required for normal cell morphology and mating"]
  Shk1/Cdc42/Skb1 ternary complex.
  [PMID:8943016 "Shk1, Cdc42, and Skb1 are able to form a ternary complex in vivo"]
  Pak2/Shk2 PAK binds Cdc42 (membrane localization via PBD + Cdc42).
  [PMID:9660818 "the membrane localization of Pak2p, directed by its interactions with membrane lipids and Cdc42p, is critical to its biological activity"]
  [PMID:9660817 "Like other known PAKs, Shk2 binds to Cdc42 in vivo and in vitro"]
  GEFs: Gef1 binds inactive Cdc42, stimulates GDP-GTP exchange in vitro.
  [PMID:12529446 "Gef1p binds to inactive Cdc42p... Gef1p is capable of stimulating guanine nucleotide exchange of Cdc42p in vitro"]
  Gef1p/Scd1p form a ring at division site; recruit active Cdc42 to septation site.
  [PMID:12972551 "recruitment of Cdc42p to the cell division site follows the shrinking Gef1p/Scd1p ring; the Cdc42p accumulates like a closing iris"]
  Cdc42 acts as hub in GEF feedforward (recruits scaffold Scd2 -> Scd1).
  [PMID:31719163 "Gef1 promotes Scd1 localization to the division site during cytokinesis through recruitment of the scaffold protein Scd2, via a Cdc42 feedforward pathway"]

- Spatial regulation: Orb6 NDR kinase restricts Cdc42 to tips (loss -> Cdc42/For3/Gef1 to
  cell sides).
  [PMID:19646873 "Loss of Orb6 kinase activity leads to the recruitment of Cdc42 GTPase and the Cdc42-dependent formin For3, normally found only at the cell tips, to the cell sides"]
  Two-GEF coordination by microtubules/Tea1-Tea4-Pom1.
  [PMID:29930085 "involving coordination of 'local' (Scd1) and 'global' (Gef1) Cdc42 GEFs via microtubules and microtubule-dependent polarity landmarks"]

- Invasive filaments: activated Cdc42 concentrated at single growing tip.
  [PMID:20870879 "A group of proteins involved in the growth process and actin regulation, comprising Spo20, Bgs4, activated Cdc42, and Crn1, are all concentrated at the growing tip"]

- Heat-stress adaptation: thermal stress transiently decreases Cdc42 activity -> monopolar
  growth (Cdc42 at lateral cortex).
  [PMID:24146635 "dynamic adaptation to thermal stress resulting in a period of decreased Cdc42 activity and altered, monopolar growth"]

## Annotation flags / caveats

- GO:0003925 "G protein activity" (IEA, EC mapping): small GTPases are not heterotrimeric
  G-protein subunits; this EC-based term is misapplied. The correct MF is GTPase activity
  (GO:0003924). -> REMOVE.

- GO:0003924 "GTPase activity" IDA from PMID:18793338 — that paper is about Rga2 as a Rho2
  GAP and does not measure Cdc42 intrinsic GTPase activity directly; the annotation is
  conceptually correct but the cited reference is weak. GTPase activity is well-established
  for Cdc42 (RHO-family GTPase) and supported by the GEF/GAP cycle literature. ACCEPT the
  function (core); rely on broader evidence.

- GO:0032951 "regulation of beta-glucan biosynthetic process" IGI from PMID:8887550:
  PMID:8887550 explicitly shows cdc42+ and constitutively active cdc42 do NOT activate
  (1-3)beta-D-glucan synthase (Rho1 does). [PMID:8887550 "Neither cdc42+ nor the cdc42-V12G
  or cdc42-Q61L constitutively active mutant alleles affect (1-3)beta-D-glucan synthase
  activity when overexpressed"]. The IGI annotation is at best very indirect (Cdc42 affects
  trafficking of Bgs glucan synthases per PMID:23060961). MARK_AS_OVER_ANNOTATED / KEEP non-core.

- GO:0032955 "regulation of division septum assembly" IMP also cited to PMID:8887550 (a Rho1
  paper). The PMID assignment is questionable, but Cdc42 does have well-documented roles in
  cytokinesis/septation (Gef1/Scd1, Bgs1 recruitment). Keep as non-core.

- bare "protein binding" (GO:0005515) annotations: uninformative; each represents a real
  interaction (Gef1, Scd1, Hob3, Scd2, Shk1/Pak1, Shk2/Pak2, Skb1, Pob1). MARK_AS_OVER_ANNOTATED
  in favor of more informative effector/complex terms.

- GO:0101026 "mitotic nuclear membrane biogenesis" (ISO) is in UniProt DR lines but NOT in
  the goa.tsv annotation set provided; not reviewed here.

## Core functions
1. MF: GTPase activity (molecular switch) + GTP/GDP binding.
2. BP: establishment/regulation of cell polarity and polarized tip growth (actin organization
   via For3, PAK signaling).
3. BP: cytokinesis / division-site organization (recruits Cdc42 effectors, Bgs1, restrains Rho1).
4. BP: polarized secretion / exocytosis / membrane traffic (exocyst, Bgs delivery).
5. BP: mating projection / cell fusion during sexual reproduction.
6. CC: plasma membrane of cell tip / cell division site (prenyl-anchored).
