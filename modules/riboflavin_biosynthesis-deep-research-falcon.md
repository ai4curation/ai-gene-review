---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T02:40:43.711209'
end_time: '2026-07-07T03:11:46.805157'
duration_seconds: 1863.09
template_file: templates/module_research.md.j2
template_variables:
  module_title: Riboflavin biosynthesis
  module_summary: A bacterial riboflavin, FMN, and FAD biosynthesis module covering
    conversion of GTP and ribulose 5-phosphate into riboflavin, followed by phosphorylation
    and adenylylation to the major flavin cofactors. In Pseudomonas putida KT2440,
    KEGG ppu00740 also includes FMN-dependent side chemistry and broad flavin metabolism
    entries; those are treated as boundary context unless they directly catalyze riboflavin,
    FMN, or FAD formation.
  module_outline: "- Riboflavin biosynthesis\n  - 1. GTP-derived pyrimidine precursor\
    \ formation\n  - GTP cyclohydrolase II step\n    - RibA GTP cyclohydrolase II\
    \ (molecular player: PSEPK ribA; activity or role: GTP cyclohydrolase II activity)\n\
    \    - RibAB-I GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-I;\
    \ activity or role: GTP cyclohydrolase II activity)\n    - RibAB-II GTP cyclohydrolase\
    \ II candidate (molecular player: PSEPK ribAB-II; activity or role: GTP cyclohydrolase\
    \ II activity)\n  - 2. pyrimidine deamination and reduction\n  - RibD deaminase\
    \ and reductase steps\n    - RibD riboflavin-specific deaminase (molecular player:\
    \ PSEPK ribD; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase\
    \ activity)\n    - RibD riboflavin-pathway reductase (molecular player: PSEPK\
    \ ribD; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)\n\
    \  - 3. ribulose-phosphate branch\n  - DHBP synthase step\n    - RibB DHBP synthase\
    \ (molecular player: PSEPK ribB; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate\
    \ synthase activity)\n    - RibAB-I DHBP synthase (molecular player: PSEPK ribAB-I;\
    \ activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)\n\
    \    - RibAB-II DHBP synthase (molecular player: PSEPK ribAB-II; activity or role:\
    \ 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)\n  - 4. lumazine formation\n\
    \  - Lumazine synthase step\n    - RibH lumazine synthase (molecular player: PSEPK\
    \ ribH; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)\n\
    \  - 5. riboflavin formation\n  - Riboflavin synthase step\n    - RibE riboflavin\
    \ synthase (molecular player: PSEPK ribE; activity or role: riboflavin synthase\
    \ activity)\n    - RibC riboflavin synthase candidate (molecular player: PSEPK\
    \ ribC; activity or role: riboflavin synthase activity)\n  - 6. FMN and FAD formation\n\
    \  - Riboflavin phosphorylation and FMN adenylylation\n    - RibF riboflavin kinase\
    \ (molecular player: PSEPK ribF; activity or role: riboflavin kinase activity)\n\
    \    - RibF FMN adenylyltransferase (molecular player: PSEPK ribF; activity or\
    \ role: FMN adenylyltransferase activity)"
  module_connections: No explicit connections.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: riboflavin_biosynthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Commissioned Review Brief

## Review Topic

Riboflavin biosynthesis

## Working Scope

A bacterial riboflavin, FMN, and FAD biosynthesis module covering conversion of GTP and ribulose 5-phosphate into riboflavin, followed by phosphorylation and adenylylation to the major flavin cofactors. In Pseudomonas putida KT2440, KEGG ppu00740 also includes FMN-dependent side chemistry and broad flavin metabolism entries; those are treated as boundary context unless they directly catalyze riboflavin, FMN, or FAD formation.

## Provisional Biological Outline

- Riboflavin biosynthesis
  - 1. GTP-derived pyrimidine precursor formation
  - GTP cyclohydrolase II step
    - RibA GTP cyclohydrolase II (molecular player: PSEPK ribA; activity or role: GTP cyclohydrolase II activity)
    - RibAB-I GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-I; activity or role: GTP cyclohydrolase II activity)
    - RibAB-II GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-II; activity or role: GTP cyclohydrolase II activity)
  - 2. pyrimidine deamination and reduction
  - RibD deaminase and reductase steps
    - RibD riboflavin-specific deaminase (molecular player: PSEPK ribD; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase activity)
    - RibD riboflavin-pathway reductase (molecular player: PSEPK ribD; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)
  - 3. ribulose-phosphate branch
  - DHBP synthase step
    - RibB DHBP synthase (molecular player: PSEPK ribB; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-I DHBP synthase (molecular player: PSEPK ribAB-I; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-II DHBP synthase (molecular player: PSEPK ribAB-II; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
  - 4. lumazine formation
  - Lumazine synthase step
    - RibH lumazine synthase (molecular player: PSEPK ribH; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)
  - 5. riboflavin formation
  - Riboflavin synthase step
    - RibE riboflavin synthase (molecular player: PSEPK ribE; activity or role: riboflavin synthase activity)
    - RibC riboflavin synthase candidate (molecular player: PSEPK ribC; activity or role: riboflavin synthase activity)
  - 6. FMN and FAD formation
  - Riboflavin phosphorylation and FMN adenylylation
    - RibF riboflavin kinase (molecular player: PSEPK ribF; activity or role: riboflavin kinase activity)
    - RibF FMN adenylyltransferase (molecular player: PSEPK ribF; activity or role: FMN adenylyltransferase activity)

## Known Relationships Among Steps

No explicit connections.

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

Riboflavin biosynthesis

## Working Scope

A bacterial riboflavin, FMN, and FAD biosynthesis module covering conversion of GTP and ribulose 5-phosphate into riboflavin, followed by phosphorylation and adenylylation to the major flavin cofactors. In Pseudomonas putida KT2440, KEGG ppu00740 also includes FMN-dependent side chemistry and broad flavin metabolism entries; those are treated as boundary context unless they directly catalyze riboflavin, FMN, or FAD formation.

## Provisional Biological Outline

- Riboflavin biosynthesis
  - 1. GTP-derived pyrimidine precursor formation
  - GTP cyclohydrolase II step
    - RibA GTP cyclohydrolase II (molecular player: PSEPK ribA; activity or role: GTP cyclohydrolase II activity)
    - RibAB-I GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-I; activity or role: GTP cyclohydrolase II activity)
    - RibAB-II GTP cyclohydrolase II candidate (molecular player: PSEPK ribAB-II; activity or role: GTP cyclohydrolase II activity)
  - 2. pyrimidine deamination and reduction
  - RibD deaminase and reductase steps
    - RibD riboflavin-specific deaminase (molecular player: PSEPK ribD; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase activity)
    - RibD riboflavin-pathway reductase (molecular player: PSEPK ribD; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)
  - 3. ribulose-phosphate branch
  - DHBP synthase step
    - RibB DHBP synthase (molecular player: PSEPK ribB; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-I DHBP synthase (molecular player: PSEPK ribAB-I; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
    - RibAB-II DHBP synthase (molecular player: PSEPK ribAB-II; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
  - 4. lumazine formation
  - Lumazine synthase step
    - RibH lumazine synthase (molecular player: PSEPK ribH; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)
  - 5. riboflavin formation
  - Riboflavin synthase step
    - RibE riboflavin synthase (molecular player: PSEPK ribE; activity or role: riboflavin synthase activity)
    - RibC riboflavin synthase candidate (molecular player: PSEPK ribC; activity or role: riboflavin synthase activity)
  - 6. FMN and FAD formation
  - Riboflavin phosphorylation and FMN adenylylation
    - RibF riboflavin kinase (molecular player: PSEPK ribF; activity or role: riboflavin kinase activity)
    - RibF FMN adenylyltransferase (molecular player: PSEPK ribF; activity or role: FMN adenylyltransferase activity)

## Known Relationships Among Steps

No explicit connections.

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

# Bacterial Riboflavin, FMN, and FAD Biosynthesis: A Review-Style Synthesis

## 1. Executive Summary

Riboflavin (vitamin B2) biosynthesis is one of the most highly conserved metabolic modules in biology, converting two primary metabolites—GTP and ribulose-5-phosphate (Ru5P)—into the isoalloxazine ring system of riboflavin through a series of six to seven obligatory enzymatic steps. Riboflavin is subsequently phosphorylated to flavin mononucleotide (FMN) and adenylylated to flavin adenine dinucleotide (FAD), the two major flavin cofactors required by hundreds of cellular oxidoreductases. The pathway is present in most bacteria, archaea, fungi, and plants, but is absent in vertebrates, which must obtain riboflavin from dietary sources (jimeneznava2026biosynthesisregulationand pages 4-6, ruchala2025regulationofriboflavin pages 2-4). In bacteria, the biosynthetic genes are variably organized—clustered in operons in Gram-positive species and dispersed across the chromosome in many Gram-negative species—and are regulated primarily by FMN-responsive riboswitches (jimeneznava2026biosynthesisregulationand pages 19-20, ruchala2025regulationofriboflavin pages 9-11). In the context of *Pseudomonas putida* KT2440, the KEGG module ppu00740 encompasses the core riboflavin pathway enzymes as well as the downstream FMN/FAD-forming steps, with multiple annotated paralogs (e.g., ribAB-I, ribAB-II) reflecting the gene duplication patterns common in Gammaproteobacteria.

This review anchors its analysis in the bacterial pathway as exemplified by model organisms (*Bacillus subtilis*, *Escherichia coli*, *Pseudomonas* spp.) while addressing evolutionary variation across major lineages, emerging structural and regulatory insights, and current controversies.

---

## 2. Definition and Biological Boundaries

### What is included

The riboflavin biosynthesis module sensu stricto encompasses the conversion of GTP and Ru5P into riboflavin through two converging branches (the "GTP branch" and the "Ru5P branch"), followed by the phosphorylation of riboflavin to FMN and adenylylation of FMN to FAD (jimeneznava2026biosynthesisregulationand pages 4-6, rodionova2017anovelbifunctional pages 2-3). In *P. putida* KT2440, the core module is defined by the enzymes RibA (GTP cyclohydrolase II), RibB (3,4-dihydroxy-2-butanone-4-phosphate [DHBP] synthase), RibD (bifunctional deaminase/reductase), RibH (lumazine synthase), RibE (riboflavin synthase), and RibF (bifunctional riboflavin kinase/FMN adenylyltransferase), along with bifunctional RibAB fusion variants.

### What should be treated separately

Several processes frequently annotated under broad "flavin metabolism" headings fall outside the core biosynthetic module:

- **FMN-dependent enzymatic side reactions**: Flavoprotein oxidoreductases that use FMN or FAD as cofactors are consumers of the pathway's products, not participants in biosynthesis itself.
- **Riboflavin transport**: Dedicated importers such as RibU in *B. subtilis* or ECF-type transporters mediate riboflavin uptake; they are regulated alongside biosynthetic genes but are mechanistically separate (hubenthal2024influenceofantimicrobial pages 29-31, hubenthal2024influenceofantimicrobial pages 31-34).
- **Roseoflavin and 8-aminoriboflavin biosynthesis**: These specialized flavin analogs, produced by organisms such as *Streptomyces davawensis*, branch from the core pathway but involve additional dedicated enzymes.
- **MAIT cell ligand chemistry**: The riboflavin precursor 5-A-RU (5-amino-6-ribitylamino-2,4(1H,3H)-pyrimidinedione) reacts non-enzymatically with methylglyoxal to form potent activators of mucosal-associated invariant T (MAIT) cells, a process of immunological significance but not a catalyzed biosynthetic step (chengalroyen2024modulationofriboflavin pages 1-2).

### Nomenclature caveats

A persistent source of confusion in the literature is the divergent gene nomenclature between *B. subtilis* and *E. coli*. In older *B. subtilis* literature, *ribB* encodes riboflavin synthase (the terminal step), while in *E. coli* and modern cross-species nomenclature, *ribB* encodes DHBP synthase and *ribE* denotes riboflavin synthase (rodionova2017anovelbifunctional pages 2-3, jimeneznava2026biosynthesisregulationand pages 19-20). Similarly, the bifunctional deaminase/reductase is *ribG* in *B. subtilis* but *ribD* in *E. coli* (liu2023metabolicengineeringof pages 3-4, hubenthal2024influenceofantimicrobial pages 29-31). The bifunctional kinase/FAD synthetase is *ribC* (or *ribFC*) in *B. subtilis* but *ribF* in Gram-negative bacteria (jimeneznava2026biosynthesisregulationand pages 19-20).

---

## 3. Mechanistic Overview

The pathway comprises two converging branches feeding into a terminal condensation-dismutation sequence:

### 3.1 GTP Branch (Pyrimidine Precursor Formation)

**Step 1: GTP cyclohydrolase II (RibA; EC 3.5.4.25).** The committed step of riboflavin biosynthesis involves hydrolytic opening of the imidazole ring of GTP, releasing formate and pyrophosphate to yield 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5′-phosphate (DARPP) (liu2023metabolicengineeringof pages 3-4, jimeneznava2026biosynthesisregulationand pages 4-6). This is a zinc-dependent metalloenzyme and is widely regarded as the rate-limiting step of the pathway (liu2023metabolicengineeringof pages 9-11).

**Step 2: Deamination (EC 3.5.4.26).** DARPP is deaminated to 5-amino-6-ribosylamino-2,4(1H,3H)-pyrimidinedione 5′-phosphate (ARPP). In bacteria, this reaction is catalyzed by the deaminase domain of the bifunctional RibD (or RibG in *B. subtilis*) (rodionova2017anovelbifunctional pages 2-3, ruchala2025regulationofriboflavin pages 4-5).

**Step 3: Reduction (EC 1.1.1.193).** ARPP is reduced using NADPH (or NADH) to yield 5-amino-6-ribitylamino-2,4(1H,3H)-pyrimidinedione 5′-phosphate (ArPP) by the reductase domain of RibD/RibG (liu2023metabolicengineeringof pages 3-4, rodionova2017anovelbifunctional pages 2-3).

**Step 4: Dephosphorylation.** ArPP is dephosphorylated to ArP. The phosphatase responsible for this step has historically been poorly characterized and was only recently identified in some organisms (jimeneznava2026biosynthesisregulationand pages 4-6).

A critical lineage-specific variation occurs at steps 2–3: in eubacteria, DARPP is first deaminated then reduced, whereas in archaea, fungi, and yeasts the order is reversed—DARPP is first reduced to DArPP, then deaminated to ArPP (ruchala2025regulationofriboflavin pages 4-5, jimeneznava2026biosynthesisregulationand pages 4-6).

### 3.2 Ribulose-5-Phosphate Branch

**Step 5: DHBP synthase (RibB; EC 4.1.99.12).** Ru5P is converted to 3,4-dihydroxy-2-butanone-4-phosphate (DHBP) in a complex skeletal rearrangement with loss of C-4 as formate. This step supplies the four-carbon unit that ultimately forms the xylene ring of the isoalloxazine system (jimeneznava2026biosynthesisregulationand pages 4-6, rodionova2017anovelbifunctional pages 2-3).

### 3.3 Convergence and Ring Formation

**Step 6: Lumazine synthase (RibH; EC 2.5.1.78).** ArP and DHBP are condensed to form 6,7-dimethyl-8-ribityllumazine (DMRL). The reaction involves Schiff base formation between the 5-amino group of ArP and the carbonyl of DHBP, followed by dephosphorylation and ring closure (liu2023metabolicengineeringof pages 4-5, ladenstein2020secondcareerof pages 2-3).

**Step 7: Riboflavin synthase (RibE; EC 2.5.1.9).** In the final and chemically remarkable step, two molecules of DMRL undergo a dismutation reaction: a four-carbon unit is transferred from one lumazine to another, yielding one molecule of riboflavin and regenerating one molecule of ArP (which re-enters Step 6). This reaction effectively recycles half of the pyrimidine intermediates (ruchala2025regulationofriboflavin pages 5-7, liu2023metabolicengineeringof pages 4-5).

### 3.4 Cofactor Activation

**Step 8: Riboflavin kinase (EC 2.7.1.26).** Riboflavin is phosphorylated at the ribityl 5′-hydroxyl to form FMN.

**Step 9: FMN adenylyltransferase (EC 2.7.7.2).** FMN is adenylylated with ATP to form FAD.

In most bacteria, both activities reside in the bifunctional enzyme RibF (Gram-negative) or RibC/RibFC (Gram-positive), with the N-terminal FMNAT domain and C-terminal RFK domain facilitating direct channeling of FMN between catalytic sites (ruchala2025regulationofriboflavin pages 5-7, rodionova2017anovelbifunctional pages 2-3, anoz‐carbonell2020humanriboflavinkinase pages 14-15).

---

## 4. Major Molecular Players and Active Assemblies

The following table summarizes the core enzymes, their nomenclature variants, and key functional features:

| Step | Common bacterial enzyme / family | Typical Gram-negative / *E. coli*-style name | Typical Gram-positive / *B. subtilis*-style equivalent | EC number(s) | Enzymatic activity | Reaction catalyzed | Key structural / functional notes |
|---|---|---|---|---|---|---|---|
| 1 | GTP cyclohydrolase II | **RibA** | **RibA** activity often resides in bifunctional **RibAB** / RibA-type protein; in older *B. subtilis* literature pathway names can differ | 3.5.4.25 | GTP cyclohydrolase II | GTP → pyrimidine precursor DARPP + formate/pyrophosphate-derived products in the committed upper branch of riboflavin biosynthesis | Obligatory first committed step of the canonical bacterial pathway; in many bacteria this activity is fused with DHBP synthase in a bifunctional enzyme; in plants and many Gram-positive systems the GTPCHII and DHBPS domains occur in one polypeptide; multiple paralogs can occur in some lineages (rodionova2017anovelbifunctional pages 2-3, jimeneznava2026biosynthesisregulationand pages 4-6, chengalroyen2024modulationofriboflavin pages 7-10) |
| 2 | Diaminohydroxyphosphoribosylaminopyrimidine deaminase / reductase | **RibD** | Functionally equivalent to bifunctional **RibG** in *B. subtilis* nomenclature | 3.5.4.26; 1.1.1.193 | Deamination of DARPP-derived intermediate and reduction of the ribosyl side chain intermediate | In eubacteria, DARPP is typically deaminated to ARPP and then reduced to ArPP by the bifunctional enzyme family represented by RibD/RibG | Central branch-processing enzyme; order of deamination and reduction is lineage-specific—bacteria generally deaminate then reduce, whereas archaea/fungi/plants often reduce then deaminate; this step is therefore a major boundary marker between bacterial and archaeal/eukaryotic pathway variants (rodionova2017anovelbifunctional pages 2-3, ruchala2025regulationofriboflavin pages 4-5, jimeneznava2026biosynthesisregulationand pages 4-6) |
| 3 | 3,4-Dihydroxy-2-butanone-4-phosphate synthase | **RibB** | DHBPS activity often resides in bifunctional **RibAB** / RibA-type protein in *B. subtilis* and plants | 4.1.99.12 | DHBP synthase | Ribulose-5-phosphate → 3,4-dihydroxy-2-butanone-4-phosphate (DHBP) | Obligatory lower-branch precursor-forming step from pentose phosphate metabolism; can be monofunctional (RibB) or fused with GTPCHII in RibAB/RibA-type proteins; stress-adapted paralogs exist, e.g. Acinetobacter RibBX, a RibB fusion protein important under zinc limitation and calprotectin stress (rodionova2017anovelbifunctional pages 2-3, wang2019multimetalrestrictionby pages 6-7, wang2019multimetalrestrictionby pages 7-8) |
| 4 | Bifunctional GTP cyclohydrolase II / DHBP synthase | **RibAB** (or RibBA in some bacteria) | **RibA**-type bifunctional protein in *B. subtilis* / plants; operon context varies | 3.5.4.25 + 4.1.99.12 | Combines step 1 and step 3 activities in one polypeptide | GTP → DARPP and ribulose-5-phosphate → DHBP | Common solution in many bacteria and in plastid/plant pathways; usually contains N-terminal DHBPS and C-terminal GTPCHII domains; important for pathway flux control and often considered rate-limiting in engineered producers; paralogous RibAB-like proteins may differ in relative activity of the two domains (ruchala2025regulationofriboflavin pages 9-11, jimeneznava2026biosynthesisregulationand pages 4-6, ladenstein2020secondcareerof pages 2-3) |
| 5 | Lumazine synthase | **RibH** | **RibH** | 2.5.1.78 | 6,7-dimethyl-8-ribityllumazine synthase | Condenses ArP (dephosphorylated pyrimidine precursor) + DHBP → 6,7-dimethyl-8-ribityllumazine (DMRL/DRL) | Penultimate pathway step; in some bacteria forms large oligomeric assemblies, including the classic 60-subunit T=1 icosahedral lumazine synthase capsid of *B. subtilis* that can associate with riboflavin synthase; paralog redundancy is documented in mycobacteria, where one species may carry two lumazine synthase-like genes but *M. tuberculosis* retains one essential RibH (liu2023metabolicengineeringof pages 4-5, ladenstein2020secondcareerof pages 2-3, ladenstein2020secondcareerof pages 1-2, chengalroyen2024modulationofriboflavin pages 7-10) |
| 6 | Riboflavin synthase | **RibE** | Often called **RibB** in older *B. subtilis* literature; in newer cross-species nomenclature the enzyme family is RibE | 2.5.1.9 | Riboflavin synthase | 2 × 6,7-dimethyl-8-ribityllumazine → riboflavin + recycled pyrimidine intermediate | Final riboflavin-forming step; catalyzes the characteristic dismutation/C4 transfer between two lumazine molecules; naming is a common source of confusion because older Gram-positive literature, especially for *B. subtilis*, often assigned **ribB** to riboflavin synthase rather than DHBP synthase—modern comparative genomics generally uses RibE for riboflavin synthase and RibB for DHBPS (rodionova2017anovelbifunctional pages 2-3, liu2023metabolicengineeringof pages 4-5, jimeneznava2026biosynthesisregulationand pages 19-20) |
| 7 | Riboflavin kinase / FMN adenylyltransferase (bifunctional FAD synthetase) | **RibF** in many Gram-negative bacteria | **RibC** / RibFC in many Gram-positive bacteria | 2.7.1.26; 2.7.7.2 | Riboflavin kinase and FMN adenylyltransferase | Riboflavin + ATP → FMN; FMN + ATP → FAD | Converts the vitamin product into the major flavin cofactors FMN and FAD; in most bacteria both activities are fused in one bifunctional enzyme, unlike many eukaryotes which use separate monofunctional proteins; bacterial bifunctional enzymes can form architectures that facilitate channeling/transfer of FMN between RFK and FMNAT modules; archaeal systems may instead use separate non-orthologous enzymes such as RibK and RibL (rodionova2017anovelbifunctional pages 2-3, ruchala2025regulationofriboflavin pages 5-7, anoz‐carbonell2020humanriboflavinkinase pages 14-15) |
| 8 | Specialized/accessory variants and recent additions | **RibBX**, **BrbF**, lineage-specific paralogs | Not canonical *B. subtilis* core enzymes | variable | Stress-adapted DHBPS fusion function; formamidase in alternative upper-branch modules | RibBX supports DHBP production/regulation under metal stress; BrbF deformylates AFRPP → DARoPP in an alternative bacterial module linked to invasive Rhizobiales | These are boundary-expanding but biologically important variants rather than universal core steps. RibBX lacks canonical RibA-like zinc-binding residues yet supports flavin sufficiency under Zn limitation in *A. baumannii*. BrbF defines a recently recognized alternative module for riboflavin biosynthesis in invasive bacteria and shows that some bacterial pathways are more diverse than the textbook six- or seven-step scheme implies (wang2019multimetalrestrictionby pages 6-7, wang2019multimetalrestrictionby pages 7-8, yurgel2022anovelformamidase pages 1-3) |
| 9 | Typical gene organization context | **ribA ribB ribD/G ribH ribE ribF** often dispersed in Gram-negatives | **ribDG / ribG-ribB-ribA-ribH-ribT** operon architecture common in *B. subtilis*; FMN/FAD step often **ribC** | n/a | Operon / regulon organization rather than catalytic step | Coordinates transcription of the pathway | Gram-positive bacteria often organize rib genes in a single operon under an FMN riboswitch, whereas Gram-negative bacteria often disperse the genes and regulate only subsets translationally or locally; these organizational differences are useful when mapping orthologs in organisms such as *Pseudomonas putida* KT2440, where multiple candidate paralogs can appear in annotation sets (jimeneznava2026biosynthesisregulationand pages 19-20, ruchala2025regulationofriboflavin pages 9-11, liu2023metabolicengineeringof pages 3-4, hubenthal2024influenceofantimicrobial pages 29-31) |


*Table: This table summarizes the core bacterial enzymes and common variants that convert GTP and ribulose-5-phosphate into riboflavin, FMN, and FAD. It also highlights nomenclature differences between Gram-negative and Gram-positive systems, which are a frequent source of annotation confusion.*

### 4.1 Bifunctional RibAB Fusion Proteins

A hallmark of many bacterial and plant riboflavin pathways is the fusion of GTP cyclohydrolase II and DHBP synthase activities into a single bifunctional polypeptide, typically with an N-terminal DHBPS domain and a C-terminal GTPCHII domain (jimeneznava2026biosynthesisregulationand pages 4-6). In *P. putida* KT2440, two such bifunctional candidates (ribAB-I and ribAB-II) are annotated, reflecting the paralog expansion common in Pseudomonads and other Gammaproteobacteria. The bifunctional arrangement may facilitate metabolic channeling and is considered a rate-limiting control point for pathway flux (liu2023metabolicengineeringof pages 9-11).

### 4.2 The Lumazine Synthase–Riboflavin Synthase Complex

Lumazine synthase (RibH) assembles into remarkable quaternary structures. In *B. subtilis*, 60 identical subunits form a T=1 icosahedral capsid of ~16 nm diameter (~960 kDa), encapsulating a trimeric riboflavin synthase (RibE) in its interior cavity (ladenstein2020secondcareerof pages 2-3, ladenstein2020secondcareerof pages 1-2). Under alkaline conditions, LS can convert to a T=3 capsid with 180 subunits (~29 nm diameter). In fungi and certain bacteria, LS exists instead as pentamers or decamers (ladenstein2020secondcareerof pages 2-3). This encapsulation is thought to enhance substrate channeling between the penultimate and ultimate pathway steps.

### 4.3 RibBX: A Stress-Adapted Paralog

In *Acinetobacter baumannii*, the RibBX protein represents a DHBP synthase fused with a degenerate RibA-like domain (RibX) that has lost all three zinc-coordinating cysteine residues and therefore lacks GTP cyclohydrolase II activity (wang2019multimetalrestrictionby pages 6-7). RibBX retains robust DHBPS activity and is specifically induced under calprotectin-mediated multi-metal restriction. Its RibX domain binds FMN and is allosterically inhibited by it, providing a post-translational regulatory mechanism distinct from the canonical FMN riboswitch that controls *ribB* transcription (wang2019multimetalrestrictionby pages 6-7, wang2019multimetalrestrictionby pages 7-8). RibBX homologs are widespread across Proteobacteria, suggesting that maintenance of flavin biosynthesis under metal limitation is a broadly important adaptation (wang2019multimetalrestrictionby pages 8-9).

### 4.4 The RibF Bifunctional Kinase/Adenylyltransferase

Bacterial RibF proteins contain both riboflavin kinase (RFK) and FMN adenylyltransferase (FMNAT) modules in a single polypeptide, approximately double the size of eukaryotic monofunctional RFKs. The architecture facilitates direct transfer of FMN from the RFK active site to the FMNAT module (anoz‐carbonell2020humanriboflavinkinase pages 14-15). Species-specific differences in catalytic mechanism have been documented: human RFK and some bacterial enzymes show random sequential substrate binding, while others exhibit concerted binding, and product inhibition profiles differ markedly between species (anoz‐carbonell2020humanriboflavinkinase pages 14-15, anoz‐carbonell2020humanriboflavinkinase pages 1-2).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Bacteria vs. Archaea

The riboflavin biosynthetic pathway is present across all three domains of life, but with significant non-orthologous gene replacements in Archaea. Archaeal-specific enzymes include ArfA, ArfB, and a candidate PyrD-like reductase, while archaeal riboflavin synthases (RibC) form a unique pentameric class non-homologous to the bacterial RibE trimers (rodionova2017anovelbifunctional pages 1-2). The order of deamination and reduction steps is reversed relative to bacteria (ruchala2025regulationofriboflavin pages 4-5, jimeneznava2026biosynthesisregulationand pages 4-6). Regulation also diverges fundamentally: bacteria employ FMN-responsive riboswitches, whereas archaea use a novel bifunctional riboflavin kinase/transcriptional regulator called RbkR, whose DNA-binding activity is stimulated by CTP and suppressed by FMN (rodionova2017anovelbifunctional pages 1-2). Furthermore, archaeal riboflavin kinases (RibK) are CTP-dependent rather than ATP-dependent, and the FAD synthetase (RibL) is a separate protein rather than being fused with the kinase (rodionova2017anovelbifunctional pages 2-3).

### 5.2 Bacteria vs. Fungi and Yeasts

Fungi share the reversed deamination/reduction order with archaea: DARPP is first reduced by RIB7-type reductases, then deaminated by RIB2/RIB3-type deaminases (ruchala2025regulationofriboflavin pages 4-5). Regulation in fungi is linked to iron availability and oxidative stress rather than FMN riboswitches. In *Ashbya gossypii*, sporulation-associated transcriptional regulators (HST1, HST3) and iron-responsive factors (SEF1) control flavinogenesis (ruchala2025regulationofriboflavin pages 5-7, ruchala2025regulationofriboflavin pages 12-15).

### 5.3 Plants

Plant riboflavin biosynthesis occurs in plastids and follows the bacterial-type deamination-before-reduction order, consistent with the endosymbiotic origin of plant plastids. Plants harbor bifunctional GTPCHII/DHBPS enzymes (RibA-type), and recent work in rice identified OsRibA1 and OsRibA2 as bifunctional proteins with differing relative activities of their two domains. RibA has been confirmed as the rate-limiting step in plant riboflavin biosynthesis through mathematical kinetic modeling (jimeneznava2026biosynthesisregulationand pages 4-6).

### 5.4 Gene Organization: Gram-Positive vs. Gram-Negative Bacteria

In Gram-positive bacteria such as *B. subtilis*, riboflavin genes are organized in a single ~4.3 kb operon (*ribDG-ribE-ribAB-ribH-ribT* or equivalently *ribG-ribB-ribA-ribH-ribT* in older nomenclature) under the control of a single FMN riboswitch upstream of the first gene (ruchala2025regulationofriboflavin pages 9-11, liu2023metabolicengineeringof pages 3-4, hubenthal2024influenceofantimicrobial pages 29-31). In Gram-negative bacteria such as *E. coli*, the genes are dispersed across the chromosome, and only subsets (e.g., *ribB*, *ribH2*) are subject to FMN-mediated translational regulation (jimeneznava2026biosynthesisregulationand pages 19-20). In *P. putida* KT2440, the presence of multiple paralogous ribAB genes reflects the more complex gene complement typical of metabolically versatile Pseudomonads.

### 5.5 Paralog Redundancy

Multiple bacterial lineages harbor paralogous copies of pathway genes. In mycobacteria, *M. smegmatis* carries two lumazine synthase genes (RibH and MSMEG_6598, 39% identity) that provide functional redundancy; deletion of one is tolerated, but loss of both is lethal (chengalroyen2024modulationofriboflavin pages 7-10). *M. tuberculosis*, by contrast, retains only one essential RibH. Similarly, the roles of RibA1 vs. RibA2 paralogs in mycobacteria remain incompletely understood, though RibA2 is essential in both *M. smegmatis* and *M. tuberculosis* (chengalroyen2024modulationofriboflavin pages 7-10).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering

The pathway has a strictly ordered sequence within each branch. GTP cyclohydrolase II must act before the deaminase/reductase, and dephosphorylation of ArPP must precede condensation with DHBP. The two branches converge obligatorily at lumazine synthase, which requires both ArP and DHBP as co-substrates (jimeneznava2026biosynthesisregulationand pages 4-6, ruchala2025regulationofriboflavin pages 7-7).

### 6.2 Metal Dependencies

GTP cyclohydrolase II requires zinc for catalysis, creating a vulnerability under metal-restricted conditions such as those imposed by the host innate immune protein calprotectin. This constraint has driven the evolution of zinc-independent alternatives like RibBX in pathogenic bacteria (wang2019multimetalrestrictionby pages 6-7, wang2019multimetalrestrictionby pages 7-8).

### 6.3 Cofactor Recycling

The dismutation reaction of riboflavin synthase regenerates one molecule of ArP for every molecule of riboflavin produced, creating an internal recycling loop that effectively doubles the pyrimidine flux through the pathway (ruchala2025regulationofriboflavin pages 5-7).

### 6.4 Regulation as a Constraint

FMN riboswitches bind FMN with high affinity (~5 nM) and discriminate against both riboflavin and FAD (hubenthal2024influenceofantimicrobial pages 31-34). This creates tight negative feedback: accumulation of the phosphorylated product FMN shuts down transcription (in Gram-positives) or translation initiation (in Gram-negatives) of biosynthetic genes. The RibR protein can override this feedback in *Bacillus* species, enabling continued rib operon expression even at high FMN concentrations; RibR itself is regulated by sulfur compounds—induced by methionine and taurine, repressed by MgSO₄ (hubenthal2024influenceofantimicrobial pages 139-142, hubenthal2024influenceofantimicrobial pages 31-34).

### 6.5 Essentiality and Drug Targeting

In organisms lacking canonical riboflavin transporters (notably *M. tuberculosis*), the pathway is essential for viability. Silencing of *ribA2* or *ribF* is profoundly bactericidal in *M. tuberculosis*, genetically validating these enzymes as potential drug targets (chengalroyen2024modulationofriboflavin pages 1-2). The absence of riboflavin biosynthetic enzymes in humans provides a favorable therapeutic window.

---

## 7. Controversies and Open Questions

### 7.1 The Phosphatase Step

The identity of the phosphatase that converts ArPP to ArP prior to the lumazine synthase step has been historically ambiguous. Only recently has a dedicated phosphatase been identified in some organisms (e.g., *Aquifex aeolicus*), and whether this activity is provided by a dedicated enzyme or a promiscuous phosphatase in most bacteria remains an open question.

### 7.2 Functional Significance of Paralogs

Many bacteria, including *P. putida* KT2440, carry multiple paralogs of riboflavin biosynthesis genes (e.g., ribAB-I and ribAB-II). Whether these represent true functional redundancy, condition-specific alternatives, or pseudogenes in the process of decay is often unclear. Mycobacterial studies suggest condition-dependent essentiality, but comprehensive genetic dissection in Pseudomonas is lacking (chengalroyen2024modulationofriboflavin pages 7-10).

### 7.3 The Novel Formamidase Module

The discovery of BrbF, a formamidase required for riboflavin biosynthesis in invasive Rhizobiales (including *Brucella* and *Sinorhizobium*), revealed that some bacteria possess two partly interchangeable riboflavin biosynthetic modules—one serving intracellular metabolism and one linked to secretion (yurgel2022anovelformamidase pages 1-3, yurgel2022anovelformamidase pages 10-11). The generality and evolutionary significance of this dual-module architecture remains to be determined.

### 7.4 Cross-Kingdom Comparisons

The deamination-then-reduction vs. reduction-then-deamination dichotomy between bacteria and archaea/fungi is well established, but intermediate cases and the evolutionary transitions between these orders are poorly resolved. Whether the plant pathway's bacterial-type order reflects retention from the cyanobacterial endosymbiont or convergent evolution has not been definitively established (ruchala2025regulationofriboflavin pages 4-5, jimeneznava2026biosynthesisregulationand pages 4-6).

### 7.5 Riboflavin Pathway Intermediates and Immunity

The role of riboflavin biosynthetic intermediates as MAIT cell ligands has opened an entirely new dimension to pathway biology. The intermediate 5-A-RU non-enzymatically condenses with host-derived methylglyoxal or glyoxal to form potent MR1-presented antigens. However, whether bacteria can modulate MAIT cell activation by regulating flux through the pathway remains controversial, and attempts to exploit MAIT cells therapeutically against *M. tuberculosis* have yielded mixed results (chengalroyen2024modulationofriboflavin pages 1-2, chengalroyen2024modulationofriboflavin pages 17-18).

### 7.6 Industrial Production Ceiling

Despite decades of metabolic engineering, achieved riboflavin titers in engineered *B. subtilis* (~15 g/L) and *C. famata* (up to 16.4 g/L in fed-batch) remain below theoretical maxima, partly due to incompletely understood regulatory bottlenecks, precursor supply limitations, and the tight feedback regulation imposed by FMN riboswitches (ruchala2025regulationofriboflavin pages 18-19, ruchala2025regulationofriboflavin pages 11-12, liu2023metabolicengineeringof pages 9-11).

---

## 8. Key References

1. Ruchala J, Najdecka A, Wojdyla D, Liu W, Sibirny A. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. *Int J Mol Sci*. 2025;26(13):6243. doi:10.3390/ijms26136243

2. Jiménez-Nava RA, Chávez-Camarillo GM, Cristiani-Urbina E. Biosynthesis, regulation, and biotechnological production strategies of riboflavin (vitamin B2) and its derivatives: a review. *Pharmaceuticals*. 2026;19(3):389. doi:10.3390/ph19030389

3. Liu Y, Zhang Q, Qi X, et al. Metabolic engineering of *Bacillus subtilis* for riboflavin production: a review. *Microorganisms*. 2023;11(1):164. doi:10.3390/microorganisms11010164

4. Chengalroyen MD, Mehaffy C, Lucas M, et al. Modulation of riboflavin biosynthesis and utilization in mycobacteria. *Microbiol Spectr*. 2024;12(8). doi:10.1128/spectrum.03207-23

5. Rodionova IA, Vetting MW, Li X, et al. A novel bifunctional transcriptional regulator of riboflavin metabolism in Archaea. *Nucleic Acids Res*. 2017;45(7):3785-3799. doi:10.1093/nar/gkw1331

6. Wang J, Lonergan ZR, Gonzalez-Gutierrez G, et al. Multi-metal restriction by calprotectin impacts de novo flavin biosynthesis in *Acinetobacter baumannii*. *Cell Chem Biol*. 2019;26(5):745-755.e7. doi:10.1016/j.chembiol.2019.02.011

7. Yurgel SN, Johnson SA, Rice J, et al. A novel formamidase is required for riboflavin biosynthesis in invasive bacteria. *J Biol Chem*. 2022;298(9):102377. doi:10.1016/j.jbc.2022.102377

8. Ladenstein R, Morgunova E. Second career of a biosynthetic enzyme: Lumazine synthase as a virus-like nanoparticle in vaccine development. *Biotechnol Rep*. 2020;27:e00494. doi:10.1016/j.btre.2020.e00494

9. Anoz-Carbonell E, Rivero M, Polo V, et al. Human riboflavin kinase: Species-specific traits in the biosynthesis of the FMN cofactor. *FASEB J*. 2020;34(8):10871-10886. doi:10.1096/fj.202000566r

10. Hübenthal A. Influence of antimicrobial compounds and the RNA-binding protein RibR on the activity of B vitamin-responsive bacterial riboswitches. Heidelberg University, 2024. doi:10.11588/heidok.00034817

11. Faustino M, Lourenço TF, Strobbe S, et al. Mathematical kinetic modelling followed by in vitro and in vivo assays reveal the bifunctional rice GTPCHII/DHBPS enzymes. *BMC Plant Biol*. 2024;24. doi:10.1186/s12870-024-04878-z

References

1. (jimeneznava2026biosynthesisregulationand pages 4-6): Raziel Arturo Jiménez-Nava, Griselda Ma. Chávez-Camarillo, and Eliseo Cristiani-Urbina. Biosynthesis, regulation, and biotechnological production strategies of riboflavin (vitamin b2) and its derivatives: a review. Pharmaceuticals, 19:389, Feb 2026. URL: https://doi.org/10.3390/ph19030389, doi:10.3390/ph19030389. This article has 0 citations.

2. (ruchala2025regulationofriboflavin pages 2-4): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

3. (jimeneznava2026biosynthesisregulationand pages 19-20): Raziel Arturo Jiménez-Nava, Griselda Ma. Chávez-Camarillo, and Eliseo Cristiani-Urbina. Biosynthesis, regulation, and biotechnological production strategies of riboflavin (vitamin b2) and its derivatives: a review. Pharmaceuticals, 19:389, Feb 2026. URL: https://doi.org/10.3390/ph19030389, doi:10.3390/ph19030389. This article has 0 citations.

4. (ruchala2025regulationofriboflavin pages 9-11): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

5. (rodionova2017anovelbifunctional pages 2-3): Irina A. Rodionova, Matthew W. Vetting, Xiaoqing Li, Steven C. Almo, Andrei L. Osterman, and Dmitry A. Rodionov. A novel bifunctional transcriptional regulator of riboflavin metabolism in archaea. Nucleic Acids Research, 45:3785-3799, Jan 2017. URL: https://doi.org/10.1093/nar/gkw1331, doi:10.1093/nar/gkw1331. This article has 31 citations and is from a highest quality peer-reviewed journal.

6. (hubenthal2024influenceofantimicrobial pages 29-31): Anna Hübenthal. Influence of antimicrobial compounds and the rna-binding protein ribr on the activity of b vitamin-responsive bacterial riboswitches. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00034817, doi:10.11588/heidok.00034817. This article has 0 citations and is from a peer-reviewed journal.

7. (hubenthal2024influenceofantimicrobial pages 31-34): Anna Hübenthal. Influence of antimicrobial compounds and the rna-binding protein ribr on the activity of b vitamin-responsive bacterial riboswitches. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00034817, doi:10.11588/heidok.00034817. This article has 0 citations and is from a peer-reviewed journal.

8. (chengalroyen2024modulationofriboflavin pages 1-2): Melissa D. Chengalroyen, Carolina Mehaffy, Megan Lucas, Niel Bauer, Mabule L. Raphela, Nurudeen Oketade, Digby F. Warner, Deborah A. Lewinsohn, David M. Lewinsohn, Karen M. Dobos, and Valerie Mizrahi. Modulation of riboflavin biosynthesis and utilization in mycobacteria. Aug 2024. URL: https://doi.org/10.1128/spectrum.03207-23, doi:10.1128/spectrum.03207-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (liu2023metabolicengineeringof pages 3-4): Yang Liu, Quan Zhang, Xiaoxiao Qi, Huipeng Gao, Meng Wang, Hao Guan, and Bo Yu. Metabolic engineering of bacillus subtilis for riboflavin production: a review. Microorganisms, 11:164, Jan 2023. URL: https://doi.org/10.3390/microorganisms11010164, doi:10.3390/microorganisms11010164. This article has 39 citations.

10. (liu2023metabolicengineeringof pages 9-11): Yang Liu, Quan Zhang, Xiaoxiao Qi, Huipeng Gao, Meng Wang, Hao Guan, and Bo Yu. Metabolic engineering of bacillus subtilis for riboflavin production: a review. Microorganisms, 11:164, Jan 2023. URL: https://doi.org/10.3390/microorganisms11010164, doi:10.3390/microorganisms11010164. This article has 39 citations.

11. (ruchala2025regulationofriboflavin pages 4-5): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

12. (liu2023metabolicengineeringof pages 4-5): Yang Liu, Quan Zhang, Xiaoxiao Qi, Huipeng Gao, Meng Wang, Hao Guan, and Bo Yu. Metabolic engineering of bacillus subtilis for riboflavin production: a review. Microorganisms, 11:164, Jan 2023. URL: https://doi.org/10.3390/microorganisms11010164, doi:10.3390/microorganisms11010164. This article has 39 citations.

13. (ladenstein2020secondcareerof pages 2-3): Rudolf Ladenstein and Ekaterina Morgunova. Second career of a biosynthetic enzyme: lumazine synthase as a virus-like nanoparticle in vaccine development. Sep 2020. URL: https://doi.org/10.1016/j.btre.2020.e00494, doi:10.1016/j.btre.2020.e00494. This article has 48 citations and is from a peer-reviewed journal.

14. (ruchala2025regulationofriboflavin pages 5-7): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

15. (anoz‐carbonell2020humanriboflavinkinase pages 14-15): Ernesto Anoz‐Carbonell, Maribel Rivero, Victor Polo, Adrián Velázquez‐Campoy, and Milagros Medina. Human riboflavin kinase: species‐specific traits in the biosynthesis of the fmn cofactor. The FASEB Journal, 34:10871-10886, Jul 2020. URL: https://doi.org/10.1096/fj.202000566r, doi:10.1096/fj.202000566r. This article has 23 citations.

16. (chengalroyen2024modulationofriboflavin pages 7-10): Melissa D. Chengalroyen, Carolina Mehaffy, Megan Lucas, Niel Bauer, Mabule L. Raphela, Nurudeen Oketade, Digby F. Warner, Deborah A. Lewinsohn, David M. Lewinsohn, Karen M. Dobos, and Valerie Mizrahi. Modulation of riboflavin biosynthesis and utilization in mycobacteria. Aug 2024. URL: https://doi.org/10.1128/spectrum.03207-23, doi:10.1128/spectrum.03207-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

17. (wang2019multimetalrestrictionby pages 6-7): Jiefei Wang, Zachery R. Lonergan, Giovanni Gonzalez-Gutierrez, Brittany L. Nairn, Christina N. Maxwell, Yixiang Zhang, Claudia Andreini, Jonathan A. Karty, Walter J. Chazin, Jonathan C. Trinidad, Eric P. Skaar, and David P. Giedroc. Multi-metal restriction by calprotectin impacts de novo flavin biosynthesis in acinetobacter baumannii. Cell chemical biology, 26 5:745-755.e7, May 2019. URL: https://doi.org/10.1016/j.chembiol.2019.02.011, doi:10.1016/j.chembiol.2019.02.011. This article has 82 citations and is from a domain leading peer-reviewed journal.

18. (wang2019multimetalrestrictionby pages 7-8): Jiefei Wang, Zachery R. Lonergan, Giovanni Gonzalez-Gutierrez, Brittany L. Nairn, Christina N. Maxwell, Yixiang Zhang, Claudia Andreini, Jonathan A. Karty, Walter J. Chazin, Jonathan C. Trinidad, Eric P. Skaar, and David P. Giedroc. Multi-metal restriction by calprotectin impacts de novo flavin biosynthesis in acinetobacter baumannii. Cell chemical biology, 26 5:745-755.e7, May 2019. URL: https://doi.org/10.1016/j.chembiol.2019.02.011, doi:10.1016/j.chembiol.2019.02.011. This article has 82 citations and is from a domain leading peer-reviewed journal.

19. (ladenstein2020secondcareerof pages 1-2): Rudolf Ladenstein and Ekaterina Morgunova. Second career of a biosynthetic enzyme: lumazine synthase as a virus-like nanoparticle in vaccine development. Sep 2020. URL: https://doi.org/10.1016/j.btre.2020.e00494, doi:10.1016/j.btre.2020.e00494. This article has 48 citations and is from a peer-reviewed journal.

20. (yurgel2022anovelformamidase pages 1-3): Svetlana N. Yurgel, Skylar A. Johnson, Jennifer Rice, Na Sa, Clayton Bailes, John Baumgartner, Josh E. Pitzer, R. Martin Roop, and Sanja Roje. A novel formamidase is required for riboflavin biosynthesis in invasive bacteria. Journal of Biological Chemistry, 298:102377, Sep 2022. URL: https://doi.org/10.1016/j.jbc.2022.102377, doi:10.1016/j.jbc.2022.102377. This article has 5 citations and is from a domain leading peer-reviewed journal.

21. (wang2019multimetalrestrictionby pages 8-9): Jiefei Wang, Zachery R. Lonergan, Giovanni Gonzalez-Gutierrez, Brittany L. Nairn, Christina N. Maxwell, Yixiang Zhang, Claudia Andreini, Jonathan A. Karty, Walter J. Chazin, Jonathan C. Trinidad, Eric P. Skaar, and David P. Giedroc. Multi-metal restriction by calprotectin impacts de novo flavin biosynthesis in acinetobacter baumannii. Cell chemical biology, 26 5:745-755.e7, May 2019. URL: https://doi.org/10.1016/j.chembiol.2019.02.011, doi:10.1016/j.chembiol.2019.02.011. This article has 82 citations and is from a domain leading peer-reviewed journal.

22. (anoz‐carbonell2020humanriboflavinkinase pages 1-2): Ernesto Anoz‐Carbonell, Maribel Rivero, Victor Polo, Adrián Velázquez‐Campoy, and Milagros Medina. Human riboflavin kinase: species‐specific traits in the biosynthesis of the fmn cofactor. The FASEB Journal, 34:10871-10886, Jul 2020. URL: https://doi.org/10.1096/fj.202000566r, doi:10.1096/fj.202000566r. This article has 23 citations.

23. (rodionova2017anovelbifunctional pages 1-2): Irina A. Rodionova, Matthew W. Vetting, Xiaoqing Li, Steven C. Almo, Andrei L. Osterman, and Dmitry A. Rodionov. A novel bifunctional transcriptional regulator of riboflavin metabolism in archaea. Nucleic Acids Research, 45:3785-3799, Jan 2017. URL: https://doi.org/10.1093/nar/gkw1331, doi:10.1093/nar/gkw1331. This article has 31 citations and is from a highest quality peer-reviewed journal.

24. (ruchala2025regulationofriboflavin pages 12-15): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

25. (ruchala2025regulationofriboflavin pages 7-7): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

26. (hubenthal2024influenceofantimicrobial pages 139-142): Anna Hübenthal. Influence of antimicrobial compounds and the rna-binding protein ribr on the activity of b vitamin-responsive bacterial riboswitches. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00034817, doi:10.11588/heidok.00034817. This article has 0 citations and is from a peer-reviewed journal.

27. (yurgel2022anovelformamidase pages 10-11): Svetlana N. Yurgel, Skylar A. Johnson, Jennifer Rice, Na Sa, Clayton Bailes, John Baumgartner, Josh E. Pitzer, R. Martin Roop, and Sanja Roje. A novel formamidase is required for riboflavin biosynthesis in invasive bacteria. Journal of Biological Chemistry, 298:102377, Sep 2022. URL: https://doi.org/10.1016/j.jbc.2022.102377, doi:10.1016/j.jbc.2022.102377. This article has 5 citations and is from a domain leading peer-reviewed journal.

28. (chengalroyen2024modulationofriboflavin pages 17-18): Melissa D. Chengalroyen, Carolina Mehaffy, Megan Lucas, Niel Bauer, Mabule L. Raphela, Nurudeen Oketade, Digby F. Warner, Deborah A. Lewinsohn, David M. Lewinsohn, Karen M. Dobos, and Valerie Mizrahi. Modulation of riboflavin biosynthesis and utilization in mycobacteria. Aug 2024. URL: https://doi.org/10.1128/spectrum.03207-23, doi:10.1128/spectrum.03207-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

29. (ruchala2025regulationofriboflavin pages 18-19): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

30. (ruchala2025regulationofriboflavin pages 11-12): Justyna Ruchala, Alicja Najdecka, Dominik Wojdyla, Wen Liu, and Andriy Sibirny. Regulation of riboflavin biosynthesis in microorganisms and construction of the advanced overproducers of this vitamin. International journal of molecular sciences, 26 13:6243, Jun 2025. URL: https://doi.org/10.3390/ijms26136243, doi:10.3390/ijms26136243. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](riboflavin_biosynthesis-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. chengalroyen2024modulationofriboflavin pages 1-2
2. jimeneznava2026biosynthesisregulationand pages 19-20
3. liu2023metabolicengineeringof pages 9-11
4. jimeneznava2026biosynthesisregulationand pages 4-6
5. ladenstein2020secondcareerof pages 2-3
6. wang2019multimetalrestrictionby pages 6-7
7. wang2019multimetalrestrictionby pages 8-9
8. rodionova2017anovelbifunctional pages 1-2
9. rodionova2017anovelbifunctional pages 2-3
10. ruchala2025regulationofriboflavin pages 4-5
11. chengalroyen2024modulationofriboflavin pages 7-10
12. ruchala2025regulationofriboflavin pages 5-7
13. hubenthal2024influenceofantimicrobial pages 31-34
14. ruchala2025regulationofriboflavin pages 2-4
15. ruchala2025regulationofriboflavin pages 9-11
16. hubenthal2024influenceofantimicrobial pages 29-31
17. liu2023metabolicengineeringof pages 3-4
18. liu2023metabolicengineeringof pages 4-5
19. wang2019multimetalrestrictionby pages 7-8
20. ladenstein2020secondcareerof pages 1-2
21. yurgel2022anovelformamidase pages 1-3
22. ruchala2025regulationofriboflavin pages 12-15
23. ruchala2025regulationofriboflavin pages 7-7
24. hubenthal2024influenceofantimicrobial pages 139-142
25. yurgel2022anovelformamidase pages 10-11
26. chengalroyen2024modulationofriboflavin pages 17-18
27. ruchala2025regulationofriboflavin pages 18-19
28. ruchala2025regulationofriboflavin pages 11-12
29. DHBP
30. https://doi.org/10.3390/ph19030389,
31. https://doi.org/10.3390/ijms26136243,
32. https://doi.org/10.1093/nar/gkw1331,
33. https://doi.org/10.11588/heidok.00034817,
34. https://doi.org/10.1128/spectrum.03207-23,
35. https://doi.org/10.3390/microorganisms11010164,
36. https://doi.org/10.1016/j.btre.2020.e00494,
37. https://doi.org/10.1096/fj.202000566r,
38. https://doi.org/10.1016/j.chembiol.2019.02.011,
39. https://doi.org/10.1016/j.jbc.2022.102377,