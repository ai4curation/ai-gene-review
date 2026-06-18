# MKRN2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H000
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MKRN2/MKRN2-ai-review.yaml](MKRN2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/MKRN2/MKRN2-ai-review.html](MKRN2-ai-review.html)
- Gene notes: present - [genes/human/MKRN2/MKRN2-notes.md](MKRN2-notes.md)
- GOA TSV: present - [genes/human/MKRN2/MKRN2-goa.tsv](MKRN2-goa.tsv)
- UniProt record: present - [genes/human/MKRN2/MKRN2-uniprot.txt](MKRN2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MKRN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MKRN2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MKRN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MKRN2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MKRN2 (makorin RING finger protein 2; RNF62) is a RING-type E3 ubiquitin ligase of the makorin family and a paralog of MKRN1. Like other makorins it pairs a C3HC4 RING domain, which confers ubiquitin-protein ligase activity, with CCCH/C3H zinc-finger motifs capable of RNA binding. MKRN2 catalyzes ubiquitin transfer onto substrate proteins; it has been reported (largely by similarity to the rodent ortholog) to promote polyubiquitination and proteasome-dependent degradation of the NF-kB subunit RELA/p65, thereby suppressing RELA-mediated transactivation and dampening inflammatory responses, and to contribute to spermiation and male fertility. It is found in both the cytoplasm and nucleus. MKRN2 is considerably less characterized than MKRN1, and many of its biological-process annotations derive from cross-species inference rather than direct human experimentation.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 14; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Partial mismatch. The UPS/E3-ligase placement (GO:0061630, GO:0016567) matches the review perfectly — both already in GOA (IBA/IEA/ISS). BUT the PN puts MKRN2 in the **same RQC node as MKRN1**, projecting GO:0006515 (protein QC). The review finds **no direct or inferred RQC evidence for human MKRN2** — RQC is raised only as a *suggested question* ("does MKRN2 contribute to co-translational QC… how is it partitioned from MKRN1?"). MKRN2's characterized biology is RELA/p65 / NF-kB (mostly ISS/by-similarity from rodent), not poly(A) RQC. So the PN RQC placement for MKRN2 is **paralogy-driven over-reach**, inherited from MKRN1.
- **PN story / NEW pressure:** No defensible NEW pressure. There is no human-experimental basis to annotate MKRN2 to GO:0006515 or GO:1990116; doing so would be PARALOG_OVERANNOTATION (MKRN1 evidence applied to MKRN2). The review correctly withholds an RQC annotation. The genuine MKRN2 functions (E3 ligase, NF-kB regulation) are already captured/over-annotation-flagged.
- **Evidence alignment:** PN row 2 cites "19489725 / rev" (makorin review, same as MKRN1). Review anchors only on RNA-binding screen PMID:22681889 (HDA, VERIFIED) plus uniprot/ISS; notably **no dedicated experimental paper establishes human MKRN2's E3 activity or any RQC role** — consistent with the review's caution. Divergence: PN asserts RQC; review evidence does not.
- **Verdict:** Over-reach on the RQC branch (paralog inheritance from MKRN1). E3-ligase placement consistent. **Recommended edits:** [MAP] do not project GO:0006515 / GO:1990116 onto MKRN2 from the RQC node — no human-experimental RQC evidence; flag MKRN2's RQC-node membership as paralogy-driven (PARALOG_OVERANNOTATION) pending the suggested iCLIP/ribosome-profiling experiment.

## Full Consistency Review

- **UniProt:** Q9H000 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** two rows — `Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination` (TR) and `UPS|E3 ubiquitin and UBL ligases|RING|Makorin|C3H1-type ZnF` (UPS). **PN-node mapping:** identical to MKRN1 — RQC type→GO:0016567 (mapped); RQC group→GO:0006515 (mapped); RING group→GO:0061630 (mapped); subtype + UPS branch = no_mapping.
- **Consistency:** Partial mismatch. The UPS/E3-ligase placement (GO:0061630, GO:0016567) matches the review perfectly — both already in GOA (IBA/IEA/ISS). BUT the PN puts MKRN2 in the **same RQC node as MKRN1**, projecting GO:0006515 (protein QC). The review finds **no direct or inferred RQC evidence for human MKRN2** — RQC is raised only as a *suggested question* ("does MKRN2 contribute to co-translational QC… how is it partitioned from MKRN1?"). MKRN2's characterized biology is RELA/p65 / NF-kB (mostly ISS/by-similarity from rodent), not poly(A) RQC. So the PN RQC placement for MKRN2 is **paralogy-driven over-reach**, inherited from MKRN1.
- **PN story / NEW pressure:** No defensible NEW pressure. There is no human-experimental basis to annotate MKRN2 to GO:0006515 or GO:1990116; doing so would be PARALOG_OVERANNOTATION (MKRN1 evidence applied to MKRN2). The review correctly withholds an RQC annotation. The genuine MKRN2 functions (E3 ligase, NF-kB regulation) are already captured/over-annotation-flagged.
- **Mapping strategy:** This gene should NOT inherit the RQC-group GO:0006515 projection. The node mapping is fine as a *bucket* for MKRN1, but MKRN2's membership in that node is the problem — its projected GO:0006515 is unsupported for this paralog. Flag: MKRN2 RQC placement is broader/unsupported relative to the review (which has zero RQC terms).
- **Evidence alignment:** PN row 2 cites "19489725 / rev" (makorin review, same as MKRN1). Review anchors only on RNA-binding screen PMID:22681889 (HDA, VERIFIED) plus uniprot/ISS; notably **no dedicated experimental paper establishes human MKRN2's E3 activity or any RQC role** — consistent with the review's caution. Divergence: PN asserts RQC; review evidence does not.
- **Verdict:** Over-reach on the RQC branch (paralog inheritance from MKRN1). E3-ligase placement consistent. **Recommended edits:** [MAP] do not project GO:0006515 / GO:1990116 onto MKRN2 from the RQC node — no human-experimental RQC evidence; flag MKRN2's RQC-node membership as paralogy-driven (PARALOG_OVERANNOTATION) pending the suggested iCLIP/ribosome-profiling experiment.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/MKRN2/MKRN2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ubiquitination
- UniProt: Q9H000
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016567 protein ubiquitination]
        rationale: This PN RQC type denotes ubiquitination events on stalled translation complexes. Protein ubiquitination is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | Makorin | C3H1-type ZnF
- UniProt: Q9H000
- In branches: TR, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR000571
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|Makorin|C3H1-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|Makorin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0016567 protein ubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
