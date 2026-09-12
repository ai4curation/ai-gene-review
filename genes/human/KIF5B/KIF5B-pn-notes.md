# KIF5B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P33176
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/KIF5B/KIF5B-ai-review.yaml](KIF5B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/KIF5B/KIF5B-ai-review.html](KIF5B-ai-review.html)
- Gene notes: present - [genes/human/KIF5B/KIF5B-notes.md](KIF5B-notes.md)
- GOA TSV: present - [genes/human/KIF5B/KIF5B-goa.tsv](KIF5B-goa.tsv)
- UniProt record: present - [genes/human/KIF5B/KIF5B-uniprot.txt](KIF5B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/KIF5B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/KIF5B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/KIF5B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/KIF5B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: KIF5B encodes the ubiquitous kinesin-1 heavy chain, an ATP-dependent, plus-end-directed microtubule motor. Its core molecular role is to form kinesin-1 motor complexes that bind microtubules and move vesicles and organelles toward microtubule plus ends. KIF5B is recruited to many cargos through adaptors, including Arl8/SKIP-dependent lysosome positioning, lytic granule polarization in natural killer cells, mitochondrial transport, neuronal cargo transport, centrosome/nuclear positioning, and channel trafficking. Its lysosomal role is kinesin-dependent lysosome localization/positioning through adaptor-mediated cargo recruitment.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 36; MARK_AS_OVER_ANNOTATED: 19; MODIFY: 12

## PN Consistency Summary

- **Consistency:** Mutually consistent. Deep research, review YAML, PN notes, and node mapping all describe a kinesin-1 heavy-chain motor recruited (Arl8/SKIP) to position lysosomes. The single projected term GO:0032418 is present in the review as IMP/KEEP_AS_NON_CORE (PMID:22172677), matching `already_in_goa_exact`. No contradictions.
- **PN story / NEW pressure:** The PN ALR/lysosomal-tubulation story (KIF5B pulling autolysosome tubules via PI(4,5)P2) goes beyond current GO, but the node itself is `context_only/too_broad` and projects nothing. Review explicitly declines to add a lysosome-organization/ALR term, noting the tubulation evidence is not KIF5B-specific enough. Conclusion: already captured (lysosome localization); ALR role over-reaches for a new term now — correctly deferred to expert question.
- **Evidence alignment:** PN cites Cheng/Schiefermeier-type ALR reviews + the KIF5B lysosome-distribution paper; review anchors the same biology to PMID:22172677 (Arl8/SKIP) and PMID:24088571 (Arl8b/NK granules). PN's ALR review titles are not cited as PMIDs in the review, but the substantive lysosome-positioning evidence overlaps.
- **Verdict:** Consistent and well-scoped; PN ALR story noted but correctly not propagated. No edits required.

## Full Consistency Review

- **UniProt:** P33176 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Localization of the lysosome` (row 1) and `ALP|Autophagic lysosome reformation|Lysosomal tubulation` (row 2) ; **PN-node mapping:** row1 group `mapped / ok_for_propagation / GO:0032418 lysosome localization`; row2 group+class `context_only / too_broad_to_propagate / GO:0007040 lysosome organization`.
- **Consistency:** Mutually consistent. Deep research, review YAML, PN notes, and node mapping all describe a kinesin-1 heavy-chain motor recruited (Arl8/SKIP) to position lysosomes. The single projected term GO:0032418 is present in the review as IMP/KEEP_AS_NON_CORE (PMID:22172677), matching `already_in_goa_exact`. No contradictions.
- **PN story / NEW pressure:** The PN ALR/lysosomal-tubulation story (KIF5B pulling autolysosome tubules via PI(4,5)P2) goes beyond current GO, but the node itself is `context_only/too_broad` and projects nothing. Review explicitly declines to add a lysosome-organization/ALR term, noting the tubulation evidence is not KIF5B-specific enough. Conclusion: already captured (lysosome localization); ALR role over-reaches for a new term now — correctly deferred to expert question.
- **Mapping strategy:** No change. The `mapped` lysosome-localization node and the two `context_only` lysosome-organization nodes are appropriately scoped; KIF5B does not push the ALR node toward propagation (parallels TOMM20/RAB7A "broader, rejected").
- **Evidence alignment:** PN cites Cheng/Schiefermeier-type ALR reviews + the KIF5B lysosome-distribution paper; review anchors the same biology to PMID:22172677 (Arl8/SKIP) and PMID:24088571 (Arl8b/NK granules). PN's ALR review titles are not cited as PMIDs in the review, but the substantive lysosome-positioning evidence overlaps.
- **Verdict:** Consistent and well-scoped; PN ALR story noted but correctly not propagated. No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/KIF5B/KIF5B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Localization of the lysosome
- UniProt: P33176
- In branches: ALP
- Notes: A kinesin. Regulates lysosome positioning in the cell, so involved in autophagosome-lysosome fusion. Knockdown leads to autophagosome accumulation near the Golgi and peripheral accumulation of lysosomes. Also drives the formation of tubules from autolysosomes during ALR by binding to PI(4,5)P2 enriched microdomains.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Depletion of Kinesin 5B Affects Lysosomal Distribution and Stability and Induces Peri-Nuclear Accumulation of Autophagosomes in Cancer Cells (plos.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the lysosome
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032418 lysosome localization]
        rationale: This group is explicitly about lysosome positioning in late autophagy. Lysosome localization is the correct propagation target rather than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Lysosomal tubulation
- UniProt: P33176
- In branches: ALP
- Notes: A kinesin. Regulates lysosome positioning in the cell, so involved in autophagosome-lysosome fusion. Knockdown leads to autophagosome accumulation near the Golgi and peripheral accumulation of lysosomes. Also drives the formation of tubules from autolysosomes during ALR by binding to PI(4,5)P2 enriched microdomains.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Depletion of Kinesin 5B Affects Lysosomal Distribution and Stability and Induces Peri-Nuclear Accumulation of Autophagosomes in Cancer Cells (plos.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Lysosomal tubulation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: This PN group specifically captures the tubulation and membrane-remodeling step that regenerates lysosomes from autolysosomes. That aligns better to lysosome organization than to generic autophagy, but the current member set mixes factors annotated in GO to lysosome localization and phagosome/lysosome fusion rather than a clean shared lysosome-organization process role, so propagation would overstate the evidence.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0032418 lysosome localization | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the lysosome

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
