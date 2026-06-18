# CALCOCO1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9P1Z2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CALCOCO1/CALCOCO1-ai-review.yaml](CALCOCO1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CALCOCO1/CALCOCO1-ai-review.html](CALCOCO1-ai-review.html)
- Gene notes: present - [genes/human/CALCOCO1/CALCOCO1-notes.md](CALCOCO1-notes.md)
- GOA TSV: present - [genes/human/CALCOCO1/CALCOCO1-goa.tsv](CALCOCO1-goa.tsv)
- UniProt record: present - [genes/human/CALCOCO1/CALCOCO1-uniprot.txt](CALCOCO1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CALCOCO1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CALCOCO1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CALCOCO1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CALCOCO1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/CALCOCO1/CALCOCO1-deep-research-falcon.md](CALCOCO1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: CALCOCO1 (Calcium-binding and coiled-coil domain-containing protein 1; also known as CoCoA/coiled-coil coactivator and calphoglin) is a multidomain protein built from an N-terminal SKICH domain, a central CALCOCO1 domain with several coiled-coil segments, a disordered region, and a C-terminal UBZ1-type zinc finger. It is a soluble selective-autophagy cargo receptor that mediates turnover of the endoplasmic reticulum (reticulophagy/ER-phagy) and of the Golgi apparatus (Golgiphagy). In this role it binds membrane-associated ER/Golgi proteins on one side and members of the ATG8 family (LC3/GABARAP, in particular GABARAPL1 and GABARAPL2) on the other through LIR- and UIM/UDS-type interaction motifs, thereby tethering organelle fragments to the forming autophagosome. CALCOCO1 acts predominantly in the cytoplasm. Independently of autophagy, CALCOCO1 has a long-standing characterization as a nuclear transcriptional coactivator (CoCoA) that shuttles between cytoplasm and nucleus and acts as a secondary/bridging coactivator for nuclear receptors, the aryl hydrocarbon receptor, and the Wnt/beta-catenin (CTNNB1) and LEF1/TCF pathways, cooperating with p160 coactivators (GRIP1/NCOA2), p300/CBP, CARM1, and with CCAR1/MED1 (for example enhancing GATA1-driven transcription during erythroid differentiation). It has also been reported as a component of a calphoglin complex that activates inorganic pyrophosphatase and phosphoglucomutase.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 18; MARK_AS_OVER_ANNOTATED: 7; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Consistent. Deep research, notes, and review YAML all frame CALCOCO1 as a dual-function protein: (core) soluble selective-autophagy receptor for ER (reticulophagy) and Golgi (Golgiphagy) binding ATG8/GABARAP via LIR/UDS motifs; (non-core, historical) CoCoA transcriptional coactivator. The PN ERphagy mapping aligns with the review's core function. The notes explicitly flag that the autophagy-receptor role is absent from curated GOA, matching the review's GOA set (dominated by coactivator + generic protein-binding terms).
- **PN story / NEW pressure:** Strong, defensible ADD pressure for the core receptor role, which is genuinely absent from GOA. GO:0061709 reticulophagy (BP, verified real) is the PN projection and is `new_to_goa` — should be added. Review proposes NEW MF "reticulophagy receptor activity" / "Golgiphagy receptor activity"; however an existing MF term GO:0160247 autophagy cargo adaptor activity ("brings together a cargo, targeted for degradation via autophagy, to a phagophore"; verified real) plus GO:0038024 cargo receptor activity already capture this — so the bespoke MF terms over-reach as proposed-new. Recommend annotating existing GO:0160247 + GO:0061709 (and BP GO:0061709-Golgi analog if available) rather than minting new MF terms.
- **Evidence alignment:** Partial overlap. PN cites the EMBO ER-phagy paper (CALCOCO1+VAP) and an ER-phagy review; the review's foundational autophagy reference is Stefely 2020 (PMID:31971854, full_text_unavailable, statement-only) plus Golgiphagy papers PMID:38822137/39871880. The specific EMBO "CALCOCO1 acts with VAMP-associated proteins to mediate ER-phagy" paper named in the PN dossier is NOT cited by PMID in the review — a gap.
- **Verdict:** Consistent; ADD reticulophagy is warranted. Avoid minting new MF terms — existing GO:0160247 covers the receptor MF.

## Full Consistency Review

- **UniProt:** Q9P1Z2 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (thorough)
- **PN placement:** `ALP|Autophagy substrate selection|Selective autophagy receptor|ERphagy`; `...|Golgiphagy`; `UPS|Ubiquitin and UBL binding|trafficking|selective autophagy|UBZ1-type ZnF`. PN-node mappings: ERphagy type=mapped/propagation GO:0061709 reticulophagy; Golgiphagy type=no_mapping; UPS ancestors=no_mapping/context_only (GO:0140036).
- **Consistency:** Consistent. Deep research, notes, and review YAML all frame CALCOCO1 as a dual-function protein: (core) soluble selective-autophagy receptor for ER (reticulophagy) and Golgi (Golgiphagy) binding ATG8/GABARAP via LIR/UDS motifs; (non-core, historical) CoCoA transcriptional coactivator. The PN ERphagy mapping aligns with the review's core function. The notes explicitly flag that the autophagy-receptor role is absent from curated GOA, matching the review's GOA set (dominated by coactivator + generic protein-binding terms).
- **PN story / NEW pressure:** Strong, defensible ADD pressure for the core receptor role, which is genuinely absent from GOA. GO:0061709 reticulophagy (BP, verified real) is the PN projection and is `new_to_goa` — should be added. Review proposes NEW MF "reticulophagy receptor activity" / "Golgiphagy receptor activity"; however an existing MF term GO:0160247 autophagy cargo adaptor activity ("brings together a cargo, targeted for degradation via autophagy, to a phagophore"; verified real) plus GO:0038024 cargo receptor activity already capture this — so the bespoke MF terms over-reach as proposed-new. Recommend annotating existing GO:0160247 + GO:0061709 (and BP GO:0061709-Golgi analog if available) rather than minting new MF terms.
- **Mapping strategy:** PN ERphagy=mapped/propagation GO:0061709 is correct and not too broad (reticulophagy is a specific leaf process). Golgiphagy=no_mapping is the right call given Kitta 2024 (PMID:38822137) shows CALCOCO1 is NOT the dominant Golgi receptor (YIPF3/4 are) — propagating Golgiphagy would over-reach. No mapping change needed.
- **Evidence alignment:** Partial overlap. PN cites the EMBO ER-phagy paper (CALCOCO1+VAP) and an ER-phagy review; the review's foundational autophagy reference is Stefely 2020 (PMID:31971854, full_text_unavailable, statement-only) plus Golgiphagy papers PMID:38822137/39871880. The specific EMBO "CALCOCO1 acts with VAMP-associated proteins to mediate ER-phagy" paper named in the PN dossier is NOT cited by PMID in the review — a gap.
- **Verdict:** Consistent; ADD reticulophagy is warranted. Avoid minting new MF terms — existing GO:0160247 covers the receptor MF.

**Recommended edits:** [YAML] Add GO:0061709 reticulophagy (BP, involved_in) to CALCOCO1 existing/core annotations — currently new_to_goa and the validated core process. [YAML] Replace `proposed_new_terms` "reticulophagy/Golgiphagy receptor activity" with existing GO:0160247 autophagy cargo adaptor activity (and GO:0038024 cargo receptor activity) as the molecular_function for the core receptor role. [REF] Add the EMBO J "CALCOCO1 acts with VAMP-associated proteins to mediate ER-phagy" PMID (named in PN dossier) to the review references.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CALCOCO1/CALCOCO1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q9P1Z2
- In branches: ALP, UPS
- Notes: Adapter for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in ERphagy
- PN references (titles):
    - Regulatory events controlling ER-phagy - ScienceDirect
    - CALCOCO1 acts with VAMP‐associated proteins to mediate ER‐phagy | The EMBO Journal (embopress.org)
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Golgiphagy
- UniProt: Q9P1Z2
- In branches: ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Golgiphagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | selective autophagy | UBZ1-type ZnF
- UniProt: Q9P1Z2
- In branches: ALP, UPS
- Signature domains: IPR041641
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|selective autophagy|UBZ1-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a selective-autophagy or trafficking subdivision under a UPS binding context. The autophagy context is real, but this node is too indirect for automatic GO propagation.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
