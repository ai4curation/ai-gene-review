---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T01:05:03.045004'
end_time: '2026-08-13T01:22:46.044240'
duration_seconds: 1063.0
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial fructose PTS uptake and catabolism
  module_summary: A reusable bacterial module coupling phosphoenolpyruvate-driven
    phosphorelay, fructose translocation with phosphorylation to fructose 1-phosphate,
    and ATP-dependent production of fructose 1,6-bisphosphate. The Pseudomonas implementation
    uses a fused EI-HPr-EIIA FruB protein and an EIIB-EIIC FruA transporter. Nitrogen-related
    PTS signaling and metabolism downstream of fructose 1,6-bisphosphate are outside
    the module boundary.
  module_outline: "- Bacterial fructose PTS uptake and catabolism\n  - 1. phosphoenolpyruvate-driven\
    \ fructose PTS phosphorelay\n  - Fused EI-HPr-EIIA fructose PTS phosphorelay\n\
    \    - FruB multiphosphoryl-transfer activity (molecular player: fused fructose\
    \ PTS EI-HPr-EIIA family; activity or role: phosphoenolpyruvate-protein phosphotransferase\
    \ activity)\n  - 2. fructose uptake coupled to fructose 1-phosphate formation\n\
    \  - Fructose PTS transport and phosphorylation\n    - FruA fructose-specific\
    \ EIIB-EIIC activity (molecular player: fructose-specific PTS EIIB-EIIC family;\
    \ activity or role: fructose phosphotransferase system transporter activity)\n\
    \  - 3. fructose 1-phosphate conversion to fructose 1,6-bisphosphate\n  - Fructose\
    \ 1-phosphate phosphorylation\n    - FruK 1-phosphofructokinase activity (molecular\
    \ player: 1-phosphofructokinase family; activity or role: 1-phosphofructokinase\
    \ activity)"
  module_connections: '- Fused EI-HPr-EIIA fructose PTS phosphorelay feeds into Fructose
    PTS transport and phosphorylation: Phosphorylated FruB donates phosphate to the
    FruA EIIB domain.

    - Fructose PTS transport and phosphorylation feeds into Fructose 1-phosphate phosphorylation:
    FruA-produced fructose 1-phosphate is the FruK substrate.'
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_fructose_pts_catabolism-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_fructose_pts_catabolism-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial fructose PTS uptake and catabolism

## Working Scope

A reusable bacterial module coupling phosphoenolpyruvate-driven phosphorelay, fructose translocation with phosphorylation to fructose 1-phosphate, and ATP-dependent production of fructose 1,6-bisphosphate. The Pseudomonas implementation uses a fused EI-HPr-EIIA FruB protein and an EIIB-EIIC FruA transporter. Nitrogen-related PTS signaling and metabolism downstream of fructose 1,6-bisphosphate are outside the module boundary.

## Provisional Biological Outline

- Bacterial fructose PTS uptake and catabolism
  - 1. phosphoenolpyruvate-driven fructose PTS phosphorelay
  - Fused EI-HPr-EIIA fructose PTS phosphorelay
    - FruB multiphosphoryl-transfer activity (molecular player: fused fructose PTS EI-HPr-EIIA family; activity or role: phosphoenolpyruvate-protein phosphotransferase activity)
  - 2. fructose uptake coupled to fructose 1-phosphate formation
  - Fructose PTS transport and phosphorylation
    - FruA fructose-specific EIIB-EIIC activity (molecular player: fructose-specific PTS EIIB-EIIC family; activity or role: fructose phosphotransferase system transporter activity)
  - 3. fructose 1-phosphate conversion to fructose 1,6-bisphosphate
  - Fructose 1-phosphate phosphorylation
    - FruK 1-phosphofructokinase activity (molecular player: 1-phosphofructokinase family; activity or role: 1-phosphofructokinase activity)

## Known Relationships Among Steps

- Fused EI-HPr-EIIA fructose PTS phosphorelay feeds into Fructose PTS transport and phosphorylation: Phosphorylated FruB donates phosphate to the FruA EIIB domain.
- Fructose PTS transport and phosphorylation feeds into Fructose 1-phosphate phosphorylation: FruA-produced fructose 1-phosphate is the FruK substrate.

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

# Bacterial Fructose PTS Uptake and Catabolism: A Mechanistic Review

*A commissioned review-style synthesis of the phosphoenolpyruvate-driven fructose phosphotransferase module, from PEP phosphorelay through fructose 1,6-bisphosphate.*

---

## 1. Executive Summary

The bacterial fructose phosphotransferase system (PTS^Fru) is a compact, self-contained metabolic module that couples the free energy of phosphoenolpyruvate (PEP) to the simultaneous import and phosphorylation of fructose, delivering the phosphorylated sugar directly into central carbon metabolism. In its canonical Gammaproteobacterial and *Pseudomonas* implementation the module comprises just three functional players: (i) **FruB**, a fused multiphosphoryl-transfer protein carrying Enzyme I (EI), HPr (here called FPr), and EIIA^Fru domains in a single polypeptide; (ii) **FruA**, a membrane transporter fusing the cytoplasmic EIIB domain to the integral-membrane EIIC permease; and (iii) **FruK**, a soluble ATP-dependent 1-phosphofructokinase of the PfkB/ribokinase superfamily. The phosphoryl chain runs PEP → EI → HPr(FPr) → EIIA^Fru → EIIB → fructose, producing intracellular **fructose 1-phosphate (F1P)**; FruK then phosphorylates F1P at the expense of ATP to yield **fructose 1,6-bisphosphate (FBP)**, the point at which the sugar enters lower glycolysis and the module's boundary is reached.

The central mechanistic insight, supported across three independent bacterial lineages, is that this is a **group-translocation** system rather than an "import-then-phosphorylate" pathway: the membrane EIIC (FruA) carries fructose across the bilayer while the coupled EIIB domain phosphorylates it, so free intracellular fructose is never released — the transported molecule emerges already committed as F1P. This tight coupling of translocation and phosphorylation is a defining structural and thermodynamic feature that rules out otherwise plausible alternative routes. Evolutionarily, the module has a clear "ancient core / mobile periphery" architecture: the PEP-utilizing EI/HPr phosphotransfer chemistry is deeply conserved and vertically inherited — Enzyme I is a structural homolog of pyruvate phosphate dikinase (PPDK) within the ancient PEP-utilizing enzyme superfamily — whereas the sugar-specific enzyme II components are horizontally mobile and lineage-variable.

Two systems lie immediately adjacent to, but outside, the module boundary and are frequently conflated with it: the **nitrogen-related PTS (PTS^Ntr)**, a paralogous non-transporting signaling branch that can receive phosphate from FruB; and **Cra/FruR**, a global central-carbon transcription factor that senses F1P but regulates ~40–180 promoters genome-wide, far beyond the *fru* operon. Recognizing these as separate layers — cross-talk partner and regulatory overlay, respectively — is essential to a clean definition of the fructose PTS module.

---

## 2. Definition and Biological Boundaries

### What the module is

The fructose PTS uptake-and-catabolism module is defined here as the minimal set of reactions and molecular players that convert **extracellular fructose** into **fructose 1,6-bisphosphate** using PEP (for transport/phosphorylation) and ATP (for the second phosphorylation). It consists of three obligatory steps:

1. **PEP-driven phosphorelay** through the fused FruB protein (EI–HPr–EIIA^Fru).
2. **Fructose translocation coupled to phosphorylation** by the FruA transporter (EIIB–EIIC), yielding F1P.
3. **F1P → FBP conversion** by the 1-phosphofructokinase FruK.

In Gammaproteobacteria these three functions are genetically organized in a single *fru* operon encoding FruA, FruB, and FruK, with F1P serving as the internal inducer that links catabolic flux to operon expression ([PMID: 33476373](https://pubmed.ncbi.nlm.nih.gov/33476373/); [PMID: 22708906](https://pubmed.ncbi.nlm.nih.gov/22708906/)).

### What lies just outside the boundary (and is often confused with it)

- **The nitrogen-related PTS (PTS^Ntr):** encoded by *ptsP–ptsO–ptsN* (EI^Ntr–NPr–EIIA^Ntr), this is a paralogous phosphorelay that does **not** transport sugar. It is a signaling branch coordinating carbon and nitrogen status. Phosphorylated FruB can donate high-energy phosphate to EIIA^Ntr (PtsN), so the two systems cross-talk — but PTS^Ntr should be treated as an adjacent module, not part of fructose catabolism ([PMID: 22708906](https://pubmed.ncbi.nlm.nih.gov/22708906/); [PMID: 17478425](https://pubmed.ncbi.nlm.nih.gov/17478425/)).
- **Cra/FruR global regulation:** the catabolite repressor/activator that responds to F1P is a genome-wide regulator of glycolysis, gluconeogenesis, the TCA cycle, and respiration, not a *fru*-specific switch. It is best treated as a regulatory overlay ([PMID: 29394395](https://pubmed.ncbi.nlm.nih.gov/29394395/); [PMID: 21115656](https://pubmed.ncbi.nlm.nih.gov/21115656/)).
- **Downstream glycolysis:** everything beyond FBP (aldolase, lower glycolysis, the Entner–Doudoroff pathway in *Pseudomonas*) is out of scope.
- **Other sugar PTS branches:** glucose (ptsG), mannose (Man-PTS), mannitol, and cellobiose PTS systems share the general EI/HPr chemistry but are substrate-distinct and structurally distinct. In particular, fructose-specific EIIC belongs to a different transporter superfamily than glucose- or mannose-family permeases.

### Competing definitions

The literature is not fully uniform. Some treatments fold the F1P-sensing regulator (Cra/FruR) and even the PTS^Ntr cross-talk into "the fructose PTS system" because they are functionally intertwined in signaling. The definition adopted here — restricting the module to the three catabolic steps and treating PTS^Ntr and Cra/FruR as adjacent layers — follows the working scope of the brief and keeps mechanism and regulation cleanly separated. This distinction matters because regulatory polarity and cross-talk vary by lineage even where the core catabolic chemistry is invariant.

---

## 3. Mechanistic Overview

### The phosphoryl relay and its topology

The defining chemistry is a chain of reversible phosphohistidine (and, at EIIB, phosphocysteine) transfers that channel the phosphoryl group of PEP onto the incoming sugar:

```
   PEP ──► EI ──► HPr(FPr) ──► EIIA^Fru ──► EIIB ──► fructose (at EIIC)
   \___________ FruB (single polypeptide) ___________/   \___ FruA ___/
        EI–HPr–EIIA fused                              EIIB–EIIC fused

   Net: extracellular fructose + PEP ──► intracellular fructose 1-phosphate + pyruvate
        fructose 1-phosphate + ATP  ──(FruK)──► fructose 1,6-bisphosphate + ADP
```

A subtle but important point of topology: although the phosphoryl group flows EI → HPr → EIIA, the **physical domain order** within FruB is the reverse — **EIIA^Fru (N-terminus) – HPr(FPr) – EI (C-terminus)** — as established by sequence and domain analysis in *Rhodobacter capsulatus* and *Xanthomonas campestris* (see Finding F001). The fusion therefore places the terminal acceptor domain (EIIA) first and the initiating PEP-binding EI domain last.

### Obligatory, conditional, and accessory steps

- **Obligatory:** all three catabolic steps. EI autophosphorylation by PEP (requires Mg²⁺ and EI dimerization), phosphotransfer down the FruB chain, EIIB→sugar transfer coupled to EIIC translocation, and FruK-catalyzed phosphorylation of F1P are each required to convert extracellular fructose to FBP. Because transport and phosphorylation by FruA are mechanically coupled, they cannot be decoupled into separate steps.
- **Conditional:** cross-talk from FruB to PtsN (PTS^Ntr) occurs on fructose but is almost completely suppressed on gluconeogenic substrates such as succinate — it is a physiological-state-dependent event, not an obligatory part of catabolism.
- **Accessory / regulatory:** Cra/FruR-mediated transcriptional control of the *fru* operon; F1P acts as the internal inducer antagonizing Cra DNA binding. This tunes flux but is not part of the catalytic path.

### Why "import-then-phosphorylate" is ruled out

In all PTS, cytoplasmic IIA and IIB units sequentially transfer phosphate to the sugar, which is transported by the membrane IIC (or IICIID) complex, and **phosphorylation by IIB and translocation by IIC are tightly coupled** ([PMID: 31214989](https://pubmed.ncbi.nlm.nih.gov/31214989/)). Crystal structures of glucose-superfamily EIICs trapped in outward- and inward-facing states show that translocation proceeds by a large rigid-body, elevator-like motion of a discrete sugar-binding domain ([PMID: 29784777](https://pubmed.ncbi.nlm.nih.gov/29784777/)). The consequence is that fructose is not released as a free intracellular pool and then phosphorylated by a separate kinase; the molecule emerges from the transporter already phosphorylated as F1P. This is a hard mechanistic constraint that distinguishes group translocation from facilitated diffusion or ABC-type import (Finding F005).

---

## 4. Major Molecular Players and Active Assemblies

### 4.1 FruB — the fused multiphosphoryl-transfer protein (Finding F001)

FruB (the "MTP," multiphosphoryl-transfer protein) is a single polypeptide fusing three functional domains. The architecture is conserved across distant lineages:

| Organism | Domain 1 (N-term) | Domain 2 (middle) | Domain 3 (C-term) | Reference |
|---|---|---|---|---|
| *Rhodobacter capsulatus* MTP | EIIA/III^fru-like (res. 1–143) | FPr(HPr)-like (157–245) | EI-like (273–827) | [PMID: 2193161](https://pubmed.ncbi.nlm.nih.gov/2193161/) |
| *Xanthomonas campestris* MTP (837 aa) | EIIA-like (1–148) | HPr-like (161–251) | EI-like (274–837) | [PMID: 7496537](https://pubmed.ncbi.nlm.nih.gov/7496537/) |
| *Pseudomonas putida* FruB | EI–HPr–EIIA^Fru polyprotein (functional description) | | | [PMID: 22708906](https://pubmed.ncbi.nlm.nih.gov/22708906/) |

Predicted phospho-histidine sites in the *R. capsulatus* protein are His62 (EIIA domain), His171 (HPr domain), and His457 (EI domain), the three obligatory relay residues. The domains are joined by proline/alanine-rich hinge segments (explicitly noted in *Xanthomonas*), consistent with flexible tethers that allow the mobile phospho-domains to dock sequentially. Cross-lineage identity is high — *R. capsulatus* vs. *X. campestris* MTP are 46% identical — indicating that the fusion is an ancient and stable arrangement rather than an idiosyncratic one. Functionally, this fusion is what the brief refers to as the "fused EI-HPr-EIIA fructose PTS phosphorelay."

### 4.2 FruA — the group-translocating transporter (Finding F005)

FruA fuses the cytoplasmic **EIIB** phosphotransfer domain to the integral-membrane **EIIC** permease. EIIB accepts phosphate from EIIA^Fru and hands it to the incoming fructose; EIIC forms the translocation pathway. There are four structurally distinct EIIC transporter superfamilies (glucose, glucitol/mannitol, ascorbate, mannose); fructose-specific EIIC belongs to the **mannitol/glucitol-type** superfamily — a point that distinguishes fructose transport structurally from the better-known glucose (ptsG) and mannose systems. The elevator-like conformational cycle inferred from glucose-superfamily EIIC structures ([PMID: 29784777](https://pubmed.ncbi.nlm.nih.gov/29784777/)) provides the physical basis for coupling translocation to phosphorylation.

### 4.3 FruK — the 1-phosphofructokinase (Finding F002)

FruK converts F1P + ATP → FBP + ADP. It belongs to the **PfkB/ribokinase superfamily**, not the PfkA phosphofructokinase family. In *R. capsulatus*, FruK is 316 aa (~31.2 kDa) and homologous to *E. coli* FruK, *E. coli* PfkB, *Staphylococcus aureus* phosphotagatokinase, and *E. coli* ribokinase ([PMID: 1850730](https://pubmed.ncbi.nlm.nih.gov/1850730/)). This superfamily assignment is mechanistically meaningful: it explains why FruK is a distinct small-molecule kinase acting on the 1-phosphate ester (producing the 1,6-bisphosphate) rather than the classical PfkA-type enzyme that phosphorylates fructose 6-phosphate in canonical glycolysis. The two enzymes converge on FBP by different routes, but FruK is the fructose-PTS-specific one.

### 4.4 The active assembly

The working system is best pictured as a soluble relay (FruB, plus PEP and Mg²⁺) feeding a membrane transporter (FruA), followed by a soluble kinase (FruK). EI must dimerize to autophosphorylate from PEP; the dimerization determinant resides in the C-terminal PEP-binding domain, and the conserved Gly356 is critical (see §5). The phospho-domains of FruB act as mobile carriers docking sequentially — the fusion effectively raises the local concentration of each partner and enforces the order of transfer.

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep origin: an ancient core and a mobile periphery (Finding F004)

The module is a chimera of an ancient conserved core and a horizontally mobile periphery.

**Ancient core — the PEP-utilizing chemistry.** Enzyme I derives from the ancient **PEP-utilizing enzyme superfamily** that also contains pyruvate phosphate dikinase (PPDK) and PEP synthase. The C-terminal PEP-binding domain of EI (EIC) folds as a (βα)₈ TIM barrel whose active-site residues adopt almost identical conformations to those in PPDK ([PMID: 15670601](https://pubmed.ncbi.nlm.nih.gov/15670601/)). The N-terminal EIN phosphohistidine subdomain is topologically similar to the PPDK His domain ([PMID: 8805571](https://pubmed.ncbi.nlm.nih.gov/8805571/)), and the dimerization-critical Gly356 is conserved between EI and PPDK ([PMID: 10736161](https://pubmed.ncbi.nlm.nih.gov/10736161/)). Thus the phosphoryl-donating machinery of the PTS is a repurposing of primordial PEP metabolism.

**Mobile periphery — the substrate-specific enzyme II.** Phylogenomic analysis of 222 genomes places the origin of the PTS phosphoryl-transfer chain **within Bacteria, after the divergence of the earliest lineages** (Aquificales, Thermotogales, Thermus/Deinococcus). The general phosphoryl-transfer proteins (EI, HPr) evolved largely by **vertical inheritance**, whereas the substrate-specific enzyme II complexes are dominated by **horizontal gene transfer** ([PMID: 18485189](https://pubmed.ncbi.nlm.nih.gov/18485189/)). The PTS is absent from eukaryotes and rare/limited in archaea, reinforcing that it is a bacterial innovation grafted onto ancient PEP chemistry.

**Best representatives for the ancestral role.** Because the sugar-specific EII parts have expanded and been shuffled by HGT, the general EI and HPr proteins are the most reliable guides to the ancestral PTS. For understanding EI's deepest origin, PPDK is the closest structural relative and the best proxy for the ancestral PEP-binding fold.

### 5.2 Lineage variation in the transcriptional wiring (Finding F006)

The catalytic core is remarkably invariant, but the regulatory polarity around it is lineage-specific. Cra/FruR **represses** the *fru* operon in *E. coli* and *P. putida* but **activates** it in *Vibrio cholerae*, where FruR facilitates RNA polymerase binding to the *fru* promoter in the presence of F1P ([PMID: 33476373](https://pubmed.ncbi.nlm.nih.gov/33476373/)). This is a genuine, well-supported inversion of regulatory sign around a conserved catalytic module — a caution against assuming that regulatory conclusions from one organism transfer to another.

### 5.3 Fusion architecture as a variable

The EI–HPr–EIIA fusion of FruB is itself a lineage feature. In many bacteria EI, HPr, and EIIA are separate proteins; the fructose branch of *Pseudomonas*, *Rhodobacter*, *Xanthomonas*, and related organisms fuses them into a dedicated multiphosphoryl-transfer protein. Fusion likely enhances channeling and dedicates a private phosphorelay to fructose, insulating it from the general HPr pool.

### 5.4 Physiological-state dependence of cross-talk (Finding F003)

The FruB → PtsN phosphate cross-talk is conditional on metabolic state: it occurs during growth on fructose but is almost completely prevented on the gluconeogenic substrate succinate, and it persists in a Δ*cra* mutant, showing the cross-talk is not simply a transcriptional consequence of Cra ([PMID: 22708906](https://pubmed.ncbi.nlm.nih.gov/22708906/)). PtsN phosphorylation state also varies with growth phase and nitrogen source independently of sugar traffic ([PMID: 17478425](https://pubmed.ncbi.nlm.nih.gov/17478425/)).

---

## 6. Constraints, Dependencies, and Failure Modes

### Ordering constraints (what must happen in sequence)

1. **PEP before everything.** EI cannot initiate the relay without PEP and Mg²⁺, and it must dimerize to autophosphorylate. Loss of dimerization (e.g., Gly356Ser) sharply reduces activity and raises the K_m for PEP ([PMID: 10736161](https://pubmed.ncbi.nlm.nih.gov/10736161/)).
2. **Phosphotransfer is strictly sequential:** EI → HPr → EIIA → EIIB → sugar. Each His/Cys must be phosphorylated by its upstream partner before it can donate downstream.
3. **Transport requires phosphorylation.** Because FruA's EIIB phosphorylation and EIIC translocation are mechanically coupled, fructose cannot be moved across the membrane without the phospho-relay being competent. A dephosphorylated system halts transport.
4. **FruK acts only on F1P.** FruK requires F1P (the FruA product) as substrate; there is no bypass that feeds free fructose or fructose-6-P into FruK.

### Mutually exclusive / substrate-specific events

- Fructose is committed to F1P at the membrane; there is no free intracellular fructose intermediate, so a cytoplasmic fructokinase route is excluded for the PTS-imported pool.
- Cross-talk to PTS^Ntr is substrate-state-specific (fructose-on, succinate-off), making it mutually exclusive with gluconeogenic growth.
- FruK (PfkB/ribokinase family, acts on F1P) and PfkA (acts on F6P) are distinct enzymes converging on FBP; the fructose-PTS route uses FruK.

### Failure modes

- **Loss of EI/HPr competence** (e.g., *ptsI* mutation) abolishes all PTS transport, not just fructose, because the general proteins are shared — a systemic failure mode.
- **Loss of FruK** traps F1P, which is toxic/regulatory (F1P is the Cra effector); accumulation would derepress the operon while blocking downstream flux.
- **Regulatory miswiring:** because Cra/FruR is global, mutations in *fruR/cra* redistribute carbon flux genome-wide. Engineering FruR redirects central carbon flow, e.g., to enhance L-phenylalanine biosynthesis ([PMID: 36289548](https://pubmed.ncbi.nlm.nih.gov/36289548/)), illustrating that the regulatory overlay has system-wide leverage.

---

## 7. Controversies and Open Questions

1. **F1P vs. FBP as the Cra effector.** F1P is the more potent antagonist of Cra DNA binding in enterobacteria and is the direct *fru*-inducer signal ([PMID: 22708906](https://pubmed.ncbi.nlm.nih.gov/22708906/)), but fructose 1,6-bisphosphate was historically also proposed as an effector. The relative contributions likely differ by organism and physiological state; this is not fully resolved.

2. **Repressor vs. activator polarity.** The *Vibrio cholerae* case, where FruR activates the *fru* operon ([PMID: 33476373](https://pubmed.ncbi.nlm.nih.gov/33476373/)), stands opposite to the repressor role in *E. coli*/*P. putida*. Whether this reflects promoter architecture, effector concentration, or FruR structural differences remains open.

3. **Where exactly is the module boundary in signaling?** The FruB→PtsN cross-talk blurs the line between carbon uptake and nitrogen signaling. Whether PtsN phosphorylation by FruB is a physiologically important regulatory output or incidental phosphotransfer promiscuity is debated; the conditional (substrate-dependent) nature argues for genuine signaling, but the downstream consequences are incompletely mapped.

4. **Structural gaps for fructose-specific EIIC.** Mechanistic models of translocation rely on glucose-superfamily EIIC structures ([PMID: 29784777](https://pubmed.ncbi.nlm.nih.gov/29784777/)); a high-resolution structure of a genuine fructose (mannitol/glucitol-family) EIIC in multiple conformational states would confirm that the elevator mechanism applies to FruA specifically.

5. **Generality of the fusion.** The EI–HPr–EIIA fusion is well documented in a handful of lineages; the full phylogenetic distribution of FruB-type fusions versus split-component fructose PTS, and whether the fusion confers measurable channeling advantages, is not comprehensively established.

6. **Organism mixing in the literature.** Much mechanistic detail is stitched together from *Rhodobacter*, *Xanthomonas*, *E. coli*, *P. putida*, and *Vibrio*. While the domain architecture is strikingly conserved, regulatory conclusions in particular should not be freely transferred across these organisms.

---

## 8. Mechanistic Model (Synthesis)

```
  EXTRACELLULAR                MEMBRANE                    CYTOPLASM
  ─────────────                ────────                    ─────────

     fructose ───────────►  ┌───────────────┐
                            │  FruA  EIIC    │  elevator-like
                            │  (mannitol/    │  translocation
                            │   glucitol     │
                            │   superfamily) │
                            │      │         │
                            │   EIIB ~P ─────┼──► fructose 1-PHOSPHATE (F1P)
                            └──────▲─────────┘          │
                                   │                    │  + ATP
                                   │ ~P                 ▼  (FruK, PfkB/ribokinase family)
              PEP                  │            fructose 1,6-BISPHOSPHATE (FBP)
               │                   │                    │
               ▼                   │                    ▼  [MODULE BOUNDARY]
   ┌──────────────────────────────┴──┐          (lower glycolysis / ED pathway)
   │   FruB (fused polypeptide)       │
   │   EI ~P → HPr(FPr) ~P → EIIA ~P  │────┐
   │   (physical order EIIA–HPr–EI)   │    │ conditional cross-talk
   └──────────────────────────────────┘    │ (fructose ON, succinate OFF)
                                            ▼
                                    EIIA^Ntr (PtsN)  →  PTS^Ntr signaling
                                    [ADJACENT MODULE]

   Regulatory overlay: F1P antagonizes Cra/FruR DNA binding
                       Cra/FruR = global regulator (~40–180 promoters)
                       polarity: repressor (E. coli, P. putida) / activator (V. cholerae)
```

The narrative: PEP powers a private, fused phosphorelay (FruB) that hands phosphate to a group-translocating transporter (FruA), which imports and phosphorylates fructose in a single mechanically coupled event, producing F1P. F1P is both the substrate for the committed catabolic kinase (FruK → FBP) and the intracellular signal that releases the operon from Cra/FruR control. The ancient PEP-utilizing chemistry (EI ≈ PPDK) is the conserved heart; the sugar-specific EII parts are the HGT-mobile skin; and the PTS^Ntr cross-talk plus Cra/FruR regulation are the two adjacent layers that frame — but do not belong to — the catabolic module.

---

## 9. Evidence Base

| PMID | Contribution to this review | Strength |
|---|---|---|
| [2193161](https://pubmed.ncbi.nlm.nih.gov/2193161/) | Defines the EIIA–HPr–EI fused architecture and P-His sites in *R. capsulatus* MTP/FruB | Primary sequence/structure |
| [7496537](https://pubmed.ncbi.nlm.nih.gov/7496537/) | Independent confirmation of EIIA–HPr–EI fusion in *X. campestris* (837 aa) | Primary sequence |
| [22708906](https://pubmed.ncbi.nlm.nih.gov/22708906/) | *P. putida* FruB as EI–HPr–EIIA polyprotein; FruB→PtsN cross-talk; F1P as Cra effector | Primary functional |
| [33476373](https://pubmed.ncbi.nlm.nih.gov/33476373/) | *fru* operon composition (FruA/FruB/FruK); FruR as activator in *V. cholerae* | Primary functional |
| [1850730](https://pubmed.ncbi.nlm.nih.gov/1850730/) | FruK in PfkB/ribokinase superfamily, distinct from PfkA | Primary sequence |
| [31214989](https://pubmed.ncbi.nlm.nih.gov/31214989/) | Group-translocation principle; IIB phosphorylation coupled to IIC translocation | Review |
| [29784777](https://pubmed.ncbi.nlm.nih.gov/29784777/) | Elevator-like EIIC translocation mechanism from inward/outward structures | Primary structural |
| [15670601](https://pubmed.ncbi.nlm.nih.gov/15670601/) | EIC PEP-binding domain ≈ PPDK active site (shared ancestry) | Primary structural |
| [8805571](https://pubmed.ncbi.nlm.nih.gov/8805571/) | EIN phosphohistidine domain topologically similar to PPDK His domain | Primary structural |
| [10736161](https://pubmed.ncbi.nlm.nih.gov/10736161/) | EI dimerization, Gly356 conserved with PPDK, roles in phosphoryl transfer | Primary functional |
| [18485189](https://pubmed.ncbi.nlm.nih.gov/18485189/) | Phylogenomics: PTS bacterial origin; EI/HPr vertical, EII by HGT | Primary phylogenomic |
| [17478425](https://pubmed.ncbi.nlm.nih.gov/17478425/) | PtsN (EIINtr) growth-phase/nitrogen-dependent phosphorylation | Primary functional |
| [29394395](https://pubmed.ncbi.nlm.nih.gov/29394395/) | Cra genome-wide: 39 sites, 97 regulon genes (ChIP-exo/RNA-seq) | Primary genomic |
| [21115656](https://pubmed.ncbi.nlm.nih.gov/21115656/) | Genomic SELEX: up to ~178 Cra-controlled promoters | Primary genomic |
| [36289548](https://pubmed.ncbi.nlm.nih.gov/36289548/) | FruR engineering redirects global carbon flux | Primary applied |

Together these papers support each of the six confirmed findings with concordant, cross-lineage evidence. The strongest claims — the fused FruB architecture, group translocation, and EI/PPDK homology — rest on multiple independent structural and sequence studies. The weaker or more variable claims — Cra polarity and F1P-vs-FBP effector identity — are flagged as lineage-dependent or unresolved.

---

## 10. Limitations and Knowledge Gaps

- **Organism heterogeneity.** The composite model draws on at least five bacterial genera. Domain architecture is conserved, but kinetic parameters, effector affinities, and regulatory polarity are not guaranteed to transfer.
- **No direct fructose-EIIC structure in hand.** Translocation mechanism is inferred from glucose-superfamily EIIC; a fructose (glucitol/mannitol-family) FruA structure is a genuine gap.
- **F1P/FBP effector ambiguity** remains partially unresolved and may be condition-dependent.
- **Quantitative flux and channeling.** Whether the FruB fusion measurably improves phosphotransfer channeling relative to split components has not been quantified here.
- **This review is literature-synthesis-based**; no new experimental or sequence analysis was performed beyond consolidating published evidence.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Structural determination of a fructose-specific FruA (EIIB–EIIC)** in multiple conformational states (cryo-EM) to confirm the elevator mechanism for the glucitol/mannitol-family transporter specifically.
2. **Quantitative phosphotransfer kinetics of intact FruB vs. reconstituted split EI/HPr/EIIA** to test the channeling hypothesis for the fusion.
3. **Systematic effector titration** (F1P vs. FBP) against purified Cra/FruR from *E. coli*, *P. putida*, and *V. cholerae* to resolve effector identity and explain the repressor/activator polarity switch.
4. **Phylogenetic census of FruB-type fusions** across Proteobacteria to map where the EI–HPr–EIIA fusion arose and how often split architectures persist, using EI/HPr (vertical markers) as the backbone.
5. **In vivo dissection of FruB→PtsN cross-talk** under defined carbon/nitrogen regimes to determine its physiological output and confirm the substrate-state gating (fructose-on/succinate-off).
6. **Metabolic-engineering validation:** exploit FruK/FruR nodes to redirect flux (building on FruR engineering for L-phenylalanine) as a functional test of the module boundary and the F1P signal.

---

*Prepared as a commissioned review synthesis. Confidence is highest for the core mechanistic and architectural claims (multiple independent structural/sequence studies across lineages) and explicitly lower for regulatory polarity and effector-identity questions, which are lineage-dependent and partly unresolved.*


## Artifacts

- [OpenScientist final report](bacterial_fructose_pts_catabolism-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_fructose_pts_catabolism-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33476373
2. PMID:22708906
3. PMID:17478425
4. PMID:29394395
5. PMID:21115656
6. PMID:31214989
7. PMID:29784777
8. PMID:2193161
9. PMID:7496537
10. PMID:1850730
11. PMID:15670601
12. PMID:8805571
13. PMID:10736161
14. PMID:18485189
15. PMID:36289548