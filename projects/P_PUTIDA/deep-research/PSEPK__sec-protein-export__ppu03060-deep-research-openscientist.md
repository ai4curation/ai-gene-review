---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T15:28:31.366731'
end_time: '2026-08-08T15:52:16.613440'
duration_seconds: 1425.25
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: sec_protein_export
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu03060
  pathway_id: ppu03060
  pathway_name: Protein export
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03060 with 19 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '19'
  candidate_genes: '- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase
    YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)

    - secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)

    - secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)

    - lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein
    signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket
    kegg:ppu03060)

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

    - secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8;
    primary bucket kegg:ppu03060)

    - lepB: PP_1432 | Q88MY6 | Signal peptidase I (EC 3.4.21.89) (EC 3.4.21.89; primary
    bucket kegg:ppu03060)

    - ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four
    homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)

    - tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA
    (primary bucket kegg:ppu03060)

    - tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary
    bucket kegg:ppu03060)

    - tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC
    (primary bucket kegg:ppu03060)

    - secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)

    - ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor)
    (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)

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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__sec-protein-export__ppu03060-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__sec-protein-export__ppu03060-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

sec_protein_export in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03060
- Resolved ID: ppu03060
- Resolved name: Protein export
- Source: KEGG

Resolved local bucket kegg:ppu03060 with 19 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 19

- yidC: PP_0006 | P0A140 | Membrane protein insertase YidC (Foldase YidC) (Membrane integrase YidC) (Membrane protein YidC) (primary bucket kegg:ppu03060)
- secE: PP_0441 | Q88QP7 | Protein translocase subunit SecE (primary bucket kegg:ppu03060)
- secY: PP_0474 | Q88QL5 | Protein translocase subunit SecY (primary bucket kegg:ppu03060)
- lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket kegg:ppu03060)
- yajC: PP_0834 | Q88PL6 | Sec translocon accessory complex subunit YajC (primary bucket kegg:ppu03060)
- secD: PP_0835 | Q88PL5 | Protein translocase subunit SecD (primary bucket kegg:ppu03060)
- secF: PP_0836 | Q88PL4 | Protein-export membrane protein SecF (primary bucket kegg:ppu03060)
- tatC-I: PP_1039 | Q88P14 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- tatB-I: PP_1040 | Q88P13 | Sec-independent protein translocase TatB (primary bucket kegg:ppu03060)
- tatA-I: PP_1041 | Q88P12 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- secA: PP_1345 | Q88N69 | Protein translocase subunit SecA (EC 7.4.2.8) (EC 7.4.2.8; primary bucket kegg:ppu03060)
- lepB: PP_1432 | Q88MY6 | Signal peptidase I (EC 3.4.21.89) (EC 3.4.21.89; primary bucket kegg:ppu03060)
- ffh: PP_1461 | Q88MV7 | Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- tatA-II: PP_5016 | Q88D13 | Sec-independent protein translocase protein TatA (primary bucket kegg:ppu03060)
- tatB: PP_5017 | Q88D12 | Sec-independent protein translocase protein TatB (primary bucket kegg:ppu03060)
- tatC-II: PP_5018 | Q88D11 | Sec-independent protein translocase protein TatC (primary bucket kegg:ppu03060)
- secB: PP_5053 | Q88CX7 | Protein-export protein SecB (primary bucket kegg:ppu03060)
- ftsY: PP_5111 | Q88CR9 | Signal recognition particle receptor FtsY (SRP receptor) (EC 3.6.5.4) (EC 3.6.5.4; primary bucket kegg:ppu03060)
- secG: PP_5706 | A0A140FWQ9 | Protein-export membrane protein SecG (primary bucket kegg:ppu03060)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

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

# Module/Pathway/Taxon Review: `sec_protein_export` (KEGG ppu03060, "Protein export") in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** `kegg:ppu03060` — "Protein export" (module area: other_kegg_pathway)
**Candidate genes reviewed:** 19 protein-coding loci + 2 ncRNA features

---

## 1. Executive summary

The KEGG **ppu03060 "Protein export"** module is **fully satisfiable** in *Pseudomonas putida* KT2440 and should be marked **covered**. Every canonical step of the bacterial inner-membrane protein-export apparatus is encoded by a genuine, canonically annotated gene in the KT2440 genome: cytoplasmic chaperone/targeting factors (SecB, the SRP components Ffh + FtsY + 4.5S RNA), the SecA ATPase motor, the SecYEG protein-conducting channel, the accessory SecDF–YajC complex, the YidC membrane insertase, the twin-arginine (Tat) translocase, and both signal peptidases (LepB / SPase I and LspA / SPase II). No canonical step is missing, and the over-annotation risk across the 19 candidate loci is low — each maps 1:1 to a canonical single-copy protein-export KEGG Orthology (KO) identifier.

The single substantive, curation-relevant biological feature is a **genuine duplication of the Tat translocase into two complete, functional gene clusters** (`tat-1` = PP_1039–PP_1041 and a second cluster = PP_5016–PP_5018). This is real lineage-relevant paralogy — not redundant or over-propagated annotation — and is supported by direct experimental evidence in *P. putida* itself: both clusters can transport the Tat substrate UxpB, and the `tat-1` cluster is transcriptionally induced under phosphate limitation. This duplication should be recorded as paralogy in the module rather than collapsed.

Two minor housekeeping fixes remain. First, the second Tat cluster's TatB (PP_5017) is labeled `tatB` in the metadata without the `-II` suffix used for its cluster-mates (`tatA-II`, `tatC-II`) and should be relabeled `tatB-II` for internal consistency. Second, the SRP 4.5S RNA "duplication" (PP_mr49 + PP_mr50, both mapped to K01983) is **not** a real gene duplication: the two features occupy essentially the same genomic coordinates (they overlap over 96 nt, offset by 1 bp) and represent two Rfam covariance-model hits ("Bacteria_small_SRP" and "Bacteria_large_SRP") on a single RNA locus; they should be collapsed to one SRP-RNA step. Finally, the module boundary versus the physically adjacent Xcp type II secretion system (T2SS; KEGG ppu03070) is correct as drawn and must be kept distinct — ppu03060 covers *inner-membrane translocation and signal-peptide processing*, whereas Xcp handles the subsequent *outer-membrane secretion* step.

---

## 2. Target-organism pathway definition

**Process included in ppu03060.** KEGG map 03060 "Protein export" covers the machinery that moves newly synthesized proteins **from the cytoplasm across (or into) the cytoplasmic/inner membrane**, plus the proteolytic maturation of their signal peptides. In a Gram-negative bacterium like *P. putida* KT2440 this comprises the following functional sub-modules:

1. **Co-translational targeting (SRP pathway):** signal recognition particle Ffh + its 4.5S RNA, delivered to the membrane receptor FtsY.
2. **Post-translational targeting and translocation (Sec pathway):** the chaperone SecB, the ATPase motor SecA, the SecYEG channel, and the accessory SecDF–YajC complex that enhances throughput.
3. **Membrane-protein insertion:** the YidC insertase, which acts both in concert with SecYEG and independently (Sec-independent) for certain small membrane proteins.
4. **Folded-protein export (Tat pathway):** the twin-arginine translocase TatABC, which exports **already-folded** proteins bearing a twin-arginine (S/T-R-R-x-F-L-K) signal.
5. **Signal-peptide processing:** signal peptidase I (LepB) for general secretory substrates and signal peptidase II (LspA) for lipoproteins.

**Neighboring pathways to keep separate.** The most important boundary is with the **Xcp type II secretion system (KEGG ppu03070, "Bacterial secretion system")**, whose genes sit immediately downstream of the `tat-1` cluster in the KT2440 genome (PP_1042–PP_1054). ppu03060 ends at the inner membrane; the T2SS begins at the periplasm and delivers proteins across the *outer* membrane. Other broad overview maps that should not be merged into this bucket include the general "Bacterial secretion system" map (which aggregates T1SS–T6SS) and the ribosome/translation maps upstream.

**Alternate names / database definitions.** The module is referred to as the "Sec/protein export" or "general secretory (Sec) pathway" plus the "twin-arginine translocation (Tat)" pathway. KEGG bundles both Sec and Tat under a single "Protein export" map; other resources (e.g., TransportDB, MetaCyc) split them. Curators should be aware that "protein export" in KEGG is broader than the Sec translocon alone — it explicitly includes SRP targeting, YidC insertion, Tat, and both signal peptidases.

---

## 3. Expected step model

The table below lists the canonical steps expected for a Gram-negative γ-proteobacterium and the KT2440 candidate gene assigned to each. All steps are **covered**.

| Functional step | Canonical gene(s) | KT2440 locus | KO | Status |
|---|---|---|---|---|
| Cytoplasmic chaperone (post-translational) | SecB | PP_5053 | K03071 | covered |
| SRP protein (co-translational targeting) | Ffh | PP_1461 | K03106 [EC:3.6.5.4] | covered |
| SRP receptor | FtsY | PP_5111 | K03110 [EC:3.6.5.4] | covered |
| SRP 4.5S RNA | *ffs*/SRP RNA | PP_mr49 (+PP_mr50) | K01983 | covered (single locus; see §5) |
| ATPase motor | SecA | PP_1345 | K03070 [EC:7.4.2.8] | covered |
| Channel core | SecY | PP_0474 | K03076 | covered |
| Channel subunit | SecE | PP_0441 | K03073 | covered |
| Channel subunit | SecG | PP_5706 | K03075 | covered |
| Accessory translocation | SecD | PP_0835 | K03072 | covered |
| Accessory translocation | SecF | PP_0836 | K03074 | covered |
| Accessory translocation | YajC | PP_0834 | K03210 | covered |
| Membrane insertase | YidC | PP_0006 | K03217 | covered |
| Tat translocase (cluster I) | TatA/TatB/TatC | PP_1041 / PP_1040 / PP_1039 | K03116 / K03117 / K03118 | covered (paralog cluster 1) |
| Tat translocase (cluster II) | TatA/TatB/TatC | PP_5016 / PP_5017 / PP_5018 | K03116 / K03117 / K03118 | covered (paralog cluster 2) |
| Signal peptidase I | LepB | PP_1432 | K03100 [EC:3.4.21.89] | covered |
| Signal peptidase II | LspA | PP_0604 | K03101 [EC:3.4.23.36] | covered |

**Steps probably not expected / not applicable in this organism.** There are no Gram-positive-specific accessory export components (e.g., a dedicated SecA2/SecY2 accessory system, or the single-fusion SecDF protein form) expected here; KT2440 uses the standard γ-proteobacterial SecDF two-gene arrangement, which is present. No step is judged *not_expected_in_target_taxon* — the module is complete for a Gram-negative organism.

---

## 4. Candidate genes and evidence

### Finding F001 — the export apparatus is complete

KEGG REST (`link/ppu/path:ppu03060`) returns **19 protein-coding genes plus 2 ncRNAs** for this pathway in KT2440, and these cover every canonical export step with no gaps. The cytoplasmic/targeting layer is provided by SecB (PP_5053) for post-translational hand-off and the SRP system — Ffh (PP_1461), the FtsY receptor (PP_5111), and the 4.5S SRP RNA (PP_mr49/PP_mr50, K01983) — for co-translational targeting. The translocation core comprises the SecA ATPase (PP_1345), the SecYEG channel (SecY PP_0474 / SecE PP_0441 / SecG PP_5706), and the accessory SecDF–YajC complex (SecD PP_0835 / SecF PP_0836 / YajC PP_0834). Membrane-protein insertion is served by YidC (PP_0006, K03217). Folded-protein export runs through the Tat translocase, present in **two** clusters (PP_1039–1041 and PP_5016–5018). Signal-peptide maturation is handled by signal peptidase I (LepB PP_1432, K03100) and signal peptidase II (LspA PP_0604, K03101). This is the basis for marking the module **covered/satisfiable**.

### Finding F004 — clean, canonical KO assignments; low over-annotation risk

Retrieving the full KEGG records (`get`) for all 19 loci shows each maps **1:1 to a canonical single-copy protein-export KO**: YidC → K03217; SecE → K03073; SecY → K03076; LspA → K03101 [EC:3.4.23.36]; YajC → K03210; SecD → K03072; SecF → K03074; TatC → K03118; TatB → K03117; TatA → K03116; SecA → K03070 [EC:7.4.2.8]; LepB → K03100 [EC:3.4.21.89]; Ffh → K03106 [EC:3.6.5.4]; SecB → K03071; FtsY → K03110; SecG → K03075. This is a "clean" bucket: there are no promiscuous multi-KO mappings, no broad EC terms that would raise over-propagation concerns, and no orphan loci. The only two annotation caveats are the SRP-RNA double annotation and the Tat paralog labeling, both discussed in §5.

**Curation-relevant notes on individual genes.**

- **YidC (PP_0006, P0A140).** UniProt carries the mature-protein description "Membrane protein insertase YidC (Foldase / Integrase / Membrane protein YidC)." Its dual role — Sec-associated *and* Sec-independent membrane insertion — is well established biochemically in *E. coli* (see §6), so the KT2440 annotation is safe by strong homology. P0A140 is a shared/identical-sequence accession, worth a confirmatory note but not a problem.
- **SecA (PP_1345).** EC 7.4.2.8 (the reclassified protein-translocating ATPase EC) is correct and current; no caveat.
- **LepB (PP_1432) / LspA (PP_0604).** The two signal peptidases have distinct, non-overlapping EC numbers (3.4.21.89 SPase I; 3.4.23.36 SPase II) and substrate classes (general secretory vs lipoprotein). Both are single-copy; clean.
- **Tat loci.** See F002/F003 below — genuine paralogy, high-confidence.

### Finding F002 — two functional Tat clusters (genuine paralogy)

Direct *P. putida* evidence establishes that the two Tat clusters are **both real and both functional**, not an annotation artifact. Putker et al. 2013 ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)) state: *"Two different tat gene clusters were detected in the P. putida genome, of which one, named tat-1, is located adjacent to the uxpB and xcp genes. Both Tat systems appeared to be capable of transporting the UxpB protein."* The `tat-1` cluster is strongly induced under low phosphate. In the KEGG bucket these correspond to **tatA-I / tatB-I / tatC-I (PP_1041 / PP_1040 / PP_1039)** and **tatA-II / tatB / tatC-II (PP_5016 / PP_5017 / PP_5018)**. Because functional competence of both clusters was demonstrated in the target species itself, the transfer of this conclusion to KT2440 is **strong (direct)**. Curators should record the Tat step as covered by **paralogous duplication**, keeping both clusters.

### Finding F003 — pathway boundary vs the Xcp T2SS

The `tat-1` cluster sits immediately upstream of the Xcp type II secretion system genes (PP_1042–PP_1054) in the genome, which can invite accidental merging of the two modules. They are, however, mechanistically distinct steps in a two-stage export route: Tat (+ signal peptidase II) moves the folded substrate across the *inner* membrane; Xcp then secretes it across the *outer* membrane. Putker et al. 2013 experimentally separated these steps for the substrate UxpB: *"both processing by leader peptidase II and Tat dependency were experimentally confirmed"* ([PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)), and the Xcp genes "encode an active T2SS." The ppu03060 / ppu03070 boundary is therefore **correct as drawn** and should be preserved.

---

## 5. Gaps, ambiguities, and likely over-annotations

There are **no true pathway gaps** in ppu03060 for KT2440. The remaining items are annotation/labeling issues, not biological gaps.

### 5.1 SRP 4.5S RNA is one locus double-annotated (Finding F005)

The metadata lists two ncRNA features, **PP_mr49** ("Bacteria_small_SRP") and **PP_mr50** ("Bacteria_large_SRP"), both mapping to K01983. KEGG POSITION records show these are essentially the same physical locus:

```
PP_mr49 = complement(4858397..4858493)   (97 nt)
PP_mr50 = complement(4858398..4858494)   (97 nt)
          └── overlap of 96 nt, offset by exactly 1 bp ──┘
```

This is a **single SRP RNA gene** that returned two overlapping Rfam covariance-model hits (a "small SRP" and a "large SRP" model). It is *not* a gene duplication. For module satisfiability, the SRP-RNA step should be counted **once** (covered), and the duplicate feature should be flagged for collapse in the underlying annotation.

### 5.2 Tat paralogy — labeling inconsistency, not over-annotation

The Tat duplication is genuine (see F002) and should be retained as paralogy. The only issue is cosmetic: the second cluster's TatB is labeled **`tatB` (PP_5017)** without the `-II` suffix that its cluster-mates carry (`tatA-II` PP_5016, `tatC-II` PP_5018). **Recommendation: relabel PP_5017 → `tatB-II`** for consistency and to prevent it being mistaken for a lone/unpaired TatB.

### 5.3 No broad-EC or over-propagation concerns

Every protein-coding locus maps to a single, specific KO, and where EC numbers are present they are narrow and correct (SecA 7.4.2.8; LepB 3.4.21.89; LspA 3.4.23.36; Ffh/FtsY 3.6.5.4). There is no evidence of a promiscuous or over-propagated annotation among the 19 candidates.

---

## 6. Module and GO-curation recommendations

| Module step | Recommendation | Rationale |
|---|---|---|
| SecB, SecA, SecYEG, SecDF–YajC | **covered** | Single-copy, canonical KOs; core Sec present. |
| SRP (Ffh, FtsY) | **covered** | Canonical; single-copy. |
| SRP 4.5S RNA | **covered (collapse duplicate)** | PP_mr49/PP_mr50 are one overlapping locus; count once. |
| YidC insertase | **covered** | K03217; role confirmed by strong *E. coli* biochemistry. |
| Tat translocase | **covered (record as paralogy)** | Two functional clusters demonstrated directly in *P. putida*. |
| Signal peptidase I (LepB) | **covered** | K03100; single-copy. |
| Signal peptidase II (LspA) | **covered** | K03101; single-copy. |
| Overall module | **covered / satisfiable** | No missing steps. |

**Module-boundary guidance.** The generic module boundaries are **correct for this organism**. Keep ppu03060 (Sec/SRP/Tat/YidC/signal peptidases) distinct from ppu03070 (Xcp T2SS / bacterial secretion systems). No new module document is required. No new GO-term request is triggered — existing GO terms for Sec translocation (GO:0043952), SRP-dependent targeting (GO:0006614/0006616), Tat translocation (GO:0043953), and signal-peptide processing cover all present steps.

**Housekeeping edits to request in the annotation source:**
1. Relabel PP_5017 as `tatB-II`.
2. Collapse PP_mr49 / PP_mr50 to a single SRP-RNA feature (or annotate one as the canonical gene and the other as a redundant Rfam hit).

---

## 7. Genes to promote to full review

Most loci are clean and do not need individual `fetch-gene` review. The following are worth promoting, in priority order:

1. **Tat cluster loci (PP_1039–PP_1041 and PP_5016–PP_5018)** — promote as a **set**. These are the one biologically substantive curation feature (genuine paralogy with direct functional evidence and differential regulation). A full review should confirm substrate ranges, the `-II` relabeling of PP_5017, and the genomic-context boundary with Xcp.
2. **SRP RNA features (PP_mr49 / PP_mr50)** — promote for a quick **annotation-cleanup** review to collapse the double annotation.
3. **YidC (PP_0006)** — optional promotion; the shared accession (P0A140) and its dual Sec-dependent/Sec-independent role make it worth a confirmatory note, though the annotation is safe.

The remaining 12 protein-coding loci (SecB, SecA, SecY, SecE, SecG, SecD, SecF, YajC, Ffh, FtsY, LepB, LspA) are high-confidence single-copy members and do **not** require individual promotion.

---

## Mechanistic model / interpretation

The KT2440 protein-export system is a textbook Gram-negative apparatus with one lineage-specific twist (Tat duplication). The flow of a secreted protein through the module:

```
              CYTOPLASM
   ┌───────────────────────────────────────────┐
   │  Ribosome ── nascent chain                 │
   │      │                                     │
   │   ┌──┴── co-translational ──┐              │
   │  SRP(Ffh)+4.5S RNA        SecB (post-      │
   │      │                     translational   │
   │   FtsY (receptor)          chaperone)      │
   │      │                        │            │
   └──────┼────────────────────────┼────────────┘
          ▼                        ▼
   ═════ SecYEG channel ◄──── SecA (ATPase motor) ═══  INNER
          │  + SecDF–YajC (accessory)                   MEMBRANE
          │
      YidC (membrane-protein insertion; Sec-assoc & Sec-independent)
   ─────────────────────────────────────────────────────────────
   Folded proteins (twin-Arg signal):
      TatABC cluster I  (PP_1039-41) ─┐
      TatABC cluster II (PP_5016-18) ─┴──► across inner membrane
   ─────────────────────────────────────────────────────────────
   Signal-peptide processing:  LepB (SPase I, general)
                               LspA (SPase II, lipoproteins)
              PERIPLASM
   ┌────────────────────────────────────────────────────────────┐
   │  (mature protein) ──► Xcp T2SS (ppu03070) ──► OUTER MEMBRANE │
   └────────────────────────────────────────────────────────────┘
```

Two features give the module its species-specific character. First, the **Tat duplication**: `tat-1` (PP_1039–1041) sits next to the `uxpB`/`xcp` genes and is phosphate-regulated, suggesting a dedicated role in exporting periplasmic phosphatases under Pi limitation, while the second cluster (PP_5016–5018) provides an additional or housekeeping Tat capacity. Both are functional for UxpB export. Second, the **two-stage export logic** for folded periplasmic enzymes: Tat + SPase II move the substrate across the inner membrane (ppu03060), then Xcp secretes it across the outer membrane (ppu03070) — the reason the two maps are physically adjacent yet mechanistically separate.

---

## Evidence base

| PMID | Title (abbrev.) | Relevance to this review |
|---|---|---|
| [23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/) | *Type II secretion system (Xcp) of P. putida is active…* | **Direct, target-species.** Documents two functional Tat clusters, `tat-1` adjacency to `uxpB`/`xcp`, Pi induction, and experimental separation of Tat/SPase II export from Xcp T2SS secretion. Supports F002, F003. |
| [14739936](https://pubmed.ncbi.nlm.nih.gov/14739936/) | *E. coli YidC is a membrane insertase for Sec-independent proteins* | Confirms YidC's Sec-independent insertase function; supports the KT2440 YidC (PP_0006) annotation by strong homology. |
| [18996118](https://pubmed.ncbi.nlm.nih.gov/18996118/) | *Pf3 coat protein contacts TM1/TM3 of YidC…* | Mechanistic detail of YidC substrate contacts; corroborates YidC insertase role. |
| [30093651](https://pubmed.ncbi.nlm.nih.gov/30093651/) | *Genome-wide identification of P. aeruginosa Tat substrates* | *Pseudomonas* (related-species) evidence that Tat exports a large, niche-relevant substrate set; contextualizes the physiological importance of the KT2440 Tat clusters. |
| [27279369](https://pubmed.ncbi.nlm.nih.gov/27279369/) | *Contribution of Tat to the exoproteome of P. aeruginosa* | Related-species: Tat feeds substrates onward to secretion, including T2SS — supports the ppu03060→ppu03070 hand-off logic. |
| [36448838](https://pubmed.ncbi.nlm.nih.gov/36448838/) | *Brucella suis Tat system essential for viability* | Broader bacterial context: three-gene *tatABC* operon organization; frames the KT2440 clusters as canonical Tat operons. |
| [27501981](https://pubmed.ncbi.nlm.nih.gov/27501981/) | *Tat pathway functions in Yersinia pseudotuberculosis* | Broader context on Tat physiology/regulation; not target-specific. |
| [23687945](https://pubmed.ncbi.nlm.nih.gov/23687945/) | *Broad host range vectors… periplasmic YFP export in P. putida KT2440* | Target-species: demonstrates functional Sec-mediated periplasmic export in KT2440, confirming an active general secretory pathway. |

**Species-transfer caveats.** The Tat duplication and the Tat/Xcp boundary are supported by **direct KT2440/*P. putida* evidence** (Putker 2013) — strong transfer. YidC mechanism rests on *E. coli* biochemistry — strong by deep conservation but formally a homology transfer. The broader Tat-substrate/physiology papers are from *P. aeruginosa*, *Yersinia*, and *Brucella* — useful context but **not** direct evidence for KT2440 substrate sets.

---

## Limitations and knowledge gaps

- **No proteomic/genetic verification within this review.** Coverage was established from KEGG KO assignments and genome coordinates plus literature; we did not experimentally confirm expression or essentiality of each locus in KT2440. The Sec core is essential in all bacteria, so this is low-risk, but it remains inference.
- **Tat substrate range in KT2440 is only partly known.** Direct evidence exists for UxpB; the full KT2440 Tat substrate repertoire (analogous to the 34 validated *P. aeruginosa* substrates) has not been mapped. Which cluster serves which substrate under which condition is not fully resolved.
- **Functional differentiation of the two Tat clusters.** Both can transport UxpB, but whether they are redundant, specialized, or differentially regulated beyond the Pi induction of `tat-1` is unresolved.
- **YidC shared accession.** P0A140 is an identical-sequence/shared accession; a confirmatory check that it maps uniquely to PP_0006 in KT2440 would remove residual ambiguity.
- **SRP-RNA collapse depends on the source annotation.** The recommendation to collapse PP_mr49/PP_mr50 assumes the coordinate overlap reflects a single locus; this should be verified in the authoritative genome annotation before editing.

---

## Proposed follow-up experiments / actions

1. **Curation edits (immediate, low effort):**
   - Relabel PP_5017 → `tatB-II`.
   - Collapse PP_mr49 / PP_mr50 into a single SRP-RNA feature (K01983); mark the redundant Rfam hit.
   - Record the Tat step as **covered by paralogy** with both clusters retained.
2. **Promote the Tat cluster set to full `fetch-gene` review** to document substrate ranges, regulation, and the genomic boundary with Xcp (ppu03070).
3. **Experimental (if resources permit):** an amidase- or reporter-based Tat-substrate screen in KT2440 (analogous to the *P. aeruginosa* work, [PMID: 30093651](https://pubmed.ncbi.nlm.nih.gov/30093651/)) to map the target-species Tat substrate set and test whether the two clusters have distinct substrate preferences.
4. **Confirm YidC accession uniqueness** (P0A140 → PP_0006) in the KT2440 proteome.
5. **Verify Sec-core expression** via existing KT2440 transcriptomic/proteomic datasets to add direct evidence beyond homology (optional, low priority).

---

## 8. Key references

- Putker F. et al. (2013). *The type II secretion system (Xcp) of Pseudomonas putida is active and involved in the secretion of phosphatases.* [PMID: 23530902](https://pubmed.ncbi.nlm.nih.gov/23530902/)
- Serek J. et al. (2004). *Escherichia coli YidC is a membrane insertase for Sec-independent proteins.* [PMID: 14739936](https://pubmed.ncbi.nlm.nih.gov/14739936/)
- *The Pf3 coat protein contacts TM1 and TM3 of YidC during membrane biogenesis.* [PMID: 18996118](https://pubmed.ncbi.nlm.nih.gov/18996118/)
- *Genome-wide identification and experimental validation of Pseudomonas aeruginosa Tat substrates.* [PMID: 30093651](https://pubmed.ncbi.nlm.nih.gov/30093651/)
- *Contribution of the Twin Arginine Translocation system to the exoproteome of Pseudomonas aeruginosa.* [PMID: 27279369](https://pubmed.ncbi.nlm.nih.gov/27279369/)
- *Analysis of the Brucella suis Twin Arginine Translocation System…* [PMID: 36448838](https://pubmed.ncbi.nlm.nih.gov/36448838/)
- *Transcriptomic and phenotypic analysis of the Tat pathway in Yersinia pseudotuberculosis.* [PMID: 27501981](https://pubmed.ncbi.nlm.nih.gov/27501981/)
- *Broad host range vectors for expression of proteins… in Pseudomonas putida KT2440.* [PMID: 23687945](https://pubmed.ncbi.nlm.nih.gov/23687945/)

---

*Data sources: KEGG REST (`link`/`get`/`find` on `ppu03060` and constituent loci), UniProt, and the cited literature. Findings F001–F005 as recorded in the knowledge state.*


## Artifacts

- [OpenScientist final report](PSEPK__sec-protein-export__ppu03060-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__sec-protein-export__ppu03060-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23530902
2. PMID:30093651
3. PMID:14739936
4. PMID:18996118
5. PMID:27279369
6. PMID:36448838
7. PMID:27501981
8. PMID:23687945