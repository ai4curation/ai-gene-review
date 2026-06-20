# FBXO39 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N4B4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO39/FBXO39-ai-review.yaml](FBXO39-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO39/FBXO39-ai-review.html
- Gene notes: missing - genes/human/FBXO39/FBXO39-notes.md
- GOA TSV: present - [genes/human/FBXO39/FBXO39-goa.tsv](FBXO39-goa.tsv)
- UniProt record: present - [genes/human/FBXO39/FBXO39-uniprot.txt](FBXO39-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO39.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO39.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO39.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO39.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO39/FBXO39-deep-research-falcon.md](FBXO39-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO39 (F-box only protein 39) is a 442-amino-acid F-box protein that serves as the substrate-recognition component of an SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex (a Cullin-RING ligase, CRL1). It contains an N-terminal F-box domain (residues ~16-61) through which it docks onto the SKP1-CUL1 scaffold, and a C-terminal leucine-rich-repeat (LRR)/RNI-like region predicted to mediate substrate binding. As an F-box "other" (FBXO) protein, FBXO39 acts as the interchangeable specificity subunit that targets substrate proteins for poly-ubiquitination and subsequent proteasomal degradation; the catalytic RING/E2-recruiting role within the complex is provided by RBX1/CUL1, not by FBXO39 itself. FBXO39 expression is testis-enriched and the gene is a cancer/testis antigen (historically named BCP-20), aberrantly re-expressed in several tumors (colorectal, glioma/glioblastoma, others), where it has been used as a prognostic/immunotherapy-candidate biomarker; knockdown in osteosarcoma cells reduces proliferation and increases apoptosis, indicating functional relevance to tumor-cell viability. The protein remains poorly characterized at the mechanistic level: no validated physiological substrate was established in the curated literature, although an emerging report proposes that FBXO39 promotes degradation of p53 to drive LDHA-mediated aerobic glycolysis in colorectal cancer. Its subcellular localization has not been experimentally determined.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 1

## PN Consistency Summary

- **Consistency:** Consistent. Deep research (cancer/testis antigen BCP-20; testis-enriched; no validated substrate; emerging 2026 p53/LDHA lead), review YAML, PN annotation, and PN-node mapping all agree on an F-box+LRR SCF substrate receptor. Review ACCEPTs GO:0019005/GO:0031146 (both IBA + NAS), KEEP_AS_NON_CORE on the bare protein binding (FBXO39-MEOX2, HuRI), core MF = GO:1990756. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role = already captured. The emerging p53-degradation mechanism is a single 2026 lead correctly held UNVERIFIED (not in cache, author-year only) and not promoted. proposed_new_terms = []. Conclusion: **already captured**; no defensible NEW term yet (a future "negative regulation of p53" claim would need verification).
- **Evidence alignment:** PN cites only "15340381 / rev." Review anchors on GO_REF:0000033 (IBA), PMID:34445249 (NAS), PMID:32296183 (HuRI), plus Falcon leads. No PMID overlap with PN's generic citation; same family-level framing.
- **Verdict:** Consistent, mapping correct, no NEW pressure. ACCEPT as-is. **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** Q8N4B4 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** F-box subtype/type = no_mapping; group = mapped, ok_for_propagation_to_go, GO:1990756; class = context_only/too_broad (GO:0061630).
- **Consistency:** Consistent. Deep research (cancer/testis antigen BCP-20; testis-enriched; no validated substrate; emerging 2026 p53/LDHA lead), review YAML, PN annotation, and PN-node mapping all agree on an F-box+LRR SCF substrate receptor. Review ACCEPTs GO:0019005/GO:0031146 (both IBA + NAS), KEEP_AS_NON_CORE on the bare protein binding (FBXO39-MEOX2, HuRI), core MF = GO:1990756. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role = already captured. The emerging p53-degradation mechanism is a single 2026 lead correctly held UNVERIFIED (not in cache, author-year only) and not promoted. proposed_new_terms = []. Conclusion: **already captured**; no defensible NEW term yet (a future "negative regulation of p53" claim would need verification).
- **Mapping strategy:** Gene does not change the node. GO:1990756 (OLS-verified) is correctly scoped and matches review core MF; the LRR subtype correctly defers to the parent group mapping. Not over-broad.
- **Evidence alignment:** PN cites only "15340381 / rev." Review anchors on GO_REF:0000033 (IBA), PMID:34445249 (NAS), PMID:32296183 (HuRI), plus Falcon leads. No PMID overlap with PN's generic citation; same family-level framing.
- **Verdict:** Consistent, mapping correct, no NEW pressure. ACCEPT as-is. **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO39/FBXO39-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q8N4B4
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001611, IPR032675
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
