# SMIM13 review notes

## Identity

SMIM13 (previous symbol C6orf228; UniProt P0DJ93, SIM13_HUMAN) is a 91-residue (10.4 kDa)
protein. UniProt: one predicted helical TM segment at residues 10-30 (ECO:0000255); residues
47-91 predicted disordered (MobiDB-lite), with a basic stretch (71-80) and a basic/acidic
stretch (81-91). Four phosphosites (S58, S60, T62, S69) annotated by similarity to mouse
E9Q942 (ECO:0000250). Pfam PF15938 (DUF4750), PANTHER PTHR36877 (SMIM13 family). UniProt
subcellular location "Membrane; Single-pass membrane protein" is curator inference
(ECO:0000305). PE level 1.

## Literature search (2026-10-03)

PubMed `SMIM13[tiab] OR C6orf228[tiab]`: 2 hits, an osteoarthritis biomarker study and a
cattle selection-signature scan, both mentioning the gene only in a list. No study of SMIM13
protein function exists.

## Localisation and expression

- Human Protein Atlas (ENSG00000224531, JSON inspected 2026-10-03): immunofluorescence
  reliability "Approved"; main location nucleoplasm, additional nuclear membrane and Golgi
  apparatus. A nucleoplasmic signal is hard to reconcile with an integral membrane protein
  and could reflect antibody cross-reactivity; nuclear membrane / Golgi are plausible for a
  single-pass protein. One antibody, not orthogonally validated - not used for annotation.
- HPA RNA: tissue enhanced in brain; single-cell enhanced in basal keratinocytes and
  syncytiotrophoblasts.

## Decisions

- membrane (IEA): ACCEPT (only annotation; correct, uninformative).
- No MF/BP/NEW. The HPA nuclear-envelope/Golgi signal is noted as a question, not proposed
  as NEW (single antibody, conflicting main location).
