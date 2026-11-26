---
name: sequence-read
description: Optional, opt-in. Read a gene's protein sequence as part of a gene review - Pfam domains with boundaries, transmembrane helices, signal peptide, catalytic residues present or lost, likely function - and reason over it together with the papers, UniProt record and annotations in context. Default mode is the reviewing agent's own in-context read, with every residue it relies on checked by `sequence-read residues`; the isolated blind read (fs2f prompts via peptalk-llm, --context blind, with shuffled and catalytic/decoy controls) is a control that measures what the sequence alone contributes. Results are recorded as a clearly labelled bioinformatics line of evidence, never a substitute for literature.
metadata:
  short-description: Sequence read inside a review, with a blind fs2f control
---

# Reading the sequence in a gene review

The aim, from the fable-sequence-to-function study (fs2f;
<https://github.com/ai4curation/fable-sequence-to-function>, `manuscript.tex`) and
its preprint, is **combined reasoning**. Frontier models can read a protein
sequence: they place Pfam domains, notice a lost catalytic residue and ignore a
matched decoy. A reviewing agent can do the same while it reasons over what it
knows and what is in its context: papers, the UniProt record, the existing
annotations. The skill therefore has two modes:

| Mode | What it is | When |
|---|---|---|
| **A. In-context read (default)** | The reviewing agent reads the sequence alongside the evidence and records sequence-based observations as part of its reasoning, each residue checked by a deterministic command. | Whenever the sequence bears on a decision: a catalytic term on a possible pseudoenzyme, domain boundaries, a TM or signal-peptide claim, an implausible name. |
| **B. Isolated blind read (control)** | The fs2f FEAT and PSEUDO prompts sent as single direct API calls with nothing but `>sequence`, plus shuffled and catalytic/decoy controls. | To measure what the sequence alone contributes, separately from recall and context. Not a substitute for mode A. |

Both are **opt-in** and neither is literature. Mode A costs nothing beyond the review.
Mode B bills three to six model calls per gene.

## What the study found, and what follows for this skill

The settings here are those that worked in fs2f; the limits are the ones it reported.

- **Models and effort.** Fable 5.2 and Opus 5.5 at high effort did well; Opus 4.6
  did not (it invented domains for 28 of 60 shuffled sequences and missed most
  catalytic substitutions outside the kinase Asp). Use `claude-fable-5-2` (the
  default) or `claude-opus-5-5`, at `high` effort. Do not use older models.
- **Domains.** Fable 5.2 named a correct Pfam family for 39 of 45 sampled proteins
  with mean boundary overlap 0.85, and assigned a domain to 1 of 60 shuffled
  sequences. **Obscure DUFs are weak**: Fable 5.2 named the exact family for 8 of 15,
  Opus 5.5 for 3, Gemini 4 Neon for none. An empty or wrong domain list for a DUF
  protein is expected and says nothing.
- **Transmembrane helices** were all recovered, but multi-pass helices were split
  (85 predicted against 74), and shuffled sequences often get a helix (12 of 60):
  composition alone can produce one.
- **Catalytic residues.** Fable 5.2 called all 20 kinase Asp-to-Asn mutants inactive
  and named the substituted position in 57 of 60 mutants. In the decoy control it
  called all 58 decoys active and only 3 of 58 catalytic-site mutants active: the
  call tracks the catalytic position, not any change.
- **Two error patterns** among mutants called active: moving the catalytic role to a
  neighbouring residue of the same type, and reporting the substitution then
  arguing around it. Both end in a confident "active".
- **Recall, not reading.** For a well-studied protein the model usually recognises
  the entry (in our tests it said so: "matches ARH1 from memory"). Its answer is
  then recall of the literature, not independent evidence. The shuffled and decoy
  controls test whether it is reading the residues.
- **No next-residue advantage is needed** for these abilities (Gemini 4 Neon had
  none and still detected substitutions), so the skill does not run the NR test.
- **Function names were right for half or fewer** of recently released structures
  (STRFN test). The skill reports the model's one-sentence function but never treats
  it as evidence.
- **The read can be right where UniProt is wrong** (YrfG Asp16 against UniProt Asp9,
  by alignment and structure), but two cases give no rate. A disagreement with a
  curated site is a lead to check, not a correction.

## Mode A: the in-context read (default)

1. **Read the sequence** from `GENE-uniprot.txt` (the `SQ` block) with the record's
   features, the papers and the annotations in view. Look for the things fs2f showed a
   frontier model can see: domain order and boundaries, hydrophobic stretches that make
   TM helices or a signal peptide, catalytic and cofactor-binding motifs and whether
   each canonical residue is present or replaced.
2. **Check every residue you rely on.** Positions are where reading goes wrong: fs2f saw
   the catalytic role moved to a neighbouring residue of the same type. Run

   ```bash
   uv run ai-gene-review sequence-read residues human ADPRHL1 N58 E304 A306 A307 \
       --note "ARH1 Mg2+-site aspartates" --write
   ```

   Each line states the residue at that position (and whether it matches the one you
   claimed) and the UniProt features covering it. `--write` appends the lines to
   `GENE-bioinformatics/sequence-read/residue-checks.md`. Correct the observation
   rather than the check when they disagree.
3. **Say where the sequence agrees or disagrees with the record.** The value of the
   combined read is in the disagreements, for example a catalytic term on a protein
   whose motif has lost its nucleophile, or a UniProt active site whose alignment
   places it elsewhere (fs2f's YrfG). Put the observation in `review.reason` or the
   notes, say that it is your own reading of the sequence, and cite
   `residue-checks.md` (or a mode-B `RESULTS.md`) for the residues.
4. **Separate reading from recall.** When you know the protein, a "reading" may be
   memory of the literature. Say which it is. If the call matters and you cannot tell,
   run mode B: a blind read that agrees with you shows that the sequence alone supports
   the call.

## Mode B: the isolated blind read (control)

Use [peptalk-llm](https://github.com/ai4curation/peptalk) (`pip install peptalk-llm`,
or `uvx --from peptalk-llm peptalk`). It sends each fs2f prompt as one direct API call
with no system prompt and no tools; with `--context blind` the header is reduced to
`>sequence`; and it checks that the provider counted no input beyond the prompt. It
needs `ANTHROPIC_API_KEY` (or a Gemini or OpenAI key). Do not use the `claude`
command-line tool for the control: it adds context of its own (about 900 input tokens
for a one-sentence prompt), and in our runs its usage record showed a Haiku side call
on every high-effort question.

```bash
uv run ai-gene-review sequence-read blind-fasta human PTEN    # writes GENE-blind.fasta and GENE-probe.fasta
D=genes/human/PTEN/PTEN-bioinformatics/sequence-read
peptalk annotate $D/PTEN-blind.fasta -t features -t active-site --context blind \
    --shuffle-control -o $D/peptalk-blind.jsonl
peptalk annotate $D/PTEN-probe.fasta -t active-site --context blind -o $D/peptalk-probe.jsonl
uv run ai-gene-review sequence-read import-peptalk human PTEN $D/peptalk-blind.jsonl $D/peptalk-probe.jsonl
```

`blind-fasta` takes the probe target from the UniProt `ACT_SITE`, or from `--position N`
when there is none (add `--kinase` for the kinase Asp-to-Asn and Lys-to-Met
substitutions). `import-peptalk` refuses records that were not asked with
`--context blind` or whose prompt is not the fs2f prompt verbatim (peptalk's blind
prompt hashes identically to it). It then runs the same checks as the CLI route and
renders `RESULTS.md`. Default model `claude-fable-5-2` at high effort; keep the JSONL
files beside the run file. Not run live here: peptalk was checked with its stub
provider, which was all this environment allowed (no API key).

### The claude-CLI route (kept for the committed worked examples)

`just sequence-read ORG GENE` asks the same questions through `claude -p` with the
revised fs2f flags (`--tools ""`, empty system prompt, `--setting-sources ""`,
`--strict-mcp-config`, `--disable-slash-commands`, `--no-chrome`) from an empty
temporary directory, and chooses the probe from the model's own wild-type answer when
UniProt has no `ACT_SITE`. It is convenient where there is no API key but is not a
clean blind control, for the reasons above. The worked examples below came from it.

```bash
just sequence-read human ADPRHL1                      # Fable 5.2, high effort, with controls
uv run ai-gene-review sequence-read render human ADPRHL1   # re-render RESULTS.md, no calls
```

### Questions asked

| Question | Condition | Purpose |
|---|---|---|
| FEAT | real | Pfam domains + boundaries, TM helices, signal peptide, name, EC, function |
| FEAT | shuffled | Control: same composition, seeded by the accession's CRC32 (as fs2f) |
| PSEUDO | wild type | Catalytic residues present, residues lost, active yes/no/uncertain |
| PSEUDO | catalytic mutant | Probe: one catalytic residue substituted |
| PSEUDO | decoy | Control: the same substitution at an unannotated residue of the same type |

The prompts are the fs2f strings verbatim (a test pins their SHA-256). The probe
target is the UniProt `ACT_SITE`, else a residue the model itself named and that is
really present at that position, preferring a stated catalytic role, then an acidic
residue UniProt annotates as `BINDING` (a metal ligand), then list order.
The substitution is Asp to Asn and Lys to Met for kinases, otherwise Ala. The decoy
follows the fs2f rule: same residue type, inside the same UniProt `DOMAIN` when there
is one, at least 3 residues from any annotated site or model-named residue, outside
cleaved peptides, drawn with a seeded generator. The probe runs only when the wild
type is called active.

### Outputs

`genes/ORG/GENE/GENE-bioinformatics/sequence-read/`:

- `residue-checks.md` - mode A: residues checked during an in-context read.
- `MODEL-EFFORT-peptalk-blind.json` (peptalk) or `MODEL-EFFORT.json` (claude CLI) - the run file: sequence checksum and version, route, every
  prompt hash, reply text, parsed answer, token counts per model, and the checks.
  A second run for the same model and effort is refused without `--force`.
- `RESULTS.md` - rendered from all run files, one finding per line so it can be
  quoted. Nothing in it is typed by hand.

For the claude-CLI route the `claude` tool's usage record can list a second model (in
our runs `claude-haiku-5-5` on every high-effort call, but not on a one-sentence
low-effort canary). The page says so and checks that the reply is one turn whose token
counts are the requested model's; if that check fails for a call, do not rely on it.

## Reading the results

| Line in RESULTS.md | How to read it |
|---|---|
| Pfam `MATCH`, IoU >= 0.8 | Corroborates the domain call and boundaries. |
| Pfam `IN_UNIPROT_NOT_INTERPRO` | UniProt and InterPro are on different Pfam releases; not an error by the model. |
| Pfam `NOT_IN_REFERENCE` | A domain no reference has. Treat as a possible hallucination unless an alignment supports it. |
| Shuffled control `FAILS` | Discard the domain calls of this run. |
| Named residue `NOT in the sequence` | The model misread or misremembered the position; discount its residue claims. |
| Reported lost residue that matches the sequence | A lead that a canonical catalytic or cofactor residue is absent; check it with an alignment to active relatives. |
| Probe `TRACKS_CATALYTIC_RESIDUE` | The catalytic mutant was called inactive and the decoy active: the model is reading that residue. |
| Probe `REPORTS_BUT_NOT_INACTIVE` | The model named the substituted position but still called the mutant active or uncertain: the fs2f pattern of seeing a loss and arguing around it. It reads the residue but its activity calls are not reliable. |
| Probe `REJECTS_ANY_CHANGE` | The decoy changed the call too; the activity calls of this run are not residue-specific. |
| Probe `INSENSITIVE` | Neither changed the call; it is probably recall. Give its activity call no weight. |
| Probe not run, wild type inactive | Expected for a pseudoenzyme or a non-enzyme; the lost-residue lines are the result. |

## Recording it in the review

The schema already allows this as a bioinformatics reference; no schema change is
needed. In mode A the observation itself lives in the review's reasoning
(`review.reason`, `core_functions` description, notes), written as your own reading of
the sequence; the reference is `residue-checks.md`, with title
`'GENE: residues checked during an in-agent sequence read'`, and its quotes are the
checked lines. In mode B, cite `RESULTS.md` as below.

1. Add the page to `references:`:

   ```yaml
   - id: file:human/ADPRHL1/ADPRHL1-bioinformatics/sequence-read/RESULTS.md
     title: 'ADPRHL1: sequence-only language-model read'
     publication_type: BIOINFORMATICS
     reference_review:
       relevance: LOW            # MEDIUM at most, and only if the probe and controls pass
       correctness: VERIFIED     # you checked the cited lines against the sequence
       review_notes: Sequence-only read by claude-fable-5-2 (high effort), FEAT and PSEUDO
         prompts of fable-sequence-to-function; not literature. The model recognised the
         protein, so its lost-residue calls are partly recall.
   ```

2. Quote **the check lines**, not the model's prose (`Model function:` and `Model
   reason:` lines are the model's own words and are not evidence). Good quotes:
   `Reported lost residue: ... expected D, found N at 58 (matches the sequence).`,
   `Probe verdict: TRACKS_CATALYTIC_RESIDUE`, `Predicted Pfam PF03747 ... MATCH ...`.
   `just validate-quotes` checks them against the file.

3. Use it only as **additional** support, in this order of strength:
   - It may **flag**: a catalytic term on a protein whose read reports lost catalytic
     residues, or an implausible name. A flag motivates `UNDECIDED`, a
     `suggested_questions` entry, or a check of the catalytic term; with independent
     evidence (an alignment you ran, a curated feature, a paper) it can support
     `MARK_AS_OVER_ANNOTATED` or `REMOVE` of an electronic catalytic term.
   - It may **corroborate** domain and boundary calls that other sources make.
   - It is **never the sole support** for `ACCEPT`, `NEW`, a `core_functions` entry,
     or a source defect. It cannot show a protein is inactive (residues can be
     displaced, as in WNK1), nor that intact motifs mean activity (kin-32), and a lost
     catalytic residue says nothing against a non-catalytic function.

4. Add a history record (`just new-history --kind gene ...`) for every gene whose run
   you commit, cited in its review or not: `docs/history.md` puts any session on a file
   in the gene folder, bioinformatics included, under the gene's target. Note the run in
   `GENE-notes.md` when the gene has one.

A possible schema refinement, not yet made: a dedicated `publication_type` value for
model reads (for example `SEQUENCE_MODEL_READ`) would let reports separate them from
other bioinformatics. Until then the folder name `sequence-read/` and the title
suffix `sequence-only language-model read` identify them; keep both.

## Worked examples (2026-11-25, Fable 5.2, high effort, claude-CLI route)

**These were not blind tests.** The model said or implied that it recognised all four
proteins, so the runs show that the pipeline and its checks work; they do not show what
the sequence alone contributes. That needs the mode-B control on proteins the model
does not know.

| Gene | Kind | Result |
|---|---|---|
| PTEN (P60484) | well studied | PF10409 C2 at IoU 0.99; the phosphatase domain named as PF22785, which the UniProt record lists but InterPro now gives as PF22784 (`IN_UNIPROT_NOT_INTERPRO`); Cys124 named (UniProt ACT_SITE); C124A called inactive with the position reported, decoy C83A called active: `TRACKS_CATALYTIC_RESIDUE`. |
| ADPRH (P54922) | active paralog | PF03747 at IoU 0.94; six Mg2+-site residues named, all UniProt BINDING; no ACT_SITE, so the probe took the acidic BINDING residue Asp55: D55A called inactive with the position reported, decoy D255A active: `TRACKS_CATALYTIC_RESIDUE`. |
| ADPRHL1 (Q8NDY3) | catalytic-dead paralog | Called inactive; reported lost aspartates at 58 (Asn), 304 (Glu) and 306 (Ala), each matching the sequence. That is the aspartate-only count of PMID:27217161; the review's own donor census keeps Glu304 and scores Ser305 to Ala307 as lost, which the read does not mention. Recorded in the review as a LOW-relevance reference (see `genes/human/ADPRHL1`). |
| C7orf25 (Q9BPX7) | obscure, two DUFs | Both DUFs (PF18474, PF07000) named, IoU 0.91 and 0.98; activity "uncertain", no residues named, so no probe. |

All controls passed (one transmembrane helix was predicted on the shuffled ADPRHL1
sequence, as fs2f saw for 12 of 60). Cost was US$0.19 to 0.50 per gene. The ADPRHL1 case
shows why the check lines matter: a read can agree with one published reading of a
site and not with another, and the review has to say which.

See each gene's `GENE-bioinformatics/sequence-read/RESULTS.md` for the run.
