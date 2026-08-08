# BRCA2 (P51587) notes

## 2026-07-22 — QA re-review (no changes to YAML)

Performed a quality-assurance pass over `BRCA2-ai-review.yaml` (~151 annotations).
The file was already the product of a careful A→Z manual review. Conclusion: it is
in good shape and **no edits were warranted** under a conservative bar (only change
what is a confident improvement).

Checks performed and results:

- **Structural validation** (`uv run ai-gene-review validate`): ✓ Valid, no warnings.
- **Supporting-text verbatim check** (`linkml-reference-validator validate data`): all
  PMID-quoted `supporting_text` values pass as verbatim substrings of the cached
  publications. The only reported errors were "Could not fetch reference" for Reactome
  and `file:` references — these are offline-fetch failures in this environment, not
  quote mismatches.
- **Action consistency across evidence types**: consistent. GO:0000724 (HR repair) is
  ACCEPT across IBA/IEA/IDA/IMP; GO:0005515 (protein binding) is uniformly REMOVE;
  GO:0005654 (nucleoplasm) uniformly ACCEPT; GO:0005813 (centrosome) and GO:0070200
  uniformly KEEP_AS_NON_CORE; GO:0010484/GO:0010485 (HAT) both UNDECIDED. No same-term
  action conflicts.
- **"protein binding" guideline**: no GO:0005515 annotation is marked ACCEPT — all are
  REMOVE (with the specific interactor recorded in the summary). REMOVE is an
  established repo-wide action for this uninformative term, so these were left as-is
  rather than flipped wholesale.
- **core_functions branch placement** (strictly validated): correct. `molecular_function`
  = GO:0003697 (MF); `directly_involved_in` = GO:0000724/0000730/0042148/0031297/1990426
  (all BP); `locations` = GO:0005634/0005654 (CC); `in_complex` = GO:1990391 (CC/complex).
- **Core function capture**: RAD51 loading / presynaptic filament (ssDNA binding + HR +
  DNA recombinase assembly + DNA strand invasion) and stalled-fork protection are both
  captured as core; D-loop formation is represented via the GO:0042148 NEW term. Not
  over-generalized.
- **Description field**: clean standalone biology, no project/workflow framing.

Issues considered but deliberately left alone (all guideline-compliant as written):

- **HAT activity tension**: the positive H3/H4 HAT IDAs (GO:0010484/GO:0010485,
  PMID:9619837) are UNDECIDED while the negated GO:0004402 (NOT HAT, PMID:9824164) is
  ACCEPT. Mild internal tension, but UNDECIDED is the correct conservative choice for a
  contested experimental IDA, and REMOVE of an experimental annotation is disallowed.
- **GO:0006289 nucleotide-excision repair** (IMP, PMID:16845393) sits on an
  interstrand-cross-link-repair paper; KEEP_AS_NON_CORE with an honest caveat is a
  defensible conservative call (a MODIFY to GO:0036297 would be reinterpreting a GOA
  term id, out of scope for QA).
- **GO:0030141 secretory granule** (IDA, PMID:8589722, a BRCA1-titled paper) is
  UNDECIDED with a hedged "possible annotation error" note — compliant because the
  cached abstract explicitly foregrounds BRCA1, and the reviewer used UNDECIDED (not
  REMOVE) per the guideline for experimental annotations whose full text is unseen.
