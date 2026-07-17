---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T13:38:47.082921'
end_time: '2026-07-17T14:00:39.067537'
duration_seconds: 1311.98
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: L-lysine biosynthesis by the succinylated diaminopimelate pathway
  module_summary: Bacterial L-lysine biosynthesis from L-aspartate 4-semialdehyde
    and pyruvate through the succinylated diaminopimelate route. DapA and DapB form
    and reduce the tetrahydrodipicolinate intermediate. DapD masks it by succinylation,
    DapC introduces the second amino group, and DapE removes the succinyl group. DapF
    converts LL-diaminopimelate to meso-diaminopimelate, and LysA performs the terminal
    decarboxylation to L-lysine. Aspartate kinase and aspartate-semialdehyde dehydrogenase
    provide a shared precursor used by lysine, threonine, and methionine synthesis
    and are outside the dedicated module boundary. The meso-diaminopimelate product
    also feeds peptidoglycan assembly before its conversion to lysine.
  module_outline: "- succinylated diaminopimelate pathway of L-lysine biosynthesis\n\
    \  - 1. committed diaminopimelate-ring formation\n  - Aspartate semialdehyde and\
    \ pyruvate to hydroxytetrahydrodipicolinate\n    - DapA hydroxytetrahydrodipicolinate\
    \ synthase (molecular player: DapA dihydrodipicolinate synthase family; activity\
    \ or role: 4-hydroxy-tetrahydrodipicolinate synthase activity)\n  - 2. tetrahydrodipicolinate\
    \ reduction\n  - Hydroxytetrahydrodipicolinate to tetrahydrodipicolinate\n   \
    \ - DapB hydroxytetrahydrodipicolinate reductase (molecular player: bacterial\
    \ DapB family; activity or role: 4-hydroxy-tetrahydrodipicolinate reductase activity)\n\
    \  - 3. tetrahydrodipicolinate succinylation\n  - Tetrahydrodipicolinate to N-succinyltetrahydrodipicolinate\n\
    \    - DapD tetrahydrodipicolinate N-succinyltransferase (molecular player: gammaproteobacterial\
    \ DapD family; activity or role: 2,3,4,5-tetrahydropyridine-2,6-dicarboxylate\
    \ N-succinyltransferase activity)\n  - 4. succinyldiaminopimelate transamination\n\
    \  - N-succinyl-2-amino-6-oxopimelate to N-succinyl-LL-diaminopimelate\n    -\
    \ DapC succinyldiaminopimelate aminotransferase (molecular player: beta/gammaproteobacterial\
    \ DapC family; activity or role: succinyldiaminopimelate:2-oxoglutarate transaminase\
    \ activity)\n  - 5. LL-diaminopimelate deprotection\n  - N-succinyl-LL-diaminopimelate\
    \ to LL-diaminopimelate\n    - DapE succinyl-diaminopimelate desuccinylase (molecular\
    \ player: proteobacterial DapE family; activity or role: succinyl-diaminopimelate\
    \ desuccinylase activity)\n  - 6. meso-diaminopimelate formation\n  - LL-diaminopimelate\
    \ to meso-diaminopimelate\n    - DapF diaminopimelate epimerase (molecular player:\
    \ DapF diaminopimelate epimerase family; activity or role: diaminopimelate epimerase\
    \ activity)\n  - 7. terminal L-lysine formation\n  - meso-Diaminopimelate to L-lysine\n\
    \    - LysA diaminopimelate decarboxylase (molecular player: LysA diaminopimelate\
    \ decarboxylase family; activity or role: diaminopimelate decarboxylase activity)"
  module_connections: '- Aspartate semialdehyde and pyruvate to hydroxytetrahydrodipicolinate
    precedes Hydroxytetrahydrodipicolinate to tetrahydrodipicolinate

    - Hydroxytetrahydrodipicolinate to tetrahydrodipicolinate precedes Tetrahydrodipicolinate
    to N-succinyltetrahydrodipicolinate

    - Tetrahydrodipicolinate to N-succinyltetrahydrodipicolinate precedes N-succinyl-2-amino-6-oxopimelate
    to N-succinyl-LL-diaminopimelate

    - N-succinyl-2-amino-6-oxopimelate to N-succinyl-LL-diaminopimelate precedes N-succinyl-LL-diaminopimelate
    to LL-diaminopimelate

    - N-succinyl-LL-diaminopimelate to LL-diaminopimelate precedes LL-diaminopimelate
    to meso-diaminopimelate

    - LL-diaminopimelate to meso-diaminopimelate precedes meso-Diaminopimelate to
    L-lysine'
  pathway_query: ppu00300
  pathway_id: ppu00300
  pathway_name: Lysine biosynthesis
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu00300 with 12 primary genes; module
    area: amino_acid_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '19'
  candidate_genes: '- aruC: PP_0372 | Q88QW2 | Acetylornithine aminotransferase 2
    (EC 2.6.1.11, EC 2.6.1.13) (EC 2.6.1.11; 2.6.1.13; primary bucket kegg:ppu00300)

    - PP_0664: PP_0664 | Q88Q34 | homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3;
    primary bucket kegg:ppu00300)

    - dapA__Q88NH2: PP_1237 | Q88NH2 | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA
    synthase) (EC 4.3.3.7) (EC 4.3.3.7; primary bucket kegg:ppu00261)

    - murE: PP_1332 | Q88N81 | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate
    ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme)
    (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase)
    (UDP-N-acetylmuramyl-tripeptide synthetase) (EC 6.3.2.13; primary bucket kegg:ppu00300)

    - murF: PP_1333 | Q88N80 | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine
    ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (EC 6.3.2.10; primary
    bucket kegg:ppu01502)

    - hom: PP_1470 | Q88MU8 | Homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary
    bucket kegg:ppu00300)

    - dapE: PP_1525 | Q88MP5 | Succinyl-diaminopimelate desuccinylase (SDAP desuccinylase)
    (EC 3.5.1.18) (N-succinyl-LL-2,6-diaminoheptanedioate amidohydrolase) (EC 3.5.1.18;
    primary bucket kegg:ppu00300)

    - dapD: PP_1530 | Q88MP1 | 2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase
    (EC 2.3.1.117) (Tetrahydrodipicolinate N-succinyltransferase) (THDP succinyltransferase)
    (THP succinyltransferase) (Tetrahydropicolinate succinylase) (EC 2.3.1.117; primary
    bucket kegg:ppu00300)

    - dapC: PP_1588 | Q88MI3 | N-succinyl-L,L-diaminopimelate aminotransferase alternative
    (EC 2.6.1.17) (EC 2.6.1.17; primary bucket kegg:ppu00300)

    - asd__Q88LE4: PP_1989 | Q88LE4 | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase)
    (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase) (EC 1.2.1.11;
    primary bucket kegg:ppu00261)

    - PP_2036: PP_2036 | Q88L99 | 4-hydroxy-tetrahydrodipicolinate synthase (EC 4.3.3.7)
    (EC 4.3.3.7; primary bucket kegg:ppu00261)

    - lysA-I: PP_2077 | Q88L58 | Diaminopimelate decarboxylase (DAP decarboxylase)
    (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)

    - dapA__Q88JL0: PP_2639 | Q88JL0 | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA
    synthase) (EC 4.3.3.7) (EC 4.3.3.7; primary bucket kegg:ppu00261)

    - aspC: PP_3786 | Q88GD8 | Aminotransferase (EC 2.6.1.1) (EC 2.6.1.1; primary
    bucket kegg:ppu00300)

    - dapF__Q88GD4: PP_3790 | Q88GD4 | Diaminopimelate epimerase (DAP epimerase) (EC
    5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)

    - PP_4473: PP_4473 | Q88EI9 | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) (EC
    2.7.2.4; primary bucket kegg:ppu00261)

    - dapB: PP_4725 | Q88DU4 | 4-hydroxy-tetrahydrodipicolinate reductase (HTPA reductase)
    (EC 1.17.1.8) (EC 1.17.1.8; primary bucket kegg:ppu00261)

    - lysA-II: PP_5227 | Q88CF4 | Diaminopimelate decarboxylase (DAP decarboxylase)
    (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)

    - dapF__Q88CF3: PP_5228 | Q88CF3 | Diaminopimelate epimerase (DAP epimerase) (EC
    5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)'
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__lysine_biosynthesis__ppu00300-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__lysine_biosynthesis__ppu00300-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

L-lysine biosynthesis by the succinylated diaminopimelate pathway in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu00300
- Resolved ID: ppu00300
- Resolved name: Lysine biosynthesis
- Source: KEGG

Resolved local bucket kegg:ppu00300 with 12 primary genes; module area: amino_acid_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 19

- aruC: PP_0372 | Q88QW2 | Acetylornithine aminotransferase 2 (EC 2.6.1.11, EC 2.6.1.13) (EC 2.6.1.11; 2.6.1.13; primary bucket kegg:ppu00300)
- PP_0664: PP_0664 | Q88Q34 | homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary bucket kegg:ppu00300)
- dapA__Q88NH2: PP_1237 | Q88NH2 | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7) (EC 4.3.3.7; primary bucket kegg:ppu00261)
- murE: PP_1332 | Q88N81 | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diaminopimelate-adding enzyme) (UDP-MurNAc-L-Ala-D-Glu:meso-diaminopimelate ligase) (UDP-MurNAc-tripeptide synthetase) (UDP-N-acetylmuramyl-tripeptide synthetase) (EC 6.3.2.13; primary bucket kegg:ppu00300)
- murF: PP_1333 | Q88N80 | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (EC 6.3.2.10; primary bucket kegg:ppu01502)
- hom: PP_1470 | Q88MU8 | Homoserine dehydrogenase (EC 1.1.1.3) (EC 1.1.1.3; primary bucket kegg:ppu00300)
- dapE: PP_1525 | Q88MP5 | Succinyl-diaminopimelate desuccinylase (SDAP desuccinylase) (EC 3.5.1.18) (N-succinyl-LL-2,6-diaminoheptanedioate amidohydrolase) (EC 3.5.1.18; primary bucket kegg:ppu00300)
- dapD: PP_1530 | Q88MP1 | 2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase (EC 2.3.1.117) (Tetrahydrodipicolinate N-succinyltransferase) (THDP succinyltransferase) (THP succinyltransferase) (Tetrahydropicolinate succinylase) (EC 2.3.1.117; primary bucket kegg:ppu00300)
- dapC: PP_1588 | Q88MI3 | N-succinyl-L,L-diaminopimelate aminotransferase alternative (EC 2.6.1.17) (EC 2.6.1.17; primary bucket kegg:ppu00300)
- asd__Q88LE4: PP_1989 | Q88LE4 | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenase) (EC 1.2.1.11; primary bucket kegg:ppu00261)
- PP_2036: PP_2036 | Q88L99 | 4-hydroxy-tetrahydrodipicolinate synthase (EC 4.3.3.7) (EC 4.3.3.7; primary bucket kegg:ppu00261)
- lysA-I: PP_2077 | Q88L58 | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)
- dapA__Q88JL0: PP_2639 | Q88JL0 | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7) (EC 4.3.3.7; primary bucket kegg:ppu00261)
- aspC: PP_3786 | Q88GD8 | Aminotransferase (EC 2.6.1.1) (EC 2.6.1.1; primary bucket kegg:ppu00300)
- dapF__Q88GD4: PP_3790 | Q88GD4 | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)
- PP_4473: PP_4473 | Q88EI9 | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) (EC 2.7.2.4; primary bucket kegg:ppu00261)
- dapB: PP_4725 | Q88DU4 | 4-hydroxy-tetrahydrodipicolinate reductase (HTPA reductase) (EC 1.17.1.8) (EC 1.17.1.8; primary bucket kegg:ppu00261)
- lysA-II: PP_5227 | Q88CF4 | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) (EC 4.1.1.20; primary bucket kegg:ppu00300)
- dapF__Q88CF3: PP_5228 | Q88CF3 | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) (EC 5.1.1.7; primary bucket kegg:ppu00300)

## Generic Module Context

### Working Scope

Bacterial L-lysine biosynthesis from L-aspartate 4-semialdehyde and pyruvate through the succinylated diaminopimelate route. DapA and DapB form and reduce the tetrahydrodipicolinate intermediate. DapD masks it by succinylation, DapC introduces the second amino group, and DapE removes the succinyl group. DapF converts LL-diaminopimelate to meso-diaminopimelate, and LysA performs the terminal decarboxylation to L-lysine. Aspartate kinase and aspartate-semialdehyde dehydrogenase provide a shared precursor used by lysine, threonine, and methionine synthesis and are outside the dedicated module boundary. The meso-diaminopimelate product also feeds peptidoglycan assembly before its conversion to lysine.

### Provisional Biological Outline

- succinylated diaminopimelate pathway of L-lysine biosynthesis
  - 1. committed diaminopimelate-ring formation
  - Aspartate semialdehyde and pyruvate to hydroxytetrahydrodipicolinate
    - DapA hydroxytetrahydrodipicolinate synthase (molecular player: DapA dihydrodipicolinate synthase family; activity or role: 4-hydroxy-tetrahydrodipicolinate synthase activity)
  - 2. tetrahydrodipicolinate reduction
  - Hydroxytetrahydrodipicolinate to tetrahydrodipicolinate
    - DapB hydroxytetrahydrodipicolinate reductase (molecular player: bacterial DapB family; activity or role: 4-hydroxy-tetrahydrodipicolinate reductase activity)
  - 3. tetrahydrodipicolinate succinylation
  - Tetrahydrodipicolinate to N-succinyltetrahydrodipicolinate
    - DapD tetrahydrodipicolinate N-succinyltransferase (molecular player: gammaproteobacterial DapD family; activity or role: 2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase activity)
  - 4. succinyldiaminopimelate transamination
  - N-succinyl-2-amino-6-oxopimelate to N-succinyl-LL-diaminopimelate
    - DapC succinyldiaminopimelate aminotransferase (molecular player: beta/gammaproteobacterial DapC family; activity or role: succinyldiaminopimelate:2-oxoglutarate transaminase activity)
  - 5. LL-diaminopimelate deprotection
  - N-succinyl-LL-diaminopimelate to LL-diaminopimelate
    - DapE succinyl-diaminopimelate desuccinylase (molecular player: proteobacterial DapE family; activity or role: succinyl-diaminopimelate desuccinylase activity)
  - 6. meso-diaminopimelate formation
  - LL-diaminopimelate to meso-diaminopimelate
    - DapF diaminopimelate epimerase (molecular player: DapF diaminopimelate epimerase family; activity or role: diaminopimelate epimerase activity)
  - 7. terminal L-lysine formation
  - meso-Diaminopimelate to L-lysine
    - LysA diaminopimelate decarboxylase (molecular player: LysA diaminopimelate decarboxylase family; activity or role: diaminopimelate decarboxylase activity)

### Known Relationships Among Steps

- Aspartate semialdehyde and pyruvate to hydroxytetrahydrodipicolinate precedes Hydroxytetrahydrodipicolinate to tetrahydrodipicolinate
- Hydroxytetrahydrodipicolinate to tetrahydrodipicolinate precedes Tetrahydrodipicolinate to N-succinyltetrahydrodipicolinate
- Tetrahydrodipicolinate to N-succinyltetrahydrodipicolinate precedes N-succinyl-2-amino-6-oxopimelate to N-succinyl-LL-diaminopimelate
- N-succinyl-2-amino-6-oxopimelate to N-succinyl-LL-diaminopimelate precedes N-succinyl-LL-diaminopimelate to LL-diaminopimelate
- N-succinyl-LL-diaminopimelate to LL-diaminopimelate precedes LL-diaminopimelate to meso-diaminopimelate
- LL-diaminopimelate to meso-diaminopimelate precedes meso-Diaminopimelate to L-lysine

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

# Species-Aware Review: L-Lysine Biosynthesis via the Succinylated Diaminopimelate Pathway in *Pseudomonas putida* KT2440

**Taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway bucket:** KEGG ppu00300 "Lysine biosynthesis" / KEGG module **M00016** (Lysine biosynthesis, succinyl-DAP pathway, aspartate ⇒ lysine)
**Module area:** amino_acid_metabolism

---

## 1. Executive summary

The dedicated **succinylated diaminopimelate (succinyl-DAP) route** to L-lysine is **fully satisfiable** in *P. putida* KT2440. Every reaction from (S)-tetrahydrodipicolinate through meso-DAP to L-lysine — DapA→DapB→DapD→(DapC/transaminase)→DapE→DapF→LysA — maps to at least one candidate gene, and the two shared upstream precursor steps (aspartate kinase, aspartate-semialdehyde dehydrogenase) are also present. KT2440 is a **lysine prototroph and standard metabolic chassis** whose genome-scale models encode complete lysine biosynthesis (PMID 28085902; re-annotated genome PMID 26913973), so the pathway is expected to be functional in vivo.

However, the candidate list is **noisy in ways that matter for curation**:

- **Paralog redundancy** exists at three steps: three DapA/K01714 genes, two LysA/K01586 genes, two DapF/K01778 genes. Sequence identity to *E. coli* references cleanly identifies the **primary ortholog** in each case (DapA = PP_1237; LysA = PP_2077; DapF = PP_5228) and marks the others as divergent paralogs / likely KO over-propagation.
- **The transamination step (step 4)** is covered by two mechanistically distinct candidates. **PP_1588 (*dapC*, K14267)** carries the DapC-specific InterPro/TIGRFAM signatures (IPR019878 "Succinyldiaminopimelate transaminase, DapC, beta/gammaproteobacteria"; TIGR03538) — **domain-level evidence that it is a genuine, lineage-appropriate DapC**, so it is the preferred step-4 gene. The **argD-type** enzyme PP_0372 (*aruC*, K00821, class-III PF00202) is a plausible bifunctional backup (it performs this reaction in *E. coli*). PP_1588's low pairwise identity to *E. coli* AspC/ArgD simply reflects that DapC is a distinct aminotransferase subfamily.
- **PP_3786 (*aspC*) → K10206 (DapL, EC 2.6.1.83)** is a **likely over-propagation**; the DapL bypass is not a gammaproteobacterial route.
- **Boundary contamination**: the candidate list includes threonine/methionine (hom/PP_1470, PP_0664) and peptidoglycan (murE/PP_1332, murF/PP_1333) genes that are **not** dedicated succinyl-DAP module members.

No pathway step is a genuine gap, and no new GO term or DapL/DapH module document is warranted for this organism.

---

## 2. Target-organism pathway definition

**Included process.** Cytoplasmic conversion of the aspartate-pathway intermediate L-aspartate-4-semialdehyde (+ pyruvate) into L-lysine through the DAP intermediates, using the **succinylase (acyl-protected) sub-variant** of the DAP pathway:

(S)-tetrahydrodipicolinate → N-succinyl-2-amino-6-oxopimelate → N-succinyl-LL-DAP → LL-DAP → meso-DAP → L-lysine.

meso-DAP is a **branch metabolite** simultaneously feeding peptidoglycan cross-linking (via MurE) and, after decarboxylation by LysA, cytoplasmic L-lysine.

**Alternate names / database definitions.**
- KEGG: pathway map00300 "Lysine biosynthesis"; module **M00016** "Lysine biosynthesis, succinyl-DAP pathway, aspartate ⇒ lysine". M00016 definition: `AK · ASADH · DapA(K01714) · DapB(K00215) · DapD(K00674) · [DapC K00821|K14267] · DapE(K01439) · DapF(K01778) · LysA(K01586|K12526)`.
- MetaCyc: "L-lysine biosynthesis I" (DAP, succinylase variant).
- UniProt PATHWAY tag: "L-lysine biosynthesis via DAP pathway; … (succinylase route)".

**Neighbouring pathways to keep separate.**
- **Aspartate-pathway trunk** (aspartate kinase, ASADH): shared precursor node feeding Lys **and** Thr/Met — keep outside the dedicated module boundary.
- **Threonine/methionine branch** (homoserine dehydrogenase *hom*/PP_1470, PP_0664; EC 1.1.1.3).
- **Peptidoglycan biosynthesis / cell-wall maps** (murE ppu00300-linked ligase, murF; consumers of meso-DAP, not synthesis steps).
- **Arginine biosynthesis** (acetylornithine aminotransferase side of PP_0372).
- Overview maps map01100 / map01110 / map01230 should not be used as the module boundary.

---

## 3. Expected step model (with target-organism call)

| # | Step (enzyme) | EC | KO | Primary gene in KT2440 | Other candidates | Module call |
|---|---------------|----|----|------------------------|------------------|-------------|
| — | Aspartate kinase (precursor) | 2.7.2.4 | K00928 | **PP_4473** (aspK, PE1) | — | covered (shared precursor, outside module) |
| — | Aspartate-semialdehyde dehydrogenase (precursor) | 1.2.1.11 | K00133 | **PP_1989** (asd) | — | covered (shared precursor, outside module) |
| 1 | 4-OH-tetrahydrodipicolinate synthase (DapA) | 4.3.3.7 | K01714 | **PP_1237** (56.8% to EcoDapA) | PP_2639 (31%), PP_2036 (26%) | **covered** |
| 2 | 4-OH-tetrahydrodipicolinate reductase (DapB) | 1.17.1.8 | K00215 | **PP_4725** | — | **covered** |
| 3 | THDP N-succinyltransferase (DapD) | 2.3.1.117 | K00674 | **PP_1530** | — | **covered** |
| 4 | N-succinyl-DAP aminotransferase (DapC) | 2.6.1.17 | K14267 / K00821 | **PP_1588** (dapC/K14267; DapC-specific TIGR03538/IPR019878) | PP_0372 (argD-type, K00821, bifunctional backup) | **covered** |
| 5 | Succinyl-DAP desuccinylase (DapE) | 3.5.1.18 | K01439 | **PP_1525** | — | **covered** |
| 6 | DAP epimerase (DapF) | 5.1.1.7 | K01778 | **PP_5228** (57.6% to EcoDapF) | PP_3790 (33%) | **covered** |
| 7 | DAP decarboxylase (LysA) | 4.1.1.20 | K01586 | **PP_2077** (lysA-I, 57.7%) | PP_5227 (lysA-II, 33%) | **covered** |

All seven module steps → **covered**. No step is a gap or "not_expected".

---

## 4. Candidate genes and evidence

**High-confidence, keep as primary enzyme for the step:**

- **PP_4473 / aspK (Q88EI9)** — Aspartate kinase, EC 2.7.2.4, **PE1 (protein-level evidence)**, annotation score 4. The strongest-evidenced gene in the set; shared precursor (Lys/Thr/Met). *Curation: covered, mark as shared-precursor, outside module boundary.*
- **PP_1989 / asd (Q88LE4)** — ASADH, EC 1.2.1.11, PE3, score 4. Shared precursor.
- **PP_1237 / dapA (Q88NH2)** — DapA/HTPA synthase, EC 4.3.3.7. Curated UniProt keywords "Lysine biosynthesis / Diaminopimelate biosynthesis / Schiff base"; **56.8% identity to E. coli DapA** — the clear primary ortholog. UniProt PATHWAY = "(S)-tetrahydrodipicolinate from L-aspartate: step 3/4". *Note: local metadata mis-buckets it to ppu00261; belongs to lysine (ppu00300).*
- **PP_4725 / dapB (Q88DU4)** — DapB, EC 1.17.1.8, single-copy, PATHWAY step 4/4. Unambiguous.
- **PP_1530 / dapD (Q88MP1)** — DapD, EC 2.3.1.117, single-copy, PATHWAY "succinylase route step 1/3". Diagnostic of the succinylase variant.
- **PP_1525 / dapE (Q88MP5)** — DapE, EC 3.5.1.18, single-copy, PATHWAY "succinylase route step 3/3". Diagnostic of the succinylase variant.
- **PP_5228 / dapF (Q88CF3)** — DapF, EC 5.1.1.7, PF01678; **57.6% to E. coli DapF** and in an operon with PP_5227 → strongest DapF call.
- **PP_2077 / lysA-I (Q88L58)** — LysA/DAPDC, EC 4.1.1.20, PF02784; **57.7% to E. coli LysA** → primary DAP decarboxylase.

**Transamination step (step 4) — covered, primary gene domain-supported:**

- **PP_1588 / dapC (Q88MI3)** — KEGG K14267 (dedicated DapC), local EC 2.6.1.17. Although UniProt is thin (PE4 "Predicted", score 1, PF00155, no EC), **InterPro assigns the DapC-specific family IPR019878 "Succinyldiaminopimelate transaminase, DapC, beta/gammaproteobacteria" and NCBIfam TIGR03538 "succinyldiaminopimelate transaminase"** — a diagnostic, lineage-appropriate signature. This is the **preferred step-4 enzyme**. Its low pairwise identity to *E. coli* AspC/ArgD reflects that DapC is a distinct aminotransferase subfamily, not weak evidence.
- **PP_0372 / aruC (Q88QW2)** — KEGG K00821 = acetylornithine/**N-succinyldiaminopimelate aminotransferase** (EC 2.6.1.11 **+ 2.6.1.17**), class-III aminotransferase (PF00202/IPR005814, CDD OAT_like, PIRSF "4-aminobutyrate/lysine/ornithine transaminase"), 36.9% to E. coli ArgD. In *E. coli* the argD/ArgD-type enzyme physiologically performs succinyl-DAP transamination, so this is a **plausible bifunctional backup** for step 4; primarily an arginine-biosynthesis enzyme.

**Likely over-propagation / lower-confidence paralogs:**

- **PP_2639 / dapA (Q88JL0)** — K01714, curated lysine keywords, but only **31% to E. coli DapA**; divergent DHDPS-superfamily paralog. Possible functional back-up DapA or a specialised aldolase.
- **PP_2036 (Q88L99)** — K01714 but UniProt has only "Lyase" keyword, submission-name, score 1, **no EC**; **26% to E. coli DapA, 28% to NanA/NAL**. Weakest DapA call — probably a non-canonical DHDPS/NAL-family enzyme, not a third lysine DapA.
- **PP_5227 / lysA-II (Q88CF4)** — K01586, EC 4.1.1.20, extra Pfam PF00278; **33% to E. coli LysA**. Divergent decarboxylase, but sits in an operon with a bona fide DapF (PP_5228), so plausibly a second functional LysA.
- **PP_3790 / dapF (Q88GD4)** — K01778, EC 5.1.1.7; **33% to E. coli DapF**; standalone. Divergent second epimerase.
- **PP_3786 / aspC (Q88GD8)** — KEGG **K10206 = DapL (LL-DAP aminotransferase, EC 2.6.1.83)**; local EC 2.6.1.1. UniProt: generic "Aminotransferase", PE4, no EC. InterPro places it only in the **broad IPR050881/PANTHER PTHR42832 "LL-diaminopimelate aminotransferase" family** and it **lacks the DapC signature** (no IPR019878/TIGR03538). **Likely over-propagation** — probably a generic aspartate/aromatic aminotransferase (see §5).

**Not module members (boundary contamination in the candidate list):**

- **PP_1470 / hom** and **PP_0664** — homoserine dehydrogenase, EC 1.1.1.3; UniProt PATHWAY = methionine/threonine. Belong to Thr/Met, not lysine.
- **PP_1332 / murE** — UDP-MurNAc-tripeptide:meso-DAP ligase, EC 6.3.2.13; **consumes** meso-DAP for peptidoglycan (downstream consumer, not a synthesis step).
- **PP_1333 / murF** — EC 6.3.2.10; peptidoglycan, unrelated to DAP synthesis.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **No genuine gaps.** All seven succinyl-DAP steps + both precursor steps are encoded. Module M00016 KO set is complete for *ppu*.
2. **Step-4 enzyme assignment (resolved by domain evidence).** PP_1588 carries the DapC-specific TIGR03538/IPR019878 signature and is the preferred dedicated DapC; PP_0372 (argD-type, K00821) is a plausible bifunctional backup. The step is **covered**; the residual uncertainty is only *in vivo* flux partitioning (which enzyme dominates), which is **not experimentally resolved in KT2440**. Note UniProt still assigns PP_1588 no EC, so the specific EC 2.6.1.17 rests on family signatures rather than direct assay.
3. **DapL over-propagation.** PP_3786→K10206 (DapL, EC 2.6.1.83) implies a THDP→LL-DAP shortcut. DapL is characterised in cyanobacteria, plants, Chlamydiae, Leptospira, Treponema and methanococci (PMIDs 16361515, 20418392, 25309529, 32274387), **not** in *Pseudomonas*/gammaproteobacteria, and KT2440 already has the full succinylase route. Treat as **likely over-propagation**; PP_3786 is more probably a generic aspartate/aromatic aminotransferase (local aspC/EC 2.6.1.1).
4. **DapA over-propagation.** Three genes carry K01714/EC 4.3.3.7 but only PP_1237 is a high-identity ortholog; PP_2639 and especially PP_2036 are divergent DHDPS-superfamily members that may not be lysine DapA.
5. **Broad/bifunctional EC mappings.** PP_0372 carries EC 2.6.1.11 + 2.6.1.13 (+2.6.1.17 via KEGG) — genuinely bifunctional (arginine + lysine); do not treat its lysine role as exclusive.
6. **Local bucket inconsistencies.** Several core lysine genes (PP_1237, PP_2036, PP_2639 dapA; PP_1989 asd; PP_4473 aspK; PP_4725 dapB) are tagged primary bucket **ppu00261** in the metadata but functionally belong to ppu00300/M00016; murF is tagged ppu01502. These are database-partition artifacts, not biology.

---

## 6. Module and GO-curation recommendations

**Per-step status:**

| Step | Status | Note |
|------|--------|------|
| DapA (1) | **covered** | primary PP_1237; PP_2639/PP_2036 candidate_uncertain paralogs |
| DapB (2) | **covered** | PP_4725, unambiguous |
| DapD (3) | **covered** | PP_1530, diagnostic of succinylase variant |
| DapC/transaminase (4) | **covered** | primary PP_1588 (DapC-specific TIGR03538/IPR019878); PP_0372 (K00821) bifunctional backup; no direct assay in KT2440 |
| DapE (5) | **covered** | PP_1525, diagnostic of succinylase variant |
| DapF (6) | **covered** | primary PP_5228; PP_3790 candidate_uncertain |
| LysA (7) | **covered** | primary PP_2077; PP_5227 second copy (operon with DapF) |

**Module boundary:** the generic module boundary is broadly correct. Recommend:
- **Exclude** hom/PP_1470, PP_0664 (Thr/Met) and murE/PP_1332, murF/PP_1333 (peptidoglycan) from the dedicated succinyl-DAP module.
- **Keep** aspK/PP_4473 and asd/PP_1989 flagged as **shared precursor (outside module boundary)** — matches the generic scope note.
- **Do not** open a DapL/aminotransferase-variant (DapH acetylase or DapL) module for this organism; **not_expected_in_target_taxon** for those variants.

**GO / EC actions:**
- No new GO terms required — all activities map to existing GO/EC.
- Flag PP_3786 GO/KO "LL-diaminopimelate aminotransferase (GO:0010285 / K10206)" for **review/removal** (over-propagation).
- Flag PP_1588 EC 2.6.1.17 as **inferred by homology (IEA)**, not experimental.
- **module_needs_revision:** minor — reassign the ppu00261-bucketed core genes (PP_1237, PP_2036, PP_2639, PP_1989, PP_4473, PP_4725) to the ppu00300/M00016 lysine module in local metadata.

---

## 7. Genes to promote to full `fetch-gene` review

Priority order:

1. **PP_3786 (aspC, Q88GD8)** — adjudicate/remove the DapL (K10206, EC 2.6.1.83) call vs. generic aspartate aminotransferase (EC 2.6.1.1); it lacks the DapC signature and DapL is not a *Pseudomonas* route. Highest-value correction.
2. **PP_1588 (dapC, Q88MI3)** — confirm and promote to a full DapC annotation (K14267, EC 2.6.1.17); supported by TIGR03538/IPR019878 but UniProt still gives no EC/name. Set as primary step-4 gene.
3. **PP_0372 (aruC, Q88QW2)** — clarify bifunctional acetylornithine (arginine) + succinyl-DAP (lysine backup) role (K00821, EC 2.6.1.11 + 2.6.1.17).
4. **PP_2036 (Q88L99)** and **PP_2639 (dapA, Q88JL0)** — determine whether either is a functional lysine DapA or a specialised/non-lysine DHDPS/NAL-family enzyme.
5. **PP_5227 (lysA-II) / PP_5228 (dapF)** — confirm the operon and whether PP_5227 is a second functional DAP decarboxylase.

---

## 8. Key references

- Nelson KE *et al.* (2002) Complete genome of *P. putida* KT2440. *Environ Microbiol* 4:799–808. (genome basis; via PMID 26913973)
- Belda E *et al.* (2016) The revisited genome of *P. putida* KT2440… robust metabolic chassis. *Environ Microbiol* 18:3403–3424. **PMID 26913973** (re-annotation; 1548 genes re-annotated).
- Yuan H *et al.* (2017) Pathway-consensus genome-scale metabolic reconstruction of *P. putida* KT2440. *Front Microbiol* / **PMID 28085902** (complete lysine biosynthesis in GSM).
- Hudson AO *et al.* (2006) LL-DAP aminotransferase (DapL) variant in plants/cyanobacteria. **PMID 16361515** (DapL taxonomic scope).
- Liu Y *et al.* (2010) Methanococci use the DapL pathway. **PMID 20418392** (DapL scope).
- Triassi AJ *et al.* (2014) DapL as a narrow-spectrum antibacterial target; DapL in ~13% of genomes (Chlamydia/Leptospira/Treponema). **PMID 25309529** (DapL not gammaproteobacterial).
- Peverelli MG *et al.* (2016) Dimerization of bacterial DAP decarboxylase essential for catalysis. **PMID 26921318** (LysA biology).
- Gokulan K *et al.* (2003) Crystal structure of *M. tuberculosis* LysA/DAPDC. **PMID 12637582** (LysA fold/mechanism).

---

### Evidence provenance note
Direct *P. putida* KT2440 experimental evidence for individual step enzymes is limited (only aspK/PP_4473 is UniProt PE1). Satisfiability rests on: (i) complete KEGG M00016 KO assignments for *ppu*; (ii) UniProt curated pathway annotations; (iii) genome-scale metabolic models encoding lysine biosynthesis (strain-specific, strong); (iv) sequence-identity ortholog assignment to *E. coli* K-12 experimentally characterised enzymes (family-level transfer, strong for primary orthologs, weak for divergent paralogs); and (v) InterPro/TIGRFAM family signatures (decisive for the PP_1588 DapC call). The succinylase-variant assignment is firm because DapD (PP_1530) and DapE (PP_1525) are both present and are diagnostic of this sub-variant.

### Limitations and open questions
- **No strain-specific enzyme assays.** With the exception of aspartate kinase, no KT2440 lysine-pathway enzyme has direct biochemical/genetic characterisation; all step assignments are homology/family inferences. Species transfer from *E. coli* is strong at the family level but does not establish in-vivo flux.
- **Step-4 flux partitioning unresolved.** Whether PP_1588 (dedicated DapC) or PP_0372 (argD-type) carries physiological succinyl-DAP transamination — or both — is unknown; a ΔPP_1588 / ΔPP_0372 auxotrophy test on minimal medium would resolve it.
- **Paralog functionality.** It is untested whether the divergent DapA (PP_2639, PP_2036), LysA (PP_5227) and DapF (PP_3790) paralogs are functional lysine enzymes, back-ups, or repurposed; single/double knockouts and complementation would clarify.
- **DapL call.** PP_3786 should be re-examined against a curated aspartate/aromatic-aminotransferase reference set; its EC 2.6.1.83 (K10206) is not supported by a DapL-specific signature and is very likely a mis-assignment.
- **No plasmid/second-copy caveats.** Analysis is chromosome-based (KT2440 is plasmid-free), so no additional lysine genes are expected elsewhere.


## Artifacts

- [OpenScientist final report](PSEPK__lysine_biosynthesis__ppu00300-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__lysine_biosynthesis__ppu00300-deep-research-openscientist_artifacts/final_report.pdf)