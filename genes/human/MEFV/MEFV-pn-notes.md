# MEFV PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O15553
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MEFV/MEFV-ai-review.yaml](MEFV-ai-review.yaml)
- AIGR review HTML: missing - genes/human/MEFV/MEFV-ai-review.html
- Gene notes: present - [genes/human/MEFV/MEFV-notes.md](MEFV-notes.md)
- GOA TSV: present - [genes/human/MEFV/MEFV-goa.tsv](MEFV-goa.tsv)
- UniProt record: present - [genes/human/MEFV/MEFV-uniprot.txt](MEFV-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MEFV.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MEFV.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MEFV.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MEFV.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MEFV encodes pyrin (also called marenostrin or TRIM20), a cytosolic innate-immune protein expressed predominantly in myeloid/granulocytic cells. Pyrin has an N-terminal PYRIN (PYD/DAPIN) domain, a central B-box-type zinc finger and coiled-coil region, and a C-terminal B30.2/SPRY (PRY-SPRY) domain; it belongs to the tripartite-motif (TRIM) family (TRIM20). Pyrin functions as an inflammasome sensor that detects pathogen-driven inactivation of the small GTPase RhoA. In the resting state, RhoA-activated kinases PKN1/PKN2 phosphorylate pyrin (Ser208/Ser242), creating docking sites for inhibitory 14-3-3 proteins that keep pyrin inactive. Loss of RhoA activity (e.g. by bacterial toxins/effectors) dephosphorylates pyrin, releases 14-3-3, and triggers assembly of the pyrin inflammasome: pyrin nucleates PYCARD/ASC speck (pyroptosome) formation through PYD-PYD interactions, activating caspase-1 and driving maturation of IL-1beta and IL-18 and pyroptotic cell death. Pyrin inflammasome activation in wild-type cells requires intact microtubules. Beyond this sensor role, pyrin also acts as a selective-autophagy receptor ("precision autophagy"): it serves as a platform that recruits ULK1, Beclin-1/BECN1, ATG16L1 and ATG8/LC3-family proteins to target inflammasome components (NLRP3, NLRP1, pro-caspase-1) for autophagic degradation, thereby restraining excessive IL-1beta/IL-18-driven inflammation. Pyrin localizes to the cytoplasm and cytoskeleton, associating with microtubules and actin filaments (perinuclear filaments, leading-edge ruffles/lamellipodia) and with ASC specks and autophagosomes; an alternatively spliced isoform lacking exon 2 translocates to the nucleus. Gain-of-function MEFV mutations, mostly in the B30.2/SPRY domain, cause autosomal-recessive Familial Mediterranean Fever (FMF), and mutations affecting the Ser242 14-3-3 site cause autosomal-dominant Pyrin-Associated Autoinflammation with Neutrophilic Dermatosis (PAAND).
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 33; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Mostly consistent, with one watch-point the PN mapping itself flags. Deep research, review and PN agree pyrin is both a pro-inflammatory inflammasome sensor (ASC/caspase-1/IL-1β) and an anti-inflammatory TRIM20 "precision-autophagy" receptor degrading NLRP3/NLRP1/pro-caspase-1. The PN row2 subtype label literally says "Pyrin, ringless, SPRY" — i.e. PN itself records that pyrin is a RINGLESS TRIM, matching the review's `MARK_AS_OVER_ANNOTATED` of GO:0061630 (no functional RING). No hard contradiction.
- **PN story / NEW pressure:** Row1 projects GO:0160247 autophagy cargo adaptor activity (verified real; confirmed ABSENT from GOA). This is a defensible **ADD**: pyrin/TRIM20 binds inflammasome cargo and recruits ATG machinery (PMID:26347139), an MF the review currently captures only as positive-regulation-of-autophagy (KEEP_AS_NON_CORE) + bare protein binding — never as cargo-adaptor MF. Row2 GO:0061630 is the over-annotation watch case: PN's RING-group default projects ligase MF, but pyrin has NO functional RING; the review correctly marks the existing IBA GO:0061630 as over-annotated.
- **Evidence alignment:** Good. PN row1 ref (precision autophagy JCB = PMID:26347139) is in the review (HIGH/VERIFIED). PN row2 "33791238 / rev" not in the review (family review pointer); review's pyrin biochemistry rests on the inflammasome/PAAND papers instead.
- **Verdict:** Consistent; GO:0160247 cargo-adaptor is a justified ADD; the RING-group ligase MF must NOT propagate to ringless pyrin (review already over-annotates it).

## Full Consistency Review

- **UniProt:** O15553 (Pyrin/TRIM20) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (very thorough; inflammasome sensor + precision-autophagy receptor; 2 PN rows)
- **PN placement:** row1 `ALP|Autophagy substrate selection|Selective autophagy receptor|Individual substrates`; row2 `UPS|E3 ubiquitin and UBL ligases|RING|TRIM / unclassified|Pyrin, ringless, SPRY`. **PN-node mapping:** row1 type→mapped GO:0160247 autophagy cargo adaptor activity; row2 RING group→mapped GO:0061630 ubiquitin protein ligase activity (class context_only/too_broad).
- **Consistency:** Mostly consistent, with one watch-point the PN mapping itself flags. Deep research, review and PN agree pyrin is both a pro-inflammatory inflammasome sensor (ASC/caspase-1/IL-1β) and an anti-inflammatory TRIM20 "precision-autophagy" receptor degrading NLRP3/NLRP1/pro-caspase-1. The PN row2 subtype label literally says "Pyrin, ringless, SPRY" — i.e. PN itself records that pyrin is a RINGLESS TRIM, matching the review's `MARK_AS_OVER_ANNOTATED` of GO:0061630 (no functional RING). No hard contradiction.
- **PN story / NEW pressure:** Row1 projects GO:0160247 autophagy cargo adaptor activity (verified real; confirmed ABSENT from GOA). This is a defensible **ADD**: pyrin/TRIM20 binds inflammasome cargo and recruits ATG machinery (PMID:26347139), an MF the review currently captures only as positive-regulation-of-autophagy (KEEP_AS_NON_CORE) + bare protein binding — never as cargo-adaptor MF. Row2 GO:0061630 is the over-annotation watch case: PN's RING-group default projects ligase MF, but pyrin has NO functional RING; the review correctly marks the existing IBA GO:0061630 as over-annotated.
- **Mapping strategy:** Row1 cargo-adaptor mapping is sound and aligns with the established CALCOCO/TRIM precision-autophagy receptor concept. Row2 needs a per-gene caveat: the RING-group→GO:0061630 propagation is the right *default* for catalytic RING E3s but MUST be suppressed for pyrin (ringless) — exactly the over-annotation pattern. The subtype is already no_mapping, so propagation flows only from the group default; recommend a node-level exclusion note for ringless members.
- **Evidence alignment:** Good. PN row1 ref (precision autophagy JCB = PMID:26347139) is in the review (HIGH/VERIFIED). PN row2 "33791238 / rev" not in the review (family review pointer); review's pyrin biochemistry rests on the inflammasome/PAAND papers instead.
- **Verdict:** Consistent; GO:0160247 cargo-adaptor is a justified ADD; the RING-group ligase MF must NOT propagate to ringless pyrin (review already over-annotates it).
- **Recommended edits:** [YAML] consider adding GO:0160247 autophagy cargo adaptor activity (MF) for the TRIM20 precision-autophagy receptor role (PMID:26347139) — currently captured only as non-core positive-regulation-of-autophagy. [MAP] annotate the RING-group node (or a ringless-TRIM exclusion) so GO:0061630 does NOT auto-propagate to "Pyrin, ringless, SPRY" members lacking a functional RING; the review's over-annotation flag on GO:0061630 should be honored by the mapping.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/MEFV/MEFV-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Individual substrates
- UniProt: O15553
- In branches: ALP, UPS
- Notes: TRIM20 and TRIM21 bind to targets for degradation and recruit autophagy components.
- PN references (titles):
    - TRIM-mediated precision autophagy targets cytoplasmic regulators of innate immunity | Journal of Cell Biology | Rockefeller University Press (rupress.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Individual substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160247 autophagy cargo adaptor activity]
        rationale: This PN category groups receptors such as TRIM-family factors that bind specific substrates and recruit autophagy components for their turnover. That aligns best with autophagy cargo adaptor activity rather than with a single selective-autophagy process term.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | TRIM / unclassified | Pyrin, ringless, SPRY
- UniProt: O15553
- In branches: ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR004020, IPR003877, IPR006574
- PN references (titles):
    - 33791238 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / unclassified|Pyrin, ringless, SPRY
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|TRIM / unclassified
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Individual substrates
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
