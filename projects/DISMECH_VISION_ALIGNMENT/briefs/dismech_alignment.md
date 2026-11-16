# Brief: align dismech vision-disorder entries with the reviewed function of their genes

You work in the repository `/home/user/dismech` on a short list of disorder entries
(`kb/disorders/<Entry>.yaml`). A coordinator commits the results; you never touch git.

The campaign: dismech's Mendelian non-syndromic vision disorders are being checked
against the normal function of their causal genes as reviewed in the sister repository
`/home/user/ai-gene-review` (read-only for you). dismech models what goes wrong; the gene
review records what the gene product normally does. The two should say compatible things,
and a dismech entry should carry the chain **gene -> molecular function -> process** on
its mechanism graph instead of only naming the gene in its `genetic:` section.

## Hard rules

- Edit only the entries you were given, plus the `history/` record for each. Tool-written
  cache files (`references_cache/`, `cache/**/*.csv`) may change as a side effect of the
  recipes below; never hand-edit them. Do not edit anything in `/home/user/ai-gene-review`.
- No git commands that change state. No installs, no `uv sync`.
- Never write an ontology identifier or its label from memory. Look it up in the same
  step you write it (`cache/<prefix>/terms.csv`, OLS, or QuickGO:
  `curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008020"`), and
  copy the label exactly. HGNC CURIEs are lowercase `hgnc:`.
- Never add or change an evidence `snippet` unless it is an exact substring of the cached
  reference. Cache a reference only with `just fetch-reference PMID:<n>`.
- Do not add a claim the entry's evidence does not support. Binding a gene and a GO term
  to a node whose description and evidence already state that activity is annotation of
  an existing claim and needs no new evidence. A new node, a new edge or a changed claim
  needs its own evidence item.
- Prose in `description`, `notes` and `explanation` is about the disease, for a reader who
  has never seen this session. No process narration ("review round", "the audit found").
- Read `/home/user/dismech/CLAUDE.md` before editing, at least: "Evidence Items",
  "Ontology Term Contract", "Gain/Loss of Function: which slot?", "Pathograph Targets Are
  Bare Names", "Two Rows With One Name Are One Node", "A Gene Binding Only Has To Be
  Self-Consistent", "Gene-Disease Validity Is Copied, Never Assigned", "History Records",
  "YAML Formatter Safety", and "Evidence and Reference Workflow". Use the
  `.claude/skills/dismech-terms/SKILL.md` and `.claude/skills/dismech-references/SKILL.md`
  procedures when you bind a term or touch evidence.

## What to check and repair in each entry

For each causal gene of the entry, read the gene review at
`/home/user/ai-gene-review/genes/human/<GENE>/<GENE>-ai-review.yaml`: its `description`,
its `core_functions` (molecular function, process, location, complex) and its `status`.
A review that is not COMPLETE is weaker guidance; say so in your report.

1. **Gene records (`genetic:`).**
   - `relationship_type` must be set. `CAUSATIVE` means an established Mendelian cause;
     use `DISPUTED` or `REFUTED` when the entry's own evidence says so. Run
     `just list-gene-validity kb/disorders/<Entry>.yaml` and read what ClinGen holds:
     a `backfill` row may be recorded as `gene_disease_validity` exactly as CLAUDE.md
     describes (tier copied, `CGGV:` record quoted); an `overstated` row means
     `CAUSATIVE` is stronger than ClinGen's tier and needs a decision. Never assign a
     tier yourself.
   - `variant_origin: GERMLINE` where the causal variants are constitutional.
2. **The gene on the mechanism graph.** The node that states what the gene product fails
   to do should carry the gene (`genes:` with the lowercase `hgnc:` CURIE and exact
   symbol) and a `molecular_functions:` term for that activity, with the right `modifier`
   (read "Gain/Loss of Function: which slot?"; `DECREASED` is the default for a loss) and
   a `genetic_context` where the entry's evidence supports the functional impact. Prefer
   the same GO molecular function term as the gene review's core function, when that
   term is what the node actually claims. Where the gene review says the gene only
   contributes to a complex's activity, bind the activity only if the node is about the
   complex, and say in the node description that the subunit is non-catalytic or
   regulatory. If no existing node states the gene's molecular dysfunction, add one only
   with evidence; otherwise report it.
3. **Agreement.** Compare what the entry says the gene product does (activity, location,
   complex, process) with the gene review. Where they disagree, read the cited evidence
   on both sides and decide. Fix dismech when dismech is wrong. When the gene review
   looks wrong or incomplete, do not edit it: report the row and the evidence.
4. **Do not widen the task.** Leave phenotypes, treatments, prevalence and other
   sections alone unless you find an error there while reading; report such errors
   instead of fixing them, unless the fix is a one-line identifier or label repair.

## Validate

After each entry edit:

```bash
just validate kb/disorders/<Entry>.yaml
just validate-terms kb/disorders/<Entry>.yaml
just count-verified-snippets kb/disorders/<Entry>.yaml
just check-causal-targets kb/disorders/<Entry>.yaml
just check-entity-refs kb/disorders/<Entry>.yaml
just check-duplicate-keys kb/disorders/<Entry>.yaml
just check-block-scalar-comments kb/disorders/<Entry>.yaml
just check-enum-values kb/disorders/<Entry>.yaml
just list-gene-term-mismatches kb/disorders/<Entry>.yaml
```

When all your entries are done: `just normalize-cache`, `just check-cache-order`,
`just check-gene-activity-grounding`, `just check-snippet-grading`, and once
`just validate-disorders <all your entry files>`. Report any failure you could not fix.

## History record

For each entry you changed, scaffold a record (never hand-write the filename) and edit
its `details`:

```bash
just new-history --help
just new-history --kind disorder --slug <Entry> --event <EVENT> --outcome changed \
  --summary "<short summary>" --agent-tool claude-code \
  --sections genetic,pathophysiology --details "<what was changed and how it was validated>"
just validate-history <printed path>
```

Do not pass a model name.

## What to send back

A short plain-text report, at most about 300 words, no file dumps. Per entry: what you
changed (gene record typing, node, GO term and modifier); any disagreement between the
entry and the gene review and how you resolved it; anything in the gene review that
looks wrong, with the evidence; validation result; anything left undone and why.
