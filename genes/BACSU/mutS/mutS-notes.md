# B. subtilis mutS (P49849) notes

## 2026-11-13 review session

Context: Gram-positive exemplar of MutH-independent MMR for the module.
All GOA rows are IBA/IEA; experimental literature on the gene was fetched
into publications/.

### Function summary (with provenance)

- mutS-mutL operon; deletion raises spontaneous mutation and abolishes the transformation marker effect [PMID:8760914 "Deletion of both mutS and mutL resulted in an increase in the frequency of spontaneous mutations and abolished the marker effect observed in transformation."].
- 225-fold increased mutation frequency for mutS null (UniProt DISRUPTION PHENOTYPE, ECO:0000269 PubMed:12483591; PMID:12483591 has no cached abstract).
- MutS C terminus binds the beta clamp; required for MutS and MutL foci [PMID:18280235 "We demonstrate that the C terminus of Bacillus subtilis MutS is necessary for an interaction with beta clamp."; "it is mismatch recognition that licenses MutS's interaction with beta clamp"].
- No purified-protein biochemistry on B. subtilis MutS was found in the cache; mismatch binding rests on the bacterial MutS IBA node (E. coli seed, PMID:3014530).

### Decisions

- Damaged DNA binding -> MARK_AS_OVER_ANNOTATED; dsDNA binding IBA -> MODIFY to GO:0030983; ATP binding -> KEEP_AS_NON_CORE; others ACCEPT.
- No GO term exists for beta sliding clamp binding (searched the local GO), so no NEW MF row was added.
