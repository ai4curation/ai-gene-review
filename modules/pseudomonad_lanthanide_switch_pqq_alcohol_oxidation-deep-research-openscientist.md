---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T06:18:00.330421'
end_time: '2026-08-31T06:41:41.749647'
duration_seconds: 1421.42
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pseudomonad lanthanide-switch PQQ alcohol oxidation
  module_summary: A reusable pseudomonad module coupling PedS2/PedR2 two-component
    signaling to metal-conditioned periplasmic alcohol oxidation. In the absence of
    usable lanthanides, phosphorylated PedR2 favors expression of the calcium-dependent
    PQQ alcohol dehydrogenase PedE. Lanthanide availability shifts the system toward
    the lanthanide-dependent paralog PedH. Both enzymes oxidize diverse alcohols in
    the periplasm and pass electrons to cytochrome c. PQQ biosynthesis, downstream
    aldehyde metabolism, and lanthanide uptake are adjacent systems and are outside
    this module.
  module_outline: "- Pseudomonad lanthanide-switch PQQ alcohol oxidation\n  - 1. lanthanide-responsive\
    \ PedS2 sensor signaling\n  - PedS2 sensor-kinase signaling\n    - PedS2 phosphorelay\
    \ sensor kinase (molecular player: pseudomonad PedS2 sensor-kinase family; activity\
    \ or role: phosphorelay sensor kinase activity)\n  - 2. PedR2 transcriptional\
    \ switch output\n  - PedR2-dependent transcriptional control\n    - PedR2 phosphorelay\
    \ response regulator (molecular player: pseudomonad PedR2 response-regulator family;\
    \ activity or role: phosphorelay response regulator activity)\n  - 3. metal-conditioned\
    \ periplasmic PQQ alcohol oxidation\n  - Alternative PedE/PedH alcohol oxidation\n\
    \    - Alternative versions by catalytic metal availability: Ped alcohol-dehydrogenase\
    \ metal variants\n      - Calcium-dependent PedE alcohol oxidation\n        -\
    \ Calcium-dependent PQQ alcohol dehydrogenase PedE (molecular player: calcium-dependent\
    \ PedE-type PQQ alcohol dehydrogenase family; activity or role: alcohol dehydrogenase\
    \ (cytochrome c) activity)\n      - Lanthanide-dependent PedH alcohol oxidation\n\
    \        - Lanthanide-dependent PQQ alcohol dehydrogenase PedH (molecular player:\
    \ lanthanide-dependent PedH-type PQQ alcohol dehydrogenase family; activity or\
    \ role: alcohol dehydrogenase (cytochrome c) activity)"
  module_connections: '- PedS2 sensor-kinase signaling promotes PedR2-dependent transcriptional
    control: PedS2-dependent phosphorylation activates PedR2 output in the lanthanide-free
    state.

    - PedR2-dependent transcriptional control promotes Calcium-dependent PedE alcohol
    oxidation: Phosphorylated PedR2 promotes the calcium-dependent PedE branch.

    - PedR2-dependent transcriptional control inhibits Lanthanide-dependent PedH alcohol
    oxidation: PedR2 contributes to repression of the PedH branch without lanthanides.'
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
  path: pseudomonad_lanthanide_switch_pqq_alcohol_oxidation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pseudomonad_lanthanide_switch_pqq_alcohol_oxidation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Pseudomonad lanthanide-switch PQQ alcohol oxidation

## Working Scope

A reusable pseudomonad module coupling PedS2/PedR2 two-component signaling to metal-conditioned periplasmic alcohol oxidation. In the absence of usable lanthanides, phosphorylated PedR2 favors expression of the calcium-dependent PQQ alcohol dehydrogenase PedE. Lanthanide availability shifts the system toward the lanthanide-dependent paralog PedH. Both enzymes oxidize diverse alcohols in the periplasm and pass electrons to cytochrome c. PQQ biosynthesis, downstream aldehyde metabolism, and lanthanide uptake are adjacent systems and are outside this module.

## Provisional Biological Outline

- Pseudomonad lanthanide-switch PQQ alcohol oxidation
  - 1. lanthanide-responsive PedS2 sensor signaling
  - PedS2 sensor-kinase signaling
    - PedS2 phosphorelay sensor kinase (molecular player: pseudomonad PedS2 sensor-kinase family; activity or role: phosphorelay sensor kinase activity)
  - 2. PedR2 transcriptional switch output
  - PedR2-dependent transcriptional control
    - PedR2 phosphorelay response regulator (molecular player: pseudomonad PedR2 response-regulator family; activity or role: phosphorelay response regulator activity)
  - 3. metal-conditioned periplasmic PQQ alcohol oxidation
  - Alternative PedE/PedH alcohol oxidation
    - Alternative versions by catalytic metal availability: Ped alcohol-dehydrogenase metal variants
      - Calcium-dependent PedE alcohol oxidation
        - Calcium-dependent PQQ alcohol dehydrogenase PedE (molecular player: calcium-dependent PedE-type PQQ alcohol dehydrogenase family; activity or role: alcohol dehydrogenase (cytochrome c) activity)
      - Lanthanide-dependent PedH alcohol oxidation
        - Lanthanide-dependent PQQ alcohol dehydrogenase PedH (molecular player: lanthanide-dependent PedH-type PQQ alcohol dehydrogenase family; activity or role: alcohol dehydrogenase (cytochrome c) activity)

## Known Relationships Among Steps

- PedS2 sensor-kinase signaling promotes PedR2-dependent transcriptional control: PedS2-dependent phosphorylation activates PedR2 output in the lanthanide-free state.
- PedR2-dependent transcriptional control promotes Calcium-dependent PedE alcohol oxidation: Phosphorylated PedR2 promotes the calcium-dependent PedE branch.
- PedR2-dependent transcriptional control inhibits Lanthanide-dependent PedH alcohol oxidation: PedR2 contributes to repression of the PedH branch without lanthanides.

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

# Pseudomonad Lanthanide-Switch PQQ Alcohol Oxidation: A Review-Style Synthesis

*A commissioned review of the PedS2/PedR2 two-component system coupling lanthanide availability to metal-conditioned periplasmic PQQ alcohol dehydrogenases PedE and PedH.*

---

## 1. Executive Summary

The **pseudomonad lanthanide switch** is a compact, reusable regulatory-catalytic module that allows a soil/rhizosphere bacterium to select which of two periplasmic pyrroloquinoline-quinone (PQQ) alcohol dehydrogenases (ADHs) it deploys, according to the availability of usable light lanthanides (rare-earth elements, REEs). The module has three linked parts: (i) a **lanthanide-responsive sensor histidine kinase, PedS2**; (ii) a **cognate LuxR-type response regulator, PedR2**, that reads the phosphorylation state set by PedS2; and (iii) two paralogous, functionally overlapping **quinoprotein alcohol dehydrogenases, PedE (Ca²⁺-dependent) and PedH (lanthanide-dependent)**, that oxidize a broad range of alcohols and aldehydes in the periplasm and pass electrons to cytochrome *c*.

The best-supported model (worked out chiefly in *Pseudomonas putida* KT2440) is a phosphorylation-gated inverse switch. In the **absence of usable lanthanides**, PedS2 phosphorylates PedR2; phospho-PedR2 **activates *pedE*** and simultaneously **contributes to repression of *pedH***. When **light lanthanides (La³⁺–Nd³⁺) become available**, PedS2 kinase activity falls — proposed to result from lanthanide perception at its periplasmic region — lowering phospho-PedR2 so that *pedE* transcription declines and *pedH* repression is relieved. Notably, full *pedH* activation additionally requires a second, still-unidentified regulatory input, so the switch is **not symmetric**: de-repression of *pedH* is necessary but not sufficient (Wehrmann et al., 2017 [PMID 28655819]; Wehrmann et al., 2018 [PMID 30158283]).

This system is best understood as a **heterotrophic elaboration of an ancient scaffold** — two-component regulation of a PQQ alcohol dehydrogenase feeding cytochrome *c* — that predates the lanthanide dimension in pseudomonads (ExaD/ExaE and AgmR systems; Görisch 2003 [PMID 12686116]; Vrionis et al. 2002 [PMID 11954793]). It is mechanistically **analogous but not identical** to the methylotroph XoxF/MxaF "lanthanide switch," from which much of the structural and chemical rationale is borrowed (Skovran et al. 2019 [PMID 31166187]; Yu & Chistoserdova 2019 [PMID 31166192]). Adjacent systems — **lanthanide uptake (PedA1A2BC), PQQ biosynthesis, and downstream aldehyde/carbon metabolism** — set the inputs and consume the outputs of the module but lie outside its core. The most important open questions are the molecular identity of the additional *pedH* activator and direct structural proof that PedS2 senses lanthanides.

---

## 2. Definition and Biological Boundaries

### 2.1 What is inside the module

The module comprises exactly four dedicated molecular players and their regulatory relationships:

| Component | Identity | Role in the module |
|---|---|---|
| **PedS2** (e.g., PP_2671 in KT2440) | Sensor histidine kinase | Perceives lanthanide status; sets PedR2 phosphorylation |
| **PedR2** (e.g., PP_2672) | LuxR-type response regulator | Dual activator/repressor; transcriptional output |
| **PedE** | Ca²⁺-dependent PQQ-ADH | Alcohol oxidation when lanthanides unavailable |
| **PedH** | Lanthanide-dependent PQQ-ADH | Alcohol oxidation when lanthanides available |

Both enzymes are periplasmic quinoproteins that oxidize a broad substrate range of alcohols (and some aldehydes) and transfer electrons to cytochrome *c*, connecting to the respiratory chain. The regulatory logic — a phospho-relay two-component system driving reciprocal expression of a Ca/Ln enzyme pair — is the defining feature.

### 2.2 What is adjacent but outside the module

Several closely coupled processes are frequently discussed alongside the switch but are mechanistically distinct and should be treated separately:

- **Lanthanide uptake and trafficking** — e.g., the ABC-type transporter **PedA1A2BC** and lanthanide chaperones such as lanmodulin. Uptake sets the intracellular lanthanide concentration that the switch experiences but is not part of the sensing/output circuit itself (Wehrmann et al. 2019 [PMID 31736923]; Cotruvo 2020 [PMID 32979423]).
- **PQQ biosynthesis** — supplies the essential cofactor shared by both enzymes but is a separate biosynthetic pathway.
- **Downstream aldehyde and carbon metabolism** — e.g., aldehyde dehydrogenases (PedI-type) and the novel PedE/PedH-initiated glycerol-oxidation route into central metabolism. These consume the module's products but do not participate in the metal-conditioned switch (Wehrmann et al. 2020 [PMID 32345644]).

### 2.3 Competing and overlapping definitions

The term **"lanthanide switch"** was first coined in the methylotrophy literature for the reciprocal regulation of **XoxF (Ln-dependent) versus MxaFI (Ca-dependent) methanol dehydrogenases** (Skovran et al. 2019 [PMID 31166187]; Yu & Chistoserdova 2019 [PMID 31166192]). The pseudomonad PedE/PedH system is the **archetypal non-methylotrophic instance** of the same regulatory logic applied to multi-carbon (non-methanol) alcohol metabolism. Readers should be careful not to conflate:

- the **methylotroph methanol-oxidation switch** (XoxF/MxaF), with
- the **pseudomonad broad-alcohol switch** (PedE/PedH, regulated by PedS2/PedR2).

They are homologous in concept and enzyme family but differ in the specific regulators, enzyme architecture details, and physiological substrate.

---

## 3. Mechanistic Overview

### 3.1 The core switch model

The best current model, established primarily through adaptive laboratory evolution, site-directed mutagenesis, reporter fusions, and complementation in *P. putida* KT2440 (Wehrmann et al. 2018 [PMID 30158283]), is as follows:

```
   LANTHANIDE-FREE STATE                    LANTHANIDE-REPLETE STATE
   ─────────────────────                    ────────────────────────
   PedS2 (kinase ON)                        La3+ perceived at PedS2
        │ phosphorylates                    PedS2 (kinase LOW)
        ▼                                         │
   PedR2 ~ P  (active)                       PedR2 (mostly unphosph.)
    │            │                                │
    │ activates  │ represses                      │ (activation lost,
    ▼            ▼                                 ▼  repression relieved)
  pedE  ON     pedH  OFF                      pedE  DOWN    pedH  UP*
    │                                                         │
    ▼                                                         ▼
  PedE (Ca2+) oxidizes alcohols            PedH (Ln3+) oxidizes alcohols
        │                                                     │
        └──────────► cytochrome c ◄───────────────────────────┘
                         │
                         ▼
                 respiratory chain / energy

  * full pedH activation additionally requires a
    yet-unidentified second regulatory module
```

### 3.2 Obligatory, conditional, and accessory steps

- **Obligatory:** PedS2-dependent phosphotransfer to PedR2 is the central node. In the lanthanide-free state, phospho-PedR2 is required both to activate *pedE* and to help repress *pedH*.
- **Conditional:** Lanthanide perception is the conditional input that flips the switch. Its downstream consequence — reduced PedS2 kinase activity — is what lowers phospho-PedR2.
- **Accessory / incompletely defined:** Full activation of *pedH* is **not** achieved by de-repression alone; a **second, uncharacterized activator module** is required. This is the single largest mechanistic gap in the model.

### 3.3 Metal-conditioned catalysis

Once expressed, each enzyme performs the same chemical reaction — PQQ-dependent alcohol oxidation with electron transfer to cytochrome *c* — but uses a different catalytic metal at the PQQ active site. The choice of Ca²⁺ versus Ln³⁺ is not arbitrary: lanthanides are **superior Lewis acids** at the PQQ site. Density-functional calculations on the cerium-dependent methanol dehydrogenase active site show that Ce(III) stabilizes the PQQ LUMO by ~0.81 eV relative to calcium, providing an electronic rationale for a catalytic advantage (Bogart et al. 2015 [PMID 25421364]). Cells that can acquire REEs therefore gain access to a kinetically favorable oxidation route.

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 PedS2 — lanthanide-responsive sensor histidine kinase

PedS2 is the input node. In the lanthanide-free state it acts as an active kinase, phosphorylating PedR2. Lanthanide availability lowers its kinase activity, proposed to occur either by **direct binding of Ln³⁺ to the periplasmic region of PedS2** or by an uncharacterized indirect interaction (Wehrmann et al. 2018 [PMID 30158283]). Direct structural or biophysical proof of lanthanide binding by PedS2 has **not yet been reported** and remains a key gap. PedS2 is also a proposed target of **mismetallation**: iron (and to a lesser extent copper and zinc) can raise the minimal Ln³⁺ concentration required to flip the switch by orders of magnitude, consistent with Fe-driven mismetallation of putative La³⁺-binding proteins such as PedS2 (Wehrmann et al. 2019 [PMID 31736923]).

### 4.2 PedR2 — LuxR-type response regulator with dual output

PedR2 is a **dual-function** transcriptional regulator: in its phosphorylated form it **activates *pedE*** and **contributes to repression of *pedH***. This makes the switch reciprocal from a single regulator's phosphorylation state (Wehrmann et al. 2018 [PMID 30158283]). Because full *pedH* activation requires an additional module, PedR2 is best described as the master regulator of the Ca-branch and a partial (necessary-but-not-sufficient) contributor to control of the Ln-branch.

### 4.3 PedE — calcium-dependent PQQ alcohol dehydrogenase

PedE is a Ca²⁺-dependent quinoprotein ADH that oxidizes a broad range of alcohols/aldehydes in the periplasm and passes electrons to cytochrome *c*. It is the "default" enzyme when usable lanthanides are absent (Wehrmann et al. 2017 [PMID 28655819]).

### 4.4 PedH — lanthanide-dependent PQQ alcohol dehydrogenase

PedH is the **first lanthanide-dependent PQQ-ADH characterized in a non-methylotrophic bacterium**. Purified from *P. putida* KT2440, it requires light lanthanides (La³⁺–Nd³⁺) for alcohol-oxidizing activity, whereas its paralog PedE is Ca²⁺-dependent. The two are **functionally redundant** periplasmic isozymes with overlapping broad substrate ranges (Wehrmann et al. 2017 [PMID 28655819]).

### 4.5 Structural context of the enzyme pair

PedE and PedH are members of the **QEDH/XoxF-type** family of PQQ-ADHs. Crystallography of the lanthanide methanol dehydrogenase XoxF reveals a **La(III) ion in the active site within a homodimeric fold**, contrasting with the Ca²⁺-dependent **MxaFI heterotetramer** (Deng et al. 2018 [PMID 30132076]). By homology, PedE/PedH are expected to be XoxF/QEDH-like homodimeric PQQ-ADHs, distinct from the classic MxaFI architecture. These methylotroph enzymes are the best-characterized structural proxies, and inferences to PedE/PedH should be made with that caveat in mind.

| Feature | Ca²⁺ branch (PedE / MxaF-like) | Ln³⁺ branch (PedH / XoxF-like) |
|---|---|---|
| Catalytic metal | Ca²⁺ | Light Ln³⁺ (La–Nd) |
| Structural archetype | MxaFI heterotetramer | XoxF homodimer |
| Electronic effect on PQQ | Baseline | LUMO stabilized ~0.81 eV (Ce vs Ca) |
| Regulatory state favoring it | phospho-PedR2 high | phospho-PedR2 low + extra activator |
| Electron acceptor | cytochrome *c* | cytochrome *c* |

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 An ancient two-component/PQQ-ADH scaffold

Two-component regulation of a PQQ alcohol-oxidation system feeding cytochrome *c* **predates** the lanthanide dimension in pseudomonads. In *Pseudomonas aeruginosa*, transcription of the quinoprotein ethanol dehydrogenase (QEDH/ExaA) is controlled by a two-component system — histidine kinase **ExaD** and response regulator **ExaE** — with cytochrome c₅₅₀ as the essential electron acceptor (Görisch 2003 [PMID 12686116]). *P. putida* KT2440 was already known to carry two PQQ-linked ADH genes and a response regulator (**AgmR**) governing alcohol utilization before the lanthanide role was recognized (Vrionis et al. 2002 [PMID 11954793]). The lanthanide switch is thus best read as a **lineage-specific elaboration** — the addition of metal-sensing input and a Ln-dependent paralog — onto a pre-existing TCS→PQQ-ADH→cytochrome-*c* scaffold.

### 5.2 The methylotroph connection

The reciprocal Ca/Ln regulatory logic is shared with, and was first defined in, methylotrophs, where the **XoxF (Ln) / MxaF (Ca)** methanol dehydrogenase switch is central to one-carbon metabolism (Skovran et al. 2019 [PMID 31166187]; Yu & Chistoserdova 2019 [PMID 31166192]). The recognition that lanthanide-dependent enzymes extend to **multi-carbon metabolism in non-methylotrophs** — with PedE/PedH as the archetype — expanded the scope of lanthanide biochemistry well beyond methylotrophy (Skovran et al. 2019 [PMID 31166187]).

### 5.3 Conservation and elaboration beyond Pseudomonas

The Ca/Ln paralog pair and its inverse regulation are **portable across lineages**. In the plastic-degrading betaproteobacterium *Ideonella sakaiensis*, homologs **IsPedE (Ca²⁺)** and **IsPedH (Pr³⁺)** were identified alongside an additional **IsXoxF (Pr³⁺)** with a larger catalytic pocket that favors bulkier substrates, plus the aldehyde dehydrogenase **IsPedI** — all homologs of *P. putida* KT2440 ethylene-glycol metabolic enzymes. Pr³⁺ negatively regulated IsPedE protein and positively regulated IsPedH and IsXoxF, **reproducing the inverse REE-switch expression pattern in a distinct lineage** (Hachisuka et al. 2022 [PMID 36289066]).

This example also refines the "functional redundancy" claim: the paralogs are **tuned rather than perfectly redundant**. Substrate partitioning — a broad-range PedE, a small-alcohol-preferring PedH, and a bulky-substrate-preferring XoxF — shows the enzyme set is diversified to cover complementary substrate space, with lineage-specific additions (a third XoxF-type enzyme) expanding range.

### 5.4 Compartmental and physiological states

The enzymes operate in the **periplasm**; the regulators span the membrane (sensor) and cytoplasm (response regulator). The switch is physiologically important under conditions requiring efficient growth on **alcoholic volatiles**, and lanthanum strongly affects growth on **glycerol**, where PedE/PedH initiate a novel oxidation route (to glycerate via glyceraldehyde, then GarK) operating in parallel with the canonical glpFKRD pathway. The cellular La³⁺ response is largely **substrate-specific** rather than global (Wehrmann et al. 2020 [PMID 32345644]).

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering constraints

- **Sensing precedes output:** PedS2 must set PedR2's phosphorylation state before transcriptional output changes.
- **Cofactor and metal must be available for catalysis:** Both enzymes require PQQ; PedE additionally requires Ca²⁺ and PedH requires a usable light Ln³⁺. If the appropriate metal is unavailable to the expressed enzyme, oxidation fails regardless of transcription.
- **Uptake gates the input:** Intracellular lanthanide availability — not merely external concentration — determines the switch state, and uptake is gated by the PedA1A2BC transporter (see below).

### 6.2 Mutually exclusive / conditional relationships

- The **Ca and Ln branches are reciprocally regulated**: high phospho-PedR2 favors PedE and represses PedH, and vice versa. They are not simultaneously maximally expressed.
- *pedH* de-repression is **necessary but not sufficient** for its full expression; the second activator module is a required conditional input.

### 6.3 Uptake gating and metal competition (failure modes)

REE-dependent growth on 2-phenylethanol at low (nanomolar) Ln³⁺ requires the ABC-type uptake system **PedA1A2BC**. Its loss raises the La³⁺ needed for PedH-dependent growth ~100-fold, **but not** the concentration needed to repress PedE — indicating uptake specifically feeds the enzyme/activation arm (Wehrmann et al. 2019 [PMID 31736923]).

**Metal competition is a major failure mode and confounder.** Copper, zinc, and especially **iron** raise the minimal Ln³⁺ concentration required for the switch by orders of magnitude, consistent with **Fe-driven mismetallation** of putative La³⁺-binding proteins such as PedS2 (Wehrmann et al. 2019 [PMID 31736923]). Consequently, the **La³⁺/Fe ratio** — and, more broadly, medium composition — strongly affects apparent switch thresholds. This is a crucial caveat when comparing quantitative results across studies and organisms.

### 6.4 Boundary dependencies

The module depends on but does not contain: PQQ biosynthesis (cofactor supply), lanthanide uptake/trafficking (input concentration), and downstream aldehyde/carbon metabolism (product disposal and energy capture). Failures in any of these adjacent systems will impair the module's physiological output without altering its intrinsic switch logic.

---

## 7. Controversies and Open Questions

1. **Identity of the second *pedH* activator.** The most important unresolved mechanistic point. Loss of PedR2-mediated repression is insufficient for full *pedH* expression; a distinct, uncharacterized regulatory module is required (Wehrmann et al. 2018 [PMID 30158283]). Its identity, whether it directly senses lanthanides, and how it integrates with PedR2 are unknown.

2. **Direct proof of lanthanide sensing by PedS2.** Lanthanide perception at the PedS2 periplasmic region is **inferred, not structurally demonstrated**. Whether Ln³⁺ binds PedS2 directly or acts through an intermediary remains open (Wehrmann et al. 2018 [PMID 30158283]).

3. **Degree of enzyme redundancy vs specialization.** Early work emphasized functional redundancy of PedE/PedH (Wehrmann et al. 2017 [PMID 28655819]), but cross-lineage data reveal substrate partitioning and additional paralogs (Hachisuka et al. 2022 [PMID 36289066]). How much substrate specialization exists in *P. putida* itself, versus other organisms, is not fully resolved.

4. **Comparability across organisms and assays.** Much of the structural and chemical rationale is imported from **methylotroph** enzymes (XoxF/MxaF) and DFT models (Bogart et al. 2015 [PMID 25421364]; Deng et al. 2018 [PMID 30132076]). Extrapolation to PedE/PedH is reasonable by homology but not directly proven at the structural level. Quantitative switch thresholds are strongly medium-dependent (iron, other metals), complicating cross-study comparison (Wehrmann et al. 2019 [PMID 31736923]).

5. **Generality of the regulatory architecture.** Whether the PedS2/PedR2 architecture (as opposed to the methylotroph MxbD/MxcQ-type systems) is the dominant mode of lanthanide-switch control in non-methylotrophs broadly, or is one of several convergent solutions, is not yet established.

---

## 8. Limitations and Knowledge Gaps

This synthesis rests heavily on a single, deeply studied model organism (*P. putida* KT2440) and a small number of laboratories. Several structural claims about PedE/PedH are **inferred from methylotroph homologs** (XoxF/MxaF) rather than proven for the Ped enzymes themselves. The lanthanide-sensing mechanism of PedS2 is **hypothetical at the molecular level**, and the second *pedH* activator is **entirely uncharacterized**. Quantitative parameters (switch thresholds, effective La³⁺ concentrations) are **highly medium-dependent** — particularly sensitive to iron and other divalent/trivalent metals — so numbers are not directly transferable between studies. Cross-lineage conservation is supported by one betaproteobacterial example (*I. sakaiensis*); broader phylogenetic sampling is needed to know how general the PedS2/PedR2 architecture is.

---

## 9. Proposed Follow-up Experiments and Actions

1. **Identify the second *pedH* activator** via transposon/CRISPRi screens for mutants that fail to induce *pedH* under lanthanide-replete conditions despite loss of PedR2 repression.
2. **Biophysically test lanthanide binding to PedS2** — isolate the periplasmic domain and measure direct Ln³⁺ binding (ITC, spectroscopy) versus indirect models, including Fe³⁺ competition to test the mismetallation hypothesis.
3. **Determine PedE and PedH crystal or cryo-EM structures** to confirm the predicted XoxF-like homodimeric architecture and the metal-coordination geometry, replacing homology inference with direct evidence.
4. **Systematically map substrate specialization** of PedE vs PedH in *P. putida* under matched conditions to quantify the degree of redundancy versus tuning.
5. **Survey the PedS2/PedR2 architecture across diverse bacteria** to establish whether it is the dominant non-methylotroph lanthanide-switch solution or one of several convergent designs.

---

## 10. Key References

Citations are drawn from the verified evidence base assembled during this investigation. PMIDs link to PubMed.

- Wehrmann M, et al. *Functional Role of Lanthanides in Enzymatic Activity and Transcriptional Regulation of PQQ-Dependent Alcohol Dehydrogenases in Pseudomonas putida KT2440.* mBio (2017). [PMID: 28655819](https://pubmed.ncbi.nlm.nih.gov/28655819/) — First characterization of a lanthanide-dependent PQQ-ADH (PedH) in a non-methylotroph; establishes PedE (Ca²⁺) / PedH (Ln³⁺) as functionally redundant periplasmic isozymes.
- Wehrmann M, et al. *The PedS2/PedR2 Two-Component System Is Crucial for the Rare Earth Element Switch in Pseudomonas putida KT2440.* mSphere (2018). [PMID: 30158283](https://pubmed.ncbi.nlm.nih.gov/30158283/) — Defines the core switch: phospho-PedR2 activates *pedE* and represses *pedH*; La³⁺ lowers PedS2 kinase activity; full *pedH* activation needs an additional unknown module.
- Wehrmann M, et al. *Lanthanide uptake (PedA1A2BC) and iron cross-talk in the REE switch.* Front. Microbiol. (2019). [PMID: 31736923](https://pubmed.ncbi.nlm.nih.gov/31736923/) — ABC transporter gates lanthanide input; iron mismetallation of PedS2 as a failure mode.
- Wehrmann M, et al. *The Cellular Response to Lanthanum Is Substrate Specific and Reveals a Novel Route for Glycerol Metabolism in Pseudomonas putida KT2440.* mBio (2020). [PMID: 32345644](https://pubmed.ncbi.nlm.nih.gov/32345644/) — Physiological importance for growth on alcoholic volatiles; PedE/PedH-initiated glycerol route.
- Hachisuka S, et al. *PedE/PedH/XoxF homologs in Ideonella sakaiensis.* Appl. Microbiol. Biotechnol. (2022). [PMID: 36289066](https://pubmed.ncbi.nlm.nih.gov/36289066/) — Conservation of the Ca/Ln paralog pair and inverse REE regulation beyond *Pseudomonas*, with substrate partitioning.
- Görisch H. *The ethanol oxidation system and its regulation in Pseudomonas aeruginosa.* (2003). [PMID: 12686116](https://pubmed.ncbi.nlm.nih.gov/12686116/) — Ancestral two-component (ExaD/ExaE) regulation of a PQQ-ADH with cytochrome c₅₅₀.
- Vrionis HA, et al. *Identification and characterization of the AgmR regulator of Pseudomonas putida: role in alcohol utilization.* (2002). [PMID: 11954793](https://pubmed.ncbi.nlm.nih.gov/11954793/) — KT2440 carries two PQQ-ADH genes and a response regulator governing alcohol use.
- Skovran E, et al. *Lanthanides in Methylotrophy.* (2019). [PMID: 31166187](https://pubmed.ncbi.nlm.nih.gov/31166187/) — Defines the methylotroph "lanthanide switch" and notes extension to non-methylotrophs.
- Yu Z, Chistoserdova L. *Systems Biology Meets Enzymology: Communal Metabolism of Methane and the Role of Lanthanides.* (2019). [PMID: 31166192](https://pubmed.ncbi.nlm.nih.gov/31166192/) — Lanthanide switch regulating alternative methanol dehydrogenases.
- Bogart JA, et al. *DFT of the cerium-dependent methanol dehydrogenase active site.* (2015). [PMID: 25421364](https://pubmed.ncbi.nlm.nih.gov/25421364/) — ~0.81 eV LUMO stabilization at Ce vs Ca rationalizes the catalytic advantage of lanthanides.
- Deng YW, et al. *Crystal structure of the lanthanide methanol dehydrogenase XoxF.* (2018). [PMID: 30132076](https://pubmed.ncbi.nlm.nih.gov/30132076/) — La(III) in a homodimeric fold vs the Ca²⁺ MxaFI heterotetramer; structural template for PedE/PedH.
- Cotruvo JA Jr. *The biochemistry of lanthanide acquisition, trafficking, and utilization.* (2020). [PMID: 32979423](https://pubmed.ncbi.nlm.nih.gov/32979423/) — Context for lanthanide uptake/trafficking (adjacent system).

---

*Prepared as a commissioned review synthesis. Uncertainty is flagged throughout; claims are attributed to the specific studies that support them, and inferences from methylotroph systems to the pseudomonad enzymes are identified as such.*


## Artifacts

- [OpenScientist final report](pseudomonad_lanthanide_switch_pqq_alcohol_oxidation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pseudomonad_lanthanide_switch_pqq_alcohol_oxidation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28655819
2. PMID:30158283
3. PMID:31736923
4. PMID:32345644
5. PMID:36289066
6. PMID:12686116
7. PMID:11954793
8. PMID:31166187
9. PMID:31166192
10. PMID:25421364
11. PMID:30132076
12. PMID:32979423