# Bcep18194_C7570: evidence review

2026-11-06 annotation-reviewer consultation. Identity: Q39LQ2, Burkholderia lata strain 383 / ATCC 17760, NCBITaxon:482957. Locus, strain aliases and accession are taken from the frozen UniProt record.

Q39LQ2 maps to PTHR21240:SF28 and PF04909. That establishes membership, not a substrate assignment from the surprising family label. The published gene neighborhood supports a LigJ-like candidate. Broad hydro-lyase activity is retained; KCH-specific and OMA-isomer-specific assertions are withheld. A module test requiring exact KCH hydration must not count this member solely because its family matches.

The 2011 publisher full text (https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2010.07448.x) includes strain 383 in the comparative cluster panel and reports native gallate growth. This is not a target-protein assay. The dated excerpt and figure mapping are preserved in `modules/bacterial_gallate_catabolism-source-analysis/PMID21219457-evidence-notes.md`. Published experimental results for other species remain comparative evidence.

Evidence quotations and provenance:

- [file:BURL3/Bcep18194_C7570/Bcep18194_C7570-uniprot.txt] `DR   PANTHER; PTHR21240:SF28; ISO-OROTATE DECARBOXYLASE (EUROFUNG); 1.`
- [file:BURL3/Bcep18194_C7570/Bcep18194_C7570-uniprot.txt] `DR   Pfam; PF04909; Amidohydro_2; 1.`

Search and retrieval: exact locus/accession searches on 2026-11-06 returned no indexed results establishing a target-specific biochemical assay. A genuine `just deep-research BURL3 Bcep18194_C7570 --provider falcon` attempt failed with HTTP 403 authentication failure; no provider report was produced or fabricated. The command and error are retained under `.cache/module-audit-logs/gallate-20261106/BURL3-C7570-falcon.log`. Manual review used the frozen UniProt classification, publisher PMID:21219457 and the cited comparative papers.

All original annotation rows, order, source terms, evidence codes, references, qualifiers and supporting entities are preserved. No NEW annotation rows were manufactured. Ontology definitions were checked against the official QuickGO response in `analysis/module_audits/bacterial_gallate_catabolism/burkholderia-consultation.ontology.json`.


## 2026-11-07 PR6158 follow-up

Removed the growth phenotype from localization and chemical-class assessments. Added the independently verified comparative LigJ-like neighborhood excerpt only where relevant. Retained carboxy-lyase/hydrolase MARK_AS_OVER_ANNOTATED: the unassayed target lacks the direct product evidence available for SYK-6 LigJ, and an inferred sibling chemistry is not an exclusion assay. Core hydro-lyase specificity remains bounded.

No annotation payload, row order, inherited NEW action, raw/provider artifact or existing publication cache was altered. No additional NEW rows were added. Focused validation, render and helper-history results are recorded in the round1-gene-review handoff.
