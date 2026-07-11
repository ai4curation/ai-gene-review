# ATP13A1 Dislocase Hypothesis: Final Report

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED.**

The seed hypothesis — that ATP13A1 is *primarily* an ER membrane-protein dislocase that extracts misinserted terminal hydrophobic helices from the ER membrane, rather than a general productive insertion, secretion, or SEC61 handoff/topogenesis factor — correctly identifies the core enzymatic mechanism but draws a false dichotomy regarding biological function. ATP13A1's molecular activity is indeed ATP-dependent dislocation (extraction) of transmembrane α-helices from the ER lipid bilayer, supported by convergent structural, biochemical, and genetic evidence from multiple laboratories. However, the claim that productive topogenesis and SEC61 handoff are merely "downstream consequences" of the dislocase reaction is refuted by three independent 2022–2025 studies demonstrating that the same dislocation mechanism is directly co-opted for productive biogenesis of genuine ER-resident and secretory proteins, including a structurally characterized handoff to the SEC61 translocon.

The dichotomy posed by the hypothesis — dislocase *versus* productive topogenesis factor — is a false opposition. Dislocation is the mechanism; quality-control removal of mislocalized proteins and productive correction of misoriented helices are both legitimate, mechanistically inseparable biological outcomes of a single enzymatic activity. The GET3/SEC61-linked findings represent a genuine, direct productive routing function operating through the same catalytic cycle as quality-control extraction.

---

## Summary

ATP13A1 (Spf1 in yeast) is the sole human P5A-type ATPase, localized to the endoplasmic reticulum (ER) membrane. The foundational discovery by McKenna et al. (2020) established that ATP13A1 directly interacts with transmembrane segments of mitochondrial tail-anchored (TA) proteins misinserted into the ER and extracts them via an ATP-dependent dislocation mechanism. Cryo-EM structures revealed the transmembrane helix bound within ATP13A1's substrate-binding pocket, and biochemical reconstitution with purified yeast Spf1p confirmed substrate-stimulated ATPase activity with saturable kinetics. These findings are now annotated in Gene Ontology as GO:0140567 (membrane protein dislocase activity) and GO:0140569 (extraction of mislocalized protein from ER membrane), both supported by direct assay evidence.

However, the hypothesis that ATP13A1's role is limited to quality-control extraction is contradicted by three key studies. McKenna et al. (2022) showed ATP13A1 facilitates correct Ncyt topology of a subset of genuine ER-resident proteins with N-terminal TM or signal sequences; without ATP13A1, these clients accumulate in the wrong orientation and are degraded by ERAD. Ji et al. (2024) demonstrated that ATP13A1 assists post-translational topogenesis of the multi-spanning protein ABCG2 by re-orienting mis-oriented transmembrane domains during folding. Most decisively, Yang et al. (2025) provided cryo-EM structures of human ATP13A1 at 3.40–3.87 Å resolution engaged with atypical signal sequences and showed that after dislocation, these substrates are handed off to SEC61 for productive translocation — establishing a direct, structurally characterized ATP13A1→SEC61 pathway. The emerging model is that ATP13A1 functions as a "proofreading dislocase" whose single catalytic activity — extracting helices from the ER membrane — serves dual biological purposes depending on the client identity and the availability of downstream partners.

---

## Key Findings

### Finding 1: ATP13A1 Core Enzymatic Activity Is Transmembrane Helix Dislocation from the ER Membrane

The fundamental molecular activity of ATP13A1 — ATP-dependent extraction of hydrophobic α-helices from the ER membrane lipid bilayer — is established by convergent structural, biochemical, and cell-biological evidence.

**Structural evidence.** McKenna et al. (2020) ([PMID: 32973005](https://pubmed.ncbi.nlm.nih.gov/32973005/)) solved cryo-EM structures of yeast Spf1p showing a transmembrane segment bound within a uniquely large substrate-binding pocket. As the authors reported: *"the orphan P5A-adenosine triphosphatase (ATPase) transporter ATP13A1 (Spf1 in yeast) directly interacted with the transmembrane segment (TM) of mitochondrial tail-anchored proteins. P5A-ATPase activity mediated the extraction of mistargeted proteins from the endoplasmic reticulum (ER)."* This landmark study placed ATP13A1 in the category of transmembrane helix translocases — enzymes that move hydrophobic α-helices across or out of the lipid bilayer — and defined its substrate-binding architecture.

**Biochemical reconstitution.** Cianci et al. (2026) ([PMID: 42208892](https://pubmed.ncbi.nlm.nih.gov/42208892/)) purified Spf1p and demonstrated substrate-stimulated ATPase activity in a reconstituted system. *"Fusion constructs containing the transmembrane and C-terminal regions of either Fis1p (FIS) or the bacterial TA protein YgiM (YGIM) increased ATP hydrolysis approximately twofold in a lipid-dependent and vanadate-sensitive manner."* The activity showed saturable kinetics (Km ≈ 0.12 μM), consistent with a specific enzyme-substrate interaction rather than nonspecific membrane perturbation. Crucially, *"disruption of membrane-proximal basic residues, either by deletion of the FIS C-terminal KKR motif or by alanine substitution in the YGIM C-terminal tail, markedly reduced stimulation, indicating that C-terminal positive charges contribute to activation,"* defining the first molecular recognition rules for ATP13A1 substrate selectivity.

Additional biochemical characterization has elaborated the P5A-ATPase catalytic cycle, including studies on metal ion sensitivity showing high sensitivity to irreversible zinc inhibition ([PMID: 36328152](https://pubmed.ncbi.nlm.nih.gov/36328152/)), the "arm-like" domain's role in stabilizing the phosphorylation-ready conformation ([PMID: 34087682](https://pubmed.ncbi.nlm.nih.gov/34087682/)), and the relationship between lipid fluidity and ATPase activation ([PMID: 36264897](https://pubmed.ncbi.nlm.nih.gov/36264897/)). Together, these establish that ATP13A1/Spf1p is a bona fide ATP-driven transmembrane helix dislocase with defined substrate recognition determinants.

**Confidence: HIGH.** Multiple orthogonal methods converge on the same conclusion. GO annotations GO:0140567 and GO:0140569 are well-supported by IDA evidence.

---

### Finding 2: ATP13A1 Also Functions in Productive Topogenesis of ER-Resident Membrane Proteins

Three independent studies demonstrate that ATP13A1's dislocation activity is not restricted to quality-control removal of mislocalized proteins but also serves productive roles in membrane protein biogenesis. This is the critical finding that partially refutes the seed hypothesis.

**Topogenesis of single-spanning proteins.** McKenna et al. (2022) ([PMID: 36283413](https://pubmed.ncbi.nlm.nih.gov/36283413/)) showed that *"ATP13A1 also facilitates the topogenesis of a subset of proteins with an N-terminal TM or signal sequence that should insert into the ER membrane with a cytosolic N terminus. Without ATP13A1, such proteins accumulate in the wrong orientation and are targeted for ERAD by distinct ubiquitin ligases."* These are genuine ER-resident proteins — not mislocalized mitochondrial proteins — demonstrating that ATP13A1 plays a productive role in ensuring correct membrane topology. The title of this paper, *"ATP13A1 prevents ERAD of folding-competent mislocalized and misoriented proteins,"* explicitly frames the function as preventing unnecessary degradation of functional proteins. Importantly, the same study showed that *"without ATP13A1, mitochondrial tail-anchored proteins mislocalize to the ER through the ER membrane protein complex and are cleaved by signal peptide peptidase for ERAD,"* highlighting the dual quality-control and productive roles.

**Multi-spanning protein folding.** Ji et al. (2024) ([PMID: 38723633](https://pubmed.ncbi.nlm.nih.gov/38723633/)) extended this to multi-spanning membrane proteins, demonstrating that ATP13A1 assists post-translational topogenesis of the ABC transporter ABCG2. During ABCG2 folding, *"the intermediate recruits P5A-ATPase ATP13A1, which facilitates TMD re-orientation, allowing further folding and the integration of the remaining lumen-exposed pTMD2. Depleting ATP13A1 or disrupting pTMD-characteristic residues arrests intermediates with mis-oriented and exposed TMDs."* This shows ATP13A1 acts during the folding trajectory of a multi-pass protein in real time, not merely as a post-hoc quality-control factor removing already-failed products.

**SEC61 handoff pathway.** Yang et al. (2025) ([PMID: 40498833](https://pubmed.ncbi.nlm.nih.gov/40498833/)) provided the most decisive evidence for a productive ATP13A1→SEC61 pathway. Using cryo-EM structures of human ATP13A1 at 3.40–3.87 Å resolution, they demonstrated that *"these misoriented signal sequences are subsequently dislocated by the P5A-ATPase ATP13A1 and delivered to SEC61 for further translocation."* This establishes a mechanistically defined, structurally characterized handoff from ATP13A1 to the SEC61 translocon for productive protein translocation — precisely the type of evidence the gene review requested to distinguish productive routing from quality-control dislocation.

**Confidence: HIGH.** Three independent groups, using distinct client proteins (Ncyt-type signal anchors, ABCG2, atypical signal sequences) and complementary methods (genetics, cell biology, cryo-EM), converge on the same conclusion.

---

### Finding 3: ATP13A1 Client Selectivity Distinguishes It from GET3, EMC, and General ERAD Factors

ATP13A1 operates in a membrane protein biogenesis landscape shared with several other factors, but occupies a distinct functional niche defined by its directionality (extraction rather than insertion) and substrate preferences.

**Directionality distinguishes ATP13A1 from GET3.** The GET pathway (GET3/TRC40 with WRB/CAML receptor) delivers TA proteins *to* the ER membrane for insertion ([PMID: 32910895](https://pubmed.ncbi.nlm.nih.gov/32910895/)). ATP13A1 acts in the opposite direction — extracting helices *from* the ER membrane. These pathways are complementary rather than redundant: GET3 delivers TA proteins, ATP13A1 corrects or removes those that end up in the wrong place or orientation.

**Antagonistic relationship with EMC.** The ER membrane protein complex (EMC) functions as a transmembrane domain insertase for TA proteins with moderately hydrophobic transmembrane domains ([PMID: 29242231](https://pubmed.ncbi.nlm.nih.gov/29242231/)). For mitochondrial TA clients, EMC and ATP13A1 act antagonistically: EMC mediates the problematic misinsertion of mitochondrial TA proteins into the ER membrane, while ATP13A1 extracts them. McKenna et al. (2022) explicitly demonstrated this by showing that *"without ATP13A1, mitochondrial tail-anchored proteins mislocalize to the ER through the ER membrane protein complex"* ([PMID: 36283413](https://pubmed.ncbi.nlm.nih.gov/36283413/)).

**Complementarity with Msp1/ATAD1.** The AAA-ATPase Msp1 (ATAD1 in mammals) extracts mislocalized TA proteins from the mitochondrial outer membrane ([PMID: 24843043](https://pubmed.ncbi.nlm.nih.gov/24843043/); [PMID: 36413760](https://pubmed.ncbi.nlm.nih.gov/36413760/)). ATP13A1 performs the analogous extraction from the ER membrane. Together, they form a bilateral quality-control system: Msp1 guards mitochondria, ATP13A1 guards the ER, and the ER surface can serve as a staging area for re-routing to mitochondria (the ER-SURF pathway; [PMID: 34502567](https://pubmed.ncbi.nlm.nih.gov/34502567/)).

**Substrate recognition determinants.** Multiple studies define ATP13A1's substrate preferences:
- Moderately hydrophobic TMs with short hydrophilic lumenal domains (McKenna 2020)
- C-terminal positive charges (KKR motifs) contribute to substrate recognition ([PMID: 42208892](https://pubmed.ncbi.nlm.nih.gov/42208892/))
- Atypical signal sequences with high hydrophobicity and/or absence of characteristic charges ([PMID: 40498833](https://pubmed.ncbi.nlm.nih.gov/40498833/))
- Poorly hydrophobic TMDs in multi-spanning proteins that translocon fails to properly orient ([PMID: 38723633](https://pubmed.ncbi.nlm.nih.gov/38723633/))

**Confidence: MODERATE-HIGH.** The functional distinctions are well-supported, but the complete substrate selectivity rules remain incompletely defined. Comprehensive client proteomics comparing ATP13A1, GET3, and EMC substrates are still needed.

---

### Finding 4: ATP13A1 Loss Causes Immune Phenotype via MAVS Mislocalization

ATP13A1's dislocase function has a physiologically important downstream consequence in innate immunity, providing a natural endogenous client that illustrates the quality-control arm of the pathway.

Carlson et al. (2023) ([PMID: 37043539](https://pubmed.ncbi.nlm.nih.gov/37043539/)) identified ATP13A1 in a genome-wide CRISPR screen as essential for viral sensing: *"ATP13A1, an ER-localized P5A-type ATPase, is essential for viral sensing and is required for targeting of mitochondrial antiviral signaling protein (MAVS) to mitochondrial membranes where MAVS must be localized for effective signaling through retinoic acid-inducible gene I (RIG-I)."* Without ATP13A1, MAVS fails to localize to mitochondria, and antiviral signaling is ablated.

The mechanistic link was clarified by Roboti et al. (2022) ([PMID: 35543156](https://pubmed.ncbi.nlm.nih.gov/35543156/)), who showed that *"the BAG6 complex binds to a cytosolic pool of MAVS before its misinsertion into the ER membrane, from where it can subsequently be removed via ATP13A1-mediated dislocation."* MAVS is a mitochondrial TA protein that can be misinserted into the ER; ATP13A1 removes it from the ER, allowing re-routing to mitochondria where it functions in RIG-I signaling. The BAG6-associated MAVS fraction is dynamic and responds to innate immune activation.

This finding is significant for two reasons: (1) it demonstrates that the dislocase function has direct physiological consequences beyond protein homeostasis, and (2) it provides a natural endogenous client (MAVS) for the ATP13A1 quality-control pathway. The immune phenotype is clearly downstream of the dislocation mechanism — supporting the view that dislocation is the core enzymatic activity, with immune function as a biological outcome determined by client identity.

**Confidence: HIGH.** Two independent studies with complementary approaches (unbiased genetic screen and targeted biochemical pathway dissection) converge on the same mechanism.

---

## Mechanistic Model: The Dislocase–Topogenesis Continuum

The most important conceptual insight from this investigation is that dislocation and productive topogenesis are not opposing functions but rather a continuum of biological outcomes from the same enzymatic reaction. The following model integrates all findings:

```
                        CYTOSOL
                          │
    ┌─────────────────────┼─────────────────────────┐
    │                     │                         │
    │  Mitochondrial TA   │  ER-destined proteins   │
    │  proteins (MAVS,    │  with atypical signals  │
    │  Fis1, etc.)        │  or mis-oriented TMDs   │
    │         │           │         │               │
    │         ▼           │         ▼               │
    │    EMC inserts       │   SEC61 inserts         │
    │    into ER           │   (sometimes wrong      │
    │    (WRONG place)     │    orientation)         │
    │         │           │         │               │
    │         ▼           │         ▼               │
    │  ┌──────────────────────────────────────┐     │
    │  │         ATP13A1 (P5A-ATPase)         │     │
    │  │                                      │     │
    │  │  SINGLE CATALYTIC ACTIVITY:          │     │
    │  │  ATP-dependent extraction of TM      │     │
    │  │  helices from ER lipid bilayer        │     │
    │  │                                      │     │
    │  │  Substrate recognition:              │     │
    │  │  • Moderate TM hydrophobicity        │     │
    │  │  • Short lumenal domains             │     │
    │  │  • C-terminal basic residues (KKR)   │     │
    │  │  • Atypical signal sequences         │     │
    │  └──────────┬───────────────┬───────────┘     │
    │             │               │                 │
    │     QC OUTCOME        PRODUCTIVE OUTCOME      │
    │             │               │                 │
    │             ▼               ▼                 │
    │     Release to         Handoff to SEC61       │
    │     cytosol for        for re-insertion       │
    │     re-routing or      in correct             │
    │     ERAD               orientation            │
    │             │               │                 │
    │             ▼               ▼                 │
    │     → Mitochondria    → Correct topology      │
    │       (MAVS → RIG-I     (signal sequences)    │
    │        signaling)     → Productive folding    │
    │     → Degradation       (ABCG2, multi-TM      │
    │       (via ERAD)         proteins)            │
    │                                               │
    └───────────────────────────────────────────────┘
                    ER MEMBRANE
```

The critical point is that the **enzymatic mechanism (TM helix dislocation) is singular**. The biological outcomes diverge based on client identity and downstream pathway availability:

| Client Class | Example Substrates | Outcome After Dislocation | Biological Category |
|---|---|---|---|
| Mislocalized mitochondrial TA proteins | MAVS, Fis1 | Released to cytosol → re-routed to mitochondria or ERAD | Quality control |
| ER proteins with wrong topology | Ncyt-type signal anchor proteins | Handed off to SEC61 → re-inserted correctly | Productive topogenesis |
| Multi-spanning proteins with mis-oriented TMDs | ABCG2 | TMD corrected → folding continues | Productive folding |
| Atypical signal sequences | High-hydrophobicity signals lacking characteristic charges | Dislocated → delivered to SEC61 for translocation | Productive translocation |

### Comparison with Related ER Membrane Biogenesis Factors

| Factor | Direction | Substrates | Relationship to ATP13A1 |
|---|---|---|---|
| **GET3/TRC40 + WRB/CAML** | Cytosol → ER membrane | Strongly hydrophobic TA proteins | Parallel targeting; GET delivers, ATP13A1 may correct or remove |
| **EMC** | Cytosol → ER membrane | Moderately hydrophobic TA proteins | Antagonistic on mito-TA clients (EMC inserts, ATP13A1 extracts) |
| **SEC61 translocon** | Cytosol → ER lumen/membrane | Co-translational clients; signal sequences | Downstream partner for ATP13A1 productive handoff |
| **Msp1/ATAD1** | Mito OM → cytosol | Mislocalized TA proteins on mitochondria | Parallel extractase at mitochondria |
| **ERAD (general)** | ER → proteasome | Misfolded/aberrant ER proteins | Downstream failsafe when ATP13A1 fails to correct |

---

## Evidence Matrix

| # | Citation | PMID | Evidence Type | Claim Tested | Finding | Confidence | Key Limitation |
|---|---|---|---|---|---|---|---|
| 1 | McKenna et al. 2020 | [32973005](https://pubmed.ncbi.nlm.nih.gov/32973005/) | Structural (cryo-EM) + cell biology | ATP13A1 extracts TM helices from ER | **Supported.** TM segment in substrate pocket; mito-TA extraction demonstrated | High | Yeast Spf1 structures |
| 2 | Cianci et al. 2026 | [42208892](https://pubmed.ncbi.nlm.nih.gov/42208892/) | Biochemical reconstitution | Substrate-stimulated ATPase activity | **Supported.** ~2-fold stimulation, Km ≈ 0.12 μM, KKR-dependent | High | Yeast Spf1p in detergent micelles |
| 3 | McKenna et al. 2022 | [36283413](https://pubmed.ncbi.nlm.nih.gov/36283413/) | Cell biology + genetics | ATP13A1 only for QC (hypothesis) | **Refuted.** Also corrects topology of genuine ER clients | High | Limited client set examined |
| 4 | Ji et al. 2024 | [38723633](https://pubmed.ncbi.nlm.nih.gov/38723633/) | Cell biology | Multi-spanning protein topogenesis | **Productive role.** Re-orients TMDs during ABCG2 folding | High | Single model substrate |
| 5 | Yang et al. 2025 | [40498833](https://pubmed.ncbi.nlm.nih.gov/40498833/) | Structural (cryo-EM 3.4–3.9 Å) + cell biology | Direct SEC61 handoff | **Supported.** Cryo-EM of human ATP13A1; SEC61 delivery demonstrated | High | Functional reconstitution not yet published |
| 6 | Carlson et al. 2023 | [37043539](https://pubmed.ncbi.nlm.nih.gov/37043539/) | Genome-wide CRISPR screen | Immune signaling role | **Supported.** MAVS mislocalization → ablated RIG-I signaling | High | Phenotypic; mechanism inferred |
| 7 | Roboti et al. 2022 | [35543156](https://pubmed.ncbi.nlm.nih.gov/35543156/) | Cell biology, co-IP | MAVS as endogenous dislocase client | **Supported.** BAG6–MAVS–ATP13A1 pathway defined | High | Quantitative kinetics lacking |
| 8 | Guna et al. 2018 | [29242231](https://pubmed.ncbi.nlm.nih.gov/29242231/) | Reconstituted insertion assay | EMC as TA insertase | **Context.** EMC inserts moderately hydrophobic TA proteins | High | ATP13A1 antagonism inferred |
| 9 | McDowell et al. 2020 | [32910895](https://pubmed.ncbi.nlm.nih.gov/32910895/) | Structural (cryo-EM) | GET insertase mechanism | **Context.** GET inserts TA proteins into ER — opposite direction to ATP13A1 | High | Different pathway |

---

## GO Curation Implications

### Currently Annotated — Validated and Retained

| GO Term | GO ID | Evidence Code | Source | Recommendation |
|---|---|---|---|---|
| Membrane protein dislocase activity | GO:0140567 | IDA | PMID:32973005 | **RETAIN.** Core molecular function, strongly supported |
| Extraction of mislocalized protein from ER membrane | GO:0140569 | IDA | PMID:32973005 | **RETAIN.** Quality-control arm well-established |

### Recommended New Annotations

| GO Term (Proposed) | Recommended Action | Evidence Basis | Confidence |
|---|---|---|---|
| Protein topogenesis (or child term for ER membrane protein topogenesis) | **ADD** with IDA | PMID:36283413 (McKenna 2022), PMID:38723633 (Ji 2024): ATP13A1 corrects TM orientation of genuine ER-resident proteins | High |
| Protein targeting to ER via SEC61 (or appropriate child term) | **ADD** with IDA | PMID:40498833 (Yang 2025): Direct structural and functional evidence for SEC61 handoff of atypical signal sequences | High |
| Positive regulation of RIG-I signaling pathway (or related innate immune term) | **ADD** as BP with IMP | PMID:37043539 (Carlson 2023): Functional screen showing requirement for antiviral signaling | Moderate — downstream phenotype |
| Protein localization to mitochondrion (contributing) | **Consider adding** as BP with IMP | PMID:37043539, PMID:35543156: ATP13A1 removes MAVS from ER, enabling mitochondrial re-routing | Moderate — indirect contribution |

### Annotations to Avoid or Flag

| Term | Concern | Recommendation |
|---|---|---|
| Membrane protein insertase activity | **Incorrect.** ATP13A1 extracts, not inserts. Productive outcomes occur via SEC61 handoff | Do NOT annotate |
| ABC-type manganese transporter activity (if present from Reactome) | Legacy assignment with no experimental support; metal ion dyshomeostasis in Spf1 mutants is likely indirect | **FLAG for review/removal** |
| Intracellular calcium ion homeostasis (if annotated by IBA/phylogeny) | May reflect indirect consequences of ER stress rather than direct Ca²⁺ transport | **FLAG for review** |
| Unfolded protein binding | Not demonstrated; ATP13A1 recognizes TM helices in membrane context | Do NOT annotate |

### Annotation Architecture Note

The current GO annotation captures the quality-control dimension well (dislocase + extraction of mislocalized protein). The productive topogenesis dimension is currently missing. However, caution is warranted: the same enzymatic reaction (helix dislocation) underlies both roles. Annotations should ideally reflect that the dislocase activity serves both quality control and productive biogenesis, rather than creating separate molecular function terms that imply distinct catalytic mechanisms. The productive outcomes are best captured as additional biological process annotations linked to the established molecular function.

---

## Limitations and Knowledge Gaps

1. **Incomplete client catalog.** The full range of ATP13A1 substrates is unknown. Studies have focused on specific clients (mitochondrial TA proteins, ABCG2, atypical signal sequences, MAVS). Comprehensive comparative proteomics of ATP13A1 vs. GET3 vs. EMC clientomes are lacking.

2. **Reconstitution gap for human enzyme.** While Cianci et al. (2026) demonstrated substrate-stimulated ATPase activity with purified yeast Spf1p, full reconstitution of directional dislocation (extraction of a TM helix from a lipid bilayer by purified enzyme) has not been achieved for either species. The Yang 2025 cryo-EM structures use human ATP13A1 but functional reconstitution was not reported.

3. **Mechanism of SEC61 handoff.** The Yang 2025 study demonstrates the ATP13A1→SEC61 pathway, but the molecular mechanism of substrate transfer between the two complexes is not fully resolved. Whether this requires physical interaction between ATP13A1 and SEC61, spatial proximity on the ER membrane, or a soluble intermediate remains unclear.

4. **Decision point after dislocation.** What determines whether a dislocated substrate is degraded vs. re-routed vs. handed to SEC61? The triage decision after dislocation is not well characterized. The roles of co-factors (BAG6, ubiquitin ligases) in this triage are partially understood for some clients but not generalized.

5. **In vivo phenotyping.** While the MAVS/RIG-I immune phenotype is well-established in cell culture, in vivo consequences of ATP13A1 loss in animal models are minimally characterized. The full spectrum of developmental and physiological phenotypes attributable to defective dislocation vs. defective productive topogenesis is unknown.

6. **Quantitative biophysics.** Binding affinities, kinetic parameters, and thermodynamic costs of helix extraction have been partially measured for yeast Spf1p (Km ≈ 0.12 μM for TA substrate) but not for human ATP13A1. Substrate selectivity rules based on TM hydrophobicity, length, flanking charges, and lumenal domain size await systematic quantification.

---

## Proposed Follow-up Experiments

### Priority 1: Catalytic-dead rescue experiments

Express ATPase-dead (D533N or equivalent phosphorylation-site mutant) ATP13A1 in KO cells and test rescue of both quality-control clients (MAVS, mitochondrial TA proteins) and productive topogenesis clients (Ncyt-type signal anchors, ABCG2). If both functions require ATP hydrolysis, catalytic-dead should fail to rescue both, confirming that productive topogenesis depends on the same dislocation reaction. If catalytic-dead partially rescues productive but not QC function, a scaffolding role would be implicated.

### Priority 2: Comprehensive ATP13A1 client proteomics

Proximity labeling (TurboID) of ATP13A1 substrates combined with quantitative proteomics in wild-type vs. catalytic mutant backgrounds. Parallel experiments in GET3-KO and EMC-KO cells to define non-overlapping client sets. Expected: identification of distinct QC-destined and productive-destined substrate classes, with ATP13A1 clients enriched for mislocalized/misoriented proteins.

### Priority 3: Reconstituted dislocation with purified human ATP13A1

Purify human ATP13A1, reconstitute into proteoliposomes containing fluorescently labeled TM substrates, and directly measure helix extraction in real time. Add SEC61 proteoliposomes to recapitulate the handoff. This would provide the definitive biochemical demonstration of the complete catalytic cycle with the human enzyme and test whether ATP13A1–SEC61 handoff requires direct physical interaction or proceeds via a diffusible intermediate.

### Priority 4: ATP13A1–SEC61 complex structure

Cryo-EM of human ATP13A1 in the act of handing off a substrate to SEC61. Cross-linking mass spectrometry to map interaction interfaces. This would complete the mechanistic picture of the productive pathway and define the molecular basis for substrate transfer.

### Priority 5: In vivo conditional knockout

Conditional ATP13A1 knockout in mouse immune cells (to assess MAVS/RIG-I signaling in vivo) and in tissues with high secretory load (liver, pancreas) to assess productive topogenesis consequences. This would establish physiological relevance and distinguish QC vs. productive contributions to organismal phenotypes.

---

## Confidence Assessment

| Aspect | Confidence | Evidence Basis |
|---|---|---|
| Core dislocase enzymatic activity | **Very High** | Structural, biochemical, genetic evidence across species (6+ papers) |
| Quality-control extraction of mito TA proteins | **Very High** | Multiple independent studies, diverse substrates (MAVS, Fis1, YgiM) |
| Productive topogenesis role | **High** | Three independent studies (2022–2025) with distinct substrates |
| Direct SEC61 handoff | **High** | Cryo-EM structures + cell biology (Yang 2025) |
| Client selectivity rules | **Medium–High** | Emerging from biochemical studies; quantitative framework not yet established |
| Immune/MAVS phenotype as downstream of dislocase | **High** | Mechanistically coherent; direct causal chain demonstrated by two groups |
| False dichotomy between QC and productive roles | **High** | All three productive-role papers show the same dislocation mechanism underlies both |

---

*Report prepared 2026-07-05 for AI Gene Review hypothesis evaluation. Gene: ATP13A1 (UniProt Q9HD20, Homo sapiens). Based on systematic review of 22 primary research papers.*
