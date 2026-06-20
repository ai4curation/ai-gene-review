# ATG2A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q2TAZ0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1375)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATG2A/ATG2A-ai-review.yaml](ATG2A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATG2A/ATG2A-ai-review.html](ATG2A-ai-review.html)
- Gene notes: present - [genes/human/ATG2A/ATG2A-notes.md](ATG2A-notes.md)
- GOA TSV: present - [genes/human/ATG2A/ATG2A-goa.tsv](ATG2A-goa.tsv)
- UniProt record: present - [genes/human/ATG2A/ATG2A-uniprot.txt](ATG2A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATG2A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATG2A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATG2A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATG2A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATG2A/ATG2A-deep-research-falcon.md](ATG2A-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATG2A is a large autophagy-related lipid transfer protein that acts at ER-phagophore contact sites during autophagosome biogenesis. It forms functional assemblies with WIPI/Atg18-family PI3P effectors and ATG9A-containing membranes, tethers membrane compartments, and transfers glycerophospholipids to support phagophore expansion. ATG2A also associates with lipid droplets and ER-mitochondria contact sites, but its principal characterized role is membrane supply for autophagosome formation.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 6; MODIFY: 9; NEW: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research, notes, review YAML agree ATG2A is a rod-like bulk lipid-transfer/tethering protein bridging ER and phagophore, partnered with WIPI4/ATG18 and coupled to ATG9A scramblase. PN component placement (ATG2-WIPI complex) matches exactly. Review core = GO:0120013 lipid transfer + GO:0043495 protein-membrane adaptor → GO:0000045 autophagosome assembly.
- **PN story / NEW pressure:** PN projects GO:0062079 (ATG2-ATG18 complex), absent from GOA (more_specific_than_existing_goa). The review **accepted it as NEW (IDA)** — well-supported by ATG2A-WIPI4 evidence (PMID:31271352). Term verified real. **Conclude: ADD, already done in-review.** This is the well-behaved case: PN projects a MORE specific component term than existing GOA, and the review adopted it. No over-reach.
- **Evidence alignment:** PN reference titles (ATG2A-WIPI4 complex structure, ATG2 essential for autophagosome formation, lipid-droplet/early-autophagosome targeting) overlap the review's lipid-transfer core (PMID:30952800, PMID:31271352) and lipid-droplet non-core. PN refs are titles-only (not all PMIDs in review) but biologically concordant; no conflicts.
- **Verdict:** Consistent and well-supported; PN GO:0062079 correctly added as NEW. Exemplary specific-component projection. No edits warranted.

## Full Consistency Review

- **UniProt:** Q2TAZ0 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE (Falcon DR present)
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component` ; **PN-node mapping:** type(ATG2-WIPI component)=mapped/ok GO:0062079 (ATG2-ATG18 complex, more_specific_than_existing_goa); group/branch=no_mapping; class=context_only GO:0016236 (macroautophagy). PN Notes: lipid transporter carrying phospholipids to phagophore, recruits ATG9. 5 reference titles (Atg2A-WIPI4 structure, lipid-droplet targeting, autophagosome biogenesis reviews).
- **Consistency:** Fully consistent. Deep research, notes, review YAML agree ATG2A is a rod-like bulk lipid-transfer/tethering protein bridging ER and phagophore, partnered with WIPI4/ATG18 and coupled to ATG9A scramblase. PN component placement (ATG2-WIPI complex) matches exactly. Review core = GO:0120013 lipid transfer + GO:0043495 protein-membrane adaptor → GO:0000045 autophagosome assembly.
- **PN story / NEW pressure:** PN projects GO:0062079 (ATG2-ATG18 complex), absent from GOA (more_specific_than_existing_goa). The review **accepted it as NEW (IDA)** — well-supported by ATG2A-WIPI4 evidence (PMID:31271352). Term verified real. **Conclude: ADD, already done in-review.** This is the well-behaved case: PN projects a MORE specific component term than existing GOA, and the review adopted it. No over-reach.
- **Mapping strategy:** ATG2A is a clean driver for the ATG2-WIPI component node; the type→GO:0062079 mapping is appropriately specific (more specific than existing GOA, opposite of the TOMM20/RAB7A "too broad" rejections). The notes correctly resisted broadening cargo-specific process terms (mitophagy/pexophagy/glycophagy IBA rows MODIFY'd toward general autophagosome assembly) and kept class-level macroautophagy as context_only. Sound strategy.
- **Evidence alignment:** PN reference titles (ATG2A-WIPI4 complex structure, ATG2 essential for autophagosome formation, lipid-droplet/early-autophagosome targeting) overlap the review's lipid-transfer core (PMID:30952800, PMID:31271352) and lipid-droplet non-core. PN refs are titles-only (not all PMIDs in review) but biologically concordant; no conflicts.
- **Verdict:** Consistent and well-supported; PN GO:0062079 correctly added as NEW. Exemplary specific-component projection. No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATG2A/ATG2A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Regulation of autophagophore membrane composition | ATG2-WIPI complex component
- UniProt: Q2TAZ0
- In branches: ALP
- Notes: Component of ATG2-WIPI complex, which recruits ATG9 to the autophagosome. ATG2A and ATG2B are lipid transporters, carry phospholipids to the phagophore
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Insights into autophagosome biogenesis from structural and biochemical analyses of the ATG2A-WIPI4 complex | PNAS
    - Mammalian Atg2 proteins are essential for autophagosome formation and important for regulation of size and distribution of lipid droplets | Molecular Biology of the Cell (molbiolcell.org)
    - Lipid droplet and early autophagosomal membrane targeting of Atg2A and Atg14L in human tumor cells[S] - Journal of Lipid Research (jlr.org)
    - Autophagosome biogenesis comes out of the black box | Nature Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0062079 ATG2-ATG18 complex]
        rationale: This PN component bucket corresponds to the ATG2-WIPI/ATG18 lipid-transfer complex used during autophagophore membrane expansion. The GO ATG2-ATG18 complex term is the closest component-level target.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0062079 ATG2-ATG18 complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
