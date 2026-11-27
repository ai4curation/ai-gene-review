# SLC2A1 (GLUT1, P11166) — curation notes

## Identity and fold
- Solute carrier family 2, facilitated glucose transporter member 1 (GLUT1); the archetypal
  erythrocyte/brain glucose transporter. 492 aa, 12 transmembrane helices (UniProt FT TOPO_DOM/TRANSMEM,
  TM1 12-33 … TM12 430-450), canonical Major Facilitator Superfamily (MFS) / sugar porter fold.
- UniProt SIMILARITY: "Belongs to the major facilitator superfamily. Sugar transporter (TC 2.A.1.1)
  family. Glucose transporter subfamily." TCDB 2.A.1.1.28.

## Core molecular function: facilitative (uniport) D-glucose transport
- GLUT1 catalyses **facilitated diffusion** of glucose (NOT Na+-coupled / not active transport).
  [PMID:24847886 "The glucose transporter GLUT1 catalyses facilitative diffusion of glucose into"];
  the crystal structure "has a canonical major facilitator superfamily fold" captured in an
  inward-open state showing the "alternating access mechanism."
- UniProt CATALYTIC ACTIVITY: Reaction D-glucose(out) = D-glucose(in) (RHEA:60376, CHEBI:4167),
  evidence ECO:0000269 from PubMed:10227690, 10954735, 25982116, 27078104, 32860739.
- UniProt FUNCTION: "Facilitative glucose transporter, which is responsible for constitutive or basal
  glucose uptake"; "Has a very broad substrate specificity; can transport a wide range of aldoses
  including both pentoses and hexoses"; "Most important energy carrier of the brain: present at the
  blood-brain barrier and assures the energy-independent, facilitative transport of glucose into the brain."
- Kinetics: KM ≈ 2.5 mM glucose [PMID:10954735]; KM ≈ 25.6 mM (and 50.1 mM with TPA) [PMID:25982116].
- Structure-function: TM6 is an outer helix with side chains essential for transport
  [PMID:18245775 "Transmembrane segment 6 of the Glut1 glucose transporter is an outer helix and"].
  Inhibitors (cytochalasin B, Phe-amides) "all binding sites overlap the glucose-binding site"
  [PMID:27078104]. Exofacial substrate-binding site modeled by scanning mutagenesis [PMID:19449892].
- Measured D-glucose transport activity IDA: PMID:18245775, PMID:2211693 (GLUT1 assayed alongside GLUT4
  at cell surface in rat adipose cells — the title names GLUT4 but both isoforms are measured),
  PMID:25982116, PMID:27078104. IMP from disease variants: PMID:10227690, PMID:1714544, PMID:21791420,
  PMID:28993322, PMID:23280796.

## Oligomeric state / complex
- GLUT1 forms homo-oligomers: erythrocyte GLUT1 is a homotetramer in equilibrium with dimer, redox-dependent
  [PMID:1429721 "Erythrocyte-resident glucose transporter is a GLUT1 homotetramer, binds 1 mol of"].
  ComplexPortal CPX-3111 "Glucose transporter complex 1" (GO:1990350). Supports identical protein binding
  (GO:0042802) and part_of glucose transporter complex.

## Localization
- Primarily **plasma membrane / cell surface** (core functional location), confirmed by many EXP/IDA studies
  (PMID:18245775, 19449892, 23219802, 24847886, 25982116, 30197081; HPA GO_REF:0000052). UniProt
  SUBCELLULAR LOCATION: "Cell membrane … Multi-pass membrane protein."
- Polarized epithelia / BBB: present at **both apical and basolateral** plasma membranes (RPE and brain
  endothelium) [PMID:31791063; PMID:31678436 apical RPE; PMID:18619525 BBB biotinylation].
- Secondary/peripheral sites (mostly ortholog IEA or large-scale proteomics; kept non-core): melanosome
  [PMID:17081065], midbody [PMID:15166316], cortical actin cytoskeleton / erythrocyte junctional complex
  [PMID:18347014], extracellular exosome [PMID:20458337], blood microparticle [PMID:22516433], caveola /
  membrane raft, photoreceptor inner segment, synapse/presynapse, sarcolemma/Z-disc/intercalated disc
  (muscle, rat ortholog), vesicle (recycling pool).
- Mutant GLUT1 with disease dileucine motifs mislocalizes intracellularly [PMID:30197081 "Mutations in
  Disordered Regions Can Cause Disease by Creating Dileucine Motifs"].

## Secondary substrate: dehydroascorbic acid (vitamin C)
- GLUT1 transports dehydroascorbic acid (DHA), the oxidized form of vitamin C, which is reduced to ascorbate
  intracellularly — a genuine but secondary physiological route for vitamin C uptake.
  [PMID:9228080 "apparent Km of DHA transport via GLUT1 and GLUT3 was 1.1 +/- 0.2 and 1.7 +/- 0.3"];
  [PMID:10862609 "transported by GLUT1 and GLUT3 in Xenopus laevis oocytes with transport rates"].
  Linked to Reactome Vitamin C (ascorbate) metabolism (R-HSA-196836), hence L-ascorbic acid metabolic
  process (non-core). Kept as non-core — glucose transport is the core evolved function.

## Blood-brain barrier and physiology
- Defining physiological role: glucose transport across the blood-brain barrier; haploinsufficiency causes
  GLUT1 deficiency syndrome [PMID:1714544; PMID:10227690; PMID:9462754]. GO:0150104 transport across
  blood-brain barrier is a core process for GLUT1 (IGI/IMP/NAS). CNS/cerebral cortex development is an
  indirect downstream consequence of glucose supply (acts_upstream_of_or_within; non-core).
- Partners that regulate surface GLUT1 (captured in UniProt SUBUNIT): SNX27 (recycling, prevents lysosomal
  degradation) [PMID:23563491]; DMTN/ADD2 (cytoskeletal link) [PMID:18347014]; STOM [PMID:23219802];
  BSG/NXNL1 (cone survival, By similarity/IDA) [PMID:25957687]; SMIM43/NEMEP (mesendoderm) [PMID:35810171].

## Disease
- GLUT1DS1 (De Vivo disease, MIM:606777), GLUT1DS2 paroxysmal exercise-induced dyskinesia (MIM:612126),
  EIG12 (MIM:614847), DYT9 (MIM:601042), stomatin-deficient cryohydrocytosis SDCHCN (MIM:608885). All from
  SLC2A1 variants (UniProt DISEASE). Regulated by PKC phosphorylation at Ser-226 [PMID:25982116].

## Curation decisions (summary)
- CORE MF: GO:0055056 D-glucose transmembrane transporter activity (facilitative uniport); location
  GO:0005886 plasma membrane; complex GO:1990350 glucose transporter complex.
- Bare GO:0005515 protein binding (29 IPI rows) → REMOVE per protein-binding policy (uninformative);
  functionally meaningful interactors are recorded in UniProt SUBUNIT and noted above.
- GO:0016020 membrane (generic) → MODIFY to GO:0005886 plasma membrane.
- Root/entailed transport terms (GO:0022857, GO:0055085, GO:1904659 D-glucose transmembrane transport)
  → TOO_GENERAL (entailed by the specific core MF / GO:0098708 import across plasma membrane).
- Over-annotations (REMOVE/MARK_AS_OVER_ANNOTATED): long-chain fatty acid transport (GO:0005324/GO:0015911,
  IMP to a GLUT1DS clinical paper — biologically implausible; LCFAs use FATP/CD36), fucose transport
  (ortholog IEA), xenobiotic transport (ortholog IEA), response to insulin (GLUT4 hallmark; over-propagated
  IBA/IEA), female pronucleus / cytoplasm / cytosol / mechanical-stimulus / hyperosmotic / T3-response
  (ortholog IEA, weak or implausible for a surface sugar transporter).
- DHA transport, vitamin C metabolism, polarized-membrane and tissue-specific locations, hypoxia response
  (HIF-1 target), photoreceptor maintenance → KEEP_AS_NON_CORE (real but peripheral to the core function).
