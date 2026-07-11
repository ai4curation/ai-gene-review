---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-06T16:02:12.812849'
end_time: '2026-07-06T16:25:40.793560'
duration_seconds: 1407.98
template_file: templates/module_research.md.j2
template_variables:
  module_title: L-methionine biosynthesis (from homoserine)
  module_summary: 'De novo biosynthesis of L-methionine from L-homoserine, modelled
    as a species-agnostic pathway template with alternative routes at three steps,
    so the same logic can be evaluated across genomes (a eukaryote-to-prokaryote test
    of the module satisfiability engine). Homoserine is first activated by acylation,
    for which bacteria use either an O-succinyltransferase (metA) or an O-acetyltransferase
    (metX). Sulfur is then incorporated to give homocysteine by one of two routes:
    trans-sulfuration (cystathionine gamma-synthase metB plus cystathionine beta-lyase
    metC, drawing sulfur from cysteine) or direct sulfhydrylation (an O-acyl-homoserine
    sulfhydrylase, metY/metZ, using free sulfide in a single step). Finally homocysteine
    is methylated to methionine by either the cobalamin-independent synthase (metE)
    or the cobalamin-dependent synthase (metH). Because every step has alternatives,
    no single enzyme is universally required; an organism makes methionine if it encodes
    at least one option at each of the three steps. This mirrors GapMind-style pathway
    reconstruction: the template defines steps and route alternatives, and a per-genome
    oracle decides which candidates are present.'
  module_outline: "- L-methionine biosynthesis\n  - 1. acylation of homoserine (succinyl\
    \ or acetyl)\n  - Homoserine activation by acylation\n    - Alternative versions\
    \ by acyl donor: Homoserine acyltransferase\n      - O-succinyltransferase (metA)\n\
    \        - metA: homoserine O-succinyltransferase (molecular player: metA (homoserine\
    \ O-succinyltransferase); activity or role: homoserine O-succinyltransferase activity)\n\
    \      - O-acetyltransferase (metX)\n        - metX: homoserine O-acetyltransferase\
    \ (molecular player: metX (homoserine O-acetyltransferase); activity or role:\
    \ homoserine O-acetyltransferase activity)\n  - 2. sulfur incorporation to homocysteine\
    \ (trans-sulfuration or direct)\n  - Sulfur incorporation to homocysteine\n  \
    \  - Alternative versions by sulfur source: Sulfur-incorporation route\n     \
    \ - Trans-sulfuration (metB + metC)\n        - 1. cystathionine formation\n  \
    \      - Cystathionine gamma-synthase\n          - metB: cystathionine gamma-synthase\
    \ (molecular player: metB (cystathionine gamma-synthase); activity or role: cystathionine\
    \ gamma-synthase activity)\n        - 2. cystathionine cleavage to homocysteine\n\
    \        - Cystathionine beta-lyase\n          - metC: cystathionine beta-lyase\
    \ (molecular player: metC (cystathionine beta-lyase); activity or role: cysteine-S-conjugate\
    \ beta-lyase activity)\n      - Direct sulfhydrylation (metY)\n        - metY:\
    \ O-acylhomoserine sulfhydrylase (molecular player: metY (O-acetylhomoserine sulfhydrylase);\
    \ activity or role: O-acetylhomoserine aminocarboxypropyltransferase activity)\n\
    \  - 3. methylation of homocysteine to methionine (cobalamin-independent or -dependent)\n\
    \  - Homocysteine methylation to methionine\n    - Alternative versions by cobalamin\
    \ dependence: Methionine synthase\n      - Cobalamin-independent synthase (metE)\n\
    \        - metE: cobalamin-independent methionine synthase (molecular player:\
    \ metE (cobalamin-independent methionine synthase); activity or role: 5-methyltetrahydropteroyltriglutamate-homocysteine\
    \ S-methyltransferase activity)\n      - Cobalamin-dependent synthase (metH)\n\
    \        - metH: cobalamin-dependent methionine synthase (molecular player: metH\
    \ (cobalamin-dependent methionine synthase); activity or role: methionine synthase\
    \ activity)"
  module_connections: '- Homoserine activation by acylation precedes Sulfur incorporation
    to homocysteine

    - Sulfur incorporation to homocysteine precedes Homocysteine methylation to methionine'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: methionine_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: methionine_biosynthesis-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

L-methionine biosynthesis (from homoserine)

## Working Scope

De novo biosynthesis of L-methionine from L-homoserine, modelled as a species-agnostic pathway template with alternative routes at three steps, so the same logic can be evaluated across genomes (a eukaryote-to-prokaryote test of the module satisfiability engine). Homoserine is first activated by acylation, for which bacteria use either an O-succinyltransferase (metA) or an O-acetyltransferase (metX). Sulfur is then incorporated to give homocysteine by one of two routes: trans-sulfuration (cystathionine gamma-synthase metB plus cystathionine beta-lyase metC, drawing sulfur from cysteine) or direct sulfhydrylation (an O-acyl-homoserine sulfhydrylase, metY/metZ, using free sulfide in a single step). Finally homocysteine is methylated to methionine by either the cobalamin-independent synthase (metE) or the cobalamin-dependent synthase (metH). Because every step has alternatives, no single enzyme is universally required; an organism makes methionine if it encodes at least one option at each of the three steps. This mirrors GapMind-style pathway reconstruction: the template defines steps and route alternatives, and a per-genome oracle decides which candidates are present.

## Provisional Biological Outline

- L-methionine biosynthesis
  - 1. acylation of homoserine (succinyl or acetyl)
  - Homoserine activation by acylation
    - Alternative versions by acyl donor: Homoserine acyltransferase
      - O-succinyltransferase (metA)
        - metA: homoserine O-succinyltransferase (molecular player: metA (homoserine O-succinyltransferase); activity or role: homoserine O-succinyltransferase activity)
      - O-acetyltransferase (metX)
        - metX: homoserine O-acetyltransferase (molecular player: metX (homoserine O-acetyltransferase); activity or role: homoserine O-acetyltransferase activity)
  - 2. sulfur incorporation to homocysteine (trans-sulfuration or direct)
  - Sulfur incorporation to homocysteine
    - Alternative versions by sulfur source: Sulfur-incorporation route
      - Trans-sulfuration (metB + metC)
        - 1. cystathionine formation
        - Cystathionine gamma-synthase
          - metB: cystathionine gamma-synthase (molecular player: metB (cystathionine gamma-synthase); activity or role: cystathionine gamma-synthase activity)
        - 2. cystathionine cleavage to homocysteine
        - Cystathionine beta-lyase
          - metC: cystathionine beta-lyase (molecular player: metC (cystathionine beta-lyase); activity or role: cysteine-S-conjugate beta-lyase activity)
      - Direct sulfhydrylation (metY)
        - metY: O-acylhomoserine sulfhydrylase (molecular player: metY (O-acetylhomoserine sulfhydrylase); activity or role: O-acetylhomoserine aminocarboxypropyltransferase activity)
  - 3. methylation of homocysteine to methionine (cobalamin-independent or -dependent)
  - Homocysteine methylation to methionine
    - Alternative versions by cobalamin dependence: Methionine synthase
      - Cobalamin-independent synthase (metE)
        - metE: cobalamin-independent methionine synthase (molecular player: metE (cobalamin-independent methionine synthase); activity or role: 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase activity)
      - Cobalamin-dependent synthase (metH)
        - metH: cobalamin-dependent methionine synthase (molecular player: metH (cobalamin-dependent methionine synthase); activity or role: methionine synthase activity)

## Known Relationships Among Steps

- Homoserine activation by acylation precedes Sulfur incorporation to homocysteine
- Sulfur incorporation to homocysteine precedes Homocysteine methylation to methionine

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

L-methionine biosynthesis (from homoserine)

## Working Scope

De novo biosynthesis of L-methionine from L-homoserine, modelled as a species-agnostic pathway template with alternative routes at three steps, so the same logic can be evaluated across genomes (a eukaryote-to-prokaryote test of the module satisfiability engine). Homoserine is first activated by acylation, for which bacteria use either an O-succinyltransferase (metA) or an O-acetyltransferase (metX). Sulfur is then incorporated to give homocysteine by one of two routes: trans-sulfuration (cystathionine gamma-synthase metB plus cystathionine beta-lyase metC, drawing sulfur from cysteine) or direct sulfhydrylation (an O-acyl-homoserine sulfhydrylase, metY/metZ, using free sulfide in a single step). Finally homocysteine is methylated to methionine by either the cobalamin-independent synthase (metE) or the cobalamin-dependent synthase (metH). Because every step has alternatives, no single enzyme is universally required; an organism makes methionine if it encodes at least one option at each of the three steps. This mirrors GapMind-style pathway reconstruction: the template defines steps and route alternatives, and a per-genome oracle decides which candidates are present.

## Provisional Biological Outline

- L-methionine biosynthesis
  - 1. acylation of homoserine (succinyl or acetyl)
  - Homoserine activation by acylation
    - Alternative versions by acyl donor: Homoserine acyltransferase
      - O-succinyltransferase (metA)
        - metA: homoserine O-succinyltransferase (molecular player: metA (homoserine O-succinyltransferase); activity or role: homoserine O-succinyltransferase activity)
      - O-acetyltransferase (metX)
        - metX: homoserine O-acetyltransferase (molecular player: metX (homoserine O-acetyltransferase); activity or role: homoserine O-acetyltransferase activity)
  - 2. sulfur incorporation to homocysteine (trans-sulfuration or direct)
  - Sulfur incorporation to homocysteine
    - Alternative versions by sulfur source: Sulfur-incorporation route
      - Trans-sulfuration (metB + metC)
        - 1. cystathionine formation
        - Cystathionine gamma-synthase
          - metB: cystathionine gamma-synthase (molecular player: metB (cystathionine gamma-synthase); activity or role: cystathionine gamma-synthase activity)
        - 2. cystathionine cleavage to homocysteine
        - Cystathionine beta-lyase
          - metC: cystathionine beta-lyase (molecular player: metC (cystathionine beta-lyase); activity or role: cysteine-S-conjugate beta-lyase activity)
      - Direct sulfhydrylation (metY)
        - metY: O-acylhomoserine sulfhydrylase (molecular player: metY (O-acetylhomoserine sulfhydrylase); activity or role: O-acetylhomoserine aminocarboxypropyltransferase activity)
  - 3. methylation of homocysteine to methionine (cobalamin-independent or -dependent)
  - Homocysteine methylation to methionine
    - Alternative versions by cobalamin dependence: Methionine synthase
      - Cobalamin-independent synthase (metE)
        - metE: cobalamin-independent methionine synthase (molecular player: metE (cobalamin-independent methionine synthase); activity or role: 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase activity)
      - Cobalamin-dependent synthase (metH)
        - metH: cobalamin-dependent methionine synthase (molecular player: metH (cobalamin-dependent methionine synthase); activity or role: methionine synthase activity)

## Known Relationships Among Steps

- Homoserine activation by acylation precedes Sulfur incorporation to homocysteine
- Sulfur incorporation to homocysteine precedes Homocysteine methylation to methionine

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

# De Novo Biosynthesis of L-Methionine from L-Homoserine: A Review of Pathway Architecture, Variation, and Genome-Based Reconstruction

## 1. Executive Summary

L-Methionine biosynthesis from L-homoserine is a modular pathway in which every catalytic step can be accomplished by two or more non-homologous or paralogous enzyme families. The pathway proceeds through three obligatory phases: (i) activation of homoserine by acylation (succinylation via MetA or acetylation via MetX/MET2); (ii) incorporation of sulfur to yield homocysteine, either through trans-sulfuration (MetB + MetC, using cysteine as sulfur donor) or direct sulfhydrylation (MetY/MET25, using free sulfide); and (iii) methylation of homocysteine to methionine by a cobalamin-independent synthase (MetE), a cobalamin-dependent synthase (MetH), or one of at least four additional folate-independent methionine synthase families (MesA–D) (augustus2011themetjregulon pages 7-8, price2021fourfamiliesof pages 1-4). Because every step has alternatives, no single enzyme gene is universally required across all methionine-producing organisms; an organism synthesizes methionine if and only if it encodes at least one functional variant at each of the three steps. This combinatorial logic underlies GapMind-style pathway reconstruction tools, which define steps and route alternatives as a template, then query individual genomes for candidate proteins at each position (price2020gapmindautomatedannotation pages 1-2, price2020gapmindautomatedannotation pages 2-4). Plants represent a notable departure from the bacterial framework, using O-phosphohomoserine rather than an acyl-homoserine intermediate, with the first two steps compartmentalized in the chloroplast and the final methylation occurring in the cytosol (chen2025theyangcycle pages 2-3, watanabe2021metabolismandregulatory pages 3-5).

## 2. Definition and Biological Boundaries

### 2.1 Scope of the Pathway

The pathway covered in this review begins with L-homoserine, a product of aspartate semialdehyde reduction by homoserine dehydrogenase, and ends with L-methionine. The three sequential phases—acylation, sulfur incorporation, and methylation—are chemically and genetically separable. Each phase presents binary or higher-order route alternatives, making the pathway a natural test case for modular pathway reconstruction (price2020gapmindautomatedannotation pages 1-2).

### 2.2 Neighboring Pathways to Distinguish

Several interconnected metabolic processes are routinely confused with de novo methionine biosynthesis and should be treated separately:

- **The SAM cycle (S-adenosylmethionine cycle):** Methionine is adenylated by MetK/MAT to form SAM, which serves as a universal methyl donor. Following methyl transfer, SAM becomes S-adenosylhomocysteine (SAH), which is hydrolyzed to homocysteine and adenosine. Cytosolic methionine synthase then regenerates methionine from this recycled homocysteine. This is methionine *regeneration*, not de novo *biosynthesis* (watanabe2021metabolismandregulatory pages 5-6, rodionov2004comparativegenomicsof pages 2-3).

- **The methionine salvage pathway (Yang cycle):** Recycling of 5′-methylthioadenosine (MTA), a byproduct of polyamine and ethylene biosynthesis, back to methionine via methylthioribose intermediates. This is biochemically distinct and involves entirely different enzymes (sekowska2004bacterialvariationson pages 1-2, rodionov2004comparativegenomicsof pages 8-9).

- **Reverse trans-sulfuration:** In many organisms, homocysteine can be converted to cysteine through cystathionine β-synthase and cystathionine γ-lyase. This reverses the sulfur flow relative to the forward trans-sulfuration route of methionine biosynthesis and is a cysteine-producing pathway rather than a methionine-producing one (rodionov2004comparativegenomicsof pages 8-9, thomas1997metabolismofsulfur pages 11-12).

- **Threonine and isoleucine biosynthesis:** Homoserine is a branch-point metabolite shared with threonine kinase (ThrB) and ultimately threonine/isoleucine production. In plants, the key branch-point metabolite is O-phosphohomoserine (OPH), competed for by cystathionine γ-synthase (CGS, toward methionine) and threonine synthase (TS, toward threonine) (watanabe2021metabolismandregulatory pages 3-5, chen2025theyangcycle pages 2-3, devi2023geneticandmolecular pages 4-6).

- **Upstream aspartate pathway:** Conversion of aspartate to aspartate semialdehyde and then to homoserine precedes this pathway and is shared with lysine biosynthesis (via the DAP route) (watanabe2021metabolismandregulatory pages 3-5).

## 3. Mechanistic Overview

### 3.1 Step 1: Activation of Homoserine by Acylation

Homoserine must be activated before sulfur can be incorporated. Activation is achieved by transfer of an acyl group from a CoA thioester to the γ-hydroxyl of homoserine. Two non-homologous enzyme families accomplish this:

**MetA (homoserine O-succinyltransferase, EC 2.3.1.46)** transfers a succinyl group from succinyl-CoA, producing O-succinyl-L-homoserine. This enzyme is characteristic of *Escherichia coli* and many γ-proteobacteria (augustus2011themetjregulon pages 7-8, rodionov2004comparativegenomicsof pages 1-2). MetA is subject to strong feedback inhibition by both methionine and SAM, and the protein is notably thermolabile, a feature that has been a target of metabolic engineering efforts (rodionov2004comparativegenomicsof pages 7-7).

**MetX (homoserine O-acetyltransferase, EC 2.3.1.31)** transfers an acetyl group from acetyl-CoA, producing O-acetyl-L-homoserine. MetX is phylogenetically unrelated to MetA and is found in *Leptospira meyeri*, *Mycobacterium tuberculosis*, *Staphylococcus*, *Listeria*, and many other organisms (rodionov2004comparativegenomicsof pages 1-2, sari2024theroleof pages 1-2, sari2024theroleof pages 2-3). In *Bacillus subtilis*, the acetyltransferase (designated MetB in the *B. subtilis* nomenclature, not to be confused with the *E. coli* cystathionine γ-synthase MetB) is feedback inhibited by SAM, whereas MetX in *Leptospira* is notably not feedback inhibited (rodionov2004comparativegenomicsof pages 7-7).

In *Saccharomyces cerevisiae*, the homologous enzyme is encoded by **MET2** and uses acetyl-CoA as the acyl donor. MET2 protein is a dimer of approximately 100 kDa (thomas1997metabolismofsulfur pages 10-11).

Plants represent a fundamentally different solution: rather than acylating homoserine, plants use **O-phosphohomoserine (OPH)** as the activated intermediate, which is produced by homoserine kinase. CGS then directly displaces the phosphate group during cystathionine formation. This makes plants non-analogous to the bacterial acylation framework at step 1 (chen2025theyangcycle pages 2-3, watanabe2021metabolismandregulatory pages 3-5).

### 3.2 Step 2: Sulfur Incorporation to Yield Homocysteine

Two fundamentally different strategies exist for introducing sulfur into the carbon skeleton:

**Trans-sulfuration route (MetB + MetC):** This two-enzyme route draws sulfur from L-cysteine. Cystathionine γ-synthase (MetB, EC 2.5.1.48) catalyzes a γ-replacement reaction in which the acyl leaving group of O-acylhomoserine is displaced by the thiol of cysteine to form cystathionine. Cystathionine β-lyase (MetC, EC 4.4.1.8) then cleaves cystathionine to release L-homocysteine, pyruvate, and ammonia. Both enzymes are pyridoxal 5′-phosphate (PLP)-dependent. This route is the sole sulfur incorporation pathway in *E. coli* and is used in plants (via CGS and CBL operating on O-phosphohomoserine) (augustus2011themetjregulon pages 7-8, rodionov2004comparativegenomicsof pages 1-2, chen2025theyangcycle pages 2-3).

**Direct sulfhydrylation route (MetY/MET25):** A single PLP-dependent enzyme, O-acylhomoserine sulfhydrylase (EC 2.5.1.49), catalyzes the direct replacement of the acyl leaving group with inorganic sulfide (H₂S/HS⁻), yielding homocysteine in one step without a cystathionine intermediate. In *S. cerevisiae*, this enzyme is encoded by MET25 (also known as MET17 or MET15) and functions as a homotetramer of approximately 200 kDa binding four PLP molecules (thomas1997metabolismofsulfur pages 10-11). This route is also the primary pathway in many Gram-positive bacteria and in *Corynebacterium glutamicum* (rodionov2004comparativegenomicsof pages 1-2).

*Corynebacterium glutamicum* is notable for possessing **both** the trans-sulfuration and direct sulfhydrylation routes, operating in parallel (rodionov2004comparativegenomicsof pages 1-2). Among Gram-positive bacteria surveyed by Rodionov et al., twelve species possessed only MetY, two had only the MetI-MetC trans-sulfuration pair, and seven contained both pathways (rodionov2004comparativegenomicsof pages 7-7).

### 3.3 Step 3: Methylation of Homocysteine to Methionine

The final step transfers a methyl group to the thiol of homocysteine. This is the most diversified step, with at least six distinct enzyme families known:

**MetE (cobalamin-independent methionine synthase, EC 2.1.1.14):** Uses 5-methyltetrahydrofolate (5-methyl-THF) as the methyl donor and requires zinc for catalysis. MetE is the predominant methionine synthase across most methionine-producing Firmicutes and is the sole type in plants (rodionov2004comparativegenomicsof pages 7-7, price2021fourfamiliesof pages 1-4, watanabe2021metabolismandregulatory pages 3-5).

**MetH (cobalamin-dependent methionine synthase, EC 2.1.1.13):** Also uses 5-methyl-THF as the ultimate methyl donor but employs cobalamin (vitamin B₁₂) as an intermediate carrier. MetH is a large, modular protein with distinct domains for binding homocysteine, methyltetrahydrofolate, cobalamin, and S-adenosylmethionine (the latter for reductive reactivation). In some bacteria, MetH exists as a single large polypeptide (as in *E. coli*), while in others it is split into two or three separate proteins with different domain arrangements (price2020gapmindautomatedannotation pages 4-7). In *Mycobacterium tuberculosis*, cobalamin availability regulates the choice between MetE and MetH: endogenous cobalamin significantly inhibits MetE transcription and translation, switching the organism to MetH when B₁₂ is available (sari2024theroleof pages 3-4).

**MesA–D (folate-independent core methionine synthases):** Price et al. (2021) identified four families of methionine synthases that lack folate-binding domains and use alternative methyl donors (price2021fourfamiliesof pages 1-4). MesA is found exclusively in methanogens and obtains methyl groups from the MtrA corrinoid protein of the methanogenesis pathway. MesB and MesC are found in organisms with the Wood-Ljungdahl pathway and obtain methyl groups from the iron-sulfur corrinoid protein (CoFeSP). MesD is found only in aerobic bacteria and requires an uncharacterized partner protein (MesX/DUF1852) and molecular oxygen for activity, with no requirement for cobalamin or folate (price2021fourfamiliesof pages 12-15, price2021fourfamiliesof pages 15-18, price2021fourfamiliesof pages 9-12). These four families share less than 30% pairwise amino acid identity, though all conserve the zinc-binding and homocysteine-binding residues of the MetE catalytic domain (price2021fourfamiliesof pages 9-12, price2021fourfamiliesof pages 1-4).

Some organisms also use **betaine-homocysteine methyltransferase (BhmT)** as an alternative, notably *Oceanobacillus iheyensis* which lacks both MetE and MetH (rodionov2004comparativegenomicsof pages 7-7).

## 4. Major Molecular Players and Active Assemblies

The following table summarizes the complete catalog of enzymes at each pathway step:

| Step | Route/Alternative | Gene Name | Enzyme Name | EC Number | Reaction (substrate → product) | Cofactors | Representative Organisms |
|---|---|---|---|---|---|---|---|
| 1. Acylation | O-succinylation | **metA** | Homoserine O-succinyltransferase | **2.3.1.46** | L-homoserine + succinyl-CoA → O-succinyl-L-homoserine + CoA | Succinyl-CoA | *Escherichia coli* and many Proteobacteria (rodionov2004comparativegenomicsof pages 1-2, augustus2011themetjregulon pages 7-8, leyn2014comparativegenomicsof pages 2-3) |
| 1. Acylation | O-acetylation | **metX** | Homoserine O-acetyltransferase | **2.3.1.31** | L-homoserine + acetyl-CoA → O-acetyl-L-homoserine + CoA | Acetyl-CoA | *Mycobacterium tuberculosis*, *Leptospira meyeri*, diverse Gram-positives (rodionov2004comparativegenomicsof pages 1-2, sari2024theroleof pages 1-2) |
| 1. Acylation | O-acetylation (yeast ortholog) | **MET2** | Homoserine O-acetyltransferase / homoserine transacetylase | **2.3.1.31** | L-homoserine + acetyl-CoA → O-acetyl-L-homoserine + CoA | Acetyl-CoA | *Saccharomyces cerevisiae* (thomas1997metabolismofsulfur pages 10-11) |
| 2. Sulfur incorporation | Trans-sulfuration, cystathionine formation | **metB** | Cystathionine γ-synthase | **2.5.1.48** | O-succinyl- or O-acetyl-homoserine + cysteine → cystathionine + succinate/acetate | **PLP** | *E. coli*; trans-sulfuration-using bacteria (augustus2011themetjregulon pages 7-8, rodionov2004comparativegenomicsof pages 1-2) |
| 2. Sulfur incorporation | Trans-sulfuration, cystathionine cleavage | **metC** | Cystathionine β-lyase | **4.4.1.8** | Cystathionine → homocysteine + pyruvate + NH3 | **PLP** | *E. coli*; trans-sulfuration-using bacteria (augustus2011themetjregulon pages 7-8, rodionov2004comparativegenomicsof pages 1-2) |
| 2. Sulfur incorporation | Direct sulfhydrylation | **metY** | O-acylhomoserine sulfhydrylase | **2.5.1.49** | O-acetyl- or O-succinyl-homoserine + sulfide → homocysteine + acetate/succinate | **PLP** | *Corynebacterium glutamicum*, many direct-sulfhydrylation bacteria (rodionov2004comparativegenomicsof pages 7-7, rodionov2004comparativegenomicsof pages 1-2) |
| 2. Sulfur incorporation | Direct sulfhydrylation (yeast enzyme) | **MET25 / MET17 / MET15** | O-acetylhomoserine sulfhydrylase | **2.5.1.49** | O-acetylhomoserine + sulfide → homocysteine + H2O/acetate equivalent | **PLP** | *Saccharomyces cerevisiae* (thomas1997metabolismofsulfur pages 10-11, thomas1997metabolismofsulfur pages 4-5) |
| 3. Methylation | Cobalamin-independent methionine synthase | **metE** | Methionine synthase, cobalamin-independent | **2.1.1.14** | Homocysteine + 5-methyltetrahydrofolate → methionine + tetrahydrofolate | **Zn** | Many bacteria; plants use related cobalamin-independent methionine synthases (rodionov2004comparativegenomicsof pages 7-7, leyn2014comparativegenomicsof pages 2-3, watanabe2021metabolismandregulatory pages 3-5) |
| 3. Methylation | Cobalamin-dependent methionine synthase | **metH** | Methionine synthase, cobalamin-dependent | **2.1.1.13** | Homocysteine + 5-methyltetrahydrofolate → methionine + tetrahydrofolate | **Cobalamin, Zn** | *E. coli*, some Bacilli, mycobacteria when B12 is available (rodionov2004comparativegenomicsof pages 7-7, price2020gapmindautomatedannotation pages 4-7, sari2024theroleof pages 3-4) |
| 3. Methylation | Folate-independent methionine synthase family A | **mesA** | Core methionine synthase (MesA family) | N/A | Homocysteine + methylated corrinoid protein → methionine | Corrinoid protein donor | Methanogens (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 4-7) |
| 3. Methylation | Folate-independent methionine synthase family B | **mesB** | Core methionine synthase (MesB family) | N/A | Homocysteine + CoFeSP-bound methyl group → methionine | Corrinoid iron-sulfur protein | Anaerobic bacteria and some archaea with Wood-Ljungdahl pathway (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 7-9) |
| 3. Methylation | Folate-independent methionine synthase family C | **mesC** | Core methionine synthase (MesC family) | N/A | Homocysteine + CoFeSP-bound methyl group → methionine | Corrinoid iron-sulfur protein | Anaerobic archaea with Wood-Ljungdahl pathway (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 4-7, price2021fourfamiliesof pages 7-9) |
| 3. Methylation | Folate-independent methionine synthase family D | **mesD** | Core methionine synthase (MesD family) | N/A | Homocysteine + unknown MesX-derived methyl donor → methionine | Requires **MesX/DUF1852** and **O2**; no folate or cobalamin required | Aerobic bacteria (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 12-15, price2021fourfamiliesof pages 15-18) |


*Table: This table summarizes the major enzyme alternatives used in L-methionine biosynthesis from homoserine across taxa, including the canonical acylation, sulfur-incorporation, and methylation steps plus recently recognized folate-independent methionine synthase families.*

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Distribution Across Lineages

The pathway exhibits striking combinatorial diversity across the tree of life. The following table captures the dominant route choices across representative organisms:

| Organism/Lineage | Step 1 (Acylation enzyme) | Step 2 (Sulfur incorporation route) | Step 3 (Methylation enzyme) | Key Regulatory Mechanism |
|---|---|---|---|---|
| *Escherichia coli* | **metA**; homoserine *O*-succinyltransferase | Trans-sulfuration via **metB + metC** | **metE** and **metH** | **MetJ** repressor + **MetR** activator (augustus2011themetjregulon pages 7-8, leyn2014comparativegenomicsof pages 2-3, rodionov2004comparativegenomicsof pages 2-3) |
| *Bacillus subtilis* | **metB**; homoserine *O*-acetyltransferase, SAM-inhibited | Primarily direct sulfhydrylation via **metY** | **metE** | **S-box / SAM-I riboswitch** (rodionov2004comparativegenomicsof pages 7-7, rodionov2004comparativegenomicsof pages 11-11, rodionov2004comparativegenomicsof pages 2-3) |
| *Corynebacterium glutamicum* | **metX**; homoserine *O*-acetyltransferase | Both trans-sulfuration and direct sulfhydrylation | **metH / metE** | **McbR** repressor (rodionov2004comparativegenomicsof pages 1-2, leyn2014comparativegenomicsof pages 11-11) |
| *Mycobacterium tuberculosis* | **metX**; homoserine *O*-acetyltransferase | Trans-sulfuration | **metE** and **metH**; cobalamin-regulated usage | Cobalamin-dependent switching of **metE/metH**; broader transcriptional control unresolved here (sari2024theroleof pages 1-2, sari2024theroleof pages 3-4, sari2024theroleof pages 2-3) |
| *Saccharomyces cerevisiae* | **MET2**; homoserine *O*-acetyltransferase | Direct sulfhydrylation via **MET25/MET17/MET15** | **Met6p**; B12-independent methionine synthase | **Met4/Met28/Met31/Met32** transcriptional network (thomas1997metabolismofsulfur pages 10-11, thomas1997metabolismofsulfur pages 11-12, thomas1997metabolismofsulfur pages 1-4) |
| Plants (*Arabidopsis*) | **O-phosphohomoserine** branch point; no homoserine acylation step | Trans-sulfuration-like route via **CGS + CBL** in chloroplast | Cobalamin-independent **MS** isoforms in chloroplast/cytosol | **SAM feedback on CGS mRNA/expression** (chen2025theyangcycle pages 2-3, watanabe2021metabolismandregulatory pages 3-5, hell2008sulfurmetabolismin pages 139-140) |
| Methanogens | Variable / not standardized in the bacterial acylation framework | Variable | **MesA**; folate-independent methionine synthase using **MtrA**-derived methyl groups | Not resolved in the cited sources (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 4-7) |
| Anaerobic Wood-Ljungdahl bacteria | Variable / not standardized in the bacterial acylation framework | Variable | **MesB / MesC**; folate-independent methionine synthases using **CoFeSP** | Not resolved in the cited sources (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 7-9, price2021fourfamiliesof pages 4-7) |


*Table: This table compares the major route choices for methionine biosynthesis across representative lineages, emphasizing the lineage-specific substitutions at homoserine activation, sulfur incorporation, methylation, and regulation. It is useful for genome-based pathway reconstruction because it highlights which enzymes are alternatives rather than universal requirements.*

### 5.2 Key Patterns of Variation

**Acylation step:** MetA (succinyltransferase) and MetX (acetyltransferase) are non-homologous proteins that catalyze the same logical step with different acyl donors. MetA predominates in enterobacteria, while MetX is used in mycobacteria, spirochaetes, staphylococci, and listeriae (rodionov2004comparativegenomicsof pages 1-2, rodionov2004comparativegenomicsof pages 7-7). In *B. subtilis*, the acetyltransferase (confusingly named MetB in that organism's nomenclature) is feedback-inhibited by SAM, whereas MetX in *Leptospira* is not (rodionov2004comparativegenomicsof pages 7-7). Plants bypass this step entirely by using O-phosphohomoserine (chen2025theyangcycle pages 2-3).

**Sulfur incorporation:** The trans-sulfuration route is phylogenetically widespread but not universal. Direct sulfhydrylation predominates in yeast and many Gram-positive bacteria. *C. glutamicum* uniquely maintains both routes in parallel (rodionov2004comparativegenomicsof pages 1-2). In *S. cerevisiae*, sulfide is incorporated into a four-carbon chain (yielding homocysteine directly), whereas *E. coli* incorporates sulfide into a three-carbon chain (yielding cysteine), necessitating trans-sulfuration for methionine biosynthesis (thomas1997metabolismofsulfur pages 10-11).

**Methylation step:** The MetE/MetH dichotomy correlates with cobalamin availability: organisms in cobalamin-rich environments tend to rely on MetH, while those without reliable B₁₂ supply maintain MetE. In methanogens and Wood-Ljungdahl organisms, entirely different methionine synthase families (MesA–C) are employed that obtain methyl groups from pathway-specific corrinoid proteins (price2021fourfamiliesof pages 1-4, price2021fourfamiliesof pages 4-7). The aerobic MesD family represents yet another independent solution (price2021fourfamiliesof pages 12-15, price2021fourfamiliesof pages 15-18).

### 5.3 Plant-Specific Features

In plants such as *Arabidopsis*, the pathway is compartmentalized: cystathionine γ-synthase (CGS) and cystathionine β-lyase (CBL) are localized exclusively in the chloroplast, while methionine synthase (MS) exists in both chloroplastic and cytosolic isoforms (chen2025theyangcycle pages 2-3, watanabe2021metabolismandregulatory pages 3-5). Arabidopsis has three MS genes: AtMS3 (chloroplastic, involved in de novo synthesis) and AtMS1/AtMS2 (cytosolic, involved in SAM cycle methionine regeneration) (watanabe2021metabolismandregulatory pages 3-5). All plant methionine synthases are cobalamin-independent. The plant *mto1* mutant of Arabidopsis, carrying a mutation in CGS that abolishes SAM-mediated mRNA destabilization, accumulates 40-fold more soluble methionine than wild type, illustrating the importance of post-transcriptional feedback regulation (chen2025theyangcycle pages 2-3).

### 5.4 Fungal Features

In *S. cerevisiae*, the pathway uses O-acetylhomoserine (MET2) and direct sulfhydrylation (MET25) exclusively; no cysteine is synthesized directly from sulfide, and cysteine production depends entirely on the forward trans-sulfuration pathway from homocysteine (thomas1997metabolismofsulfur pages 10-11, thomas1997metabolismofsulfur pages 11-12, thomas1997metabolismofsulfur pages 4-5). The yeast pathway is regulated by a network of transcription factors including Met4, Met28, Met31, Met32, and Cbf1 (thomas1997metabolismofsulfur pages 1-4). In the fungal pathogen *Candida albicans*, the regulatory circuit has diverged: only Met4 and Cbf1 are core regulators of methionine biosynthesis, suggesting the *S. cerevisiae* circuit represents a recently evolved arrangement.

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering

The three steps must proceed in strict sequence: acylation → sulfur incorporation → methylation. Homoserine cannot accept sulfur without prior activation, and homocysteine cannot be methylated before it is formed (augustus2011themetjregulon pages 7-8, watanabe2021metabolismandregulatory pages 3-5).

### 6.2 Substrate and Cofactor Constraints

The sulfur incorporation enzymes (MetB, MetC, MetY/MET25) are all PLP-dependent, making pyridoxal 5′-phosphate an essential cofactor for step 2 regardless of route choice (thomas1997metabolismofsulfur pages 10-11, thomas1997metabolismofsulfur pages 11-12). The methylation step introduces cofactor-dependent constraints: MetH requires cobalamin, and MetE requires zinc. MesD requires molecular oxygen and the partner protein MesX, making it incompatible with anaerobic growth (price2021fourfamiliesof pages 12-15, price2021fourfamiliesof pages 15-18). MesA–C require specific corrinoid proteins from methanogenesis or the Wood-Ljungdahl pathway, restricting their use to organisms possessing those pathways (price2021fourfamiliesof pages 4-7).

### 6.3 Mutual Exclusivities and Dependencies

GapMind's pathway analysis includes a critical dependency check: if an organism appears to both synthesize methionine from cysteine (via trans-sulfuration) and cysteine from methionine (via reverse trans-sulfuration), this creates a circular dependency that would indicate auxotrophy for one or both amino acids (price2020gapmindautomatedannotation pages 16-17). This logic is essential for correct genome-based pathway reconstruction.

The acyl donor choice (succinyl-CoA vs. acetyl-CoA) constrains which form of acylhomoserine is available to downstream enzymes, though both MetB and MetY can generally accept either O-succinylhomoserine or O-acetylhomoserine, with varying kinetic preferences (augustus2011themetjregulon pages 7-8).

### 6.4 Regulation as a Constraint

Methionine biosynthesis is regulated at multiple levels, and the regulatory mechanisms themselves vary across lineages:

- In *E. coli*, the SAM-responsive repressor **MetJ** binds tandem MET-box sequences to repress biosynthesis genes, while the homocysteine-sensing activator **MetR** upregulates MetE and MetF (leyn2014comparativegenomicsof pages 2-3, rodionov2004comparativegenomicsof pages 2-3).

- In *B. subtilis* and Clostridia, the **S-box (SAM-I) riboswitch** directly binds SAM, stabilizing a terminator hairpin structure that causes premature transcription termination of methionine biosynthesis operons (rodionov2004comparativegenomicsof pages 11-11, rodionov2004comparativegenomicsof pages 2-3). Lactobacillales use a methionine-specific **T-box** mechanism involving uncharged tRNA sensing (rodionov2004comparativegenomicsof pages 11-11).

- In α-proteobacteria, the **SAM-II (SAM_alpha) riboswitch** controls metX, metY, and metA genes (leyn2014comparativegenomicsof pages 2-3).

- In Proteobacteria, the **SahR** transcription factor senses S-adenosylhomocysteine (SAH) and controls methionine metabolism genes (leyn2014comparativegenomicsof pages 1-2, leyn2014comparativegenomicsof pages 10-11).

- In Corynebacteria, the **McbR** repressor modulated by SAH controls methionine and cysteine biosynthesis regulons (leyn2014comparativegenomicsof pages 11-11).

- In plants, CGS expression is regulated post-transcriptionally by SAM, which triggers degradation of CGS mRNA through a conserved regulatory element (chen2025theyangcycle pages 2-3).

## 7. Pathway Reconstruction: GapMind and Module Satisfiability

The methionine biosynthesis pathway is an exemplary case for automated pathway reconstruction tools. GapMind defines each biosynthetic pathway as a series of steps, where each step can have alternative enzyme candidates. A genome is considered to possess a pathway if high-confidence candidates are identified for all steps (price2020gapmindautomatedannotation pages 1-2, price2020gapmindautomatedannotation pages 2-4). For methionine biosynthesis, GapMind incorporates variant pathways including both acyltransferase types, both sulfur incorporation routes, and multiple methionine synthases including split MetH arrangements (price2020gapmindautomatedannotation pages 4-7). The tool uses similarity to experimentally characterized proteins (from a database of 1,821 characterized proteins across 149 steps) with confidence thresholds: high-confidence candidates must be ≥40% identical to a characterized protein with the specific function (price2024interactivetoolsfor pages 9-10, price2020gapmindautomatedannotation pages 2-4).

The 2024 update to GapMind reduced unexplained gaps from an average of 1.4 to 0.8 per genome across 206 prototrophic prokaryotes, with many remaining gaps involving phosphate-group-related steps (price2024improvingtheannotation pages 16-19). For methionine specifically, GapMind handles split MetE proteins (folate-binding and catalytic halves found in halophilic/thermophilic archaea) and three-protein split MetH systems (price2024improvingtheannotation pages 16-19, price2020gapmindautomatedannotation pages 4-7). Ramoneda et al. (2023) applied GapMind to 26,277 bacterial genomes and found that 78.4% of taxa are predicted to synthesize all amino acids, with auxotrophies more prevalent in obligate intracellular parasites and streamlined genomes.

## 8. Controversies and Open Questions

Several unresolved issues persist in the field:

**1. Methyl donor for MesD:** The MesD/MesX system, found only in aerobic bacteria, does not use 5-methyl-THF, cobalamin, or any known methyl carrier. The actual methyl donor remains unidentified, though it is hypothesized to derive from central metabolism via an oxygen-dependent mechanism (price2021fourfamiliesof pages 12-15, price2021fourfamiliesof pages 15-18).

**2. Remaining pathway gaps:** Even with the latest GapMind 2024 database, many prototrophic organisms have unexplained gaps in methionine (and other amino acid) biosynthesis, suggesting the existence of as-yet-undiscovered enzyme families or non-orthologous replacements (price2024improvingtheannotation pages 16-19, price2020gapmindautomatedannotation pages 1-2).

**3. Nomenclatural confusion:** The gene name "metB" refers to cystathionine γ-synthase in *E. coli* but to homoserine O-acetyltransferase in *B. subtilis*. Similarly, "metX" has been used for both acyltransferases and sulfhydrylases in different organisms. This non-standardized nomenclature complicates cross-species comparisons (rodionov2004comparativegenomicsof pages 1-2, rodionov2004comparativegenomicsof pages 7-7).

**4. Overgeneralization from model organisms:** Much of the mechanistic understanding derives from *E. coli*, *B. subtilis*, and *S. cerevisiae*. The diversity of regulatory systems—from protein repressors (MetJ, McbR) to RNA switches (S-box, T-box, SAM-II) to post-transcriptional mechanisms (plant CGS mRNA regulation)—cautions against extrapolating regulatory logic from one lineage to another (rodionov2004comparativegenomicsof pages 11-11, leyn2014comparativegenomicsof pages 1-2, chen2025theyangcycle pages 2-3).

**5. Deep evolutionary origins:** The presence of non-homologous isofunctional enzymes at every pathway step suggests that the "pathway" as a logical module may predate any particular set of enzyme genes. Whether the acylation-then-sulfhydrylation logic is more ancient than the trans-sulfuration route, or vice versa, remains unresolved (sekowska2004bacterialvariationson pages 1-2, price2021fourfamiliesof pages 1-4, rodionov2004comparativegenomicsof pages 7-7).

**6. Drug target potential:** In *M. tuberculosis*, methionine biosynthesis has emerged as a promising drug target because the pathway is absent from the human host. Deletion of metA/metX renders MTB unable to replicate in macrophages, and several MetAP inhibitors show activity against drug-resistant strains (sari2024theroleof pages 1-2, sari2024theroleof pages 2-3). However, the feasibility of targeting specific pathway enzymes without affecting human metabolism requires further validation.

## 9. Key References

1. Thomas, D. & Surdin-Kerjan, Y. (1997). Metabolism of sulfur amino acids in *Saccharomyces cerevisiae*. *Microbiology and Molecular Biology Reviews*, 61, 503–532. DOI: 10.1128/mmbr.61.4.503-532.1997

2. Rodionov, D. et al. (2004). Comparative genomics of the methionine metabolism in Gram-positive bacteria: a variety of regulatory systems. *Nucleic Acids Research*, 32, 3340–3353. DOI: 10.1093/nar/gkh659

3. Leyn, S.A. et al. (2014). Comparative genomics of transcriptional regulation of methionine metabolism in Proteobacteria. *PLoS ONE*, 9, e113714. DOI: 10.1371/journal.pone.0113714

4. Price, M.N. et al. (2020). GapMind: Automated annotation of amino acid biosynthesis. *mSystems*, 5, e00291-20. DOI: 10.1128/msystems.00291-20

5. Price, M.N. et al. (2021). Four families of folate-independent methionine synthases. *bioRxiv*. DOI: 10.1101/2020.04.21.054031

6. Augustus, A.M. & Spicer, L.D. (2011). The MetJ regulon in gammaproteobacteria determined by comparative genomics methods. *BMC Genomics*, 12, 558. DOI: 10.1186/1471-2164-12-558

7. Price, M.N. et al. (2024). Improving the annotation of amino acid biosynthesis pathways: GapMind 2024. *bioRxiv*. DOI: 10.1101/2024.10.14.618325

8. Sari, P.S. et al. (2024). The role of methionine in tuberculosis and its potential clinical significance. *Indonesia Journal of Biomedical Science*, 18, 45–51. DOI: 10.15562/ijbs.v18i1.534

9. Watanabe, M. et al. (2021). Metabolism and regulatory functions of O-acetylserine, S-adenosylmethionine, homocysteine, and serine in plant development and environmental responses. *Frontiers in Plant Science*, 12. DOI: 10.3389/fpls.2021.643403

10. Chen, H. et al. (2025). The Yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. *Plant Hormones*, 1. DOI: 10.48130/ph-0025-0007

11. Devi, V. et al. (2023). Genetic and molecular understanding for the development of methionine-rich maize: a holistic approach. *Frontiers in Plant Science*, 14. DOI: 10.3389/fpls.2023.1249230

12. Ramoneda, J. et al. (2023). Taxonomic and environmental distribution of bacterial amino acid auxotrophies. *Nature Communications*, 14. DOI: 10.1038/s41467-023-43435-4

References

1. (augustus2011themetjregulon pages 7-8): Anne M Augustus and Leonard D Spicer. The metj regulon in gammaproteobacteria determined by comparative genomics methods. BMC Genomics, 12:558-558, Nov 2011. URL: https://doi.org/10.1186/1471-2164-12-558, doi:10.1186/1471-2164-12-558. This article has 29 citations and is from a peer-reviewed journal.

2. (price2021fourfamiliesof pages 1-4): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Four families of folate-independent methionine synthases. bioRxiv, Apr 2021. URL: https://doi.org/10.1101/2020.04.21.054031, doi:10.1101/2020.04.21.054031. This article has 29 citations.

3. (price2020gapmindautomatedannotation pages 1-2): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Gapmind: automated annotation of amino acid biosynthesis. Jun 2020. URL: https://doi.org/10.1128/msystems.00291-20, doi:10.1128/msystems.00291-20. This article has 83 citations and is from a peer-reviewed journal.

4. (price2020gapmindautomatedannotation pages 2-4): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Gapmind: automated annotation of amino acid biosynthesis. Jun 2020. URL: https://doi.org/10.1128/msystems.00291-20, doi:10.1128/msystems.00291-20. This article has 83 citations and is from a peer-reviewed journal.

5. (chen2025theyangcycle pages 2-3): Huixin Chen, Ziyi Zhao, Jiawen Chen, Jana Mertens, Bram Van de Poel, Dongdong Li, and Kunsong Chen. The yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. Plant Hormones, 1:0-0, Jan 2025. URL: https://doi.org/10.48130/ph-0025-0007, doi:10.48130/ph-0025-0007. This article has 8 citations.

6. (watanabe2021metabolismandregulatory pages 3-5): Mutsumi Watanabe, Yukako Chiba, and Masami Yokota Hirai. Metabolism and regulatory functions of o-acetylserine, s-adenosylmethionine, homocysteine, and serine in plant development and environmental responses. Frontiers in Plant Science, May 2021. URL: https://doi.org/10.3389/fpls.2021.643403, doi:10.3389/fpls.2021.643403. This article has 99 citations.

7. (watanabe2021metabolismandregulatory pages 5-6): Mutsumi Watanabe, Yukako Chiba, and Masami Yokota Hirai. Metabolism and regulatory functions of o-acetylserine, s-adenosylmethionine, homocysteine, and serine in plant development and environmental responses. Frontiers in Plant Science, May 2021. URL: https://doi.org/10.3389/fpls.2021.643403, doi:10.3389/fpls.2021.643403. This article has 99 citations.

8. (rodionov2004comparativegenomicsof pages 2-3): D. Rodionov, A. Vitreschak, A. Mironov, and M. Gelfand. Comparative genomics of the methionine metabolism in gram-positive bacteria: a variety of regulatory systems. Nucleic acids research, 32 11:3340-53, Jun 2004. URL: https://doi.org/10.1093/nar/gkh659, doi:10.1093/nar/gkh659. This article has 224 citations and is from a highest quality peer-reviewed journal.

9. (sekowska2004bacterialvariationson pages 1-2): Agnieszka Sekowska, Valérie Dénervaud, Hiroki Ashida, Karine Michoud, Dieter Haas, Akiho Yokota, and Antoine Danchin. Bacterial variations on the methionine salvage pathway. BMC Microbiology, Mar 2004. URL: https://doi.org/10.1186/1471-2180-4-9, doi:10.1186/1471-2180-4-9. This article has 204 citations and is from a peer-reviewed journal.

10. (rodionov2004comparativegenomicsof pages 8-9): D. Rodionov, A. Vitreschak, A. Mironov, and M. Gelfand. Comparative genomics of the methionine metabolism in gram-positive bacteria: a variety of regulatory systems. Nucleic acids research, 32 11:3340-53, Jun 2004. URL: https://doi.org/10.1093/nar/gkh659, doi:10.1093/nar/gkh659. This article has 224 citations and is from a highest quality peer-reviewed journal.

11. (thomas1997metabolismofsulfur pages 11-12): Dominique Thomas and Y. Surdin-Kerjan. Metabolism of sulfur amino acids in saccharomyces cerevisiae. Microbiology and Molecular Biology Reviews, 61:503-532, Dec 1997. URL: https://doi.org/10.1128/mmbr.61.4.503-532.1997, doi:10.1128/mmbr.61.4.503-532.1997. This article has 942 citations and is from a domain leading peer-reviewed journal.

12. (devi2023geneticandmolecular pages 4-6): Veena Devi, Bharat Bhushan, Mamta Gupta, Mehak Sethi, Charanjeet Kaur, Alla Singh, Vishal Singh, Ramesh Kumar, Sujay Rakshit, and Dharam P. Chaudhary. Genetic and molecular understanding for the development of methionine-rich maize: a holistic approach. Frontiers in Plant Science, Sep 2023. URL: https://doi.org/10.3389/fpls.2023.1249230, doi:10.3389/fpls.2023.1249230. This article has 18 citations.

13. (rodionov2004comparativegenomicsof pages 1-2): D. Rodionov, A. Vitreschak, A. Mironov, and M. Gelfand. Comparative genomics of the methionine metabolism in gram-positive bacteria: a variety of regulatory systems. Nucleic acids research, 32 11:3340-53, Jun 2004. URL: https://doi.org/10.1093/nar/gkh659, doi:10.1093/nar/gkh659. This article has 224 citations and is from a highest quality peer-reviewed journal.

14. (rodionov2004comparativegenomicsof pages 7-7): D. Rodionov, A. Vitreschak, A. Mironov, and M. Gelfand. Comparative genomics of the methionine metabolism in gram-positive bacteria: a variety of regulatory systems. Nucleic acids research, 32 11:3340-53, Jun 2004. URL: https://doi.org/10.1093/nar/gkh659, doi:10.1093/nar/gkh659. This article has 224 citations and is from a highest quality peer-reviewed journal.

15. (sari2024theroleof pages 1-2): Putu Suwita Sari, Mas Rizky A A Syamsunarno, and Lidya Chaidir. The role of methionine in tuberculosis and its potential clinical significance. Indonesia Journal of Biomedical Science, 18:45-51, Feb 2024. URL: https://doi.org/10.15562/ijbs.v18i1.534, doi:10.15562/ijbs.v18i1.534. This article has 0 citations.

16. (sari2024theroleof pages 2-3): Putu Suwita Sari, Mas Rizky A A Syamsunarno, and Lidya Chaidir. The role of methionine in tuberculosis and its potential clinical significance. Indonesia Journal of Biomedical Science, 18:45-51, Feb 2024. URL: https://doi.org/10.15562/ijbs.v18i1.534, doi:10.15562/ijbs.v18i1.534. This article has 0 citations.

17. (thomas1997metabolismofsulfur pages 10-11): Dominique Thomas and Y. Surdin-Kerjan. Metabolism of sulfur amino acids in saccharomyces cerevisiae. Microbiology and Molecular Biology Reviews, 61:503-532, Dec 1997. URL: https://doi.org/10.1128/mmbr.61.4.503-532.1997, doi:10.1128/mmbr.61.4.503-532.1997. This article has 942 citations and is from a domain leading peer-reviewed journal.

18. (price2020gapmindautomatedannotation pages 4-7): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Gapmind: automated annotation of amino acid biosynthesis. Jun 2020. URL: https://doi.org/10.1128/msystems.00291-20, doi:10.1128/msystems.00291-20. This article has 83 citations and is from a peer-reviewed journal.

19. (sari2024theroleof pages 3-4): Putu Suwita Sari, Mas Rizky A A Syamsunarno, and Lidya Chaidir. The role of methionine in tuberculosis and its potential clinical significance. Indonesia Journal of Biomedical Science, 18:45-51, Feb 2024. URL: https://doi.org/10.15562/ijbs.v18i1.534, doi:10.15562/ijbs.v18i1.534. This article has 0 citations.

20. (price2021fourfamiliesof pages 12-15): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Four families of folate-independent methionine synthases. bioRxiv, Apr 2021. URL: https://doi.org/10.1101/2020.04.21.054031, doi:10.1101/2020.04.21.054031. This article has 29 citations.

21. (price2021fourfamiliesof pages 15-18): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Four families of folate-independent methionine synthases. bioRxiv, Apr 2021. URL: https://doi.org/10.1101/2020.04.21.054031, doi:10.1101/2020.04.21.054031. This article has 29 citations.

22. (price2021fourfamiliesof pages 9-12): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Four families of folate-independent methionine synthases. bioRxiv, Apr 2021. URL: https://doi.org/10.1101/2020.04.21.054031, doi:10.1101/2020.04.21.054031. This article has 29 citations.

23. (leyn2014comparativegenomicsof pages 2-3): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

24. (thomas1997metabolismofsulfur pages 4-5): Dominique Thomas and Y. Surdin-Kerjan. Metabolism of sulfur amino acids in saccharomyces cerevisiae. Microbiology and Molecular Biology Reviews, 61:503-532, Dec 1997. URL: https://doi.org/10.1128/mmbr.61.4.503-532.1997, doi:10.1128/mmbr.61.4.503-532.1997. This article has 942 citations and is from a domain leading peer-reviewed journal.

25. (price2021fourfamiliesof pages 4-7): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Four families of folate-independent methionine synthases. bioRxiv, Apr 2021. URL: https://doi.org/10.1101/2020.04.21.054031, doi:10.1101/2020.04.21.054031. This article has 29 citations.

26. (price2021fourfamiliesof pages 7-9): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Four families of folate-independent methionine synthases. bioRxiv, Apr 2021. URL: https://doi.org/10.1101/2020.04.21.054031, doi:10.1101/2020.04.21.054031. This article has 29 citations.

27. (rodionov2004comparativegenomicsof pages 11-11): D. Rodionov, A. Vitreschak, A. Mironov, and M. Gelfand. Comparative genomics of the methionine metabolism in gram-positive bacteria: a variety of regulatory systems. Nucleic acids research, 32 11:3340-53, Jun 2004. URL: https://doi.org/10.1093/nar/gkh659, doi:10.1093/nar/gkh659. This article has 224 citations and is from a highest quality peer-reviewed journal.

28. (leyn2014comparativegenomicsof pages 11-11): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

29. (thomas1997metabolismofsulfur pages 1-4): Dominique Thomas and Y. Surdin-Kerjan. Metabolism of sulfur amino acids in saccharomyces cerevisiae. Microbiology and Molecular Biology Reviews, 61:503-532, Dec 1997. URL: https://doi.org/10.1128/mmbr.61.4.503-532.1997, doi:10.1128/mmbr.61.4.503-532.1997. This article has 942 citations and is from a domain leading peer-reviewed journal.

30. (hell2008sulfurmetabolismin pages 139-140): R. Hell, C. Dahl, D. Knaff, and T. Leustek. Sulfur metabolism in phototrophic organisms. ArXiv, Jan 2008. URL: https://doi.org/10.1007/978-1-4020-6863-8, doi:10.1007/978-1-4020-6863-8. This article has 33 citations.

31. (price2020gapmindautomatedannotation pages 16-17): Morgan N. Price, Adam M. Deutschbauer, and Adam P. Arkin. Gapmind: automated annotation of amino acid biosynthesis. Jun 2020. URL: https://doi.org/10.1128/msystems.00291-20, doi:10.1128/msystems.00291-20. This article has 83 citations and is from a peer-reviewed journal.

32. (leyn2014comparativegenomicsof pages 1-2): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

33. (leyn2014comparativegenomicsof pages 10-11): Semen A. Leyn, Inna A. Suvorova, Tatiana D. Kholina, Sofia S. Sherstneva, Pavel S. Novichkov, Mikhail S. Gelfand, and Dmitry A. Rodionov. Comparative genomics of transcriptional regulation of methionine metabolism in proteobacteria. PLoS ONE, 9:e113714, Nov 2014. URL: https://doi.org/10.1371/journal.pone.0113714, doi:10.1371/journal.pone.0113714. This article has 37 citations and is from a peer-reviewed journal.

34. (price2024interactivetoolsfor pages 9-10): Morgan N Price and Adam P Arkin. Interactive tools for functional annotation of bacterial genomes. Database: The Journal of Biological Databases and Curation, Apr 2024. URL: https://doi.org/10.1093/database/baae089, doi:10.1093/database/baae089. This article has 6 citations.

35. (price2024improvingtheannotation pages 16-19): Morgan N. Price, Anthony L. Shiver, Leslie A. Day, Marta Torres, Hira P. Lesea, Trenton K. Owens, Adam M. Deutschbauer, and Adam P. Arkin. Improving the annotation of amino acid biosynthesis pathways: gapmind 2024. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.14.618325, doi:10.1101/2024.10.14.618325. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](methionine_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](methionine_biosynthesis-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. price2020gapmindautomatedannotation pages 1-2
2. watanabe2021metabolismandregulatory pages 3-5
3. rodionov2004comparativegenomicsof pages 7-7
4. thomas1997metabolismofsulfur pages 10-11
5. rodionov2004comparativegenomicsof pages 1-2
6. price2020gapmindautomatedannotation pages 4-7
7. sari2024theroleof pages 3-4
8. price2021fourfamiliesof pages 1-4
9. chen2025theyangcycle pages 2-3
10. thomas1997metabolismofsulfur pages 1-4
11. price2021fourfamiliesof pages 4-7
12. price2020gapmindautomatedannotation pages 16-17
13. augustus2011themetjregulon pages 7-8
14. rodionov2004comparativegenomicsof pages 11-11
15. leyn2014comparativegenomicsof pages 2-3
16. leyn2014comparativegenomicsof pages 11-11
17. price2024improvingtheannotation pages 16-19
18. price2020gapmindautomatedannotation pages 2-4
19. watanabe2021metabolismandregulatory pages 5-6
20. rodionov2004comparativegenomicsof pages 2-3
21. sekowska2004bacterialvariationson pages 1-2
22. rodionov2004comparativegenomicsof pages 8-9
23. thomas1997metabolismofsulfur pages 11-12
24. devi2023geneticandmolecular pages 4-6
25. sari2024theroleof pages 1-2
26. sari2024theroleof pages 2-3
27. price2021fourfamiliesof pages 12-15
28. price2021fourfamiliesof pages 15-18
29. price2021fourfamiliesof pages 9-12
30. thomas1997metabolismofsulfur pages 4-5
31. price2021fourfamiliesof pages 7-9
32. hell2008sulfurmetabolismin pages 139-140
33. leyn2014comparativegenomicsof pages 1-2
34. leyn2014comparativegenomicsof pages 10-11
35. price2024interactivetoolsfor pages 9-10
36. https://doi.org/10.1186/1471-2164-12-558,
37. https://doi.org/10.1101/2020.04.21.054031,
38. https://doi.org/10.1128/msystems.00291-20,
39. https://doi.org/10.48130/ph-0025-0007,
40. https://doi.org/10.3389/fpls.2021.643403,
41. https://doi.org/10.1093/nar/gkh659,
42. https://doi.org/10.1186/1471-2180-4-9,
43. https://doi.org/10.1128/mmbr.61.4.503-532.1997,
44. https://doi.org/10.3389/fpls.2023.1249230,
45. https://doi.org/10.15562/ijbs.v18i1.534,
46. https://doi.org/10.1371/journal.pone.0113714,
47. https://doi.org/10.1007/978-1-4020-6863-8,
48. https://doi.org/10.1093/database/baae089,
49. https://doi.org/10.1101/2024.10.14.618325,