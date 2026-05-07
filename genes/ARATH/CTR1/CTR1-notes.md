# CTR1 review notes

Deep research provider status, 2026-05-06: Falcon timed out on CTR1 after 600 seconds and a longer retry stalled; the batch Falcon run was stopped before repeating the same failure for the other genes. Perplexity returned 401 insufficient_quota, and OpenAI timed out on CTR1 after 300 seconds. I therefore performed this review manually from the fetched UniProt record, cached publication records, and PANTHER family context.

QuickGO annotation/search returned HTTP 500 for this accession on 2026-05-06, including with a `UniProtKB:` prefix. The GOA TSV in this branch was populated from UniProtKB REST GO cross-references so the existing-annotation validator has PMID/GO_REF provenance rather than treating known annotations as new.

Core interpretation: CTR1 is a Raf-like serine/threonine protein kinase and negative regulator of ethylene signaling. It is associated with the ER-localized ethylene receptor complex and phosphorylates EIN2, preventing downstream ethylene signaling when ethylene is absent [PMID:8431946; PMID:23132950]. Sugar, hypoxia, root, stem cell, floral transition, and gibberellin phenotypes are downstream or cross-talk outputs rather than the core molecular role.

Falcon retry status, 2026-05-07: Falcon deep research completed in `CTR1-deep-research-falcon.md`. The report supports the existing review conclusion that CTR1's core function is ER-associated Raf-like Ser/Thr kinase control of ethylene signaling through EIN2 phosphorylation, while newer nuclear-trafficking/autophagy context remains non-core for this review.
