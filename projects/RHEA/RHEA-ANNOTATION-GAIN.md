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

## Litmus test: is there a *missed-mapping* gap? (no)

Per the project's value test — *would a Swiss-Prot curated entry lose a good,
non-redundant GO annotation if we did not make the mapping?* — and **without
assuming EC2GO will be extended**, I hunted the no-`ec2go` space for reactions
where a correct GO term already exists but isn't reachable by EC/RHEA xref.

First, a structural check: **GO's own RHEA xrefs equal `rhea2go` exactly** (7,746,
zero difference) and **GO's EC xrefs equal `ec2go` exactly** (4,830, zero
difference). So there is no hidden bridge — a reaction unmapped in `rhea2go` whose
EC is absent from `ec2go` has **no xref path to GO at all**.

Name-matching reviewed enzymes for those reactions to GO terms produced 30
Swiss-Prot-gain candidates — but **verification against each GO term's definition
reaction rejected all of them**: the matched term is for a *different* reaction
(different cofactor, electron acceptor, or stereochemistry), which is exactly why
GO keeps it separate and why it isn't xref-linked:

| Reaction (unmapped) | Name-matched GO term | Why it is the WRONG term |
|---------------------|----------------------|--------------------------|
| RHEA:28202 light-independent protochlorophyllide reductase (EC 1.3.7.7, **ferredoxin**) | GO:0016630 (def uses **NADPH**) | different reductant (DPOR vs LPOR) |
| RHEA:26522 2-methylcitrate dehydratase (EC 4.2.1.117, **trans**) | GO:0047547 (def is **cis**, EC 4.2.1.79) | different stereochemistry |
| RHEA:26442 alcohol dehydrogenase (EC 1.1.5.5, **quinone**) | GO:0004022 (def is **NAD⁺**) | different electron acceptor |
| RHEA:27417 nicotinate dehydrogenase (EC 1.17.2.1, **cytochrome**) | GO:0050138 (def is **NADP**) | different electron acceptor |
| RHEA:29595 sulfoacetaldehyde dehydrogenase (EC 1.2.1.81, **acylating/NADP**) | GO:0102984 (def is **NAD, non-acylating**) | different reaction |

The remaining candidates matched **generic class roots** (`hydro-lyase activity`,
`demethylase activity`, `5'-nucleotidase activity`) or were outright **name
collisions** (RHEA:16301, an IL-18-receptor protein carrying a spurious NADase
reaction, matched `interleukin-18 receptor activity`; another matched `iron ion
binding`). None is a good non-redundant annotation.

**Conclusion.** There is **no missed-mapping gap**: every reviewed entry whose
reaction has a *correct* existing GO term is already covered (the EC-bridge work
above), and the reactions that remain genuinely **lack a correct GO term** —
GO distinguishes the cofactor/stereochemistry variants they represent. So closing
the rest is strictly a **new-GO-term** effort (the 7 seeded `sssom:NoTermFound`
rows are the start), not more mapping. This holds the line on the litmus test:
we do not add a mapping unless a Swiss-Prot entry would gain a *correct*,
non-redundant annotation.
