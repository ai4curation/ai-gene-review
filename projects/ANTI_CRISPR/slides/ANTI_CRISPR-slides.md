---
title: "Anti-CRISPR Proteins"
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

# Anti-CRISPR Proteins

### Phage-encoded inhibitors of bacterial CRISPR-Cas — an evolutionary arms race

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## Why anti-CRISPR proteins?

Anti-CRISPR (Acr) proteins are **phage-encoded inhibitors** of bacterial CRISPR-Cas immune systems — a striking example of the evolutionary arms race between bacteria and their viral predators.

They present four distinct challenges for GO annotation:

1. **Novel molecular mechanisms** — often not well-captured by existing GO terms
2. **Dual-targeting strategies** — some Acrs interact with both protein and RNA components
3. **Regulatory complexity** — expression tightly regulated via Aca (anti-CRISPR associated) repressors
4. **Sparse annotations** — many Acr proteins carry only generic IEA annotations

Mechanisms are well-studied structurally, but annotations lag behind.

---

## Key biology: Acr and Aca

**Acr proteins** inhibit CRISPR-Cas, organized by the CRISPR type they target:

- **Type I-F** (AcrIF) — target the Csy surveillance complex
- **Type I-E** (AcrIE) — target the Cascade complex
- **Type II** (AcrIIA / AcrIIC) — target Cas9 / Cas12
- **Type III** — target Csm / Cmr complexes

**Aca repressors** regulate Acr expression in a negative-feedback loop.

---

## Inhibition strategies

Acr proteins disable CRISPR-Cas through diverse mechanisms:

- Blocking DNA recognition
- Preventing R-loop formation
- Mimicking DNA substrates
- Direct crRNA binding (a unique mechanism)
- Enzymatic inactivation

This mechanistic diversity is exactly what makes precise GO annotation hard.

---

## The approach: AI-assisted gene review

We apply the **AI gene review framework** to Acr proteins:

- Review existing GO annotations against strict GO guidelines
- Synthesize literature + structural biology + bioinformatics
- Identify over-general or missing annotations
- Propose specific replacement and **new GO terms** where the ontology is insufficient

Acrs are excellent targets: structurally well-characterized, but under-annotated.

---

## Featured example: AcrF8

**Pectobacterium phage ZF40** · Organism **BPZF4** · UniProt **H9C181** · Status **COMPLETE**

- 92-amino acid protein inhibiting the **Type I-F** CRISPR-Cas system
- **Dual-targeting**: binds BOTH the Cas7f protein backbone AND the crRNA scaffold
- Contacts crRNA nucleotides **U[+21], U[+22], G[+23]** at **<4 Å** distance
- Blocks R-loop formation and prevents target DNA recognition
- Cryo-EM structure at **3.42 Å** (PMID:32170016)

---

## AcrF8: annotation issues identified

| Existing term | Problem | Action |
|---------------|---------|--------|
| GO:0052170 — symbiont-mediated suppression of host innate immune response | Too general | MODIFY → GO:0098672 |
| GO:0098672 — symbiont-mediated suppression of host CRISPR-cas system | Specific target | Replacement term |
| Ribonucleoprotein complex binding | Missing | Add core function |

A more specific term (GO:0098672) precisely captures the CRISPR-Cas target,
and the dual protein-RNA binding requires explicit core-function annotation.

---

## AcrF8: proposed new GO term

**Name**: CRISPR RNA binding anti-CRISPR activity

**Justification**: Current terms do not distinguish between Acrs that *only* bind Cas proteins and those that *directly contact crRNA*.

AcrF8 defines a **unique class** with dual protein-RNA binding:
- It contacts crRNA nucleotides at <4 Å
- Existing GO terms cannot express this mechanism

A dedicated term would let curators capture the crRNA-binding mechanism distinctly.

---

## Key mechanisms to annotate

1. **Surveillance complex binding** — GO:0043021 (ribonucleoprotein complex binding)
2. **CRISPR-Cas suppression** — GO:0098672 (symbiont-mediated suppression of host CRISPR-cas system)
3. **DNA mimic function** — where Acrs structurally mimic DNA
4. **crRNA binding** — direct RNA contacts (needs a new term?)

---

## Challenges of GO annotation for Acrs

- **Mechanistic novelty** outpaces the ontology — terms for crRNA-binding inhibition do not yet exist
- **Dual targeting** (protein + RNA) is hard to express with a single MF term
- **Generic IEA annotations** dominate, leaving rich structural knowledge uncaptured
- **Regulatory context** (Aca feedback loops) adds layers not reflected in current annotations
- Over-general terms (e.g. GO:0052170) need MODIFY actions to more specific targets

---

## Key references

- Bondy-Denomy J et al. (2013) *Nature* — Anti-CRISPR discovery
- Pawluk A et al. (2016) *Cell* — AcrIF mechanisms
- Wang J et al. (2020) *Nat Commun* — AcrF8/F9/F6 cryo-EM structures (PMID:32170016)
- Stanley SY et al. (2019) *Cell* — Aca repressor mechanisms (PMID:31474367)

Presented at the **Gene Ontology Consortium Meeting, October 2025, Cambridge UK**.

---

## Conclusions & future directions

**Status: project COMPLETE for the AcrF8 flagship review**

The AcrF8 example demonstrates:
1. Need for more **specific GO terms** for CRISPR-Cas inhibition mechanisms
2. Value of **structural biology** in informing function annotations
3. Importance of distinguishing **protein-only vs. protein+RNA** binding mechanisms

**Next steps**:
- Identify additional Acr proteins in UniProt / QuickGO
- Review Aca regulator annotations
- Propose new GO terms for crRNA-binding mechanisms
