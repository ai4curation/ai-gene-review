# Brief for PANTHER family-review agents (YeastPathways module project)

Repo: /home/user/ai-gene-review. You are writing `FamilyReview` records,
`interpro/panther/<PTHR>/<PTHR>-review.yaml`, for PANTHER families that are
used as role families in the YeastPathways-derived modules
(`projects/YEAST_PATHWAYS/module_members/*.yaml` list them under
`panther_families`). The goal: decide whether the family is functionally
coherent enough for each GO activity/process the modules (and PAINT) attach to
it, and record subfamily divergence once at family level.

## Read first
- `CLAUDE.md`, especially "What an IBA asserts", "PANTHER ids", and the
  rule that you never guess identifiers.
- `src/ai_gene_review/schema/family_review.yaml` (the FamilyReview class and
  enums; `functional_coherence`, `term_assessments[].scope`,
  `node_assessments[].assessment`).
- Two or three existing complete examples, e.g.
  `interpro/panther/PTHR10202/PTHR10202-review.yaml` (node assessments),
  `interpro/panther/PTHR10102/PTHR10102-review.yaml` (compact),
  and any other `interpro/panther/*/*-review.yaml` with `review_status: COMPLETE`.

## For each family in your batch
1. Make sure the fetched inputs exist; if not run
   `just fetch-panther-family <PTHR>` and `just fetch-panther-paint <PTHR>`
   (they write `<PTHR>-metadata.yaml`, `<PTHR>-entries.csv`, `<PTHR>-paint.tsv`;
   never hand-edit those). Get the official family/subfamily names from
   `interpro/panther/panther.obo` (`grep -A1 "^id: PANTHER:PTHRxxxxx"`).
2. Read the module YAML(s) that use the family (listed in your batch), the
   gene reviews of the S. cerevisiae / S. pombe / other members that exist
   under `genes/**` (their `core_functions` and any `propagation_review`
   findings), and the PAINT IBD nodes in `<PTHR>-paint.tsv`.
3. Write the review:
   - `family_id`, `family_name` (official PANTHER name, verbatim),
     `preferred_name` (your readable name), `summary`.
   - `functional_coherence` + `coherence_reason` (say what diverges).
   - `subfamilies` for functionally distinct groups that matter to the modules
     (official SF ids/names; `representative_members` with UniProtKB ids and
     `gene_review` paths where they exist; `diverged_from_family` when true).
   - `term_assessments` for every GO term the modules assert for this family's
     role and for each PAINT IBD term in the paint file that a reviewed member
     received: scope (FAMILY_WIDE / SUBFAMILY_ONLY / etc. per the enum),
     `scope_reason`, `supported_by` with verbatim quotes from cached
     publications (`publications/PMID_*.md`, fetch with `just fetch-pmid`) or
     `file:` references to gene reviews / module YAML / PANTHER files.
   - `node_assessments` where a gene review flagged a PAINT node as wrong (e.g.
     paralog over-propagation such as SPE4 spermidine synthase from SPE3, CTT1
     peroxisome from CTA1, BIO3 dethiobiotin synthase from the AtBIO1 fusion
     node, CAB4 dephospho-CoA kinase from COASY). Use exact PTN ids from the
     paint file; never invent one.
   - `residue_sites` only if you can anchor a residue to a real UniProt
     sequence position you have checked; otherwise omit.
   - `references`, `review_status: COMPLETE`, `reviewed_by: claude-code`,
     `review_date: 2026-10-06`.
4. Validate (all must pass without errors):
   ```
   uv run linkml-validate --schema src/ai_gene_review/schema/family_review.yaml --target-class FamilyReview interpro/panther/<PTHR>/<PTHR>-review.yaml
   uv run linkml-term-validator validate-data interpro/panther/<PTHR>/<PTHR>-review.yaml -s src/ai_gene_review/schema/family_review.yaml -t FamilyReview --labels -c conf/oak_config.yaml
   scripts/run_reference_validator.sh validate data interpro/panther/<PTHR>/<PTHR>-review.yaml --schema src/ai_gene_review/schema/family_review.yaml --target-class FamilyReview --config conf/reference_validator_config.yaml
   ```
   ("Total checks: 0" from the reference validator means no failures.)
5. History record:
   `just new-history --kind other --path interpro/panther/<PTHR>/<PTHR>-review.yaml --slug <PTHR>-family-review --event CREATE --outcome changed --summary "Family review: <PTHR>" --agent-tool claude-code --details "..."`
   then `just validate-history <path>`.

## Rules
- Touch only `interpro/panther/<your PTHRs>/`, `publications/` (via fetch),
  and `history/other/<PTHR>-family-review/`. Do not edit modules or gene
  reviews; report inconsistencies instead. Do not commit. Revert incidental
  `cache/` changes (`git checkout -- cache/`). Use a uniquely named scratchpad
  subfolder for any helper scripts.
- Do not assert node placements, residue losses or subfamily functions you have
  not checked against the PANTHER/PAINT files, sequences, or literature.

## Final answer
Per family: coherence call, key term scopes, node assessments, inconsistencies
found between module / gene reviews / PAINT, and validation status.
