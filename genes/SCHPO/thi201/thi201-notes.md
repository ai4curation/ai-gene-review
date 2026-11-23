# thi201 (SPBP8B7.18c; UniProt O94266) notes

Fetch: `just fetch-gene SCHPO thi201` failed (UniProt has only the ORF name); fetched with `-u O94266`. Verified `AC   O94266` (UniProt entry name THI22_SCHPO, "Putative hydroxymethylpyrimidine/phosphomethylpyrimidine kinase 2", 551 aa) [UniProt:O94266].
PomBase API (2026-10-06): name thi201, product "phosphomethylpyrimidine kinase Thi201", characterisation "biological role inferred", deletion viable. thi201 and thi20 (SPBP8B7.17c) have consecutive systematic IDs on the same cosmid, suggesting neighbouring loci (tandem paralogues; not checked further).

## Naming traps
- UniProt mnemonic THI22_SCHPO does not mean orthology to S. cerevisiae THI22.
- thi201, not thi20, is the S. pombe protein in the same PANTHER subfamily as S. cerevisiae THI20/THI21/THI22 (PTHR20858:SF17, "HYDROXYMETHYLPYRIMIDINE_PHOSPHOMETHYLPYRIMIDINE KINASE THI20-RELATED") [UniProt:O94266]; thi20 is SF22.
- Pairwise identity (Biopython local alignment, BLOSUM62): thi201 vs THI20 0.41, vs THI21 0.40, vs THI22 0.38; thi20 vs THI20 0.29 [file:SCHPO/thi201/thi201-bioinformatics/RESULTS.md]. Modest, so this orders similarity only.

## Evidence
- Two-domain: ThiD-like HMP/HMP-P kinase (IPR004399, Pfam Phos_pyr_kin) + C-terminal TenA/thiaminase-2 domain [UniProt:O94266].
- Function and EC by similarity to S. cerevisiae THI21 (Q08975) only [UniProt:O94266 "Catalyzes the phosphorylation of hydroxymethylpyrimidine"].
- ORFeome YFP: cytoplasm; PomBase HDA cytosol.
- Budding-yeast THI20/THI21 are isofunctional HMP-P kinases and also HMP kinases [PMID:10383756; PMID:15614489].

## Ortholog consistency
- S. cerevisiae THI21 review core: GO:0008972 / GO:0009228 / cytosol; THI20 review adds GO:0008902 as a second core function. I follow THI20 (both kinase activities core) since the IBA node carries both and the module lists thi201 in both the HMP-kinase and HMP-P-kinase steps.
- No S. pombe experimental data; no S. pombe-specific divergence known.

## GO-CAM
- gomodel:66c7d41500000963 has thi201 enabling GO:0008902 (66c7d41500000985) and GO:0008972 (66c7d41500001006), cytosol, part_of GO:0009228. The module's gocam_associations for the two kinase steps cite only the thi20 nodes; the thi201 and SPCC18B5.05c nodes exist too.
