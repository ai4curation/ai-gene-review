# GBA1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P04062
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GBA1/GBA1-ai-review.yaml](GBA1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GBA1/GBA1-ai-review.html](GBA1-ai-review.html)
- Gene notes: present - [genes/human/GBA1/GBA1-notes.md](GBA1-notes.md)
- GOA TSV: present - [genes/human/GBA1/GBA1-goa.tsv](GBA1-goa.tsv)
- UniProt record: present - [genes/human/GBA1/GBA1-uniprot.txt](GBA1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GBA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GBA1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GBA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GBA1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GBA1 encodes lysosomal acid glucosylceramidase, a LIMP-2/SCARB2-trafficked lysosomal enzyme that hydrolyzes glucosylceramide to ceramide and glucose. Its core function is lysosomal glycosphingolipid catabolism at the lumenal side of the lysosomal membrane. Loss of GCase activity also impairs autophagic lysosome reformation, lysosomal recycling, and alpha-synuclein/lysosomal proteostasis in disease models, while cholesterol glucosylation, steryl-beta-glucoside hydrolysis, ceramide salvage, and inflammatory signaling are supported non-core contexts.
- Existing/core annotation action counts: ACCEPT: 33; KEEP_AS_NON_CORE: 38; MARK_AS_OVER_ANNOTATED: 15; MODIFY: 10

## PN Consistency Summary

- **Consistency:** Excellent — the best-aligned of the set. Deep-research, review, PN, and mapping converge: core function is lysosomal acid glucosylceramidase (GO:0004348; LIMP-2/SCARB2-trafficked), and the ALR/Parkinson axis is a genuine but downstream/mechanism-unknown consequence of GCase loss. The review's handling (GO:0007040 lysosome organization; regulation of macroautophagy; "current GO lacks an autophagic lysosome reformation term") mirrors the PN node's `context_only`→GO:0007040 + "function unknown"→`no_mapping` exactly. No contradictions.
- **PN story / NEW pressure:** The PN's ALR placement asserts a role not captured by an exact GO term — and the review correctly recognizes this. OLS confirms there is NO existing GO term "autophagic lysosome reformation" (only GO:0061739 = "protein lipidation involved in autophagosome assembly", unrelated). The review already mints the right response: `proposed_new_terms` includes "autophagic lysosome reformation" (parent GO:0007040) — **candidate, correctly unverified/new** — plus "lysosomal glucosylceramide catabolic process" (parent GO:0006680). No fabricated existing term used. **Already captured (proposed_new_terms + suggested_questions); no further ADD warranted.**
- **Evidence alignment:** Strong overlap. PN cites the ALR paper (Magalhaes et al., HMG 2016) = **PMID:27378698 (verified via PubMed, DOI 10.1093/hmg/ddw185)**, and the review cites the SAME PMID:27378698 for ALR (in core_functions, the GO:0007040 annotation, and the proposed ALR term). PN's other refs (Schröder lysosome proteome; hLGDB) are localization/database context not needed by the review.
- **Verdict:** Fully consistent; exemplary handling of a "GO-gap" PN node (proposed NEW term instead of forcing an existing one), with matching primary evidence. **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** P04062 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP → Lysosomal catabolism → Lysosomal lipid catabolism → Lysosomal sphingomyelin/ceramide metabolism → Lysosomal ceramidase` AND `ALP → Autophagic lysosome reformation → Specific function in autophagic lysosome reformation unknown` (2 rows)
- **PN-node mapping:** ceramidase subtype/type = `no_mapping` (mixed ASAH1/GALC/GBA1 bucket; no safe shared ceramidase term); lipid-catabolism group = `context_only` → GO:0016042; catabolism class = `no_mapping`; ALR class = `context_only`/`too_broad` → GO:0007040 lysosome organization; ALR group ("function unknown") = `no_mapping`; branch `no_mapping`.
- **Consistency:** Excellent — the best-aligned of the set. Deep-research, review, PN, and mapping converge: core function is lysosomal acid glucosylceramidase (GO:0004348; LIMP-2/SCARB2-trafficked), and the ALR/Parkinson axis is a genuine but downstream/mechanism-unknown consequence of GCase loss. The review's handling (GO:0007040 lysosome organization; regulation of macroautophagy; "current GO lacks an autophagic lysosome reformation term") mirrors the PN node's `context_only`→GO:0007040 + "function unknown"→`no_mapping` exactly. No contradictions.
- **PN story / NEW pressure:** The PN's ALR placement asserts a role not captured by an exact GO term — and the review correctly recognizes this. OLS confirms there is NO existing GO term "autophagic lysosome reformation" (only GO:0061739 = "protein lipidation involved in autophagosome assembly", unrelated). The review already mints the right response: `proposed_new_terms` includes "autophagic lysosome reformation" (parent GO:0007040) — **candidate, correctly unverified/new** — plus "lysosomal glucosylceramide catabolic process" (parent GO:0006680). No fabricated existing term used. **Already captured (proposed_new_terms + suggested_questions); no further ADD warranted.**
- **Mapping strategy:** No change. Including GBA1 does not alter the node: the ALR group is rightly `no_mapping` ("function unknown"), the class rightly `context_only`→GO:0007040 (broader than GBA1's enzymatic core), and the ceramidase bucket rightly `no_mapping` (GBA1 is a glucosylceramidase, not a ceramidase — the PN's mixed ASAH1/GALC/GBA1 grouping is appropriately not propagated). PN-projected GO:0007040 is broader than the review's enzyme-level core, so non-propagation is the right call (cf. rejected broader projections).
- **Evidence alignment:** Strong overlap. PN cites the ALR paper (Magalhaes et al., HMG 2016) = **PMID:27378698 (verified via PubMed, DOI 10.1093/hmg/ddw185)**, and the review cites the SAME PMID:27378698 for ALR (in core_functions, the GO:0007040 annotation, and the proposed ALR term). PN's other refs (Schröder lysosome proteome; hLGDB) are localization/database context not needed by the review.
- **Verdict:** Fully consistent; exemplary handling of a "GO-gap" PN node (proposed NEW term instead of forcing an existing one), with matching primary evidence. **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/GBA1/GBA1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Lysosomal catabolism | Lysosomal lipid catabolism | Lysosomal sphingomyelin/ceramide metabolism | Lysosomal ceramidase
- UniProt: P04062
- In branches: ALP
- Notes: Catabolic enzyme of the lysosome, per Gene ontology. Also autophagic lysosomal reformation is impaired in GBA1 mutants, potentially increasing susceptibility to Parkinson's Disease.
- PN references (titles):
    - Autophagic lysosome reformation dysfunction in glucocerebrosidase deficient cells: relevance to Parkinson disease | Human Molecular Genetics | Oxford Academic (oup.com)
    - The proteome of lysosomes - Schröder - 2010 - PROTEOMICS - Wiley Online Library
    - hLGDB: a database of human lysosomal genes and their regulation | Database | Oxford Academic (oup.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Lysosomal lipid catabolism|Lysosomal sphingomyelin/ceramide metabolism|Lysosomal ceramidase
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed lysosomal ceramide/glycosylceramide hydrolase bucket containing ASAH1, GALC, and GBA1. The current GO cache lacks a non-obsolete ceramidase term that safely covers all members, so no direct universal mapping is made.
    - [type] Autophagy-Lysosome Pathway|Lysosomal catabolism|Lysosomal lipid catabolism|Lysosomal sphingomyelin/ceramide metabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed sphingomyelin/ceramide metabolism container. The child leaves include enzymes and activators with different molecular functions, so direct propagation from the container would lose specificity.
    - [group] Autophagy-Lysosome Pathway|Lysosomal catabolism|Lysosomal lipid catabolism
        status=context_only scope=too_broad_to_propagate GO=[GO:0016042 lipid catabolic process]
        rationale: This group is a lysosomal lipid-catabolism context, but it mixes lipases, phospholipases, sphingolipid enzymes, and activators. Specific molecular functions are mapped at narrower leaves.
    - [class] Autophagy-Lysosome Pathway|Lysosomal catabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad lysosomal-degradation container. The subtree includes carbohydrate, lipid, protein, nuclease, phosphatase, sulfatase, and environment-regulation roles, so mapping should occur at the enzyme or process subtype level.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Specific function in autophagic lysosome reformation unknown
- UniProt: P04062
- In branches: ALP
- Notes: Catabolic enzyme of the lysosome, per Gene ontology. Also autophagic lysosomal reformation is impaired in GBA1 mutants, potentially increasing susceptibility to Parkinson's Disease.
- PN references (titles):
    - Autophagic lysosome reformation dysfunction in glucocerebrosidase deficient cells: relevance to Parkinson disease | Human Molecular Genetics | Oxford Academic (oup.com)
    - The proteome of lysosomes - Schröder - 2010 - PROTEOMICS - Wiley Online Library
    - hLGDB: a database of human lysosomal genes and their regulation | Database | Oxford Academic (oup.com)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Specific function in autophagic lysosome reformation unknown
        status=no_mapping scope= GO=[]
        rationale: This PN group explicitly states that the specific role within autophagic lysosome reformation is unknown. That makes GO propagation unsafe until a narrower mechanistic interpretation is available.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
