---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T23:24:23.428103'
end_time: '2026-08-12T23:48:12.976200'
duration_seconds: 1429.55
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial ImuABC damage-induced mutagenesis
  module_summary: A reusable bacterial module for SOS-regulated, error-prone DNA synthesis
    by an ImuA-ImuB-DnaE2 cassette. RecA-dependent DNA-damage signaling and a LexA-family
    repressor provide a common but regulon-specific induction gate. ImuA and catalytically
    inactive ImuB organize access of the DnaE2 polymerase to stalled or damaged replication
    intermediates, where DnaE2 performs damage-tolerant, mutagenic DNA synthesis.
    Canonical nucleotide excision, homologous recombination, and constitutive chromosome
    replication are outside the module boundary.
  module_outline: "- bacterial ImuABC damage-induced mutagenesis\n  - 1. RecA-dependent\
    \ DNA-damage signaling\n  - activated RecA damage signal\n    - RecA nucleoprotein\
    \ damage sensor (molecular player: bacterial RecA family; activity or role: ATP-dependent\
    \ DNA damage sensor activity)\n  - 2. LexA-family repression and damage-induced\
    \ derepression\n  - LexA cassette regulatory gate\n    - cassette-specific LexA\
    \ repressor (molecular player: LexA repressor family; activity or role: DNA-binding\
    \ transcription repressor activity)\n  - 3. ImuA translesion-synthesis accessory\
    \ function\n  - ImuA accessory step\n    - ImuA translesion-synthesis accessory\
    \ protein (molecular player: ImuA family)\n  - 4. ImuB polymerase-recruitment\
    \ scaffold\n  - ImuB recruitment step\n    - ImuB translesion-synthesis accessory\
    \ protein (molecular player: ImuB/IMS family)\n  - 5. DnaE2-dependent mutagenic\
    \ DNA synthesis\n  - DnaE2 error-prone DNA synthesis\n    - DnaE2 error-prone\
    \ DNA polymerase (molecular player: DnaE2 family; activity or role: DNA-directed\
    \ DNA polymerase activity)"
  module_connections: '- activated RecA damage signal promotes LexA cassette regulatory
    gate: Activated RecA promotes LexA-family autocleavage and cassette derepression.

    - LexA cassette regulatory gate inhibits ImuA accessory step: Intact cassette-associated
    LexA represses transcription of the ImuABC effector genes.

    - ImuA accessory step feeds into ImuB recruitment step: ImuA contributes the first
    noncatalytic accessory function of the cassette.

    - ImuB recruitment step feeds into DnaE2 error-prone DNA synthesis: ImuB recruits
    or organizes DnaE2 at the damaged replication intermediate.'
  pathway_query: error-prone translesion synthesis
  pathway_id: error-prone translesion synthesis
  pathway_name: error-prone translesion synthesis
  pathway_source: free-text pathway query
  pathway_context: No local pathway bucket was resolved for this query.
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '0'
  candidate_genes: No local candidate gene table was available or no genes matched
    this pathway/bucket.
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_imuabc_damage_induced_mutagenesis__error-prone-translesion-synthesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_imuabc_damage_induced_mutagenesis__error-prone-translesion-synthesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial ImuABC damage-induced mutagenesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: error-prone translesion synthesis
- Resolved ID: error-prone translesion synthesis
- Resolved name: error-prone translesion synthesis
- Source: free-text pathway query

No local pathway bucket was resolved for this query.

## Candidate Genes From Local Metadata

Candidate gene count: 0

No local candidate gene table was available or no genes matched this pathway/bucket.

## Generic Module Context

### Working Scope

A reusable bacterial module for SOS-regulated, error-prone DNA synthesis by an ImuA-ImuB-DnaE2 cassette. RecA-dependent DNA-damage signaling and a LexA-family repressor provide a common but regulon-specific induction gate. ImuA and catalytically inactive ImuB organize access of the DnaE2 polymerase to stalled or damaged replication intermediates, where DnaE2 performs damage-tolerant, mutagenic DNA synthesis. Canonical nucleotide excision, homologous recombination, and constitutive chromosome replication are outside the module boundary.

### Provisional Biological Outline

- bacterial ImuABC damage-induced mutagenesis
  - 1. RecA-dependent DNA-damage signaling
  - activated RecA damage signal
    - RecA nucleoprotein damage sensor (molecular player: bacterial RecA family; activity or role: ATP-dependent DNA damage sensor activity)
  - 2. LexA-family repression and damage-induced derepression
  - LexA cassette regulatory gate
    - cassette-specific LexA repressor (molecular player: LexA repressor family; activity or role: DNA-binding transcription repressor activity)
  - 3. ImuA translesion-synthesis accessory function
  - ImuA accessory step
    - ImuA translesion-synthesis accessory protein (molecular player: ImuA family)
  - 4. ImuB polymerase-recruitment scaffold
  - ImuB recruitment step
    - ImuB translesion-synthesis accessory protein (molecular player: ImuB/IMS family)
  - 5. DnaE2-dependent mutagenic DNA synthesis
  - DnaE2 error-prone DNA synthesis
    - DnaE2 error-prone DNA polymerase (molecular player: DnaE2 family; activity or role: DNA-directed DNA polymerase activity)

### Known Relationships Among Steps

- activated RecA damage signal promotes LexA cassette regulatory gate: Activated RecA promotes LexA-family autocleavage and cassette derepression.
- LexA cassette regulatory gate inhibits ImuA accessory step: Intact cassette-associated LexA represses transcription of the ImuABC effector genes.
- ImuA accessory step feeds into ImuB recruitment step: ImuA contributes the first noncatalytic accessory function of the cassette.
- ImuB recruitment step feeds into DnaE2 error-prone DNA synthesis: ImuB recruits or organizes DnaE2 at the damaged replication intermediate.

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

# Module/Pathway Review: Bacterial ImuABC Damage-Induced Mutagenesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway/bucket query:** error-prone translesion synthesis
**Generic module:** SOS-regulated, error-prone DNA synthesis by an ImuA–ImuB–DnaE2 cassette
**Local candidate genes supplied:** 0 (empty metadata table — resolved de novo from UniProt/KEGG + literature)

---

## Summary

The ImuABC/DnaE2 damage-induced mutagenesis module is **fully present and satisfiable** in *Pseudomonas putida* KT2440, despite the empty local candidate-gene table. All five expected module steps map to identifiable genes, and the effector portion of the module is organized as a single contiguous SOS operon. The cassette comprises **PP_3116 (lexA2)**, **PP_3117 (imuA)**, **PP_3118 (imuB)**, and **PP_3119 (dnaE2/imuC)**, with the shared upstream damage sensor **RecA (PP_1629)** completing the RecA-dependent signaling step. This assignment is anchored by direct target-organism evidence: a genome-wide microarray study in KT2440 established that one of the strain's two LexA paralogs, **LexA2**, regulates only its own transcriptional unit, which contains *imuA*, *imuB*, and *dnaE2* ([PMID: 17933893](https://pubmed.ncbi.nlm.nih.gov/17933893/)).

The most curation-relevant conclusion is that this module must be **specialized to the correct paralogs** in KT2440. The strain carries two LexA repressors: LexA1 (PP_2143) runs the conventional *E. coli*-like SOS regulon, while LexA2 (PP_3116) is a dedicated gate for the *imu* cassette. The module's "LexA-family repression" step should therefore be pinned to **LexA2, not the housekeeping LexA1**. Similarly, the DnaE2 step must be kept distinct from the essential replicative Pol III α-subunit **DnaE1 (PP_1606)**; both share EC 2.7.7.7 but only DnaE2 is the mutagenic translesion enzyme. Functional support for the DnaE2/ImuC step is direct in pseudomonads: alkylation-damage-induced mutagenesis in *P. putida* and *P. aeruginosa* is "largely ImuC-dependent" ([PMID: 28118378](https://pubmed.ncbi.nlm.nih.gov/28118378/)).

The two accessory steps — **ImuA (PP_3117)** and **ImuB (PP_3118)** — are covered by operon context and LexA2 co-regulation in the target strain, but their mechanistic roles are transferred by homology from *Caulobacter crescentus* and *Myxococcus xanthus* models; they have not been individually knocked out for mutagenesis in KT2440. These two steps should be marked **covered but candidate_uncertain**. One explicit over-annotation risk requires a curator note: ImuB carries a Y-family (UmuC/IMS) polymerase domain but is expected to be **catalytically dead**, functioning as a scaffold rather than an active polymerase. The cassette is **single-copy**, and KT2440 lacks a chromosomal Pol V (no *umuDC*/*rulAB*/*samB*), making DnaE2 the strain's principal SOS-dependent mutagenic polymerase.

---

## Target-Organism Pathway Definition

### What the module includes

The module covers **SOS-regulated, error-prone (mutagenic) DNA synthesis** carried out by the ImuA–ImuB–DnaE2 cassette when replication stalls at a damaged template. Concretely, in KT2440 the process is:

1. DNA damage generates ssDNA; **RecA (PP_1629)** forms an activated nucleoprotein filament that acts as the damage sensor and co-protease.
2. Activated RecA promotes autocleavage of the cassette-specific repressor **LexA2 (PP_3116)**, derepressing the operon.
3. **ImuA (PP_3117)** provides a non-catalytic accessory function, in part by modulating RecA-mediated template switching to favor translesion synthesis over recombinational bypass.
4. **ImuB (PP_3118)** acts as a (catalytically inactive) scaffold that recruits and organizes the polymerase at the damaged replication intermediate.
5. **DnaE2/ImuC (PP_3119)** performs damage-tolerant, low-fidelity DNA synthesis across the lesion, producing mutations.

### Neighboring pathways to keep separate

To avoid module bleed, the following processes — all active in KT2440 — must be kept **outside** this module boundary:

| Neighboring process | KT2440 genes | Why separate |
|---|---|---|
| Canonical *E. coli*-like SOS regulon | LexA1 (PP_2143) | Different repressor paralog/SOS box; governs recombination/repair genes, not the *imu* cassette ([PMID: 17933893](https://pubmed.ncbi.nlm.nih.gov/17933893/)) |
| Pol IV / DinB mutagenesis | *dinB* (PP_1203) | Distinct Y-family polymerase; largely **RecA-independent**, starvation/stationary-phase associated ([PMID: 15090515](https://pubmed.ncbi.nlm.nih.gov/15090515/)) |
| Replicative chromosome synthesis | DnaE1 (PP_1606) | Essential Pol III α-subunit; shares EC 2.7.7.7 but is high-fidelity, not damage-induced |
| Nucleotide excision repair | uvrA/uvrA2/uvrB/uvrC | Error-free excision; separate from mutagenic bypass ([PMID: 17720631](https://pubmed.ncbi.nlm.nih.gov/17720631/)) |
| NHEJ / stationary-phase mutagenesis | *ligD*, *ku* | Independent mutagenic pathways ([PMID: 25942369](https://pubmed.ncbi.nlm.nih.gov/25942369/)) |
| GO/oxidative-damage avoidance | *mutY*, *mutM*, *mutT*, *dps* | Prevent mutations rather than generate them ([PMID: 17545288](https://pubmed.ncbi.nlm.nih.gov/17545288/)) |

### Alternate names and database definitions

- **imuC = dnaE2** — the *P. putida*/*P. aeruginosa* literature increasingly uses **ImuC** for the DnaE2 polymerase ([PMID: 28118378](https://pubmed.ncbi.nlm.nih.gov/28118378/)). UniProt for KT2440 uses "Error-prone DNA polymerase" (DNAE2_PSEPK, Q88I82).
- The cassette is variably called **imuAB-dnaE2**, the **imuABC operon**, or the **DnaE2 mutagenesis cassette** across taxa.
- "Error-prone translesion synthesis" (the free-text query) is the umbrella functional description; note it can also encompass DinB/Pol IV and Pol V bypass in other organisms, so the module must be scoped specifically to the ImuAB-DnaE2 machinery.

---

## Expected Step Model and Satisfiability

```
  DNA damage / stalled fork
          │
          ▼
 ┌───────────────────────┐
 │ 1. RecA damage signal │   RecA  = PP_1629  (shared sensor)      [COVERED]
 └───────────┬───────────┘
             │ promotes LexA autocleavage
             ▼
 ┌───────────────────────┐
 │ 2. LexA gate          │   LexA2 = PP_3116  (cassette-specific)  [COVERED — specialize to LexA2]
 └───────────┬───────────┘
             │ derepression
             ▼
 ┌───────────────────────┐
 │ 3. ImuA accessory     │   ImuA  = PP_3117                       [COVERED / candidate_uncertain]
 └───────────┬───────────┘
             │
             ▼
 ┌───────────────────────┐
 │ 4. ImuB scaffold      │   ImuB  = PP_3118  (Y-fam domain, dead) [COVERED / candidate_uncertain + over-annotation flag]
 └───────────┬───────────┘
             │ recruits polymerase
             ▼
 ┌───────────────────────┐
 │ 5. DnaE2 synthesis    │   DnaE2 = PP_3119  (=ImuC)              [COVERED — direct functional evidence]
 └───────────────────────┘
       operon: PP_3116 — PP_3117 — PP_3118 — PP_3119 (LexA2-controlled)
```

| Step | Expected player | KT2440 gene | Status | Evidence type |
|---|---|---|---|---|
| 1. RecA damage signal | RecA family | PP_1629 | **covered** | Homology + universal SOS role |
| 2. LexA gate | LexA repressor | **PP_3116 (LexA2)** | **covered** | Direct KT2440 microarray ([PMID: 17933893](https://pubmed.ncbi.nlm.nih.gov/17933893/)) |
| 3. ImuA accessory | ImuA family | PP_3117 | **covered / candidate_uncertain** | Operon + regulon context; function by homology |
| 4. ImuB scaffold | ImuB/IMS family | PP_3118 | **covered / candidate_uncertain** | Operon + domain; catalytic-dead by homology |
| 5. DnaE2 synthesis | DnaE2 family | PP_3119 (ImuC) | **covered** | Direct functional evidence in *P. putida* ([PMID: 28118378](https://pubmed.ncbi.nlm.nih.gov/28118378/)) |

**No step is a gap, and no step is "not expected in the target taxon."** The module is satisfiable.

---

## Key Findings — Candidate Genes and Evidence

### F001 — The cassette is a contiguous LexA2-controlled operon (PP_3116–PP_3119)

UniProt/KEGG for proteome UP000000556 resolve a contiguous four-gene cluster: **PP_3116** = LexA repressor 2 (LEXA2_PSEPK, P59479); **PP_3117** = ImuA (Q88I84, "Translesion DNA synthesis-associated protein ImuA", 206 aa); **PP_3118** = *imuB* (Q88I83, 472 aa, Y-family-like); **PP_3119** = *dnaE2* (DNAE2_PSEPK, Q88I82, "Error-prone DNA polymerase", EC 2.7.7.7, 1033 aa). Genome-wide microarray analysis in KT2440 showed that *"the other LexA protein (LexA2) regulates only its own transcriptional unit, which includes the imuA, imuB, and dnaE2 genes"* ([PMID: 17933893](https://pubmed.ncbi.nlm.nih.gov/17933893/)). This is **direct target-strain evidence** for both cassette composition and its repressor, and it satisfies the operon/co-regulation premise of the generic module.

### F002 — DnaE2/ImuC (PP_3119) is the principal SOS-dependent mutagenic polymerase

Functional work in *P. aeruginosa* and *P. putida* demonstrated that the TLS polymerase **ImuC (former DnaE2)** confers alkylation-damage tolerance, and that *"mutagenesis induced by MMS in pseudomonads was largely ImuC-dependent"* ([PMID: 28118378](https://pubmed.ncbi.nlm.nih.gov/28118378/)). This is direct functional evidence in the target species for the DnaE2 synthesis step. It contrasts with **DinB/Pol IV (PP_1203)**, which drives a distinct, largely **RecA-independent**, starvation-associated mutagenic pathway (*"mechanisms different from the classical RecA-dependent SOS response could elevate Pol IV-dependent mutagenesis in starving P. putida cells"*, [PMID: 15090515](https://pubmed.ncbi.nlm.nih.gov/15090515/)). Curators should therefore not conflate DinB-dependent mutagenesis with the ImuABC module.

### F003 — Two-LexA architecture: LexA1 (PP_2143) canonical SOS vs LexA2 (PP_3116) *imu* gate

KT2440 encodes two LexA paralogs recognizing distinct SOS-box motifs. The microarray study found that *"one of the two LexA proteins (LexA1) seems to be in control of the conventional Escherichia coli-like SOS response"* ([PMID: 17933893](https://pubmed.ncbi.nlm.nih.gov/17933893/)), whereas LexA2 governs only the *imuA-imuB-dnaE2* unit (plus a prophage gene, PP_3901). **RecA (PP_1629)** is the shared sensor triggering autocleavage of both repressors. For the module, the LexA step must be assigned to **LexA2 (PP_3116)**; assigning it to LexA1 would be biologically incorrect for this cassette in this strain.

### F004 — ImuA (PP_3117) and ImuB (PP_3118) roles inferred by homology

The founding functional study in *Caulobacter crescentus* showed the *imuA-imuB-dnaE2* operon is *recA*-dependent and damage-inducible, and that *"the three genes are required for the error-prone processing of DNA lesions"* ([PMID: 15886391](https://pubmed.ncbi.nlm.nih.gov/15886391/)). In *Myxococcus xanthus*, *"DnaE2 is an error-prone TLS polymerase, and its functions require ImuA and ImuB"*, with ImuA inhibiting RecA-mediated activity to favor TLS ([PMID: 34190612](https://pubmed.ncbi.nlm.nih.gov/34190612/)). In KT2440, PP_3117 and PP_3118 are supported by operon context and LexA2 co-regulation but have **not** been individually knocked out for mutagenesis; their accessory/scaffold roles are transferred from these related organisms. Transfer is **moderately strong** (conserved operon architecture, conserved regulon) but not experimentally confirmed in the target strain — hence **candidate_uncertain**.

### F005 — Domain signatures resolve paralog ambiguity and flag ImuB over-annotation

InterPro/Pfam signatures cleanly separate the players:

| Gene | Protein | Key domain signatures | Curation note |
|---|---|---|---|
| PP_3117 | ImuA | ImuA_translesion (IPR047610) + SulA/P-loop NTPase fold | RecA-inhibitory fold consistent with Myxococcus ImuA role |
| PP_3118 | ImuB | UmuC / Y-family polymerase (PF00817 IMS, IPR001126) | **Expected catalytically dead** — do NOT annotate active DNA-pol activity |
| PP_3119 | DnaE2 | DnaE2-specific (IPR023073) | Distinct from replicative DnaE1 |
| PP_1606 | DnaE1 | PolIIIA_DnaE1_PHP (IPR049821) | Essential replicative Pol III α — outside module |

Both DnaE2 and DnaE1 share **EC 2.7.7.7**, so EC number alone cannot distinguish them — the DnaE2-specific InterPro signature (IPR023073) is required.

### F006 — Single-copy cassette; no chromosomal Pol V

A proteome-wide InterPro scan of taxon 160488 found: ImuA-family IPR047610 in only PP_3117; DnaE2-specific IPR023073 in only PP_3119 (replicative DnaE1/PP_1606 correctly excluded); and the IMS/UmuC domain PF00817 in only two proteins — ImuB (PP_3118) and DinB/Pol IV (PP_1203). Crucially, **no *umuC*/*umuD*/*rulA*/*rulB*/*samB* (Pol V) genes are present** on the chromosome. (The *mucA*/*mucB* hits correspond to the AlgU anti-sigma-factor system PP_1428/PP_1429, not MucAB Pol V.) The module cassette is therefore single-copy, and DnaE2 is the sole SOS-dependent mutagenic polymerase in KT2440 — reinforcing its functional importance. Note that plasmid-borne *rulAB* can be introduced experimentally and does bypass oxidized adenine ([PMID: 17545288](https://pubmed.ncbi.nlm.nih.gov/17545288/)), but this is not part of the native KT2440 chromosome.

---

## Mechanistic Model / Interpretation

The module in KT2440 is a clean, self-contained regulatory-effector circuit that can be read directly from genome order:

```
   PP_3116        PP_3117     PP_3118     PP_3119
   ┌──────┐       ┌─────┐     ┌─────┐     ┌──────┐
   │ lexA2│──┐    │ imuA│─────│ imuB│─────│ dnaE2│   ← one LexA2-repressed operon
   └──────┘  │    └─────┘     └─────┘     └──────┘
             │ represses (SOS box)          ▲
             │                              │ mutagenic bypass synthesis
   RecA (PP_1629) ──[damage]──► autocleaves LexA2 ──► derepression ──► ImuA + ImuB organize DnaE2 at lesion
```

The circuit's logic: RecA senses ssDNA at a stalled fork and triggers LexA2 self-cleavage; derepression co-expresses the ImuA accessory factor, the ImuB scaffold, and the DnaE2 polymerase in stoichiometric proximity. ImuA biases the outcome away from RecA-mediated recombinational template switching and toward translesion synthesis; ImuB (a catalytically dead Y-family relative) recruits and positions DnaE2 at the primer terminus; DnaE2 then extends across the lesion with low fidelity, generating point mutations. The output is damage-induced, RecA/LexA-gated mutagenesis — mechanistically and regulatorily distinct from KT2440's RecA-independent DinB/Pol IV starvation mutagenesis and from its error-free NER and NHEJ pathways.

Two paralog collisions dominate the curation risk profile and are summarized below:

| Collision | Module (correct) | Confounder (wrong) | Discriminator |
|---|---|---|---|
| LexA repressor | LexA2 (PP_3116) | LexA1 (PP_2143) | Regulon target (own operon vs canonical SOS) |
| DnaE polymerase | DnaE2 (PP_3119) | DnaE1 (PP_1606) | IPR023073 vs IPR049821; both EC 2.7.7.7 |
| Y-family domain | ImuB scaffold (PP_3118) | DinB/Pol IV (PP_1203) | Operon context + catalytic-site degeneracy |

---

## Gaps, Ambiguities, and Likely Over-Annotations

- **ImuB polymerase activity (over-annotation risk).** ImuB (PP_3118) carries a UmuC/Y-family polymerase domain and may be automatically annotated with DNA-directed DNA polymerase activity (GO:0003887 / EC 2.7.7.7). Across characterized ImuB proteins, the catalytic aspartates are degenerate and ImuB acts as a **scaffold**, not an active polymerase. Curators should annotate ImuB with a scaffolding/accessory role and explicitly withhold or qualify polymerase-activity terms.
- **LexA paralog ambiguity.** Automated pipelines may map the module's LexA step to either LexA1 (PP_2143) or LexA2 (PP_3116). Only **LexA2** is correct for this cassette; this is a strain-specific specialization not captured by generic bacterial modules.
- **DnaE1/DnaE2 EC collision.** EC 2.7.7.7 is shared with the essential replicative DnaE1 (PP_1606). EC-based mapping alone would erroneously include DnaE1; the module must rely on the DnaE2-specific signature.
- **ImuA/ImuB functional transfer.** No direct KT2440 knockout data exist for PP_3117 or PP_3118 mutagenesis phenotypes; roles are homology-inferred (candidate_uncertain).
- **DinB cross-talk.** In *P. aeruginosa*, both *dinB* and *imuBC* contribute to ciprofloxacin-resistance mutations ([PMID: 37625357](https://pubmed.ncbi.nlm.nih.gov/37625357/)); the two systems can act in parallel, so mutagenesis phenotypes are not uniquely diagnostic of the ImuABC module.
- **Regulatory layering.** The *imu* regulon in *Pseudomonas* also intersects with RpoS/PsrA physiology ([PMID: 30684026](https://pubmed.ncbi.nlm.nih.gov/30684026/), [PMID: 11371535](https://pubmed.ncbi.nlm.nih.gov/11371535/)); these are context modifiers, not core module steps.

---

## Module and GO-Curation Recommendations

| Module step | Recommended status | Assigned gene | Rationale |
|---|---|---|---|
| RecA damage signal | **covered** | PP_1629 | Universal SOS sensor; strong transfer |
| LexA gate | **covered (specialize)** | PP_3116 (LexA2) | Direct KT2440 evidence; must not use LexA1 |
| ImuA accessory | **covered / candidate_uncertain** | PP_3117 | Operon+regulon; function by homology |
| ImuB scaffold | **covered / candidate_uncertain** | PP_3118 | Operon+domain; flag over-annotation |
| DnaE2 synthesis | **covered** | PP_3119 (ImuC) | Direct functional evidence in *P. putida* |

**Overall module verdict: SATISFIABLE / covered.** No step is a gap or `not_expected_in_target_taxon`.

Additional recommendations:
- **Module boundary correction for this organism:** the generic module's single "LexA-family repressor" node should be documented as **LexA2-specific** in *Pseudomonas putida*, with a note that LexA1 runs a parallel canonical SOS regulon. This is a `module_needs_revision`-style annotation at the documentation level (paralog specialization), not a structural failure.
- **GO annotation guidance:** annotate PP_3118 (ImuB) with an accessory/scaffold function (e.g., DNA damage response / SOS mutagenesis) and **avoid** propagating DNA polymerase catalytic activity. Annotate PP_3119 with translesion synthesis / error-prone DNA polymerase activity (GO:0003887 with an SOS/translesion qualifier), distinguished from the housekeeping replicative activity of PP_1606.
- **No new GO term request is strictly required**, but a curator-facing note distinguishing DnaE2 (mutagenic) from DnaE1 (replicative) under EC 2.7.7.7 would prevent recurrent mis-mapping.

---

## Genes to Promote to Full `fetch-gene` Review

1. **PP_3116 (LexA2)** — high priority. Confirm SOS-box binding specificity and its exclusive control of the *imu* cassette; anchor the paralog specialization.
2. **PP_3118 (imuB)** — high priority. Verify catalytic-dead status and scaffold role; primary over-annotation risk in the module.
3. **PP_3119 (dnaE2/imuC)** — medium priority. Confirm DnaE2-specific signature and functional annotation; the direct functional evidence already exists but the EC collision with DnaE1 warrants an explicit review note.
4. **PP_3117 (imuA)** — medium priority. Confirm ImuA_translesion + SulA/NTPase fold and candidate_uncertain functional status.
5. **PP_1629 (recA)** — low priority. Standard confirmation of the shared sensor.

---

## Evidence Base

| PMID | Organism / scope | How it supports or challenges the review |
|---|---|---|
| [17933893](https://pubmed.ncbi.nlm.nih.gov/17933893/) | **Direct KT2440** | LexA2 regulates the *imuA-imuB-dnaE2* unit; LexA1 runs canonical SOS. Anchors cassette composition, repressor identity, and paralog specialization. |
| [28118378](https://pubmed.ncbi.nlm.nih.gov/28118378/) | **Direct *P. putida*/*P. aeruginosa*** | MMS-induced mutagenesis is largely ImuC(DnaE2)-dependent — direct functional support for the DnaE2 step. |
| [15886391](https://pubmed.ncbi.nlm.nih.gov/15886391/) | *C. crescentus* | Founding study: all three *imuA-imuB-dnaE2* genes required for error-prone lesion processing — basis for ImuA/ImuB role transfer. |
| [34190612](https://pubmed.ncbi.nlm.nih.gov/34190612/) | *M. xanthus* | DnaE2 requires ImuA and ImuB; ImuA inhibits RecA-mediated activity to favor TLS — supports accessory/non-catalytic roles. |
| [15090515](https://pubmed.ncbi.nlm.nih.gov/15090515/) | *P. putida* | Pol IV/DinB mutagenesis is RecA-independent — distinguishes DinB from the ImuABC module. |
| [37625357](https://pubmed.ncbi.nlm.nih.gov/37625357/) | *P. aeruginosa* | DinB and ImuBC both contribute to ciprofloxacin-resistance mutations — flags parallel-pathway cross-talk. |
| [17545288](https://pubmed.ncbi.nlm.nih.gov/17545288/) | *P. putida* | Plasmid *rulAB* (Pol V homolog) bypasses oxidized adenine — clarifies that native chromosome lacks Pol V. |
| [17720631](https://pubmed.ncbi.nlm.nih.gov/17720631/) | *P. putida* | NER dual role in mutagenesis — neighboring pathway to keep separate. |
| [25942369](https://pubmed.ncbi.nlm.nih.gov/25942369/) | *P. putida* | NHEJ (LigD/Ku) stationary-phase mutagenesis — separate module. |
| [30684026](https://pubmed.ncbi.nlm.nih.gov/30684026/) / [11371535](https://pubmed.ncbi.nlm.nih.gov/11371535/) | *Pseudomonas* | RpoS/PsrA regulatory layering on *lexA* — context modifier, not a core step. |

---

## Limitations and Knowledge Gaps

- **No KT2440-specific knockouts** of *imuA* (PP_3117) or *imuB* (PP_3118) for mutagenesis; their roles rest on operon context plus *Caulobacter*/*Myxococcus* homology.
- **DnaE2/ImuC functional data** in pseudomonads derive substantially from *P. aeruginosa* and aggregate "pseudomonad" experiments; while *P. putida* is included, strain-KT2440-resolved lesion-bypass biochemistry is limited.
- **Regulatory detail** of LexA2 autocleavage kinetics and RecA co-protease specificity in KT2440 is inferred, not measured.
- **Analysis is annotation-/literature-based** (UniProt, KEGG, InterPro, PubMed); no primary sequence realignment or structural modeling was performed to independently confirm ImuB catalytic-site degeneracy.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted knockouts in KT2440:** Δ*imuA*, Δ*imuB*, Δ*dnaE2* single mutants; assay MMS/UV-induced and ciprofloxacin-resistance mutation frequencies to confirm each step's requirement directly in the target strain.
2. **ImuB catalytic-site mutagenesis:** align PP_3118 against active UmuC/DinB polymerases to verify degenerate catalytic aspartates; test a catalytic-restoration or catalytic-dead point mutant to confirm the scaffold model.
3. **LexA2 SOS-box footprinting:** EMSA/ChIP to confirm LexA2 binds the *imu* operon promoter and to delimit the LexA2 regulon versus LexA1 in KT2440.
4. **Epistasis with DinB:** Δ*dinB* Δ*dnaE2* double mutants to partition SOS-dependent (ImuABC) from RecA-independent (Pol IV) mutagenesis.
5. **Curation action:** update the module document to specialize the LexA node to LexA2, add the ImuB over-annotation caveat, and add the DnaE1/DnaE2 EC-2.7.7.7 disambiguation note.

---

*Report generated from a 3-iteration autonomous curation review. Evidence tiers: direct KT2440 (LexA2 regulon, cassette composition); direct pseudomonad (DnaE2/ImuC mutagenesis); homology-transferred (ImuA/ImuB mechanistic roles from Caulobacter/Myxococcus).*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_imuabc_damage_induced_mutagenesis__error-prone-translesion-synthesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_imuabc_damage_induced_mutagenesis__error-prone-translesion-synthesis-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17933893
2. PMID:28118378
3. PMID:15090515
4. PMID:17720631
5. PMID:25942369
6. PMID:17545288
7. PMID:15886391
8. PMID:34190612
9. PMID:37625357
10. PMID:30684026
11. PMID:11371535