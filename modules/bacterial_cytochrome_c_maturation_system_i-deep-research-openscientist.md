---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T12:31:51.668794'
end_time: '2026-09-01T13:08:34.002561'
duration_seconds: 2202.33
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial cytochrome c maturation system I
  module_summary: A reusable bacterial module for covalent attachment of heme to exported
    c-type cytochrome apoproteins by the Ccm (system I) machinery. The module comprises
    CcmABCD-dependent heme handling, covalent loading of the CcmE heme chaperone,
    reductive preparation of apocytochrome CXXCH motifs, and CcmF/CcmH-dependent heme
    ligation, with lineage-variable CycH-family factors supporting maturation by a
    molecular mechanism that remains unresolved. General Sec export of apocytochromes
    and upstream DsbD electron delivery are external dependencies rather than parts
    of this module.
  module_outline: "- Bacterial cytochrome c maturation system I\n  - 1. membrane-associated\
    \ heme handling and delivery to CcmE\n  - CcmABCD heme-handling complex\n    -\
    \ CcmA ATPase (molecular player: CcmA heme-export ATPases; activity or role: ATP\
    \ hydrolysis activity)\n    - CcmB membrane subunit (molecular player: CcmB heme-export\
    \ membrane proteins)\n    - CcmC heme-handling subunit (molecular player: CcmC\
    \ cytochrome-c biogenesis proteins; activity or role: heme binding)\n    - CcmD\
    \ accessory membrane subunit (molecular player: CcmD heme-export proteins)\n \
    \ - 2. covalent heme chaperoning by CcmE\n  - CcmE heme chaperone loading\n  \
    \  - CcmE heme chaperone (molecular player: CcmE heme chaperones; activity or\
    \ role: heme binding)\n  - 3. reductive preparation of apocytochrome heme-binding\
    \ motifs\n  - CcmG/CcmH apocytochrome redox preparation\n    - CcmG periplasmic\
    \ thioredoxin (molecular player: CcmG/DsbE thioredoxin family; activity or role:\
    \ disulfide oxidoreductase activity)\n    - CcmH redox/assembly component (molecular\
    \ player: CcmH cytochrome-c maturation proteins)\n  - 4. heme ligation and accessory\
    \ CycH function\n  - CcmF-centered ligation machinery with CycH accessory\n  \
    \  - CcmF holocytochrome-c synthetase component (molecular player: CcmF cytochrome-c\
    \ maturation proteins; activity or role: heme binding)\n    - CycH-family accessory\
    \ component (molecular player: CycH cytochrome-c maturation proteins)"
  module_connections: '- CcmABCD heme-handling complex precedes CcmE heme chaperone
    loading

    - CcmE heme chaperone loading precedes CcmF-centered ligation machinery with CycH
    accessory

    - CcmG/CcmH apocytochrome redox preparation feeds into CcmF-centered ligation
    machinery with CycH accessory

    - CcmG periplasmic thioredoxin feeds into CcmH redox/assembly component'
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_cytochrome_c_maturation_system_i-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_cytochrome_c_maturation_system_i-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial cytochrome c maturation system I

## Working Scope

A reusable bacterial module for covalent attachment of heme to exported c-type cytochrome apoproteins by the Ccm (system I) machinery. The module comprises CcmABCD-dependent heme handling, covalent loading of the CcmE heme chaperone, reductive preparation of apocytochrome CXXCH motifs, and CcmF/CcmH-dependent heme ligation, with lineage-variable CycH-family factors supporting maturation by a molecular mechanism that remains unresolved. General Sec export of apocytochromes and upstream DsbD electron delivery are external dependencies rather than parts of this module.

## Provisional Biological Outline

- Bacterial cytochrome c maturation system I
  - 1. membrane-associated heme handling and delivery to CcmE
  - CcmABCD heme-handling complex
    - CcmA ATPase (molecular player: CcmA heme-export ATPases; activity or role: ATP hydrolysis activity)
    - CcmB membrane subunit (molecular player: CcmB heme-export membrane proteins)
    - CcmC heme-handling subunit (molecular player: CcmC cytochrome-c biogenesis proteins; activity or role: heme binding)
    - CcmD accessory membrane subunit (molecular player: CcmD heme-export proteins)
  - 2. covalent heme chaperoning by CcmE
  - CcmE heme chaperone loading
    - CcmE heme chaperone (molecular player: CcmE heme chaperones; activity or role: heme binding)
  - 3. reductive preparation of apocytochrome heme-binding motifs
  - CcmG/CcmH apocytochrome redox preparation
    - CcmG periplasmic thioredoxin (molecular player: CcmG/DsbE thioredoxin family; activity or role: disulfide oxidoreductase activity)
    - CcmH redox/assembly component (molecular player: CcmH cytochrome-c maturation proteins)
  - 4. heme ligation and accessory CycH function
  - CcmF-centered ligation machinery with CycH accessory
    - CcmF holocytochrome-c synthetase component (molecular player: CcmF cytochrome-c maturation proteins; activity or role: heme binding)
    - CycH-family accessory component (molecular player: CycH cytochrome-c maturation proteins)

## Known Relationships Among Steps

- CcmABCD heme-handling complex precedes CcmE heme chaperone loading
- CcmE heme chaperone loading precedes CcmF-centered ligation machinery with CycH accessory
- CcmG/CcmH apocytochrome redox preparation feeds into CcmF-centered ligation machinery with CycH accessory
- CcmG periplasmic thioredoxin feeds into CcmH redox/assembly component

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

# Bacterial Cytochrome *c* Maturation System I (Ccm): A Review-Style Synthesis

*Commissioned review-style synthesis. Search date: 2026-09-01. Primary literature accessed via PubMed.*

---

## 1. Executive Summary

Bacterial cytochrome *c* maturation system I (the **Ccm** system) is a periplasmic, membrane-embedded post-translational machine that solves a chemically demanding problem: the stereospecific formation of two covalent thioether bonds between the vinyl groups of heme (Fe-protoporphyrin IX) and the two cysteine thiols of a **CXXCH** motif in a Sec-exported apocytochrome. Because heme attachment occurs on the far side of the membrane from where heme is synthesized, and because the periplasm is an oxidizing environment while thioether ligation requires reduced substrate thiols and controlled heme-iron chemistry, the cell has evolved a multi-protein relay that traffics heme across the membrane, holds it covalently on a dedicated chaperone, keeps the apoprotein cysteines reduced, and finally catalyzes ligation. The system, encoded by *ccmABCDEFGH* (plus lineage-variable CycH/CcmI factors), is found in α-, β-, γ-, δ-, and ε-proteobacteria, in plant and protozoan mitochondria, and in modified form in archaea.

The central, defining feature of system I — and the feature that most cleanly distinguishes it from the parallel systems II (CcsBA) and III (HCCS) — is the **covalent heme chaperone CcmE**, which binds heme through a covalent bond to a conserved histidine (His130 in *Escherichia coli*) as an obligatory holo-intermediate. Our synthesis of the literature supports a two-phase model. In **phase 1**, the ABC-transporter-like complex **CcmABCD** binds heme at CcmC, uses ATP hydrolysis at CcmA to drive covalent loading of heme onto CcmE, and then releases oxidized (Fe³⁺) holoCcmE. In **phase 2**, holoCcmE docks onto the **CcmF/CcmH** cytochrome *c* synthase via WWD-domain histidines, where the heme iron is re-reduced to Fe²⁺ and ligated to the CXXCH motif. Running in parallel is a **reductive branch** — DsbD → CcmG → CcmH — that delivers cytoplasmic reducing power to keep the apocytochrome cysteines reduced. Lineage-variable **CycH-family proteins (CcmI)** act as TPR-domain apocytochrome chaperones that recognize and present the substrate to the synthase.

Seven findings anchor this review: (F001) the obligatory covalent His-heme CcmE intermediate; (F002) holoCcmE-to-CcmF heme handoff via WWD histidines; (F003) the requirement for CcmAB ATP hydrolysis at the CcmE loading/release step; (F004) the DsbD→CcmG→CcmH reductive branch; (F005) cryo-EM localization of the ATP site to CcmA and the heme site to CcmC; (F006) heme-iron redox control (Fe³⁺ release, Fe²⁺ re-reduction before ligation); and (F007) CcmI/CycH as a TPR-domain apocytochrome chaperone. Major open questions concern the atomic mechanism of heme hand-off between successive WWD platforms, the electron source and catalytic role of CcmF at the ligation step, and the stoichiometry and hand-off geometry of the CycH/CcmI chaperones.

---

## 2. Definition and Biological Boundaries

### What is included

System I is a **reusable maturation module** whose input is an unfolded, Sec-exported apocytochrome bearing one or more CXXCH heme-binding motifs, plus heme delivered from the cytoplasmic side, and whose output is a folded holocytochrome *c* with covalently attached heme. The module comprises four functional sub-steps:

1. **Membrane-associated heme handling and delivery to CcmE** — the CcmABCD complex (CcmA ATPase, CcmB membrane subunit, CcmC heme-handling subunit, CcmD accessory subunit).
2. **Covalent heme chaperoning by CcmE** — loading of heme onto the CcmE histidine as a covalent holo-intermediate.
3. **Reductive preparation of the apocytochrome CXXCH motif** — CcmG (periplasmic thioredoxin) and CcmH (CXXC redox/assembly component).
4. **Heme ligation and accessory CycH function** — the CcmF holocytochrome *c* synthetase working with CcmH and the CycH-family (CcmI) apocytochrome chaperone.

### What lies outside the module (boundary conditions)

Two upstream processes are **external dependencies rather than parts of the module**:

- **General Sec-dependent export** of the apocytochrome across the inner membrane. The apoprotein must be delivered to the periplasm before maturation; the Sec translocon is not a Ccm component.
- **DsbD-mediated transmembrane electron delivery.** DsbD is the conduit that transfers reducing equivalents from cytoplasmic thioredoxin to the periplasm ([PMID: 19004826](https://pubmed.ncbi.nlm.nih.gov/19004826/)). It is a shared resource that also serves oxidative protein folding (DsbC/DsbG), so it is best treated as an input to the module rather than a dedicated part of it. CcmG, by contrast, is dedicated to Ccm and is treated as internal.

### Neighboring pathways often confused with system I

- **System II (Ccs / CcsBA):** an unrelated cytochrome *c* synthase found in Gram-positive bacteria, cyanobacteria, and chloroplasts. It attaches heme to CXXCH without a covalent CcmE intermediate, transporting heme through a channel in the CcsBA complex to an external active site ([PMID: 37827288](https://pubmed.ncbi.nlm.nih.gov/37827288/)). It converges on the same chemistry by different molecular means.
- **System III (HCCS):** the single-protein holocytochrome *c* synthase of the mitochondrial intermembrane space in animals, fungi, and some protists — mechanistically and evolutionarily distinct.
- **The Dsb oxidative-folding network (DsbA/DsbB):** shares the periplasmic thiol-redox chemistry and the DsbD conductor, but performs disulfide *bond formation*, the opposite redox logic from the reductive Ccm branch. The two pathways are kinetically insulated ([PMID: 15057279](https://pubmed.ncbi.nlm.nih.gov/15057279/)).

### Competing definitions in the literature

The most consequential definitional variation concerns whether **CcmH and CycH/CcmI are one protein or two**, and whether **CcmE is "canonical" (His-based) or variant**. In many γ-proteobacteria (*E. coli*), CcmH is a discrete CXXC redox protein and CcmI/CycH is separate; in α-proteobacteria such as *Rhodobacter*, functionally analogous activities can be distributed differently across fused or split polypeptides. A "system I*" variant uses a **cysteine-based CcmE** (CxxxY motif) instead of the canonical His-based CcmE (HxxxY), and in archaea and some bacteria this variant CcmE is accompanied by **loss of CcmH** ([PMID: 16920107](https://pubmed.ncbi.nlm.nih.gov/16920107/)). These are genuine, well-supported alternative architectures rather than annotation artifacts.

---

## 3. Mechanistic Overview

The best-supported current model is a **directed relay of external-facing (periplasmic) WWD heme platforms**, coupled to ATP-driven loading/release and to strict heme-iron redox control. The sequence of events:

```
 Cytoplasm  |  Inner Membrane  |            Periplasm
            |                  |
   heme --->|===== CcmABCD ====|  CcmC(heme site) --ATP(CcmA)--> covalent load
            |                  |          |
            |                  |          v
            |                  |   holoCcmE (His130~heme, Fe3+)   [PHASE 1]
            |                  |          | release requires ATP hydrolysis
            |                  |          v
   e- (Trx) |=== DsbD ===>CcmG=|=> CcmH (CXXC) --reduces--> apoCyt CXXCH thiols
            |                  |          |                         |
            |                  |          v                         v
            |                  |   holoCcmE docks CcmF (P-His1/2, WWD)  [PHASE 2]
            |                  |          | Fe3+ --> Fe2+ re-reduction
            |                  |          v
            |                  |   CcmF/CcmH synthase + CcmI(TPR) chaperone
            |                  |          |
            |                  |          v
            |                  |   HOLOCYTOCHROME c (2 thioethers to CXXCH)
```

**Phase 1 — heme handling and covalent CcmE loading (obligatory).** Heme is bound at the CcmC subunit of the CcmABCD complex. Cryo-EM structures place the ATP-binding site in CcmA and the heme-binding site in CcmC ([PMID: 36307425](https://pubmed.ncbi.nlm.nih.gov/36307425/)). CcmABCD behaves as an ABC transporter that uses the energy of ATP hydrolysis not for classical substrate import but to transfer heme from CcmC to CcmE and to release the resulting holoCcmE. The heme becomes covalently bonded to a histidine of CcmE (His130 in *E. coli*, within a conserved HxxxY motif); this holo-CcmE is released carrying heme in the **oxidized Fe³⁺ state** ([PMID: 19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/)).

**Phase 2 — heme ligation (obligatory).** Released holoCcmE must first dissociate from CcmABCD before it can interact with CcmF; the holo-form binds CcmF at least 20-fold more strongly than apoCcmE, and the heme is coordinated by two conserved periplasmic histidines (P-His1, P-His2) in the WWD domain of CcmF ([PMID: 24513106](https://pubmed.ncbi.nlm.nih.gov/24513106/)). At the synthase, the heme iron is **re-reduced to Fe²⁺** by CcmFH prior to thioether ligation to the CXXCH motif ([PMID: 19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/)).

**Parallel reductive branch (conditional/supporting).** The apocytochrome CXXCH cysteines must be reduced for ligation. CcmH carries a periplasmic CXXC motif whose cysteines are both required aerobically and whose deficiency is chemically rescued by exogenous thiol, consistent with a role keeping the heme-binding site reduced ([PMID: 9914305](https://pubmed.ncbi.nlm.nih.gov/9914305/)). Reducing power flows from cytoplasmic thioredoxin through DsbD to CcmG (a periplasmic thioredoxin-family protein) and onward to CcmH ([PMID: 19004826](https://pubmed.ncbi.nlm.nih.gov/19004826/)).

**Accessory apocytochrome chaperoning (accessory/lineage-variable).** CycH-family proteins (CcmI) recognize and bind the apocytochrome via a TPR domain and exhibit general chaperone activity, presenting the unfolded substrate to the synthase ([PMID: 23648553](https://pubmed.ncbi.nlm.nih.gov/23648553/), [PMID: 17122341](https://pubmed.ncbi.nlm.nih.gov/17122341/)).

### Obligatory vs. conditional vs. accessory steps

| Step | Player(s) | Classification | Basis |
|---|---|---|---|
| Heme binding at CcmC | CcmC (heme site) | **Obligatory** | Cryo-EM heme site in CcmC (F005) |
| ATP hydrolysis for CcmE loading/release | CcmA/CcmB | **Obligatory** | K40D abolishes biogenesis (F003) |
| Covalent His-heme CcmE intermediate | CcmE | **Obligatory (committed checkpoint)** | H130A abolishes holoCcmE (F001) |
| holoCcmE → CcmF handoff | CcmF WWD P-His1/2 | **Obligatory** | 20-fold holo preference (F002) |
| Fe³⁺→Fe²⁺ re-reduction | CcmF/CcmH | **Obligatory** | Two-step redox model (F006) |
| CXXCH thiol reduction | DsbD→CcmG→CcmH | **Conditional (aerobic)** | Thiol rescue of CcmH (F004) |
| Apocytochrome chaperoning | CycH/CcmI (TPR) | **Accessory / lineage-variable** | CcmI chaperone activity (F007) |

---

## 4. Key Findings and Major Molecular Players

### F001 — CcmE forms a covalent His-heme bond as an obligatory holo-intermediate

The single most diagnostic feature of system I is that heme is carried on a dedicated chaperone through a **covalent bond**, not a non-covalent pocket. In *E. coli* CcmE, His130 (in a conserved HxxxY motif) forms a covalent bond to a heme vinyl group; the chaperone then transfers heme **stereospecifically** to the apocytochrome ([PMID: 19178152](https://pubmed.ncbi.nlm.nih.gov/19178152/)). Mutation of His130 to alanine abolishes holoCcmE and cytochrome *c* formation, and alanine insertions near His130 abolish holoCcmE without perturbing the fold — defining a discrete heme pocket and establishing the covalent bond as a **committed checkpoint** in the pathway.

Remarkably, an **H130C variant still forms a covalent heme bond**, which is the mechanistic basis of the "system I*" variant ([PMID: 12657624](https://pubmed.ncbi.nlm.nih.gov/12657624/)). Resonance Raman studies of non-covalent heme binding illuminate the trigger: His130 ligates the iron in the ferric state, whereas two other residues ligate the iron in the ferrous form, freeing His130 to attack the vinyl group. A change in ligation, sensitive to heme-iron oxidation state, thus acts as the trigger for covalent bond formation ([PMID: 16373344](https://pubmed.ncbi.nlm.nih.gov/16373344/)).

> *"…requires the participation of the heme chaperone CcmE that binds heme covalently via a His residue (H130 in Escherichia coli) before transferring it stereospecifically to the apo form of cytochromes c"* ([PMID: 19178152](https://pubmed.ncbi.nlm.nih.gov/19178152/))

### F002 — holoCcmE delivers heme to CcmF via WWD-domain histidines

The two halves of system I are coupled by a controlled heme hand-off. A trapped holoCcmE:CcmF complex forms only after holoCcmE is **released from CcmABCD**, and the holo form binds CcmF **at least 20-fold** better than apoCcmE ([PMID: 24513106](https://pubmed.ncbi.nlm.nih.gov/24513106/)). At the acceptor, two conserved periplasmic histidines of CcmF (P-His1, P-His2) sit within the **WWD domain** and act as heme ligands, mirroring the CcmC:heme:CcmE ternary arrangement on the donor side. This establishes a common structural theme — external-facing WWD heme platforms with paired histidine ligands — repeated at each stage of the relay.

> *"the heme of holoCcmE is coordinated by P-His1 and P-His2 within the WWD domain of CcmF"* ([PMID: 24513106](https://pubmed.ncbi.nlm.nih.gov/24513106/))

### F003 — CcmAB ATP hydrolysis acts at the CcmE loading/release step, not at initial heme binding

A purified CcmA/CcmB complex has ATPase activity, and CcmA is membrane-associated only when CcmB is present. The Walker A **CcmA(K40D)** mutation abolishes in vitro ATPase activity and cytochrome *c* biogenesis in vivo — yet it still permits covalent heme attachment to CcmE. The resulting holoCcmE is, however, **incompetent for heme transfer/release** ([PMID: 17419738](https://pubmed.ncbi.nlm.nih.gov/17419738/)). This experiment is decisive: it localizes the ATP requirement **downstream** of covalent bond formation, to the maturation/release of holoCcmE, and rules out the hypothesis that ATP is needed for initial heme binding or for the covalent chemistry itself.

> *"Mutation of the Walker A motif in CcmA(K40D) results in loss of the in vitro ATPase activity and in loss of cytochrome c biogenesis in vivo. The same mutation does not prevent covalent attachment of heme to the heme chaperone CcmE, but holo-CcmE is, for some unidentified reason, incompetent for heme transfer"* ([PMID: 17419738](https://pubmed.ncbi.nlm.nih.gov/17419738/))

### F004 — A reductive branch (DsbD→CcmG→CcmH) keeps the CXXCH thiols reduced

Thioether ligation requires reduced apocytochrome cysteines, which is at odds with the oxidizing periplasm. CcmH contains a periplasmic **CXXC motif**; both cysteines are required aerobically, and the deficiency is chemically rescued by exogenous thiol (2-mercaptoethanesulfonic acid), consistent with a thiol-reductant role that keeps the apocytochrome heme-binding site reduced ([PMID: 9914305](https://pubmed.ncbi.nlm.nih.gov/9914305/)). The reducing power originates in cytoplasmic thioredoxin and is delivered across the membrane by **DsbD**, whose nDsbD/cDsbD domains relay electrons via oxidation-state-dependent, kinetically insulated thiol-disulfide exchange ([PMID: 19004826](https://pubmed.ncbi.nlm.nih.gov/19004826/), [PMID: 15057279](https://pubmed.ncbi.nlm.nih.gov/15057279/), [PMID: 21543317](https://pubmed.ncbi.nlm.nih.gov/21543317/)).

> *"We propose a model for the reaction sequence in which CcmH keeps the heme binding site of apocytochrome c in a reduced form for subsequent heme ligation"* ([PMID: 9914305](https://pubmed.ncbi.nlm.nih.gov/9914305/))

### F005 — Cryo-EM localizes the ATP site to CcmA and the heme site to CcmC

High-resolution cryo-EM structures of CcmABCD were solved in the apo form, with the non-hydrolyzable analog AMP-PNP, and with ATP + heme. They locate the **ATP-binding site in CcmA** and the **heme-binding site in CcmC**, and support a model in which CcmABCD is an ABC transporter that uses ATP hydrolysis energy not for classical substrate import but to **transfer heme from CcmC to CcmE and to release holoCcmE** ([PMID: 36307425](https://pubmed.ncbi.nlm.nih.gov/36307425/)). This structural work grounds the biochemistry of F003 in an atomic model of the machine.

> *"CcmABCD represents an ABC transporter complex using the energy of ATP hydrolysis for the transfer of heme from one binding partner (CcmC) to another (CcmE)"* ([PMID: 36307425](https://pubmed.ncbi.nlm.nih.gov/36307425/))

### F006 — Heme-iron redox control: Fe³⁺ release, Fe²⁺ re-reduction before ligation

The authoritative two-step model frames system I as: **Step 1**, CcmABCD-mediated synthesis and release of **oxidized** holoCcmE (heme in the Fe³⁺ state), with external histidines of CcmC involved in heme attachment; **Step 2**, CcmFH-mediated **reduction of the holoCcmE heme (to Fe²⁺)** and ligation to CXXCH ([PMID: 19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/)). The parallel system II achieves an analogous goal by a different means, using the CcsA WWD domain and two external histidines to maintain heme reduced before ligation. Redox control of the heme iron is thus a unifying constraint across cytochrome *c* biogenesis, implemented by non-homologous machinery.

> *"Step 1 is the CcmABCD-mediated synthesis and release of oxidized holoCcmE (heme in the Fe(+3) state)"* / *"Step 2 includes the CcmFH-mediated reduction (to Fe(+2)) of holoCcmE and ligation of the heme to CXXCH"* ([PMID: 19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/))

### F007 — CycH-family proteins (CcmI) are TPR-domain apocytochrome chaperones

In *Pseudomonas aeruginosa*, the periplasmic domain of CcmI comprises a **TPR domain** plus a peculiar C-terminal domain. It both binds *P. aeruginosa* apo-cytochrome c551 — recognition mediated mainly by the apoprotein's C-terminal sequence, via the TPR domain — and shows **general chaperone activity**, preventing citrate synthase aggregation in a concentration-dependent manner, with affinities consistent with a multiprotein-complex component ([PMID: 23648553](https://pubmed.ncbi.nlm.nih.gov/23648553/)). In *Rhodobacter capsulatus*, CcmI is required for maturation; its membrane-spanning (CcmI-1) and periplasmic (CcmI-2) segments have distinct functions, and CcmI-null defects are suppressed by co-overproduction of the CcmF–CcmH couple plus CcmG (or apocytochrome c2), placing CcmI functionally alongside both the ligation and reductive components ([PMID: 17122341](https://pubmed.ncbi.nlm.nih.gov/17122341/)).

> *"Binding experiments show that the interaction occurs at the level of the TPR domain and that the recognition is mediated mainly by the C-terminal sequence of Pa-apoCyt"* ([PMID: 23648553](https://pubmed.ncbi.nlm.nih.gov/23648553/))

### Summary table of players

| Player | Family / motif | Role | Key evidence |
|---|---|---|---|
| CcmA | ABC ATPase (Walker A/B) | ATP hydrolysis to drive CcmE loading/release | K40D (F003); cryo-EM ATP site (F005) |
| CcmB | Membrane subunit | Anchors CcmA; part of transmembrane assembly | ATPase requires CcmB (F003) |
| CcmC | WWD heme-handling | Binds heme; presents it to CcmE | Cryo-EM heme site (F005) |
| CcmD | Accessory membrane subunit | Efficient holoCcmE release | Part of CcmABCD complex (F005) |
| CcmE | Covalent heme chaperone (His130, HxxxY) | Covalent holo-intermediate; stereospecific transfer | H130A/H130C (F001) |
| CcmF | WWD synthase (P-His1/2) | Receives heme; re-reduces & ligates to CXXCH | 20-fold holo binding (F002); redox (F006) |
| CcmG | Periplasmic thioredoxin (CXXC) | Relays reducing power to CcmH | Reductive branch (F004) |
| CcmH | CXXC redox/assembly | Keeps CXXCH thiols reduced | Thiol rescue (F004) |
| CycH/CcmI | TPR domain | Apocytochrome recognition & chaperoning | TPR binding (F007) |

---

## 5. Evolutionary and Cell-Biological Variation

### Lineage distribution

Canonical, His-based system I is characteristic of **proteobacteria** and of **plant and protozoan mitochondria**. A **variant "system I\*"** uses a cysteine-based CcmE (CxxxY motif rather than HxxxY) and is found across **archaea and some bacteria** (e.g., *Desulfovibrio*). In two halobacteria, CcmE contains yet another arrangement (HxxxHxxxH). Strikingly, **CcmH is absent from all complete archaeal genomes examined and from most bacterial genomes carrying the CxxxY-type CcmE**, indicating coordinated evolutionary co-variation between the chaperone chemistry and the redox-preparation component ([PMID: 16920107](https://pubmed.ncbi.nlm.nih.gov/16920107/)).

| Feature | Canonical System I | System I* variant |
|---|---|---|
| CcmE reactive residue | His (HxxxY motif) | Cys (CxxxY motif), or HxxxHxxxH in some halobacteria |
| Representative taxa | Proteobacteria; plant/protozoan mitochondria | Archaea; some bacteria (e.g., *Desulfovibrio*) |
| CcmH | Present | Frequently absent |
| Covalent heme intermediate | Yes (His~heme) | Yes (Cys~heme) |

### CcmH / CycH architecture

Across proteobacteria, the redox/assembly and apocytochrome-chaperone activities are distributed differently — as separate CcmH and CcmI/CycH polypeptides in some lineages and as fused or differently partitioned modules in others. In *Rhodobacter*, CcmI-null defects are suppressed by co-overproduction of the CcmF–CcmH couple plus CcmG (or the apocytochrome c2), placing CcmI functionally alongside both the ligation and reductive components ([PMID: 17122341](https://pubmed.ncbi.nlm.nih.gov/17122341/)).

### Convergent alternative routes

The same chemical outcome — two thioethers between reduced heme and a CXXCH motif — is achieved by three non-homologous systems (I/Ccm, II/Ccs, III/HCCS). System II (CcsBA) transports heme through a protein channel to an external active site and dispenses with a covalent chaperone intermediate ([PMID: 37827288](https://pubmed.ncbi.nlm.nih.gov/37827288/)). This convergence is a strong argument that the underlying chemical constraints — not the machinery — dictate the essential logic. When considering which family members best represent the ancestral role, the canonical His-based *E. coli* CcmE is the most-studied and mechanistically transparent representative, while the Cys-based archaeal/Desulfovibrio CcmEs illuminate the plasticity of the covalent chemistry and probably represent lineage-specific replacements rather than the ancestral state.

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering constraints (what must precede what)

1. **Apocytochrome export precedes maturation.** Sec export must deliver the apoprotein to the periplasm before heme ligation.
2. **CcmABCD acts before CcmE loading.** Heme binding at CcmC precedes covalent transfer to CcmE.
3. **CcmE loading precedes CcmF ligation.** HoloCcmE must be released from CcmABCD before it can dock on CcmF ([PMID: 24513106](https://pubmed.ncbi.nlm.nih.gov/24513106/)).
4. **Reduction of CXXCH precedes ligation.** The apoprotein cysteines must be reduced (DsbD→CcmG→CcmH) before thioether formation ([PMID: 9914305](https://pubmed.ncbi.nlm.nih.gov/9914305/)).
5. **Fe³⁺→Fe²⁺ re-reduction precedes ligation.** HoloCcmE is released oxidized; the synthase re-reduces the heme before ligation ([PMID: 19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/)).

### Redox and compartment constraints

Thioether ligation requires **reduced substrate thiols** in an otherwise **oxidizing periplasm**, so the reductive branch must be kinetically insulated from the oxidative Dsb pathway. This insulation is achieved by **oxidation-state-dependent protein–protein affinities** and large kinetic barriers to cross-pathway disulfide exchange ([PMID: 21543317](https://pubmed.ncbi.nlm.nih.gov/21543317/), [PMID: 15057279](https://pubmed.ncbi.nlm.nih.gov/15057279/)). Simultaneously, the heme iron must be in the correct oxidation state at each stage — ferric during covalent CcmE formation and release, ferrous immediately before ligation.

### Failure modes revealed by mutation

- **CcmA Walker-A K40D:** abolishes ATPase activity in vitro and cytochrome *c* biogenesis in vivo. Critically, covalent heme attachment to CcmE still occurs, but the resulting holoCcmE is **incompetent for heme transfer/release** — pinpointing the ATP requirement to the loading/release step downstream of covalent bond formation ([PMID: 17419738](https://pubmed.ncbi.nlm.nih.gov/17419738/)).
- **CcmE H130A:** abolishes holoCcmE and cytochrome *c* formation, whereas nearby alanine insertions abolish holoCcmE without perturbing the fold — defining a discrete heme pocket and confirming the covalent bond as a committed checkpoint ([PMID: 19178152](https://pubmed.ncbi.nlm.nih.gov/19178152/)).
- **CcmH CXXC mutation:** loss of function aerobically, chemically rescued by exogenous thiol — confirming the redox (rather than structural) nature of the defect ([PMID: 9914305](https://pubmed.ncbi.nlm.nih.gov/9914305/)).

### Evidence that rules out otherwise-plausible paths

- The 20-fold holo-over-apoCcmE preference for CcmF, and the requirement for prior release from CcmABCD, **rules out** a model where CcmE simply hands heme to CcmF while still bound to the ABC complex ([PMID: 24513106](https://pubmed.ncbi.nlm.nih.gov/24513106/)).
- The K40D result **rules out** the hypothesis that ATP is needed for initial heme binding or for the covalent chemistry itself; it is needed for holoCcmE maturation/release ([PMID: 17419738](https://pubmed.ncbi.nlm.nih.gov/17419738/)).
- A previously proposed quinone-binding site on CcmF was shown **not** essential for either system I or system I*, removing one candidate route for the reductive chemistry at the synthase ([PMID: 24044352](https://pubmed.ncbi.nlm.nih.gov/24044352/)).

---

## 7. Controversies and Open Questions

**Strongly supported claims.** The covalent His-heme CcmE intermediate (F001), the ATP requirement at the CcmE loading/release step (F003), the holoCcmE→CcmF WWD-histidine handoff (F002), the DsbD→CcmG→CcmH reductive logic (F004), and the cryo-EM assignment of ATP/heme sites in CcmABCD (F005) rest on convergent genetic, biochemical, spectroscopic, and structural evidence.

**Areas of uncertainty or indirect evidence.**

1. **Atomic mechanism of heme hand-off between WWD platforms.** How heme is passed from CcmC to CcmE and then from CcmE to CcmF at the atomic level — the trajectory, transient ligation states, and whether direct protein-protein channeling occurs — remains unresolved. The oxidation-state-triggered ligation switch on CcmE ([PMID: 16373344](https://pubmed.ncbi.nlm.nih.gov/16373344/)) is a clue, not a complete mechanism.
2. **Electron source and catalytic role of CcmF at ligation.** The reductant that re-reduces holoCcmE heme (Fe³⁺→Fe²⁺) at the synthase, and whether CcmF is a true catalyst or a scaffold that positions substrate and cofactor, are not fully established. The refutation of the CcmF quinone site ([PMID: 24044352](https://pubmed.ncbi.nlm.nih.gov/24044352/)) narrows but does not close this question.
3. **CycH/CcmI stoichiometry, substrate specificity, and hand-off geometry.** The TPR-domain chaperone role is supported ([PMID: 23648553](https://pubmed.ncbi.nlm.nih.gov/23648553/)), but how CcmI presents the apoprotein to the synthase, its copy number in the mature complex, and how broadly it recognizes different cytochrome *c* substrates are open.
4. **Cross-organism extrapolation.** Much mechanistic detail comes from *E. coli* (systems I and I*), with key chaperone data from *Pseudomonas* and *Rhodobacter*. The lineage co-variation of CcmE chemistry with CcmH presence/absence ([PMID: 16920107](https://pubmed.ncbi.nlm.nih.gov/16920107/)) is a caution against assuming a single universal mechanism; conclusions should be qualified by organism.

**The most important open questions**, in priority order: (i) a structure of the holoCcmE:CcmF(H) synthase complex captured mid-ligation; (ii) identification of the physiological electron donor for heme re-reduction at CcmF; and (iii) a unified account of how covalent-chaperone chemistry (His vs. Cys) co-evolves with the reductive branch across lineages.

---

## 8. Limitations and Knowledge Gaps

This synthesis draws on 19 primary and review papers spanning genetics, biochemistry, spectroscopy, NMR, crystallography, and cryo-EM. Its principal limitations mirror those of the field:

- **Organism heterogeneity.** Conclusions weave together data from *E. coli*, *Pseudomonas aeruginosa*, *Rhodobacter capsulatus*, archaea, and mitochondria. Where a claim rests on a single organism (e.g., CcmI chaperone activity in *P. aeruginosa*), it is flagged accordingly.
- **Structural coverage is incomplete.** The CcmABCD complex now has high-resolution cryo-EM structures ([PMID: 36307425](https://pubmed.ncbi.nlm.nih.gov/36307425/)), but a substrate-loaded CcmF/H synthase structure with docked holoCcmE and apocytochrome is not yet available, leaving the ligation geometry inferred rather than observed.
- **Redox intermediates are largely inferred.** The Fe³⁺-release / Fe²⁺-ligation model ([PMID: 19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/)) is well-motivated but the transient in-complex oxidation states have not all been directly trapped.
- **CycH/CcmI functional boundaries are fuzzy.** The distribution of redox and chaperone functions across CcmH and CycH/CcmI varies by lineage, complicating a single definition.

---

## 9. Proposed Follow-up Experiments / Actions

1. **Trap the synthase mid-reaction.** Determine a cryo-EM structure of a holoCcmE:CcmFH complex, ideally with a bound apocytochrome CXXCH peptide, to resolve the WWD-to-CXXCH heme hand-off geometry and the roles of P-His1/P-His2.
2. **Identify the ligation-step reductant.** Use defined in vitro reconstitution with CcmF/CcmH to test candidate electron donors for Fe³⁺→Fe²⁺ re-reduction, and probe whether CcmH's CXXC or a separate cofactor supplies the electrons.
3. **Dissect CcmI hand-off.** Combine crosslinking mass spectrometry and single-molecule assays to measure CcmI:apocytochrome:synthase stoichiometry and to test whether TPR-domain recognition of the apoprotein C-terminus is generalizable across diverse cytochrome *c* substrates.
4. **Systematically compare system I and I\*.** Extend the H130C/system I* toolkit to map, residue by residue, how Cys-based versus His-based covalent chemistry alters heme trafficking kinetics, and correlate with the genomic loss of CcmH.
5. **Reconstitute the full relay in vitro.** Build a minimal proteoliposome system containing CcmABCD, CcmE, CcmFH, CcmG, and DsbD to test the predicted obligatory ordering and to identify rate-limiting steps and failure points.

---

## 10. Key References

| PMID | Short title | Role in this review |
|---|---|---|
| [19178152](https://pubmed.ncbi.nlm.nih.gov/19178152/) | Probing the heme-binding site of CcmE | Covalent His130-heme bond; H130A abolishes holoCcmE (F001) |
| [12657624](https://pubmed.ncbi.nlm.nih.gov/12657624/) | CcmE active-site mutant variants | H130C still forms covalent bond → basis of system I* (F001) |
| [24513106](https://pubmed.ncbi.nlm.nih.gov/24513106/) | HoloCcmE–CcmF interaction | 20-fold holo preference; WWD P-His1/2 ligands (F002) |
| [17419738](https://pubmed.ncbi.nlm.nih.gov/17419738/) | Loss of CcmAB ATP hydrolysis | K40D blocks release, not covalent attachment (F003) |
| [9914305](https://pubmed.ncbi.nlm.nih.gov/9914305/) | CcmH redox pathway | CXXC keeps apocytochrome reduced (F004) |
| [19004826](https://pubmed.ncbi.nlm.nih.gov/19004826/) | Control of interdomain exchange in DsbD | DsbD as transmembrane reductant conductor (F004) |
| [36307425](https://pubmed.ncbi.nlm.nih.gov/36307425/) | Structures of CcmABCD | ATP site in CcmA, heme site in CcmC (F005) |
| [19721088](https://pubmed.ncbi.nlm.nih.gov/19721088/) | Cytochrome *c* biogenesis review (Kranz et al.) | Two-step Fe³⁺/Fe²⁺ redox model (F006) |
| [23648553](https://pubmed.ncbi.nlm.nih.gov/23648553/) | *P. aeruginosa* CcmI recognition | TPR apocytochrome chaperone (F007) |
| [17122341](https://pubmed.ncbi.nlm.nih.gov/17122341/) | CcmI segments in *Rhodobacter* | Membrane/periplasmic CcmI functions (F007) |
| [16920107](https://pubmed.ncbi.nlm.nih.gov/16920107/) | Variant system I in archaea | Cys-based CcmE; CcmH loss covariation |
| [16373344](https://pubmed.ncbi.nlm.nih.gov/16373344/) | Dynamic ligation of CcmE | Oxidation-state-triggered covalent bond |
| [24044352](https://pubmed.ncbi.nlm.nih.gov/24044352/) | Probing heme delivery in system I | CcmF quinone site not essential |
| [37827288](https://pubmed.ncbi.nlm.nih.gov/37827288/) | Structural basis of heme-attaching machines | System I vs. system II synthase comparison |
| [21543317](https://pubmed.ncbi.nlm.nih.gov/21543317/) | Oxidation-state-dependent interactions | Kinetic insulation of redox pathways |
| [15057279](https://pubmed.ncbi.nlm.nih.gov/15057279/) | DsbD disulfide exchange structure/kinetics | Kinetic barriers between Dsb pathways |
| [16042600](https://pubmed.ncbi.nlm.nih.gov/16042600/) | Covalent cofactor attachment review | Overview of c-type cytochrome chemistry |
| [17544440](https://pubmed.ncbi.nlm.nih.gov/17544440/) | cDsbD active-site NMR | DsbD C-terminal domain redox properties |
| [22127524](https://pubmed.ncbi.nlm.nih.gov/22127524/) | nDsbD NMR assignments | DsbD N-terminal domain redox states |

---

*Prepared as a commissioned review-style synthesis of bacterial cytochrome c maturation system I. Mechanistic claims are anchored to the cited primary and review literature; areas of uncertainty are flagged explicitly, and cross-organism extrapolations are qualified where the underlying data derive from a single lineage.*


## Artifacts

- [OpenScientist final report](bacterial_cytochrome_c_maturation_system_i-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_cytochrome_c_maturation_system_i-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19004826
2. PMID:37827288
3. PMID:15057279
4. PMID:16920107
5. PMID:36307425
6. PMID:19721088
7. PMID:24513106
8. PMID:9914305
9. PMID:23648553
10. PMID:17122341
11. PMID:19178152
12. PMID:12657624
13. PMID:16373344
14. PMID:17419738
15. PMID:21543317
16. PMID:24044352