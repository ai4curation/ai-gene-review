---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T13:04:57.079839'
end_time: '2026-08-08T13:25:18.482603'
duration_seconds: 1221.4
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: hydroxycinnamate_vanillate_catabolism
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu00627
  pathway_id: ppu00627
  pathway_name: Aminobenzoate degradation
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00627 with 8 primary genes; module
    area: aromatic_and_xenobiotic_catabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '12'
  candidate_genes: '- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129)
    (EC 2.5.1.129; primary bucket kegg:ppu00627)

    - PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - galA: PP_2518 | Q88JX5 | Gallate dioxygenase (EC 1.13.11.57) (Gallate degradation
    protein A) (EC 1.13.11.57; primary bucket kegg:ppu00627)

    - PP_2805: PP_2805 | Q88J44 | Baeyer-Villiger monooxygenase (BVMO) (EC 1.14.13.-)
    (EC 1.14.13.-; primary bucket kegg:ppu00627)

    - PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)

    - paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17;
    primary bucket kegg:ppu00930)

    - fcs: PP_3356 | Q88HK0 | Feruloyl-CoA-synthetase (EC 6.2.1.34) (EC 6.2.1.34;
    primary bucket kegg:ppu00627)

    - vdh: PP_3357 | Q88HJ9 | Vanillin dehydrogenase (EC 1.2.1.67) (EC 1.2.1.67; primary
    bucket kegg:ppu00627)

    - PP_3358: PP_3358 | Q88HJ8 | Hydroxycinnamoyl-CoA hydratase-lyase (EC 4.1.2.41,
    EC 4.2.1.101) (EC 4.1.2.41; 4.2.1.101; primary bucket kegg:ppu00996)

    - PP_3657: PP_3657 | Q88GR1 | p-nitrobenzoate reductase NfnB (primary bucket kegg:ppu00627)

    - vanA: PP_3736 | Q88GI6 | Vanillate O-demethylase oxygenase subunit (EC 1.14.13.82)
    (EC 1.14.13.82; primary bucket kegg:ppu00627)

    - vanB: PP_3737 | Q88GI5 | Vanillate O-demethylase oxidoreductase (EC 1.14.13.-)
    (EC 1.14.13.-; primary bucket kegg:ppu00627)'
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__hydroxycinnamate-vanillate-catabolism__ppu00627-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__hydroxycinnamate-vanillate-catabolism__ppu00627-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

hydroxycinnamate_vanillate_catabolism in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00627
- Resolved ID: ppu00627
- Resolved name: Aminobenzoate degradation
- Source: KEGG

Resolved local bucket kegg:ppu00627 with 8 primary genes; module area: aromatic_and_xenobiotic_catabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 12

- ubiX: PP_0548 | Q88QE6 | Flavin prenyltransferase UbiX (EC 2.5.1.129) (EC 2.5.1.129; primary bucket kegg:ppu00627)
- PP_2217: PP_2217 | Q88KS2 | enoyl-CoA hydratase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- galA: PP_2518 | Q88JX5 | Gallate dioxygenase (EC 1.13.11.57) (Gallate degradation protein A) (EC 1.13.11.57; primary bucket kegg:ppu00627)
- PP_2805: PP_2805 | Q88J44 | Baeyer-Villiger monooxygenase (BVMO) (EC 1.14.13.-) (EC 1.14.13.-; primary bucket kegg:ppu00627)
- PP_2932: PP_2932 | Q88IR7 | Amidase family protein (primary bucket kegg:ppu00643)
- paaF: PP_3284 | Q88HR9 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) (EC 4.2.1.17; primary bucket kegg:ppu00930)
- fcs: PP_3356 | Q88HK0 | Feruloyl-CoA-synthetase (EC 6.2.1.34) (EC 6.2.1.34; primary bucket kegg:ppu00627)
- vdh: PP_3357 | Q88HJ9 | Vanillin dehydrogenase (EC 1.2.1.67) (EC 1.2.1.67; primary bucket kegg:ppu00627)
- PP_3358: PP_3358 | Q88HJ8 | Hydroxycinnamoyl-CoA hydratase-lyase (EC 4.1.2.41, EC 4.2.1.101) (EC 4.1.2.41; 4.2.1.101; primary bucket kegg:ppu00996)
- PP_3657: PP_3657 | Q88GR1 | p-nitrobenzoate reductase NfnB (primary bucket kegg:ppu00627)
- vanA: PP_3736 | Q88GI6 | Vanillate O-demethylase oxygenase subunit (EC 1.14.13.82) (EC 1.14.13.82; primary bucket kegg:ppu00627)
- vanB: PP_3737 | Q88GI5 | Vanillate O-demethylase oxidoreductase (EC 1.14.13.-) (EC 1.14.13.-; primary bucket kegg:ppu00627)

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

# Module/Pathway Review: Hydroxycinnamate & Vanillate Catabolism in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Nominal bucket:** KEGG `ppu00627` "Aminobenzoate degradation" (module area: aromatic and xenobiotic catabolism)
**Curation objective:** Species-aware satisfiability and gene-annotation review to support manual module curation.

---

## 1. Executive Summary

The hydroxycinnamate/vanillate catabolic module in *P. putida* KT2440 is **directly experimentally validated at its core**, and this review can assign high curator confidence to six of the twelve candidate genes. Ferulic acid (and related hydroxycinnamates) is degraded through a **CoA-dependent, non-β-oxidative route**: feruloyl-CoA synthetase **Fcs (PP_3356)** activates ferulate to feruloyl-CoA; the enoyl-CoA hydratase/aldolase **Ech (PP_3358)** hydrates and retro-aldol cleaves it to vanillin; and vanillin dehydrogenase **Vdh (PP_3357)** oxidizes vanillin to vanillate. Vanillate is then O-demethylated to protocatechuate by the two-component **vanillate O-demethylase VanAB (PP_3736/PP_3737)**, releasing formaldehyde. Protocatechuate is the convergence node feeding the separate **β-ketoadipate (protocatechuate branch)** pathway — which should be curated as a *neighboring* module, not part of this one. In parallel, **gallate** is cleaved by a dedicated ring-fission dioxygenase **GalA (PP_2518)** to 4-oxalomesaconate. All six assignments rest on **loss-of-function genetics and/or purified-enzyme biochemistry performed in the target strain or with target-strain proteins**.

The nominal KEGG bucket `ppu00627` ("Aminobenzoate degradation") is a **catch-all overview map**, and the review identifies **six candidate genes that are almost certainly over-propagated into it**: the flavin prenyltransferase **UbiX (PP_0548)**, a Baeyer-Villiger monooxygenase **PP_2805**, an amidase-family protein **PP_2932**, the nitroreductase **NfnB (PP_3657)**, and two generic enoyl-CoA hydratases **PP_2217** and **paaF (PP_3284)**. None of these is part of the phenylpropenoid/vanillate peripheral pathway as defined by the authoritative genome-wide catabolic survey of the strain, and none is induced by vanillin in proteomic studies. They should **not** be used to satisfy this module.

Two items require **module metadata revision rather than new biology**: (1) the **uptake step** is biologically present — KT2440 encodes dedicated aromatic-acid/H⁺ symporters for ferulate, 4-coumarate and vanillate, plus an OprD-family porin (OpdK) — but is missing from the candidate metadata; and (2) the **gallate-downstream steps (galBCD, 4-oxalomesaconate → pyruvate + oxaloacetate)** are biologically expected but not mapped in the candidate set. Both should be flagged `module_needs_revision`. Net recommendation: **6 covered core genes, 6 likely over-annotations to demote, and 2 metadata/mapping revisions.**

---

## 2. Target-Organism Pathway Definition

**What the module *is* in KT2440.** The biologically coherent process is the **peripheral (upper) catabolism of lignin-derived hydroxycinnamates and their aromatic aldehyde/acid intermediates to protocatechuate**, plus the **parallel gallate ring-cleavage branch**. Concretely it comprises:

1. **Uptake** of ferulate, 4-coumarate, and vanillate (aromatic acid/H⁺ symport + porin).
2. **CoA-dependent side-chain shortening** of hydroxycinnamates: ferulate → feruloyl-CoA → vanillin (+ acetyl-CoA) via Fcs and Ech.
3. **Aldehyde oxidation**: vanillin → vanillate via Vdh.
4. **O-demethylation**: vanillate → protocatechuate (+ formaldehyde) via VanAB.
5. **Gallate ring cleavage**: gallate → 4-oxalomesaconate via GalA (a mechanistically distinct entry that does *not* pass through protocatechuate).

**Boundaries — what to keep separate.** The candidate genes are nominally filed under KEGG `ppu00627` "Aminobenzoate degradation," but that map is a **broad overview/catch-all** that aggregates loosely related aromatic reactions. For curation, the following neighboring pathways must be kept as **distinct modules**:

- **β-ketoadipate pathway, protocatechuate branch** (PcaGH, PcaB, PcaC, PcaD, PcaIJ, PcaF): this is the *downstream* central pathway that consumes protocatechuate. Protocatechuate is the **exit node** of the present module and the **entry node** of β-ketoadipate; the two should link, not merge.
- **4-hydroxybenzoate (pob) and benzoate (ben) peripheral pathways**: converge on the same central funnel but have their own upper steps.
- **Gallate downstream utilization (galBCD / 4-oxalomesaconate hydrolase route)**: a distinct lower branch (see §5).

**Alternate names / database definitions.** Depending on the resource, relevant fragments appear as: KEGG "Aminobenzoate degradation" (`ppu00627`, the nominal bucket), the phenylpropenoid/**ferulate catabolic** cluster (`fcs`, `ech`, `vdh` — in some literature `ech` is annotated as `cal` or as "hydroxycinnamoyl-CoA hydratase-lyase," EC 4.2.1.101 / 4.1.2.41), the **vanillate demethylation** step (`vanAB`, EC 1.14.13.82), and the **gallate degradation** locus (`galA` + `galBCD`). The peripheral phenylpropenoid pathway was authoritatively delimited by the genome-wide survey as the gene set `fcs, ech, vdh, cal, van, acd, acs` ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)).

---

## 3. Expected Step Model

The table below is the curator's target model. "Status" reflects the review's satisfiability call.

| # | Expected step | Reaction (EC) | Gene(s) in KT2440 | Candidate present? | Status |
|---|---------------|---------------|-------------------|--------------------|--------|
| 0 | Aromatic acid uptake | ferulate/4-coumarate/vanillate H⁺-symport + porin | aromatic acid/H⁺ symporters; OpdK porin | **No (metadata gap)** | module_needs_revision |
| 1 | Ferulate activation | ferulate + CoA → feruloyl-CoA (6.2.1.34) | **fcs / PP_3356** | Yes | **covered** |
| 2 | Hydration + retro-aldol cleavage | feruloyl-CoA → vanillin + acetyl-CoA (4.2.1.101 / 4.1.2.41) | **ech / PP_3358** | Yes | **covered** |
| 3 | Vanillin oxidation | vanillin → vanillate (1.2.1.67) | **vdh / PP_3357** | Yes | **covered** |
| 4 | Vanillate O-demethylation | vanillate → protocatechuate + HCHO (1.14.13.82) | **vanA / PP_3736 + vanB / PP_3737** | Yes | **covered** |
| 5 | Gallate ring cleavage | gallate → 4-oxalomesaconate (1.13.11.57) | **galA / PP_2518** | Yes | **covered** |
| 6 | Gallate downstream | 4-oxalomesaconate → pyruvate + OAA | galBCD (not in candidate set) | **No (unmapped)** | module_needs_revision |
| — | Protocatechuate ring cleavage & β-ketoadipate | (1.13.11.3 …) | pcaGH…pcaF | (separate module) | not part of this module |

**Formaldehyde detoxification** (step 4 by-product) is handled by a coupled formaldehyde/formate detox route and can be noted as an ancillary requirement rather than a core module step.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence core genes (promote to "covered")

**Fcs — PP_3356 — feruloyl-CoA synthetase (EC 6.2.1.34).** Direct target-strain genetics: Ω-element insertional inactivation of *fcs* abolished growth on ferulic acid, and *E. coli* expressing *fcs*+*ech* converted ferulate to vanillin ([PMID: 12764569](https://pubmed.ncbi.nlm.nih.gov/12764569/)). The authors state that "the essential involvement of *fcs*, *ech* and *vdh* in the catabolism of ferulic acid in *P. putida* KT2440 was proven by separately inactivating each gene by insertion of Omega-elements." Metabolic-engineering work independently confirmed *fcs* as the ferulate-activating structural gene, describing "enhanced chromosomal expression of the structural genes for feruloyl-CoA synthetase (*fcs*) and enoyl-CoA hydratase/aldolase (*ech*)" ([PMID: 24136472](https://pubmed.ncbi.nlm.nih.gov/24136472/)). *Evidence type:* direct loss-of-function + heterologous reconstitution in the target strain. *Caveat:* none material; role is well established.

**Ech — PP_3358 — hydroxycinnamoyl-CoA hydratase/lyase (EC 4.2.1.101 / 4.1.2.41).** Same Ω-element study: inactivation abolished growth on ferulate ([PMID: 12764569](https://pubmed.ncbi.nlm.nih.gov/12764569/)); engineering work names it the enoyl-CoA hydratase/aldolase acting with Fcs ([PMID: 24136472](https://pubmed.ncbi.nlm.nih.gov/24136472/)). *Curation caveat:* the candidate metadata files PP_3358 under bucket `ppu00996` and labels it generically "Hydroxycinnamoyl-CoA hydratase-lyase" — the annotation is correct but the **bucket mapping is misplaced**; it belongs with fcs/vdh in this module. This is a metadata (not biological) discrepancy.

**Vdh — PP_3357 — vanillin dehydrogenase (EC 1.2.1.67).** Ω-element inactivation abolished growth on ferulate; Vdh activity was measured in extracts ([PMID: 12764569](https://pubmed.ncbi.nlm.nih.gov/12764569/)); *vdh* deletion blocks vanillin oxidation and causes vanillin accumulation — the basis of the vanillin-production strain ([PMID: 24136472](https://pubmed.ncbi.nlm.nih.gov/24136472/)). *Evidence type:* direct genetics + enzymology in the target strain.

**VanA — PP_3736 / VanB — PP_3737 — vanillate O-demethylase (EC 1.14.13.82 + reductase EC 1.14.13.-).** Recombinant *E. coli* expressing *P. putida* VanA+VanB efficiently converted vanillate to protocatechuate with formaldehyde release, which was detoxified to formate: "Recombinant *E. coli* strain K-12 cells expressing VanAB efficiently converted vanillate into protocatechuate" ([PMID: 16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/)). The genome survey maps the *van* cluster as the vanillate peripheral step feeding protocatechuate ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)). *Evidence type:* direct biochemistry with target-strain proteins. *Caveat:* VanA is the oxygenase (catalytic) subunit; VanB the oxidoreductase — both required; curate as a two-gene step.

**GalA — PP_2518 — gallate dioxygenase (EC 1.13.11.57).** Purified GalA is an Fe²⁺-dependent trimer (47.6 kDa subunits) acting specifically on gallate to give 4-oxalomesaconate (Km 144 µM; Vmax 53.2 µmol/min/mg); expression is gallate-induced; "a *P. putida* KT2440 *galA* mutant strain was unable to use gallate as the sole carbon source and it did not show gallate dioxygenase activity, suggesting that the GalA protein is the only dioxygenase involved in gallate cleavage" — establishing GalA as "a ring-cleavage dioxygenase that acts specifically on gallate to produce 4-oxalomesaconate" ([PMID: 16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/)). *Evidence type:* purified enzyme kinetics + loss-of-function genetics in the target strain. *Caveat:* this is a **parallel entry** (not through protocatechuate); its downstream steps (galBCD) are not in the candidate set.

### 4.2 Summary table of candidate assessment

| Gene / locus | Annotation | Evidence for role in this module | Call |
|---|---|---|---|
| **fcs / PP_3356** | Feruloyl-CoA synthetase (6.2.1.34) | Direct KT2440 genetics + reconstitution | **Covered (core)** |
| **ech / PP_3358** | Hydroxycinnamoyl-CoA hydratase-lyase (4.2.1.101/4.1.2.41) | Direct KT2440 genetics | **Covered (core); fix bucket** |
| **vdh / PP_3357** | Vanillin dehydrogenase (1.2.1.67) | Direct KT2440 genetics + enzymology | **Covered (core)** |
| **vanA / PP_3736** | Vanillate O-demethylase oxygenase (1.14.13.82) | Target-protein biochemistry | **Covered (core)** |
| **vanB / PP_3737** | Vanillate O-demethylase reductase | Component of VanAB | **Covered (core)** |
| **galA / PP_2518** | Gallate dioxygenase (1.13.11.57) | Purified enzyme + KT2440 mutant | **Covered (parallel branch)** |
| ubiX / PP_0548 | Flavin prenyltransferase (2.5.1.129) | Generic prenyl-FMN supplier (ubiquinone, UbiD-family) | **Over-annotation** |
| PP_2805 | Baeyer-Villiger monooxygenase (1.14.13.-) | Not induced by vanillin; no pathway link | **Over-annotation** |
| PP_2932 | Amidase family protein | Filed under ppu00643; no pathway link | **Over-annotation** |
| paaF / PP_3284 | Enoyl-CoA hydratase-isomerase (4.2.1.17) | Generic; primary bucket ppu00930 (phenylacetate) | **Over-annotation** |
| PP_2217 | Enoyl-CoA hydratase (4.2.1.17) | Generic; primary bucket ppu00930 | **Over-annotation** |
| PP_3657 | p-nitrobenzoate reductase NfnB | Nitroreductase; not vanillin-induced | **Over-annotation** |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 Likely over-propagated annotations (do NOT satisfy the module)

The genome-wide catabolic survey assigns the phenylpropenoid/vanillate peripheral pathway *specifically* to "the genes encoding the peripheral pathways for the catabolism of p-hydroxybenzoate (pob), benzoate (ben), quinate (qui), phenylpropenoid compounds (fcs, ech, vdh, cal, van, acd and acs)" and maps convergence at the protocatechuate branch of the β-ketoadipate pathway ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)). Proteomics shows "Protocatechuate 3,4-dioxygenase (PcaGH) was induced by p-hydroxybenzoate and vanilline" — i.e. vanillin catabolism converges on PcaGH and β-ketoadipate enzymes, **not** the nitroreductase/BVMO/amidase candidates ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)). On that basis:

- **UbiX (PP_0548)** is a flavin prenyltransferase that supplies **prenyl-FMN generically** (ubiquinone biosynthesis and as a cofactor-maturation partner for UbiD-family decarboxylases). It is not a dedicated ferulate/vanillate enzyme; its presence in `ppu00627` reflects EC-based over-mapping.
- **PP_2805 (Baeyer-Villiger monooxygenase, EC 1.14.13.-)**, **PP_2932 (amidase family; primary bucket ppu00643)**, and **PP_3657 (NfnB nitroreductase)** have no demonstrated role in hydroxycinnamate/vanillate catabolism and are not vanillin-induced. They are catch-all inclusions.
- **PP_2217** and **paaF (PP_3284)** are generic **enoyl-CoA hydratases (EC 4.2.1.17)** whose primary bucket is `ppu00930`; they belong to fatty-acid/phenylacetate β-oxidation contexts, not the retro-aldol Ech step of ferulate catabolism (which is a distinct EC 4.2.1.101/4.1.2.41 activity encoded by PP_3358).

**Curation action:** mark these six as *not part of module* (over-annotation); optionally record as `candidate_uncertain` only if a curator wishes to preserve a paper trail before demotion.

### 5.2 Genuine metadata gaps (biology present, mapping missing)

- **Transport (step 0).** KT2440 "can grow on lignin-related monomers, such as ferulate (FA), 4-coumarate (4CA), vanillate (VA), 4-hydroxybenzoate (4HBA), and protocatechuate (PCA)," and encodes **five aromatic-acid/proton symporters** with selectivity for these lignin monomers; protonophore inhibition confirmed proton-symport uptake ([PMID: 33549838](https://pubmed.ncbi.nlm.nih.gov/33549838/)). An OprD-family porin, **OpdK**, is required for vanillate growth — "an *opdK* mutant had a deficiency in the ability to grow on vanillate as a carbon source" (demonstrated in *P. aeruginosa*; strong transfer to *Pseudomonas* KT2440) ([PMID: 16352820](https://pubmed.ncbi.nlm.nih.gov/16352820/)). **PcaK** (MFS) is the 4-hydroxybenzoate/protocatechuate permease of the pca regulon ([PMID: 25582673](https://pubmed.ncbi.nlm.nih.gov/25582673/)). The uptake step is therefore **covered biologically but absent from candidate metadata** → `module_needs_revision`.

- **Gallate downstream (step 6).** GalA produces 4-oxalomesaconate ([PMID: 16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/)), but the enzymes converting 4-oxalomesaconate to pyruvate + oxaloacetate (the *galBCD*-type lower branch) are **not represented** in the candidate set. If the module is meant to reach central metabolism via the gallate branch, these steps must be added → `module_needs_revision`.

### 5.3 Boundary ambiguity

The nominal bucket name "Aminobenzoate degradation" is **misleading** for this organism: the biologically real process is hydroxycinnamate/vanillate/gallate catabolism converging on protocatechuate. The **protocatechuate ring-cleavage and β-ketoadipate steps are a separate downstream module** and should not be pulled into this one. This argues for authoring a KT2440-specific module document rather than relying on the generic KEGG overview map.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|---|---|---|
| Ferulate activation (Fcs) | **covered** | Direct KT2440 genetics ([PMID: 12764569](https://pubmed.ncbi.nlm.nih.gov/12764569/)) |
| Hydration/retro-aldol (Ech) | **covered** (fix bucket mapping from ppu00996) | Direct KT2440 genetics |
| Vanillin oxidation (Vdh) | **covered** | Direct KT2440 genetics + enzymology |
| Vanillate O-demethylation (VanAB) | **covered** (two-gene step) | Target-protein biochemistry ([PMID: 16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/)) |
| Gallate ring cleavage (GalA) | **covered** (parallel branch) | Purified enzyme + mutant ([PMID: 16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/)) |
| Aromatic acid uptake | **module_needs_revision** (add symporters + OpdK) | Present but unmapped ([PMID: 33549838](https://pubmed.ncbi.nlm.nih.gov/33549838/)) |
| Gallate downstream (galBCD) | **module_needs_revision** (add steps) | 4-oxalomesaconate fate unmapped |
| UbiX, PP_2805, PP_2932, NfnB, PP_2217, paaF | **not part of module** (over-annotation) | No pathway-specific evidence; catch-all bucket |
| Protocatechuate/β-ketoadipate | **separate module** | Downstream central pathway |

**Module boundary revision.** The generic KEGG `ppu00627` boundary is wrong for this organism (its "aminobenzoate" label does not describe the real substrates). **Recommend authoring a dedicated module document** — e.g., "hydroxycinnamate & vanillate catabolism to protocatechuate (KT2440)" — that (a) includes uptake, fcs/ech/vdh, vanAB; (b) branches gallate/galA→galBCD; and (c) links out to the β-ketoadipate module at the protocatechuate node.

**GO-term needs.** Core activities are already covered by existing GO/EC terms (feruloyl-CoA synthetase, vanillate O-demethylase, vanillin dehydrogenase, gallate dioxygenase). No new GO term is strictly required, but a **process term for "ferulate catabolic process via feruloyl-CoA"** and explicit annotation of the aromatic-acid/H⁺ symporters would improve module satisfiability tracking. No GO request is needed for the over-annotated genes — they should simply be excluded.

---

## 7. Genes to Promote to Full `fetch-gene` Review

Priority for full per-gene review (to lock annotations and finalize module coverage):

1. **PP_3358 (ech)** — high priority: correct role but **misfiled bucket** (`ppu00996`); confirm EC 4.2.1.101/4.1.2.41 and re-associate with the ferulate module.
2. **PP_3736 / PP_3737 (vanA/vanB)** — confirm two-component curation as a single functional step and formaldehyde-detox coupling.
3. **PP_2518 (galA)** — confirm parallel-branch placement and request mapping of the downstream galBCD steps.
4. **PP_0548 (ubiX)** — review to formally **demote** from this module (document its generic prenyl-FMN role to prevent re-propagation).
5. **PP_2217 and PP_3284 (paaF)** — review to confirm assignment to fatty-acid/phenylacetate β-oxidation and **demote** from this module.
6. **Aromatic-acid symporter loci** (from [PMID: 33549838](https://pubmed.ncbi.nlm.nih.gov/33549838/)) and **OpdK** — promote so the uptake step can be added with explicit gene IDs.

Genes **not** needing promotion (clear over-annotations, safe to exclude directly): PP_2805, PP_2932, PP_3657.

---

## 8. Mechanistic Model

```
   Lignin-derived monomers (extracellular)
        ferulate / 4-coumarate / vanillate
                     │
      [Step 0] aromatic-acid/H+ symporters + OpdK porin   (present; unmapped in metadata)
                     ▼
   ferulate ──Fcs(PP_3356, 6.2.1.34)──► feruloyl-CoA
                     │
        Ech(PP_3358, 4.2.1.101/4.1.2.41)  (+H2O, retro-aldol; releases acetyl-CoA)
                     ▼
                 vanillin
                     │
            Vdh(PP_3357, 1.2.1.67)  (aldehyde → acid)
                     ▼
                 vanillate
                     │
   VanAB(PP_3736/PP_3737, 1.14.13.82)  (O-demethylation; releases HCHO → HCOOH)
                     ▼
             PROTOCATECHUATE ───────────► β-ketoadipate pathway (SEPARATE module)
                     ▲
                     │  (convergence node — module exit)

   gallate ──GalA(PP_2518, 1.13.11.57)──► 4-oxalomesaconate ──(galBCD; unmapped)──► pyruvate + OAA
```

The narrative: KT2440 funnels multiple lignin-derived aromatics onto **protocatechuate** through a CoA-dependent, non-oxidative side-chain cleavage of hydroxycinnamates plus a demethylation step, while gallate enters through an independent ring-cleavage dioxygenase. Six candidate genes precisely encode the confirmed steps; the remaining six are artifacts of a broad KEGG overview map. The only real "missing" elements from the metadata are the transport step and the gallate lower branch — both known to exist in the strain.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports the review |
|---|---|---|
| [12764569](https://pubmed.ncbi.nlm.nih.gov/12764569/) | *Functional analyses of ferulic acid metabolism genes in P. putida KT2440* | Ω-element inactivation of fcs, ech, vdh each abolished growth on ferulate — **direct target-strain genetics** for core steps 1–3 |
| [24136472](https://pubmed.ncbi.nlm.nih.gov/24136472/) | *Engineering KT2440 for vanillin production from ferulic acid* | Confirms fcs/ech identities; vdh deletion blocks vanillin oxidation (defines Vdh) |
| [16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/) | *Coupling of vanillate-O-demethylase and formaldehyde detox* | Recombinant VanAB converts vanillate → protocatechuate + HCHO — **step 4 biochemistry** |
| [16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/) | *Gallate dioxygenase from KT2440* | Purified GalA kinetics + galA mutant — GalA is the **sole** gallate dioxygenase (step 5) |
| [12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/) | *Genomic analysis of aromatic catabolism in KT2440* | Authoritative gene-set definition (fcs, ech, vdh, van, …); **draws the pathway boundary** |
| [16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) | *Proteomic analysis of aromatic pathways in KT2440* | Vanillin induces PcaGH/PcaF/PcaD — confirms convergence on β-ketoadipate; excludes catch-all candidates |
| [33549838](https://pubmed.ncbi.nlm.nih.gov/33549838/) | *Aromatic acid/proton symporters in KT2440* | Dedicated symporters for FA/4CA/VA uptake — **covers step 0** |
| [16352820](https://pubmed.ncbi.nlm.nih.gov/16352820/) | *OprD-family porins in P. aeruginosa* | opdK mutant deficient in vanillate growth — porin uptake (Pseudomonas transfer) |
| [25582673](https://pubmed.ncbi.nlm.nih.gov/25582673/) | *Chemotaxis/transport/catabolism integration; PcaY* | PcaK permease and pca regulon context for protocatechuate branch |

**Direct vs inferred:** Steps 1–5 rest on **direct experiments in KT2440 or with KT2440 proteins** (highest confidence). The uptake step is direct for KT2440 symporters ([PMID: 33549838](https://pubmed.ncbi.nlm.nih.gov/33549838/)) and inferred-by-strong-transfer for the OpdK porin (demonstrated in *P. aeruginosa*). The over-annotation calls are inferred from the authoritative genomic/proteomic definition of the pathway ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/); [PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)) plus enzyme-family reasoning.

---

## 10. Limitations and Knowledge Gaps

- **Gallate lower branch unmapped.** GalA's product (4-oxalomesaconate) fate via galBCD-type enzymes was not located in the candidate set; the module cannot yet claim gallate → central metabolism completeness.
- **Transport gene IDs not enumerated here.** The symporter study establishes five aromatic-acid/H⁺ symporters biologically, but the specific PP_ locus tags need to be pinned during a full gene review before they can be added to the module.
- **OpdK transfer is cross-species.** The porin requirement for vanillate uptake was shown in *P. aeruginosa*; transfer to KT2440 is strong but not directly demonstrated.
- **Over-annotation calls are exclusionary inferences.** While well supported by the genome/proteome definition of the pathway, "not part of this module" is a negative claim; each demotion should be recorded with its rationale so the annotation is not silently re-propagated.
- **Regulation not reviewed in depth.** Inducer specificity (Fer/Van regulators) and cross-talk with the pca regulon were only touched on; relevant for satisfiability under specific growth conditions.

---

## 11. Proposed Follow-up Actions

1. **Author a KT2440-specific module document** for hydroxycinnamate/vanillate catabolism with steps 0–5 as defined here, branching gallate separately, and linking out to the β-ketoadipate module at protocatechuate.
2. **Reassign PP_3358 (ech)** from bucket `ppu00996` to this module; verify EC 4.2.1.101/4.1.2.41.
3. **Demote six over-annotations** (UbiX, PP_2805, PP_2932, NfnB, PP_2217, paaF) from `ppu00627` satisfiability with documented rationale.
4. **Add the uptake step**: run a full `fetch-gene` review on the aromatic-acid symporter loci from [PMID: 33549838](https://pubmed.ncbi.nlm.nih.gov/33549838/) and on OpdK; record explicit PP_ IDs.
5. **Map the gallate lower branch** (galBCD / 4-oxalomesaconate → pyruvate + OAA) and add those steps.
6. **Optional wet-lab confirmations** where curation confidence must be maximal: (a) direct KT2440 opdK-homolog vanillate-uptake assay; (b) transcriptomic confirmation that the six over-annotated genes are *not* induced on ferulate/vanillate.

---

### Bottom line for curators

Mark **fcs (PP_3356), ech (PP_3358), vdh (PP_3357), vanA (PP_3736), vanB (PP_3737), and galA (PP_2518)** as **covered** on direct target-strain evidence. Mark **uptake** and the **gallate downstream branch** as **module_needs_revision** (present but unmapped). Treat **UbiX (PP_0548), PP_2805, PP_2932, NfnB (PP_3657), PP_2217, and paaF (PP_3284)** as **likely over-annotations** from the catch-all KEGG "aminobenzoate degradation" bucket and exclude them from module satisfiability.


## Artifacts

- [OpenScientist final report](PSEPK__hydroxycinnamate-vanillate-catabolism__ppu00627-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__hydroxycinnamate-vanillate-catabolism__ppu00627-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12534466
2. PMID:12764569
3. PMID:24136472
4. PMID:16242864
5. PMID:16030014
6. PMID:16470664
7. PMID:33549838
8. PMID:16352820
9. PMID:25582673