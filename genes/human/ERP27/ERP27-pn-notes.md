# ERP27 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96DN0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ERP27/ERP27-ai-review.yaml](ERP27-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ERP27/ERP27-ai-review.html](ERP27-ai-review.html)
- Gene notes: present - [genes/human/ERP27/ERP27-notes.md](ERP27-notes.md)
- GOA TSV: present - [genes/human/ERP27/ERP27-goa.tsv](ERP27-goa.tsv)
- UniProt record: present - [genes/human/ERP27/ERP27-uniprot.txt](ERP27-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ERP27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ERP27.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERP27.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERP27.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ERP27 (endoplasmic reticulum resident protein 27; ER protein 27; also known as C12orf46) is a soluble, ER-lumenal, two-domain member of the protein disulfide isomerase (PDI) family that is catalytically inactive. Unlike redox-active PDIs, it lacks the CXXC thioredoxin active-site motif and therefore cannot itself catalyze thiol-disulfide exchange; its thioredoxin-like domains correspond to the non-catalytic b and b' substrate-binding domains of PDI. ERP27 binds unfolded/misfolded proteins through a hydrophobic substrate-binding cleft in its C-terminal (b'-like) domain, discriminating folded from unfolded clients, and presents/recruits the catalytic PDI-family oxidoreductase PDIA3 (ERp57) to those substrates via a defined PDIA3-binding surface (residues 230-233). It is retained in the ER lumen by a C-terminal retention motif, is induced during ER stress / the unfolded protein response, and is enriched in the pancreas. Functionally it acts as a non-catalytic chaperone/substrate-recruiter within the ER oxidative-folding machinery rather than as a disulfide isomerase.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 7

## PN Consistency Summary

- **Consistency:** **Direct contradiction.** Notes and review YAML both establish that ERP27 is a **catalytically inactive, non-catalytic PDI-family member that LACKS the CXXC active-site motif** and therefore cannot perform thiol-disulfide exchange. The review contains an explicit **negated** annotation — `GO:0003756 protein disulfide isomerase activity, negated: true` (IBA, GO_REF:0000033), action ACCEPT — i.e. the curated record states ERP27 does NOT have PDI activity. The PN group node projects the **exact same term GO:0003756 as new_to_goa** (a positive addition). PN proposes adding the precise term the review explicitly negates. This is the hardest conflict in the batch.
- **PN story / NEW pressure:** GO:0003756 (OLS-verified) must **NOT** be added to ERP27 — it is biologically wrong (no CXXC) and is already correctly captured as a NOT annotation in GOA/review. ERP27's real core functions are **GO:0051082 unfolded protein binding** (substrate discrimination via the b'-like cleft, PMID:23192347) and **GO:0051087 protein-folding chaperone binding** (recruits/presents substrates to the catalytic PDIA3/ERp57, PMID:16940051/23192347) — both added in the review, neither surfaced by the PN node. Conclusion: PN projection **over-reaches / is incorrect**; the review's substrate-presenter framing is the right model.
- **Evidence alignment:** PN dossier lists no reference titles. Review evidence (PMID:16940051 founding non-catalytic characterization, GOA-anchored to GO:0005788 EXP; PMID:23192347 crystal structure + ITC substrate discrimination) is reviewer-supplied and directly supports the non-catalytic substrate-presenter role. No shared citation list to compare; the biology flatly opposes the PN GO:0003756 projection.
- **Verdict:** **Contradiction** — PN projects GO:0003756 (new_to_goa) onto a gene whose review explicitly NEGATES that exact term (no CXXC, catalytically inactive). PN over-reaches; review is correct. **Recommended edits:** [MAP] remove/suppress the GO:0003756 projection for ERP27 (it is a non-catalytic PDI-family member; the term is correctly a NOT annotation). If a positive mapping is wanted, target GO:0051082 unfolded protein binding and/or GO:0051087 protein-folding chaperone binding (both OLS-real, both already in the review's core_functions).

## Full Consistency Review

- **UniProt:** Q96DN0 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Folding enzyme|Protein disulfide isomerases`. **PN-node mapping:** group `Protein disulfide isomerases`=mapped→**GO:0003756 protein disulfide isomerase activity** (new_to_goa); class `Folding enzyme`=no_mapping; branch=no_mapping.
- **Consistency:** **Direct contradiction.** Notes and review YAML both establish that ERP27 is a **catalytically inactive, non-catalytic PDI-family member that LACKS the CXXC active-site motif** and therefore cannot perform thiol-disulfide exchange. The review contains an explicit **negated** annotation — `GO:0003756 protein disulfide isomerase activity, negated: true` (IBA, GO_REF:0000033), action ACCEPT — i.e. the curated record states ERP27 does NOT have PDI activity. The PN group node projects the **exact same term GO:0003756 as new_to_goa** (a positive addition). PN proposes adding the precise term the review explicitly negates. This is the hardest conflict in the batch.
- **PN story / NEW pressure:** GO:0003756 (OLS-verified) must **NOT** be added to ERP27 — it is biologically wrong (no CXXC) and is already correctly captured as a NOT annotation in GOA/review. ERP27's real core functions are **GO:0051082 unfolded protein binding** (substrate discrimination via the b'-like cleft, PMID:23192347) and **GO:0051087 protein-folding chaperone binding** (recruits/presents substrates to the catalytic PDIA3/ERp57, PMID:16940051/23192347) — both added in the review, neither surfaced by the PN node. Conclusion: PN projection **over-reaches / is incorrect**; the review's substrate-presenter framing is the right model.
- **Mapping strategy:** This gene exposes the core flaw of the `Protein disulfide isomerases` group projecting GO:0003756 to all leaves: the node lumps catalytic isomerases (P4HB, AGR2-debated), redox oxidases (ERO1A/B), and **non-catalytic members (ERP27)**. For ERP27 the projection is not merely broad (TOMM20/HSPA8/RAB7A precedent) but actively wrong, contradicting an explicit negation. Gene-level mapping for ERP27 should be no_mapping for GO:0003756 (or carry the negation), with any positive mapping pointing at unfolded protein binding / chaperone-binding.
- **Evidence alignment:** PN dossier lists no reference titles. Review evidence (PMID:16940051 founding non-catalytic characterization, GOA-anchored to GO:0005788 EXP; PMID:23192347 crystal structure + ITC substrate discrimination) is reviewer-supplied and directly supports the non-catalytic substrate-presenter role. No shared citation list to compare; the biology flatly opposes the PN GO:0003756 projection.
- **Verdict:** **Contradiction** — PN projects GO:0003756 (new_to_goa) onto a gene whose review explicitly NEGATES that exact term (no CXXC, catalytically inactive). PN over-reaches; review is correct. **Recommended edits:** [MAP] remove/suppress the GO:0003756 projection for ERP27 (it is a non-catalytic PDI-family member; the term is correctly a NOT annotation). If a positive mapping is wanted, target GO:0051082 unfolded protein binding and/or GO:0051087 protein-folding chaperone binding (both OLS-real, both already in the review's core_functions).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/ERP27/ERP27-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: Q96DN0
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
