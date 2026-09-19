# ARGLU1 bioinformatics

Reproducible analyses supporting `genes/human/ARGLU1/ARGLU1-ai-review.yaml`.
Findings are written up in [`RESULTS.md`](RESULTS.md).

## Scripts

| script | output | needs network |
|---|---|---|
| `panther_node_audit.py` | `results.json` | yes (QuickGO, UniProt) |
| `reference_scope_audit.py` | `reference_scope.json` | yes (QuickGO) |
| `intact_partner_audit.py` | `intact_partners.json` | yes (IntAct, UniProt) |
| `composition_and_features.py` | `composition.json` | no (reads `../ARGLU1-uniprot.txt`) |
| `sibling_row_verdicts.py` | `sibling_verdicts.json` | no (reads `genes/**/ *-ai-review.yaml`) |
| `splicing_factor_eligibility.py` | `splicing_factor_eligibility.json` | yes (QuickGO) |
| `verify_authored_terms.py` | — (exit status) | yes (QuickGO **and** OLS4) |
| `verify_quotes.py` | — (exit status) | no (reads the review and `publications/`) |
| `audit_arglu1_review.py` | — (exit status) | no (reads the review, the GOA tsv and the JSON artefacts) |

## Running

```bash
cd genes/human/ARGLU1/ARGLU1-bioinformatics
uv run python panther_node_audit.py
uv run python reference_scope_audit.py
uv run python intact_partner_audit.py
uv run python composition_and_features.py
uv run python sibling_row_verdicts.py

# invariant checks over the finished review (exit non-zero on a problem)
uv run python audit_arglu1_review.py
uv run python audit_arglu1_review.py --self-test
```

## `verify_authored_terms.py` — two services, not two endpoints

Checks every GO id the review **authors** against **QuickGO and OLS4
independently**. Ids that came from GOA are deliberately not checked — per
`CLAUDE.md` those are machine-supplied and not the reviewer's to second-guess —
and their count is printed so the exclusion is visible rather than silent.

It exists because a single service was a confident outlier twice in this PR's
history. QuickGO reported `GO:0035259` obsolete and `GO:0016922` childless; the GO
API, OLS4 and the repository's own `cache/ontologies/go.tsv` all disagreed, and
QuickGO was wrong on both. The compounding error was that the "two checks" behind
the claim were QuickGO's `/children` endpoint and QuickGO's text search —
**two methods against one service is one check.**

### What it fails on, and what it only reports

| scope | treatment |
|---|---|
| `core_functions`, `proposed_replacement_terms`, `term.id` of `action: NEW` rows | **FAIL** on obsolescence per either service, non-resolution, or a declared `label` matching neither service |
| any `GO:\d{7}` appearing **only in free text** | **report** status + service disagreement as advisory |

**The prose arm deliberately does not adjudicate, and that is a retraction of an
earlier claim here.** The `GO:0035259` defect lived in `suggested_questions`
prose, so a structured-slot-only guard would not have caught it and an earlier
version of this README said this script "guards the class". It does not, quite.

Attributing an English status phrase to a particular id by proximity was
implemented and then withdrawn, because it produced false positives in both
directions **on this very document**:

- *"a bare `GO:0005515` row **is replaced by** a more informative term"* reads as
  an obsolescence claim about `GO:0019901`, which appears two clauses later;
- *"`GO:0035257` and `GO:0035258` were **absorbed into** `GO:0016922`"* reads as
  one about `GO:0016922`, which is active.

A guard that cries wolf on correct content gets switched off, which is worse than
not having it. So prose ids get their true status surfaced for a human to check
against the sentence, and the summary line states the structured count and the
prose count separately rather than implying one number covers both.

Also worth knowing, and the reason the two services are not interchangeable:
**QuickGO silently resolves merges.** `GO:0035257`/`GO:0035258` return
`GO:0016922`'s record with `isObsolete=False`, where OLS4 reports them
obsolete-replaced-by. So a QuickGO "not obsolete" can mean either *current* or
*merged into something else*, and the response cannot distinguish them.

## `verify_quotes.py` — where the repo's quote gate is weakest

Checks all **83** `supporting_text` values against their cached publications via
`build_supporting_text_validator()` — the repo's own helper, configured from
`conf/reference_validator_config.yaml` — so it uses the same matcher, the same
`literal_bracket_patterns` and the same `skip_prefixes` as the gate rather than an
approximation of them.

It is not redundant with `just validate`. For a reference whose cache is
**abstract-only**, `validation/validator.py:156` downgrades a non-matching quote
from ERROR to **WARNING**. **Six** of this review's references are abstract-only —
`PMID:21454576`, `PMID:22365833`, `PMID:22923044`, `PMID:23602568`,
`PMID:36533631`, `PMID:42641889`, covering 25 quote instances — so a paraphrase
against any of them would not fail the build. One of them, `PMID:22923044`,
carries the quote the whole mitochondrion finding rests on.

### The inversion this script was rewritten to fix

The first version collected a quote only when the **same dict** carried both
`reference_id` and `supporting_text`. But `references[].findings[]` entries carry
`statement` + `supporting_text`, with the identifier on the **parent**
`references[].id`. So it silently skipped all 22 findings quotes:

| path | quotes | gated by |
|---|---|---|
| `review.supported_by`, `core_functions[].supported_by`, `knowledge_gaps[].provenance` | 61 | external CLI — **strict** |
| `references[].findings[]` | 22 | `validator.py` — **ERROR→WARNING when abstract-only** |

It covered the 61 the strict gate already handles and missed every one of the 22
gated by the weak branch it cited as its reason for existing — 8 of those on
abstract-only sources. It reported *"quotes found: 61"*, which read as complete
coverage at 73%.

Two structural fixes, both of which a future shape change must survive:

1. the collector **inherits the parent `references[].id`** when walking into
   `findings`, and records which shape each quote came from; and
2. the collected count is **asserted equal to the number of `supporting_text:`
   keys in the raw file**, so a collector that cannot see part of the document
   fails loudly instead of under-reporting. Fix the walk, never the assertion.

`--self-test` corrupts a quote on the **findings path against an abstract-only
source** (the case the old version structurally could not reach *and* the only
path the downgrade covers), a quote on the `supported_by` path against a
full-text source, and asserts the coverage invariant fires on a crippled
document. Each case requires the problem to name **that path and that gate**, not
merely to be non-empty — a mutation that trips some other check is not evidence
the guard under test works.

## `audit_arglu1_review.py`

Guards the finished review against four classes of defect that no repo validator
catches: duplicate YAML keys (which delete provenance before any gate runs),
under-coverage against the GOA tsv (the `fetch-gene` stub collapses rows),
hand-maintained `source_entities` drifting from the GOA WITH/FROM column, and
numbers in prose drifting away from the artefacts they were derived from.

The claim check works two ways, because either alone is insufficient:

- **Context-bound regexes** over the review bind each number to the sentence that
  gives it meaning, so a wrong value is caught even when the right value still
  appears elsewhere.
- **Per-document occurrence counts** (`CLAIM_SITES`) catch a single-site change in
  any of the review, the notes, or `RESULTS.md`. Only the site *count* is declared
  in the table; the *value* is always read from the committed JSON, so the table
  cannot drift the numbers it checks.

`--self-test` mutates the real inputs and asserts each guard fires. Three
properties of it are deliberate and worth preserving if you edit it:

1. **Every mutation asserts its anchor occurs exactly once first.** Zero matches
   would change nothing and "pass" vacuously; two or more would silently mutate
   whichever came first, so the case stops testing what it was written for.
2. **Every case names the guard it expects** (`must_contain`). Without that, a
   mutation tripping some *other* check reports as a pass — and a guard that
   passes for the wrong reason is indistinguishable from one that works. This was
   a real defect here: dropping an annotation from the parsed object while leaving
   the raw text alone tripped the raw-vs-parsed reconciliation rather than the row
   coverage check it was written for.
3. **Structural mutations re-serialise the document** so raw text and parsed
   object stay consistent, isolating the guard under test. A baseline assertion
   confirms re-serialising the *unmutated* review still passes every check, so the
   serialiser cannot be what the mutations are testing.

A passing self-test proves the guards that exist fire. It cannot tell you which
guard was never written — the companion-document arm was declared and matched
nothing for a while, which read as coverage while checking nothing, and was found
by deliberately breaking a number rather than by reading the code.

Only `sibling_row_verdicts.py` needs a third-party import (`pyyaml`, already a
repo dependency, hence plain `uv run python`); the others use the standard
library only and can also be run with `uv run --no-project python`.

`RESULTS.md` is hand-written prose summarising the JSON artefacts. It is **not**
generated by any of the scripts, so editing it will not be reverted by a rerun —
but the numbers it quotes are taken from the JSON, and a rerun should reproduce
them.

## Design notes

These follow conventions that earlier reviews in this campaign learned the hard
way:

- **Paginated fetches assert `len(results) == numberOfHits`.** QuickGO and IntAct
  clamp an over-large page size rather than erroring, so a guard written against
  a chosen page-size constant can be silently defeated.
- **Annotation counts and entity counts are reported as separate numbers.** One
  gene product can hold several annotations to the same term; conflating the two
  inflates a projection signal.
- **Where a result set is too large to enumerate, the entity count is reported as
  unavailable** rather than extrapolated from one page.
- **`entryType.startswith("UniProtKB reviewed")`**, never `"reviewed" in
  entryType` — "reviewed" is a substring of "unreviewed", so the naive test marks
  every TrEMBL entry as reviewed and the count looks plausible because it equals
  the total.
- **Identifier lookups fetch more than one hit and fail loudly on an ambiguous or
  dead accession.** A `size=1` query turns an ambiguity into a confident wrong
  answer, and a deleted UniProt entry returns an empty record that is
  indistinguishable from "this protein has no annotations".
- **Missing input is a hard error naming the fix command**, not a silently skipped
  section.
- **The repo root is derived, never hardcoded.** A shared script carrying one
  agent's worktree path resolves against the wrong checkout and reports confident
  false failures.
