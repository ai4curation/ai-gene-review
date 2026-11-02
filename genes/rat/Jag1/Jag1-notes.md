# Jag1 (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Jag1` resolved Q63722 (JAG1_RAT, Swiss-Prot; RGD:2937;
  GeneID 29146). GOA file keyed to Q63722, 87 rows.
- Literature summary in `Jag1-deep-research-manual.md` (no deep-research API
  keys available).

### Key judgements

- Core MF: Notch binding (GO:0005112) and receptor ligand activity
  (GO:0048018). Rat Jagged activates rat Notch1 in co-culture
  [PMID:7697721 "Jagged activates rat Notch1 expressed in myoblasts and prevents muscle
  cell differentiation"].
- Core BP: Notch signaling pathway (GO:0007219), as the signal-sending ligand.
- Core CC: plasma membrane (type I TM protein).
- Bare protein binding rows (LRP1, TSP2; PMID:20472562) removed per policy.
- Developmental ISO rows from mouse Jag1 knockouts and human JAG1 genetics are
  kept as non-core.
- PMID:20145246 (Aph-1 binds full-length Jagged-1 and its CTF) shows Jag1 is a
  gamma-secretase substrate. No GOA row cites it and it supports no process
  annotation for Jag1 itself (the protease performs the cleavage step), so no
  NEW row was added.

### ISO donor audit (QuickGO, 2026-10-28)

Mouse Jag1 (Q9QXX0) and human JAG1 (P78504) annotations behind the ISO rows:

- negative regulation of cell-matrix adhesion, negative regulation of cell-cell
  adhesion, negative regulation of cell migration: the only human experimental
  source is IDA PMID:11549580, which used a secreted Jagged1 extracellular domain
  expressed in NIH3T3 cells, not native transmembrane Jagged1.
- neuronal stem cell population maintenance: the only human experimental source
  is IEP PMID:19682396, an expression-pattern annotation.
- distal tubule development and loop of Henle development: the only mouse
  experimental source is IEP PMID:15821257, an expression-pattern annotation.
- response to muramyl dipeptide: mouse IDA PMID:21156799 (BHF-UCL).
- positive regulation of transcription by RNA polymerase II: mouse IMP
  PMID:19509466 and human IMP PMID:20437614, both reporter readouts of Notch
  signalling in the receiving cell.
- membrane (GO:0016020): the human source is IMP PMID:22465068 with the
  qualifier colocalizes_with, whereas the rat ISO row carries located_in.
- Other developmental donors are mouse IMP knockouts (e.g. PMID:10196361 blood
  vessel remodeling and eye; PMID:19509466 cardiac outflow; PMID:23806616 nephron
  and podocyte; PMID:16495313 inner ear) and are biologically sound.
