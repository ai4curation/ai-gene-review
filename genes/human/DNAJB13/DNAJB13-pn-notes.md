# DNAJB13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P59910
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJB13/DNAJB13-ai-review.yaml](DNAJB13-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJB13/DNAJB13-ai-review.html](DNAJB13-ai-review.html)
- Gene notes: present - [genes/human/DNAJB13/DNAJB13-notes.md](DNAJB13-notes.md)
- GOA TSV: present - [genes/human/DNAJB13/DNAJB13-goa.tsv](DNAJB13-goa.tsv)
- UniProt record: present - [genes/human/DNAJB13/DNAJB13-uniprot.txt](DNAJB13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJB13 (DnaJ homolog subfamily B member 13; also TSARG3/TSARG6) is an HSP40/J-domain protein that, despite belonging to the co-chaperone family, acts principally as a structural component of the axonemal radial spoke complex. It is a homodimer found in the radial spoke stalk together with RSPH14, DYDC1, ROPN1L and NME5, and is required for the proper formation and function of the ciliary and flagellar axoneme. It localizes to epithelial motile (respiratory) cilia and to the sperm flagellum, where in spermatids it is enriched at the head-tail coupling apparatus and in mature sperm is distributed along the flagellum. Expression is largely restricted to testis and trachea. DNAJB13 supports the motility of sperm and cilia; biallelic loss-of-function variants cause autosomal-recessive primary ciliary dyskinesia (CILD34) with central-complex defects and male infertility.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** CONTRADICTION — this is the misfit. Notes and review YAML both conclude DNAJB13 is functionally a *structural* component of the axonemal radial spoke (RS1 stalk), NOT a working cytosolic HSP70 co-chaperone. The review actively downgrades the J-protein/HSP70 inferences: GO:0051087 chaperone binding and GO:0006457 folding are KEEP_AS_NON_CORE ("not experimentally demonstrated"), and IBA cytosol (GO:0005829) is MARK_AS_OVER_ANNOTATED. Core MF is assigned as GO:0030674 protein-macromolecule adaptor activity, located in radial spoke/axoneme. The PN placement under "HSP70 system | J-domain HSP70 cochaperone" with a mapped GO:0030544 directly conflicts with the review's verdict that no HSP70-binding function is demonstrated for this protein. Also note: PN puts it in the *ER* branch, but DNAJB13 is axonemal/ciliary — not an ER protein.
- **PN story / NEW pressure:** PN asserts HSP70 binding the review explicitly rejects as undemonstrated. No NEW GO pressure for proteostasis; the gene's defensible terms are cilium/flagellum/radial-spoke (GO:0001534, GO:0005930, GO:1904158, GO:0030317, GO:0003341) — all already captured. Over-reaches as a proteostasis HSP70 cochaperone.
- **Evidence alignment:** PN cochaperone framing diverges from the review's evidence (PMID:27486783 PCD/radial spoke; PMID:36417862 RS1) which is entirely axonemal. No HSP70/BiP papers in the review.
- **Verdict:** OVER-REACH / MISPLACED — DNAJB13 should be excluded from the HSP70-cochaperone GO:0030544 propagation (and arguably from the ER/HSP70-system PN node); its function is structural radial-spoke, captured by GO:0001534/GO:0030674.

## Full Consistency Review

- **UniProt:** P59910 (TSARG3/TSARG6) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (parents no_mapping)
- **Consistency:** CONTRADICTION — this is the misfit. Notes and review YAML both conclude DNAJB13 is functionally a *structural* component of the axonemal radial spoke (RS1 stalk), NOT a working cytosolic HSP70 co-chaperone. The review actively downgrades the J-protein/HSP70 inferences: GO:0051087 chaperone binding and GO:0006457 folding are KEEP_AS_NON_CORE ("not experimentally demonstrated"), and IBA cytosol (GO:0005829) is MARK_AS_OVER_ANNOTATED. Core MF is assigned as GO:0030674 protein-macromolecule adaptor activity, located in radial spoke/axoneme. The PN placement under "HSP70 system | J-domain HSP70 cochaperone" with a mapped GO:0030544 directly conflicts with the review's verdict that no HSP70-binding function is demonstrated for this protein. Also note: PN puts it in the *ER* branch, but DNAJB13 is axonemal/ciliary — not an ER protein.
- **PN story / NEW pressure:** PN asserts HSP70 binding the review explicitly rejects as undemonstrated. No NEW GO pressure for proteostasis; the gene's defensible terms are cilium/flagellum/radial-spoke (GO:0001534, GO:0005930, GO:1904158, GO:0030317, GO:0003341) — all already captured. Over-reaches as a proteostasis HSP70 cochaperone.
- **Mapping strategy:** The type-level GO:0030544 mapping should NOT propagate to DNAJB13 — it is a catalytically/functionally divergent J-domain member whose J domain appears repurposed structurally (review's own suggested experiment asks whether HSP70-stimulating activity is retained at all). This is exactly the "distinguish genuine Hsp70-cochaperone from members lacking direct evidence" flag.
- **Evidence alignment:** PN cochaperone framing diverges from the review's evidence (PMID:27486783 PCD/radial spoke; PMID:36417862 RS1) which is entirely axonemal. No HSP70/BiP papers in the review.
- **Verdict:** OVER-REACH / MISPLACED — DNAJB13 should be excluded from the HSP70-cochaperone GO:0030544 propagation (and arguably from the ER/HSP70-system PN node); its function is structural radial-spoke, captured by GO:0001534/GO:0030674.
- **Recommended edits:** [MAP] Exclude DNAJB13 from the `J-domain containing HSP70 cochaperone` GO:0030544 projection (catalytically-divergent, no HSP70-binding evidence; function is structural radial-spoke). [MAP] Re-examine its ER-branch placement (protein is axonemal, not ER-resident).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJB13/DNAJB13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: P59910
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
