# DNAJC9 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8WXX5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC9/DNAJC9-ai-review.yaml](DNAJC9-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC9/DNAJC9-ai-review.html](DNAJC9-ai-review.html)
- Gene notes: present - [genes/human/DNAJC9/DNAJC9-notes.md](DNAJC9-notes.md)
- GOA TSV: present - [genes/human/DNAJC9/DNAJC9-goa.tsv](DNAJC9-goa.tsv)
- UniProt record: present - [genes/human/DNAJC9/DNAJC9-uniprot.txt](DNAJC9-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC9.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC9.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC9 (also called HDJC9 or DnaJ protein SB73) is a type C DnaJ/Hsp40 (DNAJC) co-chaperone with an N-terminal J domain and a C-terminal histone-binding domain. It has a dual role as a histone H3-H4 chaperone and an HSP70 heat-shock co-chaperone. As a histone chaperone it forms a co-chaperone complex with MCM2 and histone H3-H4 heterodimers, binds H3 variants (H3.1, H3.2, H3.3) and H4, and integrates HSP70-mediated ATP-driven protein folding into the histone supply chain during replication- and transcription-coupled nucleosome assembly, helping to resolve aberrant histone-folding intermediates and assemble histones into nucleosomes. Its J domain recruits and stimulates the ATPase activity of HSP70-type chaperones (HSPA1A, HSPA1B, HSPA8). DNAJC9 is predominantly nuclear under normal conditions and translocates to the cytoplasm and plasma membrane after heat shock via a non-classical, lipid-dependent pathway; its expression is induced by heat shock, LPS, PMA and TNF.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 12; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes, review YAML, and PN all agree DNAJC9 is a J-domain HSP70 co-chaperone (binds HSPA1A/1B/8 via J domain, stimulates HSP70 ATPase). No contradictions. The review additionally develops the dual histone-H3-H4 chaperone role (MCM2 complex; PMID:33857403) that the single PN row does not capture, but this is enrichment, not conflict.
- **PN story / NEW pressure:** PN asserts only Hsp70-binding, which is captured: GOA/review already carry GO:0031072 (heat shock protein binding, parent of GO:0030544) plus GO:0032781, GO:0051087, GO:0101031. The projected GO:0030544 (verified real, child of GO:0031072) is a defensible refinement (`goa_status=more_specific_than_existing_goa` is accurate — GOA has the parent GO:0031072). No NEW term needed; the histone-chaperone axis (GO:0042393, GO:0006334) is the gene's distinctive biology and is already fully annotated in the review.
- **Evidence alignment:** PN row carries no reference titles; review anchors on PMID:17182002 (HSP70 co-chaperone, verified) and PMID:33857403 (histone chaperone, verified). No divergence — review evidence is a superset.
- **Verdict:** Consistent; PN GO:0030544 already captured (as parent in GOA) and defensible. No edits required.

## Full Consistency Review

- **UniProt:** Q8WXX5 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (group/class/branch = no_mapping)
- **Consistency:** Strong. Notes, review YAML, and PN all agree DNAJC9 is a J-domain HSP70 co-chaperone (binds HSPA1A/1B/8 via J domain, stimulates HSP70 ATPase). No contradictions. The review additionally develops the dual histone-H3-H4 chaperone role (MCM2 complex; PMID:33857403) that the single PN row does not capture, but this is enrichment, not conflict.
- **PN story / NEW pressure:** PN asserts only Hsp70-binding, which is captured: GOA/review already carry GO:0031072 (heat shock protein binding, parent of GO:0030544) plus GO:0032781, GO:0051087, GO:0101031. The projected GO:0030544 (verified real, child of GO:0031072) is a defensible refinement (`goa_status=more_specific_than_existing_goa` is accurate — GOA has the parent GO:0031072). No NEW term needed; the histone-chaperone axis (GO:0042393, GO:0006334) is the gene's distinctive biology and is already fully annotated in the review.
- **Mapping strategy:** This gene does not require changing the node. GO:0030544 is appropriately narrower than the review's broad coverage and is defensible for the J-domain-cochaperone type. The PN row legitimately under-describes DNAJC9 (ignores histone role), but that is by-design for a type-level mapping.
- **Evidence alignment:** PN row carries no reference titles; review anchors on PMID:17182002 (HSP70 co-chaperone, verified) and PMID:33857403 (histone chaperone, verified). No divergence — review evidence is a superset.
- **Verdict:** Consistent; PN GO:0030544 already captured (as parent in GOA) and defensible. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC9/DNAJC9-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q8WXX5
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
