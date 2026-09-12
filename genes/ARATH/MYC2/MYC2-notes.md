# MYC2 re-review, 2026-09-11

Reviewed all 52 annotation rows, including the pre-existing NEW jasmonate-signaling proposal, against cached publications, UniProt and Falcon context. Publication caching recovered 29/29 cited papers; selected incomplete full texts were refreshed through the CLI. New Falcon research with perplexity-lite fallback was launched; its status is recorded below when complete.

Primary evidence supports sequence-specific promoter binding and transcriptional activation [PMID:9368419, "The rd22BP1 protein binds specifically to the first MYC recognition site in the 67-bp fragment."] [PMID:21321051, "MYC2, MYC3, and MYC4 were all capable of inducing expression of JAZ::GUS reporter constructs following transfection of carrot protoplasts."]. Replaced synthetic quotations attributed to research/PANTHER files with checkable primary passages.

Jasmonate response is core, not incidental: JAZ regulation places MYC2 within signaling. The pre-existing NEW pathway row is now supported directly by PMID:17637675 and PMID:21321051, and the pathway is included in core_functions. Tetramerization is also a demonstrated mechanism: "Biochemical assays confirmed that full-length MYC2 forms a stable homo-tetramer both in solution and in DNA-bound states" [PMID:28514654].

MYC2 negatively regulates tryptophan/indole-glucosinolate metabolism and positively regulates flavonoid biosynthesis and insect resistance [PMID:17616737]. The biological-process reviews now preserve these directions and their experimental context instead of treating all outputs as unspecified phenotypes.

The MYC3-focused structural paper also assays MYC2-JAZ9 binding directly in its full text [PMID:26258305, Results, aa 55-259 mapping]. Its title/abstract focus does not justify rejecting MYC2 evidence. Nuclear localization is directly imaged [PMID:27357749, "Venus-MYC2 was targeted only to the nucleus"].

Specific interaction-map rows and an unexposed wound-induced expression measurement remain UNDECIDED pending source tables or full assay text. General promoter-binding and nuclear-location assertions with independent direct evidence remain ACCEPT, with explicit deference to the original curator for unresolved source-specific assays. IEA entries use evidence-appropriate cited rationale without mandatory snippets.

Existing proposed GO replacements and jasmonate-signaling GO:0009867 were verified against the QuickGO ontology service during this session; labels match and none is obsolete.

Targeted cache refresh recovered full text for PMID:17675405 and PMID:25490915. The virus paper explicitly tests MYC2 binding to a TPS10 G-box-like element by EMSA with mutant controls and ChIP, and reports nuclear localization; its three relevant rows now cite that direct source. The wound-study extraction still does not expose the MYC2-specific expression table. PMID:25533953 and PMID:27923776 full-text network articles likewise did not expose the MYC2-specific promoter edge, so their general DNA-binding assertions are retained with independent direct support and curator deference. PMID:25352272 and PMID:30630869 refresh attempts failed to recover full text; the parent reviewer preserved the prior generated caches rather than accepting the degraded refresh.

Research refresh outcome: Falcon timed out after 600 seconds; the automatically attempted perplexity-lite fallback failed with HTTP 401 insufficient_quota. No fresh MYC2 provider report was produced. The pre-existing Falcon report was preserved and the re-review was completed using cached primary literature and targeted full-text retrieval; no manual content was written under a provider-generated filename.
