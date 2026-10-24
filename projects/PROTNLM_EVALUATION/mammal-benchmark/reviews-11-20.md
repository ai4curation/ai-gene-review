# Horse benchmark review: pairs 11–20

All ten selected horse targets have a paired human review, a human research file, an exact-sequence comparison, and claim-level ProtNLM assessment. Unresolved experimental-source details and consequential target-sequence gaps remain explicit uncertainties.

| Pair | Human GOA rows reviewed | Horse GOA rows reviewed | Human research | ProtNLM output |
|---|---:|---:|---|---|
| CXCR3 (A0A9L0T1D1) | 53 | 12 | Primary-source manual investigation (external service unavailable) | 0 GO; 1 function paragraph |
| DARS2 (A0A9L0SB67) | 54 | 7 | Edison | 0 GO; 1 function paragraph |
| GPAM (A0A9L0TTC1) | 28 | 9 | Edison | 0 GO; 1 function paragraph |
| HSPA4 (A0A9L0S5Z5) | 27 | 3 | Primary-source manual investigation (external service unavailable) | 0 GO; 1 function paragraph |
| DUOX1 (A0A9L0SQG9) | 75 | 7 | Primary-source manual investigation (external service unavailable) | 4 GO; 1 function paragraph |
| MTMR9 (A0A9L0T3C1) | 76 | 5 | Edison | 7 GO; 0 function paragraph |
| PTPRN2 (A0A9L0T4W6) | 21 | 6 | Edison | 1 GO; 0 function paragraph |
| DNMT3L (A0A9L0T837) | 40 | 19 | Primary-source manual investigation (external service unavailable) | 2 GO; 0 function paragraph |
| IRAK3 (A0A3Q2HDT6) | 75 | 2 | Primary-source manual investigation (external service unavailable) | 0 GO; 1 function paragraph |
| PPP4R4 (A0A9L0S961) | 14 | 1 | Primary-source manual investigation (external service unavailable) | 3 GO; 0 function paragraph |

## Main findings

- CXCR3: the named CCL3/CCL4/CCL5 ligand set conflicts with directly inspected receptor experiments; broad chemokine signaling remains supported. General C-C receptor GOA assertions need separate source/phylogeny tracing.
- DARS2: tRNA(Asp) activity is supported; tRNA(Asn) acceptance remains unresolved rather than being rejected from a bacterial-function stereotype. Human membrane association is verified in the fractionation paper.
- GPAM: the acyl donor is acyl-CoA, not acyl-ACP. The human structural paper supports amphipathic outer-membrane association and contradicts the older two-transmembrane model repeated by the external report.
- HSPA4: Hsp110/Apg2 nucleotide-exchange biology is distinct from Mpp11/Hsp70L1 RAC membership.
- DUOX1: peroxide generation is distinct from peroxide catabolism; the selected horse model loses major EF-hand elements, so calcium binding and regulated output require target-specific resolution.
- MTMR9: regulatory activity is not refuted by catalytic inactivity. Exact protein-phosphatase partner classification and transfer of stabilization/autophagy phenotypes need follow-up.
- PTPRN2: protein-phosphatase and phosphoinositide-phosphatase claims must be separated; a biological-process dephosphorylation claim cannot be rejected solely from loss of intrinsic protein catalysis.
- DNMT3L: the supported predictions describe noncatalytic nuclear gene regulation.
- IRAK3: positive reconstitution and negative physiological feedback are distinct contexts; the shortened horse N terminus complicates receptor-complex transfer.
- PPP4R4: stable PP4 complex membership and regulation are supported; blastocyst hatching remains unverified.

## Validation and remaining work

All twenty gene files passed schema, source-excerpt and GOA validation. Prediction sidecars passed schema and excerpt validation. Advisory warnings concern unresolved propagation evidence, unavailable source details, and intentionally omitted exact-sequence core activities where major deletions prevent a secure assertion. Every curated gene target has a scaffolded, validated append-only history record.

The horse CXCR3 expression paper (PMID:31256888) justified a horse-specific Edison request. Other horse database references are genome sequencing/submission; broad omics hits were not counted as functional validation. Some external requests failed with Edison HTTP429 or Perplexity insufficient-quota HTTP401. Manual files are explicitly named `-deep-research-manual.md`; external reports are preserved unmodified.

Horse CXCR3 Edison completed and is preserved with its artifact. Its horse expression and chemokine-system source leads do not replace direct receptor-specific ligand validation.
