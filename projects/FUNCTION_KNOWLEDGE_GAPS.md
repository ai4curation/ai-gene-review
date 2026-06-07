# Function Knowledge Gaps

What does biology genuinely *not* know about how a gene works — and how do we state it
rigorously enough that someone could close it?

This project builds a curated, literature-grounded register of **function knowledge gaps**:
specific, defensible statements of what is unknown about a gene product's molecular function,
mechanism, partners, or biological role. It is the inverse of the rest of this repository.
Everywhere else we adjudicate what *is* known; here we adjudicate, with the same evidentiary
discipline, what is *not*.

The framing is deliberately ambitious. If a foundation set out to systematically eliminate the
conserved "unknome," the first deliverable would not be more experiments — it would be an honest
map of where the real gaps are, sharp enough to fund. That map is the goal.

## Why this matters: the unknome

Decades into the genomic era, a large fraction of even well-studied proteomes remains
functionally dark:

- ~20% of proteins in well-studied model organisms still lack any informative description of
  their biological role, and many of these are conserved from yeast to human — implying
  fundamental, not peripheral, functions (Wood et al. 2019, *Open Biology*, "Hidden in plain
  sight", PMID:30938578, [DOI](https://doi.org/10.1098/rsob.180241)).
- The Unknome database, which ranks proteins by an evidence-weighted "knownness" score
  (manual annotation = 0.9, electronic = 0.0; "unknown" = score ≤ 1.0), found 23% of human
  protein clusters still below that threshold — down from 43% a decade earlier, i.e. slow
  progress. RNAi screening of 260 conserved-unknown *Drosophila* genes found 62 essential for
  viability and 59 with measurable phenotypes — the dark set is dense with real biology
  (Rocha, Freeman et al. 2023, *PLOS Biology*, PMID:37552676,
  [DOI](https://doi.org/10.1371/journal.pbio.3002222)).

Genes stay dark largely for sociological reasons — research concentrates on what is already
famous (the streetlight effect / Matthew effect; Stoeger et al. 2018, *PLOS Biology*,
PMID:30226837; Edwards et al. 2011, *Nature*, "Too many roads not taken", PMID:21307913). The
same neglected set is over-represented among unsolved Mendelian disease, unannotated GWAS
peaks, and the druggable-but-unexplored proteome (the NIH IDG program; Oprea et al. 2018,
*Nat Rev Drug Discov*, PMID:29472638; Kustatscher et al. 2022, *Nat Methods*, "Understudied
proteins", PMID:35534633). Closing function gaps is the denominator problem under all of these.

## Core principle: a knowledge gap is a curated judgment, not a metric

The central methodological commitment of this project: **a knowledge gap is determined by
reading the primary literature and exercising judgment, not by a pattern in the annotations.**

We tested the alternative and it failed instructively. A score that flags genes with no
specific molecular function (à la Unknome, but using our adjudicated `core_functions`) marks
~14% of our reviewed genes as "MF-dark" — reassuringly close to Wood's ~20% and Unknome's 23%.
But when the conserved subset of those was inspected, "no molecular function" decomposed into
four completely different things:

| What the score called a "gap" | Share | What it actually is | Owner |
|---|---|---|---|
| Structural/accessory subunits (TOM, TRAPP, ESCRT, V-ATPase…) | ~64% | Function *is* "be part of the machine"; the GO MF aspect can't express it | **Ontology** |
| Function-kind known, MF term simply not filled (e.g. SOX9) | ~14% | Curation incompleteness | **Curation** |
| Stub / incomplete reviews (`TODO` descriptions) | ~3% | Data hygiene | — |
| Genuinely unknown mechanism (CFAP300, tam10, P3R3URF…) | ~18% | The true unknome | **Experiment** |

(Snapshot over ~2,100 reviewed genes; proportions are triage-grade, not curated.) A heavily
annotated gene can hide a gaping mechanistic hole; a sparsely annotated one can be perfectly
understood and merely under-curated. **Only reading tells them apart.** The metric is therefore
demoted to a back-of-house triage aid that produces a *read-list*, and never appears in the
product.

## A taxonomy of function knowledge gaps

Two axes. First, *what kind of ignorance* (this determines who can fix it):

1. **Biology gap** — nobody knows. Resolved by experiments. *This is the unknome and the
   project's primary target.*
2. **Curation gap** — the knowledge exists in the literature but is not yet annotated, or is
   annotated too generically. Resolved by curation (much of it in-house).
3. **Ontology gap** — the knowledge exists but no GO term can express it (e.g. "structural
   subunit of complex X", or a novel activity). Resolved by ontology development;
   tracked via `proposed_new_terms`.

Most real entries are a *blend* (CFAP300 below is biology-dominant with an ontology shadow),
and naming the blend is the actionable part.

Second, *which GO aspect is dark* — most "dark" genes are not uniformly dark:

- **MF-dark** — process/location known, molecular mechanism unknown (the most common and most
  insidious: rich BP/CC make the gene *look* known). The `protein binding` smell lives here.
- **BP-dark** — an activity is known but not what it is *for* (common in microbial/plant
  metabolism).
- **CC-dark** — function known, but where/when unknown.
- **Wholly dark** — only root terms / IEA / `protein binding` survive review (the deep unknome).

## The unit of work: anatomy of a gap entry

Each gap is a small, defensible scholarly object. Required elements:

- **Gap statement** — the specific unknown, stated precisely. Not "role unclear" but
  "the direct substrate / the catalytic activity / the essential partner is undetermined."
- **Boundary of knowledge** — what *is* established, so the gap is sharply delimited.
- **Provenance for the gap itself** — evidence that the unknown is real and not merely
  uncurated. The gold standard is the field's own admissions: primary-literature hedges
  ("remains to be determined", "the precise role is unknown"), "domain of unknown function"
  names, and a literature *trajectory* that confirms-but-never-mechanizes. Cited with the same
  `[PMID:xxxx "supporting text"]` discipline this repo uses for positive claims.
- **Type judgment** — biology / curation / ontology (or blend), per the taxonomy.
- **Significance** — why closing it matters.
- **What would resolve it** — the experiment, ontology term, or curation action.

This is strictly more than the existing `suggested_questions` field (which asks the right things
but cites nothing): the added value is the **adjudicated boundary plus provenance for the
unknown**.

## Worked example: the CFAP300 molecular-function gap

CFAP300 (formerly C11orf70) is a dynein axonemal assembly factor; loss-of-function causes
primary ciliary dyskinesia (PCD). It is in the KB (`genes/human/CFAP300/`) and is an ideal
exemplar: clear biomedical importance, a clearly established *role*, and a sharp, durable
*mechanistic* silence.

**Boundary (what is firmly known):**
- LOF causes PCD with *combined* outer + inner dynein arm (ODA+IDA) loss; CFAP300 is required
  for cytoplasmic preassembly of axonemal dyneins and their IFT-dependent delivery into the
  axoneme (Höben et al. 2018, *AJHG*, PMID:29727693, [DOI](https://doi.org/10.1016/j.ajhg.2018.03.025);
  Fassad et al. 2018, *AJHG*, PMID:29727692, [DOI](https://doi.org/10.1016/j.ajhg.2018.03.024)).
- Localizes mainly to cytoplasm, moves into cilia by IFT, and interacts with the preassembly
  factor DNAAF2 (Höben 2018).
- Re-confirmed in 2025: LOF → no CFAP300 protein → total ODA+IDA loss (Demchenko et al. 2025,
  *IJMS*, PMID:40806783, [DOI](https://doi.org/10.3390/ijms26157655)).

**Gap statement:** *The biochemical activity of CFAP300 is unknown.* It is unresolved whether
it acts as a chaperone/co-chaperone, a scaffold, or an adaptor; what its client/substrate is;
and whether it acts at one common step upstream of both arm types or in parallel ODA- and
IDA-specific steps.

**Provenance that the gap is real (the judgment):**
1. Both founding papers describe the gene as *"uncharacterized"* and frame the mechanism as a
   **hypothesis** ("supporting our hypothesis that C11orf70 is a preassembly factor") — they
   establish *requirement* and *localization*, never a biochemical activity (PMID:29727692,
   PMID:29727693).
2. Its sole domain is **DUF4498 — a "domain of unknown function"**
   (`genes/human/CFAP300/CFAP300-deep-research-falcon.md`).
3. **The trajectory is the strongest evidence:** seven years and many cohorts on (Polish 2019
   PMID:30916986; Cypriot 2021 PMID:33715250; Russian 2024 PMID:39180133; ALI-culture 2025
   PMID:40806783), every follow-up is *diagnostic* — confirming loss — not *mechanistic*. A
   durable mechanistic silence despite clear motivation is the signature of a genuine gap, and
   reading the arc of the literature is the only way to see it.

**Type judgment:** biology gap (dominant) with an ontology shadow — even "a dynein-preassembly
factor" has no adequate GO MF term, which is why the gene reads as MF-dark.

**Significance:** this is the assembly step whose failure removes *all* axonemal dynein motors —
mechanistically central to motile ciliopathy.

**What would resolve it:** proximity/affinity proteomics of the CFAP300–DNAAF2 module;
in vitro reconstitution of dynein assembly intermediates; structural characterization of
DUF4498.

## Methodology

For each candidate gene:

1. **Deep literature search** — use cached publications, the gene's `-deep-research-*.md`,
   PubMed, and full text where available. Read primarily for the *boundary* and for the field's
   *own statements of ignorance*.
2. **Harvest ignorance signals** — author hedges ("remains unknown / unclear / to be
   determined"), DUF / "uncharacterized" / hypothetical-protein naming, orphan-activity vs
   orphan-gene framing, and the diagnostic-not-mechanistic trajectory.
3. **Judge the type** — separate biology gaps from curation gaps from ontology gaps. This is
   the irreducible human/curatorial step.
4. **Write the gap entry** with full provenance.
5. **Route it** — experiment (suggested_experiments), ontology (proposed_new_terms), or
   curation (a normal review action).

Selection of *which genes to read* is curatorial, in the spirit of PomBase's "priority
unstudied genes" determination (Wood 2019) — informed, but not decided, by the triage
read-list.

## Relation to existing KB machinery

The building blocks already exist and are reused, not replaced:

| Signal | Existing field | Gap role |
|---|---|---|
| Open questions | `suggested_questions` | Seed for biology-gap statements (to be elevated with provenance) |
| Proposed experiments | `suggested_experiments` | The "what would resolve it" |
| Missing GO terms | `proposed_new_terms` | Ontology-gap entries |
| Unresolvable annotation | `action: UNDECIDED` | Often a curation gap (esp. literature inaccessible) |
| `protein binding` avoidance rule | curation guideline | Flags MF-mechanism gaps |

**Schema direction (deferred):** the cleanest long-term home would elevate `suggested_questions`
into a provenance-bearing `knowledge_gaps` structure (gap statement + boundary + `supported_by`
quotes + type) so gaps become first-class and queryable. We are *not* committing to a schema
change here; this project first proves the unit and the method on curated examples.

## Prioritization (curatorial, not computed)

When choosing what to read next, weight toward gaps that are both high-value and tractable:

- **Conservation depth** — LECA-deep conservation implies fundamental function (Wood filter).
- **Disease / GWAS / IDG overlap** — for human genes; the funder hook. (Disease-mechanism
  prioritization can be handed to / shared with Monarch's dismech.)
- **A coevolution handle** — phylogenetic-profile or co-expression clustering with a *known*
  module gives instant guilt-by-association and a ready hypothesis.
- **Microproteins / smORFs / non-canonical ORFs** — a deliberately included frontier where the
  gap is "we did not even know there was a player" (e.g. P3R3URF).

## Seed read-list (triage candidates — to be read, not yet curated)

From the conserved-MF-dark triage, after stripping structural-subunit and curation-completeness
false positives. These are *candidates for deep reading*; only CFAP300 above is a worked entry.

| Gene | Org | Why interesting |
|---|---|---|
| CFAP300 | human | **Worked exemplar.** Dynein preassembly; mechanism unknown; DUF4498 |
| P3R3URF | human | 95-aa microprotein from a uORF; non-canonical-ORF dark matter |
| tam10 | SCHPO | Uncharacterized protein from proteogenomic screening (PomBase-style unknown) |
| AGR3 | human | Small secretory AGR/thioredoxin-like protein; role unclear |
| swrD | BACSU | ~71-aa swarming-motility enhancer; mechanism unknown |
| mxaC | METEA | Auxiliary protein essential for methanol oxidation; mechanism unknown |
| TRAPPC12 | human | Moonlighting TRAPP-associated factor; second function ill-defined |

## Prior art and references

- Wood et al. 2019, *Open Biology* — "Hidden in plain sight" (PMID:30938578)
- Rocha, Freeman et al. 2023, *PLOS Biology* — Functional unknomics / Unknome database (PMID:37552676)
- Stoeger et al. 2018, *PLOS Biology* — why important genes are ignored (PMID:30226837)
- Edwards et al. 2011, *Nature* — "Too many roads not taken" (PMID:21307913)
- Oprea et al. 2018, *Nat Rev Drug Discov* — unexplored therapeutic genome / IDG (PMID:29472638)
- Kustatscher et al. 2022, *Nat Methods* — understudied proteins initiative (PMID:35534633)
- de Crécy-Lagard et al. 2025 — enzymes/proteins of unknown function, prediction error types (PMID:40703034)
- Related internal projects: `STRUCTURE_FUNCTION.md` (dark proteome via structure),
  `IBA_REVIEW.md` (how orthology propagation manufactures false knowledge),
  `OVER_ANNOTATION_PATTERNS.md` (annotation that masks gaps).
- External model: monarch-initiative/dismech — Claude-Code-curated disease-mechanism KB with
  the same per-record-YAML + verbatim-quote evidentiary discipline; derives gap/priority
  dashboards over its corpus.

## Status

- [x] Literature scan (unknome / Wood; Unknome database; dismech approach)
- [x] Survey of how gaps are captured in the KB today
- [x] Core principle established: gaps are curated judgments, not metrics
- [x] Gap taxonomy (biology / curation / ontology; MF/BP/CC darkness)
- [x] Unit defined (anatomy of a gap entry)
- [x] One worked exemplar (CFAP300)
- [ ] Curate the seed read-list into worked gap entries
- [ ] Decide unit granularity (per-gap vs per-gene narrative)
- [ ] Decide home: standalone register vs `knowledge_gaps` schema element (deferred)
- [ ] Conservation / disease prioritization pass over candidates

## Notes

- 2026-06: Project initiated. Brainstorm grounded in (a) the unknome literature, (b) the
  dismech curation model, and (c) how gaps are recorded in this KB today. Key finding from a
  throwaway triage script: apparent "missing molecular function" is dominated (~64% of the
  conserved subset) by GO's inability to describe complex *subunits*, not by true ignorance —
  reinforcing that the gap call must be made by reading, not counting. CFAP300 curated as the
  first worked exemplar.
