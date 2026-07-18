---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T12:56:01.495605'
end_time: '2026-07-18T13:12:48.881456'
duration_seconds: 1007.39
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Coenzyme A biosynthesis from pantothenate (PANK1/2/3 + PPCS + PPCDC
    + COASY)
  module_summary: "Coenzyme A (CoA) is the universal acyl-group carrier of intermediary\
    \ metabolism (fatty-acid oxidation and synthesis, the TCA cycle, ketone bodies)\
    \ and the source of the phosphopantetheine prosthetic group of acyl-carrier proteins.\
    \ It is built from the vitamin pantothenate (vitamin B5) in five conserved steps.\
    \ The first, rate-limiting and feedback-regulated step is phosphorylation of pantothenate\
    \ to 4'-phosphopantothenate by pantothenate kinase; humans have three catalytically\
    \ active isoforms \u2014 PANK1 (cytosolic/nuclear), PANK2 (mitochondrial, processed\
    \ to the intermembrane space) and PANK3 (cytosolic) \u2014 all inhibited by acyl-CoA/CoA\
    \ (a fourth paralogue, PANK4, is a 4'-phosphopantetheine phosphatase rather than\
    \ a kinase, curated separately). Phosphopantothenate is then conjugated with L-cysteine\
    \ by the (ATP-preferring, in mammals) phosphopantothenate--cysteine ligase PPCS,\
    \ and the FMN-dependent phosphopantothenoylcysteine decarboxylase PPCDC removes\
    \ the carboxyl group to give 4'-phosphopantetheine. Finally the bifunctional CoA\
    \ synthase COASY completes the pathway: its phosphopantetheine adenylyltransferase\
    \ (PPAT) domain forms dephospho-CoA and its dephospho-CoA kinase (DPCK) domain\
    \ phosphorylates it to CoA. Inherited defects cause distinct diseases: PANK2 \u2014\
    \ pantothenate-kinase-associated neurodegeneration (PKAN/NBIA1, brain iron accumulation);\
    \ COASY \u2014 COASY-protein-associated neurodegeneration (COPAN/NBIA6) and pontocerebellar\
    \ hypoplasia; PPCS \u2014 autosomal-recessive dilated cardiomyopathy."
  module_outline: "- Coenzyme A biosynthesis from pantothenate\n  - 1. pantothenate\
    \ phosphorylation (rate-limiting)\n  - Pantothenate kinase (PANK1/PANK2/PANK3)\n\
    \    - PANK1: pantothenate kinase (cytosolic) (molecular player: pantothenate\
    \ kinase (PANK) family; activity or role: pantothenate kinase activity)\n    -\
    \ PANK2: pantothenate kinase (mitochondrial; PKAN) (molecular player: pantothenate\
    \ kinase (PANK) family; activity or role: pantothenate kinase activity)\n    -\
    \ PANK3: pantothenate kinase (cytosolic) (molecular player: pantothenate kinase\
    \ (PANK) family; activity or role: pantothenate kinase activity)\n  - 2. cysteine\
    \ conjugation and decarboxylation\n  - Phosphopantothenoylcysteine synthesis and\
    \ decarboxylation (PPCS, PPCDC)\n    - PPCS: phosphopantothenoylcysteine synthetase\
    \ (molecular player: PPCS / phosphopantothenate-cysteine ligase family; activity\
    \ or role: phosphopantothenate--cysteine ligase activity)\n    - PPCDC: phosphopantothenoylcysteine\
    \ decarboxylase (FMN) (molecular player: PPCDC / phosphopantothenoylcysteine decarboxylase\
    \ family; activity or role: phosphopantothenoylcysteine decarboxylase activity)\n\
    \  - 3. adenylylation and phosphorylation to CoA\n  - Bifunctional CoA synthase\
    \ (COASY)\n    - COASY: bifunctional CoA synthase (PPAT + DPCK) (molecular player:\
    \ COASY / bifunctional CoA synthase family; activity or role: pantetheine-phosphate\
    \ adenylyltransferase activity)"
  module_connections: '- Pantothenate kinase (PANK1/PANK2/PANK3) feeds into Phosphopantothenoylcysteine
    synthesis and decarboxylation (PPCS, PPCDC): 4''-phosphopantothenate from the
    kinase step is conjugated with cysteine (PPCS) and decarboxylated (PPCDC) to 4''-phosphopantetheine.

    - Phosphopantothenoylcysteine synthesis and decarboxylation (PPCS, PPCDC) feeds
    into Bifunctional CoA synthase (COASY): 4''-phosphopantetheine is adenylylated
    and phosphorylated by the bifunctional COASY to dephospho-CoA and then CoA.'
  pathway_query: ppu00770
  pathway_id: ppu00770
  pathway_name: Pantothenate and CoA biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00770 with 10 primary genes; module
    area: cofactors_vitamins_redox.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '24'
  candidate_genes: '- coaX: PP_0438 | Q88QQ0 | Type III pantothenate kinase (EC 2.7.1.33)
    (PanK-III) (Pantothenic acid kinase) (EC 2.7.1.33; primary bucket kegg:ppu00770)

    - PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine
    amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket
    kegg:ppu00410)

    - coaE: PP_0631 | Q88Q65 | Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme
    A kinase) (EC 2.7.1.24; primary bucket kegg:ppu00770)

    - PP_0922: PP_0922 | Q88PC8 | ACP phosphodiesterase (primary bucket kegg:ppu00770)

    - PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)

    - PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4''-phosphopantetheinyl
    transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)

    - panE: PP_1351 | Q88N64 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate
    reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)

    - PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket
    kegg:ppu00660)

    - mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8)
    (EC 3.6.1.8; primary bucket kegg:ppu00770)

    - PP_2325: PP_2325 | Q88KG5 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate
    reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)

    - PP_2998: PP_2998 | Q88IK1 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate
    reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)

    - ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42)
    (EC 2.6.1.42; primary bucket kegg:ppu00290)

    - hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine
    amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket
    kegg:ppu00410)

    - pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2)
    (EC 3.5.2.2; primary bucket kegg:ppu00410)

    - pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine
    dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)

    - pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine
    dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)

    - ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86)
    (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase)
    (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC
    1.1.1.86; primary bucket kegg:ppu00290)

    - ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC
    2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket
    kegg:ppu00660)

    - ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary
    bucket kegg:ppu00660)

    - panB: PP_4699 | Q88DW9 | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC
    2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) (EC 2.1.2.11; primary
    bucket kegg:ppu00770)

    - panC: PP_4700 | Q88DW8 | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine
    ligase) (Pantoate-activating enzyme) (EC 6.3.2.1; primary bucket kegg:ppu00410)

    - coaD: PP_5123 | Q88CQ7 | Phosphopantetheine adenylyltransferase (EC 2.7.7.3)
    (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltransferase)
    (PPAT) (EC 2.7.7.3; primary bucket kegg:ppu00770)

    - ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9;
    primary bucket kegg:ppu00290)

    - dfp: PP_5285 | Q88C96 | Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate
    metabolism flavoprotein) (Phosphopantothenoylcysteine synthetase/decarboxylase)
    (PPCS-PPCDC) [Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase)
    (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5)
    (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)] (EC
    4.1.1.36; 6.3.2.5; primary bucket kegg:ppu00770)'
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
citation_count: 2
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__coenzyme_a_biosynthesis__ppu00770-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__coenzyme_a_biosynthesis__ppu00770-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Coenzyme A biosynthesis from pantothenate (PANK1/2/3 + PPCS + PPCDC + COASY) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00770
- Resolved ID: ppu00770
- Resolved name: Pantothenate and CoA biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00770 with 10 primary genes; module area: cofactors_vitamins_redox.

## Candidate Genes From Local Metadata

Candidate gene count: 24

- coaX: PP_0438 | Q88QQ0 | Type III pantothenate kinase (EC 2.7.1.33) (PanK-III) (Pantothenic acid kinase) (EC 2.7.1.33; primary bucket kegg:ppu00770)
- PP_0614: PP_0614 | Q88Q81 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- coaE: PP_0631 | Q88Q65 | Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme A kinase) (EC 2.7.1.24; primary bucket kegg:ppu00770)
- PP_0922: PP_0922 | Q88PC8 | ACP phosphodiesterase (primary bucket kegg:ppu00770)
- PP_1157: PP_1157 | Q877U6 | Acetolactate synthase (primary bucket kegg:ppu00660)
- PP_1183: PP_1183 | Q88NM4 | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) (primary bucket kegg:ppu00074)
- panE: PP_1351 | Q88N64 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- PP_1394: PP_1394 | Q88N22 | Acetolactate synthase, large subunit (primary bucket kegg:ppu00660)
- mazG: PP_1657 | Q88MB7 | Nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) (EC 3.6.1.8; primary bucket kegg:ppu00770)
- PP_2325: PP_2325 | Q88KG5 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- PP_2998: PP_2998 | Q88IK1 | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (EC 1.1.1.169; primary bucket kegg:ppu00770)
- ilvE: PP_3511 | Q88H54 | Branched-chain-amino-acid aminotransferase (EC 2.6.1.42) (EC 2.6.1.42; primary bucket kegg:ppu00290)
- hyuC: PP_4034 | Q88FQ3 | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) (EC 3.5.1.6; 3.5.3.9; primary bucket kegg:ppu00410)
- pydB: PP_4036 | A0A140FWK2 | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) (EC 3.5.2.2; primary bucket kegg:ppu00410)
- pydX: PP_4037 | Q88FQ1 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- pydA: PP_4038 | Q88FQ0 | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) (EC 1.3.1.1; primary bucket kegg:ppu00410)
- ilvC: PP_4678 | Q88DZ0 | Ketol-acid reductoisomerase (NADP(+)) (KARI) (EC 1.1.1.86) (Acetohydroxy-acid isomeroreductase) (AHIR) (Alpha-keto-beta-hydroxylacyl reductoisomerase) (Ketol-acid reductoisomerase type 1) (Ketol-acid reductoisomerase type I) (EC 1.1.1.86; primary bucket kegg:ppu00290)
- ilvH: PP_4679 | Q88DY9 | Acetolactate synthase small subunit (AHAS) (ALS) (EC 2.2.1.6) (Acetohydroxy-acid synthase small subunit) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- ilvI: PP_4680 | Q88DY8 | Acetolactate synthase (EC 2.2.1.6) (EC 2.2.1.6; primary bucket kegg:ppu00660)
- panB: PP_4699 | Q88DW9 | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC 2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) (EC 2.1.2.11; primary bucket kegg:ppu00770)
- panC: PP_4700 | Q88DW8 | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) (EC 6.3.2.1; primary bucket kegg:ppu00410)
- coaD: PP_5123 | Q88CQ7 | Phosphopantetheine adenylyltransferase (EC 2.7.7.3) (Dephospho-CoA pyrophosphorylase) (Pantetheine-phosphate adenylyltransferase) (PPAT) (EC 2.7.7.3; primary bucket kegg:ppu00770)
- ilvD: PP_5128 | Q88CQ2 | Dihydroxy-acid dehydratase (DAD) (EC 4.2.1.9) (EC 4.2.1.9; primary bucket kegg:ppu00290)
- dfp: PP_5285 | Q88C96 | Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate metabolism flavoprotein) (Phosphopantothenoylcysteine synthetase/decarboxylase) (PPCS-PPCDC) [Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase) (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5) (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)] (EC 4.1.1.36; 6.3.2.5; primary bucket kegg:ppu00770)

## Generic Module Context

### Working Scope

Coenzyme A (CoA) is the universal acyl-group carrier of intermediary metabolism (fatty-acid oxidation and synthesis, the TCA cycle, ketone bodies) and the source of the phosphopantetheine prosthetic group of acyl-carrier proteins. It is built from the vitamin pantothenate (vitamin B5) in five conserved steps. The first, rate-limiting and feedback-regulated step is phosphorylation of pantothenate to 4'-phosphopantothenate by pantothenate kinase; humans have three catalytically active isoforms — PANK1 (cytosolic/nuclear), PANK2 (mitochondrial, processed to the intermembrane space) and PANK3 (cytosolic) — all inhibited by acyl-CoA/CoA (a fourth paralogue, PANK4, is a 4'-phosphopantetheine phosphatase rather than a kinase, curated separately). Phosphopantothenate is then conjugated with L-cysteine by the (ATP-preferring, in mammals) phosphopantothenate--cysteine ligase PPCS, and the FMN-dependent phosphopantothenoylcysteine decarboxylase PPCDC removes the carboxyl group to give 4'-phosphopantetheine. Finally the bifunctional CoA synthase COASY completes the pathway: its phosphopantetheine adenylyltransferase (PPAT) domain forms dephospho-CoA and its dephospho-CoA kinase (DPCK) domain phosphorylates it to CoA. Inherited defects cause distinct diseases: PANK2 — pantothenate-kinase-associated neurodegeneration (PKAN/NBIA1, brain iron accumulation); COASY — COASY-protein-associated neurodegeneration (COPAN/NBIA6) and pontocerebellar hypoplasia; PPCS — autosomal-recessive dilated cardiomyopathy.

### Provisional Biological Outline

- Coenzyme A biosynthesis from pantothenate
  - 1. pantothenate phosphorylation (rate-limiting)
  - Pantothenate kinase (PANK1/PANK2/PANK3)
    - PANK1: pantothenate kinase (cytosolic) (molecular player: pantothenate kinase (PANK) family; activity or role: pantothenate kinase activity)
    - PANK2: pantothenate kinase (mitochondrial; PKAN) (molecular player: pantothenate kinase (PANK) family; activity or role: pantothenate kinase activity)
    - PANK3: pantothenate kinase (cytosolic) (molecular player: pantothenate kinase (PANK) family; activity or role: pantothenate kinase activity)
  - 2. cysteine conjugation and decarboxylation
  - Phosphopantothenoylcysteine synthesis and decarboxylation (PPCS, PPCDC)
    - PPCS: phosphopantothenoylcysteine synthetase (molecular player: PPCS / phosphopantothenate-cysteine ligase family; activity or role: phosphopantothenate--cysteine ligase activity)
    - PPCDC: phosphopantothenoylcysteine decarboxylase (FMN) (molecular player: PPCDC / phosphopantothenoylcysteine decarboxylase family; activity or role: phosphopantothenoylcysteine decarboxylase activity)
  - 3. adenylylation and phosphorylation to CoA
  - Bifunctional CoA synthase (COASY)
    - COASY: bifunctional CoA synthase (PPAT + DPCK) (molecular player: COASY / bifunctional CoA synthase family; activity or role: pantetheine-phosphate adenylyltransferase activity)

### Known Relationships Among Steps

- Pantothenate kinase (PANK1/PANK2/PANK3) feeds into Phosphopantothenoylcysteine synthesis and decarboxylation (PPCS, PPCDC): 4'-phosphopantothenate from the kinase step is conjugated with cysteine (PPCS) and decarboxylated (PPCDC) to 4'-phosphopantetheine.
- Phosphopantothenoylcysteine synthesis and decarboxylation (PPCS, PPCDC) feeds into Bifunctional CoA synthase (COASY): 4'-phosphopantetheine is adenylylated and phosphorylated by the bifunctional COASY to dephospho-CoA and then CoA.

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

# Coenzyme A Biosynthesis from Pantothenate in *Pseudomonas putida* KT2440 — Module/Pathway/Taxon Review

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG ppu00770 "Pantothenate and CoA biosynthesis"
**Module area:** cofactors_vitamins_redox
**Scope of this review:** the five-step conversion of pantothenate (vitamin B5) → 4′-phosphopantothenate → 4′-phosphopantothenoyl-cysteine → 4′-phosphopantetheine → dephospho-CoA → coenzyme A.

---

## 1. Executive Summary

Coenzyme A biosynthesis from pantothenate is **fully satisfiable (module status: COVERED)** in *Pseudomonas putida* KT2440. Every one of the five canonical steps is encoded by a structurally verified, correctly sized, single-copy gene in proteome UP000000556. The critical curation point is that the pathway must be described in the **bacterial enzyme frame (CoaX/CoaBC/CoaD/CoaE)**, not the human PANK1/2/3 + PPCS + PPCDC + COASY frame supplied in the generic module context. The mammalian gene names do not have one-to-one orthologs in this organism; forcing the human frame onto KT2440 would incorrectly split step 2+3 (fused into one bacterial CoaBC protein) and incorrectly fuse steps 4+5 (which are two separate bacterial proteins, not a single COASY).

The mapping is unambiguous: pantothenate phosphorylation is carried out by a **CoA-insensitive Type III pantothenate kinase, coaX/PP_0438** (EC 2.7.1.33) — not the *E. coli* Type I CoaA. The cysteine-conjugation and decarboxylation steps (the roles of human PPCS and PPCDC) are performed by a **single bifunctional CoaBC protein, dfp/PP_5285** (EC 6.3.2.5 + EC 4.1.1.36), whose two Pfam domains (Flavoprotein + DFP) each contribute one catalytic activity. The final two steps that mammalian COASY fuses are here **two separate enzymes**: **coaD/PP_5123** (phosphopantetheine adenylyltransferase, PPAT, EC 2.7.7.3) and **coaE/PP_0631** (dephospho-CoA kinase, DPCK, EC 2.7.1.24).

Two actionable curation flags emerged. First, **aspartate 1-decarboxylase (panD, EC 4.1.1.11) is genuinely absent** in KT2440 (confirmed by three independent negative queries including Pfam PF02261), even though it is present in *P. aeruginosa* and *P. fluorescens*. This is a strain-specific gap in *de novo* β-alanine supply; β-alanine (needed upstream for pantothenate synthesis) most likely comes from reductive pyrimidine catabolism (the *pyd* genes plus the amidohydrolases hyuC/PP_4034 and PP_0614). Second, **EC 1.1.1.169 (ketopantoate reductase, panE) is over-propagated**: domain architecture shows only **PP_1351 is the true panE**, while PP_2325 and PP_2998 are KPR-related paralogs in a distinct InterPro family and **PP_4452 (not in the supplied candidate list) is a mis-annotated opine dehydrogenase**. Finally, roughly half of the 24 supplied candidate genes belong to neighboring KEGG maps (branched-chain amino acid biosynthesis ppu00290/ppu00660, β-alanine/pyrimidine catabolism ppu00410, CoA *utilization* rather than synthesis) and should be excluded from the ppu00770 CoA-biosynthesis core.

---

## 2. Target-Organism Pathway Definition

### What is included

This module covers the **universal five-step conversion of pantothenate to coenzyme A**:

1. Pantothenate + ATP → 4′-phosphopantothenate (pantothenate kinase; rate-limiting/feedback step in many organisms)
2. 4′-phosphopantothenate + L-cysteine + CTP/ATP → 4′-phosphopantothenoyl-L-cysteine (phosphopantothenoylcysteine synthetase; CoaB/PPCS)
3. 4′-phosphopantothenoyl-L-cysteine → 4′-phosphopantetheine + CO₂ (phosphopantothenoylcysteine decarboxylase, FMN-dependent; CoaC/PPCDC)
4. 4′-phosphopantetheine + ATP → dephospho-CoA (phosphopantetheine adenylyltransferase, PPAT; CoaD)
5. Dephospho-CoA + ATP → CoA (dephospho-CoA kinase, DPCK; CoaE)

### What must be kept separate (neighboring pathways / overview maps)

- **Upstream pantothenate (vitamin B5) biosynthesis** — *panB, panC, panD, panE*. KEGG lumps these into the same map ppu00770, but for the CoA-biosynthesis *module* proper (pantothenate → CoA) they are the supply route, not the core. They should be tracked as an adjacent sub-module.
- **Branched-chain amino acid biosynthesis (ppu00290, ppu00660; valine/leucine/isoleucine)** — *ilvC, ilvD, ilvE, ilvH, ilvI, PP_1157, PP_1394*. These produce the 2-oxoisovalerate precursor feeding *panB*, but are not CoA-biosynthesis genes.
- **β-alanine / pyrimidine catabolism (ppu00410)** — *pydA/B/X (PP_4036–4038), hyuC/PP_4034, PP_0614*. These supply β-alanine; relevant to pantothenate supply, not to the CoA core.
- **CoA *utilization* (not synthesis)** — the 4′-phosphopantetheinyl transferase **entD/PP_1183** (siderophore/PKS holo-ACP loading), **acpH/PP_0922** (ACP phosphodiesterase, removes phosphopantetheine), and **mazG/PP_1657** (NTP pyrophosphohydrolase / house-cleaning). These consume or recycle CoA-derived groups and are not part of the biosynthetic path.

### Alternate names / database definitions

- **KEGG** ppu00770 "Pantothenate and CoA biosynthesis" merges vitamin B5 synthesis and CoA synthesis into one map.
- **Bacterial gene nomenclature:** *coaA* (Type I PanK), *coaX* (Type III PanK), *coaBC*/*dfp* (bifunctional PPCS-PPCDC), *coaD* (PPAT), *coaE* (DPCK).
- **Human/eukaryotic frame:** PANK1/2/3 (three PanK isoforms), PPCS, PPCDC, COASY (bifunctional PPAT+DPCK). The generic module context supplied uses this frame; it does **not** map cleanly onto *Pseudomonas*.

---

## 3. Expected Step Model (in the bacterial frame)

```
                 β-alanine (from pyrimidine catabolism: pyd + hyuC/PP_0614;
                            panD route ABSENT in KT2440)
                     |
   2-oxoisovalerate  |  (panB PP_4699, KPHMT)
        |            v
     ketopantoate --(panE PP_1351, EC 1.1.1.169)--> pantoate --(panC PP_4700, EC 6.3.2.1)--> PANTOTHENATE
                                                                                                  |
   =========================== CoA-biosynthesis CORE (this module) ============================== |
                                                                                                  v
  STEP 1  pantothenate  --[coaX / PP_0438, Type III PanK, EC 2.7.1.33]-->  4'-phosphopantothenate
                                                                                                  |
  STEP 2  + L-cysteine  --[dfp / PP_5285 CoaB domain (DFP, PF04127), EC 6.3.2.5]--> P-pantothenoyl-Cys
                                                                                                  |
  STEP 3                --[dfp / PP_5285 CoaC domain (Flavoprotein, PF02441), EC 4.1.1.36]--> 4'-phosphopantetheine
                                                                                                  |
  STEP 4                --[coaD / PP_5123, PPAT, EC 2.7.7.3]-->  dephospho-CoA
                                                                                                  |
  STEP 5                --[coaE / PP_0631, DPCK, EC 2.7.1.24]-->  COENZYME A
```

**Key structural notes vs. the human frame:**
- Human PANK1/2/3 (three feedback-inhibited isoforms) → **one** *Pseudomonas* Type III PanK (CoaX), **not** feedback-inhibited by CoA/acyl-CoA.
- Human PPCS + PPCDC (two proteins) → **one** bifunctional CoaBC (dfp) protein.
- Human COASY (one bifunctional PPAT+DPCK protein) → **two** separate *Pseudomonas* proteins (CoaD + CoaE).

---

## 4. Candidate Genes and Evidence

### 4.1 Core CoA-biosynthesis genes (COVERED)

| Step | EC | KT2440 gene | Locus / UniProt | Length | Domain evidence | Confidence |
|------|-----|-------------|------------------|--------|-----------------|------------|
| 1. Pantothenate kinase | 2.7.1.33 | **coaX** | PP_0438 / Q88QQ0 | 249 aa | PF03309 Pan_kinase; InterPro Type_III_PanK + ATPase_NBD (ASKHA fold) | High |
| 2. PPCS (CoaB) | 6.3.2.5 | **dfp** (CoaBC) | PP_5285 / Q88C96 | 403 aa | PF04127 DFP domain | High |
| 3. PPCDC (CoaC) | 4.1.1.36 | **dfp** (CoaBC) | PP_5285 / Q88C96 | 403 aa | PF02441 Flavoprotein domain | High |
| 4. PPAT | 2.7.7.3 | **coaD** | PP_5123 / Q88CQ7 | 161 aa | PF01467 CTP_transf_like; InterPro PPAT | High |
| 5. DPCK | 2.7.1.24 | **coaE** | PP_0631 / Q88Q65 | 207 aa | PF01121 CoaE; InterPro Depp_CoAkinase + P-loop_NTPase | High |

**coaX / PP_0438 (Type III pantothenate kinase).** Proteome UP000000556 contains a single EC 2.7.1.33 pantothenate kinase, annotated "Type III pantothenate kinase (PanK-III)." No Type I (*coaA*) or Type II PanK is present. This is biologically expected: Type III PanK is documented as the **only** PanK in the close relative *Pseudomonas aeruginosa*. A curation-relevant caveat is that Type III PanK is **not inhibited by CoA or its thioesters**, so the generic module's "rate-limiting and feedback-regulated" language (true for human PANK1/2/3) **does not transfer** to KT2440. Domain architecture (PF03309 Pan_kinase, ASKHA/ATPase fold) confirms a structurally intact enzyme at 249 aa. *Evidence: direct UniProt annotation for KT2440 + strong transfer from P. aeruginosa (PMID 16855243).*

**dfp / PP_5285 (bifunctional CoaBC).** This single 403-aa protein carries **both** catalytic domains — PF04127 (DFP; the CoaB/PPCS ligase, EC 6.3.2.5) and PF02441 (Flavoprotein; the CoaC/PPCDC decarboxylase, EC 4.1.1.36) — matching full-length *E. coli* Dfp (~406 aa). InterPro terms "CoaBC," "CoaB-like_sf," and "DNA/pantothenate-metab_flavo_C" are all present. This confirms that KT2440 fuses module steps 2 and 3 into one gene, exactly as is standard for the vast majority of prokaryotes. Curation implication: **steps 2 and 3 are both satisfied by one locus**; do not create a "gap" for a missing standalone PPCDC. *Evidence: direct UniProt/InterPro for KT2440; mechanism supported by PMID 33420031.*

**coaD / PP_5123 (PPAT).** Single EC 2.7.7.3 enzyme, 161 aa, PF01467 (CTP_transf_like), InterPro "PPAT." Correctly sized nucleotidyltransferase. High confidence. *Direct KT2440 annotation.*

**coaE / PP_0631 (DPCK).** Single EC 2.7.1.24 enzyme, 207 aa, PF01121 (CoaE), InterPro "Depp_CoAkinase" + "P-loop_NTPase." High confidence. *Direct KT2440 annotation.*

### 4.2 Upstream pantothenate-supply genes (adjacent sub-module, not CoA core)

| Enzyme | EC | Gene | Locus / UniProt | Status |
|--------|-----|------|------------------|--------|
| Ketopantoate hydroxymethyltransferase (KPHMT) | 2.1.2.11 | panB | PP_4699 / Q88DW9 | Present, high confidence |
| Ketopantoate reductase | 1.1.1.169 | **panE** | PP_1351 / Q88N64 | **True panE** (see §5) |
| Pantothenate synthetase | 6.3.2.1 | panC | PP_4700 / Q88DW8 | Present, high confidence |
| Aspartate 1-decarboxylase | 4.1.1.11 | panD | — | **ABSENT** (see §5) |

**panE / PP_1351.** InterPro cross-references for this 305-aa protein are **identical** to experimentally characterized *E. coli* PanE (P0A9J4): IPR050838 (Ketopantoate_reductase), IPR003710 (ApbA), IPR013752 (KPA_reductase), IPR013332 (KPR_N). This is the true ketopantoate reductase. High confidence.

### 4.3 Genes belonging to neighboring pathways (exclude from ppu00770 CoA core)

| Gene(s) | Locus | Native pathway | Reason to exclude |
|---------|-------|----------------|-------------------|
| ilvC, ilvD, ilvE, ilvH, ilvI | PP_4678, PP_5128, PP_3511, PP_4679, PP_4680 | BCAA biosynthesis (ppu00290/00660) | Provide 2-oxoisovalerate precursor; not CoA genes |
| PP_1157, PP_1394 | — | Acetolactate synthase (ppu00660) | BCAA branch |
| pydA/B/X | PP_4038/4036/4037 | Pyrimidine catabolism (ppu00410) | β-alanine supply, catabolic |
| hyuC, PP_0614 | PP_4034, PP_0614 | β-alanine amidohydrolases (ppu00410) | β-alanine supply |
| entD | PP_1183 | Siderophore/PKS (ppu00074) | 4′-phosphopantetheinyl transferase — CoA *utilization* |
| acpH (PP_0922) | PP_0922 | ACP recycling | Removes phosphopantetheine — CoA *utilization* |
| mazG | PP_1657 | Nucleotide house-cleaning | NTP pyrophosphohydrolase — not CoA synthesis |

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### 5.1 GAP — panD (aspartate 1-decarboxylase, EC 4.1.1.11) is genuinely absent

Three independent negative queries against proteome UP000000556 returned zero hits: (i) no protein carrying the aspartate-1-decarboxylase Pfam domain **PF02261**, (ii) no gene named *panD*, (iii) no protein with EC 4.1.1.11. A name search for "aspartate decarboxylase" returned only unrelated decarboxylases (gcvP1/2, ldcC, cobC). By contrast, panD/EC 4.1.1.11 is annotated in *P. aeruginosa* PAO1 (Q9HV68), PA14 (Q02FU1), LESB58 (B7V1E3), PA7 (A6VCI7), and *P. fluorescens* (Q848I5).

This is a **strain-specific gap in the canonical *de novo* β-alanine route** (aspartate → β-alanine + CO₂). Because β-alanine is required to make pantothenate (panC condenses pantoate + β-alanine), KT2440 must obtain β-alanine another way. The most parsimonious alternative is **reductive pyrimidine catabolism**, which is fully encoded in KT2440: pydB dihydropyrimidinase (EC 3.5.2.2, PP_4036), pydA/pydX, and the N-carbamoyl-β-alanine amidohydrolases hyuC/PP_4034 and PP_0614 (EC 3.5.1.6). Curation action: mark the panD step **not covered by a panD ortholog** but flag β-alanine supply as **satisfied by an alternative route (pyrimidine catabolism)** — i.e., a `candidate_uncertain`/lineage-specific-alternative for β-alanine supply rather than a hard pathway break.

### 5.2 OVER-ANNOTATION — EC 1.1.1.169 propagated to four loci; only one is panE

Four KT2440 loci carry EC 1.1.1.169 (2-dehydropantoate/ketopantoate reductase): PP_1351, PP_2325, PP_2998, and PP_4452 (the last not in the supplied candidate list). InterPro domain benchmarking against *E. coli* PanE (P0A9J4) resolves the ambiguity decisively:

| Locus | UniProt | Length | InterPro panel | Verdict |
|-------|---------|--------|----------------|---------|
| **PP_1351** | Q88N64 | 305 aa | IPR050838 + IPR003710 + IPR013752 + IPR013332 (identical to *E. coli* PanE) | **True panE** |
| PP_2325 | Q88KG5 | 315 aa | IPR003710 (ApbA) but IPR051402 (KPR-Related); **lacks** IPR050838 | KPR-related paralog |
| PP_2998 | Q88IK1 | 315 aa | IPR003710 (ApbA) but IPR051402 (KPR-Related); **lacks** IPR050838 | KPR-related paralog |
| PP_4452 | Q88EL0 | 359 aa | **No** ApbA/KPR signature; IPR003421 (Opine_DH) + IPR051729 (Opine/Lysopine_DH) | **Mis-annotated opine dehydrogenase** |

Curation action: retain EC 1.1.1.169 / panE only on **PP_1351**. Demote PP_2325 and PP_2998 to "ketopantoate-reductase-related (KPR family, uncharacterized specificity)." **Correct PP_4452's annotation** — it is an opine/lysopine dehydrogenase, not a ketopantoate reductase; its EC 1.1.1.169 assignment is a clear over-propagation error.

### 5.3 Frame mismatch — human PANK/PPCS/PPCDC/COASY names do not map 1:1

The generic module supplies the human gene frame. In KT2440: (a) there is one PanK, not three, and it is CoA-insensitive Type III; (b) PPCS+PPCDC are one gene (dfp), not two; (c) COASY is split into two genes (coaD + coaE). Any module document that requires named PANK1/2/3, PPCS, PPCDC, and COASY orthologs would spuriously report gaps. The module must be defined at the **activity/EC level**, not the human-gene level.

---

## 6. Module and GO-Curation Recommendations

### Module step dispositions

| Module step | Activity (EC) | KT2440 locus | Disposition |
|-------------|---------------|--------------|-------------|
| Step 1 — pantothenate phosphorylation | 2.7.1.33 | coaX / PP_0438 | **covered** (Type III PanK; note: not feedback-inhibited) |
| Step 2 — cysteine conjugation | 6.3.2.5 | dfp / PP_5285 (DFP domain) | **covered** |
| Step 3 — decarboxylation | 4.1.1.36 | dfp / PP_5285 (Flavoprotein domain) | **covered** |
| Step 4 — adenylylation | 2.7.7.3 | coaD / PP_5123 | **covered** |
| Step 5 — phosphorylation to CoA | 2.7.1.24 | coaE / PP_0631 | **covered** |
| (Adjacent) β-alanine supply — panD | 4.1.1.11 | none | **gap / lineage-specific alternative** (pyrimidine catabolism) |

**Overall module status: COVERED** (all five CoA-core steps satisfied).

### Boundary / definition recommendations

- **module_needs_revision (framing):** replace the human PANK1/2/3 + PPCS + PPCDC + COASY frame with the bacterial CoaX/CoaBC(dfp)/CoaD/CoaE frame for this taxon. Define steps by EC/activity so the one-PanK, fused-CoaBC, split-CoaD/CoaE bacterial architecture validates as complete.
- **Keep the CoA-biosynthesis core separate** from the vitamin B5 supply sub-module (panB/C/D/E) and from BCAA biosynthesis and pyrimidine/β-alanine catabolism, even though KEGG ppu00770 merges the first two.
- **CoA-utilization genes** (entD/PP_1183, acpH/PP_0922, mazG/PP_1657) should be removed from the ppu00770 core candidate set.

### GO-curation notes

- coaX/PP_0438: GO:0004594 (pantothenate kinase activity) — appropriate. Do **not** attach CoA-feedback-inhibition regulatory annotations transferred from human PANK.
- dfp/PP_5285: annotate **both** GO:0004632 (phosphopantothenate–cysteine ligase) and GO:0004633 (phosphopantothenoylcysteine decarboxylase) on the one protein.
- PP_2325/PP_2998: broaden/soften from "ketopantoate reductase (panE)" to KPR-family; avoid propagating EC 1.1.1.169 as a confirmed function.
- PP_4452: request re-annotation to opine/lysopine dehydrogenase (IPR003421); remove EC 1.1.1.169.
- No new GO term requests appear necessary; existing terms cover all activities.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **dfp / PP_5285 (CoaBC)** — highest priority. Confirm both catalytic domains are intact and that the single locus is the only route for steps 2+3 (no standalone PPCDC backup). Central, single-copy, essential.
2. **coaX / PP_0438** — confirm Type III assignment and CoA-insensitivity phenotype; document that no Type I/II PanK exists as backup.
3. **PP_4452** — promote to correct the opine-dehydrogenase mis-annotation and strip the erroneous EC 1.1.1.169/panE label.
4. **PP_2325 and PP_2998** — review to soften panE/EC 1.1.1.169 over-propagation and assign accurate KPR-family descriptions.
5. **β-alanine supply cluster (hyuC/PP_4034, PP_0614, pydA/B/X PP_4036–4038)** — review as the likely compensatory route for the absent panD, to formally close the β-alanine gap.

---

## 8. Evidence Base

| Finding | Evidence type | Strength / transfer |
|---------|---------------|---------------------|
| All 5 CoA steps encoded by single-copy genes | Direct UniProt annotation of KT2440 proteome UP000000556 | Direct, strong |
| coaX is the sole PanK and is Type III | Direct KT2440 annotation + *P. aeruginosa* literature | Direct + strong Pseudomonas transfer |
| dfp is a genuine two-domain CoaBC | Direct UniProt Pfam/InterPro (PF04127 + PF02441) for PP_5285 | Direct, strong |
| coaD/coaE structurally intact | Direct UniProt Pfam/InterPro | Direct, strong |
| panD absent | Three independent negative proteome queries (PF02261, gene, EC) | Direct negative, strong |
| panD present in other Pseudomonas | UniProt annotations for PAO1/PA14/LESB58/PA7/P. fluorescens | Direct for those strains |
| EC 1.1.1.169 over-propagation | InterPro domain benchmarking vs *E. coli* PanE (P0A9J4) | Direct comparative, strong |

**Literature:**

- **[PMID: 16855243](https://pubmed.ncbi.nlm.nih.gov/16855243/)** — *Crystal structure of a type III pantothenate kinase: insight into the mechanism of an essential coenzyme A biosynthetic enzyme universally distributed in bacteria.* Establishes that "This type III PanK, or PanK-III, is widely distributed in the bacterial kingdom and accounts for the only known PanK in many pathogenic species, such as Helicobacter pylori, Bordetella pertussis, and Pseudomonas aeruginosa," and that it "is not inhibited by CoA or its thioesters." Supports the assignment of PP_0438 as the sole, CoA-insensitive Type III PanK in *P. putida* and directly refutes transfer of the human feedback-regulation model to this taxon.

- **[PMID: 33420031](https://pubmed.ncbi.nlm.nih.gov/33420031/)** — *Inhibiting Mycobacterium tuberculosis CoaBC by targeting an allosteric site.* States that "The biosynthesis of CoA is performed in five steps, with the second and third steps being catalysed in the vast majority of prokaryotes, including M. tuberculosis, by a single bifunctional protein, CoaBC." Directly supports the interpretation that KT2440 steps 2 and 3 are both covered by the single bifunctional dfp/PP_5285 protein, and that no separate PPCDC gene is expected.

---

## 9. Limitations and Knowledge Gaps

- **No direct KT2440 biochemistry:** all step assignments rest on genome/proteome annotation and domain architecture, not on purified-enzyme assays from strain KT2440 itself. Enzymatic activity is inferred, though the domain evidence is strong.
- **coaX kinetics and feedback status** are transferred from *P. aeruginosa* Type III PanK; not experimentally verified for the KT2440 protein specifically. Transfer is strong (close relative, same enzyme family) but remains inference.
- **β-alanine supply route is inferred:** the pyrimidine-catabolism hypothesis for compensating the absent panD is based on gene presence, not on demonstrated flux. It is plausible that KT2440 acquires β-alanine from the environment or from another undetermined route.
- **PP_2325 / PP_2998 substrate specificity** is unresolved — they are KPR-family but their true physiological substrates are uncharacterized.
- **Essentiality** of each locus in KT2440 was not tested here; CoA biosynthesis is essential in bacteria generally, but strain-specific transposon-fitness data were not incorporated.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Close the β-alanine gap:** query KT2440 transposon-insertion fitness / RB-TnSeq datasets for *pydB* (PP_4036), *hyuC* (PP_4034), and PP_0614 under minimal medium without β-alanine/pantothenate — auxotrophy or fitness defect would confirm the compensatory route for the missing panD.
2. **Correct annotations:** submit re-annotation for PP_4452 (opine dehydrogenase, remove EC 1.1.1.169) and soften PP_2325/PP_2998 to KPR-family.
3. **Confirm dfp bifunctionality:** heterologous expression + coupled assay of PP_5285 to verify both CoaB and CoaC activities reside in the single protein.
4. **Verify coaX CoA-insensitivity** biochemically for the KT2440 enzyme to formally retire the human feedback-regulation annotation for this taxon.
5. **Module document update:** rewrite the ppu00770 CoA-core module in EC/activity terms with the bacterial CoaX/CoaBC/CoaD/CoaE frame, splitting off the vitamin-B5 supply sub-module and excluding CoA-utilization genes (entD, acpH, mazG) and BCAA/pyrimidine-catabolism genes.

---

*Prepared for manual module satisfiability and gene-annotation curation. Evidence is explicitly labeled as direct (KT2440 proteome/InterPro) vs. transferred (Pseudomonas/generic bacterial). Overall determination: **CoA biosynthesis from pantothenate is COVERED in P. putida KT2440**, with a panD/β-alanine-supply lineage-specific alternative and an EC 1.1.1.169 over-annotation as the two actionable curation flags.*


## Artifacts

- [OpenScientist final report](PSEPK__coenzyme_a_biosynthesis__ppu00770-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__coenzyme_a_biosynthesis__ppu00770-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16855243
2. PMID:33420031