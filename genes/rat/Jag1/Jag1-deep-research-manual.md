# Jag1 (rat, Q63722) - manual literature research

No deep-research provider was available for this session, so this summary was
assembled by hand from the cached publications in `publications/`, the UniProt
records for rat Jag1 (Q63722) and human JAG1 (P78504), and QuickGO queries
(2026-10-28) for the mouse (Q9QXX0) and human (P78504) donor annotations
behind the ISO rows.

## Identity and domain architecture

- Rat Jagged-1 is a 1219-residue single-pass type I membrane protein (signal
  peptide 1..33, extracellular 34..1067, TM 1068..1093, cytoplasmic 1094..1219)
  [UniProtKB:Q63722 "Single-pass type I membrane protein"].
- Extracellular region: MNNL (Notch ligand N-terminal) domain, DSL domain
  (185..229), 16 EGF-like repeats (the second atypical, many calcium-binding)
  and a VWC/cysteine-rich region [UniProtKB:Q63722 FT DOMAIN lines;
  InterPro IPR001774 DSL, IPR011651 Notch_ligand_N, IPR026219 Jagged/Serrate].
- The region 199..207 of the DSL domain is annotated as important for NOTCH1
  interaction (by similarity) [UniProtKB:Q63722 "Important for interaction with NOTCH1"].

## Molecular function: Notch ligand

- Rat Jagged was the first mammalian Notch ligand cloned; cells expressing it
  activate rat Notch1 in co-culture and block myoblast differentiation
  [PMID:7697721 "the biological activity of Jagged was tested using a cell culture assay
  in which Jagged activates rat Notch1 expressed in myoblasts and prevents muscle
  cell differentiation"].
- Jagged1 binds the NOTCH1 extracellular domain; Fringe glycosylation of NOTCH1
  EGF6 and EGF36 inhibits activation from Jagged1
  [PMID:28089369 "modifications at EGF6 and EGF36 (added by Manic and Lunatic but not Radical) inhibited Notch1
  activation from Jagged1"].
- Rat Jag1-expressing cells are a standard ligand source for NOTCH1 signalling
  assays [PMID:18593716 "We identify two specific mutations that reduce ligand (JAGGED1)
  induced NOTCH1 signaling."].
- Extracellular partners: TSP2 binds both Jagged1 and Notch3 ectodomains, and
  Jagged1 binds the LRP1 85-kDa B-chain [PMID:20472562 "Both Notch3 and Jagged1 bind directly to the 85-kDa B-chain of LRP1."].

## Processing: gamma-secretase substrate

- Full-length rat Jagged-1 and its membrane-anchored C-terminal fragment
  associate with the gamma-secretase subunit Aph-1, both on overexpression and
  endogenously in E13 rat embryo microsomes
  [PMID:20145246 "another endogenous canonical
  gamma-substrate, Jagged, showed association of both its full-length and
  C-terminal fragment forms with Aph-1"]
  [PMID:20145246 "Microsomes were prepared from E13 rat embryos, which were previously shown by us and others to have robust expression of Jagged-1"].
- Jagged is shed by an alpha-secretase-like cleavage and the CTF is then cut by
  gamma-secretase [PMID:20145246 "Jagged is a ligand of the Notch receptor that was previously shown by us and others to be cleaved in an α-secretase-like fashion to generate a C-terminal, membrane-anchored fragment that is then processed by γ-secretase"].
- Jag1 is the substrate here; this supports no process annotation for Jag1
  itself (the protease performs the step).

## Rat tissue studies

- Liver regeneration: Jagged-1 is upregulated in hepatocytes after 2/3 partial
  hepatectomy; recombinant Jagged-1 stimulates hepatocyte DNA synthesis, and
  in vivo siRNA against Jagged-1 suppresses hepatocyte proliferation
  [PMID:15057910 "Addition of recombinant Jagged-1 protein to primary
  cultures of hepatocytes stimulated hepatocyte DNA synthesis"]
  [PMID:15057910 "injection of silencing RNA for Notch and Jagged-1 to livers 2 days before
  partial hepatectomy significantly suppressed proliferation of hepatocytes at
  days 2 to 4 of the regenerative response"].
- Cochlea: Jag1 is expressed in supporting-cell precursors; antisense
  knock-down of Jag1 in cultured sensory epithelium increases hair cell number
  [PMID:10887092 "A decrease of
  either Notch1 or Jag1 expression by antisense oligonucleotides in cultures of
  the developing sensory epithelium resulted in an increase in the number of hair
  cells."].
- Injured carotid artery: Jagged1 is induced at the regenerating endothelial
  wound edge; a secreted Jagged1 extracellular domain (an antagonist form) alters
  adhesion and migration of NIH3T3 cells
  [PMID:11549580 "High Jagged1 expression was restricted to
  the regenerating endothelial wound edge"]
  [PMID:11549580 "the soluble Jagged1 protein caused decreased cell-matrix adhesion
  and cell migration defects"].
- Cardiac EMT: NOTCH1 LVOT variants show impaired ligand-induced EMT and Snail/Hes
  induction in endothelial cells [PMID:20951801 "these LVOT-associated NOTCH1 alleles can contribute to defective EMT
  in endothelial cell lines through impaired induction of Snail and Hes family
  members"].

## Human genetics (context)

- Human JAG1 haploinsufficiency causes Alagille syndrome, affecting liver, heart,
  skeleton, eye, face and kidney [PMID:9207788 "Alagille syndrome is an autosomal dominant disorder
  characterized by abnormal development of liver, heart, skeleton, eye, face and, less frequently, kidney."].

## Human and mouse donor evidence not cached here

- The human JAG1 cytoplasmic tail is bound and ubiquitinated by the E3 ligase MIB1; human donor annotations to ubiquitin protein ligase binding are EXP/IMP/IPI from PMID:25747658 (QuickGO, 2026-10-28; paper not cached in this repository).
- The human JAG1 intracellular region binds phospholipids (IMP PMID:22465068, CAFA; QuickGO 2026-10-28; paper not cached).
