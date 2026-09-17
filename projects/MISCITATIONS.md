---
title: "Miscitation Review Project"
maturity: SCOPING
tags: [PIPELINE]
species: [human]
genes: [NLRP3, ZBP1, GRID1, SULT1B1, PNPLA3, PEX39]
---

# Miscitation Review Project

## Overview

A **miscitation** is a citation that passes every mechanical check and is still
wrong. The identifier is well formed. It resolves. A paper comes back. But it is
not the paper that was meant, or it is the right paper and it does not say what
it is being cited for.

The schema already has a place to record this — `references[].reference_review.correctness`,
a `ReferenceCorrectnessEnum` — and reviewers have been filling it in for some time.
Nothing aggregated it, so a miscitation found while reviewing one gene stayed buried
in that gene's YAML. This project builds the register, works out what kinds of
miscitation there are, and separates the ones that are defects in **this repo's
reviews** from the ones that are defects in the **source databases** we import from.

The [register](MISCITATIONS/miscitation-register.md) is generated from the YAML, not
hand-maintained.

## Why the existing checks cannot see this

The repo already validates citations, hard. Two checks in particular:

1. **The reference resolves and the title matches.** `linkml-reference-validator`
   fetches each cited `PMID:` and compares the fetched title against the `title:`
   recorded in the review. A transposed or invented PMID whose title no longer
   matches the intended paper fails.
2. **Every `supporting_text` is verbatim.** Each quote must be an exact substring
   of the cached `publications/PMID_*.md`. A paraphrased quote fails; an invented
   quote fails; a quote lifted from a different paper fails.

Both checks are about *internal consistency*. Neither can catch either half of a
miscitation:

- **"Resolves to a different paper than intended."** Check 1 compares the fetched
  title to the *recorded* title. If a wrong identifier was imported together with
  the wrong paper's title — which is exactly what happens when a PMID is taken from
  GOA and its title fetched from that same PMID — the two agree perfectly. NLRP3's
  `PMID:1189953` has the correct title for `PMID:1189953`. It is simply not the
  paper anybody meant to cite.
- **"Right paper, wrong claim."** Check 2 verifies a quote is *present in* the
  paper. It cannot verify the quote *supports the assertion*. A verbatim sentence
  can be quoted in support of a conclusion the paper explicitly rejects — PNPLA3
  below is precisely that.

There is a third blind spot. The validator's `skip_prefixes`
(`conf/reference_validator_config.yaml`) exempt every non-literature prefix —
`GO_REF`, `Reactome`, `file`, `UniProt`, `InterPro` and others — from snippet
checking entirely. **127 of the 559 currently flagged references carry one of those
prefixes** (72 `file:`, 28 `GO_REF:`, 27 `Reactome:`), i.e. they were found by a
human reading them, because no automated check was ever going to look.

So the flag is, and has to be, a **manual** judgment. `reference_review` is where it
goes.

## Taxonomy

`ReferenceCorrectnessEnum` distinguishes four failure modes plus two states:

| Value | The identifier | The paper | The claim |
|---|---|---|---|
| `VERIFIED` | resolves as intended | is the right paper | is supported |
| `UNVERIFIED` | — | — | not yet checked |
| `WRONG_IDENTIFIER` | resolves to **something else** | wrong paper | — |
| `MISCITED` | resolves as intended | right paper | **not supported by it** |
| `DISPUTED` | resolves as intended | right paper | supported, but **contested** by other evidence |
| `LOW_QUALITY` | resolves as intended | right paper | supported, but **weakly** |

Cutting across that enum, the seed cases below separate into two kinds by *where the
error lives*, and this turns out to matter more than the enum value:

- **Reference-level miscitation.** The reference itself is wrong. `correctness`
  captures it directly and the register picks it up. NLRP3 and SULT1B1 are of this kind.
- **Evidence-attachment miscitation.** The reference is fine; the *link* from that
  reference to the assertion is wrong — a wrong interactor in `WITH/FROM`, an
  experimental evidence code on a non-experimental paper, an annotation asserting the
  positive of a result the cited paper reports as negative. ZBP1, GRID1, PNPLA3 and
  PEX39 are of this kind.

The second kind currently has **no structured home**. `reference_review` grades the
reference, and by the reference's own lights these references are all `VERIFIED` —
which is how they are in fact graded. The defect survives only as free text in
`review_notes`, where no aggregation can find it. Four of the six seed cases are like
this. That is the main structural finding so far, and the main open question (see
[Status](#status)).

## Source-database defects vs. review defects

Most of what follows is **not** a mistake in this repo. NLRP3's digit-dropped PMID is
in GOA. ZBP1's and GRID1's wrong interactors are in IntAct. PEX39's evidence code is in
UniProt. PNPLA3's `EXP` row is in GOA. These reviews are the first place the errors
have been written down; `reference_review` is the recording mechanism, not the cause.

That distinction should be kept sharp, both because it is true and because it
determines what to do next: a review defect is fixed by editing the YAML, a source
defect is fixed by reporting it upstream.

## Seed cases

Six cases surfaced during the contested-functions review. Each was re-verified here
against the local GOA/UniProt files and, where possible, a live query (QuickGO,
NCBI E-utilities, EuropePMC, UniProt REST). **All six are confirmed**, in the sense
that the factual claim in the last column was checked, not taken on report.

| Gene | What is cited | Defect | Kind | Where the error lives |
|---|---|---|---|---|
| NLRP3 | `PMID:1189953` as IDA for `GO:0060090` + `GO:0030674` | resolves to *"[Profanities and the profane person]"*, Acta Psiquiatr Psicol Am Lat **1975** | `WRONG_IDENTIFIER` | GOA |
| ZBP1 | `PMID:19590578` IPI, `WITH/FROM` `UniProtKB:Q13601` | Q13601 is **KRR1**, a ribosome-biogenesis factor; the paper's partner is RIPK1 (Q13546) | attachment | IntAct |
| GRID1 | two IPI rows, both `WITH/FROM` `UniProtKB:P68871` | P68871 is **haemoglobin subunit beta**, a classic affinity-purification contaminant | attachment | IntAct |
| PEX39 | UniProt `FUNCTION` for Q5I0X4 cites `PMID:37160800` with `ECO:0000269` | that PMID is a 2023 multi-author **meeting report**, not primary evidence | attachment | UniProt |
| SULT1B1 | `PMID:23207770` IDA for `GO:0006068` ethanol catabolic process | the paper names four ethanol-sulfating SULTs and **SULT1B1 is not one of them** | `MISCITED` | GOA |
| PNPLA3 | `PMID:21878620` as `EXP` for `GO:0003841`, no `NOT` | that paper reports **no detectable** LPAAT activity for purified PNPLA3 | attachment | GOA |

### NLRP3 — a dropped digit

`genes/human/NLRP3/NLRP3-goa.tsv` carries two IDA rows referencing `PMID:1189953`:

```
GO:0060090  molecular adaptor activity              ECO:0000314  IDA  PMID:1189953
GO:0030674  protein-macromolecule adaptor activity  ECO:0000314  IDA  PMID:1189953
```

A live QuickGO query for `UniProtKB:Q96P20` + `PMID:1189953` returns those same two
annotations, so this is live GOA and not a stale local snapshot. PubMed resolves
`1189953` to *"[Profanities and the profane person]"* (Alva Quinones J, *Acta
Psiquiatr Psicol Am Lat*, June 1975) — a Spanish-language psychiatry abstract.

The intended reference is almost certainly `PMID:31189953`, *"Structural mechanism for
NEK7-licensed activation of NLRP3 inflammasome"* (Nature, 2019). The same GOA file
already cites `31189953` for five other NLRP3 annotations. A leading `3` was dropped.

This is the cleanest possible illustration of why check 1 cannot help: the review
records the title *"[Profanities and the profane person]"*, and that is genuinely the
title of `PMID:1189953`. The citation is internally perfect and externally absurd.

### ZBP1 and GRID1 — the interactor, not the paper

`ZBP1` `GO:0005515` IPI from `PMID:19590578` lists `UniProtKB:Q13601` in `WITH/FROM`.
The paper is *"DAI/ZBP1 recruits RIP1 and RIP3 through RIP homotypic interaction motifs
to activate NF-kappaB"* — an entirely appropriate citation. But Q13601 resolves (UniProt
REST) to `KRR1_HUMAN`, "KRR1 small subunit processome component homolog". RIPK1 is
`Q13546`. The other partner recorded for the same reference, `Q9Y572`, *is* RIPK3 and
does match the paper.

`GRID1` has exactly two `GO:0005515` IPI rows, from `PMID:28514442` and
`PMID:33961781`, both proteome-scale interactome maps. Both name `UniProtKB:P68871` — `HBB_HUMAN`, haemoglobin
subunit beta. Both source papers are legitimate proteome-scale interactome screens,
correctly cited. Haemoglobin is one of the best-known contaminants of affinity
purification from tissue, and it is not a credible partner for a postsynaptic glutamate
receptor. The whole of GRID1's `protein binding` evidence rests on it.

In both cases the reference is right and the `correctness` is (correctly) `VERIFIED`.
The error is one column over.

### PEX39 — an experimental evidence code on a meeting report

UniProt's `FUNCTION` block for Q5I0X4 (PEX39) reads, in part:

```
CC   -!- FUNCTION: Cytosolic peroxin that promotes the peroxisomal import of
CC       proteins containing a type-2 peroxisomal targeting signal (PTS2) by
CC       binding to PEX7 ... (PubMed:37160800, PubMed:40739340).
CC       {ECO:0000269|PubMed:37160800, ECO:0000269|PubMed:40739340}.
```

`PMID:40739340` is the primary paper (*"PEX39 facilitates the peroxisomal import of
PTS2-containing proteins"*, Nat Cell Biol 2025) and is appropriate. `PMID:37160800` is
*"Peroxisomes: novel findings and future directions"* (Histochem Cell Biol 2023) — an
18-author community overview with no abstract in PubMed, and typed by EuropePMC as **`meeting-report`**. It
carries `ECO:0000269`, "experimental evidence used in manual assertion". A meeting
report is not a source of experimental evidence, and this one predates the primary
paper by two years.

### SULT1B1 — the negative control, annotated as a positive

`GO:0006068` ethanol catabolic process, IDA, `PMID:23207770`, assigned by CAFA. The
paper is *"Ethanol sulfation by the human cytosolic sulfotransferases: a systematic
analysis"* (Biol Pharm Bull 2012) and its abstract says:

> A systematic analysis revealed four ethanol-sulfating SULTs, SULT1A1, SULT1A2,
> SULT1A3, and SULT1C4, among the eleven human SULT enzymes previously prepared and
> purified.

SULT1B1 is one of the eleven. It is not one of the four. It was in the panel as a
negative, and the annotation asserts the opposite of the result. The cached record is
abstract-only, so the full-text panel table has not been checked — but the abstract's
enumeration is explicit, and the burden is on the annotation.

### PNPLA3 — the paper reports the negative

This is the sharpest case, because it shows `MISCITED` and "verbatim quote" are
orthogonal. GOA gives PNPLA3 `GO:0003841` (1-acylglycerol-3-phosphate
O-acyltransferase, i.e. LPAAT) three times over — once IEA, once IDA from
`PMID:22560221`, and once **`EXP` from `PMID:21878620`, with no `NOT` qualifier**.
`PMID:21878620` (Huang, Cohen & Hobbs, JBC 2011) concludes:

> Neither the wild-type nor mutant enzyme catalyzed transfer of oleic acid from
> oleoyl-CoA to glycerophosphate, lysophosphatidic acid, or diacylglycerol,
> suggesting that the enzyme does not promote de novo TAG synthesis.

"Lysophosphatidic acid" is the acceptor in `GO:0003841`. The paper assayed the exact
reaction, with CGI-58 as a positive control, and detected none. Every sentence of that
quote is verbatim; the verbatim check passes; the annotation still asserts the
reverse of what was measured. Had the row carried `NOT`, the citation would be
impeccable.

(Separately, the underlying biology is genuinely contested: `PMID:22560221` reports the
LPAAT activity that `PMID:21878620` could not find. The PNPLA3 review grades that pair
`DISPUTED`. The `EXP`/`21878620` row is a miscitation *regardless* of how the dispute
resolves.)

## Current state of the evidence

From the [register](MISCITATIONS/miscitation-register.md), regenerated from the YAML
(see [Reproducibility](#reproducibility)):

- **4513** reviewed gene files scanned; **2074 (46%)** carry at least one
  `reference_review` block
- **14559** references have been manually adjudicated
- **559 (3.8%)** are flagged as a citation or soundness problem
- **586 (4.0%)** are explicitly `UNVERIFIED` — adjudication begun, this reference not
  yet checked

| Correctness | Count | Share of adjudicated |
|---|---:|---:|
| VERIFIED | 13414 | 92.1% |
| UNVERIFIED | 586 | 4.0% |
| MISCITED | 274 | 1.9% |
| DISPUTED | 151 | 1.0% |
| LOW_QUALITY | 108 | 0.7% |
| WRONG_IDENTIFIER | 26 | 0.2% |

**These figures are not a survey.** The denominator is "references a reviewer chose to
adjudicate", and reviewers adjudicate a reference when they are already looking at it —
frequently *because* something about it looked wrong. The 3.8% is a flag rate on an
enriched, opportunistic sample, not a background error rate for GO citations, and it
should not be quoted as one. Nor is the register a complete list: 338 genes carry a
flagged reference out of 2074 adjudicated out of 4513 reviewed, and the great majority
of references in the repo have never been looked at this way at all.

The distribution across organisms reflects where curation effort has gone, not where
errors are: human accounts for 470 of the 559 flags, PSEPK for 32, DICDI 11, yeast 9,
DROME 7, SCHPO 7, and a long tail of single flags.

## Patterns visible so far

**A wrong identifier is rarely wrong once.** Of the 26 `WRONG_IDENTIFIER` rows, 11 come
from just five PMIDs, each mis-attached to two or three related genes:

| PMID | Genes | Resolves to |
|---|---|---|
| `PMID:10970790` | ELOVL1, ELOVL2, ELOVL3 | the cloning of HELO1 (= ELOVL5) — a paralog |
| `PMID:25732826` | NAA10, NAA40 | the Naa60 study — a different N-terminal acetyltransferase |
| `PMID:39329031` | NPLOC4, UFD1 | a clinical study of intellectual disability in Morocco |
| `PMID:23264731` | SERP1, SRPRB | a paper about MTR120/KIAA1383 |
| `PMID:17469741` | UPF1, UPF2 | a melanoma serum-marker study |

Two shapes are mixed in there. ELOVL1/2/3 and NAA10/NAA40 are **paralog spread**: one
family member's paper attached to its relatives, the classic failure of family-level
propagation. NPLOC4/UFD1, SERP1/SRPRB and UPF1/UPF2 are **complex-partner spread**:
one bad identifier scattered across the members of a complex or a functional pair,
which looks much more like a single import defect replicated than like independent
curation errors. Either way, finding one instance is worth checking its neighbours.

**Gene-symbol collision is its own category.** ADPRH is cited for a paper about "ARH1"
meaning autosomal-recessive hypercholesterolaemia; BRIP1 (sometimes "BACH1") is cited
for a paper about the bZIP transcription factor BACH1. These resolve, have matching
titles, and are about a different molecule that happens to share a string.

**Not everything flagged is a PMID.** 72 flagged references are `file:` citations into
the repo's own bioinformatics results, 28 are `GO_REF:`, and 27 are `Reactome:` — all
prefixes the reference validator skips wholesale. One `Reactome:` case is instructive:
P2RX7 takes a TAS localisation from `Reactome:R-HSA-139855`, an event titled
"P2X1-mediated entry of Ca++ from plasma" — a **P2X1** event supporting a **P2X7**
annotation.

## Method

1. **Aggregate first.** Run the extractor over every review; the register is the
   worklist. It costs nothing and it is already populated by work that has been done.
2. **Verify before recording.** A `reference_review` is a claim about the world, so it
   is checked against the world: resolve the PMID at NCBI, resolve accessions at
   UniProt REST, re-query GOA live at QuickGO rather than trusting the local `-goa.tsv`
   snapshot, check publication type at EuropePMC. Do not grade a reference `VERIFIED`
   on the strength of a deep-research summary asserting it is fine — that is the
   failure mode this project exists to catch, one level up.
3. **Grade the reference, note the attachment.** If the defect is in the reference,
   set `correctness`. If the defect is in how a source database *attached* the
   reference, the reference is `VERIFIED` and the defect goes in `review_notes` and in
   the annotation's `review.reason` — for now (see [Status](#status)).
4. **Check the neighbours.** On a `WRONG_IDENTIFIER`, grep the flagged PMID across
   `genes/` and check the gene's paralogs and complex partners.
5. **Say where the error lives.** Source-database defects are reported as such and are
   candidates for upstream reporting; review defects are fixed in place.

## Reproducibility

Supporting material under [`MISCITATIONS/`](MISCITATIONS/README.md):

- [`MISCITATIONS/aggregate_miscitations.py`](MISCITATIONS/aggregate_miscitations.py) —
  the extractor.
- [`MISCITATIONS/miscitation-register.md`](MISCITATIONS/miscitation-register.md) —
  the generated register (counts by correctness, by relevance, by organism; full
  table of every flagged reference).
- `reports/miscitations.tsv` — one row per adjudicated reference, untruncated notes.

```bash
uv run python projects/MISCITATIONS/aggregate_miscitations.py
```

---

# STATUS

- [x] Aggregator over every `references[].reference_review` in `genes/*/*/*-ai-review.yaml`
- [x] Generated register + TSV (14559 adjudicated, 559 flagged)
- [x] Six seed cases independently re-verified (QuickGO, NCBI E-utilities, EuropePMC,
      UniProt REST) and written up
- [x] Two-kind taxonomy established: reference-level vs. evidence-attachment miscitation
- [ ] **Open question: where does an evidence-attachment defect go?** Four of six seed
      cases are not representable in `reference_review`, because the reference is
      genuinely fine. Options: a per-annotation flag analogous to `correctness`; reuse
      of `FindingReviewStatusEnum`; or an explicit `evidence_review` on
      `ExistingAnnotation`. Not yet decided — do not add a field before the shape of
      the problem is clearer than six cases.
- [ ] Triage the 274 `MISCITED` and 26 `WRONG_IDENTIFIER` rows: confirm, classify by
      pattern, and split source-database defects from review defects
- [ ] Neighbour sweep on the five recurring wrong PMIDs — check remaining ELOVL/NAA
      family members and other complex partners
- [ ] Decide what, if anything, to report upstream to GOA / UniProt / IntAct, and in
      what form
- [ ] Consider whether `reference_review` should be *required* (currently a reviewer
      may simply omit it, which is indistinguishable from "no problem found")

Last updated: 2026-09-17

# NOTES

## 2026-09-17

**Project creation.** Built the aggregator and the register from all 4513 reviewed gene
files: 2074 carry `reference_review`, 14559 references adjudicated, 559 flagged (3.8%
of adjudicated — an enriched sample, not a survey).

Re-verified the six seed cases from the contested-functions review. All six stand.
Notes from doing so:

- **NLRP3 needed the live query.** The local `-goa.tsv` could have been stale; QuickGO
  returns the same two IDA rows against `PMID:1189953` today, so the error is current
  GOA, not a snapshot artefact.
- **The enum does not fit four of the six.** ZBP1, GRID1, PEX39 and PNPLA3 all have a
  perfectly good reference; the defect is in the `WITH/FROM` column, the evidence code,
  or the absent `NOT`. All four are already graded `VERIFIED` in their reviews, with
  the real problem written into `review_notes` — correctly, but invisibly. This is the
  finding that most shapes what the project should do next, and it argues the register
  systematically *under*-counts attachment defects relative to reference defects.
  PNPLA3's own note states it exactly: *"The citation itself is correct; what is wrong
  is GOA's use of it as EXP evidence for GO:0003841, a reaction this paper could not
  detect."*
- **Recurrence was the surprise.** 11 of 26 `WRONG_IDENTIFIER` rows trace to five PMIDs.
  The complex-partner cases (UFD1/NPLOC4, SERP1/SRPRB, UPF1/UPF2) look like one import
  defect replicated across a complex rather than independent errors, which would make
  them cheap to fix upstream and worth reporting as a group.
- **The validator's `skip_prefixes` are a real blind spot.** 127 of the 559 flags are
  on prefixes (`file:`, `GO_REF:`, `Reactome:`) that are never snippet-checked. The
  `file:` ones matter for this repo specifically — SPKW's 2026-05-30 audit found ~48%
  of `file:` quotes non-verbatim across its plant reviews, all of which had passed
  `just validate`.
