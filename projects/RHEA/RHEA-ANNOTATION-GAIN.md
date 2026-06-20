---
title: "RHEA->GO Mapping: Swiss-Prot Coverage & Annotation Gain"
---

# Swiss-Prot Annotation Gain & Coverage

**Parent project:** [RHEA.md](../RHEA.md) - **Mappings:** [rhea2go.sssom.yaml](rhea2go.sssom.yaml) - **Script:** [rhea_annotation_gain.py](rhea_annotation_gain.py)

Gain is measured from **Swiss-Prot (reviewed)** entries: how many reviewed entries carry the RHEA
reaction but do not already have the mapped GO term (`go:` is closure-aware, so a more specific
child counts as covered).

## Headline

| Scope | New GO MF annotations |
|-------|----------------------:|
| **Swiss-Prot (reviewed)** | **42** |
| all UniProtKB (secondary, mostly TrEMBL) | 26,074 |

## Swiss-Prot coverage status

We systematically scored **all 256 remaining unmapped EC-bridge reactions** (RHEA whose EC maps to
a single specific GO term) for Swiss-Prot gain. **Only 4 had any reviewed gap; all 4 are now
mapped.** So **every cleanly-mappable RHEA reaction on a reviewed entry is now covered** -- the
EC-bridge Swiss-Prot residual gain is **0**. Reviewed enzymes carrying a reaction almost always
already have the term (manual curation / EC2GO), so the curated gain is intrinsically small.

### What remains is a *missing-GO-term* problem, not a mapping problem

The only Swiss-Prot entries with a RHEA still lacking a reaction-specific term are those whose
reaction has **no GO term to map to at all**. Scoping the new-term-needed set (unmapped reactions
whose EC is absent from `ec2go`):

- **~2,331** such reactions exist; **~1,942** appear on at least one reviewed entry
  (150-reaction sample: 125/150 had a reviewed entry).
- These cannot be closed by adding `rhea2go` rows -- each needs a **new GO molecular-function
  term** (a GO term-request effort). We have seeded **7** such proposals (`sssom:NoTermFound`);
  the remainder is the backlog to full reviewed coverage.

So: full Swiss-Prot coverage **via existing GO terms is achieved**; full coverage *period* is
gated on creating ~1,900 new GO terms, not on more mappings.

## Swiss-Prot gains (every reviewed annotation the mappings add)

| RHEA | GO term | Swiss-Prot gain |
|------|---------|----------------:|
| RHEA:36079 | GO:0002950 ceramide phosphoethanolamine synthase activity | 6 |
| RHEA:26422 | GO:0004062 aryl sulfotransferase activity | 5 |
| RHEA:43620 | GO:0031132 serine 3-dehydrogenase activity | 5 |
| RHEA:49072 | GO:0018640 dibenzothiophene monooxygenase activity | 5 |
| RHEA:14321 | GO:0050109 morphine 6-dehydrogenase activity | 5 |
| RHEA:36231 | GO:0004623 A2-type glycerophospholipase activity | 4 |
| RHEA:59980 | GO:0008413 8-oxo-7,8-dihydroguanosine triphosphate pyrophosphatase activity | 4 |
| RHEA:65152 | GO:0047243 flavanone 7-O-beta-glucosyltransferase activity | 2 |
| RHEA:25193 | GO:0018504 cis-1,2-dihydrobenzene-1,2-diol dehydrogenase activity | 1 |
| RHEA:32951 | GO:0050006 isomaltulose synthase activity | 1 |
| RHEA:85243 | GO:0003960 quinone reductase (NADPH) activity | 1 |
| RHEA:27682 | GO:0004550 nucleoside diphosphate kinase activity | 1 |
| RHEA:59352 | GO:0047979 hexose oxidase activity | 1 |
| RHEA:68796 | GO:0004575 sucrose alpha-glucosidase activity | 1 |

Total: **42** reviewed annotations across 14 mappings.

## Reproduce

```bash
uv run python rhea_annotation_gain.py
```
