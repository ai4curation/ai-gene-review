# COI1 review notes

Deep research provider status, 2026-05-06: Falcon timed out on CTR1 and the batch run was stopped before repeated timeouts; Perplexity returned 401 insufficient_quota; OpenAI timed out on CTR1. I reviewed COI1 manually from UniProt, cached publications, and PANTHER family context.

QuickGO annotation/search returned HTTP 500 for this accession on 2026-05-06, including with a `UniProtKB:` prefix. The GOA TSV in this branch was populated from UniProtKB REST GO cross-references so the existing-annotation validator has PMID/GO_REF provenance rather than treating known annotations as new.

Core interpretation: COI1 is the F-box substrate-recognition and hormone co-receptor subunit of SCF(COI1). It links jasmonate perception to JAZ repressor degradation and JA-dependent defense, fertility, and growth responses [PMID:9582125; PMID:12172031; PMID:17637675; PMID:17637677; PMID:20927106]. Developmental, defense, shade, wound, stomatal, and extracellular ATP annotations are retained as non-core downstream outputs unless they describe the SCF/JAZ degradation mechanism.

Falcon retry status, 2026-05-07: Falcon deep research completed in `COI1-deep-research-falcon.md`. The report supports the existing review conclusion that COI1 is the F-box/LRR SCF substrate adaptor and jasmonate co-receptor that promotes JAZ repressor degradation.
