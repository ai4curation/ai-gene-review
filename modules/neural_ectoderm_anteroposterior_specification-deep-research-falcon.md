---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-20T16:42:30.996115'
end_time: '2026-09-20T16:56:17.449661'
duration_seconds: 826.45
template_file: templates/module_research.md.j2
template_variables:
  module_title: Neural ectoderm anteroposterior specification module
  module_summary: 'The developmental program that, during gastrulation, subdivides
    newly induced neural ectoderm along the anteroposterior axis into two parallel,
    lineage-committed brain progenitors: an OTX2-positive anterior neural ectoderm
    that generates the forebrain and midbrain, and a GBX2/HOX-positive posterior neural
    ectoderm that generates the hindbrain. The module begins where germ-layer specification
    ends - with SOX2-positive neural ectoderm established under combined BMP, TGF-beta
    and WNT inhibition - and is driven by a graded posteriorising input of FGF together
    with retinoic acid. That input is read out by a pair of mutually repressive homeodomain
    selectors, OTX2 and GBX2, whose shared border is the site at which the midbrain-hindbrain
    (isthmic) organizer forms; displacing the border displaces the organizer. The
    two territories are already committed rather than merely differently positioned:
    challenged with the opposite region''s inducing signals they do not interconvert,
    and they carry diverging accessible-chromatin landscapes that foreshadow their
    regional identities. Downstream, the anterior territory resolves into FOXG1/SIX3
    forebrain and EN1 midbrain progenitors, and the posterior territory into MAFB/HNF1B/HOXA3
    rhombomere 5/6 hindbrain progenitors. Grounded in GO:0021999 (neural plate anterior/posterior
    regionalization). Upstream neural-versus-epidermal ectoderm allocation is supplied
    by modules/germ_layer_specification.yaml and modules/body_axis_specification.yaml;
    the signalling machinery is detailed in the fgfr_signaling, retinoic_acid_receptor_signaling,
    wnt_signaling, bmp_signaling and tgfb_smad_signaling modules; the cerebellar program
    that continues from the posterior territory''s rhombomere 1 is in modules/cerebellum_development.yaml.'
  module_outline: "- Anteroposterior specification of neural ectoderm\n  - SOX2 neural\
    \ ectoderm identity factor (molecular player: SOX2; activity or role: DNA-binding\
    \ transcription factor activity)\n  - 1. extracellular input that biases identity\
    \ posteriorly\n  - Graded FGF and retinoic acid posteriorising input\n    - Posteriorising\
    \ FGF ligand (molecular player: FGF8; activity or role: growth factor activity)\n\
    \    - Retinoic acid synthesising enzyme (molecular player: ALDH1A2; activity\
    \ or role: retinal dehydrogenase (NAD+) activity)\n  - 2. the mutually repressive\
    \ selector pair that partitions the territory\n  - Mutually repressive OTX2/GBX2\
    \ selector boundary\n    - Alternative versions by anteroposterior neural ectoderm\
    \ identity: Parallel anterior and posterior neural ectoderm progenitors\n    \
    \  - Anterior neural ectoderm (forebrain/midbrain progenitor)\n        - OTX2\
    \ anterior identity selector (molecular player: OTX2; activity or role: DNA-binding\
    \ transcription factor activity)\n      - Posterior neural ectoderm (hindbrain\
    \ progenitor)\n        - GBX2 posterior identity selector (molecular player: GBX2;\
    \ activity or role: DNA-binding transcription factor activity)\n        - Anterior\
    \ HOX posterior-character factor (molecular player: HOXA1; activity or role: DNA-binding\
    \ transcription factor activity)\n  - 3. regional progenitors each territory is\
    \ committed to produce\n  - Committed regional progenitor output\n    - Alternative\
    \ versions by brain region produced: Regional progenitors produced by each neural\
    \ ectoderm territory\n      - Forebrain and midbrain progenitors (from anterior\
    \ neural ectoderm)\n        - FOXG1 telencephalic progenitor factor (molecular\
    \ player: FOXG1; activity or role: DNA-binding transcription factor activity)\n\
    \        - SIX3 rostral forebrain factor (molecular player: SIX3; activity or\
    \ role: DNA-binding transcription factor activity)\n        - EN1 midbrain identity\
    \ factor (molecular player: EN1; activity or role: DNA-binding transcription factor\
    \ activity)\n      - Rhombomere 5/6 hindbrain progenitors (from posterior neural\
    \ ectoderm)\n        - MAFB rhombomere 5/6 factor (molecular player: MAFB; activity\
    \ or role: DNA-binding transcription factor activity)\n        - HNF1B rhombomere\
    \ 5/6 factor (molecular player: HNF1B; activity or role: DNA-binding transcription\
    \ factor activity)\n        - HOXA3 caudal hindbrain positional factor (molecular\
    \ player: HOXA3; activity or role: DNA-binding transcription factor activity)"
  module_connections: '- Graded FGF and retinoic acid posteriorising input feeds into
    Mutually repressive OTX2/GBX2 selector boundary: Combined FGF and retinoic acid
    activity is the extracellular input that selects the posterior branch of the selector
    variant set; in its absence, and under BMP, TGF-beta and WNT inhibition, neural
    ectoderm adopts the anterior branch by default.

    - Mutually repressive OTX2/GBX2 selector boundary precedes Committed regional
    progenitor output: Selector identity is established first and constrains what
    regional progenitors can subsequently be induced; the chromatin landscapes of
    the two territories diverge before overt regional identity appears, which is the
    proposed mechanism of the commitment.

    - SOX2 neural ectoderm identity factor part of Mutually repressive OTX2/GBX2 selector
    boundary: The selector boundary is drawn within the SOX2-positive neural ectoderm
    population, not between it and another germ layer derivative.

    - OTX2 anterior identity selector inhibits GBX2 posterior identity selector: The
    anterior selector excludes the posterior selector from its territory; the two
    expression domains are mutually exclusive within SOX2-positive neural ectoderm.

    - GBX2 posterior identity selector inhibits OTX2 anterior identity selector: The
    posterior selector represses the anterior one and thereby positions and sharpens
    the shared border. This is the directional arm with gain- and loss-of-function
    support: without it the anterior domain expands posteriorly, and forcing it inside
    the anterior domain relocates the border and the organizer.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 60
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: neural_ectoderm_anteroposterior_specification-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Commissioned Review Brief

## Review Topic

Neural ectoderm anteroposterior specification module

## Working Scope

The developmental program that, during gastrulation, subdivides newly induced neural ectoderm along the anteroposterior axis into two parallel, lineage-committed brain progenitors: an OTX2-positive anterior neural ectoderm that generates the forebrain and midbrain, and a GBX2/HOX-positive posterior neural ectoderm that generates the hindbrain. The module begins where germ-layer specification ends - with SOX2-positive neural ectoderm established under combined BMP, TGF-beta and WNT inhibition - and is driven by a graded posteriorising input of FGF together with retinoic acid. That input is read out by a pair of mutually repressive homeodomain selectors, OTX2 and GBX2, whose shared border is the site at which the midbrain-hindbrain (isthmic) organizer forms; displacing the border displaces the organizer. The two territories are already committed rather than merely differently positioned: challenged with the opposite region's inducing signals they do not interconvert, and they carry diverging accessible-chromatin landscapes that foreshadow their regional identities. Downstream, the anterior territory resolves into FOXG1/SIX3 forebrain and EN1 midbrain progenitors, and the posterior territory into MAFB/HNF1B/HOXA3 rhombomere 5/6 hindbrain progenitors. Grounded in GO:0021999 (neural plate anterior/posterior regionalization). Upstream neural-versus-epidermal ectoderm allocation is supplied by modules/germ_layer_specification.yaml and modules/body_axis_specification.yaml; the signalling machinery is detailed in the fgfr_signaling, retinoic_acid_receptor_signaling, wnt_signaling, bmp_signaling and tgfb_smad_signaling modules; the cerebellar program that continues from the posterior territory's rhombomere 1 is in modules/cerebellum_development.yaml.

## Provisional Biological Outline

- Anteroposterior specification of neural ectoderm
  - SOX2 neural ectoderm identity factor (molecular player: SOX2; activity or role: DNA-binding transcription factor activity)
  - 1. extracellular input that biases identity posteriorly
  - Graded FGF and retinoic acid posteriorising input
    - Posteriorising FGF ligand (molecular player: FGF8; activity or role: growth factor activity)
    - Retinoic acid synthesising enzyme (molecular player: ALDH1A2; activity or role: retinal dehydrogenase (NAD+) activity)
  - 2. the mutually repressive selector pair that partitions the territory
  - Mutually repressive OTX2/GBX2 selector boundary
    - Alternative versions by anteroposterior neural ectoderm identity: Parallel anterior and posterior neural ectoderm progenitors
      - Anterior neural ectoderm (forebrain/midbrain progenitor)
        - OTX2 anterior identity selector (molecular player: OTX2; activity or role: DNA-binding transcription factor activity)
      - Posterior neural ectoderm (hindbrain progenitor)
        - GBX2 posterior identity selector (molecular player: GBX2; activity or role: DNA-binding transcription factor activity)
        - Anterior HOX posterior-character factor (molecular player: HOXA1; activity or role: DNA-binding transcription factor activity)
  - 3. regional progenitors each territory is committed to produce
  - Committed regional progenitor output
    - Alternative versions by brain region produced: Regional progenitors produced by each neural ectoderm territory
      - Forebrain and midbrain progenitors (from anterior neural ectoderm)
        - FOXG1 telencephalic progenitor factor (molecular player: FOXG1; activity or role: DNA-binding transcription factor activity)
        - SIX3 rostral forebrain factor (molecular player: SIX3; activity or role: DNA-binding transcription factor activity)
        - EN1 midbrain identity factor (molecular player: EN1; activity or role: DNA-binding transcription factor activity)
      - Rhombomere 5/6 hindbrain progenitors (from posterior neural ectoderm)
        - MAFB rhombomere 5/6 factor (molecular player: MAFB; activity or role: DNA-binding transcription factor activity)
        - HNF1B rhombomere 5/6 factor (molecular player: HNF1B; activity or role: DNA-binding transcription factor activity)
        - HOXA3 caudal hindbrain positional factor (molecular player: HOXA3; activity or role: DNA-binding transcription factor activity)

## Known Relationships Among Steps

- Graded FGF and retinoic acid posteriorising input feeds into Mutually repressive OTX2/GBX2 selector boundary: Combined FGF and retinoic acid activity is the extracellular input that selects the posterior branch of the selector variant set; in its absence, and under BMP, TGF-beta and WNT inhibition, neural ectoderm adopts the anterior branch by default.
- Mutually repressive OTX2/GBX2 selector boundary precedes Committed regional progenitor output: Selector identity is established first and constrains what regional progenitors can subsequently be induced; the chromatin landscapes of the two territories diverge before overt regional identity appears, which is the proposed mechanism of the commitment.
- SOX2 neural ectoderm identity factor part of Mutually repressive OTX2/GBX2 selector boundary: The selector boundary is drawn within the SOX2-positive neural ectoderm population, not between it and another germ layer derivative.
- OTX2 anterior identity selector inhibits GBX2 posterior identity selector: The anterior selector excludes the posterior selector from its territory; the two expression domains are mutually exclusive within SOX2-positive neural ectoderm.
- GBX2 posterior identity selector inhibits OTX2 anterior identity selector: The posterior selector represses the anterior one and thereby positions and sharpens the shared border. This is the directional arm with gain- and loss-of-function support: without it the anterior domain expands posteriorly, and forcing it inside the anterior domain relocates the border and the organizer.

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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Commissioned Review Brief

## Review Topic

Neural ectoderm anteroposterior specification module

## Working Scope

The developmental program that, during gastrulation, subdivides newly induced neural ectoderm along the anteroposterior axis into two parallel, lineage-committed brain progenitors: an OTX2-positive anterior neural ectoderm that generates the forebrain and midbrain, and a GBX2/HOX-positive posterior neural ectoderm that generates the hindbrain. The module begins where germ-layer specification ends - with SOX2-positive neural ectoderm established under combined BMP, TGF-beta and WNT inhibition - and is driven by a graded posteriorising input of FGF together with retinoic acid. That input is read out by a pair of mutually repressive homeodomain selectors, OTX2 and GBX2, whose shared border is the site at which the midbrain-hindbrain (isthmic) organizer forms; displacing the border displaces the organizer. The two territories are already committed rather than merely differently positioned: challenged with the opposite region's inducing signals they do not interconvert, and they carry diverging accessible-chromatin landscapes that foreshadow their regional identities. Downstream, the anterior territory resolves into FOXG1/SIX3 forebrain and EN1 midbrain progenitors, and the posterior territory into MAFB/HNF1B/HOXA3 rhombomere 5/6 hindbrain progenitors. Grounded in GO:0021999 (neural plate anterior/posterior regionalization). Upstream neural-versus-epidermal ectoderm allocation is supplied by modules/germ_layer_specification.yaml and modules/body_axis_specification.yaml; the signalling machinery is detailed in the fgfr_signaling, retinoic_acid_receptor_signaling, wnt_signaling, bmp_signaling and tgfb_smad_signaling modules; the cerebellar program that continues from the posterior territory's rhombomere 1 is in modules/cerebellum_development.yaml.

## Provisional Biological Outline

- Anteroposterior specification of neural ectoderm
  - SOX2 neural ectoderm identity factor (molecular player: SOX2; activity or role: DNA-binding transcription factor activity)
  - 1. extracellular input that biases identity posteriorly
  - Graded FGF and retinoic acid posteriorising input
    - Posteriorising FGF ligand (molecular player: FGF8; activity or role: growth factor activity)
    - Retinoic acid synthesising enzyme (molecular player: ALDH1A2; activity or role: retinal dehydrogenase (NAD+) activity)
  - 2. the mutually repressive selector pair that partitions the territory
  - Mutually repressive OTX2/GBX2 selector boundary
    - Alternative versions by anteroposterior neural ectoderm identity: Parallel anterior and posterior neural ectoderm progenitors
      - Anterior neural ectoderm (forebrain/midbrain progenitor)
        - OTX2 anterior identity selector (molecular player: OTX2; activity or role: DNA-binding transcription factor activity)
      - Posterior neural ectoderm (hindbrain progenitor)
        - GBX2 posterior identity selector (molecular player: GBX2; activity or role: DNA-binding transcription factor activity)
        - Anterior HOX posterior-character factor (molecular player: HOXA1; activity or role: DNA-binding transcription factor activity)
  - 3. regional progenitors each territory is committed to produce
  - Committed regional progenitor output
    - Alternative versions by brain region produced: Regional progenitors produced by each neural ectoderm territory
      - Forebrain and midbrain progenitors (from anterior neural ectoderm)
        - FOXG1 telencephalic progenitor factor (molecular player: FOXG1; activity or role: DNA-binding transcription factor activity)
        - SIX3 rostral forebrain factor (molecular player: SIX3; activity or role: DNA-binding transcription factor activity)
        - EN1 midbrain identity factor (molecular player: EN1; activity or role: DNA-binding transcription factor activity)
      - Rhombomere 5/6 hindbrain progenitors (from posterior neural ectoderm)
        - MAFB rhombomere 5/6 factor (molecular player: MAFB; activity or role: DNA-binding transcription factor activity)
        - HNF1B rhombomere 5/6 factor (molecular player: HNF1B; activity or role: DNA-binding transcription factor activity)
        - HOXA3 caudal hindbrain positional factor (molecular player: HOXA3; activity or role: DNA-binding transcription factor activity)

## Known Relationships Among Steps

- Graded FGF and retinoic acid posteriorising input feeds into Mutually repressive OTX2/GBX2 selector boundary: Combined FGF and retinoic acid activity is the extracellular input that selects the posterior branch of the selector variant set; in its absence, and under BMP, TGF-beta and WNT inhibition, neural ectoderm adopts the anterior branch by default.
- Mutually repressive OTX2/GBX2 selector boundary precedes Committed regional progenitor output: Selector identity is established first and constrains what regional progenitors can subsequently be induced; the chromatin landscapes of the two territories diverge before overt regional identity appears, which is the proposed mechanism of the commitment.
- SOX2 neural ectoderm identity factor part of Mutually repressive OTX2/GBX2 selector boundary: The selector boundary is drawn within the SOX2-positive neural ectoderm population, not between it and another germ layer derivative.
- OTX2 anterior identity selector inhibits GBX2 posterior identity selector: The anterior selector excludes the posterior selector from its territory; the two expression domains are mutually exclusive within SOX2-positive neural ectoderm.
- GBX2 posterior identity selector inhibits OTX2 anterior identity selector: The posterior selector represses the anterior one and thereby positions and sharpens the shared border. This is the directional arm with gain- and loss-of-function support: without it the anterior domain expands posteriorly, and forcing it inside the anterior domain relocates the border and the organizer.

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

# Neural ectoderm anteroposterior specification module

## 1. Executive summary

Neural ectoderm anteroposterior (AP) specification is the gastrulation-stage program that regionalizes newly induced, SOX2-positive neural ectoderm into anterior forebrain/midbrain and posterior hindbrain territories. It is downstream of neural-versus-epidermal allocation and upstream of dorsoventral patterning, rhombomere maturation, neurogenesis, and cerebellar development. The relevant Gene Ontology process is **GO:0021999, neural plate anterior/posterior regionalization**.

The best-supported vertebrate model has four phases. First, attenuation of BMP signaling establishes neural competence, usually accompanied experimentally by TGF-β and WNT inhibition. Second, posteriorly enriched FGF and retinoic acid (RA) signals oppose an anterior OTX2 program and promote GBX2 and anterior HOX expression. Third, reciprocal antagonism between OTX2 and GBX-family factors sharpens their interface. Fourth, that interface licenses the FGF8/WNT1 isthmic organizer, which patterns adjacent midbrain and rhombomere-1 tissue. Organizer formation is therefore a **consequence and stabilizer** of AP allocation, not the initial neural-induction event (sears2022controllingneuralterritory pages 5-7, martinez2001theisthmicorganizer pages 1-2, dworkin2013novelmechanismsthat pages 1-2).

A major conceptual revision was proposed in a July 2025 bioRxiv preprint: anterior and posterior neural ectoderm may arise in parallel during gastrulation and already be lineage restricted, rather than representing successive positions within a freely interconvertible pan-brain progenitor. The reported reciprocal-challenge, lineage-tracing, and chromatin-accessibility data are substantial, but the study is not yet peer reviewed and does not exclude every transient common-progenitor state or alternative reprogramming regimen (dundes2025twoparallellineagecommitted pages 3-5, dundes2025twoparallellineagecommitted pages 7-9, dundes2025twoparallellineagecommitted pages 5-7).

| Stage/module | Principal molecules | Mechanistic role | Strongest evidence and quantitative examples | Confidence/limitations |
|---|---|---|---|---|
| Neural induction prerequisite | SOX2; BMP–SMAD1/5/8, TGF-β–SMAD2/3 and WNT pathways | Establishes neural ectoderm before AP subdivision. BMP inhibition is consistently important in controlled hPSC systems; WNT suppression preserves anterior neural character and separates brain ectoderm from WNT-driven axial/NMP states. | Systems-level differentiation across four hiPSC lines identified BMP inhibition as critical for neuroectoderm induction and assigned WNT, FGF and RA chiefly to AP patterning. Neural induction, ectoderm allocation and AP specification nevertheless overlap temporally rather than forming perfectly discrete stages (sears2022controllingneuralterritory pages 5-7). | **Moderate–high.** Combined BMP/TGF-β/WNT inhibition is a robust experimental recipe, not proof that all three pathways must be completely inactive in every embryo. SOX2 provides neural identity or competence, not AP identity by itself. |
| FGF + RA posteriorization | FGF ligands; FGFR–RAS–ERK; ALDH1A2-derived RA; RAR/RXR; GBX2, HOXA1 | Joint FGF and RA exposure biases SOX2-positive neural ectoderm toward posterior-brain identity. With WNT suppressed, this route is distinct from WNT/CDX/BRACHYURY-driven spinal or neuromesodermal specification. | Peer-reviewed hPSC modeling predicted a **28-fold GBX2 decrease without RA**, an approximately **13-fold decrease without FGF2**, and a **23-fold decrease after MEK inhibition** (sears2022controllingneuralterritory pages 17-19). A 2025 hPSC study reported that FGF plus RA—but neither alone—generated GBX2-positive, OTX2-low posterior neural ectoderm while BMP, TGF-β and WNT remained inhibited (dundes2025twoparallellineagecommitted pages 3-5). | **Moderate.** The fold changes are model predictions, not embryonic morphogen measurements. The distinct lineage-committed posterior-ectoderm claim depends heavily on the **non-peer-reviewed Dundes et al. 2025 bioRxiv preprint**. |
| OTX2/GBX2 selector boundary | OTX2; GBX2/GBX1; anterior HOX factors | Complementary homeodomain selectors delimit anterior forebrain/midbrain and posterior hindbrain territories. Reciprocal antagonism sharpens their interface and helps position the midbrain–hindbrain boundary. | In chick, Otx2 and Gbx2 domains progress from separated at HH4–8, through slight overlap at HH9, to contiguous and exclusive by HH10 (hidalgosanchez2022anupdateon pages 3-4). Mouse Gbx2 loss shifts Otx2 caudally and moves the boundary posteriorly; ectopic zebrafish gbx2 represses rostral neural markers dose-dependently (hidalgosanchez2022anupdateon pages 4-5). Classic mouse evidence assigns Gbx2 a causal role in Otx2 repression and organizer positioning (hidalgosanchez2022anupdateon pages 22-23). | **High for GBX2 restricting OTX2 and positioning the boundary; moderate for fully symmetric direct repression.** Complementary expression alone does not demonstrate direct transcriptional repression, and initial domains can arise before they contact one another. |
| Isthmic organizer | FGF8, WNT1, PAX2/5, EN1/2; OTX2/GBX2 interface | The selector interface licenses a secondary signaling center. FGF8 and WNT1, reinforced by PAX/EN circuitry, pattern adjacent midbrain and rhombomere-1 tissue and maintain organizer integrity. | Genetic and grafting evidence places Fgf8 expression after boundary formation and supports an EN1–WNT1–PAX2 maintenance loop (martinez2001theisthmicorganizer pages 1-2). FGF8 can induce ectopic isthmic-organizer and isthmocerebellar development in chick while repressing Otx2 (hidalgosanchez2022anupdateon pages 22-23). Conditional Otx loss can shift ventral Fgf8 anteriorly in mouse (puelles2004otx2regulatesthe pages 5-7). | **High** that the boundary positions the organizer and that FGF8/WNT1 are major effectors. Organizer induction and maintenance are downstream of initial AP allocation. FGF8 can persist without both selectors in some contexts, implying refinement rather than a simple linear induction pathway (dworkin2013novelmechanismsthat pages 1-2). |
| Committed anterior outputs | OTX2; SIX3, FOXG1; EN1/EN2, PAX5 | Anterior neural ectoderm retains competence for forebrain and midbrain programs: SIX3/FOXG1 mark rostral or telencephalic outputs, whereas EN1 marks midbrain progenitors. | The **non-peer-reviewed Dundes et al. 2025 bioRxiv preprint** reports FOXG1-positive/SIX3-positive forebrain and EN1-positive midbrain progenitors from anterior ectoderm. Under displayed midbrain conditions, **82.1%** of anterior-derived cells versus **0.7%** of posterior-derived cells were EN1-positive (dundes2025twoparallellineagecommitted pages 5-7, dundes2025twoparallellineagecommitted pages 22-23). Reciprocal challenges produced little AP interconversion, with anterior chromatin enriched for OTX2 and later FOXG1/LHX2-associated motifs (dundes2025twoparallellineagecommitted pages 7-9, dundes2025twoparallellineagecommitted pages 5-7). | **Provisional.** Marker production, reciprocal challenge and ATAC-seq support early restriction in vitro but do not prove irreversible commitment under every perturbation. The central result comes from a July 2025 preprint, DOI 10.1101/2025.07.02.662771. |
| Committed r5/r6 outputs | GBX2, HOXA1; HNF1B, MAFB, HOXA3; RA and FGF | Posterior neural ectoderm resolves into caudal hindbrain progenitors. RA induces an HNF1B-dependent r5/r6 program; MAFB specifies r5/r6 and activates group-3 HOX genes, while FGF supplies an additional nonredundant input. | The **non-peer-reviewed 2025 preprint** reports day-4 posterior cultures containing **79.0% MAFB-positive, 88.9% HNF1B-positive and 85.6% HOXA3-positive** cells; the displayed comparison yielded **97.3% MAFB-positive** posterior derivatives versus **1.6%** anterior derivatives (dundes2025twoparallellineagecommitted pages 22-23). In zebrafish, loss of RA, FGF, hnf1ba or valentino/mafb abolishes tested r5/r6 expression; a screen identified **107** r4–r6 genes, examined **22** candidates and analyzed **six** germline mutant lines (ghosh2018analysisofnovel pages 2-4, ghosh2018analysisofnovel pages 1-2). RA-dependent Mafb requires HNF1B, and MAFB activates Hoxa3/Hoxb3 (sturgeon2011cdx1refinespositional pages 2-3). | **High** for the vertebrate RA–HNF1B–MAFB/HOX r5/r6 network; **provisional** for derivation from a separately committed human posterior-neural lineage. Regulatory logic differs between r4 and r5/r6 and among paralog-rich vertebrate genomes. |
| Evolutionary conservation | Otx/otd; Gbx/unplugged; Pax2/5/8; anterior Hox genes | An anterior Otx territory, adjoining Gbx/Pax2/5/8 transition and posterior Hox domains constitute an ancient AP patterning topology; vertebrates elaborated this interface into the isthmic organizer. | In *Platynereis*, double in situ analyses place the otx/gbx boundary anterior to sequential hox1, hox4 and lox5 boundaries (steinmetz2011thesegmentalpattern pages 1-2, steinmetz2011thesegmentalpattern pages 3-6). Cross-phylum rescue shows partial functional interchangeability between fly otd and vertebrate OTX proteins (lichtneckert2005insightsintothe pages 7-8). The **non-peer-reviewed 2025 preprint** reports separate Otx/Sox2 and Gbx/Sox2 populations in acorn worm, zebrafish, chicken, mouse and primate material (dundes2025twoparallellineagecommitted pages 7-9, dundes2025twoparallellineagecommitted pages 9-11). | **High** for deep conservation of regionalization genes; **low–moderate** for conservation of two lineage-committed brain progenitors over approximately 550 million years. Similar expression topology does not establish homologous cell lineages or brain structures; molluscan co-option/loss demonstrates evolutionary redeployment (wollesen2017brainregionalizationgenes pages 2-3, martinduran2018convergentevolutionof pages 1-2). |


*Table: Evidence matrix linking each stage of neural ectoderm anteroposterior specification to its molecular machinery, strongest experimental support, quantitative findings and limitations. The emerging two-progenitor model is explicitly distinguished from established vertebrate mechanisms and labeled as non-peer-reviewed where appropriate.*

## 2. Definition and biological boundaries

### Included processes

The module begins once neural ectodermal identity is established or being stabilized in SOX2-positive ectoderm. It includes:

1. Interpretation of AP-biased FGF and RA signaling within neural ectoderm.
2. Establishment and sharpening of complementary OTX2-positive and GBX2/HOX-positive territories.
3. Positioning of the OTX2–GBX2 interface and its conversion into the midbrain–hindbrain boundary.
4. Restriction of regional competence toward forebrain/midbrain versus hindbrain outputs.
5. The earliest transcriptional and chromatin changes that make those outputs differentially accessible.

### Processes that should be treated separately

**Neural induction and germ-layer allocation.** BMP inhibition is required to establish neuroectoderm in most vertebrate and pluripotent-cell systems, but that event is logically upstream. TGF-β/SMAD2/3 inhibition is commonly included in “dual-SMAD” protocols, although a four-hiPSC-line systems study found it was not strictly required when other pathways were appropriately controlled. Thus, combined BMP/TGF-β/WNT inhibition is a robust experimental recipe, not a universal demonstration that all three signals are completely absent in vivo (sears2022controllingneuralterritory pages 5-7).

**Neural plate border specification.** Neural crest and placodal progenitors form at the lateral neural/non-neural interface through BMP, WNT, FGF, and border-specific gene networks. This is a mediolateral fate decision, not the OTX2–GBX2 AP partition within medial neural ectoderm (thawani2020buildingtheborder pages 2-3).

**Neuromesodermal and spinal-cord specification.** Strong WNT/FGF activity can generate BRACHYURY/CDX-positive axial progenitors and posterior neural tube. The hindbrain route reviewed here is distinguished operationally by retained WNT suppression during the earliest FGF-plus-RA induction and by GBX2/HOXA1 rather than BRACHYURY/CDX2 identity. Human axial stem-cell capture with WNT/FGF therefore models a neighboring but distinct posterior program (kelle2024captureofhuman pages 50-53, dundes2025twoparallellineagecommitted pages 3-5).

**Isthmic-organizer signaling.** FGF8 and WNT1 emitted at the mature OTX2–GBX2 interface pattern adjacent tissue. This secondary-organizer activity should not be conflated with the earlier, broader FGF input that helps posteriorize neural ectoderm (martinez2001theisthmicorganizer pages 1-2, dworkin2013novelmechanismsthat pages 1-2).

**Later regional programs.** FOXG1/SIX3 forebrain, EN1 midbrain, segmented hindbrain, dorsoventral neural-tube, and cerebellar programs are outputs or continuations of AP specification. They are useful functional readouts but are not synonymous with the initial bifurcation.

### Competing definitions

The traditional “activation–transformation” framework holds that neural induction initially yields predominantly anterior neural character, which posterior signals progressively transform into hindbrain and spinal identities. A newer “parallel progenitor” model instead proposes simultaneous OTX2-positive anterior neural ectoderm and GBX2/HOX-positive posterior neural ectoderm, with early lineage restriction. Current evidence supports aspects of both: anterior identity is readily produced when posteriorizing signals are withheld, but posterior hindbrain ectoderm can emerge extremely early and appears resistant to reciprocal regional signals in hPSC experiments (sears2022controllingneuralterritory pages 17-19, dundes2025twoparallellineagecommitted pages 3-5, dundes2025twoparallellineagecommitted pages 5-7).

## 3. Mechanistic overview

### 3.1 Neural competence and the initial AP decision

SOX2 establishes or maintains neural ectodermal competence but does not itself encode AP position. In controlled hPSC differentiation, BMP inhibition is the most consistent neural-induction requirement, whereas WNT, FGF, and RA principally determine AP character. These processes overlap temporally, so “neural induction first, regionalization second” is a useful causal abstraction rather than a perfectly separated embryological sequence (sears2022controllingneuralterritory pages 5-7, thawani2020buildingtheborder pages 2-3).

In the anterior branch, low WNT/RA activity preserves OTX2 and permits later SIX3 and FOXG1 induction. In the posterior-brain branch, FGF signaling through FGFR–RAS–RAF–MEK–ERK and RA signaling through nuclear RAR/RXR receptors promote GBX2 and anterior HOX programs. RA is synthesized from retinaldehyde by ALDH1A2/RALDH2 in neighboring posterior tissues. A peer-reviewed hPSC design-of-experiments model predicted a 28-fold fall in GBX2 after RA omission, an approximately 13-fold fall after FGF2 omission, and a 23-fold fall following MEK inhibition. These are model-derived culture effects, not direct measurements of an embryonic gradient (sears2022controllingneuralterritory pages 17-19).

The 2025 preprint reports a stricter combinatorial requirement: neither FGF nor RA alone produced posterior neural ectoderm efficiently, whereas their combination generated GBX2-positive, OTX2-low cells while BMP, TGF-β, and WNT remained inhibited. The resulting population expressed HOXA1/HOXB1 but not BRACHYURY or CDX2, separating hindbrain posteriorization from trunk/NMP induction (dundes2025twoparallellineagecommitted pages 3-5).

### 3.2 OTX2–GBX2 selector antagonism

OTX2 and GBX2 are homeodomain transcription factors occupying complementary neural territories. In chick, the domains are separated at HH4–HH8, overlap slightly around HH9, and become contiguous and mutually exclusive by HH10. Their early independent establishment followed by contact-dependent refinement argues against reducing the mechanism to a single instantaneous toggle (hidalgosanchez2022anupdateon pages 3-4).

The strongest directional genetic evidence is that GBX2 confines OTX2. Mouse Gbx2 loss shifts the Otx2 domain caudally toward the r3/r4 region and displaces the midbrain–hindbrain boundary posteriorly; conditional loss after E8.5 produces a milder posterior shift and ectopic Otx2-positive cerebellar aggregates. Conversely, ectopic zebrafish gbx2 represses rostral neural markers dose-dependently and, at high dose, severely disrupts forebrain, diencephalic, midbrain, isthmic, and cerebellar territories (hidalgosanchez2022anupdateon pages 4-5).

OTX proteins reciprocally help exclude posterior identities and regulate midbrain competence, but “mutual repression” should be interpreted carefully. Complementary domains and reciprocal mutant phenotypes do not by themselves prove direct binding to each other’s regulatory elements in every species. Moreover, FGF8 can be initiated in neuroectoderm lacking both selectors in some experimental contexts, implying that OTX2/GBX2 position and refine organizer competence rather than forming a universally sufficient linear switch (dworkin2013novelmechanismsthat pages 1-2, puelles2004otx2regulatesthe pages 5-7).

### 3.3 Boundary-to-organizer transition

Once the selector interface is established, PAX2/5, EN1/2, WNT1, and FGF8 form a reinforcing regulatory system. Fgf8 is expressed primarily on the hindbrain side, whereas Wnt1 is associated with the midbrain side. The resulting planar signals pattern adjacent midbrain and anterior hindbrain and stabilize organizer tissue. FGF8 can induce ectopic isthmic-organizer and isthmocerebellar development in chick while repressing Otx2, and conditional Otx loss can shift ventral Fgf8 expression anteriorly in mouse. Wnt1 loss causes partial or complete loss of midbrain, isthmic, and cerebellar structures, illustrating its maintenance and survival functions (hidalgosanchez2022anupdateon pages 22-23, martinez2001theisthmicorganizer pages 1-2, puelles2004otx2regulatesthe pages 5-7).

The physical neural-tube constriction appears after the molecular interface. In chick, the OTX2–GBX2 limit is initially distant from the visible mesencephalic/metencephalic constriction but coincides with it at later stages. Molecular regionalization therefore precedes overt morphology (hidalgosanchez2022anupdateon pages 3-4).

### 3.4 Commitment and regional outputs

The most direct evidence for early lineage restriction comes from Dundes et al. Mouse E7.5 SOX2-positive ectoderm contained mutually exclusive OTX2-positive and GBX2-positive populations before later SOX1/PAX6 neural-progenitor markers appeared. Acute Gbx2 lineage labeling yielded descendants restricted to hindbrain through E18.5. Sparse Sox2 tracing across 16 embryos placed 62.96% of clonal clusters in forebrain/midbrain and 32.59% in hindbrain, although sparse lineage reconstruction cannot formally exclude rare cross-boundary progenitors (dundes2025twoparallellineagecommitted pages 3-5).

In reciprocal hPSC challenges, anterior ectoderm remained competent for forebrain/midbrain but not hindbrain, whereas posterior ectoderm remained competent for hindbrain but not forebrain/midbrain. Under midbrain conditions, 82.1% of anterior-derived cells versus 0.7% of posterior-derived cells became EN1 positive. Under hindbrain conditions, 97.3% of posterior-derived cells versus 1.6% of anterior-derived cells became MAFB positive. Posterior cultures contained 79.0% MAFB-positive, 88.9% HNF1B-positive, and 85.6% HOXA3-positive cells (dundes2025twoparallellineagecommitted pages 22-23).

OmniATAC-seq provided a plausible mechanism: anterior cells were enriched for OTX2-associated regulatory accessibility and later FOXG1/LHX2 motifs, whereas posterior cells showed HOX, HNF1B, MAFB, ETV1, RARB, and RXRG-associated accessibility. Importantly, inappropriate regional cues did not simply erase the starting landscape. These observations support chromatin-encoded competence restriction, but they establish resistance to the tested signals—not absolute irreversibility under all genetic or epigenetic interventions (dundes2025twoparallellineagecommitted pages 7-9, dundes2025twoparallellineagecommitted pages 5-7).

## 4. Major molecular players and active assemblies

### SOX2

SOX2 is the common neural-ectoderm competence factor. Its presence identifies the territory in which AP selection occurs, but its concentration and chromatin partners can alter how cells respond to WNT. It should therefore be viewed as a context-setting factor rather than an anterior or posterior selector.

### FGF machinery

Posteriorizing FGFs bind dimeric FGFR receptor tyrosine kinases with heparan-sulfate co-receptors and activate FRS adaptors, RAS–RAF–MEK–ERK, and context-dependent PI3K/PLCγ branches. FGF8 has two separable roles: a broad early posteriorizing/competence role and a later localized isthmic-organizer role. Failure to separate these phases is a recurrent source of conceptual confusion.

### RA machinery

ALDH1A2/RALDH2 produces RA; cellular retinoid-binding proteins and CYP26 enzymes influence its availability; RAR/RXR heterodimers bind RA-response elements and regulate anterior HOX and hindbrain genes. RA is dose- and time-dependent rather than simply “posteriorizing.” Lower or appropriately timed RA promotes MAFB in r5/r6, whereas excessive or more caudal RA contexts suppress MAFB and favor more posterior identities (sturgeon2011cdx1refinespositional pages 2-3).

### OTX2 and GBX2

These homeoproteins are selectors in the classical sense: they stabilize alternative regional transcriptional states, exclude incompatible programs, and determine where a signaling center can form. GBX2-to-OTX2 repression has particularly strong loss- and gain-of-function support; fully symmetric direct repression remains less completely resolved across species (hidalgosanchez2022anupdateon pages 22-23, hidalgosanchez2022anupdateon pages 4-5).

### Isthmic-organizer circuit

FGF8, WNT1, PAX2/PAX5, and EN1/EN2 form a cross-regulatory maintenance network centered on the OTX2–GBX2 boundary. This circuit is not a stable stoichiometric protein complex; it is a tissue-scale gene-regulatory and paracrine signaling assembly. Cell adhesion, lineage restriction, extracellular-matrix interactions, and gap-junctional communication may sharpen or maintain the physical boundary, but these are accessory to the defining selector/signaling circuit (dworkin2013novelmechanismsthat pages 1-2, martinez2001theisthmicorganizer pages 1-2).

### r5/r6 regulatory network

RA induces HNF1B/vHNF1, which is necessary but not sufficient for MAFB expression. MAFB is an early r5/r6 selector and activates group-3 HOX genes, including Hoxa3/Hoxb3. CDX factors delimit the caudal edge by repressing Mafb, thereby preventing r5/r6 identity from spreading into r7/r8 and spinal territory. FGF provides an additional nonredundant input (sturgeon2011cdx1refinespositional pages 2-3, sturgeon2011cdx1refinespositional pages 1-2).

A zebrafish screen identified 107 genes expressed in r4–r6 during the first 24 hours, selected 22 for regulatory analysis, and tested six germline mutant lines. Individual disruption of RA, FGF, hnf1ba, or valentino/mafb abolished the tested r5/r6 expression program, whereas r4 was more robust and combinatorially regulated. This demonstrates that “hindbrain specification” is not one uniform mechanism across rhombomeres (ghosh2018analysisofnovel pages 2-4, ghosh2018analysisofnovel pages 1-2).

## 5. Evolutionary and cell-biological variation

### Vertebrates

The Otx/Gbx interface and isthmic FGF/WNT organizer are strongly conserved in fish, amphibians, birds, and mammals. Nevertheless, paralog use differs: zebrafish deploy gbx1 and gbx2, duplicated Hox genes, and valentino/mafb circuitry, whereas mammals rely on different paralog combinations and enhancer architectures. Timing also differs with gastrulation mode, neurulation, and embryonic geometry. Results from zebrafish morphants, chick electroporation, mouse conditional mutants, and human hPSCs are complementary but not automatically interchangeable (hidalgosanchez2022anupdateon pages 3-4, hidalgosanchez2022anupdateon pages 5-6, ghosh2018analysisofnovel pages 1-2).

### Deeper bilaterian conservation

In the annelid *Platynereis dumerilii*, otx occupies a presegmental anterior region, gbx abuts it in a cryptic first segment, and hox1, hox4, and lox5 begin in successive posterior segments. This supports an ancient AP topography in which Otx is anterior to Gbx and Hox territories (steinmetz2011thesegmentalpattern pages 1-2, steinmetz2011thesegmentalpattern pages 2-3, steinmetz2011thesegmentalpattern pages 3-6).

Cross-phylum rescue provides functional evidence beyond expression: fly *otd* can rescue parts of mouse Otx phenotypes, and human OTX proteins can restore anterior brain structures in *Drosophila otd* mutants. Rescue remains context-dependent, demonstrating conservation of biochemical selector activity without proving one-to-one homology of entire brain regions (lichtneckert2005insightsintothe pages 7-8).

Molluscs illustrate evolutionary redeployment. Gbx retains neural expression in some lineages but has been co-opted into shell-field patterning and apparently lost from the developing CNS in some bivalves. Likewise, comparative studies caution that similar developmental genes can pattern independently evolved nervous-system architectures (wollesen2017brainregionalizationgenes pages 2-3, martinduran2018convergentevolutionof pages 1-2).

The 2025 study reports separate Otx/Sox2 and Gbx/Sox2 territories in acorn worm, zebrafish, chicken, mouse, and primate samples and proposes conservation of two progenitor classes over approximately 550 million years. That is a plausible hypothesis, but comparable expression domains do not yet demonstrate homologous lineage restriction in all those organisms (dundes2025twoparallellineagecommitted pages 7-9, dundes2025twoparallellineagecommitted pages 9-11).

## 6. Constraints, dependencies, and failure modes

### Ordering constraints

1. Neural competence must be established before AP selectors can be interpreted as neural identities.
2. Broad AP inputs and initial OTX2/GBX expression precede mature organizer signaling.
3. The molecular OTX2–GBX2 interface precedes the visible midbrain–hindbrain constriction.
4. Regional competence restriction precedes robust FOXG1/SIX3, EN1, or MAFB/HNF1B/HOXA3 progenitor output.

### Mutually exclusive and compartment-specific events

OTX2-high anterior and GBX2-high posterior selector states become mutually exclusive at the mature boundary. FGF8 and WNT1 occupy opposite but interacting sides of the organizer. Early hindbrain pNE and WNT/CDX-positive spinal/NMP identity are also experimentally separable: excessive or mistimed WNT can move cells out of the reviewed module into axial progenitor programs (dundes2025twoparallellineagecommitted pages 3-5, martinez2001theisthmicorganizer pages 1-2).

### Failure modes

- **Insufficient BMP suppression:** poor neural induction or persistence of non-neural ectoderm.
- **Excess early WNT:** CDX/BRACHYURY-positive trunk or NMP identity rather than hindbrain.
- **Insufficient FGF or RA:** failure of GBX2/anterior-HOX posterior neural identity; the culture model predicts large GBX2 losses after either omission (sears2022controllingneuralterritory pages 17-19).
- **GBX2 loss:** caudal OTX2 expansion, posterior organizer displacement, r1–r3 and cerebellar abnormalities (hidalgosanchez2022anupdateon pages 4-5).
- **Excess GBX2:** loss of rostral neural territories and disruption of isthmic organization (hidalgosanchez2022anupdateon pages 4-5).
- **OTX loss:** anterior neural and midbrain competence defects and altered FGF8 positioning (hidalgosanchez2022anupdateon pages 3-4, puelles2004otx2regulatesthe pages 5-7).
- **FGF8/WNT1 circuit failure:** defective organizer maintenance and loss of midbrain/isthmo-cerebellar structures (hidalgosanchez2022anupdateon pages 22-23, martinez2001theisthmicorganizer pages 1-2).
- **RA–HNF1B–MAFB disruption:** failure of r5/r6 markers, segmentation, and associated motor-neuron programs (sturgeon2011cdx1refinespositional pages 2-3, ghosh2018analysisofnovel pages 1-2).

## 7. Current applications and real-world implementations

**Directed differentiation.** Signaling logic is already used to generate regionally defined neural cells from hPSCs. Systems optimization can produce SIX3-positive anterior or GBX2-positive posterior neuroectoderm across multiple cell lines. The newer two-progenitor protocol generated high-purity EN1-positive midbrain and MAFB/HNF1B/HOXA3-positive r5/r6 progenitors, followed by cholinergic PHOX2A/PHOX2B-positive hindbrain motor neurons with spontaneous calcium activity, membrane currents, and optogenetically evoked responses (sears2022controllingneuralterritory pages 17-19, dundes2025twoparallellineagecommitted pages 22-23, dundes2025twoparallellineagecommitted pages 24-26).

**Organoids and quality control.** AP selectors and accessible-chromatin signatures can diagnose whether a brain organoid contains intended forebrain, midbrain, or hindbrain progenitors. This is important because apparently neuronal cultures can be regionally incorrect even when they express pan-neural markers. Recent organoid work also implicates BAF chromatin-remodeling activity in maintaining forebrain patterning, although the available 2024 evidence has small sample sizes—for example, n=2 in some longitudinal qPCR comparisons—and should be regarded as emerging (kube2024theactivityof pages 140-145).

**Disease modeling and cell therapy.** Accurate AP identity is critical for producing ventral midbrain dopaminergic neurons for Parkinson’s disease studies, cranial motor neurons for hindbrain disorders, and forebrain neurons for cortical disease models. The module supplies a developmental quality-control framework: transplantation or disease phenotypes should not be interpreted without confirming regional identity.

**Developmental toxicology.** RA excess, RA deficiency, FGFR/MEK inhibitors, and WNT-modulating compounds can alter AP identity before overt neural-tube morphology changes. OTX2/GBX2/HOX readouts therefore provide sensitive endpoints for teratogenicity screens.

## 8. Controversies and open questions

1. **One pan-brain progenitor or two parallel progenitors?** The two-progenitor model explains reciprocal challenge resistance and early chromatin divergence, but its decisive evidence is currently a 2025 preprint. Prospective clonal recording from pre-gastrulation through organogenesis is needed to establish whether a transient common progenitor exists in vivo (dundes2025twoparallellineagecommitted pages 3-5, dundes2025twoparallellineagecommitted pages 7-9).

2. **How direct is OTX2–GBX2 repression?** GBX2 restriction of OTX2 is genetically strong, but direct enhancer occupancy, cofactor requirements, and symmetry of the two arms remain incompletely defined across vertebrates (hidalgosanchez2022anupdateon pages 4-5, dworkin2013novelmechanismsthat pages 1-2).

3. **Are FGF and RA true graded instructive signals or permissive gates?** Culture perturbations demonstrate necessity and dose dependence, but direct in-vivo measurements linking ligand concentration, exposure duration, receptor occupancy, and selector choice remain limited.

4. **What establishes the initial domains before contact?** Chick timing shows that Otx2 and Gbx2 territories initially arise apart. Their upstream enhancers must therefore integrate axial signals before mutual antagonism sharpens the boundary (hidalgosanchez2022anupdateon pages 3-4).

5. **What is the commitment mechanism?** ATAC-seq implicates differential enhancer accessibility and motifs for OTX2, HOX, HNF1B, MAFB, ETV1, and RAR/RXR. Causal tests—enhancer deletion, pioneer-factor perturbation, and chromatin-remodeler manipulation—are required to distinguish cause from correlated accessibility (dundes2025twoparallellineagecommitted pages 5-7, dundes2025twoparallellineagecommitted pages 22-23).

6. **How well do hPSC states match embryos?** Marker combinations and cross-species transcriptomes are supportive, but culture doses, uniform exposure, and two-dimensional geometry differ sharply from gastrulating embryos. Human embryonic validation remains especially limited.

7. **How ancient is the complete module?** Otx/Gbx/Hox regionalization is likely ancient, whereas the vertebrate FGF8/WNT1 isthmic organizer is an elaboration. Conservation of gene topography should not be equated with conservation of lineage restriction or homologous adult brain structures (steinmetz2011thesegmentalpattern pages 1-2, wollesen2017brainregionalizationgenes pages 2-3, martinduran2018convergentevolutionof pages 1-2).

## 9. Key references

- **Dundes CE et al.** “Two parallel lineage-committed progenitors contribute to the developing brain.” bioRxiv, posted **5 July 2025**. DOI: [10.1101/2025.07.02.662771](https://doi.org/10.1101/2025.07.02.662771). Central source for the parallel-progenitor, reciprocal-challenge, lineage-tracing, ATAC-seq, and r5/r6 differentiation model; **not peer reviewed** (dundes2025twoparallellineagecommitted pages 3-5, dundes2025twoparallellineagecommitted pages 22-23).
- **Sears KE et al.** “Controlling neural territory patterning from pluripotency using a systems developmental biology approach.” *iScience* 25:104133, published **15 April 2022**. DOI: [10.1016/j.isci.2022.104133](https://doi.org/10.1016/j.isci.2022.104133) (sears2022controllingneuralterritory pages 17-19, sears2022controllingneuralterritory pages 5-7).
- **Hidalgo-Sánchez M et al.** “An Update on the Molecular Mechanism of the Vertebrate Isthmic Organizer Development in the Context of the Neuromeric Model.” *Frontiers in Neuroanatomy* 16:826976, published **24 March 2022**. DOI: [10.3389/fnana.2022.826976](https://doi.org/10.3389/fnana.2022.826976) (hidalgosanchez2022anupdateon pages 1-2, hidalgosanchez2022anupdateon pages 3-4).
- **Millet S et al.** “A role for Gbx2 in repression of Otx2 and positioning the mid/hindbrain organizer.” *Nature* 401:161–164, **September 1999**. DOI: [10.1038/43664](https://doi.org/10.1038/43664) (hidalgosanchez2022anupdateon pages 22-23).
- **Martinez-Barbera JP et al.** Mutual OTX2/GBX2 antagonism and anterior neuroectoderm competence. *Development* 128:4789–4800, **2001**. DOI: [10.1242/dev.128.23.4789](https://doi.org/10.1242/dev.128.23.4789) (hidalgosanchez2022anupdateon pages 22-23).
- **Puelles E et al.** “Otx2 regulates the extent, identity and fate of neuronal progenitor domains in the ventral midbrain.” *Development* 131:2037–2048, **May 2004**. DOI: [10.1242/dev.01107](https://doi.org/10.1242/dev.01107) (puelles2004otx2regulatesthe pages 5-7).
- **Ghosh P, Maurer JM, Sagerström CG.** “Analysis of novel caudal hindbrain genes reveals different regulatory logic for gene expression in rhombomere 4 versus 5/6 in embryonic zebrafish.” *Neural Development*, **June 2018**. DOI: [10.1186/s13064-018-0112-y](https://doi.org/10.1186/s13064-018-0112-y) (ghosh2018analysisofnovel pages 2-4, ghosh2018analysisofnovel pages 1-2).
- **Sturgeon K et al.** “Cdx1 refines positional identity of the vertebrate hindbrain by directly repressing Mafb expression.” *Development* 138:65–74, **January 2011**. DOI: [10.1242/dev.058727](https://doi.org/10.1242/dev.058727) (sturgeon2011cdx1refinespositional pages 2-3).
- **Steinmetz PRH et al.** “The segmental pattern of otx, gbx, and Hox genes in the annelid *Platynereis dumerilii*.” *Evolution & Development* 13:72–79, **January 2011**. DOI: [10.1111/j.1525-142X.2010.00457.x](https://doi.org/10.1111/j.1525-142X.2010.00457.x) (steinmetz2011thesegmentalpattern pages 1-2, steinmetz2011thesegmentalpattern pages 3-6).
- **Martín-Durán JM et al.** “Convergent evolution of bilaterian nerve cords.” *Nature* 553:45–50, published **4 January 2018**. DOI: [10.1038/nature25030](https://doi.org/10.1038/nature25030). Important caution against inferring anatomical homology solely from conserved developmental genes (martinduran2018convergentevolutionof pages 1-2).

References

1. (sears2022controllingneuralterritory pages 5-7): Katie E. Sears, Keerthi Gullapalli, Divya Trivedi, Alexander Mihas, Michael A. Bukys, and Jan Jensen. Controlling neural territory patterning from pluripotency using a systems developmental biology approach. Apr 2022. URL: https://doi.org/10.1016/j.isci.2022.104133, doi:10.1016/j.isci.2022.104133. This article has 4 citations and is from a peer-reviewed journal.

2. (martinez2001theisthmicorganizer pages 1-2): Salvador Martinez. The isthmic organizer and brain regionalization. The International journal of developmental biology, 45 1:367-71, Jan 2001. URL: https://doi.org/10.1387/ijdb.11291867, doi:10.1387/ijdb.11291867. This article has 149 citations.

3. (dworkin2013novelmechanismsthat pages 1-2): Sebastian Dworkin and Stephen M. Jane. Novel mechanisms that pattern and shape the midbrain-hindbrain boundary. Cellular and Molecular Life Sciences, 70:3365-3374, Jan 2013. URL: https://doi.org/10.1007/s00018-012-1240-x, doi:10.1007/s00018-012-1240-x. This article has 45 citations and is from a domain leading peer-reviewed journal.

4. (dundes2025twoparallellineagecommitted pages 3-5): Carolyn E. Dundes, Rayyan T. Jokhai, Hadia Ahsan, Rachel S. Kang, Rachel E.A. Salomon-Shulman, Arjun Rajan, Yoon Seok Kim, Liam J. Stanton, Christine Xu, Stephanie Do, Brennan D. McDonald, José Miguel Andrade López, Hugo A. Urrutia, Hannah Greenfeld, Alicia Wong, Yimiao Qu, Andrew S. Petkovic, Yi Miao, K. Christopher Garcia, Michelle Monje, Daniel E. Wagner, Marianne E. Bronner, Christopher J. Lowe, and Kyle M. Loh. Two parallel lineage-committed progenitors contribute to the developing brain. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.02.662771, doi:10.1101/2025.07.02.662771. This article has 4 citations.

5. (dundes2025twoparallellineagecommitted pages 7-9): Carolyn E. Dundes, Rayyan T. Jokhai, Hadia Ahsan, Rachel S. Kang, Rachel E.A. Salomon-Shulman, Arjun Rajan, Yoon Seok Kim, Liam J. Stanton, Christine Xu, Stephanie Do, Brennan D. McDonald, José Miguel Andrade López, Hugo A. Urrutia, Hannah Greenfeld, Alicia Wong, Yimiao Qu, Andrew S. Petkovic, Yi Miao, K. Christopher Garcia, Michelle Monje, Daniel E. Wagner, Marianne E. Bronner, Christopher J. Lowe, and Kyle M. Loh. Two parallel lineage-committed progenitors contribute to the developing brain. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.02.662771, doi:10.1101/2025.07.02.662771. This article has 4 citations.

6. (dundes2025twoparallellineagecommitted pages 5-7): Carolyn E. Dundes, Rayyan T. Jokhai, Hadia Ahsan, Rachel S. Kang, Rachel E.A. Salomon-Shulman, Arjun Rajan, Yoon Seok Kim, Liam J. Stanton, Christine Xu, Stephanie Do, Brennan D. McDonald, José Miguel Andrade López, Hugo A. Urrutia, Hannah Greenfeld, Alicia Wong, Yimiao Qu, Andrew S. Petkovic, Yi Miao, K. Christopher Garcia, Michelle Monje, Daniel E. Wagner, Marianne E. Bronner, Christopher J. Lowe, and Kyle M. Loh. Two parallel lineage-committed progenitors contribute to the developing brain. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.02.662771, doi:10.1101/2025.07.02.662771. This article has 4 citations.

7. (sears2022controllingneuralterritory pages 17-19): Katie E. Sears, Keerthi Gullapalli, Divya Trivedi, Alexander Mihas, Michael A. Bukys, and Jan Jensen. Controlling neural territory patterning from pluripotency using a systems developmental biology approach. Apr 2022. URL: https://doi.org/10.1016/j.isci.2022.104133, doi:10.1016/j.isci.2022.104133. This article has 4 citations and is from a peer-reviewed journal.

8. (hidalgosanchez2022anupdateon pages 3-4): Matías Hidalgo-Sánchez, Abraham Andreu-Cervera, Sergio Villa-Carballar, and Diego Echevarria. An update on the molecular mechanism of the vertebrate isthmic organizer development in the context of the neuromeric model. Frontiers in Neuroanatomy, Mar 2022. URL: https://doi.org/10.3389/fnana.2022.826976, doi:10.3389/fnana.2022.826976. This article has 20 citations.

9. (hidalgosanchez2022anupdateon pages 4-5): Matías Hidalgo-Sánchez, Abraham Andreu-Cervera, Sergio Villa-Carballar, and Diego Echevarria. An update on the molecular mechanism of the vertebrate isthmic organizer development in the context of the neuromeric model. Frontiers in Neuroanatomy, Mar 2022. URL: https://doi.org/10.3389/fnana.2022.826976, doi:10.3389/fnana.2022.826976. This article has 20 citations.

10. (hidalgosanchez2022anupdateon pages 22-23): Matías Hidalgo-Sánchez, Abraham Andreu-Cervera, Sergio Villa-Carballar, and Diego Echevarria. An update on the molecular mechanism of the vertebrate isthmic organizer development in the context of the neuromeric model. Frontiers in Neuroanatomy, Mar 2022. URL: https://doi.org/10.3389/fnana.2022.826976, doi:10.3389/fnana.2022.826976. This article has 20 citations.

11. (puelles2004otx2regulatesthe pages 5-7): Eduardo Puelles, Alessandro Annino, Francesca Tuorto, Alessandro Usiello, Dario Acampora, Thomas Czerny, Claude Brodski, Siew-Lan Ang, Wolfgang Wurst, and Antonio Simeone. Otx2 regulates the extent, identity and fate of neuronal progenitor domains in the ventral midbrain. Development, 131:2037-2048, May 2004. URL: https://doi.org/10.1242/dev.01107, doi:10.1242/dev.01107. This article has 273 citations and is from a domain leading peer-reviewed journal.

12. (dundes2025twoparallellineagecommitted pages 22-23): Carolyn E. Dundes, Rayyan T. Jokhai, Hadia Ahsan, Rachel S. Kang, Rachel E.A. Salomon-Shulman, Arjun Rajan, Yoon Seok Kim, Liam J. Stanton, Christine Xu, Stephanie Do, Brennan D. McDonald, José Miguel Andrade López, Hugo A. Urrutia, Hannah Greenfeld, Alicia Wong, Yimiao Qu, Andrew S. Petkovic, Yi Miao, K. Christopher Garcia, Michelle Monje, Daniel E. Wagner, Marianne E. Bronner, Christopher J. Lowe, and Kyle M. Loh. Two parallel lineage-committed progenitors contribute to the developing brain. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.02.662771, doi:10.1101/2025.07.02.662771. This article has 4 citations.

13. (ghosh2018analysisofnovel pages 2-4): Priyanjali Ghosh, Jennifer M. Maurer, and Charles G. Sagerström. Analysis of novel caudal hindbrain genes reveals different regulatory logic for gene expression in rhombomere 4 versus 5/6 in embryonic zebrafish. Neural Development, Jun 2018. URL: https://doi.org/10.1186/s13064-018-0112-y, doi:10.1186/s13064-018-0112-y. This article has 17 citations and is from a peer-reviewed journal.

14. (ghosh2018analysisofnovel pages 1-2): Priyanjali Ghosh, Jennifer M. Maurer, and Charles G. Sagerström. Analysis of novel caudal hindbrain genes reveals different regulatory logic for gene expression in rhombomere 4 versus 5/6 in embryonic zebrafish. Neural Development, Jun 2018. URL: https://doi.org/10.1186/s13064-018-0112-y, doi:10.1186/s13064-018-0112-y. This article has 17 citations and is from a peer-reviewed journal.

15. (sturgeon2011cdx1refinespositional pages 2-3): Kendra Sturgeon, Tomomi Kaneko, Melissa Biemann, Andree Gauthier, Kallayanee Chawengsaksophak, and Sabine P. Cordes. Cdx1 refines positional identity of the vertebrate hindbrain by directly repressing mafb expression. Development, 138:65-74, Jan 2011. URL: https://doi.org/10.1242/dev.058727, doi:10.1242/dev.058727. This article has 47 citations and is from a domain leading peer-reviewed journal.

16. (steinmetz2011thesegmentalpattern pages 1-2): Patrick R. H. Steinmetz, Roman P. Kostyuchenko, Antje Fischer, and Detlev Arendt. The segmental pattern of otx, gbx, and hox genes in the annelid platynereis dumerilii. Evolution & Development, 13:72-79, Jan 2011. URL: https://doi.org/10.1111/j.1525-142x.2010.00457.x, doi:10.1111/j.1525-142x.2010.00457.x. This article has 124 citations and is from a peer-reviewed journal.

17. (steinmetz2011thesegmentalpattern pages 3-6): Patrick R. H. Steinmetz, Roman P. Kostyuchenko, Antje Fischer, and Detlev Arendt. The segmental pattern of otx, gbx, and hox genes in the annelid platynereis dumerilii. Evolution & Development, 13:72-79, Jan 2011. URL: https://doi.org/10.1111/j.1525-142x.2010.00457.x, doi:10.1111/j.1525-142x.2010.00457.x. This article has 124 citations and is from a peer-reviewed journal.

18. (lichtneckert2005insightsintothe pages 7-8): R. Lichtneckert and H. Reichert. Insights into the urbilaterian brain: conserved genetic patterning mechanisms in insect and vertebrate brain development. Heredity, 94:465-477, May 2005. URL: https://doi.org/10.1038/sj.hdy.6800664, doi:10.1038/sj.hdy.6800664. This article has 175 citations and is from a domain leading peer-reviewed journal.

19. (dundes2025twoparallellineagecommitted pages 9-11): Carolyn E. Dundes, Rayyan T. Jokhai, Hadia Ahsan, Rachel S. Kang, Rachel E.A. Salomon-Shulman, Arjun Rajan, Yoon Seok Kim, Liam J. Stanton, Christine Xu, Stephanie Do, Brennan D. McDonald, José Miguel Andrade López, Hugo A. Urrutia, Hannah Greenfeld, Alicia Wong, Yimiao Qu, Andrew S. Petkovic, Yi Miao, K. Christopher Garcia, Michelle Monje, Daniel E. Wagner, Marianne E. Bronner, Christopher J. Lowe, and Kyle M. Loh. Two parallel lineage-committed progenitors contribute to the developing brain. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.02.662771, doi:10.1101/2025.07.02.662771. This article has 4 citations.

20. (wollesen2017brainregionalizationgenes pages 2-3): Tim Wollesen, Maik Scherholz, Sonia Victoria Rodríguez Monje, Emanuel Redl, Christiane Todt, and Andreas Wanninger. Brain regionalization genes are co-opted into shell field patterning in mollusca. Scientific Reports, Jul 2017. URL: https://doi.org/10.1038/s41598-017-05605-5, doi:10.1038/s41598-017-05605-5. This article has 40 citations and is from a peer-reviewed journal.

21. (martinduran2018convergentevolutionof pages 1-2): José M. Martín-Durán, Kevin Pang, Aina Børve, Henrike Semmler Lê, Anlaug Furu, Johanna Taylor Cannon, Ulf Jondelius, and Andreas Hejnol. Convergent evolution of bilaterian nerve cords. Dec 2018. URL: https://doi.org/10.1038/nature25030, doi:10.1038/nature25030. This article has 198 citations and is from a highest quality peer-reviewed journal.

22. (thawani2020buildingtheborder pages 2-3): Ankita Thawani and Andrew K. Groves. Building the border: development of the chordate neural plate border region and its derivatives. Frontiers in Physiology, Dec 2020. URL: https://doi.org/10.3389/fphys.2020.608880, doi:10.3389/fphys.2020.608880. This article has 63 citations.

23. (kelle2024captureofhuman pages 50-53): Dolunay Kelle, Enes Ugur, Ejona Rusha, Dmitry Shaposhnikov, Alessandra Livigni, Sandra Horschitz, Mahnaz Davoudi, Andreas Blutke, Judith Bushe, Michael Sterr, Ksenia Arkhipova, Benjamin Tak, Ruben de Vries, Mazène Hochane, Britte Spruijt, Aicha Haji Ali, Heiko Lickert, Annette Feuchtinger, Philipp Koch, Matthias Mann, Heinrich Leonhardt, Valerie Wilson, and Micha Drukker. Capture of human neuromesodermal and posterior neural tube axial stem cells. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.26.586760, doi:10.1101/2024.03.26.586760. This article has 4 citations.

24. (sturgeon2011cdx1refinespositional pages 1-2): Kendra Sturgeon, Tomomi Kaneko, Melissa Biemann, Andree Gauthier, Kallayanee Chawengsaksophak, and Sabine P. Cordes. Cdx1 refines positional identity of the vertebrate hindbrain by directly repressing mafb expression. Development, 138:65-74, Jan 2011. URL: https://doi.org/10.1242/dev.058727, doi:10.1242/dev.058727. This article has 47 citations and is from a domain leading peer-reviewed journal.

25. (hidalgosanchez2022anupdateon pages 5-6): Matías Hidalgo-Sánchez, Abraham Andreu-Cervera, Sergio Villa-Carballar, and Diego Echevarria. An update on the molecular mechanism of the vertebrate isthmic organizer development in the context of the neuromeric model. Frontiers in Neuroanatomy, Mar 2022. URL: https://doi.org/10.3389/fnana.2022.826976, doi:10.3389/fnana.2022.826976. This article has 20 citations.

26. (steinmetz2011thesegmentalpattern pages 2-3): Patrick R. H. Steinmetz, Roman P. Kostyuchenko, Antje Fischer, and Detlev Arendt. The segmental pattern of otx, gbx, and hox genes in the annelid platynereis dumerilii. Evolution & Development, 13:72-79, Jan 2011. URL: https://doi.org/10.1111/j.1525-142x.2010.00457.x, doi:10.1111/j.1525-142x.2010.00457.x. This article has 124 citations and is from a peer-reviewed journal.

27. (dundes2025twoparallellineagecommitted pages 24-26): Carolyn E. Dundes, Rayyan T. Jokhai, Hadia Ahsan, Rachel S. Kang, Rachel E.A. Salomon-Shulman, Arjun Rajan, Yoon Seok Kim, Liam J. Stanton, Christine Xu, Stephanie Do, Brennan D. McDonald, José Miguel Andrade López, Hugo A. Urrutia, Hannah Greenfeld, Alicia Wong, Yimiao Qu, Andrew S. Petkovic, Yi Miao, K. Christopher Garcia, Michelle Monje, Daniel E. Wagner, Marianne E. Bronner, Christopher J. Lowe, and Kyle M. Loh. Two parallel lineage-committed progenitors contribute to the developing brain. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.02.662771, doi:10.1101/2025.07.02.662771. This article has 4 citations.

28. (kube2024theactivityof pages 140-145): M Kube. The activity of baf complexes ensures forebrain development and brain patterning. Unknown journal, 2024.

29. (hidalgosanchez2022anupdateon pages 1-2): Matías Hidalgo-Sánchez, Abraham Andreu-Cervera, Sergio Villa-Carballar, and Diego Echevarria. An update on the molecular mechanism of the vertebrate isthmic organizer development in the context of the neuromeric model. Frontiers in Neuroanatomy, Mar 2022. URL: https://doi.org/10.3389/fnana.2022.826976, doi:10.3389/fnana.2022.826976. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](neural_ectoderm_anteroposterior_specification-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. sears2022controllingneuralterritory pages 5-7
2. sears2022controllingneuralterritory pages 17-19
3. dundes2025twoparallellineagecommitted pages 3-5
4. hidalgosanchez2022anupdateon pages 3-4
5. hidalgosanchez2022anupdateon pages 4-5
6. hidalgosanchez2022anupdateon pages 22-23
7. martinez2001theisthmicorganizer pages 1-2
8. dworkin2013novelmechanismsthat pages 1-2
9. dundes2025twoparallellineagecommitted pages 22-23
10. lichtneckert2005insightsintothe pages 7-8
11. thawani2020buildingtheborder pages 2-3
12. kube2024theactivityof pages 140-145
13. martinduran2018convergentevolutionof pages 1-2
14. dundes2025twoparallellineagecommitted pages 7-9
15. dundes2025twoparallellineagecommitted pages 5-7
16. ghosh2018analysisofnovel pages 2-4
17. ghosh2018analysisofnovel pages 1-2
18. steinmetz2011thesegmentalpattern pages 1-2
19. steinmetz2011thesegmentalpattern pages 3-6
20. dundes2025twoparallellineagecommitted pages 9-11
21. wollesen2017brainregionalizationgenes pages 2-3
22. kelle2024captureofhuman pages 50-53
23. hidalgosanchez2022anupdateon pages 5-6
24. steinmetz2011thesegmentalpattern pages 2-3
25. dundes2025twoparallellineagecommitted pages 24-26
26. hidalgosanchez2022anupdateon pages 1-2
27. 10.1101/2025.07.02.662771
28. 10.1016/j.isci.2022.104133
29. 10.3389/fnana.2022.826976
30. 10.1038/43664
31. 10.1242/dev.128.23.4789
32. 10.1242/dev.01107
33. 10.1186/s13064-018-0112-y
34. 10.1242/dev.058727
35. 10.1111/j.1525-142X.2010.00457.x
36. 10.1038/nature25030
37. https://doi.org/10.1101/2025.07.02.662771
38. https://doi.org/10.1016/j.isci.2022.104133
39. https://doi.org/10.3389/fnana.2022.826976
40. https://doi.org/10.1038/43664
41. https://doi.org/10.1242/dev.128.23.4789
42. https://doi.org/10.1242/dev.01107
43. https://doi.org/10.1186/s13064-018-0112-y
44. https://doi.org/10.1242/dev.058727
45. https://doi.org/10.1111/j.1525-142X.2010.00457.x
46. https://doi.org/10.1038/nature25030
47. https://doi.org/10.1016/j.isci.2022.104133,
48. https://doi.org/10.1387/ijdb.11291867,
49. https://doi.org/10.1007/s00018-012-1240-x,
50. https://doi.org/10.1101/2025.07.02.662771,
51. https://doi.org/10.3389/fnana.2022.826976,
52. https://doi.org/10.1242/dev.01107,
53. https://doi.org/10.1186/s13064-018-0112-y,
54. https://doi.org/10.1242/dev.058727,
55. https://doi.org/10.1111/j.1525-142x.2010.00457.x,
56. https://doi.org/10.1038/sj.hdy.6800664,
57. https://doi.org/10.1038/s41598-017-05605-5,
58. https://doi.org/10.1038/nature25030,
59. https://doi.org/10.3389/fphys.2020.608880,
60. https://doi.org/10.1101/2024.03.26.586760,