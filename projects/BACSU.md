---
title: "Bacillus subtilis project"
maturity: MATURE
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [BACSU]
genes: [fliH, fliK, fliW, fliY, gerD, spo0J, spoVAD, swrD, yddE, spo0A, sigF, ftsZ, divIVA, comK, aprE, amyE, sacB, secA, minC, sigE, sigG, sigK, spoIIE, minD, nprE, lipA, secY, comGA, spoIIGA, spoIIAA, spoIIAB, spoIIB, spoIIR, spoVD, yciC]
sidecars:
  slide_assets:
    - BACSU/slides/actions-bar.svg
    - BACSU/slides/sigG-review-table.jpg
    - BACSU/slides/sporulation-cascade.svg
manifest:
  slides:
    - href: BACSU/slides/BACSU-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/AuQCDtu8bJ3pAjSXuMRzAB
      title: Project brief
---

# Bacillus subtilis project

**Bottom line:** *Bacillus subtilis* is the model Gram-positive bacterium for
sporulation, competence, cell division and protein secretion. We reviewed all
GOA annotations on 35 genes: the original 29-gene set covering CACAO-heavy
flagellar/germination genes, key regulators, cell-division/secretion genes and
industrial enzymes, plus six follow-up reviews for the sigma-F partner switch,
spore-cortex synthesis, and ZagA/YciC zinc metallochaperone. The current cohort
has 396 review rows: 343 fetched GOA rows and 53 proposed `NEW` rows, with 225
ACCEPT, 37 KEEP_AS_NON_CORE, 47 MODIFY, 15 REMOVE, 16 MARK_AS_OVER_ANNOTATED
and 3 UNDECIDED. The recurring corrections were removing `RNA polymerase
activity` from sigma factors, removing a fold-based acyltransferase call on
spoVAD, and removing unsupported fliY/swrD rows that cite PMID:25313396, a
paper that does not examine those genes. All 35 reviews exist and render, and a
sporulation cascade pathway summary is in `BACSU/`. The remaining project work
is status finalisation: only 5 reviews are `COMPLETE`, while 26 are `DRAFT` and
4 are `IN_PROGRESS`; #4044 tracks those status decisions together with the
open per-gene re-review issues.

Use uniprot code BACSU

## Genes/proteins for which CACAO made major contributions

  | Gene   | UniProt ID                               | Protein                                 |
  |--------|------------------------------------------|-----------------------------------------|
  | fliH   | https://www.uniprot.org/uniprotkb/P23449 | Flagellar assembly protein FliH         |
  | fliK   | https://www.uniprot.org/uniprotkb/P23451 | Flagellar hook-length control protein   |
  | fliW   | https://www.uniprot.org/uniprotkb/P96503 | Flagellar assembly factor FliW          |
  | fliY   | https://www.uniprot.org/uniprotkb/P24073 | Flagellar motor switch phosphatase FliY |
  | gerD   | https://www.uniprot.org/uniprotkb/P16450 | Spore germination protein GerD          |
  | spo0J  | https://www.uniprot.org/uniprotkb/P26497 | Stage 0 sporulation protein J           |
  | spoVAD | https://www.uniprot.org/uniprotkb/P40869 | Stage V sporulation protein AD          |
  | swrD   | https://www.uniprot.org/uniprotkb/C0H412 | Swarming motility protein SwrD          |
  | yddE   | https://www.uniprot.org/uniprotkb/P96642 | ConE VirB4-like ATPase (ICEBs1 T4SS)    |

## Round 2 - Key functional genes

  | Gene   | UniProt ID                               | Protein                                 |
  |--------|------------------------------------------|-----------------------------------------|
  | spo0A  | https://www.uniprot.org/uniprotkb/P06534 | Sporulation master transcription factor |
  | sigF   | https://www.uniprot.org/uniprotkb/P07860 | RNA polymerase sigma-F factor           |
  | ftsZ   | https://www.uniprot.org/uniprotkb/P17865 | Cell division protein FtsZ              |
  | divIVA | https://www.uniprot.org/uniprotkb/P71021 | Cell division initiation protein DivIVA |
  | comK   | https://www.uniprot.org/uniprotkb/P40396 | Competence transcription factor         |
  | aprE   | https://www.uniprot.org/uniprotkb/P04189 | Subtilisin E (alkaline protease)        |
  | amyE   | https://www.uniprot.org/uniprotkb/P00691 | Alpha-amylase                           |
  | sacB   | https://www.uniprot.org/uniprotkb/P05655 | Levansucrase                            |
  | secA   | https://www.uniprot.org/uniprotkb/P28366 | Protein translocase subunit SecA        |
  | minC   | https://www.uniprot.org/uniprotkb/Q01463 | Division inhibitor MinC                 |

review these first

## Round 3 - Sporulation cascade completion + biotechnology

  | Gene   | UniProt ID                               | Protein                                 |
  |--------|------------------------------------------|-----------------------------------------|
  | sigE   | https://www.uniprot.org/uniprotkb/P06222 | RNA polymerase sigma-E factor           |
  | sigG   | https://www.uniprot.org/uniprotkb/P19940 | RNA polymerase sigma-G factor           |
  | sigK   | https://www.uniprot.org/uniprotkb/P12254 | RNA polymerase sigma-K factor           |
  | spoIIE | https://www.uniprot.org/uniprotkb/P37475 | Stage II sporulation protein E          |
  | minD   | https://www.uniprot.org/uniprotkb/Q01464 | Septum site-determining protein MinD    |
  | nprE   | https://www.uniprot.org/uniprotkb/P68736 | Extracellular neutral metalloprotease   |
  | lipA   | https://www.uniprot.org/uniprotkb/O32129 | Lipoyl synthase                         |
  | secY   | https://www.uniprot.org/uniprotkb/P16336 | Protein translocase subunit SecY        |
  | comGA  | https://www.uniprot.org/uniprotkb/P25953 | Competence protein ComGA                |
  | spoIIGA| https://www.uniprot.org/uniprotkb/P13801 | Stage II sporulation protein GA         |

## Follow-up sporulation and cofactor genes

  | Gene   | UniProt ID                               | Protein                                 |
  |--------|------------------------------------------|-----------------------------------------|
  | spoIIAA| https://www.uniprot.org/uniprotkb/P10727 | Anti-sigma-F antagonist                 |
  | spoIIAB| https://www.uniprot.org/uniprotkb/P10728 | Anti-sigma-F factor/kinase              |
  | spoIIB | https://www.uniprot.org/uniprotkb/P37575 | Stage II sporulation protein B          |
  | spoIIR | https://www.uniprot.org/uniprotkb/P39151 | Forespore signal protein                |
  | spoVD  | https://www.uniprot.org/uniprotkb/Q03524 | Spore cortex transpeptidase             |
  | yciC   | https://www.uniprot.org/uniprotkb/P94400 | ZagA zinc metallochaperone              |

 Why it's studied:
  - Model Gram-positive bacterium - counterpart to E. coli (Gram-negative)
  - GRAS status (Generally Recognized As Safe) - safe for food/industrial use
  - Natural competence - easily takes up DNA, great for genetic manipulation
  - Sporulation - forms endospores; model for cell differentiation and stress survival
  - Biofilm formation - forms complex multicellular communities

  Key genes by function:

  Sporulation (cell differentiation cascade):
  - spo0A - master regulator, initiates sporulation
  - sigF, sigE, sigG, sigK - compartment-specific sigma factors
  - spoIIAA, spoIIAB, spoIIE, spoIIR, spoIIGA - compartment-coupling switch

  Cell division:
  - ftsZ - tubulin homolog, forms Z-ring
  - minC/minD - positioning of division septum
  - divIVA - polar localization

  Competence/DNA uptake:
  - comK - master regulator of competence
  - comGA, comGB - DNA uptake machinery

  Biotechnology workhorses:
  - aprE - subtilisin (alkaline protease) - detergent enzymes
  - amyE - alpha-amylase - starch processing, commonly used integration locus
  - sacB - levansucrase - counter-selection marker (sucrose sensitivity)
  - nprE - neutral protease
  - lipA - lipoyl synthase

  Secretion system:
  - secA, secY - Sec pathway (major export route)
  - B. subtilis is favored industrially because it secretes proteins directly into medium (no periplasm like E. coli)

  Industrial applications:
  - Enzyme production (proteases, amylases, lipases) - ~60% of commercial enzymes
  - Vitamin B2 (riboflavin) production
  - Poly-γ-glutamic acid production
  - Probiotics (animal feed)
  - Biocontrol agents in agriculture

---
# STATUS

All 35 frontmatter genes have review YAML and rendered HTML. Current YAML
statuses:

| Status | Genes |
|--------|-------|
| COMPLETE | fliK, fliW, fliY, gerD, spoIIGA |
| IN_PROGRESS | minD, lipA, comGA, spoVD |
| DRAFT | fliH, spo0J, spoVAD, swrD, yddE, spo0A, sigF, ftsZ, divIVA, comK, aprE, amyE, sacB, secA, minC, sigE, sigG, sigK, spoIIE, nprE, secY, spoIIAA, spoIIAB, spoIIB, spoIIR, yciC |

- [ ] Finalise 26 DRAFT and 4 IN_PROGRESS YAML statuses (#4044)
- [ ] Resolve open per-gene re-review issues: #729, #736, #737, #745, #746, #748, #777, #820

# NOTES

## 2026-10-04

- Re-audited the project against the 35 genes now listed in frontmatter. The cohort has 396 review rows: 343 fetched GOA rows and 53 proposed NEW rows.
- Current action totals are 225 ACCEPT, 37 KEEP_AS_NON_CORE, 47 MODIFY, 15 REMOVE, 16 MARK_AS_OVER_ANNOTATED, 3 UNDECIDED, and 53 NEW.
- Corrected stale Round 3 accessions for sigG, sigK, spoIIE, minD, nprE, lipA, comGA, and spoIIGA, and fixed the lipA description to lipoyl synthase O32129 rather than lipase A.
- Added the six follow-up reviews missing from the body tables: spoIIAA, spoIIAB, spoIIB, spoIIR, spoVD, and yciC.
- Updated the sporulation pathway sidecar to include the SpoIIAA/SpoIIAB/SpoIIE partner-switch upstream of SigF and the SpoIIR signal between SigF and SpoIIGA.
- Opened #4044 to track finalising the 26 DRAFT and 4 IN_PROGRESS reviews and the open per-gene re-review issues.

## 2025-12-18 (Session 2)

**Round 3 complete!** All 10 sporulation cascade + biotechnology genes validated.

**Sporulation sigma factors:**
- sigE: 8 annotations reviewed. Mother cell sigma-E factor (sigma-29) cleaved from pro-sigmaE (P31) by SpoIIGA. MODIFY: GO:0003700 (TF activity) → GO:0016987 (sigma factor activity). ACCEPT sigma factor activity, sporulation.
- sigG: 14 annotations reviewed. Late forespore sigma-G factor regulated by anti-sigma Gin (CsfB). REMOVE GO:0003899 (RNAP activity) - sigma factors are NOT catalytic. REMOVE GO:0000976 (cis-regulatory binding) - sigma factors require core RNAP. NEW: GO:0045152 (antisigma factor binding), GO:0042601 (forespore localization).
- sigK: Validated with clean pass. Late mother cell sigma-K factor processed by SpoIVFB.

**Sporulation signaling:**
- spoIIE: 8 annotations reviewed. PP2C-family phosphatase that dephosphorylates SpoIIAA-P to activate SigF. ACCEPT phosphatase activities. Added supporting_text for PMID:25374563 findings (Y2H with RacA/RecA, in vitro dephosphorylation).
- spoIIGA: 13 annotations reviewed. Membrane-embedded aspartic protease that cleaves pro-sigmaE. MODIFY: GO:0030435/GO:0030436 (sporulation) → GO:0034301 (endospore formation) for specificity. MARK_AS_OVER_ANNOTATED: GO:0016787 (hydrolase) too general.

**Cell division:**
- minD: Validated with clean pass. Septum site-determining ATPase, MinC partner.

**Industrial enzymes:**
- nprE: 8 annotations reviewed. Bacillolysin (neutral protease), peptidase M4 family zinc metalloendopeptidase. ACCEPT metalloendopeptidase activity (GO:0004222). MODIFY: GO:0046872 (metal ion binding) → GO:0008270 (zinc ion binding) + GO:0005509 (calcium ion binding). MARK_AS_OVER_ANNOTATED: GO:0016787 (hydrolase) too general.
- lipA: 13 annotations reviewed. Lipoyl synthase, radical SAM enzyme inserting sulfur into octanoyl groups. MODIFY: GO:0003824 (catalytic activity) → GO:0016992 (lipoate synthase activity). ACCEPT all Fe-S cluster binding terms.

**Protein secretion:**
- secY: 12 annotations reviewed. SecYEG channel-forming subunit (10 TM helices). ACCEPT protein transmembrane transporter activity, signal sequence binding. KEEP_AS_NON_CORE: generic protein transport/targeting terms.

**Competence:**
- comGA: 6 annotations reviewed. AAA+ ATPase powering competence pseudopilus assembly. NEW: GO:0060187 (cell pole localization), GO:0009297 (pilus assembly). ACCEPT ATP hydrolysis activity.

**Summary of key decisions:**
- Sigma factors consistently: REMOVE RNAP catalytic activity, MODIFY TF activity → sigma factor activity
- Metal-binding terms: MODIFY generic metal ion binding → specific zinc/calcium binding where applicable
- Over-general terms (hydrolase activity): MARK_AS_OVER_ANNOTATED when more specific terms exist
- Sporulation terms: Use GO:0034301 (endospore formation) for B. subtilis specificity

## 2025-12-18

**Round 2 complete!** All 10 key functional genes validated. Summary of findings:

**Transcriptional regulators:**
- spo0A: 19 annotations reviewed. Master sporulation phosphorelay response regulator. Key actions: ACCEPT for phosphorelay signal transduction (GO:0000160), ACCEPT for DNA-binding TF activity (GO:0003700). Added supporting_text from publications. REMOVE calcium ion binding (not Ca²⁺-dependent).
- sigF: 13 annotations reviewed. Forespore-specific sigma-70 factor. Key actions: ACCEPT sigma factor activity (GO:0016987), REMOVE DNA-directed RNAP activity (sigma factors don't catalyze RNA synthesis - they confer promoter specificity), MODIFY general TF term to sigma factor activity.
- comK: 11 annotations reviewed. Competence master regulator. All IEA annotations validated.

**Cell division proteins:**
- ftsZ: 27 annotations reviewed. Tubulin-like GTPase. Key actions: ACCEPT GTPase activity (IDA from PMID:23577149), ACCEPT cell division (EXP), MARK_AS_OVER_ANNOTATED generic protein binding from high-throughput Y2H.
- divIVA: 18 annotations reviewed. Polar landmark/scaffold protein. Key actions: ACCEPT cytoskeletal protein binding, ACCEPT cell pole localization.
- minC: 7 annotations reviewed. FtsZ polymerization inhibitor. All annotations validated.

**Industrial enzymes:**
- aprE: 14 annotations reviewed. Subtilisin E serine endopeptidase. ACCEPT serine-type endopeptidase activity (GO:0004252).
- amyE: 12 annotations reviewed. Alpha-amylase. ACCEPT alpha-amylase activity (GO:0004556), starch metabolic process.
- sacB: 8 annotations reviewed. Levansucrase with dual activity (sucrose hydrolysis + fructan polymerization). ACCEPT both activities.

**Protein secretion:**
- secA: 18 annotations reviewed. Sec translocase ATPase. ACCEPT ATPase activity (GO:0016887), protein secretion (GO:0009306).

**Minor issues noted:**
- Some reviews have warnings for missing supporting_text in reference findings (sacB has 14 warnings, secA has 6 warnings)
- comK has warning about 0% supporting_text in existing annotations

## 2025-12-17

Starting BACSU project review. fliW was already reviewed and validated - it has comprehensive coverage of the flagellar assembly factor role and partner-switching mechanism with CsrA.

**Session progress:**
- fliW: Pre-existing complete review
- fliH: Reviewed but has UNDECIDED annotations - PMID:25313396 doesn't mention fliH in abstract/minimal components. Proposed GO:0042030 (ATPase inhibitor activity) based on Salmonella FliH studies.
- fliK: Complete - hook-length control protein. PMID:22730131 directly demonstrates "FliK regulated hook length". Fixed incorrect GO:0009424 (hook CC) - FliK is NOT a structural component.
- fliY: Complete - bifunctional protein with 17 annotations. CheY-P phosphatase activity (IDA from PMID:12920116) well-supported. Removed incorrect GO:0003774 (motor activity) and unsupported PMID:25313396 annotations.

**Key finding about PMID:25313396**: This paper lists minimal components for FlgM secretion (FliO, FliP, FliQ, FliR, FlhA, FlhB, FliF, FliG, FliK) - notably MISSING fliH, fliY, fliW, swrD. CACAO annotations citing this paper for genes not in the minimal list need scrutiny.

**Session 2 progress (completed 2025-12-17):**
- gerD: Germinosome scaffold protein for spore germination. Proposed new GO term for "germinosome".
- spo0J: ParB/CTP-dependent DNA-sliding clamp for chromosome segregation. Proposed 6 new annotations.
- spoVAD: SpoVA Ca-DPA channel plug. REMOVED incorrect GO:0016746 (acyltransferase) annotation - fold misprediction.
- swrD: Flagellar motor power enhancer via MotAB stator modulation. REMOVED erroneous PMID:25313396 annotation.
- yddE: NOT uncharacterized! ConE VirB4-like ATPase for ICEBs1 conjugation. Updated to reflect known function.

**Key issues identified:**
1. PMID:25313396 erroneously cited for swrD (and fliH, fliY, fliW) - paper doesn't mention these genes
2. spoVAD incorrectly annotated as acyltransferase based on thiolase-like fold
3. yddE is well-characterized as ConE but labeled "uncharacterized" in UniProt
