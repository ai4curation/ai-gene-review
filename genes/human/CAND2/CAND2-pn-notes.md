# CAND2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75155
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CAND2/CAND2-ai-review.yaml](CAND2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/CAND2/CAND2-ai-review.html
- Gene notes: missing - genes/human/CAND2/CAND2-notes.md
- GOA TSV: present - [genes/human/CAND2/CAND2-goa.tsv](CAND2-goa.tsv)
- UniProt record: present - [genes/human/CAND2/CAND2-uniprot.txt](CAND2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CAND2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CAND2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CAND2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CAND2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/CAND2/CAND2-deep-research-falcon.md](CAND2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: CAND2 (Cullin-associated NEDD8-dissociated protein 2; also TIP120B, TBP-interacting protein of 120 kDa B) is a large (~1236 aa) HEAT-repeat (alpha-solenoid) protein and the paralog of CAND1. Like CAND1, it functions as a regulator of cullin-RING ubiquitin ligase (CRL/SCF) assembly rather than as a ligase itself: it binds unneddylated, substrate-receptor-free cullin-RBX cores (CAND-bound cullins cannot be neddylated, and neddylated cullins do not stably bind CAND) and acts as an F-box-protein exchange factor, sequestering cullins and accelerating the dissociation/exchange of F-box (and other substrate-recognition) modules to dynamically reshape the cellular repertoire of active CRL complexes within the NEDD8/COP9-signalosome remodeling cycle. CAND2 has no catalytic ubiquitin-ligase activity of its own. Biochemically it binds the CUL1-RBX1 core comparably to CAND1 but catalyzes SCF disassembly with lower efficiency (higher KM, faster koff), and CAND1 and CAND2 can act nonredundantly to support optimal activity of specific SCF ligases (e.g. SCF(FBXL5)-mediated IRP2 turnover). It was originally identified as a TBP-interacting protein expressed preferentially in muscle and induced during myogenesis, where it binds CUL1 and suppresses SCF-dependent ubiquitination of the differentiation factor myogenin to accelerate myogenic differentiation; it also interacts with the transcription-related factors TBP and CNOT3/NOT3, and is a specific in vitro substrate of the HECT E3 ligase UBE3C/KIAA10, which targets it for proteasomal degradation. CAND2 is enriched in skeletal and cardiac muscle and is also found in epididymis; subcellular pools are reported in both the nucleus and the cytosol. Common variation at the CAND2 locus (rs4642101) is associated with atrial fibrillation risk.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 2; NEW: 1

## PN Consistency Summary

- **Consistency:** Deep research (falcon, HIGH), review YAML, and the dossier note all agree on the substance: CAND2/TIP120B is a muscle-enriched, non-catalytic CAND-family CRL/SCF F-box exchange factor (paralog of CAND1, less efficient; Wang 2025 kinetics, Shiraishi 2007 myogenin/CUL1, Liu 2002). All 14 GOA rows are reviewed. One framing mismatch: the PN node projects an *activator* term, but the review (correctly) stresses CAND2 can be functionally inhibitory in muscle (it suppresses SCF-mediated myogenin ubiquitination).
- **PN story / NEW pressure:** The PN core MF (cullin-RBX binding / exchange-factor activity) is genuinely absent from GOA. The review adds GO:0097602 cullin family protein binding as NEW (verified real, ISS basis) — well-justified and the right altitude. No catalytic-ligase term assigned (correct). SCF complex assembly (GO:0010265) already captures the BP.
- **Evidence alignment:** Divergent. PN cites only PMID:40011427 (the 2025 CAND2 exchange-factor paper); the review captures this same study via the falcon report (Wang 2025 Nat Commun) but does not list PMID:40011427 in `references`. Review PMIDs (12207886, 12692129, 23864651, 32296183) are not in the PN row.
- **Verdict:** Substantively consistent; PN activator mapping (GO:1990757) over-reaches and conflicts with the review's non-catalytic/context-inhibitory exchange-factor framing. Prefer review's GO:0097602 + GO:0010265. **Recommended edits:** [MAP] downgrade CAND2 type/subtype GO:1990757 mapping toward exchange-factor/cullin-binding (GO:0097602) or context_only, rather than "activator". [REF] add PMID:40011427 to CAND2 review `references` (currently only cited via falcon report).

## Full Consistency Review

- **UniProt:** O75155 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor|Armadillo-like` ; **PN-node mapping:** type/subtype mapped, scope=ok_for_propagation_to_go, GO:1990757 ubiquitin ligase activator activity (group/class context_only; branch no_mapping)
- **Consistency:** Deep research (falcon, HIGH), review YAML, and the dossier note all agree on the substance: CAND2/TIP120B is a muscle-enriched, non-catalytic CAND-family CRL/SCF F-box exchange factor (paralog of CAND1, less efficient; Wang 2025 kinetics, Shiraishi 2007 myogenin/CUL1, Liu 2002). All 14 GOA rows are reviewed. One framing mismatch: the PN node projects an *activator* term, but the review (correctly) stresses CAND2 can be functionally inhibitory in muscle (it suppresses SCF-mediated myogenin ubiquitination).
- **PN story / NEW pressure:** The PN core MF (cullin-RBX binding / exchange-factor activity) is genuinely absent from GOA. The review adds GO:0097602 cullin family protein binding as NEW (verified real, ISS basis) — well-justified and the right altitude. No catalytic-ligase term assigned (correct). SCF complex assembly (GO:0010265) already captures the BP.
- **Mapping strategy:** Concern. GO:1990757 ("Binds to and increases the activity of a ubiquitin ligase" — verified, strictly positive) over-reaches: CAND family activity is directionally context-dependent (exchange/remodeling, inhibitory in the muscle/myogenin context), echoing the dossier's own "different directionality" caveat at the group level. The review deliberately does NOT assign GO:1990757. PN-projected term is broader/mis-directional vs the review's GO:0097602 + GO:0010265.
- **Evidence alignment:** Divergent. PN cites only PMID:40011427 (the 2025 CAND2 exchange-factor paper); the review captures this same study via the falcon report (Wang 2025 Nat Commun) but does not list PMID:40011427 in `references`. Review PMIDs (12207886, 12692129, 23864651, 32296183) are not in the PN row.
- **Verdict:** Substantively consistent; PN activator mapping (GO:1990757) over-reaches and conflicts with the review's non-catalytic/context-inhibitory exchange-factor framing. Prefer review's GO:0097602 + GO:0010265. **Recommended edits:** [MAP] downgrade CAND2 type/subtype GO:1990757 mapping toward exchange-factor/cullin-binding (GO:0097602) or context_only, rather than "activator". [REF] add PMID:40011427 to CAND2 review `references` (currently only cited via falcon report).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/CAND2/CAND2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | CRL regulator | F-box exchange factor | Armadillo-like
- UniProt: O75155
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR011989
- PN references (titles):
    - 40011427
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor|Armadillo-like
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990757 ubiquitin ligase activator activity]
        rationale: This PN type captures CAND-family exchange factors that activate/remodel cullin-RING ligase assemblies. The closest shared GO activity is ubiquitin ligase activator activity.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990757 ubiquitin ligase activator activity]
        rationale: This PN type captures CAND-family exchange factors that activate/remodel cullin-RING ligase assemblies. The closest shared GO activity is ubiquitin ligase activator activity.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator
        status=context_only scope=too_broad_to_propagate GO=[GO:1904666 regulation of ubiquitin protein ligase activity]
        rationale: This PN group records regulation of cullin-RING ligase systems, but the members include inhibitors, exchange factors, and modulators with different directionality. It is context only.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:1990757 ubiquitin ligase activator activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor
- GO:1990757 ubiquitin ligase activator activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor|Armadillo-like

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
