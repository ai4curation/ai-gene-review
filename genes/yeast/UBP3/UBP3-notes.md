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

## Review follow-up (PR #2948, 2026-09-06)

Two blocking items from the `ai4c-reviewer` CHANGES_REQUESTED review were
addressed.

- **`description` stated the wrong catalytic class.** It read "cysteine-type
  serine/threonine protease", which is self-contradictory. UniProt records only
  the C19 family assignment [file:yeast/UBP3/UBP3-uniprot.txt line 121,
  "SIMILARITY: Belongs to the peptidase C19 family."] — no serine/threonine
  protease claim. Corrected to "papain-fold cysteine protease of the peptidase
  C19 (USP) family". This matters here because the `GO:0006508` rationale rests
  on Ubp3 being a cysteine peptidase.

- **`GO:0006508` proteolysis rationale asserted a parent-child relation that
  does not hold.** The earlier note above (and the YAML `reason`) described
  proteolysis as a "parent of the more specific `GO:0016579` protein
  deubiquitination". That is wrong, and the reviewer was right to flag it.
  Verified against the QuickGO ontology service: the `is_a`/`part_of` ancestor
  closure of `GO:0016579` is `GO:0016579`, `GO:0070646`, `GO:0070647`,
  `GO:0043412`, `GO:0043687`, `GO:0036211`, `GO:0019538`, `GO:0043170`,
  `GO:0044238`, `GO:0009987`, `GO:0008152`, `GO:0008150` — `GO:0006508` is
  **not** among them. GO deliberately keeps the asymmetry: the MF
  `GO:0004843` *is* under peptidase activity, but the BP for deubiquitination
  sits under `GO:0070646` protein modification by small protein removal, not
  under proteolysis.

  Because the broad term is therefore not a true parent of the specific process
  already annotated, `KEEP_AS_NON_CORE` (which frames it as a correct
  general parent) is the wrong encoding. Changed to `MARK_AS_OVER_ANNOTATED`
  — "not entirely wrong, but likely represents an over-annotation" fits
  exactly, and it matches the in-project precedent for the same term on a
  USP-family DUB (`genes/human/USP25/USP25-ai-review.yaml`, `GO:0006508`,
  `MARK_AS_OVER_ANNOTATED`). This is still not a `REMOVE`, so it does not
  reintroduce the error this PR set out to fix.

The three non-blocking suggestions in the review (MODIFY-with-replacement for
the Hog1 protein-binding row, adding `in_complex: GO:1990861` to
`core_functions`, and removing the stale `UBP3-CURATION-*` /
`UBP3-ai-review-CURATED.yaml` sidecars) are left for the PR author — the first
two are curation judgment calls beyond the requested fixes, and the third
deletes files outside this PR's diff.

`just validate yeast UBP3` passes after the edit.
