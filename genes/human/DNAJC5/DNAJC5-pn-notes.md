# DNAJC5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H3Z4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC5/DNAJC5-ai-review.yaml](DNAJC5-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC5/DNAJC5-ai-review.html](DNAJC5-ai-review.html)
- Gene notes: present - [genes/human/DNAJC5/DNAJC5-notes.md](DNAJC5-notes.md)
- GOA TSV: present - [genes/human/DNAJC5/DNAJC5-goa.tsv](DNAJC5-goa.tsv)
- UniProt record: present - [genes/human/DNAJC5/DNAJC5-uniprot.txt](DNAJC5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC5 (cysteine string protein alpha, CSPalpha; also CLN4) is a palmitoylated DnaJ/HSP40 co-chaperone of the presynaptic and secretory-vesicle membrane. It carries an N-terminal J domain that recruits and stimulates the constitutive HSP70 chaperone HSC70/HSPA8 and a central cysteine-string domain whose extensive palmitoylation anchors the protein to vesicle membranes. As a vesicle-localized co-chaperone it maintains the conformational integrity of the SNARE machinery, acting as a co-chaperone for SNAP-25 (with HSC70 and SGTA) and interacting with synaptotagmins, thereby supporting regulated/calcium-dependent exocytosis and the synaptic vesicle cycle and protecting nerve terminals against activity-dependent degeneration. Loss-of-function or aggregation-prone mutations in the cysteine-string domain (Leu115Arg, Leu116del) cause autosomal-dominant adult-onset neuronal ceroid lipofuscinosis (CLN4/ANCL, Kufs type).
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 23; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strongly consistent on MF, with one placement nuance. Deep research (notes), review and PN converge on DNAJC5/CSPalpha as a palmitoylated J-domain co-chaperone of HSC70/HSPA8 (the SNAP-25 co-chaperone with SGTA) at the synaptic/secretory vesicle membrane; CLN4 disease gene (PMID:21820099). The review's core MF is exactly GO:0030544 Hsp70 protein binding (it even MODIFIES the rat-ortholog GO:0043008 ATP-dependent protein binding → GO:0030544), matching the PN projection. Nuance: PN places CSPalpha in the **ER** branch, whereas the dominant biology (and the review's core localizations: synaptic vesicle membrane, presynapse) is synaptic/secretory — not ER. The secretory-vesicle/exocytic role is ER-branch-adjacent (secretory pathway), so this is a reasonable umbrella, not a contradiction.
- **PN story / NEW pressure:** GO:0030544 is already the review's core MF, so the PN story is **already captured** (and verified real). No NEW pressure; CSPalpha's specific synaptic CSP role (regulation of synaptic vesicle cycle, synaptic vesicle exocytosis) is well annotated and goes beyond the generic J-domain MF the PN node carries.
- **Evidence alignment:** PN carries no row references. Review cites the disease/mechanism literature (PMID:21820099, 10099709, 15217342, 17081065, 29997244, 33961781) plus Reactome rows; well-supported, no divergence from PN.
- **Verdict:** Fully consistent; PN Hsp70-binding story already captured as core MF (GO:0030544). **Recommended edits:** none required; optionally [MAP] note that CSPalpha is the prototypical *synaptic/secretory-vesicle* CSP, so the ER-branch placement is an umbrella rather than its primary compartment.

## Full Consistency Review

- **UniProt:** Q9H3Z4 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type → mapped/ok_for_propagation_to_go GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa); all ancestor nodes no_mapping.
- **Consistency:** Strongly consistent on MF, with one placement nuance. Deep research (notes), review and PN converge on DNAJC5/CSPalpha as a palmitoylated J-domain co-chaperone of HSC70/HSPA8 (the SNAP-25 co-chaperone with SGTA) at the synaptic/secretory vesicle membrane; CLN4 disease gene (PMID:21820099). The review's core MF is exactly GO:0030544 Hsp70 protein binding (it even MODIFIES the rat-ortholog GO:0043008 ATP-dependent protein binding → GO:0030544), matching the PN projection. Nuance: PN places CSPalpha in the **ER** branch, whereas the dominant biology (and the review's core localizations: synaptic vesicle membrane, presynapse) is synaptic/secretory — not ER. The secretory-vesicle/exocytic role is ER-branch-adjacent (secretory pathway), so this is a reasonable umbrella, not a contradiction.
- **PN story / NEW pressure:** GO:0030544 is already the review's core MF, so the PN story is **already captured** (and verified real). No NEW pressure; CSPalpha's specific synaptic CSP role (regulation of synaptic vesicle cycle, synaptic vesicle exocytosis) is well annotated and goes beyond the generic J-domain MF the PN node carries.
- **Mapping strategy:** No change to the node. GO:0030544 is the correct, defensible Hsp70-cochaperone MF (not an over-broad holdase claim). goa_status=more_specific_than_existing_goa is accurate (GOA had only the broader/ATP-dependent terms).
- **Evidence alignment:** PN carries no row references. Review cites the disease/mechanism literature (PMID:21820099, 10099709, 15217342, 17081065, 29997244, 33961781) plus Reactome rows; well-supported, no divergence from PN.
- **Verdict:** Fully consistent; PN Hsp70-binding story already captured as core MF (GO:0030544). **Recommended edits:** none required; optionally [MAP] note that CSPalpha is the prototypical *synaptic/secretory-vesicle* CSP, so the ER-branch placement is an umbrella rather than its primary compartment.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC5/DNAJC5-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9H3Z4
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
