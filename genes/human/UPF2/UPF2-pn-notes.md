# UPF2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9HAU5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UPF2/UPF2-ai-review.yaml](UPF2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UPF2/UPF2-ai-review.html](UPF2-ai-review.html)
- Gene notes: present - [genes/human/UPF2/UPF2-notes.md](UPF2-notes.md)
- GOA TSV: present - [genes/human/UPF2/UPF2-goa.tsv](UPF2-goa.tsv)
- UniProt record: present - [genes/human/UPF2/UPF2-uniprot.txt](UPF2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UPF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UPF2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UPF2 (regulator of nonsense transcripts 2; RENT2) is a core adaptor of the nonsense-mediated mRNA decay (NMD) pathway. Built around tandem MIF4G domains with a C-terminal UPF1-binding region, UPF2 bridges UPF1 (bound to the release factors eRF1/eRF3 at a terminating ribosome) to UPF3B and the exon-junction complex, nucleating the UPF1-UPF2-UPF3 surveillance complex that activates NMD. Binding of UPF2 (together with UPF3B) relieves UPF1 autoinhibition and stimulates its ATPase and RNA helicase activities, committing premature-termination-codon and certain long-3'UTR transcripts to decay. UPF2 acts mainly at the cytoplasmic/perinuclear face of the nuclear envelope and in the cytoplasm, binds spliced mRNA, and has additional reported associations (e.g. telomere/TERRA, mRNA export) peripheral to its core NMD adaptor role.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 36

## PN Consistency Summary

- **Consistency:** Gene-level: consistent. Deep-research/notes, review YAML and GOA agree UPF2 is the NMD adaptor (tandem MIF4G + C-terminal UPF1-binding region) bridging UPF1 to UPF3B/EJC, relieving UPF1 autoinhibition and stimulating its ATPase/helicase. Core annotations: GO:0000184 NMD (multiple, ACCEPT), GO:0035145 EJC, GO:0170010 NMD complex, GO:0003723 RNA binding. But the PN-node frame (translation termination) is not reflected in the review's account of UPF2.
- **PN story / NEW pressure:** PN places UPF2 under "Modulation of termination," projecting GO:0006415 as *new_to_goa*. GOA cross-check confirms UPF2 has NO translational-termination annotation (and no GO:0006449 either). But UPF2 is an NMD adaptor, not a release/termination factor — its termination link is indirect (acts on UPF1 after termination). The story is already captured by GO:0000184 NMD; no NEW translation-termination term is defensible for UPF2.
- **Evidence alignment:** PN row carries no reference titles; review is well-evidenced for the NMD-adaptor role (UniProt FUNCTION; EJC/complex terms). No competing citations to reconcile.
- **Verdict:** Gene biology consistent, but PN group→GO:0006415 over-reaches and would create an unsupported new GOA term; UPF2's role is NMD adaptor (GO:0000184), not translational termination.

## Full Consistency Review

- **UniProt:** Q9HAU5 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|Modulation of termination` ; **PN-node mapping:** type `no_mapping`; group `mapped, ok_for_propagation` → GO:0006415 translational termination; class/branch `context_only, too_broad`. Projected: GO:0006415 (goa_status=new_to_goa).
- **Consistency:** Gene-level: consistent. Deep-research/notes, review YAML and GOA agree UPF2 is the NMD adaptor (tandem MIF4G + C-terminal UPF1-binding region) bridging UPF1 to UPF3B/EJC, relieving UPF1 autoinhibition and stimulating its ATPase/helicase. Core annotations: GO:0000184 NMD (multiple, ACCEPT), GO:0035145 EJC, GO:0170010 NMD complex, GO:0003723 RNA binding. But the PN-node frame (translation termination) is not reflected in the review's account of UPF2.
- **PN story / NEW pressure:** PN places UPF2 under "Modulation of termination," projecting GO:0006415 as *new_to_goa*. GOA cross-check confirms UPF2 has NO translational-termination annotation (and no GO:0006449 either). But UPF2 is an NMD adaptor, not a release/termination factor — its termination link is indirect (acts on UPF1 after termination). The story is already captured by GO:0000184 NMD; no NEW translation-termination term is defensible for UPF2.
- **Mapping strategy:** The GROUP→GO:0006415 (translational termination, = polypeptide release) projection is wrong for UPF2 — it would add a peptide-release process the protein does not perform, and would be a genuinely new (unsupported) GOA assertion. This is the clearest over-reach of the UPF set (new_to_goa, no regulatory-term backstop unlike UPF1). The type-level `no_mapping` is correct and should govern; do not project GO:0006415.
- **Evidence alignment:** PN row carries no reference titles; review is well-evidenced for the NMD-adaptor role (UniProt FUNCTION; EJC/complex terms). No competing citations to reconcile.
- **Verdict:** Gene biology consistent, but PN group→GO:0006415 over-reaches and would create an unsupported new GOA term; UPF2's role is NMD adaptor (GO:0000184), not translational termination.

**Recommended edits:** [MAP] do NOT project GO:0006415 (translational termination) onto UPF2 — it is an NMD adaptor recruited downstream of termination, not a peptide-release factor; the type-level `no_mapping` should win. UPF2 is already correctly anchored on GO:0000184 (NMD).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UPF2/UPF2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | Modulation of termination
- UniProt: Q9HAU5
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
