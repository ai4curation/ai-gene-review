# NF2 notes

## 2026-11-22 Codex review

Fetched `NF2` with `just fetch-gene human NF2` and confirmed `NF2-goa.tsv` has data rows rather than a header-only failed fetch. The fetched GOA set contained 55 bare `GO:0005515 protein binding` rows, all removed under the project protein-binding policy.

Attempted the family from the PTHR23281 queue as a compact Merlin/ERM review. Fetching EZR, MSN, RDX, and NF2 showed that the canonical ERM branch alone carries several hundred GOA rows, so this PR scopes the first split to the Merlin/NF2 branch and leaves EZR/MSN/RDX for a later PTHR23281 split.

Deep-research generation was unavailable in this checkout because no configured provider/API key could be used. I therefore reviewed the cached UniProt, GOA, PAINT, GO-CAM, Reactome, and publication files manually instead of creating a synthetic `*-deep-research-*` provider file.

Key curation calls:

- `PTHR23281` PAINT puts `GO:0003779 actin binding` and the ERM endosome-process terms at PTN001150648, above both Merlin and canonical ERM proteins. Human Merlin lacks the canonical ERM actin-binding site and has only indirect or context-specific links to actin/endosome phenotypes, so the family review requests an IRD at the Merlin branch node PTN001150649.
- The Hippo/proliferation PAINT terms are already placed on the Merlin node PTN001150649 and were accepted for NF2.
- The production GO-CAM `gomodel:65a1f4f800003542` covers the cytoplasmic Merlin-to-LATS/YAP Hippo branch, so this PR adds a small model review and links NF2's accepted `signaling adaptor activity` / `hippo signaling` rows to it.
- Locations at the plasma membrane, nucleus/nucleoplasm, and cytoplasm are core. Junctional, ruffle/filopodial, perinuclear, nucleolar, early-endosome, and cytoskeletal phenotypes were kept as non-core where the evidence supports a real but contextual Merlin pool or downstream branch.

## 2026-11-22 reviewer follow-up
- Rechecked GO:0003779 after the first AI review: PMID:9537418 rules out the canonical ERM C-terminal actin-binding site only, while PMID:11329377 and PMID:11368764 support N-terminal/F-actin association by human Merlin, so the NF2 rows are kept non-core and the PAINT actin IRD request is dropped.
- Downgraded PAINT-only integrin binding, regulation of gliogenesis, and cell-shape calls to unresolved/undecided states; kept the ERM endosome-process pruning requests.
- Added explicit NEW rows for nuclear Merlin inhibition of CRL4(DCAF1) and negative regulation of protein ubiquitination, and retargeted the second core function to ubiquitin-protein transferase inhibitor activity.
- Replaced self-citations to same-PR family and GO-CAM prose with primary or stable source support, changed the tight-junction and spectrin-binding calls as requested, and corrected the Hippo contact-inhibition GO-CAM review.
