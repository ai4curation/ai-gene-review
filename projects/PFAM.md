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
result honestly whether positive or negative. It has **two parts**:

1. **Does the *existing* `pfam2go` already carry hidden precision?** (No — it is a
   derived copy of InterPro2GO; see below.)
2. **Is there headroom to author *new* Pfam→GO mappings with more precision than
   InterPro2GO gives?** This is the generative question and the more interesting
   one; see [HEADROOM.md](PFAM/HEADROOM.md).

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

## Part 1 — The existing `pfam2go` adds no precision

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

## Part 2 — Headroom for *new* mappings (the generative question)

Since the existing file is a copy, the real question is whether one *could* author
new per-Pfam mappings that beat InterPro2GO. The script
[`headroom_analysis.py`](PFAM/headroom_analysis.py) measures the opportunity
against the full Pfam-A universe (30,134 families) without inventing any mapping;
full numbers in [HEADROOM.md](PFAM/HEADROOM.md). Two routes were tested:

**Route A — "splitting" lumped entries: essentially no headroom.** The premise was
that InterPro lumps several functionally-distinct Pfams under one general GO term.
Empirically this barely happens for GO-bearing entries: only **76** InterPro
entries with a GO term have ≥2 Pfam members at all (184 families), and just **4**
are Family/Homologous-superfamily. The rest are *Repeat*/*Domain* entries whose
multiple Pfam members are **redundant HMM signatures of the same domain** (e.g. the
GNAT acyltransferase or EF-hand entries list several alternative Pfam models) — a
per-Pfam term would be identical, not finer. GO-bearing InterPro entries are
overwhelmingly 1 Pfam = 1 entry, so **InterPro2GO already sits at Pfam
granularity**; there is nothing to split.

**Route B — coverage: a large opportunity, and where coverage meets precision.**
The dominant finding is how *little* of Pfam is GO-annotated through InterPro at all:

| | Pfam-A families | % |
|---|---:|---:|
| Total | 30,134 | 100% |
| Get ≥1 GO via InterPro (covered) | 5,246 | 17.4% |
| **Zero GO via InterPro** | **24,888** | **82.6%** |
| …of those, DUF / unknown function | 6,529 | 26% of gap |
| …named, tractable targets | 18,359 | 74% of gap |

Crucially, InterPro2GO is **conservative**: even canonical, well-understood domains
are left unmapped — SH2 (IPR000980), EGF (IPR000742), Kringle (IPR000001), Actin
(IPR004000) all have **no** interpro2go term. For these, a new mapping is not
boxed in by an existing general term, so it can be authored *directly at a specific
level* (e.g. SH2 → phosphotyrosine residue binding, GO:0001784). **Here coverage
and precision coincide.**

**Bottom line for the generative question:** yes, new mappings can beat
InterPro2GO — but by **annotating where InterPro abstained** (the ~18k named
uncovered families, often at a specific level) and by going **below the family**
(clan subfamilies, domain architectures, active-site/residue signatures, structure)
to refine the ~5k already-covered families — *not* by splitting lumped entries.
Realizing it means *authoring* mappings (curation or grounded model prediction) and
validating them; `pfam2go` does none of this today.

### Worked proposals: Pfam families curated as their own entries

The concrete output is **9 Pfam families curated as their own entries** under
`interpro/pfam/<PFAM>/<PFAM>-review.yaml` — sidecars to the machine-fetched
`<PFAM>-metadata.yaml`, mirroring the existing `interpro/panther/<PTHR>/` layout.
Candidates were drawn from the sharpest "InterPro not viable" category — **heterogeneous
InterPro entries** that lump functionally distinct Pfams under one shared fold (so a
specific term would be wrong on the whole entry; those entries carry **no** interpro2go
term). But each candidate was then **verified against the actual reviewed SwissProt
membership of the Pfam itself** — the decisive test of whether the HMM tracks the
evolved function or is merely *named* after it. That verification split the nine:

**5 proposed** (member-verified; family is function-specific):

| Pfam | family | proposed GO | supporting member | counter-example (why not InterPro) |
|---|---|---|---|---|
| [PF27512](../../interpro/pfam/PF27512/PF27512-review.yaml) | LeuD | 3-isopropylmalate dehydratase activity (GO:0003861) + L-leucine biosynth (GO:0009098) | LEUD_ECOLI (EC 4.2.1.33) | aconitase ACO1 (PF00694 sibling, EC 4.2.1.3) |
| [PF02431](../../interpro/pfam/PF02431/PF02431-review.yaml) | Chalcone | chalcone isomerase activity (GO:0045430) | CFI1_ARATH (EC 5.5.1.6) | FAP1/FAP2 non-catalytic CHIL (PF16035, no EC) |
| [PF07228](../../interpro/pfam/PF07228/PF07228-review.yaml) | SpoIIE | sporulation (GO:0030435) | **SP2E_BACSU — `genes/BACSU/spoIIE`** (in-repo review) | generic PP2Cs PPM1D/F (PF00481) |
| [PF09043](../../interpro/pfam/PF09043/PF09043-review.yaml) | Lys-AminoMut_A | D-lysine 5,6-aminomutase activity (GO:0047826) | KAMD_ACESD (EC 5.4.3.3) | OAM α (PF16552 sibling, EC 5.4.3.5) |
| [PF16552](../../interpro/pfam/PF16552/PF16552-review.yaml) | OAM_alpha | D-ornithine 4,5-aminomutase activity (GO:0047831) | OAMS_ACESD (EC 5.4.3.5) | 5,6-LAM α (PF09043 sibling, EC 5.4.3.3) |

**4 rejected** — the family is named for a function, but its reviewed members are
functionally heterogeneous (a counter-example sits in the **same** Pfam), so the term
would over-annotate even at the Pfam level. These are kept as `status: REJECTED` entries
because the verification result is itself the useful product:

| Pfam | family | term that does NOT hold | same-family counter-example |
|---|---|---|---|
| [PF14681](../../interpro/pfam/PF14681/PF14681-review.yaml) | UPRTase | uracil PRTase (GO:0004845) | UCKL1/URK1 uridine kinases (EC 2.7.1.48) — despite real Upp (P0A8F0) also being a member |
| [PF16363](../../interpro/pfam/PF16363/PF16363-review.yaml) | GDP_Man_Dehyd | GDP-Man 4,6-dehydratase (GO:0008446) | GALE epimerase (5.1.3.2), UXS1 decarboxylase (4.1.1.35) |
| [PF13360](../../interpro/pfam/PF13360/PF13360-review.yaml) | PQQ_2 (BamB) | OM assembly (GO:0043165) | RqkA protein kinase (2.7.11.1), PedH dehydrogenase (`genes/PSEPK/pedH`) |
| [PF13561](../../interpro/pfam/PF13561/PF13561-review.yaml) | adh_short_C2 | enoyl-ACP reductase (GO:0016631) | FabG ketoacyl-ACP reductase (1.1.1.100) in the same family as FabI |

An index of both groups is in [PROPOSED_MAPPINGS.md](PFAM/PROPOSED_MAPPINGS.md).

**Why entry-centric rather than SSSOM.** A flat subject→predicate→object row cannot
structurally hold what this review needs: the parent InterPro entry and its
type/membership, the member families that make the entry heterogeneous, the
`mapping_viability` judgement and reason, and — per proposed term — relation, aspect,
confidence, status, plus **`supporting_examples` and `counter_examples`** (characterized
SwissProt members, linked to in-repo gene reviews where they exist). Each Pfam is
therefore curated as a first-class **entry** (LinkML schema
[`pfam_entry_review.yaml`](../../src/ai_gene_review/schema/pfam_entry_review.yaml)) under
`interpro/pfam/`. GO targets are id/label tuples bound to a GO-branch enum, so
`linkml-term-validator` checks every term resolves and its label matches.

The examples are **hand-picked and verified against UniProt** (reviewed entries only).
[`validate_pfam_reviews.py`](PFAM/validate_pfam_reviews.py) then checks the structural
claims a schema can't — Pfam membership of the parent entry, the member list, GO
non-obsolete/aspect, that the parent entry carries no equivalent term, that every
`gene_review` path exists, and that each `REJECTED` term is backed by a same-family
counter-example — and refreshes the index. All nine pass `just validate-pfam-reviews`.
Each PROPOSED annotation remains a **candidate needing curator / experimental
validation**, not an asserted fact.

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
python3 analyze_pfam_go_gaps.py --download   # Part 1: existing pfam2go vs interpro2go
python3 headroom_analysis.py                 # Part 2: headroom for new mappings
python3 validate_pfam_reviews.py             # Part 2: validate the hand-curated reviews + refresh index
just validate-pfam-reviews                   # the above + LinkML structural + GO-label validation
```

The `interpro/pfam/<PFAM>/<PFAM>-review.yaml` files are **hand-curated** (examples
verified against UniProt); the script validates them, it does not generate them. Pfam
entry metadata is fetched separately with `just fetch-interpro-family pfam <PFAM>` into
`interpro/pfam/<PFAM>/`.

Inputs (cached under `PFAM/data/`, git-ignored; reproducible via `--download`):

- `pfam2go`, `interpro2go` — current.geneontology.org `external2go/`
- `interpro.xml.gz` — EBI InterPro FTP (`<member_list>` membership + entry types)
- `go-basic.obo` — current.geneontology.org (GO `is_a`/`part_of` DAG)
- `Pfam-A.clans.tsv.gz` — Pfam FTP (full family universe + clan + description; fetch
  manually for `headroom_analysis.py`)

Outputs (committed):

- [`RESULTS.md`](PFAM/RESULTS.md) — Part 1 summary (auto-generated)
- [`HEADROOM.md`](PFAM/HEADROOM.md) — Part 2 summary (auto-generated)
- `interpro/pfam/<PFAM>/<PFAM>-review.yaml` — **curated Pfam entry reviews** (9 families:
  5 proposed, 4 rejected-on-verification), schema
  [`pfam_entry_review.yaml`](../../src/ai_gene_review/schema/pfam_entry_review.yaml);
  index in [`PROPOSED_MAPPINGS.md`](PFAM/PROPOSED_MAPPINGS.md), validated by `validate_pfam_reviews.py`
- `PFAM/pfam_go_precision_gaps.tsv` — Part 1 non-SAME classified assertions
- `PFAM/unintegrated_pfam_with_go.tsv` — pfam2go terms for unintegrated families
- `PFAM/lumped_entries_headroom.tsv` — multi-Pfam GO-bearing entries, ranked
- (`data/pfam_no_go_coverage_gap.tsv` — full ~25k-row coverage gap list, git-ignored,
  regenerable)

The scripts hardcode no results and fabricate no mappings; if an input is missing
they error out rather than guessing.
