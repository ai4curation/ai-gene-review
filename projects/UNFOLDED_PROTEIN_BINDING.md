# Unfolded Protein Binding Annotation Review

> **Editor Brief (as of 2026-02-09):**
> GO:0051082 "unfolded protein binding" and GO:0031249 "denatured protein binding" are proposed
> for obsoletion ([go-ontology#30962](https://github.com/geneontology/go-ontology/issues/30962)).
> We reviewed all 33 human genes with experimental annotations to these terms (~189 EXP annotations
> to GO:0051082 across all species). Each gene's GO:0051082 annotation was reclassified to a
> mechanism-specific MF term. **Decisions from GO editors are needed on**: (1) creation of a
> "holdase chaperone activity" term ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552)),
> and (2) whether "misfolded protein sensor activity" should be created for E3 ligases/F-box
> proteins that recognize misfolded substrates. Detailed review YAMLs are in `genes/human/<GENE>/`.
> Validate with: `just validate-all` (writes `reports/validation-all.tsv`).

## Terminology

These mechanism classes are used throughout this document:

| Term | Definition | ATP? | Example |
|------|-----------|------|---------|
| **Foldase** | Actively assists protein folding through iterative binding/release cycles | Yes | HSPA1A (HSP70) |
| **Holdase** | Binds unfolded/misfolded proteins to prevent aggregation; does not actively refold | No | CRYAB (alpha-crystallin) |
| **Disaggregase** | Solubilizes existing protein aggregates | Yes | HSPA1A (with DNAJ + HSPH1) |
| **Sensor** | Recognizes misfolded proteins as substrates for degradation (E3 ligase, lectin) | N/A | SYVN1 (HRD1), UGGT1 |

## Decision Rules

How GO:0051082 annotations were reclassified:

| Mechanism | Action | Replacement term | Rationale | Example |
|-----------|--------|-----------------|-----------|---------|
| Foldase (HSP70, DnaJ, prefoldin) | MODIFY | GO:0044183 protein folding chaperone | Active ATP-dependent folding | HSPA1A, DNAJB1, PFDN1 |
| Holdase (sHSP, crystallin, CLU) | MODIFY | GO:0044183 *(placeholder, see [holdase caveat](#holdase-caveat))* | Closest available; needs holdase term | CRYAA, HSPB6, CLU |
| Disaggregase (HSP70 subset) | MODIFY | GO:0140545 ATP-dependent protein disaggregase activity | Distinct disaggregation activity | HSPA1A, HSPA1B, HSPA8 |
| Co-chaperone NEF (GrpE-like) | REMOVE | *(none — not direct UPB)* | Regulates HSP70 nucleotide cycle, does not bind unfolded substrate directly | GRPEL1 |
| ER/quality control sensor | REMOVE or MARK_AS_OVER_ANNOTATED | *(none — not chaperones)* | Substrate recognition for ligase/GT, not chaperoning | SYVN1, ERLEC1, UGGT1 |
| HSP90 co-chaperone | MARK_AS_OVER_ANNOTATED | *(none — co-chaperone, not UPB)* | These assist HSP90, not direct unfolded protein binding | AHSA1, PTGES3, TMEM67 |
| Other specific MF | MODIFY | Gene-specific term | Function better captured by existing GO term | NPM1 → GO:0140713, AIP → GO:0051879 |

## Impact Summary

Primary GO:0051082 reclassification decisions (mutually exclusive; 33 unique human genes):

| Primary action | Count | Notes |
|--------|-------|-------------------|
| MODIFY → GO:0044183 | 23 | Foldase + holdase placeholder set |
| MODIFY → other specific MF | 2 | NPM1 (GO:0140713), AIP (GO:0051879) |
| MARK_AS_OVER_ANNOTATED | 5 | Sensor/co-chaperone cases where UPB overstates direct activity |
| REMOVE | 3 | SYVN1, ERLEC1, GRPEL1 |
| **Total** | **33** | |

Additional non-exclusive co-annotations:

| Additional term | Count | Genes |
|--------|-------|-------------------|
| GO:0140545 ATP-dependent protein disaggregase activity | 3 | HSPA1A, HSPA1B, HSPA8 |

## Before/After Examples

| Gene | Old annotation | New annotation | Evidence | Rationale |
|------|---------------|----------------|----------|-----------|
| HSPA1A | GO:0051082 unfolded protein binding (IDA, PMID:21231916) | GO:0044183 protein folding chaperone + GO:0140545 disaggregase | IDA | HSP70 is an ATP-dependent foldase; also disaggregates with DNAJ/HSPH1 |
| CRYAB | GO:0051082 unfolded protein binding (IDA, PMID:20159986) | GO:0044183 protein folding chaperone *(holdase placeholder)* | IDA | sHSP holdase; awaiting holdase GO term |
| SYVN1 | GO:0051082 unfolded protein binding (IDA, PMID:14593114) | REMOVE | IDA | HRD1 is an E3 ubiquitin ligase; recognizes misfolded substrates for degradation, not chaperoning |
| UGGT1 | GO:0051082 unfolded protein binding (IDA, PMID:24790089) | MARK_AS_OVER_ANNOTATED | IDA | Glycoprotein quality sensor for GT activity, not a chaperone |
| NPM1 | GO:0051082 unfolded protein binding (IDA, PMID:20625543) | GO:0140713 histone chaperone activity | IDA | Pentameric histone chaperone; UPB is secondary to core histone chaperoning |

## Open Ontology Gaps

Terms that **do not yet exist** in GO but are needed to properly annotate genes in this set:

1. **Holdase chaperone activity** ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552)) —
   ATP-independent binding of unfolded/misfolded proteins to prevent aggregation, without active refolding.
   Needed for: DNAJB6, DNAJB8, CRYAA, CRYAB, HSPB6, CLU (6 genes currently using GO:0044183 as placeholder).

2. **Misfolded protein sensor activity** — Recognition of misfolded protein substrates to target them for
   degradation (distinct from chaperone activity). Would apply to SYVN1, and to non-human genes SAN1 (yeast),
   Fbxo2 (mouse). Currently these are REMOVE/OVER_ANNOTATED since no appropriate MF term exists.

## What We Need from GO Editors

- [ ] Create "holdase chaperone activity" term (go-ontology#30552) — 6 human genes blocked on this
- [ ] Decide whether "misfolded protein sensor activity" warrants a new term — affects SYVN1 + non-human genes
- [ ] Confirm GO:0044183 is acceptable as interim annotation for holdases until holdase term exists
- [ ] Proceed with obsoletion of GO:0051082 and GO:0031249 once replacement terms are in place

---

## Replacement Terms (detailed)

Existing GO terms used as replacements:

- **GO:0044183** protein folding chaperone — assists protein folding *(existing)*
- **GO:0140545** ATP-dependent protein disaggregase activity — solubilizes protein aggregates *(existing)*
- **GO:0140713** histone chaperone activity — for NPM1 *(existing)*
- **GO:0051879** Hsp90 protein binding — for AIP *(existing)*
- **GO:0000774** adenyl-nucleotide exchange factor activity — core MF for GRPEL1 (UPB removed) *(existing)*

This project focuses on MF replacement for GO:0051082/GO:0031249. BP terms discussed in
individual gene reviews (for example GO:0030150 in GRPEL1) are not listed as MF replacements here.

Proposed new terms (not yet in GO):

- **"holdase chaperone activity"** ([go-ontology#30552](https://github.com/geneontology/go-ontology/issues/30552)) —
  Def: Binding of unfolded or misfolded proteins to prevent their aggregation, without actively catalyzing refolding.
  Synonyms: ATP-independent chaperone activity, anti-aggregation chaperone activity.
- **"misfolded protein sensor activity"** — Def: Recognition of misfolded protein conformation to initiate
  quality-control degradation. Distinct from chaperone activity.

### Holdase caveat

Several genes in this review are **holdases** rather than foldases. Holdases bind unfolded or
misfolded proteins to prevent their aggregation, but they lack ATPase activity and do **not**
actively refold substrates. This is mechanistically distinct from the ATP-dependent foldase
activity of HSP70-type chaperones.

There is currently no GO term for holdase chaperone activity (proposed in go-ontology#30552).
GO:0044183 "protein folding chaperone" is the closest available term, but it implies active
folding, which is not what holdases do. The affected genes (DNAJB6, DNAJB8, CRYAA, CRYAB,
HSPB6, CLU) are annotated to GO:0044183 as a pragmatic placeholder and should be updated to
a more specific holdase term once one is created in GO.

---

## Human Gene Checklist

33 unique human genes are in scope below. HSPA1A appears again in the GO:0031249 subsection
because it has that second term as well; this is not an additional human gene.

### Tier 1 - Classical Chaperones (foldase)
- [x] HSPA1A (P0DMV8) - HSP70, foldase → MODIFY to GO:0044183 + GO:0140545
- [x] HSPA1B (P0DMV9) - HSP70, foldase → MODIFY to GO:0044183 + GO:0140545
- [x] HSPA2 (P54652) - HSP70, foldase → MODIFY to GO:0044183
- [x] HSPA6 (P17066) - HSP70, foldase → MODIFY to GO:0044183
- [x] HSPA8 (P11142) - HSC70, foldase → MODIFY to GO:0044183 + GO:0140545
- [x] HSPA1L (P34931) - HSP70, foldase → MODIFY to GO:0044183
- [x] DNAJB1 (P25685) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJB2 (P25686) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJB6 (O75190) - HSP40, holdase → MODIFY to GO:0044183 (holdase, see [caveat](#holdase-caveat))
- [x] DNAJB8 (Q8NHS0) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJA2 (O60884) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJA4 (Q8WW22) - HSP40 co-chaperone → MODIFY to GO:0044183

### Tier 2 - Small HSPs / Holdases
- [x] CRYAA (P02489) - alpha-crystallin, holdase → MODIFY to GO:0044183 (holdase, see [caveat](#holdase-caveat))
- [x] CRYAB (P02511) - alpha-crystallin, holdase → MODIFY to GO:0044183
- [x] HSPB6 (O14558) - small HSP, holdase → MODIFY to GO:0044183

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
- [x] CLU (P10909) - clusterin, extracellular holdase → MODIFY to GO:0044183 (holdase, see [caveat](#holdase-caveat))
- [x] SCG5 (P05408) - neuroendocrine protein 7B2 → MODIFY to GO:0044183
- [x] TOMM20 (Q15388) - mitochondrial import receptor → MARK_AS_OVER_ANNOTATED
- [x] GRPEL1 (Q9HAV7) - GrpE homolog (NEF) → REMOVE (not direct unfolded-substrate binder; core MF GO:0000774)
- [x] AIP (O00170) - AH receptor interacting protein → MODIFY to GO:0051879
- [x] AHSA1 (O95433) - HSP90 co-chaperone → MARK_AS_OVER_ANNOTATED
- [x] PTGES3 (Q15185) - HSP90 co-chaperone / PGE synthase → MARK_AS_OVER_ANNOTATED
- [x] TMEM67 (Q5HYA8) - meckelin → MARK_AS_OVER_ANNOTATED

### GO:0031249 (denatured protein binding)
- HSPA1A (P0DMV8) - already in Tier 1 (same gene; listed here because it also has GO:0031249)
- [ ] SAN1 (yeast) - E3 ligase, misfolded protein sensor
- [ ] Fbxo2 (mouse) - F-box protein, glycoprotein sensor
- [ ] HSPH1 (hamster) - Hsp110, holdase

## Categories of Annotated Proteins (all species)

Based on the ~189 experimental annotations across all species:

1. **HSP70 family (foldase)**: HSPA1A/B, HSPA2, HSPA6, HSPA8, HSPA1L, HSPA5 (BiP/GRP78), SSA1-4, SSB1-2, KAR2, DnaK, SSQ1, LHS1
2. **HSP90 system**: HSP82, HSC82, AHSA1, PTGES3, CPR6, CPR7, CDC37, AIP
3. **HSP40/DnaJ co-chaperones**: DNAJB1, DNAJB2, DNAJB6, DNAJB8, DNAJA2, DNAJA4, YDJ1, MDJ1, JEM1, Dnajb11, Dnaja3
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
