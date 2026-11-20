# thrC curation notes

Q88MU7 is the canonical terminal enzyme: the current record contains EC
4.2.3.1, RHEA:10840, PLP cofactor evidence, UniPathway UPA00050/UER00065, and
GO:0004795. These convergent predictions are substantially stronger than the
submitted-name/family evidence for PP_0662. No direct KT2440 biochemical paper
was identified in the local record.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. The existing genuine provider report was read and preserved unchanged; its claims were checked against primary papers and curated features.

Specific TIGR00260 threonine-synthase classification and PIRSR604450-51 PLP-linked Lys112 support the catalytic assignment. PLP binding is integral to catalysis and retained as ACCEPT, not non-core. Broad amino-acid metabolism is refined to threonine biosynthesis. The ARBA-only reaction/keyword is not used as decisive evidence when independent classification and catalytic-feature evidence exist.

PMID:40236303 states “the remaining genes of the metabolic pathway – thrB and thrC – were overexpressed as well.” Supplement primers match MRYISTR and HGNRGKPL at the termini of Q88MU7, not PP_0662/Q88Q36. This identifies the native clone in combined engineering with heterologous E. coli ThrA; it does not measure individual ThrC kinetics or imply that the alternative paralog is inactive.

The existing Asta retrieval report contains unrelated papers and contributes no usable target-specific biological evidence. It remains byte-for-byte unchanged, is explicitly assessed as unverified/low relevance, and supplies no supporting quotations.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.
