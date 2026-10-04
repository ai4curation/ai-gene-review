# ARMC1 review notes

## Sources
- Affinage: trust gates clear. The two key papers were checked in full text: PMID:31644573 (peripheral MICOS/MIB component, distribution) and PMID:40203102 (MIRO-ARMC1-MTFR assembly; DNAJC11-mediated release).
- PMID:40203102 states the HMA-like domain "lacks cysteines in the positions required for metal coordination", which contradicts the InterPro-based metal ion binding IEA.
- Partner accessions were resolved by UniProt batch query: MTFR1L (Q9H019), RNF24 (Q9Y225), DNAJC11 (Q9NVH1), MTX1 (Q13505), IMMT (Q16891), MICOS10 (Q5TGZ0), SAMM50 (Q9Y512).

## Decisions
- ACCEPT:
  - Cytoplasm, cytosol, mitochondrion and outer mitochondrial membrane (dual localization).
  - Intracellular distribution of mitochondria (IMP).
- REMOVE:
  - Metal ion binding (IEA): the domain lacks the coordinating cysteines.
  - 11 generic protein-binding rows (policy).
- NEW: protein-macromolecule adaptor activity (IDA, PMID:40203102), for MIRO-MTFR assembly.
