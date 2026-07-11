---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T19:53:18.241276'
end_time: '2026-07-06T20:19:02.041304'
duration_seconds: 1543.8
template_file: templates/module_research.md.j2
template_variables:
  module_title: Hexuronate and aldarate catabolism
  module_summary: A bacterial free-hexuronate and aldarate catabolism module centered
    on oxidative conversion of D-glucuronate or D-galacturonate to glucarate or galactarate,
    dehydration of aldarates to keto-deoxy intermediates, and terminal oxidation of
    2,5-dioxopentanoate or KGSA to 2-oxoglutarate. This is the catabolic arm that
    KEGG places under ascorbate and aldarate metabolism in Pseudomonas putida KT2440;
    it should be kept separate from UDP-glucuronate nucleotide-sugar biosynthesis
    and from eukaryotic ascorbate metabolism.
  module_outline: "- Hexuronate and aldarate catabolism\n  - 1. hexuronate oxidation\n\
    \  - Glucuronate or galacturonate to urono-1,5-lactone\n    - Uronate dehydrogenase\
    \ (molecular player: uronate dehydrogenase activity; activity or role: uronate\
    \ dehydrogenase activity)\n  - 2. urono-lactone hydrolysis candidate\n  - Urono-1,5-lactone\
    \ hydrolysis to aldarate\n    - Gluconolactonase-family lactonase candidate (molecular\
    \ player: gluconolactonase activity; activity or role: gluconolactonase activity)\n\
    \  - 3. D-glucarate dehydration\n  - D-glucarate to 5-dehydro-4-deoxy-D-glucarate\n\
    \    - Glucarate dehydratase (molecular player: glucarate dehydratase activity;\
    \ activity or role: glucarate dehydratase activity)\n  - 4. D-galactarate dehydration\n\
    \  - D-galactarate dehydration\n    - Galactarate dehydratase (molecular player:\
    \ galactarate dehydratase activity; activity or role: galactarate dehydratase\
    \ activity)\n  - 5. 5-dehydro-4-deoxyglucarate dehydration\n  - 5-dehydro-4-deoxy-D-glucarate\
    \ to 2,5-dioxopentanoate\n    - 5-dehydro-4-deoxyglucarate dehydratase (molecular\
    \ player: 5-dehydro-4-deoxyglucarate dehydratase activity; activity or role: 5-dehydro-4-deoxyglucarate\
    \ dehydratase activity)\n  - 6. 2,5-dioxopentanoate or KGSA oxidation\n  - 2,5-dioxopentanoate\
    \ or KGSA to 2-oxoglutarate\n    - 2,5-dioxovalerate dehydrogenase (molecular\
    \ player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role:\
    \ 2,5-dioxovalerate dehydrogenase (NADP+) activity)"
  module_connections: '- Glucuronate or galacturonate to urono-1,5-lactone feeds into
    Urono-1,5-lactone hydrolysis to aldarate: Udh produces glucaro- or galactaro-1,5-lactones
    that require lactone hydrolysis before aldarate dehydration.

    - Urono-1,5-lactone hydrolysis to aldarate feeds into D-glucarate to 5-dehydro-4-deoxy-D-glucarate:
    Lactonase activity would yield D-glucarate for GudD.

    - Urono-1,5-lactone hydrolysis to aldarate feeds into D-galactarate dehydration:
    Lactonase activity would yield D-galactarate for GarD.

    - D-glucarate to 5-dehydro-4-deoxy-D-glucarate feeds into 5-dehydro-4-deoxy-D-glucarate
    to 2,5-dioxopentanoate: GudD produces 5-dehydro-4-deoxy-D-glucarate, the KDGDH
    substrate.

    - D-galactarate dehydration precedes 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate:
    The D-galactarate branch is expected to feed the downstream keto-deoxy aldarate/KGSADH
    segment, but first-pass metadata do not fully resolve the intermediate mapping.

    - 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate feeds into 2,5-dioxopentanoate
    or KGSA to 2-oxoglutarate: KDGDH produces 2,5-dioxopentanoate, the KGSADH substrate.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: hexuronate_aldarate_catabolism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: hexuronate_aldarate_catabolism-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Hexuronate and aldarate catabolism

## Working Scope

A bacterial free-hexuronate and aldarate catabolism module centered on oxidative conversion of D-glucuronate or D-galacturonate to glucarate or galactarate, dehydration of aldarates to keto-deoxy intermediates, and terminal oxidation of 2,5-dioxopentanoate or KGSA to 2-oxoglutarate. This is the catabolic arm that KEGG places under ascorbate and aldarate metabolism in Pseudomonas putida KT2440; it should be kept separate from UDP-glucuronate nucleotide-sugar biosynthesis and from eukaryotic ascorbate metabolism.

## Provisional Biological Outline

- Hexuronate and aldarate catabolism
  - 1. hexuronate oxidation
  - Glucuronate or galacturonate to urono-1,5-lactone
    - Uronate dehydrogenase (molecular player: uronate dehydrogenase activity; activity or role: uronate dehydrogenase activity)
  - 2. urono-lactone hydrolysis candidate
  - Urono-1,5-lactone hydrolysis to aldarate
    - Gluconolactonase-family lactonase candidate (molecular player: gluconolactonase activity; activity or role: gluconolactonase activity)
  - 3. D-glucarate dehydration
  - D-glucarate to 5-dehydro-4-deoxy-D-glucarate
    - Glucarate dehydratase (molecular player: glucarate dehydratase activity; activity or role: glucarate dehydratase activity)
  - 4. D-galactarate dehydration
  - D-galactarate dehydration
    - Galactarate dehydratase (molecular player: galactarate dehydratase activity; activity or role: galactarate dehydratase activity)
  - 5. 5-dehydro-4-deoxyglucarate dehydration
  - 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate
    - 5-dehydro-4-deoxyglucarate dehydratase (molecular player: 5-dehydro-4-deoxyglucarate dehydratase activity; activity or role: 5-dehydro-4-deoxyglucarate dehydratase activity)
  - 6. 2,5-dioxopentanoate or KGSA oxidation
  - 2,5-dioxopentanoate or KGSA to 2-oxoglutarate
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

## Known Relationships Among Steps

- Glucuronate or galacturonate to urono-1,5-lactone feeds into Urono-1,5-lactone hydrolysis to aldarate: Udh produces glucaro- or galactaro-1,5-lactones that require lactone hydrolysis before aldarate dehydration.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-glucarate to 5-dehydro-4-deoxy-D-glucarate: Lactonase activity would yield D-glucarate for GudD.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-galactarate dehydration: Lactonase activity would yield D-galactarate for GarD.
- D-glucarate to 5-dehydro-4-deoxy-D-glucarate feeds into 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: GudD produces 5-dehydro-4-deoxy-D-glucarate, the KDGDH substrate.
- D-galactarate dehydration precedes 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: The D-galactarate branch is expected to feed the downstream keto-deoxy aldarate/KGSADH segment, but first-pass metadata do not fully resolve the intermediate mapping.
- 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate feeds into 2,5-dioxopentanoate or KGSA to 2-oxoglutarate: KDGDH produces 2,5-dioxopentanoate, the KGSADH substrate.

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

Hexuronate and aldarate catabolism

## Working Scope

A bacterial free-hexuronate and aldarate catabolism module centered on oxidative conversion of D-glucuronate or D-galacturonate to glucarate or galactarate, dehydration of aldarates to keto-deoxy intermediates, and terminal oxidation of 2,5-dioxopentanoate or KGSA to 2-oxoglutarate. This is the catabolic arm that KEGG places under ascorbate and aldarate metabolism in Pseudomonas putida KT2440; it should be kept separate from UDP-glucuronate nucleotide-sugar biosynthesis and from eukaryotic ascorbate metabolism.

## Provisional Biological Outline

- Hexuronate and aldarate catabolism
  - 1. hexuronate oxidation
  - Glucuronate or galacturonate to urono-1,5-lactone
    - Uronate dehydrogenase (molecular player: uronate dehydrogenase activity; activity or role: uronate dehydrogenase activity)
  - 2. urono-lactone hydrolysis candidate
  - Urono-1,5-lactone hydrolysis to aldarate
    - Gluconolactonase-family lactonase candidate (molecular player: gluconolactonase activity; activity or role: gluconolactonase activity)
  - 3. D-glucarate dehydration
  - D-glucarate to 5-dehydro-4-deoxy-D-glucarate
    - Glucarate dehydratase (molecular player: glucarate dehydratase activity; activity or role: glucarate dehydratase activity)
  - 4. D-galactarate dehydration
  - D-galactarate dehydration
    - Galactarate dehydratase (molecular player: galactarate dehydratase activity; activity or role: galactarate dehydratase activity)
  - 5. 5-dehydro-4-deoxyglucarate dehydration
  - 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate
    - 5-dehydro-4-deoxyglucarate dehydratase (molecular player: 5-dehydro-4-deoxyglucarate dehydratase activity; activity or role: 5-dehydro-4-deoxyglucarate dehydratase activity)
  - 6. 2,5-dioxopentanoate or KGSA oxidation
  - 2,5-dioxopentanoate or KGSA to 2-oxoglutarate
    - 2,5-dioxovalerate dehydrogenase (molecular player: 2,5-dioxovalerate dehydrogenase (NADP+) activity; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

## Known Relationships Among Steps

- Glucuronate or galacturonate to urono-1,5-lactone feeds into Urono-1,5-lactone hydrolysis to aldarate: Udh produces glucaro- or galactaro-1,5-lactones that require lactone hydrolysis before aldarate dehydration.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-glucarate to 5-dehydro-4-deoxy-D-glucarate: Lactonase activity would yield D-glucarate for GudD.
- Urono-1,5-lactone hydrolysis to aldarate feeds into D-galactarate dehydration: Lactonase activity would yield D-galactarate for GarD.
- D-glucarate to 5-dehydro-4-deoxy-D-glucarate feeds into 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: GudD produces 5-dehydro-4-deoxy-D-glucarate, the KDGDH substrate.
- D-galactarate dehydration precedes 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate: The D-galactarate branch is expected to feed the downstream keto-deoxy aldarate/KGSADH segment, but first-pass metadata do not fully resolve the intermediate mapping.
- 5-dehydro-4-deoxy-D-glucarate to 2,5-dioxopentanoate feeds into 2,5-dioxopentanoate or KGSA to 2-oxoglutarate: KDGDH produces 2,5-dioxopentanoate, the KGSADH substrate.

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

## Hexuronate and Aldarate Catabolism: The Oxidative Pathway from Free Hexuronates to 2-Oxoglutarate

### 1. Executive Summary

Hexuronate and aldarate catabolism encompasses the enzymatic conversion of free D-glucuronate and D-galacturonate to central metabolic intermediates. This review focuses on the **oxidative catabolic arm**, best characterized in *Pseudomonas putida* KT2440 and related β- and γ-proteobacteria, in which hexuronates are first oxidized to aldarolactones by uronate dehydrogenase (Udh), hydrolyzed to the free aldaric acids by dedicated lactonases (UxuL or UxuF), dehydrated through substrate-specific aldarate dehydratases (GudD and GarD) to the common intermediate 5-dehydro-4-deoxy-D-glucarate (D-KDG), further dehydrated by KdgD to α-ketoglutaric semialdehyde (KGSA/2,5-dioxopentanoate), and terminally oxidized by KgsD (KGSADH) to 2-oxoglutarate (bouvier2019novelmetabolicpathways pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, bouvier2019novelmetabolicpathways pages 7-9). This six-step module is the catabolic pathway that KEGG places under ascorbate and aldarate metabolism. It is mechanistically and regulatorily distinct from the enterobacterial isomerization pathway (UxaC-initiated), from UDP-glucuronate nucleotide-sugar biosynthesis, and from eukaryotic ascorbate metabolism.

---

### 2. Definition and Biological Boundaries

**What is included.** This system comprises six obligatory enzymatic steps that convert free hexuronic acids to 2-oxoglutarate, along with associated transporters (TRAP-family UxuPQM, MFS-family ExuT and GarP, and TTT-family TctC), accessory enzymes (aldose 1-epimerase AldE for anomer equilibration), and transcriptional regulators (GguR, GudR, GulR, UdhR) (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12). The pathway operates on free hexuronic acids—D-glucuronate and D-galacturonate—released from plant cell wall polysaccharides (pectin, gums, hemicellulose), mucins, and peptidoglycans (bouvier2019novelmetabolicpathways pages 12-14).

**What should be treated separately.** Three neighboring systems are frequently conflated with this pathway but should be distinguished:

1. **The isomerization pathway** (UxaC-initiated), conserved in *E. coli* and other Enterobacteriales, converts hexuronates to 2-keto-3-deoxy-D-gluconate (KDG) via uronate isomerases and enters the Entner-Doudoroff pathway (bouvier2019novelmetabolicpathways pages 1-2, yoon2009cloningandcharacterization pages 1-2). This is an entirely separate route that does not involve Udh or aldarate intermediates.

2. **UDP-glucuronate nucleotide-sugar biosynthesis**, an anabolic pathway generating activated sugar donors for polysaccharide synthesis, shares the hexuronate substrate name but is biosynthetic rather than catabolic.

3. **Eukaryotic ascorbate (vitamin C) metabolism**, which is linked to uronate metabolism in KEGG pathway maps but involves distinct enzymatic chemistry and compartmentalization.

---

### 3. Mechanistic Overview

The complete oxidative pathway proceeds through six sequential steps. The following table summarizes the enzymes, substrates, products, and available kinetic data for each step, focused on *P. putida* KT2440:

| Step | Reaction | Enzyme name | Gene symbol | EC number | Key cofactors/metals | Superfamily / protein family | Key kinetic parameters where available |
|---|---|---|---|---|---|---|---|
| 1 | D-glucuronate or D-galacturonate → D-glucaro-1,5-lactone or D-galactaro-1,5-lactone | Uronate dehydrogenase | **udh** | 1.1.1.203 | NAD+; no metal requirement established for catalysis | Short-chain dehydrogenase/reductase (SDR)-like oxidoreductase with conserved Rossmann/cofactor-binding motif | **P. putida KT2440 Udh:** glucuronate **Km ~0.25 mM, kcat ~55 s^-1**; galacturonate **Km ~0.10 mM, kcat ~30 s^-1**. Pseudomonas Udhs generally show higher kcat on glucuronate than galacturonate (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 5-6) |
| 2 | D-glucaro-1,5-lactone or D-galactaro-1,5-lactone → D-glucarate or meso-galactarate | Uronolactonase / lactone hydrolase | **uxuL** or **uxuF**; in **P. putida KT2440** a candidate SGL-family lactonase is associated with the **udh-uxuPQM** locus and fitness data implicate **PP_1170** as a likely lactonase candidate | not assigned conclusively for all homologs | Divalent metal dependent; highest activity reported with **Zn2+**, **Mn2+** used in kinetics; EDTA abolishes activity | **UxuL:** SMP-30/gluconolactonase/LRE-like family (**PF08450**); **UxuF:** 7-bladed beta-propeller lactonase family (**PF10282**) | Purified UxuL/UxuF enzymes hydrolyze both glucaro- and galactaro-1,5-lactones; reported catalytic efficiencies span roughly **7.0 × 10^5 to 4.5 × 10^6 M^-1 s^-1**; R. pickettii UxuL shows **Km ~1 mM** for both substrates, with ~2-fold higher rate on galactarolactone (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 12-14, bouvier2019novelmetabolicpathways pages 10-12) |
| 3 | D-glucarate → 5-dehydro-4-deoxy-D-glucarate (D-KDG) | Glucarate dehydratase | **gudD** | 4.2.1.40 | **Mg2+** required in the canonical enzyme; phosphate implicated in active-site/cation interactions | Enolase superfamily, mandelate racemase subgroup | Canonical **E. coli GudD** has **Km ~60 μM** for D-glucarate; also acts on L-idarate and supports dehydration/epimerization chemistry. Crystal structures define catalytic bases and Mg2+-binding residues. Pseudomonas orthologs are inferred to perform the same step in the oxidative branch (mandrandberthelot2004catabolismofhexuronides pages 16-17, bouvier2019novelmetabolicpathways pages 9-10) |
| 4 | meso-Galactarate → 5-dehydro-4-deoxy-D-glucarate (D-KDG) | Galactarate dehydratase | **garD** | 4.2.1.42 | **Fe2+** strongly stimulatory; assays classically include **β-mercaptoethanol** | Enolase superfamily | Canonical **GarD** is relatively unstable; maximal activity reported with **0.5 mM Fe2+** and **170 mM β-mercaptoethanol** at pH 7.5; **Km ~0.8 mM** for galactarate (mandrandberthelot2004catabolismofhexuronides pages 16-17, mandrandberthelot2004catabolismofhexuronides pages 15-16) |
| 5 | 5-dehydro-4-deoxy-D-glucarate (D-KDG) → 2,5-dioxopentanoate / α-ketoglutaric semialdehyde (KGSA) | 5-dehydro-4-deoxyglucarate dehydratase | **kdgD** | 4.2.1.41 | not well resolved in the cited pathway reconstructions | Functionally analogous dehydratase in the alternative aldarate route; family assignment less firmly established in the reviewed sources | In the **Pseudomonas-type alternative route**, D-KDG is dehydrated/decarboxylated to **KGSA**, in contrast to the **E. coli** aldol-cleavage route via **GarL**. Gene-context and regulon data place **kdgD** with **kgsD**, **gudD**, **garD**, **udh**, and lactonase genes in proteobacterial oxidative clusters (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12) |
| 6 | 2,5-dioxopentanoate / α-ketoglutaric semialdehyde (KGSA) → 2-oxoglutarate | α-Ketoglutarate semialdehyde dehydrogenase | **kgsD** | 1.2.1.26 | **NAD+ or NADP+**, depending on isozyme; aldehyde dehydrogenase reaction | Aldehyde dehydrogenase (ALDH) superfamily; multiple convergently evolved KGSADH types | KGSADH isozymes differ in cofactor preference across bacteria: **KGSADH-II** in D-glucarate/D-galactarate catabolism is typically **NAD+-preferring**, whereas other pathway-linked isozymes can be **NADP+-preferring**. **P. putida** has been reported to possess multiple KGSADH isozymes induced by different substrates, including D-glucarate (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) |


*Table: This table summarizes the six core enzymatic steps of the oxidative hexuronate/aldarate catabolism module centered on Pseudomonas putida KT2440. It highlights the best-supported reactions, genes, enzyme families, cofactors, and available kinetic data while marking steps where organism-specific assignments remain provisional.*

#### Step 1: Hexuronate Oxidation (Udh)

Uronate dehydrogenase (Udh, EC 1.1.1.203) catalyzes the NAD⁺-dependent oxidation of D-glucuronate or D-galacturonate to the corresponding 1,5-lactone (D-glucaro-1,5-lactone or D-galactaro-1,5-lactone) (yoon2009cloningandcharacterization pages 1-2, bouvier2019novelmetabolicpathways pages 1-2). Udh is a homodimer (~60 kDa native) belonging to the short-chain dehydrogenase/reductase (SDR) superfamily, containing conserved YxxxK and GxxGxxG motifs for NAD⁺ binding (yoon2009cloningandcharacterization pages 6-8). Three Udh enzymes have been cloned and characterized from *P. syringae*, *P. putida* KT2440, and *Agrobacterium tumefaciens* C58 (yoon2009cloningandcharacterization pages 1-2). All three accept both glucuronate and galacturonate, with generally higher k_cat on glucuronate but lower K_m on galacturonate; the *A. tumefaciens* enzyme exhibits the highest rate constant (k_cat = 1.9 × 10² s⁻¹ on glucuronate), more than twofold higher than the pseudomonad enzymes (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 5-6). Udh is thermally labile; the *A. tumefaciens* enzyme retains ~80% activity after 30 min at 37°C, while the *Pseudomonas* enzymes lose most activity under the same conditions (yoon2009cloningandcharacterization pages 5-6). The enzyme has an optimal pH of approximately 8.0 (yoon2009cloningandcharacterization pages 5-6).

A critical feature of this step is substrate anomer specificity: Udh is specific for the β-anomer of the hexuronate (bouvier2019novelmetabolicpathways pages 10-12). Consequently, in organisms with Udh-based catabolism, the gene cluster frequently includes an aldose 1-epimerase (AldE) that catalyzes mutarotation of the α- and β-anomers after transport or after hydrolysis by a uronidase (bouvier2019novelmetabolicpathways pages 10-12).

#### Step 2: Urono-lactone Hydrolysis (UxuL/UxuF)

The Udh reaction produces δ-lactones (1,5-lactones), which must be hydrolyzed to the free aldaric acids (D-glucarate or *meso*-galactarate) before dehydration can proceed. Two previously uncharacterized families of lactonases fill this role:

- **UxuL**, from the SMP-30/gluconolactonase/LRE-like family (PF08450), and
- **UxuF**, from the 7-bladed beta-propeller lactonase family (PF10282) (bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 12-14).

Both enzymes belong to the beta-propeller Pfam clan (CL0186) and require divalent metal cations for activity; EDTA abolishes catalysis entirely (bouvier2019novelmetabolicpathways pages 12-14). Contrary to the Ca²⁺ preference expected from related family members, these lactonases show highest activity with Zn²⁺, followed by Mn²⁺ (bouvier2019novelmetabolicpathways pages 12-14). Purified UxuL and UxuF enzymes from *Burkholderia*, *Ralstonia*, and *Pseudomonas* species hydrolyze both glucaro- and galactaro-1,5-lactones with catalytic efficiencies in the range of 7.0 × 10⁵ to 4.5 × 10⁶ M⁻¹ s⁻¹ (bouvier2019novelmetabolicpathways pages 12-14). Notably, *P. syringae* encodes both UxuL and UxuF, with UxuL showing preference for glucarolactone and UxuF for galactarolactone (bouvier2019novelmetabolicpathways pages 12-14). The UxuF from *P. syringae* carries a signal peptide suggesting periplasmic localization, and its gene is not part of the GguR regulon, in contrast to cytoplasmic UxuL enzymes (bouvier2019novelmetabolicpathways pages 12-14).

In *P. putida* KT2440, the *uxuPQM* genes are co-transcribed with *udh* and a putative lactonase from the SGL family (PF08450), along with a putative aldose 1-epimerase (bouvier2019novelmetabolicpathways pages 7-9). High-throughput fitness data confirm that the putative lactonase PP_1170 is important during growth on D-glucuronate and D-galacturonate (price2022fillinggapsin pages 7-9). Neither UxuL nor UxuF shows activity on the γ-lactones (1,4-lactones) or on gluconolactone, demonstrating substrate specificity for the 1,5-lactone products of Udh (bouvier2019novelmetabolicpathways pages 12-14).

An alternative route exists in *A. tumefaciens* and some Halomonadaceae, where the galactaro-1,5-lactone is isomerized through a 1,4-lactone intermediate by the enzymes Gli and Gci, rather than being directly hydrolyzed (bouvier2019novelmetabolicpathways pages 12-14). However, UxuL/UxuF orthologues are the predominant lactonases in the majority of *Burkholderia*, *Pseudomonas*, *Ralstonia*, and Comamonadaceae species (bouvier2019novelmetabolicpathways pages 12-14).

#### Steps 3–4: Aldarate Dehydration (GudD and GarD)

The free aldaric acids are dehydrated by substrate-specific dehydratases that converge on the common intermediate D-5-keto-4-deoxyglucarate (D-KDG):

- **GudD** (EC 4.2.1.40), glucarate dehydratase, acts on D-glucarate with a K_m of ~60 μM and also dehydrates L-idarate (K_m ~16 μM) (mandrandberthelot2004catabolismofhexuronides pages 15-16, mandrandberthelot2004catabolismofhexuronides pages 16-17). GudD is a member of the mandelate racemase subgroup of the **enolase superfamily**, functioning as a tetramer with an N-terminal β-sheet domain and a C-terminal (β/α)₈-barrel domain containing three Mg²⁺-binding residues and catalytic bases for proton abstraction (mandrandberthelot2004catabolismofhexuronides pages 16-17).

- **GarD** (EC 4.2.1.42), galactarate dehydratase, acts on *meso*-galactarate with K_m ~0.8 mM, requiring Fe²⁺ (0.5 mM) and β-mercaptoethanol (170 mM) for maximal activity at pH 7.5 (mandrandberthelot2004catabolismofhexuronides pages 16-17, mandrandberthelot2004catabolismofhexuronides pages 15-16). GarD is notably less stable than GudD and shares ~32% identity with UxaA (the galacturonate dehydratase of the isomerization pathway) (mandrandberthelot2004catabolismofhexuronides pages 16-17).

GudD also exhibits promiscuity, capable of catalyzing both dehydration and epimerization reactions through a common enolic intermediate (mandrandberthelot2004catabolismofhexuronides pages 16-17, levy2025convergentevolutionof pages 7-8). This promiscuity has functional significance: in some organisms, GudD can partially substitute for GarD in galactarate metabolism (levy2025convergentevolutionof pages 7-8).

#### Step 5: D-KDG Dehydration (KdgD)

This step represents the branch point that distinguishes the **Pseudomonas-type dehydration route** from the **enterobacterial aldol cleavage route**. In the Pseudomonas pathway, KdgD (EC 4.2.1.41) catalyzes decarboxylating dehydration of D-KDG to produce 2,5-dioxopentanoate (α-ketoglutaric semialdehyde, KGSA), retaining the carbon skeleton as a C5 intermediate (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). In contrast, the *E. coli* pathway employs GarL (EC 4.1.2.20), a class II aldolase that cleaves D-KDG into pyruvate and tartronate semialdehyde (two C3 fragments) (mandrandberthelot2004catabolismofhexuronides pages 15-16, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). This fundamental distinction in carbon routing is summarized in the table below:

| Feature | *E. coli*-type aldol route | Pseudomonas-type dehydration route |
|---|---|---|
| Key enzyme for D-KDG processing | **GarL**, 5-keto-4-deoxy-D-glucarate aldolase, **EC 4.1.2.20**; class II aldolase that cleaves D-KDG (mandrandberthelot2004catabolismofhexuronides pages 15-16, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) | **KdgD**, 5-dehydro-4-deoxyglucarate dehydratase, **EC 4.2.1.41**; dehydrates/decarboxylates D-KDG to KGSA (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) |
| Immediate products from D-KDG | **Pyruvate + tartronate semialdehyde** (mandrandberthelot2004catabolismofhexuronides pages 15-16, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) | **2,5-dioxopentanoate / α-ketoglutaric semialdehyde (KGSA)** (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) |
| Subsequent enzymes | **GarR** (tartronate semialdehyde reductase) then **GarK** (glycerate kinase) convert the C3 semialdehyde branch to glycerate and then phosphoglycerate (mandrandberthelot2004catabolismofhexuronides pages 15-16) | **KgsD / KGSADH**, α-ketoglutarate semialdehyde dehydrogenase, **EC 1.2.1.26**, oxidizes KGSA to 2-oxoglutarate (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8) |
| Terminal products entering central metabolism | **Pyruvate + 2-phosphoglycerate/3-phosphoglycerate**, feeding lower glycolysis (mandrandberthelot2004catabolismofhexuronides pages 15-16) | **2-oxoglutarate**, feeding the TCA cycle (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) |
| Carbon logic / yield | D-KDG is split into **two C3-derived outputs**: one direct pyruvate and one glycerate/phosphoglycerate branch (mandrandberthelot2004catabolismofhexuronides pages 15-16, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) | D-KDG is retained as **one C5 product** via KGSA before oxidation to 2-oxoglutarate (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2) |
| Representative taxonomic distribution | Best established in **Enterobacteriales** such as *E. coli*; aldol-route genes also occur in some non-enterics, including parts of **Comamonadaceae** in comparative reconstructions (mandrandberthelot2004catabolismofhexuronides pages 15-16, bouvier2019novelmetabolicpathways pages 9-10) | Reported for **Pseudomonas**, **Burkholderia**, **Bacillus subtilis**, and **Azospirillum brasilense**; comparative genomics supports broad distribution in proteobacteria with oxidative/aldarate modules (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, bouvier2019novelmetabolicpathways pages 9-10) |
| Gene cluster organization | In *E. coli*, **garPLRK** and **gudPXD** are distinct loci rather than one compact oxidative module (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, mandrandberthelot2004catabolismofhexuronides pages 16-17) | Oxidative aldarate genes are often **clustered**, e.g. **garD-gudD-kdgD-kgsD** with transport/regulatory genes in proteobacterial loci (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12) |
| Regulatory context | Aldarate genes are induced by glucarate, galactarate, or glycerate and controlled by **CdaR** activator in *E. coli* (mandrandberthelot2004catabolismofhexuronides pages 16-17) | Oxidative/aldarate loci are commonly controlled by **GguR** and, in some lineages, **GulR** or **GudR**; GguR responds to the intermediate **KDG**, not the starting sugar acids (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12) |
| Pathway significance | Routes carbon from oxidized sugar acids into **glycolytic intermediates**; associated with classical enterobacterial glucarate/galactarate catabolism (mandrandberthelot2004catabolismofhexuronides pages 15-16) | Routes carbon into **2-oxoglutarate** and links the oxidative hexuronate arm directly to TCA metabolism; central to the Pseudomonas-type module emphasized in this review scope (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, bouvier2019novelmetabolicpathways pages 10-12) |


*Table: This table contrasts the two main bacterial fates of 5-dehydro-4-deoxy-D-glucarate: the enterobacterial aldol-cleavage route and the Pseudomonas-type dehydration route. It highlights differences in enzymes, products, regulation, taxonomic distribution, and entry points into central metabolism.*

#### Step 6: KGSA Oxidation (KgsD/KGSADH)

The terminal step is catalyzed by α-ketoglutaric semialdehyde dehydrogenase (KGSADH, KgsD, EC 1.2.1.26), which oxidizes KGSA to 2-oxoglutarate using NAD⁺ or NADP⁺ as electron acceptor (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2). This reaction directly connects aldarate catabolism to the TCA cycle.

KGSADH enzymes belong to the aldehyde dehydrogenase (ALDH) superfamily but show remarkable convergent evolution. Watanabe et al. (2007) identified three phylogenetically distinct KGSADH types in *Azospirillum brasilense*: KGSADH-I (L-arabinose pathway-associated, related to succinic semialdehyde dehydrogenase), KGSADH-II (D-glucarate/D-galactarate-inducible, NAD⁺-preferring), and KGSADH-III (hydroxy-L-proline-inducible, NADP⁺-preferring) (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2). *P. putida* possesses four KGSADH isozymes induced by different substrates—hydroxy-L-proline, D-glucarate, L-lysine, and one constitutive—reflecting the convergence of multiple metabolic pathways at KGSA (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). In *Bacillus subtilis*, the *ycbD* protein from the glucarate/galactarate operon represents yet another independently recruited ALDH, related to the methylmalonyl semialdehyde dehydrogenase subclass (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 9-10).

---

### 4. Major Molecular Players and Active Assemblies

**Transcriptional regulation.** The oxidative hexuronate/aldarate catabolism genes are coordinately regulated by a novel GntR-family transcription factor, **GguR**, in Pseudomonadaceae, Burkholderiaceae, Comamonadaceae, and Halomonadaceae (bouvier2019novelmetabolicpathways pages 9-10). The core GguR regulon includes *garD*, *gudD*, *kdgD*, *kgsD*, *udh*, *uxuPQM*, lactonase genes (*uxuL*/*uxuF*), and *gguR* itself (bouvier2019novelmetabolicpathways pages 9-10). Critically, the effector that disrupts GguR–DNA binding is **KDG** (5-keto-4-deoxy-D-glucarate/galactarate), not the starting hexuronates or free aldarates, at minimal concentration of 0.15 mM (bouvier2019novelmetabolicpathways pages 10-12). Additional lineage-specific regulators include the LacI-family **UdhR** (controlling *udh* and *exuT* in some Burkholderia spp.), **GudR** (controlling *gudD* and *tctC* in Comamonadaceae), and the LysR-family **GulR** in *Ralstonia* species (bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12). This contrasts sharply with the *E. coli* system, where aldarate genes are controlled by the activator **CdaR**, with D-glycerate as the best inducer (mandrandberthelot2004catabolismofhexuronides pages 16-17).

**Transporters.** Hexuronate uptake employs TRAP-family transporters (UxuPQM) or MFS-family transporters (ExuT), while aldarate uptake uses MFS-family GarP or TTT-family TctC proteins. The TctC component from *Polaromonas* sp. JS666 was demonstrated to bind D-glucarate (ΔT_m = 6.1°C) but not *meso*-galactarate (bouvier2019novelmetabolicpathways pages 12-14). Several Pseudomonas and Burkholderia species also encode GguR-regulated outer membrane porins (Omp) for hexuronate/polygalacturonate uptake (bouvier2019novelmetabolicpathways pages 9-10).

---

### 5. Evolutionary and Cell-Biological Variation

**Pathway distribution.** The oxidative Udh-based pathway is broadly distributed in β- and γ-proteobacteria. Orthologues of UxuL/UxuF have been identified in the majority of *Burkholderia*, *Pseudomonas*, *Ralstonia*, and Comamonadaceae species, whereas the Gli/Gci isomerization lactonases are restricted to Halomonadaceae (bouvier2019novelmetabolicpathways pages 12-14). The isomerization (UxaC) pathway for hexuronate catabolism is conserved in Enterobacteriales, Vibrionales, and Pasteurellales (bouvier2019novelmetabolicpathways pages 1-2). These two entry strategies are largely complementary and not typically co-occurring in a single genome: organisms with Udh generally lack UxaC, and vice versa (yoon2009cloningandcharacterization pages 1-2, bouvier2019novelmetabolicpathways pages 1-2).

**Downstream route variation.** The fate of D-KDG represents a major branch point in evolutionary variation. The aldol cleavage route (GarL → GarR → GarK) is the canonical *E. coli* pathway, producing pyruvate and 2-phosphoglycerate as glycolytic inputs (mandrandberthelot2004catabolismofhexuronides pages 15-16). The dehydration route (KdgD → KgsD) is characteristic of *Pseudomonas*, *Burkholderia*, *Bacillus subtilis*, and *Azospirillum*, generating 2-oxoglutarate as a TCA cycle input (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2). Some organisms encode both routes; in *Polaromonas* spp. and some *Burkholderia* spp., the GarL-GarR genes belong to reconstructed GguR regulons alongside KdgD-KgsD genes (bouvier2019novelmetabolicpathways pages 9-10).

**Convergent evolution of KGSADH.** KGSA serves as a metabolic nexus where the L-arabinose (Weimberg pathway), D-glucarate/D-galactarate, and hydroxy-L-proline catabolic pathways converge. At least three phylogenetically independent types of KGSADH have been recruited from different ALDH subclasses to catalyze this common terminal reaction, constituting a striking example of convergent metabolic evolution (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2).

**Gut microbiome context.** The *gud*/*gar* pathway for glucarate and galactarate utilization has emerged as ecologically significant in the inflamed gut. Levy et al. (2025) demonstrated that 887 gut microbial species across three phyla possess the pathway, and *gud*/*gar* gene abundance is significantly elevated in inflammatory bowel disease (IBD) patients (levy2025convergentevolutionof pages 5-6). Glucarate and galactarate are generated in the gut lumen by reactive nitrogen species-mediated oxidation of monosaccharides during inflammation, and the ability to metabolize these oxidized sugars confers a competitive fitness advantage to both commensals (e.g., *Blautia*, *Lachnoclostridium*) and pathogens (e.g., *Salmonella*) (levy2025convergentevolutionof pages 1-2, levy2025convergentevolutionof pages 10-11, levy2025convergentevolutionof pages 5-6). Convergent evolution is evident: commensals use a structurally unrelated 5-KDG aldolase (GudL) and distinct ABC transporters (GarABC), which are functionally equivalent to the pathogen enzymes (levy2025convergentevolutionof pages 7-8).

**Pathway loss.** The loss of glucarate/galactarate utilization in host-adapted pathogens exemplifies reductive evolution. *Salmonella* Typhi and Paratyphi A have independently lost this pathway through single amino acid substitutions in GudT (transporter), GudD (dehydratase), and GarD (dehydratase), despite intact gene sequences, illustrating the limitations of bioinformatic predictions of metabolic capability (machado2024lossoffunction pages 9-11).

**Homologies to archaea and eukaryotes.** Udh homologues extend to archaea (*Halorubrum lacusprofundi*, *Natronomonas pharaonis*) and are found across fungi, plants, and even in the human genome, though their functional significance outside bacteria is poorly characterized (yoon2009cloningandcharacterization pages 6-8).

---

### 6. Constraints, Dependencies, and Failure Modes

**Obligatory order.** The six steps occur in a strict linear sequence. Udh must act before lactonases (lactones are the substrates, not free hexuronates), and lactone hydrolysis must precede dehydration (dehydratases act on ring-opened aldaric acids, not lactones) (bouvier2019novelmetabolicpathways pages 7-9). The D-KDG intermediate is the obligatory branch point for either downstream route.

**Anomer specificity.** Udh is specific for the β-anomer of hexuronates; transport may deliver mixed anomers, requiring AldE-dependent mutarotation to ensure efficient flux (bouvier2019novelmetabolicpathways pages 10-12).

**Metal dependencies.** Each enzymatic step has distinct metal requirements: Udh requires no metal for catalysis; UxuL/UxuF require Zn²⁺ or Mn²⁺; GudD requires Mg²⁺; GarD requires Fe²⁺ (bouvier2019novelmetabolicpathways pages 12-14, mandrandberthelot2004catabolismofhexuronides pages 16-17, mandrandberthelot2004catabolismofhexuronides pages 15-16).

**Instability of GarD.** Galactarate dehydratase is notably labile and requires reducing conditions (high concentrations of β-mercaptoethanol) for reactivation, which may constrain the galactarate branch *in vitro* but presumably reflects Fe²⁺/thiol-dependent active site chemistry (mandrandberthelot2004catabolismofhexuronides pages 16-17).

**Cofactor constraints on KGSADH.** Different KGSADH isozymes show strong preferences for NAD⁺ or NADP⁺, which may influence the redox balance of the cell depending on which isozyme is expressed under given growth conditions (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 9-10).

---

### 7. Controversies and Open Questions

**Lactonase identity in *P. putida* KT2440.** While fitness data implicate PP_1170 as the functional lactonase (price2022fillinggapsin pages 7-9), and comparative genomics places an SGL-family gene adjacent to *udh* (bouvier2019novelmetabolicpathways pages 7-9), direct biochemical confirmation of PP_1170 as a glucaro/galactaro-1,5-lactonase in *P. putida* KT2440 has not been published. The organism-specific assignment remains provisional.

**The intermediate mapping for the galactarate branch.** While the glucarate branch (GudD → D-KDG → KdgD → KGSA → KgsD → 2-oxoglutarate) is linear and well-supported, the galactarate branch (GarD → D-KDG) converges at the same D-KDG intermediate. However, whether there are additional isomeric intermediates or whether *meso*-galactarate dehydration produces the identical D-KDG stereoisomer in all organisms is not fully resolved by existing metabolomics data.

**Aldol versus dehydration route coexistence.** Some organisms encode both GarL (aldol cleavage) and KdgD (dehydration), raising the question of whether both routes operate simultaneously, conditionally, or redundantly (bouvier2019novelmetabolicpathways pages 9-10). The regulatory and physiological logic governing route selection remains unclear.

**Convergent evolution of KGSADH.** While three phylogenetically distinct KGSADH types are established, the selective pressures and evolutionary trajectories that led to independent recruitment of different ALDH subclasses into the same metabolic node are not well understood (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2). In *P. putida*, which has four KGSADH isozymes, the specific pairing of each isozyme with its cognate upstream pathway has not been fully resolved genetically (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2).

**Role in gut inflammation.** The recent discovery that *gud*/*gar* pathway genes are enriched in IBD microbiomes opens the question of whether oxidized sugar metabolism is merely a passenger correlate of inflammation or an active contributor to dysbiosis (levy2025convergentevolutionof pages 10-11, levy2025convergentevolutionof pages 8-10). The strain-specificity of *gud*/*gar* genes complicates 16S-based analyses, and functional validation in gnotobiotic models is still limited.

**Biotechnological exploitation versus catabolic interference.** Metabolic engineers seeking to produce glucaric acid or galactaric acid in *E. coli* or yeast must contend with native catabolic pathways that consume the desired product. Strategies include deletion of *uxaC* and *garD* to block catabolism, achieving conversion rates up to 95%, with production demonstrated at 250-L scale (2.8 kg galactaric acid) (avci2025metabolicengineeringfor pages 13-15). However, the low stability and activity of myo-inositol oxygenase (MIOX), which feeds the synthetic glucaric acid pathway, remains a bottleneck (avci2025metabolicengineeringfor pages 15-17, moon2009productionofglucaric pages 6-6).

---

### 8. Key References

1. **Bouvier JT, Sernova NV, Ghasempur S, et al.** (2019). Novel metabolic pathways and regulons for hexuronate utilization in Proteobacteria. *Journal of Bacteriology* 201(2). doi:10.1128/jb.00431-18 — Identifies UxuL/UxuF lactonases, GguR regulons, and novel transporters across four proteobacterial families (bouvier2019novelmetabolicpathways pages 1-2, bouvier2019novelmetabolicpathways pages 7-9, bouvier2019novelmetabolicpathways pages 12-14, bouvier2019novelmetabolicpathways pages 9-10, bouvier2019novelmetabolicpathways pages 10-12).

2. **Mandrand-Berthelot M-A, Condemine G, Hugouvieux-Cotte-Pattat N.** (2004). Catabolism of hexuronides, hexuronates, aldonates, and aldarates. *EcoSal Plus* 1(1). doi:10.1128/ecosalplus.3.4.2 — Comprehensive review of *E. coli* hexuronate/aldarate catabolism (mandrandberthelot2004catabolismofhexuronides pages 15-16, mandrandberthelot2004catabolismofhexuronides pages 16-17).

3. **Yoon S-H, Moon TS, Iranpour P, Lanza AM, Prather KLJ.** (2009). Cloning and characterization of uronate dehydrogenases from two pseudomonads and *Agrobacterium tumefaciens* strain C58. *Journal of Bacteriology* 191(5):1565–1573. doi:10.1128/JB.00586-08 — First cloning and kinetic characterization of Udh from *P. putida* KT2440 (yoon2009cloningandcharacterization pages 1-2, yoon2009cloningandcharacterization pages 5-6, yoon2009cloningandcharacterization pages 6-8).

4. **Watanabe S, Yamada M, Ohtsu I, Makino K.** (2007). α-Ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of D-glucarate, D-galactarate, and hydroxy-L-proline. *Journal of Biological Chemistry* 282(9):6685–6695. doi:10.1074/jbc.M611057200 — Defines three convergently evolved KGSADH types in the ALDH superfamily (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2, watanabe2007αketoglutaricsemialdehydedehydrogenase pages 9-10).

5. **Levy S, Jiang AK, Grant MR, et al.** (2025). Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. *Nature Communications* 16. doi:10.1038/s41467-025-56332-9 — Demonstrates ecological significance of *gud*/*gar* pathway in IBD microbiomes across 887 species (levy2025convergentevolutionof pages 1-2, levy2025convergentevolutionof pages 10-11, levy2025convergentevolutionof pages 5-6, levy2025convergentevolutionof pages 2-3).

6. **Price MN, Deutschbauer AM, Arkin AP.** (2022). Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. *PLOS Genetics* 18(4):e1010156. doi:10.1371/journal.pgen.1010156 — Fitness data confirming PP_1170 as the functional lactonase in *P. putida* KT2440 (price2022fillinggapsin pages 7-9).

7. **Avci FG, Prasun T, Wendisch VF.** (2025). Metabolic engineering for microbial production of sugar acids. *BMC Biotechnology* 25. doi:10.1186/s12896-025-00973-7 — Recent review of biotechnological applications of Udh and aldarate pathway enzymes (avci2025metabolicengineeringfor pages 23-24, avci2025metabolicengineeringfor pages 13-15, avci2025metabolicengineeringfor pages 15-17, avci2025metabolicengineeringfor pages 7-9, avci2025metabolicengineeringfor pages 2-5).

8. **Moon TS, Yoon S-H, Lanza AM, Roy-Mayhew JD, Prather KLJ.** (2009). Production of glucaric acid from a synthetic pathway in recombinant *Escherichia coli*. *Applied and Environmental Microbiology* 75(3):589–595. doi:10.1128/AEM.00973-08 — Foundational work on synthetic glucaric acid production using Udh (moon2009productionofglucaric pages 6-6).

9. **Machado LFM, Galán JE.** (2024). Loss of function of metabolic traits in typhoidal *Salmonella* without apparent genome degradation. *mBio* 15(5). doi:10.1128/mbio.00607-24 — Demonstrates pathway inactivation through cryptic point mutations in host-adapted pathogens (machado2024lossoffunction pages 9-11).

10. **Suvorova IA, Tutukina MN, Ravcheev DA, et al.** (2011). Comparative genomic analysis of the hexuronate metabolism genes and their regulation in Gammaproteobacteria. *Journal of Bacteriology* 193(15):3956–3963. doi:10.1128/jb.00277-11 — Foundational comparative genomics of hexuronate pathways.

References

1. (bouvier2019novelmetabolicpathways pages 1-2): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

2. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 2-2): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

3. (bouvier2019novelmetabolicpathways pages 7-9): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

4. (bouvier2019novelmetabolicpathways pages 9-10): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

5. (bouvier2019novelmetabolicpathways pages 10-12): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

6. (bouvier2019novelmetabolicpathways pages 12-14): Jason T. Bouvier, Natalia V. Sernova, Salehe Ghasempur, Irina A. Rodionova, Matthew W. Vetting, Nawar F. Al-Obaidi, Steven C. Almo, John A. Gerlt, and Dmitry A. Rodionov. Novel metabolic pathways and regulons for hexuronate utilization in proteobacteria. Journal of Bacteriology, Jan 2019. URL: https://doi.org/10.1128/jb.00431-18, doi:10.1128/jb.00431-18. This article has 28 citations and is from a peer-reviewed journal.

7. (yoon2009cloningandcharacterization pages 1-2): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

8. (yoon2009cloningandcharacterization pages 5-6): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

9. (mandrandberthelot2004catabolismofhexuronides pages 16-17): M.-A. Mandrand-Berthelot, G. Condemine, and N. Hugouvieux-Cotte-Pattat. Catabolism of hexuronides, hexuronates, aldonates, and aldarates. Dec 2004. URL: https://doi.org/10.1128/ecosalplus.3.4.2, doi:10.1128/ecosalplus.3.4.2. This article has 19 citations.

10. (mandrandberthelot2004catabolismofhexuronides pages 15-16): M.-A. Mandrand-Berthelot, G. Condemine, and N. Hugouvieux-Cotte-Pattat. Catabolism of hexuronides, hexuronates, aldonates, and aldarates. Dec 2004. URL: https://doi.org/10.1128/ecosalplus.3.4.2, doi:10.1128/ecosalplus.3.4.2. This article has 19 citations.

11. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 1-2): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

12. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 7-8): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

13. (yoon2009cloningandcharacterization pages 6-8): Sang-Hwal Yoon, Tae Seok Moon, Pooya Iranpour, Amanda M. Lanza, and Kristala Jones Prather. Cloning and characterization of uronate dehydrogenases from two pseudomonads and<i>agrobacterium tumefaciens</i>strain c58. Mar 2009. URL: https://doi.org/10.1128/jb.00586-08, doi:10.1128/jb.00586-08. This article has 64 citations and is from a peer-reviewed journal.

14. (price2022fillinggapsin pages 7-9): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Filling gaps in bacterial catabolic pathways with computation and high-throughput genetics. Apr 2022. URL: https://doi.org/10.1371/journal.pgen.1010156, doi:10.1371/journal.pgen.1010156. This article has 44 citations and is from a domain leading peer-reviewed journal.

15. (levy2025convergentevolutionof pages 7-8): Sophia Levy, Angela K. Jiang, Maggie R. Grant, Gabriela Arp, Glory Minabou Ndjite, Xiaofang Jiang, and Brantley Hall. Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56332-9, doi:10.1038/s41467-025-56332-9. This article has 6 citations and is from a highest quality peer-reviewed journal.

16. (watanabe2007αketoglutaricsemialdehydedehydrogenase pages 9-10): Seiya Watanabe, Masaki Yamada, Iwao Ohtsu, and Keisuke Makino. Α-ketoglutaric semialdehyde dehydrogenase isozymes involved in metabolic pathways of d-glucarate, d-galactarate, and hydroxy-l-proline. Journal of Biological Chemistry, 282:6685-6695, Mar 2007. URL: https://doi.org/10.1074/jbc.m611057200, doi:10.1074/jbc.m611057200. This article has 64 citations and is from a domain leading peer-reviewed journal.

17. (levy2025convergentevolutionof pages 5-6): Sophia Levy, Angela K. Jiang, Maggie R. Grant, Gabriela Arp, Glory Minabou Ndjite, Xiaofang Jiang, and Brantley Hall. Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56332-9, doi:10.1038/s41467-025-56332-9. This article has 6 citations and is from a highest quality peer-reviewed journal.

18. (levy2025convergentevolutionof pages 1-2): Sophia Levy, Angela K. Jiang, Maggie R. Grant, Gabriela Arp, Glory Minabou Ndjite, Xiaofang Jiang, and Brantley Hall. Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56332-9, doi:10.1038/s41467-025-56332-9. This article has 6 citations and is from a highest quality peer-reviewed journal.

19. (levy2025convergentevolutionof pages 10-11): Sophia Levy, Angela K. Jiang, Maggie R. Grant, Gabriela Arp, Glory Minabou Ndjite, Xiaofang Jiang, and Brantley Hall. Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56332-9, doi:10.1038/s41467-025-56332-9. This article has 6 citations and is from a highest quality peer-reviewed journal.

20. (machado2024lossoffunction pages 9-11): Leopoldo F. M. Machado and Jorge E. Galán. Loss of function of metabolic traits in typhoidal <i>salmonella</i> without apparent genome degradation. May 2024. URL: https://doi.org/10.1128/mbio.00607-24, doi:10.1128/mbio.00607-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

21. (levy2025convergentevolutionof pages 8-10): Sophia Levy, Angela K. Jiang, Maggie R. Grant, Gabriela Arp, Glory Minabou Ndjite, Xiaofang Jiang, and Brantley Hall. Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56332-9, doi:10.1038/s41467-025-56332-9. This article has 6 citations and is from a highest quality peer-reviewed journal.

22. (avci2025metabolicengineeringfor pages 13-15): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

23. (avci2025metabolicengineeringfor pages 15-17): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

24. (moon2009productionofglucaric pages 6-6): Tae Seok Moon, Sang-Hwal Yoon, Amanda M. Lanza, Joseph D. Roy-Mayhew, and Kristala L. Jones Prather. Production of glucaric acid from a synthetic pathway in recombinant <i>escherichia coli</i>. Applied and Environmental Microbiology, 75:589-595, Feb 2009. URL: https://doi.org/10.1128/aem.00973-08, doi:10.1128/aem.00973-08. This article has 306 citations and is from a peer-reviewed journal.

25. (levy2025convergentevolutionof pages 2-3): Sophia Levy, Angela K. Jiang, Maggie R. Grant, Gabriela Arp, Glory Minabou Ndjite, Xiaofang Jiang, and Brantley Hall. Convergent evolution of oxidized sugar metabolism in commensal and pathogenic microbes in the inflamed gut. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56332-9, doi:10.1038/s41467-025-56332-9. This article has 6 citations and is from a highest quality peer-reviewed journal.

26. (avci2025metabolicengineeringfor pages 23-24): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

27. (avci2025metabolicengineeringfor pages 7-9): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

28. (avci2025metabolicengineeringfor pages 2-5): Fatma Gizem Avci, Tim Prasun, and Volker F. Wendisch. Metabolic engineering for microbial production of sugar acids. BMC Biotechnology, May 2025. URL: https://doi.org/10.1186/s12896-025-00973-7, doi:10.1186/s12896-025-00973-7. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](hexuronate_aldarate_catabolism-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](hexuronate_aldarate_catabolism-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. bouvier2019novelmetabolicpathways pages 12-14
2. yoon2009cloningandcharacterization pages 6-8
3. yoon2009cloningandcharacterization pages 1-2
4. yoon2009cloningandcharacterization pages 5-6
5. bouvier2019novelmetabolicpathways pages 10-12
6. bouvier2019novelmetabolicpathways pages 7-9
7. price2022fillinggapsin pages 7-9
8. mandrandberthelot2004catabolismofhexuronides pages 16-17
9. levy2025convergentevolutionof pages 7-8
10. mandrandberthelot2004catabolismofhexuronides pages 15-16
11. bouvier2019novelmetabolicpathways pages 9-10
12. bouvier2019novelmetabolicpathways pages 1-2
13. levy2025convergentevolutionof pages 5-6
14. machado2024lossoffunction pages 9-11
15. avci2025metabolicengineeringfor pages 13-15
16. moon2009productionofglucaric pages 6-6
17. levy2025convergentevolutionof pages 1-2
18. levy2025convergentevolutionof pages 10-11
19. levy2025convergentevolutionof pages 8-10
20. avci2025metabolicengineeringfor pages 15-17
21. levy2025convergentevolutionof pages 2-3
22. avci2025metabolicengineeringfor pages 23-24
23. avci2025metabolicengineeringfor pages 7-9
24. avci2025metabolicengineeringfor pages 2-5
25. https://doi.org/10.1128/jb.00431-18,
26. https://doi.org/10.1074/jbc.m611057200,
27. https://doi.org/10.1128/jb.00586-08,
28. https://doi.org/10.1128/ecosalplus.3.4.2,
29. https://doi.org/10.1371/journal.pgen.1010156,
30. https://doi.org/10.1038/s41467-025-56332-9,
31. https://doi.org/10.1128/mbio.00607-24,
32. https://doi.org/10.1186/s12896-025-00973-7,
33. https://doi.org/10.1128/aem.00973-08,