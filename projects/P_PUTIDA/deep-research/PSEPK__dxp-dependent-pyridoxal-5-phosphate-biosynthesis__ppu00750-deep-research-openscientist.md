---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T05:44:10.912215'
end_time: '2026-07-17T06:05:02.210156'
duration_seconds: 1251.3
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: DXP-dependent pyridoxal 5-phosphate biosynthesis
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00750
  pathway_id: ppu00750
  pathway_name: Vitamin B6 metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00750 with 9 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '9'
  candidate_genes: '- pdxA: PP_0402 | Q88QT5 | 4-hydroxythreonine-4-phosphate dehydrogenase
    (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase) (EC 1.1.1.262; primary
    bucket kegg:ppu00750)

    - PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)

    - pdxH: PP_1129 | Q88NS5 | Pyridoxine/pyridoxamine 5''-phosphate oxidase (EC 1.4.3.5)
    (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5''-phosphate synthase) (EC 1.4.3.5; primary
    bucket kegg:ppu00750)

    - pdxJ: PP_1436 | Q88MY2 | Pyridoxine 5''-phosphate synthase (PNP synthase) (EC
    2.6.99.2) (EC 2.6.99.2; primary bucket kegg:ppu00750)

    - thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary
    bucket kegg:ppu00750)

    - serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine
    aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)

    - pdxB: PP_2117 | Q88L20 | Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290)
    (EC 1.1.1.290; primary bucket kegg:ppu00750)

    - epd: PP_4964 | Q88D63 | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) (EC
    1.2.1.72; primary bucket kegg:ppu00750)

    - pdxY: PP_5357 | Q88C26 | Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) (EC
    2.7.1.35; primary bucket kegg:ppu00750)'
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__dxp-dependent-pyridoxal-5-phosphate-biosynthesis__ppu00750-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__dxp-dependent-pyridoxal-5-phosphate-biosynthesis__ppu00750-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

DXP-dependent pyridoxal 5-phosphate biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00750
- Resolved ID: ppu00750
- Resolved name: Vitamin B6 metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00750 with 9 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 9

- pdxA: PP_0402 | Q88QT5 | 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase) (EC 1.1.1.262; primary bucket kegg:ppu00750)
- PP_0662: PP_0662 | Q88Q36 | Threonine synthase (primary bucket kegg:ppu00750)
- pdxH: PP_1129 | Q88NS5 | Pyridoxine/pyridoxamine 5'-phosphate oxidase (EC 1.4.3.5) (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5'-phosphate synthase) (EC 1.4.3.5; primary bucket kegg:ppu00750)
- pdxJ: PP_1436 | Q88MY2 | Pyridoxine 5'-phosphate synthase (PNP synthase) (EC 2.6.99.2) (EC 2.6.99.2; primary bucket kegg:ppu00750)
- thrC: PP_1471 | Q88MU7 | Threonine synthase (EC 4.2.3.1) (EC 4.2.3.1; primary bucket kegg:ppu00750)
- serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)
- pdxB: PP_2117 | Q88L20 | Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290) (EC 1.1.1.290; primary bucket kegg:ppu00750)
- epd: PP_4964 | Q88D63 | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) (EC 1.2.1.72; primary bucket kegg:ppu00750)
- pdxY: PP_5357 | Q88C26 | Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) (EC 2.7.1.35; primary bucket kegg:ppu00750)

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

# Module/Pathway/Taxon Review: DXP-dependent Pyridoxal 5'-Phosphate Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00750` — Vitamin B6 metabolism (module area: cofactors_vitamins_redox)
**Candidate gene count:** 9

---

## 1. Executive Summary

*Pseudomonas putida* KT2440 is a **clean, textbook case of the DXP-dependent (E. coli-type) de novo pyridoxal 5'-phosphate (PLP) biosynthetic pathway**. Two lines of authoritative evidence converge on this conclusion. First, direct isotope-labeling experiments in *P. putida* itself show that the ring nitrogen of pyridoxine derives from **glutamate**, not glutamine — the biochemical hallmark that distinguishes the DXP-dependent route (as in *E. coli*) from the DXP-independent Pdx1/Pdx2 (glutamine amidotransferase) route used by *Bacillus subtilis* and *Staphylococcus aureus* ([PMID: 10885790](https://pubmed.ncbi.nlm.nih.gov/10885790/), [PMID: 12775110](https://pubmed.ncbi.nlm.nih.gov/12775110/)). Second, a genome-wide check confirms that the DXP-**independent** PLP synthase (Pdx1/Pdx2; KEGG KOs K06215/K08681; SNZ/SNO family) is **absent** from KT2440, while all six DXP-pathway KOs are present. Because the two de novo routes are mutually exclusive ([PMID: 12686115](https://pubmed.ncbi.nlm.nih.gov/12686115/)), presence of the complete *pdx* set implies absence of the alternative.

The Vitamin B6 module is therefore **fully satisfiable** in KT2440. All six enzymatic steps of the de novo DXP-dependent pathway are encoded (epd → pdxB → serC → pdxA → pdxJ → pdxH), plus the salvage kinase pdxY. One required co-substrate input — 1-deoxy-D-xylulose-5-phosphate (DXP) supplied by *dxs* (PP_0527) — is present in the genome but is bucketed in the terpenoid-backbone map (`ppu00900`), so it does not appear in the `ppu00750` candidate list even though PdxJ strictly requires it.

The main curation issues are **not gaps but over-annotations**. Two of the nine candidate genes (PP_0662 and PP_1471) are **threonine synthases** (KEGG K01733, EC 4.2.3.1), pulled into the Vitamin B6 map only because threonine synthase is itself a PLP-*dependent* enzyme — a classic map artifact conflating "uses PLP" with "makes PLP." Neither is part of PLP biosynthesis. PP_1471 (*thrC*) is a canonical threonine synthase; PP_0662 is a weak, divergent paralog (UniProt PE=4 "Predicted," annotation score 1.0, lacking the diagnostic Thr-synthase InterPro signature) that should be promoted to full gene-level review. A further important caveat is that **every** B6 gene in KT2440 is annotated by homology inference only (UniProt PE=3); there is no experimental characterization in this strain.

---

## 2. Target-Organism Pathway Definition

### What the pathway *is* in KT2440

"Vitamin B6 metabolism" in *P. putida* KT2440 comprises two logically distinct sub-processes that KEGG map `ppu00750` bundles together:

1. **De novo biosynthesis of PLP via the DXP-dependent (deoxyxylulose-5-phosphate) route.** This is the *E. coli*-type pathway that constructs the pyridoxine ring from two branches — a "sugar" branch feeding via erythrose-4-phosphate and a DXP branch — condensed by PdxJ and oxidized to PLP by PdxH.

2. **The salvage pathway**, which interconverts and phosphorylates B6 vitamers (pyridoxal, pyridoxine, pyridoxamine and their phosphates) to regenerate the active cofactor PLP. In KT2440 this is represented by the single kinase PdxY/PdxK (PP_5357).

### What must be kept *separate* for curation

- **Overview/global maps** `ppu01100` (Metabolic pathways) and `ppu01240` (Biosynthesis of cofactors) — these aggregate the dedicated B6 genes but should not define module boundaries.
- **Glycine/Serine/Threonine metabolism (`ppu00260`)** — this is where the two threonine synthases (PP_0662, PP_1471) and the *serine-biosynthetic* role of *serC* properly belong. They appear in `ppu00750` because they are PLP-*dependent*, not PLP-*producing*.
- **Terpenoid backbone biosynthesis (`ppu00900`)** — home bucket of *dxs* (PP_0527), the DXP synthase. DXP is a shared precursor of both isoprenoids and vitamin B6; *dxs* is a required input to PdxJ but is not counted inside `ppu00750`.

### Alternate names / database definitions

The de novo route is variously called the "DXP-dependent pathway," the "deoxyxylulose-5-phosphate pathway," the "E. coli-type" or "glutamate-nitrogen" route, and the "pdx pathway." The mutually exclusive alternative is the "DXP-independent," "Pdx1/Pdx2," "SNZ/SNO," "SOR1," or "glutamine-nitrogen" route. Curators should treat *pdx* and *SOR1/Pdx1* as **autoexclusive** gene sets ([PMID: 12686115](https://pubmed.ncbi.nlm.nih.gov/12686115/)).

---

## 3. Expected Step Model

The DXP-dependent de novo pathway (as modeled from *E. coli*) plus salvage:

```
  SUGAR / PHOSPHOHYDROXYTHREONINE BRANCH            DXP BRANCH
  ------------------------------------             ----------
  D-erythrose-4-phosphate                          pyruvate + GAP
        | epd  (K03472, EC 1.2.1.72)                     | dxs (K01662)  [bucket ppu00900]
        v                                                v
  4-phosphoerythronate                          1-deoxy-D-xylulose-5-P (DXP)
        | pdxB (K03473, EC 1.1.1.290)                     |
        v                                                 |
  2-oxo-3-hydroxy-4-phosphobutanoate                      |
        | serC (K00831, EC 2.6.1.52)                      |
        v   [glutamate = N donor]                         |
  4-phosphohydroxy-L-threonine                            |
        | pdxA (K00097, EC 1.1.1.262)                     |
        v                                                 |
  3-amino-2-oxopropyl phosphate  ----------> PdxJ <-------+
        (1-amino-acetone-3-phosphate)   pdxJ (K03474, EC 2.6.99.2)
                                                 |
                                                 v
                                    pyridoxine-5'-phosphate (PNP)
                                                 | pdxH (K00275, EC 1.4.3.5)
                                                 v
                                    PYRIDOXAL-5'-PHOSPHATE (PLP)

  SALVAGE:  pyridoxal / pyridoxine / pyridoxamine
             --pdxY (PP_5357, K00868, EC 2.7.1.35)--> vitamer-5'-P --pdxH--> PLP
```

**Step-by-step expectation and coverage in KT2440:**

| # | Step (enzyme) | EC | KEGG KO | KT2440 gene | Status |
|---|---------------|-----|---------|-------------|--------|
| 0 | DXP synthase (input) | 2.2.1.7 | K01662 | *dxs* / PP_0527 | Present, bucketed in `ppu00900` |
| 1 | Erythrose-4-P dehydrogenase | 1.2.1.72 | K03472 | *epd* / PP_4964 | **Covered** (dedicated) |
| 2 | Erythronate-4-P dehydrogenase | 1.1.1.290 | K03473 | *pdxB* / PP_2117 | **Covered** (dedicated) |
| 3 | Phospho-hydroxythreonine aminotransferase | 2.6.1.52 | K00831 | *serC* / PP_1768 | **Covered** (moonlighting) |
| 4 | 4-hydroxythreonine-4-P dehydrogenase | 1.1.1.262 | K00097 | *pdxA* / PP_0402 | **Covered** |
| 5 | PNP synthase | 2.6.99.2 | K03474 | *pdxJ* / PP_1436 | **Covered** (dedicated) |
| 6 | PNP/PMP oxidase (→ PLP) | 1.4.3.5 | K00275 | *pdxH* / PP_1129 | **Covered** (dedicated) |
| S | Salvage kinase | 2.7.1.35 | K00868 | *pdxY* / PP_5357 | **Covered** (sole kinase) |
| — | DXP-independent PLP synthase | 4.3.3.6 | K06215/K08681 | — | **Not expected** (absent) |

---

## 4. Candidate Genes and Evidence

All nine candidate genes were assessed against KEGG KO assignments, UniProt evidence levels, and pathway membership. Below, each is summarized with likely role, evidence type, and curation caveats.

### High-confidence de novo enzymes

**epd — PP_4964 (Q88D63, K03472, EC 1.2.1.72).** Erythrose-4-phosphate dehydrogenase; catalyzes the first committed sugar-branch step. Maps only to `ppu00750` plus global overview maps → **dedicated** to the B6 bucket. Evidence: homology (UniProt PE=3). **Covered.**

**pdxB — PP_2117 (Q88L20, K03473, EC 1.1.1.290).** Erythronate-4-phosphate dehydrogenase; second sugar-branch step. Dedicated to `ppu00750`. Homology-inferred (PE=3). **Covered.**

**serC — PP_1768 (Q88M07, K00831, EC 2.6.1.52).** Phosphoserine aminotransferase / phosphohydroxythreonine aminotransferase. This is a **shared / moonlighting** enzyme: it is the phosphoserine aminotransferase of serine biosynthesis (belongs to `ppu00260`, `ppu00270`, `ppu00680`) that also performs the transamination that installs the pyridoxine ring nitrogen from **glutamate** (EC 2.6.1.52) in B6 biosynthesis. Its presence is essentially **guaranteed** by the requirement for serine biosynthesis, making this step robustly satisfiable. Caveat for curators: because it is multifunctional, do not treat its `ppu00750` membership as B6-dedicated. Homology-inferred (PE=3). **Covered.**

**pdxA — PP_0402 (Q88QT5, K00097, EC 1.1.1.262).** 4-hydroxythreonine-4-phosphate dehydrogenase; produces the amino-oxo-propyl-phosphate branch feeding PdxJ. Homology-inferred (PE=3). **Covered.**

**pdxJ — PP_1436 (Q88MY2, K03474, EC 2.6.99.2).** Pyridoxine-5'-phosphate synthase; catalyzes the ring-closing condensation of DXP with 1-amino-acetone-3-phosphate — the penultimate de novo step. This step **requires DXP from dxs (PP_0527)**, establishing the cross-map dependency ([PMID: 11286891](https://pubmed.ncbi.nlm.nih.gov/11286891/), [PMID: 12206776](https://pubmed.ncbi.nlm.nih.gov/12206776/)). Dedicated to `ppu00750`. Homology-inferred (PE=3). **Covered.**

**pdxH — PP_1129 (Q88NS5, K00275, EC 1.4.3.5).** Pyridoxine/pyridoxamine-5'-phosphate oxidase (PNPOx); performs the final oxidation to PLP and also serves the salvage branch. Note the alternate name "pyridoxal 5'-phosphate synthase" carried by this oxidase caused a proteome text-search hit — it should not be confused with the DXP-independent Pdx1/Pdx2 "PLP synthase." Dedicated to `ppu00750`. Homology-inferred (PE=3). **Covered.**

### Salvage kinase

**pdxY — PP_5357 (Q88C26, K00868, EC 2.7.1.35).** Pyridoxal kinase. A proteome-wide UniProt query for EC 2.7.1.35 returned **exactly one** protein (Q88C26), confirming this is the **sole** B6 salvage kinase in KT2440 with no second *pdxK* paralog. Naming is inconsistent across databases (UniProt "Pyridoxal kinase PdxY"; KEGG "Pyridoxamine kinase") — a curation flag but not a functional concern. **Covered** for salvage; contributes to PLP regeneration alongside pdxH.

### Over-propagated / misplaced candidates

**thrC — PP_1471 (Q88MU7, K01733, EC 4.2.3.1).** Canonical **threonine synthase** (InterPro IPR004450 Thr_synthase-like; keywords Amino-acid biosynthesis / Lyase / PLP). This is a PLP-*dependent* enzyme of Gly/Ser/Thr metabolism, **not** a PLP-biosynthetic enzyme. It appears in `ppu00750` purely because it carries the "Pyridoxal phosphate" cofactor keyword. **Reassign to `ppu00260`; mark as map artifact.**

**PP_0662 (Q88Q36, K01733).** Annotated only as "Threonine synthase" (submitted name), but is a **weak, divergent paralog**: UniProt PE=4 "Predicted," annotation score 1.0, no recommended name, no gene symbol, and — critically — **lacks the diagnostic IPR004450 Thr_synthase-like signature** (carries only the generic PALP/PF00291 fold and a Thr_synth_N domain). It is not a PLP-biosynthetic enzyme and its true function is uncertain. **Reassign out of `ppu00750` and promote to full gene review.**

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### No genuine pathway gaps

Every de novo step (epd, pdxB, serC, pdxA, pdxJ, pdxH) and salvage (pdxY) is encoded. The only step "missing" from the candidate list is the **DXP input from *dxs* (PP_0527)**, and this is a *bucketing artifact*, not a biological gap — *dxs* is present in the genome but assigned to the terpenoid map `ppu00900`. Curators modeling module satisfiability should record *dxs* as a **required external input** to the B6 module.

### Over-annotations (the main curation actions)

1. **PP_0662 and PP_1471 = threonine synthases (K01733), not B6 enzymes.** They are in the Vitamin B6 map only because threonine synthase *uses* PLP. This is the classic "PLP-dependent ≠ PLP-biosynthetic" conflation. Both should be **excluded** from the B6 module.
2. **serC dual role.** Its `ppu00750` membership is real (it moonlights in B6) but it is primarily a serine-biosynthetic enzyme; treat as shared, not B6-dedicated.
3. **pdxH alternate name "PLP synthase."** Do not mistake this oxidase for a Pdx1/Pdx2-type synthase.
4. **pdxY naming inconsistency** ("pyridoxal kinase" vs "pyridoxamine kinase") across UniProt/KEGG.

### Evidence quality caveat

**Every B6 gene in KT2440 is homology-inferred (UniProt PE=3), with no PE=1/2 experimental characterization in this strain.** The pathway assignment is strong at the level of pathway *logic* and cross-species biochemistry, but no KT2440-specific enzymatic assay, knockout, or structure underpins any single gene. This is acceptable for module satisfiability but should be flagged as "inferred, not demonstrated."

### Not expected in this organism

The **DXP-independent PLP synthase (Pdx1/Pdx2; SNZ/SNO; K06215/K08681)** is genomically absent. Proteome searches for "PLP synthase" returned nothing, and no glutamine-amidotransferase-type synthase exists. Mark this step **not_expected_in_target_taxon**.

---

## 6. Module and GO-curation Recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| epd (E4P dehydrogenase) | **covered** | Dedicated gene PP_4964, K03472 |
| pdxB (erythronate-4-P DH) | **covered** | Dedicated gene PP_2117, K03473 |
| serC (transaminase) | **covered** (shared) | PP_1768; moonlighting from serine biosynthesis — robust |
| pdxA (4-HTP dehydrogenase) | **covered** | PP_0402, K00097 |
| pdxJ (PNP synthase) | **covered** | PP_1436, K03474; requires external DXP |
| pdxH (PNP/PMP oxidase → PLP) | **covered** | PP_1129, K00275 |
| pdxY (salvage kinase) | **covered** (sole kinase) | PP_5357, K00868; only EC 2.7.1.35 in proteome |
| *dxs* (DXP input) | **covered but external** | PP_0527 present in `ppu00900`; add as required module input |
| Pdx1/Pdx2 de novo synthase | **not_expected_in_target_taxon** | K06215/K08681 absent; autoexclusive with pdx set |
| PP_0662 "threonine synthase" | **module_needs_revision** (remove) | K01733; weak paralog; not B6-biosynthetic |
| PP_1471 *thrC* | **module_needs_revision** (remove) | K01733; canonical Thr synthase; map artifact |

**Module boundary corrections:**
- **Exclude** the two threonine synthases and serC's serine role from the B6 module; they belong to `ppu00260`.
- **Record *dxs* (PP_0527)** as a required cross-map input (from `ppu00900`) so satisfiability logic does not report a false gap at the PdxJ step.
- **Do not** anchor the module on overview maps `ppu01100`/`ppu01240`.

**GO-curation notes:** No new GO term requests appear strictly necessary. The relevant GO terms (de novo PLP biosynthetic process; the individual enzyme activities) map cleanly onto the seven dedicated/moonlighting genes. If a "DXP-dependent PLP biosynthesis" module document does not yet exist, one should be created to encode the *dxs* input dependency and the autoexclusivity with the Pdx1/Pdx2 route.

---

## 7. Genes to Promote to Full Review

1. **PP_0662 (Q88Q36) — HIGH PRIORITY.** Weakly annotated (PE=4 "Predicted," score 1.0), no gene symbol, no recommended name, lacks the diagnostic threonine-synthase InterPro signature. Its true function is genuinely uncertain and it is currently mis-bucketed into B6. Full `fetch-gene` review needed to determine whether it is a divergent threonine synthase, a different PLP-dependent (fold-type II) enzyme, or a pseudogene/misannotation.
2. **PP_1471 (*thrC*) — LOW PRIORITY (housekeeping).** Function is clear (canonical threonine synthase); only the bucket assignment is wrong. A lightweight reassignment to `ppu00260`, not a full mechanistic review, is required.
3. **PP_0527 (*dxs*) — MEDIUM PRIORITY (cross-linking).** Confirm it should be registered as a required input to the B6 module despite living in the terpenoid map.

The six dedicated de novo enzymes and pdxY are well-supported by homology and consistent KO/EC/pathway assignments; they do not require full review beyond noting the universal PE=3 (inferred-only) evidence level.

---

## 8. Mechanistic Model / Interpretation

The unifying picture is that **KT2440 is an unambiguous DXP-dependent PLP producer**, and the apparent complexity of the `ppu00750` candidate list is an artifact of KEGG's tendency to gather all PLP-*dependent* enzymes into the Vitamin B6 map. Once the two threonine synthases are recognized as PLP-consumers rather than PLP-producers, the pathway collapses to a clean linear model: two dehydrogenase steps (epd, pdxB) prepare the sugar branch; a glutamate-dependent transaminase (serC, borrowed from serine biosynthesis) installs the nitrogen; a third dehydrogenase (pdxA) generates the amino-oxo-propyl-phosphate; PdxJ condenses it with DXP (from the separately-bucketed *dxs*) to form PNP; and PdxH oxidizes PNP to PLP. The salvage kinase pdxY provides a parallel entry from exogenous/recycled vitamers.

The genomic absence of Pdx1/Pdx2 is not merely inferred from a missing KO — it is biochemically *required* by the observed glutamate-nitrogen labeling, since the two routes are mutually exclusive ([PMID: 12686115](https://pubmed.ncbi.nlm.nih.gov/12686115/)). This gives an unusually strong, doubly-supported conclusion: direct isotope tracing in *P. putida* (organism-level evidence) plus a genome-content check (strain-level evidence) both point to the same route. The chief residual uncertainties are (a) the universal reliance on homology inference (PE=3) with zero KT2440-specific experimental validation, and (b) the genuinely ambiguous PP_0662, which is neither a confident threonine synthase nor a confirmed B6 enzyme.

---

## 9. Evidence Base

| PMID | Title | How it supports this review |
|------|-------|-----------------------------|
| [10885790](https://pubmed.ncbi.nlm.nih.gov/10885790/) | *Biosynthesis of pyridoxine: origin of the nitrogen atom of pyridoxine in microorganisms* | **Direct experimental evidence** that in *P. putida* the pyridoxine nitrogen comes from **glutamate** ("the nitrogen atom of glutamate was incorporated into pyridoxine in P. putida, E. aerogenes and E. coli, but not in S. aureus and B. subtilis"), placing KT2440 in the DXP-dependent route. |
| [12775110](https://pubmed.ncbi.nlm.nih.gov/12775110/) | *Biosynthesis of pyridoxine in S. cerevisiae — origin of the pyridoxine nitrogen atom under anaerobic and aerobic conditions* | Confirms *P. putida* groups with *E. coli*: "in the prokaryotes Pseudomonas putida, Enterobacter aerogenes and Escherichia coli, it is the nitrogen atom of glutamate that is incorporated into pyridoxine." |
| [12686115](https://pubmed.ncbi.nlm.nih.gov/12686115/) | *Pyridoxine 5'-phosphate synthase: de novo synthesis of vitamin B6 and beyond* | Establishes the two de novo routes are **"independent and autoexclusive"** (pdx vs SOR1), so a complete *pdx* set implies absence of Pdx1/Pdx2; also notes PNP enters salvage to form PLP. |
| [11286891](https://pubmed.ncbi.nlm.nih.gov/11286891/) | *Structural basis for the function of pyridoxine 5'-phosphate synthase* | Confirms PdxJ condenses **1-deoxy-D-xylulose-5-phosphate** with 1-amino-acetone-3-phosphate → establishes the *dxs*/DXP dependency of the PdxJ step. |
| [12206776](https://pubmed.ncbi.nlm.nih.gov/12206776/) | *Enzyme-ligand complexes of pyridoxine 5'-phosphate synthase: implications for substrate binding and catalysis* | Independent confirmation that DXP feeds the penultimate condensation ("the complicated ring-closure reaction between 1-deoxy-D-xylulose-5-phosphate and 1-amino-acetone-3-phosphate"), supporting inclusion of *dxs* as a required (externally-bucketed) input. |
| [12269807](https://pubmed.ncbi.nlm.nih.gov/12269807/) | *Multistate binding in pyridoxine 5'-phosphate synthase: 1.96 Å crystal structure in complex with 1-deoxy-D-xylulose phosphate* | Structural corroboration of the PdxJ–DXP mechanism and substrate specificity. |

**Species-transfer note.** The two most decisive papers ([PMID: 10885790](https://pubmed.ncbi.nlm.nih.gov/10885790/), [PMID: 12775110](https://pubmed.ncbi.nlm.nih.gov/12775110/)) report tracing experiments performed **directly in *P. putida***, so transfer to KT2440 is strong (species-level, likely strain-general). The PdxJ mechanistic/structural papers derive from *E. coli*/*Mycobacterium*-type enzymes and are used to model *step order and substrate requirements*; their transfer to KT2440 is at the level of conserved enzyme chemistry (strong for mechanism, but not a KT2440-specific assay).

---

## 10. Limitations and Knowledge Gaps

1. **No strain-specific experimental evidence.** All gene assignments are homology-inferred (UniProt PE=3); no KT2440 knockout, complementation, enzymatic assay, or structure exists for any B6 gene. The isotope-labeling evidence, while direct for *P. putida*, is not resolved to the KT2440 strain specifically.
2. **PP_0662 function unresolved.** Its divergence from canonical threonine synthase leaves its role genuinely open.
3. **DXP-flux coupling untested.** The dependence of PdxJ on *dxs*-supplied DXP is inferred from *E. coli*/structural work, not measured in KT2440; competition with isoprenoid biosynthesis for the shared DXP pool is unstudied here.
4. **Salvage completeness.** Only one kinase (pdxY) was found; whether KT2440 imports specific B6 vitamers or relies primarily on de novo synthesis was not examined.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Curation (immediate):** Reassign PP_0662 and PP_1471 out of `ppu00750` into `ppu00260`; register *dxs* (PP_0527) as a required external input to the B6 module; mark the Pdx1/Pdx2 step `not_expected_in_target_taxon`.
2. **Promote PP_0662** to full `fetch-gene` review to resolve its function (divergent Thr synthase vs other fold-type-II PLP enzyme vs misannotation).
3. **Experimental (if warranted):** Single-gene deletions of *pdxJ*, *pdxB*, *pdxA*, or *pdxH* in KT2440 to confirm B6 auxotrophy; and a *dxs* conditional mutant to test the shared-precursor dependency of PdxJ.
4. **Comparative:** Confirm the genomic absence of SNZ/SNO across additional *P. putida* strains to ensure the DXP-dependent assignment is lineage-wide, not KT2440-specific.

---

### Bottom line for module satisfiability

The DXP-dependent PLP biosynthesis module is **SATISFIABLE** in *P. putida* KT2440: all six de novo steps plus salvage are covered by candidate genes, the required DXP input (*dxs*) is present (external bucket), and the mutually exclusive DXP-independent route is correctly absent. The only edits required are removal of two over-propagated threonine synthases (PP_0662, PP_1471) from the B6 bucket and elevation of PP_0662 to full gene review.


## Artifacts

- [OpenScientist final report](PSEPK__dxp-dependent-pyridoxal-5-phosphate-biosynthesis__ppu00750-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__dxp-dependent-pyridoxal-5-phosphate-biosynthesis__ppu00750-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10885790
2. PMID:12775110
3. PMID:12686115
4. PMID:11286891
5. PMID:12206776