# Neuroblast Proliferation / Division — Vertebrate vs Protostome Disambiguation

## Overview

The word *neuroblast* denotes two biologically distinct cell types:

- **Vertebrates** (mouse, rat, human): a neuroblast is a **postmitotic** cell
  that does **not** divide further. It migrates and then differentiates into a
  neuron. (Cf. Cell Ontology "neuroblast (sensu Vertebrata)".)
- **Protostomes / flies**: a neuroblast is a **mitotic, self-renewing neural
  stem cell** that divides asymmetrically to produce ganglion mother cells.
  (Cf. "neuroblast (sensu Nematoda and Protostomia)".)

GO terms in the "neuroblast proliferation / neuroblast division" branch were
written around the *protostome* (dividing stem-cell) sense — e.g. GO:0007405
*neuroblast proliferation* is defined as "The expansion of a neuroblast
population by cell division. A neuroblast is any cell that will divide and give
rise to a neuron." That definition is incompatible with the vertebrate
postmitotic neuroblast, yet the QuickGO download attached to the upstream issue
shows the branch is annotated **almost entirely with vertebrate genes** (mouse,
rat, human). In vertebrates the thing that actually proliferates is the
**neural precursor / progenitor cell** (GO:0061351 *neural precursor cell
proliferation*, verified in OLS 2026-05-18), not the neuroblast.

This is therefore not a simple obsoletion. The upstream plan is to **separate
the two senses**: keep the division branch for protostomes, migrate the
vertebrate annotations to vertebrate-appropriate proliferation/neurogenesis
terms, then rename the terms and re-map the Cell Ontology so the two senses can
never be confused again. This repo's contribution is the **annotation-level
review**: for each affected vertebrate gene, decide the correct replacement
term from the cited literature (mostly `MODIFY` → GO:0061351 or a more specific
neural-precursor-proliferation / neurogenesis child).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6393](https://github.com/geneontology/go-annotation/issues/6393)
  — "Review mouse annotations under 'neuroblast proliferation'" (curator
  @sjm41; last upstream activity 2026-05-07).
- **No GO-ontology ticket yet.** The upstream curator is still in the
  scoping/discussion phase ("before I make the tickets for the ontology
  changes and annotation migrations, I wanted to check if you think this is
  the correct path"). The ontology renaming + CL re-mapping is **out of scope
  for this repo**; our annotation MODIFY recommendations are an independent
  input that does not need to wait for the ontology decision.

## Affected terms (from the upstream QuickGO export, 42 rows)

| GO ID | Label | Rows | Sense as written |
|---|---|---|---|
| GO:0007405 | neuroblast proliferation | 26 | protostome (division-centric) |
| GO:0055059 | asymmetric neuroblast division | 4 | protostome |
| GO:0021849 | neuroblast division in subventricular zone | 4 | mixed / vertebrate SVZ |
| GO:0021847 | ventricular zone neuroblast division | 4 | mixed / vertebrate VZ |
| GO:0045200 | establishment of neuroblast polarity | 2 | mixed |
| GO:0021873 | forebrain neuroblast division | 2 | vertebrate forebrain |

Term IDs/labels are taken verbatim from the upstream QuickGO TSV; GO:0007405
and the proposed replacement GO:0061351 were independently re-verified in OLS
on 2026-05-18.

## Scope analysis

- **Organisms (annotation rows)**: Mouse (NCBITaxon:10090) 35 rows, Human
  (9606) 4 rows, Rat (10116) 3 rows = 42 rows total — i.e. **100% vertebrate**,
  confirming the conceptual mismatch. No fly/protostome annotations appear in
  this export.
- **Distinct genes**: ~33 (some mouse genes carry multiple annotations across
  the 6 affected terms; ARHGEF2 additionally appears in both mouse and human).
  The gene-count is approximate pending the per-gene review pass; the
  authoritative figure is the 42-row annotation count.
- **Evidence**: All experimental (IMP / IGI / IDA / IEP). Many are
  `acts_upstream_of_or_within` MGI annotations (regulatory/upstream genes that
  modulate progenitor proliferation, not neuroblast division per se).
- **Common problem**: a protostome stem-cell term applied to vertebrate genes
  whose cited papers describe **neural precursor/progenitor proliferation,
  cortical neurogenesis, or progenitor polarity/spindle orientation** — not
  the division of a (postmitotic) vertebrate neuroblast.
- **Expected action distribution**: predominantly `MODIFY`
  (proposed_replacement_terms → GO:0061351 *neural precursor cell
  proliferation* or a VZ/SVZ/forebrain-specific neural-precursor child, chosen
  per-gene from the cited PMID), with occasional `REMOVE` where the paper does
  not support any proliferation/neurogenesis claim, and `KEEP_AS_NON_CORE`
  where proliferation is a genuine but peripheral effect of a pleiotropic gene.

## Candidate genes for initial review (priority order)

Prioritised by (a) already present in this repo, (b) human ortholog directly
annotated, (c) high-profile, well-characterised vertebrate neurogenesis genes
where the correct term is unambiguous.

| # | Gene | Acc | Taxon | Term annotated | Ev | PMID | In repo? | Likely action |
|---|---|---|---|---|---|---|---|---|
| 1 | ASCL1 (Mash1) | Q02067 | mouse | GO:0007405 | IGI | PMID:15976074 | human ortholog only (genes/human/ASCL1); human ASCL1 P50553 has no GO:0007405 annotation | MODIFY → GO:0061351 on the mouse Mash1 annotation (Mash1 drives progenitor proliferation/neurogenesis) |
| 2 | FGFR2 | P21802 | human | GO:0021847 | ISS | GO_REF:0000024 (with/from UniProtKB:P21803 mouse) | **genes/human/FGFR2** (already KEEP_AS_NON_CORE) | revisit: existing review action is KEEP_AS_NON_CORE; under this project consider MODIFY → vertebrate VZ neural-precursor proliferation |
| 3 | SOX5 | — | human | GO:0055059 | IGI | PMID:23946438 | no (genes/human) | review — likely MODIFY/REMOVE (asymmetric *neuroblast* division is protostome) |
| 4 | ARHGEF2 | Q60875 | human+mouse | GO:0055059 | IDA/IMP | PMID:28453519 | no | MODIFY → progenitor mitotic spindle / asymmetric progenitor division |
| 5 | DOCK7 | — | human | GO:0045200 | IMP | PMID:16982419 | no | review progenitor-polarity context |
| 6 | TEAD3 | — | human | GO:0055059 | IGI | PMID:23946438 | no | review (co-cited with SOX5) |
| 7 | Pafah1b1 (LIS1) | P63005 | mouse | GO:0007405 | IMP | PMID:12629176 | no | MODIFY → neural precursor proliferation (LIS1 = classic neurogenesis/migration gene) |
| 8 | Aspm | Q8CJ27 | mouse | GO:0021873 | IMP | PMID:16798874 | no | MODIFY → forebrain neural-precursor proliferation (ASPM = microcephaly/progenitor gene) |
| 9 | Shh | Q62226 | mouse | GO:0007405 | IDA | PMID:15337776 | no | MODIFY → neural precursor proliferation |
| 10 | Nde1 | Q9CZA6 | mouse | GO:0007405 | IMP | PMID:15473967 | no | MODIFY → neural precursor proliferation (NDE1 = microcephaly/progenitor) |

Other affected mouse genes (defer to a second batch): Plxnb2, Numb, Numbl,
Neurod4, Kcna1, Fgfr1, Lef1, Dct, Id4, Nfix, Eml1, Zzef1, Dagla, Daglb, Hhip,
Ckap2l, Akna, Frs2, Acsl6, Racgap1, Fzd9; rat Gh1, Ifrd1, Rab10.

## Proposed approach

1. **Use the two repo genes (ASCL1, FGFR2) to demonstrate the pattern**, but
   note that neither carries the offending annotation on the human gene as
   listed in the human GOA:
   - `genes/human/ASCL1` has **no** GO:0007405 annotation; the upstream
     annotation is on **mouse Mash1 (Q02067)** via IGI in PMID:15976074. The
     `existing_annotations` block on the human ASCL1 review cannot be used
     here; the appropriate channel is a new mouse-ASCL1 review under
     `genes/mouse/ASCL1` (or to record the recommendation in the project doc
     and propagate upstream via geneontology/go-annotation#6393).
   - `genes/human/FGFR2` already reviews GO:0021847 with
     `action: KEEP_AS_NON_CORE` (ISS via GO_REF:0000024, with/from mouse
     P21803). Under this project the action should be revisited — the
     candidate replacement is GO:0061351 or a VZ-specific neural-precursor
     proliferation child confirmed via OLS — but this is an `action` update
     on an existing review, not a new `existing_annotations` entry.
2. **Then the four human-annotated genes** (SOX5, ARHGEF2, DOCK7, TEAD3) —
   these live directly in `genes/human` and are the upstream-impacted
   *human* set. `just fetch-gene human <SYMBOL>` then `/review`.
3. **Then the high-profile mouse progenitor genes** (LIS1/Pafah1b1, Aspm,
   Nde1, Shh) as mouse reviews (`genes/mouse/` exists). These are textbook
   neural-precursor-proliferation genes; the MODIFY target is unambiguous and
   they make a clean illustrative cluster.
4. **Per-gene rule**: read the cited PMID. If it describes proliferation of a
   *progenitor/stem* population (VZ/SVZ radial glia, intermediate
   progenitors) → MODIFY to GO:0061351 or the appropriate
   neural-precursor-proliferation child. If it describes spindle
   orientation / asymmetric progenitor division → MODIFY to the relevant
   progenitor-division term, **not** "asymmetric *neuroblast* division". If
   the paper does not support any proliferation/neurogenesis claim →
   REMOVE. Never retain GO:0007405/GO:0055059 etc. on a vertebrate gene as
   *core*.
5. **Do not block on upstream ontology timing.** The MODIFY/REMOVE action
   codes are independent of whether/when GO renames the terms or re-maps the
   Cell Ontology. Record the upstream rationale in each review's
   `existing_annotations[].review.summary`.
6. Cross-link the emerging pattern into
   `projects/OVER_ANNOTATION_PATTERNS.md` (protostome stem-cell term applied
   wholesale to vertebrate genes) once 3–4 reviews are done.

## Priority

**Medium.** 42 annotations / ~33 distinct genes — larger than the typical
obsoletion-tracking set, with a crisp, repeating conceptual error (a
protostome neural-stem-cell term applied 100% to vertebrate genes). Two genes
(ASCL1, FGFR2) are already in the repo, and the cluster includes textbook
neurogenesis genes (LIS1, ASPM, NDE1, ASCL1, SHH) where the correct vertebrate
term is unambiguous, making this a strong, well-evidenced illustrative
batch. Upstream is still in discussion, so there is no deadline pressure — but
the annotation review is valuable input to that discussion now.

## Status

- **2026-05-18** — Project file created. Tracking upstream
  geneontology/go-annotation#6393 (last upstream activity 2026-05-07). The
  attached QuickGO export (42 rows, 6 GO terms, 100% vertebrate) was fetched
  and parsed for scope. GO:0007405 and the proposed replacement GO:0061351
  verified in OLS. No reviews started yet; ASCL1 and FGFR2 are the only
  affected genes currently in the repo (both `genes/human/`).
