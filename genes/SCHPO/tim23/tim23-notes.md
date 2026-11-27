# tim23 review notes

## Deep research

Automated deep research was tested in this worktree on the closely related `tim17` review. Falcon plus Perplexity-lite failed because those providers were unavailable in the deep-research client, and the direct `claude_code` provider failed because it was not logged in. Because the provider failures were environmental and happened before any report was written, the TIM23 subunit reviews were completed manually instead of fabricating provider-named deep-research files.

Manual review used the fetched PomBase GOA, the curated UniProtKB record Q9USM7, the cached PANTHER family PTHR15371 PAINT table, the PMID cache, and the GO-CAM context from `gocams/69729a3800007453/69729a3800007453-src.yaml`.

## Functional synthesis

S. pombe tim23 is the fission-yeast ortholog of S. cerevisiae TIM23 and is assigned by PANTHER to the eukaryotic Tim23 PAINT node PTN000394914. That node carries TIM23 complex membership, protein transmembrane transporter activity, and protein import into mitochondrial matrix.

Tim23 is a multi-pass inner mitochondrial membrane core subunit of the TIM23 presequence translocase. Budding-yeast Tim23 can form a presequence- and voltage-sensitive channel, and the S. pombe Q9USM7 record is a member of the same conserved Tim17/Tim23 family. The GO-CAM model 69729a3800007453 represents tim23 with `GO:0008320`, `GO:0030150`, and `GO:0005743`; that agrees with this gene review.

The ISO row for `GO:0032977 membrane insertase activity` uses `UniProtKB:M0R003` as its supporting entity. Live UniProt identifies M0R003 as an unreviewed Homo sapiens TIMM50 fragment, not TIMM23, so that row's own WITH/FROM support does not establish Tim23 as a membrane insertase. TIM23-SORT-mediated inner-membrane insertion is retained as a biological process for tim23, but the molecular function should stay at `GO:0008320` unless direct Tim23 evidence supports a specific insertase assertion.

## GO-CAM consistency

No disagreement with GO-CAM model 69729a3800007453 was found for tim23.
