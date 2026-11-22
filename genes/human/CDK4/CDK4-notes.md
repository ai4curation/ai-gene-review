# CDK4 (human, P11802) — curation notes

## Identity and core biology

CDK4 = cyclin-dependent kinase 4 (EC 2.7.11.22), a 303-aa CMGC-group Ser/Thr protein
kinase, CDC2/CDKX subfamily. It is the catalytic subunit of the cyclin D-CDK4 ("DC")
holoenzyme. Its defining, best-established function is to phosphorylate the
retinoblastoma (RB) family pocket proteins RB1/pRb, RBL1/p107 and RBL2/p130 in early-mid
G1, relieving their repression of E2F and driving the G1/S transition.

- UniProt FUNCTION: "Ser/Thr-kinase component of cyclin D-CDK4 (DC) complexes that
  phosphorylate and inhibit members of the retinoblastoma (RB) protein family including
  RB1 and regulate the cell-cycle during G(1)/S transition." [file:human/CDK4/CDK4-uniprot.txt]
- [PMID:19237555 "Cyclin-dependent kinase 4 (CDK4)/cyclin D complexes are expressed early in the G(1) phase of the cell cycle and stimulate the expression of genes required for G(1) progression by phosphorylation of the product of the retinoblastoma gene, pRb."]
- [PMID:22094256 "These complexes promote G1-S transition in cancer cells by phosphorylating critical substrates, of which the Retinoblastoma tumor suppressor protein, RB1, as well as the related family members, RBL1 (p107) and RBL2 (p130), remain best characterized."]
- [PMID:19237565 "The cyclin D1-cyclin-dependent kinase 4 (CDK4) complex is a key regulator of the transition through the G(1) phase of the cell cycle."]

## Activation and regulation

- Requires BOTH binding of a D-type cyclin (CCND1/2/3) AND activation-loop phosphorylation
  at Thr172 (UniProt ACTIVITY REGULATION; MOD_RES 172 phosphothreonine).
- Cyclin binding is obligatory and is the meaningful MF underlying the many D-cyclin
  "protein binding" rows. [PMID:11896535 "immune complexes consisting of cyclin D2 and cdk4 or cyclin D3 and cdk4 were both functional and phosphorylated the RB protein in vitro."]
- CIP/KIP proteins (p21/CDKN1A, p27/CDKN1B, p57/CDKN1C) both promote assembly and, at
  higher stoichiometry, inhibit; they are assembly factors, not only inhibitors.
  [PMID:9106657 "the CDK inhibitors p21(CIP), p27(KIP), and p57(KIP2) all promote the association of cdk4 with the D-type cyclins."]
- INK4 proteins (p16/CDKN2A, p15/CDKN2B, p18/CDKN2C, p19/CDKN2D) specifically bind and
  inhibit CDK4/6.
  [PMID:8259215 "p16 binds to CDK4 and inhibits the catalytic activity of the CDK4/cyclin D enzymes."]
  [PMID:7603984 "p16ink4 specifically binds and inhibits the cyclin-dependent kinases 4 and 6."]
- Hsp90-Cdc37 chaperone stabilizes/matures CDK4 before complex assembly.
  [PMID:9150368 "Cdc37 protein specifically interacts with Cdk4 and Cdk6, but not with Cdc2, Cdk2, Cdk3, Cdk5"]
  [PMID:27339980 "cryo-electron microscopy structure of the Hsp90-Cdc37-Cdk4 kinase complex."]

## Localization

Cytoplasmic when uncomplexed; cyclin D-CDK4 assembles in the cytoplasm, accumulates at
the nuclear membrane and enters the nucleus at the G1→S transition, colocalizing with RB1.
Also present in nucleoli and heterochromatin lumps.
[PMID:18827403 "They accumulated on the cytosolic surfaces of the nuclear pores and then were arrested at the nuclear membrane"]
[PMID:18827403 "the complex was released into the nucleus and colocalized with pRb there, which led to pRb phosphorylation and DNA synthesis."]
Core functional location = nucleus/nucleoplasm (site of RB phosphorylation); cytosol =
resting/assembly pool.

## Metazoan-specific G1 CDK

CDK4/CDK6 with cyclin D are the dedicated metazoan G1 CDKs; the repository module
`modules/g1_s_transition.yaml` uses CDK4 (UniProtKB:P11802) as the metazoan exemplar of
the "G1 cyclin-dependent kinase" family node (PANTHER:PTHR24056; PAINT node
PTN000623980). GO-CAM `gocams/61e0e55600000624` models CDK4 with GO:0004693 acting in
GO:0000082 (G1/S transition).

## Curation decisions (summary)

- **Molecular function**: kinase activity terms (GO:0004693, GO:0106310, GO:0004672,
  GO:0016301), ATP binding (GO:0005524) and cyclin binding (GO:0030332) all ACCEPT — core.
- **GO:0016538** cyclin-dependent protein serine/threonine kinase *regulator* activity
  (TAS, Reactome): this MF describes the cyclin/regulatory subunit, not the catalytic
  kinase. CDK4 is the catalyst → MODIFY to GO:0004693.
- **Complexes/locations**: GO:0000307 (CDK holoenzyme), GO:0097128/9/30 (cyclin
  D1/2/3-CDK4 complexes), nucleus (GO:0005634), nucleoplasm (GO:0005654), cytoplasm
  (GO:0005737), cytosol (GO:0005829) ACCEPT. Nuclear membrane (GO:0031965), nucleolus
  (GO:0005730), chromatin (GO:0000785) KEEP_AS_NON_CORE (real but transient/minor pools).
- **Over-propagated ortholog IEA CC** (GO_REF:0000107): transcription regulator complex
  (GO:0005667) and bicellular tight junction (GO:0005923) → MARK_AS_OVER_ANNOTATED
  (CDK4 phosphorylates transcription factors but is not a structural subunit of these
  complexes; tight-junction localization is a spurious ortholog transfer).
- **G1/S** (GO:0000082) ACCEPT — core BP. **G2/M** (GO:0000086, IBA) KEEP_AS_NON_CORE —
  reflects the pan-CDK ancestral node (PTN000623979); CDK4 itself is a G1 kinase.
- **GO:0010971** positive regulation of G2/M (IDA, INSM1 paper): the flow-cytometry
  readout of cells reaching G2/M after cyclin D1-CDK4 released a G1/S block; CDK4's direct
  role is at G1/S → MARK_AS_OVER_ANNOTATED.
- **Generic/indirect BP**: signal transduction (GO:0007165), regulation of gene
  expression (GO:0010468), regulation of cell cycle (GO:0051726), positive regulation of
  cell population proliferation (GO:0008284), positive regulation of fibroblast
  proliferation (GO:0048146) → KEEP_AS_NON_CORE (downstream/general). Regulation of
  transcription initiation by Pol II (GO:0060260, Reactome generic pathway) and response
  to xenobiotic stimulus (GO:0009410, IEP: cdk4 mRNA merely falls after sulindac) →
  MARK_AS_OVER_ANNOTATED.
- **GO:0005515 protein binding (167 IPI rows)**: per repository policy, bare protein
  binding is uninformative. D-cyclin partners (CCND1/P24385, CCND2/P30279, CCND3/P30281)
  → MODIFY to cyclin binding (GO:0030332), the evidence-backed informative MF. All other
  partners (INK4/CIP-KIP inhibitors, HSP90AB1, CDC37, RBL1/2, MYC, CEBPA, APOBEC3B,
  FNIP1/2, FBXW7, RNF26, UCHL1, PSMD10, ZNF655, HOOK1, IKZF3, INCA1, OGDHL, CDK7, and the
  Legionella effector lpg1972) → REMOVE (real interactions, but the bare term carries no
  functional information and no specific MF is invented from interaction data alone). The
  underlying interactions are documented in UniProt SUBUNIT/INTERACTION and remain valid.

## Disease
Familial/cutaneous melanoma (CMM3; e.g. R24C variant abrogating p16 binding) and
autosomal-recessive primary microcephaly 31 (MCPH31). CDK4/6 inhibitors (palbociclib,
ribociclib, abemaciclib) are established in HR+/HER2- breast cancer.
