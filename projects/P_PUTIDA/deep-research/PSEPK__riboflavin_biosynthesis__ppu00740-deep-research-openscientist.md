---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T04:08:06.016804'
end_time: '2026-07-15T04:26:25.997139'
duration_seconds: 1099.98
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: De novo riboflavin biosynthesis and bacterial flavin cofactor activation
  module_summary: 'Species-neutral bacterial pathway for making the riboflavin ring
    de novo from GTP and ribulose 5-phosphate and then converting riboflavin to the
    active flavin cofactors FMN and FAD. The ring pathway has two converging branches:
    a GTP-derived pyrimidine branch made by GTP cyclohydrolase II and the RibD deaminase/reductase
    activities, and a ribulose-5-phosphate branch made by 3,4-dihydroxy-2-butanone
    4-phosphate synthase. These branches converge at lumazine synthase, followed by
    riboflavin synthase. In bacteria, riboflavin kinase and FMN adenylyltransferase
    are frequently combined in a bifunctional RibF/RibC-family enzyme, connecting
    vitamin B2 synthesis to FMN and FAD supply.'
  module_outline: "- De novo riboflavin biosynthesis\n  - 1. GTP-derived pyrimidine\
    \ branch\n  - GTP-derived pyrimidine branch\n    - 1. GTP cyclohydrolase II\n\
    \    - GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate\n   \
    \   - RibA/RibBA: GTP cyclohydrolase II (molecular player: RibA/RibBA GTP cyclohydrolase\
    \ II family; activity or role: GTP cyclohydrolase II activity)\n    - 2. RibD\
    \ deamination\n    - Pyrimidine deamination\n      - RibD: diaminohydroxyphosphoribosylaminopyrimidine\
    \ deaminase (molecular player: RibD riboflavin biosynthesis protein family; activity\
    \ or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase activity)\n \
    \   - 3. RibD reduction\n    - Pyrimidine side-chain reduction\n      - RibD:\
    \ 5-amino-6-(5-phosphoribosylamino)uracil reductase (molecular player: RibD riboflavin\
    \ biosynthesis protein family; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil\
    \ reductase activity)\n  - 2. Ribulose-5-phosphate donor branch\n  - 3,4-dihydroxy-2-butanone\
    \ 4-phosphate formation\n    - RibB/RibBA: 3,4-dihydroxy-2-butanone 4-phosphate\
    \ synthase (molecular player: RibB/RibBA DHBP synthase family; activity or role:\
    \ 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)\n  - 3. Lumazine assembly\n\
    \  - 6,7-dimethyl-8-ribityllumazine formation\n    - RibH: 6,7-dimethyl-8-ribityllumazine\
    \ synthase (molecular player: RibH lumazine synthase family; activity or role:\
    \ 6,7-dimethyl-8-ribityllumazine synthase activity)\n  - 4. Riboflavin formation\n\
    \  - Riboflavin synthase\n    - RibE/RibC: riboflavin synthase (molecular player:\
    \ RibE/RibC riboflavin synthase family; activity or role: riboflavin synthase\
    \ activity)\n  - 5. Flavin cofactor activation\n  - Riboflavin to FMN and FAD\n\
    \    - 1. riboflavin phosphorylation to FMN\n    - Riboflavin kinase\n      -\
    \ RibF/RFK: riboflavin kinase (molecular player: RibF/RFK riboflavin kinase family;\
    \ activity or role: riboflavin kinase activity)\n    - 2. FMN adenylylation to\
    \ FAD\n    - FMN adenylyltransferase\n      - RibF/FADS: FMN adenylyltransferase\
    \ (molecular player: RibF/FADS FMN adenylyltransferase family; activity or role:\
    \ FMN adenylyltransferase activity)"
  module_connections: '- GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5''-phosphate
    precedes Pyrimidine deamination

    - Pyrimidine deamination precedes Pyrimidine side-chain reduction

    - Pyrimidine side-chain reduction feeds into 6,7-dimethyl-8-ribityllumazine formation

    - 3,4-dihydroxy-2-butanone 4-phosphate formation feeds into 6,7-dimethyl-8-ribityllumazine
    formation

    - 6,7-dimethyl-8-ribityllumazine formation precedes Riboflavin synthase

    - Riboflavin synthase feeds into Riboflavin kinase

    - Riboflavin kinase precedes FMN adenylyltransferase'
  pathway_query: ppu00740
  pathway_id: ppu00740
  pathway_name: Riboflavin metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00740 with 14 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '15'
  candidate_genes: '- ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38)
    (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)

    - ribD: PP_0514 | Q88QH9 | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine
    deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil
    reductase (EC 1.1.1.193) (HTP reductase)] (EC 1.1.1.193; 3.5.4.26; primary bucket
    kegg:ppu00740)

    - ribE: PP_0515 | Q88QH8 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary
    bucket kegg:ppu00740)

    - ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - ribH: PP_0517 | Q88QH6 | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase)
    (LS) (Lumazine synthase) (EC 2.5.1.78) (EC 2.5.1.78; primary bucket kegg:ppu00740)

    - ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase
    II) (EC 3.5.4.25; primary bucket kegg:ppu00740)

    - ribB: PP_0530 | Q88QG4 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129;
    primary bucket kegg:ppu00627)

    - ribF: PP_0602 | Q88Q93 | Riboflavin biosynthesis protein [Includes: Riboflavin
    kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD
    pyrophosphorylase) (FAD synthase)] (EC 2.7.1.26; 2.7.7.2; primary bucket kegg:ppu00740)

    - bluB: PP_1674 | Q88MA0 | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79)
    (EC 1.13.11.79; primary bucket kegg:ppu00740)

    - msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase)
    (EC 1.5.1.38; primary bucket kegg:ppu00740)

    - ribC: PP_2916 | Q88IT3 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary
    bucket kegg:ppu00740)

    - ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP
    synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)

    - nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose
    diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase)
    (EC 3.6.1.13; primary bucket kegg:ppu00740)

    - had: PP_5231 | Q88CF0 | (S)-2-haloacid dehalogenase (EC 3.8.1.-) (EC 3.8.1.-;
    primary bucket kegg:ppu00740)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

De novo riboflavin biosynthesis and bacterial flavin cofactor activation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00740
- Resolved ID: ppu00740
- Resolved name: Riboflavin metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00740 with 14 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 15

- ssuE: PP_0236 | Q88R97 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ribD: PP_0514 | Q88QH9 | Riboflavin biosynthesis protein RibD [Includes: Diaminohydroxyphosphoribosylaminopyrimidine deaminase (DRAP deaminase) (EC 3.5.4.26) (Riboflavin-specific deaminase); 5-amino-6-(5-phosphoribosylamino)uracil reductase (EC 1.1.1.193) (HTP reductase)] (EC 1.1.1.193; 3.5.4.26; primary bucket kegg:ppu00740)
- ribE: PP_0515 | Q88QH8 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary bucket kegg:ppu00740)
- ribAB-I: PP_0516 | Q88QH7 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ribH: PP_0517 | Q88QH6 | 6,7-dimethyl-8-ribityllumazine synthase (DMRL synthase) (LS) (Lumazine synthase) (EC 2.5.1.78) (EC 2.5.1.78; primary bucket kegg:ppu00740)
- ribA: PP_0522 | Q88QH1 | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) (EC 3.5.4.25; primary bucket kegg:ppu00740)
- ribB: PP_0530 | Q88QG4 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- ribF: PP_0602 | Q88Q93 | Riboflavin biosynthesis protein [Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD pyrophosphorylase) (FAD synthase)] (EC 2.7.1.26; 2.7.7.2; primary bucket kegg:ppu00740)
- bluB: PP_1674 | Q88MA0 | 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79) (EC 1.13.11.79; primary bucket kegg:ppu00740)
- msuE: PP_2764 | Q88J85 | FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (EC 1.5.1.38; primary bucket kegg:ppu00740)
- ribC: PP_2916 | Q88IT3 | Riboflavin synthase (EC 2.5.1.9) (EC 2.5.1.9; primary bucket kegg:ppu00740)
- ribAB-II: PP_3813 | Q88GB1 | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) (EC 4.1.99.12; primary bucket kegg:ppu00740)
- nudF: PP_4919 | Q88DA8 | ADP-ribose pyrophosphatase (EC 3.6.1.13) (ADP-ribose diphosphatase) (ADP-ribose phosphohydrolase) (Adenosine diphosphoribose pyrophosphatase) (EC 3.6.1.13; primary bucket kegg:ppu00740)
- had: PP_5231 | Q88CF0 | (S)-2-haloacid dehalogenase (EC 3.8.1.-) (EC 3.8.1.-; primary bucket kegg:ppu00740)

## Generic Module Context

### Working Scope

Species-neutral bacterial pathway for making the riboflavin ring de novo from GTP and ribulose 5-phosphate and then converting riboflavin to the active flavin cofactors FMN and FAD. The ring pathway has two converging branches: a GTP-derived pyrimidine branch made by GTP cyclohydrolase II and the RibD deaminase/reductase activities, and a ribulose-5-phosphate branch made by 3,4-dihydroxy-2-butanone 4-phosphate synthase. These branches converge at lumazine synthase, followed by riboflavin synthase. In bacteria, riboflavin kinase and FMN adenylyltransferase are frequently combined in a bifunctional RibF/RibC-family enzyme, connecting vitamin B2 synthesis to FMN and FAD supply.

### Provisional Biological Outline

- De novo riboflavin biosynthesis
  - 1. GTP-derived pyrimidine branch
  - GTP-derived pyrimidine branch
    - 1. GTP cyclohydrolase II
    - GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate
      - RibA/RibBA: GTP cyclohydrolase II (molecular player: RibA/RibBA GTP cyclohydrolase II family; activity or role: GTP cyclohydrolase II activity)
    - 2. RibD deamination
    - Pyrimidine deamination
      - RibD: diaminohydroxyphosphoribosylaminopyrimidine deaminase (molecular player: RibD riboflavin biosynthesis protein family; activity or role: diaminohydroxyphosphoribosylaminopyrimidine deaminase activity)
    - 3. RibD reduction
    - Pyrimidine side-chain reduction
      - RibD: 5-amino-6-(5-phosphoribosylamino)uracil reductase (molecular player: RibD riboflavin biosynthesis protein family; activity or role: 5-amino-6-(5-phosphoribosylamino)uracil reductase activity)
  - 2. Ribulose-5-phosphate donor branch
  - 3,4-dihydroxy-2-butanone 4-phosphate formation
    - RibB/RibBA: 3,4-dihydroxy-2-butanone 4-phosphate synthase (molecular player: RibB/RibBA DHBP synthase family; activity or role: 3,4-dihydroxy-2-butanone-4-phosphate synthase activity)
  - 3. Lumazine assembly
  - 6,7-dimethyl-8-ribityllumazine formation
    - RibH: 6,7-dimethyl-8-ribityllumazine synthase (molecular player: RibH lumazine synthase family; activity or role: 6,7-dimethyl-8-ribityllumazine synthase activity)
  - 4. Riboflavin formation
  - Riboflavin synthase
    - RibE/RibC: riboflavin synthase (molecular player: RibE/RibC riboflavin synthase family; activity or role: riboflavin synthase activity)
  - 5. Flavin cofactor activation
  - Riboflavin to FMN and FAD
    - 1. riboflavin phosphorylation to FMN
    - Riboflavin kinase
      - RibF/RFK: riboflavin kinase (molecular player: RibF/RFK riboflavin kinase family; activity or role: riboflavin kinase activity)
    - 2. FMN adenylylation to FAD
    - FMN adenylyltransferase
      - RibF/FADS: FMN adenylyltransferase (molecular player: RibF/FADS FMN adenylyltransferase family; activity or role: FMN adenylyltransferase activity)

### Known Relationships Among Steps

- GTP to 2,5-diamino-6-ribosylamino-4(3H)-pyrimidinone 5'-phosphate precedes Pyrimidine deamination
- Pyrimidine deamination precedes Pyrimidine side-chain reduction
- Pyrimidine side-chain reduction feeds into 6,7-dimethyl-8-ribityllumazine formation
- 3,4-dihydroxy-2-butanone 4-phosphate formation feeds into 6,7-dimethyl-8-ribityllumazine formation
- 6,7-dimethyl-8-ribityllumazine formation precedes Riboflavin synthase
- Riboflavin synthase feeds into Riboflavin kinase
- Riboflavin kinase precedes FMN adenylyltransferase

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

# Species-Aware Review: De novo Riboflavin Biosynthesis and Flavin Cofactor Activation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00740 "Riboflavin metabolism"; module area cofactors_vitamins_redox
**Module scope reviewed:** de novo riboflavin ring synthesis (GTP + ribulose-5-P → riboflavin) and flavin cofactor activation (riboflavin → FMN → FAD)

---

## 1. Executive summary

The de novo riboflavin biosynthesis + FMN/FAD activation module is **fully satisfiable** in *P. putida* KT2440. Every expected catalytic step maps to at least one candidate gene, and the core biosynthetic genes are organized in a recognizable chromosomal cluster (PP_0514–PP_0517) with dispersed additional copies. Confidence is high on architectural/homology grounds; however, **almost all of the evidence is homology-based** (UniProt/InterPro), not direct biochemistry in KT2440 itself.

The 15-gene candidate list is a mixture of (a) **7 genuine pathway enzymes**, (b) **2–3 real paralogs** that create redundancy but also naming/EC ambiguity, and (c) **~6 flavin-associated genes that are KEGG-map co-occurrence artifacts** (over-propagated into ppu00740). The most important curation actions are: exclude the peripheral flavin-utilization genes from the biosynthesis module; reclassify the two "ribAB" genes (PP_0516, PP_3813) as **RibB/RibBX** — active-site analysis shows their C-terminal GTP-cyclohydrolase-II-fold domain has lost the catalytic zinc-cysteine cluster and is catalytically dead, so EC 3.5.4.25 and the "ribAB" symbol should be withheld and GTP-CHII treated as a single-copy step on RibA (PP_0522); and treat the two riboflavin-synthase paralogs as genuine duplicates rather than errors.

---

## 2. Target-organism pathway definition

**Included process:** conversion of GTP and D-ribulose 5-phosphate into the riboflavin isoalloxazine ring, then phosphorylation to FMN and adenylylation to FAD. Two converging branches (GTP-derived pyrimidine branch via GTP cyclohydrolase II + RibD; ribulose-5-P branch via DHBP synthase) meet at lumazine synthase (RibH), followed by riboflavin synthase (RibE), then the bifunctional RibF (riboflavin kinase + FMN adenylyltransferase).

**Neighboring maps/processes to keep separate (do NOT fold into this module):**
- **Flavin-dependent monooxygenase electron supply** — NAD(P)H:FMN reductases (SsuE, MsuE) that feed reduced FMN to sulfonate monooxygenases (sulfur assimilation / *ssu*, *msu* systems).
- **Ubiquinone/aromatic decarboxylation** — UbiX prenylated-FMN (prFMN) synthesis for UbiD-type decarboxylases (KEGG ppu00627); prFMN is a *specialized flavin derivative*, not FMN/FAD cofactor activation.
- **Cobalamin (B12) biosynthesis** — BluB (5,6-dimethylbenzimidazole synthase) *consumes* reduced FMN; belongs to the B12 lower-ligand pathway.
- **Nucleotide/Nudix hydrolysis** (NudF) and **haloacid dehalogenation** (Had) — not flavin metabolism at all.

**Alternate names / database definitions:** KEGG ppu00740 "Riboflavin metabolism" is broader than the biosynthesis-only module and intentionally sweeps in flavin-consuming/producing enzymes. MetaCyc/BioCyc split this into "flavin biosynthesis" + "FAD biosynthesis" sub-pathways. Gene-symbol nomenclature is inconsistent across databases: *ribC* and *ribE* both denote riboflavin synthase here, whereas in *E. coli* "ribC" historically denotes the RibF/FAD-synthetase — a known source of curation confusion.

---

## 3. Expected step model and satisfiability

| # | Step (activity, EC) | Expected family | KT2440 gene(s) | Status |
|---|--------------------|-----------------|----------------|--------|
| 1 | GTP cyclohydrolase II (EC 3.5.4.25) | RibA / RibBA | **PP_0522 (ribA, reviewed)** only; PP_0516/PP_3813 C-domains are catalytically dead (RibBX) | **covered** (single copy) |
| 2 | DRAP deaminase (EC 3.5.4.26) | RibD N-domain | **PP_0514 (ribD)** | **covered** |
| 3 | HTP reductase (EC 1.1.1.193) | RibD C-domain | **PP_0514 (ribD)** | **covered** |
| 4 | DHBP synthase (EC 4.1.99.12) | RibB / RibBA | **PP_0530 (ribB, reviewed)**; DHBP domain of PP_0516, PP_3813 | **covered** |
| 5 | Lumazine synthase (EC 2.5.1.78) | RibH | **PP_0517 (ribH, reviewed)** | **covered** |
| 6 | Riboflavin synthase (EC 2.5.1.9) | RibE / RibC | **PP_0515 (ribE, operonic)**; paralog PP_2916 (ribC) | **covered** |
| 7 | Riboflavin kinase (EC 2.7.1.26) | RibF N-term | **PP_0602 (ribF)** | **covered** |
| 8 | FMN adenylyltransferase (EC 2.7.7.2) | RibF C-term | **PP_0602 (ribF)** | **covered** |

**All eight catalytic activities are encoded.** The bifunctional RibF (PP_0602, 316 aa) performs both activation steps 7+8, as is typical for bacteria (PMID 22892871). RibD (PP_0514, 378 aa) is genuinely bifunctional (deaminase + reductase domains). No step is a gap; no step is "not expected."

---

## 4. Candidate genes and evidence

### High-confidence pathway enzymes (7)
- **PP_0514 ribD (Q88QH9, 378 aa, TrEMBL).** Bifunctional deaminase/reductase (EC 3.5.4.26 + 1.1.1.193). Operonic. Covers steps 2–3. Evidence: homology + domain architecture.
- **PP_0515 ribE (Q88QH8, 221 aa, TrEMBL).** Riboflavin synthase (EC 2.5.1.9); InterPro: paired Lumazine-binding + riboflavin-synthase β-barrel domains. Operonic → canonical copy. Covers step 6.
- **PP_0517 ribH (Q88QH6, 158 aa, reviewed).** Lumazine synthase (EC 2.5.1.78). Covers step 5. Highest-quality annotation (Swiss-Prot).
- **PP_0522 ribA (Q88QH1, 205 aa, reviewed).** Monofunctional GTP cyclohydrolase II (EC 3.5.4.25). Covers step 1. Swiss-Prot.
- **PP_0530 ribB (Q88QG4, 216 aa, reviewed).** Monofunctional DHBP synthase (EC 4.1.99.12). Covers step 4. Swiss-Prot.
- **PP_0602 ribF (Q88Q93, 316 aa, TrEMBL).** Bifunctional riboflavin kinase / FMN adenylyltransferase (EC 2.7.1.26 + 2.7.7.2). Covers steps 7–8.
- *Note:* the three most central biosynthetic genes (ribD, ribE, ribF) are **unreviewed TrEMBL**, whereas peripheral FMN reductases are reviewed — an inverted evidence-quality pattern worth flagging to curators.

### Paralogs / ambiguity (3)
- **PP_2916 ribC (Q88IT3, 209 aa, TrEMBL).** Second riboflavin synthase; InterPro confirms genuine two-domain riboflavin-synthase fold. **Genuine paralog, not an error.** Ectopic (not in the rib cluster). Which copy is physiologically primary is unresolved.
- **PP_0516 ribAB-I (Q88QH7, 369 aa, TrEMBL)** and **PP_3813 ribAB-II (Q88GB1, 373 aa, TrEMBL).** Both are two-domain proteins: an N-terminal DHBP-synthase RibB domain plus a C-terminal domain that InterPro assigns to the GTP-cyclohydrolase-II superfamily (fold), so the local metadata symbol "ribAB" implies bifunctionality. **Direct active-site inspection refutes this:** the reviewed monofunctional RibA (PP_0522) retains the intact GTP-CHII catalytic core `SECLTGD...CDCGSQ` (the ECLTGD catalytic motif + the three-cysteine CDCG zinc cluster), whereas the C-terminal domains of PP_0516 and PP_3813 contain **neither** the zinc-cysteine cluster (no CxC[G/S]) **nor** the EC..GD catalytic motif, and align only trivially to RibA (Smith-Waterman windows of just 15–33 residues). Loss of the catalytic zinc-coordinating cysteines abolishes GTP cyclohydrolase II activity — the hallmark **RibBX** phenotype (PMID 24097946). **Conclusion:** these are DHBP-synthase-active RibB/RibBX proteins with a catalytically dead C-domain. UniProt's "DHBP synthase only" (EC 4.1.99.12) recommended name is **correct**; EC 3.5.4.25 and the "ribAB" symbol should NOT be assigned. Step 1 rests solely on the standalone reviewed RibA (PP_0522). (Strong sequence-based inference, not experimental proof.)

### Likely over-propagated / out-of-scope (5)
- **PP_0236 ssuE (Q88R97, reviewed)** and **PP_2764 msuE (Q88J85, reviewed)** — NAD(P)H:FMN reductases (EC 1.5.1.38) for sulfonate monooxygenase systems. Flavin *utilization*, not synthesis.
- **PP_0548 ubiX (Q88QE6)** — flavin prenyltransferase making prFMN for UbiD decarboxylases (EC 2.5.1.129; primary bucket ppu00627) (PMID 29551348, 31072498). Distinct specialized cofactor.
- **PP_1674 bluB (Q88MA0)** — 5,6-dimethylbenzimidazole synthase (EC 1.13.11.79); B12 lower-ligand biosynthesis, consumes FMNH₂.
- **PP_4919 nudF (Q88DA8)** — Nudix ADP-ribose pyrophosphatase (EC 3.6.1.13).
- **PP_5231 had (Q88CF0)** — (S)-2-haloacid dehalogenase (EC 3.8.1.-); not flavin-related.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps.** Every de novo + activation step is encoded.
- **RibBX correction** (curation fix): do NOT add EC 3.5.4.25 to PP_0516/PP_3813 and do NOT use the "ribAB" symbol — their C-terminal GTP-CHII-fold domain lacks the catalytic zinc-cysteine cluster and is catalytically dead (RibBX). Rename toward *ribB*/*ribBX*. GTP cyclohydrolase II is a **single-copy** step carried by RibA (PP_0522).
- **Over-annotation into ppu00740:** ssuE, msuE, ubiX, bluB, nudF, had are present only because they consume/produce flavins or share EC-class fragments. They inflate the apparent gene count (15) relative to the ~7–9 true module members.
- **Nomenclature ambiguity:** ribC (PP_2916) vs ribE (PP_0515) both = riboflavin synthase; distinct from the *E. coli* ribC=RibF convention.
- **Evidence-quality inversion:** core enzymes are TrEMBL; peripheral enzymes are Swiss-Prot.

---

## 6. Module and GO-curation recommendations

**Module step status:**
- Steps 1–8: **covered.**
- Step 1 (GTP-CHII): **covered as a single copy by PP_0522**; PP_0516/PP_3813 do NOT contribute (RibBX, catalytically dead C-domain) — mark their EC 3.5.4.25 claim as **module_needs_revision / reject**.
- Step 6 (riboflavin synthase): covered by PP_0515; PP_2916 = **covered (redundant paralog)**.

**Module membership edits:**
- **Remove/downgrade** ssuE, msuE, ubiX, bluB, nudF, had from the de-novo-biosynthesis module (mark `not_expected_in_target_taxon`/out-of-scope for this module; they belong to sulfur assimilation, ubiquinone/aromatic decarboxylation, B12, and nucleotide/dehalogenase modules respectively).
- **module_needs_revision:** generic module lists GTP-CHII only under "RibA/RibBA" — for KT2440 the canonical activity is the *standalone* RibA (PP_0522); the RibBA copies are lineage-specific extras of uncertain catalytic status.

**GO / annotation requests:**
- Consider GO annotation `GO:0003935` (GTP cyclohydrolase II) for PP_0516/PP_3813 only after active-site confirmation.
- No new GO terms appear necessary; existing terms cover all activities.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0516 (ribAB-I)** and **PP_3813 (ribAB-II)** — sequence analysis indicates degenerate **RibBX** (dead C-terminal GTP-CHII domain, EC 3.5.4.25 absent); confirm experimentally and correct EC/gene symbol to *ribB*/*ribBX*.
2. **PP_2916 (ribC)** — establish that it is a functional second riboflavin synthase and its physiological role vs operonic PP_0515.
3. **PP_0602 (ribF)** — TrEMBL; central bifunctional flavin-activation enzyme deserves reviewed-level curation.
4. (Lower priority) **PP_0514 ribD** and **PP_0515 ribE** — TrEMBL core genes worth Swiss-Prot-level review.

---

## 8. Key references

- Brutinel ED, Dean AM, Gralnick JA. *Description of a riboflavin biosynthetic gene variant prevalent in the phylum Proteobacteria.* J Bacteriol. 2013. **PMID 24097946.** (ribBA→ribBX misannotation; ~40% of Proteobacterial ribBA lack GTP-CHII activity.)
- Fassbinder F, Kist M, Bereswill S. *Structural and functional analysis of the riboflavin synthesis genes... from Helicobacter pylori.* FEMS Microbiol Lett. 2000. **PMID 11024263.** (Why a standalone ribA is retained alongside ribBA.)
- Serrano A, et al. *Key residues at the riboflavin kinase catalytic site of the bifunctional riboflavin kinase/FMN adenylyltransferase.* 2013. **PMID 22892871.** (Single bifunctional RibF/FADS converts riboflavin→FMN→FAD.)
- Wang Z, Khusnutdinova AN, et al. *Biosynthesis and Activity of Prenylated FMN Cofactors.* 2018. **PMID 29551348**; Khusnutdinova AN, et al. *Prenylated FMN: Biosynthesis, purification, and Fdc1 activation.* 2019. **PMID 31072498.** (UbiX makes prFMN for UbiD — out of scope for FMN/FAD activation.)
- Yurgel SN, et al. *Sinorhizobium meliloti flavin secretion... bifunctional RibBA protein.* 2014. **PMID 24405035.** (RibBA duplication / flavin secretion context.)
- UniProt/InterPro (proteome UP000000556) — accessions Q88QH9, Q88QH8, Q88QH7, Q88QH6, Q88QH1, Q88QG4, Q88Q93, Q88IT3, Q88GB1, Q88QE6, Q88R97, Q88J85, Q88MA0, Q88DA8, Q88CF0.

---

### Evidence basis and limitations
All conclusions are **homology/architecture-based** (UniProt recommended names, InterPro domains, sequence lengths, operon context). **No KT2440-specific biochemical or genetic (knockout/complementation) data** were located for the rib genes; transfer from related bacteria (*E. coli*, *H. pylori*, *S. oneidensis*, *S. meliloti*) is strong for pathway logic but does not confirm the catalytic status of the KT2440 ribBA/ribBX and ribC paralogs. Definitive resolution requires: (i) active-site residue analysis or enzyme assays for PP_0516/PP_3813 GTP-CHII, (ii) complementation/expression tests for PP_2916, and (iii) upgrading core TrEMBL entries to reviewed status.


## Artifacts

- [OpenScientist final report](PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-openscientist_artifacts/final_report.pdf)