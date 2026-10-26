# ARF19 (At1g19220; Q8RYC8) curation notes

## 2026-10 follow-up (auxin_nuclear_signaling module)

- Prior review existed (status COMPLETE) but 8 annotations were UNDECIDED.
- Resolved the 7 protein-binding IPIs: partners are Aux/IAA repressors (IAA3/SHY2 [PMID:15889151], IAA14 [PMID:16236149 "IAA14 interacted with ARF7 and ARF19 in yeasts"], IAA18 [PMID:18505759], large Aux/IAA sets in interactomes [PMID:21734647, PMID:28650476, PMID:32612234], IAA27 [PMID:36088536]) -> MODIFY to GO:0001222 transcription corepressor binding (same as ARF7).
- GO:0043565 IDA from the BAT1 paper [PMID:23020607] (abstract-only): accepted, deferring to curator; ARF19 AuxRE binding independently shown [PMID:29681137 "We showed that ARF7 and ARF19 directly bind AuxRE in the LBD18 promoter"].
- NEW GO:0001216 DNA-binding transcription activator activity [PMID:15960621 "We show that ARF19, the fifth Q-rich ARF, also activates transcription"]; added as first core function.


## 2026-10-26 native auxin-system evidence audit

All seeded annotation payloads were preserved, including term IDs, evidence types, original sources, supporting entities and flags. The review evaluates biological claims independently of inert relationship fields. No new annotation row was added. Available genuine prior research reports were used for discovery; primary text and curated record statements were preferred for evidence. The actual Falcon and perplexity-lite fallback attempts failed (authorization/quota errors), as recorded in `.cache/module-audit-logs/auxin-fetch/`; no provider report was fabricated. Normal publication fetching and normal ReferenceFetcher URL recovery supplied the sources below. Canonical PMID records were not hand-edited to insert recovered text.

The annotation-reviewer workflow was applied to every row. Bare protein-binding rows are refined only where the interaction and functional partner class support a more informative term; removal of an otherwise uninformative binding row does not dispute the measured interaction. True general transcription terms are refined rather than rejected. Nuclear evidence does not establish absence from cytoplasm.
ARF19 directly activates LBD genes together with ARF7; the supported main MF is GO:0001216, with sequence-specific cis-regulatory DNA binding. The full PMID:17259263 source is separately cached at `url:https://pmc.ncbi.nlm.nih.gov/articles/PMC1820965/`; it contains the target-specific GFP localization absent from the abstract-only PMID cache. Nuclear location is independently supported by PMID:31421981, which also documents mature-root cytoplasmic condensates. An old Aux/IAA-family quotation was not used as localization evidence for ARF19.

The many Aux/IAA interactions were evaluated by partner class rather than assuming a single repressive mechanism. IAA33 contacts in the shoot-apex and CrY2H screens are refined to GO:0001221 transcription coregulator binding. PMID:31617603 (full source normally recovered at `url:https://pmc.ncbi.nlm.nih.gov/articles/PMC6939196/`) demonstrates IAA33 competition with IAA5 for ARF10/16, not TPL recruitment or a direct repressive effect on ARF19. IAA32/34 retain the corepressor-binding class, supported by their noncanonical repressor roles in PMID:30944466; TMK1-dependent stabilization is not silently transferred into the specific ARF19 screen complexes. The existing NOT9B bare-binding removal remains an informativeness decision, not denial of interaction.

Direct LBD regulation supports lateral-root participation; the process is not dismissed as an indirect phenotype. Regeneration/callus roles remain contextual, and the original evidence codes are preserved. The abstract-only BAT1-source annotation is not embellished with a guessed exact promoter; independent ARF19 AuxRE binding supports the activity. Generic transcription and hormone terms are refined consistently with the demonstrated positive direction and auxin/ethylene biology.

Validation and source-closure results are recorded in `.cache/module-audit-logs/auxin-arf-tpl-final-report.md`; the committed helper history identifies this curation session.
