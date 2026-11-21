# SYN1 notes

## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- One GO:0005794 row: IEA GO_REF:0000044 mapped from the UniProt item "Golgi apparatus
  {ECO:0000250|UniProtKB:O88935}" (by similarity to mouse synapsin-1).
- Traced the donor: in UniProt O88935 (mouse Syn1, retrieved 2026-11-19 from rest.uniprot.org) the Golgi
  item is tagged ECO:0000269 to PMID:11571277 (Spielhaupter and Schaetzl 2001, J Biol Chem, DOI
  10.1074/jbc.M103289200), a yeast two-hybrid screen with prion protein as bait. Rat P09951 inherits the
  same item from O88935 by similarity.
- PMID:11571277 fetched: abstract only, no PMC record; publisher full text returned HTTP 403. The abstract
  has no Golgi content, so the marker basis of the Golgi claim cannot be checked.
- Verdict: unreadable donor (CD247 rule) -> UNDECIDED, replacing the earlier KEEP_AS_NON_CORE that assumed
  a biosynthetic transit pool (synapsin-1 is a soluble cytosolic peripheral synaptic vesicle protein, so
  it does not transit the Golgi). Readings set out in the reason: marker-confirmed endogenous pool ->
  KEEP_AS_NON_CORE; perinuclear overexpression signal -> MARK_AS_OVER_ANNOTATED.
