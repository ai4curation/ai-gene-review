# TXNDC12 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O95881
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TXNDC12/TXNDC12-ai-review.yaml](TXNDC12-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TXNDC12/TXNDC12-ai-review.html
- Gene notes: present - [genes/human/TXNDC12/TXNDC12-notes.md](TXNDC12-notes.md)
- GOA TSV: present - [genes/human/TXNDC12/TXNDC12-goa.tsv](TXNDC12-goa.tsv)
- UniProt record: present - [genes/human/TXNDC12/TXNDC12-uniprot.txt](TXNDC12-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TXNDC12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TXNDC12.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TXNDC12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TXNDC12.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/TXNDC12/TXNDC12-deep-research-falcon.md](TXNDC12-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: TXNDC12 (Thioredoxin domain-containing protein 12; also known as ERp18, ERp19, ERp16, and hTLP19) is a small (172 aa precursor; 146 aa mature) soluble thioredoxin- superfamily oxidoreductase resident in the endoplasmic reticulum lumen. After cleavage of an N-terminal signal peptide it is retained in the ER via a C-terminal EDEL motif. It comprises a single thioredoxin-like fold carrying an unusual CGAC redox-active active-site motif (catalytic cysteines Cys66/Cys69) with a redox potential (about -165 mV) within the range of the ER, allowing it to catalyze the formation, reduction, and isomerization of disulfide bonds in client/substrate proteins. TXNDC12 thus acts early in oxidative protein folding in the ER, promoting native disulfide bond formation, and contributes to cellular defense against prolonged ER stress, where its catalytic activity attenuates ER-stress-induced apoptosis. It is widely expressed.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 4

## PN Consistency Summary

- **Consistency:** Largely consistent with a caveat on the projected term. Review, notes, and deep research describe a small soluble ER-lumen thioredoxin-superfamily oxidoreductase with an unusual CGAC active site (Cys66/Cys69) that "catalyzes formation, reduction, and isomerization of disulfide bonds" (PMID:18628206; PMID:12761212), redox potential ~−165 mV, EDEL-retained. So it does have isomerase-type chemistry (unlike TXNDC11). GOA MF terms are GO:0019153 protein-disulfide reductase (glutathione) activity and GO:0015035 protein-disulfide reductase activity; the review core MF is GO:0015035. The PN projects GO:0003756 (isomerase).
- **PN story / NEW pressure:** Lower NEW pressure than TXNDC11 — TXNDC12 already HAS catalytic MF terms in GOA (GO:0015035, GO:0019153; verified goa.tsv), accepted in the review. PN claims GO:0003756 is new_to_goa, which is literally true (isomerase term specifically is absent), and the literature does report isomerization activity, so GO:0003756 is defensible-but-redundant given the existing reductase terms. Per OLS, GO:0003756 (isomerase) and GO:0015035 (reductase) are siblings, so GO:0003756 would ADD an activity facet rather than refine an existing one. Conclusion: already substantially captured (reductase); GO:0003756 is a defensible minor ADD, not an over-reach, since isomerase activity is experimentally reported.
- **Evidence alignment:** PN mapping-only. Review key refs: IDA PMID:12761212 (ERp18 characterization), PMID:18628206 (ERp16, isomerization + anti-apoptotic role), PMID:39696500 (vWF/thrombosis, non-core). Isomerization activity in PMID:18628206 supports the PN GO:0003756 projection.
- **Verdict:** Consistent; catalytic MF already in GOA (reductase) — PN GO:0003756 isomerase projection is a defensible, literature-supported minor ADD rather than core-missing or over-reach.

## Full Consistency Review

- **UniProt:** O95881 (ERp18/ERp19/ERp16/hTLP19) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Folding enzyme | Protein disulfide isomerases` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO=GO:0003756 protein disulfide isomerase activity (class/branch=no_mapping). Projection goa_status=new_to_goa.
- **Consistency:** Largely consistent with a caveat on the projected term. Review, notes, and deep research describe a small soluble ER-lumen thioredoxin-superfamily oxidoreductase with an unusual CGAC active site (Cys66/Cys69) that "catalyzes formation, reduction, and isomerization of disulfide bonds" (PMID:18628206; PMID:12761212), redox potential ~−165 mV, EDEL-retained. So it does have isomerase-type chemistry (unlike TXNDC11). GOA MF terms are GO:0019153 protein-disulfide reductase (glutathione) activity and GO:0015035 protein-disulfide reductase activity; the review core MF is GO:0015035. The PN projects GO:0003756 (isomerase).
- **PN story / NEW pressure:** Lower NEW pressure than TXNDC11 — TXNDC12 already HAS catalytic MF terms in GOA (GO:0015035, GO:0019153; verified goa.tsv), accepted in the review. PN claims GO:0003756 is new_to_goa, which is literally true (isomerase term specifically is absent), and the literature does report isomerization activity, so GO:0003756 is defensible-but-redundant given the existing reductase terms. Per OLS, GO:0003756 (isomerase) and GO:0015035 (reductase) are siblings, so GO:0003756 would ADD an activity facet rather than refine an existing one. Conclusion: already substantially captured (reductase); GO:0003756 is a defensible minor ADD, not an over-reach, since isomerase activity is experimentally reported.
- **Mapping strategy:** Acceptable. Catalytic, canonical PDI-family member that genuinely belongs in the "Protein disulfide isomerases" group (in contrast to TXNDC11). Group GO:0003756 projection is reasonable here. No node change needed.
- **Evidence alignment:** PN mapping-only. Review key refs: IDA PMID:12761212 (ERp18 characterization), PMID:18628206 (ERp16, isomerization + anti-apoptotic role), PMID:39696500 (vWF/thrombosis, non-core). Isomerization activity in PMID:18628206 supports the PN GO:0003756 projection.
- **Verdict:** Consistent; catalytic MF already in GOA (reductase) — PN GO:0003756 isomerase projection is a defensible, literature-supported minor ADD rather than core-missing or over-reach.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/TXNDC12/TXNDC12-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: O95881
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
