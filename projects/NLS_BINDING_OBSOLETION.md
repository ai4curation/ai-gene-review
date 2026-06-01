# Nuclear Localization Sequence Binding — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will retire **GO:0008139 nuclear localization
sequence binding** (MF) and replace it with **GO:0140142 nucleocytoplasmic
carrier activity**. This is part of the broader "signal sequence binding
and children" refactor in go-ontology#31419 (CLOSED), which moves the
sub-tree of `GO:0005048 signal sequence binding` from a generic *binding*
formulation to a *non-binding receptor / carrier* formulation. The sibling
"mitochondrion targeting sequence binding" obsoletion (go-annotation#6437)
is tracked separately in
[`projects/MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md`](MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md).

The replacement term `GO:0140142 nucleocytoplasmic carrier activity` is
defined as "Binding to and carrying a cargo between the nucleus and the
cytoplasm by moving along with the cargo. The cargo can be either a RNA or
a protein." This is the canonical importin / karyopherin / exportin MF and
fits the experimental annotations on KPNA / KPNB / TNPO / IPO / PSE1 /
KAP104 / KAP123 / MTR10 etc. However, several GO:0008139 annotations are
on proteins that **bind** an NLS without **carrying** it across the
nuclear pore (e.g. nucleoporins Nup98/Nup153/Nup214/Nup58, the nucleolar
NSR1, IκBα/NFKBIA, BRAP, Su(fu), CABP1, Nolc1). For these, the upstream
proposal is to evaluate case-by-case — some will move to GO:0140142,
others to alternative MFs (e.g. structural constituent of nuclear pore,
`GO:0050839 cell adhesion molecule binding`-style cargo-binding terms, or
removal when the assertion no longer holds under current evidence
standards).

This project queues the affected genes for prospective review, since
**none of the directly annotated genes are currently in this repository.**

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6435](https://github.com/geneontology/go-annotation/issues/6435) (opened 2026-05-27)
- Ontology ticket: [geneontology/go-ontology#31419](https://github.com/geneontology/go-ontology/issues/31419) (CLOSED — "Review 'signal sequence binding' and children", high priority, MF refactoring)
- Sibling sub-issues from the same refactor that are tracked here:
  - **go-annotation#6437** mitochondrion targeting sequence binding → [`MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION`](MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION.md)
  - **go-annotation#6383** ER-PM tethering (different parent, same refactor wave) → [`ER_PM_TETHERING_OBSOLETION`](ER_PM_TETHERING_OBSOLETION.md)
  - Peroxisome targeting signal binding (also under `GO:0005048`) → [`PEROXISOME_TARGETING_SIGNAL_OBSOLETION`](PEROXISOME_TARGETING_SIGNAL_OBSOLETION.md)
- Affected annotations spreadsheet (upstream): https://docs.google.com/spreadsheets/d/1NLoo-WPT-6YpYDKVbUqrOHZSnOkIbDVtj4OB2s5Cx3M/edit?gid=779903919
- FYPO usage: FYPO:0007070 uses GO:0008139 as a UbergraphImplementation relationship object (will need to follow the GO change).

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| nuclear localization sequence binding (MF) | GO:0008139 | GO:0140142 nucleocytoplasmic carrier activity (case-by-case; some annotations may map to a different MF or be removed) |

Term status verified in OLS on 2026-06-01:

- **GO:0008139** (`nuclear localization sequence binding`) — live (`isObsolete: false`); synonyms: NLS binding, nuclear localization signal binding, nuclear localisation sequence binding.
- **GO:0140142** (`nucleocytoplasmic carrier activity`) — live, has children; synonyms: miRNA transporter activity, nucleocytoplasmic importin/exportin activity, pre-miRNA transporter activity.
- The ontology ticket #31419 is CLOSED, so the upstream agreement that GO:0008139 should be obsoleted is settled; the per-annotation remapping work in go-annotation#6435 is still open.

## Affected experimental / curated annotations

The upstream issue tallies direct annotations by source DB:

| Source | Count | Status |
|---|---|---|
| UniProt | 10 | Open |
| SGD | 7 | Open |
| RGD | 6 | Open |
| PINC | 5 | Open |
| FlyBase | 2 | Open |
| ParkinsonsUK-UCL | 2 | Open |
| MGI | 1 | Open |
| PomBase | 1 | **DONE** (struck through upstream) |

Pulled via QuickGO REST on 2026-06-01 (manual + experimental evidence
filters, plus PINC ECO:0000304 author-statement entries):

### UniProt (10)

| # | Accession | Symbol | Organism (taxon) | Evidence | Reference |
|---|---|---|---|---|---|
| 1 | F4JL11 | IMPA2 | A. thaliana (3702) | IMP | PMID:37676567 |
| 2 | O00629 | KPNA4 | H. sapiens (9606) | IDA | PMID:20818336 |
| 3 | O00629 | KPNA4 | H. sapiens (9606) | IDA | PMID:38512451 |
| 4 | O88751 | Cabp1 | R. norvegicus (10116) | IDA | PMID:18303947 |
| 5 | P25963 | NFKBIA (IκBα) | H. sapiens (9606) | IPI | PMID:1493333 |
| 6 | P52292 | KPNA2 | H. sapiens (9606) | IDA | PMID:17324944 |
| 7 | P52292 | KPNA2 | H. sapiens (9606) | IDA | PMID:28991411 |
| 8 | Q19969 | ima-3 | C. elegans (6239) | IDA | PMID:31417366 |
| 9 | Q8TEX9 | IPO4 | H. sapiens (9606) | IDA | PMID:17682055 |
| 10 | Q96321 | IMPA1 | A. thaliana (3702) | IMP | PMID:37676567 |

### SGD (7) — all *S. cerevisiae* (taxon 559292)

| # | Accession | Symbol | Evidence | Reference |
|---|---|---|---|---|
| 1 | P27476 | NSR1 | IDA | PMID:1706724 |
| 2 | P32337 | PSE1 / KAP121 | IDA | PMID:11694505 |
| 3 | P38217 | KAP104 | IDA | PMID:9488461 |
| 4 | P38748 | ETP1 | IDA | PMID:9497340 |
| 5 | P40069 | KAP123 | IDA | PMID:11694505 |
| 6 | Q02932 | KAP120 | IDA | PMID:20219973 |
| 7 | Q99189 | MTR10 / KAP111 | IDA | PMID:9545233 |

### RGD (6 manual/experimental) — *R. norvegicus* (taxon 10116)

| # | Accession | Symbol | Evidence | Reference |
|---|---|---|---|---|
| 1 | D4ACK1 | Nup214 | IDA | PMID:7878057 |
| 2 | O08984 | Lbr | IPI | PMID:8486604 |
| 3 | P41777 | Nolc1 | IDA | PMID:1623516 |
| 4 | P49791 | Nup153 | IDA | PMID:7878057 |
| 5 | P49793 | Nup98 | IDA | PMID:7878057 |
| 6 | P70581 | Nup58 | IDA | PMID:8707840 |

(RGD also has 5 additional ECO:0000266 ortholog-projection entries on
Brap, Ipo4, Kpna4, Nfkbia, Kpna2 against GO_REF:0000121 — these follow
the manual annotations on the corresponding human genes and will
update automatically.)

### PINC (5) — all *H. sapiens* (taxon 9606), ECO:0000304 (TAS)

| # | Accession | Symbol | Reference |
|---|---|---|---|
| 1 | O00505 | KPNA3 | PMID:9435235 |
| 2 | O14787 | TNPO2 | PMID:9298975 |
| 3 | P52294 | KPNA1 | PMID:7754385 |
| 4 | Q14974 | KPNB1 | PMID:7627554 |
| 5 | Q92973 | TNPO1 | PMID:8808633 |

### FlyBase (2) — *D. melanogaster* (taxon 7227)

| # | Accession | Symbol | Evidence | Reference |
|---|---|---|---|---|
| 1 | O76521 | Kap-alpha1 | IDA | PMID:26887950 |
| 2 | Q9VG38 | Su(fu) | IPI | PMID:24413177 |

(A third FlyBase entry, Q9VRV8 Tnpo, is ISS — follows manual human TNPO1/2.)

### ParkinsonsUK-UCL (2)

| # | Accession | Symbol | Organism | Evidence | Reference |
|---|---|---|---|---|---|
| 1 | O88751 | Cabp1 | R. norvegicus | IDA | PMID:18303947 |
| 2 | P83953 | Kpna1 | R. norvegicus | IDA | PMID:18303947 |

### MGI (1)

| # | Accession | Symbol | Organism | Evidence | Reference |
|---|---|---|---|---|---|
| 1 | Q7Z569 | BRAP | H. sapiens (9606) | IDA | PMID:9497340 |

(Q99MP8 mouse Brap is ISS and follows automatically.)

### PomBase — DONE upstream

| # | Accession | Symbol | Organism | Evidence | Reference | Status |
|---|---|---|---|---|---|---|
| ✓ | O14063 | cut15 | *S. pombe* (taxon 284812) | IDA | PMID:9740803 | already remapped per upstream |

### IEA / IBA scope (not enumerated)

QuickGO reports **18,125 total annotations** to GO:0008139 across all
sources. The bulk are IEA ortholog projections (GO_REF:0000120 /
GO_REF:0000117) and IBA PAINT projections (GO_REF:0000033) — the IBA
projections fan out from the experimentally annotated importin/karyopherin
genes above. Once the manual annotations are remapped to GO:0140142, the
IBA/IEA fanout will be regenerated automatically by PAINT and the UniProt
inference pipeline.

## Mappings flagged for redirection

The upstream issue body explicitly flags **one** InterPro2GO mapping:

| Source | Mapping ID | Description | Current target | Action |
|---|---|---|---|---|
| InterPro2GO | IPR024882 | Nucleoporin p58/p45/NUP49 | GO:0008139 | redirect (likely *structural constituent of nuclear pore complex* GO:0017056 rather than carrier activity, since p58/p45/NUP49 are pore components not importins) |

No UniRule or UniProt-Keywords mappings to GO:0008139 are listed upstream.

The FYPO term **FYPO:0007070** uses GO:0008139 as a relationship object
in its UbergraphImplementation — it will need to follow the GO change
when the obsoletion is implemented.

## Impact on this repo

**None of the affected genes are currently reviewed here** (searches for
KPNA1, KPNA2, KPNA3, KPNA4, KPNB1, TNPO1, TNPO2, IPO4, IMPA1, IMPA2,
NFKBIA, BRAP, Cabp1, Su(fu), Kap-alpha1, NSR1, PSE1, KAP104, KAP120,
KAP123, MTR10, ETP1, Nup58, Nup98, Nup153, Nup214, Nolc1, Lbr, cut15,
ima-3 returned no matches under `genes/` on 2026-06-01). This means
**no existing reviews need refresh** for the obsoletion itself; the
project is a queueing exercise that lines up the importin/karyopherin
family for prospective review.

## Scope

- **Organisms**: Human (10 direct: KPNA1-4, KPNB1, TNPO1, TNPO2, IPO4,
  NFKBIA, BRAP), *S. cerevisiae* (7), *R. norvegicus* (6 + 2 from
  ParkinsonsUK-UCL), *D. melanogaster* (2), *C. elegans* (1: ima-3),
  *A. thaliana* (2: IMPA1, IMPA2). Total ~28 manual/experimental
  annotations across ~25 distinct gene products.
- **GO branches**: MF only. The replacement GO:0140142 sits under
  `GO:0005215 transporter activity` rather than `GO:0005488 binding`,
  which is the explicit semantic shift driving go-ontology#31419
  (binding-without-transport is no longer appropriate when the protein
  actually *carries* the cargo through the NPC).
- **Type of fix**: terminological + per-annotation triage. The bulk
  (importins / karyopherins / exportins) move cleanly to GO:0140142.
  The exceptions are:
  - **Nucleoporins** (Nup58, Nup98, Nup153, Nup214) — these are NPC
    structural components, not carriers. The annotation likely came
    from interaction assays with karyopherins / FG-repeat–binding,
    and the right replacement is probably GO:0017056 *structural
    constituent of nuclear pore* rather than GO:0140142.
  - **NFKBIA / IκBα** (PMID:1493333) — IκBα masks the NLS of NF-κB
    p65/RelA; the "binding" assay measures IκBα binding to the NLS
    region of p65, not nuclear-pore transit. The right replacement
    is probably a transcription-factor-binding term or simply removal.
  - **Su(fu)** (PMID:24413177) — Su(fu) binds the NLS of Ci/Gli to
    retain it in the cytoplasm (Hedgehog signaling). Again, not a
    carrier; likely keep as a cargo-retention / NLS-masking MF or
    remove.
  - **NSR1**, **Nolc1**, **Cabp1**, **Lbr**, **BRAP**, **ETP1** —
    each needs literature triage to determine whether the original
    assay supports a carrier role (→ GO:0140142) or a different
    interaction role (→ alternative MF or remove).
- **Special case (FYPO dependency)**: when GO:0008139 is obsoleted,
  FYPO:0007070's UbergraphImplementation needs to be updated upstream;
  no action required from this repo.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting.
None are currently in `genes/`.

### Tier 1 — canonical karyopherins with multiple high-quality IDA annotations

1. **KPNA2** (human, UniProt **P52292**) — importin-α1; two independent
   IDA annotations (PMID:17324944, PMID:28991411) plus extensive IBA
   fanout. Canonical NLS-recognition receptor; clean GO:0140142
   replacement. Good entry point for the importin-α family.
2. **KPNA4** (human, UniProt **O00629**) — importin-α3; two
   IDA annotations (PMID:20818336, PMID:38512451). Pair naturally
   with KPNA2 review.
3. **KPNB1** (human, UniProt **Q14974**) — importin-β1; PINC TAS
   annotation (PMID:7627554). Textbook importin-β / RanGTP-cycle
   nuclear import receptor; clean carrier-activity case and the
   anchor for all KPNA/KPNB IBA propagations.
4. **IPO4** (human, UniProt **Q8TEX9**) — importin-4 / RanBP4; IDA
   PMID:17682055. Histone H3/H4 import; clean carrier case.

### Tier 2 — yeast importins (PAINT seeds)

5. **PSE1 / KAP121** (*S. cerevisiae*, UniProt **P32337**) — IDA
   PMID:11694505. Spo1 / pheromone-response NLS receptor.
6. **KAP104** (*S. cerevisiae*, UniProt **P38217**) — IDA PMID:9488461.
   hnRNP NLS receptor; the founding β-karyopherin for mRNA-binding
   protein import.
7. **KAP123** (*S. cerevisiae*, UniProt **P40069**) — IDA PMID:11694505.
   Ribosomal protein import; pairs with PSE1.
8. **MTR10 / KAP111** (*S. cerevisiae*, UniProt **Q99189**) — IDA
   PMID:9545233. mRNA-binding protein import receptor.

### Tier 3 — non-importin annotations that need triage

9. **NFKBIA / IκBα** (human, UniProt **P25963**) — IPI PMID:1493333.
   Diagnostic case: the GO:0008139 annotation reflects NLS-*masking*,
   not NLS-*carrying*. The right call may be REMOVE or MODIFY to a
   transcription-factor-binding term. This is the most interesting
   review of the set.
10. **Su(fu)** (*D. melanogaster*, UniProt **Q9VG38**) — IPI
    PMID:24413177. NLS-masking on Ci/Gli; similar triage to NFKBIA.
11. **Nup98** (*R. norvegicus*, UniProt **P49793**), **Nup153**
    (P49791), **Nup214** (D4ACK1), **Nup58** (P70581) — all
    nucleoporins from PMID:7878057 (Radu et al. 1995) / PMID:8707840.
    Annotation reflects FG-repeat binding to importins (transit
    interaction), not NLS-binding for transport. Likely MODIFY to
    GO:0017056 *structural constituent of nuclear pore* or removal.

### Tier 4 — disease-relevant / outlier annotations

12. **BRAP** (human, UniProt **Q7Z569**) — IDA PMID:9497340. BRCA1-
    associated protein; cytoplasmic retention factor for NLS-bearing
    cargos. Triage needed (cargo-retention, not carrier).
13. **IMPA1** (UniProt **Q96321**) and **IMPA2** (UniProt **F4JL11**)
    — *A. thaliana* importin-α homologs; both IMP PMID:37676567.
    Pair the two together; useful plant-side coverage.

## Proposed approach

1. **No urgent action.** The ontology ticket (go-ontology#31419) is
   CLOSED — the conceptual decision is settled — but the per-annotation
   remapping in go-annotation#6435 is still in progress. The PomBase
   entry (cut15) is the only one already DONE. Reviews can proceed
   immediately using the live GO:0140142 term as the proposed
   replacement; the formal obsoletion of GO:0008139 will follow the
   per-annotation triage.
2. **Begin with KPNA2 + KPNA4 (paired).** These are the cleanest cases
   for the GO:0140142 replacement and the IDA evidence is strong and
   recent. KPNA2's two independent IDAs from different groups make
   it an especially solid template.
3. **Add KPNB1 next.** The canonical importin-β; anchors the IBA
   fanout for the broader karyopherin family.
4. **Tackle a Tier-3 diagnostic case (NFKBIA or Su(fu)) early** to
   stress-test the per-annotation triage logic. These are the
   annotations where the carrier-vs-masking distinction matters most
   and where a straight `MODIFY` to GO:0140142 would be wrong.
5. **Yeast block (PSE1 / KAP104 / KAP123 / MTR10) as one project.**
   Shared literature and shared cargo classes (ribosomal protein
   import, mRNA-binding protein import) make a paired review efficient.
6. **Nucleoporin block (Nup58 / Nup98 / Nup153 / Nup214)** —
   probably one review per protein, with consistent MODIFY → GO:0017056
   recommendations and a shared rationale citing Radu et al. 1995
   (PMID:7878057) as the original annotation source.
7. **Cross-reference with**
   - [[MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION]] (same
     parent refactor wave)
   - [[PEROXISOME_TARGETING_SIGNAL_OBSOLETION]] (same parent)
   - Any future nuclear-pore / nucleocytoplasmic transport projects.

## Priority

**Low-medium.** The biology is canonical (nuclear-import machinery is
textbook), the upstream ontology decision is settled, and no existing
reviews in this repo are blocked. This is opportunistic — KPNA/KPNB
family is a major unreviewed area, and the triage cases (NFKBIA, Su(fu),
nucleoporins) make for instructive diagnostic reviews of the
carrier-vs-binding distinction. PINC's 5 TAS annotations (1990s-era
reviews) are also good candidates for evidence-code modernization.

## Status

- 2026-06-01 — Project file created. Tracking upstream issue
  geneontology/go-annotation#6435 (opened 2026-05-27, updated 2026-06-01).
  Upstream ontology ticket geneontology/go-ontology#31419 is CLOSED
  (decision settled; per-annotation triage in progress). Verified
  GO:0008139 still live in OLS (isObsolete: false) and GO:0140142
  (nucleocytoplasmic carrier activity) live and ready as replacement.
  Verified the annotation source tally via QuickGO REST: UniProt 10,
  SGD 7, RGD 6 manual + 5 ortholog-projection, PINC 5, FlyBase 2,
  ParkinsonsUK-UCL 2, MGI 1, PomBase 1 (DONE). Total bulk fanout is
  ~18k IEA/IBA entries that follow automatically. One InterPro2GO
  mapping (IPR024882, Nucleoporin p58/p45/NUP49) flagged for
  redirection. No UniRule/Keywords mappings. No gene reviews started
  yet in this repo; none of the ~25 affected gene products are present
  under `genes/`.
