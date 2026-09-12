---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T13:05:39.834713'
end_time: '2026-07-11T13:17:54.605980'
duration_seconds: 734.77
template_file: templates/module_research.md.j2
template_variables:
  module_title: tRNA m7G46 methylation
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00989 module for SAM-dependent
    formation of N7-methylguanosine at position 46 of tRNA. The module is centered
    on TrmB, the tRNA (guanine(46)-N7)-methyltransferase encoded by PP_5103. Broader
    RNA methylation and methyltransferase-complex annotations are retained only as
    context unless supported by more specific evidence.
  module_outline: "- tRNA m7G46 methylation\n  - 1. Formation of m7G46 in tRNA\n \
    \ - TrmB tRNA guanine-46 N7 methylation\n    - trmB: tRNA m7G46 methyltransferase\
    \ (molecular player: PSEPK trmB; activity or role: tRNA (guanine(46)-N7)-methyltransferase\
    \ activity)"
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: trna_m7g46_methylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: trna_m7g46_methylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

tRNA m7G46 methylation

## Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00989 module for SAM-dependent formation of N7-methylguanosine at position 46 of tRNA. The module is centered on TrmB, the tRNA (guanine(46)-N7)-methyltransferase encoded by PP_5103. Broader RNA methylation and methyltransferase-complex annotations are retained only as context unless supported by more specific evidence.

## Provisional Biological Outline

- tRNA m7G46 methylation
  - 1. Formation of m7G46 in tRNA
  - TrmB tRNA guanine-46 N7 methylation
    - trmB: tRNA m7G46 methyltransferase (molecular player: PSEPK trmB; activity or role: tRNA (guanine(46)-N7)-methyltransferase activity)

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

# tRNA m7G46 Methylation: The TrmB Module of *Pseudomonas putida* KT2440 (UPA00989)

*A commissioned review-style synthesis*

---

## 1. Executive Summary

The *Pseudomonas putida* KT2440 UniPathway module **UPA00989** describes a single, chemically simple, but biologically consequential reaction: the *S*-adenosyl-L-methionine (SAM)–dependent transfer of a methyl group to the **N7 atom of guanine-46** in the variable loop of transfer RNA, producing **7-methylguanosine (m7G46)**. The reaction is carried out by **TrmB**, the tRNA (guanine(46)-N7)-methyltransferase encoded by **PP_5103** — the *P. putida* ortholog of *E. coli* YggH and of the biochemically characterized *P. aeruginosa* TrmB. As a biological *system*, the module is best understood not as a self-contained pathway but as **one obligatory catalytic step that behaves as a node in a larger, cooperative tRNA-modification and quality-control network**.

Three ideas organize this review. First, the **chemistry and catalytic scaffold are ancient and near-universal**: TrmB is a Class I (Rossmann-fold) methyltransferase whose catalytic domain traces back toward the Last Universal Common Ancestor (LUCA), and m7G46 is among the most broadly conserved tRNA modifications across bacteria, archaea, and eukaryotes. Second, the **active assembly is lineage-variable**: TrmB is a monomer in *E. coli* and (by orthology) *Pseudomonas*, a homodimer in *Bacillus subtilis*, and an obligate heterodimer in eukaryotes (yeast Trm8–Trm82; human METTL1–WDR4). Third, the **physiological importance of m7G46 is conditional**: it is largely dispensable under permissive laboratory conditions but becomes critical under thermal and oxidative stress, where it stabilizes tRNA, supports the deposition of other modifications, and tunes codon-biased translation.

For the *P. putida* module specifically, the strongest direct evidence comes from the close relative *P. aeruginosa*, where TrmB forms m7G46 on tRNAs bearing G46 and where its loss impairs translation of phenylalanine- and aspartate-enriched messages (including catalases) and causes hydrogen-peroxide sensitivity. Direct enzymatic characterization of PP_5103 itself is limited, so the model presented here is **orthology-based but well-triangulated** across enzymology, structural biology, and comparative genomics. Throughout, the tRNA m7G46 system must be kept **distinct** from the mechanistically separate rRNA m7G (Bud23–Trm112 / RsmG) and internal mRNA m7G pathways, and its dedicated accessory subunit (Trm82/WDR4) must be distinguished from the promiscuous methyltransferase activator Trm112/TRMT112.

---

## 2. Definition and Biological Boundaries

### 2.1 What the system *is*

UPA00989 comprises exactly **one reaction**:

```
Guanine-46 (tRNA) + SAM  ──TrmB──▶  m7G46 (tRNA) + S-adenosyl-L-homocysteine (SAH)
```

The molecular player is **TrmB (PP_5103)**, a stand-alone bacterial enzyme. Its substrate is the subset of cellular tRNAs that carry an unmodified guanosine at position 46, which lies in the **variable loop** (the connector between the anticodon stem and the T-arm). In *P. aeruginosa*, 23 tRNA species with G46 were identified as candidate substrates. The methyl group is delivered from SAM, and the enzyme belongs to the **Rossmann-fold methyltransferase (RFM / Class I)** superfamily.

### 2.2 What lies *outside* the boundary

Because "m7G" appears in several unrelated contexts, careful boundary-drawing is essential. The following are frequently conflated with tRNA m7G46 but are **separate systems**:

- **rRNA m7G.** In eukaryotes, 18S rRNA position 1575 is methylated by **Bud23–Trm112** (human WBSCR22–TRMT112) during 40S ribosome biogenesis; the bacterial counterpart on 16S rRNA (m7G527) is installed by **RsmG (GidB)**. These use different writers, different substrates, and different biology from tRNA m7G46.
- **mRNA m7G.** The 5′ **cap** m7G and recently described **internal** mRNA m7G marks are distinct epitranscriptomic features, again with separate machinery and readout.
- **The Trm112 activator network.** Trm112 (human TRMT112) is a small allosteric activator that partners with a *set* of translation-related methyltransferases — Bud23 (rRNA m7G), Trm9, Trm11, Mtq2 (eRF1 methylation) — and is **not** the partner of the tRNA m7G46 writer. The dedicated m7G46 partner in eukaryotes is **Trm82/WDR4**.

### 2.3 Competing definitions

The main definitional tension is **"single reaction" vs. "network node."** UniPathway and enzyme databases treat UPA00989 as one isolated catalytic step (the correct atomic definition). The functional-genomics and physiology literature, however, shows that m7G46 exerts its effects **only in the context of other modifications** (e.g., Gm18, m1G37, m5U54) and of tRNA-decay surveillance. Both framings are valid at different levels of description; this review adopts the reaction as the *boundary* while treating the network as the *context*.

---

## 3. Mechanistic Overview

### 3.1 The best current model

The consensus sequence of events is:

1. **Substrate selection.** TrmB binds a tRNA presenting G46 in an appropriately sized variable loop. Recognition depends critically on the **variable-loop size** and on the **T-stem**, rather than on the full three-dimensional L-shape of mature tRNA.
2. **SAM binding.** SAM docks in the Rossmann-fold catalytic domain.
3. **Methyl transfer.** The methyl group is transferred to N7 of G46, yielding a positively charged 7-methylguanosine and releasing SAH.
4. **Release and downstream coupling.** The modified tRNA re-enters the pool, where m7G46 contributes to structural stability and enables/supports other modification events.

The reaction is **SN2-type methyl transfer** typical of Class I MTases: SAM as methyl donor, direct transfer to the nucleobase nitrogen, no covalent enzyme intermediate required. Notably, **N7 methylation does not alter Watson–Crick pairing** (N7 faces the major groove), consistent with a primarily **structural/stabilizing** rather than decoding-altering role at this position.

### 3.2 Obligatory, conditional, and accessory elements

| Element | Status | Basis |
|---|---|---|
| SAM as methyl donor | **Obligatory** | Class I RFM chemistry |
| G46 in a variable loop of adequate size | **Obligatory** (substrate) | Recognition depends on variable-loop size |
| T-stem contacts | **Obligatory** (recognition) | Most important recognition element in *A. aeolicus* |
| Full L-shaped tertiary fold | **Dispensable** | Truncated substrates still methylated |
| Accessory subunit (Trm82/WDR4) | **Conditional (lineage-specific)** | Required in eukaryotes, absent in *E. coli*/*Pseudomonas* |
| Homodimerization | **Accessory (lineage-specific)** | Seen in *B. subtilis*, not *E. coli* |
| m7G46 itself for baseline growth | **Conditional/accessory** | Dispensable at permissive temperature; required under stress |

### 3.3 Molecular assemblies carrying out each step

The single catalytic step is executed by different physical assemblies across life (see Section 5), but the **catalytic core is a conserved RFM domain** in every case. In bacteria the enzyme acts alone (or as a homodimer in Bacilli); in eukaryotes it requires a catalytically silent partner that stabilizes the writer and sharpens substrate discrimination.

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 TrmB (PP_5103) — the catalytic writer

TrmB is the SAM-dependent tRNA (guanine(46)-N7)-methyltransferase at the center of the module. Direct enzymatic characterization in *P. aeruginosa* — the nearest well-studied relative of *P. putida* KT2440 — established that *trmB* encodes the enzyme forming m7G46 in the variable loop ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)): *"the P. aeruginosa trmB gene encodes a tRNA guanine (46)-N7-methyltransferase that catalyzes the formation of m7G46 in the tRNA variable loop."* Crystallographic work on the *E. coli* and *B. subtilis* enzymes places TrmB firmly in the Rossmann-fold class ([PMID: 16600901](https://pubmed.ncbi.nlm.nih.gov/16600901/)): *"It reveals a unique variant of the Rossmann-fold methyltransferase (RFM) structure, with the N-terminal helix folded on the opposite site of the catalytic domain."* This is **Finding F001**.

### 4.2 Substrate recognition module

TrmB does not require an intact L-shaped tRNA. Work on *Aquifex aeolicus* TrmB ([PMID: 15358762](https://pubmed.ncbi.nlm.nih.gov/15358762/)) showed that *"the enzyme specificity was critically dependent on the size of the variable loop"* and that *"the L-shaped tRNA structure is not required for methyl acceptance activity."* The T-stem emerges as the single most important recognition element. This defines the **local variable-loop/T-stem architecture**, not global tertiary structure, as the recognition determinant (**Finding F004**), and it distinguishes TrmB from elbow-modifying enzymes (e.g., TruB, TrmA) that read the tertiary core. Consistent with a minimal catalytic requirement, the isolated **core domain** of *A. aeolicus* TrmB retains methyl-transfer activity ([PMID: 17150909](https://pubmed.ncbi.nlm.nih.gov/17150909/)), and the *E. coli* enzyme's tRNA-binding mechanism has been dissected biochemically ([PMID: 36933808](https://pubmed.ncbi.nlm.nih.gov/36933808/)).

### 4.3 Accessory subunits — the eukaryotic heterodimer

In eukaryotes the writer is catalytically inert on its own. Yeast **Trm8–Trm82** is active only when both subunits are **co-translated** ([PMID: 18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/)): *"Active Trm8-Trm82 heterodimer was only synthesized under conditions, in which both Trm8 and Trm82 mRNAs were co-translated."* The human orthologs are **METTL1–WDR4**, whose structures and catalytic mechanism have been solved ([PMID: 36599982](https://pubmed.ncbi.nlm.nih.gov/36599982/)). Importantly, **Trm82/WDR4 is dedicated to the m7G46 writer** and is *distinct* from the general activator **Trm112/TRMT112**, which partners with a different client set ([PMID: 28134793](https://pubmed.ncbi.nlm.nih.gov/28134793/): *"The last complex formed between Trm112 and Bud23 proteins modifies 18S rRNA and participates in the 40S biogenesis pathway"*; [PMID: 30010922](https://pubmed.ncbi.nlm.nih.gov/30010922/): *"Trm112 is a general partner for methyltransferases in all living organisms"*). This is the substance of **Findings F003 and F006**.

### 4.4 The network partners (context, not core)

m7G46 does not act in isolation. In *Thermus thermophilus*, m7G46 supports the deposition of **Gm18** and **m1G37** and is embedded in a modification network ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/)). The related folate/FAD-dependent enzyme **TrmFO** (m5U54) participates in the same class of temperature-tuned networks ([PMID: 27238446](https://pubmed.ncbi.nlm.nih.gov/27238446/)). These enzymes provide context; they are not members of UPA00989 itself.

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Quaternary-structure variation across lineages

The single conserved reaction is carried out by different assemblies:

| Lineage | Enzyme | Active assembly | Accessory subunit |
|---|---|---|---|
| *E. coli* (γ-proteobacteria) | TrmB (YggH) | **Monomer** | None |
| *Pseudomonas* spp. | TrmB (PP_5103 ortholog) | Monomer (by orthology) | None |
| *Bacillus subtilis* (Firmicutes) | TrmB | **Homodimer** | None |
| *Aquifex aeolicus* (thermophile) | TrmB | Monomer; extended C-terminus | None |
| *S. cerevisiae* | Trm8 | **Obligate heterodimer** | Trm82 |
| *Homo sapiens* | METTL1 | **Obligate heterodimer** | WDR4 |

The homodimerization of *B. subtilis* TrmB is explicitly lineage-specific ([PMID: 16600901](https://pubmed.ncbi.nlm.nih.gov/16600901/)): *"unlike EcTrmB, BsTrmB is shown here to be dimeric both in the crystal and in solution."* The eukaryotic heterodimer recognizes tRNA more stringently than the bacterial monomer. This spread — monomer → homodimer → obligate heterodimer — is a textbook example of **conserved chemistry with elaborated assembly** (**Finding F003**).

### 5.2 Conservation and origin

The **catalytic RFM scaffold is ancient**. Comparative and phylogenetic analyses of RNA methyltransferases indicate that several MTase catalytic domains predate the divergence of the domains of life ([PMID: 40508070](https://pubmed.ncbi.nlm.nih.gov/40508070/)): *"indicating their ancient origin in the Last Universal Common Ancestor (LUCA)."* m7G46 is one of the most broadly distributed tRNA modifications. The picture is therefore of an **ancient catalytic core** onto which **later, lineage-specific elaborations** (auxiliary domains, oligomerization, obligate partner subunits) were layered (**Finding F007**). For understanding the *ancestral* role, the **bacterial monomeric enzymes (E. coli, Pseudomonas) are the best representatives**, because they retain the minimal writer without the eukaryote-specific heterodimeric apparatus.

### 5.3 Physiological-state and cell-type variation

Because N7 methylation is chemically identical everywhere, variation is expressed mainly through **when and how much** the mark matters:

- **Thermophiles / high temperature.** In *T. thermophilus*, m7G46 is required for viability at high temperature and supports the modification network; loss lowers tRNA melting temperature and depresses protein synthesis above 70 °C ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/)).
- **Oxidative stress.** In *P. aeruginosa*, m7G rises upon H2O2 exposure and TrmB loss impairs catalase translation ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)).
- **Eukaryotic disease states.** METTL1/WDR4-mediated tRNA m7G is dysregulated in multiple cancers, where it modulates translation of oncogenic messages ([PMID: 34371184](https://pubmed.ncbi.nlm.nih.gov/34371184/), [PMID: 42010934](https://pubmed.ncbi.nlm.nih.gov/42010934/)) — a eukaryote-specific elaboration of the same core mark, retained here only as context.

### 5.4 Alternative routes

There is **no known alternative enzyme** that installs m7G46; the reaction is monopolized by the TrmB/METTL1 family. "Alternative routes" exist only at the level of the *network outcome* (tRNA stability/translation), which is buffered by other modifications and, when it fails, by tRNA-decay surveillance.

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering and dependency constraints

- **SAM must be bound before transfer** (obligate co-substrate ordering).
- **G46 must be presented in a correctly sized variable loop** for recognition; the T-stem is required for productive binding.
- **In the modification network, m7G46 acts upstream of / supports other modifications.** In *T. thermophilus*, m7G46 supports introduction of Gm18 and m1G37 ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/)): *"the m(7)G46 modification is required for cell viability at high temperatures via a tRNA modification network, in which the m(7)G46 modification supports introduction of other modifications."* This is the clearest ordering constraint in the system (**Finding F002**).

### 6.2 Failure modes

The dominant failure mode of losing m7G46 is **tRNA destabilization and surveillance-mediated decay**. In yeast, mature tRNA-Val(AAC) lacking both m7G and m5C is degraded by the **rapid tRNA decay (RTD)** pathway (Rat1/Xrn1/Met22) ([PMID: 18443146](https://pubmed.ncbi.nlm.nih.gov/18443146/)): *"mature tRNA(Val(AAC)) lacking 7-methylguanosine and 5-methylcytidine is rapidly degraded and deacylated at 37 degrees C in a trm8-Delta trm4-Delta strain."* The downstream consequence is **codon-biased translational failure**: in *P. aeruginosa*, TrmB loss selectively impairs translation of Phe- and Asp-enriched mRNAs ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)): *"loss of trmB had a strong negative effect on the translation of Phe- and Asp-enriched mRNAs"* (**Finding F005**).

```
   Loss of TrmB
        │
        ▼
   No m7G46  ──▶ reduced tRNA stability / lower Tm
        │                 │
        │                 ▼
        │        (with other losses) RTD decay of tRNA
        ▼
   Impaired deposition of Gm18, m1G37  (network effect)
        │
        ▼
   Codon-biased translation defects (Phe/Asp-rich mRNAs)
        │
        ▼
   Stress-specific phenotypes (heat >70°C; H2O2 sensitivity)
```

### 6.3 What is ruled out

- **Full L-shape requirement is ruled out**: truncated substrates lacking tertiary structure are still methylated ([PMID: 15358762](https://pubmed.ncbi.nlm.nih.gov/15358762/)).
- **Baseline essentiality is ruled out**: at permissive temperature, m7G46 loss is tolerated; essentiality is conditional on stress.
- **Shared machinery with rRNA/mRNA m7G is ruled out**: those marks are installed by distinct writers (Bud23–Trm112 / RsmG; cap and internal mRNA enzymes) ([PMID: 25489090](https://pubmed.ncbi.nlm.nih.gov/25489090/)).

---

## 7. Mechanistic Model / Consolidated Interpretation

Integrating eight findings across 28 papers yields a coherent model (**Finding F008**):

- **Core identity.** TrmB (PP_5103 ortholog) catalyzes SAM-dependent m7G46 in the tRNA variable loop ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)).
- **Enzyme class and recognition.** It is a Rossmann-fold Class I MTase that reads the variable-loop/T-stem, not the full L-shape ([PMID: 16600901](https://pubmed.ncbi.nlm.nih.gov/16600901/), [PMID: 15358762](https://pubmed.ncbi.nlm.nih.gov/15358762/)).
- **Conditional importance.** Dispensable at baseline; required under thermal/oxidative stress; acts in a cooperative modification network and gates codon-biased translation ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/), [PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)).
- **Failure surveillance.** Loss (with other modification losses) triggers rapid tRNA decay ([PMID: 18443146](https://pubmed.ncbi.nlm.nih.gov/18443146/)).
- **Evolution.** The catalytic core is LUCA-ancient, while accessory subunits (Trm82/WDR4, distinct from Trm112) and oligomerization are lineage-specific elaborations ([PMID: 40508070](https://pubmed.ncbi.nlm.nih.gov/40508070/), [PMID: 28134793](https://pubmed.ncbi.nlm.nih.gov/28134793/), [PMID: 18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/)).

In one sentence: **UPA00989 is one ancient, conserved reaction that behaves as a stress-tuned node in the tRNA-modification and quality-control network, executed by a catalytic scaffold that is universal even though its active assembly is lineage-variable.**

```
         ┌─────────────────────────────────────────────┐
         │  CORE (ancient, LUCA-level, universal)       │
         │  RFM/Class I catalytic domain + SAM          │
         │  → m7G46 on variable-loop G46                │
         └─────────────────────────────────────────────┘
                 │                     │
    lineage-specific assembly     network context
                 │                     │
   ┌─────────────┼───────────┐   ┌────┴─────────────────┐
   monomer     homodimer   heterodimer   Gm18/m1G37/m5U54 · RTD surveillance
  (E. coli/    (B. subtilis) (Trm8-Trm82, · codon-biased translation
   Pseudomonas)              METTL1-WDR4)
```

---

## 8. Evidence Base

| PMID | Title (abbreviated) | Role in this review |
|---|---|---|
| [31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/) | *TrmB, a tRNA m7G46 methyltransferase, in H2O2 resistance (P. aeruginosa)* | **Primary anchor** for enzyme identity in Pseudomonas; codon-biased translation & oxidative-stress phenotype (F001, F005) |
| [16600901](https://pubmed.ncbi.nlm.nih.gov/16600901/) | *Crystal structure of B. subtilis TrmB* | Rossmann-fold classification; lineage-specific homodimerization (F001, F003) |
| [15358762](https://pubmed.ncbi.nlm.nih.gov/15358762/) | *Substrate tRNA recognition by A. aeolicus TrmB* | Variable-loop/T-stem recognition; L-shape dispensable (F004) |
| [19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/) | *m7G46 required for viability at high temperature (T. thermophilus)* | Network node; supports other modifications; stress essentiality (F002, F008) |
| [18443146](https://pubmed.ncbi.nlm.nih.gov/18443146/) | *Degradation of hypomodified tRNAs (RTD pathway)* | Failure mode: rapid tRNA decay on m7G loss (F002) |
| [18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/) | *Yeast Trm8–Trm82 heterodimer assembly* | Obligate co-translational heterodimer in eukaryotes (F003) |
| [28134793](https://pubmed.ncbi.nlm.nih.gov/28134793/) | *Trm112, activator of translational MTases* | Distinguishes Trm112 (rRNA m7G/Bud23) from m7G46 partner (F006) |
| [30010922](https://pubmed.ncbi.nlm.nih.gov/30010922/) | *Trm112-methyltransferase holoenzymes, archaea vs eukaryotes* | Trm112 as broad multi-client activator (F006) |
| [25489090](https://pubmed.ncbi.nlm.nih.gov/25489090/) | *Bud23–Trm112 and 18S rRNA m7G1575* | Separates rRNA m7G from tRNA m7G46 (F005) |
| [40508070](https://pubmed.ncbi.nlm.nih.gov/40508070/) | *Evolutionary origins of 2′-O-MTases / RNA-MTases* | LUCA-level origin of RFM catalytic core (F007) |
| [17150909](https://pubmed.ncbi.nlm.nih.gov/17150909/) | *Core domain of A. aeolicus TrmB has methyl-transfer activity* | Minimal catalytic core suffices; thermophile C-terminal variation |
| [36933808](https://pubmed.ncbi.nlm.nih.gov/36933808/) | *Molecular mechanism of tRNA binding by E. coli TrmB* | Biochemistry of bacterial TrmB–tRNA binding |
| [36599982](https://pubmed.ncbi.nlm.nih.gov/36599982/) | *Structures and mechanisms of METTL1–WDR4* | Eukaryotic heterodimer structure (context) |
| [27238446](https://pubmed.ncbi.nlm.nih.gov/27238446/) | *TrmFO regulates other modifications at low temperature* | Modification-network context |
| [34371184](https://pubmed.ncbi.nlm.nih.gov/34371184/) | *METTL1/WDR4 tRNA m7G in cancer* | Eukaryotic disease-state elaboration (context) |

**How the evidence fits together.** The *P. aeruginosa* study ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)) is the load-bearing anchor for the *Pseudomonas* module because it is the closest relative of *P. putida* with direct enzymatic and phenotypic data. Structural biology ([PMID: 16600901](https://pubmed.ncbi.nlm.nih.gov/16600901/), [PMID: 36933808](https://pubmed.ncbi.nlm.nih.gov/36933808/)) fixes the enzyme class and recognition logic. Thermophile genetics ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/), [PMID: 17150909](https://pubmed.ncbi.nlm.nih.gov/17150909/)) reveal the network and conditional-essentiality behavior. Eukaryotic and comparative studies ([PMID: 18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/), [PMID: 28134793](https://pubmed.ncbi.nlm.nih.gov/28134793/), [PMID: 40508070](https://pubmed.ncbi.nlm.nih.gov/40508070/)) establish the ancient core and lineage-variable assembly. No paper in the set contradicts the core model; the main tension is one of *emphasis* (single reaction vs. network node).

---

## 9. Controversies and Open Questions

1. **Direct characterization of PP_5103.** The *P. putida* KT2440 enzyme itself has not been directly characterized enzymatically; the assignment rests on strong orthology to *P. aeruginosa* TrmB and *E. coli* YggH. The full substrate set, kinetics, and stress phenotypes of PP_5103 remain to be measured directly.

2. **Single reaction vs. network node.** The literature productively disagrees on framing. Atomically, UPA00989 is one reaction; physiologically, m7G46's effects are inseparable from the surrounding modification network and from tRNA-decay surveillance. Both are correct at different levels.

3. **Mechanism of "network support."** How m7G46 *facilitates* deposition of Gm18 and m1G37 is not resolved at the structural level — whether through direct conformational priming, altered folding kinetics, or thermal stabilization that keeps substrates in a competent state.

4. **Cross-organism generalization.** Much mechanistic detail comes from thermophiles (*T. thermophilus*, *A. aeolicus*) and from eukaryotes (yeast, human). Extrapolating quantitative importance to a mesophilic soil bacterium like *P. putida* should be done cautiously; the *qualitative* biochemistry is robust, but the *magnitude* of stress phenotypes may differ.

5. **Accessory-subunit logic.** Why eukaryotes require an obligate heterodimer while bacteria do not is not fully explained. The partner (Trm82/WDR4) appears to stabilize the writer and sharpen specificity, but the evolutionary driver for making it *obligate* remains an open question.

---

## 10. Limitations and Knowledge Gaps

1. **Orthology-based inference.** The strongest limitation is that **PP_5103 has not been directly characterized**. All claims about the *P. putida* enzyme rest on orthology to *P. aeruginosa* TrmB and *E. coli* YggH. While this inference is well-supported, the exact substrate set, kinetics, and knockout phenotype of *P. putida* KT2440 TrmB remain experimentally unverified.

2. **Cross-organism mixing.** Mechanistic depth comes disproportionately from thermophiles and eukaryotes. The *quantitative* magnitude of stress phenotypes in a mesophilic soil bacterium is uncertain, even if the qualitative biochemistry is robust.

3. **Network mechanism unresolved.** *How* m7G46 supports downstream modifications (Gm18, m1G37) is not mechanistically defined.

4. **Regulation of the writer.** Whether and how *trmB* expression or TrmB activity is regulated in *P. putida* under stress is unknown.

5. **No structural data for the Pseudomonas enzyme.** All available structures are from *E. coli*, *B. subtilis*, *A. aeolicus*, or the eukaryotic heterodimer.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Direct biochemical characterization of PP_5103.** Express and purify *P. putida* KT2440 TrmB; confirm SAM-dependent m7G46 activity in vitro on defined tRNA substrates; measure kinetic parameters and quaternary state (monomer vs. dimer by SEC-MALS).

2. **Substrate mapping in *P. putida*.** Use tRNA-seq / mass spectrometry or m7G-specific sequencing to enumerate the G46-bearing tRNAs actually methylated in vivo and quantify occupancy.

3. **Clean knockout phenotyping.** Construct a Δ*PP_5103* strain; assay growth under thermal stress and oxidative stress (H2O2, paraquat), and test the predicted catalase-translation / peroxide-sensitivity phenotype seen in *P. aeruginosa*.

4. **Network coupling test.** In the knockout, quantify secondary hypomodification (e.g., changes at other tRNA positions) to test whether the *T. thermophilus* "modification-network" behavior extends to a mesophile.

5. **tRNA-stability / decay assay.** Test whether m7G46 loss (alone or combined with another modification deficiency) accelerates tRNA turnover in *P. putida*, probing whether an RTD-like surveillance operates.

6. **Structural determination.** Solve a *Pseudomonas* TrmB structure (crystallography or cryo-EM) to confirm the RFM fold and map the variable-loop/T-stem recognition surface in this lineage.

7. **Codon-usage / translation profiling.** Ribosome profiling of wild-type vs. Δ*PP_5103* to test for codon-biased translational defects analogous to the Phe/Asp-enriched-message effect in *P. aeruginosa*.

---

## 12. Key References

- *TrmB, a tRNA m7G46 methyltransferase, plays a role in hydrogen peroxide resistance and positively modulates the translation of katA and katB mRNAs in Pseudomonas aeruginosa.* [PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)
- *Crystal structure of Bacillus subtilis TrmB, the tRNA (m7G46) methyltransferase.* [PMID: 16600901](https://pubmed.ncbi.nlm.nih.gov/16600901/)
- *Substrate tRNA recognition mechanism of tRNA (m7G46) methyltransferase from Aquifex aeolicus.* [PMID: 15358762](https://pubmed.ncbi.nlm.nih.gov/15358762/)
- *N7-Methylguanine at position 46 (m7G46) in tRNA from Thermus thermophilus is required for cell viability at high temperatures through a tRNA modification network.* [PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/)
- *Degradation of several hypomodified mature tRNA species in Saccharomyces cerevisiae is mediated by Met22 and the 5′-3′ exonucleases Rat1 and Xrn1.* [PMID: 18443146](https://pubmed.ncbi.nlm.nih.gov/18443146/)
- *Hetero subunit interaction and RNA recognition of yeast tRNA (m7G46) methyltransferase synthesized in a wheat germ cell-free translation system.* [PMID: 18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/)
- *Trm112, a Protein Activator of Methyltransferases Modifying Actors of the Eukaryotic Translational Apparatus.* [PMID: 28134793](https://pubmed.ncbi.nlm.nih.gov/28134793/)
- *Evolutionary insights into Trm112-methyltransferase holoenzymes involved in translation between archaea and eukaryotes.* [PMID: 30010922](https://pubmed.ncbi.nlm.nih.gov/30010922/)
- *Structural and functional studies of Bud23-Trm112 reveal 18S rRNA N7-G1575 methylation occurs on late 40S precursor ribosomes.* [PMID: 25489090](https://pubmed.ncbi.nlm.nih.gov/25489090/)
- *Evolutionary Origins and Functional Diversification of 2′-O-Methyltransferases: Insights from Phylogenetic and Structural Analysis.* [PMID: 40508070](https://pubmed.ncbi.nlm.nih.gov/40508070/)
- *The core domain of Aquifex aeolicus tRNA (m7G46) methyltransferase has the methyl-transfer activity to tRNA.* [PMID: 17150909](https://pubmed.ncbi.nlm.nih.gov/17150909/)
- *Molecular mechanism of tRNA binding by the Escherichia coli N7 guanosine methyltransferase TrmB.* [PMID: 36933808](https://pubmed.ncbi.nlm.nih.gov/36933808/)
- *Structures and mechanisms of tRNA methylation by METTL1-WDR4.* [PMID: 36599982](https://pubmed.ncbi.nlm.nih.gov/36599982/)

---

*Prepared as a commissioned review synthesis of the P. putida KT2440 UPA00989 (TrmB / m7G46) module. Direct characterization of PP_5103 is limited; the model is orthology-based and triangulated across enzymology, structural biology, and comparative genomics. Claims are anchored to primary literature, and uncertainty is flagged where extrapolation across organisms or assay systems is required.*


## Artifacts

- [OpenScientist final report](trna_m7g46_methylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](trna_m7g46_methylation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31428787
2. PMID:16600901
3. PMID:15358762
4. PMID:17150909
5. PMID:36933808
6. PMID:18029735
7. PMID:36599982
8. PMID:28134793
9. PMID:30010922
10. PMID:19934251
11. PMID:27238446
12. PMID:40508070
13. PMID:34371184
14. PMID:42010934
15. PMID:18443146
16. PMID:25489090