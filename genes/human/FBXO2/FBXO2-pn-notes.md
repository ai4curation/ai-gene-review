# FBXO2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UK22
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO2/FBXO2-ai-review.yaml](FBXO2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO2/FBXO2-ai-review.html
- Gene notes: missing - genes/human/FBXO2/FBXO2-notes.md
- GOA TSV: present - [genes/human/FBXO2/FBXO2-goa.tsv](FBXO2-goa.tsv)
- UniProt record: present - [genes/human/FBXO2/FBXO2-uniprot.txt](FBXO2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO2/FBXO2-deep-research-falcon.md](FBXO2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO2 (FBG1/FBX2/NFB42) is a 296-residue cytoplasmic F-box protein that serves as the substrate-recognition subunit of a Skp1-Cul1-F-box (SCF) E3 ubiquitin-protein ligase complex. It contains an N-terminal F-box domain (residues 44-91) that binds SKP1, bridging the receptor to the CUL1-RBX1 catalytic core, and a C-terminal F-box-associated (FBA) sugar-binding domain (residues 113-296) that folds as a galactose-binding-domain-like lectin and binds N-linked high-mannose oligosaccharides. The FBA domain recognizes the innermost N-glycan core (Man3GlcNAc2 / the chitobiose-proximal GlcNAc2 moiety) through a small hydrophobic pocket, a "sugar degron" that becomes exposed when a glycoprotein is misfolded, denatured, or aberrantly retrotranslocated to the cytosol. Through this lectin activity FBXO2 recognizes N-glycans on misfolded/denatured glycoproteins that have been retrotranslocated from the endoplasmic reticulum into the cytosol, recruiting them to the SCF complex for polyubiquitination and proteasomal degradation as part of the ER-associated degradation (ERAD) pathway, thereby preventing the accumulation of cytosolic aggregates of unfolded glycoproteins. Reported glycoprotein clients in the Fbs1/Fbs2 quality-control orbit include pre-integrin beta-1, the T-cell receptor alpha chain, the asialoglycoprotein receptor subunit, and the disease variant CFTR-deltaF508; in neurons FBXO2 additionally turns over APP and BACE1 to limit amyloidogenic processing. FBXO2 is most highly expressed in the nervous system, where it has additional roles in synaptic protein turnover and in clearance of damaged glycan-bearing membranes (lysophagy) and intracellular bacteria (xenophagy), recognizing GlcNAc/high- mannose glycans on these targets. The protein is a peripheral cytoplasmic-side membrane protein and is itself a glycoprotein-specific lectin, not a glycosidase.
- Existing/core annotation action counts: ACCEPT: 28; KEEP_AS_NON_CORE: 15

## PN Consistency Summary

- **Consistency:** Consistent on substance; one nuance. Falcon DR, review YAML, and the PN FBA F-box receptor placement converge on FBXO2 as a lectin-type SCF substrate receptor for glycoprotein-ERAD. SPECIAL CASE confirmed: FBA = real carbohydrate-binding MF (GO:0030246, verified real), recognizing the innermost Man3GlcNAc2 N-glycan core on misfolded glycoproteins.
- **PN story / NEW pressure:** PN projects the generic GO:1990756 adaptor term (new_to_goa). The review's chosen **core MF is the more informative, substrate-class-specific GO:0030246 carbohydrate binding (ACCEPT, already in GOA via IEA/keyword Lectin)** — a genuine lectin activity beyond bare adaptor binding. Review also correctly demotes catalytic TAS GO:0004842/GO:0061630 to non-core/contributes_to. Conclude: PN adaptor term is captured at family level but the gene's distinctive MF (carbohydrate binding) is already in GOA and is the better core — no new term needed; FBXO2 lectin function over-rides the generic adaptor projection.
- **Evidence alignment:** PN reference only "15340381 / rev"; review draws on PMID:10531035 (family), PMID:18203720-equivalent FBA-lectin work (cited heavily for FBXO6), PMID:34515398 (xenophagy/glycan, HIGH/VERIFIED), PMID:34445249, plus Falcon DR (Yoshida/Suzuki reviews, lysophagy). Strong gene-specific evidence; PN family review is a subset.
- **Verdict:** Consistent; core MF correctly GO:0030246 (lectin, in GOA) rather than the generic PN adaptor term. No over-reach; secondary xenophagy/lysophagy/synaptic roles kept non-core.

## Full Consistency Review

- **UniProt:** Q9UK22 (FBXO2/FBG1/Fbs1) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|FBA` ; **PN-node mapping:** group `Cul1 substrate receptor`=`mapped`/ok_for_propagation→GO:1990756; F-box/FBA subtype+type=`no_mapping`; class=`context_only`/too_broad→GO:0061630.
- **Consistency:** Consistent on substance; one nuance. Falcon DR, review YAML, and the PN FBA F-box receptor placement converge on FBXO2 as a lectin-type SCF substrate receptor for glycoprotein-ERAD. SPECIAL CASE confirmed: FBA = real carbohydrate-binding MF (GO:0030246, verified real), recognizing the innermost Man3GlcNAc2 N-glycan core on misfolded glycoproteins.
- **PN story / NEW pressure:** PN projects the generic GO:1990756 adaptor term (new_to_goa). The review's chosen **core MF is the more informative, substrate-class-specific GO:0030246 carbohydrate binding (ACCEPT, already in GOA via IEA/keyword Lectin)** — a genuine lectin activity beyond bare adaptor binding. Review also correctly demotes catalytic TAS GO:0004842/GO:0061630 to non-core/contributes_to. Conclude: PN adaptor term is captured at family level but the gene's distinctive MF (carbohydrate binding) is already in GOA and is the better core — no new term needed; FBXO2 lectin function over-rides the generic adaptor projection.
- **Mapping strategy:** Gene refines, does not change, the node. The GO:1990756 group projection is the lowest-common-denominator F-box MF; for the FBA lectin subfamily the more specific GO:0030246 is preferable and already present, so the projection is not wrong but is broader than the gene's best MF. Consider noting FBA-lectin subfamilies carry carbohydrate binding as the distinguishing MF.
- **Evidence alignment:** PN reference only "15340381 / rev"; review draws on PMID:10531035 (family), PMID:18203720-equivalent FBA-lectin work (cited heavily for FBXO6), PMID:34515398 (xenophagy/glycan, HIGH/VERIFIED), PMID:34445249, plus Falcon DR (Yoshida/Suzuki reviews, lysophagy). Strong gene-specific evidence; PN family review is a subset.
- **Verdict:** Consistent; core MF correctly GO:0030246 (lectin, in GOA) rather than the generic PN adaptor term. No over-reach; secondary xenophagy/lysophagy/synaptic roles kept non-core.
- **Recommended edits:** none to FBXO2-ai-review.yaml. [MAP] Optionally annotate FBA-lectin F-box subfamily nodes so carbohydrate binding (GO:0030246) is recognized as their distinguishing MF alongside the generic GO:1990756.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO2/FBXO2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | FBA
- UniProt: Q9UK22
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
