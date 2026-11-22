---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T08:37:23.386714'
end_time: '2026-09-01T08:55:32.234710'
duration_seconds: 1088.85
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial FabA/FabB unsaturated-fatty-acid biosynthesis
  module_summary: A reusable oxygen-independent branch of bacterial type-II fatty-acid
    synthesis in which FabA dehydrates 3-hydroxydecanoyl-ACP and isomerizes the resulting
    trans-2-decenoyl-ACP to cis-3-decenoyl-ACP, FabB commits that intermediate to
    elongation, and FabF can extend palmitoleoyl-ACP toward cis-vaccenoyl-ACP. General
    FAS-II reduction and dehydration reactions are shared with saturated-fatty-acid
    synthesis and are outside this focused branch.
  module_outline: "- Bacterial FabA/FabB unsaturated-fatty-acid biosynthesis\n  -\
    \ 1. decanoyl-branch dehydration\n  - FabA 3-hydroxydecanoyl-ACP dehydration\n\
    \    - FabA 3-hydroxydecanoyl-ACP dehydratase (molecular player: FabA-family dehydratase/isomerases;\
    \ activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)\n\
    \  - 2. cis double-bond introduction\n  - FabA trans-2-decenoyl-ACP isomerization\n\
    \    - FabA trans-2-decenoyl-ACP isomerase (molecular player: FabA-family dehydratase/isomerases;\
    \ activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)\n\
    \  - 3. committed unsaturated-chain elongation\n  - FabB cis-3-decenoyl-ACP condensation\n\
    \    - FabB 3-oxoacyl-ACP synthase I (molecular player: FabB/KAS-I condensing\
    \ enzymes; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)\n\
    \  - 4. long-chain unsaturated-product extension\n  - FabF palmitoleoyl-ACP condensation\n\
    \    - FabF 3-oxoacyl-ACP synthase II (molecular player: FabF/KAS-II condensing\
    \ enzymes; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)"
  module_connections: '- FabA 3-hydroxydecanoyl-ACP dehydration feeds into FabA trans-2-decenoyl-ACP
    isomerization: The first FabA reaction supplies trans-2-decenoyl-ACP.

    - FabA trans-2-decenoyl-ACP isomerization feeds into FabB cis-3-decenoyl-ACP condensation:
    FabA supplies cis-3-decenoyl-ACP to FabB.

    - FabB cis-3-decenoyl-ACP condensation precedes FabF palmitoleoyl-ACP condensation'
  pathway_query: ppu01040
  pathway_id: ppu01040
  pathway_name: Biosynthesis of unsaturated fatty acids
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu01040 with 3 primary genes; module
    area: lipid_cell_envelope_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '3'
  candidate_genes: '- tesA: PP_2318 | Q88KH2 | Acyl-CoA thioesterase I/protease I/lysophospholipase
    L1 (EC 3.1.1.5, EC 3.1.2.14, EC 3.1.2.2) (EC 3.1.1.5; 3.1.2.14; 3.1.2.2; primary
    bucket kegg:ppu01040)

    - tesB: PP_4762 | Q88DR1 | Acyl-CoA thioesterase 2 (EC 3.1.2.20) (Thioesterase
    II) (EC 3.1.2.20; primary bucket kegg:ppu01040)

    - PP_5331: PP_5331 | Q88C52 | Long-chain acyl-CoA thioester hydrolase (primary
    bucket kegg:ppu01040)'
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
  path: PSEPK__bacterial_unsaturated_fatty_acid_biosynthesis__ppu01040-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_unsaturated_fatty_acid_biosynthesis__ppu01040-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial FabA/FabB unsaturated-fatty-acid biosynthesis in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu01040
- Resolved ID: ppu01040
- Resolved name: Biosynthesis of unsaturated fatty acids
- Source: KEGG

Resolved local bucket kegg:ppu01040 with 3 primary genes; module area: lipid_cell_envelope_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 3

- tesA: PP_2318 | Q88KH2 | Acyl-CoA thioesterase I/protease I/lysophospholipase L1 (EC 3.1.1.5, EC 3.1.2.14, EC 3.1.2.2) (EC 3.1.1.5; 3.1.2.14; 3.1.2.2; primary bucket kegg:ppu01040)
- tesB: PP_4762 | Q88DR1 | Acyl-CoA thioesterase 2 (EC 3.1.2.20) (Thioesterase II) (EC 3.1.2.20; primary bucket kegg:ppu01040)
- PP_5331: PP_5331 | Q88C52 | Long-chain acyl-CoA thioester hydrolase (primary bucket kegg:ppu01040)

## Generic Module Context

### Working Scope

A reusable oxygen-independent branch of bacterial type-II fatty-acid synthesis in which FabA dehydrates 3-hydroxydecanoyl-ACP and isomerizes the resulting trans-2-decenoyl-ACP to cis-3-decenoyl-ACP, FabB commits that intermediate to elongation, and FabF can extend palmitoleoyl-ACP toward cis-vaccenoyl-ACP. General FAS-II reduction and dehydration reactions are shared with saturated-fatty-acid synthesis and are outside this focused branch.

### Provisional Biological Outline

- Bacterial FabA/FabB unsaturated-fatty-acid biosynthesis
  - 1. decanoyl-branch dehydration
  - FabA 3-hydroxydecanoyl-ACP dehydration
    - FabA 3-hydroxydecanoyl-ACP dehydratase (molecular player: FabA-family dehydratase/isomerases; activity or role: (3R)-hydroxyacyl-acyl-carrier-protein dehydratase activity)
  - 2. cis double-bond introduction
  - FabA trans-2-decenoyl-ACP isomerization
    - FabA trans-2-decenoyl-ACP isomerase (molecular player: FabA-family dehydratase/isomerases; activity or role: trans-2-decenoyl-acyl-carrier-protein isomerase activity)
  - 3. committed unsaturated-chain elongation
  - FabB cis-3-decenoyl-ACP condensation
    - FabB 3-oxoacyl-ACP synthase I (molecular player: FabB/KAS-I condensing enzymes; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)
  - 4. long-chain unsaturated-product extension
  - FabF palmitoleoyl-ACP condensation
    - FabF 3-oxoacyl-ACP synthase II (molecular player: FabF/KAS-II condensing enzymes; activity or role: 3-oxoacyl-acyl-carrier-protein synthase activity)

### Known Relationships Among Steps

- FabA 3-hydroxydecanoyl-ACP dehydration feeds into FabA trans-2-decenoyl-ACP isomerization: The first FabA reaction supplies trans-2-decenoyl-ACP.
- FabA trans-2-decenoyl-ACP isomerization feeds into FabB cis-3-decenoyl-ACP condensation: FabA supplies cis-3-decenoyl-ACP to FabB.
- FabB cis-3-decenoyl-ACP condensation precedes FabF palmitoleoyl-ACP condensation

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

# Module/Pathway/Taxon Review: Bacterial FabA/FabB Unsaturated-Fatty-Acid Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK, NCBI:txid160488, proteome UP000000556)
**Target bucket:** KEGG `ppu01040` "Biosynthesis of unsaturated fatty acids"
**Module area:** lipid_cell_envelope_metabolism
**Date:** 2026-09-01

---

## 1. Executive summary

- The **FabA/FabB oxygen-independent unsaturated-fatty-acid (UFA) module is fully present and essential** in *P. putida* KT2440. All four expected steps are encoded — but by genes that are **absent from the candidate list**.
- The three candidate genes attached to bucket `kegg:ppu01040` (**tesA/PP_2318, tesB/PP_4762, PP_5331**) are **acyl-CoA thioesterases** (KO K10804/K10805/K10806). They cover **none** of the four FabA/FabB/FabF module steps and are a **mis-scoped / over-propagated** attachment. KEGG map01040 for bacteria displays only the thioesterase-mediated acyl-release reactions, so the bucket harvested the wrong genes.
- The true module genes live on KEGG map `ppu00061` (fatty acid biosynthesis):
  - **FabA = PP_4174** (Q88FC4; K01716; EC 4.2.1.59 dehydratase **+** EC 5.3.3.14 isomerase) → covers **steps 1 & 2** (bifunctional).
  - **FabB = PP_4175** (Q88FC3; K00647; EC 2.3.1.41) → covers **step 3**. `fabA`–`fabB` are adjacent and form an **operon**.
  - **FabF = PP_1916** (Q88LL4; K09458; EC 2.3.1.179) → covers **step 4**; paralog-ambiguous with **PP_3303**.
- **Direct target-species evidence** (Cronan lab, PMID 36537550): the *P. putida* `fabA fabB` operon is **essential** — its inactivation blocks growth unless exogenous UFA is supplied — and the aerobic **DesA** desaturase (KT2440 homolog **PP_0217**, Q88RB6) does **not** rescue UFA synthesis in *P. putida*. This distinguishes *P. putida* from *P. aeruginosa*.
- **Curation bottom line:** Module = **SATISFIED**, but the bucket **needs revision** — re-point it to PP_4174/PP_4175/PP_1916 and detach the three thioesterases.

---

## 2. Target-organism pathway definition

**Included process (this module):** the oxygen-independent branch of bacterial type-II fatty-acid synthesis (FAS-II) that introduces a *cis* double bond during de novo elongation. Specifically: FabA dehydrates (3R)-3-hydroxydecanoyl-ACP to *trans*-2-decenoyl-ACP and isomerizes it to *cis*-3-decenoyl-ACP; FabB commits *cis*-3-decenoyl-ACP to elongation; FabF elongates palmitoleoyl-ACP (16:1Δ9) toward *cis*-vaccenoyl-ACP (18:1Δ11). In *P. putida* the physiological end-products are the membrane-phospholipid acyl chains **16:1Δ9** and **18:1Δ11** (PMID 36537550).

**Neighboring processes to keep separate:**
- **KEGG map00061 "Fatty acid biosynthesis"** — the shared FAS-II initiation/reduction/dehydration machinery (AccABCD, FabD, FabG, FabZ, FabI/FabV, FabH). These reactions are shared with saturated-FA synthesis and are *outside* the focused UFA branch, even though FabA/FabB/FabF physically reside on this map.
- **KEGG map01040 "Biosynthesis of unsaturated fatty acids"** — as drawn for bacteria, this map is dominated by acyl-CoA **thioesterase** hydrolysis and (eukaryote-style) acyl-CoA elongation/desaturation; it is **not** the FabA/FabB module and is the source of the mis-scoped candidate genes.
- **Aerobic desaturation (DesA/DesB)** — an oxygen-*dependent* alternative route to UFAs; present as a homolog (PP_0217) but non-functional as a bypass in *P. putida*. Keep as a distinct module.
- **β-oxidation / acyl-CoA activation** (FadD PP_4549/PP_4550) and **cyclopropane-FA synthesis** — downstream/parallel, not part of this module.

**Alternate names / database definitions:** "anaerobic UFA pathway"; FabA = β-hydroxydecanoyl-ACP dehydratase/isomerase; FabB = KAS I; FabF = KAS II. Note the naming trap: KEGG map01040 ≠ the FabA/FabB module despite the identical English name.

---

## 3. Expected step model and satisfiability

| # | Module step | Enzyme (activity) | KT2440 gene | KO / EC | Call |
|---|---|---|---|---|---|
| 1 | 3-hydroxydecanoyl-ACP dehydration | FabA dehydratase | **PP_4174** (fabA) | K01716 / EC 4.2.1.59 | **covered** |
| 2 | *trans*-2→*cis*-3-decenoyl-ACP isomerization | FabA isomerase | **PP_4174** (fabA, same bifunctional enzyme) | K01716 / EC 5.3.3.14 | **covered** |
| 3 | *cis*-3-decenoyl-ACP committed condensation | FabB / KAS I | **PP_4175** (fabB) | K00647 / EC 2.3.1.41 | **covered** |
| 4 | palmitoleoyl-ACP → *cis*-vaccenoyl-ACP elongation | FabF / KAS II | **PP_1916** (fabF) | K09458 / EC 2.3.1.179 | **covered** (canonical fabD-fabG-acpP-fabF operon; paralog PP_3303 excluded) |

- **Steps encoded by candidate genes:** none. The candidate thioesterases map to no module step.
- **Steps present under a different name:** all four — via PP_4174 (fabA, steps 1+2), PP_4175 (fabB, step 3), PP_1916 (fabF, step 4), none of which is in the candidate list.
- **Steps not expected in this organism:** none are missing. FabF (step 4) is mechanistically an *accessory/elongation* step rather than a UFA-committing step, but it is encoded.

---

## 4. Candidate genes and evidence

| Gene | Locus | UniProt | KEGG KO | Actual function | Relation to module |
|---|---|---|---|---|---|
| tesA | PP_2318 | Q88KH2 (TrEMBL, PE4 predicted) | K10804 | Acyl-CoA thioesterase I / protease I / lysophospholipase L1 | **Not in module** — acyl release/editing; over-propagated |
| tesB | PP_4762 | Q88DR1 (TrEMBL, PE3) | K10805 | Acyl-CoA thioesterase II (EC 3.1.2.20) | **Not in module** — over-propagated |
| PP_5331 | PP_5331 | Q88C52 (TrEMBL, PE3) | K10806 | Long-chain acyl-CoA thioester hydrolase | **Not in module** — over-propagated |

**Module-relevant genes (not in candidate list, should be added):**

| Gene | Locus | UniProt | Evidence | Curation notes |
|---|---|---|---|---|
| **fabA** | PP_4174 | Q88FC4 (**Swiss-Prot**, PE3 inferred) | Function: **direct genetics** in *P. putida* (PMID 36537550); sequence: homology | Single K01716; bifunctional dehydratase+isomerase; operon with fabB. High confidence. |
| **fabB** | PP_4175 | Q88FC3 (TrEMBL, PE3) | Function: **direct genetics** (operon knockout, PMID 36537550); sequence: homology | Single K00647; essential; internal *fabB* promoter within *fabA* CDS. High confidence. |
| **fabF** | PP_1916 | Q88LL4 (TrEMBL, PE3) | Homology + gene neighborhood (adjacent to fabD PP_1913, fabG PP_1914) | K09458; canonical FabF in core FAS-II cluster. Confident but see paralog. |
| PP_3303 | PP_3303 | Q88HQ0 (TrEMBL, PE3) | Homology | Second K09458 KAS-II paralog; needs disambiguation vs PP_1916. |

**Evidence-type summary:** *Function* of FabA/FabB is supported by **direct experiments in the target species** (genetic operon dissection and essentiality, *P. putida* F1; transfer to KT2440 strong via syntenic PP_4174/PP_4175 operon). *Sequence-level* UniProt evidence for all module genes is homology-based (PE=3/4). The candidate thioesterases have only predicted/homology evidence and no experimental link to UFA synthesis.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **Bucket mis-scoping (highest priority):** `kegg:ppu01040` attached three thioesterases that satisfy no module step. This is a KEGG-map artifact (map01040 shows thioesterase hydrolysis for bacteria), not a biological gap.
2. **FabF paralog ambiguity — RESOLVED by gene neighborhood:** PP_1916 vs PP_3303, both K09458/EC 2.3.1.179. **PP_1916** is embedded in the canonical FAS-II core operon **fabD(PP_1913)–fabG(PP_1914)–acpP(PP_1915)–fabF(PP_1916)** (all same strand), identifying it as the physiological FabF. **PP_3303** sits between an RND efflux transporter (PP_3302) and a Bcr/CflA multidrug MFS transporter (PP_3304), with no FAS-II genes nearby — a divergent KAS-II paralog unlikely to serve core UFA elongation. Mark PP_1916 **covered (high confidence)**, PP_3303 `candidate_uncertain` (do not use to satisfy the module).
3. **FabH mislabel (over-annotation):** **PP_4379** (Q88ES4) is annotated "β-ketoacyl-ACP synthase I" in some sources but KEGG assigns **K00648 / EC 2.3.1.180 = FabH (KAS III, initiation)**. It is **not** a FabB/KAS-I and must **not** be used to satisfy the FabB step.
4. **Aerobic desaturase not a bypass:** DesA homolog **PP_0217** (Q88RB6) exists but, unlike in *P. aeruginosa* PAO1, does not supply sufficient UFA when FabA/FabB is inactivated (PMID 36537550). Keep as separate `not_expected_in_target_taxon` for *this* module (it belongs to the aerobic-desaturation module).
5. **Broad/multi-EC mappings:** tesA carries a broad multi-activity annotation (EC 3.1.1.5 / 3.1.2.2 / 3.1.2.14 / protease); such promiscuous entries are prone to over-propagation across lipid buckets.

---

## 6. Module and GO-curation recommendations

**Per-step status:**
- Step 1 (FabA dehydratase) → **covered** by PP_4174.
- Step 2 (FabA isomerase) → **covered** by PP_4174 (same bifunctional protein).
- Step 3 (FabB condensation) → **covered** by PP_4175.
- Step 4 (FabF elongation) → **covered (high confidence)** by PP_1916 (canonical fabD-fabG-acpP-fabF operon); paralog PP_3303 marked **candidate_uncertain** and excluded.

**Overall module:** **SATISFIED** but **`module_needs_revision`** for the bucket wiring:
- **Re-point** the FabA/FabB module to PP_4174, PP_4175, PP_1916 (source map ppu00061).
- **Detach** tesA/PP_2318, tesB/PP_4762, PP_5331 from the FabA/FabB module (they may remain in a distinct "acyl-thioesterase / fatty-acyl release" bucket, not a UFA-biosynthesis module).
- **Do not** count PP_4379 (FabH) or PP_0217 (DesA) toward this module.

**Module-boundary judgment:** the *generic* module boundaries are biochemically correct; the error is organism-specific bucket population from KEGG map01040. No change to the generic step model is required, but a curator note should warn that "KEGG map01040 members ≠ FabA/FabB module members" for bacteria.

**GO-term suitability (no new GO requests needed):**
- FabA/PP_4174: GO:0019171 (3-hydroxyacyl-ACP dehydratase) **and** GO:0034017 (trans-2-decenoyl-ACP isomerase) — annotate **both** to capture bifunctionality.
- FabB/PP_4175: GO:0004315 (3-oxoacyl-ACP synthase).
- FabF/PP_1916: GO:0033817 (β-ketoacyl-ACP synthase II) or GO:0004315.
- Parent process: GO:0006636 (unsaturated fatty acid biosynthetic process) for PP_4174/PP_4175.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4174 (fabA)** — primary module gene; add to bucket; annotate dual dehydratase+isomerase activity. *High priority.*
2. **PP_4175 (fabB)** — primary module gene; essential; add to bucket. *High priority.*
3. **PP_1916 (fabF)** — module step-4 gene; confirm as canonical FabF vs PP_3303. *High priority.*
4. **PP_3303** — resolve FabF paralog ambiguity. *Medium.*
5. **PP_4379** — correct FabH vs FabB mislabel. *Medium (annotation fix).*
6. **PP_0217 (desA)** — assign to the aerobic-desaturation module, not here. *Low/context.*
7. tesA/tesB/PP_5331 — reassign out of the UFA module. *Low (bucket cleanup).*

---

## 8. Key references

- Dong H, Wang M, Cronan JE. **Divergent unsaturated fatty acid synthesis in two highly related model pseudomonads.** *mBio / Mol Microbiol* 2023. **PMID 36537550.** — Direct *P. putida* evidence: fabA-fabB operon (internal fabB promoter), essentiality, DesA not a functional bypass; end-products 16:1Δ9 and 18:1Δ11.
- Zhu K, Zhang YM, Rock CO. **Transcriptional regulation of membrane lipid homeostasis in *Escherichia coli*.** 2009. **PMID 19854834.** — FabR control of fabA/fabB; defines FabA (β-hydroxydecanoyl-ACP dehydratase/isomerase) and FabB (KAS I) roles (broader-bacterial transfer).
- Marrakchi H, Choi KH, Rock CO. **A new mechanism for anaerobic unsaturated fatty acid formation in *Streptococcus pneumoniae*.** 2002. **PMID 12237320.** — Establishes the FabA/FabB anaerobic branch point and the FabM alternative (context for lineage variation).
- KEGG: pathways ppu01040, ppu00061; orthologies K01716, K00647, K09458, K00648, K10804–K10806 (rest.kegg.jp, accessed 2026-09-01).
- UniProt: Q88FC4 (fabA), Q88FC3 (fabB), Q88LL4 (fabF), Q88HQ0 (PP_3303), Q88ES4 (PP_4379/fabH), Q88RB6 (desA/PP_0217).

---

## 9. Evidence status and open questions

**Supported by direct experiments (target species):** FabA/FabB operon structure, essentiality, and the failure of DesA to bypass FabA/FabB loss — all from *P. putida* F1 (PMID 36537550). Transfer to KT2440 is **strong** (syntenic PP_4174–PP_4175 operon with 11-bp gap; near-isogenic strains).

**Inferred from homology / pathway DB / gene neighborhood:** the KO→step and EC assignments for PP_4174/PP_4175/PP_1916 (KEGG); the FabF assignment to PP_1916 (fabD-fabG-acpP-fabF operon context); the FabH re-identification of PP_4379 (KEGG K00648); the thioesterase identities of the candidate genes (KEGG K10804–K10806). UniProt sequence-level evidence for every module gene is PE=3/4 (no direct protein-level proof in KT2440 specifically).

**Open questions / experiments to resolve gaps:**
1. *KT2440-specific confirmation:* has the fabA-fabB knockout / UFA-auxotrophy phenotype been reproduced in KT2440 itself (vs F1)? A defined KT2440 ΔfabAB with UFA rescue would upgrade transfer from "strong inference" to "direct."
2. *FabF vs FabB division of labour:* does PP_1916 (FabF) elongate palmitoleoyl-ACP to *cis*-vaccenoyl-ACP and show the temperature-dependent 18:1Δ11 regulation seen in *E. coli*? Lipidomics across growth temperatures would confirm step 4.
3. *PP_3303 function:* what does the efflux-associated KAS-II paralog do? Its neighborhood suggests a role outside membrane-phospholipid UFA synthesis (e.g., specialized acyl chain modification) — a targeted deletion + lipidomics would clarify whether it ever contributes to the module.
4. *DesA (PP_0217) conditions:* are there conditions (e.g., specific carbon sources, stress) under which the KT2440 DesA becomes functionally relevant? Cronan 2023 showed it is non-functional as a bypass, but conditional relevance is untested.

## 10. Limitations

- No experimental data files were provided; all conclusions rest on public databases (KEGG, UniProt) and literature.
- The strongest functional evidence is from *P. putida* F1, not KT2440 directly (though loci are syntenic).
- No sequence alignment/BLAST was run in-session; paralog calls rest on KO identity plus gene neighborhood, which is strong but not a substitute for phylogenetic analysis.

### Confidence & species-transfer statement
FabA/FabB presence, essentiality, and operon structure are **directly demonstrated in *P. putida*** (F1; strong transfer to KT2440 via identical syntenic loci). Enzyme-to-step assignments rest on KEGG KO/EC plus gene neighborhood (strong for FabA/FabB, good-but-paralog-flagged for FabF). Sequence-level UniProt evidence is homology-based for all module members. The over-annotation and mis-scoping conclusions are supported directly by KEGG map membership.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_unsaturated_fatty_acid_biosynthesis__ppu01040-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_unsaturated_fatty_acid_biosynthesis__ppu01040-deep-research-openscientist_artifacts/final_report.pdf)