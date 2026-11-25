# RELA review notes

## GO-CAM context

Model `5fce9b7300000030`, "Diacyl lipopeptide and bacteriocin activation of TLR6_TLR2 receptor (Human)", names RELA (`UniProtKB:Q04206`) as the downstream DNA-binding transcription factor activity in the TLR6:TLR2 signaling pathway. The cached model uses `PMID:3091258` as the enabled_by evidence for the RELA node; that paper describes the original NF-kappaB activity as nuclear factors bound to immunoglobulin enhancer sequences before RELA/p65 had been cloned, so it supports the NF-kappaB activity generally but not the RELA gene product specifically. The 1992 recombinant-p65 DNA-binding paper is the better RELA-specific activity support: "Using purified recombinant p50, p65, and c-Rel proteins, optimal DNA-binding motifs were selected from a pool of random oligonucleotides" [PMID:1406630].

The GO-CAM's TLR2/TLR6-to-RELA connection is a defensible pathway synthesis, but the lactic-acid-bacteria paper used by the model measures NF-kappaB/AP-1 reporter output rather than RELA biochemistry. The GOA `GO:0038124` row is therefore accepted as a pathway synthesis supported jointly by TLR2/TLR6 reporter activation and the primary p65/NF-kappaB papers instead of treating `PMID:27708357` as direct RELA evidence.

## Automated research

`just deep-research-falcon human RELA --fallback perplexity-lite` was attempted on 2026-11-25. Both provider attempts failed before producing a research artifact because the environment only exposed `claude_code`; no `RELA-deep-research-falcon.md` or `RELA-deep-research-perplexity-lite.md` file was created or filled manually.

## QuickGO seed

The first `just fetch-gene human RELA` call on 2026-11-25 created a header-only `RELA-goa.tsv` even though the fetched UniProt record listed curated GO cross-references for RELA, including `GO:0000981`, `GO:0035525`, `GO:0005634`, and `GO:0038124`. Re-querying QuickGO immediately afterward returned 454 rows for `Q04206`, so the header-only response was treated as a transient empty QuickGO page rather than as evidence that RELA had no GOA annotations. `just fetch-gene human RELA --force` then fetched all 454 rows and seeded the 447 projected GOA annotations reviewed here.
