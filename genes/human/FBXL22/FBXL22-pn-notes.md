# FBXL22 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6P050
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL22/FBXL22-ai-review.yaml](FBXL22-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL22/FBXL22-ai-review.html
- Gene notes: missing - genes/human/FBXL22/FBXL22-notes.md
- GOA TSV: present - [genes/human/FBXL22/FBXL22-goa.tsv](FBXL22-goa.tsv)
- UniProt record: present - [genes/human/FBXL22/FBXL22-uniprot.txt](FBXL22-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL22.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL22.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL22.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL22.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL22/FBXL22-deep-research-falcon.md](FBXL22-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL22 (F-box and leucine-rich protein 22) is a cardiac-enriched member of the FBXL subfamily of F-box proteins, with an N-terminal F-box domain and a C-terminal leucine-rich repeat (LRR) region. It serves as the substrate-recognition subunit of a Cullin-RING (SCF; SKP1-CUL1-F-box) E3 ubiquitin ligase, docking onto SKP1/CUL1 through its F-box domain and recruiting substrates via its LRRs. FBXL22 is enriched in striated (cardiac and skeletal) muscle and localizes to the sarcomeric Z-disc, where it binds and promotes the proteasome-dependent polyubiquitination and degradation of the Z-disc sarcomeric proteins alpha-actinin-2 (ACTN2) and filamin-C (FLNC), thereby controlling sarcomeric/cytoskeletal protein turnover and quality control. Loss of FBXL22 (e.g. in zebrafish) causes accumulation of alpha-actinin and progressive reduction in cardiac contractility, and FBXL22 is essential for maintenance of normal contractile function in vivo. Beyond steady-state cardiac maintenance, FBXL22 participates in sarcomere remodeling programs: in skeletal muscle it is an atrogene-like factor strongly and transiently induced during neurogenic atrophy (denervation, ~15-fold within days) and during myogenic differentiation, with isoform-dependent effects on muscle mass and myopathic phenotypes upon overexpression; and in zebrafish heart regeneration its expression is regulated by AP-1-dependent chromatin accessibility and it promotes sarcomere disassembly. Most mechanistic substrate/localization/contractility evidence derives from model organisms (zebrafish, mouse) and reviews rather than direct human assays.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 14; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Falcon DR (cardiac Z-disc adaptor; ACTN2/FLNC substrates; zebrafish contractility; denervation atrogene), review YAML, the PN F-box LRR receptor placement, and the GO:1990756 group mapping all converge. No contradictions.
- **PN story / NEW pressure:** PN projects GO:1990756 (verified real) as new_to_goa. Review does not add it as NEW but reaches the same endpoint via **`action: MODIFY` of the existing GO:0061630 ubiquitin protein ligase activity (IDA, PMID:22972877) → proposed_replacement GO:1990756** — the canonical F-box correction (catalysis is in RBX1, not the receptor). Net effect = adaptor MF present, matching PN. Conclude: already addressed by review via MODIFY; concordant with PN projection.
- **Evidence alignment:** PN reference is only "15340381 / rev"; review anchors on the gene-defining PMID:22972877 (HIGH/VERIFIED — Z-disc, ACTN2/FLNC, SKP1/CUL1, in vivo contractility) plus FBXL review PMID:33234069 and Falcon DR. Divergence benign — PN generic family review vs review's primary cardiac study.
- **Verdict:** Consistent; adaptor MF (GO:1990756) supplied via MODIFY of the mis-attributed catalytic term, matching PN. No over-reach.

## Full Consistency Review

- **UniProt:** Q6P050 (FBXL22) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group `Cul1 substrate receptor`=`mapped`/ok_for_propagation→GO:1990756; F-box/LRR subtype+type=`no_mapping`; class=`context_only`/too_broad→GO:0061630.
- **Consistency:** Fully consistent. Falcon DR (cardiac Z-disc adaptor; ACTN2/FLNC substrates; zebrafish contractility; denervation atrogene), review YAML, the PN F-box LRR receptor placement, and the GO:1990756 group mapping all converge. No contradictions.
- **PN story / NEW pressure:** PN projects GO:1990756 (verified real) as new_to_goa. Review does not add it as NEW but reaches the same endpoint via **`action: MODIFY` of the existing GO:0061630 ubiquitin protein ligase activity (IDA, PMID:22972877) → proposed_replacement GO:1990756** — the canonical F-box correction (catalysis is in RBX1, not the receptor). Net effect = adaptor MF present, matching PN. Conclude: already addressed by review via MODIFY; concordant with PN projection.
- **Mapping strategy:** Gene supports the node. KEY PATTERN exemplary: review explicitly demotes the catalytic ligase MF (the MGI IDA "ligase activity," which over-attributes RBX1 chemistry to the receptor) to the GO:1990756 adaptor term. PN class-level GO:0061630 correctly flagged too_broad. No broader/narrower mismatch.
- **Evidence alignment:** PN reference is only "15340381 / rev"; review anchors on the gene-defining PMID:22972877 (HIGH/VERIFIED — Z-disc, ACTN2/FLNC, SKP1/CUL1, in vivo contractility) plus FBXL review PMID:33234069 and Falcon DR. Divergence benign — PN generic family review vs review's primary cardiac study.
- **Verdict:** Consistent; adaptor MF (GO:1990756) supplied via MODIFY of the mis-attributed catalytic term, matching PN. No over-reach.
- **Recommended edits:** none to FBXL22-ai-review.yaml; PN mappings sound as-is.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL22/FBXL22-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q6P050
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR006553
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
