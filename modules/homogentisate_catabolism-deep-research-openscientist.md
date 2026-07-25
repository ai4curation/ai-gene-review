---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T11:11:11.596211'
end_time: '2026-07-23T11:45:34.103856'
duration_seconds: 2062.51
template_file: templates/module_research.md.j2
template_variables:
  module_title: Homogentisate catabolism
  module_summary: A reusable three-reaction pathway that opens the aromatic ring of
    homogentisate to form maleylacetoacetate, isomerizes maleylacetoacetate to fumarylacetoacetate,
    and hydrolyzes fumarylacetoacetate to fumarate and acetoacetate. This lower pathway
    accepts homogentisate from multiple upstream aromatic-substrate routes and ends
    at metabolites that can enter central carbon metabolism.
  module_outline: "- Homogentisate catabolism\n  - 1. homogentisate ring cleavage\n\
    \  - Homogentisate oxidative ring cleavage\n    - Homogentisate 1,2-dioxygenase\
    \ (molecular player: HmgA homogentisate 1,2-dioxygenases; activity or role: homogentisate\
    \ 1,2-dioxygenase activity)\n  - 2. maleylacetoacetate isomerization\n  - Maleylacetoacetate\
    \ isomerization\n    - Maleylacetoacetate isomerase (molecular player: HmgC maleylacetoacetate\
    \ isomerases; activity or role: maleylacetoacetate isomerase activity)\n  - 3.\
    \ fumarylacetoacetate hydrolysis\n  - Fumarylacetoacetate hydrolysis\n    - Fumarylacetoacetase\
    \ (molecular player: HmgB fumarylacetoacetases; activity or role: fumarylacetoacetase\
    \ activity)"
  module_connections: '- Homogentisate oxidative ring cleavage feeds into Maleylacetoacetate
    isomerization: HmgA produces maleylacetoacetate for HmgC.

    - Maleylacetoacetate isomerization feeds into Fumarylacetoacetate hydrolysis:
    HmgC produces fumarylacetoacetate for HmgB.'
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: homogentisate_catabolism-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: homogentisate_catabolism-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Homogentisate catabolism

## Working Scope

A reusable three-reaction pathway that opens the aromatic ring of homogentisate to form maleylacetoacetate, isomerizes maleylacetoacetate to fumarylacetoacetate, and hydrolyzes fumarylacetoacetate to fumarate and acetoacetate. This lower pathway accepts homogentisate from multiple upstream aromatic-substrate routes and ends at metabolites that can enter central carbon metabolism.

## Provisional Biological Outline

- Homogentisate catabolism
  - 1. homogentisate ring cleavage
  - Homogentisate oxidative ring cleavage
    - Homogentisate 1,2-dioxygenase (molecular player: HmgA homogentisate 1,2-dioxygenases; activity or role: homogentisate 1,2-dioxygenase activity)
  - 2. maleylacetoacetate isomerization
  - Maleylacetoacetate isomerization
    - Maleylacetoacetate isomerase (molecular player: HmgC maleylacetoacetate isomerases; activity or role: maleylacetoacetate isomerase activity)
  - 3. fumarylacetoacetate hydrolysis
  - Fumarylacetoacetate hydrolysis
    - Fumarylacetoacetase (molecular player: HmgB fumarylacetoacetases; activity or role: fumarylacetoacetase activity)

## Known Relationships Among Steps

- Homogentisate oxidative ring cleavage feeds into Maleylacetoacetate isomerization: HmgA produces maleylacetoacetate for HmgC.
- Maleylacetoacetate isomerization feeds into Fumarylacetoacetate hydrolysis: HmgC produces fumarylacetoacetate for HmgB.

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

# Homogentisate Catabolism: A Mechanistic Review

*A concise, review-style synthesis of the three-reaction "lower" pathway that
opens homogentisate and delivers its carbon to central metabolism.*

---

## 1. Executive Summary

Homogentisate (2,5-dihydroxyphenylacetate, HGA) catabolism is a compact,
evolutionarily ancient, three-enzyme module that dismantles an aromatic ring and
routes its carbon skeleton into central carbon metabolism. The module comprises,
in obligate order:

1. **Homogentisate 1,2-dioxygenase (HmgA / HGD)** — an Fe(II)-dependent
   dioxygenase that oxidatively cleaves the aromatic ring to yield
   **maleylacetoacetate (MAA)**.
2. **Maleylacetoacetate isomerase (HmgC / MAAI = GSTZ1)** — a
   glutathione-dependent *cis→trans* isomerase that converts MAA to
   **fumarylacetoacetate (FAA)**.
3. **Fumarylacetoacetate hydrolase / fumarylacetoacetase (HmgB / FAH)** — a
   metal-dependent C–C bond hydrolase that splits FAA into **fumarate**
   (a TCA-cycle intermediate) and **acetoacetate** (a ketone-body precursor).

This module is the shared *terminal* segment of tyrosine/phenylalanine
catabolism in animals and of numerous microbial and fungal aromatic-degradation
routes that converge on homogentisate. Its clinical and physiological importance
is underscored by two human inborn errors: **alkaptonuria** (loss of HGD) and
**hereditary tyrosinemia type I / HT1** (loss of FAH). Notably, the middle step
(MAAI/GSTZ1) is partially redundant with a non-enzymatic glutathione-mediated
isomerization, which likely explains why no unequivocal human "MAAI deficiency"
disease exists, in contrast to the flanking steps.

---

## 2. Definition and Biological Boundaries

**What is included.** The system, sensu stricto, is exactly three reactions:
ring cleavage (HGA → MAA), isomerization (MAA → FAA), and hydrolysis
(FAA → fumarate + acetoacetate). Its **entry metabolite** is homogentisate and
its **exit metabolites** are fumarate and acetoacetate. Everything between those
boundaries defines the pathway.

**What feeds in but is not part of it (upstream boundary).** Homogentisate is a
*convergence node*. In vertebrates it is produced from 4-hydroxyphenylpyruvate by
**4-hydroxyphenylpyruvate dioxygenase (HPD/HPPD)**, itself downstream of tyrosine
aminotransferase acting on tyrosine (and, before that, phenylalanine hydroxylase
acting on phenylalanine). In microbes and fungi, homogentisate is generated from
diverse aromatic substrates — e.g., an ethylbenzene → styrene → phenylacetate →
homogentisate route in the fungus *Exophiala lecanii-corni* (PMID: 15731901).
These upstream reactions (HPPD in particular) are frequently conflated with the
pathway but are **accessory feeder reactions**, not part of the ring-opening
module itself. The clinical drug **nitisinone (NTBC)**, used in HT1 and
alkaptonuria, acts *upstream* by inhibiting HPPD — it does not touch any of the
three core enzymes (PMID: 41003839, 33375092).

**What should be treated separately (commonly confused).**
- **Gentisate (2,5-dihydroxybenzoate) 1,2-dioxygenase pathways.** Gentisate
  catabolism is a *parallel but distinct* microbial ring-cleavage route with a
  similar name and similar chemistry (dioxygenolytic cleavage to
  maleylpyruvate, then a GSH-dependent isomerase to fumarylpyruvate, then a
  hydrolase). The enzymes, substrates, and gene sets differ; do not merge the two.
- **GSTZ1's xenobiotic/moonlighting biology.** Because MAAI *is* GSTZ1,
  much literature discusses its role in dichloroacetate (DCA) biotransformation,
  redox/ferroptosis signaling (NRF2/GPX4, HMGB1/GPX4), and cancer metabolism
  (PMID: 37742772, 33931597, 36905252, 35562974). These are genuine activities of
  the same protein but are **not the isomerization step** of homogentisate
  catabolism and should be kept conceptually distinct.
- **Pyomelanin / ochronotic pigment formation.** When the pathway is blocked,
  accumulated homogentisate auto-oxidizes and polymerizes into pigment
  (pyomelanin in microbes; ochronotic pigment in human connective tissue). This
  is a *downstream consequence of pathway failure*, not a pathway reaction
  (PMID: 19028908, 31020477).

**Competing definitions.** The main terminological variation is nomenclature:
the microbial locus names **hmgA/hmgB/hmgC** versus the mammalian gene names
**HGD/FAH/GSTZ1(MAAI)**. Some literature draws the pathway boundary to *include*
HPPD (the "homogentisate branch of tyrosine catabolism"); others, as in this
brief, restrict it to the three ring-processing reactions. Both usages are
defensible provided the boundary is stated.

---

## 3. Mechanistic Overview

The current best model is a strictly linear, non-branched relay in which each
product is the next enzyme's substrate:

```
   Homogentisate
        │   HGD/HmgA  (Fe2+, O2)   — oxidative aromatic ring cleavage
        ▼
   Maleylacetoacetate (cis)
        │   MAAI/GSTZ1/HmgC  (glutathione)   — cis→trans isomerization
        ▼
   Fumarylacetoacetate (trans)
        │   FAH/HmgB  (Mg2+/Ca2+, H2O)   — C–C bond hydrolysis
        ▼
   Fumarate  +  Acetoacetate  → central carbon metabolism
```

**Step 1 — Ring cleavage (obligatory).** HGD is a non-heme Fe(II) dioxygenase.
Computational (hybrid-DFT and QM/MM) studies converge on a mechanism with three
chemical stages: formation of an Fe-bound **peroxo/alkylperoxo intermediate**,
**homolytic O–O cleavage** producing an arene-oxide radical, and finally
scission of the six-membered ring to the ring-opened product (PMID: 16332080,
27119315). The regiochemistry (intra- vs extra-diol relative to the
iron-coordinating substituents) is controlled by the relative barriers for decay
of the arene-oxide radical intermediate (PMID: 16332080). Both oxygen atoms of O2
are incorporated, defining this as an intradiol-type dioxygenase reaction on a
homogentisate substrate.

**Step 2 — Isomerization (obligatory chemically, but conditionally
enzyme-dependent).** MAA is produced in the *cis* (maleyl) configuration; entry
into the final hydrolysis requires the *trans* (fumaryl) configuration. MAAI
(=GSTZ1) uses glutathione as a catalytic cofactor to rotate about the double
bond. Crucially, this *cis→trans* isomerization can also occur **non-enzymatically
via glutathione** — a bypass demonstrated directly in vitro and inferred in vivo
from MAAI-knockout mice, which remain viable but accumulate FAA and
succinylacetone (PMID: 12052898). Thus the *isomerization event* is obligatory,
but the *enzyme* is accessory/facultative.

**Step 3 — Hydrolysis (obligatory).** FAH catalyzes an unusual **C–C bond
hydrolysis**, cleaving FAA into fumarate and acetoacetate. Structural work
established FAH as the founding member of a novel metalloenzyme fold (a "mixed
β-sandwich roll"), employing a divalent metal ion (Ca2+/Mg2+ observed), a
**Glu–His catalytic dyad activating a water nucleophile**, and a charged
**oxyanion hole** that stabilizes a **tetrahedral alkoxide transition-state
intermediate** (PMID: 10508789, 11154690). Phosphorus-based transition-state
mimics bind with nanomolar affinity and phenocopy the metabolic block, validating
the tetrahedral-intermediate model (PMID: 17064256).

**Obligatory ordering and no shortcuts.** The three reactions must proceed in
order because each substrate is chemically defined by the prior step (an intact
ring cannot be hydrolyzed by FAH; *cis*-MAA is not the FAH substrate). No
non-enzymatic bypass is known for steps 1 or 3, which is why their loss produces
frank human disease.

---

## 4. Major Molecular Players and Active Assemblies

| Step | Enzyme (microbial / mammalian) | EC | Cofactor / metal | Products | Assembly & structural notes |
|------|-------------------------------|----|------------------|----------|-----------------------------|
| 1 | Homogentisate 1,2-dioxygenase — **HmgA / HGD** | 1.13.11.5 | Non-heme **Fe(II)**, O2 | Maleylacetoacetate | Human HGD: 445 aa, gene on 3q13, 14 exons; oligomeric (multi-subunit) enzyme; active site with 3 His + Glu iron ligands in the modeled chemistry (PMID: 16332080, 41236909) |
| 2 | Maleylacetoacetate isomerase — **HmgC / MAAI = GSTZ1** | 5.2.1.2 | **Glutathione** (catalytic) | Fumarylacetoacetate | Member of the cytosolic **GST superfamily** (zeta class); Cys16 implicated in DCA-mediated inactivation; most abundant in liver (PMID: 21303221, 37742772) |
| 3 | Fumarylacetoacetate hydrolase — **HmgB / FAH** | 3.7.1.2 | **Mg2+/Ca2+**, H2O | Fumarate + acetoacetate | Novel α/β "FAH-superfamily" fold; N-terminal (~120 aa) + C-terminal (~300 aa) domains; **catalytically active dimer** in equilibrium with an inactive, aggregation-prone monomer; Glu–His–water triad + oxyanion hole (PMID: 10508789, 11154690, 31300554) |

**Genomic organization.** In many microbes and fungi the genes are clustered and
co-regulated with the feeder enzymes. In *Aspergillus fumigatus*, the
L-tyrosine/L-phenylalanine degradation cluster contains **hppD, hmgX, hmgA, fahA,
maiA, hmgR** (the last a pathway-specific regulator), tying homogentisate
processing to a single inducible operon-like unit (PMID: 31020477, 19028908). In
mammals the three genes are unlinked (HGD on 3q13; FAH on 15q; GSTZ1 on 14q) and
regulated independently, but co-expressed in the same organs (liver hepatocytes
and kidney proximal tubule; PMID: 12052898).

---

## 5. Evolutionary and Cell-Biological Variation

**Deep conservation.** All three activities are found across bacteria, fungi,
plants, and animals, reflecting an ancient role in aromatic-ring catabolism that
predates the split of these lineages. FAH in particular has **no sequence
homologs among other hydrolase classes** and defines its own fold/superfamily
(PMID: 10508789), implying an ancient and singular evolutionary invention for
C–C hydrolysis. HGD belongs to the broad non-heme Fe(II) dioxygenase repertoire
that underpins microbial aromatic degradation globally.

**Lineage variation.**
- **Microbes/fungi:** homogentisate catabolism is the **central/lower funnel**
  for catabolism of many aromatics (tyrosine, phenylacetate, styrene,
  ethylbenzene, nicotinate-related aromatics), typically clustered and
  substrate-inducible. Blocking step 1 diverts flux to **pyomelanin**, a stress-
  and virulence-associated pigment (PMID: 19028908, 31020477, 15731901).
- **Animals:** the pathway is the **terminal segment of Tyr/Phe catabolism**,
  restricted largely to **liver and kidney**, and gated developmentally and
  nutritionally (induced by dietary aromatic amino-acid load).
- **Protein-family expansion (step 2):** MAAI sits inside the large **glutathione
  transferase (GST) superfamily**. The **zeta class (GSTZ1)** is the member that
  carries the ancestral isomerase activity; the alpha/mu/pi classes are later,
  lineage-specific expansions specialized for xenobiotic conjugation and are
  **not** good proxies for the ancestral homogentisate-pathway role. For
  understanding the ancestral function, **GSTZ1/zeta is the representative
  member** (PMID: 21303221).

**Cell-type / physiological state.** GSTZ1/MAAI expression and activity depend on
age and intracellular chloride, and are highest in liver (PMID: 37742772). In
mammals, the primary target organ of pathway dysfunction is the **kidney**
(proximal tubule) for MAA-related accumulation and the **liver** for FAA/
succinylacetone toxicity (PMID: 12052898, 15277241).

**Alternative routes to the same outcome.** The *cis→trans* isomerization can be
achieved by (i) the GSTZ1 enzyme or (ii) a **non-enzymatic glutathione-mediated**
reaction — molecularly different means to the same chemical end (PMID: 12052898).
At the whole-pathway level, **gentisate catabolism** achieves the analogous
outcome (aromatic-ring opening → fumarate + pyruvate) by a *parallel* enzyme set,
representing a convergent solution rather than a variant of this pathway.

---

## 6. Constraints, Dependencies, and Failure Modes

**Mandatory ordering.** Ring cleavage → isomerization → hydrolysis is fixed by
substrate chemistry (Section 3). FAH cannot act on an intact ring; the hydrolase
requires the *trans* isomer.

**Compartment / cell-type constraints (mammals).** The complete pathway operates
in hepatocytes and renal proximal tubule cells; GSTZ1 is predominantly cytosolic
(several-fold higher in cytoplasm than mitochondria; PMID: 37742772).

**Failure modes and their differential severity — an informative asymmetry.**
- **Loss of step 1 (HGD):** **alkaptonuria** — homogentisate accumulates,
  auto-oxidizes, polymerizes, and deposits as ochronotic pigment in cartilage,
  connective tissue, heart valves, leading to arthropathy and valvular disease
  (PMID: 41236909, 40938761). Severe, but slowly progressive.
- **Loss of step 2 (MAAI/GSTZ1):** **no clear human disease**; knockout mice are
  viable, thanks to the glutathione bypass, though they accumulate FAA and
  succinylacetone and show liver/kidney pathology under aromatic-amino-acid
  overload (PMID: 12052898, 15277241, 37742772). This is the strongest evidence
  that the isomerase, uniquely among the three, is **facultative**.
- **Loss of step 3 (FAH):** **hereditary tyrosinemia type I (HT1)** — the most
  severe error, causing accumulation of FAA and the derived toxin
  **succinylacetone**, with hepatic failure, renal tubulopathy, neurologic crises,
  and hepatocellular carcinoma risk (PMID: 10508789, 31611405). Most HT1 mutations
  act by **destabilizing the active FAH dimer and accelerating aggregation**,
  not merely by ablating catalysis (PMID: 31300554).

**Evidence ruling out otherwise-plausible paths.**
- The **MAAI/FAH double-knockout is rapidly lethal**, demonstrating that
  MAA→FAA *does* proceed in the absence of MAAI (via GSH) — otherwise the double
  mutant would be no worse than the FAH single mutant (PMID: 12052898). This
  simultaneously proves the bypass exists and that FAA is the toxic bottleneck.
- **Nitisinone (HPPD inhibition) rescues HT1** by shutting off homogentisate
  production upstream, confirming that toxicity flows through the pathway rather
  than from tyrosine itself, and that the three core enzymes are downstream of the
  druggable choke point (PMID: 41003839, 33375092).

---

## 7. Controversies and Open Questions

1. **Why is there no human MAAI-deficiency disease?** The dominant explanation is
   the glutathione non-enzymatic bypass (PMID: 12052898), but whether additional
   enzymatic redundancy exists, and how efficient the bypass is in human liver in
   vivo, remains incompletely quantified (PMID: 37742772).
2. **HGD structural mechanism at atomic resolution.** The ring-cleavage mechanism
   rests substantially on computational models (DFT/QM-MM; PMID: 16332080,
   27119315) and older crystallography; the protonation state of the substrate C2
   hydroxyl (ionized vs non-ionized pathway) and the precise regiochemical
   control are still debated.
3. **FAH oligomeric state and pathogenicity.** The monomer–dimer equilibrium and
   aggregation model for HT1 (PMID: 31300554) reframes many mutations as
   folding/stability defects, motivating pharmacological-chaperone strategies —
   but which mutations are catalytic vs conformational is not fully mapped.
4. **Moonlighting vs. metabolic roles of GSTZ1.** A large, partly separate
   literature links GSTZ1 to ferroptosis, NRF2/GPX4 redox signaling, DCA
   pharmacology, and cancer (PMID: 33931597, 36905252, 35562974, 35979621). How
   much of this reflects the isomerase's metabolic function (accumulating tyrosine
   intermediates) versus independent activities of the same protein is unresolved
   and a frequent source of cross-organism/cross-assay conflation.
5. **Cross-organism extrapolation.** Mechanistic claims often mix data from
   humans, mice, fungi, and bacteria. The enzymology is conserved, but regulation,
   tissue distribution, gene clustering, and physiological consequences differ;
   claims should be anchored to the organism studied.
6. **Residual disease under nitisinone.** Even with upstream HPPD blockade, HT1
   models retain molecular remnants of liver disease and HCC risk (PMID: 36980965),
   indicating incomplete understanding of the toxic intermediates and their
   long-term signaling effects.

---

## 8. Key References

- Timm DE et al. *Crystal structure and mechanism of a carbon-carbon bond
  hydrolase* (FAH fold, Glu–His–water triad, products). Nat Struct Biol 1999.
  **PMID: 10508789**
- Bateman RL et al. *Mechanistic inferences from the crystal structure of FAH
  with a bound phosphorus-based inhibitor* (tetrahedral intermediate, Mg2+).
  PNAS 2001. **PMID: 11154690**
- Bateman RL et al. *Slow-onset inhibition of FAH by phosphinate transition-state
  mimics* (nM inhibitors, in vivo phenocopy). Biochem J 2007. **PMID: 17064256**
- Macias I et al. *HT1-associated FAH mutations reduce stability and increase
  aggregation* (dimer/monomer equilibrium). J Biol Chem 2019. **PMID: 31300554**
- Borowski T et al. *Catalytic reaction mechanism of homogentisate dioxygenase:
  DFT study* (peroxo → O–O homolysis → ring scission). 2005. **PMID: 16332080**
- Qi C et al. *QM/MM study of aromatic ring cleavage by homogentisate
  dioxygenase.* 2016. **PMID: 27119315**
- Fernández-Cañón JM et al. *MAAI/GSTZ-deficient mice reveal a glutathione-
  dependent non-enzymatic bypass* (viability, double-mutant lethality). PNAS 2002.
  **PMID: 12052898**
- Board PG, Anders MW. *Glutathione transferase zeta: discovery, catalysis,
  Gstz1-/- mice* (MAAI = GSTZ1). 2011. **PMID: 21303221**
- Lim CE et al. *Gstz1-/- mice: pathology and compensatory GST induction*
  (succinylacetone accumulation). 2004. **PMID: 15277241**
- Stacpoole PW. *Clinical physiology and pharmacology of GSTZ1/MAAI* (no clear
  human deficiency disease; DCA; tissue distribution). 2023. **PMID: 37742772**
- Schmaler-Ripcke J et al. *Pyomelanin via tyrosine degradation in A. fumigatus*
  (hmgA/hppD deletions). 2009. **PMID: 19028908**
- Perez-Cuesta U et al. *Melanin and pyomelanin in A. fumigatus* (hppD, hmgX,
  hmgA, fahA, maiA, hmgR cluster). 2020. **PMID: 31020477**
- Gunsch CK et al. *Homogentisate-1,2-dioxygenase in Exophiala lecanii-corni*
  (aromatic pollutant funnel to homogentisate). 2005. **PMID: 15731901**
- Azami M et al. *HGD gene analysis in alkaptonuric ochronosis* (gene structure).
  2025. **PMID: 41236909**
- Mascarello A et al. *Nitisinone reduces succinylacetone in HT1* (upstream HPPD
  block). 2025. **PMID: 41003839**

---

### Uncertainty statement

The enzymology of the three core reactions is strongly supported by
crystallography, transition-state-mimic inhibitors, computational mechanism, and
genetic knockouts. The greatest uncertainties are (i) the in vivo efficiency and
molecular basis of the MAAI-independent glutathione bypass in humans, (ii) the
atomic-resolution details/regiochemical control of HGD ring cleavage, and (iii)
disentangling GSTZ1's metabolic isomerase role from its reported redox/xenobiotic
"moonlighting" activities. Regulatory and physiological features vary
substantially across bacteria, fungi, and mammals and should not be extrapolated
between them.


## Artifacts

- [OpenScientist final report](homogentisate_catabolism-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](homogentisate_catabolism-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15731901
2. PMID:41003839
3. PMID:37742772
4. PMID:19028908
5. PMID:16332080
6. PMID:12052898
7. PMID:10508789
8. PMID:17064256
9. PMID:21303221
10. PMID:31020477
11. PMID:41236909
12. PMID:31300554
13. PMID:33931597
14. PMID:36980965
15. PMID:11154690
16. PMID:27119315
17. PMID:15277241