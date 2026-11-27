# tim17 review notes

## Deep research

Automated deep research was attempted before this manual review. `just deep-research-falcon SCHPO tim17 --fallback perplexity-lite` failed because the deep-research client exposed neither the `falcon` nor the `perplexity` provider in this checkout. `just deep-research-claude-code SCHPO tim17` also failed because the uvx `claude_code` provider was not logged in.

Manual review used the fetched PomBase GOA, the curated UniProtKB record P87130, the cached PANTHER family PTHR10485 PAINT table, the PMID cache, and the GO-CAM context from `gocams/69729a3800007453/69729a3800007453-src.yaml`.

## Functional synthesis

S. pombe tim17 is the fission-yeast ortholog of S. cerevisiae TIM17 and is assigned by PANTHER to the eukaryotic Tim17 PAINT node PTN000050380. That node carries TIM23 complex membership, protein transmembrane transporter activity, and protein import into mitochondrial matrix. The row for GO:0008320 is correctly `contributes_to` in the IBA.

Tim17 is a four-pass inner mitochondrial membrane protein and core TIM23 subunit. It works with Tim23 in the presequence translocase channel and helps couple the translocase to the matrix import motor. The GO-CAM model 69729a3800007453 represents that role as a Tim17 activity with `GO:0008320`, `GO:0030150`, and `GO:0005743`; that agrees with this gene review.

The fetched GOA also contains an `IC` ATP hydrolysis activity row inferred from `GO:0140657`. That inference conflates the ATP dependence of matrix import with a catalytic activity of Tim17. In the TIM23 machinery, ATP hydrolysis is provided by the matrix Hsp70 motor rather than by Tim17.

The `GO:7770060` TIM23-SORT route is retained as a supported TIM23 translocase process. It is not the process modeled in 69729a3800007453, but it is a central second mode of the same inner-membrane translocase.

## GO-CAM consistency

No disagreement with GO-CAM model 69729a3800007453 was found for tim17.
