# ATL3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6DD88
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1376)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATL3/ATL3-ai-review.yaml](ATL3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATL3/ATL3-ai-review.html](ATL3-ai-review.html)
- Gene notes: present - [genes/human/ATL3/ATL3-notes.md](ATL3-notes.md)
- GOA TSV: present - [genes/human/ATL3/ATL3-goa.tsv](ATL3-goa.tsv)
- UniProt record: present - [genes/human/ATL3/ATL3-uniprot.txt](ATL3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATL3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATL3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATL3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATL3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATL3/ATL3-deep-research-falcon.md](ATL3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATL3 encodes atlastin-3, a multi-pass endoplasmic reticulum membrane dynamin-like GTPase. The protein acts on ER tubules and three-way junctions, where GTP binding, hydrolysis, and transient atlastin dimerization drive homotypic ER membrane fusion and maintain the branched tubular ER network. Pathogenic ATL3 variants disrupt ER network organization and are associated with hereditary sensory neuropathy.
- Existing/core annotation action counts: ACCEPT: 33; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** Internally consistent. Deep research (Falcon) and review YAML both center ATL3 on GTP-dependent homotypic ER membrane fusion / tubular-ER maintenance; both treat the ER-phagy receptor role as unsettled. The notes explicitly document the PN reticulophagy projection and the reasoned decision NOT to add it, quoting Bryce 2023 framing ER-phagy as "possible" context. No contradictions.
- **PN story / NEW pressure:** PN asserts ATL3 as an ERphagy receptor → GO:0061709 reticulophagy, which is NOT in existing GOA and is a real term. The review correctly declined to ADD it: the ATL3-specific evidence supports ER fusion/morphology, and the GABARAP-interaction/ER-phagy receptor claim (Chen 2019, not cited in YAML) is not anchored to a cached supporting quote. Verdict: PN story over-reaches as a confident GO assertion; appropriately held as suggested question/experiment rather than a NEW annotation.
- **Evidence alignment:** Divergent. PN cites review-style titles (Chen 2019 ATL3 ER-phagy receptor; Liu/atlastin-ULK1 JCB) not present in the review's PMID set. Review is built on fusion/structure papers (PMID:37102997, 27619977, 28602821, 24459106). No PMID overlap on the ER-phagy claim → the projection is unsupported within the dossier's own citations.
- **Verdict:** Consistent; PN reticulophagy claim correctly NOT added (over-reaches gene-level evidence). No edits required.

## Full Consistency Review

- **UniProt:** Q6DD88 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagy substrate selection|Selective autophagy receptor|ERphagy` (also `...|Autophagophore initiation and elongation|ULK1 pathway, direct|Modulator of ULK1 activity`) ; **PN-node mapping:** type-leaf `mapped`, `ok_for_propagation_to_go` → GO:0061709 reticulophagy (verified real, OLS); ULK1 leaf `no_mapping`.
- **Consistency:** Internally consistent. Deep research (Falcon) and review YAML both center ATL3 on GTP-dependent homotypic ER membrane fusion / tubular-ER maintenance; both treat the ER-phagy receptor role as unsettled. The notes explicitly document the PN reticulophagy projection and the reasoned decision NOT to add it, quoting Bryce 2023 framing ER-phagy as "possible" context. No contradictions.
- **PN story / NEW pressure:** PN asserts ATL3 as an ERphagy receptor → GO:0061709 reticulophagy, which is NOT in existing GOA and is a real term. The review correctly declined to ADD it: the ATL3-specific evidence supports ER fusion/morphology, and the GABARAP-interaction/ER-phagy receptor claim (Chen 2019, not cited in YAML) is not anchored to a cached supporting quote. Verdict: PN story over-reaches as a confident GO assertion; appropriately held as suggested question/experiment rather than a NEW annotation.
- **Mapping strategy:** Gene does not change the node mapping; the type-leaf `mapped`/`ok_for_propagation` stands as a class-level statement, but this individual gene is a defensible decline (like TOMM20/HSPA8 precedent where projection out-reaches gene evidence). Projected term is narrower than review scope only in that review omits it entirely.
- **Evidence alignment:** Divergent. PN cites review-style titles (Chen 2019 ATL3 ER-phagy receptor; Liu/atlastin-ULK1 JCB) not present in the review's PMID set. Review is built on fusion/structure papers (PMID:37102997, 27619977, 28602821, 24459106). No PMID overlap on the ER-phagy claim → the projection is unsupported within the dossier's own citations.
- **Verdict:** Consistent; PN reticulophagy claim correctly NOT added (over-reaches gene-level evidence). No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATL3/ATL3-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ULK1 pathway, direct | Modulator of ULK1 activity
- UniProt: Q6DD88
- In branches: ALP
- Notes: Receptor for selective autophagy. ATL3 specifically binds to GABARAP via 2 GABARAP interaction motifs (GIMs). An ER-phagy receptor that promotes tubular ER degradation. Also ATL2/3 directly interact with ULK1 and ATG13 and facilitate the ATG13-mediated recruitment/stabilization of ULK1 and ATG101.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Atlastin 2/3 regulate ER targeting of the ULK1 complex to initiate autophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - ATL3 Is a Tubular ER-Phagy Receptor for GABARAP-Mediated Selective Autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ULK1 pathway, direct|Modulator of ULK1 activity
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups diverse regulators placed around ULK1 activity, but the current members span phosphatase regulation, stress signaling, vesicle/lysosome biology, and proteostasis context rather than a single reusable GO term for ULK1 modulation.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ULK1 pathway, direct
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q6DD88
- In branches: ALP
- Notes: Receptor for selective autophagy. ATL3 specifically binds to GABARAP via 2 GABARAP interaction motifs (GIMs). An ER-phagy receptor that promotes tubular ER degradation. Also ATL2/3 directly interact with ULK1 and ATG13 and facilitate the ATG13-mediated recruitment/stabilization of ULK1 and ATG101.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Atlastin 2/3 regulate ER targeting of the ULK1 complex to initiate autophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - ATL3 Is a Tubular ER-Phagy Receptor for GABARAP-Mediated Selective Autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN uses the community label ERphagy for selective autophagy of the endoplasmic reticulum, while GO uses the synonym reticulophagy. Receptor members of this PN category are suitable for propagation to the GO reticulophagy process.
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
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
