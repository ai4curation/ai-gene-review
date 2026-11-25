---
name: sequence-read
description: Optional, opt-in. Ask a general frontier language model (default Claude Fable 5.2, high effort) to read a gene's protein sequence with no tools - Pfam domains with boundaries, transmembrane helices, signal peptide, catalytic residues present or lost, likely function - with shuffled and catalytic/decoy controls, and record the result in the gene review as a clearly labelled bioinformatics line of evidence. Use only when a curator asks for a sequence-only read, or when a catalytic term on a possible pseudoenzyme or an implausible protein name needs a quick independent check. Never a substitute for literature.
metadata:
  short-description: Sequence-only frontier-model read (fs2f prompts + controls)
---

# Sequence-only read by a frontier language model

This skill runs the FEAT and PSEUDO questions of the fable-sequence-to-function
study (fs2f; <https://github.com/ai4curation/fable-sequence-to-function>,
`manuscript.tex`) on one gene's UniProt sequence, checks every answer against the
sequence and the UniProt record, and writes a `RESULTS.md` that a review can cite
as a `BIOINFORMATICS` reference.

It is **opt-in**. Do not run it as part of a routine review. Each run bills three to
five model calls (US$0.19 to 0.50 per gene in the worked examples below, at high effort) to
the account the `claude` tool is signed in to.

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

## Running it

Prerequisite: the gene folder exists (`just fetch-gene ORG GENE`). The sequence and
features are read from `GENE-uniprot.txt`; Pfam boundaries come from the InterPro API.

```bash
just sequence-read human ADPRHL1                      # Fable 5.2, high effort, with controls
just sequence-read human ADPRHL1 --model claude-opus-5-5
just sequence-read human ADPRHL1 --no-controls        # 2 calls, no shuffled/decoy questions
uv run ai-gene-review sequence-read render human ADPRHL1   # re-render RESULTS.md, no calls
```

The calls use the revised fs2f route: `claude -p --model M --effort E --system-prompt ""
--tools "" --setting-sources "" --strict-mcp-config --disable-slash-commands --no-chrome
--output-format json`, from an empty temporary directory, so no tools, project
instructions, skills or connectors reach the question. A reply whose input is larger
than the question allows is marked `context_tokens_high` and is not used.

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

- `MODEL-EFFORT.json` - the run file: sequence checksum and version, route, every
  prompt hash, reply text, parsed answer, token counts per model, and the checks.
  A second run for the same model and effort is refused without `--force`.
- `RESULTS.md` - rendered from all run files, one finding per line so it can be
  quoted. Nothing in it is typed by hand.

The `claude` tool's usage record can list a second model (in our runs
`claude-haiku-5-5` on every high-effort call, but not on a one-sentence low-effort canary). The page
says so and checks that the reply is one turn whose token counts are the requested
model's; if that check fails for a call, do not rely on it.

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
needed.

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

## Worked examples (2026-11-25, Fable 5.2, high effort)

| Gene | Kind | Result |
|---|---|---|
| PTEN (P60484) | well studied | PF10409 C2 at IoU 0.99; the phosphatase domain named as PF22785, which the UniProt record lists but InterPro now gives as PF22784 (`IN_UNIPROT_NOT_INTERPRO`); Cys124 named (UniProt ACT_SITE); C124A called inactive with the position reported, decoy C83A called active: `TRACKS_CATALYTIC_RESIDUE`. |
| ADPRH (P54922) | active paralog | PF03747 at IoU 0.94; six Mg2+-site residues named, all UniProt BINDING; no ACT_SITE, so the probe took the acidic BINDING residue Asp55: D55A called inactive with the position reported, decoy D255A active: `TRACKS_CATALYTIC_RESIDUE`. |
| ADPRHL1 (Q8NDY3) | catalytic-dead paralog | Called inactive; reported lost aspartates at 58 (Asn), 304 (Glu) and 306 (Ala), each matching the sequence. That is the aspartate-only count of PMID:27217161; the review's own donor census keeps Glu304 and scores Ser305 to Ala307 as lost, which the read does not mention. Recorded in the review as a LOW-relevance reference (see `genes/human/ADPRHL1`). |
| C7orf25 (Q9BPX7) | obscure, two DUFs | Both DUFs (PF18474, PF07000) named, IoU 0.91 and 0.98; activity "uncertain", no residues named, so no probe. |

The model said or implied that it recognised the protein in all four, and all
controls passed (one transmembrane helix was predicted on the shuffled ADPRHL1
sequence, as fs2f saw for 12 of 60). Cost was US$0.19 to 0.50 per gene. The ADPRHL1 case
shows why the check lines matter: a read can agree with one published reading of a
site and not with another, and the review has to say which.

See each gene's `GENE-bioinformatics/sequence-read/RESULTS.md` for the run.
