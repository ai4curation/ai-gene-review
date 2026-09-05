# UBP3 curation notes

## 2026-09-02 Update: fixed REMOVE misapplication for genuine-but-generic annotations

Audited the existing review for action-enum misuse against the project's own
`ActionEnum` definitions (`REMOVE` = "unlikely to be correct based on combined
evidence"; `MARK_AS_OVER_ANNOTATED` = "not entirely wrong, but likely
represents an over-annotation"; `KEEP_AS_NON_CORE` = correct but not core).

Found 11 rows where `REMOVE` had been applied to annotations whose underlying
evidence the review itself acknowledged as genuine and correct — the review's
own `reason` text argued only that the term was too generic/broad, not that
it was factually wrong. This misapplies `REMOVE`'s semantics (which signals
"this annotation is unlikely to be correct") to cases that are really
over-annotation or over-general-but-true annotation:

- **9x `GO:0005515` protein binding (IPI)**, one per cited PMID
  (PMID:16429126, PMID:16554755 x3, PMID:17632125, PMID:18719252,
  PMID:20508643, PMID:21179020, PMID:21743437, PMID:37968396). Every one of
  these rows is a genuinely evidenced physical interaction (IntAct IPI
  evidence); the review's own reasoning in each case was "generic/
  uninformative", which is exactly the definition of `MARK_AS_OVER_ANNOTATED`,
  not `REMOVE`. Changed action to `MARK_AS_OVER_ANNOTATED` for all 9 rows;
  reasons were left substantively intact but reworded to reflect that the
  interaction itself is real and correctly cited, with the more informative
  replacement terms (GO:1990861 Ubp3-Bre5 complex, GO:0047484 regulation of
  response to osmotic stress, GO:0034517 ribophagy) noted as already covering
  the same evidence.

- **`GO:0031647` regulation of protein stability (IBA)**: this is a
  phylogenetic (IBA) annotation, and per project policy an IBA should only be
  overturned with target-specific divergence/loss evidence, not because the
  term is broad. No such evidence was offered (or exists) here — indeed the
  claim is directly true for UBP3, which reverses degradative ubiquitination
  of Sec23 and RNAP II [PMID:12778054, PMID:18498751]. Changed action from
  `REMOVE` to `KEEP_AS_NON_CORE`, matching how comparably broad-but-true IBA
  terms are treated elsewhere in this project (e.g. TSA1's `response to
  oxidative stress`).

- **`GO:0006508` proteolysis (IEA)**: Ubp3 is a bona fide cysteine-type
  peptidase (peptidase C19/USP family, EC 3.4.19.12) that hydrolyzes the
  isopeptide bond linking ubiquitin to substrate lysines — this literally is
  proteolysis, just described at a very general level. Changed action from
  `REMOVE` to `KEEP_AS_NON_CORE` as a correct, non-core parent of the more
  specific `GO:0016579` protein deubiquitination process annotation.

No changes were made to any `ACCEPT` rows, to the `description`, or to
`core_functions`; those were sound. `validate --terms` and `validate-goa`
both pass after the edit.
