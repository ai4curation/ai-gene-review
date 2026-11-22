---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:43:28.153191'
end_time: '2026-08-31T13:44:17.002441'
duration_seconds: 3648.85
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: UDP-glucose and UDP-galactose biosynthesis
  module_summary: Species-neutral bacterial module for production of UDP-glucose from
    glucose 6-phosphate and its reversible interconversion with UDP-galactose. The
    module contains phosphoglucomutase, UTP--glucose-1-phosphate uridylyltransferase,
    and UDP-glucose 4-epimerase reactions. It supplies activated hexoses to multiple
    downstream glycoconjugate and storage-polymer pathways; those consuming pathways
    are outside this module.
  module_outline: "- UDP-glucose and UDP-galactose biosynthesis\n  - 1. glucose 1-phosphate\
    \ formation\n  - Phosphoglucomutase reaction\n    - Pgm: phosphoglucomutase (molecular\
    \ player: bacterial phosphoglucomutase family; activity or role: phosphoglucomutase\
    \ activity)\n    - AlgC: phosphoglucomutase (molecular player: bifunctional phosphomannomutase/phosphoglucomutase\
    \ family; activity or role: phosphoglucomutase activity)\n  - 2. UDP-glucose formation\n\
    \  - UTP--glucose-1-phosphate uridylyltransferase reaction\n    - GalU: UTP--glucose-1-phosphate\
    \ uridylyltransferase (molecular player: bacterial UTP--glucose-1-phosphate uridylyltransferase\
    \ family; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)\n\
    \  - 3. UDP-galactose formation and interconversion\n  - UDP-glucose 4-epimerase\
    \ reaction\n    - GalE: UDP-glucose 4-epimerase (molecular player: UDP-glucose\
    \ 4-epimerase family; activity or role: UDP-glucose 4-epimerase activity)"
  module_connections: No explicit connections.
  pathway_query: ppu00052
  pathway_id: ppu00052
  pathway_name: Galactose metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00052 with 7 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '8'
  candidate_genes: '- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase
    family protein (primary bucket kegg:ppu00052)

    - glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2;
    primary bucket kegg:ppu00052)

    - PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)

    - cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary
    bucket kegg:ppu00052)

    - galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary
    bucket kegg:ppu00052)

    - pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary
    bucket kegg:ppu00052)

    - galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9)
    (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)

    - algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC
    5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)'
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__udp_glucose_and_udp_galactose_biosynthesis__ppu00052-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__udp_glucose_and_udp_galactose_biosynthesis__ppu00052-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

UDP-glucose and UDP-galactose biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00052
- Resolved ID: ppu00052
- Resolved name: Galactose metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00052 with 7 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- PP_0501: PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase family protein (primary bucket kegg:ppu00052)
- glk: PP_1011 | Q88P42 | Glucokinase (EC 2.7.1.2) (Glucose kinase) (EC 2.7.1.2; primary bucket kegg:ppu00052)
- PP_1165: PP_1165 | Q88NP2 | Aldose 1-epimerase (primary bucket kegg:ppu00052)
- cpsG: PP_1777 | Q88LZ9 | phosphomannomutase (EC 5.4.2.8) (EC 5.4.2.8; primary bucket kegg:ppu00052)
- galE: PP_3129 | Q88I72 | UDP-glucose 4-epimerase (EC 5.1.3.2) (EC 5.1.3.2; primary bucket kegg:ppu00052)
- pgm: PP_3578 | Q88GY7 | Phosphoglucomutase (EC 5.4.2.2) (EC 5.4.2.2; primary bucket kegg:ppu00052)
- galU: PP_3821 | Q88GA4 | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) (EC 2.7.7.9; primary bucket kegg:ppu00040)
- algC: PP_5288 | Q88C93 | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) (EC 5.4.2.2; 5.4.2.8; primary bucket kegg:ppu00052)

## Generic Module Context

### Working Scope

Species-neutral bacterial module for production of UDP-glucose from glucose 6-phosphate and its reversible interconversion with UDP-galactose. The module contains phosphoglucomutase, UTP--glucose-1-phosphate uridylyltransferase, and UDP-glucose 4-epimerase reactions. It supplies activated hexoses to multiple downstream glycoconjugate and storage-polymer pathways; those consuming pathways are outside this module.

### Provisional Biological Outline

- UDP-glucose and UDP-galactose biosynthesis
  - 1. glucose 1-phosphate formation
  - Phosphoglucomutase reaction
    - Pgm: phosphoglucomutase (molecular player: bacterial phosphoglucomutase family; activity or role: phosphoglucomutase activity)
    - AlgC: phosphoglucomutase (molecular player: bifunctional phosphomannomutase/phosphoglucomutase family; activity or role: phosphoglucomutase activity)
  - 2. UDP-glucose formation
  - UTP--glucose-1-phosphate uridylyltransferase reaction
    - GalU: UTP--glucose-1-phosphate uridylyltransferase (molecular player: bacterial UTP--glucose-1-phosphate uridylyltransferase family; activity or role: UTP:glucose-1-phosphate uridylyltransferase activity)
  - 3. UDP-galactose formation and interconversion
  - UDP-glucose 4-epimerase reaction
    - GalE: UDP-glucose 4-epimerase (molecular player: UDP-glucose 4-epimerase family; activity or role: UDP-glucose 4-epimerase activity)

### Known Relationships Among Steps

No explicit connections.

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

# Module Review: UDP-glucose and UDP-galactose Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI taxon 160488, proteome UP000000556)
**Target pathway/bucket:** KEGG ppu00052 "Galactose metabolism" (local module area: UDP-glucose/UDP-galactose biosynthesis)
**Assignment:** Species-aware review to support manual module satisfiability and gene-annotation curation.

---

## 1. Executive Summary

The species-neutral UDP-glucose/UDP-galactose biosynthesis module — (1) phosphoglucomutase producing glucose-1-phosphate, (2) UTP:glucose-1-phosphate uridylyltransferase producing UDP-glucose, and (3) UDP-glucose 4-epimerase interconverting UDP-glucose and UDP-galactose — is **fully satisfiable** in *P. putida* KT2440. Every core step maps to at least one specific, plausibly correct gene: **Pgm (PP_3578)** and the bifunctional **AlgC (PP_5288)** cover the phosphoglucomutase step; **GalU (PP_3821)** covers UDP-glucose formation; and **GalE (PP_3129)** covers the UDP-glucose↔UDP-galactose epimerization. All three module steps therefore should be marked **covered**.

A key curation nuance concerns the epimerase step. The candidate list contains **two** genes annotated to the GalE KEGG ortholog K01784: PP_3129 and PP_0501. Quantitative sequence analysis resolves this ambiguity decisively. PP_3129 is 43.9% identical to the biochemically characterized *E. coli* GalE (P09147) and carries the canonical GalE architecture, whereas PP_0501 is only 34.2% identical to *E. coli* GalE and 35.2% identical to PP_3129, and instead belongs to the COG0451 / Pfam PF01370 extended-SDR epimerase-dehydratase family with PANTHER PTHR43245 (ArnA / polymyxin-resistance) and InterPro IPR050177 (lipid-A modification) signatures. PP_0501 is therefore best treated as an **over-propagated GalE annotation** and should not be counted as a second UDP-glucose 4-epimerase for module satisfiability.

The apparent "missing" Leloir catabolic genes (galactokinase *galK*, galactose-1-phosphate uridylyltransferase *galT*) are **not gaps** in this anabolic module. KT2440 does not possess a native functional Leloir pathway; it catabolizes galactose oxidatively to galactonate via glucose dehydrogenase, and engineering studies had to introduce *galETKM* + *lacY* to confer lactose/galactose utilization. Consequently, GalE in KT2440 functions as an **anabolic** UDP-sugar interconversion enzyme feeding glycoconjugate and storage-polymer pathways, not as a catabolic Leloir enzyme. Importantly, every module call rests on homology/database inference (UniProt protein-existence level 3), with **no KT2440-specific enzymology** in the literature — this is the principal limitation of the current evidence base.

---

## 2. Target-Organism Pathway Definition

### What is included

This module covers the conversion of glucose 6-phosphate into **UDP-glucose** and its reversible epimerization to **UDP-galactose**:

```
  glucose-6-P  --(Pgm / AlgC, EC 5.4.2.2)-->  glucose-1-P
  glucose-1-P + UTP  --(GalU, EC 2.7.7.9)-->  UDP-glucose + PPi
  UDP-glucose  <--(GalE, EC 5.1.3.2)-->  UDP-galactose
```

These activated nucleotide sugars are precursors for downstream glycoconjugate and storage-polymer biosynthesis (LPS core/O-antigen, exopolysaccharides, glycolipids). Those consuming pathways are **outside** the module scope.

### Neighboring pathways to keep separate

- **Leloir galactose catabolism** (galactokinase → Gal-1-P uridylyltransferase → epimerase; EC 2.7.1.6 / 2.7.7.10 / 5.1.3.2). Although KEGG map ppu00052 "Galactose metabolism" nominally contains these steps, KT2440 lacks a native functional Leloir route (see Finding F002). Do not treat *galK*/*galT* absence as a module gap.
- **Oxidative galactose catabolism** (galactose → galactonate via glucose dehydrogenase; the De Ley–Doudoroff-type route). This is the actual native galactose-utilization route in KT2440 and is a *catabolic* pathway distinct from the anabolic UDP-sugar module.
- **GDP-mannose biosynthesis / LPS biosynthesis** (phosphomannomutase, EC 5.4.2.8). AlgC and CpsG connect here; CpsG in particular is a phosphomannomutase, not a glucose-1-P–producing enzyme.
- **Downstream consumers** — alginate, LPS, rhamnolipid, and exopolysaccharide biosynthesis draw on UDP-glucose/glucose-1-P but are separate modules.

### Alternate names / database definitions

- KEGG: ppu00052 "Galactose metabolism" (broad overview map that bundles Leloir, oxidative, and UDP-sugar-interconversion reactions).
- UniProt pathway strings: "UDP-alpha-D-galactose biosynthesis" / "galactose metabolism" (for GalE); "GDP-mannose biosynthesis" and "LPS biosynthesis" (for AlgC/CpsG).
- The local module is a species-neutral **"UDP-glucose and UDP-galactose biosynthesis"** bucket — narrower and more precise than the KEGG map.

---

## 3. Expected Step Model

| Step | Reaction | EC | KEGG KO | Expected in KT2440? | Best candidate |
|------|----------|-----|---------|---------------------|----------------|
| 1. Glucose-1-P formation | glucose-6-P ↔ glucose-1-P | 5.4.2.2 | K01835 (Pgm); K15778 (PMM/PGM) | Yes | **PP_3578 (pgm)**; backup **PP_5288 (algC)** |
| 2. UDP-glucose formation | glucose-1-P + UTP → UDP-glucose + PPi | 2.7.7.9 | K00963 | Yes | **PP_3821 (galU)** |
| 3. UDP-glucose ↔ UDP-galactose | UDP-glucose ↔ UDP-galactose | 5.1.3.2 | K01784 | Yes | **PP_3129 (galE)** |

**Steps expected to be ABSENT (not module gaps):**
- Galactokinase (EC 2.7.1.6, *galK*) — no native functional gene; Leloir route not present.
- Gal-1-P uridylyltransferase (EC 2.7.7.10/12, *galT*) — no native functional gene.

These absences are consistent with the organism's biology and should be recorded as **not_expected_in_target_taxon**, not as gaps.

---

## 4. Candidate Genes and Evidence

The local metadata provides 8 candidate genes. Below, each is assessed for its role in this specific module, its evidence type, and curation caveats. All UniProt annotations are protein-existence level 3 ("inferred from homology"); none has KT2440-specific enzymological validation.

| Gene | Locus | UniProt | Annotation | KEGG KO | Module role | Call |
|------|-------|---------|------------|---------|-------------|------|
| **pgm** | PP_3578 | Q88GY7 | Phosphoglucomutase, EC 5.4.2.2 | K01835 | **Step 1 (core)** | Covered |
| **galU** | PP_3821 | Q88GA4 | UTP--glucose-1-P uridylyltransferase, EC 2.7.7.9 | K00963 | **Step 2 (core)** | Covered |
| **galE** | PP_3129 | Q88I72 | UDP-glucose 4-epimerase, EC 5.1.3.2 | K01784 | **Step 3 (core)** | Covered |
| **algC** | PP_5288 | Q88C93 | Bifunctional PMM/PGM, EC 5.4.2.2 + 5.4.2.8 | K15778 | Step 1 backup | Covered (redundant) |
| cpsG | PP_1777 | Q88LZ9 | Phosphomannomutase, EC 5.4.2.8 | K15778 | Peripheral (mannose-1-P) | Not core / EC likely partial |
| glk | PP_1011 | Q88P42 | Glucokinase, EC 2.7.1.2 | K00845 | Upstream (G6P supply) | Peripheral |
| PP_1165 | PP_1165 | Q88NP2 | Aldose 1-epimerase | K01785 | Peripheral (mutarotation) | Peripheral |
| PP_0501 | PP_0501 | Q88QJ1 | NAD-dependent epimerase/dehydratase | K01784 | **Over-propagated GalE** | Likely over-annotation |

### High-confidence core genes

**PP_3578 (pgm) — phosphoglucomutase, Step 1.** Dedicated phosphoglucomutase (EC 5.4.2.2, KO K01835). This is the canonical glucose-1-P–producing enzyme for the module. Evidence: homology/database. **Covered.**

**PP_3821 (galU) — UTP:glucose-1-P uridylyltransferase, Step 2.** UDP-glucose pyrophosphorylase (EC 2.7.7.9, KO K00963). Note the local metadata lists its primary bucket as ppu00040 rather than ppu00052, but its function is unambiguously the module's UDP-glucose-forming step. Evidence: homology/database. **Covered.**

**PP_3129 (galE) — UDP-glucose 4-epimerase, Step 3.** UDP-glucose 4-epimerase (EC 5.1.3.2, KO K01784), UniProt pathway "galactose metabolism". Pairwise Needleman–Wunsch identity to the characterized *E. coli* GalE (P09147) is **43.9%** over 321/338 aa — comfortably within the range for a genuine ortholog and clearly the true GalE of the pair sharing K01784. **Covered.** In KT2440 this enzyme acts anabolically (UDP-sugar interconversion for glycoconjugate biosynthesis), not as a Leloir catabolic epimerase (Finding F002).

### Redundant / backup gene

**PP_5288 (algC) — bifunctional PMM/PGM, Step 1 backup.** UniProt annotates dual EC 5.4.2.2 (PGM) + 5.4.2.8 (PMM), with pathways "GDP-mannose biosynthesis" and "LPS biosynthesis". The *P. aeruginosa* ortholog is a well-characterized single bifunctional enzyme: Ye et al. showed it interconverts both mannose-1-P/mannose-6-P and glucose-1-P/glucose-6-P ([PMID: 8050998](https://pubmed.ncbi.nlm.nih.gov/8050998/)), and Olvera et al. documented its dual role in alginate (via PMM) and LPS (via PGM) synthesis ([PMID: 10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/)). AlgC therefore provides genuine redundancy for the glucose-1-P–forming step. Transfer to KT2440 is **strong at the family level** (well-conserved *Pseudomonas* AlgC) but remains homology-based for KT2440 specifically.

### Peripheral genes (KEGG map members, not core UDP-sugar enzymes)

- **cpsG (PP_1777)** — EC 5.4.2.8 phosphomannomutase (KO K15778, shares with algC). Makes **mannose-1-P**, not glucose-1-P; UniProt pathway "GDP-mannose biosynthesis". The EC-5.4.2.8-only annotation is likely **partial** relative to the bifunctional K15778 definition. Peripheral to this module.
- **glk (PP_1011)** — glucokinase EC 2.7.1.2 (KO K00845). Supplies glucose-6-P upstream of the module; not a module step.
- **PP_1165** — aldose 1-epimerase (mutarotase, KO K01785, EC 5.1.3.3), UniProt PE4 "Predicted", no EC in metadata. Catalyzes anomeric mutarotation; peripheral to UDP-sugar biosynthesis.

### Likely over-annotation

- **PP_0501** — annotated "NAD-dependent epimerase/dehydratase family protein" and co-assigned to K01784 (GalE) alongside PP_3129, but it is **not** a canonical GalE. See Section 5.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### PP_0501 is an over-propagated GalE / K01784 assignment

The single most curation-relevant finding is the paralog ambiguity at the GalE step, where **both PP_3129 and PP_0501 map to K01784**. Quantitative sequence analysis resolves this:

| Comparison | % identity (Needleman–Wunsch) |
|------------|-------------------------------|
| PP_3129 (galE) vs *E. coli* GalE (P09147) | **43.9%** |
| PP_0501 vs *E. coli* GalE (P09147) | 34.2% |
| PP_0501 vs PP_3129 | 35.2% |

PP_0501 (310 aa) additionally carries a diagnostic domain signature distinct from GalE: **COG0451 / Pfam PF01370** (extended-SDR epimerase-dehydratase), **PANTHER PTHR43245** (ArnA / polymyxin-resistance protein), and **InterPro IPR050177** (lipid-A modification). This is the signature of an ArnA/lipid-A-modification-type NAD-dependent epimerase-dehydratase, not a UDP-glucose 4-epimerase. **Recommendation:** do not count PP_0501 as a second GalE for module satisfiability; flag its K01784 assignment as likely over-propagated; its true function is probably in nucleotide-sugar modification for LPS/lipid-A rather than UDP-glucose↔UDP-galactose interconversion.

### CpsG EC annotation is likely partial

CpsG (PP_1777) and AlgC (PP_5288) both map to K15778, whose full definition is bifunctional phosphomannomutase/phosphoglucomutase (EC 5.4.2.8 + 5.4.2.2). The local metadata annotates CpsG with **EC 5.4.2.8 only**. Whether CpsG has genuine PGM activity in KT2440 is unresolved from database evidence alone; the EC restriction may be an incomplete annotation rather than a true monofunctional assignment.

### "Missing" Leloir genes are expected absence, not gaps

No *galK* (galactokinase) or *galT* (Gal-1-P uridylyltransferase) appears in the candidate list. This reflects genuine biology: Saumaa et al. had to chromosomally integrate *galETKM* + *lacY* to engineer lactose/galactose utilization in KT2440 ([PMID: 40691973](https://pubmed.ncbi.nlm.nih.gov/40691973/)), and Zhou et al. showed native galactose catabolism proceeds oxidatively to galactonate via glucose dehydrogenase ([PMID: 35227739](https://pubmed.ncbi.nlm.nih.gov/35227739/)). Mark these as **not_expected_in_target_taxon**.

### Broad EC/GO and homology-only evidence

Every core call is UniProt protein-existence level 3 (inferred from homology). There is **no direct KT2440 enzymology** for Pgm, GalU, or GalE. AlgC's biochemistry is transferred from *P. aeruginosa*, a related but distinct species.

---

## 6. Module and GO-Curation Recommendations

| Module step | Status recommendation | Rationale |
|-------------|-----------------------|-----------|
| Step 1: glucose-1-P formation (PGM) | **covered** | PP_3578 (pgm, K01835) dedicated; PP_5288 (algC, K15778) redundant backup |
| Step 2: UDP-glucose formation (GalU) | **covered** | PP_3821 (galU, K00963), unambiguous |
| Step 3: UDP-glucose ↔ UDP-galactose (GalE) | **covered** | PP_3129 (galE, K01784), 43.9% identity to characterized *E. coli* GalE |
| Leloir galK / galT | **not_expected_in_target_taxon** | No native functional Leloir pathway; galactose catabolized oxidatively |
| PP_0501 as second GalE | **module_needs_revision / over-annotation** | ArnA/lipid-A-type SDR, not a canonical UDP-glucose 4-epimerase |

**Overall: the module is fully covered in *P. putida* KT2440.** All three core steps have a well-supported gene.

**Module boundary assessment:** The generic module boundaries are broadly correct for this organism, with two refinements. (1) The KEGG ppu00052 "Galactose metabolism" umbrella conflates Leloir catabolism (absent), oxidative galactose catabolism (present, separate), and anabolic UDP-sugar interconversion (this module) — curators should keep these distinct. (2) The K01784 KEGG ortholog is over-inclusive in KT2440, capturing both the true GalE (PP_3129) and an ArnA-type SDR (PP_0501); a KO/annotation correction for PP_0501 is warranted.

**GO-curation notes:** GalE (PP_3129) supports GO:0003978 (UDP-glucose 4-epimerase activity) and GO:0006012 (galactose metabolic process, anabolic sense). No new GO term requests appear necessary. Consider annotating PP_0501 to a lipid-A/nucleotide-sugar-modification function (consistent with IPR050177 / ArnA) rather than UDP-glucose 4-epimerase.

---

## 7. Genes to Promote to Full Review

1. **PP_0501 (Q88QJ1)** — **highest priority.** Resolve the over-propagated K01784/GalE assignment; confirm ArnA/lipid-A-modification-type SDR function; correct the KEGG KO and EC/GO annotations. This directly affects module satisfiability bookkeeping (avoid double-counting GalE).
2. **PP_1777 (cpsG, Q88LZ9)** — clarify whether it is monofunctional PMM (EC 5.4.2.8) or bifunctional PMM/PGM (K15778 full definition); resolve overlap with AlgC.
3. **PP_3129 (galE, Q88I72)** — confirm the anabolic (non-Leloir) role and, ideally, secure direct KT2440 enzymological/functional evidence to upgrade from homology inference.
4. **PP_5288 (algC, Q88C93)** — confirm PGM redundancy for the module and its connections to LPS/alginate/rhamnolipid consumers; transfer from *P. aeruginosa* is strong but not KT2440-direct.

---

## 8. Key References

| PMID | Relevance to this review |
|------|--------------------------|
| [8050998](https://pubmed.ncbi.nlm.nih.gov/8050998/) | *Pseudomonas aeruginosa* PMM/PGM is a single bifunctional enzyme interconverting both mannose-1-P/6-P **and glucose-1-P/6-P** — supports AlgC as a backup for the module's phosphoglucomutase step. Quote: "The enzyme catalyzed the interconversion of mannose 1-phosphate (M1P) and mannose 6-phosphate, as well as that of glucose 1-phosphate (G1P) and glucose 6-phosphate." |
| [10481091](https://pubmed.ncbi.nlm.nih.gov/10481091/) | Documents AlgC's dual PMM (alginate) / PGM (LPS) roles. Quote: "the algC gene (which is involved in alginate production through its phosphomannomutase activity and in LPS synthesis through its phosphoglucomutase activity)." |
| [40691973](https://pubmed.ncbi.nlm.nih.gov/40691973/) | Leloir genes had to be engineered into KT2440, confirming they are not natively functional. Quote: "the expression of β-galactosidase gene lacZ on a plasmid was accompanied with integration of galactose Leloir pathway genes galETKM and lactose permease gene lacY into the chromosome of KT2440." |
| [35227739](https://pubmed.ncbi.nlm.nih.gov/35227739/) | Native galactose catabolism in KT2440 is oxidative (→ galactonate), separate from the anabolic UDP-sugar module. Quote: "P. putida KT2440 was confirmed owning high ability to oxidize galactose to galactonate by glucose dehydrogenase." |
| [12761084](https://pubmed.ncbi.nlm.nih.gov/12761084/) | *Stenotrophomonas maltophilia* AlgC homolog (SpgM) is a bifunctional PGM/PMM linked to LPS — corroborates the AlgC-family bifunctionality across genera. |
| [7558335](https://pubmed.ncbi.nlm.nih.gov/7558335/) | *P. aeruginosa* algC mutant phenotype ties AlgC PGM/PMM activity to LPS/alginate biosynthesis (downstream consumers of module products). |

---

## Mechanistic Model / Interpretation

```
   [glucose]                       (peripheral: PP_1165 aldose-1-epimerase = mutarotation)
       |
   glk (PP_1011, EC 2.7.1.2)   <-- peripheral, upstream G6P supply
       v
  glucose-6-P
       |  Pgm  (PP_3578, K01835, EC 5.4.2.2)      <== STEP 1 (core)
       |  AlgC (PP_5288, K15778, EC 5.4.2.2/8)     <== STEP 1 backup (bifunctional)
       v
  glucose-1-P  + UTP
       |  GalU (PP_3821, K00963, EC 2.7.7.9)       <== STEP 2 (core)
       v
   UDP-glucose  <====== GalE (PP_3129, K01784, EC 5.1.3.2) ======>  UDP-galactose
       |                        ^  STEP 3 (core)                          |
       |                        |                                         |
       |             PP_0501 (K01784 assignment = OVER-PROPAGATED;         |
       |             actually ArnA/lipid-A-type SDR, COG0451/PF01370)      |
       v                                                                  v
  --> downstream glycoconjugate / storage-polymer pathways (LPS, EPS, alginate, rhamnolipid) -->

  SEPARATE (not this module):
   * Leloir catabolism (galK/galT) — NOT natively functional in KT2440
   * Oxidative galactose catabolism (galactose -> galactonate via glucose dehydrogenase) — native route
   * cpsG (PP_1777, K15778, EC 5.4.2.8) -> mannose-1-P / GDP-mannose branch
```

The narrative: KT2440 encodes a complete, redundant machinery for producing activated UDP-glucose and epimerizing it to UDP-galactose, serving anabolic demand for cell-surface and secreted glycoconjugates. Because the organism lacks a native Leloir catabolic route (galactose is instead oxidized to galactonate), GalE operates in the biosynthetic direction. The phosphoglucomutase step is doubly covered by a dedicated Pgm and a bifunctional AlgC. The only substantive curation hazard is the two-gene mapping to the GalE ortholog K01784, which sequence and domain analysis cleanly resolves in favor of PP_3129, exposing PP_0501 as an over-propagated annotation.

---

## Limitations and Knowledge Gaps

- **No KT2440-specific enzymology.** All core assignments (Pgm, GalU, GalE) are homology/database inferences (UniProt PE3). Direct biochemical or genetic validation in KT2440 is absent.
- **Species transfer for AlgC.** AlgC bifunctionality is directly demonstrated in *P. aeruginosa* and *S. maltophilia*, not KT2440; the *Pseudomonas* AlgC is well conserved, so transfer is strong but not KT2440-direct.
- **CpsG functional scope.** Whether CpsG contributes PGM activity (bifunctional K15778) or is a dedicated PMM (EC 5.4.2.8) in KT2440 is unresolved.
- **PP_0501 true function** is inferred from domain signatures (ArnA/lipid-A-modification family), not experimentally established in KT2440.
- **Reversibility/directionality** of GalE in vivo and the relative flux through Pgm vs AlgC are not quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Curate PP_0501:** correct/flag its K01784 (GalE) assignment; reannotate to an ArnA/lipid-A-modification-type SDR (IPR050177). Highest-value single action for module bookkeeping.
2. **Full `fetch-gene` review** of PP_0501, PP_1777 (cpsG), PP_3129 (galE), PP_5288 (algC) as prioritized in Section 7.
3. **Targeted genetics:** construct KT2440 Δpgm, ΔalgC, and Δpgm ΔalgC to test which enzyme(s) supply glucose-1-P and confirm AlgC redundancy for the module.
4. **Biochemistry:** heterologously express and assay PP_3129 (confirm UDP-glucose 4-epimerase), PP_0501 (test for UDP-glucose 4-epimerase vs UDP-sugar dehydratase/aminotransferase-linked activity), and CpsG (test for PGM alongside PMM).
5. **Module-schema fix:** ensure the module treats KEGG ppu00052 as an umbrella and separates Leloir (absent), oxidative catabolism (present, separate), and the anabolic UDP-sugar interconversion (this module).

---

*Report generated from a 3-iteration autonomous review. Core conclusion: the UDP-glucose/UDP-galactose biosynthesis module is fully satisfiable in* P. putida *KT2440 (all three steps covered), with the principal curation action being correction of the over-propagated GalE annotation on PP_0501.*


## Artifacts

- [OpenScientist final report](PSEPK__udp_glucose_and_udp_galactose_biosynthesis__ppu00052-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__udp_glucose_and_udp_galactose_biosynthesis__ppu00052-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8050998
2. PMID:10481091
3. PMID:40691973
4. PMID:35227739