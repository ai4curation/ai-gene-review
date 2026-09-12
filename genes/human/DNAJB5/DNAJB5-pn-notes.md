# DNAJB5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75953
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJB5/DNAJB5-ai-review.yaml](DNAJB5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJB5/DNAJB5-ai-review.html](DNAJB5-ai-review.html)
- Gene notes: present - [genes/human/DNAJB5/DNAJB5-notes.md](DNAJB5-notes.md)
- GOA TSV: present - [genes/human/DNAJB5/DNAJB5-goa.tsv](DNAJB5-goa.tsv)
- UniProt record: present - [genes/human/DNAJB5/DNAJB5-uniprot.txt](DNAJB5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJB5 (Hsc40, "heat shock protein cognate 40") is a cytosolic HSP40/J-domain co-chaperone of the DNAJB subfamily and a paralog of DNAJB1 and DNAJB4. Through its N-terminal J domain it is predicted to bind and stimulate the HSP70 chaperone (HSPA1A/HSPA1B/HSPA8), acting as a co-chaperone that delivers client proteins to HSP70 for folding. It is expressed constitutively and further induced by stress, is enriched in skeletal muscle and tongue, and produces several alternatively spliced isoforms. Compared with its better-studied paralogs it remains poorly characterized, with most molecular data derived from family-level inference and high-throughput interaction studies.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 9

## PN Consistency Summary

- **Consistency:** Consistent but note the weaker evidence base. Notes/YAML stress DNAJB5 is poorly characterized: it is a cytosolic class-B J-protein whose HSP70 binding rests on GOA GO:0051087 IPI (PMID:21231916) and family inference, with NO direct ATPase-stimulation data. The review correctly does NOT assert GO:0001671 as core (unlike DNAJB4). PN "J-domain HSP70 cochaperone" type is consistent with the available (family/IPI-level) evidence.
- **PN story / NEW pressure:** PN asserts HSP70 interaction — captured by GO:0051087 (IPI PMID:21231916 + IBA/IEA, ACCEPT/core). PN-projected GO:0030544 (verified real) is a child of GO:0051087, so it is a more-specific refinement, defensible from the same IPI-to-HSP70 evidence. No NEW-term pressure. A possible muscle/titin role (PMID:23414517) is flagged in notes but explicitly not functionally demonstrated — correctly left as non-core. Verdict: already captured.
- **Evidence alignment:** Shared anchor PMID:21231916 (HSP70 machine). Review adds HT-interactome PMIDs (titin, CACNA1A, EBNA-LP) absent from PN; PN adds nothing the review lacks.
- **Verdict:** CONSISTENT — GO:0030544 defensible as narrower than the gene's GO:0051087; correct that no ATPase/holdase MF is asserted for this poorly-characterized member.

## Full Consistency Review

- **UniProt:** O75953 (Hsc40) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch CY) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (parents no_mapping)
- **Consistency:** Consistent but note the weaker evidence base. Notes/YAML stress DNAJB5 is poorly characterized: it is a cytosolic class-B J-protein whose HSP70 binding rests on GOA GO:0051087 IPI (PMID:21231916) and family inference, with NO direct ATPase-stimulation data. The review correctly does NOT assert GO:0001671 as core (unlike DNAJB4). PN "J-domain HSP70 cochaperone" type is consistent with the available (family/IPI-level) evidence.
- **PN story / NEW pressure:** PN asserts HSP70 interaction — captured by GO:0051087 (IPI PMID:21231916 + IBA/IEA, ACCEPT/core). PN-projected GO:0030544 (verified real) is a child of GO:0051087, so it is a more-specific refinement, defensible from the same IPI-to-HSP70 evidence. No NEW-term pressure. A possible muscle/titin role (PMID:23414517) is flagged in notes but explicitly not functionally demonstrated — correctly left as non-core. Verdict: already captured.
- **Mapping strategy:** Mapping to GO:0030544 is appropriate; scope ok_for_propagation given the IPI HSP70 anchor. Because DNAJB5 lacks its own holdase/ATPase data, the type-level (rather than over-broad "unfolded protein binding") mapping is the right altitude — does not over-reach.
- **Evidence alignment:** Shared anchor PMID:21231916 (HSP70 machine). Review adds HT-interactome PMIDs (titin, CACNA1A, EBNA-LP) absent from PN; PN adds nothing the review lacks.
- **Verdict:** CONSISTENT — GO:0030544 defensible as narrower than the gene's GO:0051087; correct that no ATPase/holdase MF is asserted for this poorly-characterized member.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJB5/DNAJB5-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: O75953
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
