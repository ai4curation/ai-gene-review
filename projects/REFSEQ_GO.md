---
title: "NCBI RefSeq vs UniProt/GOA: prokaryotic GO pipeline comparison"
collections: [FUNCTION_PREDICTION]
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [PSEPK, PSEAE]
autolink_exclude: [degP, DegP, dnaA, ftsI, FtsI]
manifest:
  artifacts:
    - href: https://claude.ai/artifact/LEUxu7VHiPqHcJGm1EcYFq
      title: Why NCBI misses GO terms that GOA keeps
      description: worked examples (PP_0661, E. coli EntE) of winner-take-all naming
    - href: https://claude.ai/artifact/XyN2cmWm1r77VGG1efpgSY
      title: NCBI prokaryotic GO map
      description: how RefSeq, PGAP, SPARCLE, Gene, gene2go, FTP and Datasets fit together
---

# NCBI RefSeq vs UniProt/GOA: prokaryotic GO pipeline comparison

**Bottom line:** since 2022, NCBI's Prokaryotic Genome Annotation Pipeline (PGAP)
has put GO terms on RefSeq prokaryotic proteins, and per-assembly GAF files now
sit on the NCBI FTP site. GO does not ingest them, and nobody had compared them
with GOA. The two pipelines differ in kind. **NCBI is winner-take-all:** GO is an
attribute of the single protein family model that *names* the protein, so every
protein gets terms from exactly one evidence source. **UniProt/GOA is a union** of
InterPro2GO, TreeGrafter, UniRule, ARBA, EC/Rhea2GO, SubCell and others. On
*Pseudomonas putida* KT2440, scored against 956 curated gene reviews, **NCBI is
about as accurate and much less complete.** Wrong terms (REMOVE) are rare on both
sides: 3.2% of the NCBI terms reviewers could judge, against 4.8% of GOA's
electronic terms, and NCBI has fewer true-but-too-general terms (5.9% against
11.6%). But NCBI covers only half of the reviewed core molecular functions (52%,
against 81%) and about a third of core processes (37%, against 67%), and it has almost no cellular-component
annotation. The biggest NCBI-specific source is **CDD domain architectures
(SPARCLE)**, not the CDD `cd` models that InterPro integrates. They name 47% of
GO-bearing proteins and are the least concordant source. Each pipeline has its
own failure modes: GOA transfers functions between paralogs, NCBI's specific
equivalogs avoid that, and NCBI has wrong GO on a few named models (listed
below) that propagates to every genome.

This page also carries the history of GO–NCBI contact on prokaryotic GO, which
was reconstructed from email when the topic resurfaced in October 2026.

## Relationship to the NCBIFam project

[NCBIFam](NCBIFam.md) measures how NCBIFAM/CDD *signatures* reach GOA through
InterPro2GO, and proposes an `ncbifam2go` built from `hmm_PGAP.tsv`. This project
compares the **outputs**: the GO that NCBI actually assigns to proteins against the
GO that GOA assigns, gene by gene.

One correction to that project's framing: NCBIFam.md says that "CDD-proper has
no native GO". That is true of the `cd` models, but NCBI also keeps GO as an
attribute of **CDD domain architectures** (SPARCLE, `ArchId:` in the GAF
WITH/FROM column), and has propagated it to proteins since March 2023. This GO
is not in `cddannot*.dat` or `hmm_PGAP.tsv`, so the NCBIFam probe could not see
it. In the KT2440 GAF it is the largest single source.

## How the two pipelines assign GO

| | NCBI RefSeq (PGAP) | UniProt / GOA |
|---|---|---|
| Unit annotated | non-redundant `WP_` protein, shared across all genomes that encode the identical sequence | UniProtKB entry (per proteome; Swiss-Prot + TrEMBL) |
| Gene models | PGAP re-annotation of each RefSeq assembly (new `*_RS*` locus tags; old tags kept as `old_locus_tag`) | INSDC submitter CDS, translated; for older genomes, the original submission |
| Where GO lives | an attribute of protein family models: NCBIFam/TIGRFAM HMMs, Pfam HMMs wrapped as NF models (GO imported from `pfam2go`, which is itself derived from InterPro2GO; NCBI may add or remove attributes on its stored copy of each Pfam, and had added GO to about 20 by 2022), BlastRules (`NBR…`), CDD/SPARCLE architectures (`ArchId:`), and a few `cluster:` sources | external2go mappings (InterPro2GO, EC2GO, Rhea2GO, UniPathway2GO, KW2GO, SubCell2GO), rule systems (UniRule, ARBA), phylogenetic propagation (PAINT IBA, TreeGrafter), experimental curation |
| Combination rule | **only the model that names the protein passes on its GO**: one WITH/FROM per protein | **union** of every pipeline that fires |
| Evidence/reference | all `IEA`, `PMID:33270901` (the PGAP paper), WITH/FROM = the naming model | IEA with a pipeline-specific `GO_REF`, plus experimental codes |
| Distribution | `<assembly>_gene_ontology.gaf.gz` per assembly on `ftp.ncbi.nlm.nih.gov/genomes/all/`, GAF 2.2, `assigned_by=RefSeq` | GOA GAFs, QuickGO, GO releases |
| Known gaps | the roughly 15 community-curated reference genomes (e.g. *E. coli* K-12 MG1655, *B. subtilis* 168) are annotated differently and have no GAF; FTP backlog; GO version lags; some proteins lack a symbol, though GAF requires one | — |

The winner-take-all rule is the main structural difference. NCBI's design
favours precision: a protein named from a specific equivalog HMM inherits only
that HMM's curated terms, and broad domain terms from other hits are not added.
GOA favours recall, and stacks domain-level InterPro2GO terms with family- and
rule-level terms.

The winner-take-all rule applies to prokaryotes only. NCBI annotates eukaryotic
RefSeq with a separate pipeline (since 2023): InterProScan with InterPro2GO and
PANTHER/TreeGrafter GO, keyed to NCBI GeneIDs. That pipeline is much closer to
UniProt's and is out of scope here.

## Pilot: *P. putida* KT2440 (PSEPK)

Script: [`compare_refseq_goa.py`](REFSEQ_GO/compare_refseq_goa.py). Two runs are
kept:

- [`results/PSEPK/`](REFSEQ_GO/results/PSEPK/summary.yaml): NCBI GO from the
  **live** RefSeq genome record (annotation `RS_2026_02_04`, PGAP 6.10), with each
  protein's naming model taken from its WP_ record. This is the default.
- [`results/PSEPK_ftp_RS_2025_02_17/`](REFSEQ_GO/results/PSEPK_ftp_RS_2025_02_17/summary.yaml):
  NCBI GO from the downloadable GAF (annotation `RS_2025_02_17`, generated
  2025-06-12, GO version 2025-03-16). The detailed numbers further down this page
  come from this run; [Live record vs FTP](#live-record-vs-ftp) gives the 2026
  headline numbers.

Both runs use GOA for taxon 160488 from QuickGO and UniProt proteome
`UP000000556`, all fetched on 2026-10-18.

```bash
uv run python projects/REFSEQ_GO/compare_refseq_goa.py \
  --accession GCF_000007565 --taxon 160488 --proteome UP000000556 \
  --locus-regex 'PP_\d+' --out-dir projects/REFSEQ_GO/results/PSEPK
# add --ncbi-source ftp to use the per-assembly GAF instead of the live record
```

The script resolves the accession through the NCBI Datasets v2 REST API and
rejects a superseded accession. NCBI's Python client (`ncbi-datasets-pylib`) was
retired at the end of 2024, so the REST API is called directly. Datasets genome
packages have no GO option. GO therefore comes either from the GenBank record's
`/GO_function`, `/GO_process` and `/GO_component` qualifiers, fetched with
E-utilities, or from the FTP GAF. The genome record does not say which model
named each protein, so that is read from the `Evidence-For-Name-Assignment` block
of the WP_ protein records. The annotation release and fetch times are recorded
in `summary.yaml`.

### Identifiers and annotation releases

- **No NCBI Gene records.** All 6,027 KT2440 Gene records were discontinued on
  2020-04-02; one remains live. NCBI now provides Gene records only for
  prokaryotic reference genomes
  ([RefSeq prokaryote FAQ](https://www.ncbi.nlm.nih.gov/refseq/about/prokaryotes/faq/)),
  and in February 2020 it reduced Reference assemblies to the 15 with
  expert-provided annotation. *E. coli* K-12 (4,652 live records), *B. subtilis*
  168 (4,537) and *P. aeruginosa* PAO1 (5,698) keep theirs.
- **What remains is the RefSeq genome record.** Genes are features on
  `NC_002947.4` with a locus tag (`PP_RS00285`) and the original TIGR tag as
  `old_locus_tag` (`PP_0055`). The protein is a non-redundant `WP_` accession,
  shared by every genome that encodes the identical sequence. The earlier
  genome-specific `NP_`/`YP_` proteins were suppressed in NCBI's one-time
  re-annotation project, which for KT2440 replaced the record on 2016-03-04
  ([re-annotation project](https://www.ncbi.nlm.nih.gov/refseq/about/prokaryotes/reannotation/)).
- **Re-annotation continues.** Since then the genome has been re-annotated
  repeatedly with newer PGAP versions. The live record carries
  `GCF_000007565.2-RS_2026_02_04` (PGAP 6.10). Locus tags were kept:
  `PP_RS00285`/`PP_0055` is unchanged.
- **The downloads lag the live record.** The Datasets API and the FTP files
  (GAF, feature table, GBFF; all dated 2025-06-12) still serve
  `RS_2025_02_17` (PGAP 6.9). The live record does carry GO, as CDS
  qualifiers, so the script now reads GO from it by default
  (`--ncbi-source live`).

### Live record vs FTP

Between the February 2025 annotation (FTP) and the February 2026 annotation
(live record), 742 of 5,483 shared genes (13.5%) changed GO: 934 terms were
added and 180 removed, 134 genes gained GO for the first time, and 316 product
names changed. Locus tags did not change. The conclusions hold on the newer
annotation:

| | FTP, RS_2025_02_17 | live, RS_2026_02_04 |
|---|---:|---:|
| shared loci with NCBI GO | 3,413 | 3,513 |
| exact agreement with GOA: NCBIFam / TIGRFAM / architecture | 90% / 79% / 69% | 91% / 80% / 66% |
| NCBI terms reviewers REMOVEd (wrong) | 3.3% | 3.2% |
| core MF covered, NCBI (GOA electronic 81%) | 51% | 52% |
| core BP covered, NCBI (GOA electronic 67%) | 36% | 37% |
| genes with GOA GO and no NCBI GO | 780 | 699 |

Every model-level error listed under [Failure modes](#failure-modes) is still
present in the live record.

### Gene models differ, and the obvious join key is lossy

Genes are joined on the original `PP_xxxx` locus tag: from the RefSeq gene
`old_locus_tag`, and from UniProt's ordered locus name.

- 5,487 RefSeq protein-coding loci (plus 132 pseudogenes) against 5,563
  locus-tagged UniProt entries; **5,390 are shared**.
- **173 loci are UniProt-only.** Of these, 39 are RefSeq pseudogenes and 134
  are absent from the current RefSeq annotation altogether. These are original
  2002 gene calls that the PGAP re-annotation dropped or merged. **97 loci are
  RefSeq-only.**
- **1,007 UniProt entries (18%) have no RefSeq `WP_` cross-reference**, even
  though most of their loci have a WP_ protein. A join on WP_ cross-references
  would silently lose almost a fifth of the proteome, so the locus-tag join is
  needed.
- 20 WP_ proteins are encoded at several loci (identical paralogs).

### Coverage

| Over the 5,390 shared loci | NCBI | GOA |
|---|---:|---:|
| loci with ≥1 GO term | 3,413 (63%) | 3,871 (72%) |
| distinct (locus, term) annotations | 8,264 | 17,246 |

GOA has about twice as many terms per gene. This is the expected result of a
union against a single source.

### Agreement by NCBI evidence source

Each NCBI term was compared with the GOA terms for the same locus and aspect,
closure-aware over `is_a` and `part_of`. Only locus–aspect pairs annotated on
both sides are counted here; the rest appear in the TSV as
`other_side_no_aspect`.

| NCBI source | proteins named | terms compared | exact | GOA more specific | GOA more general | NCBI only |
|---|---:|---:|---:|---:|---:|---:|
| ArchId (CDD/SPARCLE architecture) | 1,593 | 3,082 | 69% | 5% | 8% | **18%** |
| HMM: TIGRFAM | 911 | 2,255 | 79% | 4% | 6% | 11% |
| HMM: NCBIFam (incl. wrapped Pfam) | 885 | 1,808 | 90% | 2% | 1% | 7% |
| BlastRule | 11 | 46 | 100% | — | — | — |

Most NCBI-only terms from architectures are broad ligand-binding or
transport terms, such as `metal ion binding` (91), `ATP binding` (45),
`ABC-type transporter activity` (31) and `monoatomic ion transport` (30). This
fits domain-architecture-level GO. Those terms have not yet been checked against
curated reviews.

From the GOA side, the sources least represented in NCBI are UniRule (46% of
compared terms have no NCBI counterpart), TreeGrafter (42%) and ARBA (31%).
InterPro2GO is 17%. The top GOA-only terms are UniRule's `DNA-templated
transcription` (155 loci) and generic `DNA binding` and `transmembrane transport`.

Experimental GOA annotations (EXP/IDA/IMP/IPI/IEP, 147 rows) are mostly
uncovered by NCBI. In aspects where both sides annotate, 16 match exactly, 2 are
more specific in NCBI, 17 are more general in NCBI, and 40 have no NCBI
counterpart.

### Staleness

The KT2440 GAF was generated in June 2025 against GO 2025-03-16, and has not
been refreshed since. 49 of its 1,626 distinct terms (3%) are obsolete in the
current GO. Most belong to the 2025–2026 obsoletions of "via X" pathway
variants and amino-acid metabolism, e.g. `GO:0009089`, `GO:0006542` and
`GO:0051082`. The comparison counts these as NCBI-only.

## Comparison results (KT2440)

Script: [`analyze_refseq_goa.py`](REFSEQ_GO/analyze_refseq_goa.py). The numbers in
this section are from the February 2025 (FTP) run; the same tables for the live
run are in `results/PSEPK/`. Generated tables:
[`analysis.yaml`](REFSEQ_GO/results/PSEPK_ftp_RS_2025_02_17/analysis.yaml),
[`ncbi_review_cases.tsv`](REFSEQ_GO/results/PSEPK_ftp_RS_2025_02_17/ncbi_review_cases.tsv),
[`goa_errors_vs_ncbi.tsv`](REFSEQ_GO/results/PSEPK_ftp_RS_2025_02_17/goa_errors_vs_ncbi.tsv) and
[`core_coverage.tsv`](REFSEQ_GO/results/PSEPK_ftp_RS_2025_02_17/core_coverage.tsv). Cases checked by hand, and
re-checked against the live record:
[`failure_cases.yaml`](REFSEQ_GO/results/PSEPK/failure_cases.yaml).

```bash
uv run python projects/REFSEQ_GO/analyze_refseq_goa.py \
  --results-dir projects/REFSEQ_GO/results/PSEPK --species PSEPK
```

### Level 1: gross differences across the genome

| Over 5,390 shared loci | NCBI loci | GOA loci | both | NCBI only | GOA only | NCBI terms | GOA terms |
|---|---:|---:|---:|---:|---:|---:|---:|
| molecular function | 3,010 | 3,306 | 2,579 | 431 | 727 | 4,571 | 8,367 |
| biological process | 2,276 | 2,840 | 1,929 | 347 | 911 | 2,649 | 5,297 |
| cellular component | 944 | 2,309 | 830 | 114 | 1,479 | 1,044 | 3,582 |

- **Cellular component is the largest gap.** At `goslim_prokaryote` level, GOA
  places 981 loci in `cytoplasm` and 835 in `plasma membrane`; NCBI places 99 and
  196. GOA gets these from SubCell2GO, ARBA and the combined pipeline, which have
  no NCBI equivalent.
- **Generic transcription terms.** `DNA-templated transcription` is on 348 loci
  in GOA and 28 in NCBI, mostly UniRule adding it to transcription factors.
  Only 4 UniRule rows of this term fall in reviewed genes (2 marked
  over-annotated, 1 removed, 1 modified), which is too few to judge.
- **NCBI has more `ATP-dependent activity`** (274 loci against 214). This is the
  only slim class where NCBI leads.
- **322 genes have NCBI GO and no GOA GO.** 213 of them are named by an
  architecture: transposases, Csu fimbrial proteins, Hcp T6SS effectors,
  MvaT/MvaU nucleoid proteins, GSTs, glycosyltransferases. This is NCBI's real
  coverage gain.
- **780 genes have GOA GO and no NCBI GO.** Their RefSeq names show why. The top
  name is "LysR substrate-binding domain-containing protein" (22). When the
  naming model is a domain model with no GO, the protein gets nothing, even if
  its other hits (here a LysR HTH domain, which InterPro2GO maps to
  `DNA-binding transcription factor activity`) carry GO. This recall failure is
  built into winner-take-all.

### Level 2: by source

From the NCBI side, agreement falls in this order: BlastRules (100% exact),
NCBIFam (90%), TIGRFAM (79%), then architectures (69%; 18% NCBI-only); see
[Agreement by NCBI evidence source](#agreement-by-ncbi-evidence-source). From the
GOA side (with combined GO_REF:0000120 rows credited to each contributing
pipeline), the terms NCBI least often supports are GO inter-ontology links (55%
have no NCBI counterpart), TreeGrafter BP (35%) and UniRule BP (33%). InterPro2GO
MF terms more often have a *more specific* NCBI counterpart (19%) than none
(14%).

### Level 3: against 956 curated reviews

Reviewers judged GOA rows, not NCBI rows. So an NCBI term shared with GOA
inherits the reviewer's verdict, and an NCBI term absent from GOA is judged only
by its relation to the accepted and removed terms. Terms with no such relation
are `unassessed`, and these were checked by hand (below).

| | terms | correct (accepted or implied) | modified | too general | over-annotated (other) | wrong (REMOVE) | unassessed |
|---|---:|---:|---:|---:|---:|---:|---:|
| **NCBI, all** | 2,078 | 69.5% | 6.1% | 4.7% | 4.5% | 3.2% | 10.8% |
| NCBI TIGRFAM | 1,071 | 75.9% | 4.9% | 2.9% | 3.6% | 2.1% | 9.7% |
| NCBI NCBIFam | 661 | 67.2% | 7.3% | 6.5% | 7.1% | 5.1% | 5.4% |
| NCBI architecture | 346 | 54.1% | 7.5% | 6.6% | 2.0% | 3.5% | 24.3% |
| **GOA electronic, all** | 4,926 | 68.4% | 7.9% | 11.6% | 5.0% | 4.8% | 0.5% |
| GOA InterPro2GO | 2,690 | 62.5% | 9.3% | 17.2% | 5.4% | 4.3% | 0.1% |
| GOA TreeGrafter | 1,486 | 81.0% | 5.4% | 2.2% | 4.2% | 4.7% | 0% |
| GOA UniRule | 1,658 | 83.8% | 4.1% | 4.7% | 3.7% | 2.2% | 0.8% |
| GOA ARBA | 592 | 69.9% | 7.3% | 15.4% | 2.7% | 2.2% | 1.5% |

"Correct" adds terms that are proper ancestors or descendants of an accepted
term. "Too general" is a term the reviewer marked over-annotated that is an
ancestor of a term the reviewer accepted: true, just less specific. Rows do not
sum to 100% because `undecided` (1–3%) is omitted. GOA terms agreed by several
pipelines (GO_REF:0000120) count for each of them. Among NCBI's HMM sources,
NCBI's own NCBIfam models have more wrong (5.1% against 2.1%) and more
too-general terms (6.5% against 2.9%) than TIGRFAM, mostly broad cofactor and
category terms (`carbohydrate metabolic process`, `membrane`, `metal ion
binding`, `ATP binding`) attached to otherwise specific models.

**Core-function coverage** (terms in the reviews' `core_functions`):

| | covered (same or more specific) | only a more general term | missed |
|---|---:|---:|---:|
| core MF (917), NCBI | 466 (51%) | 110 (12%) | 341 (37%) |
| core MF, GOA electronic | 743 (81%) | 55 (6%) | 119 (13%) |
| core BP (1,042), NCBI | 378 (36%) | 145 (14%) | 519 (50%) |
| core BP, GOA electronic | 700 (67%) | 85 (8%) | 257 (25%) |

NCBI covers a core function that GOA's electronic pipelines miss in only 7 MF
and 31 BP cases. The reverse happens in 211 MF and 266 BP cases.

**GOA errors and NCBI.** Of the 115 InterPro2GO terms that reviewers removed, NCBI
asserts the same term in 66. That much overlap suggests the two share
provenance for part of their family→GO mappings. Of the 70 TreeGrafter terms
removed, NCBI asserts one.

### Failure modes

Every case below is recorded in
[`failure_cases.yaml`](REFSEQ_GO/results/PSEPK/failure_cases.yaml).

**Errors only NCBI makes.** These come from the 224 unassessed NCBI terms. 64 of
those are obsolete terms (GO-version lag), not mapping errors. Among the rest,
the following are clear errors. Where marked *(model)*, the GO is listed on the
HMM itself in `hmm_PGAP.tsv`, so one fix corrects every genome.

- Wrong function on the model: SecG → sialic acid transport *(model, TIGR00810)*;
  QueF → a tRNA-ribosyltransferase activity *(model, TIGR03138)*; Lgt → protein
  lipoylation *(model, TIGR00544)*; TatC → type II secretion *(model, TIGR00945)*;
  MlaC-family Ttg2D → ABC-type transporter activity.
- Model name and GO disagree: TIGR01162 is named the N5-CAIR *mutase* but carries
  the *carboxylase* activity *(model)*.
- A substrate given an activity: precursor peptide PqqA → `catalytic activity`
  *(model, TIGR02107)*.
- Pathway context ignored: Aacs → mevalonate pathway *(model, TIGR01217)*, a
  pathway KT2440 lacks.
- Complex activity given to one subunit: SdhC and SdhD → succinate dehydrogenase
  activity *(model)*; YajC → protein-transporting ATPase *(model)*; PP_3384
  (gluconate 2-dehydrogenase gamma subunit) → an NADP+ gluconate dehydrogenase
  activity.
- Architecture-level transfer (the CDD-specific mode): ImuB → DNA polymerase
  activity, though it is catalytically inactive; GlgE → oligosaccharide
  *catabolic* process, though it is biosynthetic; a saccharopine-dehydrogenase-family
  carboxyspermidine dehydrogenase → lysine biosynthesis; MoaA paralogs →
  molybdopterin synthase complex; OprD's basic-amino-acid substrate copied to
  OprE, NicP and GalP.

**Errors only GOA makes**, which NCBI's specific equivalogs avoided. Paralog
transfers dominate. TreeGrafter: Mqo1–3 → (S)-2-hydroxyglutarate dehydrogenase,
DapE → acetylornithine deacetylase, MetX → the acetyl- rather than
succinyltransferase activity, KdsC → a cytidylyltransferase, PhnX →
phosphoglycolate phosphatase, Gcl → valine biosynthesis. InterPro2GO: GlyS →
*arginine*-tRNA ligase, ThiI → CCA-adding activity, PurC → cobalamin
biosynthesis.

**Errors both make** (66 reviewer-removed terms that NCBI also asserts):
- Complex activity given to one subunit: the DNA polymerase III β, ε and τ subunits
  given polymerase activity; EutC, CarA, NirD and SoxG.
- Wrong cofactor: NAD binding on the NADP-specific Icd; 2Fe-2S binding on PrpD,
  which has no cluster; ATP binding on DnaJ and GroES.
- Paralog substrate: PssA given PgsA's reaction; NH3-dependent NadE given glutamine
  activities.
- Reversed direction: GpsA as catabolic, Dfp as pantothenate *catabolism*.

**Naming.** Sometimes the name is the error. NCBI names PycB a sodium-extruding
oxaloacetate decarboxylase, where the review assigns pyruvate carboxylase. In the
other direction, UniProt still carries the 2002 submitter name for PP_3099 (puuD,
"uricase"), while NCBI correctly names it the T6SS sheath protein TssC.

### Worked case: the ParAB chromosome-partition proteins

ParA and ParB were reviewed in *P. putida* KT2440 and in *P. aeruginosa* PAO1,
where both proteins have been characterized experimentally. Each review has a
companion PGAP prediction review that scores NCBI's GO term by term. The
orthologs are 84% (ParA) and 79% (ParB) identical, with identical Walker A
and CTP-binding motifs
([alignment](../genes/PSEPK/parA/parA-bioinformatics/RESULTS.md)), so any
difference between the two species comes from the pipelines, not the
biology.

| protein | NCBI naming source | NCBI GO | GOA GO | reviewed core function |
|---|---|---|---|---|
| PSEPK/parA (PP_0002) | architecture 11439703, "ParA family protein" | ATP binding, ATP hydrolysis activity | **none** | ATP hydrolysis activity; chromosome segregation |
| PSEAE/parA (PA5563) | BlastRule NBR012933, "chromosome partitioning protein Soj" | **none** | **none** | ATP hydrolysis activity (IDA); chromosome segregation (IMP) |
| PSEPK/parB (PP_0001) | architecture 11445026, "ParB/RepB/Spo0J family partition protein" | DNA binding | DNA binding, chromosome, chromosome segregation, positive regulation of sporulation | sequence-specific DNA binding; CTPase activity; chromosome segregation |
| PSEAE/parB (PA5562) | architecture 11445026 | DNA binding | as PP_0001, plus identical protein binding (IPI) and two UniRule transcription terms | sequence-specific DNA binding (IDA); CTPase activity (IDA); chromosome segregation |

Prediction reviews:
[PP_0002](../genes/PSEPK/parA/parA-pgap-predictions-review.yaml),
[PA5563](../genes/PSEAE/parA/parA-pgap-predictions-review.yaml),
[PP_0001](../genes/PSEPK/parB/parB-pgap-predictions-review.yaml),
[PA5562](../genes/PSEAE/parB/parB-pgap-predictions-review.yaml).

What the case shows:

- **An architecture can fill a gap that GOA leaves completely open.** GOA has no
  annotation of any kind for either ParA. The Pfam domain (AAA_31) has no
  InterPro2GO mapping and the PANTHER subfamily brings no IBA. In *P. putida*,
  UniProt still calls the Swiss-Prot entry "Uncharacterized protein PP_0002".
  NCBI's architecture GO for PP_0002 is correct, and it is the only GO this
  protein has anywhere.
- **The same architecture is not used for the ortholog.** The *P. aeruginosa*
  ParA is named by a BlastRule instead, which gives it a better name and no GO.
  Under winner-take-all the architecture's terms are then not passed on, so a
  well-studied ATPase ends up with no GO from either pipeline. Adding ATP
  hydrolysis activity (GO:0016887) and chromosome segregation (GO:0007059) to
  NBR012933 would reach the 53,688 assemblies that carry WP_003097243.1.
- **The naming model is not the most informative model.** For both ParBs, the
  architecture passes on only `DNA binding`. TIGR00180 also matches, has the
  same product name, and carries chromosome segregation (plus a debatable
  cytokinesis term), but it does not pass on its GO because it did not name the
  protein. Adding GO:0007059 to architecture 11445026 would restore the core
  process on every ParB it names. That includes WP_003100240.1, which alone is
  in 39,809 assemblies.
- **Neither pipeline knows ParB is a CTPase.** The CDD region note still
  describes the N-terminal domain as a "ParB-like nuclease domain". The ParB
  CTPase activity (GO:0043273), measured directly on *P. aeruginosa* ParB
  (PMID:38843873), is absent from NCBI, from GOA and from every matched
  model. The ParB family was shown to be a CTPase in 2019, but none of these
  family models carries the term.
- **NCBI avoids two GOA errors.** GOA gives both ParBs `positive regulation of
  sporulation` from the *B. subtilis* Spo0J-seeded PANTHER node (IBA in PAO1,
  TreeGrafter in KT2440), although neither species sporulates. It also gives
  the PAO1 ParB `DNA-templated transcription` from a UniRule. The reviews
  remove all three of these rows, and NCBI asserts none of them.

## Second genome: *E. coli* K-12, via WP_ records

*E. coli* K-12 MG1655 is one of the 15 curated references, so PGAP never runs on
its assembly. PGAP's GO is attached to non-redundant WP_ proteins, though, and
almost every MG1655 protein is identical to a WP_ protein that PGAP annotates in
other genomes. The compare script's `--ncbi-source wp` mode follows each UniProt
entry's WP_ cross-reference and reads GO and the naming model from the WP_
GenPept record. It compares proteins, not gene models.

```bash
uv run python projects/REFSEQ_GO/compare_refseq_goa.py \
  --accession GCF_000005845 --taxon 83333 --proteome UP000000625 \
  --locus-regex 'b\d{4}' --ncbi-source wp --out-dir projects/REFSEQ_GO/results/ECOLI_wp
uv run python projects/REFSEQ_GO/analyze_refseq_goa.py \
  --results-dir projects/REFSEQ_GO/results/ECOLI_wp --species ECOLI
```

**The WP_ records are the freshest PGAP source.** Run in `wp` mode on KT2440
([`results/PSEPK_wp/`](REFSEQ_GO/results/PSEPK_wp/summary.yaml)), the 4,504
proteins reachable both ways have the same naming model in all cases and the
same GO in 4,247 (94%) when compared with the live February 2026 genome record.
Of the 257 differences, 184 are on WP_ records modified during 2026, and the
examples are obsolete terms the genome record still carries but the WP_ record
has replaced (GO:0019557 → GO:0006548, GO:0008785 → GO:0102039). WP_ records are
dated up to 2026-10-16. The cost is coverage: WP_ cross-references are missing
from 18% of KT2440 UniProt entries but only 7% of K-12 entries (4,112 of 4,403
have one).

**Results against experimental GO.** K-12 has experimental GO on 3,328 of the
4,123 compared genes ([`results/ECOLI_wp/`](REFSEQ_GO/results/ECOLI_wp/analysis.yaml)).
Experimental annotation is incomplete, so "no experimental support" means
unconfirmed rather than wrong.

| | NCBI (WP_ records) | GOA electronic (IEA) |
|---|---:|---:|
| terms matching, or implied by, an experimental term | 70.8% | 74.2% |
| terms with no experimental support | 26.4% | 22.3% |
| experimental terms recovered, same or more specific | 16.1% | 41.5% |
| … MF / BP / CC | 23.5% / 14.8% / 6.6% | 49.9% / 30.8% / 43.8% |

This repeats the KT2440 pattern: similar precision, much lower recall for NCBI.
The comparison favours GOA, whose rules and mappings are partly built from these
same experimental annotations (IBA is excluded from "GOA electronic" for that
reason). On KT2440 the experimental set is small (57 genes) but gives the same
picture: 13.6% recall for NCBI against 45.6% for GOA electronic.

**BlastRules name well-studied proteins and give them no GO.** Only 53% of the
K-12 WP_ records carry any GO, against 68% for KT2440. The difference is
BlastRules: they name 771 K-12 proteins (19%), and only 13 of those (2%) carry
GO. Examples are diacylglycerol kinase (NBR011105), 5'-deoxynucleotidase
(NBR007780) and the As(III)-sensing ArsR regulator (NBR009015). BlastRules are
anchored on characterised proteins, so they win the naming for exactly the
best-studied genes, and winner-take-all then discards the GO the HMMs would have
given. In KT2440, BlastRules name 92 proteins, 22% with GO.

A clean case is EntE (P10378, `WP_000026812.1`), named by BlastRule NBR012093
with no GO. InterPro shows it also matches two equivalog HMMs with the same name,
NF008192 (residues 2–534) and TIGR02275 (3–527), both carrying GO:0008668 and
GO:0019290. GOA has GO:0008668 from five EXP and one IDA annotation. In a sample
of 60 BlastRule-named K-12 proteins without GO, 25 matched a GO-bearing
NCBIfam/TIGRFAM model (InterPro's matches; PGAP does not publish its own hit
lists).

## Third genome: *Synechocystis* PCC 6803

A cyanobacterium, so a third phylum. UniProt's reference proteome (UP000001425)
and RefSeq `GCF_000009725.1` are the same assembly, so this is a same-genome
comparison like KT2440. There are no reviews in this repo, so experimental GO
(209 genes) is the only ground truth.

```bash
uv run python projects/REFSEQ_GO/compare_refseq_goa.py \
  --accession GCF_000009725 --taxon 1111708 --proteome UP000001425 \
  --locus-regex 's(?:ml|[lms][lr])[0-9]{4}[a-z]?' --out-dir projects/REFSEQ_GO/results/SYNY3
```

**Joining needed a second key.** 345 UniProt entries carry only a submitter
gene name (e.g. two different entries named `bcp`) and no ordered locus name,
and almost no entries have a WP_ cross-reference. The script now joins such
entries by identical sequence to a RefSeq translation, which recovered 282 of
them; 63 have no identical RefSeq protein, which suggests different gene calls.
The live record (`RS_2026_01_07`, PGAP 6.10) is again a release ahead of
Datasets (`RS_2025_06_29`).

| *Synechocystis* (209 genes with experimental GO) | genes with GO | experimental terms recovered | terms supported by experimental GO |
|---|---:|---:|---:|
| NCBI actual | 1,837 | 9% | 53% |
| NCBI + family HMMs | 1,973 | 11% | 50% |
| NCBI + family + Pfam copies | 2,192 | 15% | 52% |
| GOA InterPro2GO only | 1,799 | 15% | 61% |
| GOA InterPro2GO + TreeGrafter + IBA | 2,080 | 28% | 62% |
| GOA electronic | 2,001 | 50% | 66% |

The gap is wider than in KT2440 or K-12. Partly this is because the
experimental set leans on location (255 of 658 rows are CC, mostly thylakoid
membrane), where NCBI assigns little. But NCBI also recovers only 10% of the
experimental MF terms, against 54% for GOA. Examples:

- **The naming rule again.** Gap2 (sll1342) is named by NF005641, an
  equivalog with no GO; it also matches TIGR01534, with the same name and
  GAPDH GO, which is discarded.
- **BlastRule names, no GO.** sll0418 (2-methyl-6-phytyl-1,4-hydroquinone
  methyltransferase, NBR012634) and sll1253 (A-adding tRNA
  nucleotidyltransferase, NBR015769) get specific names and no MF.
- **No naming model at all.** sll0554, ferredoxin:thioredoxin reductase, has no
  naming evidence and no GO; GOA gets the activity from EC2GO/Rhea2GO.
- **Specific name, general GO.** sll0228 is named N(1)-aminopropylagmatine
  ureohydrolase (BlastRule) but carries only "agmatinase activity"; GOA has the
  exact activity from EC2GO/Rhea2GO.
- **Lineage-specific biology.** The carboxysome shell proteins (sll1028–1031)
  lack "structural constituent of carboxysome shell" in NCBI, which GOA gets
  from InterPro2GO and UniRule.

**The genome record lags the WP_ records.** CcmL (sll1030) is named by
NF053795, which carries carboxysome GO, and its WP_ record (updated 2026-04-14)
has that GO; the January 2026 genome record does not. Across all proteins, the
genome record and the WP_ records agree on GO for 92.9% (Synechocystis) and
94.5% (KT2440), with the WP_ records generally the newer.

## Counterfactual: NCBI without winner-take-all

What would NCBI's GO look like if a protein kept the GO of every NCBI model it
matches, not only the naming model? `compare_refseq_goa.py --union-models`
adds, to NCBI's actual GO, the GO of every matched HMM in `hmm_PGAP.tsv`:

- `family`: NCBIfam and TIGRFAM family models;
- `all`: family models plus NCBI's copies of Pfam models.

Matches are InterPro's, from each UniProt entry's NCBIfam and Pfam
cross-references, because PGAP does not publish its hit lists. CDD/SPARCLE
architectures cannot be added: only the winning architecture is visible.

Scored with the corrected verdict split (see the next section), on KT2440:

| | genes with NCBI GO | wrong (REMOVE) | too general | core MF | core BP |
|---|---:|---:|---:|---:|---:|
| NCBI actual | 3,513 | 3.2% | 5.9% | 52% | 37% |
| + family HMMs (`family`) | 3,643 | 3.6% | 6.3% | 57% | 45% |
| + Pfam copies too (`all`) | 3,924 | 3.7% | 10.9% | 60% | 48% |

In *E. coli* K-12, experimental-term recall goes from 16% to 21% (`family`) and
23% (`all`). Results: `results/{PSEPK,ECOLI_wp}_union_{family,all}/`.

- **Adding family models is close to free.** Recall rises on both genomes with
  almost no change in wrong or too-general terms.
- **Pfam copies mostly add true but general terms.** Of the 661 Pfam-derived
  terms KT2440 reviewers judged, 35% were marked over-annotated, nearly all for
  being less specific than an accepted term ("catalytic activity",
  "oxidoreductase activity", "membrane"); only 4% were REMOVEd. The REMOVEd ones
  are real errors shared with InterPro2GO, e.g. arginine-tRNA ligase activity
  on glycyl-tRNA synthetase. (An earlier version of this page reported "38%
  rejected", lumping the two.)
- **It is not mainly CDD/SPARCLE.** With `family`, the KT2440 genes that gain
  terms were named by NCBIfam HMMs (199), architectures (183), TIGRFAM (110),
  or had no NCBI GO at all (130). In K-12, most were genes with no NCBI GO
  (496), largely BlastRule-named, or NCBIfam-named (378); architectures
  accounted for 23.
- **Most of the gap to GOA remains**; the next section shows where it comes
  from.

## Pipeline variants scored the same way

`analyze_refseq_goa.py` now scores every annotation set identically
(`pipeline_variants` in `analysis.yaml`), and splits the reviewer verdicts:

- **wrong**: REMOVE.
- **too general**: marked over-annotated, but an ancestor of a term the
  reviewer accepted. True, just less specific, and not an error.
- **over-annotated (other)**: the rest of MARK_AS_OVER_ANNOTATED.

GOA's combined rows (GO_REF:0000120) are credited to each pipeline in their
WITH/FROM, so pipeline subsets can be scored.

**KT2440** (956 reviewed genes, 57 with experimental GO):

| | genes with GO | correct | too general | wrong | core MF | core BP |
|---|---:|---:|---:|---:|---:|---:|
| NCBI actual | 3,513 | 68.6% | 5.9% | 3.2% | 52% | 37% |
| NCBI + family HMMs | 3,643 | 68.2% | 6.3% | 3.6% | 57% | 45% |
| NCBI + family + Pfam copies | 3,924 | 63.6% | 10.9% | 3.7% | 60% | 48% |
| GOA InterPro2GO only | 3,329 | 62.5% | 17.2% | 4.3% | 54% | 37% |
| GOA InterPro2GO + TreeGrafter + IBA | 3,646 | 66.6% | 12.9% | 5.1% | 64% | 51% |
| GOA electronic without ARBA | 3,837 | 69.0% | 11.3% | 4.8% | 80% | 66% |
| GOA electronic | 3,869 | 68.4% | 11.6% | 4.8% | 81% | 67% |
| NCBI ∪ InterPro2GO + TreeGrafter + IBA | 4,109 | 64.9% | 11.3% | 4.4% | 69% | 57% |

**E. coli K-12** (3,328 genes with experimental GO; only 83 reviewed genes, so
the review columns are noisy):

| | genes with GO | experimental terms recovered | terms supported by experimental GO |
|---|---:|---:|---:|
| NCBI actual | 2,193 | 16% | 71% |
| NCBI + family HMMs | 2,689 | 21% | 69% |
| GOA InterPro2GO only | 2,932 | 21% | 73% |
| GOA InterPro2GO + TreeGrafter + IBA | 3,328 | 47% | 76% |
| GOA electronic | 3,475 | 42% | 74% |

What this changes:

- **Wrong terms are rare on every side** (3–5% REMOVE). The earlier "12% vs
  21% rejected" was mostly true-but-general terms, concentrated in InterPro2GO
  (17% too general).
- **NCBI's coverage is about InterPro2GO's.** Core MF 52% vs 54%, core BP 37%
  vs 37%, at a lower too-general rate.
- **ARBA adds little.** Removing it moves core MF from 81% to 80%.
- **GOA's lead comes from enzyme mappings and rules.** Of 268 core terms that
  only GOA's other pipelines reach (beyond NCBI and InterPro2GO + TreeGrafter +
  IBA), the supplying pipelines are EC2GO (98), UniRule (95), Rhea2GO (71),
  UniPathway2GO (58), inter-ontology links (36) and ARBA (32); a term can have
  several. Examples: BetC choline-sulfatase activity (EC2GO), DavD
  glutarate-semialdehyde dehydrogenase (NADP+) (Rhea2GO), HisH glutaminase
  activity (EC2GO, Rhea2GO).
- **NCBI already has EC numbers it does not turn into GO.** 1,592 KT2440 CDS
  carry `/EC_number`, 148 of them with no GO molecular function. An ec2go step
  on NCBI's own EC numbers is the obvious next counterfactual.
- **In K-12, IBA is circular.** PAINT uses *E. coli* experimental annotations
  as evidence, so IBA's high experimental recall there is expected.

Examples of core functions NCBI misses and the family union recovers: RpoD
(named by NF004208, no DNA binding; TIGRFAM adds DNA binding and transcription
initiation), CbcX (named by a CDD architecture; TIGRFAM adds choline binding and
transport), DegP (named by NF008189; TIGRFAM adds serine-type endopeptidase
activity), FtsI (named by a BlastRule; NCBIfam adds penicillin binding).

## Where NCBI's prokaryotic GO can be downloaded

NCBI's GO for KT2440 is in two places: the CDS features of the RefSeq genome
record, and the per-assembly GAF on the FTP site (a release behind). It is not in
`gene2go`, the GO file most tools take from NCBI. That file is keyed by NCBI Gene
ID, and KT2440 has no live Gene records.

| Genome | Live NCBI Gene records | `gene2go` rows |
|---|---:|---:|
| *P. putida* KT2440 | 1 | 0 |
| *E. coli* K-12 MG1655 | 4,652 | 41,101 (3,863 genes) |
| *P. aeruginosa* PAO1 | 5,698 | 22,779 (3,890 genes) |
| *B. subtilis* 168 | 4,537 | **0** |

Counts are from `gene2go.gz` dated 2026-10-18.

**What "reference" means for GO.** The reference genomes' RefSeq records take
their annotation from an outside group, not from PGAP, and carry no GO
qualifiers at all (0 in `NC_000913.3` and `NC_002516.2`):

- MG1655: "annotation updates are derived from EcoCyc", from a collaboration
  of EcoCyc, the University of Wisconsin, UniProtKB/Swiss-Prot and NCBI.
- PAO1: "the Sept 08, 2010 version" of the PseudoCAP annotation from
  pseudomonas.com.

Their `gene2go` rows instead match the GO Consortium per-species files, which
UniProt generates (`ECOLI-uniprot`, `PSEAE-uniprot`, July 2026). Collapsed to
one row per protein, term and evidence code, these give 43,493 (*E. coli*) and
26,077 (PAO1) rows, against 41,101 and 22,779 in `gene2go`. The gap is about the
size expected from proteins without an NCBI Gene ID (3,863 vs 4,482 and 3,890
vs 4,388). So for reference genomes, `gene2go` carries UniProt-GOA's mix:
experimental, IBA and UniProt's electronic pipelines. For PAO1, PseudoCAP's own
curation is one contributor inside that file (2,066 of 32,020 rows,
`assigned_by=PseudoCAP`).

**NCBI Gene pages show the same data, under a misleading label.** The GO
section of a reference-genome Gene record matches the GO Consortium file
exactly: *dnaA* has 36 of 36 term–evidence pairs in common for *E. coli*
(GeneID 948217) and 11 of 11 for PAO1 (GeneID 878417). Each section carries one
attribution, "Provided by EcoCyc" or "Provided by PseudoCAP". For PAO1 *dnaA*,
none of the 11 rows were made by PseudoCAP (they are `assigned_by` GO_Central,
InterPro and UniProt), so the label names the organism's community resource,
not the source of the annotations. Only one gene per genome was checked.

`gene2go` has no source column, and its IEA rows have no PubMed ID (all 14,184
K-12 and 13,192 PAO1 IEA rows show `-`), so provenance cannot be read off it
directly.

**PGAP's GO does not reach Gene or `gene2go`, even where Gene records exist.**
"Reference genome" now means two sets. Since September 2024 it is the best
genome per species, about 23,700 prokaryotes (Datasets, 2026-10-18; the
[May 2025 collection](https://ncbiinsights.ncbi.nlm.nih.gov/2025/05/27/now-available-updated-bacterial-and-archaeal-reference-genome-collection/)
had 21,794), nearly all PGAP-annotated
([terminology change](https://ncbiinsights.ncbi.nlm.nih.gov/2024/09/25/updated-terminology-reference-genome/)).
The 15 "manually curated" references
([list](https://www.ncbi.nlm.nih.gov/refseq/about/prokaryotes/)) are the
submitter-annotated subset. Gene IDs go to reference genomes of species with at
least ten RefSeq assemblies, so PGAP genomes can have Gene records. The *P. putida*
species reference, NBRC 14164 (`GCF_000412675.1`, PGAP), has 5,573 live Gene
records, yet 0 `gene2go` rows and no GO on its Gene pages (checked for *dnaA*,
GeneID 45521526). `gene2go` and Gene's GO sections appear to carry GO Consortium
data only. Tools that take GO from NCBI through `gene2go` therefore never see
NCBI's prokaryotic pipeline annotation.

**Unexplained:** *B. subtilis* 168 has live Gene records, and the GO Consortium
has a `BACSU-uniprot` file with 21,806 rows for taxon 224308, but none reach
`gene2go`.

## History of GO–NCBI contact on prokaryotic GO

Reconstructed from email and calendar records (C. Mungall's mailbox) and the two
public NCBI Insights posts.

| Date | Event |
|---|---|
| Oct 2019 | Earth BioGenome Project annotation-standards committee. F. Thibaud-Nissen drafts first answers; CJM suggests recommending InterProScan, with InterPro2GO and phylogenetic GO, over BLAST-based transfer. |
| Feb 2022 | NSF workshop on the future of protein function annotation. F. Thibaud-Nissen (NCBI) presents RefSeq prokaryotic GO. |
| 2022-02-24 | NCBI Insights: [*Bacterial and archaeal genomes with GO terms in RefSeq*](https://ncbiinsights.ncbi.nlm.nih.gov/2022/02/24/gene-ontology-refseq/). GO comes from family models (Pfam via `pfam2go`, TIGRFAMs, NCBIFams, BlastRules) and covers 65M WP_ proteins. CDD architectures are named as future work. |
| 2022-02-25 | CJM raises the announcement on go-managers and asks how to compare the two pipelines on the same proteins (the katG example looked consistent). V. Wood notices that GO's published `pfam2go` dates from December 2020; the file had stalled on the GO side (go-site#1806) and is current again by 2022-04-29. A. Bridge confirms that `pfam2go` is derived from InterPro2GO, and knows of no UniProt–NCBI coordination. PDT proposes asking NCBI for one GO_REF per IEA method. |
| Mar–Apr 2022 | CJM and P. Thomas identify Françoise as the contact. On 2022-04-13 PDT writes to her about offering GAF downloads and GO_REFs for IEA methods. NCBI replies that it does not offer GAFs yet and asks about demand. |
| 2022-04-29 | Call "GO annotation on RefSeq proks" (GO: CJM, PDT; NCBI: Thibaud-Nissen, Haft, W. Li, J. Virothaisakun). |
| May 2022 | CJM finds that `hmm_PGAP.tsv` carries only 1 of 3 `pfam2go` terms for PF00539. NCBI finds an import bug that kept only one GO term per Pfam, fixes it in HMM release 9.0, and back-fills RefSeq proteins. NCBI states that GO is an attribute of HMMs, BlastRules and CDD architectures, propagated only to the proteins those models name, and that architecture GO is not yet propagated. |
| Jul 2022 | T. Murphy (RefSeq lead) asks GO for a recommended pipeline for eukaryotic RefSeq. CJM suggests reference-proteome mappings or InterProScan. PDT missed the email and it was picked up in May 2023. |
| May–Sep 2023 | Eukaryotic RefSeq builds its own GO pipeline, separate from PGAP: InterProScan ≥5.63 with InterPro2GO plus PANTHER/TreeGrafter GO (parsed from the XML output), anchored to NCBI GeneIDs and reduced to the most specific terms. PDT advises on the GAF columns: a separate reference per method, WITH/FROM `InterPro:IPR…` or `PANTHER:PTN…`. T. Murphy settles on `NCBIGene` in column 1 and `protein` in column 12. |
| Mar 2023 | NCBI starts propagating GO from CDD architectures. |
| 2023-05-10 | NCBI Insights: [*GO terms on 100M+ RefSeq prokaryotic protein records*](https://ncbiinsights.ncbi.nlm.nih.gov/2023/05/10/go-terms-100m-refseq-records), a 55% increase attributed to CDD architectures. |
| Aug 2025 | CJM asks NCBI for a stable link for PGAP HMM ids, Bioregistry prefix registration, and family→GO mappings, after GO obsoleted `GO:0042192`, which PGAP families used. Françoise has changed role; W. Klimke now leads prokaryotic RefSeq/PGAP. `hmm_PGAP.tsv` holds the HMM mappings only. No integrated dump covers all models (BlastRules, architectures), but NCBI offers a one-off dump. |
| Sep 2025 | CJM proposes to D. Haft that NCBIFam→GO mappings be checked before GO obsoletions, as InterPro2GO is. Klimke confirms per-assembly GAFs on the FTP site. B. subtilis 168, *E. coli* K-12 and the other community reference genomes lack GAFs, and the FTP refresh is backlogged. A. Marchler-Bauer explains that gene symbols come from only a few architectures, so many proteins have no symbol (go-site#2549 relaxes the GAF symbol requirement). CJM gives two use cases: easier community access to the GAFs, and systematic pipeline comparison. |
| Apr 2026 | While GO plans a breaking pipeline change, CJM's survey of downstream consumers (geneontology/go-db-users, private) finds that most tools take GO from NCBI, then EBI-GOA, then GO's own downloads. |
| 2026-10-18 | P. Thomas recirculates the NCBI Insights posts and suggests adding NCBI to GO's download instructions and renewing contact. This project starts. |

## Next steps

- [x] Per-review audit against the 956 PSEPK reviews (see
      [Level 3](#level-3-against-956-curated-reviews)).
- [ ] Send NCBI the model-level GO fixes marked *(model)* above, with the review
      evidence for each.
- [ ] Add to that list the ParAB gaps from the [worked case](#worked-case-the-parab-chromosome-partition-proteins):
      chromosome segregation on architecture 11445026; ATP hydrolysis activity and
      chromosome segregation on BlastRule NBR012933; CTPase activity for ParB
      models; and the "nuclease" wording of the COG1475 region note.
- [ ] Score a random sample of the 160 non-obsolete unassessed NCBI terms, so the
      NCBI-only error rate can be estimated rather than just shown by example.
- [ ] Recompute obsolete NCBI terms with their GO replacements, to separate
      version lag from real disagreement.
- [ ] Find out why *B. subtilis* 168 has no `gene2go` rows despite live Gene
      records.
- [ ] Ask NCBI why the FTP files and Datasets lag the live record by an
      annotation release.
- [x] Second genome: *E. coli* K-12 via WP_ records, scored against
      experimental GO.
- [x] A same-assembly genome from another phylum: *Synechocystis* PCC 6803.
- [ ] Take up NCBI's offer of a one-off dump of all GO-bearing models
      (BlastRules and architectures as well as HMMs). Without it, architecture
      GO can only be reverse-engineered from per-genome GAFs.
- [ ] Draft text for GO's download documentation (go-site) that points to the
      NCBI per-assembly GAFs and states their scope: IEA only, one source per
      protein, no GAF for the curated reference genomes, possible GO-version lag.
- [ ] Topics for a renewed NCBI conversation: GAFs for the curated reference
      genomes; an obsoletion-notification route for NCBI model→GO mappings; a
      GO_REF per NCBI source type instead of a single PMID; and SPARCLE GO
      provenance.
