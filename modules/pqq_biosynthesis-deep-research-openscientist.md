---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T18:51:53.332617'
end_time: '2026-07-20T19:51:03.316448'
duration_seconds: 3549.98
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pyrroloquinoline quinone biosynthesis
  module_summary: Pyrroloquinoline quinone (PQQ) is made from conserved glutamate
    and tyrosine residues in the short ribosomally synthesized precursor peptide PqqA.
    A PqqD-family peptide chaperone presents PqqA to the radical-SAM enzyme PqqE,
    which forms the defining carbon-carbon cross-link. Proteolytic processing and
    PqqB-dependent oxygenation both contribute to formation of a late small-molecule
    precursor, although their relative order is unresolved. PqqC completes oxidative
    ring closure to mature PQQ. PQQ export and use by quinoprotein dehydrogenases
    are downstream of this module.
  module_outline: "- Pyrroloquinoline quinone biosynthesis\n  - 1. PqqA precursor-peptide\
    \ supply\n  - PqqA precursor-peptide supply\n    - PqqA precursor-peptide role\
    \ (molecular player: PqqA precursor-peptide family)\n  - 2. PqqD-assisted radical-SAM\
    \ cross-link formation\n  - PqqD-assisted PqqE cross-linking\n    - PqqD peptide-chaperone\
    \ role (molecular player: PqqD peptide-chaperone family)\n    - PqqE PqqA peptide\
    \ cyclase activity (molecular player: PqqE radical-SAM peptide cyclase family;\
    \ activity or role: cyclase activity)\n  - Proteolytic release of a PqqA-derived\
    \ intermediate\n  - PqqA-derived precursor proteolysis\n    - Alternative versions\
    \ by protease repertoire: PQQ precursor-proteolysis implementation\n      - Single-chain\
    \ PqqF/M16A-like protease route\n        - Single-chain PqqF metalloendopeptidase\
    \ activity (molecular player: single-chain PqqF M16 peptidase family; activity\
    \ or role: metalloendopeptidase activity)\n      - Two-component PqqF/PqqG M16B\
    \ protease route\n        - PqqF/PqqG M16B metalloendopeptidase complex (molecular\
    \ player: PqqF/PqqG M16B protease complex; activity or role: metalloendopeptidase\
    \ activity)\n      - Alternative cellular-protease route\n        - Alternative\
    \ PqqA-pathway peptidase activity (molecular player: peptidase activity; activity\
    \ or role: peptidase activity)\n  - PqqB-dependent oxygenation\n  - PqqB-dependent\
    \ precursor oxygenation\n    - PqqB oxygen-incorporating oxidoreductase activity\
    \ (molecular player: PqqB family; activity or role: oxidoreductase activity, acting\
    \ on paired donors, with incorporation or reduction of molecular oxygen)\n  -\
    \ 5. Terminal oxidative ring closure\n  - PqqC terminal PQQ formation\n    - Pyrroloquinoline-quinone\
    \ synthase activity (molecular player: PqqC-like family; activity or role: pyrroloquinoline-quinone\
    \ synthase activity)"
  module_connections: '- PqqA precursor-peptide supply feeds into PqqD-assisted PqqE
    cross-linking: PqqA supplies the precursor peptide bound by PqqD and modified
    by PqqE.

    - PqqD-assisted PqqE cross-linking feeds into PqqA-derived precursor proteolysis:
    A PqqA-derived precursor undergoes pathway-associated proteolytic processing.

    - PqqD-assisted PqqE cross-linking feeds into PqqB-dependent precursor oxygenation:
    PqqB acts on an intermediate derived from cross-linked PqqA.

    - PqqA-derived precursor proteolysis feeds into PqqC terminal PQQ formation: Proteolysis
    is required to generate the small-molecule precursor used late in the pathway.

    - PqqB-dependent precursor oxygenation feeds into PqqC terminal PQQ formation:
    PqqB-dependent oxygenation contributes to formation of the late PqqC substrate.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 27
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pqq_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pqq_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Pyrroloquinoline quinone biosynthesis

## Working Scope

Pyrroloquinoline quinone (PQQ) is made from conserved glutamate and tyrosine residues in the short ribosomally synthesized precursor peptide PqqA. A PqqD-family peptide chaperone presents PqqA to the radical-SAM enzyme PqqE, which forms the defining carbon-carbon cross-link. Proteolytic processing and PqqB-dependent oxygenation both contribute to formation of a late small-molecule precursor, although their relative order is unresolved. PqqC completes oxidative ring closure to mature PQQ. PQQ export and use by quinoprotein dehydrogenases are downstream of this module.

## Provisional Biological Outline

- Pyrroloquinoline quinone biosynthesis
  - 1. PqqA precursor-peptide supply
  - PqqA precursor-peptide supply
    - PqqA precursor-peptide role (molecular player: PqqA precursor-peptide family)
  - 2. PqqD-assisted radical-SAM cross-link formation
  - PqqD-assisted PqqE cross-linking
    - PqqD peptide-chaperone role (molecular player: PqqD peptide-chaperone family)
    - PqqE PqqA peptide cyclase activity (molecular player: PqqE radical-SAM peptide cyclase family; activity or role: cyclase activity)
  - Proteolytic release of a PqqA-derived intermediate
  - PqqA-derived precursor proteolysis
    - Alternative versions by protease repertoire: PQQ precursor-proteolysis implementation
      - Single-chain PqqF/M16A-like protease route
        - Single-chain PqqF metalloendopeptidase activity (molecular player: single-chain PqqF M16 peptidase family; activity or role: metalloendopeptidase activity)
      - Two-component PqqF/PqqG M16B protease route
        - PqqF/PqqG M16B metalloendopeptidase complex (molecular player: PqqF/PqqG M16B protease complex; activity or role: metalloendopeptidase activity)
      - Alternative cellular-protease route
        - Alternative PqqA-pathway peptidase activity (molecular player: peptidase activity; activity or role: peptidase activity)
  - PqqB-dependent oxygenation
  - PqqB-dependent precursor oxygenation
    - PqqB oxygen-incorporating oxidoreductase activity (molecular player: PqqB family; activity or role: oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen)
  - 5. Terminal oxidative ring closure
  - PqqC terminal PQQ formation
    - Pyrroloquinoline-quinone synthase activity (molecular player: PqqC-like family; activity or role: pyrroloquinoline-quinone synthase activity)

## Known Relationships Among Steps

- PqqA precursor-peptide supply feeds into PqqD-assisted PqqE cross-linking: PqqA supplies the precursor peptide bound by PqqD and modified by PqqE.
- PqqD-assisted PqqE cross-linking feeds into PqqA-derived precursor proteolysis: A PqqA-derived precursor undergoes pathway-associated proteolytic processing.
- PqqD-assisted PqqE cross-linking feeds into PqqB-dependent precursor oxygenation: PqqB acts on an intermediate derived from cross-linked PqqA.
- PqqA-derived precursor proteolysis feeds into PqqC terminal PQQ formation: Proteolysis is required to generate the small-molecule precursor used late in the pathway.
- PqqB-dependent precursor oxygenation feeds into PqqC terminal PQQ formation: PqqB-dependent oxygenation contributes to formation of the late PqqC substrate.

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

# Pyrroloquinoline Quinone Biosynthesis: A Review-Style Synthesis

## 1. Executive Summary

Pyrroloquinoline quinone (PQQ) is a small, tricyclic *ortho*-quinone redox cofactor used by bacterial quinoprotein dehydrogenases (most famously methanol and glucose dehydrogenases). Despite its status as a diffusible small molecule, PQQ is not built by classical stepwise small-molecule metabolism. It is a **ribosomally synthesized and post-translationally modified peptide (RiPP)-derived cofactor**: its entire carbon skeleton originates from a single conserved **glutamate** and a single conserved **tyrosine** embedded in a short precursor peptide, **PqqA**. This RiPP framing is the central organizing principle of the field and the boundary that defines the biosynthetic system: everything from the ribosomal synthesis of PqqA through the terminal oxidative ring closure catalyzed by PqqC is "in scope," whereas PQQ export, its incorporation into apo-dehydrogenases, lanthanide/calcium cofactor loading of those dehydrogenases, and the eukaryotic dietary/"vitamin-like" biology of PQQ are adjacent topics that lie outside the biosynthetic module.

The best-supported model comprises five gene products acting in a defined logical order. **PqqA** supplies the precursor peptide. The peptide chaperone **PqqD**, a stand-alone member of the RiPP Recognition Element (RRE) superfamily, binds the otherwise-unstructured PqqA and presents it to the SPASM-domain radical-SAM enzyme **PqqE**, which catalyzes the defining, chemically difficult **carbon–carbon cross-link between the glutamate and tyrosine side chains**. A **protease** then excises the cross-linked di-amino-acid unit from the rest of the peptide; the protease identity varies by organism (single-chain PqqF, a two-component PqqF/PqqG M16B heterodimer, or, in some genomes, a housekeeping peptidase). The metallo-β-lactamase-fold protein **PqqB** acts as an **iron-dependent hydroxylase** that installs oxygen atoms needed for the quinone, and the metal- and cofactor-free oxidase **PqqC** performs the terminal step: a ring cyclization coupled to an **eight-electron oxidation** that yields mature PQQ, passing reducing equivalents to O₂ with production of H₂O₂.

The enzymatic identities and the chemistry of the individual steps are, for the most part, firmly established. The principal unresolved mechanistic point is the **relative order of proteolysis versus PqqB-dependent oxygenation** in generating the late small-molecule precursor of PqqC. Secondary open questions include the physiological electron donor for PqqE in vivo, the exact number and timing of oxygen-insertion events, and the degree to which protease usage and operon architecture differ across lineages. This review lays out the scope, the mechanistic model, the molecular players, the evolutionary and regulatory variation, the ordering constraints, and the controversies, with explicit attention to where claims rest on one organism or on indirect evidence.

## 2. Definition and Biological Boundaries

**What is included.** The PQQ biosynthetic system is the set of gene products and reactions that convert the ribosomal precursor peptide PqqA into the free, mature PQQ cofactor. Operationally, this is the classic *pqq* operon core: **PqqA, PqqB, PqqC, PqqD, and PqqE**, plus a **protease** function (PqqF and/or PqqG, or a substitute peptidase). These five gene products are the essential, conserved unit repeatedly recovered across studies of *Klebsiella pneumoniae*, *Methylobacterium extorquens*, and other producers [PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/); [PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/).

**What is often conflated but should be treated separately.**

- **Downstream cofactor use.** PQQ-dependent alcohol/glucose dehydrogenases (e.g., MxaFI- and XoxF-type methanol dehydrogenases, ExaF ethanol dehydrogenase, membrane glucose dehydrogenase Gcd) *use* PQQ but do not *make* it. Their calcium- vs. lanthanide-dependence and regulation are a distinct field ([PMID: 27573017](https://pubmed.ncbi.nlm.nih.gov/27573017/); [PMID: 26833413](https://pubmed.ncbi.nlm.nih.gov/26833413/); [PMID: 32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/)).
- **PQQ export/secretion.** Transport of finished PQQ out of the cell is downstream of biosynthesis and mechanistically separate.
- **Eukaryotic "vitamin-like" biology.** In mammals PQQ modulates mitochondrial biogenesis and NAD⁺/sirtuin signaling and has been proposed as a "longevity vitamin" ([PMID: 34680074](https://pubmed.ncbi.nlm.nih.gov/34680074/); [PMID: 30322941](https://pubmed.ncbi.nlm.nih.gov/30322941/); [PMID: 17029795](https://pubmed.ncbi.nlm.nih.gov/17029795/)). Animals do not synthesize PQQ; this is nutrition/pharmacology, not biosynthesis.
- **Other RiPP/radical-SAM cofactor systems.** The mycofactocin system uses a PqqE-like radical-SAM enzyme and a bacteriocin-sized precursor peptide and is genuinely homologous in machinery, but produces a different electron carrier and should not be merged with PQQ biosynthesis ([PMID: 21223593](https://pubmed.ncbi.nlm.nih.gov/21223593/)).
- **Other protein-derived quinocofactors.** TPQ, LTQ, TTQ, and the galactose oxidase cofactor are also amino-acid-derived quinones, but they are formed *in situ* within their host enzymes, not released as free cofactors, and are mechanistically unrelated to the PqqA→PQQ RiPP route ([PMID: 9706222](https://pubmed.ncbi.nlm.nih.gov/9706222/)).

**Competing definitions.** The most consequential definitional evolution is the reframing of PQQ from a "cofactor of unknown biosynthetic origin" to a bona fide **RiPP**. Early structural surveys already assigned putative roles to PqqA–F ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)), but the RiPP classification—PqqA as precursor peptide, PqqD as a peptide chaperone/RRE—now anchors the field ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/); [PMID: 28481092](https://pubmed.ncbi.nlm.nih.gov/28481092/)).

## 3. Mechanistic Overview

The current best model is a five-stage pipeline in which the first three stages are strictly ordered and the middle "processing" stages (proteolysis and PqqB oxygenation) have a partially unresolved order.

```
   PqqA (ribosomal precursor peptide; conserved Glu ... Tyr)
        │  (1) supply
        ▼
   PqqD ── binds & presents ──► PqqE  [radical-SAM + SPASM]
        │                         │  (2) Glu–Tyr C–C cross-link
        ▼                         ▼
        cross-linked PqqA peptide
        │
        ├──(3a) protease (PqqF; PqqF/PqqG M16B; or housekeeping peptidase)
        │        excises the cross-linked di-amino-acid unit
        │
        ├──(3b) PqqB [Fe-dependent hydroxylase]: O-insertion → quinone O's
        │        (order of 3a vs 3b unresolved)
        ▼
   AHQQ-type small-molecule precursor
        │
        ▼  (4) PqqC [metal-free oxidase]: ring closure + 8 e⁻ oxidation, O2 → H2O2
        ▼
        PQQ  (mature ortho-quinone cofactor)
```

**Obligatory steps.** (i) Ribosomal synthesis of PqqA; (ii) PqqD-assisted PqqE cross-linking; (iii) proteolytic release of the modified di-amino-acid unit; (iv) PqqB-dependent oxygenation; (v) PqqC terminal ring closure/oxidation. Genetic evidence that *pqqA–E* are each essential makes all five obligatory in the canonical producers.

**Conditional/variable steps.** The **protease** step is obligatory in function but **variable in implementation**: which enzyme performs the excision depends on the organism's protease repertoire. This is the clearest example of an "alternative route to the same outcome" in the pathway.

**Accessory requirements.** In vitro, PqqE cross-linking requires an external **reducing system** (a flavodoxin/flavodoxin-reductase pair is commonly used); the physiological in-cell reductant is not firmly established. This is a genuine mechanistic gap rather than a settled accessory step.

## 4. Major Molecular Players and Active Assemblies

### 4.1 PqqA — the precursor peptide

PqqA is a short ribosomally synthesized peptide containing the conserved **glutamate** and **tyrosine** that become the entire carbon skeleton of PQQ. It is **intrinsically unstructured in solution** and only engages the modifying enzyme PqqE when delivered in complex with PqqD ([PMID: 27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/)). This "chaperone-gated" logic is a hallmark of RiPP biosynthesis and enforces the ordering of steps 1→2.

### 4.2 PqqD — the peptide chaperone / RRE

PqqD is a small stand-alone **RiPP Recognition Element (RRE)** that binds PqqA and presents it to PqqE; PqqE activity is strictly dependent on PqqD ([PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/); [PMID: 28481092](https://pubmed.ncbi.nlm.nih.gov/28481092/)). Although an older X-ray structure captured a dimer, PqqD is now understood to function as a **monomer** under physiological conditions, and NMR has mapped the PqqA-binding residues ([PMID: 27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/)). In some organisms (e.g., *Methylobacterium extorquens*) PqqD is naturally fused to PqqC as a single PqqCD polypeptide, underscoring the modular, sometimes-concatenated nature of the machinery.

The RRE family to which PqqD belongs is ancient and enormous. Genome mining with RRE-Finder recovered **~25,000 high-confidence RREs** spanning all characterized RRE-dependent RiPP classes, and RREs are present in roughly **half of all prokaryotic RiPP classes** ([PMID: 32873609](https://pubmed.ncbi.nlm.nih.gov/32873609/); [PMID: 36682862](https://pubmed.ncbi.nlm.nih.gov/36682862/)). The RRE fold is proposed to derive from a co-opted **winged helix-turn-helix DNA-binding transcriptional regulator**, giving PqqD a deep evolutionary pedigree distinct from the enzymology it now serves.

### 4.3 PqqE — the radical-SAM cross-linking enzyme

PqqE is the committed, chemically defining enzyme. It is a **SPASM-domain radical-SAM enzyme** that uses a catalytic **[4Fe-4S] cluster** to generate a 5′-deoxyadenosyl radical from SAM, plus two **auxiliary Fe-S clusters** housed in its SPASM domain. Detailed X-ray/EPR characterization shows an unusual architecture: the auxiliary cluster nearest the radical-SAM site (**AuxI**) is a **[2Fe-2S] cluster ligated by four cysteines**, while **AuxII** is a **[4Fe-4S] cluster ligated by three Cys and one Asp** ([PMID: 29405700](https://pubmed.ncbi.nlm.nih.gov/29405700/); [PMID: 31769977](https://pubmed.ncbi.nlm.nih.gov/31769977/)). Functionally, PqqE catalyzes **de novo C–C bond formation between the glutamate and tyrosine side chains of PqqA**, but only when PqqA is presented by PqqD and an external reductant is supplied ([PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/); [PMID: 19746930](https://pubmed.ncbi.nlm.nih.gov/19746930/); [PMID: 30097100](https://pubmed.ncbi.nlm.nih.gov/30097100/)). Like most radical-SAM enzymes, PqqE is oxygen-sensitive and requires anaerobic handling.

### 4.4 The protease(s) — PqqF / PqqG (and alternatives)

A protease must excise the cross-linked glutamyl–tyrosyl unit from the remainder of PqqA before the small-molecule steps can proceed. This function is realized in at least three ways across bacteria:

| Route | Enzyme(s) | Family | Notes |
|---|---|---|---|
| Single-chain | PqqF | M16A-like metalloendopeptidase | Classical "PqqF cuts out the linked amino acids" model ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)) |
| Two-component | PqqF + PqqG | M16B heterodimer | Demonstrated as a **two-component protease** in an α-proteobacterium ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)) |
| Substitute | Housekeeping peptidase | Various | Some genomes lack a dedicated *pqqF/G*; a cellular protease is inferred to substitute |

The demonstration of a **two-component PqqF/PqqG M16B protease** resolved a long-standing gap in which "a protease/peptidase required for excision of an early, cross-linked di-amino-acid precursor" had been missing from the mechanistic accounting ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)).

### 4.5 PqqB — the iron-dependent hydroxylase

PqqB has a **metallo-β-lactamase fold** but does not act as a hydrolase. It was shown to be an **iron-dependent hydroxylase catalyzing oxygen-insertion reactions proposed to produce the quinone moiety** of PQQ—an activity unprecedented in the metallo-β-lactamase superfamily and one that supplied a genuine "missing link" in the pathway ([PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)). The number and precise timing of PqqB's oxygen insertions, and whether it acts on the peptide-bound or released species, remain incompletely defined.

### 4.6 PqqC — the terminal metal-free oxidase

PqqC catalyzes the final, committed step: it takes the tricyclic substrate **AHQQ [3a-(2-amino-2-carboxyethyl)-4,5-dioxo-4,5,6,7,8,9-hexahydroquinoline-7,9-dicarboxylic acid]** and performs a **ring cyclization coupled to an eight-electron oxidation** to yield PQQ. Remarkably, PqqC does this **without any redox-active metal or organic cofactor**, transferring redox equivalents directly to molecular oxygen and generating **H₂O₂** ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)). Crystallographic studies of active-site mutants trapped a **tricyclic, non-planar reaction intermediate** and showed that substrate binding drives an open→closed conformational change essential for O₂ binding and catalysis ([PMID: 20602352](https://pubmed.ncbi.nlm.nih.gov/20602352/)).

## 5. Evolutionary and Cell-Biological Variation

**Taxonomic distribution.** PQQ biosynthesis is a **prokaryotic** capability, found across many Gram-negative bacteria (e.g., *Klebsiella*, *Pseudomonas*, *Serratia*, *Methylobacterium* and other α-proteobacteria) and beyond. Eukaryotes, including animals, do not encode the pathway; dietary PQQ is of microbial/environmental origin ([PMID: 9706222](https://pubmed.ncbi.nlm.nih.gov/9706222/); [PMID: 34680074](https://pubmed.ncbi.nlm.nih.gov/34680074/)).

**Operon architecture varies.** Gene content and order of *pqq* operons differ by lineage. *Klebsiella pneumoniae* carries *pqqA–F*; *Serratia* sp. S119 has a six-gene *pqqABCDEF* operon with **two promoters**; *Pseudomonas putida* has a *pqqFABCDEG* arrangement; and *Methylobacterium extorquens* fuses PqqC and PqqD into a single PqqCD protein ([PMID: 28709697](https://pubmed.ncbi.nlm.nih.gov/28709697/); [PMID: 27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/)). These rearrangements do not change the underlying reaction logic but do change how the parts are packaged and regulated.

**Alternative proteolysis is the principal "same outcome, different means" variation** (Section 4.4): single-chain PqqF, two-component PqqF/PqqG M16B, or a substitute housekeeping peptidase.

**Regulation is condition-dependent, tuned to physiology.** PQQ output is transcriptionally matched to demand. In *Serratia* sp. S119, *pqq* genes are up-regulated under **phosphate limitation** and by peanut root-exudate molecules ([PMID: 28709697](https://pubmed.ncbi.nlm.nih.gov/28709697/)). In *Pseudomonas putida* KT2440, **the levels of *pqqF* and *pqqB* expression mirror the amount of PQQ synthesized**, and glucose induces the system ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)). The physiological logic is that PQQ feeds the periplasmic glucose dehydrogenase whose product, gluconic acid, drives **mineral-phosphate solubilization**—linking cofactor supply to nutrient acquisition ([PMID: 23596526](https://pubmed.ncbi.nlm.nih.gov/23596526/)). Because PQQ producers are typically Gram-negative, the mature cofactor operates in the **periplasm/cell envelope**, where quinoprotein dehydrogenases reside; the biosynthetic steps culminating in PqqC produce the free cofactor that is then loaded onto those apoenzymes.

**Deep ancestry of the machinery.** The radical-SAM + SPASM enzyme class (PqqE) and the RRE chaperone class (PqqD) are both ancient and widely radiated. The RRE fold in particular is proposed to have been **repurposed from a winged-HTH transcriptional regulator**, and PqqE-like radical-SAM enzymes anchor other RiPP-cofactor systems such as mycofactocin ([PMID: 21223593](https://pubmed.ncbi.nlm.nih.gov/21223593/); [PMID: 32873609](https://pubmed.ncbi.nlm.nih.gov/32873609/)). Because RREs occur across roughly half of prokaryotic RiPP classes, **stand-alone RRE proteins like PqqD are among the best representatives for understanding the ancestral peptide-presentation role**, uncoupled from the fused RRE domains found in many other RiPP maturases.

## 6. Constraints, Dependencies, and Failure Modes

**Ordering that is physically enforced.**

1. **Supply before cross-link.** PqqA must exist and be bound by PqqD before PqqE can act; PqqA is unstructured alone and does not productively engage PqqE without PqqD ([PMID: 27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/); [PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/)).
2. **Cross-link before excision.** The C–C cross-link defines the di-amino-acid unit that the protease excises; proteolysis of an un-cross-linked peptide would not yield the correct precursor ([PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)).
3. **Everything before PqqC.** PqqC is the terminal, committed oxidase; its substrate AHQQ is a late tricyclic intermediate, so ring closure/8-electron oxidation must come last ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/); [PMID: 20602352](https://pubmed.ncbi.nlm.nih.gov/20602352/)).

**Ordering that is NOT resolved.** The **relative order of proteolysis (PqqF/G) and PqqB-dependent oxygenation** is the central unresolved constraint. Both contribute to forming the late small-molecule precursor of PqqC, but whether PqqB acts on the still-peptide-bound cross-linked unit or on the excised small molecule (and whether a spontaneous Schiff-base step intervenes, as older models proposed) is not settled ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/); [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)).

**Chemical/environmental constraints.**

- **Oxygen dichotomy.** PqqE is oxygen-sensitive (its Fe-S clusters are destroyed by O₂) and must operate under low-oxygen/anaerobic conditions in vitro ([PMID: 30097100](https://pubmed.ncbi.nlm.nih.gov/30097100/)), whereas PqqB and PqqC **require O₂** as co-substrate. This imposes a spatial/temporal separation between the radical-SAM chemistry and the oxidative tailoring chemistry.
- **Reductant dependence.** PqqE turnover needs an electron source; the in-vitro flavodoxin/flavodoxin-reductase surrogate stands in for an undefined physiological donor.

**Failure modes.** Loss of any of PqqA–E abolishes PQQ production. Loss of the dedicated protease can, in some organisms, be buffered by housekeeping peptidases (route redundancy), which is why the protease step is functionally obligatory but genetically variable. Regulatory failure (e.g., inability to sense phosphate or glucose status) would decouple PQQ supply from the dehydrogenase demand it normally serves.

## 7. Controversies and Open Questions

1. **Order of proteolysis vs. PqqB oxygenation.** The single largest open mechanistic question. Reviews explicitly flag both the past uncertainty over the protease and the unresolved sequencing of oxygenation relative to excision ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/); [PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)).

2. **Exact substrate and product of PqqB.** PqqB is established as an iron-dependent hydroxylase performing oxygen insertion, but the number of insertions, the precise intermediate it acts upon, and how its output connects to the AHQQ substrate of PqqC remain to be nailed down ([PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)).

3. **Physiological electron donor for PqqE.** In vitro reconstitution uses artificial or surrogate reductants; the native donor and its regulation are unknown.

4. **Organism mixing.** Much of the mechanistic picture is assembled from **different organisms**—PqqE from *Klebsiella*, PqqD/PqqA from *Methylobacterium*, the two-component protease from an α-proteobacterium, PqqC structures from *Klebsiella*. Because operon architecture and protease strategy differ across lineages, some cross-organism inferences may not transfer cleanly, and this should temper any single "universal" pathway diagram.

5. **Intermediate structures.** Several proposed intermediates (e.g., a spontaneous Schiff-base step in older models) rest on structural inference rather than isolation; PqqC's trapped intermediate is a notable exception where direct structural evidence exists ([PMID: 20602352](https://pubmed.ncbi.nlm.nih.gov/20602352/)).

6. **Boundary confusion.** The mammalian "vitamin-like" literature, while biologically interesting, is frequently cited alongside biosynthesis and can blur the boundary of the system; these effects concern PQQ *action* in eukaryotes, not its *synthesis* ([PMID: 34680074](https://pubmed.ncbi.nlm.nih.gov/34680074/); [PMID: 38767475](https://pubmed.ncbi.nlm.nih.gov/38767475/)).

## 8. Key Findings (with evidence)

### Finding 1 — PQQ is a RiPP built by a conserved five-gene module

PQQ derives from a conserved glutamate and tyrosine within the ribosomal precursor peptide PqqA, and the core module comprises PqqE (radical-SAM cross-linking), PqqD (chaperone/RRE), PqqB (iron-dependent hydroxylase), and PqqC (terminal oxidase), with PqqA–E being the essential gene products. This is stated directly by authoritative reviews: PQQ is *"produced from a ribosomally synthesized and post-translationally modified peptide PqqA via a pathway comprising four conserved proteins PqqB-E"* ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)), and the biogenesis review focuses *"on the mechanisms of PqqE, PqqF/G, and PqqB"* ([PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)).

### Finding 2 — PqqE forms the Glu–Tyr C–C cross-link and requires PqqD

PqqE is a SPASM-domain radical-SAM enzyme with a catalytic [4Fe-4S] cluster and two auxiliary clusters (AuxI = unusual [2Fe-2S] with four Cys ligands; AuxII = [4Fe-4S] with three Cys + one Asp). It catalyzes de novo C–C bond formation between glutamate and tyrosine in PqqA, but only when PqqA is presented by PqqD. *"PqqE activity is dependent on the accessory protein PqqD"* ([PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/)); *"The auxiliary cluster nearest the RS site (AuxI) is in the form of a 2Fe-2S cluster ligated by four cysteines"* ([PMID: 29405700](https://pubmed.ncbi.nlm.nih.gov/29405700/)); PqqD is identified as *"the RiPP precursor peptide recognition element (RRE)"* ([PMID: 28481092](https://pubmed.ncbi.nlm.nih.gov/28481092/)).

### Finding 3 — PqqB is an iron-dependent hydroxylase; PqqC is a metal-free 8-electron oxidase; a protease is required

*"PqqB is an iron-dependent hydroxylase catalyzing oxygen-insertion reactions that are proposed to produce the quinone moiety of the mature PQQ cofactor"* ([PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)). *"PqqC is unusual in that it transfers redox equivalents to molecular oxygen without the assistance of a redox active metal or cofactor"* ([PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/)). The requirement for proteolytic excision of *"an early, cross-linked di-amino acid precursor"* is documented, along with its historical uncertainty ([PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)).

### Finding 4 — PqqD is part of the deep, widespread RRE superfamily, and the operon is condition-regulated

*"Half of the prokaryotic RiPP classes include a protein domain called the RiPP Recognition Element (RRE)"* ([PMID: 36682862](https://pubmed.ncbi.nlm.nih.gov/36682862/)); RRE-Finder *"retrieved ∼25,000 high-confidence RREs spanning all characterized RRE-dependent RiPP classes"* ([PMID: 32873609](https://pubmed.ncbi.nlm.nih.gov/32873609/)). Operon organization varies—*"Serratia sp. S119 contains a pqq operon composed of six genes (pqqA,B,C,D,E,F) and two promoters"*—and is induced under phosphate limitation ([PMID: 28709697](https://pubmed.ncbi.nlm.nih.gov/28709697/)); output is demand-tuned, as *"the levels of expression of the pqqF and pqqB genes mirror the levels of PQQ synthesized"* ([PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/)).

## 9. Limitations and Knowledge Gaps

- **Composite pathway.** The consensus mechanism is stitched together from multiple organisms with differing operon and protease architectures; a single fully reconstituted, one-organism, start-to-finish in-vitro pathway has not been the basis of most claims here.
- **Unresolved step order.** Proteolysis vs. PqqB oxygenation ordering is unsettled, so any linear diagram is provisional at the middle stages.
- **PqqB details.** Substrate identity, number of oxygen insertions, and coupling to PqqC's substrate are incompletely defined.
- **In-vivo reductant for PqqE** is unknown.
- **This review is literature-derived.** No primary experimental dataset was analyzed; conclusions reflect published biochemistry, structural biology, and genome mining, and inherit those studies' assay-system limitations (e.g., anaerobic reconstitution, surrogate reductants, mutant-trapped intermediates).

## 10. Proposed Follow-up Experiments / Actions

1. **Order-of-events resolution.** Reconstitute the full pathway in a single organism's proteins in vitro and use time-resolved LC-MS to test whether PqqB acts before or after PqqF/PqqG excision, and whether PqqB accepts peptide-bound vs. free substrate.
2. **PqqB mechanism.** Determine PqqB's true substrate and count oxygen insertions using ¹⁸O₂ labeling; obtain a substrate/product co-structure to localize the iron site and oxygenation chemistry.
3. **Native PqqE reductant.** Identify the physiological electron donor by pull-downs/genetics and test candidate flavodoxin/ferredoxin partners in reconstitution.
4. **Protease survey.** Systematically map, across genomes, which producers use single-chain PqqF, PqqF/PqqG M16B, or housekeeping peptidases, and validate substitutes by knockout/complementation.
5. **Intermediate isolation.** Trap and structurally characterize the intermediates between cross-linking and AHQQ to test the proposed Schiff-base and dioxygenation steps directly.
6. **Regulatory logic.** Dissect how phosphate- and glucose-responsive regulators couple *pqq* transcription to dehydrogenase demand across lineages.

## 11. Key References

- Biogenesis of the peptide-derived redox cofactor PQQ — [PMID: 32731194](https://pubmed.ncbi.nlm.nih.gov/32731194/)
- Two-component protease in PQQ biosynthesis; RiPP framing; protease gap — [PMID: 31427437](https://pubmed.ncbi.nlm.nih.gov/31427437/)
- PqqE catalyzes de novo C–C cross-link, PqqD-dependent — [PMID: 26961875](https://pubmed.ncbi.nlm.nih.gov/26961875/)
- X-ray/EPR of PqqE auxiliary Fe-S clusters — [PMID: 29405700](https://pubmed.ncbi.nlm.nih.gov/29405700/); [PMID: 31769977](https://pubmed.ncbi.nlm.nih.gov/31769977/)
- PqqE is a radical-SAM enzyme (Klebsiella) — [PMID: 19746930](https://pubmed.ncbi.nlm.nih.gov/19746930/); methods — [PMID: 30097100](https://pubmed.ncbi.nlm.nih.gov/30097100/)
- PqqD as RRE; NMR structure/binding — [PMID: 28481092](https://pubmed.ncbi.nlm.nih.gov/28481092/); [PMID: 27638737](https://pubmed.ncbi.nlm.nih.gov/27638737/)
- PqqB hydroxylase "missing link" — [PMID: 30811189](https://pubmed.ncbi.nlm.nih.gov/30811189/)
- PqqC structure/mechanism; trapped intermediate — [PMID: 15148379](https://pubmed.ncbi.nlm.nih.gov/15148379/); [PMID: 20602352](https://pubmed.ncbi.nlm.nih.gov/20602352/)
- Structural overview of the pathway — [PMID: 18371220](https://pubmed.ncbi.nlm.nih.gov/18371220/)
- RRE breadth and origin — [PMID: 36682862](https://pubmed.ncbi.nlm.nih.gov/36682862/); [PMID: 32873609](https://pubmed.ncbi.nlm.nih.gov/32873609/)
- PqqE-like radical-SAM in mycofactocin (related system) — [PMID: 21223593](https://pubmed.ncbi.nlm.nih.gov/21223593/)
- Operon regulation: phosphate limitation and glucose/demand tuning — [PMID: 28709697](https://pubmed.ncbi.nlm.nih.gov/28709697/); [PMID: 27287323](https://pubmed.ncbi.nlm.nih.gov/27287323/); [PMID: 23596526](https://pubmed.ncbi.nlm.nih.gov/23596526/)
- Downstream quinoprotein/lanthanide biology (adjacent) — [PMID: 27573017](https://pubmed.ncbi.nlm.nih.gov/27573017/); [PMID: 26833413](https://pubmed.ncbi.nlm.nih.gov/26833413/); [PMID: 32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/)
- Eukaryotic "vitamin-like" biology (adjacent) — [PMID: 34680074](https://pubmed.ncbi.nlm.nih.gov/34680074/); [PMID: 30322941](https://pubmed.ncbi.nlm.nih.gov/30322941/); [PMID: 17029795](https://pubmed.ncbi.nlm.nih.gov/17029795/); [PMID: 9706222](https://pubmed.ncbi.nlm.nih.gov/9706222/)


## Artifacts

- [OpenScientist final report](pqq_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pqq_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32731194
2. PMID:31427437
3. PMID:27573017
4. PMID:26833413
5. PMID:32345644
6. PMID:34680074
7. PMID:30322941
8. PMID:17029795
9. PMID:21223593
10. PMID:9706222
11. PMID:18371220
12. PMID:28481092
13. PMID:27638737
14. PMID:26961875
15. PMID:32873609
16. PMID:36682862
17. PMID:29405700
18. PMID:31769977
19. PMID:19746930
20. PMID:30097100
21. PMID:30811189
22. PMID:15148379
23. PMID:20602352
24. PMID:28709697
25. PMID:27287323
26. PMID:23596526
27. PMID:38767475