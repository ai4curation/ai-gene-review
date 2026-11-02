# thrB curation notes

Q88RK8 has a HAMAP-supported EC 2.7.1.39 reaction, RHEA:13985, UniPathway
step 4/5, and the Pseudomonas-type ThrB family assignment. It is the first
threonine-specific enzyme in the chosen boundary; the preceding Hom reaction is
also used for methionine biosynthesis.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. The existing genuine provider report was read and preserved unchanged; its claims were checked against primary papers and curated features.

The Pseudomonas-type homoserine kinase inference is supported by HAMAP MF_00301, TIGR00938, IPR005280 and IPR050249. Its aminoglycoside-phosphotransferase-like fold and PANTHER name do not make it an antibiotic kinase. The curated reaction is “Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)”. GO:0019202 is correct but general and is refined to existing GO:0004413.

PMID:40236303 overexpressed native thrB/thrC with heterologous E. coli ThrA; the single-plasmid combination increased threonine. Supplement primers match the N-terminal MSVFTPVT and C-terminal LHLPFAL of Q88RK8. This strengthens native target identity and pathway participation but does not resolve separate enzyme kinetics or essentiality.

PMID:1333566 explicitly concerns Pseudomonas aeruginosa: “Three genes from Pseudomonas aeruginosa involved in threonine biosynthesis”. Its thrB insertion result and proposed isozymes are comparative; they do not demonstrate native KT2440 ThrB/ThrH redundancy. The inherited report is retained as a lead, not as native bypass evidence.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.

Direct DOI full-text access was attempted for the relevant historical 1970 papers and the 1992 P. aeruginosa paper using the web tool on 2026-11-01; the URLs were inaccessible. No unavailable experimental detail was invented.
