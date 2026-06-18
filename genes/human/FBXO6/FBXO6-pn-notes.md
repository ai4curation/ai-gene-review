# FBXO6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NRD1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO6/FBXO6-ai-review.yaml](FBXO6-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO6/FBXO6-ai-review.html
- Gene notes: missing - genes/human/FBXO6/FBXO6-notes.md
- GOA TSV: present - [genes/human/FBXO6/FBXO6-goa.tsv](FBXO6-goa.tsv)
- UniProt record: present - [genes/human/FBXO6/FBXO6-uniprot.txt](FBXO6-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO6.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO6.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO6/FBXO6-deep-research-falcon.md](FBXO6-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO6 (FBG2/FBS2, F-box protein that recognizes sugar chains 2) is a 293-amino-acid cytoplasmic F-box protein and a member of the FBA (F-box-associated) lectin family (FBXO2/FBXO6/FBXO17/FBXO27/FBXO44). It serves as the substrate-recognition subunit of SCF (SKP1-CUL1-F-box) E3 ubiquitin ligase complexes: its N-terminal F-box domain docks onto SKP1 (and thence CUL1-RBX1), while its C-terminal FBA/G domain is a carbohydrate-binding lectin module that recognizes N-linked glycans on client proteins. As an F-box protein FBXO6 has no intrinsic catalytic activity; catalysis is contributed by the RING subunit RBX1 within the assembled SCF complex, and FBXO6 confers substrate specificity. Through its FBA domain FBXO6 binds high-mannose oligosaccharides (with the chitobiose core being essential), complex-type glycans, and sulfated glycoproteins, and it preferentially engages denatured/misfolded glycoproteins. This lectin activity directs misfolded glycoproteins that have been retrotranslocated to the cytosol into the endoplasmic-reticulum-associated degradation (ERAD)/glycoprotein-quality-control pathway, promoting their ubiquitination and proteasomal degradation. FBXO6 also has a documented role in the DNA replication/damage checkpoint: it recognizes activated, S345-phosphorylated CHEK1 (CHK1) via its FBA domain and assembles an SCF(FBXO6) complex that ubiquitinates CHK1 and targets it for degradation, contributing to checkpoint termination and influencing cellular sensitivity to replication stress. FBXO6 is broadly but variably expressed (notably in liver and kidney) and interacts with VCP/p97. Among its glycoprotein clients, SCF(FBXO6/Fbs2) ubiquitinates the ER-membrane transcription factor NFE2L1/NRF1; in the absence of the cytoplasmic deglycosylase NGLY1, FBXO6-mediated ubiquitination of still-glycosylated NFE2L1 impairs its processing and nuclear function, blunting the proteasome "bounce-back" induction of new proteasome subunits, and genetic reduction of Fbs2/FBXO6 partially rescues Ngly1-knockout phenotypes in mice (with Fbs2-knockout mice otherwise healthy).
- Existing/core annotation action counts: ACCEPT: 27; KEEP_AS_NON_CORE: 15; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent. Falcon DR (NGLY1/NFE2L1 axis, proteasome bounce-back), review YAML, and the PN FBA F-box receptor placement converge. SPECIAL CASE confirmed: FBA lectin (GO:0030246, verified real) binding high-mannose/complex/sulfated glycans (chitobiose core essential, PMID:18203720), feeding glycoprotein-ERAD; plus a documented CHK1-degradation/checkpoint role (PMID:19716789, IDA).
- **PN story / NEW pressure:** PN projects the generic GO:1990756 adaptor term (new_to_goa). Review's **core MF is GO:0030246 carbohydrate binding (ACCEPT, already in GOA; experimentally grounded by PMID:18203720 glycan-array)** — more informative than the generic adaptor. Catalytic GO:0061630 correctly held at contributes_to/non-core. The CHK1/DNA-damage-checkpoint role (GO:0000077) is a real second process kept non-core; review aptly MARK_AS_OVER_ANNOTATED for the GO:0006281 DNA repair term (FBXO6 terminates CHK1, is not a repair factor). Conclude: gene's distinctive lectin MF already captured; generic PN adaptor term not the best core.
- **Evidence alignment:** PN reference only "15340381 / rev"; review uses gene-specific PMID:18203720 (HIGH/VERIFIED, lectin+SCF), PMID:19716789 (HIGH/VERIFIED, CHK1), PMID:34445249/ComplexPortal CPX-7905, plus Falcon DR (Fujihira/Suzuki NGLY1 review, NFE2L1). PN family review is a subset; good overlap on the SCF-receptor framing.
- **Verdict:** Consistent; core MF correctly GO:0030246 (lectin, in GOA) over the generic PN adaptor term; CHK1 checkpoint role non-core; GO:0006281 over-annotation flagged. No over-reach.

## Full Consistency Review

- **UniProt:** Q9NRD1 (FBXO6/FBG2/Fbs2) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA` ; **PN-node mapping:** group `Cul1 substrate receptor`=`mapped`/ok_for_propagation→GO:1990756; F-box/FBA subtype+type=`no_mapping`; class=`context_only`/too_broad→GO:0061630.
- **Consistency:** Consistent. Falcon DR (NGLY1/NFE2L1 axis, proteasome bounce-back), review YAML, and the PN FBA F-box receptor placement converge. SPECIAL CASE confirmed: FBA lectin (GO:0030246, verified real) binding high-mannose/complex/sulfated glycans (chitobiose core essential, PMID:18203720), feeding glycoprotein-ERAD; plus a documented CHK1-degradation/checkpoint role (PMID:19716789, IDA).
- **PN story / NEW pressure:** PN projects the generic GO:1990756 adaptor term (new_to_goa). Review's **core MF is GO:0030246 carbohydrate binding (ACCEPT, already in GOA; experimentally grounded by PMID:18203720 glycan-array)** — more informative than the generic adaptor. Catalytic GO:0061630 correctly held at contributes_to/non-core. The CHK1/DNA-damage-checkpoint role (GO:0000077) is a real second process kept non-core; review aptly MARK_AS_OVER_ANNOTATED for the GO:0006281 DNA repair term (FBXO6 terminates CHK1, is not a repair factor). Conclude: gene's distinctive lectin MF already captured; generic PN adaptor term not the best core.
- **Mapping strategy:** Gene refines, does not change, the node — same as FBXO2. GO:1990756 group projection is the safe family MF; GO:0030246 is the more specific, already-in-GOA MF for the FBA-lectin subfamily. PN class GO:0061630 correctly too_broad.
- **Evidence alignment:** PN reference only "15340381 / rev"; review uses gene-specific PMID:18203720 (HIGH/VERIFIED, lectin+SCF), PMID:19716789 (HIGH/VERIFIED, CHK1), PMID:34445249/ComplexPortal CPX-7905, plus Falcon DR (Fujihira/Suzuki NGLY1 review, NFE2L1). PN family review is a subset; good overlap on the SCF-receptor framing.
- **Verdict:** Consistent; core MF correctly GO:0030246 (lectin, in GOA) over the generic PN adaptor term; CHK1 checkpoint role non-core; GO:0006281 over-annotation flagged. No over-reach.
- **Recommended edits:** none to FBXO6-ai-review.yaml. [MAP] As for FBXO2, FBA-lectin subfamily nodes could carry GO:0030246 as the distinguishing MF in addition to GO:1990756.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO6/FBXO6-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | FBA
- UniProt: Q9NRD1
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR007397
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA
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
