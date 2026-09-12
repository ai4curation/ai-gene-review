---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T13:27:22.298658'
end_time: '2026-07-11T13:39:36.134336'
duration_seconds: 733.84
template_file: templates/module_research.md.j2
template_variables:
  module_title: tRNA ms2io6A37 hydroxylation
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00729 module for the terminal
    oxygen-dependent hydroxylation step that converts ms2i6A37-modified tRNA to ms2io6A37-modified
    tRNA. The module is centered on miaE (PP_2188, UniProtKB:Q88KV1). The upstream
    MiaA and MiaB reactions that generate the ms2i6A37 substrate are pathway context,
    not members of this single-gene UniPathway bucket.
  module_outline: "- tRNA ms2io6A37 hydroxylation\n  - 1. MiaE-dependent hydroxylation\
    \ of ms2i6A37-tRNA\n  - MiaE tRNA ms2io6A37 hydroxylation\n    - miaE: tRNA ms2i6A37\
    \ hydroxylase (molecular player: PSEPK miaE; activity or role: tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37)\
    \ hydroxylase activity)"
  module_connections: No explicit connections.
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: trna_ms2io6a37_hydroxylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: trna_ms2io6a37_hydroxylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

tRNA ms2io6A37 hydroxylation

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00729 module for the terminal oxygen-dependent hydroxylation step that converts ms2i6A37-modified tRNA to ms2io6A37-modified tRNA. The module is centered on miaE (PP_2188, UniProtKB:Q88KV1). The upstream MiaA and MiaB reactions that generate the ms2i6A37 substrate are pathway context, not members of this single-gene UniPathway bucket.

## Provisional Biological Outline

- tRNA ms2io6A37 hydroxylation
  - 1. MiaE-dependent hydroxylation of ms2i6A37-tRNA
  - MiaE tRNA ms2io6A37 hydroxylation
    - miaE: tRNA ms2i6A37 hydroxylase (molecular player: PSEPK miaE; activity or role: tRNA 2-(methylsulfanyl)-N(6)-isopentenyladenosine(37) hydroxylase activity)

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

# tRNA ms²io⁶A37 Hydroxylation: MiaE, the Terminal O₂-Dependent Diiron Tailoring Step

*A review-style synthesis centered on Pseudomonas putida KT2440 MiaE (PP_2188, UniProtKB:Q88KV1; UniPathway UPA00729)*

---

## 1. Executive Summary

The anticodon-adjacent position 37 of transfer RNAs that decode UNN codons is one of the most heavily elaborated sites in the tRNA modification landscape. In many bacteria this adenosine is built up in an ordered, three-enzyme relay: **MiaA** adds a dimethylallyl (isopentenyl) group to give N⁶-isopentenyladenosine (**i⁶A37**); **MiaB**, a radical-SAM methylthiotransferase, installs a 2-methylthio group to give **ms²i⁶A37**; and finally **MiaE** hydroxylates the terminal (C4) carbon of the isopentenyl side chain to give **ms²io⁶A37** (2-methylthio-*cis*-4-hydroxyisopentenyladenosine, historically "2-methylthio-*cis*-ribozeatin") (PMID 6362893, 17910062).

This review concerns only the last of these steps — the **MiaE-catalyzed hydroxylation** that defines UniPathway UPA00729. MiaE is a **non-heme, carboxylate-bridged diiron monooxygenase** with a ferritin-like four-α-helix-bundle catalytic domain. It uses **molecular O₂** and reducing equivalents delivered by a **ferredoxin/ferredoxin-reductase/NAD(P)H** electron-transport chain to perform a highly regio- and stereoselective (>97% *E*) allylic hydroxylation on a substrate that is embedded in a folded tRNA, not a free nucleoside (PMID 23906247, 25453905, 32785618). The crystal structure of the in-scope enzyme, *P. putida* MiaE (Pp-MiaE, PP_2188), revealed the diiron site, a dedicated tRNA-recognition linker, and a hydrophobic O₂-delivery tunnel (PMID 32785618).

Two features make MiaE biologically distinctive. First, because the reaction is **strictly O₂-dependent**, the ms²i⁶A37 ↔ ms²io⁶A37 ratio is a built-in **reporter of aerobiosis and redox state**; in *Salmonella*, hydroxylation occurs aerobically but not anaerobically, and *miaE* mutants cannot grow aerobically on TCA-cycle dicarboxylic acids (PMID 6362893, 9620964). Second, MiaE is a **late, accessory, phylogenetically patchy elaboration**: the i⁶A step (MiaA/TRIT1) is conserved across all domains of life, ms²-thiolation is a bacterial/organellar add-on, and MiaE hydroxylation is confined to a subset of bacteria (e.g., *Salmonella*, *Pseudomonas*) and is absent from *E. coli* and, as far as is known, from eukaryotes (PMID 17910062, 21873461, 24901367).

The strongest evidence base (diiron cofactor, O₂ dependence, stereochemistry, structure, tRNA-context requirement) is solid. The most important open questions concern the **oxygenated diiron intermediate** that abstracts hydrogen, the **native physiological electron donor(s)** in *Pseudomonas*, the **full tRNA substrate set** and recognition determinants, and the **biological meaning** of newly reported side-chain-modified bases and of the aerobiosis-sensing phenotype at the level of specific mRNAs.

---

## 2. Definition and Biological Boundaries

**What is included.** UPA00729/MiaE comprises exactly one biochemical transformation:

> ms²i⁶A37-tRNA + O₂ + 2 e⁻ + 2 H⁺ → ms²io⁶A37-tRNA + H₂O

carried out by a single gene product (PSEPK *miaE* / PP_2188 / Q88KV1) plus the generic redox partners that supply electrons. The substrate is a **fully formed ms²i⁶A37 residue displayed in the anticodon stem-loop (ASL/ACSL)** of specific tRNAs; the product is the hydroxylated ms²io⁶A37 residue. The tailored tRNAs are those that read codons beginning with U (UNN) — classically the isoacceptors for Phe, Tyr, Trp, Ser, Cys and Leu (PMID 6362893).

**What should be treated separately (common conflations).**

- **The upstream MiaA and MiaB reactions.** These generate the substrate and are essential *pathway context*, but they are mechanistically unrelated to MiaE (a P-loop dimethylallyltransferase and a radical-SAM/TRAM methylthiotransferase, respectively; PMID 17910062, 34526715) and are not part of the single-gene UPA00729 bucket.
- **The eukaryotic i⁶A branch and its disease biology.** Human **TRIT1** (a MiaA ortholog) makes i⁶A37 on a small subset of cytosolic and mitochondrial tRNAs; its loss causes combined oxidative phosphorylation deficiency 35 (COXPD35) (PMID 24901367, 28185376, 35418828). This is upstream i⁶A biology, not MiaE hydroxylation.
- **Cytokinin/plant hormone signaling.** The free base of ms²io⁶A resembles *cis*-zeatin-type cytokinins, and tRNA turnover is one source of *cis*-cytokinins in plants (PMID 6362893). Cytokinin perception and signaling are a distinct system that merely shares a chemical motif.
- **Other diiron monooxygenases.** MiaE belongs to the broad ferritin-like diiron-carboxylate superfamily that also contains soluble methane/toluene monooxygenases, ribonucleotide reductase R2, Δ9 desaturase and rubrerythrin. These share the four-helix diiron fold but act on entirely different substrates; MiaE is unusual in acting on a macromolecule-embedded target (PMID 32785618, 23906247).

**Competing definitions.** There is essentially no dispute about the reaction itself. Nomenclature varies (the product has been called ms²io⁶A, 2-methylthio-*cis*-hydroxyisopentenyladenosine, or 2-methylthio-*cis*-ribozeatin), and the enzyme has been abbreviated as "MiaE" / "ms²i⁶A37-tRNA monooxygenase" / "(ms²io⁶A37)hydroxylase." Recent mass-spectrometry work has reported additional side-chain-modified species (e.g., a "2-methylthio-methylenethio-N⁶-isopentenyladenosine" base; PMID 36640047) and transcriptome-wide mapping of 2-methylthio modifications (PMID 36820840); whether any such species are on-pathway MiaE products, alternative oxidation states, or products of other chemistry remains to be established and should be flagged as unsettled.

---

## 3. Mechanistic Overview

**Sequence of events (best current model).**

1. **Substrate presentation.** MiaE binds the tRNA/ASL and positions the terminal isopentenyl carbon of ms²i⁶A37 near the diiron center. tRNA context is not incidental: the enzyme is ~6,000-fold more efficient (V/K) on an anticodon-stem-loop substrate than on the free i⁶A nucleoside (PMID 25453905). A dedicated **linker region** identified in Pp-MiaE is important for this recognition (PMID 32785618).
2. **O₂ delivery and activation.** O₂ reaches the buried diiron(II) center via a **conserved hydrophobic tunnel** directly visualized by krypton-pressurized crystallography (PMID 32785618). Reaction with O₂ generates an oxygenated diiron species (by analogy to other diiron monooxygenases, a peroxo- and/or high-valent Fe–O intermediate; the exact species in MiaE has not been trapped and is an open question).
3. **C–H activation and hydroxylation.** The activated diiron center abstracts hydrogen from, and installs oxygen at, the **terminal C4 of the isopentenyl side chain**, yielding the allylic alcohol with **>97–98% *E*-stereoselectivity** and no detectable non-specific hydroxylation (PMID 23906247, 25453905).
4. **Electron resupply / turnover.** Catalysis requires two electrons per turnover, delivered in vivo by a **ferredoxin (Fd) / ferredoxin-reductase (FdR) / NAD(P)H** chain; in vitro this native chain can be bypassed by a **peroxide shunt** (H₂O₂), which recapitulates the same regio- and stereochemistry, confirming a diiron-oxygen mechanism (PMID 23906247, 25453905).

**Obligatory vs. conditional vs. accessory.**
- *Obligatory inputs*: a fully formed **ms²i⁶A37 substrate** (hence obligatory dependence on prior MiaA and MiaB action), **O₂**, and **reducing equivalents**.
- *Conditional*: the reaction proceeds **only under aerobic conditions** and is suppressed when iron/cysteine limitation blocks the upstream ms²-thiolation (leaving i⁶A) (PMID 6362893).
- *Accessory*: the MiaE step itself is **dispensable for viability** — cells lacking MiaE simply accumulate ms²i⁶A37 — so it is a physiological/regulatory tailoring layer rather than a core translational necessity (PMID 9620964).

---

## 4. Major Molecular Players and Active Assemblies

| Component | Identity / fold | Role in the step |
|---|---|---|
| **MiaE (PP_2188, Q88KV1)** | Non-heme **carboxylate-bridged diiron** enzyme; **ferritin-like four-α-helix bundle** catalytic domain + tRNA-recognition linker | Binds ms²i⁶A37-tRNA, activates O₂, performs allylic C4 hydroxylation (PMID 32785618, 23906247) |
| **tRNA substrate (ASL of UNN tRNAs)** | Folded anticodon stem-loop bearing ms²i⁶A37 | The macromolecular substrate; provides recognition determinants that drive catalytic efficiency (PMID 25453905) |
| **O₂** | Molecular oxygen delivered through a hydrophobic tunnel | Oxygen source and the switch that gates the reaction to aerobiosis (PMID 32785618, 6362893) |
| **Ferredoxin / Ferredoxin-reductase / NAD(P)H** | Generic [2Fe-2S] Fd + FAD reductase | Electron-transport chain supplying 2 e⁻ per turnover (PMID 25453905) |
| **(In vitro) H₂O₂** | Peroxide shunt | Bypasses the ETC to drive turnover, diagnostic of diiron-oxygen chemistry (PMID 23906247) |

**Upstream players (context, not part of UPA00729):** **MiaA** (dimethylallyl-PP:tRNA dimethylallyltransferase, P-loop/IPPT superfamily) makes i⁶A37; **MiaB** (radical-SAM methylthiotransferase with a TRAM domain and two [4Fe-4S] clusters) makes ms²i⁶A37 (PMID 17910062, 34526715, 31899624).

---

## 5. Evolutionary and Cell-Biological Variation

**A nested, increasingly restricted pathway.** The three tailoring layers show a clear conservation gradient:

- **i⁶A (MiaA) — ancient and universal.** Isopentenyltransferases are present in bacteria, archaea and eukaryotes; orthologs include yeast Mod5/Tit1, *C. elegans* GRO-1, and human TRIT1 (PMID 21873461). This is the best representative of the ancestral role of the whole system.
- **ms²i⁶A (MiaB / CDK5RAP1) — bacterial and organellar.** Methylthiolation is added in many bacteria and, in humans, on a subset of **mitochondrial** tRNAs by CDK5RAP1 (a MiaB relative). Notably, *E. coli* stops here (PMID 17910062).
- **ms²io⁶A (MiaE) — narrowly distributed tip.** Hydroxylation is documented in a subset of bacteria such as *Salmonella* and *Pseudomonas* and is **absent from *E. coli*** and, so far as known, from eukaryotes (PMID 9620964, 17910062, 6362893). MiaE therefore looks like a **late, lineage-specific elaboration** rather than a conserved core function.

**Physiological-state variation (the same cell, different conditions).** In a single *Salmonella* strain the modification state of A37 tracks the environment: **ms²io⁶A aerobically, ms²i⁶A anaerobically, and only i⁶A under iron/cysteine limitation** (PMID 6362893). Thus the "variation" most relevant to MiaE is not primarily across cell types but across **metabolic/redox states**, because O₂ availability directly gates the enzyme.

**Alternative routes.** No enzyme is known to reach ms²io⁶A37 by chemistry other than MiaE's diiron hydroxylation; the outcome (an allylic hydroxyl on the side chain) is not known to be produced by an independent route in bacteria. This contrasts with many tRNA modifications that have convergent, non-orthologous solutions.

---

## 6. Constraints, Dependencies, and Failure Modes

**Ordering constraints (why the sequence is fixed).**
- MiaE requires an intact ms²i⁶A37; it **cannot act before MiaA and MiaB**. Genetically and chemically, blocking either upstream step removes the substrate (i⁶A-only or A37-only tRNA) and abolishes hydroxylation (PMID 6362893).
- The **peroxide-shunt substrate studies** show MiaE will hydroxylate i⁶A and analogs lacking the 2-methylthio group in vitro, but it strongly prefers the tRNA-embedded ms²i⁶A context; the physiologically relevant order is nonetheless MiaA→MiaB→MiaE (PMID 23906247, 25453905).

**Compartment / condition constraints.**
- **Strict O₂ requirement**: hydroxylation is mutually exclusive with anaerobiosis (PMID 6362893). This makes the reaction a de facto aerobic switch and explains why *miaE* loss is phenotypically silent for viability but consequential for aerobic metabolism.
- **Substrate specificity**: only tRNAs that carry ms²i⁶A37 (UNN decoders) are candidates; MiaE does not act on bulk RNA or DNA.

**Failure modes and their consequences.**
- ***miaE* loss** → tRNAs frozen at ms²i⁶A37; cells are viable but **fail to grow aerobically on succinate/fumarate/malate**, with normal transport and TCA/respiratory enzymes — i.e., the defect is in translational tuning, not metabolism per se (PMID 9620964).
- **Upstream loss of i⁶A/ms²i⁶A (miaA/miaB)** has broader consequences on decoding: it reduces translational fidelity/efficiency of UNN codons, increases **+1 frameshifting** (synergizing with loss of wobble queuosine), promotes protein aggregation, and lowers virulence in several pathogens by impairing translation of key regulators (e.g., *Shigella* VirF; *Agrobacterium* vir induction) (PMID 42391044, 10692168, 1735704). These effects belong to the *upstream* branch but frame why the position-37 modifications matter.
- **Regulatory coupling upstream**: MiaA itself is post-transcriptionally controlled (e.g., by the CsrA/CsrB system), showing that flux into the whole pathway is tunable and stress-responsive (PMID 40649849).

---

## 7. Controversies and Open Questions

1. **The oxygenated diiron intermediate is not defined.** MiaE is firmly a diiron-oxygen monooxygenase (EPR/UV-vis, peroxide shunt, structure), but the reactive species that performs C–H activation (peroxo vs. high-valent Fe–O) has not been spectroscopically trapped for MiaE specifically. The mechanism is inferred by analogy to better-studied diiron enzymes (PMID 23906247, 32785618).
2. **The native electron donor in *Pseudomonas*.** In vitro turnover uses a generic Fd/FdR/NAD(P)H chain, but the physiological reductase partner(s) and their regulation in *P. putida* are not established (PMID 25453905).
3. **The complete tRNA substrate set and recognition code.** Docking + mutagenesis implicate a linker region and ASL contacts, but a high-resolution MiaE–tRNA complex and a definitive list of substrate isoacceptors across species are lacking (PMID 32785618).
4. **Newly reported side-chain species.** Mass-spectrometry has reported additional ms²-side-chain-modified bases (e.g., a "methylenethio" species; PMID 36640047) and transcriptome-wide ms² mapping (PMID 36820840). Whether these are on-pathway MiaE products, oxidation artifacts, or the work of other enzymes is unresolved.
5. **Mechanism of aerobiosis "sensing."** The elegant hypothesis that cells read the hydroxylation status of A37 to gate growth on TCA intermediates is well supported genetically (PMID 6362893, 9620964), but the downstream molecular chain — which specific mRNAs/attenuators are re-tuned by ms²io⁶A37 vs. ms²i⁶A37 — has not been mapped at modern resolution.
6. **Cross-organism extrapolation caution.** Much biochemistry is from *Salmonella* MiaE while the definitive structure is from *P. putida*; the two are congruent but not identical, and physiology (TCA-growth phenotype) has been characterized mainly in *Salmonella*. Claims should not be generalized to "all bacteria," and eukaryotic i⁶A/TRIT1 disease data must not be imported as MiaE biology.

---

## 8. Key References

- Buck M, Ames BN. *A modified nucleotide in tRNA as a possible regulator of aerobiosis: synthesis of cis-2-methyl-thioribosylzeatin in the tRNA of Salmonella.* Cell 1984. **PMID 6362893.** (Discovery; O₂ dependence; aerobic/anaerobic switching; cytokinin link.)
- Persson BC, et al. *The ms2io6A37 modification of tRNA in Salmonella typhimurium regulates growth on citric acid cycle intermediates.* Mol Microbiol 1998. **PMID 9620964.** (miaE gene product = tRNA(ms²io⁶A37)hydroxylase; aerobic dicarboxylate-growth phenotype.)
- Kaminska KH, et al. *Structural bioinformatics analysis of enzymes involved in the biosynthesis pathway of ms²io⁶A37 in tRNA.* Proteins 2008. **PMID 17910062.** (Ordered MiaA→MiaB→MiaE pathway; MiaE predicted diiron four-helix fold.)
- Corder AL, et al. *Peroxide-shunt substrate-specificity for the Salmonella O₂-dependent tRNA-modifying monooxygenase (MiaE).* Biochemistry 2013. **PMID 23906247.** (Diiron cofactor; peroxide shunt; >97% E-stereoselectivity.)
- Subedi BP, et al. *Steady-state kinetics and spectroscopic characterization of enzyme–tRNA interactions for the non-heme diiron tRNA-monooxygenase MiaE.* Biochemistry 2015. **PMID 25453905.** (Fd/FdR/NADPH ETC; ~6,000-fold ASL-context rate enhancement.)
- Carpentier P, et al. *Structural, biochemical and functional analyses of tRNA-monooxygenase MiaE from Pseudomonas putida.* Nucleic Acids Res 2020. **PMID 32785618.** (In-scope Pp-MiaE/PP_2188 crystal structure; diiron four-helix bundle; O₂ tunnel; tRNA-recognition linker.)
- Esakova OA, et al. *Structural basis for tRNA methylthiolation by the radical SAM enzyme MiaB.* Nature 2021. **PMID 34526715.** (Upstream MiaB mechanism/structure.)
- Zhang B, et al. *First step in catalysis of the radical SAM methylthiotransferase MiaB.* 2020. **PMID 31899624.** (Upstream MiaB chemistry.)
- Lamichhane TN, et al. *Plasticity and diversity of tRNA anticodon determinants of substrate recognition by eukaryotic A37 isopentenyltransferases.* RNA 2011. **PMID 21873461.** (Deep conservation of the i⁶A/MiaA branch; Mod5, Tit1, TRIT1, GRO-1.)
- Yarham JW, et al. *Defective i6A37 modification of mitochondrial and cytosolic tRNAs from pathogenic TRIT1 mutations.* PLoS Genet 2014. **PMID 24901367.** (Eukaryotic boundary; TRIT1/COXPD disease.)
- Durand JM, et al. *tRNA modification, temperature and DNA superhelicity target virF in Shigella.* Mol Microbiol 2000. **PMID 10692168.** (Position-37 modification and virulence, upstream branch.)
- Sun Y, et al. *Defective queuosine and i6A/ms2i6A modification of tRNATyr cause frameshifting and protein aggregation.* 2026. **PMID 42391044.** (Decoding fidelity/proteostasis consequences of A37 undermodification.)
- Libiad M, et al. *Identification of 2-methylthio-methylenethio-N⁶-… (a new modified base).* 2023. **PMID 36640047.** (Newly reported side-chain species; boundary/uncertainty.)
- Fang L, et al. *Transcriptome-wide mapping of 2-methylthio modifications.* 2023. **PMID 36820840.** (ms² mapping; boundary/uncertainty.)
- Aubee JI, et al. *Post-transcriptional regulation of MiaA by CsrA and sRNA CsrB.* 2025. **PMID 40649849.** (Upstream regulatory tuning of pathway flux.)

---

*Scope note:* This synthesis is deliberately restricted to the MiaE hydroxylation step (UPA00729). Upstream MiaA/MiaB reactions, eukaryotic i⁶A/TRIT1 disease biology, and cytokinin signaling are discussed only to delineate boundaries and are not claimed as members of this module. Where evidence derives from *Salmonella* vs. *Pseudomonas*, or from in vitro surrogate substrates, this is stated explicitly to avoid over-generalization.


## Artifacts

- [OpenScientist final report](trna_ms2io6a37_hydroxylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](trna_ms2io6a37_hydroxylation-deep-research-openscientist_artifacts/final_report.pdf)