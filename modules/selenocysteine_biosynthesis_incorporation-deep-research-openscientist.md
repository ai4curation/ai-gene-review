---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T19:38:12.347822'
end_time: '2026-07-26T20:26:54.823517'
duration_seconds: 2922.48
template_file: templates/module_research.md.j2
template_variables:
  module_title: Selenocysteine biosynthesis and co-translational incorporation
  module_summary: A reusable module for synthesis of selenocysteyl-tRNA(Sec) and recoding
    of UGA as selenocysteine. Selenophosphate synthetase activates selenium, and seryl-tRNA
    synthetase charges tRNA(Sec) with serine. Bacteria convert Ser-tRNA(Sec) directly
    with SelA, whereas the represented eukaryotic route first phosphorylates it with
    PSTK and then uses SepSecS. The completed Sec-tRNA(Sec) is delivered by a specialized
    elongation factor to a UGA codon in a SECIS-dependent translation context.
  module_outline: "- Selenocysteine biosynthesis and incorporation\n  - 1. activated\
    \ selenium donor production\n  - Selenophosphate synthesis\n    - SelD/SEPHS2\
    \ selenide, water dikinase activity (molecular player: selenophosphate synthetase\
    \ family; activity or role: selenide, water dikinase activity)\n  - 2. tRNA(Sec)\
    \ aminoacylation with serine\n  - Ser-tRNA(Sec) synthesis\n    - SerS/SARS serine-tRNA\
    \ ligase activity on tRNA(Sec) (molecular player: seryl-tRNA synthetase family;\
    \ activity or role: serine-tRNA ligase activity)\n  - 3. conversion of Ser-tRNA(Sec)\
    \ to Sec-tRNA(Sec)\n  - Alternative Sec-tRNA(Sec) synthesis routes\n    - Alternative\
    \ versions by taxonomic implementation: Ser-tRNA(Sec) conversion route\n     \
    \ - Bacterial SelA route\n        - SelA L-seryl-tRNA(Sec) selenium transferase\
    \ activity (molecular player: bacterial SelA family; activity or role: L-seryl-tRNA(Sec)\
    \ selenium transferase activity)\n      - Eukaryotic PSTK-SepSecS route\n    \
    \    - 1. Ser-tRNA(Sec) phosphorylation\n        - PSTK-dependent phosphoseryl-tRNA(Sec)\
    \ formation\n          - PSTK L-seryl-tRNA(Sec) kinase activity (molecular player:\
    \ PSTK family; activity or role: L-seryl-tRNA(Sec) kinase activity)\n        -\
    \ 2. phosphoseryl-tRNA(Sec) selenium transfer\n        - SepSecS-dependent Sec-tRNA(Sec)\
    \ formation\n          - SepSecS phosphoseryl-tRNA(Sec) selenium transferase activity\
    \ (molecular player: SepSecS family; activity or role: O-phosphoseryl-tRNA(Sec)\
    \ selenium transferase activity)\n  - 4. SECIS-dependent UGA recoding and Sec-tRNA\
    \ delivery\n  - Alternative selenocysteine insertion systems\n    - Alternative\
    \ versions by taxonomic implementation: Selenocysteine-specific translation machinery\n\
    \      - Bacterial SelB insertion system\n        - SelB selenocysteine-specific\
    \ elongation factor activity (molecular player: SelB elongation-factor family;\
    \ activity or role: translation elongation factor activity)\n      - Eukaryotic\
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
citation_count: 31
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

Selenocysteine biosynthesis and co-translational incorporation

## Working Scope

A reusable module for synthesis of selenocysteyl-tRNA(Sec) and recoding of UGA as selenocysteine. Selenophosphate synthetase activates selenium, and seryl-tRNA synthetase charges tRNA(Sec) with serine. Bacteria convert Ser-tRNA(Sec) directly with SelA, whereas the represented eukaryotic route first phosphorylates it with PSTK and then uses SepSecS. The completed Sec-tRNA(Sec) is delivered by a specialized elongation factor to a UGA codon in a SECIS-dependent translation context.

## Provisional Biological Outline

- Selenocysteine biosynthesis and incorporation
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

# Selenocysteine Biosynthesis and Co-translational Incorporation: A System-Level Review

*Commissioned review synthesis. Search date: 2026-07-27. Citations are given as PubMed IDs (PMID).*

---

## 1. Executive Summary

Selenocysteine (Sec, U) is the 21st genetically encoded amino acid, and its production is unusual in a way that shapes the entire system built around it: **there is no aminoacyl-tRNA synthetase that charges free selenocysteine onto a tRNA.** Instead, Sec is manufactured *in situ* on its own dedicated transfer RNA, tRNA(Sec) (the *selC* gene product). Canonical seryl-tRNA synthetase first mischarges tRNA(Sec) with serine, and the seryl moiety is then chemically transformed—while still esterified to the tRNA—into selenocysteine. This tRNA-dependent amino-acid-transformation logic is the organizing principle of the whole module and the single most important fact for understanding why the pathway looks the way it does ([PMID: 17142313](https://pubmed.ncbi.nlm.nih.gov/17142313/), [PMID: 18252769](https://pubmed.ncbi.nlm.nih.gov/18252769/)).

The completed Sec-tRNA(Sec) is then delivered to the ribosome to recode an in-frame **UGA codon**—normally a stop signal—as selenocysteine. This recoding is not spontaneous: it requires a dedicated, EF-Tu-like translational GTPase and a *cis*-acting mRNA structure called the **SECIS element**. The system exists in two structurally and evolutionarily distinct implementations. Bacteria use a single pyridoxal-5′-phosphate (PLP)-dependent enzyme, **SelA**, to convert Ser-tRNA(Sec) directly to Sec-tRNA(Sec), and a single fused factor, **SelB**, that both reads the SECIS (located immediately 3′ of the UGA, within the open reading frame) and delivers the tRNA. Archaea and eukaryotes split both jobs: conversion proceeds through a phosphorylated intermediate via **PSTK** and then **SepSecS**, and decoding is divided between the SECIS-binding adaptor **SBP2/SECISBP2** (reading a SECIS relocated to the 3′ untranslated region) and the dedicated elongation factor **eEFSec/EEFSEC**.

Across five confirmed findings and 45 papers reviewed, the emerging picture is of an **ancient, tRNA(Sec)-centered core** (the elongated tRNA scaffold, its serylation, selenophosphate synthesis, and an EF-Tu-like Sec-specific GTPase—all plausibly traceable to the last universal common ancestor) onto which **two independently evolved conversion-and-delivery systems** have been grafted. Every step is individually obligatory wherever the system is present, yet the entire module is evolutionarily expendable: it has been lost repeatedly (land plants, some fungi, some algae) and is even dispensable for viability in certain protists. This review lays out the system's boundaries, its best-supported mechanistic model, its lineage-specific variation, its evolutionary origin, the physical constraints that order its steps, and the open controversies that remain.

---

## 2. Definition and Biological Boundaries

### What is included

The selenocysteine biosynthesis-and-incorporation system is, functionally, a **reusable translational module** whose input is selenium plus a UGA-containing selenoprotein mRNA, and whose output is a selenoprotein with Sec correctly installed at a defined position. It comprises four mechanistic stages:

1. **Activated selenium donor production** — selenophosphate synthetase (SelD in bacteria; SEPHS2/SPS2 in mammals) generates monoselenophosphate, the biological selenium donor, from selenide and ATP.
2. **tRNA(Sec) aminoacylation with serine** — canonical seryl-tRNA synthetase (SerS/SARS) charges tRNA(Sec) with serine, producing Ser-tRNA(Sec).
3. **Conversion of Ser-tRNA(Sec) to Sec-tRNA(Sec)** — either the bacterial one-step SelA route, or the archaeal/eukaryotic two-step PSTK→SepSecS route through an O-phosphoseryl-tRNA(Sec) intermediate.
4. **SECIS-dependent UGA recoding and Sec-tRNA delivery** — a dedicated elongation factor (SelB or eEFSec), plus in eukaryotes the SBP2 adaptor and its 3′UTR SECIS.

### What sits at the boundary and should be treated separately

- **Selenium uptake, transport, and whole-body distribution** (e.g., selenoprotein P as a selenium transporter) supplies substrate but is upstream of, and mechanistically distinct from, the biosynthesis module.
- **Selenocysteine lyase (SCLY)** and selenium recycling/catabolism are a separate degradative arm, not part of Sec synthesis.
- **The downstream selenoproteins themselves** (GPx family, thioredoxin reductases, deiodinases) and their enzymology are outputs, not part of the machinery.
- **Nonsense-mediated decay (NMD)** of selenoprotein mRNAs is a *regulatory* layer superimposed on the system that modulates output during selenium deficiency; it is not part of the biosynthetic core ([PMID: 24947499](https://pubmed.ncbi.nlm.nih.gov/24947499/), [PMID: 19076066](https://pubmed.ncbi.nlm.nih.gov/19076066/)).
- **Other tRNA-dependent amino-acid transformations** (Gln-tRNA(Gln) and Asn-tRNA(Asn) via transamidation) share the "misacylate then modify" logic but are mechanistically independent systems ([PMID: 17194933](https://pubmed.ncbi.nlm.nih.gov/17194933/)).
- **Pyrrolysine (the 22nd amino acid)**, though often mentioned alongside Sec, is directly ligated to its tRNA by pyrrolysyl-tRNA synthetase and decodes UAG *without* complex recoding machinery—a genuinely different genetic-code-expansion strategy ([PMID: 19903474](https://pubmed.ncbi.nlm.nih.gov/19903474/)).

### Competing definitions

The most consequential definitional ambiguity concerns **the size of the "selenoproteome" the system serves.** The canonical human count is 25 selenoproteins defined by a 3′UTR SECIS coupled to an in-frame UGA. Recent RIP-Seq work on SECISBP2 (the 3S-DB study) identified 1,333 SECISBP2-bound RNAs with potential SECIS function and validated novel SECIS activity for transcripts such as PDF and ATP5MJ, suggesting the recoding client set may be larger than classically defined ([PMID: 41201471](https://pubmed.ncbi.nlm.nih.gov/41201471/)). This does not change the biosynthetic machinery but does widen the definition of what the machinery acts upon.

---

## 3. Mechanistic Overview

### The best current model

```
                    [ Se donor arm ]
   selenide + ATP ──SelD/SEPHS2──▶ selenophosphate  ───────────┐
                                                               │ (selenium donor)
                                                               ▼
 tRNA(Sec)(SelC) ──SerRS──▶ Ser-tRNA(Sec)                       │
                                    │                          │
        ┌───────────────────────────┴─────────────────────────┐│
        │ BACTERIA                          EUKARYA/ARCHAEA    ││
        │                                                      ││
        │   Ser-tRNA(Sec)                    Ser-tRNA(Sec)     ││
        │        │                                │            ││
        │      SelA  ◀──selenophosphate──┐      PSTK           ││
        │  (1 step, PLP)                 │        │            ││
        │        │                       │  Sep-tRNA(Sec)      ││
        │        ▼                       │        │            ││
        │   Sec-tRNA(Sec)                └────▶ SepSecS ◀──selenophosphate
        │        │                                │
        │        │                        Sec-tRNA(Sec)
        │        ▼                                │
        │  delivery: SelB                 delivery: eEFSec
        │  (fused SECIS-reader+GTPase)    + SBP2 (SECIS adaptor)
        │  SECIS in ORF, 3′ of UGA        SECIS in 3′UTR
        └──────────────────────┬───────────────────────────────┘
                               ▼
              Ribosome: in-frame UGA recoded as Sec
```

### Obligatory, conditional, and accessory steps

- **Obligatory everywhere the system operates:** selenophosphate synthesis; serylation of tRNA(Sec); Ser→Sec conversion; a dedicated elongation factor; a SECIS element. In *Trypanosoma brucei*, null mutants of PSTK or SepSecS abolish selenoprotein synthesis, and SerRS, selenophosphate synthase, and EFSec are each individually essential to the pathway—demonstrating the non-redundant, obligatory character of each node ([PMID: 19279205](https://pubmed.ncbi.nlm.nih.gov/19279205/)).
- **Lineage-conditional (mutually exclusive routes):** the bacterial SelA one-step route *versus* the archaeal/eukaryotic PSTK→SepSecS two-step route are alternative solutions to the same chemical problem; an organism uses one or the other, not both. Likewise the SelB single-factor decoding system *versus* the split SBP2+eEFSec system.
- **Accessory/regulatory:** SBP2's obligate role is eukaryote-specific (bacteria fuse this function into SelB). Auxiliary factors such as **SECp43/SEPHS1** participate in eukaryotic complex assembly—SEPSECS, SECp43, SEPHS1 and SEPHS2 form oligomers in eukaryotic cells ([PMID: 28414460](https://pubmed.ncbi.nlm.nih.gov/28414460/))—but the pathway can be reconstituted without the full complement in minimal systems.

---

## 4. Major Molecular Players and Active Assemblies

### Finding F001 — Sec is made by tRNA-dependent transformation, not direct aminoacylation

The foundational fact of the system is that **selenocysteine has no free-amino-acid aminoacyl-tRNA synthetase.** tRNA(Sec) is first serylated by canonical seryl-tRNA synthetase, and the seryl moiety is then chemically converted while still attached to the tRNA. Bacteria accomplish this with a single PLP-dependent enzyme (SelA); archaea and eukaryotes use a two-step route in which O-phosphoseryl-tRNA(Sec) kinase (PSTK) first phosphorylates Ser-tRNA(Sec) to Sep-tRNA(Sec), the obligatory precursor that Sep-tRNA:Sec-tRNA synthase (SepSecS) then converts to Sec-tRNA(Sec) ([PMID: 17142313](https://pubmed.ncbi.nlm.nih.gov/17142313/): *"In this two-step pathway, O-phosphoseryl-tRNA(Sec) kinase (PSTK) converts Ser-tRNA(Sec) to Sep-tRNA(Sec). This misacylated tRNA is the obligatory precursor for a Sep-tRNA:Sec-tRNA synthase (SepSecS)"*). This is confirmed independently: *"In Sec-tRNA synthesis, O-phosphoseryl-tRNA kinase phosphorylates Ser-tRNA to form the intermediate which is then modified to Sec-tRNA by Sep-tRNA:Sec-tRNA synthase"* ([PMID: 18252769](https://pubmed.ncbi.nlm.nih.gov/18252769/)). The consequence is that Sec biosynthesis is inseparable from its tRNA: the tRNA is not merely an adaptor but the physical platform on which the amino acid is built.

### Finding F002 — SelA and SepSecS are structurally and evolutionarily independent Sec synthases

The two conversion enzymes are not homologs that diverged; they are distinct solutions. Bacterial **SelA** is a PLP-dependent **homodecamer** (~500 kDa, a pentamer of dimers) that binds 10 tRNA(Sec) molecules and converts Ser-tRNA(Sec) directly to Sec-tRNA(Sec) using selenophosphate. Its catalysis relies on arginine residues that are non-homologous to those of SepSecS ([PMID: 23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/): *"which revealed a ring-shaped homodecamer that binds 10 tRNA(Sec) molecules, each interacting with four SelA subunits"*). The authors explicitly conclude independent evolution: *"Different protein architecture and substrate coordination of the bacterial enzyme provide structural evidence for independent evolution of the two Sec synthesis systems present in nature."* Complementary mutagenesis shows the decamer's dimer-of-dimers arrangement is essential for productive active-site formation ([PMID: 24456689](https://pubmed.ncbi.nlm.nih.gov/24456689/)). SepSecS, by contrast, is a PLP fold-type-I **tetramer** acting on the phosphorylated intermediate. This structural divergence is the primary evidence that the Ser→Sec conversion step was "invented" at least twice.

### Finding F003 — UGA recoding requires a dedicated elongation factor and, in eukaryotes, a SECIS/SBP2 platform

Sec-tRNA(Sec) is delivered to the ribosomal A-site by a **specialized translational GTPase**: bacterial SelB or eukaryotic eEFSec/EEFSEC. Structural studies show eEFSec folds into a **chalice-like** four-domain structure, with an EF-Tu-like N-terminal core (domains 1–3) and a C-terminal **domain 4** that grips Sec-tRNA(Sec) ([PMID: 27708257](https://pubmed.ncbi.nlm.nih.gov/27708257/): *"four domains of human eEFSec fold into a chalice-like structure"*). In bacteria, SelB is a single fused factor that reads a SECIS element located immediately 3′ of the UGA *within the open reading frame*: *"The Sec-specific elongation factor SelB brings the selenocysteinyl-tRNA(Sec) ... to the ribosome, dependent on both an in-frame UGA and a Sec-insertion sequence (SECIS) in the mRNA"* ([PMID: 26304550](https://pubmed.ncbi.nlm.nih.gov/26304550/)). Eukaryotes relocated the SECIS to the 3′UTR and interposed an adaptor, SBP2/SECISBP2, which binds the SECIS and recruits eEFSec: *"SECIS binding induces a conformational change in SBP2 that recruits eEFSec"* ([PMID: 18948268](https://pubmed.ncbi.nlm.nih.gov/18948268/)). The physiological importance of this platform in humans is underscored by disease: SECISBP2 loss-of-function causes multisystem selenoprotein deficiency with abnormal thyroid hormone metabolism (elevated free T4, low free T3, normal TSH, from defective deiodinase production) ([PMID: 42238688](https://pubmed.ncbi.nlm.nih.gov/42238688/)).

### Finding F004 — The PSTK–SepSecS route is essential and non-redundant, yet the whole module is dispensable in some lineages

Two facts sit in productive tension. First, **each enzyme is non-redundant**: in *T. brucei*, null mutants of either PSTK or SepSecS abolish selenoprotein synthesis ([PMID: 19279205](https://pubmed.ncbi.nlm.nih.gov/19279205/): *"Null mutants of either PSTK or SepSecS abolished selenoprotein synthesis, demonstrating the essentiality of both enzymes for Sec-tRNA(Sec) formation"*). In mammals, SPS2/SEPHS2 knockdown severely impairs selenoprotein synthesis while SPS1/SEPHS1 knockdown does not, identifying SEPHS2 as *the* essential selenide-activating enzyme ([PMID: 17346238](https://pubmed.ncbi.nlm.nih.gov/17346238/)). Second, **the pathway as a whole is evolutionarily expendable**: in trypanosomes the knockouts grow normally, showing selenoproteins are not required for viability, and the Sec machinery has been lost repeatedly across evolution—including parallel losses among algae ([PMID: 31226841](https://pubmed.ncbi.nlm.nih.gov/31226841/): *"indicating parallel loss of Sec incorporation in different groups of algae"*). The resolution is that the module's *internal* logic is rigidly interdependent, but its *external* necessity depends on whether an organism relies on selenoproteins at all.

### Finding F005 — tRNA(Sec) is the central organizing scaffold

The non-canonical geometry of tRNA(Sec) encodes essentially all downstream recognition events, making it the true hub of the system. Mammalian tRNA(Sec) has a **long 13-bp acceptor+T-stem** (versus 12 bp in canonical tRNAs), built from a **9-bp acceptor stem** and **6-bp D-stem**; these unusual stem lengths are the key identity elements for selenocysteine synthase, while SerRS reads the 13-bp acceptor+T-stem distance ([PMID: 9870610](https://pubmed.ncbi.nlm.nih.gov/9870610/): *"Key identity elements for selenocysteine synthase are the long 9 bp AA- and long 6 bp D-stems"*). PSTK discriminates Ser-tRNA(Sec) from Ser-tRNA(Ser) using the D-arm (in eukaryotes) or specific acceptor-stem base pairs (in archaea): *"the acceptor stem base pairs G2-C71 and C3-G70 in tRNA(Sec) were crucial for discrimination from tRNA(Ser)"* ([PMID: 18267971](https://pubmed.ncbi.nlm.nih.gov/18267971/)). Because the same molecule must be a good substrate for SerRS, PSTK, SepSecS/SelA, and the elongation factor while being *rejected* by the standard ribosomal EF-Tu/eEF1A pathway, tRNA(Sec) functions as an integrating checkpoint that couples all steps.

### Summary table of molecular players

| Step | Bacteria | Archaea / Eukaryotes | Activity | Assembly |
|------|----------|----------------------|----------|----------|
| Selenium activation | SelD | SEPHS2/SPS2 | selenide,water dikinase | homodimer |
| Serylation | SerRS | SerRS/SARS | serine-tRNA ligase | canonical aaRS |
| Ser→Sec conversion | **SelA** (1 step) | **PSTK → SepSecS** (2 steps) | selenium transferase / kinase + transferase | SelA homodecamer; SepSecS tetramer |
| tRNA scaffold | tRNA(Sec)/SelC | tRNA(Sec)/SelC | identity platform | elongated acceptor/T-stem |
| SECIS recognition | fused into SelB (ORF-proximal SECIS) | SBP2/SECISBP2 (3′UTR SECIS) | SECIS binding | mRNP |
| Sec-tRNA delivery | **SelB** | **eEFSec/EEFSEC** | Sec-specific EF GTPase | EF-Tu-like + domain 4 |

---

## 5. Evolutionary and Cell-Biological Variation

### Across major lineages

The clearest axis of variation is **bacteria vs. archaea/eukaryotes**, and it applies to *both* the conversion and the delivery halves of the system:

- **Conversion:** one-step (SelA) vs. two-step (PSTK→SepSecS through a phosphoserine intermediate). These are structurally unrelated ([PMID: 23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/)).
- **Delivery/recoding:** a single fused factor reading an ORF-internal SECIS (SelB) vs. a split system with a 3′UTR SECIS, a dedicated adaptor (SBP2), and a stand-alone elongation factor (eEFSec) ([PMID: 26304550](https://pubmed.ncbi.nlm.nih.gov/26304550/), [PMID: 18948268](https://pubmed.ncbi.nlm.nih.gov/18948268/)).

Within eukaryotes, protists illustrate a **stripped-down version** of the canonical machinery. Kinetoplastids (*Trypanosoma*, *Leishmania*) possess PSTK, SepSecS, SelD/SPS, and EFSec but **lack SBP2 and SECp43**, and carry a small selenoproteome ([PMID: 24251578](https://pubmed.ncbi.nlm.nih.gov/24251578/), [PMID: 26586914](https://pubmed.ncbi.nlm.nih.gov/26586914/)). *Naegleria gruberi*, a primitive eukaryote, retains a complete set (PSTK, SepSecS, SelD/SPS2, EFSec, SBP, tRNA(Sec)/SelC), with an intriguing fused methyltransferase–SelD architecture ([PMID: 23603359](https://pubmed.ncbi.nlm.nih.gov/23603359/)). These cases show the eukaryotic delivery platform is not monolithic—the SBP2 adaptor is a later, not universal, eukaryotic feature.

### Lineage-specific losses

The system has been discarded repeatedly. Phylogenomic analysis of Archaeplastida documents parallel loss of Sec incorporation across algal groups, and Sec machinery is absent from land plants and many fungi ([PMID: 31226841](https://pubmed.ncbi.nlm.nih.gov/31226841/)). Because loss requires simultaneous elimination of an interdependent gene set, these losses are informative "natural knockouts" confirming that when selenoproteins are not needed, the entire module goes together.

### Cell-type, tissue, and physiological-state variation

Selenoprotein *output* is strongly modulated even where the machinery is intact:

- **Selenium-dependent hierarchy:** only a subset of selenoprotein mRNAs are sensitive to selenium status; GPx1 collapses to a few percent of adequate levels in deficiency while many selenoprotein mRNAs are essentially unaffected ([PMID: 19076066](https://pubmed.ncbi.nlm.nih.gov/19076066/), [PMID: 22332043](https://pubmed.ncbi.nlm.nih.gov/22332043/)). Notably, the position of the UGA codon does **not** predict susceptibility, indicating current NMD models are incomplete.
- **Tissue-specific regulation of the machinery itself:** during endotoxemia, hepatic expression of SEPHS2, PSTK, SepSecS, and SCLY falls sharply while lung, kidney, and spleen are spared—showing the Se-processing apparatus is regulated in an organ-specific manner during innate immune challenge ([PMID: 33224150](https://pubmed.ncbi.nlm.nih.gov/33224150/)).
- **Human SEPSECS specialization:** vertebrate SEPSECS carries a C-terminal α-helix 16 that is a mammalian innovation; it limits tRNA-binding stoichiometry (no more than two tRNA(Sec) per tetramer) and prevents aggregation of the complex at low tRNA concentrations—a regulatory refinement absent from archaeal orthologs, which additionally require an aminoacyl group to bind ([PMID: 39385655](https://pubmed.ncbi.nlm.nih.gov/39385655/), [PMID: 36929010](https://pubmed.ncbi.nlm.nih.gov/36929010/)).

---

## 6. Conservation, Origin, and Constraints

### Deepest plausible origin

The core of the system is ancient. The elongated tRNA(Sec) scaffold, its serylation by the universally conserved SerRS, selenophosphate synthesis, and an EF-Tu-like Sec-specific GTPase are all plausibly traceable to the **last universal common ancestor (LUCA)**. The presence of Sec decoding in all three domains, and the deep conservation of the tRNA-dependent transformation logic ([PMID: 17142313](https://pubmed.ncbi.nlm.nih.gov/17142313/)), support an early origin. In contrast, the two conversion enzymes (SelA vs. SepSecS) are structurally unrelated and were most parsimoniously "invented" separately after the domains diverged ([PMID: 23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/)). Phylogenetic analysis of PSTK shows it co-evolved precisely with SepSecS, so the two-step route behaves as a coherent evolutionary unit ([PMID: 18174226](https://pubmed.ncbi.nlm.nih.gov/18174226/)).

**Best representatives of the ancestral role:** for understanding the ancestral conversion chemistry, the archaeal SepSecS/PSTK pair is informative because it lacks the mammalian-specific regulatory α-helix and reflects a simpler tRNA-binding mode ([PMID: 39385655](https://pubmed.ncbi.nlm.nih.gov/39385655/)). For the selenophosphate synthetase family, the essential, catalytically active member is SEPHS2/SPS2, not SEPHS1—SPS1 has diverged to a non-selenium-donating role ([PMID: 17346238](https://pubmed.ncbi.nlm.nih.gov/17346238/)).

### Ordering constraints (what must precede what)

The chemistry imposes a strict, non-negotiable order:

1. **Serylation must precede conversion.** Sec is built *from* the seryl moiety; there is no free-Sec charging route ([PMID: 18252769](https://pubmed.ncbi.nlm.nih.gov/18252769/)).
2. **Phosphorylation (PSTK) must precede SepSecS.** Sep-tRNA(Sec) is the *obligatory* substrate for SepSecS; PSTK produces exactly what SepSecS consumes ([PMID: 17142313](https://pubmed.ncbi.nlm.nih.gov/17142313/)).
3. **Selenophosphate must be available before conversion.** It is the selenium donor for both SelA and SepSecS ([PMID: 23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/)).
4. **Conversion must precede delivery.** Only Sec-tRNA(Sec)—not Ser- or Sep-tRNA(Sec)—is the productive substrate for SelB/eEFSec.
5. **In eukaryotes, SECIS recognition assembles the recoding-competent mRNP that eEFSec then uses**—SBP2's SECIS binding and conformational change precede eEFSec recruitment ([PMID: 18948268](https://pubmed.ncbi.nlm.nih.gov/18948268/)).

### Mutually exclusive / substrate-specific constraints

- SelA and SepSecS routes are **mutually exclusive** within an organism.
- The dedicated Sec elongation factor **must exclude Sec-tRNA(Sec) from the canonical EF-Tu/eEF1A pathway** and vice versa; the elongated acceptor/T-stem geometry is what enforces this partition ([PMID: 9870610](https://pubmed.ncbi.nlm.nih.gov/9870610/)).
- PSTK must **reject Ser-tRNA(Ser)** to avoid phosphorylating the wrong seryl-tRNA, using tRNA(Sec)-specific base pairs as positive determinants and A5-U68 in tRNA(Ser) as an anti-determinant ([PMID: 18267971](https://pubmed.ncbi.nlm.nih.gov/18267971/)).

### Failure modes

Loss-of-function anywhere in the chain collapses selenoprotein synthesis, but the phenotypes vary. Human SECISBP2 mutations produce systemic selenoprotein deficiency dominated by thyroid-hormone abnormalities ([PMID: 42238688](https://pubmed.ncbi.nlm.nih.gov/42238688/), [PMID: 34884733](https://pubmed.ncbi.nlm.nih.gov/34884733/)). SEPSECS missense mutations destabilize and misfold the enzyme, causing severe early-onset neurological disease (progressive cerebellar/cerebral atrophy, seizures, spasticity)—with reduced protein stability, rather than lost catalytic residues, as the proximate cause ([PMID: 27576344](https://pubmed.ncbi.nlm.nih.gov/27576344/)). Impaired selenoprotein translation (e.g., of GPx4) is also implicated in ferroptosis-linked pathology ([PMID: 41931851](https://pubmed.ncbi.nlm.nih.gov/41931851/)).

---

## 7. Controversies and Open Questions

1. **How many clients does the recoding machinery actually serve?** The classical 25-selenoprotein human set rests on 3′UTR SECIS prediction, which is constrained. RIP-Seq against SECISBP2 recovered >1,300 bound RNAs and validated novel SECIS activity for non-canonical transcripts, raising the possibility of a substantially larger, partly unrecognized selenoproteome and non-canonical UGA readthrough ([PMID: 41201471](https://pubmed.ncbi.nlm.nih.gov/41201471/)). Whether these represent bona fide selenoproteins or low-efficiency readthrough events is unresolved.

2. **What determines the selenium-dependent mRNA hierarchy?** The dominant model attributes differential selenoprotein mRNA stability to NMD acting on UGA-containing transcripts, but direct measurements show the **UGA position does not predict susceptibility**, so current NMD models "cannot explain which transcripts are susceptible" ([PMID: 22332043](https://pubmed.ncbi.nlm.nih.gov/22332043/), [PMID: 19076066](https://pubmed.ncbi.nlm.nih.gov/19076066/)). Additional, unidentified transcript features must be involved.

3. **What is the precise ribosomal choreography of UGA recoding?** Structural work has yielded chalice-shaped SelB/eEFSec and a domain-4 tRNA grip ([PMID: 27708257](https://pubmed.ncbi.nlm.nih.gov/27708257/), [PMID: 26304550](https://pubmed.ncbi.nlm.nih.gov/26304550/)), and a **non-canonical elongation mechanism** at the Sec-UGA has been proposed ([PMID: 29555379](https://pubmed.ncbi.nlm.nih.gov/29555379/)). But how the factor competes kinetically with release factors at UGA, and how the 3′UTR SECIS communicates with the elongating ribosome across a long mRNA distance in eukaryotes, remain incompletely defined.

4. **How comparable are the model organisms?** Much mechanistic detail is stitched together from *E. coli* (SelA/SelB), archaea (PSTK/SepSecS enzymology), trypanosomatids (essentiality genetics), and mammals (disease, regulation). The bacterial and eukaryotic systems are **independently evolved** in their conversion and delivery halves ([PMID: 23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/)), so cross-organism extrapolation must be made cautiously—particularly regarding SECIS location, adaptor requirement, and recoding efficiency.

5. **Why is SEPSECS stoichiometry restricted, and what does it regulate?** Vertebrate SEPSECS binds at most two tRNA(Sec) despite four equivalent sites, gated by a mammalian-specific C-terminal helix ([PMID: 39385655](https://pubmed.ncbi.nlm.nih.gov/39385655/)). Whether this asymmetry tunes Sec-tRNA output in vivo, and how it integrates with SECp43/SEPHS complex assembly ([PMID: 28414460](https://pubmed.ncbi.nlm.nih.gov/28414460/)), is an open mechanistic question.

---

## 8. Limitations and Knowledge Gaps

- This review is a **literature synthesis**, not a primary data analysis; no new experiments were performed. Findings rest on the cited primary and review literature.
- **Organism mixing:** the integrated model combines data from bacteria, archaea, protists, and mammals. Where the two implementations are independently evolved, mechanistic detail from one does not transfer automatically to the other.
- **Quantitative kinetics under physiological conditions** (flux control, rate-limiting steps in vivo) are sparsely characterized; most enzyme kinetics come from reconstituted systems (e.g., archaeal PSTK Km values, [PMID: 18174226](https://pubmed.ncbi.nlm.nih.gov/18174226/)).
- **The regulatory layer (NMD, selenium hierarchy) is acknowledged but incompletely explained**, as noted above.
- The **expanded-selenoproteome claim** ([PMID: 41201471](https://pubmed.ncbi.nlm.nih.gov/41201471/)) is recent and based largely on binding/reporter assays; genome-wide proteomic confirmation of Sec incorporation into the novel candidates is still needed.

---

## 9. Proposed Follow-up Experiments / Actions

1. **Ribosome profiling at Sec-UGA codons** across selenium states to directly measure recoding efficiency versus termination, and to test which transcript features (beyond UGA position) govern the selenium-dependent mRNA hierarchy.
2. **Mass-spectrometric validation of the expanded selenoproteome:** targeted proteomics (e.g., ⁷⁵Se labeling or MS detection of Sec) on the 3S-DB candidates (PDF, ATP5MJ, others) to confirm genuine Sec incorporation versus non-productive SECISBP2 binding.
3. **Cryo-EM of the eukaryotic recoding mRNP** (SBP2–SECIS–eEFSec–Sec-tRNA(Sec) on an 80S ribosome stalled at UGA) to resolve the non-canonical elongation mechanism and the 3′UTR-to-ribosome communication geometry.
4. **Systematic reconstitution of minimal eukaryotic systems** (with and without SECp43, SBP2) to define which accessory factors are strictly required versus modulatory, informed by the naturally SBP2-lacking kinetoplastid systems.
5. **Structure/function dissection of SEPSECS stoichiometric gating**: engineered variants lacking α-helix 16 tested in mammalian cells for effects on Sec-tRNA output and selenoprotein levels, connecting the in vitro asymmetry to physiology.
6. **Comparative phylogenomics of Sec-machinery loss** to test whether the interdependent gene set is always lost coordinately, and to map the order of gene loss during pathway degeneration.

---

## 10. Key References

| PMID | Contribution |
|------|--------------|
| [17142313](https://pubmed.ncbi.nlm.nih.gov/17142313/) | Establishes the two-step PSTK→SepSecS route via Sep-tRNA(Sec) |
| [18252769](https://pubmed.ncbi.nlm.nih.gov/18252769/) | Sec built from serine on the tRNA via phosphoserine intermediate |
| [23559248](https://pubmed.ncbi.nlm.nih.gov/23559248/) | SelA decamer structure; independent evolution of the two Sec synthases |
| [24456689](https://pubmed.ncbi.nlm.nih.gov/24456689/) | Dimer-dimer pentamerization essential for SelA active-site formation |
| [26304550](https://pubmed.ncbi.nlm.nih.gov/26304550/) | Full-length bacterial SelB structure; SECIS + in-frame UGA dependence |
| [27708257](https://pubmed.ncbi.nlm.nih.gov/27708257/) | Chalice-like human eEFSec; non-canonical mechanism |
| [18948268](https://pubmed.ncbi.nlm.nih.gov/18948268/) | SBP2 SECIS-binding conformational change recruits eEFSec |
| [19279205](https://pubmed.ncbi.nlm.nih.gov/19279205/) | PSTK/SepSecS essential yet dispensable for trypanosome viability |
| [17346238](https://pubmed.ncbi.nlm.nih.gov/17346238/) | SEPHS2/SPS2 is the essential selenophosphate synthetase |
| [31226841](https://pubmed.ncbi.nlm.nih.gov/31226841/) | Repeated parallel loss of Sec incorporation across algae |
| [9870610](https://pubmed.ncbi.nlm.nih.gov/9870610/) | tRNA(Sec) non-canonical stems as identity elements |
| [18267971](https://pubmed.ncbi.nlm.nih.gov/18267971/) | PSTK tRNA(Sec) discrimination determinants |
| [18174226](https://pubmed.ncbi.nlm.nih.gov/18174226/) | Archaeal PSTK kinetics; PSTK co-evolves with SepSecS |
| [39385655](https://pubmed.ncbi.nlm.nih.gov/39385655/) | Mammalian SEPSECS α-helix 16; stoichiometric gating |
| [36929010](https://pubmed.ncbi.nlm.nih.gov/36929010/) | tRNA-dependent activation of human SepSecS |
| [28414460](https://pubmed.ncbi.nlm.nih.gov/28414460/) | SEPHS1/2, SEPSECS, SECp43 oligomeric interactions |
| [27576344](https://pubmed.ncbi.nlm.nih.gov/27576344/) | SEPSECS misfolding causes early-onset neurological disease |
| [42238688](https://pubmed.ncbi.nlm.nih.gov/42238688/) | SECISBP2 deficiency: thyroid-hormone/selenoprotein phenotype |
| [41201471](https://pubmed.ncbi.nlm.nih.gov/41201471/) | 3S-DB: possibly expanded SECISBP2-bound selenoproteome |
| [19076066](https://pubmed.ncbi.nlm.nih.gov/19076066/) / [22332043](https://pubmed.ncbi.nlm.nih.gov/22332043/) | Selenium-dependent mRNA hierarchy; UGA position not predictive |
| [24947499](https://pubmed.ncbi.nlm.nih.gov/24947499/) | NMD regulation of selenoprotein mRNAs |
| [19903474](https://pubmed.ncbi.nlm.nih.gov/19903474/) | Sec vs. pyrrolysine genetic-code-expansion strategies |
| [17194933](https://pubmed.ncbi.nlm.nih.gov/17194933/) | tRNA-dependent amino-acid modification as a general theme |
| [29555379](https://pubmed.ncbi.nlm.nih.gov/29555379/) | eEFSec role and proposed non-canonical elongation |

---

*Prepared as a commissioned review-style synthesis of the selenocysteine biosynthesis and co-translational incorporation system, drawing on 45 papers and five confirmed findings. Claims are anchored to the cited literature; areas of uncertainty are flagged explicitly throughout.*


## Artifacts

- [OpenScientist final report](selenocysteine_biosynthesis_incorporation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](selenocysteine_biosynthesis_incorporation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17142313
2. PMID:18252769
3. PMID:24947499
4. PMID:19076066
5. PMID:17194933
6. PMID:19903474
7. PMID:41201471
8. PMID:19279205
9. PMID:28414460
10. PMID:23559248
11. PMID:24456689
12. PMID:27708257
13. PMID:26304550
14. PMID:18948268
15. PMID:42238688
16. PMID:17346238
17. PMID:31226841
18. PMID:9870610
19. PMID:18267971
20. PMID:24251578
21. PMID:26586914
22. PMID:23603359
23. PMID:22332043
24. PMID:33224150
25. PMID:39385655
26. PMID:36929010
27. PMID:18174226
28. PMID:34884733
29. PMID:27576344
30. PMID:41931851
31. PMID:29555379