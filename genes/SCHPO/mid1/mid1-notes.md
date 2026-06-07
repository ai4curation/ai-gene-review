# mid1 (Dmf1) — S. pombe anillin-related medial ring protein — review notes

UniProt: P78953 (BUD4_SCHPO). Gene: mid1 / dmf1 / SPCC4B3.15. 920 aa.
NOTE: Do not confuse with human MID1 (Opitz syndrome E3 ubiquitin ligase) — unrelated.

## Core biology
Mid1 (Dmf1) is the fission-yeast anillin-related protein that positions the cytokinetic
division plane. It shuttles from the nucleus to form cortical "nodes" overlying the
nucleus at the cell middle, and recruits contractile-actomyosin-ring (CAR) components
(myosin-II Myo2, IQGAP Rng2, formin Cdc12, F-BAR Cdc15, SAD kinase Cdr2, phosphatase
Clp1) to assemble the medial ring, coupling the division site to nuclear position. Its
nuclear export and cortical retention are cell-cycle regulated (Plo1 phosphorylation
drives export; Sid2 phosphorylation drives cortical removal).

## Key evidence

### Division-site positioning / function
- [PMID:8946912 "Dmf1 mutants complete mitosis and initiate septum formation, but the septa that form are positioned at random locations and angles in the cell, rather than in the middle."] — essential for correct septum placement.
- [PMID:8946912 "In wild-type cells, Dmf1p is nuclear during interphase, and relocates to form a medial ring at the cell cortex coincident with the onset of mitosis."] — nucleus -> medial ring relocalization; "associated with increased phosphorylation of Dmf1p."
- [PMID:10930468 "mid1 is required for the proper placement of the contractile actin ring for cytokinesis at a medial site overlying the nucleus."]
- [PMID:10930468 "mid1 protein (mid1p) shuttles between the nucleus and a cortical medial broad band during interphase and early mitosis. The position of this broad band, which overlies the nucleus, is linked to nuclear position even in cells with displaced or multiple nuclei."]
- [PMID:10930468 "We identified and created mutations in an NLS and in two crm1-dependent NES sequences in mid1p. NES mutations caused mid1p accumulation in the nucleus and loss of function."]
- [PMID:19427212 "These signals control the localization of the anillin-like protein Mid1, which defines the position of the division plane at the medial cortex, where it recruits contractile-ring components at mitosis onset."]
- [PMID:19427212 "the positive signaling from the nucleus is based on Mid1 nuclear export, which links division-plane position to nuclear position during early mitosis."]
- [PMID:19427212 "Cdr2 kinase anchors Mid1 at the medial cortex during interphase through association with the Mid1 N terminus."]

### Recruitment / scaffold of CAR components
- [PMID:22918943 "orderly assembly of the contractile ring in wild-type cells depends on Mid1p to recruit myosin-II, Rng2p, and Cdc15p to nodes and to place cytokinetic nodes around the cell equator."]
- [PMID:22918943 "cortical nodes containing the protein Blt1p and several kinases appear early in G2, mature into cytokinetic nodes by adding anillin Mid1p, myosin-II, formin Cdc12p, and other proteins, and condense into a contractile ring"]
- [PMID:16864655 "the anillin-like protein Mid1p establishes a broad band of small dots or nodes in the cortex near the nucleus. These nodes mature by the addition of conventional myosin II (Myo2p, Cdc4p, and Rlc1p), IQGAP (Rng2p), pombe Cdc15 homology protein (Cdc15p), and formin (Cdc12p)."]
- [PMID:14602073 "the anillin-like protein (Mid1p) migrates from the nucleus and specifies a broad band of cortex around the equator as the division site."]
- [PMID:15184401 "The accumulation of Myo2 requires the anillin homologue Mid1 that functions in proper ring placement. Myo2 interacts with Mid1 in cell lysates"] ; [PMID:15184401 "dephosphorylated Myo2 is anchored by Mid1 at the medial cortex and promotes the ring assembly in cooperation with F-actin."]
- [PMID:21376595 "Mid1p arrives first at the medial cortex and recruits actomyosin ring components to node-like structures"] ; [PMID:21376595 "Mid1p recruits Rng2p to cortical nodes at the division site and that Rng2p, in turn, recruits other components of the actomyosin ring to cortical nodes"]
- [PMID:16687577 "In the absence of functional Cdc15p, ring formation upon metaphase arrest depends on the anillin-like Mid1p."] — genetic interaction (IGI) supporting mitotic ring assembly.

### Molecular function: scaffold / membrane anchor / lipid binding
- [PMID:25959226 "Anillins and Mid1 are scaffold proteins that play key roles in anchorage of the contractile ring at the cell equator during cytokinesis in animals and fungi, respectively."]
- [PMID:25959226 "Mid1 also binds to the membrane through a cryptic C2 domain. Dimerization of Mid1 leads to high affinity and preference for PI(4,5)P2, which stably anchors Mid1 at the division plane, bypassing the requirement for Rho GTPase."]
- [PMID:15572668 "mid1p binds to the medial cortex by at least two independent means. First, mid1p C-terminus association with the cortex requires a putative amphipathic helix adjacent to mid1p nuclear localization sequence (NLS), which is predicted to insert directly into the lipid bilayer."]
- [PMID:15572668 "We propose that membrane-bound oligomers of mid1p assemble recruitment \"platforms\" for cytokinetic ring components at the medial cortex and stabilize the ring position during its compaction."]
- [PMID:31243991 "Purified Mid1p-N452 demixes into liquid droplets at concentrations far below its concentration in nodes. These physical properties are appropriate for scaffolding other proteins in nodes."] — condensate scaffold; N-terminal half intrinsically disordered.
- [PMID:18378776 "Clp1/Flp1 is tethered at the contractile ring (CR) through its association with anillin-related Mid1."] ; [PMID:18378776 "Mid1, unlike other tested CR components, is anchored at the cell midzone, and this physical property is likely to account for its scaffolding role."]

### Polo box / Plo1 interaction (MF: polo box domain specific binding)
- [PMID:9852154 "Plo1p is required for Mid1p to exit the nucleus and form a ring"] ; [PMID:9852154 "Genetic and two-hybrid analyses suggest that Plo1p and Mid1p act in a common pathway"]. Cdk1 phosphorylates Mid1 T517 to create a polo-box binding site (per 31243991 introduction).

### Sid2 phosphorylation / cortical removal
- [PMID:30853434 "the terminal SIN kinase, Sid2, phosphorylates Mid1 to drive its removal from the cortex at CR constriction onset."]
- [PMID:30853434 IPI interactors PomBase:SPAC31A2.16 and PomBase:SPAC57A10.02 (Sid2/Mob1 NDR complex).]

### Localization (CC)
- Nucleus: [PMID:8946912], [PMID:10930468], [PMID:9852154], [PMID:14602073], [PMID:30853434], [PMID:19427212], [PMID:19474789].
- Medial cortex / medial cortical node: [PMID:8946912], [PMID:16864655], [PMID:22918943], [PMID:19474789 nodes], [PMID:14602073], [PMID:24790095], [PMID:30853434].
- Mitotic actomyosin contractile ring: [PMID:9852154], [PMID:16864655], [PMID:18378776], [PMID:24790095], [PMID:30853434].
- Proximal (membrane-proximal) layer of CR: [PMID:28914606 "The most membrane-proximal layer (0-80 nm) is composed of membrane-binding scaffolds, formin, and the tail of the essential myosin-II."] — Mid1 is a membrane-binding scaffold in this layer.
- Nuclear envelope (HDA, ORFeome localization): [PMID:16823372] — high-throughput; nucleus signal expected, NE is a coarse HTP call.
- medial cortex during invasive filament growth: [PMID:20870879 "Bud6, Rga4, and Mid1, localize similarly in filaments and single cells"].

## Caveats / contested annotations
- **septin ring organization (GO:0031106)** annotated to mid1 from PMID:15385632 (IMP) and IBA. PMID:15385632 is about S. pombe **septins (Spns1-4) and Mid2p**; the full text does NOT mention mid1. Septin ring organization is the characterized function of the paralog **mid2** (SPCC18B5.04), not mid1. This appears to be a mid1/mid2 confusion. Given the curation rule against over-ruling experimental annotations from incomplete cache, but here the cached full text genuinely lacks any mid1 mention and septin ring organization is a well-established mid2 (not mid1) function, I mark these as likely mis-attributed / over-annotated (MARK_AS_OVER_ANNOTATED for IMP; REMOVE-leaning but conservative). Flagging for curator review.
- **protein binding (GO:0005515)** bare term — uninformative; recommend MODIFY/replace with the specific scaffold/adaptor activities where the interactor is meaningful, or KEEP_AS_NON_CORE as supporting evidence.
- **PMID:19075108** title missing in stub; this is the mitotic actomyosin contractile ring assembly EXP annotation. Not in cache.

## Core function summary
- MF: molecular adaptor/scaffold activity — protein-membrane adaptor (recruits CAR proteins to the membrane), cytoskeletal protein-membrane anchor, PI(4,5)P2 / lipid binding via C2-PH module, molecular condensate scaffold, polo-box-specific binding to Plo1.
- BP: mitotic cytokinesis division-site positioning; mitotic actomyosin contractile ring assembly; mitotic cytokinesis.
- CC: medial cortical node; mitotic actomyosin contractile ring (proximal layer); medial cortex; nucleus.
