# CYB5R4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q7L1T6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CYB5R4/CYB5R4-ai-review.yaml](CYB5R4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CYB5R4/CYB5R4-ai-review.html](CYB5R4-ai-review.html)
- Gene notes: present - [genes/human/CYB5R4/CYB5R4-notes.md](CYB5R4-notes.md)
- GOA TSV: present - [genes/human/CYB5R4/CYB5R4-goa.tsv](CYB5R4-goa.tsv)
- UniProt record: present - [genes/human/CYB5R4/CYB5R4-uniprot.txt](CYB5R4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CYB5R4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CYB5R4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CYB5R4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CYB5R4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CYB5R4 (NADH-cytochrome b5 reductase 4; also known as NCB5OR or b5+b5R) is a multidomain, soluble flavohemoprotein and NAD(P)H-dependent oxidoreductase. It contains an N-terminal CS/Hsp20 (p23-like) domain, a cytochrome b5-like heme-binding domain (with axial His-89 and His-112 ligating a six-coordinate low-spin heme) joined by a long hinge to a C-terminal FAD-dependent cytochrome-b5-reductase (FNR-type FAD- and NAD-binding) module. It binds stoichiometric heme and FAD and catalyzes EC 1.6.2.2 (NADH:cytochrome b5 oxidoreductase), reducing electron acceptors including cytochrome b5, cytochrome c, methemoglobin and ferricyanide; unlike the classical single-domain cytochrome b5 reductase it lacks a membrane anchor. The protein localizes to the endoplasmic reticulum and perinuclear cytoplasm. It functions in the response to oxidative and endoplasmic reticulum stress, protecting cells (notably pancreatic beta cells) from excess reactive oxygen species; loss of the orthologous gene in mice causes diabetes and lipoatrophy. Although early work proposed it as an NAD(P)H oxidase / candidate oxygen sensor, subsequent enzymology showed it preferentially reduces substrates rather than transferring electrons to molecular oxygen and is not an efficient superoxide-generating oxidase.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 4; NEW: 2; REMOVE: 3

## PN Consistency Summary

- **Consistency:** CONTRADICTION. The review's entire biology is an NAD(P)H-cytochrome b5 reductase / soluble ER flavohemoprotein (EC 1.6.2.2; heme + FAD binding; ROS/ER-stress protection). It contains an N-terminal CS/Hsp20-like (p23_NCB5OR) domain — the basis for the PN "HSP90 cochaperone, CS domain containing" placement — but the review, GOA, and notes contain ZERO Hsp90-binding or cochaperone evidence; the notes explicitly raise "how does the CS domain contribute to function" as an open question. The PN classification is a domain-architecture heuristic, not evidence.
- **PN story / NEW pressure:** PN asserts an HSP90-cochaperone role absent from existing GO. GO:0051879 Hsp90 protein binding is a real term (verified OLS), but there is no experimental support that CYB5R4 binds Hsp90; the InterPro "HSP20-like chaperone" CS-domain signature is structural homology only. Conclusion: **over-reaches** — propagating GO:0051879 onto CYB5R4 would be a speculative domain-based annotation contradicting the curated redox-enzyme function. Not a defensible ADD.
- **Evidence alignment:** No overlap. PN dossier lists no reference titles; review evidence (PMID:10611283, PMID:15131110) is entirely redox/localization. No paper supports the Hsp90 link.
- **Verdict:** Inconsistent — PN HSP90-cochaperone placement / GO:0051879 over-reaches and is unsupported by the review. **Recommended edits:** [MAP] exclude CYB5R4 from GO:0051879 Hsp90 protein binding propagation (CS/p23 domain is structural-homology only; no Hsp90-binding evidence); flag the PN "HSP90 cochaperone" classification as domain-based, not functional. [REF] none.

## Full Consistency Review

- **UniProt:** Q7L1T6 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CS domain containing` ; **PN-node mapping:** type (HSP90 cochaperone)=mapped, scope=ok_for_propagation_to_go, GO:0051879 Hsp90 protein binding (subtype/group/class/branch = no_mapping)
- **Consistency:** CONTRADICTION. The review's entire biology is an NAD(P)H-cytochrome b5 reductase / soluble ER flavohemoprotein (EC 1.6.2.2; heme + FAD binding; ROS/ER-stress protection). It contains an N-terminal CS/Hsp20-like (p23_NCB5OR) domain — the basis for the PN "HSP90 cochaperone, CS domain containing" placement — but the review, GOA, and notes contain ZERO Hsp90-binding or cochaperone evidence; the notes explicitly raise "how does the CS domain contribute to function" as an open question. The PN classification is a domain-architecture heuristic, not evidence.
- **PN story / NEW pressure:** PN asserts an HSP90-cochaperone role absent from existing GO. GO:0051879 Hsp90 protein binding is a real term (verified OLS), but there is no experimental support that CYB5R4 binds Hsp90; the InterPro "HSP20-like chaperone" CS-domain signature is structural homology only. Conclusion: **over-reaches** — propagating GO:0051879 onto CYB5R4 would be a speculative domain-based annotation contradicting the curated redox-enzyme function. Not a defensible ADD.
- **Mapping strategy:** The HSP90-cochaperone type→GO:0051879 mapping may be reasonable for canonical CS-domain HSP90 cochaperones, but CYB5R4 is a poor exemplar (a redox enzyme that happens to carry a p23-like domain). The node mapping itself is not necessarily wrong family-wide, but this gene should NOT inherit GO:0051879. Recommend de-coupling CYB5R4 from the HSP90-cochaperone propagation (treat the CS domain as a non-canonical/standalone module).
- **Evidence alignment:** No overlap. PN dossier lists no reference titles; review evidence (PMID:10611283, PMID:15131110) is entirely redox/localization. No paper supports the Hsp90 link.
- **Verdict:** Inconsistent — PN HSP90-cochaperone placement / GO:0051879 over-reaches and is unsupported by the review. **Recommended edits:** [MAP] exclude CYB5R4 from GO:0051879 Hsp90 protein binding propagation (CS/p23 domain is structural-homology only; no Hsp90-binding evidence); flag the PN "HSP90 cochaperone" classification as domain-based, not functional. [REF] none.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CYB5R4/CYB5R4-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CS domain containing
- UniProt: Q7L1T6
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CS domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family/domain/subtype label. It classifies PN members but is not itself a GO annotation target; any functional assertion should come from a parent role mapping or gene-specific review.
    - [type] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051879 Hsp90 protein binding]
        rationale: This PN type groups HSP90 cochaperones. Hsp90 protein binding is the most defensible shared GO molecular-function target for propagation.
    - [group] Cytonuclear proteostasis|Chaperone|HSP90 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
