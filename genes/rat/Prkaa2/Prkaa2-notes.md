# PRKAA2 Research Notes

## Key Research Findings

### Core Catalytic Function
PRKAA2 encodes the α2 catalytic subunit of AMPK, which has intrinsic serine/threonine kinase activity. The α2 isoform differs from α1 in tissue distribution and substrate specificity [PMID:8955377 "The alpha1 and alpha2 isoforms of the AMP-activated protein kinase have similar activities in rat liver but exhibit differences in substrate specificity in vitro"].

### Direct Substrates with Strong Evidence

1. **ACC (Acetyl-CoA Carboxylase)**: Direct phosphorylation inhibits fatty acid synthesis [PMID:12065578 "Coordinate regulation of malonyl-CoA decarboxylase, sn-glycerol-3-phosphate acyltransferase, and acetyl-CoA carboxylase by AMP-activated protein kinase in rat tissues in response to exercise"].

2. **PFK-2 (6-Phosphofructo-2-kinase)**: Direct phosphorylation at Ser466 activates the enzyme, promoting glycolysis during energy stress [PMID:11069105 "Heart PFK-2 was phosphorylated on Ser466 and activated by AMPK in vitro...AMPK-mediated PFK-2 activation is likely to be involved in the stimulation of heart glycolysis during ischaemia"].

3. **ChREBP**: Direct phosphorylation at Ser568 inhibits DNA binding, preventing lipogenic gene expression [PMID:11724780 "AMPK specifically phosphorylated Ser(568) of ChREBP. A S568A mutant of the ChREBP gene showed tight DNA binding and lost its fatty acid sensitivity"].

### Tissue-Specific Expression Patterns

- **Liver**: Highly expressed, critical for hepatic metabolism
- **Skeletal Muscle**: Essential for exercise-induced metabolic changes  
- **Heart**: Critical during ischemic stress
- **Adipose Tissue**: Responds to adrenergic stimulation [PMID:17253964]
- **Brain**: Specialized functions in neurons, recently discovered role in photoreceptors

### Recent Paradigm Shifts (2024)

#### Autophagy Regulation Controversy
Traditional view: AMPK → inhibits mTOR → activates autophagy
New evidence: AMPK may actually suppress autophagy under certain conditions, particularly amino acid starvation. This represents a major shift in understanding [Web search findings 2024].

#### Neuronal Specialization
2024 research identified PRKAA2-specific functions in photoreceptor neurons involving IMPDH (inosine monophosphate dehydrogenase) regulation, representing novel therapeutic targets.

### Energy Sensing Mechanisms

AMPK α2 responds to:
1. **AMP:ATP ratio changes**: Primary activation mechanism
2. **Upstream kinases**: LKB1 complex [PMID:14511394 "Complexes between the LKB1 tumor suppressor, STRD alpha/beta and MO25 alpha/beta are upstream kinases in the AMP-activated protein kinase cascade"]
3. **Calcium signaling**: [PMID:25788287 studies show calcium-dependent activation]
4. **Pharmacological activators**: Caffeine [PMID:19608206], AICAR, metformin

### Complex Assembly

AMPK functions as a heterotrimeric complex:
- α subunit (catalytic): PRKAA1 or PRKAA2
- β subunit (regulatory): bridges α and γ subunits [PMID:15695819 "AMP-activated protein kinase beta subunit tethers alpha and gamma subunits via its C-terminal sequence (186-270)"]
- γ subunit (regulatory): contains CBS domains for AMP/ATP binding

### Metabolic Integration Points

1. **Fatty Acid Homeostasis**: Inhibits synthesis (via ACC), promotes oxidation
2. **Glucose Homeostasis**: Context-dependent effects on glycolysis vs gluconeogenesis
3. **Cholesterol Homeostasis**: Inhibits HMGCR, reducing cholesterol synthesis
4. **Energy Homeostasis**: Master coordinator of anabolic vs catabolic balance

### Annotations Requiring Careful Review

**Strong Evidence (Accept)**:
- Kinase activities (AMP-activated, serine/threonine)
- ATP/nucleotide binding
- Fatty acid metabolic processes
- Energy homeostasis
- Glucose homeostasis

**Context-Dependent (Mark as Non-Core)**:
- Autophagy regulation (complex, bidirectional)
- Circadian rhythm regulation
- Cellular responses to specific stimuli

**Likely Over-Annotations (Consider Removal)**:
- Chromatin remodeling (likely indirect)
- Wnt signaling (likely indirect)  
- Steroid biosynthesis (should be "negative regulation")
- Histone H2BS36 kinase activity (overly specific without strong rat evidence)

### Future Research Directions

1. **Isoform-Specific Functions**: Better understanding α1 vs α2 specialization
2. **Tissue-Specific Mechanisms**: Detailed mechanisms in brain, heart, liver
3. **Therapeutic Targets**: IMPDH inhibition for photoreceptor disorders
4. **Autophagy Paradox**: Resolving conflicting evidence about AMPK's role in autophagy

### Methodology Notes

This analysis synthesized:
- Experimental papers cited in existing GO annotations
- Recent literature (2020-2024) from web searches
- Established reviews and comprehensive studies
- Tissue-specific functional studies

**Evidence Quality Assessment**:
- Direct biochemical evidence > Genetic evidence > Computational predictions
- In vivo studies > In vitro studies > Cell culture
- Multiple independent studies > Single study findings

## 2025-01-14 - Annotation Retirement Fix

**Issue**: Validation failure due to 25 annotations with `GO_REF:0000096` reference that no longer exist in the current GOA file.

**Root Cause**: The reference `GO_REF:0000096` ("Automated transfer of experimentally-verified manual GO annotation data to mouse-rat orthologs") has been retired from the GOA annotation pipeline and replaced with other reference systems like `GO_REF:0000121`.

**Action Taken**: Marked all 27 annotations with `original_reference_id: GO_REF:0000096` as `retired: true` to exclude them from GOA validation while preserving the annotation review work.

**Annotations Affected**: All annotations with ISO evidence type using GO_REF:0000096, including:
- GO:0031669 (cellular response to nutrient levels)
- GO:0004679 (AMP-activated protein kinase activity)
- GO:0004674 (protein serine/threonine kinase activity)
- GO:0140823 (histone H2BS36 kinase activity)
- GO:0042149 (cellular response to glucose starvation)
- Multiple other metabolic and regulatory terms

**Validation Status**: After marking these annotations as retired, the gene should pass GOA validation checks since retired annotations are now excluded from validation.

**Note**: These annotations represent legitimate functional information that was previously transferred from experimentally verified mouse/human data. The retirement only reflects changes in the GOA annotation pipeline, not changes in the underlying biology.

## Re-review 2026-10-10

Re-review after the GOA/UniProt refresh (commit a3cf70b6d). 193 rows in total.

### What GOA changed

- **Large turnover.** 25 rows were newly seeded and 36 rows were newly retired; 25 rows had
  already been retired before this refresh, so 61 rows are now retired in total (review text kept).
- Newly retired: the whole GO_REF:0000043 (UniProt keyword) IEA block (nucleotide binding, kinase
  activity, transferase activity, lipid/fatty acid/steroid/cholesterol metabolic and biosynthetic
  terms, autophagy, Wnt signaling, rhythmic process, metal ion binding, chromatin organization);
  the GO_REF:0000120 ATP binding, protein serine/threonine kinase activity and nucleus rows; the
  GO_REF:0000116 protein serine kinase activity row; the protein binding IPI from PMID:16648175;
  and 15 ISO GO_REF:0000121 rows (Golgi apparatus, ciliary basal body, cytoplasmic
  translation, cellular response to starvation and to amino acid starvation, TORC1 signaling,
  positive and negative regulation of translational initiation, protein localization to lysosome,
  protein K6-linked ubiquitination, positive regulation of TORC1 signaling, phosphatidylethanolamine
  and phosphatidylcholine biosynthesis, positive regulation of cytochrome c release, hepatocyte
  apoptotic process).
- Newly seeded (all resolved): donor-split ISO rows from human PRKAA2 (UniProtKB:P54646) and mouse
  Prkaa2 (MGI:MGI:1336173), ISS rows from P54646 and mouse UniProtKB:Q8BRK8, re-sourced IEA rows
  (EC:2.7.11.1, InterPro, UniProtKB-SubCell nucleus and late endosome), adiponectin-activated
  signaling pathway (ISO, P54646), and four EXP rows from UniProt catalytic-activity curation:
  GO:0047322 and GO:0106310 from PMID:2369897 (HMG-CoA reductase) and PMID:9029219 (acetyl-CoA
  carboxylase).

### Judgments

- EXP GO:0047322 from PMID:9029219 (an ACC paper) is ACCEPT: GO:0050405 [acetyl-CoA carboxylase]
  kinase activity is obsolete and replaced_by GO:0047322, whose xrefs include RHEA:20333 (the ACC
  reaction) [PMID:9029219 "Phosphorylation by AMPK increased the Km for ATP and acetyl-CoA."].
- Protein binding (GO:0005515): all three IPI rows are REMOVE (none left as MARK_AS_OVER_ANNOTATED).
  PFKFB2 and ChREBP are kinase substrates [PMID:11069105 "Heart PFK-2 was phosphorylated on Ser466
  and activated by AMPK"; PMID:11724780 "AMPK specifically phosphorylated Ser(568) of ChREBP."], so
  no binding-type MF is supported beyond the catalytic activity already annotated; the PMID:16648175
  partners are other AMPK subunits, captured by the complex row. Removal does not mean the
  interactions are false.
- Action changes on previously reviewed rows: protein kinase activity (IEA InterPro and IDA
  PMID:12065578) REMOVE -> MODIFY to AMP-activated protein kinase activity (too general, not wrong);
  protein-macromolecule adaptor activity (IDA PMID:15695819) REMOVE -> UNDECIDED (the earlier
  removal rested on the paper being about the beta subunit, which is not a valid basis for removing
  an experimental row); regulation of stress granule assembly (ISO mouse) MARK_AS_OVER_ANNOTATED ->
  KEEP_AS_NON_CORE [PMID:27430620 "Our studies identified multiple steps of de novo SG assembly that
  are controlled by the kinase."]; cellular response to prostaglandin E stimulus (ISO mouse)
  MARK_AS_OVER_ANNOTATED -> UNDECIDED (cached abstract of PMID:23479225 does not describe the AMPK
  experiment).
- Remaining MARK_AS_OVER_ANNOTATED active rows (regulation of microtubule cytoskeleton organization;
  positive regulation of protein localization) carry an explicit overshoot statement.
- Donor named in `reason` on every new ISO/ISS row; missing reasons added to three legacy rows
  (negative regulation of TOR signaling ISS; negative regulation of TORC1 signaling ISS and ISO).
- No stale `UniProtKB:` quotes remain (checker reports 0).
- Description: rat symbol used, activation mechanism (gamma-subunit nucleotide binding, Thr-172
  phosphorylation by LKB1/STK11) and mTORC1 substrates added.
- core_functions: added in_complex nucleotide-activated protein kinase complex; replaced negative
  regulation of TOR signaling with the more specific negative regulation of TORC1 signaling; the
  HMGCR/ACC kinase function is now linked to regulation of lipid metabolic process instead of
  cholesterol metabolic process (AMPK regulates, rather than executes, lipid metabolism).

### Open questions

- PMID:15695819 protein-macromolecule adaptor activity (IDA) on the alpha subunit needs a full-text
  check.
- PMID:23479225 (cellular response to prostaglandin E stimulus, mouse donor IGI) needs a full-text
  check of the AMPK experiment.
- Two advisory validator warnings remain because retired GO_REF:0000096 rows keep their legacy
  MARK_AS_OVER_ANNOTATED actions while the active GO_REF:0000121 rows were re-judged.
