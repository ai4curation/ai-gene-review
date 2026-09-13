---
title: "Naked Mole Rat (HETGA) Annotation Review"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [HETGA]
genes:
  - Has2
  - Hyal2
  - Cd44
  - Cgas
  - Ntrk1
  - Scn9a
  - Trpv1
  - Tac1
---

# Naked Mole Rat (HETGA) Annotation Review

The naked mole rat (*Heterocephalus glaber*, UniProt code `HETGA`, NCBI taxon 10181) is one
of the most intensively studied non-model mammals in ageing and sensory biology. It is
long-lived, strikingly cancer-resistant, insensitive to several classes of pain stimulus, and
tolerant of hypoxia. Almost none of that biology has reached the Gene Ontology.

## The situation this project addresses

Across the entire species, GOA holds roughly 335,000 annotations and **exactly one** of them
is experimental — `Apoa1`, protein homodimerization, IDA. Every other annotation on every
other naked mole rat protein is an electronic projection from a better-annotated ortholog or
from a sequence model:

| Source | `GO_REF` | What it asserts |
|---|---|---|
| Curator-reviewed ISS transfer | `GO_REF:0000024` | function of a named ortholog (in WITH/FROM) applies here |
| Ensembl Compara projection | `GO_REF:0000107` | orthology-based transfer |
| TreeGrafter / PANTHER | `GO_REF:0000118` | descent from an annotated ancestral node (a PTN id) |
| ARBA / UniRule | `GO_REF:0000117`, `0000104`, `0000120` | rule-based, from sequence features |
| InterPro2GO | `GO_REF:0000002` | domain-to-term mapping |
| Keyword / SubCell | `GO_REF:0000044` | UniProt controlled vocabulary |

Only six HETGA entries are Swiss-Prot reviewed at all (`APOE`, `ASAH1`, `HAS2`, `APOA1`,
`APOC3`, `APOA2`). Everything else is TrEMBL.

## Why that makes this species unusually worth reviewing

An ortholog projection is a hypothesis: *this protein does what the mouse or human protein
does.* For most species that hypothesis is untestable, because there is no species-specific
literature to test it against. The naked mole rat is the rare case where there is — and where
the literature exists **precisely because the protein diverged**. The species is famous for
the ways its proteins behave differently from their mouse and human counterparts.

So each annotation resolves one of three ways:

1. **The projection holds**, and the naked mole rat literature positively confirms it. The
   review upgrades an untested transfer into a grounded claim.
2. **The projection holds but is peripheral** — typically a developmental or organ-physiology
   term carried over from a mouse knockout or a rat tissue study, with no naked mole rat
   evidence either way. Non-core, or over-annotated.
3. **The protein is documented to differ.** This is where the value is.

Category 3 needs discipline. A *quantitative* difference — a weaker signal, a longer polymer,
a stronger proton block — usually refines a GO function rather than abolishing it. Removal
requires a positive biological argument from the species' own literature, not merely the
observation that the annotation arrived by pipeline.

Watch particularly for **organism-level physiology terms projected across species**. These
are the weakest transfers, because whole-animal physiology is exactly what differs between a
laboratory rat and a eusocial subterranean mole rat. `Has2` carries positive regulation of
urine volume and renal water absorption, both transferred by sequence similarity from rat.

## Batch 1: eight landmark genes

Two coherent stories, chosen because each has a well-documented naked-mole-rat-specific
molecular phenotype.

**The hyaluronan axis** — the basis of the cancer-resistance phenotype. Naked mole rat cells
secrete very-high-molecular-mass hyaluronan, several times longer than the mouse or human
polymer, and it accumulates because synthesis is increased *and* degradation is reduced.

| Gene | Accession | Role |
|---|---|---|
| `Has2` | G5AY81 (Swiss-Prot) | synthesises the very-high-molecular-mass polymer |
| `Hyal2` | A0A0P6J1Y4 | the degradation side of the balance |
| `Cd44` | A0AAX6R0R7 | the receptor that reads the polymer |

**Nociception** — the naked mole rat lacks several normal pain responses, and the causes are
distributed across different points of the pathway rather than concentrated in one channel.

| Gene | Accession | Role |
|---|---|---|
| `Scn9a` | G9DCX3 | NaV1.7 variant conferring acid insensitivity |
| `Ntrk1` | A0AAX6QC09 | hypofunctional TrkA, no NGF-induced sensitisation |
| `Trpv1` | G9DCX1 | the capsaicin/heat channel |
| `Tac1` | A0A0P6JY17 | substance P precursor |

**`Cgas`** (A0AAX6RS70) sits on its own and is the most interesting case in the batch. All
thirteen of its annotations come from a single PANTHER ancestral node. In humans and mice,
nuclear cGAS *suppresses* homologous recombination repair; recent work reports that the naked
mole rat protein *promotes* it. If that holds, it is a propagated annotation set carrying a
function reversed in sign in the target species.

## Method

- `just fetch-gene HETGA <Gene> --uniprot-id <ACC>` seeds the review from GOA.
- `just fetch-gene-pmids` returns nothing for these genes — GOA holds no PMIDs for them at
  all — so the literature was assembled by direct PubMed search on
  `(naked mole rat[tiab] OR Heterocephalus[tiab]) AND <topic>[tiab]` and cached with
  `just fetch-pmid`. 37 papers.
- **Deep research**: Affinage is human-only and refuses other species outright, so it was run
  on each **human ortholog** and stored in the gene folder under a filename that names the
  species scope (`<Gene>-deep-research-affinage-human-ortholog.md`). It is a conserved-mechanism
  baseline, never evidence about the naked mole rat protein. Falcon was run for the naked mole
  rat itself and produced a report for all eight genes; note that several tripped the wrapper's
  600 s timeout and returned a non-zero exit code while still writing a complete file, so check
  for the file rather than trusting the exit status.

## Results

180 annotations reviewed across the eight genes, none left pending.

| Action | n |
|---|---|
| ACCEPT | 54 |
| KEEP_AS_NON_CORE | 58 |
| MARK_AS_OVER_ANNOTATED | 27 |
| MODIFY | 22 |
| NEW | 11 |
| REMOVE | 4 |
| UNDECIDED | 4 |

The shape of that distribution is the headline. Only 4 annotations of 180 were removed, and
85 were kept but demoted to non-core or flagged as over-annotated. Ortholog projection into
this species is mostly *correct but unfocused*: it delivers the right molecular function
together with a large tail of developmental and organ-physiology terms that no naked mole rat
evidence supports.

Five new terms were proposed, each verified absent from GO including a `secondaryIds` check so
that a merged identifier is not mistaken for a missing one:

| Gene | Proposed term |
|---|---|
| `Has2` | high molecular mass hyaluronan biosynthetic process |
| `Hyal2` | regulation of hyaluronan polymer size |
| `Scn9a` | proton-inhibited voltage-gated sodium channel activity |
| `Trpv1` | vanilloid-gated monoatomic cation channel activity |
| `Cd44` | positive regulation of basal ATF6-mediated signalling |

Three of the five say something GO currently cannot: that a polymer's *length* is the
biologically important property, that a channel can be *closed* rather than opened by protons,
and that a sensor's resting set-point is distinct from the size of its stress response.

### A propagation bug worth naming

The `Hyal2` removal of `GO:0001618` virus receptor activity is the clearest case. The
annotation is a `GO_REF:0000120` rule transfer whose donor set contains mouse Hyal2 — and GOA
separately records a curated `NOT|enables GO:0001618` IDA on that very mouse protein. The
pipeline propagated a positive assertion out of a donor set holding an explicit experimental
negation for the identical term. A dependent annotation, `GO:0046718` symbiont entry into host
cell, exists only because the receptor annotation does, and falls with it.

### An expressivity gap found along the way

For `Has2`, the naked mole rat coding sequence expressed in human HEK293 cells makes them
secrete high-molecular-mass hyaluronan, and shRNA knockdown in naked mole rat fibroblasts
reduces it. That is direct and mutant-phenotype evidence in this species for terms currently
carried as ISS. There is no way to record it: the validator rejects `action: NEW` for any term
already present in GOA, on the GO id alone, so "the term is right but the evidence code
understates what is known" cannot be expressed. For a species where *every* annotation is
electronic, that is the single most valuable recommendation a review could make.

## Notes for anyone extending this

The decisive paper for a naked mole rat gene is frequently **titled for a different gene**.
The most informative recent result bearing on hyaluronan degradation is titled for `TMEM2`,
not for either hyaluronidase. Search partners, paralogs and the pathway, not just the symbol.

Several key papers are abstract-only in the cache, including all four cGAS papers and the
primary NaV1.7 acid-insensitivity paper. Quote only what those abstracts state.
