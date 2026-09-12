---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T12:30:42.095390'
end_time: '2026-08-08T12:50:36.233855'
duration_seconds: 1194.14
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: alginate_o_acetylation
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00543
  pathway_id: ppu00543
  pathway_name: Exopolysaccharide biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00543 with 11 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '11'
  candidate_genes: '- PP_0228: PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30)
    (EC 2.3.1.30; primary bucket kegg:ppu00543)

    - cysE: PP_0840 | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - PP_1110: PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)

    - algF: PP_1278 | Q88ND4 | Alginate biosynthesis protein AlgF (primary bucket
    kegg:ppu00543)

    - algJ: PP_1279 | Q88ND3 | Probable alginate O-acetylase AlgJ (EC 2.3.1.-) (Alginate
    biosynthesis protein AlgJ) (EC 2.3.1.-; primary bucket kegg:ppu00543)

    - algI: PP_1280 | Q88ND2 | Probable alginate O-acetylase AlgI (EC 2.3.1.-) (Alginate
    biosynthesis protein AlgI) (EC 2.3.1.-; primary bucket kegg:ppu00543)

    - algX: PP_1282 | Q88ND0 | Alginate biosynthesis protein AlgX (Probable alginate
    O-acetyltransferase AlgX) (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00543)

    - alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket
    kegg:ppu00543)

    - alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-;
    primary bucket kegg:ppu00543)

    - PP_2124: PP_2124 | Q88L13 | Glycosyl transferase (primary bucket kegg:ppu00543)

    - PP_3136: PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30;
    primary bucket kegg:ppu00543)'
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__alginate-o-acetylation__ppu00543-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__alginate-o-acetylation__ppu00543-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

alginate_o_acetylation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00543
- Resolved ID: ppu00543
- Resolved name: Exopolysaccharide biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00543 with 11 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 11

- PP_0228: PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- cysE: PP_0840 | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- PP_1110: PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)
- algF: PP_1278 | Q88ND4 | Alginate biosynthesis protein AlgF (primary bucket kegg:ppu00543)
- algJ: PP_1279 | Q88ND3 | Probable alginate O-acetylase AlgJ (EC 2.3.1.-) (Alginate biosynthesis protein AlgJ) (EC 2.3.1.-; primary bucket kegg:ppu00543)
- algI: PP_1280 | Q88ND2 | Probable alginate O-acetylase AlgI (EC 2.3.1.-) (Alginate biosynthesis protein AlgI) (EC 2.3.1.-; primary bucket kegg:ppu00543)
- algX: PP_1282 | Q88ND0 | Alginate biosynthesis protein AlgX (Probable alginate O-acetyltransferase AlgX) (EC 2.3.1.-) (EC 2.3.1.-; primary bucket kegg:ppu00543)
- alg44: PP_1286 | Q88NC6 | Alginate biosynthesis protein Alg44 (primary bucket kegg:ppu00543)
- alg8: PP_1287 | Q88NC5 | Glycosyltransferase alg8 (EC 2.4.-.-) (EC 2.4.-.-; primary bucket kegg:ppu00543)
- PP_2124: PP_2124 | Q88L13 | Glycosyl transferase (primary bucket kegg:ppu00543)
- PP_3136: PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) (EC 2.3.1.30; primary bucket kegg:ppu00543)

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

# Module/Pathway/Taxon Review: Alginate O-Acetylation in *Pseudomonas putida* KT2440

**Review topic:** `alginate_o_acetylation` — KEGG bucket `ppu00543` ("Exopolysaccharide biosynthesis")
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module area:** other_kegg_pathway · **Candidate gene count:** 11

---

## Summary

The alginate O-acetylation module is **COVERED and fully satisfiable** in *Pseudomonas putida* KT2440. All four canonical machinery components required to O-acetylate the alginate polymer — **AlgI** (PP_1280 / Q88ND2), **AlgJ** (PP_1279 / Q88ND3), **AlgF** (PP_1278 / Q88ND4), and **AlgX** (PP_1282 / Q88ND0) — are present in the candidate list, correctly named, and sit in the expected syntenic positions within a complete *algD* biosynthesis operon (PP_1277–PP_1288). This operon reproduces the *P. aeruginosa* gene order exactly, and the KT2440 *alg* cluster is experimentally functional (its deletion reduces biofilm-mediated drought resilience). O-acetylation is therefore biologically plausible in the target strain, not merely a homology transfer.

Two categories of candidate genes are **not** part of the alginate O-acetylation machinery and are artifacts of a coarse KEGG bucket. The four "serine O-acetyltransferase / serine acetyltransferase (EC 2.3.1.30)" entries — **PP_0228, cysE/PP_0840, PP_1110, and PP_3136** — catalyze the committed step of cysteine biosynthesis (L-serine + acetyl-CoA → O-acetyl-L-serine), which is mechanistically and structurally unrelated to polymer O-acetylation. They were pooled into `ppu00543` by a generic "O-acetyltransferase" grouping and represent **over-propagated annotation**. **PP_2124** ("glycosyl transferase") lies outside the *alg* operon and is an ambiguous, non-specific glycosyltransferase that should not be counted toward alginate biosynthesis. Together, five of eleven candidates (45%) are off-pathway or ambiguous.

The single most important open question is that **no direct biochemical demonstration of alginate O-acetylation exists in *P. putida* KT2440**. The COVERED assignment rests on genomic completeness (a full syntenic *algI/J/F/X* operon), a functional *alg* cluster with a documented phenotype, and strong homology transfer from *P. aeruginosa*, where isogenic knockouts and catalytic-triad mutants directly establish each gene's role. A strain-specific FT-IR or NMR acetylation assay on purified KT2440 alginate — or an isogenic *algX*/*algI* knockout — would convert this from a strong inference into a direct demonstration.

---

## Key Findings

### F001 — The AlgI/AlgJ/AlgF/AlgX O-acetylation machinery is present and satisfiable in KT2440

All four canonical O-acetylation genes appear in the KT2440 candidate list mapped to the *alg* operon: **algF** (PP_1278 / Q88ND4), **algJ** (PP_1279 / Q88ND3), **algI** (PP_1280 / Q88ND2), and **algX** (PP_1282 / Q88ND0). The functional roles are anchored by direct genetics in *P. aeruginosa*: isogenic knockouts of *algI*, *algJ*, and *algF* each yield O-acetylation-negative alginate ([PMID: 12003941](https://pubmed.ncbi.nlm.nih.gov/12003941/), [PMID: 8636017](https://pubmed.ncbi.nlm.nih.gov/8636017/)), and site-specific mutation of the AlgX Ser-His-Asp catalytic triad abolishes acetylation in vivo ([PMID: 23779107](https://pubmed.ncbi.nlm.nih.gov/23779107/)). AlgI, AlgJ, and AlgF form a complex that acts together with AlgX ([PMID: 31900562](https://pubmed.ncbi.nlm.nih.gov/31900562/)). Because the KT2440 genes are syntenic orthologs in a complete operon, transfer of this model is **strong**.

### F002 — The four EC 2.3.1.30 serine O-acetyltransferases are over-propagated cysteine-biosynthesis annotations

PP_0228 (Q88RA5), cysE/PP_0840 (Q88PL0), PP_1110 (Q88NU4), and PP_3136 (Q88I65) are all annotated serine O-acetyltransferase / serine acetyltransferase (EC 2.3.1.30). EC 2.3.1.30 catalyzes L-serine + acetyl-CoA → O-acetyl-L-serine, the committed step of cysteine biosynthesis (KEGG ppu00920, sulfur/cysteine metabolism). This reaction is mechanistically and structurally unrelated to alginate polymer O-acetylation, which uses the SGNH-hydrolase and MBOAT-like AlgI/J/F/X proteins — **none of which carry EC 2.3.1.30**. Their inclusion in `ppu00543` reflects a generic "O-acetyltransferase" EC/GO grouping, not alginate involvement. *cysE*/PP_0840 is the canonical cysteine-pathway enzyme; the other three are CysE paralogs (a cysteine-pathway curation question orthogonal to alginate).

### F003 — KT2440 carries a functional alginate (*alg*) exopolysaccharide gene cluster

Mekureyaw et al. 2026 used KT2440 mutants "Alg" (single *alg* EPS cluster deleted) and "Q" (four EPS clusters *alg*, *bcs*, *pea*, *peb* deleted); loss of the *alg* cluster reduced biofilm-mediated drought resilience, demonstrating the KT2440 *alg* cluster is functional and expressed ([PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/)). Related *P. putida* strain XMS-1 shows *algD* and *algB* are functional sodium-alginate biosynthesis genes ([PMID: 41633212](https://pubmed.ncbi.nlm.nih.gov/41633212/), [PMID: 40602902](https://pubmed.ncbi.nlm.nih.gov/40602902/)). The genuine *alg* operon members are PP_1278–PP_1287 (algF, algJ, algI, algX, alg44, alg8).

### F004 — KT2440 encodes the complete canonical *algD* operon in *P. aeruginosa* gene order

UniProt mapping (taxon 160488) of the locus range establishes the full operon: PP_1288 *algD* (GDP-mannose 6-dehydrogenase, Q88NC4), PP_1287 *alg8* (glycosyltransferase), PP_1286 *alg44*, PP_1285 *algK*, PP_1284 *algE*, PP_1283 *algG* (mannuronan C5-epimerase), PP_1282 *algX*, PP_1281 *algL* (alginate lyase), PP_1280 *algI*, PP_1279 *algJ*, PP_1278 *algF*, PP_1277 *algA*. This is the full *P. aeruginosa algD* operon order (algD-alg8-alg44-algK-algE-algG-algX-algL-algI-algJ-algF-algA), transcribed opposite to locus numbering. The KEGG `ppu00543` candidate bucket captured only **6/12** operon genes (algF, algJ, algI, algX, alg44, alg8); algD, algA, algK, algE, algG, and algL are present in the genome but absent from the candidate list because they sit in other KEGG maps — a bucketing artifact, not a biological gap.

### F005 — KT2440 O-acetylation is inferred from synteny/homology; no direct biochemical demonstration exists (open question)

Targeted PubMed searches for *P. putida*/environmental-strain alginate O-acetylation returned no strain-specific biochemical study. The functional importance of alginate O-acetylation is established in *P. aeruginosa*: FT-IR shows the O-acetyl ester band (~1250 cm⁻¹) in mucoid biofilms and its loss in non-acetylating strains, with acetylation required for microcolony/biofilm formation ([PMID: 11208804](https://pubmed.ncbi.nlm.nih.gov/11208804/)). The SGNH-hydrolase acetyltransferase paradigm (AlgX/AlgJ) generalizes to related *Pseudomonas* EPS acetylation systems (e.g., cellulose WssI in *P. fluorescens*; [PMID: 37224964](https://pubmed.ncbi.nlm.nih.gov/37224964/)). KT2440 evidence remains genomic (complete syntenic algI/J/F/X operon) plus phenotypic (functional *alg* cluster).

---

## Mechanistic Model / Interpretation

Alginate O-acetylation is a **post-polymerization periplasmic modification**: acetyl groups are added at the **O-2 and/or O-3 positions of D-mannuronate residues** after the polymer is synthesized and translocated across the inner membrane. Critically, loss of the acetylation genes does **not** affect polymer synthesis or C-5 epimerization — only the acetylation state changes ([PMID: 8636017](https://pubmed.ncbi.nlm.nih.gov/8636017/)).

```
 CYTOPLASM        |   INNER MEMBRANE   |            PERIPLASM
                  |                    |
 acetyl donor ----|---►  AlgI (7-TM)  =|=►  acetyl-group relay
                  |   (MBOAT-like)     |          │
                  |                    |          ▼
                  |             AlgJ (SGNH, D-H-S triad) ── acetylesterase / relay
                  |                    |          │
                  |             AlgF (periplasmic accessory, links to secretion)
                  |                    |          │
                  |                    |          ▼
   GDP-mannuronate ─► Alg8/Alg44 ─► [ M-M-M-M polymer ] ─► AlgX (SGNH + CBM)
   (AlgA, AlgD)      (polymerize)                            = TERMINAL acetyltransferase
                                                             adds O-acetyl to mannuronate
                                                             + shields polymer from AlgL lyase
```

The KT2440 operon reproduces this architecture gene-for-gene. The step-to-gene mapping is unambiguous:

| Step | Function | Gene | KT2440 locus | UniProt | Call |
|------|----------|------|--------------|---------|------|
| A1 | Acetyl translocation across inner membrane | *algI* | PP_1280 | Q88ND2 | **covered** |
| A2 | Periplasmic acetylesterase / relay (SGNH) | *algJ* | PP_1279 | Q88ND3 | **covered** |
| A3 | Periplasmic accessory, links to secretion | *algF* | PP_1278 | Q88ND4 | **covered** |
| A4 | Terminal polymer O-acetyltransferase (SGNH+CBM) | *algX* | PP_1282 | Q88ND0 | **covered** |

**Interpretation for curation:** the module is COVERED. The two SGNH proteins have distinct roles — AlgJ exhibits acetylesterase activity but weak/no polymer binding, whereas AlgX binds polymannuronate length-dependently and is the terminal transferase ([PMID: 25165982](https://pubmed.ncbi.nlm.nih.gov/25165982/)). The `ppu00543` bucket should be split into three curation groups: (1) alginate O-acetylation (AlgI/J/F/X), (2) alginate precursor/polymerization (Alg8, Alg44, and off-map AlgD/A/K/E/G/L), and (3) cysteine-pathway serine acetyltransferases (which must be removed to ppu00920).

---

## Candidate Genes and Evidence

### High-confidence alginate O-acetylation genes (keep / promote)

| Gene | Locus | UniProt | Role | Evidence type | Transfer strength | Caveat |
|------|-------|---------|------|---------------|-------------------|--------|
| AlgI | PP_1280 | Q88ND2 | Inner-membrane acetyl translocase | Homology + synteny; *P. aeruginosa* Δ*algI* → non-acetylated | Strong | EC 2.3.1.- deliberately vague; don't assign specific EC |
| AlgJ | PP_1279 | Q88ND3 | SGNH acetylesterase / relay | Homology + synteny; Δ*algJ* → non-acetylated | Strong | In-vitro esterase vs in-vivo relay distinction |
| AlgF | PP_1278 | Q88ND4 | Periplasmic accessory | Homology + synteny; complex member | Strong | No catalytic EC; keep descriptive |
| AlgX | PP_1282 | Q88ND0 | Terminal polymer O-acetyltransferase | Homology + synteny; triad mutants abolish acetylation | Strong | Dual role (transferase + AlgL protection) |

### Polymerization-context candidates (in bucket, not O-acetylation)

**Alg44 — PP_1286 (Q88NC6)** and **Alg8 — PP_1287 (Q88NC5, EC 2.4.-.-)** are genuine *alg* operon members involved in polymerization/co-polymerase function, not acetylation. They belong in the exopolysaccharide bucket but under the **polymerization** step, not the acetylation sub-module.

### Likely over-propagated / off-pathway candidates (exclude from module)

| Gene | Locus | UniProt | Annotation | Verdict |
|------|-------|---------|-----------|---------|
| PP_0228 | PP_0228 | Q88RA5 | Serine O-acetyltransferase EC 2.3.1.30 | **Over-propagated — cysteine biosynthesis** |
| cysE | PP_0840 | Q88PL0 | Serine O-acetyltransferase EC 2.3.1.30 | **Over-propagated — canonical CysE** |
| PP_1110 | PP_1110 | Q88NU4 | Serine O-acetyltransferase EC 2.3.1.30 | **Over-propagated — cysteine biosynthesis** |
| PP_3136 | PP_3136 | Q88I65 | Serine acetyltransferase EC 2.3.1.30 | **Over-propagated — cysteine biosynthesis** |
| PP_2124 | PP_2124 | Q88L13 | Glycosyl transferase (generic) | **Ambiguous — non-operon, reassign** |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges findings |
|------|-----------------|----------------------------------------|
| [8636017](https://pubmed.ncbi.nlm.nih.gov/8636017/) | Identification of *algI*/*algJ* required for O-acetylation | Isogenic *algI/algJ/algF* knockouts → non-acetylated alginate; polymer synthesis & C-5 epimerization unaffected — defines the acetylation genes. |
| [12003941](https://pubmed.ncbi.nlm.nih.gov/12003941/) | Mutant analysis & localization of AlgI/AlgJ/AlgF | AlgI/J/F essential for O-acetylation; localization supports periplasmic polymer-level modification. |
| [23779107](https://pubmed.ncbi.nlm.nih.gov/23779107/) | AlgX structure & role in acetylation | Site-specific catalytic-triad mutation → non-acetylated alginate in vivo; AlgX is a required acetyltransferase. |
| [25165982](https://pubmed.ncbi.nlm.nih.gov/25165982/) | AlgJ & AlgX SGNH topology, distinct roles | AlgX is terminal, polymer-binding transferase; AlgJ has esterase activity but weak polymer binding. |
| [31900562](https://pubmed.ncbi.nlm.nih.gov/31900562/) | Analysis of the acetylation machinery | AlgI+AlgJ+AlgF form a complex acting with AlgX — defines the four-protein machinery. |
| [15231808](https://pubmed.ncbi.nlm.nih.gov/15231808/) | *algI/algJ* cassette lateral transfer | AlgI/type-II-membrane cassette is a broad EPS-esterification family — supports homology transfer with caveats. |
| [11208804](https://pubmed.ncbi.nlm.nih.gov/11208804/) | Role of alginate O-acetylation in biofilms | FT-IR O-acetyl band (~1250 cm⁻¹); acetylation required for microcolony/biofilm formation — defines the direct assay for KT2440. |
| [41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/) | KT2440 biofilm & drought resilience | KT2440 *alg* EPS cluster deletion reduces biofilm/drought resilience — direct evidence the cluster is functional/expressed. |
| [41633212](https://pubmed.ncbi.nlm.nih.gov/41633212/), [40602902](https://pubmed.ncbi.nlm.nih.gov/40602902/) | *P. putida* XMS-1 *algD*/*algB* | Functional alginate biosynthesis in related *P. putida* strain — supports species-level alginate production. |
| [37224964](https://pubmed.ncbi.nlm.nih.gov/37224964/) | WssI cellulose O-acetyltransferase | SGNH-acetyltransferase paradigm generalizes across *Pseudomonas* EPS systems. |

**Key verbatim support:**
- [PMID: 12003941](https://pubmed.ncbi.nlm.nih.gov/12003941/): *"the algF, algJ, and algI genes are known to be essential for the addition of O-acetyl groups to alginate."*
- [PMID: 23779107](https://pubmed.ncbi.nlm.nih.gov/23779107/): *"In vivo studies reveal that site-specific mutation of these residues results in non-acetylated alginate."*
- [PMID: 31900562](https://pubmed.ncbi.nlm.nih.gov/31900562/): *"Three proteins, AlgI, AlgJ and AlgF have been implicated to form a complex and act together with AlgX for O-acetylation of alginate."*
- [PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/): *"biofilm-deficient mutants KT2440 Alg, with only one gene cluster for the exopolysaccharide alginate deleted … were used."*
- [PMID: 11208804](https://pubmed.ncbi.nlm.nih.gov/11208804/): *"1,250 cm(-1) (C---O stretching of the O-acetyl group in alginate)."*

---

## Module and GO-Curation Recommendations

| Module step | Gene(s) | Call |
|-------------|---------|------|
| AlgI acetyl translocation | PP_1280 | **covered** |
| AlgJ acetylesterase relay | PP_1279 | **covered** |
| AlgF accessory | PP_1278 | **covered** |
| AlgX polymer O-acetyltransferase | PP_1282 | **covered** |
| Serine O-acetyltransferases ×4 (EC 2.3.1.30) | PP_0228, PP_0840, PP_1110, PP_3136 | **not_expected_in_target_taxon** (mis-bucketed → ppu00920 cysteine biosynthesis) |
| Generic glycosyltransferase | PP_2124 | **candidate_uncertain** (reassign to correct EPS system) |
| Overall `ppu00543` bucket boundary | — | **module_needs_revision** — split acetylation from precursor/polymerization/cysteine content |

**GO / EC notes:** For AlgX use a specific "alginate/polysaccharide O-acetyltransferase activity" GO term rather than a generic acetyltransferase term; keep AlgF as a non-catalytic component (no EC). Do **not** apply EC 2.3.1.30 (serine O-acetyltransferase) to any *alg* gene. A dedicated **alginate O-acetylation module document** (algI/J/F/X, with the polymerization scaffold as context) is warranted, because the generic exopolysaccharide bucket conflates unrelated acetyltransferases. No new GO-term request appears necessary; existing alginate-acetylation terms suffice.

---

## Genes to Promote to Full `fetch-gene` Review

1. **AlgX — PP_1282 (Q88ND0):** the catalytic transferase + AlgL-protection dual role; highest curation value; confirm SGNH triad and C-terminal CBM.
2. **AlgI — PP_1280 (Q88ND2):** verify MBOAT-family seven-TM topology and membrane localization; keep EC generic.
3. **AlgJ — PP_1279 (Q88ND3):** confirm SGNH Asp-His-Ser triad; distinguish in-vitro esterase vs in-vivo relay role.
4. **AlgF — PP_1278 (Q88ND4):** confirm non-catalytic accessory annotation; note coupling to the secretion complex.
5. **PP_2124 (Q88L13):** resolve which EPS system it belongs to; remove from the alginate bucket if unrelated.
6. *(Lower priority — cysteine-pathway hygiene)* **cysE/PP_0840, PP_0228, PP_1110, PP_3136:** confirm as CysE + paralogs and strip from `ppu00543`.

---

## Limitations and Knowledge Gaps

1. **No KT2440-direct acetylation biochemistry.** The COVERED call is an inference. Every mechanistic knockout/mutant result derives from *P. aeruginosa*; transfer to KT2440 is **strong** (identical operon synteny, conserved gene names, functional cluster phenotype) but not experimentally confirmed in the target strain. This is the single most important open question.
2. **AlgX dual-function uncertainty.** In *P. aeruginosa*, AlgX has both acetyltransferase and periplasmic scaffolding/polymer-protection roles; which dominates in KT2440 is unresolved.
3. **Regulation and expression conditions.** KT2440 is non-mucoid relative to CF *P. aeruginosa*; whether the *algD* operon is expressed under standard laboratory conditions affects the in vivo relevance of acetylation.
4. **Bucket incompleteness.** Six of twelve operon genes were absent from the candidate list (routed to other KEGG maps); a complete satisfiability audit of the broader EPS bucket requires pulling in the off-map genes (algD, algA, algK, algE, algG, algL).

---

## Proposed Follow-up Experiments / Actions

1. **Direct acetylation assay (highest value):** Purify alginate from KT2440 under alg-inducing conditions and run FT-IR for the ~1250 cm⁻¹ O-acetyl ester band and/or ¹H-NMR for O-2/O-3 acetyl signals — directly confirms or refutes O-acetylation ([PMID: 11208804](https://pubmed.ncbi.nlm.nih.gov/11208804/)).
2. **Isogenic knockouts:** Construct KT2440 Δ*algX* and Δ*algJ*; assay acetylation loss to confirm functional transfer of the *P. aeruginosa* model.
3. **Sequence/structure review:** Full `fetch-gene` review of PP_1282 (AlgX) and PP_1279 (AlgJ) to confirm the SGNH Ser/Asp-His-Ser catalytic triads are conserved.
4. **Bucket curation:** Split `ppu00543` into acetylation, polymerization/precursor, and cysteine subgroups; reassign the four EC 2.3.1.30 genes to ppu00920; flag PP_2124 as candidate_uncertain.
5. **Expression check:** Query KT2440 transcriptomic/proteomic datasets to determine whether the *algD* operon is expressed under relevant (desiccation/biofilm) conditions.

---

### Bottom line for curation

Mark **alginate_o_acetylation COVERED** in *P. putida* KT2440: AlgI (PP_1280), AlgJ (PP_1279), AlgF (PP_1278), and AlgX (PP_1282) are all present, correctly named, and syntenic within a complete, experimentally functional *algD* operon. Reclassify the four EC 2.3.1.30 serine O-acetyltransferases (PP_0228, cysE/PP_0840, PP_1110, PP_3136) as cysteine biosynthesis (not_expected_in_target_taxon here), flag PP_2124 as uncertain, and revise the `ppu00543` bucket to separate the alginate acetylation subset from precursor/polymerization and unrelated cysteine content. The key remaining gap is the absence of any direct biochemical proof of acetylation in KT2440.


## Artifacts

- [OpenScientist final report](PSEPK__alginate-o-acetylation__ppu00543-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__alginate-o-acetylation__ppu00543-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12003941
2. PMID:8636017
3. PMID:23779107
4. PMID:31900562
5. PMID:41554215
6. PMID:41633212
7. PMID:40602902
8. PMID:11208804
9. PMID:37224964
10. PMID:25165982