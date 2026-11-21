---
name: pm
description: Manage and drive forward an ongoing project, tracked in projects/ dir
argument-hint: "[PROJECT_NAME]"
---

You should find either a file or a folder:

./PROJECT_NAME.md
./PROJECT_NAME/
   <multiple materials>

A project doc typically will contain a list of genes, potentially prioritized. This should be in the form of a checkbox you can check off.
The species for the gene (uniprot code or lowercase name like 'mouse') should be clear (if not, ask)

Review the genes in the priority order.

IMPORTANT: you MUST consult the annotation-reviewer.md subagent for this task.

If the user specifies a deep research provider(s), make sure to perform deep research using at
least this provider(s), otherwise default to falcon.

E.g. `just deep-research-falcon ORGANISM GENE_SYMBOL`

You can edit sub-pages under `projects/PROJECT_NAME/` for analysis notes, but
do not tick checkboxes or otherwise update the top-level `projects/PROJECT_NAME.md`
status page as genes finish inside a content PR. Record in-progress status in
gene notes and append-only history instead; update the top-level project page in
a separate status PR once the corresponding content has merged. After the main
description have something like:

---
# STATUS

<checkboxes etc here; keep this up to date>
<get the date from `date`>

# NOTES

## YYYY-MM-DD

<todays notes, add here>

## YYYY-MM-DD

<previous session notes, generally don't edit unless this is a direct continuation>
---


## Making PRs

ONLY make PRs when asked.

The general procedure is:

1. ensure everything validates `just validate-all`
2. make a branch
3. commit genes related to project, plus all references
4. `gh pr create`

Do not commit rendered `pages/**` HTML in the content PR. The Pages workflow
will render project pages from `main` after the PR lands. If the user asks,
build the static site and stats (`just stats`, `just update-browser-data`), but
stage only the source files owned by this project.
