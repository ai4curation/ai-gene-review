# mfsd2aa (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: mfsd2aa encodes a sodium-dependent lysophospholipid/lysophosphatidylcholine symporter at endothelial plasma membrane and ER membrane, supporting lipid transport across the blood-brain barrier. Free fatty-acid and carbohydrate transport annotations are treated cautiously because the supported substrate is lysophospholipid/LPC, not free fatty acid or carbohydrate.
- Key UniProt support: Sodium-dependent lysophosphatidylcholine (LPC) symporter.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.

## Re-review 2026-09-29

All 23 rows rewritten with primary-literature support; the previous review quoted the same UniProt FUNCTION line under every term, including localization terms. Two new full-text references were cached and cited: PMID:34349262 (mouse MFSD2A cryo-EM structure, sodium site) and PMID:36848557 (direct flippase assay).

Re-adjudicated actions:
- GO:0015245 fatty acid transmembrane transporter activity (IBA): MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0051978. The cargo is LPC, not a free fatty acid [file:DANRE/mfsd2aa/mfsd2aa-uniprot.txt "Does not transport docosahexaenoic acid in unesterified fatty acid."], and the zebrafish protein itself was assayed on LPC ligands [PMID:26005868 "both mfsd2aa and mfsd2ab exhibit similar transport activity of LPC ligands, and to a similar level as human MFSD2A"]. propagation_review added (TERM_SCOPING_PROBLEM / ROLE_CONFLATION on PTN002602210).
- GO:0015908 fatty acid transport (IBA and ISS): MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0051977, same argument, kept consistent across both evidence codes.
- GO:0008643 carbohydrate transport (IEA, InterPro IPR039672): MARK_AS_OVER_ANNOTATED -> REMOVE. IPR039672 is the "Lactose permease-like" family entry built on bacterial sodium:galactoside symporters; the sugar cargo comes from that family, not from any Mfsd2a assay. This is a wrong electronic mapping rather than an over-broad one.
- GO:0016020 membrane (IEA): REMOVE -> MODIFY to GO:0005886 + GO:0005789. The protein is genuinely an integral membrane protein; the root term is uninformative, not false, and the specific compartments are already annotated.
- GO:0045056 transcytosis (ISS from mouse Q9DA75): KEEP_AS_NON_CORE -> MODIFY to GO:1904299 negative regulation of transcytosis. Mfsd2a suppresses rather than performs transcytosis, and the zebrafish mutant shows the sign directly [PMID:31429822 "Mfsd2aa mutants exhibit increased transcytosis."; "mfsd2aa mutants have increased vesicular densities"]. propagation_review records REGULATORY_SIGN_INVERSION.
- GO:1905603 regulation of blood-brain barrier permeability (IMP): KEEP_AS_NON_CORE -> ACCEPT. The evidence is a germline mfsd2aa mutant with a paralog-resolved phenotype [PMID:31429822 "Mfsd2aa mutants displayed at least a two-fold increase in midbrain and hindbrain parenchymal tracer leakage"; "mfsd2ab mutants displayed similarly low levels of parenchymal tracer intensity to wild-type controls at 5 dpf"], stronger than the morphant row it was ranked below.
- GO:0005789 endoplasmic reticulum membrane (IEA): ACCEPT -> KEEP_AS_NON_CORE. The ER pool is an ortholog-derived inference with no functional data in zebrafish; all measured activity is at the cell surface.
- GO:0140329 lysophospholipid translocation (IBA) retained as ACCEPT, now supported by direct biochemistry rather than paraphrase [PMID:36848557 "we demonstrate that Mfsd2a flips LPS from the outer to the inner leaflet of a membrane bilayer in a sodium-dependent manner"].
- Description rewritten as standalone biology (the previous text contained curation commentary about annotations being "treated cautiously"); core_functions expanded to two entries (transport; barrier determination) and suggested_questions/experiments populated.
