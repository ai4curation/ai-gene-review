# gpm1 (S. pombe, UniProt P36623, SPAC26F1.06) notes

Role in module `emp_glycolysis`: phosphoglycerate mutase step, cofactor-dependent dPGM (EC 5.4.2.11); S. cerevisiae counterpart GPM1.

## Evidence
- BPG-dependent PGAM subfamily [UniProt:P36623 "SIMILARITY: Belongs to the phosphoglycerate mutase family. BPG-"].
- Purified with 2,3-BPG elution; monomeric ~23 kDa [PMID:2996957 "it is monomeric with Mr approximately 23,000, an extremely low value for this enzyme."].
- Expressed in S. cerevisiae gpm1 deletion [PMID:8765231 "The small, monomeric, phosphoglycerate mutase (PGAM) from Schizosaccharomyces pombe has been overexpressed in a strain of Saccharomyces cerevisiae in which the gene encoding PGAM has been deleted"]; His163 active site [PMID:8765231 "The third mutant (H163Q) involving a histidine thought to be part of the active site has greatly reduced mutase and phosphatase activities."].
- Both 1985 and 1996 papers are abstract-only in cache.

## Curation decisions
- catalytic activity and intramolecular phosphotransferase activity (IEA) -> MODIFY to GO:0004619.
- IBA to obsolete GO:0061621 -> MODIFY to GO:0006096.
- Differs from S. cerevisiae Gpm1 in quaternary structure (monomer vs tetramer); same activity.
