---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T11:17:44.190127'
end_time: '2026-09-01T11:45:24.719178'
duration_seconds: 1660.53
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial assimilatory nitrate uptake and reduction
  module_summary: A reusable bacterial module for importing nitrate and reducing it
    through nitrite to ammonium for biosynthesis. A nitrate/nitrite porter supplies
    the intracellular nitrate pool, an assimilatory molybdoenzyme reduces nitrate
    to nitrite, and a siroheme-containing NirBD complex performs the six-electron
    reduction of nitrite to ammonium. The module stops at ammonium; incorporation
    through GS-GOGAT is represented by the separate bacterial ammonia assimilation
    module. Respiratory nitrate reduction, denitrification, and dissimilatory nitrate
    reduction to ammonium are outside this boundary.
  module_outline: "- Bacterial assimilatory nitrate uptake and reduction\n  - 1. nitrate\
    \ import\n  - Nitrate import by a nitrate/nitrite porter\n    - Alternative versions\
    \ by transporter architecture: Nitrate import system\n      - Nitrate/nitrite\
    \ porter\n        - Nitrate transmembrane transporter activity (molecular player:\
    \ bacterial nitrate/nitrite porter family; activity or role: nitrate transmembrane\
    \ transporter activity)\n      - NrtABCD ABC-type nitrate importer\n        -\
    \ ABC-type nitrate import (molecular player: cyanobacterial NrtABCD nitrate transporter;\
    \ activity or role: nitrate transmembrane transporter activity)\n  - 2. nitrate\
    \ reduction to nitrite\n  - Assimilatory NAD(P)H-dependent nitrate reduction\n\
    \    - Alternative versions by electron-input architecture: Assimilatory nitrate\
    \ reductase implementation\n      - Fused molybdoenzyme and pyridine-nucleotide\
    \ reductase\n        - Fused assimilatory nitrate reductase activity (molecular\
    \ player: fused diflavin assimilatory nitrate reductase family; activity or role:\
    \ nitrate reductase [NAD(P)H] activity)\n      - Split NasBC nitrate reductase\n\
    \        - Split assimilatory nitrate reductase activity (molecular player: split\
    \ bacterial NasBC assimilatory nitrate reductase; activity or role: nitrate reductase\
    \ [NAD(P)H] activity)\n      - Ferredoxin-linked NarB nitrate reductase\n    \
    \    - Ferredoxin-nitrate reductase activity (molecular player: ferredoxin-linked\
    \ bacterial NarB nitrate-reductase family; activity or role: ferredoxin-nitrate\
    \ reductase activity)\n  - 3. nitrite reduction to ammonium\n  - NirBD-dependent\
    \ assimilatory nitrite reduction\n    - NirBD nitrite reductase activity (molecular\
    \ player: bacterial NirBD assimilatory nitrite reductase complex; activity or\
    \ role: nitrite reductase [NAD(P)H] activity)"
  module_connections: '- Nitrate import by a nitrate/nitrite porter feeds into Assimilatory
    NAD(P)H-dependent nitrate reduction: Imported nitrate is the substrate of assimilatory
    nitrate reductase.

    - Assimilatory NAD(P)H-dependent nitrate reduction feeds into NirBD-dependent
    assimilatory nitrite reduction: Nitrate reductase supplies nitrite to the NirBD
    complex.'
  pathway_query: ppu00910
  pathway_id: ppu00910
  pathway_name: Nitrogen metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00910 with 19 primary genes; module
    area: energy_respiration_inorganic_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '20'
  candidate_genes: '- cynT: PP_0100 | Q88RM9 | Carbonic anhydrase (EC 4.2.1.1) (Carbonate
    dehydratase) (EC 4.2.1.1; primary bucket kegg:ppu00910)

    - PP_0430: PP_0430 | Q88QQ8 | Uncharacterized protein (primary bucket kegg:ppu00910)

    - gdhA: PP_0675 | Q88Q23 | Glutamate dehydrogenase (primary bucket kegg:ppu00910)

    - arcC: PP_0999 | Q88P54 | Carbamate kinase (primary bucket kegg:ppu00910)

    - nirB: PP_1705 | Q88M69 | Nitrite reductase [NAD(P)H] large subunit (EC 1.7.1.4)
    (EC 1.7.1.4; primary bucket kegg:ppu00910)

    - nirD: PP_1706 | Q88M68 | Nitrite reductase (primary bucket kegg:ppu00910)

    - gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC
    1.4.1.2; primary bucket kegg:ppu00430)

    - nasA: PP_2092 | Q88L43 | Nitrate/nitrite transporter (primary bucket kegg:ppu00910)

    - puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)

    - PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - PP_3392: PP_3392 | Q88HG6 | Gamma carbonic anhydrase family protein (primary
    bucket kegg:ppu00910)

    - yrpB: PP_3827 | Q88G98 | Nitronate monooxygenase (Propionate 3-nitronate monooxygenase)
    (primary bucket kegg:ppu00910)

    - PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)

    - glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary
    bucket kegg:ppu00910)

    - gltD: PP_5075 | Q88CV5 | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13)
    (EC 1.4.1.13; primary bucket kegg:ppu00910)

    - gltB: PP_5076 | Q88CV4 | Glutamate synthase [NADPH] large chain (EC 1.4.1.13)
    (Glutamate synthase subunit alpha) (EC 1.4.1.13; primary bucket kegg:ppu00910)

    - spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)

    - puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11;
    primary bucket kegg:ppu00910)'
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_assimilatory_nitrate_reduction__ppu00910-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_assimilatory_nitrate_reduction__ppu00910-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial assimilatory nitrate uptake and reduction in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00910
- Resolved ID: ppu00910
- Resolved name: Nitrogen metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00910 with 19 primary genes; module area: energy_respiration_inorganic_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 20

- cynT: PP_0100 | Q88RM9 | Carbonic anhydrase (EC 4.2.1.1) (Carbonate dehydratase) (EC 4.2.1.1; primary bucket kegg:ppu00910)
- PP_0430: PP_0430 | Q88QQ8 | Uncharacterized protein (primary bucket kegg:ppu00910)
- gdhA: PP_0675 | Q88Q23 | Glutamate dehydrogenase (primary bucket kegg:ppu00910)
- arcC: PP_0999 | Q88P54 | Carbamate kinase (primary bucket kegg:ppu00910)
- nirB: PP_1705 | Q88M69 | Nitrite reductase [NAD(P)H] large subunit (EC 1.7.1.4) (EC 1.7.1.4; primary bucket kegg:ppu00910)
- nirD: PP_1706 | Q88M68 | Nitrite reductase (primary bucket kegg:ppu00910)
- gdhB: PP_2080 | Q88L55 | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) (EC 1.4.1.2; primary bucket kegg:ppu00430)
- nasA: PP_2092 | Q88L43 | Nitrate/nitrite transporter (primary bucket kegg:ppu00910)
- puuA-I: PP_2178 | Q88KW1 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)
- PP_3148: PP_3148 | Q88I53 | Glutamine synthetase (primary bucket kegg:ppu00910)
- PP_3392: PP_3392 | Q88HG6 | Gamma carbonic anhydrase family protein (primary bucket kegg:ppu00910)
- yrpB: PP_3827 | Q88G98 | Nitronate monooxygenase (Propionate 3-nitronate monooxygenase) (primary bucket kegg:ppu00910)
- PP_4399: PP_4399 | Q88EQ4 | Glutamine synthetase (primary bucket kegg:ppu00910)
- PP_4547: PP_4547 | Q88EB9 | Glutamine synthetase (primary bucket kegg:ppu00910)
- glnA: PP_5046 | Q88CY3 | Glutamine synthetase (EC 6.3.1.2) (EC 6.3.1.2; primary bucket kegg:ppu00910)
- gltD: PP_5075 | Q88CV5 | Glutamate synthase (NADPH) beta subunit (EC 1.4.1.13) (EC 1.4.1.13; primary bucket kegg:ppu00910)
- gltB: PP_5076 | Q88CV4 | Glutamate synthase [NADPH] large chain (EC 1.4.1.13) (Glutamate synthase subunit alpha) (EC 1.4.1.13; primary bucket kegg:ppu00910)
- spuB: PP_5183 | Q88CJ7 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- spuI: PP_5184 | Q88CJ6 | Glutamylpolyamine synthetase (primary bucket kegg:ppu00910)
- puuA-II: PP_5299 | Q88C84 | Glutamate-putrescine ligase (EC 6.3.1.11) (EC 6.3.1.11; primary bucket kegg:ppu00910)

## Generic Module Context

### Working Scope

A reusable bacterial module for importing nitrate and reducing it through nitrite to ammonium for biosynthesis. A nitrate/nitrite porter supplies the intracellular nitrate pool, an assimilatory molybdoenzyme reduces nitrate to nitrite, and a siroheme-containing NirBD complex performs the six-electron reduction of nitrite to ammonium. The module stops at ammonium; incorporation through GS-GOGAT is represented by the separate bacterial ammonia assimilation module. Respiratory nitrate reduction, denitrification, and dissimilatory nitrate reduction to ammonium are outside this boundary.

### Provisional Biological Outline

- Bacterial assimilatory nitrate uptake and reduction
  - 1. nitrate import
  - Nitrate import by a nitrate/nitrite porter
    - Alternative versions by transporter architecture: Nitrate import system
      - Nitrate/nitrite porter
        - Nitrate transmembrane transporter activity (molecular player: bacterial nitrate/nitrite porter family; activity or role: nitrate transmembrane transporter activity)
      - NrtABCD ABC-type nitrate importer
        - ABC-type nitrate import (molecular player: cyanobacterial NrtABCD nitrate transporter; activity or role: nitrate transmembrane transporter activity)
  - 2. nitrate reduction to nitrite
  - Assimilatory NAD(P)H-dependent nitrate reduction
    - Alternative versions by electron-input architecture: Assimilatory nitrate reductase implementation
      - Fused molybdoenzyme and pyridine-nucleotide reductase
        - Fused assimilatory nitrate reductase activity (molecular player: fused diflavin assimilatory nitrate reductase family; activity or role: nitrate reductase [NAD(P)H] activity)
      - Split NasBC nitrate reductase
        - Split assimilatory nitrate reductase activity (molecular player: split bacterial NasBC assimilatory nitrate reductase; activity or role: nitrate reductase [NAD(P)H] activity)
      - Ferredoxin-linked NarB nitrate reductase
        - Ferredoxin-nitrate reductase activity (molecular player: ferredoxin-linked bacterial NarB nitrate-reductase family; activity or role: ferredoxin-nitrate reductase activity)
  - 3. nitrite reduction to ammonium
  - NirBD-dependent assimilatory nitrite reduction
    - NirBD nitrite reductase activity (molecular player: bacterial NirBD assimilatory nitrite reductase complex; activity or role: nitrite reductase [NAD(P)H] activity)

### Known Relationships Among Steps

- Nitrate import by a nitrate/nitrite porter feeds into Assimilatory NAD(P)H-dependent nitrate reduction: Imported nitrate is the substrate of assimilatory nitrate reductase.
- Assimilatory NAD(P)H-dependent nitrate reduction feeds into NirBD-dependent assimilatory nitrite reduction: Nitrate reductase supplies nitrite to the NirBD complex.

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

# Module/Pathway/Taxon Review: Bacterial Assimilatory Nitrate Uptake and Reduction in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** kegg:ppu00910 "Nitrogen metabolism" (module area: energy/respiration/inorganic metabolism)
**Generic module:** Bacterial assimilatory nitrate uptake and reduction (nitrate → nitrite → ammonium, stopping at ammonium)

---

## 1. Executive Summary

The bacterial assimilatory nitrate module is **satisfiable in all three steps** in *P. putida* KT2440. Nitrate import is provided by the nitrate/nitrite porter **NasA (PP_2092, K02575)**, nitrate-to-nitrite reduction is carried out by a fused molybdoenzyme/diflavin assimilatory nitrate reductase **PP_1703 (Q88M71, NasB)**, and the six-electron reduction of nitrite to ammonium is performed by the **NirBD complex (nirB/PP_1705 + nirD/PP_1706)**. The pathway is genomically organized into two loci: a `nasA–nasT–nasS` transporter/regulator cluster (PP_2092/PP_2093/PP_2094) and a `PP_1703–nirB–nirD` reductase cluster, consistent with the classic observation that nitrate-assimilation genes in this lineage are not fully clustered.

The single most important curation finding is that **the actual assimilatory nitrate reductase, PP_1703, is missing from the 20-gene candidate list and is triple-misannotated**. KEGG assigns it K00380 (sulfite reductase flavoprotein), a UniProt ARBA rule over-propagates a periplasmic NapAB (dissimilatory) function, and residual keywords hint at periplasmic localization. All three annotations are refuted here by domain architecture (Mo-bis(molybdopterin guanine dinucleotide) + FAD/FMN diaphorase, not a CysJ flavoprotein), by the absence of any Sec/Tat signal peptide (cytoplasmic, not periplasmic), and by genomic context (immediately upstream of nirBD, not part of a nap/nar operon). Because of this misannotation, **automated KEGG module scoring falsely reports the assimilatory module as a gap in ppu**: KEGG's module M00531 requires KOs that are all absent, and KEGG additionally files NirBD under the *dissimilatory* DNRA module M00530 rather than assimilation. The blocker is annotation and database definition, **not biology**.

The remaining 16 of 20 candidate genes are **out of scope** — they belong to GS-GOGAT ammonia assimilation (eight glutamine synthetases, glutamate synthase, glutamate dehydrogenases) and other nitrogen metabolism (carbonic anhydrases, carbamate kinase, nitronate monooxygenases), which the module definition explicitly excludes ("the module stops at ammonium"). KT2440 encodes **no true dissimilatory or denitrification machinery** (no narGHI, napAB, nirK/nirS, nrfA), so the assimilatory module boundary is clean and there is no risk of confusing assimilatory and respiratory routes in this organism. The headline curation actions are: (1) **add and promote PP_1703** to full gene review and correct its annotation; (2) mark all three module steps **covered**; (3) **prune the 16 out-of-scope candidates** from this bucket; and (4) **override automated KEGG scoring** for this taxon.

---

## 2. Target-Organism Pathway Definition

**Included process.** The module covers cytoplasmic assimilatory nitrate metabolism for biosynthesis: (i) uptake of extracellular nitrate (and nitrite) across the inner membrane by a nitrate/nitrite porter; (ii) reduction of nitrate to nitrite by an NAD(P)H-dependent, molybdenum-cofactor assimilatory nitrate reductase; and (iii) the six-electron reduction of nitrite to ammonium by a siroheme/[4Fe-4S] NADH-dependent nitrite reductase (NirBD). The module terminates at ammonium.

**Neighboring pathways to keep separate.**
- **GS-GOGAT ammonia assimilation** (glutamine synthetase, glutamate synthase, glutamate dehydrogenase). This is a *separate* module. Eight of the candidate genes are glutamine synthetases and four more are glutamate synthase/dehydrogenase — all belong here, not in the nitrate module.
- **Respiratory nitrate reduction / denitrification** (NarGHI, NapAB, NirK/NirS, Nor, Nos). Absent in KT2440; must never be mapped into the assimilatory module.
- **Dissimilatory nitrate reduction to ammonium (DNRA)** (periplasmic NapAB + NrfA). KT2440 lacks NrfA. Note: KEGG idiosyncratically files the *assimilatory* NirBD under its DNRA module M00530, which is a database-definition divergence, not biology.
- **Sulfur assimilation / sulfite reduction** (CysJI, CysH). KT2440 encodes a dedicated system (cysI/PP_2371, PP_0860, cysH/PP_2328); the sulfite-reductase KEGG annotation on PP_1703 is a spurious KO assignment, not a real CysJ.

**Alternate names / database-specific definitions.**
- KEGG map: **ppu00910 "Nitrogen metabolism"** (broad overview bucket).
- KEGG modules: **M00531** "Assimilatory nitrate reduction, nitrate → ammonia"; **M00530** "Dissimilatory nitrate reduction, nitrate → ammonia."
- The assimilatory nitrate reductase in *Pseudomonas* is historically called **NasB** (in *P. aeruginosa* and *P. putida* genetics), whereas the porter is **NasA** and the sensor/antiterminator regulators are **NasS/NasT**.

---

## 3. Expected Step Model

```
                 nitrate (extracellular)
                         |
        [Step 1: nitrate import]
        NasA / PP_2092  (K02575, NNP/MFS nitrate-nitrite porter)
        regulated by NasT/PP_2093 + NasS/PP_2094
                         |
                 nitrate (cytoplasmic)
                         |
        [Step 2: nitrate -> nitrite]
        PP_1703 / Q88M71 (NasB)
        fused Mo-bisMGD + [4Fe-4S] + FAD/FMN NAD(P)H diaphorase
        (MISSING from candidate list; mis-annotated K00380)
                         |
                      nitrite
                         |
        [Step 3: nitrite -> ammonium]
        NirBD:  nirB/PP_1705 (K00362, siroheme+[4Fe-4S], large subunit)
              + nirD/PP_1706 (K00363, small subunit)
                         |
                     ammonium  --->  (handoff to GS-GOGAT module; out of scope)
```

| Step | Expected activity | KT2440 gene(s) | KO | Status |
|------|-------------------|----------------|-----|--------|
| 1. Nitrate import | Nitrate/nitrite transmembrane transporter | **PP_2092** (nasA) | K02575 | **Covered** |
| 2. Nitrate → nitrite | Assimilatory NAD(P)H nitrate reductase (fused Mo/diflavin) | **PP_1703** (nasB) | mis-KO'd K00380 → should be assimilatory NR | **Covered (annotation gap)** |
| 3. Nitrite → ammonium | Assimilatory NADH nitrite reductase (siroheme) | **PP_1705** (nirB) + **PP_1706** (nirD) | K00362 + K00363 | **Covered** |

The generic module offers alternative architectures for step 2 (fused diflavin NasB vs. split NasBC vs. ferredoxin NarB). KT2440 uses the **fused diflavin NasB** implementation. For step 1 it offers NNP porter vs. NrtABCD ABC importer; KT2440 uses the **NNP porter** (no NrtABCD KOs present).

---

## 4. Candidate Genes and Evidence

### 4.1 In-scope, high-confidence genes

**PP_2092 — nasA — Nitrate/nitrite transporter (K02575).** UniProt Q88L43, 411 aa, MFS/NNP-family porter with UniProt keyword "Nitrate assimilation," predicted inner-membrane transmembrane transporter. It is the **sole nitrate porter** in the genome — no second NNP/NarK porter (K02598) and no NrtABCD ABC importer (K15576–K15579) exist. It is flanked by NasT (PP_2093, K07183, ANTAR-domain response-regulator/antiterminator) and NasS (PP_2094, K22067, nitrate/nitrite-binding sensor), forming an intact nitrate-sensing regulon. *Curation note:* clean, high-confidence. Evidence type: sequence/family + genomic context + regulon synteny.

**PP_1703 — nasB — Assimilatory nitrate reductase (currently mis-KO'd K00380).** UniProt Q88M71, 1341 aa. Domain content: Pfam PF00384 (Molybdopterin) + PF04879 (Molybdop_Fe4S4) + PF01568 (Molybdopterin dinucleotide-binding), plus PF00667 (FAD_binding_1) and PF00258 (Flavodoxin_1). Cofactors: FAD, FMN, Mo-bis(molybdopterin guanine dinucleotide), [4Fe-4S]. UniProt places it in the "oxidoreductase family, NasA/NapA/NarB subfamily" (InterPro "CT_Nitrate-R-NapA-like"). It lies in an operon immediately upstream of nirB (PP_1705) and nirD (PP_1706). *This gene is absent from the 20-candidate list and must be added.* Evidence type: domain architecture + genomic context + lineage genetics (KT2442 nasB, PMID 10852866). **Promote to full review.**

**PP_1705 — nirB — Nitrite reductase [NAD(P)H] large subunit (K00362, EC 1.7.1.15).** UniProt Q88M69 with confirmed siroheme and [4Fe-4S] binding-site annotations (residues ~646/652/686/690). Carries the catalytic six-electron reduction of nitrite to ammonium. No competing NO-forming (nirK/nirS) or DNRA (nrfA) nitrite reductase exists, so NirBD is the **sole nitrite-reduction route**. High-confidence. Evidence type: sequence + cofactor sites + absence of alternatives + functional data in *P. putida* Y-9.

**PP_1706 — nirD — Nitrite reductase small subunit (K00363).** UniProt Q88M68. Partner subunit of NirB. High-confidence.

### 4.2 Out-of-scope candidates (belong to GS-GOGAT or other N-metabolism)

| Gene | Locus | KO | Assignment | Correct home |
|------|-------|-----|-----------|--------------|
| glnA | PP_5046 | K01915 | Glutamine synthetase | Ammonia assimilation |
| PP_3148 | PP_3148 | K01915 | Glutamine synthetase | Ammonia assimilation |
| PP_4399 | PP_4399 | K01915 | Glutamine synthetase | Ammonia assimilation |
| PP_4547 | PP_4547 | K01915 | Glutamine synthetase | Ammonia assimilation |
| puuA-I | PP_2178 | K01915 | Glutamate-putrescine ligase | Polyamine/GS family |
| puuA-II | PP_5299 | K01915 | Glutamate-putrescine ligase | Polyamine/GS family |
| spuB | PP_5183 | K01915 | Glutamylpolyamine synthetase | Polyamine metabolism |
| spuI | PP_5184 | K01915 | Glutamylpolyamine synthetase | Polyamine metabolism |
| gltB | PP_5076 | K00265 | Glutamate synthase large chain | GS-GOGAT |
| gltD | PP_5075 | K00266 | Glutamate synthase small chain | GS-GOGAT |
| gdhA | PP_0675 | K00262 | Glutamate dehydrogenase | GS-GOGAT-adjacent |
| gdhB | PP_2080 | K15371 | NAD-glutamate dehydrogenase | Glutamate catabolism (ppu00430) |
| cynT | PP_0100 | K01673 | Carbonic anhydrase | Other |
| PP_3392 | PP_3392 | K28956 | γ-carbonic anhydrase | Other |
| arcC | PP_0999 | K00926 | Carbamate kinase | Arginine/urea |
| yrpB | PP_3827 | K00459 | Nitronate monooxygenase | Nitroalkane detox |
| PP_0430 | PP_0430 | K00459 | Nitronate monooxygenase (uncharacterized) | Nitroalkane detox |

These loci are correctly part of KEGG ppu00910 "Nitrogen metabolism" as a broad overview map, but **do not belong to the assimilatory nitrate module**, whose scope explicitly ends at ammonium. `gltB` (PP_5076) is notable: although out-of-scope for the module, it is functionally coupled — inactivation of gltB abolishes nasB expression in KT2442 (PMID 10852866), evidencing a regulatory link between GOGAT and nitrate assimilation.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**5.1 The missing reductase (the central gap).** Step 2 has no representative in the candidate list. The true enzyme, PP_1703, is present in the genome and functional in the lineage but was omitted because it is not KO-mapped to any nitrate-reductase KO. This is a **metadata gap, not a biological gap**. Whole-genome scan: the canonical assimilatory nitrate reductase KOs K00372/K00360 are **absent**; K00367 (ferredoxin-nitrate reductase, narB) is **absent**. PP_1703 is the fused NasB implementation and must be recognized manually.

**5.2 Triple mis-annotation of PP_1703 — all refuted.**
- **KEGG K00380 (sulfite reductase flavoprotein alpha, CysJ).** Refuted: PP_1703 carries a molybdenum cofactor, which CysJ never has; and KT2440 has an independent, complete sulfite-reduction system (cysI/PP_2371 siroheme hemoprotein, PP_0860 flavoprotein, cysH/PP_2328 APS reductase), so PP_1703 is not required for sulfur assimilation.
- **UniProt ARBA "periplasmic assimilatory/dissimilatory NapAB."** Refuted: PP_1703 has **no Sec or Tat signal peptide** (no FT SIGNAL, no FT TRANSIT, no subcellular-location feature). Periplasmic NapA is Tat-exported and ~750–830 aa with no fused flavin domain; PP_1703 is 1341 aa with a C-terminal FAD/flavodoxin NAD(P)H diaphorase (residues ~819–957 and ~981–1191) and an N-terminal molybdoenzyme [4Fe-4S] motif (CPYCGVGCG). It is a **cytoplasmic fused NasB**, not periplasmic NapA. Confirming this, napA/napB (K02567/K02568) and narGHI are entirely absent from the ppu genome.
- **Residual periplasmic/localization keywords.** Refuted by the same absence of any export signal.

**5.3 KEGG module-definition divergence.** KEGG module M00531 DEFINITION = `(K00367,K10534,(K00372-K00360)) (K00366,K17877,(K26139+K26138),K00361)`. **None** of these KOs is assigned to any ppu gene, so KEGG lists M00531 as *not present* in ppu. Two problems: (i) PP_1703 is mis-KO'd away from any of these; (ii) the nitrite branch of M00531 demands a ferredoxin/NirA-type reductase (K00366 etc.), whereas KT2440's real nitrite reductase is **NirBD (K00362+K00363)**, which KEGG places in the *dissimilatory* module M00530 (DNRA). Automated module scoring therefore **falsely flags a gap**. Manual override is required.

**5.4 Decoy transporter.** PP_0208 (Q88RC4) is annotated "Nitrate ABC transporter permease" but sits in operon PP_0207 (K15553) – PP_0208 (K15554) – PP_0209 tauB-I (K15555): this is the **ssuABC/tauABC aliphatic-sulfonate ABC transporter** family (with a nearby sulfonate-binding protein and ferredoxin), **not** a nitrate importer. Do not count it toward step 1.

**5.5 Paralog / broad-mapping ambiguities.** Eight loci collapse onto K01915 (glutamine synthetase); this broad GS mapping is a classic source of over-propagation into "nitrogen metabolism" buckets. Two loci (yrpB, PP_0430) share K00459 (nitronate monooxygenase). None affects the nitrate module, but curators should not let the sheer count of GS/other-N genes obscure the fact that only 3 (now 4 with PP_1703) candidates are truly in-scope.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Basis |
|-------------|--------------------|-------|
| 1. Nitrate import (NNP porter) | **covered** | PP_2092 nasA (K02575), sole porter, NasST-regulated |
| 2. Nitrate → nitrite (fused NasB) | **covered** — requires metadata fix | PP_1703 present & functional; add to bucket, correct KO/annotation |
| 3. Nitrite → ammonium (NirBD) | **covered** | PP_1705 nirB (K00362) + PP_1706 nirD (K00363) |
| Alt: NrtABCD ABC importer | **not_expected_in_target_taxon** | No K15576–K15579 in genome |
| Alt: ferredoxin NarB reductase | **not_expected_in_target_taxon** | No K00367 |
| Respiratory/denitrification neighbors | **not_expected_in_target_taxon** | No narGHI, napAB, nirK/nirS, nrfA |

**Module-level actions.**
1. **Add PP_1703 (Q88M71) to the kegg:ppu00910 assimilatory-nitrate bucket** as the step-2 enzyme (NasB). This is the single most important edit.
2. Mark the whole module **satisfiable / covered (3/3)** for KT2440, with an explicit note that automated KEGG M00531 scoring must be **overridden** because (a) PP_1703 is mis-KO'd to K00380 and (b) KEGG maps the organism's actual nitrite reductase NirBD into the dissimilatory M00530.
3. **Prune the 16 out-of-scope candidates** from the assimilatory-nitrate module (retain them under the broader ppu00910 overview / ammonia-assimilation module as appropriate).
4. Flag **PP_0208** as a mislabeled sulfonate transporter (annotation-correction candidate), not a nitrate importer.
5. Generic module boundaries are **correct** for this organism (the module rightly stops at ammonium and excludes GS-GOGAT). No boundary revision is needed; the issue is entirely KT2440 metadata mapping — status **module_needs_revision** applies only to the *local KO/candidate metadata*, not to the generic module document.

**GO-curation notes.** PP_1703 should carry GO:0008940 (nitrate reductase activity) / GO:0042126 (nitrate metabolic process) / GO:0042128 (nitrate assimilation) and a **cytoplasm** localization (GO:0005737) rather than periplasm. Its erroneous sulfite-reductase and periplasmic-NapAB associations should be removed. No new GO term requests appear necessary — existing terms for assimilatory nitrate reductase, NADH nitrite reductase, and nitrate transmembrane transporter cover all three steps.

---

## 7. Genes to Promote to Full Review

| Gene | Locus | UniProt | Why promote |
|------|-------|---------|-------------|
| **PP_1703 (nasB)** | PP_1703 | Q88M71 | **Highest priority.** Missing from candidate list; triple mis-annotated; is the true step-2 assimilatory nitrate reductase. Full `fetch-gene` review to correct KO (away from K00380), remove periplasmic NapAB propagation, set cytoplasmic localization, and register as NasB. |
| PP_2092 (nasA) | PP_2092 | Q88L43 | Confirm as sole nitrate porter; document NasST regulon linkage (PP_2093/PP_2094). |
| PP_1705 (nirB) | PP_1705 | Q88M69 | Confirm siroheme/[4Fe-4S] assimilatory nitrite reductase; ensure it is not mis-filed as dissimilatory DNRA. |
| PP_1706 (nirD) | PP_1706 | Q88M68 | Partner subunit; confirm assimilatory role. |
| PP_0208 | PP_0208 | Q88RC4 | Annotation correction: reassign from "nitrate ABC transporter" to ssuABC/tauABC sulfonate transporter. |

---

## 8. Evidence and Open Questions

**Direct experimental support (target lineage).** The strongest species-level evidence is genetic: a transposon insertion mapping to the **assimilatory nitrate reductase gene nasB** in the near-isogenic strain **KT2442** ([PMID: 10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/)). That study's own words — *"is demonstrated to bear the transposon within the assimilatory nitrate reductase gene (nasB) of P. putida KT2442"* and *"Genetic evidence as well as sequence analyses of the DNA regions flanking nasB suggest that the genes required for nitrate assimilation are not clustered"* — provide direct proof that the KT2440 lineage encodes a functional assimilatory nitrate reductase and explain why the porter (PP_2092) and reductase (PP_1703) loci are genomically separate. KT2442 is essentially isogenic to KT2440 (a restriction-modification variant), so transfer of this conclusion to KT2440 is **strong**.

**Cross-strain / cross-species support (moderate transfer).** NirBD's assimilatory nitrite-to-ammonium role is functionally demonstrated in *P. putida* **Y-9**, where *"The nirBD that encodes nitrite reductase had an important role in strain growth and ammonium production"* ([PMID: 32506044](https://pubmed.ncbi.nlm.nih.gov/32506044/); see also [PMID: 41980646](https://pubmed.ncbi.nlm.nih.gov/41980646/)). Because Y-9 is a different *P. putida* strain that also runs DNRA/denitrification, transfer of the *assimilatory* interpretation to KT2440 is **moderate**; however, KT2440 lacks the dissimilatory machinery, so in KT2440 NirBD can only be assimilatory. The genetic distinctness of assimilatory (nas) and dissimilatory (nar) nitrate reductases in the genus is established in *P. aeruginosa* ([PMID: 6775047](https://pubmed.ncbi.nlm.nih.gov/6775047/)) — **weak-to-moderate** transfer, useful for the general principle that Nas ≠ Nar and that both require molybdenum.

**Inferred from homology / database evidence.** The domain architecture of PP_1703 (Mo-bisMGD + [4Fe-4S] + FAD/FMN diaphorase), the absence of a signal peptide, the KO assignments of PP_2092/PP_1705/PP_1706, the NasST regulon, and the absence of all dissimilatory/denitrification and ABC-importer KOs derive from UniProt/KEGG/Pfam/InterPro annotations and whole-genome KO scans. These are **homology/sequence inferences**, strong for family assignment but not a substitute for direct enzymology in KT2440 itself.

**Open questions / resolving experiments.**
1. **Direct enzymology on PP_1703:** heterologous expression and NAD(P)H:nitrate reductase assay to confirm activity and cofactor complement; would definitively retire the sulfite-reductase and NapAB misannotations.
2. **Subcellular fractionation** of PP_1703 to confirm cytoplasmic localization (the signal-peptide analysis predicts cytoplasm).
3. **Growth phenotyping of KT2440 (not KT2442)** on nitrate as sole N source, with ΔPP_1703, ΔPP_2092, and ΔnirBD knockouts, to confirm each step's necessity in the exact target strain.
4. **RT-PCR / RNA-seq** to verify the PP_1703–nirB–nirD operon and NasST-dependent, nitrate-inducible expression.
5. **Expert/database question:** should KEGG's placement of NirBD in the dissimilatory module M00530 be flagged for taxa (like KT2440) that lack DNRA machinery, so automated scoring stops mis-assigning it?

---

## 9. Key References

| PMID | Title (abbrev.) | Relevance |
|------|-----------------|-----------|
| [10852866](https://pubmed.ncbi.nlm.nih.gov/10852866/) | *Inactivation of gltB abolishes expression of the assimilatory nitrate reductase gene (nasB) in P. putida KT2442* | Direct genetic evidence for assimilatory nitrate reductase **nasB** in the KT2440 lineage; shows nas genes are not fully clustered and links GOGAT to nasB expression. |
| [32506044](https://pubmed.ncbi.nlm.nih.gov/32506044/) | *Nitrate assimilation, DNRA, and denitrification coexist in P. putida Y-9 under aerobic conditions* | Functional evidence that **NirBD** reduces nitrite to ammonium and supports growth/ammonium production. |
| [41980646](https://pubmed.ncbi.nlm.nih.gov/41980646/) | *The nirB and nirD genes are essential for reduction of nitrite in P. putida Y-9 under aerobic conditions* | Confirms NirBD requirement for nitrite reduction (assimilatory and dissimilatory) under aerobic conditions. |
| [6775047](https://pubmed.ncbi.nlm.nih.gov/6775047/) | *The assimilatory and dissimilatory nitrate reductases of P. aeruginosa are encoded by different genes* | Establishes that Nas (assimilatory) and Nar (dissimilatory) reductases are genetically separate in *Pseudomonas*; both require molybdenum. |

---

### Summary verdict

**Assimilatory nitrate module = SATISFIABLE (3/3) in *P. putida* KT2440.** Import = PP_2092 (nasA), reduction = PP_1703 (nasB, must be added and corrected), nitrite reduction = PP_1705/PP_1706 (nirBD). The only obstacles are (1) PP_1703's omission and triple misannotation and (2) KEGG's module definitions — both curation/metadata problems, not biological gaps. No dissimilatory or denitrification machinery exists, so the module boundary is clean and requires no revision.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_assimilatory_nitrate_reduction__ppu00910-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_assimilatory_nitrate_reduction__ppu00910-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10852866
2. PMID:32506044
3. PMID:41980646
4. PMID:6775047