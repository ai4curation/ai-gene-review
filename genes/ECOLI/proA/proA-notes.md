# proA review notes

## Deep research

Attempted `just deep-research ECOLI proA --provider perplexity-lite`; the local
environment had no configured deep-research provider/API key, so no
`proA-deep-research-*.md` file was generated.

## Functional synthesis

ProA/P07004 is E. coli gamma-glutamyl phosphate reductase, the second enzyme of
the glutamate-to-P5C branch of L-proline biosynthesis. Purified
glutamate-semialdehyde dehydrogenase catalyzes reduction of gamma-glutamyl
phosphate to glutamate 5-semialdehyde in the proline-biosynthetic pathway
[PMID:7035170]. Stoichiometry and kinetic work established the reversible
glutamate 5-semialdehyde/gamma-glutamyl phosphate reaction using the
NADP+/NADPH redox pair [PMID:7034716; PMID:6337636], and early genetics mapped
`proA` mutants to the pathway segment from glutamyl gamma-phosphate to glutamic
gamma-semialdehyde [PMID:791096].

The high-throughput `GO:0005515 protein binding` rows for SfsA, BtsR, and CysA
come from AP-MS and Y2H interactome screens [PMID:15690043; PMID:19402753;
PMID:24561554]. They may report real physical contacts, but they do not define
a specific ProA molecular function beyond the core
glutamate-5-semialdehyde dehydrogenase activity.

Two independent proteomic studies support ProA's soluble cytosolic localization
[PMID:15911532; PMID:18304323]. Homomeric assembly is also supported by the
purified enzyme's reported oligomeric state [PMID:7035170], but this is a
structural feature of the catalytic enzyme rather than a separate core function.

ProA and ProB may interact functionally to pass the unstable L-glutamyl
5-phosphate intermediate from glutamate 5-kinase to gamma-glutamyl phosphate
reductase. ProB kinase activity was detectable only in coupled assays
containing purified ProA [PMID:6319365], and E. coli ProB structures place
exposed kinase active centers in a geometry proposed to support G5P channeling
to the ProA active centers [PMID:17321544]. Stable physiological complex
formation has not yet been established strongly enough to add a new complex
annotation.
