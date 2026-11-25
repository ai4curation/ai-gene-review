# GRIN2D review notes

## 2026-11-25 NMDA GO-CAM review

- Ran `just fetch-gene human GRIN2D` to seed the review, GOA, UniProt, and publication cache.
- After the GRIN2C attempt showed that the installed deep-research client only exposed the `claude_code` provider, Falcon/Perplexity deep research was considered unavailable in this checkout and no provider-named deep-research file was written.
- Reviewed the seeded GOA annotations against the cached publications, the UniProt record, the PANTHER GluN2 family transfer, and the sibling GRIN1/GRIN2A/GRIN2B reviews.
- GO-CAM `66c7d41500003458`: the GluN2D activity, postsynaptic-membrane location, and cation transport agree with this gene review. The GO-CAM review already records a stray `RGD:2739` with-object on the glutamate activator association; that rat gene is Grin2c, not Grin2d.
- The Reactome `R-HSA-9610750` ER-membrane row was kept as over-annotated rather than wrong: it reflects secretory-pathway transit of assembled NMDA receptors, not ER residence of the mature GluN2 subunit.
