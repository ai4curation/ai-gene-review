# ATG2B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96BY7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1377)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATG2B/ATG2B-ai-review.yaml](ATG2B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATG2B/ATG2B-ai-review.html](ATG2B-ai-review.html)
- Gene notes: present - [genes/human/ATG2B/ATG2B-notes.md](ATG2B-notes.md)
- GOA TSV: present - [genes/human/ATG2B/ATG2B-goa.tsv](ATG2B-goa.tsv)
- UniProt record: present - [genes/human/ATG2B/ATG2B-uniprot.txt](ATG2B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATG2B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATG2B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATG2B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATG2B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATG2B/ATG2B-deep-research-falcon.md](ATG2B-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATG2B is a large conserved autophagy-related lipid-transfer protein that acts at endoplasmic reticulum-phagophore membrane contact sites during autophagosome biogenesis. It binds membranes and forms an ATG2-WIPI/ATG18 complex with WDR45/WIPI4, which promotes ATG2B recruitment to PI3P-containing autophagic membranes and stimulates lipid-transfer activity. Mammalian ATG2 proteins are also associated with lipid droplets and affect lipid droplet morphology and dispersion, but the best-supported core role of ATG2B is membrane tethering and lipid transfer for phagophore expansion.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 5; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research/notes, review YAML, PN annotation, and PN-node mapping all converge on ATG2B as a WDR45/WIPI4-associated lipid-transfer/membrane-tethering protein of the ATG2-WIPI complex. The review explicitly adds GO:0062079 as a NEW annotation, citing it as "the conservative way to use the PN projection." No contradictions.
- **PN story / NEW pressure:** PN asserts ATG2-WIPI complex membership not previously in GOA. This is a real term, directly supported by ATG2B-WDR45 structural/biochemical evidence (PMID:28820312, 20562859). Review correctly ADDED it (action: NEW, part_of, IDA). Core molecular function (GO:0120013 lipid transfer activity) and process (autophagosome assembly via MODIFY of GO:0006914) are independently captured. Verdict: PN story is correctly captured/ADDED — well-aligned, no over-reach.
- **Evidence alignment:** Strong overlap. PN cites Mizushima reviews plus the ATG2A-WIPI4/PNAS structural work and the lipid-droplet paper (PMID:22219374); review uses the same PMID:22219374 plus PMID:28820312 (ATG2B-WDR45 architecture) and PMID:31721365 (ATG2B lipid transfer) for the complex/MF claims. Convergent evidence base.
- **Verdict:** Consistent; PN ATG2-ATG18 complex projection correctly ADDED as NEW. No edits required.

## Full Consistency Review

- **UniProt:** Q96BY7 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ATG2-WIPI complex component` ; **PN-node mapping:** type-leaf `mapped`, `ok_for_propagation_to_go` → GO:0062079 ATG2-ATG18 complex (verified real, OLS); goa_status=more_specific_than_existing_goa.
- **Consistency:** Fully consistent. Deep research/notes, review YAML, PN annotation, and PN-node mapping all converge on ATG2B as a WDR45/WIPI4-associated lipid-transfer/membrane-tethering protein of the ATG2-WIPI complex. The review explicitly adds GO:0062079 as a NEW annotation, citing it as "the conservative way to use the PN projection." No contradictions.
- **PN story / NEW pressure:** PN asserts ATG2-WIPI complex membership not previously in GOA. This is a real term, directly supported by ATG2B-WDR45 structural/biochemical evidence (PMID:28820312, 20562859). Review correctly ADDED it (action: NEW, part_of, IDA). Core molecular function (GO:0120013 lipid transfer activity) and process (autophagosome assembly via MODIFY of GO:0006914) are independently captured. Verdict: PN story is correctly captured/ADDED — well-aligned, no over-reach.
- **Mapping strategy:** Gene supports the existing node mapping rather than changing it; projected component term is narrower than (and complementary to) the review's MF/BP terms — an appropriate complex-membership refinement, not a broad over-propagation.
- **Evidence alignment:** Strong overlap. PN cites Mizushima reviews plus the ATG2A-WIPI4/PNAS structural work and the lipid-droplet paper (PMID:22219374); review uses the same PMID:22219374 plus PMID:28820312 (ATG2B-WDR45 architecture) and PMID:31721365 (ATG2B lipid transfer) for the complex/MF claims. Convergent evidence base.
- **Verdict:** Consistent; PN ATG2-ATG18 complex projection correctly ADDED as NEW. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATG2B/ATG2B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Regulation of autophagophore membrane composition | ATG2-WIPI complex component
- UniProt: Q96BY7
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
