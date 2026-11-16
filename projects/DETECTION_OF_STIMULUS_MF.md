---
title: "Detection of Stimulus: Sensor Activity or Process?"
maturity: SCOPING
tags: [OBSOLETION, BIOLOGY_DOMAIN]
species: [human, mouse, worm, ARATH, DROME]
collections: [GO_TRACKER_BACKLOG]
---

# Detection of Stimulus: Sensor Activity or Process?

**Bottom line:** Four GO tracker issues opened in 2019-2022 propose turning
the "detection of X" biological processes into molecular functions (sensor,
receptor or binding activities), or obsoleting them. None of the heavily used
detection terms has changed; only unused leaves were cleaned up. The
question is still disputed: a 2026 thread has PomBase saying the branch is
MF-like, while Cell Ontology and FlyBase anatomy editors say detection is a
multi-gene process. Reviews here hold 306 rows on 158 genes under GO:0051606
*detection of stimulus*. They already sort the genes the way the dispute
needs: the transducer or receptor is ACCEPTed, and upstream or downstream
factors are marked over-annotated. A gene-by-gene table of that split is
evidence neither side has. Scoped, not started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment |
|---|---|---|---|
| [go-ontology#18097](https://github.com/geneontology/go-ontology/issues/18097) | 2019-11-01 | "Detection" is a molecular function: obsolete detection-of-substance BPs | 2019-11-04 |
| [go-ontology#18098](https://github.com/geneontology/go-ontology/issues/18098) | 2019-11-01 | detection of molecule of bacterial/fungal origin | 2019-11-04 |
| [go-ontology#20133](https://github.com/geneontology/go-ontology/issues/20133) | 2020-10-15 | merge GO:0043575 detection of osmotic stimulus | 2020-10-19 (later called a duplicate of #18097) |
| [go-ontology#23137](https://github.com/geneontology/go-ontology/issues/23137) | 2022-04-04 | table of 34 single-step detection BPs to convert | no comments |

The live discussion moved to
[go-ontology#31734](https://github.com/geneontology/go-ontology/issues/31734)
(2026), which is not part of the pre-2023 backlog but records the current
positions. Nothing has been posted to any of these issues.

## The question

Is "detection of X" one gene product's activity (a receptor or sensor
binding X and changing state), or a process that several gene products carry
out together? Positions as of 2026-11-16:

- **Convert to MF.** #23137 (2022-04-04): "These terms should probably all be
  MFs; some could be reformulated as a BP (such as signaling)". GO has grown
  the sensor MF branch meanwhile: GO:0140299 is now *molecular sensor
  activity*, with children for oxygen, glucose (created 2023), glutamine,
  amino acid, calcium ion and osmosensor activity.
- **Keep as process.** In #31734: "detection by a cell typically involves
  multiple gene products, not a single protein with a molecular function."
  Cell Ontology uses some detection terms to classify cell types.
- **Obsolete outright.** In #18098 an earlier ontology developer said they
  would rather obsolete the detection terms, migrating annotations up to
  "response to", than convert them to MF.

In go-edit.obo (checkout 2026-11-12), 120 live BP terms have labels starting
"detection of" and 53 more are obsolete. All five terms on the #18097
checklist (GO:0003032 oxygen, GO:0009594 nutrient, GO:0031319 cAMP,
GO:0043695 pheromone, GO:0051594 glucose) are live, as is GO:0043575.
[PR go-ontology#20144](https://github.com/geneontology/go-ontology/pull/20144),
marked do-not-merge, has been open since 2020.

## What this repo already has

All terms under GO:0051606 with at least five rows, computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py)
(`--descendants GO:0051606 --min-rows 5`). Of the 154 live descendants, 62
have at least one row.

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0051606 detection of stimulus | 8 | 5 | 0 | 0 | 0 | 7 | 1 | 0 |  | 0 |
| GO:0007602 phototransduction | 21 | 15 | 7 | 5 | 3 | 2 | 1 | 3 |  | 4 |
| GO:0007603 phototransduction, visible light | 9 | 7 | 2 | 4 | 1 | 2 | 0 | 0 |  | 2 |
| GO:0030265 phospholipase C-activating opsin-mediated signaling pathway | 6 | 4 | 5 | 0 | 0 | 0 | 0 | 0 | NEW 1 | 4 |
| GO:0009585 red, far-red light phototransduction | 8 | 8 | 2 | 2 | 3 | 0 | 1 | 0 |  | 2 |
| GO:0009584 detection of visible light | 5 | 5 | 3 | 0 | 0 | 0 | 1 | 1 |  | 1 |
| GO:0008020 G protein-coupled photoreceptor activity | 6 | 3 | 4 | 0 | 0 | 0 | 1 | 1 |  | 2 |
| GO:0050908 detection of light stimulus involved in visual perception | 14 | 10 | 3 | 2 | 4 | 0 | 0 | 5 |  | 1 |
| GO:0016048 detection of temperature stimulus | 8 | 4 | 7 | 0 | 0 | 1 | 0 | 0 |  | 3 |
| GO:0050982 detection of mechanical stimulus | 7 | 7 | 5 | 1 | 0 | 0 | 0 | 0 | NEW 1 | 4 |
| GO:0035995 detection of muscle stretch | 7 | 5 | 2 | 2 | 0 | 0 | 0 | 3 |  | 0 |
| GO:0050910 detection of mechanical stimulus involved in sensory perception of sound | 22 | 16 | 5 | 2 | 3 | 11 | 0 | 0 | NEW 1 | 5 |
| GO:0050966 detection of mechanical stimulus involved in sensory perception of pain | 8 | 6 | 0 | 5 | 2 | 0 | 1 | 0 |  | 0 |
| GO:0050974 detection of mechanical stimulus involved in sensory perception | 7 | 6 | 4 | 3 | 0 | 0 | 0 | 0 |  | 5 |
| GO:0001580 detection of chemical stimulus involved in sensory perception of bitter taste | 11 | 6 | 8 | 1 | 0 | 2 | 0 | 0 |  | 3 |
| GO:0033038 bitter taste receptor activity | 9 | 3 | 9 | 0 | 0 | 0 | 0 | 0 |  | 3 |
| GO:0005513 detection of calcium ion | 31 | 14 | 28 | 3 | 0 | 0 | 0 | 0 |  | 10 |
| GO:0010247 detection of phosphate ion | 5 | 5 | 2 | 0 | 1 | 2 | 0 | 0 |  | 2 |
| GO:0032497 detection of lipopolysaccharide | 6 | 3 | 5 | 1 | 0 | 0 | 0 | 0 |  | 2 |
| GO:0050911 detection of chemical stimulus involved in sensory perception of smell | 6 | 3 | 5 | 0 | 1 | 0 | 0 | 0 |  | 2 |
| GO:0038022 G protein-coupled olfactory receptor activity | 5 | 1 | 5 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0009372 quorum sensing | 7 | 6 | 3 | 1 | 0 | 2 | 1 | 0 |  | 3 |
| GO:0050906 detection of stimulus involved in sensory perception | 5 | 5 | 0 | 2 | 1 | 1 | 1 | 0 |  | 0 |

Total over all 154 descendants: 306 rows on 158 reviewed genes (ACCEPT 143,
KEEP_AS_NON_CORE 50, MARK_AS_OVER_ANNOTATED 42, MODIFY 28, REMOVE 16, NEW 14,
UNDECIDED 13). Some MF receptor terms (GO:0008020, GO:0033038, GO:0038022)
appear because GO places them part_of a detection process.

The sensor-MF side, for comparison (`GO:0140299 --descendants GO:0140299`):
164 rows on 98 genes, ACCEPT 117. The largest are GO:0000155 phosphorelay
sensor kinase activity (79 rows), GO:0061891 calcium ion sensor activity
(18) and GO:0019826 oxygen sensor activity (13).

What stands out:

- **Reviews already separate the detector from everything else.** On
  GO:0050910 (sound), human/TMC1, ADGRV1 and DANRE tmc2a/tmc2b are ACCEPT,
  while 11 rows are marked over-annotated on CHRNA9/CHRNA10 (efferent
  synapse), MYC, Sox2 (development), MKKS, PDZD7 and WHRN (structural). On
  GO:0005513 (calcium ion) the ACCEPT rows are sensors with their own
  calcium-binding MF: CASR, STIM1, calmodulins, CASQ2, ARATH CBL4/CBL10.
- **The microbial-molecule rows are all pattern-recognition receptors.**
  GO:0032497 (LPS) is on TLR4, LY96 and TREM2. GO:0032490 is on TLR9,
  DROME/Dscam1 and worm/daf-7 (marked over-annotated). GO:0032491 is on ARATH
  CERK1, with NEW rows proposed for LYK5 and ORYSJ/CEBIP. This is the test set
  #18098 implies: if each row is "receptor activity, part_of a recognition
  signaling pathway", the conversion PomBase proposes is lossless.
- **The root term is used only where nothing better was found.** All eight
  GO:0051606 rows are over-annotated or removed (four CADM1 entries,
  BACSU/spo0A).

## What gene review can and cannot settle

- **Can settle, per gene:** whether the product binds or transduces the
  stimulus itself (sensor, receptor or channel MF), acts in the downstream
  pathway, or sits upstream (development, structure). That classification
  of the experimental rows is what #18097 and #23137 ask for, and what the
  #31734 dispute estimates by eye.
- **Can test:** the "multiple gene products" objection. Where detection
  genuinely needs a complex (TLR4 with LY96, the hair-cell
  mechanotransduction complex), reviews can record `contributes_to` the sensor MF.
- **Cannot settle:** whether GO keeps the detection branch for Cell Ontology's
  use. That is a cross-ontology decision.

## Plan

- [ ] Export the 306 rows to a per-gene table with three columns: detector
      (MF available), pathway member, upstream or structural. Seed it from the
      existing review actions and check the ACCEPT rows against the cited
      evidence.
- [ ] For each detector, record the sensor or receptor MF the review already
      carries, or flag the gap (as for the #18097 checklist terms with no
      MF: nutrient, cAMP, pheromone).
- [ ] Re-check the 11 over-annotated GO:0050910 rows and the CADM1 root rows.
      Are they consistently argued?
- [ ] New reviews for checklist terms with no reviewed carrier: detection of
      nutrient, cAMP, pheromone and glucose. Pick one well-studied gene each
      from the GOA experimental rows.
- [ ] Write a summary of the classification for the issue owners. Posting it
      is the project lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). All four
  threads and #31734 read. Term states checked against go-edit.obo (checkout
  2026-11-12).
- #20133 is effectively a duplicate of #18097. Its single GO:0043575
  annotation is not on any reviewed gene.
