# Casp3 review notes

## 2026-09-05 — SFT binding assessment and annotation suitability

The GO:0005123 SFT prediction is UNC, rather than automatically NPI or CNN. The current review marks death receptor binding over-annotated because DISC association does not establish direct receptor contact. The accessible rat spinal-cord-injury abstract describes Fas association with FADD, caspase-8, cFLIP and caspase-3 in a DISC [PMID:17518537, “forming a death-inducing signaling complex (DISC)”]. This supports complex association but does not resolve the direct-contact question. PubMed and the publisher landing page were checked; the latter lists restricted full-text access, and the cached record has `full_text_available: false`. Failure to verify the full experiment cannot justify declaring the binding prediction refuted. The main gene review and experimental GOA annotation are unchanged.

The supported SFT wrapper now records an explicit gene/term exception for `MARK_AS_OVER_ANNOTATED` with a source-based UNC rationale. A different rejection action or accepted negation does not inherit this exception. This follows the PredictionAssessmentEnum uncertainty definition; it is not an assertion that direct binding is absent.
