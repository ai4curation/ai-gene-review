---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:15:20.150512'
end_time: '2026-07-11T16:27:02.407924'
duration_seconds: 702.26
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: methionine_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: methionine_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
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

# L-Methionine Biosynthesis from L-Homoserine: An Ordered, OR-Satisfiable Module with an Ancient Core and Sequence-Opaque Route Choices

*A review-style synthesis for a molecular-biology audience. Search date: 2026-07-11. Sources: PubMed primary literature and authoritative reviews.*

---

## 1. Executive Summary

De novo biosynthesis of L-methionine from L-homoserine is one of the clearest natural examples of a **modular, "OR-of-enzymes" metabolic pathway**: a strictly ordered sequence of three chemical transformations in which every step can be catalyzed by one of two (or more) non-orthologous enzyme families. An organism is a methionine prototroph if and only if it satisfies the Boolean expression:

> **[MetA OR MetX] AND [(MetB AND MetC) OR MetY] AND [MetE OR MetH]**

The three steps are (1) **acylation** of the homoserine γ-hydroxyl — either O-succinylation by MetA or O-acetylation by MetX; (2) **sulfur incorporation** to give L-homocysteine — either the two-enzyme trans-sulfuration branch (cystathionine γ-synthase MetB plus cystathionine β-lyase MetC, drawing sulfur from cysteine) or the one-step direct sulfhydrylation branch (O-acyl-homoserine sulfhydrylase MetY/MetZ, using free sulfide); and (3) **methylation** of homocysteine to methionine — either the cobalamin-independent synthase MetE or the cobalamin-dependent synthase MetH. Because every step has alternatives, **no single enzyme is universally required**; the order is enforced by substrate chemistry, not by any indispensable protein.

This investigation confirmed six load-bearing findings. First, the two sulfur-incorporation branches are **genuinely redundant but not equivalent** — in *Corynebacterium glutamicum* either branch alone confers prototrophy and only the double knockout is auxotrophic, yet the two enzymes differ in kinetics and regulation [PMID 11844756; 18050920]. Second, the two methionine synthases (MetE, MetH) are **non-homologous convergent solutions** to the same chemical step, and differential loss of MetE is the molecular basis of vitamin-B12 auxotrophy in algae [PMID 15630480; 21551270]. Third, **bifunctional enzymes and mis-annotation blur the "one gene = one step" model** [PMID 15576367; 11832514]. Fourth, pathway output is **gated by SAM-sensing regulators** (S-box/SAM-I riboswitches, MetJ) [PMID 18039762]. Fifth, **route identity often cannot be read from sequence** — a single active-site residue flips acetyl-vs-succinyl donor specificity [PMID 18216013]. Sixth, methionine and its downstream cofactor S-adenosylmethionine (SAM) trace to a **LUCA-era origin** [PMID 39665745].

The central practical message for GapMind-style, per-genome pathway reconstruction is a productive tension: the pathway's **template is stable and biologically real**, but the **oracle that must decide which candidate enzyme is present at each step is unreliable when it relies on sequence homology alone**. Bifunctionality, single-residue specificity switches, and independent gene losses mean that annotation transfer frequently mis-assigns route identity. The module is easy to *define* and hard to *call*.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The system begins with **L-homoserine** — the committed branch-point metabolite of the aspartate family (aspartate → aspartyl-phosphate → aspartate semialdehyde → homoserine, shared with threonine and isoleucine synthesis) — and ends with **L-methionine**. It comprises exactly three enzymatic steps and their alternative routes:

| Step | Transformation | Route A | Route B |
|------|----------------|---------|---------|
| 1. Acylation | Homoserine → O-acyl-homoserine | O-succinyltransferase **MetA** (succinyl-CoA) | O-acetyltransferase **MetX** (acetyl-CoA) |
| 2. Sulfur incorporation | O-acyl-homoserine → homocysteine | Trans-sulfuration: **MetB** (γ-synthase) + **MetC** (β-lyase), sulfur from cysteine via cystathionine | Direct sulfhydrylation: **MetY/MetZ**, sulfur from free sulfide (HS⁻) |
| 3. Methylation | Homocysteine → methionine | Cobalamin-independent **MetE** (CH₃-H₄folate donor) | Cobalamin-dependent **MetH** (methylcobalamin intermediate) |

### 2.2 Neighboring processes often conflated but that should be treated separately

- **The methionine / SAM cycle (salvage).** MetE/MetH is shared between de novo biosynthesis and the methionine cycle, but in the cycle homocysteine comes from S-adenosylhomocysteine, not from homoserine + sulfur. The enzyme is the same; the pathway context differs.
- **Cysteine biosynthesis / sulfate assimilation.** Trans-sulfuration draws sulfur from cysteine and direct sulfhydrylation from free sulfide; the sulfate-reduction machinery that makes these donors is upstream and distinct, though it gates substrate availability.
- **Reverse trans-sulfuration (methionine → cysteine).** The cystathionine γ-lyase/γ-synthase machinery can run backwards so methionine serves as a sulfur source, as in *M. tuberculosis* [PMID 15576367]. This is catabolic, not biosynthetic.
- **Regulatory apparatus.** The MetJ–SAM co-repressor (enteric bacteria) and the S-box/SAM-I riboswitch (low-G+C Gram-positives) [PMID 18039762; 20951706] control expression but are not pathway steps.

### 2.3 Competing definitions

Two framings recur. First, whether "methionine biosynthesis" includes the **aspartate-to-homoserine** stem — metabolic-engineering papers usually do, while comparative-genomics templates (this brief) start at homoserine. Second, whether **MetY-type direct sulfhydrylation** is an alternative to trans-sulfuration or part of cysteine metabolism, since the same PLP-fold enzymes act on O-acetylserine (cysteine) and O-acetylhomoserine (methionine). These are definitional, not factual, disagreements, but they change which genes an oracle should count.

---

## 3. Mechanistic Overview

The best current model is a **linear three-node dependency graph with parallel edges at each node**, in which each step creates the substrate the next requires:

```
                 [Step 1: acylate]        [Step 2: add sulfur]          [Step 3: methylate]
                  ┌── MetA (succinyl)      ┌── MetB + MetC (cysteine)     ┌── MetE (B12-independent)
 L-homoserine ──▶ │                  ──▶   │  (trans-sulfuration)    ──▶  │                         ──▶ L-methionine
                  └── MetX (acetyl)        └── MetY (free sulfide)        └── MetH (B12-dependent)
                                              (direct sulfhydrylation)
   γ-OH activated as        O-acyl leaving group        thiol (-SH) created on         -SH methylated to
   an acyl leaving group    displaced by S-nucleophile   homocysteine                   give -S-CH3
```

**Step 1 — Acylation (activation).** Homoserine's γ-hydroxyl is a poor leaving group. Acyl transfer from acyl-CoA (succinyl-CoA for MetA, acetyl-CoA for MetX) esterifies it into O-succinyl- or O-acetyl-homoserine, a far better leaving group. This is the committed step and a common feedback-control point. MetA and MetX are non-homologous: MetX has an α/β-hydrolase fold with a catalytic serine [PMID 31889085], MetA belongs to a distinct, conformationally labile transferase family [PMID 31891734]. Critically, the acetyl-vs-succinyl choice is **not cleanly predictable from sequence** [PMID 18216013].

**Step 2 — Sulfur incorporation.** The activated ester is displaced at the γ-carbon by a sulfur nucleophile, catalyzed by **PLP-dependent** enzymes of the Cys/Met-metabolism family. Trans-sulfuration is two steps: MetB performs a γ-replacement joining O-acyl-homoserine to cysteine's thiol to form cystathionine, and MetC performs a β-elimination to release homocysteine + pyruvate + ammonia. Direct sulfhydrylation is one step: MetY/MetZ uses free sulfide, converting O-acetyl-homoserine straight to homocysteine; structurally MetY belongs to the γ-elimination subclass and shares the fold of cystathionine/methionine γ-lyases, with sulfur transfer possibly proceeding via a protein thiocarboxylate intermediate [PMID 21931214].

**Step 3 — Methylation.** The homocysteine thiol is methylated using N5-methyltetrahydrofolate, yielding methionine + tetrahydrofolate. Both synthases use a **zinc ion as a thiolate-activating Lewis acid** [PMID 10625458; 15630480]. MetH uses a bound **methylcobalamin/cob(I)alamin** intermediary in a fast ping-pong mechanism with large inter-modular conformational changes [PMID 12832615; 17924667]. MetE performs the **direct** transfer with no cobalamin — a chemically harder reaction (~50-fold lower turnover) on a double (βα)₈-barrel scaffold [PMID 15630480; 15326182].

**Obligatory vs conditional vs accessory.** No individual *enzyme* is obligatory, but each *step* is obligatory — the chemistry cannot be skipped or reordered. Conditional elements are the route choices (succinyl vs acetyl; trans-sulfuration vs direct; B12-independent vs -dependent). Accessory elements are the MetH reactivation module (reductive re-methylation of oxidized cob(II)alamin using flavodoxin + SAM) [PMID 12832615], the regulatory riboswitches/repressors, and the enzymes supplying cysteine or sulfide.

---

## 4. Major Molecular Players and Active Assemblies

| Step | Enzyme (gene) | Reaction / role | Fold / cofactor | Notes |
|---|---|---|---|---|
| 1. Acylation | **MetA** | homoserine + succinyl-CoA → O-succinyl-homoserine | Distinct transferase family; conformationally labile | Feedback-inhibited by Met/SAM; L-Met engineering target [PMID 31891734; 37312226] |
| 1. Acylation | **MetX** | homoserine + acetyl-CoA → O-acetyl-homoserine | α/β-hydrolase fold, catalytic Ser | Druggable deep active-site tunnel in mycobacteria [PMID 31889085] |
| 2. Trans-sulfuration | **MetB** | O-acyl-homoserine + cysteine → cystathionine | PLP, Cys/Met family | Homotetramer; can be bifunctional CGS/CGL [PMID 18050920; 15576367] |
| 2. Trans-sulfuration | **MetC** | cystathionine → homocysteine + pyruvate + NH₃ | PLP, Cys/Met family | β-lyase of the metIC operon in *B. subtilis* [PMID 11832514] |
| 2. Direct | **MetY/MetZ** | O-acyl-homoserine + HS⁻ → homocysteine | PLP, γ-elimination subclass | Met-inhibited; high sulfide Km (~8.6 mM) [PMID 21931214; 11844756] |
| 3. Methylation | **MetE** | CH₃-H₄folate + Hcy → Met + H₄folate | Zn²⁺, dual (βα)₈ barrel; no B12 | Face-to-face double barrel from gene duplication; Zn ligands His/Cys/Glu/Cys [PMID 15630480; 10625458; 15326182] |
| 3. Methylation | **MetH** | CH₃-H₄folate + Hcy → Met + H₄folate | Zn²⁺ + methylcobalamin | ~136 kDa four-module machine; His-on/His-off coordination; flavodoxin/SAM reactivation [PMID 17924667; 12832615] |

Notable assembly features: (i) MetH is a **single-chain, multi-module machine** whose four domains reposition during catalysis and reactivation — the color of its cobalamin reports its conformation [PMID 12832615]. (ii) The trans-sulfuration and direct routes **share a PLP superfamily**, so a single promiscuous enzyme can occupy both routes (e.g., *B. subtilis* MetI has both cystathionine γ-synthase and O-acetylhomoserine thiolyase activities [PMID 11832514]). (iii) In many Gram-positives the genes are **operonic** (e.g., *metIC*), placing steps under one regulatory element.

---

## 5. Key Findings

### F001 — The two sulfur-incorporation routes are functionally redundant within a single organism, but not equivalent

The most direct demonstration that the pathway is truly OR-satisfiable at step 2 comes from *Corynebacterium glutamicum*, which encodes **both** branches simultaneously. Single deletion of *metB* (trans-sulfuration) or *metY* (direct sulfhydrylation) does **not** cause methionine auxotrophy; only the *metB/metY* double mutant is auxotrophic [PMID 11844756]. This is the genetic signature of logical redundancy: each branch alone is *sufficient*, so neither is individually *necessary*.

Redundancy does not mean interchangeability. Purified MetB and MetY have comparable kinetics toward the shared O-acetylhomoserine substrate (Km 3.9 vs 6.4 mM; kcat 21 vs 28 s⁻¹), but MetY has a **physiologically high Km for sulfide (~8.6 mM)** and is **feedback-inhibited by methionine**, whereas MetB is not [PMID 18050920]. Consequently direct sulfhydrylation is favored only when free sulfide is abundant and demand is low, while trans-sulfuration dominates under sulfur limitation. The two "equivalent" edges of the graph therefore carry different flux under different physiological states — a subtlety invisible to a purely presence/absence oracle.

### F002 — Two non-homologous methionine synthases serve step 3, and MetE loss underlies vitamin-B12 auxotrophy in algae

The final methylation is catalyzed by MetE and MetH, convergent non-homologous zinc enzymes: MetE "displays no detectable sequence homology with cobalamin-dependent methionine synthase (MetH)," yet both require zinc to bind and activate homocysteine [PMID 15630480]. The evolutionary consequence is dramatic in algae: across 15 sequenced algal genomes there is a **strong correlation between absence of a functional METE gene and B12 (cobalamin) auxotrophy** [PMID 21551270]. Because METE expression is repressed by B12, a reliable environmental B12 supply relaxes selection on METE, permitting mutation accumulation and eventual gene loss [PMID 24627342]. The phylogenetically scattered distribution of auxotrophy indicates METE has been **lost independently many times**. This has real ecological consequences: in *Chlamydomonas reinhardtii*, heat stress represses METE, and only algae partnered with B12-producing bacteria (which supply the cofactor for MetH) survive thermal stress — a documented mutualism [PMID 23486253].

### F003 — Bifunctional enzymes and mis-annotation blur the "one gene = one step" model

The clean template hides messy biology. In *M. tuberculosis*, the gene annotated *metB* (Rv1079) actually encodes a **bifunctional cystathionine γ-lyase/γ-synthase** — a γ-elimination reaction with cystathionine as well as the γ-replacement yielding cystathionine — enabling reverse trans-sulfuration so that methionine is the preferred sulfur source for pathogenic mycobacteria [PMID 15576367]. In *B. subtilis*, MetI (a metB-family enzyme) has **both** cystathionine γ-synthase and O-acetylhomoserine thiolyase activities, so a single enzyme participates in *both* step-2 branches, while MetC is the cystathionine β-lyase [PMID 11832514]. And the *W. succinogenes* MetY shares its fold with cystathionine γ-lyase / methionine γ-lyase [PMID 21931214]. The branches of step 2 are therefore not cleanly partitioned by gene family; a single locus can straddle both routes or run the pathway backwards.

### F004 — Sulfur-metabolism gene expression is gated by SAM-sensing regulators

Pathway output is coupled to demand through SAM sensing. In low-G+C Gram-positive bacteria, the **S-box (SAM-I) riboswitch** is the paradigm SAM-sensing regulatory RNA: SAM binds the leader aptamer and drives premature transcription termination, and expression is induced in response to starvation for methionine; the 11 S-box transcriptional units of *B. subtilis* show a wide range of SAM sensitivities [PMID 18039762; structural basis in 20951706]. The *B. subtilis metIC* operon carries an S-box and is induced on sulfate/cysteine but repressed on methionine [PMID 11832514]. In enteric bacteria the analogous role falls to the **MetJ–SAM co-repressor**. In both cases the pathway senses its ultimate product (as SAM) rather than methionine directly, tying biosynthetic flux to the cell's methylation economy.

### F005 — Acyl-donor specificity can flip with a single active-site residue, so sequence alone does not predict route

The *B. cereus* "metA" protein "functions as an HTA [homoserine transacetylase] despite greater than 50% sequence identity with bona fide HTS [transsuccinylase] proteins," and a **single active-site residue** determines specificity — Glu-111 confers acetyl-CoA use, Gly-111 confers succinyl-CoA use — while both enzymes share a common catalytic mechanism [PMID 18216013]. The authors explicitly warn that this "emphasizes the need for functional confirmation of annotations of enzyme function based on either sequence or structural comparisons." For a per-genome oracle, this is the crux: the MetA/MetX distinction — which sets whether the intermediate is O-succinyl- or O-acetyl-homoserine, and hence which downstream sulfhydrylase can act — **cannot be reliably called from homology**.

### F006 — Methionine and SAM trace to a LUCA-era origin

Ancestral reconstruction of LUCA-dating protein domains infers that the sulfur-containing amino acids cysteine and methionine were "added to the genetic code much earlier than previously thought," with methionine added earlier than expected from its molecular weight and compatible with inferred early use of S-adenosylmethionine [PMID 39665745]. This supports the view that the *need* for methionine — and therefore selection for a supply pathway — is extremely deep, even if the specific modern enzymes are comparatively recent.

---

## 6. Mechanistic Model and Interpretation

Synthesizing the six findings yields a coherent **two-layer model**. The lower layer is ancient and conserved: the chemical logic (activate the γ-hydroxyl → insert sulfur via PLP chemistry → methylate the thiol via a zinc-dependent folate/cobalamin reaction) and the demand for methionine/SAM date to near the origin of life (F006). The upper layer is recent and labile: which specific enzyme family is deployed at each node is a patchwork of clade-specific choices, replacements, bifunctional consolidations, and independent losses (F001–F005).

The pathway can be read as a Boolean satisfiability instance:

```
Prototroph  ⇔  (MetA ∨ MetX)  ∧  ((MetB ∧ MetC) ∨ MetY)  ∧  (MetE ∨ MetH)
```

with five real-world caveats that a naive SAT oracle misses:

| Caveat | Evidence | Consequence for reconstruction |
|--------|----------|-------------------------------|
| Route identity ≠ gene family | Glu111/Gly111 flips acetyl/succinyl (F005) | A "MetA hit" may actually be MetX chemistry |
| One gene can satisfy two literals | *B. subtilis* MetI = γ-synthase + thiolyase (F003) | A single locus covers both step-2 branches |
| Genes can run backwards | *M. tuberculosis* Rv1079 reverse trans-sulfuration (F003) | A biosynthetic "hit" may be catabolic |
| Redundant ≠ equivalent | MetY high sulfide Km + Met inhibition (F001) | Presence does not predict physiological flux |
| Loss is adaptive, not degenerative | METE loss → B12 auxotrophy in algae (F002) | Absence is often environment-driven, not error |

The **ordering constraints are hard**: acylation must precede sulfur incorporation because the acyl group is the leaving group displaced by sulfur; sulfur incorporation must precede methylation because the thiol is the methyl acceptor. These are chemistry-enforced and admit no reordering — which is why the template's edges are directional even though the nodes are interchangeable.

---

## 7. Evolutionary and Cell-Biological Variation

- **Enteric bacteria (*E. coli*):** MetA (succinyl) + trans-sulfuration (MetB/MetC) + MetE and MetH; MetJ–SAM repression. The industrial-fermentation reference; MetA feedback inhibition is the key engineering bottleneck [PMID 31891734; 37312226].
- **Corynebacteria / actinobacteria (*C. glutamicum*):** MetX (acetyl) plus **both** MetB/MetC and MetY — parallel, individually dispensable sulfur routes [PMID 11844756].
- **Firmicutes (*B. subtilis*):** acetyl activation; bifunctional MetI covering trans-sulfuration and thiolation, MetC as β-lyase; S-box/SAM-I riboswitch regulation [PMID 11832514; 18039762].
- **Mycobacteria:** MetX activation [PMID 31889085]; a bifunctional CGL/CGS enabling reverse trans-sulfuration [PMID 15576367]; a validated drug target because absent from the human host.
- **Fungi/plants:** predominantly acetyl activation + direct sulfhydrylation and/or trans-sulfuration + MetE; plants use MetE (*Arabidopsis* MetE structure [PMID 15326182]; *Neurospora* MetE [PMID 26657067]), and land plants/fungi are cobalamin-independent.
- **Algae/protists:** highly variable; ~half of microalgal species are B12 auxotrophs, correlating tightly with **loss of a functional METE**, leaving only the B12-dependent METH [PMID 21551270; 24627342].
- **Mammals (boundary case):** run trans-sulfuration in reverse (catabolic) and cannot synthesize methionine de novo — excluded from the biosynthetic template.

**Conservation and origin.** The ancient conserved skeleton is the PLP-dependent γ-substitution/elimination chemistry (the Cys/Met superfamily to which MetB, MetC, and MetY all belong [PMID 21931214]) and folate-dependent methyl transfer with a catalytic zinc [PMID 15630480], together with the fixed step order they impose. The metA-vs-metX, trans-sulfuration-vs-direct, and metE-vs-metH splits are the recent, patchily distributed top layer (e.g., independent METE losses [PMID 21551270]). Within expanded families, the best proxy for the ancestral acyltransferase role is read from the position-111 active-site residue rather than overall identity [PMID 18216013], and bifunctional Cys/Met-family members (*B. subtilis* MetI, *M. tuberculosis* Rv1079) plausibly resemble a promiscuous ancestor from which the dedicated γ-synthase (MetB) and γ-lyase (MetC) specialists were refined.

---

## 8. Constraints, Dependencies, and Failure Modes

**Ordering constraints (hard).** Acylation must precede sulfur incorporation (the sulfur nucleophile displaces the acyl leaving group); sulfur incorporation must precede methylation (homocysteine is the methyl acceptor). These are the two "precedes" relations in the brief, enforced by substrate chemistry.

**Substrate-specific constraints.** Trans-sulfuration requires cysteine (organic sulfur); direct sulfhydrylation requires free sulfide and is only effective when sulfide is abundant (high MetY sulfide Km) [PMID 18050920]. MetH requires cobalamin; in its absence, an organism lacking MetE becomes a **conditional B12 auxotroph** [PMID 21551270].

**Failure modes (ruling out plausible-but-wrong paths).**
- **Annotation ≠ function.** A gene labeled *metB* may be a bifunctional γ-lyase/γ-synthase [PMID 15576367]; a *metB*-family gene (*metI*) may carry the "other" route's thiolase activity [PMID 11832514]; a *metA*-family gene may be a transacetylase despite >50% identity [PMID 18216013]. Label-keyed oracles will mis-satisfy or falsely fail steps.
- **Enzyme lability.** MetA is thermolabile and product-inhibited; activity can bottleneck flux even when the gene is present [PMID 31891734].
- **Cofactor dependence as an environmental failure mode.** A MetH-only genome "passes" methylation in silico but fails to grow without B12 — satisfiability at the gene level is necessary but not sufficient for realized prototrophy [PMID 23486253].

---

## 9. Controversies and Open Questions

1. **How predictable is route usage from sequence alone?** Recurrent bifunctionality and mis-annotation of PLP enzymes [PMID 15576367; 11832514] give automated reconstruction a real, quantifiable error rate at the sulfur step. How best to encode "one protein, two routes" in a satisfiability model is unresolved.
2. **Sulfur source of direct sulfhydrylation in vivo.** Structural work proposes a **protein thiocarboxylate** intermediate rather than bulk free sulfide [PMID 21931214], which would change how "sulfide availability" gates the route. Only partially resolved.
3. **Why keep two synthases?** The drivers of repeated independent METE loss across algae are debated; the leading hypothesis is that chronic B12 availability relaxes selection on METE, permitting decay and loss [PMID 21551270; 24627342], but ecological triggers are incompletely mapped.
4. **Best representative for the ancestral role.** Within the Cys/Met PLP superfamily, which extant enzyme best proxies the ancestor is unsettled; shared γ-family folds [PMID 21931214] suggest deep common ancestry with later specialization.
5. **Cross-organism extrapolation.** Much mechanistic detail (especially MetH conformational dynamics) comes from *E. coli* [PMID 12832615; 17924667]; how faithfully these generalize to distant lineages and to the eukaryotic compartmentalized context is an open caveat.

**Strongly supported:** the fixed step order; zinc catalysis in both synthases; MetH's cobalamin-shuttling mechanism; MetE/MetH and MetA/MetX non-homology; genetic redundancy of the two sulfur routes; the METE-loss ↔ B12-auxotrophy correlation. **Weaker/indirect:** the in vivo sulfur donor for MetY; the universality of *E. coli*-derived mechanistic models; the evolutionary drivers of route retention.

---

## 10. Evidence Base

| Finding | Key papers | How they support / challenge the claim |
|---------|-----------|-----------------------------------------|
| F001 route redundancy | [PMID 11844756](https://pubmed.ncbi.nlm.nih.gov/11844756/); [PMID 18050920](https://pubmed.ncbi.nlm.nih.gov/18050920/) | Double-knockout genetics prove OR-sufficiency; kinetics show non-equivalence |
| F002 two synthases / B12 auxotrophy | [PMID 15630480](https://pubmed.ncbi.nlm.nih.gov/15630480/); [PMID 21551270](https://pubmed.ncbi.nlm.nih.gov/21551270/); [PMID 24627342](https://pubmed.ncbi.nlm.nih.gov/24627342/); [PMID 23486253](https://pubmed.ncbi.nlm.nih.gov/23486253/) | Non-homology + convergent zinc use; METE-loss ↔ auxotrophy correlation and mutualism |
| F003 bifunctionality / mis-annotation | [PMID 15576367](https://pubmed.ncbi.nlm.nih.gov/15576367/); [PMID 11832514](https://pubmed.ncbi.nlm.nih.gov/11832514/); [PMID 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/) | Single loci span/straddle routes or run catabolically |
| F004 SAM-sensing regulation | [PMID 18039762](https://pubmed.ncbi.nlm.nih.gov/18039762/); [PMID 20951706](https://pubmed.ncbi.nlm.nih.gov/20951706/) | S-box riboswitch couples output to SAM/methionine status |
| F005 single-residue specificity switch | [PMID 18216013](https://pubmed.ncbi.nlm.nih.gov/18216013/); [PMID 31889085](https://pubmed.ncbi.nlm.nih.gov/31889085/) | Glu111/Gly111 flips donor; route not readable from identity |
| F006 deep origin | [PMID 39665745](https://pubmed.ncbi.nlm.nih.gov/39665745/) | LUCA-era recruitment of Met/Cys into the code |
| MetH/MetE mechanism | [PMID 12832615](https://pubmed.ncbi.nlm.nih.gov/12832615/); [PMID 17924667](https://pubmed.ncbi.nlm.nih.gov/17924667/); [PMID 15326182](https://pubmed.ncbi.nlm.nih.gov/15326182/); [PMID 10625458](https://pubmed.ncbi.nlm.nih.gov/10625458/); [PMID 26657067](https://pubmed.ncbi.nlm.nih.gov/26657067/) | Conformational cycling, zinc-ligand identity, double-barrel evolution |
| Engineering / MetA control | [PMID 31891734](https://pubmed.ncbi.nlm.nih.gov/31891734/); [PMID 37312226](https://pubmed.ncbi.nlm.nih.gov/37312226/) | MetA lability/feedback as flux bottleneck |

---

## 11. Limitations and Knowledge Gaps

This review is a **literature synthesis**, not a primary-data analysis; no genome-scale reconstruction was actually benchmarked, so the reliability of an OR-satisfiability oracle across genomes was inferred from mechanistic case studies rather than measured. The strongest genetic evidence for redundancy (F001) comes from a single organism (*C. glutamicum*); generalization is plausible but unproven. Kinetic comparisons (F001) are in vitro and may not reflect in vivo flux. Evolutionary-origin claims (F006) rest on ancestral reconstruction, which carries model-dependent uncertainty. Several players (MetZ, the full diversity of MetY orthologs, eukaryotic compartmentalization) were not examined in depth. Most detailed mechanistic data derive from a small number of model organisms, and extrapolation to all biology is explicitly avoided.

---

## 12. Proposed Follow-up Experiments and Actions

1. **Benchmark the oracle.** Assemble genomes with experimentally verified methionine prototrophy/auxotrophy and measure how often homology-based calling of MetA/MetX and MetB+MetC/MetY gives the correct route, quantifying the mis-annotation rate implied by F003/F005.
2. **Residue-level annotation features.** Encode active-site determinants (acyltransferase position-111; MetY vs γ-lyase active-site signatures) into the oracle so route identity is called from structure-informed motifs, not global identity.
3. **Bifunctionality flagging.** Add logic to detect metB-family loci that may satisfy both step-2 literals or run catabolically, avoiding false prototrophy calls.
4. **Conditional-prototroph handling.** Model MetH-only genomes as B12-conditional, integrating cobalamin biosynthesis/transport genes — directly informed by the algal METE-loss finding.
5. **Flux-aware scoring.** Where both step-2 branches are present, weight by regulatory and kinetic context (sulfide availability, methionine feedback) rather than treating the edges as equivalent.

---

## 13. Key References

- Hwang B-J, et al. *Corynebacterium glutamicum* utilizes both transsulfuration and direct sulfhydrylation for methionine biosynthesis. **J Bacteriol** 2002. [PMID 11844756](https://pubmed.ncbi.nlm.nih.gov/11844756/).
- Hwang B-J, et al. Biochemical analysis on the parallel pathways of methionine biosynthesis in *C. glutamicum*. 2007. [PMID 18050920](https://pubmed.ncbi.nlm.nih.gov/18050920/).
- Tran TH, et al. A novel sulfur-transfer mechanism by O-acetylhomoserine sulfhydrylase (MetY) in *Wolinella succinogenes*. 2011. [PMID 21931214](https://pubmed.ncbi.nlm.nih.gov/21931214/).
- Wheeler PR, et al. Functional demonstration of reverse transsulfuration in the *M. tuberculosis* complex. 2005. [PMID 15576367](https://pubmed.ncbi.nlm.nih.gov/15576367/).
- Auger S, et al. The *metIC* operon in *Bacillus subtilis* is controlled by transcription antitermination (S-box). 2002. [PMID 11832514](https://pubmed.ncbi.nlm.nih.gov/11832514/).
- Chaton CT, et al. Structural analysis of mycobacterial homoserine transacetylases (MetX). 2019. [PMID 31889085](https://pubmed.ncbi.nlm.nih.gov/31889085/).
- Zubieta C, et al. A single amino acid change is responsible for evolution of acyltransferase specificity in bacterial methionine biosynthesis. **J Biol Chem** 2008. [PMID 18216013](https://pubmed.ncbi.nlm.nih.gov/18216013/).
- Wehbi S, et al. Order of amino acid recruitment into the genetic code resolved by LUCA's protein domains. **PNAS** 2024. [PMID 39665745](https://pubmed.ncbi.nlm.nih.gov/39665745/).
- Pejchal R, Ludwig ML. Cobalamin-independent methionine synthase (MetE): a face-to-face double barrel that evolved by gene duplication. **PLoS Biol** 2005. [PMID 15630480](https://pubmed.ncbi.nlm.nih.gov/15630480/).
- Ferrer J-L, et al. Crystal structures of MetE complexed with zinc, homocysteine, and methyltetrahydrofolate (*Arabidopsis*). 2004. [PMID 15326182](https://pubmed.ncbi.nlm.nih.gov/15326182/).
- Zhou ZS, et al. Identification of the zinc ligands in MetE from *E. coli*. 1999. [PMID 10625458](https://pubmed.ncbi.nlm.nih.gov/10625458/).
- Wheatley RW, et al. Fungal cobalamin-independent methionine synthase (*Neurospora crassa* MetE). 2016. [PMID 26657067](https://pubmed.ncbi.nlm.nih.gov/26657067/).
- Bandarian V, Ludwig ML, Matthews RG. Conformational equilibria in cobalamin-dependent methionine synthase (MetH). **PNAS** 2003. [PMID 12832615](https://pubmed.ncbi.nlm.nih.gov/12832615/).
- Fleischhacker AS, Matthews RG. Ligand trans influence governs conformation in MetH. 2007. [PMID 17924667](https://pubmed.ncbi.nlm.nih.gov/17924667/).
- Helliwell KE, et al. Insights into the evolution of vitamin B12 auxotrophy from sequenced algal genomes. 2011. [PMID 21551270](https://pubmed.ncbi.nlm.nih.gov/21551270/).
- Helliwell KE, et al. Unraveling vitamin B12-responsive gene regulation in algae. 2014. [PMID 24627342](https://pubmed.ncbi.nlm.nih.gov/24627342/).
- Xie B, et al. *Chlamydomonas reinhardtii* thermal tolerance mediated by B12-producing bacteria (METE/METH switch). 2013. [PMID 23486253](https://pubmed.ncbi.nlm.nih.gov/23486253/).
- Tomsic J, et al. Natural variability in SAM-dependent S-box riboswitches in *B. subtilis*. 2007. [PMID 18039762](https://pubmed.ncbi.nlm.nih.gov/18039762/).
- Lu C, et al. SAM recognition and conformational switching in the *B. subtilis* yitJ S-box/SAM-I riboswitch. 2010. [PMID 20951706](https://pubmed.ncbi.nlm.nih.gov/20951706/).
- Tang Q, et al. Regulation of homoserine O-succinyltransferase (MetA) for efficient L-methionine production in *E. coli*. 2020. [PMID 31891734](https://pubmed.ncbi.nlm.nih.gov/31891734/).
- Multivariate modular metabolic engineering for enhanced L-methionine biosynthesis in *E. coli*. 2023. [PMID 37312226](https://pubmed.ncbi.nlm.nih.gov/37312226/).

---

*Prepared as an autonomous review synthesis (finalized after 3 iterations). Uncertainty is flagged throughout; mechanistic generalizations from single model organisms are identified as such. Grounded in 35 primary sources / authoritative reviews and 6 confirmed findings.*


## Artifacts

- [OpenScientist final report](methionine_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](methionine_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)