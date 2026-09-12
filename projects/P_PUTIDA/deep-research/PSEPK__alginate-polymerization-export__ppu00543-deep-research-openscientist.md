---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T12:04:04.328299'
end_time: '2026-08-08T13:03:32.015325'
duration_seconds: 3567.7
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: alginate_polymerization_export
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
citation_count: 12
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__alginate-polymerization-export__ppu00543-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__alginate-polymerization-export__ppu00543-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

alginate_polymerization_export in Pseudomonas putida KT2440

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

# Module/Pathway/Taxon Review: alginate_polymerization_export in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI taxon 160488, proteome UP000000556)
**Target bucket:** KEGG ppu00543 "Exopolysaccharide biosynthesis" (11 primary candidate genes)
**Module reviewed:** alginate_polymerization_export
**Review type:** Species-aware manual satisfiability and annotation-curation review · 2026-08-08

---

## Summary

The **alginate_polymerization_export module is SATISFIED and functional** in *Pseudomonas putida* KT2440. The genome carries a single, contiguous alginate biosynthesis operon, **PP_1277–PP_1288**, that encodes one-to-one orthologs of every canonical polymerization and export step: the inner-membrane glycosyltransferase Alg8, the c-di-GMP–responsive copolymerase Alg44, the periplasmic scaffold proteins AlgK and AlgX, the mannuronan C5-epimerase AlgG, the alginate lyase AlgL, the O-acetylation machinery AlgI/AlgJ/AlgF, and the outer-membrane export porin AlgE. Precursor synthesis (AlgA, AlgD) and an AlgC-type phosphomannomutase are also present. The module can be marked **covered** with high confidence, with mechanism transferred from the essentially fully orthologous *P. aeruginosa* machinery.

**The commissioned KEGG ppu00543 candidate list is, however, a poor proxy for the module and must be corrected.** Of the 11 candidate genes, only 6 are genuine alginate genes. The bucket **omits four essential module genes** that are present in the genome (algL/PP_1281, algG/PP_1283, algE/PP_1284, algK/PP_1285) and **includes five over-propagated non-alginate candidates**: the four serine O-acetyltransferase / CysE proteins PP_0228, PP_0840 (cysE), PP_1110, PP_3136 (EC 2.3.1.30, cysteine biosynthesis, KO K00640), plus PP_2124 (KO K21001 = PslH, a distinct Psl-type EPS system). These over-propagations arise because KEGG map 00543 aggregates all EPS-related O-acetyl and glycosyltransferase activities, which sweeps in unrelated enzymes that share an EC number or a generic KO.

Functionally, the machinery is not merely a genomic relic. Direct experiments in *P. putida* show total EPS and alginate production increase specifically under **matric (water-limiting) stress**, that an *algD* mutant forms structurally altered biofilms with reduced desiccation survival, and that the single KT2440 *alg* cluster contributes to drought-protective biofilm formation on plants. The recommended curation action is: mark the module **covered**, **add** the four missing *alg* genes, **drop** the five over-propagated candidates, and promote the four newly added genes plus AlgX to full `fetch-gene` review.

---

## Target-Organism Pathway Definition

### What the pathway includes

The alginate_polymerization_export module covers the **membrane and periplasmic steps that convert the activated nucleotide-sugar precursor GDP-mannuronate into secreted, chemically modified alginate polymer.** In the synthase-dependent (Wzx/Wzy-independent) secretion paradigm used by *Pseudomonas*, this is a single envelope-spanning multiprotein complex that performs:

1. **Polymerization** at the inner membrane — Alg8 (GT2 glycosyltransferase) catalyzes β-1,4 linkage of mannuronate units, activated post-translationally by the copolymerase Alg44, whose PilZ domain binds c-di-GMP.
2. **Periplasmic guidance/scaffolding** — AlgK (TPR lipoprotein) and AlgX bridge the periplasm and pre-orient the nascent chain for export; AlgX additionally acts as an SGNH O-acetyltransferase.
3. **Epimerization** — AlgG, the mannuronan C5-epimerase, converts β-D-mannuronate (M) to α-L-guluronate (G), tuning polymer mechanics.
4. **Chain-length/quality control** — AlgL, a periplasmic alginate lyase, degrades mislocalized polymer and protects the periplasm.
5. **O-acetylation** — AlgI (integral membrane), AlgJ and AlgF add O-acetyl groups to mannuronate residues, protecting alginate from lyase degradation and modulating biofilm architecture.
6. **Outer-membrane export** — AlgE, an 18-stranded β-barrel porin, translocates the polyanionic chain across the outer membrane.

### Neighboring processes to keep separate

- **Precursor biosynthesis (fructose-6-P → GDP-mannuronate):** AlgA (PP_1277, Man-6-P isomerase / Man-1-P guanylyltransferase), AlgC-type phosphomannomutase (PP_1777, PP_5288, KO K15778), and AlgD (PP_1288, GDP-mannose 6-dehydrogenase). AlgC is pleiotropic (shared with LPS biosynthesis) and lies outside the cluster.
- **Cysteine biosynthesis (serine → O-acetyl-serine):** the CysE serine O-acetyltransferases (EC 2.3.1.30). These are the over-propagation source.
- **Regulation:** AlgU/AlgT (σ22), MucABCD, AlgR, and c-di-GMP turnover (e.g., PP_4959). Not part of the structural module.
- **Other KT2440 EPS systems:** Psl (PP_2124/PslH), cellulose (*bcs*), and the c-di-GMP-induced surface polysaccharide cluster PP3133–PP3141. KEGG map00543 lumps all EPS together; alginate must be resolved out.

### Alternate names / database definitions

KEGG defines the bucket as **map00543 "Exopolysaccharide biosynthesis"** — a broad aggregate map, NOT an alginate-specific module; there is no dedicated alginate KEGG module, which is the root cause of the mismatch. The alginate genes follow the canonical *P. aeruginosa* operon naming **algD-8-44-K-E-G-X-L-I-J-F-A**; in KT2440 the operon is the **reverse-strand mirror** running PP_1277 (algA) → PP_1288 (algD). UniProt uses "Alginate biosynthesis protein" descriptors for most members.

---

## Expected Step Model

| Step | Function | Enzyme | KT2440 locus | UniProt | KO | In bucket? |
|------|----------|--------|--------------|---------|-----|-----------|
| Precursor | Man-6-P isomerase / Man-1-P guanylyltransferase | AlgA | PP_1277 | — | K16011 | No (flanking) |
| O-acetylation | Alginate O-acetyl accessory | AlgF | PP_1278 | Q88ND4 | K19296 | **Yes** |
| O-acetylation | Alginate O-acetylase (SGNH) | AlgJ | PP_1279 | Q88ND3 | K19295 | **Yes** |
| O-acetylation | Alginate O-acetylase (membrane) | AlgI | PP_1280 | Q88ND2 | K19294 | **Yes** |
| Quality control | Alginate lyase | AlgL | PP_1281 | Q88ND1 | K01729 | *Missing* |
| Scaffold / O-acetyl | Periplasmic O-acetyltransferase (SGNH) | AlgX | PP_1282 | Q88ND0 | K19293 | **Yes** |
| Epimerization | Mannuronan C5-epimerase | AlgG | PP_1283 | Q88NC9 | K01795 | *Missing* |
| Export | Outer-membrane β-barrel porin | AlgE | PP_1284 | Q88NC8 | K16081 | *Missing* |
| Scaffold | Periplasmic TPR lipoprotein | AlgK | PP_1285 | Q88NC7 | K19292 | *Missing* |
| Polymerization | c-di-GMP copolymerase (PilZ) | Alg44 | PP_1286 | Q88NC6 | K19291 | **Yes** |
| Polymerization | GT2 glycosyltransferase synthase | Alg8 | PP_1287 | Q88NC5 | K19290 | **Yes** |
| Precursor | GDP-mannose 6-dehydrogenase | AlgD | PP_1288 | — | K00066 | No (flanking) |
| Precursor (ectopic) | Phosphomannomutase (AlgC-type) | AlgC | PP_1777, PP_5288 | — | K15778 | No |

**Verdict:** Every expected polymerization/export/modification step has a dedicated, contiguous ortholog. The module is genomically complete.

---

## Key Findings

### Finding 1 — The complete canonical alginate operon is present and contiguous (PP_1277–PP_1288)

KEGG/GenBank genome annotation of KT2440 shows a single contiguous *alg* cluster, **PP_1277–PP_1288**, encoding all 12 canonical alginate genes: PP_1277 *algA* (Man-6-P isomerase/Man-1-P guanylyltransferase, EC 5.3.1.8/2.7.7.13, K16011), PP_1278 *algF* (K19296), PP_1279 *algJ* (K19295), PP_1280 *algI* (K19294), PP_1281 *algL* (alginate lyase, EC 4.2.2.3, K01729), PP_1282 *algX* (K19293), PP_1283 *algG* (poly-ManA C5 epimerase, EC 5.1.3.37, K01795), PP_1284 *algE* (outer-membrane porin, K16081), PP_1285 *algK* (scaffold lipoprotein, K19292), PP_1286 *alg44* (copolymerase, K19291), PP_1287 *alg8* (GT2 polymerase, K19290), and PP_1288 *algD* (GDP-mannose 6-dehydrogenase, EC 1.1.1.132, K00066). Gene order is the reverse-strand mirror of the *P. aeruginosa* algD-8-44-K-E-G-X-L-I-J-F-A operon. Every module step therefore has a dedicated ortholog with no gaps.

This is corroborated by direct KT2440 studies. [PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) states: *"The gene clusters alg and bcs, which code for proteins mediating alginate and cellulose biosynthesis, were found to play minor roles in P. putida KT2440 biofilm formation and stability under the conditions tested"* — confirming KT2440 carries an intact *alg* cluster (its phenotypic role being condition-dependent). [PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/) describes *"biofilm-deficient mutants KT2440 Alg, with only one gene cluster for the exopolysaccharide alginate deleted"* — confirming a single, deletable-as-a-unit alginate cluster consistent with the contiguous PP_1277–PP_1288 operon.

### Finding 2 — The KEGG ppu00543 bucket omits 4 core module genes and includes 5 over-propagated candidates

The commissioned candidate list (KEGG map ppu00543) contains 11 genes but is a poor match to the module.

- **False positives / over-propagation:** PP_0228, PP_0840 (cysE), PP_1110 and PP_3136 are all serine O-acetyltransferase / CysE (EC 2.3.1.30, KO K00640) — cysteine biosynthesis enzymes mapped onto the EPS O-acetyl node; none is an alginate gene. PP_2124 (KO K21001, generic glycosyltransferase / PslH) belongs to a different EPS system.
- **Missing from the bucket but present in the genome and central to the module:** PP_1281 *algL* (lyase, K01729), PP_1283 *algG* (C5 epimerase, K01795), PP_1284 *algE* (export porin, K16081), and PP_1285 *algK* (periplasmic scaffold, K19292).
- **Genuine alginate genes correctly in the bucket:** algF (PP_1278), algJ (PP_1279), algI (PP_1280), algX (PP_1282), alg44 (PP_1286), alg8 (PP_1287).

Four CysE paralogs collapsing onto a single EPS node is a textbook signature of EC/KO over-propagation on an aggregate overview map.

### Finding 3 — UniProt independently confirms cluster functions; PP_2124 is PslH; AlgC-type PMM is ectopic

UniProt (reference proteome UP000000556) confirms each "missing-from-bucket" cluster gene: **Q88ND1 algL** = Alginate lyase (Lyase, Periplasm, Signal peptide); **Q88NC9 algG** = Mannuronan C5-epimerase (Alginate biosynthesis, Periplasm); **Q88NC8 algE** = Alginate production protein AlgE (Cell outer membrane); **Q88NC7 algK** = AlgK (Alginate biosynthesis, Lipoprotein, Palmitate, **3D-structure** cross-reference). Over-propagation candidates are confirmed non-alginate: **Q88L13 PP_2124** = "Glycosyl transferase" (keyword only "Transferase"; KO K21001 = *pslH*, mapping to map00543 EPS and map02025 biofilm — a different EPS system); **Q88PL0 cysE** = serine O-acetyltransferase (Amino-acid biosynthesis, Cytoplasm — not alginate). The precursor phosphomannomutase (AlgC-type, bifunctional PMM/PGM, KO K15778) is encoded outside the *alg* cluster at PP_1777 and PP_5288.

### Finding 4 — The machinery is functional and conditionally induced by matric/water-limiting stress

In *P. putida* (strain mt-2, the parent lineage of KT2440), total EPS and alginate production increase with matric (water-limiting) but not solute stress; an *algD* mutant forms structurally altered biofilms and shows reduced desiccation survival ([PMID: 17601783](https://pubmed.ncbi.nlm.nih.gov/17601783/)). That study reports: *"Total exopolysaccharide (EPS) and alginate production increased with increasing matric, but not solute, stress severity, and alginate was a significant component, but not the major component, of EPS,"* and *"Alginate deficiency decreased survival of desiccation not only by P. putida but also by Pseudomonas aeruginosa PAO1 and Pseudomonas syringae pv. syringae B728a."* A matric-stress genetic screen in *P. putida* independently recovered alginate-biosynthesis genes among desiccation-tolerance determinants ([PMID: 15101980](https://pubmed.ncbi.nlm.nih.gov/15101980/)). KT2440-specific work shows the single *alg* cluster contributes to biofilm stability (minor under standard lab conditions; [PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)) and to drought-protective biofilm on plants ([PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/)).

---

## Candidate Genes and Evidence

### Genuine alginate genes correctly in the bucket (retain — high confidence)

- **alg8 / PP_1287 (Q88NC5)** — GT2 alginate polymerase catalytic subunit; membrane-embedded; directly interacts with Alg44 ([PMID: 25968647](https://pubmed.ncbi.nlm.nih.gov/25968647/)). *Caveat:* broad EC 2.4.-.- placeholder — the true alginate synthase reaction lacks a clean EC.
- **alg44 / PP_1286 (Q88NC6)** — inner-membrane copolymerase with N-terminal PilZ domain; binds **dimeric c-di-GMP** to post-translationally activate polymerization ([PMID: 25817996](https://pubmed.ncbi.nlm.nih.gov/25817996/)).
- **algX / PP_1282 (Q88ND0)** — periplasmic SGNH O-acetyltransferase + chain protection; part of the AlgK–AlgX–MucD complex ([PMID: 21713511](https://pubmed.ncbi.nlm.nih.gov/21713511/)). *Caveat:* broad EC 2.3.1.- drives its bucket assignment.
- **algI / PP_1280 (Q88ND2)** — polytopic membrane O-acetylation component.
- **algJ / PP_1279 (Q88ND3)** — SGNH-family O-acetyltransferase.
- **algF / PP_1278 (Q88ND4)** — O-acetylation accessory/modulator.

### Core module genes MISSING from the bucket (add — high confidence)

- **algK / PP_1285 (Q88NC7)** — TPR lipoprotein scaffold; its loss destabilizes Alg8/Alg44 and blocks polymerization ([PMID: 23503314](https://pubmed.ncbi.nlm.nih.gov/23503314/)).
- **algE / PP_1284 (Q88NC8)** — 18-stranded β-barrel export porin; structurally solved; complexes with AlgK ([PMID: 21778407](https://pubmed.ncbi.nlm.nih.gov/21778407/), [PMID: 25084326](https://pubmed.ncbi.nlm.nih.gov/25084326/), [PMID: 23335756](https://pubmed.ncbi.nlm.nih.gov/23335756/)).
- **algG / PP_1283 (Q88NC9)** — poly-mannuronate C5-epimerase (EC 5.1.3.37); periplasmic chain modification.
- **algL / PP_1281 (Q88ND1)** — alginate lyase (EC 4.2.2.3); periplasmic quality control.

### Over-propagated / wrong-system candidates (exclude)

| Locus | UniProt | Annotation | Actual system | KO | Why over-propagated |
|-------|---------|------------|---------------|-----|--------------------|
| PP_0228 | Q88RA5 | serine O-acetyltransferase (EC 2.3.1.30) | Cysteine biosynthesis | K00640 | EC 2.3.1.30 → EPS O-acetyl node |
| PP_0840 (cysE) | Q88PL0 | serine O-acetyltransferase (EC 2.3.1.30) | Cysteine biosynthesis (cytoplasm) | K00640 | Canonical CysE; not alginate |
| PP_1110 | Q88NU4 | serine O-acetyltransferase (EC 2.3.1.30) | Cysteine biosynthesis | K00640 | EC-based mis-map |
| PP_3136 | Q88I65 | Serine acetyltransferase (EC 2.3.1.30) | Cysteine biosynthesis | K00640 | EC-based mis-map |
| PP_2124 | Q88L13 | Glycosyl transferase (generic) | Psl EPS system | K21001 (pslH) | Generic GT KO maps to map00543 + map02025 |

---

## Mechanistic Model / Interpretation

```
   Cytoplasm            Inner membrane        Periplasm              Outer membrane
   ---------            --------------        ---------              --------------
 Fru-6-P
   | AlgA (PP_1277)
 GDP-mannose
   | AlgD (PP_1288)
 GDP-mannuronate --->  [ Alg8 (PP_1287) ]==polymerize==>
                        [ Alg44(PP_1286) ]
                         ^ c-di-GMP (PilZ)
                        [ AlgI (PP_1280) ]--O-acetyl-->  AlgX (PP_1282) / AlgJ / AlgF
                                                          AlgG (PP_1283)  epimerize M->G
                                                          AlgL (PP_1281)  trim / QC
                                                          AlgK (PP_1285)  scaffold
                                                                  |
                                                                  v
                                                            [ AlgE (PP_1284) ]===> secreted alginate
```

The KT2440 machinery is the reverse-strand mirror of the *P. aeruginosa* algD-8-44-K-E-G-X-L-I-J-F-A operon. Because every subunit has a one-to-one *P. aeruginosa* ortholog, the extensive mechanistic work on the *P. aeruginosa* envelope-spanning complex — AlgE–AlgK–AlgX–Alg44–Alg8–AlgG interactions ([PMID: 23503314](https://pubmed.ncbi.nlm.nih.gov/23503314/)), c-di-GMP activation of Alg44 ([PMID: 25817996](https://pubmed.ncbi.nlm.nih.gov/25817996/)), AlgE porin gating ([PMID: 21778407](https://pubmed.ncbi.nlm.nih.gov/21778407/)), and polymerization/modification coupling ([PMID: 25968647](https://pubmed.ncbi.nlm.nih.gov/25968647/)) — transfers with **high confidence** to KT2440 at the structural/mechanistic level. Transfer of the *phenotype* (when/whether alginate is made) is more nuanced: KT2440 makes alginate **conditionally**, chiefly under water-limiting stress, rather than the constitutive mucoidy of CF-adapted *P. aeruginosa*. Presence ≠ constitutive activity; the module should be annotated as intact-but-regulated, not as a gap.

---

## Gaps, Ambiguities, and Likely Over-Annotations

1. **Bucket-vs-module mismatch (primary issue).** KEGG map00543 is a pan-EPS overview; it neither delimits alginate cleanly nor captures the AlgK/AlgE/AlgG/AlgL steps. Relying on the bucket alone would drop 4 essential steps and inject 5 non-alginate genes (6/11 precision).
2. **Broad EC/KO mappings.** algX (EC 2.3.1.-) and alg8 (EC 2.4.-.-) carry incomplete ECs; EC 2.3.1.30 (CysE) is the over-propagation source; K21001 (generic GT) pulls in PslH.
3. **Precursor boundary.** algA (PP_1277) and algD (PP_1288) flank the operon but belong to a precursor-supply module; algC (PP_1777/PP_5288) is genomically separate and pleiotropic. Whether the module includes precursor supply is a definitional choice, not a satisfiability gap.
4. **Condition-dependent expression (not a genomic gap).** The cluster is minor under standard lab conditions ([PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/)) but required for drought-protective biofilm ([PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/)) and c-di-GMP-inducible ([PMID: 21554519](https://pubmed.ncbi.nlm.nih.gov/21554519/)).
5. **No paralog ambiguity among true alg genes.** Each step = one dedicated cluster gene; ambiguity is confined to the CysE/GT over-propagations, which are unrelated.

---

## Module and GO-Curation Recommendations

| Module element / gene | Recommended status |
|------------------------|--------------------|
| alg8 (PP_1287), alg44 (PP_1286), algX (PP_1282), algI/J/F (PP_1280/1279/1278) | **covered** |
| algK (PP_1285), algE (PP_1284), algG (PP_1283), algL (PP_1281) | **covered — add to module (bucket omission corrected)** |
| algA (PP_1277), algD (PP_1288) precursor supply | **covered but out-of-scope** (assign to precursor module) |
| CysE genes PP_0228/PP_0840/PP_1110/PP_3136; PP_2124 (PslH) | **not_in_module** (over-propagation; remove) |

**Concrete curation actions:**
1. Mark the alginate_polymerization_export module **covered** for PSEPK.
2. **Add** algL (PP_1281), algG (PP_1283), algE (PP_1284), algK (PP_1285) to the module.
3. **Drop** PP_0228, PP_0840, PP_1110, PP_3136, PP_2124 (reassign CysE to cysteine biosynthesis; PP_2124 to a Psl/EPS module).
4. **module_needs_revision on the generic boundary:** create a dedicated alginate module document keyed to the **PP_1277–PP_1288 locus** rather than to KEGG ppu00543.
5. **GO curation:** ensure the added genes carry alginate-specific terms — GO:0042121 (alginic acid biosynthetic process), outer-membrane/export component for AlgE (GO:0009279), periplasm for AlgG/AlgL/AlgK, and poly-β-D-mannuronate C5-epimerase activity for AlgG. Do **not** propagate GO:0006535 (cysteine biosynthesis) into this module for the CysE genes. No new GO term requests appear necessary — existing alginate terms cover the module.

---

## Genes to Promote to Full `fetch-gene` Review

1. **PP_1284 algE** — export porin; missing from bucket, functionally essential, structurally defined in *P. aeruginosa*. Confirm β-barrel/OMP annotation and signal peptide.
2. **PP_1285 algK** — scaffold lipoprotein; confirm lipobox/TPR and periplasmic localization (3D structure available — strong evidence).
3. **PP_1283 algG** — C5-epimerase; confirm EC 5.1.3.37 and catalytic residues.
4. **PP_1281 algL** — alginate lyase; confirm EC 4.2.2.3 (avoid confusion with degradation-only lyases).
5. **PP_1282 algX** — resolve broad EC 2.3.1.- and dual scaffold/O-acetyltransferase annotation.
6. (Lower priority) **PP_2124** — reassign to its correct Psl/non-alginate EPS system; one representative CysE (e.g., PP_0840) documented as over-propagation to prevent re-inclusion.

---

## Evidence Base

### Direct target-species evidence (*P. putida*)

| PMID | Finding | Strength for KT2440 |
|------|---------|--------------------|
| [17601783](https://pubmed.ncbi.nlm.nih.gov/17601783/) | Alginate produced under matric (not solute) stress; *algD* mutant → altered biofilm, reduced desiccation survival | **Strong** — *P. putida* mt-2 (KT2440 parent lineage) |
| [15101980](https://pubmed.ncbi.nlm.nih.gov/15101980/) | Matric-stress screen recovered alginate genes among desiccation determinants | **Strong** — *P. putida*, KT2440 genome homology |
| [21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) | KT2440 carries an intact *alg* cluster; minor biofilm role under standard lab conditions | **Direct** — KT2440 |
| [41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/) | Single deletable *alg* cluster; drought-protective biofilm on tomato | **Direct** — KT2440 |
| [21554519](https://pubmed.ncbi.nlm.nih.gov/21554519/) | High c-di-GMP overproduces a *different* KT2440 EPS (PP3133–3141), not alginate/cellulose | **Direct** — KT2440; supports keeping non-alginate EPS out of the module |

### Mechanistic transfer evidence (*P. aeruginosa*, homology-based, high-confidence transfer)

| PMID | Contribution |
|------|-------------|
| [23503314](https://pubmed.ncbi.nlm.nih.gov/23503314/) | Envelope-spanning multiprotein complex; AlgK deletion destabilizes Alg8/Alg44 |
| [25968647](https://pubmed.ncbi.nlm.nih.gov/25968647/) | Alg8–Alg44 direct interaction; polymerization/modification coupling (AlgG, AlgX) |
| [21778407](https://pubmed.ncbi.nlm.nih.gov/21778407/) | AlgE 18-strand β-barrel export porin structure |
| [25084326](https://pubmed.ncbi.nlm.nih.gov/25084326/) | AlgE conformational landscape / gating; AlgK pre-orients polymer |
| [23335756](https://pubmed.ncbi.nlm.nih.gov/23335756/) | AlgE dual role in secretion and complex stability |
| [25817996](https://pubmed.ncbi.nlm.nih.gov/25817996/) | Dimeric c-di-GMP binding by Alg44 PilZ domain drives polymerization |
| [21713511](https://pubmed.ncbi.nlm.nih.gov/21713511/) | Periplasmic AlgK–AlgX–MucD complex links stability to regulation |

**Species-transfer note:** All mechanistic/structural detail derives from *P. aeruginosa* and transfers with **high confidence** because KT2440 possesses a complete, one-to-one orthologous operon. Direct KT2440 evidence confirms cluster presence and phenotypic relevance but not molecular mechanism; alginate chemical composition/acetylation in KT2440 has not been directly characterized and remains open.

---

## Limitations and Knowledge Gaps

1. **No direct KT2440 biochemistry per gene.** Gene presence and operon structure are from genome annotation (KEGG/GenBank) and UniProt; individual KT2440 subunit functions are inferred from *P. aeruginosa* orthologs, not measured in KT2440.
2. **M/G composition and acetylation of KT2440 alginate are uncharacterized.** AlgG epimerase and AlgI/J/F/AlgX acetylation activities are assumed from homology; the actual polymer chemistry in KT2440 is unknown.
3. **Conditionality of expression.** Alginate is minor/absent under standard lab conditions and induced by matric stress; the precise regulatory triggers (AlgU/σ22, MucABCD, c-di-GMP pools) in KT2440 are not fully mapped.
4. **Precursor-module boundary** (AlgA/AlgC/AlgD placement) is a definitional choice not resolved here.
5. **PslH (PP_2124) reassignment** is inferred from KO K21001; a dedicated Psl-module review would confirm it.

---

## Proposed Follow-up Experiments / Actions

1. **Curation (immediate):** Apply the recommendations above — add algL/algG/algE/algK, drop the four CysE genes + PP_2124, mark module covered, flag KEGG map00543 as a non-specific bucket.
2. **`fetch-gene` promotions:** Run full gene review on PP_1281, PP_1283, PP_1284, PP_1285, PP_1282.
3. **Schema fix:** Add a rule that EC 2.3.1.30 (serine O-acetyltransferase/CysE) and generic glycosyltransferase KOs (e.g., K21001) should not seed alginate-module membership from KEGG map00543.
4. **Experimental (to resolve gaps):** Characterize KT2440 alginate M/G ratio and acetylation under matric stress; construct single-gene deletions (ΔalgE, ΔalgK, ΔalgG) in KT2440 to confirm export/scaffold/epimerase roles directly rather than by transfer.
5. **Regulatory mapping:** Test AlgU/MucA and c-di-GMP dependence of the KT2440 *alg* operon under water-limiting conditions.

---

## Key References

- Chang WS *et al.* (2007) *Alginate production by Pseudomonas putida creates a hydrated microenvironment... under water-limiting conditions.* [PMID: 17601783](https://pubmed.ncbi.nlm.nih.gov/17601783/) — direct target-species functional evidence.
- van de Mortel M & Halverson LJ (2004) *Cell envelope components contributing to biofilm growth and survival of Pseudomonas putida in low-water-content habitats.* [PMID: 15101980](https://pubmed.ncbi.nlm.nih.gov/15101980/) — target-species.
- *Influence of putative exopolysaccharide genes on Pseudomonas putida KT2440 biofilm stability.* [PMID: 21507178](https://pubmed.ncbi.nlm.nih.gov/21507178/) — direct KT2440.
- *Biofilm formation by Pseudomonas putida KT2440 contributes to tomato drought stress resilience.* [PMID: 41554215](https://pubmed.ncbi.nlm.nih.gov/41554215/) — direct KT2440.
- Matilla MA *et al.* (2011) *Cyclic diguanylate turnover... in Pseudomonas putida.* [PMID: 21554519](https://pubmed.ncbi.nlm.nih.gov/21554519/) — KT2440 regulation.
- Hay ID *et al.* (2013) *Insights into the assembly of the alginate biosynthesis machinery in Pseudomonas aeruginosa.* [PMID: 23503314](https://pubmed.ncbi.nlm.nih.gov/23503314/)
- Moradali MF *et al.* (2015) *Alginate Polymerization and Modification Are Linked in Pseudomonas aeruginosa.* [PMID: 25968647](https://pubmed.ncbi.nlm.nih.gov/25968647/)
- Whitney JC *et al.* (2011) *Structural basis for alginate secretion across the bacterial outer membrane.* [PMID: 21778407](https://pubmed.ncbi.nlm.nih.gov/21778407/)
- Tan J *et al.* (2014) *A conformational landscape for alginate secretion across the outer membrane.* [PMID: 25084326](https://pubmed.ncbi.nlm.nih.gov/25084326/)
- Rehman ZU & Rehm BHA (2013) *Dual roles of Pseudomonas aeruginosa AlgE.* [PMID: 23335756](https://pubmed.ncbi.nlm.nih.gov/23335756/)
- Whitney JC *et al.* (2015) *Dimeric c-di-GMP is required for post-translational regulation of alginate production.* [PMID: 25817996](https://pubmed.ncbi.nlm.nih.gov/25817996/)
- Hay ID *et al.* (2012) *Identification of a periplasmic AlgK-AlgX-MucD multiprotein complex.* [PMID: 21713511](https://pubmed.ncbi.nlm.nih.gov/21713511/)
- KEGG `ppu00543` and KT2440 GenBank locus annotations PP_1277–PP_1288; UniProt reference proteome UP000000556 (retrieved 2026-08-08).

---

*Prepared for manual module satisfiability and gene-annotation curation. Evidence tiers: KT2440-direct (genome/UniProt annotation + PMIDs 17601783, 15101980, 21507178, 41554215, 21554519) vs. P. aeruginosa mechanistic transfer (strong at structure/mechanism, not phenotype).*


## Artifacts

- [OpenScientist final report](PSEPK__alginate-polymerization-export__ppu00543-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__alginate-polymerization-export__ppu00543-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21507178
2. PMID:41554215
3. PMID:17601783
4. PMID:15101980
5. PMID:25968647
6. PMID:25817996
7. PMID:21713511
8. PMID:23503314
9. PMID:21778407
10. PMID:25084326
11. PMID:23335756
12. PMID:21554519