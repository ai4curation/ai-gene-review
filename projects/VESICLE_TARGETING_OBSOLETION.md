# Vesicle Targeting (GO:0006903) & Descendants — Obsoletion & Replacement

## Overview

A GO obsoletion is retiring `GO:0006903 vesicle targeting` and its
descendant hierarchy. These BP terms conflate a *vesicle-mediated
transport* process with a *targeting/tethering* step in a way that is
no longer considered meaningful, so each is being collapsed onto a
broader, well-defined vesicle-transport parent. The biology is
unchanged; the fix is terminological (move annotations to the
designated replacement transport term).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6424](https://github.com/geneontology/go-annotation/issues/6424)
- Ontology ticket: [geneontology/go-ontology#31865](https://github.com/geneontology/go-ontology/issues/31865) — **closed 2026-05-16**
- Upstream review spreadsheet (curator-maintained): `https://docs.google.com/spreadsheets/d/1o5T_b5I9RNLdWUgcnaHxv4lqiY88_Al3CvpC4ul3Sv8`

## Obsoletion plan (per upstream issue)

| Obsoleted term | ID | Replacement |
|---|---|---|
| vesicle targeting | GO:0006903 | GO:0016192 vesicle-mediated transport |
| vesicle targeting to fusome | GO:0045479 | (no explicit replacement listed) |
| clathrin coating of Golgi vesicle, plasma membrane to endosome targeting | GO:0010785 | (no explicit replacement listed) |
| vesicle targeting, plasma membrane to endosome | GO:0048201 | (no explicit replacement listed) |
| vesicle targeting, to, from or within Golgi | GO:0048199 | GO:0048193 Golgi vesicle transport |
| vesicle targeting, rough ER to cis-Golgi | GO:0048207 | GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport |
| regulation of vesicle targeting, to, from or within Golgi | GO:0048209 | (no explicit replacement listed) |
| vesicle targeting, cis-Golgi to rough endoplasmic reticulum | GO:0048206 | GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum |
| vesicle targeting, inter-Golgi cisterna | GO:0048204 | GO:0048219 inter-Golgi cisterna vesicle-mediated transport |
| vesicle targeting, trans-Golgi to endosome | GO:0048203 | GO:0006895 Golgi to endosome transport |

All ten source terms are still **active** (not yet obsolete) in
QuickGO / GO API as of 2026-05-17 — the ontology ticket is merged but
the obsoletion has not yet propagated to the released ontology or to
annotations. All six listed replacement targets are valid, active BP
terms.

## Affected experimental / direct annotations

Pulled from QuickGO (`goUsage=exact`, experimental evidence
`ECO:0000269` descendants) on 2026-05-17. **22** experimental
annotations fall on just **4** of the 10 obsoleted terms; the other
six terms (GO:0045479, GO:0010785, GO:0048201, GO:0048209,
GO:0048206, GO:0048204) have **zero** experimental annotations and
will be handled entirely by IEA/IBA auto-migration.

### GO:0006903 vesicle targeting → GO:0016192 vesicle-mediated transport (12)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:O15498 | **YKT6** | Homo sapiens (9606) | IDA | PMID:9211930 |
| UniProtKB:Q7Z460 | **CLASP1** | Homo sapiens (9606) | IMP | PMID:24859005 |
| UniProtKB:O75122 | **CLASP2** | Homo sapiens (9606) | IMP | PMID:24859005 |
| UniProtKB:Q61161 | Map4k2 | Mus musculus (10090) | IDA | PMID:8643544 |
| UniProtKB:Q8K3E5 | Ahi1 | Mus musculus (10090) | IMP (acts_upstream_of_or_within) | PMID:20592197 |
| UniProtKB:P21707 | Syt1 | Rattus norvegicus (10116) | IDA | PMID:14715137 |
| UniProtKB:P61023 | Chp1 | Rattus norvegicus (10116) | IDA | PMID:8626580 |
| UniProtKB:Q258K2 | MYH9 | Canis lupus familiaris (9615) | IMP | PMID:18504258 |
| UniProtKB:P53141 | MLC1 | S. cerevisiae S288C (559292) | IMP | PMID:12456647 |
| ComplexPortal:CPX-3188 | polarisome | S. cerevisiae S288C (559292) | IMP | PMID:16166638 |
| UniProtKB:P0CY31 | SEC4 | Candida albicans SC5314 (237561) | IGI | PMID:9639314 |
| UniProtKB:Q9C744 | DELTA-ADR | Arabidopsis thaliana (3702) | IEP (acts_upstream_of_or_within) | PMID:28559361 |

### GO:0048203 vesicle targeting, trans-Golgi to endosome → GO:0006895 Golgi to endosome transport (7)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:Q5MNZ9 | **WIPI1** | Homo sapiens (9606) | IDA | PMID:15020712 |
| UniProtKB:Q63HQ0 | **AP1AR** | Homo sapiens (9606) | IDA | PMID:19706427 |
| UniProtKB:P35181 | APS1 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| UniProtKB:P36000 | APL2 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| UniProtKB:P38700 | APM2 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| UniProtKB:Q12028 | APL4 | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |
| ComplexPortal:CPX-533 | AP-1 complex | S. cerevisiae S288C (559292) | IMP | PMID:17003107 |

### GO:0048199 vesicle targeting, to, from or within Golgi → GO:0048193 Golgi vesicle transport (2)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:Q63584 | Tmed10 | Rattus norvegicus (10116) | IEP | PMID:17101722 |
| UniProtKB:Q9D1D4 | Tmed10 | Mus musculus (10090) | IEP | PMID:17101722 |

### GO:0048207 vesicle targeting, rough ER to cis-Golgi → GO:0006888 ER to Golgi vesicle-mediated transport (1)

| Group/ID | Gene | Species | Evidence | Reference |
|---|---|---|---|---|
| UniProtKB:Q9NZD2 | GLTP | Homo sapiens (9606) | IMP | DOI:10.1101/2025.06.17.657375 (preprint) |

A large pool of **IEA** annotations (~2,470 across these terms in
QuickGO) and any **IBA** propagations will be remapped automatically
once the obsoletion lands and the next pipeline runs. These do not
need per-annotation work here.

### Mapping cleanup (per upstream issue)

- **InterPro2GO:** `InterPro:IPR031483` (AP-1 complex-associated
  regulatory protein) → GO:0048203 — needs remapping to the
  replacement GO:0006895 by the InterPro2GO maintainers. This is an
  InterPro mapping concern, not a per-gene review item.
- No ARBA / UniRule mappings to the obsoleted terms were listed
  (UniRule appears in the upstream template header only).

## Impact on this repo

**No genes annotated to any of the obsoleted terms are currently
reviewed in this repo.** Checked all 9606/yeast symbols above
(`YKT6`, `CLASP1`, `CLASP2`, `WIPI1`, `AP1AR`, `GLTP`, `MLC1`,
`SYT1`, `CHP1`, `MAP4K2`, `AHI1`, `TMED10`, `MYH9`, `SEC4`, AP-1
subunits) against `genes/**/*-ai-review.yaml` — no matches.

So **no existing reviews need refresh** for the obsoletion itself.
This differs from the synaptic-vesicle-docking tracker
(go-annotation#6415), where `mouse Camk2a` had to be queued for a
refresh. Here the project is purely a forward-looking opportunity
to add high-value, currently-unreviewed human trafficking genes.

## Scope

- **Organisms**: human (12 of 22 EXP rows, 6 distinct human genes)
  and *S. cerevisiae* (8 rows, all the AP-1 / polarisome / MLC1
  complex annotations) carry essentially all the experimental
  signal. Rat/mouse/dog/Candida/Arabidopsis rows are orthologs that
  will largely follow automatically once the model-organism groups
  remap.
- **GO branches**: BP only — a transport-vs-targeting collapse onto
  broader vesicle-transport parents. No MF or CC changes.
- **Type of fix**: terminological. Reviews should ask whether the
  designated replacement is the *most informative* available term
  for the gene's core role, or whether a more specific extant BP
  (or an MF) better captures the function — e.g. YKT6 is a SNARE
  whose core MF (SNARE binding / SNAP receptor activity) is more
  informative than any generic transport BP.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` and confirm the
UniProt accession before starting. None are currently in the repo.

### Tier 1 — human, well-characterized, strong direct evidence

1. **YKT6 / O15498** (Homo sapiens) — longin-domain R-SNARE central
   to ER–Golgi and autophagosome–lysosome fusion. IDA on GO:0006903
   (PMID:9211930). Best single candidate: heavily studied, core MF
   anchor (SNARE / SNAP receptor activity) is far more informative
   than the generic GO:0016192 replacement, so this is a good test
   of MODIFY-vs-transfer judgement.
2. **CLASP1 / Q7Z460** and **CLASP2 / O75122** (Homo sapiens) —
   microtubule plus-end tracking proteins; both IMP on GO:0006903
   from the same study (PMID:24859005) implicating them in
   Golgi-derived vesicle transport. Reviewable as a pair.
3. **WIPI1 / Q5MNZ9** (Homo sapiens) — PI3P-binding autophagy
   effector; IDA on GO:0048203 (PMID:15020712, trans-Golgi to
   endosome). Review should weigh the GO:0006895 replacement against
   WIPI1's better-characterized autophagy/PI3P-binding roles.

### Tier 2 — human, adaptor / less direct

4. **AP1AR / Q63HQ0** (Homo sapiens) — AP-1 complex-associated
   regulatory protein (gadkin); IDA on GO:0048203 (PMID:19706427).
   Note this gene is also the subject of the InterPro2GO mapping
   cleanup (IPR031483 → GO:0048203).

### Tier 3 — opportunistic / lower value

5. **GLTP / Q9NZD2** (Homo sapiens) — glycolipid transfer protein;
   IMP on GO:0048207 but the only reference is an unpublished
   preprint (DOI:10.1101/2025.06.17.657375). Lower priority until a
   peer-reviewed reference exists.
6. *S. cerevisiae* AP-1 clathrin-adaptor subunits (**APL2/APL4/
   APM2/APS1**, PMID:17003107) — a coherent yeast complex set, but
   all IMP from a single study; consider only if extending yeast
   coverage. The Reactome/SGD groups will likely remap these
   directly.

## Proposed approach

1. **Hold as a tracking project — do not action yet.** The ontology
   ticket (#31865) is merged/closed but all ten source terms are
   still active in the released ontology and QuickGO as of
   2026-05-17. Wait for the obsoletion to propagate before pulling
   GOA, so `just fetch-gene` reflects the remapped terms.
2. **When the obsoletion lands, start with human YKT6.** Run
   `just fetch-gene human YKT6`, confirm the GOA pull shows
   GO:0006903 as obsolete / remapped to GO:0016192, then review per
   CLAUDE.md. Expect the right call to be MODIFY toward a more
   informative SNARE MF rather than a literal transfer to the
   generic transport BP.
3. **Follow with CLASP1/CLASP2 (as a pair), then WIPI1, then
   AP1AR.** Each review evaluates whether the designated
   replacement BP is the most informative term or whether a
   narrower extant BP / cognate MF is warranted.
4. **Defer Tier 3** (GLTP preprint-only; yeast AP-1 subunits) unless
   they surface via other workstreams.
5. **Do not create reviews for the ortholog rows** (rat/mouse/dog/
   Candida/Arabidopsis) or the IEA/IBA pool — these auto-migrate.

## Priority

**Medium.** 22 experimental annotations across 6 organisms — larger
than most obsoletion trackers in this repo — and several affected
human genes (YKT6, CLASP1/2, WIPI1) are biologically important
trafficking proteins with **no review yet in this repo**. The
obsoletion is a good trigger to add them, but the work should wait
until the obsoletion propagates to released annotations.

## Status

- 2026-05-17 — Project file created. Upstream annotation issue
  go-annotation#6424 open (last updated 2026-05-15); ontology ticket
  go-ontology#31865 closed 2026-05-16. All ten source terms still
  active in QuickGO/GO API; all six replacement targets valid. No
  affected gene is reviewed in this repo, so nothing needs refresh —
  held as a forward-looking tracking project. No gene reviews
  started.
