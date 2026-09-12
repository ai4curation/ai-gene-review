# FBXL7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UJT9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL7/FBXL7-ai-review.yaml](FBXL7-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL7/FBXL7-ai-review.html
- Gene notes: missing - genes/human/FBXL7/FBXL7-notes.md
- GOA TSV: present - [genes/human/FBXL7/FBXL7-goa.tsv](FBXL7-goa.tsv)
- UniProt record: present - [genes/human/FBXL7/FBXL7-uniprot.txt](FBXL7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL7/FBXL7-deep-research-falcon.md](FBXL7-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL7 (F-box/LRR-repeat protein 7) is the substrate-recognition (F-box) subunit of an SCF (SKP1-CUL1-RBX1-F-box) cullin-RING E3 ubiquitin ligase that controls mitotic progression and apoptosis by directing the ubiquitination and proteasomal degradation of mitotic regulators. Within the SCF(FBXL7) complex, FBXL7 binds SKP1 via its F-box domain and uses its leucine-rich repeats to recruit substrates, so that CUL1-RBX1 drives their polyubiquitination. Its best-characterized substrates are the mitotic kinase Aurora A (AURKA), which FBXL7 colocalizes with and targets for centrosomal degradation during mitosis to promote mitotic arrest, and the inhibitor-of-apoptosis protein survivin/BIRC5 (recognized via survivin Glu126; ubiquitinated at Lys90/Lys91), whose FBXL7-mediated degradation regulates mitochondrial function and promotes apoptosis. FBXL7 (a 491-residue protein with an N-terminal F-box motif and roughly eleven C-terminal leucine-rich repeats) additionally targets active c-SRC (after Ser104 phosphorylation) and the EMT transcription factor SNAI1/Snail1 for degradation, acting as a metastasis suppressor that restrains SRC- and Snail1-driven epithelial-mesenchymal transition and invasion, and it ubiquitinates the glycolytic enzyme PFKFB4, coupling FBXL7 to metabolic reprogramming. FBXL7 localizes to the centrosome during spindle formation. FBXL7 is itself a proapoptotic factor whose cellular abundance is controlled by the related F-box protein FBXL18, which ubiquitinates FBXL7 (at Lys109) for proteasomal degradation, and its expression is repressed transcriptionally (e.g. by hypoxia-induced EZH2 and by promoter hypermethylation in cancer). Through these activities FBXL7 contributes to the G2/M transition, spindle dynamics, apoptotic signaling, EMT/metastasis suppression, and metabolic control, and is implicated in cancer progression and drug resistance.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 25; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep research, review, PN annotation, and node mapping all describe FBXL7 as the SCF(FBXL7) receptor degrading AURKA and survivin/BIRC5 (validated: PMID:25778398 IDA, 28218735 IMP; FBXL18→FBXL7 axis PMID:25654763). Falcon extra substrates (c-SRC, SNAI1, PFKFB4) marked UNVERIFIED and held as leads. No contradictions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. FBXL7 GOA has NO MF beyond `protein binding` (no catalytic transferase). The review adds `GO:1990756` as **action: NEW (IDA, PMID:25778398)** — exactly the batch-correct call, and it matches the PN-projected term (GO:1990756, goa_status=new_to_goa). Validated substrates already drive `G2/M transition`, `regulation of apoptotic process`, `SCF-dependent catabolism` BPs. Conclusion: adaptor MF correctly ADDED as NEW; no over-reach.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses gene-specific primaries (25778398, 28218735, 25654763, 33234069) — no overlap with the PN placeholder, richer evidence in review. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. Exemplary application of the NEW→GO:1990756 pattern. No edits required.

## Full Consistency Review

- **UniProt:** Q9UJT9 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; class `context_only / too_broad / GO:0061630`.
- **Consistency:** Strong. Deep research, review, PN annotation, and node mapping all describe FBXL7 as the SCF(FBXL7) receptor degrading AURKA and survivin/BIRC5 (validated: PMID:25778398 IDA, 28218735 IMP; FBXL18→FBXL7 axis PMID:25654763). Falcon extra substrates (c-SRC, SNAI1, PFKFB4) marked UNVERIFIED and held as leads. No contradictions.
- **PN story / NEW pressure:** PN asserts the generic adaptor MF. FBXL7 GOA has NO MF beyond `protein binding` (no catalytic transferase). The review adds `GO:1990756` as **action: NEW (IDA, PMID:25778398)** — exactly the batch-correct call, and it matches the PN-projected term (GO:1990756, goa_status=new_to_goa). Validated substrates already drive `G2/M transition`, `regulation of apoptotic process`, `SCF-dependent catabolism` BPs. Conclusion: adaptor MF correctly ADDED as NEW; no over-reach.
- **Mapping strategy:** Gene does not change the node. Status/scope right; PN-projected GO:1990756 is identical to the review MF (not broader/narrower). Canonical, multiply-validated substrate receptor (AURKA, survivin) — no orphan flag. Note: FBXL7 review already encodes the MF directly, so the PN "new_to_goa" projection is consistent with the review having materialized it.
- **Evidence alignment:** PN cites only "15340381/rev"; review uses gene-specific primaries (25778398, 28218735, 25654763, 33234069) — no overlap with the PN placeholder, richer evidence in review. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. Exemplary application of the NEW→GO:1990756 pattern. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL7/FBXL7-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q9UJT9
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
