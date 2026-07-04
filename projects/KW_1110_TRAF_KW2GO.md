---
title: "KW-1110 (Inhibition of host TRAFs by virus) — KW2GO remapping"
maturity: SCOPING
tags: [KW2GO, OBSOLETION]
---

# KW-1110 (Inhibition of host TRAFs by virus) — KW2GO remapping

## Overview

Tracks a UniProt keyword-to-GO (KW2GO) mapping change proposed upstream: the
mapping from **UniProt keyword KW-1110 "Inhibition of host TRAFs by virus"** to
its current GO term is being moved to a more informative target that fits the
keyword's biology.

- **Keyword:** [KW-1110 "Inhibition of host TRAFs by virus"](https://www.uniprot.org/keywords/KW-1110)
- **Parent keyword:** [KW-1113 "Inhibition of host RLR pathway by virus"](https://www.uniprot.org/keywords/KW-1113)

### Current mapping (to be removed)

| GO ID | Label |
|---|---|
| GO:0039527 | symbiont-mediated suppression of host TRAF-mediated signal transduction |

- OLS lookup confirms this label. GO:0039527 is itself queued for obsoletion via
  [geneontology/go-ontology#29238](https://github.com/geneontology/go-ontology/issues/29238)
  because "TRAF-mediated signal transduction" is not a real pathway on the
  ontology's process branch (TRAFs act in many downstream pathways: TLR,
  TNF/TNFR, cGAS-STING, RLR, etc.).

### Proposed replacement mapping (to be added)

| GO ID | Label |
|---|---|
| GO:0140476 | symbiont-mediated suppression of host cytoplasmic pattern recognition receptor signaling pathway via inhibition of TRAF activity |

- **The GO:0140476 term ID does not yet resolve in OLS** (verified 2026-07-04).
  Per the annotation tracker discussion, this term still needs to be created in
  the ontology before the KW-1110 mapping can be repointed at it. The
  annotation tracker ticket is waiting on confirmation before deleting the
  existing mapping and adding the new one (the deletion is reversible if the
  new term is delayed).

### Nature of the change

Lateral / more-specific move within the same "symbiont-mediated suppression of
host signaling" branch. The proposed target explicitly ties TRAF-inhibition to
the **cytoplasmic pattern recognition receptor (PRR) signaling pathway** family
(RIG-I / MDA5 / LGP2 → MAVS → TBK1 / IRF3 / NF-κB), which matches the parent
keyword KW-1113 "Inhibition of host RLR pathway by virus". Reviewers on the
upstream thread note that TRAF is used by TLRs, TNFR, and cGAS-STING as well,
so this new target is a better fit for the specifically viral / RLR context
that KW-1110 sits under, but it does *not* cover TRAF interference by bacteria
or by viral proteins that act via TLR or TNFR routes — those need their own
child terms if the ontology decides to model them (see the upstream comments
by @genegodbold and @pgaudet for candidate templates).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6470](https://github.com/geneontology/go-annotation/issues/6470) (open)
- Ontology / obsoletion ticket: [geneontology/go-ontology#29238](https://github.com/geneontology/go-ontology/issues/29238) (closed)
- Prior TRAF-branch discussion (signal-transduction cleanup): geneontology/go-ontology#26498 (referenced by #29238)

## Impact on this repo

**No gene reviews currently touch either identifier.**

Searches performed on 2026-07-04:

- `grep -rl "0039527" genes` — no gene review files match (only a false-positive
  substring hit inside an Ensembl ID in a cached UniProt record).
- `grep -rl "0140476" genes` — no matches (as expected: term not yet created).
- `grep -rl "KW-1110" genes` — no matches.

So this repo has no reviews that will need to be rewritten when the mapping
lands. The purpose of this project page is therefore purely to **remember to
re-check once the ontology change and mapping change ship**, not to queue
existing rework.

## Follow-up

1. Watch [go-ontology#29238](https://github.com/geneontology/go-ontology/issues/29238)
   and [go-annotation#6470](https://github.com/geneontology/go-annotation/issues/6470)
   for term creation and mapping deployment.
2. Once GO:0140476 (or whatever ID the new term receives) is created and the
   KW-1110 mapping is repointed, re-run the two greps above to catch any newly
   added reviews for viral effector genes carrying KW-1110 (e.g. EBV BPLF1,
   FMDV Lb(pro), HSV-1 ICP0, SARS-CoV-2 M, and the bacterial TRAF-interfering
   effectors listed in the go-ontology thread).
3. If any of those viral / bacterial effector genes enter this repo later,
   their `existing_annotations` review should MODIFY away from GO:0039527 and
   toward the new PRR-signaling target when the annotation actually carries
   evidence for a cytoplasmic-PRR context; TLR or TNFR contexts should go to
   the appropriate sibling term instead (see @pgaudet's per-effector
   assignments in [go-ontology#29238](https://github.com/geneontology/go-ontology/issues/29238)).

## Status

- **Created:** 2026-07-04
- **Blocker:** GO:0140476 not yet minted; KW2GO deployment blocked on that.
- **Action needed here:** none until upstream ships. This page is a watch-list
  entry so the mapping change is not silently missed when it lands.
