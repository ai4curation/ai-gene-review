---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T22:12:08.925507'
end_time: '2026-08-12T22:29:21.602314'
duration_seconds: 1032.68
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: 2-aminoethylphosphonate degradation by PhnWX
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00440
  pathway_id: ppu00440
  pathway_name: Phosphonate and phosphinate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00440 with 2 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- phnX: PP_2208 | Q88KT1 | Phosphonoacetaldehyde hydrolase (Phosphonatase)
    (EC 3.11.1.1) (Phosphonoacetaldehyde phosphonohydrolase) (EC 3.11.1.1; primary
    bucket kegg:ppu00440)

    - phnW: PP_2209 | Q88KT0 | 2-aminoethylphosphonate--pyruvate transaminase (EC
    2.6.1.37) (2-aminoethylphosphonate aminotransferase) (AEP transaminase) (AEPT)
    (EC 2.6.1.37; primary bucket kegg:ppu00440)'
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__2-aminoethylphosphonate-degradation-by-phnwx__ppu00440-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__2-aminoethylphosphonate-degradation-by-phnwx__ppu00440-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

2-aminoethylphosphonate degradation by PhnWX in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00440
- Resolved ID: ppu00440
- Resolved name: Phosphonate and phosphinate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00440 with 2 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- phnX: PP_2208 | Q88KT1 | Phosphonoacetaldehyde hydrolase (Phosphonatase) (EC 3.11.1.1) (Phosphonoacetaldehyde phosphonohydrolase) (EC 3.11.1.1; primary bucket kegg:ppu00440)
- phnW: PP_2209 | Q88KT0 | 2-aminoethylphosphonate--pyruvate transaminase (EC 2.6.1.37) (2-aminoethylphosphonate aminotransferase) (AEP transaminase) (AEPT) (EC 2.6.1.37; primary bucket kegg:ppu00440)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Module/Pathway/Taxon Review: 2-Aminoethylphosphonate Degradation by PhnWX in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target pathway/bucket:** KEGG `ppu00440` — "Phosphonate and phosphinate metabolism"
**Module area:** other_kegg_pathway (no module YAML resolved)
**Candidate genes:** PP_2208 (*phnX*, Q88KT1), PP_2209 (*phnW*, Q88KT0)

---

## 1. Executive Summary

The 2-aminoethylphosphonate (2-AEP, ciliatine) degradation module is **satisfiable and effectively complete** in *Pseudomonas putida* KT2440. The two canonical catabolic steps — transamination of 2-AEP and hydrolysis of the resulting phosphonoacetaldehyde — are encoded by an **adjacent, co-oriented *phnWX* gene pair**: PP_2209 (*phnW*, 2-aminoethylphosphonate:pyruvate transaminase, EC 2.6.1.37, KO K03430) and PP_2208 (*phnX*, phosphonoacetaldehyde hydrolase / "phosphonatase," EC 3.11.1.1, KO K05306). These two loci constitute the entirety of the KEGG `ppu00440` bucket for this strain. Both are Swiss-Prot reviewed, but their catalytic assignments rest on **HAMAP-rule inference (ECO:0000255)**, not direct KT2440 enzymology. Direct biochemical evidence for the identical two-enzyme route exists in other *P. putida* strains (NG2 and BIRD-1), which supports strong functional transfer to KT2440.

Critically, the **broad KEGG map `ppu00440` overstates the strain's true metabolic capability**. KT2440 degrades 2-AEP *exclusively* via the phosphonatase route. KEGG orthology queries confirm it **lacks the entire C–P lyase core** (*phnGHIJKLM*, KOs K06162–K06166, K05780–K05781), the **oxidative PhnY*/PhnZ pathway** (K21195/K21196), and phosphonoacetate hydrolase. These branches of the "Phosphonate and phosphinate metabolism" map are therefore **not encoded** in this organism and should be marked `not_expected_in_target_taxon` rather than treated as gaps.

For curation, the two core steps should be marked **covered**; the upstream **2-AEP uptake step is genome-encoded but ambiguous** (`candidate_uncertain`) — a phosphonate/phosphite ABC system (PP_0824–0827) and an ambiguously annotated putrescine-family ABC operon (PP_1722–1726) are both plausible importers, but no experimentally named dedicated AEP transporter (AepXVW/AepP/AepSTU) is annotated in KT2440. A divergent **LysR-family regulator, PP_2210**, adjacent to *phnWX*, is the candidate AepR ortholog. Finally, some broad HAD-superfamily GO terms attached to PP_2208 (phosphoglycolate phosphatase / DNA-repair activities) are **likely over-propagation** and should not be counted toward module satisfiability.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the process is

The relevant biochemical process is the **degradation of 2-aminoethylphosphonate (2-AEP)**, a naturally abundant phosphonate bearing a chemically stable C–P bond, into central metabolites plus inorganic phosphate. In KT2440 this proceeds by the **phosphonatase (substrate-specific) pathway**, a two-step route:

```
                 phnW (PP_2209)                       phnX (PP_2208)
                 EC 2.6.1.37                          EC 3.11.1.1
   2-AEP + pyruvate  ───────────►  phosphonoacetaldehyde  ───────────►  acetaldehyde + Pi
                 + L-alanine          (+ H2O)
   (RHEA:17021)                       (RHEA:18905)
   PLP-dependent class-V             Mg2+-dependent HAD-superfamily
   aminotransferase                  hydrolase; Schiff-base Lys
```

The transaminase (PhnW) transfers the amino group of 2-AEP to pyruvate, yielding **phosphonoacetaldehyde** and L-alanine. The phosphonatase (PhnX) then hydrolytically cleaves the C–P bond of phosphonoacetaldehyde to release **acetaldehyde** and **inorganic phosphate**. Acetaldehyde feeds central carbon metabolism; Pi is assimilated. This route liberates phosphorus, carbon, and nitrogen from 2-AEP.

### 2.2 Pathway boundaries — what to keep separate

The KEGG map `ppu00440` "Phosphonate and phosphinate metabolism" is a **broad overview bucket** that aggregates several mechanistically distinct sub-pathways which should **not** be conflated for KT2440:

- **C–P lyase pathway** (*phnGHIJKLM* + accessory *phnCDE*, *phnNOP*): a broad-specificity, radical-SAM-based C–P cleavage machine used for many phosphonates including methylphosphonate. **Absent in KT2440.**
- **Oxidative 2-AEP pathway** (PhnY*/PhnZ): a non-heme Fe(II) oxygenase route converting 2-AEP to glycine + Pi, characteristic of certain marine bacteria. **Absent in KT2440.**
- **Phosphonoacetate hydrolase** (*phnA*): degrades phosphonoacetate (a different substrate). **Not the KT2440 route.**
- **Phosphite/methylphosphonate oxidation** (ptxD etc.): reduced-P metabolism, mechanistically separate.

Only the **phosphonatase (PhnWX) branch** is instantiated in KT2440. Neighboring maps that should stay distinct include general **phosphate/phosphonate transport (ABC systems)**, **alanine/pyruvate metabolism** (downstream of the transamination), and the **PHO regulon** (phosphate-starvation response), which is a regulatory network rather than a catabolic pathway.

### 2.3 Alternate names and database definitions

- Substrate: **2-aminoethylphosphonate**, **2-AEP**, **2-AEPn**, **AEP**, **ciliatine**, **(2-aminoethyl)phosphonic acid**.
- *phnW* product: **2-aminoethylphosphonate—pyruvate transaminase / aminotransferase (AEPT / AEP transaminase)**, EC 2.6.1.37, KO K03430, HAMAP MF_01376.
- *phnX* product: **phosphonoacetaldehyde hydrolase / phosphonatase / phosphonoacetaldehyde phosphonohydrolase**, EC 3.11.1.1, KO K05306, HAMAP MF_01375.
- The operon as a system is referred to in the *Pseudomonas* literature as **"PhnWX"** (the transaminase–phosphonatase system).

---

## 3. Expected Step Model

| Step | Reaction | Enzyme (EC / KO) | KT2440 gene | Status |
|------|----------|------------------|-------------|--------|
| S0 (upstream) | 2-AEP import across inner membrane | ABC transporter (various) | PP_0824–0827 and/or PP_1722–1726 (ambiguous) | `candidate_uncertain` |
| S1 | 2-AEP + pyruvate → phosphonoacetaldehyde + L-Ala | PhnW, EC 2.6.1.37 / K03430 | **PP_2209** | **covered** |
| S2 | phosphonoacetaldehyde + H₂O → acetaldehyde + Pi | PhnX, EC 3.11.1.1 / K05306 | **PP_2208** | **covered** |
| R (regulation) | substrate-inducible transcriptional control | LysR-type (AepR) | PP_2210 (candidate) | `candidate_uncertain` |
| Alt-A | C–P lyase (broad phosphonate cleavage) | PhnGHIJKLM / K06162–K06166 etc. | — | `not_expected_in_target_taxon` |
| Alt-B | oxidative 2-AEP → glycine + Pi | PhnY*/PhnZ / K21195/K21196 | — | `not_expected_in_target_taxon` |
| Alt-C | phosphonoacetate hydrolysis | PhnA | — | `not_expected_in_target_taxon` |

The **two-step phosphonatase core (S1 + S2) is fully covered**. Import (S0) and regulation (R) are present in the genome but require gene-name-level resolution. The three alternative branches are absent and expected to be absent.

---

## 4. Candidate Genes and Evidence

### 4.1 PP_2209 — *phnW* (2-AEP:pyruvate transaminase; Q88KT0)

**Role.** Catalyzes the committed first step: PLP-dependent transamination of 2-AEP with pyruvate to give phosphonoacetaldehyde + L-alanine (RHEA:17021). Classified by HAMAP MF_01376 as a class-V (fold-type I) aminotransferase.

**Evidence type.** Swiss-Prot reviewed; catalytic assignment via **HAMAP rule (ECO:0000255)** — i.e., high-confidence family inference, **not** a direct KT2440 assay. Strong functional support comes from *P. putida* strains where the identical activity was measured directly: in strain **NG2**, cell-free extracts contained "2-aminoethylphosphonic acid:pyruvate aminotransferase and phosphonoacetaldehyde hydrolase (phosphonatase) activities which were inducible by the presence of 2-aminoethylphosphonic acid" ([PMID: 9841125](https://pubmed.ncbi.nlm.nih.gov/9841125/)). In *P. putida* **BIRD-1**, the operon is explicitly named "the 2AEP transaminase-phosphonatase system (PhnWX)" ([PMID: 35229442](https://pubmed.ncbi.nlm.nih.gov/35229442/)).

**Curation caveats.** Because both direct-assay strains are *P. putida* (same species), transfer to KT2440 is **strong**. No known paralog competes for this KO in KT2440. Recommend **covered**.

### 4.2 PP_2208 — *phnX* (phosphonoacetaldehyde hydrolase / phosphonatase; Q88KT1)

**Role.** Catalyzes the second, C–P-bond-cleaving step: hydrolysis of phosphonoacetaldehyde to acetaldehyde + Pi (RHEA:18905). A **Mg²⁺-dependent HAD-superfamily** hydrolase (HAMAP MF_01375). Located at genome coordinates ~2,514,559–2,515,386 (complement), immediately adjacent to *phnW* (PATRIC pegs 2330/2331).

**Evidence type.** Swiss-Prot reviewed with HAMAP-rule catalytic assignment. The **enzyme mechanism is directly established** in orthologs: recombinant phosphonatases from *Bacillus cereus* and *Salmonella typhimurium* were purified and shown to use a **Schiff-base lysine** mechanism. In *B. cereus*, "reaction … with phosphonoacetaldehyde or acetaldehyde in the presence of NaBH₄ resulted in complete loss of enzymatic activity" ([PMID: 3132206](https://pubmed.ncbi.nlm.nih.gov/3132206/)); the *S. typhimurium* enzyme's mechanism "was verified … by phosphonoacetaldehyde-sodium borohydride-induced inactivation and by site-directed mutagenesis of the catalytic lysine 53" ([PMID: 9649311](https://pubmed.ncbi.nlm.nih.gov/9649311/)). KT2440 PhnX belongs to the same HAMAP family, so the mechanism transfers with **high confidence** — but the direct assays were in non-*Pseudomonas* hosts, so this is **enzyme-family evidence, not a KT2440-specific assay**.

**Curation caveats.** As a HAD-superfamily member, PP_2208 may carry **over-propagated broad GO terms** (e.g., generic phosphoglycolate-phosphatase or DNA-repair "phosphatase" activities common to HAD annotations). These should **not** be counted toward module satisfiability; only the EC 3.11.1.1 phosphonatase activity is relevant. Recommend **covered**.

### 4.3 PP_2210 — LysR-family regulator (candidate AepR)

**Role.** Immediately downstream of *phnW*, forming a *phnX*–*phnW*–*regulator* neighborhood (PP_2208–PP_2209–PP_2210). This is the strong candidate **AepR ortholog**. In *P. putida* BIRD-1, a LysR-type regulator "termed AepR, upstream of the 2AEP transaminase-phosphonatase system (PhnWX)" governs induction ([PMID: 35229442](https://pubmed.ncbi.nlm.nih.gov/35229442/)). Regulation is dual: global stress control acts "only … upon depletion of C, N, or P, controlled by CbrAB, NtrBC, or PhoBR respectively. However, the presence of 2AEP was necessary for full gene expression" ([PMID: 35229442](https://pubmed.ncbi.nlm.nih.gov/35229442/)). Consistent with this, AEP catabolism in *P. putida* NG2 was substrate-inducible "regardless of the phosphate status of the cells" ([PMID: 9841125](https://pubmed.ncbi.nlm.nih.gov/9841125/)) — i.e., **phosphate-starvation-independent**.

**Curation caveats.** The AepR assignment for PP_2210 is by synteny + homology, not direct KT2440 experiment. Mark `candidate_uncertain`.

### 4.4 Transport candidates (upstream step S0)

Two genome-encoded ABC systems are plausible for 2-AEP import; **neither is unambiguous**:

- **PP_0824–0827** — a phosphonate/phosphite ABC importer: PP_0824 *ptxB* (K02044, phosphonate substrate-binding protein), PP_0825 *phnC* (K02041, ATPase, EC 7.3.2.2), PP_0826 *phnE* (K02042, permease), PP_0827 *ptxC* (K02042, permease). Note: **no separate *phnD*/K02043** is present in this strain.
- **PP_1722–1726** — an ABC operon whose two permeases are GenBank-annotated "putative 2-aminoethylphosphonate transport system permease," yet whose KEGG KOs are **spermidine/putrescine-type (K02052–K02055)**, with an adjacent GntR regulator (PP_1727). This is a **conflicting / likely over-propagated annotation**.

No AepXVW/AepP/AepSTU ortholog is annotated by name in KT2440. The experimentally characterized dedicated 2AEP transporters were defined in marine bacteria: "we identify three bacterial 2-aminoethylphosphonate (2AEP) transporters, named AepXVW, AepP and AepSTU, whose synthesis is independent of phosphate concentrations" ([PMID: 34315891](https://pubmed.ncbi.nlm.nih.gov/34315891/)). Because KT2440 lacks these by name, its AEP uptake route is **inferred/ambiguous** — mark `candidate_uncertain`.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Confirmed absences (not gaps — genuinely not expected)

KEGG KO-linkage queries against organism `ppu` returned **ABSENT** for every C–P lyase core cistron: *phnG* (K06166), *phnH* (K05781), *phnI* (K05780), *phnJ* (K06162), *phnK* (K06163), *phnL* (K06164), *phnM* (K06165). The obligatory nature of these genes is established: "each of these strains contains phnGHIJKLM genes necessary in the C-P bond cleavage mechanism" ([PMID: 31792787](https://pubmed.ncbi.nlm.nih.gov/31792787/)). Their absence means KT2440 **cannot** run the broad-specificity C–P lyase route. Similarly, the **oxidative pathway** genes *phnY** (K21195) and *phnZ* (K21196) are ABSENT. The two degradative pathways are recognized as distinct and differentially distributed: "Homologous genes for both C-P lyase and phosphonatase degradative pathways are distributed in distantly related bacterial species" ([PMID: 16245012](https://pubmed.ncbi.nlm.nih.gov/16245012/)). KT2440 possesses **only the phosphonatase branch**.

**Curation consequence:** These branches of `ppu00440` should be scored `not_expected_in_target_taxon`, not `gap`. Failing to make this distinction would falsely flag the module as incomplete.

### 5.2 Ambiguities

- **2-AEP import (S0):** Two candidate ABC systems (PP_0824–0827; PP_1722–1726) but no named dedicated importer. The PP_1722–1726 "2-AEP permease" labels **conflict** with their spermidine/putrescine KO mapping. Genuine uncertainty.
- **Regulator (R):** PP_2210 is a strong-but-inferred AepR candidate.
- **Transporter completeness:** The PP_0824–0827 system lacks a separate *phnD* (K02043) substrate-binding component annotation, complicating confident assignment as a bona-fide phosphonate importer.

### 5.3 Likely over-annotations

- **PP_2208 broad HAD GO terms** (phosphoglycolate phosphatase / DNA-repair phosphatase activities): common HAD-superfamily over-propagation; not relevant to the AEP module.
- **PP_1722–1726 "2-aminoethylphosphonate transporter" name**: putative label at odds with KEGG polyamine-transporter orthology — likely over-propagated from a distant homolog.

---

## 6. Module and GO-Curation Recommendations

| Module element | Recommended status | Rationale |
|----------------|--------------------|-----------|
| S1 — 2-AEP transaminase (PP_2209 / PhnW) | **covered** | Swiss-Prot + HAMAP; direct activity in *P. putida* NG2/BIRD-1 |
| S2 — phosphonatase (PP_2208 / PhnX) | **covered** | Swiss-Prot + HAMAP; direct mechanism in *B. cereus*/*S. typhimurium* orthologs |
| S0 — 2-AEP uptake | **candidate_uncertain** | Genome-encoded ABC systems, but importer identity ambiguous |
| R — AepR regulator (PP_2210) | **candidate_uncertain** | Strong synteny/homology, no direct KT2440 data |
| Alt-A — C–P lyase | **not_expected_in_target_taxon** | *phnGHIJKLM* KOs all absent |
| Alt-B — oxidative PhnY*/PhnZ | **not_expected_in_target_taxon** | K21195/K21196 absent |
| Alt-C — phosphonoacetate hydrolase | **not_expected_in_target_taxon** | Different substrate; not encoded |

**Module boundary assessment.** The generic KEGG bucket `ppu00440` is **too broad** for accurate satisfiability scoring in KT2440. Recommendation: define/curate a **narrow "2-AEP phosphonatase (PhnWX) module"** capturing S1+S2 (core), with S0 and R as accessory steps. This yields a **fully satisfiable module** rather than an apparently partial `ppu00440` — i.e., the apparent incompleteness of `ppu00440` is a **module_needs_revision** artifact of overly broad boundaries, not a biological gap.

**GO-curation actions:**
- Retain EC 3.11.1.1 (GO: phosphonoacetaldehyde hydrolase activity) for PP_2208; **flag/deprioritize** generic HAD phosphatase GO terms as likely over-propagation.
- Retain EC 2.6.1.37 (GO: 2-aminoethylphosphonate–pyruvate transaminase activity) for PP_2209.
- Flag the PP_1722–1726 "2-AEP transporter" annotation for review — its KEGG orthology (polyamine) conflicts with the name.
- No new GO **term** requests appear strictly necessary (existing EC/GO cover the two steps), but a **new curated module document** for the PhnWX phosphonatase route is warranted.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_2208 (*phnX*)** — HIGH priority. Confirm the phosphonatase EC assignment and audit/strip over-propagated HAD GO terms.
2. **PP_2209 (*phnW*)** — HIGH priority. Confirm transaminase assignment; establish covered status with citation to *P. putida* NG2/BIRD-1 activity data.
3. **PP_2210 (LysR regulator)** — MEDIUM. Resolve whether it is the AepR ortholog controlling the operon.
4. **PP_1722–PP_1726 (ABC operon)** — MEDIUM. Resolve the name-vs-KO conflict (2-AEP permease label vs spermidine/putrescine KOs); determine whether it contributes to 2-AEP import.
5. **PP_0824–PP_0827 (ptxB-phnC-phnE-ptxC)** — LOW/MEDIUM. Clarify whether this phosphonate/phosphite ABC system imports 2-AEP and why *phnD* is missing.

---

## 8. Mechanistic Model and Interpretation

Synthesizing the five confirmed findings yields a coherent, species-aware picture:

```
   Extracellular 2-AEP
          │
          │  S0: ABC import (candidate: PP_0824–0827 phosphonate/phosphite
          │      ABC, or PP_1722–1726 ambiguous ABC operon)   [candidate_uncertain]
          ▼
   Cytoplasmic 2-AEP
          │
          │  S1: PhnW / PP_2209  (EC 2.6.1.37, K03430)         [COVERED]
          │      + pyruvate → + L-alanine
          ▼
   Phosphonoacetaldehyde
          │
          │  S2: PhnX / PP_2208  (EC 3.11.1.1, K05306)          [COVERED]
          │      Schiff-base Lys / HAD hydrolase; + H2O
          ▼
   Acetaldehyde  +  Pi  →  central metabolism / P assimilation

   Regulation: LysR AepR candidate PP_2210 — substrate (2AEP)-inducible,
               phosphate-starvation-independent, layered on CbrAB/NtrBC/PhoBR

   NOT ENCODED in KT2440:  C–P lyase (phnGHIJKLM) · oxidative PhnY*/PhnZ · phnA
```

The **operon architecture is decisive**: PP_2208 (*phnX*) and PP_2209 (*phnW*) are immediately adjacent, and together they are the *only* two genes KEGG maps to `ppu00440` in this strain. The presence of a divergent LysR regulator (PP_2210) directly abutting the operon matches the experimentally defined AepR/PhnWX arrangement in *P. putida* BIRD-1, strengthening the interpretation that this is a genuine, regulated catabolic operon rather than a set of orphan homologs.

The **enzymology is well understood at the family level**. The PhnW transamination is a standard PLP-dependent reaction; the PhnX step is the mechanistically interesting one — a HAD-superfamily hydrolase that cleaves the exceptionally stable C–P bond via a covalent Schiff-base intermediate on a catalytic lysine, assisted by a conserved active-site aspartate. This mechanism was proven directly in *B. cereus* and *S. typhimurium* orthologs, and because KT2440 PhnX is in the same HAMAP family (MF_01375), the assignment carries high confidence. A QM/MM study ([PMID: 18802516](https://pubmed.ncbi.nlm.nih.gov/18802516/)) offers a proton-transfer variant of the mechanism, but both models agree the reaction is a Lys/Asp-dependent HAD hydrolysis.

The **species-transfer logic** is central to curation. Direct enzyme activity for the two-step phosphonatase route was demonstrated in *P. putida* NG2 (same species), making functional transfer to KT2440 **strong**; the KT2440-specific catalytic evidence itself is HAMAP inference. The absence calls for the C–P lyase and oxidative branches are based on KEGG orthology, which is consistent with the biology (KT2440 is a soil pseudomonad using the substrate-specific phosphonatase route, not the broad C–P lyase machine).

---

## 9. Evidence Base

| PMID | Organism / Scope | Supports |
|------|------------------|----------|
| [9841125](https://pubmed.ncbi.nlm.nih.gov/9841125/) | *P. putida* NG2 (same species) | **Direct** AEP:pyruvate aminotransferase + phosphonatase activities; substrate-inducible, phosphate-independent. Strongest functional transfer to KT2440 (F001, F003). |
| [35229442](https://pubmed.ncbi.nlm.nih.gov/35229442/) | *P. putida* BIRD-1 (same species) | PhnWX operon + LysR regulator AepR; dual regulation (CbrAB/NtrBC/PhoBR + 2AEP inducer). Model for PP_2210 (F001, F003). |
| [9649311](https://pubmed.ncbi.nlm.nih.gov/9649311/) | *S. typhimurium* (family) | Schiff-base Lys53 mechanism of phosphonatase verified by NaBH₄ inactivation + mutagenesis. Underpins EC 3.11.1.1 for PhnX (F005). |
| [3132206](https://pubmed.ncbi.nlm.nih.gov/3132206/) | *B. cereus* (family) | Original active-site Schiff-base lysine evidence for phosphonatase (F005). |
| [31792787](https://pubmed.ncbi.nlm.nih.gov/31792787/) | Review / general | Establishes *phnGHIJKLM* as obligatory C–P lyase core; basis for absence call (F002). |
| [16245012](https://pubmed.ncbi.nlm.nih.gov/16245012/) | Review / general | Distinguishes C–P lyase vs phosphonatase degradative pathways and their distribution (F002). |
| [34315891](https://pubmed.ncbi.nlm.nih.gov/34315891/) | Marine bacteria | Defines dedicated 2AEP transporters (AepXVW/AepP/AepSTU); KT2440 lacks these by name → uptake ambiguous (F004). |
| [18802516](https://pubmed.ncbi.nlm.nih.gov/18802516/) | Computational | QM/MM alternative proton-transfer mechanism for phosphonoacetaldehyde hydrolase (mechanistic nuance). |
| [30810303](https://pubmed.ncbi.nlm.nih.gov/30810303/) | *Gimesia maris* | Oxidative PhnY*/PhnZ pathway characterization (branch absent in KT2440). |

---

## 10. Limitations and Knowledge Gaps

- **No KT2440-specific enzymology.** Both PhnW and PhnX catalytic roles are HAMAP-rule inferences (ECO:0000255). Direct activity is demonstrated in *other* *P. putida* strains (NG2, BIRD-1) and the phosphonatase mechanism in *B. cereus*/*S. typhimurium* — strong but indirect for KT2440 specifically.
- **Uptake unresolved.** The physiological 2-AEP importer in KT2440 is not experimentally identified; two conflicting candidate systems exist and no named dedicated importer is annotated.
- **Regulation inferred.** PP_2210 as AepR is by synteny/homology; no KT2440 transcriptomic confirmation.
- **KEGG-orthology-based absence calls.** The C–P lyase and PhnY*/PhnZ absences rest on KEGG KO linkage; while consistent and biologically sensible, a targeted genome-wide HMM search could formally exclude highly diverged homologs.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Growth phenotyping:** Test KT2440 for growth on 2-AEP as sole P (and N/C) source under phosphate-replete and -deplete conditions; expect substrate-inducible, phosphate-independent catabolism (as in NG2).
2. **Targeted knockouts:** ΔPP_2208 and ΔPP_2209 should abolish 2-AEP utilization; ΔPP_2210 should impair induction — confirming module roles.
3. **Enzyme assays:** Direct measurement of AEP:pyruvate transaminase and phosphonatase activities in KT2440 cell-free extracts to convert HAMAP inference to direct evidence.
4. **Transporter resolution:** Knock out PP_1722–1726 and PP_0824–0827 individually and in combination; measure labeled 2-AEP uptake to identify the physiological importer.
5. **Transcriptomics/reporter fusions:** Confirm PP_2210-dependent, 2-AEP-inducible expression of the *phnWX* operon.
6. **Curation actions:** Create a dedicated PhnWX phosphonatase module; mark S1/S2 covered, S0/R candidate_uncertain, and the C–P lyase / oxidative / phosphonoacetate branches not_expected_in_target_taxon; flag PP_2208 broad HAD GO terms and the PP_1722–1726 name as over-propagations; promote PP_2208 and PP_2209 to full `fetch-gene` review.

---

### Bottom line for curators

The **PhnWX 2-AEP phosphonatase module is covered and satisfiable in *P. putida* KT2440** via the adjacent PP_2209 (*phnW*) / PP_2208 (*phnX*) pair. The broad `ppu00440` bucket should be **narrowed**: mark the two core steps covered, uptake and regulation candidate_uncertain, and the C–P lyase, oxidative PhnY*/PhnZ, and phosphonoacetate branches not_expected_in_target_taxon. Watch for HAD-superfamily GO over-propagation on PP_2208 and a name/KO conflict on the PP_1722–1726 "2-AEP transporter."


## Artifacts

- [OpenScientist final report](PSEPK__2-aminoethylphosphonate-degradation-by-phnwx__ppu00440-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__2-aminoethylphosphonate-degradation-by-phnwx__ppu00440-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9841125
2. PMID:35229442
3. PMID:3132206
4. PMID:9649311
5. PMID:34315891
6. PMID:31792787
7. PMID:16245012
8. PMID:18802516