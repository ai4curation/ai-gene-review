---
title: "RCA: Omics-Derived Annotations"
autolink_exclude: [RCA, UPF1]
species: [human, ARATH, yeast]
---

# RCA: Omics-Derived Annotations

Part of [Omics and High-Throughput Evidence](../OMICS_EVIDENCE.md). This page covers the
RCA evidence code. The parent page covers the high-throughput codes (HDA/HTP/HMP/HGI)
and compares the two.

## Overview

RCA (*Inferred from Reviewed Computational Analysis*, ECO:0000245) is the GO evidence
code for a curator-reviewed conclusion drawn from a computational analysis of
large-scale data. The GO Handbook defines it as follows:

> predictions based on computational analyses of large-scale experimental data sets,
> or based on computational analyses that integrate datasets of several types,
> including experimental data (e.g. expression data, protein-protein interaction data,
> genetic interaction data), sequence data (e.g. promoter sequence, sequence-based
> structural predictions), or mathematical models.
> — *The Gene Ontology Handbook*, Chapter 3 (`docs/paper/literature/Gene_Ontology_Handbook_Full.md`)

**This project focuses on RCA annotations derived from omics data**: proteomics,
interactomics and other high-throughput experimental datasets. These are the
annotations where the "computational analysis" in RCA is a step that turns an omics
measurement into a GO claim. The questions are:

1. How much RCA is omics-derived, and from which groups and papers?
2. **What does each use assert, and does that match what the data can show?** An
   enrichment proteome shows where a protein was found. It does not show what the
   protein does there, and leaving a protein out of one fraction's protein list does
   not show that it is absent from that compartment.
3. How well do these annotations hold up, either when reviewed gene by gene or when
   checked against the rest of GOA?

Two other large uses of RCA are outside this scope and are covered briefly under
[Out of scope](#out-of-scope-quirks-noted-not-studied): the YeastPathways import, which
is half of all RCA and probably carries the wrong code, and RCA on this repository's
own `NEW` rows.

Related projects: [IEP](../IEP.md) (another evidence-code audit) and
[NOT annotation usage](../NOT_ANNOTATION_USAGE.md).

## Methods and reproducibility

Every figure on this page comes from a script in [`rca/`](rca/), and
each script's docstring states the predicates it uses. Downloads are cached under
`rca/data/`, so reruns work offline. `--refresh` re-fetches the data.

| Script | Question | Output |
|---|---|---|
| [`rca_source_catalog.py`](rca/rca_source_catalog.py) | Which references lie behind all RCA in GOA, and what kind of analysis is each? | [`rca_reference_catalog.yaml`](rca/data/rca_reference_catalog.yaml), [report](rca/data/rca_source_catalog_report.txt) |
| [`rca_reference_classes.yaml`](rca/rca_reference_classes.yaml) | Curated analysis-type call for every reference with ≥5 rows, judged from its abstract | (input to the catalog) |
| [`rca_matrisome_crosswalk.py`](rca/rca_matrisome_crosswalk.py) | Do BHF-UCL's ECM terms follow the Naba matrisome categories? | [report](rca/data/rca_matrisome_crosswalk_report.txt) |
| [`rca_not_contradictions.py`](rca/rca_not_contradictions.py) | Are proteomics-derived NOT rows contradicted by positive annotations? | [`rca_not_contradictions.tsv`](rca/data/rca_not_contradictions.tsv), [report](rca/data/rca_not_contradictions_report.txt) |
| [`rca_inventory.py`](rca/rca_inventory.py) | Which RCA rows have been reviewed in this repository, and with what action? | [`rca_reviewed_rows.yaml`](rca/data/rca_reviewed_rows.yaml), [report](rca/data/rca_inventory_report.txt) |
| [`rca_quickgo_global.py`](rca/rca_quickgo_global.py) | Global counts by group, aspect and reference | [report](rca/data/rca_quickgo_global_2026-10-05.txt) |

```bash
python3 projects/OMICS_EVIDENCE/rca/rca_source_catalog.py          # first: downloads all RCA rows
python3 projects/OMICS_EVIDENCE/rca/rca_matrisome_crosswalk.py
python3 projects/OMICS_EVIDENCE/rca/rca_not_contradictions.py
uv run python projects/OMICS_EVIDENCE/rca/rca_inventory.py --yaml projects/OMICS_EVIDENCE/rca/data/rca_reviewed_rows.yaml --list
```

Pitfalls the scripts handle:

- **RCA spans more than one ECO code.** BHF-UCL submits RCA as ECO:0007666 ("automatically
  integrated combinatorial *computational and experimental* evidence used in manual
  assertion"), which is a child of ECO:0000245. A query for exactly ECO:0000245 returns
  0 BHF-UCL rows, so all queries include descendant codes.
- **Arabidopsis *RCA* is a gene symbol** (Rubisco activase). A line-wise grep for `RCA`
  picks up about 30 false rows, so the scripts match the evidence-code column only.
- **Title keywords misclassify papers.** "Membranome" is a computational database, not
  proteomics. The zinc-proteome paper's GO terms come from a bioinformatic scan, not from
  its mass spectrometry. All 57 references with ≥5 rows (96% of RCA rows), plus 3 smaller ones the
  title rules got wrong, are therefore classified by hand in `rca_reference_classes.yaml`. Title rules cover only the tail,
  and each catalog entry records which method classified it.

## Where RCA comes from (all of GOA, 2026-10-05)

8,610 RCA rows in total, classified by the analysis behind each reference:

| Analysis class | Rows | % | Main contributors |
|---|---:|---:|---|
| Pathway / metabolic model | 4,159 | 48.3 | SGD YeastPathways (4,133) — *out of scope* |
| Proteome-scale **computational** prediction | 2,029 | 23.6 | T. brucei MitoCarta SVM (1,039), yeast zinc proteome (580), PATS apicoplast predictor (275), Membranome (119) |
| **Proteomics** | 1,465 | 17.0 | BHF-UCL (688), TAIR (627), GeneDB (79), FlyBase (70) |
| **Interactomics** | 72 | 0.8 | GeneDB, T. brucei complex map and editosome |
| **Other omics** (reporter-fusion screen) | 17 | 0.2 | EcoCyc, E. coli inner-membrane topology |
| **Genetic screen** | 3 | 0.0 | EcoCyc |
| Single-gene / operon study | 387 | 4.5 | EcoCyc, AgBase (cotton and maize gene papers) |
| Gene-family / genome survey | 237 | 2.8 | MGI (98), GeneDB, EcoCyc |
| Unclassified tail and unresolved | 241 | 2.8 | 101 references with 1–4 rows; PAMGO GO_REF:0000028 |

**Omics-derived RCA is 1,557 rows (18.1%) from 24 references and 5 groups.** No
transcriptomics papers appear: expression data enter GO through IEP/HEP, not RCA.
The proteome-scale predictions are related but different. Each is a sequence classifier
applied to a whole proteome, and some of those papers also contain proteomics data,
but the GO term comes from the classifier. They are noted below rather than studied.

## How omics data are turned into GO annotations

Grouping the 1,557 omics rows by aspect and polarity (`rca_source_catalog.py`) shows
three distinct uses:

| Use | Rows | Groups (years annotated) | What the data show | What the row asserts |
|---|---:|---|---|---|
| **A. Location → function** | 731 (47%) | BHF-UCL 688 (2018–2025), FlyBase 35 (2019), GeneDB/EcoCyc 8 | Protein detected in an ECM or cuticle fraction | MF: *ECM structural constituent* and its children; *structural constituent of chitin-based cuticle* |
| **B. Exclusion → NOT location** | 627 (40%) | TAIR (2011–2012) | Protein excluded from a fraction's reported protein set (cytosol), or called a contaminant (Golgi) | `NOT located_in` cytosol / Golgi apparatus |
| **C. Location → location** | 199 (13%) | GeneDB 145, FlyBase 35, EcoCyc 19 | Protein in an organelle fraction, complex or topology screen | CC: mitochondrial inner membrane, food vacuole, editing complex, plasma membrane… |

Use C is the straightforward case: the aspect matches the data. Since the 2019 GO
guidance on high-throughput annotation (PMID:30715275; see *Evidence code* below),
however, a localization from a proteome is usually coded **HDA**, not RCA. Uses A and B
both claim more than the data can show, and the rest of this section examines them.

### A. Location → function: the matrisome category mapping (BHF-UCL)

BHF-UCL annotated proteins from ten ECM-enrichment proteomics papers (human, mouse and
pig, all annotated 2018 or later) with four molecular-function terms:

- `GO:0005201` extracellular matrix structural constituent
- `GO:0030020` …conferring tensile strength
- `GO:0030021` …conferring compression resistance
- `GO:0030023` extracellular matrix constituent conferring elasticity

**The term each protein received follows its category in the Naba in-silico matrisome**
(the classification published in PMID:22159717, one of the ten papers).
`rca_matrisome_crosswalk.py` joins all 164 distinct gene × term pairs to the human
matrisome masterlist:

| GO term | Collagens | ECM Glycoproteins | Proteoglycans | not in masterlist¹ |
|---|---:|---:|---:|---:|
| tensile strength (GO:0030020) | **42** | 0 | 0 | 1 |
| compression resistance (GO:0030021) | 0 | 0 | **17** | 0 |
| elasticity (GO:0030023) | 0 | **9** | 0 | 0 |
| ECM structural constituent (GO:0005201) | 0 | **89** | 0 | 6 |

¹ Non-human symbols with no human match (mouse *Col6a4*, *Mfap1a/b*; pig *TNX* and three
unnamed pig accessions).

Every matched gene is in the **core matrisome**. No "matrisome-associated" protein
(regulators, secreted factors, ECM-affiliated proteins) received any of these terms.
Each category maps to exactly one term: *every* collagen gets tensile strength, *every*
proteoglycan gets compression resistance, and every glycoprotein gets the generic
structural-constituent term. The one refinement is nine elastic-fibre glycoproteins
(ELN, EMILIN1–3, FBLN2, FBLN5, EFEMP2, MFAP5, LAMC1), which get elasticity, most of
them in addition to the generic term. The
GO term is therefore decided by the protein's **category**. The proteomics paper only
decides which proteins are in scope. This explains the ECO choice: ECO:0007666
explicitly combines computational evidence (the categorisation) with experimental
evidence (detection in the matrix). The 2019 GO high-throughput guidance mentions this
work:

> the Functional Gene Annotation team at University College London is currently
> undertaking, working with leaders in the field to develop a common set of standards
> for the annotation of extracellular matrix components from high-throughput proteomics
> studies.
> — PMID:30715275

**Where the mapping goes wrong.** A matrisome category is defined by domain
architecture and naming, not by mechanical role, so whole kinds of protein fall into
the wrong term:

| Category | What the mapping misses | Examples |
|---|---|---|
| ECM Glycoproteins → *structural constituent* | Matricellular and signalling proteins that sit in the matrix without holding it together | THBS1–4, SPARC, ABI3BP, MGP, CCN1, IGFBP6/7, VWF, SLIT2, NTN1, RELN, ADIPOQ |
| Proteoglycans → *compression resistance* | Small leucine-rich proteoglycans that bind collagen with one or two GAG chains; proteins that are proteoglycans **in name only** | DCN, ASPN, BGN, FMOD, LUM, OGN, PRELP; PRG2 and PRG3 (eosinophil granule proteins) |
| Collagens → *tensile strength* | Transmembrane and multiplexin collagens | COL13A1, COL17A1, COL23A1, COL25A1 (MACIT transmembrane collagens), COL18A1 |

**Reviewed outcomes by category** (this repository's gene reviews, 62 rows):

| Category | Reviewed rows | Accepted | Not accepted, by gene |
|---|---:|---:|---|
| Collagens | 6 | **6 (100%)** | — (only COL4A1 reviewed) |
| ECM Glycoproteins | 36 | 21 (58%) | ABI3BP, MGP, THBS3 (over-annotated); THBS1, THBS2 (modified); SPARC, ADIPOQ (removed) |
| Proteoglycans | 20 | 8 (40%) | ASPN (over-annotated); DCN (modified to `collagen binding`); PRG2, PRG3 (removed) |

The proteins accepted are the true load-bearing components: COL4A1, HSPG2 (perlecan),
ACAN, FN1, AGRN, NID1, DPT and COMP. Every rejection fits one of the three rows of the
"misses" table. The ABI3BP review puts the general point in one sentence:

> Detection in an ECM-enriched proteome supports the co-annotated cellular-component
> terms, not a molecular function asserting a contribution to structural integrity.

Two consequences follow:

- **The error rate is predictable from the category and the protein class**, so the
  unreviewed BHF-UCL rows can be triaged without re-reading the ten papers. All
  matricellular glycoproteins, all SLRPs, PRG2/PRG3 and the transmembrane collagens are
  the candidates (Action Items).
- **Our own reviews were inconsistent** about the replacement for matricellular
  proteins. THBS1 was MODIFIED to a CC term, THBS2 MODIFIED to a BP term, THBS3 marked
  over-annotated and SPARC REMOVED, all for the same reason. GO has no MF term for the
  matricellular class (ABI3BP's `proposed_new_terms` raises this), and that gap is why
  reviewers reach for different substitutes.

FlyBase's 35 MF rows from the *Bombyx mori* cuticle proteome (PMID:21761556, 2019)
take the same step from location to function (`structural constituent of chitin-based
cuticle`). Cuticular-protein families are defined by a chitin-binding motif, so the
same step is probably more defensible here, but none of these rows has been reviewed.

### B. Exclusion from a fraction proteome → NOT location (TAIR)

TAIR made 627 `NOT|located_in` rows from two Arabidopsis fraction proteomes (2011–2012,
before the high-throughput evidence codes existed):

- **PMID:21166475** (436 rows, NOT cytosol). The paper reports a "robust set of 1071
  cytosolic proteins". The 436 NOT rows are a specific list, not every protein missing
  from that set, so they are presumably proteins the authors excluded from the cytosol.
  The abstract does not say on what basis, and the full text is not openly available.
- **PMID:22430844** (191 rows, NOT Golgi apparatus). The paper's composition analysis
  assigned about 19% of identifications to "contaminating compartments and ribosomes",
  and the NOT rows presumably correspond to these.

`rca_not_contradictions.py` checks each NOT row against GOA for a positive annotation
of the same gene product to the same term or an `is_a`/`part_of` descendant:

| NOT row source | Rows | Contradicted (any code) | by experimental/HTP | by low-throughput IDA/EXP |
|---|---:|---:|---:|---:|
| Cytosol: absent from the robust set | 436 | **188 (43.1%)** | 172 (39.4%) | 28 (6.4%) |
| Golgi: called a contaminant | 191 | **5 (2.6%)** | 4 (2.1%) | 1 (0.5%) |

The contradiction rates of the two sets differ by more than tenfold. **The Golgi
contaminant calls hold up. The cytosol exclusions largely do not.** Why they differ
depends on how the cytosol paper chose its exclusions, which cannot be read from the
abstract (Action Items). Whatever the method, a protein excluded from one cell-culture
fraction is not evidence that it is absent from the cytosol, and the GAF row records
neither the tissue nor the criterion. The cytosol NOT rows include:

- **37 cytosolic ribosomal proteins** (RPL\*/RPS\* paralogs such as RPL11B, RPS18A and
  RPL24B). 36 of them are contradicted in GOA, mostly by three cytosolic-ribosome
  proteomes (PMID:17934214, 15821981, 15734919), and all 37 by ribosome biology.
- Proteins with direct low-throughput cytosolic localization, including OST1/SRK2E,
  SRK2B, the PP2A A and C subunits, the exocyst subunits SEC3A/SEC10a/SEC15B, UPF1 and
  HSP70-1. Two of these were reviewed in this repository (OST1 and HSP70-1/AT5G02500),
  and both reviews REMOVED the row. The third reviewed row, BCAT3 (plastid-targeted),
  was ACCEPTED: the NOT is true there, but for reasons the proteome did not test.

Most contradictions come from other high-throughput datasets (153 rows by HDA, mainly
the PMID:28887381 membrane-oligomerization profiling and the PMID:25293756 complex
proteome). GOA therefore contains direct conflicts between proteomes, unresolved and
both curator-made. This links directly to the [NOT annotation](../NOT_ANNOTATION_USAGE.md)
project.

### Evidence code: HDA, and the Use C question

The GO consortium's 2019 framework (PMID:30715275) introduced the high-throughput codes
HTP/HDA/HMP/HGI/HEP so that users can separate screen-derived annotations from
hypothesis-driven ones. Measured against it:

- **Use C (location → location)** is the case HDA was designed for. GeneDB's
  organelle-proteome rows (2009–2014) and EcoCyc's topology-screen rows predate or
  overlap its introduction. Re-coding them would be the expected clean-up. They are
  not otherwise wrong in kind.
- **Use A (location → function)** cannot simply be re-coded as HDA. The MF does not come
  from an assay, so the honest code really is a computational one. The problem is the
  inference, not the label.
- **Use B (NOT from exclusion)** is a negative claim built on high-throughput data. The
  guidance is about controlling false positives in positive calls (e.g. "proteins should
  be identified by a minimum of two unique peptides"). It offers nothing that would
  license a NOT from leaving a protein out of one fraction, and the 43% contradiction
  rate shows why.

## Reviewer checklist for omics-derived RCA

1. **Find the reference's use** (A, B or C) from the table above or in
   [`rca_reference_catalog.yaml`](rca/data/rca_reference_catalog.yaml).
2. **Use A, an ECM "structural constituent" term from a matrisome paper:** ask whether
   the protein is load-bearing. Collagens of the fibrillar and network types,
   perlecan, aggrecan, fibronectin, laminins and nidogens usually are. Matricellular
   proteins, SLRPs, growth-factor binders, PRG2/PRG3 and transmembrane collagens are not.
   Check that the CC (`located_in extracellular matrix`) is present, because that is
   what the data actually support.
3. **Use B, NOT located_in from a fraction proteome:** look for any positive annotation to
   the same compartment, including HDA from another proteome. For PMID:21166475, treat
   the NOT row as suspect until it is confirmed. For PMID:22430844, it is usually right.
4. **Use C:** accept the location if the term is at the right granularity, and note that
   HDA would be the current code.
5. **Do not read "Reviewed" as protein-level review.** In every use, the review was of
   a method or mapping, applied once to a whole list.

## Recommendations

1. **One disposition for "matricellular → ECM structural constituent".** The proposal is
   MARK_AS_OVER_ANNOTATED, together with a `located_in extracellular matrix` NEW row
   where one is missing and a reference to the matricellular-MF `proposed_new_terms`
   entry. Then reconcile THBS1, THBS2 and SPARC.
2. **Report the mapping to BHF-UCL** as category-level findings rather than gene-level
   ones: SLRPs should not receive compression resistance, PRG2/PRG3 are not
   proteoglycans of the matrix, and transmembrane collagens should not receive tensile
   strength. The review rationales for DCN, ASPN, PRG2/PRG3, SPARC and THBS1–3 already
   provide worked examples.
3. **Report the cytosol NOT rows to TAIR**, starting with the 37 ribosomal-protein rows and the
   28 rows contradicted by low-throughput IDA. The Golgi set is sound and needs no action.

## Action items

- [ ] Triage the **unreviewed BHF-UCL rows** using the misses table. List every gene ×
      term pair whose protein is matricellular, an SLRP, PRG2/PRG3 or a transmembrane
      collagen, and spot-check about 10 that have gene reviews or are easy to review.
- [ ] Review a sample of the **FlyBase *Bombyx* cuticle MF rows** (Use A, outside the
      matrisome) to see whether the same step from location to function holds there.
- [ ] Get the full text of PMID:21166475 to find how the 436 cytosol exclusions were
      chosen, and whether that criterion explains the 43% vs 2.6% contrast.
- [ ] Turn `rca_not_contradictions.py` output into a submission-ready list for TAIR:
      ribosomal proteins plus IDA-contradicted rows.
- [ ] Sample **GeneDB Use C rows** (organelle proteomes, complex map) for correct granularity,
      e.g. 64 trypanosomatid gene products all placed in `mitochondrial mRNA editing
      complex` from one complex map.
- [ ] Add a regression test that `rca_matrisome_crosswalk.py` stays fully on its category
      diagonal for matched human genes. Any deviation would mean BHF-UCL has started
      annotating gene by gene.

## Out of scope: quirks noted, not studied

**YeastPathways import (GO_REF:0000123), 4,133 rows (48% of all RCA).** SGD exports its
curated YeastPathways GO-CAMs to the GAF with RCA (`WITH/FROM` = `SGD_PWY:*`). A curated
pathway model is not "a computational analysis of large-scale data", so **RCA is
probably the wrong evidence code here**. The rows are curated pathway assertions, which
are closer to IC or TAS than to RCA. They also share the usual pathway-to-gene failure
modes. The two reviewed in this repository illustrate them: SOD2 received the pathway's
default `is_active_in cytosol`, although SOD2 is mitochondrial, and ERG19 received an
FPP-biosynthesis process for a product made downstream of it. Both rows were REMOVED.
A full treatment belongs with GO-CAM review, not here.

**Proteome-scale computational predictions (2,029 rows).** Examples are the T. brucei
MitoCarta SVM, the PATS apicoplast predictor, Membranome and the yeast zinc-proteome
domain/motif scan. These are sequence-model predictions, the use ISM was created for.
The zinc rows are the only ones reviewed here: 32 rows, 19 ACCEPT and 10 KEEP_AS_NON_CORE.

**RCA on this repository's `NEW` rows.** 38 reviewer-authored rows use RCA for ARO→GO
mappings, UniProt cross-references and PN projections. RCA is probably not the right
code for these. Changing it is deferred.

## Session notes

### 2026-10-05 (second pass: refocus on omics)

Refocused the project on omics-derived RCA, as requested. Added `rca_source_catalog.py`,
which downloads all 8,610 RCA rows, fetches titles and classifies every reference, with
hand calls for 60 references (all 57 with ≥5 rows, plus 3) in `rca_reference_classes.yaml`. Found that
omics accounts for 1,557 rows in three uses (A/B/C). Added `rca_matrisome_crosswalk.py`,
which shows that BHF-UCL's ECM MF terms follow the Naba matrisome category for every
matched gene. Added `rca_not_contradictions.py`, which shows that 43% of TAIR's
cytosol-proteome NOT rows are contradicted, against 2.6% of its Golgi-contaminant
NOT rows. Cached PMID:30715275 (GO HTP guidance). Moved
YeastPathways and the NEW-row question to "Out of scope".

### 2026-10-05 (first pass: inventory and scoping)

Created the project. Inventoried GOA and reviewed RCA rows in the gene corpus
(`rca_inventory.py`: 130 GOA rows, all reviewed; 156 reviewed rows including 38 NEW)
and global denominators (`rca_quickgo_global.py`).
