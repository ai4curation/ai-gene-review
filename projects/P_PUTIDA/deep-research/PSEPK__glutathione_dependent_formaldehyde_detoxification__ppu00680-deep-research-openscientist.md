---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T08:27:42.317665'
end_time: '2026-09-01T09:25:34.266715'
duration_seconds: 3471.95
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Glutathione-dependent formaldehyde detoxification
  module_summary: A bacterial detoxification module in which formaldehyde is captured
    by glutathione as S-(hydroxymethyl)glutathione, the hemithioacetal is oxidized
    to S-formylglutathione, and the thioester is hydrolyzed to formate while regenerating
    glutathione. Chemical capture, oxidation, and hydrolysis are represented as separate
    steps.
  module_outline: "- Glutathione-dependent formaldehyde detoxification\n  - 1. Glutathione\
    \ capture of formaldehyde\n  - S-(hydroxymethyl)glutathione formation\n  - 2.\
    \ Hemithioacetal oxidation\n  - S-(hydroxymethyl)glutathione oxidation\n    -\
    \ FrmA S-(hydroxymethyl)glutathione dehydrogenase (molecular player: zinc-containing\
    \ alcohol dehydrogenase family, class-3 lineage; activity or role: S-(hydroxymethyl)glutathione\
    \ dehydrogenase [NAD(P)+] activity)\n  - 3. S-formylglutathione hydrolysis and\
    \ glutathione regeneration\n  - S-formylglutathione hydrolysis\n    - FrmC S-formylglutathione\
    \ hydrolase (molecular player: FrmC family; activity or role: S-formylglutathione\
    \ hydrolase activity)"
  module_connections: '- S-(hydroxymethyl)glutathione formation feeds into S-(hydroxymethyl)glutathione
    oxidation

    - S-(hydroxymethyl)glutathione oxidation feeds into S-formylglutathione hydrolysis'
  pathway_query: ppu00680
  pathway_id: ppu00680
  pathway_name: Methane metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00680 with 18 primary genes; module
    area: energy_respiration_inorganic_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '30'
  candidate_genes: '- glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1
    (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - fdhA: PP_0328 | Q88R06 | Formaldehyde dehydrogenase (EC 1.2.1.46) (EC 1.2.1.46;
    primary bucket kegg:ppu00625)

    - fdoG: PP_0489 | A0A140FVZ1 | Formate dehydrogenase-O major subunit (EC 1.2.1.2)
    (EC 1.2.1.2; primary bucket kegg:ppu00680)

    - fdoH: PP_0490 | Q88QK1 | Formate dehydrogenase iron-sulfur subunit (primary
    bucket kegg:ppu00680)

    - fdoI: PP_0491 | Q88QK0 | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2)
    (EC 1.2.1.2; primary bucket kegg:ppu00680)

    - mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37;
    primary bucket kegg:ppu00566)

    - glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine
    methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)

    - hprA: PP_0762 | Q88PT6 | Glycerate dehydrogenase (primary bucket kegg:ppu00680)

    - pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase)
    (EC 2.3.1.8; primary bucket kegg:ppu00430)

    - ppc: PP_1505 | Q88MR4 | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC
    4.1.1.31) (EC 4.1.1.31; primary bucket kegg:ppu00710)

    - eno: PP_1612 | Q88MF9 | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase)
    (2-phosphoglycerate dehydratase) (EC 4.2.1.11; primary bucket kegg:ppu03018)

    - frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1)
    (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III)
    (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary
    bucket kegg:ppu00626)

    - frmC: PP_1617 | Q88MF4 | S-formylglutathione hydrolase (EC 3.1.2.12) (EC 3.1.2.12;
    primary bucket kegg:ppu00680)

    - serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine
    aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)

    - ppsA: PP_2082 | Q88L53 | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2)
    (Pyruvate, water dikinase) (EC 2.7.9.2; primary bucket kegg:ppu00680)

    - PP_2183: PP_2183 | Q88KV6 | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase
    I subunit E) (NDH-1 subunit E) (primary bucket kegg:ppu00680)

    - PP_2184: PP_2184 | Q88KV5 | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase
    I subunit F) (NDH-1 subunit F) (primary bucket kegg:ppu00680)

    - PP_2185: PP_2185 | Q88KV4 | Formate dehydrogenase, alpha subunit (primary bucket
    kegg:ppu00680)

    - PP_2186: PP_2186 | Q88KV3 | Formate dehydrogenase, delta subunit (primary bucket
    kegg:ppu00680)

    - PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary
    bucket kegg:ppu00680)

    - PP_2533: PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family
    protein (primary bucket kegg:ppu00680)

    - ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81;
    primary bucket kegg:ppu00561)

    - acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1)
    (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2)
    (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1;
    primary bucket kegg:ppu00680)

    - serB: PP_4909 | Q88DB8 | Phosphoserine phosphatase (EC 3.1.3.3) (O-phosphoserine
    phosphohydrolase) (EC 3.1.3.3; primary bucket kegg:ppu00680)

    - fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC
    4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)

    - fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1)
    (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11;
    primary bucket kegg:ppu00710)

    - gpmI: PP_5056 | Q88CX4 | 2,3-bisphosphoglycerate-independent phosphoglycerate
    mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4.2.12) (EC
    5.4.2.12; primary bucket kegg:ppu00680)

    - serA: PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC
    1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399; 1.1.1.95; primary bucket kegg:ppu00680)

    - peaA: PP_5602 | A0A140FWF3 | Quinohaemoprotein amine dehydrogenase, alpha subunit
    (EC 1.4.9.1, EC 1.4.99.-) (EC 1.4.9.1; 1.4.99.-; primary bucket kegg:ppu00680)'
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__glutathione_dependent_formaldehyde_detoxification__ppu00680-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__glutathione_dependent_formaldehyde_detoxification__ppu00680-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Glutathione-dependent formaldehyde detoxification in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00680
- Resolved ID: ppu00680
- Resolved name: Methane metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00680 with 18 primary genes; module area: energy_respiration_inorganic_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 30

- glyA1: PP_0322 | Q88R12 | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- fdhA: PP_0328 | Q88R06 | Formaldehyde dehydrogenase (EC 1.2.1.46) (EC 1.2.1.46; primary bucket kegg:ppu00625)
- fdoG: PP_0489 | A0A140FVZ1 | Formate dehydrogenase-O major subunit (EC 1.2.1.2) (EC 1.2.1.2; primary bucket kegg:ppu00680)
- fdoH: PP_0490 | Q88QK1 | Formate dehydrogenase iron-sulfur subunit (primary bucket kegg:ppu00680)
- fdoI: PP_0491 | Q88QK0 | Formate dehydrogenase-O, gamma subunit (EC 1.2.1.2) (EC 1.2.1.2; primary bucket kegg:ppu00680)
- mdh: PP_0654 | Q88Q44 | Probable malate dehydrogenase (EC 1.1.1.37) (EC 1.1.1.37; primary bucket kegg:ppu00566)
- glyA2: PP_0671 | Q88Q27 | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) (EC 2.1.2.1; primary bucket kegg:ppu04981)
- hprA: PP_0762 | Q88PT6 | Glycerate dehydrogenase (primary bucket kegg:ppu00680)
- pta: PP_0774 | Q88PS4 | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) (EC 2.3.1.8; primary bucket kegg:ppu00430)
- ppc: PP_1505 | Q88MR4 | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC 4.1.1.31) (EC 4.1.1.31; primary bucket kegg:ppu00710)
- eno: PP_1612 | Q88MF9 | Enolase (EC 4.2.1.11) (2-phospho-D-glycerate hydro-lyase) (2-phosphoglycerate dehydratase) (EC 4.2.1.11; primary bucket kegg:ppu03018)
- frmA: PP_1616 | Q88MF5 | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrogenase class-III) (Glutathione-dependent formaldehyde dehydrogenase) (EC 1.1.1.1; 1.1.1.284; primary bucket kegg:ppu00626)
- frmC: PP_1617 | Q88MF4 | S-formylglutathione hydrolase (EC 3.1.2.12) (EC 3.1.2.12; primary bucket kegg:ppu00680)
- serC: PP_1768 | Q88M07 | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) (EC 2.6.1.52; primary bucket kegg:ppu00750)
- ppsA: PP_2082 | Q88L53 | Phosphoenolpyruvate synthase (PEP synthase) (EC 2.7.9.2) (Pyruvate, water dikinase) (EC 2.7.9.2; primary bucket kegg:ppu00680)
- PP_2183: PP_2183 | Q88KV6 | NADH-quinone oxidoreductase subunit E (NADH dehydrogenase I subunit E) (NDH-1 subunit E) (primary bucket kegg:ppu00680)
- PP_2184: PP_2184 | Q88KV5 | NADH-quinone oxidoreductase subunit F (NADH dehydrogenase I subunit F) (NDH-1 subunit F) (primary bucket kegg:ppu00680)
- PP_2185: PP_2185 | Q88KV4 | Formate dehydrogenase, alpha subunit (primary bucket kegg:ppu00680)
- PP_2186: PP_2186 | Q88KV3 | Formate dehydrogenase, delta subunit (primary bucket kegg:ppu00680)
- PP_2213: PP_2213 | Q88KS6 | Acyl-CoA synthetase (EC 6.2.1.-) (EC 6.2.1.-; primary bucket kegg:ppu00680)
- PP_2533: PP_2533 | Q88JW4 | D-isomer specific 2-hydroxyacid dehydrogenase family protein (primary bucket kegg:ppu00680)
- ttuD: PP_4300 | Q88F00 | Hydroxypyruvate reductase (EC 1.1.1.81) (EC 1.1.1.81; primary bucket kegg:ppu00561)
- acsA1: PP_4487 | Q88EH6 | Acetyl-coenzyme A synthetase 1 (AcCoA synthetase 1) (Acs 1) (EC 6.2.1.1) (Acetate--CoA ligase 1) (Acyl-activating enzyme 1) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- acsA2: PP_4702 | Q88DW6 | Acetyl-coenzyme A synthetase 2 (AcCoA synthetase 2) (Acs 2) (EC 6.2.1.1) (Acetate--CoA ligase 2) (Acyl-activating enzyme 2) (EC 6.2.1.1; primary bucket kegg:ppu00680)
- serB: PP_4909 | Q88DB8 | Phosphoserine phosphatase (EC 3.1.3.3) (O-phosphoserine phosphohydrolase) (EC 3.1.3.3; primary bucket kegg:ppu00680)
- fba: PP_4960 | Q88D67 | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) (EC 4.1.2.13; primary bucket kegg:ppu00710)
- fbp: PP_5040 | Q88CY9 | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class 1) (EC 3.1.3.11; primary bucket kegg:ppu00710)
- gpmI: PP_5056 | Q88CX4 | 2,3-bisphosphoglycerate-independent phosphoglycerate mutase (BPG-independent PGAM) (Phosphoglyceromutase) (iPGM) (EC 5.4.2.12) (EC 5.4.2.12; primary bucket kegg:ppu00680)
- serA: PP_5155 | Q88CM5 | D-3-phosphoglycerate dehydrogenase (EC 1.1.1.399) (EC 1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399; 1.1.1.95; primary bucket kegg:ppu00680)
- peaA: PP_5602 | A0A140FWF3 | Quinohaemoprotein amine dehydrogenase, alpha subunit (EC 1.4.9.1, EC 1.4.99.-) (EC 1.4.9.1; 1.4.99.-; primary bucket kegg:ppu00680)

## Generic Module Context

### Working Scope

A bacterial detoxification module in which formaldehyde is captured by glutathione as S-(hydroxymethyl)glutathione, the hemithioacetal is oxidized to S-formylglutathione, and the thioester is hydrolyzed to formate while regenerating glutathione. Chemical capture, oxidation, and hydrolysis are represented as separate steps.

### Provisional Biological Outline

- Glutathione-dependent formaldehyde detoxification
  - 1. Glutathione capture of formaldehyde
  - S-(hydroxymethyl)glutathione formation
  - 2. Hemithioacetal oxidation
  - S-(hydroxymethyl)glutathione oxidation
    - FrmA S-(hydroxymethyl)glutathione dehydrogenase (molecular player: zinc-containing alcohol dehydrogenase family, class-3 lineage; activity or role: S-(hydroxymethyl)glutathione dehydrogenase [NAD(P)+] activity)
  - 3. S-formylglutathione hydrolysis and glutathione regeneration
  - S-formylglutathione hydrolysis
    - FrmC S-formylglutathione hydrolase (molecular player: FrmC family; activity or role: S-formylglutathione hydrolase activity)

### Known Relationships Among Steps

- S-(hydroxymethyl)glutathione formation feeds into S-(hydroxymethyl)glutathione oxidation
- S-(hydroxymethyl)glutathione oxidation feeds into S-formylglutathione hydrolysis

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

# Module/Pathway/Taxon Review: Glutathione-dependent Formaldehyde Detoxification in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00680` "Methane metabolism" (module area: energy_respiration_inorganic_metabolism)
**Module under review:** Glutathione-dependent formaldehyde detoxification (chemical capture → hemithioacetal oxidation → thioester hydrolysis)

---

## 1. Executive Summary

The glutathione (GSH)-dependent formaldehyde detoxification module **is present and satisfiable** in *Pseudomonas putida* KT2440, but with two curation-critical qualifications. First, the module's enzymatic core reduces to exactly **two adjacent, single-copy genes**: `frmA` (**PP_1616**, Q88MF5; S-(hydroxymethyl)glutathione dehydrogenase, EC 1.1.1.1 / 1.1.1.284, KO K00121) and `frmC` (**PP_1617**, Q88MF4; S-formylglutathione hydrolase, EC 3.1.2.12, KO K01070). These form a compact two-gene operon (9-bp intergenic gap) controlled by a divergently transcribed LysR-type regulator, PP_1615. Step 1 of the module — capture of formaldehyde by glutathione to form S-(hydroxymethyl)glutathione — is a **spontaneous, non-enzymatic** chemical reaction in this organism; no formaldehyde-activating enzyme (Gfa) is encoded in the proteome, which is expected because KT2440 is not a methylotroph.

Second, and most important for module satisfiability, the GSH route is a **secondary/backup pathway** in KT2440. The organism detoxifies formaldehyde predominantly through **glutathione-INDEPENDENT** NAD-linked formaldehyde dehydrogenases — `fdhA`/PP_0328 (EC 1.2.1.46, KO K00148, carrying the diagnostic InterPro IPR014184 "HCHO_DH_non_GSH" signature) and PP_3970 (a Zn/NAD(P) oxidoreductase not in the candidate list). Roca et al. (2009) showed that a double mutant lacking both GSH-independent enzymes still evolved CO₂ from formaldehyde, implying an additional route — plausibly the GSH-dependent FrmA pathway acting as backup. The resulting formate is oxidized to CO₂ by two formate dehydrogenase clusters (PP_0489–0492 and PP_2183–2186).

The dominant curation problem is that the supplied 30-gene candidate list is an artifact of **KEGG map-level (ppu00680 "Methane metabolism") membership**, not true module membership. Only `frmA` and `frmC` belong to the GSH-dependent formaldehyde-oxidation steps. The remaining ~28 genes are serine-cycle / serine-biosynthesis enzymes, downstream formate dehydrogenases, central-metabolism enzymes, and an amine dehydrogenase that co-occur on the broad overview map. **Recommendation:** mark steps 2 and 3 *covered* by `frmA` and `frmC` respectively, mark step 1 *covered (non-enzymatic)*, flag `frmA` and `frmC` for full `fetch-gene` review, and **revise the bucket** into a dedicated {frmA, frmC} module distinct from the KEGG methane-metabolism overview map.

---

## 2. Target-Organism Pathway Definition

### What this module includes

The GSH-dependent formaldehyde detoxification module is a three-step process that converts cytotoxic formaldehyde into formate while regenerating glutathione:

| Step | Reaction | Catalyst in KT2440 | Nature |
|------|----------|--------------------|--------|
| 1. GSH capture | Formaldehyde + GSH → S-(hydroxymethyl)glutathione (hemithioacetal) | none (spontaneous) | Non-enzymatic |
| 2. Hemithioacetal oxidation | S-(hydroxymethyl)glutathione + NAD⁺ → S-formylglutathione + NADH + H⁺ | FrmA / PP_1616 | Enzymatic |
| 3. Thioester hydrolysis | S-formylglutathione + H₂O → formate + GSH + H⁺ | FrmC / PP_1617 | Enzymatic |

The output, **formate**, is then handed off to formate dehydrogenase(s) for oxidation to CO₂ — but that oxidation is a **separate downstream pathway**, not part of the detox module proper.

### Neighboring pathways to keep separate

For curation, the following processes are represented in the candidate list because they share the KEGG ppu00680 overview map, but must be kept **outside** the GSH-detox module boundary:

- **Glutathione-independent formaldehyde oxidation** (`fdhA`/PP_0328, PP_3970) — a *parallel* detox route, mechanistically and evolutionarily distinct (different KO: K00148 vs. K00121).
- **Formate oxidation to CO₂** (`fdoGHI`/PP_0489–0491; PP_2183–2186) — downstream of the module.
- **Serine cycle / C1 assimilation and serine biosynthesis** (`glyA1`, `glyA2`, `serA`, `serB`, `serC`, `hprA`, `gpmI`, `eno`, `ppc`, `ppsA`, `fba`, `fbp`, `mdh`, `pta`, `ttuD`, PP_2533).
- **Acetate/acyl-CoA activation** (`acsA1`, `acsA2`, PP_2213).
- **Amine oxidation** (`peaA`, quinohaemoprotein amine dehydrogenase).

### Alternate names / database definitions

- The FrmA enzyme has multiple synonyms: **class-III (class-3) alcohol dehydrogenase**, **glutathione-dependent formaldehyde dehydrogenase**, **S-(hydroxymethyl)glutathione dehydrogenase**, ADH5 (eukaryotic ortholog). EC numbers 1.1.1.1 and 1.1.1.284 both apply.
- FrmC = **S-formylglutathione hydrolase (FGH)**, EstD in humans, EC 3.1.2.12.
- In enterobacteria the operon is `frmRAB` (regulator–dehydrogenase–hydrolase); KT2440 lacks the enterobacterial FrmR sensor and uses a LysR-type regulator instead (see §5).

---

## 3. Expected Step Model and Satisfiability

```
   Formaldehyde (HCHO)
        |
        |  + GSH   (STEP 1: spontaneous chemical capture — NON-ENZYMATIC)
        v
   S-(hydroxymethyl)glutathione   [hemithioacetal]
        |
        |  NAD+ --> NADH   (STEP 2: FrmA / PP_1616, EC 1.1.1.284, K00121)   <-- COVERED
        v
   S-formylglutathione   [thioester]
        |
        |  + H2O   (STEP 3: FrmC / PP_1617, EC 3.1.2.12, K01070)            <-- COVERED
        v
   Formate  +  GSH (regenerated)
        |
        |  (downstream, SEPARATE pathway: formate dehydrogenases
        |   PP_0489-0492, PP_2183-2186)
        v
       CO2
```

**Satisfiability verdict:**

| Module step | Status | Encoded by | Confidence |
|-------------|--------|-----------|------------|
| 1. GSH capture of formaldehyde | **covered (non-enzymatic)** | none required | High — reaction is spontaneous; module outline itself labels it "chemical capture" |
| 2. Hemithioacetal oxidation | **covered** | `frmA` / PP_1616 | High — direct UniProt annotation + operon context + literature |
| 3. S-formylglutathione hydrolysis | **covered** | `frmC` / PP_1617 | High — direct UniProt annotation + operon context |

No expected step is a *gap*. No step requires a lineage-specific replacement. The only "missing" component relative to the enterobacterial paradigm is the FrmR regulator, and its absence is expected (see §5) and does not affect catalytic satisfiability.

---

## 4. Candidate Genes and Evidence

### 4.1 High-confidence module core

**`frmA` — PP_1616 (Q88MF5), S-(hydroxymethyl)glutathione dehydrogenase**

FrmA is a zinc-containing, class-III alcohol dehydrogenase that catalyzes the NAD⁺-dependent oxidation of the GSH–formaldehyde hemithioacetal: S-(hydroxymethyl)glutathione + NAD⁺ → S-formylglutathione + NADH + H⁺ (EC 1.1.1.1 / 1.1.1.284). UniProt Q88MF5 explicitly notes "Has high formaldehyde dehydrogenase activity in the presence of glutathione." This is the **central, defining reaction** of the module. Osman et al. (2016) confirm that "Formaldehyde detoxification by FrmA requires S-(hydroxymethyl)glutathione" [PMID: 27474740], establishing that FrmA acts on the GSH adduct rather than free formaldehyde. Evidence type for KT2440: strong homology-based annotation plus operon/genomic-context support; direct enzymology is from orthologs. **Curation caveat:** the KEGG primary bucket for `frmA` in the metadata is `ppu00626` (naphthalene/aminobenzoate — likely a class-III ADH broad mapping), which is misleading; the functionally correct assignment is the GSH-detox module. Promote to full review.

**`frmC` — PP_1617 (Q88MF4), S-formylglutathione hydrolase**

FrmC is a serine hydrolase (GXSXG-type esterase fold) that hydrolyzes the S-formylglutathione thioester: S-formylglutathione + H₂O → formate + glutathione + H⁺ (EC 3.1.2.12). UniProt Q88MF4 describes it as "Serine hydrolase involved in the detoxification of formaldehyde." This step both releases formate and **regenerates glutathione**, closing the cycle. Homology-based support is strengthened by the note that lactococcal EstA and human EstD/FGH share significant similarity as "part of a universal formaldehyde detoxification pathway" [PMID: 10742212]. Evidence type for KT2440: strong homology-based annotation + operon context. Promote to full review.

### 4.2 Parallel / downstream / off-module candidates (do NOT count toward module coverage)

| Gene | Locus | Assigned role | Why excluded from GSH module |
|------|-------|---------------|------------------------------|
| `fdhA` | PP_0328 | Formaldehyde dehydrogenase, EC 1.2.1.46 | **Glutathione-INDEPENDENT** (IPR014184 "HCHO_DH_non_GSH", KO K00148) — parallel route, not GSH module |
| (PP_3970) | PP_3970 | Zn/NAD(P) oxidoreductase | Second GSH-independent formaldehyde dehydrogenase; not in candidate list |
| `fdoG/H/I` | PP_0489–0491 | Formate dehydrogenase-O | Downstream formate → CO₂, separate pathway |
| PP_2183–2186 | — | NDH-1 subunits + formate dehydrogenase α/δ | Downstream formate oxidation / respiration |
| `glyA1`,`glyA2` | PP_0322, PP_0671 | Serine hydroxymethyltransferase | Serine/one-carbon metabolism (bucket ppu04981) |
| `serA`,`serB`,`serC` | PP_5155, PP_4909, PP_1768 | Serine biosynthesis | Amino-acid biosynthesis, not detox |
| `hprA`,`ttuD`,PP_2533 | PP_0762, PP_4300, PP_2533 | 2-hydroxyacid/hydroxypyruvate reductases | Serine cycle / C2 metabolism |
| `eno`,`gpmI`,`fba`,`fbp`,`ppc`,`ppsA`,`mdh`,`pta` | various | Central carbon metabolism | Glycolysis/gluconeogenesis/anaplerosis |
| `acsA1`,`acsA2`,PP_2213 | PP_4487, PP_4702, PP_2213 | Acetyl-CoA synthetases / acyl-CoA synthetase | Acetate activation |
| `peaA` | PP_5602 | Quinohaemoprotein amine dehydrogenase | Amine oxidation (a formaldehyde *source*, not detox) |

Of the 30 candidates, **28 are KEGG map-level associations** that co-occur on the ppu00680 "Methane metabolism" overview map but do not participate in the GSH-dependent detox reactions.

---

## 5. Gaps, Ambiguities, and Likely Over-annotations

### 5.1 The candidate list is a KEGG overview-map artifact

The single largest curation issue: `ppu00680` "Methane metabolism" is a **broad overview map**, and 28 of 30 candidates were pulled in by map membership rather than by participation in the GSH-detox reactions (Finding F003). This inflates apparent module complexity. The true module core is `frmA` + `frmC`. Any automated satisfiability call that treats all 30 as module members would be wrong.

### 5.2 No paralog ambiguity for the core enzymes

KEGG KO→gene mapping in *P. putida* KT2440 is clean and single-copy (Finding F007):

- K00121 (S-(hydroxymethyl)glutathione dehydrogenase) → **PP_1616 only**
- K01070 (S-formylglutathione hydrolase) → **PP_1617 only**

There is no second copy of either enzyme to create ambiguity. The GSH-independent `fdhA`/PP_0328 is cleanly separated into a distinct ortholog group (K00148), so it will not be mis-assigned to the GSH module at the KO level.

### 5.3 No Gfa; no enterobacterial FrmR

A proteome-wide InterPro/Pfam screen (Finding F006) confirmed:

- **No bona fide Gfa** (glutathione-dependent formaldehyde-activating enzyme). The single Pfam PF04244 hit (Q88JB7 / PP_2732) is a cryptochrome/photolyase family protein, not Gfa. This is expected: Gfa accelerates hemithioacetal formation in methylotrophs (e.g., *Paracoccus denitrificans*, *Methylobacterium*), and KT2440 is not a methylotroph. Step 1 therefore remains non-enzymatic in this organism.
- **No FrmR formaldehyde sensor.** The only DUF156-family protein (Pfam PF02583 / IPR003735) is Q88IN0 / PP_2969 = **CsoR**, a copper-sensing repressor, NOT a formaldehyde-sensing FrmR. Instead, the frm operon is controlled by a divergent **LysR-type regulator, PP_1615** (Q88MF6) (Findings F003, F005).

### 5.4 Broad EC / bucket mislabels to correct

- `frmA` primary bucket in metadata is `ppu00626`; functionally it belongs to formaldehyde detox. The class-III ADH annotation (EC 1.1.1.1) is broad; the module-relevant activity is EC 1.1.1.284.
- `frmC` metadata bucket is correctly `ppu00680`, but should be re-scoped to the dedicated detox module.
- `fdhA` is at risk of being conflated with GSH-dependent formaldehyde dehydrogenase because both share the phrase "formaldehyde dehydrogenase"; the IPR014184 signature and EC 1.2.1.46 firmly place it in the **GSH-independent** class.

### 5.5 Genomic context of the operon

KEGG coordinates (Finding F005): `frmA` PP_1616 at 1,812,522–1,813,637 (+); `frmC` PP_1617 at 1,813,646–1,814,500 (+) — a 9-bp intergenic gap consistent with a single transcriptional unit. PP_1615 (LysR regulator) sits divergently on the (–) strand at 1,811,521–1,812,417, ~105 bp upstream of `frmA`. Flanking genes PP_1614 (`ispD`) and PP_1618 (`ispF`) are MEP-pathway isoprenoid genes, unrelated to formaldehyde metabolism — so the operon is compact and cleanly bounded.

```
 (-) strand        (+) strand ----->
 PP_1614  PP_1615        PP_1616 (frmA) --9bp-- PP_1617 (frmC)   PP_1618
 ispD    LysR reg  <-->  S-(hydroxymethyl)GSH   S-formylGSH       ispF
 (MEP)   (divergent)      dehydrogenase          hydrolase        (MEP)
```

---

## 6. Module and GO-curation Recommendations

### 6.1 Step-level status calls

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| 1. GSH capture of formaldehyde | **covered — non-enzymatic** | Spontaneous hemithioacetal formation; no gene needed; Gfa correctly *not_expected_in_target_taxon* |
| 2. Hemithioacetal oxidation | **covered** | `frmA` / PP_1616 (K00121), single-copy, high confidence |
| 3. S-formylglutathione hydrolysis + GSH regeneration | **covered** | `frmC` / PP_1617 (K01070), single-copy, high confidence |

No step is `gap` or `candidate_uncertain` at the catalytic level.

### 6.2 Bucket / module boundary corrections (`module_needs_revision`)

- **The bucket needs revision.** The generic `ppu00680` "Methane metabolism" bucket is the wrong container for this module in KT2440. Create/point to a **dedicated {frmA, frmC} GSH-dependent formaldehyde detoxification** module, explicitly excluding the 28 overview-map co-members.
- Mark the parallel **GSH-independent** detox route (`fdhA`/PP_0328, PP_3970) as a *separate module* — it is biologically the dominant route and should be tracked, but not folded into the GSH module.
- Optionally annotate a *downstream* formate-oxidation module (PP_0489–0492, PP_2183–2186) as adjacent but distinct.

### 6.3 Species-aware note for module satisfiability

The GSH module is **satisfiable but non-essential** in KT2440. Because the organism carries redundant GSH-independent formaldehyde dehydrogenases (Finding F001), a satisfiability engine should record the GSH route as a **backup/secondary** pathway. This context prevents an over-interpretation that FrmA/FrmC are the primary formaldehyde-clearance machinery.

### 6.4 GO-term requests

No new GO terms appear necessary. Existing terms cover the reactions: GO:0004022/GO:0051903 (S-(hydroxymethyl)glutathione dehydrogenase / alcohol dehydrogenase [NAD⁺] activity), GO:0018738 (S-formylglutathione hydrolase activity), and GO:0046294 (formaldehyde catabolic process). Ensure `frmA` carries the class-III/GSH-dependent activity annotation (GO:0051903) and not merely generic alcohol dehydrogenase; and that `fdhA` is annotated to the **glutathione-independent** formaldehyde dehydrogenase activity to keep the two routes distinct.

---

## 7. Genes to Promote to Full `fetch-gene` Review

| Gene | Locus | UniProt | Priority | Reason |
|------|-------|---------|----------|--------|
| `frmA` | PP_1616 | Q88MF5 | **High** | Core module step 2; correct EC 1.1.1.284 vs broad EC 1.1.1.1; fix misleading ppu00626 bucket |
| `frmC` | PP_1617 | Q88MF4 | **High** | Core module step 3; confirm S-formylglutathione hydrolase and GSH regeneration |
| `fdhA` | PP_0328 | Q88R06 | Medium | Ensure annotation as **GSH-independent** (K00148, IPR014184); prevent conflation with FrmA |
| PP_1615 | PP_1615 | Q88MF6 | Medium | Confirm LysR-type regulator of frm operon; document divergent transcription |
| PP_3970 | PP_3970 | Q88FV8 | Low | Second GSH-independent formaldehyde dehydrogenase; add to parallel module if tracked |

---

## 8. Mechanistic Model / Interpretation

*P. putida* KT2440 possesses a **layered formaldehyde defense**. The frontline is a set of **glutathione-independent, NAD-linked formaldehyde dehydrogenases** (`fdhA`/PP_0328 and PP_3970) that directly oxidize free formaldehyde to formate. Roca et al. (2009) demonstrated this redundancy: single and double knockouts of the two GSH-independent enzymes both retained the ability to evolve ¹⁴CO₂ from ¹⁴C-formaldehyde, and a double mutant *still* evolved CO₂, implying at least a third route [PMID: 19304846]. That residual activity is most parsimoniously explained by the **GSH-dependent FrmA/FrmC pathway acting as a backup**.

In the GSH route, formaldehyde is first captured spontaneously by cellular glutathione to form the hemithioacetal S-(hydroxymethyl)glutathione — no enzyme (Gfa) is needed or encoded, consistent with KT2440's non-methylotrophic lifestyle. FrmA (PP_1616) then oxidizes the hemithioacetal to the thioester S-formylglutathione using NAD⁺, and FrmC (PP_1617) hydrolyzes the thioester to release formate and regenerate glutathione. Both enzymatic steps are encoded by a tight two-gene operon under a dedicated LysR-type regulator (PP_1615). All formaldehyde-derived formate — from either route — converges on the cell's **formate dehydrogenase clusters** (PP_0489–0492 and PP_2183–2186) for terminal oxidation to CO₂, allowing near-stoichiometric conversion of formaldehyde to CO₂ (physiological study, [PMID: 21261833]).

This layered model has a clear curation implication: the *molecular identity* of the GSH module is minimal and unambiguous (two single-copy genes), while its *physiological weight* is secondary. The candidate list's apparent breadth is an accident of KEGG overview-map bookkeeping, not biology.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports/challenges the review |
|------|-----------------|----------------------------------------|
| [PMID: 19304846](https://pubmed.ncbi.nlm.nih.gov/19304846/) | *Redundancy of enzymes for formaldehyde detoxification in P. putida* | **Core evidence** that KT2440 uses redundant GSH-INDEPENDENT formaldehyde dehydrogenases as the dominant route; residual CO₂ evolution in the double mutant implies an additional (GSH) route. Establishes the "backup" status of the module. |
| [PMID: 21261833](https://pubmed.ncbi.nlm.nih.gov/21261833/) | *Physiological responses of P. putida to formaldehyde* | Confirms two formaldehyde dehydrogenases + two formate dehydrogenase complexes stoichiometrically convert formaldehyde to CO₂; glutathione-biosynthesis mutants fail to grow at 1.5 mM HCHO, supporting a role for the GSH system. |
| [PMID: 27474740](https://pubmed.ncbi.nlm.nih.gov/27474740/) | *Effectors and sensory sites of FrmR* | Confirms "Formaldehyde detoxification by FrmA requires S-(hydroxymethyl)glutathione" — anchors FrmA's substrate as the GSH adduct (module step 2). |
| [PMID: 16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/) | *Coupling of vanillate-O-demethylase and formaldehyde detox* | Shows formaldehyde (a demethylation by-product) is converted to formate, and that *frmA* (GSH-dependent formaldehyde dehydrogenase) disruption blocks formate accumulation — supports FrmA's detox function (in a coupled *P. putida*/E. coli context). |
| [PMID: 11133961](https://pubmed.ncbi.nlm.nih.gov/11133961/) | *Two-component regulation of methanol/formaldehyde oxidation in Paracoccus denitrificans* | Documents the GSH-dependent formaldehyde dehydrogenase (fhlA) + S-formylglutathione hydrolase (fghA) pair in a methylotroph — the context where Gfa-type activation is relevant, contrasting with non-methylotroph KT2440. |
| [PMID: 10742212](https://pubmed.ncbi.nlm.nih.gov/10742212/) | *Tributyrin esterase of Lactococcus lactis* | Establishes S-formylglutathione hydrolase (FGH) as part of a "universal formaldehyde detoxification pathway" via sequence similarity — supports FrmC family assignment. |
| [PMID: 37273222](https://pubmed.ncbi.nlm.nih.gov/37273222/) | *Core and auxiliary functions of one-carbon metabolism* | Context for one-carbon/serine metabolism that populates much of the ppu00680 overview map — supports excluding those genes from the detox module. |

**Direct experimental evidence for the target strain:** the redundancy and physiology of formaldehyde detoxification (PMIDs 19304846, 21261833) are from *P. putida* KT2440 itself. **Homology/database-inferred evidence:** the specific catalytic assignments of FrmA and FrmC in KT2440 rest on UniProt annotation and operon context, with direct enzymology drawn from orthologs (Paracoccus, human, lactococcal FGH).

---

## 10. Limitations and Knowledge Gaps

1. **No direct KT2440 enzymology for FrmA/FrmC.** The catalytic assignments are annotation- and homology-based (UniProt Q88MF5, Q88MF4). No published in-vitro kinetics or knockout-phenotype paper isolates FrmA/FrmC activity in KT2440 specifically. The "backup route" interpretation is inferred from residual activity in GSH-independent double mutants (PMID 19304846), not from a direct frmA/frmC knockout.
2. **Regulator not experimentally validated.** PP_1615 is annotated as LysR-type and is positioned divergently, but its role as the frm-operon regulator and its inducer (formaldehyde? S-formylglutathione?) have not been experimentally demonstrated in KT2440.
3. **Step 1 kinetics.** The assumption that hemithioacetal formation is fully non-enzymatic is standard for non-methylotrophs, but glutathione pool size and any accessory factors under formaldehyde stress in KT2440 are not quantified here.
4. **PP_3970 not in candidate list.** Identified from proteome screening; its exact contribution relative to fdhA is not resolved.
5. **Literature scope.** Two of the seven retrieved papers (Paracoccus, Lactococcus) are non-target organisms used for cross-species inference; transfer of mechanistic detail to KT2440 is homology-based, not direct.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate):**
1. Split the `ppu00680` bucket: create a dedicated **{frmA, frmC} GSH-dependent formaldehyde detoxification** module; move the 28 overview-map co-members out.
2. Create a separate **GSH-independent formaldehyde oxidation** module ({fdhA/PP_0328, PP_3970}) and a **formate → CO₂** module (fdo clusters).
3. Correct `frmA` bucket (from ppu00626) and ensure EC 1.1.1.284 / GO:0051903 are primary.
4. Promote `frmA`, `frmC` (and secondarily `fdhA`, PP_1615) to full `fetch-gene` review.

**Wet-lab / expert questions (to resolve gaps):**
5. Construct single and double `ΔfrmA`/`ΔfrmC` mutants (and combine with `ΔfdhA ΔPP_3970`) and measure formaldehyde tolerance and ¹⁴CO₂ evolution to directly quantify the GSH route's backup contribution.
6. Test whether PP_1615 deletion derepresses or abolishes frmA-frmC expression, and identify the inducing signal.
7. Verify the frmA-frmC operon by RT-PCR / RNA-seq (predicted single transcript from the 9-bp gap).
8. Confirm in-vitro that KT2440 FrmA requires the GSH-formaldehyde adduct (not free formaldehyde) and that FrmC regenerates GSH.

---

## Key References

1. Roca A, Rodríguez-Herva JJ, Ramos JL. *Redundancy of enzymes for formaldehyde detoxification in Pseudomonas putida.* [PMID: 19304846](https://pubmed.ncbi.nlm.nih.gov/19304846/)
2. Roca A et al. *Physiological responses of Pseudomonas putida to formaldehyde during detoxification.* [PMID: 21261833](https://pubmed.ncbi.nlm.nih.gov/21261833/)
3. Osman D et al. *The effectors and sensory sites of formaldehyde-responsive regulator FrmR and metal-sensing variant.* [PMID: 27474740](https://pubmed.ncbi.nlm.nih.gov/27474740/)
4. *Functional coupling between vanillate-O-demethylase and formaldehyde detoxification pathway.* [PMID: 16242864](https://pubmed.ncbi.nlm.nih.gov/16242864/)
5. Harms N et al. *Two-component system that regulates methanol and formaldehyde oxidation in Paracoccus denitrificans.* [PMID: 11133961](https://pubmed.ncbi.nlm.nih.gov/11133961/)
6. Fernández de Palencia P et al. *Cloning and characterization of the major tributyrin esterase (S-formylglutathione hydrolase homolog) of Lactococcus lactis.* [PMID: 10742212](https://pubmed.ncbi.nlm.nih.gov/10742212/)
7. *Core and auxiliary functions of one-carbon metabolism.* [PMID: 37273222](https://pubmed.ncbi.nlm.nih.gov/37273222/)


## Artifacts

- [OpenScientist final report](PSEPK__glutathione_dependent_formaldehyde_detoxification__ppu00680-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__glutathione_dependent_formaldehyde_detoxification__ppu00680-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27474740
2. PMID:10742212
3. PMID:19304846
4. PMID:21261833
5. PMID:16242864
6. PMID:11133961
7. PMID:37273222