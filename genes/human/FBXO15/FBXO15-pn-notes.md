# FBXO15 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NCQ5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO15/FBXO15-ai-review.yaml](FBXO15-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO15/FBXO15-ai-review.html
- Gene notes: missing - genes/human/FBXO15/FBXO15-notes.md
- GOA TSV: present - [genes/human/FBXO15/FBXO15-goa.tsv](FBXO15-goa.tsv)
- UniProt record: present - [genes/human/FBXO15/FBXO15-uniprot.txt](FBXO15-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO15.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO15.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO15/FBXO15-deep-research-falcon.md](FBXO15-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO15 (F-box only protein 15, FBX15) is a 510-amino-acid F-box protein of the "FBXO/other" class that serves as the substrate-recognition component of an SCF (SKP1-CUL1-F-box protein, also called CRL1) cullin-RING E3 ubiquitin ligase complex. Like other F-box proteins, it docks onto the SCF core through its F-box domain (residues 77-117), which binds the adaptor SKP1; SKP1 in turn bridges to the scaffold CUL1 and the catalytic RING subunit RBX1 that recruits the ubiquitin-charged E2 enzyme. FBXO15 therefore does not itself possess catalytic ubiquitin-transfer activity; it confers substrate specificity on the ligase, positioning a bound target protein for poly-ubiquitination and subsequent proteasomal degradation. Several substrates have been experimentally reported, often recruited through modification-dependent degrons: FBXO15 uniquely associates with and degrades cardiolipin synthase 1 (CLS1) in a PINK1-linked module (phospho-Thr219-dependent recognition; CLS1 Lys174 ubiquitination), an ER/cytosol-associated activity that limits mitochondrial cardiolipin and has been implicated in pneumonia/lung-injury models; it cooperates with the E2 CDC34/UBE2R1 to ubiquitinate the drug-efflux transporter P-glycoprotein (ABCB1/MDR1), so that FBXO15 loss raises P-gp levels and multidrug resistance; and in breast cancer it promotes ubiquitin-dependent degradation of the stemness/signaling factors SOX2 and STAT3, dampening EGFR/ERK/STAT3 signaling and acting as a tumor suppressor (higher FBXO15 expression correlating with better survival). In mouse embryonic stem cells the ortholog recognizes an acetyldegron on KBP (acetyl-Lys501) and is preferentially expressed in undifferentiated cells, linking it to pluripotency biology. FBXO15 is expressed broadly with enhancement in testis and fallopian tube. Two splice isoforms are produced, the shorter of which lacks the N-terminal region preceding the F-box domain. Despite these reports, most substrate-pathway links rest on individual studies and the integrated physiological role of human FBXO15 remains only partly defined.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 11; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review adds GO:1990756 as an explicit `action: NEW` MF annotation (GOA had no MF for FBXO15), which directly realizes the PN projection — tighter alignment than most siblings. DR ↔ YAML agree on the SCF adaptor role and reported substrates (CLS1, ABCB1/P-gp, SOX2, STAT3).
- **PN story / NEW pressure:** PN asserts the adaptor MF; review ADDs it as NEW (GO:1990756, verified real). This is a defensible ADD, not over-reach: UniProt states FBXO15 is a substrate-recognition component directly interacting with SKP1 and CUL1, and ComplexPortal has an FBXO15-variant SCF complex. Substrate links rest on single studies (Falcon UNVERIFIED), but family/complex membership is solid; not a substrate-less F-box at the family level.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:34445249 (SCF/ComplexPortal CPX-7925), 32814053 (JPH3 Y2H, bare protein binding, LOW), plus Falcon substrate leads. The one experimental annotation (protein binding/JPH3) is non-core. Expansion, no conflict.
- **Verdict:** Consistent; review's NEW GO:1990756 exactly implements the PN adaptor mapping.

## Full Consistency Review

- **UniProt:** Q8NCQ5 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent. Review adds GO:1990756 as an explicit `action: NEW` MF annotation (GOA had no MF for FBXO15), which directly realizes the PN projection — tighter alignment than most siblings. DR ↔ YAML agree on the SCF adaptor role and reported substrates (CLS1, ABCB1/P-gp, SOX2, STAT3).
- **PN story / NEW pressure:** PN asserts the adaptor MF; review ADDs it as NEW (GO:1990756, verified real). This is a defensible ADD, not over-reach: UniProt states FBXO15 is a substrate-recognition component directly interacting with SKP1 and CUL1, and ComplexPortal has an FBXO15-variant SCF complex. Substrate links rest on single studies (Falcon UNVERIFIED), but family/complex membership is solid; not a substrate-less F-box at the family level.
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 is at the right altitude (= the NEW MF the review added). Class GO:0061630 correctly too_broad.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:34445249 (SCF/ComplexPortal CPX-7925), 32814053 (JPH3 Y2H, bare protein binding, LOW), plus Falcon substrate leads. The one experimental annotation (protein binding/JPH3) is non-core. Expansion, no conflict.
- **Verdict:** Consistent; review's NEW GO:1990756 exactly implements the PN adaptor mapping.
- **Recommended edits:** none to FBXO15-ai-review.yaml. [MAP] none — node mapping and review concur.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO15/FBXO15-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q8NCQ5
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: (none)
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other
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
