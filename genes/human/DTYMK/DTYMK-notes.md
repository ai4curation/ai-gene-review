# DTYMK (thymidylate kinase / dTMP kinase) — review notes

UniProtKB:P23919 (KTHY_HUMAN), HGNC:3061, gene symbol DTYMK (synonyms CDC8, TMPK, TYMK).
EC 2.7.4.9. 212 aa, cytosolic. Belongs to the thymidylate kinase family (P-loop NTPase fold).

## Core function

DTYMK is thymidylate kinase (dTMP kinase). It catalyses the ATP-dependent, Mg2+-dependent
phosphorylation of dTMP to dTDP:

- Reaction: dTMP + ATP = dTDP + ADP (RHEA:13517; EC 2.7.4.9)
  [file:human/DTYMK/DTYMK-uniprot.txt "Reaction=dTMP + ATP = dTDP + ADP"]
- UniProt FUNCTION: "Catalyzes the phosphorylation of thymidine monophosphate (dTMP) to
  thymidine diphosphate (dTDP), the immediate precursor for the DNA building block dTTP,
  with ATP as the preferred phosphoryl donor in the presence of Mg(2+)."
  [file:human/DTYMK/DTYMK-uniprot.txt]

This is the **penultimate, common step** of dTTP synthesis. dTMP is produced by BOTH the
de novo route (dUMP -> dTMP by thymidylate synthase) and the salvage route (thymidine ->
dTMP by thymidine kinase); both converge on dTMPK, which is therefore the bottleneck for
dTTP biosynthesis. dTDP is then phosphorylated to dTTP by nucleoside diphosphate kinase.
[PMID:34918187 "The thymidine de novo and salvage pathways converge at the point of the
phosphorylation of dTMP to dTDP by dTMPK"; "This makes dTMPK the bottleneck for dTTP
biosynthesis"]

Homodimer (Lee & Cheng 1977, PMID:18469; cited in UniProt SUBUNIT "Homodimer.").
Cofactor Mg2+. KM for dTMP ~5 uM (PMID:12614151).

## Essentiality / disease

- Enzyme activity and mRNA peak in S phase; cell-cycle regulated (PMID:8024690, PMID:8845311).
- Biallelic loss-of-function variants (p.Pro81Leu, p.Asp128Asn) cause CONPM
  (childhood-onset neurodegeneration with progressive microcephaly, MIM:619847), with
  minimal dTMPK activity in patient fibroblasts and impaired DNA replication; zebrafish
  dtymk mutants recapitulate microcephaly/neuronal death/early lethality with increased
  ribonucleotide misincorporation.
  [PMID:34918187 "In cells of affected individuals, dTMPK enzyme activity was minimal";
  abstract "loss-of-function of DTYMK as the cause of a severe postnatal neurodegenerative
  disease"]
- Also reported as a gene for mitochondrial DNA depletion syndrome (PMID:31271740).
- Essential across CRISPR screens (BioGRID-ORCS: 809 hits in 1168 screens).

## Localization

- Cytosolic: Reactome models describe "Cytosolic deoxythymidylate kinase (DTYMK)"
  (R-HSA-73635, R-HSA-75126). GOA has TAS cytosol (GO:0005829).
- IBA (GO_REF:0000033) also propagates cytoplasm, nucleus, and mitochondrion; the
  nucleus/mitochondrion CC calls are weakly supported for the human enzyme, which is a
  small soluble cytosolic kinase with no targeting sequence. The mitochondrion HTP call
  (PMID:34800366, MitoCoP proteomics) likely reflects co-purification / dual reporting; the
  established, functionally relevant compartment is the cytosol/cytoplasm.

## Structure

Extensively crystallised (PDB 1E2D–1NN5, 2XX3) in complex with dTMP/analogues and ATP/ADP
analogues; P-loop (res 13-21 / binding 16-21), DR(Y/H) motif (96-98), LID domain (133-157).
Drug-activation relevance: phosphorylates AZT-MP (zidovudine monophosphate), so it is on
the activation pathway for thymidine-analogue prodrugs (PMID:12614151).

## Curation decisions (summary)

Core: MF GO:0004798 dTMP kinase activity; directly involved in GO:0006233 dTDP biosynthetic
process and GO:0006235 dTTP biosynthetic process; located in cytosol GO:0005829.

- dTMP kinase activity (GO:0004798) — ACCEPT (all evidence lines: EXP, IDA, IBA, IEA, TAS).
- ATP binding (GO:0005524) — ACCEPT (structurally confirmed, PMID:12614151).
- dTDP biosynthetic process (GO:0006233) — ACCEPT.
- dTTP biosynthetic process (GO:0006235) — ACCEPT.
- cytosol (GO:0005829) / cytoplasm (GO:0005737) — ACCEPT.
- dUDP biosynthetic process (GO:0006227) — KEEP_AS_NON_CORE (secondary/promiscuous activity
  toward dUMP; Reactome notes dUMP as an alternative substrate, but the biological role is
  dTTP synthesis, not dUDP production).
- thymidine biosynthetic process (GO:0046105) — MARK_AS_OVER_ANNOTATED (label mismatch:
  DTYMK acts on the nucleotide dTMP, not on the nucleoside thymidine; the process it serves
  is dTTP/dTDP biosynthesis, not thymidine biosynthesis).
- nucleus (GO:0005634) — MARK_AS_OVER_ANNOTATED (IBA over-propagation; weak support for the
  human enzyme).
- mitochondrion (GO:0005739) IBA and HTP — MARK_AS_OVER_ANNOTATED (IBA over-propagation +
  HTP proteomics co-purification; the functional compartment is cytosol).
