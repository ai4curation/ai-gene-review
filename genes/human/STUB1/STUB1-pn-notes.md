# STUB1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UNE7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/STUB1/STUB1-ai-review.yaml](STUB1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/STUB1/STUB1-ai-review.html](STUB1-ai-review.html)
- Gene notes: present - [genes/human/STUB1/STUB1-notes.md](STUB1-notes.md)
- GOA TSV: present - [genes/human/STUB1/STUB1-goa.tsv](STUB1-goa.tsv)
- UniProt record: present - [genes/human/STUB1/STUB1-uniprot.txt](STUB1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/STUB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/STUB1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/STUB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/STUB1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: STUB1 (E3 ubiquitin-protein ligase CHIP, C-terminus of HSC70-interacting protein) is a cytoplasmic protein that couples the molecular-chaperone and ubiquitin-proteasome systems. It has a bipartite architecture: an N-terminal tetratricopeptide repeat (TPR) domain that binds the C-terminal EEVD/MEEVD motifs of HSP70/HSC70 and HSP90, and a C-terminal U-box domain that confers RING-type E3 ubiquitin-ligase activity. Acting as a chaperone-associated 'triage' factor, CHIP ubiquitinates chaperone-bound misfolded or damaged client proteins (in cooperation with E2 enzymes such as UBE2D and UBE2N/UBE2V1) and targets them for proteasomal degradation, while also modulating the activity of the HSP70/HSC70/HSP90 chaperone cycle as a co-chaperone. CHIP functions as a homodimer and additionally participates in protein quality control, ERAD, chaperone-mediated autophagy and mitophagy, and the regulated turnover of numerous specific substrates (e.g. tau, FOXO1, NOS1, POLB, ESR1). Loss of CHIP ubiquitin-ligase activity causes autosomal-recessive (SCAR16) and autosomal-dominant (SCA48) spinocerebellar ataxia.
- Existing/core annotation action counts: ACCEPT: 85; KEEP_AS_NON_CORE: 100; MODIFY: 12

## PN Consistency Summary

- **Consistency:** Strong. Review, notes and PN agree on the dual identity — genuine U-box E3 ligase (GO:0061630 ACCEPT, core) AND HSP70/HSP90 co-chaperone (TPR; GO:0030544/0051879/0031072/0051087 ACCEPT). Review explicitly distinguishes both MFs as the prompt requires. CMA (GO:0061684) and Ub-ligase-complex (GO:0000151) present in review, matching two PN projections. No contradictions.
- **PN story / NEW pressure:** PN row 2 asserts CASA/aggrephagy (GO:0035973, verified real, goa_status=new_to_goa). This is NOT in the review (no aggrephagy/CASA/BAG3/HSPB8 annotation anywhere). Review covers mitophagy + CMA as non-core but omits aggrephagy. STUB1 is a bona fide CASA component (BAG3-HSPB8-HSPA8-STUB1) → **ADD is defensible** (aggrephagy, IBA/IC, non-core). proposed_new_terms is empty.
- **Evidence alignment:** PN cites CASA review (tandfonline), CMA review (Nat Rev MCB), PMID:12646216, PMID:40796662 (STUB1/CHIC2). Review is UniProt/GOA-driven (197 IPI/IBA/IEA refs); none of the four PN-specific titles appear in the review. Divergence is in the autophagy-receptor literature.
- **Verdict:** Consistent and high-quality; one warranted addition (aggrephagy). **Recommended edits:** add GO:0035973 aggrephagy as KEEP_AS_NON_CORE supported by CASA literature [YAML]; optionally cite PMID:40796662 / CASA review in references [REF].

## Full Consistency Review

- **UniProt:** Q9UNE7 (CHIP) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE (197 annotations reviewed)
- **PN placement:** spans 5 rows across CY/ALP/UPS — `Cytonuclear|Chaperone|HSP70-HSP90 joint cochaperone|CC-TPR domain and Ub ligase`; `ALP|...|CASA complex component`; `ALP|CMA|Effectors|Substrate selection`; `UPS|E3 ligases|RING variant|UBOX|TPR`; `UPS|...|STUB1/CHIC2 complex` ; **PN-node mapping:** mapped → GO:0061630 (Ub ligase activity), GO:0031072 (HSP binding), GO:0035973 (aggrephagy, new), GO:0061684 (CMA), GO:0061740 (CMA targeting), GO:0000151 (Ub ligase complex)
- **Consistency:** Strong. Review, notes and PN agree on the dual identity — genuine U-box E3 ligase (GO:0061630 ACCEPT, core) AND HSP70/HSP90 co-chaperone (TPR; GO:0030544/0051879/0031072/0051087 ACCEPT). Review explicitly distinguishes both MFs as the prompt requires. CMA (GO:0061684) and Ub-ligase-complex (GO:0000151) present in review, matching two PN projections. No contradictions.
- **PN story / NEW pressure:** PN row 2 asserts CASA/aggrephagy (GO:0035973, verified real, goa_status=new_to_goa). This is NOT in the review (no aggrephagy/CASA/BAG3/HSPB8 annotation anywhere). Review covers mitophagy + CMA as non-core but omits aggrephagy. STUB1 is a bona fide CASA component (BAG3-HSPB8-HSPA8-STUB1) → **ADD is defensible** (aggrephagy, IBA/IC, non-core). proposed_new_terms is empty.
- **Mapping strategy:** Node mappings are sound and conservative (E3-complex node → GO:0000151 membership not catalytic activity; CMA class held context_only). No change needed; aggrephagy is the only genuinely novel projection.
- **Evidence alignment:** PN cites CASA review (tandfonline), CMA review (Nat Rev MCB), PMID:12646216, PMID:40796662 (STUB1/CHIC2). Review is UniProt/GOA-driven (197 IPI/IBA/IEA refs); none of the four PN-specific titles appear in the review. Divergence is in the autophagy-receptor literature.
- **Verdict:** Consistent and high-quality; one warranted addition (aggrephagy). **Recommended edits:** add GO:0035973 aggrephagy as KEEP_AS_NON_CORE supported by CASA literature [YAML]; optionally cite PMID:40796662 / CASA review in references [REF].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/STUB1/STUB1-ai-review.yaml
- PN workbook rows: 5

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR domain and Ub ligase
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR domain and Ub ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN subtype explicitly denotes TPR-containing ubiquitin ligases in the HSP70/HSP90 co-chaperone branch. The shared catalytic assertion is ubiquitin protein ligase activity.
    - [type] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031072 heat shock protein binding]
        rationale: This PN type groups joint HSP70/HSP90 cochaperones. The shared mechanistic assertion is binding heat-shock-protein chaperones, while narrower domain labels remain non-mapping unless they carry an independent activity.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Chaperone assisted selective autophagy | CASA complex component
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Notes: HSP90 cochaperone. Participates in chaperone-assisted selective autophagy by forming the CASA complex (HSPA8, BAG3, HSPB8, and STUB1) that delivers ubiquitinated substrates to the to the autophagosome
- PN references (titles):
    - Full article: The chaperone-assisted selective autophagy complex dynamics and dysfunctions (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: The PN CASA subtype covers BAG3-HSPB8-HSP70-system machinery that directs damaged or aggregation-prone substrates into selective autophagic clearance. GO lacks a dedicated CASA term in the current cache, and this subtype includes chaperones and cofactors beyond pure cargo adaptors, so aggrephagy is the closest available process target.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Effectors of chaperone-mediated autophagy | Substrate selection
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Notes: An HSP90 cochaperone. Works with HSPA8 in autophagy substrate selection.
- PN references (titles):
    - The coming of age of chaperone-mediated autophagy | Nature Reviews Molecular Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy|Substrate selection
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy]
        rationale: This leaf denotes substrate-selection machinery for CMA. The GO protein-targeting term preserves the mechanistic role without relying on broad class-level CMA propagation.
    - [group] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: This group covers direct CMA machinery and substrate-selection effectors, unlike the broader CMA class that also includes regulators. Propagation to chaperone-mediated autophagy is appropriate at this narrower level.
    - [class] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: The class label matches the GO CMA process, but the subtree includes both effectors and positive or negative modulators. The relation is retained as context so modulators are not projected as direct CMA participants unless a narrower node supports it.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING variant | UBOX | TPR
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Signature domains: IPR003613
- Auxiliary domains: IPR019734
- PN references (titles):
    - 12646216 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|UBOX|TPR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|UBOX
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 5: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic UBOX complex | STUB1/CHIC2 complex | catalytic / UBOX / TPR
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR003613, IPR019734
- PN references (titles):
    - 40796662
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex|catalytic / UBOX / TPR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (7)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR domain and Ub ligase
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
- GO:0061684 chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy
- GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy|Substrate selection
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
