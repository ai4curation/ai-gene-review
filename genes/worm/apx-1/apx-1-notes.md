# apx-1 (C. elegans) curation notes

UniProt P41990 (secondary Q9TXN4), "Protein apx-1". PANTHER (verbatim from UniProt): PTHR24049 (CRUMBS
FAMILY MEMBER), PTHR24049:SF22 (DROSOPHILA CRUMBS HOMOLOG). This is the same odd subfamily in which PANTHER
places the LIN-12 receptor. The lag-2 ligand is instead in PTHR22669 (DSL domain protein). IBA: Notch binding
(GO:0005112) from PANTHER:PTN002371879, whose donors are DSL ligands (Dl, Ser, DLL, JAG). That IBA is correct for
APX-1 but wrong for LIN-12.

## Ligand function

- P2 signal to ABp: [PMID:8674418 "We propose that APX-1 is part or all of the P2 signal that induces ABp to
  adopt a fate different than ABa."]
- Delta homolog acting with maternal GLP-1 for ABp fate; dorsal-ventral polarity [PMID:8156602]. The GOA
  "anterior/posterior axis specification, embryo" NAS row is changed with MODIFY to dorsal/ventral axis
  specification, because the abstract explicitly says dorsal-ventral.
- Redundant lateral signal with DSL-1 and LAG-2 in VPC patterning [PMID:14960273].
- vm1-to-vm2 signal for muscle arms [PMID:23539368]; intestinal twist [PMID:10903169]; DTC ligand for
  oocyte growth [PMID:19502484]; can substitute for LAG-2 [PMID:8575327].

## Flags

- Nucleus (EXP, PMID:8674418, plus IEA from the UniProt SubCell mapping): UniProt notes "Nuclear localization of
  transcripts at 36-cell stage". The nuclear signal may be RNA. Abstract-only, so I set these to UNDECIDED.
- NEW: Notch signaling pathway (IMP, PMID:8674418). APX-1 performs the ligand step. Comparator: LAG-2 (IEA)
  and human DLL1 carry GO:0007219.

## Variant notes

- Maternal DSL ligand acting in a 4-cell embryo inductive event, which is a nematode-specific use of the
  pathway. APX-1 lacks a DOS motif (C. elegans DSL ligands; see PMID:18700817).
