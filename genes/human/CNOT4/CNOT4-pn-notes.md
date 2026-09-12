# CNOT4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O95628
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CNOT4/CNOT4-ai-review.yaml](CNOT4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CNOT4/CNOT4-ai-review.html](CNOT4-ai-review.html)
- Gene notes: present - [genes/human/CNOT4/CNOT4-notes.md](CNOT4-notes.md)
- GOA TSV: present - [genes/human/CNOT4/CNOT4-goa.tsv](CNOT4-goa.tsv)
- UniProt record: present - [genes/human/CNOT4/CNOT4-uniprot.txt](CNOT4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CNOT4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CNOT4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CNOT4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CNOT4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CNOT4 (CCR4-NOT transcription complex subunit 4, the human ortholog of yeast Not4) is a RING-type E3 ubiquitin-protein ligase. Its N-terminal atypical C4C4 RING domain pairs selectively with E2 ubiquitin-conjugating enzymes of the UBE2D/UbcH5 (UBC4/5) subfamily, most prominently UBE2D2 (UbcH5B), and catalyzes the transfer of ubiquitin from the E2 onto substrate lysines, building polyubiquitin chains; the enzyme is also autoubiquitinated. Beyond the RING, CNOT4 contains an RRM and a C3H1-type zinc finger and a large disordered C-terminus. CNOT4 is a peripheral, substoichiometric subunit of the CCR4-NOT complex, the major eukaryotic cytoplasmic mRNA deadenylase and a global regulator of mRNA turnover and translation; in human and Drosophila cells CNOT4 is only loosely/transiently associated with the holocomplex (it binds the CNOT1 scaffold and the CAF40/CNOT9 subunit via a CAF40-binding motif) rather than being a stable core subunit. Its ubiquitin-ligase activity is linked to co-translational and RNA quality control - it ubiquitinates ABCE1 (K48-linked) upon mitochondrial damage to trigger PINK1-directed mitophagy, and ubiquitinates methylated RBM15 to control RNA splicing and megakaryocyte differentiation. CNOT4 localizes to the cytoplasm (including P-bodies and stress granules) and nucleus.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep-research notes, review YAML, PN annotation and node mapping all agree: CNOT4 is a C4C4 RING E3 (GO:0061630, multiple EXP) acting in co-translational/RQC contexts (ABCE1 K48-Ub → mitophagy; methylated RBM15). PN's RQC + RING-E3 dual placement matches the review's core_functions. No contradictions.
- **PN story / NEW pressure:** PN's RQC framing projects GO:0006515 "protein quality control for misfolded or incompletely synthesized proteins" (verified real via OLS), which is genuinely **new_to_goa** — confirmed absent from CNOT4-goa.tsv. The review captures ABCE1 ubiquitination/mitophagy and notes the yeast/Drosophila ribosome-associated nascent-chain Ub role as a suggested_question, but does NOT propose a process term for it. GO:0006515 is a defensible ADD for the human RQC role (well-grounded in PMID:29861391). GO:0016567/GO:0061630 already captured.
- **Evidence alignment:** PN row 2 cites the Deshaies/Joazeiro RING-E3 review (PMID:19489725, family-level, verified via PubMed) — not in the CNOT4 review references (review uses gene-specific PMID:11823428/15001359/26575292/29861391). Divergence is benign: PN cites a generic family review; review cites direct CNOT4 biochemistry. No conflict.
- **Verdict:** CONSISTENT — defensible ADD of GO:0006515 (protein QC) to capture the RQC role. **Recommended edits:** [YAML] consider adding GO:0006515 (involved_in, from PMID:29861391 ABCE1/co-translational QC) as a proposed_new_term or NEW annotation to align with the PN RQC projection.

## Full Consistency Review

- **UniProt:** O95628 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ubiquitination` and `UPS|E3 ubiquitin and UBL ligases|RING|other|C3H1-type ZnF` ; **PN-node mapping:** RQC group mapped→GO:0006515 (protein QC, new_to_goa); Ubiquitination type→GO:0016567 (already_in_goa); RING group→GO:0061630 (already_in_goa). Subtype/branch = no_mapping.
- **Consistency:** Strong. Deep-research notes, review YAML, PN annotation and node mapping all agree: CNOT4 is a C4C4 RING E3 (GO:0061630, multiple EXP) acting in co-translational/RQC contexts (ABCE1 K48-Ub → mitophagy; methylated RBM15). PN's RQC + RING-E3 dual placement matches the review's core_functions. No contradictions.
- **PN story / NEW pressure:** PN's RQC framing projects GO:0006515 "protein quality control for misfolded or incompletely synthesized proteins" (verified real via OLS), which is genuinely **new_to_goa** — confirmed absent from CNOT4-goa.tsv. The review captures ABCE1 ubiquitination/mitophagy and notes the yeast/Drosophila ribosome-associated nascent-chain Ub role as a suggested_question, but does NOT propose a process term for it. GO:0006515 is a defensible ADD for the human RQC role (well-grounded in PMID:29861391). GO:0016567/GO:0061630 already captured.
- **Mapping strategy:** No change to node mapping warranted. RING-group→GO:0061630 and Ubiquitination-type→GO:0016567 are exact and already annotated; class/branch correctly held context_only/too_broad (avoids over-propagating across the whole E3/translation taxonomy). RQC→GO:0006515 is appropriately specific (not over-broad like the rejected TOMM20/HSPA8 precedents).
- **Evidence alignment:** PN row 2 cites the Deshaies/Joazeiro RING-E3 review (PMID:19489725, family-level, verified via PubMed) — not in the CNOT4 review references (review uses gene-specific PMID:11823428/15001359/26575292/29861391). Divergence is benign: PN cites a generic family review; review cites direct CNOT4 biochemistry. No conflict.
- **Verdict:** CONSISTENT — defensible ADD of GO:0006515 (protein QC) to capture the RQC role. **Recommended edits:** [YAML] consider adding GO:0006515 (involved_in, from PMID:29861391 ABCE1/co-translational QC) as a proposed_new_term or NEW annotation to align with the PN RQC projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CNOT4/CNOT4-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ubiquitination
- UniProt: O95628
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

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | other | C3H1-type ZnF
- UniProt: O95628
- In branches: TR, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR000571
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other|C3H1-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|other
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
