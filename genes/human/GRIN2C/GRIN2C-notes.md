# GRIN2C review notes

## 2026-11-25 NMDA GO-CAM review

- Ran `just fetch-gene human GRIN2C` to seed the review, GOA, UniProt, and publication cache.
- Attempted `just deep-research-falcon human GRIN2C --fallback perplexity-lite`; the installed deep-research client only exposed the `claude_code` provider, so Falcon/Perplexity deep research was unavailable in this checkout and no provider-named deep-research file was written.
- Reviewed the seeded GOA annotations against the cached publications, the UniProt record, the PANTHER GluN2 family transfer, and the sibling GRIN1/GRIN2A/GRIN2B reviews.
- PMID:36309015 directly supports functional human GluN1/GluN2C and GluN1/GluN2D receptors: "The GluN2C and GluN2D subunits form ion channels with distinct properties". That paper is the direct support for the core NMDA receptor activity and cation transport calls.
- PMID:36115835 tested the GRIN2C C-terminal PBM in a human PDZome affinity survey; it reports that "the closest neighbors of the major oncoproteins HPV16 E6, HPV18 E6, and HTLV1 Tax1 in our explored interactome are CYSLTR2, NET1, and GRIN2C, respectively". Those rows refine bare `GO:0005515 protein binding` to `GO:0030165 PDZ domain binding`.
- The HuRI yeast two-hybrid rows from PMID:32814053 were removed because they establish binary partner candidates but not a more specific binding molecular function. The NR1 knockout and GluN2A-PAM papers support general NMDA-receptor physiology rather than GRIN2C-specific process assertions.
- The `GO_REF:0000002` InterPro2GO rows for `GO:0005216` and `GO:0038023` were kept as `TOO_GENERAL`, and `GO:0015276 ligand-gated monoatomic ion channel activity` was accepted at the granularity supported by the broad ionotropic-receptor signatures; the NMDA-specific refinement comes from direct, orthology, and phylogenetic evidence instead.
- Regulation rows that described the receptor as a regulator of the cation transport or synaptic transmission it directly mediates were marked over-annotated, leaving direct cation transport, EPSP, and excitatory chemical synaptic transmission rows as the accepted biological-process assertions.
- GO-CAM `66c7d41500001120`: the GluN2C activity, postsynaptic-membrane location, and cation transport agree with this gene review. The existing GO-CAM review already records that the enabled_by and transport edges cite `PMID:26875626`, whose cached abstract is GluN2A-focused and does not directly mention GluN2C; `PMID:36309015` is a better direct source for human GluN1-2C receptors.
- The Reactome `R-HSA-9610750` ER-membrane row was kept as over-annotated rather than wrong: it reflects secretory-pathway transit of assembled NMDA receptors, not ER residence of the mature GluN2 subunit.
