# Notes for DANRE ak2

- Core function is mitochondrial intermembrane-space adenylate kinase activity [file:DANRE/ak2/ak2-uniprot.txt "Reaction=AMP + ATP = 2 ADP;"].
- Hematopoietic and leukocyte differentiation terms are kept as non-core because they are developmental consequences of AK2 deficiency [PMID:19043417 "Knockdown of zebrafish ak2 also leads to aberrant leukocyte development"].

## Re-review 2026-09-29

- Resolved the 8 remaining PENDING rows. GO:0004017 AMP kinase activity (IBA) ACCEPT as the core molecular function (family node PTN000599576; conserved CORE/NMPbind/LID architecture and ATP/AMP binding residues; EC 2.7.4.3 reaction) [file:DANRE/ak2/ak2-uniprot.txt "Reaction=AMP + ATP = 2 ADP;"].
- GO:0005737 cytoplasm (IBA) MODIFY to GO:0005758 mitochondrial intermembrane space: the family node includes cytosolic AK1-type members so cytoplasm is correct at the node, but the AK2 subfamily is intermembrane-space localised [file:DANRE/ak2/ak2-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion intermembrane space"]. Added propagation_review (TERM_SCOPING_PROBLEM / COMPARTMENT_OR_COMPLEX_MISMATCH).
- The six duplicate ZFIN IMP rows (GO:0002244 hematopoietic progenitor cell differentiation, GO:0060218 hematopoietic stem cell differentiation) KEEP_AS_NON_CORE, consistent with their already-reviewed twins. Full text (PMID:26150473) shows HSPC specification is preserved (near-normal c-myb/runx1 at 30-36 hpf) while maturation/maintenance fails, with increased oxidative stress/apoptosis rescued by antioxidants [PMID:26150473 "AK2 deficiency induces a wide array of hematopoietic defects"; PMID:26150473 "increased AMP/ADP ratio"]. This is a downstream metabolic requirement, not participation in differentiation.
- Rewrote the top-level description as standalone biology (removed curation commentary). Added reference_review blocks to PMID:26150473 (HIGH/VERIFIED, full text) and PMID:19043417 (HIGH/VERIFIED, abstract-only). Validation passes with zero errors.
