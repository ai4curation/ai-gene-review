# UPF3B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BZI7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UPF3B/UPF3B-ai-review.yaml](UPF3B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UPF3B/UPF3B-ai-review.html](UPF3B-ai-review.html)
- Gene notes: present - [genes/human/UPF3B/UPF3B-notes.md](UPF3B-notes.md)
- GOA TSV: present - [genes/human/UPF3B/UPF3B-goa.tsv](UPF3B-goa.tsv)
- UniProt record: present - [genes/human/UPF3B/UPF3B-uniprot.txt](UPF3B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UPF3B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UPF3B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF3B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF3B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UPF3B (Regulator of nonsense transcripts 3B; also called UPF3X, hUpf3b, RENT3B) is a core factor of the nonsense-mediated mRNA decay (NMD) pathway, the surveillance mechanism that degrades mRNAs bearing premature termination codons. UPF3B is a peripheral component of the exon-junction complex (EJC) that is deposited upstream of exon-exon junctions after splicing. It acts as a molecular adaptor that bridges the EJC core to the central NMD machinery, binding the EJC (through its C-terminal region that contacts EIF4A3 and the MAGOH-RBM8A heterodimer) and recruiting UPF2, which in turn links to the RNA helicase/ATPase UPF1 at the terminating ribosome; together UPF2 and UPF3B stimulate the ATPase and helicase activities of UPF1 to activate NMD. UPF3B binds spliced mRNA upstream of exon-exon junctions, shuttles between nucleus and cytoplasm, and can also stimulate translation in vitro. The gene is X-linked, and loss-of-function mutations cause X-linked syndromic and non-syndromic intellectual disability (including Lujan-Fryns syndrome), reflecting an important role of NMD in neurodevelopment.
- Existing/core annotation action counts: ACCEPT: 36; KEEP_AS_NON_CORE: 29; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Gene-level consistent. Deep-research/notes, review YAML and GOA agree UPF3B is the principal active UPF3 paralog: EJC-associated NMD adaptor that recruits UPF2 and links to UPF1, stimulating NMD. Core: GO:0003729 mRNA binding, GO:0035145 EJC, GO:0170010 NMD complex, GO:0000184 NMD (ACCEPT, multiple), and notably GO:2000624 *positive* regulation of NMD — the correct opposite directionality to its antagonist paralog UPF3A. No internal contradictions; the UPF3A/UPF3B directionality is handled correctly across the pair.
- **PN story / NEW pressure:** PN groups UPF3B under "Modulation of termination," projecting GO:0006415 as new_to_goa. UPF3B's biology (positive NMD adaptor) is fully captured by GO:0000184 + GO:2000624 + EJC/complex terms. No NEW term is defensible; the termination link is indirect (acts after termination, via the surveillance complex).
- **Evidence alignment:** PN row carries no reference titles; review well-evidenced (PMID:18066079 UPF2/UPF3 bridge UPF1 / stimulate helicase; UniProt EJC-link FUNCTION; NMD/complex terms). No competing PN citations.
- **Verdict:** Consistent gene biology with correct positive directionality (mirror of UPF3A); PN group→GO:0006415 over-reaches — UPF3B's role is NMD adaptor (GO:0000184 / GO:2000624), not translational termination.

## Full Consistency Review

- **UniProt:** Q9BZI7 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|Modulation of termination` ; **PN-node mapping:** type `no_mapping`; group `mapped, ok_for_propagation` → GO:0006415 translational termination; class/branch `context_only, too_broad`. Projected: GO:0006415 (goa_status=new_to_goa).
- **Consistency:** Gene-level consistent. Deep-research/notes, review YAML and GOA agree UPF3B is the principal active UPF3 paralog: EJC-associated NMD adaptor that recruits UPF2 and links to UPF1, stimulating NMD. Core: GO:0003729 mRNA binding, GO:0035145 EJC, GO:0170010 NMD complex, GO:0000184 NMD (ACCEPT, multiple), and notably GO:2000624 *positive* regulation of NMD — the correct opposite directionality to its antagonist paralog UPF3A. No internal contradictions; the UPF3A/UPF3B directionality is handled correctly across the pair.
- **PN story / NEW pressure:** PN groups UPF3B under "Modulation of termination," projecting GO:0006415 as new_to_goa. UPF3B's biology (positive NMD adaptor) is fully captured by GO:0000184 + GO:2000624 + EJC/complex terms. No NEW term is defensible; the termination link is indirect (acts after termination, via the surveillance complex).
- **Mapping strategy:** As with the other UPF genes, GROUP→GO:0006415 (translational termination, = peptide release) over-reaches — UPF3B is an EJC/NMD adaptor, not a release factor — and would be an unsupported new GOA assertion. Type-level `no_mapping` should govern; UPF3B is already correctly anchored on GO:0000184 and positively-directed GO:2000624.
- **Evidence alignment:** PN row carries no reference titles; review well-evidenced (PMID:18066079 UPF2/UPF3 bridge UPF1 / stimulate helicase; UniProt EJC-link FUNCTION; NMD/complex terms). No competing PN citations.
- **Verdict:** Consistent gene biology with correct positive directionality (mirror of UPF3A); PN group→GO:0006415 over-reaches — UPF3B's role is NMD adaptor (GO:0000184 / GO:2000624), not translational termination.

**Recommended edits:** [MAP] do NOT project GO:0006415 (translational termination) onto UPF3B — it is an EJC/NMD adaptor acting downstream of termination, already correctly anchored on GO:0000184 and GO:2000624 (positive regulation of NMD). Type-level `no_mapping` should win.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UPF3B/UPF3B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | Modulation of termination
- UniProt: Q9BZI7
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
