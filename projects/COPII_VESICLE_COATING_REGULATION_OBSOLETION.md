# Regulation of COPII Vesicle Coating — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will retire **GO:0003400 regulation of COPII vesicle
coating** (BP) and merge its annotations into **GO:0048208 COPII vesicle
coating** (BP). The rationale, captured in the upstream ontology ticket, is
that the proteins currently annotated to GO:0003400 act *part_of* the COPII
vesicle coating pathway (they are components of the coating machinery —
SAR1, SEC12, SEC23, SEC16, SED4, PEF1, PREB) rather than upstream regulators
of that pathway, so the "regulation of …" parent does not describe their
biology accurately. One UniProt entry on the upstream list (human MAPK15,
Q8TD08) is being disputed and is slated for removal rather than transfer.

The replacement term GO:0048208 is also being renamed at the same time:

- `GO:0048208` *COPII vesicle coating* → **COPII vesicle coat assembly**
- `GO:0006901` *vesicle coating* → **vesicle coat assembly**

(both labels were rebranded to clearer "coat assembly" wording in the
go-ontology PR opened in response to the obsoletion request).

This project tracks the impact on AI Gene Review and queues affected genes
for review, since none of the directly annotated genes are currently in this
repository.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6389](https://github.com/geneontology/go-annotation/issues/6389)
- Ontology ticket: [geneontology/go-ontology#31945](https://github.com/geneontology/go-ontology/issues/31945) (CLOSED — obsoletion + rename applied via PR #32013)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| regulation of COPII vesicle coating | GO:0003400 | GO:0048208 COPII vesicle coat assembly (renamed from "COPII vesicle coating") |

Term labels were verified in OLS on 2026-05-24. Both `GO:0003400` and
`GO:0048208` are still live in OLS at the time of this check (the obsoletion
will become visible after the next GO release ingests PR #32013).

## Affected experimental annotations (from upstream spreadsheet)

11 EXP annotations across two groups (SGD 8, UniProt 3). Pulled from the
upstream Google Sheet on 2026-05-24:

| # | Group | Gene | Species | ID | PMID | Evidence | PANTHER | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | SGD | SAR1 | S. cerevisiae | SGD:S000006139 | PMID:14627716 | IDA | PTHR45684 | move to GO:0048208 |
| 2 | SGD | SAR1 | S. cerevisiae | SGD:S000006139 | PMID:15665868 | IDA | PTHR45684 | move to GO:0048208 |
| 3 | SGD | SED4 | S. cerevisiae | SGD:S000000663 | PMID:21291503 | IDA | PTHR23284 | move to GO:0048208 |
| 4 | SGD | PEF1 | S. cerevisiae | SGD:S000003290 | PMID:22792405 | IDA | PTHR46212 | move to GO:0048208 |
| 5 | SGD | PEF1 | S. cerevisiae | SGD:S000003290 | PMID:22792405 | IMP | PTHR46212 | move to GO:0048208 |
| 6 | SGD | PEF1 | S. cerevisiae | SGD:S000003290 | PMID:22792405 | IPI (with SGD:S000002354) | PTHR46212 | move to GO:0048208 |
| 7 | SGD | SEC12 | S. cerevisiae | SGD:S000005309 | PMID:8377826 | IDA | PTHR23284 | move to GO:0048208 |
| 8 | SGD | SEC23 | S. cerevisiae | SGD:S000006385 | PMID:8451644 | IDA | PTHR11141 | move to GO:0048208 |
| 9 | UniProt | SEC16A | H. sapiens | UniProtKB:O15027 | PMID:17005010 | IMP | PTHR13402 | move to GO:0048208 |
| 10 | UniProt | MAPK15 | H. sapiens | UniProtKB:Q8TD08 | PMID:24618899 | IMP | PTHR24055 | **DISPUTED — to be removed** (ValWood, per upstream issue body) |
| 11 | UniProt | PREB | H. sapiens | UniProtKB:Q9HCU5 | PMID:32358066 | IDA | PTHR23284 | move to GO:0048208 |

## Mappings flagged for redirection

- `unirule2go`: **UniRule:UR001628761** → GO:0003400. Verified live via
  UniProt REST on 2026-05-24. Condition set: PANTHER **PTHR23284** AND
  taxon ∈ {Mammalia (40674), Arabidopsis (3701), Ascomycota (4890)}. This
  is the SEC12/PREB/SED4 family (matches affected SGD SEC12 + SED4 and
  human PREB entries above), so a clean redirect to GO:0048208 (COPII
  vesicle coat assembly) is appropriate once the obsoletion lands. The
  human MAPK15 PTHR24055 entry is outside this rule's family condition and
  is independently handled by the disputed-annotation removal.

No InterPro2GO or UniProt-Keywords mappings to GO:0003400 were listed in the
upstream issue.

## Impact on this repo

No genes directly annotated to GO:0003400 are currently reviewed here.
Searches under `genes/` for SAR1, SED4, PEF1, SEC12, SEC23, SEC16A, MAPK15,
and PREB (and the UniProt accessions O15027, Q8TD08, Q9HCU5) returned no
matches on 2026-05-24. This means **no existing reviews need refresh** for
the obsoletion itself; the project is a queueing exercise that lines up
COPII machinery components for prospective review.

The repo currently has a related COPII track in
[`projects/`](.) only via the parallel vesicle-targeting / vesicle-tethering
obsoletions (`VESICLE_TARGETING_OBSOLETION.md`,
`SYNAPTIC_VESICLE_DOCKING_OBSOLETION.md`,
`ER_PM_TETHERING_OBSOLETION.md`,
`MITO_ER_TETHERING_OBSOLETION.md`,
`CILIARY_BASAL_BODY_DOCKING_OBSOLETION.md`), and via the yeast ERV14 review
(tracked separately in [#402](https://github.com/ai4curation/ai-gene-review/issues/402)
against [#6406](https://github.com/geneontology/go-annotation/issues/6406)
for COPII cargo receptor activity). Adding canonical COPII coating
components (SAR1, SEC23, SEC16) here would substantially strengthen the
ER-to-Golgi early-secretory-pathway coverage.

## Scope

- **Organisms**: S. cerevisiae (SAR1, SED4, PEF1, SEC12, SEC23) and human
  (SEC16A, PREB; MAPK15 is dispute-only). All 11 EXP rows are mammalian or
  fungal — no plant or invertebrate direct annotations are on the upstream
  list.
- **GO branches**: BP only. The replacement is in the same branch (parent
  `GO:0006901 vesicle coat assembly` / `GO:0048193 Golgi vesicle transport`),
  so existing parent classifications are preserved. No MF or CC overlap.
- **Type of fix**: terminological — annotated proteins genuinely participate
  in COPII coat formation (they *are* coat components or coat regulators
  that act as part of the pathway), and the obsoletion simply removes a
  spurious "regulation of …" framing. Most reviews can ACCEPT the
  replacement GO:0048208 as core function for the SAR1/SEC23/SEC16 family
  and KEEP_AS_NON_CORE for accessory regulators (SED4, PEF1).
- **Special case**: human MAPK15 (Q8TD08) annotation is disputed by the
  upstream curator and should be REMOVED rather than transferred. A MAPK15
  review here would need to evaluate PMID:24618899 directly and either
  confirm the removal or push back.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting. None
are currently in the repo.

### Tier 1 — canonical COPII coat GTPase + scaffold

1. **SAR1A** (human, UniProt **Q9NR31**) — small Ras-family GTPase that
   nucleates COPII coat assembly on the ER membrane after activation by
   SEC12 (the cognate GEF). The yeast `SAR1` entry on the upstream list
   (SGD:S000006139, PMID:14627716 and PMID:15665868) reflects the same
   biology; reviewing the human SAR1A is the highest-value anchor here
   because SAR1A is well-studied, has clear core function (GTPase activity
   driving COPII coat assembly), and serves a similar didactic role to
   CEP290 in the parallel cilia-obsoletion project.
2. **SEC23A** (human, UniProt **Q15436**) — inner-layer COPII coat subunit
   and SAR1 GAP. The yeast `SEC23` entry (SGD:S000006385, PMID:8451644)
   captures the canonical biochemistry. SEC23A loss-of-function causes
   cranio-lenticulo-sutural dysplasia, so the gene is also clinically
   well-characterised — a good complement to SAR1A.

### Tier 2 — coat-recruiting / scaffolding regulators with direct annotations

3. **SEC16A** (human, UniProt **O15027**) — the human direct-annotation
   target on the upstream list (PMID:17005010, IMP). SEC16A organises
   transitional-ER exit sites and recruits the SAR1/SEC23/SEC24 complex.
   Confirming GO:0048208 as core function and reviewing the broader
   ER-exit-site machinery annotations would be useful.
4. **PREB / SEC12** (human, UniProt **Q9HCU5**) — the human direct-annotation
   target on the upstream list (PMID:32358066, IDA). PREB is the mammalian
   SEC12 ortholog, a guanine nucleotide exchange factor for SAR1. Pairs
   naturally with the SAR1A review.

### Tier 3 — yeast-only entries (lower repo priority)

5. **Yeast SAR1, SEC12, SEC23, SED4, PEF1** (SGD) — the 8 SGD direct
   annotations cover the same biology as the human Tier 1/2 entries. A
   single human-anchored review per family is more efficient than separate
   yeast reviews, but the SED4 and PEF1 entries describe accessory
   regulators (SED4 = SEC12 paralog without measurable GEF activity in
   vitro; PEF1 = penta-EF-hand calcium-binding protein with a non-canonical
   regulatory role) that have no direct human equivalent in this repo yet,
   so a yeast PEF1 review would be worth adding once the canonical entries
   are in.

### Special case — disputed annotation

6. **MAPK15 / ERK7** (human, UniProt **Q8TD08**) — the disputed
   PMID:24618899 IMP annotation. Worth a focused review only if there is
   independent interest in MAPK15; for the obsoletion-tracking purpose, the
   simpler action is to wait for the upstream removal and not start a
   ground-up MAPK15 review here.

## Proposed approach

1. **Wait for the obsoletion to land before bulk-rewriting.** The upstream
   ontology ticket #31945 is CLOSED and the corresponding PR (#32013) was
   opened on 2026-04-22; the obsoletion + rename will be visible once a
   GO release ingests it. Reviews can proceed on the underlying biology
   now using the live GO:0048208 term ID (action codes ACCEPT / MODIFY /
   REMOVE are independent of the obsoletion timing).
2. **Begin with SAR1A (human)** as the anchor review. The COPII coat GTPase
   is the canonical example for the replacement term and has substantial
   biochemistry / cryo-EM literature for `core_functions` synthesis.
3. **Follow with SEC23A (human)** to cover the inner coat layer and the
   SAR1-GAP relationship — gives a paired review that exercises the
   GTPase / GAP partnership in one of the field's textbook examples.
4. **Add SEC16A and PREB** if the project expands beyond the GTPase /
   GAP pair, since they are the human entries actually on the upstream list.
5. **Defer the yeast-only entries** (SAR1, SEC12, SEC23, SED4, PEF1) and
   the disputed MAPK15 unless interest develops; the human Tier 1/2 reviews
   cover the biology more efficiently for this repo's audience.
6. **Cross-reference with the ERV14 COPII cargo receptor project**
   ([#402](https://github.com/ai4curation/ai-gene-review/issues/402),
   tracking [go-annotation#6406](https://github.com/geneontology/go-annotation/issues/6406))
   — that project covers the cargo-recognition side of COPII budding,
   which sits immediately downstream of the coat-assembly biology covered
   here.
7. **Flag the disputed MAPK15 annotation upstream** if interest develops in
   reviewing it locally; otherwise the upstream removal stands on its own.

## Priority

**Medium-low.** The biology is canonical and well-established, and no
existing reviews are blocked by the obsoletion (no SAR1 / SEC23 / SEC16 /
PREB reviews exist here yet). This is opportunistic — SAR1A and SEC23A in
particular are major unreviewed components of the early secretory pathway,
so the obsoletion is a reasonable trigger to start that coverage.

## Status

- 2026-05-24 — Project file created. Tracking upstream issue #6389 (opened
  2026-04-22). Upstream ontology ticket #31945 is CLOSED and PR #32013 has
  been opened to obsolete GO:0003400 + rename GO:0048208 and GO:0006901.
  Verified GO:0003400 and GO:0048208 still live in OLS on 2026-05-24;
  verified UniRule UR001628761 (PTHR23284, mammalian/Arabidopsis/Ascomycota
  scope) live in UniProt REST on 2026-05-24. No gene reviews started yet
  in this repo; none of the 11 affected genes are present under `genes/`.
