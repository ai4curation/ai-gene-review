# DNAJC4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NNZ3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC4/DNAJC4-ai-review.yaml](DNAJC4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC4/DNAJC4-ai-review.html](DNAJC4-ai-review.html)
- Gene notes: present - [genes/human/DNAJC4/DNAJC4-notes.md](DNAJC4-notes.md)
- GOA TSV: present - [genes/human/DNAJC4/DNAJC4-goa.tsv](DNAJC4-goa.tsv)
- UniProt record: present - [genes/human/DNAJC4/DNAJC4-uniprot.txt](DNAJC4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC4 (DnaJ homolog subfamily C member 4; also called DnaJ-like protein HSPF2 and MEN1 candidate protein 18, MCG18) is a poorly characterized member of the DnaJ/HSP40 (type III, "C") co-chaperone family. It comprises an N-terminal J domain (the signature HPD-motif-containing module that engages and stimulates HSP70 chaperones), a disordered central region, and a predicted single-pass transmembrane helix near the C-terminus, consistent with annotation as a membrane protein. By family assignment it is expected to act as an HSP70 co-chaperone, but no direct biochemical characterization of its chaperone activity or client repertoire has been reported. It is expressed broadly with enhancement in testis.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 4

## PN Consistency Summary

- **Consistency:** Mostly consistent but with a placement nuance and an MF mismatch. Deep research (notes), review and PN agree DNAJC4 is a Tdark, essentially uncharacterized type-III DnaJ/HSP40 co-chaperone (J domain aa 34-99) with a predicted single-pass TM helix; PAN-GO returns 0 evolutionary annotations. No experimental chaperone data exist. Discrepancy 1: PN places DNAJC4 in the **Mitochondrial** branch, but neither the review nor notes give any mitochondrial evidence (review's only locations are membrane/single-pass TM; UniProt gives no mito targeting). Discrepancy 2: PN projects GO:0030544 Hsp70 protein binding as the type MF, but the review's core MF is GO:0051082 unfolded protein binding (chosen deliberately as a cautious family-level call) — GO:0030544 appears nowhere in the review.
- **PN story / NEW pressure:** PN asserts an Hsp70-binding MF (GO:0030544, verified real via OLS) not present in GOA (GOA has only response to unfolded protein, BP) nor in the review. For a J-domain protein this is the canonical co-chaperone MF and is defensible **by family**, but is unverified experimentally for DNAJC4 specifically — consistent with the review's deliberately cautious GO:0051082. Conclusion: a defensible family-level ADD candidate, but **unverified**; do not assert as core.
- **Evidence alignment:** PN row carries no reference titles. Review/notes cite PMID:9473517 (cloning paper; UNVERIFIED, not cached), PMID:17500595 (HTT interactome), PMID:32814053 (neurodegeneration interactome). No overlap with PN, but no contradiction.
- **Verdict:** Family-level J-co-chaperone call sound; GO:0030544 is a defensible-but-unverified ADD; mitochondrial placement and the GO:0030544-vs-GO:0051082 MF mismatch need reconciling. **Recommended edits:** [MAP] reconcile Hsp70 protein binding (GO:0030544) projection with the review's GO:0051082 unfolded protein binding — both are family-level/unverified; prefer GO:0030544 only if asserted as predicted, not experimental. [MAP][WB] verify the Mitochondrial-branch assignment — no mitochondrial localization evidence appears in the review or notes.

## Full Consistency Review

- **UniProt:** Q9NNZ3 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch MI) ; **PN-node mapping:** type → mapped/ok_for_propagation_to_go GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa); all ancestor nodes no_mapping.
- **Consistency:** Mostly consistent but with a placement nuance and an MF mismatch. Deep research (notes), review and PN agree DNAJC4 is a Tdark, essentially uncharacterized type-III DnaJ/HSP40 co-chaperone (J domain aa 34-99) with a predicted single-pass TM helix; PAN-GO returns 0 evolutionary annotations. No experimental chaperone data exist. Discrepancy 1: PN places DNAJC4 in the **Mitochondrial** branch, but neither the review nor notes give any mitochondrial evidence (review's only locations are membrane/single-pass TM; UniProt gives no mito targeting). Discrepancy 2: PN projects GO:0030544 Hsp70 protein binding as the type MF, but the review's core MF is GO:0051082 unfolded protein binding (chosen deliberately as a cautious family-level call) — GO:0030544 appears nowhere in the review.
- **PN story / NEW pressure:** PN asserts an Hsp70-binding MF (GO:0030544, verified real via OLS) not present in GOA (GOA has only response to unfolded protein, BP) nor in the review. For a J-domain protein this is the canonical co-chaperone MF and is defensible **by family**, but is unverified experimentally for DNAJC4 specifically — consistent with the review's deliberately cautious GO:0051082. Conclusion: a defensible family-level ADD candidate, but **unverified**; do not assert as core.
- **Mapping strategy:** Type-level GO:0030544 is appropriate breadth for a J-domain co-chaperone and is NOT an over-reach (unlike holdase claims). However the Mitochondrial-branch placement is unsupported by any evidence in the dossier and should be checked.
- **Evidence alignment:** PN row carries no reference titles. Review/notes cite PMID:9473517 (cloning paper; UNVERIFIED, not cached), PMID:17500595 (HTT interactome), PMID:32814053 (neurodegeneration interactome). No overlap with PN, but no contradiction.
- **Verdict:** Family-level J-co-chaperone call sound; GO:0030544 is a defensible-but-unverified ADD; mitochondrial placement and the GO:0030544-vs-GO:0051082 MF mismatch need reconciling. **Recommended edits:** [MAP] reconcile Hsp70 protein binding (GO:0030544) projection with the review's GO:0051082 unfolded protein binding — both are family-level/unverified; prefer GO:0030544 only if asserted as predicted, not experimental. [MAP][WB] verify the Mitochondrial-branch assignment — no mitochondrial localization evidence appears in the review or notes.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC4/DNAJC4-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9NNZ3
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
