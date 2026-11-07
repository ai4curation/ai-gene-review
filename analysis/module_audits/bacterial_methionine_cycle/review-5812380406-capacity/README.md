# Additive capacity and source closure for review 5812380406

This supplement preserves the prior science and audit receipts and makes their supersession explicit. It does not claim that the previous full-corpus run validated these later changes.

The copied original checker passes all **47 cases, 9 mutations and 10 gate sensitivities** with exactly the prior biological expectations. Only its repository-depth and output-file paths changed. The extension adds **28 cases, 8 mutations and 4 classification sensitivities**: totals are **75 cases, 17 mutations and 14 sensitivities**. It uses the production compiler and satisfaction evaluator. For each restored AhcY, Pfs, MetH and MetE classification, a qualified member passes; masking classification, function, role, or source support fails. A synthetic same-family unreviewed protein cannot bypass the exact exemplar gate. Native flux remains unestablished. Removing a classification admits a deliberately unqualified witness, and replacing it with a wrong family rejects the independently grounded positive; both mutations are caught.

These controls preserve the original MesD/MesX, monoglutamate/polyglutamate, cofactor/input, same-organism, complete-route and noncanonical remethylation exclusions. Architecture is the independently curated member-role judgment used by the original oracle, not a new genome-wide sequence classifier. Synthetic negatives establish failure of evidence qualification, not biological absence. No family-wide catalytic grant is inferred from a family identifier.

`source-closure.json` contains **906 current input hashes**, 232 recursive citation edges, all 18 current member reviews, seven relevant family reviews, the module, the old publication-input union, and released artifacts/receipts. There are no missing cited local sources. The earlier 854-input freeze is retained: 14 scientific paths have explicit supersessions; the four shared project metadata files are separately observed and were HEAD-identical at capture. Their subsequent root-owned metadata update is outside this immutable scientific closure. No old receipt or checker has been rewritten. PTHR43794 and PTHR46015 have no family-review files; this is reported as an assessment limit, not filled with invented grants.

All **192 ordered source annotation payloads and four active historical NEW rows** match the published head. The 60 protected-path capture plus three ontology/classification observations represents **63 observations over 62 unique paths**, because `panther.obo` occurs in both lists. Every unique protected hash is unchanged.

The original 28-file follow-up manifest remains byte-identical. Root's focused schema check exposed five PTHR23420 provenance-only attachments lacking the schema-required quotation. With explicit authorization, only that family-review hash is superseded: its exact sealed bytes are archived in `PTHR23420-sealed-before.yaml`; the five old attachments are preserved in `family-attachment-supersession.json`. The topology source remains a top-level reference and is explained in notes; biological quotations remain. Node IDs, assertions, seeds, placement verdicts and scopes are unchanged. The other 27 sealed hashes are exact. The new helper history and single-family schema both pass.

Root normally fetched the previously absent bibliographic record PMID35289639; it is now included additively. Its normal cache is abstract-only. The already frozen publisher capture `literature-consultation/preflight/correction-35289639-web.json` identifies the byline and acknowledgment corrections. This is provenance for the authorship note, not new activity evidence. The neighboring failed XML acquisition is not counted as a successfully read full article. See `bibliographic-source-assessment.json`.

Reproduce without overwriting any old result:

```sh
.venv/bin/python -B analysis/module_audits/bacterial_methionine_cycle/review-5812380406-capacity/check_capacity.py
.venv/bin/python -B analysis/module_audits/bacterial_methionine_cycle/review-5812380406-capacity/extend_capacity.py
.venv/bin/python -B analysis/module_audits/bacterial_methionine_cycle/review-5812380406-capacity/check_closure.py
.venv/bin/ruff check --no-cache analysis/module_audits/bacterial_methionine_cycle/review-5812380406-capacity/*.py
```

No downloads, full-corpus validation, renders, commits, or shared metadata edits were performed by this supplement. Root owns final focused validation and publication.
