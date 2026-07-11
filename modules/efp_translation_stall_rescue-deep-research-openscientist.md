---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T12:30:26.323660'
end_time: '2026-07-11T12:42:40.097896'
duration_seconds: 733.77
template_file: templates/module_research.md.j2
template_variables:
  module_title: EF-P translation stall rescue
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00345 module for elongation
    factor P-dependent stimulation of peptide-bond formation and rescue of stalled
    cytosolic ribosomes. The module is centered on efp (PP_1858, UniProtKB:Q88LS0).
    EarP-dependent Arg32 rhamnosylation and dTDP-L-rhamnose supply are activation
    context for pseudomonad EF-P, but they are not members of the single-gene UPA00345
    pathway bucket.
  module_outline: "- EF-P translation stall rescue\n  - 1. EF-P-dependent rescue of\
    \ stalled translation elongation\n  - EF-P stalled-ribosome rescue\n    - efp:\
    \ elongation factor P (molecular player: PSEPK efp; activity or role: translation\
    \ elongation factor activity)"
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: efp_translation_stall_rescue-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: efp_translation_stall_rescue-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

EF-P translation stall rescue

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00345 module for elongation factor P-dependent stimulation of peptide-bond formation and rescue of stalled cytosolic ribosomes. The module is centered on efp (PP_1858, UniProtKB:Q88LS0). EarP-dependent Arg32 rhamnosylation and dTDP-L-rhamnose supply are activation context for pseudomonad EF-P, but they are not members of the single-gene UPA00345 pathway bucket.

## Provisional Biological Outline

- EF-P translation stall rescue
  - 1. EF-P-dependent rescue of stalled translation elongation
  - EF-P stalled-ribosome rescue
    - efp: elongation factor P (molecular player: PSEPK efp; activity or role: translation elongation factor activity)

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

# EF-P Translation Stall Rescue: A Review-Style Synthesis

*Commissioned review of the Pseudomonas putida KT2440 UniPathway UPA00345 module for elongation factor P-dependent rescue of stalled cytosolic ribosomes, centered on efp (PP_1858, UniProtKB:Q88LS0).*

---

## 1. Executive Summary

Elongation factor P (EF-P) is a universally conserved bacterial translation factor whose single, well-defined job is to rescue 70S ribosomes that stall when the peptidyl-transferase center must join intrinsically poor peptide-bond substrates — most prominently consecutive proline residues (PPP, PPG, and longer strings). EF-P is a **structural mimic of tRNA**: it binds into the space between the ribosomal P and E sites, engages the CCA-end of the P-site peptidyl-tRNA through a post-translationally modified residue at the tip of its first domain, stabilizes the peptidyl-tRNA in a productive geometry, and thereby accelerates Pro–Pro bond formation. This is the entirety of the UPA00345 pathway bucket as it applies to *Pseudomonas putida* KT2440: a **single-gene module**, centered on *efp* (PP_1858 / Q88LS0), performing EF-P-dependent stimulation of peptide-bond formation and stall rescue.

The system's most important boundary condition is that EF-P requires a **lineage-specific post-translational modification** to reach full activity. In enterobacteria (*E. coli*, *Salmonella*) the modification is β-lysylation of Lys34 (via EpmA/EpmB); in pseudomonads and several other lineages (*P. aeruginosa*, *P. putida*, *Shewanella*, *Neisseria*) it is instead **rhamnosylation of Arg32**, catalyzed by the glycosyltransferase EarP using dTDP-L-rhamnose as the sugar donor. For the KT2440 scope defined here, EarP-dependent Arg32 rhamnosylation and the dTDP-L-rhamnose biosynthetic supply are the **activation context** for EF-P — biologically essential for full function, but *not* members of the single-gene UPA00345 pathway. Keeping this distinction crisp is central to the scope of this review.

Three further facts frame the biology. First, EF-P is **ancient and universal**: it is the bacterial ortholog of eukaryotic eIF5A and archaeal aIF5A, sharing an L-shaped, tRNA-like architecture and a conserved modified basic residue at the domain-I tip. Second, EF-P's requirement is usually **conditional** rather than absolute — cells lacking it grow, albeit with fitness and regulatory defects — but it is essential in some species (e.g., *Neisseria meningitidis*), reflecting how many polyproline-containing essential proteins a given genome carries. Third, polyproline rescue is **partially redundant**: paralogs (EfpL/YeiP) and unrelated factors (YfmR, YebC2, the ABCF ATPase Uup) provide alternative or overlapping routes to resolving proline-induced arrest. EF-P nonetheless remains mechanistically distinct from trans-translation, ribosome recycling, and ribosome-associated quality control (RQC), which act on genuinely dead-end or aberrant complexes rather than on transiently slow but competent elongation.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The UPA00345 module comprises a **single molecular player and a single activity**:

| Component | Identity | Role |
|-----------|----------|------|
| **efp** | PP_1858 / UniProtKB:Q88LS0 (PSEPK EF-P) | Translation elongation factor that binds stalled 70S ribosomes and stimulates peptide-bond formation at hard-to-translate motifs |

The biological function is the **EF-P-dependent rescue of stalled translation elongation** in the cytosol: EF-P recognizes and binds a ribosome whose P-site holds a peptidyl-tRNA that is a poor peptide-bond donor (canonically peptidyl-prolyl-tRNA), stabilizes that tRNA, and promotes formation of the next peptide bond with an incoming (typically prolyl-)aminoacyl-tRNA. This is elongation-phase catalysis assistance, not initiation, termination, or recycling.

### 2.2 What is activation context, not a pathway member

Full EF-P activity in *P. putida* depends on **Arg32 rhamnosylation by EarP**, which in turn depends on **dTDP-L-rhamnose supply** (the RmlABCD nucleotide-sugar pathway). These are biologically obligatory for full function but are, by the scope of this brief, *activation context* rather than steps of the single-gene UPA00345 module. They are discussed here because no honest account of pseudomonad EF-P can omit them, but they should be catalogued separately (e.g., under rhamnose biosynthesis and protein glycosylation) rather than folded into the stall-rescue bucket.

### 2.3 Neighboring processes often confused with EF-P rescue

Several ribosome-rescue and quality-control systems share vocabulary ("rescue," "stalling") with EF-P but are mechanistically and functionally distinct and **should be treated separately**:

- **trans-translation (tmRNA–SmpB)** and the alternative rescue factors ArfA/ArfB: these act on ribosomes stalled at the **3′ end of a broken or nonstop mRNA** (no A-site codon), tagging the nascent chain for degradation and recycling the ribosome. EF-P, by contrast, acts on **competent, translatable** complexes to keep elongation going.
- **Ribosome-associated quality control (RQC)**: resolves stalled/collided ribosomes and targets aberrant nascent chains for degradation. EF-P prevents the stall in the first place rather than dismantling the product.
- **The ABCF ATPases (Uup, YfmR, EttA, etc.)**: some of these overlap functionally with EF-P at proline-dependent stalls (see §5.3), but they are a distinct protein family using ATP hydrolysis, not tRNA mimicry.
- **eIF5A/aIF5A**: the eukaryotic/archaeal orthologs performing the same catalytic role — homologous, not a separate confusable system, but they use a chemically different modification (hypusine) and should not be assumed identical in regulation.

### 2.4 Competing definitions in the literature

Historically, EF-P was defined (1975) as a factor that **stimulates the peptidyltransferase reaction in vitro** and was thought to act specifically on **first-peptide-bond formation** during early elongation. The modern definition — established in 2013 — is that EF-P acts **throughout elongation** to alleviate stalling at polyproline and related motifs. The review by Lassak and colleagues traces this shift explicitly ([PMID: 32011712](https://pubmed.ncbi.nlm.nih.gov/32011712/)). Thus "competing definitions" are largely historical: the polyproline model has superseded the first-bond model, though EF-P's general peptidyltransferase-stimulating activity remains part of the picture.

---

## 3. Mechanistic Overview

### 3.1 The best current model

The consensus sequence of events for EF-P-mediated rescue is:

```
   Ribosome translating an mRNA encoding a polyproline (or related) motif
                                │
                                ▼
   Peptidyl-prolyl-tRNA in P site = poor peptide-bond DONOR;
   incoming prolyl-tRNA = poor ACCEPTOR  →  elongation STALLS
                                │
                                ▼
   EF-P (tRNA-shaped) SCANS for a ribosome with a vacant E site
                                │
                                ▼
   EF-P binds between P and E sites; domain-I tip (modified
   Arg32-rhamnose in P. putida) reaches the P-site tRNA CCA end
                                │
                                ▼
   Peptidyl-tRNA STABILIZED; nascent chain reoriented into a
   favorable geometry for catalysis
                                │
                                ▼
   Pro–Pro PEPTIDE BOND forms; ribosome resumes elongation
                                │
                                ▼
   EF-P dissociates; cycle repeats at the next problematic motif
```

### 3.2 Obligatory, conditional, and accessory steps

- **Obligatory:** (i) presence of a stall-prone motif in the mRNA; (ii) a P-site peptidyl-tRNA whose D-arm EF-P can recognize; (iii) a vacant E site to admit EF-P; (iv) engagement of the peptidyl-tRNA CCA-end by EF-P's domain-I tip; (v) stimulation of peptide-bond formation.
- **Conditional (for full activity, lineage-dependent):** post-translational modification of the domain-I tip residue — β-Lys34 (enterobacteria) or rhamnosyl-Arg32 (pseudomonads and others). Unmodified EF-Ps of the PGKGP subfamily can be active without modification, and specific amino-acid substitutions can convert marginally active unmodified EF-Ps into fully functional ones ([PMID: 38635400](https://pubmed.ncbi.nlm.nih.gov/38635400/)). So modification is conditional, not universally obligatory.
- **Accessory/context-dependent:** the strength of a given stall depends on the **sequence context upstream** of the motif — some N-terminal residues (Cys, Thr) suppress stalling while others (Arg, His) promote it ([PMID: 25143529](https://pubmed.ncbi.nlm.nih.gov/25143529/)). Redundant factors (EfpL, YfmR, YebC2, Uup) are accessory routes rather than core steps.

### 3.3 Molecular assemblies carrying out each step

The active assembly is the **stalled 70S ribosome + P-site peptidyl-tRNA + EF-P**. Cryo-EM of stalled 70S complexes with and without EF-P shows that EF-P's modification contacts the CCA-end of the P-site tRNA and enforces an alternative nascent-chain conformation that permits favorable substrate geometry ([PMID: 29100052](https://pubmed.ncbi.nlm.nih.gov/29100052/)). Kinetically, EF-P **scans** for a free E site and can bind any ribosome with a P-site tRNA regardless of functional state, but is **retained selectively** on complexes that actually need help; the modification increases the association rate roughly two-fold ([PMID: 39315709](https://pubmed.ncbi.nlm.nih.gov/39315709/)).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 EF-P — the tRNA mimic (Finding F003)

The crystal structure of *Thermus thermophilus* EF-P revealed **three β-barrel domains arranged in an L-shape**, with 65-Å and 53-Å arms meeting at ~95°, "reminiscent of tRNA" ([PMID: 15210970](https://pubmed.ncbi.nlm.nih.gov/15210970/): *"The three domains of EF-P are arranged in an 'L' shape, with 65- and 53-Å-long arms at an angle of 95 degrees, which is reminiscent of tRNA."*). The tip of domain I carries a conserved positively charged residue — the modification site. The same study established that Eukarya and Archaea possess the homolog **eIF5A/aIF5A** (*"Eukarya and Archaea have an EF-P homologue, eukaryotic initiation factor 5A (eIF-5A)."*), marking EF-P as part of a deeply conserved, cross-domain protein family. This structural mimicry explains how EF-P slots into the tRNA-binding channel of the ribosome between the P and E sites.

### 4.2 The catalytic action on the ribosome (Finding F001)

EF-P performs two coupled actions: it **stabilizes the P-site peptidyl-tRNA** in the catalytic center and **promotes peptide-bond formation**. Doerfel et al. (2013) demonstrated that EF-P prevents stalling at PPG/PPP and longer proline strings and accelerates peptide-bond formation ([PMID: 23239624](https://pubmed.ncbi.nlm.nih.gov/23239624/): *"EF-P promotes peptide-bond formation and stabilizes the peptidyl-transfer RNA in the catalytic center of the ribosome."*). Huter et al. (2017) provided the structural basis: *"Binding of EF-P stabilizes the P-site tRNA, particularly via interactions between its modification and the CCA end, thereby enforcing an alternative conformation of the polyproline-containing nascent chain, which allows a favorable substrate geometry for peptide bond formation"* ([PMID: 29100052](https://pubmed.ncbi.nlm.nih.gov/29100052/)).

### 4.3 The activation module — EarP, Arg32, and dTDP-L-rhamnose (Finding F002)

In pseudomonads, EF-P is activated by a modification chemically distinct from the enterobacterial one. Rajkovic et al. (2015) showed that *P. aeruginosa* EF-P carries a **single cyclic rhamnose on Arg32**, at the position equivalent to *E. coli* β-Lys34, and that the enzyme **EarP uses dTDP-L-rhamnose in vitro** ([PMID: 26060278](https://pubmed.ncbi.nlm.nih.gov/26060278/): *"Structural analyses of P. aeruginosa EF-P revealed the attachment of a single cyclic rhamnose moiety to an Arg residue at a position equivalent to that at which β-Lys is attached to E. coli EF-P."* and *"In vitro assays confirmed the ability of EarP to use dTDP-L-rhamnose as a substrate for the posttranslational glycosylation of EF-P."*). Loss of *efp*, *earP*, or *rmlC* (rhamnose biosynthesis) abolishes Pro4-GFP reporter output. Krafczyk et al. (2017) solved the EarP structure and confirmed Arg32 as the acceptor ([PMID: 28951478](https://pubmed.ncbi.nlm.nih.gov/28951478/): *"EF-P is rhamnosylated on arginine 32 by the glycosyltransferase EarP."*). Per the review scope, **this activation module is context, not a member of the single-gene UPA00345 pathway** — but it is functionally indispensable in *P. putida*.

### 4.4 Substrate recognition and kinetics (Finding F004)

EF-P's selectivity derives partly from the **tRNA it recognizes** and partly from its **binding kinetics**. Katoh et al. (2016) identified the **9-nucleotide D-loop closed by a stable D-stem** of tRNA(Pro) — a feature shared with tRNA(fMet) — as the crucial recognition determinant ([PMID: 27216360](https://pubmed.ncbi.nlm.nih.gov/27216360/): *"We show that the 9-nt D-loop closed by the stable D-stem sequence in tRNA(Pro) is a crucial recognition determinant for EF-P."*). Mudryi et al. (2024), using FRET kinetics, showed that EF-P **rapidly scans for a free E site and can bind any ribosome containing a P-site tRNA regardless of functional state** ([PMID: 39315709](https://pubmed.ncbi.nlm.nih.gov/39315709/): *"EF-P rapidly scans for a free E site and can bind to any ribosome containing a P-site tRNA, regardless of the ribosome's functional state."*), being retained only on complexes that need rescue — a scanning-engagement mechanism in which the modification tunes affinity.

### 4.5 Redundant and alternative factors (Finding F005)

EF-P is not the only route to resolving proline-induced arrest:

| Factor | Family | Evidence |
|--------|--------|----------|
| **EfpL / YeiP** | EF-P paralog | *"numerous bacteria possess an EF-P paralog called EfpL (also known as YeiP) of unknown function"*; resolves overlapping and additional arrest motifs ([PMID: 39622818](https://pubmed.ncbi.nlm.nih.gov/39622818/)) |
| **YebC2** | Transcription-factor-like | *"YebC2 can reduce ribosome stalling and support cellular fitness in the absence of EF-P and YfmR"* ([PMID: 40215226](https://pubmed.ncbi.nlm.nih.gov/40215226/)) |
| **Uup** | ABCF ATPase | *"Uup for poly-proline-dependent stalling"* within a division of labor across ABCFs ([PMID: 38661232](https://pubmed.ncbi.nlm.nih.gov/38661232/)) |
| **YfmR** | ABCF ATPase | Acts alongside EF-P; its loss with EF-P is compensated by YebC2 ([PMID: 40215226](https://pubmed.ncbi.nlm.nih.gov/40215226/)) |

This redundancy is one reason EF-P's requirement is usually conditional.

### 4.6 Physiological output — tuning the polyproline proteome (Finding F006)

Ude et al. (2013), co-discoverers of the polyproline function, showed that *"In the absence of EF-P, ribosomes stall at polyproline stretches, whereas the presence of EF-P alleviates the translational stalling"* and demonstrated *"the physiological relevance of EF-P to fine-tune the expression of the polyproline-containing pH receptor CadC to levels necessary for an appropriate stress response"* ([PMID: 23239623](https://pubmed.ncbi.nlm.nih.gov/23239623/)). Because bacterial, archaeal, and eukaryotic proteomes contain hundreds to thousands of polyproline proteins, EF-P is best understood as a **proteome-wide tuner** of a specific, functionally enriched subset (transporters, regulators, enzymes with proline-rich motifs), not merely a rescuer of rare catastrophic stalls.

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Cross-domain conservation and origin (Finding F003)

EF-P is **ancient and universal**. Its L-shaped, tRNA-mimicking architecture and its cross-domain orthology to eIF5A (eukaryotes) and aIF5A (archaea) place its origin at or before the last universal common ancestor of the translation apparatus ([PMID: 15210970](https://pubmed.ncbi.nlm.nih.gov/15210970/)). The tRNA-like fold and the conserved modified basic tip are the deeply conserved core; the *chemistry* of the modification is the variable, lineage-specific elaboration.

### 5.2 Variation in the modification chemistry

The single conserved job (activate the domain-I tip) is met by at least three distinct solutions:

| Lineage | Modified residue | Modification | Enzymes |
|---------|-----------------|--------------|---------|
| Enterobacteria (*E. coli*, *Salmonella*) | Lys34 | (R)-β-lysylation | EpmA (YjeA), EpmB (YjeK), EpmC |
| Pseudomonads, *Shewanella*, *Neisseria* | Arg32 | Cyclic rhamnosylation | EarP + dTDP-L-rhamnose (RmlABCD) |
| Eukaryotes / Archaea (eIF5A/aIF5A) | Lys | Hypusination | Deoxyhypusine synthase, deoxyhypusine hydroxylase |
| PGKGP-subfamily bacteria | — | None (or context-compensated) | — ([PMID: 38635400](https://pubmed.ncbi.nlm.nih.gov/38635400/)) |

The β-lysyl pathway is conserved in only ~26–28% of bacteria; the rhamnosyl pathway serves a substantial additional fraction, and some EF-Ps require no modification at all. This is a striking case of **convergent activation of a conserved core** by non-homologous chemistries.

### 5.3 Redundancy and alternative routes across lineages

As catalogued in §4.5, some bacteria carry EF-P paralogs (EfpL/YeiP) and unrelated factors (YebC2, ABCF Uup/YfmR) that partially substitute for or complement EF-P ([PMID: 39622818](https://pubmed.ncbi.nlm.nih.gov/39622818/); [PMID: 40215226](https://pubmed.ncbi.nlm.nih.gov/40215226/); [PMID: 38661232](https://pubmed.ncbi.nlm.nih.gov/38661232/)). The distribution of these backups varies across lineages and helps explain why the *efp* deletion phenotype ranges from mild to lethal.

### 5.4 Conditional vs. essential requirement

In *E. coli*, *Salmonella*, *P. aeruginosa*, and *Shewanella*, EF-P and its modification are **dispensable for viability** (though important for fitness and virulence). In *Neisseria meningitidis*, by contrast, EF-P and its active-site Arg are **essential for cell viability** ([PMID: 26840407](https://pubmed.ncbi.nlm.nih.gov/26840407/)). The likely explanation is that *N. meningitidis* has more essential polyproline-containing proteins and/or a lower basal ability to translate proline stretches without EF-P. This makes EarP a candidate antibacterial target in that pathogen.

### 5.5 The mitochondrial and eukaryotic parallels

Eukaryotic cytosolic translation uses eIF5A for the identical role. Notably, **mitochondria lack an obvious EF-P/eIF5A ortholog**, and recent work implicates **TACO1** as the functional counterpart that alleviates mitoribosome stalling at polyproline stretches in human mitochondria ([PMID: 39036954](https://pubmed.ncbi.nlm.nih.gov/39036954/)). This is an example of an **analogous, non-homologous solution** evolving to meet the same constraint in a different compartment — and it underscores that one should not assume the bacterial cytosolic mechanism generalizes to all compartments.

### 5.6 Horizontal transfer and proteome co-evolution

The *efp* gene has been **horizontally transferred** multiple times among bacteria, events associated with the loss of highly conserved polyproline motifs and even of entire polyproline-containing proteins (e.g., the proteases Lon, ClpC, FtsH and the tRNA synthetases ValS, IleS1, IleS2) ([PMID: 39189989](https://pubmed.ncbi.nlm.nih.gov/39189989/)). This co-evolution shows that the EF-P system and the polyproline proteome are **coupled**: perturbing EF-P leaves lasting genomic traces in the distribution of proline motifs, particularly near ATP-binding regions.

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering constraints

- EF-P acts **only after** a peptidyl-tRNA occupies the P site and **only when the E site is vacant** — it cannot bind an E-site-occupied ribosome ([PMID: 39315709](https://pubmed.ncbi.nlm.nih.gov/39315709/)). Thus its action is temporally gated within each elongation cycle.
- EF-P engages **before** peptide-bond formation, stabilizing the substrate; it is not a post-catalysis factor.
- Modification (where required) must occur **before** the ribosome-binding step: unmodified EF-P in modification-dependent lineages is marginally active.

### 6.2 Compartment and substrate specificity

- **Cytosolic 70S ribosomes only** — this is the scope of UPA00345. Organellar (mitochondrial) stalling is handled by other factors (e.g., TACO1; [PMID: 39036954](https://pubmed.ncbi.nlm.nih.gov/39036954/)).
- **Substrate-specific**: EF-P is recruited via recognition of the P-site tRNA D-arm, with tRNA(Pro) (and tRNA(fMet)) sharing the key 9-nt D-loop/stable D-stem determinant ([PMID: 27216360](https://pubmed.ncbi.nlm.nih.gov/27216360/)). The stalling that requires rescue is concentrated at proline-proline and proline-rich motifs, extended by problematic flanking residues and specific upstream contexts ([PMID: 25143529](https://pubmed.ncbi.nlm.nih.gov/25143529/)).

### 6.3 Failure modes

- **Loss of EF-P** (Δ*efp*): ribosome stalling at polyproline motifs, reduced/altered expression of polyproline proteins, fitness and stress-response defects (e.g., impaired CadC-mediated acid response; [PMID: 23239623](https://pubmed.ncbi.nlm.nih.gov/23239623/)), attenuated virulence, and — in some species — lethality ([PMID: 26840407](https://pubmed.ncbi.nlm.nih.gov/26840407/)).
- **Loss of the modification machinery** (Δ*earP*, Δ*rmlC* in pseudomonads; Δ*epmA/B* in enterobacteria): phenocopies partial loss of EF-P because the factor is present but under-active ([PMID: 26060278](https://pubmed.ncbi.nlm.nih.gov/26060278/)).
- **Compensation**: partial rescue by EfpL, YebC2, YfmR, and Uup mitigates these failures to varying degrees ([PMID: 39622818](https://pubmed.ncbi.nlm.nih.gov/39622818/); [PMID: 40215226](https://pubmed.ncbi.nlm.nih.gov/40215226/); [PMID: 38661232](https://pubmed.ncbi.nlm.nih.gov/38661232/)).

### 6.4 Evidence ruling out otherwise-plausible paths

- EF-P is **not** a first-peptide-bond-only factor: the 2013 studies and subsequent work show it acts throughout elongation ([PMID: 32011712](https://pubmed.ncbi.nlm.nih.gov/32011712/); [PMID: 23239624](https://pubmed.ncbi.nlm.nih.gov/23239624/)).
- EF-P is **not** a nonstop/no-A-site rescue factor — that niche belongs to tmRNA–SmpB/ArfA/ArfB. EF-P rescues **competent, translatable** complexes.
- Modification is **not strictly obligatory in all lineages** — PGKGP-subfamily EF-Ps function unmodified, ruling out a universal "modification-is-essential" model ([PMID: 38635400](https://pubmed.ncbi.nlm.nih.gov/38635400/)).

---

## 7. Controversies and Open Questions

**Strongly supported claims.** The core mechanism — EF-P is a tRNA-mimic that binds the vacant E site of a stalled ribosome, stabilizes the P-site peptidyl-tRNA via a modified domain-I tip, and stimulates polyproline peptide-bond formation — is supported by convergent biochemical (Doerfel/Ude 2013), structural (cryo-EM 2017), and kinetic (FRET 2024) evidence ([PMID: 23239624](https://pubmed.ncbi.nlm.nih.gov/23239624/); [PMID: 23239623](https://pubmed.ncbi.nlm.nih.gov/23239623/); [PMID: 29100052](https://pubmed.ncbi.nlm.nih.gov/29100052/); [PMID: 39315709](https://pubmed.ncbi.nlm.nih.gov/39315709/)). The existence of the alternative pseudomonad Arg32-rhamnosyl modification is likewise firmly established ([PMID: 26060278](https://pubmed.ncbi.nlm.nih.gov/26060278/); [PMID: 28951478](https://pubmed.ncbi.nlm.nih.gov/28951478/)).

**Areas of disagreement or indirect evidence.**

1. **Role of the modification.** The classic view held modification to be strictly required for activity; newer work shows a more nuanced, sometimes dispensable role, with unmodified EF-Ps active in certain sequence contexts ([PMID: 32011712](https://pubmed.ncbi.nlm.nih.gov/32011712/); [PMID: 38635400](https://pubmed.ncbi.nlm.nih.gov/38635400/)). How much of the modification's contribution is affinity (the ~2-fold association effect; [PMID: 39315709](https://pubmed.ncbi.nlm.nih.gov/39315709/)) versus catalytic geometry remains only partly resolved.

2. **Full motif spectrum.** Beyond canonical PPP/PPG, the complete set of arrest-inducing motifs — and how upstream sequence context modulates them — is still being mapped, with reporter and profiling approaches sometimes disagreeing ([PMID: 25143529](https://pubmed.ncbi.nlm.nih.gov/25143529/); [PMID: 39425678](https://pubmed.ncbi.nlm.nih.gov/39425678/)).

3. **Division of labor among rescue factors.** How EF-P, EfpL, YebC2, YfmR, and Uup partition the polyproline/hard-to-translate motif space — and whether this partition is conserved across lineages — is an active question ([PMID: 39622818](https://pubmed.ncbi.nlm.nih.gov/39622818/); [PMID: 40215226](https://pubmed.ncbi.nlm.nih.gov/40215226/); [PMID: 38661232](https://pubmed.ncbi.nlm.nih.gov/38661232/)).

4. **Cross-organism extrapolation.** Much mechanistic detail comes from *E. coli* and *T. thermophilus*; the pseudomonad system is inferred largely by homology plus the specific rhamnosylation data. The essential-vs-conditional distinction (*Neisseria* vs. *E. coli*) warns against assuming one organism's phenotype generalizes ([PMID: 26840407](https://pubmed.ncbi.nlm.nih.gov/26840407/)).

5. **Compartmental non-homology.** The mitochondrial solution (TACO1) is non-homologous, cautioning against assuming the bacterial mechanism is the only way to meet the polyproline constraint ([PMID: 39036954](https://pubmed.ncbi.nlm.nih.gov/39036954/)).

**Most important open questions.** (i) What is the precise catalytic contribution of the rhamnosyl modification at the atomic level in *P. putida* EF-P? (ii) What is the full, context-aware motif spectrum that EF-P rescues in pseudomonads specifically? (iii) How do the redundant factors distribute the load in vivo, and does EarP represent a viable narrow-spectrum antibacterial target in pathogens where EF-P is essential?

---

## 8. Key References

| PMID | Contribution | Relevance |
|------|-------------|-----------|
| [23239624](https://pubmed.ncbi.nlm.nih.gov/23239624/) | Doerfel et al. 2013 — EF-P stabilizes peptidyl-tRNA and promotes peptide-bond formation at proline runs | Core mechanism (F001) |
| [23239623](https://pubmed.ncbi.nlm.nih.gov/23239623/) | Ude et al. 2013 — EF-P alleviates polyproline stalling; tunes CadC | Co-discovery, physiology (F006) |
| [29100052](https://pubmed.ncbi.nlm.nih.gov/29100052/) | Huter et al. 2017 — cryo-EM structural basis of stall and rescue | Structural mechanism (F001) |
| [15210970](https://pubmed.ncbi.nlm.nih.gov/15210970/) | Hanawa-Suetsugu et al. 2004 — *T. thermophilus* EF-P structure; tRNA mimicry; eIF5A orthology | Conservation/origin (F003) |
| [26060278](https://pubmed.ncbi.nlm.nih.gov/26060278/) | Rajkovic et al. 2015 — Arg32 rhamnosylation via EarP/dTDP-L-rhamnose in *P. aeruginosa* | Pseudomonad activation (F002) |
| [28951478](https://pubmed.ncbi.nlm.nih.gov/28951478/) | Krafczyk et al. 2017 — EarP structure; Arg32 acceptor | Pseudomonad activation (F002) |
| [27216360](https://pubmed.ncbi.nlm.nih.gov/27216360/) | Katoh et al. 2016 — tRNA(Pro) D-arm recognition determinant | Substrate specificity (F004) |
| [39315709](https://pubmed.ncbi.nlm.nih.gov/39315709/) | Mudryi et al. 2024 — scanning-engagement kinetics | Recruitment mechanism (F004) |
| [39622818](https://pubmed.ncbi.nlm.nih.gov/39622818/) | Sieber et al. 2024 — EfpL/YeiP paralog | Redundancy (F005) |
| [40215226](https://pubmed.ncbi.nlm.nih.gov/40215226/) | Hong et al. 2025 — YebC2 rescues Δefp Δyfmr | Redundancy (F005) |
| [38661232](https://pubmed.ncbi.nlm.nih.gov/38661232/) | Chadani et al. 2024 — ABCF Uup handles poly-proline stalling | Redundancy (F005) |
| [32011712](https://pubmed.ncbi.nlm.nih.gov/32011712/) | Lassak review — history and evolving definition of EF-P | Definitions/controversy |
| [38635400](https://pubmed.ncbi.nlm.nih.gov/38635400/) | Unmodified EF-P design principles (PGKGP subfamily) | Modification conditionality |
| [25143529](https://pubmed.ncbi.nlm.nih.gov/25143529/) | Upstream sequence context modulates stalling | Motif determinants |
| [26840407](https://pubmed.ncbi.nlm.nih.gov/26840407/) | EF-P essential in *N. meningitidis* | Conditional vs. essential |
| [39036954](https://pubmed.ncbi.nlm.nih.gov/39036954/) | TACO1 as mitochondrial polyproline-rescue factor | Compartmental non-homology |
| [39189989](https://pubmed.ncbi.nlm.nih.gov/39189989/) | Horizontal transfer of *efp* and polyproline proteome co-evolution | Evolution |
| [25364902](https://pubmed.ncbi.nlm.nih.gov/25364902/) | Proline-repeat proteome and eIF5A across kingdoms | Proteome scope |
| [39425678](https://pubmed.ncbi.nlm.nih.gov/39425678/) | Dual reporter to map EF-P-alleviated pausing motifs | Motif mapping |

---

## Appendix A: Limitations and Knowledge Gaps of This Review

- **Data source:** This synthesis is literature-based; no primary sequence, structural, or omics dataset was analyzed de novo for *P. putida* KT2440 specifically. Pseudomonad-specific mechanistic claims rest on *P. aeruginosa*/*Shewanella*/*Neisseria* data plus homology to KT2440 EF-P (Q88LS0).
- **Organism mixing:** Mechanistic detail derives disproportionately from *E. coli* and *T. thermophilus*. Extrapolation to *P. putida* is reasonable but not experimentally confirmed at every step here.
- **Modification chemistry:** The atomic-level catalytic role of the rhamnosyl modification (vs. the β-lysyl modification) is incompletely resolved.
- **Redundancy quantification:** The in vivo load-sharing among EF-P, EfpL, YebC2, YfmR, and Uup is not quantitatively established for pseudomonads.

## Appendix B: Proposed Follow-up Experiments / Actions

1. **KT2440-specific reporter panel.** Deploy a dual-reporter polyproline pausing assay ([PMID: 39425678](https://pubmed.ncbi.nlm.nih.gov/39425678/)) in *P. putida* KT2440 across Δ*efp*, Δ*earP*, and Δ*rmlC* backgrounds to define the organism-specific motif spectrum and quantify the rhamnosylation dependence directly.
2. **Ribosome profiling** of wild-type vs. Δ*efp* KT2440 to map genome-wide stall sites and identify which polyproline-containing proteins (transporters, regulators, proteases) are EF-P-dependent in this organism.
3. **Structural determination** of rhamnosyl-EF-P (Q88LS0) on a stalled *P. putida* 70S complex by cryo-EM to resolve the catalytic contribution of the Arg32-rhamnose modification.
4. **Redundancy dissection.** Systematically delete EF-P backup candidates (EfpL, YebC2, ABCF ATPases) singly and in combination with Δ*efp* to measure epistasis and quantify load-sharing.
5. **EarP as antibacterial target.** Assess whether EarP inhibition phenocopies EF-P loss and screen for EarP inhibitors, prioritizing pathogens where EF-P is essential ([PMID: 26840407](https://pubmed.ncbi.nlm.nih.gov/26840407/)).
6. **Comparative proteomics** to test the horizontal-transfer/proteome-coupling hypothesis ([PMID: 39189989](https://pubmed.ncbi.nlm.nih.gov/39189989/)) within the pseudomonad lineage.

---

*Prepared as a commissioned review synthesis. Scope centered on the single-gene UPA00345 module (efp / PP_1858 / Q88LS0); EarP-dependent Arg32 rhamnosylation and dTDP-L-rhamnose supply treated as activation context, not pathway members.*


## Artifacts

- [OpenScientist final report](efp_translation_stall_rescue-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](efp_translation_stall_rescue-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32011712
2. PMID:38635400
3. PMID:25143529
4. PMID:29100052
5. PMID:39315709
6. PMID:15210970
7. PMID:23239624
8. PMID:26060278
9. PMID:28951478
10. PMID:27216360
11. PMID:39622818
12. PMID:40215226
13. PMID:38661232
14. PMID:23239623
15. PMID:26840407
16. PMID:39036954
17. PMID:39189989
18. PMID:39425678