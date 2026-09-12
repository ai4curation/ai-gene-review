# DNAJC30 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96LL9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC30/DNAJC30-ai-review.yaml](DNAJC30-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC30/DNAJC30-ai-review.html](DNAJC30-ai-review.html)
- Gene notes: present - [genes/human/DNAJC30/DNAJC30-notes.md](DNAJC30-notes.md)
- GOA TSV: present - [genes/human/DNAJC30/DNAJC30-goa.tsv](DNAJC30-goa.tsv)
- UniProt record: present - [genes/human/DNAJC30/DNAJC30-uniprot.txt](DNAJC30-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC30.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC30.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC30.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC30.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC30 (WBSCR18) is a mitochondrial inner-membrane DnaJ/HSP40 (J-domain) protein encoded in the 7q11.23 Williams-Beuren syndrome critical region. Imported via an N-terminal transit peptide and anchored by a single transmembrane helix, it has two intertwined roles in oxidative phosphorylation. It is an auxiliary component of the ATP synthase machinery, interacting directly with MT-ATP6 and ATP5MC2 and facilitating ATP synthesis. It also acts as a chaperone in a mitochondrial complex I (NADH:ubiquinone oxidoreductase) repair mechanism, promoting the efficient exchange/turnover of N-module subunits damaged by reactive oxygen species and thereby maintaining complex I efficiency. DNAJC30 is highly expressed in brain (pyramidal neurons). Biallelic loss-of-function variants cause autosomal-recessive Leber hereditary optic neuropathy (LHONAR1), and hemizygous loss contributes to the mitochondrial dysfunction underlying neurodevelopmental features of Williams-Beuren syndrome.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 3; MODIFY: 1

## PN Consistency Summary

- **Consistency:** SUBSTANTIVE TENSION. Deep research and review YAML establish DNAJC30 as a mitochondrial inner-membrane factor with two well-supported, NON-canonical-chaperone roles: (1) auxiliary component of ATP synthase (direct MT-ATP6/ATP5MC2 binding, PMID:30318146; core MF GO:0019899 enzyme binding); (2) chaperone in **complex I N-module repair/subunit exchange** (PMID:33465056; core MF GO:0051082 unfolded protein binding; causes recessive LHON). The review explicitly does NOT establish any HSP70 interaction. The PN "J-domain HSP70 cochaperone" placement is an over-broad family inference: DNAJC30 is a complex-I assembly/repair factor, not a characterized HSP70 cochaperone.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real) — but this is contradicted in emphasis by the review, which found no HSP70 partner (the J-domain's canonical cochaperone activity is itself flagged as an open question in suggested_questions). GOA has no chaperone-binding term, so "more_specific_than_existing_goa" is wrong; at most new_to_goa, and even as new it OVER-REACHES given the characterized complex-I/ATP-synthase biology. Mirrors the TOMM20/HSPA8/RAB7A "rejected as broader/family-inferred" precedent.
- **Evidence alignment:** PN row no titles; review cites PMID:30318146 (ATP synthase/brain dev) and PMID:33465056 (complex I repair / recessive LHON) — both VERIFIED, full-text cached. No paper supports HSP70 binding.
- **Verdict:** Over-reach. GO:0030544 projection is unsupported for DNAJC30 (a complex-I repair / ATP-synthase auxiliary factor). **Recommended edits:** [MAP] do not propagate GO:0030544 to DNAJC30 (family-level over-inference; gene-level GO:0051082 + GO:0019899 already capture its biology); [MAP] if retained, downgrade goa_status to new_to_goa and mark as IBA/family-inferred only.

## Full Consistency Review

- **UniProt:** Q96LL9 (WBSCR18) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (projected more_specific_than_existing_goa); group/class/branch=no_mapping (class explicitly "too heterogeneous").
- **Consistency:** SUBSTANTIVE TENSION. Deep research and review YAML establish DNAJC30 as a mitochondrial inner-membrane factor with two well-supported, NON-canonical-chaperone roles: (1) auxiliary component of ATP synthase (direct MT-ATP6/ATP5MC2 binding, PMID:30318146; core MF GO:0019899 enzyme binding); (2) chaperone in **complex I N-module repair/subunit exchange** (PMID:33465056; core MF GO:0051082 unfolded protein binding; causes recessive LHON). The review explicitly does NOT establish any HSP70 interaction. The PN "J-domain HSP70 cochaperone" placement is an over-broad family inference: DNAJC30 is a complex-I assembly/repair factor, not a characterized HSP70 cochaperone.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real) — but this is contradicted in emphasis by the review, which found no HSP70 partner (the J-domain's canonical cochaperone activity is itself flagged as an open question in suggested_questions). GOA has no chaperone-binding term, so "more_specific_than_existing_goa" is wrong; at most new_to_goa, and even as new it OVER-REACHES given the characterized complex-I/ATP-synthase biology. Mirrors the TOMM20/HSPA8/RAB7A "rejected as broader/family-inferred" precedent.
- **Mapping strategy:** This gene argues AGAINST propagating GO:0030544 from the type node to DNAJC30. The review's evidence-backed MFs (GO:0051082, GO:0019899) are the right calls; the family-projected GO:0030544 is broader/unsupported for this member.
- **Evidence alignment:** PN row no titles; review cites PMID:30318146 (ATP synthase/brain dev) and PMID:33465056 (complex I repair / recessive LHON) — both VERIFIED, full-text cached. No paper supports HSP70 binding.
- **Verdict:** Over-reach. GO:0030544 projection is unsupported for DNAJC30 (a complex-I repair / ATP-synthase auxiliary factor). **Recommended edits:** [MAP] do not propagate GO:0030544 to DNAJC30 (family-level over-inference; gene-level GO:0051082 + GO:0019899 already capture its biology); [MAP] if retained, downgrade goa_status to new_to_goa and mark as IBA/family-inferred only.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC30/DNAJC30-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q96LL9
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [type] Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Mitochondrial proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Mitochondrial proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: This PN class is too heterogeneous for a single safe GO mapping. In the workbook it mixes HSP70, HSP60, and HSP90 systems, small intermembrane-space chaperones, membrane-protein chaperones, and other mitochondrial-specific factors.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
