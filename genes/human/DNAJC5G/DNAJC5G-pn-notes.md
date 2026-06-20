# DNAJC5G PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N7S2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC5G/DNAJC5G-ai-review.yaml](DNAJC5G-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC5G/DNAJC5G-ai-review.html](DNAJC5G-ai-review.html)
- Gene notes: present - [genes/human/DNAJC5G/DNAJC5G-notes.md](DNAJC5G-notes.md)
- GOA TSV: present - [genes/human/DNAJC5G/DNAJC5G-goa.tsv](DNAJC5G-goa.tsv)
- UniProt record: present - [genes/human/DNAJC5G/DNAJC5G-uniprot.txt](DNAJC5G-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC5G.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC5G.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC5G.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC5G.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC5G (cysteine string protein-gamma, CSP-gamma) is a testis-specific, poorly characterized paralog of the synaptic co-chaperone CSPalpha/DNAJC5. It carries an N-terminal J domain characteristic of DnaJ/HSP40 co-chaperones, which in characterized family members recruits and stimulates the HSP70 chaperone HSC70/HSPA8, together with a cysteine-string region that is predicted to be palmitoylated and to anchor the protein to membranes. No direct biochemical characterization of CSP-gamma's activity or clients has been reported; its function is inferred from family membership to be HSP70 co-chaperone activity in a testis secretory/membrane context.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 1

## PN Consistency Summary

- **Consistency:** Consistent on identity, with an MF-term mismatch. Deep research (notes), review and PN agree DNAJC5G/CSP-gamma is a testis-specific, Tdark, completely uncharacterized CSPalpha paralog (J domain aa 17-98), membrane lipid-anchor by similarity, PE2 (transcript-level), PAN-GO 0 annotations. No experimental chaperone data. Mismatch: PN projects GO:0030544 Hsp70 protein binding as the type MF, but the review's core MF is GO:0051082 unfolded protein binding (deliberately cautious family-level call) — GO:0030544 appears nowhere in the review. Same pattern as DNAJC4.
- **PN story / NEW pressure:** PN asserts GO:0030544 (verified real) as new_to_goa — correct that GOA has no chaperone-binding MF (only cytoplasm + membrane IEA). For a J-domain protein this is the canonical co-chaperone MF, defensible **by family**, but entirely unverified experimentally for CSP-gamma. Conclusion: a defensible family-level ADD candidate, but **unverified**; the review chose the equally-family-level GO:0051082 instead.
- **Evidence alignment:** PN carries no row references; review cites only the UniProt file (no PMIDs — no functional literature exists). No overlap, no contradiction.
- **Verdict:** Family-level call sound; GO:0030544 is a defensible-but-unverified ADD; harmonize MF term with the CSP family. **Recommended edits:** [MAP] reconcile the GO:0030544 (PN) vs GO:0051082 (review) MF choice across the CSP paralogs — for consistency with DNAJC5/DNAJC5B, GO:0030544 Hsp70 protein binding is preferable, asserted as predicted/family-level (not experimental).

## Full Consistency Review

- **UniProt:** Q8N7S2 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type → mapped/ok_for_propagation_to_go GO:0030544 Hsp70 protein binding (goa_status=new_to_goa); all ancestor nodes no_mapping.
- **Consistency:** Consistent on identity, with an MF-term mismatch. Deep research (notes), review and PN agree DNAJC5G/CSP-gamma is a testis-specific, Tdark, completely uncharacterized CSPalpha paralog (J domain aa 17-98), membrane lipid-anchor by similarity, PE2 (transcript-level), PAN-GO 0 annotations. No experimental chaperone data. Mismatch: PN projects GO:0030544 Hsp70 protein binding as the type MF, but the review's core MF is GO:0051082 unfolded protein binding (deliberately cautious family-level call) — GO:0030544 appears nowhere in the review. Same pattern as DNAJC4.
- **PN story / NEW pressure:** PN asserts GO:0030544 (verified real) as new_to_goa — correct that GOA has no chaperone-binding MF (only cytoplasm + membrane IEA). For a J-domain protein this is the canonical co-chaperone MF, defensible **by family**, but entirely unverified experimentally for CSP-gamma. Conclusion: a defensible family-level ADD candidate, but **unverified**; the review chose the equally-family-level GO:0051082 instead.
- **Mapping strategy:** Type-level GO:0030544 is appropriate breadth (J-domain co-chaperone), not an over-reach. goa_status=new_to_goa is accurate. The only issue is term-choice harmonization with the sibling paralogs: DNAJC5/DNAJC5B reviews use GO:0030544 as core, whereas DNAJC5G (and DNAJC4) reviews use GO:0051082.
- **Evidence alignment:** PN carries no row references; review cites only the UniProt file (no PMIDs — no functional literature exists). No overlap, no contradiction.
- **Verdict:** Family-level call sound; GO:0030544 is a defensible-but-unverified ADD; harmonize MF term with the CSP family. **Recommended edits:** [MAP] reconcile the GO:0030544 (PN) vs GO:0051082 (review) MF choice across the CSP paralogs — for consistency with DNAJC5/DNAJC5B, GO:0030544 Hsp70 protein binding is preferable, asserted as predicted/family-level (not experimental).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC5G/DNAJC5G-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q8N7S2
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
