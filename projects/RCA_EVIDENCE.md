---
title: "Inferred from Reviewed Computational Analysis (RCA) Evidence Code Review"
maturity: SCOPING
tags: [PIPELINE, EVALUATION]
species: [human, yeast, ECOLI, mouse, ARATH, ACIBA, ACIBZ, AERER, AERME, BACAN, BACFG, BACSP, BACSU, ECOLX, ENTCL, KLEPN, MYCSM, PRORE, PSEAI, SALSP, STAAU, STAHA, STAWA]
genes:
  - ABI3BP
  - ACAN
  - ADIPOQ
  - AGRN
  - ASPN
  - COL4A1
  - COMP
  - DCN
  - DPT
  - FN1
  - HSPG2
  - MGP
  - NID1
  - PRG2
  - PRG3
  - SPARC
  - THBS1
  - THBS2
  - THBS3
  - SLC7A11
  - ATP6V0B
  - Casp3
  - Casp9
  - APC11
  - APJ1
  - ATG7
  - CPS1
  - ESA1
  - GAT2
  - GET3
  - HDA1
  - HRT1
  - HST1
  - HST2
  - HST3
  - LEE1
  - MAL33
  - MDJ1
  - MOH1
  - PNC1
  - RCO1
  - RPD3
  - SAN1
  - SAS2
  - SAS3
  - SDD3
  - SET1
  - SET6
  - SIR2
  - SIZ1
  - SWI1
  - TIM10
  - TIM9
  - UBP11
  - YDJ1
  - ERG19
  - SOD2
  - AT5G02500
  - BCAT3
  - OST1
  - HdeA
  - Skp
  - fruA
  - ftsI
  - ftsW
  - pstA
  - pstC
  - blaOXA-400
  - blaOXA-480
  - blaOXA-418
  - ermA
  - ermJ
  - ermF
  - mcr-3
  - mcr2
  - mcr-4
  - knt
  - aadK
  - ereB
  - hph
  - strB
  - rmtD
  - rmtE
  - rmtF
  - fosA3
  - fosA5
  - arr
  - apmA
  - lnuA
  - cfr
---

# Inferred from Reviewed Computational Analysis (RCA) Evidence Code Review

## Overview

RCA (ECO:0000245, "automatically integrated combinatorial evidence used in manual
assertion") is the GO evidence code for a curator-reviewed conclusion drawn from a
computational analysis. The GO Handbook defines its scope as

> predictions based on computational analyses of large-scale experimental data sets,
> or based on computational analyses that integrate datasets of several types,
> including experimental data (e.g. expression data, protein-protein interaction data,
> genetic interaction data), sequence data (e.g. promoter sequence, sequence-based
> structural predictions), or mathematical models.
> — *The Gene Ontology Handbook*, Chapter 3 (`docs/paper/literature/Gene_Ontology_Handbook_Full.md`)

RCA sits between the experimental codes and the sequence-similarity codes (ISS/ISO/ISM,
IBA). In principle a curator has looked at the result. In practice the
"computational analysis" is often one paper or pipeline that is applied to hundreds of
genes in one batch, and the review step happens once, for the method, not per gene. So
the questions for this project are:

1. **Which analyses produce RCA rows**, and how much of GOA does each one account for?
2. **What kind of claim does each analysis support?** For example, presence in a
   proteome is evidence about location. It is not evidence of a molecular function.
3. **How do RCA rows hold up** when a reviewer looks at each gene individually?
4. **Is this repository using RCA correctly** on the `NEW` annotations its own
   reviewers write?

This is a sibling of the [IEP](IEP.md) and [NOT annotation](NOT_ANNOTATION_USAGE.md)
evidence-code projects, and it uses the same approach: every figure is produced by a
script, and the predicate behind it is stated.

## Methods and reproducibility

| Script | What it does | Output |
|---|---|---|
| [`RCA_EVIDENCE/rca_inventory.py`](RCA_EVIDENCE/rca_inventory.py) | Scans every `genes/*/*/*-goa.tsv` (column 9 == `RCA`) and every `*-ai-review.yaml` (`evidence_type: RCA`). Joins the two, checks that each GOA row is covered by a review, and tabulates actions by cluster, term and reference. | [`data/rca_inventory_report.txt`](RCA_EVIDENCE/data/rca_inventory_report.txt), [`data/rca_reviewed_rows.yaml`](RCA_EVIDENCE/data/rca_reviewed_rows.yaml) |
| [`RCA_EVIDENCE/rca_quickgo_global.py`](RCA_EVIDENCE/rca_quickgo_global.py) | Gets global RCA counts from QuickGO, by group, aspect, reference and ECO code, for the denominator. | [`data/rca_quickgo_global_2026-10-05.txt`](RCA_EVIDENCE/data/rca_quickgo_global_2026-10-05.txt) |

```bash
uv run python projects/RCA_EVIDENCE/rca_inventory.py --yaml projects/RCA_EVIDENCE/data/rca_reviewed_rows.yaml --list
python3 projects/RCA_EVIDENCE/rca_quickgo_global.py
```

Two traps, both handled in the scripts:

- **Do not grep `\tRCA\t`.** Arabidopsis *RCA* (Rubisco activase) is a gene symbol.
  A whole-line match adds about 30 false rows from `genes/ARATH/RCA/RCA-goa.tsv`. The
  inventory matches column 9 only.
- **RCA is more than one ECO code.** BHF-UCL submits RCA as ECO:0007666 ("automatically
  integrated combinatorial computational and experimental evidence used in manual
  assertion"), which is a descendant of ECO:0000245. An exact query for ECO:0000245
  returns **0** BHF-UCL rows. The global script therefore uses
  `evidenceCodeUsage=descendants`.

## Corpus snapshot

### Global denominator (QuickGO, 2026-10-05)

| | Rows |
|---|---:|
| All RCA rows in GOA | **8,610** |
| ECO:0000245 exact / ECO:0007666 exact | 7,922 / 688 |
| CC / MF / BP | 3,943 / 3,119 / 1,548 |
| `NOT\|located_in` | 627 |

| Assigned by | Rows | | Reference (cluster) | Rows |
|---|---:|---|---|---:|
| SGD | 4,713 | | GO_REF:0000123 (YeastPathways to GO-CAM) | **4,133** |
| GeneDB | 1,586 | | PMID:30358795 (yeast zinc proteome) | 580 |
| BHF-UCL | 688 | | PMID:21166475 (Arabidopsis cytosolic proteome) | 436 |
| TAIR | 659 | | PMID:28675934 (one matrisome proteomics paper) | 84 |
| EcoCyc | 448 | | PMID:12819136 (mouse–human apoptosis gene comparison) | 57 |
| AgBase | 204 | | | |
| MGI | 99 | | | |
| FlyBase / ARUK-UCL / WB / AspGD / UniProt | 70 / 15 / 15 / 14 / 3 | | | |
| groups not probed | 96 | | | |

RCA is used at scale by very few groups. **Nearly half of all RCA in GOA (4,133 rows,
48%) comes from one pipeline**: SGD's conversion of YeastPathways into pathway GO-CAMs
(GO_REF:0000123, `WITH/FROM` = `SGD_PWY:*`). Two proteome-scale papers add another
1,016 rows between them. GeneDB, the second-largest submitter, has no genes in this
corpus.

### This repository (`rca_inventory.py`)

- **130 GOA RCA rows in 66 gene folders.** Every one is covered by a reviewed row in the
  gene's review, so 0 GOA rows are unreviewed.
- **156 reviewed RCA rows in 90 gene folders.** 118 of them audit GOA rows. The
  difference from 130 is GOA duplicates, such as the same term and reference with
  different `WITH/FROM` pathway ids, which the reviews collapse into one row. The
  other **38 are `NEW` rows that our reviewers wrote and coded as RCA** (see Pattern 6).
- The corpus covers about 1.5% of global RCA, and it is heavily skewed. It contains 62
  rows from BHF-UCL's matrisome papers but only 8 rows from the GO_REF:0000123 pipeline,
  which is about half of all RCA.

## Dispositions by cluster

Each row is assigned to a cluster by its reference, because review rows have no
`assigned_by` field.

| Cluster | Reviewed | ACCEPT | KEEP_AS_NON_CORE | OVER_ANNOT. | MODIFY | REMOVE | UNDECIDED | Not accepted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BHF-UCL matrisome proteomics (7 PMIDs) | 62 | 35 | 0 | 13 | 10 | 4 | 0 | **44%** |
| SGD zinc proteome (PMID:30358795) | 32 | 19 | 10 | 2 | 0 | 0 | 1 | 41%¹ |
| SGD YeastPathways import (GO_REF:0000123) | 8 | 6 | 0 | 0 | 0 | 2 | 0 | 25% |
| Single-paper RCA (EcoCyc, UniProt) | 9 | 7 | 2 | 0 | 0 | 0 | 0 | 22%¹ |
| MGI comparative genomics (PMID:12819136) | 4 | 1 | 2 | 0 | 1 | 0 | 0 | 75%¹ |
| TAIR proteome absence (NOT cytosol) | 3 | 1 | 0 | 0 | 0 | 2 | 0 | 67% |
| *Reviewer-authored NEW* | 38 | — | — | — | — | — | — | — |

¹ Most of these are KEEP_AS_NON_CORE. The term is true but peripheral, not wrong.

Across the 118 audited GOA rows, **68 were accepted (58%)**. The low acceptance does not
mean RCA is unreliable in general. It is driven by **two clusters with a specific,
nameable inference error**, described below as Patterns 1 and 4. The zinc, pathway and
EcoCyc clusters are mostly correct. When reviewers do not accept those rows, it is
usually because the term is not core rather than wrong.

## Failure patterns

### 1. Location read as function: matrisome proteomics → "ECM structural constituent"

BHF-UCL annotated matrisome proteins from seven ECM-enrichment proteomics papers
(PMID:20551380, 23979707, 25037231, 27068509, 27559042, 28327460, 28675934) to
`GO:0005201 extracellular matrix structural constituent` and its children
`GO:0030021 …conferring compression resistance` and `GO:0030020 …conferring tensile
strength`. Detecting a protein in a decellularised matrix fraction is **cellular
component** evidence. A structural-constituent molecular function is a different
claim, that the protein contributes to the integrity of the matrix, and the proteomics
data cannot show it. The ABI3BP review states this directly:

> Detection in an ECM-enriched proteome supports the co-annotated cellular-component
> terms, not a molecular function asserting a contribution to structural integrity.

The outcome splits cleanly along known protein biology:

| Accepted (35 rows) | Not accepted (27 rows) |
|---|---|
| COL4A1 (tensile), HSPG2, ACAN (compression), FN1, AGRN, NID1, DPT, COMP | **Matricellular:** THBS1, THBS2, THBS3, SPARC, ABI3BP · **regulatory:** MGP · **SLRPs given "compression resistance":** DCN, ASPN · **not ECM proteins:** PRG2, PRG3 (eosinophil granule), ADIPOQ (secreted hormone) |

Two subtypes are worth separating:

- **Wrong class of protein.** Matricellular proteins and calcification inhibitors sit in
  the matrix but do not hold it together. Proteomics cannot tell them apart from
  collagens.
- **Wrong child term.** DCN and ASPN are single-GAG small leucine-rich proteoglycans
  (SLRPs) that bind collagen and regulate fibril assembly. They were given the
  *compression resistance* child term, which suits large aggrecan-type proteoglycans
  and probably reflects the "proteoglycan" label. The DCN review proposes
  `GO:0005518 collagen binding`.

**Consistency problem in our own reviews.** The matricellular proteins reached four
different actions for the same reason: THBS1 MODIFY→`GO:0031012` (a CC term), THBS2
MODIFY→`GO:0030198` (a BP term), THBS3 MARK_AS_OVER_ANNOTATED, and SPARC REMOVE. GO has
no molecular-function term for the matricellular class (the ABI3BP review raises this
as a `proposed_new_terms` entry). That gap is why reviewers keep using different
substitutes. The project should pick one disposition for this pattern (see
Recommendations).

### 2. Proteome-scale cofactor prediction: generic but mostly true

PMID:30358795, the *S. cerevisiae* zinc proteome (580 rows globally), assigns
`GO:0008270 zinc ion binding`. Of the 32 reviewed rows, 19 were accepted and 10 kept as
non-core. Where it fails, the failure is subtle:

- **The zinc site is not in the mature functional form.** In TIM9, the CX3C motifs are
  disulfide-bonded in the intermembrane space, so zinc binding happens only before
  import, if it happens at all (MARK_AS_OVER_ANNOTATED).
- **No residue-level support.** UBP11 has no zinc site in UniProt, so the only support
  is the proteome-wide prediction (MARK_AS_OVER_ANNOTATED).
- **The zinc is structural.** In ESA1 (MYST zinc finger), HDA1 and SET1, zinc binding is
  real but structural or catalytic-support, which is why these are KEEP_AS_NON_CORE
  rather than ACCEPT.

The cluster is mostly right but low in information. `zinc ion binding` is the kind of
term reviewers routinely move to non-core whatever its evidence code.

### 3. Pathway import: the model's location and pathway boundaries pass to every enzyme

GO_REF:0000123 rows are generated from SGD YeastPathways GO-CAMs. Every enzyme in a
pathway model gets the model's molecular function, its biological process and an
`is_active_in` location. We have reviewed only 8 of 4,133 rows, and 2 were removed:

- **Default location.** SOD2 (mitochondrial MnSOD) received `is_active_in cytosol` from
  DETOX1-PWY. The activity and process rows are correct. Only the location is wrong.
- **Pathway-level process given to an upstream enzyme.** ERG19 (diphosphomevalonate
  decarboxylase) received `farnesyl diphosphate biosynthetic process, mevalonate
  pathway`. ERG19 makes IPP. FPP is made downstream by IDI1 and ERG20. (The term is now
  obsolete as well.) This is the same "who performs the step" question as the
  substrate rule in `CLAUDE.md`, applied to an enzyme upstream of the step rather than
  to a substrate.

Both errors come from the pipeline, not from the individual genes. With 4,133 rows,
even a few-percent rate of default-cytosol or pathway-boundary errors would be one of
the largest correctable error sources in yeast GO. **This is the highest-priority
sampling target** (Action Items).

### 4. NOT from absence in a proteome

TAIR's PMID:21166475, a cytosolic proteome of Arabidopsis cell cultures, supports 436
`NOT|located_in cytosol` rows globally. Not being detected in one fractionation dataset
is weak negative evidence. It also depends on the tissue and growth condition, which
the GAF row does not record. Of the three reviewed rows:

- **OST1/SRK2E and AT5G02500 (HSP70-1) were REMOVED.** Experimental evidence of
  cytosolic localization exists (for OST1, IDA cytosol and cytoplasm, PMID:41417897 and
  PMID:19880399), so the NOT row contradicts direct observation.
- **BCAT3 was ACCEPTED.** It has a plastid transit peptide and experimentally
  determined chloroplast localization, so "not in cytosol" is correct.

This is the only cluster where a reviewed RCA row was removed for contradicting direct
experimental evidence. It belongs with the [NOT annotation](NOT_ANNOTATION_USAGE.md)
project. At 436 rows, an automated check is worth building: flag any NOT|cytosol RCA
row for a gene that also has a positive IDA/HDA cytosol or cytoplasm annotation.

### 5. Comparative genomics coded as RCA

MGI's Casp3 and Casp9 rows (PMID:12819136, a mouse–human comparison of apoptosis genes,
57 rows globally) assign `peptidase activity` and `proteolysis`. The underlying
inference is orthology, which ISO is meant to capture, and the terms are generic
parents of `cysteine-type endopeptidase activity`. The rows are not wrong. Reviewers
kept 2 as non-core, modified 1 to the specific term and accepted 1. The issue is
evidence-code choice and term granularity, not truth.

### 6. Our own NEW rows: RCA used as a catch-all

38 reviewed RCA rows are not from GOA. Our reviewers wrote them as `NEW`:

| Source cited | Rows | What the inference actually is |
|---|---:|---|
| `file:projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml` | 31 | A curated ARO→GO **mapping** applied through the CARD cross-reference: a family-membership transfer |
| `file:genes/<ORG>/<gene>/<gene>-uniprot.txt` | 3 | A GO cross-reference copied from the UniProt record |
| PMID (arr, cfr, lnuA) | 3 | Two of these cite gene-disruption or biochemical papers |
| `file:projects/PROTEOSTASIS/…/pn_projected_annotations.tsv` | 1 | A projection from proteostasis-network placement to a GO term (ATP6V0B) |

None of these is an "integrated analysis of large-scale data sets". The ARO→GO rows
are a mapping-based family transfer, nearer to ISM or IEA-style mapping evidence. The
UniProt cross-reference rows repeat someone else's assertion. Where a paper reports a
knockout or an enzyme assay (Arr disruption increases rifampin susceptibility), IMP or
IDA describes the evidence and RCA hides it. RCA is being used to mean "a computational
step that a curator looked at". That describes almost every row in this repository, so
it carries no information.

This is a convention gap in this repository, not an error in GOA. It should be settled
before more batch projects (AMR, PN projection) add RCA-coded NEW rows.

## Where RCA is legitimate

- **Validated integrative analyses** that combine several data types, as the Handbook
  intends. The YeastPathways import qualifies as a method: its MF and BP rows are
  usually correct (6/8 accepted). Its problems come from pathway granularity, not from
  the evidence code.
- **Proteome-scale cofactor surveys with residue-level support.** The zinc proteome is
  accepted wherever UniProt or structure confirms a site.
- **Matrisome proteomics for CC terms.** The same papers would support
  `located_in extracellular matrix` with no objection. The error is the aspect, not the
  data.

## Reviewer checklist

1. **Identify the analysis.** Look at the reference and `WITH/FROM`. GO_REF:0000123 +
   `SGD_PWY:*`, a matrisome PMID, the zinc proteome and PMID:21166475 each fail in their
   own way (Patterns 1–4).
2. **Ask which aspect the data can support.** Proteomics → location. Pathway membership
   → process, but only for the step the enzyme performs. Cofactor prediction → binding,
   and usually not core.
3. **For pathway imports, check location and step separately.** Reject the
   `is_active_in` row on its own if the enzyme is in another compartment. Reject a
   process row that names a product the enzyme does not make.
4. **For NOT rows from proteome absence**, look for any positive IDA/HDA localization.
   A direct observation outranks a non-detection.
5. **Do not treat RCA as stronger than the analysis behind it.** "Reviewed" means the
   method was reviewed, usually once and for a whole batch.
6. **When you write a NEW row, choose the code for the actual inference** (see
   Recommendations). Do not default to RCA.

## Recommendations

1. **Repository convention for NEW-row evidence codes.** Add guidance to `CLAUDE.md`
   (or `docs/`). Mapping or family transfers (ARO→GO, PN projection) should use the
   code for the inference (ISM/ISS, or IEA for a pure mapping). Rows backed by a
   knockout or assay paper should use IMP/IDA. RCA should be kept for a genuinely
   integrative analysis. Then re-code the 38 existing rows in one pass, after
   agreement with the AMR and PROTEOSTASIS project owners.
2. **One disposition for "matricellular protein → ECM structural constituent".** The
   proposal is MARK_AS_OVER_ANNOTATED, together with a `located_in extracellular matrix`
   NEW row where one is missing and a reference to the matricellular-MF
   `proposed_new_terms` entry. Then reconcile THBS1, THBS2 and SPARC.
3. **Report Pattern 1 upstream.** Send BHF-UCL a short list: SLRPs given compression
   resistance (DCN, ASPN) and non-ECM proteins (PRG2, PRG3, ADIPOQ). The review rationales
   are already written.
4. **Report the two YeastPathways errors to SGD** (SOD2 cytosol, ERG19 FPP-process) as
   examples of a pipeline-level failure, after the sampling below shows how often it
   occurs.

## Action items

- [ ] **Sample GO_REF:0000123.** Pick about 30 yeast genes with GO_REF:0000123 rows,
      stratified over organellar enzymes (mitochondrial, peroxisomal, vacuolar) and
      multi-step pathways. Estimate the default-cytosol and pathway-boundary error
      rates. This cluster is 48% of all RCA, and we have reviewed 8 rows.
- [ ] **Automated NOT|cytosol contradiction check** across the 436 PMID:21166475 rows,
      against positive IDA/HDA cytosol or cytoplasm annotations for the same gene in
      QuickGO.
- [ ] **Sample GeneDB RCA** (1,586 rows, none in the corpus) to see which analyses GeneDB
      codes as RCA.
- [ ] Write the NEW-row evidence-code convention (Recommendation 1) and re-code the 38
      rows.
- [ ] Reconcile the matricellular dispositions (Recommendation 2).
- [ ] Add a regression test so that `rca_inventory.py` keeps reporting 0 uncovered GOA
      RCA rows as genes are added.

## Session notes

### 2026-10-05 (first pass: inventory and scoping)

Created the project. Inventoried all GOA and reviewed RCA rows with
`rca_inventory.py` and fetched global QuickGO denominators with
`rca_quickgo_global.py`. Found that BHF-UCL's RCA uses ECO:0007666 (invisible to an
exact ECO:0000245 query), that GO_REF:0000123 is 48% of all RCA, and that 38 of our
reviewed RCA rows are reviewer-authored NEW rows from mappings and projections. The
pattern write-ups are based on reading the review rationales for each cluster. No gene
reviews were edited in this pass.
