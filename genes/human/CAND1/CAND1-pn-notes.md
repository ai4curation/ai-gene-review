# CAND1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86VP6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CAND1/CAND1-ai-review.yaml](CAND1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CAND1/CAND1-ai-review.html](CAND1-ai-review.html)
- Gene notes: present - [genes/human/CAND1/CAND1-notes.md](CAND1-notes.md)
- GOA TSV: present - [genes/human/CAND1/CAND1-goa.tsv](CAND1-goa.tsv)
- UniProt record: present - [genes/human/CAND1/CAND1-uniprot.txt](CAND1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CAND1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CAND1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CAND1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CAND1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CAND1 (Cullin-Associated and Neddylation-Dissociated 1; originally TIP120A) is a large HEAT-repeat protein that regulates the assembly and dynamic remodeling of cullin-RING E3 ubiquitin ligases (CRLs), most prominently SCF (SKP1-CUL1-F-box) complexes. CAND1 binds the unneddylated CUL1-RBX1 (ROC1) catalytic core and clamps around the cullin scaffold, with a beta-hairpin occupying the SKP1-adaptor binding site so that SKP1/F-box subunits cannot bind simultaneously. Rather than acting as a static inhibitor, CAND1 functions as a substrate-receptor (F-box protein) exchange factor: it accelerates dissociation of existing SCF complexes and promotes exchange of F-box receptors, allowing a common cullin-RBX1 core to be redistributed among many different substrate receptors. Its action is reciprocally coupled to the neddylation cycle - CUL1 neddylation (and binding of SKP1/F-box plus substrate) dissociates CAND1, while deneddylation regenerates the CAND1-bound state. Through this exchange activity CAND1 is a positive regulator of overall CRL activity in vivo and acts on cullins broadly, not just CUL1. CAND1 is predominantly cytoplasmic with nuclear pools, and it is a regulator/assembly factor rather than a catalytic ubiquitin-transfer enzyme.
- Existing/core annotation action counts: ACCEPT: 27; MARK_AS_OVER_ANNOTATED: 29

## PN Consistency Summary

- **Consistency:** Consistent. PN, review, notes and (no separate deep-research file; review references serve) all describe CAND1 as the CUL1-RBX1-binding **F-box/substrate-receptor exchange factor** that remodels SCF/CRL complexes and is a positive regulator of CRL activity in vivo (PMID:12504026, 15537541, 21249194). PN's "F-box exchange factor / Armadillo-like (HEAT-repeat)" matches the review's mechanism exactly.
- **PN story / NEW pressure:** PN projects GO:1990757 "ubiquitin ligase activator activity" (verified real; def "binds to and increases the activity of a ubiquitin ligase"). This aligns with the review's conclusion that CAND1 is an in-vivo positive regulator of CRL activity and is genuinely NEW to GOA (current GOA carries SCF assembly / part-of CRL, not an activator MF). It is defensible as ADD. Separately, the review independently proposes a finer NEW term "cullin-RING ligase substrate-receptor exchange factor activity" — I verified via OLS that NO such GO term exists (candidate, correctly flagged as new). So GO:1990757 is the best existing real term and is a sound PN-node addition; the review's bespoke term is a legitimate future request.
- **Evidence alignment:** PN row cites reference 23453757 (title not resolved in dossier). Review supports activator/exchange role via PMID:12504026, 15537541, 21249194, 12609982. Overlap is thematic (CRL assembly regulation); the PN-cited 23453757 is not in the review's reference list — minor divergence worth noting.
- **Verdict:** Consistent and the strongest ADD case of the six — GO:1990757 (real) is a defensible new MF for CAND1, matching both PN and the review's positive-regulator framing. **Recommended edits:** [YAML] consider adding GO:1990757 ubiquitin ligase activator activity to CAND1 existing/core (currently only proposed as a bespoke new term); [REF] confirm PN reference 23453757 and add to the review if it supports the activator role.

## Full Consistency Review

- **UniProt:** Q86VP6 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|F-box exchange factor|Armadillo-like` ; **PN-node mapping:** F-box-exchange-factor type/subtype → mapped/ok_for_propagation GO:1990757 ubiquitin ligase activator activity (new_to_goa); CRL-regulator group → context_only/too_broad GO:1904666; E3-ligases class → context_only GO:0061630.
- **Consistency:** Consistent. PN, review, notes and (no separate deep-research file; review references serve) all describe CAND1 as the CUL1-RBX1-binding **F-box/substrate-receptor exchange factor** that remodels SCF/CRL complexes and is a positive regulator of CRL activity in vivo (PMID:12504026, 15537541, 21249194). PN's "F-box exchange factor / Armadillo-like (HEAT-repeat)" matches the review's mechanism exactly.
- **PN story / NEW pressure:** PN projects GO:1990757 "ubiquitin ligase activator activity" (verified real; def "binds to and increases the activity of a ubiquitin ligase"). This aligns with the review's conclusion that CAND1 is an in-vivo positive regulator of CRL activity and is genuinely NEW to GOA (current GOA carries SCF assembly / part-of CRL, not an activator MF). It is defensible as ADD. Separately, the review independently proposes a finer NEW term "cullin-RING ligase substrate-receptor exchange factor activity" — I verified via OLS that NO such GO term exists (candidate, correctly flagged as new). So GO:1990757 is the best existing real term and is a sound PN-node addition; the review's bespoke term is a legitimate future request.
- **Mapping strategy:** Type/subtype projection of GO:1990757 onto CAND1 is appropriate and adds value over current GOA. The group/class context_only (too_broad) calls are correct (CRL-regulator descendants mix inhibitors and activators; E3 class mixes catalytic/scaffold/adaptor). No precedent-style over-broadening here.
- **Evidence alignment:** PN row cites reference 23453757 (title not resolved in dossier). Review supports activator/exchange role via PMID:12504026, 15537541, 21249194, 12609982. Overlap is thematic (CRL assembly regulation); the PN-cited 23453757 is not in the review's reference list — minor divergence worth noting.
- **Verdict:** Consistent and the strongest ADD case of the six — GO:1990757 (real) is a defensible new MF for CAND1, matching both PN and the review's positive-regulator framing. **Recommended edits:** [YAML] consider adding GO:1990757 ubiquitin ligase activator activity to CAND1 existing/core (currently only proposed as a bespoke new term); [REF] confirm PN reference 23453757 and add to the review if it supports the activator role.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CAND1/CAND1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | CRL regulator | F-box exchange factor | Armadillo-like
- UniProt: Q86VP6
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR011989
- PN references (titles):
    - 23453757
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
