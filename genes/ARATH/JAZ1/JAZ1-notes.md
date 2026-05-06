# JAZ1 review notes

Deep research provider status, 2026-05-06: Falcon timed out on CTR1 and the batch run was stopped before repeated timeouts; Perplexity returned 401 insufficient_quota; OpenAI timed out on CTR1. I reviewed JAZ1 manually from UniProt, cached publications, and PANTHER family context.

QuickGO annotation/search returned HTTP 500 for this accession on 2026-05-06, including with a `UniProtKB:` prefix. The GOA TSV in this branch was populated from UniProtKB REST GO cross-references so the existing-annotation validator has PMID/GO_REF provenance rather than treating known annotations as new.

Core interpretation: JAZ1/TIFY10A is a nuclear JAZ repressor in jasmonate signaling. JA-Ile promotes COI1-JAZ1 interaction and JAZ1 degradation; in the unelicited state, JAZ proteins repress MYC transcription factors and recruit the NINJA/TOPLESS corepressor module [PMID:17637675; PMID:17637677; PMID:19151223; PMID:20360743]. Developmental and defense phenotypes are downstream consequences of JA signaling control.
