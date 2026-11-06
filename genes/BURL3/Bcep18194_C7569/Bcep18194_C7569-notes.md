# Bcep18194_C7569: evidence review

2026-11-06 annotation-reviewer consultation. Identity: Q39LQ3, Burkholderia lata strain 383 / ATCC 17760, NCBITaxon:482957. Locus, strain aliases and accession are taken from the frozen UniProt record.

TIGR02798, the CHA-aldolase FunFam and PTHR33254:SF16 support a LigK/GalC-family candidate independently of ARBA. Current QuickGO GO:0047443 explicitly includes CHA cleavage, so the short HMG label is not a reason to reject the term or invent a redundant CHA term. Extra HMG kinetics and oxaloacetate decarboxylation are not target-specific claims.

The 2011 publisher full text (https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2010.07448.x) includes strain 383 in the comparative cluster panel and reports native gallate growth. This is not a target-protein assay. The dated excerpt and figure mapping are preserved in `modules/bacterial_gallate_catabolism-source-analysis/PMID21219457-evidence-notes.md`. Published experimental results for other species remain comparative evidence.

Evidence quotations and provenance:

- [file:BURL3/Bcep18194_C7569/Bcep18194_C7569-uniprot.txt] `DR   NCBIfam; TIGR02798; ligK_PcmE; 1.`
- [file:BURL3/Bcep18194_C7569/Bcep18194_C7569-uniprot.txt] `DR   FunFam; 3.50.30.40:FF:000002; 4-carboxy-4-hydroxy-2-oxoadipate aldolase/oxaloacetate decarboxylase; 1.`
- [file:BURL3/Bcep18194_C7569/Bcep18194_C7569-uniprot.txt] `DR   PANTHER; PTHR33254:SF16; BLR3842 PROTEIN; 1.`

Search and retrieval: exact locus/accession searches on 2026-11-06 returned no indexed results establishing a target-specific biochemical assay. A genuine `just deep-research BURL3 Bcep18194_C7569 --provider falcon` attempt failed with HTTP 403 authentication failure; no provider report was produced or fabricated. The command and error are retained under `.cache/module-audit-logs/gallate-20261106/BURL3-C7569-falcon.log`. Manual review used the frozen UniProt classification, publisher PMID:21219457 and the cited comparative papers.

All original annotation rows, order, source terms, evidence codes, references, qualifiers and supporting entities are preserved. No NEW annotation rows were manufactured. Ontology definitions were checked against the official QuickGO response in `analysis/module_audits/bacterial_gallate_catabolism/burkholderia-consultation.ontology.json`.
