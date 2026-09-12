# UFSP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6NVU6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UFSP1/UFSP1-ai-review.yaml](UFSP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UFSP1/UFSP1-ai-review.html](UFSP1-ai-review.html)
- Gene notes: present - [genes/human/UFSP1/UFSP1-notes.md](UFSP1-notes.md)
- GOA TSV: present - [genes/human/UFSP1/UFSP1-goa.tsv](UFSP1-goa.tsv)
- UniProt record: present - [genes/human/UFSP1/UFSP1-uniprot.txt](UFSP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UFSP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UFSP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFSP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFSP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UFSP1 (UFM1-specific protease 1) is a cytosolic thiol-dependent (cysteine-type) isopeptidase of the peptidase C78 family and a paralog of UFSP2. The catalytically active human protein is produced from an upstream near-cognate (217CUG) initiation codon, generating an N-terminally extended form that contains the catalytic Cys protease domain; the previously annotated 445AUG-initiated short form lacks the active site and is inactive. UFSP1 carries out two reactions in the UFM1 (ubiquitin-fold modifier 1) conjugation system - it cleaves pro-UFM1 to expose the C-terminal glycine required for activation (UFM1 maturation), and it removes UFM1 from conjugated substrates (deUFMylation). It acts early in the pathway, maturing UFM1 and removing an autoinhibitory UFM1 modification on the E2 enzyme UFC1, and in vitro disassembles polyUFM1 chains. UFSP1 and UFSP2 act redundantly in pro-UFM1 maturation, but differ in substrate specificity and localization (UFSP2, not UFSP1, deUFMylates the ribosomal subunit RPL26).
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep-research notes, review YAML, PN annotation and PN-node mapping all converge: UFSP1 is an active UFM1-specific cysteine protease (deUFMylase) that matures pro-UFM1 and removes an autoinhibitory UFM1 mark on UFC1; it is cytosolic and (unlike UFSP2) does NOT deUFMylate RPL26. GOA cross-check confirms goa_status: GO:0071567 already-in-GOA (4 records), GO:0071569 already-in-GOA (2), GO:0006515 new-to-GOA (0). No contradictions.
- **PN story / NEW pressure:** PN's deUFMylase + ufmylation story is fully captured by existing annotations (GO:0071567 IDA/IBA, GO:0071569 IDA, GO:0008234, GO:0051604). The one element NOT in GOA is the group-level GO:0006515 (PQC). For UFSP1 this over-reaches: UFSP1 acts on UFM1/UFC1 maturation in the cytosol, not on ribosome-associated QC of misfolded/stalled nascent chains (that arm is UFSP2/RPL26). No defensible NEW term needed; deUFMylase activity already captured.
- **Evidence alignment:** PN row 2 cites PMID:29476094 (Millrine UFSP review) — not in the review YAML, which instead anchors on the two primary 2022 papers (PMID:35525273, PMID:35926457) plus the HuRI interactome (PMID:32296183). Same biology, complementary references; no conflict.
- **Verdict:** Consistent and complete; the only flag is the RQC-group GO:0006515 projection over-reaching for cytosolic UFSP1.

## Full Consistency Review

- **UniProt:** Q6NVU6 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** two rows — `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation` and `Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase` ; **PN-node mapping:** type/group both `mapped, ok_for_propagation` → GO:0071569 protein ufmylation, GO:0071567 deUFMylase activity, plus group-level GO:0006515 PQC for misfolded/incompletely synthesized proteins (from RQC group); UPS class/branch `no_mapping`.
- **Consistency:** Strong. Deep-research notes, review YAML, PN annotation and PN-node mapping all converge: UFSP1 is an active UFM1-specific cysteine protease (deUFMylase) that matures pro-UFM1 and removes an autoinhibitory UFM1 mark on UFC1; it is cytosolic and (unlike UFSP2) does NOT deUFMylate RPL26. GOA cross-check confirms goa_status: GO:0071567 already-in-GOA (4 records), GO:0071569 already-in-GOA (2), GO:0006515 new-to-GOA (0). No contradictions.
- **PN story / NEW pressure:** PN's deUFMylase + ufmylation story is fully captured by existing annotations (GO:0071567 IDA/IBA, GO:0071569 IDA, GO:0008234, GO:0051604). The one element NOT in GOA is the group-level GO:0006515 (PQC). For UFSP1 this over-reaches: UFSP1 acts on UFM1/UFC1 maturation in the cytosol, not on ribosome-associated QC of misfolded/stalled nascent chains (that arm is UFSP2/RPL26). No defensible NEW term needed; deUFMylase activity already captured.
- **Mapping strategy:** UFSP1 does not change the UPS-side node (correctly anchored on GO:0071567). On the Translation/RQC side, the GROUP→GO:0006515 projection is too broad for UFSP1 specifically (cytosolic UFM1-maturation enzyme, not a misfolded/incomplete-protein degradation factor). Status/scope on the deUFMylase nodes are right.
- **Evidence alignment:** PN row 2 cites PMID:29476094 (Millrine UFSP review) — not in the review YAML, which instead anchors on the two primary 2022 papers (PMID:35525273, PMID:35926457) plus the HuRI interactome (PMID:32296183). Same biology, complementary references; no conflict.
- **Verdict:** Consistent and complete; the only flag is the RQC-group GO:0006515 projection over-reaching for cytosolic UFSP1.

**Recommended edits:** [MAP] do not project group-level GO:0006515 (PQC for misfolded/incompletely synthesized proteins) onto UFSP1 — UFSP1 is a cytosolic UFM1-maturation/deUFMylase enzyme, not a ribosome-associated misfolded-protein QC factor (contrast UFSP2/RPL26).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFSP1/UFSP1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q6NVU6
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071569 protein ufmylation]
        rationale: This PN RQC type denotes UFM1 conjugation in ribosome quality control. Protein ufmylation is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | DUBs and UBL demodifiers | UFSP | deUFMylase
- UniProt: Q6NVU6
- In branches: TR, UPS
- Signature domains: IPR012462
- Auxiliary domains: (none)
- PN references (titles):
    - 29476094
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071567 deUFMylase activity]
        rationale: This PN type is the explicit deUFMylase bucket under UFSP proteins. The matching GO molecular-function term is deUFMylase activity.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071567 deUFMylase activity]
        rationale: This PN group captures UFSP-family deUFMylases. The matching GO molecular-function term is deUFMylase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0071567 deUFMylase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP
- GO:0071567 deUFMylase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
