# PP_4473 curation notes

Q88EI9 is a reviewed UniProt entry and the strongest PSEPK anchor in this
module. UniProt attributes the reaction, feedback inhibition by lysine and
threonine, kinetic values, and methionine repression to the direct P. putida
study [PMID:5441401, "The aspartate kinase of Pseudomonas putida. Regulation of synthesis and activity."].
The local publication cache is bibliographic only, so claims were anchored to
the curated UniProt record and the experimental GOA was not second-guessed.

This enzyme is a shared entry point, not a threonine-specific enzyme. Its core
summary therefore uses the broad amino-acid biosynthetic process while retaining
the supported lysine, homoserine, and threonine branch annotations.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. A normal Falcon attempt returned HTTP 403 Failed to authenticate; no fabricated report was written. Manual literature and curated-source review supplied the fallback.

The historical PMID:5441401 record contains bibliographic information, not accessible experimental text. Neither the 1970 strain nor its enzyme sequence is established. The original IDA row and UniProt experimental link are preserved: aspartate kinase activity is independently persuasive from the curated reaction and TIGR00656/TIGR00657/PS00324. This does not verify the old numerical Km values, concerted inhibition or methionine repression specifically for KT2440 Q88EI9. Do not repeat the earlier batch's claim of a direct exact-target assay. ACT-domain presence does not settle a particular regulatory response.

PMID:40236303 reports native LysC/Hom overproduction: “Despite the successful overproduction of two key enzymes, aspartate kinase (LysC) and homoserine dehydrogenase (Hom) from different plasmid combinations”, there was no threonine increase. The Table S2 reverse primer lysC_xba_R encodes terminal PARQGE, matching Q88EI9. This is direct native cloning/engineering identity, not purified kinetics. The reproducible terminal-primer analysis is in PP_4473-bioinformatics/primer-identity/; it includes the original DOCX, source extraction, all input hashes and comparison paralogs. Cytosolic location is an inference from the curated cytoplasmic soluble metabolic enzyme, not direct localization. Broad biosynthesis is refined to the supported existing branches.

The inherited authored GO:0071266 NEW row is archived in full at PP_4473-source-analysis/retired-new-annotations.yaml and retired from the active review. Live QuickGO defines this process as forming methionine from simpler components including aspartate or homoserine; shared precursor enzymes can therefore participate. The issue is insufficient independent support for this particular extra native assertion, not exclusion by definition. Its parents include amino-acid biosynthesis (GO:0008652), sulfur amino-acid biosynthesis and methionine biosynthesis. Existing annotations/cores were checked for overlapping methionine terms. Exact-term QuickGO comparator queries on E. coli ThrA P00561 and MetL P00562 returned zero; this is a convention warning, not proof of false biology. No cached GO-CAM index hit was found for these three targets. Shared methionine precursor biology remains in prose; no replacement NEW ancestor/descendant is proposed. Query responses are preserved in the ignored audit logs.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.

Direct DOI full-text access was attempted for the relevant historical 1970 papers and the 1992 P. aeruginosa paper using the web tool on 2026-11-01; the URLs were inaccessible. No unavailable experimental detail was invented.


## 2026-11-01 PR5858: restoration of inherited methionine proposal

This resolves and supersedes the earlier retirement verdict above for PP_4473 alone. The full original ISS proposal and historical retirement reason remain in `PP_4473-source-analysis/retired-new-annotations.yaml`, now with a separate current disposition. The active row is restored as authored IC, and the same inferred process is included in the core and broad-process refinement. No additional novel proposal was created.

The reviewed Q88EI9 UniProt record explicitly states “L-methionine biosynthesis via de novo” followed by “pathway; L-homoserine from L-aspartate: step 1/3.” This untagged curated pathway assignment is distinct from Hom's ARBA-only pathway line and from PP_0664's unresolved native role. Independent aspartokinase family and catalytic evidence establish that PP_4473 executes the first chemical reaction. The live GO:0071266 definition explicitly covers synthesis “from simpler components such as L-aspartate or L-homoserine.” Thus it is actual pathway chemistry, not mere necessity of a consumed substrate. No existing methionine ancestor/descendant duplicates this restored proposal.

The earlier exact-GO:0071266 comparison was incomplete: current parent-inclusive GO:0071265 queries find an ISS parent row on E. coli ThrA P00561 and MetL P00562. Both are bifunctional, so these rows cannot isolate their kinase domains. E. coli LysC P08660 and C. glutamicum LysC P26512 lack methionine rows in the same queries. This absence does not establish exclusion: the latter has the same curated step 1/3 pathway statement, and the primary C. glutamicum study PMID:20573952 explicitly places aspartokinase at the first shared lysine/threonine/methionine reaction. E. coli LysC's own curated pathway instead lists lysine only. Query sources, dates, responses, definition and interpretation are retained in `PP_4473-source-analysis/methionine-comparators.yaml`; comparator annotations are convention context, not biological support.

The conclusion remains inferred. Neither the unavailable 1970 paper nor the 2025 KT2440 cloning study establishes a native methionine phenotype or quantitative branch flux for this exact protein. Historical strain uncertainty, lack of verified KT2440 feedback kinetics and the limits of terminal-primer identity evidence remain unchanged.
