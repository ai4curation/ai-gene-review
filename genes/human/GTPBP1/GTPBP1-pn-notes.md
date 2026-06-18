# GTPBP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O00178
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GTPBP1/GTPBP1-ai-review.yaml](GTPBP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GTPBP1/GTPBP1-ai-review.html](GTPBP1-ai-review.html)
- Gene notes: present - [genes/human/GTPBP1/GTPBP1-notes.md](GTPBP1-notes.md)
- GOA TSV: present - [genes/human/GTPBP1/GTPBP1-goa.tsv](GTPBP1-goa.tsv)
- UniProt record: present - [genes/human/GTPBP1/GTPBP1-uniprot.txt](GTPBP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GTPBP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GTPBP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GTPBP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GTPBP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GTPBP1 (GTP-binding protein 1, also called GP-1) is a cytoplasmic translational GTPase of the TRAFAC-class translation-factor superfamily, most closely related to eEF1A, eRF3 and Hbs1. It possesses eEF1A-like elongation activity, forming ternary complexes with GTP and aminoacyl-tRNA and delivering cognate aa-tRNA to the ribosomal A site in a GTP-dependent manner, and can also deliver deacylated tRNA. aa-tRNA binding stabilizes its GTP binding and stimulates GTP hydrolysis. Unlike canonical eEF1A, GTP hydrolysis by GTPBP1 is not promptly followed by peptide-bond formation; it retains aa-tRNA in the A site, which delays accommodation and can stall the ribosome, coupling GTPBP1 to mRNA surveillance and ribosome-associated quality control, notably by promoting exosome-mediated degradation of faulty mRNAs engaged in elongation complexes. GTPBP1 associates with cytoplasmic exosome subunits and has been implicated in the regulation of circadian mRNA stability. Loss-of-function variants cause an autosomal-recessive neurodevelopmental disorder (NEDFET1).
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 5

## PN Consistency Summary

- **Consistency:** Largely consistent on biology, with one term-level mismatch. Deep research, notes, and review agree GTPBP1 is an eEF1A-like translational GTPase that delivers aa-tRNA to the A site but, with non-canonical kinetics (delayed peptide-bond formation), retains aa-tRNA, stalls the ribosome, and promotes exosome-mediated degradation of faulty mRNAs — i.e., couples elongation to mRNA surveillance/RQC (PMID:30108131). Review ACCEPTs GO:0003746 (elongation factor activity), GO:0003924 (GTPase), GO:0071025 (RNA surveillance, IDA), GO:0061014 (positive regulation of mRNA catabolic process). The review does NOT carry GO:0072344 — it frames GTPBP1's QC role as mRNA surveillance/decay (GO:0071025/GO:0061014), not ribosome rescue.
- **PN story / NEW pressure:** PN's "Ribosomal rescue" type→GO:0072344 (verified real; goa_status=more_specific_than_existing_goa) asserts GTPBP1 rescues stalled cytosolic ribosomes. This is the divergence: GTPBP1's documented role is to CAUSE stalling and recruit the exosome to degrade the mRNA (a surveillance/decay outcome), not to split/rescue the stalled ribosome (the PELO/HBS1L/ABCE1 sense of GO:0072344). GTPBP1 GOA contains GO:0071025 but NOT GO:0072344. So GO:0072344 is a candidate NEW term that **over-reaches**: the evidence supports mRNA surveillance (GO:0071025, already present) rather than ribosome rescue. The PN "more_specific_than_existing_goa" framing is questionable — GO:0072344 is not strictly more specific than GO:0071025; they are different processes.
- **Evidence alignment:** PN dossier lists no reference titles for GTPBP1; the single mechanistic anchor (PMID:30108131) is shared with the review (cited HIGH/VERIFIED). The review reads that paper as surveillance/exosomal decay (GO:0071025/GO:0061014); PN reads it as ribosome rescue (GO:0072344) — same paper, divergent term interpretation.
- **Verdict:** Biology consistent; PN's GO:0072344 "Ribosomal rescue" mapping over-reaches vs the review's surveillance/decay framing (GO:0071025 present in GOA; GO:0072344 absent). **Recommended edits:** [MAP] do not project GO:0072344 (rescue of stalled cytosolic ribosome) onto GTPBP1 — its evidenced role is mRNA surveillance/exosomal decay (GO:0071025/GO:0061014), not ribosome rescue; reclassify the PN row from "Ribosomal rescue" to "other RQC processes" (RQC-group→GO:0006515 still applies). [REF] PMID:30108131 supports surveillance, not rescue — note the interpretive divergence.

## Full Consistency Review

- **UniProt:** O00178 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` ; **PN-node mapping:** rescue type=mapped→GO:0072344 (rescue of stalled cytosolic ribosome); RQC group=mapped→GO:0006515; class/branch context_only (GO:0002181/GO:0006412 too_broad).
- **Consistency:** Largely consistent on biology, with one term-level mismatch. Deep research, notes, and review agree GTPBP1 is an eEF1A-like translational GTPase that delivers aa-tRNA to the A site but, with non-canonical kinetics (delayed peptide-bond formation), retains aa-tRNA, stalls the ribosome, and promotes exosome-mediated degradation of faulty mRNAs — i.e., couples elongation to mRNA surveillance/RQC (PMID:30108131). Review ACCEPTs GO:0003746 (elongation factor activity), GO:0003924 (GTPase), GO:0071025 (RNA surveillance, IDA), GO:0061014 (positive regulation of mRNA catabolic process). The review does NOT carry GO:0072344 — it frames GTPBP1's QC role as mRNA surveillance/decay (GO:0071025/GO:0061014), not ribosome rescue.
- **PN story / NEW pressure:** PN's "Ribosomal rescue" type→GO:0072344 (verified real; goa_status=more_specific_than_existing_goa) asserts GTPBP1 rescues stalled cytosolic ribosomes. This is the divergence: GTPBP1's documented role is to CAUSE stalling and recruit the exosome to degrade the mRNA (a surveillance/decay outcome), not to split/rescue the stalled ribosome (the PELO/HBS1L/ABCE1 sense of GO:0072344). GTPBP1 GOA contains GO:0071025 but NOT GO:0072344. So GO:0072344 is a candidate NEW term that **over-reaches**: the evidence supports mRNA surveillance (GO:0071025, already present) rather than ribosome rescue. The PN "more_specific_than_existing_goa" framing is questionable — GO:0072344 is not strictly more specific than GO:0071025; they are different processes.
- **Mapping strategy:** This gene's placement under "Ribosomal rescue" is the issue. GTPBP1 fits "other RQC processes" / mRNA surveillance better than "Ribosomal rescue." The rescue type→GO:0072344 projection should not be applied to O00178. RQC group→GO:0006515 (umbrella) is acceptable. Recommend reclassifying or, at minimum, not projecting GO:0072344.
- **Evidence alignment:** PN dossier lists no reference titles for GTPBP1; the single mechanistic anchor (PMID:30108131) is shared with the review (cited HIGH/VERIFIED). The review reads that paper as surveillance/exosomal decay (GO:0071025/GO:0061014); PN reads it as ribosome rescue (GO:0072344) — same paper, divergent term interpretation.
- **Verdict:** Biology consistent; PN's GO:0072344 "Ribosomal rescue" mapping over-reaches vs the review's surveillance/decay framing (GO:0071025 present in GOA; GO:0072344 absent). **Recommended edits:** [MAP] do not project GO:0072344 (rescue of stalled cytosolic ribosome) onto GTPBP1 — its evidenced role is mRNA surveillance/exosomal decay (GO:0071025/GO:0061014), not ribosome rescue; reclassify the PN row from "Ribosomal rescue" to "other RQC processes" (RQC-group→GO:0006515 still applies). [REF] PMID:30108131 supports surveillance, not rescue — note the interpretive divergence.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GTPBP1/GTPBP1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: O00178
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072344 rescue of stalled cytosolic ribosome]
        rationale: This PN RQC type denotes rescue of stalled cytosolic ribosomes. The matching GO process term is the direct target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (2)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
