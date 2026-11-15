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


## 2026-11-07 evidence re-audit

All original annotation payloads and row order are preserved. No NEW annotation was added. The catalytic reaction and proline-biosynthetic participation remain supported. Direct E. coli primary studies and newer experiments are distinguished from inferred KT2440 function.

The normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Manual source review used the protected existing caches and normally fetched new publications.

PMID:39514317 (full text) challenges required ProA–ProB channeling: heterologous kinase replacements and overexpressed alternative reductases support E. coli growth; failed crosslinking alone is not universal proof of no interaction. ProA is reduced glutamyl-phosphate chemistry; spontaneous GSA cyclization supplies P5C. The computed GP half-life and diffusion times are calculations, not intracellular measurements. Native-locus monomeric-GFP fusions show dispersed cytoplasmic localization. Expression/purification used engineered BL21 derivatives, while growth experiments used K-12 BW25113 derivatives. No matched-protein complex requirement is imposed.

NADP binding includes both NADP+ and NADPH under the verified current GO definition and directly supports ProA catalysis; it is not peripheral simply because the catalytic term is more informative.

PAINT loss checks reported no IRD/IKR on the target lineage. Existing abstract-only primary caches were not refreshed. Curated experimental annotations remain supported where independent evidence agrees; no target-table detail was invented. Complete validation, ontology snapshots and preservation proof are in the member-review audit and ignored existing-review logs.
