---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T14:25:46.006744'
end_time: '2026-08-08T15:52:16.762298'
duration_seconds: 5190.76
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: ruvabc_holliday_junction_processing
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__ruvabc-holliday-junction-processing__ppu03440-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__ruvabc-holliday-junction-processing__ppu03440-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

ruvabc_holliday_junction_processing in Pseudomonas putida KT2440

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

# Module Review: RuvABC Holliday-Junction Processing in *Pseudomonas putida* KT2440

**Review topic:** `ruvabc_holliday_junction_processing`
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Anchor pathway:** KEGG ppu03440 — Homologous recombination
**Module area:** other_kegg_pathway (no module YAML resolved)

---

## 1. Executive Summary

The RuvABC Holliday-junction (HJ) processing module is **complete, syntenically organized, and predicted catalytically competent** in *Pseudomonas putida* KT2440. The three core genes — **ruvA (PP_1216 / Q88NJ1)**, **ruvB (PP_1217 / Q88NJ0)** and **ruvC (PP_1215 / Q88NJ2)** — are encoded in a conserved *ruvCAB* arrangement, with *ruvA* and *ruvB* adjacent and *ruvC* directly upstream. RuvC, the resolvase, retains its full RNase-H-fold catalytic active site (annotated acidic residues at positions 8/67/139 and the diagnostic G-I-D-P-G motif), and a global alignment shows **63.4% amino-acid identity to *Escherichia coli* RuvC**, comfortably above the ~30% threshold used for confident ortholog functional transfer. The alternative branch-migration helicase **RecG (PP_5310 / Q88C73)** is also present and intact, providing RuvAB-independent branch migration. On this basis, all core module steps — junction recognition/branch-migration loading (RuvA), ATP-driven branch migration (RuvB, with RecG redundancy), and junction resolution (RuvC) — should be marked **COVERED at homology grade**.

Two caveats are important for curation. First, **all evidence is homology-based**: every core protein carries UniProt PE=3 ("inferred from homology"), and there are no direct KT2440 biochemical or genetic experiments on RuvABC function. Second, the target strain is unusually **DNA-damage-sensitive and recombination-inefficient**: Akkaya et al. (2021) show KT2440 mounts a weak SOS response because of an inefficient RecA–LexA interplay, so the *pathway is present but operates at low efficiency* — a phenotype driven by regulation, not by missing HJ-processing genes.

Finally, the supplied candidate list of 24 genes is **over-broad for this module**. Only ruvA, ruvB, ruvC and (as a related-but-distinct step) recG are true HJ-processing genes. DNA polymerase III subunits (dnaN, holC, dnaEA, holB, dnaQ, dnaX, holA), PolA, SSB and the generic "Exonuclease" ORFs belong to replication (ppu03030) and should be excluded from the module scope. The presynaptic recombination genes (recA, recBCD, recFOR, recJ, priA) are legitimate *homologous-recombination* genes but sit **upstream** of HJ processing and belong to sibling module steps, not to `ruvabc_holliday_junction_processing`. We also flag **PP_0151** ("Holliday junction resolvase") as a **spurious machine-generated annotation** that should not be counted as a second resolvase.

---

## 2. Target-Organism Pathway Definition

### 2.1 What the module includes

`ruvabc_holliday_junction_processing` covers the **late steps of homologous recombination and recombinational DNA repair** at which a four-way Holliday junction — formed after RecA-mediated strand invasion — is (i) recognized, (ii) branch-migrated to extend heteroduplex DNA, and (iii) resolved into two duplex products by a structure-specific endonuclease. The canonical division of labor, established in *E. coli*, is: **RuvA** recognizes and binds the junction and loads the motor; **RuvB**, a hexameric ATP-driven DNA helicase/pump, drives branch migration; and **RuvC**, an RNase-H-superfamily dimeric endonuclease, resolves the junction by symmetric strand nicking ([PMID: 9501105](https://pubmed.ncbi.nlm.nih.gov/9501105/)).

### 2.2 Neighboring pathways to keep separate

For curation, the module boundary should **exclude**:

- **DNA replication (KEGG ppu03030 / replisome):** DNA polymerase III holoenzyme subunits (β-clamp *dnaN*, χ *holC*, α *dnaEA*, δ' *holB*, ε *dnaQ*, γ/τ *dnaX*, δ *holA*), Pol I (*polA*), SSB (*ssb*), and generic exonucleases. These are replication-associated and were swept in only because they share the broad "homologous recombination" KEGG map.
- **Presynaptic homologous recombination (upstream of HJ processing):** RecA (strand exchange), RecBCD and RecFOR (end resection / RecA loading), RecJ (5'→3' ssDNA exonuclease), PriA (replication restart). These are *bona fide* HR genes but belong to earlier module steps, not to HJ processing itself.
- **Mismatch repair (ppu03430) and base/nucleotide excision repair (ppu03410/ppu03420):** overlap in some shared nucleases but distinct processes.

### 2.3 Alternate names / database definitions

- KEGG groups all of these under **ppu03440 "Homologous recombination,"** which is broader than the RuvABC module.
- RuvABC is also described as the **"RuvABC resolvasome"** or **"RuvAB branch-migration complex + RuvC resolvase."**
- RecG is annotated as **"ATP-dependent DNA helicase RecG"** and is sometimes grouped with RuvAB as a parallel branch-migration activity; it is **not** a resolvase.

---

## 3. Expected Step Model

| Step | Function | Expected gene(s) | KT2440 candidate | Status |
|------|----------|------------------|------------------|--------|
| 1. HJ recognition / motor loading | Binds four-way junction, loads RuvB | *ruvA* | PP_1216 (Q88NJ1) | **Covered** |
| 2. Branch migration (motor) | ATP-driven hexameric helicase extends heteroduplex | *ruvB* | PP_1217 (Q88NJ0) | **Covered** |
| 3. Junction resolution | Structure-specific endonuclease nicks junction | *ruvC* | PP_1215 (Q88NJ2) | **Covered** |
| 2'. Alternative branch migration | RuvAB-independent HJ/fork branch migration | *recG* | PP_5310 (Q88C73) | **Covered (parallel/redundant)** |
| 3'. Alternative resolvase (RusA-type) | Cryptic/prophage HJ resolvase | *rusA* | — none | **Not expected / absent** |

**Interpretation:** The three obligatory steps (1–3) are each covered by a single high-confidence candidate. Step 2 has genuine redundancy via RecG. Step 3 (resolution) depends on **RuvC alone** — there is no second, RusA-type resolvase in the KT2440 candidate set, consistent with RusA being a cryptic prophage function in *E. coli* rather than a conserved core gene.

---

## 4. Candidate Genes and Evidence

### 4.1 Core module genes (promote / keep in module)

**ruvA — PP_1216 (Q88NJ1), 205 aa, PE=3.** Holliday-junction branch-migration complex subunit RuvA. Encoded immediately adjacent to *ruvB*. Role: junction recognition and RuvB loading. Evidence type: homology/synteny. Caveat: no direct KT2440 assay; PE=3.

**ruvB — PP_1217 (Q88NJ0), 348 aa, PE=3.** Branch-migration motor. Walker A and Walker B ATP-binding motifs are annotated, consistent with the AAA+/helicase mechanism required for the DNA pump activity. Evidence type: homology + conserved ATPase motifs. Caveat: *E. coli* work (RuvBL268S, [PMID: 9973614](https://pubmed.ncbi.nlm.nih.gov/9973614/)) shows RuvB can be fully active in vitro yet still fail in vivo, i.e., in-vitro-competent motifs do not guarantee full cellular function — a reason to keep confidence at homology grade.

**ruvC — PP_1215 (Q88NJ2), 174 aa, PE=3.** Crossover-junction endodeoxyribonuclease (EC 3.1.21.10), the resolvase. Directly upstream of *ruvA/ruvB* in a *ruvCAB* cluster. Retains all three annotated catalytic active-site residues (positions 8, 67, 139) matching the *E. coli* RuvC RNase-H catalytic tetrad (D7/E66/D138/D141); the N-terminal motif M-T-L-I-L-G-**I-D-P-G** contains the catalytic Asp8. Global Needleman–Wunsch alignment vs. *E. coli* RuvC (P0A814) gives **63.4% identity** (104/164 aligned columns), near-identical length. Evidence type: homology + active-site conservation + high global identity. This is the strongest single line of transfer evidence in the module.

**recG — PP_5310 (Q88C73), 692 aa, PE=3.** ATP-dependent DNA helicase RecG (EC 5.6.2.4). Both Helicase ATP-binding and Helicase C-terminal domains are intact. Provides RuvAB-independent branch migration and can convert stalled replication forks into Holliday junctions ([PMID: 18375550](https://pubmed.ncbi.nlm.nih.gov/18375550/)). Note that RecG activity at reversed/stalled forks is itself regulated (e.g., limited by DisA in *Bacillus subtilis*, [PMID: 34073022](https://pubmed.ncbi.nlm.nih.gov/34073022/)). Curation status: keep as **parallel branch-migration** step, not as a resolvase.

### 4.2 Upstream HR genes (legitimate, but NOT part of this module)

These are correctly annotated homologous-recombination genes that generate the substrates RuvABC acts on; assign them to their own (presynaptic) module steps rather than to HJ processing:

- **recA — PP_1629 (Q88ME4):** central recombinase / strand exchange.
- **recBCD — recB PP_4673, recC PP_4674, recD PP_4672:** double-strand-break end resection and RecA loading (ExoV).
- **recFOR — recF PP_0012, recO PP_1435, recR PP_4267:** RecA loading at ssDNA gaps.
- **recJ — PP_1477:** 5'→3' ssDNA exonuclease (end processing).
- **priA — PP_5088:** replication restart at recombination intermediates.

All are present and intact, confirming KT2440 encodes a **complete upstream HR machinery** feeding the RuvABC step.

### 4.3 Replication genes wrongly swept into the candidate set (exclude)

*dnaN* (PP_0011), *holC* (PP_0979), *dnaEA* (PP_1606), *holB* (PP_1966), *dnaQ* (PP_4141), *dnaX* (PP_4269), *holA* (PP_4796), *polA* (PP_0123), *ssb* (PP_0485), and the generic "Exonuclease" ORFs **PP_0353**, **PP_4768** are DNA Pol III / replisome / general-repair components (primary buckets ppu03030 / ppu03420). They should be **removed from the HJ-processing module** scope.

### 4.4 Spurious / over-propagated annotation (do NOT count)

**PP_0151 (Q88RH8), 97 aa, PE=4 "Predicted":** named "Holliday junction resolvase" **solely** from an automated ProtNLM/Google ML prediction (evidence ECO:0008006), with no curated support. Its domain assignments are **PF09498 (DUF2388, domain of unknown function)**, InterPro IPR012661 / TIGRFAM TIGR02448 ("conserved hypothetical protein"). The sequence begins with a hydrophobic signal-peptide-like stretch (MRYLLPLLFAAAGMASAHAMDT…) and **lacks** the RuvC RNase-H catalytic acidic residues and the diagnostic G-I-D-P-G motif. This is a textbook **annotation-hallucination**: it must not be treated as a second resolvase. Separately, **PP_1116 (Q88NT8)** "Site-specific recombinase, resolvase family" is a serine (Tn3-family) site-specific recombinase, unrelated to HJ resolution in recombinational repair.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

1. **No experimental evidence in the target strain.** Every core gene is PE=3 (homology-inferred). No KT2440 knockout, complementation, or biochemical resolvase assay exists. This is the dominant knowledge gap; the module is "covered" by homology, not by direct function.

2. **Single point of failure at resolution.** Resolution depends on RuvC alone — there is **no RusA-type backup resolvase** in the candidate set. This is biologically expected (RusA is a cryptic prophage function in *E. coli*), but it means the module has no redundancy at Step 3. Curators should mark the "alternative resolvase" step as **not_expected_in_target_taxon** rather than a gap.

3. **Regulatory bottleneck, not a genetic gap.** KT2440 is "very sensitive to DNA damage and displays poor homologous recombination efficiencies," attributed to an inefficient RecA–LexA interplay and weak SOS promoters ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)). The HJ-processing genes are all present; the phenotype is a *regulation/expression* limitation. This is consistent with earlier reports that *P. putida* SOS/*lexA* induction differs from *E. coli* ([PMID: 8319897](https://pubmed.ncbi.nlm.nih.gov/8319897/); [PMID: 2372559](https://pubmed.ncbi.nlm.nih.gov/2372559/)).

4. **Over-broad candidate list.** 20 of 24 candidates are either replication genes or upstream HR genes. The KEGG ppu03440 "Homologous recombination" bucket is much wider than the RuvABC module and should not be equated with it.

5. **Over-propagated ML annotation (PP_0151).** As detailed above — exclude.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| RuvA (junction recognition/loading) | **covered** (homology) | PP_1216, syntenic, PE=3 |
| RuvB (branch-migration motor) | **covered** (homology) | PP_1217, Walker A/B annotated, PE=3 |
| RuvC (junction resolution) | **covered** (homology, high confidence) | PP_1215, 63% identity to *E. coli*, full active site |
| RecG (alt. branch migration) | **covered** (parallel/redundant) | PP_5310, domains intact |
| RusA-type alt. resolvase | **not_expected_in_target_taxon** | cryptic prophage function; no ortholog |
| Upstream HR (recA/recBCD/recFOR/recJ/priA) | **out of module scope** (assign to sibling steps) | present but presynaptic |
| Pol III / replisome / generic exonucleases | **out of module scope** (exclude) | belong to ppu03030 |
| PP_0151 "HJ resolvase" | **exclude — likely over-annotation** | ML-only ECO:0008006, DUF2388, no catalytic residues |

**Module-boundary judgment:** The generic KEGG bucket boundary is **wrong for this module** because it conflates the whole ppu03440 "Homologous recombination" map with the narrow RuvABC step. Recommend authoring a dedicated `ruvabc_holliday_junction_processing` module document scoped to RuvA/RuvB/RuvC (+RecG as a parallel branch-migration alternative), and explicitly listing RusA-type resolution as not_expected.

**GO terms of interest (no new-term request appears necessary):** GO:0009378 (four-way junction helicase / Holliday junction helicase), GO:0008821 (crossover junction endodeoxyribonuclease, RuvC), GO:0000725 (recombinational repair), GO:0006310 (DNA recombination). Existing terms cover the module; the main curation action is **restricting propagation**, not requesting new terms.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority order:

1. **ruvC (PP_1215 / Q88NJ2)** — the resolvase and the sole HJ-resolution step; highest curation value. Confirm active-site residues and the 63%-identity ortholog call in a full review.
2. **ruvB (PP_1217 / Q88NJ0)** — confirm Walker A/B motifs and hexamer-forming residues; the *E. coli* RuvBL268S precedent ([PMID: 9973614](https://pubmed.ncbi.nlm.nih.gov/9973614/)) means motif presence ≠ full in-vivo function.
3. **ruvA (PP_1216 / Q88NJ1)** — confirm junction-binding domains and synteny.
4. **recG (PP_5310 / Q88C73)** — confirm helicase domains and clarify its "parallel branch migration" (not resolvase) role in the module document.
5. **PP_0151 (Q88RH8)** — promote specifically to **correct/remove** the spurious "Holliday junction resolvase" name and reclassify as DUF2388 hypothetical protein.

---

## 8. Mechanistic Model / Interpretation

```
   Homologous recombination in P. putida KT2440
   ---------------------------------------------

   DSB / stalled fork
        │
        ▼
   [ RecBCD ]  or  [ RecFOR + RecJ ]   ← end resection / RecA loading  (upstream; present, PE≈3)
        │
        ▼
   [ RecA ]  strand invasion → D-loop   (present)
        │
        ▼
   ┌─────────── HOLLIDAY JUNCTION ───────────┐
   │                                         │
   │   [ RuvA:PP_1216 ] recognizes junction  │
   │            │ loads motor                │
   │   [ RuvB:PP_1217 ] ATP-driven branch    │   ‖  parallel branch migration
   │            │ migration                  │   ‖  [ RecG:PP_5310 ]
   │            ▼                             │
   │   [ RuvC:PP_1215 ] RESOLUTION           │   ← single resolvase, no RusA backup
   │   (RNase-H fold; D8/E67/D139; 63% id)   │
   └─────────────────────────────────────────┘
        │
        ▼
   Two duplex products  →  [ PriA ] replication restart

   REGULATORY OVERLAY: weak RecA–LexA/SOS circuit (PMID 33393180)
   → genes all present, but low induction ⇒ poor HR efficiency & DNA-damage sensitivity
```

The narrative: KT2440 possesses a genetically **complete** HR pathway from resection through resolution. The RuvABC resolvasome is intact and syntenic, RuvC is a high-confidence *E. coli* ortholog, and RecG supplies branch-migration redundancy. The organism's documented fragility toward DNA damage is therefore best explained not by any missing gene, but by a **regulatory bottleneck** in the SOS response that limits how strongly these genes are induced.

---

## 9. Evidence Base

| PMID | Relevance | How it supports/challenges the review |
|------|-----------|----------------------------------------|
| [9501105](https://pubmed.ncbi.nlm.nih.gov/9501105/) | RuvABC division of labor (*E. coli*) | "branch migration is catalysed by the RuvB protein… loaded onto the junction by RuvA, whereas resolution is promoted by the RuvC endonuclease" — defines the roles the KT2440 orthologs perform. |
| [7923356](https://pubmed.ncbi.nlm.nih.gov/7923356/) | RuvC atomic structure (*E. coli*) | "the catalytic center, comprising four acidic residues, lies at the bottom of a cleft" — the acidic residues KT2440 RuvC retains, supporting predicted catalysis. |
| [23118486](https://pubmed.ncbi.nlm.nih.gov/23118486/) | *T. thermophilus* RuvC dimer | Supports the conserved "nick-counter-nick" HJ-resolution mechanism across prokaryotes, applicable to KT2440 RuvC. |
| [27013661](https://pubmed.ncbi.nlm.nih.gov/27013661/) | Poxvirus resolvase vs RuvC | Confirms the RNase-H-superfamily active-site/metal-binding architecture RuvC shares. |
| [18375550](https://pubmed.ncbi.nlm.nih.gov/18375550/) | RecG as independent branch-migration helicase | "Orthologs of RecG and RuvABC are highly conserved… independent pathways that branch migrate Holliday junctions… RecG… convert stalled replication forks into Holliday junctions." |
| [9973614](https://pubmed.ncbi.nlm.nih.gov/9973614/) | RuvBL268S mutant (*E. coli*) | In-vitro-active RuvB can still fail in vivo — a caution that motif presence ≠ full function; keeps RuvB at homology grade. |
| [33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/) | Faulty SOS in KT2440 (**target strain**) | "very sensitive to DNA damage and displays poor homologous recombination efficiencies"; "fails to mount a strong SOS response due to the inefficacy of the crucial RecA-LexA interplay." |
| [8319897](https://pubmed.ncbi.nlm.nih.gov/8319897/) | *P. putida/aeruginosa lexA* induction | *P. putida lexA* induction is higher/earlier and UV-dose-independent vs *E. coli* — corroborates atypical SOS regulation. |
| [2372559](https://pubmed.ncbi.nlm.nih.gov/2372559/) | SOS-like response in *P. putida* | RecA-dependent SOS-like response exists in *P. putida*, but with distinct behavior. |
| [34073022](https://pubmed.ncbi.nlm.nih.gov/34073022/) | DisA limits RecG at forks | RecG fork activity is itself regulated — relevant to interpreting RecG's role. |
| [37358447](https://pubmed.ncbi.nlm.nih.gov/37358447/) | RuvABC not required for certain IS processes | Context on RuvABC dispensability in some transposition contexts. |

**Evidence grade for the target organism:** All *P. putida* KT2440 conclusions about RuvABC/RecG gene content and structure are **homology-grade** (UniProt PE=3; sequence/synteny/active-site analysis). The **only direct target-strain experimental evidence** is the SOS/recombination-efficiency phenotype ([PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)). Functional transfer of RuvABC roles from *E. coli* is rated **strong** for RuvC (63% identity, full active site) and **strong-to-moderate** for RuvA/RuvB/RecG (domain/synteny conservation, but the RuvBL268S precedent tempers certainty).

---

## 10. Limitations and Knowledge Gaps

- **No direct KT2440 function data** for any RuvABC/RecG gene (no knockouts, no purified-protein resolvase assays). Confidence rests on homology and conserved motifs.
- **Single resolvase:** no redundancy at the resolution step; if RuvC were non-functional, the model predicts no backup (RusA-type) resolvase.
- **Regulation not fully mapped:** the weak SOS circuit is documented at the *recA/lexA* level, but induction kinetics of *ruvCAB* specifically in KT2440 have not been measured.
- **Sequence analysis performed here** (identity, active-site inspection) is bioinformatic; structural or biochemical confirmation is absent.

---

## 11. Proposed Follow-up Experiments / Curation Actions

1. **Curation (immediate):** Re-scope the module to {ruvA PP_1216, ruvB PP_1217, ruvC PP_1215} + RecG PP_5310 (parallel branch migration); mark RusA-type resolvase **not_expected_in_target_taxon**; move recA/recBCD/recFOR/recJ/priA to sibling presynaptic steps; exclude all Pol III / replisome / generic-exonuclease genes.
2. **Fix annotation:** Submit a correction for **PP_0151** (remove "Holliday junction resolvase"; reclassify as DUF2388 hypothetical) and flag the ProtNLM ECO:0008006 source.
3. **Promote to full review:** ruvC → ruvB → ruvA → recG → PP_0151 (as above).
4. **Wet-lab (to resolve the core gap):** construct *ruvC*, *ruvAB*, and *recG* deletions in KT2440; assay UV/mitomycin-C/ciprofloxacin sensitivity and conjugational/recombination frequency to confirm functional roles directly in the target strain.
5. **Biochemistry:** purify KT2440 RuvC and test HJ cleavage in vitro (Mg²⁺/Mn²⁺ dependence) to validate the RNase-H active-site prediction.
6. **Expression:** measure *ruvCAB* induction after DNA damage in KT2440 to test whether the weak-SOS phenotype extends to reduced RuvABC induction specifically.

---

## 12. Key References

- Van Gool AJ et al. Functional interactions between the Holliday junction resolvase and the branch migration motor of *E. coli*. [PMID: 9501105](https://pubmed.ncbi.nlm.nih.gov/9501105/)
- Ariyoshi M et al. Atomic structure of the RuvC resolvase. [PMID: 7923356](https://pubmed.ncbi.nlm.nih.gov/7923356/)
- Górna AE et al. Structural asymmetry in the *T. thermophilus* RuvC dimer. [PMID: 23118486](https://pubmed.ncbi.nlm.nih.gov/23118486/)
- Poxvirus resolvase structure/metal binding. [PMID: 27013661](https://pubmed.ncbi.nlm.nih.gov/27013661/)
- Repair and antirepair DNA helicases in *Helicobacter pylori* (RecG/RuvABC). [PMID: 18375550](https://pubmed.ncbi.nlm.nih.gov/18375550/)
- *E. coli* RuvBL268S mutant. [PMID: 9973614](https://pubmed.ncbi.nlm.nih.gov/9973614/)
- Akkaya Ö et al. The faulty SOS response of *P. putida* KT2440. [PMID: 33393180](https://pubmed.ncbi.nlm.nih.gov/33393180/)
- *P. putida/aeruginosa lexA* induction. [PMID: 8319897](https://pubmed.ncbi.nlm.nih.gov/8319897/)
- SOS-like reactions of *P. putida*. [PMID: 2372559](https://pubmed.ncbi.nlm.nih.gov/2372559/)
- DisA limits RecG at stalled/reversed forks. [PMID: 34073022](https://pubmed.ncbi.nlm.nih.gov/34073022/)
- RuvABC not required for certain IS processes. [PMID: 37358447](https://pubmed.ncbi.nlm.nih.gov/37358447/)

---

## Consensus Answer

The RuvABC Holliday-junction processing module is complete and predicted catalytically competent in *P. putida* KT2440: *ruvA* (PP_1216), *ruvB* (PP_1217) and *ruvC* (PP_1215) form a conserved *ruvCAB* cluster, RuvC is a strong *E. coli* ortholog (63% identity, intact RNase-H active site), and RecG (PP_5310) provides parallel branch migration — so all core steps are COVERED at homology grade. All evidence is homology-based (PE=3, no direct KT2440 experiments), and the strain's documented DNA-damage sensitivity reflects a weak RecA–LexA/SOS regulatory circuit rather than any missing HJ-processing gene. The supplied candidate list is over-broad (Pol III/replisome and upstream HR genes belong to other buckets), and PP_0151 "Holliday junction resolvase" is a spurious ML annotation to be excluded.


## Artifacts

- [OpenScientist final report](PSEPK__ruvabc-holliday-junction-processing__ppu03440-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__ruvabc-holliday-junction-processing__ppu03440-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9501105
2. PMID:9973614
3. PMID:18375550
4. PMID:34073022
5. PMID:33393180
6. PMID:8319897
7. PMID:2372559
8. PMID:7923356
9. PMID:23118486
10. PMID:27013661
11. PMID:37358447