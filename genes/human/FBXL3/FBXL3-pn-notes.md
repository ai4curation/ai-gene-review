# FBXL3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKT7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL3/FBXL3-ai-review.yaml](FBXL3-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL3/FBXL3-ai-review.html
- Gene notes: missing - genes/human/FBXL3/FBXL3-notes.md
- GOA TSV: present - [genes/human/FBXL3/FBXL3-goa.tsv](FBXL3-goa.tsv)
- UniProt record: present - [genes/human/FBXL3/FBXL3-uniprot.txt](FBXL3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL3/FBXL3-deep-research-falcon.md](FBXL3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL3 (F-box/LRR-repeat protein 3) is the substrate-recognition (F-box) subunit of an SCF (SKP1-CUL1-RBX1-F-box) cullin-RING E3 ubiquitin ligase that controls the mammalian circadian clock by targeting the cryptochrome repressors CRY1 and CRY2 for ubiquitination and proteasomal degradation. Within the predominantly nuclear SCF(FBXL3) complex, FBXL3 binds SKP1 through its F-box domain and uses its leucine-rich repeats to capture CRY: a conserved C-terminal tail of FBXL3 inserts into the FAD-binding pocket of CRY and buries the PER-binding interface, an interaction that can be displaced by FAD and by the Period proteins. By timing CRY degradation, SCF(FBXL3) sets the period and robustness of the circadian oscillator, permitting reactivation of the CLOCK-BMAL1 transcriptional activator and the consequent rhythmic expression of clock-controlled genes including Per1/Per2. Its activity is counterbalanced by the related SCF(FBXL21) ligase, which stabilizes CRY. In humans, biallelic loss-of-function variants in FBXL3 cause an autosomal-recessive intellectual developmental disorder with short stature.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 28; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Strong. Deep research (falcon), review YAML, PN annotation, and node mapping all describe FBXL3 as the SCF(FBXL3) substrate receptor that degrades CRY1/CRY2 to set circadian period. No contradictions. Falcon-only leads (K48 chain elongation, substrate-gated assembly, KL001 pocket) are flagged UNVERIFIED but corroborated by the experimental cache (PMID:17463251 IMP/IDA; PMID:23503662 structure).
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF (GO:1990756). This is NOT already an MF in the GOA, which carries only catalytic `GO:0004842` (IDA/IEA/NAS) + `protein binding`. The review correctly MODIFY's the two catalytic transferase annotations to GO:1990756 (verified real, current). No new BP pressure; circadian/SCF-catabolism BPs already captured. Conclusion: adaptor MF added by MODIFY = correct, not over-reaching.
- **Evidence alignment:** PN reference is only "15340381/rev" (PMID:15340381, an FBXL/Cul1 review). The review does NOT cite PMID:15340381; its key PMIDs (17463251, 23503662, 10531035, 33234069) are richer/gene-specific. Divergence is benign — PN uses a family-level placeholder; review uses primary literature.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; the MODIFY→GO:1990756 pattern is correctly applied. Optional [REF]: PN-row reference PMID:15340381 not reflected in review (placeholder only).

## Full Consistency Review

- **UniProt:** Q9UKT7 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box/LRR subtype+type `no_mapping`; class `context_only / too_broad / GO:0061630`.
- **Consistency:** Strong. Deep research (falcon), review YAML, PN annotation, and node mapping all describe FBXL3 as the SCF(FBXL3) substrate receptor that degrades CRY1/CRY2 to set circadian period. No contradictions. Falcon-only leads (K48 chain elongation, substrate-gated assembly, KL001 pocket) are flagged UNVERIFIED but corroborated by the experimental cache (PMID:17463251 IMP/IDA; PMID:23503662 structure).
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF (GO:1990756). This is NOT already an MF in the GOA, which carries only catalytic `GO:0004842` (IDA/IEA/NAS) + `protein binding`. The review correctly MODIFY's the two catalytic transferase annotations to GO:1990756 (verified real, current). No new BP pressure; circadian/SCF-catabolism BPs already captured. Conclusion: adaptor MF added by MODIFY = correct, not over-reaching.
- **Mapping strategy:** Gene does not change the node. Status/scope are right: the F-box adaptor MF lives at the group node, catalysis correctly excluded from the F-box/LRR sub-nodes (RBX1 RING does catalysis). PN-projected GO:1990756 matches the review's core_functions MF exactly (neither broader nor narrower). Canonical, well-validated SCF receptor (CRY substrate validated) — no orphan flag.
- **Evidence alignment:** PN reference is only "15340381/rev" (PMID:15340381, an FBXL/Cul1 review). The review does NOT cite PMID:15340381; its key PMIDs (17463251, 23503662, 10531035, 33234069) are richer/gene-specific. Divergence is benign — PN uses a family-level placeholder; review uses primary literature.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; the MODIFY→GO:1990756 pattern is correctly applied. Optional [REF]: PN-row reference PMID:15340381 not reflected in review (placeholder only).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL3/FBXL3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q9UKT7
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR032675
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
