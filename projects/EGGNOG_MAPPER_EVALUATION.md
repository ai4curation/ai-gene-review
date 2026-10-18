---
title: "eggNOG-mapper Evaluation"
collections: [FUNCTION_PREDICTION, HOMOLOGY_PROPAGATION]
maturity: IN_PROGRESS
tags: [EVALUATION, PIPELINE]
last_reviewed: 2026-10-18
# Bare symbols here span many species (ddb-1, Hspa8, SecA ...); prose
# auto-linking would mis-target, so keep it off.
autolink_gene_symbols: false
manifest:
  artifacts:
    - href: https://claude.ai/artifact/5Le1BXcjqJRPs26BDPuuBb
      title: Project brief
---

# eggNOG-mapper Evaluation

**Bottom line:** [eggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper)
is the most widely used tool for annotating new genomes. It finds a protein's
orthologs in eggNOG and copies across **the union of every ortholog's GO
terms**. We ran it (v2.1.13, database 5.0.2, default settings) on 520 proteins
sampled from completed AI Gene Review reviews and compared each predicted
most-specific term with what the review concluded. Run normally, 40% of
predicted leaf terms match a supported claim exactly and two thirds of
reviewed core-function terms are recovered. That run is flattered, because
eggNOG already holds GOA annotations for most of these proteins and returns
them. To simulate a newly sequenced organism we hid the query's own species.
Exact matches then fell to 33% of leaves and core-function recall to 44%. A
further 44% of leaves were related to nothing in the review. In a manual check
of 45 of those unrelated terms, about half were wrong and one in five was a
correct, informative addition. The errors are characteristic: process terms
that came from an ortholog's mutant phenotype, terms that cannot apply in the
query's lineage (eye development on a worm protein), activities that belong to
a paralog or a complex partner, and source annotations that were wrong.
Molecular-function terms most often match the review exactly. But in a
24-claim sample per aspect of terms going beyond what the review supports, two
in three MF terms were wrong, against half or fewer for process and location
terms
([failure modes by ontology](EGGNOG_MAPPER_EVALUATION/failure-modes.md)).

On three non-model genomes the profile depends on the lineage
([deep dive](EGGNOG_MAPPER_EVALUATION/deep-dive.md)):
- ***P. putida* and poplar:** few terms per protein, mostly matching GOA's
  electronic annotation.
- **Horse:** absent from eggNOG and annotated from all of Metazoa, so each
  protein gets a long list. That list holds real mammalian knowledge that
  horse GOA lacks, mixed with mouse-phenotype errors.

Restricting transfer to a narrow clade raises precision but leaves most
proteins with no GO at all.

We also found and fixed an emapper bug: `--excluded_taxa` never excludes the
named taxon itself (see [Methods](#leave-species-out)).

## Why evaluate it

eggNOG-mapper output enters annotation pipelines, MAGs and comparative
studies, and it is often treated as roughly equivalent to curated orthology
transfer. Unlike [PAINT/IBA](IBA_REVIEW.md) it involves no curator, and unlike
[TreeGrafter](TREEGRAFTER.md) it does not place the query on a tree and take
one ancestral node's terms. It takes everything any ortholog in the chosen
orthologous group carries. Its GO output never appears in GOA, so the corpus
has no existing rows to tally: we ran the tool ourselves.

## Methods

### Cohort

[`build_cohort.py`](EGGNOG_MAPPER_EVALUATION/build_cohort.py) takes reviews in
which every live `existing_annotations` row has a non-PENDING action (at least
three rows) and the cached UniProt record has a sequence. It samples 40 per
organism, with a fixed seed, from human, mouse, rat, zebrafish, fly, worm,
budding and fission yeast, Arabidopsis, Dictyostelium, *E. coli* and
*P. putida* KT2440, plus 40 from all remaining organisms pooled (28 further
organism directories, from phages to sea urchin). That gives 520 proteins; DIAMOND found a
seed ortholog for 515
([`cohort.yaml`](EGGNOG_MAPPER_EVALUATION/cohort.yaml)).

### Running emapper

The emapper annotation database (`eggnog.db`) is a 41 GB SQLite file. That is
more than the disk where this was run, so
[`zchunk_build_http.py`](EGGNOG_MAPPER_EVALUATION/scripts/zchunk_build_http.py)
streamed it into a store of independently compressed 256 KiB chunks (6.5 GB).
[`run_emapper.py`](EGGNOG_MAPPER_EVALUATION/scripts/run_emapper.py) serves that
store to SQLite through a read-only VFS. The bytes SQLite sees are identical to
the original; the store's length matched the page count in the SQLite header
exactly. emapper's own code is unchanged apart from the connection and the
taxon fix below. The seed search used emapper defaults (DIAMOND sensitive mode
with iteration, e-value 0.001) against `eggnog_proteins.dmnd`, and GO transfer
used the default `--go_evidence non-electronic`. The full pipeline is
[`scripts/run_all.sh`](EGGNOG_MAPPER_EVALUATION/scripts/run_all.sh).

### Leave-species-out

Three annotation runs were made from the same seed orthologs:

| Run | Orthologs used for transfer |
|---|---|
| `default` | all (what a user annotating these proteins gets) |
| `species_excluded` | all except those from the query's own species (`--excluded_taxa <species>`); simulates a new genome |
| `species_excluded_experimental` | as above, and only experimentally supported GO terms (`--go_evidence experimental`), removing ISS/ISO/IBA terms that may themselves descend from the query |

`--excluded_taxa` has a bug in emapper 2.1.13. `normalize_target_taxa` expands
each taxid to its NCBI descendants *only*. So `--excluded_taxa 9606` excludes
Neanderthal and Denisovan records but keeps human ones, and
`--excluded_taxa 4932` keeps every *S. cerevisiae* record filed at 4932.
Species whose eggNOG records sit at a strain-level taxid, such as *E. coli*
K-12 (511145), were excluded correctly, which hid the problem. Our first
exclusion run left human, mouse, rat, yeast, fission yeast and Dictyostelium
outputs byte-identical to the default run. The wrapper now adds the taxid
itself, which is what the help text ("taxa and all its descendants")
describes. The same bug affects `--target_taxa`. The species-level taxid of
each query comes from eggNOG's own taxonomy
([`cohort_species_taxa.yaml`](EGGNOG_MAPPER_EVALUATION/cohort_species_taxa.yaml)).
One phage protein's taxon is missing from that taxonomy, so the seed
ortholog's own taxon was excluded instead.

### Scoring

[`score_emapper.py`](EGGNOG_MAPPER_EVALUATION/score_emapper.py) reduces each
prediction set to **leaf terms**, then compares each leaf with the review
through the GO is_a/part_of closure (GO release 2026-03-25).

emapper's lists were propagated with a 2019–2020 GO, so leaf reduction uses
the union of ancestry from the 2019-07-01, 2020-12-08 and current releases.
With today's ontology alone, grouping classes that have since lost their
subclasses ("heterocyclic compound binding", "multi-organism reproductive
process") surface as 2,500 spurious leaves. Obsolete leaf terms without a
replacement are dropped (447 in the default run).

The review side has three sets:
- **Supported:** ACCEPT, KEEP_AS_NON_CORE and NEW rows, MODIFY replacements,
  and all `core_functions` terms.
- **Downgraded:** MARK_AS_OVER_ANNOTATED, TOO_GENERAL and UNDECIDED rows, and
  the original MODIFY term.
- **Rejected:** REMOVE rows and upheld NOT annotations. Removals of
  placeholders (aspect roots, `binding`, `protein binding`) are not counted,
  since they mean "uninformative" rather than "false".

| Category | Leaf term is… |
|---|---|
| EXACT | a supported term |
| REJECTED | a rejected term or one of its descendants |
| BROADER | an ancestor of a supported term (true, less precise) |
| NARROWER | a descendant of a supported term (more specific than the review; unverified) |
| DOWNGRADED | related to a downgraded term |
| UNRELATED | related to nothing in the review |

Core-function recall counts a `core_functions` term as recovered when it lies
in the prediction's closure.

Because the reviews start from GOA, UNRELATED means "absent from current GOA
in any related form". It is not the same as wrong, which is why it was sampled
for manual review.

## Results

### Automatic comparison

| Run | Proteins with GO | Leaf terms | EXACT % | BROADER % | NARROWER % | DOWNGRADED % | REJECTED % | UNRELATED % | Core recall % |
|---|---|---|---|---|---|---|---|---|---|
| default | 449 | 9,050 | 39.9 | 1.7 | 11.4 | 6.5 | 1.7 | 38.7 | 66.2 (1583/2391) |
| species_excluded | 332 | 6,674 | 33.1 | 2.2 | 12.4 | 6.4 | 1.8 | 44.2 | 43.5 (1040/2391) |
| species_excluded_experimental | 288 | 4,941 | 31.6 | 2.4 | 11.4 | 6.3 | 1.9 | 46.5 | 32.1 (767/2391) |

The 515 proteins with a seed ortholog received a median of 10 leaf terms each
(up to 243). Large sets come from big, heavily annotated mammalian orthologous
groups, so pooled percentages are weighted towards them. Per protein, the
median share of leaves that were EXACT was 0.50 in the default run and 0.38
with the own species excluded.

By aspect, in the species-excluded run (% of leaves):

| Aspect | Leaves | EXACT | BROADER | NARROWER | DOWNGRADED | REJECTED | UNRELATED |
|---|---|---|---|---|---|---|---|
| MF | 1,095 | 50.9 | 2.6 | 4.6 | 12.5 | 2.6 | 26.9 |
| BP | 4,309 | 25.5 | 2.2 | 10.8 | 5.6 | 1.6 | 54.3 |
| CC | 1,270 | 43.3 | 2.1 | 24.5 | 3.8 | 1.6 | 24.7 |

Biological-process terms are two thirds of all leaves and over half of them
are UNRELATED. Molecular-function leaves match exactly twice as often. MF
leaves are also the most often DOWNGRADED, mostly protein-binding-type terms
(identical protein binding, protein kinase binding) that reviews mark as
over-annotations or replace with more specific terms.

Coverage depends on the query's lineage having other annotated species in
eggNOG (proteins with GO / core recall):

| Stratum | default | species_excluded | + experimental only |
|---|---|---|---|
| human | 37 / 0.63 | 35 / 0.52 | 28 / 0.31 |
| mouse | 39 / 0.81 | 38 / 0.73 | 37 / 0.60 |
| rat | 40 / 0.81 | 40 / 0.78 | 39 / 0.57 |
| zebrafish | 34 / 0.72 | 33 / 0.63 | 32 / 0.52 |
| fly | 40 / 0.79 | 32 / 0.47 | 31 / 0.36 |
| worm | 36 / 0.73 | 29 / 0.52 | 29 / 0.45 |
| budding yeast | 38 / 0.74 | 28 / 0.48 | 19 / 0.26 |
| fission yeast | 36 / 0.66 | 30 / 0.45 | 30 / 0.39 |
| Arabidopsis | 38 / 0.50 | 17 / 0.14 | 12 / 0.11 |
| Dictyostelium | 36 / 0.69 | 1 / 0.01 | 1 / 0.01 |
| *E. coli* | 37 / 0.57 | 12 / 0.12 | 1 / 0.02 |
| *P. putida* | 20 / 0.38 | 19 / 0.37 | 16 / 0.26 |
| other species | 18 / 0.27 | 18 / 0.26 | 13 / 0.20 |

- **Mammals barely notice losing their own species.** Mouse and rat recall
  stays high because their orthologs carry each other's terms, many of them
  ISO/ISS transfers. The drop when only experimental evidence is allowed
  (rat 0.78 to 0.57) is the measure of that circularity.
- **Dictyostelium and *E. coli* collapse.** Their annotation in eggNOG comes
  almost entirely from themselves: no other amoebozoan has GO annotations, and
  experimental annotation of other gammaproteobacteria is sparse.
- **Arabidopsis falls from 0.50 to 0.14.** For a newly sequenced plant,
  bacterium or protist, the leave-species-out numbers are the ones that apply.
- ***P. putida* barely changes.** Even the default run gave GO terms to only
  20 of its 40 proteins, so little of its coverage came from its own records.

### Manual adjudication

80 leaves from the species-excluded run were drawn with a fixed seed: 40
UNRELATED, 20 REJECTED and 20 NARROWER, at most one per protein
([`adjudication/`](EGGNOG_MAPPER_EVALUATION/adjudication/draw_sample.py)).
AI reviewers judged each against the gene's review, UniProt record and notes,
using the COR/LSP/UNC/PLI/NPI/REP scheme of de Crécy-Lagard et al. 2025
(PMID:40703034). Eight claims drawn as REJECTED moved category once
placeholder removals stopped counting
([`summary.yaml`](EGGNOG_MAPPER_EVALUATION/adjudication/summary.yaml)), so
counts below use the current category:

| Category | n | COR | LSP | UNC | Wrong (NPI/PLI/REP) |
|---|---|---|---|---|---|
| UNRELATED | 45 | 9 | 7 | 7 | 22 |
| NARROWER | 20 | 9 | 0 | 6 | 5 |
| REJECTED | 12 | 1 | 0 | 3 | 8 |
| BROADER / DOWNGRADED | 3 | 1 | 1 | 0 | 1 |

- **UNRELATED: about half are wrong, and one in five is a real gap.**
  Correct additions included macroautophagy for the fly VMP1 ortholog Tango5,
  site of double-strand break for mouse Trp53, xenobiotic metabolism for
  Ephx1, and peptidyl-prolyl isomerization for SurA.
- **NARROWER: under half are confirmed.** For example, mRNA splicing via
  spliceosome for CBP80 and TGN membrane for worm clic-1. Most of the rest are
  plausible compartments with no evidence either way.
- **REJECTED: the curators were usually right.** In 8 of 12 genuine
  rejections the transferred term was wrong again. In one case, Golgi
  apparatus for zebrafish procollagen col1a1a, the reviewer judged the
  removal too strict.

Error types among the 36 wrong calls:

| Error type | n | Examples |
|---|---|---|
| CURATION_MISTAKE (source annotation wrong) | 11 | insulin receptor activity on a lipocalin; guanyl-nucleotide exchange factor activity on KRAS; DNA recombination on Rbpj, a leftover of its old name |
| TAXON_CONSTRAINT_VIOLATION | 7 | mushroom body development and camera-type-eye development on worm proteins; Candida phenotypic switching on budding-yeast HST2; Cul7-RING complex in yeast |
| MULTIPLE_FUNCTIONS (phenotype-derived process) | 6 | exit from mitosis on SKP1; feeding behaviour on UCK2; filamentous growth on HSC82 |
| PARALOG_OVERANNOTATION | 4 | RSC complex on SWI3 (yeast uses the paralog Rsc8); aconitate hydratase on an AcnD-family enzyme; ANG localization on Ang2 |
| DOMAIN_ARCHITECTURE_MISMATCH | 2 | ABC-type transporter on the SecA motor ATPase; protein-transporting ATPase on the TPR receptor TOMM70 |
| COMPLEX_ACTIVITY_TRANSFER | 1 | damaged DNA binding (a DDB2 function) on worm ddb-1 |
| others | 5 | frequency bias, in vitro-only autophosphorylation, default cytosol, pathway target mistaken for participant |

The pattern follows from the method. emapper takes the union of everything
any ortholog in the group carries, so one ortholog's mutant phenotype, one
lineage's anatomy, or one database's mistaken row becomes a prediction for
every member. Transfer at a deep level (Metazoa, Eukaryota) adds terms that
belong to one paralog or one complex partner. Single wrong rows are amplified
rather than outvoted, because the output keeps no ortholog-support threshold.

### Failure modes by ontology

A second round of 72 claims, 24 per aspect, was drawn to compare the three
ontologies like for like. Of each aspect's 24 claims, 16 MF, 12 BP and 10 CC
were wrong. Each ontology fails in its own way:

- **MF: the molecule differs.**
  - Domain missing: ABC transporter on SecA.
  - Non-catalytic subunit: phosphatase activity on calcineurin B.
  - Sister subfamily: glutathione transferase on *S. aureus* FosB.
  - Pseudoenzyme: protease inhibitor on HSP47.
- **BP: the context differs.**
  - Anatomy the target lacks: nail development on a fly protein; telomerase
    on fly Mre11.
  - Phenotypes read as processes: negative regulation of locomotion on fly
    dunce.
- **CC: the protein's own sorting differs.**
  - Missing targeting signals: peroxisomal matrix on fly Idh.
  - Generic defaults: nucleus on a mitochondrial tRNA synthetase.
  - Structures absent in the lineage: polytene chromosome puff on mouse
    Ccnt1.

Across all 152 adjudicated claims, 23 of the wrong calls copied a mistaken
source annotation. The full catalog, with examples and rationale for every
wrong call, is on the
[failure-modes page](EGGNOG_MAPPER_EVALUATION/failure-modes.md).

### Narrowing the taxonomic scope

emapper's default `auto` scope transfers at broad clades: Metazoa, Fungi,
Streptophyta, Gammaproteobacteria. The pre-configured `--tax_scope all_narrow`
list reaches Mammalia, Brassicales and similar clades. Re-running the
species-excluded cohort with it:

| Run | Proteins with GO | Leaf terms | EXACT % | REJECTED % | UNRELATED % | Core recall |
|---|---|---|---|---|---|---|
| species_excluded (default scope) | 332 | 6,674 | 33.1 | 1.8 | 44.2 | 43.5% |
| species_excluded_narrow | 92 | 1,723 | 51.7 | 3.9 | 27.2 | 11.8% |

The leaves that remain match better, but three quarters of the proteins lose
all GO. The narrowest clade around the seed usually has no annotated member,
and nearly all that survive are rat and mouse proteins borrowing from each
other. Neither setting gets a broad scope's coverage without its errors.

### Non-model genomes

The [deep dive](EGGNOG_MAPPER_EVALUATION/deep-dive.md) ran every completed
review for *P. putida* KT2440 (850), horse (30), poplar (113) and pennycress
(4). eggNOG holds essentially no GO for these organisms, so the default run is
already independent.

| Genome | Proteins with GO | Median leaves | EXACT % | UNRELATED % | Core recall | Manual check: correct / wrong |
|---|---|---|---|---|---|---|
| *P. putida* | 484 / 850 | 4 | 54.9 | 27.0 | 0.41 | 8 / 14 of 24 |
| Horse | 29 / 30 | 18 | 12.5 | 70.0 | 0.69 | 7 / 5 of 16 |
| Poplar | 84 / 113 | 4 | 26.8 | 44.6 | 0.35 | 4 / 11 of 16 |
| Pennycress | 4 / 4 | 2 | 25.0 | 50.0 | 0.27 | 1 / 4 of 9 |

The characteristic errors differ by lineage:
- ***P. putida*:** *E. coli* phenotypes and paralog pooling (GABA shunt on
  DavD).
- **Horse:** mouse knockout phenotypes.
- **Poplar:** *Arabidopsis* chloroplast proteomics and paralog merges.

For genomes already in UniProt, emapper recovered fewer reviewed core
functions than GOA already held, and added a core term GOA lacked for about
one *P. putida* protein in ten.

## Caveats

- **The reference is the AI reviews, not ground truth.** EXACT and REJECTED
  inherit any errors in those reviews. The manual samples are small (152
  claims on the main cohort, 65 on the deep dive) and were judged by AI
  reviewers, not curators.
- **UNRELATED is not "wrong".** Reviews cover GOA, so a correct term GOA lacks
  lands here. The adjudication gives the rate: roughly 20% correct.
- **Transfer is not independent of the reviewed annotations.** Even with the
  own species excluded, orthologs' terms can be ISO/ISS copies of the query's.
  The experimental-only run bounds this.
- **Ontology versions differ.** eggNOG 5.0.2 is from 2020. Leaf reduction
  accounts for that, but a few correct-then terms may now be obsolete or
  moved.
- **Only GO is scored.** emapper also reports KEGG KO, EC, CAZy, BiGG, PFAM
  and preferred names, which are not evaluated here.

## Files

| File | Contents |
|---|---|
| [`cohort.yaml`](EGGNOG_MAPPER_EVALUATION/cohort.yaml), `cohort.fasta` | the 520 proteins and their sequences |
| `runs/<run>/<run>.emapper.annotations` | raw emapper output for each run |
| `results/<run>_leaf_scores.tsv` | one row per predicted leaf, with category |
| `results/<run>_protein.tsv` | per-protein counts, core recall and missed core terms |
| [`results/summary.yaml`](EGGNOG_MAPPER_EVALUATION/results/summary.yaml) | all aggregate tables |
| `adjudication/batch_*.yaml`, `adjudication/round2_batch_*.yaml` | the 80 + 72 adjudicated claims with rationale |
| [`adjudication/summary.yaml`](EGGNOG_MAPPER_EVALUATION/adjudication/summary.yaml) | adjudication tallies, overall and by aspect |
| [`adjudication/failure_modes.yaml`](EGGNOG_MAPPER_EVALUATION/adjudication/failure_modes.yaml) | every wrong call, by aspect and error type |
| [`failure-modes.md`](EGGNOG_MAPPER_EVALUATION/failure-modes.md) | failure modes by ontology, with examples |
| [`deep-dive.md`](EGGNOG_MAPPER_EVALUATION/deep-dive.md), `deep_dive/` | non-model genome cohort, runs, results and adjudication |

To reproduce: `projects/EGGNOG_MAPPER_EVALUATION/scripts/run_all.sh WORK_DIR`
(about 17 GB of disk and two hours, mostly the DIAMOND search), then
`uv run python projects/EGGNOG_MAPPER_EVALUATION/score_emapper.py` and
`uv run python projects/EGGNOG_MAPPER_EVALUATION/adjudication/summarize.py`.

## Next steps

- Report the `--excluded_taxa`/`--target_taxa` bug upstream.
- Test `--target_orthologs one2one`, and an intermediate scope list (for
  example Vertebrata or eudicots) between `auto` and `all_narrow`.
- Score the KEGG KO and EC outputs.
- Feed the correct UNRELATED terms back to the gene reviews as candidate
  `NEW` annotations, after a curator check.
