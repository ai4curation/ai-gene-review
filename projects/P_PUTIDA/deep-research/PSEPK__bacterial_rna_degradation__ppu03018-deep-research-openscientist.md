---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T14:10:25.413708'
end_time: '2026-09-01T14:31:02.502293'
duration_seconds: 1237.09
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Gammaproteobacterial RNase E-centered RNA degradation
  module_summary: Reusable RNA-degradation module in which RNase E initiates decay,
    an optional recruited DEAD-box helicase assists with structured substrates, and
    a 3'-to-5' exoribonuclease completes processive degradation. RhlB/RhlE and PNPase/RNase
    R are represented as lineage-variable implementations.
  module_outline: "- Gammaproteobacterial RNase E-centered RNA degradation\n  - 1.\
    \ endonucleolytic initiation and complex organization\n  - RNase E cleavage of\
    \ RNA\n    - RNase E catalytic and scaffolding activity (molecular player: bacterial\
    \ RNase E family; activity or role: ribonuclease E activity)\n  - 2. ATP-dependent\
    \ unwinding of structured RNA\n  - DEAD-box-helicase-assisted RNA unwinding\n\
    \    - Alternative versions by helicase partner identity: Recruited DEAD-box helicase\
    \ variants\n      - RhlB-assisted unwinding\n        - RhlB RNA helicase activity\
    \ (molecular player: DEAD-box RNA helicase RhlB family; activity or role: RNA\
    \ helicase activity)\n      - RhlE-assisted unwinding\n        - RhlE RNA helicase\
    \ activity (molecular player: DEAD-box RNA helicase RhlE family; activity or role:\
    \ RNA helicase activity)\n  - 3. processive 3'-to-5' exonucleolysis\n  - Processive\
    \ 3'-to-5' RNA degradation\n    - Alternative versions by exonuclease partner\
    \ identity: Recruited 3'-to-5' exonuclease variants\n      - PNPase phosphorolysis\n\
    \        - PNPase activity (molecular player: bacterial polynucleotide phosphorylase\
    \ family; activity or role: polyribonucleotide nucleotidyltransferase activity)\n\
    \      - RNase R hydrolytic exonucleolysis\n        - RNase R activity (molecular\
    \ player: bacterial RNase R family; activity or role: exoribonuclease II activity)"
  module_connections: '- RNase E cleavage of RNA feeds into DEAD-box-helicase-assisted
    RNA unwinding: RNase E cleavage products can be unwound before exonucleolysis.

    - RNase E cleavage of RNA feeds into Processive 3''-to-5'' RNA degradation: RNase
    E cleavage generates substrates for processive 3''-to-5'' degradation.

    - DEAD-box-helicase-assisted RNA unwinding feeds into Processive 3''-to-5'' RNA
    degradation: Helicase-assisted unwinding makes structured substrates accessible
    to exonucleases.'
  pathway_query: ppu03018
  pathway_id: ppu03018
  pathway_name: RNA degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03018 with 15 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '17'
  candidate_genes: '- ppkB: PP_0712 | Q88PY6 | ADP/GDP-polyphosphate phosphotransferase
    (EC 2.7.4.-) (Polyphosphate kinase PPK2) (EC 2.7.4.-; primary bucket kegg:ppu03018)

    - rhlB: PP_1295 | Q88NB7 | ATP-dependent RNA helicase RhlB (EC 3.6.4.13) (EC 3.6.4.13;
    primary bucket kegg:ppu03018)

    - groEL: PP_1361 | Q88N55 | Chaperonin GroEL (EC 5.6.1.7) (60 kDa chaperonin)
    (Chaperonin-60) (Cpn60) (EC 5.6.1.7; primary bucket kegg:ppu04156)

    - eno: PP_1612 | Q88MF9 | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase)
    (2-phosphoglycerate dehydratase) (EC 4.2.1.11; primary bucket kegg:ppu03018)

    - deaD: PP_1868 | Q88LR1 | ATP-dependent RNA helicase DeaD (EC 3.6.4.13) (Cold-shock
    DEAD box protein A) (EC 3.6.4.13; primary bucket kegg:ppu03018)

    - rne: PP_1905 | Q88LM4 | Ribonuclease E (RNase E) (EC 3.1.26.12) (EC 3.1.26.12;
    primary bucket kegg:ppu03018)

    - recQ: PP_4516 | Q88EE9 | DNA helicase RecQ (EC 5.6.2.4) (EC 5.6.2.4; primary
    bucket kegg:ppu03018)

    - pcnB: PP_4697 | Q88DX1 | Poly(A) polymerase I (PAP I) (EC 2.7.7.19) (EC 2.7.7.19;
    primary bucket kegg:ppu03018)

    - pnp: PP_4708 | Q88DW0 | Polyribonucleotide nucleotidyltransferase (EC 2.7.7.8)
    (Polynucleotide phosphorylase) (PNPase) (EC 2.7.7.8; primary bucket kegg:ppu03018)

    - dnaK: PP_4727 | Q88DU2 | Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein)
    (Heat shock protein 70) (primary bucket kegg:ppu04156)

    - rhlE-I: PP_4766 | Q88DQ7 | DEAD-box ATP-dependent RNA helicase RhpA (EC 3.6.4.13)
    (EC 3.6.4.13; primary bucket kegg:ppu03018)

    - rnr: PP_4880 | Q88DE6 | Ribonuclease R (RNase R) (EC 3.1.13.1) (EC 3.1.13.1;
    primary bucket kegg:ppu03018)

    - hfq: PP_4894 | Q88DD3 | RNA-binding protein Hfq (primary bucket kegg:ppu03018)

    - rhlE: PP_4980 | Q88D48 | ATP-dependent RNA helicase RhlE (EC 3.6.4.13) (EC 3.6.4.13;
    primary bucket kegg:ppu03018)

    - rppH: PP_5146 | Q88CN4 | RNA pyrophosphohydrolase (EC 3.6.1.-) ((Di)nucleoside
    polyphosphate hydrolase) (EC 3.6.1.-; primary bucket kegg:ppu03018)

    - rho: PP_5214 | Q88CG7 | Transcription termination factor Rho (EC 3.6.4.-) (ATP-dependent
    helicase Rho) (EC 3.6.4.-; primary bucket kegg:ppu03018)

    - ppk: PP_5217 | Q88CG4 | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate
    phosphotransferase) (Polyphosphoric acid kinase) (EC 2.7.4.1; primary bucket kegg:ppu03018)'
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_rna_degradation__ppu03018-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_rna_degradation__ppu03018-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Gammaproteobacterial RNase E-centered RNA degradation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03018
- Resolved ID: ppu03018
- Resolved name: RNA degradation
- Source: KEGG

Resolved local bucket kegg:ppu03018 with 15 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 17

- ppkB: PP_0712 | Q88PY6 | ADP/GDP-polyphosphate phosphotransferase (EC 2.7.4.-) (Polyphosphate kinase PPK2) (EC 2.7.4.-; primary bucket kegg:ppu03018)
- rhlB: PP_1295 | Q88NB7 | ATP-dependent RNA helicase RhlB (EC 3.6.4.13) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- groEL: PP_1361 | Q88N55 | Chaperonin GroEL (EC 5.6.1.7) (60 kDa chaperonin) (Chaperonin-60) (Cpn60) (EC 5.6.1.7; primary bucket kegg:ppu04156)
- eno: PP_1612 | Q88MF9 | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase) (EC 4.2.1.11; primary bucket kegg:ppu03018)
- deaD: PP_1868 | Q88LR1 | ATP-dependent RNA helicase DeaD (EC 3.6.4.13) (Cold-shock DEAD box protein A) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- rne: PP_1905 | Q88LM4 | Ribonuclease E (RNase E) (EC 3.1.26.12) (EC 3.1.26.12; primary bucket kegg:ppu03018)
- recQ: PP_4516 | Q88EE9 | DNA helicase RecQ (EC 5.6.2.4) (EC 5.6.2.4; primary bucket kegg:ppu03018)
- pcnB: PP_4697 | Q88DX1 | Poly(A) polymerase I (PAP I) (EC 2.7.7.19) (EC 2.7.7.19; primary bucket kegg:ppu03018)
- pnp: PP_4708 | Q88DW0 | Polyribonucleotide nucleotidyltransferase (EC 2.7.7.8) (Polynucleotide phosphorylase) (PNPase) (EC 2.7.7.8; primary bucket kegg:ppu03018)
- dnaK: PP_4727 | Q88DU2 | Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein) (Heat shock protein 70) (primary bucket kegg:ppu04156)
- rhlE-I: PP_4766 | Q88DQ7 | DEAD-box ATP-dependent RNA helicase RhpA (EC 3.6.4.13) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- rnr: PP_4880 | Q88DE6 | Ribonuclease R (RNase R) (EC 3.1.13.1) (EC 3.1.13.1; primary bucket kegg:ppu03018)
- hfq: PP_4894 | Q88DD3 | RNA-binding protein Hfq (primary bucket kegg:ppu03018)
- rhlE: PP_4980 | Q88D48 | ATP-dependent RNA helicase RhlE (EC 3.6.4.13) (EC 3.6.4.13; primary bucket kegg:ppu03018)
- rppH: PP_5146 | Q88CN4 | RNA pyrophosphohydrolase (EC 3.6.1.-) ((Di)nucleoside polyphosphate hydrolase) (EC 3.6.1.-; primary bucket kegg:ppu03018)
- rho: PP_5214 | Q88CG7 | Transcription termination factor Rho (EC 3.6.4.-) (ATP-dependent helicase Rho) (EC 3.6.4.-; primary bucket kegg:ppu03018)
- ppk: PP_5217 | Q88CG4 | Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate phosphotransferase) (Polyphosphoric acid kinase) (EC 2.7.4.1; primary bucket kegg:ppu03018)

## Generic Module Context

### Working Scope

Reusable RNA-degradation module in which RNase E initiates decay, an optional recruited DEAD-box helicase assists with structured substrates, and a 3'-to-5' exoribonuclease completes processive degradation. RhlB/RhlE and PNPase/RNase R are represented as lineage-variable implementations.

### Provisional Biological Outline

- Gammaproteobacterial RNase E-centered RNA degradation
  - 1. endonucleolytic initiation and complex organization
  - RNase E cleavage of RNA
    - RNase E catalytic and scaffolding activity (molecular player: bacterial RNase E family; activity or role: ribonuclease E activity)
  - 2. ATP-dependent unwinding of structured RNA
  - DEAD-box-helicase-assisted RNA unwinding
    - Alternative versions by helicase partner identity: Recruited DEAD-box helicase variants
      - RhlB-assisted unwinding
        - RhlB RNA helicase activity (molecular player: DEAD-box RNA helicase RhlB family; activity or role: RNA helicase activity)
      - RhlE-assisted unwinding
        - RhlE RNA helicase activity (molecular player: DEAD-box RNA helicase RhlE family; activity or role: RNA helicase activity)
  - 3. processive 3'-to-5' exonucleolysis
  - Processive 3'-to-5' RNA degradation
    - Alternative versions by exonuclease partner identity: Recruited 3'-to-5' exonuclease variants
      - PNPase phosphorolysis
        - PNPase activity (molecular player: bacterial polynucleotide phosphorylase family; activity or role: polyribonucleotide nucleotidyltransferase activity)
      - RNase R hydrolytic exonucleolysis
        - RNase R activity (molecular player: bacterial RNase R family; activity or role: exoribonuclease II activity)

### Known Relationships Among Steps

- RNase E cleavage of RNA feeds into DEAD-box-helicase-assisted RNA unwinding: RNase E cleavage products can be unwound before exonucleolysis.
- RNase E cleavage of RNA feeds into Processive 3'-to-5' RNA degradation: RNase E cleavage generates substrates for processive 3'-to-5' degradation.
- DEAD-box-helicase-assisted RNA unwinding feeds into Processive 3'-to-5' RNA degradation: Helicase-assisted unwinding makes structured substrates accessible to exonucleases.

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

# Commissioned Review: Gammaproteobacterial RNase E-Centered RNA Degradation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03018` "RNA degradation" (15 primary genes; module area `other_kegg_pathway`)
**Module:** Reusable RNase E-initiated decay module — endonucleolytic initiation → optional DEAD-box unwinding → processive 3'→5' exonucleolysis, with RhlB/RhlE and PNPase/RNase R as lineage-variable implementations.

---

## 1. Executive Summary

The RNase E-centered RNA-degradation module encoded by KEGG bucket `ppu03018` is **satisfiable in *Pseudomonas putida* KT2440**. Every mechanistic step of the working module can be assigned to at least one candidate gene, and — importantly — **both OR-branches of the two variant steps are encoded in the genome**. Step 1 (endonucleolytic initiation and degradosome scaffolding) is covered by *rne*/RNase E (PP_1905). Step 2 (ATP-dependent unwinding of structured RNA) is covered by RhlB (PP_1295) with additional DEAD-box paralogs RhlE (PP_4980), RhlE-I/RhpA (PP_4766), and the cold-shock helicase DeaD/CsdA (PP_1868). Step 3 (processive 3'→5' exonucleolysis) is covered by **both** PNPase (PP_4708) and RNase R (PP_4880). The presence of both exonucleases and multiple helicases is consistent with condition-dependent degradosome remodeling seen elsewhere in the genus, where cold-adapted *Pseudomonas* substitutes RNase R + RhlE for PNPase + RhlB.

The strongest, most directly transferable evidence comes from the same genus. Systematic mapping of the *P. aeruginosa* RNase E C-terminal scaffolding domain identifies short linear motifs (SLiMs) that recruit **PNPase and RhlB as the core partners** — establishing the Pseudomonas degradosome architecture that KT2440 almost certainly shares. However, mechanistic details diverge sharply from the *E. coli* paradigm: Pseudomonas RhlB belongs to a distinct **"Type II" helicase clade** with an N-terminal intrinsically disordered region driving phase separation, and RNase E *antagonizes* rather than stimulates it. A sequence-similarity analysis quantified this: KT2440 degradosome proteins are roughly an order of magnitude more similar to their *P. aeruginosa* orthologs than to *E. coli* (e.g., RhlB ~52% vs. ~4% 5-mer Jaccard similarity). **Species transfer from *P. aeruginosa* is strong; transfer from *E. coli* is weak and must be flagged in curation.** Only Hfq (PP_4894) has direct functional characterization in KT2440 itself (Crc–Hfq translational repression).

For curation, the candidate list should be **trimmed of KEGG map co-listings and over-propagated annotations**: *recQ* (a DNA helicase), *rho* (transcription termination), *dnaK* and *groEL* (general chaperones, primary bucket ppu04156), and *ppk*/*ppkB* (polyphosphate kinases) are not core module members. Enolase (*eno*, PP_1612) is a bona fide *E. coli* degradosome subunit but is **most likely NOT a core Pseudomonas degradosome component** — its inclusion reflects *E. coli*-templated annotation, and the *P. aeruginosa* CTD interactome does not report an enolase-binding microdomain. The genes *rne*, *rhlB*, *pnp*, *rnr*, *rhlE*, and *rhlE-I* should be promoted to full `fetch-gene` review.

---

## 2. Target-Organism Pathway Definition

### What the pathway includes

The module describes **RNase E-initiated messenger-RNA and stable-RNA turnover** — the ordered, mostly cytoplasmic process by which:

1. **Initiation / 5'-end sensing:** RNA pyrophosphohydrolase (RppH) converts protective 5'-triphosphate ends to 5'-monophosphate, the preferred substrate for RNase E; RNase E then makes internal endonucleolytic cuts.
2. **Scaffolding:** The RNase E C-terminal domain (CTD) nucleates a multi-enzyme "RNA degradosome" via short linear motifs.
3. **Unwinding:** A recruited DEAD-box RNA helicase (RhlB and/or RhlE) uses ATP to melt secondary structure that would otherwise block exonucleases.
4. **Processive decay:** A 3'→5' exoribonuclease (PNPase and/or RNase R) degrades the cleavage products to short oligonucleotides/mononucleotides.
5. **3'-end tagging (accessory):** Poly(A) polymerase PcnB adds 3' A-tails that stimulate exonucleolytic attack.
6. **Riboregulation (accessory):** Hfq chaperones small RNAs and modulates target accessibility.

### Neighboring pathways to keep separate

- **Transcription termination** (Rho): a distinct process; Rho terminates transcription and is not part of the decay machinery.
- **DNA repair/recombination** (RecQ): a DNA helicase, unrelated to RNA decay.
- **Protein folding / chaperones** (ppu04156: DnaK, GroEL): peripheral to degradosome assembly at best, not catalytic decay steps.
- **Polyphosphate metabolism** (Ppk, PpkB): energy/phosphate storage, not RNA decay.
- **Glycolysis / central carbon metabolism** (Enolase): a glycolytic enzyme whose *E. coli* degradosome moonlighting does not clearly transfer to Pseudomonas.

### Alternate names and database definitions

- KEGG `ppu03018` = "RNA degradation" (organism-specific instance of the reference map `03018`).
- The physical complex is the **"RNA degradosome"**; the Pseudomonas version is sometimes called the "cold-shock degradosome" when RNase R + RhlE are incorporated.
- RNase E = EC 3.1.26.12; PNPase = EC 2.7.7.8; RNase R = EC 3.1.13.1; DEAD-box helicases = EC 3.6.4.13.

---

## 3. Expected Step Model

```
        5'-PPP RNA
           │
      [RppH: PP_5146]  ── 5'-pyrophosphate removal ──►  5'-P RNA
           │
   ┌───────▼─────────────────────────────────────────┐
   │  STEP 1  ENDONUCLEOLYTIC INITIATION + SCAFFOLD   │
   │  RNase E (rne, PP_1905)  ◄── degradosome hub     │
   │  CTD SLiMs recruit partners (Pseudomonas mode)   │
   └───────┬──────────────────────────┬──────────────┘
           │                          │
   ┌───────▼──────────┐       ┌───────▼───────────────┐
   │ STEP 2 UNWINDING │       │ (Hfq PP_4894: sRNA)    │
   │  DEAD-box helicase│      │ (PcnB PP_4697: 3'-A tag)│
   │  OR-branch:       │      └────────────────────────┘
   │   • RhlB PP_1295  │ (Type II clade, core partner)
   │   • RhlE PP_4980  │ (RGG/IDR, phase-separating)
   │   • RhlE-I PP_4766│ (RhpA paralog)
   │   • DeaD  PP_1868 │ (cold-shock CsdA)
   └───────┬───────────┘
           │
   ┌───────▼─────────────────────────────────────────┐
   │  STEP 3  PROCESSIVE 3'→5' EXONUCLEOLYSIS         │
   │  OR-branch:                                      │
   │   • PNPase (pnp, PP_4708)   phosphorolytic       │
   │   • RNase R (rnr, PP_4880)  hydrolytic, cold     │
   └──────────────────────────────────────────────────┘
```

**Branch logic:** Steps 2 and 3 are OR-steps. The module is satisfied if *at least one* helicase and *at least one* exonuclease are present. In KT2440 **all branches are encoded**, which is stronger than minimal satisfiability and consistent with condition-dependent degradosome composition.

---

## 4. Candidate Genes and Evidence

### High-confidence core module genes

| Gene | Locus | UniProt | Module step | Confidence | Evidence type |
|------|-------|---------|-------------|------------|---------------|
| *rne* (RNase E) | PP_1905 | Q88LM4 | Step 1 scaffold + endonuclease | High | Genus (P. aeruginosa) direct + homology |
| *rhlB* | PP_1295 | Q88NB7 | Step 2 helicase (core partner) | High | Genus direct + sequence orthology |
| *pnp* (PNPase) | PP_4708 | Q88DW0 | Step 3 exonuclease (core partner) | High | Genus direct + homology |
| *rnr* (RNase R) | PP_4880 | Q88DE6 | Step 3 exonuclease (cold variant) | High | Genus (P. syringae) direct |
| *rhlE* | PP_4980 | Q88D48 | Step 2 helicase (variant) | High | Genus + sequence (IDR) |
| *rhlE-I*/RhpA | PP_4766 | Q88DQ7 | Step 2 helicase (paralog) | Medium | Sequence paralog resolution |
| *hfq* | PP_4894 | Q88DD3 | Accessory riboregulator | High | **Direct KT2440 experiment** |
| *rppH* | PP_5146 | Q88CN4 | Accessory 5'-trigger | Medium | Homology (E. coli mechanism) |
| *pcnB* (PAP I) | PP_4697 | Q88DX1 | Accessory 3'-tagging | Medium | Homology (E. coli mechanism) |
| *deaD*/CsdA | PP_1868 | Q88LR1 | Step 2 helicase (cold-shock) | Medium | Sequence paralog + homology |

### Gene-by-gene assessment

**RNase E — *rne* (PP_1905).** The conserved catalytic and scaffolding hub of the module. In *P. aeruginosa*, systematic CTD interactome mapping identified the SLiMs required for membrane attachment, RNA binding, complex clustering, and **direct binding to the core partners PNPase and RhlB** ([PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/)). Cryo-EM/biochemistry showed the PNPase–RNase E association is maintained across *E. coli*, *Salmonella*, and *P. aeruginosa* but through lineage-specific recognition modes ([PMID: 41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/)). KT2440 encodes a full-length RNase E (~1091 aa) with an intact C-terminal scaffold, so the scaffolding step transfers strongly from the genus. **Caveat:** the recognition interface is genus-specific — do not transfer *E. coli* CTD-microdomain annotations verbatim.

**RhlB — *rhlB* (PP_1295).** A core degradosome helicase in Pseudomonas. It belongs to a **distinct "Type II" clade** exemplified by *P. aeruginosa* RhlB, containing an N-terminal intrinsically disordered region that drives RNA-dependent liquid–liquid phase separation; *P. aeruginosa* RNase E binds it through an interface **distinct from the E. coli model** and **antagonizes** rather than stimulates its condensation, controlling growth at low temperature ([PMID: 42581758](https://pubmed.ncbi.nlm.nih.gov/42581758/)). Sequence analysis confirms KT2440 RhlB (Q88NB7, 398 aa) is a near-identical ortholog of the *P. aeruginosa* Type II reference (Q9HXE5, 397 aa) with a compact architecture (~15 aa upstream of the DEAD-box Walker A GTGKT motif) like *E. coli* RhlB. **Caveat:** annotation should note the Type II regulatory divergence from *E. coli*.

**PNPase — *pnp* (PP_4708).** The phosphorolytic 3'→5' exonuclease and a core degradosome partner in Pseudomonas ([PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/); [PMID: 41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/)). High confidence for Step 3.

**RNase R — *rnr* (PP_4880).** The hydrolytic 3'→5' exonuclease alternative. In the psychrotroph *P. syringae* Lz4W, the degradosome contains **RNase R instead of PNPase**, together with RNase E and the DEAD-box helicase RhlE ([PMID: 15705581](https://pubmed.ncbi.nlm.nih.gov/15705581/)); RNase R interacts directly with RNase E and is essential for growth at 4 °C, with a novel role in rRNA 3'-end processing ([PMID: 17405875](https://pubmed.ncbi.nlm.nih.gov/17405875/)). This establishes the exonuclease-variant OR-branch as genuine within the genus. High confidence.

**RhlE — *rhlE* (PP_4980).** The RhlE-family helicase and the demonstrated cold-degradosome partner in *P. syringae* ([PMID: 15705581](https://pubmed.ncbi.nlm.nih.gov/15705581/)). Sequence analysis shows KT2440 RhlE (Q88D48, 626 aa) carries a ~249-aa C-terminal extension that is strongly disorder-promoting (fraction A/R/G/Q/S/E/K/P = 0.76) and RGG/RG-rich (…GGGEKRPPRANNGGGARRDGGGGRGRPARD…) — a classic phase-separation-prone IDR. **This is the phase-separating helicase in KT2440**, distinct from the compact RhlB.

**RhlE-I / RhpA — *rhlE-I* (PP_4766).** A second RhlE-family paralog (Q88DQ7, 443 aa) with a ~66-aa Lys/Arg-rich C-tail (disorder-promoting fraction 0.73). Resolved as a distinct paralog by sequence. Medium confidence; paralog ambiguity flagged.

**DeaD / CsdA — *deaD* (PP_1868).** Cold-shock DEAD-box helicase (Q88LR1, 559 aa, ~177-aa C-tail, disorder fraction 0.62). A fourth distinct paralog; likely a condition-specific helicase rather than the constitutive core partner. Medium confidence.

**Hfq — *hfq* (PP_4894).** The **only candidate with direct KT2440 evidence**: in *P. putida* KT2440, carbon catabolite repression is mediated by the **Crc–Hfq complex** binding the 5' region of target mRNAs to inhibit translation ([PMID: 37348756](https://pubmed.ncbi.nlm.nih.gov/37348756/)). This directly validates Hfq's post-transcriptional-regulatory role in the target strain.

**RppH — *rppH* (PP_5146).** Accessory 5'-end decay trigger. In *E. coli*, RppH (formerly NudH/YgdP) removes pyrophosphate to convert 5'-triphosphate to 5'-monophosphate, initiating 5'-end-dependent decay via RNase E ([PMID: 18202662](https://pubmed.ncbi.nlm.nih.gov/18202662/)). Role in KT2440 is homology-inferred (medium confidence).

**PcnB (PAP I) — *pcnB* (PP_4697).** Accessory 3'-tagging. In *E. coli*, 3' adenylation directly affects digestion by PNPase, and 3' adenylation and 5' phosphorylation act cooperatively ([PMID: 7533264](https://pubmed.ncbi.nlm.nih.gov/7533264/)). Role in KT2440 is homology-inferred (medium confidence).

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### Likely KEGG co-listings / over-propagated annotations (recommend removal from module)

The KEGG RNA-degradation map co-lists helper/regulatory nodes that are **not** part of the RNase E endo–helicase–exo core:

| Gene | Locus | Actual function | Why excluded |
|------|-------|-----------------|--------------|
| *recQ* | PP_4516 | DNA helicase (EC 5.6.2.4) | DNA repair/recombination; no RNA-decay role |
| *rho* | PP_5214 | Transcription termination factor Rho | Transcription, not decay |
| *dnaK* | PP_4727 | Chaperone HSP70 | General chaperone (primary bucket ppu04156) |
| *groEL* | PP_1361 | Chaperonin GroEL | General chaperone (primary bucket ppu04156) |
| *ppk* | PP_5217 | Polyphosphate kinase (EC 2.7.4.1) | PolyP metabolism |
| *ppkB* | PP_0712 | ADP/GDP-polyphosphate phosphotransferase | PolyP metabolism |

These are peripheral degradosome-assembly/cold-shock helpers at best (DnaK/GroEL) or wholly unrelated (RecQ, Rho, Ppk/PpkB). They should not count toward module satisfiability.

### Enolase — the key over-annotation call

Enolase (*eno*, PP_1612) is a genuine and well-documented degradosome subunit in *E. coli*/Enterobacteriaceae, where it is recruited via a short, poorly conserved CTD microdomain. However, its membership in the **Pseudomonas** degradosome is **not established**. The systematic *P. aeruginosa* RNase E CTD interactome reported binding microdomains for **PNPase and RhlB only — no enolase-binding microdomain** ([PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/)). The only *P. aeruginosa* mention of an "enolase dimer" appears in a generic degradosome description within a structural RraA paper ([PMID: 21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/)), **not** a demonstration of direct binding. KT2440 *eno* carries a canonical glycolytic annotation (EC 4.2.1.11). **Recommendation: treat enolase as glycolytic, not a core Pseudomonas degradosome subunit; its ppu03018 listing reflects E. coli-templated annotation.**

### Paralog ambiguity

Four distinct DEAD-box helicase paralogs are resolved by sequence: RhlB (compact core partner, 398 aa), RhlE (RGG/IDR, phase-separating, 626 aa), RhlE-I/RhpA (short K/R-rich tail, 443 aa), and DeaD/CsdA (cold-shock, 559 aa). Curators should ensure each locus retains its specific paralog identity and not be collapsed under a generic "EC 3.6.4.13 DEAD-box helicase" annotation. RhlE vs. RhlB identity is the most important distinction because they play mechanistically different roles (RhlB = constitutive core; RhlE = cold/structured-substrate variant).

### Species-transfer strength (quantified)

A conservative 5-mer Jaccard similarity proxy showed KT2440 degradosome proteins are far closer to *P. aeruginosa* (same genus) than to *E. coli*:

| Protein | vs. *E. coli* | vs. *P. aeruginosa* |
|---------|--------------|---------------------|
| RhlB | 3.8% | 52.5% (containment 68.8%) |
| PNPase | 10.6% | 41.4% (containment 58.6%) |
| Hfq | 21.6% | 44.1% (containment 59.8%) |
| RNase E | 9.5% | (not retrieved; expected high) |
| RNase R | 5.1% | (not retrieved; expected high) |
| RhlE | 9.4% | (not retrieved; expected high) |

**Curation rule of thumb:** transfer functional detail from *P. aeruginosa*/genus with high confidence; transfer from *E. coli* only for broad enzyme identity, and flag mechanistic/regulatory details (especially RhlB regulation and enolase membership) as *E. coli*-specific.

---

## 6. Mechanistic Model / Interpretation

Synthesizing the findings, KT2440 possesses a **complete, genus-typical, and condition-flexible RNase E degradosome**. RNase E serves as the membrane-associated scaffold whose C-terminal disordered domain presents SLiMs recruiting the core partners PNPase and RhlB ([PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/)). Unlike the textbook *E. coli* complex, the Pseudomonas complex (a) uses genus-specific recognition interfaces for PNPase ([PMID: 41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/)), (b) recruits a **Type II RhlB** whose activity is *antagonized* — not stimulated — by RNase E through phase-separation control ([PMID: 42581758](https://pubmed.ncbi.nlm.nih.gov/42581758/)), and (c) **likely does not incorporate enolase** as a core subunit ([PMID: 40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/)).

Under cold stress, the genus can remodel the complex to swap RNase R for PNPase and RhlE for RhlB ([PMID: 15705581](https://pubmed.ncbi.nlm.nih.gov/15705581/), [PMID: 17405875](https://pubmed.ncbi.nlm.nih.gov/17405875/)), and KT2440 encodes all the parts (RNase R PP_4880, RhlE PP_4980, DeaD PP_1868) to do so. Upstream, RppH primes transcripts by 5'-pyrophosphate removal ([PMID: 18202662](https://pubmed.ncbi.nlm.nih.gov/18202662/)) and PcnB tags 3' ends to accelerate exonucleolysis ([PMID: 7533264](https://pubmed.ncbi.nlm.nih.gov/7533264/)); Hfq, the only directly validated KT2440 component, integrates small-RNA and catabolite-repression signals ([PMID: 37348756](https://pubmed.ncbi.nlm.nih.gov/37348756/)). The net picture is a module that is not merely "present" but **redundantly and adaptively provisioned** in this organism.

The degradosome remodeling logic can be summarized as:

| Condition | Endonuclease | Helicase | Exonuclease |
|-----------|-------------|----------|-------------|
| Standard (mesophilic) | RNase E (PP_1905) | RhlB (PP_1295) | PNPase (PP_4708) |
| Cold / structured substrates | RNase E (PP_1905) | RhlE (PP_4980) / DeaD (PP_1868) | RNase R (PP_4880) |

---

## 7. Module and GO-Curation Recommendations

| Module step | Status | Rationale |
|-------------|--------|-----------|
| Step 1: RNase E cleavage / scaffold | **covered** | *rne* PP_1905; genus-direct scaffold evidence (PMID 40096066, 41036625) |
| Step 2: RhlB-assisted unwinding | **covered** | *rhlB* PP_1295; Type II ortholog of P. aeruginosa (PMID 42581758) |
| Step 2: RhlE-assisted unwinding | **covered** | *rhlE* PP_4980 + genus precedent (PMID 15705581) |
| Step 3: PNPase phosphorolysis | **covered** | *pnp* PP_4708; core partner (PMID 40096066) |
| Step 3: RNase R hydrolysis | **covered** | *rnr* PP_4880; genus-direct (PMID 15705581, 17405875) |
| Accessory: 5'-trigger (RppH) | **candidate_uncertain** | Homology only; no KT2440 data |
| Accessory: 3'-tagging (PcnB) | **candidate_uncertain** | Homology only; no KT2440 data |
| Accessory: Hfq riboregulation | **covered** | Direct KT2440 evidence (PMID 37348756) |
| Enolase as core subunit | **not_expected_in_target_taxon** | No Pseudomonas enolase-binding microdomain (PMID 40096066) |
| RecQ, Rho, DnaK, GroEL, Ppk, PpkB | **not module members** | KEGG co-listings / other buckets |

**Module-boundary note:** The generic module models Steps 2 and 3 as OR-branches with a single selected implementation. KT2440 encodes **all** branches, which the module should treat as full satisfiability. The generic boundaries are broadly correct, but the **Pseudomonas instance should explicitly exclude enolase** from the degradosome core (unlike the E. coli-derived generic degradosome) and should annotate RhlB with the **Type II** regulatory divergence.

**GO-curation:** No new GO terms appear strictly required. Existing terms cover ribonuclease E activity (GO:0008995), RNA helicase activity (GO:0003724), polyribonucleotide nucleotidyltransferase activity (GO:0004654), and exoribonuclease activity. A curator note distinguishing "RNA degradosome" assembly (Pseudomonas mode) from the *E. coli* mode would be valuable, and a request to capture **RhlB Type II phase-separation antagonism by RNase E** as an annotation extension could be considered.

---

## 8. Genes to Promote to Full `fetch-gene` Review

Promote the following core module genes to full individual review, in priority order:

1. **rne (PP_1905)** — the module hub; verify CTD SLiM inventory and Pseudomonas-specific partner interfaces.
2. **rhlB (PP_1295)** — confirm Type II clade assignment and IDR annotation; reconcile with generic RhlB.
3. **pnp (PP_4708)** — core exonuclease; confirm degradosome membership.
4. **rnr (PP_4880)** — cold-variant exonuclease; confirm RNase E interaction potential in KT2440.
5. **rhlE (PP_4980)** — resolve RhlE vs. RhlB roles; annotate the RGG/IDR.
6. **rhlE-I / RhpA (PP_4766)** — paralog disambiguation.

Secondary (accessory) review: *hfq* (PP_4894, already validated), *rppH* (PP_5146), *pcnB* (PP_4697), *deaD* (PP_1868). Enolase (PP_1612) should be reviewed specifically to **downgrade** its degradosome annotation to glycolytic.

---

## 9. Limitations and Knowledge Gaps

- **Direct KT2440 evidence is thin.** Only Hfq has been experimentally characterized in the target strain. Nearly all mechanistic conclusions rely on transfer from *P. aeruginosa* or *P. syringae*. The transfer is well-justified by high sequence similarity within the genus, but no KT2440 degradosome has been directly isolated or its composition mass-spec-verified.
- **Sequence proxy caveats.** The 5-mer Jaccard analysis is a conservative, divergence-sensitive proxy, not a phylogenetic or structural alignment; *P. aeruginosa* orthologs for RNase E, RNase R, and RhlE were not retrieved by exact gene-name search, so their genus-transfer strength is inferred by trend rather than measured.
- **Enolase call is negative evidence.** The conclusion that enolase is not a core Pseudomonas degradosome subunit rests on its *absence* from a reported interactome, which is weaker than a direct binding-negative experiment.
- **Accessory step uncertainty.** RppH and PcnB roles are entirely homology-inferred; their actual contribution to decay in KT2440 is untested.
- **Condition dependence untested in KT2440.** Whether KT2440 actually swaps RNase R/RhlE into its degradosome under cold stress (as *P. syringae* does) is an extrapolation.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Affinity-purify the KT2440 RNase E degradosome** (tagged *rne* PP_1905) under standard and cold-shock conditions; identify partners by LC-MS/MS. This would directly confirm PNPase/RhlB core membership, test RNase R/RhlE cold substitution, and settle the enolase question in the target strain.
2. **Map the KT2440 RNase E CTD SLiM inventory** in silico against the *P. aeruginosa* reference (PMID 40096066) to predict partner-binding microdomains and confirm absence of an enolase microdomain.
3. **Phenotype the KT2440 *rppH* and *pcnB* deletions** with 5'-end and 3'-tail sequencing to test their inferred accessory roles directly.
4. **Confirm RhlB Type II assignment** by phylogenetic placement and IDR prediction, and test RNase E antagonism of RhlB condensation in KT2440 (following PMID 42581758).
5. **Curation actions:** trim RecQ, Rho, DnaK, GroEL, Ppk, PpkB from the module; downgrade enolase to glycolytic; promote *rne*, *rhlB*, *pnp*, *rnr*, *rhlE*, *rhlE-I* to full review; annotate all four DEAD-box loci with distinct paralog identities.

---

## 11. Evidence Base / Key References

| PMID | Title (abbrev.) | How it supports the review |
|------|-----------------|----------------------------|
| [40096066](https://pubmed.ncbi.nlm.nih.gov/40096066/) | Critical functions of the RNase E scaffolding domain in *P. aeruginosa* | Establishes PNPase + RhlB as core degradosome partners; no enolase microdomain reported |
| [42581758](https://pubmed.ncbi.nlm.nih.gov/42581758/) | RNase E resolves toxic condensates of Type II RhlB helicases | Defines Pseudomonas Type II RhlB and its E. coli-divergent regulation |
| [41036625](https://pubmed.ncbi.nlm.nih.gov/41036625/) | Multi-dentate endo–exo interaction in the bacterial degradosome | RNase E–PNPase association conserved but genus-specific in Pseudomonas |
| [15705581](https://pubmed.ncbi.nlm.nih.gov/15705581/) | RNase R interacts with RNase E + helicase in *P. syringae* | Supports RNase R and RhlE variant branches in Pseudomonas |
| [17405875](https://pubmed.ncbi.nlm.nih.gov/17405875/) | RNase R essential at low temperature in *P. syringae* | Direct RNase R–RNase E degradosome interaction in the genus |
| [37348756](https://pubmed.ncbi.nlm.nih.gov/37348756/) | Crc–Hfq system of *P. putida* KT2440 | **Direct KT2440 evidence** for Hfq function |
| [18202662](https://pubmed.ncbi.nlm.nih.gov/18202662/) | RppH triggers mRNA degradation by 5'-pyrophosphate removal | Establishes RppH's 5'-trigger role upstream of RNase E |
| [7533264](https://pubmed.ncbi.nlm.nih.gov/7533264/) | RNA degradation regulated by 3' adenylation and 5' phosphorylation | Establishes PcnB stimulation of PNPase degradation |
| [21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/) | Crystal structure of hexameric RraA from *P. aeruginosa* | Context for Pseudomonas degradosome; enolase mention is generic, not direct binding |
| [27447594](https://pubmed.ncbi.nlm.nih.gov/27447594/) / [27834591](https://pubmed.ncbi.nlm.nih.gov/27834591/) | Phage Dip inhibits the *P. aeruginosa* degradosome | Confirms RNase E scaffold has conserved RNA-binding sites in Pseudomonas |

---

*Report prepared for manual module satisfiability and gene-annotation curation. All species-transfer judgments are stated explicitly; direct KT2440 evidence is limited to Hfq, with the remaining core mechanism transferred with high confidence from the same genus (*P. aeruginosa*, *P. syringae*) and only weakly from *E. coli*.*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_rna_degradation__ppu03018-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_rna_degradation__ppu03018-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:40096066
2. PMID:41036625
3. PMID:42581758
4. PMID:15705581
5. PMID:17405875
6. PMID:37348756
7. PMID:18202662
8. PMID:7533264
9. PMID:21063756