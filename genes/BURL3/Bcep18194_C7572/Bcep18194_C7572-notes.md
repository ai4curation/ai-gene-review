# Bcep18194_C7572: evidence review

2026-11-06 annotation-reviewer consultation. Identity: Q39LQ0, Burkholderia lata strain 383 / ATCC 17760, NCBITaxon:482957. Locus, strain aliases and accession are taken from the frozen UniProt record.

Q39LQ0 has paired gallate-dioxygenase domains IPR034939/IPR034940 and NCBIfam NF009904. The imported protocatechuate name/EC is not independent functional evidence. The gallate assignment is a homology/context inference; no strict substrate exclusion, kinetic value or native gene-specific phenotype is transferred from DesB.

The 2011 publisher full text (https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2010.07448.x) includes strain 383 in the comparative cluster panel and reports native gallate growth. This is not a target-protein assay. The dated excerpt and figure mapping are preserved in `modules/bacterial_gallate_catabolism-source-analysis/PMID21219457-evidence-notes.md`. Published experimental results for other species remain comparative evidence.

Evidence quotations and provenance:

- [file:BURL3/Bcep18194_C7572/Bcep18194_C7572-uniprot.txt] `DR   InterPro; IPR034940; Gallate_dioxygenase_C.`
- [file:BURL3/Bcep18194_C7572/Bcep18194_C7572-uniprot.txt] `DR   InterPro; IPR034939; Gallate_Doxase_N.`
- [file:BURL3/Bcep18194_C7572/Bcep18194_C7572-uniprot.txt] `DR   NCBIfam; NF009904; PRK13367.1; 1.`

Search and retrieval: exact locus/accession searches on 2026-11-06 returned no indexed results establishing a target-specific biochemical assay. A genuine `just deep-research BURL3 Bcep18194_C7572 --provider falcon` attempt failed with HTTP 403 authentication failure; no provider report was produced or fabricated. The command and error are retained under `.cache/module-audit-logs/gallate-20261106/BURL3-C7572-falcon.log`. Manual review used the frozen UniProt classification, publisher PMID:21219457 and the cited comparative papers.

All original annotation rows, order, source terms, evidence codes, references, qualifiers and supporting entities are preserved. No NEW annotation rows were manufactured. Ontology definitions were checked against the official QuickGO response in `analysis/module_audits/bacterial_gallate_catabolism/burkholderia-consultation.ontology.json`.


## 2026-11-07 PR6158 follow-up

Removed whole-strain growth quotes from molecular-function refinements while retaining domain/signature and comparator mechanistic evidence. Scoped growth remains physiological context for the inferred pathway role, not a direct enzyme or specificity assay. New publisher-excerpt provenance is shared under C7570 source analysis.

No annotation payload, row order, inherited NEW action, raw/provider artifact or existing publication cache was altered. No additional NEW rows were added. Focused validation, render and helper-history results are recorded in the round1-gene-review handoff.

## 2026-11-07 — PR6158 boundary and provenance follow-up

Family/domain and cluster evidence plus whole-strain growth support a qualified gallate-process core, not a target-specific pathway assay or exact intermediate assignment. An inferred core does not mandate a manufactured NEW annotation merely to remove a coverage warning. All three BURL3 candidates use this policy. C7570's original secondary-metabolism classification is now UNDECIDED because the GO definition permits unusual nutrients but target evidence does not resolve that classification; its prior lateral replacement was withdrawn. No new rows or loss claims were added.
