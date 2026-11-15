# Burkholderia strain 383 annotation-reviewer consultation

Completed 2026-11-06 using the repository annotation-reviewer skill. Scope is the three newly seeded BURL3 candidates; no module, family, shared tracker, validator, publication cache, commit or push was changed by this consultation.

| Protein | Seed rows and decisions | Supported core and boundary |
| --- | --- | --- |
| Q39LQ0 / Bcep18194_C7572 | Ferrous iron binding ACCEPT; oxidoreductase, dioxygenase parent and PCA 4,5-dioxygenase rows MODIFY to gallate dioxygenase | Paired gallate-dioxygenase domains IPR034939/IPR034940 and NF009904 support the gallate-family inference. The unchecked submitter PCA name/EC is insufficient to outweigh these classifications. No target kinetics or strict substrate exclusion is asserted. |
| Q39LQ2 / Bcep18194_C7570 | Cytoplasm ACCEPT; hydrolase and carboxy-lyase MARK_AS_OVER_ANNOTATED; secondary metabolism MODIFY to gallate catabolism; exact OMA hydratase MODIFY to hydro-lyase | PTHR21240:SF28 and amidohydrolase-related fold establish membership. Cluster context supports a LigJ-like candidate, but KCH versus OMA-isomer specificity remains unresolved. Fold labels do not establish hydrolysis or decarboxylation. |
| Q39LQ3 / Bcep18194_C7569 | GO:0047443 ACCEPT | TIGR02798 and the CHA-aldolase FunFam support the inferred CHA cleavage activity independently of ARBA. The current GO definition explicitly includes CHA cleavage despite its HMG short name. Extra HMG turnover or oxaloacetate decarboxylation is not asserted as measured target activity. |

The [2011 primary paper](https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2010.07448.x) was inspected through the publisher full text. Its strain 383 growth result and comparative cluster mapping support physiological context, not direct assays of these three proteins. Root's dated evidence transcription is `modules/bacterial_gallate_catabolism-source-analysis/PMID21219457-evidence-notes.md`. The original abstract cache remains unchanged. Comparative DesB and LigK assays are explicitly assigned to their actual species in the gene reference assessments.

No NEW rows were needed. All ten seed rows retain their original order and every non-review payload field, and all six raw files match their frozen hashes. Reviews now have evidence-backed descriptions, core functions, questions, experiments and notes. The standard helper added 33 record-section values with no mismatch or unplaceable quote.

Three genuine Falcon attempts failed with HTTP 403 authentication errors. No provider report was created or fabricated. Exact locus/accession web queries yielded no target-specific biochemical evidence; manual source review and the failed attempts are documented in each gene's notes.

Three focused gene validations, three renders and three generated history validations passed. Two nonblocking warnings identify the gallate-process core terms in Q39LQ0 and Q39LQ3 without corresponding annotation rows; these were not silenced by manufacturing process proposals.

Matching limit: the production GO function predicate accepts GO:0016836 against the same generic hydro-lyase ID. It cannot thereby establish KCH specificity. Q39LQ2 must remain outside a complete-route claim unless the module's independent evidence/chemistry checks establish that specificity. This consultation reproduced the generic-ID match and the failure to infer the more specific GO:0047584 from it; it did not run module capacity or full-repository validation. Root owns those checks.

Machine-readable preservation and check proof: `burkholderia-consultation.json`. Official QuickGO response: `burkholderia-consultation.ontology.json`. Cache handoff: `.cache/module-audit-logs/gallate-20261106/burkholderia-handoff.json`.
