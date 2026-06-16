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

Extracted reproducibly by [`extract_caution_notes.py`](UNIPROT_CAUTION_NOTE/extract_caution_notes.py):

```bash
python3 projects/UNIPROT_CAUTION_NOTE/extract_caution_notes.py
```

Outputs (regenerated, not hand-edited):

- [`caution_notes.tsv`](UNIPROT_CAUTION_NOTE/caution_notes.tsv) — one row per note
  (organism, gene, UniProt ID, category, retracted flag, PMIDs, text)
- [`caution_notes.md`](UNIPROT_CAUTION_NOTE/caution_notes.md) — grouped human-readable report

### Current tallies (cached records as of 2026-06-16)

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
- [x] Wrote reproducible extractor `extract_caution_notes.py`.
- [x] Generated categorized worklist (`caution_notes.tsv`, `caution_notes.md`).

## Pending
- [ ] Cross-reference high-value notes against existing `*-ai-review.yaml` files
  to find annotations contradicted by a CAUTION note.
- [ ] Audit the 12 retracted-reference genes for retracted `original_reference_id`s.
- [ ] Triage the 38 "other" notes; promote genuine cases into the high-value
  categories or refine the classifier.
- [ ] Add a `just` target / CI hook to regenerate the worklist when genes are added.

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
