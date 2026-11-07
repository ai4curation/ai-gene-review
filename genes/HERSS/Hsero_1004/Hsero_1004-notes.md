# Hsero_1004 notes

## 2026-11-04 session (Claude, AI-assisted)

- Fetched with `just fetch-gene HERSS <accession> --alias Hsero_1004`: the gene-name lookup
  failed because the UniProt stream endpoint returned 503, so the accession route was used.
- No provider deep-research file was generated (no provider API keys in this session).
  The review rests on the UniProt record, the cached pathway papers
  [PMID:27059806] (abstract only) and, for fdeE, [PMID:39107441] (full text), the
  KEGG queries in `genes/HERSS/Hsero_1007/Hsero_1007-bioinformatics/`, and the P.
  putida ortholog reviews (PSEPK PP_3195-PP_3206) with their committed alignments.
- Literature search (PubMed E-utilities, 2026-11-04): "naringenin Herbaspirillum"
  (13 hits), "fdeE naringenin" (2: PMID:27059806, PMID:39107441), "Hsero_1007"
  (1: PMID:27059806). Pathway-relevant hits cached: PMID:23125118 (fde operon induced
  by naringenin; fdeA and fdeR mutants cannot degrade naringenin), PMID:27059806
  (fdeE, fdeC, fdeG mutants), PMID:27878922 (FdeR activator), PMID:39107441 (purified
  FdeE). Only FdeE has been assayed biochemically; only fdeA, fdeC, fdeE, fdeG and fdeR
  have been mutated.
- Context: written for the module `modules/bacterial_flavonoid_degradation.yaml`.

## 2026-11-06 — comparative fde audit

Read the 2013 full paper through its author-uploaded copy; its fdeA mutation is probably polar. Preserve the distinction between locus-level inference and exact catalytic assignment. See modules/bacterial_flavonoid_degradation-notes.md for source access and comparative boundaries.

## 2026-11-06 — comparative review follow-up

Reassessed the PR #6140 review requests against the original row payloads and independent sources. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md` for the mapping, family and participation decisions. All original rows remain in their original order; inherited proposals that lack positive participation evidence are withdrawn by review action rather than deleted. No raw UniProt, GOA or provider artifact was edited.

The inherited GO:0046275 proposal is explicitly `retired: true` because this review withdraws it from the active curator-authored set. Its source fields and row position are retained. This does not claim that an upstream GOA row disappeared. The current MAOA judgment records the reassessment; the original NEW judgment is preserved in git and the follow-up preservation record. The existing schema defines retirement as an annotation being retired or replaced, and `docs/goa_source_refresh.md` uses explicit retirement to preserve withdrawn curator-authored assertions.


## 2026-11-07 PR #6140 round-2 review follow-up

The inherited GO:0046275 proposal now uses REMOVE with its existing retired:true flag. This explicitly withdraws a curator-authored proposal, following the documented cysI precedent, rather than making a biological absence claim or reporting disappearance from upstream GOA. Original payload, position and evidence remain present. Broad GO:0016787 hydrolase activity is retained in the core synthesis as a family/fold/conserved-candidate inference, without selecting ester versus C-C chemistry, substrate, or native process participation. The independent sequence check corrects the provider report's Asp358 to actual Asp359 in PP_3195. Its H405 candidate corresponds to bll6428 Q374, while alignment of characterized Q93NG6 S217/D300/H329 maps to PP_3195 S268/D359/H394, Hsero_1004 S233/D324/H359 and bll6428 S237/D328/H363. Candidate correspondence is not proof of target geometry or catalytic loss. See PP_3195-bioinformatics/fdeb-round2/RESULTS.md and the reproducible round2 maps. The C-C family comparator is now cited directly to the primary PMID:16321959 (hydrolytic cleavage) and official reviewed Q93NG6 record; PMID:17275835 supports the comparator structure/mutagenesis context. Both fetched papers are abstract-only; no target experiment is attributed to them.

See `analysis/module_audits/bacterial_flavonoid_degradation/round2-review-response.md` for source provenance, limits and disposition of all seven review points. Earlier journal entries record superseded judgments and remain unchanged.
