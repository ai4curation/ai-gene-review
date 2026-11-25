# PP_0664 curation notes

Q88Q34 has a short-form homoserine dehydrogenase architecture, EC 1.1.1.3, and
UniPathway mappings to threonine and methionine biosynthesis. The record lacks a
specific catalytic-reaction comment or direct KT2440 assay. It is therefore a
valid predicted exemplar but not evidence that it carries the same in-vivo flux
as Q88MU8.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. The existing genuine provider report was read and preserved unchanged; its claims were checked against primary papers and curated features.

The short-form homoserine dehydrogenase inference has independent support: RuleBase family membership, IPR022697 HDH_short, PS01042 and PIRSR-assigned catalytic proton donor 227, NADPH contact 128 and homoserine contact 212. Retain GO:0004412 and the existing predicted threonine role, while stating that native substrate/donor kinetics and contribution relative to PP_1470 remain unmeasured. These are family-based biochemical predictions, not proof that PP_0664 substitutes for canonical Hom in vivo. No ACT domain is reported; this does not prove absence of allosteric regulation.

The inherited OpenScientist report's preferred-NADPH, native feedback and locus-specific auxotrophy claims are unverified. PMID:20158506 abstract reports threonine/methionine auxotrophs without identifying this locus. PMID:29636528 assays the archaeon Sulfolobus tokodaii. PMID:4391829 shows comparative donor variability, not target-specific kinetics. The 2025 KT2440 Hom construct maps to Q88MU8/PP_1470 by terminal primer and size, not PP_0664. Preserve the report unchanged but do not use its confident claims as primary evidence. Broad amino-acid metabolism is refined to the existing predicted threonine role.

The inherited authored GO:0071266 NEW row is archived in full at PP_0664-source-analysis/retired-new-annotations.yaml and retired from the active review. Live QuickGO defines this process as forming methionine from simpler components including aspartate or homoserine; shared precursor enzymes can therefore participate. The issue is insufficient independent support for this particular extra native assertion, not exclusion by definition. Its parents include amino-acid biosynthesis (GO:0008652), sulfur amino-acid biosynthesis and methionine biosynthesis. Existing annotations/cores were checked for overlapping methionine terms. Exact-term QuickGO comparator queries on E. coli ThrA P00561 and MetL P00562 returned zero; this is a convention warning, not proof of false biology. No cached GO-CAM index hit was found for these three targets. Shared methionine precursor biology remains in prose; no replacement NEW ancestor/descendant is proposed. Query responses are preserved in the ignored audit logs.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.

Direct DOI full-text access was attempted for the relevant historical 1970 papers and the 1992 P. aeruginosa paper using the web tool on 2026-11-01; the URLs were inaccessible. No unavailable experimental detail was invented.
