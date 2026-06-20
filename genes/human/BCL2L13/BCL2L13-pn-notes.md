# BCL2L13 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BXK5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/BCL2L13/BCL2L13-ai-review.yaml](BCL2L13-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BCL2L13/BCL2L13-ai-review.html](BCL2L13-ai-review.html)
- Gene notes: present - [genes/human/BCL2L13/BCL2L13-notes.md](BCL2L13-notes.md)
- GOA TSV: present - [genes/human/BCL2L13/BCL2L13-goa.tsv](BCL2L13-goa.tsv)
- UniProt record: present - [genes/human/BCL2L13/BCL2L13-uniprot.txt](BCL2L13-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/BCL2L13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/BCL2L13.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BCL2L13.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BCL2L13.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/BCL2L13/BCL2L13-deep-research-falcon.md](BCL2L13-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BCL2L13 (Bcl-rambo, Mil1) is a tail-anchored mitochondrial outer-membrane protein of the BCL-2 family that contains all four BCL-2 homology motifs (BH1-BH4) plus a unique ~250-residue insertion with tandem repeats preceding its C-terminal transmembrane anchor. It is the mammalian functional homolog of the yeast mitophagy receptor Atg32: through an LC3-interacting region it binds Atg8-family proteins (LC3/GABARAP, including GABARAPL2) to recruit the autophagy machinery to mitochondria, promoting mitochondrial fragmentation and selective autophagy of mitochondria (mitophagy) independently of the canonical DRP1 fission machinery. BCL2L13 was originally described as a pro-apoptotic BCL-2 homolog whose cell-death activity, which can promote caspase-3 activation, is conferred by its membrane-anchored C-terminal region rather than its BH motifs; unlike most BCL-2-family members it does not heterodimerize with other family members. It is broadly expressed (notably in heart, placenta, pancreas and skeletal muscle) and is targeted by the Legionella pneumophila effector SidF, which neutralizes it to block host apoptosis. A short nuclear-localized splice isoform lacking the transmembrane anchor also exists.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 11; NEW: 2

## PN Consistency Summary

- **Consistency:** Consistent. PN (selective-autophagy/mitophagy receptor, Atg32 homolog binding LC3/ATG8 via LIR, induces fragmentation + Parkin-independent mitophagy), the review, notes and Falcon deep research all agree (PMID:26146385 Murakawa 2015; UniProt GABARAPL2 IntAct; PMID:36589739). PN Notes match the review description verbatim in substance.
- **PN story / NEW pressure:** PN projects GO:0000423 mitophagy as new_to_goa. The review notes UniProt/Ensembl GOA already carries GO:0000423 (IEA), but it is absent from the seeded existing_annotations — so adding the process is warranted (mild discrepancy: "new_to_goa" vs already-IEA-in-UniProt). The stronger NEW pressure is the **MF**: as with BNIP3L, the review proposes a new term "mitophagy receptor activity" stating the seeded set lacks any mitophagy MF. **GO:0140580 "mitochondrion autophagosome adaptor activity" already exists** and exactly captures the LIR-tethering activity — so the MF should be ADD GO:0140580, not a brand-new term. Conclusion: process partly captured (IEA), MF capturable by an existing real term that both PN and the review missed.
- **Evidence alignment:** PN cites the Murakawa Nat Commun mitophagy paper (=PMID:26146385) and a selective-autophagy ATG8/LIR review — both align with the review's references. Strong overlap. Deep research adds DRP1-dependent (GBM, PMID:37660127) vs DRP1-independent (Murakawa) context and MAM/Ca2+ role (PMID:39175772), none contradicting the mitophagy core.
- **Verdict:** Consistent; mitophagy process correctly added (note it is already IEA in UniProt GOA). Key finding: the review's proposed NEW "mitophagy receptor activity" duplicates existing **GO:0140580**. **Recommended edits:** [YAML][REF] replace the BCL2L13 proposed_new_term with existing GO:0140580 mitochondrion autophagosome adaptor activity (add as core MF, supported by PMID:26146385); [MAP] note GO:0000423 is already UniProt-IEA, so goa_status is closer to "already_in_goa" than "new_to_goa".

## Full Consistency Review

- **UniProt:** Q9BXK5 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy` ; **PN-node mapping:** Mitophagy type → mapped/ok_for_propagation GO:0000423 mitophagy (goa_status=new_to_goa); group/class/branch → no_mapping.
- **Consistency:** Consistent. PN (selective-autophagy/mitophagy receptor, Atg32 homolog binding LC3/ATG8 via LIR, induces fragmentation + Parkin-independent mitophagy), the review, notes and Falcon deep research all agree (PMID:26146385 Murakawa 2015; UniProt GABARAPL2 IntAct; PMID:36589739). PN Notes match the review description verbatim in substance.
- **PN story / NEW pressure:** PN projects GO:0000423 mitophagy as new_to_goa. The review notes UniProt/Ensembl GOA already carries GO:0000423 (IEA), but it is absent from the seeded existing_annotations — so adding the process is warranted (mild discrepancy: "new_to_goa" vs already-IEA-in-UniProt). The stronger NEW pressure is the **MF**: as with BNIP3L, the review proposes a new term "mitophagy receptor activity" stating the seeded set lacks any mitophagy MF. **GO:0140580 "mitochondrion autophagosome adaptor activity" already exists** and exactly captures the LIR-tethering activity — so the MF should be ADD GO:0140580, not a brand-new term. Conclusion: process partly captured (IEA), MF capturable by an existing real term that both PN and the review missed.
- **Mapping strategy:** Mitophagy type → GO:0000423 projection is appropriate for BCL2L13 (well-supported Atg32-homolog receptor). The shared-node projection is sound; this gene strengthens (does not over-broaden) the node, unlike rejected-broader precedents.
- **Evidence alignment:** PN cites the Murakawa Nat Commun mitophagy paper (=PMID:26146385) and a selective-autophagy ATG8/LIR review — both align with the review's references. Strong overlap. Deep research adds DRP1-dependent (GBM, PMID:37660127) vs DRP1-independent (Murakawa) context and MAM/Ca2+ role (PMID:39175772), none contradicting the mitophagy core.
- **Verdict:** Consistent; mitophagy process correctly added (note it is already IEA in UniProt GOA). Key finding: the review's proposed NEW "mitophagy receptor activity" duplicates existing **GO:0140580**. **Recommended edits:** [YAML][REF] replace the BCL2L13 proposed_new_term with existing GO:0140580 mitochondrion autophagosome adaptor activity (add as core MF, supported by PMID:26146385); [MAP] note GO:0000423 is already UniProt-IEA, so goa_status is closer to "already_in_goa" than "new_to_goa".
- **2026-06-18 follow-up:** Implemented the high-confidence YAML edits: added GO:0140580 mitochondrion autophagosome adaptor activity and GO:0000423 mitophagy as NEW recommendations, updated the core MF, and removed the duplicate mitophagy-receptor NTR block. Mapping goa_status cleanup remains separate.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/BCL2L13/BCL2L13-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: Q9BXK5
- In branches: ALP
- Notes: Receptor for selective autophagy. Atg32 homologue binds to LC3/ATG8 and induces mitochondrial fragmentation and mitophagy in an Parkin independent manner.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Bcl-2-like protein 13 is a mammalian Atg32 homologue that mediates mitophagy and mitochondrial fragmentation
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN path denotes selective-autophagy receptors for mitochondrial cargo. The source category is a mechanistic sub-role within mitophagy, so propagation rather than exact equivalence is the correct scope.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
