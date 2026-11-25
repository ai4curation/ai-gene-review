# SDG8 manual deep research

## Retrieval

`just deep-research-falcon ARATH SDG8 --fallback perplexity-lite` failed in this worktree because the local `deep-research-client` installation exposed only the `claude_code` provider and the `agentapi` binary was not available. `just fetch-gene ARATH SDG8` returned a QuickGO/GOA file with only the header row, so the review proposes new rows instead of modifying existing ones.

## Functional Synthesis

SDG8/ASHH2/EFS/LAZ2 is the main Arabidopsis SET2-family H3K36 methyltransferase. Xu et al. reported direct SDG8 oligonucleosome methylation, nuclear localization, and a severe sdg8 defect in H3K36me2/H3K36me3, summarized in the abstract as "SDG8 is thus specifically required for di- and trimethylation of H3K36" [PMID:18070919].

Earlier FLC-focused work mapped EFS to AT1G77300 and showed that it is needed for high FLC expression in FRI-containing and autonomous-pathway backgrounds [PMID:16258034]. Another study showed that loss of SDG8 reduces H3K36me2 at FLC-associated chromatin and causes reduced FLC expression and early flowering [PMID:16299497].

Later locus-specific work repeatedly reinforced H3K36me3 as an SDG8-dependent active mark. ASHH2/sdg8 mutants reduce H3K36me3 at AP1, AtDMC1 and MYB99 during reproductive development without comparable H3K4me3 or H3K36me2 loss at those loci [PMID:19915673]. LAZ2/SDG8 maintains H3K36me3 at LAZ5 and RPM1 immune-receptor chromatin [PMID:20949080]. SDG8 is also needed for H3K36me3 at brassinosteroid-regulated genes [PMID:24838002].

The GO-CAM source paper places SDG8 upstream of MRG1/MRG2: SDG8 loss nearly eliminates H3K36me3, abolishes MRG2 binding to target chromatin, and the plant MRG readers recruit HAM1/HAM2 to raise histone H4 acetylation near flowering genes [PMID:25183522].

The SDG8 CW domain binds methylated H3K4 peptides [PMID:21522130], and SDG8 is recruited in an FRI-C/SWR1-C context at FLC [PMID:21282526]. The methyl-H3K4 binding supports broad histone reader activity, while the FRI-C/SWR1-C context does not support direct H3K4 methyltransferase activity.

## GO-CAM Consistency

The SDG8 gene review agrees with the GO-CAM's `GO:0140955 histone H3K36 trimethyltransferase activity` assignment and `GO:0000785 chromatin` location.

The gene review also proposes `GO:0140954 histone H3K36 dimethyltransferase activity` because primary literature supports a global H3K36me2 defect in sdg8. This makes the GO-CAM's strict serial SDG7-dimethylates/SDG8-trimethylates relationship too narrow as a model of all H3K36 methylation: SDG8 itself is required for a substantial global H3K36me2 signal, while SDG7's exact product state has not been assayed with purified enzyme.

The model-wide process `GO:0140673 transcription elongation-coupled chromatin remodeling` is a poor biological-process fit for the Arabidopsis MRG mechanism. Xu et al. emphasize a plant-specific 5' H3K36me3 profile and a pathway in which MRG1/MRG2 read SDG8-mediated H3K36me3 to recruit HAM1/HAM2 and elevate H4 acetylation at FT and FLC; the process should be represented as positive chromatin-mediated transcriptional regulation of flowering-time genes rather than elongation-coupled restoration after RNA polymerase II passage.
