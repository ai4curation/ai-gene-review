# PIK1 (P39104, YNL267W) notes

Evidence journal (YeastPathways phosphoinositide_biosynthesis batch, 2026-10-06).

## Activity
- Type III PI 4-kinase (PI4KB ortholog) [UniProt:P39104 "Type III PI4K"].
- Encodes PI 4-kinase essential for growth [PMID:8194527 "PIK1 encodes a phosphatidylinositol 4-kinase (PI 4-kinase) essential for growth."]; overexpression raises activity [PMID:8248783 "Expression of PIK1 from a multicopy plasmid elevated PtdIns 4-kinase activity"].
- Stt4 and Pik1 have the same biochemical activity but are non-redundant [PMID:10930462 "Both gene products phosphorylate PtdIns at the D-4 position of the inositol ring to generate PtdIns(4)P"]; each single ts mutant halves PtdIns4P, double >10-fold [PMID:10930462 "Both single mutants reduce PtdIns(4)P by approximately 50%"].
- YeastPathways step PI + ATP -> PI4P (EC 2.7.1.67) is correct.

## Location
- TGN and nucleus [PMID:16365163 "GFP-Pik1 localized to cytoplasmic puncta and the nucleus. The puncta colocalized with Sec7-DsRed, a marker of trans-Golgi cisternae."]; both pools needed [PMID:16365163 "PtdIns4P must be generated both in the nucleus and at the Golgi for normal cell function"].
- Golgi recruitment by Frq1 [PMID:16365163 "Frq1 (frequenin orthologue) also is essential for viability and binds near the NH2 terminus of Pik1."] and Gga2 [PMID:22344030 "the Gga2p VHS domain bound directly to a recombinant Pik1p fragment"].

## Processes
- Golgi secretion [PMID:10930462 "pik1(ts) cells exhibit a rapid defect in secretion of Golgi-modified secretory pathway cargos, Hsp150p and invertase"].
- Autophagy / microautophagy roles are downstream lipid requirements [PMID:31125705 "Pik1p and Stt4p play essential roles in autophagosome formation and autophagosome-vacuole fusion in yeast cells, respectively"].

## Curation decisions
- RCA cytosol -> MODIFY to TGN; generic kinase IEA -> MODIFY to GO:0004430; protein binding (Frq1, Gga2) REMOVE as uninformative; ARBA 'cellular response to stress' over-annotated.
- PMID:10587649 not available (no abstract in cache); its IDA/IMP rows accepted because consistent with other evidence.
