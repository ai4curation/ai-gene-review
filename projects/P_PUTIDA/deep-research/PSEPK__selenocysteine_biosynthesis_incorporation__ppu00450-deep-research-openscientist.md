---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:30:40.858437'
end_time: '2026-09-01T10:48:16.922873'
duration_seconds: 1056.06
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial and eukaryotic selenocysteine biosynthesis and co-translational
    incorporation
  module_summary: A reusable module for the bacterial and eukaryotic synthesis of
    selenocysteyl-tRNA(Sec) and recoding of UGA as selenocysteine. Selenophosphate
    synthetase activates selenium, and seryl-tRNA synthetase charges tRNA(Sec) with
    serine. Bacteria convert Ser-tRNA(Sec) directly with SelA, whereas the represented
    eukaryotic route first phosphorylates it with PSTK and then uses SepSecS. The
    completed Sec-tRNA(Sec) is delivered by a lineage-specific elongation system to
    a UGA codon in a SECIS-dependent translation context.
  module_outline: "- Bacterial and eukaryotic selenocysteine biosynthesis and incorporation\n\
    \  - 1. activated selenium donor production\n  - Selenophosphate synthesis\n \
    \   - SelD/SEPHS2 selenide, water dikinase activity (molecular player: selenophosphate\
    \ synthetase family; activity or role: selenide, water dikinase activity)\n  -\
    \ 2. tRNA(Sec) aminoacylation with serine\n  - Ser-tRNA(Sec) synthesis\n    -\
    \ SerS/SARS serine-tRNA ligase activity on tRNA(Sec) (molecular player: seryl-tRNA\
    \ synthetase family; activity or role: serine-tRNA ligase activity)\n  - 3. conversion\
    \ of Ser-tRNA(Sec) to Sec-tRNA(Sec)\n  - Alternative Sec-tRNA(Sec) synthesis routes\n\
    \    - Alternative versions by taxonomic implementation: Ser-tRNA(Sec) conversion\
    \ route\n      - Bacterial SelA route\n        - SelA L-seryl-tRNA(Sec) selenium\
    \ transferase activity (molecular player: bacterial SelA family; activity or role:\
    \ L-seryl-tRNA(Sec) selenium transferase activity)\n      - Eukaryotic PSTK-SepSecS\
    \ route\n        - 1. Ser-tRNA(Sec) phosphorylation\n        - PSTK-dependent\
    \ phosphoseryl-tRNA(Sec) formation\n          - PSTK L-seryl-tRNA(Sec) kinase\
    \ activity (molecular player: PSTK family; activity or role: L-seryl-tRNA(Sec)\
    \ kinase activity)\n        - 2. phosphoseryl-tRNA(Sec) selenium transfer\n  \
    \      - SepSecS-dependent Sec-tRNA(Sec) formation\n          - SepSecS phosphoseryl-tRNA(Sec)\
    \ selenium transferase activity (molecular player: SepSecS family; activity or\
    \ role: O-phosphoseryl-tRNA(Sec) selenium transferase activity)\n  - 4. SECIS-dependent\
    \ UGA recoding and Sec-tRNA delivery\n  - Alternative selenocysteine insertion\
    \ systems\n    - Alternative versions by taxonomic implementation: Selenocysteine-specific\
    \ translation machinery\n      - Bacterial SelB insertion system\n        - SelB\
    \ bacterial SECIS-binding activity (molecular player: SelB elongation-factor family;\
    \ activity or role: selenocysteine insertion sequence binding)\n        - SelB\
    \ selenocysteine-specific elongation factor activity (molecular player: SelB elongation-factor\
    \ family; activity or role: translation elongation factor activity)\n      - Eukaryotic\
    \ SECISBP2-EEFSEC insertion system\n        - 1. SECIS-element recognition\n \
    \       - SECISBP2-dependent SECIS recognition\n          - SECISBP2 SECIS-binding\
    \ activity (molecular player: SECISBP2 family; activity or role: selenocysteine\
    \ insertion sequence binding)\n        - 2. Sec-tRNA(Sec) delivery\n        -\
    \ EEFSEC-dependent Sec-tRNA(Sec) delivery\n          - EEFSEC translation elongation\
    \ factor activity (molecular player: selenocysteine-specific elongation-factor\
    \ family; activity or role: translation elongation factor activity)"
  module_connections: '- Selenophosphate synthesis feeds into Alternative Sec-tRNA(Sec)
    synthesis routes: Selenophosphate supplies selenium to either Sec-tRNA synthesis
    route.

    - Ser-tRNA(Sec) synthesis feeds into Alternative Sec-tRNA(Sec) synthesis routes:
    SerS supplies Ser-tRNA(Sec) to either conversion route.

    - Alternative Sec-tRNA(Sec) synthesis routes feeds into Alternative selenocysteine
    insertion systems: Completed Sec-tRNA(Sec) is the substrate delivered during UGA
    recoding.

    - PSTK-dependent phosphoseryl-tRNA(Sec) formation feeds into SepSecS-dependent
    Sec-tRNA(Sec) formation: PSTK produces the phosphoseryl-tRNA consumed by SepSecS.

    - SECISBP2-dependent SECIS recognition feeds into EEFSEC-dependent Sec-tRNA(Sec)
    delivery: SECISBP2-dependent mRNP assembly supplies the recoding context used
    during EEFSEC delivery.'
  pathway_query: ppu00450
  pathway_id: ppu00450
  pathway_name: Selenocompound metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00450 with 9 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '12'
  candidate_genes: '- selA: PP_0493 | Q88QJ8 | L-seryl-tRNA(Sec) selenium transferase
    (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec)
    synthase) (EC 2.9.1.1; primary bucket kegg:ppu00450)

    - metB: PP_0659 | Q88Q39 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - selD: PP_0823 | P59392 | Selenide, water dikinase (EC 2.7.9.3) (Selenium donor
    protein) (Selenophosphate synthase) (EC 2.7.9.3; primary bucket kegg:ppu00450)

    - metG: PP_1097 | Q88NV7 | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA
    synthetase) (MetRS) (EC 6.1.1.10; primary bucket kegg:ppu00450)

    - cysD: PP_1303 | Q88NA9 | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4)
    (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4;
    primary bucket kegg:ppu00261)

    - cysNC: PP_1304 | Q88NA8 | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4)
    (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4;
    primary bucket kegg:ppu00261)

    - mdeA: PP_1308 | Q88NA4 | L-methionine gamma-lyase (EC 4.4.1.11) (EC 4.4.1.11;
    primary bucket kegg:ppu00450)

    - metH: PP_2375 | Q88KB5 | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine
    methyltransferase) (EC 2.1.1.13; primary bucket kegg:ppu04980)

    - metE: PP_2698 | Q88JF1 | 5-methyltetrahydropteroyltriglutamate-homocysteine
    methyltransferase (primary bucket kegg:ppu00450)

    - PP_4348: PP_4348 | Q88EV4 | Cystathionine beta-lyase (primary bucket kegg:ppu00450)

    - PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)

    - PP_4637: PP_4637 | Q88E31 | 5-methyltetrahydropteroyltriglutamate-homocysteine
    S-methyltransferase family protein (primary bucket kegg:ppu00450)'
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
  path: PSEPK__selenocysteine_biosynthesis_incorporation__ppu00450-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__selenocysteine_biosynthesis_incorporation__ppu00450-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial and eukaryotic selenocysteine biosynthesis and co-translational incorporation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00450
- Resolved ID: ppu00450
- Resolved name: Selenocompound metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00450 with 9 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 12

- selA: PP_0493 | Q88QJ8 | L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec) synthase) (EC 2.9.1.1; primary bucket kegg:ppu00450)
- metB: PP_0659 | Q88Q39 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- selD: PP_0823 | P59392 | Selenide, water dikinase (EC 2.7.9.3) (Selenium donor protein) (Selenophosphate synthase) (EC 2.7.9.3; primary bucket kegg:ppu00450)
- metG: PP_1097 | Q88NV7 | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA synthetase) (MetRS) (EC 6.1.1.10; primary bucket kegg:ppu00450)
- cysD: PP_1303 | Q88NA9 | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4; primary bucket kegg:ppu00261)
- cysNC: PP_1304 | Q88NA8 | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) (EC 2.7.7.4; primary bucket kegg:ppu00261)
- mdeA: PP_1308 | Q88NA4 | L-methionine gamma-lyase (EC 4.4.1.11) (EC 4.4.1.11; primary bucket kegg:ppu00450)
- metH: PP_2375 | Q88KB5 | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) (EC 2.1.1.13; primary bucket kegg:ppu04980)
- metE: PP_2698 | Q88JF1 | 5-methyltetrahydropteroyltriglutamate-homocysteine methyltransferase (primary bucket kegg:ppu00450)
- PP_4348: PP_4348 | Q88EV4 | Cystathionine beta-lyase (primary bucket kegg:ppu00450)
- PP_4594: PP_4594 | Q88E72 | Cystathionine gamma-synthase (primary bucket kegg:ppu00450)
- PP_4637: PP_4637 | Q88E31 | 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase family protein (primary bucket kegg:ppu00450)

## Generic Module Context

### Working Scope

A reusable module for the bacterial and eukaryotic synthesis of selenocysteyl-tRNA(Sec) and recoding of UGA as selenocysteine. Selenophosphate synthetase activates selenium, and seryl-tRNA synthetase charges tRNA(Sec) with serine. Bacteria convert Ser-tRNA(Sec) directly with SelA, whereas the represented eukaryotic route first phosphorylates it with PSTK and then uses SepSecS. The completed Sec-tRNA(Sec) is delivered by a lineage-specific elongation system to a UGA codon in a SECIS-dependent translation context.

### Provisional Biological Outline

- Bacterial and eukaryotic selenocysteine biosynthesis and incorporation
  - 1. activated selenium donor production
  - Selenophosphate synthesis
    - SelD/SEPHS2 selenide, water dikinase activity (molecular player: selenophosphate synthetase family; activity or role: selenide, water dikinase activity)
  - 2. tRNA(Sec) aminoacylation with serine
  - Ser-tRNA(Sec) synthesis
    - SerS/SARS serine-tRNA ligase activity on tRNA(Sec) (molecular player: seryl-tRNA synthetase family; activity or role: serine-tRNA ligase activity)
  - 3. conversion of Ser-tRNA(Sec) to Sec-tRNA(Sec)
  - Alternative Sec-tRNA(Sec) synthesis routes
    - Alternative versions by taxonomic implementation: Ser-tRNA(Sec) conversion route
      - Bacterial SelA route
        - SelA L-seryl-tRNA(Sec) selenium transferase activity (molecular player: bacterial SelA family; activity or role: L-seryl-tRNA(Sec) selenium transferase activity)
      - Eukaryotic PSTK-SepSecS route
        - 1. Ser-tRNA(Sec) phosphorylation
        - PSTK-dependent phosphoseryl-tRNA(Sec) formation
          - PSTK L-seryl-tRNA(Sec) kinase activity (molecular player: PSTK family; activity or role: L-seryl-tRNA(Sec) kinase activity)
        - 2. phosphoseryl-tRNA(Sec) selenium transfer
        - SepSecS-dependent Sec-tRNA(Sec) formation
          - SepSecS phosphoseryl-tRNA(Sec) selenium transferase activity (molecular player: SepSecS family; activity or role: O-phosphoseryl-tRNA(Sec) selenium transferase activity)
  - 4. SECIS-dependent UGA recoding and Sec-tRNA delivery
  - Alternative selenocysteine insertion systems
    - Alternative versions by taxonomic implementation: Selenocysteine-specific translation machinery
      - Bacterial SelB insertion system
        - SelB bacterial SECIS-binding activity (molecular player: SelB elongation-factor family; activity or role: selenocysteine insertion sequence binding)
        - SelB selenocysteine-specific elongation factor activity (molecular player: SelB elongation-factor family; activity or role: translation elongation factor activity)
      - Eukaryotic SECISBP2-EEFSEC insertion system
        - 1. SECIS-element recognition
        - SECISBP2-dependent SECIS recognition
          - SECISBP2 SECIS-binding activity (molecular player: SECISBP2 family; activity or role: selenocysteine insertion sequence binding)
        - 2. Sec-tRNA(Sec) delivery
        - EEFSEC-dependent Sec-tRNA(Sec) delivery
          - EEFSEC translation elongation factor activity (molecular player: selenocysteine-specific elongation-factor family; activity or role: translation elongation factor activity)

### Known Relationships Among Steps

- Selenophosphate synthesis feeds into Alternative Sec-tRNA(Sec) synthesis routes: Selenophosphate supplies selenium to either Sec-tRNA synthesis route.
- Ser-tRNA(Sec) synthesis feeds into Alternative Sec-tRNA(Sec) synthesis routes: SerS supplies Ser-tRNA(Sec) to either conversion route.
- Alternative Sec-tRNA(Sec) synthesis routes feeds into Alternative selenocysteine insertion systems: Completed Sec-tRNA(Sec) is the substrate delivered during UGA recoding.
- PSTK-dependent phosphoseryl-tRNA(Sec) formation feeds into SepSecS-dependent Sec-tRNA(Sec) formation: PSTK produces the phosphoseryl-tRNA consumed by SepSecS.
- SECISBP2-dependent SECIS recognition feeds into EEFSEC-dependent Sec-tRNA(Sec) delivery: SECISBP2-dependent mRNP assembly supplies the recoding context used during EEFSEC delivery.

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

# Species-Aware Module Review: Selenocysteine Biosynthesis & Co-translational Incorporation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Commissioned module:** Bacterial and eukaryotic selenocysteyl-tRNA(Sec) synthesis and UGA→Sec recoding
**Resolved local bucket:** KEGG `ppu00450` "Selenocompound metabolism" (module area: other_kegg_pathway)
**Evidence base:** Direct target-strain UniProt/genome annotation (UP000000556) + bacterial Sec literature

---

## 1. Executive summary

*P. putida* KT2440 **encodes a complete and demonstrably used bacterial selenocysteine (Sec) pathway.** All four functional steps of the module are satisfied by the **bacterial SelA/SelB route**, and the machinery is validated by a genuine downstream selenoprotein target — formate dehydrogenase-O major subunit **fdoG (PP_0489), which carries an annotated selenocysteine at residue 197**. The eukaryotic route (PSTK, SepSecS, SECISBP2, EEFSEC) is absent, as expected for a bacterium.

The **module is therefore `covered`/satisfiable**, but the **local metadata for this module is substantially misaligned**:

- **Two obligatory module genes are MISSING from the candidate list**: the Sec-specific elongation factor **selB (PP_0494)** and the seryl-tRNA(Sec) ligase **serS (PP_4000)**. tRNA(Sec)/selC (a tRNA gene) is also required and not represented.
- **Ten of the 12 candidate genes are out-of-scope over-propagations**: methionine/cysteine/sulfur-assimilation enzymes (metB, metG, cysD, cysNC, mdeA, metH, metE, PP_4348, PP_4594, PP_4637) pulled in only because the resolved bucket is KEGG **ppu00450 "Selenocompound metabolism"**, a broad map that lumps promiscuous Se-amino-acid analog metabolism with the Sec translational trait.
- KT2440 additionally carries the **distinct selenouridine (SeU) trait** (SelU/YbbB, PP_0822), a tRNA-modification trait that shares the SelD selenophosphate donor but is **not** part of the Sec incorporation module.

**Bottom line for curation:** mark the four Sec steps `covered`; add selB, serS, selC; reclassify the methionine/cysteine enzymes as out-of-module; document the boundary problem between the commissioned Sec module and the KEGG "Selenocompound metabolism" bucket.

---

## 2. Target-organism pathway definition

**In scope (the commissioned module):** the co-translational, ribosome-dependent pathway that (1) activates selenium to selenophosphate, (2) charges tRNA(Sec) with serine, (3) converts Ser-tRNA(Sec) to Sec-tRNA(Sec), and (4) recodes an in-frame UGA codon as selenocysteine in a SECIS-dependent context. In KT2440 this is realized entirely by the **bacterial branch**.

**Must be kept separate (neighboring processes wrongly co-bucketed here):**
- **Methionine biosynthesis / one-carbon metabolism** (KEGG ppu00270/ppu00920/ppu04980): metB, metG, metH, metE, PP_4637, mdeA, cystathionine β/γ enzymes.
- **Sulfate assimilation** (KEGG ppu00261/ppu00920): cysD, cysNC (ATP-sulfurylase).
- **tRNA wobble modification / selenouridine trait**: selU (PP_0822) — a separate Se-utilization trait.
These enzymes appear under "Selenocompound metabolism" only because KEGG maps the **free-amino-acid seleno-analogs** (selenomethionine, Se-adenosylselenomethionine, selenocystathionine) through the same sulfur/methionine enzymes. That is **not** the co-translational Sec trait.

**Alternate names / database definitions:**
- KEGG **ppu00450 "Selenocompound metabolism"** = broad map (analog metabolism + SelD + SelA + SelU), *not* a clean Sec-incorporation module.
- The clean concept corresponds to GO **selenocysteine incorporation (GO:0001514)**, **selenocysteine biosynthetic process**, and the "Sec utilization trait (SUT)" of the comparative-genomics literature (Zhang & Gladyshev).
- Gene synonyms: SelD = selenophosphate synthetase / SPS / "selenide, water dikinase"; SelC = tRNA(Sec); SelU = YbbB / tRNA 2-selenouridine synthase.

---

## 3. Expected step model (bacterial branch) and status in KT2440

| # | Module step | Player (bacterial) | KT2440 gene | Status |
|---|-------------|--------------------|-------------|--------|
| 1 | Selenophosphate synthesis | SelD selenophosphate synthetase | **selD / PP_0823** (P59392) | **covered** (in candidate list) |
| 2 | Ser-tRNA(Sec) aminoacylation | SerRS (dual Ser/Sec) | **serS / PP_4000** (Q88FT2) | **covered** — *missing from candidate list* |
| — | tRNA(Sec) scaffold | SelC tRNA(Sec) | selC (tRNA gene) | **covered by functional inference** — a mature Sec-containing product (fdoG Sec197) cannot form without an active tRNA(Sec); confirm gene locus with tRNAscan-SE/GtRNAdb |
| 3 | Ser→Sec conversion | SelA Sec synthase | **selA / PP_0493** (Q88QJ8) | **covered** (in candidate list) |
| 4 | UGA recoding + Sec-tRNA delivery | SelB EF + SECIS | **selB / PP_0494** (Q88QJ7) | **covered** — *missing from candidate list* |
| Target | Selenoprotein substrate | selenoprotein w/ in-frame UGA + SECIS | **fdoG / PP_0489** (Sec197) | **present & validated** |

**Eukaryotic branch (PSTK → SepSecS; SECISBP2 → EEFSEC):** zero proteome hits → **`not_expected_in_target_taxon`** for all eukaryotic-route steps.

**Genomic context (strong corroboration):** the pathway is organized as a co-localized cluster **PP_0489–PP_0494 = fdoG–fdoH–fdoI–fdhE–selA–selB**, with **selD (PP_0823) adjacent to selU (PP_0822)** elsewhere on the chromosome. The physical adjacency of the selenoprotein target (fdoGHI), its maturation factor (fdhE), and the Sec-decoding genes (selA, selB) is exactly the operonic arrangement expected of a functional Sec system.

---

## 4. Candidate genes and evidence

### High-confidence, in-module (keep)
- **selA — PP_0493 (Q88QJ8).** L-seryl-tRNA(Sec) selenium transferase, EC 2.9.1.1; GO:0004125, GO:0001717, GO:0001514. Role: Ser-tRNA(Sec)→Sec-tRNA(Sec). Evidence: sequence/family + operon context (strong). **Covered.**
- **selD — PP_0823 (P59392, reviewed Swiss-Prot).** Selenophosphate synthetase, EC 2.7.9.3; GO:0004756, GO:0016260. Role: selenium activation for BOTH Sec and SeU traits. Evidence: reviewed entry (strong). **Covered.** Caveat: SelD presence alone does not prove Sec (it also feeds SelU); however here SelA/SelB co-presence removes that ambiguity.

### In-module but ABSENT from candidate list (must be added)
- **selB — PP_0494 (Q88QJ7).** Selenocysteyl-tRNA-specific elongation factor (EC 3.6.5.-); GTPase; RNA binding; GO:0001514. Obligatory step-4 gene; adjacent to selA. **Promote to full review; add to module.**
- **serS — PP_4000 (Q88FT2).** Seryl-tRNA(Ser/Sec) synthetase, EC 6.1.1.11; GO:0016260. Dual-function housekeeping SerRS that also charges tRNA(Sec). **Add as step-2 gene** (flag: shared with canonical Ser-tRNA charging; not Sec-exclusive).
- **selC / tRNA(Sec)** — required tRNA; not a protein, so absent from the proteome-derived candidate list. **Flag for tRNA-level curation** (tRNAscan / genome check).
- **fdoG — PP_0489 (A0A140FVZ1)** and its subunits fdoH/PP_0490, fdoI/PP_0491, maturation factor fdhE/PP_0492. The Sec-containing substrate that justifies the module. **Document as the selenoprotein target.**

### Out-of-scope over-propagations (reclassify to sulfur/methionine metabolism)
metB (PP_0659), metG (PP_1097), cysD (PP_1303), cysNC (PP_1304), mdeA (PP_1308), metH (PP_2375), metE (PP_2698), PP_4348 (cystathionine β-lyase), PP_4594 (cystathionine γ-synthase), PP_4637 (MetE-family). None participate in tRNA(Sec) synthesis or UGA recoding. They enter the bucket via KEGG "Selenocompound metabolism" (free seleno-amino-acid analog turnover). Note cysD/cysNC are even primary-bucketed to ppu00261 and metH to ppu04980 in the metadata itself — internal evidence that they are not native to this module.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Metadata gap (high priority):** the candidate list is built from a KEGG *pathway* bucket and therefore captures 2 of ~5 real module genes while missing selB, serS, and selC. This is a **metadata-construction artifact**, not a biological gap.
- **Boundary error (high priority):** `module_needs_revision` at the bucket level — the KEGG ppu00450 "Selenocompound metabolism" mapping is the wrong source for a "Sec biosynthesis + incorporation" module. 10/12 candidates are false-positive module members.
- **SelD ambiguity:** SelD alone is a weak indicator of Sec (it also serves the SeU/SelU trait, PMID 18510720). Here disambiguated by SelA+SelB co-presence.
- **Evidence-quality caveat on the selenoprotein target:** fdoG's Sec197 rests on **imported genome-annotation evidence (ECO:0000313|EMBL:AMM02774.1, TrEMBL)** — i.e., the genome pipeline translated an in-frame TGA as Sec. Direct experimental confirmation of the Sec residue (or of the in-frame UGA + downstream bacterial SECIS hairpin) is not on record for KT2440.
- **Paralog note:** the cytoplasmic formate dehydrogenase α-subunit **PP_2185** is a **non-Sec (Cys) homolog** — a reminder that "formate dehydrogenase" annotation ≠ selenoprotein. Only fdoG/PP_0489 carries Sec.
- **Selenoproteome size:** exactly **one** selenoprotein genome-wide — consistent with an aerobic Gammaproteobacterium (selenoprotein-rich taxa are Deltaproteobacteria/Clostridia; PMID 17054778).

---

## 6. Module and GO-curation recommendations

**Step status calls:**
- Step 1 (selenophosphate, SelD) → **covered** (PP_0823).
- Step 2 (Ser-tRNA(Sec), SerRS) → **covered** (PP_4000) — *add to module metadata.*
- Step 3 (SelA route) → **covered** (PP_0493).
- Step 4 (SelB insertion system) → **covered** (PP_0494) — *add to module metadata.*
- tRNA(Sec)/selC → **covered by functional inference** (the mature fdoG selenoprotein product is obligate proof of an active tRNA(Sec)); flag only for explicit gene-locus annotation via tRNAscan-SE/GtRNAdb. Direct tRNA-database retrieval was not obtainable in this review.
- All **eukaryotic-route steps** (PSTK, SepSecS, SECISBP2, EEFSEC) → **not_expected_in_target_taxon.**

**Module-level:**
- **`module_needs_revision`** on the bucket-to-module mapping: replace the KEGG ppu00450 source with a curated Sec-incorporation gene set {selD, serS, selA, selB, selC, + selenoprotein targets}.
- Recommend a **separate module/annotation for the selenouridine (SeU) trait** (selU/PP_0822 + selD) and keep it distinct from Sec incorporation.
- Move metB/metG/cysD/cysNC/mdeA/metH/metE/PP_4348/PP_4594/PP_4637 to methionine/cysteine/sulfur modules.

**GO curation:**
- GO:0001514 (selenocysteine incorporation) and GO:0016260 (selenocysteine biosynthetic process) are appropriately assignable to PP_0493, PP_0494, PP_0823, PP_4000. No new GO terms appear required; the existing selenocysteine-incorporation and selenouridine-modification terms cover the traits.

---

## 7. Genes to promote to full `fetch-gene` review

1. **selB — PP_0494 (Q88QJ7)** — missing obligatory step-4 gene; highest priority.
2. **serS — PP_4000 (Q88FT2)** — missing step-2 gene; flag dual Ser/Sec function.
3. **fdoG — PP_0489 (A0A140FVZ1)** — the sole selenoprotein target; verify in-frame UGA + SECIS; note TrEMBL/imported evidence.
4. **selC / tRNA(Sec)** — confirm tRNA gene at genome level (tRNAscan-SE).
5. **selD — PP_0823 (P59392)** and **selU — PP_0822 (Q88PM7)** — confirm dual-trait assignment and separate SeU trait.

---

## 8. Key references

- Fischer et al. 2007, *Biol Chem* — bacterial UGA recoding requires SECIS, SelB, Sec-tRNASec formed from Ser-tRNASec by SelA using selenophosphate. **PMID 17937620.**
- Serrão et al. 2021 — bacterial Ser→Sec conversion by homodecameric SelA followed by SelB delivery. **PMID 34624294.**
- Silva et al. 2015 — SelA/tRNA(Sec)/SelD/SelB/SECIS ternary-complex biochemistry. **PMID 26378233.**
- Zhang, Turanov, Hatfield, Gladyshev 2008 — SelD required for both Sec and SeU; SelA/SelB define Sec, YbbB defines SeU. **PMID 18510720.**
- Zhang, Romero, Salinas, Gladyshev 2006 — Sec utilization dynamics; selenoprotein-rich taxa are Deltaproteobacteria/Clostridia (aerobes tend to lose selenoproteomes). **PMID 17054778.**
- Peng et al. 2016 — comparative genomics of Se-utilization traits across >5200 bacteria. **PMID 26800233.**
- Shaw et al. 2012 — selA/selB required for FDH selenoprotein biogenesis (link between Sec machinery and FDH). **PMID 22609917.**
- Primary data: UniProt proteome **UP000000556** (P. putida KT2440); reviewed entry **P59392 (SelD)**; **A0A140FVZ1 (fdoG, Sec197, ECO:0000313|EMBL:AMM02774.1)**.

---

### Evidence provenance summary
- **Direct target-strain (strong):** presence/annotation of selD, selA, selB, serS, selU, and the fdoG Sec197 residue — all from the KT2440 proteome/genome (UP000000556).
- **Imported/predicted (moderate):** the fdoG Sec assignment (genome-pipeline translation of in-frame TGA; ECO:0000313).
- **Homology/comparative-genomics transfer (contextual):** mechanistic role of each Sec factor and the expectation of a minimal aerobic selenoproteome (from *E. coli*/broad bacterial studies; strong mechanistic transfer because the KT2440 genes are clear orthologs in an intact operon).


## Artifacts

- [OpenScientist final report](PSEPK__selenocysteine_biosynthesis_incorporation__ppu00450-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__selenocysteine_biosynthesis_incorporation__ppu00450-deep-research-openscientist_artifacts/final_report.pdf)