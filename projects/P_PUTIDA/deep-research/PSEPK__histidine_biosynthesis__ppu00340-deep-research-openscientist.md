---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T03:58:48.515427'
end_time: '2026-07-17T04:54:43.769503'
duration_seconds: 3355.25
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-histidine biosynthesis (microbial)
  module_summary: 'De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose
    1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten
    enzymatic activities that is broadly conserved across bacteria, archaea, fungi,
    and plants, and is the canonical microbial route. The pathway is metabolically
    unusual in that its purine-like intermediates connect it to nucleotide metabolism:
    the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide
    ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring
    of ATP back into the nucleotide pool. Several activities are commonly fused or
    bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase,
    and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in
    enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two
    successive NAD+-dependent oxidations through a histidinal intermediate. The pathway
    is energetically expensive and is tightly regulated, classically by feedback inhibition
    of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.'
  module_outline: "- L-histidine biosynthesis\n  - 1. PRPP supply (shared, not histidine-specific)\n\
    \  - Ribose-5-phosphate to PRPP\n    - prs: ribose-phosphate diphosphokinase (molecular\
    \ player: ribose phosphate diphosphokinase activity; activity or role: ribose\
    \ phosphate diphosphokinase activity)\n  - 2. first committed step\n  - PRPP to\
    \ phosphoribosyl-ATP\n    - hisG: ATP phosphoribosyltransferase (molecular player:\
    \ ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase\
    \ activity)\n  - 3. pyrophosphohydrolase (often HisIE bifunctional)\n  - Phosphoribosyl-ATP\
    \ to phosphoribosyl-AMP\n    - hisI: phosphoribosyl-ATP diphosphatase (molecular\
    \ player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP\
    \ diphosphatase activity)\n  - 4. cyclohydrolase (often HisIE bifunctional)\n\
    \  - Phosphoribosyl-AMP to ProFAR\n    - hisE: phosphoribosyl-AMP cyclohydrolase\
    \ (molecular player: phosphoribosyl-AMP cyclohydrolase (HisE / HisIE); activity\
    \ or role: phosphoribosyl-AMP cyclohydrolase activity)\n  - 5. amino-isomerase\n\
    \  - ProFAR to PRFAR\n    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide\
    \ isomerase activity; activity or role: ProFAR isomerase activity)\n  - 6. imidazole-glycerol-phosphate\
    \ synthase (glutamine amidotransferase)\n  - PRFAR to imidazole-glycerol-phosphate\
    \ + AICAR\n    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate\
    \ synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate\
    \ synthase activity)\n    - hisH: IGP synthase, glutamine amidotransferase subunit\
    \ (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit\
    \ HisH; activity or role: imidazoleglycerol-phosphate synthase activity)\n  -\
    \ 7. dehydratase\n  - IGP to imidazole-acetol phosphate\n    - hisB: imidazoleglycerol-phosphate\
    \ dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity;\
    \ activity or role: imidazoleglycerol-phosphate dehydratase activity)\n  - 8.\
    \ transaminase\n  - Imidazole-acetol phosphate to L-histidinol phosphate\n   \
    \ - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate\
    \ aminotransferase activity; activity or role: histidinol-phosphate aminotransferase\
    \ activity)\n  - 9. phosphatase\n  - L-histidinol phosphate to L-histidinol\n\
    \    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase\
    \ activity; activity or role: histidinol-phosphatase activity)\n  - 10. terminal\
    \ bifunctional dehydrogenase\n  - L-histidinol to L-histidine\n    - hisD: histidinol\
    \ dehydrogenase (molecular player: histidinol dehydrogenase activity; activity\
    \ or role: histidinol dehydrogenase activity)"
  module_connections: '- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP:
    PRPP from the diphosphokinase feeds the first committed step.

    - PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP

    - Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR

    - Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR

    - ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR

    - PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol
    phosphate

    - IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol
    phosphate

    - Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate
    to L-histidinol

    - L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine'
  pathway_query: ppu00340
  pathway_id: ppu00340
  pathway_name: Histidine metabolism
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00340 with 18 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '20'
  candidate_genes: '- gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2)
    (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket
    kegg:ppu00340)

    - hisB: PP_0289 | Q88R45 | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC
    4.2.1.19) (EC 4.2.1.19; primary bucket kegg:ppu00340)

    - hisH: PP_0290 | Q88R44 | Imidazole glycerol phosphate synthase subunit HisH
    (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP synthase subunit
    HisH) (ImGP synthase subunit HisH) (IGPS subunit HisH) (EC 3.5.1.2; 4.3.2.10;
    primary bucket kegg:ppu00340)

    - hisA: PP_0292 | Q88R42 | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]
    imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole
    carboxamide ribotide isomerase) (EC 5.3.1.16; primary bucket kegg:ppu00340)

    - hisF: PP_0293 | Q88R41 | Imidazole glycerol phosphate synthase subunit HisF
    (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit HisF) (ImGP
    synthase subunit HisF) (IGPS subunit HisF) (EC 4.3.2.10; primary bucket kegg:ppu00340)

    - hisG: PP_0965 | Q88P87 | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase)
    (EC 2.4.2.17) (EC 2.4.2.17; primary bucket kegg:ppu00340)

    - hisD: PP_0966 | P59400 | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) (EC 1.1.1.23;
    primary bucket kegg:ppu00340)

    - hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9)
    (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)

    - PP_1721: PP_1721 | Q88M53 | Phosphoserine phosphatase (EC 3.1.3.-) (EC 3.1.3.-;
    primary bucket kegg:ppu00340)

    - PP_3157: PP_3157 | Q88I44 | Histidinol-phosphatase (EC 3.1.3.15) (EC 3.1.3.15;
    primary bucket kegg:ppu00340)

    - hisZ: PP_4890 | Q88DD7 | ATP phosphoribosyltransferase regulatory subunit (primary
    bucket kegg:ppu00340)

    - PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3;
    primary bucket kegg:ppu00350)

    - hisI: PP_5014 | Q88D15 | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19)
    (EC 3.5.4.19; primary bucket kegg:ppu00340)

    - hisE: PP_5015 | Q88D14 | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31)
    (EC 3.6.1.31; primary bucket kegg:ppu00340)

    - hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68;
    primary bucket kegg:ppu00340)

    - hutI: PP_5030 | Q88CZ9 | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate
    hydrolase) (EC 3.5.2.7; primary bucket kegg:ppu00340)

    - hutH: PP_5032 | Q88CZ7 | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) (EC
    4.3.1.3; primary bucket kegg:ppu00340)

    - hutU: PP_5033 | Q88CZ6 | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate
    hydrolase) (EC 4.2.1.49; primary bucket kegg:ppu00340)

    - hutF: PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase (EC 3.5.3.13) (EC 3.5.3.13;
    primary bucket kegg:ppu00340)

    - PP_5147: PP_5147 | Q88CN3 | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate
    phosphatase) (EC 3.1.3.15; primary bucket kegg:ppu00340)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__histidine_biosynthesis__ppu00340-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__histidine_biosynthesis__ppu00340-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-histidine biosynthesis (microbial) in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00340
- Resolved ID: ppu00340
- Resolved name: Histidine metabolism
- Source: KEGG

Resolved local bucket kegg:ppu00340 with 18 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 20

- gshA: PP_0243 | Q88R90 | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) (EC 6.3.2.2; primary bucket kegg:ppu00340)
- hisB: PP_0289 | Q88R45 | Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19) (EC 4.2.1.19; primary bucket kegg:ppu00340)
- hisH: PP_0290 | Q88R44 | Imidazole glycerol phosphate synthase subunit HisH (EC 4.3.2.10) (IGP synthase glutaminase subunit) (EC 3.5.1.2) (IGP synthase subunit HisH) (ImGP synthase subunit HisH) (IGPS subunit HisH) (EC 3.5.1.2; 4.3.2.10; primary bucket kegg:ppu00340)
- hisA: PP_0292 | Q88R42 | 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (EC 5.3.1.16) (Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase) (EC 5.3.1.16; primary bucket kegg:ppu00340)
- hisF: PP_0293 | Q88R41 | Imidazole glycerol phosphate synthase subunit HisF (EC 4.3.2.10) (IGP synthase cyclase subunit) (IGP synthase subunit HisF) (ImGP synthase subunit HisF) (IGPS subunit HisF) (EC 4.3.2.10; primary bucket kegg:ppu00340)
- hisG: PP_0965 | Q88P87 | ATP phosphoribosyltransferase (ATP-PRT) (ATP-PRTase) (EC 2.4.2.17) (EC 2.4.2.17; primary bucket kegg:ppu00340)
- hisD: PP_0966 | P59400 | Histidinol dehydrogenase (HDH) (EC 1.1.1.23) (EC 1.1.1.23; primary bucket kegg:ppu00340)
- hisC: PP_0967 | Q88P86 | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) (EC 2.6.1.9; primary bucket kegg:ppu00401)
- PP_1721: PP_1721 | Q88M53 | Phosphoserine phosphatase (EC 3.1.3.-) (EC 3.1.3.-; primary bucket kegg:ppu00340)
- PP_3157: PP_3157 | Q88I44 | Histidinol-phosphatase (EC 3.1.3.15) (EC 3.1.3.15; primary bucket kegg:ppu00340)
- hisZ: PP_4890 | Q88DD7 | ATP phosphoribosyltransferase regulatory subunit (primary bucket kegg:ppu00340)
- PP_4983: PP_4983 | Q88D45 | Tryptophan 2-monooxygenase (EC 1.13.12.3) (EC 1.13.12.3; primary bucket kegg:ppu00350)
- hisI: PP_5014 | Q88D15 | Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19) (EC 3.5.4.19; primary bucket kegg:ppu00340)
- hisE: PP_5015 | Q88D14 | Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31) (EC 3.6.1.31; primary bucket kegg:ppu00340)
- hutG: PP_5029 | Q88D00 | N-formylglutamate deformylase (EC 3.5.1.68) (EC 3.5.1.68; primary bucket kegg:ppu00340)
- hutI: PP_5030 | Q88CZ9 | Imidazolonepropionase (EC 3.5.2.7) (Imidazolone-5-propionate hydrolase) (EC 3.5.2.7; primary bucket kegg:ppu00340)
- hutH: PP_5032 | Q88CZ7 | Histidine ammonia-lyase (Histidase) (EC 4.3.1.3) (EC 4.3.1.3; primary bucket kegg:ppu00340)
- hutU: PP_5033 | Q88CZ6 | Urocanate hydratase (Urocanase) (EC 4.2.1.49) (Imidazolonepropionate hydrolase) (EC 4.2.1.49; primary bucket kegg:ppu00340)
- hutF: PP_5036 | Q88CZ3 | Formimidoylglutamate deiminase (EC 3.5.3.13) (EC 3.5.3.13; primary bucket kegg:ppu00340)
- PP_5147: PP_5147 | Q88CN3 | Histidinol-phosphatase (EC 3.1.3.15) (Histidinol-phosphate phosphatase) (EC 3.1.3.15; primary bucket kegg:ppu00340)

## Generic Module Context

### Working Scope

De novo biosynthesis of L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) and ATP. This is an ancient, largely linear pathway of ten enzymatic activities that is broadly conserved across bacteria, archaea, fungi, and plants, and is the canonical microbial route. The pathway is metabolically unusual in that its purine-like intermediates connect it to nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring of ATP back into the nucleotide pool. Several activities are commonly fused or bifunctional in microbes (e.g. the HisIE pyrophosphohydrolase/cyclohydrolase, and the HisB dehydratase fused to a histidinol-phosphate phosphatase domain in enteric bacteria), and the terminal HisD histidinol dehydrogenase performs two successive NAD+-dependent oxidations through a histidinal intermediate. The pathway is energetically expensive and is tightly regulated, classically by feedback inhibition of the first committed enzyme (ATP phosphoribosyltransferase, HisG) by L-histidine.

### Provisional Biological Outline

- L-histidine biosynthesis
  - 1. PRPP supply (shared, not histidine-specific)
  - Ribose-5-phosphate to PRPP
    - prs: ribose-phosphate diphosphokinase (molecular player: ribose phosphate diphosphokinase activity; activity or role: ribose phosphate diphosphokinase activity)
  - 2. first committed step
  - PRPP to phosphoribosyl-ATP
    - hisG: ATP phosphoribosyltransferase (molecular player: ATP phosphoribosyltransferase activity; activity or role: ATP phosphoribosyltransferase activity)
  - 3. pyrophosphohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-ATP to phosphoribosyl-AMP
    - hisI: phosphoribosyl-ATP diphosphatase (molecular player: phosphoribosyl-ATP diphosphatase activity; activity or role: phosphoribosyl-ATP diphosphatase activity)
  - 4. cyclohydrolase (often HisIE bifunctional)
  - Phosphoribosyl-AMP to ProFAR
    - hisE: phosphoribosyl-AMP cyclohydrolase (molecular player: phosphoribosyl-AMP cyclohydrolase (HisE / HisIE); activity or role: phosphoribosyl-AMP cyclohydrolase activity)
  - 5. amino-isomerase
  - ProFAR to PRFAR
    - hisA: ProFAR isomerase (molecular player: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]imidazole-4-carboxamide isomerase activity; activity or role: ProFAR isomerase activity)
  - 6. imidazole-glycerol-phosphate synthase (glutamine amidotransferase)
  - PRFAR to imidazole-glycerol-phosphate + AICAR
    - hisF: IGP synthase, cyclase subunit (molecular player: imidazole-glycerol-phosphate synthase cyclase subunit HisF; activity or role: imidazoleglycerol-phosphate synthase activity)
    - hisH: IGP synthase, glutamine amidotransferase subunit (molecular player: imidazole-glycerol-phosphate synthase amidotransferase subunit HisH; activity or role: imidazoleglycerol-phosphate synthase activity)
  - 7. dehydratase
  - IGP to imidazole-acetol phosphate
    - hisB: imidazoleglycerol-phosphate dehydratase (molecular player: imidazoleglycerol-phosphate dehydratase activity; activity or role: imidazoleglycerol-phosphate dehydratase activity)
  - 8. transaminase
  - Imidazole-acetol phosphate to L-histidinol phosphate
    - hisC: histidinol-phosphate aminotransferase (molecular player: histidinol-phosphate aminotransferase activity; activity or role: histidinol-phosphate aminotransferase activity)
  - 9. phosphatase
  - L-histidinol phosphate to L-histidinol
    - hisN: histidinol-phosphate phosphatase (molecular player: histidinol-phosphatase activity; activity or role: histidinol-phosphatase activity)
  - 10. terminal bifunctional dehydrogenase
  - L-histidinol to L-histidine
    - hisD: histidinol dehydrogenase (molecular player: histidinol dehydrogenase activity; activity or role: histidinol dehydrogenase activity)

### Known Relationships Among Steps

- Ribose-5-phosphate to PRPP feeds into PRPP to phosphoribosyl-ATP: PRPP from the diphosphokinase feeds the first committed step.
- PRPP to phosphoribosyl-ATP precedes Phosphoribosyl-ATP to phosphoribosyl-AMP
- Phosphoribosyl-ATP to phosphoribosyl-AMP precedes Phosphoribosyl-AMP to ProFAR
- Phosphoribosyl-AMP to ProFAR precedes ProFAR to PRFAR
- ProFAR to PRFAR precedes PRFAR to imidazole-glycerol-phosphate + AICAR
- PRFAR to imidazole-glycerol-phosphate + AICAR precedes IGP to imidazole-acetol phosphate
- IGP to imidazole-acetol phosphate precedes Imidazole-acetol phosphate to L-histidinol phosphate
- Imidazole-acetol phosphate to L-histidinol phosphate precedes L-histidinol phosphate to L-histidinol
- L-histidinol phosphate to L-histidinol precedes L-histidinol to L-histidine

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

# Module/Pathway/Taxon Review: L-Histidine Biosynthesis in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu00340` "Histidine metabolism" → de novo L-histidine biosynthesis module (KEGG M00026, PRPP ⇒ histidine)
**Module area:** amino_acid_metabolism
**Scope of this review:** de novo L-histidine biosynthesis only (10 catalytic activities from PRPP + ATP to L-histidine)

---

## 1. Executive Summary

De novo L-histidine biosynthesis is **fully satisfiable** in *Pseudomonas putida* KT2440. All ten canonical catalytic activities that convert 5-phospho-α-D-ribose-1-diphosphate (PRPP) and ATP into L-histidine are encoded by identifiable candidate genes, with clean one-to-one KEGG Orthology (KO) and EC-number assignments for every biosynthetic step. The first committed step is present as a short-form ATP phosphoribosyltransferase (HisG, PP_0965) paired with a dedicated regulatory subunit (HisZ, PP_4890), the classic HisG/HisZ feedback-control architecture. The bifunctional imidazole-glycerol-phosphate synthase is split across HisF (PP_0293) and HisH (PP_0290); the amino-isomerase HisA (PP_0292), the dehydratase HisB (PP_0289), the aminotransferase HisC (PP_0967), and the terminal bifunctional dehydrogenase HisD (PP_0966) are all present; and the pyrophosphohydrolase/cyclohydrolase pair HisE (PP_5015) and HisI (PP_5014) covers the early steps.

The single genuine ambiguity is **step 8, histidinol-phosphate phosphatase (HolPase / HisN, EC 3.1.3.15)**. *P. putida* lacks the enteric bifunctional HisB (IGPD fused to a HAD-family phosphatase domain), so the phosphatase activity must be supplied by a stand-alone enzyme. Three paralogous loci carry HolPase-like annotations — PP_3157, PP_1721, and PP_5147 — and only one is the true HisN. Protein-family evidence resolves this cleanly: **PP_3157 belongs to the inositol-monophosphatase (IMPase) "his9" superfamily** that is the canonical non-enteric HolPase fold, carries the UniProt "Histidine biosynthesis" keyword and an explicit L-histidine-biosynthesis pathway assignment, and is corroborated by its GenBank product name ("Inositol monophosphatase family protein"). By contrast, PP_1721 and PP_5147 both belong to the HAD-like SerB family; PP_1721 is most likely a phosphoserine phosphatase (*serB*), and PP_5147 is a HAD hydrolase over-annotated with EC 3.1.3.15 but lacking the histidine-biosynthesis keyword. **PP_3157 should be curated as HisN; PP_1721 and PP_5147 should be excluded from the module.**

Finally, the parent KEGG bucket `ppu00340` conflates three distinct biological processes and **over-reaches** relative to the biosynthesis module. Seven candidate genes are catabolic or peripheral and should be excluded: the five histidine-utilization (*hut*) genes (hutH, hutU, hutI, hutF, hutG) that degrade histidine to glutamate, the glutathione-biosynthesis gene *gshA* (PP_0243), and PP_4983 (an amine oxidase mislabeled in local metadata as tryptophan 2-monooxygenase). All *his*-gene calls in this organism are **homology-inferred (UniProt PE=3)**; no in-strain biochemical or genetic validation of the histidine biosynthetic pathway exists for KT2440 itself.

---

## 2. Target-Organism Pathway Definition

### What is included

The module scope is **de novo biosynthesis of L-histidine from PRPP and ATP** — the ten-activity linear route conserved across bacteria, archaea, fungi, and plants (KEGG module **M00026**, "Histidine biosynthesis, PRPP ⇒ histidine"). In *P. putida* KT2440 this corresponds to the biosynthetic subset of KEGG map `ppu00340`. The pathway is metabolically distinctive because its purine-like intermediates connect it to nucleotide metabolism: the imidazole-glycerol-phosphate synthase step releases AICAR (5-aminoimidazole-4-carboxamide ribonucleotide), a purine-biosynthesis intermediate, recycling the adenine ring of ATP back into the nucleotide pool.

### What must be kept separate

The KEGG map `ppu00340` "Histidine metabolism" is a broad overview map that mixes **three processes** that should not be co-curated into one biosynthesis module:

1. **De novo biosynthesis** (the *his* genes) — the target module.
2. **Histidine catabolism / utilization** (the *hut* genes): a five-step degradation route (histidase → urocanase → imidazolonepropionase → formimidoylglutamate deiminase → N-formylglutamate deformylase) that converts histidine to glutamate for use as a carbon and nitrogen source. This is a catabolic locus, functionally opposite to biosynthesis.
3. **Peripheral / cross-listed reactions**: *gshA* (glutamate–cysteine ligase, glutathione biosynthesis) and PP_4983 (an amine oxidase). These appear on the overview map for chemical-neighborhood reasons, not because they participate in histidine biosynthesis.

Upstream **PRPP supply** (ribose-5-phosphate → PRPP, catalyzed by *prs* ribose-phosphate diphosphokinase) is shared central metabolism, not histidine-specific, and is correctly **outside** the candidate list and the module scope.

### Alternate names / database definitions

- **KEGG:** map/module `ppu00340` (Histidine metabolism) and module `M00026` (Histidine biosynthesis, PRPP ⇒ histidine).
- **MetaCyc/BioCyc:** "L-histidine biosynthesis" (HISTSYN-PWY).
- **HisN nomenclature caveat:** the dedicated histidinol-phosphate phosphatase has been given at least three independent enzyme solutions across bacteria (enteric bifunctional HisB; PHP-family; IMPase/"his9" family). The gene symbol *hisN* was coined for the IMPase-type HolPase in *Corynebacterium glutamicum* ([PMID: 16901339](https://pubmed.ncbi.nlm.nih.gov/16901339/)).

---

## 3. Expected Step Model

The canonical ten-activity model, mapped to *P. putida* KT2440 candidate genes:

| Step | Reaction | Activity (EC) | Expected gene | KT2440 locus | KO | Call |
|------|----------|---------------|---------------|--------------|----|------|
| 0 | R5P → PRPP | ribose-P diphosphokinase (2.7.6.1) | *prs* | (not in candidate list; shared metabolism) | K00948 | out of scope |
| 1 | PRPP → PR-ATP | ATP phosphoribosyltransferase (2.4.2.17) | *hisG* (+*hisZ*) | PP_0965 (+PP_4890) | K00765 (+K02502) | **covered** |
| 2 | PR-ATP → PR-AMP | phosphoribosyl-ATP pyrophosphohydrolase (3.6.1.31) | *hisE* | PP_5015 | K01523 | **covered** |
| 3 | PR-AMP → ProFAR | phosphoribosyl-AMP cyclohydrolase (3.5.4.19) | *hisI* | PP_5014 | K01496 | **covered** |
| 4 | ProFAR → PRFAR | ProFAR isomerase (5.3.1.16) | *hisA* | PP_0292 | K01814 | **covered** |
| 5 | PRFAR → IGP + AICAR | IGP synthase (4.3.2.10) | *hisF* + *hisH* | PP_0293 + PP_0290 | K02500 + K02501 | **covered** |
| 6 | IGP → IAP | IGP dehydratase (4.2.1.19) | *hisB* | PP_0289 | K01693 | **covered** |
| 7 | IAP → L-His-P | histidinol-P aminotransferase (2.6.1.9) | *hisC* | PP_0967 | K00817 | **covered** |
| 8 | L-His-P → L-histidinol | histidinol-P phosphatase (3.1.3.15) | *hisN* | **PP_3157** | K05602 | **covered (resolved)** |
| 9 | L-histidinol → L-histidine | histidinol dehydrogenase (1.1.1.23) | *hisD* | PP_0966 | K00013 | **covered** |

*(Step numbering follows the biological order; UniProt's internal "step X/9" numbering differs by one because it collapses the PRPP-supply step.)*

**Nomenclature note (module_needs_revision, minor):** the generic module outline inverts the HisE/HisI labels. Standard nomenclature is **HisE = phosphoribosyl-ATP pyrophosphohydrolase (EC 3.6.1.31)** acting first, and **HisI = phosphoribosyl-AMP cyclohydrolase (EC 3.5.4.19)** acting second. The provided outline labels step 3 "hisI diphosphatase" and step 4 "hisE cyclohydrolase," which is backwards. The *P. putida* loci themselves are correctly annotated (PP_5015 = HisE/EC 3.6.1.31; PP_5014 = HisI/EC 3.5.4.19); only the generic outline text needs the label swap.

```
PRPP ──hisG(PP_0965)+hisZ(PP_4890)──▶ PR-ATP
      ──hisE(PP_5015)──▶ PR-AMP ──hisI(PP_5014)──▶ ProFAR
      ──hisA(PP_0292)──▶ PRFAR ──hisF(PP_0293)+hisH(PP_0290)──▶ IGP (+AICAR→purine pool)
      ──hisB(PP_0289)──▶ IAP ──hisC(PP_0967)──▶ L-His-P
      ──hisN(PP_3157)──▶ L-histidinol ──hisD(PP_0966)──▶ L-HISTIDINE
```

---

## 4. Candidate Genes and Evidence

### High-confidence biosynthetic genes (covered)

**hisG — PP_0965 (Q88P87), ATP phosphoribosyltransferase, EC 2.4.2.17, K00765.** The first committed step. KEGG module M00026 encodes this step as the paired block **K00765–K02502**, i.e., a short-form catalytic HisG that requires the HisZ regulatory subunit. Evidence: homology (PE=3). Curation note: retain; expect HisZ-dependent activity and feedback control.

**hisZ — PP_4890 (Q88DD7), ATP-PRT regulatory subunit, K02502.** HisZ is a catalytically inactive paralog of histidyl-tRNA synthetase that partners with short-form HisG to form the active hetero-oligomeric ATP-PRT and confers L-histidine feedback inhibition on the complex. Its presence alongside a short-form HisG is internally consistent and the expected architecture. Evidence: homology. Curation note: retain as a required accessory subunit of step 1 (not an independent catalytic step).

**hisE — PP_5015 (Q88D14), phosphoribosyl-ATP pyrophosphohydrolase, EC 3.6.1.31, K01523.** Step 2. Evidence: homology (PE=3). Curation note: covered.

**hisI — PP_5014 (Q88D15), phosphoribosyl-AMP cyclohydrolase, EC 3.5.4.19, K01496.** Step 3. *hisI* and *hisE* are adjacent (PP_5014/PP_5015), consistent with the common HisIE gene neighborhood, though here annotated as separate monofunctional genes rather than a fusion. Evidence: homology (PE=3). Curation note: covered.

**hisA — PP_0292 (Q88R42), ProFAR isomerase, EC 5.3.1.16, K01814.** Step 4. Sits in the main biosynthetic cluster PP_0289–PP_0293. Evidence: homology. Curation note: covered.

**hisF — PP_0293 (Q88R41), IGP synthase cyclase subunit, EC 4.3.2.10, K02500; and hisH — PP_0290 (Q88R44), IGP synthase glutamine-amidotransferase subunit, EC 4.3.2.10 (+3.5.1.2), K02501.** Step 5, the two-subunit imidazole-glycerol-phosphate synthase. Both present in the PP_0289–PP_0293 cluster. Evidence: homology. Curation note: covered as an obligate heterodimer.

**hisB — PP_0289 (Q88R45), imidazoleglycerol-phosphate dehydratase, EC 4.2.1.19, K01693.** Step 6. Critically, in *P. putida* this is a **monofunctional IGPD** (dehydratase domain only), NOT the enteric bifunctional HisB that also carries a HAD-family HolPase domain. This is precisely why *P. putida* needs a separate HisN for step 8. Evidence: homology. Curation note: covered; flag as monofunctional.

**hisC — PP_0967 (Q88P86), histidinol-phosphate aminotransferase, EC 2.6.1.9, K00817.** Step 7. Local metadata lists its primary bucket as `ppu00401`, but this is only a secondary cross-listing of the promiscuous aminotransferase on another map; the UniProt "Histidine biosynthesis" keyword and internal pathway step (7/9) confirm this is the genuine histidine HisC. Curation note: covered; retain despite the ppu00401 bucket label.

**hisD — PP_0966 (P59400), histidinol dehydrogenase, EC 1.1.1.23, K00013.** Terminal step, the bifunctional NAD⁺-dependent dehydrogenase that performs two successive oxidations (histidinol → histidinal → histidine). This is the only candidate with a Swiss-Prot (reviewed) accession (P59400), though still PE=3. Adjacent to hisG (PP_0965) and hisC (PP_0967). Curation note: covered.

### The resolved ambiguous step — HisN (step 8)

**hisN — PP_3157 (Q88I44), histidinol-phosphate phosphatase, EC 3.1.3.15, K05602 — HIGH CONFIDENCE.** *P. putida* lacks a bifunctional HisB HolPase domain, so a stand-alone HolPase is required. Three paralogs are annotated with EC 3.1.3.15 (see §5), but PP_3157 is the strongest candidate on protein-family grounds: it belongs to the **inositol-monophosphatase (IMPase) superfamily** — InterPro IPR000760 (IMPase-like), IPR011809 ("Histidinol-phosphatase His_9, proposed"), Pfam PF00459 (Inositol_P) — carries UniProt keywords "Histidine biosynthesis" / "Amino-acid biosynthesis" and an explicit L-histidine-biosynthesis pathway/step assignment, and its GenBank product name is "Inositol monophosphatase family protein." The IMPase "his9" fold is the canonical non-enteric HolPase family established in *Corynebacterium glutamicum* and Actinobacteria ([PMID: 16901339](https://pubmed.ncbi.nlm.nih.gov/16901339/); [PMID: 28720084](https://pubmed.ncbi.nlm.nih.gov/28720084/)). Curation note: **assign as HisN; promote to full fetch-gene review.**

### Out-of-module candidates (not_expected_in_target_taxon for a biosynthesis module)

| Gene | Locus | Annotation | KO/EC | Why excluded |
|------|-------|-----------|-------|--------------|
| hutH | PP_5032 | histidine ammonia-lyase (histidase) | K01745 / 4.3.1.3 | catabolism (His degradation) |
| hutU | PP_5033 | urocanate hydratase (urocanase) | K01712 / 4.2.1.49 | catabolism |
| hutI | PP_5030 | imidazolonepropionase | K01468 / 3.5.2.7 | catabolism |
| hutF | PP_5036 | formimidoylglutamate deiminase | K05603 / 3.5.3.13 | catabolism |
| hutG | PP_5029 | N-formylglutamate deformylase | K01458 / 3.5.1.68 | catabolism |
| gshA | PP_0243 | glutamate–cysteine ligase | K01919 / 6.3.2.2 | glutathione biosynthesis (peripheral) |
| PP_4983 | PP_4983 | amine oxidase (locally mislabeled Trp 2-monooxygenase) | K00274 / 1.4.3.4 | peripheral; local EC 1.13.12.3 likely wrong |

The *hut* genes cluster at PP_5029–PP_5036 and constitute the catabolic histidine-utilization locus, functionally the reverse of biosynthesis ([PMID: 17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/)).

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

### The HolPase paralog problem (the central curation decision)

Three loci carry EC 3.1.3.15 (or related phosphatase) annotations. Only one is the true HisN. This is exactly the over-propagation hazard flagged by Kulis-Horn et al.: IMPase-like paralogs (CysQ, ImpA, SuhB) are highly similar to HisN yet do not perform HolPase in vivo ([PMID: 28720084](https://pubmed.ncbi.nlm.nih.gov/28720084/)).

| Locus | Family (InterPro/Pfam) | GenBank product | UniProt "His biosynthesis" kw | Genomic neighborhood | Verdict |
|-------|------------------------|-----------------|:---:|----------------------|---------|
| **PP_3157** (Q88I44) | IMPase superfamily; IPR000760 / IPR011809 (His_9) / PF00459 | "Inositol monophosphatase family protein" | **Yes** + pathway assignment | isolated (nbrs: universal-stress PP_3156, exported protein PP_3158) | **true HisN** |
| PP_5147 (Q88CN3) | HAD-like SerB; IPR006385 / IPR050582 / PF12710 | "Hydrolase, haloacid dehalogenase-like family" | No | nbrs RNA pyrophosphohydrolase PP_5146, membrane protein PP_5148 | HAD over-annotation |
| PP_1721 (Q88M53) | HAD-like SerB; IPR006385 / IPR050582 / PF12710 | "putative phosphoserine phosphatase" | No (PE=4 Predicted; blank protein name) | nbrs Zn-ADH PP_1720, ABC transporter PP_1722 | likely *serB*, not HolPase |

The two decisive discriminators are (1) **protein fold** — PP_3157 is IMPase/his9 (the bona fide non-enteric HolPase fold), whereas PP_5147 and PP_1721 are HAD-SerB; and (2) **the UniProt "Histidine biosynthesis" keyword plus explicit pathway assignment**, which only PP_3157 carries. Dispersal of PP_3157 away from the *his* clusters is expected and normal for IMPase-type HisN, which is typically not co-located with the biosynthetic operon. Two independent annotation sources (UniProt InterPro families and KEGG/GenBank product names) agree.

**Curation actions:** PP_5147 → mark `candidate_uncertain` / likely over-annotation (HAD hydrolase; strip the histidine-biosynthesis inference). PP_1721 → re-annotate as *serB* (phosphoserine phosphatase); remove from the histidine module.

### Local-metadata errors flagged for correction

- **PP_4983** is labeled "Tryptophan 2-monooxygenase (EC 1.13.12.3)" in local metadata, but KEGG assigns K00274 (monoamine oxidase, EC 1.4.3.4). Peripheral regardless; reconcile the EC to the KEGG call and exclude from the histidine module.
- **PP_1721** local annotation "Phosphoserine phosphatase (EC 3.1.3.-)" is consistent with the SerB re-assignment — the local EC 3.1.3.- (not 3.1.3.15) already hints it is not a dedicated HolPase.
- **Generic outline HisE/HisI label inversion** (see §3): a documentation fix, not a gene-level error.

### Evidence-level gap

Every *his* candidate is **UniProt PE=3 (inferred from homology)**. There is no direct biochemical or genetic characterization of the histidine biosynthetic pathway in KT2440 itself. All calls rest on sequence homology, KO/EC transfer, and protein-family membership.

---

## 6. Module and GO-Curation Recommendations

### Per-step module status

| Module step | Status | Gene(s) |
|-------------|--------|---------|
| 1 ATP-PRT (HisG + HisZ) | **covered** | PP_0965 (+ PP_4890) |
| 2 PR-ATP pyrophosphohydrolase (HisE) | **covered** | PP_5015 |
| 3 PR-AMP cyclohydrolase (HisI) | **covered** | PP_5014 |
| 4 ProFAR isomerase (HisA) | **covered** | PP_0292 |
| 5 IGP synthase (HisF + HisH) | **covered** | PP_0293 + PP_0290 |
| 6 IGP dehydratase (HisB, monofunctional) | **covered** | PP_0289 |
| 7 HolP aminotransferase (HisC) | **covered** | PP_0967 |
| 8 HolPase (HisN) | **covered (resolved by fold evidence)** | PP_3157 |
| 9 histidinol dehydrogenase (HisD) | **covered** | PP_0966 |
| — HolPase paralogs | **candidate_uncertain / exclude** | PP_5147, PP_1721 |
| — *hut* catabolism (×5), *gshA*, PP_4983 | **not_expected_in_target_taxon** | PP_5029/30/32/33/36, PP_0243, PP_4983 |

**Overall module verdict: fully covered, 10/10 catalytic steps satisfied.**

### Module boundary and document recommendations

1. **Split the bucket.** The generic module boundary that inherits all of `ppu00340` is wrong for a biosynthesis module. Recommend a dedicated biosynthesis module (M00026-equivalent) containing only PP_0965, PP_4890, PP_5015, PP_5014, PP_0292, PP_0293, PP_0290, PP_0289, PP_0967, PP_3157, PP_0966. The *hut* catabolic locus warrants its own separate catabolism module.
2. **Fix the HisE/HisI outline labels** (module_needs_revision, minor/documentation).
3. **GO curation for PP_3157:** support annotation to GO:0004401 (histidinol-phosphatase activity) and GO:0000105 (histidine biosynthetic process). Because the assignment is homology-based, use evidence code **IEA/ISS**, not experimental codes.
4. **GO down-annotation for PP_5147 and PP_1721:** remove or qualify GO:0004401; PP_1721 should carry GO:0004647 (phosphoserine phosphatase activity) / serine biosynthesis.
5. **No new GO terms appear necessary** — the required terms (histidinol-phosphatase activity; histidine biosynthetic process; ATP-PRT regulatory activity for HisZ) already exist.

---

## 7. Genes to Promote to Full `fetch-gene` Review

1. **PP_3157 (HisN) — highest priority.** The one step resolved by inference rather than a named dedicated gene. A full review should confirm the IMPase/his9 active-site residues, verify it is not a CysQ/ImpA/SuhB-type IMPase with a different substrate, and (ideally) seek experimental or structural evidence. This is the linchpin of module satisfiability.
2. **PP_1721 and PP_5147 — paired disambiguation review.** Confirm PP_1721 = *serB* and PP_5147 = generic HAD hydrolase, and formally strip their HolPase over-annotations.
3. **PP_4983 — EC reconciliation.** Resolve the tryptophan-2-monooxygenase (local) vs. monoamine-oxidase (KEGG) discrepancy; confirm exclusion from the histidine module.
4. **PP_0965 / PP_4890 (HisG/HisZ pair).** Lower priority; confirm the short-form HisG requires HisZ and document the feedback-regulation architecture.

The remaining core *his* genes (PP_5015, PP_5014, PP_0292, PP_0293, PP_0290, PP_0289, PP_0967, PP_0966) have clean, unambiguous KO/EC/keyword assignments and do not need individual promotion unless the module is being upgraded from IEA to experimental evidence.

---

## 8. Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the review |
|------|-----------------|----------|----------------------------|
| [16901339](https://pubmed.ncbi.nlm.nih.gov/16901339/) | *IS6100 transposon mutagenesis identifies the last His gene in C. glutamicum* | *C. glutamicum* | Established that the IMPase-like gene (cg0910, renamed **hisN**) is the missing HolPase (EC 3.1.3.15) in a non-enteric bacterium — the precedent for assigning an IMPase-fold gene (PP_3157) as HisN. Direct experimental evidence; species transfer moderate (same fold family, different genus). |
| [28720084](https://pubmed.ncbi.nlm.nih.gov/28720084/) | *Sequence-based identification of IMPase-like HisN in C. glutamicum, Actinobacteria, and beyond* | Actinobacteria + survey | Defines the IMPase/"his9" HolPase family and **explicitly warns that IMPase paralogs (CysQ, ImpA, SuhB) are very similar to HisN but most likely do not participate in histidine biosynthesis** — the exact over-propagation hazard motivating disambiguation of PP_3157 vs. PP_5147/PP_1721. |
| [17717196](https://pubmed.ncbi.nlm.nih.gov/17717196/) | *Genetic analysis of the hut genes in P. fluorescens SBW25* | *P. fluorescens* | Shows the **hut locus is catabolic** (histidine as sole C/N source), supporting exclusion of hutH/U/I/F/G from the biosynthesis module. Species transfer to *P. putida*: strong (same genus, orthologous locus). |
| [9561727](https://pubmed.ncbi.nlm.nih.gov/9561727/) | *hut operon upregulated at low temperature in P. syringae* | *P. syringae* (+ *P. putida* assays) | Confirms *hut* genes (hutU urocanase, histidase) are a regulated catabolic operon in pseudomonads, including direct enzyme assays in *P. putida* — reinforces the biosynthesis/catabolism split. |
| [2203754](https://pubmed.ncbi.nlm.nih.gov/2203754/) | *hutC repressor sequence, K. aerogenes* (with P. putida comparison) | *K. aerogenes* / *P. putida* | Documents *hut* operon regulation and the *P. putida hutC* repressor, corroborating that the *hut* genes form a distinct regulated catabolic system. |

**Direct vs. inferred evidence summary:** No cited study characterizes the *P. putida* KT2440 histidine **biosynthetic** genes directly. The strongest experimental anchor (PMID 16901339) is the *C. glutamicum* HisN identification, transferred by fold homology. The *hut*/catabolism exclusions are supported by direct genus-level experiments (PMIDs 17717196, 9561727, 2203754). All histidine biosynthetic assignments in KT2440 remain homology-inferred.

---

## 9. Limitations and Knowledge Gaps

- **No in-strain experimental validation.** All *his* candidates are UniProt PE=3 (inferred from homology). There is no published biochemical assay, knockout auxotrophy, or structure for any KT2440 histidine biosynthetic enzyme. Module satisfiability is therefore an inference, albeit a strong one.
- **HisN rests on fold + keyword inference, not function.** PP_3157 is the best candidate, but the assignment relies on IMPase/his9 family membership and UniProt keywords rather than a demonstrated HolPase activity in *P. putida*. A CysQ/ImpA/SuhB-type false positive cannot be fully excluded without functional data (the caution raised by PMID 28720084).
- **Regulatory architecture unverified.** The HisG(short)/HisZ feedback model is inferred from the KO pairing (K00765–K02502); *P. putida* HisZ-dependence and histidine feedback inhibition have not been demonstrated in-strain.
- **Local-metadata inconsistencies** (PP_4983 EC label; PP_1721 annotation; generic HisE/HisI outline inversion) indicate the source metadata is imperfect and should not be treated as ground truth.
- **PRPP flux/regulation** (upstream *prs*) and the AICAR-recycling link to purine metabolism were not analyzed quantitatively; they are out of module scope but relevant to any flux-based satisfiability claim.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Functional confirmation of PP_3157 as HisN.** Construct a PP_3157 deletion in KT2440 and test for histidine auxotrophy rescuable by histidinol (the assay design that identified *C. glutamicum hisN*, PMID 16901339). Complement in a HolPase-deficient *E. coli/C. glutamicum* background. This is the single most valuable experiment for the module.
2. **In vitro HolPase assay** on purified PP_3157 (with PP_5147 and PP_1721 as negative controls) against L-histidinol-phosphate to directly measure EC 3.1.3.15 activity and rule out IMPase off-target activity.
3. **serB confirmation for PP_1721.** Test complementation of an *E. coli serB* mutant and/or serine auxotrophy to formally re-annotate PP_1721 and retire its HolPase label.
4. **Curation updates now (no experiment needed):** (a) assign PP_3157 = HisN with GO:0004401/GO:0000105 (IEA/ISS); (b) exclude PP_5147, PP_1721 from the histidine module and re-annotate PP_1721 as serB; (c) split the biosynthesis module from the *hut* catabolism genes and *gshA*/PP_4983; (d) fix the generic-outline HisE/HisI label inversion; (e) reconcile the PP_4983 EC number to KEGG K00274.
5. **HisG/HisZ regulation.** Enzyme assay of the reconstituted PP_0965/PP_4890 complex ± L-histidine to confirm HisZ-dependent activity and feedback inhibition.

---

### Bottom line

De novo L-histidine biosynthesis is **fully satisfiable (10/10 steps)** in *P. putida* KT2440. The only non-trivial call — the stand-alone histidinol-phosphate phosphatase — resolves to **PP_3157 (IMPase/his9-family HisN)**, with PP_5147 and PP_1721 excluded as HAD/SerB over-annotations. The parent `ppu00340` bucket over-reaches and should be narrowed to exclude the *hut* catabolic genes, *gshA*, and PP_4983. All assignments are homology-based and would benefit from targeted experimental confirmation, most urgently a PP_3157 auxotrophy/complementation test.


## Artifacts

- [OpenScientist final report](PSEPK__histidine_biosynthesis__ppu00340-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__histidine_biosynthesis__ppu00340-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16901339
2. PMID:28720084
3. PMID:17717196