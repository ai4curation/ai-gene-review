---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T07:02:31.632767'
end_time: '2026-07-23T07:40:29.660935'
duration_seconds: 2278.03
template_file: templates/module_research.md.j2
template_variables:
  module_title: Type-II fatty-acid synthesis
  module_summary: A reusable dissociated bacterial fatty-acid synthase pathway that
    forms malonyl-CoA with acetyl-CoA carboxylase, loads malonate onto acyl carrier
    protein, initiates an acyl-ACP chain, and iteratively elongates that chain through
    condensation, beta-keto reduction, dehydration, and enoyl reduction. A FabA/FabB
    branch introduces and extends cis unsaturation. Enzyme-family and cofactor variants
    are represented explicitly rather than collapsed into a type-I fatty-acid synthase.
  module_outline: "- Type-II fatty-acid synthesis\n  - 1. malonyl-CoA formation\n\
    \  - Acetyl-CoA carboxylase\n    - Heteromeric acetyl-CoA carboxylase (molecular\
    \ player: bacterial AccABCD acetyl-CoA carboxylase; activity or role: acetyl-CoA\
    \ carboxylase activity)\n  - 2. acyl-group carriage\n  - Acyl carrier protein\n\
    \    - Holo-acyl carrier protein (molecular player: PSEPK canonical AcpP; activity\
    \ or role: acyl carrier activity)\n  - 3. malonyl-ACP formation\n  - FabD malonyl-ACP\
    \ loading\n    - Malonyl-CoA:ACP transacylase (molecular player: PSEPK canonical\
    \ FabD; activity or role: acyl-carrier-protein S-malonyltransferase activity)\n\
    \  - 4. fatty-acid chain initiation\n  - KAS-III-type chain initiation\n    -\
    \ Beta-ketoacyl-ACP synthase III initiator (molecular player: PSEPK PP_4379 chain-initiation\
    \ candidate; activity or role: beta-ketoacyl-acyl-carrier-protein synthase III\
    \ activity)\n  - 5. iterative acyl-chain elongation\n  - Four-reaction FAS-II\
    \ elongation cycle\n    - 1. decarboxylative condensation\n    - KAS-I/KAS-II\
    \ condensation\n      - Iterative decarboxylative condensation (molecular player:\
    \ 3-oxoacyl-acyl-carrier-protein synthase activity; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ synthase activity)\n      - Alternative versions by condensing enzyme: Elongation\
    \ condensing-enzyme variants\n        - FabB KAS-I\n          - FabB 3-oxoacyl-ACP\
    \ synthase (molecular player: PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ synthase activity)\n        - FabF KAS-II\n          - FabF 3-oxoacyl-ACP synthase\
    \ (molecular player: PSEPK FabF; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ synthase activity)\n        - PP_3303 KAS-II candidate\n          - PP_3303\
    \ 3-oxoacyl-ACP synthase candidate (molecular player: PSEPK PP_3303; activity\
    \ or role: 3-oxoacyl-acyl-carrier-protein synthase activity)\n    - 2. beta-keto\
    \ reduction\n    - 3-oxoacyl-ACP reduction\n      - NADPH-dependent beta-keto\
    \ reduction (molecular player: 3-oxoacyl-acyl-carrier-protein reductase (NADPH)\
    \ activity; activity or role: 3-oxoacyl-acyl-carrier-protein reductase (NADPH)\
    \ activity)\n      - Alternative versions by reductase paralog: 3-oxoacyl-ACP\
    \ reductase variants\n        - Canonical FabG\n          - FabG 3-oxoacyl-ACP\
    \ reductase (molecular player: PSEPK FabG; activity or role: 3-oxoacyl-acyl-carrier-protein\
    \ reductase (NADPH) activity)\n        - PP_0581 reductase candidate\n       \
    \   - PP_0581 3-oxoacyl-ACP reductase candidate (molecular player: PSEPK PP_0581)\n\
    \    - 3. 3-hydroxyacyl dehydration\n    - 3-hydroxyacyl-ACP dehydration\n   \
    \   - Elongation-cycle dehydration (molecular player: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity)\n      - Alternative versions by dehydratase family: FAS-II\
    \ dehydratase variants\n        - FabZ dehydratase\n          - FabZ 3-hydroxyacyl-ACP\
    \ dehydratase (molecular player: PSEPK FabZ; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity)\n        - FabA dehydratase\n          - FabA 3-hydroxyacyl-ACP\
    \ dehydratase (molecular player: PSEPK FabA; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein\
    \ dehydratase activity)\n    - 4. enoyl reduction\n    - Enoyl-ACP reduction\n\
    \      - Elongation-cycle enoyl reduction (molecular player: enoyl-acyl-carrier-protein\
    \ reductase activity)\n      - Alternative versions by electron donor and enzyme\
    \ family: Enoyl-ACP reductase variants\n        - FabV NADH-dependent reductase\n\
    \          - FabV enoyl-ACP reductase (molecular player: PSEPK FabV; activity\
    \ or role: enoyl-acyl-carrier-protein reductase (NADH) activity)\n        - PP_1852\
    \ NADPH-dependent reductase\n          - PP_1852 enoyl-ACP reductase candidate\
    \ (molecular player: PSEPK PP_1852; activity or role: enoyl-acyl-carrier-protein\
    \ reductase (NADPH) activity)\n  - 6. cis-unsaturated fatty-acid branch\n  - FabA/FabB\
    \ cis-unsaturated branch\n    - 1. trans-2 to cis-3 isomerization\n    - FabA\
    \ trans-2-decenoyl-ACP isomerization\n      - FabA trans-2-decenoyl-ACP isomerase\
    \ (molecular player: PSEPK FabA; activity or role: trans-2-decenoyl-acyl-carrier-protein\
    \ isomerase activity)\n    - 2. cis-unsaturated chain extension\n    - FabB unsaturated-chain\
    \ condensation\n      - FabB cis-unsaturated chain elongation (molecular player:\
    \ PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)"
  module_connections: '- Acetyl-CoA carboxylase feeds into FabD malonyl-ACP loading:
    AccABCD supplies malonyl-CoA to FabD.

    - Acyl carrier protein feeds into FabD malonyl-ACP loading: Holo-ACP accepts malonate
    from FabD.

    - FabD malonyl-ACP loading feeds into KAS-III-type chain initiation: Malonyl-ACP
    is the two-carbon donor for chain initiation.

    - KAS-III-type chain initiation feeds into Four-reaction FAS-II elongation cycle:
    The initiated beta-ketoacyl-ACP enters reductive elongation.

    - Four-reaction FAS-II elongation cycle feeds into FabA/FabB cis-unsaturated branch:
    A C10 trans-2-enoyl-ACP intermediate can enter the FabA/FabB branch.

    - KAS-I/KAS-II condensation feeds into 3-oxoacyl-ACP reduction: Condensation produces
    3-oxoacyl-ACP for reduction.

    - 3-oxoacyl-ACP reduction feeds into 3-hydroxyacyl-ACP dehydration: Reduction
    produces 3-hydroxyacyl-ACP for dehydration.

    - 3-hydroxyacyl-ACP dehydration feeds into Enoyl-ACP reduction: Dehydration produces
    trans-2-enoyl-ACP for reduction.

    - Enoyl-ACP reduction feeds into KAS-I/KAS-II condensation: The saturated acyl-ACP
    product re-enters another elongation round.

    - FabA trans-2-decenoyl-ACP isomerization feeds into FabB unsaturated-chain condensation:
    FabA supplies cis-3-decenoyl-ACP to FabB.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 26
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: type_ii_fatty_acid_synthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: type_ii_fatty_acid_synthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Type-II fatty-acid synthesis

## Working Scope

A reusable dissociated bacterial fatty-acid synthase pathway that forms malonyl-CoA with acetyl-CoA carboxylase, loads malonate onto acyl carrier protein, initiates an acyl-ACP chain, and iteratively elongates that chain through condensation, beta-keto reduction, dehydration, and enoyl reduction. A FabA/FabB branch introduces and extends cis unsaturation. Enzyme-family and cofactor variants are represented explicitly rather than collapsed into a type-I fatty-acid synthase.

## Provisional Biological Outline

- Type-II fatty-acid synthesis
  - 1. malonyl-CoA formation
  - Acetyl-CoA carboxylase
    - Heteromeric acetyl-CoA carboxylase (molecular player: bacterial AccABCD acetyl-CoA carboxylase; activity or role: acetyl-CoA carboxylase activity)
  - 2. acyl-group carriage
  - Acyl carrier protein
    - Holo-acyl carrier protein (molecular player: PSEPK canonical AcpP; activity or role: acyl carrier activity)
  - 3. malonyl-ACP formation
  - FabD malonyl-ACP loading
    - Malonyl-CoA:ACP transacylase (molecular player: PSEPK canonical FabD; activity or role: acyl-carrier-protein S-malonyltransferase activity)
  - 4. fatty-acid chain initiation
  - KAS-III-type chain initiation
    - Beta-ketoacyl-ACP synthase III initiator (molecular player: PSEPK PP_4379 chain-initiation candidate; activity or role: beta-ketoacyl-acyl-carrier-protein synthase III activity)
  - 5. iterative acyl-chain elongation
  - Four-reaction FAS-II elongation cycle
    - 1. decarboxylative condensation
    - KAS-I/KAS-II condensation
      - Iterative decarboxylative condensation (molecular player: 3-oxoacyl-acyl-carrier-protein synthase activity; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
      - Alternative versions by condensing enzyme: Elongation condensing-enzyme variants
        - FabB KAS-I
          - FabB 3-oxoacyl-ACP synthase (molecular player: PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
        - FabF KAS-II
          - FabF 3-oxoacyl-ACP synthase (molecular player: PSEPK FabF; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
        - PP_3303 KAS-II candidate
          - PP_3303 3-oxoacyl-ACP synthase candidate (molecular player: PSEPK PP_3303; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
    - 2. beta-keto reduction
    - 3-oxoacyl-ACP reduction
      - NADPH-dependent beta-keto reduction (molecular player: 3-oxoacyl-acyl-carrier-protein reductase (NADPH) activity; activity or role: 3-oxoacyl-acyl-carrier-protein reductase (NADPH) activity)
      - Alternative versions by reductase paralog: 3-oxoacyl-ACP reductase variants
        - Canonical FabG
          - FabG 3-oxoacyl-ACP reductase (molecular player: PSEPK FabG; activity or role: 3-oxoacyl-acyl-carrier-protein reductase (NADPH) activity)
        - PP_0581 reductase candidate
          - PP_0581 3-oxoacyl-ACP reductase candidate (molecular player: PSEPK PP_0581)
    - 3. 3-hydroxyacyl dehydration
    - 3-hydroxyacyl-ACP dehydration
      - Elongation-cycle dehydration (molecular player: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
      - Alternative versions by dehydratase family: FAS-II dehydratase variants
        - FabZ dehydratase
          - FabZ 3-hydroxyacyl-ACP dehydratase (molecular player: PSEPK FabZ; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
        - FabA dehydratase
          - FabA 3-hydroxyacyl-ACP dehydratase (molecular player: PSEPK FabA; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
    - 4. enoyl reduction
    - Enoyl-ACP reduction
      - Elongation-cycle enoyl reduction (molecular player: enoyl-acyl-carrier-protein reductase activity)
      - Alternative versions by electron donor and enzyme family: Enoyl-ACP reductase variants
        - FabV NADH-dependent reductase
          - FabV enoyl-ACP reductase (molecular player: PSEPK FabV; activity or role: enoyl-acyl-carrier-protein reductase (NADH) activity)
        - PP_1852 NADPH-dependent reductase
          - PP_1852 enoyl-ACP reductase candidate (molecular player: PSEPK PP_1852; activity or role: enoyl-acyl-carrier-protein reductase (NADPH) activity)
  - 6. cis-unsaturated fatty-acid branch
  - FabA/FabB cis-unsaturated branch
    - 1. trans-2 to cis-3 isomerization
    - FabA trans-2-decenoyl-ACP isomerization
      - FabA trans-2-decenoyl-ACP isomerase (molecular player: PSEPK FabA; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)
    - 2. cis-unsaturated chain extension
    - FabB unsaturated-chain condensation
      - FabB cis-unsaturated chain elongation (molecular player: PSEPK FabB; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)

## Known Relationships Among Steps

- Acetyl-CoA carboxylase feeds into FabD malonyl-ACP loading: AccABCD supplies malonyl-CoA to FabD.
- Acyl carrier protein feeds into FabD malonyl-ACP loading: Holo-ACP accepts malonate from FabD.
- FabD malonyl-ACP loading feeds into KAS-III-type chain initiation: Malonyl-ACP is the two-carbon donor for chain initiation.
- KAS-III-type chain initiation feeds into Four-reaction FAS-II elongation cycle: The initiated beta-ketoacyl-ACP enters reductive elongation.
- Four-reaction FAS-II elongation cycle feeds into FabA/FabB cis-unsaturated branch: A C10 trans-2-enoyl-ACP intermediate can enter the FabA/FabB branch.
- KAS-I/KAS-II condensation feeds into 3-oxoacyl-ACP reduction: Condensation produces 3-oxoacyl-ACP for reduction.
- 3-oxoacyl-ACP reduction feeds into 3-hydroxyacyl-ACP dehydration: Reduction produces 3-hydroxyacyl-ACP for dehydration.
- 3-hydroxyacyl-ACP dehydration feeds into Enoyl-ACP reduction: Dehydration produces trans-2-enoyl-ACP for reduction.
- Enoyl-ACP reduction feeds into KAS-I/KAS-II condensation: The saturated acyl-ACP product re-enters another elongation round.
- FabA trans-2-decenoyl-ACP isomerization feeds into FabB unsaturated-chain condensation: FabA supplies cis-3-decenoyl-ACP to FabB.

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

# Type-II Fatty-Acid Synthesis (FAS-II): A Dissociated Bacterial Pathway — A Review

## 1. Executive Summary

Type-II fatty-acid synthesis (FAS-II) is the bacterial route to *de novo* fatty acids. Its defining feature is architectural: unlike the single multifunctional megasynthase of animals and fungi (type-I FAS), FAS-II is **dissociated** — every catalytic step is carried out by a separate, freely diffusing, mono-functional protein, and the growing acyl chain is passed between them while covalently tethered to a small, acidic acyl carrier protein (ACP) through a 4′-phosphopantetheine (4′-PP) arm ([PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/); [PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/)). This modularity is not a mere biochemical curiosity: it makes individual steps genetically and pharmacologically addressable and underlies the appeal of FAS-II as an antibacterial target.

The chemistry of the pathway is rigidly conserved and can be stated compactly. Acetyl-CoA carboxylase (ACC, the AccABCD complex) produces malonyl-CoA; FabD transfers the malonyl group to holo-ACP; a KAS-III enzyme (FabH) initiates the first chain by condensing acetyl-CoA with malonyl-ACP; and a fixed four-reaction elongation cycle — decarboxylative condensation (FabB/FabF), NADPH-dependent β-keto reduction (FabG), (3R)-hydroxyacyl dehydration (FabZ/FabA), and enoyl reduction (FabI/FabK/FabL/FabV) — extends the chain two carbons at a time. A conditional FabA/FabB branch introduces *cis* double bonds anaerobically without an oxygen-dependent desaturase. The **order** of these reactions is dictated by substrate chemistry and is essentially invariant across bacteria.

What varies, and varies extensively, is **which protein family and cofactor fill each slot**. The clearest illustration is the enoyl-ACP reductase step, performed by at least four non-homologous families (FabI, FabK, FabL, FabV) with divergent cofactor use and inhibitor sensitivity ([PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/); [PMID: 18193820](https://pubmed.ncbi.nlm.nih.gov/18193820/)). The unsaturated-fatty-acid branch is similarly implemented by non-orthologous but functionally matched pairs — FabA/FabB in *E. coli*, FabN/FabO in *Enterococcus faecalis* ([PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/)). Finally, the biological importance of the whole system is **conditional**: many Gram-positive pathogens scavenge host fatty acids and can bypass FAS-II inhibition entirely, so essentiality — and therefore drug-target value — is context-dependent ([PMID: 34309397](https://pubmed.ncbi.nlm.nih.gov/34309397/); [PMID: 38014966](https://pubmed.ncbi.nlm.nih.gov/38014966/)). This review synthesizes five confirmed findings into a coherent picture of a pathway that is chemically stereotyped but molecularly plastic.

---

## 2. Definition and Biological Boundaries

### What is included

FAS-II is the set of discrete enzymes and carrier proteins that, starting from acetyl-CoA and bicarbonate/ATP, build saturated and *cis*-unsaturated acyl-ACP products of physiologically appropriate chain length (typically C14–C18) that are then handed to membrane-phospholipid biosynthesis. The system comprises:

- **Priming:** acetyl-CoA carboxylase (AccABCD) → malonyl-CoA.
- **Carrier activation and loading:** ACP (holo-AcpP) and FabD (malonyl-CoA:ACP transacylase) → malonyl-ACP.
- **Initiation:** a KAS-III enzyme (FabH) → the first β-ketoacyl-ACP.
- **Iterative elongation:** the four-reaction cycle (condensation → keto-reduction → dehydration → enoyl-reduction).
- **Unsaturation branch:** the FabA/FabB (or equivalent) route to *cis*-unsaturated chains.

### What is adjacent but should be treated separately

Several processes are mechanistically related or historically conflated with FAS-II but fall outside its boundary:

- **Type-I FAS (FAS-I).** The animal/fungal megasynthase performs the same chemistry within one (or a few) large multifunctional polypeptides. It is the architectural counterpoint to FAS-II, not a variant of it ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/); [PMID: 30248156](https://pubmed.ncbi.nlm.nih.gov/30248156/)). Some lineages carry both: *Mycobacterium* uses FAS-I to make medium-chain acyl-CoA primers that FAS-II then **elongates** to very long meromycolate chains ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/); [PMID: 11278743](https://pubmed.ncbi.nlm.nih.gov/11278743/)).
- **Mitochondrial FAS-II (mtFAS).** Eukaryotic mitochondria retain a bacterial-type, ACP-dependent FAS-II that is essential for respiration and supplies octanoyl-ACP for lipoic-acid synthesis; it is a distinct cellular system that happens to be homologous to bacterial FAS-II ([PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/); [PMID: 19686777](https://pubmed.ncbi.nlm.nih.gov/19686777/)).
- **Polyketide synthases (PKS) and non-ribosomal peptide synthetases (NRPS).** These use the same ACP/4′-PP chemistry and share the four-helix-bundle carrier fold, but produce secondary metabolites, not membrane fatty acids ([PMID: 37345808](https://pubmed.ncbi.nlm.nih.gov/37345808/); [PMID: 28187530](https://pubmed.ncbi.nlm.nih.gov/28187530/)).
- **β-Oxidation and exogenous-fatty-acid incorporation.** These are catabolic/salvage routes that intersect FAS-II regulation (via FadR) and can substitute for it physiologically, but they are not part of the synthetic pathway ([PMID: 33283913](https://pubmed.ncbi.nlm.nih.gov/33283913/); [PMID: 38014966](https://pubmed.ncbi.nlm.nih.gov/38014966/)).

### Competing definitions

The main definitional tension in the literature is whether FAS-II denotes (a) the strict *de novo* pathway from acetyl-CoA or (b) any dissociated ACP-dependent acyl-chain-elongation system. Mycobacterial FAS-II fits (b) but not (a) — it cannot initiate *de novo* synthesis and only elongates FAS-I products ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/)). We treat the dissociated, ACP-dependent architecture as the defining criterion, noting that initiation capacity is lineage-variable.

---

## 3. Mechanistic Overview

The best current model is a strictly ordered, iterative cycle. The order is enforced by substrate chemistry: each enzyme acts only on the product of the previous step.

```
 Acetyl-CoA + HCO3- + ATP
        │  ACC (AccABCD)  ── biotin carboxylase + carboxyltransferase
        ▼
   Malonyl-CoA
        │  FabD (malonyl-CoA:ACP transacylase)     Holo-AcpP (4'-PP arm)
        ▼                                              ▲ AcpS adds 4'-PP from CoA
   Malonyl-ACP ◄───────────────────────────────────────┘
        │  FabH (KAS-III): acetyl-CoA + malonyl-ACP → C4 β-ketoacyl-ACP + CO2
        ▼
 ┌───────────────── FOUR-REACTION ELONGATION CYCLE ─────────────────┐
 │  (1) Condensation      FabB / FabF (KAS-I/II)                     │
 │        acyl-ACP + malonyl-ACP → β-ketoacyl-ACP(+2C) + CO2         │
 │  (2) Keto-reduction    FabG  (NADPH)                              │
 │        β-ketoacyl-ACP → (3R)-hydroxyacyl-ACP                      │
 │  (3) Dehydration       FabZ (all rounds) / FabA (specific)        │
 │        (3R)-hydroxyacyl-ACP → trans-2-enoyl-ACP                   │
 │  (4) Enoyl-reduction   FabI / FabK / FabL / FabV  (NADH or NADPH) │
 │        trans-2-enoyl-ACP → saturated acyl-ACP(+2C)               │
 └──────────────────────────┬───────────────────────────────────────┘
                            │ re-enters cycle (elongate)
                            │
        At C10, trans-2-decenoyl-ACP may branch:
                            ▼
   FabA (isomerase): trans-2-decenoyl-ACP → cis-3-decenoyl-ACP
                            │
                            ▼
   FabB (KAS-I): elongates cis intermediate → cis-unsaturated fatty acids
                            ▼
        Acyl-ACP products (C16:0, C16:1, C18:1 ...) → phospholipid synthesis
```

**Obligatory steps:** priming (ACC), loading (FabD), initiation (a KAS-III or equivalent primer-generating activity), and the four elongation reactions. Without any of these, chain assembly cannot proceed. The condensation → keto-reduction → dehydration → enoyl-reduction order is chemically obligatory: keto-reduction requires the β-keto group that condensation produces; dehydration requires the 3-hydroxy group that keto-reduction produces; enoyl-reduction requires the trans-2 double bond that dehydration produces ([PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/); [PMID: 23322253](https://pubmed.ncbi.nlm.nih.gov/23322253/)).

**Conditional steps:** the FabA/FabB unsaturation branch is engaged only when *cis*-unsaturated chains are needed and only in lineages that use the anaerobic mechanism. It is a diversion from, not a replacement of, the core cycle ([PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/); [PMID: 36515967](https://pubmed.ncbi.nlm.nih.gov/36515967/)).

**Accessory activities:** ACP maturation (AcpS adds 4′-PP; AcpH removes it), branched-chain and hydroxy-fatty-acid tailoring, and regulatory inputs (FadR, FabR) tune output but are not part of the core catalytic cycle ([PMID: 37345808](https://pubmed.ncbi.nlm.nih.gov/37345808/); [PMID: 33283913](https://pubmed.ncbi.nlm.nih.gov/33283913/); [PMID: 32535524](https://pubmed.ncbi.nlm.nih.gov/32535524/)).

---

## 4. Major Molecular Players and Active Assemblies

### Finding F001 — FAS-II is a dissociated multi-enzyme system distinct from type-I FAS

The foundational fact about FAS-II is architectural. Multiple authoritative reviews establish that in most bacteria fatty acids are made by a group of highly conserved, discrete, mono-functional, freely diffusible proteins — "*Fatty acid biosynthesis is catalyzed in most bacteria by a group of highly conserved proteins known as the type II fatty acid synthase (FAS II) system*" ([PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/)). This is explicitly contrasted with the eukaryotic-type multifunctional FAS-I: the two systems are "*the eukaryotic-like multifunctional enzyme FAS I and the acyl carrier protein (ACP)-dependent FAS II systems, which consists of a series of discrete mono-functional proteins, each catalyzing one reaction in the pathway*" ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/)). The dissociated design means each reaction is a separate gene product, and the growing chain is shuttled among them on ACP. Crucially, this same source documents a lineage-specific departure: "*the mycobacterial FAS II is incapable of de novo fatty acid synthesis from acetyl-coenzyme A, but instead elongates medium-chain-length fatty acids previously synthesized by FAS I*" ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/)). Thus even the "initiation" boundary of the system is variable.

### Finding F002 — Holo-ACP with a 4′-phosphopantetheine arm is the central shuttle

The pathway's logic depends on a single small carrier protein. Apo-ACP is converted to holo-ACP by AcpS-catalyzed transfer of the 4′-PP prosthetic group from coenzyme A; acyl intermediates are then thioesterified to the terminal thiol of that arm. The chain length carried on the arm governs the protein's behaviour and partner recognition: "*The addition of the 4′PP prosthetic group converts apo-AcpP to holo-AcpP (commonly referred to as AcpP). Acylation of the 4′PP prosthetic group gives acyl-AcpP species. The length of the acyl chain determines the properties of the acyl-AcpP*" ([PMID: 37345808](https://pubmed.ncbi.nlm.nih.gov/37345808/)). ACP is a small acidic four-helix bundle used across FAS, PKS and NRPS systems, and structural studies of freestanding and doublet ACPs confirm the conserved fold and the phosphopantetheinylation-dependent dynamics ([PMID: 28187530](https://pubmed.ncbi.nlm.nih.gov/28187530/); [PMID: 33416314](https://pubmed.ncbi.nlm.nih.gov/33416314/); [PMID: 32128972](https://pubmed.ncbi.nlm.nih.gov/32128972/)). Because every catalytic step reads the chain off the same carrier, ACP is simultaneously a substrate presenter and a specificity determinant — the physical hub that makes a "dissociated" pathway function as an integrated system.

### Table: Core FAS-II enzymes and their reactions

| Step | Reaction | Prototype enzyme(s) | Cofactor | Notes |
|------|----------|---------------------|----------|-------|
| Priming | acetyl-CoA → malonyl-CoA | ACC (AccABCD) | ATP, biotin, HCO₃⁻ | Heteromeric in most bacteria; AccC is a drug-target node |
| Carrier | apo-ACP → holo-ACP | AcpS (adds 4′-PP) | CoA | AcpH reverses |
| Loading | malonyl-CoA → malonyl-ACP | FabD | — | Malonyl-CoA:ACP transacylase |
| Initiation | acetyl-CoA + malonyl-ACP → C4 β-ketoacyl-ACP | FabH (KAS-III) | — | Substrate specificity sets branching/chain start |
| Condensation | acyl-ACP + malonyl-ACP → β-ketoacyl-ACP(+2C) | FabB (KAS-I), FabF (KAS-II) | — | FabB also serves the UFA branch |
| Keto-reduction | β-ketoacyl-ACP → (3R)-hydroxyacyl-ACP | FabG | NADPH | Highly conserved |
| Dehydration | (3R)-hydroxyacyl-ACP → trans-2-enoyl-ACP | FabZ (general), FabA (bifunctional) | — | FabA also isomerizes |
| Enoyl-reduction | trans-2-enoyl-ACP → acyl-ACP(+2C) | FabI, FabK, FabL, FabV | NADH or NADPH | Non-homologous families (F003) |
| UFA branch | trans-2- → cis-3-decenoyl-ACP; elongation | FabA + FabB (or FabN + FabO) | — | Conditional; anaerobic (F004) |

### The initiation enzyme (KAS-III/FabH)

FabH condenses an acyl-CoA primer with malonyl-ACP and thereby sets the starting chain and, in some organisms, the branch pattern. The structure of *M. tuberculosis* FabH illustrates how substrate specificity is tuned: mtFabH accepts long-chain acyl-CoA (e.g. C14 myristoyl-CoA) rather than acetyl-CoA because a hydrophobic channel that is blocked by phenylalanine in *E. coli* FabH is opened by a threonine substitution, while a capping helix limits the product to ~C16 ([PMID: 11278743](https://pubmed.ncbi.nlm.nih.gov/11278743/)). FabH is an actively pursued antibacterial target, with diverse synthetic inhibitor scaffolds reported over 2006–2025 ([PMID: 42446656](https://pubmed.ncbi.nlm.nih.gov/42446656/)).

---

## 5. Evolutionary and Cell-Biological Variation

### Finding F003 — Enoyl-ACP reductase is functionally convergent but family-variable

The most striking example of molecular plasticity is the final elongation step. The same chemical transformation — reduction of the trans-2 double bond — is carried out by **non-homologous** isozyme families with different cofactor preferences and inhibitor sensitivities:

- **FabI** — NADH-dependent, triclosan-sensitive, the *E. coli* prototype and the target of isoniazid, diazaborines and triclosan ([PMID: 18193820](https://pubmed.ncbi.nlm.nih.gov/18193820/)).
- **FabV** — NADH-dependent but triclosan-**resistant**; present in *Vibrio cholerae* and *Pseudomonas aeruginosa*.
- **FabK** — flavin-dependent and structurally unrelated.
- **FabL** — an additional SDR-family variant.

The physiological consequence of this substitution is dramatic. In *P. aeruginosa* PAO1, "*P. aeruginosa contains two enoyl-ACP reductase isozymes, the previously characterized FabI homologue plus a homologue of FabV, a triclosan-resistant enoyl-ACP reductase recently demonstrated in Vibrio cholerae*" ([PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/)), and deletion of *fabV* rendered the strain "*extremely sensitive to triclosan (>2,000-fold more sensitive than the wild-type strain)*" ([PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/)). This shows that intrinsic triclosan resistance in this organism is due to the identity of the enoyl reductase, not efflux. FabI's status as "*a validated but currently underexploited target for drug discovery*" ([PMID: 18193820](https://pubmed.ncbi.nlm.nih.gov/18193820/)) is therefore contingent on which reductase a given pathogen actually uses. The reductase steps generally — both FabG and the enoyl reductase — are recognized antimicrobial nodes ([PMID: 15726819](https://pubmed.ncbi.nlm.nih.gov/15726819/)). In *Sinorhizobium meliloti*, the balance among multiple FabI paralogs (FabI1 vs FabI2) even sets the unsaturated-fatty-acid content of the membrane, with FabI2 being indispensable and only complementable by the *E. faecalis fabI* gene ([PMID: 39627703](https://pubmed.ncbi.nlm.nih.gov/39627703/)).

### Finding F004 — The FabA/FabB anaerobic UFA branch is real but not universal

In *E. coli* and many γ-proteobacteria, *cis*-unsaturation is introduced **without oxygen or a desaturase**: the bifunctional dehydratase/isomerase FabA converts trans-2-decenoyl-ACP to cis-3-decenoyl-ACP, and the KAS-I condensing enzyme FabB preferentially elongates the *cis* intermediate, locking the double bond into the mature chain. This branch, however, is implemented differently across lineages and is not always essential. In *Xanthomonas*, "*the conserved FabA-FabB pathway is considered to be crucial for unsaturated fatty acid (UFA) synthesis in gram-negative bacteria*" yet was shown to be dispensable for UFA synthesis while instead modulating diffusible-signal-factor synthesis ([PMID: 36515967](https://pubmed.ncbi.nlm.nih.gov/36515967/)). In *Enterococcus faecalis*, the equivalent chemistry is supplied by a non-orthologous but functionally matched pair: "*FabO has been ascribed the same activity as E. coli FabB and we report in vitro evidence that this is the case, whereas FabN is a dehydratase/isomerase, having the activity of E. coli FabA*" ([PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/)). Critically, the reductase must be co-adapted: "*the enoyl-ACP reductase must be matched to the unsaturated fatty acid synthetic genes*" ([PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/)). More broadly, reviews note "*multiple mechanisms to generate unsaturated fatty acids and the accessory components required for branched-chain fatty acid synthesis in Gram-positive bacteria*" ([PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/)). The UFA branch is thus a **conserved outcome achieved by variable, matched enzyme sets** — a textbook case of non-orthologous gene displacement.

### Cell-biological and physiological variation

- **Both-systems lineages:** *Mycobacterium* runs FAS-I and FAS-II in series to build mycolic acids; *Streptomyces* has only FAS-II; *Corynebacterium* only FAS-I ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/); [PMID: 21204864](https://pubmed.ncbi.nlm.nih.gov/21204864/)).
- **Mitochondrial retention:** eukaryotic mitochondria keep a bacterial-type FAS-II essential for respiration and lipoic-acid synthesis ([PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/); [PMID: 19686777](https://pubmed.ncbi.nlm.nih.gov/19686777/)).
- **Temperature/physiological state:** UFA content is tuned for membrane fluidity via regulators such as FabR and FadR; in *Shewanella baltica*, cold adaptation is achieved by down-regulating FabR and up-regulating FadR ([PMID: 32535524](https://pubmed.ncbi.nlm.nih.gov/32535524/); [PMID: 33283913](https://pubmed.ncbi.nlm.nih.gov/33283913/)).

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering constraints

The four elongation reactions are locked in sequence by the functional groups they create and consume (see §3). This is why the pathway diagram is effectively a directed cycle with no shortcuts through the core: keto-reduction cannot precede condensation, dehydration cannot precede keto-reduction, and enoyl-reduction cannot precede dehydration. The UFA branch is constrained to a specific chain length — the isomerization operates on the C10 trans-2-decenoyl-ACP intermediate — because that is the intermediate FabA/FabN recognize and FabB/FabO can elongate ([PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/); [PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/)).

### Matching/compatibility constraints

The enoyl reductase and the UFA-synthesis enzymes must be co-adapted; a mismatch breaks UFA production ([PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/); [PMID: 39627703](https://pubmed.ncbi.nlm.nih.gov/39627703/)). ACP–partner recognition is chain-length dependent, so acyl intermediates are handed off in an ordered, length-gated fashion rather than promiscuously ([PMID: 37345808](https://pubmed.ncbi.nlm.nih.gov/37345808/)).

### Finding F005 — Essentiality and drug-target value are conditional on host fatty-acid scavenging

FAS-II is the validated target of isoniazid, triclosan, thiolactomycin and diazaborines, and both the ACC/AccC priming node and the FabH/FabI steps are actively pursued ([PMID: 26169404](https://pubmed.ncbi.nlm.nih.gov/26169404/); [PMID: 18193820](https://pubmed.ncbi.nlm.nih.gov/18193820/)). Bioluminescent cellular reporter assays have been built specifically to "*target the enzyme (AccC) catalyzing the biotin carboxylase half-reaction of the acetyl coenzyme A (acetyl-CoA) carboxylase step in the initiation phase of FASII*" ([PMID: 26169404](https://pubmed.ncbi.nlm.nih.gov/26169404/)). **However, the pathway's essentiality is not absolute.** Many Gram-positive pathogens incorporate exogenous host fatty acids via lipases, fatty-acid kinase systems and auxiliary ACPs, and can thereby bypass FAS-II inhibition. In *Enterococcus faecalis*, the FAS-II pathway and cyclopropane-ring formation were shown to be "*Dispensable during Enterococcus faecalis Systemic Infection*" ([PMID: 34309397](https://pubmed.ncbi.nlm.nih.gov/34309397/)) because the organism scavenges host fatty acids. The utilization of exogenous unsaturated fatty acids, mediated by bacterial lipases and buffered by human serum albumin, further modulates the impact of FAS-II inhibition ([PMID: 38014966](https://pubmed.ncbi.nlm.nih.gov/38014966/)). *E. faecalis* even maintains a dedicated auxiliary ACP (EfAcpB) for incorporating exogenous fatty acids alongside the FAS-essential EfAcpA ([PMID: 36410271](https://pubmed.ncbi.nlm.nih.gov/36410271/)). The practical corollary: **the value of FAS-II as a drug target depends on whether the pathogen, in its infection niche, can obtain fatty acids from the host.**

### Failure modes

- **Genetic loss/insufficiency:** loss of an obligatory enzyme is lethal unless salvage is available.
- **Regulatory imbalance:** overproduction of the master regulator FadR increases all acyl-chain yields but at a cost — larger cells, slower growth, intracellular membrane accumulation and abnormal morphology ("*too much FadR is bad*") ([PMID: 33283913](https://pubmed.ncbi.nlm.nih.gov/33283913/)).
- **Membrane consequences:** perturbing phospholipid composition/fluidity disrupts downstream processes such as MreB rotation ([PMID: 33330621](https://pubmed.ncbi.nlm.nih.gov/33330621/)); engineering elongation-gene expression (fabH/fabG/fabZ/fabI) reshapes chain-length and UFA output ([PMID: 23322253](https://pubmed.ncbi.nlm.nih.gov/23322253/)).

---

## 7. Controversies and Open Questions

1. **Where is the true boundary of "FAS-II"?** Mycobacterial FAS-II elongates rather than initiates, forcing a choice between an architecture-based definition (dissociated + ACP-dependent) and a function-based one (*de novo* from acetyl-CoA). We favour the architectural definition but flag that reviews mixing *E. coli* and *Mycobacterium* data can overgeneralize ([PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/)).

2. **How universal is the FabA/FabB anaerobic UFA route?** It is canonical in *E. coli*, dispensable in *Xanthomonas*, and replaced by FabN/FabO in *Enterococcus*. The literature has historically treated it as "the" Gram-negative UFA pathway; recent work shows this is an overstatement ([PMID: 36515967](https://pubmed.ncbi.nlm.nih.gov/36515967/); [PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/)).

3. **Is FAS-II a good antibacterial target?** The tension between validated inhibitors (isoniazid, triclosan) and host-fatty-acid bypass is unresolved and organism-specific. Target value must be assessed per pathogen and per infection niche, not asserted for bacteria in general ([PMID: 34309397](https://pubmed.ncbi.nlm.nih.gov/34309397/); [PMID: 38014966](https://pubmed.ncbi.nlm.nih.gov/38014966/)).

4. **Which enoyl reductase, and how redundant?** Organisms carrying multiple non-homologous reductases (e.g. FabI + FabV; multiple FabI paralogs in *Sinorhizobium*) complicate both mechanistic interpretation and inhibitor design ([PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/); [PMID: 39627703](https://pubmed.ncbi.nlm.nih.gov/39627703/)).

5. **The dynamics of chain-length gating on ACP.** How ACP's acyl-chain-dependent conformation dictates ordered partner hand-off — and how much of that is programmed versus emergent — remains only partly resolved structurally ([PMID: 37345808](https://pubmed.ncbi.nlm.nih.gov/37345808/); [PMID: 32128972](https://pubmed.ncbi.nlm.nih.gov/32128972/)).

6. **Evolutionary origin.** The dissociated, ACP-dependent design is ancient and conserved (retained even inside mitochondria), whereas the enoyl-reductase family and the UFA-branch enzyme pairs look like later, lineage-specific replacements. FabG (keto-reductase) and the core condensation/carrier machinery are the best candidates for the ancestral, conserved core; the enoyl-reductase slot is the most evolutionarily labile.

---

## 8. Limitations and Knowledge Gaps

- **Organism sampling bias.** Much mechanistic detail derives from *E. coli*; extrapolation to Gram-positives, actinomycetes and environmental bacteria should be cautious given documented non-orthologous displacements.
- **In vitro vs in vivo.** Enzyme kinetics and inhibitor potencies are often measured in isolated systems; in vivo relevance is modulated by redundancy, regulation and host-fatty-acid salvage.
- **Candidate assignments unverified.** The *Pseudomonas putida* (PSEPK) candidate genes named in the working scope (PP_4379, PP_3303, PP_0581, PP_1852) were not experimentally validated in this review; their slot assignments are provisional and rest on homology/annotation rather than functional data.
- **No new primary data.** This review synthesizes existing literature (29 papers); it does not generate new experimental evidence.

---

## 9. Proposed Follow-up Experiments / Actions

1. **Functionally validate the PSEPK candidates.** Test PP_4379 (KAS-III), PP_3303 (KAS-II), PP_0581 (FabG-like reductase) and PP_1852 (NADPH enoyl reductase) by heterologous complementation of *E. coli* conditional mutants (e.g. temperature-sensitive *fabI/fabB/fabH*) and in vitro assays with defined acyl-ACP substrates.
2. **Map enoyl-reductase redundancy per pathogen.** Systematically knock out each reductase family member and measure triclosan/AFN-1252 sensitivity, mirroring the *P. aeruginosa fabV* result, to define target vulnerability organism by organism.
3. **Quantify host-FA bypass.** Under infection-relevant fatty-acid supplementation (with serum albumin), test whether FAS-II inhibitors lose efficacy across a panel of Gram-positive pathogens, extending the *E. faecalis* dispensability finding.
4. **Structural hand-off studies.** Use crosslinked acyl-ACP:enzyme complexes to define chain-length-gated recognition at each step and test whether the UFA branch's C10 specificity can be re-engineered.
5. **Regulatory titration.** Recreate graded FadR/FabR induction to map the quantitative relationship between UFA content, membrane fluidity, cell size and fitness across temperatures.

---

## 10. Key References

- Product diversity and regulation of type II fatty acid synthases. [PMID: 15052334](https://pubmed.ncbi.nlm.nih.gov/15052334/)
- The Molecular Genetics of Mycolic Acid Biosynthesis. [PMID: 26104214](https://pubmed.ncbi.nlm.nih.gov/26104214/)
- Fatty acid biosynthesis in actinomycetes. [PMID: 21204864](https://pubmed.ncbi.nlm.nih.gov/21204864/)
- The acyl carrier proteins of lipid synthesis are busy having other affairs. [PMID: 37345808](https://pubmed.ncbi.nlm.nih.gov/37345808/)
- Inhibitors of FabI, an enzyme drug target in the bacterial fatty acid biosynthesis pathway. [PMID: 18193820](https://pubmed.ncbi.nlm.nih.gov/18193820/)
- The reductase steps of the type II fatty acid synthase as antimicrobial targets. [PMID: 15726819](https://pubmed.ncbi.nlm.nih.gov/15726819/)
- Triclosan resistance of *Pseudomonas aeruginosa* PAO1 is due to FabV. [PMID: 19933806](https://pubmed.ncbi.nlm.nih.gov/19933806/)
- Unsaturated fatty acid synthesis in *Enterococcus faecalis* requires a specific enoyl-ACP reductase. [PMID: 36100979](https://pubmed.ncbi.nlm.nih.gov/36100979/)
- The FabA-FabB Pathway Is Not Essential for UFA Synthesis but Modulates DSF Synthesis (*Xanthomonas*). [PMID: 36515967](https://pubmed.ncbi.nlm.nih.gov/36515967/)
- Type II Fatty Acid Synthesis Pathway and Cyclopropane Ring Formation Are Dispensable during *Enterococcus faecalis* Systemic Infection. [PMID: 34309397](https://pubmed.ncbi.nlm.nih.gov/34309397/)
- Elucidating the impact of bacterial lipases, human serum albumin, and FASII inhibition on exogenous fatty-acid utilization. [PMID: 38014966](https://pubmed.ncbi.nlm.nih.gov/38014966/)
- Discovery of bacterial FAS-II inhibitors using a cellular bioluminescent reporter assay (AccC). [PMID: 26169404](https://pubmed.ncbi.nlm.nih.gov/26169404/)
- Crystal structure of the *M. tuberculosis* β-ketoacyl-ACP synthase III (FabH). [PMID: 11278743](https://pubmed.ncbi.nlm.nih.gov/11278743/)
- FabH — Promising Novel Antibacterial Target and Its Inhibitors. [PMID: 42446656](https://pubmed.ncbi.nlm.nih.gov/42446656/)
- The low ENR activity of FabI2 drives high UFA composition in *Sinorhizobium meliloti*. [PMID: 39627703](https://pubmed.ncbi.nlm.nih.gov/39627703/)
- The *E. coli* FadR transcription factor: Too much of a good thing? [PMID: 33283913](https://pubmed.ncbi.nlm.nih.gov/33283913/)
- Transcription factors FabR and FadR regulate cold adaptability of *Shewanella baltica*. [PMID: 32535524](https://pubmed.ncbi.nlm.nih.gov/32535524/)
- Mitochondrial fatty acid synthesis and respiration. [PMID: 20226757](https://pubmed.ncbi.nlm.nih.gov/20226757/)
- Mitochondrial fatty acid synthesis — an adopted set of enzymes. [PMID: 19686777](https://pubmed.ncbi.nlm.nih.gov/19686777/)
- Correlations between FAS elongation-cycle gene expression and fatty-acid production in *E. coli*. [PMID: 23322253](https://pubmed.ncbi.nlm.nih.gov/23322253/)
- Structural study of *E. faecalis* ACP and its interaction with FAS enzymes. [PMID: 36410271](https://pubmed.ncbi.nlm.nih.gov/36410271/)
- Expression of a recombinant, 4′-phosphopantetheinylated, active *M. tuberculosis* FAS I in *E. coli*. [PMID: 30248156](https://pubmed.ncbi.nlm.nih.gov/30248156/)
- Alteration of membrane fluidity/phospholipid composition perturbs MreB rotation. [PMID: 33330621](https://pubmed.ncbi.nlm.nih.gov/33330621/)
- Structural/dynamic characterization of a freestanding ACP (friulimicin biosynthesis). [PMID: 28187530](https://pubmed.ncbi.nlm.nih.gov/28187530/)
- Solution structure of a doublet ACP from prodigiosin biosynthesis. [PMID: 33416314](https://pubmed.ncbi.nlm.nih.gov/33416314/)
- Conformational flexibility of CoA and its impact on 4′-PP transfer to ACP. [PMID: 32128972](https://pubmed.ncbi.nlm.nih.gov/32128972/)

---

*Prepared as a commissioned review synthesis on Type-II fatty-acid synthesis. Evidence base: 29 papers; 5 confirmed findings. The chemistry and step-order of FAS-II are strongly conserved; the enzyme families and cofactors filling each catalytic slot, and the pathway's physiological essentiality, are lineage- and niche-dependent.*


## Artifacts

- [OpenScientist final report](type_ii_fatty_acid_synthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](type_ii_fatty_acid_synthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15052334
2. PMID:26104214
3. PMID:19933806
4. PMID:18193820
5. PMID:36100979
6. PMID:34309397
7. PMID:38014966
8. PMID:30248156
9. PMID:11278743
10. PMID:20226757
11. PMID:19686777
12. PMID:37345808
13. PMID:28187530
14. PMID:33283913
15. PMID:23322253
16. PMID:36515967
17. PMID:32535524
18. PMID:33416314
19. PMID:32128972
20. PMID:42446656
21. PMID:15726819
22. PMID:39627703
23. PMID:21204864
24. PMID:26169404
25. PMID:36410271
26. PMID:33330621