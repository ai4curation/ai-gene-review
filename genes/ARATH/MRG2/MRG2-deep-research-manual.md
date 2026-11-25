# MRG2 manual deep research

## Retrieval

`just deep-research-falcon ARATH MRG2 --fallback perplexity-lite` failed in this worktree because the local `deep-research-client` installation exposed only the `claude_code` provider and the `agentapi` binary was not available. The initial `just fetch-gene ARATH MRG2` call returned a QuickGO/GOA file with only the header row, but a later forced refetch populated the current GOA rows and this review audits those existing annotations.

## Findings

MRG2 (AT1G02740) is one of two Arabidopsis MRG15-family chromatin effectors. The two 2014 Arabidopsis papers agree that MRG1 and MRG2 are partly redundant readers of active H3 methylation. Xu et al. showed MRG2 euchromatin localization, direct chromodomain binding to H3K36me2/3 and H3K4me3 peptides, proximity to H3K36me3/H3K4me3 marks in vivo, dependence on SDG8-made H3K36me3 for MRG2-histone H3 proximity, and direct interaction with HAM1/HAM2 MYST histone acetyltransferases [PMID:25183522]. Bu et al. independently identified MRG2 as an H3K36me3-binding protein in an Arabidopsis nuclear extract pull-down, confirmed MRG1/MRG2 chromodomain binding to H3K36me3 and H3K4me3, solved MRG2 chromodomain structures bound to both trimethylated peptides, and showed MRG2 cooperation with CONSTANS at FT promoter chromatin [PMID:25211338].

The supported molecular function is methyl-histone reader activity. The downstream flowering phenotypes are real, but the mrg1 mrg2 double mutant and shared FT/FLC transcriptional defects are better treated as pathway context than as a separate core GO biological-process annotation for MRG2 alone.

## GO-CAM Consistency

The GO-CAM assignment of MRG2 to `GO:0140003 histone H3K36me3 reader activity` at `GO:0000785 chromatin` is supported.

The MRG2 activity should not have SCL27/AT2G45160 as an input. Xu et al. show that MRG1/MRG2 interact with the MYST H4K5 acetyltransferases HAM1 and HAM2; SCL27/AT2G45160 only shares the HAM1 alias and is a GRAS transcription regulator, not the acetyltransferase partner.

MRG1/AT4G37280 is absent from the current model even though Xu et al. and Bu et al. describe MRG1 as redundant with MRG2.
