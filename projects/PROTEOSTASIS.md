---
title: Human Proteostasis Network
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
priority: high
scope: Full Proteostasis Consortium workbook and manuscripts; unfolded protein binding is a sub-use case
sidecars:
  priority_genes: PROTEOSTASIS/priority_genes.tsv
  review_batches: PROTEOSTASIS/review_batches.tsv
  mapping_sets_dir: PROTEOSTASIS/mappings
  tests_dir: PROTEOSTASIS/tests
  reports_dir: PROTEOSTASIS/reports
  upb_genes: UNFOLDED_PROTEIN_BINDING/genes.csv
related_projects:
  - UNFOLDED_PROTEIN_BINDING.md
  - RIBOSOME_QUALITY_CONTROL.md
  - INTEGRATED_STRESS_RESPONSE.md
  - ER_PHAGY.md
external_sources:
  - Human Proteostasis Network Annotation 4.3.11 workbook (release 2026-04-17)
  - Survey of the Human PN MS1 Translation Folding Transport
  - Survey of the Human PN MS2 ALP
  - Survey of the Human PN MS3 UPS
review_batches:
  - id: proteostasis-pr-1217
    title: "[codex] Review proteostasis network genes"
    source_pr: 1217
    source_pr_url: "https://github.com/ai4curation/ai-gene-review/pull/1217"
    merged_at: "2026-06-02T19:59:17Z"
    species: human
    gene_count: 50
    sidecar: PROTEOSTASIS/review_batches.tsv
  - id: proteostasis-batch-2026-06-03
    title: "Proteostasis PN projected candidate additions batch 2"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 50
    sidecar: PROTEOSTASIS/review_batches.tsv
  - id: proteostasis-batch-2026-06-06
    title: "Proteostasis PN candidate additions batch 3 (V-ATPase, ER folding/QC, autophagy receptors, co-chaperone/UPS)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 20
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch3_selection_notes.md
  - id: proteostasis-batch-2026-06-07
    title: "Proteostasis PN candidate additions batch 4 (V-ATPase tissue isoforms + ClC-7, mito/ER chaperones, collagen biogenesis, histone chaperones, CRL/UPS adaptors, CK2/CK1)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 30
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch4_selection_notes.md
  - id: proteostasis-batch-2026-06-07b
    title: "Proteostasis PN candidate additions batch 5 (protein-folding chaperone & co-chaperone network: DNAJ/HSP40 family, small HSPs, HSP70/HSP90 hub co-chaperones, FKBP immunophilins, ER oxidative folding/PPIases)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 50
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch5_selection_notes.md
  - id: proteostasis-batch-2026-06-07c
    title: "Proteostasis PN candidate additions batch 6 (co-translational quality control: ribosome-associated QC & ribosome rescue, UFMylation, NMD surveillance, nascent-chain N-terminal acetylation)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 50
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch6_selection_notes.md
  - id: proteostasis-batch-2026-06-11
    title: "Proteostasis PN candidate additions batch 7 (ER protein biogenesis & ERAD: SRP/translocon/signal peptidase, EMC & GET membrane-protein insertion, ER glycoprotein-folding QC mannosidases/lectins, collagen prolyl hydroxylases & ER thioredoxins, ERAD ubiquitin machinery)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 50
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch7_selection_notes.md
  - id: proteostasis-batch-2026-06-13
    title: "Proteostasis PN candidate additions batch 8 (UPS branch: Cullin-RING ligase substrate-recognition & assembly modules — F-box SCF/CRL1 substrate receptors FBXL/FBXW/FBXO incl. lectin F-box ERAD subfamily and APC/C-inhibitor F-box members, plus CRL4 core DDB1/DDB2/DDA1/DTL and CRL assembly regulators CAND2/GLMN)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 50
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch8_selection_notes.md
  - id: proteostasis-batch-2026-06-14
    title: "Proteostasis PN candidate additions batch 9 (ALP branch: selective autophagy cargo recognition — SQSTM1/NBR1/OPTN/CCDC50/NUFIP1/RETREG2 receptors, TBK1/AZI2/TANK activation axis, TRIM5/13/16/17, ubiquitin-tagging E3s SIAH1/RNF41/RNF166/LRSAM1, plus MEFV/NLRX1/MAP1S)"
    status: in_progress
    source_report: PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
    species: human
    target_gene_count: 20
    sidecar: PROTEOSTASIS/review_batches.tsv
    selection_notes: PROTEOSTASIS/batch9_selection_notes.md
---
# Human Proteostasis Network Project

## Background

Proteostasis is used here in the broad systems sense: the cellular machinery that
supports protein synthesis, folding, trafficking, quality control, sequestration,
and degradation.

The source resource analyzed in this project is the **Human Proteostasis Network
Annotation 4.3.11** workbook together with three Proteostasis Consortium survey
manuscripts:

- `MS1` introduces the overall PN framework and covers translation, folding,
  transport, and organelle-specific proteostasis systems.
- `MS2` covers the autophagy-lysosome pathway (`ALP`) and provides the most
  detailed row-level notes and references in the current release.
- `MS3` covers the ubiquitin-proteasome system (`UPS`) and explains the
  domain-heavy inclusion and classification logic used for that branch.

The mapping and browser artifacts now use the `2026-04-17` PN `4.3.11`
workbook. Earlier 2024 release artifacts are kept only as provenance for
individual curation comments that were started against that release.

## Overview

The Proteostasis Consortium workbook and papers define a curated human proteostasis
membership and role taxonomy. They do **not** define a GO-ready annotation set.

This project asks three main questions:

- What biological claims do the PN annotations actually make?
- Which PN statements are close to GO terms, which imply ontology gaps, and which
  are better treated as systems metadata?
- Which workbook entries look especially useful, curious, or suspect in the
  context of AIGR?

Within this project:

- the PN resource provides systems architecture and candidate roles
- unfolded protein binding is treated as one mechanistic subdomain within proteostasis
- AIGR uses PN as a scaffold, a QA source, and a prioritization layer

See:

- [Priority genes](PROTEOSTASIS/priority_genes.tsv)
- [Reviewed gene batches](PROTEOSTASIS/review_batches.tsv)
- [PN tree browser](PROTEOSTASIS/pn.html)
- [ALP mapping set](PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml)
- [Chaperone mapping set](PROTEOSTASIS/mappings/chaperone_systems.yaml)
- [ER proteostasis mapping set](PROTEOSTASIS/mappings/er_proteostasis.yaml)
- [Extracellular proteostasis mapping set](PROTEOSTASIS/mappings/extracellular_proteostasis.yaml)
- [Mitochondrial proteostasis mapping set](PROTEOSTASIS/mappings/mitochondrial_proteostasis.yaml)
- [Nuclear proteostasis mapping set](PROTEOSTASIS/mappings/nuclear_proteostasis.yaml)
- [PN regulation mapping set](PROTEOSTASIS/mappings/pn_regulation.yaml)
- [Translation mapping set](PROTEOSTASIS/mappings/translation.yaml)
- [UPS mapping set](PROTEOSTASIS/mappings/ubiquitin_proteasome_system.yaml)
- [Project-local tests](PROTEOSTASIS/tests)
- [Project-local reports](PROTEOSTASIS/reports)
- [Report-local PN tree browser](PROTEOSTASIS/reports/pn_taxonomy_tree/pn_taxonomy_tree.html)
- [Mapping scrutiny report](PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- [Unusual propagation report](PROTEOSTASIS/reports/pn_mapping_audit/unusual_propagations.tsv)
- [Mapping export workbook](PROTEOSTASIS/reports/pn_mappings/pn_mappings.xlsx)
- [UPB gene list](UNFOLDED_PROTEIN_BINDING/genes.csv)
- [Unfolded Protein Binding project](UNFOLDED_PROTEIN_BINDING.md)
- [Ribosome Quality Control project](RIBOSOME_QUALITY_CONTROL.md)
- [Integrated Stress Response project](INTEGRATED_STRESS_RESPONSE.md)
- [ER-phagy project](ER_PHAGY.md)

## Gene Review Tracking

The most recent PN review batch is
[`#1217`](https://github.com/ai4curation/ai-gene-review/pull/1217),
merged on `2026-06-02`. It reviewed `50` human proteostasis-network genes:
`49` new review YAMLs plus a refresh of the existing `PIK3C3` review. The
gene-level metadata for this batch is tracked in
[review_batches.tsv](PROTEOSTASIS/review_batches.tsv).

The current PN review batch, `proteostasis-batch-2026-06-03`, was selected from
the projected candidate additions report and has `50` human gene-review PR rows
in the same sidecar. Merged PRs record `merged_at`; open PRs keep that field
empty until merged.

Subsequent candidate-addition batches continued the rereview queue:
`proteostasis-batch-2026-06-06` (`20` genes), `proteostasis-batch-2026-06-07`
(`30` genes), and `proteostasis-batch-2026-06-07b` (`50` genes — the
protein-folding chaperone & co-chaperone network: the DNAJ/HSP40 J-domain family,
small heat-shock proteins, HSP70/HSP90 hub co-chaperones such as STUB1/CHIP,
STIP1/HOP, SGTA and SERPINH1/HSP47, FKBP immunophilin co-chaperones, and ER
oxidative-folding/PPIase enzymes including P4HB/PDI, ERO1A/B, ERP27/29 and
PPIB). The mega-hubs `HSPA5`, `HSP90AA1` and `HSP90AB1` were deliberately
deferred to dedicated single-gene reviews (50+ GOA terms each). See
[batch5_selection_notes.md](PROTEOSTASIS/batch5_selection_notes.md).

`proteostasis-batch-2026-06-07c` (`51` reviewed) covers the Translation
branch's co-translational quality-control machinery: ribosome-associated quality
control and ribosome rescue (LTN1, NEMF, ZNF598, PELO/HBS1L, GTPBP1/2, the
makorin and RNF14/RNF25 E3s, GIGYF1/2–4EHP, RACK1, TRIP4, MAP3K20/ZAK, GCN1,
NPLOC4/UFD1), the UFMylation cascade (UFM1, UBA5, UFC1, UFL1, UFSP1/2, DDRGK1),
NMD surveillance (UPF1/2/3A/3B), and nascent-chain N-terminal acetylation (HYPK,
NAA10/15/25/30/35/38/40), plus ribosome recycling (DENR/MCTS1/EIF2D/GTPBP6/
EEF2K). `HUWE1` and `OGT` were deferred as mega/pleiotropic. The batch totals
`51` because the `USP21` symbol resolved to the synonym gene `USP25` (also a
valid ERAD-associated DUB); both were reviewed. See
[batch6_selection_notes.md](PROTEOSTASIS/batch6_selection_notes.md).

`proteostasis-batch-2026-06-11` (`50` reviewed) covers the **ER proteostasis
branch**, walking the full ER lifecycle of a secretory/membrane protein:
co-translational SRP targeting (`SRP9/19/68/72`, `SRPRB`), Sec61-translocon
association and signal-peptide processing (`SEC62/63`, `SEC11A/C`,
`SPCS1/2/3`, `SERP1/2`), ER membrane-protein insertion by the EMC
(`EMC1/2/3/4/6/7/8/9/10`, `MMGT1`/EMC5) and GET/TRC tail-anchor pathway
(`GET1/3/4`), ER glycoprotein-folding quality control via the ERAD
mannosidases and cargo lectins (`EDEM1/2/3`, `MAN1B1`, `LMAN1/2`, `LMAN1L`,
`LMAN2L`), ER oxidative folding and collagen prolyl hydroxylation
(`P3H1/2`, `P4HA1/2/3`, `TXNDC11/12/16`), and the ERAD ubiquitin machinery and
membrane cofactors (`RNF5/185/170`, `FAF2`, `UBAC2`, `ERLIN1/2`). All `50`
review YAMLs validate; across `1347` reviewed annotations the action mix was
`783` ACCEPT, `476` KEEP_AS_NON_CORE, `75` MARK_AS_OVER_ANNOTATED, `8` REMOVE,
`3` MODIFY, `1` UNDECIDED, `1` NEW. Notable curation calls: REMOVE of
pathway-bleed-through IEA terms (`transmembrane transport` / `ER mannose
trimming` on the RNF5/RNF185 ERAD E3s), REMOVE of an over-propagated IBA serine
endopeptidase MF on the `UBAC2` rhomboid **pseudoprotease**, MARK_AS_OVER_ANNOTATED
of `ERLIN2` plasma-membrane and `MMGT1` legacy magnesium-transporter
annotations, and handling of negated (NOT) historical mannosidase annotations on
`EDEM1/EDEM2`. A shared caveat flagged for human follow-up: `PMID:23264731`
(MTR120/KIAA1383 microtubule study) is cited for a `cytoplasmic microtubule`
IDA on both `SERP1` (removed; full text confirms wrong gene) and `SRPRB`
(left UNDECIDED where full text was unavailable). The mega-hub ER chaperones
`HSPA5`/BiP, `HSP90B1`/GRP94, and the `ERN1`/`EIF2AK3` UPR sensors were deferred to
dedicated reviews. See
[batch7_selection_notes.md](PROTEOSTASIS/batch7_selection_notes.md).

`proteostasis-batch-2026-06-13` (`50` reviewed) moves into the **Ubiquitin–
Proteasome System (UPS) branch**, covering the **Cullin–RING ligase (CRL)
substrate-recognition & assembly modules**: the `44` F-box substrate receptors
of the SCF/CRL1 complex grouped by recognition module — leucine-rich-repeat
`FBXL3/5/6/7/8/12/13/14/15/16/17/18/20/22`, WD40 `FBXW2/4/5/7/8/9/10/12`, and
"other" `FBXO2/5/6/7/8/10/15/16/17/21/22/25/27/30/33/34/36/39/40/41/43/47` — plus
the CRL4 core/receptors (`DDB1` adaptor scaffold, `DDB2` and `DTL`/CDT2 DCAF
receptors, `DDA1` stabilizing subunit) and the CRL assembly regulators `CAND2`
(CAND1 paralog) and `GLMN`/glomulin. All `50` review YAMLs pass schema, term
(label + verbatim-quote), and best-practices validation; across `1590` reviewed
annotations the action mix was `649` ACCEPT, `878` KEEP_AS_NON_CORE, `23`
MARK_AS_OVER_ANNOTATED, `19` MODIFY, `11` NEW, `8` UNDECIDED, `2` REMOVE. The
dominant curation pattern is the recurring **MODIFY/NEW that replaces a catalytic
`ubiquitin protein ligase activity` / `ubiquitin-protein transferase activity`
(IEA/NAS) on an F-box receptor with `GO:1990756 ubiquitin-like ligase-substrate
adaptor activity`** — catalysis resides in the RBX1 RING, not the F-box adaptor —
while bare `protein binding` was uniformly kept non-core in favor of the
substrate-adaptor function. Notable calls: the **lectin/FBA F-box subfamily**
(`FBXO2/6/17/27`) was framed by carbohydrate/high-mannose-glycan binding feeding
ERAD/glycoprotein catabolism, but `FBXO17`'s ERAD term was MARK_AS_OVER_ANNOTATED
because the experimental characterization shows it does **not** bind high-mannose
glycans (only `FBXO2/FBXO6` do); the non-canonical "F-box" members `FBXO5`/EMI1
and `FBXO43`/EMI2 were framed as **APC/C inhibitors** (not productive SCF
receptors), with SCF-receptor IEA/NAS propagations marked non-core/over-annotated;
`CAND2` and `GLMN` were modeled as CRL **assembly regulators/inhibitors** with no
catalytic ligase activity assigned (`GLMN` core = `ubiquitin-protein transferase
inhibitor activity` + RBX1 binding). The `2` REMOVE calls are both clearly-wrong
IEA over-propagations — `FBXO21` `DNA binding` (a remote YccV/hemimethylated-DNA
fold match, not a function) and `FBXO43` `cellular response to NGF` (an
implausible Ensembl ortholog transfer onto a gonad-restricted meiotic APC/C
inhibitor). The mega/pleiotropic UPS hubs `HUWE1` and `OGT` were left out of
scope. See [batch8_selection_notes.md](PROTEOSTASIS/batch8_selection_notes.md).

`proteostasis-batch-2026-06-14` (`20` reviewed) moves into the
**Autophagy–Lysosome Pathway (ALP) branch** — the best-row-level-supported PN
branch — covering the **selective autophagy cargo-recognition** machinery: the
core selective autophagy receptors (`SQSTM1`/p62, `NBR1`, `OPTN`, `CCDC50`,
the ribophagy receptor `NUFIP1`, and the ER-phagy receptor `RETREG2`/FAM134A),
the TBK1 activation axis that phosphorylates those receptors (`TBK1`, `AZI2`/
NAP1, `TANK`), the TRIM-family receptors/regulators (`TRIM5`, `TRIM13`,
`TRIM16`, `TRIM17`), the ubiquitin-tagging E3 ligases that generate the
autophagy signal (`SIAH1`, `RNF41`/NRDP1, `RNF166`, `LRSAM1`), and the
selective-autophagy regulators `MEFV`/pyrin, `NLRX1`, and `MAP1S`. All `20`
review YAMLs pass schema, term (label + verbatim-quote), and best-practices
validation; across `1222` reviewed annotations the action mix was `690`
KEEP_AS_NON_CORE, `505` ACCEPT, `19` MARK_AS_OVER_ANNOTATED, `5` NEW, `2`
UNDECIDED, `1` REMOVE. The dominant curation pattern is the recurring elevation
of the **selective-autophagy cargo-adaptor/receptor MF** (ubiquitin binding +
LIR/Atg8 binding) over bare `protein binding`, which was uniformly kept non-core
(the receptor hubs carry ~70 IPI `protein binding` entries each). Notable calls:
genuine catalytic RING E3s (SIAH1, RNF41, RNF166, LRSAM1, TRIM5/13/17) kept
catalytic ligase MF as core, whereas the **RING-less** TRIMs were handled
conservatively — `TRIM16` ACCEPTed only the experimentally-supported atypical
B-box autoubiquitination and `MEFV`/pyrin's IBA ubiquitin-ligase MF (no
functional RING) was MARK_AS_OVER_ANNOTATED; `NEW`/proposed terms verified via
QuickGO were added for receptor functions absent from GOA (`GO:0034517`
ribophagy, `GO:0160247` autophagy cargo adaptor activity, `GO:0035973`
aggrephagy, `GO:0010508` positive regulation of autophagy); disputed-direction
electronic NF-κB-regulation terms on `NLRX1` and `AZI2` were flagged
(MARK_AS_OVER_ANNOTATED / non-core) rather than removed; the single REMOVE is an
implausible IEA `mitochondrial intermembrane space` localization on the
cytosolic receptor `NBR1`; and `SIAH1`'s `zinc ion binding` IDA was ACCEPTed but
its citation (PMID:11863358) flagged `WRONG_IDENTIFIER` in `reference_review`.
The mega/pleiotropic hub `HUWE1` and a dedicated mitophagy/CMA effector set
(DNM1L, MFN1, VDAC1, USP30, MARCHF5, MUL1, PARL, PGAM5, etc.) were left for a
future batch. See [batch9_selection_notes.md](PROTEOSTASIS/batch9_selection_notes.md).

## What The PN Resource Actually Contains

The workbook is a row-per-role annotation table, not a gene-centered review file.

- `3123` unique genes
- `4000` annotation rows
- `323` genes with cross-branch annotations
- `318` genes with multiple annotations within one branch
- `2482` genes with a single annotation

The custom hierarchy has:

- `9` Branches
- `33` Classes
- `277` Groups
- `676` Types
- `536` Subtypes

This is their own vocabulary:

- the workbook contains **no GO IDs or explicit GO term mappings**
- the papers explicitly describe the PN hierarchy as a taxonomy that **complements** structured vocabularies such as GO
- the manuscripts say GO, Reactome, KEGG, UniProt, and InterPro were used as **inputs** for building preliminary lists, not as the target representation

### Current Mapping Completion Status

The current curated mapping pass is complete for the `Human Proteostasis Network
Annotation 4.3.11` workbook release dated `2026-04-17`.

Coverage after the completion pass:

| Level | Total source codes | Pending review | Mapped | Context only | No mapping | Deferred | Missing from YAML |
|-------|--------------------|----------------|--------|--------------|------------|----------|-------------------|
| Branch | 9 | 0 | 0 | 1 | 8 | 0 | 0 |
| Class | 42 | 0 | 9 | 16 | 17 | 0 | 0 |
| Group | 297 | 0 | 133 | 31 | 133 | 0 | 0 |
| Type | 800 | 0 | 233 | 26 | 541 | 0 | 0 |
| Subtype | 881 | 0 | 105 | 16 | 760 | 0 | 0 |

Every `2026-04-17` PN source code now has exactly one `subject_curations`
record in a branch mapping YAML. `missing_from_yaml` is now a QA failure state,
not a normal curator bucket, and should remain zero.

The current hierarchy has `2029` total source nodes and `1348` leaf nodes.
The YAML inventory contains:

| Curation status | Records | Meaning |
|-----------------|---------|---------|
| `mapped` | 480 | Reviewed and mapped to a GO term |
| `context_only` | 90 | GO relationship recorded, but unsafe for gene-level propagation |
| `no_mapping` | 1459 | Reviewed and concluded that no GO mapping should be made |

Mapping scopes are:

| Mapping scope | Records | Use |
|---------------|---------|-----|
| `exact` | 3 | Direct semantic match |
| `ok_for_propagation_to_go` | 477 | May produce candidate gene-GO propagations |
| `too_broad_to_propagate` | 90 | Real contextual alignment, but excluded from propagation |

There are no remaining `pending_review`, `deferred`, or `missing_from_yaml`
records in the current mapping set. Most source codes now resolve to
`no_mapping`, which is an intentional curation outcome: the PN node is useful
for proteostasis taxonomy but should not become a GO assertion.

Projection against the human GOA DuckDB at
`~/repos/go-db/db/goa_human.ddb` produced:

| Projection status | Unique gene-GO pairs |
|-------------------|----------------------|
| already in GOA exactly | 1928 |
| entailed by GOA closure | 512 |
| more specific than existing GOA | 305 |
| supported by GOA regulation | 35 |
| new to GOA | 753 |
| no local GOA available | 32 |

Only the `1093` candidate additions (`more_specific_than_existing_goa` +
`supported_by_goa_regulation` + `new_to_goa`) should enter manual AIGR
rereview queues. The `no_local_goa` class is mostly a data-availability state,
not biological evidence; with the DuckDB source it is now a small residual
category.

### Extra-Scrutiny Findings

The mapping audit flags `430/519` GO-bearing curation records as requiring manual
gene-level review before they are used to change a gene review. These are not
necessarily wrong mappings; they are places where propagation can mislead if the
projected GO term is treated as an asserted gene function.

Main flagged patterns:

- `313` mappings have regulatory, recruitment, localization, sensing, or other
  contextual PN source labels.
- `131` mappings use broad or context-losing GO targets such as generic
  translation, protein transport, DNA repair, DNA binding, or stress-response
  terms.
- `262` mappings include domain, family, or subtype metadata in the source label.
- `190` mappings are at branch or class level.
- `89` mappings are explicitly categorized as `too_broad_to_propagate` and are
  excluded from propagation reports.

Representative cases that should stay in the manual review queue:

- `Translation -> GO:0006412 translation`: useful as high-level context but too
  broad for many PN rows; `EDF1` showed that only the RQC term survived manual
  rereview.
- `Mitochondrial proteostasis|Protein transport|Protein import ->
  GO:0017038 protein import`: can be broader than an existing route-specific
  mitochondrial import term, as seen for `TOMM20`.
- `Autophagosome/endosome docking` and related ALP docking labels ->
  `GO:0061909 autophagosome-lysosome fusion`: plausible pathway-stage
  propagation, but `RAB7A` showed that fusion versus post-fusion maturation must
  be checked gene by gene.
- HSPA8-like CMA/aggrephagy boundary cases: PN aggregate-handling context does
  not automatically justify aggrephagy when direct CMA annotations are better
  supported.
- UPS ubiquitin/UBL-binding context buckets: many are useful triage labels, but
  the UPS branch is intentionally inclusive and domain-heavy, so these should
  not be imported into GO without independent evidence.

### Evidence Shape By Branch

The current release is uneven by design.

| Branch set | What is present in the workbook | What it means for reuse |
|------------|----------------------------------|--------------------------|
| ALP | Per-row notes for `1003/1003` rows and references for `1001/1003` rows | Best-supported branch for row-level reuse and audit |
| UPS | Principal domains for `1528/1528` rows and auxiliary domains for `1521/1528` rows | Strong domain/family scaffold, but weaker row-level functional justification in this release |
| Other 7 branches | No row-level notes, no row-level references, no domain columns | Useful as curated membership/context, but not ready to import into GO as-is |

### What Each Level Means

The hierarchy is semantically mixed, which is the main reason it does not map cleanly to GO.

| PN level | What it usually encodes | Relation to GO |
|----------|--------------------------|----------------|
| Branch | Localization or top-level pathway membership | BP/CC hybrid, not a GO class |
| Class | Function in proteostasis, except ALP where it is a stage of autophagy | MF/BP hybrid |
| Group | System, complex, pathway module, or mechanistic bucket | Sometimes GO-like, often not |
| Type | More specific mechanistic role, family, or complex membership | May correspond to MF, BP, CC, or family metadata |
| Subtype | Structural family, domain class, or finer mechanistic subdivision | Often outside GO scope |

Examples by level:

- `Branch`
  - `Cytonuclear proteostasis`
  - `ER proteostasis`
  - `Autophagy-Lysosome Pathway`
  - `Ubiquitin Proteasome System`
- `Class`
  - `Chaperone`
  - `Protein transport`
  - `Autophagophore initiation and elongation`
  - `E3 ubiquitin and UBL ligases`
- `Group`
  - `HSP70 system`
  - `TRAP complex component`
  - `Class 3 PI3K complex 1, direct`
  - `CRL family`
- `Type`
  - `HSP70 nucleotide exchange factor`
  - `J-domain containing HSP70 cochaperone`
  - `Modulator of class 3 PI3K complex 1 activity`
  - `BTB`
- `Subtype`
  - `BAG domain family`
  - `KCTD type`
  - `WD40`
  - many rows have no subtype

Fully expanded examples:

- `BAG1`
  - `Cytonuclear proteostasis -> Chaperone -> HSP70 system -> HSP70 nucleotide exchange factor -> BAG domain family`
- `STAT1`
  - `Autophagy-Lysosome Pathway -> Autophagy gene expression -> Transcriptional repressor`
- `KCTD11`
  - `Ubiquitin Proteasome System -> E3 ubiquitin and UBL ligases -> CRL family -> BTB -> KCTD type`

These are informative for humans, but they are not all GO terms and they are not all the same kind of thing.

## Relationship To GO

### Explicit GO mapping

There is essentially none in the released workbook.

- I searched the workbook for `GO:` and `Gene Ontology` strings and found none.
- The row schema is PN-native: `Branch/Class/Group/Type/Subtype`, plus optional notes, references, and UPS domain fields.
- The papers cite GO as a source database used to build candidate lists, especially for ALP, not as a field embedded back into the final annotation table.

### Implicit GO mapping

There is a lot of **implicit** overlap with GO, but it is inconsistent in kind.

Some PN rows look close to GO:

- `TRAP complex component`
- `Class 3 PI3K complex 1 component`
- `HSP70 nucleotide exchange factor`
- `Ribosome-associated QC`

But many PN labels are not GO-ready assertions:

- family labels like `BAG domain family`
- domain labels like `WD40` or `TPR domain containing`
- branch-local staging labels like `Autophagophore initiation and elongation`
- inclusive UPS buckets like `RING`, `BTB`, `DCAF`, `MEX3`

So the right reading is:

- the PN taxonomy is biologically meaningful
- some rows are close to GO MF/BP/CC concepts
- many rows are module, family, or pathway-context labels rather than GO-annotatable facts

## PN-GO Bridge Contract

The recommended collaboration is not "PN keeps doing PN, GO keeps doing GO, and
we occasionally sync." That is too loose. The better model is a **GO-ready
companion layer** for each PN release.

PN should keep its native Branch/Class/Group/Type/Subtype taxonomy because it
captures proteostasis systems information that GO should not flatten. But each
PN row should also carry a bridge decision saying exactly what GO can do with
that row.

### Row-level bridge fields

Each PN row should be assigned:

- `go_bridge_status`: `direct_go_annotation`, `go_annotation_after_gene_review`,
  `ontology_gap`, `pn_context_only`, `domain_family_only`, or `not_go_relevant`
- `go_term_id`: the candidate GO term, when one exists
- `go_relation`: `exact`, `narrower_than_pn`, `broader_than_pn`,
  `contextual_to_pn`, or `none`
- `evidence_basis`: `row_primary_literature`, `review_article`,
  `domain_architecture`, `orthology`, `database_seed`, or `unknown`
- `directness`: `direct_gene_evidence`, `family_inference`, `module_context`,
  `regulator`, or `hypothesis`
- `gene_exceptions`: genes in the node that must not inherit the candidate GO term
- `ontology_gap`: optional NTR/design triage when the existing GO target is
  insufficient
- `aigr_outcome`: `accepted`, `modified`, `rejected`, `ontology_ticket`,
  `pending_gene_review`, or `not_reviewed`

This turns PN into a GO-compatible curation product without forcing PN to become
a GO annotation table.

### Ontology-gap triage

The `ontology_gap` block lives inside the existing mapping row so it does not
duplicate the mapping schema. The parent row still answers: "what existing GO
term, if any, can represent this PN node today?" The nested block answers:
"does this mismatch justify ontology work?"

The block records `status` values such as `covered_by_existing_go`,
`ntr_candidate`, `ntr_justified`, `needs_design_pattern`, or
`better_as_gocam_or_annotation_extension`; a `gap_type`; candidate parent GO
terms; example genes; anti-scope notes; recommended action; and priority. For
example, the SPNS1/ALR efflux row is marked `ntr_candidate`, not yet
`ntr_justified`, because `GO:0007041 lysosomal transport` is usable today but
loses the autophagic-lysosome-reformation efflux semantics that PN captures.

### Deliverables per PN release

For each PN workbook release, GO/AIGR should produce four artifacts:

1. **GO annotation candidate table**: only rows with `direct_go_annotation` or
   `go_annotation_after_gene_review`.
2. **Exception table**: cases such as `HSPA12A/HSPA12B` under HSP70, `TTC28`
   under HSP90 cochaperone, BAG6 under broad ER protein transport, and
   pseudoenzymes under enzyme-family buckets.
3. **Ontology-gap list**: missing GO concepts exposed by PN, separated from
   ordinary annotation work.
4. **PN feedback table**: workbook corrections, ambiguous placements, weak
   domain-only inclusions, and evidence upgrades needed from PN authors.

The sync point should be release-gated, not informal: PN release -> bridge
classification -> projection/audit -> gene-level review of action rows -> GO
annotations, ontology tickets, and PN feedback.

### Decision policy

| PN row type | GO action |
|-------------|-----------|
| Direct complex/component/enzyme/process role with gene-level evidence | Curate or project to GO, then validate gene-by-gene if propagation is involved |
| Family/domain bucket with known divergent members | Keep PN-native; add gene exceptions before any GO projection |
| Regulatory or pathway-stage placement | Usually GO-review queue, not automatic annotation |
| Proteostasis systems context with no clean GO semantics | Keep as PN context only |
| Real biology lacking a GO term | Open an ontology ticket; do not force into a broad existing GO box |

This is stricter than a periodic mapping sync. It makes every PN row either
actionable for GO, explicitly non-actionable for GO, or queued as an ontology or
evidence problem.

## AIGR Triage Opportunities

The PN resource is useful inside AIGR primarily as a **triage and QA layer**.

### High-value positive controls

These are cases where PN and existing AIGR work largely agree and help validate the framework:

- `CRYAA`, `CRYAB`: PN small-HSP placement agrees with the UPB/holdase interpretation
- `SSR1`, `SSR2`: PN `TRAP complex component` fits existing ER protein-targeting/translocation GO work
- `EDF1`: PN ribosome-associated QC placement is consistent with the current AIGR review
- `KCTD11`: PN CRL/BTB placement matches the current AIGR view of a Cul3 adaptor

### Context-specific but plausible PN rows

These are probably real, but should be treated as non-core or secondary until checked carefully:

- `STAT1`: ALP transcriptional repressor role based on `ULK1` promoter regulation
- `BIRC6`: ALP docking/fusion regulator role on top of its core UPS E2/E3 biology
- `CIAO1`: UPS `DCAF` placement on top of its stronger Fe-S assembly/chaperone identity

### Domain- or family-driven caution cases

These are especially useful for AIGR because the papers themselves signal uncertainty or inclusivity:

- `HSPA12A`, `HSPA12B`: included as HSP70 PN components despite admitted lack of clear proteostasis function
- `AARSD1`: dual placement as `HSP90 cochaperone` and `tRNA synthetase`
- `BAG6`: split across GET-pathway transport and UPS; MS1 explicitly distinguishes it from canonical BAG-domain NEFs
- `TTC28`: PN places it as an HSP70-HSP90 joint cochaperone, but the current AIGR review treats it as a mitotic scaffold
- `MEX3B`: RING-family UPS placement may be real but needs distinction between family membership and core proteostasis role

### Existing-review rereview examples

On the `83`-gene existing-review queue, the useful distinction was not just the
pipeline label but whether the PN-projected term was actually a better GO
assertion than the current AIGR review. In practice,
`more_specific_than_existing_goa` is a projection label, not a guarantee that
the PN term remains the most specific biologically defensible choice after
manual rereview.

- `BCAP31` (`more_specific_than_existing_goa`): accepted `GO:0036503 ERAD pathway`.
  This is a good positive-control case where the PN mapping is exact and the
  biology holds up. The current review already supported direct ERAD
  participation, and the rereview added the pathway term because BCAP31 helps
  handle retrotranslocation of ERAD substrates rather than only acting in a
  looser ER-stress or regulatory context.
- `EDF1` (`new_to_goa`): PN suggested `GO:0002181 cytoplasmic translation`,
  `GO:0006412 translation`, and `GO:0006515 protein quality control for
  misfolded or incompletely synthesized proteins`. Only `GO:0006515` survived
  conservative rereview. The broad translation terms were not added because the
  best-supported biology is collided-ribosome surveillance and
  ribosome-associated quality control rather than generic translation.
- `TOMM20` (`more_specific_than_existing_goa` in the queue): rejected. The PN
  mitochondrial mapping propagates the group-level `Protein import` bucket to
  `GO:0017038 protein import`, but the current AIGR review already uses the
  route-specific mitochondrial import term `GO:0030150 protein import into
  mitochondrial matrix`. At the gene-review level, the PN suggestion was
  broader rather than more specific.
- `HSPA8` (`more_specific_than_existing_goa` in the queue): rejected. The PN
  `GO:0035973 aggrephagy` projection comes from a selective-autophagy-receptor
  path, whereas the current review already captures HSPA8's direct and much
  better supported CMA biology with `GO:0061684 chaperone-mediated autophagy`
  and `GO:0061740 protein targeting to lysosome involved in chaperone-mediated
  autophagy`. HSPA8 clearly participates in proteostasis and aggregate handling,
  but that did not justify promoting it to aggrephagy here.
- `RAB7A` (`more_specific_than_existing_goa` in the queue): rejected on
  conservative rereview. PN projected `GO:0061909 autophagosome-lysosome
  fusion`, but the local evidence base is mixed, and mammalian knockout work
  supports a stronger role in post-fusion autolysosome maturation than in the
  fusion step itself. That was not strong enough to add the more specific term
  to the human review.

## Priority Follow-up Targets

See [priority_genes.tsv](PROTEOSTASIS/priority_genes.tsv).

These rows began as first-pass priorities, but local reviews now exist for all
listed genes. They are not yet represented in `review_batches.tsv` or the
phase-1 dossier set, so the next task is bookkeeping plus bridge-outcome
integration rather than initial fetch/review.

Recommended follow-up jobs:

1. Add these reviewed boundary cases to PN review tracking or create a
   separate `boundary-review` batch so they appear in phase-1-style dossiers.
2. Materialize their mapping outcomes in the bridge layer:
   `HSPA12A/HSPA12B` are HSP70-family exceptions; `AARSD1` and `TTC28` are
   HSP90-cochaperone exceptions; `BAG6` supports specific GET/ERAD/holdase
   terms but not broad ER protein-transport propagation; `BTF3` is a positive
   NAC-component case.
3. Re-run the phase-1 dossier builder after updating the tracking sidecar.

## PN-vs-UPB Comparison

- all `33/33` human UPB genes are present in the PN workbook
- most of those genes are consistent with PN placement at a coarse level
- the best bridge cases are the small HSPs, HSP70/J-domain systems, and the QC boundary genes

The UPB project is the best place to reason about:

- direct unfolded-protein binding
- holdase vs foldase vs co-chaperone distinctions
- GO MF correction and ontology-gap pressure

The PN project is broader:

- define the proteostasis universe
- understand the authors' own annotation model
- identify GO-compatible vs non-GO-compatible PN statements
- use PN to drive AIGR QA and job selection

## Next Steps

- Add the reviewed priority/boundary genes in
  [priority_genes.tsv](PROTEOSTASIS/priority_genes.tsv) to tracking and
  phase-1-style dossier generation.
- Work through the `1093` projected candidate additions, using the unusual
  propagation report as a blocklist for automatic review edits.
- Promote only gene-level decisions that survive evidence review into AIGR
  YAML.
- Convert the mapping layer into the explicit PN-GO bridge contract described
  above, including actionability status, evidence basis, directness, exceptions,
  ontology gaps, and PN feedback.
