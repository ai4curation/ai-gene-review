# GRIN2D review notes

## 2026-11-25 NMDA GO-CAM review

- Ran `just fetch-gene human GRIN2D` to seed the review, GOA, UniProt, and publication cache.
- After the GRIN2C attempt showed that the installed deep-research client only exposed the `claude_code` provider, Falcon/Perplexity deep research was considered unavailable in this checkout and no provider-named deep-research file was written.
- Reviewed the seeded GOA annotations against the cached publications, the UniProt record, the PANTHER GluN2 family transfer, and the sibling GRIN1/GRIN2A/GRIN2B reviews.
- PMID:9489750 cloned and functionally expressed the human NMDAR2D/GluN2D subunit; the direct `GO:0004972 NMDA glutamate receptor activity` and transport rows are retained against that evidence. PMID:27616483 directly supports gain-of-function human GRIN2D channel variants that increase glutamate/glycine potency and open probability.
- The `GO_REF:0000002` InterPro2GO rows for `GO:0005216` and `GO:0038023` were kept as `TOO_GENERAL`, and `GO:0015276 ligand-gated monoatomic ion channel activity` was accepted at the granularity supported by the broad ionotropic-receptor signatures; the NMDA-specific refinement comes from direct, orthology, and phylogenetic evidence instead.
- Rat Grin2d presynaptic and mossy-fiber annotations were kept as non-core orthology transfers, not rejected. Regulation rows that described the receptor as a regulator of the cation transport, presynaptic membrane potential, or synaptic transmission it directly mediates were kept non-core for the presynaptic rat context or marked over-annotated for generic regulation phrasings.
- GO-CAM `66c7d41500003458`: the GluN2D activity, postsynaptic-membrane location, and cation transport agree with this gene review. The GO-CAM review already records a stray `RGD:2739` with-object on the glutamate activator association; that rat gene is Grin2c, not Grin2d.
- The Reactome `R-HSA-9610750` ER-membrane row was kept as over-annotated rather than wrong: it reflects secretory-pathway transit of assembled NMDA receptors, not ER residence of the mature GluN2 subunit.
