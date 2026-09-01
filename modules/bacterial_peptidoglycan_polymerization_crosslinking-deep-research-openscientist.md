---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:59:44.914375'
end_time: '2026-08-31T23:24:22.804091'
duration_seconds: 1477.89
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial peptidoglycan polymerization and crosslinking
  module_summary: A reusable bacterial module downstream of lipid II export. It separates
    septal and lateral-wall SEDS-bPBP synthases from class-A bifunctional PBPs, monofunctional
    glycan polymerases, and D,D-carboxypeptidase-mediated stem peptide maturation.
    The module does not include cytoplasmic precursor synthesis, lipid II flipping,
    or peptidoglycan recycling.
  module_outline: "- Bacterial peptidoglycan polymerization and crosslinking\n  -\
    \ 1. septal glycan polymerization and peptide crosslinking\n  - Septal FtsW-FtsI\
    \ peptidoglycan synthesis\n    - 1. septal glycan polymerization\n    - FtsW glycan\
    \ polymerization\n      - FtsW peptidoglycan glycosyltransferase (molecular player:\
    \ FtsW septal SEDS glycosyltransferases; activity or role: peptidoglycan glycosyltransferase\
    \ activity)\n    - 2. septal D,D-transpeptidation\n    - FtsI peptide crosslinking\n\
    \      - FtsI D,D-transpeptidase (molecular player: FtsI/PBP3 septal D,D-transpeptidases)\n\
    \  - 2. lateral-wall glycan polymerization and peptide crosslinking\n  - RodA-MrdA\
    \ peptidoglycan synthesis\n    - 1. lateral-wall glycan polymerization\n    -\
    \ RodA glycan polymerization\n      - RodA peptidoglycan glycosyltransferase (molecular\
    \ player: RodA/MrdB lateral-wall SEDS glycosyltransferases; activity or role:\
    \ peptidoglycan glycosyltransferase activity)\n    - 2. lateral-wall D,D-transpeptidation\n\
    \    - MrdA peptide crosslinking\n      - Alternative versions by enzyme paralog:\
    \ MrdA/PBP2 paralogs\n        - MrdA-I\n          - MrdA-I D,D-transpeptidase\
    \ (molecular player: MrdA/PBP2 D,D-transpeptidases)\n        - MrdA-II\n     \
    \     - MrdA-II D,D-transpeptidase (molecular player: MrdA/PBP2 D,D-transpeptidases)\n\
    \  - 3. bifunctional glycan polymerization and peptide crosslinking\n  - Class-A\
    \ PBP peptidoglycan synthesis\n    - Alternative versions by enzyme family member:\
    \ Class-A PBP variants\n      - PBP1A/MrcA\n        - PBP1A bifunctional synthase\
    \ (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan\
    \ glycosyltransferase activity)\n      - PBP1B/MrcB\n        - PBP1B bifunctional\
    \ synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan\
    \ glycosyltransferase activity)\n      - PbpC\n        - PbpC peptidoglycan synthase\
    \ (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan\
    \ glycosyltransferase activity)\n  - 4. monofunctional glycan polymerization\n\
    \  - MtgA glycan polymerization\n    - MtgA peptidoglycan glycosyltransferase\
    \ (molecular player: monofunctional biosynthetic peptidoglycan glycosyltransferases;\
    \ activity or role: peptidoglycan glycosyltransferase activity)\n  - 5. pentapeptide\
    \ stem trimming\n  - DacA D,D-carboxypeptidation\n    - DacA D,D-carboxypeptidase\
    \ (molecular player: DacA low-molecular-mass D,D-carboxypeptidases; activity or\
    \ role: serine-type D-Ala-D-Ala carboxypeptidase activity)"
  module_connections: No explicit connections.
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_peptidoglycan_polymerization_crosslinking-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_peptidoglycan_polymerization_crosslinking-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial peptidoglycan polymerization and crosslinking

## Working Scope

A reusable bacterial module downstream of lipid II export. It separates septal and lateral-wall SEDS-bPBP synthases from class-A bifunctional PBPs, monofunctional glycan polymerases, and D,D-carboxypeptidase-mediated stem peptide maturation. The module does not include cytoplasmic precursor synthesis, lipid II flipping, or peptidoglycan recycling.

## Provisional Biological Outline

- Bacterial peptidoglycan polymerization and crosslinking
  - 1. septal glycan polymerization and peptide crosslinking
  - Septal FtsW-FtsI peptidoglycan synthesis
    - 1. septal glycan polymerization
    - FtsW glycan polymerization
      - FtsW peptidoglycan glycosyltransferase (molecular player: FtsW septal SEDS glycosyltransferases; activity or role: peptidoglycan glycosyltransferase activity)
    - 2. septal D,D-transpeptidation
    - FtsI peptide crosslinking
      - FtsI D,D-transpeptidase (molecular player: FtsI/PBP3 septal D,D-transpeptidases)
  - 2. lateral-wall glycan polymerization and peptide crosslinking
  - RodA-MrdA peptidoglycan synthesis
    - 1. lateral-wall glycan polymerization
    - RodA glycan polymerization
      - RodA peptidoglycan glycosyltransferase (molecular player: RodA/MrdB lateral-wall SEDS glycosyltransferases; activity or role: peptidoglycan glycosyltransferase activity)
    - 2. lateral-wall D,D-transpeptidation
    - MrdA peptide crosslinking
      - Alternative versions by enzyme paralog: MrdA/PBP2 paralogs
        - MrdA-I
          - MrdA-I D,D-transpeptidase (molecular player: MrdA/PBP2 D,D-transpeptidases)
        - MrdA-II
          - MrdA-II D,D-transpeptidase (molecular player: MrdA/PBP2 D,D-transpeptidases)
  - 3. bifunctional glycan polymerization and peptide crosslinking
  - Class-A PBP peptidoglycan synthesis
    - Alternative versions by enzyme family member: Class-A PBP variants
      - PBP1A/MrcA
        - PBP1A bifunctional synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan glycosyltransferase activity)
      - PBP1B/MrcB
        - PBP1B bifunctional synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan glycosyltransferase activity)
      - PbpC
        - PbpC peptidoglycan synthase (molecular player: class-A bifunctional PBPs; activity or role: peptidoglycan glycosyltransferase activity)
  - 4. monofunctional glycan polymerization
  - MtgA glycan polymerization
    - MtgA peptidoglycan glycosyltransferase (molecular player: monofunctional biosynthetic peptidoglycan glycosyltransferases; activity or role: peptidoglycan glycosyltransferase activity)
  - 5. pentapeptide stem trimming
  - DacA D,D-carboxypeptidation
    - DacA D,D-carboxypeptidase (molecular player: DacA low-molecular-mass D,D-carboxypeptidases; activity or role: serine-type D-Ala-D-Ala carboxypeptidase activity)

## Known Relationships Among Steps

No explicit connections.

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

# Bacterial Peptidoglycan Polymerization and Crosslinking: A Reusable Extracytoplasmic Module

*A commissioned review-style synthesis of the SEDS–bPBP, class-A PBP, monofunctional glycosyltransferase, and D,D-carboxypeptidase machinery that converts exported Lipid II into mature, crosslinked sacculus.*

---

## 1. Executive Summary

Bacterial peptidoglycan (PG) polymerization and crosslinking is the extracytoplasmic module that receives membrane-presented **Lipid II** and converts it into the covalently crosslinked mesh (the **sacculus**) that gives bacteria their shape and protects them from osmotic lysis. The central conceptual advance of the past decade is that this module is built from **two mechanistically independent, convergently evolved glycan-polymerase systems that feed a shared crosslinking chemistry**. The first is the **SEDS glycosyltransferase** family (FtsW at the septum, RodA at the sidewall), which polymerizes glycan chains from within cytoskeleton-organized machines and works in **obligate cognate pairs** with class-B penicillin-binding-protein (bPBP) transpeptidases (FtsI/PBP3 septally, MrdA/PBP2 laterally). The second is the family of **bifunctional class-A PBPs** (PBP1A/MrcA, PBP1B/MrcB, PbpC), which carry a **GT51-fold glycosyltransferase** domain and a transpeptidase domain in a single polypeptide and are switched on by outer-membrane lipoproteins (LpoA, LpoB). Two accessory activities complete the module: **monofunctional GT51 glycan polymerases** (MtgA/MGT), which polymerize glycan without crosslinking, and **DacA/PBP5-type low-molecular-mass D,D-carboxypeptidases**, which trim stem pentapeptides to tetrapeptides and thereby tune the density of crosslinking.

The crosslinking chemistry itself is **D,D-transpeptidation**, forming **4→3 (D-Ala–meso-DAP) crosslinks**, and it is the pharmacological target of β-lactam antibiotics. This is mechanistically distinct from the **L,D-transpeptidases** that form 3→3 crosslinks and can, in some organisms, bypass the PBPs to confer β-lactam resistance — an activity that sits at the boundary of, and should be distinguished from, the core module described here.

Crucially, the module is best understood **not as a single fixed pathway but as a variable toolkit**. The SEDS–bPBP synthase is the near-universal, ancestral, cytoskeleton-gated core; the aPBP branch behaves largely as a semi-autonomous fortification and repair system. Some bacterial lineages lack aPBPs entirely, and in at least one pathogen (*Clostridioides difficile*) a class-A PBP has taken over the division role normally played by FtsW/FtsI. This review lays out the boundaries, mechanism, molecular players, evolutionary variation, ordering constraints, and open controversies of the system, anchored to primary literature and authoritative reviews.

---

## 2. Definition and Biological Boundaries

### What is included

The module comprises everything that acts on Lipid II **after it has been flipped to the outer (periplasmic or extracellular) leaflet of the cytoplasmic membrane** and before/while the resulting glycan strands are stitched into the existing sacculus. Concretely, it includes:

- **Glycan polymerization (glycosyltransfer):** SEDS enzymes (FtsW, RodA, and developmental paralogs such as SpoVE), the GT51 domain of class-A PBPs, and monofunctional GT51 enzymes (MtgA/MGT).
- **Peptide crosslinking (D,D-transpeptidation):** class-B PBP transpeptidases (FtsI/PBP3, MrdA/PBP2) and the transpeptidase domains of class-A PBPs.
- **Stem-peptide maturation:** DacA/PBP5-type D,D-carboxypeptidases that trim pentapeptides to tetrapeptides.

### What is explicitly excluded (neighboring processes often confused with it)

- **Cytoplasmic precursor synthesis** (the Mur pathway, MraY, MurG) — upstream; produces Lipid II but is not part of the polymerization/crosslinking module.
- **Lipid II flipping** across the membrane by **MurJ** — the gate that delivers substrate to the module but is mechanistically separate ([PMID: 35274942](https://pubmed.ncbi.nlm.nih.gov/35274942/)).
- **Peptidoglycan recycling** and the salvage of muropeptides.
- **L,D-transpeptidation (3→3 crosslinking):** a chemically distinct crosslinking route that operates in parallel and can bypass the D,D-transpeptidases; it is a remodeling/resistance activity rather than part of the canonical polymer-and-crosslink core ([PMID: 30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/)).
- **Autolysins/hydrolases** (amidases, endopeptidases, lytic transglycosylases) that open the sacculus for insertion — the essential counterpart of synthesis, but not synthases.

### Competing definitions in the literature

Historically, PG polymerization was attributed **solely to the PBPs**, because the class-A PBP GT51 domain was the only biochemically demonstrated glycan polymerase and the only one with a known inhibitor (moenomycin). The discovery that **SEDS proteins are bona fide polymerases** ([PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/)) forced a redefinition: the module now contains **two structurally unrelated polymerase families**. A second definitional tension is whether the aPBPs are "core" synthases or an accessory repair/fortification system; genetic and cell-biological data (below) increasingly support the latter framing in rod-shaped model organisms, while cautioning that lineage-specific exceptions exist.

---

## 3. Mechanistic Overview

### The best current model of the sequence of events

```
                 Lipid II  (GlcNAc–MurNAc–pentapeptide–PP–undecaprenol)
                    │  [delivered to outer leaflet by MurJ — upstream, excluded]
                    ▼
   ┌──────────────────────── GLYCAN POLYMERIZATION ────────────────────────┐
   │                                                                        │
   │   SEDS system (in cytoskeletal machines)      aPBP system (semi-auto)  │
   │   RodA (sidewall) / FtsW (septum)             PBP1A/1B/PbpC GT51 domain │
   │   + cognate bPBP (MrdA/PBP2, FtsI/PBP3)       + MtgA (monofunctional GT)│
   │   grows chain at the REDUCING end             grows chain (GT51 fold)   │
   │                                                                        │
   └───────────────────────────────┬────────────────────────────────────────┘
                                    ▼
   ┌──────────────────────── PEPTIDE CROSSLINKING ─────────────────────────┐
   │   D,D-transpeptidation → 4→3 crosslinks (donor D-Ala–D-Ala,            │
   │   acceptor meso-DAP)   — bPBP TPase or aPBP TPase; β-lactam target     │
   └───────────────────────────────┬────────────────────────────────────────┘
                                    ▼
   ┌──────────────────── STEM-PEPTIDE MATURATION ──────────────────────────┐
   │   DacA/PBP5 D,D-carboxypeptidase: pentapeptide → tetrapeptide          │
   │   (removes terminal D-Ala; limits donors → tunes crosslinking density) │
   └────────────────────────────────────────────────────────────────────────┘
                                    ▼
                        Mature crosslinked SACCULUS
```

### Obligatory, conditional, and accessory steps

- **Obligatory:** Glycan polymerization *and* D,D-transpeptidation must both occur to build load-bearing wall. In canonical rod-shaped bacteria, **at least one SEDS–bPBP pair (elongation: RodA–PBP2; division: FtsW–PBP3) is required**. Activation of the septal synthase is itself an obligatory gated step (below).
- **Conditional / redundant:** The **aPBP branch** is dispensable for viability in several organisms — its polymerase activity is not required for glycan synthesis by the elongation machinery in *E. coli* ([PMID: 27643381](https://pubmed.ncbi.nlm.nih.gov/27643381/)), and *B. subtilis* remains viable on RodA alone when all known aPBP polymerases are depleted ([PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/)). Its role is context-dependent fortification/repair.
- **Accessory / tuning:** **Monofunctional GT (MtgA)** and the **D,D-carboxypeptidases (DacA/PBP5 family)** are individually non-essential and functionally redundant; they modulate glycan supply and crosslink density rather than being obligatory for wall closure.

### Directionality and substrate handling

SEDS polymerases grow the glycan strand by adding new Lipid II monomers to the **reducing end** of the chain — the opposite polarity to the GT51 (aPBP) enzymes — and they have distinct lipid requirements for the glycosyl-donor versus acceptor substrates ([PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/)). This is a hard mechanistic distinction between the two polymerase families, not merely a difference in regulation.

---

## 4. Major Molecular Players and Active Assemblies

| Player / family | Activity | Fold / mechanism | Partner / activator | Essential? |
|---|---|---|---|---|
| **FtsW** (SEDS) | Septal glycan polymerase | 10-TM SEDS fold; TM active-site cavity | Cognate bPBP **FtsI/PBP3**; divisome relay | Yes (canonical divisome) |
| **RodA** (SEDS) | Sidewall glycan polymerase | 10-TM SEDS fold, conserved TM cavity | Cognate bPBP **MrdA/PBP2**; MreB elongasome; MreC/MreD | Yes (for rod shape) |
| **SpoVE** (SEDS) | Sporulation spore-PG polymerase | SEDS fold | **SpoVD** (bPBP) | Sporulation-specific |
| **FtsI / PBP3** (bPBP) | D,D-transpeptidase (4→3) | PBP TPase; β-lactam target | FtsW; FtsQLB/FtsN relay | Yes (division) |
| **MrdA / PBP2** (bPBP) | D,D-transpeptidase (4→3) | PBP TPase | RodA; MreCD | Yes (elongation) |
| **PBP1A/MrcA, PBP1B/MrcB, PbpC** (aPBP) | Bifunctional GT51 + TPase | GT51 GTase fold + TPase | **LpoA / LpoB** (OM lipoproteins) | Individually dispensable; pair often synthetic-lethal |
| **MtgA / MGT** | Monofunctional glycan polymerase | GT51 fold; moenomycin-sensitive | — | Accessory |
| **DacA / PBP5 family** (LMM PBP) | D,D-carboxypeptidase (penta→tetra) | Serine D-Ala–D-Ala carboxypeptidase | — | Redundant; shape-tuning |

### The SEDS fold and its catalytic cavity

The crystal structure of *Thermus thermophilus* RodA (solved at 2.9 Å via evolutionary-covariance fold prediction) revealed a **ten-pass transmembrane fold with large extracellular loops** and a **highly conserved transmembrane cavity that is catalytically essential** — perturbing the cavity abolishes RodA function in vitro and in vivo in both *B. subtilis* and *E. coli* ([PMID: 29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/)). This fold is unrelated to the GT51 glycosyltransferase domain of the aPBPs, cementing the two-family view.

### Allosteric activation of the SEDS–bPBP synthase

SEDS–bPBP pairs are not constitutively active; they are switched on through the cognate bPBP. In the *E. coli* divisome, epistasis of activating and bypass mutations places the FtsN-triggered signal in the order **FtsN → FtsQLB → FtsI → FtsW**, and activity-altering substitutions map to the interface between SEDS extracellular loop 4 (ECL4) and the bPBP pedestal domain ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)). A cryo-EM structure of the *Pseudomonas aeruginosa* FtsQBLWI complex resolves **FtsI-mediated allosteric activation of FtsW** and β-lactam-triggered conformational rearrangements, providing structural corroboration that the transpeptidase partner activates the glycosyltransferase ([PMID: 42537644](https://pubmed.ncbi.nlm.nih.gov/42537644/)). Activation is broadly coupled to the cytoskeleton: in *Caulobacter*, the FtsZ-binding protein **FzlA** links FtsZ to activation of FtsW/FtsI, and hyperactive FtsWI mutants bypass the FzlA requirement, supporting a conserved cytoskeleton-gated activation logic ([PMID: 31031115](https://pubmed.ncbi.nlm.nih.gov/31031115/)).

### The aPBP branch and its "hit-and-run" activation

Class-A PBPs are **bifunctional**, carrying both PG glycosyltransferase and transpeptidase activities in one polypeptide ([PMID: 34429361](https://pubmed.ncbi.nlm.nih.gov/34429361/)). Their activity is controlled by outer-membrane lipoproteins: **LpoA is required to stimulate PBP1a polymerase activity** ([PMID: 34429361](https://pubmed.ncbi.nlm.nih.gov/34429361/)), and single-molecule work shows that **LpoB triggers PBP1b synthesis through a conserved allosteric switch and then dissociates once synthesis begins** — a "hit-and-run" mechanism that directs repair to low-density regions of the wall ([PMID: 40691462](https://pubmed.ncbi.nlm.nih.gov/40691462/)). This transient, spatially-targeted activation is consistent with a repair/fortification role rather than a bulk-synthesis role.

### The GT51 glycosyltransferase and monofunctional polymerases

The peptidoglycan GT (GT51) domain adopts a **fold distinct from other glycosyltransferase classes** and is the target of **moenomycin** ([PMID: 17347437](https://pubmed.ncbi.nlm.nih.gov/17347437/)). A **monofunctional glycosyltransferase (MGT/MtgA)**, homologous to the N-terminal GT domain of class-A PBPs, incorporates UDP-GlcNAc into peptidoglycan in vitro and is inhibited by moenomycin A, proving that a GT51 enzyme can **polymerize glycan on its own**, without a transpeptidase domain ([PMID: 11466281](https://pubmed.ncbi.nlm.nih.gov/11466281/)).

### Stem-peptide maturation

DD-carboxypeptidases cleave the terminal D-alanine from stem pentapeptides to yield tetrapeptides ([PMID: 40777447](https://pubmed.ncbi.nlm.nih.gov/40777447/)). In *E. coli*, loss of the DD-CPase PBP6b raises PG pentapeptide content and causes morphological defects at acidic pH, and multiple DD-CPases (PBP4, PBP4b, PBP5, PBP6a, PBP7, AmpH) provide **redundant, condition-dependent** trimming ([PMID: 27329754](https://pubmed.ncbi.nlm.nih.gov/27329754/)). Because the pentapeptide is the acyl-donor for D,D-transpeptidation, trimming it to a tetrapeptide **removes potential donors and thereby limits crosslinking density** — the mechanistic link between this "tailoring" step and the crosslinking core.

---

## 5. Evolutionary and Cell-Biological Variation

### Two convergent polymerase systems

The strongest organizing principle for variation is that the module contains **two structurally unrelated polymerase families that function semi-autonomously**: SEDS proteins acting *within* the cytoskeletal machines (elongasome/divisome), and aPBPs acting *outside* those complexes ([PMID: 27643381](https://pubmed.ncbi.nlm.nih.gov/27643381/)). The SEDS fold (10-TM, TM cavity) and the GT51 fold are non-homologous and grow chains with opposite polarity ([PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/)), so their coexistence is best read as **convergent evolution onto the same chemical outcome**.

### Lineage-level variation

- **aPBP-less bacteria:** At least **four phylogenetically distinct groups of bacteria lack any identifiable aPBP** yet still build crosslinked PG, demonstrating that the aPBP branch is a **dispensable elaboration**, not a universal requirement ([PMID: 34311584](https://pubmed.ncbi.nlm.nih.gov/34311584/)).
- **aPBP replacing SEDS at the septum:** *Clostridioides difficile* lacks functional FtsW/FtsI orthologs for division and instead uses the **bifunctional class-A PBP1** to mediate cell division, requiring both its GT and TP activities — an **alternative route to septal synthesis** ([PMID: 41118402](https://pubmed.ncbi.nlm.nih.gov/41118402/)).
- **Cocci reuse the rod logic:** *Staphylococcus aureus*, though a coccus, maintains **two SEDS–bPBP cognate pairs** — RodA–PBP3 (sidewall) and FtsW–PBP1 (septum) — mirroring the elongation/division division of labor seen in rods ([PMID: 31086309](https://pubmed.ncbi.nlm.nih.gov/31086309/)).
- **Developmental paralogs:** Sporulation deploys a dedicated SEDS–bPBP pair, **SpoVE–SpoVD**, for spore PG synthesis in *B. subtilis*, showing that the cognate-pair architecture is redeployed at specific developmental stages ([PMID: 20417640](https://pubmed.ncbi.nlm.nih.gov/20417640/)).

### Which family member best represents the ancestral role?

Because the SEDS–bPBP synthase is near-universal, cytoskeleton-gated, and present even where aPBPs are absent, the **SEDS–bPBP pair (exemplified by RodA–PBP2 for elongation and FtsW–PBP3 for division) is the best representative of the ancestral polymerization/crosslinking role**. The aPBPs, monofunctional GTs, and DD-carboxypeptidases are better read as later elaborations, replacements, or accessory/tuning modules layered onto that core.

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering constraints

1. **Substrate delivery precedes polymerization.** Lipid II must be flipped to the outer leaflet before any GT can act (upstream of, and separable from, the module).
2. **Polymerization is coupled to, and gates, crosslinking.** D,D-transpeptidation requires nascent glycan chains bearing pentapeptide donors; in SEDS–bPBP complexes, activation of the polymerase (FtsW) is relayed *through* the transpeptidase (FtsI) — i.e., the two activities are allosterically interlocked ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/); [PMID: 42537644](https://pubmed.ncbi.nlm.nih.gov/42537644/)).
3. **Carboxypeptidation acts on pentapeptides.** DD-CPase trimming can only affect the crosslinking that has not yet consumed a given pentapeptide; excess or deficient trimming shifts the pentapeptide/tetrapeptide balance and cell shape ([PMID: 27329754](https://pubmed.ncbi.nlm.nih.gov/27329754/)).

### Compartment- and machine-specific segregation

- **Septal vs. lateral:** FtsW–FtsI operate in the **divisome** (FtsZ-organized, midcell); RodA–MrdA operate in the **elongasome** (MreB-organized, lateral). These are spatially and temporally segregated machines even within one cell.
- **Inside vs. outside the cytoskeletal machine:** SEDS enzymes function inside the machines; aPBPs act semi-autonomously outside them ([PMID: 27643381](https://pubmed.ncbi.nlm.nih.gov/27643381/)), and aPBP activation is spatially targeted to damage/low-density regions via the hit-and-run lipoprotein mechanism ([PMID: 40691462](https://pubmed.ncbi.nlm.nih.gov/40691462/)).

### Crosslink chemistry as a hard boundary

Crosslinking in this module is **D,D-transpeptidation forming 4→3 crosslinks**, and it is the target of β-lactams ([PMID: 30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/)). **L,D-transpeptidases forming 3→3 crosslinks are a separate route** that can bypass the PBPs and confer β-lactam resistance in some strains — evidence that rules out treating 3→3 crosslinking as part of the canonical D,D-transpeptidase core, even though it can substitute for it under stress ([PMID: 30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/)).

### Failure modes

- **Loss of SEDS/bPBP function** collapses either elongation (rod → sphere) or division (filamentation), depending on the pair affected ([PMID: 31086309](https://pubmed.ncbi.nlm.nih.gov/31086309/)).
- **Loss of DD-CPases** raises pentapeptide content and distorts shape, especially under stress (acidic pH) ([PMID: 27329754](https://pubmed.ncbi.nlm.nih.gov/27329754/)).
- **β-lactam inhibition** of the transpeptidases uncouples polymerization from crosslinking, producing weak, uncrosslinked glycan and, ultimately, lysis ([PMID: 30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/)); structural work shows β-lactams also trigger conformational rearrangements in the synthase complex ([PMID: 42537644](https://pubmed.ncbi.nlm.nih.gov/42537644/)).

---

## 7. Mechanistic Model and Interpretation (Synthesis)

Reading the evidence together, the module resolves into a **conserved ancestral core plus a variable accessory layer**:

- **Ancestral core:** an obligate **SEDS glycosyltransferase + class-B PBP transpeptidase cognate pair**, embedded in and gated by a cytoskeletal machine (MreB elongasome or FtsZ divisome). The bPBP allosterically activates the SEDS polymerase through the ECL4–pedestal interface, so polymerization and crosslinking are physically interlocked. This core is present essentially everywhere, is redeployed for elongation (RodA–PBP2), division (FtsW–PBP3), and sporulation (SpoVE–SpoVD), and is the best proxy for the ancestral state.

- **Accessory / fortification layer:** **bifunctional aPBPs** (activated transiently and locally by OM lipoproteins) that patch and reinforce the wall from outside the machines, plus **monofunctional GT51 polymerases** that add glycan without crosslinking. This layer is dispensable in many organisms and absent in some, but can be promoted to an essential division role in special cases (*C. difficile*).

- **Tuning layer:** **DacA/PBP5 DD-carboxypeptidases** that trim pentapeptide donors to tetrapeptides, setting the ceiling on crosslink density and thereby shaping the cell.

The single most important interpretive point for a non-specialist audience is that **"peptidoglycan synthesis" is not one enzyme or one pathway but a toolkit** in which two chemically distinct polymerase families feed a shared 4→3 transpeptidation chemistry, with the balance among tools varying by organism, cell-cycle stage, and stress state. This toolkit view explains why the system is simultaneously an outstanding antibiotic target (β-lactams hit the shared transpeptidase step; moenomycin hits GT51) and a source of intrinsic and evolved resistance (aPBP loss, LDT 3→3 bypass, and lineage-specific rewiring).

```
        ANCESTRAL CORE                 ACCESSORY LAYER            TUNING LAYER
   ┌────────────────────────┐   ┌────────────────────────┐   ┌──────────────────┐
   │ SEDS  +  cognate bPBP  │   │ aPBP (GT51+TPase)      │   │ DacA/PBP5 DD-CPase│
   │ RodA–PBP2 (elongation) │   │  + LpoA/LpoB (OM)      │   │ penta → tetra     │
   │ FtsW–PBP3 (division)   │   │ MtgA (monofunctional)  │   │ limits crosslinks │
   │ SpoVE–SpoVD (spore)    │   │ hit-and-run repair     │   │ redundant paralogs│
   │ cytoskeleton-gated     │   │ dispensable / variable │   │ shape maintenance │
   │ near-universal         │   │ absent in some clades  │   │                   │
   └────────────────────────┘   └────────────────────────┘   └──────────────────┘
        most conserved                more variable              modulatory
```

---

## 8. Controversies and Open Questions

**1. Is the aPBP branch "core" or "accessory"?** In *E. coli* and *B. subtilis*, aPBP polymerase activity is dispensable for glycan synthesis by the elongation machinery ([PMID: 27643381](https://pubmed.ncbi.nlm.nih.gov/27643381/); [PMID: 27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/)), supporting an accessory/repair framing. But *C. difficile* divides using an aPBP in place of FtsW/FtsI ([PMID: 41118402](https://pubmed.ncbi.nlm.nih.gov/41118402/)), and some lineages lack aPBPs entirely ([PMID: 34311584](https://pubmed.ncbi.nlm.nih.gov/34311584/)). The "core vs. accessory" label is therefore **organism-dependent**, and generalizing from *E. coli* is unsafe.

**2. How, mechanically, does the bPBP activate the SEDS polymerase?** Genetics places the signal FtsQLB→FtsI→FtsW and maps it to the ECL4–pedestal interface ([PMID: 33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/)), and cryo-EM now visualizes FtsI-mediated activation of FtsW ([PMID: 42537644](https://pubmed.ncbi.nlm.nih.gov/42537644/)). The precise conformational trajectory that opens the SEDS TM cavity for catalysis remains to be resolved at the level of catalytic intermediates.

**3. What is the true in-cell polymerization polarity and processivity of each family, and how are chain lengths set?** SEDS grows at the reducing end ([PMID: 31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/)) while GT51 enzymes grow with opposite polarity, but how the two systems' products are integrated into one sacculus in vivo is not fully understood.

**4. How redundant are the DD-carboxypeptidases, really?** Multiple paralogs provide condition-dependent trimming ([PMID: 27329754](https://pubmed.ncbi.nlm.nih.gov/27329754/)), yet the division of labor among them across growth states and species is not settled.

**5. Comparability across organisms.** Much of the mechanistic detail derives from a handful of models (*E. coli*, *B. subtilis*, *S. aureus*, *T. thermophilus*, *P. aeruginosa*, *Caulobacter*, *C. difficile*). Claims about "the" mechanism should be tied to the organism in which they were demonstrated; cocci, sporeformers, diderms, and aPBP-less clades each show variations that caution against overgeneralization.

---

## 9. Limitations and Knowledge Gaps

- **Model-organism bias.** The mechanistic core is drawn from a small set of species; cocci, diderms, sporeformers, and aPBP-less clades each modify the scheme, so organism-specific caveats are essential.
- **In vitro vs. in vivo gaps.** Polymerization polarity, processivity, and chain-length control are best characterized in reconstituted systems; how the two polymerase families' products are woven into one sacculus in the living cell is incompletely understood.
- **Activation intermediates unresolved.** Genetics and static cryo-EM define the activation relay, but the catalytic-intermediate conformations of the SEDS active-site cavity remain to be captured.
- **Redundancy accounting.** The precise, condition-resolved division of labor among the many DD-carboxypeptidases (and among aPBP paralogs) is not settled.
- **Boundary blurring under stress.** L,D-transpeptidation and hydrolase coordination sit at the edges of the module and can substitute for or gate its activities; where exactly to draw the boundary is partly a matter of convention.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Cross-lineage structural comparison** of SEDS–bPBP complexes (e.g., diderm vs. monoderm vs. aPBP-less clades) to test whether the ECL4–pedestal activation logic is truly universal.
2. **Time-resolved / trapped-intermediate cryo-EM** of an activating FtsW–FtsI or RodA–PBP2 complex to capture the conformational trajectory that opens the SEDS TM cavity.
3. **Single-molecule co-tracking** of SEDS and aPBP synthases in the same cell to quantify their spatial partitioning and the fraction of wall built by each under different growth/stress states.
4. **Systematic DD-carboxypeptidase deletion series** across conditions (pH, osmolarity, growth rate) with muropeptide profiling to resolve the redundancy structure and its link to shape.
5. **Comparative reconstitution** of SEDS vs. GT51 polymerization on defined Lipid II to directly compare polarity, processivity, and chain-length distributions under matched conditions.
6. **Targeted study of aPBP-as-divisome organisms** (*C. difficile* and relatives) to define what molecular features allow an aPBP to substitute for FtsW/FtsI, informing pathogen-specific antibiotic strategies.

---

## 11. Key References

| PMID | Contribution |
|---|---|
| [27525505](https://pubmed.ncbi.nlm.nih.gov/27525505/) | SEDS proteins are a widespread family of PG polymerases (redefines the polymerase concept). |
| [27643381](https://pubmed.ncbi.nlm.nih.gov/27643381/) | Two semi-autonomous polymerase systems: SEDS in cytoskeletal machines vs. aPBPs outside. |
| [29590088](https://pubmed.ncbi.nlm.nih.gov/29590088/) | RodA structure: 10-TM SEDS fold with catalytically essential TM cavity. |
| [31386359](https://pubmed.ncbi.nlm.nih.gov/31386359/) | SEDS grow glycan at the reducing end; distinct substrate/lipid preferences. |
| [33857142](https://pubmed.ncbi.nlm.nih.gov/33857142/) | Conserved SEDS–bPBP activation relay: FtsQLB→FtsI→FtsW. |
| [42537644](https://pubmed.ncbi.nlm.nih.gov/42537644/) | Cryo-EM of FtsWIQBL: FtsI-mediated activation of FtsW; β-lactam rearrangements. |
| [34429361](https://pubmed.ncbi.nlm.nih.gov/34429361/) | aPBP bifunctionality; LpoA required to stimulate PBP1a polymerase. |
| [40691462](https://pubmed.ncbi.nlm.nih.gov/40691462/) | LpoB "hit-and-run" allosteric activation of PBP1b. |
| [27329754](https://pubmed.ncbi.nlm.nih.gov/27329754/) | Redundant DD-carboxypeptidases; PBP6b loss raises pentapeptide, distorts shape. |
| [40777447](https://pubmed.ncbi.nlm.nih.gov/40777447/) | DD-CPase reaction: cleaves terminal D-Ala, penta→tetra. |
| [34311584](https://pubmed.ncbi.nlm.nih.gov/34311584/) | Diverse bacteria build walls without any aPBP. |
| [41118402](https://pubmed.ncbi.nlm.nih.gov/41118402/) | *C. difficile* divides with class-A PBP1 instead of FtsW/FtsI. |
| [31086309](https://pubmed.ncbi.nlm.nih.gov/31086309/) | *S. aureus* uses two SEDS–bPBP pairs (RodA–PBP3, FtsW–PBP1). |
| [30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/) | 4→3 crosslinks by PBPs (β-lactam target) vs. 3→3 LDT bypass. |
| [17347437](https://pubmed.ncbi.nlm.nih.gov/17347437/) | GT51 glycosyltransferase fold is distinct from other GT classes. |
| [11466281](https://pubmed.ncbi.nlm.nih.gov/11466281/) | Monofunctional GT51 (MGT/MtgA) polymerizes PG alone; moenomycin-sensitive. |
| [31031115](https://pubmed.ncbi.nlm.nih.gov/31031115/) | FzlA links FtsZ to SEDS–PBP activation; conserved cytoskeleton gating. |
| [20417640](https://pubmed.ncbi.nlm.nih.gov/20417640/) | Sporulation-specific SEDS–bPBP pair SpoVE–SpoVD. |
| [35274942](https://pubmed.ncbi.nlm.nih.gov/35274942/) | Review: Lipid II flipping (MurJ) and the SEDS polymerase discovery. |

---

*Prepared as a commissioned review synthesis. All mechanistic claims are anchored to the cited primary literature and authoritative reviews; where evidence is organism-specific or indirect, this is stated explicitly.*


## Artifacts

- [OpenScientist final report](bacterial_peptidoglycan_polymerization_crosslinking-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_peptidoglycan_polymerization_crosslinking-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:35274942
2. PMID:30275297
3. PMID:27525505
4. PMID:27643381
5. PMID:31386359
6. PMID:29590088
7. PMID:33857142
8. PMID:42537644
9. PMID:31031115
10. PMID:34429361
11. PMID:40691462
12. PMID:17347437
13. PMID:11466281
14. PMID:40777447
15. PMID:27329754
16. PMID:34311584
17. PMID:41118402
18. PMID:31086309
19. PMID:20417640