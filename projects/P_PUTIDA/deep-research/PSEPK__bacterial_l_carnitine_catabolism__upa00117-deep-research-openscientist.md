---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T05:25:28.512244'
end_time: '2026-08-13T06:22:50.273831'
duration_seconds: 3441.76
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial L-carnitine catabolism through 3-dehydrocarnitine
  module_summary: A bacterial L-carnitine utilization module in which imported L-carnitine
    is oxidized to 3-dehydrocarnitine, cleaved to a betainyl-CoA intermediate, and
    converted to glycine betaine. The oxygenolytic CntAB route, anaerobic Cai reduction,
    compatible-solute retention, and downstream glycine-betaine demethylation are
    outside this boundary.
  module_outline: "- Bacterial L-carnitine catabolism through 3-dehydrocarnitine\n\
    \  - 1. L-carnitine uptake\n  - L-carnitine uptake\n  - 2. L-carnitine oxidation\n\
    \  - L-carnitine to 3-dehydrocarnitine\n  - 3. 3-dehydrocarnitine cleavage\n \
    \ - 3-dehydrocarnitine cleavage\n  - 4. glycine-betaine formation\n  - Betainyl-CoA\
    \ conversion to glycine betaine"
  module_connections: '- L-carnitine uptake feeds into L-carnitine to 3-dehydrocarnitine

    - L-carnitine to 3-dehydrocarnitine feeds into 3-dehydrocarnitine cleavage

    - 3-dehydrocarnitine cleavage feeds into Betainyl-CoA conversion to glycine betaine'
  pathway_query: UPA00117
  pathway_id: UPA00117
  pathway_name: UniPathway UPA00117
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00117 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- lcdH: PP_0302 | Q88R32 | L-carnitine dehydrogenase (CDH) (L-CDH)
    (EC 1.1.1.108) (EC 1.1.1.108; primary bucket unipathway:UPA00117)'
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
  path: PSEPK__bacterial_l_carnitine_catabolism__upa00117-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_l_carnitine_catabolism__upa00117-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial L-carnitine catabolism through 3-dehydrocarnitine in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00117
- Resolved ID: UPA00117
- Resolved name: UniPathway UPA00117
- Source: UniPathway

Resolved local bucket unipathway:UPA00117 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- lcdH: PP_0302 | Q88R32 | L-carnitine dehydrogenase (CDH) (L-CDH) (EC 1.1.1.108) (EC 1.1.1.108; primary bucket unipathway:UPA00117)

## Generic Module Context

### Working Scope

A bacterial L-carnitine utilization module in which imported L-carnitine is oxidized to 3-dehydrocarnitine, cleaved to a betainyl-CoA intermediate, and converted to glycine betaine. The oxygenolytic CntAB route, anaerobic Cai reduction, compatible-solute retention, and downstream glycine-betaine demethylation are outside this boundary.

### Provisional Biological Outline

- Bacterial L-carnitine catabolism through 3-dehydrocarnitine
  - 1. L-carnitine uptake
  - L-carnitine uptake
  - 2. L-carnitine oxidation
  - L-carnitine to 3-dehydrocarnitine
  - 3. 3-dehydrocarnitine cleavage
  - 3-dehydrocarnitine cleavage
  - 4. glycine-betaine formation
  - Betainyl-CoA conversion to glycine betaine

### Known Relationships Among Steps

- L-carnitine uptake feeds into L-carnitine to 3-dehydrocarnitine
- L-carnitine to 3-dehydrocarnitine feeds into 3-dehydrocarnitine cleavage
- 3-dehydrocarnitine cleavage feeds into Betainyl-CoA conversion to glycine betaine

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

# Module/Pathway/Taxon Review: Bacterial L-Carnitine Catabolism through 3-Dehydrocarnitine in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** UniPathway UPA00117 (L-carnitine → 3-dehydrocarnitine → glycine betaine)
**Commissioned candidate genes:** 1 (lcdH / PP_0302 / Q88R32)

---

## 1. Executive Summary

The UPA00117 module — bacterial L-carnitine catabolism that oxidizes imported L-carnitine to 3-dehydrocarnitine, cleaves it to a betainyl-CoA intermediate, and converts that intermediate to glycine betaine — **is present and satisfiable in *Pseudomonas putida* KT2440**. All four defined module steps map to dedicated genes, and those genes sit within a single, contiguous, co-regulated genomic locus (approximately PP_0294–PP_0326). The pathway is therefore best described as *complete but under-represented in the commissioned metadata*, rather than gapped.

The most important curation-facing conclusion is that **the candidate gene list is incomplete, not incorrect**. The metadata lists only `lcdH`/PP_0302 (L-carnitine dehydrogenase, EC 1.1.1.108) as the single primary gene for UPA00117. In reality, KT2440 encodes dedicated genes for the other three steps in the same operonic region: PP_0303 ("Dehydrocarnitine cleavage enzyme", KEGG K27837, EC 2.3.1.317) for 3-dehydrocarnitine cleavage to betainyl-CoA; PP_0301 ("Betainyl-CoA thiolase/thioesterase", KEGG K27492, EC 3.1.2.33) for the final conversion to glycine betaine; and betaine/carnitine ABC-transporter components (cbcVWX / PP_0294–0296 and caiX / PP_0304) for uptake. These genes should be added to the module and promoted to full gene review. Notably, lcdH is the *only* protein in the KT2440 proteome carrying EC 1.1.1.108, so there is **no evidence of EC over-propagation** for the committed step.

The chief caveat is evidentiary. The KT2440 annotations rest predominantly on **computational reannotation and homology transfer** — chiefly orthology to the experimentally defined *Pseudomonas aeruginosa* PA14 carnitine-catabolism gene set ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)) — rather than KT2440-specific biochemistry. Direct enzymatic evidence for the committed EC 1.1.1.108 reaction exists *in the species but in a different strain* (*P. putida* IFP 206; [PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/)). Only PP_0301 reaches UniProt protein-level evidence (existence level 1); the others are at homology/predicted levels (3–4). A minor but genuine curation gap is that, despite dedicated KEGG orthologs existing for each step, **no assembled KEGG MODULE (M-number)** encapsulates this L-carnitine → glycine betaine route, which strengthens the case for authoring a new module document.

---

## 2. Target-Organism Pathway Definition

### 2.1 What is included in the module boundary

The module covers the aerobic, oxidative catabolism of L-carnitine to glycine betaine through a 3-dehydrocarnitine intermediate:

1. **L-carnitine uptake** — import of L-carnitine across the cell envelope.
2. **L-carnitine oxidation** — NAD⁺-dependent oxidation of L-carnitine to 3-dehydrocarnitine (EC 1.1.1.108).
3. **3-dehydrocarnitine cleavage** — CoA-dependent cleavage of 3-dehydrocarnitine to a betainyl-CoA intermediate (a 3-ketoacid CoA-transferase-type reaction; EC 2.3.1.317).
4. **Glycine-betaine formation** — conversion of betainyl-CoA to glycine betaine (thioesterase; EC 3.1.2.33).

The essential chemistry is captured directly by the *P. aeruginosa* work: "*carnitine is converted to 3-dehydrocarnitine (3-dhc) which is in turn metabolized to glycine betaine (GB), an intermediate metabolite in the catabolism of carnitine to glycine*" ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)). The KT2440 gene cluster reproduces exactly this chemistry.

### 2.2 What should be kept separate (neighboring pathways / overview maps)

The following are **outside** the UPA00117 boundary and must not be merged into module satisfiability, even though several of the responsible genes are physically co-clustered in KT2440:

- **Oxygenolytic CntAB route** — a Rieske-oxygenase carnitine monooxygenase system; a distinct catabolic entry, not the dehydrogenase route.
- **Anaerobic Cai reduction** — the *E. coli*-type CaiABCDT crotonobetaine/carnitine racemase-reductase system.
- **Compatible-solute retention** — non-catabolic osmotic accumulation of carnitine/glycine betaine.
- **Downstream glycine-betaine demethylation** — the glycine betaine → dimethylglycine → sarcosine → glycine route. In KT2440 these genes (**gbcAB / PP_0315–0316, dgcAB / PP_0310–0311, soxBDAG / PP_0323–0326**) are co-clustered with the carnitine genes but belong to a downstream module and should be scored separately.

### 2.3 Alternate names / database-specific definitions

- **UniPathway:** UPA00117 (target).
- **KEGG orthology (organism `ppu`):** K17735 (carnitine 3-dehydrogenase, EC 1.1.1.108), K27837 (3-dehydrocarnitine:acetyl-CoA trimethylamine transferase, EC 2.3.1.317), K27492 (betainyl-CoA thioesterase, EC 3.1.2.33). **No KEGG MODULE (M-number)** assembles these into a single route.
- **Enzyme naming:** "L-carnitine dehydrogenase" = "carnitine 3-dehydrogenase" = EC 1.1.1.108. "Dehydrocarnitine cleavage enzyme" corresponds to a 3-ketoacid CoA-transferase activity.

---

## 3. Expected Step Model

| # | Module step | KT2440 gene(s) | Locus tag(s) | EC / KEGG KO | Status |
|---|-------------|----------------|--------------|--------------|--------|
| 1 | L-carnitine uptake | cbcVWX + caiX | PP_0294–0296, PP_0304 | EC 7.6.2.9 / K02000 (ProV-like), K02002 (ProX-like) | **Covered** (transporter specificity uncertain) |
| 2 | L-carnitine → 3-dehydrocarnitine | **lcdH** | **PP_0302** | EC 1.1.1.108 / K17735 | **Covered** (committed candidate) |
| 3 | 3-dehydrocarnitine cleavage → betainyl-CoA | dehydrocarnitine cleavage enzyme | PP_0303 | EC 2.3.1.317 / K27837 | **Covered** (add to metadata) |
| 4 | Betainyl-CoA → glycine betaine | betainyl-CoA thioesterase | PP_0301 | EC 3.1.2.33 / K27492 | **Covered** (add to metadata; only protein-level evidence) |

Regulators within the locus: **gbdR** (PP_0298) and **cdhR** (PP_0305).

Step-linkage (as defined by the module and reproduced by the locus):

```
 L-carnitine (out)
      │  uptake: cbcVWX (PP_0294–0296) + caiX (PP_0304)
      ▼
 L-carnitine (in)
      │  oxidation: lcdH / PP_0302  (EC 1.1.1.108, K17735)  [committed candidate]
      ▼
 3-dehydrocarnitine
      │  cleavage: PP_0303  (EC 2.3.1.317, K27837)
      ▼
 betainyl-CoA
      │  thioesterase: PP_0301  (EC 3.1.2.33, K27492)  [protein-level evidence]
      ▼
 glycine betaine  ──►  (downstream demethylation module: gbcAB/dgcAB/soxBDAG — OUT OF SCOPE)
```

---

## 4. Candidate Genes and Evidence

### 4.1 lcdH / PP_0302 / Q88R32 — L-carnitine dehydrogenase (committed candidate; step 2)

- **Likely role:** NAD⁺-dependent oxidation of L-carnitine to 3-dehydrocarnitine (EC 1.1.1.108; KEGG K17735). This is the committed first catabolic step and is correctly listed in the metadata.
- **Evidence type:** UniProt existence level 3 (inferred from homology); annotation score 3/5. Assigned to the 3-hydroxyacyl-CoA dehydrogenase / L-carnitine dehydrogenase subfamily (Pfam PF00725 + PF02737). Species-level direct enzymology exists but in a *different* strain: carnitine dehydrogenase (EC 1.1.1.108) was purified and shown to catalyze L-carnitine → 3-dehydrocarnitine in *P. putida* IFP 206 — "*Carnitine dehydrogenase (carnitine:NAD+ oxidoreductase, EC 1.1.1.108) from Pseudomonas putida IFP 206 catalyzes the oxidation of L-carnitine to 3-dehydrocarnitine*" ([PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/)).
- **Over-propagation check (curation-relevant):** A UniProt proteome query returned lcdH/Q88R32 as the **only** protein carrying EC 1.1.1.108 in UP000000556. There is therefore no EC over-propagation for the committed step; the EC is uniquely and correctly assigned.
- **Caveat:** The parent family (3-hydroxyacyl-CoA dehydrogenase) is broad; homology-only assignment means substrate specificity for KT2440 has not been directly demonstrated. Recommend promotion to full review, but confidence in the assignment is high given the unique EC mapping and adjacent regulator (cdhR/PP_0305).

### 4.2 PP_0303 — Dehydrocarnitine cleavage enzyme (missing from metadata; step 3)

- **Likely role:** CoA-dependent cleavage of 3-dehydrocarnitine to betainyl-CoA (KEGG K27837, EC 2.3.1.317; 3-dehydrocarnitine:acetyl-CoA trimethylamine transferase). This corresponds to the *P. aeruginosa* "predicted 3-ketoacid CoA-transferase" activity: "*encodes the alpha and beta subunits of a predicted 3-ketoacid CoA-transferase, an enzymic activity hypothesized to be involved in the first step of deacetylation of 3-dhc*" ([PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)).
- **Evidence type:** UniProt existence level 4 (predicted); KEGG ortholog assigned. Direct-strain biochemistry absent.
- **Curation action:** Add to UPA00117 metadata; promote to full review.

### 4.3 PP_0301 — Betainyl-CoA thiolase/thioesterase (missing from metadata; step 4)

- **Likely role:** Conversion of betainyl-CoA to glycine betaine (KEGG K27492, EC 3.1.2.33; betainyl-CoA thioesterase). Completes the module.
- **Evidence type:** UniProt existence level **1 (evidence at protein level)** — the only step in the module with protein-level support (most plausibly proteomic detection rather than a dedicated enzymatic assay). Named "Betainyl-CoA thiolase" in UniProt; KEGG assigns thioesterase EC 3.1.2.33.
- **Curation action:** Add to UPA00117 metadata; promote to full review. Flag the thiolase-vs-thioesterase naming discrepancy for expert resolution.

### 4.4 Uptake components — cbcVWX (PP_0294–0296) + caiX (PP_0304) (missing from metadata; step 1)

- **Likely role:** ABC-transporter-mediated import. PP_0294 (cbcV) → K02000 (ProV-like ATP-binding, EC 7.6.2.9); PP_0304 (caiX) → K02002 (ProX-like substrate-binding periplasmic component). The system is annotated as a choline/betaine/carnitine ABC transporter.
- **Evidence type:** Homology (existence level 3–4). Maps to the **generic glycine betaine/proline ABC system**, so carnitine-specificity is not established from the annotation alone.
- **Curation action:** Add to the uptake step but score with uncertainty (broad transporter family; substrate specificity unverified in KT2440).

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

- **Metadata incompleteness (primary gap):** Only lcdH was committed; steps 1, 3, and 4 have dedicated KT2440 genes (PP_0294–0296, PP_0304, PP_0303, PP_0301) not captured in the metadata. This is the single most consequential curation issue — the module appears "1-gene" but is actually fully populated.
- **Transporter ambiguity:** The uptake genes map to the generic ProU-like (K02000/K02002) glycine betaine/proline system. Carnitine uptake specificity in KT2440 is inferred, not demonstrated. Score step 1 as **candidate_uncertain**.
- **Evidence provenance:** Cluster annotations reference only the two KT2440 genome papers — Nelson 2002 ([PMID: 12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/)) and the Belda 2016 "genome revisited" reannotation ([PMID: 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/)) — i.e., computational reannotation, not pathway-specific biochemistry. The functional gene set was defined in *P. aeruginosa* PA14 (carnitine dehydrogenase region PA5388–PA5384; 3-ketoacid CoA-transferase PA1999–PA2000; [PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/)). Species-to-strain transfer for lcdH is **strong** (same species, direct enzymology in IFP 206); genus-level transfer of the cleavage/thioesterase steps from *P. aeruginosa* is **moderate**.
- **No over-propagation of EC 1.1.1.108:** Confirmed — lcdH is the sole carrier in the proteome.
- **Naming inconsistency:** PP_0301 is "thiolase" in UniProt vs "thioesterase" (EC 3.1.2.33) in KEGG. Minor, but should be harmonized.
- **No KEGG MODULE:** Dedicated KOs exist (K17735, K27837, K27492) but no M-number assembles the route; a `find/module/carnitine` query returned nothing. This is a genuine reference-database gap, not a KT2440 gap.
- **Out-of-scope co-clustering risk:** The downstream demethylation genes (gbcAB, dgcAB, soxBDAG) are physically adjacent and could be erroneously pulled into UPA00117 satisfiability. Keep them in a separate module.

---

## 6. Module and GO-Curation Recommendations

Per-step module scoring:

| Module step | Recommended status | Rationale |
|-------------|-------------------|-----------|
| L-carnitine uptake | **candidate_uncertain** | cbcVWX/caiX present but generic betaine/proline ABC family; carnitine specificity unverified |
| L-carnitine → 3-dehydrocarnitine | **covered** | lcdH/PP_0302, unique EC 1.1.1.108, adjacent cdhR, species-level enzymology (IFP 206) |
| 3-dehydrocarnitine cleavage | **covered** | PP_0303, K27837/EC 2.3.1.317; homology to PA14 CoA-transferase (predicted evidence) |
| Betainyl-CoA → glycine betaine | **covered** | PP_0301, K27492/EC 3.1.2.33; protein-level evidence |

Overall module: **satisfiable / covered**, with the caveat that most support is homology-based and the metadata needs to be expanded.

Actions:
1. **Expand UPA00117 metadata** to include PP_0301, PP_0303, and the uptake components (PP_0294–0296, PP_0304) — do not leave it as a 1-gene bucket.
2. **Author a new module document** for the L-carnitine → 3-dehydrocarnitine → glycine betaine route, since no KEGG M-number exists. Explicitly bound it against the CntAB, Cai, compatible-solute, and glycine-betaine-demethylation neighbors.
3. **GO curation:** Verify GO terms exist for the cleavage (EC 2.3.1.317) and betainyl-CoA thioesterase (EC 3.1.2.33) activities; request new GO terms if the reactions are not represented. Ensure lcdH carries carnitine 3-dehydrogenase activity (EC 1.1.1.108).
4. **Correct module boundaries** so the co-clustered downstream demethylation genes are scored under a separate module, not UPA00117.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Gene | Locus | Priority | Reason |
|------|-------|----------|--------|
| lcdH | PP_0302 | High | Committed candidate; confirm substrate specificity and unique EC assignment |
| PP_0303 | PP_0303 | High | Step-3 cleavage enzyme; missing from metadata; predicted evidence only |
| PP_0301 | PP_0301 | High | Step-4 thioesterase; missing from metadata; protein-level evidence but naming conflict |
| caiX | PP_0304 | Medium | Uptake substrate-binding component; verify carnitine specificity |
| cbcVWX | PP_0294–0296 | Medium | Uptake ABC system; generic family, needs specificity check |
| cdhR / gbdR | PP_0305 / PP_0298 | Low–Medium | Regulators; useful for confirming co-regulation of the locus |

---

## 8. Mechanistic Model and Interpretation

The picture that emerges is coherent and internally consistent. KT2440 carries a **single contiguous operonic locus** (evidenced by consecutive GenBank protein IDs: PP_0300 AAN65931.1, PP_0301 AAN65932.1, PP_0302 AAN65933.1, PP_0303 AAN65934.1, PP_0304 AAN65935.2, PP_0305 AAN65936.1) that encodes, in order, the thioesterase (PP_0301), the dehydrogenase (PP_0302), the cleavage enzyme (PP_0303), an uptake component (caiX/PP_0304), and an adjacent regulator (cdhR/PP_0305). This physical clustering, together with two dedicated regulators (gbdR/PP_0298, cdhR/PP_0305), is exactly what is expected for a co-regulated catabolic module and strengthens confidence that the individually homology-assigned genes act together on the carnitine pathway.

Layered on top, KEGG assigns a precise, distinct KO/EC to every step — K17735/EC 1.1.1.108, K27837/EC 2.3.1.317, K27492/EC 3.1.2.33 — with no ambiguity or shared EC across the module, and lcdH is the unique EC 1.1.1.108 carrier in the proteome. The result is a module that is **structurally complete, orthology-anchored, and free of over-propagation** at the committed step. The residual uncertainty is almost entirely about *direct experimental confirmation in KT2440 specifically*: the enzymology is real but was done in *P. putida* IFP 206 and *P. aeruginosa* PA14, and the transporter's carnitine specificity is inferred from a generic betaine/proline family. These are the questions to resolve, not whether the pathway exists.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | Relevance |
|------|-----------------|-----------|
| [19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/) | *Identification of genes required for Pseudomonas aeruginosa carnitine catabolism* | Defines the pathway chemistry and the ortholog set (PA5388–PA5384; PA1999–PA2000) transferred to KT2440 |
| [3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/) | *Purification and properties of carnitine dehydrogenase from Pseudomonas putida* | Direct species-level (strain IFP 206) enzymology for EC 1.1.1.108, the lcdH step |
| [8645721](https://pubmed.ncbi.nlm.nih.gov/8645721/) | *Purification and properties of L(-)-carnitine dehydrogenase from Agrobacterium sp.* | Reference enzymology for EC 1.1.1.108 (L-carnitine → 3-dehydrocarnitine) in another taxon |
| [9003445](https://pubmed.ncbi.nlm.nih.gov/9003445/) | *Purification and characterization of D(+)-carnitine dehydrogenase from Agrobacterium sp.* | Stereochemical / substrate-specificity context for carnitine dehydrogenases |
| [12534463](https://pubmed.ncbi.nlm.nih.gov/12534463/) | KT2440 complete genome (Nelson 2002) | Primary source of KT2440 locus annotations |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | KT2440 genome revisited (Belda 2016) | Reannotation underpinning current gene assignments |

**Supporting quotes:**

- *"carnitine is converted to 3-dehydrocarnitine (3-dhc) which is in turn metabolized to glycine betaine (GB), an intermediate metabolite in the catabolism of carnitine to glycine"* — [PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/). Defines the exact module chemistry that the KT2440 cluster reproduces.
- *"encodes the alpha and beta subunits of a predicted 3-ketoacid CoA-transferase, an enzymic activity hypothesized to be involved in the first step of deacetylation of 3-dhc"* — [PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/). Supports assigning the KT2440 PP_0301/PP_0303 CoA-transferase/thiolase genes to the cleavage/betainyl-CoA step.
- *"Carnitine dehydrogenase (carnitine:NAD+ oxidoreductase, EC 1.1.1.108) from Pseudomonas putida IFP 206 catalyzes the oxidation of L-carnitine to 3-dehydrocarnitine"* — [PMID: 3058208](https://pubmed.ncbi.nlm.nih.gov/3058208/). Direct species-level (different strain) enzymatic evidence for the lcdH step.
- *"The PA5388-PA5384 region contains the predicted P. aeruginosa carnitine dehydrogenase homologue along with other genes required for growth on carnitine"* — [PMID: 19406895](https://pubmed.ncbi.nlm.nih.gov/19406895/). Source of the orthology-based transfer underpinning KT2440 cluster annotations.

---

## 10. Limitations and Knowledge Gaps

- **No KT2440-specific growth or biochemical data** were located; satisfiability rests on homology + reannotation + genomic context.
- **Transporter specificity** for L-carnitine (vs choline/betaine/proline) in KT2440 is unverified.
- **Cleavage and thioesterase steps** have no direct in-strain assays; PP_0301 has protein-level (likely proteomic) evidence only.
- **Species-to-strain transfer** of the lcdH enzymology (IFP 206 → KT2440) is strong but formally an inference; genus-level transfer of steps 3–4 (from *P. aeruginosa*) is moderate.
- **Reference-database gap:** absence of a KEGG MODULE means no external module-level consistency check is available.

---

## 11. Proposed Follow-up Experiments / Actions

1. **Growth phenotyping:** Test KT2440 growth on L-carnitine as sole carbon/nitrogen source; assay knockouts of lcdH (PP_0302), PP_0303, PP_0301, and caiX for loss of growth.
2. **In vitro enzymology:** Express and assay PP_0302 (NAD⁺-dependent L-carnitine oxidation), PP_0303 (3-dehydrocarnitine cleavage), and PP_0301 (betainyl-CoA thioesterase) to confirm EC assignments in KT2440.
3. **Transporter specificity:** Uptake assays (labeled L-carnitine) in cbcVWX/caiX mutants to establish carnitine-specific import.
4. **Metabolite tracing:** LC-MS detection of 3-dehydrocarnitine, betainyl-CoA, and glycine betaine intermediates during growth on carnitine.
5. **Curation actions:** Expand UPA00117 metadata (add PP_0301, PP_0303, PP_0294–0296, PP_0304); author a new module document; harmonize the PP_0301 thiolase/thioesterase naming; verify/request GO terms for EC 2.3.1.317 and EC 3.1.2.33.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_l_carnitine_catabolism__upa00117-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_l_carnitine_catabolism__upa00117-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19406895
2. PMID:3058208
3. PMID:12534463
4. PMID:26913973