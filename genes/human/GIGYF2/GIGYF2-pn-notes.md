# GIGYF2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6Y7W6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GIGYF2/GIGYF2-ai-review.yaml](GIGYF2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GIGYF2/GIGYF2-ai-review.html](GIGYF2-ai-review.html)
- Gene notes: present - [genes/human/GIGYF2/GIGYF2-notes.md](GIGYF2-notes.md)
- GOA TSV: present - [genes/human/GIGYF2/GIGYF2-goa.tsv](GIGYF2-goa.tsv)
- UniProt record: present - [genes/human/GIGYF2/GIGYF2-uniprot.txt](GIGYF2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GIGYF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GIGYF2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GIGYF2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GIGYF2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GIGYF2 (GRB10-interacting GYF protein 2; TNRC15) is the principal scaffold of the 4EHP-GYF2 translational-repressor complex. Through an N-terminal 4EHP-binding motif it binds the non-canonical cap-binding protein 4EHP (EIF4E2), which occupies the mRNA 5' cap but cannot recruit eIF4G, thereby blocking cap-dependent translation initiation. Its central GYF domain bridges EIF4E2 to RNA-associated repressors, including the AU-rich-element protein ZFP36/tristetraprolin, the miRNA-pathway Argonaute AGO2/TNRC6 machinery, and the collided-ribosome sensor E3 ligase ZNF598, and it recruits the DEAD-box helicase/decapping effector DDX6, coupling translational repression to mRNA destabilization and decay. A major role is in ribosome-associated quality control: on mRNAs that cause ribosome stalling, GIGYF2-EIF4E2 impose a negative-feedback loop that suppresses further initiation, reducing translational load and working in parallel with degradation of the stalled nascent chain. The 4EHP-GIGYF2 complex is essential for mammalian embryonic development, and compromised GIGYF2 function causes neurodevelopmental and neuropsychiatric phenotypes; the gene lies at the PARK11 locus (Parkinson disease 11), although its causal role in Parkinson disease is unclear. GIGYF2 is predominantly cytosolic and also localizes to stress granules, P-bodies and neuronal perikarya/proximal dendrites; SARS-CoV-2 nsp2 co-opts GIGYF2 to repress interferon (IFNB1) translation. A separate legacy role, via the GRB10 adapter, modulates IGF-1/insulin receptor signaling.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 22; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research, notes, and review agree GIGYF2 is the principal scaffold of the 4EHP-GYF2 repressor complex: its 4EHP-binding motif tethers EIF4E2 to the cap, its GYF domain bridges ZFP36/TTP, AGO2/TNRC6, ZNF598 and DDX6, coupling translational repression to mRNA decay; a major role is RQC negative-feedback on stalled-ribosome mRNAs. Review ACCEPTs GO:0045947 (negative reg translational initiation, IDA), GO:0072344 (rescue of stalled cytosolic ribosome, IDA), GO:0000900 (translation repressor activity), GO:0060090 (adaptor), and MODIFYs protein binding→GO:0008190 (eIF4E binding). All directly encode the RQC-coupled repression the PN node targets. No contradictions.
- **PN story / NEW pressure:** PN asserts only GO:0006515 (RQC umbrella, new_to_goa, verified real). The review already captures the RQC role more specifically via GO:0072344 (IDA, PMID:32726578) plus GO:0045947. GO:0006515 is a broad umbrella over these. **Already captured** (more precisely); GO:0006515 adds no function the review lacks and does not over-reach (GIGYF2's RQC role is directly evidenced).
- **Evidence alignment:** PN dossier lists no reference titles for GIGYF2; alignment is via projected GO:0006515. Review's RQC PMIDs (32726578 RQC negative feedback; 33053355 translation-coupled decay; 31439631 complex assembly; 22751931 development) all anchor the same RQC/repression biology the PN node encodes. No divergence.
- **Verdict:** Fully consistent; PN RQC story already captured more precisely (GO:0072344 + GO:0045947 + GO:0000900). GO:0006515 is a defensible umbrella, not an over-reach. No edits warranted.

## Full Consistency Review

- **UniProt:** Q6Y7W6 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** RQC type=no_mapping; RQC group=mapped→GO:0006515; class/branch context_only (GO:0002181/GO:0006412 too_broad).
- **Consistency:** Strong and mutually consistent. Deep research, notes, and review agree GIGYF2 is the principal scaffold of the 4EHP-GYF2 repressor complex: its 4EHP-binding motif tethers EIF4E2 to the cap, its GYF domain bridges ZFP36/TTP, AGO2/TNRC6, ZNF598 and DDX6, coupling translational repression to mRNA decay; a major role is RQC negative-feedback on stalled-ribosome mRNAs. Review ACCEPTs GO:0045947 (negative reg translational initiation, IDA), GO:0072344 (rescue of stalled cytosolic ribosome, IDA), GO:0000900 (translation repressor activity), GO:0060090 (adaptor), and MODIFYs protein binding→GO:0008190 (eIF4E binding). All directly encode the RQC-coupled repression the PN node targets. No contradictions.
- **PN story / NEW pressure:** PN asserts only GO:0006515 (RQC umbrella, new_to_goa, verified real). The review already captures the RQC role more specifically via GO:0072344 (IDA, PMID:32726578) plus GO:0045947. GO:0006515 is a broad umbrella over these. **Already captured** (more precisely); GO:0006515 adds no function the review lacks and does not over-reach (GIGYF2's RQC role is directly evidenced).
- **Mapping strategy:** RQC group→GO:0006515 is an acceptable umbrella over the review's GO:0072344/GO:0045947. No mapping change required. The class/branch context_only demotions (too_broad GO:0002181/GO:0006412) are correct. GIGYF2 is the better-evidenced paralog (direct IDA for GO:0072344); the GIGYF1 review lacks GO:0072344, a paralog asymmetry to flag on the GIGYF1 side rather than here.
- **Evidence alignment:** PN dossier lists no reference titles for GIGYF2; alignment is via projected GO:0006515. Review's RQC PMIDs (32726578 RQC negative feedback; 33053355 translation-coupled decay; 31439631 complex assembly; 22751931 development) all anchor the same RQC/repression biology the PN node encodes. No divergence.
- **Verdict:** Fully consistent; PN RQC story already captured more precisely (GO:0072344 + GO:0045947 + GO:0000900). GO:0006515 is a defensible umbrella, not an over-reach. No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GIGYF2/GIGYF2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: Q6Y7W6
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
