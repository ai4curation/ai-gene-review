---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:20:18.471551'
end_time: '2026-08-31T16:29:53.165646'
duration_seconds: 574.69
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial flagellar assembly and type III export
  module_summary: Reusable bacterial module spanning transcriptional staging, flagellar
    type III export, basal-body and switch construction, rod-hook assembly and length
    control, filament completion, and stator installation. Exact Pseudomonas putida
    representatives ground each architectural part without making the module specific
    to its large flagellar locus.
  module_outline: "- Bacterial flagellar assembly and export\n  - 1. late flagellar\
    \ transcription control\n  - FliA and FlgM transcriptional checkpoint\n    - FliA\
    \ sigma factor (molecular player: flagellar sigma factor FliA family)\n    - FlgM\
    \ anti-sigma factor (molecular player: flagellar anti-sigma factor FlgM family)\n\
    \  - 2. flagellar type III export\n  - Membrane export gate and cytosolic ATPase\n\
    \    - FlhA export-gate component (molecular player: FlhA family)\n    - FliP\
    \ export-gate component (molecular player: FliP family)\n    - FliI export ATPase\
    \ (molecular player: FliI flagellar export ATPase family)\n  - 3. basal-body MS\
    \ ring and switch assembly\n  - FliF MS ring and FliG switch\n    - FliF MS-ring\
    \ component (molecular player: FliF family)\n    - FliG switch component (molecular\
    \ player: FliG family)\n  - 4. rod-hook construction and length control\n  - Distal\
    \ rod, hook, and hook-length checkpoint\n    - FlgG distal rod (molecular player:\
    \ FlgG family)\n    - FlgE hook (molecular player: FlgE hook family)\n    - FliK\
    \ hook-length control (molecular player: FliK family)\n  - 5. filament junction,\
    \ polymerization, and capping\n  - Hook-filament junction, flagellin filament,\
    \ and cap\n    - FlgK hook-filament junction (molecular player: FlgK family)\n\
    \    - FliC flagellin (molecular player: bacterial flagellin family)\n    - FliD\
    \ filament cap (molecular player: FliD cap family)\n  - 6. stator installation\
    \ and torque generation\n  - MotAB stator complex\n    - MotA stator subunit (molecular\
    \ player: MotA family)\n    - MotB stator subunit (molecular player: MotB family)"
  module_connections: '- FliA and FlgM transcriptional checkpoint promotes Membrane
    export gate and cytosolic ATPase

    - Membrane export gate and cytosolic ATPase part of FliF MS ring and FliG switch

    - FliF MS ring and FliG switch precedes Distal rod, hook, and hook-length checkpoint

    - Distal rod, hook, and hook-length checkpoint precedes Hook-filament junction,
    flagellin filament, and cap

    - FliF MS ring and FliG switch precedes MotAB stator complex'
  pathway_query: ppu02040
  pathway_id: ppu02040
  pathway_name: Flagellar assembly
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu02040 with 47 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '47'
  candidate_genes: '- fliY: PP_0227 | Q88RA6 | Periplasmic cystine-binding protein
    (primary bucket kegg:ppu02040)

    - rpoD: PP_0387 | Q88QU7 | RNA polymerase sigma factor RpoD (Sigma-70) (primary
    bucket kegg:ppu02040)

    - rpoN: PP_0952 | P0A171 | RNA polymerase sigma-54 factor (primary bucket kegg:ppu02040)

    - PP_1087: PP_1087 | Q88NW6 | Outer membrane protein, OmpA family (primary bucket
    kegg:ppu02040)

    - PP_4335: PP_4335 | Q88EW7 | Flagellar motor protein (primary bucket kegg:ppu02040)

    - PP_4336: PP_4336 | Q88EW6 | Flagellar motor rotation protein (primary bucket
    kegg:ppu02040)

    - fliA: PP_4341 | Q88EW1 | RNA polymerase sigma factor FliA (RNA polymerase sigma
    factor for flagellar operon) (Sigma F) (Sigma-28) (primary bucket kegg:ppu02040)

    - flhA: PP_4344 | Q88EV8 | Flagellar biosynthesis protein FlhA (primary bucket
    kegg:ppu02040)

    - flhB: PP_4352 | Q88EV1 | Flagellar biosynthetic protein FlhB (primary bucket
    kegg:ppu02040)

    - fliR: PP_4353 | Q88EV0 | Flagellar biosynthetic protein FliR (primary bucket
    kegg:ppu02040)

    - fliQ: PP_4354 | Q88EU9 | Flagellar biosynthetic protein FliQ (primary bucket
    kegg:ppu02040)

    - fliP: PP_4355 | Q88EU8 | Flagellar biosynthetic protein FliP (primary bucket
    kegg:ppu02040)

    - fliO: PP_4356 | Q88EU7 | Flagellar protein (primary bucket kegg:ppu02040)

    - fliN: PP_4357 | Q88EU6 | Flagellar motor switch protein FliN (primary bucket
    kegg:ppu02040)

    - fliM: PP_4358 | Q88EU5 | Flagellar motor switch protein FliM (primary bucket
    kegg:ppu02040)

    - fliL: PP_4359 | Q88EU4 | Flagellar protein FliL (primary bucket kegg:ppu02040)

    - fliK: PP_4361 | Q88EU2 | Flagellar hook-length control protein FliK (primary
    bucket kegg:ppu02040)

    - fliJ: PP_4365 | Q88ET8 | Flagellar FliJ protein (primary bucket kegg:ppu02040)

    - fliI: PP_4366 | Q88ET7 | Flagellum-specific ATP synthase (EC 7.1.2.2) (EC 7.1.2.2;
    primary bucket kegg:ppu02040)

    - fliH: PP_4367 | Q88ET6 | Flagellar assembly protein FliH (primary bucket kegg:ppu02040)

    - fliG: PP_4368 | Q88ET5 | Flagellar motor switch protein FliG (primary bucket
    kegg:ppu02040)

    - fliF: PP_4369 | Q88ET4 | Flagellar M-ring protein (primary bucket kegg:ppu02040)

    - fliE: PP_4370 | Q88ET3 | Flagellar hook-basal body complex protein FliE (primary
    bucket kegg:ppu02040)

    - atoC: PP_4371 | Q88ET2 | Two component system AtoC DNA-binding transcriptional
    activator (primary bucket kegg:ppu02040)

    - fleQ: PP_4373 | Q88ET0 | Transcriptional regulator FleQ (primary bucket kegg:ppu02040)

    - fliT: PP_4374 | Q88ES9 | Flagellar protein FliT (primary bucket kegg:ppu02040)

    - fliS: PP_4375 | Q88ES8 | Flagellar secretion chaperone FliS (primary bucket
    kegg:ppu02040)

    - fliD: PP_4376 | Q88ES7 | Flagellar hook-associated protein 2 (HAP2) (Flagellar
    cap protein) (primary bucket kegg:ppu02040)

    - fliC: PP_4378 | Q88ES5 | Flagellin (primary bucket kegg:ppu02040)

    - flgL: PP_4380 | Q88ES3 | Flagellar hook-associated protein FlgL (primary bucket
    kegg:ppu02040)

    - flgK: PP_4381 | Q88ES2 | Flagellar hook-associated protein 1 (primary bucket
    kegg:ppu02040)

    - flgJ: PP_4382 | Q88ES1 | Peptidoglycan hydrolase FlgJ (Muramidase FlgJ) (primary
    bucket kegg:ppu02040)

    - flgI: PP_4383 | Q88ES0 | Flagellar P-ring protein (Basal body P-ring protein)
    (primary bucket kegg:ppu02040)

    - flgH: PP_4384 | Q88ER9 | Flagellar L-ring protein (Basal body L-ring protein)
    (primary bucket kegg:ppu02040)

    - flgG: PP_4385 | Q88ER8 | Flagellar basal-body rod protein FlgG (Distal rod protein)
    (primary bucket kegg:ppu02040)

    - flgF: PP_4386 | Q88ER7 | Flagellar basal-body rod protein FlgF (primary bucket
    kegg:ppu02040)

    - flgE: PP_4388 | Q88ER5 | Flagellar hook protein FlgE (primary bucket kegg:ppu02040)

    - flgD: PP_4389 | Q88ER4 | Basal-body rod modification protein FlgD (primary bucket
    kegg:ppu02040)

    - flgC: PP_4390 | Q88ER3 | Flagellar basal-body rod protein FlgC (primary bucket
    kegg:ppu02040)

    - flgB: PP_4391 | Q88ER2 | Flagellar basal body rod protein FlgB (primary bucket
    kegg:ppu02040)

    - flgA: PP_4394 | Q88EQ9 | Flagella basal body P-ring formation protein FlgA (primary
    bucket kegg:ppu02040)

    - flgM: PP_4395 | Q88EQ8 | Negative regulator of flagellin synthesis (Anti-sigma-28
    factor) (primary bucket kegg:ppu02040)

    - PP_4396: PP_4396 | Q88EQ7 | Flagellar biosynthesis protein FlgN (primary bucket
    kegg:ppu02040)

    - motB: PP_4904 | Q88DC3 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)

    - motA: PP_4905 | Q88DC2 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)

    - PP_5157: PP_5157 | Q88CM3 | Solute-binding protein family 3/N-terminal domain-containing
    protein (primary bucket kegg:ppu02040)

    - PP_5209: PP_5209 | Q88CH2 | Flagellar protein FliL (primary bucket kegg:ppu02040)'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_flagellar_assembly_export__ppu02040-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_flagellar_assembly_export__ppu02040-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial flagellar assembly and type III export in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu02040
- Resolved ID: ppu02040
- Resolved name: Flagellar assembly
- Source: KEGG

Resolved local bucket kegg:ppu02040 with 47 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 47

- fliY: PP_0227 | Q88RA6 | Periplasmic cystine-binding protein (primary bucket kegg:ppu02040)
- rpoD: PP_0387 | Q88QU7 | RNA polymerase sigma factor RpoD (Sigma-70) (primary bucket kegg:ppu02040)
- rpoN: PP_0952 | P0A171 | RNA polymerase sigma-54 factor (primary bucket kegg:ppu02040)
- PP_1087: PP_1087 | Q88NW6 | Outer membrane protein, OmpA family (primary bucket kegg:ppu02040)
- PP_4335: PP_4335 | Q88EW7 | Flagellar motor protein (primary bucket kegg:ppu02040)
- PP_4336: PP_4336 | Q88EW6 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)
- fliA: PP_4341 | Q88EW1 | RNA polymerase sigma factor FliA (RNA polymerase sigma factor for flagellar operon) (Sigma F) (Sigma-28) (primary bucket kegg:ppu02040)
- flhA: PP_4344 | Q88EV8 | Flagellar biosynthesis protein FlhA (primary bucket kegg:ppu02040)
- flhB: PP_4352 | Q88EV1 | Flagellar biosynthetic protein FlhB (primary bucket kegg:ppu02040)
- fliR: PP_4353 | Q88EV0 | Flagellar biosynthetic protein FliR (primary bucket kegg:ppu02040)
- fliQ: PP_4354 | Q88EU9 | Flagellar biosynthetic protein FliQ (primary bucket kegg:ppu02040)
- fliP: PP_4355 | Q88EU8 | Flagellar biosynthetic protein FliP (primary bucket kegg:ppu02040)
- fliO: PP_4356 | Q88EU7 | Flagellar protein (primary bucket kegg:ppu02040)
- fliN: PP_4357 | Q88EU6 | Flagellar motor switch protein FliN (primary bucket kegg:ppu02040)
- fliM: PP_4358 | Q88EU5 | Flagellar motor switch protein FliM (primary bucket kegg:ppu02040)
- fliL: PP_4359 | Q88EU4 | Flagellar protein FliL (primary bucket kegg:ppu02040)
- fliK: PP_4361 | Q88EU2 | Flagellar hook-length control protein FliK (primary bucket kegg:ppu02040)
- fliJ: PP_4365 | Q88ET8 | Flagellar FliJ protein (primary bucket kegg:ppu02040)
- fliI: PP_4366 | Q88ET7 | Flagellum-specific ATP synthase (EC 7.1.2.2) (EC 7.1.2.2; primary bucket kegg:ppu02040)
- fliH: PP_4367 | Q88ET6 | Flagellar assembly protein FliH (primary bucket kegg:ppu02040)
- fliG: PP_4368 | Q88ET5 | Flagellar motor switch protein FliG (primary bucket kegg:ppu02040)
- fliF: PP_4369 | Q88ET4 | Flagellar M-ring protein (primary bucket kegg:ppu02040)
- fliE: PP_4370 | Q88ET3 | Flagellar hook-basal body complex protein FliE (primary bucket kegg:ppu02040)
- atoC: PP_4371 | Q88ET2 | Two component system AtoC DNA-binding transcriptional activator (primary bucket kegg:ppu02040)
- fleQ: PP_4373 | Q88ET0 | Transcriptional regulator FleQ (primary bucket kegg:ppu02040)
- fliT: PP_4374 | Q88ES9 | Flagellar protein FliT (primary bucket kegg:ppu02040)
- fliS: PP_4375 | Q88ES8 | Flagellar secretion chaperone FliS (primary bucket kegg:ppu02040)
- fliD: PP_4376 | Q88ES7 | Flagellar hook-associated protein 2 (HAP2) (Flagellar cap protein) (primary bucket kegg:ppu02040)
- fliC: PP_4378 | Q88ES5 | Flagellin (primary bucket kegg:ppu02040)
- flgL: PP_4380 | Q88ES3 | Flagellar hook-associated protein FlgL (primary bucket kegg:ppu02040)
- flgK: PP_4381 | Q88ES2 | Flagellar hook-associated protein 1 (primary bucket kegg:ppu02040)
- flgJ: PP_4382 | Q88ES1 | Peptidoglycan hydrolase FlgJ (Muramidase FlgJ) (primary bucket kegg:ppu02040)
- flgI: PP_4383 | Q88ES0 | Flagellar P-ring protein (Basal body P-ring protein) (primary bucket kegg:ppu02040)
- flgH: PP_4384 | Q88ER9 | Flagellar L-ring protein (Basal body L-ring protein) (primary bucket kegg:ppu02040)
- flgG: PP_4385 | Q88ER8 | Flagellar basal-body rod protein FlgG (Distal rod protein) (primary bucket kegg:ppu02040)
- flgF: PP_4386 | Q88ER7 | Flagellar basal-body rod protein FlgF (primary bucket kegg:ppu02040)
- flgE: PP_4388 | Q88ER5 | Flagellar hook protein FlgE (primary bucket kegg:ppu02040)
- flgD: PP_4389 | Q88ER4 | Basal-body rod modification protein FlgD (primary bucket kegg:ppu02040)
- flgC: PP_4390 | Q88ER3 | Flagellar basal-body rod protein FlgC (primary bucket kegg:ppu02040)
- flgB: PP_4391 | Q88ER2 | Flagellar basal body rod protein FlgB (primary bucket kegg:ppu02040)
- flgA: PP_4394 | Q88EQ9 | Flagella basal body P-ring formation protein FlgA (primary bucket kegg:ppu02040)
- flgM: PP_4395 | Q88EQ8 | Negative regulator of flagellin synthesis (Anti-sigma-28 factor) (primary bucket kegg:ppu02040)
- PP_4396: PP_4396 | Q88EQ7 | Flagellar biosynthesis protein FlgN (primary bucket kegg:ppu02040)
- motB: PP_4904 | Q88DC3 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)
- motA: PP_4905 | Q88DC2 | Flagellar motor rotation protein (primary bucket kegg:ppu02040)
- PP_5157: PP_5157 | Q88CM3 | Solute-binding protein family 3/N-terminal domain-containing protein (primary bucket kegg:ppu02040)
- PP_5209: PP_5209 | Q88CH2 | Flagellar protein FliL (primary bucket kegg:ppu02040)

## Generic Module Context

### Working Scope

Reusable bacterial module spanning transcriptional staging, flagellar type III export, basal-body and switch construction, rod-hook assembly and length control, filament completion, and stator installation. Exact Pseudomonas putida representatives ground each architectural part without making the module specific to its large flagellar locus.

### Provisional Biological Outline

- Bacterial flagellar assembly and export
  - 1. late flagellar transcription control
  - FliA and FlgM transcriptional checkpoint
    - FliA sigma factor (molecular player: flagellar sigma factor FliA family)
    - FlgM anti-sigma factor (molecular player: flagellar anti-sigma factor FlgM family)
  - 2. flagellar type III export
  - Membrane export gate and cytosolic ATPase
    - FlhA export-gate component (molecular player: FlhA family)
    - FliP export-gate component (molecular player: FliP family)
    - FliI export ATPase (molecular player: FliI flagellar export ATPase family)
  - 3. basal-body MS ring and switch assembly
  - FliF MS ring and FliG switch
    - FliF MS-ring component (molecular player: FliF family)
    - FliG switch component (molecular player: FliG family)
  - 4. rod-hook construction and length control
  - Distal rod, hook, and hook-length checkpoint
    - FlgG distal rod (molecular player: FlgG family)
    - FlgE hook (molecular player: FlgE hook family)
    - FliK hook-length control (molecular player: FliK family)
  - 5. filament junction, polymerization, and capping
  - Hook-filament junction, flagellin filament, and cap
    - FlgK hook-filament junction (molecular player: FlgK family)
    - FliC flagellin (molecular player: bacterial flagellin family)
    - FliD filament cap (molecular player: FliD cap family)
  - 6. stator installation and torque generation
  - MotAB stator complex
    - MotA stator subunit (molecular player: MotA family)
    - MotB stator subunit (molecular player: MotB family)

### Known Relationships Among Steps

- FliA and FlgM transcriptional checkpoint promotes Membrane export gate and cytosolic ATPase
- Membrane export gate and cytosolic ATPase part of FliF MS ring and FliG switch
- FliF MS ring and FliG switch precedes Distal rod, hook, and hook-length checkpoint
- Distal rod, hook, and hook-length checkpoint precedes Hook-filament junction, flagellin filament, and cap
- FliF MS ring and FliG switch precedes MotAB stator complex

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

# Module/Pathway Review — Flagellar assembly & type III export in *Pseudomonas putida* KT2440 (KEGG ppu02040)

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Bucket:** kegg:ppu02040 "Flagellar assembly" — 47 primary candidate genes
**Module area:** transport_motility_signaling
**Prepared for:** manual module-satisfiability and gene-annotation curation

---

## 1. Executive summary

The KEGG ppu02040 flagellar-assembly module is **fully satisfiable** in *P. putida* KT2440. All six generic module steps — (1) late transcription control, (2) flagellar type III export, (3) MS-ring/switch, (4) rod–hook + length control, (5) filament junction/polymerization/cap, (6) stator/torque — are represented by high-confidence structural genes, most within one contiguous chromosomal region (~PP_4335–PP_4396, the canonical *Pseudomonas* flagellar Region I), with motor and accessory loci distributed elsewhere. KT2440 is polarly flagellated and motile, and its master flagellar regulator **FleQ** is directly validated (ChIP-seq and Δ*fleQ* non-motility, target-strain evidence).

Of the 47 candidates, **~39 are solid core flagellar genes**. Curation attention should concentrate on eight entries:

- **Three likely over-annotations to remove** from the flagellar bucket: `fliY` (PP_0227, a cystine ABC-transporter binding protein — a name collision), `PP_5157` (amino-acid ABC binding protein), and `PP_1087` (generic OmpA porin).
- **One generic inclusion to drop:** `rpoD`/σ⁷⁰ (PP_0387) is housekeeping, not flagellar-specific.
- **One mis-annotation to correct:** `atoC` (PP_4371) is almost certainly **fleR**, the σ⁵⁴-dependent flagellar response-regulator.
- **Paralog ambiguities to resolve:** the second stator pair `PP_4335`/`PP_4336` (MotCD/MotY-type) and the second FliL paralog `PP_5209`.

The only genuine **coverage gaps** are in the regulatory step: **fleS, fleR, and fleN** — dedicated *Pseudomonas* flagellar regulators — are not captured by the bucket (though fleR is likely mislabeled as atoC). The structural pathway itself has no gaps.

**Confidence:** Structural completeness — high (direct genomic + strong *Pseudomonas* homology). FleQ function — high (direct KT2440 experiments). Regulator identities (atoC→fleR; second stator ortholog) — moderate, flagged for fetch-gene confirmation.

---

## 2. Target-organism pathway definition

**Process included.** Assembly of the bacterial flagellum: the membrane-embedded **flagellum-specific type III secretion system (fT3SS) export apparatus** (FlhA, FlhB, FliP, FliQ, FliR, FliO + cytoplasmic ATPase complex FliI/FliH/FliJ), the **MS-ring** (FliF) and **C-ring/switch** (FliG, FliM, FliN), the **rod** (FlgB, FlgC, FlgF, FlgG, FliE) with rod/hook caps (FlgD, FlgJ), **P- and L-rings** (FlgI/FlgA, FlgH), the **hook** (FlgE) and hook-length control (FliK), the **hook–filament junction** (FlgK, FlgL), **flagellin filament** (FliC) and **cap** (FliD), export **chaperones** (FliS, FliT, FlgN), the **stator/torque units** (MotA/MotB and a second MotCD-type set) plus **FliL**, and the **dedicated transcriptional circuit** (FleQ, FleSR, FliA/σ²⁸, FlgM anti-σ, FleN, with σ⁵⁴/RpoN).

**Neighboring pathways to keep separate.**
- **Bacterial chemotaxis** (KEGG ppu02030): Che proteins signal *to* the C-ring switch (FliM/FliN/FliG) but are a distinct map — do not fold Che genes into ppu02040.
- **Two-component systems** (ppu02020): FleS/FleR belong functionally here as a flagellar TCS, but generic TCS/σ⁷⁰ housekeeping should not be pulled in.
- **Bacterial secretion / injectisome T3SS** (ppu03070): evolutionarily homologous to the flagellar export gate, but KT2440 (an environmental saprophyte) lacks a virulence injectisome — the flagellar apparatus is its principal type III secretion system. No separate injectisome module is expected.

**Alternate names / database definitions.** KEGG map02040 = "Flagellar assembly." GO anchors: flagellum assembly (GO:0009296 / GO:0044780), bacterial-type flagellum (GO:0009288), flagellum-dependent cell motility (GO:0071973), protein secretion by the type III secretion system (GO:0030254). *Pseudomonas* literature refers to the "*fla* regulon" organized in non-contiguous chromosomal regions (Dasgupta 2003, PMID 14617143).

---

## 3. Expected step model (satisfiability verdict)

| # | Module step | Key players expected | KT2440 candidates | Verdict |
|---|-------------|----------------------|-------------------|---------|
| 1 | Late transcription control / regulatory circuit | FleQ, FleS, FleR, FliA(σ²⁸), FlgM, FleN, RpoN(σ⁵⁴) | fleQ (PP_4373), fliA (PP_4341), flgM (PP_4395), rpoN (PP_0952); **atoC=likely fleR** (PP_4371) | **covered but module_needs_revision** (add fleS/fleN; fix atoC→fleR; drop rpoD) |
| 2 | Flagellar type III export | FlhA, FlhB, FliP, FliQ, FliR, FliO, FliI, FliH, FliJ | all 9 present (PP_4344–PP_4367) | **covered** |
| 3 | MS-ring + C-ring switch | FliF, FliG, FliM, FliN | all present (PP_4357–PP_4369) | **covered** |
| 4 | Rod, rings, hook, length control | FlgB/C/F/G, FliE, FlgD, FlgJ, FlgA, FlgH, FlgI, FlgE, FliK | all present (PP_4361–PP_4394) | **covered** |
| 5 | Junction, filament, cap, chaperones | FlgK, FlgL, FliC, FliD, FliS, FliT, FlgN | all present (PP_4374–PP_4396) | **covered** |
| 6 | Stator installation / torque + FliL | MotA, MotB (+ MotCD set), FliL | motA/motB (PP_4905/PP_4904), PP_4335/PP_4336 (2nd stator), fliL (PP_4359), PP_5209 (2nd FliL) | **covered; candidate_uncertain on paralog identity** |

No step is `not_expected_in_target_taxon`. No structural step is a `gap`.

---

## 4. Candidate genes and evidence

**Regulatory (step 1).**
- **fleQ (PP_4373)** — master flagellar/biofilm regulator; **direct KT2440 evidence**: 103 FleQ ChIP-seq binding sites (Blanco-Romero 2018, PMID 30177764); Δ*fleQ* is non-motile with reduced biofilm (Kim 2024, PMID 39570920). High confidence.
- **fliA (PP_4341)** σ²⁸ and **flgM (PP_4395)** anti-σ²⁸ — canonical late-gene checkpoint; homology + operon context; high confidence.
- **rpoN (PP_0952)** σ⁵⁴ — required for Class II flagellar transcription in *Pseudomonas* (PMID 14617143); shared with many σ⁵⁴ regulons (not flagellar-exclusive). Keep, with caveat.
- **atoC (PP_4371)** — annotated generic σ⁵⁴-dependent NtrC/AtoC activator; located inside the flagellar operon between the *fli* genes and *fleQ*; **almost certainly FleR** (the flagellar σ⁵⁴ response regulator). Curation-relevant mis-name → **promote to fetch-gene**.
- **rpoD (PP_0387)** σ⁷⁰ — housekeeping sigma; generic KEGG-map artifact, **not flagellar-specific**.

**Export apparatus (step 2).** flhA, flhB, fliP, fliQ, fliR, fliO, fliI, fliH, fliJ — complete membrane export gate + cytoplasmic ATPase (FliI, EC 7.1.2.2). Note the EC on FliI is a broad F₁-ATPase-like mapping; export can also be PMF-driven via FlhA/FlhB, so treat the EC as descriptive, not a distinct enzymatic step. High confidence by strong *Pseudomonas*/enterobacterial homology + tight operon synteny.

**Basal body / switch / rod / hook / rings / filament / chaperones (steps 3–5).** fliF, fliG, fliM, fliN; flgB/C/F/G, fliE, flgD, flgJ, flgA, flgH, flgI, flgE, fliK; flgK, flgL, fliC, fliD, fliS, fliT, flgN (PP_4396). All are core, unambiguous, syntenic within Region I; high confidence. Caveat: FliO is poorly conserved and short — low sequence identity is expected and should not be read as absence.

**Stator/torque + FliL (step 6).**
- **motA/motB (PP_4905/PP_4904)** and **PP_4335/PP_4336** = two homologous stator sets, matching the **MotAB + MotCD** architecture of *Pseudomonas* (Zhang 2022, *P. aeruginosa*, PMID 36286538). Transfer to KT2440 is strong (close relative, conserved synteny). Ortholog assignment of which pair is MotAB vs MotCD (and whether MotX/MotY-type components exist) needs fetch-gene.
- **fliL (PP_4359)** and **PP_5209 (2nd FliL)** — FliL rings the stator to tune torque/switching and stabilizes the rod (Partridge 2024 review PMID 39096095; P. aeruginosa PMID 36286538). Two paralogs likely partition between the two stator systems.

---

## 5. Gaps, ambiguities, and likely over-annotations

**Likely over-annotations (recommend removal from ppu02040):**
- **fliY (PP_0227)** — annotated "Periplasmic cystine-binding protein." Enterobacterial "FliY" is the substrate-binding subunit of the **FliY/YecS/YecC cystine ABC importer** (Deutch 2014, PMID 25139244), *not* a flagellar C-ring protein. Proteobacteria use the FliM+FliN switch and lack the Bacillus FliM/FliN/FliY switch, so a flagellar FliY is not expected. Classic KEGG **name-collision over-propagation**.
- **PP_5157** — "Solute-binding protein family 3": another amino-acid ABC substrate-binding protein; no flagellar role.
- **PP_1087** — generic OmpA-family outer-membrane porin; not a documented flagellar component (the OmpA/peptidoglycan-binding domain it shares with MotB is a domain-level, not functional, match).

**Generic inclusion to drop:** **rpoD/σ⁷⁰ (PP_0387)** — housekeeping.

**Ambiguity / mis-annotation:** **atoC (PP_4371) → FleR** (see §4).

**Genuine coverage gaps (regulatory step):** **fleS** (sensor kinase) and **fleN** (FleQ anti-activator P-loop ATPase controlling flagellar number; Jain 2016, PMID 26841764) are expected in the KT2440 genome but **not captured** by the bucket. **fleR** is likely present but mislabeled as atoC. → mark step 1 **module_needs_revision**.

**Not over-annotation but worth noting:** two flagellin/HAP paralogs and possible flagellin glycosylation islands vary across *Pseudomonas* (PMID 14617143); if a second flagellin exists in KT2440 it would be an addition, not a gap.

---

## 6. Module and GO-curation recommendations

**Step-level status:**
- Steps 2, 3, 4, 5: **covered**.
- Step 6 (stator): **covered**, but set the two extra stator genes and PP_5209 to **candidate_uncertain** pending ortholog assignment.
- Step 1 (regulation): **covered but module_needs_revision** — add fleS and fleN; reassign atoC→fleR; drop rpoD as non-specific.

**Bucket hygiene:**
- Remove `fliY` (PP_0227), `PP_5157`, `PP_1087`, and `rpoD` (PP_0387) from the flagellar satisfiability count so they do not inflate coverage.
- Keep chemotaxis (ppu02030), generic TCS (ppu02020), and injectisome T3SS (ppu03070) as **separate** modules; mark injectisome **not_expected_in_target_taxon**.

**Module-boundary judgement:** the generic six-step boundary is essentially **correct** for KT2440. One refinement: the regulatory step should explicitly enumerate the *Pseudomonas* enhancer-binding-protein circuit (FleQ–FleSR–FleN–σ⁵⁴ + FliA/FlgM–σ²⁸) rather than the enterobacterial FlhDC master operon, which *Pseudomonas* **does not use** — a lineage-specific alternative worth encoding in the module document.

**GO/term requests:** existing GO terms (GO:0044780 flagellum assembly, GO:0071973 flagellum-dependent motility, GO:0030254 T3SS protein secretion, GO:0006935 chemotaxis for the neighbor) are sufficient; no new terms needed. A curator note recording the FleQ-master-regulator (vs FlhDC) lineage distinction would prevent future over-propagation.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_4371 (atoC → FleR):** confirm identity as the flagellar σ⁵⁴ response regulator; highest curation impact.
2. **PP_4335 / PP_4336:** assign as MotCD (or MotAB) stator set; distinguish from PP_4904/PP_4905.
3. **PP_5209 (2nd FliL):** confirm paralog and its stator partner.
4. **PP_0227 (fliY):** confirm reclassification as cystine-ABC binding protein and removal from the flagellar bucket.
5. **PP_5157 / PP_1087:** confirm non-flagellar (ABC binding protein / OmpA porin) and remove.
6. (Add if present in genome) **fleS, fleN** loci: locate and add to the regulatory step.

---

## 8. Key references

- Blanco-Romero E, *et al.* (2018) Genome-wide analysis of the FleQ direct regulon in *Pseudomonas fluorescens* F113 and *Pseudomonas putida* KT2440. **PMID 30177764** — *direct KT2440 evidence for FleQ as master regulator (103 ChIP-seq sites).*
- Kim, Lee, Darlington, Kim (2024) Impact of *fleQ* deficiency on resource allocation and heterologous gene expression in *Pseudomonas putida*. **PMID 39570920** — *Δ*fleQ* KT2440 is non-motile.*
- Dasgupta N, *et al.* (2003) A four-tiered transcriptional regulatory circuit controls flagellar biogenesis in *Pseudomonas aeruginosa*. **PMID 14617143** — *defines FleQ/FleS/FleR/FliA/FlgM/FleN + RpoN circuit and non-contiguous flagellar regions (strong transfer to KT2440).*
- Jain (2016) Crystallization/analysis of FleN from *P. aeruginosa*. **PMID 26841764** — *FleN is a P-loop ATPase anti-activator of FleQ controlling flagellar number.*
- Zhang C, *et al.* (2022) FliL differentially interacts with two stator systems to regulate flagellar motor output in *Pseudomonas aeruginosa*. **PMID 36286538** — *two homologous MotAB/MotCD stators + FliL.*
- Partridge JD, Harshey RM (2024) Flagellar protein FliL: a many-splendored thing. **PMID 39096095** — *FliL functions at the stator/rod.*
- Deutch CE, *et al.* (2014) L-selenaproline uptake depends on two L-cystine transport systems. **PMID 25139244** — *FliY is the cystine ABC-transporter binding protein (supports over-annotation call).*

---

### Evidence provenance summary
- **Direct KT2440 experimental:** FleQ master-regulator role (PMID 30177764, 39570920).
- **Strong *Pseudomonas* transfer:** four-tiered regulatory circuit, FleN, two-stator system (PMID 14617143, 26841764, 36286538) — close relatives, conserved synteny.
- **Homology / operon-context inference:** all structural export/basal-body/rod-hook/filament genes (Region I synteny + universal bacterial conservation).
- **Over-annotation calls:** fliY/PP_5157/PP_1087/rpoD based on family assignment and KEGG map scope (PMID 25139244 for fliY).

**Open questions for experts:** (i) Does KT2440 encode fleS/fleN at loci outside the bucket, and is PP_4371 confirmed as fleR? (ii) Which stator pair is MotAB vs MotCD, and do accessory MotX/MotY components exist? (iii) Is there a second flagellin / glycosylation island? These are the highest-value resolutions for finalizing module satisfiability.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_flagellar_assembly_export__ppu02040-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_flagellar_assembly_export__ppu02040-deep-research-openscientist_artifacts/final_report.pdf)