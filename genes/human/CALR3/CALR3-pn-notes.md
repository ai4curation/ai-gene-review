# CALR3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96L12
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CALR3/CALR3-ai-review.yaml](CALR3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CALR3/CALR3-ai-review.html](CALR3-ai-review.html)
- Gene notes: present - [genes/human/CALR3/CALR3-notes.md](CALR3-notes.md)
- GOA TSV: present - [genes/human/CALR3/CALR3-goa.tsv](CALR3-goa.tsv)
- UniProt record: present - [genes/human/CALR3/CALR3-uniprot.txt](CALR3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CALR3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CALR3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CALR3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CALR3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: Calreticulin-3 (also known as calreticulin-2, calsperin, or CRT2) is a testis-specific member of the calreticulin/calnexin family of endoplasmic reticulum (ER) lumen chaperones and a paralog of calreticulin-1 (CALR). It has the canonical calreticulin architecture - an N-terminal globular lectin domain, a proline-rich P-domain, and a C-terminal acidic domain - together with an N-terminal signal peptide and a C-terminal ER-retention motif. During spermatogenesis it acts as a molecular chaperone that assists the folding and maturation of specific client proteins such as ADAM3 and is required for normal sperm fertility. Unlike calreticulin-1, which is a major ER calcium-buffering protein, calreticulin-3 does not bind calcium (or binds it with much lower capacity), indicating that its chaperone role rather than calcium handling is its principal function. It is localized to the lumen of the endoplasmic reticulum.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 3

## PN Consistency Summary

- **Consistency:** Consistent on identity (testis-specific calreticulin-family ER-lumen chaperone; calsperin/CRT2; client ADAM3; required for sperm fertility) across notes, YAML, and PN. Key point the YAML captures and PN does not: CALR3 does NOT bind calcium (negated GO:0005509, PMID:21590275, Stains-all) and UniProt flags it as a possibly *lectin-independent* chaperone — so the "Lectin chaperone" PN label is itself partly inaccurate for CALR3. Same GO:0006487 term-mismatch as CLGN.
- **PN story / NEW pressure:** PN's GO:0006487 projection over-reaches: CALR3 is a folding chaperone (binds clients), not an N-glycan-transfer enzyme, and is reported lectin-INdependent for ADAM3. The review's GO:0044183 protein folding chaperone, GO:0006457, GO:0007283 spermatogenesis, GO:0005788 ER lumen, and the NOT GO:0005509 capture the biology. GO:0006487 verified real but wrong-process → do not ADD.
- **Evidence alignment:** PN listed no reference titles for this row. Review anchors on PMID:21590275 (ER-lumen localization + no Ca2+ binding) and UniProt; PMID:12384296 (identification, uncached) noted. No evidence conflict; the divergence is term/label choice.
- **Verdict:** Identity consistent, but PN GO:0006487 projection **over-reaches** (chaperone, not glycosyltransferase) and the `Lectin chaperone` label sits awkwardly with CALR3's lectin-independent, non-Ca2+ profile.

## Full Consistency Review

- **UniProt:** Q96L12 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** identical to CLGN — leaf `[type] Lectin chaperone` `no_mapping`; `[group] N-glycosylation system` → `mapped` GO:0006487 protein N-linked glycosylation (`new_to_goa`); class/branch unmapped.
- **Consistency:** Consistent on identity (testis-specific calreticulin-family ER-lumen chaperone; calsperin/CRT2; client ADAM3; required for sperm fertility) across notes, YAML, and PN. Key point the YAML captures and PN does not: CALR3 does NOT bind calcium (negated GO:0005509, PMID:21590275, Stains-all) and UniProt flags it as a possibly *lectin-independent* chaperone — so the "Lectin chaperone" PN label is itself partly inaccurate for CALR3. Same GO:0006487 term-mismatch as CLGN.
- **PN story / NEW pressure:** PN's GO:0006487 projection over-reaches: CALR3 is a folding chaperone (binds clients), not an N-glycan-transfer enzyme, and is reported lectin-INdependent for ADAM3. The review's GO:0044183 protein folding chaperone, GO:0006457, GO:0007283 spermatogenesis, GO:0005788 ER lumen, and the NOT GO:0005509 capture the biology. GO:0006487 verified real but wrong-process → do not ADD.
- **Mapping strategy:** Same TOMM20-style over-reach as CLGN — the `N-glycosylation system` group projects a biosynthetic term onto a chaperone. Additionally, the `Lectin chaperone` leaf label conflicts with CALR3's documented lectin-independent mode, so even a lectin-specific mapping would be shaky. Recommend not propagating GO:0006487 to CALR3 and revisiting the leaf classification.
- **Evidence alignment:** PN listed no reference titles for this row. Review anchors on PMID:21590275 (ER-lumen localization + no Ca2+ binding) and UniProt; PMID:12384296 (identification, uncached) noted. No evidence conflict; the divergence is term/label choice.
- **Verdict:** Identity consistent, but PN GO:0006487 projection **over-reaches** (chaperone, not glycosyltransferase) and the `Lectin chaperone` label sits awkwardly with CALR3's lectin-independent, non-Ca2+ profile.

**Recommended edits:** [MAP] Do not propagate GO:0006487 to CALR3; remap `N-glycosylation system` group to a folding/glycoprotein-QC term or leave chaperone members unmapped. [MAP] Reconsider the `Lectin chaperone` leaf for CALR3 (documented lectin-independent). [YAML] No glycosylation annotation for CALR3.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CALR3/CALR3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: Q96L12
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
