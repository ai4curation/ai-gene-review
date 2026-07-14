---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-14T07:02:28.385550'
end_time: '2026-07-14T07:16:43.092511'
duration_seconds: 854.71
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial lipoprotein maturation
  module_summary: A species-neutral bacterial envelope-biogenesis module for the ordered
    maturation of lipobox-containing prolipoproteins by Lgt diacylglyceryl transfer,
    LspA signal peptide cleavage, and Lnt or lineage-equivalent N-acylation where
    triacylated lipoproteins are produced. Pseudomonas putida KT2440 provides the
    current UniProt exemplars for the canonical diderm Lgt-LspA-Lnt route; Lol sorting
    and substrate-specific lipoprotein functions are downstream context outside this
    module.
  module_outline: "- Bacterial lipoprotein maturation\n  - 1. Diacylglyceryl transfer\
    \ to prolipoprotein cysteine\n  - Lgt diacylglyceryl transfer\n    - Lgt family:\
    \ prolipoprotein diacylglyceryl transferase (molecular player: prolipoprotein\
    \ diacylglyceryl transferase family; activity or role: phosphatidylglycerol-prolipoprotein\
    \ diacylglyceryl transferase activity)\n  - 2. Signal peptide cleavage from diacylglyceryl-prolipoprotein\n\
    \  - LspA signal peptide cleavage\n    - LspA family: signal peptidase II (molecular\
    \ player: lipoprotein signal peptidase family; activity or role: aspartic-type\
    \ endopeptidase activity)\n  - 3. Terminal N-acylation of apolipoprotein\n  -\
    \ Lnt N-acylation\n    - Lnt family: apolipoprotein N-acyltransferase (molecular\
    \ player: apolipoprotein N-acyltransferase family; activity or role: N-acyltransferase\
    \ activity)"
  module_connections: '- Lgt diacylglyceryl transfer precedes LspA signal peptide
    cleavage

    - LspA signal peptide cleavage precedes Lnt N-acylation'
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
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_lipoprotein_maturation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_lipoprotein_maturation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial lipoprotein maturation

## Working Scope

A species-neutral bacterial envelope-biogenesis module for the ordered maturation of lipobox-containing prolipoproteins by Lgt diacylglyceryl transfer, LspA signal peptide cleavage, and Lnt or lineage-equivalent N-acylation where triacylated lipoproteins are produced. Pseudomonas putida KT2440 provides the current UniProt exemplars for the canonical diderm Lgt-LspA-Lnt route; Lol sorting and substrate-specific lipoprotein functions are downstream context outside this module.

## Provisional Biological Outline

- Bacterial lipoprotein maturation
  - 1. Diacylglyceryl transfer to prolipoprotein cysteine
  - Lgt diacylglyceryl transfer
    - Lgt family: prolipoprotein diacylglyceryl transferase (molecular player: prolipoprotein diacylglyceryl transferase family; activity or role: phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity)
  - 2. Signal peptide cleavage from diacylglyceryl-prolipoprotein
  - LspA signal peptide cleavage
    - LspA family: signal peptidase II (molecular player: lipoprotein signal peptidase family; activity or role: aspartic-type endopeptidase activity)
  - 3. Terminal N-acylation of apolipoprotein
  - Lnt N-acylation
    - Lnt family: apolipoprotein N-acyltransferase (molecular player: apolipoprotein N-acyltransferase family; activity or role: N-acyltransferase activity)

## Known Relationships Among Steps

- Lgt diacylglyceryl transfer precedes LspA signal peptide cleavage
- LspA signal peptide cleavage precedes Lnt N-acylation

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

# Bacterial Lipoprotein Maturation: The Lgt–LspA–Lnt Module

*A commissioned review-style synthesis of the ordered inner-membrane pathway that lipidates lipobox-containing prolipoproteins in bacteria. Pseudomonas putida KT2440 and Escherichia coli exemplify the canonical diderm route; Lol sorting and substrate-specific lipoprotein functions are treated as downstream context.*

---

## 1. Executive Summary

Bacterial lipoprotein maturation is a compact, strictly ordered enzymatic module that converts a newly translocated, lipobox-containing prolipoprotein into a membrane-anchored, lipidated mature protein. The module comprises three inner-membrane reactions performed in an obligatory sequence: (i) **Lgt** (phosphatidylglycerol:prolipoprotein diacylglyceryl transferase) recognizes the conserved **lipobox** and transfers a diacylglyceryl group from phosphatidylglycerol onto the thiol of an invariant cysteine; (ii) **LspA** (signal peptidase II) then cleaves the signal peptide immediately upstream of that modified cysteine, exposing a new N-terminal S-diacylglyceryl-cysteine (the **apolipoprotein**); and (iii) **Lnt** (apolipoprotein N-acyltransferase), where present, adds a third acyl chain to the free α-amino group of that cysteine to yield the fully **triacylated** mature lipoprotein. The ordering is not regulatory but substrate-logical: each enzyme acts only on the product of the preceding one.

Two features define the biological boundaries and the intellectual interest of the system. First, the **Lgt→LspA core is near-universal and essential**: Lgt is present in all bacteria and absent from archaea, and its depletion permeabilizes the Gram-negative outer membrane and is typically lethal. Second, the **terminal N-acylation step is evolutionarily variable**. Canonical Lnt operates in diderm (Gram-negative) bacteria and in high-GC Gram-positives (Actinobacteria, including mycobacteria — though via a distinct enzyme in the *ppm* operon), whereas low-GC Gram-positives (Firmicutes) lack canonical Lnt yet still modify the N-terminus, producing lyso-form, N-acetyl, and diacyl end-products through non-orthologous enzymes such as the intramolecular transacylase **Lit**. This makes lipoprotein maturation an unusually clean example of a conserved catalytic backbone with a lineage-swappable terminal module.

The three core enzymes are mechanistically well characterized by crystallography and biochemistry: Lgt is a lateral-access integral membrane transferase with essential arginines (Arg143, Arg239); LspA is an intramembrane aspartyl peptidase inhibited by the natural products globomycin and myxovirescin acting as tetrahedral-intermediate mimics; and Lnt is a nitrilase-superfamily enzyme running a ping-pong mechanism through a Cys387 thioester acyl-enzyme intermediate on a Cys–Glu–Glu catalytic triad. All three are actively pursued antimicrobial targets. Maturation ends at the lipid-anchored cysteine; the downstream **Lol** sorting system and substrate-specific lipoprotein functions are separate pathways that recognize the mature lipid anchor but lie outside this module.

---

## 2. Definition and Biological Boundaries

### 2.1 What is included

The maturation module is defined by three sequential, membrane-embedded catalytic steps acting on a defined class of substrate — proteins bearing a **lipobox** motif (canonically [LVI]-[ASTVI]-[GAS]-**C**, with the cysteine being the invariant lipidation site) within an N-terminal signal sequence. The included reactions are:

1. **Diacylglyceryl transfer** to the prolipoprotein cysteine thiol (Lgt).
2. **Signal peptide cleavage** N-terminal to the modified cysteine (LspA).
3. **N-acylation** of the resulting free α-amino group (Lnt or a lineage equivalent), *where triacylated products are made*.

The substrate enters the module after Sec- (or Tat-) dependent translocation places the prolipoprotein at the periplasmic/extracytoplasmic face of the inner membrane with its signal sequence still attached. The module's product is a lipid-anchored mature lipoprotein whose N-terminal cysteine carries two (di-acyl/apolipoprotein form) or three (tri-acyl form) acyl chains.

### 2.2 What is adjacent and often conflated

- **Lol-dependent sorting and targeting.** After maturation, Gram-negative lipoproteins are triaged for retention on the inner membrane or trafficking to the outer membrane or cell surface. The **LolCDE** ABC transporter extracts outer-membrane-destined lipoproteins from the inner membrane, **LolA** chaperones them across the periplasm, and **LolB** inserts them into the outer membrane ([PMID: 33667939](https://pubmed.ncbi.nlm.nih.gov/33667939/); [PMID: 27720009](https://pubmed.ncbi.nlm.nih.gov/27720009/)). The Lol machinery *recognizes the lipid anchor produced by maturation* but is a distinct downstream pathway and should not be treated as part of the maturation module.
- **Sec/Tat translocation** delivers the substrate but is a general protein-export system, not lipoprotein-specific.
- **Substrate-specific lipoprotein functions** (e.g., Braun's lipoprotein Lpp cross-linking to peptidoglycan, nutrient capture, TLR2 signaling) are consequences of the mature product, not steps in its production.

### 2.3 Competing definitions

There is broad agreement on the three-step core, and authoritative reviews explicitly separate "maturation" from "sorting and targeting" ([PMID: 33667939](https://pubmed.ncbi.nlm.nih.gov/33667939/)). The principal definitional tension concerns **the third step**: whether "maturation" should be defined narrowly as the canonical Lnt-catalyzed N-acylation (in which case many Firmicutes "lack step 3") or broadly as "whatever N-terminal modification follows LspA cleavage" (in which case lyso-form, N-acetyl, and diacyl end-states are all legitimate terminal outcomes). This review adopts the broad, species-neutral definition: the terminal step is **N-terminal cysteine modification**, achieved by Lnt in some lineages and by non-orthologous enzymes or not at all in others.

---

## 3. Mechanistic Overview

### 3.1 The best current model of the sequence

```
 Prolipoprotein (Sec-translocated, signal peptide + lipobox-Cys)
        |
        |  [1] Lgt  — phosphatidylglycerol:prolipoprotein diacylglyceryl transferase
        |     transfers diacylglyceryl (DAG) from phosphatidylglycerol
        |     onto the invariant lipobox cysteine thiol (thioether bond)
        v
 Diacylglyceryl-prolipoprotein  (signal peptide still attached)
        |
        |  [2] LspA  — signal peptidase II (aspartyl intramembrane peptidase)
        |     cleaves the signal peptide immediately N-terminal to the
        |     modified cysteine
        v
 Apolipoprotein  =  N-terminal S-diacylglyceryl-cysteine (free alpha-amino group)
        |
        |  [3] Lnt  — apolipoprotein N-acyltransferase (diderms, high-GC Gram+)
        |     transfers a third acyl group from a phospholipid onto the
        |     free alpha-amino group (amide bond)
        v
 Mature triacylated lipoprotein  ->  (downstream: Lol sorting, function)
```

The ordering is enforced by substrate specificity rather than by regulation: LspA requires the diacylglyceryl-modified cysteine as part of its substrate, and Lnt requires the *free α-amino group* that only appears after LspA cleavage. Thus **Lgt precedes LspA, and LspA precedes Lnt** — an intrinsic dependency chain confirmed across structural and biochemical studies ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)).

### 3.2 Obligatory, conditional, and accessory steps

| Step | Enzyme | Status | Basis |
|---|---|---|---|
| 1. Diacylglyceryl transfer | Lgt | **Obligatory & essential** | Present in all bacteria; depletion permeabilizes OM and is lethal in most Gram-negatives |
| 2. Signal peptide cleavage | LspA | **Obligatory** in the canonical route | Required to generate the apolipoprotein N-terminus; top antimicrobial target |
| 3. N-acylation | Lnt / Lit / Ppm2 | **Conditional / lineage-variable** | Canonical Lnt essential in many diderms; absent in low-GC Gram-positives where alternative enzymes or no third acyl chain occur |

Step 3 is the conditional step: whether a third acyl chain is added, and by what chemistry, depends on the lineage (see Section 5).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 Lgt — the committed first step

Lgt catalyzes the committed, universal first reaction (**Finding F002**). Crystal structures of *E. coli* Lgt (1.6–1.9 Å) captured with phosphatidylglycerol and palmitic acid reveal **two distinct binding sites** and a **lateral-access architecture**: both the phospholipid substrate and the lipid-modified product enter and leave the enzyme laterally, relative to the plane of the bilayer, rather than through an aqueous channel. Complementation of *lgt*-knockout cells with mutant variants identified **Arg143 and Arg239 as essential catalytic residues** for diacylglyceryl transfer: *"Complementation results of lgt-knockout cells with different mutant Lgt variants revealed critical residues, including Arg143 and Arg239, that are essential for diacylglyceryl transfer"* ([PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)).

Two facts anchor Lgt's central role. First, it is **essential and universal**: evolutionary analysis shows *"Lgt is present in all bacteria and absent from archaea"* ([PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)). Second, loss of Lgt has severe envelope consequences — in a clinical uropathogenic *E. coli* strain, Lgt depletion permeabilizes the outer membrane and increases sensitivity to serum killing and antibiotics, and the first-described Lgt inhibitor (G2824) is insensitive to resistance from deletion of Braun's lipoprotein ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)). The mechanism of phosphatidylglycerol activation by Lgt has been dissected structurally ([PMID: 31340643](https://pubmed.ncbi.nlm.nih.gov/31340643/)), and the "arm" and "head" domains of this highly conserved enzyme contribute to functional diversity among pathogens ([PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)).

### 4.2 LspA — the aspartyl intramembrane peptidase

LspA (signal peptidase II) cleaves the signal peptide from the diacylglyceryl-prolipoprotein (**Finding F003**). A crystal structure of *Pseudomonas aeruginosa* LspA bound to the antibiotic **globomycin** (2.8 Å), combined with mutagenesis, established LspA as an **aspartyl (aspartic-type) peptidase**, and showed that globomycin inhibits by **molecular mimicry**: *"Mutagenesis studies identify LspA as an aspartyl peptidase. In an example of molecular mimicry, globomycin appears to inhibit by acting as a noncleavable peptide that sterically blocks the active site"* ([PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)).

A striking case of chemical convergence reinforces the mechanism: structures of *Staphylococcus aureus* LspA complexed with two chemically distinct natural products — globomycin and **myxovirescin** (antibiotic TA) — show that *"they appear to inhibit identically as non-cleavable tetrahedral intermediate analogs. Remarkably, the two antibiotics superpose along nineteen contiguous atoms that interact similarly with LspA"* ([PMID: 31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/)). Independent genetic work confirmed LspA as the molecular target of myxovirescin, isolated by both resistance mapping and overexpression suppression ([PMID: 22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/)). Because LspA is highly conserved and druggable, it has been argued to be a **top-priority target** for novel antibacterials ([PMID: 31036406](https://pubmed.ncbi.nlm.nih.gov/31036406/)).

### 4.3 Lnt — the N-acyltransferase and its ping-pong mechanism

Lnt performs the terminal N-acylation in the canonical route (**Finding F004**). It is a nitrilase-superfamily enzyme with a **Cys–Glu–Glu catalytic triad** and operates by a **two-step ping-pong mechanism** through a covalent acyl-enzyme intermediate. Biochemically, *E. coli* Lnt forms a **palmitoyl thioester with the active-site Cys387**: *"the Lnt reaction proceeds through an acyl-enzyme intermediate in which a palmitoyl group forms a thioester bond with the thiol of the active site residue C387"* ([PMID: 20000742](https://pubmed.ncbi.nlm.nih.gov/20000742/)). The thioester is cleavable by neutral hydroxylamine, and the C387A substitution abolishes both intermediate formation and activity. Within the triad, Glu267 promotes formation of the intermediate by enhancing the nucleophilicity of Cys387, while a set of residues (Trp237, Tyr388, Glu389) act in the second (N-acyl transfer) step.

Kinetic analysis using **phosphatidylethanolamine** as acyl donor and the synthetic lipopeptide **FSL-1** as acceptor is *"consistent with a ping-pong type mechanism, demonstrating slow acyl-enzyme intermediate formation and rapid N-acyl transfer to the apolipopeptide in vitro"*, with strong dependence on phospholipid headgroup and acyl-chain identity ([PMID: 21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/)). Lnt exists as an **extracytoplasmic (periplasmic-facing) acyl-enzyme intermediate** ([PMID: 20000742](https://pubmed.ncbi.nlm.nih.gov/20000742/)), consistent with N-acylation occurring on the outer face of the inner membrane. Mutagenesis further shows that residues on membrane-embedded flexible periplasmic and cytoplasmic loops are required specifically for the **second step** of the reaction ([PMID: 25471278](https://pubmed.ncbi.nlm.nih.gov/25471278/)). The structural basis of Lnt-catalyzed N-acylation has been solved ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)).

### 4.4 Summary table of core players

| Enzyme | Reaction | Catalytic class / key residues | Product | Distribution | Inhibitors / tools |
|---|---|---|---|---|---|
| **Lgt** | S-diacylglyceryl transfer from PG | Membrane transferase; Arg143, Arg239; two lipid sites, lateral access | Diacylglyceryl-prolipoprotein | All bacteria; absent in archaea | G2824 |
| **LspA** | Signal peptide cleavage | Aspartyl intramembrane peptidase | Apolipoprotein (S-diacylglyceryl-Cys) | Near-universal | Globomycin, myxovirescin |
| **Lnt** | N-acylation (amide) | Nitrilase superfamily; Cys387–Glu267–Glu389 triad; ping-pong | Triacylated lipoprotein | Diderms + high-GC Gram+ | — |
| **Lit** (alt.) | Intramolecular acyl migration | 4-TM; two catalytic His; 8-membered ring intermediate | Lyso-form lipoprotein | Low-GC Gram+ (some) | — |
| **Ppm2** (alt.) | N-acylation | Distinct from canonical Lnt; *ppm* operon | Triacylated mycobacterial lipoprotein | Actinobacteria/mycobacteria | — |

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 A conserved core with a swappable terminal module

The two upstream steps constitute a deeply conserved backbone (**Findings F002, F005**). **Lgt is present in all bacteria and absent from archaea** ([PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)), and LspA is likewise near-universal. The terminal N-acylation step, by contrast, is the locus of nearly all evolutionary variation. **Lnt homologues are found in Gram-negative and high-GC Gram-positive (Actinobacteria) bacteria but not in low-GC Gram-positive (Firmicutes) bacteria** — as reported: *"Lnt homologues are found in Gram-negative and high GC-rich Gram-positive, but not in low GC-rich Gram-positive bacteria, although N-acylation is observed"* ([PMID: 24093492](https://pubmed.ncbi.nlm.nih.gov/24093492/)). This is a clear case of a conserved catalytic backbone with a lineage-swappable third module.

### 5.2 High-GC Gram-positives: N-acylation by a distinct enzyme

Mycobacteria produce **triacylated, N-acylated** lipoproteins, but the responsible enzyme is not a canonical Lnt orthologue. In slow-growing mycobacteria, N-acylation is carried out by **BCG_2070c** (mycobacterial Ppm2), and the substrate for N-acylation is a C16 fatty acid ([PMID: 24093492](https://pubmed.ncbi.nlm.nih.gov/24093492/); [PMID: 19661058](https://pubmed.ncbi.nlm.nih.gov/19661058/)). Ppm2 is part of the **ppm operon**; in *Corynebacterium glutamicum*, Cg-Ppm1 (a polyprenol-monophosphomannose synthase) and Cg-Ppm2 (the Lnt-equivalent) operate in a common biosynthetic pathway in which lipoprotein **N-acylation and O-glycosylation are tightly coupled** ([PMID: 23029442](https://pubmed.ncbi.nlm.nih.gov/23029442/)). Thus the same end-product (triacylated lipoprotein) is reached by a molecularly distinct route in Actinobacteria.

### 5.3 Low-GC Gram-positives: alternative end-products and the Lit enzyme

In Firmicutes, which lack canonical Lnt, the N-terminal cysteine adopts **structurally heterogeneous** end-states (**Findings F005, F006**). Mass spectrometry identified a **novel "lyso" structure — N-acyl-S-monoacyl-glyceryl-cysteine —** in several species: *"we identified a novel and unique bacterial lipoprotein structure containing an N-acyl-S-monoacyl-glyceryl-cysteine (named the lyso structure) from low-GC gram-positive Enterococcus faecalis, Bacillus cereus, Streptococcus sanguinis, and Lactobacillus bulgaricus"* ([PMID: 22303020](https://pubmed.ncbi.nlm.nih.gov/22303020/)). Alongside the lyso form, **N-acetyl (N-acetyl-S-diacyl-glyceryl-cysteine)** structures occur, and the acylation state is variable and even **strain-specific**.

Crucially, the lyso-form is **not** made by an Lnt-type intermolecular transfer. It is produced by a **lipoprotein intramolecular transacylase (Lit)** ([PMID: 28320885](https://pubmed.ncbi.nlm.nih.gov/28320885/)); as established, *"Bacterial lyso-form lipoproteins are synthesized via an intramolecular acyl chain migration"* ([PMID: 32471867](https://pubmed.ncbi.nlm.nih.gov/32471867/)). The *B. cereus* Lit crystal structure reveals four transmembrane helices with an extracellular cap and two catalytic histidines; *"The reaction involves acyl transfer from the sn-2 position of the glyceryl moiety to the amino group on the N-terminal cysteine of the substrate via an 8-membered ring intermediate"* — a **unimolecular acyl migration** rather than transfer from an external phospholipid donor ([PMID: 34253723](https://pubmed.ncbi.nlm.nih.gov/34253723/)). Lit is biologically consequential and mobile: its expression can be **copper-induced and horizontally transmissible**, and lyso-form conversion alters (reduces) the immunogenicity of lipoproteins by modulating the **TLR2** response ([PMID: 30988036](https://pubmed.ncbi.nlm.nih.gov/30988036/)).

### 5.4 Immunological and compartmental consequences

The N-terminal acylation state is the principal determinant of lipoprotein recognition by the host innate immune system: triacylated lipoproteins signal through TLR2/TLR1 heterodimers and diacylated/lyso forms through TLR2/TLR6, so lineage variation in step 3 has direct consequences for host–pathogen interaction ([PMID: 32723923](https://pubmed.ncbi.nlm.nih.gov/32723923/); [PMID: 22303020](https://pubmed.ncbi.nlm.nih.gov/22303020/)). Compartmentally, all three canonical reactions occur at the inner (cytoplasmic) membrane, with the diacylglyceryl transfer and N-acylation active sites oriented toward the extracytoplasmic face.

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordering constraints

The pathway is **strictly ordered by substrate logic**, not by external regulation (**Finding F001**). As stated in the structural consensus: *"Lipoprotein maturation requires the sequential activity of three enzymes that are embedded in the cytoplasmic membrane. First, phosphatidylglycerol:prolipoprotein diacylglyceryl transferase (Lgt) recognizes a conserved lipobox motif within the prolipoprotein signal sequence and catalyzes the addition of diacylglycerol to an invariant cysteine. The signal sequence is then cleaved by signal peptidase II (LspA) to give an N-terminal S-diacylglyceryl cysteine"* ([PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)). The dependency structure:

- **Lgt must act first** because LspA's substrate is the *diacylglyceryl-modified* prolipoprotein. LspA does not efficiently cleave an unmodified prolipoprotein.
- **LspA must act before Lnt** because Lnt requires the **free α-amino group** on the cysteine, which only exists after the signal peptide is removed.

This explains why the steps cannot be reordered: no plausible route allows Lnt N-acylation before signal-peptide removal, and none allows LspA cleavage to generate the correct product without prior diacylglyceryl modification.

### 6.2 Compartment- and substrate-specificity

- The substrate must carry a **lipobox with an invariant cysteine**; proteins without it are not module substrates.
- Reactions are **membrane-embedded**: Lgt uses phospholipid substrates delivered laterally through the bilayer, and Lnt acts as an extracytoplasmic acyl-enzyme intermediate. This constrains catalysis to the membrane interface.
- Lnt exhibits **phospholipid-donor specificity** (headgroup and acyl-chain dependence) ([PMID: 21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/)), so N-acyl chain identity reflects the local phospholipid pool.

### 6.3 Failure modes

- **Lgt loss** → accumulation of unmodified prolipoprotein, outer-membrane permeabilization, increased antibiotic/serum sensitivity, and lethality in most Gram-negatives ([PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)).
- **LspA loss/inhibition** → toxic buildup of uncleaved, mislocalized diacylglyceryl-prolipoprotein; this is the basis of globomycin and myxovirescin toxicity ([PMID: 22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/); [PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)).
- **Lnt loss** → in diderms, often lethal or severely impaired sorting (the mature triacyl anchor is the preferred Lol substrate); in Actinobacteria, N-acylation defects couple to loss of O-glycosylation ([PMID: 23029442](https://pubmed.ncbi.nlm.nih.gov/23029442/)); in Firmicutes lacking Lnt, N-acylation is dispensable and alternative end-states persist.

---

## 7. Mechanistic Model / Interpretation

Synthesizing the findings, the maturation module is best understood as a **conserved two-step catalytic backbone (Lgt→LspA) plus a lineage-variable terminal cap (Lnt / Ppm2 / Lit / none)**:

```
                         CONSERVED CORE                 |     LINEAGE-VARIABLE CAP
   -----------------------------------------------------|-------------------------------
   Prolipoprotein --Lgt--> DAG-prolipoprotein --LspA--> Apolipoprotein
        (lipobox Cys)     (thioether, S-diacyl)         (S-diacylglyceryl-Cys, free NH2)
                                                                |
                                    +---------------------------+---------------------------+
                                    |                           |                           |
                              Diderms & high-GC          Some low-GC Gram+           Many low-GC Gram+
                                    |                           |                           |
                              Lnt (E. coli) /             Lit (intramolecular          No 3rd acyl /
                              Ppm2 (Actino)               acyl migration)              N-acetyl / diacyl
                                    |                           |                           |
                              Triacyl lipoprotein         Lyso-form lipoprotein       Diacyl/variant
                                    |                           |                           |
                                    +-------------> Lol sorting (diderms), function <-------+
```

The core is conserved because it solves an invariant chemical problem — anchoring a soluble protein to the membrane via a thioether-linked diacylglyceryl group and removing the now-redundant signal peptide. The cap is variable because the third acyl chain serves lineage-specific purposes (Lol recognition in diderms; immune evasion via TLR2 tuning in Firmicutes) that different clades solve with different enzymes or forgo entirely. This architecture — invariant backbone, swappable terminus — is what makes the system both a robust drug target (hit the conserved Lgt/LspA core) and an evolutionary case study in non-orthologous gene displacement (the interchangeable step 3).

Because Lgt is present across all bacteria and absent from archaea ([PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)), the diacylglyceryl-transfer/signal-cleavage core is plausibly **ancestral to the bacterial domain**, with the N-acylation step a later, lineage-specific elaboration or replacement. For understanding the ancestral "Lnt-type" role, **canonical Lnt in Gram-negatives (E. coli) is the best-characterized representative**, but it should not be assumed to represent the ancestral N-acylation chemistry given the mechanistic diversity (Lnt vs. Ppm2 vs. Lit) across lineages.

---

## 8. Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/) | Structural basis of Lnt N-acylation; states the obligatory Lgt→LspA→(Lnt) order | F001, F004 |
| [26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/) | *E. coli* Lgt crystal structure; Arg143/Arg239 essential; lateral access | F002 |
| [42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/) | Lgt present in all bacteria, absent from archaea; arm/head domain diversity | F002 |
| [33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/) | Lgt depletion permeabilizes OM; G2824 inhibitor | F002 |
| [31340643](https://pubmed.ncbi.nlm.nih.gov/31340643/) | Mechanism of phosphatidylglycerol activation by Lgt | F002 |
| [26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/) | LspA is an aspartyl peptidase; globomycin molecular mimicry | F003 |
| [31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/) | Globomycin + myxovirescin as convergent tetrahedral-intermediate analogs | F003 |
| [22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/) | Genetic identification of LspA as myxovirescin (TA) target | F003 |
| [31036406](https://pubmed.ncbi.nlm.nih.gov/31036406/) | LspA prioritized as antimicrobial target | Boundaries/therapeutics |
| [20000742](https://pubmed.ncbi.nlm.nih.gov/20000742/) | Lnt Cys387 thioester acyl-enzyme intermediate; extracytoplasmic | F004 |
| [21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/) | Ping-pong kinetics; phospholipid specificity | F004 |
| [25471278](https://pubmed.ncbi.nlm.nih.gov/25471278/) | Flexible-loop residues required for the second (transfer) step | F004 |
| [24093492](https://pubmed.ncbi.nlm.nih.gov/24093492/) | Lnt absent in low-GC Gram+; mycobacterial N-acylation by BCG_2070c | F005 |
| [19661058](https://pubmed.ncbi.nlm.nih.gov/19661058/) | Identification of Lnt activity (Ppm1/Ppm2) in mycobacteria; triacylation | F005 |
| [23029442](https://pubmed.ncbi.nlm.nih.gov/23029442/) | *ppm* operon couples N-acylation and O-glycosylation in *C. glutamicum* | F005 |
| [22303020](https://pubmed.ncbi.nlm.nih.gov/22303020/) | Lyso-form and N-acetyl structures in low-GC Gram+; TLR2 recognition | F005 |
| [28320885](https://pubmed.ncbi.nlm.nih.gov/28320885/) | Identification of the lyso-form–forming enzyme (Lit) | F006 |
| [32471867](https://pubmed.ncbi.nlm.nih.gov/32471867/) | Lyso-form synthesized via intramolecular acyl chain migration | F006 |
| [34253723](https://pubmed.ncbi.nlm.nih.gov/34253723/) | *B. cereus* Lit structure; 8-membered-ring acyl-migration mechanism | F006 |
| [30988036](https://pubmed.ncbi.nlm.nih.gov/30988036/) | Copper-induced, transmissible Lit alters acylation and TLR2 response | F006 |
| [33667939](https://pubmed.ncbi.nlm.nih.gov/33667939/) | Separates maturation from sorting/targeting (Lol) | F007 |
| [27720009](https://pubmed.ncbi.nlm.nih.gov/27720009/) | Lipoprotein journey; Lol sorting and multiple destinations | F007 |
| [32723923](https://pubmed.ncbi.nlm.nih.gov/32723923/) | Acylation-state heterogeneity and TLR2 recognition | F005 context |

**Strongly supported claims:** the ordered three-enzyme sequence and its substrate-logical dependency (F001); Lgt structure, essential residues, and universal bacterial distribution (F002); LspA as an aspartyl peptidase inhibited by mimicry (F003); Lnt's Cys387 thioester ping-pong mechanism (F004); and the lineage variability of step 3 including the Lit acyl-migration mechanism (F005, F006). These rest on crystal structures, mutagenesis, kinetics, mass spectrometry, and genetics across multiple organisms.

**Areas relying on narrower or indirect evidence:** the exact phylogenetic breadth of alternative N-acylation enzymes; the in vivo essentiality of Lnt across diverse diderms; and whether the enzymes are physically coordinated. The literature also mixes native-substrate and synthetic-substrate (FSL-1) assays for Lnt, which should be borne in mind.

---

## 9. Controversies and Open Questions

1. **Definitional scope of step 3.** Whether "maturation" requires N-acylation at all is genuinely lineage-dependent. Many Firmicutes make functional, membrane-anchored lipoproteins that are diacylated (apolipoprotein state) or bear alternative modifications, meaning the "three-enzyme pathway" framing is a diderm-centric idealization. The species-neutral view — terminal cysteine modification, achieved by non-orthologous means or omitted — is more accurate but less tidy.

2. **Essentiality of Lnt is not universal.** Lnt is essential in many Gram-negatives but its requirement varies; some organisms tolerate diacylated lipoproteins for Lol sorting. Generalizing *E. coli* essentiality to all diderms risks overreach.

3. **Non-orthologous displacement of the N-acylation step.** Lit (intramolecular transacylase, His-based, acyl migration) and Ppm2 (Actinobacterial, *ppm*-operon-linked) achieve N-terminal acylation by mechanisms unrelated to Lnt's nitrilase-superfamily ping-pong chemistry. The full phylogenetic mapping of which lineages use which enzyme — and whether additional undiscovered N-acylation systems exist — is incomplete.

4. **Ancestral state and origin.** The Lgt→LspA core is plausibly ancestral to bacteria; the N-acylation step is a later, lineage-specific elaboration or replacement. The identity of the ancestral third-step chemistry (if any) remains unresolved.

5. **In vivo coordination and hand-off.** Whether the three enzymes physically associate into a super-complex or a substrate channel, or act as independent stations, is not fully resolved. The kinetic ordering is clear; the spatial organization is not.

6. **Reliance on mixed-organism data.** Much mechanistic detail derives from *E. coli* (Lgt, Lnt), *P. aeruginosa* and *S. aureus* (LspA), *B. cereus* (Lit), and mycobacteria/*C. glutamicum* (Ppm2). Cross-organism synthesis is powerful but must be qualified: assay systems, substrates, and physiological contexts differ.

---

## 10. Limitations and Knowledge Gaps

- **Organism sampling bias.** Mechanistic depth is concentrated in a handful of model organisms. The generality of specific quantitative findings to the wider bacterial tree is inferred, not directly established.
- **Spatial organization unknown.** Whether Lgt, LspA, and Lnt form a physical assembly or substrate channel in vivo is unresolved; the ordering is kinetically enforced but the choreography is unclear.
- **Incomplete map of step-3 diversity.** The full census of N-acylation (and N-modification) enzymes across Firmicutes and other lineages, and the rules governing strain-specific acylation states, is incomplete.
- **Regulation.** How (or whether) the pathway is regulated in response to membrane phospholipid composition, stress, or growth phase is largely unexplored — Lnt's phospholipid-donor dependence hints at a passive coupling to lipid metabolism, but active regulation is not established.
- **This synthesis is literature-derived.** No primary experimental data were generated in this investigation; conclusions rest entirely on published structural, biochemical, genetic, and mass-spectrometric studies.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Comparative phylogenomics of step 3.** Systematically map Lnt, Ppm2-type, and Lit-type enzymes (and lipobox-bearing proteomes) across bacterial phyla to define the true distribution of N-acylation strategies and identify candidate novel enzymes in "orphan" lineages.
2. **In vivo assembly test.** Use crosslinking, co-purification, or cryo-EM in a native membrane context to determine whether the three maturation enzymes physically associate or hand off substrate diffusively.
3. **Reconstituted ordered pathway.** Rebuild the full Lgt→LspA→Lnt sequence in vitro with defined lipids and a native prolipoprotein substrate to directly measure step coupling, rate-limiting steps, and the strictness of the ordering constraint.
4. **Structure–function of Lit vs. Lnt.** Compare the acyl-migration (Lit, His-based) and intermolecular-transfer (Lnt, Cys-based) chemistries side by side to understand why two mechanisms coexist and what selective pressures favor each.
5. **Therapeutic exploitation of the conserved core.** Advance Lgt (e.g., G2824-class) and LspA (globomycin/myxovirescin-class) inhibitors, prioritizing the near-universal, essential steps; evaluate resistance liabilities given that Lnt-independent lineages may respond differently.
6. **Immunological consequences of acylation state.** Systematically link maturation-enzyme genotype (triacyl vs. lyso vs. diacyl output) to TLR2/1 vs. TLR2/6 signaling and in vivo virulence, building on the Lit/TLR2 observations.

---

## 12. Key References

- **Structural insights into lipoprotein N-acylation by apolipoprotein N-acyltransferase.** [PMID: 28698362](https://pubmed.ncbi.nlm.nih.gov/28698362/)
- **Crystal structure of E. coli lipoprotein diacylglyceryl transferase.** [PMID: 26729647](https://pubmed.ncbi.nlm.nih.gov/26729647/)
- **Arm and head domain in highly conserved lipoprotein modification enzyme Lgt determine functional diversity among bacterial pathogens.** [PMID: 42126242](https://pubmed.ncbi.nlm.nih.gov/42126242/)
- **Inhibition of E. coli Lgt is insensitive to resistance caused by deletion of Braun's lipoprotein.** [PMID: 33875545](https://pubmed.ncbi.nlm.nih.gov/33875545/)
- **Mechanism of phosphatidylglycerol activation catalyzed by prolipoprotein diacylglyceryl transferase.** [PMID: 31340643](https://pubmed.ncbi.nlm.nih.gov/31340643/)
- **Structural basis of lipoprotein signal peptidase II action and inhibition by globomycin.** [PMID: 26912896](https://pubmed.ncbi.nlm.nih.gov/26912896/)
- **Structures of LspA from S. aureus complexed with globomycin and myxovirescin.** [PMID: 31919415](https://pubmed.ncbi.nlm.nih.gov/31919415/)
- **Myxobacterium-produced antibiotic TA (myxovirescin) inhibits type II signal peptidase.** [PMID: 22232277](https://pubmed.ncbi.nlm.nih.gov/22232277/)
- **The essential E. coli Lnt exists as an extracytoplasmic thioester acyl-enzyme intermediate.** [PMID: 20000742](https://pubmed.ncbi.nlm.nih.gov/20000742/)
- **Kinetics and phospholipid specificity of apolipoprotein N-acyltransferase.** [PMID: 21676878](https://pubmed.ncbi.nlm.nih.gov/21676878/)
- **Residues on membrane-embedded flexible loops essential for the second step of Lnt.** [PMID: 25471278](https://pubmed.ncbi.nlm.nih.gov/25471278/)
- **Lipoproteins of slow-growing Mycobacteria are N-acylated by BCG_2070c.** [PMID: 24093492](https://pubmed.ncbi.nlm.nih.gov/24093492/)
- **Identification of apolipoprotein N-acyltransferase (Lnt) in mycobacteria.** [PMID: 19661058](https://pubmed.ncbi.nlm.nih.gov/19661058/)
- **The ppm operon is essential for acylation and glycosylation of lipoproteins in C. glutamicum.** [PMID: 23029442](https://pubmed.ncbi.nlm.nih.gov/23029442/)
- **Novel lipoprotein structures conserved in low-GC Gram-positive bacteria recognized by TLR2.** [PMID: 22303020](https://pubmed.ncbi.nlm.nih.gov/22303020/)
- **Identification of the lyso-form lipoprotein synthase (Lit).** [PMID: 28320885](https://pubmed.ncbi.nlm.nih.gov/28320885/)
- **Bacterial lyso-form lipoproteins are synthesized via an intramolecular acyl chain migration.** [PMID: 32471867](https://pubmed.ncbi.nlm.nih.gov/32471867/)
- **Structural basis of the membrane intramolecular transacylase reaction (Lit).** [PMID: 34253723](https://pubmed.ncbi.nlm.nih.gov/34253723/)
- **Copper-induced expression of a transmissible Lit alters lipoprotein acylation and the TLR2 response.** [PMID: 30988036](https://pubmed.ncbi.nlm.nih.gov/30988036/)
- **Lipoproteins in Gram-negative bacteria: biogenesis, subcellular targeting and functional roles.** [PMID: 33667939](https://pubmed.ncbi.nlm.nih.gov/33667939/)
- **The Journey of Lipoproteins Through the Cell: One Birthplace, Multiple Destinations.** [PMID: 27720009](https://pubmed.ncbi.nlm.nih.gov/27720009/)
- **Targeting lipoprotein biogenesis: considerations towards antimicrobials.** [PMID: 31036406](https://pubmed.ncbi.nlm.nih.gov/31036406/)
- **Lipoprotein N-terminal acylation heterogeneity and TLR2 recognition.** [PMID: 32723923](https://pubmed.ncbi.nlm.nih.gov/32723923/)

---

## 13. Conclusion

Bacterial lipoprotein maturation is a strictly ordered, inner-membrane module in which Lgt transfers a diacylglyceryl group from phosphatidylglycerol onto the invariant lipobox cysteine (the committed step), LspA — an aspartyl signal peptidase II — cleaves the signal peptide to expose the apolipoprotein N-terminus, and Lnt (or a lineage equivalent) N-acylates that free α-amino group to yield a triacylated lipoprotein. The order is enforced because each enzyme's substrate is the previous enzyme's product. Lgt and LspA constitute a near-universal, essential conserved core (Lgt is present in all bacteria and absent from archaea), while the terminal N-acylation step is lineage-variable: canonical Lnt in diderms and high-GC Actinobacteria versus non-orthologous routes — notably the intramolecular transacylase Lit producing lyso-form lipoproteins, plus N-acetyl and diacyl products — in low-GC Firmicutes. Maturation ends at the lipidated N-terminal cysteine; downstream Lol sorting and substrate-specific functions lie outside the module.


## Artifacts

- [OpenScientist final report](bacterial_lipoprotein_maturation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_lipoprotein_maturation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33667939
2. PMID:27720009
3. PMID:28698362
4. PMID:26729647
5. PMID:42126242
6. PMID:33875545
7. PMID:31340643
8. PMID:26912896
9. PMID:31919415
10. PMID:22232277
11. PMID:31036406
12. PMID:20000742
13. PMID:21676878
14. PMID:25471278
15. PMID:24093492
16. PMID:19661058
17. PMID:23029442
18. PMID:22303020
19. PMID:28320885
20. PMID:32471867
21. PMID:34253723
22. PMID:30988036
23. PMID:32723923