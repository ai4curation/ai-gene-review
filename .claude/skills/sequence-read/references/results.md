# sequence-read: results, findings and caveats

Addendum to [`../SKILL.md`](../SKILL.md). This page holds the evidence behind the
skill's instructions. It is expected to change as models and tests change; the skill's
instructions should not need to.

Source study: fable-sequence-to-function (fs2f),
<https://github.com/ai4curation/fable-sequence-to-function> (`manuscript.tex`), whose
FEAT and PSEUDO prompts the blind control uses verbatim.

## What fs2f found, and what follows for the skill

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

- **Cost of a blind read can be dominated by the shuffled control.** In the live PTEN
  peptalk run below, the PSEUDO question on the shuffled sequence used 48,863 thinking
  tokens (US$1.98 of the run's US$2.27) and ended in a confident hallucination.

## Blind control, live (2026-11-25, peptalk-llm 0.1.0, claude-fable-5-2, high effort)

PTEN (P60484), `--context blind`, every call verified by peptalk's
`input_tokens_match` check. Run files in
`genes/human/PTEN/PTEN-bioinformatics/sequence-read/` (`peptalk-*.jsonl`,
`claude-fable-5-2-high-peptalk-blind.json`, `RESULTS.md`).

- Domains: PF10409 at IoU 0.99; phosphatase domain named PF22785
  (`IN_UNIPROT_NOT_INTERPRO`); shuffled sequence got no domain.
- Activity: Cys124 named (UniProt ACT_SITE); C124A called inactive with the position
  reported, decoy C83A active: `TRACKS_CATALYTIC_RESIDUE`.
- **The shuffled sequence was called an active enzyme.** Asked the PSEUDO question, the
  shuffled PTEN sequence was named a "Deoxyribonuclease II-like protein" with catalytic
  HxK motifs at chance positions and called active. peptalk flagged the wild-type
  activity answer (`shuffled_control`), and `RESULTS.md` now scores the shuffled
  activity call as a failed control. fs2f asked the shuffled control only of the FEAT
  question, so this failure mode was not measured there.
- The model said it recognised PTEN ("matches human PTEN from memory"), so this, too,
  is not a test of the sequence alone.

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

## The claude-CLI route


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

## Mechanics of the blind and CLI routes

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

