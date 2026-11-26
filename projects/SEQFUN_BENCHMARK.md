---
title: "Sequence-to-function benchmark: blind, organism and agent-review conditions"
maturity: IN_PROGRESS
collections: [FUNCTION_PREDICTION]
tags: [EVALUATION, PIPELINE]
index_group: CROSS_CUTTING
description: Time-split, leakage-checked GO benchmarks comparing a blind sequence read with combined reasoning in a reviewing agent.
species: [human]
autolink_gene_symbols: false
---

# Sequence-to-function benchmark (SEQFUN)

**Bottom line so far:** the pipeline runs end to end for all three kinds of
condition on the 24-protein example benchmark, at a total cost of about $36.
The first numbers cannot answer the project's question yet. Every target
predates the models' training cutoffs, so the example is a pipeline test.
The peptalk conditions and the agent-review condition also measure different
things: peptalk asks the model yes or no about each target term, while a
review must come up with the term unprompted. The agent-review result (10 of
50 targets) is a recall floor for open-ended annotation. It is not evidence
that reading the literature makes a model worse.

## Aim

To robustly expand the analysis of Mungall and Joachimiak,
[arXiv:2611.28529](https://arxiv.org/abs/2611.28529), *General-purpose
language models are neurosymbolic reasoners able to annotate proteins from
sequence*. The preprint found that frontier generalist models perform well
above chance at annotation tasks from sequence alone: Pfam domain presence and
coordinates, loss of catalytic residues, structure and activity. It used small,
hand-built task sets.

This project asks the same kind of question on time-split, leakage-checked GO
benchmarks, and compares, item by item:

| condition | what the predictor sees | tool |
|---|---|---|
| `blind` | the sequence only, with a shuffled-sequence control | `peptalk ask --context blind` |
| `organism` | the sequence plus the organism | `peptalk ask --context organism` |
| `full` | the sequence plus the UniProt-style header | `peptalk ask --context full` (not run yet) |
| `agent-review` | combined reasoning: an ai-gene-review agent reads the sequence (the `sequence-read` skill, combined mode) together with the literature, UniProt and baseline annotations | the normal review workflow, seeded with baseline-release GOA |

The question is how much of a correct annotation comes from reading the
sequence, and how much from recalling or retrieving knowledge about the named
protein. Decoy terms and shuffled sequences measure how often a predictor says
yes regardless.

The machinery is the `benchmark-builder` skill
(`.claude/skills/benchmark-builder/`), `ai-gene-review benchmark` and
[docs/benchmarks.md](../docs/benchmarks.md).

## Benchmarks owned

| benchmark | proteins | targets | decoys | baseline → current GO release | fair for |
|---|---|---|---|---|---|
| [`benchmarks/human-goa-2025-06`](../benchmarks/human-goa-2025-06/) | 24 human (20 random, 4 pseudoenzymes) | 50 targets + 1 NOT target | 72 | 2025-06-01 → 2026-08-05 | no current frontier model: all target papers predate the June 2026 cutoff. It is a pipeline test. |

## Runs

### Peptalk blind and organism, Fable 5.2 and Opus 5.5 (2026-11-26)

These were direct API calls at high effort on 123 claims, with shuffled-sequence
controls in the blind conditions. They cost $22.04 by peptalk's log, canaries
included. Details are in
`.claude/skills/benchmark-builder/references/example-results.md`. The raw
JSONL lives in the git-ignored `benchmarks/human-goa-2025-06/runs/`.

### Agent review, Opus 5.5 (2026-11-26)

Each of the 24 genes was reviewed by headless Claude Code (`claude -p --bare`,
`claude-opus-5-5`, effort `high`) in its own sandbox outside the repository.
Each sandbox held only what was available on 2025-06-01
([scripts/agent_review_sandbox.py](SEQFUN_BENCHMARK/scripts/agent_review_sandbox.py)):

- the baseline-release GOA file from `benchmark export`, which contains none of the targets;
- the UniProt entry version current on 2025-06-01, from UniSave (for example, GSK3B v271, PLD5 v163);
- a review stub seeded from that GOA file with `ai-gene-review seed-goa`;
- cached papers cited by the baseline GOA and published before 2025;
- the `sequence-read` skill, an offline GO term lookup, and the residue checker.

Web tools and MCP servers were disabled. The prompt
([scripts/agent-review-prompt.md](SEQFUN_BENCHMARK/scripts/agent-review-prompt.md))
forbade network access and reading outside the sandbox, and asked the agent to
mark recalled claims. An audit of every tool call
([scripts/summarize_agent_runs.py](SEQFUN_BENCHMARK/scripts/summarize_agent_runs.py))
found no network commands and no reads outside the sandbox. The per-gene
model, effort, cost, turns, action counts and audit are in
[agent-review-runs.yaml](SEQFUN_BENCHMARK/agent-review-runs.yaml). The
reviews live in the git-ignored `benchmarks/human-goa-2025-06/runs/agent-review/genes/`.
They are not production reviews and were never written to `genes/`.

**Cost: $14.33 for 24 genes** ($0.23 for TGDS to $1.06 for MYD88). Claude Code
billed a small part of that to Haiku 5.5 for its own housekeeping calls.

### Comparison

The scores are in
`benchmarks/human-goa-2025-06/human-goa-2025-06-scores.{yaml,md}`. The full
per-target table is
[human-goa-2025-06-comparison.md](SEQFUN_BENCHMARK/human-goa-2025-06-comparison.md),
made by [scripts/compare_conditions.py](SEQFUN_BENCHMARK/scripts/compare_conditions.py).

| condition | targets yes | NOT target yes | decoys yes |
|---|---|---|---|
| blind, Fable 5.2 | 32/50 | 1/1 | 1/72 |
| organism, Fable 5.2 | 31/50 (1 missing, refused) | 1/1 | 1/72 |
| blind, Opus 5.5 | 28/50 (5 uncertain) | 1/1 | 3/72 (6 uncertain) |
| organism, Opus 5.5 | 28/50 (7 uncertain) | 1/1 | 6/72 (3 uncertain) |
| agent-review, Opus 5.5 | 10/50 | 1/1 | not asked |

| condition | C targets | F targets | P targets |
|---|---|---|---|
| blind, Fable 5.2 | 8/11 | 11/15 | 13/24 |
| blind, Opus 5.5 | 5/11 | 10/15 | 13/24 |
| agent-review, Opus 5.5 | 4/11 | 2/15 | 4/24 |

How to read it:

- **The tasks differ.** A peptalk run is asked "does this protein have
  function X?" for each target and decoy, so naming the term is itself a hint.
  A review is asked nothing about the targets. It scores yes only when a kept
  row, a NEW row or a core function entails the target term. Reviews are never
  asked about decoys, so the agent-review decoy rate is not measured. Compare
  agent-review with the others on targets only, and read its 10/50 as recall
  in open-ended annotation.
- **The agent did well where the target extends known biology:** SLC25A16
  mitochondrial CoA transport, SUCLG1 succinate-CoA ligase, SKIC2 non-stop
  decay, ERLEC1 Hrd1 complex, POPDC2 heart rate, TRIM28 chromatin, MRGPRE
  plasma membrane, and WHR1 (STK19) transcription-coupled repair. For WHR1 it
  said it was recalling 2024–early-2025 papers, so the knowledge predated the
  2025-06 baseline, even though the GO annotation did not ("new to GO is not
  new knowledge").
- **It missed targets that report genuinely new findings**, such as MPO
  nucleosome disassembly, LAMP2 ferroptosis and STING1 cholesterol and
  PI(3,5)P2 binding. The peptalk runs said yes to most of these when asked
  directly. That is consistent with recognition from the question plus recall
  of the target papers (all published before the models' cutoffs), and cannot
  be told apart from it here.
- **Every condition said yes to TGDS's NOT target**, dTDP-glucose
  4,6-dehydratase activity. The agent kept the baseline IBA row for it,
  citing family membership and retained catalytic residues.

## Leakage risks

- **Training cutoff.** All 51 target papers predate the June 2026 cutoff of
  Opus 5.5 (`reference_recency` WARN on every target). Fable 5.2's cutoff is
  not recorded. Every condition may recall the target papers. This is a
  pipeline test.
- **Agent-specific: literature search can find the target paper.** A normal
  review fetches current UniProt and GOA (which contain the targets) and runs
  deep research and PubMed searches, which can retrieve the very paper behind
  a target. This run closed those routes: baseline GOA only, the UniProt entry
  version of 2025-06-01, pre-2025 cached papers only, and no network, checked
  by the audit. Recall from training remains open, and the agent was asked
  only to flag it, not to avoid it.
- **Names and symbols.** The sandbox folders and prompts use current gene
  symbols. WHR1 was STK19 at baseline, so the prompt gave the agent a symbol
  that did not exist on 2025-06-01. The UniProt entry version itself carries
  the baseline name (STK19, "Inactive serine/threonine-protein kinase 19").
- **Ontology version.** The offline GO lookup used the current GO (2026-11),
  so terms created after the baseline were visible to the agent.

## Next steps

1. **A fair test needs a post-cutoff GO release.** Draw a benchmark whose
   targets rest on papers published after the reviewing model's training
   cutoff (for Opus 5.5, after June 2026), using a baseline release at the
   cutoff and the first GO release that accumulates enough new experimental
   annotations after it. Rerun all conditions on it.
2. **Make the tasks comparable.** Either ask the agent the peptalk claims at
   the end of its review (recognition with combined reasoning), or score the
   peptalk conditions by open generation. Both are needed to separate reading
   the sequence from being prompted with the answer.
3. **Decoys across GO aspects.** Decoys are currently drawn from other items'
   targets. Draw them per aspect (C, F, P), matched for specificity, so that
   a yes rate on decoys can be compared aspect by aspect with targets.
4. **Run the `full` peptalk condition and a Fable 5.2 agent review** on the
   same benchmark (Fable cost 2 to 4 times as much as Opus in the peptalk runs).
5. **Bigger samples.** With 50 targets the blind versus organism differences
   (one target here and there) are within noise.

## Reproducing

```bash
just benchmark-export benchmarks/human-goa-2025-06/human-goa-2025-06.yaml
uv run python projects/SEQFUN_BENCHMARK/scripts/agent_review_sandbox.py \
    benchmarks/human-goa-2025-06/human-goa-2025-06.yaml SANDBOX_ROOT
sh projects/SEQFUN_BENCHMARK/scripts/run_agent_review.sh SANDBOX_ROOT GSK3B P49841 claude-opus-5-5 high 4
# copy SANDBOX_ROOT/*/genes/human/* to benchmarks/human-goa-2025-06/runs/agent-review/genes/human/
just benchmark-score benchmarks/human-goa-2025-06/human-goa-2025-06.yaml \
    --peptalk runs/blind-claude-fable-5-2.jsonl ... \
    --reviews-dir benchmarks/human-goa-2025-06/runs/agent-review/genes
```

`run_agent_review.sh` takes the API key from `GO_ANTHROPIC_API_KEY`.
