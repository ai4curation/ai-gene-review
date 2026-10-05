---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:09:55.796752'
end_time: '2026-09-01T14:48:09.712986'
duration_seconds: 2293.92
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial chromosomal DNA replication
  module_summary: Reusable bacterial chromosome-replication module spanning origin
    initiation, fork unwinding and single-strand protection, RNA priming, DNA polymerase
    III synthesis and proofreading, sliding-clamp processivity, clamp loading, and
    Okazaki-fragment ligation. Verified Pseudomonas putida and Escherichia coli exemplars
    ground the conserved activities and complexes without restricting the module to
    either species.
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
    \ to DNA clamp loader activity)\n    - HolA delta clamp-loader subunit (molecular\
    \ player: bacterial HolA delta family)\n    - HolB delta-prime clamp-loader subunit\
    \ (molecular player: bacterial HolB delta-prime family)\n    - HolC chi clamp-loader\
    \ subunit (molecular player: bacterial HolC chi family)\n  - 7. Okazaki-fragment\
    \ nick sealing\n  - LigA-dependent DNA ligation\n    - NAD-dependent DNA ligase\
    \ LigA (molecular player: bacterial NAD-dependent DNA ligase family; activity\
    \ or role: DNA ligase (NAD+) activity)"
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

Reusable bacterial chromosome-replication module spanning origin initiation, fork unwinding and single-strand protection, RNA priming, DNA polymerase III synthesis and proofreading, sliding-clamp processivity, clamp loading, and Okazaki-fragment ligation. Verified Pseudomonas putida and Escherichia coli exemplars ground the conserved activities and complexes without restricting the module to either species.

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
    - HolA delta clamp-loader subunit (molecular player: bacterial HolA delta family)
    - HolB delta-prime clamp-loader subunit (molecular player: bacterial HolB delta-prime family)
    - HolC chi clamp-loader subunit (molecular player: bacterial HolC chi family)
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

# Species-Aware Review: Chromosomal DNA Replication in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03030` "DNA replication" (18 candidate genes)
**Purpose:** Support manual module satisfiability and gene-annotation curation (not a generic pathway essay).

---

## 1. Executive summary

The bacterial chromosome-replication module is **fully satisfiable** in *P. putida* KT2440. Every mechanistic step — origin initiation, fork unwinding, single-strand protection, RNA priming, processive Pol III synthesis + proofreading, sliding-clamp processivity, clamp loading, and Okazaki maturation/ligation — is encoded by a confidently identifiable gene. However, the `ppu03030` candidate list is **both incomplete and contaminated**, so it should not be used as ground truth:

- **Incomplete at the initiation step.** The initiator **dnaA (PP_0010)** and the helicase loader **dnaC (PP_1552)** are not in the bucket at all; they live in other KEGG maps. dnaA sits in the canonical **dnaA–dnaN–recF–gyrB** origin cluster (PP_0010–PP_0011–PP_0012–PP_0013), which is strong direct genomic evidence.
- **Contaminated by KO over-propagation.** Three genes carry the epsilon KO (K02342) but only **dnaQ (PP_4141)** is the replisome proofreader; **PP_0353** and **PP_4768** are DnaQ/DEDDh exonuclease paralogs. **PP_3893** carries the DnaB KO (K02314) but is a *"putative phage DNA helicase"* — the true replicative helicase is **dnaB (PP_4873)**.
- **Two accessory subunits are unannotatable.** **holD (psi)** and **holE (theta)** have **no ortholog** in KEGG (ppu), the UniProt proteome, or (for psi) a positive-control-validated Pfam/InterPro domain search — and psi is likewise undetectable in *P. aeruginosa* PAO1, i.e. a genus-level pattern. Theta absence is expected (largely enterobacteria-restricted); psi is a genuine gap/lineage-divergent call. Neither blocks satisfiability (both are non-essential; the core clamp loader DnaX₃-δ-δ'-χ is intact).
- The metadata name **"dnaEA"** for PP_1606 implies a second Pol III alpha. That paralog is **dnaE2/imuC (PP_3119)** within an **imuB–imuC (PP_3118–PP_3119)** SOS mutagenesis cassette — a translesion polymerase, **not** part of the core replisome.

**Bottom line for curation:** mark all seven module steps **covered**, but re-assign initiation to dnaA/dnaC, restrict the epsilon and helicase steps to the single true gene each, flag PP_0353/PP_4768/PP_3893 as over-propagated paralogs, log psi as a gap and theta as not_expected_in_target_taxon, and move ligB, imuC/dnaE2, rnhA/rnhB, and polA to their more appropriate repair/maturation contexts.

---

## 2. Target-organism pathway definition

**Included process (KEGG ppu03030, "DNA replication"):** the semiconservative synthesis machinery acting at the replication fork — helicase-driven unwinding, single-strand protection, primer synthesis, coordinated leading/lagging-strand Pol III holoenzyme synthesis with proofreading, sliding-clamp processivity, ATP-dependent clamp loading, and RNA-primer removal + nick ligation to mature Okazaki fragments.

**Neighboring processes to keep separate:**
- **Initiation regulation / origin licensing** — dnaA, dnaC, DiaA, Hda/regulatory inactivation. KEGG scatters dnaA/dnaC outside ppu03030; the reusable module should still treat DnaA-dependent origin opening as **step 1**.
- **DNA topology** — DNA gyrase (gyrA PP_1767 / gyrB PP_0013), topoisomerase IV (parC PP_4912 / parE PP_4915), topoisomerase I (topA PP_2139, PP_3831). Required for fork progression/decatenation but curated under topology maps, not the replisome step model.
- **Mismatch/base-excision/nucleotide-excision repair (KEGG ppu03420/ppu03430)** — polA, ligA, ligB, rnhA, rnhB are placed by KEGG in these buckets even though they physically contribute to lagging-strand maturation.
- **SOS/translesion synthesis** — imuA/imuB/dnaE2(imuC), dinB (Pol IV), umuDC/Pol V. These overlap the Pol III alpha family by homology but are a distinct mutagenesis module.

**Alternate names / database definitions:** KEGG `map03030`/`ppu03030` "DNA replication"; the replisome is also captured as KEGG modules **M00263** (bacterial DNA polymerase III complex) and by BioCyc/MetaCyc "DNA replication" and Pseudomonas Genome DB (PseudoCAP) categories. UniProt uses the eco/E. coli reference nomenclature (dnaE, dnaQ, holA–holE, dnaX, dnaN).

---

## 3. Expected step model (satisfiability call per step)

| # | Step | Expected player(s) | KT2440 gene(s) | Call |
|---|------|--------------------|----------------|------|
| 1 | Origin initiation | DnaA (+ DnaC loader) | **dnaA PP_0010** (K02313); **dnaC PP_1552** (K02315) | **covered** (outside bucket — metadata gap) |
| 2 | Fork unwinding + ssDNA protection | DnaB helicase, SSB | **dnaB PP_4873** (K02314); **ssb PP_0485** (K03111) | **covered** (exclude prophage helicase PP_3893) |
| 3 | RNA priming | DnaG primase | **dnaG PP_0388** (K02316) | **covered** |
| 4 | Pol III core synthesis + proofreading | alpha (DnaE), epsilon (DnaQ) | **dnaEA PP_1606** (K02337); **dnaQ PP_4141** (K02342) | **covered** (exclude PP_0353/PP_4768) |
| 5 | Sliding-clamp processivity | beta clamp (DnaN) | **dnaN PP_0011** (K02338) | **covered** |
| 6 | Clamp loading / replisome coupling | DnaX (tau/gamma), delta (HolA), delta' (HolB), chi (HolC), psi (HolD) | **dnaX PP_4269** (K02343); **holA PP_4796** (K02340); **holB PP_1966** (K02341); **holC PP_0979** (K02339); **holD = none** | **covered** for core loader; **psi = gap/candidate_uncertain** |
| — | (core accessory theta, HolE) | theta | **none** | **not_expected_in_target_taxon** |
| 7 | Okazaki maturation + nick sealing | Pol I (polA), RNase H (rnhA/rnhB), LigA | **polA PP_0123** (K02335); **rnhA PP_4142** (K03469); **rnhB PP_1605** (K03470); **ligA PP_4274** (K01972) | **covered** |

---

## 4. Candidate genes and evidence

**High-confidence, one-to-one core replisome genes (direct KEGG/UniProt orthology; strong):**
- **dnaN / PP_0011 (P0A120)** — beta sliding clamp (K02338). Origin-cluster context. **Covered, step 5.**
- **dnaG / PP_0388 (P0A118)** — DNA primase (K02316). **Covered, step 3.**
- **ssb / PP_0485 (Q88QK5)** — single-strand DNA-binding protein (K03111). **Covered, step 2.**
- **dnaEA / PP_1606 (Q88MG5)** — Pol III alpha (K02337). The replicative catalytic subunit. **Covered, step 4.** Caveat: "dnaEA" name implies a paralog (see dnaE2 below); confirm this is the *replicative* alpha (it is, by KO K02337).
- **dnaQ / PP_4141 (Q88FF6)** — Pol III epsilon proofreader (K02342). Adjacent to rnhA (PP_4142). **Covered, step 4.**
- **dnaX / PP_4269 (Q88F30)** — clamp-loader tau/gamma ATPase (K02343). **Covered, step 6.**
- **holA / PP_4796 (Q88DM9)** — clamp-loader delta (K02340). **Covered, step 6.**
- **holB / PP_1966 (Q88LG7)** — clamp-loader delta' (K02341). **Covered, step 6.**
- **holC / PP_0979 (Q88P74)** — clamp-loader chi (K02339). **Covered, step 6.**
- **dnaB / PP_4873 (Q88DF2)** — replicative helicase (K02314), GenBank "replicative DNA helicase (ATPase)". **Covered, step 2.**

**Okazaki-maturation genes (correct biology, but bucketed elsewhere by KEGG):**
- **polA / PP_0123 (Q88RK6)** — Pol I (K02335) with 5'→3' and 3'→5' exonuclease; removes RNA primers, fills gaps. Primary bucket ppu03420. **Covered, step 7**, cross-listed.
- **ligA / PP_4274 (Q88F25)** — NAD+-dependent DNA ligase (K01972). The **essential** replicative nick-sealer. Primary bucket ppu03420. **Covered, step 7.**
- **rnhA / PP_4142 (Q88FF5)** — RNase HI (K03469); **rnhB / PP_1605 (Q88MG6)** — RNase HII (K03470). Remove RNA primers/R-loops. Supportive of Okazaki processing but also repair; keep as accessory.

**Ambiguous / likely over-propagated (see §5).**

*Evidence type:* All assignments above are **homology/orthology-based** (KEGG KO + UniProt), corroborated by **synteny** (origin cluster, dnaQ–rnhA adjacency) and by cross-*Pseudomonas* conservation. No KT2440-specific biochemical/genetic knockouts of individual replisome subunits were found in the literature searched; the strain's genome organization is directly documented (origin/dnaA region conserved with *B. subtilis*, PMID 1552862).

---

## 5. Gaps, ambiguities, and likely over-annotations

**Over-propagated epsilon KO (K02342) — three genes, one true epsilon.**
Only **dnaQ (PP_4141)** is the replisome proofreader — it is the sole gene carrying the epsilon-specific signatures (CDD **cd06131** "DNA_pol_III_epsilon_Ecoli_like", InterPro **IPR006054 DnaQ + IPR006309 DnaQ_proteo**, PANTHER **PTHR30231:SF41**). **PP_0353** and **PP_4768** are generically named "Exonuclease" and inherit K02342 only because the whole DnaQ/DEDDh 3'→5' exonuclease superfamily maps to Pfam **PF00929 (RNase_T)** / PANTHER family **PTHR30231** / eggNOG **COG0847**. Their discriminating subfamily assignments identify them as *distinct* enzymes:
- **PP_0353** → CDD **cd06127** (generic DEDDh), PANTHER **PTHR30231:SF4 "protein NEN2"** — a NEN/oligoribonuclease-like exonuclease, **not** the replisome epsilon.
- **PP_4768** → CDD **cd06127**, PANTHER **PTHR30231:SF37 "Exodeoxyribonuclease 10" (ExoX)** — a mismatch/repair-associated 3'→5' exodeoxyribonuclease. Its UniProt "DNA polymerase III … core" FUNCTION/SUBUNIT text is transferred boilerplate, not evidence of replisome membership.

→ Both are **candidate_uncertain / remove from module**; do not count toward step 4, and re-annotate with a generic 3'→5' exonuclease term (GO:0008408) rather than the Pol III epsilon term.

**Over-propagated DnaB KO (K02314) — prophage helicase.**
**PP_3893** is a *"putative phage DNA helicase"* sharing K02314 with the real **dnaB (PP_4873)**. Metadata's generic "DNA 5'-3' helicase" label masks its prophage origin. → **not_in_module / candidate_uncertain** (prophage paralog).

**Missing accessory subunits.**
- **holD (psi):** undetectable by **three** independent methods — KEGG KO (K02344), UniProt gene/name search, and a **positive-control-validated domain search** (Pfam **PF03603** / InterPro **IPR004615**, which correctly retrieves *E. coli* holD P28632 but returns nothing in KT2440). The same domain is also absent from *P. aeruginosa* PAO1, so this is a **genus-level pattern**, not a KT2440 annotation lapse. Its chi partner (holC, Pfam PF04364) *is* present. Interpretation: psi is either genuinely absent in *Pseudomonas* or so divergent that no current family model detects it; because psi is a non-essential accessory clamp-loader subunit and the core loader (DnaX₃-δ-δ'-χ) is intact, its absence does **not** block satisfiability. → **gap / lineage-divergent** (resolve only by expert HMM/AlphaFold-structural check).
- **holE (theta):** no ortholog; theta is largely enterobacteria-restricted. → **not_expected_in_target_taxon** (expected negative).

**Second Pol III alpha = SOS polymerase, not replisome.**
**dnaE2/imuC (PP_3119, K14162)** with **imuB (PP_3118, K14161)** is the error-prone translesion cassette. The "dnaEA" name in metadata is the tell that a second alpha exists; ensure dnaE2/imuC is curated into the **SOS/mutagenesis** module, not step 4.

**Second ligase.**
**ligB (PP_4968, K01972)** shares the LigA KO. LigB is a non-essential NAD+-ligase paralog in *Pseudomonas*; **ligA (PP_4274)** is the essential replicative ligase. → keep **ligA** as the step-7 player; mark **ligB** accessory/candidate_uncertain.

**Boundary leakage.** gyrA/gyrB/parC/parE/topA are required for replication but are topology enzymes; keep them **out** of the replisome step model (separate maps).

---

## 6. Module and GO-curation recommendations

**Per-step status:**
- Step 1 initiation → **covered** via dnaA (PP_0010) + dnaC (PP_1552); **module_needs_revision**: add these loci to the reusable module's initiation slot (currently absent from the ppu03030 candidate metadata).
- Step 2 unwinding/protection → **covered** (dnaB PP_4873, ssb PP_0485); remove PP_3893 from the module.
- Step 3 priming → **covered** (dnaG PP_0388).
- Step 4 core synthesis/proofreading → **covered** (dnaEA PP_1606 + dnaQ PP_4141); exclude PP_0353, PP_4768.
- Step 5 processivity → **covered** (dnaN PP_0011).
- Step 6 clamp loading → **covered** for DnaX/δ/δ'/χ; **psi = candidate_uncertain/gap**; **theta = not_expected_in_target_taxon**.
- Step 7 ligation/maturation → **covered** (ligA PP_4274; polA PP_0123; rnhA/rnhB accessory); ligB accessory.

**Module-document actions:**
- Update bucket boundaries: the reusable module should explicitly place **dnaA/dnaC** (initiation) and, if desired, note topology enzymes as a linked-but-separate module.
- Add a **"lineage-specific / expected-absent" annotation** for HolE(theta) so its absence is not scored as an unmet step.
- Add a **paralog-disambiguation note** for the epsilon KO (K02342) and DnaB KO (K02314) so future over-propagation is auto-flagged.

**GO-curation:**
- Existing GO terms suffice for all covered steps (e.g., GO:0006269 DNA replication initiation; GO:0006271 DNA strand elongation; GO:0003887 DNA-directed DNA polymerase; GO:0008408 3'-5' exonuclease; GO:0003689 DNA clamp loader; GO:0003896 DNA primase; GO:0003697 ssDNA binding; GO:0003911 DNA ligase (NAD+)). **No new GO term requests are needed.**
- Recommend GO annotations be **restricted**: e.g., "DNA clamp loader activity" (GO:0003689) should be assigned to the DnaX/HolA/HolB/HolC set, not extended to psi (absent); "3'-5' exonuclease, replisome proofreading" should map to PP_4141 only, with PP_0353/PP_4768 given a generic exonuclease term rather than the Pol III epsilon term.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_3893** — resolve prophage vs. functional accessory replicative helicase; likely remove from module. *(High priority.)*
2. **PP_0353** (likely NEN2/oligoribonuclease-like DEDDh exonuclease, PANTHER SF4) and **PP_4768** (likely ExoX / Exodeoxyribonuclease 10, PANTHER SF37) — DnaQ-superfamily exonuclease paralogs mis-KO'd as Pol III epsilon; assign correct specific names, remove Pol III epsilon KO/GO, and re-annotate as generic 3'→5' exonucleases. *(High priority.)*
3. **holD/psi** — three annotation methods (KEGG KO, UniProt name, positive-control Pfam PF03603/IPR004615) all negative in KT2440 *and* PAO1; only a sensitive profile-HMM/AlphaFold-structural search could distinguish true loss from extreme divergence. *(Medium — expert/structural, not routine fetch-gene.)*
4. **PP_3119 (dnaE2/imuC) + PP_3118 (imuB)** — confirm SOS cassette membership and ensure exclusion from the replicative core step. *(Medium.)*
5. **ligB (PP_4968)** — confirm non-essential paralog status; keep ligA as the module player. *(Low–medium.)*

---

## 8. Key references

- Ogasawara N, Yoshikawa H. *Genes and their organization in the replication origin region of the bacterial chromosome.* Mol Microbiol 1992. **PMID 1552862** — direct sequence evidence that the *P. putida* dnaA/origin region and gene order are conserved (grounds step 1).
- Takami H et al. *Replication origin region of the chromosome of alkaliphilic Bacillus halodurans C-125.* 1999. **PMID 10427704** — notes conserved DnaA-box/origin organization shared with *P. putida* (supports origin-cluster interpretation).
- Fahey J et al. *DinB (Pol IV), ImuBC and RpoS contribute to ciprofloxacin-resistance mutations in Pseudomonas aeruginosa.* 2023. **PMID 37625357** — *Pseudomonas* evidence that imuBC/dnaE2 is an SOS mutagenesis (translesion) system, supporting exclusion of PP_3118/PP_3119 from the replicative core (species transfer from *P. aeruginosa* to *P. putida*: strong at the pathway level).
- Molina-Henares MA et al. *Conditionally essential genes for growth of Pseudomonas putida KT2440 on minimal medium.* 2010. **PMID 20158506** — KT2440 functional-genomics context (essential-gene framework).
- de Siqueira GMV et al. *Differences in GenBank and RefSeq annotations may affect genomics data interpretation for [P. putida].* 2025. **PMID 41036861** — caution that KT2440 annotation source affects gene calls, directly relevant to over-propagation risk.
- Primary database evidence (direct, this review): **KEGG REST** (rest.kegg.jp) organism `ppu` — KO assignments for all 18 bucket genes, K02313→PP_0010 (dnaA), K02315→PP_1552 (dnaC), K02344/K02345 (holD/holE) → no gene; **UniProt** proteome UP000000556 — no holD/holE entries; gyr/par/top loci.
- Positive-control domain evidence (direct, this review): **UniProt/Pfam/InterPro** — HolD/psi signature **PF03603 / IPR004615** retrieves *E. coli* K-12 holD (**P28632**) but returns nothing in *P. putida* KT2440 (UP000000556) or *P. aeruginosa* PAO1 (UP000002438); chi signature PF04364 is present (holC=PP_0979). Epsilon discrimination: CDD cd06131 + InterPro IPR006309 (DnaQ_proteo) + PANTHER PTHR30231:SF41 unique to dnaQ=PP_4141; PP_0353=SF4 (NEN2-like), PP_4768=SF37 (ExoX).

---

### Uncertainty & species-transfer notes
- All KT2440 gene→step assignments are **homology/orthology-based** (KEGG KO + UniProt) plus **synteny**; no strain-specific subunit knockouts were located. Confidence is high for the universally conserved core (alpha, beta, DnaB, SSB, DnaG, DnaX, LigA) and high that PP_0353/PP_4768/PP_3893 are paralogs (based on KO sharing + generic/prophage names).
- HolE(theta) absence is a well-established phylogenetic pattern (enterobacteria-restricted); transfer to KT2440 as an expected negative is **strong**.
- HolD(psi) absence is now supported by **three** independent methods (KEGG KO, UniProt name, and a positive-control-validated Pfam/InterPro domain search) and is a **genus-level** pattern (also undetectable in *P. aeruginosa* PAO1 while robustly found in *E. coli*). This strongly indicates either true loss or extreme divergence; final discrimination requires profile-HMM/AlphaFold-structural analysis. It does not affect satisfiability (psi is a non-essential accessory subunit; core loader intact).
- imuBC/dnaE2 role is transferred from *P. aeruginosa*/general *Pseudomonas* SOS biology — **strong** at the pathway level, not yet demonstrated biochemically in KT2440.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_chromosomal_dna_replication__ppu03030-deep-research-openscientist_artifacts/final_report.pdf)