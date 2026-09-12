# MKRN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UHC7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MKRN1/MKRN1-ai-review.yaml](MKRN1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/MKRN1/MKRN1-ai-review.html](MKRN1-ai-review.html)
- Gene notes: present - [genes/human/MKRN1/MKRN1-notes.md](MKRN1-notes.md)
- GOA TSV: present - [genes/human/MKRN1/MKRN1-goa.tsv](MKRN1-goa.tsv)
- UniProt record: present - [genes/human/MKRN1/MKRN1-uniprot.txt](MKRN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MKRN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MKRN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MKRN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MKRN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MKRN1 (makorin RING finger protein 1; RNF61) is a cytoplasmic RNA-binding RING-type E3 ubiquitin ligase of the makorin family. It combines a C3HC4 RING domain, which confers ubiquitin-protein ligase activity, with multiple CCCH/C3H zinc-finger motifs that mediate RNA binding. MKRN1 ubiquitinates several substrate proteins - including p53/TP53 (which it suppresses under normal conditions to keep cells alive), the CDK inhibitor CDKN1A/p21 (which it degrades under stress to promote apoptosis), the telomerase catalytic subunit TERT (acting as a negative regulator of telomerase), and FILIP1 - thereby influencing cell-cycle arrest, apoptosis and telomere maintenance. In addition, MKRN1 acts in ribosome-associated quality control of poly(A) translation: by binding the poly(A)-binding protein PABPC1 and associating with polysomes just upstream of poly(A) tails, it promotes ribosome stalling on prematurely polyadenylated (A-rich) messages and ubiquitinates the 40S ribosomal protein RPS10 and PABPC1, positioning it upstream of ZNF598/LTN1 in clearing aberrant nascent chains and preventing production of erroneous proteins.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 3; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Review, notes, deep-research, PN annotation, and PN-node mapping all converge: MKRN1 is a makorin RING E3 ligase (GO:0061630, GO:0016567 — both already in GOA, IDA/IBA) that also acts in poly(A) ribosome-associated QC (PMID:31640799). No contradictions.
- **PN story / NEW pressure:** The RQC story IS the value-add and the review already acted on it — it adds GO:1990116 "ribosome-associated ubiquitin-dependent protein catabolic process" as a **NEW** annotation (IMP, PMID:31640799), verified real and non-obsolete via OLS. This is more specific and more apt than the PN-projected GO:0006515. ADD already done in YAML.
- **Evidence alignment:** PN row 2 cites "19489725 / rev" (a makorin review). The review instead anchors on the primary functional papers PMID:19536131 (p53/p21 E3 activity) and PMID:31640799 (poly(A) RQC) — stronger, primary evidence; the PN review-citation is a reasonable family-level pointer not needed in the gene review.
- **Verdict:** Consistent; NEW GO:1990116 already correctly added (verified). No edits required; keep gene-level RQC annotation at GO:1990116 rather than the broader PN-projected GO:0006515.

## Full Consistency Review

- **UniProt:** Q9UHC7 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** two rows — `Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination` (TR) and `UPS|E3 ubiquitin and UBL ligases|RING|Makorin|C3H1-type ZnF` (UPS). **PN-node mapping:** RQC type→GO:0016567 protein ubiquitination (mapped); RQC group→GO:0006515 protein QC for misfolded/incompletely synthesized proteins (mapped); RING group→GO:0061630 ubiquitin protein ligase activity (mapped); Makorin/ZnF subtype + UPS branch = no_mapping.
- **Consistency:** Strong agreement. Review, notes, deep-research, PN annotation, and PN-node mapping all converge: MKRN1 is a makorin RING E3 ligase (GO:0061630, GO:0016567 — both already in GOA, IDA/IBA) that also acts in poly(A) ribosome-associated QC (PMID:31640799). No contradictions.
- **PN story / NEW pressure:** The RQC story IS the value-add and the review already acted on it — it adds GO:1990116 "ribosome-associated ubiquitin-dependent protein catabolic process" as a **NEW** annotation (IMP, PMID:31640799), verified real and non-obsolete via OLS. This is more specific and more apt than the PN-projected GO:0006515. ADD already done in YAML.
- **Mapping strategy:** No node-mapping change needed. The PN RQC-group projection GO:0006515 is **broader** than the review's GO:1990116 (a descendant capturing ribosome-associated ubiquitin-dependent catabolism). Per the TOMM20/HSPA8/RAB7A precedent the broader class-projection is acceptable as a group-level node mapping (it spans many RQC members), but for MKRN1 specifically the gene-level annotation should remain the more specific GO:1990116, not GO:0006515. GO:0016567 / GO:0061630 projections are exact and already in GOA.
- **Evidence alignment:** PN row 2 cites "19489725 / rev" (a makorin review). The review instead anchors on the primary functional papers PMID:19536131 (p53/p21 E3 activity) and PMID:31640799 (poly(A) RQC) — stronger, primary evidence; the PN review-citation is a reasonable family-level pointer not needed in the gene review.
- **Verdict:** Consistent; NEW GO:1990116 already correctly added (verified). No edits required; keep gene-level RQC annotation at GO:1990116 rather than the broader PN-projected GO:0006515.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/MKRN1/MKRN1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ubiquitination
- UniProt: Q9UHC7
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
- UniProt: Q9UHC7
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
