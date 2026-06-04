# ARL8B notes

## Deep research attempt

`just deep-research-falcon human ARL8B --fallback perplexity-lite` was run on 2026-06-03. Falcon timed out after 600 seconds, and the `perplexity-lite` fallback failed with an API quota/401 error, so no `ARL8B-deep-research-falcon.md` or fallback provider report was produced. I proceeded using the fetched UniProt record, cached GOA-derived PMIDs, cached publication text, and the Proteostasis PN projection reports.

## Proteostasis PN review

Fetched human ARL8B on 2026-06-03 and reviewed it in the Proteostasis PN batch. The PN projection proposes `GO:0061906 autophagosome localization` from the Autophagy-Lysosome Pathway node "HOPS-BORC complex bridging" [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv "ARL8B\t\tGO:0061906\tautophagosome localization\tnew_to_goa"].

I treated that projection conservatively. The direct ARL8B literature strongly supports lysosomal/endolysosomal membrane localization, lysosome positioning, HOPS-linked cargo delivery to lysosomes, and autophagosome-lysosome fusion. It does not clearly show that ARL8B directly localizes autophagosomes as the transported organelle. The strongest autophagy-related ARL8B evidence is that PLEKHM1 connects ARL8B with HOPS at lysosomal contact/fusion sites and that ARL8B binding is needed for lysosomal degradation of autophagic cargo [PMID:28325809 "Arl8b mediates recruitment of HOPS complex to PLEKHM1-positive vesicle contact sites"; PMID:28325809 "Arl8b binding is crucial for PLEKHM1 to promote lysosomal degradation of endocytic and autophagic cargo"].

Core synthesis: ARL8B is best curated as a small GTPase on lysosomal/endolysosomal membranes that recruits effectors for lysosome positioning and cargo-delivery/fusion. BORC recruits ARL8B to lysosomes and enables peripheral lysosome movement [PMID:25898167 "BORC functions to recruit Arl8 to lysosomes"], SKIP/PLEKHM2 links ARL8 to kinesin-1 for plus-end-directed lysosome motility [PMID:22172677 "Arl8 binding to SKIP provides a link from lysosomal membranes to plus-end-directed motility"], and VPS41/HOPS recruitment supports endosome/phagosome/autophagosome delivery to lysosomes [PMID:21802320 "Arl8b was found to bind and recruit the VPS41 subunit of the HOPS"].

The seeded `GO:0007059 chromosome segregation` annotation points to PMID:14871887, which is a Drosophila Topors/Hairy ubiquitin ligase paper and appears unrelated to ARL8B [PMID:14871887 "Drosophila Topors is a RING finger-containing protein"]. The term itself has support from the ARL8B/GIE paper [PMID:15331635 "Gie protein has ability to bind to tubulin and localizes with microtubules on the spindle mid-zone in late mitosis"], so I retained it as non-core and flagged the PMID mismatch in the review.
