---
title: "RHEA->GO Mapping: Swiss-Prot Annotation Gain"
---

# Swiss-Prot Annotation Gain from the Curated RHEA->GO Mappings

**Parent project:** [RHEA.md](../RHEA.md) - **Mappings:** [rhea2go.sssom.yaml](rhea2go.sssom.yaml) - **Script:** [rhea_annotation_gain.py](rhea_annotation_gain.py)

Gain is measured from **Swiss-Prot (reviewed)** entries: for each mapping, how many reviewed
UniProtKB entries carry the RHEA reaction but do **not** already have the mapped GO term
(`gain = N(rhea AND reviewed) - N(rhea AND go AND reviewed)`; UniProt `go:` is closure-aware, so
entries carrying a more specific child are excluded). This is the curation-relevant, trustworthy
number; the all-of-UniProtKB figure (mostly automated TrEMBL annotations) is secondary context.

## Headline

| Scope | New GO MF annotations |
|-------|----------------------:|
| **Swiss-Prot (reviewed)** | **34** |
| all UniProtKB (secondary, mostly TrEMBL) | 25,842 |

Across 111 GO-bearing mappings, 10 add a reviewed annotation. The reviewed
gain is small because curated enzymes carrying the reaction almost always already have the term
(manual curation / EC2GO) -- the EC-masking result at the annotation level. The mappings still
fill genuine **Swiss-Prot curation gaps** where the term is missing, listed below.

## Swiss-Prot gains (every reviewed annotation added)

| RHEA | GO term | Swiss-Prot gain | reviewed carry reaction | already have |
|------|---------|----------------:|------------------------:|-------------:|
| RHEA:36079 | GO:0002950 ceramide phosphoethanolamine synthase activity | 6 | 14 | 8 |
| RHEA:26422 | GO:0004062 aryl sulfotransferase activity | 5 | 5 | 0 |
| RHEA:43620 | GO:0031132 serine 3-dehydrogenase activity | 5 | 8 | 3 |
| RHEA:49072 | GO:0018640 dibenzothiophene monooxygenase activity | 5 | 5 | 0 |
| RHEA:36231 | GO:0004623 A2-type glycerophospholipase activity | 4 | 25 | 21 |
| RHEA:59980 | GO:0008413 8-oxo-7,8-dihydroguanosine triphosphate pyrophosphatase activity | 4 | 8 | 4 |
| RHEA:65152 | GO:0047243 flavanone 7-O-beta-glucosyltransferase activity | 2 | 3 | 1 |
| RHEA:25193 | GO:0018504 cis-1,2-dihydrobenzene-1,2-diol dehydrogenase activity | 1 | 1 | 0 |
| RHEA:32951 | GO:0050006 isomaltulose synthase activity | 1 | 1 | 0 |
| RHEA:85243 | GO:0003960 quinone reductase (NADPH) activity | 1 | 17 | 16 |

## Selecting future batches

Per project convention, future mapping batches are ranked by **Swiss-Prot gain** (not the
all-UniProt figure), so curation effort targets reactions that fill real reviewed-entry gaps.

## Caveats

- broadMatch rows propagate a broader term; a root-level broadMatch should not be propagated as-is.
- The 7 `sssom:NoTermFound` new-term rows contribute 0 (no GO object) until the proposed terms exist.

## Reproduce

```bash
uv run python rhea_annotation_gain.py   # Swiss-Prot gain is the primary total
```
