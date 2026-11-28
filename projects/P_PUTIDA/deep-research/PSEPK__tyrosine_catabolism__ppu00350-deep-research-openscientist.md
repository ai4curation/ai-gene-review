---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:05:32.143595'
end_time: '2026-08-31T21:28:41.463373'
duration_seconds: 1389.32
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-tyrosine catabolism to fumarate and acetoacetate
  module_summary: A five-reaction route that converts L-tyrosine to fumarate and acetoacetate.
    Tyrosine aminotransferase forms 4-hydroxyphenylpyruvate; HPD forms homogentisate;
    homogentisate 1,2-dioxygenase cleaves the aromatic ring; maleylacetoacetate isomerase
    forms fumarylacetoacetate; and fumarylacetoacetase releases the two central-metabolism
    products. The same lower homogentisate pathway can receive carbon from additional
    aromatic substrates, but those entry routes are outside this module.
  module_outline: "- L-tyrosine catabolism\n  - 1. transamination (entry step)\n \
    \ - L-tyrosine + 2-oxoglutarate to 4-hydroxyphenylpyruvate + L-glutamate\n   \
    \ - TAT: tyrosine aminotransferase (molecular player: Tyrosine aminotransferase\
    \ family (TAT); activity or role: L-tyrosine:2-oxoglutarate transaminase activity)\n\
    \    - TyrB: bacterial aromatic-amino-acid aminotransferase (molecular player:\
    \ Bacterial aromatic-amino-acid aminotransferase family; activity or role: L-tyrosine:2-oxoglutarate\
    \ transaminase activity)\n  - 2. oxidative decarboxylation to homogentisate\n\
    \  - 4-hydroxyphenylpyruvate + O2 to homogentisate + CO2\n    - HPD/HPPD: 4-hydroxyphenylpyruvate\
    \ dioxygenase (molecular player: 4-hydroxyphenylpyruvate dioxygenase family (HPD);\
    \ activity or role: 4-hydroxyphenylpyruvate dioxygenase activity)\n  - 3. aromatic\
    \ ring cleavage\n  - homogentisate + O2 to 4-maleylacetoacetate\n    - HGD: homogentisate\
    \ 1,2-dioxygenase (molecular player: Homogentisate 1,2-dioxygenase family (HGD);\
    \ activity or role: homogentisate 1,2-dioxygenase activity)\n  - 4. cis-trans\
    \ isomerization\n  - 4-maleylacetoacetate to 4-fumarylacetoacetate\n    - GSTZ1/MAAI:\
    \ maleylacetoacetate isomerase (molecular player: Maleylacetoacetate isomerase\
    \ / GST-zeta family (GSTZ1); activity or role: maleylacetoacetate isomerase activity)\n\
    \  - 5. terminal hydrolysis to central metabolites\n  - 4-fumarylacetoacetate\
    \ to fumarate + acetoacetate\n    - FAH: fumarylacetoacetate hydrolase (molecular\
    \ player: Fumarylacetoacetate hydrolase family (FAH); activity or role: fumarylacetoacetase\
    \ activity)"
  module_connections: '- L-tyrosine + 2-oxoglutarate to 4-hydroxyphenylpyruvate +
    L-glutamate feeds into 4-hydroxyphenylpyruvate + O2 to homogentisate + CO2: 4-hydroxyphenylpyruvate
    from TAT is the substrate of HPD.

    - 4-hydroxyphenylpyruvate + O2 to homogentisate + CO2 feeds into homogentisate
    + O2 to 4-maleylacetoacetate: Homogentisate from HPD is the substrate of HGD.

    - homogentisate + O2 to 4-maleylacetoacetate feeds into 4-maleylacetoacetate to
    4-fumarylacetoacetate: 4-maleylacetoacetate from HGD is isomerised by GSTZ1/MAAI.

    - 4-maleylacetoacetate to 4-fumarylacetoacetate feeds into 4-fumarylacetoacetate
    to fumarate + acetoacetate: 4-fumarylacetoacetate from GSTZ1 is hydrolysed by
    FAH.'
  pathway_query: ppu00350
  pathway_id: ppu00350
  pathway_name: Tyrosine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00350 with 6 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '16'
  candidate_genes: '- davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase
    (EC 1.2.1.-) (EC 1.2.1.-; primary bucket kegg:ppu00350)

    - hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9)
    (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - PP_1709: PP_1709 | Q88M65 | Fumarylacetoacetate hydrolase family protein (primary
    bucket kegg:ppu00350)

    - tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase
    (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)

    - PP_2552: PP_2552 | Q88JU5 | DOPA decarboxylase (EC 4.1.1.28) (EC 4.1.1.28; primary
    bucket kegg:ppu00350)

    - hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27)
    (EC 1.13.11.27; primary bucket kegg:ppu00130)

    - peaE: PP_3463 | Q88H97 | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) (EC
    1.2.1.39; primary bucket kegg:ppu00643)

    - amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary
    bucket kegg:ppu00401)

    - adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1)
    (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)

    - gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC
    1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)

    - hmgC: PP_4619 | Q88E49 | Maleylacetoacetate isomerase (EC 5.2.1.2) (EC 5.2.1.2;
    primary bucket kegg:ppu00643)

    - hmgB: PP_4620 | Q88E48 | fumarylacetoacetase (EC 3.7.1.2) (EC 3.7.1.2; primary
    bucket kegg:ppu00643)

    - hmgA: PP_4621 | Q88E47 | Homogentisate 1,2-dioxygenase (HGDO) (EC 1.13.11.5)
    (Homogentisate oxygenase) (Homogentisic acid oxidase) (Homogentisicase) (EC 1.13.11.5;
    primary bucket kegg:ppu00643)

    - PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00350)'
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__tyrosine_catabolism__ppu00350-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__tyrosine_catabolism__ppu00350-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-tyrosine catabolism to fumarate and acetoacetate in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00350
- Resolved ID: ppu00350
- Resolved name: Tyrosine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00350 with 6 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 16

- davD: PP_0213 | Q88RC0 | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) (EC 1.2.1.-; primary bucket kegg:ppu00350)
- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- PP_1709: PP_1709 | Q88M65 | Fumarylacetoacetate hydrolase family protein (primary bucket kegg:ppu00350)
- tyrB: PP_1972 | Q88LG1 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- sad-I: PP_2488 | Q88K05 | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) (EC 1.2.1.24; primary bucket kegg:ppu00350)
- PP_2552: PP_2552 | Q88JU5 | DOPA decarboxylase (EC 4.1.1.28) (EC 4.1.1.28; primary bucket kegg:ppu00350)
- hpd: PP_3433 | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) (EC 1.13.11.27; primary bucket kegg:ppu00130)
- peaE: PP_3463 | Q88H97 | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) (EC 1.2.1.39; primary bucket kegg:ppu00643)
- amaC: PP_3590 | Q88GX7 | Aminotransferase (EC 2.6.1.-) (EC 2.6.1.-; primary bucket kegg:ppu00401)
- adhP: PP_3839 | Q88G86 | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) (EC 1.1.1.-; 1.1.1.1; primary bucket kegg:ppu00626)
- gabD-II: PP_4422 | Q88EN2 | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) (EC 1.2.1.79; primary bucket kegg:ppu00350)
- hmgC: PP_4619 | Q88E49 | Maleylacetoacetate isomerase (EC 5.2.1.2) (EC 5.2.1.2; primary bucket kegg:ppu00643)
- hmgB: PP_4620 | Q88E48 | fumarylacetoacetase (EC 3.7.1.2) (EC 3.7.1.2; primary bucket kegg:ppu00643)
- hmgA: PP_4621 | Q88E47 | Homogentisate 1,2-dioxygenase (HGDO) (EC 1.13.11.5) (Homogentisate oxygenase) (Homogentisic acid oxidase) (Homogentisicase) (EC 1.13.11.5; primary bucket kegg:ppu00643)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)

## Generic Module Context

### Working Scope

A five-reaction route that converts L-tyrosine to fumarate and acetoacetate. Tyrosine aminotransferase forms 4-hydroxyphenylpyruvate; HPD forms homogentisate; homogentisate 1,2-dioxygenase cleaves the aromatic ring; maleylacetoacetate isomerase forms fumarylacetoacetate; and fumarylacetoacetase releases the two central-metabolism products. The same lower homogentisate pathway can receive carbon from additional aromatic substrates, but those entry routes are outside this module.

### Provisional Biological Outline

- L-tyrosine catabolism
  - 1. transamination (entry step)
  - L-tyrosine + 2-oxoglutarate to 4-hydroxyphenylpyruvate + L-glutamate
    - TAT: tyrosine aminotransferase (molecular player: Tyrosine aminotransferase family (TAT); activity or role: L-tyrosine:2-oxoglutarate transaminase activity)
    - TyrB: bacterial aromatic-amino-acid aminotransferase (molecular player: Bacterial aromatic-amino-acid aminotransferase family; activity or role: L-tyrosine:2-oxoglutarate transaminase activity)
  - 2. oxidative decarboxylation to homogentisate
  - 4-hydroxyphenylpyruvate + O2 to homogentisate + CO2
    - HPD/HPPD: 4-hydroxyphenylpyruvate dioxygenase (molecular player: 4-hydroxyphenylpyruvate dioxygenase family (HPD); activity or role: 4-hydroxyphenylpyruvate dioxygenase activity)
  - 3. aromatic ring cleavage
  - homogentisate + O2 to 4-maleylacetoacetate
    - HGD: homogentisate 1,2-dioxygenase (molecular player: Homogentisate 1,2-dioxygenase family (HGD); activity or role: homogentisate 1,2-dioxygenase activity)
  - 4. cis-trans isomerization
  - 4-maleylacetoacetate to 4-fumarylacetoacetate
    - GSTZ1/MAAI: maleylacetoacetate isomerase (molecular player: Maleylacetoacetate isomerase / GST-zeta family (GSTZ1); activity or role: maleylacetoacetate isomerase activity)
  - 5. terminal hydrolysis to central metabolites
  - 4-fumarylacetoacetate to fumarate + acetoacetate
    - FAH: fumarylacetoacetate hydrolase (molecular player: Fumarylacetoacetate hydrolase family (FAH); activity or role: fumarylacetoacetase activity)

### Known Relationships Among Steps

- L-tyrosine + 2-oxoglutarate to 4-hydroxyphenylpyruvate + L-glutamate feeds into 4-hydroxyphenylpyruvate + O2 to homogentisate + CO2: 4-hydroxyphenylpyruvate from TAT is the substrate of HPD.
- 4-hydroxyphenylpyruvate + O2 to homogentisate + CO2 feeds into homogentisate + O2 to 4-maleylacetoacetate: Homogentisate from HPD is the substrate of HGD.
- homogentisate + O2 to 4-maleylacetoacetate feeds into 4-maleylacetoacetate to 4-fumarylacetoacetate: 4-maleylacetoacetate from HGD is isomerised by GSTZ1/MAAI.
- 4-maleylacetoacetate to 4-fumarylacetoacetate feeds into 4-fumarylacetoacetate to fumarate + acetoacetate: 4-fumarylacetoacetate from GSTZ1 is hydrolysed by FAH.

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

# Module/Pathway/Taxon Review: L-Tyrosine Catabolism to Fumarate and Acetoacetate in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target pathway:** KEGG ppu00350 "Tyrosine metabolism" (module scope: five-reaction route L-tyrosine → fumarate + acetoacetate)
**Module area:** amino-acid metabolism

---

## 1. Executive Summary

The L-tyrosine → fumarate + acetoacetate module is **satisfiable** in *Pseudomonas putida* KT2440. All five expected reactions are encoded in the genome, and the four lower/oxidative steps (steps 2–5) are supported by strong, in some cases direct, target-organism evidence. The route proceeds L-tyrosine → 4-hydroxyphenylpyruvate → homogentisate → 4-maleylacetoacetate → 4-fumarylacetoacetate → fumarate + acetoacetate, and converges on the **homogentisate central catabolic pathway** encoded by the clustered *hmgABC* genes plus *hpd*. These loci map to concrete candidates: **hpd = PP_3433**, **hmgA = PP_4621** (homogentisate 1,2-dioxygenase), **hmgC = PP_4619** (maleylacetoacetate isomerase), and **hmgB = PP_4620** (fumarylacetoacetase). This assignment is anchored by detailed genetic and biochemical characterization in the near-identical strain *P. putida* U [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/), by whole-genome mapping of the KT2440 aromatic catabolic machinery [PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/), and by direct proteomic detection of Hpd and HmgA in KT2440 under aromatic-amino-acid catabolic conditions [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/).

The **only genuinely ambiguous step is the entry transamination** (step 1), which converts L-tyrosine + 2-oxoglutarate to 4-hydroxyphenylpyruvate + L-glutamate. This activity is present but is carried by a promiscuous, paralog-redundant class-I aminotransferase family rather than by a uniquely demonstrated locus. The best candidates are **tyrB = PP_1972** and its equal-length paralog **amaC = PP_3590**; both are annotated (by homology/rule propagation) with the exact GO term for L-tyrosine:2-oxoglutarate transaminase activity. Step 1 should therefore be marked **candidate_uncertain / covered-by-redundant-paralogs**, not gap.

A curation-critical observation is that **most of the 16 metadata candidate genes are over-propagated into KEGG ppu00350 and are not part of this module.** Semialdehyde dehydrogenases (davD, sad-I, gabD-II), a formaldehyde dehydrogenase (frmA), a phenylacetaldehyde dehydrogenase (peaE), a short-chain alcohol dehydrogenase (adhP), a histidine-biosynthesis aminotransferase (hisC), a tryptophan monooxygenase (PP_4983), and a DOPA/tyramine-branch decarboxylase (PP_2552) have no mechanistic role in the tyrosine → fumarate + acetoacetate route. Notably, **PP_1709**, annotated as a "fumarylacetoacetate hydrolase family protein," is a **236-aa FAH-superfamily paralog** that is far too short to be a genuine fumarylacetoacetase (the real HmgB/PP_4620 is 430 aa with EC 3.7.1.2) and should not be counted as a second physiological FAH. A further caveat for automated satisfiability scoring: the true module genes carry KEGG buckets **ppu00643 / ppu00130 / ppu00401** rather than ppu00350, so the raw ppu00350 metadata *understates* real coverage.

---

## 2. Target-Organism Pathway Definition

### 2.1 Exact process included

The module comprises the **catabolic conversion of L-tyrosine into two central-metabolism products, fumarate and acetoacetate**, via five enzymatic reactions:

1. **Transamination** — L-tyrosine + 2-oxoglutarate → 4-hydroxyphenylpyruvate + L-glutamate
2. **Oxidative decarboxylation / hydroxylation** — 4-hydroxyphenylpyruvate + O₂ → homogentisate + CO₂
3. **Aromatic ring cleavage** — homogentisate + O₂ → 4-maleylacetoacetate
4. **cis–trans isomerization** — 4-maleylacetoacetate → 4-fumarylacetoacetate
5. **Terminal hydrolysis** — 4-fumarylacetoacetate → fumarate + acetoacetate

Steps 3–5 constitute the **homogentisate central catabolic pathway**, which in *P. putida* is a hub that also receives carbon from L-phenylalanine (via *phh* → Tyr) and from 3-hydroxyphenylacetate. Fumarate re-enters the TCA cycle; acetoacetate is activated to acetoacetyl-CoA and consumed as an acetyl-CoA source.

### 2.2 Neighboring pathways to keep separate

- **Tyrosine/DOPA decarboxylation branch (Tyr → tyramine/dopamine):** the aromatic-L-amino-acid/DOPA decarboxylase **PP_2552** belongs here, a *different sub-map of ppu00350*, not this module.
- **Phenylalanine hydroxylation (phh):** feeds tyrosine but is an upstream entry route, not part of the five-step module.
- **GABA / succinate-semialdehyde and glutarate-semialdehyde metabolism** (sad-I, gabD-II, davD): distinct semialdehyde dehydrogenase reactions in ppu00350/other maps.
- **Phenylethylamine / phenylacetaldehyde route** (peaE; ppu00360/00643) and **C1/formaldehyde metabolism** (frmA; ppu00626).
- **Broad KEGG overview maps** (e.g., ppu01100 "metabolic pathways," ppu01110 "biosynthesis of secondary metabolites") should not be used to judge satisfiability.

### 2.3 Alternate names / database-specific definitions

- KEGG: **ppu00350 "Tyrosine metabolism"** (broad; includes biosynthesis, decarboxylation, and catabolism branches).
- The catabolic core is variously called the **homogentisate pathway**, the **homogentisate ring-cleavage pathway**, or **"hmg/fah/mai" genes** in the KT2440 genome annotation [PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/).
- MetaCyc: "L-tyrosine degradation I" (homogentisate route).
- Gene-name note: in *P. putida*, the FAH-step gene is **hmgB** (sometimes *fah*) and the isomerase is **hmgC** (sometimes *mai*); this nomenclature swap between databases is a curation hazard.

---

## 3. Expected Step Model and Satisfiability

```
   L-tyrosine
       │  (1) transamination  [TyrB / class-I aromatic aminotransferase]
       │      + 2-oxoglutarate → + L-glutamate
       ▼
  4-hydroxyphenylpyruvate
       │  (2) HPD, EC 1.13.11.27   [hpd = PP_3433] + O2 → + CO2
       ▼
   homogentisate
       │  (3) HGD ring cleavage, EC 1.13.11.5  [hmgA = PP_4621] + O2
       ▼
  4-maleylacetoacetate
       │  (4) MAAI isomerase, EC 5.2.1.2  [hmgC = PP_4619]
       ▼
  4-fumarylacetoacetate
       │  (5) FAH hydrolysis, EC 3.7.1.2  [hmgB = PP_4620]
       ▼
   fumarate + acetoacetate  → central metabolism (TCA / acetyl-CoA)
```

| Step | Reaction | Enzyme / EC | KT2440 locus | Status | Evidence strength |
|------|----------|-------------|--------------|--------|-------------------|
| 1 | Tyr + 2-OG → 4-HPP + Glu | Aromatic aminotransferase, EC 2.6.1.- | tyrB = PP_1972; paralog amaC = PP_3590 | **candidate_uncertain** (covered by redundant paralogs) | Family/rule-based; no locus-unique KT2440 assay |
| 2 | 4-HPP + O₂ → homogentisate + CO₂ | 4-hydroxyphenylpyruvate dioxygenase (HPD), EC 1.13.11.27 | **hpd = PP_3433** | **covered** | Direct KT2440 proteomics + genome mapping |
| 3 | Homogentisate + O₂ → 4-maleylacetoacetate | Homogentisate 1,2-dioxygenase (HGD), EC 1.13.11.5 | **hmgA = PP_4621** | **covered** | Direct KT2440 proteomics; *P. putida* U biochem |
| 4 | 4-maleylacetoacetate → 4-fumarylacetoacetate | Maleylacetoacetate isomerase (MAAI), EC 5.2.1.2 | **hmgC = PP_4619** | **covered** | *P. putida* U biochem; genome cluster |
| 5 | 4-fumarylacetoacetate → fumarate + acetoacetate | Fumarylacetoacetase (FAH), EC 3.7.1.2 | **hmgB = PP_4620** | **covered** | *P. putida* U biochem; genome cluster |

**Bottom line:** 4 of 5 steps are covered with strong evidence; 1 of 5 (entry transamination) is present but gene-ambiguous. The module is **satisfiable**.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence module genes

**hmgA = PP_4621 (Q88E47) — homogentisate 1,2-dioxygenase, EC 1.13.11.5 (step 3).**
This is the ring-cleaving dioxygenase, the committed step of the central pathway. UniProt carries a curated FUNCTION statement explicitly placing HmgA in phenylalanine/tyrosine degradation. HmgA was **directly detected as an induced protein in KT2440** when cells were grown on phenylalanine [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/), and the enzyme is biochemically characterized in *P. putida* U as part of the *hmgABC* transcriptional unit [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/). **High confidence; no caveats.**

**hmgB = PP_4620 (Q88E48) — fumarylacetoacetase, EC 3.7.1.2, 430 aa (step 5).**
The terminal hydrolase releasing fumarate and acetoacetate. It sits immediately adjacent to *hmgA* and *hmgC* in a single operon in *P. putida* U [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/). The 430-aa length and assigned EC 3.7.1.2 are consistent with a genuine FAH. **High confidence.**

**hmgC = PP_4619 (Q88E49) — maleylacetoacetate isomerase, EC 5.2.1.2 (step 4).**
A GST-zeta-family isomerase converting the cis (maleyl) to trans (fumaryl) isomer; glutathione-dependent. Part of the *hmgABC* operon [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/). **High confidence.**

**hpd = PP_3433 (Q88HC7) — 4-hydroxyphenylpyruvate dioxygenase, EC 1.13.11.27 (step 2).**
Produces homogentisate from 4-hydroxyphenylpyruvate. Directly detected as **induced in KT2440 on phenylalanine** [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) and mapped to the KT2440 chromosome as *hpd* [PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/). Note KEGG assigns *hpd* to bucket ppu00130 (ubiquinone/other), not ppu00350 — a database-boundary artifact, not biology. **High confidence.**

### 4.2 Entry-step candidates (transamination, step 1)

**tyrB = PP_1972 (Q88LG1) — aromatic-amino-acid aminotransferase, 398 aa, EC 2.6.1.- .**
Assigned the entry reaction (Tyr → 4-hydroxyphenylpyruvate) by analogy to *P. putida* U TyrB [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/). UniProt places it in the class-I PLP-dependent aminotransferase family, with Asp_trans (IPR000796) and class-I PLP site (IPR004838) domains, and annotates GO:0004838 "L-tyrosine:2-oxoglutarate transaminase activity." **Caveat:** its primary KEGG bucket is ppu00401 (aromatic amino-acid *biosynthesis*), and the annotation is rule-/homology-based, not a KT2440 enzyme assay.

**amaC = PP_3590 (Q88GX7) — aminotransferase, 398 aa, EC 2.6.1.- .**
An **equal-length paralog of tyrB** carrying **word-for-word identical** UniProt annotations: same class-I PLP family membership, identical InterPro set (IPR000796, IPR004838), and the identical GO:0004838 + GO:0030170 (PLP binding) + "L-phenylalanine biosynthesis from chorismate via phenylpyruvate" process term. This identity is the signature of **UniRule/rule-based propagation**, not two independent experimental characterizations. The two loci therefore represent **paralog redundancy**: the transamination activity is present, but neither locus is uniquely demonstrated as *the* physiological Tyr aminotransferase in KT2440.

**hisC = PP_0967 (Q88P86)** (histidinol-phosphate aminotransferase, EC 2.6.1.9) shares EC 2.6.1.- space but belongs to histidine biosynthesis; it is not a serious step-1 candidate.

### 4.3 Over-propagated / non-module candidates

| Locus | Annotation | Real pathway | Verdict |
|-------|-----------|--------------|---------|
| PP_1709 (Q88M65) | FAH-family protein, **236 aa**, no EC, no gene name | FAH superfamily, different substrate | **Not a second FAH**; too short vs 430-aa HmgB |
| PP_2552 (Q88JU5) | DOPA/aromatic-L-amino-acid decarboxylase, EC 4.1.1.28 | Tyr → tyramine decarboxylation branch | Different sub-map; **exclude** |
| davD = PP_0213 | Glutarate-semialdehyde DH, EC 1.2.1.- | Lysine/glutarate | Exclude |
| sad-I = PP_2488 | Succinate-semialdehyde DH, EC 1.2.1.24 | GABA/succinate | Exclude |
| gabD-II = PP_4422 | SSADH (NADP+), EC 1.2.1.79 | GABA | Exclude |
| frmA = PP_1616 | S-(hydroxymethyl)glutathione DH, EC 1.1.1.1/284 | C1/formaldehyde | Exclude |
| peaE = PP_3463 | Phenylacetaldehyde DH, EC 1.2.1.39 | Phenylethylamine (ppu00360/643) | Exclude |
| adhP = PP_3839 | Short-chain alcohol DH, EC 1.1.1.- | Generic redox | Exclude |
| PP_4983 (Q88D45) | Tryptophan 2-monooxygenase, EC 1.13.12.3 | Tryptophan | Exclude |

**PP_1709 in detail:** UniProt lists it as a "Fumarylacetoacetate hydrolase family protein," 236 aa, **no gene name and no EC number**. Genuine fumarylacetoacetase (HmgB/PP_4620) is 430 aa with EC 3.7.1.2. The ~200-aa truncation and absent EC strongly indicate PP_1709 is an FAH-*superfamily* member acting on a different substrate (e.g., an acylpyruvate- or oxaloacetate-type hydrolase), **not** a second physiological fumarylacetoacetase. It should not count toward step 5.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 The one real ambiguity — entry transamination

The transamination step is the sole point of genuine uncertainty. It is **not a gap** (activity is annotated on ≥2 loci with the correct GO term) but it is **candidate_uncertain**: aromatic aminotransferases are notoriously promiscuous and functionally redundant, and no KT2440-specific enzyme assay isolates a single physiological Tyr aminotransferase. In *P. putida* U the reaction is attributed to TyrB [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/); transfer to KT2440 is reasonable at the *family* level but weak at the *locus* level.

### 5.2 KEGG bucket mismatch (satisfiability-scoring hazard)

The true module genes are **not** all filed under ppu00350:
- *hpd* → ppu00130
- *hmgA/hmgB/hmgC* → ppu00643 (in the local metadata)
- *tyrB/amaC* → ppu00401

An automated check that counts only ppu00350-bucketed genes would **under-count** coverage and could falsely flag the module as a gap. The module is satisfied; the bucketing is a database-boundary artifact.

### 5.3 Over-annotation into ppu00350

Of the 16 candidates, only ~5–6 are mechanistically relevant (hpd, hmgA, hmgB, hmgC, and one of tyrB/amaC). The remaining ~10 loci — semialdehyde dehydrogenases, formaldehyde/alcohol dehydrogenases, a His aminotransferase, a Trp monooxygenase, and the DOPA decarboxylase — are **over-propagated** into the tyrosine-metabolism bucket by broad EC/GO mappings and should be excluded from module satisfiability.

### 5.4 Broad EC/GO mappings

- EC 2.6.1.- (unspecified aminotransferase) on tyrB, amaC, hisC is too broad to disambiguate function.
- The FAH-superfamily annotation on PP_1709 is a classic broad-family over-call.
- GST-zeta on hmgC and dioxygenase superfamilies on hpd/hmgA are specific enough here to be reliable.

---

## 6. Module and GO-Curation Recommendations

| Step | Recommended module status | Locus | Rationale |
|------|---------------------------|-------|-----------|
| 1. Transamination | **candidate_uncertain** | tyrB = PP_1972 (primary), amaC = PP_3590 (redundant) | Activity present via rule-based GO:0004838 on two paralogs; no locus-unique assay |
| 2. HPD | **covered** | hpd = PP_3433 | Direct KT2440 proteomics + genome mapping |
| 3. HGD | **covered** | hmgA = PP_4621 | Direct KT2440 proteomics; *P. putida* U biochem |
| 4. MAAI | **covered** | hmgC = PP_4619 | *P. putida* U biochem; operon cluster |
| 5. FAH | **covered** | hmgB = PP_4620 | *P. putida* U biochem; operon cluster |

**Additional recommendations:**

1. **Do not count PP_1709 toward step 5.** Reannotate as an FAH-superfamily hydrolase of unspecified substrate; flag as "likely over-propagated fumarylacetoacetase annotation."
2. **Remove the ~10 non-module candidates** (davD, sad-I, gabD-II, frmA, peaE, adhP, hisC, PP_4983, PP_2552) from module satisfiability scoring for the tyrosine→fumarate route. PP_2552 should instead anchor a *separate* Tyr-decarboxylation module.
3. **Module boundary is correct for this organism**; no `module_needs_revision`. But the **KEGG-bucket-based candidate harvesting is misleading** — recommend that satisfiability logic ignore the ppu00350 bucket label and instead match on EC / GO / ortholog identity, which correctly picks up hpd (ppu00130) and hmgABC (ppu00643).
4. **GO curation:** hmgA/hmgB/hmgC/hpd already carry appropriate GO MF terms. For step 1, retain GO:0004838 on tyrB and amaC but tag the evidence code as inferred from electronic/rule-based annotation (IEA/UniRule), not experimental.
5. **No new GO term requests appear necessary**; the reactions all have existing EC/GO coverage.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Gene | Locus | Why promote |
|------|-------|-------------|
| **tyrB** | PP_1972 | Resolve the entry-step ambiguity; determine whether it is the physiological Tyr aminotransferase vs amaC. Highest-value open question. |
| **amaC** | PP_3590 | Equal-length paralog with identical rule-based annotation; needs disambiguation from tyrB. |
| **PP_1709** | PP_1709 | Confirm it is NOT a fumarylacetoacetase; reclassify the 236-aa FAH-superfamily protein and prevent over-count of step 5. |
| **hmgB** | PP_4620 | Confirm EC 3.7.1.2 assignment and operon membership in KT2440 (currently transferred from *P. putida* U). |

hpd, hmgA, and hmgC are well-supported and are **lower priority** for full review, though confirming the KT2440 *hmgABC* operon structure directly (rather than by transfer from strain U) would close a minor gap.

---

## 8. Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the review |
|------|-----------------|----------|----------------------------|
| [15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/) | *The homogentisate pathway: a central catabolic pathway...in Pseudomonas putida* | *P. putida* U | Defines steps 3–5 (HmgA/HmgB/HmgC → fumarate + acetoacetate), the *hmgABC* operon, HmgR regulation, and the TyrB entry step. Strongest mechanistic anchor; transfer to KT2440 strong (near-identical strain). |
| [16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) | *Analysis of aromatic catabolic pathways in P. putida KT2440...proteomic approach* | **KT2440 (direct)** | Direct proteomic detection of **Hpd and HmgA induced on phenylalanine** — target-organism evidence for steps 2 and 3. |
| [12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/) | *Genomic analysis of the aromatic catabolic pathways from P. putida KT2440* | **KT2440 (direct)** | Whole-genome mapping placing the homogentisate pathway (**hmg/fah/mai**) plus **phh, hpd** on the KT2440 chromosome — confirms genomic presence of the module. |

**Verbatim supporting quotes:**

- [PMID: 15262943](https://pubmed.ncbi.nlm.nih.gov/15262943/): *"Homogentisate is then catabolized by a central catabolic pathway that involves three enzymes, homogentisate dioxygenase (HmgA), fumarylacetoacetate hydrolase (HmgB), and maleylacetoacetate isomerase (HmgC), finally yielding fumarate and acetoacetate."* — establishes enzymes and products of steps 3–5.
- [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/): *"Phenylalanine induced 4-hydroxyphenyl-pyruvate dioxygenase (Hpd) and homogentisate 1,2-dioxygenase (HmgA), key enzymes in the homogentisate degradation pathway."* — direct KT2440 expression evidence for Hpd (step 2) and HmgA (step 3).
- [PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/): *"the homogentisate pathway (hmg/fah/mai genes)"* and *"phenylalanine and tyrosine (phh, hpd)"* — confirms genomic presence and correct pathway attribution.

---

## 9. Limitations and Knowledge Gaps

1. **Locus-level transamination assignment is unresolved.** Family evidence is strong; the specific physiological gene (tyrB vs amaC vs both) is not experimentally pinned in KT2440.
2. **Steps 4–5 rest partly on transfer from *P. putida* U**, not direct KT2440 enzyme assays. Strain U and KT2440 are closely related, making transfer strong, but the KT2440 *hmgABC* operon structure and MAAI/FAH activities have not been individually re-characterized in KT2440 to the same depth.
3. **PP_1709's true substrate is unknown.** It is confidently *not* the physiological FAH, but its actual role is uncharacterized.
4. **No transcriptomic/mutant fitness data were analyzed here**; the review rests on genome, proteome, and biochemical literature plus UniProt structural/annotation evidence.
5. **Annotation-propagation risk:** the identical UniProt annotations on tyrB/amaC are a strength for "activity present" but a weakness for locus specificity — they reflect a rule, not two experiments.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Single and double knockouts of PP_1972 (tyrB) and PP_3590 (amaC)** in KT2440, followed by growth on L-tyrosine as sole carbon/nitrogen source, to test which paralog(s) support entry transamination and whether they are redundant.
2. **In vitro assay** of purified PP_1972 and PP_3590 for L-tyrosine:2-oxoglutarate transaminase activity (K_m/k_cat), to quantify physiological relevance.
3. **Biochemical characterization of PP_1709** across candidate FAH-superfamily substrates (acylpyruvates, oxaloacetate) to reclassify it and remove it from the FAH step.
4. **Direct verification of the KT2440 hmgABC operon** (RT-PCR/RNA-seq) and its induction by homogentisate, confirming HmgR-type regulation transferred from *P. putida* U.
5. **Curation actions:** update the module to mark steps 2–5 covered and step 1 candidate_uncertain; strip the ~10 over-propagated ppu00350 candidates from satisfiability scoring; add a note that satisfiability logic should match on EC/GO/ortholog identity rather than the ppu00350 KEGG bucket.

---

*Prepared for manual module satisfiability and gene-annotation curation. Evidence is explicitly labeled as direct-KT2440, transferred-from-*P. putida*-U, or rule-based homology throughout.*


## Artifacts

- [OpenScientist final report](PSEPK__tyrosine_catabolism__ppu00350-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__tyrosine_catabolism__ppu00350-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15262943
2. PMID:12534466
3. PMID:16470664