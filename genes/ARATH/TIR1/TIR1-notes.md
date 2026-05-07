# TIR1 review notes

Deep research provider status, 2026-05-06: Falcon timed out on CTR1 and the batch run was stopped before repeated timeouts; Perplexity returned 401 insufficient_quota; OpenAI timed out on CTR1. I reviewed TIR1 manually from UniProt, cached publications, and PANTHER family context.

QuickGO annotation/search returned HTTP 500 for this accession on 2026-05-06, including with a `UniProtKB:` prefix. The GOA TSV in this branch was populated from UniProtKB REST GO cross-references so the existing-annotation validator has PMID/GO_REF provenance rather than treating known annotations as new.

Core interpretation: TIR1 is the F-box auxin receptor and substrate-recognition subunit of SCF(TIR1). Auxin binds the TIR1 pocket, promotes Aux/IAA substrate recruitment, and drives Aux/IAA degradation and auxin-regulated transcription [PMID:10398681; PMID:11713520; PMID:15917797; PMID:15917798; PMID:17410169]. Lateral root, stamen, and phosphate starvation phenotypes are retained as non-core outputs.

Falcon retry status, 2026-05-07: Falcon deep research completed in `TIR1-deep-research-falcon.md`. The report supports the existing review conclusion that TIR1 is the F-box/LRR auxin receptor and SCF substrate adaptor that recruits Aux/IAA repressors for degradation.
