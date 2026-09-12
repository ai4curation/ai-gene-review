# DNAJC13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75165
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC13/DNAJC13-ai-review.yaml](DNAJC13-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC13/DNAJC13-ai-review.html](DNAJC13-ai-review.html)
- Gene notes: present - [genes/human/DNAJC13/DNAJC13-notes.md](DNAJC13-notes.md)
- GOA TSV: present - [genes/human/DNAJC13/DNAJC13-goa.tsv](DNAJC13-goa.tsv)
- UniProt record: present - [genes/human/DNAJC13/DNAJC13-uniprot.txt](DNAJC13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC13 (RME-8, "Required for receptor-mediated endocytosis 8") is a large (2243 aa) multidomain DnaJ/HSP40 subfamily C protein that acts as an endosomal co-chaperone of the HSC70 (HSPA8) chaperone. It is a peripheral membrane protein associated with early endosomes via its N-terminal region and carries an internal J domain (residues 1301-1366) that stimulates the ATPase activity of HSC70 to drive clathrin dynamics on endosomal membranes. Through this activity DNAJC13 regulates endosomal protein sorting and membrane trafficking, including transferrin recycling (early endosome to recycling endosome transport) and EGF/EGFR degradation (early endosome to late endosome transport). It binds the WASH complex subunit WASHC2/FAM21 and the sorting nexin SNX1, coordinating WASH complex activity with retromer-dependent endosomal membrane tubulation. DNAJC13 variants have been implicated in autosomal-dominant Parkinson disease (PARK21).
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Partial. PN frames DNAJC13 purely as a J-domain HSP70 cochaperone (GO:0030544). The review and notes agree it is an HSC70/HSPA8 co-chaperone whose internal J domain stimulates HSC70 ATPase to drive endosomal clathrin dynamics — so the cochaperone identity is consistent — but the review's center of gravity is the endosomal sorting biology (GO:0007032 endosome organization, GO:2001135, GO:2000641, GO:0071203 WASH complex). Notably the review chose GO:0001671 (ATPase activator activity) for core_functions, NOT GO:0030544, and GOA contains neither. So the specific Hsp70-binding claim is inferred, not directly annotated.
- **PN story / NEW pressure:** GO:0030544 is verified real. Relative to GOA (which has only bare GO:0005515 for protein binding among MF terms) this is `new_to_goa`, not `more_specific_than_existing_goa` as the PN label states. The cochaperone MF is biologically defensible (J domain + HSC70 binding, conserved from C. elegans), so GO:0030544 is a reasonable ADD — but the review's preferred GO:0001671 (ATPase activator activity) is the complementary/arguably more mechanistic MF. The distinctive endosomal-sorting biology is already well captured; no further NEW term needed.
- **Evidence alignment:** PN carries no titles; review anchors on PMID:18256511, 18307993, 24643499 (all verified) — endosomal/WASH/SNX1, none directly demonstrating Hsp70 binding (the cochaperone MF rests on UniProt + orthology). Divergence: PN emphasizes the (inferred) Hsp70 MF; literature emphasizes endosomal function.
- **Verdict:** Cochaperone identity consistent; GO:0030544 defensible but inferred. **Recommended edits:** [MAP] (minor) correct DNAJC13 projected `goa_status` to `new_to_goa`; optionally co-propagate GO:0001671 (ATPase activator activity) to match the review's core MF.

## Full Consistency Review

- **UniProt:** O75165 (RME-8) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (group/class/branch = no_mapping)
- **Consistency:** Partial. PN frames DNAJC13 purely as a J-domain HSP70 cochaperone (GO:0030544). The review and notes agree it is an HSC70/HSPA8 co-chaperone whose internal J domain stimulates HSC70 ATPase to drive endosomal clathrin dynamics — so the cochaperone identity is consistent — but the review's center of gravity is the endosomal sorting biology (GO:0007032 endosome organization, GO:2001135, GO:2000641, GO:0071203 WASH complex). Notably the review chose GO:0001671 (ATPase activator activity) for core_functions, NOT GO:0030544, and GOA contains neither. So the specific Hsp70-binding claim is inferred, not directly annotated.
- **PN story / NEW pressure:** GO:0030544 is verified real. Relative to GOA (which has only bare GO:0005515 for protein binding among MF terms) this is `new_to_goa`, not `more_specific_than_existing_goa` as the PN label states. The cochaperone MF is biologically defensible (J domain + HSC70 binding, conserved from C. elegans), so GO:0030544 is a reasonable ADD — but the review's preferred GO:0001671 (ATPase activator activity) is the complementary/arguably more mechanistic MF. The distinctive endosomal-sorting biology is already well captured; no further NEW term needed.
- **Mapping strategy:** Node mapping is acceptable for the cochaperone MF, but for DNAJC13 the propagated term arguably should pair GO:0030544 with GO:0001671 (the review's choice). The J domain is internal/non-canonical, but the cochaperone role is real, so this is not an over-reach like DNAJC11.
- **Evidence alignment:** PN carries no titles; review anchors on PMID:18256511, 18307993, 24643499 (all verified) — endosomal/WASH/SNX1, none directly demonstrating Hsp70 binding (the cochaperone MF rests on UniProt + orthology). Divergence: PN emphasizes the (inferred) Hsp70 MF; literature emphasizes endosomal function.
- **Verdict:** Cochaperone identity consistent; GO:0030544 defensible but inferred. **Recommended edits:** [MAP] (minor) correct DNAJC13 projected `goa_status` to `new_to_goa`; optionally co-propagate GO:0001671 (ATPase activator activity) to match the review's core MF.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC13/DNAJC13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: O75165
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
