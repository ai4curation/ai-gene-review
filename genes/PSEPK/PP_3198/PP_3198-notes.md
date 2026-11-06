# PP_3198 curation notes

- UniProt identifies PP_3198 as a 112-aa Rieske [2Fe-2S] ferredoxin-domain
  protein [file:PSEPK/PP_3198/PP_3198-uniprot.txt "Rieske_2Fe-2S"].
- KEGG maps PP_3198 to K26179/FdeD and reaction R13074, but labels R13074 an
  unclear reaction. This supports placement in the predicted pathway, not a
  defined electron-transfer partner.
- The OpenScientist run ended with a DNS connection failure and produced no
  research artifact. The review therefore uses the fetched records, KEGG
  mapping, primary pathway paper, and a reproducible ortholog comparison.

## 2026-11-06 — comparative fde audit

Read the 2013 full paper through its author-uploaded copy; its fdeA mutation is probably polar. Preserve the distinction between locus-level inference and exact catalytic assignment. See modules/bacterial_flavonoid_degradation-notes.md for source access and comparative boundaries.

## 2026-11-06 — comparative review follow-up

Reassessed the PR #6140 review requests against the original row payloads and independent sources. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md` for the mapping, family and participation decisions. All original rows remain in their original order; inherited proposals that lack positive participation evidence are withdrawn by review action rather than deleted. No raw UniProt, GOA or provider artifact was edited.

The inherited GO:0046275 proposal is explicitly `retired: true` because this review withdraws it from the active curator-authored set. Its source fields and row position are retained. This does not claim that an upstream GOA row disappeared. The current MAOA judgment records the reassessment; the original NEW judgment is preserved in git and the follow-up preservation record. The existing schema defines retirement as an annotation being retired or replaced, and `docs/goa_source_refresh.md` uses explicit retirement to preserve withdrawn curator-authored assertions.
