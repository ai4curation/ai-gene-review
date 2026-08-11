---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T11:36:03.111646'
end_time: '2026-08-08T12:03:53.204040'
duration_seconds: 1670.09
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: kdo_biosynthesis
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00541
  pathway_id: ppu00541
  pathway_name: Biosynthesis of various nucleotide sugars
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00541 with 11 primary genes; module
    area: nucleotide_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '26'
  candidate_genes: '- gmhB: PP_0059 | Q88RS0 | D-glycero-beta-D-manno-heptose-1,7-bisphosphate
    7-phosphatase (EC 3.1.3.82) (D,D-heptose 1,7-bisphosphate phosphatase) (HBP phosphatase)
    (EC 3.1.3.82; primary bucket kegg:ppu00541)

    - rmlC: PP_0265 | Q88R69 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13)
    (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket
    kegg:ppu00523)

    - PP_0500: PP_0500 | Q88QJ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133)
    (EC 1.1.1.133; primary bucket kegg:ppu00523)

    - kdsC: PP_0956 | Q88P96 | 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase
    KdsC (EC 3.1.3.45) (KDO 8-P phosphatase) (EC 3.1.3.45; primary bucket kegg:ppu00541)

    - kdsD: PP_0957 | Q88P95 | Arabinose 5-phosphate isomerase (API) (EC 5.3.1.13)
    (EC 5.3.1.13; primary bucket kegg:ppu00541)

    - algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate
    isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate
    guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP)
    (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary
    bucket kegg:ppu00051)

    - gmhA: PP_1323 | Q88N89 | Phosphoheptose isomerase (EC 5.3.1.28) (Sedoheptulose
    7-phosphate isomerase) (EC 5.3.1.28; primary bucket kegg:ppu00541)

    - kdsA1: PP_1611 | Q88MG0 | 2-dehydro-3-deoxyphosphooctonate aldolase 1 (EC 2.5.1.55)
    (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase 1) (KDO-8-phosphate synthase
    1) (KDO 8-P synthase 1) (KDOPS 1) (Phospho-2-dehydro-3-deoxyoctonate aldolase
    1) (EC 2.5.1.55; primary bucket kegg:ppu00541)

    - PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13)
    (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)

    - rfbC: PP_1782 | Q88LZ4 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13)
    (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket
    kegg:ppu00523)

    - rfbA: PP_1783 | Q88LZ3 | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24)
    (EC 2.7.7.24; primary bucket kegg:ppu00525)

    - rfbD: PP_1784 | Q88LZ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (EC
    1.1.1.133; primary bucket kegg:ppu00523)

    - rffG: PP_1785 | Q88LZ1 | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) (EC 4.2.1.46;
    primary bucket kegg:ppu00525)

    - gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose
    dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)

    - rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)

    - wbpV: PP_1803 | Q88LX4 | UDP-sugar epimerase (primary bucket kegg:ppu00541)

    - wbpM: PP_1805 | Q88LX2 | Polysaccharide biosynthesis protein (primary bucket
    kegg:ppu00552)

    - PP_1806: PP_1806 | Q88LX1 | Arabinose 5-phosphate isomerase (API) (EC 5.3.1.13)
    (EC 5.3.1.13; primary bucket kegg:ppu00541)

    - kdsA2: PP_1807 | Q88LX0 | 2-dehydro-3-deoxyphosphooctonate aldolase 2 (EC 2.5.1.55)
    (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase 2) (KDO-8-phosphate synthase
    2) (KDO 8-P synthase 2) (KDOPS 2) (Phospho-2-dehydro-3-deoxyoctonate aldolase
    2) (EC 2.5.1.55; primary bucket kegg:ppu00541)

    - rffE: PP_1811 | Q88LW6 | UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) (EC
    5.1.3.14; primary bucket kegg:ppu00520)

    - kdsB: PP_1902 | Q88LM7 | 3-deoxy-manno-octulosonate cytidylyltransferase (EC
    2.7.7.38) (CMP-2-keto-3-deoxyoctulosonic acid synthase) (CKS) (CMP-KDO synthase)
    (EC 2.7.7.38; primary bucket kegg:ppu00541)

    - udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22;
    primary bucket kegg:ppu00040)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

    - hldE: PP_4934 | Q88D93 | Bifunctional protein HldE [Includes: D-beta-D-heptose
    7-phosphate kinase (EC 2.7.1.167) (D-beta-D-heptose 7-phosphotransferase) (D-glycero-beta-D-manno-heptose-7-phosphate
    kinase); D-beta-D-heptose 1-phosphate adenylyltransferase (EC 2.7.7.70) (D-glycero-beta-D-manno-heptose
    1-phosphate adenylyltransferase)] (EC 2.7.1.167; 2.7.7.70; primary bucket kegg:ppu00541)

    - PP_5212: PP_5212 | Q88CG9 | Oxidoreductase, iron-sulfur-binding (primary bucket
    kegg:ppu00541)

    - glmU: PP_5411 | Q88BX6 | Bifunctional protein GlmU [Includes: UDP-N-acetylglucosamine
    pyrophosphorylase (EC 2.7.7.23) (N-acetylglucosamine-1-phosphate uridyltransferase);
    Glucosamine-1-phosphate N-acetyltransferase (EC 2.3.1.157)] (EC 2.3.1.157; 2.7.7.23;
    primary bucket kegg:ppu00520)'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__kdo-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__kdo-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

kdo_biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00541
- Resolved ID: ppu00541
- Resolved name: Biosynthesis of various nucleotide sugars
- Source: KEGG

Resolved local bucket kegg:ppu00541 with 11 primary genes; module area: nucleotide_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 26

- gmhB: PP_0059 | Q88RS0 | D-glycero-beta-D-manno-heptose-1,7-bisphosphate 7-phosphatase (EC 3.1.3.82) (D,D-heptose 1,7-bisphosphate phosphatase) (HBP phosphatase) (EC 3.1.3.82; primary bucket kegg:ppu00541)
- rmlC: PP_0265 | Q88R69 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket kegg:ppu00523)
- PP_0500: PP_0500 | Q88QJ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (EC 1.1.1.133; primary bucket kegg:ppu00523)
- kdsC: PP_0956 | Q88P96 | 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC (EC 3.1.3.45) (KDO 8-P phosphatase) (EC 3.1.3.45; primary bucket kegg:ppu00541)
- kdsD: PP_0957 | Q88P95 | Arabinose 5-phosphate isomerase (API) (EC 5.3.1.13) (EC 5.3.1.13; primary bucket kegg:ppu00541)
- algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP) (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- gmhA: PP_1323 | Q88N89 | Phosphoheptose isomerase (EC 5.3.1.28) (Sedoheptulose 7-phosphate isomerase) (EC 5.3.1.28; primary bucket kegg:ppu00541)
- kdsA1: PP_1611 | Q88MG0 | 2-dehydro-3-deoxyphosphooctonate aldolase 1 (EC 2.5.1.55) (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase 1) (KDO-8-phosphate synthase 1) (KDO 8-P synthase 1) (KDOPS 1) (Phospho-2-dehydro-3-deoxyoctonate aldolase 1) (EC 2.5.1.55; primary bucket kegg:ppu00541)
- PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- rfbC: PP_1782 | Q88LZ4 | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) (EC 5.1.3.13; primary bucket kegg:ppu00523)
- rfbA: PP_1783 | Q88LZ3 | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) (EC 2.7.7.24; primary bucket kegg:ppu00525)
- rfbD: PP_1784 | Q88LZ2 | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (EC 1.1.1.133; primary bucket kegg:ppu00523)
- rffG: PP_1785 | Q88LZ1 | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) (EC 4.2.1.46; primary bucket kegg:ppu00525)
- gmd: PP_1799 | Q88LX8 | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase) (EC 4.2.1.47; primary bucket kegg:ppu00051)
- rmd: PP_1800 | Q88LX7 | Oxidoreductase Rmd (primary bucket kegg:ppu00051)
- wbpV: PP_1803 | Q88LX4 | UDP-sugar epimerase (primary bucket kegg:ppu00541)
- wbpM: PP_1805 | Q88LX2 | Polysaccharide biosynthesis protein (primary bucket kegg:ppu00552)
- PP_1806: PP_1806 | Q88LX1 | Arabinose 5-phosphate isomerase (API) (EC 5.3.1.13) (EC 5.3.1.13; primary bucket kegg:ppu00541)
- kdsA2: PP_1807 | Q88LX0 | 2-dehydro-3-deoxyphosphooctonate aldolase 2 (EC 2.5.1.55) (3-deoxy-D-manno-octulosonic acid 8-phosphate synthase 2) (KDO-8-phosphate synthase 2) (KDO 8-P synthase 2) (KDOPS 2) (Phospho-2-dehydro-3-deoxyoctonate aldolase 2) (EC 2.5.1.55; primary bucket kegg:ppu00541)
- rffE: PP_1811 | Q88LW6 | UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) (EC 5.1.3.14; primary bucket kegg:ppu00520)
- kdsB: PP_1902 | Q88LM7 | 3-deoxy-manno-octulosonate cytidylyltransferase (EC 2.7.7.38) (CMP-2-keto-3-deoxyoctulosonic acid synthase) (CKS) (CMP-KDO synthase) (EC 2.7.7.38; primary bucket kegg:ppu00541)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- hldE: PP_4934 | Q88D93 | Bifunctional protein HldE [Includes: D-beta-D-heptose 7-phosphate kinase (EC 2.7.1.167) (D-beta-D-heptose 7-phosphotransferase) (D-glycero-beta-D-manno-heptose-7-phosphate kinase); D-beta-D-heptose 1-phosphate adenylyltransferase (EC 2.7.7.70) (D-glycero-beta-D-manno-heptose 1-phosphate adenylyltransferase)] (EC 2.7.1.167; 2.7.7.70; primary bucket kegg:ppu00541)
- PP_5212: PP_5212 | Q88CG9 | Oxidoreductase, iron-sulfur-binding (primary bucket kegg:ppu00541)
- glmU: PP_5411 | Q88BX6 | Bifunctional protein GlmU [Includes: UDP-N-acetylglucosamine pyrophosphorylase (EC 2.7.7.23) (N-acetylglucosamine-1-phosphate uridyltransferase); Glucosamine-1-phosphate N-acetyltransferase (EC 2.3.1.157)] (EC 2.3.1.157; 2.7.7.23; primary bucket kegg:ppu00520)

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

# Module/Pathway/Taxon Review: KDO Biosynthesis in *Pseudomonas putida* KT2440

**Review topic:** `kdo_biosynthesis` (KEGG module M00063; CMP-KDO biosynthesis)
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Commissioned bucket:** KEGG `ppu00541` — "Biosynthesis of various nucleotide sugars"
**Module area:** nucleotide_metabolism

---

## 1. Executive Summary

The KDO (3-deoxy-D-*manno*-octulosonate) biosynthesis module is **fully satisfiable** in *Pseudomonas putida* KT2440. The biologically correct scope for this review is **KEGG module M00063** (D-ribulose-5-phosphate → CMP-KDO), *not* the broad umbrella map `ppu00541` ("Biosynthesis of various nucleotide sugars") into which the candidate list was drawn. All four committed enzymatic steps of the KDO pathway are encoded in the KT2440 genome by unambiguous candidate genes, and the biochemistry — production of the activated sugar CMP-KDO that is transferred onto lipid A to form the essential inner core of lipopolysaccharide (LPS) — is conserved and essential in Gram-negative bacteria.

The central curation problem in this brief is **over-propagation**. The commissioned bucket `ppu00541` lists 26 candidate genes, but only **6** are true KDO-pathway genes: `kdsD`/PP_0957 and a second arabinose-5-phosphate isomerase PP_1806 (step 1), `kdsA1`/PP_1611 and its paralog `kdsA2`/PP_1807 (step 2), `kdsC`/PP_0956 (step 3), and `kdsB`/PP_1902 (step 4). The remaining ~20 candidates belong to biochemically distinct nucleotide-sugar modules (dTDP-L-rhamnose, GDP-mannose/GDP-fucose, UDP-GlcNAc, UDP-glucose/UDP-glucuronate) or to the neighboring but separate ADP-L-*glycero*-D-*manno*-heptose module (M00064: `gmhA`, `gmhB`, `hldE`). These should be reassigned to their proper modules and excluded from the KDO satisfiability assessment. The KDO glycosyltransferase WaaA/KdtA (PP_4928) that consumes CMP-KDO sits just outside the biosynthetic module boundary and belongs to LPS core assembly.

A notable lineage feature is a **two-cluster paralog architecture**: a dispersed set of housekeeping core-LPS genes (`kdsD`, `kdsA1`, `kdsC`, `kdsB`) versus a second arabinose-5-P isomerase (PP_1806) and KDO-8-P synthase (`kdsA2`/PP_1807) embedded adjacently inside the O-antigen/*wbp* biosynthesis cluster. Sequence analysis shows both KdsA paralogs are genuine, near-equivalent KDO-8-P synthases (~71% mutual identity; ~71–73% to *E. coli* KdsA), whereas the two APIs are divergent — PP_0957 is the clear housekeeping ortholog (57% to *E. coli* KdsD) while PP_1806 is a divergent second copy (47% to KdsD, 48% to its own paralog). All six KDO proteins in KT2440 are homology-only annotations (UniProt evidence level PE=3); none has been experimentally characterized in this strain, so all conclusions rest on strong ortholog transfer plus KT2440-specific sequence and genomic-context analysis. Recommended curation: mark all four module steps **covered**; flag PP_1806 as **candidate_uncertain**; promote the single-copy essential `kdsB` and the ambiguous PP_1806 to full `fetch-gene` review.

---

## 2. Target-Organism Pathway Definition

### What the module is

KDO biosynthesis (module M00063) is the four-step cytoplasmic route that converts a pentose-phosphate-pathway intermediate into the activated sugar nucleotide **CMP-KDO**:

```
D-ribulose 5-phosphate
      │  (1) arabinose-5-phosphate isomerase   EC 5.3.1.13   KdsD / API
      ▼
D-arabinose 5-phosphate
      │  (2) KDO-8-phosphate synthase           EC 2.5.1.55   KdsA  (+ PEP)
      ▼
KDO 8-phosphate
      │  (3) KDO-8-phosphate phosphatase        EC 3.1.3.45   KdsC
      ▼
KDO (3-deoxy-D-manno-octulosonate)
      │  (4) CMP-KDO synthetase                 EC 2.7.7.38   KdsB  (+ CTP)
      ▼
CMP-KDO  ──►  (WaaA/KdtA, EC 2.4.99.12/13 — OUTSIDE module) ──► (KDO)₂-lipid A
```

The product CMP-KDO is the sugar donor used by the KDO transferase WaaA (KdtA) to glycosylate lipid IVA, forming the conserved inner-core linkage between lipid A and the rest of LPS. KDO is **essential for outer-membrane biogenesis and viability** in Gram-negative bacteria ([PMID: 16765569](https://pubmed.ncbi.nlm.nih.gov/16765569/)), which makes the module biologically obligatory for *P. putida* KT2440.

### Boundaries — what to keep separate

- **Neighboring but distinct — ADP-heptose biosynthesis (M00064):** `gmhA` (PP_1323), `gmhB` (PP_0059), and `hldE` (PP_4934) make ADP-L-*glycero*-D-*manno*-heptose, the *other* inner-core sugar. KEGG places these on the same `ppu00541` umbrella, but they are a separate module and should not count toward KDO satisfiability.
- **Downstream LPS core assembly — WaaA/KdtA (PP_4928):** consumes CMP-KDO; belongs to LPS core biosynthesis, not to the CMP-KDO-*producing* module. It is genomically adjacent to `hldE`/PP_4934 (~5,614,100 bp).
- **Unrelated nucleotide-sugar modules co-drawn on map00541:** dTDP-L-rhamnose (ppu00523/00525), GDP-mannose/GDP-fucose/GDP-perosamine (ppu00051/00552), UDP-GlcNAc (ppu00520), UDP-glucose/UDP-glucuronate (ppu00040). These are the source of the over-propagation described in Section 5.

### Alternate names / database definitions

- Pathway synonyms: "KDO₂-lipid A biosynthesis" (KDO portion), "3-deoxy-D-*manno*-oct-2-ulosonate biosynthesis," MetaCyc "CMP-KDO biosynthesis I."
- KEGG umbrella `map00541`/`ppu00541` is a *composite overview* ("Biosynthesis of various nucleotide sugars"), not a single pathway. The KDO segment is best represented by **module M00063**.
- Enzyme naming caveat: "arabinose-5-phosphate isomerase" (API) is the name used in KDO context; in *E. coli* the housekeeping API is KdsD and the redundant copy is **GutQ** ([PMID: 16199563](https://pubmed.ncbi.nlm.nih.gov/16199563/)).

---

## 3. Expected Step Model

| Step | Reaction | EC | KO | Expected gene(s) | KT2440 candidate(s) | Status |
|------|----------|----|----|------------------|---------------------|--------|
| 1 | ribulose-5-P → arabinose-5-P | 5.3.1.13 | K06041 | *kdsD* / API (+ redundant API) | **PP_0957** (*kdsD*), **PP_1806** (2nd API) | Covered (paralog redundancy) |
| 2 | arabinose-5-P + PEP → KDO-8-P | 2.5.1.55 | K01627 | *kdsA* | **PP_1611** (*kdsA1*), **PP_1807** (*kdsA2*) | Covered (two genuine paralogs) |
| 3 | KDO-8-P → KDO + Pi | 3.1.3.45 | K03270 | *kdsC* | **PP_0956** (*kdsC*) | Covered (single copy) |
| 4 | KDO + CTP → CMP-KDO | 2.7.7.38 | K00979 | *kdsB* | **PP_1902** (*kdsB*) | Covered (single copy) |
| (exit) | CMP-KDO → (KDO)₂-lipid A | 2.4.99.12/13 | K02527 | *waaA*/*kdtA* | PP_4928 | Outside module (LPS core) |

**All four committed steps are encoded, with ≥1 unambiguous gene each.** Steps 1 and 2 have paralog redundancy; steps 3 and 4 are single-copy.

---

## 4. Candidate Genes and Evidence

### 4.1 True KDO-module genes (retain)

**`kdsD` / PP_0957 — arabinose-5-P isomerase (step 1, housekeeping).** UniProt Q88P95, annotated API (EC 5.3.1.13). Genomically adjacent to and divergently oriented from `kdsC`/PP_0956 (~1,098,054–1,099,565 bp), consistent with a core-LPS operon. Sequence analysis: **57.0% identical to *E. coli* KdsD (P45395)** and 52.4% to GutQ (P17115) by global Needleman–Wunsch alignment — the clear housekeeping ortholog. Evidence type: strong ortholog transfer + genomic context. Caveat: PE=3 (homology-only), not experimentally verified in KT2440.

**PP_1806 — second arabinose-5-P isomerase (step 1, redundant).** UniProt Q88LX1, annotated API (EC 5.3.1.13). Full-length (317 aa) CBS/SIS-domain protein, but **divergent**: only 47.1% to *E. coli* KdsD, 45.1% to GutQ, and 48.1% to its own paralog PP_0957. Located *inside* the O-antigen/*wbp* cluster (2,030,374–2,031,327 bp), immediately adjacent to `kdsA2`/PP_1807. This mirrors the *E. coli* KdsD/GutQ two-API paradigm ([PMID: 16199563](https://pubmed.ncbi.nlm.nih.gov/16199563/)) but its cluster location suggests a possible specialized role (e.g., O-antigen-linked A5P provision). **Flag candidate_uncertain; promote to full review.**

**`kdsA1` / PP_1611 — KDO-8-P synthase (step 2).** UniProt Q88MG0, EC 2.5.1.55. Housekeeping copy at ~1,807,950–1,808,795 bp. **70.6% identical to *E. coli* KdsA (P0A715)** — a bona fide KDO-8-P synthase. PE=3.

**`kdsA2` / PP_1807 — KDO-8-P synthase paralog (step 2).** UniProt Q88LX0, EC 2.5.1.55. Located in the O-antigen cluster adjacent to PP_1806 (2,031,402–2,032,244, complement strand). **71.4% identical to kdsA1 and 72.5% to *E. coli* KdsA** — genuinely a second KDO-8-P synthase, not a degenerate pseudogene. PE=3.

**`kdsC` / PP_0956 — KDO-8-P phosphatase (step 3).** UniProt Q88P96, EC 3.1.3.45, HAD-family. Single copy, adjacent to `kdsD`/PP_0957. Unambiguous annotation. PE=3.

**`kdsB` / PP_1902 — CMP-KDO synthetase (step 4).** UniProt Q88LM7, EC 2.7.7.38. Single copy (~2,144,883–2,145,647 bp). The committed activation step; the direct *Pseudomonas* target whose inhibition causes lipid-A-precursor accumulation and growth stasis in *P. aeruginosa* ([PMID: 2833499](https://pubmed.ncbi.nlm.nih.gov/2833499/)). **Highest-priority essential gene; promote to full review.** PE=3.

### 4.2 Adjacent module (heptose, M00064) — reassign, do not count for KDO

| Gene | Locus | Function | Correct module |
|------|-------|----------|----------------|
| `gmhA` | PP_1323 | phosphoheptose isomerase (EC 5.3.1.28) | ADP-heptose (M00064) |
| `gmhB` | PP_0059 | HBP 7-phosphatase (EC 3.1.3.82) | ADP-heptose (M00064) |
| `hldE` | PP_4934 | bifunctional heptose kinase/adenylyltransferase | ADP-heptose (M00064) |

### 4.3 Unrelated nucleotide-sugar genes over-propagated from map00541 — remove from KDO bucket

| Gene(s) | Loci | Pathway | KEGG bucket |
|---------|------|---------|-------------|
| `rmlC`, PP_0500, `rfbC`, `rfbD` | PP_0265, PP_0500, PP_1782, PP_1784 | dTDP-L-rhamnose | ppu00523 |
| `rfbA`, `rffG` | PP_1783, PP_1785 | dTDP-glucose/rhamnose | ppu00525 |
| `algA`, PP_1776, `gmd`, `rmd`, `wbpM` | PP_1277, PP_1776, PP_1799, PP_1800, PP_1805 | GDP-mannose/GDP-fucose/perosamine | ppu00051/00552 |
| `glmU`, `rffE` | PP_5411, PP_1811 | UDP-GlcNAc / UDP-ManNAc | ppu00520 |
| `galU`, `udg` | PP_3821, PP_2926 | UDP-glucose / UDP-glucuronate | ppu00040 |
| `wbpV` | PP_1803 | re-annotated by KEGG as **K24310 UDP-QuiNAc dehydrogenase** (M01009) | — |
| PP_5212 | PP_5212 | "iron-sulfur oxidoreductase" — **no KDO EC assignment** | — |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 No true gaps in the KDO module

Every committed step (EC 5.3.1.13, 2.5.1.55, 3.1.3.45, 2.7.7.38) has at least one unambiguous gene. There is **no missing step** and no need for a lineage-specific alternative enzyme. The module is covered.

### 5.2 The dominant issue is over-annotation of the bucket

Only **6 of 26** candidate genes are KDO genes. The bucket `ppu00541` is a KEGG *overview* map that aggregates many unrelated nucleotide-sugar pathways; propagating its full gene set into a KDO-specific review inflates the candidate list ~4-fold with dTDP-rhamnose, GDP-mannose/fucose, UDP-GlcNAc, and UDP-glucose enzymes that have no role in KDO synthesis. PP_5212 ("iron-sulfur oxidoreductase") carries no relevant EC number and appears to be a spurious inclusion. `wbpV`/PP_1803, listed as a generic "UDP-sugar epimerase," is re-annotated by KEGG as a UDP-QuiNAc dehydrogenase (K24310) belonging to O-antigen sugar biosynthesis — not KDO.

### 5.3 Genuine ambiguities to resolve

- **PP_1806 (second API):** divergent sequence + O-antigen-cluster location raise the question of whether it is a fully redundant housekeeping backup (GutQ-like) or a specialized isozyme. Biochemically unverified.
- **KdsA paralog redundancy (PP_1611 vs PP_1807):** both are genuine KDO-8-P synthases. Whether they are functionally redundant or differentially regulated (housekeeping core-LPS vs O-antigen-linked) is unknown in KT2440.
- **All annotations are homology-only (PE=3).** No enzyme in this KT2440 module has been directly assayed; conclusions rest on ortholog transfer from *E. coli*/*P. aeruginosa* plus KT2440 sequence/context analysis.

### 5.4 Essentiality and dispensability

KDO itself is essential ([PMID: 16765569](https://pubmed.ncbi.nlm.nih.gov/16765569/)), but the *individual* API and KDO-8-P-phosphatase steps are dispensable in *E. coli* because of redundancy — single Δ*kdsD* and Δ*kdsC* are viable, and only the Δ*kdsD* Δ*gutQ* double mutant becomes A5P-auxotrophic ([PMID: 16199563](https://pubmed.ncbi.nlm.nih.gov/16199563/)). The KT2440 `kdsD`/PP_1806 pair likely provides the same buffering. The committed activation step `kdsB` (single copy) is the most vulnerable node — inhibiting CMP-KDO synthetase blocks the pathway and causes growth stasis in *P. aeruginosa* ([PMID: 2833499](https://pubmed.ncbi.nlm.nih.gov/2833499/)). API is feedback-inhibited by the end-product CMP-KDO (Ki ~1.9 µM in *Bacteroides fragilis*, [PMID: 24891442](https://pubmed.ncbi.nlm.nih.gov/24891442/)), indicating end-product control at step 1.

---

## 6. Mechanistic Model and Interpretation

### Two-cluster paralog architecture

The most curation-relevant biological insight is that KT2440 organizes its KDO genes into **two spatially and (likely) functionally distinct sets**:

```
HOUSEKEEPING core-LPS set (dispersed)          O-ANTIGEN-cluster set (co-located)
────────────────────────────────────          ─────────────────────────────────
kdsC/PP_0956 ─ kdsD/PP_0957   ~1.098 Mb        PP_1806 (2nd API) ─ kdsA2/PP_1807
   (divergent pair, likely operon)                (adjacent, ~2.030–2.032 Mb,
kdsA1/PP_1611                 ~1.808 Mb             embedded in wbp / O-antigen
kdsB/PP_1902                 ~2.145 Mb             cluster: gmd, rmd, wbpV, wbpM)
WaaA/KdtA PP_4928 ─ hldE/PP_4934  ~5.614 Mb
```

Sequence identities support this interpretation: PP_0957 is the clear housekeeping API ortholog (57% to *E. coli* KdsD), while PP_1806 is divergent (47%). Both KdsA copies are near-equivalent (71% mutual), suggesting a relatively recent duplication or horizontal acquisition alongside the O-antigen cluster. Functionally, this parallels the *E. coli* KdsD/GutQ redundancy paradigm — one housekeeping enzyme guaranteeing core-LPS KDO for viability, plus a second copy that may be co-regulated with, or dedicated to, surface-polysaccharide biosynthesis. This architecture explains why individual API/KdsA deletions would be tolerated while total loss of KDO would be lethal.

### Curation logic

Because KDO is essential and every step is covered, the module is **satisfiable with high confidence**. The redundancy at steps 1–2 strengthens rather than weakens this call. The single-copy steps (`kdsC`, `kdsB`) are the pathway's essential bottlenecks and its most reliable "presence markers."

---

## 7. Module and GO-Curation Recommendations

### Step-level module calls

| Module step (M00063) | Gene(s) | Call |
|----------------------|---------|------|
| Step 1 — API (EC 5.3.1.13) | `kdsD`/PP_0957 (+ PP_1806) | **covered** (PP_1806 = candidate_uncertain) |
| Step 2 — KDO-8-P synthase (EC 2.5.1.55) | `kdsA1`/PP_1611, `kdsA2`/PP_1807 | **covered** |
| Step 3 — KDO-8-P phosphatase (EC 3.1.3.45) | `kdsC`/PP_0956 | **covered** |
| Step 4 — CMP-KDO synthetase (EC 2.7.7.38) | `kdsB`/PP_1902 | **covered** |

**Overall module status: COVERED / fully satisfiable.**

### Bucket / boundary recommendations

1. **module_needs_revision (scope):** Do not use `ppu00541` ("various nucleotide sugars") as the KDO module boundary. Adopt **M00063** for KDO. The umbrella map's 26-gene candidate list should be de-aggregated.
2. **Reassign** the ~20 non-KDO genes to their proper modules: dTDP-rhamnose (ppu00523/00525), GDP-mannose/fucose (ppu00051/00552), UDP-GlcNAc (ppu00520), UDP-glucose/glucuronate (ppu00040).
3. **Separate module:** Keep `gmhA`/`gmhB`/`hldE` under ADP-heptose (M00064); do not count them toward KDO.
4. **Boundary marker:** WaaA/KdtA (PP_4928) is downstream (LPS core assembly), not part of CMP-KDO production — keep outside the module.
5. **Remove** PP_5212 (no KDO EC) and PP_1803/`wbpV` (KEGG K24310, O-antigen sugar) from the KDO bucket.

### GO-curation

- No new GO terms appear necessary — existing terms (GO:0019294 KDO biosynthetic process; GO:0008676 3-deoxy-8-phosphooctulonate synthase; GO:0019143 KDO-8-P phosphatase; GO:0008690 CMP-KDO synthetase; GO:0019180 A5P isomerase) cover the module.
- Recommend **evidence-code accuracy**: all six proteins should retain IEA/homology evidence (ISO/ISS from *E. coli*) rather than experimental codes, since none is characterized in KT2440.

---

## 8. Genes to Promote to Full `fetch-gene` Review

| Gene | Locus | Reason to promote |
|------|-------|-------------------|
| `kdsB` | PP_1902 | Single-copy, essential committed activation step; validated *Pseudomonas* essentiality/drug node; anchor "presence marker" for the module. |
| PP_1806 | PP_1806 | Divergent second API (47% to KdsD), O-antigen-cluster-embedded; unresolved whether redundant backup or specialized isozyme — candidate_uncertain. |
| (secondary) `kdsC` | PP_0956 | Single-copy essential phosphatase; second reliable presence marker; low ambiguity but worth confirming operon structure with `kdsD`. |

---

## 9. Evidence Base

| PMID | Relevance | How it supports the review |
|------|-----------|----------------------------|
| [16765569](https://pubmed.ncbi.nlm.nih.gov/16765569/) | KDO essentiality; API/phosphatase redundancy | "KDO … is essential for outer membrane biogenesis and cell viability"; "*kdsD* and *kdsC* … non-essential, indicating genetic redundancy." Establishes module obligatoriness and step-level dispensability. |
| [16199563](https://pubmed.ncbi.nlm.nih.gov/16199563/) | GutQ = second *E. coli* API | "Recombinant GutQ … a second copy of API." Directly supports the KT2440 `kdsD`/PP_1806 two-API interpretation. |
| [24891442](https://pubmed.ncbi.nlm.nih.gov/24891442/) | API biochemistry / feedback | Defines API as "the first step in the biosynthesis of Kdo, an essential component of LPS"; CMP-KDO feedback inhibition (Ki ~1.9 µM). |
| [2833499](https://pubmed.ncbi.nlm.nih.gov/2833499/) | *Pseudomonas* KdsB essentiality | Inhibiting CMP-KDO synthetase "causing accumulation of lipid A precursor and subsequent growth stasis." Direct *Pseudomonas* evidence for step-4 essentiality. |
| [19664604](https://pubmed.ncbi.nlm.nih.gov/19664604/) | KdsD structure/function | SIS-domain API structural model; supports domain-based annotation of PP_0957/PP_1806. |
| [28630128](https://pubmed.ncbi.nlm.nih.gov/28630128/) | API distribution | API present across diverse bacteria; supports ortholog transfer confidence. |
| [7961456](https://pubmed.ncbi.nlm.nih.gov/7961456/) | *P. aeruginosa* lipid A/KDO ordering | Lineage-specific acylation-before-KDO in *Pseudomonas*; context for LPS assembly boundary (WaaA downstream). |

**Species-transfer note:** Direct KT2440 experimental evidence for these enzymes is absent; the strongest species-specific data come from *P. aeruginosa* (KdsB essentiality, lipid A ordering). Transfer of *E. coli* KDO biochemistry to *P. putida* is **strong** (conserved essential pathway, high sequence identity), while transfer of the *E. coli* GutQ redundancy model to PP_1806 is **moderate** (analogous architecture, but PP_1806 is more divergent and differently located).

---

## 10. Limitations and Knowledge Gaps

1. **No direct KT2440 characterization.** All six proteins are UniProt PE=3 (inferred from homology). No enzyme assay, structure, or deletion phenotype exists for KT2440 KDO genes specifically.
2. **PP_1806 function unresolved.** Divergence and O-antigen-cluster context leave open whether it is a redundant API, a specialized isozyme, or has an altered substrate preference.
3. **KdsA paralog regulation unknown.** Whether `kdsA1` and `kdsA2` are differentially expressed (core-LPS vs O-antigen) has not been tested.
4. **Essentiality inferred, not measured, in KT2440.** No transposon-essentiality or conditional-knockout data for KT2440 KDO genes were located in this review.
5. **Bucket provenance.** The over-propagation stems from using a KEGG overview map as a module boundary; the corrected scope depends on adopting M00063.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate):**
- Re-scope the KDO module to M00063; de-aggregate `ppu00541`; reassign the ~20 non-KDO genes; remove PP_5212 and re-file `wbpV`/PP_1803 (K24310).
- Mark all four steps **covered**; PP_1806 **candidate_uncertain**.
- Promote `kdsB`/PP_1902 and PP_1806 to full `fetch-gene` review.

**Experimental / bioinformatic (to resolve gaps):**
1. **Biochemical assay of PP_1806** (recombinant A5P isomerase activity; CMP-KDO feedback sensitivity) to classify it vs `kdsD`.
2. **Single and double knockouts** (`kdsD` alone; `kdsD`+PP_1806; `kdsA1` alone; `kdsA1`+`kdsA2`) to test the redundancy model in KT2440.
3. **Expression profiling / reporter fusions** of the two KdsA and two API copies under core-LPS vs O-antigen-inducing conditions.
4. **Essentiality confirmation** for single-copy `kdsC` and `kdsB` via conditional depletion or Tn-seq essentiality-data mining.
5. **Operon mapping** (RT-PCR/RNA-seq) of the `kdsC`–`kdsD` divergent pair and the PP_1806–`kdsA2` O-antigen-cluster pair.

**Expert questions:** Is PP_1806 co-regulated with the O-antigen/*wbp* cluster? Does KT2440 tolerate loss of both APIs, or is the housekeeping copy strictly required for core-LPS KDO?

---

## 12. Key References

- [PMID: 16765569](https://pubmed.ncbi.nlm.nih.gov/16765569/) — *Non-essential KDO biosynthesis and new essential cell envelope biogenesis genes in the E. coli yrbG-yhbG locus.* KDO essentiality; API/phosphatase redundancy.
- [PMID: 16199563](https://pubmed.ncbi.nlm.nih.gov/16199563/) — *Identification of GutQ from Escherichia coli as a D-arabinose 5-phosphate isomerase.* Second *E. coli* API paradigm.
- [PMID: 24891442](https://pubmed.ncbi.nlm.nih.gov/24891442/) — *Analysis of the arabinose-5-phosphate isomerase of Bacteroides fragilis…* API regulation / CMP-KDO feedback inhibition.
- [PMID: 2833499](https://pubmed.ncbi.nlm.nih.gov/2833499/) — *Lipid A precursor from Pseudomonas aeruginosa is completely acylated prior to addition of KDO.* CMP-KDO synthetase essentiality in *Pseudomonas*.
- [PMID: 19664604](https://pubmed.ncbi.nlm.nih.gov/19664604/) — *Structure prediction and functional analysis of KdsD…* SIS-domain API structure/function.
- [PMID: 28630128](https://pubmed.ncbi.nlm.nih.gov/28630128/) — *Identification of a D-Arabinose-5-Phosphate Isomerase in the Gram-Positive Clostridium tetani.* API taxonomic distribution.
- [PMID: 7961456](https://pubmed.ncbi.nlm.nih.gov/7961456/) — *Endotoxin biosynthesis in Pseudomonas aeruginosa: enzymatic incorporation of laurate before KDO.* Lineage-specific LPS assembly ordering.


## Artifacts

- [OpenScientist final report](PSEPK__kdo-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__kdo-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16765569
2. PMID:16199563
3. PMID:2833499
4. PMID:24891442
5. PMID:19664604
6. PMID:28630128
7. PMID:7961456