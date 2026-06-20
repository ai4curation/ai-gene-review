# BAG2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O95816
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/BAG2/BAG2-ai-review.yaml](BAG2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BAG2/BAG2-ai-review.html](BAG2-ai-review.html)
- Gene notes: present - [genes/human/BAG2/BAG2-notes.md](BAG2-notes.md)
- GOA TSV: present - [genes/human/BAG2/BAG2-goa.tsv](BAG2-goa.tsv)
- UniProt record: present - [genes/human/BAG2/BAG2-uniprot.txt](BAG2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/BAG2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/BAG2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BAG2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BAG2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/BAG2/BAG2-deep-research-falcon.md](BAG2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BAG2 (BAG family molecular chaperone regulator 2) is a cytosolic co-chaperone of the HSP70/HSC70 molecular chaperone system. Through its C-terminal BAG domain it binds the ATPase (nucleotide-binding) domain of HSP70/HSC70 and acts as a nucleotide-exchange factor (NEF), promoting ADP release and consequent release of bound client/substrate proteins, thereby regulating the HSP70 chaperone cycle. BAG2 is a major component of complexes containing the chaperone-associated E3 ubiquitin ligase CHIP (STUB1) and inhibits CHIP ligase activity by disrupting cooperation between CHIP and its E2 enzyme, so that BAG2 reduces ubiquitination of chaperone clients and shifts protein triage away from degradation toward folding/maturation and stabilization. In neurons, the BAG2/HSP70 complex is tethered to microtubules and captures misfolded, phosphorylated, detergent-insoluble tau, delivering it for ubiquitin-independent proteasomal degradation. BAG2 also binds and stabilizes specific clients (e.g., CFTR, PINK1, polyglutamine-expanded ataxin-3) by lowering their ubiquitination. Unlike BAG1, BAG2 lacks a ubiquitin-like domain. Its core roles are HSP70 nucleotide exchange, chaperone-assisted protein quality control, and negative regulation of CHIP-dependent client ubiquitination.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 17; MARK_AS_OVER_ANNOTATED: 24; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Row 1 fully consistent. Review, notes and Falcon deep research converge on BAG2 as an HSP70/HSC70 nucleotide-exchange factor (BAG domain) that inhibits CHIP/STUB1 E3 ligase and stabilizes clients (PMID:24318877, 16207813, 24383081, 25006867). GO:0000774 is the accepted core MF (verified real) and is ACCEPT in the review. Row 2 (proteasome adaptor → proteasome binding) is NOT supported: BAG2 acts on HSP70 and on the E3 CHIP, not on the 26S proteasome; neither review nor deep research reports direct proteasome binding. The tau pathway delivers tau "to the proteasome" but via HSP70, not by BAG2 binding the proteasome.
- **PN story / NEW pressure:** Row 1 already captured (GO:0000774 ACCEPT). Row 2 GO:0070628 proteasome binding (verified real term) is flagged new_to_goa, but it is an over-reach for BAG2 — no evidence BAG2 directly binds the proteasome. The better-supported UPS-side functions (ubiquitin protein ligase binding GO:0031625, negative regulation of ubiquitination GO:0031397) are already ACCEPT in the review. Conclusion: row 1 already captured; row 2 proteasome-binding projection over-reaches.
- **Evidence alignment:** PN cites no row-level references. Review/deep-research PMIDs (Arndt 2005=PMID:16207813, 24318877, 19228967, 24383081, 25006867) all concern HSP70/CHIP/client biology, none proteasome binding — divergent from the row-2 projection.
- **Verdict:** NEF classification sound and already captured; the UPS "adaptor → proteasome binding" projection is unsupported for BAG2. **Recommended edits:** [MAP] do not project GO:0070628 proteasome binding onto O95816 (BAG2 binds HSP70 and CHIP, not the proteasome); its UPS role is already covered by GO:0031625 / GO:0031397 in the review.

## Full Consistency Review

- **UniProt:** O95816 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE
- **PN placement:** two rows — `Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor|BAG domain subtype` and `Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|BAG` ; **PN-node mapping:** NEF type → mapped/ok GO:0000774 (already_in_goa_exact); UPS adaptors group → mapped/ok GO:0070628 proteasome binding (new_to_goa); proteasome class → context_only/too_broad GO:0000502.
- **Consistency:** Row 1 fully consistent. Review, notes and Falcon deep research converge on BAG2 as an HSP70/HSC70 nucleotide-exchange factor (BAG domain) that inhibits CHIP/STUB1 E3 ligase and stabilizes clients (PMID:24318877, 16207813, 24383081, 25006867). GO:0000774 is the accepted core MF (verified real) and is ACCEPT in the review. Row 2 (proteasome adaptor → proteasome binding) is NOT supported: BAG2 acts on HSP70 and on the E3 CHIP, not on the 26S proteasome; neither review nor deep research reports direct proteasome binding. The tau pathway delivers tau "to the proteasome" but via HSP70, not by BAG2 binding the proteasome.
- **PN story / NEW pressure:** Row 1 already captured (GO:0000774 ACCEPT). Row 2 GO:0070628 proteasome binding (verified real term) is flagged new_to_goa, but it is an over-reach for BAG2 — no evidence BAG2 directly binds the proteasome. The better-supported UPS-side functions (ubiquitin protein ligase binding GO:0031625, negative regulation of ubiquitination GO:0031397) are already ACCEPT in the review. Conclusion: row 1 already captured; row 2 proteasome-binding projection over-reaches.
- **Mapping strategy:** Row-1 NEF mapping needs no change (exact match). Row-2 "proteasome binding" should NOT project onto BAG2; if the adaptors group genuinely shares proteasome binding, BAG2 is the exception (it is a chaperone/E3-adaptor, not a proteasome shuttle like the UBL-UBA family).
- **Evidence alignment:** PN cites no row-level references. Review/deep-research PMIDs (Arndt 2005=PMID:16207813, 24318877, 19228967, 24383081, 25006867) all concern HSP70/CHIP/client biology, none proteasome binding — divergent from the row-2 projection.
- **Verdict:** NEF classification sound and already captured; the UPS "adaptor → proteasome binding" projection is unsupported for BAG2. **Recommended edits:** [MAP] do not project GO:0070628 proteasome binding onto O95816 (BAG2 binds HSP70 and CHIP, not the proteasome); its UPS role is already covered by GO:0031625 / GO:0031397 in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/BAG2/BAG2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | HSP70 nucleotide exchange factor | BAG domain subtype
- UniProt: O95816
- In branches: CY, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor|BAG domain subtype
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000774 adenyl-nucleotide exchange factor activity]
        rationale: These PN entries denote nucleotide exchange factors that reset HSP70 chaperones by promoting ADP release. The current validated GO cache does not expose a more HSP70-specific exchange-factor term, so adenyl-nucleotide exchange factor activity is the best supported target.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Ubiquitin Proteasome System | Proteasome and associated proteins | adaptors | BAG
- UniProt: O95816
- In branches: CY, UPS
- Signature domains: IPR037689
- Auxiliary domains: IPR003103, IPR037689
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|BAG
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070628 proteasome binding]
        rationale: This PN group captures proteasome adaptors and shuttle factors. Proteasome binding is the safe shared molecular-function target.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000774 adenyl-nucleotide exchange factor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70 nucleotide exchange factor
- GO:0070628 proteasome binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
