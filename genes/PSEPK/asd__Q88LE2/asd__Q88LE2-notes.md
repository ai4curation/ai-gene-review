# asd PP_1992 curation notes

Q88LE2 is full length, but its UniProt name is submitted and the record lacks a
curated reaction, EC assignment, HAMAP MF_02121 hit, or UniPathway mapping. The
PTHR46278:SF2 subfamily itself is not discriminating because it contains many
reviewed Asd proteins as well as a few USG-1-like entries. The imported specific
MF and pathway BP remain undecided; no core function or module satisfaction is
inferred.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. A normal Falcon attempt returned HTTP 403 Failed to authenticate; no fabricated report was written. Manual literature and curated-source review supplied the fallback.

PP_1992 has IPR000534 semialdehyde-dehydrogenase NAD-binding and IPR012280 dimerization domains. These support a broad aldehyde oxidoreductase core prediction, retained as ACCEPT because it is the current warranted specificity, not relegated to non-core because it is broad. The precise NADP-dependent Asd reaction and amino-acid pathway assignment remain UNDECIDED, as do unphosphorylated NAD binding and native oligomerization.

Absence of the gamma-type HAMAP/TIGR01745 assignment does not establish catalytic loss. PANTHER PTHR46278:SF2 also contains the functional Corynebacterium glutamicum Asd P0C1D8, so this family cannot be used to exclude Asd activity. This remains a plausible substrate-specific candidate requiring native assay/complementation. No generic family label, missing signature or inferred gene name is treated as proof of a distinct physiological role. It must not silently replace canonical PP_1989 in a proven native route.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.
