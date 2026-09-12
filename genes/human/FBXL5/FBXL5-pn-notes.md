# FBXL5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKA1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL5/FBXL5-ai-review.yaml](FBXL5-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL5/FBXL5-ai-review.html
- Gene notes: missing - genes/human/FBXL5/FBXL5-notes.md
- GOA TSV: present - [genes/human/FBXL5/FBXL5-goa.tsv](FBXL5-goa.tsv)
- UniProt record: present - [genes/human/FBXL5/FBXL5-uniprot.txt](FBXL5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL5/FBXL5-deep-research-falcon.md](FBXL5-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL5 (F-box/LRR-repeat protein 5) is the substrate-recognition (F-box) subunit of an SCF (SKP1-CUL1-F-box) cullin-RING E3 ubiquitin ligase that is the master sensor coupling cellular iron and oxygen status to the stability of the iron regulatory proteins IRP2/IREB2 and IRP1/ACO1. Within the SCF complex, FBXL5 binds SKP1 through its F-box domain and uses its leucine-rich repeats to recruit substrate, thereby directing CUL1-RBX1-mediated polyubiquitination and proteasomal degradation of IRP2. FBXL5 carries two metal-sensing modules: an N-terminal hemerythrin-like (Hr) domain with a diiron center that binds iron and oxygen, and a C-terminal redox-sensitive [2Fe-2S] cluster. In iron- and oxygen-replete cells the Hr domain is loaded and stable and the oxidized [2Fe-2S] cluster enables substrate (IRP2) recruitment, so the SCF(FBXL5) ligase degrades IRP2 and shuts down the iron-starvation response. Under iron deficiency or hypoxia the Hr domain cannot bind iron, FBXL5 undergoes conformational destabilization and is itself ubiquitinated and degraded, allowing IRP2 to accumulate, bind iron-responsive elements, and upregulate iron uptake. FBXL5 thus sits at the center of mammalian iron homeostasis. Additional reported substrates include the dynactin subunit DCTN1/p150-glued, the EMT transcription factor SNAI1/Snail1 (ubiquitinated in the nucleus), and the single-stranded DNA-binding protein NABP2/hSSB1, linking FBXL5 to cytoskeletal regulation, EMT, and the DNA-damage response. The oxidized [2Fe-2S] cluster only forms when both iron and oxygen are sufficient, so its redox state gates IRP2 recruitment, making FBXL5 a combined iron-and-oxygen sensor; at steady state FBXL5 also undergoes constitutive HERC2-mediated ubiquitin-dependent turnover. Loss of FBXL5 derepresses the IRP2-driven iron-acquisition program, causing intracellular iron overload; consistent with this, liver-specific Fbxl5 knockout sensitizes hepatocytes to iron-dependent ferroptosis, framing FBXL5 as a physiological brake on iron accumulation and ferroptotic injury.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 28; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep research, review YAML, PN annotation, and node mapping agree: FBXL5 is the iron/oxygen-sensing SCF substrate receptor for IRP2/IREB2. Rich experimental backbone (PMID:19762596 IMP/IDA, 19762597 IDA/IEP, 17532294 DCTN1, 24157836 SNAI1). No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF. The review goes well beyond: it keeps the experimentally validated `GO:0005506 iron ion binding` (IDA) as a co-core MF — a real function the PN mapping does NOT capture — and MODIFY's the catalytic `GO:0004842` (NAS) to GO:1990756. The review also PROPOSES a new term "iron- and oxygen-sensing ubiquitin-ligase substrate adaptor activity" (child of GO:1990756). OLS search returns no existing GO equivalent, so this is a legitimate candidate-new-term, not a duplicate; correctly justified as more precise than GO:1990756. Conclusion: adaptor MF captured; the iron-sensing MF + proposed child are an ADD beyond the PN story (defensible).
- **Evidence alignment:** PN cites only "15340381/rev" (PMID:15340381). The review does not cite it; it uses gene-specific primaries plus falcon. Benign placeholder divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits needed. Note: proposed_new_term (iron/oxygen-sensing adaptor) is verified as not pre-existing in GO — keep as candidate (unverified existence elsewhere, but no GO clash).

## Full Consistency Review

- **UniProt:** Q9UKA1 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; class `context_only / too_broad / GO:0061630`.
- **Consistency:** Strong. Deep research, review YAML, PN annotation, and node mapping agree: FBXL5 is the iron/oxygen-sensing SCF substrate receptor for IRP2/IREB2. Rich experimental backbone (PMID:19762596 IMP/IDA, 19762597 IDA/IEP, 17532294 DCTN1, 24157836 SNAI1). No contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor MF. The review goes well beyond: it keeps the experimentally validated `GO:0005506 iron ion binding` (IDA) as a co-core MF — a real function the PN mapping does NOT capture — and MODIFY's the catalytic `GO:0004842` (NAS) to GO:1990756. The review also PROPOSES a new term "iron- and oxygen-sensing ubiquitin-ligase substrate adaptor activity" (child of GO:1990756). OLS search returns no existing GO equivalent, so this is a legitimate candidate-new-term, not a duplicate; correctly justified as more precise than GO:1990756. Conclusion: adaptor MF captured; the iron-sensing MF + proposed child are an ADD beyond the PN story (defensible).
- **Mapping strategy:** Gene does not change the node; group GO:1990756 is appropriate and matches review core_functions. PN scope correct. The metal-sensing layer is gene-specific and rightly stays out of the shared node mapping. Canonical, validated-substrate receptor — no orphan flag.
- **Evidence alignment:** PN cites only "15340381/rev" (PMID:15340381). The review does not cite it; it uses gene-specific primaries plus falcon. Benign placeholder divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits needed. Note: proposed_new_term (iron/oxygen-sensing adaptor) is verified as not pre-existing in GO — keep as candidate (unverified existence elsewhere, but no GO clash).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL5/FBXL5-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q9UKA1
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
