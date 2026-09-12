# DNAJC27 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NZQ0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC27/DNAJC27-ai-review.yaml](DNAJC27-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC27/DNAJC27-ai-review.html](DNAJC27-ai-review.html)
- Gene notes: present - [genes/human/DNAJC27/DNAJC27-notes.md](DNAJC27-notes.md)
- GOA TSV: present - [genes/human/DNAJC27/DNAJC27-goa.tsv](DNAJC27-goa.tsv)
- UniProt record: present - [genes/human/DNAJC27/DNAJC27-uniprot.txt](DNAJC27-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC27.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC27.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC27 (RBJ/RABJS; "Rab and DnaJ domain-containing protein") is an unusual chimeric protein combining an N-terminal Ras/Rab-like small-GTPase (P-loop NTPase) domain with a C-terminal DnaJ/J domain, a member of the RJL family. It binds GTP and, in its GTP-bound form, engages the MAP kinase MAP2K1/MEK1 and binds MAPK1/ERK2 through its N-terminal region; nucleus-localized RBJ entraps MEK1/MEK2 in the nucleus and prolongs ERK1/ERK2 activation, acting as a positive regulator/scaffold of the MEK/ERK (MAPK) cascade. Unlike canonical Ras-superfamily GTPases the RJL proteins lack the catalytic glutamine that coordinates GTP hydrolysis, so its intrinsic GTPase activity is uncertain. The C-terminal J domain is predicted to recruit Hsc70/HSP70. DNAJC27 is enhanced in testis, is overexpressed in gastrointestinal cancers, and behaves as an oncogene promoting carcinogenesis and tumor progression.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** PARTIAL TENSION. Deep research and review YAML converge on RBJ as a chimeric Ras/Rab-GTPase + J-domain protein whose CHARACTERIZED function is a GTP-bound MEK/ERK scaffold/positive regulator (core MF GO:0005525 GTP binding; core BP GO:0070374 ERK cascade), oncogenic in GI cancer. The C-terminal J-domain is only PREDICTED to recruit Hsc70/HSP70 (PMID:14980719), with no experimental HSP70-cochaperone characterization. The PN node files RBJ purely as a "J-domain HSP70 cochaperone," which captures the J-domain but omits its dominant, evidence-backed GTPase/ERK identity — a placement/emphasis mismatch, not a hard contradiction.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real). GOA lacks any HSP70/chaperone-binding term, so the "more_specific_than_existing_goa" label is loose — there is nothing in GOA for it to be more specific *than*; functionally it is new_to_goa. GO:0030544 is defensible only as a domain-level prediction; over-reaches if presented as a core function, since the gene's real MF is GTP binding / ERK scaffolding.
- **Evidence alignment:** PN row carries no titles; review cites PMID:14980719 (RJL family, J-domain prediction) and PMID:24746703 (nuclear MEK/ERK entrapment) — both VERIFIED. The HSP70-binding story rests only on the family prediction; no shared experimental paper supports it.
- **Verdict:** Consistent core review; PN placement over-emphasizes the J-domain. GO:0030544 is a defensible inferred ADD but **not core**. **Recommended edits:** [MAP] change goa_status from more_specific_than_existing_goa to new_to_goa (no existing chaperone-binding GOA term to refine).

## Full Consistency Review

- **UniProt:** Q9NZQ0 (RBJ / RABJS) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (projected more_specific_than_existing_goa); group/class/branch=no_mapping.
- **Consistency:** PARTIAL TENSION. Deep research and review YAML converge on RBJ as a chimeric Ras/Rab-GTPase + J-domain protein whose CHARACTERIZED function is a GTP-bound MEK/ERK scaffold/positive regulator (core MF GO:0005525 GTP binding; core BP GO:0070374 ERK cascade), oncogenic in GI cancer. The C-terminal J-domain is only PREDICTED to recruit Hsc70/HSP70 (PMID:14980719), with no experimental HSP70-cochaperone characterization. The PN node files RBJ purely as a "J-domain HSP70 cochaperone," which captures the J-domain but omits its dominant, evidence-backed GTPase/ERK identity — a placement/emphasis mismatch, not a hard contradiction.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real). GOA lacks any HSP70/chaperone-binding term, so the "more_specific_than_existing_goa" label is loose — there is nothing in GOA for it to be more specific *than*; functionally it is new_to_goa. GO:0030544 is defensible only as a domain-level prediction; over-reaches if presented as a core function, since the gene's real MF is GTP binding / ERK scaffolding.
- **Mapping strategy:** Node status unchanged. goa_status flag ("more_specific_than_existing_goa") should be new_to_goa. The projected term is domain-inferred, not characterized — keep IBA/IEA strength, do not elevate to core.
- **Evidence alignment:** PN row carries no titles; review cites PMID:14980719 (RJL family, J-domain prediction) and PMID:24746703 (nuclear MEK/ERK entrapment) — both VERIFIED. The HSP70-binding story rests only on the family prediction; no shared experimental paper supports it.
- **Verdict:** Consistent core review; PN placement over-emphasizes the J-domain. GO:0030544 is a defensible inferred ADD but **not core**. **Recommended edits:** [MAP] change goa_status from more_specific_than_existing_goa to new_to_goa (no existing chaperone-binding GOA term to refine).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC27/DNAJC27-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9NZQ0
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
