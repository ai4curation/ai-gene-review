# sid2 (Q09898, SPAC24B11.11c) review notes

Sid2 is the NDR/LATS-family Ser/Thr protein kinase that is the most downstream
effector of the Septation Initiation Network (SIN) in *S. pombe*. With regulatory
subunit Mob1 it forms the Sid2-Mob1 complex, localizes to the SPB throughout the
cell cycle, and translocates transiently to the cell-division site/contractile
ring at the end of anaphase to trigger ring constriction and septum formation.

## Core function & localization

- Sid2 is a SPB-resident kinase that localizes transiently to the division site during ring
  constriction and septation; localization and activity depend on all other SIN genes
  (cdc7, cdc11, cdc14, sid1, spg1, sid4) [PMID:10459013 "Here, we show that Sid2p is a component of the
  spindle pole body at all stages of the cell cycle and localizes transiently to the cell division
  site during medial ring constriction and septation."].
- In vitro kinase assay established; Sid2 kinase activity peaks during medial ring constriction and
  septation [PMID:10459013 "We have established an in vitro assay for measuring Sid2p kinase activity,
  and found that Sid2p kinase activity peaks during medial ring constriction and septation."].
- A kinase-dead version (K238R) was made, confirming ATP-binding/kinase function [PMID:10459013
  "a point mutation in the sid2 gene at a site that would alter the proposed ATP-binding domain of the kinase (K238 to R)"].
- Function: required for initiation of medial ring constriction and septation (UniProt FUNCTION,
  ECO:0000269|PubMed:10459013).

## Mob1 interaction / Sid2-Mob1 complex

- Mob1p can be precipitated with Sid2p [PMID:10769201 "We also demonstrate that mob1p can be precipitated
  from cells in a complex with the septation regulating kinase sid2p."].
- Mob1p associates with Sid2p; both required for initiation of cytokinesis; Mob1 required for Sid2
  localization [PMID:10837231 "Mob1p associates with the Sid2p kinase and like Sid2p, Mob1p is required
  for the initiation of cytokinesis, but not for mitotic exit."].
- Mob1 required for Sid2 SPB localization AND kinase activity; N-terminal region of Sid2 binds Mob1;
  Thr578 phosphorylation important [PMID:15060149 "Mob1p is required not only for the subcellular localization
  of Sid2p but also for its kinase activity."].

## Substrates / signaling outputs

- Sid2 directly phosphorylates Clp1/Flp1 (Cdc14-family phosphatase), creating Rad24 (14-3-3) binding sites,
  retaining Clp1 in cytoplasm [PMID:18951025 "the most downstream SIN component, the Ndr-family kinase Sid2,
  maintains Clp1 in the cytoplasm in late mitosis by phosphorylating Clp1 directly"]; direct phosphorylation
  shown [PMID:18951025 "Sid2 kinase purified by tandem affinity purification (TAP) from yeast cells was capable
  of directly phosphorylating bacterially produced Clp1 (Figure 1A)."].
- Rad24-Clp1 interaction depends on Sid2 (cytokinesis checkpoint) [PMID:16085489 "This physical interaction
  depends on the function of the SIN component, Sid2p."].
- Sid2 phosphorylates Cdc11 (SIN scaffold) — positive feedback, SIN asymmetry [PMID:22419817 "the last protein
  kinase in the signaling cascade, Sid2, feeds back to phosphorylate Cdc11 during mitosis."].
- Sid2 phosphorylates the cytokinetic formin Cdc12 to inhibit multimerization [PMID:24115772 "we identify the
  essential cytokinetic formin Cdc12 as a key CR substrate of SIN kinase Sid2."].
- Sid2 phosphorylates Mid1 (anillin) to drive it from the cortex at constriction onset [PMID:30853434 "the
  terminal SIN kinase, Sid2, phosphorylates Mid1 to drive its removal from the cortex at CR constriction onset."].
- Sid2 phosphorylates MOR components Nak1 and Sog2 (SIN-MOR crosstalk) [PMID:23394829 "multiple substrates
  of the SIN effector kinase Sid2, including the MOR pathway components Nak1 kinase and an associated protein, Sog2."].
- SIN inhibits MOR via Sid2 phosphorylation of Nak1 [PMID:20805322 "The SIN inhibits MOR signaling in mitosis
  by interfering with Nak1 kinase-mediated activation of the most downstream MOR component, the NDR family kinase Orb6."].
- SIN/Sid2 inhibition of MOR enforces temporal ordering / prevents premature cell separation [PMID:24972934
  "SIN inhibition of the MOR enforces proper temporal ordering of cytokinetic events."].
- G2 role: Sid2-Mob1 activates Fin1 NIMA kinase to control mitotic commitment via Pom1/Wee1 [PMID:22684255
  "Sid2-Mob1, acts independently of the other known SIN components in G2 phase of the cell cycle to control
  the timing of mitotic commitment. Sid2-Mob1 promotes mitotic commitment by directly activating the
  NIMA (Never In Mitosis)-related kinase Fin1."].

## Node / contractile ring biology

- SIN activity disperses type 1 nodes (Cdr2/Mid1) — Sid2 active at mitotic SPB and contractile ring
  [PMID:25501814 "SIN activity is necessary and sufficient to disperse the type 1 node proteins Cdr2p and
  Mid1p into the cytoplasm"].
- Sid2/Mob1 localize to intermediate layer of contractile ring (80-160 nm from membrane)
  [PMID:28914606 "An intermediate layer (80-160 nm) consists of a network of cytokinesis accessory proteins
  as well as multiple signaling components which influence cell division."].
- Blt1p physically interacts with Sid2p/Mob1p; recruits them to division site [PMID:24790095 "Blt1p interacts
  physically with Sid2p and Mob1p, a protein kinase complex of the septation initiation network"].
- Blt1p and Gef2p localize Sid2p/Mob1p to division site, promote timely constriction [PMID:31041892 "Blt1p
  and Gef2p work in the same pathway, rather than in parallel, to localize the NDR-family kinase Sid2p and
  its regulatory partner Mob1p to the division site"].
- Septum/furrow ingression begins in early anaphase; reduced SIN activity triggers medial recruitment of
  Sid2-Mob1 [PMID:29813053 "the reduced SIN activity present after Cdk1 loss was enough to trigger septation
  by immediately inducing the medial recruitment of the SIN kinase complex Sid2-Mob1."].

## Meiosis

- SIN required for spore formation; SIN proteins localize to SPB in meiosis [PMID:16787941 "The SIN proteins
  localise to the spindle pole body in meiosis."].

## PP2A-Pab1

- Pab1 (PP2A B subunit) physically interacts with Sid2 (and Mob1, Sid1, Cdc11) by two-hybrid [PMID:20876564
  "Two-hybrid assays indicate that Pab1 physically interacts with Mob1, Sid1, Sid2, and Cdc11"]. The GOA
  protein-binding IPI (WITH SPAC227.07c = pab1) derives from this.

## Notes on GOA peculiarities

- Many duplicate "protein serine/threonine kinase activity" IDA/EXP rows (PMID:23394829 x6, 24972934 x2,
  16787941 x2, 25501814, etc.) — these are PomBase annotations from different figures; all ACCEPT.
- "protein binding" (GO:0005515) IPI rows: PMID:10769201 (Mob1) and PMID:20876564 (pab1). Bare protein
  binding is uninformative MF; the Mob1 interaction is better captured by the Sid2-Mob1 complex CC term.
- PMID:23087209 full text not cached (title not fetched); it is McLean et al. or similar SIN paper assayed
  Sid2 kinase activity and spindle elongation / nuclear migration in telophase (PomBase IDA/IMP). Accept/defer.
