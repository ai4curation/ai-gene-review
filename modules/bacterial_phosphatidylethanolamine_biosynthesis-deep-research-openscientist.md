---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:21:08.015769'
end_time: '2026-09-01T16:40:21.799375'
duration_seconds: 1153.78
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial phosphatidylethanolamine biosynthesis through phosphatidylserine
  module_summary: A reusable two-reaction bacterial module for phosphatidylethanolamine
    biosynthesis from CDP-diacylglycerol. PssA transfers a phosphatidyl group to L-serine
    to form phosphatidylserine, and pyruvoyl-dependent Psd decarboxylates phosphatidylserine
    to phosphatidylethanolamine.
  module_outline: "- Bacterial phosphatidylethanolamine biosynthesis\n  - 1. phosphatidylserine\
    \ formation\n  - PssA-dependent phosphatidylserine formation\n    - Alternative\
    \ versions by enzyme architecture: Bacterial phosphatidylserine synthase architecture\n\
    \      - Type-I peripheral-membrane PssA\n        - Type-I PssA phosphatidylserine\
    \ synthase activity (molecular player: type-I phosphatidylserine synthase PAINT\
    \ lineage; activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase\
    \ activity)\n      - Type-II integral-membrane PssA\n        - Type-II PssA phosphatidylserine\
    \ synthase activity (molecular player: type-II phosphatidylserine synthase family;\
    \ activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)\n\
    \  - 2. phosphatidylethanolamine formation\n  - Psd-dependent phosphatidylethanolamine\
    \ formation\n    - Psd phosphatidylserine decarboxylase activity (molecular player:\
    \ phosphatidylserine decarboxylase family; activity or role: phosphatidylserine\
    \ decarboxylase activity)"
  module_connections: '- PssA-dependent phosphatidylserine formation feeds into Psd-dependent
    phosphatidylethanolamine formation: PssA supplies phosphatidylserine to Psd.'
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_phosphatidylethanolamine_biosynthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_phosphatidylethanolamine_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial phosphatidylethanolamine biosynthesis through phosphatidylserine

## Working Scope

A reusable two-reaction bacterial module for phosphatidylethanolamine biosynthesis from CDP-diacylglycerol. PssA transfers a phosphatidyl group to L-serine to form phosphatidylserine, and pyruvoyl-dependent Psd decarboxylates phosphatidylserine to phosphatidylethanolamine.

## Provisional Biological Outline

- Bacterial phosphatidylethanolamine biosynthesis
  - 1. phosphatidylserine formation
  - PssA-dependent phosphatidylserine formation
    - Alternative versions by enzyme architecture: Bacterial phosphatidylserine synthase architecture
      - Type-I peripheral-membrane PssA
        - Type-I PssA phosphatidylserine synthase activity (molecular player: type-I phosphatidylserine synthase PAINT lineage; activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)
      - Type-II integral-membrane PssA
        - Type-II PssA phosphatidylserine synthase activity (molecular player: type-II phosphatidylserine synthase family; activity or role: CDP-diacylglycerol-serine O-phosphatidyltransferase activity)
  - 2. phosphatidylethanolamine formation
  - Psd-dependent phosphatidylethanolamine formation
    - Psd phosphatidylserine decarboxylase activity (molecular player: phosphatidylserine decarboxylase family; activity or role: phosphatidylserine decarboxylase activity)

## Known Relationships Among Steps

- PssA-dependent phosphatidylserine formation feeds into Psd-dependent phosphatidylethanolamine formation: PssA supplies phosphatidylserine to Psd.

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

# Bacterial Phosphatidylethanolamine Biosynthesis Through Phosphatidylserine: A Two-Reaction Module (PssA → Psd)

*A commissioned review-style synthesis for a molecular biology audience*

---

## 1. Executive Summary

Most bacteria manufacture phosphatidylethanolamine (PE) — often the single most abundant membrane phospholipid (~70–80% in *Escherichia coli*) — through a compact, two-reaction module that branches off the central lipid intermediate CDP-diacylglycerol (CDP-DAG). In the first, committed step, **phosphatidylserine synthase (PssA)** transfers the phosphatidyl group of CDP-DAG onto L-serine, releasing CMP and producing **phosphatidylserine (PS)**. In the second step, **phosphatidylserine decarboxylase (Psd)** removes the carboxyl group of the serine headgroup to yield **PE** and CO₂. The two enzymes are functionally coupled: PssA supplies the PS substrate that Psd consumes, and in the canonical route PS is essentially a transient intermediate that does not accumulate.

The most striking feature of this system is an **asymmetry between its two halves**. The first enzyme, PssA, is not a single conserved protein but two mechanistically and structurally unrelated protein families that have *convergently* evolved to perform the same phosphatidyltransfer reaction: **Type I** peripheral/amphitropic enzymes of the phospholipase-D (PLD/HKD) superfamily (exemplified by *E. coli* PssA, which forms a covalent phosphatidyl-enzyme intermediate), and **Type II** integral-membrane enzymes of the CDP-alcohol phosphatidyltransferase (CDP-AP) superfamily (exemplified by *Bacillus subtilis* and *Sinorhizobium meliloti*). By contrast, the second enzyme, Psd, is a remarkably *uniform* and deeply conserved self-cleaving, **pyruvoyl-dependent decarboxylase** whose catalytic chemistry — autoprocessing of a proenzyme into α/β subunits followed by Schiff-base-mediated decarboxylation — is shared from bacteria to human mitochondria.

Finally, the **necessity of this module is lineage-dependent** and should not be over-generalized from *E. coli*. In *E. coli*, loss of PssA or Psd abolishes PE, imposes an absolute requirement for divalent cations, and disrupts cytokinesis. In other bacteria, PE is dispensable under some conditions (*Sinorhizobium meliloti*) or can be made by Psd-independent bypass routes (*Xanthomonas campestris* bifunctional cardiolipin/PE synthase, which condenses CDP-DAG directly with ethanolamine). This review defines the boundaries of the system, lays out the best current mechanistic model, catalogs the molecular players, and maps evolutionary and physiological variation — while being explicit about where evidence is strong and where it is indirect.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The system reviewed here is the **two-reaction bacterial PE biosynthetic module** that begins at CDP-DAG and ends at PE:

```
                PssA                         Psd
CDP-DAG + L-serine ───► phosphatidylserine ──────► phosphatidylethanolamine + CO2
        (releases CMP)        (PS)                          (PE)
```

- **Step 1 — PS formation (PssA):** a CDP-diacylglycerol–serine *O*-phosphatidyltransferase reaction (EC 2.7.8.8). CDP-DAG is the phosphatidyl donor; L-serine is the acceptor; CMP is released.
- **Step 2 — PE formation (Psd):** a phosphatidylserine decarboxylase reaction (EC 4.1.1.65). The α-carboxyl of the serine headgroup is removed, converting the serine headgroup to ethanolamine.

The upstream boundary is CDP-DAG (the shared branch-point liponucleotide feeding several phospholipid pathways). The downstream boundary is PE. PE feeds forward into further reactions (e.g., PE → phosphatidylcholine by successive methylation in some bacteria, or PE as an acyl/ethanolamine donor), but those are outside the module.

### 2.2 Neighboring processes that should be treated separately

1. **The Pcs (phosphatidylcholine synthase) route to PC.** In *Sinorhizobium meliloti* and other α-proteobacteria, choline is condensed directly with CDP-DAG to form phosphatidylcholine, entirely bypassing PS and PE ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/)). This is a parallel headgroup-transfer reaction to a *different* aminoalcohol and is not part of the PE module.
2. **Direct ethanolamine condensation (CL/PE synthase bypass).** A cardiolipin-synthase-family enzyme in *Xanthomonas campestris* (Xc_0186) condenses CDP-DAG with free ethanolamine to yield PE directly, without going through PS or Psd ([PMID: 24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/)). This achieves the same product by different chemistry and should be treated as an alternative route.
3. **The CDP-ethanolamine (Kennedy) pathway.** In many eukaryotes and some bacteria, exogenous ethanolamine is phosphorylated, activated to CDP-ethanolamine, and transferred onto diacylglycerol — same product, unrelated chemistry and enzymes.
4. **Eukaryotic, organelle-compartmentalized PSD reactions.** Yeast and animal cells run the *same* decarboxylation chemistry but distribute it across mitochondria (Psd1) and Golgi/vacuolar compartments (Psd2), and possess PS-independent routes ([PMID: 20044027](https://pubmed.ncbi.nlm.nih.gov/20044027/)). These are evolutionary descendants but involve additional trafficking and regulatory layers absent in the streamlined bacterial module.
5. **Pyruvoyl-dependent decarboxylases acting on other substrates.** The Psd catalytic scaffold has been repurposed in some organisms; e.g., in *Aspergillus oryzae* a PSD homolog functions as an **arginine decarboxylase** (ADC1) using the same pyruvoyl chemistry ([PMID: 39321488](https://pubmed.ncbi.nlm.nih.gov/39321488/)). Same mechanism, different substrate — not part of PE biosynthesis.

### 2.3 Competing definitions

The literature is largely consistent on the *reactions*, but definitions diverge on the **enzyme classification of PssA**. The "Type I / Type II" nomenclature is the most useful and best-supported framing: Type I refers to the PLD-superfamily peripheral enzymes (Gammaproteobacteria such as *E. coli*), and Type II to the CDP-AP integral-membrane enzymes (*Bacillus*, *Sinorhizobium*, and many others) ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/), [PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)). This dual-family reality means "PssA" is a *functional* label, not a single ortholog group — an important caveat for comparative genomics. A second hazard: "phosphatidylserine synthase" in mammals denotes Ca²⁺-dependent base-exchange enzymes (PSS1/PSS2) that are mechanistically unrelated to bacterial PssA and should not be conflated with it.

---

## 3. Key Findings

### F001 — Bacterial PE is made by a conserved two-enzyme module: PssA then Psd

Multiple structural and genetic studies converge on a two-reaction route from CDP-DAG: PssA condenses the phosphatidyl group with L-serine to give PS (releasing CMP); Psd then decarboxylates PS to PE. PE is a major bacterial membrane lipid. The terminal step is defined by the observation that "*Phosphatidylethanolamine (PE), a major component of the cellular membrane across all domains of life, is synthesized exclusively by membrane-anchored phosphatidylserine decarboxylase (PSD) in most bacteria*" ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/)).

The genetic logic that PssA is the committed first step is clear in *E. coli*: a *pssA* deletion strain "*lacked phosphatidylserine synthase and phosphatidylethanolamine and required divalent metal ions for growth*" ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)). The physiological importance of the endpoint is shown by the fact that PE-less cells (a *pss-93* null) "*are defective in cell division*" ([PMID: 9696776](https://pubmed.ncbi.nlm.nih.gov/9696776/)). Together these establish an obligate, ordered relay: PssA makes PS, Psd converts PS to PE, and loss of PE has severe physiological consequences in *E. coli*.

### F002 — PssA occurs as two mechanistically distinct families: Type I (PLD-superfamily) and Type II (CDP-alcohol phosphatidyltransferase)

Bacterial PS synthases split into two non-homologous architectures that arrived at the same catalytic outcome by independent evolution. **Type I** (e.g., *E. coli* PssA) is a peripheral/amphitropic membrane protein of the phospholipase-D (HKD) superfamily that catalyzes via a covalent phosphatidyl-enzyme intermediate. Crystallographic work shows that "*the membrane-bound enzyme acts on cytidine diphosphate diacylglycerol (CDP-DG) to form cytidine monophosphate and a covalent intermediate, which is subsequently targeted by serine to produce phosphatidylserine*" ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)).

**Type II** (e.g., *Bacillus subtilis*, *Sinorhizobium meliloti*) is an integral-membrane enzyme of the CDP-alcohol phosphatidyltransferase family; the *S. meliloti* enzyme "*belongs to the type II phosphatidylserine synthases*" ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/)). A functional distinction emerged from cross-complementation of an *E. coli pssA* mutant: with the membrane-bound *Bacillus* (Type II) enzyme, "*the phosphatidylethanolamine content was dependent on its activity, in contrast to that with the soluble E. coli counterpart*" ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)). The two families are a classic example of **convergent evolution of enzymatic function**: same substrates, same product, unrelated folds and mechanisms.

### F003 — Psd is a self-cleaving, pyruvoyl-dependent decarboxylase using a Schiff-base mechanism

Psd is synthesized as a proenzyme that autocatalytically cleaves at a conserved (L)GS(S/T) motif into a large **β-subunit** and a small **α-subunit**; the cleavage generates an N-terminal **pyruvoyl** prosthetic group on the α-subunit: "*The covalently attached pyruvoyl moiety is formed in a concerted reaction when the PSD proenzyme undergoes an endoproteolytic cleavage into a large β-subunit, and a smaller α-subunit, which harbors the prosthetic group at its N terminus*" ([PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)).

The self-processing is serine-protease-like: sequence analysis places PSDs in a D-H-S family, "*suggesting that PSDs belong to the D-H-S serine protease family*" ([PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)), and in *E. coli* "*E. coli PSD primarily employs D90/D142-H144-S254 to achieve auto-cleavage for the proenzyme maturation*" ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/)); PMSF (a serine-protease inhibitor) blocks processing. Once matured, "*The enzyme undergoes auto-cleavage for activation and utilizes the pyruvoyl moiety to form a Schiff base intermediate with PS to facilitate decarboxylation*" ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/)). The active *E. coli* enzyme forms a homodimer, each protomer bearing a positively charged substrate-binding pocket, with an N-terminal hydrophobic helical region mediating monotopic membrane binding and efficient PS capture — explaining broad tolerance of different PS acyl species ([PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/)).

### F004 — Alternative and bypass routes exist; the PssA/Psd module is not universally essential

PE can be produced or bypassed by non-canonical means. *Xanthomonas campestris* encodes a bifunctional cardiolipin/PE synthase (Xc_0186) that condenses CDP-DAG with ethanolamine to make PE directly, independent of PS/Psd; the authors "*consider Xc_0186 the founding member of a new class of enzymes called CL/PE synthase (CL/PEs)*" ([PMID: 24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/)). A *psd* deletion loses PE and accumulates PS, but PE synthesis is partially restored by exogenous ethanolamine via this enzyme.

In *Sinorhizobium meliloti*, "*Phosphatidylethanolamine is not essential for growth of Sinorhizobium meliloti on complex culture media*," and PC can be made without PE because "*choline is condensed with CDP-diacylglycerol to obtain PC directly*" via the Pcs route ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/)). Conversely, in *E. coli* the module is effectively required (*pssA*/*psd* nulls are PE-less, cation-dependent, and division-impaired). Essentiality is therefore lineage- and condition-dependent, not intrinsic to the module.

### F005 — The pyruvoyl-Psd step is deeply conserved bacteria→eukaryotes, while eukaryotes compartmentalize and multiply the enzymes

The self-cleaving pyruvoyl PSD mechanism is shared across prokaryotes and eukaryotes: "*PSDs play a central role in the synthesis of phosphatidylethanolamine in numerous species of prokaryotes and eukaryotes*" ([PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)), indicating an ancient conserved catalytic core. Eukaryotes retain the same chemistry but distribute it across organelles and gene copies: in *Saccharomyces cerevisiae*, PE is made by "*decarboxylation of phosphatidylserine (PS) by (i) phosphatidylserine decarboxylase 1 (Psd1p) in mitochondria and (ii) phosphatidylserine decarboxylase 2 (Psd2p) in a Golgi/vacuolar compartment*" ([PMID: 20044027](https://pubmed.ncbi.nlm.nih.gov/20044027/)), plus two PS-independent routes; deletion of *PSD1* and/or *PSD2* depletes cellular and plasma-membrane PE. Mitochondrial Psd1 is the direct descendant of the α-proteobacterial endosymbiont enzyme — a molecular fossil of the bacterial module — making streamlined bacterial Psd the best representative of the ancestral role. The upstream PS synthase, by contrast, was largely *replaced* in the animal lineage by unrelated Ca²⁺-dependent base-exchange enzymes, illustrating that the two halves of the module have very different evolutionary trajectories.

---

## 4. Mechanistic Model and Interpretation

### 4.1 Best current model of the sequence of events

1. **PssA-catalyzed phosphatidyl transfer (obligatory first step).** CDP-DAG is the activated phosphatidyl donor. In the Type I mechanism, the enzyme attacks CDP-DAG to release CMP and form a covalent phosphatidyl-enzyme intermediate; L-serine then attacks this intermediate to yield PS ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)). In the Type II mechanism (CDP-AP superfamily), catalysis proceeds within an integral-membrane active site, generally via a metal-assisted single-displacement without a stable covalent intermediate.
2. **Psd self-maturation (obligatory prerequisite for the second step).** Before Psd can act, its proenzyme must autocleave at the (L)GS(S/T) motif into β- and α-subunits, generating the N-terminal pyruvoyl group ([PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)).
3. **Psd-catalyzed decarboxylation (obligatory second step).** The pyruvoyl carbonyl forms a Schiff base with the amino group of the PS serine headgroup, providing the electron sink that drives loss of CO₂; hydrolysis of the resulting imine releases PE and regenerates the pyruvoyl group ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/), [PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/)).

### 4.2 Integrated diagram

```
                         CDP-DAG pool (central branch point)
                                   │
             ┌─────────────────────┼───────────────────────────┐
             │                     │                            │
         (PgsA→PG,             PssA STEP 1                  (Pcs → PC;
          Cls → CL)         ┌───────────────┐               Cls → CL/PE bypass)
                            │  Type I (PLD)  │  covalent phosphatidyl-enzyme
                            │   peripheral   │  intermediate + serine → PS
        CDP-DAG + L-Ser ───►│      OR        │────► phosphatidylserine (PS) + CMP
                            │Type II (CDP-AP)│  integral-membrane transfer
                            └───────────────┘
                                   │
                            PS (transient intermediate)
                                   │
                            Psd STEP 2  (monotopic homodimer)
                            ┌──────────────────────────────┐
    proenzyme ── autocleave │ D-H-S self-processing →       │
    (LGS[S/T]) ───────────► │ N-terminal PYRUVOYL on α-sub  │
                            │ pyruvoyl + PS → Schiff base   │
                            │ → decarboxylation             │
                            └──────────────────────────────┘
                                   │
                    phosphatidylethanolamine (PE) + CO2
                                   │
             ┌─────────────────────┴────────────────────────┐
   membrane bilayer stability / non-bilayer propensity   PE-specific roles
   (rescuable by CL+divalent cations or foreign glycolipid)  (e.g., LacY folding)
```

### 4.3 Obligatory, conditional, and accessory steps

| Step | Status | Basis |
|---|---|---|
| PssA phosphatidyl transfer to serine | **Obligatory** in the canonical route (only way to make PS) | *pssA* null → no PS, no PE ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)) |
| Psd proenzyme self-cleavage → pyruvoyl | **Obligatory** prerequisite for decarboxylation | Cleavage generates the catalytic prosthetic group ([PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)) |
| Psd Schiff-base decarboxylation | **Obligatory** terminal step | Structures show pyruvoyl–PS imine ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/)) |
| Divalent-cation supplementation | **Conditional** (only in PE-less mutants) | Rescues viability of PE-deficient *E. coli* ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/), [PMID: 7961817](https://pubmed.ncbi.nlm.nih.gov/7961817/)) |
| Type I PssA membrane association | **Conditional** (regulatory, links activity to membrane) | Amphitropic cytosol⇌membrane equilibrium ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/)) |
| Direct ethanolamine condensation (CL/PE synthase) | **Accessory / bypass** (lineage-specific) | Restores PE in *psd* mutants of *Xanthomonas* ([PMID: 24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/)) |

---

## 5. Major Molecular Players and Active Assemblies

| Player | Reaction | Family / fold | Membrane topology | Key mechanistic feature | Representative refs |
|---|---|---|---|---|---|
| **PssA — Type I** | CDP-DAG + serine → PS + CMP | Phospholipase-D (HKD) superfamily | Peripheral / amphitropic (cytosol ⇌ membrane) | Covalent phosphatidyl-enzyme intermediate; His nucleophile | *E. coli* ([PMID: 39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/), [PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)) |
| **PssA — Type II** | CDP-DAG + serine → PS + CMP | CDP-alcohol phosphatidyltransferase (CAPT) | Polytopic integral membrane | Metal-dependent direct transfer, no covalent intermediate | *B. subtilis*, *S. meliloti* ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/), [PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)) |
| **Psd** | PS → PE + CO₂ | Pyruvoyl-dependent decarboxylase; D-H-S self-processing | Monotopic (N-terminal amphipathic helices) | Autocleaved α/β heterodimer; N-terminal pyruvoyl; Schiff base | *E. coli* ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/), [PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/), [PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)) |
| **CL/PE synthase (Xc_0186)** *(bypass)* | CDP-DAG + ethanolamine → PE (and CDP-DAG + PG → CL) | Cardiolipin synthase (PLD) family | Integral membrane | Psd-independent direct PE synthesis | *X. campestris* ([PMID: 24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/)) |

**Assembly notes.** Neither core enzyme requires a large protein complex. PssA acts as a monomer whose activity is gated by reversible membrane binding (Type I) or by constitutive membrane insertion plus divalent metal (Type II). Mature Psd is an **α/β heterodimer** (products of one gene) that functions as a homodimer of such heterodimers at the membrane surface ([PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/)). The functional "assembly" that matters most is enzyme-plus-membrane: both steps are interfacial reactions on lipid substrates embedded in the bilayer.

---

## 6. Evolutionary and Cell-Biological Variation

**Across bacterial lineages.** PssA architecture is the major axis of variation: γ-Proteobacteria such as *E. coli* use the peripheral Type I (PLD-superfamily) enzyme; many Firmicutes and α-proteobacteria use the integral-membrane Type II (CAPT) enzyme — both accomplishing identical chemistry (convergence). Psd architecture is comparatively uniform across bacteria (a single monotopic pyruvoyl enzyme), making it the more conserved half of the module. Bypass capacity also varies — *Xanthomonas* carries a CL/PE synthase that makes PE from ethanolamine independently of Psd ([PMID: 24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/)) — as does downstream tailoring (PE→PC methylation, or direct Pcs synthesis of PC; [PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/)).

**Across domains — eukaryotic compartmentalization.** The decarboxylation chemistry is deeply conserved into eukaryotes, but enzyme count and localization expand. In *S. cerevisiae*, PE is made by mitochondrial Psd1p and Golgi/vacuolar Psd2p (plus two PS-independent routes); deleting *PSD1*/*PSD2* depletes cellular and plasma-membrane PE ([PMID: 20044027](https://pubmed.ncbi.nlm.nih.gov/20044027/)). Mitochondrial Psd1 is the direct descendant of the bacterial endosymbiont enzyme and the best representative of the ancestral role, whereas the upstream PS synthase was largely replaced in animals by Ca²⁺-dependent base-exchange enzymes.

**Physiological states.** Because Type I PssA is amphitropic and branch-point fluxes are co-regulated, the PE:anionic-lipid ratio can be tuned to growth conditions ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)). PE is enriched at specific membrane locales (division septum, cell poles) and, with cardiolipin, forms lateral microdomains implicated in division and protein localization ([PMID: 16925550](https://pubmed.ncbi.nlm.nih.gov/16925550/), [PMID: 9696776](https://pubmed.ncbi.nlm.nih.gov/9696776/)).

---

## 7. Constraints, Dependencies, and Failure Modes

**Ordering constraints.**
1. CDP-DAG must be made before either branch proceeds; PssA and PgsA compete for it.
2. **PssA before Psd:** Psd's only substrate in this module is PS; a *pssA* null therefore also abolishes PE ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/)).
3. **Psd self-processing before catalysis:** the pyruvoyl cofactor exists only after autocleavage, so maturation strictly precedes turnover; mutations in D90/D142-H144-S254 that block cleavage abolish activity ([PMID: 33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/), [PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)).

**Compartment/substrate specificity.** Both steps are interfacial and act on bilayer-embedded substrates; enzymes must reach the membrane (PssA by reversible binding; Psd by its amphipathic N-terminus). Psd's hydrophobic acyl-chain groove makes it tolerant of diverse PS species but committed to PS headgroup geometry ([PMID: 32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/)).

**Failure modes.**
- **Loss of PE (pssA or psd null):** in *E. coli*, PE-deficient cells survive only with high divalent-cation supplementation, show increased permeability, and are defective in cytokinesis ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/), [PMID: 7961817](https://pubmed.ncbi.nlm.nih.gov/7961817/), [PMID: 9696776](https://pubmed.ncbi.nlm.nih.gov/9696776/)). This reflects PE's role as a non-bilayer-prone, hydrogen-bonding lipid: the neutral, NB-prone glycolipid MGlcDAG can substitute for many PE functions ([PMID: 14688287](https://pubmed.ncbi.nlm.nih.gov/14688287/)), and PE acts as a lipid "chaperone" for folding of polytopic proteins such as lactose permease ([PMID: 10212204](https://pubmed.ncbi.nlm.nih.gov/10212204/)).
- **Conditional dispensability:** in *S. meliloti*, PE is not essential on complex media, and PC can be supplied by the PE-independent Pcs route ([PMID: 14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/)) — essentiality is not intrinsic to the module.

**Evidence that rules out alternative paths.** Genetic epistasis (a *pssA* null being PE-less; *psd* nulls accumulating PS) demonstrates that, in canonical bacteria, PE flows *only* through PS unless a dedicated bypass enzyme is present ([PMID: 8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/), [PMID: 24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/)). The requirement for a pre-formed pyruvoyl cofactor rules out a PLP-based route for Psd ([PMID: 25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/)). Separately, PE is *not* required for lipoprotein N-acylation in *E. coli* — other phospholipids can serve as the acyl donor ([PMID: 2033085](https://pubmed.ncbi.nlm.nih.gov/2033085/)) — ruling out one long-postulated obligatory PE role.

---

## 8. Evidence Base

| PMID | Title (abbrev.) | Role in this review |
|---|---|---|
| [8824831](https://pubmed.ncbi.nlm.nih.gov/8824831/) | Regulatory mechanism for balanced phospholipid synthesis in *E. coli* | PssA is committed step; *pssA* null → no PE, cation-dependent; Type I vs Type II behavior contrast (F001, F002, F004) |
| [39693441](https://pubmed.ncbi.nlm.nih.gov/39693441/) | Structural basis for membrane association and catalysis by PS synthase | Type I covalent phosphatidyl-enzyme mechanism (F002) |
| [14996797](https://pubmed.ncbi.nlm.nih.gov/14996797/) | PE not essential in *Sinorhizobium meliloti* | Type II assignment; PE dispensability; Pcs route (F002, F004) |
| [25724650](https://pubmed.ncbi.nlm.nih.gov/25724650/) | Protease to decarboxylase: PSD metamorphosis | Proenzyme self-cleavage; pyruvoyl; D-H-S family; broad conservation (F003, F005) |
| [33707636](https://pubmed.ncbi.nlm.nih.gov/33707636/) | Structural insights into PE formation in bacterial membranes | Auto-cleavage, Schiff base, catalytic residues, membrane binding (F001, F003) |
| [32402247](https://pubmed.ncbi.nlm.nih.gov/32402247/) | Structural basis for PE biosynthesis by bacterial PSD | EcPsd homodimer, substrate pocket, N-terminal helix (F003) |
| [9696776](https://pubmed.ncbi.nlm.nih.gov/9696776/) | Cell division proteins in PE-lacking filamentous *E. coli* | PE-less cells defective in division (F001) |
| [7961817](https://pubmed.ncbi.nlm.nih.gov/7961817/) | Lipid polymorphism essential for PE-deficient *E. coli* viability | Cation/CL rescue via lipid polymorphism (§7) |
| [24707916](https://pubmed.ncbi.nlm.nih.gov/24707916/) | Bifunctional cardiolipin/PE synthase | Psd-independent PE bypass from CDP-DAG + ethanolamine (F004) |
| [20044027](https://pubmed.ncbi.nlm.nih.gov/20044027/) | PE from four pathways to yeast plasma membrane | Eukaryotic Psd1/Psd2 compartmentalization (F005) |
| [14688287](https://pubmed.ncbi.nlm.nih.gov/14688287/) | Monoglucosyldiacylglycerol substitutes for PE | Foreign non-bilayer lipid rescues PE loss (§7) |
| [10212204](https://pubmed.ncbi.nlm.nih.gov/10212204/) | PE as molecular chaperone for LacY refolding | Evidence for PE-specific functional roles (§7, §9) |
| [2033085](https://pubmed.ncbi.nlm.nih.gov/2033085/) | PE not essential for lipoprotein N-acylation | Rules out one obligatory PE role (§7) |
| [39321488](https://pubmed.ncbi.nlm.nih.gov/39321488/) | Arginine decarboxylase (PSD homolog) in *A. oryzae* | Pyruvoyl scaffold repurposed to non-PE substrate (§2, §9) |
| [16925550](https://pubmed.ncbi.nlm.nih.gov/16925550/) | Lipid domains in bacterial membranes | Context: PE/CL microdomains and synthase localization (§6) |

---

## 9. Controversies and Open Questions

**Strongly supported (high confidence):**
- The two-reaction route CDP-DAG → PS (PssA) → PE (Psd) is the canonical bacterial PE pathway (F001).
- PssA exists as two convergent families, Type I (PLD-superfamily) and Type II (CDP-AP) (F002).
- Psd is a self-cleaving pyruvoyl decarboxylase using serine-protease-like D-H-S autoprocessing and Schiff-base decarboxylation (F003; strong structural evidence).

**Areas of disagreement, indirect evidence, or organism mixing:**
1. **Generalizing essentiality from *E. coli*.** Much of the "PE is essential" narrative rests on *E. coli*; yet PE is dispensable in *Sinorhizobium* on rich media and bypassable in *Xanthomonas*. Claims of universal essentiality should be qualified.
2. **Mechanistic detail of Type II PssA.** The covalent-intermediate mechanism is well established for Type I (*E. coli*), but catalytic details of the integral-membrane Type II enzymes are comparatively under-characterized structurally; most CAPT mechanistic inference is transferred by homology. Extrapolating a single mechanism across both families is unsafe.
3. **Cross-organism structural inference for Psd.** The Schiff-base/pyruvoyl model is robust, but studies mix data from *E. coli*, *Plasmodium*, yeast, and fungal homologs — some repurposed to *non-PE* substrates such as arginine ([PMID: 39321488](https://pubmed.ncbi.nlm.nih.gov/39321488/)). Care is needed not to assume identical substrate handling across all "PSD-family" proteins.
4. **What makes PE (or its physical properties) essential?** Rescue by cardiolipin+cations or a foreign glycolipid ([PMID: 7961817](https://pubmed.ncbi.nlm.nih.gov/7961817/), [PMID: 14688287](https://pubmed.ncbi.nlm.nih.gov/14688287/)) suggests it is largely the non-bilayer/charge property, but specific chaperone-like roles of PE ([PMID: 10212204](https://pubmed.ncbi.nlm.nih.gov/10212204/)) argue for additional PE-specific functions. The balance remains unresolved.
5. **In-vivo regulation of Type I PssA membrane association.** The amphitropic cytosol⇌membrane equilibrium is documented biochemically and structurally, but the physiological triggers and their quantitative contribution to flux control are incompletely resolved.
6. **Druggability.** PSD's unusual pyruvoyl chemistry and self-processing are attractive, mechanism-unique antimicrobial targets, but selectivity over the conserved human mitochondrial Psd1 is an unresolved practical concern.

**Most important open questions:** the phylogenetic distribution and relative antiquity of Type I vs. Type II PssA; high-resolution structures/mechanisms of Type II PssA; how flux is partitioned at CDP-DAG among PE, PG/CL, and PC branches; and how broadly distributed the Psd-independent bypass routes are.

---

## 10. Limitations and Knowledge Gaps

1. **Literature synthesis, not primary data.** This review synthesizes published literature (24 papers reviewed) rather than new experiments; conclusions inherit the biases of the source studies.
2. **E. coli-centric mechanistic depth.** High-resolution structural/mechanistic detail is concentrated on *E. coli* Type I PssA and *E. coli* Psd. Type II PssA mechanisms are comparatively under-resolved.
3. **Uneven phylogenetic sampling.** The prevalence of Type I vs. Type II PssA across bacterial phyla, and of Psd-independent bypass enzymes, has not been systematically quantified here.
4. **Function attribution.** Distinguishing PE's generic biophysical roles from its specific molecular-ligand roles remains partly unresolved and is confounded by rescue experiments with surrogate lipids.
5. **Cross-kingdom extrapolation.** Some cited mechanistic support comes from eukaryotic or repurposed (non-PE) homologs; care was taken to flag these, but residual extrapolation risk remains.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Comparative genomics survey.** Systematically classify PssA homologs (Type I PLD-superfamily vs. Type II CDP-AP) across sequenced bacterial phyla, and co-map Psd and Cls-family CL/PE-synthase presence to quantify how often bypass routes coexist.
2. **High-resolution structure of a Type II PssA.** Solve a cryo-EM/crystal structure of an integral-membrane Type II PS synthase (e.g., *Bacillus* or *Sinorhizobium*) with substrate/product to test whether it uses a covalent intermediate or a metal-assisted direct transfer.
3. **Quantify flux partitioning at CDP-DAG.** Use isotope tracing/lipidomics in *E. coli* and a Type-II-using organism to measure how carbon is split between PE, PG/CL, and PC branches under varied conditions.
4. **Dissect Psd maturation kinetics.** Time-resolved assays (and PMSF titration) to separate self-cleavage from decarboxylation rates and test whether maturation is rate-limiting in vivo.
5. **Test bypass generality.** Screen genomes flagged for Cls-family enzymes and experimentally test whether *psd* deletions are rescuable by exogenous ethanolamine beyond *Xanthomonas*.
6. **Separate physical vs. specific PE roles.** Systematic complementation of PE-less *E. coli* with a graded panel of non-bilayer surrogate lipids while assaying specific PE-dependent functions (e.g., LacY folding, division) to define which phenotypes require PE per se.

---

*Uncertainty statement:* Structural mechanism is strongest for the *E. coli* Type I PssA and *E. coli* Psd. Type II PssA mechanism, in-vivo regulation of PssA membrane association, and the precise self-cleavage trajectory of Psd remain partly inferential. Essentiality and downstream tailoring vary by lineage and growth condition and should not be generalized from *E. coli*.


## Artifacts

- [OpenScientist final report](bacterial_phosphatidylethanolamine_biosynthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_phosphatidylethanolamine_biosynthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:14996797
2. PMID:24707916
3. PMID:20044027
4. PMID:39321488
5. PMID:39693441
6. PMID:33707636
7. PMID:8824831
8. PMID:9696776
9. PMID:25724650
10. PMID:32402247
11. PMID:7961817
12. PMID:16925550
13. PMID:14688287
14. PMID:10212204
15. PMID:2033085