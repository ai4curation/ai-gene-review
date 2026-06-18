# FBXL14 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N1E6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL14/FBXL14-ai-review.yaml](FBXL14-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL14/FBXL14-ai-review.html
- Gene notes: missing - genes/human/FBXL14/FBXL14-notes.md
- GOA TSV: present - [genes/human/FBXL14/FBXL14-goa.tsv](FBXL14-goa.tsv)
- UniProt record: present - [genes/human/FBXL14/FBXL14-uniprot.txt](FBXL14-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL14.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL14.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL14/FBXL14-deep-research-falcon.md](FBXL14-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL14 (F-box/LRR-repeat protein 14; FBL14) is a substrate-recognition subunit of an SCF (SKP1-CUL1-RBX1) E3 ubiquitin ligase complex. Its F-box motif binds SKP1, linking it to the CUL1-RBX1 catalytic core, while its leucine-rich repeat domain provides substrate selectivity, directing substrate-specific polyubiquitination and proteasomal degradation. The best-characterized substrate is the EMT master transcription factor SNAI1/SNAIL1: SCF(FBXL14) binds (through a SNAI1 region around aa 120-151) and polyubiquitinates SNAI1 on lysines including K98, K137 and K146, promoting its proteasomal degradation in a manner independent of GSK-3beta phosphorylation, thereby controlling SNAI1 abundance during epithelial-to-mesenchymal transition. FBXL14 expression is down-regulated by hypoxia in a TWIST1-dependent manner, which stabilizes SNAI1 and supports EMT. FBXL14 also targets additional transcriptional regulators for degradation: it recognizes the conserved C-terminal WRPW motif of the Notch effector HES1 to promote its ubiquitination and turnover (affecting Notch signaling dynamics and neuronal differentiation), and it has been reported to ubiquitinate Thr58-phosphorylated c-MYC, promoting differentiation and suppressing glioma stem-cell tumorigenicity. FBXL14 is mainly cytoplasmic and acts in the cytoplasm/cytosol.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 18; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL14 is the SCF(FBXL14) substrate receptor degrading SNAI1/SNAIL1 (PMID:19955572, IDA), with falcon adding HES1 (WRPW motif) and Thr58-phospho-c-MYC substrate axes. No contradictions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF (GO:1990756, verified real). GOA carries catalytic `GO:0004842 ubiquitin-protein transferase activity` (IDA) — the classic F-box mis-attribution of RBX1-RING catalysis to the receptor. The review correctly MODIFY's GO:0004842 → GO:1990756 AND adds GO:1990756 as a NEW IDA annotation. Bare `protein binding` (SNAI1, SKP1; 6 IPI rows) kept non-core. This is the canonical correct call. No unmet UPS NEW-term gap (SNAI1/HES1 degradation captured by GO:0031146/GO:0006511).
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review PMIDs (19955572 primary; 33234069 family; plus high-throughput SKP1 interactome PMIDs) are gene-specific. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; MODIFY(GO:0004842→GO:1990756) + NEW pattern correctly applied; substrate validated.

## Full Consistency Review

- **UniProt:** Q8N1E6 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box+LRR subtype/type `no_mapping`; class `context_only / too_broad / GO:0061630`; branch `no_mapping`.
- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL14 is the SCF(FBXL14) substrate receptor degrading SNAI1/SNAIL1 (PMID:19955572, IDA), with falcon adding HES1 (WRPW motif) and Thr58-phospho-c-MYC substrate axes. No contradictions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF (GO:1990756, verified real). GOA carries catalytic `GO:0004842 ubiquitin-protein transferase activity` (IDA) — the classic F-box mis-attribution of RBX1-RING catalysis to the receptor. The review correctly MODIFY's GO:0004842 → GO:1990756 AND adds GO:1990756 as a NEW IDA annotation. Bare `protein binding` (SNAI1, SKP1; 6 IPI rows) kept non-core. This is the canonical correct call. No unmet UPS NEW-term gap (SNAI1/HES1 degradation captured by GO:0031146/GO:0006511).
- **Mapping strategy:** Gene does not change the node. Status/scope right; catalysis excluded from sub-nodes. SNAI1 (and HES1) are validated substrates → adaptor MF experimentally grounded, not orphan/inferred-only. PN-projected GO:1990756 matches review core_functions MF exactly.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review PMIDs (19955572 primary; 33234069 family; plus high-throughput SKP1 interactome PMIDs) are gene-specific. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; MODIFY(GO:0004842→GO:1990756) + NEW pattern correctly applied; substrate validated.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL14/FBXL14-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q8N1E6
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
