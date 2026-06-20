# STIP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P31948
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/STIP1/STIP1-ai-review.yaml](STIP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/STIP1/STIP1-ai-review.html](STIP1-ai-review.html)
- Gene notes: present - [genes/human/STIP1/STIP1-notes.md](STIP1-notes.md)
- GOA TSV: present - [genes/human/STIP1/STIP1-goa.tsv](STIP1-goa.tsv)
- UniProt record: present - [genes/human/STIP1/STIP1-uniprot.txt](STIP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/STIP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/STIP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/STIP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/STIP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: STIP1 (stress-induced phosphoprotein 1), better known as HOP (Hsp70-Hsp90 organizing protein) or p60, is a cytoplasmic (and partly nuclear) TPR-domain adaptor co-chaperone. It contains three TPR (tetratricopeptide repeat) domains. The TPR1 domain binds the C-terminal EEVD motif of HSP70 (HSPA8/HSC70), while the TPR2A and TPR2B domains bind the C-terminal MEEVD motif of HSP90. By simultaneously engaging both chaperones, HOP physically bridges the HSP70 and HSP90 systems and coordinates the transfer of client proteins from HSP70 to HSP90 during the chaperone cycle. HOP has no catalytic activity; it functions as a scaffold/adaptor that modulates HSP90 conformation and client maturation. It is a defining component of the HSP70-HSP90 multichaperone machine and participates in the maturation of diverse clients including protein kinases and steroid hormone receptors.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 19; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 6

## PN Consistency Summary

- **Consistency:** Partial. Review and notes correctly frame HOP as a non-catalytic TPR scaffold bridging HSP70↔HSP90 (core MF GO:0051879 Hsp90 binding; in_complex GO:0101031). But the review contains NO autophagy/CMA/microautophagy/lysosome content at all (confirmed in both YAML and notes), whereas PN asserts three ALP roles. This is a real coverage gap, not a contradiction.
- **PN story / NEW pressure:** PN projects CMA substrate-selection (GO:0061684, GO:0061740) and late endosomal microautophagy (GO:0061738) — all verified real, all new_to_goa (GOA confirms no autophagy rows). HOP/HSPA8 participation in eMI and CMA substrate handoff is literature-supported (Nat Rev MCB CMA review). **ADD is defensible** for these as non-core BPs if full text supports HOP specifically.
- **Evidence alignment:** PN cites the Nat Rev MCB CMA review; review references are UniProt/HSP90-cycle papers (e.g. PMID:27353360). No overlap on the autophagy literature.
- **Verdict:** Consistent on the chaperone core but review under-covers the ALP/CMA story PN documents. **Recommended edits:** consider adding GO:0061684 / GO:0061740 / GO:0061738 as KEEP_AS_NON_CORE pending full-text verification of HOP-specific evidence [YAML]; cite the CMA review [REF]. Do not add GO:0031072 (broader, already entailed) [MAP].

## Full Consistency Review

- **UniProt:** P31948 (HOP) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and STI/HOP domain`; `ALP|Microautophagy|Endosomal microautophagy`; `ALP|CMA|Effectors|Substrate selection` ; **PN-node mapping:** mapped → GO:0031072 (HSP binding, entailed_by_goa_closure), GO:0061738 (late endosomal microautophagy, new), GO:0061684 (CMA, new), GO:0061740 (CMA targeting, new)
- **Consistency:** Partial. Review and notes correctly frame HOP as a non-catalytic TPR scaffold bridging HSP70↔HSP90 (core MF GO:0051879 Hsp90 binding; in_complex GO:0101031). But the review contains NO autophagy/CMA/microautophagy/lysosome content at all (confirmed in both YAML and notes), whereas PN asserts three ALP roles. This is a real coverage gap, not a contradiction.
- **PN story / NEW pressure:** PN projects CMA substrate-selection (GO:0061684, GO:0061740) and late endosomal microautophagy (GO:0061738) — all verified real, all new_to_goa (GOA confirms no autophagy rows). HOP/HSPA8 participation in eMI and CMA substrate handoff is literature-supported (Nat Rev MCB CMA review). **ADD is defensible** for these as non-core BPs if full text supports HOP specifically.
- **Mapping strategy:** GO:0031072 projection is BROADER than the review's GO:0051879 (Hsp90 binding is_a heat shock protein binding, OLS-verified) but PN self-flags it entailed_by_goa_closure → redundant, no action. The novel value is the three ALP terms.
- **Evidence alignment:** PN cites the Nat Rev MCB CMA review; review references are UniProt/HSP90-cycle papers (e.g. PMID:27353360). No overlap on the autophagy literature.
- **Verdict:** Consistent on the chaperone core but review under-covers the ALP/CMA story PN documents. **Recommended edits:** consider adding GO:0061684 / GO:0061740 / GO:0061738 as KEEP_AS_NON_CORE pending full-text verification of HOP-specific evidence [YAML]; cite the CMA review [REF]. Do not add GO:0031072 (broader, already entailed) [MAP].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/STIP1/STIP1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR and STI/HOP domain containing
- UniProt: P31948
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and STI/HOP domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family/domain/subtype label. It classifies PN members but is not itself a GO annotation target; any functional assertion should come from a parent role mapping or gene-specific review.
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

## PN row 2: Autophagy-Lysosome Pathway | Microautophagy | Endosomal microautophagy
- UniProt: P31948
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Microautophagy|Endosomal microautophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061738 late endosomal microautophagy]
        rationale: This PN group contains HSPA8/co-chaperone machinery for endosomal microautophagy. The matching GO process is late endosomal microautophagy.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Effectors of chaperone-mediated autophagy | Substrate selection
- UniProt: P31948
- In branches: CY, ALP
- Notes: An HSP90 cochaperone. Works with HSPA8 in autophagy substrate selection. Also a component of the complex at the lysosomal membrane that facilitates the unfolding of substrates.
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

## Projected GO annotations (4)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0061738 late endosomal microautophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Microautophagy|Endosomal microautophagy
- GO:0061684 chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy
- GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy|Substrate selection

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
