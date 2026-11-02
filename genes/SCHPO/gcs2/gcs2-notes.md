# gcs2 (SPCC737.06c, UniProt O94246) notes

## Identity
- UniProt: "Putative glutamate--cysteine ligase regulatory subunit"; entry GSH0_SCHPO has no gene name (ORF only), so `just fetch-gene SCHPO gcs2` failed; fetched with -u O94246.
- Aldo/keto reductase fold, glutamate--cysteine ligase light chain subfamily; PANTHER PTHR13295:SF4 [UniProt:O94246].
- S. cerevisiae has no GCLM ortholog; human ortholog GCLM (P48507).

## Evidence
- No direct S. pombe biochemical demonstration that gcs2 binds or modulates gcs1 was found; GO MF annotations are IBA/ISO/IEA from GCLM orthologs (Drosophila Gclm, mouse/rat Gclm).
- PomBase phenotypes (web, not cached): deletion increases ROS and causes silver sensitivity [PomBase gene page SPCC737.06c].
- HTP YFP localization: cytoplasm/cytosol [PMID:16823372; UniProt "Cytoplasm {ECO:0000269|PubMed:16823372}"].

## GO-CAM
- 68b0f0d000008341: gcs2 enables GO:1990609, cytosol, part_of GO:0006750, directly positively regulates gcs1 GO:0004357. Consistent with homology; S. pombe experimental support for the regulatory activity is lacking.
