---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:14:02.241587'
end_time: '2026-09-01T14:42:12.160467'
duration_seconds: 1689.92
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Galactose catabolism (Leloir pathway)
  module_summary: The four-reaction Leloir pathway converts D-galactose to glucose
    1-phosphate. Aldose 1-epimerase supplies alpha-D-galactose, galactokinase forms
    galactose 1-phosphate, galactose-1-phosphate uridylyltransferase exchanges UMP
    with UDP-glucose, and UDP-glucose 4-epimerase regenerates UDP-glucose from UDP-galactose.
    The pathway is catalytic in its UDP-sugar co-substrate and is distinct from nucleotide-sugar
    biosynthesis or isolated UDP-galactose epimerization in organisms that lack the
    upstream GalK/GalT reactions.
  module_outline: "- Galactose catabolism (Leloir pathway)\n  - 1. anomer preparation\
    \ (mutarotation)\n  - beta-D-galactose to alpha-D-galactose\n    - GALM: galactose\
    \ mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase)\
    \ family (GALM); activity or role: aldose 1-epimerase activity)\n  - 2. phosphorylation\
    \ (committed step)\n  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate\
    \ + ADP\n    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase)\
    \ family (GALK1); activity or role: galactokinase activity)\n  - 3. uridylyl transfer\
    \ (central step)\n  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate\
    \ + UDP-galactose\n    - GALT: galactose-1-phosphate uridylyltransferase (molecular\
    \ player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or\
    \ role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)\n  - 4. UDP-sugar\
    \ recycling (regenerates UDP-glucose for GALT)\n  - UDP-galactose to UDP-glucose\
    \ (reversible)\n    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose\
    \ 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)"
  module_connections: '- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose
    + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the
    substrate phosphorylated by GALK1.

    - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose
    1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose
    1-phosphate from GALK1 is the substrate of GALT.

    - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by
    GALT is epimerised by GALE to UDP-glucose.

    - UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate
    + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated
    by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop
    that makes the pathway catalytic in UDP-glucose.'
  pathway_query: ppu00052
  pathway_id: ppu00052
  pathway_name: Galactose metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00052 with 7 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '8'
  candidate_genes: '- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase
    family protein (primary bucket kegg:ppu00052)

    - glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2;
    primary bucket kegg:ppu00052)

    - PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary
    bucket kegg:ppu00052)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)'
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__galactose_leloir_pathway__ppu00052-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__galactose_leloir_pathway__ppu00052-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Galactose catabolism (Leloir pathway) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00052
- Resolved ID: ppu00052
- Resolved name: Galactose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00052 with 7 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase family protein (primary bucket kegg:ppu00052)
- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2; primary bucket kegg:ppu00052)
- PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary bucket kegg:ppu00052)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

The four-reaction Leloir pathway converts D-galactose to glucose 1-phosphate. Aldose 1-epimerase supplies alpha-D-galactose, galactokinase forms galactose 1-phosphate, galactose-1-phosphate uridylyltransferase exchanges UMP with UDP-glucose, and UDP-glucose 4-epimerase regenerates UDP-glucose from UDP-galactose. The pathway is catalytic in its UDP-sugar co-substrate and is distinct from nucleotide-sugar biosynthesis or isolated UDP-galactose epimerization in organisms that lack the upstream GalK/GalT reactions.

### Provisional Biological Outline

- Galactose catabolism (Leloir pathway)
  - 1. anomer preparation (mutarotation)
  - beta-D-galactose to alpha-D-galactose
    - GALM: galactose mutarotase / aldose 1-epimerase (molecular player: Aldose 1-epimerase (mutarotase) family (GALM); activity or role: aldose 1-epimerase activity)
  - 2. phosphorylation (committed step)
  - alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP
    - GALK1: galactokinase (molecular player: Galactokinase (GHMP kinase) family (GALK1); activity or role: galactokinase activity)
  - 3. uridylyl transfer (central step)
  - alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose
    - GALT: galactose-1-phosphate uridylyltransferase (molecular player: Galactose-1-phosphate uridylyltransferase family (GALT); activity or role: UDP-glucose:hexose-1-phosphate uridylyltransferase activity)
  - 4. UDP-sugar recycling (regenerates UDP-glucose for GALT)
  - UDP-galactose to UDP-glucose (reversible)
    - GALE: UDP-galactose-4-epimerase (molecular player: UDP-glucose 4-epimerase family (GALE); activity or role: UDP-glucose 4-epimerase activity)

### Known Relationships Among Steps

- beta-D-galactose to alpha-D-galactose feeds into alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP: alpha-D-galactose from GALM is the substrate phosphorylated by GALK1.
- alpha-D-galactose + ATP to alpha-D-galactose 1-phosphate + ADP feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: alpha-D-galactose 1-phosphate from GALK1 is the substrate of GALT.
- alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose feeds into UDP-galactose to UDP-glucose (reversible): UDP-galactose produced by GALT is epimerised by GALE to UDP-glucose.
- UDP-galactose to UDP-glucose (reversible) feeds into alpha-D-galactose 1-phosphate + UDP-glucose to glucose-1-phosphate + UDP-galactose: UDP-glucose regenerated by GALE is the co-substrate GALT requires, closing the UDP-sugar recycling loop that makes the pathway catalytic in UDP-glucose.

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

# Module/Pathway/Taxon Review: Galactose Catabolism (Leloir Pathway) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00052` "Galactose metabolism"
**Module area:** other_kegg_pathway
**Curation verdict:** **GAP / module_needs_revision** — the catabolic Leloir pathway is **not satisfiable** in KT2440.

---

## 1. Executive Summary

The four-reaction Leloir pathway (GALM → GALK → GALT → GALE) that converts extracellular D-galactose into glucose-1-phosphate is **not encoded** in the native genome of *Pseudomonas putida* KT2440. The two committed catabolic steps — **galactokinase (GALK, EC 2.7.1.6)** and **galactose-1-phosphate uridylyltransferase (GALT, EC 2.7.7.12)** — have **no corresponding gene**. This is confirmed at two independent levels of KEGG annotation: EC-based queries (`link/ppu/ec:2.7.1.6` and `link/ppu/ec:2.7.7.12`) return zero genes, and KEGG-ortholog (KO) queries (galactokinase K00849; Gal-1-P uridylyltransferase K00965) are likewise absent. Because a linear catabolic pathway is broken the moment a committed step is missing, the module is unsatisfiable and should be curated as a **gap**, not as "covered."

The eight candidate genes assigned to `ppu00052` in the local metadata are almost entirely **central hexose-phosphate and nucleotide-sugar interconversion enzymes** that KEGG's map-based bucketing sweeps into the "Galactose metabolism" map. Only two of them belong to genuine Leloir enzyme families: **GALM** (aldose 1-epimerase/mutarotase, PP_1165) and **GALE** (UDP-glucose 4-epimerase, PP_3129 plus paralog PP_0501). Even GALE, when present, operates in KT2440's **UDP-sugar / LPS biosynthesis**, not in a catabolic UDP-glucose recycling loop, because the GALT reaction that would feed it UDP-galactose does not occur. The remaining candidates — `glk` (glucokinase, EC 2.7.1.2), `galU` (UTP-glucose-1-P uridylyltransferase, EC 2.7.7.9), `pgm`, `cpsG`, and `algC` (phosphoglucomutases/phosphomannomutases) — are generic and must **not** be counted toward the committed Leloir steps.

The two candidates most likely to trigger a false "covered" call are `glk` and `galU`, because of **EC/GO term breadth** ("sugar kinase", "uridylyltransferase"). Neither performs the Leloir chemistry: glucokinase phosphorylates glucose at C6 (not galactose at C1), and galU is a biosynthetic UDP-glucose pyrophosphorylase (glucose-1-P + UTP → UDP-glucose), not the Gal-1-P/UDP-glucose exchange catalyzed by GALT. The negative conclusion is corroborated by two independent metabolic-engineering studies that had to **install** galactose catabolism into KT2440 — one integrating the complete Leloir operon *galETKM* [PMID: 40691973], the other integrating a **De Ley–Doudoroff** oxidative pathway [PMID: 31890023] — direct experimental proof that the wild-type strain cannot catabolize galactose by either route.

---

## 2. Target-Organism Pathway Definition

### What the module is (working scope)

The **Leloir pathway of galactose catabolism** is a four-reaction, cytoplasmic route that channels free D-galactose into central carbon metabolism as glucose-1-phosphate:

1. **Mutarotation** — β-D-galactose ⇌ α-D-galactose (GALM, aldose 1-epimerase, EC 5.1.3.3)
2. **Phosphorylation (committed)** — α-D-galactose + ATP → α-D-galactose-1-phosphate + ADP (GALK, galactokinase, EC 2.7.1.6)
3. **Uridylyl transfer (central)** — Gal-1-P + UDP-glucose → glucose-1-phosphate + UDP-galactose (GALT, EC 2.7.7.12)
4. **UDP-sugar recycling** — UDP-galactose ⇌ UDP-glucose (GALE, UDP-glucose 4-epimerase, EC 5.1.3.2)

The pathway is **catalytic in its UDP-sugar co-substrate**: GALE regenerates the UDP-glucose that GALT consumes, so the net transformation is galactose → glucose-1-phosphate. This is the defining feature that distinguishes true catabolic Leloir flux from the isolated presence of GALE, which many organisms carry purely for **nucleotide-sugar (UDP-galactose) biosynthesis** feeding glycan/LPS assembly.

### Boundaries — what to keep separate

- **Nucleotide-sugar biosynthesis / LPS and EPS precursor supply.** The presence of GALE (and galU, pgm) alone indicates the cell can make and interconvert UDP-glucose/UDP-galactose for polysaccharide synthesis — this is **not** galactose catabolism. In *Acidithiobacillus ferrooxidans*, galE/galU/pgm/galT-like genes were shown to supply EPS precursors [PMID: 15932984]. The same enzymes in KT2440 serve biosynthesis.
- **De Ley–Doudoroff oxidative galactose pathway.** An alternative, Leloir-independent catabolic route (galactose → galactonate → 2-keto-3-deoxygalactonate → pyruvate + glyceraldehyde-3-P via dgoD/dgoK/dgoA). This must be checked separately as a lineage-specific alternative — and in KT2440 it, too, is absent (see Finding F005).
- **Broad KEGG overview maps** (e.g., ppu01100 "metabolic pathways", ppu00520 "amino sugar and nucleotide sugar metabolism") should not be conflated with the specific Leloir catabolic module.

### Alternate names / database definitions

- KEGG map: `ppu00052` "Galactose metabolism" (a broad map, **not** a Leloir-specific module).
- Gene symbols across bacteria: `galM` (GALM), `galK` (GALK), `galT` (GALT), `galE` (GALE), often organized as a `gal` operon (e.g., `galKETRM` in *Lactobacillus casei* [PMID: 9603808]; `galKT` in *Streptococcus pneumoniae* [PMID: 26544195]).
- The "Leloir pathway" name is used interchangeably with "galactose catabolism via galactose-1-phosphate."

---

## 3. Expected Step Model and Satisfiability in KT2440

| Step | Enzyme (family) | EC | KO | Expected gene | KT2440 status | Candidate |
|------|-----------------|-----|-----|---------------|---------------|-----------|
| 1. Mutarotation | GALM (aldose 1-epimerase) | 5.1.3.3 | K01785 | galM | **candidate_uncertain** | PP_1165 (generic; KEGG NAME "conserved protein of unknown function") |
| 2. Phosphorylation (committed) | GALK (galactokinase) | 2.7.1.6 | K00849 | galK | **GAP (absent)** | none (glk PP_1011 = EC 2.7.1.2 glucokinase) |
| 3. Uridylyl transfer (central) | GALT | 2.7.7.12 | K00965 | galT | **GAP (absent)** | none (galU PP_3821 = EC 2.7.7.9) |
| 4. UDP-sugar recycling | GALE (UDP-glc 4-epimerase) | 5.1.3.2 | K01784 | galE | **present but repurposed** (biosynthesis) | PP_3129, paralog PP_0501 |

**Conclusion:** With **two committed catabolic steps absent (GALK, GALT)**, the linear catabolic module is broken and **unsatisfiable**. GALM is present only as a generic aldose 1-epimerase of uncertain galactose specificity; GALE is present but functions in nucleotide-sugar/LPS biosynthesis rather than closing a catabolic recycling loop (there is no UDP-galactose being produced by GALT to recycle).

---

## 4. Candidate Genes and Evidence

The local metadata lists **8 candidate genes**. Below is the KEGG-ortholog-resolved assessment of each (Finding F002). Only PP_1165 and PP_3129/PP_0501 map to genuine Leloir enzyme families; the rest are central hexose-phosphate / nucleotide-sugar metabolism.

| Gene | Locus | UniProt | KEGG KO / EC | True function | Leloir role? |
|------|-------|---------|--------------|---------------|--------------|
| PP_0501 | PP_0501 | Q88QJ1 | K01784 / EC 5.1.3.2 | UDP-glucose 4-epimerase (GALE paralog) | Step 4 (biosynthetic) |
| galE | PP_3129 | Q88I72 | K01784 / EC 5.1.3.2 | UDP-glucose 4-epimerase (GALE) | Step 4 (biosynthetic) |
| PP_1165 | PP_1165 | Q88NP2 | K01785 / EC 5.1.3.3 | Aldose 1-epimerase (mutarotase) | Step 1 (uncertain) |
| glk | PP_1011 | Q88P42 | K00845 / EC 2.7.1.2 | **Glucokinase** (not galactokinase) | **none — over-propagation risk** |
| galU | PP_3821 | Q88GA4 | K00963 / EC 2.7.7.9 | **UDP-glucose pyrophosphorylase** (not GALT) | **none — over-propagation risk** |
| pgm | PP_3578 | Q88GY7 | K01835 / EC 5.4.2.2 | Phosphoglucomutase | none (central) |
| cpsG | PP_1777 | Q88LZ9 | K15778 / EC 5.4.2.8+5.4.2.2 | Phosphomannomutase/PGM | none (central) |
| algC | PP_5288 | Q88C93 | K15778 / EC 5.4.2.8+5.4.2.2 | Phosphomannomutase/PGM (alginate/LPS) | none (central) |

### High-confidence assessments

- **GALE — PP_3129 (galE) + PP_0501 (paralog).** Both are bona fide UDP-glucose 4-epimerases (K01784, EC 5.1.3.2). Their presence is real and high-confidence at the *enzyme* level, but the **biological role in KT2440 is nucleotide-sugar/LPS biosynthesis**, not catabolic UDP-glucose recycling. In a true Leloir pathway, GALE recycles the UDP-galactose that GALT produces; with GALT absent, there is no catabolic UDP-galactose to recycle, so GALE cannot be counted as "covering" a catabolic step. Curation-relevant caveat: **paralog ambiguity** — two GALE-family genes exist and should not be double-counted, and neither implies catabolism. (GALE-family genes function in LPS/precursor biosynthesis across bacteria, e.g., orfH8 complementing a *Salmonella* galE mutant [PMID: 10858186]; galE in the *A. ferrooxidans* EPS-precursor cluster [PMID: 15932984].)

- **GALM — PP_1165.** Assigned K01785 (aldose 1-epimerase, EC 5.1.3.3), but the KEGG NAME is "conserved protein of unknown function." It is a **generic aldose 1-epimerase**, not demonstrated to be galactose-specific. Aldose 1-epimerases act on multiple aldohexoses; mutarotase activity alone does not establish a committed galactose-catabolic role. Verdict: **candidate_uncertain**.

### Likely over-propagations (do NOT count as Leloir steps) — Finding F003

- **glk — PP_1011 (glucokinase, K00845, EC 2.7.1.2).** Mechanistically distinct from galactokinase: glucokinase phosphorylates **glucose at C6**, whereas GALK phosphorylates **galactose at C1** (EC 2.7.1.6). Broad "sugar kinase" GO/EC terms can cause this to be miscounted as satisfying the committed phosphorylation step. It does **not**.
- **galU — PP_3821 (UTP-glucose-1-P uridylyltransferase, K00963, EC 2.7.7.9).** A **biosynthetic UDP-glucose pyrophosphorylase** (glucose-1-P + UTP → UDP-glucose + PPi). This is the biosynthetic uridylyltransferase — completely different from GALT (EC 2.7.7.12), which exchanges UMP between Gal-1-P and UDP-glucose. Because both carry "uridylyltransferase" in their names, galU is the single most likely gene to be **falsely** mapped to the central Leloir step. It does **not** perform GALT chemistry.
- **pgm (PP_3578), cpsG (PP_1777), algC (PP_5288).** Phosphoglucomutase / phosphomannomutase enzymes of central carbon and nucleotide-sugar metabolism. They convert glucose-1-P ⇌ glucose-6-P (downstream of, or parallel to, the Leloir output) and support LPS/alginate biosynthesis. Not Leloir catabolic steps.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Confirmed gaps (committed steps absent)

Two orthogonal KEGG queries confirm the absence of the committed catabolic steps (Findings F001, F005):

- **EC level:** `link/ppu/ec:2.7.1.6` (galactokinase) → **0 genes**; `link/ppu/ec:2.7.7.12` (Gal-1-P uridylyltransferase) → **0 genes**.
- **KO level:** galactokinase (K00849) → **absent**; Gal-1-P uridylyltransferase (K00965) → **absent**.

### The De Ley–Doudoroff alternative is also absent

A lineage-specific oxidative alternative to Leloir was checked and ruled out at the KO level (Finding F005):

- galactonate dehydratase **dgoD (K01684) — absent**
- 2-oxo-3-deoxygalactonate kinase **dgoK (K00875) — absent**
- KDPG-galactonate aldolase **dgoA (K01631) — absent**
- galactose dehydrogenase **(K18649) — absent**

So KT2440 lacks **both** known galactose-catabolic routes natively.

### Over-annotation risks summary

| Risk | Gene | Why it's misleading |
|------|------|---------------------|
| Kinase over-propagation | glk (PP_1011) | "sugar kinase"/EC 2.7.1.x breadth; is glucokinase not galactokinase |
| Uridylyltransferase over-propagation | galU (PP_3821) | shares "uridylyltransferase" with GALT; is biosynthetic UDP-Glc pyrophosphorylase |
| Map-bucket inflation | pgm, cpsG, algC | central mutases swept into ppu00052 broad map |
| Paralog double-count | PP_3129 + PP_0501 | two GALE genes; biosynthetic, not catabolic |
| GALM specificity | PP_1165 | generic aldose 1-epimerase, "unknown function" |

---

## 6. Module and GO-Curation Recommendations

### Per-step module status (Finding F004)

| Module step | Recommended status | Rationale |
|-------------|---------------------|-----------|
| 1. GALM (mutarotation) | **candidate_uncertain** | PP_1165 generic aldose 1-epimerase, not proven galactose-specific |
| 2. GALK (phosphorylation) | **gap** | no gene; EC 2.7.1.6 and K00849 empty |
| 3. GALT (uridylyl transfer) | **gap** | no gene; EC 2.7.7.12 and K00965 empty |
| 4. GALE (recycling) | **present-but-repurposed** (biosynthesis; not catabolic) | PP_3129 + PP_0501 function in nucleotide-sugar/LPS biosynthesis |
| **Whole module** | **module_needs_revision / gap** | two committed catabolic steps absent → unsatisfiable |

### Module boundary judgment

The generic Leloir module boundaries are **biochemically correct** but the KEGG `ppu00052` bucket is **too broad** for KT2440: it aggregates central hexose-phosphate and nucleotide-sugar enzymes (glk, galU, pgm, cpsG, algC) that create a false impression of pathway completeness. Recommendation:

- **Do not mark the catabolic Leloir module "covered."** Mark it a **gap** with `module_needs_revision`.
- Explicitly annotate glk and galU as **excluded** from the GALK/GALT steps (over-propagation guards).
- Consider splitting the KEGG map bucket so that biosynthetic UDP-sugar interconversion (GALE, galU, pgm) is tracked separately from catabolic galactose utilization.

### GO-curation notes

- Avoid transferring GO:galactokinase activity or GO:UDP-glucose:hexose-1-P uridylyltransferase activity to any KT2440 gene — no gene qualifies.
- PP_1165: retain generic **aldose 1-epimerase activity** (GO:0004034) but **do not** upgrade to galactose-specific catabolic annotation without direct assay.
- PP_3129/PP_0501: annotate as **UDP-glucose 4-epimerase (GO:0003978)** in the **nucleotide-sugar biosynthesis** context, not galactose catabolism.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_1165 (putative GALM).** Highest priority. It is the only candidate for step 1 and is annotated "conserved protein of unknown function." A full review should establish substrate specificity (galactose vs. glucose/other aldoses) and genomic context (is it near any cryptic catabolic genes?).
2. **PP_3821 (galU) and PP_1011 (glk).** Promote to confirm the **over-propagation exclusion** — verify EC 2.7.7.9 and EC 2.7.1.2 assignments respectively and formally record that they do **not** satisfy the GALT/GALK steps. This protects against automated recount.
3. **PP_3129 (galE) + PP_0501.** Promote to resolve **paralog roles** and confirm the biosynthetic (LPS/nucleotide-sugar) rather than catabolic context; ensure they are not double-counted.

Lower priority (central metabolism, unlikely to change verdict): pgm (PP_3578), cpsG (PP_1777), algC (PP_5288).

---

## 8. Mechanistic Model / Interpretation

```
              CANONICAL LELOIR (what the module expects)
  b-D-Gal --GALM--> a-D-Gal --GALK--> Gal-1-P --GALT--> Glc-1-P
   (5.1.3.3)          (2.7.1.6)          |    (2.7.7.12)
                                         |  <---- UDP-Glc
                                         v
                                    UDP-Gal --GALE--> UDP-Glc (recycled)
                                              (5.1.3.2)

              WHAT KT2440 ACTUALLY HAS
  b-D-Gal --[PP_1165?]--> a-D-Gal --?--X   GALK ABSENT
                                           GALT ABSENT
                                           -----------------------
  UDP-Glc <==GALE (PP_3129/PP_0501)==> UDP-Gal   [biosynthesis only]
       ^                                    for LPS / nucleotide-sugars
       |
   galU / pgm / algC / cpsG   (central hexose-P & UDP-sugar supply)
```

The KT2440 genome retains the **biosynthetic/recycling arm** (GALE) and a possible **mutarotase** (PP_1165), but is missing the **entrance machinery** — the committed galactokinase and the central uridylyltransferase — that would let free galactose flow into central metabolism. Consequently the "recycling" arm has nothing to recycle from a catabolic standpoint: GALE serves anabolism (making UDP-galactose for glycoconjugates), which is the opposite direction of Leloir catabolism.

This interpretation is not merely computational. Two metabolic-engineering studies independently demonstrate that wild-type KT2440 cannot use galactose and had to be **retrofitted**:

- **Leloir retrofit:** engineers integrated the complete Leloir operon *galETKM* (including galK and galT) plus a lactose permease into the KT2440 chromosome to enable lactose/galactose utilization [PMID: 40691973] — direct evidence the native strain lacks galK and galT.
- **De Ley–Doudoroff retrofit:** a separate study installed an entirely different (oxidative) galactose-catabolic pathway into *P. putida* [PMID: 31890023] — indicating that neither the Leloir nor a native oxidative route works in the wild type.

Both results are **direct, target-organism evidence** and converge on the same conclusion as the KEGG EC/KO analysis.

---

## 9. Evidence Base

| PMID | Organism | Relevance | Supports/Challenges |
|------|----------|-----------|---------------------|
| [PMID: 40691973](https://pubmed.ncbi.nlm.nih.gov/40691973/) | *P. putida* KT2440 | Engineers integrated Leloir *galETKM* + *lacY* into KT2440 chromosome to enable galactose/lactose use | **Supports** (direct): native strain lacks galK/galT |
| [PMID: 31890023](https://pubmed.ncbi.nlm.nih.gov/31890023/) | *P. putida* | Integrated a De Ley–Doudoroff galactose pathway into the chromosome | **Supports** (direct): no functional native galactose catabolism |
| [PMID: 15932984](https://pubmed.ncbi.nlm.nih.gov/15932984/) | *A. ferrooxidans* | gal cluster (galE/galK/pgm/galM + galU, galT-like) supplies EPS/UDP-sugar precursors | **Context**: GALE/galU serve biosynthesis, not always catabolism |
| [PMID: 9603808](https://pubmed.ncbi.nlm.nih.gov/9603808/) | *L. casei* | Canonical gal operon galKETRM with galK/galT/galE enzyme activities | **Reference model** of a complete Leloir operon (contrast to KT2440) |
| [PMID: 12839781](https://pubmed.ncbi.nlm.nih.gov/12839781/) | *L. raffinolactis* | aga-galKT operon; galK+galT required for galactoside catabolism | **Reference model**: committed galK/galT define catabolic capability |
| [PMID: 26544195](https://pubmed.ncbi.nlm.nih.gov/26544195/) | *S. pneumoniae* | galK required for growth on galactose | **Supports**: GALK is the committed, indispensable catabolic step |
| [PMID: 10858186](https://pubmed.ncbi.nlm.nih.gov/10858186/) | *L. borgpetersenii* | GalE-like gene complements *Salmonella* galE in LPS biosynthesis | **Context**: GALE-family = biosynthesis (LPS), not catabolism |
| [PMID: 10993714](https://pubmed.ncbi.nlm.nih.gov/10993714/) | *S. cerevisiae* | GALT catalyzes second step of Leloir, following GALK, preceding GALE | **Reference** for canonical step order and GALT centrality |

**Verified direct-organism quotes:**
- *"the expression of β-galactosidase gene lacZ on a plasmid was accompanied with integration of galactose Leloir pathway genes galETKM and lactose permease gene lacY into the chromosome of KT2440"* [PMID: 40691973].
- *"we integrated a De Ley-Doudoroff catabolic pathway for galactose catabolism into the chromosome of"* [PMID: 31890023].

---

## 10. Limitations and Knowledge Gaps

- **Absence of evidence vs. evidence of absence.** The GALK/GALT gaps rest on KEGG EC/KO annotation completeness. While corroborated by two orthogonal query types (EC and KO) and by direct engineering studies, a divergent, unannotated galactokinase or uridylyltransferase cannot be fully excluded by KEGG alone. A HMM/profile search against the KT2440 proteome would strengthen the negative.
- **GALM specificity unresolved.** PP_1165's true substrate range (galactose vs. glucose vs. other aldoses) is not experimentally established; "aldose 1-epimerase" is a broad activity.
- **GALE directionality/role inferred.** The assignment of PP_3129/PP_0501 to biosynthesis is inferred from pathway logic and homology (no galactose catabolic sink exists), not from a KT2440-specific flux measurement.
- **No transporter analysis.** Even a complete Leloir pathway requires a galactose uptake system; this review did not assess galactose transport, another potential bottleneck.
- **Species transfer.** The reference operon studies (*L. casei*, *L. raffinolactis*, *S. pneumoniae*, *A. ferrooxidans*, *S. cerevisiae*) are used only to define the canonical pathway and enzyme roles; they are **not** transferred to KT2440. The KT2440-specific conclusions rest on KEGG ppu queries and the two *P. putida* engineering papers.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Profile-HMM confirmation of the gaps.** Run galactokinase (GHMP kinase, GALK) and GALT (histidine-triad Gal-1-P uridylyltransferase) HMMs against UP000000556 to formally exclude a divergent, unannotated ortholog. Expected: no hit — would harden the "gap" call.
2. **Promote PP_1165 to full `fetch-gene` review.** Determine galactose specificity (literature, structural homology, operon context) to decide GALM = candidate_uncertain vs. covered vs. not_expected.
3. **Lock over-propagation guards.** In the module document, explicitly record that PP_1011 (glk, EC 2.7.1.2) and PP_3821 (galU, EC 2.7.7.9) do **not** satisfy GALK/GALT, to prevent automated recount.
4. **Annotate GALE context.** Reassign PP_3129/PP_0501 GO/pathway context to nucleotide-sugar/LPS biosynthesis; flag the paralog pair to avoid double counting.
5. **Curation action:** mark KEGG `ppu00052` catabolic Leloir module as **gap / module_needs_revision**; request a module-boundary split separating biosynthetic UDP-sugar interconversion from catabolic galactose utilization.
6. **Optional wet-lab confirmation:** growth assay of wild-type KT2440 on D-galactose as sole carbon source (expected: no growth), matching the phenotype implied by the two engineering studies.

---

### Bottom line for curators

> **Catabolic Leloir module in *P. putida* KT2440 = GAP (unsatisfiable).** GALK (EC 2.7.1.6) and GALT (EC 2.7.7.12) are absent at both EC and KO levels; the De Ley–Doudoroff alternative is also absent. GALM (PP_1165) = candidate_uncertain; GALE (PP_3129/PP_0501) present but repurposed for biosynthesis. glk and galU are over-propagation traps and must be excluded from the committed steps.


## Artifacts

- [OpenScientist final report](PSEPK__galactose_leloir_pathway__ppu00052-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__galactose_leloir_pathway__ppu00052-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:40691973
2. PMID:31890023
3. PMID:15932984
4. PMID:9603808
5. PMID:26544195
6. PMID:10858186
7. PMID:12839781
8. PMID:10993714