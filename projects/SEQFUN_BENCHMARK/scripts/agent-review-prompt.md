# Agent-review benchmark condition: review {GENE} as of {BASELINE}

You are writing an ai-gene-review gene review of human {GENE} (UniProtKB:{ACC})
under a benchmark condition. Pretend the date is {BASELINE}. Everything in this
folder is what was available then:

- `genes/human/{GENE}/{GENE}-goa.tsv`: the GO annotations in the {BASELINE} GO release.
- `genes/human/{GENE}/{GENE}-uniprot.txt`: the UniProt entry version current on that date
  (with its `SQ` sequence block).
- `genes/human/{GENE}/{GENE}-ai-review.yaml`: a stub seeded from that GOA file, every row
  `action: PENDING`. This is the file you complete.
- `publications/`: cached papers cited by those annotations and published before
  {BASELINE_YEAR}.

## Rules of the condition (do not break them)

- **No network.** Do not use curl, wget, Python requests or any web tool. Do not
  query UniProt, QuickGO, PubMed, Europe PMC or any other service.
- **Stay in this folder.** Do not read files outside it.
- You may use what you know of the biology from your training, but in `reason`
  and `summary` say when a claim is recalled rather than read in a file here.
  Do not rely on work you know to be published after {BASELINE}.
- Never guess a GO identifier. Look terms up with
  `python3 tools/go_term.py search "text"` and `python3 tools/go_term.py info GO:NNNNNNN`.

## What to do

1. Read the UniProt entry, the GOA file and the stub, and skim the relevant papers.
2. **Read the sequence yourself** (the `sequence-read` skill, combined mode, in
   `.claude/skills/sequence-read/SKILL.md`): domains, catalytic and binding residues
   kept or lost, signal peptide, TM segments, motifs. Check every residue you rely
   on with `sh tools/residues.sh human {GENE} D58 ... --note "..." --write`. Skip the
   optional blind control (no peptalk).
3. **Give every existing row an action**: ACCEPT, KEEP_AS_NON_CORE, MODIFY (with
   `proposed_replacement_terms`), MARK_AS_OVER_ANNOTATED, REMOVE, TOO_GENERAL or
   UNDECIDED, with a one-sentence `summary` and `reason`. Rows on the same term
   should get the same action. Bare `GO:0005515` protein binding is REMOVE. For a
   gene with many rows, write a short Python script that sets actions by term
   rather than editing each row by hand.
4. **Add `NEW` rows** for functions (MF, BP, CC) you judge well supported (by the
   literature and the sequence together) but missing from the GOA file. Be
   conservative; do not add indirect or pleiotropic effects. A NEW row has
   `term`, `evidence_type: IC` (or ISS/IEA as appropriate), `original_reference_id`
   (a PMID in `publications/` or `GO_REF:0000024`), and `review` with
   `action: NEW`, `summary`, `reason`.
5. **Write `description`** (a standalone biological summary) and **`core_functions`**:
   one entry per core activity with `description`, `molecular_function` (`id`,
   `label`), and where applicable `directly_involved_in` and `locations` (lists of
   `id`/`label`).
6. Check the YAML loads: `python3 -c "import yaml;yaml.safe_load(open('genes/human/{GENE}/{GENE}-ai-review.yaml'))"`.

Finish with a two-line summary: the core functions you settled on and any NEW rows.
Be efficient: this run has a fixed budget.
