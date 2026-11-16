# Brief: review one human gene (vision-disorder alignment)

You are one of a few workers in the repository `/home/user/ai-gene-review`. Each worker
owns one gene. A coordinator commits the results; you never touch git.

The campaign: Mendelian non-syndromic vision disorders curated in the sister knowledge
base `dismech` are being checked against the normal function of their causal genes as
reviewed here. Your job is a complete, defensible GO annotation review of one gene,
following this repository's rules, at low cost: read the prepared dossier instead of
opening every source file, and write your decisions to one file that a script merges.

## Hard rules

- You write three things only: the decisions file named in your task, the notes file
  `genes/human/<GENE>/<GENE>-notes.md`, and, through the merge script, the review
  `genes/human/<GENE>/<GENE>-ai-review.yaml`. Do not edit the review YAML by hand, and do
  not edit anything under `publications/`, `reactome/`, `cache/`, `interpro/`, `src/`, any
  `*-goa.tsv`, `*-uniprot.txt` or `*-deep-research-*.md`, or another gene's folder.
- You may cache further papers with `just fetch-pmid <PMID>`.
- No git commands that change state. No `uv sync`, no installs, no deep-research recipes.
- Never write an identifier (GO, PMID, UniProt, PANTHER, Reactome) from memory; look it
  up in the step you write it. GO labels must be the exact current label.
- Every `supporting_text` must be a verbatim substring of the cited source file
  (`publications/PMID_<n>.md`, `reactome/R-HSA-<n>.md`, or the UniProt record cited as
  `file:human/<GENE>/<GENE>-uniprot.txt`). The dossier excerpts are cut and
  whitespace-normalised: before you quote, find the passage in the source file with
  `grep -n` and copy it from there. No real quote: give `reference_id` alone.
- The provider report `<GENE>-deep-research-openscientist.md` is a literature lead, not
  evidence. Do not quote it and do not cite a PMID from it that you have not opened.
- Be economical. Read the dossier once. Open a source file only to check a quote or to
  read a passage the dossier cut. The session can be cut off by a usage limit, so write
  the notes file early and merge your decisions in batches (the merge script can be run
  repeatedly).

## Read first (in this order, nothing else unless a row needs it)

1. `CLAUDE.md` lines 127-546 (gene review guidelines, actions, ND, organelle terms, do
   not overrule curators, do not add what curators declined, what an IBA asserts,
   term-id validation) and lines 587-766 (reviewing references, curation guidelines,
   knowledge gaps). Read these two ranges once.
2. `.claude/skills/annotation-reviewer/SKILL.md`.
3. Your dossier (path in your task): UniProt digest, the numbered annotation rows, each
   cited reference with abstract and gene-mentioning passages, PAINT losses.
4. The notes file, if a previous worker left one, and the OpenScientist report.
5. For format only, skim the core_functions and references sections of
   `genes/human/CNGA1/CNGA1-ai-review.yaml` (from line 862).

## Decisions file

Write YAML in the shape `projects/DISMECH_VISION_ALIGNMENT/tools/apply_review.py`
documents (read its docstring). In short:

```yaml
description: >-
  Project-independent biological summary of the gene product.
status: COMPLETE
groups:                      # one review applied to several rows that make the same claim
  - rows: [0, 1, 2]
    review:
      summary: ...
      action: KEEP_AS_NON_CORE
      reason: ...
      supported_by:
        - reference_id: Reactome:R-HSA-5620914
          supporting_text: "verbatim text from the cached entry"
rows:
  7:
    term: GO:0001750         # must match the row; the script checks it
    summary: ...
    action: ACCEPT
    reason: ...
    supported_by:
      - reference_id: PMID:25664179
        supporting_text: "verbatim text"
references:                  # reference_review and findings for the papers you read
  PMID:25664179:
    findings:
      - statement: ...
        supporting_text: "verbatim text"
    reference_review: {relevance: HIGH, correctness: VERIFIED, review_notes: ...}
core_functions:
  - description: ...
    molecular_function: {id: GO:0008020, label: G protein-coupled photoreceptor activity}
    directly_involved_in:
      - {id: GO:0141190, label: transducin-mediated opsin signaling pathway}
    locations:
      - {id: GO:0120202, label: rod photoreceptor disc membrane}
    supported_by:
      - reference_id: PMID:...
        supporting_text: "verbatim text"
suggested_questions:
  - question: ...
suggested_experiments:
  - hypothesis: ...
    description: ...
```

Then, from the repository root:

```bash
uv run python projects/DISMECH_VISION_ALIGNMENT/tools/apply_review.py <GENE> <decisions file>
just validate human <GENE>
```

Every seeded row must end with a real action; none may stay PENDING. Rows that share a
term must get consistent actions (judge the claim, not the evidence code). Fix every
validation ERROR by correcting the decisions file and merging again. Read each WARNING,
fix the real ones, and list the ones you leave. If you quoted the UniProt file, run
`just backfill-record-sections genes/human/<GENE>` after the final merge and validate
once more. Set `status: COMPLETE` only when no row is PENDING, validation has no errors,
and you would defend each action; otherwise `DRAFT`, saying what is missing.

## Looking up GO terms

- One term: `curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008020"`
- Search: `curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=<words>&limit=15"`
- Ancestors: `.../ontology/go/terms/GO:0008020/ancestors?relations=is_a,part_of`
- Who else carries a term (the comparator check before any NEW process term):
  `curl -s "https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0007601&taxonId=9606&limit=50"`
- `core_functions` ids are validated by branch: `molecular_function` and
  `contributes_to_molecular_function` take molecular functions, `locations` take cellular
  anatomical entities, `in_complex` a protein-containing complex, `directly_involved_in`
  biological processes.

## Things that go wrong on these genes

- Phototransduction proteins carry whole-pathway and whole-organ process terms (`visual
  perception`, `phototransduction`, `response to light stimulus`) from several evidence
  codes at once. A true but broad term is never REMOVE.
- Much of the experimental literature is on the bovine, mouse or frog protein. An ISS or
  IBA row to the human gene can be sound on that basis; say which species was assayed.
- Reactome TAS rows for trafficking steps (Golgi membrane, vesicle membrane, ciliary
  membrane) describe transit of a cargo protein; apply the organelle and transit rules.
- Ensembl Compara IEA transfers from mouse can carry tissue-specific locations.
- Bare `GO:0005515 protein binding`: MODIFY when the cited paper supports a specific
  molecular function, otherwise REMOVE as uninformative, not as false.
- A subunit whose activity belongs to the complex uses `contributes_to_molecular_function`.
- Do not conclude "wrong gene" or "mis-keyed reference" from a title. Record a
  `source_defects` item only when the cached text shows it; otherwise UNDECIDED.
- `knowledge_gaps` are for biological unknowns only, never for curation or ontology gaps.

## What to send back

A plain-text report of at most about 200 words, no file dumps: final `status` and row
counts by action; the core functions as `GO id - label`; anything that looks wrong in
the source record, with its row; what you could not verify and the warnings left; PMIDs
you added to the cache.
