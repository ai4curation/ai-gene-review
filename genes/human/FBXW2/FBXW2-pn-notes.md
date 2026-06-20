# FBXW2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKT8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW2/FBXW2-ai-review.yaml](FBXW2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW2/FBXW2-ai-review.html
- Gene notes: missing - genes/human/FBXW2/FBXW2-notes.md
- GOA TSV: present - [genes/human/FBXW2/FBXW2-goa.tsv](FBXW2-goa.tsv)
- UniProt record: present - [genes/human/FBXW2/FBXW2-uniprot.txt](FBXW2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW2/FBXW2-deep-research-falcon.md](FBXW2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW2 (FBW2) is an F-box/WD40-repeat protein that serves as a substrate-recognition subunit of the canonical SCF (SKP1-CUL1-RBX1) E3 ubiquitin ligase, forming the SCF(FBXW2) complex. Through its N-terminal F-box motif it binds SKP1 (which bridges to the CUL1-RBX1 catalytic core), while its five WD40 repeats provide a substrate-binding surface that recognizes (often phosphorylation-marked) target proteins and presents them for RBX1/RING-dependent polyubiquitination and proteasomal degradation; FBXW2 itself does not catalyze ubiquitin transfer. Characterized substrates include the transcription factor GCM1 (glial cell missing 1), whose turnover FBXW2 controls during placental cell migration and invasion (counter-regulated by RACK1, which competes with GCM1 for FBXW2 binding); the SCF receptor SKP2 (via a TSELLS-type degron) and β-catenin, whose FBXW2-mediated degradation suppresses proliferation and invasion of lung cancer cells; the kinase MAP3K7/TAK1, targeted for K48-linked polyubiquitination in hepatocellular carcinoma; NF-κB p65/RELA, ubiquitinated at K122 in a phosphorylation-dependent, p300-acetylation-antagonized manner to suppress breast cancer stemness and chemoresistance; the cytoskeletal effector Moesin, K48-polyubiquitinated unless protected by AKT phosphorylation at Thr558 (an AKT-Moesin-SKP2 axis); and EGFR (via a TSNNST-type degron). A non-oncologic role has also been reported in myeloid cells, where FBXW2 degrades KSRP and modulates obesity-associated inflammation. Across substrates FBXW2 acts largely as a tumor suppressor, and its substrate engagement is frequently conditional on substrate phosphorylation. FBXW2 is itself a substrate of SCF(β-TrCP1) (recognized via a phospho-dependent SSGART motif), placing it within a β-TrCP1-FBXW2-SKP2 regulatory axis. It is a predominantly cytoplasmic/cytosolic protein, though it can also ubiquitinate shuttling substrates such as p65 in the nucleus. As with other client proteins it associates transiently with the HSP90-CDC37 chaperone system during its own folding/maturation.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 16; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research (falcon), review YAML, PN annotation, and PN-node mapping all converge on FBXW2 as a non-catalytic SCF(FBXW2) substrate receptor. Description, core_functions (2x GO:1990756) and the MODIFY of the catalytic GO:0004842→GO:1990756 all match the PN projected term. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic Cul1-receptor adaptor role, which the review already captures: GO:1990756 is introduced via MODIFY (transferase IEA/TAS) — it is NOT in current GOA, so projection is correctly `new_to_goa`. Term verified real via OLS. No additional NEW term needed; substrate biology (GCM1, SKP2, β-catenin, TAK1, p65, Moesin, EGFR) is well captured by description/core_functions and the GO:0031146 catabolic process. Conclusion: already captured / ADD GO:1990756 (which the review's MODIFY already proposes).
- **Evidence alignment:** PN cites only PMID:15340381 (Cardozo & Pagano SCF review) "/ rev" — a family review, not in the review's reference list but consistent with it. Review draws substrate evidence from PMID:23651062 (GCM1/RACK1, HIGH) and PMID:35414786 (SKP2/β-catenin/TAK1, HIGH) plus falcon. Divergence is benign: PN uses the family-level review, the YAML uses gene-specific primary literature.
- **Verdict:** CONSISTENT — no edits. Validated F-box receptor; GO:1990756 ADD already handled by review MODIFY.

## Full Consistency Review

- **UniProt:** Q9UKT8 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (high quality)
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40` ; **PN-node mapping:** group=mapped/ok_for_propagation_to_go GO:1990756 (ubiquitin-like ligase-substrate adaptor activity); class=context_only/too_broad GO:0061630; subtype/type/branch=no_mapping
- **Consistency:** Fully consistent. Deep research (falcon), review YAML, PN annotation, and PN-node mapping all converge on FBXW2 as a non-catalytic SCF(FBXW2) substrate receptor. Description, core_functions (2x GO:1990756) and the MODIFY of the catalytic GO:0004842→GO:1990756 all match the PN projected term. No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic Cul1-receptor adaptor role, which the review already captures: GO:1990756 is introduced via MODIFY (transferase IEA/TAS) — it is NOT in current GOA, so projection is correctly `new_to_goa`. Term verified real via OLS. No additional NEW term needed; substrate biology (GCM1, SKP2, β-catenin, TAK1, p65, Moesin, EGFR) is well captured by description/core_functions and the GO:0031146 catabolic process. Conclusion: already captured / ADD GO:1990756 (which the review's MODIFY already proposes).
- **Mapping strategy:** Correct. Group-level GO:1990756 is neither broader nor narrower than the review's core MF; this is the recurring correct call (adaptor activity replacing catalytic transferase). Status/scope appropriate; class-level GO:0061630 correctly held as too_broad. No node change warranted.
- **Evidence alignment:** PN cites only PMID:15340381 (Cardozo & Pagano SCF review) "/ rev" — a family review, not in the review's reference list but consistent with it. Review draws substrate evidence from PMID:23651062 (GCM1/RACK1, HIGH) and PMID:35414786 (SKP2/β-catenin/TAK1, HIGH) plus falcon. Divergence is benign: PN uses the family-level review, the YAML uses gene-specific primary literature.
- **Verdict:** CONSISTENT — no edits. Validated F-box receptor; GO:1990756 ADD already handled by review MODIFY.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW2/FBXW2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: Q9UKT8
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001680
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40
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
