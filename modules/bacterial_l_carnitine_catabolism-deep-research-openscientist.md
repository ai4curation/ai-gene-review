---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:25:28.512256'
end_time: '2026-08-13T05:37:15.056952'
duration_seconds: 706.54
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial L-carnitine catabolism through 3-dehydrocarnitine
  module_summary: A bacterial L-carnitine utilization module in which imported L-carnitine
    is oxidized to 3-dehydrocarnitine, cleaved to a betainyl-CoA intermediate, and
    converted to glycine betaine. The oxygenolytic CntAB route, anaerobic Cai reduction,
    compatible-solute retention, and downstream glycine-betaine demethylation are
    outside this boundary.
  module_outline: "- Bacterial L-carnitine catabolism through 3-dehydrocarnitine\n\
    \  - 1. L-carnitine uptake\n  - L-carnitine uptake\n  - 2. L-carnitine oxidation\n\
    \  - L-carnitine to 3-dehydrocarnitine\n  - 3. 3-dehydrocarnitine cleavage\n \
    \ - 3-dehydrocarnitine cleavage\n  - 4. glycine-betaine formation\n  - Betainyl-CoA\
    \ conversion to glycine betaine"
  module_connections: '- L-carnitine uptake feeds into L-carnitine to 3-dehydrocarnitine

    - L-carnitine to 3-dehydrocarnitine feeds into 3-dehydrocarnitine cleavage

    - 3-dehydrocarnitine cleavage feeds into Betainyl-CoA conversion to glycine betaine'
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
  path: bacterial_l_carnitine_catabolism-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_l_carnitine_catabolism-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial L-carnitine catabolism through 3-dehydrocarnitine

## Working Scope

A bacterial L-carnitine utilization module in which imported L-carnitine is oxidized to 3-dehydrocarnitine, cleaved to a betainyl-CoA intermediate, and converted to glycine betaine. The oxygenolytic CntAB route, anaerobic Cai reduction, compatible-solute retention, and downstream glycine-betaine demethylation are outside this boundary.

## Provisional Biological Outline

- Bacterial L-carnitine catabolism through 3-dehydrocarnitine
  - 1. L-carnitine uptake
  - L-carnitine uptake
  - 2. L-carnitine oxidation
  - L-carnitine to 3-dehydrocarnitine
  - 3. 3-dehydrocarnitine cleavage
  - 3-dehydrocarnitine cleavage
  - 4. glycine-betaine formation
  - Betainyl-CoA conversion to glycine betaine

## Known Relationships Among Steps

- L-carnitine uptake feeds into L-carnitine to 3-dehydrocarnitine
- L-carnitine to 3-dehydrocarnitine feeds into 3-dehydrocarnitine cleavage
- 3-dehydrocarnitine cleavage feeds into Betainyl-CoA conversion to glycine betaine

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

# Bacterial L-Carnitine Catabolism Through 3-Dehydrocarnitine

*A review-style synthesis for a molecular-biology audience*

---

## 1. Executive summary

Many aerobic bacteria — best characterized in the pseudomonads and related
α/γ-proteobacteria — can grow on L-carnitine as a sole carbon and/or nitrogen
source by dismantling its four-carbon backbone rather than by simply importing
carnitine as a compatible solute. The route reviewed here is a compact
four-step **assimilatory module**: (1) L-carnitine is imported by a modular ABC
transporter; (2) it is oxidized by an NAD⁺-dependent **L-carnitine dehydrogenase
(EC 1.1.1.108)** to the β-keto acid **3-dehydrocarnitine**; (3) 3-dehydrocarnitine
is cleaved by a **CoA-dependent 3-ketoacid CoA-transferase/thiolase system** that
removes a two-carbon (acetyl) unit through a **betainyl-CoA** thioester; and
(4) the betainyl-CoA is resolved to **glycine betaine**, which then enters the
independent glycine-betaine → glycine catabolic pathway.

The overall logic is that of a β-keto-acid chain-shortening reaction grafted
onto quaternary-ammonium chemistry: oxidation of the C3 hydroxyl converts an
inert β-hydroxy acid into a labile β-keto acid that can be thiolytically shortened
by two carbons, converting the 4-carbon carnitine backbone (N–C–C–C–COO⁻) into
the 2-carbon betaine backbone (N–C–COO⁻). The committed oxidation is
thermodynamically unfavorable and is pulled forward by the essentially
irreversible downstream cleavage. This oxidative, aerobic route is one of three
mechanistically distinct ways bacteria attack carnitine, and it must be kept
separate from (i) the oxygenolytic **CntAB** route that cleaves carnitine to
trimethylamine (TMA), and (ii) the anaerobic **Cai** route that reduces carnitine
via crotonobetaine to γ-butyrobetaine. The strongest evidence is genetic
(loss-of-function screens in *Pseudomonas aeruginosa*) and enzymological (purified
dehydrogenases); the CoA-transferase/thiolase cleavage chemistry and the
betainyl-CoA intermediate are inferred from gene annotation, reaction
stoichiometry, and precedent, and remain the least directly proven link.

---

## 2. Definition and biological boundaries

**What is inside the system.** The reviewed module is the set of reactions that
convert *extracellular L-carnitine* into *intracellular glycine betaine* via
*3-dehydrocarnitine*, comprising exactly four functional steps:

1. **Uptake** of L-carnitine across the cytoplasmic membrane.
2. **Oxidation** of L-carnitine to 3-dehydrocarnitine (L-carnitine
   dehydrogenase, EC 1.1.1.108).
3. **Cleavage** of 3-dehydrocarnitine, with CoA activation of the β-keto acid and
   thiolytic loss of a C2 unit, generating a betainyl-CoA intermediate.
4. **Glycine-betaine formation** from betainyl-CoA (thioester resolution).

**What is outside the system (and frequently confused with it).**

- **The oxygenolytic CntAB route → TMA.** A two-component Rieske-type
  oxygenase/reductase (CntA/CntB) cleaves the C–N bond of carnitine to yield
  trimethylamine plus malic semialdehyde (PMID 24591617; biophysics in
  PMID 32694223). This is medically prominent (TMA → hepatic TMAO → cardiovascular
  risk) but is chemically and enzymologically unrelated to the dehydrogenase
  route: it destroys the quaternary amine instead of preserving it as betaine.
- **The anaerobic Cai/crotonobetaine route.** In *Escherichia coli* and other
  Enterobacteriaceae, the *caiTABCDE* operon (anaerobic, CRP/H-NS regulated)
  converts carnitine via crotonobetaine to γ-butyrobetaine using a
  carnitine/crotonobetaine dehydratase (CaiB) and a CoA-transferase/ligase
  (CaiC), with CaiT as the transporter (PMID 7815937; PMID 8188598). Confusingly,
  this route *also* uses CoA thioesters and *also* has a protein called "CaiB,"
  but it is a reductive fermentative pathway that never passes through
  3-dehydrocarnitine or glycine betaine.
- **Compatible-solute retention.** Carnitine and glycine betaine are also imported
  and *retained unmodified* as osmoprotectants (e.g., via BCCT/OpuC transporters;
  PMID 17660277). Osmoprotective accumulation and catabolic assimilation share
  transporters but are opposite fates; the reviewed system is the catabolic fate.
- **Downstream glycine-betaine demethylation.** Once glycine betaine is formed,
  its stepwise demethylation to dimethylglycine → sarcosine → glycine
  (gbcAB, dgcAB, soxBDAG in *P. aeruginosa*; PMID 17951379) is a separate,
  independently regulated pathway. It is the *sink* for this module's product but
  is not part of the module itself.

**Competing definitions.** The older enzymological literature (reviewed by Kleber,
PMID 9037756) frames "bacterial carnitine metabolism" as three routes and treats
the dehydrogenase route as *the* assimilatory pathway. Some sources loosely equate
"carnitine catabolism" with the gut-microbiome TMA route because of its clinical
salience. This review adopts the narrow, mechanistic definition: the
oxidative 3-dehydrocarnitine → betaine module.

---

## 3. Mechanistic overview

**Step 1 — Uptake (obligatory, but not pathway-specific).** L-carnitine crosses
the membrane before any chemistry occurs. In pseudomonads this is accomplished by
the **Cbc ABC transporter**, an unusual system in which a single core
permease/ATPase module (**CbcWV**) recruits several interchangeable periplasmic
substrate-binding proteins (SBPs). The carnitine-specific SBP **CaiX** binds
L-carnitine (Kₘ ≈ 24 µM), while choline- and betaine-specific SBPs (CbcX, BetX)
serve the same core (PMID 19919675). Lower-affinity, broad-specificity BCCT/OpuC
transporters can also admit carnitine (PMID 17660277). Uptake is therefore
obligatory for the pathway but is shared machinery, not a dedicated carnitine
importer.

**Step 2 — Oxidation (committed step).** Cytoplasmic **L-carnitine:NAD⁺
oxidoreductase (EC 1.1.1.108)** oxidizes the C3 hydroxyl of L-carnitine to a
ketone, producing 3-dehydrocarnitine (3-oxo-4-trimethylaminobutyrate) and NADH.
Purified enzymes from *Agrobacterium* sp. (114 kDa homodimer; PMID 8645721) and
*Pseudomonas putida* (62 kDa homodimer; PMID 3058208) are strictly specific for
L-carnitine and NAD⁺. The equilibrium lies far toward carnitine (Kₑq ≈ 2×10⁻¹²
for the analogous D-enzyme; PMID 9003445), so the step is thermodynamically
uphill and proceeds only because 3-dehydrocarnitine is rapidly consumed and NADH
is reoxidized by respiration. This is the *committed* step of the module.

**Step 3 — Cleavage (the defining, rate-committing chemistry).**
3-Dehydrocarnitine is a **β-keto acid**: carboxylate at C1, ketone at C3. Two
features follow. First, like all β-keto acids it is intrinsically prone to
decarboxylation, so it is a reactive, transient intermediate. Second, its C2–C3
bond is activated toward thiolytic (retro-Claisen) cleavage once the C1
carboxylate is converted to a CoA thioester. In *P. aeruginosa*, genetic screening
identified **PA1999–PA2000**, the α/β subunits of a predicted **3-ketoacid
CoA-transferase**, as required for growth on carnitine and proposed to catalyze
"the first step of deacetylation of 3-dhc" (PMID 19406895). The most parsimonious
chemistry is: CoA transfer onto 3-dehydrocarnitine → 3-dehydrocarnitinyl-CoA
(a β-ketoacyl-CoA) → thiolytic cleavage releasing **acetyl-CoA** (from C1–C2) and
leaving **betainyl-CoA** (from C3–C4; i.e., trimethylammonio-acetyl-CoA). This
removes exactly two carbons and accounts for the carnitine→betaine backbone
shortening.

**Step 4 — Glycine-betaine formation.** The betainyl-CoA thioester is resolved to
free **glycine betaine** — either by hydrolysis (thioesterase) or, more
economically, by CoA transfer back onto an incoming 3-dehydrocarnitine molecule,
which would make the CoA-transferase catalytic and couple steps 3 and 4. Glycine
betaine is the obligate product: an intact glycine-betaine catabolic pathway is
independently required for growth on carnitine (PMID 19406895).

**Obligatory vs. conditional vs. accessory.**
- *Obligatory:* oxidation (step 2) and cleavage (step 3) — no growth without them.
- *Conditional/shared:* uptake (step 1), which can be served by several
  transporters; the specific importer used depends on the organism and osmotic
  context.
- *Accessory / downstream sink:* betaine demethylation, NADH reoxidation, and
  acetyl-CoA disposal are required for net assimilation but belong to central
  metabolism, not the module proper.

---

## 4. Major molecular players and active assemblies

| Step | Function | Best-characterized players | Notes / evidence |
|------|----------|---------------------------|------------------|
| 1. Uptake | Import L-carnitine | **Cbc ABC transporter**: core **CbcWV** + carnitine-specific SBP **CaiX** (Kₘ ≈ 24 µM); also BCCT/OpuC | Modular SBP recruitment; PMID 19919675, 17660277 |
| 2. Oxidation | L-carnitine → 3-dehydrocarnitine + NADH | **L-carnitine dehydrogenase, EC 1.1.1.108** (homodimer; NAD⁺-specific) | Purified from *Agrobacterium* (PMID 8645721), *P. putida* (PMID 3058208); *P. aeruginosa* homologue in PA5388–PA5384 locus (PMID 19406895) |
| 3. Cleavage | 3-dehydrocarnitine (+CoA) → betainyl-CoA + acetyl-CoA | **3-ketoacid CoA-transferase** (α/β subunits, *P. aeruginosa* **PA1999–PA2000**) + thiolase activity | Genetically required; enzymology inferred (PMID 19406895) |
| 4. Betaine formation | betainyl-CoA → glycine betaine | Thioesterase or CoA-transfer resolution (enzyme not definitively assigned) | Glycine betaine confirmed as obligate product (PMID 19406895) |
| Regulation | Substrate-responsive induction | *P. aeruginosa* PA5389 (induces dehydrogenase locus in response to carnitine) and PA1998 (induces PA1999–PA2000) | Transcription-factor pair; PMID 19406895 |
| Product sink (outside module) | Glycine betaine → glycine | GbcAB, DgcAB, SoxBDAG; master regulator **GbdR** | PMID 17951379, 24097953 |

**Regulatory architecture.** The two catabolic loci in *P. aeruginosa* are
independently induced: PA5389 drives the dehydrogenase region in response to
carnitine, and PA1998 drives the CoA-transferase region (PMID 19406895).
Downstream, the AraC-family regulator **GbdR** integrates the betaine node,
inducing betaine/DMG/sarcosine catabolism *and* the quaternary-amine transporters
(BetX, CbcXWV) in response to glycine betaine and dimethylglycine (PMID 24097953),
with SouR providing sarcosine-specific control (PMID 26503852). Thus carnitine
assimilation is wired as a relay of substrate-responsive AraC/other regulators
rather than a single operon.

---

## 5. Evolutionary and cell-biological variation

**Lineage distribution.** The oxidative dehydrogenase route is documented across
diverse aerobic proteobacteria — *Pseudomonas* (putida, aeruginosa),
*Agrobacterium*/*Rhizobium*, and other soil/plant-associated organisms
(PMID 9037756). The Cbc/CaiX uptake system is shared between *P. aeruginosa* and
the plant pathogen *P. syringae* (PMID 19919675), indicating conservation of at
least the uptake and probably the catabolic logic across the genus.

**Alternative routes to overlapping outcomes.** Different lineages have evolved
biochemically unrelated solutions to the same substrate:
- *Oxidative assimilation* (this module) — pseudomonads/rhizobia, preserves the
  quaternary amine and funnels it to glycine.
- *Oxygenolytic C–N cleavage to TMA* — *Acinetobacter*, gut microbiota; CntAB
  Rieske oxygenase (PMID 24591617). Destroys the trimethylammonium head group.
- *Anaerobic reduction to γ-butyrobetaine* — Enterobacteriaceae; Cai system
  (PMID 7815937, 8188598). A redox-sink fermentative use.
These are best viewed as convergent, ecologically partitioned strategies (aerobic
soil catabolism vs. anaerobic gut vs. facultative), not variants of one pathway.

**Physiological-state variation.** Because carnitine and glycine betaine are also
potent osmoprotectants, the same imported molecule can be *catabolized* or
*retained* depending on osmotic stress, nitrogen/carbon limitation, and regulator
state. Under high osmolarity, retention (BCCT/OpuC accumulation) is favored;
under nutrient limitation with low osmotic stress, catabolic assimilation
dominates. This is a genuine state-dependent fork rather than a fixed fate.

**Host relevance.** In *P. aeruginosa*, host-derived quaternary amines (choline,
carnitine, glycine betaine) are abundant nutrients during infection, and their
catabolism is linked (via GbdR) to expression of virulence-associated
phospholipase C (PMID 19103776, 24097953), tying this catabolic module to the
organism's nutritional adaptation in host tissue.

---

## 6. Constraints, dependencies, and failure modes

**Mandatory ordering.** The steps are strictly sequential and each depends on the
prior product: uptake → oxidation → cleavage → betaine formation. Oxidation
*must* precede cleavage because the cleavage chemistry requires the C3 **ketone**;
the parent β-hydroxy acid (carnitine) cannot undergo thiolytic C2 shortening. This
is the key chemical constraint that rules out a direct carnitine → betaine
conversion without prior oxidation.

**Thermodynamic pull.** The committed oxidation is strongly endergonic
(Kₑq ≈ 10⁻¹²; PMID 9003445). The pathway can run only if (i) 3-dehydrocarnitine is
consumed rapidly by an essentially irreversible cleavage and (ii) NADH is
reoxidized — i.e., the route is effectively **aerobic/respiratory**. This explains
why the assimilatory route is found in aerobes and why the alternative anaerobic
fate of carnitine uses an entirely different (reductive) chemistry.

**Intermediate instability.** 3-Dehydrocarnitine is a β-keto acid prone to
spontaneous decarboxylation; efficient channeling to the CoA-transferase is likely
needed to avoid loss of the intermediate. This is a plausible driver for coupling
the dehydrogenase and CoA-transferase steps and for co-regulation of the two loci.

**Compartment/co-substrate constraints.** All chemistry after uptake is
cytoplasmic and requires NAD⁺ and CoA/acyl-CoA pools; the acetyl-CoA released
feeds central metabolism, and the CoA must be recycled (via transfer or
thioesterase) for the pathway to be catalytic. Failure to reoxidize NADH or to
recycle CoA would stall the module.

**Failure modes / genetic evidence.** Loss of the dehydrogenase locus
(PA5388–PA5384), the CoA-transferase locus (PA1999–PA2000), their regulators
(PA5389, PA1998), or the downstream glycine-betaine catabolic genes each abolishes
growth on carnitine in *P. aeruginosa* (PMID 19406895), confirming that all four
functional steps plus the betaine sink are jointly required for assimilation.

---

## 7. Controversies and open questions

1. **Direct enzymology of the cleavage step.** The 3-ketoacid CoA-transferase
   assignment (PA1999–PA2000) rests on gene annotation, mutant phenotypes, and
   reaction logic (PMID 19406895); the enzyme has not, to the standard of the
   purified dehydrogenases, been shown *in vitro* to convert 3-dehydrocarnitine to
   betainyl-CoA + acetyl-CoA. Whether a separate thiolase completes the thiolysis,
   and whether the "CoA-transferase" is truly a transferase (recycling CoA) or a
   ligase, remains to be nailed down.

2. **Existence and isolation of betainyl-CoA.** The betainyl-CoA intermediate is
   chemically reasonable and is named in pathway schemes, but its direct isolation
   and characterization from this route are, to our reading, not firmly
   established. This is the single most important experimental gap.

3. **CoA donor/acceptor identity.** If step 3 is a CoA-transferase, what is the
   physiological CoA donor (succinyl-CoA? acetoacetyl-CoA? the betainyl-CoA of the
   previous cycle)? Coupling steps 3 and 4 as a single catalytic CoA relay is
   attractive but unproven.

4. **How the enzyme escapes decarboxylation of the β-keto acid.** Mechanistically,
   channeling or a specific binding mode must suppress non-productive
   decarboxylation of 3-dehydrocarnitine; this has not been structurally addressed.

5. **Generality beyond pseudomonads.** Much of the *pathway-level genetic* evidence
   is from *P. aeruginosa*, while much of the *enzyme* evidence is from
   *Agrobacterium* and *P. putida*. Whether the same gene complement and regulatory
   wiring operate across all organisms said to use "the dehydrogenase route" is
   inferred, not comprehensively demonstrated — a caution against overgeneralizing
   from one organism.

6. **Evolutionary origin.** The dehydrogenase belongs to the broad
   short-chain-dehydrogenase-like landscape of NAD⁺ oxidoreductases, and the
   cleavage enzyme to the ancient, widely distributed **CoA-transferase/thiolase**
   superfamilies used throughout β-keto-acid and fatty-acid metabolism. The most
   plausible reading is that this module is a **repurposing of pre-existing
   β-keto-acid chain-shortening chemistry** to quaternary-ammonium substrates,
   rather than a de novo invention. Identifying the closest non-carnitine
   CoA-transferase/thiolase relatives (e.g., generic 3-oxoacid CoA-transferases,
   SCOT/OXCT-type enzymes) would be the best way to reconstruct the ancestral role;
   this phylogenetic analysis has not been done specifically for the carnitine
   enzymes.

---

## 8. Key references

- Kleber H-P. **Bacterial carnitine metabolism.** *FEMS Microbiol Lett* 1997.
  PMID 9037756. — Authoritative three-route framework; defines the boundaries.
- Wargo MJ, Hogan DA. **Identification of genes required for *Pseudomonas
  aeruginosa* carnitine catabolism.** *Microbiology* 2009. PMID 19406895. —
  Central genetic dissection: dehydrogenase locus, 3-ketoacid CoA-transferase
  (PA1999–PA2000), regulators, glycine-betaine requirement.
- Hanschmann H, Ehricht R, Kleber H-P. **Purification and properties of
  L(-)-carnitine dehydrogenase from *Agrobacterium* sp.** 1996. PMID 8645721. —
  Committed oxidation enzyme (EC 1.1.1.108).
- Goulas P. **Purification and properties of carnitine dehydrogenase from
  *Pseudomonas putida*.** 1988. PMID 3058208. — Independent purification.
- Hanschmann H, Kleber H-P. **D(+)-carnitine dehydrogenase from *Agrobacterium*
  sp.** 1997. PMID 9003445. — Equilibrium constant; pathway thermodynamics.
- Chen C, Malek AA, Wargo MJ, Hogan DA, Beattie GA. **The ABC transporter Cbc
  recruits multiple substrate-binding proteins...** *Mol Microbiol* 2010.
  PMID 19919675. — Uptake machinery; carnitine-specific CaiX.
- Wargo MJ, Szwergold BS, Hogan DA. **Two gene clusters and a regulator for
  *P. aeruginosa* glycine betaine catabolism.** 2008. PMID 17951379. — Downstream
  sink (out of scope but essential context).
- Hampel KJ, et al. **Characterization of the GbdR regulon in *P. aeruginosa*.**
  2014. PMID 24097953. — Regulatory integration of the betaine node.
- Zhu Y, et al. **Carnitine metabolism to trimethylamine by an unusual Rieske-type
  oxygenase.** *PNAS* 2014. PMID 24591617. — CntAB route (boundary/excluded).
- Massmig M, et al. **Two-component carnitine monooxygenase CntAB.** 2020.
  PMID 32694223. — CntAB biophysics (boundary/excluded).
- Eichler K, et al. **Molecular characterization of the *cai* operon in
  *E. coli*.** 1994. PMID 7815937. — Anaerobic Cai route (boundary/excluded).

---

### Evidence-confidence key
- **Strong (purified enzyme / genetic loss-of-function):** committed oxidation by
  L-carnitine dehydrogenase; requirement of the dehydrogenase and CoA-transferase
  loci and of the betaine sink for growth; identity/affinity of the Cbc/CaiX
  uptake system.
- **Moderate (annotation + phenotype + reaction logic):** the CoA-transferase as
  the cleavage catalyst; two-carbon (acetyl-CoA) loss; glycine betaine as product.
- **Inferred / open:** the discrete betainyl-CoA intermediate and its isolation;
  the CoA donor/acceptor and step-3/step-4 coupling; cross-lineage generality of
  the exact gene complement; the pathway's detailed phylogenetic origin.


## Artifacts

- [OpenScientist final report](bacterial_l_carnitine_catabolism-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_l_carnitine_catabolism-deep-research-openscientist_artifacts/final_report.pdf)