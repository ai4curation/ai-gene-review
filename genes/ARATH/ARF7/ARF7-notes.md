# ARF7 / NPH4 (At5g20730; P93022) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Deep research (falcon) failed (HTTP 402); review based on cached literature.
- Identity: UniProt P93022 ARFG_ARATH, ARF7 (NPH4/MSG1/TIR5/BIP). Correct.

### Function
- "NPH4 encodes the auxin-regulated transcriptional activator ARF7"; required for differential growth (phototropism, gravitropism) [PMID:10810148].
- ARF7 restores auxin-responsive gene expression in nph4-1 protoplasts [PMID:15923351].
- arf7 arf19 lacks lateral roots, abnormal gravitropism; auxin-induced gene expression impaired [PMID:15659631]; ARF7/ARF19 directly activate LBD16/LBD29 [PMID:17259263].
- Leaf expansion and lateral roots [PMID:15960621]; ethylene responses in roots [PMID:16461383]; callus formation via ATXR2 and JMJ30 recruitment [PMID:29184030, PMID:29923261].
- PB1 domain structure: "Mutation of interface residues in the ARF7 PB1 domain yields monomeric protein and abolishes interaction with both itself and IAA17" [PMID:24706860].
- BIN2 phosphorylation weakens ARF7-Aux/IAA binding [PMID:24362628]; MYB77 cooperates with ARF7 [PMID:17675404].
- Cytoplasmic condensates in low-auxin-response tissues [PMID:31421981].

### Decisions
- Aux/IAA protein-binding IPIs -> MODIFY GO:0001222 transcription corepressor binding; BIN2 -> GO:0019901; MYB77 -> GO:0140297; ATXR2 -> GO:1990226; JMJ30 -> GO:0019899 (consistent with ARF19 review).
- Blue light signaling pathway IMP (PMID:10364413) -> MARK_AS_OVER_ANNOTATED (ARF7 acts in auxin response downstream).
- Developmental processes (lateral root, leaf, callus, tropisms, ethylene) -> KEEP_AS_NON_CORE.
- NEW: GO:0001216 DNA-binding transcription activator activity; GO:0009734 auxin-activated signaling pathway.


## 2026-10-26 native auxin-system evidence audit

All seeded annotation payloads were preserved, including term IDs, evidence types, original sources, supporting entities and flags. The review evaluates biological claims independently of inert relationship fields. No new annotation row was added. Available genuine prior research reports were used for discovery; primary text and curated record statements were preferred for evidence. The actual Falcon and perplexity-lite fallback attempts failed (authorization/quota errors), as recorded in `.cache/module-audit-logs/auxin-fetch/`; no provider report was fabricated. Normal publication fetching and normal ReferenceFetcher URL recovery supplied the sources below. Canonical PMID records were not hand-edited to insert recovered text.

The annotation-reviewer workflow was applied to every row. Bare protein-binding rows are refined only where the interaction and functional partner class support a more informative term; removal of an otherwise uninformative binding row does not dispute the measured interaction. True general transcription terms are refined rather than rejected. Nuclear evidence does not establish absence from cytoplasm.
ARF7 is a direct activator and Aux/IAA-binding transcriptional regulator. PMID:24706860 directly perturbs the ARF7 PB1 interface, while PMID:14729917 tests the IAA19–ARF7 interaction; these are stronger than assuming that every ARF-family contact has the same mechanism. Chromatin-regulator interactions with ATXR2/JMJ30 and BIN2 binding remain distinct from ARF catalytic activity.

The full source of PMID:17259263 was recovered normally as `url:https://pmc.ncbi.nlm.nih.gov/articles/PMC1820965/`. Figure 1 explicitly distinguishes 35S-driven ARF7-GFP from ARF19-promoter ARF19-GFP, and shows nuclear localization. PMID:31421981 confirms “ARF7-Venus and ARF19-Venus localized to the nucleus in meristem cells near the root tip” while identifying cytoplasmic assemblies in mature root cells. Nuclear claims are retained without exclusivity. Direct LBD activation supports both ARF7 and ARF19 participation in lateral-root formation; the broader lateral-root-development row is refined to formation rather than treated as false.

The blue-light signaling judgment was reconsidered against the live GO:0009785 definition and full sources. Normal nph4 stomatal responses in PMID:10364413 do not refute a phototropic signaling role. PMID:10810148 identifies NPH4 as ARF7 and reports dramatically reduced phototropic responses and conditional, ethylene-suppressible differential-growth defects. This supports a non-core downstream blue-light response branch, not a photoreceptor or every blue-light pathway. A broad hormone-response mapping retains both documented auxin and ethylene descendants. The PAINT regulation node is refined for direction with no allegation of phylogenetic failure.

Validation and source-closure results are recorded in `.cache/module-audit-logs/auxin-arf-tpl-final-report.md`; the committed helper history identifies this curation session.


### Partner-matched source follow-up, 2026-10-26

Independent QA identified that the canonical PMID:14729917 extraction is truncated despite its full-text flag. The parent recovered the complete public source normally at `publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC341911_.md`. Its Results/Figure 9B directly support ARF7 CTD binding to IAA1, IAA6 and IAA13 (bars 5–7). The existing IAA1 row and core binding support now quote these experiments rather than the IAA19-only abstract; no IAA6/IAA13 rows were manufactured. All existing actions and raw annotation payloads are unchanged. Yeast binding capacity is not equated to a shared native developmental phenotype or an obligatory TPL-containing complex. Canonical PMID provenance is retained alongside the recovered full-source file.
