# CHIC2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKJ5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHIC2/CHIC2-ai-review.yaml](CHIC2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHIC2/CHIC2-ai-review.html](CHIC2-ai-review.html)
- Gene notes: present - [genes/human/CHIC2/CHIC2-notes.md](CHIC2-notes.md)
- GOA TSV: present - [genes/human/CHIC2/CHIC2-goa.tsv](CHIC2-goa.tsv)
- UniProt record: present - [genes/human/CHIC2/CHIC2-uniprot.txt](CHIC2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHIC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHIC2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHIC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHIC2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHIC2 (Cysteine-rich hydrophobic domain-containing protein 2; also known as BTL) is a small (165 aa, ~19 kDa) palmitoylated, membrane-associated protein and the defining member of the CHIC family. It contains a single cysteine-rich hydrophobic (CHIC) motif (residues 88-106); palmitoylation within this motif is required for membrane association, and mutation of the cysteine cluster abolishes both palmitoylation and membrane binding. The protein localizes to the plasma membrane and to cytoplasmic vesicles, including a Golgi-like vesicular compartment and scattered vesicles, consistent with a role in membrane-associated vesicle trafficking and secretion. Its N-terminus is an acidic predicted coiled-coil region. The specific molecular function of CHIC2 is not experimentally established. The CHIC2 locus lies at chromosome 4q12 and is recurrently deleted by the cryptic interstitial deletion that fuses FIP1L1 to PDGFRA in hypereosinophilic syndrome/chronic eosinophilic leukemia, where CHIC2 deletion serves as a diagnostic FISH marker; a separate t(4;12)(q12;p13) translocation fuses CHIC2 (BTL) to ETV6 in a form of acute myeloid leukemia.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 5

## PN Consistency Summary

- **Consistency:** PARTIAL CONFLICT. The review (and notes) state CHIC2's molecular function is undefined and frame it purely as a palmitoylated membrane/vesicle protein; it makes NO mention of STUB1 or an E3-ligase-complex role. The PN annotation rests on PMID:40796662, which is NOT cited in the review. Per PubMed, PMID:40796662 (Nat Immunol 2025, [DOI](https://doi.org/10.1038/s41590-025-02231-6)) establishes a real STUB1-CHIC2 complex in which CHIC2 is the non-catalytic **adapter** for the E3 ligase STUB1 regulating cytokine-receptor levels in CD8 T cells. So the PN is built on a genuine 2025 finding the review predates/misses.
- **PN story / NEW pressure:** PN asserts a role (member of an E3 ligase complex via STUB1) absent from existing GO and from the review. GO:0000151 "ubiquitin ligase complex" verified real (OLS) and confirmed new_to_goa (CHIC2-goa.tsv has only localization + bare protein-binding). This is a defensible **ADD** as part_of GO:0000151, supported by PMID:40796662. CHIC2 is non-catalytic, so the group-level complex-membership mapping (rather than ligase activity) is the correct, conservative target.
- **Evidence alignment:** No overlap. PN cites PMID:40796662 (the defining STUB1-CHIC2 paper); the review cites only HT-interactome PMIDs (16189514, 19060904, 25416956, 30886144, 32296183, all MARK_AS_OVER_ANNOTATED) plus PMID:11257495 (palmitoylation). The PN reference is the more functionally informative one and is missing from the review.
- **Verdict:** UNDER-CAPTURED by review — PN ADD is justified. **Recommended edits:** [YAML] add PMID:40796662 to references and add a NEW/proposed annotation GO:0000151 (part_of, "STUB1-CHIC2 complex") and an adapter/molecular-function note; [REF] flag that the review's "function undefined" framing is now superseded by the STUB1-CHIC2 adapter finding.

## Full Consistency Review

- **UniProt:** Q9UKJ5 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex|noncatalytic` ; **PN-node mapping:** group (idiosyncratic UBOX complex)→GO:0000151 ubiquitin ligase complex (new_to_goa). Subtype/type/branch = no_mapping; class context_only.
- **Consistency:** PARTIAL CONFLICT. The review (and notes) state CHIC2's molecular function is undefined and frame it purely as a palmitoylated membrane/vesicle protein; it makes NO mention of STUB1 or an E3-ligase-complex role. The PN annotation rests on PMID:40796662, which is NOT cited in the review. Per PubMed, PMID:40796662 (Nat Immunol 2025, [DOI](https://doi.org/10.1038/s41590-025-02231-6)) establishes a real STUB1-CHIC2 complex in which CHIC2 is the non-catalytic **adapter** for the E3 ligase STUB1 regulating cytokine-receptor levels in CD8 T cells. So the PN is built on a genuine 2025 finding the review predates/misses.
- **PN story / NEW pressure:** PN asserts a role (member of an E3 ligase complex via STUB1) absent from existing GO and from the review. GO:0000151 "ubiquitin ligase complex" verified real (OLS) and confirmed new_to_goa (CHIC2-goa.tsv has only localization + bare protein-binding). This is a defensible **ADD** as part_of GO:0000151, supported by PMID:40796662. CHIC2 is non-catalytic, so the group-level complex-membership mapping (rather than ligase activity) is the correct, conservative target.
- **Mapping strategy:** Mapping is sound and well-judged: assigns complex membership (GO:0000151) not catalytic activity to a non-catalytic adapter; holds the E3 class context_only to avoid over-propagation. No change needed to the node.
- **Evidence alignment:** No overlap. PN cites PMID:40796662 (the defining STUB1-CHIC2 paper); the review cites only HT-interactome PMIDs (16189514, 19060904, 25416956, 30886144, 32296183, all MARK_AS_OVER_ANNOTATED) plus PMID:11257495 (palmitoylation). The PN reference is the more functionally informative one and is missing from the review.
- **Verdict:** UNDER-CAPTURED by review — PN ADD is justified. **Recommended edits:** [YAML] add PMID:40796662 to references and add a NEW/proposed annotation GO:0000151 (part_of, "STUB1-CHIC2 complex") and an adapter/molecular-function note; [REF] flag that the review's "function undefined" framing is now superseded by the STUB1-CHIC2 adapter finding.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CHIC2/CHIC2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic UBOX complex | STUB1/CHIC2 complex | noncatalytic
- UniProt: Q9UKJ5
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: (none)
- PN references (titles):
    - 40796662
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex|noncatalytic
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
