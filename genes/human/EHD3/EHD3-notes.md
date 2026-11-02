# EHD3 curation notes

## Deep research status
- `just deep-research-falcon human EHD3` was run (unavailable perplexity-lite fallback, then `--timeout 2400`). See the end of this file for the outcome. The review was written from cached primary literature.

## Key findings (with provenance)
- Resides in recycling tubules/vesicles; interacts with EHD1 [PMID:12121420 "EHD3, expressed as a green fluorescent fusion protein was localized to endocytic vesicles and to microtubule-dependent, membrane tubules."]
- Endosome-to-Golgi transport and Golgi morphology [PMID:19139087 "Our findings support a role for EHD3 in regulating endosome-to-Golgi transport"]; Golgi effects are indirect [PMID:19139087 "These data also suggest that impaired endosome-to-Golgi transport and the resulting lack of recruitment of AP-1 gamma-adaptin to Golgi membranes affect Golgi morphology."]
- Recycling [PMID:17233914 "loss of EHD1 and 3 (and to a lesser extent EHD4) but not EHD2 function retarded transferrin exit from the endocytic recycling compartment"]; stabilizes tubular recycling endosomes [PMID:27189942 "EHD1 induces membrane vesiculation, whereas EHD3 supports TRE biogenesis and/or stabilization by an unknown mechanism."]
- Cardiac ankyrin-B-associated membrane protein targeting [PMID:20489164 "We show that EHD1-4 directly associate with ankyrin"]
- Ciliogenesis, partly redundant with EHD1 [PMID:25686250 "Importantly, an siRNA resistant form of GFP-EHD1 or GFP-EHD3 but not GFP, GFP-EHD2 or GFP-EHD4 rescued ciliation"]; [PMID:25686250 "indicating that EHD3 may be dispensable for RPE cell ciliogenesis"]; [PMID:25686250 "Together these results indicate that Ehd1 and Ehd3 have overlapping, albeit tissue specific, functions in ciliogenesis in zebrafish embryos."]
- The 2000 cloning paper (PMID:10673336) only predicts a nucleotide-binding site and an NLS; nucleic acid binding and nucleus TAS rows were REMOVEd.

## Curation decisions (summary)
- GTP binding IEA: MODIFY -> ATP binding (family evidence PMID:15710626). Ciliary membrane IEA: MODIFY -> ciliary pocket membrane.
- Protein binding x16, nucleic acid binding TAS, nucleus TAS: REMOVE.
- Recycling, endosome-to-Golgi, cilium assembly, ciliary pocket, HPA rows, recycling endosome membrane: ACCEPT.
- Cardiac physiology terms, Golgi-to-lysosome transport, regulation of Golgi organization: KEEP_AS_NON_CORE.
- NEW ciliary vesicle assembly (GO:1905556, IMP, PMID:25686250), noting redundancy with EHD1.

## HPA cilium atlas vs module role
- Module: stage 2_ciliary_vesicle, "ciliary vesicle formation", membrane-shaping ATPase with EHD1.
- HPA v25: Primary cilium (S), Primary cilium transition zone (S); main location plasma membrane. GOA HPA rows (cilium, ciliary transition zone, plasma membrane) accepted.
- Assessment: consistent with the module, with a caveat: EHD3's contribution is partly redundant with EHD1 and cell-type dependent (dispensable in RPE1, where EHD1 is >5-fold more abundant). core_functions keep ciliary vesicle assembly but list it alongside the non-ciliary recycling/endosome-to-Golgi and cardiac targeting roles. Unlike EHD1, I did not assert an ATP hydrolysis MF for EHD3 because direct EHD3 ATPase data were not available in the cache.

## Deep research outcome
- Falcon succeeded on retry (`--timeout 2400`): `EHD3-deep-research-falcon.md`. Consistent with the review: EHD3 favors tubulation/stabilization (EHD1 and EHD4 favor vesiculation), early endosome -> ERC and endosome-to-Golgi transport, preciliary membrane/ciliary pocket role with EHD1, cardiac NCX1/CaV1.2/CaV3 targeting via ankyrin-B, glomerular endothelial VEGFR2 trafficking (with EHD4 compensation). It flags that no EHD3-specific ATP-hydrolysis data were retrieved, supporting the decision not to assert an ATPase MF for EHD3 in core_functions.
