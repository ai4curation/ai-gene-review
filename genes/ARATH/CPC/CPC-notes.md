# CPC (CAPRICE; At2g46410; UniProt O22059) curation notes

## Identity
- O22059 CPC_ARATH, 94 aa single-repeat R3 MYB, locus AT2G46410.

## Key findings (with provenance)
- Cloning: Myb-like domain; cpc has few root hairs; CPC overexpression gives more root hairs and fewer trichomes [PMID:9262483 "Transgenic plants overexpressing CPC had more root hairs and fewer trichomes than normal."]
- CPC is expressed in non-hair cells, moves to hair-forming cells and represses GL2 [PMID:12403712 "CPC protein moves to the hair-forming cells and represses the GL2 expression"]; movement via plasmodesmata, nuclear accumulation [PMID:16291794].
- GL3/EGL3 bind CPC; CPC blocks the non-hair pathway in H cells [PMID:14627722]; WER and CPC compete [PMID:21914815]; CPC prevents GL3-WER/EGL3-WER interaction in yeast [PMID:17644729].
- Trichomes: TRY and CPC act together in lateral inhibition [PMID:12356720]; CPC competes with GL3 homolog R in overexpression rescue [PMID:12356720]; CPC and TRY move between leaf epidermal cells [PMID:18766177].
- Stomata: CPC promotes hypocotyl stomata with TRY [PMID:19513241].
- Mutual support model of CPC/GL3 movement in root [PMID:18816165].

## Curation decisions
- GO:0003700 ISS x2 -> MODIFY GO:0140416 transcription regulator inhibitor activity.
- GO:0005515 IPI with EGL3 x3 -> MODIFY GO:0140416 (the binding is the inhibitory mechanism).
- GO:0000976 IBA -> MARK_AS_OVER_ANNOTATED (deep MYB node; CPC lacks R2, DNA binding not shown).
- cell differentiation (IBA/TAS) -> MODIFY to plant epidermal cell differentiation.
- NEW: GO:1900032 regulation of trichome patterning (IMP, PMID:12356720); comparator TRY carries this term by IMP in GOA.
- Falcon deep research generated (CPC-deep-research-falcon.md).

## 2026-10-06 PR #4395 review follow-up
- PMID:15361138 protein-binding row: supporting_text now quotes the abstract's statement that the conserved R3 signature is "the structural basis for interaction between MYB and R/B-like BHLH proteins" (was a motif tally naming no protein). Cache is abstract-only; per-pair data deferred to the curator.
