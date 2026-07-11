---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T05:45:56.366146'
end_time: '2026-07-07T06:11:44.643330'
duration_seconds: 1548.28
template_file: templates/module_research.md.j2
template_variables:
  module_title: Oxidative phosphorylation (OXPHOS) module
  module_summary: "A taxon-neutral decomposition of oxidative phosphorylation: the\
    \ coupled process by which a respiratory electron transport chain (ETC) oxidizes\
    \ reduced cofactors and uses the released free energy to pump protons across a\
    \ coupling membrane, and an F1Fo-ATP synthase uses the resulting proton-motive\
    \ force to phosphorylate ADP. The module is deliberately phrased in terms of functional\
    \ modules, protein complexes, and pathway segments rather than a fixed gene list,\
    \ so it can represent the mitochondrial inner-membrane chain of eukaryotes and\
    \ the plasma-membrane respiratory chains of aerobic bacteria.\nDesign intent for\
    \ complexes (the central modelling question): each respiratory complex is represented\
    \ as a single PROTEIN_COMPLEX node whose emergent, complex-level catalytic activity\
    \ is carried by ONE complex-level annoton (the redox half-reaction it performs),\
    \ with its functionally important subunits exposed as `active_units` on the complex\
    \ descriptor rather than as separate per-subunit annotons. This mirrors the GO\
    \ `contributes_to` philosophy: an individual subunit contributes to but does not\
    \ independently enable the complex activity. Large, internally modular complexes\
    \ (Complex I; the F1Fo-ATP synthase) are additionally decomposed with `parts`\
    \ into their functional sub-modules (the N/Q/proton-pumping arms of Complex I;\
    \ the F1 catalytic head and Fo proton turbine of ATP synthase) \u2014 this recursive\
    \ decomposition is the payoff of the module representation over a flat subunit\
    \ list. Lineage- and chemistry-specific alternatives that bypass the proton-pumping\
    \ complexes (type-II NADH dehydrogenase, the alternative oxidase, bacterial bd-type\
    \ oxidases) are captured as `variant_sets` along explicit axes, so OXPHOS reads\
    \ as one conserved energy-conservation plan with multiple implementations. Complex\
    \ assembly/biogenesis is treated as a distinct process from chain operation and\
    \ kept as an optional sub-module."
  module_outline: "- Oxidative phosphorylation\n  - 1. respiratory electron transport\
    \ and proton pumping\n  - Respiratory electron transport chain\n    - 1. NADH:quinone\
    \ oxidoreduction (canonical, proton-pumping)\n    - Complex I (NADH:ubiquinone\
    \ oxidoreductase)\n      - NADH:ubiquinone oxidoreductase (proton-pumping) (molecular\
    \ player: NADH:ubiquinone oxidoreductase complex; activity or role: NADH:ubiquinone\
    \ oxidoreductase activity)\n      - 1. NADH oxidation (N-module)\n      - Complex\
    \ I N-module (NADH dehydrogenase)\n        - FMN-dependent NADH oxidation (molecular\
    \ player: N-module subunits (NDUFV1/NDUFV2/NDUFS1); activity or role: NADH dehydrogenase\
    \ activity)\n      - 2. ubiquinone reduction (Q-module)\n      - Complex I Q-module\
    \ (quinone reduction)\n        - Ubiquinone reduction at the Q-site (molecular\
    \ player: Q-module subunits (NDUFS2/NDUFS3/NDUFS7/NDUFS8); activity or role: ubiquinone\
    \ reduction)\n      - 3. proton translocation (P-module / membrane arm)\n    \
    \  - Complex I P-module (membrane proton-pumping arm)\n        - Redox-coupled\
    \ proton translocation (molecular player: Membrane-arm antiporter-like subunits\
    \ (ND1-ND6, ND4L; NuoH/J/K/L/M/N/A); activity or role: proton transmembrane transport)\n\
    \    - 2. succinate:quinone oxidoreduction (TCA-cycle-linked, non-pumping)\n \
    \   - Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase)\n\
    \      - Succinate:ubiquinone oxidoreductase (molecular player: succinate dehydrogenase\
    \ (ubiquinone) complex; activity or role: succinate dehydrogenase (quinone) activity)\n\
    \    - 3. auxiliary quinone-reducing dehydrogenases (additional electron entry)\n\
    \    - Auxiliary dehydrogenases feeding the quinone pool\n      - Electron-transfer-flavoprotein:ubiquinone\
    \ oxidoreductase (ETF-QO) (molecular player: electron-transferring-flavoprotein\
    \ dehydrogenase activity; activity or role: electron-transferring-flavoprotein\
    \ dehydrogenase activity)\n      - Mitochondrial glycerol-3-phosphate dehydrogenase\
    \ (FAD) (molecular player: FAD-dependent glycerol-3-phosphate dehydrogenase (GPD2\
    \ family); activity or role: glycerol-3-phosphate:quinone oxidoreductase activity)\n\
    \      - Dihydroorotate dehydrogenase (quinone) (molecular player: dihydroorotate\
    \ dehydrogenase activity; activity or role: dihydroorotate dehydrogenase (quinone)\
    \ activity)\n    - 4. mobile electron carrier (quinone pool)\n    - Quinone pool\
    \ (ubiquinone/menaquinone)\n      - Membrane quinone electron/proton carrier (molecular\
    \ player: A diffusible membrane quinone (not a protein); represented as a functional\
    \ carrier node.; activity or role: quinone-mediated electron and proton transfer)\n\
    \    - 5. quinol:cytochrome-c oxidoreduction (canonical, proton-pumping)\n   \
    \ - Complex III (cytochrome bc1 / quinol:cytochrome-c reductase)\n      - Quinol:cytochrome-c\
    \ reductase (Q-cycle) (molecular player: cytochrome bc1 complex (dimeric); activity\
    \ or role: quinol-cytochrome-c reductase activity)\n    - 6. mobile electron carrier\
    \ (soluble cytochrome)\n    - Cytochrome c (soluble carrier)\n      - Cytochrome\
    \ c electron shuttling (molecular player: cytochrome c / cytochrome c2 family;\
    \ activity or role: electron transfer activity)\n    - 7. terminal electron transfer\
    \ to dioxygen (canonical, proton-pumping)\n    - Complex IV (cytochrome c oxidase)\n\
    \      - Cytochrome c oxidase (O2 reduction) (molecular player: cytochrome c oxidase\
    \ (aa3-type); activity or role: cytochrome-c oxidase activity)\n    - 8. lineage-specific\
    \ respiratory-chain variants (bypass branches)\n    - Lineage-specific entry and\
    \ terminal-oxidase variants\n      - Alternative versions by enzyme family / energy\
    \ conservation: NADH:quinone oxidoreduction route\n        - Proton-pumping Complex\
    \ I\n          - Complex I (energy-conserving) (molecular player: respiratory\
    \ chain complex I)\n        - Type-II NADH dehydrogenase (NDH-2, non-pumping)\n\
    \          - NDH-2 NADH:quinone oxidoreductase (non-pumping) (molecular player:\
    \ type-II NADH dehydrogenase (NDH-2 / NDI1 / Ndh) family; activity or role: NADH\
    \ dehydrogenase activity (non-proton-pumping))\n      - Alternative versions by\
    \ terminal oxidase family / energy conservation: Route from the quinone pool /\
    \ cytochrome c to O2\n        - Cytochrome pathway (Complex III -> cytochrome\
    \ c -> Complex IV)\n          - bc1 / cytochrome c / aa3 oxidase route (molecular\
    \ player: cytochrome pathway terminal segment)\n        - Alternative oxidase\
    \ (AOX) ubiquinol:O2 bypass\n          - Alternative oxidase (ubiquinol:O2 oxidoreductase)\
    \ (molecular player: alternative oxidase (AOX) family; activity or role: ubiquinol:oxygen\
    \ oxidoreductase activity (non-pumping))\n        - Bacterial bd-type quinol oxidase\n\
    \          - Cytochrome bd quinol oxidase (molecular player: cytochrome bd ubiquinol\
    \ oxidase (CydAB) family; activity or role: quinol:oxygen oxidoreductase activity)\n\
    \  - 2. chemiosmotic ATP synthesis from the proton-motive force\n  - ATP synthesis\
    \ (F1Fo-ATP synthase, Complex V)\n    - Proton-motive-force-driven ATP synthesis\
    \ (rotational) (molecular player: F1Fo-ATP synthase; activity or role: proton-transporting\
    \ ATP synthase activity, rotational mechanism)\n    - 1. catalytic head (F1)\n\
    \    - F1 catalytic head\n      - Rotational ATP synthesis at F1 (molecular player:\
    \ F1 alpha/beta/gamma subunits; activity or role: proton-transporting ATP synthase\
    \ activity, rotational mechanism)\n    - 2. proton turbine (Fo)\n    - Fo proton-translocating\
    \ sector\n      - Proton-driven c-ring rotation (molecular player: Fo c-ring and\
    \ a-subunit; activity or role: proton transmembrane transport)\n    - 3. inhibition\
    \ of reverse (ATP-hydrolysis) mode\n    - IF1-mediated inhibition of ATP hydrolysis\n\
    \      - ATP synthase inhibitory factor (molecular player: ATPase inhibitory factor\
    \ 1 (ATP5IF1 / IF1) family; activity or role: ATPase inhibitor activity)\n  -\
    \ 3. supercomplex (respirasome) organization\n  - Respiratory supercomplex (respirasome)\
    \ organization\n    - Respirasome (I+III2+IV) and ATP synthase dimer organization\
    \ (molecular player: respiratory chain supercomplex / respirasome)\n  - 4. biogenesis\
    \ of the respiratory complexes (supporting context)\n  - OXPHOS complex biogenesis\
    \ (assembly factors and cofactor delivery)\n    - Respiratory-complex assembly\
    \ factors (molecular player: Examples by complex (human): Complex I \u2014 NDUFAF1-8,\
    \ ACAD9, TMEM126B, NUBPL (Fe-S); Complex II \u2014 SDHAF1-4 (Fe-S/FAD); Complex\
    \ III \u2014 BCS1L, LYRM7, TTC19; Complex IV \u2014 SURF1, SCO1/2, COX10/COX15\
    \ (heme A), COA factors; Complex V \u2014 TMEM70, ATPAF1/2.; activity or role:\
    \ respiratory-complex assembly and cofactor maturation)"
  module_connections: '- Respiratory electron transport chain precedes ATP synthesis
    (F1Fo-ATP synthase, Complex V): The electron transport chain pumps protons to
    build the proton-motive force that the ATP synthase consumes. This is energetic
    (chemiosmotic) coupling across the membrane, not a direct metabolite hand-off;
    the two are obligately coupled but can be uncoupled (e.g. by uncoupling proteins
    or protonophores).

    - Complex I (NADH:ubiquinone oxidoreductase) feeds into Quinone pool (ubiquinone/menaquinone):
    Complex I reduces ubiquinone to ubiquinol, charging the quinone pool.

    - Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase) feeds
    into Quinone pool (ubiquinone/menaquinone): Complex II reduces the quinone pool
    from succinate (TCA cycle).

    - Auxiliary dehydrogenases feeding the quinone pool feeds into Quinone pool (ubiquinone/menaquinone):
    ETF-QO, glycerol-3-phosphate dehydrogenase, and DHODH reduce the quinone pool
    from other pathways.

    - Quinone pool (ubiquinone/menaquinone) feeds into Complex III (cytochrome bc1
    / quinol:cytochrome-c reductase): Ubiquinol from the pool is the substrate oxidized
    by Complex III at the Qo site.

    - Complex III (cytochrome bc1 / quinol:cytochrome-c reductase) feeds into Cytochrome
    c (soluble carrier): Complex III reduces the soluble cytochrome c carrier.

    - Cytochrome c (soluble carrier) feeds into Complex IV (cytochrome c oxidase):
    Reduced cytochrome c donates electrons to Complex IV.

    - Quinone pool (ubiquinone/menaquinone) feeds into Lineage-specific entry and
    terminal-oxidase variants: The alternative oxidase and bacterial quinol oxidases
    draw electrons directly from the quinone pool, bypassing CIII/CIV.

    - ATP synthase inhibitory factor inhibits Proton-motive-force-driven ATP synthesis
    (rotational): IF1 inhibits the hydrolytic (reverse) mode of the ATP synthase.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 53
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: oxphos-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: oxphos-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Oxidative phosphorylation (OXPHOS) module

## Working Scope

A taxon-neutral decomposition of oxidative phosphorylation: the coupled process by which a respiratory electron transport chain (ETC) oxidizes reduced cofactors and uses the released free energy to pump protons across a coupling membrane, and an F1Fo-ATP synthase uses the resulting proton-motive force to phosphorylate ADP. The module is deliberately phrased in terms of functional modules, protein complexes, and pathway segments rather than a fixed gene list, so it can represent the mitochondrial inner-membrane chain of eukaryotes and the plasma-membrane respiratory chains of aerobic bacteria.
Design intent for complexes (the central modelling question): each respiratory complex is represented as a single PROTEIN_COMPLEX node whose emergent, complex-level catalytic activity is carried by ONE complex-level annoton (the redox half-reaction it performs), with its functionally important subunits exposed as `active_units` on the complex descriptor rather than as separate per-subunit annotons. This mirrors the GO `contributes_to` philosophy: an individual subunit contributes to but does not independently enable the complex activity. Large, internally modular complexes (Complex I; the F1Fo-ATP synthase) are additionally decomposed with `parts` into their functional sub-modules (the N/Q/proton-pumping arms of Complex I; the F1 catalytic head and Fo proton turbine of ATP synthase) — this recursive decomposition is the payoff of the module representation over a flat subunit list. Lineage- and chemistry-specific alternatives that bypass the proton-pumping complexes (type-II NADH dehydrogenase, the alternative oxidase, bacterial bd-type oxidases) are captured as `variant_sets` along explicit axes, so OXPHOS reads as one conserved energy-conservation plan with multiple implementations. Complex assembly/biogenesis is treated as a distinct process from chain operation and kept as an optional sub-module.

## Provisional Biological Outline

- Oxidative phosphorylation
  - 1. respiratory electron transport and proton pumping
  - Respiratory electron transport chain
    - 1. NADH:quinone oxidoreduction (canonical, proton-pumping)
    - Complex I (NADH:ubiquinone oxidoreductase)
      - NADH:ubiquinone oxidoreductase (proton-pumping) (molecular player: NADH:ubiquinone oxidoreductase complex; activity or role: NADH:ubiquinone oxidoreductase activity)
      - 1. NADH oxidation (N-module)
      - Complex I N-module (NADH dehydrogenase)
        - FMN-dependent NADH oxidation (molecular player: N-module subunits (NDUFV1/NDUFV2/NDUFS1); activity or role: NADH dehydrogenase activity)
      - 2. ubiquinone reduction (Q-module)
      - Complex I Q-module (quinone reduction)
        - Ubiquinone reduction at the Q-site (molecular player: Q-module subunits (NDUFS2/NDUFS3/NDUFS7/NDUFS8); activity or role: ubiquinone reduction)
      - 3. proton translocation (P-module / membrane arm)
      - Complex I P-module (membrane proton-pumping arm)
        - Redox-coupled proton translocation (molecular player: Membrane-arm antiporter-like subunits (ND1-ND6, ND4L; NuoH/J/K/L/M/N/A); activity or role: proton transmembrane transport)
    - 2. succinate:quinone oxidoreduction (TCA-cycle-linked, non-pumping)
    - Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase)
      - Succinate:ubiquinone oxidoreductase (molecular player: succinate dehydrogenase (ubiquinone) complex; activity or role: succinate dehydrogenase (quinone) activity)
    - 3. auxiliary quinone-reducing dehydrogenases (additional electron entry)
    - Auxiliary dehydrogenases feeding the quinone pool
      - Electron-transfer-flavoprotein:ubiquinone oxidoreductase (ETF-QO) (molecular player: electron-transferring-flavoprotein dehydrogenase activity; activity or role: electron-transferring-flavoprotein dehydrogenase activity)
      - Mitochondrial glycerol-3-phosphate dehydrogenase (FAD) (molecular player: FAD-dependent glycerol-3-phosphate dehydrogenase (GPD2 family); activity or role: glycerol-3-phosphate:quinone oxidoreductase activity)
      - Dihydroorotate dehydrogenase (quinone) (molecular player: dihydroorotate dehydrogenase activity; activity or role: dihydroorotate dehydrogenase (quinone) activity)
    - 4. mobile electron carrier (quinone pool)
    - Quinone pool (ubiquinone/menaquinone)
      - Membrane quinone electron/proton carrier (molecular player: A diffusible membrane quinone (not a protein); represented as a functional carrier node.; activity or role: quinone-mediated electron and proton transfer)
    - 5. quinol:cytochrome-c oxidoreduction (canonical, proton-pumping)
    - Complex III (cytochrome bc1 / quinol:cytochrome-c reductase)
      - Quinol:cytochrome-c reductase (Q-cycle) (molecular player: cytochrome bc1 complex (dimeric); activity or role: quinol-cytochrome-c reductase activity)
    - 6. mobile electron carrier (soluble cytochrome)
    - Cytochrome c (soluble carrier)
      - Cytochrome c electron shuttling (molecular player: cytochrome c / cytochrome c2 family; activity or role: electron transfer activity)
    - 7. terminal electron transfer to dioxygen (canonical, proton-pumping)
    - Complex IV (cytochrome c oxidase)
      - Cytochrome c oxidase (O2 reduction) (molecular player: cytochrome c oxidase (aa3-type); activity or role: cytochrome-c oxidase activity)
    - 8. lineage-specific respiratory-chain variants (bypass branches)
    - Lineage-specific entry and terminal-oxidase variants
      - Alternative versions by enzyme family / energy conservation: NADH:quinone oxidoreduction route
        - Proton-pumping Complex I
          - Complex I (energy-conserving) (molecular player: respiratory chain complex I)
        - Type-II NADH dehydrogenase (NDH-2, non-pumping)
          - NDH-2 NADH:quinone oxidoreductase (non-pumping) (molecular player: type-II NADH dehydrogenase (NDH-2 / NDI1 / Ndh) family; activity or role: NADH dehydrogenase activity (non-proton-pumping))
      - Alternative versions by terminal oxidase family / energy conservation: Route from the quinone pool / cytochrome c to O2
        - Cytochrome pathway (Complex III -> cytochrome c -> Complex IV)
          - bc1 / cytochrome c / aa3 oxidase route (molecular player: cytochrome pathway terminal segment)
        - Alternative oxidase (AOX) ubiquinol:O2 bypass
          - Alternative oxidase (ubiquinol:O2 oxidoreductase) (molecular player: alternative oxidase (AOX) family; activity or role: ubiquinol:oxygen oxidoreductase activity (non-pumping))
        - Bacterial bd-type quinol oxidase
          - Cytochrome bd quinol oxidase (molecular player: cytochrome bd ubiquinol oxidase (CydAB) family; activity or role: quinol:oxygen oxidoreductase activity)
  - 2. chemiosmotic ATP synthesis from the proton-motive force
  - ATP synthesis (F1Fo-ATP synthase, Complex V)
    - Proton-motive-force-driven ATP synthesis (rotational) (molecular player: F1Fo-ATP synthase; activity or role: proton-transporting ATP synthase activity, rotational mechanism)
    - 1. catalytic head (F1)
    - F1 catalytic head
      - Rotational ATP synthesis at F1 (molecular player: F1 alpha/beta/gamma subunits; activity or role: proton-transporting ATP synthase activity, rotational mechanism)
    - 2. proton turbine (Fo)
    - Fo proton-translocating sector
      - Proton-driven c-ring rotation (molecular player: Fo c-ring and a-subunit; activity or role: proton transmembrane transport)
    - 3. inhibition of reverse (ATP-hydrolysis) mode
    - IF1-mediated inhibition of ATP hydrolysis
      - ATP synthase inhibitory factor (molecular player: ATPase inhibitory factor 1 (ATP5IF1 / IF1) family; activity or role: ATPase inhibitor activity)
  - 3. supercomplex (respirasome) organization
  - Respiratory supercomplex (respirasome) organization
    - Respirasome (I+III2+IV) and ATP synthase dimer organization (molecular player: respiratory chain supercomplex / respirasome)
  - 4. biogenesis of the respiratory complexes (supporting context)
  - OXPHOS complex biogenesis (assembly factors and cofactor delivery)
    - Respiratory-complex assembly factors (molecular player: Examples by complex (human): Complex I — NDUFAF1-8, ACAD9, TMEM126B, NUBPL (Fe-S); Complex II — SDHAF1-4 (Fe-S/FAD); Complex III — BCS1L, LYRM7, TTC19; Complex IV — SURF1, SCO1/2, COX10/COX15 (heme A), COA factors; Complex V — TMEM70, ATPAF1/2.; activity or role: respiratory-complex assembly and cofactor maturation)

## Known Relationships Among Steps

- Respiratory electron transport chain precedes ATP synthesis (F1Fo-ATP synthase, Complex V): The electron transport chain pumps protons to build the proton-motive force that the ATP synthase consumes. This is energetic (chemiosmotic) coupling across the membrane, not a direct metabolite hand-off; the two are obligately coupled but can be uncoupled (e.g. by uncoupling proteins or protonophores).
- Complex I (NADH:ubiquinone oxidoreductase) feeds into Quinone pool (ubiquinone/menaquinone): Complex I reduces ubiquinone to ubiquinol, charging the quinone pool.
- Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase) feeds into Quinone pool (ubiquinone/menaquinone): Complex II reduces the quinone pool from succinate (TCA cycle).
- Auxiliary dehydrogenases feeding the quinone pool feeds into Quinone pool (ubiquinone/menaquinone): ETF-QO, glycerol-3-phosphate dehydrogenase, and DHODH reduce the quinone pool from other pathways.
- Quinone pool (ubiquinone/menaquinone) feeds into Complex III (cytochrome bc1 / quinol:cytochrome-c reductase): Ubiquinol from the pool is the substrate oxidized by Complex III at the Qo site.
- Complex III (cytochrome bc1 / quinol:cytochrome-c reductase) feeds into Cytochrome c (soluble carrier): Complex III reduces the soluble cytochrome c carrier.
- Cytochrome c (soluble carrier) feeds into Complex IV (cytochrome c oxidase): Reduced cytochrome c donates electrons to Complex IV.
- Quinone pool (ubiquinone/menaquinone) feeds into Lineage-specific entry and terminal-oxidase variants: The alternative oxidase and bacterial quinol oxidases draw electrons directly from the quinone pool, bypassing CIII/CIV.
- ATP synthase inhibitory factor inhibits Proton-motive-force-driven ATP synthesis (rotational): IF1 inhibits the hydrolytic (reverse) mode of the ATP synthase.

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

Oxidative phosphorylation (OXPHOS) module

## Working Scope

A taxon-neutral decomposition of oxidative phosphorylation: the coupled process by which a respiratory electron transport chain (ETC) oxidizes reduced cofactors and uses the released free energy to pump protons across a coupling membrane, and an F1Fo-ATP synthase uses the resulting proton-motive force to phosphorylate ADP. The module is deliberately phrased in terms of functional modules, protein complexes, and pathway segments rather than a fixed gene list, so it can represent the mitochondrial inner-membrane chain of eukaryotes and the plasma-membrane respiratory chains of aerobic bacteria.
Design intent for complexes (the central modelling question): each respiratory complex is represented as a single PROTEIN_COMPLEX node whose emergent, complex-level catalytic activity is carried by ONE complex-level annoton (the redox half-reaction it performs), with its functionally important subunits exposed as `active_units` on the complex descriptor rather than as separate per-subunit annotons. This mirrors the GO `contributes_to` philosophy: an individual subunit contributes to but does not independently enable the complex activity. Large, internally modular complexes (Complex I; the F1Fo-ATP synthase) are additionally decomposed with `parts` into their functional sub-modules (the N/Q/proton-pumping arms of Complex I; the F1 catalytic head and Fo proton turbine of ATP synthase) — this recursive decomposition is the payoff of the module representation over a flat subunit list. Lineage- and chemistry-specific alternatives that bypass the proton-pumping complexes (type-II NADH dehydrogenase, the alternative oxidase, bacterial bd-type oxidases) are captured as `variant_sets` along explicit axes, so OXPHOS reads as one conserved energy-conservation plan with multiple implementations. Complex assembly/biogenesis is treated as a distinct process from chain operation and kept as an optional sub-module.

## Provisional Biological Outline

- Oxidative phosphorylation
  - 1. respiratory electron transport and proton pumping
  - Respiratory electron transport chain
    - 1. NADH:quinone oxidoreduction (canonical, proton-pumping)
    - Complex I (NADH:ubiquinone oxidoreductase)
      - NADH:ubiquinone oxidoreductase (proton-pumping) (molecular player: NADH:ubiquinone oxidoreductase complex; activity or role: NADH:ubiquinone oxidoreductase activity)
      - 1. NADH oxidation (N-module)
      - Complex I N-module (NADH dehydrogenase)
        - FMN-dependent NADH oxidation (molecular player: N-module subunits (NDUFV1/NDUFV2/NDUFS1); activity or role: NADH dehydrogenase activity)
      - 2. ubiquinone reduction (Q-module)
      - Complex I Q-module (quinone reduction)
        - Ubiquinone reduction at the Q-site (molecular player: Q-module subunits (NDUFS2/NDUFS3/NDUFS7/NDUFS8); activity or role: ubiquinone reduction)
      - 3. proton translocation (P-module / membrane arm)
      - Complex I P-module (membrane proton-pumping arm)
        - Redox-coupled proton translocation (molecular player: Membrane-arm antiporter-like subunits (ND1-ND6, ND4L; NuoH/J/K/L/M/N/A); activity or role: proton transmembrane transport)
    - 2. succinate:quinone oxidoreduction (TCA-cycle-linked, non-pumping)
    - Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase)
      - Succinate:ubiquinone oxidoreductase (molecular player: succinate dehydrogenase (ubiquinone) complex; activity or role: succinate dehydrogenase (quinone) activity)
    - 3. auxiliary quinone-reducing dehydrogenases (additional electron entry)
    - Auxiliary dehydrogenases feeding the quinone pool
      - Electron-transfer-flavoprotein:ubiquinone oxidoreductase (ETF-QO) (molecular player: electron-transferring-flavoprotein dehydrogenase activity; activity or role: electron-transferring-flavoprotein dehydrogenase activity)
      - Mitochondrial glycerol-3-phosphate dehydrogenase (FAD) (molecular player: FAD-dependent glycerol-3-phosphate dehydrogenase (GPD2 family); activity or role: glycerol-3-phosphate:quinone oxidoreductase activity)
      - Dihydroorotate dehydrogenase (quinone) (molecular player: dihydroorotate dehydrogenase activity; activity or role: dihydroorotate dehydrogenase (quinone) activity)
    - 4. mobile electron carrier (quinone pool)
    - Quinone pool (ubiquinone/menaquinone)
      - Membrane quinone electron/proton carrier (molecular player: A diffusible membrane quinone (not a protein); represented as a functional carrier node.; activity or role: quinone-mediated electron and proton transfer)
    - 5. quinol:cytochrome-c oxidoreduction (canonical, proton-pumping)
    - Complex III (cytochrome bc1 / quinol:cytochrome-c reductase)
      - Quinol:cytochrome-c reductase (Q-cycle) (molecular player: cytochrome bc1 complex (dimeric); activity or role: quinol-cytochrome-c reductase activity)
    - 6. mobile electron carrier (soluble cytochrome)
    - Cytochrome c (soluble carrier)
      - Cytochrome c electron shuttling (molecular player: cytochrome c / cytochrome c2 family; activity or role: electron transfer activity)
    - 7. terminal electron transfer to dioxygen (canonical, proton-pumping)
    - Complex IV (cytochrome c oxidase)
      - Cytochrome c oxidase (O2 reduction) (molecular player: cytochrome c oxidase (aa3-type); activity or role: cytochrome-c oxidase activity)
    - 8. lineage-specific respiratory-chain variants (bypass branches)
    - Lineage-specific entry and terminal-oxidase variants
      - Alternative versions by enzyme family / energy conservation: NADH:quinone oxidoreduction route
        - Proton-pumping Complex I
          - Complex I (energy-conserving) (molecular player: respiratory chain complex I)
        - Type-II NADH dehydrogenase (NDH-2, non-pumping)
          - NDH-2 NADH:quinone oxidoreductase (non-pumping) (molecular player: type-II NADH dehydrogenase (NDH-2 / NDI1 / Ndh) family; activity or role: NADH dehydrogenase activity (non-proton-pumping))
      - Alternative versions by terminal oxidase family / energy conservation: Route from the quinone pool / cytochrome c to O2
        - Cytochrome pathway (Complex III -> cytochrome c -> Complex IV)
          - bc1 / cytochrome c / aa3 oxidase route (molecular player: cytochrome pathway terminal segment)
        - Alternative oxidase (AOX) ubiquinol:O2 bypass
          - Alternative oxidase (ubiquinol:O2 oxidoreductase) (molecular player: alternative oxidase (AOX) family; activity or role: ubiquinol:oxygen oxidoreductase activity (non-pumping))
        - Bacterial bd-type quinol oxidase
          - Cytochrome bd quinol oxidase (molecular player: cytochrome bd ubiquinol oxidase (CydAB) family; activity or role: quinol:oxygen oxidoreductase activity)
  - 2. chemiosmotic ATP synthesis from the proton-motive force
  - ATP synthesis (F1Fo-ATP synthase, Complex V)
    - Proton-motive-force-driven ATP synthesis (rotational) (molecular player: F1Fo-ATP synthase; activity or role: proton-transporting ATP synthase activity, rotational mechanism)
    - 1. catalytic head (F1)
    - F1 catalytic head
      - Rotational ATP synthesis at F1 (molecular player: F1 alpha/beta/gamma subunits; activity or role: proton-transporting ATP synthase activity, rotational mechanism)
    - 2. proton turbine (Fo)
    - Fo proton-translocating sector
      - Proton-driven c-ring rotation (molecular player: Fo c-ring and a-subunit; activity or role: proton transmembrane transport)
    - 3. inhibition of reverse (ATP-hydrolysis) mode
    - IF1-mediated inhibition of ATP hydrolysis
      - ATP synthase inhibitory factor (molecular player: ATPase inhibitory factor 1 (ATP5IF1 / IF1) family; activity or role: ATPase inhibitor activity)
  - 3. supercomplex (respirasome) organization
  - Respiratory supercomplex (respirasome) organization
    - Respirasome (I+III2+IV) and ATP synthase dimer organization (molecular player: respiratory chain supercomplex / respirasome)
  - 4. biogenesis of the respiratory complexes (supporting context)
  - OXPHOS complex biogenesis (assembly factors and cofactor delivery)
    - Respiratory-complex assembly factors (molecular player: Examples by complex (human): Complex I — NDUFAF1-8, ACAD9, TMEM126B, NUBPL (Fe-S); Complex II — SDHAF1-4 (Fe-S/FAD); Complex III — BCS1L, LYRM7, TTC19; Complex IV — SURF1, SCO1/2, COX10/COX15 (heme A), COA factors; Complex V — TMEM70, ATPAF1/2.; activity or role: respiratory-complex assembly and cofactor maturation)

## Known Relationships Among Steps

- Respiratory electron transport chain precedes ATP synthesis (F1Fo-ATP synthase, Complex V): The electron transport chain pumps protons to build the proton-motive force that the ATP synthase consumes. This is energetic (chemiosmotic) coupling across the membrane, not a direct metabolite hand-off; the two are obligately coupled but can be uncoupled (e.g. by uncoupling proteins or protonophores).
- Complex I (NADH:ubiquinone oxidoreductase) feeds into Quinone pool (ubiquinone/menaquinone): Complex I reduces ubiquinone to ubiquinol, charging the quinone pool.
- Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase) feeds into Quinone pool (ubiquinone/menaquinone): Complex II reduces the quinone pool from succinate (TCA cycle).
- Auxiliary dehydrogenases feeding the quinone pool feeds into Quinone pool (ubiquinone/menaquinone): ETF-QO, glycerol-3-phosphate dehydrogenase, and DHODH reduce the quinone pool from other pathways.
- Quinone pool (ubiquinone/menaquinone) feeds into Complex III (cytochrome bc1 / quinol:cytochrome-c reductase): Ubiquinol from the pool is the substrate oxidized by Complex III at the Qo site.
- Complex III (cytochrome bc1 / quinol:cytochrome-c reductase) feeds into Cytochrome c (soluble carrier): Complex III reduces the soluble cytochrome c carrier.
- Cytochrome c (soluble carrier) feeds into Complex IV (cytochrome c oxidase): Reduced cytochrome c donates electrons to Complex IV.
- Quinone pool (ubiquinone/menaquinone) feeds into Lineage-specific entry and terminal-oxidase variants: The alternative oxidase and bacterial quinol oxidases draw electrons directly from the quinone pool, bypassing CIII/CIV.
- ATP synthase inhibitory factor inhibits Proton-motive-force-driven ATP synthesis (rotational): IF1 inhibits the hydrolytic (reverse) mode of the ATP synthase.

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

# Oxidative Phosphorylation: A Module-Oriented Review of the Conserved Chemiosmotic Energy-Conservation System

## 1. Executive Summary

Oxidative phosphorylation (OXPHOS) is the coupled process by which a respiratory electron transport chain (ETC) oxidizes reduced cofactors (NADH, FADH₂, quinol) and uses the released free energy to pump protons across a coupling membrane, establishing a proton-motive force (pmf) that an F₁Fo-ATP synthase then consumes to phosphorylate ADP (nesci2021molecularandsupramolecular pages 4-5, goldman2023electrontransportchains pages 2-4). This review treats OXPHOS as one conserved energy-conservation plan with multiple molecular implementations, deliberately framed in terms of functional modules and protein complexes rather than a fixed gene list, so that it applies equally to the mitochondrial inner-membrane chain of eukaryotes and the plasma-membrane respiratory chains of aerobic bacteria. Recent cryo-EM breakthroughs have resolved individual complexes, supercomplexes, and even in situ respirasome architectures at near-atomic resolution, reshaping our understanding of coupling mechanisms, complex assembly, and the functional significance of higher-order organization. Nonetheless, fundamental questions persist—notably the precise coupling mechanism of Complex I, the functional versus structural role of respiratory supercomplexes, and the molecular logic of "unidirectional" catalysis in certain F₁Fo-ATP synthases.

## 2. Definition and Biological Boundaries

**Scope.** OXPHOS encompasses two functionally coupled subsystems: (i) the respiratory electron transport chain (Complexes I–IV and mobile carriers) that pumps protons across the coupling membrane, and (ii) the F₁Fo-ATP synthase (Complex V) that harvests the resulting pmf (nesci2021molecularandsupramolecular pages 4-5). The system is bounded by the coupling membrane—the mitochondrial inner membrane in eukaryotes or the cytoplasmic membrane in bacteria—and requires both reduced cofactors as input and molecular oxygen (in aerobic respiration) as the terminal electron acceptor.

**What is excluded.** The TCA cycle, fatty acid β-oxidation, and amino acid catabolism generate the NADH and FADH₂ consumed by the chain but are upstream processes. Mitochondrial protein import, mitochondrial DNA replication and transcription, and cristae membrane dynamics are adjacent processes that support OXPHOS but do not constitute chain operation per se. Complex biogenesis and assembly factor function are treated here as a distinct supporting module.

**Competing definitions.** In some textbooks, "oxidative phosphorylation" is used loosely to refer only to ATP synthesis driven by pmf, excluding the electron transport that generates it. The broader and more mechanistically accurate definition—coupling of respiration and phosphorylation via chemiosmosis—is adopted here, consistent with IUBMB nomenclature and the original Mitchell formulation (goldman2023electrontransportchains pages 2-4).

## 3. Mechanistic Overview

### 3.1. Electron Entry and the Quinone Pool

Electrons enter the chain at multiple points, all converging on a common lipid-soluble quinone pool (ubiquinone in most eukaryotes; menaquinone or ubiquinone in bacteria). The canonical NADH-linked entry is through Complex I, which couples NADH oxidation and ubiquinone reduction to the translocation of 4 H⁺ per NADH across the membrane (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14). Succinate-linked entry via Complex II (succinate:quinone oxidoreductase) reduces the quinone pool without proton pumping (kao2022quinonebindingsites pages 1-3). Additional auxiliary dehydrogenases—ETF:quinone oxidoreductase (from fatty acid β-oxidation), mitochondrial glycerol-3-phosphate dehydrogenase, and dihydroorotate dehydrogenase—also feed electrons into the quinone pool from diverse metabolic sources.

### 3.2. Complex I: Modular Coupling of Redox and Ion Translocation

Complex I (NADH:ubiquinone oxidoreductase) is the largest respiratory complex, comprising ~45 subunits in mammals organized into three functional modules (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4):

- **N-module (NADH dehydrogenase):** Contains FMN and the initial Fe-S clusters (N3, N1a, N1b). NADH is oxidized at the FMN site, and electrons enter the Fe-S relay chain (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9).
- **Q-module (quinone reduction):** Houses the terminal Fe-S cluster N2 (~−140 mV, pH-dependent) and the ubiquinone-binding chamber formed by subunits Nqo4, Nqo6, and Nqo8. Ubiquinone binds approximately 12 Å from N2 and is reduced in a concerted two-electron, two-proton process, though the exact mechanism remains unknown (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 9-11, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9).
- **P-module (proton-pumping membrane arm):** Contains the antiporter-like subunits ND2, ND4, and ND5, which are homologous to bacterial cation/H⁺ antiporters. The Q-binding center transitions between "closed" (catalytically competent) and "open" (deactive) conformations, and this conformational reorganization is proposed to drive long-range proton translocation through the membrane arm (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13). Recent structural and molecular dynamics studies suggest that ND5 may possess the only fully hydrated channel capable of functioning as a proper proton transporter, raising the possibility that all four protons are translocated through a single coordinated pathway (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13). An E-channel provides a Grotthus-competent proton-transfer pathway from the Q-binding center to the central axis of the membrane arm (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14). However, these coupling models remain hypothetical, and their experimental verification remains a central challenge (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14).

### 3.3. Complex II: The Non-Pumping TCA Cycle Interface

Complex II (succinate dehydrogenase) is unique among OXPHOS complexes: it participates in both the TCA cycle and the ETC, oxidizing succinate to fumarate while reducing quinone. It contains FAD, three Fe-S clusters, and (in mammals) a heme b, organized into a matrix-facing catalytic arm (SDHA/SDHB) and a membrane anchor (SDHC/SDHD) (kao2022quinonebindingsites pages 1-3). Crucially, Complex II does not translocate protons, so electrons entering through succinate contribute less to the pmf than those entering through NADH.

### 3.4. Complex III: The Q-Cycle

Complex III (cytochrome bc₁) operates as an obligate dimer (CIII₂) and accomplishes proton translocation through the Mitchellian Q-cycle mechanism (kao2022quinonebindingsites pages 3-4, kao2022quinonebindingsites pages 1-3). At the Qo (quinol oxidation) site near the positive (P) side of the membrane, ubiquinol is oxidized in a bifurcated reaction: one electron is transferred through the Rieske [2Fe-2S] cluster to cytochrome c₁ and thence to soluble cytochrome c, while the second electron is routed through heme bL and heme bH to reduce quinone at the Qi (quinone reduction) site on the N-side (kao2022quinonebindingsites pages 3-4). This bifurcated electron transfer is essential: two Qo-site turnovers are required to fully reduce one quinone at Qi, with the net result that four protons are released to the P-side and two are consumed from the N-side per pair of electrons delivered to cytochrome c (kao2022quinonebindingsites pages 3-4). The reactive semiquinone intermediate at the Qo site must be tightly controlled to prevent short-circuit reactions and harmful ROS generation (kao2022quinonebindingsites pages 3-4).

### 3.5. Cytochrome c and Complex IV

Soluble cytochrome c shuttles electrons from Complex III to Complex IV (cytochrome c oxidase, aa₃-type), which catalyzes the four-electron reduction of O₂ to 2H₂O. Complex IV is a proton pump: approximately two protons are translocated per electron pair, with additional "chemical" protons consumed from the matrix in water formation, yielding an effective stoichiometry of ~4 H⁺ moved across the membrane per O₂ reduced (nesci2021molecularandsupramolecular pages 4-5).

### 3.6. ATP Synthesis by the F₁Fo-ATP Synthase

The F₁Fo-ATP synthase (Complex V) is a rotary molecular machine composed of two coupled motors (frasch2022f1foatpsynthase pages 1-2, zharova2023f1·foatpsynthaseatpase pages 2-4):

- **Fo sector (proton turbine):** Contains the membrane-embedded c-ring and the stator a-subunit. Proton flow through half-channels in subunit-a drives clockwise rotation of the c-ring. The c-ring stoichiometry is species-specific, ranging from 8 (mammals) to 17 subunits, and directly determines the bioenergetic cost of ATP synthesis (zharova2023f1·foatpsynthaseatpase pages 2-4, nesci2021molecularandsupramolecular pages 17-19).
- **F₁ sector (catalytic head):** An (αβ)₃ hexamer surrounding the γ-subunit central stalk. Rotation of γ drives sequential conformational changes at three catalytic sites according to the binding-change mechanism, with each 360° rotation producing three ATP molecules (frasch2022f1foatpsynthase pages 1-2, nesci2021molecularandsupramolecular pages 17-19). Single-molecule studies revealed that each 120° power stroke consists of sub-steps—an 80° binding dwell (ATP binding) and a 40° catalytic dwell (hydrolysis/product release), with angular velocities that vary with rotational position (frasch2022f1foatpsynthase pages 1-2).

In E. coli, the c₁₀-ring rotates 36° per c-subunit, with each 36° step comprising an 11° proton-translocation-dependent rotation followed by a 25° electrostatic-driven rotation, consistent with a Grotthuss mechanism for proton transfer through the a/c interface (frasch2022f1foatpsynthase pages 1-2).

**IF₁-mediated inhibition.** The 10 kDa inhibitory factor IF₁ acts as a molecular ratchet: at acidic pH, IF₁ dimers bind to the F₁ catalytic interface between α and β subunits, and following ATP-driven γ rotation, the N-terminal domain of IF₁ transitions to an ordered α-helical structure that mechanically blocks further counterclockwise (hydrolytic) rotation while still permitting clockwise (synthetic) rotation (zharova2023f1·foatpsynthaseatpase pages 5-6). This ratchet-and-pawl mechanism prevents wasteful ATP hydrolysis when the pmf collapses, for example during ischemia.

The following table summarizes the core OXPHOS complexes with their modular organization, proton stoichiometry, and key cofactors:

| Complex name | Subunit count (mammalian) | Functional modules / submodules | Core catalytic activity | H+ translocated per turnover | Key cofactors | GO activity annotation |
|---|---:|---|---|---|---|---|
| Complex I (NADH:ubiquinone oxidoreductase) | ~45 | N-module (FMN-dependent NADH oxidation); Q-module (ubiquinone reduction at Q-site); P-module / membrane arm (antiporter-like proton-translocating subunits) | NADH + Q + 5H+<sub>matrix</sub> -> NAD+ + QH2 + 4H+<sub>IMS/periplasm</sub>; couples NADH oxidation and quinone reduction to long-range proton translocation | 4 H+ per NADH oxidized | FMN; 8-9 Fe-S clusters including terminal N2; bound quinone at Q-site (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 9-11, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14) | NADH dehydrogenase (ubiquinone) activity |
| Complex II (succinate dehydrogenase / succinate:quinone oxidoreductase) | 4 canonical core subunits | Matrix catalytic arm (SDHA/SDHB); membrane anchor / quinone-reduction arm (SDHC/SDHD) | Succinate oxidation to fumarate with electron transfer to quinone; feeds electrons into quinone pool but is not a proton pump | 0 H+ pumped | FAD; 3 Fe-S clusters; heme b (in mammalian CII) (kao2022quinonebindingsites pages 1-3) | succinate dehydrogenase (quinone) activity |
| Complex III (cytochrome bc1 / ubiquinol:cytochrome c oxidoreductase) | 11 per monomer; functional complex is a dimer (CIII2) | Qo site branch (quinol oxidation); Rieske ISP -> cytochrome c1 branch; bL/bH -> Qi site branch; Q-cycle chemistry | Oxidizes QH2 at Qo, transfers one electron to cytochrome c via Rieske Fe-S/c1 and one to quinone at Qi via bL/bH; bifurcated electron flow underlies Q-cycle | ~4 H+ translocated per 2 electrons delivered to 2 cytochrome c (equivalently per full Q-cycle / 2 QH2 oxidized: 4 H+ released to P side and 2 H+ taken up from N side) | Rieske 2Fe-2S center; hemes bL, bH, c1; quinone/quinol at Qo and Qi sites (kao2022quinonebindingsites pages 3-4, kao2022quinonebindingsites pages 1-3) | ubiquinol-cytochrome-c reductase activity |
| Complex IV (cytochrome c oxidase, aa3-type) | 14 | Catalytic core (MT-CO1/2/3); proton uptake pathways and oxygen-reduction center | Receives electrons from cytochrome c and reduces O2 to H2O; couples redox chemistry to vectorial proton translocation | ~4 H+ per O2 reduced / 4 e- total; equivalently ~2 H+ pumped per 2 e- and 2 additional matrix H+ consumed chemically to form water | Heme a; heme a3; CuA; CuB (nesci2021molecularandsupramolecular pages 4-5, kohler2023thefunctionalsignificance pages 2-3, bennett2022mechanismsofmitochondrial pages 11-12) | cytochrome-c oxidase activity |
| Complex V (F1Fo-ATP synthase) | ~29 protein subunits in mammals | F1 catalytic head ((alpha beta)3 with gamma/delta/epsilon central stalk); Fo proton turbine (a-subunit + c-ring); peripheral stalk; IF1-regulated reverse mode | Uses proton-motive force to drive c-ring and gamma rotation, enforcing binding-change catalysis in F1 to synthesize ATP from ADP + Pi | Consumes pmf rather than pumping in forward mode; H+/ATP depends on c-ring stoichiometry (mammalian c8 ring -> ~8 H+ per 3 ATP at rotor level, plus transport costs) | Bound nucleotides (ATP/ADP); Mg2+ at catalytic sites; c-ring carboxylates as proton carriers (frasch2022f1foatpsynthase pages 1-2, zharova2023f1·foatpsynthaseatpase pages 2-4, zharova2023f1·foatpsynthaseatpase pages 5-6, nesci2021molecularandsupramolecular pages 17-19) | proton-transporting ATP synthase activity, rotational mechanism |


*Table: This table summarizes the five core oxidative phosphorylation complexes in a module-oriented way, including their mammalian composition, catalytic roles, proton-coupling properties, cofactors, and corresponding GO-style activities. It is useful as a compact reference linking mechanistic decomposition to functional annotation.*

## 4. Major Molecular Players and Active Assemblies

### 4.1. The Quinone Pool as a Hub

The quinone pool is the central electron-distribution hub. Ubiquinone (in most eukaryotes and many bacteria) or menaquinone (in many bacteria and some archaea) serves as a mobile, lipid-soluble two-electron/two-proton carrier that equilibrates in the membrane between the reducing enzymes (Complexes I, II, and auxiliary dehydrogenases) and the oxidizing enzyme (Complex III, or alternative oxidases in branched chains) (kao2022quinonebindingsites pages 1-3). The pool size and redox state are sensed by the cell as indicators of respiratory capacity and metabolic status.

### 4.2. Auxiliary Quinone-Reducing Dehydrogenases

Beyond Complex I and II, several dehydrogenases feed electrons into the quinone pool: electron-transfer-flavoprotein:ubiquinone oxidoreductase (ETF-QO, linking fatty acid β-oxidation and amino acid catabolism), mitochondrial glycerol-3-phosphate dehydrogenase (connecting cytoplasmic NADH to mitochondrial respiration via a shuttle), and dihydroorotate dehydrogenase (from pyrimidine biosynthesis). None of these pump protons; their energetic contribution to the pmf depends entirely on the downstream proton-pumping complexes.

### 4.3. Supercomplex Organization

Respiratory complexes do not exist solely as free entities in the inner membrane but assemble into supercomplexes (SCs). The best-characterized is the respirasome (CI + CIII₂ + CIV), a ~1.7 MDa assembly that accounts for roughly half of Complex I in human cells (kohler2023thefunctionalsignificance pages 2-3). In situ cryo-EM of porcine mitochondria identified four main SC organizations: I₁III₂IV₁, I₁III₂IV₂, I₂III₂IV₂, and I₂III₄IV₂, potentially expanding into higher-order arrays on the inner membrane, largely formed by "protein-lipid-protein" interactions that significantly impact local membrane geometry (nakano2026structuresofrespiratory pages 1-4). Even larger megacomplexes (CI₁CIII₂CIV₃, CI₂CIII₂CIV₆) have been observed (nakano2026structuresofrespiratory pages 1-4). The interaction surfaces involve eukaryotic-origin supernumerary subunits (e.g., NDUFA11, NDUFB4, NDUFB9 on CI; UQCRB, UQCRQ on CIII), distinguishing them from bacterial complexes (kohler2023thefunctionalsignificance pages 2-3).

ATP synthase dimers adopt V-shaped architectures that generate positive membrane curvature at cristae tips, with tetrameric assemblies (two FoF1-IF₁ dimers) also present (nakano2026structuresofrespiratory pages 1-4). This links OXPHOS complex organization to cristae morphology and membrane dynamics (bennett2022mechanismsofmitochondrial pages 12-14).

A remarkable recent discovery in Trypanosoma brucei revealed a bona fide ETC-ATP synthase supercomplex (CII-CIV₂-CV) incorporating both respiratory chain and ATP synthase components, bridged by non-canonical subunit-g paralogs. Genetic disruption of this assembly triggered pronounced cristae remodeling from discoidal to tubular form, with relatively modest effects on steady-state ATP output, suggesting a primary role in architectural quality control rather than simple catalytic enhancement.

## 5. Evolutionary and Cell-Biological Variation

### 5.1. Deep Evolutionary Roots

Chemiosmotic coupling is among the most ancient and conserved energy-conservation strategies in biology. Phylogenetic evidence indicates that ATP synthase ancestors were present at least by the time of the Last Universal Common Ancestor (LUCA), and that diverse ETC components share evolutionarily homologous features across bacteria, archaea, and eukaryotes despite enormous diversity in substrate usage and terminal electron acceptors (goldman2023electrontransportchains pages 2-4). Bacterial ETCs show far greater diversity than the mitochondrial chain, with alternative terminal electron acceptors including sulfate, iron oxides, nitrate, and manganese oxides (goldman2023electrontransportchains pages 2-4). The mitochondrial OXPHOS system arose through the endosymbiotic merger of an archaeal host with an alpha-proteobacterial ancestor, with subsequent massive gene transfer to the nuclear genome (allison2024theoreticalandempirical pages 11-15). Key O₂-dependent enzymes for cofactor biosynthesis (including ubiquinone, heme, and NAD⁺ synthesis) evolved before the full aerobic respiratory chain, providing the biochemical prerequisites for aerobic respiration (mrnjavac2024theradicalimpact pages 20-22).

### 5.2. Lineage-Specific Variants and Bypass Pathways

A defining feature of OXPHOS is that the conserved chemiosmotic logic admits multiple molecular implementations. Several lineage-specific enzymes bypass proton-pumping complexes, trading energy conservation for metabolic flexibility:

| Enzyme variant | Replaces / bypasses | Proton pumping? | Distribution (lineages) | Energy conservation impact | Known physiological role | Key structural features |
|---|---|---|---|---|---|---|
| Type-II NADH dehydrogenase (NDH-2) | Alternative entry enzyme replacing proton-pumping Complex I for NADH:quinone oxidoreduction | No | Bacteria; also present in plants, fungi, and diverse protists (li2024alternativeoxidasefrom pages 1-3) | Lowers ATP yield relative to Complex I because NADH oxidation is uncoupled from H+ translocation; still feeds electrons into the quinone pool (li2024alternativeoxidasefrom pages 1-3) | Maintains NADH reoxidation and respiratory flux when Complex I is absent, reduced, or replaced by simpler chains; supports flexible respiratory architectures in microbial and eukaryotic lineages (li2024alternativeoxidasefrom pages 1-3, goldman2023electrontransportchains pages 2-4) | Typically a single-subunit, FAD-containing NADH:quinone oxidoreductase; lacks the long membrane antiporter arm and multisubunit proton-pumping machinery of Complex I (li2024alternativeoxidasefrom pages 1-3, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4) |
| Alternative oxidase (AOX) | Bypasses Complexes III and IV by oxidizing quinol directly with O2 as terminal acceptor | No | Plants, fungi, protists, some animals, and some bacteria (li2024alternativeoxidasefrom pages 1-3, li2024alternativeoxidasefrom pages 7-8) | Decreases energy conservation because electrons bypass proton-translocating CIII/CIV; often dissipates energy as heat rather than maximizing ATP production (li2024alternativeoxidasefrom pages 6-7, li2024alternativeoxidasefrom pages 7-8) | Limits over-reduction of the ETC, suppresses ROS formation, preserves carbon metabolism and redox balance during stress or cytochrome-pathway inhibition; important in plant stress physiology and pathogen survival (li2024alternativeoxidasefrom pages 1-3, li2024alternativeoxidasefrom pages 6-7, li2024alternativeoxidasefrom pages 7-8) | Membrane-associated non-heme diiron oxidase that oxidizes ubiquinol and reduces O2 to H2O; cyanide- and antimycin-resistant terminal oxidase of the alternative pathway (li2024alternativeoxidasefrom pages 1-3) |
| Cytochrome bd oxidase | Bacterial terminal quinol oxidase that bypasses the cytochrome bc1/cytochrome c/aa3 oxidase route | No active proton pumping; generates pmf by scalar / vector chemistry and proton transfer linked to quinol oxidation and O2 reduction | Bacteria (and broadly prokaryotic lineages in some reviews), absent from human mitochondria; especially important under microaerobic or stress conditions (nastasi2024membraneboundredoxenzyme pages 1-2, sorescu2025breakthroughsinthe pages 11-12) | Conserves less energy than heme-copper proton-pumping oxidases, but still contributes to pmf and ATP synthesis; favors survival under low O2 or toxic stress over maximal ATP efficiency (borisov2023cytochromebdas pages 1-3, nastasi2024membraneboundredoxenzyme pages 1-2) | High-affinity terminal oxidase for microaerobic respiration; supports growth under low oxygen, cyanide or carbon monoxide exposure, and oxidative/nitrosative stress; contributes to virulence in pathogens (borisov2023cytochromebdas pages 1-3, nastasi2024membraneboundredoxenzyme pages 1-2, sorescu2025breakthroughsinthe pages 11-12) | Core CydA/CydB pseudosymmetrical heterodimer; quinol-oxidizing Q-loop; three hemes in CydA—b558, b595, and d—arranged in a triangular geometry; proton- and oxygen-conducting channels resolved structurally (borisov2023cytochromebdas pages 1-3, grund2023thecryoemstructure pages 1-2, friedrich2022recentadvancesin pages 8-9, friedrich2022recentadvancesin pages 2-4) |
| Na+-NQR (sodium-pumping NADH:quinone oxidoreductase) | Bacterial alternative to Complex I for NADH:quinone oxidoreduction | Pumps Na+ rather than H+ | Bacteria, including Vibrio and other marine/pathogenic lineages (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9, goldman2023electrontransportchains pages 2-4) | Conserves energy as a sodium-motive force rather than a proton-motive force; can power ATP synthesis and transport indirectly in Na+-coupled bioenergetic systems (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9, goldman2023electrontransportchains pages 2-4) | Supports respiration in organisms using sodium-based bioenergetics; adapts electron transport to ecological niches where Na+ cycling is advantageous (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9, goldman2023electrontransportchains pages 2-4) | Six-subunit enzyme (NqrA-F) with multiple cofactors; undergoes redox-coupled conformational changes, including an electron-transfer switch centered on NqrC and an intramembranous [2Fe-2S] cluster that helps control Na+ release from NqrB (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9) |


*Table: This table summarizes major lineage-specific alternatives to the canonical OXPHOS chain, emphasizing what each variant replaces, whether it pumps ions, and the trade-off between respiratory flexibility and ATP yield. It is useful for comparing conserved chemiosmotic logic with divergent molecular implementations across taxa.*

**Type-II NADH dehydrogenase (NDH-2)** is a single-subunit, FAD-containing enzyme that catalyzes NADH:quinone oxidoreduction without proton pumping, serving as an alternative to the massive Complex I in bacteria, plants, fungi, and protists (li2024alternativeoxidasefrom pages 1-3). By uncoupling NADH oxidation from H⁺ translocation, NDH-2 maintains respiratory flux under conditions where maximal ATP yield is not required or when Complex I is absent.

**Alternative oxidase (AOX)** is a membrane-associated non-heme diiron protein that oxidizes ubiquinol and reduces O₂ directly to water, bypassing both Complex III and Complex IV without proton pumping (li2024alternativeoxidasefrom pages 1-3, li2024alternativeoxidasefrom pages 6-7). AOX is widespread in plants (where it plays critical roles in stress tolerance, thermogenesis, and ROS suppression), fungi, protists (notably in trypanosomes, where it is essential for bloodstream-form viability), and even some bacteria (li2024alternativeoxidasefrom pages 7-8). In plants, AOX comprises two subfamilies: AOX1 (stress-responsive) and AOX2 (developmentally regulated) (li2024alternativeoxidasefrom pages 7-8). AOX confers respiratory flexibility by decoupling carbon metabolism from ATP turnover, allowing continued electron flow when the cytochrome pathway is inhibited or over-reduced (li2024alternativeoxidasefrom pages 6-7).

**Cytochrome bd oxidase** is a bacterial quinol:O₂ oxidoreductase that operates as a terminal oxidase using three hemes (b558, b595, and d) arranged in a triangular geometry within the CydA/CydB heterodimer (grund2023thecryoemstructure pages 1-2, friedrich2022recentadvancesin pages 2-4). Unlike heme-copper oxidases, cytochrome bd does not pump protons actively but generates pmf through vectorial chemistry—proton uptake from the cytoplasm and quinol oxidation at the periplasmic Q-loop (borisov2023cytochromebdas pages 1-3, nastasi2024membraneboundredoxenzyme pages 1-2). Its high oxygen affinity makes it the preferred terminal oxidase under microaerobic conditions, and it confers remarkable resistance to cyanide, carbon monoxide, and reactive oxygen/nitrogen species (borisov2023cytochromebdas pages 1-3, sorescu2025breakthroughsinthe pages 11-12). Cytochrome bd is absent from eukaryotic mitochondria but is essential for virulence in many bacterial pathogens (sorescu2025breakthroughsinthe pages 11-12).

### 5.3. Plant-Specific Features

Plant OXPHOS differs substantially from the mammalian system. Plant Complex I (~47 subunits) includes a unique γ-carbonic anhydrase (CA) domain absent from opisthokonts (fungi and animals), as well as a ferredoxin-like iron-sulfur protein bridging the Q-module and CA module (ghifari2023thebiogenesisand pages 2-4). Plant Complex II contains four plant-specific subunits (SDH5–SDH8) with no homology to other eukaryotes, and plant Complex III uniquely incorporates the mitochondrial processing peptidase (MPP) in its matrix-facing domain (ghifari2023thebiogenesisand pages 4-6). The plant respiratory chain also features external and internal NDH-2 enzymes and AOX, providing a highly branched electron transport network (ghifari2023thebiogenesisand pages 4-6, ghifari2023thebiogenesisand pages 2-4).

### 5.4. Bacterial Diversity

Bacterial respiratory chains are modular and highly adaptable. The same organism may express different terminal oxidases (e.g., cytochrome bo₃, cytochrome bd-I, cytochrome bd-II in E. coli) depending on oxygen availability and environmental stressors (nastasi2024membraneboundredoxenzyme pages 1-2). In mycobacteria, a fused cytochrome bcc:aa₃ supercomplex replaces the separate CIII/cytochrome c/CIV found in mitochondria, with an integral membrane-bound cytochrome c domain substituting for the soluble mobile carrier. Some bacteria employ Na⁺-pumping NADH:quinone oxidoreductases (Na⁺-NQR), as in Vibrio cholerae, generating a sodium-motive force instead of a pmf through a six-subunit enzyme with unique cofactors including an intramembranous [2Fe-2S] cluster (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1. Obligatory Ordering

The electron-transport and ATP-synthesis subsystems are obligately coupled through the pmf: the ETC must pump protons before the ATP synthase can synthesize ATP. Within the ETC, the thermodynamic gradient (NADH → quinone → cytochrome c → O₂) imposes a strict directionality. The quinone pool must be reduced before Complex III can operate; cytochrome c must be reduced before Complex IV can turn over. However, the mobile carriers (quinone and cytochrome c) provide kinetic buffering that allows asynchronous turnover of individual complexes.

### 6.2. Compartment Specificity

In eukaryotes, the OXPHOS machinery is confined to the mitochondrial inner membrane; the pmf exists across this membrane, not across the outer membrane. In bacteria, the coupling membrane is the plasma membrane, with protons pumped to the periplasm. This fundamental topological constraint means that any process disrupting membrane integrity—uncoupling proteins, protonophores, membrane permeabilization—collapses the pmf and uncouples respiration from phosphorylation.

### 6.3. Assembly as a Bottleneck

OXPHOS complex biogenesis requires coordination between mitochondrial and nuclear genomes, involving translation, translocation, cofactor insertion, and modular assembly (ghifari2023thebiogenesisand pages 13-14, bennett2022mechanismsofmitochondrial pages 11-12). Assembly factors are complex-specific: for example, Complex I requires NDUFAF1-8, ACAD9, TMEM126B, and NUBPL for Fe-S delivery (bennett2022mechanismsofmitochondrial pages 11-12); Complex II requires SDHAF1-4 for FAD and Fe-S insertion (ghifari2023thebiogenesisand pages 7-8); Complex IV requires SURF1, SCO1/2, COX10/COX15 for heme A biosynthesis and copper delivery (ghifari2023thebiogenesisand pages 11-12). Recent cryo-EM studies have revealed that respirasome biogenesis concludes with the final maturation of CIV while already associated with fully assembled CI and CIII₂, with HIGD2A acting as a placeholder factor that is replaced by NDUFA4 during the last step of CIV and respirasome assembly (nguyen2026structuralbasisfor pages 24-28). Defects in any assembly factor can cause severe mitochondrial disease.

### 6.4. Failure Modes and Disease

Mutations in OXPHOS subunits or assembly factors underlie a broad spectrum of mitochondrial diseases characterized by phenotypic and genetic heterogeneity. Dominant negative variants in ATP5F1A (encoding the α-subunit of F₁) can reduce Complex V abundance and activity, leading to uncoupled OXPHOS with increased oxygen consumption but decreased membrane potential and ATP levels. Over-reduction of the chain (e.g., when Complex III or IV is inhibited) leads to electron leakage at Complexes I and III, generating superoxide and other ROS.

## 7. Controversies and Open Questions

### 7.1. The Complex I Coupling Mechanism

Despite remarkable structural progress, the exact mechanism by which ubiquinone reduction in the Q-module drives proton translocation through the P-module ~300 Å away remains unknown (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 9-11, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14). Proposed models invoke conformational coupling transmitted through the hydrophilic axis of the membrane arm, with the antiporter-like subunits ND2, ND4, and ND5 undergoing coordinated conformational changes. However, whether all four protons exit through a single pathway (ND5) or through separate channels in each antiporter-like subunit remains a central open question (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13). The authors of a comprehensive 2024 review emphasize that "proposed coupling schemes remain hypothetical, with experimental verification approaches not yet clear" (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14).

### 7.2. Supercomplex Function: Catalytic Enhancement versus Structural Stabilization

The functional significance of respiratory supercomplexes is the most debated topic in contemporary OXPHOS research. Two competing models exist:

**Catalytic enhancement model:** SCs channel quinone and cytochrome c between complexes via 2D diffusion along charged protein surfaces, enhancing electron-transfer kinetics and reducing ROS production (bennett2022mechanismsofmitochondrial pages 11-12). Exercise training and proliferative conditions correlate with increased SC formation (bennett2022mechanismsofmitochondrial pages 11-12).

**Structural stabilization model:** SCs primarily stabilize individual complexes, particularly under suboptimal biogenetic conditions. In Drosophila melanogaster, mitochondria normally have low SC levels despite high metabolic activity; SCs increase only when individual complex biogenesis is attenuated, suggesting a compensatory stabilization role rather than catalytic enhancement (nesci2021molecularandsupramolecular pages 4-5, nesci2021molecularandsupramolecular pages 2-4). Strikingly, knock-in mice with profoundly decreased respirasome levels but normal individual complex levels showed preserved respiratory chain capacity, normal exercise performance, and overall health, demonstrating that high respirasome levels are dispensable for bioenergetics in mice (milenkovic2023preservedrespiratorychain pages 45-48). A key unresolved issue is whether SCAF1-dependent remodeling is metabolically essential, with inconsistent findings across cell types and organisms (kohler2023thefunctionalsignificance pages 9-10). The inability to selectively disrupt SCs without affecting individual complex levels remains a major methodological obstacle (nesci2021molecularandsupramolecular pages 4-5).

### 7.3. Unidirectional Catalysis

In many bacterial F₁Fo-ATP synthases—particularly in mycobacteria—the enzyme efficiently synthesizes ATP but is incapable of ATP hydrolysis, a phenomenon termed "unidirectional catalysis" that remains mechanistically unexplained and is of considerable pharmacological interest given the emergence of OXPHOS-targeting anti-tuberculosis drugs (zharova2023f1·foatpsynthaseatpase pages 5-6).

### 7.4. Additional Open Questions

- The stoichiometry and energetics of the c-ring/F₁ symmetry mismatch (c-ring with n subunits versus the three catalytic sites of F₁) and how this mismatch is accommodated by elastic coupling remain under investigation.
- The precise topology of quinone exchange within supercomplexes—whether dedicated quinone pools exist within SCs or whether a common pool services all complexes—is unresolved (nesci2021molecularandsupramolecular pages 4-5, kohler2023thefunctionalsignificance pages 9-10).
- Whether the ETC-ATP synthase supercomplex discovered in T. brucei represents a widespread ancestral organization or a lineage-specific elaboration remains to be determined.

## 8. Key References

The core findings of this review draw on the following primary and review sources (among others):

- Grivennikova et al. (2024). Proton-Translocating NADH–Ubiquinone Oxidoreductase. *Int. J. Mol. Sci.* 25:13421. DOI: 10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 9-11, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14)
- Kao & Hunte (2022). Quinone binding sites of cyt bc complexes. *Biochem. Soc. Trans.* 50:877–893. DOI: 10.1042/bst20190963 (kao2022quinonebindingsites pages 3-4, kao2022quinonebindingsites pages 1-3)
- Frasch et al. (2022). F1FO ATP synthase molecular motor mechanisms. *Front. Microbiol.* 13:965620. DOI: 10.3389/fmicb.2022.965620 (frasch2022f1foatpsynthase pages 1-2)
- Zharova et al. (2023). F1·Fo ATP Synthase/ATPase: Contemporary View on Unidirectional Catalysis. *Int. J. Mol. Sci.* 24:5417. DOI: 10.3390/ijms24065417 (zharova2023f1·foatpsynthaseatpase pages 2-4, zharova2023f1·foatpsynthaseatpase pages 5-6)
- Zheng et al. (2024). High-resolution in situ structures of mammalian respiratory supercomplexes. *Nature* 631:232–239. DOI: 10.1038/s41586-024-07488-9
- Kohler et al. (2023). The functional significance of mitochondrial respiratory chain supercomplexes. *EMBO Rep.* 24:e57092. DOI: 10.15252/embr.202357092 (kohler2023thefunctionalsignificance pages 2-3, kohler2023thefunctionalsignificance pages 9-10)
- Bennett et al. (2022). Mechanisms of mitochondrial respiratory adaptation. *Nat. Rev. Mol. Cell Biol.* 23:817–835. DOI: 10.1038/s41580-022-00506-6 (bennett2022mechanismsofmitochondrial pages 11-12, bennett2022mechanismsofmitochondrial pages 12-14)
- Goldman et al. (2023). Electron transport chains as a window into the earliest stages of evolution. *PNAS* 120:e2210924120. DOI: 10.1073/pnas.2210924120 (goldman2023electrontransportchains pages 8-9, goldman2023electrontransportchains pages 2-4)
- Li et al. (2024). Alternative Oxidase: From Molecule and Function to Future Inhibitors. *ACS Omega* 9:12478–12499. DOI: 10.1021/acsomega.3c09339 (li2024alternativeoxidasefrom pages 1-3, li2024alternativeoxidasefrom pages 6-7, li2024alternativeoxidasefrom pages 7-8)
- Friedrich et al. (2022). Recent Advances in Structural Studies of Cytochrome bd. *Int. J. Mol. Sci.* 23:3166. DOI: 10.3390/ijms23063166 (friedrich2022recentadvancesin pages 8-9, friedrich2022recentadvancesin pages 2-4)
- Borisov et al. (2023). Cytochrome bd as Antioxidant Redox Enzyme. *Mol. Biol.* 57:1077–1084. DOI: 10.1134/s0026893323060031 (borisov2023cytochromebdas pages 1-3)
- Ghifari et al. (2023). The biogenesis and regulation of the plant oxidative phosphorylation system. *Plant Physiol.* 192:728–747. DOI: 10.1093/plphys/kiad108 (ghifari2023thebiogenesisand pages 4-6, ghifari2023thebiogenesisand pages 7-8, ghifari2023thebiogenesisand pages 11-12, ghifari2023thebiogenesisand pages 2-4)
- Nesci et al. (2021). Molecular and Supramolecular Structure of the Mitochondrial OXPHOS System. *Life* 11:242. DOI: 10.3390/life11030242 (nesci2021molecularandsupramolecular pages 17-19, nesci2021molecularandsupramolecular pages 4-5, nesci2021molecularandsupramolecular pages 2-4)
- Nakano et al. (2026). Structures of respiratory supercomplexes and ATP synthase oligomers. *Nat. Commun.* 17. DOI: 10.1038/s41467-026-70578-x (nakano2026structuresofrespiratory pages 1-4)
- Mrnjavac et al. (2024). The radical impact of oxygen on prokaryotic evolution. *FEBS Lett.* 598:1692–1714. DOI: 10.1002/1873-3468.14906 (mrnjavac2024theradicalimpact pages 20-22)
- Klusch et al. (2023). Cryo-EM structure of the respiratory I+III₂ supercomplex from Arabidopsis thaliana at 2 Å resolution. DOI: 10.15488/15708 (klusch2023cryoemstructureof pages 10-11)
- Nguyen et al. (2026). Structural basis for late maturation steps of CIV within the human respirasome. *Nat. Commun.* 17. DOI: 10.1038/s41467-025-68274-3 (nguyen2026structuralbasisfor pages 24-28)

References

1. (nesci2021molecularandsupramolecular pages 4-5): Salvatore Nesci, Fabiana Trombetti, Alessandra Pagliarani, Vittoria Ventrella, Cristina Algieri, Gaia Tioli, and Giorgio Lenaz. Molecular and supramolecular structure of the mitochondrial oxidative phosphorylation system: implications for pathology. Life, 11:242, Mar 2021. URL: https://doi.org/10.3390/life11030242, doi:10.3390/life11030242. This article has 92 citations.

2. (goldman2023electrontransportchains pages 2-4): Aaron D. Goldman, Jessica M. Weber, Douglas E. LaRowe, and Laura M. Barge. Electron transport chains as a window into the earliest stages of evolution. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2210924120, doi:10.1073/pnas.2210924120. This article has 31 citations and is from a highest quality peer-reviewed journal.

3. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 11-13): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 8 citations.

4. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 13-14): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 8 citations.

5. (kao2022quinonebindingsites pages 1-3): Wei-Chun Kao and Carola Hunte. Quinone binding sites of cyt bc complexes analysed by x-ray crystallography and cryogenic electron microscopy. Biochemical Society Transactions, 50:877-893, Mar 2022. URL: https://doi.org/10.1042/bst20190963, doi:10.1042/bst20190963. This article has 22 citations and is from a peer-reviewed journal.

6. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 8 citations.

7. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 8-9): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 8 citations.

8. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 9-11): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 8 citations.

9. (kao2022quinonebindingsites pages 3-4): Wei-Chun Kao and Carola Hunte. Quinone binding sites of cyt bc complexes analysed by x-ray crystallography and cryogenic electron microscopy. Biochemical Society Transactions, 50:877-893, Mar 2022. URL: https://doi.org/10.1042/bst20190963, doi:10.1042/bst20190963. This article has 22 citations and is from a peer-reviewed journal.

10. (frasch2022f1foatpsynthase pages 1-2): Wayne D. Frasch, Zain A. Bukhari, and Seiga Yanagisawa. F1fo atp synthase molecular motor mechanisms. Frontiers in Microbiology, Aug 2022. URL: https://doi.org/10.3389/fmicb.2022.965620, doi:10.3389/fmicb.2022.965620. This article has 43 citations and is from a peer-reviewed journal.

11. (zharova2023f1·foatpsynthaseatpase pages 2-4): Tatyana V. Zharova, Vera G. Grivennikova, and Vitaliy B. Borisov. F1·fo atp synthase/atpase: contemporary view on unidirectional catalysis. International Journal of Molecular Sciences, 24:5417, Mar 2023. URL: https://doi.org/10.3390/ijms24065417, doi:10.3390/ijms24065417. This article has 58 citations.

12. (nesci2021molecularandsupramolecular pages 17-19): Salvatore Nesci, Fabiana Trombetti, Alessandra Pagliarani, Vittoria Ventrella, Cristina Algieri, Gaia Tioli, and Giorgio Lenaz. Molecular and supramolecular structure of the mitochondrial oxidative phosphorylation system: implications for pathology. Life, 11:242, Mar 2021. URL: https://doi.org/10.3390/life11030242, doi:10.3390/life11030242. This article has 92 citations.

13. (zharova2023f1·foatpsynthaseatpase pages 5-6): Tatyana V. Zharova, Vera G. Grivennikova, and Vitaliy B. Borisov. F1·fo atp synthase/atpase: contemporary view on unidirectional catalysis. International Journal of Molecular Sciences, 24:5417, Mar 2023. URL: https://doi.org/10.3390/ijms24065417, doi:10.3390/ijms24065417. This article has 58 citations.

14. (kohler2023thefunctionalsignificance pages 2-3): Andreas Kohler, Antoni Barrientos, Flavia Fontanesi, and Martin Ott. The functional significance of mitochondrial respiratory chain supercomplexes. EMBO Reports, Oct 2023. URL: https://doi.org/10.15252/embr.202357092, doi:10.15252/embr.202357092. This article has 97 citations and is from a highest quality peer-reviewed journal.

15. (bennett2022mechanismsofmitochondrial pages 11-12): Christopher F. Bennett, Pedro Latorre-Muro, and Pere Puigserver. Mechanisms of mitochondrial respiratory adaptation. Nature Reviews Molecular Cell Biology, 23:817-835, Jul 2022. URL: https://doi.org/10.1038/s41580-022-00506-6, doi:10.1038/s41580-022-00506-6. This article has 329 citations and is from a domain leading peer-reviewed journal.

16. (nakano2026structuresofrespiratory pages 1-4): Atsuki Nakano, Takahiro Masuya, Shinsuke Akisada, Moe Ishikawa-Fukuda, Kaoru Mitsuoka, Hideto Miyoshi, Masatoshi Murai, and Ken Yokoyama. Structures of respiratory supercomplexes and atp synthase oligomers in mammalian mitochondrial inner membrane. Nature Communications, Mar 2026. URL: https://doi.org/10.1038/s41467-026-70578-x, doi:10.1038/s41467-026-70578-x. This article has 3 citations and is from a highest quality peer-reviewed journal.

17. (bennett2022mechanismsofmitochondrial pages 12-14): Christopher F. Bennett, Pedro Latorre-Muro, and Pere Puigserver. Mechanisms of mitochondrial respiratory adaptation. Nature Reviews Molecular Cell Biology, 23:817-835, Jul 2022. URL: https://doi.org/10.1038/s41580-022-00506-6, doi:10.1038/s41580-022-00506-6. This article has 329 citations and is from a domain leading peer-reviewed journal.

18. (allison2024theoreticalandempirical pages 11-15): TOM MATTHEW ALLISON. Theoretical and empirical insights into the ecology of oxidative phosphorylation in bilaterian metazoans. Text, Jan 2024. URL: https://doi.org/10.26180/25000439, doi:10.26180/25000439. This article has 0 citations and is from a peer-reviewed journal.

19. (mrnjavac2024theradicalimpact pages 20-22): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 15 citations and is from a peer-reviewed journal.

20. (li2024alternativeoxidasefrom pages 1-3): Jiye Li, Shiyun Yang, Yujie Wu, Ruina Wang, Yu Liu, Jiacun Liu, Zi Ye, Renjie Tang, Malcolm Whiteway, Quanzhen Lv, and Lan Yan. Alternative oxidase: from molecule and function to future inhibitors. ACS Omega, 9:12478-12499, Mar 2024. URL: https://doi.org/10.1021/acsomega.3c09339, doi:10.1021/acsomega.3c09339. This article has 25 citations and is from a peer-reviewed journal.

21. (li2024alternativeoxidasefrom pages 7-8): Jiye Li, Shiyun Yang, Yujie Wu, Ruina Wang, Yu Liu, Jiacun Liu, Zi Ye, Renjie Tang, Malcolm Whiteway, Quanzhen Lv, and Lan Yan. Alternative oxidase: from molecule and function to future inhibitors. ACS Omega, 9:12478-12499, Mar 2024. URL: https://doi.org/10.1021/acsomega.3c09339, doi:10.1021/acsomega.3c09339. This article has 25 citations and is from a peer-reviewed journal.

22. (li2024alternativeoxidasefrom pages 6-7): Jiye Li, Shiyun Yang, Yujie Wu, Ruina Wang, Yu Liu, Jiacun Liu, Zi Ye, Renjie Tang, Malcolm Whiteway, Quanzhen Lv, and Lan Yan. Alternative oxidase: from molecule and function to future inhibitors. ACS Omega, 9:12478-12499, Mar 2024. URL: https://doi.org/10.1021/acsomega.3c09339, doi:10.1021/acsomega.3c09339. This article has 25 citations and is from a peer-reviewed journal.

23. (nastasi2024membraneboundredoxenzyme pages 1-2): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

24. (sorescu2025breakthroughsinthe pages 11-12): Jennifer M. Sorescu, Martín A. González-Montalvo, Ming Yuan, Joseph De Paolo-Boisvert, Corina Diana Ceapă, Rodolfo Garcia-Contreras, Oscar Flores-Herrera, Michael E. Shea, Karina Tuz, and Oscar X. Juárez. Breakthroughs in the development of antibiotics, antifungals and antiparasitics targeting the pathogens’ respiratory chain. Critical Reviews in Biochemistry and Molecular Biology, 60(4-6):141-174, Aug 2025. URL: https://doi.org/10.1080/10409238.2025.2545785, doi:10.1080/10409238.2025.2545785. This article has 6 citations and is from a peer-reviewed journal.

25. (borisov2023cytochromebdas pages 1-3): V. B. Borisov, M. R. Nastasi, and E. Forte. Cytochrome bd as antioxidant redox enzyme. Molecular Biology, 57:1077-1084, Sep 2023. URL: https://doi.org/10.1134/s0026893323060031, doi:10.1134/s0026893323060031. This article has 17 citations and is from a peer-reviewed journal.

26. (grund2023thecryoemstructure pages 1-2): Tamara N. Grund, Yoshiki Kabashima, Tomoichirou Kusumoto, Di Wu, Sonja Welsch, Junshi Sakamoto, Hartmut Michel, and Schara Safarian. The cryoem structure of cytochrome bd from c. glutamicum provides novel insights into structural properties of actinobacterial terminal oxidases. Frontiers in Chemistry, Jan 2023. URL: https://doi.org/10.3389/fchem.2022.1085463, doi:10.3389/fchem.2022.1085463. This article has 13 citations.

27. (friedrich2022recentadvancesin pages 8-9): Thorsten Friedrich, Daniel Wohlwend, and Vitaliy B. Borisov. Recent advances in structural studies of cytochrome bd and its potential application as a drug target. International Journal of Molecular Sciences, 23:3166, Mar 2022. URL: https://doi.org/10.3390/ijms23063166, doi:10.3390/ijms23063166. This article has 61 citations.

28. (friedrich2022recentadvancesin pages 2-4): Thorsten Friedrich, Daniel Wohlwend, and Vitaliy B. Borisov. Recent advances in structural studies of cytochrome bd and its potential application as a drug target. International Journal of Molecular Sciences, 23:3166, Mar 2022. URL: https://doi.org/10.3390/ijms23063166, doi:10.3390/ijms23063166. This article has 61 citations.

29. (ghifari2023thebiogenesisand pages 2-4): Abi S Ghifari, Saurabh Saha, and Monika W Murcha. The biogenesis and regulation of the plant oxidative phosphorylation system. Plant Physiology, 192:728-747, Feb 2023. URL: https://doi.org/10.1093/plphys/kiad108, doi:10.1093/plphys/kiad108. This article has 58 citations and is from a highest quality peer-reviewed journal.

30. (ghifari2023thebiogenesisand pages 4-6): Abi S Ghifari, Saurabh Saha, and Monika W Murcha. The biogenesis and regulation of the plant oxidative phosphorylation system. Plant Physiology, 192:728-747, Feb 2023. URL: https://doi.org/10.1093/plphys/kiad108, doi:10.1093/plphys/kiad108. This article has 58 citations and is from a highest quality peer-reviewed journal.

31. (ghifari2023thebiogenesisand pages 13-14): Abi S Ghifari, Saurabh Saha, and Monika W Murcha. The biogenesis and regulation of the plant oxidative phosphorylation system. Plant Physiology, 192:728-747, Feb 2023. URL: https://doi.org/10.1093/plphys/kiad108, doi:10.1093/plphys/kiad108. This article has 58 citations and is from a highest quality peer-reviewed journal.

32. (ghifari2023thebiogenesisand pages 7-8): Abi S Ghifari, Saurabh Saha, and Monika W Murcha. The biogenesis and regulation of the plant oxidative phosphorylation system. Plant Physiology, 192:728-747, Feb 2023. URL: https://doi.org/10.1093/plphys/kiad108, doi:10.1093/plphys/kiad108. This article has 58 citations and is from a highest quality peer-reviewed journal.

33. (ghifari2023thebiogenesisand pages 11-12): Abi S Ghifari, Saurabh Saha, and Monika W Murcha. The biogenesis and regulation of the plant oxidative phosphorylation system. Plant Physiology, 192:728-747, Feb 2023. URL: https://doi.org/10.1093/plphys/kiad108, doi:10.1093/plphys/kiad108. This article has 58 citations and is from a highest quality peer-reviewed journal.

34. (nguyen2026structuralbasisfor pages 24-28): Minh Duc Nguyen, Ana Sierra-Magro, Vivek Singh, Anas Khawaja, Alba Timón-Gómez, Antoni Barrientos, and Joanna Rorbach. Structural basis for late maturation steps of mitochondrial respiratory chain complex iv within the human respirasome. Nature Communications, Jan 2026. URL: https://doi.org/10.1038/s41467-025-68274-3, doi:10.1038/s41467-025-68274-3. This article has 3 citations and is from a highest quality peer-reviewed journal.

35. (nesci2021molecularandsupramolecular pages 2-4): Salvatore Nesci, Fabiana Trombetti, Alessandra Pagliarani, Vittoria Ventrella, Cristina Algieri, Gaia Tioli, and Giorgio Lenaz. Molecular and supramolecular structure of the mitochondrial oxidative phosphorylation system: implications for pathology. Life, 11:242, Mar 2021. URL: https://doi.org/10.3390/life11030242, doi:10.3390/life11030242. This article has 92 citations.

36. (milenkovic2023preservedrespiratorychain pages 45-48): Dusanka Milenkovic, Jelena Misic, Johannes F Hevler, Thibaut Molinié, Injae Chung, Ilian Atanassov, Xinping Li, Roberta Filograna, Andrea Mesaros, Arnaud Mourier, Albert J R Heck, Judy Hirst, and Nils-Göran Larsson. Preserved respiratory chain capacity and physiology in mice with profoundly reduced levels of mitochondrial respirasomes. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.19.545560, doi:10.1101/2023.06.19.545560. This article has 75 citations.

37. (kohler2023thefunctionalsignificance pages 9-10): Andreas Kohler, Antoni Barrientos, Flavia Fontanesi, and Martin Ott. The functional significance of mitochondrial respiratory chain supercomplexes. EMBO Reports, Oct 2023. URL: https://doi.org/10.15252/embr.202357092, doi:10.15252/embr.202357092. This article has 97 citations and is from a highest quality peer-reviewed journal.

38. (goldman2023electrontransportchains pages 8-9): Aaron D. Goldman, Jessica M. Weber, Douglas E. LaRowe, and Laura M. Barge. Electron transport chains as a window into the earliest stages of evolution. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2210924120, doi:10.1073/pnas.2210924120. This article has 31 citations and is from a highest quality peer-reviewed journal.

39. (klusch2023cryoemstructureof pages 10-11): Niklas Klusch, Maximilian Dreimann, Jennifer Senkler, Nils Rugen, Werner Kühlbrandt, and Hans-Peter Braun. Cryo-em structure of the respiratory i + iii2 supercomplex from arabidopsis thaliana at 2 å resolution. Text, Jan 2023. URL: https://doi.org/10.15488/15708, doi:10.15488/15708. This article has 98 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](oxphos-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](oxphos-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. nesci2021molecularandsupramolecular pages 4-5
2. goldman2023electrontransportchains pages 2-4
3. kao2022quinonebindingsites pages 1-3
4. kao2022quinonebindingsites pages 3-4
5. kohler2023thefunctionalsignificance pages 2-3
6. nakano2026structuresofrespiratory pages 1-4
7. bennett2022mechanismsofmitochondrial pages 12-14
8. allison2024theoreticalandempirical pages 11-15
9. mrnjavac2024theradicalimpact pages 20-22
10. li2024alternativeoxidasefrom pages 1-3
11. li2024alternativeoxidasefrom pages 7-8
12. li2024alternativeoxidasefrom pages 6-7
13. sorescu2025breakthroughsinthe pages 11-12
14. ghifari2023thebiogenesisand pages 2-4
15. ghifari2023thebiogenesisand pages 4-6
16. nastasi2024membraneboundredoxenzyme pages 1-2
17. bennett2022mechanismsofmitochondrial pages 11-12
18. ghifari2023thebiogenesisand pages 7-8
19. ghifari2023thebiogenesisand pages 11-12
20. nguyen2026structuralbasisfor pages 24-28
21. milenkovic2023preservedrespiratorychain pages 45-48
22. kohler2023thefunctionalsignificance pages 9-10
23. borisov2023cytochromebdas pages 1-3
24. klusch2023cryoemstructureof pages 10-11
25. nesci2021molecularandsupramolecular pages 17-19
26. grund2023thecryoemstructure pages 1-2
27. friedrich2022recentadvancesin pages 8-9
28. friedrich2022recentadvancesin pages 2-4
29. ghifari2023thebiogenesisand pages 13-14
30. nesci2021molecularandsupramolecular pages 2-4
31. goldman2023electrontransportchains pages 8-9
32. 2Fe-2S
33. https://doi.org/10.3390/life11030242,
34. https://doi.org/10.1073/pnas.2210924120,
35. https://doi.org/10.3390/ijms252413421,
36. https://doi.org/10.1042/bst20190963,
37. https://doi.org/10.3389/fmicb.2022.965620,
38. https://doi.org/10.3390/ijms24065417,
39. https://doi.org/10.15252/embr.202357092,
40. https://doi.org/10.1038/s41580-022-00506-6,
41. https://doi.org/10.1038/s41467-026-70578-x,
42. https://doi.org/10.26180/25000439,
43. https://doi.org/10.1002/1873-3468.14906,
44. https://doi.org/10.1021/acsomega.3c09339,
45. https://doi.org/10.3390/ijms25021277,
46. https://doi.org/10.1080/10409238.2025.2545785,
47. https://doi.org/10.1134/s0026893323060031,
48. https://doi.org/10.3389/fchem.2022.1085463,
49. https://doi.org/10.3390/ijms23063166,
50. https://doi.org/10.1093/plphys/kiad108,
51. https://doi.org/10.1038/s41467-025-68274-3,
52. https://doi.org/10.1101/2023.06.19.545560,
53. https://doi.org/10.15488/15708,