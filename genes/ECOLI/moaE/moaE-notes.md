# moaE (P30749) notes, E. coli K-12

Deep research providers were unavailable for this gene (no API keys in this session), so no
`-deep-research-<provider>.md` file was generated. This review is built from the UniProt record
and the cached publications in `publications/`, most of which are abstract-only.

## Identity

- UniProt P30749, molybdopterin synthase catalytic subunit, EC 2.8.1.12; synonym chlA5; b0785.
  Last gene of moaABCDE. MoaE family (Pfam PF02391, PANTHER PTHR23404).

## Function

- MoaD2-MoaE2 heterotetramer with a central MoaE dimer
  [PMID:15709772 "consists of two MoaE subunits and two MoaD subunits in a heterotetrameric structure with the two MoaE subunits forming a central dimer"].
- Precursor Z binds at the MoaE dimer interface next to the MoaD C terminus
  [PMID:18092812 "precursor Z is bound by strictly conserved residues in a pocket at the MoaE dimer interface"].
- UniProt CATALYTIC ACTIVITY is tied to PubMed:12571226 (not cached); K119A abolishes activity.

## Curation decisions

- Seven bare GO:0005515 IPI rows (MoaD, MobB): REMOVE per protein-binding policy; MoaD
  interaction captured by GO:1990140 (ACCEPT).
- GO:0032324 (ARBA IEA): MODIFY to GO:0006777, the child the gene already carries; same in
  genes/PSEPK/moaE.
- GO:0042803 homodimer: KEEP_AS_NON_CORE.
- Core MF GO:0030366 molybdopterin synthase activity; complex GO:1990140; cytosol.
