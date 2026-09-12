# DNAJC28 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NX36
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC28/DNAJC28-ai-review.yaml](DNAJC28-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC28/DNAJC28-ai-review.html](DNAJC28-ai-review.html)
- Gene notes: present - [genes/human/DNAJC28/DNAJC28-notes.md](DNAJC28-notes.md)
- GOA TSV: present - [genes/human/DNAJC28/DNAJC28-goa.tsv](DNAJC28-goa.tsv)
- UniProt record: present - [genes/human/DNAJC28/DNAJC28-uniprot.txt](DNAJC28-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC28.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC28.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC28.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC28.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC28 (C21orf55/C21orf78) is a poorly characterized member of the DnaJ/HSP40 (J-domain) co-chaperone family encoded on chromosome 21. It contains a canonical J domain together with a predicted coiled-coil region, and its N-terminus resembles a mitochondrial-targeting presequence, suggesting it may act as a mitochondrial J-domain co-chaperone. By analogy to other J-domain proteins it is presumed to assist HSP70-type chaperones in protein folding, but no substrate, partner chaperone, or cellular process has been experimentally established. It is expressed in brain, testis, uterus, spleen and liver (tissue-enhanced in testis) and is phosphorylated at Thr-347.
- Existing/core annotation action counts: KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** COMPARTMENT MISMATCH. Deep research and review YAML agree DNAJC28 is an essentially uncharacterized J-domain protein whose N-terminus resembles a MITOCHONDRIAL targeting presequence (review/notes predict mitochondrial localization; review core MF GO:0051087 protein-folding chaperone binding). The PN row places it in the **ER proteostasis** branch, which conflicts with the review's mitochondrial prediction. Neither localization is experimentally confirmed, so this is an unresolved discrepancy rather than a proven error, but the branch assignment and the review point in different directions.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real). GOA has only GO:0005515 protein binding (one IPI) + GO:0001659 (IBA, marked over-annotated), so "more_specific_than_existing_goa" is loose; effectively new_to_goa. GO:0030544 is a child of the review's GO:0051087, i.e. a narrower, defensible domain-level ADD — but purely predicted.
- **Evidence alignment:** PN row no titles; review's sole literature ref is PMID:24407287 (PML/ASC inflammasome — source of the single IPI only, relevance LOW, VERIFIED). No experimental HSP70-binding evidence on either side.
- **Verdict:** Consistent on function (uncharacterized J-protein); GO:0030544 defensible inferred ADD. **Recommended edits:** [MAP] change goa_status to new_to_goa; [MAP] reconcile ER vs mitochondrial branch placement (review predicts mitochondrial targeting).

## Full Consistency Review

- **UniProt:** Q9NX36 (C21orf55/C21orf78) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (projected more_specific_than_existing_goa); group/class/branch=no_mapping.
- **Consistency:** COMPARTMENT MISMATCH. Deep research and review YAML agree DNAJC28 is an essentially uncharacterized J-domain protein whose N-terminus resembles a MITOCHONDRIAL targeting presequence (review/notes predict mitochondrial localization; review core MF GO:0051087 protein-folding chaperone binding). The PN row places it in the **ER proteostasis** branch, which conflicts with the review's mitochondrial prediction. Neither localization is experimentally confirmed, so this is an unresolved discrepancy rather than a proven error, but the branch assignment and the review point in different directions.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real). GOA has only GO:0005515 protein binding (one IPI) + GO:0001659 (IBA, marked over-annotated), so "more_specific_than_existing_goa" is loose; effectively new_to_goa. GO:0030544 is a child of the review's GO:0051087, i.e. a narrower, defensible domain-level ADD — but purely predicted.
- **Mapping strategy:** Node status unchanged. Two issues: (1) goa_status should be new_to_goa; (2) the ER-branch placement is questionable given the mitochondrial-presequence prediction — flag for reconciliation. Term direction (narrower than review) is appropriate.
- **Evidence alignment:** PN row no titles; review's sole literature ref is PMID:24407287 (PML/ASC inflammasome — source of the single IPI only, relevance LOW, VERIFIED). No experimental HSP70-binding evidence on either side.
- **Verdict:** Consistent on function (uncharacterized J-protein); GO:0030544 defensible inferred ADD. **Recommended edits:** [MAP] change goa_status to new_to_goa; [MAP] reconcile ER vs mitochondrial branch placement (review predicts mitochondrial targeting).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC28/DNAJC28-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9NX36
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
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
