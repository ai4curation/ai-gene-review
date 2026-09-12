# RNF41 / NRDP1 / FLRF review notes

UniProt: Q9H4P4 (RNF41_HUMAN), 317 aa. EC 2.3.2.27. RING-type E3 ubiquitin-protein ligase.
Synonyms: NRDP1 (neuregulin receptor degradation protein-1), FLRF, RING finger protein 41.

## Domain architecture
- RING-type zinc finger 18..57 (degenerate; catalytic, engages E2). Catalytic residues
  Cys34/His36/Asp56 required for activity [UniProt MUTAGEN: C34S+H36Q loss of activity;
  D56V loss of activity].
- SIAH-type zinc finger 78..138 (degenerate).
- C-terminal substrate/USP8-binding domain (PDB 2FZP/2GWF, residues 193-317); dimerizes;
  binds substrate ErbB3 and the DUB USP8.
  [PMID:27353365 "N-terminal RING finger domain responsible for engaging E2...The C-terminal
  domain of Nrdp1 is responsible for binding its substrate ErbB3...as well as the
  deubiquitinase USP8"]
- Originally described as an RBCC/TRIM-like protein. [PMID:11867753]

## Core molecular function
- RING-type E3 ubiquitin-protein ligase / ubiquitin-protein transferase (EC 2.3.2.27).
  Genuine catalytic RING E3. [UniProt EC 2.3.2.27; CATALYTIC ACTIVITY E2~Ub -> substrate Lys]
- Autoubiquitinated -> proteasomal degradation; stabilized by USP8 (deubiquitination).
  [PMID:15314180 "Nrdp1 protein undergoes efficient proteasome-dependent degradation and
  that mutations in its RING finger domain that disrupt ubiquitin ligase activity enhance
  stability"; "USP8 markedly enhanced the stability of Nrdp1"]
- Zinc ion binding (RING + SIAH-type Zn finger) [UniProt KW Zinc-finger].

## Substrates / processes (heart of RNF41 biology)
- ErbB3 (and ErbB4) — Nrdp1 binds the receptor cytoplasmic tail (activation-independent) and
  mediates growth-factor-independent ubiquitination and proteasomal/ERAD degradation,
  maintaining steady-state ErbB3/ErbB4 levels; specific for ErbB3/ErbB4, NOT EGFR/ErbB2.
  Loss of Nrdp1 raises ErbB3 and enhances ErbB2/ErbB3 breast tumor growth, migration,
  MAPK and PI3K/AKT signaling.
  [PMID:11867753; PMID:27353365 "the E3 ubiquitin ligase Nrdp1...targets ErbB3 and ErbB4 for
  degradation"; PMID:17145873 "loss of Nrdp1 enhances ErbB2/ErbB3-dependent breast tumor cell
  growth"] Reactome: RNF41 ubiquitinates ERBB3 (R-HSA-1358790/1358792).
  - Rtn4A/Nogo-A sequesters Nrdp1 in ER tubules and suppresses its function, stabilizing
    ErbB3. Nrdp1 localizes to cytosol/perinuclear region and redistributes to ER tubules.
    [PMID:27353365 "Rtn4A overexpression induced the redistribution of Nrdp1 from a cytosolic
    or perinuclear localization to ER tubules"]
- BIRC6/BRUCE/Apollon — Nrdp1 binds and ubiquitinates the giant IAP BRUCE, promoting its
  proteasomal degradation and triggering apoptosis (extrinsic/intrinsic). USP8 stabilizes
  Nrdp1 which then induces apoptosis.
  [PMID:14765125 "purified Nrdp1 catalyzes BRUCE ubiquitination...overexpression of Nrdp1
  promotes ubiquitination and proteasomal degradation of BRUCE...Nrdp1 can be important in
  the initiation of apoptosis by catalyzing ubiquitination and degradation of BRUCE"]
- PRKN/Parkin — Nrdp1 ubiquitinates Parkin (poly-Ub chains in vitro and in cells),
  accelerating its proteasomal degradation, reducing Parkin activity and increasing ROS;
  Parkin abrogates Nrdp1-induced oxidative stress. Relevant to Parkinson disease.
  [PMID:18541373 "Nrdp1 ubiquitinated Parkin and catalyzed the poly-ubiquitin chains on
  Parkin in vitro as well as in cells, indicating Parkin is an Nrdp1 substrate";
  "overexpression of Nrdp1 increased the production of reactive oxygen species (ROS), which
  was abrogated by co-expression of Parkin"]
- MYD88, TBK1 — Nrdp1 polyubiquitinates MYD88 (negatively regulating MyD88-dependent
  pro-inflammatory cytokines) and promotes TRIF-dependent type I IFN and TBK1/IRF3
  activation. [UniProt FUNCTION; PMID:19483718 (not cached)]
- EPOR, IL3RA/CSF2RB — ubiquitination of erythropoietin and IL-3 receptors; controls
  hematopoietic progenitor differentiation (By similarity). [UniProt FUNCTION]
- Mitophagy — RNF41-PRKN pathway regulates autophagosome-lysosome fusion during late
  mitophagy (with CLEC16A). [UniProt FUNCTION; PMID:24949970 (not cached)]

## Subcellular location
- Cytosol; perinuclear region; ER tubular network (with Rtn4A). [UniProt GO; PMID:27353365]

## Annotation-call reasoning
- ubiquitin protein ligase activity (GO:0061630) IDA/IEA, ubiquitin-protein transferase
  (GO:0004842) IDA/TAS — ACCEPT core MF; genuine RING E3.
- protein polyubiquitination (GO:0000209) IDA/IEA — ACCEPT core BP.
- protein autoubiquitination (GO:0051865) IDA — ACCEPT (well-supported; self-Ub regulates
  Nrdp1 levels). NOTE: GOA reference for this is PMID:24105792 (S-nitrosoproteome microarray)
  - keep but treat as non-core; the autoubiquitination biology itself is solid (PMID:15314180).
- proteasomal protein catabolic process (GO:0010498) IDA — ACCEPT core BP (drives proteasomal
  degradation of ErbB3, BRUCE, Parkin).
- positive regulation of protein catabolic process (GO:0045732) IMP — KEEP_AS_NON_CORE
  (Rtn4A/ErbB3 context; a regulatory framing).
- receptor tyrosine kinase binding (GO:0030971) IPI — ACCEPT/KEEP: informative MF (ErbB3
  binding), substrate recognition. Keep as non-core supporting the ErbB3 substrate role.
- erythropoietin receptor binding (GO:0005128) / interleukin-3 receptor binding (GO:0005135)
  IEA Ensembl (By similarity) — KEEP_AS_NON_CORE (ortholog-transferred substrate binding).
- ER tubular network (GO:0071782) IBA/IDA, perinuclear region (GO:0048471) IDA, cytosol
  (GO:0005829) TAS — ACCEPT/KEEP localization (cytosol+perinuclear core; ER tubules is the
  Rtn4A-sequestered pool, real but non-core).
- extrinsic apoptotic signaling pathway (GO:0097191) IDA — KEEP_AS_NON_CORE (BRUCE-degradation
  apoptosis role; downstream process).
- 2000379/2000377 ROS metabolic process IMP — KEEP_AS_NON_CORE (Parkin-axis consequence).
- 17145873 MGI annotations (neg reg cell proliferation, neg reg cell migration, reg MAPK
  cascade, reg PI3K/AKT) — KEEP_AS_NON_CORE (downstream of ErbB3 regulation; tumor context).
- small GTPase binding (GO:0031267) IPI PMID:24056301 — the cited paper is about USP33/RALB;
  RNF41 appears as an interactor. UNDECIDED (cannot verify the specific RNF41-small GTPase
  binding from abstract). Per guardrails, do not REMOVE an IPI; mark UNDECIDED / keep cautious.
  Actually the GOA annotation is IPI to RNF41 enabling small GTPase binding from a screen;
  keep as KEEP_AS_NON_CORE bare-binding-like, or UNDECIDED. Use UNDECIDED.
- enzyme binding (GO:0019899) IEA, protein domain specific binding (GO:0019904) IPI,
  identical protein binding (GO:0042802) IPI (dimerization is real), protein binding bare IPI
  — KEEP_AS_NON_CORE.
