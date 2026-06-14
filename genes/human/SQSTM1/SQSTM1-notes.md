# SQSTM1 (p62 / sequestosome-1) — Gene Review Notes

UniProt: Q13501 (SQSTM_HUMAN), 440 aa. HGNC:11280. Synonyms: ORCA, OSIL, A170, ZIP, p62, EBIAP/p60.

## Domain architecture (from UniProt feature table)
- **PB1 domain** (aa 3–102): Phox/Bem1; mediates homo-oligomerization (front-to-back arrays) and hetero-oligomerization with PRKCI/PRKCZ, NBR1, MAP2K5, FHOD3, WDR81. Required (with UBA) for localization into ubiquitin inclusion bodies [UniProt DOMAIN; PMID:12813044; PMID:12887891; PMID:15802564].
- **ZZ-type zinc finger** (aa 123–173): coordinates Zn(2+) (8 binding residues); mediates interaction with RIPK1 [UniProt; PMID:10747026]. Source of GO:0008270 zinc ion binding.
- **TRAF6-binding (TB) motif** (aa 228–233): binds TRAF6, scaffolds NF-kB activation [UniProt MOTIF].
- **LIR / LC3-interacting region** (aa 336–341; broader MAP1LC3B-binding region 321–342): binds ATG8-family proteins (LC3A/B/C, GABARAP/L1/L2); essential for autophagosome recruitment [PMID:17580304; PMID:23908376].
- **KIR (KEAP1-interacting region)** (aa 347–352): binds KEAP1 when phosphorylated at Ser-349 (also reported as Ser-351 in some nomenclatures); competes with NRF2 for KEAP1 Kelch domain [UniProt REGION 347–352; PMID:20452972; PMID:37306101].
- **UBA domain** (aa 389–434): binds (preferentially K63-linked) polyubiquitin; auto-inhibited as a dimer, relieved by phosphorylation (S403/S407), ubiquitination (K420), or acetylation (K420/K435) [PMID:12857745; PMID:15340068; PMID:28322253; PMID:31857589].

## Core biology (synthesized)
p62/SQSTM1 is the prototypical **selective autophagy receptor**. It bridges polyubiquitinated cargo (via UBA) to the nascent autophagosome (via LIR–ATG8 binding), while its PB1 domain drives oligomerization/polymerization that, together with multivalent ubiquitin binding, drives **liquid–liquid phase separation into "p62 bodies"** — membraneless condensates that concentrate ubiquitinated cargo for engulfment [PMID:29343546 "p62 filaments capture and present ubiquitinated cargos for autophagy"; PMID:29507397 "Polyubiquitin chain-induced p62 phase separation drives autophagic cargo segregation"; PMID:31857589].

Substrate breadth: aggrephagy (ubiquitinated protein aggregates) [PMID:17580304; PMID:16286508; PMID:22017874], plus more specialized selective autophagy: pexophagy (ROS-induced, via ubiquitinated PEX5) [PMID:26344566], xenophagy/antibacterial autophagy [PMID:36221902; PMID:27880896], inflammasome/RIPosome control [PMID:30612879; PMID:27498865], and a supporting (non-essential) role in PINK1/Parkin mitophagy — p62 is recruited to depolarized mitochondria and required for their perinuclear **clustering**, but is **dispensable for mitochondrial clearance itself** [PMID:20890124 "required for Parkin-induced mitochondrial clustering but not mitophagy"; PMID:20457763].

Signaling scaffold (PB1/ZZ/TB-dependent): NF-kB activation downstream of IL-1/TRAF6, NGF/TrkA, and TNF/RIPK1; binds atypical PKCs (PRKCZ/PRKCI). Also negatively regulates TLR4 signaling by acting on the TRAF6–ECSIT complex [PMID:31281713].

KEAP1–NRF2 antioxidant axis: phospho-S349 p62 sequesters KEAP1 into p62 bodies, derepressing NRF2 (NFE2L2) and inducing the antioxidant/phase-II response; SQSTM1 is itself an NRF2 target gene (positive feedback) [PMID:20452972 "p62/SQSTM1 is a target gene for transcription factor NRF2 and creates a positive feedback loop"; PMID:23274085; PMID:37306101]. This axis underlies cytoprotection including protection against ferroptosis in HCC cells [PMID:26403645].

Endosome organization: ubiquitinated p62 (RNF26/UBE2J1, K435) acts as a perinuclear molecular bridge retaining endosomal vesicles for organized cargo transport [PMID:27368102 "An ER-Associated Pathway Defines Endosomal Architecture"].

Disease: dominant gain/loss SQSTM1 variants cause Paget disease of bone (PDB3), FTD/ALS (FTDALS3), distal myopathy with rimmed vacuoles; recessive loss causes childhood neurodegeneration with ataxia/dystonia/gaze palsy (NADGP). SQSTM1-NUP214 fusion in T-ALL.

## Review decisions rationale
- **Core MF**: ubiquitin-modified protein reader activity (GO:0140036) / K63-polyUb-dependent binding (GO:0070530) / ubiquitin binding (GO:0043130); protein-macromolecule adaptor (GO:0030674) bridging cargo to ATG8; molecular condensate scaffold activity (GO:0140693); protein sequestering activity (GO:0140311). All ACCEPT where IDA-supported.
- **Core BP**: aggrephagy (GO:0035973), macroautophagy (GO:0016236), protein targeting to vacuole involved in autophagy (GO:0071211), membraneless organelle assembly (GO:0140694). ACCEPT.
- **KEAP1/NRF2 & signaling scaffold**: real, well-supported but secondary to the receptor function → mostly ACCEPT for direct experimental (positive regulation of autophagy, NF-kB regulation, TLR4 negative regulation) and KEEP_AS_NON_CORE for broad process terms.
- **bare protein binding (GO:0005515)**: ~50 IPI annotations from interactome screens and specific partners. Per curation guidelines, uninformative → KEEP_AS_NON_CORE (do not REMOVE experimental IPI).
- **identical protein binding (GO:0042802)**: real (PB1-mediated homo-oligomerization), informative-ish → KEEP_AS_NON_CORE (oligomerization is genuine).
- **mitophagy (GO:0000423) / autophagy of mitochondrion (GO:0000422)**: p62 contributes to mitophagy (recruited to damaged mito; clustering) but is dispensable for clearance → KEEP_AS_NON_CORE rather than core; experimental IGI/NAS retained, defer to curators.
- **Reactome cytosol TAS (many duplicates)**: correct localization, generic pathway context → ACCEPT a representative / KEEP_AS_NON_CORE the redundant ones.
- **Ensembl GO_REF:0000107 ortholog-transfer IEA** (temperature homeostasis, response to ischemia, brown fat cell proliferation, energy homeostasis, synapse/glutamatergic synapse, sperm midpiece, LTP, ionotropic glutamate receptor binding): pleiotropic mouse-derived; biologically plausible but peripheral → KEEP_AS_NON_CORE (not REMOVE; experimentally grounded in mouse orthologs).
- **GO:0035255 ionotropic glutamate receptor binding / synapse terms**: ortholog-transfer; keep non-core.
- **GO:0046578 regulation of Ras protein signal transduction (NAS, PMID:8618896)**: early RASA1/Lck-binding paper; weak/historical → KEEP_AS_NON_CORE.
- **GO:0045944 positive regulation of transcription by Pol II (TAS Reactome NRIF)**: indirect; KEEP_AS_NON_CORE.
- **GO:0043065 positive regulation of apoptotic process (TAS Reactome NRIF cell death)**: indirect/context-specific → KEEP_AS_NON_CORE.

## Provenance of key claims
- Phase separation / p62 bodies as condensate scaffold: [PMID:29343546], [PMID:29507397], [PMID:31857589], [PMID:37306101].
- LIR–LC3 bridging: [PMID:17580304].
- UBA K63-polyUb binding: [PMID:12857745], [PMID:15340068].
- NRF2/KEAP1: [PMID:20452972], [PMID:37306101], [PMID:23274085].
- Pexophagy: [PMID:26344566].
- Xenophagy/inflammasome: [PMID:36221902], [PMID:30612879], [PMID:27498865].
- Endosome organization: [PMID:27368102].
- Mitophagy nuance (dispensable for clearance): [PMID:20890124].
- TLR4 negative regulation: [PMID:31281713].
- Acylation/autophagosome recruitment: [PMID:37802024].
