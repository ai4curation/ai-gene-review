---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T14:13:02.679173'
end_time: '2026-08-08T16:00:24.591152'
duration_seconds: 6441.91
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: recbcd_end_resection
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__recbcd-end-resection__ppu03440-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__recbcd-end-resection__ppu03440-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

recbcd_end_resection in Pseudomonas putida KT2440

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

# Species-Aware Review: RecBCD End Resection in *Pseudomonas putida* KT2440

**Module/bucket:** `recbcd_end_resection` (mapped to KEGG ppu03440, Homologous recombination)
**Target taxon:** *Pseudomonas putida* KT2440 — PSEPK, NCBI taxon 160488, proteome UP000000556
**Review date:** 2026-08-08 · Iteration 1

---

## 1. Executive summary

The RecBCD end-resection step of homologous recombination (HR) is **satisfiable and COVERED** in *P. putida* KT2440. All three canonical subunits are encoded in a **contiguous, co-oriented recD–recB–recC operon — PP_4672 (Q88DZ6) · PP_4673 (Q88DZ5) · PP_4674 (Q88DZ4)** — with subunit lengths matching functional *E. coli* RecBCD and the expected catalytic domains (RecB: UvrD-helicase + PDDEXK nuclease; RecC: Exonuc_V_gamma; RecD: RecD helicase). The candidate list also correctly captures the downstream/parallel HR core (RecA, RecFOR, RecJ, RuvABC, RecG, PriA).

Three curation-critical caveats:

1. **Every RecBCD annotation is homology-inferred (UniProt PE3), with no direct experimental evidence in KT2440.** Presence is confident; mechanistic detail is transferred.
2. **The end-resection *regulatory* mechanism does not transfer from *E. coli*.** Direct experiments show *P. putida* RecBCD-like enzyme has nuclease/helicase activity **but does not recognize the *E. coli* Chi site (5'-GCTGGTGG-3') and shows no Chi hotspot activity** (PMID 2559208). Any Chi-based annotation is an over-propagation.
3. **Gene presence ≠ pathway proficiency.** KT2440 is intrinsically DNA-damage-sensitive with **poor HR efficiency and a weak SOS response**, traced to an inefficient RecA–LexA interplay (PMID 33393180).

Several resection-relevant genes are **absent from the 24-gene metadata** but present in the proteome and should be added to the step model: **recN, sbcCD, sbcB (ExoI), xseA (ExoVII), recQ, radA**, plus an unexpected **Ku/LigD NHEJ system**.

---

## 2. Target-organism pathway definition

**Process included (`recbcd_end_resection`):** the *initiation* of RecA-dependent HR at a double-strand DNA break (DSB). RecBCD binds a blunt/near-blunt duplex end and couples ATP-driven unwinding (RecB 3'→5' and RecD 5'→3' motors) to nucleolytic degradation, ultimately generating a 3'-tailed ssDNA onto which RecA is loaded. In *E. coli* this switch is triggered by the Chi octamer; the equivalent trigger in *Pseudomonas* is unknown (see §5).

**Boundaries — keep separate from:**
- **RecFOR/RecJ gap repair & backup resection** (recF, recO, recR, recJ, recQ): initiates HR at ssDNA gaps and substitutes for RecBCD nuclease/loading when RecBCD is inactivated. Mechanistically adjacent, but a *distinct* initiation route — not part of RecBCD end resection proper.
- **Branch migration / resolution** (ruvABC, recG): post-synaptic, downstream of resection.
- **Replisome / replication-restart** (dnaN, dnaE, dnaQ, dnaX, holABC, ssb, polA, priA): KEGG ppu03030/03430 overlap. These co-occur in the candidate list because ppu03440 shares components, but they are not resection enzymes (priA and ssb are shared cofactors).
- **NHEJ** (ku, ligD): an independent, RecA-independent DSB pathway.

**Alternate names / DB definitions:** Exonuclease V (ExoV); "Helicase/nuclease RecBCD"; EC 3.1.11.5 (RecB nuclease), EC 5.6.2.3 (RecD helicase), EC 5.6.2.4 (RecB helicase). In Firmicutes the functional analog is **AddAB (RexAB)** — *absent* here, as expected for a gammaproteobacterium.

---

## 3. Expected step model (RecBCD end resection)

| Step | Enzyme/function | KT2440 gene | Status |
|------|-----------------|-------------|--------|
| Duplex-end binding & unwinding | RecBCD helicase (dual motor) | recB, recC, recD | **Covered** |
| 3'→5' / 5'→3' nucleolysis | RecB nuclease domain | recB | **Covered** |
| Recombinogenic switch at hotspot | (Chi in *E. coli*; unknown in *Pseudomonas*) | — | **Gap / needs revision** |
| RecA loading onto 3' ssDNA | RecBCD (or RecFOR backup) | recB/recC + recFOR | Covered (mechanism uncertain) |
| Backup/alternative resection | RecJ 5'-exo + RecQ helicase + SSB | recJ, recQ, ssb | Covered (parallel path) |
| End trimming / hairpin cleavage | SbcCD, ExoI, ExoVII | sbcC/sbcD, sbcB, xseA | Present, **not in metadata** |

---

## 4. Candidate genes and evidence

**High-confidence RecBCD core (promote-worthy):**
- **recB — PP_4673 / Q88DZ5 (1224 aa).** 3'-5' helicase + single nuclease active site; the catalytic heart of resection and RecA loading. EC 3.1.11.5 / 5.6.2.4. Homology annotation; length consistent with *E. coli* RecB (~1180 aa). **Curation caveat:** the nuclease/RecA-loading regulation is Chi-independent in *Pseudomonas* — do not transfer *E. coli* Chi mechanism.
- **recC — PP_4674 / Q88DZ4 (1160 aa).** Scaffolding/Chi-recognition subunit in *E. coli*; in *Pseudomonas* the Chi-reader function is presumed non-functional or redirected to an unknown sequence. Flag GO terms implying Chi recognition.
- **recD — PP_4672 / Q88DZ6 (691 aa).** 5'-3' motor; loss converts RecBCD to a Chi-independent recombinase in *E. coli*. Homology only.

**Correctly assigned adjacent HR genes:** recF (Q88RW7), recO (Q88MY3), recR (Q88F32), recJ (Q88MU1) — RecFOR/RecJ backup route; recA (Q88ME4) — central recombinase; ruvA/ruvB/ruvC (Q88NJ1/0/2), recG (Q88C73) — Holliday-junction migration/resolution (downstream, not resection); priA (Q88CU2) — replication restart (shared cofactor).

**Likely over-inclusions for a *resection* module (replisome/other buckets):** dnaN, polA, ssb, holC, dnaEA, holB, dnaQ, dnaX, holA, and the RNase-T exonucleases **PP_0353 / PP_4768** (see below). These belong to ppu03030/03420 replication; `ssb` is a genuine shared HR cofactor, the DNA-Pol-III subunits and RNase-T exonucleases are not resection enzymes and should not count toward RecBCD-step satisfiability.

**Annotation quality flag:** all 13 HR genes checked are **UniProt PE3 "Inferred from homology"** — none has target-strain experimental protein evidence.

**Resolved (Iteration 2):** `PP_0353` (Q88QY1, 236 aa) and `PP_4768` (Q88DQ5, 203 aa) both carry **Pfam PF00929 (RNase_T) / RNase-H-like fold (SSF53098)** — the **DEDDh 3'-5' exonuclease family** (RNase T / oligoribonuclease / DnaQ-epsilon-like proofreading). PP_4768's own UniProt function text describes Pol-III-epsilon-type proofreading activity. **Neither is a RecBCD-pathway resection nuclease** — they should be **EXCLUDED** from this module, not promoted.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Chi-site over-propagation (highest priority).** Direct evidence (PMID 2559208): P. putida/P. aeruginosa RecBCD confers recombination and ATP-dependent nuclease activity **but no Chi hotspot activity and no Chi-dependent cleavage**. → Remove/annotate-as-not-applicable any 5'-GCTGGTGG recognition claim; the *Pseudomonas* recombination-hotspot sequence is an **open question**.
- **Missing resection genes in metadata:** recN (Q88DU0), sbcC (Q88LB1)/sbcD (Q88LB0), sbcB/ExoI (Q88N51), xseA/ExoVII (Q88P26), recQ (Q88EE9), radA (Q88E24). These are bona fide end-processing / recombination factors and should be represented in the step model.
- **Unexpected pathway present:** **Ku (Q88HU8) + LigD (Q88HU3) NHEJ** — a RecA-independent DSB route absent from *E. coli*. Relevant context when reasoning about DSB-repair satisfiability, though outside the resection step itself.
- **Phenotype vs. genotype mismatch:** complete gene set but **poor HR / weak SOS** (PMID 33393180). Functional inference from presence alone is unsafe.
- **AddAB not expected** and correctly absent — do not open an AddAB gap for this taxon.

---

## 6. Module and GO-curation recommendations

| Module step | Recommendation |
|-------------|----------------|
| RecBCD binding / unwinding / nucleolysis / RecA loading | **covered** (recB/recC/recD present, contiguous, correct length) |
| Chi-triggered recombinogenic switch | **module_needs_revision / candidate_uncertain** — *E. coli* Chi model does not apply; flag as gap for the hotspot signal |
| Backup resection (RecJ/RecQ/RecFOR) | **covered**, but keep as a *separate* initiation arm from RecBCD |
| SbcCD / ExoI / ExoVII end trimming | **covered but add to metadata** (currently missing) |
| AddAB alternative | **not_expected_in_target_taxon** |

**Boundary fix:** the generic bucket conflates ppu03440 (HR) with ppu03030 (replication) genes. For a `recbcd_end_resection` module, restrict counted genes to recB/recC/recD (+ optionally recA, ssb, recJ, recQ as cofactors) and exclude DNA-Pol-III subunits.

**GO/annotation requests:** (i) a note or evidence flag that KT2440 RecBCD is **Chi-independent**; (ii) add recN, sbcC/sbcD, recQ, sbcB, xseA to the resection step; (iii) resolve broad "Exonuclease" mappings for PP_0353 and PP_4768 before module inclusion.

---

## 7. Genes to promote to full `fetch-gene` review

1. **recB (PP_4673)** — catalytic core; verify nuclease/helicase domains and the Chi-independence caveat.
2. **recC (PP_4674)** — confirm whether the Chi-recognition tunnel is degenerate/redirected in *Pseudomonas*.
3. **recD (PP_4672)** — confirm 5'-3' motor and operon context.
4. **recJ (PP_1477) + recQ (Q88EE9)** — define the backup-resection arm and its metadata placement.
5. ~~PP_0353 and PP_4768~~ — **resolved in Iteration 2: RNase T/DEDDh-family (PF00929) proofreading exonucleases, NOT RecBCD resectors. Exclude from the module; no fetch-gene needed for this module.**

**Domain confirmation (Iteration 2):** RecB carries UvrD-helicase (PF00580) + PDDEXK nuclease (PF12705) domains; RecC carries the Exonuc_V_gamma domain (PF04257); RecD carries the RecD/UvrD-like helicase core — all three subunits have the expected catalytic architecture, reinforcing the COVERED call.

---

## 8. Key references

- McKittrick NH, Smith GR. *Activation of Chi recombinational hotspots by RecBCD-like enzymes from enteric bacteria.* J Mol Biol 1989. **PMID 2559208.** — Direct evidence that *P. putida/P. aeruginosa* RecBCD lacks *E. coli* Chi recognition.
- Akkaya Ö, Aparicio T, Pérez-Pantoja D, de Lorenzo V. *The faulty SOS response of Pseudomonas putida KT2440 stems from an inefficient RecA-LexA interplay.* 2021. **PMID 33393180.** — Target-strain HR/SOS deficiency.
- Vlašić I et al. *The hybrid recombinational repair pathway operates in a χ-deficient recC1004 mutant of E. coli.* 2012. **PMID 22617484.** — RecJ/RecFOR substitute for RecBCD nuclease/loading (backup-resection logic).
- Lenhart JS et al. *RecO and RecR are necessary for RecA loading…* 2014. **PMID 24891441.** — RecFOR mediator role (transfer: strong, conserved).
- Gupta R, Shuman S, Glickman MS. *RecF and RecR play critical roles in HR and SSA of mycobacteria.* 2015. **PMID 26195593.** — Comparative caveat on RecF-pathway variability across taxa.
- UniProt proteome **UP000000556** (accessions in §4) — annotation source; all HR entries are PE3 "Inferred from homology".

**Evidence basis:** Gene presence/lengths/operon context are direct from the KT2440 reference proteome (authoritative genomic evidence). The Chi-independence and HR/SOS-weakness conclusions are **direct experimental evidence in *P. putida*** (PMIDs 2559208, 33393180). RecFOR/RecJ mediator mechanisms are transferred from *E. coli*/*B. subtilis*/mycobacteria (strong conservation, but no KT2440-specific assay). No functional RecBCD biochemistry has been published for KT2440 specifically — the largest open gap.


## Artifacts

- [OpenScientist final report](PSEPK__recbcd-end-resection__ppu03440-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__recbcd-end-resection__ppu03440-deep-research-openscientist_artifacts/final_report.pdf)