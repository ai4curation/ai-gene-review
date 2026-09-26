---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T14:03:03.846620'
end_time: '2026-08-08T14:24:25.573685'
duration_seconds: 1281.73
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: recfor_recombination
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu03440
  pathway_id: ppu03440
  pathway_name: Homologous recombination
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03440 with 12 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '24'
  candidate_genes: '- dnaN: PP_0011 | P0A120 | Beta sliding clamp (Beta clamp) (Sliding
    clamp) (Beta-clamp processivity factor) (DNA polymerase III beta sliding clamp
    subunit) (DNA polymerase III subunit beta) (primary bucket kegg:ppu03030)

    - recF: PP_0012 | Q88RW7 | DNA replication and repair protein RecF (primary bucket
    kegg:ppu03440)

    - polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary
    bucket kegg:ppu03420)

    - PP_0353: PP_0353 | Q88QY1 | Exonuclease (primary bucket kegg:ppu03030)

    - ssb: PP_0485 | Q88QK5 | Single-stranded DNA-binding protein (SSB) (primary bucket
    kegg:ppu03030)

    - holC: PP_0979 | Q88P74 | DNA polymerase III subunit chi (EC 2.7.7.7) (EC 2.7.7.7;
    primary bucket kegg:ppu03030)

    - ruvC: PP_1215 | Q88NJ2 | Crossover junction endodeoxyribonuclease RuvC (EC 3.1.21.10)
    (Holliday junction nuclease RuvC) (Holliday junction resolvase RuvC) (EC 3.1.21.10;
    primary bucket kegg:ppu03440)

    - ruvA: PP_1216 | Q88NJ1 | Holliday junction branch migration complex subunit
    RuvA (primary bucket kegg:ppu03440)

    - ruvB: PP_1217 | Q88NJ0 | Holliday junction branch migration complex subunit
    RuvB (EC 3.6.4.-) (EC 3.6.4.-; primary bucket kegg:ppu03440)

    - recO: PP_1435 | Q88MY3 | DNA repair protein RecO (Recombination protein O) (primary
    bucket kegg:ppu03440)

    - recJ: PP_1477 | Q88MU1 | Single-stranded-DNA-specific exonuclease RecJ (primary
    bucket kegg:ppu03410)

    - dnaEA: PP_1606 | Q88MG5 | DNA polymerase III subunit alpha (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - recA: PP_1629 | Q88ME4 | Protein RecA (Recombinase A) (primary bucket kegg:ppu03440)

    - holB: PP_1966 | Q88LG7 | DNA polymerase III subunit delta'' (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - dnaQ: PP_4141 | Q88FF6 | DNA polymerase III subunit epsilon (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - recR: PP_4267 | Q88F32 | Recombination protein RecR (primary bucket kegg:ppu03440)

    - dnaX: PP_4269 | Q88F30 | DNA polymerase III subunit gamma/tau (EC 2.7.7.7) (EC
    2.7.7.7; primary bucket kegg:ppu03030)

    - recD: PP_4672 | Q88DZ6 | RecBCD enzyme subunit RecD (EC 5.6.2.3) (DNA 5''-3''
    helicase subunit RecD) (Exonuclease V subunit RecD) (ExoV subunit RecD) (Helicase/nuclease
    RecBCD subunit RecD) (EC 5.6.2.3; primary bucket kegg:ppu03440)

    - recB: PP_4673 | Q88DZ5 | RecBCD enzyme subunit RecB (EC 3.1.11.5) (EC 5.6.2.4)
    (DNA 3''-5'' helicase subunit RecB) (Exonuclease V subunit RecB) (ExoV subunit
    RecB) (Helicase/nuclease RecBCD subunit RecB) (EC 3.1.11.5; 5.6.2.4; primary bucket
    kegg:ppu03440)

    - recC: PP_4674 | Q88DZ4 | RecBCD enzyme subunit RecC (Exonuclease V subunit RecC)
    (ExoV subunit RecC) (Helicase/nuclease RecBCD subunit RecC) (primary bucket kegg:ppu03440)

    - PP_4768: PP_4768 | Q88DQ5 | Exonuclease (primary bucket kegg:ppu03030)

    - holA: PP_4796 | Q88DM9 | DNA polymerase III subunit delta (EC 2.7.7.7) (EC 2.7.7.7;
    primary bucket kegg:ppu03030)

    - priA: PP_5088 | Q88CU2 | Replication restart protein PriA (ATP-dependent DNA
    helicase PriA) (EC 5.6.2.4) (DNA 3''-5'' helicase PriA) (EC 5.6.2.4; primary bucket
    kegg:ppu03440)

    - recG: PP_5310 | Q88C73 | ATP-dependent DNA helicase RecG (EC 5.6.2.4) (EC 5.6.2.4;
    primary bucket kegg:ppu03440)'
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__recfor-recombination__ppu03440-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__recfor-recombination__ppu03440-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

recfor_recombination in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03440
- Resolved ID: ppu03440
- Resolved name: Homologous recombination
- Source: KEGG

Resolved local bucket kegg:ppu03440 with 12 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 24

- dnaN: PP_0011 | P0A120 | Beta sliding clamp (Beta clamp) (Sliding clamp) (Beta-clamp processivity factor) (DNA polymerase III beta sliding clamp subunit) (DNA polymerase III subunit beta) (primary bucket kegg:ppu03030)
- recF: PP_0012 | Q88RW7 | DNA replication and repair protein RecF (primary bucket kegg:ppu03440)
- polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03420)
- PP_0353: PP_0353 | Q88QY1 | Exonuclease (primary bucket kegg:ppu03030)
- ssb: PP_0485 | Q88QK5 | Single-stranded DNA-binding protein (SSB) (primary bucket kegg:ppu03030)
- holC: PP_0979 | Q88P74 | DNA polymerase III subunit chi (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- ruvC: PP_1215 | Q88NJ2 | Crossover junction endodeoxyribonuclease RuvC (EC 3.1.21.10) (Holliday junction nuclease RuvC) (Holliday junction resolvase RuvC) (EC 3.1.21.10; primary bucket kegg:ppu03440)
- ruvA: PP_1216 | Q88NJ1 | Holliday junction branch migration complex subunit RuvA (primary bucket kegg:ppu03440)
- ruvB: PP_1217 | Q88NJ0 | Holliday junction branch migration complex subunit RuvB (EC 3.6.4.-) (EC 3.6.4.-; primary bucket kegg:ppu03440)
- recO: PP_1435 | Q88MY3 | DNA repair protein RecO (Recombination protein O) (primary bucket kegg:ppu03440)
- recJ: PP_1477 | Q88MU1 | Single-stranded-DNA-specific exonuclease RecJ (primary bucket kegg:ppu03410)
- dnaEA: PP_1606 | Q88MG5 | DNA polymerase III subunit alpha (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- recA: PP_1629 | Q88ME4 | Protein RecA (Recombinase A) (primary bucket kegg:ppu03440)
- holB: PP_1966 | Q88LG7 | DNA polymerase III subunit delta' (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- dnaQ: PP_4141 | Q88FF6 | DNA polymerase III subunit epsilon (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- recR: PP_4267 | Q88F32 | Recombination protein RecR (primary bucket kegg:ppu03440)
- dnaX: PP_4269 | Q88F30 | DNA polymerase III subunit gamma/tau (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- recD: PP_4672 | Q88DZ6 | RecBCD enzyme subunit RecD (EC 5.6.2.3) (DNA 5'-3' helicase subunit RecD) (Exonuclease V subunit RecD) (ExoV subunit RecD) (Helicase/nuclease RecBCD subunit RecD) (EC 5.6.2.3; primary bucket kegg:ppu03440)
- recB: PP_4673 | Q88DZ5 | RecBCD enzyme subunit RecB (EC 3.1.11.5) (EC 5.6.2.4) (DNA 3'-5' helicase subunit RecB) (Exonuclease V subunit RecB) (ExoV subunit RecB) (Helicase/nuclease RecBCD subunit RecB) (EC 3.1.11.5; 5.6.2.4; primary bucket kegg:ppu03440)
- recC: PP_4674 | Q88DZ4 | RecBCD enzyme subunit RecC (Exonuclease V subunit RecC) (ExoV subunit RecC) (Helicase/nuclease RecBCD subunit RecC) (primary bucket kegg:ppu03440)
- PP_4768: PP_4768 | Q88DQ5 | Exonuclease (primary bucket kegg:ppu03030)
- holA: PP_4796 | Q88DM9 | DNA polymerase III subunit delta (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03030)
- priA: PP_5088 | Q88CU2 | Replication restart protein PriA (ATP-dependent DNA helicase PriA) (EC 5.6.2.4) (DNA 3'-5' helicase PriA) (EC 5.6.2.4; primary bucket kegg:ppu03440)
- recG: PP_5310 | Q88C73 | ATP-dependent DNA helicase RecG (EC 5.6.2.4) (EC 5.6.2.4; primary bucket kegg:ppu03440)

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

# Module/Pathway/Taxon Review: `recfor_recombination` (KEGG ppu03440, Homologous Recombination) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03440` — Homologous recombination (12 primary genes; 24-gene candidate list)
**Curation goal:** Species-aware module satisfiability and gene-annotation review to support manual curation.
**Evidence basis:** Direct KEGG REST gene/KO mapping for KT2440 loci (verified this study) + mechanistic and *Pseudomonas*-genus literature. Strain-direct experimental phenotype from Akkaya et al. 2021.

---

## 1. Executive Summary

The RecFOR homologous-recombination (HR) module is **satisfiable — "covered"** in *Pseudomonas putida* KT2440. Every core RecFOR presynaptic gene is encoded and confidently identified in the genome: **recF** (PP_0012), **recO** (PP_1435), **recR** (PP_4267), the strand-exchange recombinase **recA** (PP_1629), together with the shared presynaptic accessory factors **recJ** (PP_1477), **recQ** (PP_4516) and single-stranded DNA-binding protein **ssb** (PP_0485), and the full downstream branch-migration/resolution machinery **ruvA/ruvB/ruvC** (PP_1216/PP_1217/PP_1215) and **recG** (PP_5310). In addition, the alternative RecBCD presynaptic pathway is intact (**recB** PP_4673, **recC** PP_4674, **recD** PP_4672), so KT2440 carries the two canonical parallel recombination routes described for the genus *Pseudomonas*.

The single most important curation conclusion is that **the supplied 24-gene candidate list should not be treated as ground truth — it needs revision (`module_needs_revision`)**. The list is exactly the raw KEGG `map03440` membership retrieved from the KEGG REST API, and KEGG's rendering of that map deliberately shares boxes with the DNA-replication map. As a result the list is simultaneously **over-broad** and **under-complete**. It is over-broad because 12 of the 24 loci are DNA polymerase III holoenzyme subunits, DNA polymerase I, and generic exonucleases whose primary biological role is replication or excision repair, not RecFOR recombination (dnaN, polA, PP_0353, holC, dnaEA, holB, dnaQ, dnaX, PP_4768, holA, plus ssb and recJ which are mis-bucketed). It is under-complete because several bona fide genome-encoded HR/RecFOR genes are absent from the list entirely: **recQ** (PP_4516), **recN** (PP_4729), **recX** (PP_1630, immediately adjacent to recA), **radA/sms** (PP_4644), the **sbcCD** nuclease pair (PP_2024/PP_2025), and the natural-transformation loader **dprA** (PP_0069).

A crucial strain-direct caveat qualifies the "covered" verdict: despite an apparently complete gene complement, KT2440 is experimentally a **poor homologous recombiner with a weak SOS response** ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)). Gene presence therefore does **not** equal high recombination proficiency in this organism, and this should be flagged for any downstream phenotype-linked curation. Finally, the replication-restart primosome components **priB** and **dnaT** appear genuinely absent from the genome, consistent with the *Pseudomonas* PriA–PriC restart lineage; these steps should be marked `not_expected_in_target_taxon` rather than `gap`.

---

## 2. Target-Organism Pathway Definition

### What the module encompasses

The `recfor_recombination` module represents the **RecF(OR) pathway of homologous recombination and single-stranded-DNA (ssDNA) gap repair**. Mechanistically this is the presynaptic-through-resolution process by which a recombinogenic RecA nucleoprotein filament is assembled on ssDNA gaps (as opposed to double-strand-break ends, which are the preferred substrate of the RecBCD pathway), followed by RecA-mediated homology search and strand invasion, branch migration, and Holliday-junction resolution. In *E. coli* this pathway "repairs such ssDNA gaps by processing them to produce a recombinogenic RecA nucleofilament during the presynaptic phase" ([PMID: 35653392](https://pubmed.ncbi.nlm.nih.gov/35653392/)).

The presynaptic phase specifically involves: (i) resection/extension of the ssDNA gap by the 5′→3′ exonuclease **RecJ** and the 3′→5′ helicase **RecQ**; (ii) protection of exposed ssDNA by **SSB**; and (iii) **RecFOR**-mediated displacement of SSB and loading of **RecA**. Impairing "either the extension of the ssDNA gap (mediated by the nuclease RecJ and the helicase RecQ) or the loading of RecA (mediated by RecFOR) leads to a decrease in" homology-directed gap repair ([PMID: 35653392](https://pubmed.ncbi.nlm.nih.gov/35653392/)). This is the biochemical scope that defines module membership and justifies inclusion of recQ and recJ even though the KEGG metadata files them under other buckets.

### Neighboring pathways that must be kept separate

For curation purposes the module boundary must exclude several adjacent processes whose genes bleed into KEGG `map03440`:

| Neighboring process | KEGG map | Genes drawn in erroneously |
|---|---|---|
| DNA replication (Pol III holoenzyme, Pol I) | ppu03030 | dnaN, holC, dnaEA, holB, dnaQ, dnaX, holA, ssb, PP_0353, PP_4768 |
| Base-excision / mismatch repair | ppu03410 | recJ (mis-bucketed) |
| Nucleotide-excision repair | ppu03420 | polA |
| Non-homologous end joining | — (absent in KT2440) | not applicable |

The Pol III holoenzyme subunits appear in `map03440` only because KEGG renders the same replisome cartoon in both maps; their presence in the candidate list is a **rendering artifact, not a recombination assignment**. Note that **ssb** is genuinely dual-role (it is required in both replication and RecFOR presynapsis) — it should be retained as a shared/accessory member rather than deleted.

### Alternate names and database definitions

The module is variously called the **RecF pathway**, **RecFOR pathway**, or **RecF(OR) recombination**. KEGG groups it under the umbrella map "Homologous recombination" (`map03440` / organism-specific `ppu03440`), which conflates the RecFOR and RecBCD sub-pathways into one map. The genus-level literature is explicit that these are two distinct routes: "Two pathways are responsible for homologous recombination in *Pseudomonas aeruginosa*: the RecBCD pathway and the RecFOR pathway" ([PMID: 29633970](https://pubmed.ncbi.nlm.nih.gov/29633970/)). Curators should treat `recfor_recombination` as the RecFOR-specific sub-module and, if a separate RecBCD module exists, cross-reference rather than merge.

---

## 3. Expected Step Model

The following step model represents the RecFOR pathway as expected in a Gammaproteobacterium such as KT2440, annotated with the KT2440 locus that satisfies each step.

```
  ssDNA gap (e.g., behind a stalled/reprimed replication fork)
        |
        v
  [1] Gap resection / extension
        RecJ 5'->3' exonuclease  ...... PP_1477 (recJ)      COVERED
        RecQ 3'->5' helicase     ...... PP_4516 (recQ)      COVERED (missing from list)
        |
        v
  [2] ssDNA protection
        SSB                      ...... PP_0485 (ssb)       COVERED (dual-role)
        |
        v
  [3] Mediator / RecA loading (presynapsis)
        RecFOR complex:
          RecF                   ...... PP_0012 (recF)      COVERED
          RecO                   ...... PP_1435 (recO)      COVERED
          RecR                   ...... PP_4267 (recR)      COVERED
        |
        v
  [4] Synapsis / strand exchange
        RecA recombinase         ...... PP_1629 (recA)      COVERED
        RecX (RecA modulator)    ...... PP_1630 (recX)      COVERED (missing from list)
        RadA/Sms (branch migr.)  ...... PP_4644 (radA)      COVERED (missing from list)
        |
        v
  [5] Branch migration + resolution
        RuvA                     ...... PP_1216 (ruvA)      COVERED
        RuvB                     ...... PP_1217 (ruvB)      COVERED
        RuvC                     ...... PP_1215 (ruvC)      COVERED
        RecG (alt. migration)    ...... PP_5310 (recG)      COVERED
        |
        v
  [6] Replication restart
        PriA                     ...... PP_5088 (priA)      COVERED
        PriB                     ...... ABSENT              NOT_EXPECTED
        DnaT                     ...... ABSENT              NOT_EXPECTED
        (PriA-PriC/DnaC-independent restart lineage)

  Parallel presynaptic route (double-strand-break ends):
        RecBCD                   ...... PP_4673/PP_4674/PP_4672   COVERED
  Accessory / overlapping:
        RecN (DSB cohesion/SMC)  ...... PP_4729 (recN)     COVERED (missing from list)
        SbcCD (Mre11/Rad50-like) ...... PP_2024/PP_2025    COVERED (missing from list)
        DprA (transformation)    ...... PP_0069 (dprA)     COVERED (missing from list)
```

Every catalytic step of the RecFOR pathway is encoded in KT2440. The only genuinely absent components are the accessory primosome loaders PriB and DnaT, which are lineage-specific losses and should not be scored as gaps.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence RecFOR core (retain, covered)

| Gene | Locus | UniProt | KO | Role | Evidence type |
|---|---|---|---|---|---|
| recF | PP_0012 | Q88RW7 | K03629 | RecA-loading mediator | Homology + KEGG KO; strong |
| recO | PP_1435 | Q88MY3 | K03584 | SSB displacement, RecA loading | Homology + genus structure |
| recR | PP_4267 | Q88F32 | K06187 | Forms RecF/RecO complexes | Genus structural (P. aeruginosa) |
| recA | PP_1629 | Q88ME4 | K03553 | Strand-exchange recombinase | Strain-direct (KT2440 SOS study) |
| recJ | PP_1477 | Q88MU1 | K07462 | 5′→3′ ssDNA exonuclease | Homology; mechanistic |
| recQ | PP_4516 | — | K03654 | 3′→5′ helicase, gap extension | Homology; **not in candidate list** |
| ssb | PP_0485 | Q88QK5 | K03111 | ssDNA protection (dual-role) | Homology; shared with replication |

**Curation notes.** RecF, RecO and RecR are the defining triad; the *P. aeruginosa* RecR crystal structure confirms that in this genus RecR forms RecF/RecO complexes that load RecA onto ssDNA ([PMID: 29633970](https://pubmed.ncbi.nlm.nih.gov/29633970/)), a strong genus-level transfer to KT2440. RecA is the one component with **direct KT2440 experimental characterization**, via the SOS-response study ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)). RecJ carries a KEGG primary bucket of `ppu03410` (base-excision/mismatch repair) and recQ is absent from the list entirely, yet both are integral RecFOR presynaptic factors per the mechanistic literature ([PMID: 35653392](https://pubmed.ncbi.nlm.nih.gov/35653392/)); they must be **added to / retained in** the module.

### 4.2 Downstream resolution machinery (retain, covered)

| Gene | Locus | Role |
|---|---|---|
| ruvA | PP_1216 | Holliday-junction branch-migration subunit |
| ruvB | PP_1217 | Holliday-junction branch-migration ATPase |
| ruvC | PP_1215 | Holliday-junction resolvase (EC 3.1.21.10) |
| recG | PP_5310 | Alternative branch-migration helicase |

These form a contiguous ruvCAB locus (PP_1215–PP_1217) plus recG, and are unambiguous by homology. Retain as covered.

### 4.3 RecBCD parallel pathway (retain, covered but separate sub-pathway)

| Gene | Locus | Role |
|---|---|---|
| recB | PP_4673 | Helicase/nuclease subunit (EC 3.1.11.5 / 5.6.2.4) |
| recC | PP_4674 | Recognition subunit |
| recD | PP_4672 | Helicase subunit (EC 5.6.2.3) |

Contiguous recCBD operon. These serve the DSB-end presynaptic route, parallel to RecFOR ([PMID: 29633970](https://pubmed.ncbi.nlm.nih.gov/29633970/)). Keep them associated with the HR map but flagged as **RecBCD sub-pathway**, not RecFOR proper.

### 4.4 Replication genes to REMOVE from the RecFOR module (over-annotation)

| Gene | Locus | Primary bucket | Why remove |
|---|---|---|---|
| dnaN | PP_0011 | ppu03030 | β-clamp; replication processivity |
| polA | PP_0123 | ppu03420 | DNA Pol I; NER/gap filling |
| PP_0353 | PP_0353 | ppu03030 | generic "Exonuclease" |
| holC | PP_0979 | ppu03030 | Pol III χ subunit |
| dnaEA | PP_1606 | ppu03030 | Pol III α subunit |
| holB | PP_1966 | ppu03030 | Pol III δ′ subunit |
| dnaQ | PP_4141 | ppu03030 | Pol III ε subunit |
| dnaX | PP_4269 | ppu03030 | Pol III γ/τ subunit |
| PP_4768 | PP_4768 | ppu03030 | generic "Exonuclease" |
| holA | PP_4796 | ppu03030 | Pol III δ subunit |

These ten loci are replisome/repair-polymerase components that KEGG renders in `map03440` because the same replisome cartoon is shared between the replication and recombination maps. They should be **removed from the RecFOR module** (they belong to the replication module), while noting that the replisome is of course biochemically required to complete recombination-associated DNA synthesis.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Missing-from-metadata but present-in-genome (add to module)

The candidate list omits several genome-encoded HR genes that were located directly via KEGG KO→gene mapping:

- **recQ = PP_4516** (K03654, "ATP-dependent DNA 3′-5′ helicase") — an integral presynaptic factor; its omission is the most consequential gap in the list.
- **recN = PP_4729** (K03631) — SMC-family DSB-repair cohesion factor.
- **recX = PP_1630** (K03565) — RecA modulator, located immediately adjacent to recA (PP_1629), a strong syntenic argument for functional association.
- **radA/sms = PP_4644** (K04485) — branch-migration/recombination accessory.
- **sbcC = PP_2024** (K03546) + **sbcD = PP_2025** (K03547) — Mre11/Rad50-like nuclease pair involved in end processing.
- **dprA = PP_0069** (K04096) — natural-transformation RecA loader.

All definitions were retrieved directly from the KEGG REST list endpoints. These are candidates to be **added** to the module as covered (recQ, recX) or accessory/uncertain (recN, radA, sbcCD, dprA).

### 5.2 Genuinely absent (mark not_expected_in_target_taxon)

- **priB** (K02686) and **dnaT** (K02317) — KEGG name and KO searches (`find/ppu/priB`, `find/ppu/dnaT`, `link ko:K02686`, `link ko:K02317`) returned no KT2440 gene. Their absence is consistent with a *Pseudomonas* **PriA–PriC / DnaC-independent replication-restart lineage**. PriA itself (PP_5088) is present. Mark PriB and DnaT `not_expected_in_target_taxon`, not `gap`.

### 5.3 Over-annotation / broad mappings

- The ten Pol III / Pol I / generic-exonuclease loci (Section 4.4) are the primary over-propagation problem.
- **PP_0353** and **PP_4768** are annotated only as generic "Exonuclease" — broad, non-specific mappings that should not anchor a recombination step.
- **ssb (PP_0485)** carries a replication primary bucket but is legitimately dual-role; keep it, but annotate the dual assignment.
- The broad EC numbers on helicase/nuclease subunits (e.g., recB EC 3.1.11.5 / 5.6.2.4; priA/recG EC 5.6.2.4) reflect enzyme-family generalizations and should not be over-interpreted as evidence of a specific recombination substrate.

### 5.4 Phenotype caveat (strain-direct)

Even with a complete gene complement, "*Pseudomonas putida* strain KT2440 is very sensitive to DNA damage and displays poor homologous recombination efficiencies" ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)). This inefficiency is attributed to a faulty RecA–LexA SOS interplay. Curation should record that **module satisfiability (gene presence) is decoupled from measured recombination proficiency** in this strain — a distinction that matters if the module is ever tied to functional phenotype scoring.

---

## 6. Module and GO-Curation Recommendations

**Overall module verdict: `module_needs_revision` — the pathway is `covered`, but the gene set is wrong at both boundaries.**

Recommended per-step scoring:

| Step / component | Locus | Recommended status |
|---|---|---|
| RecF | PP_0012 | covered |
| RecO | PP_1435 | covered |
| RecR | PP_4267 | covered |
| RecA | PP_1629 | covered (strain-direct) |
| RecJ (presynaptic) | PP_1477 | covered — reassign from ppu03410 bucket |
| RecQ (presynaptic) | PP_4516 | covered — **add to module** |
| SSB | PP_0485 | covered (dual-role, retain) |
| RuvABC | PP_1215/16/17 | covered |
| RecG | PP_5310 | covered |
| RecBCD | PP_4672/73/74 | covered (RecBCD sub-pathway) |
| PriA | PP_5088 | covered |
| RecX | PP_1630 | candidate — add (adjacent to recA) |
| RecN | PP_4729 | candidate_uncertain — add |
| RadA/Sms | PP_4644 | candidate_uncertain — add |
| SbcCD | PP_2024/25 | candidate_uncertain — add |
| DprA | PP_0069 | candidate_uncertain — add |
| PriB | absent | not_expected_in_target_taxon |
| DnaT | absent | not_expected_in_target_taxon |
| Pol III subunits (dnaN, holABC, dnaEA, dnaQ, dnaX) | various | remove — belongs to ppu03030 replication |
| polA | PP_0123 | remove — belongs to ppu03420 NER |
| Generic exonucleases (PP_0353, PP_4768) | — | remove — non-specific |

**Boundary correction.** The generic KEGG `map03440` boundary is **wrong for module curation** because it merges RecFOR and RecBCD and pulls in the replisome. Recommend splitting into (a) a RecFOR presynaptic module and (b) a RecBCD module, with shared downstream RuvABC/RecG resolution.

**GO-curation.** No new GO term requests appear strictly necessary; existing terms cover the process:
- GO:0000730 (DNA recombinase assembly) / GO:0000731 (DNA synthesis involved in DNA repair) for RecFOR loading,
- GO:0000724 (DSB repair via homologous recombination),
- GO:0009432 (SOS response) for the RecA/LexA caveat.

A curation note requesting that **RecQ and RecJ be annotated to the RecFOR/HR process** (rather than only to their current excision-repair buckets) would improve consistency.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority order for full individual-gene review:

1. **recQ (PP_4516)** — highest priority; missing from the list, integral presynaptic helicase, needs explicit module assignment and confirmation of KO K03654 identity.
2. **recX (PP_1630)** — adjacent to recA; confirm RecA-modulator role and whether it should be covered vs. accessory.
3. **recA (PP_1629)** — only strain-direct-characterized gene; promote to anchor the phenotype caveat (poor HR, weak SOS) with primary literature.
4. **recN (PP_4729), radA/sms (PP_4644), sbcC/sbcD (PP_2024/PP_2025), dprA (PP_0069)** — accessory HR genes absent from the list; review to decide covered vs. candidate_uncertain.
5. **recJ (PP_1477)** — resolve the bucket conflict (currently ppu03410) and formally reassign to the RecFOR presynaptic step.
6. **priB / dnaT** — confirm true genomic absence (negative result) to lock in `not_expected_in_target_taxon`.

The ten replication-polymerase loci do **not** warrant HR-module fetch-gene review; they should simply be removed and left to the replication module.

---

## 8. Evidence Base and Key References

| PMID | Title (abbrev.) | How it supports the review |
|---|---|---|
| [33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/) | *The faulty SOS response of P. putida KT2440 stems from an inefficient RecA-LexA interplay* | **Strain-direct.** Establishes that KT2440 recombines poorly and has a weak SOS response despite a complete gene set — the central phenotype caveat. |
| [35653392](https://pubmed.ncbi.nlm.nih.gov/35653392/) | *Single strand gap repair: the presynaptic phase...* | Defines the RecF-pathway presynaptic step and shows RecJ + RecQ (gap extension) and RecFOR (RecA loading) are integral — justifies module scope and inclusion of recQ/recJ. |
| [29633970](https://pubmed.ncbi.nlm.nih.gov/29633970/) | *Crystal structure of RecR... from P. aeruginosa PAO1* | **Genus-level.** States RecBCD and RecFOR are the two HR pathways in *Pseudomonas* and that RecR forms RecF/RecO complexes loading RecA — supports the parallel-pathway expected model. |
| [26195593](https://pubmed.ncbi.nlm.nih.gov/26195593/) | *RecF and RecR play critical roles in HR and SSA in mycobacteria* | Cross-taxon support that RecF/RecR are central mediators of RecA loading; RecR essential for all HR — reinforces core-triad importance (weak transfer, different phylum). |
| [37070184](https://pubmed.ncbi.nlm.nih.gov/37070184/) | *RecA and SSB genome-wide distribution in ssDNA gaps... in E. coli* | Genome-scale confirmation that RecA/SSB coat ssDNA gaps and that RecBCD- and RecFOR-independent RecA loading pathways exist — informs accessory-factor scope. |
| [36985274](https://pubmed.ncbi.nlm.nih.gov/36985274/) | *Chromosome segregation and cell division defects...* | Context that HR repairs both DSBs and ssDNA gaps, linking recombination to genome maintenance. |
| [32297860](https://pubmed.ncbi.nlm.nih.gov/32297860/) | *Single-molecule observation of ATP-independent SSB displacement by RecO* | Mechanistic support for RecO's SSB-displacement role during RecA loading. |

**Evidence quality summary.** Only RecA has *direct experimental characterization in KT2440* ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)). The RecFOR triad mechanism transfers **strongly** from the genus (*P. aeruginosa*, [PMID: 29633970](https://pubmed.ncbi.nlm.nih.gov/29633970/)) and **strongly** from the well-characterized *E. coli* RecF pathway ([PMID: 35653392](https://pubmed.ncbi.nlm.nih.gov/35653392/)). Gene identities (KO/locus assignments, presence/absence of recQ, recN, recX, radA, sbcCD, dprA, priB, dnaT) rest on **KEGG REST homology mapping**, not on KT2440 experiments, and should be treated as high-confidence-by-homology but not experimentally proven.

---

## 9. Limitations and Knowledge Gaps

- **Homology-based gene calls.** Presence/absence of recQ, recN, recX, radA, sbcCD, dprA, priB and dnaT was determined by KEGG KO→locus mapping and name searches, not by experimental function assays in KT2440. A false-negative in a KEGG name search could in principle mask a divergent priB/dnaT ortholog.
- **Genotype–phenotype decoupling.** The "covered" verdict is a gene-presence statement. The strain's documented poor HR efficiency ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)) means module satisfiability does not predict recombination proficiency.
- **RecFOR vs RecBCD attribution.** KEGG merges the two pathways; the exact division of labor (which route dominates ssDNA-gap vs DSB repair) has not been measured in KT2440 specifically.
- **Accessory-factor roles.** RecN, RadA, SbcCD and DprA are placed by homology; their quantitative contribution to HR in KT2440 is unknown.
- **No expression/proteomics evidence** was incorporated; all conclusions are sequence/pathway-database derived plus targeted literature.

---

## 10. Proposed Follow-up Actions

1. **Revise the module gene set**: remove the ten Pol III/Pol I/generic-exonuclease loci; add recQ (PP_4516), recX (PP_1630), and (as accessory) recN, radA, sbcCD, dprA; retain ssb as dual-role; reassign recJ to the RecFOR presynaptic step.
2. **Mark priB and dnaT `not_expected_in_target_taxon`** with a note documenting the *Pseudomonas* PriA–PriC restart lineage; verify by a dedicated ortholog search (e.g., HMM against PriB/DnaT profiles) to convert the negative KEGG search into a confident absence call.
3. **Promote recQ, recX, recA, recJ, and the accessory quartet (recN/radA/sbcCD/dprA) to full `fetch-gene` review** (Section 7 order).
4. **Split the generic HR module** into RecFOR and RecBCD sub-modules sharing downstream RuvABC/RecG, and correct the KEGG-inherited boundary.
5. **Record the phenotype caveat** ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)) in the module annotation so that gene-presence coverage is not misread as high recombination competence.
6. **Optional experimental resolution** (expert questions): (a) measure relative RecFOR vs RecBCD contributions to gap vs DSB repair in KT2440; (b) test whether recQ/recJ deletion phenocopies RecFOR deletion; (c) confirm the SOS/RecA-LexA defect's impact on module-associated repair phenotypes.

---

*Prepared for manual module-satisfiability and gene-annotation curation. Verdict: pathway `covered`, gene set `module_needs_revision`. All locus and KO identifiers verified via KEGG REST; strain-direct evidence limited to RecA/SOS ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)); mechanistic scope from E. coli/Pseudomonas ([PMID: 35653392](https://pubmed.ncbi.nlm.nih.gov/35653392/), [PMID: 29633970](https://pubmed.ncbi.nlm.nih.gov/29633970/)).*


## Artifacts

- [OpenScientist final report](PSEPK__recfor-recombination__ppu03440-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__recfor-recombination__ppu03440-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33393180
2. PMID:35653392
3. PMID:29633970