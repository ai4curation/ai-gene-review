# SPCC18B5.05c (UniProt Q9USL6) notes

Fetch check: `just fetch-gene SCHPO SPCC18B5.05c` fetched `AC   Q9USL6;` (YJK5_SCHPO, "Putative hydroxymethylpyrimidine/phosphomethylpyrimidine kinase C18B5.05c", 327 aa) - correct [UniProt:Q9USL6].
PomBase API (2026-10-06): no gene name assigned (name = None); product "phosphomethylpyrimidine kinase"; characterisation "biological role inferred"; deletion viable. Folder name kept as the systematic ID.

## Sequence-based evidence
- Single-domain ThiD-family kinase (Pfam Phos_pyr_kin, IPR004399), no C-terminal TenA/thiaminase-II domain - the architecture of bacterial ThiD rather than of the fused S. cerevisiae Thi20/21/22 or S. pombe thi20/thi201 [UniProt:Q9USL6 "CC   -!- SIMILARITY: Belongs to the ThiD family."].
- HMP binding site annotated at residue 54 [UniProt:Q9USL6].
- EC 2.7.1.49 / 2.7.4.7 given with ECO:0000305 (curator inference) and function by similarity to S. cerevisiae THI21 [UniProt:Q9USL6].
- PANTHER PTHR20858:SF20 ("...KINASE C18B5.05C-RELATED"), a subfamily distinct from both thi20 (SF22) and thi201/THI20/21/22 (SF17).
- Pairwise identity ~0.29-0.36 to the other paralogues, over the kinase region only [file:SCHPO/thi201/thi201-bioinformatics/RESULTS.md].
- ORFeome YFP: cytoplasm and nucleus (PomBase HDA cytosol, nucleus).

## Ortholog consistency
- No one-to-one S. cerevisiae ortholog (S. cerevisiae has only the fused THI20/21/22). Module lists it as a member for both kinase steps with THI20/THI21 as reference. I follow the THI20 review's two core functions, all inferred. Note E. coli ThiD (P76422), a seed of the IBA node with the same single-domain architecture, is a bifunctional HMP/HMP-P kinase, so loss of the TenA domain is not expected to affect kinase activity (also, the THI20 C-terminal domain is not required for HMP-P kinase activity [PMID:10383756 "The function of the carboxy-terminal part of the proteins is not yet understood, but it is not required for HMP-P kinase activity."]).

## GO-CAM
- gomodel:66c7d41500000963: SPCC18B5.05c enables GO:0008902 (66c7d41500000992) and GO:0008972 (66c7d41500001012), cytosol, part_of GO:0009228.
