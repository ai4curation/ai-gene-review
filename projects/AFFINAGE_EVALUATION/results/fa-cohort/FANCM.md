# FANCM (FANCM) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 41 discoveries · self-eval pairwise = win, faith 100% · gates passed.

## Agreement (brief)

Affinage and the AIGR review converge on FANCM's core biology: an **ATP-dependent DNA
translocase / branch-point migrase** that engages branched DNA (Holliday junctions,
replication forks, D-loops) and remodels it during replication stress; a **chromatin-targeting
scaffold** that loads the **Fanconi anemia core complex** onto chromatin and is required for
**FANCD2 monoubiquitination**; a stable partner of the **MHF1-MHF2 (CENPS-CENPX)** histone-fold
dimer and of **FAAP24**; and a regulator (not core enzyme) of homologous recombination that
suppresses **sister-chromatid exchange / crossovers**. Both cite the same primary sources for
these calls (PMID:20347428/20347429 MHF complex + fork remodeling; PMID:17289582 FAAP24;
PMID:29231814 FANCD2-monoub / germ-cell role). Affinage's narrative additionally foregrounds
the translocase-dependent **ATR/Chk1 checkpoint** and **replication traverse of ICLs** roles,
which the AIGR description mentioned but had not annotated — these are now incorporated (below).

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| GO grounding depth | Coarse `mechanism_profile`: ATP-dependent activity / DNA binding / catalytic activity acting on DNA / adaptor / regulator; localization = chromosome + nucleus | Granular, correctly-branched: GO:0015616 DNA translocase activity, GO:0009378 four-way junction helicase, GO:0000400 four-way junction DNA binding, GO:0071821 FANCM-MHF complex, GO:0043240 FA nuclear complex, GO:0000785 chromatin | **AIGR.** Affinage's own note concedes the profile collapses to general parents and can contradict the narrative. AIGR re-grounds from the narrative + PMIDs to specific terms. |
| "RNA helicase" identity | Narrative never claims RNA helicase, but the legacy alt-name "ATP-dependent RNA helicase FANCM" persists in databases | GO:0003724 RNA helicase activity (IEA, EC:3.6.4.13 mapping) → **REMOVE** | **AIGR.** FANCM acts on DNA, not RNA; the EC→GO mapping is a demonstrable over-mapping. Affinage's DNA-translocase narrative supports the removal. |
| 3'-5' helicase vs translocase | Narrative calls FANCM a "translocase and branch-point migrase" but does not correct the helicase term | GO:0043138 3'-5' DNA helicase (IBA+IEA) → **MODIFY → GO:0015616 DNA translocase activity** | **AIGR.** Human FANCM shows translocase/branch-migration, not processive duplex unwinding ("only translocase activity was observed", PMID:19423727). AIGR's finer distinction is correct. |
| Meiotic crossover control | Emphasizes conserved anti-crossover / D-loop-dissociation role (PMID:18851838 Fml1, PMID:32386601 Mph1) as a headline function | GO:0000712 resolution of meiotic recombination intermediates + GO:0035825 HR → **KEEP_AS_NON_CORE** | **AIGR.** The activity is genuine but, for human FANCM, tissue-specific/regulatory relative to ICL repair and fork remodeling; ortholog (yeast) evidence should not be promoted to a core human function. Correctly retained as non-core. |
| Telomere/ALT, synthetic lethality, PARPi resistance | ~10 discoveries on ALT-telomere R-loop suppression (PMID:31138795/97), BRCA1 & SMARCAL1 synthetic lethality (PMID:33882298, 39510066), PARPi resistance (PMID:38985669) | Not annotated | **AIGR (conservative).** These are largely context-specific / disease-therapeutic phenotypes and cancer-cell-line dependencies, not distinct molecular/cellular GO functions of FANCM; they are downstream of the same translocase/fork-remodeling activity already annotated. Correctly excluded from the annotation set (valuable narrative context, not new GO terms). |
| ATR/Chk1 checkpoint activation | Well-supported function (PMID:18995830, 20670894, 20057355, 23698467) | Was described in prose but **not annotated** | **Affinage surfaces a real gap.** Now added as a NEW annotation (GO:0000077, below). |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:18206976 | Primary biochemistry: FANCM binds Holliday junctions/forks with high specificity and promotes ATP-dependent branch migration through 2.6 kb | Added to `references` (HIGH, VERIFIED); attached as verbatim `supported_by` on GO:0000400 (four-way junction DNA binding), GO:0009378 (four-way junction helicase), and `core_functions` translocase. Strengthens IBA annotations that previously rested only on PMID:20347429. No action changed. |
| PMID:18995830 | FANCM/FAAP24 required for ATR/Chk1 checkpoint signaling; translocase-dependent, FA-core-independent | Added to `references` (HIGH, VERIFIED); basis for **one NEW annotation** GO:0000077 DNA damage checkpoint signaling (involved_in, IMP) with two verbatim `supported_by` quotes. |
| PMID:24207054 | FANCM/MHF translocase + DNA-binding activities promote replication traverse of ICLs (single-molecule DNA-fiber assay) | Added to `references` (HIGH, VERIFIED); attached as `supported_by` on GO:0036297 (ICL repair, IDA) and `core_functions` translocase. Corroborates existing ICL/translocase decisions. |

One NEW annotation added (GO:0000077, verified active biological_process term via QuickGO).
No existing decisions were weakened or reversed. Affinage's remaining ~35 discoveries
(structural studies, ALT/telomere biology, synthetic-lethality/PARPi, ortholog meiosis,
regulatory phosphorylation/degradation) are strong narrative context but map either to
functions already annotated or to disease/therapeutic phenotypes that are not distinct GO
functions; they are appropriately left out of the annotation set.

## Net assessment

Affinage's 41-discovery record is factually rich, PMID-dense, and fully aligned with AIGR on
FANCM's core translocase / FA-core-scaffold / MHF-complex / ICL-repair biology. Its concrete
value here was surfacing three primary papers that let the review (a) anchor its branch-migration
and four-way-junction annotations to the founding Gari 2008 biochemistry, (b) add the genuinely
missed **ATR/Chk1 checkpoint** function as a correctly-branched NEW annotation, and (c)
corroborate the ICL-traverse translocase role with the Huang 2013 single-molecule study. Its
weaknesses are the familiar ones: a coarse `mechanism_profile` GO layer (which AIGR replaces with
granular, correctly-branched terms and which does not correct the RNA-helicase / 3'-5'-helicase
mis-mappings AIGR fixes) and a narrative that elevates context-specific ALT/telomere,
synthetic-lethality, and ortholog-meiosis findings to headline status where AIGR keeps them
non-core or out of the GO annotation set. Net: the AIGR review remains more precise and better
scoped; Affinage contributed three well-evidenced references and one defensible new function.
