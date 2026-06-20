---
title: "Pfam → GO Mapping: A Precision Gap-Filling Experiment"
maturity: MATURE
tags: [PIPELINE]
---

# Pfam → GO Mapping: A Precision Gap-Filling Experiment

## Motivation

InterPro integrates several member databases (Pfam, PROSITE/PROFILE, SMART, CDD,
NCBIfam, PANTHER, …) and publishes a single curated GO mapping,
[InterPro2GO](https://current.geneontology.org/ontology/external2go/interpro2go),
which most pipelines (including GOA's IEA `with` pipeline) consume. Pfam is also
published with its own GO mapping,
[pfam2go](https://current.geneontology.org/ontology/external2go/pfam2go).

Because an InterPro entry frequently **lumps several member signatures together**,
the GO term attached to that entry must be general enough to cover all of them.
That raises a natural gap-filling hypothesis:

> **Hypothesis.** An individual Pfam family is often narrower than the InterPro
> entry it belongs to, so `pfam2go` might sometimes carry a **more specific** GO
> term than `interpro2go` — precision that never makes it into InterPro and could
> be harvested to enrich IEA annotation.

This project tests that hypothesis directly and reproducibly, and reports the
result honestly whether positive or negative.

## Method

For every Pfam family with a `pfam2go` mapping we:

1. Determine its parent InterPro entry from the **`<member_list>`** section of
   `interpro.xml` (a member signature integrates into exactly one entry; PFAM ids
   that appear in `contains`/`found_in` relationship sections are domain-architecture
   links, *not* membership, and are ignored — getting this wrong is the easiest way
   to manufacture spurious "gaps").
2. Compare each `pfam2go` GO term against the parent InterPro entry's
   `interpro2go` terms, over the GO `is_a` + `part_of` DAG (`go-basic`):
   - **SAME** — identical GO id already on the entry
   - **MORE_SPECIFIC** — a GO descendant of an entry term *(the hypothesis)*
   - **MORE_GENERAL** — a GO ancestor of an entry term (Pfam *less* specific)
   - **DISJOINT** — unrelated; split into whether the parent entry has any GO at
     all (no GO → release-skew artifact) or genuinely different terms
3. Separately count Pfam families with `pfam2go` terms that are **not integrated**
   into any InterPro entry (a pure InterPro2GO coverage gap).

The analysis is a single self-contained script,
[`analyze_pfam_go_gaps.py`](PFAM/analyze_pfam_go_gaps.py); full numbers and tables
are in the auto-generated [results page](PFAM/RESULTS.md).

## Result: the hypothesis is not supported

The full numbers are in [PFAM/RESULTS.md](PFAM/RESULTS.md). In summary, of the
**9,871** `pfam2go` assertions on integrated families:

| Category | Assertions | Distinct families |
|---|---:|---:|
| SAME (identical to InterPro entry) | 9,844 | — |
| **MORE_SPECIFIC (precision gain)** | **0** | **0** |
| MORE_GENERAL (Pfam less specific) | 1 | 1 |
| DISJOINT — genuine | 1 | 1 |
| DISJOINT — InterPro release skew | 25 | 13 |

**There is not a single case where `pfam2go` is more specific than its parent
InterPro entry.** This is unsurprising once you read the `pfam2go` header itself:

> *"This mapping is generated from data supplied by InterPro for the InterPro2GO
> mapping."*

Pfam-specific GO curation was discontinued; modern `pfam2go` is a **derived
projection** of `interpro2go` down to member signatures. ~99.7% of its assertions
are byte-identical to the parent entry's terms; the rest are explained by:

- **The one genuine difference runs the *other* way.** For `PF08214` (HAT_KAT11,
  sole member of `IPR016849` *Histone acetyltransferase Rtt109*), `interpro2go` is
  **more** precise — it has *histone **H3** acetyltransferase activity*
  (GO:0010484) where `pfam2go` only has the parent *histone acetyltransferase
  activity* (GO:0004402). The InterPro curator added specificity the Pfam mapping
  lacks. This is the opposite of the hypothesis.
- **Release skew, not signal.** The 25 remaining "disjoint" assertions (13
  families) all map to brand-new InterPro entries (`IPR06xxxx`) that carry *no*
  GO at all. Cause: the membership file is InterPro **release 109.0 (11 Jun 2026)**
  while the GO mapping snapshot is **28 Apr 2026** (≈ release 108). Those Pfams
  were re-integrated into newly minted entries the GO snapshot has not annotated
  yet. `pfam2go` merely **retains** the older term — a small *recall* advantage
  that disappears at the next InterPro2GO refresh, never a precision gain.
- **Three unintegrated families** (`PF04715`, `PF06009`, `PF13929`) carry only
  very high-level terms (*biosynthetic process*, *cell adhesion*, *mRNA
  stabilization*) — negligible and non-specific.

## Implications for AIGR / GO annotation

- **Do not mine `pfam2go` for extra precision over `interpro2go`.** For
  gene-review purposes the two are interchangeable; consuming InterPro2GO loses
  nothing. There is no low-hanging gap-filling fruit at the Pfam-vs-InterPro layer.
- The only operational nuance is the **recall lag**: immediately after an InterPro
  release that re-integrates a signature into a new entry, `pfam2go` can transiently
  retain GO terms that InterPro2GO has temporarily dropped. This is a versioning
  artifact to be aware of, not a curation resource.

## Where increased precision actually lives (follow-ups)

The negative result usefully redirects the search. Precision below the InterPro
entry level is more plausibly found by:

1. **InterPro's own hierarchy.** Child InterPro entries
   (`ParentChildTreeFile.txt`) already provide specific terms (e.g. a kinase
   *subfamily* entry); that precision is in InterPro2GO, not waiting in Pfam.
2. **Other member databases, especially subfamily-grained ones.** NCBIfam/TIGRFAM
   and HAMAP carry tight functional assignments, and **PANTHER subfamilies** are the
   real source of subfamily-level specificity (this is what the PAINT/IBA pipeline
   exploits). A `*2go`-style comparison of NCBIfam2go / panther subfamily mappings
   vs InterPro2GO is the logical next experiment.
3. **Per-protein curation** (UniProt, GOA experimental) — outside the scope of
   domain→GO mappings entirely.

See [PANTHER_IBA_REVIEW](PANTHER_IBA_REVIEW/) and
[IBA_REVIEW.md](IBA_REVIEW.md) for the subfamily-level direction.

## Reproducing

```bash
cd projects/PFAM
python3 analyze_pfam_go_gaps.py --download   # fetch + cache inputs into ./data, run
```

Inputs (cached under `PFAM/data/`, git-ignored; reproducible via `--download`):

- `pfam2go`, `interpro2go` — current.geneontology.org `external2go/`
- `interpro.xml.gz` — EBI InterPro FTP (`<member_list>` Pfam↔InterPro membership)
- `go-basic.obo` — current.geneontology.org (GO `is_a`/`part_of` DAG)

Outputs (committed):

- [`RESULTS.md`](PFAM/RESULTS.md) — human-readable summary (auto-generated)
- `PFAM/pfam_go_precision_gaps.tsv` — every classified assertion
- `PFAM/unintegrated_pfam_with_go.tsv` — pfam2go terms for unintegrated families

The script hardcodes no results and fabricates no mappings; if an input is missing
it errors out rather than guessing.
