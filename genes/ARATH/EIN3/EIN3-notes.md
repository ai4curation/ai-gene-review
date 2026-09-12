# EIN3 review notes

Deep research provider status, 2026-05-06: Falcon timed out on CTR1 and the batch run was stopped before repeated timeouts; Perplexity returned 401 insufficient_quota; OpenAI timed out on CTR1. I reviewed EIN3 manually from UniProt, cached publications, and PANTHER family context.

QuickGO annotation/search returned HTTP 500 for this accession on 2026-05-06, including with a `UniProtKB:` prefix. The GOA TSV in this branch was populated from UniProtKB REST GO cross-references so the existing-annotation validator has PMID/GO_REF provenance rather than treating known annotations as new.

Core interpretation: EIN3 is a nuclear ethylene-pathway transcription factor. It binds ethylene-response cis-regulatory elements and activates ERF1 and other ethylene-responsive transcriptional programs [PMID:9215635; PMID:9851977; PMID:26352699]. EIN3 also participates in ethylene-dependent chromatin/histone acetylation through ENAP1/EIN2-related signaling [PMID:27694846; PMID:28874528]. Defense, hypoxia, sugar, ascorbate, and kinase-binding annotations are contextual outputs or regulation rather than the central evolved function.

Falcon retry status, 2026-05-07: Falcon deep research completed in `EIN3-deep-research-falcon.md`. The report supports the existing review conclusion that EIN3 is a nuclear ethylene-response DNA-binding transcription factor, with defense, stress, chromatin, and regulatory effects treated as contextual outputs or inputs.

## 2026-09-12 — full annotation and evidence re-review

Reviewed all 17 annotation rows, the 15 original PMID caches, the UniProt record
and existing Falcon synthesis. Publication caching completed 15/15 without forcing
any refresh. Launched Falcon with perplexity-lite fallback concurrently; the
actual outcome is appended below. No generic protein-binding row is present.

The core remains nuclear sequence-specific transcriptional regulation. Added exact
primary-source snippets for promoter binding, EBF2 feedback, WDL5 targeting,
SnRK1 regulation, SID2-dependent defense and the EIN3-ABI4-VTC2 ascorbate pathway.
For example, PMID:18466304 states that “EIN3 can bind and activate the EBF2
promoter”; PMID:30723177 states “ABI4 is transcriptionally repressed by EIN3”.
Retaining a broad response-to-ethylene term as ACCEPT recognizes that breadth
alone does not make the gene's defining hormone response non-core.

**Chromatin and histone decisions.** Retrieved the full PMC5617289 article through
`https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5617289/?report=xml` (the ordinary
browser URL returned a challenge page). The Results examine EIN3 ChIP-seq signal
at ENAP1-targeted regions. Chromatin occupancy is integral to transcriptional
control and is now ACCEPT. The histone association experiments principally
concern EIN2-C and ENAP1, and the EIN3-histone molecular interaction underlying
the original IDA annotation remains unresolved: MARK_AS_OVER_ANNOTATED becomes
UNDECIDED. This is not a claim that the curator assayed the wrong gene or that
EIN3 cannot bind histones.

A targeted search found the primary follow-up [PMID:33793786, *EIN2-directed
histone acetylation requires EIN3-mediated positive feedback regulation in response
to ethylene*](https://pubmed.ncbi.nlm.nih.gov/33793786/). Resolved its identifier and
DOI 10.1093/plcell/koaa029 through Europe PMC, then fetched the record with the
repository CLI. Its abstract states: “it is required for the ethylene-induced
elevation of H3K14Ac and H3K23Ac in the presence of EIN2.” The study establishes
EIN3 positive feedback as part of the core chromatin mechanism, so epigenetic
regulation becomes ACCEPT and enters core functions. This does not assign an
intrinsic histone acetyltransferase activity to EIN3. The newer result also avoids
overgeneralizing the earlier PMID:27694846 statement about EIN3-independent
histone-acetylation upregulation.

**Hypoxia source conflict.** Read the full cached Results and Fig.6 context of
PMID:25284079. It explicitly states: “the ein3-1 mutant was not significantly
different to wild type under either DS or LS”. It suggests EIL1 redundancy, and
the OE-1/ein3 combination does not suppress hypersensitivity. The Discussion
nevertheless groups ein3-1 among mutants with altered hypoxic tolerance. This
internal mismatch is documented as UNDECIDED. The earlier review's ceramide
study PMID:25822663 remains useful context but is not substituted for the
original source's actual phenotype.

Sugar signaling remains UNDECIDED because the original review abstract does not
resolve the EIN3-specific assertion. No artificial snippet was added to resolve
this gap. QuickGO definitions checked: GO:0000976 and GO:0042393. Source fields
(term, evidence code, original reference and flags) are preserved exactly.

Validation: `just validate ARATH EIN3` passes. The sole advisory warning is
that no annotation cites the generated research report; original and independently
verified primary papers provide the actual support. History validation and
`git diff --check` pass. Source annotation fields match the before-review snapshot
exactly.

Research refresh outcome: Falcon timed out after 600 seconds. The configured
perplexity-lite fallback failed with HTTP 401 `insufficient_quota`. The existing
Falcon report is retained unchanged; no new report was fabricated. This re-review
was completed from the existing synthesis, cached and retrieved primary sources,
and the independently identified/fetched PMID:33793786 study.


## 2026-09-12: Incorporation of completed OpenScientist hypotheses (PR2996)

Read both independent OpenScientist reports under EIN3-hypotheses/function-hypothesis-go-0001666 and function-hypothesis-go-0042393. Reports describe public literature/database checks and do not report using held-out local analyses. No new research job was run. Added both reports as provenance references, while adjudicating their recommendations against primary evidence.

Histone binding: MODIFY to GO:0003682 chromatin binding. Rechecked PMID:28874528 full Results/Fig.7 via the NCBI PMC5617289 report endpoint (full article previously retrieved to /tmp/PMC5617289.txt). EIN3 ChIP occupancy is enriched at ENAP1-bound accessible loci. The cached abstract explicitly states “more EIN3 proteins bind to the loci where ENAP1 is enriched for a quick response.” PMID:27694846 full Results assigns the histone pull-down to ENAP1, while EIN3 interacts with ENAP1. This supports chromatin association without adjudicating direct EIN3-histone contact. Neither a missing reader-domain annotation nor failure to find an assay proves binding absent. Keep the later PMID:33793786 EIN3-dependent acetylation feedback evidence and epigenetic core function. QuickGO definitions for GO:0003682, GO:0042393 and GO:0001666 verified by API in this session.

Hypoxia: KEEP_AS_NON_CORE on combined evidence, preserving the original PMID:25284079 source. Re-read its Results, Fig.6 legend and Discussion: “the ein3-1 mutant was not significantly different to wild type under either DS or LS”; four-week plants underwent two-day dark or eight-day light submergence and three-day recovery. This remains inconclusive source-specific evidence, not refutation. Normal publication fetch of the report lead PMID:31488841 successfully cached full PMC6728379. Its Results reports abolition of preadaptation in ethylene-signaling mutants; Methods lists ein3eil1-1; Fig.5 states “Ethylene perception leads to EIN2 and EIN3EIL1 dependent signalling”. This supports the broad biological-process assignment through upstream ethylene signaling, even though it does not establish direct oxygen sensing. Supplementary Fig.1 genotype-resolved data were not independently inspected: PMC file endpoint returned HTML challenge/404 and publisher CDN failed DNS resolution. Do not invent individual mutant effect sizes or partition EIN3/EIL1 contributions. Report recommendations to delete the source annotation as refuted or to discount indirect BP participation were not adopted. No new direct PGB1-binding claim.

Original annotation rows, source identifiers, evidence codes and flags preserved. Report files and existing derived caches were not manually edited.
