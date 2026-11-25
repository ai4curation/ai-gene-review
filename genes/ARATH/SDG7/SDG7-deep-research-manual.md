# SDG7 manual deep research

## Retrieval

`just deep-research-falcon ARATH SDG7 --fallback perplexity-lite` failed in this worktree because the local `deep-research-client` installation exposed only the `claude_code` provider and the `agentapi` binary was not available. `just fetch-gene ARATH SDG7` also returned a QuickGO/GOA file with only the header row, so there were no pre-existing annotation rows to review.

## Findings

SDG7/ASHH3 (AT2G44150) is a SET2-family SET-domain protein by sequence. Its UniProt entry has only similarity-based functional and nuclear/centromeric statements, so the reviewed gene file should not treat those statements as Arabidopsis-specific experiments.

The direct Arabidopsis functional evidence found during manual review comes from the MRG GO-CAM source paper. Xu et al. showed that `sdg8` nearly eliminates H3K36me3 while reducing H3K36me2 only slightly, then reported that the `sdg7 sdg8` double mutant "fully abolishes both the di- and tri-methylation marks at H3K36" [PMID:25183522]. That is good evidence that SDG7 contributes to residual H3K36 methylation in the absence of SDG8, but it is genetic evidence from a double mutant rather than an assay of purified SDG7.

## GO-CAM Consistency

The GO-CAM assigns SDG7 to `GO:0140954 histone H3K36 dimethyltransferase activity` and connects it to the SDG8 H3K36 trimethyltransferase with `directly provides input for`. The gene review is deliberately broader: it proposes `GO:0046975 histone H3K36 methyltransferase activity` because the Xu et al. double-mutant result does not isolate SDG7's exact product state.

The GO-CAM location `GO:0000785 chromatin` is plausible and is retained as a curator inference from SDG7's H3K36 methyltransferase role, not as a direct ChIP or localization result for SDG7.
