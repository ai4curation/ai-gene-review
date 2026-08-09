---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T17:48:35.583266'
end_time: '2026-08-08T18:01:19.183257'
duration_seconds: 763.61
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Glucarate and galactarate catabolism to 2-oxoglutarate
  module_summary: A reusable three-stage aldarate catabolic route in which substrate-specific
    dehydratases convert D-glucarate or D-galactarate to the common intermediate 5-dehydro-4-deoxy-D-glucarate.
    A second dehydratase then forms 2,5-dioxopentanoate, which an aldehyde dehydrogenase-family
    enzyme oxidizes to 2-oxoglutarate. Organisms can encode either or both substrate-entry
    reactions.
  module_outline: "- Glucarate and galactarate catabolism to 2-oxoglutarate\n  - 1.\
    \ substrate-specific aldarate entry\n  - Aldarate dehydration to the common intermediate\n\
    \    - Alternative versions by substrate: Aldarate substrate-entry reactions\n\
    \      - D-glucarate entry\n        - GudD glucarate dehydratase activity (molecular\
    \ player: glucarate dehydratase subfamily; activity or role: glucarate dehydratase\
    \ activity)\n      - D-galactarate entry\n        - GarD galactarate dehydratase\
    \ activity (molecular player: galactarate dehydratase subfamily; activity or role:\
    \ galactarate dehydratase activity)\n  - 2. common-intermediate decarboxylation\
    \ and dehydration\n  - 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate\n   \
    \ - KDGDH activity (molecular player: 5-dehydro-4-deoxyglucarate dehydratase subfamily;\
    \ activity or role: 5-dehydro-4-deoxyglucarate dehydratase activity)\n  - 3. terminal\
    \ oxidation to central metabolism\n  - 2,5-dioxopentanoate to 2-oxoglutarate\n\
    \    - 2,5-dioxovalerate dehydrogenase activity (molecular player: alpha-ketoglutaric-semialdehyde\
    \ dehydrogenase subfamily; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+)\
    \ activity)"
  module_connections: '- D-glucarate entry precedes 5-dehydro-4-deoxyglucarate to
    2,5-dioxopentanoate

    - D-galactarate entry precedes 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate

    - 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate precedes 2,5-dioxopentanoate
    to 2-oxoglutarate'
  pathway_query: ppu00053
  pathway_id: ppu00053
  pathway_name: Ascorbate and aldarate metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00053 with 4 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '8'
  candidate_genes: '- udh: PP_1171 | Q88NN6 | Uronate dehydrogenase (EC 1.1.1.203)
    (D-galacturonate dehydrogenase) (D-glucuronate dehydrogenase) (Hexuronate dehydrogenase)
    (EC 1.1.1.203; primary bucket kegg:ppu00053)

    - PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22;
    primary bucket kegg:ppu00040)

    - PP_3599: PP_3599 | Q88GW8 | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41)
    (5-keto-4-deoxy-glucarate dehydratase) (KDGDH) (EC 4.2.1.41; primary bucket kegg:ppu00053)

    - garD: PP_3601 | Q88GW6 | Galactarate dehydratase (EC 4.2.1.42) (EC 4.2.1.42;
    primary bucket kegg:ppu00053)

    - PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC
    1.2.1.26; primary bucket kegg:ppu00040)

    - gudD: PP_4757 | Q88DR6 | Glucarate dehydratase (EC 4.2.1.40) (EC 4.2.1.40; primary
    bucket kegg:ppu00053)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
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
  path: PSEPK__glucarate_galactarate_catabolism__ppu00053-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__glucarate_galactarate_catabolism__ppu00053-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Glucarate and galactarate catabolism to 2-oxoglutarate in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00053
- Resolved ID: ppu00053
- Resolved name: Ascorbate and aldarate metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00053 with 4 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 8

- udh: PP_1171 | Q88NN6 | Uronate dehydrogenase (EC 1.1.1.203) (D-galacturonate dehydrogenase) (D-glucuronate dehydrogenase) (Hexuronate dehydrogenase) (EC 1.1.1.203; primary bucket kegg:ppu00053)
- PP_1256: PP_1256 | Q88NF5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- PP_2585: PP_2585 | Q88JR4 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- udg: PP_2926 | Q88IS3 | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) (EC 1.1.1.22; primary bucket kegg:ppu00040)
- PP_3599: PP_3599 | Q88GW8 | 5-dehydro-4-deoxyglucarate dehydratase (EC 4.2.1.41) (5-keto-4-deoxy-glucarate dehydratase) (KDGDH) (EC 4.2.1.41; primary bucket kegg:ppu00053)
- garD: PP_3601 | Q88GW6 | Galactarate dehydratase (EC 4.2.1.42) (EC 4.2.1.42; primary bucket kegg:ppu00053)
- PP_3602: PP_3602 | Q88GW5 | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) (EC 1.2.1.26; primary bucket kegg:ppu00040)
- gudD: PP_4757 | Q88DR6 | Glucarate dehydratase (EC 4.2.1.40) (EC 4.2.1.40; primary bucket kegg:ppu00053)

## Generic Module Context

### Working Scope

A reusable three-stage aldarate catabolic route in which substrate-specific dehydratases convert D-glucarate or D-galactarate to the common intermediate 5-dehydro-4-deoxy-D-glucarate. A second dehydratase then forms 2,5-dioxopentanoate, which an aldehyde dehydrogenase-family enzyme oxidizes to 2-oxoglutarate. Organisms can encode either or both substrate-entry reactions.

### Provisional Biological Outline

- Glucarate and galactarate catabolism to 2-oxoglutarate
  - 1. substrate-specific aldarate entry
  - Aldarate dehydration to the common intermediate
    - Alternative versions by substrate: Aldarate substrate-entry reactions
      - D-glucarate entry
        - GudD glucarate dehydratase activity (molecular player: glucarate dehydratase subfamily; activity or role: glucarate dehydratase activity)
      - D-galactarate entry
        - GarD galactarate dehydratase activity (molecular player: galactarate dehydratase subfamily; activity or role: galactarate dehydratase activity)
  - 2. common-intermediate decarboxylation and dehydration
  - 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate
    - KDGDH activity (molecular player: 5-dehydro-4-deoxyglucarate dehydratase subfamily; activity or role: 5-dehydro-4-deoxyglucarate dehydratase activity)
  - 3. terminal oxidation to central metabolism
  - 2,5-dioxopentanoate to 2-oxoglutarate
    - 2,5-dioxovalerate dehydrogenase activity (molecular player: alpha-ketoglutaric-semialdehyde dehydrogenase subfamily; activity or role: 2,5-dioxovalerate dehydrogenase (NADP+) activity)

### Known Relationships Among Steps

- D-glucarate entry precedes 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate
- D-galactarate entry precedes 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate
- 5-dehydro-4-deoxyglucarate to 2,5-dioxopentanoate precedes 2,5-dioxopentanoate to 2-oxoglutarate

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

# Module/Pathway Review: Glucarate and Galactarate Catabolism to 2-Oxoglutarate in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Bucket:** KEGG ppu00053 "Ascorbate and aldarate metabolism" (module area: other_kegg_pathway)
**Scope reviewed:** three-stage aldarate route: substrate-specific aldarate dehydration → common intermediate 5-dehydro-4-deoxy-D-glucarate → 2,5-dioxopentanoate → 2-oxoglutarate.

---

## 1. Executive summary

The module is **fully satisfiable** in *P. putida* KT2440, and the organism uses the **2-oxoglutarate–forming route** (not the *E. coli*-type aldolytic route to pyruvate + glycerate). All three generic steps are encoded:

- **Substrate entry (D-glucarate):** `gudD` / **PP_4757** (glucarate dehydratase, EC 4.2.1.40) — **covered**.
- **Substrate entry (D-galactarate):** `garD` / **PP_3601** (galactarate dehydratase, EC 4.2.1.42) — **covered**.
- **Common-intermediate dehydration:** **PP_3599** (5-dehydro-4-deoxyglucarate dehydratase / KDGDH, EC 4.2.1.41) — **covered** (Swiss-Prot reviewed).
- **Terminal oxidation to 2-oxoglutarate:** **PP_3602** (α-ketoglutarate-semialdehyde dehydrogenase / KGSADH, EC 1.2.1.26) — **covered** (operon-embedded; the correct one of three paralogs).

Two candidate genes are **not** part of this module: **PP_2926** (`udg`, UDP-glucose 6-dehydrogenase) is an anabolic nucleotide-sugar enzyme (mark **not_expected_in_target_taxon**), and **PP_1256** / **PP_2585** are EC 1.2.1.26 paralogs serving other pathways (hydroxyproline and polyamine catabolism). **PP_1171** (`udh`, uronate dehydrogenase) is a legitimate but *upstream* feeder (uronate → aldarate), not one of the three core steps. A genome-wide scan finds **no GarL aldolase** (EC 4.1.2.20), confirming the intermediate can only proceed to 2-oxoglutarate.

Confidence: **high** for satisfiability and gene assignments (direct genome context + Swiss-Prot + one direct KT2440 enzyme characterization). The main residual uncertainty is the *level* of direct wet-lab evidence for growth on glucarate/galactarate in KT2440 itself.

---

## 2. Target-organism pathway definition

**Included process (this module):** intracellular catabolism of the C6 aldaric acids **D-glucarate** and **D-galactarate** to the TCA-cycle intermediate **2-oxoglutarate (α-ketoglutarate)**, via:

1. D-glucarate → 5-dehydro-4-deoxy-D-glucarate (GudD, EC 4.2.1.40)
   and/or D-galactarate → 5-dehydro-4-deoxy-D-glucarate (GarD, EC 4.2.1.42);
2. 5-dehydro-4-deoxy-D-glucarate → 2,5-dioxopentanoate (= α-ketoglutarate semialdehyde) + H₂O (KDGDH, EC 4.2.1.41);
3. 2,5-dioxopentanoate + NAD(P)⁺ → 2-oxoglutarate (KGSADH, EC 1.2.1.26).

**Neighboring pathways/maps to keep separate:**

- **KEGG ppu00053 "Ascorbate and aldarate metabolism"** and **ppu00040 "Pentose and glucuronate interconversions"** are broad umbrella maps; both contain enzymes not in this module. The bucket resolution pulled in over-broad members (see §5). **ppu01100 "Metabolic pathways"** is an overview map — ignore for satisfiability.
- The ***E. coli* D-glucarate/D-galactarate → D-glycerate pathway** (operons `garD`–`garPLRK`–`gudPD`; regulator `sdaR`; enzymes GarL aldolase EC 4.1.2.20, GarR tartronate-semialdehyde reductase, GarK glycerate kinase) is a **distinct downstream branch** and must not be transferred to KT2440, which lacks GarL (PMID 10762278).
- **Hydroxyproline degradation** (trans-4-hydroxy-L-proline → α-ketoglutarate semialdehyde → 2-oxoglutarate) and **polyamine/amino-acid catabolism** are separate modules that *share the KGSADH enzyme family* — the source of paralog cross-mapping.

**Alternate names:** "aldarate/saccharate catabolism"; the terminal enzyme appears as "2,5-dioxovalerate dehydrogenase", "2,5-dioxopentanoate dehydrogenase", or "α-ketoglutaric-semialdehyde dehydrogenase (KGSADH)"; the intermediate "5-dehydro-4-deoxy-D-glucarate" = "5-keto-4-deoxy-D-glucarate"; "2,5-dioxopentanoate" = "2,5-dioxovalerate" = "α-ketoglutarate semialdehyde".

---

## 3. Expected step model (target-aware)

| # | Step | Reaction (EC) | KT2440 gene | Status |
|---|------|---------------|-------------|--------|
| 1a | D-glucarate entry | glucarate dehydratase (4.2.1.40) | `gudD` PP_4757 | **covered** |
| 1b | D-galactarate entry | galactarate dehydratase (4.2.1.42) | `garD` PP_3601 | **covered** |
| 2 | common intermediate → 2,5-dioxopentanoate | 5-dehydro-4-deoxyglucarate dehydratase (4.2.1.41) | PP_3599 | **covered** |
| 3 | terminal oxidation → 2-oxoglutarate | KGSADH / 2,5-dioxovalerate dehydrogenase (1.2.1.26) | PP_3602 | **covered** |
| (+) | upstream feed: uronate → aldarate | uronate dehydrogenase (1.1.1.203) | `udh` PP_1171 | present (out-of-module feeder) |
| (+) | transport | MFS glucarate/aldarate transporters | PP_3600, PP_4758 | present (accessory) |
| (+) | regulation | GntR-family regulators | PP_3603, PP_4759 | present (accessory) |

Both substrate-entry reactions are present, so the module's "either or both entry" option resolves to **both** in KT2440.

---

## 4. Candidate genes and evidence

**High-confidence, in-module:**

- **PP_4757 (`gudD`, glucarate dehydratase, EC 4.2.1.40, K01706).** Enolase-superfamily D-glucarate dehydratase subgroup. Forms its own genomic cluster with a dedicated MFS transporter (PP_4758), a GntR-family regulator (PP_4759), a Zn-alcohol dehydrogenase (PP_4760) and a HAD hydrolase (PP_4761) — a self-contained, independently inducible glucarate-utilization unit. Evidence: homology + strong genomic context. UniProt TrEMBL (unreviewed). *Caveat:* substrate specificity within the ENS D-glucarate-dehydratase subgroup can be promiscuous; direct assay not confirmed in KT2440.
- **PP_3601 (`garD`, galactarate dehydratase, EC 4.2.1.42, K01708).** Classic GarD; structurally a **distinct non-enolase fold** (PMID 31811683), the first enzyme of the galactarate branch. Operon-embedded (PP_3599–PP_3602). Evidence: homology + genomic context. TrEMBL.
- **PP_3599 (KDGDH, 5-dehydro-4-deoxyglucarate dehydratase, EC 4.2.1.41, K01707).** **Swiss-Prot reviewed**; UniProt pathway "D-glucarate degradation; 2,5-dioxopentanoate from D-glucarate: step 2/2". The committed common-intermediate step; catalyzes the decarboxylation/dehydration to α-ketoglutarate semialdehyde. Highest-confidence in-module gene.
- **PP_3602 (KGSADH, EC 1.2.1.26, K13877).** Terminal oxidation to 2-oxoglutarate. Assignment rests on **guilt-by-operon** (directly downstream of `garD`). TrEMBL. This is the correct paralog for the module (see §5).

**Present but out-of-module / accessory:**

- **PP_1171 (`udh`, uronate dehydrogenase, EC 1.1.1.203, K18981).** **Swiss-Prot reviewed**; oxidizes β-D-glucuronate → D-glucarate and β-D-galacturonate → D-galactarate. **Directly characterized in KT2440** (cloned and assayed; PMID 19060141) — the strongest experimental evidence in the candidate set. It *feeds* substrates into the module from hexuronate/pectin catabolism but is not one of the three core dehydration/oxidation steps. Keep it as an "entry expansion," not a core step.
- **PP_3600, PP_4758 (MFS transporters, K03535 glucarate transporter family)** and **PP_3603, PP_4759 (GntR-family regulators)** — accessory transport/regulation, not enzymatic steps.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Three EC 1.2.1.26 paralogs (PP_1256, PP_2585, PP_3602) — paralog ambiguity + over-propagation.** KEGG maps all three identically to ppu00040/ppu00053/ppu00470 by orthology (K13877). Genome context disambiguates them:
  - **PP_3602** → aldarate operon → **the module's terminal enzyme (covered)**.
  - **PP_1256** → embedded in the **trans-4-hydroxyproline degradation operon** (PP_1255 D-hydroxyproline dehydrogenase K21060; PP_1257 1-pyrroline-4-hydroxy-2-carboxylate deaminase K21062; PP_1258 4-hydroxyproline epimerase K12658). Its KGSADH activity serves **hydroxyproline** catabolism → reassign; **candidate_uncertain / off-module** for aldarate.
  - **PP_2585** → unrelated locus near 8-oxoguanine deaminase (PP_2584), putrescine–pyruvate transaminase (PP_2588) and γ-glutamylaminobutanal dehydrogenase (PP_2589) → **polyamine/amino-acid** catabolic context → **candidate_uncertain / off-module**.
  KGSADH is a **hub aldehyde dehydrogenase** reused by convergent α-ketoglutarate-semialdehyde–producing pathways; the KEGG multi-mapping is expected over-propagation. The three proteins are **divergent paralogs, not recent duplicates** (pairwise amino-acid identity ≈57–69%: PP_1256–PP_2585 57%, PP_1256–PP_3602 57%, PP_2585–PP_3602 69%), consistent with each being retained for a distinct physiological route — so functional identity cannot be assumed uniform and must be assigned by genomic context/experiment.
- **PP_2926 (`udg`, UDP-glucose 6-dehydrogenase, EC 1.1.1.22, K00012) — spurious module inclusion.** This is an **anabolic** enzyme (UDP-glucose → UDP-glucuronate, nucleotide-sugar biosynthesis), with no reaction on glucarate/galactarate/5-dehydro-4-deoxyglucarate/2,5-dioxopentanoate. Its appearance in the ppu00053 bucket is a KEGG umbrella-map artifact. **Mark not_expected_in_target_taxon** for this module.
- **No GarL aldolase (EC 4.1.2.20) in the genome.** Genome-wide KEGG link queries (K01630/K18929) return nothing → the *E. coli* branch to pyruvate + glycerate is **absent**; the 2-oxoglutarate route is the **sole** fate of 5-dehydro-4-deoxy-D-glucarate. This is a strong pathway-boundary constraint.
- **Cofactor specificity of KGSADH (NAD⁺ vs NADP⁺)** is not established for KT2440; the generic module notes "NADP⁺". Minor; would need enzyme assay.
- **Direct growth phenotype** (KT2440 on glucarate/galactarate as sole carbon source) is inferred from complete pathway + dedicated transporters/regulators, not cited here from a KT2440 growth study.

---

## 6. Module and GO-curation recommendations

**Step status calls:**

| Module step | Call | Gene(s) |
|-------------|------|---------|
| D-glucarate entry (GudD) | **covered** | PP_4757 |
| D-galactarate entry (GarD) | **covered** | PP_3601 |
| 5-dehydro-4-deoxyglucarate → 2,5-dioxopentanoate (KDGDH) | **covered** | PP_3599 |
| 2,5-dioxopentanoate → 2-oxoglutarate (KGSADH) | **covered** | PP_3602 |

**Candidate-list cleanup:**

- **Remove from module / not_expected_in_target_taxon:** PP_2926 (`udg`, anabolic).
- **Reassign off-module (candidate_uncertain for this module):** PP_1256 (→ hydroxyproline module), PP_2585 (→ polyamine/amino-acid catabolism).
- **Retain as out-of-module upstream feeder (annotate as entry expansion, not a core step):** PP_1171 (`udh`).
- **Add accessory context (optional):** transporters PP_3600/PP_4758; regulators PP_3603/PP_4759.

**Module-boundary note:** the generic module's "either or both substrate-entry" is correct and resolves to **both** for KT2440. No module_needs_revision on structure; however, the **bucket→candidate mapping** (kegg:ppu00053 / ppu00040) is too permissive and should be tightened to exclude anabolic K00012 and non-operonic K13877 paralogs. Consider a **separate module document for hydroxyproline→2-oxoglutarate** (which legitimately claims PP_1256 + the K21060/K21062/K12658 set) so the shared KGSADH family does not collide with the aldarate module. GO annotations: PP_3602 → GO:0047533 (2,5-dioxovalerate dehydrogenase) restricted to the aldarate context; avoid propagating the same GO term to PP_1256/PP_2585 without pathway-specific evidence.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_3602** (KGSADH) — highest priority; TrEMBL-only, assignment rests on operon context; confirm it (not PP_1256/PP_2585) is the aldarate terminal enzyme and its cofactor preference.
2. **PP_3601** (`garD`) and **PP_4757** (`gudD`) — TrEMBL; confirm substrate specificity (galactarate vs glucarate) and family placement.
3. **PP_1256** — promote in the context of the **hydroxyproline** module to formally reassign it away from aldarate.
4. **PP_1171** (`udh`) — already Swiss-Prot + direct KT2440 data; low priority, but tag explicitly as an out-of-module feeder.

---

## 8. Key references

- Yoon SH, *et al.* "Cloning and characterization of uronate dehydrogenases from two pseudomonads and *Agrobacterium tumefaciens* strain C58." *J Bacteriol* 2009. **PMID 19060141.** — Direct KT2440 evidence that `udh`/PP_1171 oxidizes uronates to aldarates.
- Rosas-Lemus M, *et al.* "Structure of galactarate dehydratase, a new fold in an enolase involved in bacterial fitness after antibiotic treatment." *J Biol Chem* 2020. **PMID 31811683.** — GarD as the galactarate-entry dehydratase; distinct fold.
- Monterrubio R, *et al.* "A common regulator for the operons encoding the enzymes involved in D-galactarate, D-glucarate, and D-glycerate utilization in *E. coli*." *J Bacteriol* 2000. **PMID 10762278.** — Defines the *E. coli* aldolytic branch (GarL/GarR/GarK; regulator `sdaR`) that KT2440 lacks.
- Bearne SL. "The interdigitating loop of the enolase superfamily…" 2017. **PMID 28179138.** — Enolase-superfamily subgroups relevant to GudD and "galactarate dehydratase 2".
- Database evidence: UniProt (Q88NN6/PP_1171 and Q88GW8/PP_3599 are Swiss-Prot reviewed) and KEGG genome context for *P. putida* KT2440 (ppu), used throughout for operon structure and paralog disambiguation.

---

### Evidence provenance summary

- **Direct for KT2440:** `udh`/PP_1171 enzyme characterization (PMID 19060141); genome organization/operon structure (KEGG ppu); Swiss-Prot curation of PP_3599 and PP_1171.
- **Homology/database inference:** functional identity of PP_4757, PP_3601, PP_3602 (TrEMBL + KO assignment + operon context); GudD/GarD family placement.
- **Cross-organism (transfer noted):** *E. coli* branch/regulator (PMID 10762278) — used only to *exclude* an alternative; GarD fold (PMID 31811683, structure from another organism) — strong for family identity, neutral for KT2440 specificity.


## Artifacts

- [OpenScientist final report](PSEPK__glucarate_galactarate_catabolism__ppu00053-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__glucarate_galactarate_catabolism__ppu00053-deep-research-openscientist_artifacts/final_report.pdf)