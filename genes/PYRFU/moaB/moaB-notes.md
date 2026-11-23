# moaB (Q8U3T3, PF0372) notes, Pyrococcus furiosus

Deep research providers were unavailable for this session (no API keys), so no
`-deep-research-<provider>.md` file exists. The review is built from the UniProt record and
the cached abstract of PMID:18154309 (Bevers et al. 2008), cached for this review.

## Evidence

- Active MPT adenylyltransferase [PMID:18154309 "MoaB reconstituted the function of the homologous Escherichia coli MogA protein and catalyzes the adenylylation of MPT in a Mg2+ and ATP-dependent way."].
- Hexamer; up to 20-fold faster at 80 C; Km 225 uM ATP; D56A abolishes activity (UniProt,
  ECO:0000269 PubMed:18154309).
- E. coli MoaB is inactive [PMID:18154309 "only MogA is able to catalyze MPT adenylylation, whereas E. coli MoaB is inactive."].
  So the MoaB family (PANTHER PTHR43232) is not uniformly active; the activity of this archaeal
  member is experimentally established, and the GO:0061598 row for it is sound.

## Curation decisions

- GO:0061598 (IEA, EC mapping) ACCEPT as core function; GOA has no experimental row for it.
- GO:0006777 (InterPro2GO) MODIFY to the metal-neutral parent GO:0032324: P. furiosus uses
  tungsten enzymes, and the adenylylation serves W and Mo cofactor maturation
  [PMID:18154309 "MogA, Cnx1G, and MoaB proteins exhibit the same adenylyl transfer activity essential for metal insertion in W or Mo cofactor maturation."].
  E. coli MogA keeps GO:0006777 because its evidence is Mo-specific.
- Cytosol (TreeGrafter) kept as non-core.
