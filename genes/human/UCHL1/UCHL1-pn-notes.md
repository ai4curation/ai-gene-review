# UCHL1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P09936
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UCHL1/UCHL1-ai-review.yaml](UCHL1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UCHL1/UCHL1-ai-review.html](UCHL1-ai-review.html)
- Gene notes: present - [genes/human/UCHL1/UCHL1-notes.md](UCHL1-notes.md)
- GOA TSV: present - [genes/human/UCHL1/UCHL1-goa.tsv](UCHL1-goa.tsv)
- UniProt record: present - [genes/human/UCHL1/UCHL1-uniprot.txt](UCHL1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UCHL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UCHL1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UCHL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UCHL1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UCHL1 encodes ubiquitin carboxyl-terminal hydrolase isozyme L1, a cytosolic cysteine-type deubiquitinase/omega peptidase that hydrolyzes small ubiquitin C-terminal adducts and helps maintain monoubiquitin pools for ubiquitin-dependent proteostasis. UCHL1 also has substrate- and context-specific roles in LC3/autophagy regulation, alpha-2A adrenergic receptor/MAPK signaling, HIF-1alpha stabilization, glycolysis-linked Parkinson disease models, and Parkin interaction; these are supported non-core contexts rather than replacements for the core UCH activity.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 9; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Consistent. Deep research, review, and PN agree the core function is cysteine-type DUB / ubiquitin C-terminal hydrolase activity (GO:0004843) acting in protein deubiquitination (GO:0016579), with a substrate/context-specific LC3/autophagy branch. The review treats LC3/autophagy (GO:0016241 regulation of macroautophagy) as KEEP_AS_NON_CORE, matching the PN's "inhibits autophagosome formation through DUB activity" framing.
- **PN story / NEW pressure:** The ALP node "Deubiquitination of ATG8 homologs" describes a function GO cannot express specifically — the review proposes a NEW term **"ATG8-family protein deubiquitination"** (parent GO:0016579), justified by PMID:29462615. OLS search returns no existing GO term for ATG8/LC3 deubiquitination, so this is a genuine candidate (verified absent). Verdict: the ATG8-DUB story is real but only loosely captured by broad GO:0016579 today; defensible NEW candidate (unverified as an existing term, correctly proposed not asserted).
- **Evidence alignment:** PN ALP cites PMID:29462615 (UCHL1 inhibits autophagosome formation via DUB) — present in the review supporting the autophagy non-core annotation. PN UPS row is domain-based (IPR001578), matched by the review's deep enzymology set (PMID:9521656, 8639624, 16475834, 20439756, 23359680). Good overlap.
- **Verdict:** Consistent; the only actionable item is the proposed ATG8-family-deubiquitination NEW term (candidate, no existing GO equivalent) and the GO:0101005-vs-GO:0004843 granularity note.

## Full Consistency Review

- **UniProt:** P09936 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** ALP `…|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs` + UPS `DUBs and UBL demodifiers|UCH` ; **PN-node mapping:** ALP type mapped GO:0016579 protein deubiquitination (already_in_goa_exact); UPS group mapped GO:0101005 deubiquitinase activity (entailed_by_goa_closure).
- **Consistency:** Consistent. Deep research, review, and PN agree the core function is cysteine-type DUB / ubiquitin C-terminal hydrolase activity (GO:0004843) acting in protein deubiquitination (GO:0016579), with a substrate/context-specific LC3/autophagy branch. The review treats LC3/autophagy (GO:0016241 regulation of macroautophagy) as KEEP_AS_NON_CORE, matching the PN's "inhibits autophagosome formation through DUB activity" framing.
- **PN story / NEW pressure:** The ALP node "Deubiquitination of ATG8 homologs" describes a function GO cannot express specifically — the review proposes a NEW term **"ATG8-family protein deubiquitination"** (parent GO:0016579), justified by PMID:29462615. OLS search returns no existing GO term for ATG8/LC3 deubiquitination, so this is a genuine candidate (verified absent). Verdict: the ATG8-DUB story is real but only loosely captured by broad GO:0016579 today; defensible NEW candidate (unverified as an existing term, correctly proposed not asserted).
- **Mapping strategy:** This gene does not change the node scope. PN maps the ALP type to the broad parent GO:0016579 because no ATG8-specific term exists — consistent with the review. Minor mismatch: PN's UPS group projects GO:0101005 deubiquitinase activity, whereas GOA/review use the child GO:0004843 cysteine-type deubiquitinase activity; entailed_by_goa_closure correctly reflects that GO:0004843 entails GO:0101005, so no conflict.
- **Evidence alignment:** PN ALP cites PMID:29462615 (UCHL1 inhibits autophagosome formation via DUB) — present in the review supporting the autophagy non-core annotation. PN UPS row is domain-based (IPR001578), matched by the review's deep enzymology set (PMID:9521656, 8639624, 16475834, 20439756, 23359680). Good overlap.
- **Verdict:** Consistent; the only actionable item is the proposed ATG8-family-deubiquitination NEW term (candidate, no existing GO equivalent) and the GO:0101005-vs-GO:0004843 granularity note.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/UCHL1/UCHL1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, direct | Deubiquitination of ATG8 homologs
- UniProt: P09936
- In branches: ALP, UPS
- Notes: Deubiquitinase that interacts with LC3 proteins to inhibit autophagosome formation
- PN references (titles):
    - Ubiquitin C-Terminal Hydrolase L1 regulates autophagy by inhibiting autophagosome formation through its deubiquitinating enzyme activity - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016579 protein deubiquitination]
        rationale: This PN type denotes deubiquitination of ATG8-family proteins within the autophagy pathway. GO does not currently provide an ATG8-specific deubiquitination term, so the defensible target is the broader parent process protein deubiquitination.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | DUBs and UBL demodifiers | UCH
- UniProt: P09936
- In branches: ALP, UPS
- Signature domains: IPR001578
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|UCH
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN group is an active deubiquitinase family bucket. The shared molecular-function assertion is deubiquitinase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0016579 protein deubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UCH

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
