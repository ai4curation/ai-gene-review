---
title: "Matrisome → GO: evaluation (low yield, parked)"
---

# Matrisome → GO: evaluation (low yield, parked)

**Status: PARKED.** We evaluated the [Matrisome project](https://sites.google.com/uic.edu/matrisome)
/ [MatrisomeDB](https://matrisomedb.org) (Naba/Hynes) as a source of GO annotations for gene review
and concluded it **adds little**. This page records that negative result and the reasoning, so we
don't re-investigate it from scratch. The apparatus is kept (small, reproducible) but is **not** run
as an active propagation pipeline.

## What the matrisome is

A curated ECM **membership lookup list**, not a classifier and not a GO annotation source. It assigns
each ECM / ECM-associated gene to one of six families under two categories:

| category | families |
|---|---|
| **Core matrisome** | Collagens, ECM Glycoproteins, Proteoglycans |
| **Matrisome-associated** | ECM-affiliated Proteins, ECM Regulators, Secreted Factors |

MatrisomeDB itself reprocesses public ECM proteomics; it does **not** deposit GO annotations. The ECM
`GO:0031012` HDA annotations in GOA are made independently by GO curators (GO_Central, BHF-UCL) citing
the underlying proteomics papers — the same papers MatrisomeDB reprocesses.

## Why it adds little (the finding)

1. **No molecular function.** Every matrisome family is a *localization/membership* label, not a
   function. "Secreted Factor" is, at most, `GO:0005576 extracellular region` — a cellular component,
   **not** a GO molecular function. The curatorially valuable content (MF/BP) the matrisome simply
   does not carry.
2. **It collapses to one generic CC term.** As an annotation generator the whole resource yields at
   most `GO:0031012 extracellular matrix` (a location), shared by all three core families.
3. **GOA already has it.** Of the 24 mappable core-matrisome genes in our corpus, **19 already carry
   GO:0031012**, 1 was subsumed by a more specific term, and only **4** lacked it (GAS6, IGFBP3,
   NTN3, mouse Gas6) — and those are exactly the borderline "is this really ECM-localized?" cases, not
   confident additions. Net yield ≈ 4 weak, location-only leads across 2,778 reviewed genes. See
   [`MISSING_ANNOTATIONS.md`](MISSING_ANNOTATIONS.md).

## The one genuine (modest) nugget

The **core vs matrisome-associated** split is a useful *soft prior on the core/non-core decision* for
ECM-localization annotations we are already reviewing — not a generator of new ones. Example:
SERPINH1/HSP47 carries `GO:0031012` HDA annotations; the matrisome classes it as
**associated / ECM Regulator**, which independently supports our `KEEP_AS_NON_CORE` call (peripheral
co-purification, not true ECM residence). This is a QC signal, not annotation content, and it is weak
(the matrisome still *includes* such borderline proteins).

## Side finding: GO:0062023 is obsolete

`GO:0062023` "collagen-containing extracellular matrix" was **obsoleted** and merged back into
`GO:0031012` (`replaced_by GO:0031012`; go-ontology#29475, *"not clearly defined and usage has been
inconsistent"*). The earlier GO effort to reannotate metazoan ECM annotations *to* GO:0062023 has
therefore been reversed — `GO:0031012` is the current term. (`test_matrisome2go_mapping.py` guards
against re-introducing GO:0062023.)

## What is kept here (reproducible, not active)

- `matrisome2go.sssom.yaml` — the family→GO analysis: only the 3 core families map (to `GO:0031012`,
  `located in`); the 3 associated families are deliberate `sssom:NoTermFound` gap rows. Validated by
  `just validate-matrisome-mappings`. `matrisome2go.terms.yaml` is the generated term-validatable form.
- `missing_annotation_report.py` — the gap-finder used to produce the yield numbers above
  (`just matrisome-missing`). Species-aware; subsumption-aware.
- `MISSING_ANNOTATIONS.md` — the recorded result snapshot.
- `data/` — the masterlist CSVs are **not committed** (≈36k lines); see [`data/README.md`](data/README.md)
  to regenerate them before re-running the report.
- `src/ai_gene_review/schema/matrisome_go_mapping.yaml` — sidecar schema for GO-term validation.

## If we ever revisit

The only worthwhile direction would be the QC prior above — emitting "matrisome says *associated* →
expect non-core" flags against existing `GO:0031012` annotations — not mining the matrisome for new
annotations.
