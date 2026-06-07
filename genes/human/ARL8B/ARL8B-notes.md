# ARL8B notes

## Deep research attempt

`just deep-research-falcon human ARL8B --fallback perplexity-lite` was run on 2026-06-03. Falcon timed out after 600 seconds, and the `perplexity-lite` fallback failed with an API quota/401 error, so no `ARL8B-deep-research-falcon.md` or fallback provider report was produced. I proceeded using the fetched UniProt record, cached GOA-derived PMIDs, cached publication text, and the Proteostasis PN projection reports.

## Proteostasis PN review

Fetched human ARL8B on 2026-06-03 and reviewed it in the Proteostasis PN batch. The PN projection proposes `GO:0061906 autophagosome localization` from the Autophagy-Lysosome Pathway node "HOPS-BORC complex bridging" [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv "ARL8B\t\tGO:0061906\tautophagosome localization\tnew_to_goa"].

I treated that projection conservatively. The direct ARL8B literature strongly supports lysosomal/endolysosomal membrane localization, lysosome positioning, HOPS-linked cargo delivery to lysosomes, and autophagosome-lysosome fusion. It does not clearly show that ARL8B directly localizes autophagosomes as the transported organelle. The strongest autophagy-related ARL8B evidence is that PLEKHM1 connects ARL8B with HOPS at lysosomal contact/fusion sites and that ARL8B binding is needed for lysosomal degradation of autophagic cargo [PMID:28325809 "Arl8b mediates recruitment of HOPS complex to PLEKHM1-positive vesicle contact sites"; PMID:28325809 "Arl8b binding is crucial for PLEKHM1 to promote lysosomal degradation of endocytic and autophagic cargo"].

Core synthesis: ARL8B is best curated as a small GTPase on lysosomal/endolysosomal membranes that recruits effectors for lysosome positioning and cargo-delivery/fusion. BORC recruits ARL8B to lysosomes and enables peripheral lysosome movement [PMID:25898167 "BORC functions to recruit Arl8 to lysosomes"], SKIP/PLEKHM2 links ARL8 to kinesin-1 for plus-end-directed lysosome motility [PMID:22172677 "Arl8 binding to SKIP provides a link from lysosomal membranes to plus-end-directed motility"], and VPS41/HOPS recruitment supports endosome/phagosome/autophagosome delivery to lysosomes [PMID:21802320 "Arl8b was found to bind and recruit the VPS41 subunit of the HOPS"].

The seeded `GO:0007059 chromosome segregation` annotation points to PMID:14871887, which is a Drosophila Topors/Hairy ubiquitin ligase paper and appears unrelated to ARL8B [PMID:14871887 "Drosophila Topors is a RING finger-containing protein"]. The term itself has support from the ARL8B/GIE paper [PMID:15331635 "Gie protein has ability to bind to tubulin and localizes with microtubules on the spindle mid-zone in late mitosis"], so I retained it as non-core and flagged the PMID mismatch in the review.

## Falcon deep research findings (2026-06-07)

The Falcon report (Edison Scientific) was successfully generated (the earlier 2026-06-03 attempt had timed out). Most content CONFIRMS the existing review; one finding is genuinely NEW vs the existing annotations. Provenance below; PMIDs resolved via PubMed ID converter from DOIs.

- NEW (primary, directly ARL8B-relevant): DENND6A is a direct ARL8B effector that drives the *retrograde* arm of lysosome transport via a DENND6A→Rab34→RILP/dynein cascade, with nutrient-dependent juxtanuclear repositioning, and DENND6A loss impairs autophagic flux [PMID:38296963 (Kumar et al. 2024, Nat Commun) "Arl8b recruits DENND6A to peripheral lysosomes to activate Rab34 and initiate retrograde transport"; DOI:10.1038/s41467-024-44957-1]. This is distinct from the RUFY3/RUFY4 dynein-dynactin retrograde coupling already in the review (PMID:35314674); it adds a second, GEF-cascade-based retrograde mechanism downstream of ARL8B. Conceptually positions ARL8B as a bidirectional transport coordinator (kinesin via SKIP; dynein via DENND6A/Rab34/RILP and via RUFY3/4). I added PMID:38296963 to references.

- NEW (human disease, upstream of ARL8B, not an ARL8B coding mutation): biallelic BORCS8 (BORC subunit) variants cause an infantile-onset neurodegenerative disorder with altered lysosome dynamics; loss-of-function alleles reduce BORC assembly and peripheral lysosome distribution [PMID:38128568 (De Pace et al. 2024, Brain) "BORC associates with the cytosolic face of lysosomes, where it sequentially recruits the small GTPase ARL8 and kinesin-1 and -3 microtubule motors"; DOI:10.1093/brain/awad427]. Direct human evidence that perturbing the upstream ARL8B recruiter is clinically severe; underscores physiological importance of the BORC→ARL8B axis. Added as a reference (statement-only). Did NOT use to change any ARL8B annotation since it concerns BORCS8, not ARL8B itself.

- CONFIRMS: anterograde axis BORC→ARL8B-GTP→SKIP/PLEKHM2→kinesin-1 (KIF5B/KLC); SKIP WD motifs (W207A/D208A/W236A/E237A) required for KIF5B recruitment; KIF5B knockdown >85% phenocopies ARL8/SKIP depletion [Rosa-Ferreira & Munro 2011, DOI:10.1016/j.devcel.2011.10.007]. Already captured via PMID:22172677 and lysosome-localization annotations.

- CONFIRMS: HOPS/VPS41 tethering for endosome-lysosome fusion and EGFR degradation; ARL8B (not Rab7) required for hVps41 lysosomal localization [Khatter et al. 2015 J Cell Sci, DOI:10.1242/jcs.162651]. Already captured via PMID:21802320/PMID:28325809.

- CONFIRMS / context: PLEKHM1 (RUN domain) competes with SKIP for ARL8B, balancing positioning vs fusion; ARL8A/ARL8B ~91% identical [Marwaha et al. 2017, DOI:10.1083/jcb.201607085]. Already captured (PMID:28325809). The ~91% paralog identity supports careful attribution: SKIP/kinesin, HOPS/VPS41, BORC, RUFY, and DENND6A studies are largely on ARL8B specifically.

- PROVISIONAL / low-confidence (NOT used to change annotations): two preprint versions of the DENND6A work (bioRxiv 2023.08.21.554162; Research Square rs.3.rs-3283181/v1) predate the published PMID:38296963 and are superseded by it. OpenTargets disease associations (e.g., "neoplasm") are heterogeneous association-level evidence only. The report's structural claims (N-terminal amphipathic helix; PDB 1ZD9) are review-level context, not new primary data; not added.
