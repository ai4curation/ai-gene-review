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


## 2026-11-07 PR #6140 round-2 review follow-up

The inherited GO:0046275 proposal now uses REMOVE with its existing retired:true flag. This explicitly withdraws a curator-authored proposal, following the documented cysI precedent, rather than making a biological absence claim or reporting disappearance from upstream GOA. Original payload, position and evidence remain present.

See `analysis/module_audits/bacterial_flavonoid_degradation/round2-review-response.md` for source provenance, limits and disposition of all seven review points. Earlier journal entries record superseded judgments and remain unchanged.

## PR #6140 round-3 consultation — 2026-11-07

Corrected the retired GO:0046275 reason from the superseded over-annotation wording to withdrawal of the earlier curator-authored proposal. REMOVE and retired:true are unchanged; this is not a claim of biological incapacity or disappearance from GOA.

All ordered annotation payloads and actions are preserved, including the nine prior retirements across the panel. No source record, provider report or publication cache was edited. The shared FdeB analysis retains its stable PP_3195 host path with an explicit cross-species README and separate round-3 module-audit outputs; historical round-2 results are unchanged.
