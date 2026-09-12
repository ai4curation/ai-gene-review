# SEC11A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P67812
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SEC11A/SEC11A-ai-review.yaml](SEC11A-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SEC11A/SEC11A-ai-review.html
- Gene notes: present - [genes/human/SEC11A/SEC11A-notes.md](SEC11A-notes.md)
- GOA TSV: present - [genes/human/SEC11A/SEC11A-goa.tsv](SEC11A-goa.tsv)
- UniProt record: present - [genes/human/SEC11A/SEC11A-uniprot.txt](SEC11A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SEC11A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SEC11A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SEC11A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SEC11A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SEC11A/SEC11A-deep-research-falcon.md](SEC11A-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SEC11A (SPC18, SEC11L1; EC 3.4.21.89) is a single-pass type II endoplasmic reticulum membrane protein and one of the two catalytic serine-endopeptidase subunits of the human signal peptidase complex (SPC). As the proteolytic subunit of the SPC-A paralog (with accessory subunits SPCS1, SPCS2 and SPCS3), SEC11A catalyzes cleavage of N-terminal signal (leader) peptides from secretory and membrane pre-proteins as they are translocated into the ER lumen. It belongs to peptidase family S26B and uses a Ser/His/Asp-type charge-relay catalytic system (Ser-56 nucleophile). Its active site abuts the ER membrane, where the complex locally thins the lipid bilayer; this architecture confers selectivity for signal peptides whose hydrophobic h-region is shorter than ~18-20 residues. SEC11A is the more broadly/highly expressed of the two catalytic paralogs (the other being SEC11C) and is broadly required for biogenesis of the secretory proteome.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, review YAML, and PN all identify SEC11A as the catalytic serine-endopeptidase subunit of the SPC-A paralog (Ser-56 triad, EC 3.4.21.89, membrane-thinning specificity). PN's "ER signal peptidase" node correctly captures complex membership. No contradictions.
- **PN story / NEW pressure:** PN asserts only complex membership (GO:0005787) and the broad transport class (GO:0015031). Both already captured: review has GO:0005787 (IDA/IPI/IBA/IEA) plus the catalytic MF (GO:0009003 signal peptidase activity, GO:0004252 serine-type endopeptidase activity, EXP/IDA) — the latter being the gene's distinguishing function, which the PN node (a CC-level membership) does NOT assert. So PN under-specifies SEC11A's catalytic MF rather than over-reaching. No NEW term needed. Conclude: already captured (review is richer than PN).
- **Evidence alignment:** PN row carries no titles; review's catalytic evidence (PMID:34388369 cryo-EM/triad; Reactome signalase reactions; PMID:36454823 QC; PMID:28423309 cavinafungin) and falcon deep research (liaci2021) all converge on the catalytic identity. Congruent.
- **Verdict:** CONSISTENT; PN captures CC membership but omits the catalytic MF that defines SEC11A (already in review). No edit required.

## Full Consistency Review

- **UniProt:** P67812 (SPC18) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|ER signal peptidase`; **PN-node mapping:** group mapped, ok_for_propagation_to_go, GO:0005787 (signal peptidase complex); class GO:0015031 (protein transport).
- **Consistency:** Strong agreement. Deep research, review YAML, and PN all identify SEC11A as the catalytic serine-endopeptidase subunit of the SPC-A paralog (Ser-56 triad, EC 3.4.21.89, membrane-thinning specificity). PN's "ER signal peptidase" node correctly captures complex membership. No contradictions.
- **PN story / NEW pressure:** PN asserts only complex membership (GO:0005787) and the broad transport class (GO:0015031). Both already captured: review has GO:0005787 (IDA/IPI/IBA/IEA) plus the catalytic MF (GO:0009003 signal peptidase activity, GO:0004252 serine-type endopeptidase activity, EXP/IDA) — the latter being the gene's distinguishing function, which the PN node (a CC-level membership) does NOT assert. So PN under-specifies SEC11A's catalytic MF rather than over-reaching. No NEW term needed. Conclude: already captured (review is richer than PN).
- **Mapping strategy:** Mapping is correct but blunt: the node maps the whole "ER signal peptidase" group to the CC GO:0005787, which conflates catalytic (SEC11A/C) and accessory (SPCS1/2/3) members. For SEC11A specifically the catalytic peptidase MF is the salient function and is not represented at the node. Node need not change (GO:0005787 is right for all four), but a node-level note should distinguish catalytic-subunit MF (GO:0009003/GO:0004252) for SEC11A/C. GO:0015031 protein transport is acceptably broad. No precedent-style over-reach.
- **Evidence alignment:** PN row carries no titles; review's catalytic evidence (PMID:34388369 cryo-EM/triad; Reactome signalase reactions; PMID:36454823 QC; PMID:28423309 cavinafungin) and falcon deep research (liaci2021) all converge on the catalytic identity. Congruent.
- **Verdict:** CONSISTENT; PN captures CC membership but omits the catalytic MF that defines SEC11A (already in review). No edit required.
- **Recommended edits:** [MAP] At the "ER signal peptidase" node, annotate that catalytic subunits SEC11A/SEC11C additionally project signal peptidase MF (GO:0009003 / GO:0004252), distinct from accessory subunits — so the node does not flatten catalytic vs accessory members.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SEC11A/SEC11A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | ER signal peptidase
- UniProt: P67812
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|ER signal peptidase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005787 signal peptidase complex]
        rationale: This PN group denotes ER signal peptidase complex components. The matching GO cellular-component term is the direct propagation target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0005787 signal peptidase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|ER signal peptidase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
