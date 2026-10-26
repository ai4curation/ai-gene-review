# ABCB19 (MDR1/MDR11/PGP19; At3g28860; UniProt Q9LJX0) notes

Deep research: falcon failed (Edison API 429, 2026-10-05).

## Auxin export
- atmdr1 impaired auxin transport, NPA binding [PMID:11701880 "Auxin transport activity was greatly impaired in atmdr1 and atmdr1 atpgp1 double mutant plants."].
- Root acropetal transport reduced 80% [PMID:17557805 "Mutations in Multidrug Resistance-Like1 (MDR1) reduced acropetal auxin transport in roots by 80% without affecting basipetal transport."]. (MDR1 = ABCB19, MDR4 = ABCB4.)
- phot1 phosphorylation inhibits efflux [PMID:21666806 "phosphorylation of ABCB19 by phot1 inhibits its efflux activity"].
- PIN1 interaction/coordination [PMID:17237354 "Specific PGP-PIN interactions were seen in yeast two-hybrid and coimmunoprecipitation assays."]; stabilizes PIN1 in DRMs [PMID:18774968].

## Brassinosteroid export
- [PMID:38513023 "Bioactive brassinosteroids are potent activators of ABCB19 ATP hydrolysis activity, and transport assays showed that ABCB19 transports brassinosteroids."]
- PMID:39497419 mainly ABCB1; ABCB19 annotations from it kept (ABCB19 likely comparator in full text).
- No GO term for brassinosteroid transport; raised as a suggested question.

## Decisions
- Many developmental/light-response IMP/IEA rows KEEP_AS_NON_CORE (downstream of transport).
- Leaf phyllotactic patterning (PMID:32855213): paper studies petiole angle, not phyllotaxis (full text checked: no "phyllotaxis") -> MARK_AS_OVER_ANNOTATED.
- Cytosol HDA (PMID:28887381) and nucleus ISM REMOVE: 12-TM integral PM protein.


## Polar auxin transport source audit — 2026-10-26

This dated audit supersedes conflicting earlier shorthand. All 73 original annotation payloads, including qualifiers and inherited NEW rows, were retained exactly. Every row was reconsidered against the target biology and cited sources. Actual Falcon and fallback provider attempts failed; the orchestration logs are preserved in `.cache/module-audit-logs/auxin-polar-fetch/provider-publication-results.json`. Existing provider reports, where present, served only as discovery aids. Manual primary-source inspection and normally fetched caches support the decisions below. No provider report was fabricated.

Direct IAA-export evidence is retained, but auxin-only specificity and unqualified ATPase/IAA coupling are not asserted. Full PMID:38513023 plus supplementary text was recovered normally from the Ghent author manuscript at publications/url_https___biblio.ugent.be_publication_01HTMBK3P3PPNB73YFCMFXP3ZZ_file_01HTMC3Z7XJ6XPXCM124Z4RD35.pdf.md. It provides direct brassinosteroid transport and BR-stimulated ATPase activity; its purified binding/ATPase/proteoliposome IAA-negative results coexist with a positive ABCB19+TWD1 HEK293F cellular IAA loading/export assay (Fig. S3F). A negative ATPase stimulation result is not by itself a transport assay. PMID:39497419 mainly studies ABCB1 but contains ABCB19 comparator assays; those source-specific distinctions replace the old assumption that any ABCB19 result was merely likely.

The 28887381 cytosol claim is MARK_AS_OVER_ANNOTATED after all seven actual XLSX supplements were inspected, not because a 12-TM protein cannot have a cytoplasmic pool. ABCB19 S1 rows 2145/2804 are True membrane, with blank dual-localization flags; the material described as soluble is cholate-solubilized microsomes, not cytosol. Imported SUBAcon labels are not new localization measurements, and a blank dual-localization flag does not prove absence of any minor pool. Reproducible download/extraction, exact hits and SHA-256 provenance are in ABCB19-bioinformatics/. Nucleus prediction is UNDECIDED, superseding the old membrane-exclusivity REMOVE.

Full PMID:35512423 was inspected at publications/url_https___oup.silverchair-cdn.com_article-minimal_6581225.md. Native ABCB19–GFP occupies filament epidermis/provasculature at stage 12; abcb1 abcb19 has shorter filament cells, reduced pollen number/viability and abnormal nuclei. These support contextual morphogenesis and gametophyte contributions, not exclusive ABCB19 necessity. The failed cell-plate/callose aggregation, stamen-number, nectary and early-dehiscence effects are TWD1-specific. GO:0090627 requires acquisition of epidermal identity; measured growth of existing epidermal cells does not establish it, so both corresponding rows are overannotated. The independent leaf study PMID:32855213 concerns petiole angle/flattening rather than primordium phyllotactic patterning.

Both GO:0043481 UV-anthocyanin rows are UNDECIDED. Live GO requires UV stimulus; the accessible 15908594 abstract/publisher preview explicitly supports pigment changes and far-red/red/blue responses, but cannot establish UV treatment. PMC was browser-challenged and Europe PMC returned 403. This is not a claim that the inaccessible full study lacks a relevant experiment. Broad membrane/ATPase/transmembrane IBA refinements preserve the genuine ancestral properties; actual PTHR43394 PTN002517083/PTN000657189 entries include ABCB19 among legitimate experimental seeds, not circular support.

Final actions: 22 ACCEPT, 37 KEEP_AS_NON_CORE, 4 MARK_AS_OVER_ANNOTATED, 6 MODIFY, 1 REMOVE, 3 UNDECIDED. This panel contains no negated source rows; there are no manufactured NOT assertions. Exact-row payload proof and focused validation are recorded in `.cache/module-audit-logs/auxin-polar-six-*`. Reciprocal scientific consultation with the parallel annotation reviewer confirmed source-specific localization, integral binding and substrate-assay distinctions.


## Bounded source follow-up — 2026-10-26

Full15908594 recovered after the earlier access-limited assessment. Results/Fig.3C and Methods were independently read: anthocyanin assays use continuous far-red/blue illumination; UV-A is introductory photoreceptor context. Existing curated function supports light-dependent pigments without UV specificity, and a targeted ABCB19/MDR1 UV literature search found no independent target UV-pigment assay. Both UV rows remain UNDECIDED because the biological claim is neither established nor contradicted. This replaces the obsolete inaccessible-full-text rationale; it does not convert non-UV experiments into negative UV evidence. Normal full source: publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC1150410_.md. No action or annotation payload changed.
