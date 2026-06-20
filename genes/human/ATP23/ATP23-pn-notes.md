# ATP23 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y6H3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1386)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP23/ATP23-ai-review.yaml](ATP23-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP23/ATP23-ai-review.html](ATP23-ai-review.html)
- Gene notes: present - [genes/human/ATP23/ATP23-notes.md](ATP23-notes.md)
- GOA TSV: present - [genes/human/ATP23/ATP23-goa.tsv](ATP23-goa.tsv)
- UniProt record: present - [genes/human/ATP23/ATP23-uniprot.txt](ATP23-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP23.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP23.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP23.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP23.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP23/ATP23-deep-research-falcon.md](ATP23-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATP23 encodes a conserved M76-family metalloprotease homolog associated with mitochondria. The ATP23 family is best characterized as a mitochondrial inner-membrane/intermembrane-space factor for ATP synthase biogenesis: yeast Atp23 processes the mitochondrially encoded Atp6/subunit 6 precursor and also promotes Fo-sector assembly independently of proteolysis. Human ATP23 carries the conserved metalloprotease features and is detected in human mitochondrial proteome datasets, but its direct mammalian substrate and submitochondrial topology remain less fully characterized. Older KUB3/XRCC6BP1 literature describes Ku70 binding, but the strongest functional model for UniProt Q9Y6H3 is mitochondrial ATP synthase assembly and mitochondrial protein processing rather than DNA repair.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; NEW: 1; REMOVE: 5

## PN Consistency Summary

- **Consistency:** Deep research (falcon), review, and PN agree on the core model: conserved M76 metalloprotease / ATP synthase Fo assembly factor and mitochondrial protein-processing peptidase; KUB3/XRCC6BP1 DNA-repair annotations are alias-driven and REMOVEd. One **divergence**: PN class projects GO:0035694 *catabolic* process, but the review deliberately uses GO:0034982 mitochondrial protein **processing** (maturation, not catabolism) and never adds GO:0035694.
- **PN story / NEW pressure:** PN adds GO:0005758 (IMS) as a NEW location — the review independently adopts this (action: NEW, ISO, conservative topology inference). Verified real and appropriate. No over-reach at the leaf. **ADD (IMS) — already implemented in review.**
- **Evidence alignment:** PN gives no reference titles; review anchors on PMID:17135290 + PMID:17135288 (yeast Atp23 processing + Fo assembly), PMID:34800366 (MitoCoP). GO:0035694 and GO:0005758 are both absent from goa.tsv (new), consistent with dossier.
- **Verdict:** MOSTLY CONSISTENT — IMS location good; class-level *catabolic* projection mis-flavored for an assembly/processing peptidase. **Recommended edits:** [MAP] mark GO:0035694 class projection as not_for_propagation to ATP23 (gene is processing/assembly, not catabolism); review's GO:0034982 is the correct process term.

## Full Consistency Review

- **UniProt:** Q9Y6H3 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Organelle-specific protein degradation|Intermembrane space protease` (group = mapped, GO:0005758 mitochondrial intermembrane space, more_specific_than_existing_goa); parent *class* `...|Organelle-specific protein degradation` = mapped, GO:0035694 mitochondrial protein catabolic process (new_to_goa).
- **Consistency:** Deep research (falcon), review, and PN agree on the core model: conserved M76 metalloprotease / ATP synthase Fo assembly factor and mitochondrial protein-processing peptidase; KUB3/XRCC6BP1 DNA-repair annotations are alias-driven and REMOVEd. One **divergence**: PN class projects GO:0035694 *catabolic* process, but the review deliberately uses GO:0034982 mitochondrial protein **processing** (maturation, not catabolism) and never adds GO:0035694.
- **PN story / NEW pressure:** PN adds GO:0005758 (IMS) as a NEW location — the review independently adopts this (action: NEW, ISO, conservative topology inference). Verified real and appropriate. No over-reach at the leaf. **ADD (IMS) — already implemented in review.**
- **Mapping strategy:** The leaf (IMS protease → GO:0005758) is sound and gene-appropriate. The **class-level GO:0035694 over-reaches**: its OLS definition is "breakdown of a mitochondrial protein via an intramitochondrial lysosome-like organelle to eliminate damaged/oxidised proteins" — ATP23 is a *processing/assembly* peptidase, not a catabolic degrader. This is the TOMM20/HSPA8 "broader/wrong-flavor parent" failure mode. Recommend the class projection not propagate to ATP23.
- **Evidence alignment:** PN gives no reference titles; review anchors on PMID:17135290 + PMID:17135288 (yeast Atp23 processing + Fo assembly), PMID:34800366 (MitoCoP). GO:0035694 and GO:0005758 are both absent from goa.tsv (new), consistent with dossier.
- **Verdict:** MOSTLY CONSISTENT — IMS location good; class-level *catabolic* projection mis-flavored for an assembly/processing peptidase. **Recommended edits:** [MAP] mark GO:0035694 class projection as not_for_propagation to ATP23 (gene is processing/assembly, not catabolism); review's GO:0034982 is the correct process term.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP23/ATP23-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Intermembrane space protease
- UniProt: Q9Y6H3
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Intermembrane space protease
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005758 mitochondrial intermembrane space]
        rationale: This PN group captures proteases assigned specifically to the mitochondrial intermembrane space. The source bucket is compartmental and mechanistic rather than a single shared enzymatic GO class, so the mitochondrial intermembrane space cellular-component term is the conservative propagation target.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0005758 mitochondrial intermembrane space | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation|Intermembrane space protease

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
