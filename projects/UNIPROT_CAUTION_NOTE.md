---
title: "UniProt CAUTION Note Project"
---

# UniProt CAUTION Note Project

## Overview

UniProtKB records can carry one or more free-text **CAUTION** comments in the
flat file:

```
CC   -!- CAUTION: In contrast to other JHDM1 histone demethylases, it lacks the
CC       iron catalytic His in position 370 which is replaced by a Tyr residue
CC       and has no histone demethylase activity in vitro (PubMed:16362057). It
CC       therefore may not be functional in vivo. {ECO:0000305|PubMed:16362057}.
```

A CAUTION comment is a curator's explicit warning to the reader: a function is
**contested**, an activity was **mis-attributed**, a supporting paper was
**retracted**, a domain is **degenerate** (pseudo-enzyme), or a feature is a
likely **artifact**. These are exactly the situations where automated GO
annotation (IEA/IBA, domain-to-function mappings) is most likely to be wrong,
and where AI-assisted review adds the most value.

This project systematically harvests CAUTION comments from the UniProt records
already cached in this repository, categorizes them, and uses them as a
**prioritized worklist** for annotation review — a CAUTION note is a strong
signal that one or more existing GO annotations on that gene deserve scrutiny.

> **Yes, this is a real UniProt feature.** CAUTION is a standard UniProtKB
> "General annotation (Comments)" topic
> (<https://www.uniprot.org/help/caution>), distinct from the structured
> `SEQUENCE CAUTION` block. We confirmed **209 CAUTION comments across 201
> cached `*-uniprot.txt` records** in this repo (see data below).

## What counts here

We extract `CC   -!- CAUTION:` free-text comments and **exclude** the separate
structured `CC   -!- SEQUENCE CAUTION:` block (erroneous initiation / frameshift
/ predicted-gene-model issues), which is about sequence construction rather than
function.

## Data

### A. Local corpus (genes already fetched)

Extracted reproducibly by [`extract_caution_notes.py`](UNIPROT_CAUTION_NOTE/extract_caution_notes.py):

```bash
python3 projects/UNIPROT_CAUTION_NOTE/extract_caution_notes.py
```

Outputs (regenerated, not hand-edited):

- [`caution_notes.tsv`](UNIPROT_CAUTION_NOTE/caution_notes.tsv) — one row per note
  (organism, gene, UniProt ID, category, retracted flag, PMIDs, text)
- [`caution_notes.md`](UNIPROT_CAUTION_NOTE/caution_notes.md) — grouped human-readable report

### B. Database-wide survey (live UniProt REST API, no fetch-gene)

To see the global distribution without fetching anything, query the UniProt REST
API directly on the `cc_caution` field
([`uniprot_api_survey.py`](UNIPROT_CAUTION_NOTE/uniprot_api_survey.py)):

```bash
python3 projects/UNIPROT_CAUTION_NOTE/uniprot_api_survey.py            # all reviewed
python3 projects/UNIPROT_CAUTION_NOTE/uniprot_api_survey.py --organism 9606  # human only
```

Outputs: [`caution_uniprot_reviewed.tsv`](UNIPROT_CAUTION_NOTE/caution_uniprot_reviewed.tsv)
(raw per-entry download) and [`api_survey.md`](UNIPROT_CAUTION_NOTE/api_survey.md)
(aggregated report).

**Headline numbers (Swiss-Prot / reviewed, 2026-06-16):**

- **14,513** reviewed entries carry a CAUTION comment (vs 45,468 with the
  unrelated `SEQUENCE CAUTION` block — confirming `cc_caution` is the right field).
- **14,830** individual CAUTION notes; **~7,200** fall in high-signal categories.

| Category | Notes (DB-wide) | Curation value |
|----------|------:|----------------|
| contested-function | 3,035 | high |
| reclassified-function | 2,476 | high |
| degenerate-domain (pseudo-enzyme) | 1,366 | high |
| retracted-reference | 279 | high |
| possible-artifact | 63 | high |
| other | 7,605 | mixed (keyword classifier residual) |
| lacks-conserved-residue | 6 | low |

The WGS-preliminary boilerplate that dominated the *local* corpus essentially
**vanishes** in reviewed entries (0–6), confirming it was a TrEMBL/unreviewed
artifact rather than a curatorial signal.

**Distribution by organism** (top): Human (2,298 entries), *S. cerevisiae* (895),
Mouse (844), *A. thaliana* (714), *E. coli* K12 (334), Rat (329), Bovine (206),
*Dictyostelium* (192), *Drosophila* (160), Rice (150), *C. elegans* (122),
Zebrafish (109). Full table in `api_survey.md`.

### C. Prioritized review worklist (deeper dive)

[`shortlist_candidates.py`](UNIPROT_CAUTION_NOTE/shortlist_candidates.py)
cross-references the DB-wide survey against the accessions we have **already
fetched** (148 of our local genes overlap the reviewed-CAUTION set) and emits the
high-value entries we have **not** yet touched:

```bash
python3 projects/UNIPROT_CAUTION_NOTE/shortlist_candidates.py
```

Outputs: [`candidates_high_value.tsv`](UNIPROT_CAUTION_NOTE/candidates_high_value.tsv)
and [`candidates.md`](UNIPROT_CAUTION_NOTE/candidates.md).

**4,046 high-value, not-yet-reviewed candidates**: reclassified-function (2,401),
degenerate-domain (1,342), retracted-reference (255), possible-artifact (48).
Human alone contributes **95 pseudo-enzyme (degenerate-domain)** and **111
retracted-reference** candidates, e.g.:

- **RHBDF1** (Q96CC6) — "Lacks serine protease activity ... lacks the catalytic
  Ser residue at position 720" (iRhom pseudo-protease).
- **SUMF2** (Q8NBJ7) — "strongly similar to formylglycine-generating enzyme,
  lacks the catalytic Cys".
- **PANK4** (Q9NVE7) — pantothenate kinase domain is degenerate.
- **CHI3L1** (P36222), **SPACA3** (Q8IXA5) — glycosyl hydrolase folds with
  substituted catalytic residues.
- **ERCC8** (Q13216), **H3-3A/B** (P84243), **CBX1/CBX5** — annotations resting
  on retracted papers.

### D. First deep dive (batch 1)

[`deep_dive_batch1.md`](UNIPROT_CAUTION_NOTE/deep_dive_batch1.md) fetched 5 human
`degenerate-domain` candidates (RHBDF1, SUMF2, PANK4, DPYSL5, NAALADL2) and
checked their curated GO molecular functions against the CAUTION note. Key
results:

- **4 of 5 are already correctly handled by GO**, usually via an explicit
  `NOT|enables` on the lost catalytic term — frequently citing the *same* paper
  named in the CAUTION (RHBDF1↔PMID:21439629, PANK4↔PMID:30927326). The GO `NOT`
  qualifier is effectively the curated counterpart of the UniProt CAUTION.
- **One suspect over-annotation — DPYSL5 (CRMP5):** `GO:0004157`
  dihydropyrimidinase is correctly `NOT`-ed, while two positive **InterPro IEA**
  parent terms (`GO:0016787`, `GO:0016810` hydrolase activity) survive. This is
  *not* a logical contradiction (GO `NOT` propagates **down**, not up — so a
  negated child does not negate the parent), but it is an evidentially weak
  fold/domain-based propagation: the metal-site loss that justifies the `NOT`
  also removes the mechanistic basis for *any* metallo-hydrolase activity, with
  no positive evidence for an alternative → candidate `MARK_AS_OVER_ANNOTATED`.
- **Generalizable review flag:** look for a **positive IEA** parent term whose
  curated, more-specific **child is `NOT`-ed** (or whose activity a CAUTION
  reports as lost). Such pairs are logically admissible but flag a
  domain-based parent annotation that may have lost its evidential basis; the
  adjudication is then evidential, not logical.

### Local corpus tallies (cached records, for reference)


| Category | Count | Curation value | Description |
|----------|------:|----------------|-------------|
| contested-function | 44 | **high** | function is controversial / disputed / "however ..." |
| reclassified-function | 37 | **high** | "was originally/initially thought to be ..." |
| degenerate-domain | 16 | **high** | pseudo-enzyme; "lacks the catalytic/active-site residue" |
| retracted-reference | 12 | **high** | a supporting paper has been retracted |
| possible-artifact | 4 | **high** | result may be an experimental artifact |
| other | 38 | mixed | residual curatorial notes not matched by keywords |
| wgs-preliminary | 39 | low | boilerplate: sequence from a preliminary WGS entry |
| lacks-conserved-residue | 19 | low | boilerplate feature-propagation warning |
| **Total** | **209** | | across **201** records |

(Counts are produced by the script; rerun it after fetching new genes.)

## Why this matters for GO review

The high-value categories map directly onto well-known GO over-annotation
failure modes:

- **degenerate-domain / pseudo-enzyme** → domain-based IEA/IBA assigns a
  catalytic MF the protein cannot perform. Overlaps strongly with the
  [Contested Function project](CONTESTED_FUNCTION.md) and
  [Pseudoenzymes project](PSEUDOENZYMES.md).
- **reclassified-function** → the gene was historically placed in the wrong
  complex/pathway; legacy GO terms may persist (e.g. NDUFA4 "was initially
  believed to be a subunit of complex I").
- **retracted-reference** → annotations whose `original_reference_id` points to
  a retracted paper should be flagged `is_invalid` and the function re-examined.
- **contested-function / possible-artifact** → candidates for the schema's
  `finding_review` (`DISPUTED`) and `reference_review` machinery, or
  `KEEP_AS_NON_CORE` / `MARK_AS_OVER_ANNOTATED` actions.

## Featured examples (from the cached corpus)

- **SCHPO/Epe1** (O94603) — "lacks the iron catalytic His ... no histone
  demethylase activity in vitro ... may not be functional in vivo." Textbook
  pseudo-enzyme; already a flagship of [CONTESTED_FUNCTION](CONTESTED_FUNCTION.md).
- **human/NDUFA4** (O00483) — "Was initially believed to be a subunit of
  complex I" (it is a subunit of complex IV). Legacy complex-I GO terms are the
  risk.
- **human/AKT1** (P31749) — two CAUTION notes flag **retracted** papers
  (PUBMED:20231902, PUBMED:19940129) plus an isoform-redundancy caveat.
- **human/PARK7 / DJ-1** (Q99497) — glyoxalase vs deglycase activity is
  explicitly called **controversial**; a clean test case for contested MF.
- **human/IL4I1** (Q96RQ9) — an enzymatic-independence claim is flagged as
  needing confirmation (only Phe, not Trp, deprivation was tested).
- **human/UCHL1** (P09936) — disease association and ubiquitin-ligase activity
  both flagged as contested across conflicting papers.
- **SACEN/eryCII** (Q939Z0) — "related to the cytochrome P450 family, lacks the
  heme-binding sites"; pseudo-enzyme that is actually a glycosyltransferase
  activator (already reviewed under CONTESTED_FUNCTION).
- **ARATH/CRY1, CRY2** — "Was originally thought to be a DNA photolyase"
  (cryptochromes are photoreceptors, not repair enzymes).

## Workflow

1. (Re)generate the worklist: run `extract_caution_notes.py`.
2. Prioritize the high-value categories (contested / reclassified /
   degenerate-domain / retracted / possible-artifact).
3. For each gene that **already has** a `*-ai-review.yaml`, check whether its
   existing annotations are consistent with the CAUTION note; if a retracted
   PMID is an `original_reference_id`, flag it.
4. For genes without a review yet, treat the CAUTION note as a strong reason to
   prioritize a full review (`just fetch-gene <org> <gene>`).
5. Record findings using `reference_review` (retracted → `is_invalid`),
   `finding_review` (`DISPUTED`), and appropriate annotation `action`s.

## Related projects

- [CONTESTED_FUNCTION.md](CONTESTED_FUNCTION.md)
- [PSEUDOENZYMES.md](PSEUDOENZYMES.md)
- [OVER_ANNOTATION_PATTERNS.md](OVER_ANNOTATION_PATTERNS.md)
- [CONTESTED_FUNCTION.md](CONTESTED_FUNCTION.md) (finding-level dispute tracking)

---

# STATUS

## Done
- [x] Confirmed UniProt CAUTION comments exist and are present in the cached
  corpus (209 notes / 201 records).
- [x] Wrote reproducible local extractor `extract_caution_notes.py`.
- [x] Surveyed the **whole reviewed UniProt** via the REST API
  (`uniprot_api_survey.py`): 14,513 entries / 14,830 notes, with category and
  per-organism distributions — no `fetch-gene` required.
- [x] Built `shortlist_candidates.py` → 4,046 high-value, not-yet-reviewed
  candidates (`candidates_high_value.tsv`, `candidates.md`).
- [x] **Deep dive batch 1** (`deep_dive_batch1.md`): fetched RHBDF1, SUMF2,
  PANK4, DPYSL5, NAALADL2; found 4/5 already correctly negated by GO and **1
  suspect domain-based over-annotation (DPYSL5 hydrolase IEAs — evidentially
  weak, not a logical contradiction)**.

- [x] **DPYSL5 (CRMP5) full review** written and validated
  (`genes/human/DPYSL5/DPYSL5-ai-review.yaml`, DRAFT): `REMOVE` on the two IEA
  hydrolase over-annotations (`GO:0016787`, `GO:0016810`), `ACCEPT` on the curated
  `NOT`s, core function = negative regulation of dendrite morphogenesis.

- [x] **All 5 batch-1 reviews completed** and validated (RHBDF1, SUMF2, PANK4,
  NAALADL2 + DPYSL5). DPYSL5 was the only one needing a `REMOVE` of a positively
  asserted catalytic term; PANK4 is a domain-swap pseudoenzyme (dead PanK domain
  + real, correctly annotated 4'-phosphopantetheine phosphatase).

## Pending
- [ ] Scale the "positive-IEA-catalytic + curated-NOT" conjunction query across
  the 1,342 degenerate-domain candidates to auto-surface over-annotations.
- [ ] Audit the 255 retracted-reference candidates for retracted
  `original_reference_id`s in existing reviews.
- [ ] Scale the "positive-IEA-catalytic + curated-NOT" conjunction query across
  the 1,342 degenerate-domain candidates to auto-surface over-annotations.
- [ ] Audit retracted-reference candidates for retracted `original_reference_id`s
  in any existing review.
- [ ] Refine the keyword classifier to shrink the large "other" bucket (7,605
  DB-wide notes) — many are genuine but unmatched.
- [ ] Add a `just` target to regenerate the survey + shortlist on demand.

Last updated: 2026-06-16

# NOTES

## 2026-06-16

**Project creation.** Verified the premise before building: UniProt CAUTION is a
real, documented comment topic, and `grep -c '\-!- CAUTION:'` across the cached
`*-uniprot.txt` files returns 209 matches in 201 records. Built a parser that
correctly handles multi-line CAUTION comments and excludes the structured
`SEQUENCE CAUTION` block. Keyword categorizer separates curation-meaningful
notes (contested / reclassified / degenerate-domain / retracted / artifact) from
automatic boilerplate (WGS-preliminary, lacks-conserved-residue). The
degenerate-domain bucket overlaps heavily with existing CONTESTED_FUNCTION and
PSEUDOENZYMES work, confirming CAUTION notes are a good signal for finding
over-annotated catalytic functions.

**API survey added (same day).** Per request, queried the live UniProt REST API
on the `cc_caution` field (distinct from `cc_sequence_caution`) to get a
database-wide distribution without fetching genes: 14,513 reviewed entries,
14,830 notes, ~7,200 high-signal. Human dominates (2,298). Cross-referencing
against the 148 reviewed-CAUTION genes we already have yields a 4,046-entry
high-value worklist — the basis for a prioritized deep dive (starting with human
pseudo-enzymes flagged by degenerate-domain cautions).
