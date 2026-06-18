# CLGN PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O14967
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CLGN/CLGN-ai-review.yaml](CLGN-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CLGN/CLGN-ai-review.html](CLGN-ai-review.html)
- Gene notes: present - [genes/human/CLGN/CLGN-notes.md](CLGN-notes.md)
- GOA TSV: present - [genes/human/CLGN/CLGN-goa.tsv](CLGN-goa.tsv)
- UniProt record: present - [genes/human/CLGN/CLGN-uniprot.txt](CLGN-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CLGN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CLGN.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CLGN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CLGN.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: Calmegin (CLGN) is a testis-specific, type I single-pass integral membrane lectin-type molecular chaperone of the endoplasmic reticulum that is homologous to calnexin and belongs to the calreticulin/calnexin family. Its luminal domain contains a globular concanavalin A-like lectin fold and the extended proline-rich P domain characteristic of calnexin/calreticulin, and it binds calcium ions. Expressed during spermatogenesis in male germ cells, calmegin binds nascent polypeptides and assists the folding and assembly of a range of client proteins required for sperm function, most notably the ADAM-family sperm surface proteins fertilin (ADAM1/ADAM2) and ADAM3, whose maturation and heterodimerization depend on it. It forms a germ-cell ER chaperone complex with the testis-specific protein disulfide isomerase-like protein PDILT and also interacts with the peptidyl-prolyl isomerase cyclophilin B (PPIB), paralleling the calnexin/ERp57 system. Through chaperoning these clients, calmegin is essential for sperm adhesion to and penetration of the egg zona pellucida and for sperm migration from the uterus into the oviduct; loss of function causes male infertility in mice.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Mostly consistent on identity (testis-specific calnexin-family lectin-type ER membrane chaperone; clients = ADAM1/2/ADAM3; essential for sperm-zona binding/fertility) across notes, YAML, and PN. The friction is the projected GO term: the PN node projects GO:0006487 (the biosynthetic process that *adds* N-glycans), but CLGN is a lectin chaperone that *binds* monoglucosylated N-glycans on clients — it does not catalyze glycan transfer. The review correctly annotates GO:0044183 protein folding chaperone / GO:0006457 protein folding, not glycosylation.
- **PN story / NEW pressure:** PN's "N-glycosylation system" framing over-reaches when projected as GO:0006487 for a lectin chaperone. CLGN's real, review-captured roles (folding chaperone, single fertilization GO:0007338) are already in GOA/review. GO:0006487 is verified real but is the WRONG process for this gene's mechanism → over-reaches; do not ADD to the gene.
- **Evidence alignment:** PN listed no reference titles for this row. Review anchors on PMID:9177349 (knockout/zona-adhesion), PMID:17507649 (PDILT complex), PMID:9434179 (cloning). No conflict; the divergence is term choice, not evidence.
- **Verdict:** Identity consistent, but PN GO:0006487 projection **over-reaches** for a lectin chaperone (binds, not synthesizes, N-glycans); should not propagate to CLGN.

## Full Consistency Review

- **UniProt:** O14967 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** leaf `[type] Lectin chaperone` `no_mapping`; `[group] N-glycosylation system` → `mapped` GO:0006487 protein N-linked glycosylation (`new_to_goa`); class/branch unmapped.
- **Consistency:** Mostly consistent on identity (testis-specific calnexin-family lectin-type ER membrane chaperone; clients = ADAM1/2/ADAM3; essential for sperm-zona binding/fertility) across notes, YAML, and PN. The friction is the projected GO term: the PN node projects GO:0006487 (the biosynthetic process that *adds* N-glycans), but CLGN is a lectin chaperone that *binds* monoglucosylated N-glycans on clients — it does not catalyze glycan transfer. The review correctly annotates GO:0044183 protein folding chaperone / GO:0006457 protein folding, not glycosylation.
- **PN story / NEW pressure:** PN's "N-glycosylation system" framing over-reaches when projected as GO:0006487 for a lectin chaperone. CLGN's real, review-captured roles (folding chaperone, single fertilization GO:0007338) are already in GOA/review. GO:0006487 is verified real but is the WRONG process for this gene's mechanism → over-reaches; do not ADD to the gene.
- **Mapping strategy:** The `[group]` projection is the problem. GO:0006487 is broader/orthogonal to what lectin chaperones do; it is analogous to the TOMM20/HSPA8/RAB7A "broader, rejected" precedent — the node groups the N-glycosylation machinery but its members (OST subunits vs lectin chaperones) do not share GO:0006487. Recommend the group either map to a glycoprotein-QC/folding term (e.g. a chaperone-mediated folding concept) or leave lectin-chaperone members unmapped at this node, so GO:0006487 is not propagated to CLGN.
- **Evidence alignment:** PN listed no reference titles for this row. Review anchors on PMID:9177349 (knockout/zona-adhesion), PMID:17507649 (PDILT complex), PMID:9434179 (cloning). No conflict; the divergence is term choice, not evidence.
- **Verdict:** Identity consistent, but PN GO:0006487 projection **over-reaches** for a lectin chaperone (binds, not synthesizes, N-glycans); should not propagate to CLGN.

**Recommended edits:** [MAP] Do not propagate GO:0006487 from `N-glycosylation system` to lectin-chaperone members (CLGN); remap the group to a folding/glycoprotein-QC term or leave lectin chaperones unmapped. [YAML] No glycosylation annotation should be added to CLGN.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CLGN/CLGN-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: O14967
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
