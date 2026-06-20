# COLGALT2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IYK4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/COLGALT2/COLGALT2-ai-review.yaml](COLGALT2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/COLGALT2/COLGALT2-ai-review.html](COLGALT2-ai-review.html)
- Gene notes: present - [genes/human/COLGALT2/COLGALT2-notes.md](COLGALT2-notes.md)
- GOA TSV: present - [genes/human/COLGALT2/COLGALT2-goa.tsv](COLGALT2-goa.tsv)
- UniProt record: present - [genes/human/COLGALT2/COLGALT2-uniprot.txt](COLGALT2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/COLGALT2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/COLGALT2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/COLGALT2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/COLGALT2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: COLGALT2 (collagen beta(1-O)galactosyltransferase 2; also known as GLT25D2, glycosyltransferase 25 family member 2) is an endoplasmic reticulum-luminal, manganese-dependent glycosyltransferase that catalyzes the transfer of beta-galactose from UDP-galactose to hydroxylysine residues of collagens, forming galactosyl-O-hydroxylysine (Gal-O-Hyl). This is the first step of collagen O-glycosylation, which precedes glucosylation to generate the glucosylgalactosyl-hydroxylysine (Glc-Gal-O-Hyl) disaccharide found on collagens and other proteins with collagenous domains. It is a member of the glycosyltransferase 25 (GT25) family and a paralog of COLGALT1, with which it shares procollagen galactosyltransferase activity (EC 2.4.1.50) but no glucosyltransferase activity. The mature protein is a soluble ER-luminal enzyme retained in the ER by a C-terminal SRDEL (KDEL-like) retention signal. Compared with the ubiquitously expressed COLGALT1, COLGALT2 has a more restricted tissue distribution, with expression enriched in brain and skeletal muscle.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review, PN annotation, and PN-node mapping agree: COLGALT2/GLT25D2 is a soluble ER-luminal, Mn2+-dependent collagen beta(1-O)galactosyltransferase (EC 2.4.1.50), paralog of COLGALT1, brain/skeletal-muscle-enriched. No contradictions.
- **PN story / NEW pressure:** PN projects GO:0032964 collagen biosynthetic process (verified real OLS). Review captures the more specific GO:0050211 procollagen galactosyltransferase activity (MF) and proposes GO:0180062 protein O-linked glycosylation via galactose as a NEW BP (replacing reliance on the downstream GO:0030199). The PN pathway context is consistent with and broader than these. Conclusion: **already captured** (review goes finer-grained); no PN-driven NEW pressure.
- **Evidence alignment:** PN row has no reference titles; review's enzymatic evidence rests mainly on PMID:19075007 and UniProt (plus high-throughput protein-binding PMIDs marked over-annotated). Collagen-biosynthesis evidence base is thinner than COLGALT1's but adequate and concordant with the mapping. No divergence.
- **Verdict:** Consistent; PN collagen-biosynthesis role already captured (more specifically) in review. No edits required.

## Full Consistency Review

- **UniProt:** Q8IYK4 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO:0032964 collagen biosynthetic process (class/branch = no_mapping)
- **Consistency:** Consistent. Review, PN annotation, and PN-node mapping agree: COLGALT2/GLT25D2 is a soluble ER-luminal, Mn2+-dependent collagen beta(1-O)galactosyltransferase (EC 2.4.1.50), paralog of COLGALT1, brain/skeletal-muscle-enriched. No contradictions.
- **PN story / NEW pressure:** PN projects GO:0032964 collagen biosynthetic process (verified real OLS). Review captures the more specific GO:0050211 procollagen galactosyltransferase activity (MF) and proposes GO:0180062 protein O-linked glycosylation via galactose as a NEW BP (replacing reliance on the downstream GO:0030199). The PN pathway context is consistent with and broader than these. Conclusion: **already captured** (review goes finer-grained); no PN-driven NEW pressure.
- **Mapping strategy:** No change. Group-node → GO:0032964 is the same defensible shared-pathway mapping as for COLGALT1/CRTAP/P3H1 in this collagen-processing group; appropriate process-level umbrella, ancestors correctly no_mapping. The review's NEW GO:0180062 would be the more precise gene-level BP but does not change the node mapping.
- **Evidence alignment:** PN row has no reference titles; review's enzymatic evidence rests mainly on PMID:19075007 and UniProt (plus high-throughput protein-binding PMIDs marked over-annotated). Collagen-biosynthesis evidence base is thinner than COLGALT1's but adequate and concordant with the mapping. No divergence.
- **Verdict:** Consistent; PN collagen-biosynthesis role already captured (more specifically) in review. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/COLGALT2/COLGALT2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: Q8IYK4
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032964 collagen biosynthetic process]
        rationale: This PN group contains ER factors dedicated to collagen maturation, processing, and folding. Collagen biosynthetic process captures the shared substrate-specific pathway context.
    - [class] ER proteostasis|Maturation and folding of specific substrates
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
