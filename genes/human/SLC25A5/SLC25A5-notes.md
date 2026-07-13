# SLC25A5 (ADP/ATP translocase 2, ANT2) — review notes

UniProt: P05141 (ADT2_HUMAN). Gene: SLC25A5 (HGNC:10991), X-linked (Xq24-25).
Synonyms: ANT2, AAC2, ADP/ATP carrier protein 2, "fibroblast isoform". 298 aa.

## Core identity and function

SLC25A5/ANT2 is the ADP/ATP translocase (adenine nucleotide translocator, ANT)
isoform characteristically expressed in proliferative and glycolytic tissues
(fibroblasts, undifferentiated/growth-activated cells, tumors). It is a member of
the SLC25 mitochondrial carrier family (TC 2.A.29) and is an integral polytopic
protein of the mitochondrial inner membrane with the classic 6-transmembrane,
three-repeat (Solcar) carrier fold.

Primary molecular function is an **ATP:ADP antiporter** (GO:0005471): it exchanges
ATP synthesized in the matrix for cytosolic ADP across the inner membrane by an
alternating-access (c-state ⇄ m-state) mechanism with a single substrate-binding
site. This supplies the electron-transport chain / ATP synthase with ADP and
exports ATP to fuel the cell.

- UniProt FUNCTION: "ADP:ATP antiporter that mediates import of ADP into the
  mitochondrial matrix for ATP synthesis, and export of ATP out to fuel the cell"
  [file:human/SLC25A5/SLC25A5-uniprot.txt "mitochondrial matrix for ATP synthesis, and export of ATP out to fuel"].
- CATALYTIC ACTIVITY: "Reaction=ADP(in) + ATP(out) = ADP(out) + ATP(in)" (Rhea:RHEA:34999)
  [file:human/SLC25A5/SLC25A5-uniprot.txt].
- Alternating access: "operates by the alternating access mechanism with a single
  substrate-binding site" [file:human/SLC25A5/SLC25A5-uniprot.txt "operates by the alternating"].
- Family: "Belongs to the mitochondrial carrier (TC 2.A.29) family"
  [file:human/SLC25A5/SLC25A5-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family"].
- Localization: "Mitochondrion inner membrane ... Multi-pass membrane protein"
  [file:human/SLC25A5/SLC25A5-uniprot.txt].

Reactome R-HSA-163215 describes the antiport reaction: "A family of antiport,
ATP-ADP translocases (SLC25A4,5,6), preferentially export ATP from the matrix
while importing ADP from the cytosol" and notes isoform 2 (SLC25A5) is the
fibroblast form [reactome:R-HSA-163215].

Note: this is a **transporter, not an enzyme** — do not assign a catalytic MF.

## Secondary / moonlighting activities (well-supported, non-core)

1. **Proton transport / uncoupling / thermogenesis (By similarity).** ANT can act
   as a fatty-acid-activated proton transporter that uncouples oxidative
   phosphorylation, contributing to thermogenesis in tissues lacking UCP1; this is
   antagonized by its ADP:ATP antiport activity, so ANT2 acts as a "master
   regulator" balancing ATP output vs thermogenesis
   [file:human/SLC25A5/SLC25A5-uniprot.txt "proton transporter: proton transport uncouples the proton flows via the"].
   All proton-transport / uncoupler / adaptive-thermogenesis annotations are ISS/IEA
   transferred from paralogs (P51881 = mouse Ant1/Slc25a4 or bovine) — plausible but
   not directly demonstrated for human ANT2; treat as KEEP_AS_NON_CORE.

2. **Mitochondrial permeability transition pore (mPTP) / apoptosis.** ANT is a
   regulator (possibly component) of the mPTP. Human-specific ARHGAP11B imported
   into mitochondria "interacts with the adenine nucleotide translocase (ANT) and
   inhibits the mitochondrial permeability transition pore (mPTP)"
   [PMID:31883789 "nucleotide translocase (ANT) and inhibits the mitochondrial permeability"];
   this mPTP inhibition promotes basal-progenitor expansion/proliferation.
   UniProt: "Also plays a key role in mPTP opening ... which contributes to cell
   death (PubMed:31883789). It is however unclear if SLC25A5/ANT2 constitutes a
   pore-forming component of mPTP or regulates it"
   [file:human/SLC25A5/SLC25A5-uniprot.txt "do not express UCP1 (By similarity). Also plays a key role in mPTP"].
   Treat mPTP-complex / regulation-of-permeability / apoptosis annotations as
   KEEP_AS_NON_CORE.

3. **Mitophagy (By similarity).** "Acts as a regulator of mitophagy independently of
   ADP:ATP antiporter activity: promotes mitophagy via interaction with TIMM44 ...
   promoting stabilization of PINK1"
   [file:human/SLC25A5/SLC25A5-uniprot.txt "ADP:ATP antiporter activity: promotes mitophagy via interaction with"].
   ISS/IEA from paralog; non-core.

4. **MMXD complex / chromosome segregation.** ANT2 is a component of the mitotic
   spindle-associated MMXD (MMS19-MIP18-XPD) cytosolic iron-sulfur assembly complex.
   Ito et al.: "it included FAM96B (now designated MIP18), Ciao1, and ANT2"
   [PMID:20797633 "it included FAM96B (now designated MIP18), Ciao1, and ANT2"]; the
   complex "led to improper chromosome segregation" on knockdown
   [PMID:20797633 "led to improper chromosome segregation"]. This is a genuine IDA
   finding (part_of MMXD complex, GO:0071817) — a legitimate moonlighting role,
   non-core relative to the antiporter function.

## Interactions (IPI "protein binding" annotations)

Most GO:0005515 "protein binding" annotations come from IntAct/proteomics
co-precipitation screens and are individually uninformative:
- SIRT4 (Q9Y6E7), PMID:17715127 (mitochondrial ADP-ribosyltransferase screen).
- SLC35F6 / C2orf18 / ANT2BP (Q8N357), PMID:19154410 — ANT2-binding protein in PDAC;
  "it could interact with adenine nucleotide translocase 2 (ANT2)"
  [PMID:19154410 "it could interact with adenine nucleotide translocase 2 (ANT2)"].
- LRRK2 (Q5S007), PMIDs 21370995, 24725412, 35266954 — LRRK2 interactome screens.
- ADCK2 (Q7Z695), PMID:27499296 (mitochondrial interaction map).
- ARHGAP11B (Q3KRB8), PMID:31883789 — functional, mPTP-inhibiting interaction (see above).
- AK4 (P27144) / adenylate kinase, PMID:19130895 — "ANTs) interacted with AK4"
  [PMID:19130895 "interacted with AK4 and higher amount of ANT was"]; the paper also
  co-precipitates prohibitin (P21796). Physiologically plausible (AK4 in matrix,
  ANT in inner membrane, both in adenine-nucleotide handling).
- PHB2 (Q99623), PMID:19116139 — capsaicin/prohibitin-2 study; ANT2 pulled down.
- Parkin/PRKN (O60260), PMID:19725078 — "ubiquitin protein ligase binding"
  (GO:0031625); SLC25A5 co-purified as a Parkin interactant. "potential interactants
  of Parkin; ... SLC25A5" [PMID:19725078 "SLC25A5, TPI1, UCHL1, UQCRC1, VCL, YWHAZ, YWHAE"].

Per policy, bare "protein binding" IPI is not removed; mark as
MARK_AS_OVER_ANNOTATED (uninformative MF) or, for informative specific ones
(ubiquitin ligase binding), ACCEPT/KEEP_AS_NON_CORE.

## Localization annotations

- Mitochondrial inner membrane (GO:0005743): correct core location (IBA, ISS, TAS,
  UniProt SubCell). ACCEPT.
- Mitochondrion (GO:0005739): correct parent (IDA/HTP/HDA/IEA). ACCEPT / non-core parent.
- Membrane (GO:0016020): high-level parent; IDA PMID:27641616 found ANT in
  non-mitochondrial (erythrocyte plasma) membranes; UniProt: "May localize to
  non-mitochondrial membranes" and "Expressed in erythrocytes (at protein level)"
  [file:human/SLC25A5/SLC25A5-uniprot.txt "Expressed in erythrocytes (at protein level)"].
  Keep as uninformative parent / non-core.
- Plasma membrane (GO:0005886), TAS PMID:2168878: that paper is only a genomic
  cloning/sequence of the fibroblast ANT gene (no localization assay) — the TAS is
  weak; ANT's residence is the inner membrane, though ANT2 can appear in the RBC
  plasma membrane (PMID:27641616). Keep as non-core / over-annotated.
- Nucleus (GO:0005634) HDA PMID:21630459 (sperm-nucleus proteome) and mitochondrial
  nucleoid (GO:0042645) IDA PMID:18063578 — mass-spec co-purifications, likely
  contaminant/association; over-annotated relative to inner-membrane function.

## Suspect / over-annotated MF calls

- GO:0000295 adenine nucleotide transmembrane transporter activity (IMP PMID:19116139):
  the cited paper is the capsaicin/prohibitin-2 study; it does NOT measure ANT2
  nucleotide-transport activity, so this IMP is mis-supported. Prefer the specific
  antiporter term GO:0005471 → MODIFY.
- GO:0051503 adenine nucleotide transport (IMP PMID:19116139): same weak support;
  the true BP is ADP/ATP transmembrane transport. MODIFY/over-annotated.
- GO:0015207 adenine transmembrane transporter activity (TAS PMID:2168878) and
  GO:0015853 adenine transport (IEA inferred from GO:0015207): ANT transports the
  adenine *nucleotides* ADP/ATP, not free adenine (the base). These are incorrect
  (wrong substrate) → MODIFY to ATP:ADP antiporter / mitochondrial ADP-ATP transport.
- GO:0003723 RNA binding (HDA PMID:22658674): high-throughput mRNA-interactome
  capture; abundant mitochondrial carriers are frequent background hits. Over-annotated.
- GO:0017077 oxidative phosphorylation uncoupler activity & GO:0015078 proton
  transmembrane transporter activity (ISS/IEA from P51881): the uncoupling proton
  transport is a real (paralog-supported) secondary activity, By similarity only.
  KEEP_AS_NON_CORE.

## Process annotations

- Mitochondrial ADP transmembrane transport (GO:0140021) and mitochondrial ATP
  transmembrane transport (GO:1990544): correct core BPs (ISS/IBA/IEA). ACCEPT.
- transmembrane transport (GO:0055085): correct high-level parent.
- proton transmembrane transport (GO:1902600): secondary (uncoupling), non-core.
- adaptive thermogenesis (GO:1990845), regulation of mitochondrial membrane
  permeability (GO:0046902), positive regulation of mitophagy (GO:1901526),
  B cell differentiation (GO:0030183), erythrocyte differentiation (GO:0030218):
  all ISS/IEA transferred from paralog P51881/mouse; plausible pleiotropy but not
  human-ANT2-specific. KEEP_AS_NON_CORE.
- positive regulation of cell population proliferation (GO:0008284) IMP PMID:19154410:
  ANT2BP/C2orf18 knockdown suppresses PDAC growth; ANT2 is the historical
  proliferation-associated ("growth-regulated") ANT isoform. Reasonable IMP but a
  downstream/context role — KEEP_AS_NON_CORE. UniProt/Reactome note ANT2 is the
  fibroblast/growth-regulated isoform.
- negative regulation of mitochondrial outer membrane permeabilization involved in
  apoptotic signaling pathway (GO:1901029) IMP PMID:19154410: apoptosis regulation
  via mitochondrial membrane potential; consistent with mPTP role. KEEP_AS_NON_CORE.

## Summary of core functions

1. ATP:ADP antiporter activity (GO:0005471) in the mitochondrial inner membrane
   (GO:0005743), driving mitochondrial ADP/ATP transmembrane transport (GO:0140021,
   GO:1990544) in support of oxidative phosphorylation.

Everything else (proton/uncoupling, mPTP/apoptosis, mitophagy, MMXD/chromosome
segregation, proliferation, differentiation programs, individual interactions) is
secondary or context-specific and reviewed as non-core.
