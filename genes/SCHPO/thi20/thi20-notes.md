# thi20 (SPBP8B7.17c; UniProt O94265) notes

Fetch: `just fetch-gene SCHPO thi20` failed (UniProt has no gene name, only ORF name); fetched with `-u O94265`. Verified `AC   O94265` (UniProt entry name THI21_SCHPO, "Putative hydroxymethylpyrimidine/phosphomethylpyrimidine kinase 1", 506 aa) [UniProt:O94265].
PomBase API (2026-10-06): name thi20, product "phosphomethylpyrimidine kinase Thi20", characterisation "biological role published", deletion **inviable**.

## Naming traps
- UniProt entry name THI21_SCHPO (for O94265) and THI22_SCHPO (for O94266, PomBase thi201) do not encode orthology to S. cerevisiae THI21/THI22. PomBase "thi20" is not the closest S. pombe relative of S. cerevisiae THI20 either: by PANTHER, thi20 is in PTHR20858:SF22 ("...KINASE 1-RELATED"), whereas thi201 (O94266) shares SF17 ("...KINASE THI20-RELATED") with S. cerevisiae THI20/THI21/THI22 [UniProt:O94265; UniProt:O94266].
- Pairwise identity (local alignment): thi20 vs THI20 0.29; thi201 vs THI20 0.41 [file:SCHPO/thi201/thi201-bioinformatics/RESULTS.md].

## Evidence
- Domain architecture like budding-yeast Thi20/21/22: N-terminal ThiD-like HMP/HMP-P kinase domain (Pfam Phos_pyr_kin, IPR004399) + C-terminal TenA/thiaminase-2 domain (Pfam TENA_THI-4) [UniProt:O94265 "In the N-terminal section; belongs to the ThiD family."].
- Function and EC 2.7.1.49/2.7.4.7 by similarity to S. cerevisiae THI20 (Q08224) only [UniProt:O94265 "Catalyzes the phosphorylation of hydroxymethylpyrimidine"]. No S. pombe biochemistry.
- In S. cerevisiae, THI20 and THI21 both have HMP and HMP-P kinase activity [PMID:15614489 "we demonstrate that both Thi20p and Thi21p proteins also have HMP kinase activity."]; two of three family members are HMP-P kinases [PMID:10383756 "We demonstrate that two members are isofunctional and encode a hydroxymethylpyrimidine phosphate (HMP-P) kinase (EC 2.7.4.7)"]. THI22 has no demonstrated activity (THI22 review).
- ORFeome YFP: cytoplasm, nucleus, cytosol (PomBase HDA).
- PomBase lists deletion as inviable with germination/cell-cycle arrest phenotypes and increased acid phosphatase activity (PomBase API; large-scale deletion screens). Surprising for a thiamine-biosynthetic kinase in rich medium (which contains thiamine) when two paralogues exist; could indicate a non-thiamine essential function or a screen artefact. Not used as evidence for activity; raised as a question.

## Ortholog consistency
- S. cerevisiae THI20 review core: two core functions, GO:0008972 and GO:0008902, both directly_involved_in GO:0009228, cytosol; thiaminase (GO:0050334) kept non-core. I keep the two kinase core functions. No thiaminase annotation exists for thi20 in GOA (InterPro TenA entry IPR004305 here, not the thiaminase-specific IPR027574); not proposing NEW.
- Difference: activity for S. pombe thi20 is inferred only (phylogeny + sequence); essentiality is S. pombe specific.

## GO-CAM
- gomodel:66c7d41500000963: thi20 enables GO:0008902 (66c7d41500000977) and GO:0008972 (66c7d41500001000), cytosol, part_of GO:0009228. Same model also has parallel nodes for thi201 and SPCC18B5.05c.
