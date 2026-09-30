---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-26T01:18:54.056086'
end_time: '2026-09-26T01:31:10.467191'
duration_seconds: 736.41
template_file: templates/module_research.md.j2
template_variables:
  module_title: "Carotenoid biosynthesis I \u2014 carotene backbone (GGPP -> phytoene\
    \ -> lycopene -> cyclic carotenes)"
  module_summary: 'The carotene backbone segment of carotenoid biosynthesis converts
    two molecules of the C20 isoprenoid geranylgeranyl diphosphate (GGPP) into the
    C40 cyclic carotenes that seed every downstream carotenoid class. Phytoene synthase
    performs the head-to-head condensation that commits GGPP to carotenoids, giving
    15-cis-phytoene. Phytoene is then desaturated to all-trans-lycopene by one of
    two mutually exclusive routes: a single FAD-dependent CrtI-type desaturase in
    most bacteria and fungi, or the four-enzyme poly-cis route of cyanobacteria and
    plants (PDS, Z-ISO, ZDS, CRTISO) in which two plastoquinone-dependent desaturases
    each introduce two double bonds and two isomerases convert the poly-cis intermediates
    to the all-trans product. Lycopene cyclases then form beta rings (giving gamma-
    and beta-carotene) or, in plants, one epsilon ring (giving delta- and alpha-carotene).
    Supply of GGPP, xanthophyll formation by ring hydroxylation and epoxidation, ketolation,
    and oxidative cleavage to apocarotenoids (retinal, abscisic acid, strigolactones,
    neurosporaxanthin) are outside this module.'
  module_outline: "- Carotene backbone biosynthesis (GGPP -> phytoene -> lycopene\
    \ -> cyclic carotenes)\n  - 1. Phytoene synthesis (commitment of GGPP to carotenoids)\n\
    \  - Phytoene synthase step (2 GGPP -> 15-cis-phytoene)\n    - 15-cis-phytoene\
    \ synthase activity (molecular player: Phytoene synthase (PSY/CrtB) family; activity\
    \ or role: 15-cis-phytoene synthase activity)\n  - 2. Desaturation and isomerization\
    \ of phytoene to all-trans-lycopene\n  - Phytoene -> all-trans-lycopene (four\
    \ desaturations)\n    - Alternative versions by desaturase enzyme system: Phytoene\
    \ desaturation route\n      - CrtI-type single-enzyme desaturation\n        -\
    \ Lycopene-forming phytoene desaturase activity (molecular player: CrtI-type phytoene\
    \ desaturase family; activity or role: phytoene dehydrogenase activity)\n    \
    \  - Poly-cis desaturation/isomerization route (PDS, Z-ISO, ZDS, CRTISO)\n   \
    \     - 1. Phytoene desaturation to tri-cis-zeta-carotene\n        - PDS step\
    \ (15-cis-phytoene -> 9,15,9'-tri-cis-zeta-carotene)\n          - 15-cis-phytoene\
    \ desaturase activity (molecular player: PDS/CrtP 15-cis-phytoene desaturase family;\
    \ activity or role: phytoene dehydrogenase activity)\n        - 2. 15-cis isomerization\
    \ of tri-cis-zeta-carotene\n        - Z-ISO step (9,15,9'-tri-cis- -> 9,9'-di-cis-zeta-carotene)\n\
    \          - 15-cis-zeta-carotene isomerase activity (molecular player: Z-ISO\
    \ 15-cis-zeta-carotene isomerase family; activity or role: 9,15,9'-tri-cis-zeta-carotene\
    \ isomerase activity)\n        - 3. Zeta-carotene desaturation to prolycopene\n\
    \        - ZDS step (9,9'-di-cis-zeta-carotene -> 7,7',9,9'-tetra-cis-lycopene)\n\
    \          - Zeta-carotene desaturase activity (molecular player: ZDS/CrtQ zeta-carotene\
    \ desaturase family; activity or role: 9,9'-di-cis-zeta-carotene desaturase activity)\n\
    \        - 4. Prolycopene isomerization to all-trans-lycopene\n        - CRTISO\
    \ step (7,7',9,9'-tetra-cis-lycopene -> all-trans-lycopene)\n          - Prolycopene\
    \ isomerase activity (molecular player: CRTISO/CrtH prolycopene isomerase family;\
    \ activity or role: carotenoid isomerase activity)\n  - 3. Cyclization of lycopene\
    \ to cyclic carotenes\n  - Lycopene cyclization (lycopene -> beta-carotene or\
    \ alpha-carotene)\n    - 1. Beta-ring cyclization\n    - Beta cyclization (lycopene\
    \ -> gamma-carotene -> beta-carotene)\n      - Alternative versions by enzyme\
    \ family: Lycopene beta-cyclase implementation\n        - LCYB/CrtL-type lycopene\
    \ beta-cyclase\n          - CrtL-type lycopene beta cyclase activity (molecular\
    \ player: CrtL-type lycopene beta-cyclase subfamily; activity or role: lycopene\
    \ beta cyclase activity)\n          - Plant LCYB lycopene beta cyclase activity\
    \ (molecular player: Plant LCYB lycopene beta-cyclase subfamily; activity or role:\
    \ lycopene beta cyclase activity)\n        - CrtY-type lycopene beta-cyclase\n\
    \          - CrtY lycopene beta cyclase activity (molecular player: CrtY-type\
    \ lycopene beta-cyclase family; activity or role: lycopene beta cyclase activity)\n\
    \        - Bifunctional phytoene synthase/lycopene cyclase (fungal)\n        \
    \  - Bifunctional al-2 lycopene beta cyclase activity (molecular player: Bifunctional\
    \ lycopene cyclase/phytoene synthase family (cyclase domain); activity or role:\
    \ lycopene beta cyclase activity)\n    - 2. Epsilon-ring cyclization (alpha-carotene\
    \ branch)\n    - Epsilon cyclization (lycopene -> delta-carotene)\n      - Lycopene\
    \ epsilon cyclase activity (molecular player: LCYE lycopene epsilon-cyclase family;\
    \ activity or role: lycopene epsilon cyclase activity)"
  module_connections: '- Phytoene synthase step (2 GGPP -> 15-cis-phytoene) feeds
    into Phytoene -> all-trans-lycopene (four desaturations): Phytoene synthase supplies
    15-cis-phytoene to the desaturation step.

    - Phytoene -> all-trans-lycopene (four desaturations) feeds into Lycopene cyclization
    (lycopene -> beta-carotene or alpha-carotene): The desaturation route supplies
    all-trans-lycopene to the cyclases.

    - PDS step (15-cis-phytoene -> 9,15,9''-tri-cis-zeta-carotene) feeds into Z-ISO
    step (9,15,9''-tri-cis- -> 9,9''-di-cis-zeta-carotene): PDS supplies tri-cis-zeta-carotene
    to Z-ISO.

    - Z-ISO step (9,15,9''-tri-cis- -> 9,9''-di-cis-zeta-carotene) feeds into ZDS
    step (9,9''-di-cis-zeta-carotene -> 7,7'',9,9''-tetra-cis-lycopene): Z-ISO supplies
    di-cis-zeta-carotene to ZDS.

    - ZDS step (9,9''-di-cis-zeta-carotene -> 7,7'',9,9''-tetra-cis-lycopene) feeds
    into CRTISO step (7,7'',9,9''-tetra-cis-lycopene -> all-trans-lycopene): ZDS supplies
    prolycopene to CRTISO.

    - Epsilon cyclization (lycopene -> delta-carotene) feeds into Beta cyclization
    (lycopene -> gamma-carotene -> beta-carotene): In the alpha-carotene branch the
    epsilon cyclase acts first and a beta cyclase completes the second ring.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 2400
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 28
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: carotene_backbone_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: carotene_backbone_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Carotenoid biosynthesis I — carotene backbone (GGPP -> phytoene -> lycopene -> cyclic carotenes)

## Working Scope

The carotene backbone segment of carotenoid biosynthesis converts two molecules of the C20 isoprenoid geranylgeranyl diphosphate (GGPP) into the C40 cyclic carotenes that seed every downstream carotenoid class. Phytoene synthase performs the head-to-head condensation that commits GGPP to carotenoids, giving 15-cis-phytoene. Phytoene is then desaturated to all-trans-lycopene by one of two mutually exclusive routes: a single FAD-dependent CrtI-type desaturase in most bacteria and fungi, or the four-enzyme poly-cis route of cyanobacteria and plants (PDS, Z-ISO, ZDS, CRTISO) in which two plastoquinone-dependent desaturases each introduce two double bonds and two isomerases convert the poly-cis intermediates to the all-trans product. Lycopene cyclases then form beta rings (giving gamma- and beta-carotene) or, in plants, one epsilon ring (giving delta- and alpha-carotene). Supply of GGPP, xanthophyll formation by ring hydroxylation and epoxidation, ketolation, and oxidative cleavage to apocarotenoids (retinal, abscisic acid, strigolactones, neurosporaxanthin) are outside this module.

## Provisional Biological Outline

- Carotene backbone biosynthesis (GGPP -> phytoene -> lycopene -> cyclic carotenes)
  - 1. Phytoene synthesis (commitment of GGPP to carotenoids)
  - Phytoene synthase step (2 GGPP -> 15-cis-phytoene)
    - 15-cis-phytoene synthase activity (molecular player: Phytoene synthase (PSY/CrtB) family; activity or role: 15-cis-phytoene synthase activity)
  - 2. Desaturation and isomerization of phytoene to all-trans-lycopene
  - Phytoene -> all-trans-lycopene (four desaturations)
    - Alternative versions by desaturase enzyme system: Phytoene desaturation route
      - CrtI-type single-enzyme desaturation
        - Lycopene-forming phytoene desaturase activity (molecular player: CrtI-type phytoene desaturase family; activity or role: phytoene dehydrogenase activity)
      - Poly-cis desaturation/isomerization route (PDS, Z-ISO, ZDS, CRTISO)
        - 1. Phytoene desaturation to tri-cis-zeta-carotene
        - PDS step (15-cis-phytoene -> 9,15,9'-tri-cis-zeta-carotene)
          - 15-cis-phytoene desaturase activity (molecular player: PDS/CrtP 15-cis-phytoene desaturase family; activity or role: phytoene dehydrogenase activity)
        - 2. 15-cis isomerization of tri-cis-zeta-carotene
        - Z-ISO step (9,15,9'-tri-cis- -> 9,9'-di-cis-zeta-carotene)
          - 15-cis-zeta-carotene isomerase activity (molecular player: Z-ISO 15-cis-zeta-carotene isomerase family; activity or role: 9,15,9'-tri-cis-zeta-carotene isomerase activity)
        - 3. Zeta-carotene desaturation to prolycopene
        - ZDS step (9,9'-di-cis-zeta-carotene -> 7,7',9,9'-tetra-cis-lycopene)
          - Zeta-carotene desaturase activity (molecular player: ZDS/CrtQ zeta-carotene desaturase family; activity or role: 9,9'-di-cis-zeta-carotene desaturase activity)
        - 4. Prolycopene isomerization to all-trans-lycopene
        - CRTISO step (7,7',9,9'-tetra-cis-lycopene -> all-trans-lycopene)
          - Prolycopene isomerase activity (molecular player: CRTISO/CrtH prolycopene isomerase family; activity or role: carotenoid isomerase activity)
  - 3. Cyclization of lycopene to cyclic carotenes
  - Lycopene cyclization (lycopene -> beta-carotene or alpha-carotene)
    - 1. Beta-ring cyclization
    - Beta cyclization (lycopene -> gamma-carotene -> beta-carotene)
      - Alternative versions by enzyme family: Lycopene beta-cyclase implementation
        - LCYB/CrtL-type lycopene beta-cyclase
          - CrtL-type lycopene beta cyclase activity (molecular player: CrtL-type lycopene beta-cyclase subfamily; activity or role: lycopene beta cyclase activity)
          - Plant LCYB lycopene beta cyclase activity (molecular player: Plant LCYB lycopene beta-cyclase subfamily; activity or role: lycopene beta cyclase activity)
        - CrtY-type lycopene beta-cyclase
          - CrtY lycopene beta cyclase activity (molecular player: CrtY-type lycopene beta-cyclase family; activity or role: lycopene beta cyclase activity)
        - Bifunctional phytoene synthase/lycopene cyclase (fungal)
          - Bifunctional al-2 lycopene beta cyclase activity (molecular player: Bifunctional lycopene cyclase/phytoene synthase family (cyclase domain); activity or role: lycopene beta cyclase activity)
    - 2. Epsilon-ring cyclization (alpha-carotene branch)
    - Epsilon cyclization (lycopene -> delta-carotene)
      - Lycopene epsilon cyclase activity (molecular player: LCYE lycopene epsilon-cyclase family; activity or role: lycopene epsilon cyclase activity)

## Known Relationships Among Steps

- Phytoene synthase step (2 GGPP -> 15-cis-phytoene) feeds into Phytoene -> all-trans-lycopene (four desaturations): Phytoene synthase supplies 15-cis-phytoene to the desaturation step.
- Phytoene -> all-trans-lycopene (four desaturations) feeds into Lycopene cyclization (lycopene -> beta-carotene or alpha-carotene): The desaturation route supplies all-trans-lycopene to the cyclases.
- PDS step (15-cis-phytoene -> 9,15,9'-tri-cis-zeta-carotene) feeds into Z-ISO step (9,15,9'-tri-cis- -> 9,9'-di-cis-zeta-carotene): PDS supplies tri-cis-zeta-carotene to Z-ISO.
- Z-ISO step (9,15,9'-tri-cis- -> 9,9'-di-cis-zeta-carotene) feeds into ZDS step (9,9'-di-cis-zeta-carotene -> 7,7',9,9'-tetra-cis-lycopene): Z-ISO supplies di-cis-zeta-carotene to ZDS.
- ZDS step (9,9'-di-cis-zeta-carotene -> 7,7',9,9'-tetra-cis-lycopene) feeds into CRTISO step (7,7',9,9'-tetra-cis-lycopene -> all-trans-lycopene): ZDS supplies prolycopene to CRTISO.
- Epsilon cyclization (lycopene -> delta-carotene) feeds into Beta cyclization (lycopene -> gamma-carotene -> beta-carotene): In the alpha-carotene branch the epsilon cyclase acts first and a beta cyclase completes the second ring.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

# Carotenoid Biosynthesis I — The Carotene Backbone (GGPP → Phytoene → Lycopene → Cyclic Carotenes)

*A commissioned review-style synthesis for a molecular-biology audience*

---

## 1. Executive Summary

The **carotene backbone** is the committed core of carotenoid biosynthesis: the segment that converts two molecules of the C20 isoprenoid geranylgeranyl diphosphate (**GGPP**) into the C40 cyclic carotenes (β-, α-, and γ-carotene) that seed every downstream carotenoid class. It comprises exactly three chemical operations executed in a fixed order: (i) a head-to-head condensation of two GGPP into 15-*cis*-phytoene by **phytoene synthase (PSY/CrtB)**, the first committed and rate-limiting step; (ii) four sequential desaturations, accompanied by *cis→trans* isomerizations, that convert colorless phytoene into red **all-*trans*-lycopene**; and (iii) cyclization of one or both ends of lycopene into β- and/or ε-ionone rings by **lycopene cyclases**. Everything upstream (GGPP supply from the MEP/MVA isoprenoid pools) and everything downstream (hydroxylation, epoxidation, ketolation, and oxidative cleavage to apocarotenoids such as retinal, abscisic acid, and strigolactones) lies outside the module.

The defining feature of the backbone — and the single most important organizing principle for readers — is that the pathway solves the same chemical problem by **two mutually exclusive but functionally interchangeable desaturation routes**. Most bacteria and fungi use a single, FAD-dependent, membrane-peripheral **CrtI-type desaturase** that performs all four dehydrogenations and delivers all-*trans*-lycopene directly. Cyanobacteria, algae, and plants instead use a **four-enzyme poly-*cis* route** — two plastoquinone-dependent desaturases (**PDS/CrtP** and **ZDS/CrtQ**) that each introduce two double bonds, plus two isomerases (**Z-ISO** and **CRTISO/CrtH**) that convert *cis* intermediates to the all-*trans* product. That the bacterial CrtI can substitute for the entire four-enzyme plant machinery *in planta* (the basis of Golden Rice) is direct proof that the two routes are functionally equivalent at the level of net chemistry, even though they differ completely in enzymology, cofactors, electron acceptors, and regulatory/signaling consequences.

Cyclization is likewise solved by **at least four structurally unrelated cyclase families** (CrtY; CrtL-type, including plant LCYB and LCYE; the fungal bifunctional phytoene-synthase/cyclase CrtYB/al-2; and the CruA/CruP family of green sulfur bacteria and cyanobacteria). The pathway has deep prokaryotic roots; the plant plastid machinery was inherited from cyanobacteria via endosymbiosis. Below we lay out the boundaries, mechanism, molecular players, evolutionary and cell-biological variation, ordering constraints, and open controversies, anchoring each major claim in primary literature.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The carotene backbone module is defined by three obligatory transformations and the enzymes that carry them out:

| Step | Substrate → Product | Enzyme family | Chemistry |
|------|--------------------|--------------|-----------|
| Commitment | 2 × GGPP → 15-*cis*-phytoene | PSY / CrtB | Head-to-head condensation |
| Desaturation | 15-*cis*-phytoene → all-*trans*-lycopene | CrtI **or** (PDS + Z-ISO + ZDS + CRTISO) | 4 dehydrogenations + isomerizations |
| Cyclization | lycopene → β-/α-/γ-carotene | CrtY / CrtL (LCYB, LCYE) / CrtYB / CruA-CruP | β- and/or ε-ring formation |

The output of the module — the cyclic carotenes — is the branch point that feeds all downstream carotenoid chemistry.

### 2.2 What is adjacent but excluded

Several neighboring processes are frequently discussed alongside the backbone but are mechanistically separate and should be treated as boundaries, not contents:

- **GGPP supply.** The provision of GGPP from the plastidial MEP pathway (or cytosolic MVA in fungi) and by GGPP synthase is upstream. Notably, PSY does not act in isolation from this supply: PSY–GGPPS protein–protein interaction strength is itself a determinant of flux ([PMID: 40826491](https://pubmed.ncbi.nlm.nih.gov/40826491/)), which blurs the boundary at the commitment step but does not move it.
- **Xanthophyll formation.** Ring hydroxylation (non-heme di-iron CHY enzymes and P450 CYP97 hydroxylases), epoxidation (the xanthophyll cycle), and ketolation act on the cyclic carotenes and are downstream ([PMID: 21450689](https://pubmed.ncbi.nlm.nih.gov/21450689/), [PMID: 22513258](https://pubmed.ncbi.nlm.nih.gov/22513258/)).
- **Apocarotenoid cleavage.** Oxidative cleavage by carotenoid cleavage dioxygenases to retinal, abscisic acid, strigolactones, and neurosporaxanthin is downstream ([PMID: 33258195](https://pubmed.ncbi.nlm.nih.gov/33258195/)). The one caveat — important and returned to below — is that *linear cis-carotene intermediates of the desaturation step are themselves a substrate for a signaling apocarotenoid*, so the module has an internal regulatory output that is not merely feed-forward.
- **Photosynthetic function of carotenoids.** The structural/photoprotective roles of carotenoids in PSI/PSII reaction centers and light-harvesting complexes ([PMID: 23896007](https://pubmed.ncbi.nlm.nih.gov/23896007/)) are consequences of the products, not part of the biosynthetic module.

### 2.3 Competing definitions

The literature is largely consistent on the boundaries, but there are two genuine ambiguities. First, whether **PTOX (plastid terminal oxidase)** belongs "inside" the module: it is not a carotenoid enzyme, yet it is an obligatory redox cofactor of the plant desaturation step (§6), so functionally it is part of the machinery even though it is physically a component of the plastoquinone/photosynthetic electron-transport system. Second, in fungi the **commitment and cyclization steps are fused** into a single bifunctional CrtYB/al-2 polypeptide ([PMID: 11862485](https://pubmed.ncbi.nlm.nih.gov/11862485/)), so the "three separate operations" framing is a plant/bacterial abstraction rather than a universal architecture.

---

## 3. Mechanistic Overview

### 3.1 The best current model, step by step

```
        2 × GGPP (C20)
           │  PSY / CrtB  (head-to-head condensation; committed, rate-limiting)
           ▼
     15-cis-phytoene (C40, colorless)
           │
     ┌─────┴───────────────────────────────────────────┐
     │ ROUTE A (most bacteria, fungi)                   │ ROUTE B (cyanobacteria, algae, plants)
     │ single FAD-dependent CrtI                        │ four-enzyme poly-cis route
     │  (4 dehydrogenations, direct all-trans)          │
     │                                                  │  PDS/CrtP: +2 bonds → 9,15,9'-tri-cis-ζ-carotene
     │                                                  │  Z-ISO:    15-cis isomerization → 9,9'-di-cis-ζ-carotene
     │                                                  │  ZDS/CrtQ: +2 bonds → 7,9,7',9'-tetra-cis-lycopene
     │                                                  │  CRTISO/CrtH: cis→trans → all-trans-lycopene
     └─────┬───────────────────────────────────────────┘
           ▼
     all-trans-lycopene (C40, red)
           │
     ┌─────┴─────────────────────┐
     │ β-cyclization             │ ε-cyclization (plants/algae only)
     │ LCYB/CrtY/CrtYB/CruA-CruP │ LCYE
     ▼                           ▼
  γ-carotene (mono)          δ-carotene (mono, one ε-ring)
     │ (second β-ring)           │ (LCYB adds one β-ring)
     ▼                           ▼
  β-carotene (β,β)           α-carotene (β,ε)
```

### 3.2 Obligatory, conditional, and accessory steps

- **Obligatory:** PSY-catalyzed condensation (no phytoene, no pathway); the four net desaturations (colorless phytoene must become colored lycopene); at least one cyclization to make a cyclic carotene.
- **Conditional (route-dependent):** In Route B all four enzymes are individually required to reach all-*trans*-lycopene — but the *entire* Route B set is dispensable if Route A's CrtI is present, because CrtI performs the whole conversion by itself. This is the strongest single piece of evidence that the two routes are alternatives rather than complements.
- **Conditional (branch-dependent):** ε-cyclization is present only in lineages that make α-carotene/lutein (plants, green algae, some others). It is absent from the many bacteria and fungi that make only β-ring carotenoids.
- **Accessory / regulatory:** The **ORANGE (OR) chaperone**, which stabilizes PSY post-transcriptionally, and **PTOX**, which re-oxidizes the plastoquinone pool for the plant desaturases, are not catalytic backbone enzymes but are functionally required for normal flux in their respective systems.

### 3.3 Why the *cis* geometry matters

A crucial mechanistic subtlety is that **PSY produces 15-*cis*-phytoene, not the all-*trans* isomer**, and the plant desaturation route deliberately traffics in poly-*cis* intermediates that must be isomerized back to all-*trans*. The *cis* configuration is not incidental: Z-ISO and CRTISO exist precisely to correct geometries that the desaturases cannot. In Route A, CrtI can itself act as a *cis→trans* isomerase (anaerobically) and thus builds the isomerization function into the same polypeptide ([PMID: 22745782](https://pubmed.ncbi.nlm.nih.gov/22745782/)).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 Phytoene synthase (PSY / CrtB): the committed gate

PSY condenses two GGPP molecules into 15-*cis*-phytoene, and this is universally described as the **first committed and rate-limiting step** of carotenogenesis ([PMID: 35498681](https://pubmed.ncbi.nlm.nih.gov/35498681/)). Because it is rate-limiting, PSY output governs total carotenoid flux, and the enzyme is heavily regulated. A central mode of control is **post-transcriptional**: PSY levels and activity are fine-tuned without changing its localization to the plastid stroma and protothylakoid membranes, including through binding within a **PSY:ORANGE multi-enzyme complex** ([PMID: 37948577](https://pubmed.ncbi.nlm.nih.gov/37948577/)). The OR protein acts as a holdase chaperone that stabilizes PSY and promotes chromoplast biogenesis ([PMID: 42165846](https://pubmed.ncbi.nlm.nih.gov/42165846/)). In addition, PSY activity depends on productive interaction with GGPPS; in peach, differences in PSY1/PSY2 activity track the strength of the PSY–GGPPS interaction, and single interface residues can shift activity ([PMID: 40826491](https://pubmed.ncbi.nlm.nih.gov/40826491/)). PSY is thus best understood not as a soluble solo enzyme but as a membrane-associated node embedded in protein–protein interaction networks.

### 4.2 The two desaturation routes

**Route A — CrtI (single enzyme).** The apo-CrtI crystal structure from *Pantoea ananatis* places CrtI in the **flavoprotein superfamily** together with protoporphyrinogen IX oxidoreductase and monoamine oxidase. It is a **membrane-peripheral oxidoreductase that uses FAD as its sole redox-active cofactor**, with O2 (replaceable by quinones) as the terminal electron acceptor, and can act as a *cis-trans* isomerase under anaerobic conditions ([PMID: 22745782](https://pubmed.ncbi.nlm.nih.gov/22745782/)). One enzyme therefore accomplishes both the four dehydrogenations and the geometric correction. An instructive variation: in *Myxococcus xanthus* two distinct CrtI-type desaturases cooperate — one acting on *cis*, one on *trans* substrates — to complete the four steps ([PMID: 17662111](https://pubmed.ncbi.nlm.nih.gov/17662111/)), showing that even "the single-enzyme route" is not monolithic.

**Route B — the four-enzyme poly-*cis* system.** In cyanobacteria, algae, and plants, the conversion is partitioned:

| Enzyme | Reaction | Notable mechanism |
|--------|----------|-------------------|
| **PDS / CrtP** | 15-*cis*-phytoene → 9,15,9′-tri-*cis*-ζ-carotene (+2 bonds) | Plastoquinone-dependent desaturase |
| **Z-ISO** | 9,15,9′-tri-*cis*- → 9,9′-di-*cis*-ζ-carotene | **Heme b–dependent** isomerase of the 15-15′ bond |
| **ZDS / CrtQ** | 9,9′-di-*cis*-ζ-carotene → 7,9,7′,9′-tetra-*cis*-lycopene (+2 bonds) | Plastoquinone-dependent desaturase |
| **CRTISO / CrtH** | prolycopene (tetra-*cis*) → all-*trans*-lycopene | Redox-type isomerase, structurally related to CrtI |

Z-ISO is a *bona fide* integral-membrane enzyme that independently isomerizes the 15-15′ *cis* double bond, and — remarkably for a carotenoid enzyme — catalysis depends on a **ferrous heme b cofactor with redox-regulated ligand switching** ([PMID: 26075523](https://pubmed.ncbi.nlm.nih.gov/26075523/)). CRTISO, cloned as the tomato *tangerine* locus, is a redox-type enzyme structurally related to bacterial CrtI and is required to convert prolycopene to all-*trans*-lycopene; *tangerine* mutants accumulate prolycopene instead of lycopene ([PMID: 11884678](https://pubmed.ncbi.nlm.nih.gov/11884678/)). Z-ISO is specifically required by oxygenic phototrophs and is absent from anoxygenic species such as green sulfur bacteria, which use CrtP/CrtQ/CrtH but not Z-ISO ([PMID: 31593237](https://pubmed.ncbi.nlm.nih.gov/31593237/), [PMID: 36144332](https://pubmed.ncbi.nlm.nih.gov/36144332/)).

### 4.3 Lycopene cyclases: four unrelated solutions

Cyclization is the most striking case of **convergent enzymology** in the pathway. Four families of carotenoid cyclase are known, and *each family includes both mono- and dicyclases* that catalyze formation of γ- and β-carotene respectively ([PMID: 18676669](https://pubmed.ncbi.nlm.nih.gov/18676669/)):

1. **CrtY** — bacterial (e.g., *Pantoea*) lycopene β-cyclase.
2. **CrtL-type** — including plant **LCYB** (β-cyclase) and **LCYE** (ε-cyclase). LCYB is the major β-cyclase in Arabidopsis ([PMID: 19549928](https://pubmed.ncbi.nlm.nih.gov/19549928/)).
3. **Fungal bifunctional CrtYB / al-2** — a single polypeptide with both phytoene synthase and lycopene cyclase domains; mutations in the cyclase domain of *Neurospora* al-2 abolish cyclization and accumulate an acyclic carotenoid ([PMID: 11862485](https://pubmed.ncbi.nlm.nih.gov/11862485/)).
4. **CruA / CruP** — members of the **FixC dehydrogenase superfamily**, only distantly related to CrtL/CrtY, that fill the cyclization gap in green sulfur bacteria and cyanobacteria ([PMID: 17606904](https://pubmed.ncbi.nlm.nih.gov/17606904/)).

The **β/ε distinction** determines the downstream carotenoid class. A β-ring plus a β-ring gives β-carotene (β,β) and the β,β-xanthophylls (zeaxanthin, violaxanthin). One ε-ring plus one β-ring gives α-carotene (β,ε) and lutein. The **order is fixed in the α-branch**: LCYE forms one ε-ring first (giving δ-carotene), and LCYB then completes the molecule with a β-ring (giving α-carotene). Plant LCYE typically forms only a single ε-ring; interestingly, the liverwort *Marchantia polymorpha* LCYE can form two ε-rings (δ- → ε-carotene), unlike Arabidopsis LCYE ([PMID: 24285752](https://pubmed.ncbi.nlm.nih.gov/24285752/)), showing lineage-specific variation in cyclase specificity.

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep origin and inheritance

Phylogenetic analysis of carotenoid pathway genes indicates **early evolutionary roots in prokaryotes** ([PMID: 34324713](https://pubmed.ncbi.nlm.nih.gov/34324713/)). With the rise of oxygenic photosynthesis in cyanobacteria and the subsequent endosymbiotic origin of plastids, the **cyanobacterial carotenoid pathway was inherited into algal and plant plastids** ([PMID: 34324713](https://pubmed.ncbi.nlm.nih.gov/34324713/)). This explains why plant desaturation is cyanobacterial in type (PDS/ZDS/Z-ISO/CRTISO, plastoquinone-coupled) rather than fungal/bacterial (CrtI, FAD-coupled): the plant machinery is literally cyanobacterial machinery relocated to the plastid.

### 5.2 The route dichotomy as a lineage marker

| Feature | Route A (CrtI) | Route B (poly-*cis*) |
|---------|---------------|----------------------|
| Distribution | Most bacteria, fungi | Cyanobacteria, algae, plants |
| # enzymes | 1 | 4 (PDS, Z-ISO, ZDS, CRTISO) |
| Cofactor | FAD | Plastoquinone (desaturases); heme b (Z-ISO) |
| Electron sink | O2 / quinones | Plastoquinone → PTOX |
| Intermediates | mostly all-*trans* | poly-*cis* |
| Isomerase | built into CrtI | separate (Z-ISO, CRTISO) |

The comparative enzymology across taxa is explicit: CrtP, CrtQ and isomerase CrtH form lycopene in most cyanobacteria, PDS/ZDS/Z-ISO/CrtISO in most algae and plants, while a single CrtI type is used in most bacteria and fungi ([PMID: 29741830](https://pubmed.ncbi.nlm.nih.gov/29741830/)). Green sulfur bacteria are an informative intermediate: they are anoxygenic yet use the plant-like CrtP/CrtQ/CrtH set (but not Z-ISO), converting phytoene to lycopene via two plant-like desaturases and a plant-like isomerase — a pathway that "differs from the pathway known in all other bacteria" ([PMID: 15292122](https://pubmed.ncbi.nlm.nih.gov/15292122/)).

### 5.3 Tissue, developmental, and compartmental variation

Within a plant, the same core enzymes operate in different plastid types and developmental contexts. PSY frequently exists as **tissue-specific isoforms** (e.g., PSY1/PSY2 in peach) with divergent activity driven by differential GGPPS interaction ([PMID: 40826491](https://pubmed.ncbi.nlm.nih.gov/40826491/)). Cyclization branch usage is developmentally and tissue-tuned (leaf chloroplasts favor a lutein/β,β balance; ripening fruit chromoplasts often accumulate lycopene or β-carotene). A key light/dark difference: because the plant route generates *cis* intermediates that can also isomerize photochemically, CRTISO is especially important for carotenoid synthesis **in the dark and in non-photosynthetic tissue**, where light-driven isomerization is unavailable ([PMID: 11884678](https://pubmed.ncbi.nlm.nih.gov/11884678/)). Consistently, Z-ISO is required for **light-independent** carotenoid biosynthesis in cyanobacteria ([PMID: 36144332](https://pubmed.ncbi.nlm.nih.gov/36144332/)).

### 5.4 The signaling dimension

A distinctive feature of Route B is that its **linear *cis*-carotene intermediates are themselves a source of a plastid-signaling apocarotenoid**. In Arabidopsis, disruption of **CRTISO** (but not Z-ISO) reduces chlorophyll in young leaves; the *ccr2* (CRTISO) phenotype is rescued by lowering PSY activity, implicating a specific acyclic *cis*-carotene-derived signal that modulates the **PIF3/HY5 module and plastid biogenesis** ([PMID: 35177117](https://pubmed.ncbi.nlm.nih.gov/35177117/), [PMID: 37948577](https://pubmed.ncbi.nlm.nih.gov/37948577/)). This distinguishes CRTISO from Z-ISO mechanistically at the *organismal* level, not just the enzymatic one, and gives Route B a regulatory output that Route A (which never accumulates these intermediates) cannot produce ([PMID: 33258195](https://pubmed.ncbi.nlm.nih.gov/33258195/)).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering constraints

- **Condensation before desaturation before cyclization.** Phytoene is the obligatory first C40; lycopene is the obligatory cyclase substrate. Cyclases act on the acyclic all-*trans*-lycopene (or on partially desaturated substrates in some bacteria), never on phytoene.
- **Within Route B, the order is strictly PDS → Z-ISO → ZDS → CRTISO.** Each enzyme's product is the next enzyme's substrate: PDS supplies tri-*cis*-ζ-carotene to Z-ISO; Z-ISO supplies di-*cis*-ζ-carotene to ZDS; ZDS supplies prolycopene to CRTISO. Skipping Z-ISO leaves the 15-15′ *cis* bond uncorrected, and the route stalls in the dark.
- **In the α-branch, LCYE acts before LCYB.** The ε-ring is formed first (δ-carotene), then a β-ring is added (α-carotene). Two β-rings give β-carotene; the branch is decided by whether LCYE gets access to lycopene.

### 6.2 Compartment- and cofactor-specific dependencies

The plant desaturases are **redox-coupled to the photosynthetic electron-transport chain**. PDS and ZDS pass electrons to **plastoquinone**, which must be re-oxidized by the **plastid terminal oxidase (PTOX)**. The tomato *ghost* (*gh*) PTOX-null mutant is carotenoid-deficient with bleached fruit, consistent with PTOX acting as a phytoene-desaturase cofactor ([PMID: 17873087](https://pubmed.ncbi.nlm.nih.gov/17873087/)). This coupling has a striking consequence for metabolic engineering: when bacterial CrtI is expressed in Arabidopsis, it too dumps electrons into the plastoquinone pool via PTOX, and **PTOX competes efficiently with cyclic electron flow for plastoquinol**, raising reactive oxygen species and causing photoinhibition ([PMID: 24378845](https://pubmed.ncbi.nlm.nih.gov/24378845/)). Thus even a "foreign" desaturase is forced into the host's redox constraints.

### 6.3 Mutual exclusivity and interchangeability — the central paradox resolved

The two routes are **mutually exclusive within a lineage** (organisms use one or the other) yet **functionally interchangeable across lineages**. The decisive experiment is Golden Rice: co-expressing plant PSY with bacterial **CrtI alone** was sufficient to drive β-carotene synthesis *and* downstream xanthophylls in rice endosperm, without any of the plant PDS/Z-ISO/ZDS/CRTISO enzymes ([PMID: 11880581](https://pubmed.ncbi.nlm.nih.gov/11880581/)). The same two-gene (CrtB + CrtI) strategy enriches provitamin A in wheat ([PMID: 24692648](https://pubmed.ncbi.nlm.nih.gov/24692648/)). This rules out the otherwise plausible idea that the plant four-enzyme system is *chemically necessary* in a plastid; it is a lineage-inherited implementation, not a requirement.

### 6.4 Failure modes

- **Loss of PSY** → no carotenoids at all (complete block at commitment).
- **Loss of any Route B enzyme** → accumulation of the corresponding *cis* intermediate (e.g., prolycopene in CRTISO-null *tangerine*; ζ-carotene isomers in Z-ISO-null), photobleaching, and — in CRTISO loss — aberrant *cis*-carotene signaling that lowers chlorophyll.
- **Loss of PTOX** → desaturation stalls for lack of an electron sink; bleached, carotenoid-deficient tissue (tomato *ghost*).
- **Misregulated flux** (e.g., unstable PSY without OR) → reduced carotenoid storage and chromoplast defects.

---

## 7. Mechanistic Model — Integrated Narrative

The carotene backbone is best understood as **one conserved chemical logic implemented by two enzymatic dialects**. The logic is invariant: commit isoprenoid flux (PSY), extend the conjugated polyene to lycopene by four desaturations with geometric correction, then close rings. The dialects differ in how the desaturation problem is solved. The **CrtI dialect** is compact and self-contained — a single FAD flavoprotein that dehydrogenates and isomerizes, dumping electrons onto O2/quinones. The **poly-*cis* dialect** is distributed — two plastoquinone-coupled desaturases wired into photosynthetic redox via PTOX, plus a heme-b isomerase (Z-ISO) and a CrtI-related isomerase (CRTISO) that repair the *cis* geometries the desaturases generate.

The two dialects are not chemically superior to one another — Golden Rice proves substitutability — but they carry different *side effects*. The poly-*cis* dialect couples carotenoid synthesis to the plastoquinone pool and generates *cis*-carotene intermediates that double as retrograde signals. These side effects, not the core chemistry, are probably what natural selection acts on when a lineage "keeps" a route. Cyclization then layers a second, independent case of convergence: four unrelated protein families all learned to fold lycopene's ends into β- or ε-rings, with the β/ε choice and its order defining the entire downstream carotenoid landscape.

---

## 8. Evidence Base — Key Literature

| PMID | How it supports the review |
|------|---------------------------|
| [29741830](https://pubmed.ncbi.nlm.nih.gov/29741830/) | Contrasts the single CrtI route with the four-enzyme poly-*cis* route across taxa (route dichotomy) |
| [26075523](https://pubmed.ncbi.nlm.nih.gov/26075523/) | Z-ISO substrate/regiochemistry and heme b cofactor dependence |
| [22745782](https://pubmed.ncbi.nlm.nih.gov/22745782/) | CrtI crystal structure: flavoprotein superfamily, FAD, membrane-peripheral, isomerase activity |
| [17606904](https://pubmed.ncbi.nlm.nih.gov/17606904/) | CruA/CruP as a fourth, FixC-superfamily cyclase family |
| [18676669](https://pubmed.ncbi.nlm.nih.gov/18676669/) | Four cyclase families; mono-/di-cyclase = γ/β distinction |
| [35498681](https://pubmed.ncbi.nlm.nih.gov/35498681/) | PSY as first committed, rate-limiting step |
| [37948577](https://pubmed.ncbi.nlm.nih.gov/37948577/) | Post-transcriptional PSY control and PSY:ORANGE complex; *cis*-carotene signal to PIF3/HY5 |
| [42165846](https://pubmed.ncbi.nlm.nih.gov/42165846/) | ORANGE holdase chaperone stabilizes PSY, promotes chromoplasts |
| [40826491](https://pubmed.ncbi.nlm.nih.gov/40826491/) | PSY–GGPPS interaction strength drives isoform activity |
| [34324713](https://pubmed.ncbi.nlm.nih.gov/34324713/) | Prokaryotic roots; endosymbiotic inheritance into plastids |
| [17873087](https://pubmed.ncbi.nlm.nih.gov/17873087/) | PTOX as phytoene-desaturase cofactor (tomato *ghost*) |
| [24378845](https://pubmed.ncbi.nlm.nih.gov/24378845/) | CrtI feeds electrons into plastoquinone pool via PTOX; ROS/photoinhibition |
| [11880581](https://pubmed.ncbi.nlm.nih.gov/11880581/) | CrtI substitutes for whole plant desaturation/isomerization machinery (Golden Rice) |
| [24692648](https://pubmed.ncbi.nlm.nih.gov/24692648/) | CrtB + CrtI two-gene strategy enriches provitamin A in wheat |
| [35177117](https://pubmed.ncbi.nlm.nih.gov/35177117/) | CRTISO (not Z-ISO) loss lowers chlorophyll; *cis*-carotene retrograde signaling |
| [11884678](https://pubmed.ncbi.nlm.nih.gov/11884678/) | CRTISO cloned as tomato *tangerine*; prolycopene accumulation; dark/non-photosynthetic role |
| [31593237](https://pubmed.ncbi.nlm.nih.gov/31593237/) | Z-ISO required by oxygenic phototrophs, absent in anoxygenic species |
| [36144332](https://pubmed.ncbi.nlm.nih.gov/36144332/) | Z-ISO required for light-independent carotenoid synthesis in cyanobacteria |
| [15292122](https://pubmed.ncbi.nlm.nih.gov/15292122/) | Green sulfur bacteria use plant-like CrtP/CrtQ/CrtH (but not Z-ISO) |
| [11862485](https://pubmed.ncbi.nlm.nih.gov/11862485/) | Fungal bifunctional PSY/cyclase (al-2); cyclase-domain mutants |
| [17662111](https://pubmed.ncbi.nlm.nih.gov/17662111/) | Two cooperating CrtI-type desaturases in *Myxococcus* |
| [24285752](https://pubmed.ncbi.nlm.nih.gov/24285752/) | Liverwort LCYE forms two ε-rings (lineage-specific cyclase variation) |
| [19549928](https://pubmed.ncbi.nlm.nih.gov/19549928/) | LCYB as major β-cyclase in Arabidopsis |
| [18788479](https://pubmed.ncbi.nlm.nih.gov/18788479/) | Cyanobacterium cyclizes lycopene without a classical cyclase gene |

---

## 9. Controversies and Open Questions

1. **Where exactly is the module boundary at the commitment step?** Because PSY activity is governed by GGPPS interaction and by the OR chaperone, the "first committed step" is really a regulated multi-protein node. How much of carotenoid flux control lies in PSY catalysis versus PSY stabilization/complex assembly remains quantitatively unresolved ([PMID: 37948577](https://pubmed.ncbi.nlm.nih.gov/37948577/), [PMID: 40826491](https://pubmed.ncbi.nlm.nih.gov/40826491/)).

2. **The identity and generality of the *cis*-carotene signal.** The acyclic *cis*-carotene-derived apocarotenoid that regulates the PIF3/HY5 module is functionally inferred but not chemically identified in most reports; whether a single molecule or a family of signals is responsible, and how broadly it operates beyond Arabidopsis, is open ([PMID: 35177117](https://pubmed.ncbi.nlm.nih.gov/35177117/), [PMID: 33258195](https://pubmed.ncbi.nlm.nih.gov/33258195/)).

3. **Cyclase family boundaries and convergence.** With four unrelated cyclase families (including CruA/CruP in the FixC dehydrogenase superfamily), the ancestral cyclase and the number of independent inventions of ring formation are debated ([PMID: 17606904](https://pubmed.ncbi.nlm.nih.gov/17606904/), [PMID: 18676669](https://pubmed.ncbi.nlm.nih.gov/18676669/)). Some cyanobacterial genomes lack any classical cyclase gene yet still cyclize, indicating additional undiscovered players ([PMID: 18788479](https://pubmed.ncbi.nlm.nih.gov/18788479/)).

4. **Mixing organisms.** Much mechanistic detail comes from a few models (Arabidopsis, tomato, maize, *Pantoea*, *Synechocystis*, *Neurospora*). Z-ISO has been functionally characterized in only a handful of species ([PMID: 31593237](https://pubmed.ncbi.nlm.nih.gov/31593237/)), and inferring universal mechanism from these is a real risk. The presence of plant-like desaturases in *anoxygenic* green sulfur bacteria — but without Z-ISO — warns against equating "plant-type route" with "oxygenic" in every detail ([PMID: 15292122](https://pubmed.ncbi.nlm.nih.gov/15292122/), [PMID: 31593237](https://pubmed.ncbi.nlm.nih.gov/31593237/)).

5. **Why keep the complicated route at all?** If CrtI can do the whole job, why did the cyanobacterial/plant lineage retain a four-enzyme, poly-*cis*, PTOX-dependent system? The signaling output of *cis* intermediates and integration with photosynthetic redox poise are candidate answers, but a rigorous adaptive explanation is not settled.

---

## 10. Limitations and Knowledge Gaps

- **Organismal narrowness.** The mechanistic backbone is assembled from a small set of model systems; several enzymes (notably Z-ISO) are characterized in only a few species, and cross-organism generalization should be made cautiously.
- **This review is a literature synthesis, not a data analysis.** No new experimental or sequence data were generated; conclusions rest on published primary literature and reviews.
- **Chemical identity of the *cis*-carotene signal** is unresolved, as is the quantitative apportioning of flux control between PSY catalysis and PSY stabilization.
- **Cyclase completeness.** At least one cyanobacterium cyclizes lycopene without a recognizable classical cyclase, implying undiscovered enzymes ([PMID: 18788479](https://pubmed.ncbi.nlm.nih.gov/18788479/)).
- **Structural data are uneven.** High-resolution structures exist for CrtI but are sparse for the plant desaturases and most cyclases, limiting mechanistic modeling.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Chemically identify the acyclic *cis*-carotene retrograde signal** using targeted metabolomics in *ccr2*/CRTISO and Z-ISO backgrounds, and test candidate apocarotenoids for PIF3/HY5 modulation.
2. **Structural determination of PDS, ZDS, Z-ISO, and CRTISO** (cryo-EM of membrane-embedded forms) to explain plastoquinone binding and Z-ISO's heme-b redox switching.
3. **Systematic route-swap panel** — express CrtI vs. the full poly-*cis* set in a common plastid host and quantify redox load, ROS, and photoinhibition to test whether the poly-*cis* route's persistence reflects redox integration rather than chemistry ([PMID: 24378845](https://pubmed.ncbi.nlm.nih.gov/24378845/)).
4. **Search cyanobacterial genomes lacking classical cyclases** for the missing cyclase activity implied by [PMID: 18788479](https://pubmed.ncbi.nlm.nih.gov/18788479/).
5. **Quantitative flux-control analysis at the commitment node**, dissecting PSY catalysis, PSY–GGPPS interaction, and OR-mediated stabilization contributions to total carotenoid flux.
6. **Broaden Z-ISO characterization** across additional oxygenic and anoxygenic lineages to firm up the "oxygenic phototrophs need Z-ISO" generalization.

---

*Prepared as a commissioned review synthesis. Claims are anchored to the cited primary literature; uncertainty is flagged where mechanistic detail derives from a single organism or indirect evidence.*


## Artifacts

- [OpenScientist final report](carotene_backbone_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](carotene_backbone_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:40826491
2. PMID:21450689
3. PMID:22513258
4. PMID:33258195
5. PMID:23896007
6. PMID:11862485
7. PMID:22745782
8. PMID:35498681
9. PMID:37948577
10. PMID:42165846
11. PMID:17662111
12. PMID:26075523
13. PMID:11884678
14. PMID:31593237
15. PMID:36144332
16. PMID:18676669
17. PMID:19549928
18. PMID:17606904
19. PMID:24285752
20. PMID:34324713
21. PMID:29741830
22. PMID:15292122
23. PMID:35177117
24. PMID:17873087
25. PMID:24378845
26. PMID:11880581
27. PMID:24692648
28. PMID:18788479