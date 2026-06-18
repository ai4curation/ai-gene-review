# P4HB PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P07237
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/P4HB/P4HB-ai-review.yaml](P4HB-ai-review.yaml)
- AIGR review HTML: present - [genes/human/P4HB/P4HB-ai-review.html](P4HB-ai-review.html)
- Gene notes: present - [genes/human/P4HB/P4HB-notes.md](P4HB-notes.md)
- GOA TSV: present - [genes/human/P4HB/P4HB-goa.tsv](P4HB-goa.tsv)
- UniProt record: present - [genes/human/P4HB/P4HB-uniprot.txt](P4HB-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/P4HB.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/P4HB.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HB.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HB.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: P4HB encodes protein disulfide-isomerase (PDI, also PDIA1), the prototypical and highly abundant thioredoxin-fold redox enzyme of the endoplasmic reticulum. It has an a-b-b'-a' domain architecture with two catalytically active thioredoxin-like (CGHC) active sites and a C-terminal KDEL ER-retention signal. As an enzyme it catalyzes the formation, breakage and rearrangement (isomerization) of disulfide bonds in nascent and misfolded proteins and can act as a thiol oxidase (with ERO1) or, at the cell surface, as a disulfide reductase. In a redox- and concentration-dependent manner it also functions as a molecular chaperone that suppresses aggregation of misfolded proteins (and at low concentration shows anti-chaperone activity). Beyond its catalytic roles, PDI is the non-catalytic beta-subunit of two ER enzyme complexes; it forms the alpha2beta2 prolyl 4-hydroxylase tetramer (with P4HA1/P4HA2) that hydroxylates proline in collagen, and it is the structural subunit of the microsomal triglyceride transfer protein (MTTP) complex, stabilizing and retaining both enzymes in the ER. It additionally regulates the unfolded-protein-response sensor IRE1/ERN1 (when phosphorylated by FAM20C) and has moonlighting roles at the cell surface and cytoskeleton (LGALS9 receptor, integrin and beta-actin binding, T-cell migration, viral entry). It localizes principally to the ER and ER lumen, with additional pools at the cell membrane, melanosome and cytoskeleton.
- Existing/core annotation action counts: ACCEPT: 25; KEEP_AS_NON_CORE: 72; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Notes, review YAML, and both PN mappings are consistent. P4HB is the prototypical PDI: review ACCEPTs GO:0003756 (EXP/IDA/IEA, the canonical core MF) and documents its dual structural-subunit roles (P4H beta-subunit; MTTP). No contradiction.
- **PN story / NEW pressure:** Row 1 GO:0003756 (OLS-verified) is already_in_goa_exact and ACCEPTed — captured. Row 2 GO:0032964 collagen biosynthetic process (OLS-verified real) is flagged new_to_goa. The review captures the collagen role via the **prolyl-4-hydroxylase axis**: GO:0004656 procollagen-proline 4-dioxygenase activity (contributes_to, IDA/TAS), GO:0016222 procollagen-proline 4-dioxygenase complex (part_of), GO:0018401 peptidyl-proline hydroxylation. These are more precise/mechanistic than GO:0032964 (a broad biosynthetic-process umbrella). So the PN's collagen story is biologically real and already mechanistically represented; GO:0032964 itself is a defensible (verified) but broader process-level addition. Conclusion: collagen role already captured at finer granularity; GO:0032964 is a legitimate-but-broader ADD, not strictly needed.
- **Evidence alignment:** PN dossier lists no reference titles; alignment is by biology. Review collagen evidence (PMID:7753822, PMID:2846539, both GOA-anchored to GO:0004656/GO:0016222) and PDI evidence (PMID:15720785, 21091435, 32149426) are reviewer-supplied; no shared citation list to compare.
- **Verdict:** Consistent; PDI core validated; collagen role real but already captured via finer P4H-complex terms, making GO:0032964 a broader optional addition. **Recommended edits:** [MAP] consider downgrading the ER-collagen-processing leaf projection (GO:0032964) to context/non-propagating for P4HB (it acts as the non-catalytic structural beta-subunit; the review's GO:0004656 contributes_to + GO:0016222 part_of are the more accurate, already-present representation).

## Full Consistency Review

- **UniProt:** P07237 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** 2 rows — (1) `ER proteostasis|Folding enzyme|Protein disulfide isomerases`; (2) `ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding`. **PN-node mapping:** PDI group=mapped→**GO:0003756 protein disulfide isomerase activity** (already_in_goa_exact); ER-collagen group=mapped→**GO:0032964 collagen biosynthetic process** (new_to_goa); classes/branch=no_mapping.
- **Consistency:** Notes, review YAML, and both PN mappings are consistent. P4HB is the prototypical PDI: review ACCEPTs GO:0003756 (EXP/IDA/IEA, the canonical core MF) and documents its dual structural-subunit roles (P4H beta-subunit; MTTP). No contradiction.
- **PN story / NEW pressure:** Row 1 GO:0003756 (OLS-verified) is already_in_goa_exact and ACCEPTed — captured. Row 2 GO:0032964 collagen biosynthetic process (OLS-verified real) is flagged new_to_goa. The review captures the collagen role via the **prolyl-4-hydroxylase axis**: GO:0004656 procollagen-proline 4-dioxygenase activity (contributes_to, IDA/TAS), GO:0016222 procollagen-proline 4-dioxygenase complex (part_of), GO:0018401 peptidyl-proline hydroxylation. These are more precise/mechanistic than GO:0032964 (a broad biosynthetic-process umbrella). So the PN's collagen story is biologically real and already mechanistically represented; GO:0032964 itself is a defensible (verified) but broader process-level addition. Conclusion: collagen role already captured at finer granularity; GO:0032964 is a legitimate-but-broader ADD, not strictly needed.
- **Mapping strategy:** Group-level GO:0003756 is the cleanest catalytic-family target (correctly already_in_goa_exact, matching AGR2/ERO1A/ERO1B/ERP27 siblings under the same node — but see the oxidase/non-catalytic caveats for those genes). For the collagen row, GO:0032964 is broader than the review's P4H-complex terms; per the TOMM20/HSPA8/RAB7A "broader-than-review" precedent it risks over-reaching the process when the review's structural-subunit framing (P4HB contributes_to, does not catalyze) is the more accurate model. Prefer the review's GO:0004656/GO:0016222 representation.
- **Evidence alignment:** PN dossier lists no reference titles; alignment is by biology. Review collagen evidence (PMID:7753822, PMID:2846539, both GOA-anchored to GO:0004656/GO:0016222) and PDI evidence (PMID:15720785, 21091435, 32149426) are reviewer-supplied; no shared citation list to compare.
- **Verdict:** Consistent; PDI core validated; collagen role real but already captured via finer P4H-complex terms, making GO:0032964 a broader optional addition. **Recommended edits:** [MAP] consider downgrading the ER-collagen-processing leaf projection (GO:0032964) to context/non-propagating for P4HB (it acts as the non-catalytic structural beta-subunit; the review's GO:0004656 contributes_to + GO:0016222 part_of are the more accurate, already-present representation).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/P4HB/P4HB-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: P07237
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: P07237
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032964 collagen biosynthetic process]
        rationale: This PN group contains ER factors dedicated to collagen maturation, processing, and folding. Collagen biosynthetic process captures the shared substrate-specific pathway context.
    - [class] ER proteostasis|Maturation and folding of specific substrates
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
