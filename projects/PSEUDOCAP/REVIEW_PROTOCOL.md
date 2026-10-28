# PseudoCAP IBA-seed review protocol

Brief for reviewing one *P. aeruginosa* PAO1 gene from
[`iba_seed_worklist.yaml`](iba_seed_worklist.yaml). Read the repository
`CLAUDE.md` first; everything below is in addition to it.

## Context

PseudoCAP annotations on PAO1 genes are seeds for PAINT IBD node annotations.
An error in a seed is copied as an IBA to every leaf below the node. The
worklist entry for the gene lists each PAINT node it seeds, the node term, the
number of seeds (`n_seeds`; `sole_seed: true` means the IBD rests only on this
gene), the leaf IBA count, and the experimental annotations that support the
seeding.

## Steps

1. `just fetch-gene PSEAE <symbol>` (re-run if EBI times out). Check that the
   fetched UniProt accession matches the worklist. If a symbol is ambiguous or
   missing, use the locus tag or the accession as the folder name.
2. Read the UniProt file, the GOA file, and the cached `publications/PMID_*.md`
   for every cited PMID. Many are abstract-only: use the PubMed MCP
   (`mcp__PubMed__get_full_text_article`, `mcp__PubMed__search_articles`) for
   full text where possible. Do not write files into `publications/` by hand.
3. No deep-research provider keys are available. Do your own literature research
   and write it into `<GENE>-notes.md` with inline provenance. Never create a
   `-deep-research-<provider>.md` file.
4. Write the full review: description, references (with `reference_review` for
   the PseudoCAP-cited papers), every existing annotation with an action,
   `core_functions`. Follow the CLAUDE.md rules on IBAs, on not overruling
   curators from incomplete evidence (prefer `UNDECIDED` to `REMOVE` for a paper
   you cannot read, unless the abstract itself shows the claim is an indirect
   phenotype), on protein binding, and on `NEW`.
5. **Seed assessment.** For each PseudoCAP annotation that seeds an IBD, decide
   whether the paper directly supports that term for this gene, and so whether
   the IBD is sound. The typical failure is a mutant phenotype (lost motility,
   reduced enzyme activity in a lysate, less pigment) annotated as the gene's
   own molecular function or process. Also judge whether the node term suits a
   clade of that size and breadth.
   - A wrong PseudoCAP row gets `review.source_defects` with
     `resource: PSEUDOCAP` (see `docs/source_defects.md`).
   - If that leaves the IBA on this gene unsupported, review the IBA row
     accordingly and add a defect with `resource: GO_CENTRAL` naming the PTN
     node.
   - Add `## PseudoCAP IBA-seed assessment` to the notes with a table:
     PTN node | node term | n_seeds | leaf IBAs | seed annotation (term,
     evidence, PMID) | verdict | rationale. Verdicts: `SOUND`,
     `OVER-SPECIFIC`, `INDIRECT-PHENOTYPE`, `WRONG`, `UNVERIFIABLE`.
6. `just validate PSEAE <GENE>` and
   `just backfill-record-sections genes/PSEAE/<GENE>`; fix all errors and the
   warnings you reasonably can.
7. History record:
   `uv run python scripts/new_history.py --kind gene --organism PSEAE --slug <GENE> --event REVIEW --summary "..." --details "..." --sections existing_annotations,core_functions,references --agent-tool claude-code`,
   then `just validate-history <path>`.
8. Edit only `genes/PSEAE/<GENE>/`, `history/`, and `publications/` (through
   the tooling). Do not commit.

## Report back

Under 300 words: per seeding node, the verdict and a one-line reason; action
counts; validation warnings left; anything you could not verify.
