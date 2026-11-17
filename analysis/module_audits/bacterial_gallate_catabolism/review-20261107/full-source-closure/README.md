# Additive Gallate publication and source closure

This receipt closes the current scoped scientific inputs of PR6158 against published baseline `f852d88b3b0cfe9f4658d879171b446a90dd6f1c`. It does not change science, source files, earlier receipts, renders or project metadata, and does not assert a new whole-corpus validation result.

The 305 current inputs unite the original 177-file full-validation publication manifest, the latest 202-file publication manifest, all `files` **and** `source_dependencies` from the three new handoffs, and recursive explicit source citations. The latest manifest has 197 nonshared inputs; five individually named shared project paths remain root-owned. All 197 nonshared manifest hashes were checked against the published Git blobs. The three historical provenance moves are byte-identical relocations. Every changed scientific/notes/HTML hash is authorized by the frozen science or render supersession receipts; no blanket changed-file exclusion is used. All 833 historical manifest/handoff hash assertions resolve to unchanged bytes or those exact authorized successors.

Coverage includes all 12 member/boundary-comparator reviews, all five relevant PANTHER reviews and their raw metadata/entries/PAINT files, module and notes, and the two PrpF reviews cited by a family review. The 12-panel baseline retains all 60 ordered source payloads and nine historical NEW rows, with no retirements. The extra PrpF records are source comparators, not added module members. References are followed through review/notes/scoped analysis and linked provider reports. Publication records and raw UniProt/PAINT records are terminal evidence inputs: their own bibliographies are not silently promoted to curation claims. There are 203 resolved citation edges and no explicit Reactome citation in this scope.

The 27 publication caches include four newly fetched **provider bibliography leads only**: PMID26867578, PMID21063756, PMID36724292 and PMID41024182. Their fetched titles and full-text flags are in `publication-access.json`; PMID21063756 is abstract-only. No new claim from any of these papers was adopted. The root's normal acquisition receipt is copied byte-for-byte into `provider-lead-fetch.json`.

The complete transitive provider bibliography is **not closed**: 24 citation occurrences, representing 21 distinct missing PMIDs, occur only in PrpF/methylcitrate provider reports reached through comparator links. `unresolved-provider-leads.json` names each occurrence. Their exact report bytes are included, but the missing papers are not represented as read or verified. Root explicitly accepted this boundary to avoid expanding Gallate into unrelated project literature. No missing citation used by the scoped curated reviews is excused by this rule.

Three failed BURL3 Falcon logs are now byte-identical durable copies under `provider-attempts/`; `aliases.json` resolves the original private note paths. No private cache path is required by the checker. The two private PMID21219457 publisher captures remain private. Existing bounded excerpt/provenance files support the claims actually used; those excerpts do not reconstruct the full captures and are not labeled byte-identical replacements. Original abstract-only publication and publisher provenance bytes are unchanged. Historical validation logs/private acquisition paths appearing inside old receipts remain provenance metadata, not new active evidence dependencies.

`capture.py` documents the scoped acquisition of manifests, graph and hashes; it refuses to regenerate after sealing. Run the read-only checker from the repository root:

```sh
.venv/bin/python -B analysis/module_audits/bacterial_gallate_catabolism/review-20261107/full-source-closure/check.py
```

The checker verifies current hashes, every exact supersession, all declared citation targets, preserved source payload/order/NEW lifecycle, provider bibliography limits, and the seal when present. It does not rewrite output files. Ruff and checker results are recorded separately. Root retains responsibility for project metadata, staging, publication and any final integration validation.
