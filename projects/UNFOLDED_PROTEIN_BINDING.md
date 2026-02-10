# Unfolded Protein Binding Annotation Review

## Context

GitHub issue: https://github.com/geneontology/go-ontology/issues/30962

GO:0051082 "unfolded protein binding" and GO:0031249 "denatured protein binding" are
proposed for obsoletion. The rationale is that "unfolded protein binding" is not a proper
molecular function -- the binding should be annotated to the actual activity (holdase,
foldase, disaggregase, transporter, ubiquitin ligase sensor, etc.).

## Replacement Terms

Potential replacement MF terms include:

- **GO:0044183** protein folding chaperone (aka foldase) - assists protein folding
- **GO:0140545** ATP-dependent protein disaggregase activity - solubilizes protein aggregates
- **GO:1904378** maintenance of unfolded protein involved in ERAD pathway
- Proposed new terms from issue discussion:
  - "holdase chaperone activity" (from #30552) - binds unfolded proteins to prevent aggregation WITHOUT actively folding them
  - "ATP-dependent unfolded protein binding activity (foldase type)"
  - "ATP-independent unfolded protein binding activity (holdase type)"
  - "misfolded protein sensor activity" - for E3 ligases/F-box proteins that detect misfolded substrates

## Categories of Annotated Proteins

Based on the ~189 experimental annotations across all species:

1. **HSP70 family (foldase chaperones)**: HSPA1A/B, HSPA2, HSPA6, HSPA8, HSPA1L, HSPA5 (BiP/GRP78), SSA1-4, SSB1-2, KAR2, DnaK, SSQ1, LHS1
2. **HSP90 system**: HSP82, HSC82, AHSA1, PTGES3, CPR6, CPR7, CDC37, AIP
3. **HSP40/DnaJ co-chaperones**: DNAJB1, DNAJB2, DNAJB6, DNAJB8, DNAJA2, DNAJA4, YDJ1, MDJ1, JEM1, Dnajb11, Dnaja3
4. **Small HSPs (holdases)**: CRYAA, CRYAB, HSPB6, Hsp22/23/26/27(Drosophila), HSP26(yeast)
5. **Chaperonin/TRiC/CCT**: TCP1, CCT2-8, GroEL, HSP60, HSP10
6. **Prefoldin complex**: PFDN1-6, VBP1, PFD1
7. **Disaggregase**: HSP104
8. **ER quality control**: UGGT1, ERLEC1, SYVN1, CNE1, EPS1, PDI1, EUG1, ROT1, IRE1
9. **Mitochondrial import/assembly**: TOMM20, TIM9, TIM10, COX20, PET100, SHY1, ATP10, ATP11, GRPEL1, Grpel2
10. **Ubiquitin/quality control sensors**: SYVN1 (E3 ligase), SAN1(yeast), Fbxo2(mouse)
11. **Other chaperone-like**: NPM1, CLU, SCG5, TMEM67, NAP1, GET3, SecB, SurA, Skp, Spy, HdeA/B
12. **Ribosome assembly factors**: SQT1, SYO1, YAR1, RRB1, TSR4, PNO1, ACL4, SHQ1
13. **Peroxiredoxins with chaperone function**: TSA1, pmp20, tpx1, CnoX, RidA
14. **Membrane protein chaperones**: SHR3, PHO86, GSF2, CHS7, NSG1, NSG2, VMA22, VPS45

## Priority: Human Genes

Focus on human genes first, as these are highest-impact for GO annotation.

### Tier 1 - Classical Chaperones (clear functional replacement)
- [x] HSPA1A (P0DMV8) - HSP70, foldase chaperone → MODIFY to GO:0044183 + GO:0140545
- [x] HSPA1B (P0DMV9) - HSP70, foldase chaperone → MODIFY to GO:0044183 + GO:0140545
- [x] HSPA2 (P54652) - HSP70, foldase chaperone → MODIFY to GO:0044183
- [x] HSPA6 (P17066) - HSP70, foldase chaperone → MODIFY to GO:0044183
- [x] HSPA8 (P11142) - HSC70, foldase chaperone → MODIFY to GO:0044183 + GO:0140545
- [x] HSPA1L (P34931) - HSP70, foldase chaperone → MODIFY to GO:0044183
- [x] DNAJB1 (P25685) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJB2 (P25686) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJB6 (O75190) - HSP40, holdase → MODIFY to GO:0044183 (holdase caveat)
- [x] DNAJB8 (Q8NHS0) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJA2 (O60884) - HSP40 co-chaperone → MODIFY to GO:0044183
- [x] DNAJA4 (Q8WW22) - HSP40 co-chaperone → MODIFY to GO:0044183

### Tier 2 - Small HSPs / Holdases
- [x] CRYAA (P02489) - alpha-crystallin, holdase → MODIFY to GO:0044183 (holdase caveat)
- [x] CRYAB (P02511) - alpha-crystallin, holdase → MODIFY to GO:0044183
- [x] HSPB6 (O14558) - small HSP, holdase → MODIFY to GO:0044183

### Tier 3 - Prefoldin Complex
- [x] PFDN1 (O60925) - prefoldin subunit → MODIFY to GO:0044183
- [x] PFDN2 (Q9UHV9) - prefoldin subunit → MODIFY to GO:0044183
- [x] PFDN4 (Q9NQP4) - prefoldin subunit → MODIFY to GO:0044183
- [x] PFDN5 (Q99471) - prefoldin subunit → MODIFY to GO:0044183 + GO:0003714 (transcription corepressor)
- [x] PFDN6 (O15212) - prefoldin subunit → MODIFY to GO:0044183
- [x] VBP1 (P61758) - prefoldin subunit 3 → MODIFY to GO:0044183

### Tier 4 - ER Quality Control
- [x] UGGT1 (Q9NYU2) - glycoprotein quality sensor → MARK_AS_OVER_ANNOTATED (substrate recognition for GT activity)
- [x] ERLEC1 (Q96DZ1) - ER lectin, ERAD → REMOVE
- [x] SYVN1 (Q86TM6) - E3 ligase, ERAD → REMOVE (substrate recognition for E3 ligase, not chaperone)

### Tier 5 - Other / Unusual
- [x] NPM1 (P06748) - nucleophosmin, histone chaperone → MODIFY to GO:0140713 + GO:0140142 + GO:0044183 + GO:0019901
- [x] CLU (P10909) - clusterin, extracellular holdase → MODIFY to GO:0044183 (holdase caveat)
- [x] SCG5 (P05408) - neuroendocrine protein 7B2 → MODIFY to GO:0044183
- [x] TOMM20 (Q15388) - mitochondrial import receptor → MARK_AS_OVER_ANNOTATED (signal recognition, not chaperone)
- [x] GRPEL1 (Q9HAV7) - GrpE homolog, nucleotide exchange factor → MODIFY to GO:0060211 + GO:0044183
- [x] AIP (O00170) - AH receptor interacting protein → MODIFY to GO:0051879
- [x] AHSA1 (O95433) - HSP90 co-chaperone → MARK_AS_OVER_ANNOTATED
- [x] PTGES3 (Q15185) - HSP90 co-chaperone / PGE synthase → MARK_AS_OVER_ANNOTATED
- [x] TMEM67 (Q5HYA8) - meckelin → MARK_AS_OVER_ANNOTATED

### Denatured Protein Binding (GO:0031249) - Human
- [x] HSPA1A (P0DMV8) - already in Tier 1

### Denatured Protein Binding (GO:0031249) - Other Species
- [ ] SAN1 (yeast) - E3 ligase, misfolded protein sensor
- [ ] Fbxo2 (mouse) - F-box protein, glycoprotein sensor
- [ ] HSPH1 (hamster) - Hsp110, holdase

---
# STATUS

## Overall Progress (2026-02-09) - COMPLETE

| Category | Total | Reviewed | Annotations Done | Core Functions | % Done |
|----------|-------|----------|-----------------|----------------|--------|
| Tier 1 - Classical Chaperones | 12 | 12 | 0 PENDING | 12/12 | 100% |
| Tier 2 - Small HSPs | 3 | 3 | 0 PENDING | 3/3 | 100% |
| Tier 3 - Prefoldin | 6 | 6 | 0 PENDING | 6/6 | 100% |
| Tier 4 - ER Quality Control | 3 | 3 | 0 PENDING | 3/3 | 100% |
| Tier 5 - Other | 9 | 9 | 0 PENDING | 9/9 | 100% |
| **Total Human** | **33** | **33** | **0 PENDING** | **33/33** | **100%** |
| Other Species | 3 | 0 | - | - | 0% |

### GO:0051082 replacement decisions (all 33 genes)
- **MODIFY → GO:0044183** (protein folding chaperone): 22 genes (HSP70s, DnaJs, small HSPs, prefoldin, CLU, SCG5, GRPEL1)
- **MODIFY → other terms**: 2 genes (NPM1 → GO:0140713 histone chaperone; AIP → GO:0051879 Hsp90 protein binding)
- **MARK_AS_OVER_ANNOTATED**: 5 genes (UGGT1, TOMM20, AHSA1, PTGES3, TMEM67)
- **REMOVE**: 2 genes (SYVN1, ERLEC1 - substrate recognition, not chaperone activity)
- **Additional disaggregase**: 3 genes also have GO:0140545 ATP-dependent protein disaggregase (HSPA1A, HSPA1B, HSPA8)

### Validation status
- All 33 genes pass validation (no ERRORs) except SYVN1 which has pre-existing title/supporting_text character encoding issues being fixed
- Warnings are mostly about supporting_text coverage (can be incrementally improved)

### What's remaining:
1. ~~Review remaining 7 stub genes~~ DONE
2. ~~Complete annotation review for all genes~~ DONE (0 PENDING across all 33 genes)
3. ~~Populate core_functions for all 33 genes~~ DONE
4. Coordinate with ontology editors on holdase term (DNAJB6, DNAJB8, CRYAA, CRYAB, HSPB6, CLU need holdase distinction)
5. Other species (SAN1/yeast, Fbxo2/mouse, HSPH1/hamster) - not started

# NOTES

## 2026-02-09 (session 5 - COMPLETION)

- **All 33 human genes fully complete**: 0 PENDING annotations, all core_functions populated
- Used parallel annotation-reviewer and core-function-synthesizer agents across 5 context windows
- HSPA8 was the largest gene (234 annotations) - completed with dedicated agent
- Prefoldin subunits (PFDN2-6, VBP1) batch-reviewed efficiently given shared function
- HSPA1A core_functions added last (agent got stuck, completed manually using HSPA1B as template)
- SYVN1 has minor supporting_text encoding issues (Greek α characters) being fixed
- Key insight: many genes annotated to GO:0051082 have distinct mechanisms (foldase vs holdase vs disaggregase vs sensor) that existing GO terms can capture
- Holdase-type genes (DNAJB6, DNAJB8, CRYAA, CRYAB, HSPB6, CLU) annotated to GO:0044183 with notes about holdase distinction pending ontology term creation

## 2026-02-09 (session 2 - status update)

- Comprehensive status audit performed
- 26/33 human genes have at least partial review (GO:0051082 annotation addressed)
- However, most genes have many remaining PENDING annotations (e.g. HSPA1A: 193 PENDING out of 197 total)
- The "reviewed" count only reflects the GO:0051082/GO:0031249 unfolded protein binding annotations being addressed
- HSPA8 is the largest gene (234 annotations) and still entirely PENDING - this should be next priority
- Prefoldin subunits (PFDN2-6, VBP1) are mostly stubs - these could likely be batch-reviewed since they share function
- core_functions not yet populated for any gene

## 2026-02-09 (session 1)

- Project initiated based on go-ontology#30962
- ~189 experimental annotations across all species to GO:0051082
- 5 experimental annotations to GO:0031249
- Key ontological debate: should we create holdase vs foldase subtypes, or use existing terms?
- Raymond suggests: ATP-dependent (foldase) vs ATP-independent (holdase) split
- Val notes SAN1 and Fbxo2 are "misfolded protein sensors" rather than chaperones
- No "holdase" GO term exists yet - GO:0044183 "protein folding chaperone" exists for foldase
- The prefoldin complex (PFDN1-6) functions as a co-chaperone for TRiC/CCT, delivering substrates
- Many annotated genes have diverse functions beyond unfolded protein binding
