# ADRB2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P07550
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1339)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ADRB2/ADRB2-ai-review.yaml](ADRB2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ADRB2/ADRB2-ai-review.html](ADRB2-ai-review.html)
- Gene notes: present - [genes/human/ADRB2/ADRB2-notes.md](ADRB2-notes.md)
- GOA TSV: present - [genes/human/ADRB2/ADRB2-goa.tsv](ADRB2-goa.tsv)
- UniProt record: present - [genes/human/ADRB2/ADRB2-uniprot.txt](ADRB2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ADRB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ADRB2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ADRB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ADRB2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ADRB2/ADRB2-deep-research-falcon.md](ADRB2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ADRB2 encodes the beta-2 adrenergic receptor, a seven-transmembrane catecholamine GPCR that acts mainly at the plasma membrane. Epinephrine and norepinephrine binding activate bifurcated G protein signaling, especially Gs/cAMP/PKA and context-dependent Gi branches, with downstream effects on MAPK signaling, smooth-muscle and cardiovascular physiology, thermogenesis, and adipocyte lipolysis. Activated receptors are regulated by arrestin- and ubiquitin-dependent endocytosis, recycling, lysosomal sorting, and Golgi-associated palmitoylation-dependent trafficking. Beyond terminating signaling, internalized beta-arrestin-bound receptors can sustain G protein signaling from endosomes, so receptor output is shaped by subcellular location as well as ligand.
- Existing/core annotation action counts: ACCEPT: 56; KEEP_AS_NON_CORE: 38; MARK_AS_OVER_ANNOTATED: 26; MODIFY: 9

## PN Consistency Summary

- **Consistency:** **CONTRADICTION (PN projection rejected by review).** PN node label itself says "Upstream lipophagy **signaling**," yet the type-node projects direct **GO:0061724 lipophagy**. The review, notes, and Falcon deep research all agree ADRB2 is the **beta-2 adrenergic GPCR** acting as an **upstream signal** for adipocyte lipophagy; the direct lipid-droplet/autolysosome machinery in the source paper is **RAB7**, not ADRB2 (PMID:23708524). The review keeps existing GO:1904504 positive regulation of lipophagy (IDA, in GOA) and declines direct lipophagy.
- **PN story / NEW pressure:** PN pressures a direct-process term (GO:0061724, OLS-verified real) onto an upstream signaling gene. The regulatory role is **already captured** in GOA (GO:1904504 positive regulation of lipophagy + GO:1905168 positive regulation of autophagosome maturation, both KEEP_AS_NON_CORE). No NEW direct term is defensible; the core function is GPCR/catecholamine signaling. Conclusion: PN over-reaches (regulation→direct process upgrade); already captured at the regulation level.
- **Evidence alignment:** PN reference (the tandfonline RAB7/autolysosomal-lipid-degradation article = PMID:23708524) is the **same paper** the review uses — and that paper's own data assign the direct machinery to RAB7, supporting the review's downgrade. No citation divergence; interpretation diverges (direct vs upstream).
- **Verdict:** PN direct-lipophagy projection over-reaches; review correctly retains positive-regulation-of-lipophagy and declines GO:0061724 (RAB7 is the direct factor). **Recommended edits:** [MAP] Keep ADRB2 mapping at GO:1904504 positive regulation of lipophagy; do not propagate direct GO:0061724 lipophagy.

## Full Consistency Review

- **UniProt:** P07550 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy|Upstream lipophagy signaling` ; **PN-node mapping:** type `Lipophagy`=mapped→**GO:0061724 lipophagy** (scope=ok_for_propagation; goa_status=supported_by_goa_regulation); group/class/branch=no_mapping; subtype `Upstream lipophagy signaling`=no_mapping.
- **Consistency:** **CONTRADICTION (PN projection rejected by review).** PN node label itself says "Upstream lipophagy **signaling**," yet the type-node projects direct **GO:0061724 lipophagy**. The review, notes, and Falcon deep research all agree ADRB2 is the **beta-2 adrenergic GPCR** acting as an **upstream signal** for adipocyte lipophagy; the direct lipid-droplet/autolysosome machinery in the source paper is **RAB7**, not ADRB2 (PMID:23708524). The review keeps existing GO:1904504 positive regulation of lipophagy (IDA, in GOA) and declines direct lipophagy.
- **PN story / NEW pressure:** PN pressures a direct-process term (GO:0061724, OLS-verified real) onto an upstream signaling gene. The regulatory role is **already captured** in GOA (GO:1904504 positive regulation of lipophagy + GO:1905168 positive regulation of autophagosome maturation, both KEEP_AS_NON_CORE). No NEW direct term is defensible; the core function is GPCR/catecholamine signaling. Conclusion: PN over-reaches (regulation→direct process upgrade); already captured at the regulation level.
- **Mapping strategy:** Direct precedent of **TOMM20/HSPA8/RAB7A rejected as broader/mis-leveled.** Here the PN-projected GO:0061724 is mis-leveled in the opposite direction — it asserts the direct process for a gene that only regulates it upstream. GO:0061724 should **not** propagate to ADRB2; the safe target is the regulation term already in GOA. The review even flags this as an open question (line ~2522: "Should PN projection for ADRB2 remain at GO:1904504 ... rather than direct GO:0061724").
- **Evidence alignment:** PN reference (the tandfonline RAB7/autolysosomal-lipid-degradation article = PMID:23708524) is the **same paper** the review uses — and that paper's own data assign the direct machinery to RAB7, supporting the review's downgrade. No citation divergence; interpretation diverges (direct vs upstream).
- **Verdict:** PN direct-lipophagy projection over-reaches; review correctly retains positive-regulation-of-lipophagy and declines GO:0061724 (RAB7 is the direct factor). **Recommended edits:** [MAP] Keep ADRB2 mapping at GO:1904504 positive regulation of lipophagy; do not propagate direct GO:0061724 lipophagy.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ADRB2/ADRB2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Lipophagy | Upstream lipophagy signaling
- UniProt: P07550
- In branches: ALP
- Notes: Mediates beta-adrenergic receptor-stimulated lipophagy which decreases following inhibition of autophagy
- PN references (titles):
    - Full article: β-adrenergic receptor-stimulated lipolysis requires the RAB7-mediated autolysosomal lipid degradation (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy|Upstream lipophagy signaling
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061724 lipophagy]
        rationale: This PN type denotes factors that mark lipid cargo for selective autophagy. The category is narrower than the full lipophagy process, so propagation scope is the correct fit.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0061724 lipophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
