---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T11:49:33.582077'
end_time: '2026-08-08T12:29:04.246868'
duration_seconds: 2370.67
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: adp_heptose_biosynthesis
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

adp_heptose_biosynthesis in Pseudomonas putida KT2440

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

# Species-Aware Module Review: ADP-heptose Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Commissioned topic:** `adp_heptose_biosynthesis`
**Resolved local bucket:** KEGG `ppu00541` — "Biosynthesis of various nucleotide sugars" (11 primary + 26 candidate genes)
**Correct module identity:** KEGG **module M00064**, "ADP-L-glycero-D-manno-heptose biosynthesis (sedoheptulose-7P ⇒ ADP-LDmanHep)"
**Date:** 2026-08-08

---

## 1. Executive summary

- The commissioned topic **adp_heptose_biosynthesis** is a narrow, well-defined 4-enzyme pathway (KEGG **M00064**) that makes **ADP-L-glycero-β-D-manno-heptose**, the activated sugar donor for the heptose residues of the LPS **inner core**. It is **not** the same as the broad KEGG bucket `ppu00541`/`map00541` ("Biosynthesis of various nucleotide sugars") from which the 26-gene candidate list was drawn. That bucket conflates ≥6 unrelated nucleotide-sugar pathways.
- **Only 3 of the 26 candidate genes belong to this module.** The other 23 are KDO, dTDP-rhamnose, GDP-mannose/fucose, UDP-GlcNAc and UDP-glucuronate genes that should be excluded from ADP-heptose satisfiability.
- **Steps 1–4 are covered with high confidence:** `gmhA` (PP_1323), bifunctional `hldE` (PP_4934, covering two steps), and `gmhB` (PP_0059). KEGG orthology and UniProt curated EC numbers agree.
- **The final step — the ADP-L-glycero-D-manno-heptose-6-epimerase HldD/GmhD (K03274, EC 5.1.3.20) — is a genome-confirmed GAP in KT2440.** Four independent authorities agree there is no *hldD*: KEGG (`link/ppu/K03274` → none), UniProt/UniRef (no KT2440 protein in the UniRef50 *or* UniRef90 cluster of the same-genus HldD *P. aeruginosa* PA3337/Q9HYQ8), NCBI RefSeq (zero heptose-6-epimerase / *hldD/gmhD/rfaD* records for txid160488), and — decisively — **tblastn of PA3337 against the KT2440 chromosome (AE015451.2 + 9 other assemblies) yields only a 29%-identity best hit (a *galE*), with no ortholog-level ORF anywhere in the 6-frame-translated genome.** Method calibration confirms sensitivity: true PA↔PP orthologs score 80–92% (gmhA 91.8%, gmhB 80.0%). So the gene is genuinely absent, not merely un-annotated.
- **CORRECTION (Iteration 2):** PP_3206 is **not** the epimerase — KEGG K26183 defines it as *fdeJ* (naringenin/flavonoid degradation, map00946). Its PANTHER-subfamily match reflected the broad NAD-epimerase/dehydratase superfamily, not HldD specificity.
- **Interpretation:** steps 1–4 still make ADP-D-glycero-D-manno-heptose and the downstream WaaC/WaaF/WaaG/WaaP inner-core machinery is intact, so heptose *is* incorporated. Because the D→L epimerase is absent, either **(a)** KT2440 uses **D-glycero-D-manno-heptose (D,D-Hep) directly** in its core (no epimerization needed → step 5 `not_expected_in_target_taxon`, and the generic module endpoint is wrong for this organism), or **(b)** a **non-orthologous/novel epimerase** supplies the activity (→ new gene/GO request). Note *P. aeruginosa* uses L,D-Hep and *does* encode HldD, so this is a KT2440-specific feature. Curation call: **step 5 = gap / module_needs_revision**; the decisive open question is the **stereochemistry of KT2440 inner-core heptose** (needs LPS structural data).

---

## 2. Target-organism pathway definition

**Process included (M00064):** cytoplasmic conversion of the pentose-phosphate-pathway intermediate **D-sedoheptulose-7-phosphate** into the nucleotide sugar **ADP-L-glycero-β-D-manno-heptose**, in four enzymatic activities:

| # | Reaction | Enzyme | EC | KO |
|---|----------|--------|----|----|
| 1 | Sedoheptulose-7-P → D-glycero-D-manno-heptose-7-P | GmhA (phosphoheptose isomerase) | 5.3.1.28 | K03271 |
| 2 | Heptose-7-P → D-glycero-β-D-manno-heptose-1,7-bisP | HldE kinase domain | 2.7.1.167 | K03272 (or K21344) |
| 3 | Heptose-1,7-bisP → D-glycero-β-D-manno-heptose-1-P | GmhB (bisphosphate 7-phosphatase) | 3.1.3.82 | K03273 |
| 4 | Heptose-1-P → ADP-D-glycero-β-D-manno-heptose | HldE adenylyltransferase domain | 2.7.7.70 | K03272 (or K21345) |
| 5 | ADP-D-glycero-heptose → **ADP-L-glycero-D-manno-heptose** | **HldD/GmhD (6-epimerase)** | **5.1.3.20** | **K03274** |

Canonical pathway biochemically established in *E. coli* (Kneidinger et al. 2002, PMID 11751812; McArthur et al. 2005, PMID 16030223).

**Neighboring pathways to keep separate:**
- **KDO biosynthesis** (KdsD/KdsA/KdsC/KdsB) — the *other* LPS inner-core sugar (3-deoxy-D-manno-octulosonate). Distinct module (M00063), even though KEGG places it on the same `map00541` overview.
- **LPS core assembly / transfer** — WaaC, WaaF heptosyltransferases and WaaP/WapP/WapQ heptose kinases *use* ADP-heptose but are downstream (map00540 LPS biosynthesis), not part of M00064.
- **dTDP-L-rhamnose** (rmlA-D/rfbA-D), **GDP-D-rhamnose/GDP-fucose** (gmd/rmd), **UDP-GlcNAc** (glmU/rffE), **UDP-glucuronate** (galU/udg) — all separate nucleotide-sugar modules.

**Alternate names:** module M00064 "ADP-LDmanHep biosynthesis"; genes historically *rfaE* (=*hldE*), *yaeD* (=*gmhB*), *waaD/rfaD/htrM* (=*hldD*), *gmhD* (=*hldD*).

---

## 3. Expected step model (satisfiability call per step)

| Step | Enzyme (KO) | KT2440 gene | Call | Basis |
|------|-------------|-------------|------|-------|
| 1 | GmhA (K03271) | PP_1323 | **covered** | KEGG ortholog + UniProt EC 5.3.1.28 |
| 2 | HldE kinase (K03272) | PP_4934 | **covered** | KEGG ortholog + UniProt EC 2.7.1.167 (bifunctional) |
| 3 | GmhB (K03273) | PP_0059 | **covered** | KEGG ortholog + UniProt EC 3.1.3.82 |
| 4 | HldE adenylyltransferase (K03272) | PP_4934 | **covered** | same bifunctional protein, UniProt EC 2.7.7.70 |
| 5 | HldD/GmhD epimerase (K03274) | ***none — absent from genome*** | **gap / module_needs_revision** (possibly `not_expected_in_target_taxon`) | no gene in KEGG/UniProt/RefSeq; genome tblastn best hit 29% (a *galE*) across all 10 KT2440 assemblies |

**Module verdict:** 4 of 5 catalytic steps covered by 3 genes (through ADP-**D**-glycero-D-manno-heptose). The terminal D→L epimerase (step 5) is **genome-confirmed absent**, so ADP-**L**-glycero-D-manno-heptose is *not* demonstrably produced by an M00064-canonical route. The module is therefore **not satisfiable as defined** in KT2440. Whether this is a true biological difference (D,D-Hep core → epimerase not needed) or a novel epimerase is the key open question — resolvable by LPS structural analysis.

---

## 4. Candidate genes and evidence

### High-confidence, in-module (promote to "covered")
- **PP_1323 `gmhA`** (Q88N89, 195 aa) — phosphoheptose isomerase, EC 5.3.1.28, KEGG K03271. Also carries synonym *diaA* (DnaA-interacting); the GmhA/DiaA fold is shared, but the EC and KO assignment are unambiguous. **Direct KEGG+UniProt evidence.**
- **PP_4934 `hldE`/`rfaE`** (Q88D93, 473 aa) — bifunctional D-β-D-heptose-7-P kinase (EC 2.7.1.167) + heptose-1-P adenylyltransferase (EC 2.7.7.70), KEGG K03272. Covers module steps 2 and 4. **Direct evidence.**
- **PP_0059 `gmhB`** (Q88RS0, 175 aa) — D,D-heptose-1,7-bisphosphate 7-phosphatase, EC 3.1.3.82, KEGG K03273. **Direct evidence.**

### Downstream users of the pathway product (evidence the module is functional; not part of M00064)
- **PP_0342 `waaC`** (heptosyltransferase I, EC 2.4.99.23), **PP_0341 `waaF`** (heptosyltransferase II, EC 2.4.99.24), **PP_0344 `waaP`** (heptose-I kinase), **PP_0345 WapP**, **PP_0346 WapQ** — an intact inner-core cluster. Their presence is strong indirect evidence that ADP-L-glycero-D-manno-heptose is synthesized in KT2440.

### Step 5 (HldD/GmhD epimerase) — no ortholog present (`gap`)
No KT2440 protein is a credible HldD. Evidence: aligning the entire KT2440 IPR001509 epimerase set (9 proteins) against the same-genus reference HldD (P. aeruginosa PA3337/Q9HYQ8, 330 aa, EC 5.1.3.20, carries HldD-specific IPR011912) yields a best identity of only **34.8% (PP_3129 galE)** — below even the galE↔galE cross-species value (44.1%) and far below true-ortholog calibration (gmhA 91.8%, gmhB 80.0%). No KT2440 protein is in UniRef50/90_Q9HYQ8.
- **PP_3206 (Q88HZ6) — RETRACTED as HldD candidate.** KEGG K26183 defines it as *fdeJ* (naringenin/flavonoid degradation, map00946). Its PANTHER PTHR43103:SF3 assignment is shared with HldD only at the broad superfamily level; sequence identity to genuine HldD is ~33% (background). **Not the epimerase.**
- Other epimerase-family proteins are their own enzymes, not HldD: **PP_3129 `galE`** and **PP_0501** are GalE-type (InterPro IPR005886 UDP_G4E); **PP_5305** and **PP_1803 `wbpV`** are in PANTHER PTHR48079; **PP_1805 `wbpM`** is a large polytopic protein. None carries the HldD-specific IPR011912.

### Candidate-list genes that are OUT of scope (exclude from this module)
KDO: PP_0956 `kdsC` (K03270), PP_0957/PP_1806 (K06041 API), PP_1611/PP_1807 `kdsA1/2` (K01627), PP_1902 `kdsB` (K00979). dTDP-rhamnose: PP_0265 `rmlC`, PP_0500, PP_1782 `rfbC`, PP_1783 `rfbA`, PP_1784 `rfbD`, PP_1785 `rffG`. GDP-mannose/fucose: PP_1277/PP_1776 `algA`, PP_1799 `gmd` (K01711), PP_1800 `rmd` (K22252). UDP-GlcNAc: PP_5411 `glmU`, PP_1811 `rffE`. UDP-glucuronate: PP_3821 `galU`, PP_2926 `udg`. Misc oxidoreductases PP_5212 (K00523), PP_1805 `wbpM` (K24300).

---

## 5. Gaps, ambiguities, and likely over-annotations

**Genuine gap (single):** HldD/GmhD (K03274, EC 5.1.3.20). Confirmed absent by four independent methods: KEGG (no ppu K03274), UniProt/UniRef (no KT2440 member in UniRef50/90 of PA3337 HldD), NCBI RefSeq (no heptose-6-epimerase record for txid160488), and genome tblastn (best hit 29%, a *galE*, across all 10 KT2440 assemblies). KEGG lists M00064 COMPLETE only for *E. coli*, not *ppu*.

**This is a real absence, not an annotation artifact** — the earlier "annotation gap" hypothesis was disproven this iteration by the genome-level tblastn (an unannotated ORF would have been detected by 6-frame translation).

**The biological puzzle and two remaining hypotheses:** steps 1–4 (GmhA/HldE/GmhB) plus intact WaaC/WaaF/WaaG/WaaP mean ADP-heptose is made and transferred to the core, yet the D→L epimerase is missing.
- **(a) D,D-heptose core (favored, testable):** KT2440 incorporates D-glycero-D-manno-heptose without epimerization; step 5 is then `not_expected_in_target_taxon` and the generic module boundary (which assumes the L,D-Hep endpoint) is wrong for this organism. Requires the L-vs-D stereochemistry of KT2440 core heptose (LPS structural data).
- **(b) Non-orthologous epimerase:** a novel/analogous enzyme performs the D→L step; would warrant a new gene model and GO request.

**Species-transfer caveat:** *P. aeruginosa* (congener) uses L-glycero-D-manno-heptose in its inner core and *does* encode HldD (PA3337) — so the KT2440 absence is lineage-/strain-specific and cannot be assumed from *Pseudomonas*-level evidence. The Helander et al. 1980 (PMID 7000706) heptose data are for "*P. putida*" generically and do not resolve heptose stereochemistry or strain.

**Retracted (Iteration 2):** PP_3206 is *fdeJ* (K26183, flavonoid degradation), not HldD; the Iteration-1 PANTHER-subfamily match was superfamily-level only. No KT2440 NAD-epimerase (PP_0501, PP_3206, PP_5305, PP_1803 wbpV, PP_3129 galE) is the epimerase.

**Over-annotation / over-propagation risks for curation:**
- The 26-gene bucket massively over-includes; treating it as the module gene set would wrongly inflate coverage.
- **PP_1323 `gmhA`** carries a *diaA* synonym — do not let the DnaA-regulation annotation dilute its metabolic (GmhA) role.
- Multiple generic "epimerase/dehydratase" proteins (PP_0501, PP_3206, PP_5305, PP_1803) risk being over-mapped to EC 5.1.3.20 without sequence proof. **PP_3206 in particular must NOT be mapped to HldD** — it is *fdeJ* (flavonoid degradation, K26183). None of these is the epimerase; the real HldD is absent from the reference proteome.

---

## 6. Module and GO-curation recommendations

| Module step | Recommended status |
|-------------|--------------------|
| GmhA (step 1) | **covered** (PP_1323) |
| HldE kinase (step 2) | **covered** (PP_4934) |
| GmhB (step 3) | **covered** (PP_0059) |
| HldE adenylyltransferase (step 4) | **covered** (PP_4934) |
| HldD/GmhD epimerase (step 5) | **gap → module_needs_revision**; candidate `not_expected_in_target_taxon` pending LPS data |

**Actions:**
1. **Redefine the module gene set** to the M00064 core (gmhA, hldE, gmhB, hldD) and explicitly exclude KDO/rhamnose/mannose/GlcNAc/glucuronate genes; the current `ppu00541` bucket boundary is wrong for this organism-specific module.
2. **Do NOT assign any gene to HldD in KT2440.** PP_3206 is *fdeJ* (K26183, flavonoid degradation). No KT2440 protein should be mapped to K03274/EC 5.1.3.20/GO:0008712 — the gene is genome-confirmed absent.
3. **Mark M00064 as `module_needs_revision` for PSEPK** and add an organism note that the terminal 6-epimerase is absent while steps 1–4 and the downstream heptosyltransferases are present.
4. **Request expert/experimental clarification of KT2440 inner-core heptose stereochemistry** (L- vs D-glycero-D-manno-heptose). If D,D-Hep, set step 5 `not_expected_in_target_taxon` and create a KT2440-specific module variant ending at ADP-D,D-heptose. If L,D-Hep, open a search for a **non-orthologous epimerase** and a possible new gene/GO request.
5. Keep GO terms for steps 1–4 as-is (well-supported by UniProt EC annotations).

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0342 `waaC` / PP_0341 `waaF` (highest priority, now):** the heptosyltransferases define which heptose stereoisomer is used. A `fetch-gene` review of their substrate specificity (vs characterized L,D-Hep transferases) is the fastest bioinformatic route to decide whether an L→D epimerase (HldD) is even required — directly resolving the step-5 gap without wet-lab work.
2. **PP_3206 `fdeJ`** — review only to formally *exclude* it from HldD (confirm K26183 flavonoid-degradation assignment); prevents future over-mapping to EC 5.1.3.20.
3. **PP_4934 `hldE`** — verify both catalytic domains are intact (single bifunctional protein carrying two module steps).
4. **PP_1323 `gmhA`** — confirm the metabolic (isomerase) assignment is not overshadowed by the *diaA* regulatory annotation.
5. Note: there is **no HldD locus to promote** — genome tblastn confirms none exists.

---

## 8. Key references

- Kneidinger B, et al. *Biosynthesis pathway of ADP-L-glycero-β-D-manno-heptose in Escherichia coli.* J Biol Chem 2002. **PMID 11751812.** — Defines the GmhA/HldE/GmhB/HldD four-enzyme pathway.
- McArthur F, et al. *Functional analysis of the glycero-manno-heptose 7-phosphate kinase domain from the bifunctional HldE protein…* J Bacteriol 2005. **PMID 16030223.** — HldE is bifunctional (kinase + adenylyltransferase).
- Desroy N, et al. *Towards Gram-negative antivirulence drugs: new inhibitors of HldE kinase.* 2009. **PMID 19124251.** — HldE bifunctional role; heptose-less LPS attenuates virulence.
- Helander I, et al. *Chemical structure and inhalation toxicity of lipopolysaccharides…* 1980. **PMID 7000706.** — *P. putida* LPS contains heptose.
- KEGG module **M00064**, orthology links `rest.kegg.jp/link/ppu/K03271…K03274`, and KO **K26183** (fdeJ) definition (accessed 2026-08-08).
- UniProt proteome **UP000000556** (organism 160488); reference HldD **Q9HYQ8** (*P. aeruginosa* PA3337, EC 5.1.3.20, InterPro IPR011912) and *E. coli* HldD **P67910**; **UniRef50/UniRef90_Q9HYQ8** cluster membership (no taxon-160488 member) (accessed 2026-08-08).
- **NCBI**: RefSeq protein / Gene esearch for txid160488 (no *hldD/gmhD/rfaD* or heptose-6-epimerase); **tblastn** of Q9HYQ8 vs KT2440 genome **AE015451.2** (+ assemblies CP167163.1, CP097524–529, CP169744.1, CP159467.1) — best hit 29% id, E=9e-15 (accessed 2026-08-08).

---

### Uncertainty & species-transfer statement
Steps 1–4 rest on **direct KT2440 evidence** (KEGG ortholog assignments + UniProt curated EC numbers for PP_1323/PP_4934/PP_0059) and are high-confidence. Step 5 (HldD) is now settled at the sequence/genome level as a **direct-for-KT2440 absence**: no gene in KEGG/UniProt/RefSeq, no UniRef50/90 membership, and genome tblastn (6-frame) finds only a 29% *galE*-level hit across all 10 KT2440 assemblies — calibrated against 80–92%-identity true PA↔PP orthologs. What remains genuinely open is the **biological interpretation**: (a) a D,D-heptose core with no epimerase requirement (→ `not_expected_in_target_taxon`), or (b) a non-orthologous epimerase. This is **inferred, not demonstrated**, and needs KT2440 LPS structural data (heptose stereochemistry) and/or heptosyltransferase substrate characterization. Species transfer is explicitly weak here: the congener *P. aeruginosa* uses L,D-Hep and *does* encode HldD (PA3337), so *Pseudomonas*-level or generic-bacterial evidence must **not** be used to assert an HldD in KT2440. The Helander et al. 1980 (PMID 7000706) heptose datum is species-generic and does not resolve stereochemistry or strain.


## Artifacts

- [OpenScientist final report](PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist_artifacts/final_report.pdf)