# Receipts for rule reviews

A rule review ends in a verdict on somebody else's annotation rule. The verdict is
only as good as the facts behind it, so every claim in a review must come with a
**receipt**: a fact, in a field a program can test, that names its source. The idea
is from [Show me the receipts](https://chrismungall.substack.com/p/show-me-the-receipts-patterns-for):
do not ask the reviewer for a verdict, ask for a verdict plus the receipts, and
check the receipts.

This page says what counts as a receipt in a rule review, which checks run, and
why. It exists because an audit of the 78 ARBA reviews in November 2026 found that
about 45 of them reached a verdict their own evidence did not support. Nearly all
of the errors were detectable from the file.

## What went wrong

| Error | Example | Reviews |
|---|---|---:|
| Rule size used as evidence the annotation is false | "343 condition sets exceeds the analysis threshold of 12" | about 40 |
| Verdict on conditions never recorded | `condition_sets: []`, DEPRECATE at 0.95 | about 38 |
| The review's own notes cited as literature | `literature_support: CONTRADICTED`, source `...-deep-research-manual.md` | about 38 |
| Conditions judged one at a time | "P-loop domain is promiscuous" when the set is P-loop AND two family signatures | about 28 |
| Identifier given another entry's name | IPR000999 called "ribonucleoside-diphosphate reductase" (it is Ribonuclease III domain) | over 20 |
| "True but general" turned into DEPRECATE | replacements proposed are descendants of the rule's own term | about 20 |
| A "false positive" that is experimentally annotated | ESA1 called a false positive for negative regulation of gene expression; SGD has IMP for rDNA heterochromatin formation | about 19 |

The "limit of 12 condition sets" is `max_condition_sets=12` in
`src/ai_gene_review/etl/rule_analysis.py`, the number of sets the overlap analysis
reads by default. It says nothing about whether a rule is right.

## Two questions, both with receipts

A rule review answers two questions, and a verdict needs both.

1. **Accuracy.** Is the annotation true for the proteins each condition set
   matches? This is what most of this page is about.
2. **Meaning and parsimony.** Is the rule a useful biological statement, made
   with conditions that are necessary and sufficient? A rule can be accurate set
   by set and still say nothing: 343 families under one umbrella term, each of
   which curators annotate with a more specific descendant.

The audit found the first question answered from memory. The corrections that
followed answered it from evidence and dropped the second question, which left
reviews that test a rule the way one tests a classifier and say nothing about
its biology. Both are required.

The second question is answered in three fields:

- `biological_units`: the families, complexes or pathways the condition sets
  resolve into. Each unit lists its sets, example proteins, and the most
  informative GO term that curated annotation puts on its members, with the
  annotation (accession, GO id, evidence code, reference) in `evidence`, and
  `term_relation` saying how that term relates to the rule's consequent.
- `biological_meaning.assessment`: `COHERENT` (the consequent is the most
  informative term true of all the units), `TRUE_BUT_UNINFORMATIVE` (units carry
  more specific descendants), `HETEROGENEOUS` (the best term of some units lies
  outside the consequent), or `NOT_ASSESSED` with the reason.
- `parsimony`, `go_specificity`, `taxonomic_scope`: the rule-level judgements,
  with numbers. The receipts are `projects/ARBA_REVIEW/rule_redundancy.tsv`
  (how many descendants the consequent has, and how many of the rule's sets are
  already matched by a rule asserting a more specific term, so emit nothing),
  per-set match counts, and `rules/arba/_interpro2go.txt` (whether one InterPro
  family already maps to the consequent).

Size and generality are not evidence that an annotation is false. They are what
the second question is about. "343 sets is too many" is not a finding;
"320 of 355 sets are covered by rules for more specific terms" is, and so is
"each of these six families is curated to a descendant of the consequent". A
taxon restriction that follows where the training annotations happen to be
(Primates, because the support is human Reactome TAS) rather than where the
biology is, is narrow coverage; say so in `taxonomic_scope`, and do not call the
annotation wrong.

## What a receipt is

| Claim | Receipt |
|---|---|
| "The rule has these conditions" | `rule.condition_sets` copied from the fetched rule, with `rule.retrieved_date` and `rule.source_condition_set_count` |
| "IPR000999 is X" | the official InterPro name as the condition's `label`; in prose, `IPR000999 (Ribonuclease III domain)` |
| "GO:nnnnnnn means X" / "is more specific than Y" | the GO label, and the parent that makes it a descendant |
| "This protein is wrongly annotated" | a UniProt accession in `annotation_assessments[].incorrect_examples`, and no experimental annotation to the term or a descendant |
| "This set is right" | accessions in `correct_examples`, each with the GO id, evidence code and reference in `notes` |
| "N proteins match" | the UniProtKB query, the count and the release |
| "The term is too general for this family" | a `biological_units` entry: the family's curated annotation to a descendant of the consequent |
| "These proteins match the conditions and should not carry the term, though the rule does not annotate them" | accessions in `would_match_examples` (typically reviewed entries). They show what the rule does to unreviewed relatives and are weaker than `incorrect_examples`, which lists proteins that carry the rule's annotation |
| "N of M sets are covered" | the row of `projects/ARBA_REVIEW/rule_redundancy.tsv` (GO rules) or `keyword_redundancy.tsv` (keyword rules); prose that names the file must quote its figures |
| "These sets do no work" | the set numbers with a match count of 0, or `sets_covered_by_more_specific_rule` from `rule_redundancy.tsv` |
| "The literature says" | a PMID or DOI, and a `supporting_text` that is verbatim in the cached paper |

A note the reviewer wrote, an AI deep-research file, and a file that does not exist
are not receipts. Notes and research files are where leads come from; the receipt is
the paper or database record the lead points to.

## Rules for verdicts

- **UNDECIDED is the verdict for a rule that was not examined.** A rule with
  hundreds of condition sets that nobody read set by set is UNDECIDED, however
  general its term. Say which sets were sampled and what they showed.
- **ACCEPT covers the whole rule, on both questions.** Every condition set served
  at `retrieved_date` is recorded and supported, `biological_meaning` is
  `COHERENT`, and `parsimony` is `PARSIMONIOUS` or `ACCEPTABLE`.
- **SPLIT is the verdict for an umbrella term.** At least two `biological_units`,
  each with its own more informative term; `suggested_modifications` says which
  sets go to which term. A sample is enough to show this for a large rule: state
  the sample, and let `confidence` reflect it.
- **MODIFY names the change.** A specific set, protein, term or taxon, in
  `suggested_modifications`.
- **DEPRECATE is for a rule that is still served and should go**: a wrongly
  annotated protein (accessions in `incorrect_examples`), an obsolete consequent,
  or a rule that does no work because every condition set is also matched by a
  rule asserting a more specific term (`sets_covered_by_more_specific_rule` equal
  to the number of sets, as `rule_redundancy.tsv` gives it). The validator checks
  only that count. The judgement has a second half it cannot check: nothing in
  the rule is worth re-homing. A rule that emits nothing but has uncovered sets
  selecting families worth keeping under their own terms is SPLIT (ARBA00026480,
  ARBA00027624, ARBA00026572). This ground is for GO rules only: UniProt keeps
  the most specific ARBA GO term on a protein, but keywords from different rules
  stack, so a covered keyword set still emits. A true but general term whose
  sets are not all covered is SPLIT or MODIFY; low recall alone is not a defect.
- **WITHDRAWN records that UniProt no longer serves the rule** (`rule.withdrawn`).
  It is a fact about the rule, not a verdict, and needs no confidence.
- **Read condition sets as conjunctions.** A set is the proteins that match all its
  conditions, including the taxon. Judge that set, never one of its signatures.
  Alternative sets are expected to be disjoint.
- **A FunFam label is the name of one member**, not the identity of every member.
  Check what the conjunction matches in UniProtKB.
- **Check the alleged false positive before writing it down.** Look up the
  protein's experimental annotations to the term and its descendants. The rule was
  mined from such annotations, so a surprising family is more often a curated
  annotation the reviewer did not know than an error.
- **`confidence` is confidence in the verdict.** Below 0.5, the verdict is
  UNDECIDED.
- **A wrong claim is withdrawn in `corrections`**, with the evidence that refuted
  it, and removed from the prose.

## The checks

`just rules-validate` runs the schema check and then
`src/ai_gene_review/validation/rule_review_receipts.py`. Errors fail the file.

| Check | Severity | Fires when |
|---|---|---|
| `verdict_without_conditions` | error | action is not UNDECIDED and `rule.condition_sets` is empty |
| `missing_rule_snapshot` | error (warning when UNDECIDED) | no `rule.retrieved_date`, or a verdict with no `rule.source_condition_set_count` on a rule that is not withdrawn |
| `verdict_without_confidence` | error | action is not UNDECIDED and no `confidence` is stated |
| `accept_on_partial_examination` | error | ACCEPT with fewer sets recorded than `source_condition_set_count` |
| `condition_label_mismatch`, `go_label_mismatch` | error | a recorded label differs from the official one in `rules/_labels.json` |
| `prose_identifier_label_mismatch` | error / warning | prose writes `ID (name)` or `name (ID)` and the name shares no word with the official label |
| `condition_set_out_of_range` | error | prose or a reference finding names a condition set number higher than the rule as recorded has (usually text left over from an earlier version of the rule) |
| `size_as_evidence` | error | a review that faults the rule (DEPRECATE, MODIFY, SPLIT, MERGE) appeals to a limit, threshold or recommended maximum of condition sets |
| `unresolvable_reference` | error | `supported_by` cites something that is not a PMID, DOI, database record, URL or file |
| `missing_cited_file` | error | a cited `file:` does not exist |
| `own_notes_as_support` | warning | `supported_by` cites notes or an AI research file |
| `literature_verdict_without_literature` | error | `literature_support` is STRONG, MODERATE or CONTRADICTED and the block itself (its `supported_by` or `notes`) names no publication or curated pathway record |
| `verdict_without_meaning` | error | a verdict (ACCEPT, MODIFY, SPLIT, MERGE, DEPRECATE) with no `biological_meaning`, or ACCEPT/SPLIT with `NOT_ASSESSED` |
| `accept_of_uninformative_rule` | error | ACCEPT with `biological_meaning` `TRUE_BUT_UNINFORMATIVE` or `HETEROGENEOUS` |
| `accept_without_parsimony` | error | ACCEPT with `parsimony` missing, or not `PARSIMONIOUS`/`ACCEPTABLE` |
| `split_without_units` | error | SPLIT with fewer than two `biological_units` that carry a term |
| `uninformative_without_units`, `heterogeneous_without_units` | error | the meaning assessment is not backed by units showing it |
| `unit_term_label_mismatch`, `unit_term_without_label`, `unit_term_without_evidence` | error | a unit's term label differs from GO's, is missing, or the term has no curated annotation cited |
| `redundancy_receipt_mismatch` | error | `consequent_descendant_count` or `sets_covered_by_more_specific_rule` differs from `rule_redundancy.tsv` |
| `redundancy_prose_mismatch` | error | prose or a correction's evidence names `rule_redundancy.tsv` or `keyword_redundancy.tsv` with a figure (`N of M sets`, `covered_sets N`, `condition_sets N`, `go_descendants N`) the committed table does not contain |
| `correct_assessment_with_incorrect_examples` | error | an annotation assessment is `CORRECT` and lists `incorrect_examples` |
| `sample_not_described` | warning | `sets_examined_for_meaning` is below the rule's set count and the meaning notes do not say how the sets were chosen |
| `withdrawn_action_mismatch` | error | WITHDRAWN without `rule.withdrawn`, or DEPRECATE on a withdrawn rule |
| `deprecate_without_counterexample` | error | DEPRECATE with no `incorrect_examples`, no `consequent_obsolete: true`, and not every set covered by a more specific rule |
| `modify_without_modification` | error | MODIFY, SPLIT or MERGE with no `suggested_modifications` |
| `low_confidence_verdict` | error | a verdict other than UNDECIDED at confidence below 0.5 |
| `example_not_an_accession` | error | an example is not a UniProt accession |

`just rules-validate --online <file>` adds checks that need the network:

| Check | Severity | Fires when |
|---|---|---|
| `false_positive_has_experimental_annotation` | error | an `incorrect_examples` accession carries the consequent, or a descendant, on experimental evidence in QuickGO |
| `unit_evidence_not_found` | error | a `biological_units[].evidence` line of the form `ACCESSION GO:id CODE reference` names an annotation QuickGO does not hold (that accession, exactly that term, that evidence code and, when given, that reference) |
| `unit_term_relation_mismatch` | error | a unit's `term_relation` to the rule's term is not borne out by the ontology |
| `stale_rule_snapshot`, `rule_withdrawn_upstream` | warning | UniProt now serves a different number of condition sets, or no longer serves the rule |
| `withdrawn_but_served` | error | `rule.withdrawn` is true but UniProt serves the rule |
| `consequent_not_obsolete` | error | `consequent_obsolete` is true but QuickGO serves the term as current |
| `online_check_failed` | warning | a lookup failed, so that check did not run; a clean `--online` result with this warning is not a pass |

Run `--online` before marking a review COMPLETE.

**A receipt field left out is not a pass.** The checks that test a field also require
it: a verdict must state its rule snapshot and its confidence, and the two grounds
that excuse a DEPRECATE from naming a protein (`withdrawn`, `consequent_obsolete`) are
both verified online. FunFam labels are compared with the cache but cannot be
refreshed by `--refresh-labels`, which covers InterPro and GO only; update a renamed
FunFam label in `rules/_labels.json` by hand, from CATH.

The label checks compare against the committed cache `rules/_labels.json`. InterPro
renames entries, so a label error can mean the cache is stale. Run
`uv run python -m ai_gene_review.validation.rule_review_receipts --refresh-labels <file>`:
it re-fetches only the identifiers whose recorded label disagrees with the cache.
If the error remains, the review is wrong.

## What ACCEPT means

In the corrected reviews, ACCEPT means every condition set was examined and its
reviewed (Swiss-Prot) matches carry the consequent on evidence other than ARBA
itself, usually with an experimental annotation in each set. Swiss-Prot entries can
carry a term only as an ARBA IEA (GO_REF:0000117); those are the rule's own output
and are excluded. This is still in-sample evidence: the rule was mined from
Swiss-Prot, and the unreviewed entries it annotates were counted, not inspected.
Read ACCEPT as "no conflict found", and keep the confidence modest.

## What the checks cannot see

Deterministic checks test that a receipt exists and resolves. They do not test that
it supports the claim it is attached to. A real PMID can be cited for something the
paper does not say, and a real accession can be a poor example. Two things cover
that gap:

- **Spot-checks by a second reader.** The November 2026 audit was this: independent
  readers re-derived the facts each verdict depended on. Sample new reviews the same
  way, starting with DEPRECATE verdicts and anything a reviewer flags as unusual.
- **Corrections as test cases.** Each `corrections` entry records a claim, its
  `error_type` and the refuting evidence. Count them by `error_type` to see which
  errors recur, and turn recurring ones into a check here or a line in the
  reviewer skill.

Receipts can also be written after the fact to fit a verdict. That is why the
online check looks for evidence against the review (experimental annotation on an
alleged false positive) and not only for evidence the reviewer chose to cite.
