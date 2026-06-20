# FKBP8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q14318
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FKBP8/FKBP8-ai-review.yaml](FKBP8-ai-review.yaml)
- AIGR review HTML: present - [genes/human/FKBP8/FKBP8-ai-review.html](FKBP8-ai-review.html)
- Gene notes: present - [genes/human/FKBP8/FKBP8-notes.md](FKBP8-notes.md)
- GOA TSV: present - [genes/human/FKBP8/FKBP8-goa.tsv](FKBP8-goa.tsv)
- UniProt record: present - [genes/human/FKBP8/FKBP8-uniprot.txt](FKBP8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FKBP8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FKBP8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBP8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBP8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: FKBP8 (FKBP38) is a membrane-anchored member of the FKBP immunophilin family. It has a single FKBP-type peptidyl-prolyl cis-trans isomerase (PPIase) domain, three tetratricopeptide (TPR) repeats, and a C-terminal transmembrane helix that anchors it as a tail-anchored, single-pass protein in the mitochondrial outer membrane with its catalytic domain facing the cytoplasm. Unlike other FKBPs, its PPIase activity is constitutively inactive and is switched on by binding calmodulin in a Ca2+-dependent manner. FKBP8 acts as a chaperone that recruits the anti-apoptotic protein BCL2 to mitochondria and modulates its phosphorylation, thereby regulating apoptosis, and it functions as a mitophagy receptor/adaptor that engages BNIP3 and the LC3/GABARAP autophagy machinery to promote selective clearance of mitochondria. It also contributes to chaperone relays (e.g. axonemal dynein assembly), restricts influenza A virus infection, binds HSP90, and has been implicated in mTOR and Hedgehog/Smoothened signaling. It is regulated by PRKN-mediated ubiquitination (degraded during mitophagy) and USP30 deubiquitination.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 28; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Notes, review YAML, and all three PN mappings are mutually consistent. The review captures the full dual-role membrane-FKBP picture: conditional Ca2+/CaM-activated PPIase (GO:0003755, ACCEPT), HSP90 co-chaperone (multiple protein-binding rows MODIFY→GO:0051879), and mitophagy receptor (GO:1901524 ACCEPT x2). No contradiction.
- **PN story / NEW pressure:** All three PN molecular roles are already in GOA/review. GO:0051879 (OLS-verified) is correctly "more_specific" — the review independently proposes it via MODIFY of HSP90 protein-binding rows. GO:0003755 is already_in_goa_exact (review ACCEPT, IEA). Mitophagy: PN maps GO:0000423 (mitophagy, verified real) but the review and GOA carry **GO:1901524 regulation of mitophagy** (IDA x2, PMID:28381481/31908024), not GO:0000423 itself — PN flags this honestly as supported_by_goa_regulation (FKBP8 is a receptor that *regulates*, rather than *is*, mitophagy). Nothing to ADD; all captured.
- **Evidence alignment:** PN row-3 titles ("FKBP8 recruits LC3A to mediate Parkin-independent mitophagy" = PMID:28381481; "Selective Autophagy: ATG8…LIR…Cargo Receptors") overlap the review's mitophagy anchors (PMID:28381481 cited; PMID:31908024 added). Strong overlap on mitophagy; PN does not surface the HSP90/dynein-relay (PMID:29916806) or CaM-activation (PMID:20707607) evidence the review adds — enrichment, not conflict.
- **Verdict:** Consistent; all PN molecular roles captured; only nuance is mitophagy process (GO:0000423) vs regulation (GO:1901524) granularity. **Recommended edits:** [MAP] optionally retarget the Mitophagy-receptor leaf projection from GO:0000423 to GO:1901524 regulation of mitophagy to match FKBP8's experimental (IDA) evidence and the review.

## Full Consistency Review

- **UniProt:** Q14318 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** 3 rows — (1) `Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain containing`; (2) `Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type`; (3) `Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy`. **PN-node mapping:** HSP90-cochaperone type=mapped→**GO:0051879 Hsp90 protein binding** (more_specific_than_existing_goa); PPIase group/type=mapped→**GO:0003755 PPIase activity** (already_in_goa_exact); Mitophagy type=mapped→**GO:0000423 mitophagy** (supported_by_goa_regulation); subtype/class/group/branch=no_mapping.
- **Consistency:** Notes, review YAML, and all three PN mappings are mutually consistent. The review captures the full dual-role membrane-FKBP picture: conditional Ca2+/CaM-activated PPIase (GO:0003755, ACCEPT), HSP90 co-chaperone (multiple protein-binding rows MODIFY→GO:0051879), and mitophagy receptor (GO:1901524 ACCEPT x2). No contradiction.
- **PN story / NEW pressure:** All three PN molecular roles are already in GOA/review. GO:0051879 (OLS-verified) is correctly "more_specific" — the review independently proposes it via MODIFY of HSP90 protein-binding rows. GO:0003755 is already_in_goa_exact (review ACCEPT, IEA). Mitophagy: PN maps GO:0000423 (mitophagy, verified real) but the review and GOA carry **GO:1901524 regulation of mitophagy** (IDA x2, PMID:28381481/31908024), not GO:0000423 itself — PN flags this honestly as supported_by_goa_regulation (FKBP8 is a receptor that *regulates*, rather than *is*, mitophagy). Nothing to ADD; all captured.
- **Mapping strategy:** Three leaf mappings, all defensible and gene-appropriate; ancestors correctly no_mapping (TOMM20/HSPA8-style umbrella restraint). One nuance: the Mitophagy-receptor leaf projects GO:0000423 (the process), whereas FKBP8's experimental evidence is for the *regulation* term GO:1901524. supported_by_goa_regulation captures this, but if the projection is meant to land an annotation, GO:1901524 is the better-supported target.
- **Evidence alignment:** PN row-3 titles ("FKBP8 recruits LC3A to mediate Parkin-independent mitophagy" = PMID:28381481; "Selective Autophagy: ATG8…LIR…Cargo Receptors") overlap the review's mitophagy anchors (PMID:28381481 cited; PMID:31908024 added). Strong overlap on mitophagy; PN does not surface the HSP90/dynein-relay (PMID:29916806) or CaM-activation (PMID:20707607) evidence the review adds — enrichment, not conflict.
- **Verdict:** Consistent; all PN molecular roles captured; only nuance is mitophagy process (GO:0000423) vs regulation (GO:1901524) granularity. **Recommended edits:** [MAP] optionally retarget the Mitophagy-receptor leaf projection from GO:0000423 to GO:1901524 regulation of mitophagy to match FKBP8's experimental (IDA) evidence and the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/FKBP8/FKBP8-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CC-TPR and PPIase domain containing
- UniProt: Q14318
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed HSP90 cochaperone subtype with FKBP/PPIase-like members. The parent HSP90-cochaperone mapping captures the shared HSP90-binding role; a subtype-level PPIase mapping would overstate the activity for all members.
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

## PN row 2: Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | FKBP type
- UniProt: Q14318
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes FKBP-family peptidyl-prolyl isomerases. The matching GO molecular-function term is appropriate for propagation.
    - [group] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the cytonuclear peptidyl-prolyl isomerase branch. The matching GO molecular-function term is appropriate for propagation.
    - [class] Cytonuclear proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 3: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: Q14318
- In branches: CY, ALP
- Notes: Receptor for selective autophagy. FKBP8 efficiently recruits lipidated LC3A to damaged mitochondria in a LIR-dependent manner. Mediate Parkin independent mitophagy. Can escape from mitochondria to avoid degradation during mitophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - FKBP8 recruits LC3A to mediate Parkin-independent mitophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN path denotes selective-autophagy receptors for mitochondrial cargo. The source category is a mechanistic sub-role within mitophagy, so propagation rather than exact equivalence is the correct scope.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
