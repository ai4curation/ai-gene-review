# TCF7L2 notes

## 2026-11-26 curation

- Automated deep research did not run in this workspace: `just deep-research human TCF7L2 --provider perplexity` reported that `perplexity` was unavailable and only `claude_code` was configured. I used cached GOA evidence, UniProt, Reactome, PANTHER family data, and cached primary papers for manual synthesis instead.
- TCF7L2 is the heavily annotated human TCF4 member of PTHR10373. The 1997 hTCF-4 study cloned the colonic TCF family member and directly placed it in constitutively active nuclear beta-catenin-TCF transcriptional complexes in APC-deficient colon carcinoma cells [PMID:9065401, "hTcf-4 transactivates transcription only when associated with beta-catenin"].
- Multiple rows describe the same core Wnt effector mechanism at different granularities: RNA polymerase II cis-regulatory DNA binding, beta-catenin binding, beta-catenin-TCF7L2 complex membership, chromatin or nucleoplasm localization, and canonical Wnt target-gene regulation. These were accepted as core where the term was specific.
- TCF7L2 also has many cell-context rows. Beta-cell, endocrine, endothelial, EMT, adipocyte, androgen-receptor, and smooth-muscle annotations were kept as non-core when they represented direct transcriptional regulation or direct perturbation phenotypes rather than the family-wide core mechanism.
- The 26 `GO:0005515` rows were all left distinct by PMID and `WITH/FROM`, then removed only under the bare-protein-binding policy.
