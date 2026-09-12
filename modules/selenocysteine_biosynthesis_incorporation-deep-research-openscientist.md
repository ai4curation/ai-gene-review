---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:30:38.950528'
end_time: '2026-09-01T10:57:17.596905'
duration_seconds: 1598.65
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial and eukaryotic selenocysteine biosynthesis and co-translational
    incorporation
  module_summary: A reusable module for the bacterial and eukaryotic synthesis of
    selenocysteyl-tRNA(Sec) and recoding of UGA as selenocysteine. Selenophosphate
    synthetase activates selenium, and seryl-tRNA synthetase charges tRNA(Sec) with
    serine. Bacteria convert Ser-tRNA(Sec) directly with SelA, whereas the represented
    eukaryotic route first phosphorylates it with PSTK and then uses SepSecS. The
    completed Sec-tRNA(Sec) is delivered by a lineage-specific elongation system to
    a UGA codon in a SECIS-dependent translation context.
  module_outline: "- Bacterial and eukaryotic selenocysteine biosynthesis and incorporation\n\
    \  - 1. activated selenium donor production\n  - Selenophosphate synthesis\n \
    \   - SelD/SEPHS2 selenide, water dikinase activity (molecular player: selenophosphate\
    \ synthetase family; activity or role: selenide, water dikinase activity)\n  -\
    \ 2. tRNA(Sec) aminoacylation with serine\n  - Ser-tRNA(Sec) synthesis\n    -\
    \ SerS/SARS serine-tRNA ligase activity on tRNA(Sec) (molecular player: seryl-tRNA\
    \ synthetase family; activity or role: serine-tRNA ligase activity)\n  - 3. conversion\
    \ of Ser-tRNA(Sec) to Sec-tRNA(Sec)\n  - Alternative Sec-tRNA(Sec) synthesis routes\n\
    \    - Alternative versions by taxonomic implementation: Ser-tRNA(Sec) conversion\
    \ route\n      - Bacterial SelA route\n        - SelA L-seryl-tRNA(Sec) selenium\
    \ transferase activity (molecular player: bacterial SelA family; activity or role:\
    \ L-seryl-tRNA(Sec) selenium transferase activity)\n      - Eukaryotic PSTK-SepSecS\
    \ route\n        - 1. Ser-tRNA(Sec) phosphorylation\n        - PSTK-dependent\
    \ phosphoseryl-tRNA(Sec) formation\n          - PSTK L-seryl-tRNA(Sec) kinase\
    \ activity (molecular player: PSTK family; activity or role: L-seryl-tRNA(Sec)\
    \ kinase activity)\n        - 2. phosphoseryl-tRNA(Sec) selenium transfer\n  \
    \      - SepSecS-dependent Sec-tRNA(Sec) formation\n          - SepSecS phosphoseryl-tRNA(Sec)\
    \ selenium transferase activity (molecular player: SepSecS family; activity or\
    \ role: O-phosphoseryl-tRNA(Sec) selenium transferase activity)\n  - 4. SECIS-dependent\
    \ UGA recoding and Sec-tRNA delivery\n  - Alternative selenocysteine insertion\
    \ systems\n    - Alternative versions by taxonomic implementation: Selenocysteine-specific\
    \ translation machinery\n      - Bacterial SelB insertion system\n        - SelB\
    \ bacterial SECIS-binding activity (molecular player: SelB elongation-factor family;\
    \ activity or role: selenocysteine insertion sequence binding)\n        - SelB\
    \ selenocysteine-specific elongation factor activity (molecular player: SelB elongation-factor\
    \ family; activity or role: translation elongation factor activity)\n      - Eukaryotic\
    \ SECISBP2-EEFSEC insertion system\n        - 1. SECIS-element recognition\n \
    \       - SECISBP2-dependent SECIS recognition\n          - SECISBP2 SECIS-binding\
    \ activity (molecular player: SECISBP2 family; activity or role: selenocysteine\
    \ insertion sequence binding)\n        - 2. Sec-tRNA(Sec) delivery\n        -\
    \ EEFSEC-dependent Sec-tRNA(Sec) delivery\n          - EEFSEC translation elongation\
    \ factor activity (molecular player: selenocysteine-specific elongation-factor\
    \ family; activity or role: translation elongation factor activity)"
  module_connections: '- Selenophosphate synthesis feeds into Alternative Sec-tRNA(Sec)
    synthesis routes: Selenophosphate supplies selenium to either Sec-tRNA synthesis
    route.

    - Ser-tRNA(Sec) synthesis feeds into Alternative Sec-tRNA(Sec) synthesis routes:
    SerS supplies Ser-tRNA(Sec) to either conversion route.

    - Alternative Sec-tRNA(Sec) synthesis routes feeds into Alternative selenocysteine
    insertion systems: Completed Sec-tRNA(Sec) is the substrate delivered during UGA
    recoding.

    - PSTK-dependent phosphoseryl-tRNA(Sec) formation feeds into SepSecS-dependent
    Sec-tRNA(Sec) formation: PSTK produces the phosphoseryl-tRNA consumed by SepSecS.

    - SECISBP2-dependent SECIS recognition feeds into EEFSEC-dependent Sec-tRNA(Sec)
    delivery: SECISBP2-dependent mRNP assembly supplies the recoding context used
    during EEFSEC delivery.'
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
  path: selenocysteine_biosynthesis_incorporation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: selenocysteine_biosynthesis_incorporation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial and eukaryotic selenocysteine biosynthesis and co-translational incorporation

## Working Scope

A reusable module for the bacterial and eukaryotic synthesis of selenocysteyl-tRNA(Sec) and recoding of UGA as selenocysteine. Selenophosphate synthetase activates selenium, and seryl-tRNA synthetase charges tRNA(Sec) with serine. Bacteria convert Ser-tRNA(Sec) directly with SelA, whereas the represented eukaryotic route first phosphorylates it with PSTK and then uses SepSecS. The completed Sec-tRNA(Sec) is delivered by a lineage-specific elongation system to a UGA codon in a SECIS-dependent translation context.

## Provisional Biological Outline

- Bacterial and eukaryotic selenocysteine biosynthesis and incorporation
  - 1. activated selenium donor production
  - Selenophosphate synthesis
    - SelD/SEPHS2 selenide, water dikinase activity (molecular player: selenophosphate synthetase family; activity or role: selenide, water dikinase activity)
  - 2. tRNA(Sec) aminoacylation with serine
  - Ser-tRNA(Sec) synthesis
    - SerS/SARS serine-tRNA ligase activity on tRNA(Sec) (molecular player: seryl-tRNA synthetase family; activity or role: serine-tRNA ligase activity)
  - 3. conversion of Ser-tRNA(Sec) to Sec-tRNA(Sec)
  - Alternative Sec-tRNA(Sec) synthesis routes
    - Alternative versions by taxonomic implementation: Ser-tRNA(Sec) conversion route
      - Bacterial SelA route
        - SelA L-seryl-tRNA(Sec) selenium transferase activity (molecular player: bacterial SelA family; activity or role: L-seryl-tRNA(Sec) selenium transferase activity)
      - Eukaryotic PSTK-SepSecS route
        - 1. Ser-tRNA(Sec) phosphorylation
        - PSTK-dependent phosphoseryl-tRNA(Sec) formation
          - PSTK L-seryl-tRNA(Sec) kinase activity (molecular player: PSTK family; activity or role: L-seryl-tRNA(Sec) kinase activity)
        - 2. phosphoseryl-tRNA(Sec) selenium transfer
        - SepSecS-dependent Sec-tRNA(Sec) formation
          - SepSecS phosphoseryl-tRNA(Sec) selenium transferase activity (molecular player: SepSecS family; activity or role: O-phosphoseryl-tRNA(Sec) selenium transferase activity)
  - 4. SECIS-dependent UGA recoding and Sec-tRNA delivery
  - Alternative selenocysteine insertion systems
    - Alternative versions by taxonomic implementation: Selenocysteine-specific translation machinery
      - Bacterial SelB insertion system
        - SelB bacterial SECIS-binding activity (molecular player: SelB elongation-factor family; activity or role: selenocysteine insertion sequence binding)
        - SelB selenocysteine-specific elongation factor activity (molecular player: SelB elongation-factor family; activity or role: translation elongation factor activity)
      - Eukaryotic SECISBP2-EEFSEC insertion system
        - 1. SECIS-element recognition
        - SECISBP2-dependent SECIS recognition
          - SECISBP2 SECIS-binding activity (molecular player: SECISBP2 family; activity or role: selenocysteine insertion sequence binding)
        - 2. Sec-tRNA(Sec) delivery
        - EEFSEC-dependent Sec-tRNA(Sec) delivery
          - EEFSEC translation elongation factor activity (molecular player: selenocysteine-specific elongation-factor family; activity or role: translation elongation factor activity)

## Known Relationships Among Steps

- Selenophosphate synthesis feeds into Alternative Sec-tRNA(Sec) synthesis routes: Selenophosphate supplies selenium to either Sec-tRNA synthesis route.
- Ser-tRNA(Sec) synthesis feeds into Alternative Sec-tRNA(Sec) synthesis routes: SerS supplies Ser-tRNA(Sec) to either conversion route.
- Alternative Sec-tRNA(Sec) synthesis routes feeds into Alternative selenocysteine insertion systems: Completed Sec-tRNA(Sec) is the substrate delivered during UGA recoding.
- PSTK-dependent phosphoseryl-tRNA(Sec) formation feeds into SepSecS-dependent Sec-tRNA(Sec) formation: PSTK produces the phosphoseryl-tRNA consumed by SepSecS.
- SECISBP2-dependent SECIS recognition feeds into EEFSEC-dependent Sec-tRNA(Sec) delivery: SECISBP2-dependent mRNP assembly supplies the recoding context used during EEFSEC delivery.

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

# Selenocysteyl-tRNA(Sec) Biosynthesis and Co-translational UGA Recoding: A System-Level Review

*Commissioned review synthesis — bacterial and eukaryotic selenocysteine biosynthesis and incorporation. Prepared for a molecular-biology audience. Search date: 2026-09-01 (PubMed).*

---

## 1. Executive summary

Selenocysteine (Sec) is the 21st proteinogenic amino acid. Unlike the other twenty, it has no free-standing pool and no dedicated aminoacyl-tRNA synthetase: it is **built on its own tRNA (tRNA^Sec, gene *selC*)** and then **inserted co-translationally in response to an in-frame UGA codon** that is normally a stop signal. The system therefore couples an unusual anabolic pathway (tRNA-templated amino-acid synthesis) to an unusual decoding event (context-dependent stop-codon reassignment).

The pathway can be read as **four functional modules that operate in an obligatory order**:

1. **Selenium activation** — selenophosphate synthetase (SelD in bacteria; SEPHS2 in eukaryotes) makes **selenophosphate**, the sole biological selenium donor for Sec.
2. **tRNA^Sec charging with serine** — seryl-tRNA synthetase (SerS/SARS) misacylates tRNA^Sec with serine to give **Ser-tRNA^Sec**.
3. **Ser→Sec conversion** — achieved by **two mechanistically and evolutionarily independent routes**: the **bacterial one-step SelA** route, and the **archaeal/eukaryotic two-step PSTK→SepSecS** route that passes obligately through a phosphoseryl (Sep) intermediate.
4. **UGA recoding and delivery** — a **lineage-specific elongation machinery** decodes UGA as Sec: bacterial **SelB** (a single protein that binds both the SECIS element and Sec-tRNA^Sec), versus the eukaryotic split system of **SECISBP2 (SBP2)** + **EEFSEC (eEFSec)**, in which the SECIS element has migrated to the 3′ UTR.

The **backbone (modules 1, 2, and the general logic of module 4) is deeply conserved and ancient**, present in all three domains of life and subject to extensive horizontal transfer and lineage-specific loss. The **major variation lies in module 3** (SelA vs. PSTK/SepSecS) and in the **architecture of module 4** (one protein vs. an mRNP adaptor + dedicated EF-Tu paralog). The strongest experimental support comes from bacterial (*E. coli*, *Aquifex aeolicus*), archaeal (*Methanococcus*), and mammalian/trypanosomatid systems; the biggest open questions concern the exact hand-offs between enzymes (channeling vs. diffusion), the composition and stoichiometry of the eukaryotic recoding mRNP at the ribosome, and how selenium status quantitatively tunes recoding efficiency.

---

## 2. Definition and biological boundaries

### 2.1 What is inside the system

The system comprises everything required to convert inorganic selenium plus a serine-charged special tRNA into a **Sec residue at a defined UGA codon**:

- **tRNA^Sec (*selC*)** — the physical scaffold on which Sec is synthesized and the adaptor that reads UGA. It has a distinctive long acceptor/T-arm (8/5 bp in bacteria; 9/4 in archaea/eukaryotes), an extended variable arm, and non-canonical features that make it the identity determinant for every enzyme in the pathway.
- **Selenophosphate synthetase** (SelD / SEPHS2) — activates selenide to selenophosphate.
- **Seryl-tRNA synthetase** (SerS/SARS) — the *only* enzyme in the pathway not unique to Sec; it charges both tRNA^Ser and tRNA^Sec with serine.
- **Ser→Sec converting enzyme(s)** — SelA (bacteria); PSTK + SepSecS (archaea/eukaryotes).
- **Sec-specific decoding machinery** — SelB (bacteria); SBP2 + EEFSEC (eukaryotes), plus the **SECIS element** *cis*-signal in the mRNA.

### 2.2 What is adjacent but should be treated separately

- **Selenium uptake, transport, and storage** (e.g., SELENOP as a plasma Se carrier; selenosugars; dietary selenoamino acids). These set the substrate supply but are not part of the Sec-synthesis/insertion chemistry.
- **Selenocysteine lyase (SCLY)** and the **salvage/recycling** of Se from degraded selenoproteins. This is catabolic, not part of Sec synthesis, though it feeds selenide back to SelD/SEPHS2.
- **2-Selenouridine (tRNA wobble) synthesis by YbbB/SelU** — a *different* selenium-utilization trait that also consumes selenophosphate. Because **selD is shared** between the Sec trait and the 2-selenouridine trait, the presence of selenophosphate synthetase alone does *not* imply a Sec pathway [PMID 16086848].
- **The selenoproteins themselves** (GPX, TXNRD, DIO, SELENOP, MsrB1, etc.) and their downstream redox/thyroid/antioxidant biology. These are the *products*, not the machinery.
- **SEPHS1** — a selenophosphate-synthetase *paralog* in animals that does **not** efficiently make selenophosphate and has a distinct, still-debated role (redox/regulatory; implicated in neurodevelopment). It is easily confused with the catalytic SEPHS2 but is mechanistically separate [PMID 38960024].
- **Canonical translation termination / other stop-codon readthrough** (near-cognate suppression, ribosomal frameshifting). Sec insertion is a *programmed* recoding event and should not be lumped with stochastic readthrough.

### 2.3 Competing definitions

Two framing choices recur in the literature:
- **"Sec biosynthesis" (on the tRNA)** vs. **"Sec incorporation/recoding" (at the ribosome).** Some reviews treat these as one pathway; others separate anabolism (modules 1–3) from decoding (module 4). This review treats them as one integrated system but keeps the modules explicit.
- **Whether the SECIS + trans-factors constitute part of the "code" or part of "regulated gene expression."** In eukaryotes, SECIS-driven recoding is strongly modulated by Se status, cofactors, and mRNP assembly, so the boundary between "decoding machinery" and "translational regulation" is genuinely fuzzy [PMID 39988117, 28115638].

---

## 3. Mechanistic overview

### 3.1 Best current model (sequence of events)

**Step 1 — Selenium activation (obligatory, shared).**
Selenide (HSe⁻) + ATP → **selenophosphate** + AMP + Pᵢ, catalyzed by **SelD/SEPHS2** (selenide, water dikinase). Crystallographic and kinetic work on *E. coli* SPS shows a **Mg²⁺/K⁺-dependent homodimer** with a mobile **glycine-rich N-terminal loop** and a cluster of catalytic aspartates (D51/D68/D91/D227, with N87) whose mutation abolishes AMP production; the reaction runs in **two steps** — ATP → ADP + γ-phosphate, then transfer of the γ-phosphate to selenide to make selenophosphate while ADP is hydrolyzed to AMP + Pᵢ [PMID 22081394, 29715549]. Selenophosphate is the only known in-vivo Se donor for Sec, is chemically **labile and its selenide precursor is toxic**, arguing for tight coupling to both upstream supply and downstream use: in bacteria, **SelD binds selenocysteine lyase (CsdB) at ~1.8 nM (1:1)** to sequester the selenide released during Se recycling, evidence that the entry point is a controlled hand-off rather than free diffusion [PMID 32275991]. Only the catalytic **SEPHS2** (bearing an active-site Sec/Cys) makes selenophosphate in eukaryotes; the **SEPHS1** paralog lacks this activity [PMID 29715549].

**Step 2 — Serylation (obligatory, shared).**
**SerS/SARS** charges tRNA^Sec with L-serine → **Ser-tRNA^Sec**. tRNA^Sec is a poor EF-Tu/eEF1A substrate and is not used in general translation; this "misacylation" is the committed entry into the pathway.

**Step 3 — Ser→Sec conversion (obligatory; route is lineage-specific).**

- **Bacterial (one step):** **SelA** (selenocysteine synthase), a **pyridoxal-5′-phosphate (PLP)-dependent fold-type-I enzyme**, forms a Schiff base with the seryl moiety, eliminates water to a dehydroalanyl-tRNA intermediate, and adds selenium from selenophosphate → **Sec-tRNA^Sec**. Structurally, SelA is a **homodecamer (≈500 kDa) that binds 10 tRNA^Sec**, each tRNA contacting four subunits; **decamerization is required for a competent active site** [PMID 23559248, 24456689].
- **Archaeal/eukaryotic (two steps):**
  (a) **PSTK** (O-phosphoseryl-tRNA^Sec kinase) phosphorylates the seryl hydroxyl → **Sep-tRNA^Sec** (ATP-dependent).
  (b) **SepSecS** (Sep-tRNA:Sec-tRNA synthase / SLA/LP antigen), a **PLP-dependent tetramer**, converts Sep-tRNA^Sec to **Sec-tRNA^Sec** using selenophosphate [PMID 21564332, 19279205].

**Step 4 — UGA recoding and delivery (obligatory; architecture is lineage-specific).**

- **Bacteria:** the **SECIS element lies immediately 3′ of the UGA within the ORF**. **SelB**, an EF-Tu-like GTPase with a C-terminal extension, simultaneously (i) binds the SECIS hairpin and (ii) delivers **Sec-tRNA^Sec•GTP** to the ribosomal A site at that UGA [PMID 16086848, 26160755].
- **Eukaryotes/archaea:** the **SECIS element is in the 3′ UTR**, physically far from the UGA. The bacterial SelB functions are **split**: **SBP2/SECISBP2** binds the SECIS and organizes a recoding mRNP, while the dedicated elongation factor **EEFSEC (eEFSec)** binds Sec-tRNA^Sec and delivers it to the ribosome. eEFSec adopts a chalice-like architecture (three EF-Tu-like N-terminal domains + a C-terminal domain 4 that grips Sec-tRNA^Sec) and is proposed to use a **non-canonical mechanism** distinct from eEF1A/EF-Tu: guanine-nucleotide exchange does **not** produce the large domain-1 rearrangement seen in EF-Tu but instead **swings domain 4**, which is thought to control Sec-tRNA^Sec release during decoding [PMID 27708257, 29555379, 39988117].

**A shared non-canonical decoding chassis.** Both SelB and eEFSec are **translational GTPases built on an EF-Tu-like core plus an extra C-terminal tRNA-binding domain**, and both recode UGA rather than terminate. On the bacterial ribosome, single-molecule/cryo-EM and kinetic studies have mapped a **distinct pathway to GTPase activation for SelB** during UGA decoding, and ribosome-dynamics work directly contrasts EF-Tu- and SelB-mediated aa-tRNA selection [PMID 27842381, 28138068]. This reuse of the ancestral GTPase chassis, elaborated with a dedicated domain to grip the reactive Sec-tRNA^Sec and to gate insertion to the correct SECIS context, is a recurring theme of the delivery step across domains.

### 3.2 Obligatory vs. conditional vs. accessory

- **Obligatory (core):** SelD/SEPHS2 → SerS → (SelA *or* PSTK+SepSecS) → (SelB *or* SBP2+EEFSEC) + tRNA^Sec + SECIS. Genetic ablation of any core node abolishes Sec formation: in *Methanococcus maripaludis*, deleting *selD*, *pstk*, or *sepsecs* individually eliminates Sec [PMID 21564332]; in *Trypanosoma brucei*, PSTK, SepSecS, SerRS, SPS (SelD), and eEFSec are each essential for selenoprotein synthesis [PMID 19279205].
- **Conditional / regulatory (eukaryote-specific):** SBP2 cofactor interactions, **SMN complex + methylosome-dependent mRNP assembly** and cap hypermethylation (Tgs1), and tRNA^Sec anticodon-loop modifications (see §3.3) tune *efficiency* and Se-responsiveness rather than acting as absolute on/off switches [PMID 28115638, 39988117].
- **Accessory / lineage-restricted:** SECp43, ribosomal protein L30, eIF4a3, nucleolin and other reported SECIS-mRNP partners; the salvage enzyme SCLY; SEPHS1's regulatory role. Trypanosomatids notably **lack SBP2 and SecP43** yet still recode UGA, showing these are not universally required in eukaryotes [PMID 24251578].

### 3.3 A conditional layer worth flagging

In eukaryotes, **anticodon-loop modifications of tRNA^Sec** (notably the two isoforms differing at position 34, mcm⁵U vs. mcm⁵Um) bias which selenoprotein mRNAs (the "housekeeping" vs. "stress-related" subsets) are efficiently recoded, providing a post-transcriptional dial on selenoproteome composition [PMID 39988117]. This is a genuine cell-physiological variable, not a fixed pathway step.

---

## 4. Major molecular players and active assemblies

| Module | Bacteria | Archaea/Eukaryotes | Active assembly / mechanism | Key evidence |
|---|---|---|---|---|
| Se activation | **SelD** | **SEPHS2** (catalytic); SEPHS1 = non-catalytic paralog | Mg²⁺/K⁺ homodimer; **two-step** ATP catalysis; Gly-rich loop + catalytic Asp cluster; couples to CsdB to sequester selenide | 22081394; 29715549; 32275991; 38960024 |
| tRNA^Sec charging | **SerS** | **SARS** | Class-II aaRS; serylates tRNA^Sec (shared with tRNA^Ser) | 19279205 |
| Ser→Sec | **SelA** (1 step) | **PSTK** then **SepSecS** (2 steps) | SelA: PLP, **homodecamer** binding 10 tRNA; SepSecS: PLP, **tetramer**, tRNA-activated | 23559248; 24456689; 36929010 |
| Sep intermediate | — | **PSTK** | ATP-dependent kinase; tRNA^Sec-dependent ATPase; structurally akin to Kti12 | 30916349 |
| UGA decoding *cis* | **SECIS in ORF** (3′ of UGA) | **SECIS in 3′ UTR** | mRNA hairpin; recruits trans-factors | 42080570 |
| UGA decoding *trans* | **SelB** (SECIS-binding **and** EF) | **SBP2** (SECIS-binding) + **EEFSEC** (EF) | SelB = EF-Tu-like GTPase, one protein does both jobs; eukaryotic functions split | 29555379; 26160755 |
| mRNP assembly (euk.) | — | **SBP2 + SMN complex + methylosome** (+ SECp43, L30…) | RNP chaperoning, cap hypermethylation; required for efficient GPx1 translation | 28115638 |

**Structural highlights.**
- **SelA decamer** (*A. aeolicus*): the ring is five dimers; the catalytic site sits at the dimer–dimer interface, and disrupting pentamerization distorts and inactivates it — a striking example of quaternary structure being *required* for catalysis [PMID 23559248, 24456689].
- **Human SEPSECS**: a tetramer with four equivalent active sites that nonetheless binds **only two tRNA^Sec** because a vertebrate-specific acidic **C-terminal α-helix (α16)** blocks two protomers; tRNA binding *organizes* the active site (substrate-induced competency), and disease mutations act largely by **destabilizing/misfolding** the enzyme, causing early-onset cerebellar/cerebral atrophy [PMID 36929010, 39385655, 27576344].
- **eEFSec / SelB**: chalice-like, EF-Tu-like N-terminal core plus a Sec-tRNA-clamping **domain 4**; in human eEFSec, nucleotide exchange swings domain 4 rather than domain 1, implying a non-canonical release/delivery mechanism; SelB follows a distinct GTPase-activation pathway on the bacterial ribosome [PMID 27708257, 27842381, 29555379].
- **Selenophosphate synthetase (SelD/SPS)**: Mg²⁺/K⁺-dependent homodimer whose glycine-rich N-terminal loop closes over ATP; catalytic aspartates (D51/D68/D91/D227) are essential, and in bacteria the enzyme physically partners CsdB to hand off/sequester toxic selenide [PMID 22081394, 32275991].

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across the domains of life

- **Deep conservation of the logic; divergence in the conversion enzyme.** All Sec-utilizing organisms share tRNA^Sec, selenophosphate synthetase, serylation, and a dedicated Sec-EF. The **branch point is module 3**: bacteria use **SelA**; archaea and eukaryotes use **PSTK + SepSecS**. Structural comparison of SelA and SepSecS (different folds, different catalytic residues, different substrate — Ser vs. Sep) supports **independent evolutionary origins** of the two conversion strategies [PMID 23559248].
- **The three-domain "core" is ancient.** Comparative genomics places the Sec-decoding trait early, with **extensive horizontal gene transfer and independent losses** producing a patchy, dynamic distribution [PMID 16086848]. Sec has been lost entirely in many lineages (e.g., higher plants, fungi, some nematodes and arthropods), often with **Sec→Cys substitution** in the orthologous selenoproteins [PMID 41212935].
- **SECIS relocation.** The migration of the SECIS from *within the ORF* (bacteria) to the *3′ UTR* (archaea/eukaryotes) is the single change that necessitated splitting SelB's dual role into SBP2 (mRNA-anchoring) + eEFSec (tRNA delivery), because one codon can no longer be adjacent to the *cis*-signal.

### 5.2 Best representatives for the ancestral role

- For the **terminal converting enzyme**, the **archaeal SepSecS ortholog** is the better proxy for the ancestral eukaryotic-type enzyme: it *lacks* the mammalian α16 helix and *requires* an aminoacyl (Sep) group to engage tRNA, whereas mammalian SEPSECS acquired the ability to bind unacylated tRNA plus asymmetric regulation — a **later vertebrate elaboration** [PMID 39385655].
- For **selenium activation**, **SEPHS2** (not the animal-specific SEPHS1 paralog) is the catalytically competent representative; SEPHS1 is a derived paralog with a divergent function [PMID 38960024].
- For the **decoding EF**, bacterial **SelB** best represents the ancestral single-protein logic (SECIS-binding + delivery fused), from which the eukaryotic split derived.

### 5.3 Cell-type, tissue, and physiological-state variation

- **Se-status sensitivity and a tissue-ranked hierarchy.** Recoding efficiency and the resulting selenoproteome depend strongly on selenium supply; under limitation, a reproducible **hierarchy** protects "essential" selenoproteins (e.g., GPX4, SELENOP, TXNRD) over "stress-responsive" ones (e.g., GPX1), partly via tRNA^Sec modification state and SECIS/SBP2 kinetics [PMID 39988117]. This hierarchy is **organ-specific**: rodent Se-deficiency/repletion studies show the **brain is preferentially protected** while **liver and plasma deplete first** (GPx1 and SEPHS2 fall earliest), and neonatal organs vary with the duration of maternal deficiency [PMID 37202582, 39546178, 33672905]. The **processing machinery itself is regulated** — SEPHS2, PSTK, SepSecS, and SCLY are coordinately downregulated in the liver during endotoxemia — so the pathway is an actively tuned output, not a constitutive one [PMID 33224150].
- **Tissue coupling to disease.** Loss of SepSecS activity is **especially deleterious to the CNS** (progressive cerebellar/cerebral atrophy), and SEPHS1 defects cause neurodevelopmental disorders — indicating heightened dependence of neural tissue on intact Sec synthesis [PMID 27576344, 38960024].
- **Inflammation/sepsis.** Endotoxemia downregulates the whole processing module (Sps2/SEPHS2, Pstk, SepSecS, Scly) in a **liver-specific** manner, showing the pathway is itself a regulated target of physiological state [PMID 33224150].
- **Compartment.** In canonical eukaryotic biology, Sec synthesis on tRNA^Sec and cytosolic selenoprotein translation are cytoplasmic; note the curious report of tRNA-Sec/SECIS machinery encoded in a **land-plant mitochondrial genome** (cranberry), a lineage otherwise thought to have lost Sec — a caution against assuming clean lineage-wide presence/absence [PMID 24342657].
- **Dispensability differs by organism.** Selenoproteins are **essential in mammals** but **dispensable for viability** in *T. brucei* and *Leishmania* under lab conditions, so knockouts of core enzymes are tolerated in these parasites [PMID 19279205, 26586914].

---

## 6. Constraints, dependencies, and failure modes

**Obligatory ordering (physical/chemical constraints):**
1. **Serylation must precede conversion** — SelA/SepSecS act on a tRNA-bound seryl/phosphoseryl moiety, not on free amino acid.
2. **In the eukaryotic route, phosphorylation must precede selenium transfer** — SepSecS uses **Sep**-tRNA^Sec, not Ser-tRNA^Sec; PSTK's product is SepSecS's obligate substrate. This is a strict linear dependency [PMID 21564332, 19279205].
3. **Selenophosphate must be available at the conversion step** — both SelA and SepSecS require it as the Se donor; hence **module 1 feeds module 3**, and Se limitation stalls conversion.
4. **Conversion must precede delivery** — only **Sec**-tRNA^Sec is a productive cargo; SelB/eEFSec bind the completed Sec-tRNA, not Ser- or Sep-tRNA.
5. **SECIS recognition sets the recoding context before/at delivery** — in eukaryotes, SBP2•SECIS mRNP assembly supplies the platform that licenses eEFSec-mediated insertion at the UGA [PMID 28115638].
6. **Selenide must be handed to SelD, not released free** — the selenide intermediate is cytotoxic, and its production (e.g., by CsdB during Se recycling) is kinetically coupled to its consumption by selenophosphate synthetase, constraining Step 1 to occur within a protected protein–protein interface rather than by bulk diffusion [PMID 32275991].

**Mutually exclusive / substrate-specific facts that rule out otherwise plausible paths:**
- **UGA is read as Sec only in a SECIS context;** absent a functional SECIS/trans-factors, the same UGA terminates translation. This *cis*-dependence prevents genome-wide misincorporation.
- **tRNA^Sec is excluded from canonical elongation** (poor EF-Tu/eEF1A substrate), so serine/Sep on tRNA^Sec cannot be mistakenly delivered to ordinary Ser codons — a safeguard, though engineered EF-Tu variants can override it [PMID 25064855, 26160755].
- **The bacterial and eukaryotic conversion enzymes are not interchangeable in vivo without their cognate accessory factors:** e.g., *Leishmania* SepSecS complements *E. coli* ΔselA **only when archaeal PSTK is also supplied**, because SepSecS needs the Sep intermediate that bacteria (SelA route) never make [PMID 26586914].
- A **rescue/failure mode:** under Se starvation, Sep-tRNA^Sec can be mis-converted toward **Cys-tRNA^Sec** (SepCysS-type chemistry in some organisms) or Sec formation simply fails, so the same intermediate can have alternative fates depending on Se supply [PMID 21564332].

**Failure modes with phenotypes:**
- **Destabilizing SEPSECS mutations** → misfolding/loss of activity → progressive early-onset neurodegeneration [PMID 27576344].
- **SEPHS2 loss** cripples the sole selenophosphate supply → global selenoprotein collapse; **SEPHS1** defects → neurodevelopmental disease via a distinct mechanism [PMID 38960024].
- **Environmental inhibition:** arsenite (As III) suppresses Sec-tRNA^Sec formation/selenite utilization via the SEPHS2 axis, linking a toxicant to a specific pathway node [PMID 42219356].

---

## 7. Controversies and open questions

1. **Channeling vs. free diffusion.** Are the labile intermediate (selenophosphate) and the charged tRNAs **substrate-channeled** through a physical super-complex, or do they diffuse? Co-IP/BRET data show **SEPHS1, SEPHS2, SEPSECS, and SECp43 oligomerize** in mammalian cells, hinting at a synthesis complex, but a defined, stoichiometric channeling assembly has not been proven [PMID 28414460].
2. **Composition and stoichiometry of the eukaryotic recoding mRNP at the ribosome.** SBP2 links to the **SMN complex and methylosome**, and many partners (SECp43, L30, eIF4a3, nucleolin) have been reported, but the minimal in-vivo machine and the order of assembly during a decoding cycle remain unsettled [PMID 28115638, 39988117].
3. **Do all eukaryotes need SBP2?** Trypanosomatids recode UGA **without SBP2 or SecP43**, so either an unidentified functional analog exists or the "canonical" mammalian model overgeneralizes [PMID 24251578]. This is a clear case where mixing organisms risks false universals.
4. **eEFSec mechanism.** The proposed **non-canonical, GTPase-coupled** delivery differs from eEF1A; the precise conformational cycle, the role of domain 4, and how SBP2 hands off to eEFSec are still being resolved [PMID 29555379].
5. **Regulatory logic of the selenoprotein hierarchy.** How tRNA^Sec **anticodon modifications**, SECIS variants, and SBP2 abundance quantitatively set the ranked protection of selenoproteins under Se limitation is incompletely mapped [PMID 39988117].
6. **Function of SEPHS1.** Whether the non-catalytic SEPHS1 paralog acts in Se recycling, redox signaling, or a moonlighting role is genuinely open, and it is frequently conflated with SEPHS2 in the literature [PMID 38960024].
7. **Evolutionary polarity of module 3.** SelA (bacteria) vs. SepSecS (archaea/eukaryotes) appear independently derived; which (if either) reflects the ancestral state of the earliest Sec-encoding organism, and how the Sep intermediate arose, remain debated [PMID 23559248, 39385655].

**Cautions on evidence.** Much bacterial mechanism rests on *E. coli* and *A. aeolicus*; much eukaryotic mechanism on mammalian cells, *Xenopus*, and trypanosomatids; archaeal mechanism largely on *Methanococcus* genetics and *M. jannaschii* biochemistry. Structural claims (SelA decamer, human SEPSECS asymmetry) are strong and crystallographically grounded, whereas mRNP-assembly and channeling models are more indirect (interaction assays, knockdowns). Presence/absence of the pathway should be inferred from **selB + selC (tRNA^Sec)**, not from selD alone [PMID 16086848].

---

## 8. Key references

1. **Itoh Y, Bröcker MJ, Sekine S, et al.** Decameric SelA•tRNA(Sec) ring structure reveals mechanism of bacterial selenocysteine formation. *Science* 2013. **PMID 23559248.** — Bacterial SelA decamer; evidence for independent evolution of the two conversion systems.
2. **Itoh Y, Bröcker MJ, Sekine S, Söll D, Yokoyama S.** Dimer-dimer interaction of SelA promotes active-site formation and specificity. *J Mol Biol* 2014. **PMID 24456689.** — Quaternary structure required for SelA catalysis.
3. **Hohn MJ, Palioura S, Su D, Yuan J, Söll D.** Genetic analysis of Sec biosynthesis in *Methanococcus maripaludis*. 2011. **PMID 21564332.** — Archaeal three-step pathway; single essential route; Sep→Cys rescue under Se starvation.
4. **Aeby E, Palioura S, Pusnik M, et al.** The canonical Sec insertion pathway is dispensable in trypanosomes. *PNAS* 2009. **PMID 19279205.** — Eukaryotes use a single Sep-tRNA^Sec-dependent route; core enzymes essential for Sec but not for viability in *T. brucei*.
5. **Puppala AK, Castillo Suchkou J, French RL, Kiernan KA, Simonović M.** Structural basis for tRNA-dependent activation of the terminal complex of Sec synthesis in humans. 2023. **PMID 36929010.** — Substrate-induced activation of human SepSecS.
6. **Puppala AK, Sosa J, Castillo Suchkou J, et al.** Human SEPSECS evolved to optimize binding of a tRNA-based substrate. 2024. **PMID 39385655.** — Vertebrate-specific α16 helix; archaeal ortholog as ancestral proxy.
7. **Puppala AK, French RL, Matthies D, et al.** Structural basis for early-onset neurological disorders caused by SepSecS mutations. *Sci Rep* 2016. **PMID 27576344.** — Disease via destabilization/misfolding.
8. **Simonović M, Puppala AK.** On elongation factor eEFSec, its role and mechanism. *BBA* 2018. **PMID 29555379.** — eEFSec chalice architecture; non-canonical delivery.
9. **Gribling-Burrer AS, Leichter M, Wurth L, et al.** SBP2 interacts with the SMN complex and methylosome for selenoprotein mRNP assembly and translation. *NAR* 2017. **PMID 28115638.** — Eukaryotic SECIS recognition embedded in RNP-assembly machinery.
10. **Romero H, Zhang Y, Gladyshev VN, Salinas G.** Evolution of selenium utilization traits. *Genome Biol* 2005. **PMID 16086848.** — selB/selC as Sec signatures; selD shared with 2-selenouridine; ancient origin, HGT, losses.
11. **Chavatte L, Lange L, Schweizer U, Ohlmann T.** tRNA modifications in eukaryotic UGA recoding as Sec. 2025. **PMID 39988117.** — tRNA^Sec modification isoforms and selenoprotein hierarchy.
12. **Ticó JR, Mariotti M.** The Metazoan Selenoproteome. 2026. **PMID 41212935.** — Sec pathway losses and Sec→Cys substitutions across animals.
13. **Oudouhou F, Casu B, Dopgwa Puemi AS, Sygusch J, Baron C.** Interactions among SEPHS1, SEPHS2, SEPSECS, SECp43. 2017. **PMID 28414460.** — Evidence for a synthesis oligomer/complex.
14. **Ahmed Mohamed A, et al.** SEPHS1: a master key for neurodevelopmental disorders. 2024. **PMID 38960024.** — SEPHS1 vs. SEPHS2 distinction; disease relevance.
15. **Manhas R, Gowri VS, Madhubala R.** *Leishmania donovani* encodes a functional SepSecS. 2016. **PMID 26586914.** — SepSecS complements ΔselA only with archaeal PSTK (Sep-intermediate dependency).
16. **Miller C, Bröcker MJ, et al.** A synthetic tRNA for EF-Tu-mediated Sec incorporation. 2015. **PMID 26160755.** — SelB/SECIS requirement and engineering around it.
17. **da Silva MTA, Silva-Jardim I, Thiemann OH.** Selenium and its role in trypanosomiasis. 2014. **PMID 24251578.** — Trypanosomatids recode UGA without SBP2/SecP43.
18. **Sherlock LG, et al.** Hepatic decrease of Se-processing enzymes after endotoxemia. 2020. **PMID 33224150.** — Physiological-state regulation of the whole module.
19. **Krutyhołowa R, et al.** Kti12, a PSTK-like tRNA-dependent ATPase. 2019. **PMID 30916349.** — Structural kinship of PSTK to a broader ATPase family.
20. **Zhang J, Wang Y, Li Y, Chen X.** Composition and evolution of the prokaryotic selenoproteome. 2026. **PMID 42080570.** — SECIS diversity and prokaryotic Sec machinery overview.
21. **Noinaj N, Wattanasak R, Lee DY, et al.** Structural insights into the catalytic mechanism of *E. coli* selenophosphate synthetase. *J Bacteriol* 2012. **PMID 22081394.** — SPS homodimer, glycine-rich loop, catalytic Asp cluster, two-step ATP mechanism.
22. **Na J, Jung J, Bang J, et al.** Selenophosphate synthetase 1 and its role in redox homeostasis, defense and proliferation. 2018. **PMID 29715549.** — SEPHS2 (catalytic) vs. SEPHS1 (non-catalytic); two-step selenophosphate synthesis.
23. **Scortecci JF, Serrão VHB, Fernandes CAH, et al.** Interaction between selenocysteine lyase and selenophosphate synthetase. 2020. **PMID 32275991.** — SelD·CsdB coupling (~1.8 nM) sequesters toxic selenide.
24. **Dobosz-Bartoszek M, Pinkerton MH, Otwinowski Z, et al.** Crystal structures of human eEFSec suggest a non-canonical mechanism for Sec incorporation. *Nat Commun* 2016. **PMID 27708257.** — Domain-4 swing on nucleotide exchange; non-canonical delivery.
25. **Fischer N, Neumann P, Bock LV, et al.** The pathway to GTPase activation of elongation factor SelB on the ribosome. *Nature* 2016. **PMID 27842381.** — Distinct SelB GTPase-activation pathway during UGA decoding.
26. **Rodnina MV, Fischer N, Maracci C, Stark H.** Ribosome dynamics during decoding. 2017. **PMID 28138068.** — EF-Tu vs. SelB tRNA selection on the ribosome.
27. **Castel R, Léon K, Gandubert C, et al.** Se supplementation after deficiency: growth, tissue Se, and selenoprotein expression in rats. 2024. **PMID 37202582.** — Demonstrates a selenium-distribution and selenoprotein-expression hierarchy.
28. **Li X, Zhang Y, Shen H, et al.** Selenium metabolism and selenoproteins in brain and encephalopathy. 2025. **PMID 39546178.** — Brain ranks highest in the organ hierarchy for maintaining Se/selenoproteins.
29. **Sherlock LG, Balasubramaniyan D, Zheng L, et al.** Neonatal selenoenzyme expression and maternal Se deficiency. 2021. **PMID 33672905.** — Protein- and organ-specific selenoprotein hierarchy in neonates.

---

*Prepared as a system-level synthesis. Uncertainty is flagged throughout; claims about complex assembly, channeling, and the minimal eukaryotic recoding mRNP rest on indirect evidence and should not be over-generalized across lineages.*


## Artifacts

- [OpenScientist final report](selenocysteine_biosynthesis_incorporation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](selenocysteine_biosynthesis_incorporation-deep-research-openscientist_artifacts/final_report.pdf)