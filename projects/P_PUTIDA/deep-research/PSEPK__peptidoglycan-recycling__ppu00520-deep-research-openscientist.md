---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T11:25:04.416012'
end_time: '2026-08-08T11:49:25.840633'
duration_seconds: 1461.42
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: peptidoglycan_recycling
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00520
  pathway_id: ppu00520
  pathway_name: Amino sugar and nucleotide sugar metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00520 with 8 primary genes; module
    area: nucleotide_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '25'
  candidate_genes: '- amgK: PP_0405 | Q88QT3 | N-acetylmuramate/N-acetylglucosamine
    kinase (MurNAc/GlcNAc kinase) (EC 2.7.1.221) (Anomeric sugar kinase) (EC 2.7.1.221;
    primary bucket kegg:ppu00520)

    - murU: PP_0406 | Q88QT2 | N-acetylmuramate alpha-1-phosphate uridylyltransferase
    (MurNAc-1P uridylyltransferase) (MurNAc-alpha-1P uridylyltransferase) (EC 2.7.7.99)
    (EC 2.7.7.99; primary bucket kegg:ppu00520)

    - anmK: PP_0434 | Q88QQ4 | Anhydro-N-acetylmuramic acid kinase (EC 2.7.1.170)
    (AnhMurNAc kinase) (EC 2.7.1.170; primary bucket kegg:ppu00520)

    - PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase family protein
    (primary bucket kegg:ppu00052)

    - murA: PP_0964 | Q88P88 | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC
    2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase)
    (EPT) (EC 2.5.1.7; primary bucket kegg:ppu00550)

    - glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2;
    primary bucket kegg:ppu00052)

    - algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate
    isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate
    guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP)
    (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary
    bucket kegg:ppu00051)

    - algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC
    1.1.1.132; primary bucket kegg:ppu00051)

    - mupP: PP_1764 | Q88M11 | N-acetylmuramic acid 6-phosphate phosphatase (MurNAc
    6-phosphate phosphatase) (MurNAc-6P phosphatase) (EC 3.1.3.105) (EC 3.1.3.105;
    primary bucket kegg:ppu00520)

    - PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13)
    (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - rfbA: PP_1783 | Q88LZ3 | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24)
    (EC 2.7.7.24; primary bucket kegg:ppu00525)

    - pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9)
    (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - rffE: PP_1811 | Q88LW6 | UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) (EC
    5.1.3.14; primary bucket kegg:ppu00520)

    - murB: PP_1904 | Q88LM5 | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98)
    (UDP-N-acetylmuramate dehydrogenase) (EC 1.3.1.98; primary bucket kegg:ppu00550)

    - nagZ: PP_2145 | Q88KZ4 | Beta-hexosaminidase (EC 3.2.1.52) (Beta-N-acetylhexosaminidase)
    (N-acetyl-beta-glucosaminidase) (EC 3.2.1.52; primary bucket kegg:ppu01501)

    - udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22;
    primary bucket kegg:ppu00040)

    - galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary
    bucket kegg:ppu00052)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

    - pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9)
    (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9;
    primary bucket kegg:ppu00500)

    - glmM: PP_4716 | Q88DV3 | Phosphoglucosamine mutase (EC 5.4.2.10) (EC 5.4.2.10;
    primary bucket kegg:ppu00520)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

    - glmS: PP_5409 | Q88BX8 | Glutamine--fructose-6-phosphate aminotransferase [isomerizing]
    (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) (GFAT) (Glucosamine-6-phosphate
    synthase) (Hexosephosphate aminotransferase) (L-glutamine--D-fructose-6-phosphate
    amidotransferase) (EC 2.6.1.16; primary bucket kegg:ppu00520)

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
  path: PSEPK__peptidoglycan-recycling__ppu00520-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__peptidoglycan-recycling__ppu00520-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

peptidoglycan_recycling in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00520
- Resolved ID: ppu00520
- Resolved name: Amino sugar and nucleotide sugar metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00520 with 8 primary genes; module area: nucleotide_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 25

- amgK: PP_0405 | Q88QT3 | N-acetylmuramate/N-acetylglucosamine kinase (MurNAc/GlcNAc kinase) (EC 2.7.1.221) (Anomeric sugar kinase) (EC 2.7.1.221; primary bucket kegg:ppu00520)
- murU: PP_0406 | Q88QT2 | N-acetylmuramate alpha-1-phosphate uridylyltransferase (MurNAc-1P uridylyltransferase) (MurNAc-alpha-1P uridylyltransferase) (EC 2.7.7.99) (EC 2.7.7.99; primary bucket kegg:ppu00520)
- anmK: PP_0434 | Q88QQ4 | Anhydro-N-acetylmuramic acid kinase (EC 2.7.1.170) (AnhMurNAc kinase) (EC 2.7.1.170; primary bucket kegg:ppu00520)
- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase family protein (primary bucket kegg:ppu00052)
- murA: PP_0964 | Q88P88 | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC 2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase) (EPT) (EC 2.5.1.7; primary bucket kegg:ppu00550)
- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2; primary bucket kegg:ppu00052)
- algA: PP_1277 | Q88ND5 | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphomannose isomerase) (PMI); Mannose-1-phosphate guanylyltransferase (EC 2.7.7.13) (GDP-mannose pyrophosphorylase) (GMP) (GMPP) (GTP--mannose-1-phosphate guanylyltransferase)] (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- algD: PP_1288 | Q88NC4 | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) (EC 1.1.1.132; primary bucket kegg:ppu00051)
- mupP: PP_1764 | Q88M11 | N-acetylmuramic acid 6-phosphate phosphatase (MurNAc 6-phosphate phosphatase) (MurNAc-6P phosphatase) (EC 3.1.3.105) (EC 3.1.3.105; primary bucket kegg:ppu00520)
- PP_1776: PP_1776 | Q88M00 | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) (EC 2.7.7.13; 5.3.1.8; primary bucket kegg:ppu00051)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- rfbA: PP_1783 | Q88LZ3 | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) (EC 2.7.7.24; primary bucket kegg:ppu00525)
- pgi1: PP_1808 | Q88LW9 | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (PHI 1) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- rffE: PP_1811 | Q88LW6 | UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) (EC 5.1.3.14; primary bucket kegg:ppu00520)
- murB: PP_1904 | Q88LM5 | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase) (EC 1.3.1.98; primary bucket kegg:ppu00550)
- nagZ: PP_2145 | Q88KZ4 | Beta-hexosaminidase (EC 3.2.1.52) (Beta-N-acetylhexosaminidase) (N-acetyl-beta-glucosaminidase) (EC 3.2.1.52; primary bucket kegg:ppu01501)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary bucket kegg:ppu00052)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- pgi2: PP_4701 | Q88DW7 | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (PHI 2) (EC 5.3.1.9; primary bucket kegg:ppu00500)
- glmM: PP_4716 | Q88DV3 | Phosphoglucosamine mutase (EC 5.4.2.10) (EC 5.4.2.10; primary bucket kegg:ppu00520)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)
- glmS: PP_5409 | Q88BX8 | Glutamine--fructose-6-phosphate aminotransferase [isomerizing] (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) (GFAT) (Glucosamine-6-phosphate synthase) (Hexosephosphate aminotransferase) (L-glutamine--D-fructose-6-phosphate amidotransferase) (EC 2.6.1.16; primary bucket kegg:ppu00520)
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

# Species-Aware Module Review: Peptidoglycan (MurNAc) Recycling in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI txid 160488; proteome UP000000556)
**Review topic:** `peptidoglycan_recycling`
**Nominal bucket:** KEGG `ppu00520` — *Amino sugar and nucleotide sugar metabolism* (module area: nucleotide_metabolism)
**Prepared for:** manual module satisfiability + gene-annotation curation

---

## 1. Executive summary

*P. putida* KT2440 possesses a **complete, biochemically validated cell-wall-sugar (MurNAc) recycling module** built around the *Pseudomonas*-defining **AmgK–MurU shortcut** that regenerates UDP-MurNAc directly from recycled N-acetylmuramic acid, **bypassing the de novo MurA/MurB route** (and thereby conferring intrinsic fosfomycin resistance) (Gisin et al. 2013, PMID 23831760). Two of the committed enzymes — **AmgK (PP_0405)** and **MurU (PP_0406)** — were characterized *directly in P. putida*, and the downstream phosphatase **MupP (PP_1764)** was *first discovered in P. putida* (Borisova et al. 2017, PMID 28351914). This is therefore an unusually strong, species-direct module.

Key curation conclusions:

- **The review topic is a focused sub-module of the broad KEGG map.** Only ~5 of the 25 candidate genes are true peptidoglycan-recycling steps (`amgK`, `murU`, `anmK`, `mupP`, `nagZ`). The remaining genes belong to **de novo UDP-GlcNAc/UDP-MurNAc synthesis** or to **unrelated nucleotide-sugar branches** (alginate, dTDP-rhamnose, UDP-glucose/galactose) that share map `ppu00520` and neighbors but are **not** recycling.
- **Several recycling steps are missing from the candidate metadata but are genomically present** and should be added: the importer **AmpG (PP_1355)**, the cytoplasmic recycling amidase **AmpD (PP_0789, EC 3.5.1.28)**, and the murein-peptide ligase **Mpl (PP_0547, EC 6.3.2.45)**. (Verified via KEGG ortholog links and UniProt proteome UP000000556.) Note the recycling amidase is **AmpD (PP_0789)**, distinct from the septal division amidase AmiC (PP_4897).
- **The *E. coli* catabolic branch is absent.** No **MurQ etherase** (K07106) gene exists in `ppu`; consequently the *P. putida* route is **anabolic (wall → wall)** rather than catabolic (wall → central metabolism). `murQ` should be marked **not_expected_in_target_taxon**.

Evidence strength: **strong/direct** for AmgK, MurU, MupP; **strong** (UniProt pathway tag + KEGG ortholog + *Pseudomonas* functional literature) for AnmK, NagZ, AmpG, AmpD, Mpl; **inference/not-assessed** only for accessory peptide-recycling steps not in scope here (e.g. LdcA LD-carboxypeptidase, peptide permeases).

**Independent curation-grade confirmation (UniProt UP000000556):** AmgK (PP_0405), MurU (PP_0406) and MupP (PP_1764) are annotated `PATHWAY: Cell wall biogenesis; peptidoglycan recycling` with **experimental ECO codes** — `ECO:0000269|PubMed:23831760` (AmgK, MurU) and `ECO:0000269|PubMed:28351914` (MupP); AnmK (PP_0434) and Mpl (PP_0547) carry the same recycling pathway tag; the importer is explicitly `Muropeptide permease AmpG` (PP_1355) and the amidase `1,6-anhydro-N-acetylmuramyl-L-alanine amidase AmpD` (PP_0789, cytoplasmic, Zn). Curators can therefore rely on UniProt pathway tags + ECO codes, not just homology.

---

## 2. Target-organism pathway definition

**Included process (this module):** the intracellular salvage of the amino sugar **N-acetylmuramic acid (MurNAc)** and its anhydro form (1,6-anhydro-MurNAc) that are released during normal peptidoglycan (PGN) turnover, converting them back into the activated cell-wall precursor **UDP-MurNAc** for reincorporation into peptidoglycan. In *P. putida* this proceeds:

> PGN turnover → periplasmic lytic transglycosylases generate **GlcNAc-1,6-anhydro-MurNAc-peptides** → import (**AmpG**) → cytoplasmic **NagZ** removes GlcNAc → **AmpD** removes the stem peptide → **AnmK** phosphorylates 1,6-anhydro-MurNAc to MurNAc-6-P → **MupP** dephosphorylates to MurNAc → **AmgK** (anomeric C1 kinase) → MurNAc-1-P → **MurU** → **UDP-MurNAc**.

**Neighboring processes to keep separate:**

- **De novo UDP-GlcNAc biosynthesis** (GlmS→GlmM→GlmU) and **de novo UDP-MurNAc synthesis** (MurA→MurB). These *feed the same product pool* but are a different module; the recycling shortcut explicitly *bypasses* MurA/MurB.
- **Peptidoglycan biosynthesis proper** (MurC–F, MurG, MraY, PBPs) — downstream consumers of UDP-MurNAc.
- **Other nucleotide-sugar metabolism in `ppu00520`/neighbors:** alginate/GDP-mannose (`algA`, `algC`, `algD`, `cpsG`, `PP_1776`), dTDP-rhamnose (`rfbA`), UDP-glucose/UDP-galactose/UDP-glucuronate (`galU`, `galE`, `udg`, `pgm`, `pgi1/2`, `glk`, `PP_0501`). None are peptidoglycan recycling.
- **Enterobacterial-common-antigen / UDP-ManNAc branch** (`rffE`/`wecB`, UDP-GlcNAc 2-epimerase) — a UDP-GlcNAc consumer, not recycling.

**Alternate names / database definitions:** "PGN recycling", "cell-wall sugar recycling/salvage", "MurNAc recycling", "AmgK/MurU recycling shortcut", "muropeptide recycling". KEGG folds the enzymes into map 00520; there is no dedicated KEGG *pathway* for the *Pseudomonas* recycling shortcut, so a bespoke module document is appropriate.

---

## 3. Expected step model

| # | Step (function) | Enzyme/type | EC | Expected? | Notes |
|---|-----------------|-------------|-----|-----------|-------|
| S0 | Generate 1,6-anhydro-MurNAc muropeptides (turnover) | Lytic transglycosylases (Slt/MltF) | 4.2.2.29 | Yes | Upstream of module; many paralogs |
| S1 | Import muropeptides across inner membrane | AmpG MFS permease | – | Yes | **Missing from metadata** |
| S2 | Remove terminal GlcNAc | NagZ β-N-acetylglucosaminidase | 3.2.1.52 | Yes | In metadata (bucket ppu01501) |
| S3 | Remove stem peptide | AmpD amidase (**PP_0789**) | 3.5.1.28 | Yes | **Missing from metadata**; distinct from septal AmiC PP_4897 |
| S4 | Phosphorylate 1,6-anhydro-MurNAc → MurNAc-6-P | AnmK | 2.7.1.170 | Yes | In metadata |
| S5 | Dephosphorylate MurNAc-6-P → MurNAc | MupP (HAD) | 3.1.3.105 | Yes | In metadata; *first found in P. putida* |
| S6 | Anomeric (C1) phosphorylation MurNAc → MurNAc-1-P | AmgK | 2.7.1.221 | Yes | In metadata; direct P. putida evidence |
| S7 | Uridylylation MurNAc-1-P → UDP-MurNAc | MurU | 2.7.7.99 | Yes | In metadata; direct P. putida evidence |
| — | *Catabolic diversion MurNAc-6-P → GlcNAc-6-P* | MurQ etherase | 4.2.1.126 | **No** | Absent in *Pseudomonas*; makes route anabolic |
| S8 | Re-ligate intact stem peptide onto UDP-MurNAc | Mpl (**PP_0547**) | 6.3.2.45 | Yes | Confirmed in UniProt UP000000556 (see §5) |

---

## 4. Candidate genes and evidence

### 4a. Core recycling steps — **COVERED** (promote to full review)

- **amgK — PP_0405 | Q88QT3 | EC 2.7.1.221 (K07102).** Anomeric MurNAc/GlcNAc 1-kinase; makes MurNAc-α-1-P. **Direct P. putida biochemical characterization** (Gisin 2013). Committed step. *Caveat:* ROK/kinase family; the UniProt "GlcNAc kinase" side-activity broadens EC/GO mapping — annotate primarily as the C1 MurNAc kinase.
- **murU — PP_0406 | Q88QT2 | EC 2.7.7.99 (K00992).** MurNAc-α-1-P uridylyltransferase; makes UDP-MurNAc. **Direct P. putida evidence** (Gisin 2013). Adjacent to *amgK* (likely operon). Committed step.
- **anmK — PP_0434 | Q88QQ4 | EC 2.7.1.170 (K09001).** Anhydro-MurNAc kinase; funnels the *actual* turnover product (1,6-anhydro-MurNAc) into the route. KEGG ortholog + Borisova 2017 model. High confidence.
- **mupP — PP_1764 | Q88M11 | EC 3.1.3.105 (K22292).** MurNAc-6-P phosphatase; the essential link that connects AnmK output to AmgK input. **First characterized in P. putida** (Borisova 2017). *Caveat:* KEGG gene NAME is the generic "Phosphoglycolate phosphatase 2" and UniProt lists the gene synonym **`gph`** (HAD superfamily) — an **over-general annotation** that hides its verified recycling role; curate to EC 3.1.3.105 (UniProt already tags it peptidoglycan recycling, ECO:0000269|PubMed:28351914).
- **nagZ — PP_2145 | Q88KZ4 | EC 3.2.1.52 (K01207).** Cytoplasmic β-N-acetylglucosaminidase removing GlcNAc from imported muropeptides. Functionally validated across *Pseudomonas* as a recycling enzyme and drug target (Torrens 2019 PMID 31325363; Ho 2018 PMID 30178799). *Caveat:* its metadata **primary bucket is ppu01501 (β-lactam resistance), not ppu00520** — genuine recycling step nonetheless; the broad EC 3.2.1.52 also covers other β-hexosaminidases.

### 4b. De novo UDP-sugar synthesis — present but a **different module** (keep separate)

- **glmS PP_5409 (EC 2.6.1.16)**, **glmM PP_4716 (EC 5.4.2.10)**, **glmU PP_5411 (EC 2.3.1.157/2.7.7.23)** — de novo UDP-GlcNAc. Real, but *biosynthetic*, not recycling.
- **murA PP_0964 (EC 2.5.1.7)**, **murB PP_1904 (EC 1.3.1.98)** — de novo UDP-MurNAc. **These are exactly the steps the AmgK–MurU shortcut bypasses**; their presence does not satisfy the recycling module and vice-versa.

### 4c. Candidates that are **out of scope** for peptidoglycan recycling

`rffE`/PP_1811 (UDP-GlcNAc 2-epimerase, ECA/UDP-ManNAc), `algA`/PP_1277, `PP_1776`, `algD`/PP_1288, `algC`/PP_5288, `cpsG`/PP_1777 (alginate/GDP-mannose), `rfbA`/PP_1783 (dTDP-rhamnose/LPS), `galU`/PP_3821, `udg`/PP_2926, `galE`/PP_3129, `pgm`/PP_3578, `pgi1`/PP_1808, `pgi2`/PP_4701, `glk`/PP_1011, `PP_0501`. These co-occur in the broad amino/nucleotide-sugar map but are **not** peptidoglycan recycling and were pulled in by resolving the whole `ppu00520` bucket.

---

## 5. Gaps, ambiguities, and likely over-annotations

**Missing-from-metadata but genomically present (gap-fill):**

- **AmpG importer — PP_1355 (K08218).** Inner-membrane MFS permease for GlcNAc-anhMurNAc muropeptides; essential first cytoplasmic step. *Add to module.* (Functional importance shown in *P. aeruginosa*; ortholog transfer strong.)
- **AmpD amidase — PP_0789 (Q88PQ9, EC 3.5.1.28).** "1,6-anhydro-N-acetylmuramyl-L-alanine amidase AmpD" — the *cytoplasmic* recycling amidase releasing the stem peptide from anhydro-muropeptides. *Add to module.* **Do not confuse with the septal/division amidase AmiC (PP_4897)** or the periplasmic AmiD (PP_0130); KT2440 has ≥4 amidase paralogs (PP_0130, PP_0789, PP_2269, PP_4897) with distinct roles — only PP_0789 is the core recycling AmpD.
- **Mpl murein peptide ligase — PP_0547 (Q88QE7, EC 6.3.2.45).** Re-ligates the intact L-Ala-γ-D-Glu-*meso*-DAP tripeptide directly onto UDP-MurNAc, enabling *peptide-level* recycling. *Add to module.* (This resolves the earlier candidate_uncertain call; the KO-only probe had missed it.)
- **Lytic transglycosylases** (e.g. PP_2130 Slt K08309, PP_1036 MltF K18691) generate the 1,6-anhydro-MurNAc substrate. Upstream context; large paralog family, do not force single-gene mapping.

**Not expected in this taxon:**

- **MurQ etherase (K07106): absent in `ppu`.** No gene links to K07106. This is the mechanistic reason the *Pseudomonas* route recycles MurNAc back to the wall rather than diverting MurNAc-6-P to GlcNAc-6-P/central metabolism as in *E. coli*. Mark `murQ` **not_expected_in_target_taxon**.

**Resolved (was ambiguous):**

- **Mpl (murein peptide ligase, EC 6.3.2.45): present as PP_0547** (UniProt Q88QE7). Peptide-level recycling is therefore intact. The earlier "no ortholog" impression came from a KO-only probe (K05363 not linked); the authoritative UniProt annotation confirms presence. Lesson for curation: KO-link absence alone is not evidence of absence — confirm by protein/EC search. (My first automated KEGG probe also mis-labeled K01925 as Mpl when it is MurD, and K18691 as AmpG when it is MltF — KO-only calls need sequence confirmation.)

**Likely over-annotations / broad mappings:**

- **MupP/PP_1764** carries a generic HAD "phosphoglycolate phosphatase" name (see §4a).
- **NagZ/PP_2145** EC 3.2.1.52 is a broad β-hexosaminidase class; primary bucket mis-placed in ppu01501.
- **AmgK** "GlcNAc kinase" secondary activity broadens its GO/EC footprint.

---

## 6. Module and GO-curation recommendations

| Module step | Status | Gene(s) |
|-------------|--------|---------|
| Muropeptide import | **covered (add)** | AmpG **PP_1355** |
| GlcNAc removal | **covered** | NagZ PP_2145 |
| Peptide removal (amidase) | **covered (add)** | AmpD **PP_0789** (not AmiC PP_4897) |
| anhMurNAc → MurNAc-6-P | **covered** | AnmK PP_0434 |
| MurNAc-6-P → MurNAc | **covered** | MupP PP_1764 |
| MurNAc → MurNAc-1-P | **covered** | AmgK PP_0405 |
| MurNAc-1-P → UDP-MurNAc | **covered** | MurU PP_0406 |
| MurNAc-6-P → GlcNAc-6-P (catabolic) | **not_expected_in_target_taxon** | MurQ (none) |
| Stem-peptide re-ligation | **covered (add)** | Mpl **PP_0547** |
| de novo UDP-MurNAc (MurA/MurB) | **module_needs_revision** — separate module | PP_0964, PP_1904 |

**Boundary verdict:** the generic `ppu00520` bucket is **too broad** for this review. Recommend a **dedicated "peptidoglycan/MurNAc recycling (AmgK–MurU shortcut)" module** for *Pseudomonas*, containing AmpG (PP_1355), NagZ (PP_2145), AmpD (PP_0789), AnmK (PP_0434), MupP (PP_1764), AmgK (PP_0405), MurU (PP_0406), and Mpl (PP_0547); explicitly excluding MurA/MurB (de novo) and the unrelated nucleotide-sugar genes; and explicitly recording MurQ as **absent** in the lineage.

**GO-curation flags:** the newer EC activities — **AmgK 2.7.1.221**, **MurU 2.7.7.99**, **MupP 3.1.3.105**, **AnmK 2.7.1.170** — should be checked for precise GO molecular-function terms; MupP's specific "MurNAc-6-phosphate phosphatase activity" and MurU's "MurNAc-1-phosphate uridylyltransferase activity" are the most likely to need term requests or tightened mappings. Recommend GO annotations with experimental evidence codes for AmgK/MurU/MupP citing PMIDs 23831760 and 28351914.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_0405 amgK**, **PP_0406 murU**, **PP_1764 mupP** — direct *P. putida* experimental evidence; highest-value, curate with EXP GO codes.
2. **PP_0434 anmK**, **PP_2145 nagZ** — confirm EC/GO and fix bucket placement (NagZ).
3. **PP_1355 (AmpG)**, **PP_0789 (AmpD)**, and **PP_0547 (Mpl)** — add to module. For AmpD, distinguish from the amidase paralogs AmiD (PP_0130), AmiC (PP_4897), and PP_2269, which serve periplasmic/septal (not recycling) roles.

---

## 8. Key references

- **Gisin, Schneider, Nägele, Borisova, Mayer (2013).** *A cell wall recycling shortcut that bypasses peptidoglycan de novo biosynthesis.* Nat Chem Biol. **PMID 23831760.** — Direct characterization of AmgK & MurU in *P. putida*; intrinsic fosfomycin resistance.
- **Borisova, Gisin, Mayer (2017).** *[Blocking peptidoglycan recycling / MurNAc recycling routes; MupP characterization].* mBio. **PMID 28351914.** — MupP (MurNAc-6-P phosphatase) first described in *P. putida*; two recycling routes.
- **Torrens, Sánchez-Diener, Jordana-Lluch, Barceló, Zamorano, Juan, Oliver (2019).** *In vivo validation of peptidoglycan recycling as a target…* **PMID 31325363.** — AmpG/NagZ recycling functional in *Pseudomonas*.
- **Ho, Winogrodzki, Debowski, Madden, Vocadlo, Mark, Stubbs (2018).** *Mechanism-based NagZ inactivator reverses β-lactam resistance in P. aeruginosa.* **PMID 30178799.**
- **Barceló et al. (2022) PMID 35171032; Juan et al. (2017) PMID 29029112** — recycling–resistance–virulence interplay (broader *Pseudomonas*).
- **KEGG / UniProt** for `ppu` (rest.kegg.jp; UniProt UP000000556): amgK PP_0405/K07102; murU PP_0406/K00992; anmK PP_0434/K09001; mupP PP_1764/K22292; nagZ PP_2145/K01207; ampG PP_1355/K08218; **ampD PP_0789** (Q88PQ9, EC 3.5.1.28); **mpl PP_0547** (Q88QE7, EC 6.3.2.45); murQ (K07106) — no `ppu` gene. Amidase paralogs: AmiD PP_0130, AmiC PP_4897, PP_2269.

---

### Uncertainty & species-transfer notes

- **Direct for KT2440:** AmgK, MurU (enzymology in *P. putida*); MupP (discovery in *P. putida*).
- **Strong transfer / ortholog-confirmed:** AnmK, NagZ, AmpG, AmpD (KEGG orthologs in `ppu`; functional data largely from *P. aeruginosa*, same PGN chemistry).
- **Regulatory caveat:** the recycling→AmpC-β-lactamase induction circuit is well established in *P. aeruginosa*; *P. putida* KT2440 is environmental and its β-lactamase regulation is less characterized, so do **not** transfer the resistance-induction phenotype uncritically to KT2440. The *metabolic* recycling module, however, transfers well.
- **Open experiments / expert questions:** (i) test whether Δ*mupP* or Δ*amgK* abolishes MurNAc recycling and restores fosfomycin susceptibility in KT2440 *specifically* (current fosfomycin-resistance rationale is from the heterologous *E. coli* engineering in Gisin 2013); (ii) confirm AmpG (PP_1355) is the physiological muropeptide importer in KT2440 vs. an Opp-type peptide transporter; (iii) clarify the division of labour among the four amidase paralogs (PP_0130/PP_0789/PP_2269/PP_4897); (iv) determine whether the environmental strain KT2440 couples recycling to any β-lactamase induction, given its divergence from clinical *P. aeruginosa*.


## Artifacts

- [OpenScientist final report](PSEPK__peptidoglycan-recycling__ppu00520-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__peptidoglycan-recycling__ppu00520-deep-research-openscientist_artifacts/final_report.pdf)