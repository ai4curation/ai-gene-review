# arg4 (SPBC215.08c, UniProt O94313) notes

## Naming trap
- S. pombe arg4 = CPSase A large subunit (= S. cerevisiae CPA2). S. cerevisiae ARG4 = argininosuccinate lyase (= S. pombe arg41/arg7).

## Evidence
- [UniProt:O94313 "linked to the arginine pathway and is designated CPSase A (arg5-arg4),"]; [UniProt:O94313 "it is localized to mitochondria and repressed by arginine."]; location from Urrestarazu et al. 1977 (PMID:200419, title only cached) and ORFeome HDA.
- Classical mutant (Kohli et al. 1977, PMID:17248775) and deletion screen (PMID:32896087).
- Not in the PomBase arginine GO-CAM (gomodel:6690711d00000916 omits CPSase).

## Decisions
- IBA cytoplasm MODIFY -> mitochondrial matrix (ancestral cytosolic location; pombe enzyme relocated), propagation_review added.
- Core: MF GO:0004087, contributes_to GO:0004088, in complex GO:0005951, matrix (CPA2 core but mitochondrial).
