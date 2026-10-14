---
title: "KW-1110 (Inhibition of host TRAFs by virus) — KW2GO remapping"
maturity: COMPLETE
last_reviewed: "2026-10-04"
tags: [PIPELINE, OBSOLETION]
manifest:
  slides:
    - href: KW_1110_TRAF_KW2GO/slides/KW_1110_TRAF_KW2GO-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/HpYCKxoFy6C6gRzHn7FTcp
      title: Project brief
---

# KW-1110 (Inhibition of host TRAFs by virus) — KW2GO remapping

**Bottom line:** UniProt keyword KW-1110 "Inhibition of host TRAFs by virus"
was mapped to GO:0039527, a process term GO obsoleted because
"TRAF-mediated signal transduction" is not a single pathway: TRAFs act in RLR,
TLR, TNFR and cGAS-STING signaling. The mapping has been repointed to
GO:0140476, which ties TRAF inhibition to cytoplasmic pattern recognition
receptor signaling and matches the current KW2GO scope of the parent keyword
KW-1113. As of 2026-10-04, QuickGO resolves GO:0140476 and marks GO:0039527
obsolete (suggesting GO:0140476 or the TLR sibling GO:0140470), the current GO
`uniprotkb_kw2go` file maps KW-1110 to GO:0140476, and
geneontology/go-annotation#6470 is closed. This page was a watch-list entry,
not a review project, and no gene review in this repository carries
GO:0039527, GO:0140476 or KW-1110, so nothing needs rework.

We keep this record so that any viral or bacterial TRAF-interfering effector
reviewed later is moved to the right pathway-specific term rather than to the
obsolete parent.

## Overview

Records a completed UniProt keyword-to-GO (KW2GO) mapping change: **UniProt
keyword KW-1110 "Inhibition of host TRAFs by virus"** was moved from an
obsolete, nonspecific TRAF-process term to a pathway-specific target that fits
the keyword's RLR/cytoplasmic-PRR biology.

- **Keyword:** [KW-1110 "Inhibition of host TRAFs by virus"](https://www.uniprot.org/keywords/KW-1110)
- **Parent keyword:** [KW-1113 "Inhibition of host IFN-mediated response initiation by virus"](https://www.uniprot.org/keywords/KW-1113)

### Former mapping

| GO ID | Label |
|---|---|
| GO:0039527 | symbiont-mediated suppression of host TRAF-mediated signal transduction |

- QuickGO now lists this term as obsolete. GO:0039527 was retired via
  [geneontology/go-ontology#29238](https://github.com/geneontology/go-ontology/issues/29238)
  because "TRAF-mediated signal transduction" is not a real pathway on the
  ontology's process branch (TRAFs act in many downstream pathways: TLR,
  TNF/TNFR, cGAS-STING, RLR, etc.).

### Current replacement mapping

| GO ID | Label |
|---|---|
| GO:0140476 | symbiont-mediated suppression of host cytoplasmic pattern recognition receptor signaling pathway via inhibition of TRAF activity |

- GO:0140476 now resolves in QuickGO, and the current GO
  `uniprotkb_kw2go` file maps KW-1110 to it.

### Nature of the change

Lateral / more-specific move within the same "symbiont-mediated suppression of
host signaling" branch. The replacement target explicitly ties TRAF-inhibition to
the **cytoplasmic pattern recognition receptor (PRR) signaling pathway** family
(RIG-I / MDA5 / LGP2 → MAVS → TBK1 / IRF3 / NF-κB), which matches the
cytoplasmic-PRR mapping of the parent keyword KW-1113 "Inhibition of host
IFN-mediated response initiation by virus". Reviewers on the upstream thread
note that TRAF is used by TLRs, TNFR, and cGAS-STING as well, so this new
target is a better fit for the specifically viral / RLR context that KW-1110
sits under, but it does *not* cover TRAF interference by bacteria or by viral
proteins that act via TLR, TNFR, or the separately modelled cGAS-STING route
(see the upstream comments by @genegodbold and @pgaudet for candidate
templates).

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6470](https://github.com/geneontology/go-annotation/issues/6470) (closed)
- Ontology / obsoletion ticket: [geneontology/go-ontology#29238](https://github.com/geneontology/go-ontology/issues/29238) (closed)
- Prior TRAF-branch discussion (signal-transduction cleanup): geneontology/go-ontology#26498 (referenced by #29238)

## Impact on this repo

**No gene reviews currently touch either identifier.**

Searches re-run on 2026-10-04:

- `rg -l "GO:0039527" genes -g "*-ai-review.yaml"` — no matches.
- `rg -l "GO:0140476" genes -g "*-ai-review.yaml"` — no matches.
- `rg -l "KW-1110" genes -g "*-ai-review.yaml"` — no matches.

So this repo had no reviews to rewrite after the mapping landed. The purpose
of this project page is therefore to preserve the KW2GO cleanup rationale, not
to queue existing rework.

## Follow-up

No local follow-up is required. If a viral or bacterial TRAF-interfering
effector enters this repo later, its `existing_annotations` review should
MODIFY away from GO:0039527 and toward GO:0140476 only when the annotation
actually carries evidence for a cytoplasmic-PRR / RLR context. TLR contexts
belong under GO:0140470; cGAS-STING contexts belong under the cGAS-STING
suppression branch, such as GO:0141074; and TNFR contexts should not be forced
into GO:0140476 just because the inhibited host molecule is a TRAF.

## Status

- **Created:** 2026-07-04
- **2026-07-04:** Watch-list created while GO:0140476 was not yet minted and
  KW2GO deployment was blocked on that.
- **2026-07-06:** go-annotation#6470 closed after GO:0140476 was added to the
  KW-1110 mapping.
- **Update 2026-09-26:** OLS shows GO:0140476 minted and GO:0039527 obsolete
  (consider GO:0140476 or GO:0140470). Re-ran the three greps: still no matches in
  `genes/`. The GO `external2go/uniprotkb_kw2go` file (version date 2026/07/06)
  maps KW-1110 to GO:0140476, so the mapping change has shipped.
- **Update 2026-10-04:** QuickGO, GO's current `uniprotkb_kw2go`, and exact
  local `genes/` searches still show the upstream mapping is complete and no
  local reviews need edits.
