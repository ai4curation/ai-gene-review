# Unfolded Protein Binding Annotation Review

> **Editor Brief (as of 2026-02-11, revised after editor feedback + go-ontology#30552 review):**
> GO:0051082 "unfolded protein binding" and GO:0031249 "denatured protein binding" are proposed
> for obsoletion ([go-ontology#30962](https://github.com/geneontology/go-ontology/issues/30962)).
> We reviewed all 33 human genes plus 3 non-human genes (SAN1/yeast, Fbxo2/mouse, HSPH1/hamster)
> with experimental annotations to these terms (~189 EXP annotations
> to GO:0051082 across all species). Each gene's GO:0051082/GO:0031249 annotation was reclassified to a
> mechanism-specific MF term. **Critical finding**: GO:0140309 "unfolded protein carrier activity"
> was created specifically for TIM carrier-holdases ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552))
> and does **not** fit in-situ holdases (crystallins, sHSPs, CLU). A general "holdase chaperone
> activity" term was discussed in #30552 but never created — this is now the primary NTR needed.
> **Decisions from GO editors are needed on**: (1) NTR for general holdase chaperone activity
> (non-carrier), (2) whether "misfolded protein sensor activity" should be created for E3
> ligases/F-box proteins, (3) how to annotate J-domain co-chaperone MF given that GO:0003767
> "co-chaperone activity" is obsolete, and (4) whether GO:0051082 obsoletion should be blocked
> until the holdase NTR exists. Detailed review YAMLs are in `genes/human/<GENE>/`.
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

Primary GO:0051082 reclassification decisions (mutually exclusive; 33 unique human genes):

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

Based on the ~189 experimental annotations across all species:

1. **HSP70 family (foldase/holdase, context-dependent)**: HSPA1A/B, HSPA2, HSPA6, HSPA8, HSPA1L, HSPA5 (BiP/GRP78), SSA1-4, SSB1-2, KAR2, DnaK, SSQ1, LHS1 — can function as foldase or holdase depending on conditions, clients, de novo vs quality control
2. **HSP90 system (co-chaperones)**: HSP82, HSC82, AHSA1 (ATPase activator), PTGES3 (mechanism unclear), CPR6, CPR7, CDC37, AIP
3. **HSP40/DnaJ co-chaperones (substrate adaptors + HSP70 activators)**: DNAJB1, DNAJB2, DNAJB6 (holdase-type), DNAJB8 (holdase-type), DNAJA2, DNAJA4, YDJ1, MDJ1, JEM1, Dnajb11, Dnaja3 — not independent foldases; activate HSP70 ATPase and deliver substrates
4. **Small HSPs (holdase)**: CRYAA, CRYAB, HSPB6, Hsp22/23/26/27(Drosophila), HSP26(yeast)
5. **Chaperonin/TRiC/CCT**: TCP1, CCT2-8, GroEL, HSP60, HSP10
6. **Prefoldin complex**: PFDN1-6, VBP1, PFD1
7. **Disaggregase**: HSP104
8. **ER quality control (sensor)**: UGGT1, ERLEC1, SYVN1, CNE1, EPS1, PDI1, EUG1, ROT1, IRE1
9. **Mitochondrial import/assembly**: TOMM20, TIM9, TIM10, COX20, PET100, SHY1, ATP10, ATP11, GRPEL1, Grpel2
10. **Ubiquitin/quality control (sensor)**: SYVN1 (E3 ligase), SAN1(yeast), Fbxo2(mouse)
11. **Other chaperone-like**: NPM1, CLU, SCG5, TMEM67, NAP1, GET3, SecB, SurA, Skp, Spy, HdeA/B
12. **Ribosome assembly factors**: SQT1, SYO1, YAR1, RRB1, TSR4, PNO1, ACL4, SHQ1
13. **Peroxiredoxins with chaperone function**: TSA1, pmp20, tpx1, CnoX, RidA
14. **Membrane protein chaperones**: SHR3, PHO86, GSF2, CHS7, NSG1, NSG2, VMA22, VPS45

---

# Session Log

<details>
<summary>Curation session notes (click to expand)</summary>

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
