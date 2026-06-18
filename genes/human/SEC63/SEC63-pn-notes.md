# SEC63 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UGP8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SEC63/SEC63-ai-review.yaml](SEC63-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SEC63/SEC63-ai-review.html
- Gene notes: present - [genes/human/SEC63/SEC63-notes.md](SEC63-notes.md)
- GOA TSV: present - [genes/human/SEC63/SEC63-goa.tsv](SEC63-goa.tsv)
- UniProt record: present - [genes/human/SEC63/SEC63-uniprot.txt](SEC63-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SEC63.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SEC63.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SEC63.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SEC63.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SEC63/SEC63-deep-research-falcon.md](SEC63-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SEC63 (also DNAJC23) is a multi-pass endoplasmic reticulum membrane protein and an auxiliary component of the Sec61 translocon. It contains a luminal J-domain (DnaJ/Hsp40-type) and two Sec63 domains. Together with SEC62 it forms the SEC62-SEC63 subcomplex that supports cotranslational and post-translational translocation of precursor polypeptides into the ER. Its defining mechanism is co-chaperone activity, in which the luminal J-domain recruits and stimulates the ATPase cycle of the ER Hsp70 chaperone BiP (HSPA5), positioning BiP on incoming polypeptides at the translocon to drive and gate their translocation into the ER lumen. SEC63 cooperates with SEC62 and BiP in importing small presecretory proteins with short, apolar signal peptides, and is required for efficient biogenesis and trafficking of polycystin-1 (PKD1). SEC63 is widely expressed with high levels in liver, and loss-of-function variants cause autosomal dominant polycystic liver disease (PCLD2).
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, notes, and review YAML all frame SEC63 as a translocon-accessory DnaJ/Hsp40 J-domain co-chaperone that recruits/stimulates ER Hsp70 BiP (HSPA5) via its luminal J-domain (HPD/H132) to gate Sec61 and drive translocation. PN's dual placement (HSP70-system J-cochaperone + SEC61 component) exactly matches the review's two core_functions. No contradictions.
- **PN story / NEW pressure:** PN asserts a role NOT in existing GO annotations. SEC63 GOA has GO:0031207 (Sec62/Sec63 complex) and translocation BP terms, but NO molecular-function term for the J-domain/BiP co-chaperone activity. The review's own suggested_questions explicitly flags this gap. PN-projected GO:0030544 Hsp70 protein binding (verified real, def "Binding to a Hsp70 protein") precisely captures the J-domain-BiP interaction. Strong, defensible ADD. (GO:0051087 protein-folding chaperone binding is a verified broader alternative.) Conclude: ADD GO:0030544.
- **Evidence alignment:** PN rows carry no reference titles, but the review's BiP/J-domain evidence (PMID:29719251, 36459117, 32133789; SUBUNIT/DOMAIN/H132 mutagenesis) and the falcon deep research (shao2023, sun2022, schorr2019) fully support the PN J-cochaperone claim. Congruent; no divergence.
- **Verdict:** CONSISTENT; PN supplies the strongest NEW-term signal of the set (Hsp70 binding MF missing from GOA).

## Full Consistency Review

- **UniProt:** Q9UGP8 (DNAJC23) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` and `ER proteostasis|Protein transport|SEC61 channel complex component`; **PN-node mapping:** J-cochaperone type mapped, ok_for_propagation_to_go, GO:0030544 (Hsp70 protein binding); translocon group GO:0005784 (Sec61 translocon complex); transport class GO:0015031 (protein transport).
- **Consistency:** Strong agreement. Deep research, notes, and review YAML all frame SEC63 as a translocon-accessory DnaJ/Hsp40 J-domain co-chaperone that recruits/stimulates ER Hsp70 BiP (HSPA5) via its luminal J-domain (HPD/H132) to gate Sec61 and drive translocation. PN's dual placement (HSP70-system J-cochaperone + SEC61 component) exactly matches the review's two core_functions. No contradictions.
- **PN story / NEW pressure:** PN asserts a role NOT in existing GO annotations. SEC63 GOA has GO:0031207 (Sec62/Sec63 complex) and translocation BP terms, but NO molecular-function term for the J-domain/BiP co-chaperone activity. The review's own suggested_questions explicitly flags this gap. PN-projected GO:0030544 Hsp70 protein binding (verified real, def "Binding to a Hsp70 protein") precisely captures the J-domain-BiP interaction. Strong, defensible ADD. (GO:0051087 protein-folding chaperone binding is a verified broader alternative.) Conclude: ADD GO:0030544.
- **Mapping strategy:** Mapping is correct and is the gene that most justifies its node's MF. GO:0030544 is appropriately specific (not over-broad). Dossier `more_specific_than_existing_goa` is accurate (no MF chaperone term in GOA). GO:0005784 translocon CC is also defensible (TRAP-inclusive def); note SEC63 already has the narrower GO:0031207. No mapping change needed.
- **Evidence alignment:** PN rows carry no reference titles, but the review's BiP/J-domain evidence (PMID:29719251, 36459117, 32133789; SUBUNIT/DOMAIN/H132 mutagenesis) and the falcon deep research (shao2023, sun2022, schorr2019) fully support the PN J-cochaperone claim. Congruent; no divergence.
- **Verdict:** CONSISTENT; PN supplies the strongest NEW-term signal of the set (Hsp70 binding MF missing from GOA).
- **Recommended edits:** [YAML] Add MF GO:0030544 Hsp70 protein binding (enables; J-domain stimulation of BiP/HSPA5) to SEC63 existing_annotations + core_functions, supported by H132/HPD mutagenesis and PMID:29719251/36459117. [YAML] Optionally add GO:0005784 Sec61 translocon complex CC to mirror the PN node.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SEC63/SEC63-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9UGP8
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

## PN row 2: ER proteostasis | Protein transport | SEC61 channel complex component
- UniProt: Q9UGP8
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|SEC61 channel complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005784 Sec61 translocon complex]
        rationale: This PN group denotes SEC61 translocon components. The GO Sec61 translocon complex term is the direct cellular-component target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=ER proteostasis|Protein transport
- GO:0005784 Sec61 translocon complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|SEC61 channel complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
