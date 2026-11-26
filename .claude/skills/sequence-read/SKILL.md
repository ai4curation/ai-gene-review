---
name: sequence-read
description: Optional, opt-in, frontier models only. During a gene review, read the protein sequence yourself and reason over it together with the papers, UniProt record and annotations in context - catalytic and binding residues retained or lost, domain architecture, signal peptide and TM segments, motifs, low-complexity regions - checking every residue you rely on with `ai-gene-review sequence-read residues`. Optionally run a blind control (fs2f prompts via peptalk-llm, --context blind) to measure what the sequence alone supports. Use for catalytic terms on possible pseudoenzymes, domain or topology claims, and implausible names. A sequence read never justifies an annotation action on its own.
compatibility: Requires a frontier model as the reviewing agent (Claude Fable 5.2 or Opus 5.5 class; older and smaller models invent domains and miss catalytic substitutions). Needs the ai-gene-review repository with uv. The blind control needs peptalk-llm (run with uvx) and an Anthropic, Gemini or OpenAI API key.
model: claude-fable-5-2
metadata:
  requires_frontier_model: "true"
  frontier_models: "claude-fable-5-2, claude-opus-5-5"
  short-description: "Read the sequence inside a gene review, with a blind fs2f control"
---

# Reading the protein sequence in a gene review

Use this skill only if you are a frontier model. If you are not, stop: do not read the
sequence, and do not run the blind control on a non-frontier model either.

## When to use it

- A catalytic or binding molecular-function term may sit on a protein that has lost
  the residues the activity needs (a possible pseudoenzyme, a dead paralog).
- A domain, transmembrane, signal-peptide or localisation claim depends on the
  sequence.
- A protein name or annotation looks implausible for the sequence.
- UniProt places an active site where the sequence suggests it is not.

## When not to use it

- To supply an annotation the literature does not support. A sequence read is a
  bioinformatics line of evidence, never literature.
- For an obscure DUF protein's family or function: models usually cannot name these,
  so an empty or confident answer says nothing.
- For a routine review where nothing turns on the sequence.

## Steps

1. **Read the sequence yourself** from the `SQ` block of `GENE-uniprot.txt`, with its
   `FT` features, the papers and the existing annotations in view. Look for:
   - catalytic and binding residues retained or lost, compared with UniProt
     `ACT_SITE`/`BINDING` and with active paralogs or orthologs;
   - domain architecture and boundaries, compared with Pfam/InterPro;
   - signal peptide, transit peptide and transmembrane segments;
   - known motifs (P-loop, HRD/DFG, CxxC, HxK and so on) and whether each is intact;
   - low-complexity, coiled-coil or disordered stretches that limit what can be said.
2. **Check every residue you rely on.** Catalytic roles are easily misplaced onto a
   neighbouring residue of the same type. Run:

   ```bash
   uv run ai-gene-review sequence-read residues ORG GENE N58 E304 A306 \
       --note "what you are checking" --write
   ```

   Each line gives the residue at that position, whether it matches your claim, and the
   UniProt features covering it. The command exits non-zero on a mismatch; fix your
   observation, not the check. `--write` appends the lines to
   `GENE-bioinformatics/sequence-read/residue-checks.md`.
3. **Record what you see and how it bears on each annotation**, in that row's
   `review.reason` (or the notes). Say whether it supports or contradicts the term,
   and say that it is your own reading of the sequence. Say where you are recalling the
   protein rather than reading it.
4. **Never let the sequence read alone justify an action.** It can flag a term
   (`UNDECIDED`, a `suggested_questions` entry), or support `MARK_AS_OVER_ANNOTATED` or
   `REMOVE` of an electronic catalytic term together with independent evidence (an
   alignment, a curated feature, a paper). It is never the sole support for `ACCEPT`,
   `NEW`, a core function or a source defect. A lost catalytic residue does not prove
   inactivity, intact motifs do not prove activity, and a dead enzyme may still have a
   non-catalytic function.
5. **Cite the checked file, not your prose.** Add a `references:` entry
   `file:ORG/GENE/GENE-bioinformatics/sequence-read/residue-checks.md`, with title
   `'GENE: residues checked during an in-agent sequence read'`, `publication_type:
   BIOINFORMATICS` and `relevance: LOW` (`MEDIUM` at most). Quote its checked lines as
   `supporting_text`, and run `just validate-quotes`.
6. **Add a history record** (`just new-history --kind gene ...`) for every gene whose
   `sequence-read/` files you commit, cited in the review or not, and a line in
   `GENE-notes.md` when the gene has one.

## Optional: the blind control

To find out what the sequence alone supports, separate from recall and context, ask
the fs2f FEAT and PSEUDO prompts blind through
[peptalk-llm](https://github.com/ai4curation/peptalk). It makes single direct API calls
with only `>sequence` as the header, and verifies that nothing else was sent. Do not
use the `claude` command-line tool for this: it adds context of its own.

```bash
uv run ai-gene-review sequence-read blind-fasta ORG GENE   # add --position N if UniProt has no ACT_SITE
D=genes/ORG/GENE/GENE-bioinformatics/sequence-read
uvx --from peptalk-llm peptalk annotate $D/GENE-blind.fasta -t features -t active-site \
    --context blind --shuffle-control -o $D/peptalk-blind.jsonl
uvx --from peptalk-llm peptalk annotate $D/GENE-probe.fasta -t active-site --context blind \
    -o $D/peptalk-probe.jsonl
uv run ai-gene-review sequence-read import-peptalk ORG GENE $D/peptalk-blind.jsonl $D/peptalk-probe.jsonl
```

This writes a checked `RESULTS.md`. Trust it only when every call shows `input
verified blind: yes` and the shuffled controls pass. A probe verdict of
`TRACKS_CATALYTIC_RESIDUE` means the call followed the catalytic residue and not the
decoy. The control costs real money: the shuffled activity question alone can cost
dollars. A model that recognises the protein is not reading it blind, whatever the
header says. Cite `RESULTS.md` as for step 5.

## Addendum

The evidence behind these instructions is in
[`references/results.md`](references/results.md): the fs2f findings, the live blind
control and worked examples, the claude-CLI route (`just sequence-read`), and how to
read every line of `RESULTS.md`.
