# DDAH1 notes

## Review notes

- `just deep-research-perplexity human DDAH1` could not run because only `claude_code`
  was configured and `agentapi` was absent from `PATH`. I used the fetched UniProt,
  GOA, publication caches, the Reactome cache, and PTHR12737 PAINT files instead of
  writing a provider-named deep-research file by hand.
- DDAH1 is the active human ADMA/L-NMMA dimethylargininase in PTHR12737. Forbes et al.
  measured recombinant hDDAH1 hydrolysis of ADMA and L-NMMA, and the 2023 multicentre
  DDAH2 consortium re-confirmed DDAH1 activity under the same conditions in which DDAH2
  was inactive.
- The PMID:19663506 `GO:0036487 nitric-oxide synthase inhibitor activity` row is the
  clearest bad DDAH1 row. The paper tested known NOS inhibitors as inhibitors of
  recombinant DDAH1; it did not show that DDAH1 directly inhibits NOS. The same PMID
  already supports an IDA row to `GO:0016403 dimethylargininase activity`.
- Reactome `R-HSA-203615` is the broad eNOS activation pathway. Its nested DDAH1
  reaction, `R-HSA-5693373`, correctly places DDAH1 as the ADMA hydrolase that relieves
  NOS inhibition.
- The only GO-CAM indexed for this family is mouse model `69c59f8a00002841`, which
  places mouse Ddah1 in a nitric oxide biosynthetic-process model. There is no production
  human DDAH GO-CAM to review in this family PR.
