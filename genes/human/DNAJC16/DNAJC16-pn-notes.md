# DNAJC16 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y2G8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC16/DNAJC16-ai-review.yaml](DNAJC16-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC16/DNAJC16-ai-review.html](DNAJC16-ai-review.html)
- Gene notes: present - [genes/human/DNAJC16/DNAJC16-notes.md](DNAJC16-notes.md)
- GOA TSV: present - [genes/human/DNAJC16/DNAJC16-goa.tsv](DNAJC16-goa.tsv)
- UniProt record: present - [genes/human/DNAJC16/DNAJC16-uniprot.txt](DNAJC16-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC16.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC16.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC16 (ERdj8, "ER-resident protein ERdj8") is a large, single-pass type IV endoplasmic reticulum membrane protein of the DnaJ/HSP40 subfamily C. It has an N-terminal cleaved signal peptide, a cytoplasmically oriented N-terminal J domain and an adjacent thioredoxin (TRX) domain in its large cytoplasmic region, followed by a C-terminal transmembrane anchor. ERdj8 localizes to a meshwork-like ER subdomain together with phosphatidylinositol synthase and autophagy-related (Atg) proteins, and functions in autophagosome biogenesis where it regulates the size of forming autophagosomes, enabling engulfment of large targets; both its J domain and TRX domain are required for this activity. It is otherwise poorly characterized, and its direct molecular activity (presumed J-domain co-chaperone and/or redox function) has not been biochemically defined. An alternative splice isoform lacks the J and thioredoxin domains.
- Existing/core annotation action counts: ACCEPT: 3

## PN Consistency Summary

- **Consistency:** Partial mismatch. Deep-research notes and review agree the gene is poorly characterized (Pharos Tdark, PAN-GO 0): the ONLY experimental function is ER-membrane localization (GO:0005789) and regulation of autophagosome size (GO:0016243, IMP, PMID:32492081). Crucially the review states the "direct molecular activity (presumed J-domain co-chaperone... ) has not been biochemically defined" — so the PN assertion of Hsp70 binding is an inference, not established. The PN node nonetheless tags it as a confident new-to-GOA propagation, which over-states the evidence.
- **PN story / NEW pressure:** PN proposes ADD of GO:0030544 Hsp70 protein binding as new_to_goa. GO:0030544 is verified real (OLS), but for DNAJC16 there is no experimental HSP70-binding/co-chaperone data; the J domain is required for autophagosome enlargement but no HSP70 partner has been identified (the review's own suggested experiment is to test this). This is over-reach at the gene level: the projection rests purely on family/domain membership.
- **Evidence alignment:** Single shared paper PMID:32492081 (Yamamoto 2020). PN node carries no DNAJC16-specific reference; the projection is purely taxonomic. No evidence divergence, but no positive evidence for the Hsp70-binding claim either.
- **Verdict:** Over-reaches for this gene — Hsp70 binding is domain-inferred only, no HSP70 partner shown; flag as family-level inference, not new_to_goa. **Recommended edits:** [MAP] downgrade DNAJC16's GO:0030544 projection from new_to_goa confident annotation to family/ISS-level inference (no experimental HSP70 binding); note the established function (autophagosome-size regulation) lies outside this HSP70-cochaperone node.

## Full Consistency Review

- **UniProt:** Q9Y2G8 (ERdj8) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone` (branch CY) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (goa_status=new_to_goa)
- **Consistency:** Partial mismatch. Deep-research notes and review agree the gene is poorly characterized (Pharos Tdark, PAN-GO 0): the ONLY experimental function is ER-membrane localization (GO:0005789) and regulation of autophagosome size (GO:0016243, IMP, PMID:32492081). Crucially the review states the "direct molecular activity (presumed J-domain co-chaperone... ) has not been biochemically defined" — so the PN assertion of Hsp70 binding is an inference, not established. The PN node nonetheless tags it as a confident new-to-GOA propagation, which over-states the evidence.
- **PN story / NEW pressure:** PN proposes ADD of GO:0030544 Hsp70 protein binding as new_to_goa. GO:0030544 is verified real (OLS), but for DNAJC16 there is no experimental HSP70-binding/co-chaperone data; the J domain is required for autophagosome enlargement but no HSP70 partner has been identified (the review's own suggested experiment is to test this). This is over-reach at the gene level: the projection rests purely on family/domain membership.
- **Mapping strategy:** The node-level mapping (J-domain cochaperones bind Hsp70) is defensible as a family heuristic, but for DNAJC16 specifically the new_to_goa propagation should be down-weighted to an inference (ISS/family-level) rather than asserted as a confident annotation, since the molecular function is explicitly undefined. PN-projected term is broader than the review's actual core (autophagosome-size regulation), which the node does not capture at all.
- **Evidence alignment:** Single shared paper PMID:32492081 (Yamamoto 2020). PN node carries no DNAJC16-specific reference; the projection is purely taxonomic. No evidence divergence, but no positive evidence for the Hsp70-binding claim either.
- **Verdict:** Over-reaches for this gene — Hsp70 binding is domain-inferred only, no HSP70 partner shown; flag as family-level inference, not new_to_goa. **Recommended edits:** [MAP] downgrade DNAJC16's GO:0030544 projection from new_to_goa confident annotation to family/ISS-level inference (no experimental HSP70 binding); note the established function (autophagosome-size regulation) lies outside this HSP70-cochaperone node.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC16/DNAJC16-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9Y2G8
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
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
