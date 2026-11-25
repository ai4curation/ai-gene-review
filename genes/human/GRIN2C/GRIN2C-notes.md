# GRIN2C review notes

## 2026-11-25 NMDA GO-CAM review

- Ran `just fetch-gene human GRIN2C` to seed the review, GOA, UniProt, and publication cache.
- Attempted `just deep-research-falcon human GRIN2C --fallback perplexity-lite`; the installed deep-research client only exposed the `claude_code` provider, so Falcon/Perplexity deep research was unavailable in this checkout and no provider-named deep-research file was written.
- Reviewed the seeded GOA annotations against the cached publications, the UniProt record, the PANTHER GluN2 family transfer, and the sibling GRIN1/GRIN2A/GRIN2B reviews.
- GO-CAM `66c7d41500001120`: the GluN2C activity, postsynaptic-membrane location, and cation transport agree with this gene review. The existing GO-CAM review already records that the enabled_by and transport edges cite `PMID:26875626`, whose cached abstract is GluN2A-focused and does not directly mention GluN2C; `PMID:36309015` is a better direct source for human GluN1-2C receptors.
- The Reactome `R-HSA-9610750` ER-membrane row was kept as over-annotated rather than wrong: it reflects secretory-pathway transit of assembled NMDA receptors, not ER residence of the mature GluN2 subunit.
