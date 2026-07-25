---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T08:22:42.432942'
end_time: '2026-07-15T09:15:34.661132'
duration_seconds: 3172.23
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pentose phosphate pathway
  module_summary: A reusable central-carbon module for the pentose phosphate pathway,
    covering the oxidative conversion of glucose 6-phosphate to ribulose 5-phosphate
    and the non-oxidative interconversion of pentose phosphates with fructose 6-phosphate
    and glyceraldehyde 3-phosphate. The oxidative branch generates NADPH through glucose-6-phosphate
    dehydrogenase and 6-phosphogluconate dehydrogenase, with 6-phosphogluconolactonase
    hydrolyzing the intermediate lactone. The non-oxidative branch uses ribose-5-phosphate
    isomerase, ribulose-phosphate 3-epimerase, transketolase, and transaldolase to
    balance ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose 7-phosphate, erythrose
    4-phosphate, fructose 6-phosphate, and glyceraldehyde 3-phosphate. Pseudomonas
    putida KT2440 proteins are used as concrete exemplars, but the boundary is the
    conserved PPP chemistry rather than a KT2440-specific KEGG map.
  module_outline: "- Pentose phosphate pathway\n  - 1. oxidative branch from glucose\
    \ 6-phosphate to ribulose 5-phosphate\n  - Pentose phosphate oxidative branch\n\
    \    - 1. glucose 6-phosphate oxidation\n    - Glucose-6-phosphate dehydrogenase\n\
    \      - Glucose-6-phosphate dehydrogenase (molecular player: glucose-6-phosphate\
    \ dehydrogenase family; activity or role: glucose-6-phosphate dehydrogenase activity)\n\
    \    - 2. lactone hydrolysis\n    - 6-phosphogluconolactonase\n      - 6-phosphogluconolactonase\
    \ (molecular player: 6-phosphogluconolactonase family; activity or role: 6-phosphogluconolactonase\
    \ activity)\n    - 3. oxidative decarboxylation to ribulose 5-phosphate\n    -\
    \ 6-phosphogluconate dehydrogenase\n      - 6-phosphogluconate dehydrogenase (molecular\
    \ player: 6-phosphogluconate dehydrogenase family; activity or role: phosphogluconate\
    \ dehydrogenase (decarboxylating) activity)\n  - 2. non-oxidative pentose-phosphate\
    \ rearrangements\n  - Pentose phosphate non-oxidative branch\n    - 1. ribulose\
    \ 5-phosphate to ribose 5-phosphate\n    - Ribose-5-phosphate isomerase\n    \
    \  - Ribose-5-phosphate isomerase (molecular player: ribose-5-phosphate isomerase\
    \ family; activity or role: ribose-5-phosphate isomerase activity)\n    - 2. ribulose\
    \ 5-phosphate to xylulose 5-phosphate\n    - Ribulose-phosphate 3-epimerase\n\
    \      - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate\
    \ 3-epimerase family; activity or role: D-ribulose-phosphate 3-epimerase activity)\n\
    \    - 3. first two-carbon transfer\n    - Transketolase: xylulose 5-phosphate\
    \ plus ribose 5-phosphate\n      - Transketolase first PPP reaction (molecular\
    \ player: bacterial transketolase family; activity or role: transketolase activity)\n\
    \    - 4. three-carbon transfer\n    - Transaldolase\n      - Transaldolase (molecular\
    \ player: transaldolase family; activity or role: transaldolase activity)\n  \
    \  - 5. second two-carbon transfer\n    - Transketolase: xylulose 5-phosphate\
    \ plus erythrose 4-phosphate\n      - Transketolase second PPP reaction (molecular\
    \ player: bacterial transketolase family; activity or role: transketolase activity)"
  module_connections: '- Glucose-6-phosphate dehydrogenase feeds into 6-phosphogluconolactonase:
    6-phospho-D-glucono-1,5-lactone produced by G6PDH is the Pgl substrate.

    - 6-phosphogluconolactonase feeds into 6-phosphogluconate dehydrogenase: 6-phospho-D-gluconate
    produced by Pgl is the substrate for the decarboxylating dehydrogenase step.

    - 6-phosphogluconate dehydrogenase feeds into Ribose-5-phosphate isomerase: Ribulose
    5-phosphate from the oxidative branch is the substrate for ribose-5-phosphate
    isomerase.

    - 6-phosphogluconate dehydrogenase feeds into Ribulose-phosphate 3-epimerase:
    Ribulose 5-phosphate from the oxidative branch is also the substrate for ribulose-phosphate
    3-epimerase.

    - Ribose-5-phosphate isomerase feeds into Transketolase: xylulose 5-phosphate
    plus ribose 5-phosphate: Ribose 5-phosphate is one substrate for the first transketolase
    step.

    - Ribulose-phosphate 3-epimerase feeds into Transketolase: xylulose 5-phosphate
    plus ribose 5-phosphate: Xylulose 5-phosphate is the ketose donor for the first
    transketolase step.

    - Transketolase: xylulose 5-phosphate plus ribose 5-phosphate feeds into Transaldolase:
    Sedoheptulose 7-phosphate and glyceraldehyde 3-phosphate from transketolase are
    the transaldolase substrates.

    - Transaldolase feeds into Transketolase: xylulose 5-phosphate plus erythrose
    4-phosphate: Erythrose 4-phosphate from transaldolase is used by the second transketolase
    step.

    - Ribulose-phosphate 3-epimerase feeds into Transketolase: xylulose 5-phosphate
    plus erythrose 4-phosphate: Xylulose 5-phosphate also supplies the second transketolase
    step.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 31
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pentose_phosphate_pathway-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pentose_phosphate_pathway-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Pentose phosphate pathway

## Working Scope

A reusable central-carbon module for the pentose phosphate pathway, covering the oxidative conversion of glucose 6-phosphate to ribulose 5-phosphate and the non-oxidative interconversion of pentose phosphates with fructose 6-phosphate and glyceraldehyde 3-phosphate. The oxidative branch generates NADPH through glucose-6-phosphate dehydrogenase and 6-phosphogluconate dehydrogenase, with 6-phosphogluconolactonase hydrolyzing the intermediate lactone. The non-oxidative branch uses ribose-5-phosphate isomerase, ribulose-phosphate 3-epimerase, transketolase, and transaldolase to balance ribose 5-phosphate, xylulose 5-phosphate, sedoheptulose 7-phosphate, erythrose 4-phosphate, fructose 6-phosphate, and glyceraldehyde 3-phosphate. Pseudomonas putida KT2440 proteins are used as concrete exemplars, but the boundary is the conserved PPP chemistry rather than a KT2440-specific KEGG map.

## Provisional Biological Outline

- Pentose phosphate pathway
  - 1. oxidative branch from glucose 6-phosphate to ribulose 5-phosphate
  - Pentose phosphate oxidative branch
    - 1. glucose 6-phosphate oxidation
    - Glucose-6-phosphate dehydrogenase
      - Glucose-6-phosphate dehydrogenase (molecular player: glucose-6-phosphate dehydrogenase family; activity or role: glucose-6-phosphate dehydrogenase activity)
    - 2. lactone hydrolysis
    - 6-phosphogluconolactonase
      - 6-phosphogluconolactonase (molecular player: 6-phosphogluconolactonase family; activity or role: 6-phosphogluconolactonase activity)
    - 3. oxidative decarboxylation to ribulose 5-phosphate
    - 6-phosphogluconate dehydrogenase
      - 6-phosphogluconate dehydrogenase (molecular player: 6-phosphogluconate dehydrogenase family; activity or role: phosphogluconate dehydrogenase (decarboxylating) activity)
  - 2. non-oxidative pentose-phosphate rearrangements
  - Pentose phosphate non-oxidative branch
    - 1. ribulose 5-phosphate to ribose 5-phosphate
    - Ribose-5-phosphate isomerase
      - Ribose-5-phosphate isomerase (molecular player: ribose-5-phosphate isomerase family; activity or role: ribose-5-phosphate isomerase activity)
    - 2. ribulose 5-phosphate to xylulose 5-phosphate
    - Ribulose-phosphate 3-epimerase
      - Ribulose-phosphate 3-epimerase (molecular player: ribulose-phosphate 3-epimerase family; activity or role: D-ribulose-phosphate 3-epimerase activity)
    - 3. first two-carbon transfer
    - Transketolase: xylulose 5-phosphate plus ribose 5-phosphate
      - Transketolase first PPP reaction (molecular player: bacterial transketolase family; activity or role: transketolase activity)
    - 4. three-carbon transfer
    - Transaldolase
      - Transaldolase (molecular player: transaldolase family; activity or role: transaldolase activity)
    - 5. second two-carbon transfer
    - Transketolase: xylulose 5-phosphate plus erythrose 4-phosphate
      - Transketolase second PPP reaction (molecular player: bacterial transketolase family; activity or role: transketolase activity)

## Known Relationships Among Steps

- Glucose-6-phosphate dehydrogenase feeds into 6-phosphogluconolactonase: 6-phospho-D-glucono-1,5-lactone produced by G6PDH is the Pgl substrate.
- 6-phosphogluconolactonase feeds into 6-phosphogluconate dehydrogenase: 6-phospho-D-gluconate produced by Pgl is the substrate for the decarboxylating dehydrogenase step.
- 6-phosphogluconate dehydrogenase feeds into Ribose-5-phosphate isomerase: Ribulose 5-phosphate from the oxidative branch is the substrate for ribose-5-phosphate isomerase.
- 6-phosphogluconate dehydrogenase feeds into Ribulose-phosphate 3-epimerase: Ribulose 5-phosphate from the oxidative branch is also the substrate for ribulose-phosphate 3-epimerase.
- Ribose-5-phosphate isomerase feeds into Transketolase: xylulose 5-phosphate plus ribose 5-phosphate: Ribose 5-phosphate is one substrate for the first transketolase step.
- Ribulose-phosphate 3-epimerase feeds into Transketolase: xylulose 5-phosphate plus ribose 5-phosphate: Xylulose 5-phosphate is the ketose donor for the first transketolase step.
- Transketolase: xylulose 5-phosphate plus ribose 5-phosphate feeds into Transaldolase: Sedoheptulose 7-phosphate and glyceraldehyde 3-phosphate from transketolase are the transaldolase substrates.
- Transaldolase feeds into Transketolase: xylulose 5-phosphate plus erythrose 4-phosphate: Erythrose 4-phosphate from transaldolase is used by the second transketolase step.
- Ribulose-phosphate 3-epimerase feeds into Transketolase: xylulose 5-phosphate plus erythrose 4-phosphate: Xylulose 5-phosphate also supplies the second transketolase step.

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

# The Pentose Phosphate Pathway as a Two-Module, Mode-Switching Central-Carbon Device

*A commissioned review-style synthesis for a molecular-biology audience. Pseudomonas putida KT2440 proteins are used as concrete bacterial exemplars, but the intended boundary of the system is the conserved chemistry of glucose-6-phosphate oxidation and pentose-phosphate rearrangement, not any one organism's metabolic map.*

---

## 1. Executive Summary

The pentose phosphate pathway (PPP) is best understood not as a single linear route but as **two coupled biochemical modules** whose net direction is dictated by cellular boundary demand rather than by any fixed metabolic wiring diagram. The **oxidative branch** — glucose-6-phosphate dehydrogenase (G6PDH/Zwf), 6-phosphogluconolactonase (Pgl), and 6-phosphogluconate dehydrogenase (6PGDH/Gnd) — irreversibly converts glucose 6-phosphate (G6P) to ribulose 5-phosphate (Ru5P), paying out two molecules of NADPH and releasing CO₂. The **non-oxidative branch** — ribose-5-phosphate isomerase (Rpi), ribulose-phosphate 3-epimerase (Rpe), the thiamine-diphosphate (ThDP)-dependent transketolase, and the Schiff-base transaldolase — reversibly rearranges the five-carbon pool against fructose 6-phosphate (F6P) and glyceraldehyde 3-phosphate (G3P), supplying ribose 5-phosphate (R5P) for nucleotides and erythrose 4-phosphate (E4P) for aromatic amino acids.

The central mechanistic insight from this investigation is a **thermodynamic and directional asymmetry** between the two modules. Only the two dehydrogenase steps are truly obligatory and directional; the lactonase is a *protective accelerant* rather than a thermodynamically necessary step, and the entire non-oxidative branch operates near equilibrium and is freely reversible. As a direct consequence, the identical enzyme set can run in at least three distinct operating modes: (i) a forward, NADPH-generating oxidative mode; (ii) a reversed, ribose-synthesizing mode that draws R5P from glycolytic intermediates without spending the oxidative branch; and (iii) a cyclic mode in which oxidative and non-oxidative reactions merge with glycolytic/gluconeogenic reactions to fine-tune redox output. The cyclic mode is exemplified by the **EDEMP cycle** of *Pseudomonas putida* KT2440 and by light/dark redox switching between the oxidative PPP and the reductive Calvin–Benson cycle in plant plastids.

The pathway's sugar-phosphate interconversion chemistry is **ancient and pre-enzymatic**: reconstituted Archean-ocean conditions catalyse many of the same reactions non-enzymatically, with Fe(II) acting as catalyst and cosubstrate and pH setting network topology. Against this deep conservation of chemistry sits a striking degree of *non-homologous convergence* in the protein families that later domesticated it — most clearly in ribose-5-phosphate isomerase, where two structurally unrelated families (RpiA and RpiB) independently catalyse the same reaction. The most important open questions concern quantitative flux control, the moonlighting/non-catalytic roles of PPP enzymes, and rigorous ancestral reconstruction of the expanded protein families.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

For the purposes of this review, the PPP comprises exactly the reactions that (a) oxidise G6P to Ru5P with NADPH production and (b) interconvert the resulting pentose phosphates with F6P and G3P. Concretely:

**Oxidative branch (irreversible, directional):**

| Step | Enzyme (EC) | Reaction | Output |
|------|-------------|----------|--------|
| 1 | Glucose-6-phosphate dehydrogenase, Zwf (1.1.1.49/363) | G6P → 6-phospho-D-glucono-1,5-lactone | NAD(P)H |
| 2 | 6-Phosphogluconolactonase, Pgl (3.1.1.31) | δ-lactone → 6-phospho-D-gluconate | (protective hydrolysis) |
| 3 | 6-Phosphogluconate dehydrogenase, Gnd (1.1.1.44) | 6-phosphogluconate → ribulose 5-phosphate + CO₂ | NADPH |

**Non-oxidative branch (near-equilibrium, reversible):**

| Step | Enzyme (EC) | Reaction |
|------|-------------|----------|
| 4 | Ribose-5-phosphate isomerase, Rpi (5.3.1.6) | Ru5P ⇌ R5P |
| 5 | Ribulose-phosphate 3-epimerase, Rpe (5.1.3.1) | Ru5P ⇌ Xu5P |
| 6 | Transketolase, Tkt (2.2.1.1) | Xu5P + R5P ⇌ S7P + G3P |
| 7 | Transaldolase, Tal (2.2.1.2) | S7P + G3P ⇌ E4P + F6P |
| 8 | Transketolase, Tkt (2.2.1.1) | Xu5P + E4P ⇌ F6P + G3P |

### 2.2 What should be treated separately

Several neighbouring processes are frequently conflated with the PPP but are mechanistically distinct and belong outside the boundary:

- **The Entner–Doudoroff (ED) pathway.** In many bacteria (notably *Pseudomonas*), G6P oxidation and 6-phosphogluconate share chemistry with the oxidative PPP but are then channelled through ED-specific enzymes (Edd/Eda) rather than 6PGDH. G6PDH is genuinely a *branch point* feeding either the reductive PPP or the ED route, so the two must be distinguished even though they share intermediates ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)).
- **The reductive Calvin–Benson cycle.** The non-oxidative PPP enzymes (transketolase, aldolase-type chemistry, and pentose interconversions) are *shared* with the reductive pentose-phosphate cycle in plastids, but the physiological direction and the presence/absence of active oxidative steps differ, and the two are reciprocally regulated ([PMID: 24079807](https://pubmed.ncbi.nlm.nih.gov/24079807/)).
- **The phosphoketolase "bifid shunt."** Phosphoketolase is a ThDP-dependent relative of transketolase that cleaves Xu5P/F6P using inorganic phosphate to make acetyl-phosphate; it is a distinct enzyme with distinct chemistry ([PMID: 36974963](https://pubmed.ncbi.nlm.nih.gov/36974963/)).
- **Downstream NADPH consumers** — the glutathione and thioredoxin reductase systems — are the *reason* the oxidative branch exists physiologically but are not part of the pathway itself.

### 2.3 Competing definitions

The literature carries at least two implicit definitions. The classical textbook picture treats the PPP as a linear "shunt" off glycolysis with fixed stoichiometry. The systems/flux picture, supported here, treats it as a directionally plastic module whose operating mode is set by demand — the definition that best accommodates the EDEMP cycle and plastid redox gating.

---

## 3. Mechanistic Overview

### 3.1 The best current model: two modules, one directional gate

The core model that emerges from this investigation (**Finding F010**) is that the PPP is gated at exactly two points — the two dehydrogenases — and is otherwise a freely equilibrating carbon-shuffling network:

```
                    IRREVERSIBLE, DIRECTIONAL                 NEAR-EQUILIBRIUM, REVERSIBLE
                 ┌───────────────────────────┐        ┌──────────────────────────────────────┐

   Glucose 6-P ──►[G6PDH]──► 6-P-glucono-δ-lactone
      (G6P)      +NADPH          │
                                 ▼ [Pgl]  (protective accelerant)
                          6-phosphogluconate
                                 │
                                 ▼ [6PGDH]  +NADPH +CO2
                          ribulose 5-P (Ru5P) ──┬──►[Rpi]──► ribose 5-P (R5P) ──┐
                                                │                                ├─►[TKT-1]─► S7P + G3P
                                                └──►[Rpe]──► xylulose 5-P (Xu5P)─┘        │
                                                                                          ▼ [TAL]
                                                                                     E4P + F6P
                                                                     Xu5P ──►[TKT-2]──► F6P + G3P
                                                                              (with E4P)
```

Two irreversible NADPH-producing steps commit carbon and set the forward direction; everything to the right of Ru5P is a reversible carbon economy that balances whatever the cell needs.

### 3.2 Obligatory vs. conditional vs. accessory steps

- **Obligatory and directional:** G6PDH and 6PGDH. These are the only two steps that are effectively irreversible under physiological conditions and thus define pathway directionality (**F001, F004, F010**).
- **Accessory (protective, not thermodynamically required):** 6-phosphogluconolactonase. NMR kinetics show that G6PDH produces exclusively the δ-(1→5) lactone, a highly electrophilic species that *can* hydrolyse spontaneously but can also isomerise to a "dead-end" γ-(1→4) form or react toxically with cellular nucleophiles. Pgl selectively accelerates hydrolysis of the δ-form, channelling the reactive intermediate and preventing both the unproductive γ-lactone and cytotoxicity (**F008**; [PMID: 11457850](https://pubmed.ncbi.nlm.nih.gov/11457850/)).
- **Conditional/reversible:** Rpi, Rpe, transketolase (both reactions), and transaldolase. These run in whichever direction the boundary metabolite concentrations dictate.

### 3.3 Catalytic chemistry of the non-oxidative enzymes

The non-oxidative branch is carried by two chemically distinct classes of carbon-transfer enzyme (**F002**):

- **Transketolase** is a **ThDP-dependent** transferase that moves two-carbon units. Catalysis proceeds through a reactive ThDP **ylide/carbene** intermediate, whose formation at physiological pH depends on dynamic protonation states within the active site ([PMID: 37748048](https://pubmed.ncbi.nlm.nih.gov/37748048/)). The same enzyme performs both PPP two-carbon transfers (steps 6 and 8). Its stereoselective α-hydroxyketone chemistry has made it a workhorse of biocatalysis ([PMID: 41203356](https://pubmed.ncbi.nlm.nih.gov/41203356/)), and bacterial transketolases can show unexpected cooperative kinetics and alternative substrate-binding sites ([PMID: 38145310](https://pubmed.ncbi.nlm.nih.gov/38145310/)).
- **Transaldolase** transfers a three-carbon unit via a **lysine Schiff-base (class I aldolase)** mechanism and is entirely **independent of ThDP**.

This division of labour — ThDP for C2 transfer, a covalent lysine imine for C3 transfer — is a recurring theme and explains why the two enzymes have entirely different fold families despite acting consecutively.

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 Glucose-6-phosphate dehydrogenase (G6PDH / Zwf)

G6PDH catalyses the **first committing step** and is a redox hub, not merely a gateway to Ru5P (**F001**). Two properties are central:

1. **Cofactor plasticity.** G6PDH isozymes differ in NADP⁺/NAD⁺ preference. In *Pseudomonas*, dual-cofactor isozymes exist, and cofactor specificity is a general principle underlying bacterial glycolytic strategy ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/); [PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)). This lets the same reaction serve either biosynthetic NADPH supply or NADH-linked energy metabolism.
2. **Stability as the dominant failure mode.** In humans, G6PD deficiency is the most common enzymopathy (~400–500 million people). Detailed biochemistry of clinical variants shows that most are **folding/stability defects, not catalytic defects** (**F005**). For G6PD(Plymouth, G163D) and G6PD(Mahidol, G163S), Kₘ(NADP⁺), Kₘ(G6P) and k_cat match wild type, yet stability is markedly reduced — after 24 h at 37 °C, WT/Mahidol/Plymouth retained 58.3 / 27.0 / 3.9 % of activity, and NADP⁺ binding stabilises the protein ([PMID: 17959407](https://pubmed.ncbi.nlm.nih.gov/17959407/)). The bacterial enzyme is similarly stabilised by its substrate ([PMID: 31760039](https://pubmed.ncbi.nlm.nih.gov/31760039/)), and small molecules that bridge the dimer interface can rescue oligomerisation and activity ([PMID: 31183991](https://pubmed.ncbi.nlm.nih.gov/31183991/)).

### 4.2 6-Phosphogluconolactonase (Pgl)

A **protective accelerant** that channels the reactive δ-lactone (see §3.2, **F008**). Its dispensability in principle — but importance in practice — makes it the clearest "accessory but valuable" component of the pathway. The literature had long treated the lactonase as questionable precisely because the lactones were believed to hydrolyse spontaneously; the resolution is that the enzyme guards against accumulation of the toxic electrophilic δ-form ([PMID: 11457850](https://pubmed.ncbi.nlm.nih.gov/11457850/)).

### 4.3 6-Phosphogluconate dehydrogenase (6PGDH / Gnd)

The **third PPP enzyme and a principal cellular NADPH generator** feeding thioredoxin/glutathione reductases (**F004**). It is an **obligate homodimer** with a Rossmann NADP⁺-binding domain. Structurally, its C-terminal tail penetrates the partner subunit: truncating the C-terminal 35–53 residues of yeast Gnd1 abolishes activity despite retained dimerisation (Kₘ ≈ 50 µM 6PG, ≈ 35 µM NADP⁺) ([PMID: 17570834](https://pubmed.ncbi.nlm.nih.gov/17570834/)). This intersubunit "arm" is an assembly constraint: the functional unit is the dimer, not the monomer.

### 4.4 Non-oxidative enzymes and non-homologous convergence

A striking feature is **lineage-specific family choice** for chemically identical reactions (**F009**):

- **Ribose-5-phosphate isomerase** exists as two structurally distinct, **non-homologous** classes, **RpiA** and **RpiB**. RpiB predominates in bacteria (with independent recruitments in fungi), yet both catalyse R5P ⇌ Ru5P — a textbook case of convergent evolution to the same reaction ([PMID: 21995815](https://pubmed.ncbi.nlm.nih.gov/21995815/)). RpiB's substrate specificity is itself evolutionarily labile and can be reshaped by gene loss ([PMID: 28362260](https://pubmed.ncbi.nlm.nih.gov/28362260/)).
- **Ribulose-5-phosphate 3-epimerase** adopts a metal-dependent **TIM-barrel** fold, structurally related to epimerases such as UlaE from the anaerobic ascorbate pathway ([PMID: 18849419](https://pubmed.ncbi.nlm.nih.gov/18849419/)).

The lesson for anyone asking "which family member best represents the ancestral role" is that there may be **no single ancestor** — different lineages solved the same isomerisation problem with unrelated scaffolds.

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep, pre-enzymatic origins

The PPP's sugar-phosphate chemistry predates enzymes (**F003**). In reconstituted Archean-ocean mimetics, **29 reactions overlapping glycolysis and the PPP occur non-enzymatically**, including formation and interconversion of ribose 5-phosphate and erythrose 4-phosphate. **Fe(II)** acts as both catalyst and cosubstrate, binds sugar phosphates, and — together with pH — sets the network topology: alkaline conditions favour the PPP-like branch, while neutral/acidic conditions favour glycolysis-like reactivity ([PMID: 24771084](https://pubmed.ncbi.nlm.nih.gov/24771084/); [PMID: 26824074](https://pubmed.ncbi.nlm.nih.gov/26824074/)). This supports a **deep, plausibly pre-LUCA origin** of the pathway *topology*, with enzymes later domesticating a chemistry that already existed. Consistent with broader "gluconeogenic-first" arguments, the well-conserved trunk enzymes of central carbon metabolism are universally distributed, whereas upper-pathway steps derive from multiple independent gene families ([PMID: 15803666](https://pubmed.ncbi.nlm.nih.gov/15803666/)).

### 5.2 Bacterial cyclic operation: the EDEMP cycle

*Pseudomonas putida* KT2440 provides the clearest example that the PPP is a *mode-switching* device (**F006**). ¹³C-flux analysis shows the strain **lacks a functional EMP glycolysis** and channels ~90 % of glucose (via gluconate/6-phosphogluconate) into the ED route, while ~10 % of triose phosphates are **recycled back to hexose phosphates**. This merges ED, gluconeogenic EMP, and PPP reactions into the **EDEMP cycle**, whose default state is a *slight catabolic overproduction of NADPH* — a redox buffer contributing to this organism's environmental robustness ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). *P. putida* central metabolism further shows segregated flux architecture and GAPDH-homolog gatekeeping that tunes co-utilisation of substrates ([PMID: 30936206](https://pubmed.ncbi.nlm.nih.gov/30936206/); [PMID: 41259139](https://pubmed.ncbi.nlm.nih.gov/41259139/)), and the pathway is a practical engineering target for aromatic amino acid production from lignocellulosic sugars via the pentose phosphate pool ([PMID: 34403199](https://pubmed.ncbi.nlm.nih.gov/34403199/)).

### 5.3 Plastid redox gating: avoiding a futile cycle

In photosynthetic plastids, the non-oxidative branch is **physically shared** with the reductive Calvin–Benson cycle, so running the oxidative branch in the light would create a futile cycle (**F007**). Chloroplast G6PDH — catalysing the first, rate-limiting oxidative step — is therefore **redox-regulated by thioredoxin**: a regulatory disulfide is reduced and the enzyme inactivated in the light, coordinating the oxidative PPP with reductive carbon fixation. Mechanistically, reduction of the regulatory disulfide changes substrate accessibility and NADPH-dependent cofactor binding via a conserved Arg residue ([PMID: 24079807](https://pubmed.ncbi.nlm.nih.gov/24079807/); [PMID: 27717462](https://pubmed.ncbi.nlm.nih.gov/27717462/)). Plant plastidial G6PDH isoforms are also notoriously unstable and rapidly lose activity, complicating their study ([PMID: 24161756](https://pubmed.ncbi.nlm.nih.gov/24161756/)).

### 5.4 Physiological states in animals

In mammals the oxidative branch is the redox linchpin of erythrocytes: G6PD deficiency renders red cells vulnerable to oxidative haemolysis after oxidant exposure (e.g., naphthalene, certain drugs) ([PMID: 41763665](https://pubmed.ncbi.nlm.nih.gov/41763665/); [PMID: 39354868](https://pubmed.ncbi.nlm.nih.gov/39354868/)). Yet the phenotype is context-dependent and not uniformly deleterious — humanised G6PD-deficient mice can show *increased* exercise tolerance and improved cardiac mitochondrial function, cautioning against overgeneralising from the erythrocyte ([PMID: 39514761](https://pubmed.ncbi.nlm.nih.gov/39514761/)). In cancer and immune biology, PPP-derived NADPH is a recurring node governing antioxidant capacity, redox-dependent cell death (ferroptosis, cuproptosis, disulfidptosis), and immune tolerance ([PMID: 42190602](https://pubmed.ncbi.nlm.nih.gov/42190602/); [PMID: 42311140](https://pubmed.ncbi.nlm.nih.gov/42311140/); [PMID: 42397604](https://pubmed.ncbi.nlm.nih.gov/42397604/); [PMID: 42372728](https://pubmed.ncbi.nlm.nih.gov/42372728/)).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering constraints

The oxidative branch enforces a strict order because each step consumes the product of the previous one:

```
G6P ──G6PDH──► δ-lactone ──Pgl──► 6-phosphogluconate ──6PGDH──► Ru5P
```

The two dehydrogenases are irreversible, so carbon cannot flow backward through the oxidative branch; ribose synthesised *without* NADPH production must therefore come from the **reversed non-oxidative branch** drawing on F6P and G3P. This is the key evidence that rules out an otherwise plausible "always-oxidative" route to ribose: cells that need R5P but not NADPH bypass the oxidative branch entirely.

### 6.2 Compartment- and state-specific exclusivity

- **Light vs. dark (plastids):** the oxidative branch and reductive carbon fixation are mutually exclusive in time, enforced by thioredoxin redox switching (§5.3).
- **Cofactor-specific routing:** whether G6PDH output supports biosynthesis or energy metabolism depends on the NADP⁺/NAD⁺ preference of the isozyme present (§4.1).
- **Substrate channelling:** the δ-lactone must be hydrolysed before it isomerises to the dead-end γ-form — a kinetic, not thermodynamic, constraint met by Pgl (§3.2).

### 6.3 Failure modes

| Failure mode | Molecular basis | Consequence | Evidence |
|--------------|-----------------|-------------|----------|
| G6PDH instability | Folding/stability defects; loss of NADP⁺ structural stabilisation | Oxidative haemolysis; most common human enzymopathy | [PMID: 17959407](https://pubmed.ncbi.nlm.nih.gov/17959407/), [PMID: 31760039](https://pubmed.ncbi.nlm.nih.gov/31760039/) |
| Lactone toxicity | Loss of Pgl → δ-lactone reacts with nucleophiles or forms γ-dead-end | Toxic adducts, wasted carbon | [PMID: 11457850](https://pubmed.ncbi.nlm.nih.gov/11457850/) |
| 6PGDH assembly failure | C-terminal intersubunit arm truncation | Complete loss of activity despite intact dimer | [PMID: 17570834](https://pubmed.ncbi.nlm.nih.gov/17570834/) |
| Redox miscoordination (plastid) | Failure to inactivate oxidative branch in light | Futile cycle with Calvin–Benson | [PMID: 24079807](https://pubmed.ncbi.nlm.nih.gov/24079807/) |

A recurring theme is that **stability and assembly — not catalytic competence — are the dominant failure points** for the oxidative-branch dehydrogenases.

---

## 7. Mechanistic Model / Interpretation (Synthesis)

Pulling the findings together, the PPP is most coherently described as a **directionally gated carbon-and-redox exchanger** with three operating modes:

| Mode | Boundary demand | Oxidative branch | Non-oxidative branch | Net output |
|------|-----------------|------------------|----------------------|------------|
| **(i) Oxidative / NADPH** | High NADPH need, low nucleotide need | ON (forward) | Forward: Ru5P → F6P + G3P | 2 NADPH per G6P; CO₂ released; carbon returned to glycolysis |
| **(ii) Reversed / ribose-synthesis** | High R5P need, low NADPH need | OFF | Reverse: F6P + G3P → pentose-P | R5P for nucleotides without spending oxidative branch |
| **(iii) Cyclic (EDEMP / redox-buffer)** | Redox robustness under stress | ON | Recycles trioses to hexoses | Net NADPH overproduction (*P. putida*) |

The gate is set by the two irreversible dehydrogenases; the non-oxidative branch is a reversible "gearbox" that lets the cell take whatever carbon it needs from whichever direction is cheapest. Plastids add a fourth wrinkle by sharing the gearbox with reductive carbon fixation and switching the oxidative gate off in the light.

This model directly answers the review brief's central tension: the "known relationships among steps" (the linear feed-forward chain from G6PDH to the second transketolase reaction) are correct as a description of *substrate connectivity*, but they do not fix *direction*. Direction is an emergent property of boundary metabolite concentrations acting on a near-equilibrium network — which is why the same eight enzymes behave so differently in *Pseudomonas*, plastids, and mammalian erythrocytes.

---

## 8. Evidence Base

| PMID | Contribution | Supports finding |
|------|--------------|------------------|
| [33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/) | G6PDH is first committing oxidative step; branch point to reductive PPP or ED; cofactor specificity principle | F001, F010 |
| [36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/) | Oxidative step generates NAD(P)H; links to anabolism and oxidative-stress defense; dual-cofactor isozyme | F001 |
| [37748048](https://pubmed.ncbi.nlm.nih.gov/37748048/) | ThDP carbene intermediate in transketolase; dynamic protonation | F002 |
| [41203356](https://pubmed.ncbi.nlm.nih.gov/41203356/) | Transketolase ThDP mechanism and engineering | F002 |
| [24771084](https://pubmed.ncbi.nlm.nih.gov/24771084/) | Non-enzymatic PPP/glycolysis reactions in Archean-ocean mimetic; Fe(II) catalysis | F003 |
| [26824074](https://pubmed.ncbi.nlm.nih.gov/26824074/) | Iron- and pH-dependent conditional non-enzymatic network topology | F003 |
| [15803666](https://pubmed.ncbi.nlm.nih.gov/15803666/) | Gluconeogenic origin; conserved trunk vs. multi-family upper enzymes | F003 |
| [17570834](https://pubmed.ncbi.nlm.nih.gov/17570834/) | 6PGDH is third PPP enzyme, main NADPH generator; obligate homodimer; C-terminal arm essential | F004 |
| [17959407](https://pubmed.ncbi.nlm.nih.gov/17959407/) | G6PD deficiency variants are folding/stability defects; NADP⁺ stabilises | F005 |
| [31760039](https://pubmed.ncbi.nlm.nih.gov/31760039/) | Bacterial G6PDH stabilised by substrate | F005 |
| [31183991](https://pubmed.ncbi.nlm.nih.gov/31183991/) | Small-molecule G6PD activators bridge dimer interface | F005 |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | EDEMP cycle in *P. putida*; ~90% via ED, ~10% triose recycling; default NADPH overproduction | F006, F010 |
| [24079807](https://pubmed.ncbi.nlm.nih.gov/24079807/) | Chloroplast G6PDH thioredoxin redox regulation; light/dark coordination | F007, F010 |
| [27717462](https://pubmed.ncbi.nlm.nih.gov/27717462/) | Plastidic P2-G6PDH cysteine redox regulation and NADPH inhibition | F007 |
| [11457850](https://pubmed.ncbi.nlm.nih.gov/11457850/) | Pgl accelerates δ-lactone hydrolysis; prevents γ-dead-end and toxicity | F008, F010 |
| [21995815](https://pubmed.ncbi.nlm.nih.gov/21995815/) | Two non-homologous Rpi classes (RpiA/RpiB); convergent evolution | F009 |
| [18849419](https://pubmed.ncbi.nlm.nih.gov/18849419/) | Rpe/UlaE metal-dependent TIM-barrel fold | F009 |
| [28362260](https://pubmed.ncbi.nlm.nih.gov/28362260/) | RpiB substrate specificity evolves via gene loss | F009 |
| [36974963](https://pubmed.ncbi.nlm.nih.gov/36974963/) | Phosphoketolase vs. transketolase distinction (boundary clarification) | Scope |
| [38145310](https://pubmed.ncbi.nlm.nih.gov/38145310/) | Bacterial transketolase cooperativity and alternative sites | F002 |
| [39514761](https://pubmed.ncbi.nlm.nih.gov/39514761/) | G6PD deficiency can improve exercise/cardiac performance | Controversy |

---

## 9. Controversies and Open Questions

1. **Ancestral protein family for isomerisation.** Because RpiA and RpiB are non-homologous yet catalyse the same reaction, there is no single "best representative" of the ancestral isomerase. Whether one class is genuinely older, or whether the reaction was independently captured multiple times, remains unresolved ([PMID: 21995815](https://pubmed.ncbi.nlm.nih.gov/21995815/); [PMID: 28362260](https://pubmed.ncbi.nlm.nih.gov/28362260/)).

2. **How linear is the "textbook" PPP?** Flux data from *P. putida* (EDEMP cycle) and plastids show that the linear map is often a poor description of real flux. The extent to which cyclic/reversed operation dominates in other organisms is largely unmeasured ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)).

3. **Moonlighting and non-catalytic roles.** Glycolytic and PPP enzymes increasingly show non-enzymatic "moonlighting" functions in signalling and disease. Whether PPP enzymes beyond G6PD have physiologically important moonlighting roles is an open and largely correlative area ([PMID: 42311140](https://pubmed.ncbi.nlm.nih.gov/42311140/)).

4. **Organism-mixing in the redox-disease literature.** Much of the ferroptosis/cuproptosis/disulfidptosis literature links "PPP → NADPH → cell fate" using indirect, correlative evidence in cancer cell lines. These claims should not be read as mechanistic statements about the pathway's enzymology.

5. **The physiological cost/benefit of the lactonase.** Pgl is dispensable in principle but protective in practice; quantifying how much toxic flux escapes in its absence, across organisms, is unresolved ([PMID: 11457850](https://pubmed.ncbi.nlm.nih.gov/11457850/)).

6. **Why does G6PD deficiency sometimes help?** The counterintuitive exercise-tolerance and cardiac benefits in humanised deficient mice challenge the assumption that reduced oxidative-branch flux is uniformly harmful ([PMID: 39514761](https://pubmed.ncbi.nlm.nih.gov/39514761/)).

---

## 10. Limitations and Knowledge Gaps

- **Organism breadth.** Direct mechanistic evidence is concentrated in a few systems (yeast Gnd1, human G6PD variants, *Pseudomonas* flux, Arabidopsis/poplar plastid G6PDH, *E. coli*/fungal Rpi). Generalising quantitative flux behaviour to all lineages is not yet warranted.
- **No primary data analysed here.** This review synthesises published biochemistry and structural work; it does not include new experimental measurements. The "findings" are literature-anchored inferences, not fresh assays.
- **Flux control is under-quantified.** The three-mode model is qualitatively well supported but lacks organism-by-organism control coefficients that would say *how much* each gate contributes under defined conditions.
- **Correlative disease literature.** The cancer/immunometabolism papers link PPP-derived NADPH to cell-fate decisions largely by correlation; these should be treated as motivating context, not mechanism.
- **Ancestral reconstruction is incomplete.** The non-homology of RpiA/RpiB means the "ancestral isomerase" question cannot currently be answered from sequence data alone.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Quantitative multi-organism flux atlas.** Apply ¹³C-metabolic flux analysis across phylogenetically diverse microbes (beyond *P. putida*) under matched conditions to measure how often the reversed and cyclic modes dominate, and to estimate control coefficients for the two dehydrogenase gates.
2. **Pgl channelling assay in vivo.** Use isotope-labelled δ-lactone and mass spectrometry in Pgl-knockout vs. wild-type cells to quantify how much reactive lactone escapes to nucleophile adducts or the γ-dead-end, directly testing the "protective accelerant" model.
3. **Ancestral sequence reconstruction of transketolase and 6PGDH.** Resurrect and characterise inferred ancestral enzymes to test whether ancestral forms were cofactor-generalist and whether the obligate 6PGDH dimer arm is ancestral or derived.
4. **Systematic G6PD variant stability screen.** Extend the folding-defect model with high-throughput thermostability and NADP⁺-rescue assays across clinical variants to build a predictive stability–phenotype map, and test small-molecule dimer-interface activators ([PMID: 31183991](https://pubmed.ncbi.nlm.nih.gov/31183991/)) as chemical chaperones.
5. **Plastid futile-cycle test.** Engineer thioredoxin-insensitive G6PDH in plants and measure whether light-driven futile cycling measurably penalises carbon fixation, quantifying the physiological value of redox gating.
6. **RpiA vs. RpiB fitness swap.** Complement an RpiB-dependent bacterium with RpiA (and vice versa) to test whether family choice is neutral or lineage-adaptive.

---

## 12. Key References

- Volke DC, Olavarría K, Nikel PI. *Cofactor Specificity of Glucose-6-Phosphate Dehydrogenase Isozymes in Pseudomonas putida...* [PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)
- Shah et al. *Glucose-6-Phosphate Dehydrogenase, ZwfA... in Pseudomonas bharatica CSV86.* [PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)
- Miclet E et al. *NMR spectroscopic analysis of the first two steps of the pentose-phosphate pathway... role of 6-phosphogluconolactonase.* [PMID: 11457850](https://pubmed.ncbi.nlm.nih.gov/11457850/)
- He W et al. *Crystal structure of Saccharomyces cerevisiae 6-phosphogluconate dehydrogenase Gnd1.* [PMID: 17570834](https://pubmed.ncbi.nlm.nih.gov/17570834/)
- Huang Y et al. *...G6PD(Plymouth) and G6PD(Mahidol): Evidence for defective protein folding...* [PMID: 17959407](https://pubmed.ncbi.nlm.nih.gov/17959407/)
- Benítez-Rangel E et al. *The substrate of the glucose-6-phosphate dehydrogenase of Pseudomonas aeruginosa provides structural stability.* [PMID: 31760039](https://pubmed.ncbi.nlm.nih.gov/31760039/)
- Nikel PI et al. *Pseudomonas putida KT2440... EDEMP cycle.* [PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)
- Née G et al. *Redox regulation of chloroplastic G6PDH activity by thioredoxin...* [PMID: 24079807](https://pubmed.ncbi.nlm.nih.gov/24079807/)
- Cardi M et al. *Plastidic P2 glucose-6P dehydrogenase from poplar... thioredoxin m-type.* [PMID: 27717462](https://pubmed.ncbi.nlm.nih.gov/27717462/)
- Keller MA, Turchyn AV, Ralser M. *Non-enzymatic glycolysis and pentose phosphate pathway-like reactions in a plausible Archean ocean.* [PMID: 24771084](https://pubmed.ncbi.nlm.nih.gov/24771084/)
- Keller MA et al. *Conditional iron and pH-dependent activity of a non-enzymatic glycolysis and pentose phosphate pathway.* [PMID: 26824074](https://pubmed.ncbi.nlm.nih.gov/26824074/)
- Edwards T et al. *Structural characterization of a ribose-5-phosphate isomerase B from Coccidioides immitis.* [PMID: 21995815](https://pubmed.ncbi.nlm.nih.gov/21995815/)
- Shi R et al. *Structure of L-xylulose-5-phosphate 3-epimerase (UlaE)... TIM barrel fold.* [PMID: 18849419](https://pubmed.ncbi.nlm.nih.gov/18849419/)
- *Evolution of substrate specificity in a retained enzyme driven by gene loss (RpiA/RpiB).* [PMID: 28362260](https://pubmed.ncbi.nlm.nih.gov/28362260/)
- *Dynamic Protonation States Underlie Carbene Formation in ThDP-Dependent Enzymes.* [PMID: 37748048](https://pubmed.ncbi.nlm.nih.gov/37748048/)
- *Distribution and phylogenies of EMP enzymes... support a gluconeogenic origin of metabolism.* [PMID: 15803666](https://pubmed.ncbi.nlm.nih.gov/15803666/)

---

## 13. Conclusion

The pentose phosphate pathway is neither a simple linear shunt nor a single cycle: it is a **two-module, directionally gated central-carbon device**. Two irreversible dehydrogenase steps (G6PDH, 6PGDH) commit carbon and produce NADPH; a protective lactonase channels a reactive intermediate; and a reversible, near-equilibrium non-oxidative gearbox (Rpi, Rpe, transketolase, transaldolase) rebalances pentose phosphates against F6P and G3P. Because only the gate is directional, the same enzymes run forward for NADPH, backward for ribose, and cyclically for redox buffering — as demonstrated by the EDEMP cycle in *Pseudomonas putida* and by light/dark redox switching in plastids. The pathway's chemistry is ancient enough to have non-enzymatic, iron-catalysed prebiotic counterparts, yet its enzymes show repeated non-homologous convergence, most vividly in the two unrelated ribose-5-phosphate isomerase families. The largest open questions are quantitative flux control, enzyme moonlighting, and rigorous ancestral reconstruction of the expanded families.


## Artifacts

- [OpenScientist final report](pentose_phosphate_pathway-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pentose_phosphate_pathway-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33727391
2. PMID:24079807
3. PMID:36974963
4. PMID:11457850
5. PMID:37748048
6. PMID:41203356
7. PMID:38145310
8. PMID:36354357
9. PMID:17959407
10. PMID:31760039
11. PMID:31183991
12. PMID:17570834
13. PMID:21995815
14. PMID:28362260
15. PMID:18849419
16. PMID:24771084
17. PMID:26824074
18. PMID:15803666
19. PMID:26350459
20. PMID:30936206
21. PMID:41259139
22. PMID:34403199
23. PMID:27717462
24. PMID:24161756
25. PMID:41763665
26. PMID:39354868
27. PMID:39514761
28. PMID:42190602
29. PMID:42311140
30. PMID:42397604
31. PMID:42372728