# tim50 review notes

## Deep research

Automated deep research was tested in this worktree on the closely related `tim17` review. Falcon plus Perplexity-lite failed because those providers were unavailable in the deep-research client, and the direct `claude_code` provider failed because it was not logged in. Because the provider failures were environmental and happened before any report was written, the TIM23 subunit reviews were completed manually instead of fabricating provider-named deep-research files.

Manual review used the fetched PomBase GOA, the curated UniProtKB record O13636, the cached PANTHER family PTHR12210 PAINT table and PTHR12210 family review, the PMID cache, and the GO-CAM context from `gocams/69729a3800007453/69729a3800007453-src.yaml`.

## Functional synthesis

S. pombe tim50 is the fission-yeast ortholog of S. cerevisiae TIM50 and belongs to the Tim50 branch of the broader PTHR12210 FCP1-like phosphatase family. PAINT node PTN002639282 supports TIM23 complex membership and matrix-import pathway participation for Tim50 while also recording an IRD loss of ancestral phosphoprotein phosphatase activity. The PTHR12210 family review judges that phosphatase loss to be supported for the Tim50 clade.

Tim50 is a single-pass inner mitochondrial membrane subunit of the TIM23 presequence translocase. Its large C-terminal domain faces the intermembrane space, where Tim50 receives presequences emerging from the TOM complex, interacts with Tim23, gates the channel, and directs matrix-destined precursors toward the Tim17/Tim23 channel.

The fetched GOA contains an `IC` row placing tim50 in the mitochondrial matrix by inference from TIM23 complex membership. That is a lateral compartment error: TIM23 is an inner-membrane complex, and the receptor function of Tim50 occurs from the intermembrane-space side of an inner-membrane protein. GO-CAM model 69729a3800007453 has the same `occurs_in GO:0005759` matrix location on the tim50 activity, so the final GO-CAM consistency PR should repoint that activity to `GO:0005743 mitochondrial inner membrane`.

## GO-CAM consistency

- In model 69729a3800007453, activity `gomodel:69729a3800007453/69729a3800007642` for PomBase:SPBC17A3.01c uses `GO:0005759 mitochondrial matrix` as `occurs_in`; the gene review corrects the matching GOA IC row to `GO:0005743 mitochondrial inner membrane`.
