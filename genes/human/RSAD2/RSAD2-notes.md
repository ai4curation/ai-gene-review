# RSAD2 (viperin, Q8WXG1) — curation notes

Human RSAD2 / viperin / cig5 / SAND (S-adenosylmethionine-dependent nucleotide
dehydratase). Reviewed as part of the RADICAL_SAM project. Deep research for this
gene is the asta retrieval file (`RSAD2-deep-research-asta.md`); it returned only
generic database/bioinformatics papers and no viperin-specific literature, so the
notes below were assembled from the cached primary literature and the UniProt
record. (A falcon deep-research run failed with an authentication 403 and was not
retried.)

## Core enzymology: radical SAM CTP dehydratase

- The protein is a radical SAM superfamily member with the canonical CX3CX2C motif
  and a single [4Fe-4S] cluster coordinated by Cys83/Cys87/Cys90 plus an
  exchangeable SAM
  [file:human/RSAD2/RSAD2-uniprot.txt "Note=Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3"].
- Cluster binding and radical SAM chemistry were demonstrated directly: reduced
  viperin carries a [4Fe-4S](1+) cluster whose EPR g-values shift on SAM addition,
  and incubation with SAM yields 5'-deoxyadenosine
  [PMID:20176015 "The reduced protein contains a"; "Incubation of reduced viperin with SAM results in reductive cleavage of SAM to"].
- The reconstitution of the cluster in viperin(45-361) was the first structural
  confirmation that viperin is a radical SAM enzyme
  [PMID:20026307 "we have successfully reconstituted the [4Fe-4S] cluster in Viperin (45-361)"].
- Mutating the three cluster cysteines abolishes cluster assembly and destabilises
  the protein
  [PMID:22363738 "The CX3CX2C motif is involved in iron-sulfur (Fe-S) cluster binding in"];
  the same C-to-A mutations abolish antiviral activity and 55Fe incorporation in
  cells, and SAM depletion by ectopic T3 SAMase likewise abolishes antiviral
  activity
  [PMID:24245804 "Mutation of the \ncysteine residues ligating the Fe-S cluster in the central radical SAM domain \nentirely abolished both antiviral activity and incorporation of (55) Fe"].
- The physiological reaction was identified by Gizzi et al.: CTP is the substrate
  that activates 5'-deoxyadenosine formation ~130-fold, and the product is
  3'-deoxy-3',4'-didehydro-CTP (ddhCTP), formed by dehydration (loss of the
  4'-hydrogen and the 3'-hydroxyl) without rearrangement of the carbon skeleton;
  Km(CTP) = 183 uM, one 5'dA per ddhCTP
  [PMID:29925952 "CTP selectively activates 5′dA production by ~130-fold relative to protein alone"].
- ddhCTP is a chain terminator for flavivirus RdRps (dengue, West Nile, Zika, HCV),
  but not for rhinovirus/poliovirus RdRps — so susceptibility is virus-dependent
  [PMID:29925952 "as expected for the action of chain terminators"; "we conclude that not all RdRps are sensitive to ddhCTP"].
- UniProt records the reaction and EC 4.2.-.- (RHEA:65944)
  [file:human/RSAD2/RSAD2-uniprot.txt "Reaction=CTP + AH2 + S-adenosyl-L-methionine = 3'-deoxy-3',4'-"].
- **Ontology gap:** GO has no term for this activity. QuickGO/OLS searches for
  "ddhCTP", "CTP dehydratase", "didehydro-CTP" and "nucleotide dehydratase"
  (2026-10-18) return nothing matching; the nearest parent is GO:0016836 hydro-lyase
  activity. Hence `proposed_new_terms` + `proposed_molecular_function` in the review.

## Localization

- Peripheral protein on the **cytosolic face of the ER membrane**, targeted by the
  N-terminal amphipathic helix (residues 1-42); the helix is necessary and
  sufficient for ER targeting
  [PMID:19074433 "viperin specifically localizes to the cytoplasmic face of the ER"].
- **Lipid droplets** are the second resting site; in pDCs viperin localizes to lipid
  bodies and recruits IRAK1/TRAF6 there [PMID:21435586], and in HSV-1 infection it
  colocalizes with gD at Golgi and lipid droplets
  [PMID:31921110 "gD and viperin co-localized at the Golgi body and lipid droplets"].
  At the HCV replication complex viperin sits at the lipid-droplet interface with
  NS5A and VAP-A [PMID:22045669].
- **Golgi** localization is largely infection-driven redistribution: HCMV infection
  moves viperin from the ER first to the Golgi and then to gB/pp28-containing
  vacuoles [PMID:11752458 "HCMV infection"].
- **Mitochondrial** localization is also infection-driven: HCMV vMIA/UL37 binding
  relocalizes viperin from the ER to mitochondria, where it binds the trifunctional
  protein (HADHB) and lowers ATP
  [PMID:21527675 "Viperin interaction with \nthe viral protein vMIA resulted in viperin relocalization from the endoplasmic \nreticulum to the mitochondria"].
  This is a virus-coopted, not a constitutive, location, and UniProt's mitochondrial
  inner/outer-membrane statements carry no publication evidence tags.

## Antiviral function

- Broad-spectrum inhibition of DNA and RNA viruses; IFN type I/II-inducible
  [PMID:11752458, PMID:16108059, PMID:16982913, PMID:17686841].
- Anti-HCV activity in replicon and HCVcc systems, requiring the C-terminus; viperin
  competes with HCV NS5A for VAPA/hVAP-33 binding
  [PMID:21957124 "viperin could \ninteract competitively with hVAP-33"], and interacts with NS5A at the LD
  interface [PMID:22045669].
- TBEV: viperin inhibits viral genome RNA synthesis, requires ER localization, the
  Fe-S cluster, SAM, and the CIA factor CIAO1 for cluster maturation
  [PMID:24245804 "acts through an enzymatic, Fe-S cluster- and \nSAM-dependent mechanism to inhibit viral RNA synthesis"].
- EV-A71: viperin binds the viral 2C protein via residues 50-60 of its N-terminus
  [PMID:30587778 "viperin interacts and colocalizes with the EVA71 protein 2C in the endoplasmic reticulum"].
- ZIKV: the conserved C-terminal K358 is required for antiviral activity
  [PMID:30934824].
- HCMV is the notable exception: HCMV coopts viperin (via vMIA) to disrupt fatty-acid
  beta-oxidation/ATP generation and the actin cytoskeleton, *enhancing* infection
  [PMID:21527675].
- Influenza A: viperin perturbs lipid rafts and inhibits virus budding, through
  inhibition of farnesyl diphosphate synthase (FPPS)
  [PMID:18005724 "Intracellular interaction of viperin with farnesyl diphosphate"].
  This predates the ddhCTP work and is an indirect, lipid-metabolism-mediated effect.

## Innate immune signalling (second genuine function)

- In pDCs, viperin is required for TLR7- and TLR9-induced type I IFN: it recruits
  IRAK1 and TRAF6 to lipid bodies and facilitates K63-linked IRAK1 ubiquitination,
  driving IRF7 nuclear translocation; loss of viperin reduces TLR7/9-induced IFN but
  not nucleic-acid-sensor-induced IFN (mouse)
  [PMID:21435586 "Viperin interacted with the signal \nmediators IRAK1 and TRAF6 to recruit them to the lipid bodies"].
- Human reconstitution confirms the scaffold role is a real, bidirectional coupling:
  IRAK1+TRAF6 raise viperin's CTP dehydratase activity ~10-fold, and conversely
  TRAF6-mediated IRAK1 ubiquitination requires viperin association with both — and
  does **not** require catalytically active viperin
  [PMID:30872404 "IRAK1 and TRAF6 increase viperin activity ∼10-fold"].
  So viperin performs work in the TLR7/9 branch (adaptor/scaffold), independent of
  its catalysis.
- HSV-1 gD binding increases IRF7-mediated IFN-beta by promoting the
  viperin-IRAK1 interaction [PMID:31921110].

## Pleiotropic / peripheral effects

- Mouse knockout: CD4+ T cells show impaired Th2 cytokine production (IL-4/5/13) and
  impaired GATA3 activation, with reduced NF-kB1/p50 and AP-1/JunB DNA binding;
  proliferation and IL-2 are normal
  [PMID:19047684 "viperin facilitates TCR-mediated GATA-3 activation and optimal Th2 cytokine production"].
  Real but downstream/modulatory, and only established in mouse; the human rows for
  these terms are ISS/IEA from Q8CBB9.
- Inhibition of secretion of soluble proteins is an overexpression-associated
  consequence of the N-terminal helix inducing crystalloid ER; membrane-protein
  transport is unaffected
  [PMID:19074433 "Expression of intact viperin or an N-terminal alpha-helix-dsRed fusion protein significantly reduced secretion of soluble alkaline phosphatase"].
- Protein turnover: HAT1 acetylates K197, recruiting UBE4A, which drives K6-linked
  polyubiquitination at K206 and proteasomal degradation [PMID:31812350].
- Up-regulated in atherosclerosis (UniProt MISCELLANEOUS) — expression correlation,
  not a function.

## Interaction rows (GO:0005515)

Partners in the GOA rows: HCMV UL37/vMIA (P16778, viral), HADHB (P55084), VAPA
(Q9P0L0, two papers), CIAO1 (O76071, Fe-S maturation factor), and three HuRI binary
screen hits — APOC1 (P02654), APOC4 (P55056), RHBDD2 (Q6NTF9-3)
[PMID:32296183]. All are uninformative as `protein binding`; none supports a
specific molecular function for viperin itself (CIAO1 makes viperin the *client* of
cluster maturation, not the possessor of a new activity). Per repository policy these
rows are removed as uninformative, which does not dispute the interactions.

## Comparator / NEW-term reasoning

- No `NEW` process terms proposed. The one tempting candidate was
  `GO:0032728 positive regulation of interferon-beta production`: viperin does
  perform work in that branch (scaffolding IRAK1/TRAF6 K63-ubiquitination), but the
  existing `GO:0034157`/`GO:0034165` rows already assert the pathway-level positive
  regulation it mediates, and GO:0032728 would add a second, partly overlapping
  claim from mouse-only knockout data plus one human reporter assay. Raised as a
  suggested question instead.
- Two `NEW` molecular-function rows are added where the evidence is direct and the
  claim is cofactor/cosubstrate binding, consistent with the RADICAL_SAM project's
  treatment of these rows across the family: `GO:1904047` S-adenosyl-L-methionine
  binding (EPR g-value shift on SAM addition and reductive SAM cleavage,
  PMID:20176015; UniProt BINDING "4Fe-4S-S-AdoMet") and `GO:0030674`
  protein-macromolecule adaptor activity for the IRAK1/TRAF6 scaffold function
  (PMID:30872404 human reconstitution; PMID:21435586 mouse pDCs) — viperin itself
  positions the kinase and the E3 ligase, which is the work the term names, and the
  function is separable from catalysis.
