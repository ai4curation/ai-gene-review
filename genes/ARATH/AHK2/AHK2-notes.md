# AHK2 notes (Q9C5U2, At5g35750)

## 2026-10-05 review session (cytokinin two-component signaling module)

- Identity checked: UniProt Q9C5U2 AHK2_ARATH, At5g35750, 1176 aa CHASE-domain hybrid histidine kinase.
- Deep research (`just deep-research-perplexity-lite`) failed in this environment ("All providers failed"); no deep-research file was produced. Review is based on cached publications.
- One of three cytokinin receptors [PMID:14503005 "Cytokinins are perceived by three histidine kinases--CRE1/WOL/AHK4, AHK2, and AHK3--which initiate intracellular phosphotransfer."].
- Positive regulator of cytokinin signaling, redundant with AHK3/AHK4 [PMID:15155880 "both AHK2 and AHK3 function as positive regulators for cytokinin signaling similar to AHK4"]; triple mutant is fully cytokinin-insensitive [PMID:15166290 "Plants carrying mutations in all three genes did not show cytokinin responses"].
- Kinase-favouring receptor: [PMID:16753566 "replacing CRE1 with AHK2, which favors kinase activity, increased cytokinin sensitivity"] -> supports the NOT phosphoprotein phosphatase annotation.
- Location: mainly ER [PMID:21709172 "the large majority of cytokinin receptors are localized to the ER"]; plasma membrane kept as non-core.
- Physiology (non-core): secondary growth/procambium [PMID:19622803], flower development via CUC2/CUC3 [PMID:19913077], cold/ABA [PMID:20463025], drought/salt negative regulation [PMID:18077346], seed germination & chlorophyll retention [PMID:16361392].
- Flags:
  - GO:0009636 (PMID:17216481): abstract describes the cre1 (AHK4) mutant, not ahk2 -> UNDECIDED.
  - GO:0046686 (PMID:40858022): "AtHK2" in a glycolysis/autophagy context may be HEXOKINASE2 -> UNDECIDED.
  - GO:0034757 (PMID:18397377): abstract names AHK3 and CRE1 only -> UNDECIDED.
- Protein-binding rows (Y2H): AHK-AHK -> MODIFY to GO:0043424; AHK-AHP and screen partners -> REMOVE (phosphotransfer captured by GO:0000155).
- Proposed NEW: GO:0009885 transmembrane histidine kinase cytokinin receptor activity (AHK4 already carries it by IDA).

## 2026-10-06 follow-up: resolving UNDECIDED rows

- Tried full text for PMID:17216481, PMID:18397377, PMID:40858022: none has a PMC/Europe PMC copy (Europe PMC: no pmcid, not open access); publisher pages (Springer, Wiley, ScienceDirect) blocked (403/login redirect). Web search snippets repeat the abstracts only.
- PMID:17216481 (GO:0009636) and PMID:18397377 (GO:0034757 IMP + ARBA IEA): cannot see whether ahk2 was assayed; deferred to curator as KEEP_AS_NON_CORE (plausible for a redundant cytokinin receptor, indirect output).
- PMID:40858022 (GO:0046686): "AtHK2" appears with AtGAPDH/AtENO2 in a glycolysis/energy context, most consistent with HEXOKINASE2; marked MARK_AS_OVER_ANNOTATED with a reference_review noting the suspected gene mis-mapping (unverified without full text).
