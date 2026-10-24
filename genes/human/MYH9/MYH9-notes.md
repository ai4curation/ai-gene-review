# MYH9 review notes

## 2026-09-27 (claude-code)

Sources: UniProt P35579, cached GOA-cited publications (many abstract-only), PMID:37987147 (amoeboid nucleokinesis).
Falcon deep research was not available when the review was finalized.

Core biology
- Heavy chain of non-muscle myosin IIA; actin-activated Mg-ATPase that translocates actin
  [PMID:12237319 "The R702C mutant displays 25% of the maximal MgATPase activity of wild type heavy meromyosin and moves actin filaments at half the wild type rate"].
- Forms bipolar filaments after RLC phosphorylation [PMID:24072716 "Phosphorylation of the regulatory light chain leads to assembly into filaments, which bind to actin in the presence of ATP"].
- Contractile ring / cleavage furrow [PMID:11029059 "GFP-tagged full-length NMHC II-A or II-B, but not delta N592, were localized to the cytokinetic ring during mitosis"].
- Only class II myosin in T cells; uropod and motility [PMID:15064761 "MyH9 function is required for maintenance of the uropod and for T cell motility but is dispensable for synapse formation"].

Nucleokinesis (module context)
- MYH9-GFP accumulates behind the nucleus during amoeboid (dendritic cell) nucleokinesis; myosin II forces drive it
  [PMID:37987147 "Amoeboid nucleokinesis comprises a two-step polarity switch and is driven by myosin-II forces that readjust the nuclear to the cellular path"].
- The neuronal nucleokinesis papers used by the module are either paralog-agnostic (blebbistatin) or MYH10-specific
  (PMID:19607793 studies Myosin IIB in cerebellar granule neurons). No MYH9-specific neuronal evidence found in cache,
  so no NEW nuclear migration annotation was added.

Citation problem
- PMID:2732579 (cited by GOA for RAB3A binding, lysosome localization, regulated exocytosis, regulation of plasma
  membrane repair) is a 1989 Japanese case report on hypoparathyroidism. Same WITH/FROM partner (RAB3A) and content as
  PMID:27325790 (Rab3a/Slp4-a/NMHC-IIA), whose id it truncates. Recorded as WRONG_IDENTIFIER with replacement.

Decisions summary
- Protein binding: S100A4/S100 papers -> MODIFY to GO:0044548 S100 protein binding; RAB3A -> GO:0031267 small GTPase binding;
  ITGB3 -> integrin binding; the rest REMOVE (uninformative).
- ACE shedding (membrane protein ectodomain proteolysis) -> MODIFY to negative regulation (GO:0051045).
- Exosome/RNA-binding/COP9/cadherin HDA rows -> MARK_AS_OVER_ANNOTATED.
- Nucleus (PMID:14508515) -> UNDECIDED (abstract-only, cannot see nuclear data).

## 2026-09-27 update: Falcon deep research incorporated

- MYH9-deep-research-falcon.md arrived after the first pass. It is review-based (Brito & Sousa 2020; Asensio-Juarez 2020;
  Feroz 2024 and others; no new primary PMIDs) and agrees with the review: core = actin-activated Mg-ATPase motor forming
  bipolar minifilaments; MYH9-RD; megakaryocytes express only NMIIA.
- Used as retrieval support only: added to the platelet formation row (non-core, unchanged) and to the leukocyte-migration
  core function, for its caveat "many pharmacologic studies inhibit all NMII isoforms, whereas MYH9-specific knockout,
  knockdown or mutation gives stronger isoform-level evidence". This matches the nucleokinesis paralog question.
- No action changes: nothing in the report contradicts a decision or adds new primary evidence for any row.
