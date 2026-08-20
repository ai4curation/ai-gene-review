---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T08:19:10.441080'
end_time: '2026-08-13T08:40:25.984891'
duration_seconds: 1275.54
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial purine nucleoside and nucleobase salvage
  module_summary: A reusable bacterial salvage module in which purine nucleosides
    are phosphorolyzed to free bases and ribose 1-phosphate, after which adenine,
    hypoxanthine or guanine, and xanthine are returned to the nucleotide pool as AMP,
    IMP or GMP, and XMP. The three phosphoribosyltransferase branches use PRPP and
    release diphosphate.
  module_outline: "- Bacterial purine nucleoside and nucleobase salvage\n  - 1. liberation\
    \ of purine bases from nucleosides\n  - Purine nucleoside phosphorolysis\n   \
    \ - PpnP purine-nucleoside phosphorylase activity (molecular player: PpnP pyrimidine/purine\
    \ nucleoside phosphorylase family; activity or role: purine-nucleoside phosphorylase\
    \ activity)\n  - 2. adenine salvage\n  - Adenine conversion to AMP\n    - Apt\
    \ adenine phosphoribosyltransferase activity (molecular player: Adenine phosphoribosyltransferase\
    \ family; activity or role: adenine phosphoribosyltransferase activity)\n  - 3.\
    \ hypoxanthine and guanine salvage\n  - Hypoxanthine and guanine conversion to\
    \ IMP and GMP\n    - HGPRT hypoxanthine-guanine phosphoribosyltransferase activity\
    \ (molecular player: Hypoxanthine-guanine phosphoribosyltransferase family; activity\
    \ or role: hypoxanthine phosphoribosyltransferase activity)\n  - 4. xanthine salvage\n\
    \  - Xanthine conversion to XMP\n    - Xpt xanthine phosphoribosyltransferase\
    \ activity (molecular player: Xanthine phosphoribosyltransferase subfamily; activity\
    \ or role: xanthine phosphoribosyltransferase activity)"
  module_connections: '- Purine nucleoside phosphorolysis feeds into Adenine conversion
    to AMP: PpnP can release adenine from adenosine for Apt-dependent salvage.

    - Purine nucleoside phosphorolysis feeds into Hypoxanthine and guanine conversion
    to IMP and GMP: PpnP can release hypoxanthine or guanine from inosine or guanosine
    for HGPRT-dependent salvage.

    - Purine nucleoside phosphorolysis feeds into Xanthine conversion to XMP: PpnP
    can release xanthine from xanthosine for Xpt-dependent salvage.'
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
  path: bacterial_purine_salvage-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_purine_salvage-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial purine nucleoside and nucleobase salvage

## Working Scope

A reusable bacterial salvage module in which purine nucleosides are phosphorolyzed to free bases and ribose 1-phosphate, after which adenine, hypoxanthine or guanine, and xanthine are returned to the nucleotide pool as AMP, IMP or GMP, and XMP. The three phosphoribosyltransferase branches use PRPP and release diphosphate.

## Provisional Biological Outline

- Bacterial purine nucleoside and nucleobase salvage
  - 1. liberation of purine bases from nucleosides
  - Purine nucleoside phosphorolysis
    - PpnP purine-nucleoside phosphorylase activity (molecular player: PpnP pyrimidine/purine nucleoside phosphorylase family; activity or role: purine-nucleoside phosphorylase activity)
  - 2. adenine salvage
  - Adenine conversion to AMP
    - Apt adenine phosphoribosyltransferase activity (molecular player: Adenine phosphoribosyltransferase family; activity or role: adenine phosphoribosyltransferase activity)
  - 3. hypoxanthine and guanine salvage
  - Hypoxanthine and guanine conversion to IMP and GMP
    - HGPRT hypoxanthine-guanine phosphoribosyltransferase activity (molecular player: Hypoxanthine-guanine phosphoribosyltransferase family; activity or role: hypoxanthine phosphoribosyltransferase activity)
  - 4. xanthine salvage
  - Xanthine conversion to XMP
    - Xpt xanthine phosphoribosyltransferase activity (molecular player: Xanthine phosphoribosyltransferase subfamily; activity or role: xanthine phosphoribosyltransferase activity)

## Known Relationships Among Steps

- Purine nucleoside phosphorolysis feeds into Adenine conversion to AMP: PpnP can release adenine from adenosine for Apt-dependent salvage.
- Purine nucleoside phosphorolysis feeds into Hypoxanthine and guanine conversion to IMP and GMP: PpnP can release hypoxanthine or guanine from inosine or guanosine for HGPRT-dependent salvage.
- Purine nucleoside phosphorolysis feeds into Xanthine conversion to XMP: PpnP can release xanthine from xanthosine for Xpt-dependent salvage.

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

# Bacterial Purine Nucleoside and Nucleobase Salvage: A Modular Two-Tier Recycling System

*A commissioned review-style synthesis for a molecular-biology audience.*
*Search date: 2026-08-13. Evidence base: primary literature and authoritative reviews retrieved via PubMed.*

---

## 1. Executive summary

Bacteria rarely build purine nucleotides from scratch when preformed purines are
available. Instead they run a compact, reusable **salvage module** organized into
two tiers. In the **first tier**, purine nucleosides (adenosine, inosine,
guanosine, xanthosine) are cleaved by **nucleoside phosphorylases** in a
phosphate-dependent reaction that liberates the free base and **α-D-ribose
1-phosphate (R1P)**. In the **second tier**, three **type I
phosphoribosyltransferases (PRTases)** reattach the freed bases to the activated
sugar donor **5-phospho-α-D-ribose 1-diphosphate (PRPP)**, releasing
**diphosphate (PPi)** and regenerating nucleoside monophosphates: **Apt** makes
**AMP** from adenine; **HGPRT/Hpt** makes **IMP and GMP** from hypoxanthine and
guanine; and **Xpt** (or the broader-specificity **Gpt** in enterobacteria) makes
**XMP** from xanthine (PMID 26443734).

The module is best understood as a *shared phosphorolysis front end feeding three
parallel, base-specific outputs*. Its second tier is ancient: the four purine
PRTases are paralogues of one another and are homologous to the nucleoside
phosphorylases, assembled by gene duplication and "patchwork" recruitment before
the divergence of Bacteria, Archaea and Eukarya (PMID 9742728). The first tier is
mechanistically redundant and evolutionarily heterogeneous: purine-nucleoside
phosphorylase activity is delivered by at least three unrelated protein folds —
the classical trimeric/hexameric **NP-I (DeoD)** family, the **NP-II
(XapA/Pdp)** family, and the more recently characterized **Cupin-fold PpnP**
(PMID 35094440, 11444965). This review defines the system's boundaries,
reconstructs its mechanism, surveys lineage variation, traces its deep origin,
and flags the points where evidence is thin or contested.

---

## 2. Definition and biological boundaries

**What is included.** The salvage module comprises exactly two enzymatic
operations acting on the N-glycosyl bond and the base:

1. **Phosphorolysis of purine nucleosides** to free base + R1P
   (PpnP; and, in most bacteria, the classical PNPs DeoD and XapA).
2. **Phosphoribosyl transfer** from PRPP onto a free purine base to give a
   nucleoside-5′-monophosphate + PPi (Apt, HGPRT/Hpt, Xpt/Gpt).

The defining chemistry is the making and breaking of the N-glycosyl bond that
links base to ribosyl moiety, together with PRPP-dependent nucleotide formation
(PMID 26443734). By this definition the system's inputs are *extracellular or
intracellular purine bases and nucleosides*, and its output is *the purine
nucleotide monophosphate pool (AMP, IMP, GMP, XMP)*.

**Neighboring processes that should be treated separately.** Several adjacent
pathways are frequently conflated with salvage but are mechanistically and
genetically distinct:

- **De novo purine biosynthesis** (the *pur* regulon: PurF→…→IMP) builds IMP from
  PRPP, amino acids and one-carbon units. Salvage and de novo *converge* on the
  IMP/AMP/GMP pool but use entirely different enzymes; they are coupled only
  through shared PRPP demand and through regulation (Section 6).
- **Nucleotide interconversion** — IMP→AMP (PurA/PurB), IMP→XMP→GMP (GuaB/GuaA),
  and the deaminase/reductase steps (Add, GuaC/GuaD) — reshapes the monophosphate
  pool *after* salvage. These are downstream of, not part of, the salvage module,
  although they determine which base a given nucleoside ultimately becomes.
- **Nucleoside kinases** (e.g., guanosine–inosine kinase Gsk; adenosine kinase in
  some taxa) provide an *alternative, phosphorylytic-independent* route from
  nucleoside to nucleotide **without** passing through a free base. This is a
  genuine competing route (Section 5), not part of the phosphorolysis→PRTase
  logic, and its presence varies by lineage (PMID 765747).
- **Ribose-1-phosphate disposal** (via Deo enzymes / phosphopentomutase into
  central carbon metabolism) is the fate of the sugar co-product and links
  salvage to carbon/energy metabolism, but is not itself a salvage step.
- **Transport** (NupC/NupG nucleoside permeases; base permeases such as PbuX,
  PbuG, and NCS2/NCS1 family transporters; the xanthosine permease XapB) delivers
  substrates but is accessory to the catalytic core (PMID 30341391, 11466294).

**Competing definitions.** The brief treats **PpnP** as *the* purine-nucleoside
phosphorylase of the module. The broader literature is more pluralistic: in
*E. coli* the historically dominant purine-nucleoside phosphorylase is the
*deoD*-encoded **hexameric PNP-I**, with **XapA** handling xanthosine, and PpnP is
an additional broad-specificity (pyrimidine *and* purine) enzyme (PMID 17639373,
11466294, 35094440). A rigorous scope therefore treats "purine-nucleoside
phosphorylase activity" as a *function* that can be discharged by any of three
unrelated families, of which PpnP is the newest and most catholic member, rather
than a single obligatory enzyme.

---

## 3. Mechanistic overview

**Tier 1 — phosphorolysis (base liberation).** The general reaction is:

> purine nucleoside + Pi ⇌ purine base + α-D-ribose 1-phosphate

The reaction is freely reversible and near-equilibrium; direction is set by
substrate/product concentrations and by downstream pull. For the classical PNPs,
catalysis proceeds through an oxocarbenium-ion-like transition state, exploited
by transition-state-analogue inhibitors such as immucillin-H (PMID 11444965).
PpnP performs the same net chemistry but from a completely different scaffold: a
rigid Cupin-fold dimer with a hydrophobic nucleoside pocket (PMID 35094440).

**Tier 2 — phosphoribosyl transfer (base → nucleotide).** The general reaction is:

> purine base + PRPP → purine-5′-monophosphate + PPi

This step is effectively **irreversible** under physiological conditions because
PPi is hydrolyzed by inorganic pyrophosphatase, pulling flux toward nucleotide.
The chemistry is an **in-line SN1-like nucleophilic substitution** at the ribose
C1′: the purine N9 attacks the anomeric carbon of PRPP with inversion of
configuration (α→β), displacing PPi. Two **Mg²⁺ ions** orient and electrostatically
activate the PRPP diphosphate for departure; a mobile **catalytic loop** closes
over the active site as the penultimate step, sequestering the reaction from
solvent (Toxoplasma HGPRT ternary complex, PMID 10545171; PfHGXPRT loop III′,
PMID 27479359). Base specificity is imposed by the **C-terminal "hood"** that
caps the type I PRTase core (PMID 12037295).

**Sequence, obligation, and accessory steps.**

- *Obligatory* for base salvage: at least one Tier-1 phosphorylase (or a nucleoside
  kinase bypass) to generate the free base, plus the matching Tier-2 PRTase.
- *Conditional*: Tier 1 is only required when the substrate arrives as a
  *nucleoside*; free bases enter Tier 2 directly. Conversely, if a nucleoside
  kinase is present, the base need never be generated at all.
- *Accessory*: transporters, ribose-1-phosphate salvage, and the interconversion
  enzymes that decide whether hypoxanthine-derived IMP becomes AMP or GMP.

A key ordering constraint: **a base cannot be phosphoribosylated until it is
free**, so for nucleoside substrates phosphorolysis strictly precedes PRT.
Because PRPP is the shared donor for both salvage and de novo synthesis, the two
pathways compete for it, and PRPP availability gates Tier-2 flux.

---

## 4. Major molecular players and active assemblies

### 4.1 Tier 1 — nucleoside phosphorylases (three unrelated families)

| Family | Representative(s) | Fold / assembly | Notes |
|---|---|---|---|
| **NP-I** | DeoD (PNP) | Trimeric or hexameric α/β | *E. coli* DeoD is **hexameric**; *M. tuberculosis* DeoD is **trimeric**, like mammalian PNP (PMID 11444965, 17639373, 11437593). Broad on Ino/Guo/adenosine. |
| **NP-II** | XapA (xanthosine PNP), Pdp (pyrimidine-nucleoside PNP) | Dimeric | XapA acts on xanthosine; substrate delivered by XapB permease (PMID 11466294). |
| **Cupin / PpnP** | PpnP | RlmC-like Cupin **dimer** | Broad pyrimidine+purine specificity; conserved dimer/pocket residues across bacteria (PMID 35094440). |

The existence of three convergent folds discharging the same activity is the
central surprise of Tier 1 and the reason the module is robust to loss of any one
phosphorylase in many species.

### 4.2 Tier 2 — purine phosphoribosyltransferases (one ancestral fold, four specificities)

All are **type I PRTases**: a central five-stranded parallel β-sheet flanked by
α-helices, carrying the conserved ~13-residue **PRPP-binding motif** and a
variable **C-terminal hood** for the base (PMID 12037295, 9016724). They act as
homodimers/tetramers with two Mg²⁺ per active site.

| Enzyme (gene) | Base(s) | Product(s) | Notes |
|---|---|---|---|
| **Apt** (adenine PRTase) | adenine | AMP | Constitutive in *E. coli*; bacterial APRT structure and ligand-induced closure characterized in *Fusobacterium nucleatum* (PMID 41588988). Can also condense PRPP with the de novo intermediate AICA (PMID 9742728). |
| **HGPRT/Hpt** (*hpt*) | hypoxanthine, guanine | IMP, GMP | The double-specificity purine PRTase; in many organisms extends to xanthine (HG*X*PRT), e.g., *P. falciparum* (PMID 27479359). |
| **Xpt** (*xpt*) | xanthine | XMP | Dedicated xanthine PRTase in *B. subtilis*, in the *xpt-pbuX* operon (PMID 9098051). |
| **Gpt** (*gpt*, enterobacteria) | xanthine, guanine (± hypoxanthine) | XMP, GMP | Broader-specificity enterobacterial enzyme; distinct locus from *hpt* (PMID 765747). |

### 4.3 Accessory transporters and disposal

NupC/NupG import nucleosides (PMID 30341391); XapB imports xanthosine
(PMID 11466294); base-specific permeases (PbuX for xanthine in *B. subtilis*,
PMID 9098051; NCS2/NCS1 families broadly) import free bases. R1P is routed by
phosphopentomutase/Deo enzymes into central metabolism.

---

## 5. Evolutionary and cell-biological variation

**Deep origin.** The Tier-2 PRTases are **monophyletic**: adenine-, hypoxanthine-,
guanine- and xanthine-PRTases are homologous to one another *and* to the
nucleoside phosphorylases, and were assembled by gene duplication before the
Bacteria/Archaea/Eukarya split (PMID 9742728). Substrate specialization is
therefore a *derived* property layered onto a promiscuous ancestral PRPP-condensing
enzyme; because APRT still condenses PRPP with AICA, **adenine PRTase is arguably
the best living proxy for the ancestral role** (PMID 9742728). By contrast, the
**Cupin-fold PpnP is a later, convergent invention** for Tier-1 chemistry
(PMID 35094440), and the split of the classical PNPs into hexameric vs trimeric
forms is a **lineage-specific quaternary-structure elaboration** (PMID 11444965).

**Lineage differences in the enzyme roster.**
- *Enterobacteria (E. coli/Salmonella):* Hpt (hypoxanthine/guanine) + Gpt
  (guanine/xanthine) + Apt; DeoD (hexamer) + XapA + PpnP for Tier 1; nucleoside
  kinase Gsk present (PMID 765747, 26443734).
- *Firmicutes (B. subtilis):* dedicated Xpt with its own permease PbuX in a
  purine-repressed operon, i.e., xanthine salvage is a *separately regulated,
  import-coupled* branch (PMID 9098051).
- *Actinobacteria (M. tuberculosis):* trimeric DeoD PNP and a characterized HGPRT
  (PMID 11444965, 19362594); salvage enzymes are studied as drug targets.

**Alternative routes to the same outcome.**
- **Nucleoside kinase bypass:** Gsk phosphorylates guanosine/inosine directly to
  GMP/IMP, and adenosine kinases (where present) make AMP, *without* liberating a
  base — a parallel solution that skips the PRTase tier entirely (PMID 765747).
- **Deamination re-routing:** adenosine deaminase (Add) converts adenosine→inosine
  and adenine deaminase converts adenine→hypoxanthine, shunting adenine-derived
  material into the HGPRT branch rather than Apt (PMID 765747).
- **Redundant phosphorylases:** DeoD, XapA and PpnP overlap on several nucleosides,
  so no single Tier-1 enzyme is universally essential (PMID 35094440, 11466294).

**No true compartments.** Because bacteria lack organelles, the entire module is
cytoplasmic; "compartmentalization" is achieved kinetically (active-site loop
closure, metabolite channeling to pyrophosphatase) rather than by membranes.
Physiological-state variation (starvation, nitrogen limitation) alters *expression*
(e.g., xanthine dehydrogenase induction and *xpt-pbuX* repression respond to
purine and nitrogen status; PMID 9098051) far more than it alters the enzymes.

---

## 6. Constraints, dependencies, and failure modes

**Ordering constraints.**
- For nucleoside substrates, **phosphorolysis must precede phosphoribosyl
  transfer** — a base cannot be salvaged until it is free.
- **PRPP must be available** for Tier 2; PRPP is co-required by de novo synthesis,
  pyrimidine salvage, NAD/histidine/tryptophan pathways, so Tier 2 is embedded in
  a competitive economy for this single activated sugar.
- **PPi hydrolysis** makes Tier 2 effectively irreversible and provides the
  thermodynamic pull that orients the whole module toward nucleotide formation.

**Substrate-specificity constraints.**
- Apt cannot rescue *hpt/gpt* loss and vice versa: the hood dictates which base
  enters which nucleotide, so specificity failures create metabolically distinct
  phenotypes (adenine vs hypoxanthine/guanine/xanthine auxotrophy-like defects).
- Whether hypoxanthine-derived **IMP** becomes **AMP** or **GMP** is decided
  *downstream* by the interconversion enzymes, not by salvage itself.

**Regulatory integration and feedback.**
- The salvage **products themselves are signals**: hypoxanthine and guanine are the
  physiological **corepressors of PurR**, the master repressor of the *pur* regulon
  (holorepressor–*purF* operator Kd ≈ 3.4 nM; aporepressor binds guanine at 1.7 µM,
  hypoxanthine at 7.1 µM) (PMID 2211500, 2089227, 1490614). When salvage supplies
  ample bases, de novo synthesis is shut off — a clean example of pathway-level
  economy.
- In Firmicutes, the same bases act largely through **cis-acting purine
  riboswitches** and dedicated transcription factors rather than a PurR-type
  protein repressor. The *xpt-pbuX* operon is repressed up to 160-fold by
  hypoxanthine+guanine (PMID 9098051); a guanine-sensing riboswitch (e.g., the
  *B. subtilis yxjA* purine riboswitch) downregulates a nucleoside transporter by
  cotranscriptional RNA strand exchange that favors a transcriptional terminator
  (PMID 35348734); and dedicated regulators such as NupR govern nucleoside
  permease expression (PMID 35862946). The regulatory *outcome* (throttle uptake
  and salvage when purines are abundant) is conserved, but the *mechanism* differs
  from enterobacterial PurR — a caution against generalizing salvage regulation
  from *E. coli* to all bacteria.

**Failure modes and their exploitation.**
- Loss of HGPRT/PNP salvage sensitizes or desensitizes cells to **purine-analogue
  prodrugs** (6-mercaptopurine, 6-thioguanine), which must be salvaged to become
  toxic nucleotides; these analogues also activate PurR (PMID 2089227). This is the
  basis of *gpt/hpt*-based positive/negative genetic selections (PMID 1761220).
- In pathogens (*M. tuberculosis*, apicomplexan parasites) the salvage enzymes are
  pursued as **drug targets**, exploiting transition-state analogues (immucillins)
  and species-specific active-site features (PMID 11444965, 19362594, 27479359).

**What is ruled out.** The chemistry forbids certain "shortcuts": a PRTase cannot
act on an intact nucleoside (no free N9), and a phosphorylase cannot on its own
produce a nucleotide (it makes a base + R1P, not an NMP). Thus any path from an
imported nucleoside to an NMP must either (i) go base→PRPP via a PRTase, or
(ii) be phosphorylated by a kinase; there is no single-enzyme phosphorolytic route
to a nucleotide.

---

## 7. Controversies and open questions

1. **Is PpnP a principal salvage phosphorylase or a specialist?** PpnP was defined
   biochemically and structurally only recently (PMID 35094440); its *quantitative*
   contribution to purine salvage relative to DeoD and XapA in vivo, and across
   species, is not well established. The brief's framing of PpnP as the module's
   phosphorylase is a simplification the field has not fully validated.

2. **Boundary between salvage and de novo.** Because APRT can condense PRPP with
   AICA (PMID 9742728), the historical line between "salvage" and "biosynthesis" is
   blurry at the level of enzyme capability. How often such promiscuous activities
   matter physiologically is unresolved.

3. **Generalization across organisms.** Much mechanistic detail (two-Mg²⁺ catalysis,
   loop closure, hood-based specificity) comes from *eukaryotic parasite* HGPRTs
   (Toxoplasma, Plasmodium; PMID 10545171, 27479359) and is *assumed* to transfer
   to bacterial enzymes. It very likely does, given the shared fold, but direct
   bacterial structural coverage — especially of Hpt, Xpt and Gpt with bound
   PRPP·Mg²⁺ and base — remains comparatively thin. Bacterial APRT structures are
   only now appearing (PMID 41588988).

4. **Quaternary-structure significance.** Why *E. coli* DeoD is hexameric while
   mycobacterial and mammalian PNPs are trimeric (PMID 11444965) — and whether this
   affects cooperativity, substrate range, or inhibitor design — is not fully
   explained.

5. **Redundancy and essentiality.** With three unrelated phosphorylase folds and a
   kinase bypass, which Tier-1 activities are genuinely essential under nutrient
   limitation, and how flux partitions among them, is largely inferred rather than
   measured by flux analysis.

6. **Transporter–enzyme coupling.** The degree to which base/nucleoside uptake is
   kinetically coupled to (or rate-limiting for) salvage — e.g., XapB→XapA→Gpt for
   xanthosine — is suggested by operon organization (PMID 9098051, 11466294) but not
   quantified in most systems.

**Overarching caution.** The salvage "module" is a useful abstraction, but its
enzyme roster, regulation, and even its dominant phosphorylase differ between
enterobacteria, Firmicutes and Actinobacteria. Claims should be anchored to the
organism in which they were demonstrated and not assumed universal.

---

## 8. Key references

- Jensen KF, Dandanell G, Hove-Jensen B, Willemoës M. **Nucleotides, Nucleosides,
  and Nucleobases.** *EcoSal Plus* (2008). PMID 26443734. — Authoritative review of
  *E. coli*/*Salmonella* nucleotide metabolism, including salvage and transport.
- Becerra A, Lazcano A. **The role of gene duplication in the evolution of purine
  nucleotide salvage pathways.** *Orig Life Evol Biosph* (1998). PMID 9742728. —
  Monophyly of purine PRTases and their homology to phosphorylases; pre-LUCA-era
  assembly by patchwork.
- Wen L, et al. **Crystal structures of a new class of pyrimidine/purine nucleoside
  phosphorylase revealed a Cupin fold.** (2022). PMID 35094440. — Structural
  definition of PpnP as a distinct NP class.
- Basso LA, et al. **Purine nucleoside phosphorylase from *M. tuberculosis*…**
  (2001). PMID 11444965. — Trimeric vs hexameric DeoD; transition-state inhibition.
- Modrak-Wójcik A, et al. **Ionization of the phosphate cosubstrate on
  phosphorolysis by PNP (E. coli and human).** (2008). PMID 17639373. — *deoD*
  PNP-I kinetics/cooperativity.
- Kadziola A, Neuhard J, Larsen S. **Product-bound *B. caldolyticus* UPRTase…**
  (2002). PMID 12037295. — Type I PRTase fold, PRPP motif, C-terminal hood.
- Héroux A, et al. **Toxoplasma HGPRT ternary complex with XMP·PPi·2 Mg²⁺.**
  (1999). PMID 10545171. — Two-Mg²⁺ activation mechanism of purine PRTases.
- Roy S, et al. **W181 and loop III′ in *P. falciparum* HGXPRT.** (2016).
  PMID 27479359. — Catalytic-loop closure and base specificity.
- Kim et al. **Ligand-induced conformational changes in APRT from *Fusobacterium
  nucleatum*.** (2025). PMID 41588988. — Bacterial adenine PRTase structure.
- Christiansen LC, et al. **Xanthine metabolism in *B. subtilis*: *xpt-pbuX*
  operon.** (1997). PMID 9098051. — Dedicated Xpt + xanthine permease; purine/
  nitrogen-controlled regulation.
- Jochimsen B, Nygaard P, Vestergaard T. **Location of *add*, *gsk*, *hpt*.**
  (1975). PMID 765747. — Genetic separability of salvage/deaminase/kinase loci.
- Rolfes RJ, Zalkin H. **Purification of the *E. coli* pur repressor and
  corepressors.** (1990). PMID 2211500; Meng LM, Nygaard P (1990) PMID 2089227;
  Steiert JG, et al. (1992) PMID 1490614. — Hypoxanthine/guanine as PurR
  corepressors.
- Nørholm MHH, Dandanell G. **Specificity and topology of the *E. coli*
  xanthosine permease XapB.** (2001). PMID 11466294. — Substrate delivery to XapA.
- Almagro G, et al. **NupC/NupG nucleoside transporters.** (2018). PMID 30341391.
- Cheng L, et al. **Cotranscriptional RNA strand exchange underlies the gene
  regulation mechanism in a purine-sensing transcriptional riboswitch.** (2022).
  PMID 35348734. — *B. subtilis yxjA* guanine riboswitch controlling nucleoside
  transport.
- Qin Y, et al. **NupR is a nucleoside permease regulator in *Bacillus
  thuringiensis*.** (2022). PMID 35862946. — Protein-level control of nucleoside
  uptake in a Firmicute.

---

*Uncertainty statement:* Structural/mechanistic detail is strongest for the type I
PRTase chemistry (well supported across multiple organisms) and for the PpnP fold;
it is weakest for direct bacterial Hpt/Xpt/Gpt structures with full substrate
complements and for in vivo flux partitioning among redundant Tier-1 enzymes.
Where findings derive from eukaryotic parasites or from a single species, this is
stated in-text and should not be generalized to all bacteria.


## Artifacts

- [OpenScientist final report](bacterial_purine_salvage-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_purine_salvage-deep-research-openscientist_artifacts/final_report.pdf)