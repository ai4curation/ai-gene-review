# ADM5 (C9JUS6) — review notes

2026-09-26. PAINT no-IBA backlog. Deep research provider: affinage.

## Headline

Human ADM5 has **8 annotations, all electronic** (7 IBA + 1 IEA), and they describe a
cardiovascular peptide hormone: hormone activity, adrenomedullin receptor signalling,
adenylate-cyclase-coupled GPCR signalling, regulation of blood pressure, heart rate and urine
volume.

UniProt's own curated function line for the same accession reads:

> [file:genes/human/ADM5/ADM5-uniprot.txt "Probable non-functional remnant of adrenomedullin-5."]

Both cannot be right. 6 REMOVE, 2 ACCEPT.

## Why the removals are safe to make

CLAUDE.md permits REMOVE for "over-propagated electronic (IEA/IBA) inferences you can argue
against on biological grounds", and forbids it for experimental annotations whose full text I
have not read. **There is not a single experimental annotation on this gene** — no IDA, IMP,
IPI, nothing. So no curator's reading is being second-guessed. Three independent lines:

1. **The mature peptide is deleted in our lineage.**
   > [PMID:18434369 "In primates, nucleotide deletion occurred in the mature AM5 sequence in anthropoids (human and chimp) during transition from the rhesus monkey."]

   This is the same paper UniProt cites, with an experimental evidence code, for its
   "non-functional remnant" statement.

2. **UniProt has no mature-peptide feature, no amidation site, and PE=2** (transcript level),
   in contrast to pig A5LHG2, which annotates `PEPTIDE 26..77` and `MOD_RES 77 Tyrosine amide`.

3. **A sequence analysis run for this review** (`ADM5-bioinformatics/`) reaches the same place
   independently.

## The bioinformatics, and why the result is the interesting shape

A functional CGRP/adrenomedullin peptide needs two things: the disulfide ring, and C-terminal
α-amidation (encoded as `X-G-[KR][KR]` in the precursor). Amidation is required for receptor
activation across the whole family.

> [file:genes/human/ADM5/ADM5-bioinformatics/RESULTS.md "**The ring survived; the amidation signal did not.**"]

The ring is retained (human C39–C44 ↔ pig C38–C43). The amidation signal is gone — and the
decisive form of that test needs no alignment at all:

> [file:genes/human/ADM5/ADM5-bioinformatics/RESULTS.md "| `G[KR][KR]` anywhere in the protein | **two** (pos 68 `GRK`, pos 78 `GRR`) | **none** | **lost** |"]

That combination is exactly why the gene still attracts annotations: **the feature that keeps the
sequence looking plausible to similarity and phylogeny methods survived; the feature that
licenses receptor activation did not.** Human is also 45 residues longer than pig, the shape a
frameshift leaves.

Limitations are stated in RESULTS.md and are real: two sequences, a motif argument rather than a
measurement, and it cannot exclude some unrelated acquired function.

## Two independent defects, not one

Looking at the donor sets made a second problem visible. PANTHER node `PTN000602075` spans ADM,
ADM2 **and** ADM5, so most donors are paralogs:

| Row | ADM5 ortholog among donors? | Other donors |
|---|---|---|
| GO:0005179 hormone activity | **no** | human ADM, pig ADM, human ADM2 |
| GO:1990410 AM receptor signaling | **no** | human ADM, human ADM2 |
| GO:0005576 extracellular region | **no** | rat Adm, human ADM, human ADM2 |
| GO:0003073 blood pressure | yes (pig ADM5) | human ADM |
| GO:0007189 adenylate cyclase GPCR | yes | human ADM, rat Adm2 |
| GO:0010460 heart rate | yes | human ADM, rat Adm |
| GO:0035809 urine volume | yes | human ADM |

(Donor identities resolved via the UniProt and RGD APIs, not from memory.)

So even before the pseudogenisation argument, the hormone-activity and receptor-signalling rows
are transfers from ADM/ADM2 onto a gene that has no ADM5 evidence behind them at all.

## Two rows that are contradicted even for the functional peptide

Worth separating out, because these would be wrong for AM5 in *any* mammal:

- **GO:1990410 / GO:0007189.** The mammalian AM5 peptide was tested against the adrenomedullin
  receptors and failed:
  > [PMID:18434369 "did not induce appreciable increases in cAMP production in any combination"]
  > [PMID:18434369 "These data indicate that AM5 seems to act on as yet unknown receptor(s) for AM5, other than CLR/CTR+RAMP, to exert central and peripheral cardiovascular actions in mammals."]

  The CLR-RAMP3 evidence is pufferfish and Xenopus only.

- **GO:0035809 regulation of urine volume.** Negative in two mammals:
  > [PMID:18434369 "AM5 did not cause significant changes in urine flow and urine Na+ concentration at any dose."]
  > [PMID:21436721 "Urine volume and sodium excretion were unchanged."]

  A diuretic effect appears only in *heart-failure* sheep — a disease context, not a normal role.

## What survives

The two extracellular-region rows. Secretion does not depend on the mature peptide surviving,
and the signal peptide is intact:

> [file:genes/human/ADM5/ADM5-uniprot.txt "SIGNAL          1..18"]

Accepted on the human sequence's own features rather than on the strength of the propagation
(the donors there are all paralogs).

## core_functions is deliberately empty

`just validate` warns "No core functions defined". That warning is the correct output here.
Inventing a core function for a gene I have just argued is a non-functional remnant would
contradict the review. Left as-is intentionally.

## The deep-research record got this backwards

affinage's gates passed and all nine of its citations are real and correctly summarised. But its
narrative opens:

> [file:genes/human/ADM5/ADM5-deep-research-affinage.md "ADM5 (adrenomedullin 5) is an evolutionarily ancient member of the calcitonin gene-related peptide (CGRP)/adrenomedullin peptide family that functions as a secreted regulator of cardiovascular, fluid, and neuroendocrine homeostasis"]

— written as a description of *the human gene*, on the strength of experiments in pufferfish,
medaka, Xenopus, pig, rat and sheep. It never says the human mature peptide is deleted, even
though its own 2006 dated finding records the anthropoid deletion. **Taken at face value this
record would have produced eight ACCEPTs.** Marked `correctness: DISPUTED` in the references
block for that reason.

This is a different failure from the ADIG case earlier today (where affinage simply missed the
decisive paper). Here it had the right papers and framed them as if the human gene were
functional. Both are recall/framing problems that the precision gates cannot see.

## Outcome

8 rows: 6 REMOVE, 2 ACCEPT. `just validate human ADM5` passes (1 intentional warning).
All 16 distinct supporting_text quotes (44 instances) verified as substrings, including the
19 `file:` instances CI does not check.

## Round 2 (review feedback)

The reviewer found three substantive problems. Two were errors in my reasoning, and the most
important one I should have caught myself.

### I marked an experimental annotation SOURCE_BAD from an abstract

The pig donor A5LHG2 carries **`GO:0035809` regulation of urine volume with evidence code IDA**
from PMID:18434369 — checked directly against QuickGO. It also carries an IDA for `GO:0007189`.
I had marked the urine-volume donor `SOURCE_BAD` on the strength of two negative *abstracts*,
which is precisely the move CLAUDE.md forbids: the curator read the full text and I did not.

Worse, the heart-failure paper reconciles the apparent contradiction itself:

> [PMID:22087608 "in these studies in normal animals, urine volume and sodium were maintained despite the reductions in BP, suggesting a relative improvement in renal function in normal health also"]

Maintained urine output against falling blood pressure is a renal action, not the absence of one.
Donor status corrected to `SUPPORTS_SOURCE_BUT_NOT_TARGET`. The REMOVE stands, but now rests
**only** on the target — human ADM5 cannot make the peptide — not on any claim that the pig
annotation is wrong.

### The "AM5 raises no cAMP" argument was wrong

I wrote that AM5 produces no cAMP. It does:

> [PMID:21436721 "cyclic adenosine monophosphate (50% increment, P < 0.001) all rose in response to high dose AM-5"]

The negative result is specific to **transfected CLR/CTR+RAMP combinations**, which bears on
*which receptor* AM5 uses — relevant to `GO:1990410` — not on whether the signalling is
adenylate-cyclase coupled. Since pig also holds an IDA to `GO:0007189`, the donor is sound there
too. Rewritten so the receptor-assignment argument stays with `GO:1990410` and `GO:0007189` rests
on the human deletion alone.

### Four references were cached but uncited

PMID:16195494 (pufferfish CLR-RAMP), PMID:33711314 (Xenopus), PMID:19420012 (central AM5) were
all doing argumentative work while absent from `references`. PMID:22087608 (heart-failure
diuresis) was asserted with **no citation and no cached record**, sourced only from the affinage
record this very review marks DISPUTED — the same failure I flagged in the ADIG review on the
same day. All four now cached and cited.

One incidental gem from PMID:19420012:
> [PMID:19420012 "We used porcine AM5 in the present study because rat AM5 has not been detected."]

Independent support for the degeneracy story: rodents lack AM5 entirely.

### Framing improvements taken

- **These seven IBAs are the PAN-GO reference set**, which UniProt itself advertises
  (`DR PAN-GO; C9JUS6; 7 GO annotations based on evolutionary models`). So this is not a stray
  pipeline versus a curator — it is two curated resources disagreeing, and the removals are now
  framed that way.
- **The node ask is better as "move the IBD down"** than "split the family": PTHR23414 already
  resolves into subfamilies with ADM5 as SF6 alone, so re-placing the ancestral assertion at
  subfamily level is the actual fix.
- **Both `GO:0005576` rows are now `KEEP_AS_NON_CORE`.** The reviewer noted the IBA row's
  relationship type reads as the product being *active* extracellularly, which contradicts a
  review that empties `core_functions`. The repo convention is that the qualifier column is inert
  and not argued from, so the action is not driven by it — but the tension is genuine, and
  non-core records that the extracellular placement is a routing consequence rather than a site
  of action. (Validation also enforces one action per term, so the IEA row moved with it.)

Final: 8 rows, 6 REMOVE / 2 KEEP_AS_NON_CORE. 23 distinct quotes (50 instances) verified.

## Round 3 (review feedback)

Two residual items, both the same class as round 1 and 2 — a claim surviving in one field after
being retracted in another, and a contrary sentence left out of a paper I mined twice.

1. **The `GO:0007189` summary still asserted the retracted claim.** The `reason` said plainly
   that "AM5 raises no cAMP" was wrong, and thirty lines above, the `summary` still said the row's
   defect was that "the mammalian AM5 peptide raised no cAMP through any CLR/CTR-RAMP
   combination". Two fields disagreeing inside one row, and the summary is what renders. Rewritten.

2. **I mined PMID:22087608 for two findings and omitted the third — the one that cuts against me.**
   Its Discussion reads:
   > [PMID:22087608 "Despite continued haemodynamic improvement during HD AM5, cAMP levels rose, suggesting that AM5 did activate this second messenger and may indeed signal via the same receptors as AM and AM2"]

   That is the contrary view on the receptor question, directly against the `GO:1990410` reason's
   closing claim that even a functional mammalian AM5 should not carry the term. Now recorded on
   both the reference entry and in the row, with the closing claim withdrawn: **the receptor
   question is genuinely open**, and the removal never depended on settling it.

Also taken: PMID:21436721's cAMP finding is now on its reference entry (it was used in
`supported_by` but missing from `findings`); the PMID:16195494 quote extended so it actually
reaches `CLR1-RAMP3 (AM5)`; the teleost and amphibian papers wired into the `GO:1990410`
`supported_by`; and a history record added under `history/genes/human/ADM5/`.

**A process note for myself.** My builder scripts accumulate substitutions in memory and write
once at the end, so when a later substitution fails the earlier ones are silently discarded —
even though each printed `ok:`. That happened here: the summary fix reported success, was lost,
and I only caught it because I re-read the *output YAML* rather than trusting the script's log.
Verify the artifact, not the transcript.

No REMOVE changed in any round. The human-deletion argument was load-bearing throughout.

## Round 4 (review feedback)

Two items, and the first is the more serious because it was **self-contradicting structured data**,
not just prose.

### The shared paralogy paragraph was false on four of six rows

I wrote one preamble asserting that the donor set is "dominated by paralogs rather than by ADM5
orthologs" and applied it to all six REMOVEs. Checking the actual `supporting_entities`:

| Row | A5LHG2 (true ortholog)? | Q7Z4H4 (ADM2)? | paralogy claim |
|---|---|---|---|
| GO:0003073 | **yes** | no | false |
| GO:0007189 | **yes** | no | false |
| GO:0010460 | **yes** | no | false |
| GO:0035809 | **yes** | no | false |
| GO:0005179 | no | yes | true |
| GO:1990410 | no | yes | true |

So on four rows the boilerplate contradicted the row's own `propagation_review` — which calls
A5LHG2 "the true ortholog" — and its own `supporting_entities`, and the donor table in my own PR
body.

Worse, **`WRONG_ORTHOLOG_OR_PARALOG` was in all six `failure_modes` lists**, and that field feeds
the IBA audit aggregation. On the four orthologous rows the propagation failed through
lineage-specific loss in the target, not donor misidentification. Corrected: the preamble is now
split into `PARALOG` (no ADM5 donor present) and `ORTHOLOG` (donor present, target-side loss),
and `WRONG_ORTHOLOG_OR_PARALOG` survives only on the two rows where it is true.

**The lesson is about shared preambles.** A paragraph written once and pasted into six rows is
not checked against any of them. The same structural risk was flagged on AJM1 today, where a
~160-word preamble repeats across eight rows. There it happens to be true everywhere; here it
was false in two thirds of its uses.

### The retraction did not reach the fields that render

Third instance of this shape in one PR. `description` still said "so its mammalian receptor is
unidentified" and a `suggested_question` still said the term "may be wrong for AM5 in every
mammal" — both stating as settled exactly what the `GO:1990410` reason had just recorded as open.
Both now say the evidence conflicts and that this review takes no position.

### Suggestions

- **The mirror-image omission.** Having added the heart-failure paper's pro-receptor sentence, I
  had left out its opposite:
  > [PMID:22087608 "Although plasma cAMP concentrations tended to increase during the HD AM5 infusion in the present study, levels did not rise significantly above control, and the LD infusion period was characterized by clear-cut reductions in cAMP."]

  Both are now recorded. The paper argues both sides and should be represented as doing so.
- **The Xenopus quote did not support its statement.** Replaced with the operative result four
  lines down: [PMID:33711314 "In HEK293T cells expressing clr-ramp3, CRE-Luc reporter activity was increased by the treatment with am2 at the lowest dose, but with am5 and am1 at higher dose."]
- **"An earlier draft" / "round 2" phrasing removed** from `review.reason` and from the one
  reference note carrying it. A reason field should read as curation, not as PR history; the
  round-by-round narrative belongs here and in the history record.

Final: 8 rows, 6 REMOVE / 2 KEEP_AS_NON_CORE, unchanged across four rounds. 26 distinct quotes
(57 instances) verified.

## Round 5 (review feedback)

One residual, and it is the same mechanism as the thing it was fixing: **splitting a six-row
falsehood produced a two-row one.** My new `PARALOG` variant named pig ADM (P53366) as a donor.
That is true for `GO:0005179` but not for `GO:1990410`, whose WITH/FROM is only the node, P35318
and Q7Z4H4 — so the reason again disagreed with the `source_entities` beside it.

Fixed by removing accession enumeration from the shared preamble entirely. Per-row donors live in
`source_entities`, which is generated from the data and cannot drift. **A shared preamble should
carry no row-specific facts at all** — that is the generalisable form of this lesson, arrived at
the hard way twice.

### One reviewer claim I checked and did not accept

The review said the `ORTHOLOG` variant's "present and sound" holds firmly "only for the two rows
with QuickGO IDAs". It is four, not two. Pig ADM5 (A5LHG2) holds experimental IDAs for
**GO:0003073, GO:0007189, GO:0010460 and GO:0035809** — every term whose human row lists it as a
donor — all from PMID:18434369.

Rather than assert that back, I committed `ADM5-donor-goa-check.json` so it is checkable:

> [file:genes/human/ADM5/ADM5-donor-goa-check.json "pig ADM5 holds experimental IDAs for all four of the terms whose human rows list it as a donor"]

The snapshot was worth making regardless — several rounds of this review turned on which evidence
codes that donor holds, and those facts had lived only in prose. It also confirms the converse
cleanly: pig ADM5 has *no* experimental annotation for GO:1990410, consistent with that row having
no ADM5 donor at all.

### History churn

Round 4 rewrote the two earlier history events from block literals to quoted folded scalars — text
unchanged, 60 lines of diff in a record that is supposed to be append-only. Cause: I round-tripped
the file through `yaml.dump` to append an event. Restored from the round-3 blob and the new event
appended as text, so the diff against round 3 is now 38 insertions and zero deletions.

Final: 8 rows, 6 REMOVE / 2 KEEP_AS_NON_CORE — unchanged across five rounds.
