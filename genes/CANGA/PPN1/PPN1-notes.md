# PPN1 notes

## 2026-11-06

- Fetched the C. glabrata `PPN1` seed with `just fetch-gene CANGA PPN1 --uniprot-id Q6FMQ0`; a symbol-based fetch hit UniProt rate limiting first, so the review used the accession from the audited PTHR10340 family member table.
- Falcon deep research was unavailable in this checkout: `just deep-research CANGA PPN1 --provider falcon` reported that only `claude_code` was configured. I therefore used the seeded GOA rows, the Q6FMQ0 UniProt record, the PTHR10340 PAINT and family review files, the completed S. cerevisiae PPN1 review, and manual PubMed searches.
- Manual PubMed searches on 2026-11-06 for CAGL0K06237, Q6FMQ0, "Candida glabrata" PPN1, "Nakaseomyces glabratus" PPN1, "Candida glabrata" polyphosphate endopolyphosphatase, and "Candida glabrata" vacuole polyphosphate found no direct C. glabrata PPN1 characterization.
- The C. glabrata record has no direct publication-backed function rows beyond the 2004 comparative yeast genome paper. UniProt infers the endopolyphosphatase reaction and vacuole-membrane topology by similarity to S. cerevisiae Ppn1, and PAINT places Q6FMQ0 in PTHR10340:SF55 under the fungal `PTN000818947` Ppn1 node.
- Current PAINT supports the same four fungal Ppn1 conclusions used in the S. cerevisiae review: `GO:0000298 endopolyphosphatase activity`, `GO:0004309 exopolyphosphatase activity`, `GO:0000324 fungal-type vacuole`, and `GO:0006798 polyphosphate catabolic process`. The self-seed concern does not arise for C. glabrata because Q6FMQ0 is a recipient, while the process IBD also has a CGD seed from *Candida albicans* `CAL0000182615`.
- The TreeGrafter `GO:0008081 phosphoric diester hydrolase activity` row is stale or over-propagated relative to the current PAINT file: `PTN000818947` now has a 2026 IRD that prunes the metazoan/ENPP-like phosphoric-diester-hydrolase assertion before the fungal Ppn1 branch.
