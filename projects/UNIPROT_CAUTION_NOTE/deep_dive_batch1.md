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
| **DPYSL5** | Q9BPU6 | dihydropyrimidinase activity (metal-cofactor residues) | GO:0004157 dihydropyrimidinase | **NOT\|enables** (IBA) **plus** two positive **IEA** hydrolase parent terms (see below) | ⚠️ **suspect over-annotation** (not a strict contradiction) |

## The one actionable finding: DPYSL5 (CRMP5)

DPYSL5 has the specific catalytic term correctly negated:

- `GO:0004157` dihydropyrimidinase activity — **NOT|enables** (IBA, GO_REF:0000033)

…and still carries two positive **IEA** parent terms derived from
metallo-hydrolase fold signatures:

- `GO:0016787` hydrolase activity — IEA, InterPro:IPR006680 (Amidohydrolase-related)
- `GO:0016810` hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds — IEA, InterPro:IPR011059 (Metal-dependent hydrolase composite)

**This is not a logical contradiction.** Under GO's true-path rule a `NOT`
annotation propagates *downward* (to subtypes of dihydropyrimidinase), **not**
upward — so `NOT enables dihydropyrimidinase` does not entail `NOT enables
hydrolase`. A protein can consistently be "some hydrolase" while "not a
dihydropyrimidinase," so the positive-parent + negated-child pair is logically
admissible.

**It is, however, an evidentially suspect domain-based over-annotation.** Both
positive terms rest *only* on fold/superfamily signatures (IPR006680, IPR011059;
UniProt `SIMILARITY: Belongs to the metallo-dependent hydrolases superfamily`) —
pure "has-the-fold ⇒ has-the-activity" propagation. The CAUTION states DPYSL5
"Lacks most of the conserved residues that are essential for binding the metal
cofactor and hence for dihydropyrimidinase activity," and catalysis across the
*entire* metallo-dependent hydrolase superfamily depends on that metal site. So
the very fact that justifies the curated `NOT` (no metal-binding residues) also
undermines the evidential basis for the generic hydrolase parents: there is no
positive evidence DPYSL5 performs *any* hydrolysis, and its curated function is
non-catalytic (`FUNCTION: negative regulation of dendrite outgrowth`; a CRMP5
cytoskeletal adapter).

**Proposed action:** `MARK_AS_OVER_ANNOTATED` for `GO:0016787` and `GO:0016810`
on DPYSL5 — domain-based IEA propagations that are unsupported and biologically
improbable given metal-site loss. This is a deliberately *weaker* claim than
`REMOVE`-as-contradiction, and weaker than asserting `NOT hydrolase` (which would
overclaim absence of activity without positive evidence). The CRMP5
protein-binding / cytoskeleton annotations are the real function and are
retained. Same pattern as
[OVER_ANNOTATION_PATTERNS](../OVER_ANNOTATION_PATTERNS.md) /
[CONTESTED_FUNCTION](../CONTESTED_FUNCTION.md).

> **Action taken.** `genes/human/DPYSL5/DPYSL5-ai-review.yaml` is now a full
> DRAFT review (schema- and term-validated). The two IEA hydrolase terms
> (`GO:0016787`, `GO:0016810`) are set to **`REMOVE`** with the reasoning above
> (electronic over-propagation refutable on biological grounds — *not*
> `MARK_AS_OVER_ANNOTATED`, which is reserved for terms the gene is genuinely but
> peripherally related to). The two curated `NOT` annotations are `ACCEPT`-ed as
> correct, and the IMP `negative regulation of dendrite morphogenesis`
> (PMID:33894126) is recorded as the core function.

## All five reviews completed

Full, schema- and term-validated DRAFT reviews are now written for every gene in
the batch:

| Gene | Catalytic `NOT` handled | Notable actions |
|------|-------------------------|-----------------|
| **DPYSL5** | ACCEPT (dihydropyrimidinase) | **2× REMOVE** of domain-based hydrolase IEAs; core = neg. reg. dendrite morphogenesis |
| **RHBDF1** | ACCEPT (serine endopeptidase, IBA+IDA) | core = ADAM17/EGFR sheddase regulation; ER/Golgi scaffold |
| **SUMF2** | n/a (no catalytic MF was asserted) | ACCEPT enzyme-inhibitor activity (inhibits SUMF1); 4× over-annotated viral/interactome protein binding |
| **PANK4** | ACCEPT (pantothenate kinase, IBA+IMP) | ACCEPT real phosphatase activity — a **domain-swap** pseudoenzyme (dead PanK domain + active 4'-phosphopantetheine phosphatase) |
| **NAALADL2** | n/a (no catalytic MF asserted) | molecular function recorded as **not established**; flagged nucleoplasm vs membrane-topology conflict |

Only DPYSL5 required a `REMOVE` of a positively-asserted catalytic term; the
others were already self-consistent (curators had either negated the lost
activity or never asserted it). PANK4 is the most instructive: the CAUTION
negates one domain's activity while a *different*, real activity is correctly
annotated — a reminder that "pseudoenzyme" can mean domain-specific, not
whole-protein, inactivation.

## Cross-resource insight (worth generalizing)

For 4 of 5 genes the GO **`NOT` qualifier is the curated counterpart of the
UniProt CAUTION note** — curators have already encoded "this family member lost
the activity" as an explicit negative annotation, frequently citing the *same*
primary paper named in the CAUTION (e.g. RHBDF1 ↔ PMID:21439629; PANK4 ↔
PMID:30927326). This is a strong cross-resource consistency signal and a good
sanity check on the CAUTION→over-annotation hypothesis.

The remaining leak is almost always **IEA from InterPro/UniRule domain rules**
(DPYSL5's two hydrolase terms), applied before/independently of the
member-specific NOT. So a useful **review flag** (not a contradiction detector)
is: *"a **positive IEA** parent term whose curated, more-specific **child** is
`NOT`-ed (or whose activity a CAUTION reports as lost)."* Such a pair is
logically consistent — `NOT` does not propagate up — but it marks a
**fold/domain-based parent annotation that may have lost its evidential basis**,
and is worth a curator's eye. The adjudication is then evidential, not logical:
is there any positive support for the parent activity, or does it rest solely on
the fold signature that the CAUTION/`NOT` has specifically discredited?

## Reproducibility

```bash
for g in RHBDF1 SUMF2 PANK4 DPYSL5 NAALADL2; do
  uv run ai-gene-review fetch-gene human "$g" --output-dir .
done
# then inspect molecular_function rows in genes/human/<G>/<G>-goa.tsv
```

Last updated: 2026-06-16
