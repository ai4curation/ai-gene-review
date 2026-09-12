# DNAJC22 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N4W6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC22/DNAJC22-ai-review.yaml](DNAJC22-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC22/DNAJC22-ai-review.html](DNAJC22-ai-review.html)
- Gene notes: present - [genes/human/DNAJC22/DNAJC22-notes.md](DNAJC22-notes.md)
- GOA TSV: present - [genes/human/DNAJC22/DNAJC22-goa.tsv](DNAJC22-goa.tsv)
- UniProt record: present - [genes/human/DNAJC22/DNAJC22-uniprot.txt](DNAJC22-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC22.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC22.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC22.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC22.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC22 (DnaJ homolog subfamily C member 22) is a poorly characterized polytopic membrane protein of the HSP40/DnaJ family. It has an N-terminal TM2-type region, multiple predicted transmembrane helices, and a C-terminal J-domain, the hallmark module that engages and stimulates HSP70-family chaperones. It is a multi-pass membrane protein and is predicted to act as a co-chaperone. Its Drosophila ortholog Wurst is a transmembrane J-domain protein that recruits clathrin and Hsc70 to the apical membrane to drive clathrin-mediated endocytosis (e.g. airway liquid clearance), suggesting DNAJC22 may have a related membrane co-chaperone/endocytic role, but direct functional data for the human protein are lacking. DNAJC22 is tissue-enriched in liver.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 1

## PN Consistency Summary

- **Consistency:** Consistent at the inference level. Notes and review agree DNAJC22 is a poorly characterized polytopic membrane J-domain protein (liver-enriched) with NO direct human functional data; the co-chaperone role is inferred from the C-terminal J domain and the Drosophila ortholog Wurst (recruits Hsc70/clathrin for endocytosis). The PN node and review both treat it as a predicted HSP70 co-chaperone — no contradiction, but both rest on family/orthology inference, not experiment.
- **PN story / NEW pressure:** PN proposes GO:0030544 Hsp70 protein binding (verified real, OLS). The review's core MF is the parent GO:0031072 heat shock protein binding (also inference-only). GO:0030544 is a verified more-specific child of GO:0031072, so the projection is internally defensible and consistent in direction with the review — but it remains a domain/orthology inference (candidate, no experimental HSP70-binding data). Existing GOA has only membrane (IBA/IEA) and bare protein binding (MEOX2 Y2H), so an HSP70-binding term would be new — but should be ISS/family-level, not a confident annotation.
- **Evidence alignment:** Minimal and aligned. Only literature reference is PMID:32296183 (HuRI Y2H, MEOX2 — relevance LOW, supplies the uninformative protein-binding term). Both review and PN lean on UniProt/Wurst orthology; no functional paper supports the Hsp70-binding claim directly.
- **Verdict:** Consistent family-level inference; GO:0030544 is a defensible more-specific candidate but unverified experimentally — flag as ISS/family inference rather than confident new annotation. **Recommended edits:** [MAP] retain GO:0030544 for DNAJC22 but mark as family/domain-level inference (no experimental HSP70 binding; Wurst-orthology basis only).

## Full Consistency Review

- **UniProt:** Q8N4W6 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa)
- **Consistency:** Consistent at the inference level. Notes and review agree DNAJC22 is a poorly characterized polytopic membrane J-domain protein (liver-enriched) with NO direct human functional data; the co-chaperone role is inferred from the C-terminal J domain and the Drosophila ortholog Wurst (recruits Hsc70/clathrin for endocytosis). The PN node and review both treat it as a predicted HSP70 co-chaperone — no contradiction, but both rest on family/orthology inference, not experiment.
- **PN story / NEW pressure:** PN proposes GO:0030544 Hsp70 protein binding (verified real, OLS). The review's core MF is the parent GO:0031072 heat shock protein binding (also inference-only). GO:0030544 is a verified more-specific child of GO:0031072, so the projection is internally defensible and consistent in direction with the review — but it remains a domain/orthology inference (candidate, no experimental HSP70-binding data). Existing GOA has only membrane (IBA/IEA) and bare protein binding (MEOX2 Y2H), so an HSP70-binding term would be new — but should be ISS/family-level, not a confident annotation.
- **Mapping strategy:** Node heuristic applies cleanly here (genuine J domain). PN-projected GO:0030544 is appropriately specific (more specific than the review's GO:0031072) and the "more_specific_than_existing_goa" direction is at least internally consistent. Keep as inference-level propagation given the absence of any functional data; do not elevate to a confident new annotation.
- **Evidence alignment:** Minimal and aligned. Only literature reference is PMID:32296183 (HuRI Y2H, MEOX2 — relevance LOW, supplies the uninformative protein-binding term). Both review and PN lean on UniProt/Wurst orthology; no functional paper supports the Hsp70-binding claim directly.
- **Verdict:** Consistent family-level inference; GO:0030544 is a defensible more-specific candidate but unverified experimentally — flag as ISS/family inference rather than confident new annotation. **Recommended edits:** [MAP] retain GO:0030544 for DNAJC22 but mark as family/domain-level inference (no experimental HSP70 binding; Wurst-orthology basis only).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC22/DNAJC22-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q8N4W6
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
