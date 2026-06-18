# DNAJC12 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKB3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC12/DNAJC12-ai-review.yaml](DNAJC12-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC12/DNAJC12-ai-review.html](DNAJC12-ai-review.html)
- Gene notes: present - [genes/human/DNAJC12/DNAJC12-notes.md](DNAJC12-notes.md)
- GOA TSV: present - [genes/human/DNAJC12/DNAJC12-goa.tsv](DNAJC12-goa.tsv)
- UniProt record: present - [genes/human/DNAJC12/DNAJC12-uniprot.txt](DNAJC12-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC12.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC12.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC12 (also called JDP1) is a small cytosolic "J domain-only" co-chaperone of the DnaJ/Hsp40 (DNAJC) family, consisting of an N-terminal J domain (with the conserved HPD motif) and a C-terminal intrinsically disordered region. As a co-chaperone of the HSP70 family, it binds the cognate Hsp70 chaperone Hsc70 (HSPA8) and, through its J domain, stimulates HSP70 ATPase activity. DNAJC12 is a dedicated chaperone for the biopterin (BH4)-dependent aromatic amino acid hydroxylases, interacting with phenylalanine hydroxylase (PAH), tyrosine hydroxylase (TH) and tryptophan hydroxylases (TPH1, TPH2) and assisting their proper folding and stability. It is diffusely cytoplasmic and is up-regulated by ER stress. Biallelic loss-of-function variants cause autosomal-recessive non-BH4-deficient hyperphenylalaninemia accompanied by dopamine and serotonin deficiency, dystonia/parkinsonism and intellectual disability, a condition treatable with BH4 and neurotransmitter precursors.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 2; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Consistent on the J-domain axis. Review, notes, and PN agree DNAJC12 is a cytosolic J-domain-only HSP70 co-chaperone that binds Hsc70/HSPA8 and stimulates HSP70 ATPase. The review MODIFIES the bare GO:0005515 (HSPA8 interaction, PMID:24122553) to GO:0030544, matching the PN projection exactly. No contradiction. The disease-defining specific-client role (chaperone for aromatic amino acid hydroxylases PAH/TH/TPH; PMID:28132689) is captured in the review's core_functions but is outside the single PN row.
- **PN story / NEW pressure:** GO:0030544 is verified real and is the right target. GOA currently has only GO:0005515 + GO:0005737, so relative to GOA this is effectively `new_to_goa`, not `more_specific_than_existing_goa` as the PN label states (no GO:0031072 parent in GOA) — a minor status-label inaccuracy. The hydroxylase-chaperone biology is the gene's distinctive story but there is no specific "aromatic amino acid hydroxylase binding" GO term; it is appropriately rendered via GO:0051087 (protein-folding chaperone binding) in core_functions. No NEW term warranted.
- **Evidence alignment:** PN row carries no titles; review anchors on PMID:24122553 (Hsc70 binding, verified) and PMID:28132689 (HSP70 cochaperone of hydroxylases, verified). No divergence.
- **Verdict:** Consistent; PN GO:0030544 defensible and already realized in the review. **Recommended edits:** [MAP] (minor) correct DNAJC12 projected `goa_status` from `more_specific_than_existing_goa` to `new_to_goa` (GOA lacks the GO:0031072 parent).

## Full Consistency Review

- **UniProt:** Q9UKB3 (JDP1) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (group/class/branch = no_mapping)
- **Consistency:** Consistent on the J-domain axis. Review, notes, and PN agree DNAJC12 is a cytosolic J-domain-only HSP70 co-chaperone that binds Hsc70/HSPA8 and stimulates HSP70 ATPase. The review MODIFIES the bare GO:0005515 (HSPA8 interaction, PMID:24122553) to GO:0030544, matching the PN projection exactly. No contradiction. The disease-defining specific-client role (chaperone for aromatic amino acid hydroxylases PAH/TH/TPH; PMID:28132689) is captured in the review's core_functions but is outside the single PN row.
- **PN story / NEW pressure:** GO:0030544 is verified real and is the right target. GOA currently has only GO:0005515 + GO:0005737, so relative to GOA this is effectively `new_to_goa`, not `more_specific_than_existing_goa` as the PN label states (no GO:0031072 parent in GOA) — a minor status-label inaccuracy. The hydroxylase-chaperone biology is the gene's distinctive story but there is no specific "aromatic amino acid hydroxylase binding" GO term; it is appropriately rendered via GO:0051087 (protein-folding chaperone binding) in core_functions. No NEW term warranted.
- **Mapping strategy:** Node mapping is appropriate; DNAJC12 is a genuine HSP70 cochaperone and GO:0030544 is a defensible, suitably narrow propagation. The review already realizes it (MODIFY), so propagation would be confirmatory.
- **Evidence alignment:** PN row carries no titles; review anchors on PMID:24122553 (Hsc70 binding, verified) and PMID:28132689 (HSP70 cochaperone of hydroxylases, verified). No divergence.
- **Verdict:** Consistent; PN GO:0030544 defensible and already realized in the review. **Recommended edits:** [MAP] (minor) correct DNAJC12 projected `goa_status` from `more_specific_than_existing_goa` to `new_to_goa` (GOA lacks the GO:0031072 parent).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC12/DNAJC12-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9UKB3
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
