# Delta (Q8T4N9, Strongylocentrotus purpuratus) — curation notes

## Identity

- UniProt Q8T4N9 (unreviewed, TrEMBL) is the *S. purpuratus* Delta cDNA
  (EMBL AAL71862, gene name `Delta`, "Delta-like protein"), a 674-aa **fragment**.
  The record's only literature reference is Sweet, Gehring & Ettensohn 2002
  (PMID:11934860), which is written about the *Lytechinus variegatus* orthologue
  LvDelta; the companion LvDelta accession is AAL71861 (cited as the probe source
  in Croce & McClay 2010, PMID:20023163), so AAL71861/AAL71862 are the Lv/Sp pair
  deposited by the Ettensohn lab. The *S. purpuratus* gene is the `SpDelta` of
  Revilla-i-Domingo et al. 2004 (PMID:15385170) and the `delta` node of the
  Davidson endomesoderm GRN. No identity doubt.
- Domain architecture (UniProt features): Notch-ligand N-terminal MNNL domain
  (Pfam PF07657), DSL domain (Pfam PF01414; InterPro IPR001774, residues 182-226),
  eight EGF-like repeats (291-552, several calcium-binding-type), a single
  transmembrane helix at 594-616 and a short C-terminal cytoplasmic tail — the
  canonical single-pass type I Delta ligand topology. The UniProt CAUTION line
  notes that one EGF domain lacks residues required for ProRule feature
  propagation (PRU00076); this concerns feature annotation only.
- PANTHER placement is PTHR24033 / PTHR24033:SF232 (a laminin-gamma-2-related
  subfamily), which reflects EGF-repeat similarity of a fragment rather than the
  Delta subfamily; not asserted anywhere in the review (CLAUDE.md rule).

## What the gene does (GRN placement)

Delta is a **signaling ligand, not a transcription factor**: a cell-surface
Notch ligand that acts strictly on contiguous neighbours.
[PMID:22306924 "In contrast to many other signaling ligands it is bound to the
cell surface of the delta expressing cell and not secreted."]

### Inputs: the double-negative gate

- *delta* is one of the direct targets of the pmar1–hesC double-negative gate.
  It is activated by ubiquitous factors and repressed everywhere by HesC; Pmar1
  represses *hesC* only in the micromeres, so *delta* transcription is confined
  to the skeletogenic micromere lineage.
  [PMID:17636127 "every cell of the embryo expressed either hesC (purple) or δ
  (orange), but no cell expressed both genes"; "in hesC MASO embryos, it is
  detected throughout the whole embryo"]
  [PMID:12027443 "In both cases, the effects are derepression: of the delta
  gene; and of skeletogenic genes"]
- Timing: [PMID:19104065 "Expression of the delta gene begins between 8 h and
  8 h 40 min postfertilization (i.e., late fifth cleavage)."]
  [PMID:22306924 "The Strongylocentrotus purpuratus delta gene is first
  expressed between 8 and 9 hpf in the cells of the skeletogenic micromere
  lineage that lie at the center of the vegetal plate"]
- cis-regulation. Two CRMs: R11, ~13-16 kb downstream of the last exon, drives
  micromere-lineage expression and responds to the pmar1 repression system
  [PMID:15385170 "this cis-regulatory element is able to drive the expression of
  a reporter gene in the same cells and at the same time that the endogenous
  delta gene is expressed, and that temporally, spatially, and quantitatively it
  responds to the pmar1 repression system"], with Ets1 sites required for
  activity [PMID:19104065 "Three putative Ets1 binding sites were identified in
  the R11 CRM within a 75 bp stretch of sequence; when these Ets1 target sites
  were disrupted, sharply decreased reporter activity was observed"]. A proximal
  CRM (−90 to +484, in the 5'UTR) reproduces the entire pregastrular pattern
  (SM, NSM, apical plate), is activated by Runx and directly repressed by HesC
  through a class-C E-box.
  [PMID:19104065 "transcription of the gene encoding the Notch ligand Delta is
  activated by the widely expressed Runx transcription factor, but spatially
  restricted by HesC-mediated repression through a site in the delta 5′UTR"]
- Second phase: when skeletogenic cells ingress, *delta* turns off in them and
  is activated in the NSM (Blimp1 has by then repressed *hesC* there), so that
  Notch signaling moves outward to the veg2 endoderm ring.
  [PMID:19104065 "When the SM cells ingress into the blastocoel at late
  (mesenchyme) blastula stage, the delta gene is turned off in these cells, but
  at this time it is activated in the NSM."] The NSM phase itself depends on the
  earlier skeletogenic Delta signal [PMID:22306924 "the NSM phase of delta
  transcription is dependent on D/N signaling from the skeletogenic mesoderm"].

### Outputs: Notch-mediated induction of non-skeletogenic mesoderm

- Micromere-descendant Delta is the signal that makes the adjacent veg2 ring
  mesodermal. [PMID:18413610 "from seventh cleavage, the Notch ligand Delta.
  Reception of this signal causes the ring of cells then immediately adjacent to
  the micromere lineage to assume mesodermal fate"]
  [PMID:12027443 "they express Delta, a Notch ligand which triggers the
  conditional specification of the central mesodermal domain of the vegetal
  plate"]
  [PMID:19104065 "The early SM Delta signal is critical for specification of the
  adjacent ring of cells as NSM beginning at the early blastula stage."]
- Loss of function in *S. purpuratus* (Materna & Davidson 2012, full text):
  Delta MASO, Notch MASO, dominant-negative Su(H) and DAPT gave the same result
  on a 205-gene regulome panel. [PMID:22306924 "These were injection of
  morpholino-substituted antisense oligonucleotides (MASO) to block translation
  of the Delta ligand; injection of MASO targeting the Notch receptor; expression
  of a dominant negative form of the Suppressor of Hairless (Su(H))"] Direct
  pregastrular targets are few and mesodermal: [PMID:22306924 "In our data set,
  gcm, gataE, foxA, and foxY are significantly affected in their expression level
  in repeat experiments"]; [PMID:22306924 "The expression of the Delta signaling
  ligand is required for pregastrular specification of all mesoderm derivatives
  in the adjacent NSM."]; the NSM phase feeds *foxY* in the small micromeres
  [PMID:22306924 "Disruption of the second phase of Delta expression specifically
  abolishes specification of late mesodermal derivatives such as the coelomic
  pouches to which the small micromeres contribute."]
- Direct transcriptional target in the receiving cell: *gcm*, via Su(H) sites.
  [PMID:16925988 "confirming that spgcm is a direct target of canonical N
  signaling mediated through Su(H) inputs"]
- Blocking the ligand or the pathway abolishes pigment cells.
  [PMID:18413610 "blockade of the micromere lineage expression of delta or of
  the reception and transduction of this signal by the Notch pathway in the
  adjacent cells severely affects their mesodermal specification and abolishes
  pigment cell differentiation"]
- Orthologue evidence in *Lytechinus variegatus* (necessity AND sufficiency):
  [PMID:11934860 "expression of LvDelta by micromere descendants is both
  necessary and sufficient for the development of two mesodermal cell types,
  pigment cells and blastocoelar cells"]; [PMID:11934860 "Macromere-derived
  LvDelta is necessary for blastocoelar cell and muscle cell development."];
  [PMID:20023163 "Initially, Delta is expressed exclusively in the micromeres,
  where it is necessary for the most vegetal endomesoderm cell descendants to
  express Gcm and become mesoderm."] Croce & McClay also show a continuous Delta
  input of >2 cleavages (~2.5 h) is needed before *gcm* becomes Delta-independent.
  The receptor side was established by Sherwood & McClay 1999 in Lv
  [PMID:10079232 "these results offer compelling evidence that LvNotch signaling
  directly specifies the SMC fate"].

### Second, non-core role: lateral inhibition in the neurogenic ectoderm

- Delta/Notch signaling also restricts neural progenitor number in the
  gastrula-stage ectoderm and ciliary band (Mellott, Thompson & Burke 2017,
  abstract only). [PMID:28851710 "Inhibition of γ-secretase, injection of
  Sp-Delta morpholinos or CRISPR/Cas9-induced mutation of Sp-Delta results in
  supernumerary neural progenitors and neurons."]; [PMID:28851710 "Thus, Notch
  signaling restricts the number of neural progenitors recruited and regulates
  the fate of progeny of the asymmetric division."] This is a classical
  lateral-inhibition role and is the only sea urchin evidence bearing on the
  ARBA "neuron development" transfer; it argues for a negative-regulation-of-
  neurogenesis term rather than the vague parent, and it is not the core
  (endomesoderm GRN) function of the gene.

## Curation decisions (summary)

- Electronic rows: Notch signaling pathway (InterPro) — ACCEPT, with IMP support
  from PMID:22306924 (Sp) and PMID:11934860 (Lv). Plasma membrane / membrane —
  ACCEPT (type I TM ligand; surface presentation is how it signals). Calcium ion
  binding — KEEP_AS_NON_CORE (structural cbEGF repeats). Cell communication —
  MODIFY to the Notch pathway term (too general). Extracellular region and
  cytoplasm (ARBA subcellular mapping from vertebrate family members) — REMOVE:
  a membrane-tethered, contact-dependent ligand is neither secreted nor
  cytoplasmic. ARBA gliogenesis and cell morphogenesis are vertebrate Dll1-derived
  transfers with no sea urchin evidence: REMOVE. ARBA neuron development —
  MODIFY to GO:0050768 negative regulation of neurogenesis on the strength of
  PMID:28851710 (non-core).
- NEW: GO:0048018 receptor ligand activity (IMP; Delta MASO, Notch MASO,
  dominant-negative Su(H) and DAPT give the same regulome phenotype, i.e. the
  ligand acts through the Notch receptor; this is the MF used for Drosophila Dl
  in the production GO-CAM 60ad85f700000309, gocams/index.tsv);
  GO:0007501 mesodermal cell fate specification (IMP); GO:0050768 negative
  regulation of neurogenesis (IMP, non-core).
- Comparator check (QuickGO, 2026-09): mouse Dll1 (Q61483) carries GO:0005112
  Notch binding (IPI), GO:0007219 (IMP), GO:0007267 cell-cell signaling (IDA),
  GO:0045747 (IDA/IMP), GO:0050767 regulation of neurogenesis and GO:0045665
  negative regulation of neuron differentiation (IMP), and tissue-specific fate
  terms by IMP; the Drosophila FGF ligands pyr and ths carry GO:0007501 by IMP.
  Lineage-fate terms on an inductive ligand are therefore within GO convention.
  GO:0045168 "cell-cell signaling involved in cell fate commitment" was
  considered and dropped: only two experimental annotations exist (both plant
  peptides), so it is not the conventional term.
- Participation test: the ligand is the inductive signal itself, i.e. it
  performs the intercellular step of the specification (Delta on the micromere
  surface activates Notch on the veg2 cell, whose Su(H) then activates gcm),
  not merely a prerequisite.
- Not proposed: GO:0005112 Notch binding (no direct binding assay for the sea
  urchin protein; raised as a question), endoderm specification (Materna &
  Davidson found no endoderm regulatory gene activated by Delta before
  gastrulation), pigment cell differentiation (downstream of gcm), positive
  regulation of Notch signaling (the ligand is a pathway component, not a
  regulator of it).
