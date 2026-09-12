# LMAN1L PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9HAT1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LMAN1L/LMAN1L-ai-review.yaml](LMAN1L-ai-review.yaml)
- AIGR review HTML: missing - genes/human/LMAN1L/LMAN1L-ai-review.html
- Gene notes: present - [genes/human/LMAN1L/LMAN1L-notes.md](LMAN1L-notes.md)
- GOA TSV: present - [genes/human/LMAN1L/LMAN1L-goa.tsv](LMAN1L-goa.tsv)
- UniProt record: present - [genes/human/LMAN1L/LMAN1L-uniprot.txt](LMAN1L-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN1L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN1L.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN1L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN1L.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/LMAN1L/LMAN1L-deep-research-falcon.md](LMAN1L-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: LMAN1L (ERGL; "Protein ERGIC-53-like", also "Lectin mannose-binding 1-like") is a testis- and prostate-enriched human paralog of LMAN1/ERGIC-53 and a member of the L-type lectin (legume lectin-like) family. It is a 526-aa single-pass type I membrane glycoprotein with a lumenal L-type lectin-like domain, a single transmembrane segment, and a short cytoplasmic tail, an architecture typical of ERGIC/ER-resident cargo receptors. By homology to ERGIC-53 it is predicted to be a calcium-dependent mannose-binding lectin that acts as a cargo receptor in the endoplasmic reticulum-Golgi intermediate compartment and in COPII-mediated ER-to-Golgi transport. Direct functional evidence is lacking, however; the protein is characterized only at the transcript level and essentially all of its functional roles are inferred by homology (phylogenetic and electronic annotation) rather than demonstrated for this paralog.
- Existing/core annotation action counts: KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Deep research ↔ review ↔ PN annotation consistent and appropriately hedged. LMAN1L is a testis/prostate-enriched LMAN1 paralog with an L-type lectin domain; the review keeps essentially all annotations KEEP_AS_NON_CORE because there is NO direct functional evidence (Falcon returned no gene-specific experimental literature). It is correctly treated as a predicted lectin (not a glycosidase). No contradictions.
- **PN story / NEW pressure:** No NEW pressure — there is barely enough evidence to support the existing predicted-lectin framing, let alone a new term. Conclude: nothing to add; uncharacterized paralog.
- **Evidence alignment:** PN dossier is mapping-only. The review's sole experimental reference is an ECM-proteomics co-isolate (PMID:28675934), explicitly flagged as a transmembrane contaminant; everything else is IBA/IEA/UniProt-by-similarity. No bibliographic conflict; the only divergence is the inappropriate group-level biosynthesis projection.
- **Verdict:** Review correctly conservative for an uncharacterized paralog; PN node correct to leave it unmapped. Inherited group→GO:0006487 projection is an over-reach (wrong branch + unsupported on a PE 2 gene).

## Full Consistency Review

- **UniProt:** Q9HAT1 (Protein ERGIC-53-like / ERGL) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE; intentionally cautious (PE 2, transcript-level only; all roles homology-inferred).
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** type "Lectin chaperone" no_mapping; group "N-glycosylation system" mapped→GO:0006487 (protein N-linked glycosylation, ok_for_propagation, new_to_goa); class/branch no_mapping.
- **Consistency:** Deep research ↔ review ↔ PN annotation consistent and appropriately hedged. LMAN1L is a testis/prostate-enriched LMAN1 paralog with an L-type lectin domain; the review keeps essentially all annotations KEEP_AS_NON_CORE because there is NO direct functional evidence (Falcon returned no gene-specific experimental literature). It is correctly treated as a predicted lectin (not a glycosidase). No contradictions.
- **PN story / NEW pressure:** No NEW pressure — there is barely enough evidence to support the existing predicted-lectin framing, let alone a new term. Conclude: nothing to add; uncharacterized paralog.
- **Mapping strategy:** **Group→GO:0006487 (new_to_goa) is doubly inappropriate here:** (1) wrong branch — predicted glycan-reader, not an N-glycosylation installer (same over-reach as LMAN1/LMAN2); (2) the gene is uncharacterized (PE 2), so projecting any new biosynthesis assertion onto it is unwarranted. PN node correctly leaves "Lectin chaperone" unmapped. The projected GO term should not propagate to this paralog.
- **Evidence alignment:** PN dossier is mapping-only. The review's sole experimental reference is an ECM-proteomics co-isolate (PMID:28675934), explicitly flagged as a transmembrane contaminant; everything else is IBA/IEA/UniProt-by-similarity. No bibliographic conflict; the only divergence is the inappropriate group-level biosynthesis projection.
- **Verdict:** Review correctly conservative for an uncharacterized paralog; PN node correct to leave it unmapped. Inherited group→GO:0006487 projection is an over-reach (wrong branch + unsupported on a PE 2 gene).
**Recommended edits:** [MAP] Suppress GO:0006487 (protein N-linked glycosylation) propagation to LMAN1L — predicted lectin/cargo receptor, no N-glycosylation activity, and transcript-level-only evidence; do not introduce a new biosynthesis annotation on an uncharacterized paralog.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/LMAN1L/LMAN1L-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: Q9HAT1
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] ER proteostasis|Glycoproteostasis|N-glycosylation system
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006487 protein N-linked glycosylation]
        rationale: This PN group captures the ER N-glycosylation machinery that installs and processes N-linked glycans during proteostasis. GO protein N-linked glycosylation is the best current propagation target in the local cache.
    - [class] ER proteostasis|Glycoproteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
