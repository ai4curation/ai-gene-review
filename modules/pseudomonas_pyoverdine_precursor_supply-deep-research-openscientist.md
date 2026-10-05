---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:35:16.531385'
end_time: '2026-08-31T08:58:56.995500'
duration_seconds: 1420.46
template_file: templates/module_research.md.j2
template_variables:
  module_title: Pseudomonas pyoverdine non-proteinogenic precursor supply
  module_summary: A reusable Pseudomonas module for reactions that supply unusual
    amino-acid building blocks to the cytoplasmic pyoverdine NRPS assembly line. PvdA
    hydroxylates L-ornithine to produce N5-hydroxy-L-ornithine, and PvdH forms L-2,4-diaminobutyrate
    from L-aspartate 4-semialdehyde by PLP-dependent transamination. NRPS assembly,
    ferribactin export, periplasmic maturation, secretion, ferripyoverdine uptake,
    and iron release are outside this module.
  module_outline: "- Pseudomonas pyoverdine non-proteinogenic precursor supply\n \
    \ - 1. N5-hydroxy-L-ornithine precursor supply\n  - PvdA-dependent ornithine N5-hydroxylation\n\
    \    - Pyoverdine ornithine N5-monooxygenase PvdA (molecular player: Pseudomonas\
    \ pyoverdine PvdA ornithine N5-monooxygenase family; activity or role: ornithine\
    \ N5-monooxygenase activity)\n  - 2. L-2,4-diaminobutyrate precursor supply\n\
    \  - PvdH-dependent L-2,4-diaminobutyrate formation\n    - Pyoverdine diaminobutyrate\
    \ transaminase PvdH (molecular player: Pseudomonas pyoverdine PvdH diaminobutyrate\
    \ transaminase family; activity or role: L-2,4-diaminobutyrate:2-oxoglutarate\
    \ transaminase activity)"
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
citation_count: 26
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pseudomonas_pyoverdine_precursor_supply-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pseudomonas_pyoverdine_precursor_supply-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Pseudomonas pyoverdine non-proteinogenic precursor supply

## Working Scope

A reusable Pseudomonas module for reactions that supply unusual amino-acid building blocks to the cytoplasmic pyoverdine NRPS assembly line. PvdA hydroxylates L-ornithine to produce N5-hydroxy-L-ornithine, and PvdH forms L-2,4-diaminobutyrate from L-aspartate 4-semialdehyde by PLP-dependent transamination. NRPS assembly, ferribactin export, periplasmic maturation, secretion, ferripyoverdine uptake, and iron release are outside this module.

## Provisional Biological Outline

- Pseudomonas pyoverdine non-proteinogenic precursor supply
  - 1. N5-hydroxy-L-ornithine precursor supply
  - PvdA-dependent ornithine N5-hydroxylation
    - Pyoverdine ornithine N5-monooxygenase PvdA (molecular player: Pseudomonas pyoverdine PvdA ornithine N5-monooxygenase family; activity or role: ornithine N5-monooxygenase activity)
  - 2. L-2,4-diaminobutyrate precursor supply
  - PvdH-dependent L-2,4-diaminobutyrate formation
    - Pyoverdine diaminobutyrate transaminase PvdH (molecular player: Pseudomonas pyoverdine PvdH diaminobutyrate transaminase family; activity or role: L-2,4-diaminobutyrate:2-oxoglutarate transaminase activity)

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

# Pseudomonas Pyoverdine Non-Proteinogenic Precursor Supply: PvdA and PvdH as a Two-Enzyme Building-Block Module

*A commissioned review-style synthesis for a molecular biology audience. Search date: 2026-08-31. Scope restricted to the cytoplasmic reactions that supply the two unusual amino-acid building blocks — N5-hydroxy-L-ornithine (PvdA) and L-2,4-diaminobutyrate (PvdH) — to the pyoverdine nonribosomal peptide synthetase (NRPS) assembly line.*

---

## 1. Executive Summary

Pyoverdines are the primary, high-affinity peptidic siderophores of the fluorescent pseudomonads. Their iron-chelating power depends on two chemically unusual, non-proteinogenic amino-acid building blocks that ordinary primary metabolism does not supply in usable form: **N5-hydroxy-L-ornithine** (subsequently formylated/acylated to form the hydroxamate iron ligands) and **L-2,4-diaminobutyrate (DABA)** (which contributes to the fluorescent dihydroquinoline chromophore and the peptide backbone). This review treats the **precursor-supply module** — the two cytoplasmic reactions that make these monomers — as a discrete, reusable biological subsystem, distinct from the downstream NRPS assembly line, ferribactin export, periplasmic maturation, secretion, ferripyoverdine uptake, and iron release.

The module comprises exactly two catalytic activities carried by two evolutionarily unrelated enzymes. **PvdA** is a class B FAD/NADPH-dependent N-hydroxylating flavoprotein monooxygenase that installs a hydroxyl group on the side-chain (N5) amine of L-ornithine, generating N5-hydroxy-L-ornithine. Its chemistry proceeds through a C4a-hydroperoxyflavin oxygenating intermediate that is stabilized by bound NADP+ and gated so that oxygen and substrate reactivity are coupled — a hallmark of the siderophore-associated monooxygenase family that also includes fungal SidA, bacterial IucD, DfoA, and DesB. **PvdH** is a pyridoxal-5'-phosphate (PLP)-dependent aminotransferase that forms L-2,4-diaminobutyrate from L-aspartate-4-semialdehyde (aspartate β-semialdehyde, ASA) via a classic ping-pong (bi-bi) mechanism, using α-ketoglutarate as the preferred amino acceptor.

Three organizing principles emerge. First, the module is **transcriptionally gated by iron starvation**: pvdA (and, by extension, the co-clustered precursor genes) is controlled by the Fur repressor and the extracytoplasmic-function (ECF) sigma factor PvdS, so precursor supply is switched on in lockstep with the assembly line only when iron is scarce. Second, the module is **physically integrated** into a membrane-associated cytoplasmic multienzyme complex — the "siderosome" — where precursor-generating enzymes co-assemble with the NRPSs, plausibly channeling reactive intermediates to the assembly line. Third, the module is **conserved across pyoverdine-producing pseudomonads** while the NRPS peptide backbone it feeds is highly diversified, making PvdA/PvdH a stable, reusable supply unit beneath a variable product.

---

## 2. Definition and Biological Boundaries

### What is included

The precursor-supply module is defined by two reactions and the two enzymes that catalyze them:

| Branch | Enzyme | Reaction | Product's role in pyoverdine |
|---|---|---|---|
| N5-hydroxy-L-ornithine supply | **PvdA** (L-ornithine N5-monooxygenase / "L-ornithine N5-oxygenase") | L-ornithine + NADPH + O2 → N5-hydroxy-L-ornithine | Hydroxamate iron-ligand precursor (formylated by PvdF) |
| DABA supply | **PvdH** (diaminobutyrate:2-oxoglutarate transaminase) | L-aspartate-4-semialdehyde + L-glutamate ⇌ L-2,4-diaminobutyrate + α-ketoglutarate | Chromophore/backbone residue |

Both enzymes are cytoplasmic and act *before* monomer loading onto the NRPS. They generate free non-proteinogenic amino acids (or amino-acid derivatives) that are subsequently activated and condensed by the assembly line.

### What is explicitly outside the module (and often confused with it)

- **N5-acylation / formylation (PvdF, PvdY).** PvdF is an N5-hydroxyornithine *formyltransferase* that acts on PvdA's product to complete the hydroxamate. Although PvdF is functionally adjacent — and evidence indicates it physically interacts with a substrate-providing enzyme — it is a *tailoring* enzyme, not a precursor-supply enzyme, and belongs outside the strict two-reaction module.
- **The NRPS assembly line (PvdL, PvdI, PvdJ, PvdD, etc.).** These condense the monomers into ferribactin; they consume, but do not supply, the precursors.
- **Upstream primary metabolism.** Ornithine biosynthesis (from glutamate/arginine metabolism) and the Asd (aspartate-β-semialdehyde dehydrogenase) reaction that generates ASA are *feeders* to the module. Asd is genetically required for DABA/pyoverdine synthesis, but it is a central-metabolism enzyme shared with lysine/threonine/methionine and diaminopimelate biosynthesis and is best treated as an input, not a module member.
- **Ferribactin export (PvdE), periplasmic maturation (PvdM, PvdN, PvdO, PvdP, PvdQ), secretion, FpvA-mediated ferripyoverdine uptake, and cytoplasmic iron release.** All are downstream of monomer supply.
- **Ectoine biosynthesis.** The ectoine pathway's EctB is a DABA transaminase catalyzing the *same* ASA→DABA reaction as PvdH. This is a genuine biochemical parallel and a source of confusion, but ectoine synthesis is an osmolyte pathway, not part of siderophore precursor supply. The shared chemistry is informative for family assignment (see §4, §5) but the pathways are physiologically separate.

### Competing definitions

The literature does not use the term "precursor-supply module" uniformly; the concept is implicit. Some reviews fold PvdA and PvdH into a general "pyoverdine biosynthesis" gene set of 30+ genes governed by Fur/PvdS/FpvI, without separating precursor supply from assembly and maturation ([PMID: 35171432](https://pubmed.ncbi.nlm.nih.gov/35171432/)). The nomenclature "L-ornithine N5-oxygenase" (older, genetic literature) and "L-ornithine N5-monooxygenase" (biochemical/structural literature) refer to the same PvdA activity. Drawing the module boundary at "reactions producing free non-proteinogenic monomers, upstream of NRPS loading and before N-acylation" is the most defensible operational definition and the one used here.

---

## 3. Mechanistic Overview

### 3.1 The two branches

```
 Primary metabolism            PRECURSOR-SUPPLY MODULE            Downstream (outside module)
 ─────────────────             ──────────────────────            ───────────────────────────

 L-ornithine  ───────────────►  PvdA (FAD, NADPH, O2)  ─────►  N5-OH-L-Orn ──► PvdF formylation
                                 class B N-hydroxylase                          ──► NRPS loading
                                 (C4a-OOH flavin, NADP+-gated)

 L-aspartate                                                     L-2,4-diaminobutyrate (DABA)
   │ (Asd)                                                                │
   ▼                                                                      ▼
 L-Asp-4-semialdehyde ───────►  PvdH (PLP transaminase)  ─────►  DABA ──► NRPS loading / chromophore
   (ASA)                         ping-pong; α-KG acceptor
```

**PvdA branch.** PvdA reduces its FAD cofactor with NADPH, then reacts the reduced flavin with molecular O2 to form a C4a-(hydro)peroxyflavin. This oxygenating species transfers an oxygen atom to the N5 (side-chain) amine of L-ornithine, producing N5-hydroxy-L-ornithine, water, and NADP+. Catalysis is tightly regulated at the oxygen-activation step: the reactive C4a-hydroperoxyflavin is stabilized by bound NADP+, which prevents wasteful decay to H2O2 and couples oxygen consumption to productive hydroxylation ([PMID: 20650894](https://pubmed.ncbi.nlm.nih.gov/20650894/)). The enzyme is highly specific for ornithine; lysine binds but acts as a non-substrate effector that *uncouples* the reaction, and high ornithine concentrations cause substrate inhibition ([PMID: 17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/)).

**PvdH branch.** PvdH is a fold-type-I PLP aminotransferase operating by a ping-pong bi-bi mechanism. In the first half-reaction, the amino donor (L-glutamate) transfers its amino group to enzyme-bound PLP, forming pyridoxamine-5'-phosphate (PMP) and releasing α-ketoglutarate. In the second half-reaction, PMP transfers the amino group to the aldehyde carbon of L-aspartate-4-semialdehyde, producing L-2,4-diaminobutyrate and regenerating PLP. Kinetically, α-ketoglutarate/glutamate is by far the preferred keto-acid/amino-acid pair (≈41-fold higher specificity than pyruvate/alanine; negligible activity with other keto acids) ([PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/)).

### 3.2 Which steps are obligatory, conditional, or accessory

- **Obligatory:** Both PvdA and PvdH activities are required for pyoverdine production. Genetic knockouts of pvdH (and of the upstream feeder asd) abolish pyoverdine synthesis unless DABA is supplied exogenously, demonstrating that PvdH-derived DABA is essential and non-redundant in P. aeruginosa PAO1 ([PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/)). PvdA's product is the sole route to the hydroxamate ligands.
- **Conditional (regulatory gating):** Expression of the module is conditional on iron limitation via Fur/PvdS. Under iron-replete conditions the module is off; the *catalytic requirement* is unconditional whenever pyoverdine is made.
- **Accessory / adjacent:** N5-formylation (PvdF) is required to complete the functional hydroxamate but is a tailoring step, not precursor supply. Physical incorporation into the siderosome enhances efficiency but is an organizational, not strictly catalytic, feature.

### 3.3 Ordering constraints

Within each branch the order is fixed by chemistry: PvdA must hydroxylate ornithine before PvdF can formylate it; Asd must generate ASA before PvdH can transaminate it. Across branches, the two reactions are independent and can proceed in parallel. The two products only "meet" downstream, during NRPS assembly of the ferribactin precursor. The precursor reactions must precede NRPS loading — a free-monomer supply logic rather than an on-line tailoring logic.

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 PvdA — L-ornithine N5-monooxygenase (class B flavoprotein monooxygenase)

PvdA is a well-characterized member of the **N-hydroxylating flavin-dependent monooxygenase (NMO/FMO)** family within class B flavoprotein monooxygenases. Formation of the iron-chelating hydroxamate functional group in pyoverdine requires PvdA, "a flavin-dependent monooxygenase that catalyzes the N(5) hydroxylation of l-ornithine" ([PMID: 17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/)). Biochemical reconstitution of purified PvdA established an absolute requirement for FAD and NADPH, an optimal pH near 8.0, and Michaelis-Menten kinetics on L-ornithine with apparent Km ≈ 0.58 mM and Vmax ≈ 1.34 µmol·min⁻¹·mg⁻¹; the L-ornithine-dependent NADPH oxidation "obeyed Michaelis-Menten kinetics with apparent K(m) and V(max) values of 0.58 mM and 1.34 micromol min(-1) mg(-1)" ([PMID: 17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/)). Ornithine stimulates NADPH oxidation roughly 5-fold with tight coupling to N5-hydroxylamine formation.

The enzyme was formally assigned to the class B flavoprotein monooxygenases: "The ornithine hydroxylase from Pseudomonas aeruginosa (PvdA) catalyzes the FAD-dependent hydroxylation of the side chain amine of ornithine, which is subsequently formylated to generate the iron-chelating hydroxamates of the siderophore pyoverdin. PvdA belongs to the class B flavoprotein monooxygenases" ([PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)). Two X-ray crystal structures — oxidized (1.9 Å) and reduced (3.03 Å) — place PvdA in the class B fold with two Rossmann dinucleotide-binding domains (for FAD and NADPH) plus a substrate-binding domain. Structurally and mechanistically PvdA is the bacterial paradigm alongside fungal SidA (*Aspergillus fumigatus*), *E. coli* IucD (lysine hydroxylase), *Erwinia* DfoA, and *Streptomyces* DesB (cadaverine hydroxylase), all of which share the same protomer architecture and the NADP+-stabilized C4a-hydroperoxyflavin strategy ([PMID: 21871647](https://pubmed.ncbi.nlm.nih.gov/21871647/); [PMID: 22928747](https://pubmed.ncbi.nlm.nih.gov/22928747/); [PMID: 33784308](https://pubmed.ncbi.nlm.nih.gov/33784308/)).

### 4.2 PvdH — diaminobutyrate:2-oxoglutarate transaminase (fold-type-I PLP enzyme)

PvdH catalyzes the interconversion of ASA and DABA. A coupled steady-state assay established its ping-pong kinetic mechanism and its strong preference for α-ketoglutarate as amino acceptor: "PvdH was found to catalyze an aminotransferase reaction, interconverting aspartate beta-semialdehyde and l-2,4-diaminobutyrate. Steady-state kinetic analysis with a novel coupled assay established that the enzyme adopts a ping-pong kinetic mechanism and has the highest specificity for alpha-ketoglutarate" ([PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/)). Genetic evidence places it downstream of ASA supply and shows it is essential for pyoverdine synthesis: "Both pvdH and asd (encoding aspartate beta-semialdehyde dehydrogenase) knockout mutants of Pseudomonas aeruginosa PAO1 were unable to synthesize pyoverdine under iron-limiting conditions in the absence of l-2,4-diaminobutyrate in the culture media" ([PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/)). PvdH homologues are encoded within pyoverdine gene loci across *Pseudomonas* spp., indicating the DABA-supply function is a conserved, co-clustered part of the pyoverdine biosynthetic apparatus.

The same ASA→DABA transamination is performed by the ectoine-pathway enzyme **EctB**, a tetrameric fold-type-I PLP DABA transaminase: "The rate-limiting step of ectoine biosynthesis is catalyzed by the l-2,4-diaminobutyric acid (DABA) transaminase enzyme EctB, which converts aspartate-β-semialdehyde (ASA) to DABA" ([PMID: 41652856](https://pubmed.ncbi.nlm.nih.gov/41652856/)). This confirms that PvdH belongs to a broadly distributed DABA-transaminase family repurposed for siderophore precursor supply.

### 4.3 The siderosome — a membrane-associated cytoplasmic multienzyme complex

Cell fractionation, protein–protein interaction, and in vivo labeling in P. aeruginosa show that the pyoverdine NRPSs assemble together with precursor-generating enzymes into a membrane-bound multienzyme complex: "pyoverdine NRPSs assemble with precursor-generating enzymes into a membrane-bound multi-enzymatic complex, for which we propose the name 'siderosome'" ([PMID: 24042050](https://pubmed.ncbi.nlm.nih.gov/24042050/)). Active-site mapping of the tailoring enzyme PvdF provided evidence for direct interaction between PvdF and a substrate-providing enzyme — consistent with **substrate channeling** in the precursor branch, which would protect reactive intermediates and improve pathway flux ([PMID: 33672312](https://pubmed.ncbi.nlm.nih.gov/33672312/)). The precursor-supply enzymes are therefore best understood not as free-floating cytoplasmic catalysts but as components co-localized with the assembly line.

### 4.4 Regulatory apparatus

The module's genes are embedded in the iron-starvation regulon. The pvdA gene "encoding the enzyme L-ornithine N5-oxygenase, catalyzes a key step of the pyoverdin biosynthetic pathway in Pseudomonas aeruginosa" ([PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/)). **Fur** (ferric uptake regulator) represses the system under iron-replete conditions; two fur mutants "were much less responsive than wild-type PAO1 to the iron-dependent regulation of pvdA expression" ([PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/)). Under iron limitation, derepression allows the ECF sigma factor **PvdS** to direct RNA polymerase to pyoverdine promoters, including the pvdA promoter, which carries an "iron-starvation box." Purified PvdS forms 1:1 complexes with core RNA polymerase, "promoting in vitro binding of the PvdS-RNAP holoenzyme to the promoter region of the pvdA gene" ([PMID: 10692351](https://pubmed.ncbi.nlm.nih.gov/10692351/)).

The broader pyoverdine regulon (>30 genes) is governed by Fur plus two ECF sigma factors: "Its synthesis and uptake are triggered by iron scarcity via the Fur regulator and involves two extra cytoplasmic sigma factors (ECF), PvdS for the biosynthesis of PVD and FpvI for the uptake" ([PMID: 35171432](https://pubmed.ncbi.nlm.nih.gov/35171432/)). Additional regulators fine-tune this output — AlgQ acts as an anti-sigma factor for RpoD to favor PvdS-directed transcription ([PMID: 16030202](https://pubmed.ncbi.nlm.nih.gov/16030202/)), and small RNAs modulate the pyochelin/pyoverdine balance under low iron ([PMID: 40150866](https://pubmed.ncbi.nlm.nih.gov/40150866/)).

```
 Iron-replete:   Fur–Fe(II) ──┤ pvdS, pvdA, pvd genes   (module OFF)
 Iron-limited:   Fur released ──► PvdS + RNAP ──► pvdA promoter (iron-starvation box) ──► transcription (module ON)
                                             └─► co-transcription with NRPS/assembly genes
```

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep origins of each branch

The two branches have independent, ancient origins.

- **PvdA (N-hydroxylating FMO):** The class B flavoprotein monooxygenase fold with tandem Rossmann domains is ancient and broadly distributed across bacteria and fungi. N-hydroxylating members are a coherent siderophore-biosynthetic subfamily (PvdA, SidA, IucD, DfoA, DesB) unified by the C4a-hydroperoxyflavin chemistry and NADP+ gating. Because this subfamily is deployed across diverse siderophore pathways (pyoverdine, ferrichrome/fusarinine, aerobactin, desferrioxamine), the ancestral role is plausibly generic amine N-hydroxylation for hydroxamate siderophore production. For inferring the ancestral function, the well-studied ornithine/lysine hydroxylases (PvdA, SidA, IucD) are the best representatives; the broader-specificity DesB (cadaverine, putrescine, spermidine, lysine) illustrates how substrate scope can expand within the family ([PMID: 33784308](https://pubmed.ncbi.nlm.nih.gov/33784308/); [PMID: 21871647](https://pubmed.ncbi.nlm.nih.gov/21871647/)).
- **PvdH (DABA transaminase):** Fold-type-I PLP aminotransferases are among the most ancient enzyme superfamilies. The specific ASA→DABA activity is shared with ectoine biosynthesis (EctB) and other DABA-utilizing pathways, indicating the DABA-transaminase function predates and is broader than pyoverdine ([PMID: 41652856](https://pubmed.ncbi.nlm.nih.gov/41652856/)). PvdH represents a lineage of this family co-opted into the siderophore locus.

Thus the module is a *convergent assembly* of two independently ancient enzyme families brought together to supply one siderophore, rather than a single coherent evolutionary unit.

### 5.2 Conservation versus diversification

A striking feature of pyoverdine biology is that the **peptide backbone is highly variable** across *Pseudomonas* strains — driven by substitution and modification of NRPS clusters, generating dozens of distinct pyoverdine structures — while the **precursor-supply enzymes are comparatively conserved** and co-clustered within pyoverdine loci ([PMID: 40572297](https://pubmed.ncbi.nlm.nih.gov/40572297/); [PMID: 39224222](https://pubmed.ncbi.nlm.nih.gov/39224222/)). This makes PvdA/PvdH a stable "reusable module": the same non-proteinogenic monomers are supplied even as the NRPS diversifies the product. Genome-mining and comparative-genomic surveys (e.g., feature-sequence-based mining across ~1,928 genomes; *P. chlororaphis* comparative genomics) consistently identify pyoverdine biosynthetic clusters including the precursor-supply functions across fluorescent pseudomonads ([PMID: 39352117](https://pubmed.ncbi.nlm.nih.gov/39352117/); [PMID: 41792602](https://pubmed.ncbi.nlm.nih.gov/41792602/)).

### 5.3 Physiological-state and ecological variation

The module is a **physiological-state-dependent** system rather than a cell-type- or tissue-dependent one (these are bacteria). Its dominant modulator is iron availability, integrated with quorum sensing and competition sensing. RNA-seq studies show pyoverdine genes are upregulated in response to competitor cues (e.g., *Burkholderia cenocepacia* supernatant) in an iron-context-dependent manner ([PMID: 39143311](https://pubmed.ncbi.nlm.nih.gov/39143311/)), and small RNAs (e.g., Lrs1) fine-tune siderophore balance under low iron ([PMID: 40150866](https://pubmed.ncbi.nlm.nih.gov/40150866/)). Pyoverdine's ecological importance is strain- and context-specific: in some biocontrol settings pyoverdine plays only a minor role in pathogen inhibition, with iron competition or alternative siderophores dominating ([PMID: 42210498](https://pubmed.ncbi.nlm.nih.gov/42210498/)).

### 5.4 Alternative routes to the same outcome

- **N-hydroxylamine building blocks** in other siderophores are made by paralogous FMOs with different substrate preferences (lysine by IucD/SidA-type enzymes; diamines by DesB). The *chemistry* (flavin N-hydroxylation) is conserved; the *substrate* varies by pathway.
- **DABA** is produced by PvdH in pyoverdine and by EctB in ectoine — the same reaction reached by homologous but pathway-distinct enzymes.

These parallels show the module's outputs are not unique to pyoverdine; what is pyoverdine-specific is the *co-clustering and co-regulation* of PvdA and PvdH with the assembly line.

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering and compartment constraints

- Both reactions are **cytoplasmic** and occur **before** NRPS loading; the products are free monomers channeled to the assembly line, plausibly within the siderosome.
- Within the ornithine branch, **hydroxylation must precede formylation** (PvdA before PvdF); the reverse order is chemically impossible.
- Within the DABA branch, **Asd must generate ASA before PvdH acts**; PvdH cannot substitute for the missing ASA input, as shown by the asd knockout phenotype rescued only by exogenous DABA ([PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/)).

### 6.2 Substrate-specificity and coupling constraints

- PvdA is **substrate-specific for ornithine**; a hydroxylation assay "indicated substrate inhibition at high ornithine concentration. PvdA is highly specific for both substrate and coenzyme, and lysine was shown to be a nonsubstrate effector and mixed inhibitor of the enzyme with respect to ornithine" ([PMID: 17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/)). Lysine uncouples NADPH oxidation to yield H2O2 rather than product. Productive catalysis therefore depends on both correct substrate occupancy and NADP+-mediated stabilization of the C4a-hydroperoxyflavin — a built-in failure mode is uncoupling (futile NADPH/O2 consumption) when the wrong amine binds.
- PvdH is **acceptor-specific for α-ketoglutarate**; the reaction is a reversible transamination, so intracellular pools of glutamate/α-ketoglutarate and ASA set the direction and flux.

### 6.3 Regulatory dependency

- Because the module is **Fur/PvdS-gated**, loss of PvdS (or constitutive Fur repression under high iron) shuts down precursor supply even when substrates are abundant. The module cannot operate "on demand" independently of the iron-starvation signal in vivo ([PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/); [PMID: 10692351](https://pubmed.ncbi.nlm.nih.gov/10692351/)).

### 6.4 Evidence ruling out alternative paths

- The **asd/pvdH double genetic requirement** rules out an alternative DABA source in P. aeruginosa PAO1 under the tested conditions: no pyoverdine is made without PvdH unless DABA is fed. This excludes redundant DABA-supply routes as sufficient for pyoverdine in this organism.
- The **flavin/NADPH dependence and C4a-hydroperoxyflavin mechanism** exclude non-flavin (e.g., simple oxidase or P450-independent) routes to N5-hydroxyornithine in this system.

### 6.5 Failure modes (summary table)

| Perturbation | Consequence | Evidence type |
|---|---|---|
| pvdA loss | No hydroxamate ligand; pyoverdine defective | Genetic/biochemical |
| pvdH loss | No DABA; no pyoverdine (rescued by exogenous DABA) | Genetic |
| asd loss (feeder) | No ASA → no DABA → no pyoverdine (rescued by DABA) | Genetic |
| Wrong amine in PvdA (e.g., lysine) | Uncoupling → H2O2, no product | Biochemical |
| Loss of PvdS / high iron | Module transcriptionally off | Genetic/regulatory |

---

## 7. Controversies and Open Questions

**Strongly supported claims.** The identity, cofactor requirements, kinetics, structures, and reaction mechanisms of PvdA (class B FMO, N5-hydroxylation, C4a-hydroperoxyflavin, NADP+ gating) and PvdH (PLP ping-pong transaminase, ASA↔DABA, α-KG preference) are well established by purified-enzyme biochemistry and, for PvdA, crystallography. The essentiality of both for pyoverdine, and the Fur/PvdS iron-starvation control of pvdA, are supported by genetics and in vitro transcription.

**Areas of uncertainty and mixed evidence.**

1. **Siderosome channeling.** Co-assembly of precursor enzymes with NRPSs (the "siderosome") is supported by fractionation and interaction data, and PvdF–substrate-provider interaction data hint at channeling, but *direct kinetic proof of channeled transfer* of N5-hydroxyornithine or DABA to the assembly line is still lacking. How tightly the precursor enzymes are coupled to the NRPS remains an open mechanistic question. (One supporting reference for the PvdF–substrate-provider interaction was available largely at the title level during curation, so the channeling interpretation rests more on the fractionation/interaction study than on that single reference.)

2. **Cross-organism extrapolation.** Much biochemistry comes from P. aeruginosa PAO1 and closely related strains, whereas the family-level generalizations draw on fungal SidA, *E. coli* IucD, *Streptomyces* DesB, and *Marinobacter* EctB. These support family assignment but should not be over-read as identical regulation or in vivo behavior across lineages. Substrate scope, in particular, differs (e.g., DesB's broad diamine activity vs. PvdA's strict ornithine specificity).

3. **Order and gating of oxygen chemistry.** The precise role of NADP+ in gating O2 reactivity, and how uncoupling is avoided in vivo at physiological substrate/NADPH ratios, is inferred largely from steady-state and transient kinetics on representative family members; direct in vivo flux measurements are scarce.

4. **DABA-branch redundancy across strains.** The strict PvdH/asd requirement is demonstrated in PAO1; whether other pseudomonads have alternative DABA sources or bypasses is not established.

5. **Physiological relevance vs. laboratory conditions.** Pyoverdine's ecological weight varies (minor role in some biocontrol contexts), so the module's importance is context-dependent even where the biochemistry is fixed.

**Most important open questions.**
- Is there direct substrate channeling of N5-hydroxyornithine (and its formylated form) and of DABA within the siderosome, and what interaction surfaces mediate it?
- What sets in vivo coupling efficiency and prevents PvdA uncoupling under fluctuating ornithine/NADPH pools?
- How conserved is the strict PvdH/asd dependence across the diverse pyoverdine-producing pseudomonads?
- Can the module be exploited as an antivirulence target or a biocatalytic tool (e.g., for engineered/clickable pyoverdines), given PvdA's and PvdH's defined specificities?

---

## 8. Mechanistic Model and Synthesis

The best current model treats pyoverdine precursor supply as **two parallel, chemically orthogonal reactions that are co-regulated and co-localized with the assembly line**:

```
                        IRON STARVATION
                     (Fur released → PvdS·RNAP)
                              │  transcription of pvd regulon
        ┌─────────────────────┴──────────────────────┐
        ▼                                             ▼
  ORNITHINE BRANCH                              DABA BRANCH
  L-ornithine                                   L-aspartate
     │  PvdA (FAD/NADPH/O2)                         │ Asd (feeder)
     │  C4a-OOH flavin, NADP+-gated                 ▼
     ▼                                          L-Asp-4-semialdehyde (ASA)
  N5-OH-L-ornithine                                 │  PvdH (PLP, ping-pong, α-KG)
     │  PvdF formyltransferase (tailoring)          ▼
     ▼                                          L-2,4-diaminobutyrate (DABA)
  N5-formyl-N5-OH-ornithine ───┐          ┌──────────┘
                               ▼          ▼
                        NRPS ASSEMBLY LINE (siderosome-embedded)
                               │
                               ▼
                          ferribactin → (export, periplasmic maturation) → pyoverdine
```

The module's coherence comes not from shared enzymology (PvdA and PvdH are unrelated) but from **shared logic**: both convert abundant central-metabolic inputs into scarce, specialized siderophore monomers; both are switched on only under iron limitation through the same Fur→PvdS cascade; and both are physically integrated into the siderosome where their reactive products can be delivered to the NRPS. Because the enzymes are conserved while the NRPS-encoded peptide diversifies, PvdA/PvdH function as a **reusable supply chassis** beneath a variable product — precisely the "reusable Pseudomonas module" framing of the review scope.

---

## 9. Evidence Base

| Claim | Key references (PMIDs) | Nature of support |
|---|---|---|
| PvdA is a flavin-dependent monooxygenase performing N5-hydroxylation of L-ornithine | [PMID: 17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/) | Direct biochemical identity |
| PvdA is a class B FAD-dependent flavoprotein monooxygenase (FAD N-hydroxylation, later formylation) | [PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/) | Family assignment + structures |
| PvdA steady-state kinetics: Km ≈ 0.58 mM, Vmax ≈ 1.34 µmol·min⁻¹·mg⁻¹ | [PMID: 17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/) | Purified-enzyme kinetics |
| C4a-hydroperoxyflavin stabilized by NADP+ (t½ ≈ 33 min); regulator of O2/substrate reactivity; effect extends to PvdA | [PMID: 20650894](https://pubmed.ncbi.nlm.nih.gov/20650894/) | Transient/steady-state kinetics |
| PvdA substrate inhibition + strict specificity; lysine a non-substrate effector | [PMID: 17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/) | Biochemical |
| PvdA structural/mechanistic context within N-hydroxylating FMO family (SidA, IucD, DesB) | [PMID: 21871647](https://pubmed.ncbi.nlm.nih.gov/21871647/), [PMID: 22928747](https://pubmed.ncbi.nlm.nih.gov/22928747/), [PMID: 33784308](https://pubmed.ncbi.nlm.nih.gov/33784308/) | Family/structural reviews |
| PvdH aminotransferase: ASA↔DABA, ping-pong, α-KG preference | [PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/) | Purified-enzyme kinetics |
| pvdH and asd knockouts abolish pyoverdine unless DABA supplied | [PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/) | Genetics |
| Same ASA→DABA reaction performed by ectoine EctB (shared DABA-transaminase family) | [PMID: 41652856](https://pubmed.ncbi.nlm.nih.gov/41652856/) | Comparative biochemistry |
| Precursor enzymes co-assemble with NRPSs into membrane-bound "siderosome" | [PMID: 24042050](https://pubmed.ncbi.nlm.nih.gov/24042050/) | Fractionation/interaction |
| PvdF interacts with a substrate-providing enzyme (channeling evidence) | [PMID: 33672312](https://pubmed.ncbi.nlm.nih.gov/33672312/) | Interaction (treat cautiously) |
| pvdA is iron-regulated; Fur-dependent | [PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/) | Genetics/promoter analysis |
| PvdS·RNAP holoenzyme binds pvdA promoter | [PMID: 10692351](https://pubmed.ncbi.nlm.nih.gov/10692351/) | In vitro transcription |
| Fur/PvdS/FpvI architecture governs pyoverdine synthesis and uptake | [PMID: 35171432](https://pubmed.ncbi.nlm.nih.gov/35171432/) | Review |
| AlgQ modulates PvdS-directed pvd transcription (anti-sigma for RpoD) | [PMID: 16030202](https://pubmed.ncbi.nlm.nih.gov/16030202/) | Genetics/mechanism |
| Pyoverdine structural/biosynthetic diversity; NRPS variation across strains | [PMID: 40572297](https://pubmed.ncbi.nlm.nih.gov/40572297/), [PMID: 39224222](https://pubmed.ncbi.nlm.nih.gov/39224222/), [PMID: 39352117](https://pubmed.ncbi.nlm.nih.gov/39352117/) | Comparative/genome mining |
| Context-dependent ecological role; strain specificity | [PMID: 42210498](https://pubmed.ncbi.nlm.nih.gov/42210498/), [PMID: 39143311](https://pubmed.ncbi.nlm.nih.gov/39143311/), [PMID: 40150866](https://pubmed.ncbi.nlm.nih.gov/40150866/) | Phenotypic/transcriptomic |
| Engineering pyoverdine via NRPS A-domain (downstream context) | [PMID: 39044227](https://pubmed.ncbi.nlm.nih.gov/39044227/) | Enzyme engineering |
| Iron uptake/regulation overviews in pseudomonads | [PMID: 20352420](https://pubmed.ncbi.nlm.nih.gov/20352420/), [PMID: 24294593](https://pubmed.ncbi.nlm.nih.gov/24294593/), [PMID: 19153809](https://pubmed.ncbi.nlm.nih.gov/19153809/) | Reviews |

---

## 10. Limitations and Knowledge Gaps

1. **Direct channeling unproven.** The siderosome model is supported by co-localization and interaction data, but no direct kinetic demonstration of intermediate channeling for the precursor branch exists. The key citation for a PvdF–substrate-provider interaction should be corroborated with orthogonal methods.
2. **Organism scope.** Core biochemistry is P. aeruginosa-centric; family-level claims mix data from fungi, enterobacteria, actinobacteria, and marine bacteria. Regulatory and in vivo details may not transfer across lineages.
3. **In vivo flux and coupling.** How PvdA avoids uncoupling and how intracellular α-KG/glutamate/ASA pools set PvdH directionality in living cells are not directly measured.
4. **DABA-branch redundancy.** Strict PvdH/asd dependence is shown in PAO1 only; alternative routes in other pseudomonads are untested.
5. **Boundary enzymes.** PvdF (formyltransferase) and Asd (feeder) sit at the module's edges; their precise classification depends on where one draws the module boundary.
6. **No PvdH structure.** Unlike PvdA (two crystal structures), PvdH lacks an experimental structure, leaving its active-site determinants inferred from homology (EctB and other fold-type-I transaminases).

---

## 11. Proposed Follow-up Experiments and Actions

1. **Test substrate channeling directly.** Use isotope-dilution / transient-kinetic assays with reconstituted PvdA + PvdF (and PvdH + downstream NRPS loading modules) to determine whether N5-hydroxyornithine and DABA are channeled versus released into bulk solvent. Combine with cryo-EM or crosslinking-MS of the siderosome to map interaction surfaces.
2. **In vivo flux and coupling.** Quantify NADPH/O2 coupling efficiency of PvdA under physiological ornithine/NADPH ratios in cell extracts and by metabolic labeling; test how ornithine-pool perturbations affect uncoupling (H2O2 production) and pyoverdine yield.
3. **Cross-strain genetics.** Perform pvdH and asd knockouts (with DABA rescue) across phylogenetically diverse pyoverdine producers (*P. fluorescens*, *P. putida*, *P. chlororaphis*, *P. donghuensis*) to test whether the strict DABA dependence is universal or has lineage-specific bypasses.
4. **Regulatory dissection.** Map PvdS-dependent promoters for pvdH and Asd-branch feeder genes; quantify co-transcription of precursor and NRPS genes under iron limitation and competitor cues by time-resolved RNA-seq.
5. **Structural completion.** Solve a PvdH crystal structure (currently lacking relative to PvdA) to confirm fold-type-I assignment, define the DABA/ASA and α-KG binding determinants, and compare directly with EctB.
6. **Biotechnological / antivirulence exploitation.** Given PvdA's strict specificity and PvdH's defined chemistry, evaluate the module as an antivirulence target (blocking hydroxamate/DABA supply) and as a supply chassis for engineered/"clickable" pyoverdine analogues, complementing NRPS A-domain engineering ([PMID: 39044227](https://pubmed.ncbi.nlm.nih.gov/39044227/)).

---

## 12. Key References

- Vandenende, Vlasschaert & Seah (2004). *Functional characterization of an aminotransferase required for pyoverdine siderophore biosynthesis in Pseudomonas aeruginosa PAO1.* [PMID: 15317763](https://pubmed.ncbi.nlm.nih.gov/15317763/)
- Ge & Seah (2006). *Heterologous expression, purification, and characterization of an l-ornithine N(5)-hydroxylase involved in pyoverdine siderophore biosynthesis in Pseudomonas aeruginosa.* [PMID: 17015659](https://pubmed.ncbi.nlm.nih.gov/17015659/)
- Meneely & Lamb (2007). *Biochemical characterization of a FAD-dependent monooxygenase, ornithine hydroxylase from Pseudomonas aeruginosa, suggests a novel reaction mechanism.* [PMID: 17900176](https://pubmed.ncbi.nlm.nih.gov/17900176/)
- Mayfield et al. (2010). *Comprehensive spectroscopic, steady state, and transient kinetic studies of a representative siderophore-associated flavin monooxygenase.* [PMID: 20650894](https://pubmed.ncbi.nlm.nih.gov/20650894/)
- Olucha et al. (2011). *Two structures of an N-hydroxylating flavoprotein monooxygenase: ornithine hydroxylase from Pseudomonas aeruginosa.* [PMID: 21757711](https://pubmed.ncbi.nlm.nih.gov/21757711/)
- Olucha & Lamb (2011). *Mechanistic and structural studies of the N-hydroxylating flavoprotein monooxygenases.* [PMID: 21871647](https://pubmed.ncbi.nlm.nih.gov/21871647/)
- Franceschini et al. (2012). *Structural insight into the mechanism of oxygen activation and substrate selectivity of flavin-dependent N-hydroxylating monooxygenases (SidA).* [PMID: 22928747](https://pubmed.ncbi.nlm.nih.gov/22928747/)
- Setser et al. (2021). *Characterization of a broadly specific cadaverine N-hydroxylase (DesB) involved in desferrioxamine B biosynthesis in Streptomyces sviceus.* [PMID: 33784308](https://pubmed.ncbi.nlm.nih.gov/33784308/)
- Skogvold et al. (2026). *Biochemical characterization and mutational analysis of the tetrameric DABA transaminase EctB from the Arctic bacterium Marinobacter sp. CK1.* [PMID: 41652856](https://pubmed.ncbi.nlm.nih.gov/41652856/)
- Imperi & Visca (2013). *Subcellular localization of the pyoverdine biogenesis machinery of Pseudomonas aeruginosa: a membrane-associated "siderosome".* [PMID: 24042050](https://pubmed.ncbi.nlm.nih.gov/24042050/)
- Philem et al. (2021). *Identification of Active Site Residues of the Siderophore Synthesis Enzyme PvdF and Evidence for Interaction of PvdF with a Substrate-Providing Enzyme.* [PMID: 33672312](https://pubmed.ncbi.nlm.nih.gov/33672312/)
- Leoni et al. (1996). *Iron-regulated transcription of the pvdA gene in Pseudomonas aeruginosa: effect of Fur and PvdS on promoter activity.* [PMID: 8636031](https://pubmed.ncbi.nlm.nih.gov/8636031/)
- Leoni et al. (2000). *Functional analysis of PvdS, an iron starvation sigma factor of Pseudomonas aeruginosa.* [PMID: 10692351](https://pubmed.ncbi.nlm.nih.gov/10692351/)
- Ambrosi et al. (2005). *Involvement of AlgQ in transcriptional regulation of pyoverdine genes in Pseudomonas aeruginosa PAO1.* [PMID: 16030202](https://pubmed.ncbi.nlm.nih.gov/16030202/)
- Cornelis & Matthijs (2023). *High affinity iron uptake by pyoverdine in Pseudomonas aeruginosa involves multiple regulators besides Fur, PvdS, and FpvI.* [PMID: 35171432](https://pubmed.ncbi.nlm.nih.gov/35171432/)
- Genome-mining / diversity: [PMID: 39352117](https://pubmed.ncbi.nlm.nih.gov/39352117/), [PMID: 40572297](https://pubmed.ncbi.nlm.nih.gov/40572297/), [PMID: 39224222](https://pubmed.ncbi.nlm.nih.gov/39224222/)
- Reviews / context: [PMID: 20352420](https://pubmed.ncbi.nlm.nih.gov/20352420/), [PMID: 24294593](https://pubmed.ncbi.nlm.nih.gov/24294593/), [PMID: 19153809](https://pubmed.ncbi.nlm.nih.gov/19153809/), [PMID: 39044227](https://pubmed.ncbi.nlm.nih.gov/39044227/)

---

*Prepared as a commissioned review synthesis. Claims are anchored to the cited primary literature and reviews; uncertainty is flagged explicitly, and biochemical generalizations across organisms are qualified where the underlying data derive from different species or assay systems.*


## Artifacts

- [OpenScientist final report](pseudomonas_pyoverdine_precursor_supply-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pseudomonas_pyoverdine_precursor_supply-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:35171432
2. PMID:20650894
3. PMID:17900176
4. PMID:15317763
5. PMID:17015659
6. PMID:21757711
7. PMID:21871647
8. PMID:22928747
9. PMID:33784308
10. PMID:41652856
11. PMID:24042050
12. PMID:33672312
13. PMID:8636031
14. PMID:10692351
15. PMID:16030202
16. PMID:40150866
17. PMID:40572297
18. PMID:39224222
19. PMID:39352117
20. PMID:41792602
21. PMID:39143311
22. PMID:42210498
23. PMID:39044227
24. PMID:20352420
25. PMID:24294593
26. PMID:19153809