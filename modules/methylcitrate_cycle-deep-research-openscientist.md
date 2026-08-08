---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:43:43.626331'
end_time: '2026-07-23T13:56:24.076480'
duration_seconds: 760.45
template_file: templates/module_research.md.j2
template_variables:
  module_title: 2-methylcitrate cycle
  module_summary: A reusable propionate-assimilation module that activates propionate
    to propionyl-CoA, condenses propionyl-CoA with oxaloacetate to form 2-methylcitrate,
    converts 2-methylcitrate to 2-methylisocitrate through alternative dehydration/isomerization
    implementations, and cleaves 2-methylisocitrate to succinate and pyruvate. The
    module distinguishes the direct PrpD route from the two-component AcnD/PrpF route
    and represents the common aconitase-family hydration step separately.
  module_outline: "- 2-methylcitrate cycle\n  - 1. propionate activation\n  - Propionate\
    \ activation to propionyl-CoA\n    - Propionate-CoA ligase (molecular player:\
    \ PrpE-family propionate-CoA ligases; activity or role: propionate-CoA ligase\
    \ activity)\n  - 2. 2-methylcitrate formation\n  - 2-methylcitrate synthesis\n\
    \    - 2-methylcitrate synthase (molecular player: PrpC 2-methylcitrate synthases;\
    \ activity or role: 2-methylcitrate synthase activity)\n  - 3. 2-methyl-cis-aconitate\
    \ generation\n  - Conversion of 2-methylcitrate to 2-methyl-cis-aconitate\n  \
    \  - Alternative versions by reaction mechanism: 2-methylcitrate dehydration implementations\n\
    \      - Direct PrpD route\n        - PrpD 2-methylcitrate dehydratase (molecular\
    \ player: PrpD 2-methylcitrate dehydratases; activity or role: 2-methylcitrate\
    \ dehydratase activity)\n      - Two-component AcnD/PrpF route\n        - 1. AcnD-dependent\
    \ dehydration\n        - AcnD-family 2-methylcitrate dehydration\n          -\
    \ AcnD 2-methylcitrate dehydratase (molecular player: AcnD-family 2-methylcitrate\
    \ dehydratases; activity or role: hydro-lyase activity)\n        - 2. methylaconitate\
    \ isomerization\n        - PrpF methylaconitate isomerization\n          - PrpF\
    \ aconitate isomerase (molecular player: PrpF methylaconitate isomerases; activity\
    \ or role: isomerase activity)\n  - 4. 2-methylisocitrate formation\n  - 2-methyl-cis-aconitate\
    \ hydration\n    - Alternative versions by aconitase paralog family: Aconitase-family\
    \ hydration implementations\n      - AcnB-family hydration\n        - AcnB-family\
    \ 2-methylisocitrate hydratase (molecular player: AcnB-family aconitate hydratases\
    \ with methylisocitrate activity; activity or role: 2-methylisocitrate dehydratase\
    \ activity)\n      - AcnA-family hydration\n        - AcnA-family 2-methylisocitrate\
    \ hydratase (molecular player: AcnA-family aconitate hydratases with methylisocitrate\
    \ activity; activity or role: 2-methylisocitrate dehydratase activity)\n  - 5.\
    \ carbon-carbon cleavage\n  - 2-methylisocitrate cleavage\n    - 2-methylisocitrate\
    \ lyase (molecular player: PrpB 2-methylisocitrate lyases; activity or role: methylisocitrate\
    \ lyase activity)"
  module_connections: '- Propionate activation to propionyl-CoA feeds into 2-methylcitrate
    synthesis: Propionyl-CoA is the acyl donor for 2-methylcitrate synthesis.

    - 2-methylcitrate synthesis feeds into Conversion of 2-methylcitrate to 2-methyl-cis-aconitate:
    2-methylcitrate enters either dehydration implementation.

    - Conversion of 2-methylcitrate to 2-methyl-cis-aconitate feeds into 2-methyl-cis-aconitate
    hydration: Both alternatives converge on 2-methyl-cis-aconitate.

    - 2-methyl-cis-aconitate hydration feeds into 2-methylisocitrate cleavage: 2-methylisocitrate
    is the substrate cleaved by PrpB.

    - AcnD-family 2-methylcitrate dehydration feeds into PrpF methylaconitate isomerization:
    The AcnD product is the substrate rearranged by PrpF.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: methylcitrate_cycle-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: methylcitrate_cycle-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

2-methylcitrate cycle

## Working Scope

A reusable propionate-assimilation module that activates propionate to propionyl-CoA, condenses propionyl-CoA with oxaloacetate to form 2-methylcitrate, converts 2-methylcitrate to 2-methylisocitrate through alternative dehydration/isomerization implementations, and cleaves 2-methylisocitrate to succinate and pyruvate. The module distinguishes the direct PrpD route from the two-component AcnD/PrpF route and represents the common aconitase-family hydration step separately.

## Provisional Biological Outline

- 2-methylcitrate cycle
  - 1. propionate activation
  - Propionate activation to propionyl-CoA
    - Propionate-CoA ligase (molecular player: PrpE-family propionate-CoA ligases; activity or role: propionate-CoA ligase activity)
  - 2. 2-methylcitrate formation
  - 2-methylcitrate synthesis
    - 2-methylcitrate synthase (molecular player: PrpC 2-methylcitrate synthases; activity or role: 2-methylcitrate synthase activity)
  - 3. 2-methyl-cis-aconitate generation
  - Conversion of 2-methylcitrate to 2-methyl-cis-aconitate
    - Alternative versions by reaction mechanism: 2-methylcitrate dehydration implementations
      - Direct PrpD route
        - PrpD 2-methylcitrate dehydratase (molecular player: PrpD 2-methylcitrate dehydratases; activity or role: 2-methylcitrate dehydratase activity)
      - Two-component AcnD/PrpF route
        - 1. AcnD-dependent dehydration
        - AcnD-family 2-methylcitrate dehydration
          - AcnD 2-methylcitrate dehydratase (molecular player: AcnD-family 2-methylcitrate dehydratases; activity or role: hydro-lyase activity)
        - 2. methylaconitate isomerization
        - PrpF methylaconitate isomerization
          - PrpF aconitate isomerase (molecular player: PrpF methylaconitate isomerases; activity or role: isomerase activity)
  - 4. 2-methylisocitrate formation
  - 2-methyl-cis-aconitate hydration
    - Alternative versions by aconitase paralog family: Aconitase-family hydration implementations
      - AcnB-family hydration
        - AcnB-family 2-methylisocitrate hydratase (molecular player: AcnB-family aconitate hydratases with methylisocitrate activity; activity or role: 2-methylisocitrate dehydratase activity)
      - AcnA-family hydration
        - AcnA-family 2-methylisocitrate hydratase (molecular player: AcnA-family aconitate hydratases with methylisocitrate activity; activity or role: 2-methylisocitrate dehydratase activity)
  - 5. carbon-carbon cleavage
  - 2-methylisocitrate cleavage
    - 2-methylisocitrate lyase (molecular player: PrpB 2-methylisocitrate lyases; activity or role: methylisocitrate lyase activity)

## Known Relationships Among Steps

- Propionate activation to propionyl-CoA feeds into 2-methylcitrate synthesis: Propionyl-CoA is the acyl donor for 2-methylcitrate synthesis.
- 2-methylcitrate synthesis feeds into Conversion of 2-methylcitrate to 2-methyl-cis-aconitate: 2-methylcitrate enters either dehydration implementation.
- Conversion of 2-methylcitrate to 2-methyl-cis-aconitate feeds into 2-methyl-cis-aconitate hydration: Both alternatives converge on 2-methyl-cis-aconitate.
- 2-methyl-cis-aconitate hydration feeds into 2-methylisocitrate cleavage: 2-methylisocitrate is the substrate cleaved by PrpB.
- AcnD-family 2-methylcitrate dehydration feeds into PrpF methylaconitate isomerization: The AcnD product is the substrate rearranged by PrpF.

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

# The 2-Methylcitrate Cycle: A Reusable Propionate-Assimilation Module

*A review-style synthesis for a molecular-biology audience*
*Iteration 1 — commissioned review*

---

## 1. Executive summary

The 2-methylcitrate cycle (2-MCC, also "methylcitrate cycle," MCC) is a compact
metabolic module that oxidizes propionate to pyruvate and succinate, thereby both
**assimilating** propionate as a carbon/energy source and **detoxifying**
propionyl-CoA, a broadly inhibitory acyl-CoA. It is the dominant aerobic route of
propionate catabolism in many bacteria and in fungi, and it operates as a
citric-acid-cycle "mimic": propionyl-CoA (rather than acetyl-CoA) is condensed with
oxaloacetate, and the resulting C7 tricarboxylate is processed by a series of
reactions structurally parallel to citrate → *cis*-aconitate → isocitrate, but
terminating in a carbon–carbon lyase step that regenerates a C4 (succinate) and
releases a C3 (pyruvate) (PMID 10482501; 12473114).

Five catalytic activities define the module: (1) **propionate activation** to
propionyl-CoA by a PrpE-family CoA ligase; (2) **condensation** of propionyl-CoA
with oxaloacetate to 2-methylcitrate by the citrate-synthase-family enzyme PrpC;
(3) **dehydration** of 2-methylcitrate to 2-methyl-*cis*-aconitate — implemented
either by the standalone, cofactorless dehydratase **PrpD**, or by the aconitase-like
**AcnD** working with the accessory isomerase **PrpF**; (4) **hydration** of
2-methyl-*cis*-aconitate to 2-methylisocitrate by a **housekeeping aconitase**
(AcnB or AcnA), not a dedicated enzyme; and (5) **cleavage** of 2-methylisocitrate to
succinate + pyruvate by the lyase **PrpB** (PMID 10482501; 11294638; 12473114;
29145506; 14575713).

The module's most important internal variation is at the dehydration step, where a
stereochemical mismatch between PrpD chemistry and aconitase chemistry dictates whether
an accessory isomerase (PrpF) is obligatory. Its most important external feature is that
it plugs into pre-existing central metabolism at two points — it borrows the general
aconitase for hydration and returns products directly to the TCA cycle and
gluconeogenesis. Because propionyl-CoA arises during infection (from host lipids,
amino acids, cholesterol, and gut microbiota), the cycle is a virulence determinant in
several pathogens and an attractive antimicrobial/antifungal target (PMID 17973657;
31504787). In humans there is **no** 2-MCC; the appearance of methylcitrate in human
biofluids is a pathological byproduct of propionic/methylmalonic acidemia, made by
citrate synthase, and must not be conflated with the microbial cycle (PMID 31451751).

---

## 2. Definition and biological boundaries

### 2.1 What is inside the module

The 2-MCC is defined by the transformation **propionate + oxaloacetate → pyruvate +
succinate**, carried out through a fixed set of intermediates:

```
propionate ─PrpE→ propionyl-CoA
propionyl-CoA + oxaloacetate ─PrpC→ (2S,3S)-2-methylcitrate
2-methylcitrate ─PrpD  OR  AcnD+PrpF→ 2-methyl-cis-aconitate
2-methyl-cis-aconitate ─aconitase (AcnB/AcnA)→ (2R,3S)-2-methylisocitrate
2-methylisocitrate ─PrpB→ succinate + pyruvate
```

Everything required to convert free propionate into two central-metabolic products
(pyruvate + succinate) belongs to the module. Oxaloacetate is consumed and succinate is
returned, so the module is catalytic in C4-dicarboxylate in the same sense that the TCA
cycle is catalytic in oxaloacetate: the net input is the propionyl unit, the net outputs
are pyruvate + CO2-equivalents once pyruvate is further oxidized.

### 2.2 What is adjacent but should be treated separately

- **The methylmalonyl-CoA pathway.** The other major propionate/propionyl-CoA route
  carboxylates propionyl-CoA (biotin-dependent propionyl-CoA carboxylase) to
  (S)-methylmalonyl-CoA and isomerizes it (adenosylcobalamin/B12-dependent
  methylmalonyl-CoA mutase) to succinyl-CoA. This is the route in mammalian
  mitochondria and in many bacteria; it is **B12-dependent and CO2-fixing**, whereas the
  2-MCC is **B12-independent and oxidative**. The two are alternative solutions to the
  same problem and should be kept distinct (PMID 42341992).

- **The TCA cycle and glyoxylate shunt.** The 2-MCC shares chemistry and even enzymes
  with these. The hydration step is done by the *same* aconitase that acts in the TCA
  cycle, and in *Pseudomonas aeruginosa* the glyoxylate-shunt isocitrate lyase (AceA)
  moonlights with 2-methylisocitrate lyase activity, linking the two cycles by
  enzymatic redundancy (PMID 40015638). These overlaps are real biology, but the
  glyoxylate shunt (acetyl-CoA anaplerosis) and TCA cycle (acetyl-CoA oxidation) are
  separate modules with separate purposes.

- **Human "methylcitrate" chemistry.** In humans, propionyl-CoA accumulating in
  propionic and methylmalonic acidemia is condensed with oxaloacetate by ordinary
  citrate synthase to form methylcitrate, which is excreted as a **biomarker**, not
  processed by a cycle (PMID 31451751; 16406646). There is no PrpD/PrpF/PrpB machinery
  in humans.

- **Regulatory and transport events.** The 2-methylcitrate *signal* (sensed by PrpR)
  and propionyl-CoA sensing (by the [4Fe4S]/CoA-binding PrpR of mycobacteria), as well
  as substrate transporters sometimes encoded in *prp* operons, are functionally linked
  but conceptually separate from the catalytic core (PMID 15528672; 31504787;
  41114503).

### 2.3 Competing definitions

The literature uses "2-methylcitric acid cycle," "2-methylcitrate cycle," and
"methylcitrate cycle" interchangeably. A subtler definitional split concerns the
**dehydration step**: some treatments describe a single "2-methylcitrate dehydratase"
activity, but mechanistically there are two non-homologous implementations (PrpD;
AcnD+PrpF) whose products are different aconitate isomers (PMID 29145506; 17567742).
A rigorous definition therefore treats "generation of 2-methyl-*cis*-aconitate" as a
*function* that can be filled by either implementation, and treats the aconitase
hydration as a **shared** step rather than a pathway-dedicated one.

---

## 3. Mechanistic overview

### 3.1 Step 1 — Propionate activation (PrpE)

Free propionate is activated to propionyl-CoA by an ATP-dependent propionyl-CoA
synthetase of the PrpE (acyl-CoA synthetase/AMP-forming) family. In *Salmonella*, PrpE
is encoded within the *prpBCDE* operon, but the cell also possesses **redundant**
propionyl-CoA-forming systems — acetyl-CoA synthetase (Acs) and the propionate
kinase/phosphotransacetylase (PduW/Pta) route — with different affinities that ensure
propionyl-CoA supply across a range of propionate concentrations (PMID 12700259).
PrpE activity is itself post-translationally controlled by reversible acetylation
(the CobB sirtuin/acetyltransferase system in *Salmonella*), tying activation to the
cell's acetylation/energy status (PMID 12700259; 9851993). Activation is **obligatory**:
all downstream chemistry operates on the CoA thioester.

### 3.2 Step 2 — 2-Methylcitrate synthesis (PrpC)

PrpC, a member of the citrate-synthase family, condenses the methylene carbon of
propionyl-CoA with the carbonyl of oxaloacetate to give (2S,3S)-2-methylcitrate. PrpC
enzymes are typically **bifunctional**, retaining citrate synthase activity, but kinetic
analysis shows propionyl-CoA is the preferred substrate (PMID 10482501). This step is
**obligatory and committing**: it defines the C7 methyl-branched tricarboxylate that the
rest of the module processes, and its product (2-methylcitrate) is the physiological
inducer of the pathway (Section 4.6).

### 3.3 Step 3 — Dehydration to 2-methyl-cis-aconitate (PrpD, or AcnD + PrpF)

This is the mechanistically richest and most variable step, and it exists in two
alternative implementations that converge on the same product, 2-methyl-*cis*-aconitate:

- **Direct PrpD route.** PrpD is a **cofactorless** dehydratase — no iron–sulfur
  cluster, no metal, no reducing agent — unrelated in sequence to aconitases (PMID
  11294638). It removes water from (2S,3S)-2-methylcitrate by an **unusual *syn*
  elimination** to give *cis*-2-methylaconitate (Km ≈ 440 µM), and can also weakly
  hydrate *cis*-aconitate (~5-fold slower) (PMID 12473114). Crucially, PrpD does **not**
  hydrate 2-methyl-*cis*-aconitate to 2-methylisocitrate — that job belongs to the
  aconitase (PMID 11294638). PrpD belongs to the "MmgE/PrpD" family.

- **Two-component AcnD/PrpF route.** Many bacteria (e.g., *Shewanella oneidensis*)
  lack *prpD* and instead use **AcnD**, an aconitase-like (Fe-S) 2-methylcitrate
  dehydratase, together with **PrpF**. AcnD dehydrates 2-methylcitrate but yields a
  **different** 2-methylaconitate isomer (evidence points to 4-methylaconitate) that is
  **not** a substrate for the housekeeping aconitase. **PrpF**, a non-PLP isomerase
  structurally similar to diaminopimelate epimerase/proline racemase (with a catalytic
  Lys73 and Cys107), isomerizes the AcnD product into 2-methyl-*cis*-aconitate — the
  same isomer PrpD makes and the one aconitase accepts (PMID 17567742; 29145506).
  AcnD+PrpF fully complement a *Salmonella prpD* mutant, and PrpF is **obligatory** in
  this route (PrpD-using bacteria do not need PrpF) (PMID 29145506).

The deep reason two implementations exist is **stereochemistry**: PrpD performs a *syn*
elimination while aconitase adds water *anti*; the AcnD reaction produces the "wrong"
geometric isomer, which is why an accessory isomerase is required to feed the shared
aconitase step (PMID 12473114; 29145506).

### 3.4 Step 4 — Hydration to 2-methylisocitrate (housekeeping aconitase, AcnB/AcnA)

The 2-methyl-*cis*-aconitate is hydrated to (2R,3S)-2-methylisocitrate by a
**general-purpose aconitase**, not a pathway-dedicated enzyme. In *E. coli*, AcnB was
purified from propionate-grown cells as the physiological 2-methylaconitate hydratase
(Km ≈ 210 µM for 2-methylisocitrate; no activity on 2-methylcitrate) (PMID 12473114).
In *Salmonella*, AcnA hydrates 2-methyl-*cis*-aconitate in vitro, yet *acnA* deletion
does not block growth on propionate because AcnB provides redundant activity (PMID
11294638). Thus the module **borrows** an existing TCA-cycle activity for this step —
an important boundary point, because the aconitase is shared with, and regulated by,
central carbon/iron metabolism.

### 3.5 Step 5 — Carbon–carbon cleavage (PrpB)

PrpB, a 2-methylisocitrate lyase, cleaves (2R,3S)-2-methylisocitrate into **succinate +
pyruvate** in a Mg²⁺-dependent aldol-retro-cleavage reaction. Its crystal structures
(from *E. coli* and *Salmonella*) place it in the isocitrate-lyase/PEP-mutase
superfamily; the active site binds pyruvate and Mg²⁺, with a mobile "active-site loop"
that closes over the substrate, and subtle pocket differences rationalize why PrpB
prefers 2-methylisocitrate while the related isocitrate lyase prefers isocitrate (PMID
14575713). This step is **obligatory and defines the outputs**; succinate re-enters the
TCA cycle and pyruvate enters central metabolism/gluconeogenesis.

### 3.6 Obligatory vs. conditional vs. accessory

- **Obligatory (core):** PrpE-type activation (or an equivalent propionyl-CoA source),
  PrpC condensation, a dehydration implementation, aconitase hydration, PrpB cleavage.
- **Conditional (implementation-dependent):** PrpF is required **only** in the
  AcnD-dependent route; PrpD and AcnD are mutually exclusive alternatives.
- **Accessory / context-dependent:** the choice of propionyl-CoA source (PrpE vs.
  Acs vs. PduW-Pta), CoA-transferase-based detoxification bypasses (fungi), transporters
  co-encoded in *prp* operons, and the regulatory proteins (PrpR).

---

## 4. Major molecular players and active assemblies

| Step | Enzyme / player | Family / fold | Cofactor | Notes |
|------|-----------------|---------------|----------|-------|
| Activation | **PrpE** propionyl-CoA synthetase | AMP-forming acyl-CoA synthetase | ATP, Mg²⁺ | Redundant with Acs, PduW/Pta; regulated by acetylation (CobB) (PMID 12700259) |
| Condensation | **PrpC** 2-methylcitrate synthase | Citrate-synthase family | none | Bifunctional (citrate + methylcitrate synthase); prefers propionyl-CoA (PMID 10482501) |
| Dehydration (route A) | **PrpD** 2-methylcitrate dehydratase | MmgE/PrpD family | **none** (cofactorless) | *syn* elimination; no Fe-S; does not hydrate the product (PMID 11294638; 12473114) |
| Dehydration (route B) | **AcnD** + **PrpF** | AcnD: aconitase-like (Fe-S); PrpF: DAP-epimerase/proline-racemase fold | AcnD: [Fe-S]; PrpF: none | AcnD makes wrong isomer; PrpF (Lys73, Cys107) isomerizes to 2-methyl-*cis*-aconitate (PMID 17567742; 29145506) |
| Hydration | **AcnB / AcnA** aconitase | Aconitase (Fe-S) | [4Fe-4S] | Housekeeping TCA enzyme; redundant AcnA/AcnB (PMID 12473114; 11294638) |
| Cleavage | **PrpB** 2-methylisocitrate lyase | Isocitrate-lyase/PEP-mutase superfamily | Mg²⁺ | Products succinate + pyruvate; mobile active-site loop (PMID 14575713) |

### 4.6 Regulatory assemblies (adjacent but tightly coupled)

- **PrpR (σ54/bEBP type, γ-proteobacteria).** A σ54-dependent enhancer-binding
  activator that senses **2-methylcitrate** (not propionate or citrate) as coactivator;
  it requires RpoN (σ54/NtrA) and IHF to activate the *prpBCDE* promoter (PMID 15528672;
  10648513). Because PrpC must make 2-methylcitrate before the operon is induced, a small
  basal propionyl-CoA pool (from Acs/PduW-Pta) is needed to prime the system — a
  feed-forward logic (PMID 12700259; 9851993).
- **PrpR (Mycobacterium tuberculosis).** A structurally distinct transcription factor
  that binds CoA/short-chain acyl-CoAs and carries a **[4Fe4S] cluster**; it activates
  *prpC*/*prpD* during cholesterol catabolism. The cluster is stable (probably an
  iron/nutrient sensor rather than a redox sensor) (PMID 31504787).

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across bacterial lineages

- **γ-Proteobacteria (E. coli, Salmonella).** Canonical *prpBCDE* operon; PrpD route;
  hydration by AcnB (with redundant AcnA); σ54/PrpR/IHF regulation (PMID 10482501;
  10648513; 12473114).
- **AcnD/PrpF users (e.g., Shewanella).** Replace *prpD* with *acnD* + *prpF*; obligate
  isomerase requirement (PMID 29145506).
- **Actinobacteria (Corynebacterium glutamicum).** Two paralogous *prpDBC* clusters
  (*prpD1B1C1*, *prpD2B2C2*); the *prpD2B2C2* cluster is the propionate-induced,
  physiologically relevant one; PrpC1/PrpC2 are both active citrate/methylcitrate
  synthases (PMID 11976302).
- **Mycobacterium tuberculosis.** MCC is up-regulated to detoxify propionyl-CoA
  generated by **cholesterol** catabolism during infection; controlled by the
  [4Fe4S]/acyl-CoA-sensing PrpR — a key host-adaptation circuit (PMID 31504787).
- **Pseudomonas aeruginosa.** MCC is functionally interwoven with the glyoxylate shunt;
  isocitrate lyase (AceA) supplies secondary 2-methylisocitrate lyase activity, an
  example of cross-pathway enzymatic redundancy (PMID 40015638).
- **Acetic-acid bacteria (Acetobacter).** *prp* clusters frequently **lack a dedicated
  prpE**, recruiting a PrpE-homologous acetyl-CoA synthetase (*prpE′*) into the operon;
  growth on propionate requires PrpB, PrpC and PrpD (PMID 42271202).
- **Neisseria meningitidis.** The *prp* operon includes a transporter for
  α-ketobutyrate, and the pathway balances propionate **assimilation vs. detoxification**
  depending on the host microenvironment and co-substrate (PMID 41114503).

### 5.2 Fungi

Filamentous fungi run the MCC to detoxify propionyl-CoA arising from amino acids
(Val/Ile/Met), odd-chain fatty acids, and propionate. Genetic proof exists for
*Aspergillus nidulans* and *A. fumigatus*, and for pathogenic *Fusarium* species
(PMID 19661181; 16008561). Fungal methylcitrate synthase (**mcsA**) is the pivotal
enzyme: its deletion causes propionyl-CoA accumulation, blocks polyketide synthesis and
conidial pigmentation, and directly inhibits the **pyruvate dehydrogenase complex**
(PMID 16008561). Fungi possess an additional **CoA-transferase** detoxification bypass
that transfers CoASH from propionyl-CoA to acetate, relieving toxicity independently of
the cycle (PMID 18331473). MCC is a **virulence factor**: *A. fumigatus mcsA* mutants
are attenuated in murine invasive aspergillosis and cleared by the host, marking the
cycle as an antifungal target (PMID 17973657). MCC activation also remodels the cell
wall and increases oxidative stress in *Histoplasma capsulatum* (PMID 40023528).

### 5.3 Compartmentalization

In fungi (and by analogy in eukaryotic MCC-bearing lineages) propionyl-CoA metabolism
and the MCC are associated with the **mitochondrion**, co-localized with the source of
oxaloacetate and the TCA machinery. In bacteria the module is cytoplasmic. The
compartment dictates substrate access (oxaloacetate, CoA pools) and coupling to
respiration.

### 5.4 Humans and mammals — a boundary, not a variant

Mammals do **not** operate the 2-MCC; they use the B12-dependent methylmalonyl-CoA
route. When that route fails (propionic/methylmalonic acidemia), propionyl-CoA
accumulates and citrate synthase produces **methylcitrate**, a diagnostic biomarker and
a toxic metabolite that inhibits TCA and urea-cycle enzymes — but the downstream
PrpD/aconitase/PrpB steps do not exist in humans (PMID 31451751; 16406646; 32451238).

---

## 6. Constraints, dependencies, and failure modes

### 6.1 Ordering constraints

The chemistry enforces a strict order: activation → condensation → dehydration →
hydration → cleavage. Each enzyme's substrate is the previous enzyme's product, and the
intermediates are not interconvertible by other routes. The **dehydration–hydration
pair** is a formal dehydration/rehydration (as in citrate → isocitrate via aconitate)
that repositions the hydroxyl to make the C–C bond cleavable by PrpB.

### 6.2 Stereochemical/isomer constraints (mutual exclusivity)

- Aconitase hydrates only 2-methyl-*cis*-aconitate; it is inactive on the AcnD product.
  Therefore AcnD **cannot** function without PrpF (PMID 29145506).
- PrpD and AcnD are **mutually exclusive** implementations of the same step; genomes
  carry one or the other, and PrpF co-occurs with AcnD, not with PrpD (PMID 17567742).
- AcnB hydrates 2-methyl-*cis*-aconitate but shows no activity on 2-methylcitrate;
  substrate specificity is strict (PMID 12473114).

### 6.3 Regulatory dependency (feed-forward)

The *prpBCDE* operon is induced by 2-methylcitrate, which can only be made by PrpC from
propionyl-CoA. So a **basal propionyl-CoA supply** (Acs, PduW/Pta) is a prerequisite to
switch on the full operon — a chicken-and-egg dependency the cell resolves with
redundant activation systems (PMID 12700259; 9851993). In mycobacteria the analogous
switch is an acyl-CoA/[4Fe4S] sensor (PMID 31504787).

### 6.4 Failure modes

- **Loss of the cycle → propionyl-CoA toxicity.** Blocking PrpC/mcsA causes
  propionyl-CoA accumulation that inhibits pyruvate dehydrogenase, polyketide synthesis,
  growth, and (in pathogens) virulence (PMID 16008561; 17973657).
- **Metabolic imbalance from intermediate accumulation.** Accumulated 2-methylcitrate
  itself is inhibitory/imbalancing (PMID 41684677; and, in the human analogue,
  methylcitrate inhibits TCA/urea-cycle enzymes, PMID 16406646).
- **Redundancy buffers single losses.** *acnA* loss is masked by AcnB; *prpB* loss can
  be partly covered by AceA in *P. aeruginosa*; missing *prpE* is covered by *prpE′*/Acs
  (PMID 11294638; 40015638; 42271202). This redundancy is a robustness feature but
  complicates single-gene knockout interpretation.

---

## 7. Controversies and open questions

1. **Identity of the AcnD product.** The AcnD reaction yields a 2-methylaconitate isomer
   that is not an aconitase substrate; indirect evidence (in vivo/in vitro, PrpF
   requirement) points to **4-methylaconitate**, but the precise structure/stereochemistry
   has been inferred rather than directly determined for every system (PMID 29145506).
2. **Which aconitase does the hydration in vivo.** In *E. coli* it is AcnB; in
   *Salmonella* AcnA is competent but AcnB provides redundancy — the physiological split
   between AcnA and AcnB, and how iron/oxidative status shifts it, is not fully resolved
   (PMID 12473114; 11294638).
3. **Boundaries between the MCC and the glyoxylate shunt.** The AceA/PrpB and
   AcnA/AcnB overlaps show the "cycle" is not cleanly separable from central metabolism;
   how flux is partitioned under infection-relevant conditions is an open,
   organism-specific question (PMID 40015638).
4. **Cross-organism extrapolation.** Much mechanistic detail comes from a few models
   (*Salmonella*, *E. coli*, *Shewanella*, *Aspergillus*). Whether kinetic and
   stereochemical conclusions transfer to actinobacteria, acetic-acid bacteria, and
   diverse fungi is often assumed rather than demonstrated (PMID 11976302; 42271202).
5. **Regulatory diversity.** The σ54/PrpR (γ-proteobacteria) and [4Fe4S]/acyl-CoA
   PrpR (mycobacteria) are unrelated solutions to sensing propionate flux; the full range
   of MCC regulatory logic across lineages (and nitrogen/GlnR control) is incompletely
   mapped (PMID 15528672; 31504787; 30745367).
6. **Therapeutic targeting.** Because the MCC is essential for virulence in
   *A. fumigatus* and important in *M. tuberculosis* cholesterol catabolism yet absent in
   humans, its enzymes (PrpC/mcsA, PrpB, PrpD) are candidate drug targets; selective
   inhibitors and resistance via redundancy remain to be worked out (PMID 17973657;
   31504787).

---

## 8. Key references

- Horswill AR, Escalante-Semerena JC. *Salmonella typhimurium* LT2 catabolizes propionate
  via the 2-methylcitric acid cycle. **PMID 10482501** (1999).
- Horswill AR, Escalante-Semerena JC. In vitro conversion of propionate to pyruvate:
  PrpD and aconitase. **PMID 11294638** (2001).
- Brock M et al. Oxidation of propionate to pyruvate in *E. coli*: methylcitrate
  dehydratase and aconitase (AcnB); *syn*/*anti* stereochemistry. **PMID 12473114** (2002).
- Garvey GS et al. Crystal structure of PrpF (*Shewanella*): a non-PLP isomerase.
  **PMID 17567742** (2007).
- Rocco CJ et al. PrpF isomerizes 2-methyl-*cis*-aconitate in the AcnD-dependent 2-MCC;
  AcnD product likely 4-methylaconitate. **PMID 29145506** (2017).
- Simanshu DK et al. Crystal structure of *Salmonella* PrpB (2-methylisocitrate lyase)
  with pyruvate/Mg²⁺. **PMID 14575713** (2003).
- Palacios L, Escalante-Semerena JC. PrpR senses 2-methylcitrate. **PMID 15528672** (2004).
- Palacios L, Escalante-Semerena JC. prpR, ntrA (σ54), ihf required for *prpBCDE*
  expression. **PMID 10648513** (2000).
- Palacios L et al. Propionyl-CoA is the common intermediate; redundant activation
  systems. **PMID 12700259** (2003).
- Tsang AW et al. Regulation integrating 1,2-propanediol and propionate catabolism.
  **PMID 9851993** (1998).
- Claes WA et al. Two *prpDBC* clusters in *Corynebacterium glutamicum*. **PMID 11976302** (2002).
- Maerker C et al. *A. fumigatus* methylcitrate synthase; propionyl-CoA inhibits PDH and
  polyketide synthesis. **PMID 16008561** (2005).
- Ibrahim-Granet O et al. Methylcitrate synthase essential for invasive aspergillosis.
  **PMID 17973657** (2008).
- Fleck CB, Brock M. CoA-transferase detoxification of propionyl-CoA in *A. nidulans*.
  **PMID 18331473** (2008).
- Domin N et al. Functional MCC in *Fusarium*. **PMID 19661181** (2009).
- Tang J et al. *M. tuberculosis* PrpR: [4Fe4S]/acyl-CoA-sensing transcription factor.
  **PMID 31504787** (2019).
- Wijaya F et al. MCC and glyoxylate cycle linked by enzymatic redundancy in
  *P. aeruginosa* (AceA secondary 2-MIC lyase). **PMID 40015638** (2025).
- Talà A et al. Methylcitrate pathway balancing assimilation/detoxification in
  meningococci; α-ketobutyrate transporter. **PMID 41114503** (2025).
- Yang B et al. *prp* operon in *Acetobacter pasteurianus*; prpE′ recruitment.
  **PMID 42271202** (2026).
- Santos LPA et al. Propionate/MCC in *Histoplasma capsulatum*. **PMID 40023528** (2025).
- Al-Dirbashi OY et al. Methylcitrate/citrate ratio as biomarker of inborn propionate
  errors (human, non-cyclic). **PMID 31451751** (2019).
- Filipowicz HR et al. Metabolic changes in propionic acidemia (human methylcitrate).
  **PMID 16406646** (2006).

---

### Uncertainty statement

Mechanistic conclusions on PrpD/AcnD/PrpF stereochemistry and aconitase involvement rest
chiefly on *E. coli*, *Salmonella*, and *Shewanella*; fungal MCC on *Aspergillus* and
*Fusarium*. The exact structure of the AcnD product, the in-vivo AcnA/AcnB partition, and
the flux boundary with the glyoxylate shunt are inferred or organism-specific. Human
"methylcitrate" is a pathological citrate-synthase product, **not** evidence of a 2-MCC in
mammals. Claims here should not be uniformly extrapolated across all lineages.


## Artifacts

- [OpenScientist final report](methylcitrate_cycle-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](methylcitrate_cycle-deep-research-openscientist_artifacts/final_report.pdf)