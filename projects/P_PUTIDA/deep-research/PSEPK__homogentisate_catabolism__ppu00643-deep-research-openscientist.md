---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T11:45:37.585627'
end_time: '2026-07-23T12:01:20.329263'
duration_seconds: 942.74
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Homogentisate catabolism
  module_summary: A reusable three-reaction pathway that opens the aromatic ring of
    homogentisate to form maleylacetoacetate, isomerizes maleylacetoacetate to fumarylacetoacetate,
    and hydrolyzes fumarylacetoacetate to fumarate and acetoacetate. This lower pathway
    accepts homogentisate from multiple upstream aromatic-substrate routes and ends
    at metabolites that can enter central carbon metabolism.
  module_outline: "- Homogentisate catabolism\n  - 1. homogentisate ring cleavage\n\
    \  - Homogentisate oxidative ring cleavage\n    - Homogentisate 1,2-dioxygenase\
    \ (molecular player: HmgA homogentisate 1,2-dioxygenases; activity or role: homogentisate\
    \ 1,2-dioxygenase activity)\n  - 2. maleylacetoacetate isomerization\n  - Maleylacetoacetate\
    \ isomerization\n    - Maleylacetoacetate isomerase (molecular player: HmgC maleylacetoacetate\
    \ isomerases; activity or role: maleylacetoacetate isomerase activity)\n  - 3.\
    \ fumarylacetoacetate hydrolysis\n  - Fumarylacetoacetate hydrolysis\n    - Fumarylacetoacetase\
    \ (molecular player: HmgB fumarylacetoacetases; activity or role: fumarylacetoacetase\
    \ activity)"
  module_connections: '- Homogentisate oxidative ring cleavage feeds into Maleylacetoacetate
    isomerization: HmgA produces maleylacetoacetate for HmgC.

    - Maleylacetoacetate isomerization feeds into Fumarylacetoacetate hydrolysis:
    HmgC produces fumarylacetoacetate for HmgB.'
  pathway_query: ppu00643
  pathway_id: ppu00643
  pathway_name: Styrene degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00643 with 5 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '5'
  candidate_genes: '- PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary
    bucket kegg:ppu00643)

    - peaE: PP_3463 | Q88H97 | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) (EC
    1.2.1.39; primary bucket kegg:ppu00643)

    - hmgC: PP_4619 | Q88E49 | Maleylacetoacetate isomerase (EC 5.2.1.2) (EC 5.2.1.2;
    primary bucket kegg:ppu00643)

    - hmgB: PP_4620 | Q88E48 | fumarylacetoacetase (EC 3.7.1.2) (EC 3.7.1.2; primary
    bucket kegg:ppu00643)

    - hmgA: PP_4621 | Q88E47 | Homogentisate 1,2-dioxygenase (HGDO) (EC 1.13.11.5)
    (Homogentisate oxygenase) (Homogentisic acid oxidase) (Homogentisicase) (EC 1.13.11.5;
    primary bucket kegg:ppu00643)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: PSEPK__homogentisate_catabolism__ppu00643-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__homogentisate_catabolism__ppu00643-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Homogentisate catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00643
- Resolved ID: ppu00643
- Resolved name: Styrene degradation
- Source: KEGG

Resolved local bucket kegg:ppu00643 with 5 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 5

- PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)
- peaE: PP_3463 | Q88H97 | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) (EC 1.2.1.39; primary bucket kegg:ppu00643)
- hmgC: PP_4619 | Q88E49 | Maleylacetoacetate isomerase (EC 5.2.1.2) (EC 5.2.1.2; primary bucket kegg:ppu00643)
- hmgB: PP_4620 | Q88E48 | fumarylacetoacetase (EC 3.7.1.2) (EC 3.7.1.2; primary bucket kegg:ppu00643)
- hmgA: PP_4621 | Q88E47 | Homogentisate 1,2-dioxygenase (HGDO) (EC 1.13.11.5) (Homogentisate oxygenase) (Homogentisic acid oxidase) (Homogentisicase) (EC 1.13.11.5; primary bucket kegg:ppu00643)

## Generic Module Context

### Working Scope

A reusable three-reaction pathway that opens the aromatic ring of homogentisate to form maleylacetoacetate, isomerizes maleylacetoacetate to fumarylacetoacetate, and hydrolyzes fumarylacetoacetate to fumarate and acetoacetate. This lower pathway accepts homogentisate from multiple upstream aromatic-substrate routes and ends at metabolites that can enter central carbon metabolism.

### Provisional Biological Outline

- Homogentisate catabolism
  - 1. homogentisate ring cleavage
  - Homogentisate oxidative ring cleavage
    - Homogentisate 1,2-dioxygenase (molecular player: HmgA homogentisate 1,2-dioxygenases; activity or role: homogentisate 1,2-dioxygenase activity)
  - 2. maleylacetoacetate isomerization
  - Maleylacetoacetate isomerization
    - Maleylacetoacetate isomerase (molecular player: HmgC maleylacetoacetate isomerases; activity or role: maleylacetoacetate isomerase activity)
  - 3. fumarylacetoacetate hydrolysis
  - Fumarylacetoacetate hydrolysis
    - Fumarylacetoacetase (molecular player: HmgB fumarylacetoacetases; activity or role: fumarylacetoacetase activity)

### Known Relationships Among Steps

- Homogentisate oxidative ring cleavage feeds into Maleylacetoacetate isomerization: HmgA produces maleylacetoacetate for HmgC.
- Maleylacetoacetate isomerization feeds into Fumarylacetoacetate hydrolysis: HmgC produces fumarylacetoacetate for HmgB.

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

# Homogentisate Catabolism in *Pseudomonas putida* KT2440 — Module/Pathway Review

**Review topic:** Homogentisate catabolism (lower/central pathway) in *Pseudomonas putida* KT2440
**Target taxon:** PSEPK — *Pseudomonas putida* KT2440 (NCBI taxon 160488; proteome UP000000556)
**Queried bucket:** `kegg:ppu00643` (KEGG "Styrene degradation"), module area: aromatic_and_xenobiotic_catabolism
**Candidate genes:** PP_2932, peaE/PP_3463, hmgC/PP_4619, hmgB/PP_4620, hmgA/PP_4621

---

## 1. Executive Summary

The three-reaction homogentisate central (lower) pathway is **fully present, operonic, and directly characterized** in *Pseudomonas putida* KT2440. All three expected module steps map cleanly onto the co-clustered `hmgABC` genes: **HmgA** (homogentisate 1,2-dioxygenase, EC 1.13.11.5, PP_4621/Q88E47), **HmgC** (glutathione-dependent maleylacetoacetate isomerase, EC 5.2.1.2, PP_4619/Q88E49), and **HmgB** (fumarylacetoacetate hydrolase / fumarylacetoacetase, EC 3.7.1.2, PP_4620/Q88E48). This is not an inference from homology alone: the pathway was biochemically and genetically dissected in *P. putida* by Arias-Barrau et al. ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)), predicted from the KT2440 genome by Jiménez et al. ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)), and HmgA was detected at the protein level in KT2440 by proteomics ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)). The module should therefore be marked **covered** with strong, species-level evidence.

The central curation finding is that the queried bucket is **the wrong container** for two of the five candidate genes. `kegg:ppu00643` resolves to the KEGG "Styrene degradation" overview map, a heterogeneous map that embeds the homogentisate branch alongside phenylacetaldehyde/phenylacetate chemistry. As a result, two genes that have nothing to do with homogentisate ring cleavage were swept into the bucket: **peaE/PP_3463** (phenylacetaldehyde dehydrogenase, feeding the phenylacetyl-CoA route) and **PP_2932** (a generic, unannotated amidase-family protein). Neither belongs to the three-reaction homogentisate module and both should be excluded from module satisfiability accounting.

Two curation caveats remain for the genuine `hmg` genes. First, the reviewed Swiss-Prot entry for HmgA (Q88E47) carries DNA-binding transcription-repressor GO terms that biologically belong to the co-encoded IclR-type regulator **HmgR**, not to the dioxygenase — a likely annotation mis-merge. Second, HmgB and HmgC are **TrEMBL (unreviewed)** entries, and HmgC lacks a recommended protein name; both warrant promotion to full gene review. The module is satisfiable today, but the bucket definition and two propagated annotations need correction.

---

## 2. Target-Organism Pathway Definition

### What the pathway is

The homogentisate central pathway is a **reusable three-reaction lower pathway** that channels homogentisate (2,5-dihydroxyphenylacetate) into central carbon metabolism. In *P. putida* KT2440 the reactions are:

1. **Oxidative aromatic ring cleavage** of homogentisate → 4-maleylacetoacetate, by homogentisate 1,2-dioxygenase (HmgA, a non-heme Fe(II) enzyme).
2. **cis–trans isomerization** of 4-maleylacetoacetate → 4-fumarylacetoacetate, by maleylacetoacetate isomerase (HmgC, a glutathione-dependent GST-zeta family enzyme).
3. **Hydrolysis** of 4-fumarylacetoacetate → **fumarate + acetoacetate**, by fumarylacetoacetate hydrolase / fumarylacetoacetase (HmgB).

The two end products enter the TCA cycle (fumarate) and ketone-body/acetyl-CoA metabolism (acetoacetate). This is a **convergent central route**: it accepts homogentisate produced by several distinct upstream peripheral pathways.

### Upstream feeders (kept separate from the module)

In *P. putida*, homogentisate is generated from **L-phenylalanine and L-tyrosine** (via the Phh/Hpd route: phenylalanine → tyrosine → 4-hydroxyphenylpyruvate → homogentisate, by 4-hydroxyphenylpyruvate dioxygenase, Hpd) and from **3-hydroxyphenylacetate** (via the two-component hydroxylase MhaAB in the related strain *P. putida* U) ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/); [PMID: 15866873](https://pubmed.ncbi.nlm.nih.gov/15866873/)). These upstream steps (Phh, Hpd, Mha) are **separate modules** and must not be folded into the three-reaction homogentisate lower pathway.

### Boundaries and neighboring maps to keep distinct

- **KEGG "Styrene degradation" (map00643 / ppu00643)** — an overview map, *not* a clean module. It bundles the homogentisate branch with phenylacetaldehyde/phenylacetate chemistry. Membership in this map does **not** imply membership in the homogentisate module.
- **Phenylacetyl-CoA (paa) pathway** — the destination of phenylacetaldehyde dehydrogenase (peaE) product phenylacetate; a distinct catabolic route ([PMID: 20050871](https://pubmed.ncbi.nlm.nih.gov/20050871/)).
- **KEGG "Tyrosine metabolism" / "Phenylalanine metabolism"** — where UniProt and KEGG place hmgABC as the terminal steps of aromatic amino-acid degradation.

### Alternate names / database-specific definitions

- **HmgA**: homogentisate 1,2-dioxygenase; homogentisate oxygenase; homogentisic acid oxidase; homogentisicase; HGDO/HGD (human ortholog nomenclature). EC 1.13.11.5.
- **HmgB**: fumarylacetoacetate hydrolase (FAH); fumarylacetoacetase. EC 3.7.1.2. (Note: gene-letter/enzyme pairing differs across databases — in KT2440 metadata, *hmgB* = the hydrolase and *hmgC* = the isomerase.)
- **HmgC**: maleylacetoacetate isomerase (MAAI); glutathione S-transferase zeta 1 (GSTZ1) in the mammalian literature; GST-zeta family. EC 5.2.1.2.
- In some *P. putida* genome annotations the operon is written **hmg/fah/mai** ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)).

---

## 3. Expected Step Model

| # | Module step | Activity (GO/EC) | Expected player | KT2440 gene | Status |
|---|-------------|------------------|-----------------|-------------|--------|
| 1 | Homogentisate oxidative ring cleavage | homogentisate 1,2-dioxygenase (EC 1.13.11.5) | HmgA | **PP_4621 (hmgA, Q88E47)** | **Covered — direct** |
| 2 | Maleylacetoacetate isomerization | maleylacetoacetate isomerase (EC 5.2.1.2) | HmgC | **PP_4619 (hmgC, Q88E49)** | **Covered — strong** |
| 3 | Fumarylacetoacetate hydrolysis | fumarylacetoacetase (EC 3.7.1.2) | HmgB | **PP_4620 (hmgB, Q88E48)** | **Covered — strong** |

**Step relationships (linear, product-to-substrate coupled):**

```
 L-Phe / L-Tyr / 3-OH-phenylacetate   (upstream, SEPARATE modules)
                 │
                 ▼
          homogentisate
                 │  HmgA  (PP_4621, EC 1.13.11.5, O2, Fe(II))   ── STEP 1
                 ▼
        4-maleylacetoacetate
                 │  HmgC  (PP_4619, EC 5.2.1.2, glutathione)     ── STEP 2
                 ▼
       4-fumarylacetoacetate
                 │  HmgB  (PP_4620, EC 3.7.1.2, hydrolysis)      ── STEP 3
                 ▼
         fumarate  +  acetoacetate  →  central carbon metabolism
```

All three steps are encoded, contiguous, and co-regulated in KT2440 — the module is topologically complete with no orphan steps.

---

## 4. Candidate Genes and Evidence

### 4.1 hmgA / PP_4621 (Q88E47) — homogentisate 1,2-dioxygenase — **HIGH CONFIDENCE**

- **Role:** Step 1, oxidative ring cleavage of homogentisate to maleylacetoacetate. Non-heme Fe(II) dioxygenase, EC 1.13.11.5.
- **Evidence type:** *Direct, target-species.* Biochemically/genetically characterized in *P. putida* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)): "*Homogentisate is then catabolized by a central catabolic pathway that involves three enzymes, homogentisate dioxygenase (HmgA), fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC), finally yielding fumarate and acetoacetate.*" Detected at the protein level in KT2440 by 2-DE/MS proteomics, induced by phenylalanine ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)): "*Phenylalanine induced 4-hydroxyphenyl-pyruvate dioxygenase (Hpd) and homogentisate 1,2-dioxygenase (HmgA), key enzymes in the homogentisate degradation pathway.*" Swiss-Prot **reviewed**.
- **Curation caveat:** The Swiss-Prot entry over-merges regulator function. It carries GO terms *DNA-binding transcription repressor activity*, *protein-DNA complex*, and *negative regulation of DNA-templated transcription* alongside the correct *homogentisate 1,2-dioxygenase activity* and *iron ion binding*. The transcription-repressor terms biologically belong to the co-encoded IclR-type repressor **HmgR** ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)), not to the dioxygenase — a probable annotation mis-merge that should be flagged for correction.

### 4.2 hmgC / PP_4619 (Q88E49) — maleylacetoacetate isomerase — **HIGH CONFIDENCE**

- **Role:** Step 2, glutathione-dependent cis–trans isomerization of maleylacetoacetate to fumarylacetoacetate, EC 5.2.1.2. Member of the GST-zeta (GSTZ1/MAAI) family.
- **Evidence type:** *Strong; species-genomic + biochemical pathway context.* Named as one of the three central-pathway enzymes in *P. putida* ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)) and predicted in the KT2440 genome ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)). Family-level biochemistry (glutathione dependence, bifunctional GSTZ1/MAAI) is well established ([PMID: 37742772](https://pubmed.ncbi.nlm.nih.gov/37742772/)).
- **Curation caveat:** **TrEMBL (unreviewed)**; the entry has **no recommended protein name** and is annotated via GST/glutathione-transferase + maleylacetoacetate-isomerase GO. Family membership (GST superfamily) can attract broad, generic GST GO terms; ensure the specific EC 5.2.1.2 / MAAI activity is retained and generic "glutathione transferase" terms are not over-weighted. **Promote to full gene review.**

### 4.3 hmgB / PP_4620 (Q88E48) — fumarylacetoacetate hydrolase — **HIGH CONFIDENCE**

- **Role:** Step 3, hydrolysis of fumarylacetoacetate to fumarate + acetoacetate, EC 3.7.1.2 (FAH/fumarylacetoacetase family).
- **Evidence type:** *Strong; species-genomic + biochemical pathway context.* Named as one of the three central-pathway enzymes ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/)); part of the single `hmgABC` transcriptional unit in *P. putida*: "*the hmgABC genes appear to form a single transcriptional unit.*"
- **Curation caveat:** **TrEMBL (unreviewed).** FAH-family proteins are a large superfamily; confirm the specific fumarylacetoacetase activity rather than a generic FAH-domain assignment. **Promote to full gene review.**

### 4.4 peaE / PP_3463 (Q88H97) — phenylacetaldehyde dehydrogenase — **MIS-BUCKETED (exclude)**

- **Annotated role:** Phenylacetaldehyde dehydrogenase (NAD+), EC 1.2.1.39 — converts phenylacetaldehyde → phenylacetate, feeding the **phenylacetyl-CoA (paa)** route.
- **Why it is in the bucket:** It is a component of the KEGG "Styrene degradation" overview map (styrene → styrene oxide → phenylacetaldehyde → phenylacetate), *not* of the homogentisate branch. UniProt annotates it only with *phenylacetaldehyde dehydrogenase (NAD+) activity*. Homologous to the well-characterized styrene-pathway phenylacetaldehyde dehydrogenase of *P. putida* S12 ([PMID: 28153386](https://pubmed.ncbi.nlm.nih.gov/28153386/): "*Structure and biochemistry of phenylacetaldehyde dehydrogenase from the Pseudomonas putida S12 styrene catabolic pathway.*").
- **Curation action:** **Not part of the homogentisate module.** Remove from module satisfiability accounting; it belongs to a styrene/phenylacetate module.

### 4.5 PP_2932 (Q88IR7) — Amidase family protein — **MIS-BUCKETED (exclude)**

- **Annotated role:** Generic "Amidase family protein" — **no EC, no UniProt function/pathway/GO** annotation.
- **Why it is in the bucket:** Co-occurrence in the heterogeneous KEGG map; no biochemical link to any homogentisate step.
- **Curation action:** **Not part of the homogentisate module.** Exclude. If curation attention is warranted at all, it is as an unrelated amidase, not a homogentisate enzyme.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**No true pathway gaps.** All three enzymatic steps are covered by contiguous, co-regulated genes with direct or strong species evidence. There is no missing step, no need for a lineage-specific alternative enzyme, and no step "not expected" in this organism — homogentisate catabolism is a core, experimentally confirmed capability of *P. putida* KT2440.

**Bucket / boundary problem (primary issue).** The `kegg:ppu00643` "Styrene degradation" map is an overview map that conflates two biochemically distinct destinations. Of the 5 candidates, **only 3 (60%)** belong to the homogentisate module; the other 2 (peaE, PP_2932) are artifacts of overview-map membership. Any module-satisfiability logic keyed on this KEGG bucket will mis-count without manual pruning.

**Over-propagation / mis-merge on HmgA.** The Swiss-Prot HmgA entry (Q88E47) mixes dioxygenase activity with transcription-repressor GO terms that belong to HmgR. This is a concrete example of feature mis-merge between two genes of the same operon and should be reported to UniProt curation.

**Broad-family GO risk on HmgC.** HmgC sits in the GST-zeta / GSTZ1 family, which in eukaryotes has pleiotropic annotations (drug metabolism, ferroptosis, cancer biomarker roles — [PMID: 37742772](https://pubmed.ncbi.nlm.nih.gov/37742772/), [PMID: 36905252](https://pubmed.ncbi.nlm.nih.gov/36905252/), [PMID: 35562974](https://pubmed.ncbi.nlm.nih.gov/35562974/)). Those eukaryote-specific roles must **not** propagate to the bacterial enzyme; only EC 5.2.1.2 / MAAI activity is appropriate.

**Regulatory conditionality (not a gap, but curation-relevant).** Expression of `hmgA`/`hpd` is under **carbon catabolite (Crc) repression** in *P. putida* ([PMID: 14973036](https://pubmed.ncbi.nlm.nih.gov/14973036/): "*Crc is involved in the catabolic repression of the hpd and hmgA genes from the homogentisate pathway*") and induced by homogentisate via the IclR-type repressor HmgR. The module is present but conditionally expressed; absence of expression under a given condition should not be read as absence of the genes.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| 1. Homogentisate ring cleavage (HmgA) | **covered** | Direct target-species biochemistry + KT2440 proteomics ([PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/), [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)) |
| 2. Maleylacetoacetate isomerization (HmgC) | **covered** | Named central-pathway enzyme; genomic + family biochemistry; PP_4619 unambiguous |
| 3. Fumarylacetoacetate hydrolysis (HmgB) | **covered** | Named central-pathway enzyme; operonic; PP_4620 unambiguous |

**Bucket-level actions:**

1. **Do not treat `kegg:ppu00643` as the homogentisate module.** The clean module is the `hmgABC` operon (PP_4619–PP_4621), best associated with KEGG Tyrosine/Phenylalanine metabolism, not "Styrene degradation." Consider re-anchoring the module to the operon or to a homogentisate-specific KEGG module rather than the overview map.
2. **Remove peaE/PP_3463 and PP_2932** from the homogentisate module. Re-file peaE under a styrene/phenylacetaldehyde→phenylacetate (paa) module; leave PP_2932 as an unrelated amidase.
3. **No `not_expected_in_target_taxon` calls needed** — every module step is expected and present.
4. **No new module document strictly required** for homogentisate itself, but a separate **styrene/phenylacetaldehyde module** would cleanly absorb peaE and prevent future mis-bucketing from the same overview map.

**GO/UniProt curation requests:**

- **HmgA (Q88E47):** request removal/relocation of DNA-binding transcription-repressor GO terms (belong to HmgR); retain *homogentisate 1,2-dioxygenase activity* (GO:0004411) and *iron ion binding*.
- **HmgC (Q88E49):** add recommended protein name "Maleylacetoacetate isomerase"; ensure EC 5.2.1.2 / MAAI GO is primary; guard against generic GST or eukaryote-specific GSTZ1 terms.
- **HmgB (Q88E48):** confirm specific fumarylacetoacetase (EC 3.7.1.2) activity over generic FAH-domain annotation.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Gene | UniProt | Reason to promote |
|------|---------|-------------------|
| **hmgB / PP_4620** | Q88E48 (TrEMBL) | Unreviewed; verify specific fumarylacetoacetase activity vs. broad FAH family; core module step |
| **hmgC / PP_4619** | Q88E49 (TrEMBL) | Unreviewed; **no recommended protein name**; GST-zeta family broad-annotation risk; core module step |
| **hmgA / PP_4621** | Q88E47 (Swiss-Prot) | Reviewed, but flag the HmgR transcription-repressor GO mis-merge for correction |

peaE/PP_3463 and PP_2932 do **not** warrant homogentisate-module review; they should be re-routed out of this bucket.

---

## 8. Key References

- Arias-Barrau E, et al. *The homogentisate pathway: a central catabolic pathway involved in the degradation of L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate in Pseudomonas putida.* J Bacteriol. 2004. [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/) — **Primary direct evidence**: defines HmgA/HmgB/HmgC, the operon, and HmgR regulation.
- Jiménez JI, et al. *Genomic analysis of the aromatic catabolic pathways from Pseudomonas putida KT2440.* Environ Microbiol. 2002. [PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/) — Genome-level prediction of the homogentisate (hmg/fah/mai) pathway in the exact target strain.
- Kim YH, et al. *Analysis of aromatic catabolic pathways in Pseudomonas putida KT2440 using a combined proteomic approach: 2-DE/MS and cleavable isotope-coded affinity tag analysis.* Proteomics. 2006. [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) — Protein-level detection of HmgA induction in KT2440.
- Morales G, et al. *The Pseudomonas putida Crc global regulator controls the expression of genes from several chromosomal catabolic pathways for aromatic compounds.* J Bacteriol. 2004. [PMID: 14973036](https://pubmed.ncbi.nlm.nih.gov/14973036/) — Crc catabolite repression of hmgA/hpd.
- Herrera MC & Ramos JL. *Identification and characterization of the PhhR regulon in Pseudomonas putida.* 2010. [PMID: 20050871](https://pubmed.ncbi.nlm.nih.gov/20050871/) — Upstream Phe/Tyr regulon and the distinct paa route (context for peaE mis-bucketing).
- Arias-Barrau E, et al. *A two-component hydroxylase involved in the assimilation of 3-hydroxyphenyl acetate in Pseudomonas putida.* 2005. [PMID: 15866873](https://pubmed.ncbi.nlm.nih.gov/15866873/) — Upstream 3-OH-phenylacetate → homogentisate feeder (MhaAB); HmgABC as convergent central route.
- Crabo AG, et al. *Structure and biochemistry of phenylacetaldehyde dehydrogenase from the Pseudomonas putida S12 styrene catabolic pathway.* 2017. [PMID: 28153386](https://pubmed.ncbi.nlm.nih.gov/28153386/) — Confirms peaE-type enzyme belongs to the styrene/phenylacetate route, not homogentisate.
- Board PG. *Clinical physiology and pharmacology of GSTZ1/MAAI.* 2023. [PMID: 37742772](https://pubmed.ncbi.nlm.nih.gov/37742772/) — MAAI/GSTZ1 family biochemistry relevant to HmgC annotation.

---

### Bottom line for curation

Mark all three homogentisate module steps **covered** in *P. putida* KT2440 on the strength of the operonic `hmgABC` genes (PP_4619–PP_4621) with direct species evidence. Prune peaE/PP_3463 and PP_2932 from the bucket as overview-map artifacts. Promote HmgB and HmgC (TrEMBL) to full gene review, and flag the HmgA→HmgR transcription-repressor GO mis-merge for correction.


## Artifacts

- [OpenScientist final report](PSEPK__homogentisate_catabolism__ppu00643-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__homogentisate_catabolism__ppu00643-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15262943
2. PMID:12534466
3. PMID:16470664
4. PMID:15866873
5. PMID:20050871
6. PMID:37742772
7. PMID:28153386
8. PMID:36905252
9. PMID:35562974
10. PMID:14973036