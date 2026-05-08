# catC notes

- `catC` in *Pseudomonas putida* KT2440 corresponds to UniProt `Q88GK7` / locus `PP_3714` and is annotated as muconolactone delta-isomerase, EC `5.3.3.4` [UniProt:Q88GK7 "RecName: Full=Muconolactone Delta-isomerase"; "Reaction=(S)-muconolactone = (4,5-dihydro-5-oxofuran-2-yl)-acetate;"].
- The Falcon deep research places CatC in the catechol branch of the beta-ketoadipate pathway, downstream of CatA and CatB [file:PSEPK/catC/catC-deep-research-falcon.md "CatC functions in the **catechol branch of the β-ketoadipate pathway**, downstream of CatA and CatB."].
- Falcon also supports that `catBC` is an operon under CatR control rather than an isolated enzyme annotation [file:PSEPK/catC/catC-deep-research-falcon.md "**catBC is an operon** encoding **CatB (EC 5.5.1.1)** and **CatC (EC 5.3.3.4)**."].
- Review decision: keep `GO:0016159` as the core MF term, but narrow `GO:0042952 beta-ketoadipate pathway` to `GO:0019615 catechol catabolic process, ortho-cleavage`, because UniProt places CatC at the catechol-derived step `3/3` rather than generically across the whole pathway [UniProt:Q88GK7 "4,5-dihydro-2-furylacetate from catechol: step 3/3."].
