---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T15:32:25.915578'
end_time: '2026-08-31T15:48:01.846527'
duration_seconds: 935.93
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial chromosomal DNA replication
  module_summary: Reusable bacterial chromosome-replication module spanning origin
    initiation, fork unwinding and single-strand protection, RNA priming, DNA polymerase
    III synthesis and proofreading, sliding-clamp processivity, clamp loading, and
    Okazaki-fragment ligation. Exact Pseudomonas putida exemplars ground the conserved
    activities and complexes.
  module_outline: "- Bacterial chromosomal DNA replication\n  - 1. replication initiation\
    \ at the chromosomal origin\n  - DnaA-dependent origin opening\n    - DnaA replication\
    \ initiator (molecular player: bacterial DnaA family; activity or role: DNA replication\
    \ origin binding)\n  - 2. fork unwinding and single-strand protection\n  - DnaB\
    \ helicase and SSB expose and protect templates\n    - DnaB replicative helicase\
    \ (molecular player: bacterial DnaB helicase family; activity or role: 5'-3' DNA\
    \ helicase activity)\n    - SSB single-strand protection (molecular player: bacterial\
    \ single-stranded DNA-binding protein family; activity or role: single-stranded\
    \ DNA binding)\n  - 3. RNA primer synthesis\n  - DnaG primer synthesis\n    -\
    \ DnaG primase (molecular player: bacterial DnaG primase family; activity or role:\
    \ DNA-directed RNA polymerase activity)\n  - 4. processive DNA synthesis and proofreading\n\
    \  - DNA polymerase III alpha-epsilon core\n    - DNA polymerase III alpha subunit\
    \ (molecular player: bacterial DNA polymerase III alpha family; activity or role:\
    \ DNA-directed DNA polymerase activity)\n    - DNA polymerase III epsilon subunit\
    \ (molecular player: bacterial DnaQ proofreading exonuclease family; activity\
    \ or role: 3'-5' exonuclease activity)\n  - 5. sliding-clamp processivity\n  -\
    \ DnaN beta sliding clamp\n    - DnaN beta clamp (molecular player: bacterial\
    \ DNA polymerase III beta-clamp family; activity or role: DNA polymerase processivity\
    \ factor activity)\n  - 6. clamp loading and replisome coupling\n  - DnaX-containing\
    \ clamp-loader complex\n    - DnaX tau/gamma clamp-loader ATPase contribution\
    \ (molecular player: bacterial DnaX clamp-loader family; activity or role: contributes\
    \ to DNA clamp loader activity)\n  - 7. Okazaki-fragment nick sealing\n  - LigA-dependent\
    \ DNA ligation\n    - NAD-dependent DNA ligase LigA (molecular player: bacterial\
    \ NAD-dependent DNA ligase family; activity or role: DNA ligase (NAD+) activity)"
  module_connections: '- DnaA-dependent origin opening precedes DnaB helicase and
    SSB expose and protect templates

    - DnaB helicase and SSB expose and protect templates precedes DnaG primer synthesis

    - DnaG primer synthesis feeds into DNA polymerase III alpha-epsilon core

    - DnaN beta sliding clamp feeds into DNA polymerase III alpha-epsilon core

    - DnaX-containing clamp-loader complex causes DnaN beta sliding clamp

    - DNA polymerase III alpha-epsilon core precedes LigA-dependent DNA ligation'
  pathway_query: ppu03030
  pathway_id: ppu03030
  pathway_name: DNA replication
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03030 with 15 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '18'
  candidate_genes: '- dnaN: PP_0011 | P0A120 | Beta sliding clamp (Beta clamp) (Sliding
    clamp) (Beta-clamp processivity factor) (DNA polymerase III beta sliding clamp
    subunit) (DNA polymerase III subunit beta) (primary bucket kegg:ppu03030)

    - polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary
    bucket kegg:ppu03420)

    - PP_0353: PP_0353 | Q88QY1 | Exonuclease (primary bucket kegg:ppu03030)

    - dnaG: PP_0388 | P0A118 | DNA primase (EC 2.7.7.101) (EC 2.7.7.101; primary bucket
    kegg:ppu03030)

    - ssb: PP_0485 | Q88QK5 | Single-stranded DNA-binding protein (SSB) (primary bucket
    kegg:ppu03030)

    - holC: PP_0979 | Q88P74 | DNA polymerase III subunit chi (EC 2.7.7.7) (EC 2.7.7.7;
    primary bucket kegg:ppu03030)

    - rnhB: PP_1605 | Q88MG6 | Ribonuclease HII (RNase HII) (EC 3.1.26.4) (EC 3.1.26.4;
    primary bucket kegg:ppu03030)

    - dnaEA: PP_1606 | Q88MG5 | DNA polymerase III subunit alpha (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - holB: PP_1966 | Q88LG7 | DNA polymerase III subunit delta'' (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - PP_3893: PP_3893 | Q88G33 | DNA 5''-3'' helicase (EC 5.6.2.3) (EC 5.6.2.3; primary
    bucket kegg:ppu03030)

    - dnaQ: PP_4141 | Q88FF6 | DNA polymerase III subunit epsilon (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - rnhA: PP_4142 | Q88FF5 | Ribonuclease HI (RNase HI) (EC 3.1.26.4) (EC 3.1.26.4;
    primary bucket kegg:ppu03030)

    - dnaX: PP_4269 | Q88F30 | DNA polymerase III subunit gamma/tau (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - ligA: PP_4274 | Q88F25 | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase
    [NAD(+)]) (EC 6.5.1.2; primary bucket kegg:ppu03420)

    - PP_4768: PP_4768 | Q88DQ5 | Exonuclease (primary bucket kegg:ppu03030)

    - holA: PP_4796 | Q88DM9 | DNA polymerase III subunit delta (EC 2.7.7.7) (EC 2.7.7.7;
    primary bucket kegg:ppu03030)

    - dnaB: PP_4873 | Q88DF2 | Replicative DNA helicase (EC 5.6.2.3) (EC 5.6.2.3;
    primary bucket kegg:ppu03030)

    - ligB: PP_4968 | Q88D59 | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide
    synthase [NAD(+)] B) (EC 6.5.1.2; primary bucket kegg:ppu03420)'
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial chromosomal DNA replication in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03030
- Resolved ID: ppu03030
- Resolved name: DNA replication
- Source: KEGG

Resolved local bucket kegg:ppu03030 with 15 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 18

- dnaN: PP_0011 | P0A120 | Beta sliding clamp (Beta clamp) (Sliding clamp) (Beta-clamp processivity factor) (DNA polymerase III beta sliding clamp subunit) (DNA polymerase III subunit beta) (primary bucket kegg:ppu03030)
- polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03420)
- PP_0353: PP_0353 | Q88QY1 | Exonuclease (primary bucket kegg:ppu03030)
- dnaG: PP_0388 | P0A118 | DNA primase (EC 2.7.7.101) (EC 2.7.7.101; primary bucket kegg:ppu03030)
- ssb: PP_0485 | Q88QK5 | Single-stranded DNA-binding protein (SSB) (primary bucket kegg:ppu03030)
- holC: PP_0979 | Q88P74 | DNA polymerase III subunit chi (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- rnhB: PP_1605 | Q88MG6 | Ribonuclease HII (RNase HII) (EC 3.1.26.4) (EC 3.1.26.4; primary bucket kegg:ppu03030)
- dnaEA: PP_1606 | Q88MG5 | DNA polymerase III subunit alpha (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- holB: PP_1966 | Q88LG7 | DNA polymerase III subunit delta' (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- PP_3893: PP_3893 | Q88G33 | DNA 5'-3' helicase (EC 5.6.2.3) (EC 5.6.2.3; primary bucket kegg:ppu03030)
- dnaQ: PP_4141 | Q88FF6 | DNA polymerase III subunit epsilon (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- rnhA: PP_4142 | Q88FF5 | Ribonuclease HI (RNase HI) (EC 3.1.26.4) (EC 3.1.26.4; primary bucket kegg:ppu03030)
- dnaX: PP_4269 | Q88F30 | DNA polymerase III subunit gamma/tau (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- ligA: PP_4274 | Q88F25 | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)]) (EC 6.5.1.2; primary bucket kegg:ppu03420)
- PP_4768: PP_4768 | Q88DQ5 | Exonuclease (primary bucket kegg:ppu03030)
- holA: PP_4796 | Q88DM9 | DNA polymerase III subunit delta (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- dnaB: PP_4873 | Q88DF2 | Replicative DNA helicase (EC 5.6.2.3) (EC 5.6.2.3; primary bucket kegg:ppu03030)
- ligB: PP_4968 | Q88D59 | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B) (EC 6.5.1.2; primary bucket kegg:ppu03420)

## Generic Module Context

### Working Scope

Reusable bacterial chromosome-replication module spanning origin initiation, fork unwinding and single-strand protection, RNA priming, DNA polymerase III synthesis and proofreading, sliding-clamp processivity, clamp loading, and Okazaki-fragment ligation. Exact Pseudomonas putida exemplars ground the conserved activities and complexes.

### Provisional Biological Outline

- Bacterial chromosomal DNA replication
  - 1. replication initiation at the chromosomal origin
  - DnaA-dependent origin opening
    - DnaA replication initiator (molecular player: bacterial DnaA family; activity or role: DNA replication origin binding)
  - 2. fork unwinding and single-strand protection
  - DnaB helicase and SSB expose and protect templates
    - DnaB replicative helicase (molecular player: bacterial DnaB helicase family; activity or role: 5'-3' DNA helicase activity)
    - SSB single-strand protection (molecular player: bacterial single-stranded DNA-binding protein family; activity or role: single-stranded DNA binding)
  - 3. RNA primer synthesis
  - DnaG primer synthesis
    - DnaG primase (molecular player: bacterial DnaG primase family; activity or role: DNA-directed RNA polymerase activity)
  - 4. processive DNA synthesis and proofreading
  - DNA polymerase III alpha-epsilon core
    - DNA polymerase III alpha subunit (molecular player: bacterial DNA polymerase III alpha family; activity or role: DNA-directed DNA polymerase activity)
    - DNA polymerase III epsilon subunit (molecular player: bacterial DnaQ proofreading exonuclease family; activity or role: 3'-5' exonuclease activity)
  - 5. sliding-clamp processivity
  - DnaN beta sliding clamp
    - DnaN beta clamp (molecular player: bacterial DNA polymerase III beta-clamp family; activity or role: DNA polymerase processivity factor activity)
  - 6. clamp loading and replisome coupling
  - DnaX-containing clamp-loader complex
    - DnaX tau/gamma clamp-loader ATPase contribution (molecular player: bacterial DnaX clamp-loader family; activity or role: contributes to DNA clamp loader activity)
  - 7. Okazaki-fragment nick sealing
  - LigA-dependent DNA ligation
    - NAD-dependent DNA ligase LigA (molecular player: bacterial NAD-dependent DNA ligase family; activity or role: DNA ligase (NAD+) activity)

### Known Relationships Among Steps

- DnaA-dependent origin opening precedes DnaB helicase and SSB expose and protect templates
- DnaB helicase and SSB expose and protect templates precedes DnaG primer synthesis
- DnaG primer synthesis feeds into DNA polymerase III alpha-epsilon core
- DnaN beta sliding clamp feeds into DNA polymerase III alpha-epsilon core
- DnaX-containing clamp-loader complex causes DnaN beta sliding clamp
- DNA polymerase III alpha-epsilon core precedes LigA-dependent DNA ligation

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

# Module/Pathway/Taxon Review: Bacterial Chromosomal DNA Replication in *Pseudomonas putida* KT2440 (KEGG ppu03030)

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03030` "DNA replication" (local module: bacterial chromosome-replication)
**Purpose:** Support manual module satisfiability and gene-annotation curation.

## 1. Executive Summary

The KEGG **ppu03030 "DNA replication"** module is **fully satisfiable (COVERED)** in *Pseudomonas putida* KT2440. All seven expected steps of the reusable bacterial chromosome-replication module — (1) DnaA-dependent origin initiation, (2) DnaB/SSB fork unwinding and single-strand protection, (3) DnaG RNA priming, (4) Pol III α/ε processive synthesis and proofreading, (5) DnaN β-clamp processivity, (6) DnaX clamp-loader assembly with δ/δ′/χ/ψ, and (7) LigA Okazaki-fragment ligation — have high-confidence, one-to-one gene assignments in the KT2440 genome. The core replisome is completely encoded and internally consistent in UniProt annotation.

The single most important curation action is that the **replication initiator `dnaA` (PP_0010, UniProt P0A116) is a metadata gap, not a biological gap.** DnaA is present in the KT2440 genome — it sits immediately upstream of `dnaN`/PP_0011 in the canonical *dnaA–dnaN–recF–gyrB* origin-proximal cluster — but it is omitted from the 18-gene candidate list because the KEGG map03030 reference pathway does not enumerate the initiator. This locus should be added to the module metadata as a covered step.

The second key finding is that **three candidate genes are likely over-propagated / paralogous annotations that do not belong to the core replisome:** PP_0353 (Q88QY1), PP_4768 (Q88DQ5), and PP_3893 (Q88G33). Domain-signature analysis (InterPro/Pfam) cleanly discriminates these from the authentic components: PP_0353 and PP_4768 carry only the generic RNase H-like/DEDDh exonuclease fold and lack the DnaQ-proteobacterial epsilon signature (IPR006309) that uniquely marks the true proofreader `dnaQ`/PP_4141; PP_3893 carries a phage-type DnaB helicase signature (IPR019889) absent from the bona fide replicative helicase `dnaB`/PP_4873. These three should be demoted to **candidate_uncertain** and promoted to full `fetch-gene` review, but their removal does not create any module gap because every step they nominally covered is already satisfied by a higher-confidence gene. Finally, enterobacterial-lineage-specific factors (dnaC/dnaI, priB/priC/dnaT, seqA) are legitimately **not_expected_in_target_taxon**.

## 2. Target-Organism Pathway Definition

**Process included.** KEGG ppu03030 as scoped for this module covers *chromosomal* (replisome-centric) DNA replication: origin initiation, replication-fork unwinding and single-strand protection, RNA primer synthesis, processive leading/lagging-strand DNA synthesis with proofreading, sliding-clamp processivity, clamp loading and replisome coupling, and Okazaki-fragment maturation/nick sealing.

**Neighboring pathways to keep separate.** KT2440's candidate metadata already reveals the boundary tension: several genes carry a **primary bucket of kegg:ppu03420 (Nucleotide excision repair)** rather than ppu03030 — notably `polA`/PP_0123 (DNA polymerase I), `ligA`/PP_4274 (NAD-dependent DNA ligase), and `ligB`/PP_4968 (DNA ligase B). These are shared "primer-processing and nick-sealing" enzymes that participate in both replication (Okazaki maturation) and repair. For a chromosomal-replication module, `polA`, `ligA`, `rnhA`, and `rnhB` are best treated as **supporting** primer-processing functions rather than core replisome subunits. Broad overview maps (map01100 metabolic pathways; recombination/repair maps ppu03430/ppu03440) should be kept out of scope.

**Alternate names / database definitions.** The pathway is variously called "DNA replication" (KEGG map03030), the "bacterial replisome," or "DNA polymerase III holoenzyme + accessory factors." The initiator DnaA belongs to KEGG's replication-*initiation* description but is not enumerated in the map03030 enzyme list, which is why it is absent from the candidate metadata despite being biologically central. Curators should note this systematic KEGG-map limitation.

## 3. Expected Step Model

The reusable module and its ordering map onto KT2440 loci as follows:

| # | Module step | Expected activity | KT2440 gene | Locus | UniProt | Verdict |
|---|-------------|-------------------|-------------|-------|---------|---------|
| 1 | Origin initiation | DNA replication origin binding | dnaA | PP_0010 | P0A116 | **Covered (add to metadata)** |
| 2 | Fork unwinding | 5′→3′ replicative helicase | dnaB | PP_4873 | Q88DF2 | **Covered** |
| 2 | Single-strand protection | ssDNA binding | ssb | PP_0485 | Q88QK5 | **Covered** |
| 3 | RNA priming | DNA-directed RNA primer synthesis | dnaG | PP_0388 | P0A118 | **Covered** |
| 4 | Processive synthesis | DNA-directed DNA polymerase (Pol III α) | dnaEA | PP_1606 | Q88MG5 | **Covered** |
| 4 | Proofreading | 3′→5′ exonuclease (Pol III ε) | dnaQ | PP_4141 | Q88FF6 | **Covered** |
| 5 | Sliding-clamp processivity | β-clamp processivity factor | dnaN | PP_0011 | P0A120 | **Covered** |
| 6 | Clamp loading | DnaX τ/γ clamp-loader ATPase | dnaX | PP_4269 | Q88F30 | **Covered** |
| 6 | Clamp loading | δ subunit | holA | PP_4796 | Q88DM9 | **Covered** |
| 6 | Clamp loading | δ′ subunit | holB | PP_1966 | Q88LG7 | **Covered** |
| 6 | Clamp loading | χ subunit | holC | PP_0978/0979 | Q88P75/Q88P74 | **Covered (annotation swap)** |
| 6 | Clamp loading | ψ subunit | holD | PP_0978/0979 | (adjacent) | **Candidate_uncertain** |
| 6 | Core coupling | θ subunit | holE | — | — | **Candidate_uncertain / not required** |
| 7 | Nick sealing | NAD-dependent DNA ligase | ligA | PP_4274 | Q88F25 | **Covered (supporting)** |
| S | Primer processing | Pol I (nick translation) | polA | PP_0123 | Q88RK6 | **Supporting** |
| S | Primer removal | RNase HI / HII | rnhA / rnhB | PP_4142 / PP_1605 | Q88FF5 / Q88MG6 | **Supporting** |

## 4. Candidate Genes and Evidence

### 4.1 Origin initiation — the DnaA metadata gap (Finding F001)

**`dnaA` (PP_0010, UniProt P0A116)** is a reviewed UniProt entry, "Chromosomal replication initiator protein DnaA," in proteome UP000000556 (taxon 160488). It is **absent from the 18-gene candidate list** even though it is the entry point of the entire pathway. The evidence that this is a metadata artifact rather than a biological absence is strong and multi-pronged: (i) DnaA is a reviewed, high-confidence entry in the target proteome; (ii) it occupies the canonical origin-proximal position immediately upstream of `dnaN`/PP_0011 (which *is* in the candidate list), following the conserved *dnaA–dnaN–recF–gyrB* synteny (gyrB = PP_0013, confirmed present); and (iii) the omission traces directly to KEGG map03030 not enumerating the initiator. **Curation action: add PP_0010 to module metadata as a covered Step-1 gene.**

Supporting context from KT2440 chromosome biology: origin-proximal coordination of replication and segregation is an established feature of this organism, consistent with a functional DnaA-dependent origin ([PMID: 30352930](https://pubmed.ncbi.nlm.nih.gov/30352930/)).

### 4.2 Core replisome, steps 2–7 (Finding F002)

The core replisome is **fully encoded and consistently annotated** in UniProt. Each subunit has a specific, non-generic functional call:

- **`dnaB`/PP_4873** — "main replicative DNA helicase," DnaB family, 5′→3′ unwinding (Step 2).
- **`ssb`/PP_0485** — single-stranded DNA-binding protein (Step 2).
- **`dnaG`/PP_0388** — DnaG primase, EC 2.7.7.101 (Step 3).
- **`dnaEA`/PP_1606** — Pol III α subunit, EC 2.7.7.7 (Step 4, synthesis).
- **`dnaQ`/PP_4141** — Pol III ε subunit, 3′→5′ proofreading exonuclease (Step 4, proofreading).
- **`dnaN`/PP_0011** — β sliding clamp, processivity factor (Step 5).
- **`dnaX`/PP_4269** — τ/γ clamp-loader ATPase, DnaX family (Step 6).
- **`holA`/PP_4796 (δ), `holB`/PP_1966 (δ′), `holC` (χ)** — clamp-loader accessory subunits (Step 6).
- **`ligA`/PP_4274** — NAD-dependent DNA ligase LigA (Step 7).
- **Supporting:** `polA`/PP_0123 (Pol I), `rnhA`/PP_4142 (RNase HI), `rnhB`/PP_1605 (RNase HII) for Okazaki primer processing.

These are all high-confidence, one-to-one assignments and require no promotion to deep review except where noted below.

### 4.3 The χ/ψ (holC/holD) annotation swap (Finding F005)

The clamp-loader **χ and ψ subunits map to the adjacent locus pair PP_0978–PP_0979**, but with a curation-relevant inconsistency:

- **Q88P75 / PP_0978** = protein name "DNA polymerase III subunit chi" (121 aa) but carries **no gene name**.
- **Q88P74 / PP_0979** = gene name `holC` but a **blank protein name** (142 aa).

The candidate metadata assigns "chi = holC" to PP_0979, which conflicts with UniProt's chi call on PP_0978. Both loci fall in the size range of χ (~147 aa) and ψ (~137 aa) and are adjacent — the canonical *holC–holD* arrangement. A gene-name search for `holD`/ψ returns nothing, but the PP_0978–PP_0979 pair is the expected χ–ψ cassette. **Interpretation:** χ is present (locus identity needs harmonizing between UniProt and metadata), and ψ (holD) is very likely present as the unnamed partner locus. Curation action: disambiguate the PP_0978/PP_0979 pair and assign χ and ψ explicitly. This is why holD is marked **candidate_uncertain** in the step model — present by synteny/size but not name-confirmed.

### 4.4 Three over-propagated candidates (Findings F003, F007)

Three candidate genes carry generic or paralogous annotations and are **not** core replisome components:

**PP_0353 (Q88QY1)** — UniProt has no protein name, no EC number, no family assignment, and protein-existence level 4 (Predicted): a bare "Exonuclease" call. Domain analysis shows it shares only the generic RNase H-like/DEDDh exonuclease fold (Pfam PF00929; InterPro IPR013520/IPR012337/IPR036397) and **lacks the DnaQ-proteobacterial epsilon signature IPR006309**. It is an ExoX/oligoribonuclease-type exonuclease, not a replisome subunit.

**PP_4768 (Q88DQ5)** — carries only generic DnaQ/Pol-III-epsilon boilerplate function text but is **not** the epsilon subunit (the true ε is `dnaQ`/PP_4141). It is 203 aa, shares the generic RNase H-like/DEDDh fold, and — critically — **lacks IPR006309**. This is a DnaQ-family exonuclease paralog (ExoX-like), a classic case of over-propagated epsilon annotation.

**PP_3893 (Q88G33)** — annotated "DNA 5′→3′ helicase," DnaB subfamily. It shares the DnaB Pfam architecture (PF00772 + PF03796) with the authentic `dnaB`/PP_4873 but **additionally carries the phage-specific signature IPR019889 (DNA_helicase_DnaB-like_phg)** that `dnaB`/PP_4873 lacks. This marks PP_3893 as a phage/prophage-type DnaB paralog, not the chromosomal replicative helicase.

The discriminating logic is summarized below:

```
Authentic proofreader   dnaQ/PP_4141 (252 aa): DEDDh fold + IPR006054 + IPR006309  [OK] epsilon
Over-annotation         PP_4768 (203 aa):      DEDDh fold, NO IPR006309            [X] ExoX-like
Over-annotation         PP_0353 (236 aa):      DEDDh fold, NO name/EC/family, PE4  [X] predicted exo

Authentic helicase      dnaB/PP_4873:  PF00772+PF03796, NO phage signature         [OK] replicative
Over-annotation         PP_3893 (465): PF00772+PF03796 + IPR019889 (phage)         [X] phage-type
```

**Curation action:** demote PP_0353, PP_4768, PP_3893 to **candidate_uncertain**, remove from the core replisome, and promote all three to full `fetch-gene` review. Because Steps 4 (proofreading) and 2 (helicase) are already satisfied by `dnaQ`/PP_4141 and `dnaB`/PP_4873, their removal creates **no module gap**.

### 4.5 Lineage-specific replication features (Finding F004)

A gene-name survey of taxon 160488 in UniProt shows KT2440's replication accessory landscape differs from the enterobacterial paradigm:

**Present (beyond the candidate list):** `dnaE2`/PP_3119 (error-prone/translesion DNA polymerase) and `imuB`/PP_3118 (part of the *imuA–imuB–dnaE2* mutagenesis cassette); `hda`/PP_1668 (DnaA regulatory inactivation, RIDA); `priA`/PP_5088 (replication-fork restart); topoisomerases `gyrA`/PP_1767, `gyrB`/PP_0013, `parC`/PP_4912, `parE`/PP_4915; helicases/nucleases `rep`/PP_5264, `recD`/PP_4672, `recQ`/PP_4516.

**Absent by name (enterobacterial-specific, not_expected_in_target_taxon):** `dnaC` (and `dnaI`), `priB`, `priC`, `dnaT`, `holE`, `imuA`, `imuC`, `seqA`. The absence of `dnaC`, the *priB/priC/dnaT* primosome accessories, and `seqA` reflects genuine lineage divergence — *Pseudomonas* uses a DnaC-independent helicase-loading mechanism and lacks the *E. coli* SeqA sequestration system. These should not be counted as module gaps.

## 5. Gaps, Ambiguities, and Likely Over-Annotations

| Item | Category | Rationale |
|------|----------|-----------|
| dnaA / PP_0010 | **Metadata gap (add)** | Present in genome; omitted only because KEGG map03030 doesn't list the initiator |
| holC/holD (PP_0978–PP_0979) | **Ambiguity (harmonize)** | χ named on wrong locus; ψ present but unnamed; needs disambiguation |
| holE (θ) | **candidate_uncertain / not required** | No name hit; θ is dispensable and often absent outside enterobacteria |
| PP_0353 | **Over-annotation → candidate_uncertain** | Predicted (PE4), no name/EC/family; generic DEDDh exo, lacks IPR006309 |
| PP_4768 | **Over-annotation → candidate_uncertain** | DnaQ boilerplate but not ε; lacks IPR006309; ExoX-like paralog |
| PP_3893 | **Over-annotation → candidate_uncertain** | Phage-type DnaB (IPR019889); true helicase is dnaB/PP_4873 |
| polA, ligA, rnhA, rnhB | **Supporting (not core)** | Primer processing / nick sealing; polA & ligA primary-bucketed to ppu03420 |
| dnaC/dnaI, priB/priC/dnaT, seqA | **not_expected_in_target_taxon** | Enterobacterial-specific; genuine lineage divergence |

The over-annotation calls are well-justified by the documented history of KT2440 re-annotation (Finding F006). The original genome ([PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)) was substantially revised: Belda et al. re-annotated 1548 gene functions and added 242 new protein-coding genes ([PMID: 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/)), and GenBank-vs-RefSeq annotation discrepancies persist for this strain ([PMID: 41036861](https://pubmed.ncbi.nlm.nih.gov/41036861/)). This establishes both the plausibility of over-propagated calls and the value of locus-level re-curation.

## 6. Module and GO-Curation Recommendations

**Module verdict: COVERED (fully satisfiable).** All seven steps have high-confidence gene assignments (Finding F008).

Step-by-step curation status:

- **Step 1 (initiation):** COVERED — add `dnaA`/PP_0010 to metadata.
- **Step 2 (unwinding + ssDNA):** COVERED — `dnaB`/PP_4873 + `ssb`/PP_0485.
- **Step 3 (priming):** COVERED — `dnaG`/PP_0388.
- **Step 4 (synthesis + proofreading):** COVERED — `dnaEA`/PP_1606 + `dnaQ`/PP_4141.
- **Step 5 (β-clamp):** COVERED — `dnaN`/PP_0011.
- **Step 6 (clamp loader):** COVERED — `dnaX`/PP_4269 + `holA`/PP_4796 + `holB`/PP_1966 + χ/ψ at PP_0978–PP_0979; `holE`/θ candidate_uncertain (not required).
- **Step 7 (ligation):** COVERED — `ligA`/PP_4274 (supported by `polA`, `rnhA`, `rnhB`).

**Module-boundary guidance.** The generic module boundaries are essentially correct for this organism, with two refinements: (i) the module should explicitly include the initiator DnaA even though KEGG map03030 omits it; and (ii) the primer-processing/nick-sealing enzymes (`polA`, `ligA`, `rnhA`, `rnhB`) should be labeled as *supporting* functions shared with repair (ppu03420), not core replisome subunits, to avoid double-counting across modules.

**GO-curation notes.** The broad EC 2.7.7.7 (DNA-directed DNA polymerase) mapping is attached to many clamp-loader subunits (holA/holB/holC) and to the exonuclease paralogs, which is misleading — these subunits are structural/ATPase components, not catalytic polymerases. Curators should prefer specific GO terms: DNA polymerase III complex (GO:0009360), DNA clamp loader activity, single-stranded DNA binding (ssb), 3′-5′ exonuclease activity restricted to `dnaQ`, and DNA-directed DNA polymerase activity restricted to `dnaEA`. No new module documents or new GO term requests appear necessary; existing terms cover all satisfied steps.

## 7. Genes to Promote to Full Review

The following loci warrant full `fetch-gene` review:

1. **PP_0353 (Q88QY1)** — resolve identity of predicted "Exonuclease"; confirm ExoX/oligoribonuclease assignment and remove from replication module.
2. **PP_4768 (Q88DQ5)** — confirm DnaQ-family paralog (not epsilon); reassign away from Pol III core.
3. **PP_3893 (Q88G33)** — confirm phage/prophage-type DnaB paralog (IPR019889); reassign away from chromosomal replisome.
4. **PP_0978 / PP_0979 (Q88P75 / Q88P74)** — harmonize the χ (holC) / ψ (holD) annotation swap and assign gene names and protein names consistently.
5. **PP_0010 (P0A116, dnaA)** — add to module metadata as the Step-1 initiator (administrative, not a deep-review need, but must be entered).

## 8. Mechanistic Model / Synthesis

The KT2440 chromosomal replisome follows the canonical Gram-negative bacterial architecture with minimal lineage-specific modification within the core:

```
         Step 1: ORIGIN INITIATION
         DnaA (PP_0010) -- binds oriC, opens duplex
         [regulated by Hda/PP_1668, RIDA]
                 |
                 v
         Step 2: FORK UNWINDING + ssDNA PROTECTION
         DnaB helicase (PP_4873) --> 5'->3' unwinding
         SSB (PP_0485) --> coats exposed ssDNA
         [DnaC-independent loading -- no dnaC in KT2440]
                 |
                 v
         Step 3: RNA PRIMING
         DnaG primase (PP_0388) --> RNA primers
                 |
                 v
         Step 4-6: POL III HOLOENZYME
         +-----------------------------------------+
         |  a  DnaEA (PP_1606)  -- synthesis        |
         |  e  DnaQ  (PP_4141)  -- 3'->5' proofread  |
         |  b  DnaN  (PP_0011)  -- processivity clamp|
         |  clamp loader: t/g DnaX (PP_4269)         |
         |      d HolA (PP_4796), d' HolB (PP_1966)  |
         |      x/psi  PP_0978-PP_0979                |
         +-----------------------------------------+
                 |
                 v
         Step 7: OKAZAKI MATURATION
         RNase HI/HII (PP_4142/PP_1605) -- primer removal
         Pol I (PP_0123) -- gap filling
         LigA (PP_4274) -- NAD+-dependent nick sealing

   NOT in core (over-annotations -> candidate_uncertain):
     PP_0353  predicted exonuclease (ExoX-like)
     PP_4768  DnaQ-family paralog (NOT epsilon)
     PP_3893  phage-type DnaB paralog (NOT replicative helicase)

   Not expected in taxon: dnaC/dnaI, priB/priC/dnaT, seqA, holE
```

The discriminating diagnostic that resolves the three over-annotations is the **presence/absence of family-specific InterPro signatures superimposed on a shared fold**: the DEDDh exonuclease fold is shared by both the authentic proofreader and its paralogs, but only the true `dnaQ`/PP_4141 carries IPR006309; likewise the DnaB helicase fold is shared, but only the phage paralog PP_3893 carries IPR019889. This "shared-fold-plus-diagnostic-signature" logic is a reusable rule for future replication-module curation in other *Pseudomonas* strains.

## 9. Evidence Base

| PMID | Title (abbreviated) | Relevance |
|------|---------------------|-----------|
| [12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/) | *Complete genome sequence... P. putida KT2440* | Authoritative KT2440 genome underlying all PP_xxxx locus tags |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *The revisited genome of P. putida KT2440* | 1548 genes re-annotated, 242 new CDS added — justifies locus-level re-curation |
| [41036861](https://pubmed.ncbi.nlm.nih.gov/41036861/) | *Differences in GenBank and RefSeq annotations* | Documents persistent annotation discrepancies in KT2440 |
| [30352930](https://pubmed.ncbi.nlm.nih.gov/30352930/) | *Segregation but not replication of the... chromosome* | Origin-proximal replication/segregation coordination context |

Verified supporting quotations:

- [PMID: 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/): *"We identified 242 new protein-coding genes and re-annotated the functions of 1548 genes, which are linked to almost 4900 PubMed references."* — Direct evidence that KT2440 annotations have been substantially revised, justifying locus-level re-curation of the replication candidate genes.
- [PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/): *"Sequence analysis of the 6.18 Mb genome of strain KT2440 reveals diverse transport and metabolic systems."* — Establishes the authoritative KT2440 genome underlying the PP_xxxx locus tags used throughout this review.

**Evidence-type summary.** Every gene assignment in this review is grounded in **UniProt/InterPro/Pfam annotation plus genomic synteny**, cross-checked against the KEGG ppu03030 reference pathway and the re-annotated KT2440 genome. No direct target-strain biochemical or genetic experiments were located for the individual replisome subunits; transfer of mechanism from generic bacterial/*E. coli* models is **strong for the conserved core** (β-clamp, Pol III, DnaB, DnaG, SSB, LigA are near-universal) and **uncertain for lineage-specific accessories** (χ/ψ locus identity, holE presence, DnaC-independent loading).

## 10. Limitations and Knowledge Gaps

1. **Homology-based, not experimental.** Every gene assignment rests on annotation and synteny, not on direct biochemical or genetic experiments in KT2440. No target-strain knockout, complementation, or in-vitro reconstitution data were found for the individual replisome subunits.
2. **holD/ψ and holE/θ are name-inferred.** ψ is inferred present from the PP_0978–PP_0979 synteny and size range, not from a confirmed gene name. θ (holE) may be genuinely absent; its dispensability makes this hard to distinguish from a gap.
3. **The χ/ψ annotation swap** was diagnosed from a UniProt inconsistency and has not been resolved against a curated reference — it needs a full gene-level review.
4. **Over-annotation calls** rest on signature analysis; final confirmation of the alternative functions (ExoX vs oligoribonuclease for PP_0353/PP_4768; prophage origin for PP_3893) would benefit from genomic-context inspection and phylogenetic placement.
5. **Literature specificity.** Most retrieved KT2440 literature concerns metabolic engineering, biodegradation, and genome annotation rather than replication mechanism directly; mechanistic conclusions for the conserved core are therefore "strong but indirect."

## 11. Proposed Follow-up Experiments / Actions

1. **Metadata fix (immediate):** Add `dnaA`/PP_0010 to the ppu03030 module as a covered Step-1 gene.
2. **Full `fetch-gene` reviews** for PP_0353, PP_4768, PP_3893, and the PP_0978/PP_0979 pair (Section 7).
3. **Genomic-context check** for PP_3893 — determine whether it lies within an annotated prophage region, which would corroborate the phage-DnaB call.
4. **Phylogenetic placement** of PP_0353/PP_4768 among DEDDh exonucleases to assign ExoX vs oligoribonuclease vs other paralog identity.
5. **GO-term refinement:** replace broad EC 2.7.7.7 mappings on clamp-loader subunits with specific complex/activity terms; restrict 3′-5′ exonuclease activity to `dnaQ`/PP_4141.
6. **Expert question:** confirm the *Pseudomonas* DnaC-independent helicase-loading mechanism so that the absence of `dnaC` is documented as expected rather than a gap.

---

*Review completed over 5 iterations; 8 findings confirmed; 12 papers reviewed. Module verdict: **ppu03030 DNA replication is COVERED (fully satisfiable) in P. putida KT2440**.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30352930
2. PMID:12534463
3. PMID:26913973
4. PMID:41036861