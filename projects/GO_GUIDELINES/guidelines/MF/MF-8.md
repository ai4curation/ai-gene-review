---
id: MF-8
title: Distinguish adaptor, scaffold, sequestering, carrier and regulator by what the binding does
status: proposed
topic: MF
provenance: GOC_PLUS
aspects:
- F
evidence_codes:
- IPI
go_terms:
- term_id: GO:0140378
  label: protein complex scaffold activity
- term_id: GO:0160072
  label: ubiquitin ligase complex scaffold activity
- term_id: GO:0005198
  label: structural molecule activity
- term_id: GO:0060090
  label: molecular adaptor activity
- term_id: GO:0140693
  label: molecular condensate scaffold activity
- term_id: GO:0140566
  label: histone reader activity
- term_id: GO:0035615
  label: clathrin-cargo adaptor activity
- term_id: GO:1990756
  label: ubiquitin-like ligase-substrate adaptor activity
- term_id: GO:0140311
  label: protein sequestering activity
- term_id: GO:0140104
  label: molecular carrier activity
differences:
- prior_source: '[MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md)'
  prior_said: Names `GO:0032947` as "protein-containing complex scaffold activity", the out-of-branch
    scaffold term
  we_recommend: Use `GO:0140378` protein complex scaffold activity
  why: GO:0032947 does not resolve in the GO release used here; GO:0140378 is the live structural scaffold
    term
  issue: 6444
open_questions:
- '**Adaptor with one input.** The GO-CAM guideline permits a single `has_input` on an adaptor activity
  while warning that it may be the wrong term. Should that be a hard requirement of two inputs?'
sources:
- kind: drive
  title: MF guidelines for GO-CAM
  url: https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4
- kind: repo
  title: MOLECULAR_ADAPTOR_ACTIVITY
  path: projects/MOLECULAR_ADAPTOR_ACTIVITY.md
- kind: wiki
  title: Non-catalytic Molecular Functions
  url: https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions
- kind: issue
  title: go-annotation#3510
  url: https://github.com/geneontology/go-annotation/issues/3510
date: '2026-11-15'
---

# MF-8. Distinguish adaptor, scaffold, sequestering, carrier and regulator by what the binding does

## Decision

Choose among the non-catalytic activities by the test in the [Decision aid](README.md#decision-aid):
adaptor (brings two or more molecules together so they act in a coordinated way),
scaffold (structural organiser of a complex), sequestering (binds a molecule to keep it
from its partners or location), carrier (moves with its cargo to an acceptor or
location), regulator (modulates the target's activity directly). An adaptor annotation
needs evidence of at least two bridged partners.

## Context

The GO-CAM activity-unit guidelines define each activity by its inputs and
its causal effect
([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
The adaptor activity "has input the two (or more) molecules it brings together", and the
guideline warns that a single input suggests adaptor activity may not be the right term.
A single binary interaction (one IPI hit) evidences binding, not bridging
([MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md), decision rule 1).
In the ontology the adaptor and scaffold branches are separate: `GO:0140378` protein
complex scaffold activity (and its child `GO:0160072` ubiquitin ligase complex scaffold
activity) sit under `GO:0005198` structural molecule activity, not under `GO:0060090`
molecular adaptor activity, whereas `GO:0140693` molecular condensate scaffold activity
and `GO:0140566` histone reader activity are adaptor children (checked against the
local GO release, 2026-11-15).

## Application

Worked examples.

- LDLRAP1 bridges the LDL receptor's NPxY motif to clathrin and AP-2:
  `GO:0035615` clathrin-cargo adaptor activity (`genes/human/LDLRAP1`).
- In a cullin–RING ligase, CUL4A or DDB1 enables `GO:0160072` ubiquitin ligase complex
  scaffold activity with `has_input` the substrate adaptor and the ligase, and the
  substrate receptor enables `GO:1990756` ubiquitin-like ligase-substrate adaptor
  activity with `has_input` the substrate
  ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
- CAV1 binds TLR4 and holds it inactive: `GO:0140311` protein sequestering activity,
  `has_input` TLR4, part of negative regulation of the TLR4 pathway.
- CD14 delivers LPS to TLR4–MD-2: `GO:0140104` molecular carrier activity; the
  carrier "moves with the substrate it carries", which distinguishes it from a
  transporter ([wiki: Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)).

In standard annotation, the MF-to-MF relations (`directly positively regulates`,
`provides input for`) are not captured; record the MF, its `has_input` partners, the BP
and the CC ([Drive: MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)).
A general adaptor term may stand beside a specific child only for a distinct bridging
event the child does not cover; otherwise the parent is `TOO_GENERAL`
([MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md), decision rule 5).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Evidence codes | IPI |
| GO terms | `GO:0140378` protein complex scaffold activity; `GO:0160072` ubiquitin ligase complex scaffold activity; `GO:0005198` structural molecule activity; `GO:0060090` molecular adaptor activity; `GO:0140693` molecular condensate scaffold activity; `GO:0140566` histone reader activity; `GO:0035615` clathrin-cargo adaptor activity; `GO:1990756` ubiquitin-like ligase-substrate adaptor activity; `GO:0140311` protein sequestering activity; `GO:0140104` molecular carrier activity |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md) | Names `GO:0032947` as "protein-containing complex scaffold activity", the out-of-branch scaffold term | Use `GO:0140378` protein complex scaffold activity | GO:0032947 does not resolve in the GO release used here; GO:0140378 is the live structural scaffold term (#6444) |

## Open questions

1. **Adaptor with one input.** The GO-CAM guideline permits a single `has_input` on an adaptor activity while warning that it may be the wrong term. Should that be a hard requirement of two inputs?

## Sources

- drive: [MF guidelines for GO-CAM](https://drive.google.com/open?id=1DWvc_g5yH4S8-Tc2rPtaAyPOIkYzITagK1sXysj0CY4)
- repo: [MOLECULAR_ADAPTOR_ACTIVITY](../../../MOLECULAR_ADAPTOR_ACTIVITY.md)
- wiki: [Non-catalytic Molecular Functions](https://wiki.geneontology.org/index.php/Non-catalytic_Molecular_Functions)
- issue: [go-annotation#3510](https://github.com/geneontology/go-annotation/issues/3510)

<!-- END GENERATED -->
