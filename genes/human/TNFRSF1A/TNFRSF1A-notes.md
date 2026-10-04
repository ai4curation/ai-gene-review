# TNFRSF1A notes

## 2026-09-30

- Revisited the pre-existing TNFRSF1A review after a GOA refresh appended 12
  fresh `GO:0005515` rows. These new rows were all physical interactions that
  duplicate already reviewed TNFR1 signaling contexts or add high-throughput
  edges: TRADD/RIPK1 death-domain contacts, RFK coupling to NADPH oxidase,
  SH3RF2-dependent recruitment of TRADD, progranulin/GRN binding to CRD2/CRD3,
  UBB and MON2 from the TNF-alpha/NF-kappaB pathway AP-MS map, and UBB/RIPK1/TRADD
  from BioPlex 3.0.
- The TRADD and RIPK1 rows can be folded into `GO:0005031 tumor necrosis factor
  receptor activity`, matching the existing treatment of the same mechanism.
  TRADD and RIPK1 recruitment to TNFR1 is the receptor's proximal death-domain
  signaling function, not a separable generic binding activity [PMID:16611992
  Competitive control of independent programs of tumor necrosis factor receptor-induced
  cell death by TRADD and RIP1, "TRADD and RIP1 compete for recruitment to the
  TNFR1 signaling complex"].
- RFK has direct TNFR1-coupled signaling evidence [PMID:19641494 Riboflavin
  kinase couples TNF receptor 1 to NADPH oxidase, "previously unrecognized
  TNF-receptor-1 (TNFR1)-binding protein"], and SH3RF2 affects TNFR1 adaptor
  recruitment [PMID:24130170 SH3RF2 functions as an oncogene by mediating PAK4
  protein stability, "attenuates TRADD (TNFR-associated death domain) recruitment"].
  I kept both as `MODIFY` to the receptor activity rather than retaining bare
  `protein binding`.
- GRN/progranulin binds the TNFR extracellular CRD2/CRD3 domains [PMID:24070898
  Progranulin directly binds to the CRD2 and CRD3 of TNFR extracellular domains,
  "CRD2 and CRD3 of TNFR are important for the interaction with PGRN"], but
  this is not `tumor necrosis factor binding`; with no precise TNFRSF1A-side
  molecular function term, the generic new IntAct row was removed.
- UBB and MON2 from the 2004 pathway interactome [PMID:14743216 A physical and
  functional map of the human TNF-alpha/NF-kappa B signal transduction pathway,
  "tandem affinity purification, liquid-chromatography tandem mass spectrometry"]
  and the three BioPlex 3.0 rows [PMID:33961781 Dual proteome-scale networks
  reveal cell-specific remodeling of the human interactome, "proteome-scale,
  cell-line-specific interaction networks"] are high-throughput AP-MS edges, so
  they were removed as uninformative TNFRSF1A functions.
- The synthesized core-function section already had matching, reviewed process
  assertions in the body of the file. I changed `GO:0007249 canonical NF-kappaB
  signal transduction` to the accepted `GO:0043123 positive regulation of
  canonical NF-kappaB signal transduction`, and changed generic `GO:0097191
  extrinsic apoptotic signaling pathway` to the accepted death-domain-receptor
  descendant `GO:0008625`.
