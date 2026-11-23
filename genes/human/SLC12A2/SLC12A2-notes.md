# SLC12A2 (NKCC1) curation notes

UniProt P55011; HGNC:10911; HGNC symbol SLC12A2. Basolateral Na-K-2Cl
cotransporter 1 (NKCC1), SLC12 cation-chloride cotransporter (CCC) family.

## Core biology
- Electroneutral secondary-active cotransporter: imports 1 Na+ : 1 K+ : 2 Cl-
  into the cell, driven by the inwardly directed Na+ gradient set by the
  Na/K-ATPase [UniProt CATALYTIC ACTIVITY Rhea:RHEA:72395; PMID:7629105].
  KM: 19.6 mM Na+, 2.68 mM K+, 26.5 mM Cl- [UniProt BIOPHYSICOCHEMICAL PROPERTIES].
- Homodimer with domain-swap at the scissor helices connecting TMD and C-terminal
  domain; 12 TM helices; cytoplasmic N- and C-termini [UniProt SUBUNIT; PMID:33597714,
  PMID:32081947, PMID:36239040].
- Inhibited by loop diuretics bumetanide and furosemide [UniProt; PMID:35585053,
  PMID:36306358].
- Activated by phosphorylation at Thr-203/207/212 by SPAK (STK39) and OSR1 (OXSR1)
  downstream of WNK kinases (WNK1-4); RFXV motifs mediate SPAK/OSR1 docking
  [UniProt PTM/DOMAIN; PMID:16669787].

## Physiology
- Sets intracellular Cl- concentration; in immature neurons high [Cl]i makes GABA_A
  depolarizing; NKCC1 facilitates neonatal seizures (bumetanide-sensitive)
  [PMID:16227993].
- Regulatory volume increase / cell volume homeostasis.
- Transepithelial salt and fluid secretion (basolateral Cl- entry step); native
  human colon epithelium, Ca2+/cAMP-regulated membrane recycling [PMID:17478539,
  PMID:12946942].
- Inner-ear endolymph K+ secretion; loss causes deafness (DFNA78) and Kilquist /
  Delpire-McNeill syndromes [UniProt DISEASE; PMID:32294086, PMID:32658972,
  PMID:30740830, PMID:32754646].
- NH4+ can substitute for K+ on the carrier -> contributes to (trans)epithelial
  ammonium transport; this is carrier substitution, NOT a channel [PMID:12946942,
  PMID:18032481]. GO:0008519 ammonium channel activity is mechanistically wrong
  (NKCC1 is not a channel).
- WNK1-OSR1/SPAK-SLC12A2 pathway drives T-cell migration/chemotaxis [PMID:27400149].
- Interacts with Hsp90 (P07900) at C-terminus during biogenesis [PMID:15347682].
- Interacts with ezrin (EZR, P15311) linking to cytoskeleton / focal adhesions in
  glioma dispersal [PMID:22570591, PMID:24555568].

## Curation decisions of note
- Core MF: GO:0008511 sodium:potassium:chloride symporter activity (verified; UniProt
  DR GO line IDA:UniProtKB). GO:0015377 (chloride:cation symporter), GO:0046873 (metal
  ion transporter), GO:0022857 (transmembrane transporter) are TOO_GENERAL vs this.
- GO:0016020 membrane -> MODIFY -> GO:0005886 plasma membrane (basolateral PM is the
  core location, GO:0016323).
- GO:0005515 bare protein binding (OXSR1, EZR x2) -> REMOVE (uninformative); the OXSR1
  interaction is captured by GO:0120283 protein serine/threonine kinase binding.
- GO:0019901 protein kinase binding -> MODIFY -> GO:0120283 (SPAK/OSR1 are Ser/Thr
  kinases; gene already carries GO:0120283).
- GO:0008519 ammonium channel activity (IDA x2) -> MARK_AS_OVER_ANNOTATED (carrier
  substitution, not a channel).
