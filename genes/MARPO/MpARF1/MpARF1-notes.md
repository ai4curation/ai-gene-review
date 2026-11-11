# MpARF1 evidence notes


## 2026-10-26 native auxin-system evidence audit

All seeded annotation payloads were preserved, including term IDs, evidence types, original sources, supporting entities and flags. The review evaluates biological claims independently of inert relationship fields. No new annotation row was added. Available genuine prior research reports were used for discovery; primary text and curated record statements were preferred for evidence. The actual Falcon and perplexity-lite fallback attempts failed (authorization/quota errors), as recorded in `.cache/module-audit-logs/auxin-fetch/`; no provider report was fabricated. Normal publication fetching and normal ReferenceFetcher URL recovery supplied the sources below. Canonical PMID records were not hand-edited to insert recovered text.

The annotation-reviewer workflow was applied to every row. Bare protein-binding rows are refined only where the interaction and functional partner class support a more informative term; removal of an otherwise uninformative binding row does not dispute the measured interaction. True general transcription terms are refined rather than rejected. Nuclear evidence does not establish absence from cytoplasm.
Identity is tied to the primary publication clone KP877969/AKJ88118.1 and UniProt A0A0G3FLP1 (926 aa), explicitly named in PMID:26020649. Independent 2015 assays use the AB981317 clone; alternative current genome products A0A2R6XES5/A0A2R6XEU4 differ in length. These records are not asserted to be sequence-identical. Functional conclusions are at the resolved locus and conserved-domain level, with precise clone provenance retained. PMID:26901620 corrects figure/control presentation and methods in the first 2015 study and is cited alongside it.

PMID:26020919 directly tests Gal4-fused full-length and middle-region proteins in tobacco BY-2 cells: “Both the middle region and full-length sequences of MpARF1 showed approximately two-fold higher activity than the effector expressing only Gal4 DBD.” This establishes activation capacity in a heterologous assay. Native genetic/domain complementation in PMID:32415296 and PMID:40168121 supports its physiological relevance. The 2025 bulk-gemma auxin transcriptome found no differential response without MpARF1 in the tested conditions; this does not make all transcription or every cell response dependent on MpARF1. DNA-contacting mutants were tested with protein accumulation/localization controls; structural docking alone was not called a binding assay.

The normally fetched full 2020 PDF is `url:https://edepot.wur.nl/523089`; the 2025 DBD paper is `url:https://edepot.wur.nl/690102` (canonical PMID:40086441). MpARF2 B3 or DBD swaps into MpARF1 test recognition within an activator scaffold, not the native activity of MpARF2. An isolated MpARF1 LFG peptide can repress with MpTPL in a reporter but full-length MpARF1 did not show the clear MpTPL interaction seen for MpARF2; no native MpARF1–MpTPL direct pair is manufactured. Nuclear function is a conserved inference, not a claim of exclusive residence. All five seeded rows were adjudicated and no NEW row added merely to mirror the independently supported core MF.

Validation and source-closure results are recorded in `.cache/module-audit-logs/auxin-arf-tpl-final-report.md`; the committed helper history identifies this curation session.


## 2026-10-26 — PR #5576 evidence follow-up

Removed the automated UniProt nucleus statement as purported independent confirmation of the IEA. Nuclear activity is a functional inference from independently assayed ARF transcriptional regulation, with source references and explicit native-imaging limits. No row payload/action changed.
