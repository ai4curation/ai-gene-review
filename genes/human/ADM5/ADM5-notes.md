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
