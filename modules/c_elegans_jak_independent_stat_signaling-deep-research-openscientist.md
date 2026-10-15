---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T07:01:04.695373'
end_time: '2026-10-04T07:14:23.728171'
duration_seconds: 799.03
template_file: templates/module_research.md.j2
template_variables:
  module_title: JAK-independent STAT signaling in Caenorhabditis elegans
  module_summary: 'Caenorhabditis elegans lacks Janus kinases, interferons and cytokine-receptor
    JAK docking, yet its two STAT-family transcription factors act in immune gene-regulatory
    pathways. STA-1 acts in intestinal antiviral immunity against Orsay virus, largely
    as a constitutive transcriptional repressor of infection-response genes, with
    the tyrosine kinase SID-3 acting genetically upstream. STA-2 acts in the epidermis,
    where it associates with hemidesmosomes and the SLC6 transporter SNF-12 and is
    required for induction of antimicrobial peptide genes such as nlp-29 after fungal
    infection or wounding. Research question: which upstream inputs, STAT post-translational
    regulation, target genes and negative regulators define each pathway, and how
    do they differ from canonical receptor-JAK-STAT signaling?'
  module_outline: "- JAK-independent STAT signaling in C. elegans\n  - Alternative\
    \ versions by STAT paralog and tissue: STAT paralog-specific pathways\n    - STA-1\
    \ intestinal antiviral pathway\n      - 1. upstream non-JAK kinase input\n   \
    \   - SID-3 tyrosine kinase input to STA-1\n      - 2. STAT transcriptional repression\
    \ of infection-response genes\n      - STA-1 repression of antiviral response\
    \ genes\n    - STA-2 epidermal antimicrobial peptide pathway\n      - 1. damage/infection\
    \ sensing and upstream signaling\n      - Hemidesmosome, SNF-12 and p38 MAPK inputs\
    \ to STA-2\n      - 2. STAT transcriptional activation of antimicrobial peptide\
    \ genes\n      - STA-2 activation of nlp-29 cluster AMP genes"
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: c_elegans_jak_independent_stat_signaling-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: c_elegans_jak_independent_stat_signaling-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

JAK-independent STAT signaling in Caenorhabditis elegans

## Working Scope

Caenorhabditis elegans lacks Janus kinases, interferons and cytokine-receptor JAK docking, yet its two STAT-family transcription factors act in immune gene-regulatory pathways. STA-1 acts in intestinal antiviral immunity against Orsay virus, largely as a constitutive transcriptional repressor of infection-response genes, with the tyrosine kinase SID-3 acting genetically upstream. STA-2 acts in the epidermis, where it associates with hemidesmosomes and the SLC6 transporter SNF-12 and is required for induction of antimicrobial peptide genes such as nlp-29 after fungal infection or wounding. Research question: which upstream inputs, STAT post-translational regulation, target genes and negative regulators define each pathway, and how do they differ from canonical receptor-JAK-STAT signaling?

## Provisional Biological Outline

- JAK-independent STAT signaling in C. elegans
  - Alternative versions by STAT paralog and tissue: STAT paralog-specific pathways
    - STA-1 intestinal antiviral pathway
      - 1. upstream non-JAK kinase input
      - SID-3 tyrosine kinase input to STA-1
      - 2. STAT transcriptional repression of infection-response genes
      - STA-1 repression of antiviral response genes
    - STA-2 epidermal antimicrobial peptide pathway
      - 1. damage/infection sensing and upstream signaling
      - Hemidesmosome, SNF-12 and p38 MAPK inputs to STA-2
      - 2. STAT transcriptional activation of antimicrobial peptide genes
      - STA-2 activation of nlp-29 cluster AMP genes

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

# JAK-Independent STAT Signaling in *Caenorhabditis elegans*: Two Tissue-Specific Pathways of Opposite Polarity

*A commissioned review-style synthesis*

---

## 1. Executive Summary

*Caenorhabditis elegans* possesses two STAT-family transcription factors, **STA-1** and **STA-2**, yet its genome encodes **no Janus kinase (JAK), no interferon, and no cytokine receptor bearing a JAK-docking module**. This creates a natural experiment: how does a metazoan deploy the ancient STAT DNA-binding fold for immune gene regulation when the canonical receptor→JAK→STAT activation machinery has been lost? The answer, synthesized here from ~22 primary studies and reviews, is that the worm has repurposed STATs into **two mechanistically distinct, tissue-restricted pathways that operate with opposite transcriptional polarity**.

In the **epidermis**, **STA-2 is a transcriptional activator** of antimicrobial peptide (AMP) genes, most prominently the *nlp-29* cluster, induced after fungal (*Drechmeria coniospora*) infection or physical wounding. Its regulation is strikingly non-JAK: STA-2 is tethered at apical **hemidesmosomes** and released upon structural damage; it binds directly to the **SLC6 transporter SNF-12**; and it sits downstream of a danger-sensing **GPCR (DCAR-1)** activated by the endogenous ligand HPLA, a conserved **p38 MAPK cassette (TIR-1–NSY-1–SEK-1–PMK-1)**, and a **TGF-β/SMA-3** input. Multiple negative regulators—including non-apoptotic **CED-3 caspase** cleavage of PMK-1 and pathogen-deployed enterotoxins that directly antagonize STA-2—keep the pathway in check.

In the **intestine**, **STA-1 acts in the opposite direction, as a constitutive repressor** of antiviral/infection-response genes; its loss *de-represses* Orsay virus-response genes and alters viral susceptibility. The non-JAK **ACK-family tyrosine kinase SID-3** acts genetically upstream, and recent work indicates regulated, infection-driven re-localization of the STAT protein. Critically, this STAT arm is molecularly separable from the parallel **RNAi (DRH-1/RIG-I-like)** antiviral branch and from the species-specific **pals/Intracellular Pathogen Response (IPR)** program. Together these two pathways show that STATs can be driven without JAKs by transporter partners, structural tethers, non-JAK tyrosine kinases, and stress-activated MAPK relays—and that the same protein fold can be wired as either activator or repressor depending on tissue context.

---

## 2. Definition and Biological Boundaries

### What is included

The system under review comprises **the two JAK-independent STAT pathways of *C. elegans***:

1. **The STA-2 epidermal AMP-activation pathway** — upstream danger sensing (DCAR-1/HPLA GPCR), the TIR-1–NSY-1–SEK-1–PMK-1 p38 cassette, TGF-β/SMA-3, hemidesmosome tethering, the SNF-12/SLC6 partner, and the downstream *nlp-29*-cluster target genes, together with their negative regulators.

2. **The STA-1 intestinal antiviral pathway** — the upstream non-JAK tyrosine kinase SID-3, STA-1 acting as a constitutive repressor of infection-response genes, and infection-driven STAT re-localization.

### Neighboring processes that should be treated separately

A central contribution of this review is to draw clean boundaries against pathways that are frequently discussed alongside—but are mechanistically distinct from—STAT signaling:

- **The pals-22/pals-25 Intracellular Pathogen Response (IPR):** a STAT-*independent* transcriptional defense program controlled by the species-specific, expanded *pals* gene family (39 members). It responds to the same Orsay virus (and to the microsporidian *Nematocida parisii*) as STA-1, which is why it is easily conflated, but it is molecularly separate (Finding F004).

- **The antiviral RNAi branch (DRH-1/RIG-I-like):** the dominant cell-intrinsic antiviral effector system in the worm, distinct from both STA-1 and the IPR.

- **Actin-based wound closure:** wounding triggers *two* genetically separable epidermal programs—a Gαq (EGL-30)–PLCβ (EGL-8)–Ca²⁺ pathway that drives Cdc42/Arp2/3 actin-dependent closure, and the p38/STA-2 antimicrobial program. Neither requires the other (Finding F006). This is a crucial scope boundary: "wound response" is not a single pathway.

- **Cross-tissue insulin peptide signaling (e.g., *ins-11*):** although *ins-11* is induced in the epidermis via p38/STA-2, insulin signaling does **not** regulate the AMP response itself; it coordinates organismal physiology ([PMID: 29405821](https://pubmed.ncbi.nlm.nih.gov/29405821/)).

### Competing definitions

The literature sometimes labels STA-1 and STA-2 as "STAT-like" rather than bona fide STATs, reflecting structural divergence—most notably, STA-1 **lacks the conserved N-terminal oligomerization domain** found in vertebrate and other invertebrate STATs ([PMID: 16873887](https://pubmed.ncbi.nlm.nih.gov/16873887/)). Whether these proteins should be called "STATs" or "STAT-like regulatory switches" is partly semantic, but it matters mechanistically because the missing domains correlate with the loss of canonical JAK-driven dimerization.

---

## 3. Mechanistic Overview

### 3.1 The STA-2 epidermal pathway (activation)

The best current model proceeds as follows:

```
 Fungal infection / wounding
            │
            ▼
   Damage-associated ligand (HPLA, tyrosine-derived)
            │
            ▼
      DCAR-1 (GPCR, epidermis)           Hemidesmosome integrity
            │                                     │
            ▼                            (structural damage releases STA-2)
   TIR-1 ─► NSY-1 ─► SEK-1 ─► PMK-1 (p38 MAPK)    │
            ▲                                      │
   (NIPI-3 upstream of SEK-1, infection-only)     │
            │                                      │
     TGF-β / SMA-3 ──────────────────────────┐    │
            │                                 ▼    ▼
            └──────────────────►   STA-2  ◄──► SNF-12 (SLC6)
                                        │
                                        ▼
                     nlp-29 cluster AMP genes ──► antimicrobial defense
                                                   (+ downstream sleep signaling)
```

**Obligatory steps:** p38/PMK-1 activity and STA-2 itself are required for *nlp-29* induction in response to both infection and wounding. The SNF-12 partner and STA-2 "function together" and are both required (Finding F001, [PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/)).

**Conditional steps:** The Tribbles-like kinase **NIPI-3** acts upstream of SEK-1 and is required **only after infection**, not after wounding—defining distinct infection-vs-wounding input routes that converge on p38 (Finding F003, [PMID: 18394898](https://pubmed.ncbi.nlm.nih.gov/18394898/)). The GPCR DCAR-1/HPLA branch provides danger sensing but is one of several inputs.

**Accessory/structural steps:** Hemidesmosome tethering is a mechanical regulatory layer—STA-2 is held inactive at hemidesmosomes and liberated upon damage, providing a direct damage-sensing route independent of classical ligand–receptor signaling (Finding F001, [PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/)).

### 3.2 The STA-1 intestinal pathway (repression)

```
   Orsay virus infection
            │
            ▼
   SID-3 (ACK-family tyrosine kinase, non-JAK) ──(genetically upstream)──┐
            │                                                            │
            ▼                                                            ▼
   STA-1 (constitutive repressor) ──┤ antiviral / infection-response genes
            │
   (loss of STA-1 → DE-REPRESSION → altered Orsay susceptibility)
            │
   infection-driven re-localization of the STAT protein (regulated dynamics)
```

Here STA-1 sets a **repressive baseline**: in the uninfected state it keeps antiviral/infection-response genes off, and its loss releases that repression (Finding F002, [PMID: 28874466](https://pubmed.ncbi.nlm.nih.gov/28874466/)). SID-3, a conserved **activated-Cdc42-associated (ACK) tyrosine kinase** also required for efficient dsRNA import, acts genetically upstream ([PMID: 22912399](https://pubmed.ncbi.nlm.nih.gov/22912399/)). A 2026 study reports viral-infection-driven, cell-intrinsic re-localization of the STAT protein, implying that STA-1 is not statically bound but is dynamically regulated during infection ([PMID: 42427644](https://pubmed.ncbi.nlm.nih.gov/42427644/)).

### 3.3 The unifying principle

Both pathways dispense with the JAK→tyrosine-phosphorylation→SH2-mediated dimerization logic of mammalian signaling. Instead:

| Canonical mammalian JAK-STAT | *C. elegans* STA-2 (epidermis) | *C. elegans* STA-1 (intestine) |
|---|---|---|
| Cytokine/interferon ligand | HPLA (endogenous); fungal/mechanical damage | Orsay virus infection |
| Cytokine receptor + JAK docking | DCAR-1 GPCR; hemidesmosome tether | (no defined receptor module) |
| JAK tyrosine kinase | **absent** — replaced by p38 MAPK cascade | **absent** — SID-3 ACK tyrosine kinase upstream |
| STAT activation mode | SNF-12 binding + release from hemidesmosomes | Unclear; infection-driven re-localization |
| Transcriptional output | **Activation** of *nlp-29* AMPs | **Repression** of antiviral genes |

---

## 4. Major Molecular Players and Active Assemblies

### STA-2 (epidermal STAT)
A STAT-family transcription factor acting cell-autonomously in the epidermis. It physically interacts with SNF-12 and associates with hemidesmosomes; its release from hemidesmosomes upon structural damage drives AMP transcription (Findings F001, F005).

### SNF-12 (SLC6 transporter)
A sodium–neurotransmitter symporter family (SLC6) member and **direct physical interactor of STA-2**. The two proteins "function together to regulate AMP gene expression in the epidermis" ([PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/)). This is one of the clearest examples of a solute-carrier transporter acting as a STAT co-regulator—an unusual, non-JAK regulatory mode.

### Hemidesmosomes
Apical epidermal attachment structures that act as a mechanosensory platform. Targeted disruption of hemidesmosomes (but not other architectural components) releases STA-2 and triggers AMP transcription, making them a structural "sensor" node of the pathway ([PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/)).

### DCAR-1 (GPCR) and HPLA
DCAR-1 is a G-protein-coupled receptor activated by the endogenous tyrosine-derived ligand **4-hydroxyphenyllactic acid (HPLA)**. It acts in the epidermis upstream of the p38 cascade to control AMP expression ([PMID: 25086774](https://pubmed.ncbi.nlm.nih.gov/25086774/))—a damage-associated-ligand danger-sensing input.

### The p38 cassette: TIR-1 → NSY-1 → SEK-1 → PMK-1
A conserved MAP kinase relay that forms the signaling backbone upstream of *nlp-29*/STA-2 and is required for responses to both infection and wounding ([PMID: 18394898](https://pubmed.ncbi.nlm.nih.gov/18394898/)). The Tribbles-like kinase **NIPI-3** acts upstream of SEK-1 specifically after infection.

### TGF-β/SMA-3
A SMAD transcription factor branch that, together with PMK-1/p38, acts on STA-2/SNF-12 to induce AMPs ([PMID: 33259791](https://pubmed.ncbi.nlm.nih.gov/33259791/)). This same study links AMP induction to organismal sleep via downstream somnogen signaling.

### STA-1 (intestinal STAT)
A STAT-family factor that lacks the conserved N-terminal oligomerization domain ([PMID: 16873887](https://pubmed.ncbi.nlm.nih.gov/16873887/)) and acts largely as a constitutive repressor of antiviral genes in the intestine ([PMID: 28874466](https://pubmed.ncbi.nlm.nih.gov/28874466/)).

### SID-3 (ACK tyrosine kinase)
A conserved activated-Cdc42-associated kinase, required for efficient dsRNA import, placed genetically upstream of STA-1 in antiviral immunity ([PMID: 22912399](https://pubmed.ncbi.nlm.nih.gov/22912399/)).

### Negative regulators
- **CED-3 caspase**: directly cleaves PMK-1/p38 to limit the epidermal stress/immune program and favor development; >300 genes are inversely regulated by CED-3 vs PMK-1, a non-apoptotic brake ([PMID: 32302544](https://pubmed.ncbi.nlm.nih.gov/32302544/)).
- **Fungal enterotoxins**: *D. coniospora* deploys antagonistic enterotoxins—one prevents STA-2 from activating AMP genes (via altered vesicle trafficking), while the other paradoxically raises nuclear STA-2 and increases defense gene expression through a surveillance mechanism ([PMID: 34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/)).

---

## 5. Evolutionary and Cell-Biological Variation

### Across lineages
Canonical JAK-STAT signaling is the dominant cytokine/interferon response system in vertebrates and is also present (with JAK) in insects such as *Drosophila*. The STAT **fold itself is ancient**, predating JAKs: the social amoeba *Dictyostelium* uses a STAT homolog (Dd-STATa) for developmental gene regulation entirely without JAKs ([PMID: 19207182](https://pubmed.ncbi.nlm.nih.gov/19207182/), [PMID: 18204858](https://pubmed.ncbi.nlm.nih.gov/18204858/)). *C. elegans* therefore represents a **JAK-less metazoan lineage** in which STATs have been retained and redeployed. This strongly supports the view that **the STAT DNA-binding/transcriptional module is the ancient, conserved core**, while JAK coupling is a later elaboration that the nematode lineage lost (or never fully adopted).

### Best representative for the ancestral role
Because Dd-STATa (*Dictyostelium*) operates without JAKs as a developmental regulator, it—and arguably the *C. elegans* STATs—are more informative about the **ancestral, JAK-independent function** of STATs than the highly derived mammalian JAK-coupled STATs. The *C. elegans* STA-1 lacking the N-terminal oligomerization domain exemplifies how lineage-specific loss of canonical STAT features accompanies loss of JAK coupling.

### Across tissues and transcriptional polarity
The sharpest intra-organismal variation is **polarity**: the epidermal STA-2 is an activator, whereas the intestinal STA-1 is a repressor. This demonstrates that STAT output is set by tissue context and partner assemblies, not intrinsic to the fold.

### Alternative routes to similar outcomes
Within antiviral defense, *C. elegans* runs at least **three parallel, molecularly distinct programs** against Orsay virus: (i) STA-1/STAT repression, (ii) DRH-1/RIG-I-like antiviral RNAi, and (iii) the pals/IPR transcriptional response. These achieve overlapping protective outcomes by different molecular means (Finding F004). Within the wound response, actin-based closure (Gαq–Ca²⁺) and p38/STA-2 immunity are parallel, separable outputs of a single insult (Finding F006).

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering constraints
- In the epidermis, **danger sensing (DCAR-1/HPLA or hemidesmosome disruption) must precede p38 activation**, which must precede STA-2-dependent transcription. SNF-12 binding is required concurrently.
- NIPI-3 acts upstream of SEK-1 and only in the infection route—so the infection-specific branch point lies above the shared SEK-1→PMK-1 core.
- In the intestine, STA-1 repression is the **default/constitutive** state; de-repression is the regulated event, inverting the usual "stimulus→activation" logic.

### Compartment- and cell-type specificity
Both pathways act **cell-autonomously** in their respective tissues (epidermis for STA-2; intestine for STA-1). The hemidesmosome-tethering mechanism is specific to the apical epidermal architecture and cannot generalize to the intestine.

### Mutual exclusivity / separability
- Actin wound closure vs p38/STA-2 immunity are mutually dispensable ([PMID: 22100061](https://pubmed.ncbi.nlm.nih.gov/22100061/)).
- The pals/IPR and RNAi programs operate independently of STA-1 ([PMID: 30640956](https://pubmed.ncbi.nlm.nih.gov/30640956/), [PMID: 37463170](https://pubmed.ncbi.nlm.nih.gov/37463170/)).
- Insulin (*ins-11*) signaling is explicitly **not** required for epidermal AMP regulation ([PMID: 29405821](https://pubmed.ncbi.nlm.nih.gov/29405821/)).

### Failure modes
- **Pathogen subversion:** *D. coniospora* enterotoxins directly block STA-2 ([PMID: 34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/)), a clear molecular failure mode of host defense.
- **Over-activation cost:** sustained immune activation impairs growth/reproduction; the IPR illustrates this immunity–development trade-off, and CED-3 cleavage of PMK-1 exists precisely to cap the epidermal program and protect development ([PMID: 37463170](https://pubmed.ncbi.nlm.nih.gov/37463170/), [PMID: 32302544](https://pubmed.ncbi.nlm.nih.gov/32302544/)).

---

## 7. Controversies and Open Questions

**Strongly supported claims.** The direct STA-2–SNF-12 interaction and their joint requirement for AMP induction ([PMID: 21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/)); hemidesmosome tethering/release of STA-2 ([PMID: 25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/)); the p38 cassette's requirement for *nlp-29* induction ([PMID: 18394898](https://pubmed.ncbi.nlm.nih.gov/18394898/)); DCAR-1/HPLA as an upstream GPCR input ([PMID: 25086774](https://pubmed.ncbi.nlm.nih.gov/25086774/)); STA-1 as a repressor whose loss de-represses antiviral genes ([PMID: 28874466](https://pubmed.ncbi.nlm.nih.gov/28874466/)); and the separability of actin closure from p38 immunity ([PMID: 22100061](https://pubmed.ncbi.nlm.nih.gov/22100061/)) are all backed by direct genetic/biochemical experiments.

**Areas of uncertainty and indirect evidence.**
- **STAT post-translational regulation is poorly defined.** Without a JAK, how is STA-2 "activated" at the molecular level after release from hemidesmosomes? Is tyrosine phosphorylation involved at all, and if so, by which kinase? Whether SID-3 directly phosphorylates STA-1, or acts indirectly, remains genetically inferred rather than biochemically proven.
- **The exact nature of SID-3→STA-1 coupling** is "genetically upstream" but the biochemical link is unestablished.
- **Infection-driven STA-1 re-localization** ([PMID: 42427644](https://pubmed.ncbi.nlm.nih.gov/42427644/)) is newly reported; its functional consequences for the repressor-to-derepressor transition need mechanistic dissection.
- **Cross-organism extrapolation risk.** Much of the "JAK-independent STAT" framing borrows intuition from mammalian JAK-STAT and from *Dictyostelium*; these systems are not directly comparable, and claims should not be generalized across them without care.

**Most important open questions.**
1. What is the biochemical activation switch for STA-2 and STA-1 in the absence of JAK?
2. How does one STAT fold achieve opposite polarity (activator vs repressor) across tissues—co-factor swap, target-site context, or distinct post-translational states?
3. Is there any residual tyrosine-phosphorylation logic (via SID-3 or another non-JAK kinase), or is STAT regulation here entirely localization/partner-based?
4. How do the parallel antiviral arms (STA-1, RNAi, IPR) integrate or compete during a single Orsay infection?

---

## 8. Key References

| PMID | Short title | Role in this review |
|---|---|---|
| [21575913](https://pubmed.ncbi.nlm.nih.gov/21575913/) | *Unusual regulation of a STAT protein by an SLC6 family transporter* | Direct STA-2–SNF-12 interaction; non-JAK regulation (F001) |
| [25692704](https://pubmed.ncbi.nlm.nih.gov/25692704/) | *Structural damage causes release of STA-2* | Hemidesmosome tethering/release of STA-2 (F001) |
| [28874466](https://pubmed.ncbi.nlm.nih.gov/28874466/) | *An Alternative STAT Signaling Pathway Acts in Viral Immunity* | STA-1 as repressor; alternative antiviral STAT pathway (F002) |
| [22912399](https://pubmed.ncbi.nlm.nih.gov/22912399/) | *Conserved tyrosine kinase promotes import of silencing RNA* | SID-3 ACK kinase, non-JAK upstream input (F002) |
| [16873887](https://pubmed.ncbi.nlm.nih.gov/16873887/) | *C. elegans STAT: evolution of a regulatory switch* | STA-1 lacks N-terminal oligomerization domain (F002) |
| [18394898](https://pubmed.ncbi.nlm.nih.gov/18394898/) | *Distinct innate immune responses to infection and wounding* | p38 cassette + NIPI-3 infection/wound split (F003) |
| [25086774](https://pubmed.ncbi.nlm.nih.gov/25086774/) | *Activation of a GPCR by its endogenous ligand* | DCAR-1/HPLA danger sensing upstream of p38 (F003) |
| [33259791](https://pubmed.ncbi.nlm.nih.gov/33259791/) | *Innate Immunity Promotes Sleep through Epidermal AMPs* | PMK-1 + TGF-β/SMA-3 on STA-2/SNF-12 (F003) |
| [30640956](https://pubmed.ncbi.nlm.nih.gov/30640956/) | *Antagonistic paralogs control growth vs pathogen resistance* | pals-22/pals-25 IPR, STAT-independent (F004) |
| [37463170](https://pubmed.ncbi.nlm.nih.gov/37463170/) | *Multiple pals gene modules control immunity vs development* | IPR responds to Orsay + microsporidia, distinct from STAT (F004) |
| [32302544](https://pubmed.ncbi.nlm.nih.gov/32302544/) | *Non-Canonical Caspase Activity Antagonizes p38 MAPK* | CED-3 cleaves PMK-1, negative regulation (F005) |
| [34166401](https://pubmed.ncbi.nlm.nih.gov/34166401/) | *Antagonistic fungal enterotoxins intersect host defences* | Pathogen enterotoxins antagonize STA-2 (F005) |
| [22100061](https://pubmed.ncbi.nlm.nih.gov/22100061/) | *A Gαq-Ca²⁺ pathway promotes actin-mediated wound closure* | Actin closure separable from p38/STA-2 immunity (F006) |
| [42427644](https://pubmed.ncbi.nlm.nih.gov/42427644/) | *Viral infection drives cell-intrinsic re-localization of STAT* | Regulated STA-1 dynamics during infection (F002) |
| [29405821](https://pubmed.ncbi.nlm.nih.gov/29405821/) | *Modulatory upregulation of an insulin peptide gene* | ins-11 via STA-2 but insulin not needed for AMP (scope) |
| [19207182](https://pubmed.ncbi.nlm.nih.gov/19207182/) | *Dd-STATa regulates expansin-like gene in Dictyostelium* | JAK-independent STAT ancestry (evolution) |
| [18204858](https://pubmed.ncbi.nlm.nih.gov/18204858/) | *GBF-dependent suppressors of Dictyostelium STATa* | Ancient STAT developmental role (evolution) |
| [33992157](https://pubmed.ncbi.nlm.nih.gov/33992157/) | *Innate immunity in C. elegans* | Authoritative overview/context |

---

## 9. Limitations and Knowledge Gaps

This synthesis rests primarily on *C. elegans* genetics with select biochemistry; the **biochemical activation mechanism of both STATs in the absence of JAK remains the central gap**. Key unknowns include: (i) whether and how STA-2 and STA-1 are post-translationally modified to switch states; (ii) the direct substrate relationship (if any) between SID-3 and STA-1; (iii) the molecular basis of the activator-vs-repressor polarity difference; and (iv) how the newly reported STA-1 re-localization maps onto de-repression. Evolutionary claims draw on *Dictyostelium* and mammalian comparisons that are instructive but not directly comparable, and should be read as framing rather than proof. Finally, the STA-1 arm is less deeply characterized than the STA-2 arm, so the apparent symmetry of "two opposite pathways" may partly reflect uneven experimental coverage.

---

## 10. Proposed Follow-up Experiments

1. **Define the STA-2 activation switch:** phosphoproteomics / targeted mutagenesis of candidate tyrosines on STA-2 before and after hemidesmosome disruption; test whether any non-JAK tyrosine kinase (e.g., an ACK/FER-family member) phosphorylates STA-2.
2. **Test SID-3→STA-1 directness:** in-vitro kinase assays with recombinant SID-3 and STA-1; epistasis with SID-3 catalytic-dead alleles; map STA-1 modification sites.
3. **Dissect polarity:** ChIP-seq / CUT&RUN for STA-1 and STA-2 to compare occupancy and co-factor recruitment at activated vs repressed targets; swap tissue expression to ask whether polarity follows the factor or the tissue.
4. **Integrate antiviral arms:** systematic epistasis among STA-1, DRH-1/RNAi, and pals/IPR during a single Orsay infection to define hierarchy and redundancy.
5. **Resolve re-localization function:** live imaging of tagged STA-1 during infection coupled to nascent-transcription readouts to connect localization dynamics to de-repression kinetics.

---

*Prepared as a review-style synthesis of JAK-independent STAT signaling in* C. elegans*. Mechanistic claims are attributed to the primary literature cited above; uncertainty is flagged explicitly in Sections 7 and 9.*


## Artifacts

- [OpenScientist final report](c_elegans_jak_independent_stat_signaling-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](c_elegans_jak_independent_stat_signaling-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29405821
2. PMID:16873887
3. PMID:21575913
4. PMID:18394898
5. PMID:25692704
6. PMID:28874466
7. PMID:22912399
8. PMID:42427644
9. PMID:25086774
10. PMID:33259791
11. PMID:32302544
12. PMID:34166401
13. PMID:19207182
14. PMID:18204858
15. PMID:22100061
16. PMID:30640956
17. PMID:37463170