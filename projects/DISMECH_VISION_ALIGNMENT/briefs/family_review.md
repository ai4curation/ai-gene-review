# Brief: review a PANTHER family (vision-disorder alignment)

You work in the repository `/home/user/ai-gene-review`. A coordinator commits the
results; you never touch git.

Gene reviews written for this project keep meeting GO annotations that reach a gene by
descent in a PANTHER tree (IBA, from a PAINT curator's IBD at an ancestral node). A
family review records, once and for the whole family, whether such a term can be
inherited family-wide, only within named subfamilies, or not at all, and judges each
PAINT node. Your job is the family review for each family named in your task.

## Hard rules

- You write only `interpro/panther/<PTHR>/<PTHR>-review.yaml` for the families in your
  task. Do not edit gene reviews, `*-paint.tsv`, `*-entries.csv`, `*-metadata.yaml`,
  anything under `publications/`, `cache/`, `src/`, or another family.
- You may cache papers with `just fetch-pmid <PMID>`. No git commands that change state.
  No `uv sync`, no installs, no deep-research recipes.
- Never write an identifier from memory. PANTHER family and subfamily labels must be the
  official names: `grep -A1 "^id: PANTHER:PTHR24240$" interpro/panther/panther.obo`.
  PTN node ids come only from the family's `<PTHR>-paint.tsv` or from the
  `supporting_entities` of an IBA row in a gene review. GO labels must be exact
  (`curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008020"`).
- Every `supporting_text` must be a verbatim substring of the cited source: a cached
  publication (`publications/PMID_<n>.md`), or a repository file cited as
  `file:<path>` (for example a gene review or a UniProt record). Find the passage with
  `grep -n` and copy it. No real quote: cite the reference without `supporting_text`.
- If the evidence for a node placement or a loss is not clear, say UNRESOLVED. Do not
  assert an evolutionary claim the data does not support, and do not guess a node.

## Read first

1. `CLAUDE.md` lines 436-546 (what an IBA asserts; PANTHER ids).
2. `src/ai_gene_review/schema/family_review.yaml`: the `FamilyReview`, `TermAssessment`,
   `NodeAssessment`, `MemberException` classes and the enums `FunctionalCoherenceEnum`,
   `TermScopeEnum`, `NodeAssessmentEnum`. Read the enum descriptions before using a value.
3. Two finished examples: `interpro/panther/PTHR12210/PTHR12210-review.yaml` (term and
   node assessments with quotes) and `interpro/panther/PTHR11347/PTHR11347-review.yaml`
   (minimal).
4. For each family: `<PTHR>-metadata.yaml`, `<PTHR>-paint.tsv` (every IBD, IRD and IKR
   node row PAINT holds for the family: node, term, evidence, seeds, taxon, date), and
   `<PTHR>-entries.csv` (members). Then the finished gene reviews of the family members
   named in your task: their IBA rows, the actions taken on them and the reasons.
5. `projects/IBA_REVIEW.md` only if you need the catalogue of propagation failure
   patterns; `projects/IRD_EVIDENCE.md` only if the family has IRD or IKR rows.

## What a family review must contain

- `family_id`, `family_name` (official), `summary`, `functional_coherence` and
  `coherence_reason`, `reference_protein` (a reviewed human member, with `gene_review`
  path), `references`, `review_status`, `reviewed_by: claude-code`, `review_date`.
- `term_assessments`: one for each GO term that matters for inheritance in this family,
  at least every term that an IBA row carries in the reviewed members' gene reviews. Give
  the `scope` and a `scope_reason` that names which branches do and do not have the
  function, with quotes. Where a gene review REMOVEs or marks over-annotated an IBA that
  the family term would otherwise cover, record it as a `member_exceptions` entry on that
  term assessment (read the schema for its slots), so that the family review and the gene
  review agree.
- `node_assessments`: one for each PAINT node row that lies on the lineage of a reviewed
  member (the PTN ids in that member's IBA rows), and for any IRD or IKR row in the
  slice. Judge the placement: is the function present across the clade below the node, or
  is the node too deep, on the wrong branch, or in need of pruning for a subclade? A short
  seed list is not weak evidence, and a member appearing among its own seeds is expected.
  You cannot inspect the PANTHER tree or alignment here beyond the slice, the member list
  and the literature; say so where it limits a verdict, and prefer UNRESOLVED to a guess.

After writing the file, copy the PAINT facts in and validate:

```bash
just fill-node-evidence --apply interpro/panther/<PTHR>/<PTHR>-review.yaml
uv run linkml-validate --schema src/ai_gene_review/schema/family_review.yaml --target-class FamilyReview interpro/panther/<PTHR>/<PTHR>-review.yaml
uv run linkml-term-validator validate-data interpro/panther/<PTHR>/<PTHR>-review.yaml -s src/ai_gene_review/schema/family_review.yaml -t FamilyReview --labels -c conf/oak_config.yaml
scripts/run_reference_validator.sh validate data interpro/panther/<PTHR>/<PTHR>-review.yaml --schema src/ai_gene_review/schema/family_review.yaml --target-class FamilyReview --config conf/reference_validator_config.yaml
uv run python -m ai_gene_review.validation.quote_check interpro/panther/<PTHR>/<PTHR>-review.yaml
uv run python -m ai_gene_review.validation.family_gene_crosscheck 2>&1 | grep -B2 -A6 "<PTHR>"
```

Fix every error. The last command reports disagreements between family reviews and gene
reviews across the whole corpus; only the lines about your families concern you.
Set `review_status: COMPLETE` only when all of these pass and you would defend each
verdict; otherwise `DRAFT`, saying in `notes` what is missing.

## What to send back

At most about 120 words per family, plain text: coherence call; the term scopes; node
verdicts that are not SOUND, with the reason in one line each; member exceptions
recorded; anything in a gene review that the family evidence contradicts (do not edit the
gene review, report it); validation result.
