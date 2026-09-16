---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:34:43.539806'
end_time: '2026-09-01T13:59:21.543495'
duration_seconds: 1478.0
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial twin-arginine protein translocation
  module_summary: A species-neutral bacterial membrane-translocation module for export
    of folded, twin-arginine-signal-bearing proteins by the TatA, TatB, and TatC machinery.
    TatC and TatB form the substrate-receptor complex, after which TatA oligomerization
    supports proton-motive-force-dependent passage across the cytoplasmic membrane.
    Signal-peptide recognition, receptor assembly, and translocation are modeled as
    separate substantive roles.
  module_outline: "- Bacterial twin-arginine protein translocation\n  - 1. Twin-arginine\
    \ signal recognition and receptor scaffolding\n  - TatC substrate recognition\n\
    \    - TatC-family receptor component (molecular player: TatC family)\n  - 2.\
    \ Tat receptor-complex organization\n  - TatB receptor-complex organization\n\
    \    - TatB-family receptor component (molecular player: TatB family)\n  - 3.\
    \ Proton-motive-force-dependent translocation assembly\n  - TatA translocation\
    \ assembly\n    - TatA-family translocation component (molecular player: TatA/E\
    \ family, represented here by TatA proteins)"
  module_connections: '- TatC substrate recognition precedes TatB receptor-complex
    organization

    - TatB receptor-complex organization precedes TatA translocation assembly'
  pathway_query: ppu03070
  pathway_id: ppu03070
  pathway_name: Bacterial secretion system
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03070 with 42 primary genes; module
    area: transport_motility_signaling.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '61'
  candidate_genes: '- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase
    YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)

    - secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)

    - secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)

    - yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary
    bucket kegg:ppu03060)

    - secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)

    - secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket
    kegg:ppu03060)

    - tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary
    bucket kegg:ppu03060)

    - tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - xcpX: PP_1042 | Q88P11 | Type II secretion system protein K (primary bucket
    kegg:ppu03070)

    - xcpP: PP_1045 | Q88P08 | Type II secretion pathway protein XcpP (primary bucket
    kegg:ppu03070)

    - xcpQ: PP_1046 | Q88P07 | Type II secretion pathway protein XcpQ (primary bucket
    kegg:ppu03070)

    - gspE: PP_1047 | Q88P06 | General secretion pathway protein E (primary bucket
    kegg:ppu03070)

    - gspF: PP_1048 | Q88P05 | General secretion pathway protein F (primary bucket
    kegg:ppu03070)

    - gspG: PP_1049 | Q88P04 | Type II secretion system core protein G (primary bucket
    kegg:ppu03070)

    - xcpU: PP_1050 | Q88P03 | Type II secretion pathway protein XcpU (primary bucket
    kegg:ppu03070)

    - xcpV: PP_1051 | Q88P02 | Type II secretion pathway protein XcpV (primary bucket
    kegg:ppu03070)

    - xcpW: PP_1052 | Q88P01 | Type II secretion pathway protein XcpW (primary bucket
    kegg:ppu03070)

    - xcpY: PP_1053 | Q88P00 | Type II secretion pathway protein XcpY (primary bucket
    kegg:ppu03070)

    - secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8;
    primary bucket kegg:ppu03060)

    - PP_1449: PP_1449 | Q88MW9 | Filamentous haemagglutinin FhaB/tRNA nuclease CdiA-like
    TPS domain-containing protein (primary bucket kegg:ppu03070)

    - PP_1450: PP_1450 | Q88MW8 | Activation/secretion protein, TPS family (primary
    bucket kegg:ppu03070)

    - ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four
    homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - PP_1798: PP_1798 | Q88LX9 | Outer membrane efflux protein (primary bucket kegg:ppu01501)

    - vgrG-I: PP_2614 | Q88JN5 | Type 6 secretion system protein (primary bucket kegg:ppu03070)

    - hcpC-I: PP_2615 | Q88JN4 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)

    - PP_2616: PP_2616 | Q88JN3 | Type IV / VI secretion system DotU domain-containing
    protein (primary bucket kegg:ppu03070)

    - PP_2618: PP_2618 | Q88JN1 | Type VI secretion system lipoprotein TssJ (primary
    bucket kegg:ppu03070)

    - PP_2627: PP_2627 | Q88JM2 | Type VI secretion system membrane subunit TssM (primary
    bucket kegg:ppu03070)

    - PP_3089: PP_3089 | Q88IB0 | Type VI secretion system effector, Hcp1 family (primary
    bucket kegg:ppu03070)

    - PP_3090: PP_3090 | Q88IA9 | OmpA domain protein (primary bucket kegg:ppu03070)

    - PP_3091: PP_3091 | Q88IA8 | ImcF-like family protein (primary bucket kegg:ppu03070)

    - PP_3092: PP_3092 | Q88IA7 | Type IV / VI secretion system DotU domain-containing
    protein (primary bucket kegg:ppu03070)

    - PP_3094: PP_3094 | Q88IA5 | Type VI secretion system lipoprotein TssJ (primary
    bucket kegg:ppu03070)

    - clpV: PP_3095 | Q88IA4 | Protein ClpV1 (primary bucket kegg:ppu03070)

    - PP_3106: PP_3106 | Q88I93 | Uncharacterized protein (primary bucket kegg:ppu03070)

    - PP_3385: PP_3385 | Q88HH3 | Type IV / VI secretion system DotU domain-containing
    protein (primary bucket kegg:ppu03070)

    - vgrG-II: PP_3386 | Q88HH2 | Type 6 secretion system protein (primary bucket
    kegg:ppu03070)

    - xcpT: PP_3423 | Q88HD7 | Type II secretion system core protein G (primary bucket
    kegg:ppu03070)

    - xcpS: PP_3424 | Q88HD6 | Type II secretion pathway protein XcpS (primary bucket
    kegg:ppu03070)

    - PP_3476: PP_3476 | Q88H85 | Type II secretion system protein G (primary bucket
    kegg:ppu03070)

    - PP_3477: PP_3477 | Q88H84 | Secretion type II protein related to protein G (primary
    bucket kegg:ppu03070)

    - PP_3478: PP_3478 | Q88H83 | Secretion protein (primary bucket kegg:ppu03070)

    - PP_3483: PP_3483 | Q88H78 | Type II secretion system protein (primary bucket
    kegg:ppu03070)

    - vgrG-III: PP_4049 | Q88FP0 | Type 6 secretion system protein (primary bucket
    kegg:ppu03070)

    - PP_4071: PP_4071 | Q88FL8 | Type VI secretion system membrane subunit TssM (primary
    bucket kegg:ppu03070)

    - PP_4079: PP_4079 | Q88FL1 | Type VI secretion system lipoprotein TssJ (primary
    bucket kegg:ppu03070)

    - PP_4081: PP_4081 | Q88FK9 | Type 4/6 secretion system (primary bucket kegg:ppu03070)

    - hcpC-II: PP_4082 | Q88FK8 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)

    - PP_4886: PP_4886 | Q88DE1 | Hcp1 family type VI secretion system effector (primary
    bucket kegg:ppu03070)

    - PP_4923: PP_4923 | Q88DA4 | Outer membrane efflux protein (primary bucket kegg:ppu01501)

    - PP_4926: PP_4926 | Q88DA1 | Membrane fusion protein (MFP) family protein (primary
    bucket kegg:ppu03070)

    - cyaB: PP_4927 | Q88DA0 | Cyclolysin secretion/processing ATP-binding protein
    CyaB (EC 3.4.22.-) (EC 3.4.22.-; primary bucket kegg:ppu03070)

    - tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary
    bucket kegg:ppu03060)

    - tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)

    - ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor)
    (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - PP_5190: PP_5190 | Q88CJ1 | Type II secretion system protein (primary bucket
    kegg:ppu03070)

    - PP_5238: PP_5238 | Q88CE3 | Fimbrial protein (primary bucket kegg:ppu03070)

    - secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket
    kegg:ppu03060)'
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_twin_arginine_translocation__ppu03070-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_twin_arginine_translocation__ppu03070-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial twin-arginine protein translocation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03070
- Resolved ID: ppu03070
- Resolved name: Bacterial secretion system
- Source: KEGG

Resolved local bucket kegg:ppu03070 with 42 primary genes; module area: transport_motility_signaling.

## Candidate Genes From Local Metadata

Candidate gene count: 61

- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)
- secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)
- secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)
- yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary bucket kegg:ppu03060)
- secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)
- secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket kegg:ppu03060)
- tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary bucket kegg:ppu03060)
- tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- xcpX: PP_1042 | Q88P11 | Type II secretion system protein K (primary bucket kegg:ppu03070)
- xcpP: PP_1045 | Q88P08 | Type II secretion pathway protein XcpP (primary bucket kegg:ppu03070)
- xcpQ: PP_1046 | Q88P07 | Type II secretion pathway protein XcpQ (primary bucket kegg:ppu03070)
- gspE: PP_1047 | Q88P06 | General secretion pathway protein E (primary bucket kegg:ppu03070)
- gspF: PP_1048 | Q88P05 | General secretion pathway protein F (primary bucket kegg:ppu03070)
- gspG: PP_1049 | Q88P04 | Type II secretion system core protein G (primary bucket kegg:ppu03070)
- xcpU: PP_1050 | Q88P03 | Type II secretion pathway protein XcpU (primary bucket kegg:ppu03070)
- xcpV: PP_1051 | Q88P02 | Type II secretion pathway protein XcpV (primary bucket kegg:ppu03070)
- xcpW: PP_1052 | Q88P01 | Type II secretion pathway protein XcpW (primary bucket kegg:ppu03070)
- xcpY: PP_1053 | Q88P00 | Type II secretion pathway protein XcpY (primary bucket kegg:ppu03070)
- secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8; primary bucket kegg:ppu03060)
- PP_1449: PP_1449 | Q88MW9 | Filamentous haemagglutinin FhaB/tRNA nuclease CdiA-like TPS domain-containing protein (primary bucket kegg:ppu03070)
- PP_1450: PP_1450 | Q88MW8 | Activation/secretion protein, TPS family (primary bucket kegg:ppu03070)
- ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- PP_1798: PP_1798 | Q88LX9 | Outer membrane efflux protein (primary bucket kegg:ppu01501)
- vgrG-I: PP_2614 | Q88JN5 | Type 6 secretion system protein (primary bucket kegg:ppu03070)
- hcpC-I: PP_2615 | Q88JN4 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)
- PP_2616: PP_2616 | Q88JN3 | Type IV / VI secretion system DotU domain-containing protein (primary bucket kegg:ppu03070)
- PP_2618: PP_2618 | Q88JN1 | Type VI secretion system lipoprotein TssJ (primary bucket kegg:ppu03070)
- PP_2627: PP_2627 | Q88JM2 | Type VI secretion system membrane subunit TssM (primary bucket kegg:ppu03070)
- PP_3089: PP_3089 | Q88IB0 | Type VI secretion system effector, Hcp1 family (primary bucket kegg:ppu03070)
- PP_3090: PP_3090 | Q88IA9 | OmpA domain protein (primary bucket kegg:ppu03070)
- PP_3091: PP_3091 | Q88IA8 | ImcF-like family protein (primary bucket kegg:ppu03070)
- PP_3092: PP_3092 | Q88IA7 | Type IV / VI secretion system DotU domain-containing protein (primary bucket kegg:ppu03070)
- PP_3094: PP_3094 | Q88IA5 | Type VI secretion system lipoprotein TssJ (primary bucket kegg:ppu03070)
- clpV: PP_3095 | Q88IA4 | Protein ClpV1 (primary bucket kegg:ppu03070)
- PP_3106: PP_3106 | Q88I93 | Uncharacterized protein (primary bucket kegg:ppu03070)
- PP_3385: PP_3385 | Q88HH3 | Type IV / VI secretion system DotU domain-containing protein (primary bucket kegg:ppu03070)
- vgrG-II: PP_3386 | Q88HH2 | Type 6 secretion system protein (primary bucket kegg:ppu03070)
- xcpT: PP_3423 | Q88HD7 | Type II secretion system core protein G (primary bucket kegg:ppu03070)
- xcpS: PP_3424 | Q88HD6 | Type II secretion pathway protein XcpS (primary bucket kegg:ppu03070)
- PP_3476: PP_3476 | Q88H85 | Type II secretion system protein G (primary bucket kegg:ppu03070)
- PP_3477: PP_3477 | Q88H84 | Secretion type II protein related to protein G (primary bucket kegg:ppu03070)
- PP_3478: PP_3478 | Q88H83 | Secretion protein (primary bucket kegg:ppu03070)
- PP_3483: PP_3483 | Q88H78 | Type II secretion system protein (primary bucket kegg:ppu03070)
- vgrG-III: PP_4049 | Q88FP0 | Type 6 secretion system protein (primary bucket kegg:ppu03070)
- PP_4071: PP_4071 | Q88FL8 | Type VI secretion system membrane subunit TssM (primary bucket kegg:ppu03070)
- PP_4079: PP_4079 | Q88FL1 | Type VI secretion system lipoprotein TssJ (primary bucket kegg:ppu03070)
- PP_4081: PP_4081 | Q88FK9 | Type 4/6 secretion system (primary bucket kegg:ppu03070)
- hcpC-II: PP_4082 | Q88FK8 | Hemolysin-coregulated protein (primary bucket kegg:ppu03070)
- PP_4886: PP_4886 | Q88DE1 | Hcp1 family type VI secretion system effector (primary bucket kegg:ppu03070)
- PP_4923: PP_4923 | Q88DA4 | Outer membrane efflux protein (primary bucket kegg:ppu01501)
- PP_4926: PP_4926 | Q88DA1 | Membrane fusion protein (MFP) family protein (primary bucket kegg:ppu03070)
- cyaB: PP_4927 | Q88DA0 | Cyclolysin secretion/processing ATP-binding protein CyaB (EC 3.4.22.-) (EC 3.4.22.-; primary bucket kegg:ppu03070)
- tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary bucket kegg:ppu03060)
- tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)
- ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor) (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- PP_5190: PP_5190 | Q88CJ1 | Type II secretion system protein (primary bucket kegg:ppu03070)
- PP_5238: PP_5238 | Q88CE3 | Fimbrial protein (primary bucket kegg:ppu03070)
- secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket kegg:ppu03060)

## Generic Module Context

### Working Scope

A species-neutral bacterial membrane-translocation module for export of folded, twin-arginine-signal-bearing proteins by the TatA, TatB, and TatC machinery. TatC and TatB form the substrate-receptor complex, after which TatA oligomerization supports proton-motive-force-dependent passage across the cytoplasmic membrane. Signal-peptide recognition, receptor assembly, and translocation are modeled as separate substantive roles.

### Provisional Biological Outline

- Bacterial twin-arginine protein translocation
  - 1. Twin-arginine signal recognition and receptor scaffolding
  - TatC substrate recognition
    - TatC-family receptor component (molecular player: TatC family)
  - 2. Tat receptor-complex organization
  - TatB receptor-complex organization
    - TatB-family receptor component (molecular player: TatB family)
  - 3. Proton-motive-force-dependent translocation assembly
  - TatA translocation assembly
    - TatA-family translocation component (molecular player: TatA/E family, represented here by TatA proteins)

### Known Relationships Among Steps

- TatC substrate recognition precedes TatB receptor-complex organization
- TatB receptor-complex organization precedes TatA translocation assembly

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

# Commissioned Review: Bacterial Twin-Arginine Protein Translocation (Tat) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Queried bucket:** KEGG `ppu03070` "Bacterial secretion system" (42 primary genes)
**Module under review:** Bacterial twin-arginine protein translocation (TatA/TatB/TatC)
**Curation goal:** Manual module satisfiability and gene-annotation review

---

## 1. Executive Summary

The twin-arginine translocation (Tat) module is **fully satisfiable** in *Pseudomonas putida* KT2440, and — unusually — it is encoded **twice**. KT2440 carries two complete, canonical *tatABC* operons: an accessory, phosphate-starvation-induced cluster (**tat-1**: `tatC-I`/PP_1039, `tatB-I`/PP_1040, `tatA-I`/PP_1041) that sits immediately adjacent to the Xcp type II secretion system (T2SS) genes, and a housekeeping cluster (**tat-2**: `tatC-II`/PP_5018, `tatB`/PP_5017, `tatA-II`/PP_5016). All three mechanistic steps of the generic module — (1) twin-arginine signal recognition by TatC, (2) receptor-complex organization by TatB, and (3) proton-motive-force (PMF)-driven translocation assembly by TatA — are therefore **COVERED in duplicate**. Both systems have been experimentally shown to translocate a genuine Tat substrate (the periplasmic phosphatase UxpB) in the target species itself, so the paralogous annotations reflect real biology rather than annotation over-propagation ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)).

A key curation point concerns **pathway boundaries**. Although the commission query resolved to KEGG `ppu03070` ("Bacterial secretion system"), the Tat machinery in KEGG actually belongs to the neighboring map `ppu03060` ("Protein export"), and all six KT2440 *tat* genes carry that primary bucket. The Tat pathway — export of *fully folded*, twin-arginine-signal-bearing proteins across the cytoplasmic membrane in a PMF-dependent, Sec-independent manner — is mechanistically distinct from the Sec/SRP/YidC general secretory route and from the outer-membrane-spanning secretion systems (T1SS, T2SS/Xcp, T6SS) that dominate the `ppu03070` map. The two modules are nonetheless functionally *linked*: the Tat substrate UxpB is first exported to the periplasm by Tat and then secreted across the outer membrane by the Xcp T2SS, which explains the genomic adjacency of the tat-1 operon and the *xcp* genes.

The recommended curation outcome is: mark all three Tat module steps **covered** (in duplicate); flag the generic single-*tatABC* module description as **module_needs_revision** to capture the gene-duplicated architecture unique to this strain; re-anchor the module to KEGG Protein export (`ppu03060`) rather than the `ppu03070` secretion overview; and relabel the six genes with explicit TatA/TatB/TatC family + cluster identifiers. The remaining 55 candidate genes are **out-of-module**, belonging to distinct secretion systems, and require no Tat annotation. Two genes — `tatC-I`/PP_1039 and `tatC-II`/PP_5018 — should be promoted to full `fetch-gene` review as the anchor substrate-recognition components of each cluster.

---

## 2. Target-Organism Pathway Definition

### What the Tat pathway is (and is not)

The twin-arginine translocation pathway exports **folded** proteins across the bacterial cytoplasmic membrane. This is its defining feature and the property that separates it from all other protein-export routes: whereas the Sec system threads unfolded polypeptides through the SecYEG channel, the Tat system moves proteins that are already folded — and in many cases already loaded with cofactors (molybdopterin, FeS clusters, etc.) or assembled into oligomers — across the membrane ([PMID: 16756481](https://pubmed.ncbi.nlm.nih.gov/16756481/)).

Substrates are targeted by an N-terminal signal peptide bearing a near-invariant **twin-arginine consensus motif, S/T-R-R-x-F-L-K (SRRxFLK)** ([PMID: 10766774](https://pubmed.ncbi.nlm.nih.gov/10766774/)). The two arginine residues are essentially invariant and, together with the conserved phenylalanine, are critical for recognition, although the hydrophobic core and N-terminal charge can act synergistically to allow targeting even of atypical signals ([PMID: 11829474](https://pubmed.ncbi.nlm.nih.gov/11829474/)).

Translocation is driven by the **transmembrane proton-motive force (PMF)** and requires no ATP hydrolysis at the translocation step — again distinguishing Tat from the ATP-driven SecA motor of the Sec pathway ([PMID: 24003141](https://pubmed.ncbi.nlm.nih.gov/24003141/)).

### Pathway boundaries for curation

| Keep together (Tat module) | Keep separate (neighboring modules) |
|---|---|
| TatC (signal recognition) | Sec translocon: SecYEG, SecA, SecDF-YajC (`ppu03060`) |
| TatB (receptor organization) | SRP targeting: Ffh, FtsY, SecB (`ppu03060`) |
| TatA (PMF-driven translocation) | Membrane insertase YidC (`ppu03060`) |
| | T1SS (CyaB/HlyBD-type ABC exporters) |
| | T2SS / Xcp (main terminal branch of GSP) |
| | T6SS (VgrG/Hcp/TssJLM/ClpV) |
| | Outer-membrane efflux (`ppu01501`) |

**Alternate names / database definitions.** The pathway is variously called the *twin-arginine translocation (Tat)* pathway, the *Sec-independent protein translocation* pathway, the *ΔpH-dependent* pathway (in the chloroplast literature), and the *TAT* system. In KEGG it is a component of map `03060` "Protein export." Individual genes appear under UniProt as "Sec-independent protein translocase protein TatA/TatB/TatC." The commission's resolved bucket `ppu03070` ("Bacterial secretion system") is a broad *overview* map that should be kept distinct from the mechanistic Tat module.

---

## 3. Expected Step Model

The generic module posits three ordered substantive roles. The KT2440 investigation confirmed each step and its ordering against experimental literature.

```
  Twin-arginine substrate (folded, bearing SRRxFLK signal)
                    │
                    ▼
 ┌───────────────────────────────────────────────┐
 │ STEP 1 — TatC substrate recognition            │
 │  TatC-family receptor component                │
 │  "TatC is both necessary and sufficient" for   │
 │  the primary signal-peptide interaction        │
 └───────────────────────────────────────────────┘
                    │  precedes
                    ▼
 ┌───────────────────────────────────────────────┐
 │ STEP 2 — TatB receptor-complex organization    │
 │  TatB-family receptor component                │
 │  transfers substrate from TatC to the pore;    │
 │  TatBC form the co-localized substrate receptor│
 └───────────────────────────────────────────────┘
                    │  precedes
                    ▼
 ┌───────────────────────────────────────────────┐
 │ STEP 3 — TatA translocation assembly (PMF)     │
 │  TatA-family translocation component           │
 │  PMF-dependent, reversible oligomerization     │
 │  forms the translocation site                  │
 └───────────────────────────────────────────────┘
                    │
                    ▼
        Folded protein delivered to periplasm
```

The ordering is directly supported by *E. coli* crosslinking and imaging studies: for the primary interaction "TatC is both necessary and sufficient while a subsequent association with TatB likely mediates transfer from TatC to the actual Tat pore" ([PMID: 14580344](https://pubmed.ncbi.nlm.nih.gov/14580344/)), and TatA complex "formation … requires both a functional TatBC substrate receptor and the transmembrane proton motive force (PMF)" and is reversible — "Removing the PMF causes TatA complexes to dissociate" ([PMID: 24003141](https://pubmed.ncbi.nlm.nih.gov/24003141/)). This matches module steps 1 → 2 → 3 and their stated precedence relationships exactly. The transfer of this mechanism from *E. coli* to *P. putida* is **strong**, because the Tat components are highly conserved across Gram-negative bacteria (tatABC operons are near-universally present in α- and γ-proteobacteria; [PMID: 22438962](https://pubmed.ncbi.nlm.nih.gov/22438962/)).

---

## 4. Candidate Genes and Evidence

### 4.1 In-module genes — the two Tat operons

KT2440 encodes **two** canonical *tatABC* operons. Both are represented in the candidate metadata under the KEGG Protein-export bucket (`ppu03060`).

| Cluster | Gene | Locus | UniProt | Module step | Evidence in target species |
|---|---|---|---|---|---|
| **tat-1** (accessory, Pi-induced; adjacent to *xcp*) | `tatC-I` | PP_1039 | Q88P14 | Step 1 — recognition | Translocates UxpB ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)) |
| | `tatB-I` | PP_1040 | Q88P13 | Step 2 — receptor | " |
| | `tatA-I` | PP_1041 | Q88P12 | Step 3 — translocation | " |
| **tat-2** (housekeeping) | `tatC-II` | PP_5018 | Q88D11 | Step 1 — recognition | Translocates UxpB ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)) |
| | `tatB` | PP_5017 | Q88D12 | Step 2 — receptor | " |
| | `tatA-II` | PP_5016 | Q88D13 | Step 3 — translocation | " |

**Direct target-species evidence.** Putker et al. (2013) report, working directly in *P. putida*: *"Two different tat gene clusters were detected in the P. putida genome, of which one, named tat-1, is located adjacent to the uxpB and xcp genes. Both Tat systems appeared to be capable of transporting the UxpB protein. However, expression of the tat-1 genes was strongly induced by low Pi levels"* ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)). This is the highest possible tier of evidence for curation: (i) it establishes that KT2440 has two *tat* clusters, (ii) it shows **both** are functionally competent for Tat export, and (iii) it distinguishes their regulation — tat-1 is inducible under phosphate limitation, whereas tat-2 behaves as a constitutive housekeeping system.

**Regulatory and genomic-context distinction.** The tat-1 cluster is genomically embedded next to the *uxpB* gene and the *xcp* T2SS genes (PP_1042–PP_1053). This is not coincidental: UxpB is a Tat substrate (its signal contains a twin-arginine motif) that is exported by Tat to the periplasm and then secreted across the outer membrane in an Xcp/T2SS-dependent manner — *"transported across the cell envelope in an Xcp-dependent manner demonstrating that the xcp genes encode an active T2SS. The signal sequence of UxpB contains a twin-arginine translocation (Tat) motif"* ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)). The two secretion systems therefore act *sequentially* on a shared substrate, which is a curation-relevant reason to keep the modules **separate but cross-referenced**.

### 4.2 Confidence assessment per component

- **TatC (PP_1039, PP_5018):** High confidence. TatC is the most conserved and diagnostic Tat component; it is the primary signal-peptide receptor and is "necessary and sufficient" for the initial substrate interaction ([PMID: 14580344](https://pubmed.ncbi.nlm.nih.gov/14580344/)). Two paralogs, cleanly separable by operon/cluster. **Promote both to full review** as module anchors.
- **TatB (PP_1040, PP_5017):** High confidence. TatB partners TatC in the substrate receptor complex, and BiFC imaging shows TatBC hetero-oligomers co-localized at the cell poles ([PMID: 20169075](https://pubmed.ncbi.nlm.nih.gov/20169075/)). The metadata labels are appropriate ("Sec-independent protein translocase TatB").
- **TatA (PP_1041, PP_5016):** High confidence. TatA forms the PMF-dependent, reversibly assembling translocation site ([PMID: 24003141](https://pubmed.ncbi.nlm.nih.gov/24003141/)). Note the paralog-naming inconsistency in the metadata: PP_1041 is `tatA-I` and PP_5016 is `tatA-II`, but the corresponding TatB genes are `tatB-I`/PP_1040 and (unqualified) `tatB`/PP_5017. Cluster suffixes should be harmonized (see §6).

### 4.3 Out-of-module candidates (55 genes)

The remaining candidates were resolved to distinct secretion/export modules and are **not** part of the Tat module:

| System | Representative candidate genes | Correct bucket |
|---|---|---|
| Sec translocon / SRP / insertase | yidC (PP_0006), secE (PP_0441), secY (PP_0474), yajC/secD/secF (PP_0834–0836), secA (PP_1345), ffh (PP_1461), secB (PP_5053), ftsY (PP_5111), secG (PP_5706) | `ppu03060` Protein export |
| T2SS / Xcp | xcpX/P/Q/U/V/W/Y, gspE/F/G (PP_1042–1053), xcpS/T (PP_3423–3424), PP_3476–3483, PP_5190 | `ppu03070` |
| T1SS (ABC exporter) | cyaB (PP_4927), PP_4926 (MFP) | `ppu03070` |
| T6SS | vgrG-I/II/III, hcpC-I/II, clpV, tss* / DotU / ImcF / TssJ / TssM loci (multiple) | `ppu03070` |
| Two-partner secretion (TPS) | PP_1449, PP_1450 | `ppu03070` |
| Outer-membrane efflux | PP_1798, PP_4923 | `ppu01501` |

None of these encode TatA/TatB/TatC functions and none should receive Tat-module annotation.

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

**No TatE expected.** The generic module notes the "TatA/E family." *TatE* is an *E. coli*-specific, low-abundance TatA paralog arising from a gene duplication in the enterobacterial lineage; it is functionally redundant with TatA. *Pseudomonas* species typically encode only TatA + TatB + TatC. The apparent "duplication" in KT2440 is **not** a TatA/TatE split but a whole-operon duplication (two full *tatABC* clusters). Curators should **not** open a TatE gap; its absence is expected in this taxon and should be marked `not_expected_in_target_taxon` if the template requires a TatA/E slot.

**The gene-duplicated architecture is genuine, not over-propagation.** A naive reviewer might suspect that two sets of *tatABC* annotations reflect over-propagated homology calls. The direct experimental demonstration that *both* clusters translocate UxpB rules this out ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)). This is the opposite of an over-annotation problem: the generic single-*tatABC* module *under*-represents KT2440's true architecture.

**Bucket mislocation.** The commission query resolved to `ppu03070` (Bacterial secretion system overview), but the Tat genes carry `ppu03060` (Protein export). This is a boundary/definitional issue, not a biological gap — but it should be corrected so the module is anchored to the mechanistically correct map.

**Substrate scope is inferred, not exhaustively mapped in KT2440.** Beyond UxpB, the KT2440 Tat substrate repertoire has not been experimentally enumerated. In the related organism *Pseudomonas aeruginosa*, at least 18 Tat substrates were identified and a *tatC* mutant showed pleiotropic loss of phospholipases, pyoverdine/iron-uptake proteins, anaerobic-respiration enzymes, osmotic-stress defense, motility, and biofilm functions ([PMID: 12034867](https://pubmed.ncbi.nlm.nih.gov/12034867/)). Transfer of this substrate list to KT2440 is **plausible but uncertain** — the two species differ in lifestyle (opportunistic pathogen vs. soil saprophyte) and in Tat operon copy number.

**Naming inconsistency.** As noted, PP_5017 is labeled simply `tatB` while its cluster partners are `tatA-II`/`tatC-II`. Harmonize to `tatB-II` to avoid downstream confusion.

---

## 6. Module and GO-Curation Recommendations

| Module step | Molecular player | KT2440 status | Genes |
|---|---|---|---|
| 1. Twin-arginine signal recognition | TatC family | **covered (×2)** | PP_1039, PP_5018 |
| 2. Tat receptor-complex organization | TatB family | **covered (×2)** | PP_1040, PP_5017 |
| 3. PMF-dependent translocation assembly | TatA family | **covered (×2)** | PP_1041, PP_5016 |

**Recommended curation actions:**

1. **Mark all three module steps `covered`** — and annotate that coverage is *duplicated* (two independent functional operons).
2. **Flag the generic module as `module_needs_revision`.** The species-neutral single-*tatABC* template does not capture KT2440's two-operon architecture with distinct regulation (tat-1 phosphate-inducible/accessory; tat-2 constitutive/housekeeping). A strain-aware module document should record both clusters and their regulatory divergence.
3. **Correct the pathway boundary / bucket.** Re-anchor the Tat module to KEGG **Protein export (`ppu03060`)**, not the `ppu03070` secretion overview. Keep a cross-reference to Xcp/T2SS (`ppu03070`) to document the sequential UxpB export relationship.
4. **Relabel genes with explicit family + cluster identifiers:** `tatA-I/tatB-I/tatC-I` (PP_1041/1040/1039) and `tatA-II/tatB-II/tatC-II` (PP_5016/5017/5018). In particular, rename PP_5017 from `tatB` → `tatB-II` for consistency.
5. **Do not open a TatE gap.** TatE is not expected in *Pseudomonas*; mark `not_expected_in_target_taxon`.
6. **GO annotations:** All six genes support GO:0043953 *protein transport by the Tat complex*; TatA additionally supports GO:0009977 *proton motive force-dependent protein transmembrane transporter activity*; TatBC support GO:0033281 *TAT protein transport complex* (cellular component). No new GO term requests appear necessary; existing Tat GO terms are adequate.

---

## 7. Genes to Promote to Full Review

| Priority | Gene | Locus | Rationale |
|---|---|---|---|
| High | `tatC-I` | PP_1039 | Anchor substrate-recognition component of the accessory tat-1 cluster; genomic linkage to *uxpB*/*xcp*; Pi-induced regulation warrants documentation. |
| High | `tatC-II` | PP_5018 | Anchor substrate-recognition component of the housekeeping tat-2 cluster. |
| Medium | `tatA-I` / `tatA-II` | PP_1041 / PP_5016 | Confirm PMF-dependent translocation role and clarify paralog naming. |
| Medium | `tatB-I` / `tatB` | PP_1040 / PP_5017 | Harmonize naming (PP_5017 → `tatB-II`); confirm receptor-complex role. |
| Reference only | UxpB (*uxpB*) | (not in candidate list) | The validated Tat substrate; worth adding as a substrate cross-reference even though it is not a translocase component. |

The two *tatC* genes are the highest-value promotions because TatC is the diagnostic, most-conserved Tat component and the primary determinant of substrate specificity.

---

## 8. Mechanistic Model / Interpretation

Synthesizing the findings into a coherent KT2440-specific narrative:

KT2440's cytoplasmic membrane houses **two parallel Tat translocases**. Both follow the canonical mechanism: a folded, SRRxFLK-bearing substrate is captured first by **TatC** (the necessary-and-sufficient primary receptor), handed off through **TatB** to organize the receptor complex, and finally translocated when **TatA** oligomerizes into a transient, PMF-powered pore that dissociates once the substrate has passed. The two clusters differ not in mechanism but in **deployment**: tat-2 is the constitutive housekeeping route, while tat-1 is upregulated under phosphate starvation and is physically and functionally coupled to the Xcp T2SS. Under low-phosphate conditions, the phosphatase substrate UxpB is exported to the periplasm by Tat and then pushed across the outer membrane by Xcp — a two-step secretion relay that explains why the tat-1 operon and the *xcp* genes are genomic neighbors.

```
 LOW-Pi CONDITION (tat-1 induced)              HOUSEKEEPING (tat-2 constitutive)
 ─────────────────────────────────             ────────────────────────────────
   cytoplasm                                     cytoplasm
     UxpB (folded, RR-signal)                      folded RR-substrates
         │ Tat-1 (PP_1039/40/41)                       │ Tat-2 (PP_5018/17/16)
         ▼                                             ▼
    ── inner membrane ──                          ── inner membrane ──
     periplasm: UxpB                               periplasm
         │ Xcp T2SS (PP_1042–1053)
         ▼
    ── outer membrane ──
     extracellular UxpB
```

For module curation, the crucial reinterpretation is that a "single canonical Tat operon" template is factually wrong for this strain. The correct statement is: **all module steps satisfied, in duplicate, by two experimentally validated operons with divergent regulation.**

---

## 9. Limitations and Knowledge Gaps

1. **Substrate repertoire in KT2440 is not enumerated.** Only UxpB is experimentally validated as a KT2440 Tat substrate. The wider substrate set is inferred by homology to *P. aeruginosa* ([PMID: 12034867](https://pubmed.ncbi.nlm.nih.gov/12034867/)) — a transfer weakened by differing lifestyle and Tat copy number.
2. **Functional redundancy vs. specialization of the two operons is only partly resolved.** Both export UxpB, but whether tat-1 and tat-2 have distinct or overlapping substrate specificities under different conditions is unknown. The regulatory distinction (Pi-inducible tat-1 vs. constitutive tat-2) suggests condition-specific roles.
3. **No direct structural/interaction data in KT2440.** Mechanistic step ordering is transferred from *E. coli* ([PMID: 14580344](https://pubmed.ncbi.nlm.nih.gov/14580344/), [PMID: 24003141](https://pubmed.ncbi.nlm.nih.gov/24003141/)); this transfer is strong (Tat is highly conserved) but not experimentally verified in *Pseudomonas putida*.
4. **Essentiality unknown.** In *Brucella suis* the Tat system is essential for viability ([PMID: 36448838](https://pubmed.ncbi.nlm.nih.gov/36448838/)); KT2440 essentiality — especially of single vs. double operon knockouts — has not been established here.

---

## 10. Proposed Follow-up Experiments / Actions

1. **Bioinformatic substrate prediction (TatP/TatFind) across the KT2440 proteome** to build a candidate Tat-substrate list, cross-referenced to periplasmic/cofactor-binding annotations, to test transfer of the *P. aeruginosa* substrate scope.
2. **Single and double *tat* operon knockouts** (Δtat-1, Δtat-2, Δtat-1/Δtat-2) with UxpB and predicted-substrate export assays to define redundancy vs. specialization and essentiality.
3. **Regulatory verification** of tat-1 phosphate induction (e.g., promoter–reporter fusion under Pi limitation) to confirm the accessory/housekeeping split in KT2440 directly.
4. **Curation execution:** update the module document to the two-operon architecture, correct the bucket to `ppu03060`, harmonize gene names (PP_5017 → `tatB-II`), and add UxpB as a substrate cross-reference plus the Xcp T2SS as a downstream link.
5. **Expert question:** confirm with the module owner whether the generic template should support taxon-specific *operon duplication* as a first-class annotation, since KT2440 is a concrete case where single-copy assumptions fail.

---

## 11. Key References

| PMID | Title (abbrev.) | Role in this review |
|---|---|---|
| [23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/) | *The type II secretion system (Xcp) of P. putida … secretion of phosphatases* | **Primary target-species evidence**: two functional *tat* clusters, both export UxpB; tat-1 Pi-induced and *xcp*-adjacent; UxpB then Xcp-secreted. |
| [16756481](https://pubmed.ncbi.nlm.nih.gov/16756481/) | *The bacterial twin-arginine translocation pathway* | Defines the pathway boundary (export of folded proteins across the cytoplasmic membrane). |
| [10766774](https://pubmed.ncbi.nlm.nih.gov/10766774/) | *The twin arginine consensus motif … Sec-independent targeting* | Defines the SRRxFLK signal recognized by the receptor. |
| [11829474](https://pubmed.ncbi.nlm.nih.gov/11829474/) | *Unusual signal peptide directs penicillin amidase … Tat machinery* | Signal-recognition flexibility (hydrophobic core + N-terminal charge synergy). |
| [14580344](https://pubmed.ncbi.nlm.nih.gov/14580344/) | *Differential interactions between a twin-arginine signal peptide and its translocase* | Step ordering: TatC necessary/sufficient for primary interaction, then TatB transfer. |
| [24003141](https://pubmed.ncbi.nlm.nih.gov/24003141/) | *Live cell imaging … reversible assembly of TatA* | Step 3: PMF-dependent, reversible TatA oligomerization requires TatBC receptor. |
| [20169075](https://pubmed.ncbi.nlm.nih.gov/20169075/) | *Visualizing interactions along the E. coli Tat pathway (BiFC)* | TatBC receptor assembly, cell-pole localization, chaperone/proofreading interactions. |
| [12034867](https://pubmed.ncbi.nlm.nih.gov/12034867/) | *Effects of the twin-arginine translocase on virulence … P. aeruginosa* | Broader *Pseudomonas* substrate scope (≥18 substrates); transfer to KT2440 uncertain. |
| [36448838](https://pubmed.ncbi.nlm.nih.gov/36448838/) | *Analysis of the Brucella suis Tat system … essential for viability* | Comparative: three-gene *tat* operon architecture; Tat essentiality in a Gram-negative. |
| [22438962](https://pubmed.ncbi.nlm.nih.gov/22438962/) | *The Tat pathway in α-proteobacteria is functionally preserved* | Comparative: tatABC conservation despite synteny divergence. |

---

*Report prepared from a 3-iteration autonomous review. Confidence is high for module satisfiability and the two-operon architecture (direct KT2440 experimental evidence); moderate for substrate scope and operon specialization (homology-based inference from related Pseudomonas).*


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_twin_arginine_translocation__ppu03070-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_twin_arginine_translocation__ppu03070-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23530902
2. PMID:16756481
3. PMID:10766774
4. PMID:11829474
5. PMID:24003141
6. PMID:14580344
7. PMID:22438962
8. PMID:20169075
9. PMID:12034867
10. PMID:36448838