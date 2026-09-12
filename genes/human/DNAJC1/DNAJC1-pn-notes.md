# DNAJC1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96KC8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC1/DNAJC1-ai-review.yaml](DNAJC1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC1/DNAJC1-ai-review.html](DNAJC1-ai-review.html)
- Gene notes: present - [genes/human/DNAJC1/DNAJC1-notes.md](DNAJC1-notes.md)
- GOA TSV: present - [genes/human/DNAJC1/DNAJC1-goa.tsv](DNAJC1-goa.tsv)
- UniProt record: present - [genes/human/DNAJC1/DNAJC1-uniprot.txt](DNAJC1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC1 (MTJ1/ERdj1, human homolog HTJ1) is a single-pass type I endoplasmic reticulum (and nuclear/microsomal) membrane protein of the DNAJC subfamily of J-domain co-chaperones. Its N-terminal J domain faces the ER lumen and stimulates the ATPase activity of the ER HSP70 chaperone BiP (HSPA5), while its large cytosolic C-terminal region associates with ribosomes and modulates protein synthesis, and contains two SANT (Myb-like) domains. Through its second SANT domain it binds the serpin SERPINA3/alpha-1-antichymotrypsin and the inter-alpha-trypsin inhibitor heavy chain ITIH4, modulating their protease-inhibitory/processing behavior. DNAJC1 thereby couples the ER-membrane BiP chaperone system to translation and to regulation of secreted protease/protease-inhibitor activity.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent on the chaperone axis. Notes/YAML describe a single-pass type-I ER-membrane J-protein whose lumenal J domain stimulates BiP/HSPA5 ATPase (GO:0001671 TAS PMID:14668352, ACCEPT/core) and binds BiP (GO:0051087 IEA, ACCEPT). PN "J-domain HSP70 cochaperone" type fits. The review adds two non-chaperone facets PN does not capture (ribosome-associated translation modulation; SANT2-mediated serpin/protease regulation — GO:0045861, GO:0050708) — these are extra, not contradictory.
- **PN story / NEW pressure:** PN's HSP70-binding claim is captured (GO:0001671 ATPase activator + GO:0051087 chaperone binding, both ACCEPT/core). PN-projected GO:0030544 (verified real) is narrower than GO:0051087 — defensible specialization since DNAJC1 has TAS evidence its J domain stimulates BiP. No NEW GO term needed for proteostasis. Verdict: already captured.
- **Evidence alignment:** Core PMID:14668352 (J-domain→BiP ATPase; SANT2-serpin) and PMID:16271702 (ITIH4) carry the function; PN supplies path context. No conflict; review's many HT-interactome PMIDs (CFTR, RMND1, etc.) are non-core and absent from PN.
- **Verdict:** CONSISTENT — GO:0030544 a sound narrower specialization of the verified J-domain→BiP ATPase-stimulating MF; node mapping correct.

## Full Consistency Review

- **UniProt:** Q96KC8 (MTJ1/ERdj1/HTJ1) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (parents no_mapping)
- **Consistency:** Consistent on the chaperone axis. Notes/YAML describe a single-pass type-I ER-membrane J-protein whose lumenal J domain stimulates BiP/HSPA5 ATPase (GO:0001671 TAS PMID:14668352, ACCEPT/core) and binds BiP (GO:0051087 IEA, ACCEPT). PN "J-domain HSP70 cochaperone" type fits. The review adds two non-chaperone facets PN does not capture (ribosome-associated translation modulation; SANT2-mediated serpin/protease regulation — GO:0045861, GO:0050708) — these are extra, not contradictory.
- **PN story / NEW pressure:** PN's HSP70-binding claim is captured (GO:0001671 ATPase activator + GO:0051087 chaperone binding, both ACCEPT/core). PN-projected GO:0030544 (verified real) is narrower than GO:0051087 — defensible specialization since DNAJC1 has TAS evidence its J domain stimulates BiP. No NEW GO term needed for proteostasis. Verdict: already captured.
- **Mapping strategy:** GO:0030544 mapping is appropriate and does not over-reach — DNAJC1 has direct (TAS) BiP-ATPase-stimulation evidence, a genuine HSP70-cochaperone MF (not an over-broad holdase/unfolded-protein-binding claim). Note the partner is ER HSP70 BiP, consistent with "Hsp70 protein binding."
- **Evidence alignment:** Core PMID:14668352 (J-domain→BiP ATPase; SANT2-serpin) and PMID:16271702 (ITIH4) carry the function; PN supplies path context. No conflict; review's many HT-interactome PMIDs (CFTR, RMND1, etc.) are non-core and absent from PN.
- **Verdict:** CONSISTENT — GO:0030544 a sound narrower specialization of the verified J-domain→BiP ATPase-stimulating MF; node mapping correct.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC1/DNAJC1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q96KC8
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
