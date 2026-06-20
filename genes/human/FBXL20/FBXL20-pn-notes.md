# FBXL20 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96IG2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL20/FBXL20-ai-review.yaml](FBXL20-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL20/FBXL20-ai-review.html
- Gene notes: missing - genes/human/FBXL20/FBXL20-notes.md
- GOA TSV: present - [genes/human/FBXL20/FBXL20-goa.tsv](FBXL20-goa.tsv)
- UniProt record: present - [genes/human/FBXL20/FBXL20-uniprot.txt](FBXL20-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL20.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL20.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL20.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL20.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL20/FBXL20-deep-research-falcon.md](FBXL20-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL20 (F-box/LRR-repeat protein 20; FBL2; the mouse ortholog is named SCRAPPER) is a substrate-recognition subunit of an SCF (SKP1-CUL1-RBX1) E3 ubiquitin ligase complex. Its F-box motif binds SKP1, linking it to the CUL1-RBX1 catalytic core, while its leucine-rich repeat domain provides substrate selectivity, directing substrate-specific polyubiquitination and proteasomal degradation. FBXL20 carries a C-terminal CAAX motif that is isoprenylated, targeting it to membranes, and its localization governs which substrates it engages. A well-characterized human substrate is VPS34/PIK3C3, the catalytic subunit of class III PI3K: FBXL20 binds VPS34 through its C-terminal LRR region (engaging the VPS34 C2 domain) and, downstream of DNA damage, promotes CDK-dependent (VPS34 Thr159) phosphodegron-gated ubiquitination and proteasomal degradation of VPS34. FBXL20 is itself a p53-inducible gene (and a miR-3151 target), so the p53 to FBXL20 to VPS34 axis lowers PtdIns3P output, dampening autophagy and slowing endosomal receptor (e.g. EGFR) degradation under genotoxic stress. FBXL20 also promotes ubiquitination and degradation of PR55alpha/PPP2R2A, a regulatory B subunit of the PP2A serine/threonine phosphatase. In the nervous system the SCRAPPER/FBXL20 ortholog is a membrane-associated presynaptic regulator that ubiquitinates the active-zone protein RIM1/RIMS1, controlling synaptic vesicle release and neurotransmission; accordingly the protein has documented roles at the presynapse and at glutamatergic synapses (largely inferred from the mouse ortholog). FBXL20 acts in the cytoplasm/cytosol and at membranes.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 21; NEW: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Falcon DR (VPS34/PIK3C3 phosphodegron axis; CAAX-isoprenylation/RIM1; PR55alpha), the review YAML, the PN F-box LRR substrate-receptor placement, and the GO:1990756 group mapping all converge. No contradictions.
- **PN story / NEW pressure:** PN projects GO:1990756 (verified real, OLS: "binding...brings together a ubiquitin-like ligase and its substrate. Usually mediated by F-box...proteins") as new_to_goa. Review **independently ADDS GO:1990756 as `action: NEW`** (IDA, PMID:34731788), replacing five bare protein binding (SKP1/PR55alpha) IPI annotations. Matches PN projection exactly. Conclude: ADD — warranted and concordant.
- **Evidence alignment:** PN reference is only "15340381 / rev" (Jin et al. F-box family review), not directly in the review's PMID set; review anchors on the human PR55alpha study PMID:34731788 (HIGH/VERIFIED) plus FBXL family review PMID:33234069 and Falcon DR for the VPS34 axis. Divergence is benign — PN uses a generic family review; review uses gene-specific primary literature.
- **Verdict:** Consistent; GO:1990756 NEW warranted and matches PN (new_to_goa). No over-reach.

## Full Consistency Review

- **UniProt:** Q96IG2 (FBXL20/FBL2; mouse ortholog SCRAPPER) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group `Cul1 substrate receptor`=`mapped`/ok_for_propagation→GO:1990756; F-box/LRR subtype+type=`no_mapping`; class=`context_only`/too_broad→GO:0061630.
- **Consistency:** Fully consistent. Falcon DR (VPS34/PIK3C3 phosphodegron axis; CAAX-isoprenylation/RIM1; PR55alpha), the review YAML, the PN F-box LRR substrate-receptor placement, and the GO:1990756 group mapping all converge. No contradictions.
- **PN story / NEW pressure:** PN projects GO:1990756 (verified real, OLS: "binding...brings together a ubiquitin-like ligase and its substrate. Usually mediated by F-box...proteins") as new_to_goa. Review **independently ADDS GO:1990756 as `action: NEW`** (IDA, PMID:34731788), replacing five bare protein binding (SKP1/PR55alpha) IPI annotations. Matches PN projection exactly. Conclude: ADD — warranted and concordant.
- **Mapping strategy:** Gene supports, does not change, the node. KEY PATTERN holds: F-box = SCF substrate receptor, catalysis in RBX1; the correct shared MF is the GO:1990756 adaptor term at the receptor group, with the catalytic GO:0061630 correctly held at class level as too_broad. No PN-projected term is broader than the review (unlike TOMM20/HSPA8 precedent). Scopes correct.
- **Evidence alignment:** PN reference is only "15340381 / rev" (Jin et al. F-box family review), not directly in the review's PMID set; review anchors on the human PR55alpha study PMID:34731788 (HIGH/VERIFIED) plus FBXL family review PMID:33234069 and Falcon DR for the VPS34 axis. Divergence is benign — PN uses a generic family review; review uses gene-specific primary literature.
- **Verdict:** Consistent; GO:1990756 NEW warranted and matches PN (new_to_goa). No over-reach.
- **Recommended edits:** none to FBXL20-ai-review.yaml; PN mappings sound as-is.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL20/FBXL20-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q96IG2
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
