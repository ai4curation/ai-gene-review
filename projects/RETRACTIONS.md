---
title: "Retracted Literature Behind Annotations"
maturity: SCOPING
tags: [PIPELINE]
---

# Retracted Literature Behind Annotations

## Overview

A GO annotation outlives its source. Once a paper has been curated, the annotation
persists in GOA, propagates by IBA to the rest of the family, and gets quoted as
`supporting_text` in gene reviews — and **nothing in this repository's pipeline ever
re-checks whether that paper is still standing**. `just fetch-gene` caches the
publication once; `just validate` checks that a `supporting_text` is a verbatim
substring of the cached text, not that the text it quotes has since been withdrawn.

This project closes that hole: a checker that takes every PMID cited anywhere in the
gene reviews and asks PubMed whether it has been retracted, placed under an expression
of concern, or corrected.

## The failure class

Retraction is a *source* failure, not a biological one, and that distinction governs
everything downstream:

- A retracted paper may still have reported a real result. Retractions are issued for
  image duplication, statistics, unreproducibility, misconduct, and honest error, and
  the retraction notice itself often affirms that part of the work stands.
- Conversely, an annotation whose *only* evidence line is a retracted paper has lost its
  evidential base even if the claim later turns out to be true.
- The cited paper and the retraction notice are two different PubMed records. A review
  that cites **both** — the retracted paper flagged `is_invalid: true`, plus the notice
  — is doing the right thing, and a checker must not report the notice as if it were
  itself withdrawn.

The three PubMed signals differ sharply in seriousness, and conflating them manufactures
alarm:

| Signal | What it means | Weight |
|--------|---------------|--------|
| **Retracted Publication** / `RetractionIn` | The paper has been withdrawn | Actionable |
| **Expression of Concern** / `ExpressionOfConcernIn` | The record is questioned, not withdrawn | Read the notice |
| `ErratumIn` | A correction was published | **Usually benign** |

An erratum is most often a corrected author name, affiliation, funding statement or
figure legend. Errata are counted here for completeness and reported quietly; they are
not a defect list.

## What the checker does

[`RETRACTIONS/check_retractions.py`](RETRACTIONS/check_retractions.py):

1. Walks every `genes/*/*/*-ai-review.yaml` and collects each `PMID:` citation
   **with its citation site**, which is what makes the result actionable:
   - `reference` — an entry in the top-level `references:` list;
   - `annotation` — the `original_reference_id` of an existing annotation, i.e. the GO
     evidence line itself rests on this paper (**the serious case**);
   - `supporting_text` — a `supported_by[].reference_id`, i.e. the paper is quoted in
     support of a review judgment.
2. Queries PubMed through NCBI E-utilities `efetch` (POST, XML) in batches of 200 with a
   pause between requests, and reads two independent signals: the record's
   `PublicationType` list and its `CommentsCorrections` `RefType`s.
3. Suppresses *notices*. A record that is itself a retraction notice, an expression-of-
   concern notice or a published erratum (`Retraction of Publication`, `Published
   Erratum`, or a backward-pointing `RetractionOf` / `ExpressionOfConcernFor` /
   `ErratumFor` reference) is never reported as a problem.
4. Writes `RETRACTIONS/retraction-check.tsv` (one row per flagged PMID),
   `RETRACTIONS/retraction-check.json` (full detail, including PMIDs PubMed did not
   resolve), and the generated [retraction register](RETRACTIONS/retraction-register.md).

```bash
uv run --no-dev python projects/RETRACTIONS/check_retractions.py
uv run --no-dev python projects/RETRACTIONS/check_retractions.py --pmids 19225519 --out-dir /tmp/spot
uv run --no-dev python projects/RETRACTIONS/check_retractions.py --from-json projects/RETRACTIONS/retraction-check.json
```

A partial run (`--pmids` or `--limit`) must be given an `--out-dir`: writing a
handful of rows into the project directory would overwrite the last full scan with
a report that looks like an all-clear. The checker also exits non-zero without
writing anything if any `efetch` batch failed, for the same reason - `RETRACTED=0`
has to mean "PubMed says none", never "PubMed did not answer".

Supporting material, including the output-file descriptions and the severity tiers, is
in [`RETRACTIONS/`](RETRACTIONS/README.md).

## Relationship to the Miscitation project

[Miscitations](MISCITATIONS.md) and retractions are adjacent but distinct failures, and
they need different machinery:

- a **miscitation** is wrong *at the moment it is written* — the identifier points at a
  different paper, or the right paper does not say what it is cited for. It is found by
  reading, and it is recorded by hand in `reference_review.correctness`;
- a **retraction** is a citation that was fine when written and **went bad afterwards**.
  Nobody can find it by re-reading the review; it can only be found by re-asking PubMed.

The two meet at one enum value: a retracted source is recorded as
`correctness: DISPUTED` with the notice in `review_notes`, which is how it reaches the
[miscitation register](MISCITATIONS/miscitation-register.md). This project's job is to
tell a curator *which* references to adjudicate that way.

Set `NCBI_API_KEY` to raise the NCBI rate limit. A full pass is ~126 requests and
takes roughly 40-60 minutes without an API key.

## First full run

The first full pass (2026-09-17) covered **3,736** review files carrying citations,
**25,088** distinct PMIDs. PubMed resolved 25,087 of them.

| Signal | PMIDs | Cited as GO annotation evidence |
|--------|------:|--------------------------------:|
| Retracted | **7** | 4 |
| Expression of concern | 13 | 13 |
| Erratum | 659 | - (informational) |

**Seven retracted papers out of 25,088 citations is a good result** - 0.03% of cited
PMIDs, and the reviews had already caught three of them by hand. The point of the
register is not that the reviews are riddled with retracted sources; it is that nothing
was watching, and four of the seven sit under a GO annotation.

The full list is in the [retraction register](RETRACTIONS/retraction-register.md). The
retracted seven:

| PMID | Paper | Gene | How it is cited | Already flagged? |
|------|-------|------|-----------------|------------------|
| PMID:16616141 | Taxol / p53 transactivation of p21 (FEBS Lett 2006); retracted PMID:40963457 | human/TP53 | `original_reference_id` of `GO:0005515 protein binding` (IPI) | no - but already actioned `REMOVE` |
| PMID:19225519 | APP binds DR6 (Nature 2009); retracted PMID:38110576 | human/TNFRSF21 | reference list only | **yes** |
| PMID:22483618 | LOXL2 deaminates histone H3K4 (Mol Cell 2012); retracted PMID:27392148 | human/LOXL2 | reference + `supporting_text` | **yes** |
| PMID:27782176 | Functional kinomics of cation-Cl- cotransporter regulation (Sci Rep 2016); retracted PMID:42642456 | mouse/Mtor | `original_reference_id` of `GO:0044325 transmembrane transporter binding` (IPI) | no - actioned `KEEP_AS_NON_CORE` |
| PMID:29371969 | miR-124 / BACE1 (Oncotarget 2017); retracted PMID:42664430 | human/BACE1 | `original_reference_id` of `GO:0043525 positive regulation of neuron apoptotic process` (IGI) | no - actioned `KEEP_AS_NON_CORE` |
| PMID:31638206 | miR-4500 / STAT3 (Mol Med Rep 2019); retracted PMID:41645757 | human/STAT3 | `original_reference_id` of `GO:0030335 positive regulation of cell migration` (IMP) | no - actioned `UNDECIDED` |
| PMID:32125225 | ACTL8 in endometrial cancer (Biosci Biotechnol Biochem 2020); retracted PMID:35078223 | human/ACTL8 | reference list only | **yes** |

Three observations from the first run:

1. **The reviews already caught three of the seven by hand.** human/TNFRSF21,
   human/LOXL2 and human/ACTL8 carry `is_invalid: true`; the first two also cite the
   retraction notice, and human/TNFRSF21 goes furthest, recording that the retraction
   touches no GO annotation on the gene. That is the standard the rest should meet, and
   it is exactly the work this checker makes systematic instead of incidental.
2. **Retraction notices arrive after the review was written.** Four of the seven
   retraction notices are 2025-2026 records (PMID:40963457, Nov 2025; PMID:41645757,
   Apr 2026; PMID:42642456, Aug 2026; PMID:42664430, 2026). A review can be scrupulous
   at the time and stale a year later, which is the argument for re-running this check
   periodically rather than treating it as a one-off audit. The BACE1 paper also shows
   why the notice types must be kept apart: it carried a 2018 *correction*
   (PMID:29873327) long before the 2026 retraction, and reporting the two together would
   have dated the retraction eight years too early.
3. **Nothing here forces a removal.** None of the four annotation-evidence cases is an
   `ACCEPT`ed core function resting on a retracted paper: the actions already recorded
   are `REMOVE` (human/TP53), `KEEP_AS_NON_CORE` (mouse/Mtor, human/BACE1) and
   `UNDECIDED` (human/STAT3), all reached on biological grounds before anyone knew about
   the retraction. The retraction is corroborating evidence for judgments already made,
   not grounds to overturn a curator.

The 13 expressions of concern are all cited as annotation evidence, but seven of them
have the same low-stakes shape: a generic `GO:0005515 protein binding` IPI row
(human/MYC, human/EGFR, human/PTPN11, human/AGO2, human/CLU, ARATH/CIPK24, ARATH/PYR1)
that the review had already marked `REMOVE` or `MARK_AS_OVER_ANNOTATED` for reasons
unrelated to the notice. The one that deserves a look is PMID:19033661 (AIP1/VEGFR2,
*J Clin Invest* 2008, EoC PMID:40955656, Sep 2025), which supports **13 `ACCEPT`ed or
`KEEP_AS_NON_CORE` annotations** across human/DAB2IP and human/VEGFA.

**The 659 errata are not a defect list.** They are dominated by large interactome and
genome papers that hundreds of gene reviews cite - PMID:40205054 (multimodal cell maps,
*Nature* 2025) alone is cited by 277 genes, PMID:21988832 (human liver interactome) by
83, PMID:12534463 (*P. putida* KT2440 genome) by 79. One erratum on such a paper
inflates the count without implying anything about the citing reviews. They are recorded
for completeness and should stay in the quiet section of the register.

**One PMID could not be resolved**: PMID:34521819 (cited by human/JAK1 and human/STAT1),
which returns no PubMed record. The STAT1 review already notes this. It is a
bibliographic dead end rather than a retraction, but it is the same class of problem -
a citation that no longer points at anything.

## What a curator should do

A retraction is about the **source**, so the first move is bibliographic, not
annotation surgery. CLAUDE.md's rule that experimental annotations are not overruled
from incomplete evidence applies with full force here: the curator who made an IDA had
the full text, and a retraction notice is not a substitute for reading what they read.

1. **Flag the citation.** Set `is_invalid: true` on the reference and record *why* in
   `reference_review` (`correctness: DISPUTED`, with the retraction date and the notice
   PMID in `review_notes`). This is what the existing CLI command is for:

   ```bash
   uv run --no-dev ai-gene-review mark-invalid-pmids genes/human/GENE/GENE-ai-review.yaml PMID:19225519
   ```

   It sets `is_invalid: true` on matching entries in the `references:` list of one file.
   It does *not* detect anything, does not touch annotations, and rewrites the YAML
   through a plain `yaml.dump`, so re-check the diff for reformatting before committing.
2. **Cite the notice.** Add the retraction notice as its own reference with
   `correctness: VERIFIED`. The pair (retracted paper + notice) is the honest record,
   and it stops the next reviewer rediscovering the problem.
3. **Ask what actually rests on it.** Use the `citation_sites` column:
   - cited only in `references` → bibliographic cleanup, nothing else to do;
   - cited as `supporting_text` → find independent support for the claim, or soften the
     review text; a quote from a retracted paper should not be load-bearing;
   - cited as an annotation's `original_reference_id` → this is the real case. Check
     whether the annotation is corroborated independently (another experimental
     annotation, an IBA whose node rests on other descendants, a later replication). If
     it is, say so in `review.reason` and keep it. If the retracted paper is the sole
     evidence, that is grounds for `UNDECIDED` or a proposed `REMOVE` with the
     retraction cited — a curation recommendation to be sent upstream to the source MOD,
     not a silent deletion.
4. **Do not mass-remove.** Retraction of one paper does not invalidate every annotation
   on the gene, and a retraction notice frequently affirms parts of the work. Scope the
   action to the specific evidence line.

The worked example is human/TNFRSF21, which already does all of this by hand.


---

# STATUS

- [x] Checker built (`RETRACTIONS/check_retractions.py`): citation harvest with site
      attribution, batched E-utilities `efetch`, notice suppression, TSV + JSON output
- [x] Generated register (`RETRACTIONS/retraction-register.md`), severity-tiered
- [x] First full run over all 3,736 citing review files / 25,088 distinct PMIDs
- [x] Seed case verified end-to-end (PMID:19225519 / human/TNFRSF21): flagged
      `Retracted Publication`, cited only in the reference list, already
      `is_invalid: true`, and cited by **no** GO annotation in any review or any cached
      `*-goa.tsv` in the repo
- [ ] Work the four annotation-evidence retractions (human/TP53, human/BACE1,
      human/STAT3, mouse/Mtor): set `is_invalid: true`, cite the notice, and record in
      `review.reason` whether the annotation survives on independent evidence
- [ ] Add `reference_review` entries (`correctness: DISPUTED`) for the 13 expressions of
      concern; start with PMID:19033661, which carries 13 accepted annotations
- [ ] Extend the scan to the cached `*-goa.tsv` reference columns, so retracted sources
      behind *unreviewed* GOA annotations are caught too (currently only the reviews are
      scanned)
- [ ] Decide whether this runs in CI. The natural hook is the existing publication-type
      backfill (`ai_gene_review/etl/publication_type.py`), which already fetches each
      PMID's PubMed PT list and simply ignores `Retracted Publication`; a
      retraction/EoC flag could ride along at no extra request cost

# NOTES

## 2026-09-17

**Project creation and first run.** Built the checker and ran it across the repository.
Headline: 7 retracted, 13 expression-of-concern, 659 erratum PMIDs out of 25,088 cited -
and 4 of the 7 retractions sit under a GO annotation.

Design decisions worth recording:

- **Citation site is the whole point.** A retracted paper in a `references:` list is a
  bibliographic cleanup; the same paper as an annotation's `original_reference_id` is a
  curation question. The checker records which, so the register can sort the two apart
  rather than reporting one undifferentiated count of "retracted citations".
- **Notices must be suppressed.** A good review cites both the retracted paper *and* its
  retraction notice. A naive checker flags the notice too (it carries
  `Retraction of Publication`, and PubMed puts `Expression of Concern` on the *notice*,
  not on the paper it concerns), which would penalize exactly the reviews that did the
  right thing. Notices are detected by publication type and by backward-pointing
  `RetractionOf` / `ExpressionOfConcernFor` / `ErratumFor` references, and excluded.
- **Errata are reported quietly and deliberately.** 659 is a big number that means very
  little: it is driven by a handful of interactome/genome papers with hundreds of citing
  genes each. Presenting errata next to retractions would manufacture an alarm the data
  does not support.
- **`mark-invalid-pmids` already existed and is reused, not replaced.** It is a manual,
  per-file setter for `is_invalid` on `references:` entries with no detection of its own;
  this project supplies the detection that tells a curator which PMIDs to hand it. Caveat
  found while reading it: it rewrites the YAML through a plain `yaml.dump`, so it can
  reflow a whole file - check the diff before committing.

Last updated: 2026-09-17
