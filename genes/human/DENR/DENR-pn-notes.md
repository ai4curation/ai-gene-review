# DENR PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43583
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DENR/DENR-ai-review.yaml](DENR-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DENR/DENR-ai-review.html](DENR-ai-review.html)
- Gene notes: present - [genes/human/DENR/DENR-notes.md](DENR-notes.md)
- GOA TSV: present - [genes/human/DENR/DENR-goa.tsv](DENR-goa.tsv)
- UniProt record: present - [genes/human/DENR/DENR-uniprot.txt](DENR-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DENR.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DENR.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DENR.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DENR.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DENR (Density-regulated protein, DRP) is a small cytoplasmic protein containing a C-terminal SUI1 (eIF1-like) domain. Together with its obligate partner MCTS1 it forms the MCTS1-DENR heterodimer, a non-canonical translation factor that is the functional equivalent of eIF2D (Ligatin) split into two polypeptides (MCTS1 corresponds to the N-terminal half, DENR to the C-terminal SUI1 half of Ligatin). The complex acts at the post-termination 40S ribosome to promote translation reinitiation, particularly after translation of short upstream ORFs (uORFs), enabling the small subunit to resume scanning and initiate at a downstream main ORF. Mechanistically the complex (i) promotes dissociation of deacylated tRNA and mRNA from recycled 40S subunits following ABCE1-mediated splitting of post-termination complexes, and (ii) recruits aminoacylated initiator tRNA into the ribosomal P-site in an eIF2-independent manner when the start codon is already positioned in the P-site (as on certain HCV-like IRESs and reinitiation events). This activity governs the translation of a defined set of mRNAs (including JAK2), and MCTS1-DENR-dependent reinitiation is required for IFN-gamma immunity.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 13

## PN Consistency Summary

- **Consistency:** Internal review/notes are self-consistent and accurate: DENR is the SUI1 half of the MCTS1-DENR heterodimer (eIF2D split), a **reinitiation / 40S-recycling** factor. But this CONTRADICTS the PN placement under "Translation termination" and the projected GO:0006415. DENR is not a release factor and does no peptide release.
- **PN story / NEW pressure:** Dossier projects GO:0006415 translational termination as `new_to_goa`. Verified (OLS): GO:0006415 = "release of a polypeptide chain from the ribosome ... in response to a termination codon" — i.e. eRF1/eRF3 activity, NOT DENR's. DENR's true process, GO:0002188 translation reinitiation, is **already in GOA** (IBA + IDA PMID:37875108) and accepted as core in the review; GO:0001731 and GO:0032790 (recycling) are also present. So the PN node mis-assigns DENR to termination; the real function is already captured. The projected term **over-reaches / is biologically wrong** for this gene.
- **Evidence alignment:** Dossier row carries no reference titles; review evidence (PMID:20713520 recycling, PMID:29889857 heterodimer, PMID:37875108 JAK2/IFN-γ) is rich and verified — no overlap to compare, divergence is by omission in the dossier.
- **Verdict:** Mapping mismatch — PN "translation termination" + GO:0006415 contradicts DENR's reinitiation/recycling biology (already in GOA as GO:0002188). **Recommended edits:** [MAP] do not project GO:0006415 to DENR; reclassify the PN node as translation reinitiation/40S recycling (GO:0002188 already in GOA).

## Full Consistency Review

- **UniProt:** O43583 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|tRNA, mRNA release` ; **PN-node mapping:** group `Translation termination` → GO:0006415 translational termination (mapped, ok_for_propagation); type `tRNA, mRNA release` no_mapping.
- **Consistency:** Internal review/notes are self-consistent and accurate: DENR is the SUI1 half of the MCTS1-DENR heterodimer (eIF2D split), a **reinitiation / 40S-recycling** factor. But this CONTRADICTS the PN placement under "Translation termination" and the projected GO:0006415. DENR is not a release factor and does no peptide release.
- **PN story / NEW pressure:** Dossier projects GO:0006415 translational termination as `new_to_goa`. Verified (OLS): GO:0006415 = "release of a polypeptide chain from the ribosome ... in response to a termination codon" — i.e. eRF1/eRF3 activity, NOT DENR's. DENR's true process, GO:0002188 translation reinitiation, is **already in GOA** (IBA + IDA PMID:37875108) and accepted as core in the review; GO:0001731 and GO:0032790 (recycling) are also present. So the PN node mis-assigns DENR to termination; the real function is already captured. The projected term **over-reaches / is biologically wrong** for this gene.
- **Mapping strategy:** This gene argues the `Translation termination|tRNA, mRNA release` node mixes genuine release factors with post-termination *recycling/reinitiation* factors (DENR, EIF2D). Recommend re-placing DENR (and EIF2D) under a reinitiation/recycling node, or at minimum not propagating GO:0006415 to them.
- **Evidence alignment:** Dossier row carries no reference titles; review evidence (PMID:20713520 recycling, PMID:29889857 heterodimer, PMID:37875108 JAK2/IFN-γ) is rich and verified — no overlap to compare, divergence is by omission in the dossier.
- **Verdict:** Mapping mismatch — PN "translation termination" + GO:0006415 contradicts DENR's reinitiation/recycling biology (already in GOA as GO:0002188). **Recommended edits:** [MAP] do not project GO:0006415 to DENR; reclassify the PN node as translation reinitiation/40S recycling (GO:0002188 already in GOA).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/DENR/DENR-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | tRNA, mRNA release
- UniProt: O43583
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation termination|tRNA, mRNA release
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
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
