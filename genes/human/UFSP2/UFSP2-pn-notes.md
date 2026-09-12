# UFSP2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NUQ7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UFSP2/UFSP2-ai-review.yaml](UFSP2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UFSP2/UFSP2-ai-review.html](UFSP2-ai-review.html)
- Gene notes: present - [genes/human/UFSP2/UFSP2-notes.md](UFSP2-notes.md)
- GOA TSV: present - [genes/human/UFSP2/UFSP2-goa.tsv](UFSP2-goa.tsv)
- UniProt record: present - [genes/human/UFSP2/UFSP2-uniprot.txt](UFSP2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UFSP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UFSP2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFSP2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFSP2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UFSP2 (UFM1-specific protease 2) is the principal human UFM1-specific cysteine (thiol-dependent) isopeptidase of the peptidase C78 family (catalytic Cys302). It acts in the UFM1 (ubiquitin-fold modifier 1) conjugation system, where it both processes pro-UFM1 to expose the activating C-terminal glycine and, predominantly, removes UFM1 from conjugated target proteins (deUFMylation). Documented substrates include the ribosomal protein RPL26/uL24, CYB5R3, DDRGK1, MRE11, TRIP4 and CD274/PD-L1. At the cytoplasmic surface of the endoplasmic reticulum, UFSP2 deUFMylates RPL26 on 60S ribosomal subunits, a step required to release the UFM1 E3 ligase complex and recycle 60S subunits after ribosome-associated quality control of stalled ER-translocating ribosomes. Through deUFMylation of CYB5R3 it modulates ER-phagy, and through TRIP4 it influences nuclear-receptor (estrogen receptor) transactivation. Loss-of-function and missense UFSP2 variants cause autosomal-dominant skeletal dysplasias (Beukes hip dysplasia, spondyloepimetaphyseal dysplasia) and a recessive neurodevelopmental/epileptic encephalopathy.
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep-research/notes, review YAML, PN annotation and PN-node mapping agree: UFSP2 is the principal human UFM1-specific cysteine protease (Cys302) that deUFMylates substrates (RPL26/uL24, CYB5R3, TRIP4, etc.) and processes pro-UFM1; ER-membrane-tethered, acting on 60S after RQC splitting. GOA cross-check confirms goa_status: GO:0071567 already-in-GOA (12 records), GO:0071569 new-to-GOA (0), GO:0006515 new-to-GOA (0). No contradictions.
- **PN story / NEW pressure:** PN's deUFMylase/ufmylation story is captured (GO:0071567 multiple IDA/IMP/IBA). The RQC-specific biology is ALSO captured by review-only terms NOT generated from the PN node: GO:0072344 rescue of stalled cytosolic ribosome (IDA, PMID:38383785) and GO:0032790 ribosome disassembly (IDA) — these are more precise than the PN group's GO:0006515 and are already in the review. So GO:0006515 (new-to-GOA) is defensible-but-redundant for UFSP2; the better RQC terms already exist. No new term required.
- **Evidence alignment:** PN row 2 cites PMID:29476094 (UFSP review) — absent from the review YAML, which spans many primaries (PMID:38383785, 35926457, 36543799, 25219498, 31595041, 27926783, 33473208, 32160526, 36893266, 37795761). Same biology; PN reference is a secondary review not used in the YAML.
- **Verdict:** Consistent and complete; PN-projected GO:0006515 is correct but broader than the review's already-present GO:0072344/GO:0032790.

## Full Consistency Review

- **UniProt:** Q9NUQ7 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** two rows — `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation` and `Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase` ; **PN-node mapping:** type/group both `mapped, ok_for_propagation` → GO:0071569 protein ufmylation, GO:0071567 deUFMylase activity, group-level GO:0006515 PQC (from RQC group); UPS class/branch `no_mapping`.
- **Consistency:** Strong. Deep-research/notes, review YAML, PN annotation and PN-node mapping agree: UFSP2 is the principal human UFM1-specific cysteine protease (Cys302) that deUFMylates substrates (RPL26/uL24, CYB5R3, TRIP4, etc.) and processes pro-UFM1; ER-membrane-tethered, acting on 60S after RQC splitting. GOA cross-check confirms goa_status: GO:0071567 already-in-GOA (12 records), GO:0071569 new-to-GOA (0), GO:0006515 new-to-GOA (0). No contradictions.
- **PN story / NEW pressure:** PN's deUFMylase/ufmylation story is captured (GO:0071567 multiple IDA/IMP/IBA). The RQC-specific biology is ALSO captured by review-only terms NOT generated from the PN node: GO:0072344 rescue of stalled cytosolic ribosome (IDA, PMID:38383785) and GO:0032790 ribosome disassembly (IDA) — these are more precise than the PN group's GO:0006515 and are already in the review. So GO:0006515 (new-to-GOA) is defensible-but-redundant for UFSP2; the better RQC terms already exist. No new term required.
- **Mapping strategy:** Unlike UFSP1, the GROUP→GO:0006515/RQC projection IS biologically defensible for UFSP2 (RPL26 deUFMylation enabling 60S recycling after RQC). However the review already holds the narrower, IDA-backed GO:0072344 / GO:0032790; GO:0006515 is broader than these. UPS-side deUFMylase node anchoring is correct.
- **Evidence alignment:** PN row 2 cites PMID:29476094 (UFSP review) — absent from the review YAML, which spans many primaries (PMID:38383785, 35926457, 36543799, 25219498, 31595041, 27926783, 33473208, 32160526, 36893266, 37795761). Same biology; PN reference is a secondary review not used in the YAML.
- **Verdict:** Consistent and complete; PN-projected GO:0006515 is correct but broader than the review's already-present GO:0072344/GO:0032790.

**Recommended edits:** [MAP] the RQC-group GO:0006515 projection is acceptable for UFSP2 but redundant/broader than the review's existing GO:0072344 (rescue of stalled cytosolic ribosome) and GO:0032790 (ribosome disassembly); prefer those narrower IDA-supported terms when representing UFSP2's RQC role.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFSP2/UFSP2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q9NUQ7
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
- UniProt: Q9NUQ7
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
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0071567 deUFMylase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP
- GO:0071567 deUFMylase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
