---
title: "Rare Earth Element (REE) Extraction Pathways"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# Rare Earth Element (REE) Extraction Pathways

Engineered biological pathways to **sense, mobilize, capture, concentrate, and release** rare earth elements

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## Why this is interesting

- REEs (La, Ce, Pr, Nd … Lu, Y) and co-occurring strategic metals (Co, Ni, Mn, Cu, Zn, Fe) are critical for magnets, batteries, and electronics
- Conventional extraction is chemically harsh and produces difficult-to-separate mixtures of chemically similar lanthanides
- **Biomining** offers a milder, tunable alternative driven by living chassis
- Biology already does lanthanide chemistry: **lanthanide-dependent enzymes** are widespread in methylotrophs
- Goal: program microbial or plant chassis to do selective metal recovery

---

## Target scope

**REEs:** La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Y

**Strategic co-occurring metals:** Co, Ni, Mn, Cu, Zn, Fe

**System goals**
1. Detect metal ions in complex matrices
2. Mobilize metals via leaching (acidolysis, redoxolysis)
3. Bind and sequester selectively
4. Concentrate intracellularly
5. Trigger controlled export into recovery solution

---

## Key biology: lanthanides are biological

- Methylotrophs use **lanthanide-dependent methanol dehydrogenases** (XoxF-type MDHs) — Ln³⁺ sits in the active site
- **Lanmodulin (lanM)** is a compact, highly REE-selective EF-hand binding protein [PMID:35814700]
- **Lanthanophores** (e.g. methylolanthanin) are secreted small molecules that mobilize REEs, analogous to siderophores for iron
- Dedicated **lut** uptake clusters import lanthanides into the cell [PMID:35875576]
- These natural parts are the building blocks for engineered recovery pathways

---

## Approach: AI-assisted gene review → design

- Use the AI gene review framework to map candidate genes to chassis and annotate GO terms
- Decompose recovery into **four modules**: detect → mobilize/leach → capture/uptake → sequester/concentrate → export/release
- For each module: pick candidate gene systems, candidate chassis, and selectivity strategies
- Conceptual blueprint (placeholder loci flagged TBD where biology is not yet mapped)

```
Sensing → [TF/Riboswitch] → Leaching agents → Solubilized ions
       → Selective binding → Uptake → Sequestration → Export → Recovery
```

---

## Module 1: Biosensors + leaching control

**Sense target metals, induce leaching agents (acidolysis + redoxolysis)**

- Metal-responsive regulators: NikR (Ni), MntR (Mn), CnrX/CnrY/CnrH (Co/Ni)
- Acidolysis via PQQ-dependent gluconate: gcd + pqqABCDE/pqqFG [PMID:7665488; PMID:9043136]
- Redox shuttles: phenazine operon phzA–G [PMID:8586283; PMID:28871340]
- Fe(II) oxidation bioleaching: rus operon (cyc2, cyc1, coxBACD, rus)

**METEA lanthanophore loci:** mll cluster `MexAM1_META1p4132–4138`, regulators mluA/R/I `META1p4129–4131`, PQQ `META1p1748/1751` → methylolanthanin secretion

---

## Module 2: Selective binding + uptake

**Capture solubilized metals with high selectivity, transfer into the cell**

- Lanthanide-binding protein: **lanM** (lanmodulin)
- Lanthanide uptake cluster: **lutH** (TonB receptor) + lut genes (`META1_1778–1787`, includes lanM and lutD)
- Ln-dependent MDH module: xoxF + xoxG + xoxJ [PMID:31017712]
- Ni uptake: nikABCDE + NikR [PMID:9882686]; Mn uptake: mntH [PMID:21908668]

**METEA loci:** lanM `META1p1786`; xoxF1 `META1p1740`; xoxG `META1p1741`; xoxJ `META1p1742`

**Selectivity:** geometry matched to REE ionic radius; competitive exclusion of Fe/Cu/Zn; pH-gated binding

---

## Module 3: Sequestration + concentration

**Store metals safely and concentrate to useful levels**

- Metallothionein: **smtA** (cyanobacterial; transferable module) [PMID:1607014]
- Polyphosphate granules: ppk1/ppk2 polyphosphate kinases [PMID:12486232; PMID:17360677]
- Engineered protein nanocages / bacterial microcompartments

**Readouts:** fluorescent REE reporters; growth-linked selection for high accumulators

**METEA status:** lanthasome-like polyphosphate storage phenotype reported, but specific storage loci **not yet mapped** — a discovery priority

---

## Module 4: Inducible export + recovery

**Release concentrated metals into recovery solution after harvest**

- Co/Zn/Cd efflux: czcCBA RND pump [PMID:12867443]
- Co/Ni efflux: cnrCBA + cnrYXH regulation [PMID:10671463]
- Ni/Co efflux: rcnA + rcnR [PMID:15805538]; Mn efflux: mntP

**Timing for fractionation:**
```
T0 Harvest → T1 Induce REE export → T2 Collect REE fraction
           → T3 Induce Co/Ni/Mn export (secondary fraction)
```

**METEA status:** REE/Co/Ni/Mn efflux loci remain **TBD** — to map once transporters are identified

---

## Chassis comparison

| Chassis | Strengths | Primary role | Best-fit module(s) |
|---|---|---|---|
| *M. extorquens* AM1 (METEA) | Native Ln use; lanthanophore + lut + xoxF | High-selectivity REE acquisition/handling | Binding/uptake, sequestration |
| *A. ferrooxidans* | Extreme acid tolerance; Fe(II) oxidation | Aggressive bioleaching | Biosensor/leaching |
| *Cupriavidus* sp. CH34 | Broad metal resistance; czc/cnr efflux | Post-harvest export/detox | Export/recovery |
| *P. chlororaphis* | Robust secretion; phenazine shuttles | Redox-assisted leaching | Leaching |

---

## Chassis scoring (heuristic)

Weights: REE selectivity 0.45, leaching strength 0.35, metal tolerance 0.20

| Chassis | REE sel. | Leaching | Tolerance | Weighted |
|---|---:|---:|---:|---:|
| *M. extorquens* AM1 (METEA) | 5 | 2 | 3 | **3.75** |
| *A. ferrooxidans* | 1 | 5 | 5 | 3.00 |
| *P. chlororaphis* | 2 | 4 | 3 | 2.85 |
| *Cupriavidus* CH34 | 2 | 2 | 5 | 2.75 |

*Heuristic placeholders — tune after pilot assays (leaching rates, uptake specificity, survival).*

---

## Challenges

- **Selectivity** among chemically similar lanthanides, and REE vs Fe/Cu/Zn competition in real matrices
- **Chassis engineering:** acid tolerance, genetic stability under metal stress, growth vs accumulation tradeoff
- **Sparse annotation:** METEA storage and export loci still TBD; biology not fully mapped
- Avoiding non-specific uptake of toxic metals
- Biosecurity and containment (kill-switches)

---

## Conclusions & future directions

**Status:** IN_PROGRESS — modular conceptual blueprint with chassis-mapped candidate genes

**Next steps**
- Map candidate genes to chassis species and annotate GO terms
- Identify literature for REE-binding proteins and lanthanide transport systems
- Prototype biosensor circuits with tunable thresholds and logic gates
- Pilot small-scale bioleaching with complex ore simulants

**Milestones:** reporter strains → leaching induction → selective uptake → intracellular concentration → triggered export with measured purity
