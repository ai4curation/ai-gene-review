# RBOHD (Q9FIJ0) curation notes

Gene: RESPIRATORY BURST OXIDASE HOMOLOG PROTEIN D (RBOHD / AtrbohD), Arabidopsis thaliana, locus AT5G47910.

## Identity and architecture (UniProt Q9FIJ0)
- Plasma-membrane NADPH oxidase of the RBOH (TC 5.B.1.3) family; gp91phox/NOX homolog. 921 aa, six transmembrane helices, N-terminal cytoplasmic region (~1-376) carrying two canonical EF-hand Ca2+-binding domains (residues 253-288 and 297-332) plus EF-hand-like regions, and a C-terminal cytoplasmic FAD-binding (FR-type) + NADPH-binding ferredoxin-reductase module.
- EC=1.6.3.- (NAD(P)H:oxygen oxidoreductase) and EC=1.11.1.- listed; BRENDA cross-reference 1.6.3.1.
- Ca2+ binding sites at residues 266, 268, 270, 272, 277 (PROSITE EF-hand). [UniProt FT BINDING Ca(2+)]
- Phosphoserines: Ser-8, Ser-9, Ser-26, Ser-39, Ser-339, Ser-343, Ser-347. Ser-39/Ser-343/Ser-347 phosphorylated by BIK1 upon flg22; Ser-347 (+Ser-8/9/339) by SIK1 — phosphorylation activates ROS production. [UniProt PTM]
- UniProt FUNCTION: "Calcium-dependent NADPH oxidase that generates superoxide. Involved in the generation of reactive oxygen species (ROS) during incompatible interactions with pathogens, in response to pathogen-associated molecular pattern (PAMP)-triggered immunity (PTI) signaling and in UV-B and abscisic acid ROS-dependent signaling."
- Subcellular location: Membrane; multi-pass membrane protein. Tissue: more abundant in roots; expressed in mesophyll and guard cells.

## Core molecular function
RBOHD is the catalytic subunit of a plasma-membrane NADPH oxidase that transfers electrons from cytosolic NADPH across the membrane to molecular O2, producing apoplastic superoxide (O2.-), which dismutates to H2O2. The proximal product is superoxide:
- [PMID:11756663 "an NADPH oxidase subunit is required for ROI production confirms Doke's original suggestion that O is the first ROI produced"]
- The correct catalytic MF GO term is GO:0016175 "superoxide-generating NAD(P)H oxidase activity" (verified via OLS; def "NAD(P)H + O2 = NAD(P)+ + O2-"). The seeded annotations use GO:0016174 "NAD(P)H oxidase H2O2-forming activity" (def NAD(P)H + O2 = NAD(P)+ + H2O2) — H2O2 is formed only after dismutation of the primary superoxide product, so GO:0016175 is more accurate for RBOH proteins.

## Activation / regulation
- Calcium binds the EF-hands; activity is calcium-dependent (UniProt). GO:0005509 calcium ion binding is well supported by EF-hand domains.
- BIK1, a receptor-like cytoplasmic kinase in the FLS2 complex, directly phosphorylates RBOHD at Ser-39/Ser-343/Ser-347 in a Ca2+-independent manner to enhance ROS. [PMID:24629339 "directly phosphorylates the NADPH oxidase RbohD at specific sites in a calcium-independent manner to enhance ROS generation"]
- SIK1 (MAP4K) binds RBOHD upon flagellin perception and activates it by phosphorylation (Ser-347). [UniProt; PubMed:30212650]
- PBL13 (a Ser/Thr RLCK) associates with RBOHD before pathogen perception and negatively regulates ROS; the association is disrupted by flg22. [PMID:26432875 "PBL13 is able to associate with the ... oxidase RESPIRATORY BURST OXIDASE HOMOLOG PROTEIN D (RBOHD) by split-luciferase complementation assay, and this association is disrupted by flagellin treatment"]
- LecRK-IX.2 induces RBOHD phosphorylation, likely via CPKs, in pattern-triggered immunity. [PMID:28696275 "LecRK-IX.2 is capable of inducing RbohD phosphorylation, likely by recruiting calcium-dependent protein kinases to trigger ROS production"]
- HRU1 (universal stress protein) interacts with RBOHD and ROP2 to modulate ROS under anoxia. [PMID:27251529 "HRU1 interacts with proteins that induce ROS production, the GTPase ROP2 and the NADPH oxidase RbohD"]
- MPK8 (Ca2+/CaM-MKK3 pathway) negatively regulates ROS via control of RbohD expression in wound signaling. [PMID:21419340 "The MPK8 pathway negatively regulates ROS accumulation through controlling expression of the Rboh D gene"]

## Biological processes
- PAMP/PTI immunity and the apoplastic oxidative (respiratory) burst; defense response. [PMID:11756663 "AtrbohD and AtrbohF are required for accumulation of reactive oxygen intermediates in the plant defense response"; "AtrbohD gene is required for most of the ROI observed after inoculation with avirulent Pst"]
- Control/limitation of cell death: RBOHD-derived ROS suppress spread of hypersensitive cell death in surrounding cells (antagonize SA-dependent pro-death signals). [PMID:16170317 "the subsequent oxidative burst can suppress cell death in cells surrounding sites of NADPH oxidase activation"] Context-dependent (dual roles) in Alternaria pathosystem. [PMID:19726575 "dual roles of RBOHD ... suggesting either initiation or prevention of cell death dependent on the distance from pathogen attack"]
- Defense response to fungus (Alternaria brassicicola). [PMID:19726575]
- ROS metabolic process / ROS gene network. [PMID:15608336; PMID:15705948 (ozone, G-protein)]
- ABA/stomatal: RBOHD-derived ROS required for ABA-induced stomatal closure and drought responses. [PMID:26704641 "HY1-ABI4 signaling ... involved in stomatal closure was dependent on the RbohD-derived ROS production"; UniProt disruption phenotype "impaired in abscisic acid-induced stomatal closing"]
- Osmosensing / carbohydrate homeostasis under cellulose-biosynthesis inhibition: rbohDF impaired in osmosensitive metabolic changes. [PMID:22422940 "osmotic support does not suppress CBI-induced metabolic changes in seedlings impaired in ... reactive oxygen species production (respiratory burst oxidase homolog DF [rbohDF])"]
- Response to wounding (via MPK8 control of RbohD). [PMID:21419340]
- Response to heat / thermotolerance: atrbohD shows weaker thermotolerance defects. [PMID:15923322 "Mutations in nicotinamide adenine dinucleotide phosphate oxidase homolog genes (atrbohB and D) ... showed weaker defects"]
- Cellular response to hypoxia: RBOHD transcript regulation under transient hypoxia stress (HEP, translatome/epigenome study). [PMID:31519798]

## Localization
- Plasma membrane is the functional location (HDA proteomics PMID:22923678; abundant literature). Multi-pass PM protein.
- Golgi (HDA, PMID:22430844 / LOPIT proteomics PMID:22923678) and plastid (HDA, PMID:28887381 protein-correlation profiling) signals are high-throughput organellar-proteomics assignments. For a multi-pass PM oxidase these most likely reflect endomembrane/secretory trafficking or co-fractionation rather than a distinct functional compartment; mark as over-annotated / non-core.
- Nucleus (ISM, GO_REF:0000122, AtSubP prediction) is a computational subcellular-localization prediction with no experimental support for a nuclear RBOHD; a transmembrane PM oxidase is not expected in the nucleus. Remove.

## GO term decisions summary
- GO:0016175 superoxide-generating NAD(P)H oxidase activity = correct core MF (proposed replacement for GO:0016174).
- GO:0005509 calcium ion binding = ACCEPT (EF-hands, Ca2+-dependent).
- GO:0004601 peroxidase activity (IEA, InterPro/KW) = REMOVE/over-annotation: RBOHD is a superoxide-generating oxidase, not a peroxidase; the "Peroxidase" keyword derives from the gp91phox/cytochrome-b245 InterPro signature and is misleading.
- GO:0016491 oxidoreductase, GO:0050664 oxidoreductase acting on NAD(P)H O2 acceptor = generic parents of GO:0016175; keep as accept (true but less informative).
- GO:0098869 cellular oxidant detoxification (inferred from peroxidase activity) = REMOVE: RBOHD generates ROS for signaling, it does not detoxify oxidants; inference rests on the spurious peroxidase MF.
- GO:0005515 protein binding (BIK1/FLS2, PBL13, HRU1, LecRK) = uninformative; mark over-annotated, captured better by molecular_function regulator interactions.
- GO:0002679 respiratory burst involved in defense response = good candidate NEW BP term for the immune oxidative burst (verified via OLS).
