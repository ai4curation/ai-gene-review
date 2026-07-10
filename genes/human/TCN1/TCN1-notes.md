# TCN1 (Transcobalamin-1 / Haptocorrin) review notes

UniProtKB: P20061 (TCO1_HUMAN). Gene TCN1 (syn. TC1), HGNC:11652, chr 11.
433 aa precursor; signal 1-23; mature chain 24-433. ~30% carbohydrate (heavily
N-glycosylated). Belongs to the eukaryotic cobalamin transport protein family
(with TCN2/transcobalamin and GIF/intrinsic factor).

## Core biology

- Secreted broad-specificity cobalamin (vitamin B12)-binding glycoprotein, aka
  haptocorrin (HC), transcobalamin I, protein R / R-binder.
  [file:human/TCN1/TCN1-uniprot.txt "SUBCELLULAR LOCATION: Secreted."]
- Binds B12 with femtomolar affinity, protecting it from the acidic stomach.
  [file:human/TCN1/TCN1-uniprot.txt "Binds vitamin B12 with femtomolar affinity and protects it"]
  [file:human/TCN1/TCN1-uniprot.txt "from the acidic environment of the stomach."]
- Produced by salivary glands (food-induced) and is a major constituent of the
  secondary (specific) granules of neutrophils.
  [file:human/TCN1/TCN1-uniprot.txt "Produced by the salivary glands of the oral cavity,"]
  [file:human/TCN1/TCN1-uniprot.txt "in response to ingestion of food. Major constituent of secondary"]
  [PMID:2777761 "It is a major protein constituent of secondary granules in"]
- "R binder family of vitamin B12 binding proteins." [PMID:2777761]

## Binding specificity / structure

- Crystal structures of human HC with cyanocobalamin and cobinamide (Furger 2013,
  PDB 4KKI/4KKJ). Three transport proteins (TC, IF, HC) share overall structure but
  differ in corrinoid selectivity; HC has the broadest specificity (binds cobalamin
  AND inactive corrinoid analogues).
  [PMID:23846701 "a similar overall structure but a different selectivity for corrinoids."]
  Reactome R-HSA-3245898: "broad correnoid specificity of TCN1 ... a role for the
  latter in scavenging and mediating the hepatobiliary excretion of corrinoids."
- HC is NOT the cellular-delivery carrier: unlike TC (TCN2), haptocorrin is not
  recognized by the cellular uptake receptor CD320.
  [PMID:27411955 "haptocorrin (HC), a high affinity Cbl-binding protein that shares significant sequence and structural similarities with TC and is also circulating in the plasma, is not recognized by CD320."]

## Localization

- Secreted / extracellular (GO:0005576 extracellular region present in GOA via IBA,
  IEA-SubCell, HDA proteomics, and Reactome TAS).
- Neutrophil granule lumen: specific granule lumen (GO:0035580) and tertiary granule
  lumen (GO:1904724), consistent with degranulation / secondary-granule protein role.
- Identified in body fluids incl. plasma (glycoproteome), saliva, colostrum
  (PMID:16502470 proteomic detection in colostrum — localization support only).

## GOA MF/BP/CC used for core_functions (exact current terms, from go.db)

- MF: GO:0031419 cobalamin binding (molecular_function) — the core function.
- BP: GO:0015889 cobalamin transport (biological_process).
- CC: GO:0005576 extracellular region (cellular_component).

## Annotation-specific judgments

- GO:0005515 protein binding (IPI, PMID:32814053, JPH3 interactor from an ND
  interactome Y2H screen): bare "protein binding" is uninformative; single
  high-throughput Y2H hit with no functional follow-up. Per policy, do NOT REMOVE
  an experimental IPI whose full text is unverified — MARK_AS_OVER_ANNOTATED.
  UniProt records the P20061-JPH3 (Q8WXH2) IntAct interaction.
- GO:0140355 cargo receptor ligand activity (EXP, Reactome/PMID:22547309): TCN1 does
  bind Cbl and its complex is endocytosed (via asialoglycoprotein receptor in liver,
  not CD320). "Cargo receptor ligand activity" is a defensible Reactome MF framing but
  is secondary to cobalamin binding; keep as non-core. Abstract-only review; do not remove.
- GO:0140313 molecular sequestering activity (EXP x2, PMID:23846701, PMID:27411955):
  captures HC's scavenging of Cbl/corrinoids (protecting B12; sequestering inactive
  analogues). Correct in essence; secondary framing → KEEP_AS_NON_CORE.
- Cobalt/cobalt-ion-transport keyword (GO:0006824) appears only in the UniProt DR/KW
  block, NOT in the seeded GOA, so it is out of scope for existing_annotations.

## Deep research
Falcon deep research is OUT OF CREDITS (HTTP 402); no -deep-research-falcon.md was
generated. Review grounded in TCN1-uniprot.txt, TCN1-goa.tsv, cached publications/
PMID_*.md, and cached reactome/ entries.
