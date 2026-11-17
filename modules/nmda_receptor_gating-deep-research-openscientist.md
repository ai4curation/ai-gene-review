---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-10T15:24:50.589781'
end_time: '2026-11-10T15:38:07.270750'
duration_seconds: 796.68
template_file: templates/module_research.md.j2
template_variables:
  module_title: Human NMDA receptor family channel gating by GluN1 and its partner
    subunits
  module_summary: How the heterotetrameric receptors built on the GluN1 subunit are
    opened. Every receptor of this family contains two GluN1 subunits, which bind
    the co-agonist glycine or D-serine, and two partner subunits. With GluN2 partners
    (GluN2A to GluN2D) the partner binds glutamate, and the channel opens only when
    both ligands are bound; the open pore conducts sodium, potassium and calcium and
    is blocked by magnesium at resting potential, so current also requires depolarisation.
    With GluN3 partners (GluN3A or GluN3B) both subunit types bind glycine, glutamate
    is not needed, and the channel has low calcium permeability and no magnesium block.
    The module covers ligand sensing by each subunit and conduction by the assembled
    tetramer. Receptor assembly and trafficking, synaptic anchoring by PSD-95 family
    scaffolds, allosteric modulation, and signalling downstream of calcium entry are
    outside it.
  module_outline: "- NMDA receptor family channel gating\n  - 1. co-agonist sensing\
    \ by the obligatory GluN1 subunit\n  - GluN1 binding of glycine or D-serine\n\
    \    - GRIN1 glycine site (molecular player: GRIN1; activity or role: glycine\
    \ binding)\n  - 2. agonist sensing by the partner subunit\n  - Agonist binding\
    \ by the GluN2 or GluN3 partner subunit\n    - Alternative versions by subunit\
    \ composition: Partner subunit\n      - GRIN2A glutamate sensing\n        - GRIN2A\
    \ glutamate site (molecular player: GRIN2A; activity or role: glutamate binding)\n\
    \      - GRIN2B glutamate sensing\n        - GRIN2B glutamate site (molecular\
    \ player: GRIN2B; activity or role: glutamate binding)\n      - GRIN2C glutamate\
    \ sensing\n        - GRIN2C glutamate site (molecular player: GRIN2C; activity\
    \ or role: glutamate binding)\n      - GRIN2D glutamate sensing\n        - GRIN2D\
    \ glutamate site (molecular player: GRIN2D; activity or role: glutamate binding)\n\
    \      - GRIN3A glycine sensing\n        - GRIN3A glycine site (molecular player:\
    \ GRIN3A; activity or role: glycine binding)\n      - GRIN3B glycine sensing\n\
    \        - GRIN3B glycine site (molecular player: GRIN3B; activity or role: glycine\
    \ binding)\n  - 3. cation conduction by the assembled tetramer\n  - Ligand-gated\
    \ cation conduction\n    - Alternative versions by partner subunit class: Receptor\
    \ class\n      - GluN1/GluN2 NMDA receptor\n        - Glutamate- and glycine-gated,\
    \ calcium-permeable channel (molecular player: NMDA selective glutamate receptor\
    \ complex; activity or role: NMDA glutamate receptor activity)\n      - GluN1/GluN3\
    \ glycine-gated receptor\n        - Glycine-gated cation channel (molecular player:\
    \ neurotransmitter receptor complex; activity or role: glycine-gated cation channel\
    \ activity)"
  module_connections: '- GluN1 binding of glycine or D-serine promotes Ligand-gated
    cation conduction: Co-agonist binding to GluN1 is required for the channel to
    open. Corresponds to the GRIN1 "directly positively regulates" edge in each GO-CAM
    model.

    - Agonist binding by the GluN2 or GluN3 partner subunit promotes Ligand-gated
    cation conduction: Glutamate binding to GluN2, or glycine binding to GluN3, is
    required for the channel to open. Corresponds to the partner-subunit edge in each
    GO-CAM model.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: nmda_receptor_gating-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nmda_receptor_gating-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Human NMDA receptor family channel gating by GluN1 and its partner subunits

## Working Scope

How the heterotetrameric receptors built on the GluN1 subunit are opened. Every receptor of this family contains two GluN1 subunits, which bind the co-agonist glycine or D-serine, and two partner subunits. With GluN2 partners (GluN2A to GluN2D) the partner binds glutamate, and the channel opens only when both ligands are bound; the open pore conducts sodium, potassium and calcium and is blocked by magnesium at resting potential, so current also requires depolarisation. With GluN3 partners (GluN3A or GluN3B) both subunit types bind glycine, glutamate is not needed, and the channel has low calcium permeability and no magnesium block. The module covers ligand sensing by each subunit and conduction by the assembled tetramer. Receptor assembly and trafficking, synaptic anchoring by PSD-95 family scaffolds, allosteric modulation, and signalling downstream of calcium entry are outside it.

## Provisional Biological Outline

- NMDA receptor family channel gating
  - 1. co-agonist sensing by the obligatory GluN1 subunit
  - GluN1 binding of glycine or D-serine
    - GRIN1 glycine site (molecular player: GRIN1; activity or role: glycine binding)
  - 2. agonist sensing by the partner subunit
  - Agonist binding by the GluN2 or GluN3 partner subunit
    - Alternative versions by subunit composition: Partner subunit
      - GRIN2A glutamate sensing
        - GRIN2A glutamate site (molecular player: GRIN2A; activity or role: glutamate binding)
      - GRIN2B glutamate sensing
        - GRIN2B glutamate site (molecular player: GRIN2B; activity or role: glutamate binding)
      - GRIN2C glutamate sensing
        - GRIN2C glutamate site (molecular player: GRIN2C; activity or role: glutamate binding)
      - GRIN2D glutamate sensing
        - GRIN2D glutamate site (molecular player: GRIN2D; activity or role: glutamate binding)
      - GRIN3A glycine sensing
        - GRIN3A glycine site (molecular player: GRIN3A; activity or role: glycine binding)
      - GRIN3B glycine sensing
        - GRIN3B glycine site (molecular player: GRIN3B; activity or role: glycine binding)
  - 3. cation conduction by the assembled tetramer
  - Ligand-gated cation conduction
    - Alternative versions by partner subunit class: Receptor class
      - GluN1/GluN2 NMDA receptor
        - Glutamate- and glycine-gated, calcium-permeable channel (molecular player: NMDA selective glutamate receptor complex; activity or role: NMDA glutamate receptor activity)
      - GluN1/GluN3 glycine-gated receptor
        - Glycine-gated cation channel (molecular player: neurotransmitter receptor complex; activity or role: glycine-gated cation channel activity)

## Known Relationships Among Steps

- GluN1 binding of glycine or D-serine promotes Ligand-gated cation conduction: Co-agonist binding to GluN1 is required for the channel to open. Corresponds to the GRIN1 "directly positively regulates" edge in each GO-CAM model.
- Agonist binding by the GluN2 or GluN3 partner subunit promotes Ligand-gated cation conduction: Glutamate binding to GluN2, or glycine binding to GluN3, is required for the channel to open. Corresponds to the partner-subunit edge in each GO-CAM model.

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

# Human NMDA Receptor Family Channel Gating by GluN1 and Its Partner Subunits

*A commissioned review-style synthesis*

---

## 1. Executive Summary

The NMDA receptor (NMDAR) family comprises a set of GluN1-containing heterotetrameric cation channels that convert the coincident binding of extracellular small-molecule agonists into the opening of a central ion-conducting pore. Every receptor in this family is built on an invariant scaffold of **two obligatory GluN1 subunits plus two partner subunits**. The identity of the partner — one of four GluN2 subunits (GluN2A–D) or one of two GluN3 subunits (GluN3A–B) — sets the ligand logic and the biophysical personality of the channel, yet the underlying gating machine is strikingly conserved across the family. This review treats that machine as a biological system: its boundaries, its core transduction mechanism, its subunit-dependent variants, its deep evolutionary origin, and the points where the evidence is strong, indirect, or contested.

The best-supported mechanistic model is a **mechanical, ligand-to-pore transduction cascade**. Each agonist binds inside a bilobed, clamshell-like ligand-binding domain (LBD); agonist binding closes the clamshell; clamshell closure loads the short linkers that connect the LBD to the pore-lining M3 transmembrane helix with mechanical tension; and that tension splays open the M3 gate. Cryo-EM structures captured in distinct ligand states show that this tension — transmitted chiefly through the GluN2 LBD–TMD linkers — is the proximate control variable for gating, and that competitive antagonists at either subunit shut the channel by relaxing it (F001). In GluN1/GluN2 receptors the system behaves as an obligatory **two-input AND gate**: glycine or D-serine must occupy the GluN1 site *and* glutamate must occupy the GluN2 site (F006). The open GluN1/GluN2 pore conducts Na⁺, K⁺ and Ca²⁺ but is blocked at resting potential by a rapid, voltage-dependent Mg²⁺ block, so current additionally requires postsynaptic depolarization — making the receptor a molecular **Hebbian coincidence detector** (F004). The GluN1/GluN3 branch of the family uses the same gating mechanics but a different ligand logic: both subunit types bind glycine, glutamate is dispensable, Ca²⁺ permeability is low, and there is no Mg²⁺ block; paradoxically glycine at the low-affinity GluN1 site auto-inhibits rather than activates (F002).

Two further conclusions frame the system. First, the conducting pore is **evolutionarily ancient**: the iGluR pore module is an inverted potassium-channel selectivity filter, placing the deepest origin of NMDAR conduction in a prokaryotic lineage, with the accessory M4 helix and obligatory heteromerization emerging as later eukaryotic elaborations (F003). Second, the entire sevenfold subunit repertoire assembles into di- and tri-heteromers whose gating is quantitatively tuned around this one shared mechanism; human disease variants cluster near the ligand-sensing sites, confirming those sites as the obligatory control points of gating (F005). The scope of this review is deliberately restricted to **ligand sensing and conduction**; assembly/trafficking, PSD-95 anchoring, NTD allosteric modulation, and downstream Ca²⁺ signalling are treated as neighboring systems.

---

## 2. Definition and Biological Boundaries

### What is included

The system under review is the **ligand-gated opening and ion conduction of GluN1-based heterotetrameric receptors**. Concretely, it spans three linked steps:

1. **Co-agonist sensing by the obligatory GluN1 subunit** — binding of glycine or D-serine to the GluN1 LBD.
2. **Agonist sensing by the partner subunit** — glutamate binding to a GluN2 subunit, or glycine binding to a GluN3 subunit.
3. **Cation conduction by the assembled tetramer** — the mechanical opening of the M3 gate and the resulting flux of cations through the pore.

Each receptor contains exactly two GluN1 subunits and two partners arranged as a dimer-of-dimers around a central pore. GluN1 is obligatory and non-interchangeable; it is the subunit that reads the co-agonist. The partner subunit supplies the second required input and sets the receptor's biophysical class.

### What is adjacent but excluded

Several neighboring processes are frequently discussed alongside NMDAR gating but are mechanistically separable and are **outside this scope**:

- **Receptor assembly and trafficking** — ER biogenesis, subunit stoichiometry control, and cell-surface delivery of di- vs. tri-heteromers (e.g., [PMID: 38727903](https://pubmed.ncbi.nlm.nih.gov/38727903/)). These determine *which* receptors exist at the membrane, not *how* an assembled receptor opens.
- **Synaptic anchoring by PSD-95-family scaffolds** — positioning and clustering of receptors.
- **N-terminal-domain (NTD) allosteric modulation** — zinc, ifenprodil, protons, polyamines, and GluN2C/2D-selective positive allosteric modulators (e.g., [PMID: 36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/), [PMID: 21504727](https://pubmed.ncbi.nlm.nih.gov/21504727/)). These tune open probability but are not the obligatory gating inputs; they are accessory.
- **Downstream Ca²⁺ signalling** — CaMKII activation, LTP/LTD induction, and excitotoxicity. These are *consequences* of conduction, not part of gating.

A note on a common confusion: NMDARs are one of several iGluR classes (AMPA, kainate, delta). AMPA receptors share the overall architecture and the pore-opening logic but differ fundamentally in ligand logic (single agonist, no co-agonist requirement) and in auxiliary-subunit biology (TARPs; [PMID: 42286176](https://pubmed.ncbi.nlm.nih.gov/42286176/)). AMPAR gating should not be imported wholesale as a model for NMDAR gating, even though the mechanical principle is shared.

### Competing definitions

The main definitional tension in the literature concerns whether **GluN1/GluN3 "glycine receptors"** should be grouped with "NMDA receptors" at all. They are NMDAR-*family* members by sequence and architecture, but functionally they are glutamate-independent, excitatory glycine-gated channels with properties "strikingly different" from GluN1/GluN2 receptors ([PMID: 32389749](https://pubmed.ncbi.nlm.nih.gov/32389749/)). This review follows the inclusive, architecture-based definition — all GluN1-containing heterotetramers — while making the functional divergence explicit.

---

## 3. Mechanistic Overview

### The core transduction cascade

The central mechanistic claim, supported by multiple cryo-EM structures solved in distinct ligand states at ≤4 Å, is that NMDAR gating is a **mechanical process driven by agonist-induced linker tension** (F001). The sequence of events is:

```
  Agonist binds          Clamshell             Linker tension          M3 gate
  inside bilobed   ──►    (LBD lobes)    ──►    loaded on LBD–    ──►   splays
  LBD cleft              close around          M3 linkers,            open; pore
  (glycine@GluN1,        ligand                chiefly GluN2          conducts
   glutamate@GluN2)                                                   cations
```

Chou et al. (2020) showed directly that "activation and competitive inhibition by both GluN1 and GluN2 antagonists occur by controlling the tension of the linker between the ligand-binding domain and the transmembrane ion channel of the GluN2 subunit" ([PMID: 32610085](https://pubmed.ncbi.nlm.nih.gov/32610085/)). Competitive antagonists at either the GluN1 (glycine-site) or GluN2 (glutamate-site) cleft prevent clamshell closure, relax the linkers, and keep the gate shut. Kang et al. (2025) extended this to a tri-heteromeric GluN1/2B/2D receptor, reporting "ligand-dependent conformational dynamics that modulate the tension between the extracellular domain and transmembrane channels, governing channel gating and blockade" ([PMID: 39954679](https://pubmed.ncbi.nlm.nih.gov/39954679/)). The convergence of these independent structural studies on the **linker-tension model** makes it the best-supported mechanistic framework.

### Obligatory, conditional, and accessory steps

| Step | Status in GluN1/GluN2 | Status in GluN1/GluN3 |
|---|---|---|
| Co-agonist binding to GluN1 | **Obligatory** (glycine or D-serine) | Required, but **auto-inhibitory** at the low-affinity GluN1 site |
| Agonist binding to partner | **Obligatory** (glutamate @ GluN2) | Glycine @ GluN3 is the **activating** input; glutamate not needed |
| LBD clamshell closure → linker tension | **Obligatory**, shared mechanism | **Obligatory**, shared mechanism |
| M3 gate opening | **Obligatory** | **Obligatory** |
| Depolarization to relieve Mg²⁺ block | **Conditional** (required for current, not for opening) | Not applicable (no Mg²⁺ block) |
| NTD allosteric modulation (Zn²⁺, protons, PAMs) | **Accessory** (tunes P_open) | **Accessory** (GluN3A NTD sets efficacy) |

The crucial distinction for GluN1/GluN2 receptors is between **gate opening** and **current flow**. Both agonists are obligatory for the gate to open (the AND gate). But even with an open gate, at resting membrane potential external Mg²⁺ occludes the pore; current therefore additionally requires depolarization. This is a conditional, voltage-dependent requirement layered on top of the obligatory ligand requirement (F004).

### The GluN1/GluN2 AND gate at the level of endogenous physiology

The dual-ligand requirement is not merely a recombinant-expression artifact. In native synaptic plasticity, NMDAR activation "requires the binding of glutamate but also the presence of the co-agonist D-serine at the glycine site" ([PMID: 25740810](https://pubmed.ncbi.nlm.nih.gov/25740810/)). The physiological co-agonist D-serine is synthesized by serine racemase, and bidirectional manipulation of D-serine levels bidirectionally alters NMDAR function and plasticity (F006; [PMID: 28598327](https://pubmed.ncbi.nlm.nih.gov/28598327/)). This confirms the AND gate operates in vivo, under the control of endogenous co-agonist supply.

### The GluN1/GluN3 inverted logic

GluN1/GluN3 receptors reveal how much of the family's diversity comes from re-wiring the *inputs* to a conserved machine. Here both subunit types bind glycine, and "unlike 'conventional' GluN1-N2 receptors, which require both glycine and glutamate for activation, GluN1-N3 receptors are activated solely by glycine" ([PMID: 40235311](https://pubmed.ncbi.nlm.nih.gov/40235311/)). The counterintuitive twist is that glycine occupancy of the two different glycine sites has opposite effects: "Binding of glycine to the high-affinity GluN3 subunits triggers channel opening, whereas glycine binding to the low-affinity GluN1 subunits causes an auto-inhibition of the maximal glycine-inducible receptor current" ([PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/)). Because GluN1 occupancy inhibits, GluN1 competitive antagonists *potentiate* GluN1/GluN3 currents — the inverse of their effect on GluN1/GluN2 receptors. The GluN3A N-terminal domain sets the efficacy of the response ([PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/)).

---

## 4. Major Molecular Players and Active Assemblies

### Subunit repertoire

| Gene | Subunit | Ligand bound | Role in gating |
|---|---|---|---|
| GRIN1 | GluN1 | Glycine / D-serine | Obligatory co-agonist sensor (all receptors) |
| GRIN2A | GluN2A | Glutamate | Partner; fast kinetics, high P_open |
| GRIN2B | GluN2B | Glutamate | Partner; slow kinetics, developmentally early |
| GRIN2C | GluN2C | Glutamate | Partner; distinct inter-subunit arrangement |
| GRIN2D | GluN2D | Glutamate | Partner; intrinsically closed NTD, low P_open |
| GRIN3A | GluN3A | Glycine | Partner; glutamate-independent, NTD sets efficacy |
| GRIN3B | GluN3B | Glycine | Partner; glutamate-independent |

### Domain architecture of a gating subunit

Each subunit contributes four modular regions arranged vertically:

```
   NTD  (N-terminal domain)      ── allosteric layer (accessory)
    │
   LBD  (ligand-binding domain)  ── bilobed clamshell; binds agonist
    │   (S1–S2 segments)
   LBD–M3 linker                 ── tension-transmitting element (the key lever)
    │
   M1 – M2 re-entrant loop – M3  ── pore module (inverted K⁺-channel unit)
    │   M3 = gate; M2 = selectivity/Mg²⁺ block
   M4  (accessory TM helix)      ── later eukaryotic elaboration
```

### The pore module and its selectivity determinants

The conducting pore is formed by the **M1 / M2 re-entrant loop / M3** segments of all four subunits. The M3 helices form the gate; the M2 re-entrant loop forms the selectivity filter and the Mg²⁺-block site. The molecular determinants of both Ca²⁺ permeability and voltage-dependent Mg²⁺ block reside in the M2 loop — specifically the **"N-site" asparagine** (the Q/R/N site) contributed by GluN2 — and have now been resolved structurally (F004; [PMID: 42086762](https://pubmed.ncbi.nlm.nih.gov/42086762/)). GluN1/GluN3 receptors lack this pore signature in the functionally relevant configuration, which explains their low Ca²⁺ permeability and absence of Mg²⁺ block.

### Di- and tri-heteromeric assemblies

The seven subunits assemble into **di-heteromers** (e.g., GluN1/2A, GluN1/2B) and **tri-heteromers** (e.g., GluN1/2A/2B, GluN1/2B/2D). Tri-heteromers are abundant in the adult brain and display gating properties intermediate between their parent di-heteromers: "Triheteromeric GluN1/2B/2D receptors have functional properties intermediate to those of diheteromeric GluN1/2B and GluN1/2D receptors" ([PMID: 31541561](https://pubmed.ncbi.nlm.nih.gov/31541561/)). This intermediacy is itself evidence that subunit identity tunes a single shared mechanism rather than switching between different mechanisms (F005).

---

## 5. Evolutionary and Cell-Biological Variation

### Deep evolutionary origin of the pore

The most striking conservation result is that the iGluR pore is derived from a **potassium channel**, but inverted in the membrane. Janovjak et al. (2011) identified "an ionotropic glutamate receptor that combines the typical eukaryotic domain architecture with the 'TXVGYG' signature sequence of the selectivity filter found in K⁺ channels," with functional properties intermediate between bacterial and eukaryotic glutamate-gated channels ([PMID: 21407198](https://pubmed.ncbi.nlm.nih.gov/21407198/)). This places the deepest plausible origin of NMDAR conduction in a **prokaryotic lineage** (F003).

Langer et al. (2021) further resolved the layering of ancient vs. derived parts: "the architecture of all eukaryotic iGluRs derives from a common prokaryotic ancestral receptor that lacks M4 and consists only of transmembrane segments M1 and M3" ([PMID: 34658899](https://pubmed.ncbi.nlm.nih.gov/34658899/)). The implications for "which parts are ancient":

| Component | Evolutionary status |
|---|---|
| M1 / M2 / M3 pore module | **Ancient** — inverted K⁺-channel core, prokaryotic |
| M2 N-site (Ca²⁺/Mg²⁺ determinants) | Ancient pore element, specialized in eukaryotes |
| M4 accessory TM helix | **Later eukaryotic elaboration** (absent in prokaryotic iGluR) |
| Obligatory GluN1 heteromerization | **Later eukaryotic elaboration** |
| NTD allosteric layer | Eukaryotic elaboration (tuning, not core gating) |

For understanding the **ancestral role**, the minimal prokaryotic iGluR (M1+M3, no M4, homomeric) is the best representative: it demonstrates that the mechanical LBD→pore transduction principle predates both heteromerization and the co-agonist/agonist AND-gate logic, which are vertebrate/eukaryotic refinements.

### Developmental and cell-type variation

Subunit composition is not fixed; it changes with development. The canonical switch is from GluN2B-dominated to GluN2A-containing receptors: "During development, GluN2A becomes incorporated into previously GluN2B-dominated NMDARs" ([PMID: 30355491](https://pubmed.ncbi.nlm.nih.gov/30355491/)). Because GluN2A and GluN2B confer different deactivation kinetics and open probabilities, this switch retunes synaptic integration without altering the core gating mechanism. GluN2C and GluN2D have distinct spatio-temporal expression and distinct inter-subunit/domain arrangements ([PMID: 36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/), [PMID: 36959261](https://pubmed.ncbi.nlm.nih.gov/36959261/)), and GluN3 subunits are enriched in specific developmental windows and cell types.

### Alternative routes to a similar outcome

The GluN2 vs. GluN3 branches represent **two molecularly distinct routes** to a ligand-gated cation channel built on the same GluN1 scaffold and the same gating mechanics. One route (GluN2) is a dual-ligand, Ca²⁺-permeable, Mg²⁺-blocked coincidence detector; the other (GluN3) is a single-ligand (glycine), weakly Ca²⁺-permeable, Mg²⁺-insensitive channel. They achieve "a ligand-gated cation channel" by different ligand logic and different pore chemistry.

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering and logical constraints

- **AND-gate requirement (GluN1/GluN2):** The gate does not open unless *both* clefts are occupied. Occupying only one leaves insufficient linker tension. This is a logical constraint enforced by the dimer-of-dimers geometry.
- **Opening precedes current, but current needs depolarization:** Even a correctly opened GluN1/GluN2 gate passes no current at resting potential because Mg²⁺ occludes the pore. "The NMDAR is subject to a rapid, highly voltage-dependent block by Mg²⁺" ([PMID: 39615648](https://pubmed.ncbi.nlm.nih.gov/39615648/)). Thus the temporal/physical constraint: **ligand binding and depolarization must coincide** for Ca²⁺ influx — the molecular basis of Hebbian coincidence detection ([PMID: 42086762](https://pubmed.ncbi.nlm.nih.gov/42086762/)).
- **Compartment/stage specificity:** Co-agonist supply (D-serine via serine racemase) is a rate-limiting, cell-type- and region-specific constraint on whether the GluN1 site is occupied in vivo ([PMID: 25740810](https://pubmed.ncbi.nlm.nih.gov/25740810/), [PMID: 28598327](https://pubmed.ncbi.nlm.nih.gov/28598327/)).

### Mutual exclusivities

- In GluN1/GluN3 receptors, glycine occupancy of the GluN1 site and maximal current are **antagonistic**: GluN1 occupancy auto-inhibits ([PMID: 26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/)). This is the opposite polarity to GluN1/GluN2.
- The Mg²⁺-block / high-Ca²⁺-permeability phenotype (GluN2) and the no-block / low-Ca²⁺ phenotype (GluN3) are set by the pore and are **mutually exclusive consequences of subunit composition**.

### What the evidence rules out

The cryo-EM antagonist structures rule out a purely "conformational-selection without mechanical linkage" model: because competitive antagonists at either subunit act by **relaxing linker tension**, the LBD–M3 linker is established as the obligatory mechanical conduit, not an incidental connector ([PMID: 32610085](https://pubmed.ncbi.nlm.nih.gov/32610085/)). The structural resolution of the M2 determinants also rules out models that place Ca²⁺/Mg²⁺ selectivity elsewhere than the re-entrant loop ([PMID: 42086762](https://pubmed.ncbi.nlm.nih.gov/42086762/)).

### Failure modes — human disease

The gating control points are validated as such by pathology. Pathogenic *GRIN* missense variants "cluster by spatial proximity to the agonist/antagonist binding sites," and this proximity is "a key predictive feature for both variant pathogenicity and molecular functional consequences," predicting gain- vs. loss-of-function ([PMID: 39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/); see also [PMID: 38766179](https://pubmed.ncbi.nlm.nih.gov/38766179/), [PMID: 38836461](https://pubmed.ncbi.nlm.nih.gov/38836461/)). That human variants converge on the ligand-sensing sites is independent, genetic confirmation that these sites are the obligatory levers of the gating mechanism (F005). Clinically, distance of a gain-of-function variant from the memantine (pore-blocker) binding site correlates with therapeutic response ([PMID: 41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/)).

---

## 7. Controversies and Open Questions

**Strongly supported claims.** The linker-tension gating model (F001), the obligatory dual-ligand AND gate for GluN1/GluN2 at both recombinant and endogenous levels (F006), the voltage-dependent Mg²⁺ block / Ca²⁺-permeability coincidence-detection logic with M2 determinants (F004), the glutamate-independent glycine activation and GluN1 auto-inhibition of GluN1/GluN3 (F002), and the prokaryotic K⁺-channel origin of the pore (F003) are each anchored in multiple independent structural, functional, and genetic studies.

**Areas of uncertainty and disagreement:**

1. **Classification of GluN1/GluN3 receptors.** Whether these are best called "NMDA receptors" is a genuine terminological dispute; they are family members by architecture but glutamate-independent by function ([PMID: 40235311](https://pubmed.ncbi.nlm.nih.gov/40235311/), [PMID: 32389749](https://pubmed.ncbi.nlm.nih.gov/32389749/)). Their native physiological roles, cell-type distribution, and endogenous activation conditions remain incompletely defined.
2. **Tri-heteromer stoichiometry and native abundance.** Although tri-heteromers are intermediate in gating ([PMID: 31541561](https://pubmed.ncbi.nlm.nih.gov/31541561/)) and methods now exist to express them cleanly ([PMID: 38727903](https://pubmed.ncbi.nlm.nih.gov/38727903/)), the precise native stoichiometry and relative abundance across brain regions and developmental stages are still being mapped.
3. **Co-agonist identity in vivo.** The relative in-vivo contributions of glycine vs. D-serine, and the spatial/temporal control of serine-racemase-derived D-serine, differ across circuits and remain debated ([PMID: 25740810](https://pubmed.ncbi.nlm.nih.gov/25740810/), [PMID: 25138794](https://pubmed.ncbi.nlm.nih.gov/25138794/)).
4. **Organism mixing.** Much structural work uses rat or human constructs interchangeably, and some functional parameters are extrapolated across species and expression systems. Quantitative gating parameters should not be assumed identical across organisms, cell types, or assays.
5. **Quantitative mapping of linker tension to open probability.** The qualitative tension model is secure, but a fully quantitative energetic description of how clamshell closure translates into gate-opening free energy — and how NTD modulators bias it — is not yet complete.

**Most important open questions:**
- What are the native functions and activation conditions of GluN1/GluN3 receptors in the human brain?
- Can the linker-tension model be made quantitative enough to predict P_open for arbitrary subunit combinations and disease variants?
- How do accessory layers (NTD modulators, M4, auxiliary proteins) bias the core gating energetics without being part of the obligatory input logic?

---

## 8. Mechanistic Model (Synthesis)

Putting the findings together, the NMDAR family implements **one conserved mechanical machine with two interchangeable ligand-logic front-ends and a composition-tuned pore**:

```
                    ┌─────────────── GluN1/GluN2 branch ───────────────┐
  Inputs:           glycine/D-serine @ GluN1  AND  glutamate @ GluN2
  Logic:            two-input AND gate
  Pore phenotype:   Na⁺/K⁺/Ca²⁺ permeable; voltage-dependent Mg²⁺ block
  Extra constraint: needs depolarization → Hebbian coincidence detector
                    └──────────────────────────────────────────────────┘

                    ┌─────────────── GluN1/GluN3 branch ───────────────┐
  Inputs:           glycine @ GluN3 (activating)  +  glycine @ GluN1 (auto-inhibitory)
  Logic:            glutamate-independent; GluN1-site occupancy limits efficacy
  Pore phenotype:   low Ca²⁺ permeability; NO Mg²⁺ block
                    └──────────────────────────────────────────────────┘

        BOTH BRANCHES share the same core transduction:
        agonist → LBD clamshell closes → LBD–M3 linker tension (chiefly partner)
                → M3 gate splays open → cation conduction

        Ancient core: inverted K⁺-channel pore (M1/M2/M3)
        Later add-ons: M4 helix, obligatory GluN1 heteromerization, NTD allostery
```

The elegance of the system is that **nature changed the computation (AND gate vs. single-input; coincidence detector vs. not) by swapping the partner subunit and re-pointing the ligand logic, while keeping the conserved mechanical transducer and the ancient pore scaffold essentially intact.**

---

## 9. Evidence Base

| PMID | Finding | Contribution |
|---|---|---|
| [32610085](https://pubmed.ncbi.nlm.nih.gov/32610085/) | F001 | Cryo-EM: gating controlled by LBD–TMD linker tension in GluN2; antagonists relax it |
| [39954679](https://pubmed.ncbi.nlm.nih.gov/39954679/) | F001 | Tri-heteromer GluN1/2B/2D: ligand-dependent extracellular-to-TMD tension governs gating/blockade |
| [40235311](https://pubmed.ncbi.nlm.nih.gov/40235311/) | F002 | GluN1/GluN3 activated solely by glycine, not glutamate |
| [32389749](https://pubmed.ncbi.nlm.nih.gov/32389749/) | F002 | Both GluN1 and GluN3 bind glycine; distinct functional/pharmacological properties |
| [26777280](https://pubmed.ncbi.nlm.nih.gov/26777280/) | F002 | GluN3 glycine triggers opening; GluN1 glycine auto-inhibits; GluN3A NTD sets efficacy |
| [21407198](https://pubmed.ncbi.nlm.nih.gov/21407198/) | F003 | iGluR with K⁺-channel 'TXVGYG' selectivity signature — pore–K⁺-channel link |
| [34658899](https://pubmed.ncbi.nlm.nih.gov/34658899/) | F003 | Prokaryotic ancestral iGluR (M1+M3 only); M4 a later eukaryotic addition |
| [42086762](https://pubmed.ncbi.nlm.nih.gov/42086762/) | F004 | Structural mechanism of Ca²⁺ permeability and Mg²⁺ block; coincidence detection |
| [39615648](https://pubmed.ncbi.nlm.nih.gov/39615648/) | F004 | Rapid, highly voltage-dependent Mg²⁺ block requiring depolarization |
| [31541561](https://pubmed.ncbi.nlm.nih.gov/31541561/) | F005 | Tri-heteromer gating intermediate between parent di-heteromers |
| [30355491](https://pubmed.ncbi.nlm.nih.gov/30355491/) | F005 | Developmental GluN2B→GluN2A compositional switch |
| [39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/) | F005 | Pathogenic variants cluster near ligand sites; proximity predicts function |
| [25740810](https://pubmed.ncbi.nlm.nih.gov/25740810/) | F006 | Native plasticity requires glutamate AND D-serine co-agonist |
| [28598327](https://pubmed.ncbi.nlm.nih.gov/28598327/) | F006 | D-serine availability regulates NMDAR function/trafficking |

Supporting/contextual literature: structural diversity of GluN2C/2D receptors ([PMID: 36309015](https://pubmed.ncbi.nlm.nih.gov/36309015/), [PMID: 36959261](https://pubmed.ncbi.nlm.nih.gov/36959261/)); comprehensive iGluR review ([PMID: 34753794](https://pubmed.ncbi.nlm.nih.gov/34753794/)); tri-heteromer expression methods ([PMID: 38727903](https://pubmed.ncbi.nlm.nih.gov/38727903/)); disease-variant functional analyses ([PMID: 38836461](https://pubmed.ncbi.nlm.nih.gov/38836461/), [PMID: 38766179](https://pubmed.ncbi.nlm.nih.gov/38766179/)); memantine precision therapy ([PMID: 41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/)); NTD/zinc allostery ([PMID: 21504727](https://pubmed.ncbi.nlm.nih.gov/21504727/)); serine racemase regulation ([PMID: 25164819](https://pubmed.ncbi.nlm.nih.gov/25164819/)).

---

## 10. Limitations and Knowledge Gaps

1. **Static snapshots of a dynamic process.** The linker-tension model rests largely on cryo-EM structures captured in discrete ligand states. These are powerful but are endpoints; the full energetic trajectory of gating and the lifetimes of intermediate states are inferred, not directly observed at atomic resolution.
2. **Species and system heterogeneity.** Findings aggregate human, rat, and mouse data across recombinant and native preparations. Quantitative gating parameters (P_open, deactivation rates, agonist potencies) can differ across these systems and should not be universalized.
3. **GluN1/GluN3 physiology underdetermined.** The in-vivo activation conditions, native partners, and functional roles of GluN3-containing receptors remain among the least-resolved aspects of the family.
4. **Accessory-to-core coupling not fully quantified.** How NTD modulators, the M4 helix, and auxiliary proteins bias the core gating energetics — while remaining outside the obligatory input logic — is qualitatively understood but not quantitatively modeled.
5. **Co-agonist occupancy in vivo.** The degree of endogenous saturation of the GluN1 glycine site, and the division of labor between glycine and D-serine across circuits and states, remain debated.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Time-resolved structural dynamics.** Use time-resolved cryo-EM, single-molecule FRET, or HS-AFM to capture the LBD-closure → linker-tension → M3-opening trajectory in real time, converting the static tension model into a kinetic one. (Single-molecule structural readouts have already been demonstrated for NMDARs, e.g. [PMID: 23223336](https://pubmed.ncbi.nlm.nih.gov/23223336/).)
2. **Quantitative tension-to-P_open mapping.** Engineer graded linker constraints (cross-links, length variants) across GluN2A–D and GluN3A/B backgrounds to build a predictive relationship between clamshell closure, linker tension, and open probability.
3. **Native GluN1/GluN3 characterization.** Determine the native cell types, developmental windows, endogenous agonist conditions, and physiological functions of GluN3-containing receptors in human/primate tissue.
4. **Variant-to-mechanism pipeline.** Combine the "distance-from-ligand" pathogenicity predictor ([PMID: 39535073](https://pubmed.ncbi.nlm.nih.gov/39535073/)) with functional assays across the full di-/tri-heteromer repertoire to prospectively classify novel *GRIN* variants as gain- vs. loss-of-function and guide memantine/precision therapy ([PMID: 41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/)).
5. **Pore-determinant swaps.** Systematically interchange M2 re-entrant-loop residues between GluN2 and GluN3 subunits to confirm, at the residue level, which elements convert the high-Ca²⁺/Mg²⁺-blocked phenotype into the low-Ca²⁺/no-block phenotype.
6. **Reconstructing the ancestral machine.** Characterize minimal prokaryotic-style iGluRs (M1+M3, homomeric; [PMID: 21407198](https://pubmed.ncbi.nlm.nih.gov/21407198/), [PMID: 34658899](https://pubmed.ncbi.nlm.nih.gov/34658899/)) to define the ancestral gating logic before heteromerization and the AND-gate arose.

---

*Scope note: This review is restricted to ligand sensing and conduction by assembled GluN1-containing heterotetramers. Receptor assembly/trafficking, PSD-95 anchoring, NTD allosteric modulation, and downstream Ca²⁺ signalling are treated as adjacent systems and are cited only where they bound or constrain the gating process itself.*


## Artifacts

- [OpenScientist final report](nmda_receptor_gating-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nmda_receptor_gating-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:38727903
2. PMID:36309015
3. PMID:21504727
4. PMID:42286176
5. PMID:32389749
6. PMID:32610085
7. PMID:39954679
8. PMID:25740810
9. PMID:28598327
10. PMID:40235311
11. PMID:26777280
12. PMID:42086762
13. PMID:31541561
14. PMID:21407198
15. PMID:34658899
16. PMID:30355491
17. PMID:36959261
18. PMID:39615648
19. PMID:39535073
20. PMID:38766179
21. PMID:38836461
22. PMID:41489401
23. PMID:25138794
24. PMID:34753794
25. PMID:25164819
26. PMID:23223336