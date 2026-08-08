---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:43:41.044913'
end_time: '2026-07-18T17:57:25.747019'
duration_seconds: 824.7
template_file: templates/module_research.md.j2
template_variables:
  module_title: Ubiquinone biosynthesis from chorismate-derived 4-hydroxybenzoate
  module_summary: Species-neutral pathway for de novo biosynthesis of ubiquinone (coenzyme
    Q) from the chorismate-derived aromatic head group 4-hydroxybenzoate and a polyprenyl
    diphosphate side chain. The bacterial pathway begins with UbiC chorismate lyase,
    UbiA polyprenyltransferase, and UbiD-dependent decarboxylation, with UbiX providing
    the prenylated-FMN cofactor required by UbiD-family decarboxylases. Subsequent
    hydroxylation and methylation steps, carried out by UbiH/VisC/Coq7-like monooxygenases
    and UbiG/UbiE methyltransferases, tailor the prenylated aromatic ring to mature
    ubiquinone.
  module_outline: "- Ubiquinone biosynthesis\n  - 1. aromatic head-group synthesis\n\
    \  - 4-hydroxybenzoate formation from chorismate\n    - UbiC: chorismate lyase\
    \ (molecular player: UbiC chorismate lyase family; activity or role: chorismate\
    \ lyase activity)\n  - 2. polyprenyl side-chain attachment\n  - Polyprenylation\
    \ of 4-hydroxybenzoate\n    - UbiA: 4-hydroxybenzoate polyprenyltransferase (molecular\
    \ player: UbiA 4-hydroxybenzoate polyprenyltransferase family; activity or role:\
    \ 4-hydroxybenzoate polyprenyltransferase activity)\n  - 3. UbiD decarboxylation\
    \ and prFMN cofactor supply\n  - prFMN-dependent decarboxylation\n    - UbiX:\
    \ flavin prenyltransferase (molecular player: UbiX flavin prenyltransferase family;\
    \ activity or role: flavin prenyltransferase activity)\n    - UbiD: 4-hydroxy-3-polyprenylbenzoate\
    \ decarboxylase (molecular player: UbiD prFMN-dependent decarboxylase family;\
    \ activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)\n \
    \ - 4. aromatic ring hydroxylation\n  - Hydroxylation of prenylated ubiquinone\
    \ intermediates\n    - UbiH/VisC-family: 2-polyprenylphenol 6-hydroxylase (molecular\
    \ player: UbiH/VisC ubiquinone hydroxylase family; activity or role: 2-polyprenylphenol\
    \ 6-hydroxylase activity)\n    - UbiH: 2-octaprenyl-6-methoxyphenol hydroxylase\
    \ (molecular player: UbiH/VisC ubiquinone hydroxylase family; activity or role:\
    \ 2-octaprenyl-6-methoxyphenol hydroxylase activity)\n    - Coq7: 3-demethoxyubiquinol\
    \ 3-hydroxylase (molecular player: Coq7 demethoxyubiquinol hydroxylase family;\
    \ activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)\n  - 5. aromatic\
    \ ring methylation\n  - O- and C-methylation of ubiquinone intermediates\n   \
    \ - UbiG: 2-polyprenyl-6-hydroxyphenol methylase (molecular player: UbiG ubiquinone\
    \ O-methyltransferase family; activity or role: 2-polyprenyl-6-hydroxyphenol methylase\
    \ activity)\n    - UbiE: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase\
    \ (molecular player: UbiE/Coq5 ubiquinone C-methyltransferase family; activity\
    \ or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)\n\
    \    - UbiG: 3-demethylubiquinol 3-O-methyltransferase (molecular player: UbiG\
    \ ubiquinone O-methyltransferase family; activity or role: 3-demethylubiquinol\
    \ 3-O-methyltransferase activity)"
  module_connections: '- 4-hydroxybenzoate formation from chorismate feeds into Polyprenylation
    of 4-hydroxybenzoate

    - Polyprenylation of 4-hydroxybenzoate feeds into prFMN-dependent decarboxylation

    - UbiX: flavin prenyltransferase feeds into UbiD: 4-hydroxy-3-polyprenylbenzoate
    decarboxylase

    - prFMN-dependent decarboxylation feeds into Hydroxylation of prenylated ubiquinone
    intermediates

    - Hydroxylation of prenylated ubiquinone intermediates feeds into O- and C-methylation
    of ubiquinone intermediates'
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
  path: ubiquinone_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiquinone_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Ubiquinone biosynthesis from chorismate-derived 4-hydroxybenzoate

## Working Scope

Species-neutral pathway for de novo biosynthesis of ubiquinone (coenzyme Q) from the chorismate-derived aromatic head group 4-hydroxybenzoate and a polyprenyl diphosphate side chain. The bacterial pathway begins with UbiC chorismate lyase, UbiA polyprenyltransferase, and UbiD-dependent decarboxylation, with UbiX providing the prenylated-FMN cofactor required by UbiD-family decarboxylases. Subsequent hydroxylation and methylation steps, carried out by UbiH/VisC/Coq7-like monooxygenases and UbiG/UbiE methyltransferases, tailor the prenylated aromatic ring to mature ubiquinone.

## Provisional Biological Outline

- Ubiquinone biosynthesis
  - 1. aromatic head-group synthesis
  - 4-hydroxybenzoate formation from chorismate
    - UbiC: chorismate lyase (molecular player: UbiC chorismate lyase family; activity or role: chorismate lyase activity)
  - 2. polyprenyl side-chain attachment
  - Polyprenylation of 4-hydroxybenzoate
    - UbiA: 4-hydroxybenzoate polyprenyltransferase (molecular player: UbiA 4-hydroxybenzoate polyprenyltransferase family; activity or role: 4-hydroxybenzoate polyprenyltransferase activity)
  - 3. UbiD decarboxylation and prFMN cofactor supply
  - prFMN-dependent decarboxylation
    - UbiX: flavin prenyltransferase (molecular player: UbiX flavin prenyltransferase family; activity or role: flavin prenyltransferase activity)
    - UbiD: 4-hydroxy-3-polyprenylbenzoate decarboxylase (molecular player: UbiD prFMN-dependent decarboxylase family; activity or role: 4-hydroxy-3-polyprenylbenzoate decarboxylase activity)
  - 4. aromatic ring hydroxylation
  - Hydroxylation of prenylated ubiquinone intermediates
    - UbiH/VisC-family: 2-polyprenylphenol 6-hydroxylase (molecular player: UbiH/VisC ubiquinone hydroxylase family; activity or role: 2-polyprenylphenol 6-hydroxylase activity)
    - UbiH: 2-octaprenyl-6-methoxyphenol hydroxylase (molecular player: UbiH/VisC ubiquinone hydroxylase family; activity or role: 2-octaprenyl-6-methoxyphenol hydroxylase activity)
    - Coq7: 3-demethoxyubiquinol 3-hydroxylase (molecular player: Coq7 demethoxyubiquinol hydroxylase family; activity or role: 3-demethoxyubiquinol 3-hydroxylase activity)
  - 5. aromatic ring methylation
  - O- and C-methylation of ubiquinone intermediates
    - UbiG: 2-polyprenyl-6-hydroxyphenol methylase (molecular player: UbiG ubiquinone O-methyltransferase family; activity or role: 2-polyprenyl-6-hydroxyphenol methylase activity)
    - UbiE: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase (molecular player: UbiE/Coq5 ubiquinone C-methyltransferase family; activity or role: 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity)
    - UbiG: 3-demethylubiquinol 3-O-methyltransferase (molecular player: UbiG ubiquinone O-methyltransferase family; activity or role: 3-demethylubiquinol 3-O-methyltransferase activity)

## Known Relationships Among Steps

- 4-hydroxybenzoate formation from chorismate feeds into Polyprenylation of 4-hydroxybenzoate
- Polyprenylation of 4-hydroxybenzoate feeds into prFMN-dependent decarboxylation
- UbiX: flavin prenyltransferase feeds into UbiD: 4-hydroxy-3-polyprenylbenzoate decarboxylase
- prFMN-dependent decarboxylation feeds into Hydroxylation of prenylated ubiquinone intermediates
- Hydroxylation of prenylated ubiquinone intermediates feeds into O- and C-methylation of ubiquinone intermediates

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

# Ubiquinone Biosynthesis from Chorismate-Derived 4-Hydroxybenzoate: A Mechanistic Review

*A review-style synthesis of the de novo pathway to coenzyme Q, from the aromatic head group 4-hydroxybenzoate and a polyprenyl side chain through the fully substituted benzoquinone ring.*

---

## 1. Executive summary

Ubiquinone (coenzyme Q, UQ or CoQ) is a redox-active polyprenylated benzoquinone lipid that shuttles electrons and protons in respiratory and photosynthetic electron-transport chains and acts as a membrane antioxidant. Its biosynthesis is conceptually simple — take an aromatic ring, hang a long isoprenoid tail on it, and decorate the ring with two methoxy groups, one methyl group, and two ring-oxygens arranged as a *para*-quinone — but mechanistically remarkable, because almost every tailoring reaction operates on an extremely hydrophobic substrate.

The best-understood version of the pathway, in *Escherichia coli*, proceeds in five conceptual modules: (1) **head-group synthesis**, in which UbiC (chorismate lyase) converts the shikimate-pathway branch-point metabolite chorismate to 4-hydroxybenzoate (4-HB); (2) **prenylation**, in which the intramembrane prenyltransferase UbiA attaches an octaprenyl tail to 4-HB; (3) **decarboxylation**, in which the UbiD family enzyme removes the ring carboxyl using the exotic prenylated-FMN (prFMN) cofactor supplied by the flavin prenyltransferase UbiX; and (4–5) **ring tailoring**, three hydroxylations (UbiI/UbiH/UbiF, FAD-monooxygenases) interleaved with three methylations (the O-methyltransferase UbiG and the C-methyltransferase UbiE). A central modern insight is that in bacteria the tailoring reactions are carried out not by free membrane enzymes but by a soluble ~1-MDa **Ubi metabolon** that sequesters the hydrophobic intermediates in the SCP2 lipid-binding cavity of UbiJ [PMID:30686758]. Eukaryotes reproduce this metabolon logic on the matrix face of the mitochondrial inner membrane with a **COQ "synthome"** (Coq3–Coq9 plus the regulatory UbiB-family kinase Coq8) [PMID:17391640; PMID:38425362], but with a divergent parts list — notably lacking recognizable UbiC/UbiX/UbiD orthologs.

The system's deepest origin appears to lie in **cyanobacteria**, with subsequent diversification in proteobacteria and, via the mitochondrial endosymbiont, in eukaryotes [PMID:29106540]. The clearest axis of variation is **oxygen**: the canonical hydroxylases are O₂-dependent flavin monooxygenases, whereas many bacteria run an **O₂-independent route** (UbiT/UbiU/UbiV) to make UQ anaerobically [PMID:31289180; PMID:32409583]. Below I lay out the boundaries of the system, the current mechanistic model, the molecular machines that execute it, its evolutionary and cell-biological variants, the ordering and compartment constraints, and the principal controversies.

---

## 2. Definition and biological boundaries

### 2.1 What is included

For the purpose of this review, the "system" is the **de novo enzymatic conversion of 4-hydroxybenzoate plus a polyprenyl-diphosphate into mature ubiquinone**, comprising:

- Formation of the aromatic head group 4-HB from chorismate (UbiC in γ-proteobacteria).
- Attachment of the polyprenyl tail (UbiA / eukaryotic COQ2).
- Removal of the ring carboxyl (UbiD + UbiX cofactor supply).
- Sequential ring hydroxylation and O-/C-methylation to install the two methoxy, one methyl and the *para*-quinone oxygens (UbiI/H/F, UbiG, UbiE; eukaryotic Coq6/Coq7, Coq3, Coq5).
- The accessory factors that organize these reactions (UbiJ/UbiK scaffolds; Coq4/Coq8/Coq9).

### 2.2 Adjacent processes that should be treated separately

Several neighboring processes are frequently conflated with UQ biosynthesis and are better treated as **inputs, outputs, or parallel pathways**:

- **The shikimate pathway and chorismate branch point.** Chorismate is the shared precursor of folate, menaquinone, enterobactin, tryptophan, tyrosine and phenylalanine. UbiC merely taps this pool; the shikimate pathway itself is upstream and not part of UQ biosynthesis proper.
- **Isoprenoid (polyprenyl-diphosphate) synthesis.** The tail is built by the MEP or mevalonate pathway plus a dedicated polyprenyl-diphosphate synthase (IspB in *E. coli*; PDSS1/PDSS2 in humans). This determines side-chain length (Q₈ in *E. coli*, Q₆ in yeast, Q₉/Q₁₀ in mammals) but is a **separate module** feeding UbiA.
- **Menaquinone / plastoquinone biosynthesis.** These are chemically related prenylquinones made by partly homologous machinery (the UbiA superfamily of intramembrane prenyltransferases is shared) [PMID:26922674; PMID:28018418], but they use different ring precursors and are distinct pathways.
- **The mevalonate pathway and its clinical modulation.** Statins lower CoQ indirectly by blocking mevalonate-derived isoprenoid supply; this is a regulatory/pharmacological effect on precursor availability, not a step of the ring-modification pathway [PMID:37202505].
- **Downstream UQ function and trafficking.** UQ's roles in respiration, in ferroptosis suppression via FSP1 [PMID:35395704], and its inter-organelle distribution (mediated in yeast by the UbiB-family proteins Cqd1/Cqd2) [PMID:34362905] are consequences of, not steps in, biosynthesis.

### 2.3 Competing definitions

There is genuine definitional tension over **where the ring precursor comes from** and therefore where the pathway "starts." The chorismate→4-HB→UbiC definition is faithful to *E. coli*, but is not universal: eukaryotes generate 4-HB largely from **tyrosine** (and some fungi via a **mandelate pathway**) rather than by a UbiC-type chorismate lyase [PMID:32561586; PMID:30822625], and several organisms can also use alternative ring precursors (e.g., *para*-aminobenzoate in yeast, coumarate/vanillate in some plants). A species-neutral definition therefore treats "4-HB (or an equivalent aromatic ring precursor) entering prenylation" as the true boundary, and treats "chorismate → 4-HB by UbiC" as the *bacterial-specific* entry reaction.

---

## 3. Mechanistic overview

The consensus reaction sequence, using *E. coli* (aerobic) nomenclature, is:

1. **Chorismate → 4-hydroxybenzoate (4-HB)** — UbiC chorismate (pyruvate-)lyase eliminates pyruvate and aromatizes the ring [PMID:1644192; PMID:4595202]. *Obligatory as an entry point in bacteria; substituted by tyrosine-derived routes in eukaryotes.*
2. **4-HB → 3-octaprenyl-4-hydroxybenzoate (OPP)** — UbiA transfers the octaprenyl tail from octaprenyl-diphosphate onto ring C3 [PMID:4552989; PMID:26922674]. *Obligatory; commits the ring to the membrane phase.*
3. **OPP → 2-octaprenylphenol (2-OPP)** — UbiD decarboxylates the ring using prFMN; UbiX supplies prFMN by prenylating FMN with a dimethylallyl unit [PMID:28754323; PMID:32951834]. *Obligatory in bacteria; UbiX cofactor supply is obligately upstream of UbiD.*
4. **Ring tailoring — three hydroxylations + three methylations, interleaved.** The ring is decorated by three FAD-monooxygenase hydroxylations at distinct ring positions — UbiI catalyzes the **C5**-hydroxylation [PMID:23709220], with UbiH and UbiF acting at the remaining positions — alternating with O- and C-methylations, because each O-methylation requires a hydroxyl installed by a preceding monooxygenase step. The two O-methyl transfers are both catalyzed by the single SAM-dependent O-methyltransferase **UbiG** — a bifunctional assignment demonstrated directly by showing that purified *E. coli* UbiG (and its eukaryotic ortholog Coq3) catalyzes both O-methylation steps [PMID:10419476] — and the single ring C-methyl by **UbiE** [PMID:24480387]. (Exact positional order of individual tailoring steps is best defined in *E. coli*; the precise sequence and intermediate identities differ in eukaryotes.)

The **best current model** is thus a defined, largely linear reaction order in which prenylation and decarboxylation precede the alternating hydroxylation/methylation steps, and in which the whole tailoring phase is executed within a supramolecular assembly rather than by diffusing enzymes.

**Obligatory vs conditional vs accessory:**
- *Obligatory chemistry*: prenylation (UbiA), decarboxylation (UbiD/UbiX), and the full set of three ring-oxygen insertions and three methylations — no mature UQ forms without them.
- *Conditional*: the **identity of the hydroxylases** depends on oxygen. Under aerobiosis, FAD monooxygenases (UbiI/UbiH/UbiF) use O₂ as the oxygen donor; under anaerobiosis, UbiT/UbiU/UbiV replace them with an O₂-independent mechanism [PMID:23709220; PMID:31289180; PMID:32409583]. UbiC itself is conditional/replaceable (tyrosine route in eukaryotes).
- *Accessory*: the scaffolding/regulatory factors **UbiJ, UbiK** (bacteria) [PMID:36142227; PMID:28559279] and **Coq4, Coq8, Coq9** (eukaryotes) [PMID:17391640; PMID:38425362] are essential for efficient flux and complex integrity but do not themselves carry out ring chemistry (Coq8 is an ATPase/atypical kinase, not a canonical Coq enzyme).

---

## 4. Major molecular players and active assemblies

| Module | Bacterial enzyme (family) | Reaction | Eukaryotic counterpart | Key refs |
|---|---|---|---|---|
| Head group | **UbiC** (chorismate lyase) | chorismate → 4-HB + pyruvate | (no ortholog; 4-HB from Tyr) | PMID:1644192 |
| Prenylation | **UbiA** (UbiA intramembrane prenyltransferase superfamily) | 4-HB + octaprenyl-PP → OPP | **COQ2** | PMID:4552989; PMID:26922674 |
| Cofactor supply | **UbiX** (flavin prenyltransferase) | FMN + DMAP(P) → prFMN | (none) | PMID:31142738; PMID:32951834 |
| Decarboxylation | **UbiD** (prFMN (de)carboxylase) | OPP → 2-OPP + CO₂ | (non-orthologous) | PMID:28754323; PMID:33763291 |
| Hydroxylation | **UbiI, UbiH, UbiF** (FAD monooxygenases, aerobic) / **UbiU, UbiV** (anaerobic) | 3× ring hydroxylation | **Coq6** (+Coq7 di-iron hydroxylase) | PMID:23709220; PMID:31289180 |
| Methylation | **UbiG** (O-MTase), **UbiE** (C-MTase), SAM-dependent | 2× O-methyl, 1× C-methyl | **Coq3** (O), **Coq5** (C) | PMID:24480387 |
| Scaffold / regulation | **UbiJ** (SCP2 cavity), **UbiK** | substrate channeling | **Coq4, Coq8/ADCK, Coq9** | PMID:30686758; PMID:36142227; PMID:38425362 |

### 4.1 The prFMN cofactor and the UbiX–UbiD module
UbiX performs a non-metal-dependent prenyl transfer resembling class I terpene-cyclase chemistry, linking a dimethylallyl moiety to the FMN N5 and C6 to create a fourth, non-aromatic ring; after oxidative maturation to an iminium species, prFMN is competent for UbiD catalysis [PMID:31142738; PMID:32951834]. UbiD-family enzymes are **reversible (de)carboxylases**; the well-characterized model member ferulic acid decarboxylase (Fdc1) reveals a reversible **1,3-dipolar cycloaddition** between prFMN and substrate [PMID:33763291; PMID:28754323]. This module is the mechanistic showpiece of the pathway and the part with the greatest biocatalytic reach beyond UQ (aromatic acid (de)carboxylation) [PMID:38176649].

### 4.2 The Ubi metabolon and the hydrophobicity problem
The signature organizational insight is that the last six reactions in *E. coli* are catalyzed by a **stable, soluble ~1-MDa metabolon of seven Ubi proteins**, in which the SCP2 domain of **UbiJ** provides an extended hydrophobic cavity that binds the polyprenylated intermediates and hands them from enzyme to enzyme in a hydrophilic cytoplasm [PMID:30686758]. **UbiK** is an accessory factor that complexes with UbiJ [PMID:28559279; PMID:36142227]. This directly resolves the paradox of how soluble tailoring enzymes act on membrane-partitioning substrates.

### 4.3 The eukaryotic COQ synthome
Yeast Coq3/4/5/6/7/9 co-migrate at ~1 MDa and are mutually stabilizing (loss of one destabilizes the others) [PMID:17391640]. Reconstitution of the animal metabolon in vitro (via ancestral sequence reconstruction) captured the pathway and demonstrated that the atypical **UbiB-family kinase COQ8** "increases and streamlines" CoQ output [PMID:38425362]. COQ8/ADCK3/ADCK4 is an ancient atypical protein-kinase-like ATPase whose activity is stimulated by CoQ intermediates and phospholipids and is required for synome integrity [PMID:32479562; PMID:36302899].

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across lineages
- **Deep origin.** Comparative genomics places the origin of Q biosynthesis in **cyanobacteria**, followed by diversification in anaerobic α-proteobacteria whose extant relatives resemble the mitochondrial pathway more than the *E. coli* Ubi pathway [PMID:29106540]. Two branches emerge: the *ubi* genes (proteobacteria/*E. coli*) and the *coq* genes (eukaryotes/mitochondria).
- **Head-group entry differs.** Chorismate lyase (UbiC) is essentially a bacterial solution; eukaryotes derive 4-HB from **tyrosine**, and some ascomycete yeasts use a **mandelate pathway** for benzenoid supply [PMID:32561586; PMID:30822625].
- **The prFMN module is bacterially specific.** Eukaryotes lack recognizable UbiX/UbiD, so the decarboxylation and its cofactor supply are handled by **non-orthologous** means — a major discontinuity in an otherwise deeply conserved pathway.
- **Side-chain length is lineage-tuned** by the polyprenyl-diphosphate synthase (Q₈ *E. coli*, Q₆ *S. cerevisiae*, Q₉ rodents, Q₁₀ humans), even though the ring chemistry is conserved.

### 5.2 Physiological-state variation (oxygen)
The strongest, best-supported conditional variation is the **oxygen regime**. Aerobically, three FAD monooxygenases (UbiI/UbiH/UbiF) insert ring oxygens using O₂ [PMID:23709220]. Anaerobically, a distinct set (**UbiT, UbiU, UbiV**) performs O₂-independent hydroxylation, allowing continuous UQ production across the whole O₂ range [PMID:31289180; PMID:32409583]. UbiT carries an SCP2 domain (a UbiJ paralog) specialized for anaerobic conditions. This is a textbook case of **alternative molecular routes achieving the same chemical outcome**.

### 5.3 Compartment and cell biology
- In bacteria, evidence points to a **cytoplasmic/soluble metabolon** despite lipid substrates [PMID:30686758].
- In eukaryotes, synthesis occurs on the **matrix face of the mitochondrial inner membrane** via the COQ synthome [PMID:17391640], after which UQ must be **distributed** to other membranes — a process governed by UbiB-family proteins (Cqd1/Cqd2 in yeast) and still incompletely understood [PMID:34362905].
- **Disease relevance**: defects in COQ genes cause primary CoQ deficiency (e.g., steroid-resistant nephrotic syndrome, encephalomyopathy), sometimes responsive to CoQ₁₀ supplementation [PMID:35643375; PMID:39864756], underscoring that the pathway's output is rate-limiting for human mitochondrial function.

---

## 6. Constraints, dependencies, and failure modes

- **Strict ordering at the front end.** Prenylation (UbiA) must precede decarboxylation and tailoring: the ring must be committed to the lipid phase before the hydrophobic-substrate-handling machinery engages it. UbiC (or an equivalent 4-HB source) must precede UbiA.
- **Cofactor-supply dependency.** UbiX-generated prFMN is *obligately* required before UbiD can act; without mature prFMN, decarboxylation fails and prenylphenol intermediates accumulate [PMID:28754323].
- **Alternating hydroxylation/methylation.** The interleaving of O-methylation (which requires a preceding hydroxyl) and hydroxylation imposes a defined sequence; the two UbiG O-methylations act on hydroxyls generated by preceding monooxygenase steps [PMID:24480387].
- **Oxygen as a hard constraint on enzyme identity.** Aerobic FAD monooxygenases cannot function without O₂; organisms that respire anaerobically *must* deploy the UbiT/U/V system or fail to make UQ under anoxia [PMID:31289180]. UbiI is demonstrably aerobic-only, with an alternative enzyme catalyzing C5-hydroxylation anaerobically [PMID:23709220].
- **Metabolon integrity as a failure mode.** In both bacteria and eukaryotes, disrupting a scaffold or one enzyme destabilizes the whole assembly, producing a CoQ-less phenotype and accumulation of pathway intermediates [PMID:17391640; PMID:36142227]. This is the molecular basis of secondary CoQ deficiencies.
- **Evidence ruling out otherwise-plausible paths.** The metabolon data argue *against* a purely diffusion-based, fully membrane-embedded assembly line for the tailoring steps [PMID:30686758]; the identification of the O₂-independent hydroxylases rules against the earlier assumption that UQ synthesis is strictly aerobic [PMID:31289180].

---

## 7. Controversies and open questions

1. **Do bacteria run the pathway soluble or membrane-bound?** The ~1-MDa soluble Ubi metabolon challenges the classical membrane-bound model [PMID:30686758]. How intermediates partition between the SCP2 cavity and the membrane, and whether the metabolon docks transiently to membranes, remain open.
2. **How is the anaerobic hydroxylation chemistry actually done?** UbiT/U/V enable O₂-independent hydroxylation, but the oxygen donor and catalytic mechanism (proposed metallo-/radical chemistry) are not fully resolved [PMID:32409583].
3. **What replaces UbiC/UbiX/UbiD in eukaryotes?** The eukaryotic decarboxylation step and its "cofactor logic" are enigmatic; several reactions in the animal metabolon were only recently captured in vitro and some remain uncharacterized [PMID:38425362]. More broadly, as of authoritative review the CoQ pathway "has not been fully defined in any organism," with multiple steps catalyzed by still-unidentified enzymes [PMID:28927698].
4. **What does COQ8 actually do?** Despite being essential, the precise catalytic contribution of the UbiB-family kinase/ATPase (phosphorylation vs ATP-dependent chaperoning of the synome, vs lipid extraction) is still debated [PMID:32479562; PMID:36302899].
5. **How is mature UQ trafficked from its synthesis site?** The export/distribution machinery (Cqd1/Cqd2 and beyond) is only beginning to be defined [PMID:34362905].
6. **Cross-organism extrapolation risks.** Much mechanistic detail comes from *E. coli*, *S. cerevisiae*, and reconstituted animal enzymes; ring-modification order, precursor choice, and enzyme complements differ enough between lineages that findings should not be assumed universal.

---

## 8. Key references

- Aussel L, et al. *Biosynthesis and physiology of coenzyme Q in bacteria.* Biochim Biophys Acta. 2014. **PMID:24480387** — authoritative bacterial pathway review.
- Stefely JA, Pagliarini DJ. *Biochemistry of Mitochondrial Coenzyme Q Biosynthesis.* Trends Biochem Sci. 2017. **PMID:28927698** — authoritative eukaryotic review; open questions and unidentified steps.
- Poon WW, et al. *Yeast/rat Coq3 and E. coli UbiG catalyze both O-methyltransferase steps.* J Biol Chem. 1999. **PMID:10419476** — one O-MTase performs both O-methylations; matrix-side localization.
- Hajj Chehade M, et al. *A Soluble Metabolon Synthesizes the Isoprenoid Lipid Ubiquinone.* Cell Rep. 2019. **PMID:30686758** — the ~1-MDa Ubi metabolon / UbiJ SCP2 cavity.
- Loiseau L, et al. *The UbiK protein is an accessory factor… forms a complex with UbiJ.* J Biol Chem. 2017. **PMID:28559279**; Launay E, et al. 2022. **PMID:36142227** — UbiJ/UbiK scaffolds.
- Marshall SA, et al. *The UbiX-UbiD system: biosynthesis and use of prFMN.* 2017. **PMID:28754323**; *UbiX resembles terpene-cyclase chemistry.* PNAS 2019. **PMID:31142738**; Saaret A, et al. *Biochemistry of prenylated-FMN enzymes.* 2020. **PMID:32951834** — prFMN cofactor.
- Payne KAP, et al. *Structure and Mechanism of Fdc1-type UbiD (de)carboxylases.* 2021. **PMID:33763291** — reversible 1,3-cycloaddition decarboxylation.
- Hajj Chehade M, et al. *ubiI… aerobic C5-hydroxylation.* J Biol Chem. 2013. **PMID:23709220** — first structure of a UQ monooxygenase; aerobic vs anaerobic hydroxylation.
- Pelosi L, et al. *Ubiquinone Biosynthesis over the Entire O₂ Range.* mBio 2019. **PMID:31289180**; Vo CD, et al. 2020. **PMID:32409583** — O₂-independent UbiT/U/V route.
- Degli Esposti M. *A Journey across Genomes Uncovers the Origin of Ubiquinone in Cyanobacteria.* 2017. **PMID:29106540** — evolutionary origin.
- Siebert M, et al. *Cloning of ubiC (chorismate pyruvate-lyase) and ubiA.* 1992. **PMID:1644192** — head-group and prenylation genes.
- Li W. *The UbiA Superfamily of Intramembrane Aromatic Prenyltransferases.* J Mol Biol. 2016. **PMID:26922674** — UbiA prenyltransferase family/structure.
- Hsieh EJ, et al. *Coq9 is a subunit of the mitochondrial CoQ biosynthetic complex.* 2007. **PMID:17391640** — eukaryotic ~1-MDa COQ complex.
- Nicoll CR, et al. *In vitro construction of the COQ metabolon.* 2024. **PMID:38425362** — reconstituted animal metabolon; COQ8 kinase role.
- Awad AM, et al. 2020 **PMID:32479562**; Murray J, et al. 2023 **PMID:36302899**; Kemmerer ZA, et al. 2021 **PMID:34362905** — COQ8/UbiB kinase and CoQ distribution.
- Drovandi S, et al. 2022 **PMID:35643375**; Fernández-Ayala D, et al. 2025 **PMID:39864756** — human/Drosophila CoQ deficiency and supplementation.

---

*Uncertainty statement.* The bacterial pathway (especially *E. coli*) is the most rigorously supported, including enzyme structures and reconstituted chemistry for UbiX/UbiD and the metabolon. Eukaryotic steps are strong for enzyme identity and complex organization but weaker for the decarboxylation-equivalent chemistry and for UQ trafficking. Oxygen-dependent vs O₂-independent hydroxylation is well supported genetically/biochemically, but the anaerobic mechanism is not fully solved. Claims here are anchored to specific organisms and should not be assumed to hold uniformly across all of biology.


## Artifacts

- [OpenScientist final report](ubiquinone_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiquinone_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30686758
2. PMID:17391640
3. PMID:38425362
4. PMID:29106540
5. PMID:31289180
6. PMID:32409583
7. PMID:26922674
8. PMID:28018418
9. PMID:37202505
10. PMID:35395704
11. PMID:34362905
12. PMID:32561586
13. PMID:30822625
14. PMID:1644192
15. PMID:4595202
16. PMID:4552989
17. PMID:28754323
18. PMID:32951834
19. PMID:23709220
20. PMID:10419476
21. PMID:24480387
22. PMID:36142227
23. PMID:28559279
24. PMID:31142738
25. PMID:33763291
26. PMID:38176649
27. PMID:32479562
28. PMID:36302899
29. PMID:35643375
30. PMID:39864756
31. PMID:28927698