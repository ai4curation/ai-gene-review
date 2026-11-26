# E. coli MetE substrate specificity (PMID:16618097)

Primary source: Taurog, Jakubowski and Matthews (2006), DOI10.1021/bi060051u; https://pmc.ncbi.nlm.nih.gov/articles/PMC2041902/ . Full PMC text read 2026-11-07; the normal publication cache is abstract-only and has not been edited. Acquisition details are in 16618097-provenance.json. The Introduction states, for monoglutamyl methyltetrahydrofolate:

> neither a substrate nor an inhibitor

The Methods identify the expression host and construct as:

> E. coli K-12 strain GW2531

> expresses wild-type MetE from pJG816

The Introduction attributes the monoglutamate exclusion to earlier biochemical sources; it is not a newly performed monoglutamate-negative experiment in this paper. The experiments in this paper directly measure binding and methyl transfer with synthesized (6S)-methyltetrahydrofolate triglutamate, including radiolabeled methionine production and the tetrahydrofolate-product assay. The Methods specify a MetE-deficient K-12 host, zinc-supplemented overexpression and purified protein. These experiments support wild-type E. coli MetE chemistry, not an unqualified flux measurement in native MG1655 cells.

Current GO:0003871 specifies the triglutamate methyl donor, whereas GO:0008705 specifies the monoglutamate donor. The substrate evidence therefore warrants a substrate-specific correction of E. coli MetE GO:0008705 to GO:0003871. This conclusion does not rest on a B12 requirement in GO:0008705, whose current definition has none. It does not demonstrate the substrate scope of every plant or bacterial MetE-family member. Structural comparisons in this article include Thermotoga maritima; those structures must not be described as E. coli structures.
