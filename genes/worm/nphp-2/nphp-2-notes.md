# nphp-2 (C. elegans) — research notes

Gene: nphp-2 / Y32G9A.6 / WBGene00021304
UniProt: Q9BPN3 (TrEMBL, unreviewed, PE=4 Predicted), 812 aa, ANK-repeat protein.
Human ortholog: INVS (inversin / nephrocystin-2, NPHP2). Ciliary "inversin compartment" protein.
Project: CAEEL_CILIOPATHY (flagship). Reviewed as a transition-zone-adjacent / inversin-compartment protein.

## Identity verification (done)

- UniProt Q9BPN3 GN=nphp-2, ORF Y32G9A.6a, WormBase WBGene00021304, taxon 6239. Confirmed.
- UniProt DR lines already carry two experimental GO annotations from WormBase:
  - GO:0097543 ciliary inversin compartment (IDA)
  - GO:1904108 protein localization to ciliary inversin compartment (IMP)
- Domain architecture (UniProt/InterPro): ankyrin-repeat region (11 ANK by SMART; PF00023/PF12796/PF13637),
  several disordered regions; no catalytic domain. PANTHER PTHR24198 (ankyrin repeat family).
- IMPORTANT ortholog nuance: there are TWO C. elegans ANK-repeat "inversin-like" proteins.
  - **nphp-2 / Y32G9A.6** = the *ciliary* inversin ortholog used in the Barr/Leroux sensory-cilia
    studies; selected as closest ortholog by X-box promoter usage + domain conservation
    [falcon report; warburtonpitt2012].
  - **mlt-4** = the INVS homolog that forms the canonical vertebrate-style "Inversin complex"
    (MLT-4/NEKL-2/MLT-2 = INVS/NEK8/ANKS6) but functions at **epithelial junctions in molting,
    not cilia** [PMID:39110529 Beyrent 2024, "loss-of-function mutations in the INVS homolog, MLT-4,
    result in a lethal-molting phenotype"; "the C. elegans homologues colocalize, albeit at
    epithelial junctions rather than cilia"].
  This is a genuine knowledge gap: which worm protein is the true functional inversin ortholog, and
  how the ciliary NPHP-2 relates to the junctional MLT-4/NEKL-2/MLT-2 complex, is unresolved.

## Existing GOA annotations (3)

From nphp-2-goa.tsv (all WB-assigned):
1. GO:0003674 molecular_function — ND, GO_REF:0000015 (root placeholder; no MF assigned).
2. GO:0097543 ciliary inversin compartment — IDA, PMID:25335890, located_in.
3. GO:1904108 protein localization to ciliary inversin compartment — IMP, PMID:25335890, involved_in.

Both experimental annotations trace to PMID:25335890 (Nguyen 2014, AFD thermosensory neuron paper).

## Key literature (cached)

### PMID:25335890 (Nguyen, Liou, Hall, Leroux 2014, J Cell Sci) — abstract-only in cache
AFD thermosensory neuron bipartite signaling compartment.
- [PMID:25335890 "requires NPHP-2 (known as inversin in mammals) to anchor a cGMP-gated ion channel
  within the proximal ciliary region"] — NPHP-2 anchors the cGMP-gated channel (TAX-2/TAX-4) in the
  proximal cilium (the InvC region). This is the source of both GOA experimental annotations.
- [PMID:25335890 "One compartment, a bona fide cilium, is delineated by proteins associated with
  Bardet-Biedl syndrome (BBS), Meckel syndrome and nephronophthisis at its base"] — NPHP as base/TZ
  ciliopathy proteins.

### PMID:22393243 (Warburton-Pitt, Jauregui, Li, Wang, Leroux, Barr 2012, J Cell Sci) — abstract-only
"Ciliogenesis in C. elegans requires genetic interactions between ciliary middle segment localized
NPHP-2 (inversin) and transition zone-associated proteins."
- [PMID:22393243 "the C. elegans inversin ortholog, NPHP-2, localizes to the middle segment of
  sensory cilia"] — MIDDLE SEGMENT (InvC), NOT the transition zone. KEY distinction vs nphp-1/nphp-4.
- [PMID:22393243 "nphp-2 is partially redundant with nphp-1 and nphp-4 ... for cilia placement within
  the head and tail sensilla"].
- [PMID:22393243 "nphp-2 also genetically interacts with MKS ciliopathy gene orthologs, including
  mks-1, mks-3, mks-6, mksr-1 and mksr-2, in a sensilla-dependent manner to control cilia formation
  and placement"].
- [PMID:22393243 "nphp-2 is not required for correct localization of the NPHP- and MKS-encoded ciliary
  transition zone proteins or for intraflagellar transport (IFT)"] — NOT a TZ-assembly or IFT gene.
- [PMID:22393243 "nphp-2 plays an important role in C. elegans cilia by acting as a modifier of the
  NPHP and MKS pathways to control cilia formation and development"].

### PMID:25501555 (Warburton-Pitt, Silva, Nguyen, Hall, Barr 2014, PLoS Genet) — FULL TEXT cached
"The nphp-2 and arl-13 genetic modules interact to regulate ciliogenesis and ciliary microtubule
patterning in C. elegans." Most detailed nphp-2 paper.
- InvC conserved & distinct from doublet region:
  [PMID:25501555 "We show that the InvC is conserved and distinct from the doublet region."]
  [PMID:25501555 "nphp-2 (the C. elegans Inversin homolog) and the doublet region genes arl-13,
  klp-11, and unc-119 are redundantly required for ciliogenesis."]
- Two modules antagonized by hdac-6:
  [PMID:25501555 "InvC and doublet region genes can be sorted into two modules-nphp-2+klp-11 and
  arl-13+unc-119-which are both antagonized by the hdac-6 deacetylase."]
- Microtubule patterning + anchoring:
  [PMID:25501555 "These defects indicate that nphp-2 is required both for microtubule patterning and
  for cilia anchoring."]
- Glutamylation is downstream:
  [PMID:25501555 "glutamylation is modulated by nphp-2, arl-13, and unc-119"]
- EF-hand required for InvC targeting & function:
  [PMID:25501555 "NPHP-2 does require its calcium binding EF hand domain for targeting to the InvC."]
  [PMID:25501555 "the calcium-binding EF-hand plays a significant role in both localization and
  function of NPHP-2 in amphid channel and phasmid cilia"]
- Ciliary targeting independent of TZ/DR/InvC genes:
  [PMID:25501555 "The ciliary targeting and restricted localization of NPHP-2, ARL-13, and UNC-119
  does not require TZ-, doublet region, and InvC-associated genes."]
- Marks a region distinct from the doublet region (= InvC):
  [PMID:25501555 "We conclude that NPHP-2 marks a region of the cilium distinct from the doublet
  region, and propose that this region is analogous to the InvC of mammalian cilia."]
- GAP statements (field's own admissions):
  [PMID:25501555 "The mechanisms that establish and maintain the InvC are unknown."]
  [PMID:25501555 "how the InvC is initially established is not known."]
  [PMID:25501555 "the origin and nature of the calcium signal these domains detect is unknown."]
  [PMID:25501555 "The next challenge is to determine what initially patterns the doublet region and
  InvC, and to understand the function of these cilia regions."]
  [PMID:25501555 "Determining the mechanism by which HDAC-6 acts as a genetic modifier of InvC and
  doublet region gene defects is an important future direction."]
  EF-hand mechanism unresolved:
  [PMID:25501555 "Two possibilities arise for the function of these domains: Ca2+ specifies the
  localization of NPHP-2, modulates the activity of the protein, or both."]

### PMID:39110529 (Beyrent 2024, Mol Biol Cell) — FULL TEXT cached — background/ortholog nuance
Inversin complex activated by dimerization; but the worm complex is MLT-4/NEKL-2/MLT-2, functioning
at epithelial junctions in molting, NOT the ciliary NPHP-2/Y32G9A.6.
- [PMID:39110529 "loss-of-function mutations in the INVS homolog, MLT-4, result in a lethal-molting
  phenotype"]
- [PMID:39110529 "the C. elegans homologues colocalize, albeit at epithelial junctions rather than
  cilia"]
- [PMID:39110529 "we lack fundamental knowledge about how the components might assemble into a
  functionally active state"]
Use only for the ortholog-assignment knowledge gap; do NOT attribute MLT-4 findings to nphp-2.

### Deep research: nphp-2-deep-research-falcon.md (Edison Scientific Literature, 25 citations)
Genuine, corroborates all of the above. Adds: two isoforms (NPHP-2L middle-segment/InvC; NPHP-2S
broader, TZ/nucleus-excluded); ankyrin repeats support ciliary targeting (AWB); required for TAX-2
(and partly TAX-4) proximal-cilium localization; NPHP-2 not an enzyme/transporter — a structural
organizer/genetic modifier. Falcon file:-quotes are NOT validator-checked, so I anchor claims to
PMID quotes above wherever used.

## KNOWN vs NOT-KNOWN (explicit)

KNOWN:
- NPHP-2 is the ciliary C. elegans inversin/INVS(NPHP2) ortholog; ANK-repeat protein, non-catalytic.
- Localizes to the ciliary inversin compartment (InvC) = middle/proximal doublet region of amphid &
  phasmid sensory cilia, distal to the TZ (IDA, PMID:25335890; PMID:22393243; PMID:25501555).
- Required for microtubule ultrastructural patterning and cilia anchoring/placement; ciliogenesis
  (redundant with nphp-1/nphp-4 and with arl-13/klp-11/unc-119 modules).
- Required to anchor/localize the cGMP-gated channel TAX-2(/TAX-4) in the proximal cilium
  (PMID:25335890) → basis of GO:1904108 (protein localization to InvC, IMP).
- Regulates tubulin glutamylation (upstream), interacts genetically with MKS module and hdac-6.
- Its EF-hand (Ca-binding) domain is required for InvC targeting and function (PMID:25501555).

NOT KNOWN / uncertain:
- No direct molecular function assigned (ND at MF root is currently accurate); whether the EF-hand
  actually binds Ca2+ biochemically (predicted, not shown) and whether Ca sensing specifies
  localization vs modulates activity.
- How the InvC is initially established/patterned (field states this is unknown).
- Direct binding partners of NPHP-2 in the worm InvC; whether it scaffolds a NEK8/ANKS6-like
  complex in cilia (the classical complex uses MLT-4 at junctions, PMID:39110529).
- Mechanism by which HDAC-6 antagonizes InvC/doublet-region gene function.
- Whether worm NPHP-2 has any Wnt/PCP role (mammalian inversin does; disputed; untested in worm).

## Curation plan

- GO:0003674 ND → ACCEPT (no MF experimentally defined; accurate placeholder). Note EF-hand
  Ca-binding as an ONTOLOGY/BIOLOGY knowledge-gap MF candidate, not a confident core MF.
- GO:0097543 ciliary inversin compartment (IDA) → ACCEPT, CORE localization.
- GO:1904108 protein localization to ciliary inversin compartment (IMP) → ACCEPT, CORE process
  (channel anchoring in the InvC).
- core_functions: InvC localization (CC) + protein localization to InvC / non-motile cilium assembly
  (BP). No confident MF (leave MF unpopulated / note gap).
- knowledge_gaps: (1) MF-dark — no molecular activity; EF-hand Ca-binding unverified (biology+ontology);
  (2) how the InvC is established/patterned & NPHP-2's direct partners (biology, residual sub-gap);
  (3) ortholog-assignment: ciliary NPHP-2 vs junctional MLT-4/NEKL-2/MLT-2 Inversin complex (biology).
