# BNIP3L PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O60238
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/BNIP3L/BNIP3L-ai-review.yaml](BNIP3L-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BNIP3L/BNIP3L-ai-review.html](BNIP3L-ai-review.html)
- Gene notes: present - [genes/human/BNIP3L/BNIP3L-notes.md](BNIP3L-notes.md)
- GOA TSV: present - [genes/human/BNIP3L/BNIP3L-goa.tsv](BNIP3L-goa.tsv)
- UniProt record: present - [genes/human/BNIP3L/BNIP3L-uniprot.txt](BNIP3L-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/BNIP3L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/BNIP3L.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BNIP3L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BNIP3L.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/BNIP3L/BNIP3L-deep-research-falcon.md](BNIP3L-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BNIP3L (NIX) is a tail-anchored, atypical BH3-containing member of the BNIP3/NIP3 family that is inserted into the mitochondrial outer membrane via its C-terminal transmembrane helix, with its N-terminal disordered region facing the cytosol. Its principal, conserved function is as a selective autophagy (mitophagy) receptor: an LC3-interacting region in the cytosolic domain binds Atg8-family proteins (LC3 and GABARAP/GABARAPL1/GABARAPL2), tethering mitochondria to the forming autophagosome and driving their programmed autophagic clearance. This is most prominent during terminal erythroid/reticulocyte maturation and other developmentally programmed or stress-induced episodes of mitochondrial turnover. NIX also participates in non-canonical mitochondrial quality control through ROS-dependent interaction with SPATA18/MIEAP, and under hypoxia it is induced by HIF and promotes pro-survival macroautophagy via its atypical BH3 domain. Although first described as a pro-apoptotic BCL-2-family protein, its effects on cell death are context-dependent and direction-dependent (it can both promote and inhibit cell death) and act largely through mitochondrial membrane permeability/necrosis rather than classical cytochrome-c/caspase apoptosis. Beyond mitochondria, NIX can independently localize to peroxisomes and act as a selective autophagy receptor for their clearance (pexophagy), broadening its cargo selectivity. NIX abundance is held in check by constitutive ubiquitin-mediated turnover: an SCF(FBXL4) ubiquitin ligase complex at the mitochondrial outer membrane, with the phosphatase PPTC7 as a cofactor, degrades NIX (and BNIP3) to restrain basal mitophagy, while hypoxia/HIF signaling induces NIX transcription. NIX is also exploited by several viruses, which hijack NIX-mediated mitophagy to degrade mitochondrial antiviral signaling components.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 23; MARK_AS_OVER_ANNOTATED: 23; MODIFY: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Consistent. PN (mitophagy receptor + BECN1-availability modulator via atypical BH3), the review, notes and Falcon deep research all agree: NIX is an OMM tail-anchored mitophagy receptor (LIR→LC3/GABARAP; PMID:20200478) that under hypoxia also promotes pro-survival macroautophagy by disrupting Bcl-2-Beclin1 (PMID:19273585). PN row 1 = review core (mitophagy); PN row 2 = review's hypoxia/BECN1 axis. No contradictions.
- **PN story / NEW pressure:** PN row-1 GO:0000423 mitophagy is correctly "supported_by_goa_regulation" — the review carries GO:1901524 regulation of mitophagy (ACCEPT, IEA) so the process is already captured. The genuine NEW pressure is the **MF**: the review proposes a new term "mitophagy receptor activity" claiming none exists. This is incorrect — **GO:0140580 "mitochondrion autophagosome adaptor activity" already exists** (def "binding activity of a molecule that brings together a mitochondrial membrane and an autophagosome during mitophagy"), exactly the LIR-tethering activity. So the MF is already captured by a real term; ADD GO:0140580 rather than a new term. BECN1-modulator (class III PI3K) row is correctly context_only (NIX modulates, is not a complex subunit).
- **Evidence alignment:** PN cites review-style titles (Marinkovic FEBS Open Bio 2021; hypoxia BH3 paper = PMID:19273585; mitophagy-initiation BST review). Review uses PMID:20200478, 19273585, 21264228, 9973195, plus FBXL4/PPTC7 turnover refs. Strong overlap on the hypoxia and receptor papers.
- **Verdict:** Consistent; mitophagy process already captured. Key finding: the review's proposed NEW "mitophagy receptor activity" term duplicates the existing **GO:0140580**. **Recommended edits:** [YAML][REF] replace the BNIP3L proposed_new_term "mitophagy receptor activity" with the existing GO:0140580 mitochondrion autophagosome adaptor activity (add as core MF, supported by PMID:20200478).

## Full Consistency Review

- **UniProt:** O60238 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE
- **PN placement:** two rows — `Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy` and `...|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 availability` ; **PN-node mapping:** Mitophagy type → mapped/ok GO:0000423 mitophagy (goa_status=supported_by_goa_regulation); BECN1-modulator path → context_only/too_broad GO:0035032 (class III PI3K complex), class → context_only GO:0016236.
- **Consistency:** Consistent. PN (mitophagy receptor + BECN1-availability modulator via atypical BH3), the review, notes and Falcon deep research all agree: NIX is an OMM tail-anchored mitophagy receptor (LIR→LC3/GABARAP; PMID:20200478) that under hypoxia also promotes pro-survival macroautophagy by disrupting Bcl-2-Beclin1 (PMID:19273585). PN row 1 = review core (mitophagy); PN row 2 = review's hypoxia/BECN1 axis. No contradictions.
- **PN story / NEW pressure:** PN row-1 GO:0000423 mitophagy is correctly "supported_by_goa_regulation" — the review carries GO:1901524 regulation of mitophagy (ACCEPT, IEA) so the process is already captured. The genuine NEW pressure is the **MF**: the review proposes a new term "mitophagy receptor activity" claiming none exists. This is incorrect — **GO:0140580 "mitochondrion autophagosome adaptor activity" already exists** (def "binding activity of a molecule that brings together a mitochondrial membrane and an autophagosome during mitophagy"), exactly the LIR-tethering activity. So the MF is already captured by a real term; ADD GO:0140580 rather than a new term. BECN1-modulator (class III PI3K) row is correctly context_only (NIX modulates, is not a complex subunit).
- **Mapping strategy:** Row-1 mitophagy projection is fine (already in GOA via regulation term). Row-2 context_only/too_broad for GO:0035032 is correct (do not assign complex membership to a modulator) — consistent with the rejected-broader precedent.
- **Evidence alignment:** PN cites review-style titles (Marinkovic FEBS Open Bio 2021; hypoxia BH3 paper = PMID:19273585; mitophagy-initiation BST review). Review uses PMID:20200478, 19273585, 21264228, 9973195, plus FBXL4/PPTC7 turnover refs. Strong overlap on the hypoxia and receptor papers.
- **Verdict:** Consistent; mitophagy process already captured. Key finding: the review's proposed NEW "mitophagy receptor activity" term duplicates the existing **GO:0140580**. **Recommended edits:** [YAML][REF] replace the BNIP3L proposed_new_term "mitophagy receptor activity" with the existing GO:0140580 mitochondrion autophagosome adaptor activity (add as core MF, supported by PMID:20200478).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/BNIP3L/BNIP3L-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Modulator of class 3 PI3K complex 1 activity | Modulator of BECN1 availability
- UniProt: O60238
- In branches: ALP
- Notes: Mitochondrial membrane protein. Inhibits RHEB, also releases BECN1 from complexes with Bcl2 or BclXL. Also is a receptor for mitophagy by binding to LC3 through an LIR domain and enhances autophagy in response to hypoxia.
- PN references (titles):
    - Atypical BH3-domains of BNIP3 and BNIP3L lead to autophagy in hypoxia (tandfonline.com)
    - A brief overview of BNIP3L/NIX receptor‐mediated mitophagy - Marinković - 2021 - FEBS Open Bio - Wiley Online Library
    - The dynamics of mitochondrial autophagy at the initiation stage | Biochemical Society Transactions | Portland Press
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 availability
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: O60238
- In branches: ALP
- Notes: Mitochondrial membrane protein. Inhibits RHEB, also releases BECN1 from complexes with Bcl2 or BclXL. Also is a receptor for mitophagy by binding to LC3 through an LIR domain and enhances autophagy in response to hypoxia.
- PN references (titles):
    - Atypical BH3-domains of BNIP3 and BNIP3L lead to autophagy in hypoxia (tandfonline.com)
    - A brief overview of BNIP3L/NIX receptor‐mediated mitophagy - Marinković - 2021 - FEBS Open Bio - Wiley Online Library
    - The dynamics of mitochondrial autophagy at the initiation stage | Biochemical Society Transactions | Portland Press
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
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
