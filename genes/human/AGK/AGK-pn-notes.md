# AGK PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q53H12
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1351)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AGK/AGK-ai-review.yaml](AGK-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AGK/AGK-ai-review.html](AGK-ai-review.html)
- Gene notes: present - [genes/human/AGK/AGK-notes.md](AGK-notes.md)
- GOA TSV: present - [genes/human/AGK/AGK-goa.tsv](AGK-goa.tsv)
- UniProt record: present - [genes/human/AGK/AGK-uniprot.txt](AGK-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AGK.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AGK.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AGK.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AGK.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AGK/AGK-deep-research-falcon.md](AGK-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AGK encodes a mitochondrial acylglycerol kinase with dual roles in lipid metabolism and mitochondrial protein import. Its catalytic activity phosphorylates monoacylglycerol and diacylglycerol to generate lysophosphatidic acid and phosphatidic acid. Independently of lipid kinase activity, AGK is a metazoan TIM22 complex subunit at the mitochondrial inner membrane/intermembrane-space interface, where it supports import and assembly of carrier-type multipass inner-membrane proteins. Biallelic AGK variants cause Sengers syndrome, linking defects in mitochondrial lipid metabolism and TIM22-dependent protein biogenesis to congenital cataracts, cardiomyopathy, skeletal myopathy, and lactic acidosis.
- Existing/core annotation action counts: ACCEPT: 25; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 4; REMOVE: 11

## PN Consistency Summary

- **Consistency:** Deep research notes (falcon failed; manual fallback), review, and PN agree on AGK's dual role: mitochondrial acylglycerol/diacylglycerol kinase (LPA/PA) plus kinase-independent TIM22-complex subunit supporting carrier-protein import. No contradictions. The review actively removes mis-seeded ceramide/sphingosine-kinase and plasma-membrane/BRAF-fusion-cytosol annotations — independent of PN, and consistent with PN's mitochondrial framing.
- **PN story / NEW pressure:** PN class projects GO:0015031 protein transport as new-to-GOA. The review instead uses the more specific, directly-supported GO:0045039 protein insertion into mitochondrial inner membrane (IDA, PMID:28712724/28712726/32901109) and notes the strongest PN-relevant role is the TIM22 import-complex role "not a generic protein-transport assertion." GO:0042721 TIM22 complex is already in GOA (3 rows confirmed). Verdict: PN protein-transport role already captured by a narrower term; broad GO:0015031 not needed.
- **Evidence alignment:** PN dossier lists no reference titles. Review evidence overlaps PN's mitochondrial-import framing via PMID:28712724, 28712726, 32901109 (TIM22), 15939762 (lipid kinase). PN projection TSV cited for GO:0045039 context. No PMID conflicts.
- **Verdict:** Consistent; PN TIM22 (GO:0042721) adopted; PN class GO:0015031 protein transport too broad — review's GO:0045039 is the correct narrower call. **Recommended edits:** none required. Optional [MAP]: confirm class-level GO:0015031 stays gene-gated in favor of compartment-specific insertion/import terms.

## Full Consistency Review

- **UniProt:** Q53H12 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Protein transport|Inner membrane import|TIMM22 complex` ; **PN-node mapping:** type (TIMM22) `mapped` GO:0042721 TIM22 complex (already_in_goa_exact); group (inner-membrane import) `context_only` too_broad GO:0044743; class (Protein transport) `mapped` GO:0015031 protein transport (new_to_goa); branch `no_mapping`.
- **Consistency:** Deep research notes (falcon failed; manual fallback), review, and PN agree on AGK's dual role: mitochondrial acylglycerol/diacylglycerol kinase (LPA/PA) plus kinase-independent TIM22-complex subunit supporting carrier-protein import. No contradictions. The review actively removes mis-seeded ceramide/sphingosine-kinase and plasma-membrane/BRAF-fusion-cytosol annotations — independent of PN, and consistent with PN's mitochondrial framing.
- **PN story / NEW pressure:** PN class projects GO:0015031 protein transport as new-to-GOA. The review instead uses the more specific, directly-supported GO:0045039 protein insertion into mitochondrial inner membrane (IDA, PMID:28712724/28712726/32901109) and notes the strongest PN-relevant role is the TIM22 import-complex role "not a generic protein-transport assertion." GO:0042721 TIM22 complex is already in GOA (3 rows confirmed). Verdict: PN protein-transport role already captured by a narrower term; broad GO:0015031 not needed.
- **Mapping strategy:** Gene does not change the node. The TIMM22-type GO:0042721 mapping is correct and adopted. The class-level GO:0015031 protein transport projection is broader than the review's GO:0045039 — same broader-rejected pattern as TOMM20/HSPA8/RAB7A; gene-level narrower term is preferred. PN's own group node is already `too_broad_to_propagate`, consistent with this.
- **Evidence alignment:** PN dossier lists no reference titles. Review evidence overlaps PN's mitochondrial-import framing via PMID:28712724, 28712726, 32901109 (TIM22), 15939762 (lipid kinase). PN projection TSV cited for GO:0045039 context. No PMID conflicts.
- **Verdict:** Consistent; PN TIM22 (GO:0042721) adopted; PN class GO:0015031 protein transport too broad — review's GO:0045039 is the correct narrower call. **Recommended edits:** none required. Optional [MAP]: confirm class-level GO:0015031 stays gene-gated in favor of compartment-specific insertion/import terms.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AGK/AGK-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Protein transport | Inner membrane import | TIMM22 complex
- UniProt: Q53H12
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [type] Mitochondrial proteostasis|Protein transport|Inner membrane import|TIMM22 complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042721 TIM22 mitochondrial import inner membrane insertion complex]
        rationale: This PN type captures TIMM22-complex components responsible for a specific inner-membrane import route. The GO cellular-component term for the TIM22 insertion complex is an appropriate propagation target.
    - [group] Mitochondrial proteostasis|Protein transport|Inner membrane import
        status=context_only scope=too_broad_to_propagate GO=[GO:0044743 protein transmembrane import into intracellular organelle]
        rationale: In `4.3.11`, inner-membrane import is a group that covers TIM22, TIM17/23, PAM-associated matrix import, and related inner-membrane sorting routes. The source is useful context for mitochondrial protein import, but protein insertion into mitochondrial inner membrane is too specific for all descendants because reviewed TIM23/PAM components include matrix-import motor and gatekeeper roles. Propagation should come from narrower child nodes such as TIM22 complex, TIM23 complex, or OXA1L-mediated insertion.
    - [class] Mitochondrial proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN mitochondrial Protein transport class groups protein-targeting and import pathways into mitochondria. GO protein transport is the appropriate propagation target, while the source class remains mitochondria-specific and broader than any single GO transport subtype.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Protein transport
- GO:0042721 TIM22 mitochondrial import inner membrane insertion complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Mitochondrial proteostasis|Protein transport|Inner membrane import|TIMM22 complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
