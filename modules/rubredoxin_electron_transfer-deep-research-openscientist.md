---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:47:05.010444'
end_time: '2026-07-11T14:57:47.895896'
duration_seconds: 642.89
template_file: templates/module_research.md.j2
template_variables:
  module_title: Rubredoxin electron transfer
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00191 module for the small
    iron-binding rubredoxin electron carrier RubA (PP_5315, UniProtKB:Q88C68). RubA
    is annotated as transferring electrons in a hydrocarbon hydroxylating system,
    likely functioning with the adjacent rubredoxin reductase AlkT as an electron-transfer
    component for alkane monooxygenase chemistry.
  module_outline: "- Rubredoxin electron transfer\n  - 1. Rubredoxin electron carrier\
    \ for hydrocarbon hydroxylation\n  - RubA rubredoxin electron-transfer step\n\
    \    - rubA: rubredoxin electron carrier (molecular player: PSEPK rubA; activity\
    \ or role: electron transfer activity)"
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rubredoxin_electron_transfer-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rubredoxin_electron_transfer-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Rubredoxin electron transfer

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00191 module for the small iron-binding rubredoxin electron carrier RubA (PP_5315, UniProtKB:Q88C68). RubA is annotated as transferring electrons in a hydrocarbon hydroxylating system, likely functioning with the adjacent rubredoxin reductase AlkT as an electron-transfer component for alkane monooxygenase chemistry.

## Provisional Biological Outline

- Rubredoxin electron transfer
  - 1. Rubredoxin electron carrier for hydrocarbon hydroxylation
  - RubA rubredoxin electron-transfer step
    - rubA: rubredoxin electron carrier (molecular player: PSEPK rubA; activity or role: electron transfer activity)

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

# Rubredoxin Electron Transfer: RubA and the Alkane-Hydroxylase Redox Relay of *Pseudomonas putida* KT2440

*A commissioned review-style synthesis. Focal system: the UniPathway UPA00191 rubredoxin electron-carrier module built around RubA (PP_5315; UniProtKB:Q88C68) of* Pseudomonas putida *KT2440.*

---

## 1. Executive summary

Rubredoxins are the smallest and structurally simplest of the biological iron redox proteins: a single non-heme iron held in a tetrahedral cage of four cysteine thiolates (an "[1Fe–0S]" centre), with no acid-labile sulfide. In alkanotrophic bacteria they serve one particularly well-defined job — ferrying single electrons from a soluble NAD(P)H-dependent flavoenzyme (rubredoxin reductase, AlkT) to a membrane-bound non-heme **diiron** alkane hydroxylase (AlkB), which uses those electrons to reductively activate O₂ and hydroxylate the terminal carbon of an otherwise inert alkane. In *P. putida* KT2440 the rubredoxin filling this role is **RubA (PP_5315)**. The system is therefore a compact, three-component electron-transfer chain: **NADH → AlkT (FAD/NAD flavoprotein) → RubA (rubredoxin) → AlkB (diiron ω-hydroxylase)** (PMID 34990970; PMID 2319593; PMID 12804773).

Three points define the biology. First, RubA is an **obligatory but purely accessory** carrier: it performs no chemistry on the substrate, only electron relay, and the diferric AlkB centre cannot turn over without it. Second, not all rubredoxins are interchangeable in this task — productive reduction of AlkB requires the "AlkG2/RubA-functional" surface class, whereas a closely related and highly conserved "AlkG1" class cannot deliver electrons to AlkB despite being an intact rubredoxin (PMID 11872724). Third, the rubredoxin fold is deeply ancient and broadly re-used (P450 reduction, oxidative-stress defence, hydrogenase-like chemistry in engineered variants), so the alkane role is best understood as **one specialization of a universal electron-carrier scaffold** whose redox potential and partner preferences are locally tuned (PMID 33618255; PMID 15382226).

The principal uncertainties for the KT2440 module specifically are (i) the exact domain architecture and iron stoichiometry of RubA (single- vs two-domain), (ii) whether KT2440 uses RubA physiologically for alkane growth given its incomplete/atypical alk gene complement relative to the archetypal GPo1 system, and (iii) the structural basis of the AlkT→RubA→AlkB docking events, which appear transient and are only partly resolved.

---

## 2. Definition and biological boundaries

**What is inside the system.** The RubA module (UPA00191) comprises exactly three functional parts and the reactions that connect them:

1. **Rubredoxin reductase (AlkT)** — a ~41 kDa cytoplasmic flavoprotein that oxidizes NADH and reduces the rubredoxin. It carries an N-terminal FAD-binding βαβ fingerprint and a central NAD(P)-binding fingerprint, placing it firmly in the glutathione-reductase/ferredoxin-reductase structural family of pyridine-nucleotide:disulfide/flavin oxidoreductases (PMID 2319593).
2. **Rubredoxin (RubA / AlkG)** — the FeS₄ single-electron carrier that is the subject of this review.
3. **Alkane ω-hydroxylase (AlkB)** — the integral-membrane, non-heme **diiron** terminal oxidase that receives the electrons and does the C–H activation chemistry (PMID 12804773).

The **boundary of the module** is therefore: electrons *in* from NADH via AlkT; electrons *out* into the AlkB diiron centre. Everything downstream of hydroxylation (the alcohol dehydrogenase AlkJ, aldehyde dehydrogenase AlkH, and the acyl-CoA/β-oxidation machinery that consumes the fatty acid) belongs to the broader alkane-catabolic pathway but is **not** part of the electron-transfer module and should be treated separately.

**What is often confused with it, and should be kept separate.**

- **Ferredoxins and flavodoxins.** Rubredoxins are frequently lumped with "ferredoxins" as generic bacterial electron carriers, but they are chemically distinct: rubredoxin has a mononuclear Fe(III/II) thiolate site with **no inorganic sulfide**, whereas ferredoxins carry [2Fe–2S] or [4Fe–4S] clusters. Confusingly, some AlkB-family enzymes are naturally fused to a **ferredoxin + ferredoxin-reductase** electron-transfer module rather than a rubredoxin one (PMID 34990970); these are functional analogues but a different molecular solution and should not be described as "rubredoxin systems."
- **Cytochrome P450 alkane/fatty-acid hydroxylases (e.g., CYP153, CYP52).** These soluble heme-thiolate monooxygenases hydroxylate alkanes/fatty acids using their own ferredoxin/FAD or flavoprotein reductase partners. They are an *alternative route to the same chemical outcome* (terminal/sub-terminal hydroxylation) but are mechanistically unrelated to the RubA→AlkB relay.
- **Rubredoxin in oxidative-stress defence.** In many anaerobes and in *Mycobacterium*, rubredoxins shuttle electrons in oxygen-detoxification chains (e.g., toward superoxide/oxygen reductases) or to cytochrome P450s (PMID 33618255). These are legitimate rubredoxin functions but a different physiological system; the alkane role is only one branch of rubredoxin biology.

**Competing definitions.** The nomenclature is genuinely tangled. The archetypal *P. putida* GPo1 (historically "*P. oleovorans*") alkane rubredoxin is called **AlkG**, and is an unusual **two-domain, two-iron** protein (PMID 15023067). Other organisms encode single-domain rubredoxins named **RubA** (e.g., *P. aeruginosa* RubA1/RubA2; *P. putida* KT2440 RubA/PP_5315) that functionally substitute for GPo1 AlkG in octane oxidation (PMID 14574114; PMID 11872725). "AlkG," "AlkG2," and "RubA" thus refer to functionally equivalent alkane-system rubredoxins that differ in domain count and naming convention across strains. This review uses **RubA** for the KT2440 protein and **AlkG-type/AlkG2-type** for the functional class.

---

## 3. Mechanistic overview

**Best current model (sequence of events).**

1. **NADH oxidation at AlkT.** AlkT binds NADH and FAD; hydride transfer from NADH reduces the flavin (FAD → FADH⁻/FADH₂) (PMID 2319593).
2. **Flavin → rubredoxin electron transfer.** Reduced AlkT transfers electrons **one at a time** to the rubredoxin iron, cycling RubA between Fe(III) and Fe(II). This is the step where the two-electron chemistry of the pyridine nucleotide is split into the one-electron currency required downstream. The AlkG/RubA reduction potential sits in the range expected for such carriers (bacterial rubredoxins ~ −264 mV vs Ag/AgCl for *M. tuberculosis* RubB; comparable low-potential range for alkane rubredoxins) (PMID 33618255).
3. **Rubredoxin → AlkB electron delivery.** Reduced RubA docks onto AlkB and delivers one electron to the diferric [Fe(III)–Fe(III)] centre; a second RubA turnover delivers the second electron, generating the diferrous [Fe(II)–Fe(II)] state (PMID 34990970).
4. **O₂ activation and hydroxylation at AlkB.** The reduced diiron centre binds and activates O₂, generating a high-valent iron–oxo species that abstracts a hydrogen and inserts oxygen into the terminal C–H bond, yielding a primary alcohol (ω-hydroxylation). The eight conserved histidines that ligate the diiron site are each essential (PMID 12804773).

**Obligatory vs conditional vs accessory steps.**

- **Obligatory:** every step above is required for a single catalytic turnover of AlkB. RubA is obligatory *as an electron conduit* — without a functional AlkG-type rubredoxin, AlkB cannot be reduced and no hydroxylation occurs (PMID 11872724).
- **Conditional / substitutable:** the *identity* of the reductase and rubredoxin is conditional. Rubredoxins from other alkane systems can replace GPo1 AlkG in octane oxidation (PMID 11872725), and *P. aeruginosa* RubA1/RubA2 and RubB can substitute for their GPo1 counterparts (PMID 14574114). Some AlkB relatives dispense with separate carriers entirely by fusing a ferredoxin/ferredoxin-reductase module to the hydroxylase, requiring only NADH (PMID 34990970).
- **Accessory:** RubA itself is accessory to the chemistry — it changes no substrate bond. It is nonetheless indispensable to flux.

**Why the one-electron carrier is needed.** The chemistry couples a two-electron donor (NADH) to a diiron site that must be reduced by two sequential one-electron steps to bind and cleave O₂. A mobile, low-potential single-electron shuttle (rubredoxin) is the adaptor that reconciles these, moving between the soluble flavoenzyme and the membrane-embedded oxidase.

---

## 4. Major molecular players and active assemblies

| Component | Gene / ID | Cofactor / centre | Role | Key evidence |
|---|---|---|---|---|
| Rubredoxin reductase | *alkT* (alkST operon) | FAD + NAD(P) sites | Oxidizes NADH; reduces rubredoxin | PMID 2319593 |
| **Rubredoxin (focus)** | ***rubA* / PP_5315 (Q88C68)**; GPo1 *alkG* | Fe in FeS₄ (Cys₄); "[1Fe–0S]" | One-electron shuttle AlkT→AlkB | PMID 11872724; PMID 15023067; PMID 33618255 |
| Alkane ω-hydroxylase | *alkB* (alkBFGHJKL operon) | Non-heme diiron, 8 His ligands; integral membrane | O₂ activation, terminal C–H hydroxylation | PMID 12804773; PMID 34990970 |

**Rubredoxin structural unit.** The canonical rubredoxin fold is a small (~50–55 residue) β-sheet-and-loop domain presenting two **CXXCG "cysteine-knuckle" motifs** that supply the four Fe-coordinating thiolates. Reduction potential is tuned locally: NH···S hydrogen bonds from backbone amides to the cysteine sulfurs and the size/packing of second-shell residues (e.g., Val44 in *Clostridium pasteurianum* Rd) modulate the Fe(III/II) potential in a side-chain-size-dependent way, and surface residues govern partner docking (PMID 15382226).

**Alkane-system specializations of the fold.** Alkane rubredoxins carry two CXXCG iron-binding motifs and a characteristic set of **four non-conserved negatively charged surface residues** implicated in partner recognition (PMID 11872724). The GPo1 AlkG protein is a striking elaboration: **two rubredoxin folds joined by a ~70-residue flexible linker**, typically metallated in only one (C-terminal) domain, with SAXS/NMR showing the domains are separated and mobile — consistent with conformational adjustment during docking to AlkT/AlkB (PMID 15023067). Whether KT2440 RubA is single- or two-domain is a strain-level question (single-domain RubA proteins are common, e.g., *P. aeruginosa*), and is one of the open structural points below.

**The reductase.** AlkT belongs to the two-dinucleotide-binding-domain flavoprotein oxidoreductases; its N-terminal FAD site and internal NAD(P) site are diagnostic βαβ Rossmann fingerprints (PMID 2319593).

**The terminal oxidase.** AlkB is an **integral-membrane diiron** enzyme with an eight-histidine ligand set homologous in relative spacing to the non-heme membrane **fatty-acid desaturase / epoxidase / decarbonylase** superfamily, even though overall sequence similarity is undetectable; each conserved His is essential (PMID 12804773). This places the electron *sink* of the RubA relay in a distinct enzyme family from the heme-thiolate P450s and the Rieske/mononuclear-iron soluble oxygenases.

---

## 5. Evolutionary and cell-biological variation

**Across lineages.** Alkane hydroxylases of the AlkB class are found across Gram-negative and Gram-positive alkanotrophs, with pairwise protein identities as low as ~35% and the *Pseudomonas* enzymes as distant from one another as from those of *Alcanivorax*, *Mycobacterium*, or *Prauserella* (PMID 11872725). Despite this divergence, the **rubredoxin electron-transfer solution is conserved and modular**: rubredoxins from one system routinely complement another in octane oxidation (PMID 11872725; PMID 14574114). The rubredoxin fold itself is ubiquitous across bacteria and archaea and is repeatedly redeployed — for P450 reduction and stress adaptation in *M. tuberculosis* (PMID 33618255), and, in engineered nickel-substituted form, even as a [NiFe]-hydrogenase mimic (PMID 30016865) — underscoring the antiquity and plasticity of the scaffold.

**Two functional sub-types (a key variation).** Alkane rubredoxins split into **AlkG1** and **AlkG2** classes. Only **AlkG2-type** rubredoxins complement GPo1 AlkG and reduce AlkB in octane hydroxylation; **AlkG1-type** rubredoxins are *more highly conserved* across Gram-positive and Gram-negative bacteria yet **cannot** transfer electrons to AlkB. The block is chiefly an **arginine insertion downstream of the second CXXCG motif** (glycine substitutions in the CXXCG motifs have only a limited effect) (PMID 11872724). This is a clean, well-supported example of surface/electrostatic determinants dictating partner specificity rather than the redox centre itself. RubA-type alkane carriers belong to the functional (AlkG2-like) class.

**Architectural variation.** The GPo1 two-domain, two-iron AlkG (PMID 15023067) contrasts with single-domain RubA proteins in other pseudomonads (PMID 14574114). And an entire branch of the AlkB family has **replaced** the rubredoxin relay with a covalently fused **ferredoxin/ferredoxin-reductase** module (ferr_ferrR_AlkB), catalysing C6–C14 hydroxylation with only NADH — a lineage-specific streamlining that eliminates the diffusible carrier (PMID 34990970).

**Physiological state / compartment.** The system is a **membrane–cytoplasm interface** device: AlkT and RubA are soluble/cytoplasmic while AlkB is membrane-integral, so electron delivery is inherently a 3-D docking problem at the inner-membrane surface. Expression is induced by alkane availability (classically via an AraC-family regulator, AlkS, acting on the alk operons in GPo1), tying flux to substrate presence. Strain-to-strain differences in alk gene complement mean the *in vivo* role of a given rubredoxin must be inferred cautiously (see §7).

---

## 6. Constraints, dependencies, and failure modes

**Ordering constraints (what must happen in sequence).**
- Electrons must flow **NADH → AlkT → RubA → AlkB**; the diiron centre must be **fully reduced (di-ferrous) before O₂ binding**, otherwise O₂ activation and C–H cleavage cannot proceed (PMID 34990970).
- The two electrons reach AlkB **sequentially via one-electron RubA turnovers**; there is no direct two-electron hand-off from NADH to the hydroxylase in the rubredoxin-dependent architecture.

**Specificity / mutual-exclusivity constraints.**
- **Partner specificity at the AlkB face:** only AlkG2/RubA-type surfaces productively dock and reduce AlkB; the arginine-insertion AlkG1 surface is excluded (PMID 11872724). This is a discrimination at the *protein–protein* level, not the metal site.
- **Cofactor-class exclusivity:** rubredoxin (FeS₄, no sulfide) and ferredoxin ([Fe–S] cluster) modules are alternative, mutually exclusive electron-relay solutions for AlkB-type hydroxylases (PMID 34990970).
- **Enzyme-family exclusivity of the sink:** electrons from RubA are delivered to a **membrane diiron/desaturase-type** centre (eight essential His), not to a heme or Rieske centre (PMID 12804773).

**Failure modes.**
- Loss/inactivation of the rubredoxin (deletion of AlkG-type Rd) abolishes octane hydroxylation — the defining loss-of-function phenotype used to classify functional vs non-functional rubredoxins (PMID 11872724).
- Substitution of any of the eight conserved AlkB histidines fully inactivates the hydroxylase, i.e., destroying the electron sink stalls the whole relay regardless of RubA function (PMID 12804773).
- Mis-tuned reduction potential (via second-shell/NH···S changes) would throttle electron transfer even with intact folding (PMID 15382226).

**Evidence that rules out otherwise-plausible paths.** Complementation and knockout data (PMID 11872724; PMID 11872725; PMID 14574114) directly demonstrate that (i) a rubredoxin is required, (ii) rubredoxins are cross-complementing within the functional class, and (iii) the AlkG1 class — although a *bona fide* rubredoxin — does **not** short-circuit into AlkB, ruling out the assumption that any rubredoxin suffices.

---

## 7. Controversies and open questions

1. **RubA architecture and iron stoichiometry in KT2440.** The archetypal GPo1 AlkG is two-domain/two-iron (PMID 15023067), but many RubA proteins are single-domain (PMID 14574114). The domain count, metallation state, and functional class (AlkG1 vs AlkG2) of KT2440 RubA (PP_5315) have not, to our reading, been directly characterized biochemically and are inferred from homology. This is the central strain-specific uncertainty.

2. **Physiological role of RubA in *P. putida* KT2440.** KT2440 is not the classic OCT-plasmid alkane degrader; its alkane-catabolic complement differs from GPo1. Whether RubA is deployed for growth on medium-chain alkanes, serves an AlkB-independent role, or is a conserved-but-latent AlkG1-type carrier requires organism-specific experiments rather than extrapolation from *P. oleovorans*/GPo1. Mixing GPo1, *P. oleovorans*, *P. aeruginosa*, and KT2440 data is a real hazard in this literature.

3. **Structure of the electron-transfer complexes.** Docking of AlkT→RubA and RubA→AlkB appears transient and conformationally gated (PMID 15023067), and rubredoxin partner interactions are generally weak/transient (PMID 33618255). High-resolution structures of the productive complexes — especially rubredoxin bound to a membrane AlkB — are lacking, so the electron-transfer geometry and rate-limiting step remain models.

4. **Why keep a highly conserved but non-functional AlkG1 class?** AlkG1-type rubredoxins are more conserved than the functional AlkG2 type yet cannot reduce AlkB (PMID 11872724). Their true physiological role (stress response? another oxidoreductase partner, as for mycobacterial RubB with P450s, PMID 33618255?) is unresolved and is a strong lead for the "ancestral role" question.

5. **Depth of evolutionary origin.** The rubredoxin fold is minimal and ubiquitous and is widely regarded as an ancient metal-binding scaffold; the AlkG1-type (the conserved, housekeeping-like branch) is the better candidate to represent the ancestral rubredoxin role, with the AlkG2/RubA alkane-carrier function a more derived, operon-linked specialization. Direct phylogenetic dating was outside the scope of the sources gathered here and is flagged as a limitation.

**Strength-of-evidence summary.** Strongly supported: the three-component chain and AlkT's flavoprotein identity (PMID 2319593; PMID 34990970); the AlkG2/AlkG1 functional dichotomy and the arginine determinant (PMID 11872724); AlkB as an essential-His membrane diiron enzyme (PMID 12804773); cross-complementation among alkane rubredoxins (PMID 11872725; PMID 14574114). Indirect/model-level: complex structures, KT2440-specific RubA properties, and evolutionary timing.

---

## 8. Key references

- Williams SC, Luongo D, Orman M, Vizcarra CL, Austin RN. *An alkane monooxygenase (AlkB) family in which all electron transfer partners are covalently bound to the oxygen-activating hydroxylase.* 2022. **PMID 34990970.** — Canonical NADH→AlkT→rubredoxin→AlkB chain; ferredoxin-fused AlkB variant.
- van Beilen JB, Neuenschwander M, Smits THM, Roth C, Balada SB, Witholt B. *Rubredoxins involved in alkane oxidation.* 2002. **PMID 11872724.** — AlkG1 vs AlkG2 functional classes; arginine-insertion specificity determinant; CXXCG motifs.
- Smits THM, Balada SB, Witholt B, van Beilen JB. *Functional analysis of alkane hydroxylases from gram-negative and gram-positive bacteria.* 2002. **PMID 11872725.** — Rubredoxin cross-complementation; AlkB homolog diversity (~35% identity).
- Smits THM, Witholt B, van Beilen JB. *Functional characterization of genes involved in alkane oxidation by* Pseudomonas aeruginosa. 2003. **PMID 14574114.** — RubA1/RubA2 and RubB substitute for GPo1 counterparts.
- Eggink G, Engel H, Vriend G, Terpstra P, Witholt B. *Rubredoxin reductase of Pseudomonas oleovorans...one NAD and two FAD fingerprints.* 1990. **PMID 2319593.** — AlkT = ~41 kDa FAD/NAD flavoprotein; alkST operon; three-component system.
- Perry A, Tambyrajah W, Grossmann JG, Lian LY, Scrutton NS. *Solution structure of the two-iron rubredoxin of Pseudomonas oleovorans...interactions with rubredoxin reductase.* 2004. **PMID 15023067.** — Two-domain, two-iron AlkG; flexible linker; domain mobility on docking.
- Shanklin J, Whittle E. *Evidence linking the Pseudomonas oleovorans alkane omega-hydroxylase...and the fatty acid desaturase family.* 2003. **PMID 12804773.** — AlkB is a membrane diiron enzyme; eight essential His ligands; desaturase superfamily.
- Sushko T, et al. *A new twist of rubredoxin function in M. tuberculosis.* 2021. **PMID 33618255.** — Rubredoxins as ubiquitous [1Fe–0S] carriers; transient, low-specificity partnerships; RubB→P450s; redox potential.
- Park IY, Eidsness MK, et al. *Crystallographic studies of V44 mutants of Clostridium pasteurianum rubredoxin: effects of side-chain size on reduction potential.* 2004. **PMID 15382226.** — Local tuning of rubredoxin reduction potential (NH···S H-bonds, side-chain size).
- Slater JW, Marguet SC, Monaco HA, Shafaat HS. *Nickel-substituted rubredoxin as a mechanistic model for [NiFe] hydrogenases.* 2018. **PMID 30016865.** — Plasticity of the rubredoxin FeS₄ scaffold.

---

*Prepared as an autonomous literature synthesis. Uncertainties are flagged explicitly; claims about* P. putida *KT2440 RubA specifically rest partly on homology to* P. oleovorans*/GPo1 and* P. aeruginosa *systems and would benefit from strain-specific biochemical confirmation.*


## Artifacts

- [OpenScientist final report](rubredoxin_electron_transfer-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rubredoxin_electron_transfer-deep-research-openscientist_artifacts/final_report.pdf)