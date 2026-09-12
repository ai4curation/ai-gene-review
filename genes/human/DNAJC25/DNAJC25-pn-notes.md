# DNAJC25 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H1X3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC25/DNAJC25-ai-review.yaml](DNAJC25-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC25/DNAJC25-ai-review.html](DNAJC25-ai-review.html)
- Gene notes: present - [genes/human/DNAJC25/DNAJC25-notes.md](DNAJC25-notes.md)
- GOA TSV: present - [genes/human/DNAJC25/DNAJC25-goa.tsv](DNAJC25-goa.tsv)
- UniProt record: present - [genes/human/DNAJC25/DNAJC25-uniprot.txt](DNAJC25-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC25.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC25.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC25 (DnaJ homolog subfamily C member 25) is a poorly characterized multi-pass membrane protein of the HSP40/DnaJ co-chaperone family. It has an N-terminal signal-anchor/transmembrane segment followed by a J-domain bearing the canonical HPD tripeptide, plus additional predicted transmembrane helices. The J-domain is the module by which DnaJ proteins recruit and stimulate HSP70-family ATPases. By phylogenetic inference within its protein family, DNAJC25 is predicted to act at the endoplasmic reticulum membrane as a co-chaperone that assists HSP70-dependent protein folding/quality control, although no direct experimental functional data exist for the human protein. It is tissue-enriched in liver.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 3

## PN Consistency Summary

- **Consistency:** Deep research, notes, and review YAML agree: DNAJC25 is a poorly characterized multi-pass membrane DnaJ/HSP40 protein with an HPD-bearing J-domain; no direct human functional data. Review core MF = GO:0031072 heat shock protein binding (family/domain inference). PN "J-domain HSP70 cochaperone" placement is consistent. No contradictions; both flag the inference-only basis.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real). GOA lacks it (new_to_goa correct). GO:0030544 is a child of the review's GO:0031072 (heat shock protein binding) via GO:0051087 — i.e. PN proposes a strictly MORE SPECIFIC term than the review. Defensible as a J-protein domain-level inference, but rests on the same predicted-only evidence; an ADD as an inferred MF is reasonable but should not be over-elevated given zero experimental support for the human protein.
- **Evidence alignment:** PN row has no reference titles; review cites only the UniProt file (no primary literature exists). No divergence, but evidence base is thin on both sides.
- **Verdict:** Consistent. GO:0030544 ADD defensible as domain-inferred MF (new_to_goa, narrower than review's GO:0031072); keep IBA-strength caveat.

## Full Consistency Review

- **UniProt:** Q9H1X3 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (projected new_to_goa); group/class/branch=no_mapping.
- **Consistency:** Deep research, notes, and review YAML agree: DNAJC25 is a poorly characterized multi-pass membrane DnaJ/HSP40 protein with an HPD-bearing J-domain; no direct human functional data. Review core MF = GO:0031072 heat shock protein binding (family/domain inference). PN "J-domain HSP70 cochaperone" placement is consistent. No contradictions; both flag the inference-only basis.
- **PN story / NEW pressure:** PN asserts GO:0030544 Hsp70 protein binding (verified real). GOA lacks it (new_to_goa correct). GO:0030544 is a child of the review's GO:0031072 (heat shock protein binding) via GO:0051087 — i.e. PN proposes a strictly MORE SPECIFIC term than the review. Defensible as a J-protein domain-level inference, but rests on the same predicted-only evidence; an ADD as an inferred MF is reasonable but should not be over-elevated given zero experimental support for the human protein.
- **Mapping strategy:** Node status unchanged. Projection accurate (term absent from GOA). PN term is NARROWER than the review's core MF — appropriate direction for a J-domain protein, no over-broad inference concern.
- **Evidence alignment:** PN row has no reference titles; review cites only the UniProt file (no primary literature exists). No divergence, but evidence base is thin on both sides.
- **Verdict:** Consistent. GO:0030544 ADD defensible as domain-inferred MF (new_to_goa, narrower than review's GO:0031072); keep IBA-strength caveat.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC25/DNAJC25-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9H1X3
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
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
