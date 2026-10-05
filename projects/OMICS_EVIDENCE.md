---
title: "Omics and High-Throughput Evidence in GO Annotation"
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
autolink_exclude: [RCA]
species: [human, yeast, SCHPO, ARATH]
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
  - GLOD4
  - HSPA8
  - TXN
  - HSPA9
  - ALPL
  - TTK
  - ACOX3
  - ADIRF
  - AT5G02500
  - BCAT3
  - OST1
---

# Omics and High-Throughput Evidence in GO Annotation

**Bottom line:** GO annotations derived from omics data are filed under two
evidence-code families. The high-throughput (HTP) codes HDA/HTP/HMP/HGI cover 65,876
rows. RCA, the reviewed-computational-analysis code, covers another 1,557 omics rows.
The same dataset can appear under both codes, and the code says little about what the
annotation claims. What predicts whether an annotation holds up is **how the data were
used**:

- **A location read from a fraction is usually sound.** 57% of reviewed rows are
  accepted, rising to 63–89% for systematic localization screens and organelle
  proteomes. The exceptions are vesicle and body-fluid proteomes (6% accepted) and the
  generic term `membrane` (23%).
- **A function read from location or co-purification is unreliable under either code.**
  Examples are "cadherin binding" from an E-cadherin proximity screen (2 of 50 accepted)
  and the RCA matrisome "ECM structural constituent" rows (56%).
- **A process read from differential expression has been coded HDA.** These are 0 of 9
  accepted.
- **NOT annotations from exclusion exist only under RCA.** There are 627 such rows and
  just 4 HTP-family NOTs, and 43% of the RCA cytosol NOTs are contradicted elsewhere in
  GOA.

The same papers make the point directly. For the twelve papers cited under both codes,
our reviews accepted 74% of the HDA location rows and 56% of the RCA function rows.

This project replaces the earlier `RCA_EVIDENCE` project. Its RCA analysis is now the
sub-page [RCA: omics-derived annotations](OMICS_EVIDENCE/rca.md).

## Scope

| Evidence code | ECO | GOA rows | Distinct gene × term | Reviewed here | Covered |
|---|---|---:|---:|---:|---|
| HDA high-throughput direct assay | ECO:0007005 | 54,282 | 40,864 | 2,381 | here |
| HTP high-throughput experiment | ECO:0006056 | 9,088 | 9,088 | 371 | here |
| HMP high-throughput mutant phenotype | ECO:0007001 | 2,419 | 880 | 41 | here |
| HGI high-throughput genetic interaction | ECO:0007003 | 87 | 52 | 6 | here |
| RCA, omics-derived | ECO:0000245 + descendants | 1,557 | — | ~65 | [sub-page](OMICS_EVIDENCE/rca.md) |
| HEP high-throughput expression pattern | ECO:0007007 | 1,154 | — | 41 | [IEP project](IEP.md) |

The framework is the GO consortium's guidance for annotating from high-throughput studies
(PMID:30715275), which introduced the HTP codes so that users could separate
screen-derived annotations from hypothesis-driven ones.

## Methods and reproducibility

| Script | Question | Output |
|---|---|---|
| [`htp/htp_inventory.py`](OMICS_EVIDENCE/htp/htp_inventory.py) | All HTP-family rows in GOA (by code, aspect, group, reference, term); every reviewed HTP-family row and its action; papers cited under both HTP and RCA codes | [report](OMICS_EVIDENCE/htp/data/htp_inventory_report.txt), [`htp_reviewed_rows.yaml`](OMICS_EVIDENCE/htp/data/htp_reviewed_rows.yaml) |
| [`rca/`](OMICS_EVIDENCE/rca/) scripts | RCA source catalogue, matrisome crosswalk, NOT-contradiction check | see the [RCA sub-page](OMICS_EVIDENCE/rca.md) |

```bash
python3 projects/OMICS_EVIDENCE/rca/rca_source_catalog.py     # RCA download (also used for cross-code joins)
uv run python projects/OMICS_EVIDENCE/htp/htp_inventory.py    # HTP download + reviewed corpus
```

**Count claims as distinct gene × term pairs, not rows.** A GAF row is repeated once per
annotation extension, so row counts can mislead badly. The 1,535 HMP rows for
`metal-dependent deubiquitinase activity` (PMID:26412298) are **5** *S. pombe* DUBs,
each listed once per substrate. The 4,090 HDA rows for `RNA polymerase II
cis-regulatory region sequence-specific DNA binding` (PMID:40015273) are **67**
transcription factors, each listed once per target. In GOA, 65,876 HTP-family rows
reduce to 50,795 distinct gene × term pairs.

## How omics data become GO annotations

The classification below applies across evidence codes. Each row is a way of turning a
dataset into a GO claim. Reviewed-row figures are from this repository's gene reviews.
"Rejected" means MARK_AS_OVER_ANNOTATED, REMOVE or MODIFY.

| Use | Typical data | Codes seen | GOA scale | Reviewed: accepted / non-core / rejected | Verdict |
|---|---|---|---|---|---|
| **1. Location → location** | Organelle or fraction proteome, GFP/YFP localization screen, complex map | HDA, HTP, RCA | ~47,000 pairs | other locations: 57% / 27% / 13% | Sound; the data match the aspect |
| ↳ vesicle / body-fluid cargo | Exosome, microvesicle, tear, urine, CSF proteomes | HDA | thousands (one paper alone: 1,046 genes) | **6%** / 59% / 26% | Real, but almost never informative |
| ↳ generic `membrane` | Membrane-fraction proteome | HDA | 1,142 genes from one NK-cell paper | 23% / 25% / **48%** | Soluble contaminants plus an uninformative term |
| **2. Assay → function** | RNA interactome capture, TF–DNA atlas, activity-based probes, kinase autophosphorylation | HDA | ~2,500 pairs | RNA binding: 40% accepted; abundant-protein carry-over is the main error | Usually sound when the assay measures the activity itself |
| **3. Location or co-purification → function** | ECM proteome → *structural constituent*; proximity/IP proteome → *X binding* | RCA (ECM), HDA (cadherin binding) | 731 RCA rows; 255 HDA pairs | ECM: 56% accepted ([RCA sub-page](OMICS_EVIDENCE/rca.md)); cadherin binding: **2/50** | Unreliable; the aspect does not match the data |
| **4. Expression change → process** | Differential proteome during differentiation | HDA (should be HEP at most) | 42 pairs for osteoblast differentiation from one paper | **0/9** accepted | Wrong code and wrong inference ([IEP](IEP.md) territory) |
| **5. Mutant / RNAi screen → process** | Genome-wide RNAi and mutant screens | HMP, HGI | 875 + 52 pairs | HMP 12% accepted, mostly non-core | Pleiotropy; usually non-core rather than wrong |
| **6. Exclusion → NOT location** | Proteins left out of a fraction's reported set | RCA only (TAIR) | 627 rows; HTP-family NOTs: **4** | 43% of cytosol NOTs contradicted in GOA | Unsupported as a negative claim ([RCA sub-page](OMICS_EVIDENCE/rca.md)) |

### 1. Location → location: sound, unless the compartment is a vesicle or "membrane"

Nearly three-quarters of HTP-family pairs are HDA locations, and they are the use the
codes were designed for. Accepted rates are high when the experiment localizes proteins
one by one or purifies a defined organelle:

| Reference | Reviewed rows | ACCEPT | Kind of experiment |
|---|---:|---:|---|
| PMID:11914276 yeast proteome localization | 18 | 89% | tagged-protein screen |
| PMID:14562095 budding-yeast GFP localization | 44 | 82% | tagged-protein screen |
| PMID:26928762 yeast SWAp-Tag library | 29 | 72% | tagged-protein screen |
| PMID:34800366 human high-confidence mitochondrial proteome (HTP) | 371 | 63% | organelle proteome with confidence scoring |
| PMID:16823372 *S. pombe* ORFeome localization | 164 | 63% | tagged-protein screen |
| PMID:19946888 NK-cell membrane proteome | 273 | 22% | membrane fraction → `membrane` |
| PMID:23533145 urinary/prostatic exosomes | 202 | 5% | vesicle cargo → `extracellular exosome` |
| PMID:19056867 urinary exosomes | 233 | 4% | vesicle cargo |
| PMID:20458337 B-cell exosomes | 116 | 3% | vesicle cargo |

Vesicle-type terms (`extracellular exosome`, `extracellular vesicle`, `blood
microparticle`, `vesicle`) account for **712 reviewed rows, more than any other HTP
cluster**. Reviewers rarely say they are false. 59% are kept as non-core and only 11
are removed. They do say the location carries no information about function. In the ADIRF
review's words, one such paper "annotates 1046 distinct gene products with GO:0070062
and nothing else … a bulk import, not 1046 independent findings". The generic
`membrane` term from membrane fractions fails differently. The fraction includes soluble
and peripheral proteins (ACOX3 "has no transmembrane domain and is a matrix-soluble
enzyme"), so half of those rows are rejected.

### 2–3. Function from omics: the assay must measure the function

When the assay measures the activity itself, as with RNA crosslinking in interactome
capture, DNA binding in a TF atlas, or activity-based probes for serine hydrolases, the
molecular-function claim is direct. Errors there come from **carry-over of abundant
proteins**. TXN and HSPA9 appear as "RNA binders", and 40% of reviewed
interactome-capture RNA-binding rows were accepted.

When the function is **inferred from where the protein was found**, the claim goes beyond
the data, whatever the evidence code:

- **ECM proteomics → "ECM structural constituent" (RCA).** The term follows the protein's
  matrisome category, not its biology. See the [RCA sub-page](OMICS_EVIDENCE/rca.md).
- **E-cadherin proximity proteomics → "cadherin binding" (HDA, PMID:25468996, 255
  genes).** 48 of 50 reviewed rows were not accepted. The GLOD4 review describes the
  artefact: "abundant soluble cytosolic proteins are labelled by a membrane-tethered
  biotin ligase and enter GOA as cadherin binders."

Both are the same inference ("found with X, therefore binds or builds X") filed under
different codes. A direct assay code makes the error harder to spot.

### 4. Expression change coded as a direct assay

PMID:16210410 (a differential membrane proteome during osteoblast differentiation)
supports 42 HDA `osteoblast differentiation` pairs. None of the 9 reviewed rows was
accepted: "differential expression during osteoblast differentiation does not imply a
functional role in the differentiation process" (CLTC review). This is an expression
pattern used as evidence of process involvement, the problem analysed in the
[IEP](IEP.md) project. It also uses the wrong code: HEP is the high-throughput
expression code, and HDA asserts a direct assay of the process.

### 5. Screens → process (HMP/HGI)

Genome-wide RNAi and mutant screens supply 875 HMP and 52 HGI process pairs. The
reviewed sample is small (47 rows). HGI rows are mostly accepted (5/6), while HMP rows
are mostly kept as non-core (22/41): a screen hit in "defense response to Gram-negative
bacterium" or "wound healing" is usually a pleiotropic phenotype rather than the gene's
role.

### 6. NOT annotations: an RCA-only practice

The HTP-family codes carry **4** NOT rows in all of GOA: three *S. pombe* DUBs `NOT
is_active_in nucleolus` and one miRNA. RCA carries **627**, all from two Arabidopsis
fraction proteomes. The Golgi paper PMID:22430844 shows the split cleanly. It supports
415 positive HDA `Golgi apparatus` rows and 191 RCA `NOT Golgi apparatus` rows: the same
experiment, recorded with one code for each polarity. Analysis of the cytosol NOTs
(43% contradicted, including 37 cytosolic ribosomal proteins) is on the
[RCA sub-page](OMICS_EVIDENCE/rca.md).

## Same papers, two codes

`htp_inventory.py` finds 12 papers cited by both HTP-family and RCA rows. Ten are
BHF-UCL's ECM proteomics papers, which yield HDA locations (`extracellular matrix`,
`extracellular region`) **and** RCA molecular functions. The other two are the Golgi
paper and a *T. brucei* mitochondrial-membrane proteome. Reviewed outcomes on those 12
papers:

| Rows | Reviewed | ACCEPT | Rejected |
|---|---:|---:|---:|
| HTP-family (locations) | 148 | **73.6%** | 8% |
| RCA (functions) | 62 | **56.5%** | 44% |

The data and the curators are the same. The difference is the inference step.

## Reviewer checklist

1. **Classify the use** (table above) before judging the code. The evidence code tells
   you the provenance, and the use tells you how much the data support.
2. **Location rows:** accept localization screens and confidence-scored organelle
   proteomes. Keep vesicle and body-fluid rows as non-core unless the protein is a known
   vesicle component. Prefer a specific membrane over `membrane`, and reject the
   generic term for proteins with no membrane anchor.
3. **Function rows:** ask whether the assay measured the activity. If it did not, and the
   function is inferred from co-location or co-purification, treat the row as
   over-annotated unless independent evidence exists. If it did (crosslinking, binding
   assay, activity probe), check for abundant-protein carry-over.
4. **Process rows from HDA:** check whether the data are really differential expression.
   If they are, the row is an IEP-type inference with the wrong code.
5. **NOT rows from omics:** look for positive annotations to the same compartment. A
   positive observation outranks an exclusion.
6. **Judge by distinct gene × term pairs.** A gene can carry hundreds of rows for one
   claim through annotation extensions.

## Recommendations

1. **Decide project-wide dispositions** for the two largest low-information clusters.
   Proposals: vesicle-type locations from bulk proteomes are KEEP_AS_NON_CORE by default,
   and `membrane` from a membrane-fraction proteome is MARK_AS_OVER_ANNOTATED for proteins
   without a membrane anchor. This would make the 1,000 or so existing rows consistent
   and speed up future reviews.
2. **Report the mis-coded clusters to their groups:**
   - HDA→HEP for expression-derived process rows (PMID:16210410).
   - HDA for RCA Use C rows that are really direct localizations (see the RCA sub-page).
3. **Report the location-to-function inferences:** BHF-UCL for the matrisome mapping
   (RCA sub-page), and the E-cadherin proximity screen (PMID:25468996, 255 genes,
   cadherin binding).

## Action items

- [ ] Decide and document the vesicle-type and generic-`membrane` dispositions
      (Recommendation 1), then apply them as a batch to existing reviews.
- [ ] Review a sample of the **unreviewed MF clusters** with the use-2/use-3 test: serine
      hydrolase activity-based probes (PMID:33827210), copper/cobalt/zinc ion binding from
      plant mitochondrial metal-affinity proteomics (PMID:20018591), kinase
      autophosphorylation (PMID:21477822).
- [ ] Review the 33 unreviewed `osteoblast differentiation` pairs from PMID:16210410, and
      look for other differential-expression papers coded HDA for process terms.
- [ ] Sample the largest HTP-family location sources that have no reviews yet: the
      *T. brucei* protein map (PMID:36804636, 5,439 genes) and the Arabidopsis
      membrane-oligomerization profiling (PMID:28887381, 3,263 rows), which also
      supplies most of the HDA rows that contradict the RCA cytosol NOTs.
- [ ] Extend the HTP-family inventory with a per-paper confidence signal (screen vs
      fraction vs vesicle) so that reviewers can triage rows automatically.

## Sub-pages

- [RCA: omics-derived annotations](OMICS_EVIDENCE/rca.md): source catalogue of all RCA,
  the matrisome category mapping, NOT contradictions, and out-of-scope RCA notes
  (YeastPathways, proteome-scale predictions, NEW rows).

## Session notes

### 2026-10-05: created from RCA_EVIDENCE; HTP-family inventory

Renamed and broadened `RCA_EVIDENCE` into this project at the user's request, because
the omics analyses for RCA and HDA overlap. The RCA page and its scripts moved to
`OMICS_EVIDENCE/rca.md` and `OMICS_EVIDENCE/rca/`. Added `htp/htp_inventory.py`, which
covers 65,876 HTP-family GOA rows (50,795 distinct pairs) and 2,799 reviewed rows in
1,435 gene folders, and found the six uses above. HEP is left to the IEP project. No
gene reviews were edited.
