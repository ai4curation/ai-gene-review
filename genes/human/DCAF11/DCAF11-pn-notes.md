# DCAF11 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8TEB1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DCAF11/DCAF11-ai-review.yaml](DCAF11-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DCAF11/DCAF11-ai-review.html](DCAF11-ai-review.html)
- Gene notes: present - [genes/human/DCAF11/DCAF11-notes.md](DCAF11-notes.md)
- GOA TSV: present - [genes/human/DCAF11/DCAF11-goa.tsv](DCAF11-goa.tsv)
- UniProt record: present - [genes/human/DCAF11/DCAF11-uniprot.txt](DCAF11-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DCAF11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DCAF11.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DCAF11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DCAF11.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DCAF11 (DDB1- and CUL4-associated factor 11; also called WD repeat-containing protein 23, WDR23) is a WD40-repeat protein that serves as a substrate-recognition receptor of the CRL4 (DDB1-CUL4-RBX1) cullin-RING E3 ubiquitin ligase. Through a conserved WDXR motif it docks onto the DDB1 adaptor of CUL4A- and CUL4B-based complexes and uses its C-terminal WD40 beta-propeller to present specific substrates for polyubiquitination and proteasomal degradation. Characterized substrates include the NRF2/NFE2L2 transcription factor (via the DIDLID sequence of its Neh2 domain), which links DCAF11 to the cellular antioxidant/oxidative-stress response, and the centromeric histone variant CENP-A, whose phospho-Ser68-primed degradation DCAF11 mediates to maintain centromere identity. The protein localizes predominantly to the nucleoplasm, consistent with its nuclear substrates. The orthologous receptor in C. elegans (WDR-23) controls the NRF/Nrf2 ortholog SKN-1, and DCAF11 has also been exploited as a recruited ligase in covalent molecular-glue targeted protein degradation.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 8; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep-research notes, review, and PN all describe DCAF11 as a CRL4 substrate receptor (WD40 + WDxR docking on DDB1) with two validated substrates: NRF2/NFE2L2 (PMID:31586112) and CENP-A (PMID:34758320). Better characterized than DCAF10. No contradictions.
- **PN story / NEW pressure:** Already captured. Unlike DCAF10, the DCAF11 review already MODIFIES a bare protein-binding annotation to GO:1990756 (proposed_replacement_terms on the PMID:16949367 DDB1/CUL4 IPI) AND uses GO:1990756 as the molecular_function of its first core_function. PN's projected GO:1990756 thus duplicates an MF the review already asserts. No additional ADD needed. (PN flags it new_to_goa because GOA proper still only has bare protein binding — the review's MODIFY is the mechanism to introduce it.) Substrate-adaptor MF only; no catalytic RING (distinct from COP1).
- **Evidence alignment:** PN cites 17588513 (DCAF review). Review's gene-specific evidence (PMID:16949367 founding DCAF, 16964240 DDB1-CUL4A architecture, 31586112 NRF2, 34758320 CENP-A) does not directly overlap the single PN citation but is concordant at the family/mechanism level.
- **Verdict:** Consistent; mapping sound; no edits. GO:1990756 already in review (core_function + MODIFY); PN projection is redundant-but-correct.

## Full Consistency Review

- **UniProt:** Q8TEB1 (WDR23) · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other` ; **PN-node mapping:** group node `Cul4A/Cul4B substrate receptor` mapped → GO:1990756 (ok_for_propagation, new_to_goa); class context_only (GO:0061630, too_broad).
- **Consistency:** Fully consistent. Deep-research notes, review, and PN all describe DCAF11 as a CRL4 substrate receptor (WD40 + WDxR docking on DDB1) with two validated substrates: NRF2/NFE2L2 (PMID:31586112) and CENP-A (PMID:34758320). Better characterized than DCAF10. No contradictions.
- **PN story / NEW pressure:** Already captured. Unlike DCAF10, the DCAF11 review already MODIFIES a bare protein-binding annotation to GO:1990756 (proposed_replacement_terms on the PMID:16949367 DDB1/CUL4 IPI) AND uses GO:1990756 as the molecular_function of its first core_function. PN's projected GO:1990756 thus duplicates an MF the review already asserts. No additional ADD needed. (PN flags it new_to_goa because GOA proper still only has bare protein binding — the review's MODIFY is the mechanism to introduce it.) Substrate-adaptor MF only; no catalytic RING (distinct from COP1).
- **Mapping strategy:** Correct. Group → GO:1990756 substrate-adaptor MF is right; class GO:0061630 correctly too_broad. Projection is precisely scoped, not over-reaching (contrast the rejected TOMM20/HSPA8/RAB7A broader-term cases). No mapping change.
- **Evidence alignment:** PN cites 17588513 (DCAF review). Review's gene-specific evidence (PMID:16949367 founding DCAF, 16964240 DDB1-CUL4A architecture, 31586112 NRF2, 34758320 CENP-A) does not directly overlap the single PN citation but is concordant at the family/mechanism level.
- **Verdict:** Consistent; mapping sound; no edits. GO:1990756 already in review (core_function + MODIFY); PN projection is redundant-but-correct.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/DCAF11/DCAF11-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | WD40 | other
- UniProt: Q8TEB1
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN references (titles):
    - 17588513 rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
