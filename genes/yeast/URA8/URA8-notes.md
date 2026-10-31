# URA8 (YJR103W, P38627) notes

Review context: YeastPathways module `de_novo_pyrimidine_synthesis` (CTP synthase step, EC 6.3.4.2, CTPSYN-RXN).

## Evidence journal
- Minor CTP synthase isozyme, cloned as synthetic-lethal partner of ura7 [PMID:8121398 "a second gene, named URA8, which also encodes a CTP synthetase"]; double null lethal [PMID:8121398 "simultaneous presence of null alleles both URA7 and URA8 is lethal"]; URA7 is the major gene [PMID:8121398 "URA7 appears to be the major gene for CTP biosynthesis"].
- Purified from cytosol, kinetics, dimer-tetramer, GTP activation, CTP inhibition [PMID:7559626 "URA8-encoded CTP synthetase was purified to apparent homogeneity by ammonium sulfate fractionation of the cytosolic fraction"; "existed as a dimer which oligomerized to a tetramer in the presence of its substrates UTP and ATP"].
- Forms cytoplasmic filaments (cytoophidia) with Ura7 [PMID:20713603 "Ura7p and Ura8p, which both encode for CTP synthases in S. cerevisiae, coassembled into a common filament"].
- UniProt: catalytic activity RHEA:26426, EC 6.3.4.2; pathway CTP biosynthesis via de novo pathway step 2/2 [UniProt:P38627].

## Curation observations
- YeastPathways RCA rows put the PWY-7176 / PYRIMID-RNTSYN-PWY step under GO:0006207 'de novo' pyrimidine *nucleobase* biosynthetic process and the PRPP-PWY-1 superpathway under GO:0009165; both MODIFY to GO:0044210 'de novo' CTP biosynthetic process. The PANTHER IBA GO:0019856 (pyrimidine nucleobase biosynthetic process) is the same wrong-branch problem.
- Default cytosol compartment is correct here (cytosolic purification).
- Vacuole HDA (PMID:26928762, N-terminal SWAT-GFP endomembrane library) cannot be verified for URA8; left UNDECIDED.
