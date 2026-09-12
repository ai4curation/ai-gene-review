# UPF3A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H1J1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UPF3A/UPF3A-ai-review.yaml](UPF3A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UPF3A/UPF3A-ai-review.html](UPF3A-ai-review.html)
- Gene notes: present - [genes/human/UPF3A/UPF3A-notes.md](UPF3A-notes.md)
- GOA TSV: present - [genes/human/UPF3A/UPF3A-goa.tsv](UPF3A-goa.tsv)
- UniProt record: present - [genes/human/UPF3A/UPF3A-uniprot.txt](UPF3A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UPF3A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UPF3A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF3A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF3A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UPF3A (Regulator of nonsense transcripts 3A; hUpf3p/hUPF3L) is a nonsense-mediated mRNA decay (NMD) factor and the paralog of UPF3B. It is a nuclear/cytoplasmic shuttling protein that associates with the exon-junction complex (EJC) deposited upstream of exon-exon junctions on spliced mRNA and acts as a molecular adaptor bridging the EJC to the core NMD machinery, binding UPF2 (and RBM8A/EJC) and helping assemble the UPF1-UPF2-UPF3 surveillance complex that licenses decay of premature-termination-codon-containing mRNAs. UPF3A is only marginally active in promoting NMD compared with UPF3B; because the two paralogs compete for the same MIF4G-III surface of UPF2, UPF3A can act as an NMD antagonist/repressor by sequestering UPF2, and in many tissues UPF3A is itself cleared but is stabilized by binding UPF2 when functional UPF3B is absent. UPF3A also binds spliced mRNA and weakly stimulates translation in vitro, and has been reported to bind telomeric-repeat (TERRA) RNA/DNA in the context of telomere RNA surveillance. Through these activities UPF3A contributes to the magnitude and substrate selectivity of NMD and to paralog-buffering of the NMD pathway during development.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 14; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Gene-level consistent and notably careful on directionality: deep-research/notes and review YAML agree UPF3A is the partial NMD ANTAGONIST of UPF3B — only marginally active in canonical NMD, competes with UPF3B for the UPF2 MIF4G-III surface, sequesters UPF2 to repress/buffer NMD. The review encodes this with a NEGATED GO:0000184 (NMD, NOT, IDA PMID:16601204, ACCEPT) and an ACCEPTed GO:2000623 (negative regulation of NMD), plus core_function GO:0140311 protein sequestering activity. This antagonist directionality is the opposite of the simple "termination factor" the PN node implies — a real framing mismatch.
- **PN story / NEW pressure:** PN groups UPF3A with the active termination/NMD factors and projects GO:0006415 as new_to_goa. This both (a) over-reaches as with the other UPF genes (UPF3A is not a peptide-release factor), and (b) ignores UPF3A's antagonist/negative-regulation directionality already captured by GO:2000623. No NEW term needed; the negative-regulation and sequestering story is already annotated.
- **Evidence alignment:** PN row carries no reference titles; review cites PMID:16601204 (UPF3A inactive in canonical NMD), PMID:35640974 (UPF2-dependent stabilization), PMID:14636577 (UPF2/EJC interactions). No competing PN citations.
- **Verdict:** Consistent gene biology with correct antagonist directionality in the YAML; PN group→GO:0006415 over-reaches AND mis-directs (UPF3A is an NMD repressor — GO:2000623 — not a termination/decay driver).

## Full Consistency Review

- **UniProt:** Q9H1J1 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|Modulation of termination` ; **PN-node mapping:** type `no_mapping`; group `mapped, ok_for_propagation` → GO:0006415 translational termination; class/branch `context_only, too_broad`. Projected: GO:0006415 (goa_status=new_to_goa).
- **Consistency:** Gene-level consistent and notably careful on directionality: deep-research/notes and review YAML agree UPF3A is the partial NMD ANTAGONIST of UPF3B — only marginally active in canonical NMD, competes with UPF3B for the UPF2 MIF4G-III surface, sequesters UPF2 to repress/buffer NMD. The review encodes this with a NEGATED GO:0000184 (NMD, NOT, IDA PMID:16601204, ACCEPT) and an ACCEPTed GO:2000623 (negative regulation of NMD), plus core_function GO:0140311 protein sequestering activity. This antagonist directionality is the opposite of the simple "termination factor" the PN node implies — a real framing mismatch.
- **PN story / NEW pressure:** PN groups UPF3A with the active termination/NMD factors and projects GO:0006415 as new_to_goa. This both (a) over-reaches as with the other UPF genes (UPF3A is not a peptide-release factor), and (b) ignores UPF3A's antagonist/negative-regulation directionality already captured by GO:2000623. No NEW term needed; the negative-regulation and sequestering story is already annotated.
- **Mapping strategy:** GROUP→GO:0006415 is wrong for UPF3A on two counts: wrong process (peptide release) and wrong direction (UPF3A dampens, not drives, decay). Projecting a positive translation-termination/NMD-adjacent term onto a partial antagonist is a directionality error the reviewers explicitly guarded against (negated GO:0000184). Type-level `no_mapping` should govern.
- **Evidence alignment:** PN row carries no reference titles; review cites PMID:16601204 (UPF3A inactive in canonical NMD), PMID:35640974 (UPF2-dependent stabilization), PMID:14636577 (UPF2/EJC interactions). No competing PN citations.
- **Verdict:** Consistent gene biology with correct antagonist directionality in the YAML; PN group→GO:0006415 over-reaches AND mis-directs (UPF3A is an NMD repressor — GO:2000623 — not a termination/decay driver).

**Recommended edits:** [MAP] do NOT project GO:0006415 (translational termination) onto UPF3A; UPF3A is a partial NMD antagonist (negated GO:0000184; GO:2000623 negative regulation of NMD; GO:0140311 sequestering). The type-level `no_mapping` should win, and any node-level frame must respect its negative/antagonist directionality.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UPF3A/UPF3A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | Modulation of termination
- UniProt: Q9H1J1
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation termination|Modulation of termination
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN bucket. The label is useful for curator triage, but no direct GO mapping is appropriate because propagation would add a process, activity, or localization not shared cleanly by all members.
    - [group] Translation|Cytosolic translation|Translation termination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006415 translational termination]
        rationale: This PN group denotes cytosolic translation termination and release factors. Translational termination is the shared process target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006415 translational termination | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Translation termination

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
