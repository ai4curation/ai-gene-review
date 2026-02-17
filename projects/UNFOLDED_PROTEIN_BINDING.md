---
species: [human, mouse, yeast, SCHPO, DROME, DANRE, ARATH, "..."]
---
# Unfolded Protein Binding Annotation Review

> **Editor Brief (as of 2026-02-14, revised after full cross-species audit):**
> GO:0051082 "unfolded protein binding" and GO:0031249 "denatured protein binding" are proposed
> for obsoletion ([go-ontology#30962](https://github.com/geneontology/go-ontology/issues/30962)).
> We reviewed **all 148 unique genes** (33 human + 115 non-human across 17 species) carrying
> experimental annotations to these terms — **5,529 total annotations, 0 PENDING**. Each gene's
> GO:0051082/GO:0031249 annotation was reclassified to a mechanism-specific MF term.
> The 33 human genes provide the primary evidence base with full literature review (see
> [Human Gene Checklist](#human-gene-checklist)); the 115 non-human genes validate that the
> same decision rules apply consistently across all species (see
> [Cross-Species Completeness Audit](#cross-species-completeness-audit)).
> **Critical finding**: GO:0140309 "unfolded protein carrier activity"
> was created specifically for TIM carrier-holdases ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552))
> and does **not** fit in-situ holdases (crystallins, sHSPs, CLU). A general "holdase chaperone
> activity" term was discussed in #30552 but never created — this is now the primary NTR needed.
> **Decisions from GO editors are needed on**: (1) NTR for general holdase chaperone activity
> (non-carrier), (2) whether "misfolded protein sensor activity" should be created for E3
> ligases/F-box proteins, (3) how to annotate J-domain co-chaperone MF given that GO:0003767
> "co-chaperone activity" is obsolete, and (4) whether GO:0051082 obsoletion should be blocked
> until the holdase NTR exists. Detailed review YAMLs are in `genes/<SPECIES>/<GENE>/`.
> Validate with: `just validate-all` (writes `reports/validation-all.tsv`).

## Terminology

These mechanism classes are used throughout this document:

| Term | GO term | Definition | ATP? | Example |
|------|---------|-----------|------|---------|
| **Foldase** | GO:0044183 protein folding chaperone | Actively assists protein folding through iterative binding/release cycles | Yes | GroEL/ES, TRiC/CCT |
| **Holdase** | *(NTR needed: holdase chaperone activity)* | Binds unfolded/misfolded proteins to prevent aggregation in situ; does not actively refold or transport between compartments | No | CRYAB (alpha-crystallin), CLU |
| **Carrier-holdase** | GO:0140309 unfolded protein carrier activity | Binds unfolded protein and escorts it between cellular components, preventing aggregation in transit | No | Tim9-Tim10, Tim8-Tim13 (small TIMs) |
| **Foldase/holdase** | GO:0044183 + holdase NTR | Context-dependent: can function as foldase or holdase depending on conditions, clients, de novo vs quality control | Yes | HSPA1A (HSP70) |
| **Co-chaperone** | *(see [co-chaperone note](#co-chaperone-note))* | Binds to chaperone to activate its ATPase and/or deliver substrates; does not independently fold proteins | N/A | DNAJB1 (J-domain), AHSA1 (HSP90 activator) |
| **Disaggregase** | GO:0140545 | Solubilizes existing protein aggregates | Yes | HSPA1A (with DNAJ + HSPH1) |
| **Sensor** | *(proposed: misfolded protein sensor activity)* | Recognizes misfolded proteins as substrates for degradation (E3 ligase, lectin) | N/A | SYVN1 (HRD1), UGGT1 |

## Decision Rules

How GO:0051082 annotations were reclassified:

| Mechanism | Action | Replacement term | Rationale | Example |
|-----------|--------|-----------------|-----------|---------|
| Foldase (strictly: GroEL/ES, TRiC) | MODIFY | GO:0044183 protein folding chaperone | Active ATP-dependent folding; strictly foldase proteins | PFDN1 (delivers to TRiC) |
| Foldase/holdase (HSP70 family) | MODIFY | GO:0044183 protein folding chaperone | HSP70 functions as foldase or holdase depending on context (conditions, clients, de novo vs quality control); curators should review per experimental evidence. Holdase aspect awaits [holdase NTR](#holdase-annotation-gap) | HSPA1A, HSPA8 |
| Co-chaperone, J-domain | MODIFY | GO:0044183 *(interim, see [co-chaperone note](#co-chaperone-note))* | J-domain proteins are substrate adaptors and HSP70 ATPase activators, not independent foldases; GO:0044183 used as interim since GO:0003767 "co-chaperone activity" is obsolete | DNAJB1, DNAJA2 |
| Co-chaperone, J-domain holdase | MODIFY | holdase NTR *(retain GO:0051082 until NTR created)* | J-domain proteins with independent holdase activity (aggregation suppression, no refolding). GO:0140309 is carrier-specific and does not fit; see [holdase annotation gap](#holdase-annotation-gap) | DNAJB6, DNAJB8 |
| Holdase (sHSP, crystallin, CLU) | MODIFY | holdase NTR *(retain GO:0051082 until NTR created)* | ATP-independent in-situ aggregation prevention. GO:0140309 does not fit — it was created for carrier-holdases (TIM chaperones); see [holdase annotation gap](#holdase-annotation-gap) | CRYAA, HSPB6, CLU |
| Disaggregase (HSP70 subset) | MODIFY | GO:0140545 ATP-dependent protein disaggregase activity | Distinct disaggregation activity | HSPA1A, HSPA1B, HSPA8 |
| Co-chaperone NEF (GrpE-like) | REMOVE | *(none — not direct UPB)* | Regulates HSP70 nucleotide cycle, does not bind unfolded substrate directly | GRPEL1 |
| ER/quality control sensor | REMOVE or MARK_AS_OVER_ANNOTATED | *(none — not chaperones)* | Substrate recognition for ligase/GT, not chaperoning | SYVN1, ERLEC1, UGGT1 |
| HSP90 co-chaperone | MARK_AS_OVER_ANNOTATED | *(none — co-chaperone, not UPB)* | These assist HSP90, not direct unfolded protein binding. AHSA1 is an HSP90 ATPase activator; PTGES3 mechanism less clear (activator? substrate adaptor?) | AHSA1, PTGES3, TMEM67 |
| Other specific MF | MODIFY | Gene-specific term | Function better captured by existing GO term | NPM1 → GO:0140713, AIP → GO:0051879 |

## Impact Summary

Primary GO:0051082 reclassification decisions (mutually exclusive; 33 unique human genes).
Cross-species audit (115 non-human genes) confirms the same mechanism classes apply
universally — see [Cross-Species Completeness Audit](#cross-species-completeness-audit).

| Primary action | Count | Notes |
|--------|-------|-------------------|
| MODIFY → GO:0044183 (foldase) | 16 | HSP70 family (6), J-domain co-chaperones as interim (4), prefoldin (6, incl. VBP1) — note: HSP70 holdase aspect awaits holdase NTR |
| MODIFY → holdase NTR (pending) | 7 | sHSPs/crystallins (3), CLU, SCG5, DNAJB6, DNAJB8 — retain GO:0051082 until NTR created. Also HSPH1 (non-human, not in 33 count). See [holdase annotation gap](#holdase-annotation-gap) |
| MODIFY → other specific MF | 2 | NPM1 (GO:0140713), AIP (GO:0051879) |
| MARK_AS_OVER_ANNOTATED | 5 | Sensor/co-chaperone cases where UPB overstates direct activity |
| REMOVE | 3 | SYVN1, ERLEC1, GRPEL1 |
| **Total** | **33** | |

Additional non-exclusive co-annotations:

| Additional term | Count | Genes |
|--------|-------|-------------------|
| GO:0140545 ATP-dependent protein disaggregase activity | 3 | HSPA1A, HSPA1B, HSPA8 |

> **Note on counts**: Some genes may need dual foldase+holdase annotation (e.g. HSP70 family)
> depending on experimental context. J-domain co-chaperone counts use GO:0044183 as interim
> pending editor guidance on co-chaperone MF representation. 7 holdase genes cannot be properly
> reannotated until a general holdase NTR is created — GO:0051082 obsoletion should be blocked
> on this.

## Before/After Examples

| Gene | Old annotation | New annotation | Evidence | Rationale |
|------|---------------|----------------|----------|-----------|
| HSPA1A | GO:0051082 unfolded protein binding (IDA, PMID:21231916) | GO:0044183 protein folding chaperone (foldase) + GO:0140545 disaggregase | IDA | HSP70 is an ATP-dependent foldase; also disaggregates with DNAJ/HSPH1. Holdase aspect awaits holdase NTR |
| CRYAB | GO:0051082 unfolded protein binding (IDA, PMID:20159986) | holdase NTR *(retain GO:0051082 until created)* | IDA | sHSP holdase; prevents aggregation in situ without active refolding or inter-compartment transport. GO:0140309 does not fit (carrier-specific) |
| DNAJB1 | GO:0051082 unfolded protein binding (IDA, PMID:21231916) | GO:0044183 protein folding chaperone *(interim)* | IDA | J-domain co-chaperone: substrate adaptor + HSP70 ATPase activator. Not an independent foldase. GO:0044183 used as interim; see [co-chaperone note](#co-chaperone-note) |
| SYVN1 | GO:0051082 unfolded protein binding (IDA, PMID:14593114) | REMOVE | IDA | HRD1 is an E3 ubiquitin ligase; recognizes misfolded substrates for degradation, not chaperoning. Candidate for proposed "misfolded protein sensor activity" |
| UGGT1 | GO:0051082 unfolded protein binding (IDA, PMID:24790089) | MARK_AS_OVER_ANNOTATED | IDA | Glycoprotein quality sensor for GT activity, not a chaperone |
| NPM1 | GO:0051082 unfolded protein binding (IDA, PMID:20625543) | GO:0140713 histone chaperone activity | IDA | Pentameric histone chaperone; UPB is secondary to core histone chaperoning |

## Open Ontology Gaps

Ontology changes needed to properly annotate genes in this set:

1. **NTR: general holdase chaperone activity** — The most critical gap. GO:0140309
   "unfolded protein carrier activity" was created in Nov 2025 specifically for TIM carrier-holdases
   (Tim9-Tim10, Tim8-Tim13) that escort unfolded proteins across the mitochondrial IMS
   ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552)). Its definition
   requires escort "between two different cellular components" and it is a child of GO:0140597
   "protein carrier chaperone." Val and Pascale acknowledged in #30552 that a more general holdase
   term was needed but deferred it: *"we thought it would be better to add this specific term as
   it was needed immediately for annotation, and add the more general parent 'holdase' when it was
   requested for annotation"* (Val, 2025-11-04). Raymond also flagged that an ER holdase
   (PMID:30287478) doesn't fit GO:0140309. "holdase" is explicitly a **BROAD** synonym on
   GO:0140309, confirming it is not the general holdase term.
   - **We are now requesting this term.** 7 genes in this review (CRYAA, CRYAB, HSPB6, CLU, SCG5,
     DNAJB6, DNAJB8) plus HSPH1 (non-human) are in-situ holdases that prevent aggregation without
     inter-compartment escort. They cannot be annotated to GO:0140309.
   - **Proposed term**: "holdase chaperone activity" — Def: "Binding to an unfolded or misfolded
     protein to prevent its aggregation without actively catalyzing refolding. The holdase maintains
     the client protein in a soluble, folding-competent state." Parent: direct child of
     GO:0003674 molecular_function (per #30552 discussion; "protein carrier chaperone" is wrong
     for non-carriers). GO:0140309 would become a child of this new term (carrier-holdases are
     a subtype of holdases).
   - **Relationship to Raymond's proposal**: Raymond (in [go-annotation#5581](https://github.com/geneontology/go-annotation/issues/5581))
     proposed creating foldase/holdase subtypes under GO:0051082. We recommend against this because
     (a) GO:0051082 is a "binding" term and Val/Pascale want "activity" terms, (b) GO:0044183
     already covers foldase, and (c) a standalone holdase term is more composable than a subtype
     of a binding term being obsoleted.
   - **Until this NTR is created, GO:0051082 obsoletion should be blocked** for holdase genes.
   - Affects: CRYAA, CRYAB, HSPB6, CLU, SCG5, DNAJB6, DNAJB8, HSPH1.

2. **Misfolded protein sensor activity** — Recognition of misfolded protein conformation to
   target substrates for quality-control degradation (distinct from chaperone activity). Would
   apply to SYVN1, and to non-human genes SAN1 (yeast), Fbxo2 (mouse). Useful for ubiquitin
   degradation pathways. Currently these are REMOVE/OVER_ANNOTATED since no appropriate MF
   term exists.

3. **Co-chaperone MF representation** — GO:0003767 "co-chaperone activity" was deliberately
   obsoleted because it "represents a class of gene products rather than a molecular function."
   Similarly, GO:0030189 "chaperone activator activity" and all HSP-specific regulator terms
   are obsolete. There is currently no MF term that captures what J-domain co-chaperones do
   (activate HSP70 ATPase + deliver substrates). GO:0044183 is used as pragmatic interim.
   Affects: DNAJB1, DNAJB2, DNAJA2, DNAJA4 and all J-domain proteins across species.

## What We Need from GO Editors

- [ ] **Holdase NTR (BLOCKING)**: Create general "holdase chaperone activity" term for in-situ holdases. GO:0140309 is carrier-specific (created for TIM chaperones in #30552) and does not fit 7 genes in this review. See [holdase annotation gap](#holdase-annotation-gap) for proposed def and parentage
- [ ] **Block GO:0051082 obsoletion** until holdase NTR exists — 7 holdase genes have no valid replacement term without it
- [ ] **Preferred labels**: Add "foldase" as exact synonym for GO:0044183; "holdase" should be exact synonym on the new general holdase term (currently BROAD on GO:0140309, which is correct since GO:0140309 is carrier-specific)
- [ ] **Co-chaperone MF gap**: How should J-domain co-chaperone function be annotated? GO:0003767 is obsolete; GO:0044183 is used as interim but obscures the co-chaperone mechanism. Affects all J-domain proteins
- [ ] **HSP70 dual annotation**: Confirm that HSP70-family genes may need both GO:0044183 (foldase) and the holdase NTR depending on experimental context
- [ ] **PTGES3 co-chaperone mechanism**: Clarify whether PTGES3 is an HSP90 activator, substrate adaptor, or both
- [ ] **Misfolded protein sensor**: Decide whether "misfolded protein sensor activity" warrants a new term — affects SYVN1, SAN1, Fbxo2 and ubiquitin degradation pathways
- [ ] Proceed with obsoletion of GO:0051082 and GO:0031249 once holdase NTR and other replacement terms are in place

## Scope Note: Phase-2 Sensor Batch

This document's primary scope (phase 1) is manual reclassification of existing
GO:0051082 / GO:0031249 annotations. A separate phase 2 batch is reserved for
misfolded-protein sensing and degradation-triage genes that are mechanistically
related but not necessarily in the unfolded/denatured binding annotation set.

Phase 2 candidate genes from deep-research synthesis:

- STUB1 (CHIP), UBR1, UBR2, HUWE1 (core misfolded-protein sensor/E3 axis)
- BAG3, BAG6 (co-chaperone/triage adapters; secondary sensor-adjacent set)

Phase 2 is a follow-up ontology/annotation effort and should not block phase 1
GO:0051082/GO:0031249 replacement and obsoletion work.

---

## Replacement Terms (detailed)

Existing GO terms used as replacements:

- **GO:0044183** protein folding chaperone (="foldase") — assists protein folding *(existing)*
- **GO:0140545** ATP-dependent protein disaggregase activity — solubilizes protein aggregates *(existing)*
- **GO:0140713** histone chaperone activity — for NPM1 *(existing)*
- **GO:0051879** Hsp90 protein binding — for AIP *(existing; note: binding term, not function)*
- **GO:0000774** adenyl-nucleotide exchange factor activity — core MF for GRPEL1 (UPB removed) *(existing)*

**Not used** (despite initial consideration):

- **GO:0140309** unfolded protein carrier activity — This is a carrier-holdase term created
  specifically for TIM chaperones ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552)).
  Its definition requires escort between cellular components. None of the holdase genes in
  this review (crystallins, sHSPs, CLU, SCG5, DNAJB6, DNAJB8) are carrier-holdases.

This project focuses on MF replacement for GO:0051082/GO:0031249. BP terms discussed in
individual gene reviews (for example GO:0030150 in GRPEL1) are not listed as MF replacements here.

Proposed new terms (not yet in GO):

- **"holdase chaperone activity"** — Def: "Binding to an unfolded or misfolded protein to prevent
  its aggregation without actively catalyzing refolding. The holdase maintains the client protein
  in a soluble, folding-competent state." Parent: direct child of GO:0003674. GO:0140309 (carrier-holdase)
  would become a child of this term. **This is the primary NTR needed to unblock GO:0051082 obsoletion.**
  Affects 7 human genes + HSPH1.
- **"misfolded protein sensor activity"** — Def: Recognition of misfolded protein conformation to initiate
  quality-control degradation. Distinct from chaperone activity. Useful for ubiquitin degradation pathways.

Proposed refinements to existing terms:

- **GO:0044183** — Add "foldase" as exact synonym.

### Holdase annotation gap

Several genes in this review are **holdases** rather than foldases. Holdases bind unfolded or
misfolded proteins to prevent their aggregation, but they lack ATPase activity and do **not**
actively refold substrates. This is mechanistically distinct from the ATP-dependent foldase
activity of HSP70-type chaperones. Some proteins (notably HSP70) can function as both foldase
and holdase depending on conditions, clients, and whether the context is de novo folding or
quality control.

**GO:0140309 "unfolded protein carrier activity" does not fit these genes.** Review of the
original term request ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552))
shows that GO:0140309 was created in Nov 2025 specifically for TIM carrier-holdases (Tim9-Tim10,
Tim8-Tim13) that escort unfolded proteins across the mitochondrial IMS. Key evidence:

- Its definition requires escort "between two different cellular components"
- It is a child of GO:0140597 "protein carrier chaperone"
- "holdase" is explicitly a **BROAD** synonym (not exact), because not all holdases are carriers
- Val (2025-11-04): *"we were aware that there were holdases that did not bind to unfolded
  proteins [in transit], but we needed a use case"* for the carrier-holdase
- Raymond flagged that an ER holdase (PMID:30287478) doesn't fit GO:0140309; Val agreed a
  separate holdase term is needed

The holdase genes in this review (CRYAA, CRYAB, HSPB6, CLU, SCG5, DNAJB6, DNAJB8) all prevent
aggregation **in situ** — they do not escort substrates between compartments. HSPH1 (non-human)
is likewise an in-situ holdase. These genes require a new general "holdase chaperone activity"
term (see [Open Ontology Gaps](#open-ontology-gaps) item 1).

**Until the holdase NTR is created, these 7 genes should retain GO:0051082** — the obsoletion
of GO:0051082 should be blocked on this NTR.

### Co-chaperone note

J-domain (DnaJ/HSP40) proteins are **co-chaperones**, not independent foldases. They:
- Activate HSP70's ATPase via their J-domain
- Act as substrate adaptors, delivering unfolded clients to HSP70
- Do not independently fold proteins

GO previously had GO:0003767 "co-chaperone activity" but it was deliberately obsoleted because
it "represents a class of gene products rather than a molecular function." Similarly,
GO:0030189 "chaperone activator activity" and all HSP-specific regulator terms are obsolete.

There is currently **no active GO MF term** for co-chaperone function. GO:0044183 "protein
folding chaperone" is used as a pragmatic interim because J-domain proteins do participate in
the folding process (as part of the HSP70 machine), but this obscures the co-chaperone
mechanism. Editor guidance is requested on how to represent this function.

Note: Some J-domain proteins (DNAJB6, DNAJB8) have **independent holdase activity** in addition
to their co-chaperone function — these are annotated to GO:0140309 for their holdase activity.

---

## Human Gene Checklist

33 unique human genes are in scope below. HSPA1A appears again in the GO:0031249 subsection
because it has that second term as well; this is not an additional human gene.

### Tier 1a - HSP70 family (foldase/holdase, context-dependent)
- [x] HSPA1A (P0DMV8) - HSP70, foldase/holdase → MODIFY to GO:0044183 + GO:0140545; holdase aspect awaits holdase NTR
- [x] HSPA1B (P0DMV9) - HSP70, foldase/holdase → MODIFY to GO:0044183 + GO:0140545; holdase aspect awaits holdase NTR
- [x] HSPA2 (P54652) - HSP70, foldase/holdase → MODIFY to GO:0044183; holdase aspect awaits holdase NTR
- [x] HSPA6 (P17066) - HSP70, foldase/holdase → MODIFY to GO:0044183; holdase aspect awaits holdase NTR
- [x] HSPA8 (P11142) - HSC70, foldase/holdase → MODIFY to GO:0044183 + GO:0140545; holdase aspect awaits holdase NTR
- [x] HSPA1L (P34931) - HSP70, foldase/holdase → MODIFY to GO:0044183; holdase aspect awaits holdase NTR

### Tier 1b - J-domain co-chaperones (see [co-chaperone note](#co-chaperone-note))
- [x] DNAJB1 (P25685) - HSP40, foldase-type co-chaperone → MODIFY to GO:0044183 *(interim; substrate adaptor + HSP70 ATPase activator)*
- [x] DNAJB2 (P25686) - HSP40, co-chaperone → MODIFY to GO:0044183 *(interim)*
- [x] DNAJA2 (O60884) - HSP40, foldase-type co-chaperone → MODIFY to GO:0044183 *(interim)*
- [x] DNAJA4 (Q8WW22) - HSP40, co-chaperone → MODIFY to GO:0044183 *(interim)*
- [x] DNAJB6 (O75190) - HSP40, holdase-type co-chaperone → holdase NTR *(retain GO:0051082 until created; independent in-situ holdase, not carrier)*
- [x] DNAJB8 (Q8NHS0) - HSP40, holdase-type co-chaperone → holdase NTR *(retain GO:0051082 until created; independent in-situ holdase, not carrier)*

### Tier 2 - Small HSPs / Holdases
- [x] CRYAA (P02489) - alpha-crystallin, holdase → holdase NTR *(retain GO:0051082; in-situ holdase, not carrier)*
- [x] CRYAB (P02511) - alpha-crystallin, holdase → holdase NTR *(retain GO:0051082; in-situ holdase, not carrier)*
- [x] HSPB6 (O14558) - small HSP, holdase → holdase NTR *(retain GO:0051082; in-situ holdase, not carrier)*

### Tier 3 - Prefoldin Complex
- [x] PFDN1 (O60925) - prefoldin subunit → MODIFY to GO:0044183
- [x] PFDN2 (Q9UHV9) - prefoldin subunit → MODIFY to GO:0044183
- [x] PFDN4 (Q9NQP4) - prefoldin subunit → MODIFY to GO:0044183
- [x] PFDN5 (Q99471) - prefoldin subunit → MODIFY to GO:0044183 + GO:0003714 (transcription corepressor)
- [x] PFDN6 (O15212) - prefoldin subunit → MODIFY to GO:0044183
- [x] VBP1 (P61758) - prefoldin subunit 3 → MODIFY to GO:0044183

### Tier 4 - ER Quality Control (sensors, not chaperones)
- [x] UGGT1 (Q9NYU2) - glycoprotein quality sensor → MARK_AS_OVER_ANNOTATED
- [x] ERLEC1 (Q96DZ1) - ER lectin, ERAD → REMOVE
- [x] SYVN1 (Q86TM6) - E3 ligase, ERAD → REMOVE

### Tier 5 - Other / Unusual
- [x] NPM1 (P06748) - nucleophosmin → MODIFY to GO:0140713 + GO:0140142 + GO:0044183 + GO:0019901
- [x] CLU (P10909) - clusterin, extracellular holdase → holdase NTR *(retain GO:0051082; in-situ/extracellular holdase, not carrier)*
- [x] SCG5 (P05408) - neuroendocrine protein 7B2 → holdase NTR *(retain GO:0051082; secretory pathway holdase, not carrier)*
- [x] TOMM20 (Q15388) - mitochondrial import receptor → MARK_AS_OVER_ANNOTATED
- [x] GRPEL1 (Q9HAV7) - GrpE homolog (NEF) → REMOVE (not direct unfolded-substrate binder; core MF GO:0000774)
- [x] AIP (O00170) - AH receptor interacting protein → MODIFY to GO:0051879
- [x] AHSA1 (O95433) - HSP90 ATPase activator co-chaperone → MARK_AS_OVER_ANNOTATED
- [x] PTGES3 (Q15185) - HSP90 co-chaperone (mechanism unclear: activator? substrate adaptor?) / PGE synthase → MARK_AS_OVER_ANNOTATED
- [x] TMEM67 (Q5HYA8) - meckelin → MARK_AS_OVER_ANNOTATED

### GO:0031249 (denatured protein binding)
- HSPA1A (P0DMV8) - already in Tier 1 (same gene; listed here because it also has GO:0031249)
- [x] SAN1 (yeast) - E3 ligase, misfolded protein sensor → MODIFY GO:0031249 to GO:0051787 (misfolded protein binding)
- [x] Fbxo2 (mouse) - F-box protein, glycoprotein sensor → MODIFY GO:0031249 (glycan-mediated recognition, not general denatured protein binding)
- [x] HSPH1 (hamster) - Hsp110, holdase → MODIFY GO:0031249 to holdase NTR *(retain GO:0031249 until created)* + core NEF function (GO:0000774)

## Categories of Annotated Proteins (all species)

All 148 genes organized by mechanism class (human + non-human combined):

| # | Category | Genes | Decision pattern |
|---|----------|-------|------------------|
| 1 | **HSP70 foldase/holdase** | HSPA1A/B, HSPA2, HSPA6, HSPA8, HSPA1L (human); SSA1-4, SSB1-2, SSQ1, SSZ1, KAR2, LHS1 (yeast); DnaK (E. coli); Hspa8 (mouse, rat); Hspa5/BiP (rat) | MODIFY → GO:0044183; holdase NTR pending |
| 2 | **HSP90 system** | AHSA1, PTGES3, AIP (human); HSP82, HSC82, CPR6, CPR7, CDC37 (yeast); CDC37 (C. albicans); Hsp83 (fly) | MODIFY or OVER_ANNOTATED |
| 3 | **J-domain co-chaperones** | DNAJB1, DNAJB2, DNAJA2, DNAJA4 (human); DNAJB6, DNAJB8 (human, holdase-type); YDJ1, MDJ1, APJ1 (yeast); JEM1 (yeast, C. albicans); DnaJ (E. coli); Dnaja3, Dnajb11 (mouse) | MODIFY → GO:0044183 (interim); holdase-type → holdase NTR |
| 4 | **sHSPs/holdases** | CRYAA, CRYAB, HSPB6 (human); CLU, SCG5 (human); CRYAA (bovine); cryaa/cryaba/cryabb (zebrafish); HSP26 (yeast); Hsp22/23/26/27 (fly); HSP17.7 (Arabidopsis); HSPH1 (hamster) | MODIFY → holdase NTR; retain GO:0051082 until NTR created |
| 5 | **Chaperonin/TRiC/CCT** | TCP1, CCT2-8 (yeast); GroEL (E. coli); HSP60, HSP10 (yeast) | MODIFY → GO:0044183 |
| 6 | **Prefoldin** | PFDN1-6, VBP1 (human); PFD1, EGD1, EGD2 (yeast) | MODIFY → GO:0044183 |
| 7 | **Disaggregase** | HSP104 (yeast) | MODIFY → GO:0044183 (also GO:0140545) |
| 8 | **ER quality control** | UGGT1, ERLEC1, SYVN1 (human); Uggt1 (rat); CNE1, EPS1, PDI1, EUG1, ROT1, IRE1 (yeast); IRE1 (T. reesei); CSH3 (C. albicans); Edem2 (fly) | OVER_ANNOTATED or REMOVE (sensors, not chaperones) |
| 9 | **Mito import/assembly** | TOMM20, GRPEL1 (human); TIM9, TIM10, COX20, PET100, SHY1, ATP10, ATP11 (yeast); Grpel2 (mouse); cia30 (N. crassa) | OVER_ANNOTATED (assembly factors) or MODIFY (TIMs → GO:0140309) |
| 10 | **Ubiquitin/QC sensor** | SYVN1 (human); SAN1 (yeast); Fbxo2 (mouse); slrP (Salmonella) | REMOVE or MODIFY to GO:0051787 |
| 11 | **Periplasmic chaperones** | SurA, Skp, Spy, SecB, HdeA, HdeB, SlyD, CpxP (E. coli) | MODIFY → GO:0044183 (holdase/chaperone) |
| 12 | **Ribosome assembly** | SQT1, SYO1, YAR1, RRB1, TSR4, PNO1, ACL4, SHQ1, BTT1 (yeast) | MODIFY → GO:0044183 or OVER_ANNOTATED |
| 13 | **Peroxiredoxin/redox chaperones** | TSA1 (yeast); pmp20, tpx1 (S. pombe); CnoX, RidA (E. coli) | MODIFY → GO:0044183 (stress-activated holdase) |
| 14 | **Membrane protein chaperones** | SHR3, PHO86, GSF2, CHS7, NSG1, NSG2, VMA22, VPS45 (yeast) | MODIFY or OVER_ANNOTATED |
| 15 | **Other** | NPM1, TMEM67 (human); NAP1, GET3 (yeast); St13, Serpinh1 (mouse/rat); Nmnat (fly); nud-1, hsp-12.3, hsp-12.6 (worm); tigA (A. niger); GIP1 (Arabidopsis) | Gene-specific decisions |

## Cross-Species Completeness Audit

All experimental annotations to GO:0051082 and GO:0031249 across all species have been
reviewed. The [Human Gene Checklist](#human-gene-checklist) provides detailed mechanism-level
analysis with full literature review; this section documents that the same decision rules
apply consistently across species.

### Coverage

| Metric | Count |
|--------|-------|
| Unique gene reviews (by UniProt ID) | 148 |
| Human genes (primary analysis) | 33 |
| Non-human genes | 115 |
| Species covered | 17 |
| Total annotations reviewed | 5,529 |
| Remaining PENDING | 0 |

### GO:0051082/GO:0031249 decisions (non-human genes only)

| Decision | Count | Description |
|----------|-------|-------------|
| MODIFY → GO:0044183 or holdase NTR | 88 | Genuine chaperones reclassified to mechanism-specific terms |
| MARK_AS_OVER_ANNOTATED | 23 | Assembly factors, sensors, co-chaperones where UPB overstates activity |
| ACCEPT (retain GO:0051082) | 3 | Genes where GO:0051082 remains best available term |
| KEEP_AS_NON_CORE | 2 | UPB is secondary to primary function (ATP11, VMA22) |
| REMOVE | 2 | Misannotations (slrP/Salmonella, hsp-12.6/worm) |

### Species breakdown

| Species | Genes | Notes |
|---------|-------|-------|
| *S. cerevisiae* | 67 | Largest set; covers all 14 mechanism classes |
| *E. coli* | 13 | Major bacterial chaperone repertoire including periplasmic holdases (SurA, Skp, Spy, HdeA/B, SecB) with no human orthologs |
| *D. melanogaster* | 7 | sHSPs (Hsp22-27), Hsp83 (HSP90), Edem2 (ERAD sensor), Nmnat |
| *M. musculus* | 6 | Orthologs of human genes; Hspa8 was largest review (240 annotations) |
| *R. norvegicus* | 4 | Hspa5/BiP (101 annotations), Hspa8, St13, Uggt1 |
| *C. albicans* | 3 | CDC37, CSH3, JEM1 |
| *D. rerio* | 3 | Crystallin holdases: cryaa, cryaba, cryabb |
| *C. elegans* | 3 | sHSPs (hsp-12.3, hsp-12.6) and nud-1 |
| *S. pombe* | 2 | Peroxiredoxins: pmp20, tpx1 |
| *A. thaliana* | 1 | HSP17.7 (cytosolic class II sHSP holdase) |
| *B. taurus* | 1 | CRYAA (classic holdase reference) |
| *N. crassa* | 1 | cia30 (complex I assembly factor, not general UPB) |
| *A. niger* | 1 | tigA (PDI family ER chaperone) |
| *S. typhimurium* | 1 | slrP (T3SS effector E3 ligase — misannotation removed) |
| *T. reesei* | 1 | IRE1 (UPR sensor, not chaperone) |
| Chinese hamster | 1 | HSPH1 (Hsp110, holdase + NEF) |

### Notable non-human findings

These cases added genuinely new mechanistic insights beyond what the human gene reviews
established:

1. **SlrP (S. typhimurium)** — **Misannotation identified and removed**. SlrP is a T3SS
   effector E3 ubiquitin ligase that binds the ER chaperone ERdj3; the GO:0051082 annotation
   was based on co-IP with ERdj3, misinterpreted as unfolded protein binding. SlrP disrupts
   ERdj3's chaperone function rather than acting as a chaperone itself.

2. **E. coli periplasmic chaperones (SurA, Skp, Spy, HdeA/B, SecB, CpxP, SlyD)** —
   Bacterial-specific holdase/chaperone category with no human orthologs. SurA is a holdase
   that escorts OMPs to the BAM complex; Spy and HdeA/B are acid-activated holdases; SecB
   is a secretion-coupled holdase. All MODIFY → GO:0044183. These validate the foldase/holdase
   framework in a phylogenetically distant lineage.

3. **CnoX (E. coli)** — Redox-activated holdase with thioredoxin domain. Interesting
   mechanistic variant: becomes an active holdase specifically under oxidative stress when
   its Cys residues are oxidized. Supports the holdase NTR need.

4. **Assembly factors (ATP10, PET100, COX20, SHY1, cia30)** — Single-client assembly
   chaperones for respiratory chain complexes. These bind specific subunits during complex
   assembly, not unfolded proteins generally. All MARK_AS_OVER_ANNOTATED. GO:0140777
   (protein-containing complex stabilizing activity) proposed as replacement for some.

5. **IRE1 (yeast + T. reesei)** — UPR sensor kinase/endoribonuclease. Detects unfolded
   proteins in the ER lumen as a signaling sensor, not a chaperone. Cross-kingdom confirmation
   of OVER_ANNOTATED. The T. reesei review also flagged metazoan-specific GO terms
   (IRE1-TRAF2-ASK1 complex) that are biologically impossible in fungi.

6. **Peroxiredoxins (TSA1, pmp20, tpx1)** — Dual-function: peroxidase at low oxidative
   stress, holdase chaperone at high stress (after overoxidation of catalytic Cys). Confirms
   that GO:0051082 is appropriate for the chaperone function but should become holdase NTR.

<details>
<summary>Full non-human gene table (click to expand)</summary>


| Gene | Species | UniProt | Annotations | GO:0051082 decision | Notes |
|------|---------|---------|-------------|---------------------|-------|
| HSP17.7 | *A. thaliana* | O81822 | 14 | MODIFY (holdase NTR) | Cytosolic class II sHSP |
| tigA | *A. niger* | Q00216 | 7 | MODIFY → GO:0044183 | PDI family ER chaperone |
| CRYAA | *B. taurus* | P02470 | 25 | MODIFY (holdase NTR) | Classic holdase reference |
| CDC37 | *C. albicans* | Q8X1E6 | 23 | MODIFY | HSP90 co-chaperone |
| CSH3 | *C. albicans* | A0A1D8PLU5 | 17 | MODIFY | ER oxidoreductase |
| JEM1 | *C. albicans* | A0A1D8PIB5 | 11 | MODIFY | ER DnaJ co-chaperone |
| hsp-12.3 | *C. elegans* | Q20164 | 6 | ACCEPT | sHSP |
| hsp-12.6 | *C. elegans* | G5EE36 | 7 | REMOVE | UPB not well-supported |
| nud-1 | *C. elegans* | G5EE74 | 15 | MODIFY | Nudix hydrolase |
| HSPH1 | Chinese hamster | Q60446 | 12 | MODIFY (holdase NTR) | Hsp110 holdase + NEF |
| cryaa | *D. rerio* | Q8UUZ6 | 17 | MODIFY (holdase NTR) | Crystallin holdase |
| cryaba | *D. rerio* | Q9PUR2 | 16 | MODIFY (holdase NTR) | Crystallin holdase |
| cryabb | *D. rerio* | A0A8M9Q8E3 | 19 | MODIFY (holdase NTR) | Crystallin holdase |
| Hsp22 | *D. melanogaster* | P02515 | 18 | MODIFY (holdase NTR) | sHSP |
| Hsp23 | *D. melanogaster* | P02516 | 22 | MODIFY (holdase NTR) | sHSP |
| Hsp26 | *D. melanogaster* | P02517 | 22 | MODIFY (holdase NTR) | sHSP |
| Hsp27 | *D. melanogaster* | P02518 | 24 | MODIFY (holdase NTR) | sHSP |
| Hsp83 | *D. melanogaster* | P02828 | 54 | MODIFY → GO:0044183 | HSP90 ortholog |
| Nmnat | *D. melanogaster* | Q9VC03 | 32 | MODIFY | Neuroprotective chaperone |
| Edem2 | *D. melanogaster* | Q9VK27 | 23 | OVER_ANNOTATED | ERAD sensor, not chaperone |
| CnoX | *E. coli* | P77395 | 12 | MODIFY → GO:0044183 | Redox-activated holdase |
| CpxP | *E. coli* | P0AE85 | 11 | OVER_ANNOTATED | Cpx pathway adaptor |
| DnaJ | *E. coli* | P08622 | 48 | MODIFY → GO:0044183 | J-domain co-chaperone |
| DnaK | *E. coli* | P0A6Y8 | 61 | MODIFY → GO:0044183 | HSP70 foldase/holdase |
| GroEL | *E. coli* | P0A6F5 | 64 | MODIFY → GO:0044183 | Chaperonin |
| HdeA | *E. coli* | P0AES9 | 14 | MODIFY → GO:0044183 | Acid-activated holdase |
| HdeB | *E. coli* | P0AET2 | 8 | MODIFY → GO:0044183 | Acid-activated holdase |
| RidA | *E. coli* | P0AF93 | 22 | OVER_ANNOTATED | Reactive intermediate deaminase |
| SecB | *E. coli* | P0AG86 | 27 | MODIFY → GO:0044183 | Secretion chaperone |
| Skp | *E. coli* | P0AEU7 | 34 | MODIFY → GO:0044183 | Periplasmic holdase |
| SlyD | *E. coli* | P0A9K9 | 35 | MODIFY → GO:0044183 | FKBP-type PPIase/chaperone |
| Spy | *E. coli* | P77754 | 11 | MODIFY → GO:0044183 | Periplasmic holdase |
| surA | *E. coli* | P0ABZ6 | 31 | MODIFY → GO:0044183 | Periplasmic OMP holdase |
| Dnaja3 | *M. musculus* | Q99M87 | 81 | MODIFY → GO:0044183 | Mitochondrial J-domain co-chaperone |
| Dnajb11 | *M. musculus* | Q99KV1 | 33 | MODIFY → GO:0044183 | ER J-domain co-chaperone |
| Fbxo2 | *M. musculus* | Q80UW2 | 44 | MODIFY | Glycoprotein QC sensor (GO:0031249) |
| Grpel2 | *M. musculus* | O88396 | 15 | MODIFY | Mitochondrial NEF |
| Hspa8 | *M. musculus* | P63017 | 240 | MODIFY → GO:0044183 | HSC70 foldase/holdase |
| Serpinh1 | *M. musculus* | P19324 | 26 | MODIFY → GO:0044183 | Collagen chaperone |
| cia30 | *N. crassa* | O42636 | 7 | OVER_ANNOTATED | Complex I assembly factor |
| Hspa5 | *R. norvegicus* | P06761 | 101 | MODIFY → GO:0044183 | BiP/GRP78 ER HSP70 |
| Hspa8 | *R. norvegicus* | P63018 | 208 | MODIFY → GO:0044183 | HSC70 foldase/holdase |
| St13 | *R. norvegicus* | P50503 | 23 | MODIFY | HSP70/HSP90 co-chaperone |
| Uggt1 | *R. norvegicus* | Q9JLA3 | 26 | OVER_ANNOTATED | Glycoprotein QC sensor |
| pmp20 | *S. pombe* | O14313 | 18 | MODIFY → GO:0044183 | Peroxiredoxin/holdase |
| tpx1 | *S. pombe* | O74887 | 35 | MODIFY → GO:0044183 | Peroxiredoxin/holdase |
| IRE1 | *T. reesei* | G0RBE3 | 21 | OVER_ANNOTATED | UPR sensor, not chaperone |
| slrP | *S. typhimurium* | Q8ZQQ2 | 16 | REMOVE | T3SS effector E3 ligase (misannotation) |
| ACL4 | *S. cerevisiae* | Q03771 | 18 | MODIFY | Ribosome assembly |
| APJ1 | *S. cerevisiae* | P53940 | 26 | MODIFY | J-domain co-chaperone |
| ATP10 | *S. cerevisiae* | P18496 | 14 | OVER_ANNOTATED | Atp6p assembly factor |
| ATP11 | *S. cerevisiae* | P32453 | 16 | NON_CORE | Atp12p assembly factor |
| BTT1 | *S. cerevisiae* | P40314 | 15 | MODIFY | Ribosome assembly |
| CCT2 | *S. cerevisiae* | P39076 | 21 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CCT3 | *S. cerevisiae* | P39077 | 17 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CCT4 | *S. cerevisiae* | P39078 | 19 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CCT5 | *S. cerevisiae* | P40413 | 17 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CCT6 | *S. cerevisiae* | P39079 | 17 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CCT7 | *S. cerevisiae* | P42943 | 16 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CCT8 | *S. cerevisiae* | P47079 | 20 | MODIFY → GO:0044183 | TRiC/CCT subunit |
| CDC37 | *S. cerevisiae* | P06101 | 23 | OVER_ANNOTATED | HSP90 co-chaperone |
| CHS7 | *S. cerevisiae* | P38843 | 20 | MODIFY | Chitin synthase chaperone |
| CNE1 | *S. cerevisiae* | P27825 | 17 | OVER_ANNOTATED | ER lectin |
| COX20 | *S. cerevisiae* | Q04935 | 12 | OVER_ANNOTATED | Cox2p assembly factor |
| CPR6 | *S. cerevisiae* | P53691 | 28 | OVER_ANNOTATED | HSP90 co-chaperone |
| CPR7 | *S. cerevisiae* | P47103 | 21 | OVER_ANNOTATED | HSP90 co-chaperone |
| EGD1 | *S. cerevisiae* | Q02642 | 19 | MODIFY → GO:0044183 | NAC complex |
| EGD2 | *S. cerevisiae* | P38879 | 22 | MODIFY → GO:0044183 | NAC complex |
| EPS1 | *S. cerevisiae* | P40557 | 15 | OVER_ANNOTATED | ER QC factor |
| EUG1 | *S. cerevisiae* | P32474 | 24 | OVER_ANNOTATED | PDI homolog |
| GET3 | *S. cerevisiae* | Q12154 | 64 | MODIFY | TA protein chaperone |
| GSF2 | *S. cerevisiae* | Q04697 | 9 | MODIFY | Glucose transporter chaperone |
| HSC82 | *S. cerevisiae* | P15108 | 47 | MODIFY → GO:0044183 | HSP90 |
| HSP10 | *S. cerevisiae* | P38910 | 21 | OVER_ANNOTATED | GroES co-chaperonin |
| HSP104 | *S. cerevisiae* | P31539 | 46 | MODIFY → GO:0044183 | Disaggregase |
| HSP26 | *S. cerevisiae* | P15992 | 16 | MODIFY (holdase NTR) | sHSP holdase |
| HSP60 | *S. cerevisiae* | P19882 | 47 | MODIFY → GO:0044183 | Chaperonin |
| HSP82 | *S. cerevisiae* | P02829 | 73 | MODIFY → GO:0044183 | HSP90 |
| IRE1 | *S. cerevisiae* | P32361 | 46 | OVER_ANNOTATED | UPR sensor |
| JEM1 | *S. cerevisiae* | P40358 | 15 | MODIFY | ER J-domain co-chaperone |
| KAR2 | *S. cerevisiae* | P16474 | 42 | MODIFY → GO:0044183 | ER HSP70 (BiP) |
| LHS1 | *S. cerevisiae* | P36016 | 22 | MODIFY → GO:0044183 | ER HSP70-like |
| MDJ1 | *S. cerevisiae* | P35191 | 25 | MODIFY → GO:0044183 | Mito J-domain |
| NAP1 | *S. cerevisiae* | P25293 | 60 | MODIFY | Histone chaperone |
| NSG1 | *S. cerevisiae* | P38837 | 16 | OVER_ANNOTATED | Sterol-binding |
| NSG2 | *S. cerevisiae* | P53898 | 8 | OVER_ANNOTATED | Sterol-binding |
| PDI1 | *S. cerevisiae* | P17967 | 32 | OVER_ANNOTATED | Protein disulfide isomerase |
| PET100 | *S. cerevisiae* | P38958 | 12 | OVER_ANNOTATED | Cox assembly factor |
| PFD1 | *S. cerevisiae* | P46988 | 20 | MODIFY → GO:0044183 | Prefoldin subunit |
| PHO86 | *S. cerevisiae* | P46956 | 12 | MODIFY | Phosphate transporter chaperone |
| PNO1 | *S. cerevisiae* | Q99216 | 18 | OVER_ANNOTATED | Ribosome biogenesis |
| ROT1 | *S. cerevisiae* | Q03691 | 23 | MODIFY | ER chaperone |
| RRB1 | *S. cerevisiae* | Q04225 | 11 | MODIFY | Ribosome assembly |
| SAN1 | *S. cerevisiae* | P22470 | 20 | MODIFY (GO:0051787) | E3 ligase QC sensor (GO:0031249) |
| SHQ1 | *S. cerevisiae* | P40486 | 12 | MODIFY | H/ACA snoRNP assembly |
| SHR3 | *S. cerevisiae* | Q02774 | 18 | MODIFY | Amino acid permease chaperone |
| SHY1 | *S. cerevisiae* | P53266 | 14 | OVER_ANNOTATED | Cox assembly factor |
| SQT1 | *S. cerevisiae* | P35184 | 9 | MODIFY | Ribosome assembly |
| SSA1 | *S. cerevisiae* | P10591 | 71 | MODIFY → GO:0044183 | HSP70 |
| SSA2 | *S. cerevisiae* | P10592 | 58 | MODIFY → GO:0044183 | HSP70 |
| SSA3 | *S. cerevisiae* | P09435 | 26 | MODIFY → GO:0044183 | HSP70 |
| SSA4 | *S. cerevisiae* | P22202 | 25 | MODIFY → GO:0044183 | HSP70 |
| SSB1/2 | *S. cerevisiae* | P10080/P40150 | 32/39 | MODIFY → GO:0044183 | Ribosome-associated HSP70 |
| SSQ1 | *S. cerevisiae* | Q05931 | 29 | MODIFY → GO:0044183 | Mito HSP70 |
| SSZ1 | *S. cerevisiae* | P38788 | 30 | MODIFY → GO:0044183 | RAC HSP70 |
| SYO1 | *S. cerevisiae* | Q07395 | 12 | MODIFY | Ribosome assembly |
| TCP1 | *S. cerevisiae* | P12612 | 23 | MODIFY → GO:0044183 | TRiC subunit |
| TIM9 | *S. cerevisiae* | O74700 | 30 | MODIFY → GO:0140309 | Carrier-holdase |
| TIM10 | *S. cerevisiae* | P87108 | 34 | MODIFY → GO:0140309 | Carrier-holdase |
| TSA1 | *S. cerevisiae* | P34760 | 60 | MODIFY → GO:0044183 | Peroxiredoxin/holdase |
| TSR4 | *S. cerevisiae* | P25040 | 15 | MODIFY → GO:0044183 | Ribosome assembly chaperone |
| VMA22 | *S. cerevisiae* | P38784 | 9 | NON_CORE | V-ATPase assembly |
| VPS45 | *S. cerevisiae* | P38932 | 35 | OVER_ANNOTATED | SNARE regulator |
| YAR1 | *S. cerevisiae* | P46683 | 19 | MODIFY | Rps3 chaperone |
| YDJ1 | *S. cerevisiae* | P25491 | 49 | MODIFY → GO:0044183 | J-domain co-chaperone |

</details>

---

# Session Log

<details>
<summary>Curation session notes (click to expand)</summary>

## 2026-02-14 (session 9 - CROSS-SPECIES COMPLETENESS AUDIT)

- **Full cross-species audit completed**: queried QuickGO for ALL experimental annotations to GO:0051082 and GO:0031249
- Found 148 unique genes (by UniProt ID) across 17 species; 33 human were already reviewed
- 115 non-human genes identified; most yeast genes (67) had been reviewed in previous sessions
- Newly reviewed in this session: 13 genes
  - E. coli: dnaJ, groEL, dnaK, slyD, cpxP, hdeA, hdeB, skp, ridA, secB, cnoX, spy, surA
  - Yeast: ATP10
  - Mouse: Dnaja3, Hspa8 (240 annotations — largest review), Dnajb11, Grpel2, Serpinh1
  - Rat: Hspa5 (101 annotations)
  - Fly: Edem2
  - Bovine: CRYAA
  - N. crassa: cia30
  - A. niger: tigA
  - Salmonella: slrP (misannotation — REMOVED)
  - T. reesei/C. glabrata: IRE1
  - Arabidopsis: HSP17.7
  - Drosophila: Hsp26
- **5,529 total annotations reviewed, 0 PENDING remaining**
- Decision distribution for non-human genes: 88 MODIFY, 23 OVER_ANNOTATED, 3 ACCEPT, 2 NON_CORE, 2 REMOVE
- Same mechanism classes apply universally across species — validates the human-derived decision rules
- Notable findings: SlrP misannotation (T3SS effector, not UPB), CnoX redox-activated holdase, peroxiredoxin dual function
- Added Cross-Species Completeness Audit section to project doc with full gene table
- Updated editor brief to reflect full scope (148 genes, 17 species)

## 2026-02-11 (session 8 - GO:0140309 CARRIER CORRECTION)

- **Critical correction**: GO:0140309 is NOT a general holdase term
  - Reviewed full discussion in [go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552)
  - GO:0140309 was created Nov 2025 specifically for TIM carrier-holdases (Tim9-Tim10, Tim8-Tim13)
  - Definition requires escort "between two different cellular components"; child of GO:0140597 "protein carrier chaperone"
  - "holdase" is BROAD synonym (not exact), confirming it's not the general holdase term
  - Val acknowledged general holdase term needed but deferred: "add the more general parent 'holdase' when it was requested for annotation"
  - Raymond flagged ER holdase (PMID:30287478) doesn't fit; Val agreed separate term needed
- **All 7 holdase genes (CRYAA, CRYAB, HSPB6, CLU, SCG5, DNAJB6, DNAJB8) + HSPH1 changed from GO:0140309 to "holdase NTR pending"**
- Primary NTR is now "holdase chaperone activity" (general, non-carrier) — GO:0140309 would become a child
- GO:0051082 obsoletion should be blocked until holdase NTR exists
- Added note on Raymond's foldase/holdase subtype proposal and why standalone term is preferred
- Fixed small Tims example (they ARE carrier-holdases, so were wrong as example of non-carrier holdases)
- HSP70 holdase aspect now references holdase NTR instead of GO:0140309

## 2026-02-11 (session 7 - EDITOR FEEDBACK)

- **Major corrections based on GO editor review**:
  - DNAJ proteins reclassified from "foldase" to "co-chaperone" (substrate adaptors + HSP70 ATPase activators)
  - HSP70 noted as context-dependent foldase/holdase (varies by conditions, clients, de novo vs QC)
  - Holdase replacement term changed from GO:0044183 placeholder to GO:0140309 "unfolded protein carrier activity"
  - Proposed refinement of GO:0140309 def to foreground aggregation prevention
  - Proposed "holdase" as exact (not broad) synonym on GO:0140309
  - Flagged carrier/escort semantics issue: does GO:0140309 fit in-situ holdases (crystallins)?
  - AHSA1 confirmed as HSP90 ATPase activator; PTGES3 mechanism unclear (activator? adaptor?)
  - Note: GO:0003767 "co-chaperone activity" is deliberately obsolete — no MF term exists for J-domain function
  - "misfolded protein sensor activity" confirmed useful for ubiquitin degradation pathways
  - Biologist-friendly labels: "foldase" for GO:0044183, "holdase" for GO:0140309
- Gene checklist restructured: Tier 1a (HSP70 foldase/holdase), Tier 1b (J-domain co-chaperones)
- **Gene review YAMLs not yet updated** — deferred pending editor decisions on holdase carrier semantics and co-chaperone MF representation

## 2026-02-09 (session 6 - NON-HUMAN GENES)

- **3 non-human genes completed**: SAN1 (yeast), Fbxo2 (mouse), HSPH1 (Chinese hamster/CRIGR)
- SAN1: E3 ubiquitin ligase for nuclear protein quality control; GO:0031249 → MODIFY to GO:0051787 (misfolded protein binding)
- Fbxo2: SCF(Fbxo2) substrate adaptor recognizing N-glycans on misfolded glycoproteins; GO:0031249 addressed via glycan-mediated mechanism
- HSPH1: Hsp110 holdase + NEF for Hsp70; GO:0031249 → MODIFY to GO:0044183 (holdase placeholder)
- All 3 validate (0 errors; minor warnings about deep research cross-referencing)
- **All 36 genes (33 human + 3 non-human) now complete**

## 2026-02-09 (session 5 - COMPLETION)

- **All 33 human genes fully complete**: 0 PENDING annotations, all core_functions populated
- Used parallel annotation-reviewer and core-function-synthesizer agents across 5 context windows
- HSPA8 was the largest gene (234 annotations) - completed with dedicated agent
- Prefoldin subunits (PFDN2-6, VBP1) batch-reviewed efficiently given shared function
- HSPA1A core_functions added last (agent got stuck, completed manually using HSPA1B as template)
- SYVN1 had minor supporting_text encoding issues (Greek alpha characters) - fixed
- Key insight: many genes annotated to GO:0051082 have distinct mechanisms (foldase vs holdase vs disaggregase vs sensor) that existing GO terms can capture
- Holdase-type genes (DNAJB6, DNAJB8, CRYAA, CRYAB, HSPB6, CLU) annotated to GO:0044183 with notes about holdase distinction pending ontology term creation

## 2026-02-09 (session 2 - status update)

- Comprehensive status audit performed
- 26/33 human genes had at least partial review (GO:0051082 annotation addressed)
- Most genes had many remaining PENDING annotations (e.g. HSPA1A: 193 PENDING out of 197 total)
- HSPA8 was the largest gene (234 annotations) and still entirely PENDING
- Prefoldin subunits (PFDN2-6, VBP1) were mostly stubs - batch-reviewed given shared function

## 2026-02-09 (session 1)

- Project initiated based on go-ontology#30962
- ~189 experimental annotations across all species to GO:0051082
- 5 experimental annotations to GO:0031249
- Key ontological debate: should we create holdase vs foldase subtypes, or use existing terms?
- Raymond suggests: ATP-dependent (foldase) vs ATP-independent (holdase) split
- Val notes SAN1 and Fbxo2 are "misfolded protein sensors" rather than chaperones
- No "holdase" GO term exists yet - GO:0044183 "protein folding chaperone" exists for foldase
- The prefoldin complex (PFDN1-6) functions as a co-chaperone for TRiC/CCT, delivering substrates

</details>
