# MpTPL evidence notes


## 2026-10-26 native auxin-system evidence audit

All seeded annotation payloads were preserved, including term IDs, evidence types, original sources, supporting entities and flags. The review evaluates biological claims independently of inert relationship fields. No new annotation row was added. Available genuine prior research reports were used for discovery; primary text and curated record statements were preferred for evidence. The actual Falcon and perplexity-lite fallback attempts failed (authorization/quota errors), as recorded in `.cache/module-audit-logs/auxin-fetch/`; no provider report was fabricated. Normal publication fetching and normal ReferenceFetcher URL recovery supplied the sources below. Canonical PMID records were not hand-edited to insert recovered text.

The annotation-reviewer workflow was applied to every row. Bare protein-binding rows are refined only where the interaction and functional partner class support a more informative term; removal of an otherwise uninformative binding row does not dispute the measured interaction. True general transcription terms are refined rather than rejected. Nuclear evidence does not establish absence from cytoplasm.
The selected protein A0A0G3FGV9 (1184 aa) is the publication-linked KP877967/AKJ88116.1 clone from PMID:26020649. The current alternative genome accession A0A2R6WXA2 was not silently substituted. Conserved LisH/CTLH/WD40 architecture and the primary experimental work support a corepressor classification independently of its submitter protein name and ARBA-only location line.

The 2015 MpTPL–D34/PB1 fusions are engineered recruitment experiments. Their developmental/auxin-insensitive phenotypes demonstrate the effect of forcing repression into the circuit, not a direct native MpTPL–MpIAA or MpTPL–MpARF1 binary interaction. The promoter3xVENUSN7 construct includes an artificial NLS: its nuclear reporter distribution measures expression and does not localize the native MpTPL protein. PMID:26901620 corrects figure/control and method presentation in that paper and is retained.

The normal full 2020 source is `url:https://edepot.wur.nl/523089` (PMID:32415296). Full MpARF2, but not full MpARF1, clearly associates with MpTPL in Arabidopsis-protoplast FRET–FLIM; LFG→AAA eliminates this interaction. LFG-peptide/MpTPL coexpression represses the tobacco reporter, supporting corepressor capacity. Native Marchantia MpARF2 genetics strengthens the circuit model but does not convert those heterologous assays into native complex isolation. GO:0003714 is the supported core MF. Nuclear action is retained as a conserved functional inference with the explicit lack of native-protein imaging, not as an ARBA-supported fact. Both initial rows are preserved and no automatic NEW MF/location row is added.

Validation and source-closure results are recorded in `.cache/module-audit-logs/auxin-arf-tpl-final-report.md`; the committed helper history identifies this curation session.
