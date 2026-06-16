---
title: "CAUTION Deep Dive — Batch 1 (human degenerate-domain pseudo-enzymes)"
---

# Deep Dive Batch 1 — Human pseudo-enzymes flagged by UniProt CAUTION

[← back to UNIPROT_CAUTION_NOTE](../UNIPROT_CAUTION_NOTE.md)

Five human entries from the `degenerate-domain` candidate list
([`candidates.md`](candidates.md)) were fetched (`fetch-gene human <GENE>`) and
their curated GO **molecular-function** annotations were checked against the
UniProt CAUTION note. The question for each: **does GOA still assert the
catalytic activity that the CAUTION note says the protein has lost?**

## Result summary

| Gene | UniProt acc | CAUTION says it lacks… | Lost-activity GO term | GOA status of that term | Verdict |
|------|-------------|------------------------|-----------------------|-------------------------|---------|
| **RHBDF1** | Q96CC6 | serine protease activity (no catalytic Ser-720) | GO:0004252 serine-type endopeptidase | **NOT\|enables** (IBA + IDA, PMID:21439629) | ✅ GO already negates it |
| **SUMF2** | Q8NBJ7 | FGE catalytic Cys-261/266 | (oxidoreductase / FGE) | **absent**; only binding + GO:0004857 enzyme inhibitor (TAS) | ✅ GO never asserted it |
| **PANK4** | Q9NVE7 | functional pantothenate kinase | GO:0004594 pantothenate kinase | **NOT\|enables** (IBA + IMP, PMID:30927326); real GO:0016791 phosphatase is positively annotated (EXP, PMID:27322068) | ✅ GO negates it; real function captured |
| **NAALADL2** | Q58DX5 | M28-peptidase zinc-binding + active sites | (peptidase / hydrolase) | **absent**; only protein binding | ✅ GO never asserted it |
| **DPYSL5** | Q9BPU6 | dihydropyrimidinase activity (metal-cofactor residues) | GO:0004157 dihydropyrimidinase | **NOT\|enables** (IBA) **but** two positive **IEA** hydrolase terms remain (see below) | ⚠️ **over-annotation found** |

## The one actionable finding: DPYSL5 (CRMP5)

DPYSL5 has the specific catalytic term correctly negated:

- `GO:0004157` dihydropyrimidinase activity — **NOT|enables** (IBA, GO_REF:0000033)

…yet still carries two **positive InterPro-derived IEA** parent terms that
contradict the loss-of-activity caution:

- `GO:0016787` hydrolase activity — IEA, InterPro:IPR006680
- `GO:0016810` hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds — IEA, InterPro:IPR011059

The UniProt CAUTION states DPYSL5 "Lacks most of the conserved residues that are
essential for binding the metal cofactor and hence for dihydropyrimidinase
activity" — i.e. it is a catalytically dead member of the amidohydrolase
(DHP/CRMP) family that functions as a cytoskeletal/axon-guidance adapter (CRMP5).
The two generic-hydrolase IEAs are **domain-presence over-annotations** of the
classic kind: they propagate the family's ancestral catalytic MF onto a member
that has demonstrably lost it.

**Proposed action:** `MARK_AS_OVER_ANNOTATED` (or `REMOVE`) for `GO:0016787` and
`GO:0016810` on DPYSL5, consistent with the curated `NOT|dihydropyrimidinase`
and the CAUTION note. (The CRMP5 protein-binding / cytoskeleton annotations are
the real function and are retained.) This belongs to the same pattern catalogued
in [OVER_ANNOTATION_PATTERNS](../OVER_ANNOTATION_PATTERNS.md) /
[CONTESTED_FUNCTION](../CONTESTED_FUNCTION.md).

## Cross-resource insight (worth generalizing)

For 4 of 5 genes the GO **`NOT` qualifier is the curated counterpart of the
UniProt CAUTION note** — curators have already encoded "this family member lost
the activity" as an explicit negative annotation, frequently citing the *same*
primary paper named in the CAUTION (e.g. RHBDF1 ↔ PMID:21439629; PANK4 ↔
PMID:30927326). This is a strong cross-resource consistency signal and a good
sanity check on the CAUTION→over-annotation hypothesis.

The remaining leak is almost always **IEA from InterPro/UniRule domain rules**
(DPYSL5's two hydrolase terms), which are applied before/independently of the
member-specific NOT. So the high-yield query for this project is **not** "does a
catalytic term exist?" but: *"does a **positive IEA** catalytic/parent term
co-exist with a curated **NOT** of its child (or a CAUTION of lost activity)?"* —
that conjunction is where the genuine over-annotations hide.

## Reproducibility

```bash
for g in RHBDF1 SUMF2 PANK4 DPYSL5 NAALADL2; do
  uv run ai-gene-review fetch-gene human "$g" --output-dir .
done
# then inspect molecular_function rows in genes/human/<G>/<G>-goa.tsv
```

Last updated: 2026-06-16
