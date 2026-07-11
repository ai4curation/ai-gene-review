---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:08:36.031320'
end_time: '2026-07-11T14:19:19.012665'
duration_seconds: 642.98
template_file: templates/module_research.md.j2
template_variables:
  module_title: L-carnitine dehydrogenation
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00117 module for the NAD(+)-dependent
    oxidation of L-carnitine to 3-dehydrocarnitine. The local UniPathway bucket contains
    lcdH/PP_0302/Q88R32, a reviewed UniProtKB L-carnitine dehydrogenase entry with
    EC 1.1.1.108 and Rhea:RHEA:19265. This seed treats UPA00117 as the dehydrogenase
    step in carnitine catabolism rather than the full downstream utilization route
    for the 3-dehydrocarnitine product.
  module_outline: "- L-carnitine dehydrogenation\n  - 1. NAD(+)-dependent L-carnitine\
    \ oxidation\n  - LcdH L-carnitine dehydrogenation\n    - lcdH: L-carnitine dehydrogenase\
    \ (molecular player: PSEPK lcdH; activity or role: carnitine 3-dehydrogenase activity)"
  module_connections: No explicit connections.
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: l_carnitine_dehydrogenation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: l_carnitine_dehydrogenation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

L-carnitine dehydrogenation

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00117 module for the NAD(+)-dependent oxidation of L-carnitine to 3-dehydrocarnitine. The local UniPathway bucket contains lcdH/PP_0302/Q88R32, a reviewed UniProtKB L-carnitine dehydrogenase entry with EC 1.1.1.108 and Rhea:RHEA:19265. This seed treats UPA00117 as the dehydrogenase step in carnitine catabolism rather than the full downstream utilization route for the 3-dehydrocarnitine product.

## Provisional Biological Outline

- L-carnitine dehydrogenation
  - 1. NAD(+)-dependent L-carnitine oxidation
  - LcdH L-carnitine dehydrogenation
    - lcdH: L-carnitine dehydrogenase (molecular player: PSEPK lcdH; activity or role: carnitine 3-dehydrogenase activity)

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

# L-Carnitine Dehydrogenation: A Review of the NAD⁺-Dependent Oxidation Module (UniPathway UPA00117)

*A commissioned review-style synthesis centred on the *Pseudomonas putida* KT2440 LcdH/PP_0302/Q88R32 L-carnitine dehydrogenase (EC 1.1.1.108; Rhea:RHEA:19265)*

---

## 1. Executive Summary

L-Carnitine dehydrogenation, as captured by the UniPathway module **UPA00117**, is a single, chemically committed enzymatic step: the **NAD⁺-dependent, stereospecific oxidation of the C3 secondary hydroxyl of L-carnitine to the ketone 3-dehydrocarnitine**. In *Pseudomonas putida* the reaction is carried out by **LcdH (locus PP_0302, UniProt Q88R32)**, a soluble cytosolic **L-carnitine dehydrogenase** classified as EC 1.1.1.108 and mapped to Rhea:RHEA:19265. The enzyme is a member of the classic NAD(H)-dependent oxidoreductase repertoire — it uses no metal centre and no flavin, extracting a hydride from C3 and transferring it to NAD⁺. The biochemically characterised orthologue from *P. putida* IFP 206 is a **62 kDa homodimer**, strictly specific for L-carnitine and NAD⁺, with an alkaline pH optimum for oxidation and a near-neutral optimum for the reverse (reductive) reaction ([PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/)).

The single most important framing point for a non-specialist reader is that **carnitine catabolism in bacteria is served by at least three mechanistically unrelated strategies, and UPA00117 is only one of them.** The dehydrogenase route (this review's subject) oxidises carnitine to 3-dehydrocarnitine and keeps the carbon skeleton intact. It must be sharply distinguished from (i) the **O₂-dependent Rieske-type carnitine monooxygenase CntAB/YeaWX**, which cleaves the C–N bond to release **trimethylamine (TMA)** plus malic semialdehyde and has nothing to do with 3-dehydrocarnitine ([PMID: 24591617](https://pubmed.ncbi.nlm.nih.gov/24591617/); [PMID: 33158989](https://pubmed.ncbi.nlm.nih.gov/33158989/)), and (ii) the **anaerobic caiTABCDE reductase system**, in which carnitine acts as an electron acceptor and is reduced via crotonobetaine to γ-butyrobetaine ([PMID: 7815937](https://pubmed.ncbi.nlm.nih.gov/7815937/)). Layered on top of these catabolic fates is carnitine's entirely separate, **non-catabolic role as a compatible solute / osmoprotectant** ([PMID: 25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/)). Confusing these systems is the most common error in the primary and annotation literature, and the boundary is the central analytical contribution of this review.

Finally, the KT2440 LcdH is annotated **chiefly by orthology** to biochemically characterised enzymes from *P. putida* IFP 206 and *Agrobacterium* sp., rather than by direct enzymology of the KT2440 protein itself. The reaction chemistry, cofactor requirement, stereospecificity, and reversibility of the *family* are firmly established; the specific kinetics, structure, and physiological regulation of the KT2440 enzyme, together with the enzymatic fate of the labile 3-dehydrocarnitine product, remain the principal open questions.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

UPA00117 is defined by exactly one biochemical transformation:

```
   L-carnitine  +  NAD⁺   ⇌   3-dehydrocarnitine  +  NADH  +  H⁺
                (EC 1.1.1.108; Rhea:RHEA:19265; carnitine 3-dehydrogenase activity)
```

The system boundary therefore comprises:

- **The substrate:** L-carnitine (the physiologically dominant stereoisomer; a quaternary ammonium compound bearing a C3 hydroxyl and a carboxylate).
- **The catalyst:** LcdH, a soluble NAD⁺-dependent L-carnitine dehydrogenase.
- **The cofactor:** free NAD⁺/NADH (no bound flavin, no metal).
- **The immediate product:** 3-dehydrocarnitine (a β-keto quaternary ammonium acid, chemically labile at neutral pH).

This is a **committed, aerobic-compatible entry point** into carnitine catabolism. It converts the inert secondary alcohol into a reactive ketone that primes the molecule for subsequent (largely uncharacterised in KT2440) decarboxylation/thiolytic breakdown.

### 2.2 What is explicitly excluded — and routinely confused

| Neighbouring system | Chemistry | Key catalyst | Why it is *not* UPA00117 |
|---|---|---|---|
| **Rieske carnitine monooxygenase** | O₂-dependent oxidative **C–N cleavage** → trimethylamine + malic semialdehyde | CntAB (Acinetobacter/human microbiota), YeaWX (E. coli) | Produces TMA, not 3-dehydrocarnitine; uses O₂ + Fe/[2Fe-2S] centres, not NAD⁺; non-homologous to LcdH ([PMID: 24591617](https://pubmed.ncbi.nlm.nih.gov/24591617/); [PMID: 33158989](https://pubmed.ncbi.nlm.nih.gov/33158989/); [PMID: 36066069](https://pubmed.ncbi.nlm.nih.gov/36066069/)) |
| **Anaerobic cai reductase pathway** | Carnitine used as **electron acceptor**, reduced via crotonobetaine to γ-butyrobetaine | caiTABCDE operon | Reductive, not oxidative; anaerobic; no NAD⁺-linked 3-dehydrocarnitine ([PMID: 7815937](https://pubmed.ncbi.nlm.nih.gov/7815937/)) |
| **Compatible-solute uptake / osmoprotection** | No catabolism; carnitine accumulated intact | BCCT-family transporters (CaiT, others), OpuC ABC importer | Non-metabolic; protective role, not a pathway step ([PMID: 25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/); [PMID: 20923416](https://pubmed.ncbi.nlm.nih.gov/20923416/)) |
| **Downstream glycine-betaine hub** | Convergent catabolic node feeding demethylation to sarcosine | GB catabolism genes | Downstream of, and shared by, multiple routes; not the dehydrogenase step itself ([PMID: 17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/)) |

### 2.3 Competing definitions in the literature

Two definitional tensions recur. First, the **"carnitine dehydrogenase" name is shared** by enzymes with different stereospecificity and quaternary structure: an L(−)-carnitine dehydrogenase (EC 1.1.1.108, the UPA00117 enzyme) and a distinct **D(+)-carnitine dehydrogenase** found in *Agrobacterium* ([PMID: 9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/)). Second, some annotation resources treat "carnitine catabolism" as a single UniPathway umbrella, whereas the biochemistry demands that the oxidative dehydrogenase, the oxygenolytic TMA route, and the reductive anaerobic route be treated as **separate, non-homologous modules**. This review adopts the narrow, mechanistically coherent definition: UPA00117 = the NAD⁺-dependent L-carnitine 3-dehydrogenase step, and nothing else.

---

## 3. Mechanistic Overview

### 3.1 The core reaction

LcdH catalyses a textbook **NAD⁺-dependent alcohol→ketone oxidation**. The C3 secondary hydroxyl of L-carnitine is oxidised to a carbonyl; a hydride is transferred to NAD⁺, generating NADH and the β-keto product 3-dehydrocarnitine. Because there is no flavin or metal, the enzyme belongs mechanistically to the large family of soluble pyridine-nucleotide-linked dehydrogenases rather than to the oxygenases or the flavin-dependent oxidases.

```
   L-carnitine (C3-OH)                     3-dehydrocarnitine (C3=O)
        |                                          |
        |   hydride (H⁻) from C3                    |
        v                                          v
   [ LcdH active site ] ---- NAD⁺ ----> NADH  +  H⁺
                     (no metal, no flavin cofactor)
```

### 3.2 Reversibility and directionality

The reaction is **readily reversible**. Purified enzymes show a clear split in pH optima — alkaline (pH ~9.0–9.5) favours oxidation, while near-neutral to mildly acidic conditions favour the reductive back-reaction ([PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/); [PMID: 8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/)). The reverse direction is thermodynamically favourable enough to have been **exploited industrially**: coupling L-carnitine dehydrogenase run in reverse with an NADH-regenerating enzyme (e.g. glucose dehydrogenase) enables stereospecific synthesis of L-carnitine ([PMID: 16232482](https://pubmed.ncbi.nlm.nih.gov/16232482/)). For the *Agrobacterium* D(+)-enzyme the equilibrium constant was measured at **Keq = 2.2 × 10⁻¹²**, quantitatively explaining why the reductive direction dominates under near-physiological conditions ([PMID: 9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/)).

### 3.3 Product instability — a defining constraint

The product 3-dehydrocarnitine is a β-keto acid analogue that is **chemically unstable at neutral pH** and must be held under acidic conditions to be recovered intact ([PMID: 16232482](https://pubmed.ncbi.nlm.nih.gov/16232482/)). This has two consequences for how the pathway must work in vivo: (i) the dehydrogenase step is effectively **metabolically channelled** — the product is expected to be consumed rapidly by the next enzyme (a decarboxylase/thiolase) rather than accumulating; and (ii) in vitro assays of the forward reaction typically require product stabilisation or coupling. Product lability is thus not a nuisance but a mechanistic feature that shapes pathway architecture.

### 3.4 Obligatory vs. accessory steps

Within UPA00117 there is only the single obligatory catalytic step. However, the **module is gated upstream by transport**: carnitine must first enter the cytoplasm through BCCT-family or ABC-type importers before LcdH can act ([PMID: 25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/); [PMID: 20923416](https://pubmed.ncbi.nlm.nih.gov/20923416/)). Downstream steps (breakdown of 3-dehydrocarnitine, funnelling toward glycine betaine/central metabolism) are conditional and largely uncharacterised in KT2440. Thus: **transport (accessory/gating) → LcdH oxidation (obligatory core) → downstream catabolism (conditional).**

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 LcdH and its orthologues

The best-characterised representatives of the L-carnitine dehydrogenase family are summarised below. These provide the biochemical grounding for the KT2440 annotation.

| Enzyme / source | EC | Native mass / quaternary structure | pI | pH optimum (ox / red) | Temp opt | Specificity | Reference |
|---|---|---|---|---|---|---|---|
| *P. putida* IFP 206 carnitine DH | 1.1.1.108 | **62 kDa homodimer** (2 identical subunits) | 4.7 | 9.0 / 7.0 | 30 °C | strictly L-carnitine + NAD⁺ | [PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/) |
| *Agrobacterium* sp. L(−)-carnitine DH | 1.1.1.108 | **114 kDa homodimer** (2 identical subunits) | 5.2–5.4 | 9.5 / 5.5–6.5 | 45 °C | strictly L-carnitine + NAD⁺; competitively inhibited by D-carnitine & TMA | [PMID: 8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/) |
| *Agrobacterium* sp. D(+)-carnitine DH | — | **~88 kDa trimer** (3 × 28 kDa subunits) | — | — | — | D-carnitine; Keq = 2.2 × 10⁻¹² | [PMID: 9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/) |
| *P. putida* KT2440 **LcdH / PP_0302 / Q88R32** | 1.1.1.108 | *inferred by orthology* | — | — | — | *predicted* L-carnitine + NAD⁺ | UniProtKB (reviewed) |

Two points stand out. First, the family shows **conserved chemistry but variable quaternary structure** — dimers of different subunit sizes for the L-enzymes, and a trimer for the D-enzyme — indicating that oligomeric state is not tightly constrained by the catalytic mechanism. Second, the L-enzymes are **strictly stereospecific and strictly NAD⁺-dependent**, with D-carnitine and trimethylamine acting as competitive inhibitors of the *Agrobacterium* L-enzyme ([PMID: 8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/)) — a clean demonstration that the active site reads both the carnitine backbone and the quaternary ammonium head group.

### 4.2 Cofactor

Free **NAD⁺/NADH** is the sole cofactor. The absence of a metal or flavin distinguishes LcdH from every enzyme in the competing carnitine routes and places it firmly in the soluble pyridine-nucleotide dehydrogenase class.

### 4.3 Transporters (gating layer)

Carnitine entry is mediated by **BCCT-family** carriers and **ABC-type (OpuC)** importers. Notably, **CaiT** is a BCCT-family L-carnitine/γ-butyrobetaine antiporter with solved inward-open structures that is *not* osmoregulatory ([PMID: 20923416](https://pubmed.ncbi.nlm.nih.gov/20923416/)), whereas OpuC systems (e.g. in *Listeria*, *Cronobacter*) serve compatible-solute uptake ([PMID: 21918371](https://pubmed.ncbi.nlm.nih.gov/21918371/)). The same molecule (carnitine) can therefore be routed either to catabolism or to osmoprotection depending on which transport and enzymatic machinery is engaged.

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Three non-homologous catabolic strategies

The deepest form of variation here is not sequence divergence within one family but the **existence of three unrelated molecular solutions** to catabolising the same substrate ([PMID: 25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/)):

```
                          L-CARNITINE
                               |
        ┌──────────────────────┼───────────────────────┐
        v                      v                        v
 (1) NAD⁺ DEHYDROGENASE   (2) RIESKE MONOOXYGENASE   (3) ANAEROBIC cai
     LcdH (EC 1.1.1.108)      CntAB / YeaWX               caiTABCDE
        |                        |                         |
     3-dehydrocarnitine      trimethylamine (TMA)       crotonobetaine
        |                     + malic semialdehyde          |
        v                        v                       γ-butyrobetaine
   downstream catabolism    (cardiovascular relevance)   (electron acceptor)
        \________________________|________________________/
                                 v
                 glycine betaine hub → sarcosine (shared node)
```

- **Route 1 (this review):** oxidative, NAD⁺-dependent, aerobic-compatible, keeps the carbon skeleton, produces 3-dehydrocarnitine.
- **Route 2:** O₂-dependent two-component Rieske oxygenase; the reductase supplies electrons via FMN and a plant-type [2Fe-2S] cluster to the oxygenase's Rieske [2Fe-2S] and mononuclear [Fe] centre; cleaves C–N to give TMA + malic semialdehyde. This route is medically important because gut-microbial TMA production is linked to atherosclerosis and cardiovascular disease ([PMID: 24591617](https://pubmed.ncbi.nlm.nih.gov/24591617/); [PMID: 33158989](https://pubmed.ncbi.nlm.nih.gov/33158989/); [PMID: 36066069](https://pubmed.ncbi.nlm.nih.gov/36066069/)).
- **Route 3:** anaerobic reductive use of carnitine as an electron acceptor, encoded by the caiTABCDE operon, proceeding through crotonobetaine to γ-butyrobetaine ([PMID: 7815937](https://pubmed.ncbi.nlm.nih.gov/7815937/)).

### 5.2 Convergence downstream

Despite divergent entry chemistry, catabolic routes converge on **glycine betaine**, a shared hub that can serve as sole carbon or nitrogen source and is demethylated to sarcosine in *P. aeruginosa* ([PMID: 17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/)). This convergence means that the *identity of the entry enzyme* (LcdH vs. CntAB vs. cai) is the main axis of lineage- and condition-specific variation, while downstream metabolism is more conserved.

### 5.3 Physiological-state and compartment variation

In bacteria the same carnitine pool is partitioned between **nutrient catabolism and stress protection**. Carnitine is an osmoprotectant that also enhances thermo-, cryo- and barotolerance ([PMID: 25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/)). Whether a given cell dehydrogenates carnitine or hoards it as a compatible solute is therefore a **physiological-state decision** governed by transporter expression and metabolic demand, not a fixed property. Oxygen availability further gates the choice between the oxidative/oxygenolytic routes (aerobic) and the cai reductive route (anaerobic).

---

## 6. Constraints, Dependencies, and Failure Modes

**Ordering constraints.**
1. **Transport precedes oxidation.** LcdH is cytosolic; carnitine must be imported before it can be a substrate ([PMID: 25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/); [PMID: 20923416](https://pubmed.ncbi.nlm.nih.gov/20923416/)).
2. **Oxidation precedes downstream breakdown.** The C3 ketone of 3-dehydrocarnitine is the chemical handle enabling subsequent decarboxylation/cleavage; without it the inert secondary alcohol cannot be processed by the same logic.

**Mutually exclusive / condition-specific events.**
- The **NAD⁺ dehydrogenase route and the Rieske oxygenase route are chemically incompatible outcomes** for a single carnitine molecule: it is either oxidised at C3 (skeleton intact, 3-dehydrocarnitine) *or* cleaved at the C–N bond (TMA released). These are alternative fates, not sequential steps.
- The **anaerobic cai route is oxygen-excluded**, whereas the oxygenase route is strictly O₂-dependent; they are therefore largely mutually exclusive by growth condition.
- **Compatible-solute accumulation vs. catabolism** compete for the same imported carnitine pool.

**Stereochemical constraint.**
- LcdH is strictly **L-specific**; D-carnitine is not a substrate and actually inhibits the *Agrobacterium* L-enzyme competitively, as does trimethylamine ([PMID: 8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/)). A separate D(+)-carnitine dehydrogenase is required to handle the D-isomer ([PMID: 9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/)).

**Failure modes.**
- **Product accumulation:** because 3-dehydrocarnitine is unstable at neutral pH ([PMID: 16232482](https://pubmed.ncbi.nlm.nih.gov/16232482/)), any bottleneck in the downstream enzyme would lead to non-productive decomposition of the intermediate — a strong argument that the step is kinetically coupled/channelled in vivo.
- **Cofactor imbalance:** as an NAD⁺-linked reaction, flux depends on the cellular NAD⁺/NADH ratio; the near-neutral reductive optimum means the reaction can run backwards under reducing conditions, which is exactly what is exploited biotechnologically ([PMID: 16232482](https://pubmed.ncbi.nlm.nih.gov/16232482/); [PMID: 9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/)).

**Evidence that rules out alternative paths.**
- The **product identity** (3-dehydrocarnitine, not TMA) rules out that UPA00117 is an oxygenolytic step ([PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/)).
- The **cofactor** (NAD⁺, no metal/flavin) rules out a Rieske-type mechanism.
- The **oxidative directionality and aerobic compatibility** distinguish it from the reductive cai route.

---

## 7. Controversies and Open Questions

1. **The KT2440 enzyme is annotated by orthology, not measured.** The reviewed UniProt entry Q88R32 (PP_0302, LcdH) inherits its EC number and reaction from the well-characterised *P. putida* IFP 206 and *Agrobacterium* enzymes. **No direct kinetic, structural, or knockout data for the KT2440 protein itself** are represented in the evidence base assembled here. Its specific kₐₜ/Kₘ, oligomeric state, and in-vivo essentiality for growth on carnitine remain to be demonstrated experimentally. This is the single largest caveat on the module.

2. **The downstream fate of 3-dehydrocarnitine in KT2440 is unresolved.** The classic model invokes a decarboxylation/thiolytic cleavage that ultimately connects to the glycine betaine hub, but the specific KT2440 enzyme(s) and gene(s) that consume the labile β-keto product are not established here.

3. **Structural biology gap.** There are solved structures for the *competing* carnitine monooxygenase CntA ([PMID: 33158989](https://pubmed.ncbi.nlm.nih.gov/33158989/)) and for the CaiT transporter ([PMID: 20923416](https://pubmed.ncbi.nlm.nih.gov/20923416/)), but no experimental structure of an L-carnitine dehydrogenase is represented in this dataset. The structural basis of L-stereospecificity and quaternary-ammonium recognition is therefore inferred, not seen.

4. **Cross-organism mixing.** Much of the mechanistic understanding pools data from *P. putida*, *Agrobacterium*, *E. coli*, and human-gut *Acinetobacter*/*Escherichia*. Because these organisms deploy **non-homologous** enzymes, care is needed not to transfer, for example, the medically prominent TMA-producing oxygenase biology onto the NAD⁺ dehydrogenase module. The literature frequently blurs this line.

5. **Quaternary-structure variability.** Why L-carnitine dehydrogenases occur as 62 kDa vs. 114 kDa dimers, and the D-enzyme as an ~88 kDa trimer ([PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/); [PMID: 8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/); [PMID: 9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/)), and whether this affects regulation or stability, is unexplained.

---

## 8. Mechanistic Model / Synthesis

Putting the pieces together, UPA00117 in *P. putida* KT2440 is best modelled as a **single committed valve** on the front end of aerobic carnitine catabolism:

```
 ENVIRONMENT                 MEMBRANE                        CYTOPLASM
 -----------                 --------                        ---------
 L-carnitine  --->  BCCT / ABC (OpuC) importer  --->  L-carnitine
                    (gating; also osmoprotection)             |
                                                              |  LcdH (EC 1.1.1.108)
                                                    NAD⁺ ----> |  ⇌   NADH + H⁺   (reversible;
                                                              |        alkaline favours ox.)
                                                              v
                                                     3-dehydrocarnitine
                                                     (labile β-keto acid;
                                                      unstable at neutral pH)
                                                              |
                                                              v  (downstream, uncharacterised in KT2440)
                                                     ...  →  glycine betaine hub  →  central metabolism
```

The valve is **stereospecific (L only), cofactor-simple (NAD⁺, no metal/flavin), reversible, and product-labile.** Its identity as a *dehydrogenase* — not an oxygenase or a reductase — is what defines the module and separates it from the TMA-producing and anaerobic routes it is habitually confused with. The biology is well understood at the family level and under-characterised at the specific-protein (KT2440) level.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | Contribution to this review |
|---|---|---|
| [3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/) | Carnitine dehydrogenase from *P. putida* | Defines EC 1.1.1.108, NAD⁺ cofactor, 62 kDa homodimer, strict L-specificity, pH/temp optima — the biochemical anchor for the UPA00117 step |
| [16232482](https://pubmed.ncbi.nlm.nih.gov/16232482/) | L-carnitine production with NADH regeneration | Establishes reversibility and the chemical instability of 3-dehydrocarnitine at neutral pH |
| [8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/) | L(−)-carnitine DH from *Agrobacterium* | 114 kDa homodimer; strict L/NAD⁺ specificity; competitive inhibition by D-carnitine and TMA |
| [9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/) | D(+)-carnitine DH from *Agrobacterium* | Distinct stereospecificity and quaternary structure (trimer); Keq = 2.2 × 10⁻¹² quantifies favourable reduction |
| [24591617](https://pubmed.ncbi.nlm.nih.gov/24591617/) | Rieske carnitine monooxygenase (CntAB) | Documents the O₂-dependent TMA-producing route — the pathway most confused with dehydrogenation |
| [33158989](https://pubmed.ncbi.nlm.nih.gov/33158989/) | CntA structure & specificity | Structural basis of the oxygenase route; contrasts with metal/flavin-free LcdH |
| [36066069](https://pubmed.ncbi.nlm.nih.gov/36066069/) | Two-component carnitine monooxygenase (E. coli YeaWX) | Cofactor architecture (FMN, [2Fe-2S], Rieske, mononuclear Fe) of the competing route |
| [7815937](https://pubmed.ncbi.nlm.nih.gov/7815937/) | cai operon in *E. coli* | Documents the anaerobic reductive route (carnitine as electron acceptor) |
| [17951379](https://pubmed.ncbi.nlm.nih.gov/17951379/) | Glycine betaine catabolism in *P. aeruginosa* | Shows the downstream convergence hub of carnitine catabolism |
| [25787873](https://pubmed.ncbi.nlm.nih.gov/25787873/) | Carnitine in bacterial physiology (review) | Frames the dual fate (nutrient vs. compatible solute) and the multiplicity of catabolic pathways |
| [20923416](https://pubmed.ncbi.nlm.nih.gov/20923416/) | BCCT carrier family | Identifies CaiT as a non-osmoregulatory L-carnitine antiporter (transport/gating layer) |
| [21918371](https://pubmed.ncbi.nlm.nih.gov/21918371/) | Osmotolerance in *Cronobacter* | Documents OpuC multi-component carnitine uptake in the compatible-solute role |
| [28506279](https://pubmed.ncbi.nlm.nih.gov/28506279/) | TMA producers of the human gut | Context for the medically prominent, non-homologous oxygenase route (cntA) |

**How the evidence coheres.** Findings F001–F004 are mutually reinforcing: F001 fixes the enzyme's identity and chemistry; F002 draws the sharp boundary against the two non-homologous catabolic routes and the shared downstream hub; F003 establishes stereospecificity, reversibility, and structural diversity across the family; and F004 supplies the transport-gating and osmoprotection context that bounds the module upstream. No finding in the assembled evidence contradicts the narrow definition of UPA00117 adopted here.

---

## 10. Limitations and Knowledge Gaps

- **Orthology-only annotation of KT2440 LcdH.** All quantitative enzymology in this review derives from *P. putida* IFP 206 and *Agrobacterium* proteins, not from PP_0302/Q88R32 directly.
- **No downstream pathway resolution.** The enzyme(s) consuming 3-dehydrocarnitine in KT2440 are not identified in this dataset; the connection to the glycine-betaine hub is inferential.
- **No experimental structure** of any L-carnitine dehydrogenase in the evidence base; stereochemical and substrate-recognition mechanisms are inferred.
- **Cross-organism heterogeneity.** Mechanistic claims necessarily pool data across bacteria with non-homologous enzymes; over-transfer between the dehydrogenase and oxygenase routes is a real risk.
- **Regulation unknown.** How KT2440 decides between carnitine catabolism and osmoprotective retention, and how lcdH expression is controlled, is not addressed by the available evidence.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Direct biochemistry of KT2440 LcdH.** Heterologously express PP_0302/Q88R32, purify, and measure kₐₜ/Kₘ for L-carnitine and NAD⁺, pH/temperature optima, and oligomeric state — confirming (or revising) the orthology-based annotation.
2. **Genetic essentiality.** Construct a KT2440 *lcdH* deletion and test growth on L-carnitine as sole carbon/nitrogen source, aerobically and anaerobically, to establish the enzyme's in-vivo role and rule in/out redundancy with other routes.
3. **Trace the downstream fate of 3-dehydrocarnitine.** Use ¹³C-labelled L-carnitine plus targeted metabolomics (under product-stabilising acidic quenching) to identify the next intermediate(s) and the responsible enzyme(s), connecting the module to central metabolism.
4. **Structure determination.** Solve an experimental structure (X-ray or cryo-EM) of an L-carnitine dehydrogenase — ideally the KT2440 enzyme — to define the L-stereospecific, quaternary-ammonium-reading active site and rationalise the D-carnitine/TMA competitive inhibition.
5. **Discriminate routes in situ.** In organisms carrying more than one carnitine strategy, use condition-controlled (aerobic vs. anaerobic; osmotic stress vs. nutrient limitation) transcriptomics/proteomics to map when the dehydrogenase, oxygenase, cai, and compatible-solute systems are each deployed.
6. **Cofactor-engineering / biocatalysis.** Given the demonstrated reversibility and favourable reduction equilibrium, benchmark the KT2440 enzyme for reductive stereospecific L-carnitine synthesis with NADH regeneration, comparing to established *Agrobacterium*/*Pseudomonas* systems.

---

*Prepared as a commissioned review synthesis. All quantitative and mechanistic claims are anchored to the cited primary literature; uncertainty — especially the orthology-based nature of the KT2440 annotation and the unresolved downstream chemistry — is flagged explicitly throughout.*


## Artifacts

- [OpenScientist final report](l_carnitine_dehydrogenation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](l_carnitine_dehydrogenation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:3058208
2. PMID:24591617
3. PMID:33158989
4. PMID:7815937
5. PMID:25787873
6. PMID:36066069
7. PMID:20923416
8. PMID:17951379
9. PMID:9003445
10. PMID:8645721
11. PMID:16232482
12. PMID:21918371