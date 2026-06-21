# Evidence subtraction reports

The **subtraction report** is a generic mechanism that answers: *if we removed
all annotations from a given reference / evidence code, what would we lose?*

It was built for the [IBA review project](https://github.com/ai4curation/ai-gene-review/blob/main/projects/IBA_REVIEW.md)
— where, in addition to flagging IBAs we want to question, we want to see what
IBA actually *contributes* — but it works for any reference id (e.g.
`GO_REF:0000033`) or evidence code (e.g. `IBA`, `ISS`, `IEA`).

## What it reports

For the chosen filter, it simulates **removing** the matching annotations and
reports two things per gene:

1. **Endorsed annotations that disappear.** Every annotation the reviewer
   endorsed (`ACCEPT` / `KEEP_AS_NON_CORE`) that matches the filter, flagged as:
   - `UNIQUE` — no surviving annotation still asserts that term, so the
     information is genuinely lost; or
   - `REDUNDANT` — a surviving annotation still asserts that term *or a more
     specific descendant of it*, so the term survives the subtraction.

2. **`core_functions` grounding after subtraction.** Each GO term used in a
   `core_functions` entry (`molecular_function`,
   `contributes_to_molecular_function`, `directly_involved_in`, `locations`,
   `in_complex`) is classified as:
   - `RETAINED` — still grounded by a surviving endorsed annotation;
   - `LOST` — grounded only by subtracted annotations (this is the real cost of
     the subtraction); or
   - `UNSUPPORTED` — not grounded by any annotation at all (pure synthesis;
     unaffected by the subtraction).

## Closure

Grounding is **closure-aware** (over `is_a` + `part_of`). A core-function term
`T` is grounded by an annotation whose effective term is `X` when `T` is a
reflexive ancestor of `X` — i.e. `X` is `T` itself or a *more specific*
descendant. A more *general* surviving annotation does not ground a specific
core-function claim. `MODIFY` annotations are grounded via their
`proposed_replacement_terms`.

## Usage

```bash
# Markdown report to stdout — what does removing IBA lose, across all genes?
ai-gene-review subtraction-report -e IBA

# Restrict to a subset, subtract by reference id
ai-gene-review subtraction-report genes/human -r GO_REF:0000033

# Two TSVs: <prefix>-lost-annotations.tsv and <prefix>-core-functions.tsv
ai-gene-review subtraction-report genes -e IBA --format tsv -o reports/iba

# Disable closure (exact-term matching only)
ai-gene-review subtraction-report -e IBA --no-closure
```

### Inverse direction: "use only IBA" (where IBA is too conservative)

`--keep-only` inverts the filter — it subtracts everything *except* the
filter. `--keep-only -e IBA` removes all non-IBA annotations, so the report
shows what is lost if IBA were the only evidence used:

- **LOST `core_functions` terms** are grounded only by non-IBA (often
  experimental) evidence — molecular functions IBA alone would miss. This is the
  signal that IBA is *too conservative* for that gene.
- **Lost endorsed annotations** are the non-IBA `ACCEPT`/`KEEP_AS_NON_CORE`
  calls that IBA does not reproduce.

```bash
ai-gene-review subtraction-report genes/human --keep-only -e IBA -r GO_REF:0000033
just subtraction-report-iba-only-tsv          # TSVs under reports/
```

Because closure is applied, an IBA annotation to a *more general* parent does
**not** count as grounding a specific experimental child — so a gene where IBA
gives only the broad term and experiment pins the specific activity correctly
shows the specific term as LOST.

### Suppressing low-information branches

`--exclude-branch` drops every term under a given branch (closure-aware) from
both the lost-annotation and core-function reports. Use `GO:0005488` to remove
generic `binding` molecular functions (including `protein binding`), which carry
little mechanistic information:

```bash
ai-gene-review subtraction-report genes/human --keep-only -e IBA \
    --exclude-branch GO:0005488 -f tsv -o reports/iba-only
```

The ranked, evidence-enriched view of the **curated core molecular functions**
IBA alone would miss (binding excluded) is produced by
`projects/IBA_REVIEW/iba_too_conservative_core_mf.py`
(`just subtraction-report-iba-conservative-core-mf`), which writes
`reports/iba-too-conservative-core-mf.md`. A term promoted into `core_functions`
is the curator's highest-confidence judgement of what the gene does, so these are
weighted above ordinary `ACCEPT` annotations.

Just recipes:

```bash
just subtraction-report-evidence IBA genes/human   # markdown to stdout
just subtraction-report-iba-tsv                    # TSVs under reports/
```

The first run with closure downloads the GO SQLite build via OAK
(`sqlite:obo:go`); pass `--no-closure` for a fast, exact-match approximation.

## Programmatic API

```python
from ai_gene_review.analysis import (
    SubtractionFilter, SubtractionReporter, make_go_ancestor_fn,
)

reporter = SubtractionReporter(ancestors=make_go_ancestor_fn())
filt = SubtractionFilter.create(evidence_codes=["IBA"])
results = reporter.analyze_files(["genes/human/UBA7/UBA7-ai-review.yaml"], filt)
for res in results:
    print(res.gene_symbol, res.n_uniquely_lost, res.n_core_terms_lost)
```

The `ancestors` argument is an injectable reflexive ancestor function, so the
engine can be unit-tested without an ontology backend (and closure can be turned
off entirely by omitting it).
