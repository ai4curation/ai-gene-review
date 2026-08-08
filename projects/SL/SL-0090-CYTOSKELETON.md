---
title: "SL-0090 Cytoskeleton"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, mouse, worm, SCHPO, BETPN, DORPE, DROME]
autolink_gene_symbols: false
---

# SL-0090 Cytoskeleton → GO:0005856

59 SL-unique annotations reviewed, **16 with a hard issue (27%)**. This is where the SL and
[SPKW](../SPKW.md) failure modes meet: the flagged cases split cleanly into two patterns, one
of which is SPKW's regulatory conflation wearing a cellular-component costume.

## Pattern A — under-specification (the SL-0162 pattern)

The majority. `cytoskeleton` where the evidence supports a named filament system:

| gene | proposed instead |
|---|---|
| SCHPO mid1 | GO:0110085 mitotic actomyosin contractile ring, GO:0071341 medial cortical node |
| human ABRAXAS2 | microtubule / spindle-pole components |
| human BAIAP2L1 | GO:0015629 actin cytoskeleton |
| human CFAP61 | GO:0005930 axoneme ("already annotated with stronger evidence") |
| human GDPD2 | actin filaments |
| human ABRA | actin-specific term "already independently supported on the same record" |
| human ACTR10 | GO:0005869 dynactin complex |

## Pattern B — association is not residence

This is the interesting one, and it has no analogue in SL-0162:

> **human SGCA** — "SGCA is not itself a cytoskeletal component but rather a sarcolemmal
> membrane protein that indirectly associates with the cytoskeleton through the
> dystrophin-glycoprotein complex."
>
> **human SGCE** — "SGCE is transmembrane protein in DGC that indirectly associates with
> cytoskeleton, not a cytoskeletal protein per se. The term 'cytoskeleton' suggests SGCE is
> part of cytoskeletal structure itself."
>
> **human ACTL7B** — "asserts a compartment that no observation supports, derived from a
> by-similarity statement"

Here the term is not merely vague — it is **wrong in kind**. A transmembrane protein that
binds the cytoskeleton is not located in it. This is the cellular-component counterpart of
SPKW's "regulatory conflation" (gene regulates X, annotated to X): *gene binds X, annotated
to X*.

The pattern generalises beyond these three. The corpus's SL-0090 population is full of
cytoskeletal *regulators and modifiers* rather than components — ABL1 (kinase), HDAC6 and
SIRT2 (tubulin deacetylases), INPP5D (phosphatase), FERMT2 and CD2AP and BAIAP2 (adaptors),
GAPDH (moonlighting glycolytic enzyme). Each is plausibly *at* the cytoskeleton while doing
its job, so none is a clear error; but "cytoskeleton" is carrying an implication of
membership that the evidence does not license. Adjudicating that set is the natural next
batch and would need per-gene reading, not a rule.

## Batch reviewed under this subproject

Six annotations moved `ACCEPT` → `MARK_AS_OVER_ANNOTATED`, all Pattern A, all with a strictly
more specific term already present from independent evidence:

| gene | already carries | source |
|---|---|---|
| human MAPT | GO:0045298 tubulin complex; GO:0005874 microtubule | IDA |
| human MAP7 | GO:0005875 microtubule associated complex; GO:0005874 microtubule | TAS |
| mouse Tuba1a | GO:0035371 microtubule plus-end; GO:0005881 cytoplasmic microtubule | IMP, IDA |
| human ACTG2 | GO:0015629 actin cytoskeleton | IBA |
| human WIPF1 | GO:0005884 actin filament; GO:0015629 actin cytoskeleton | IBA |
| worm che-3 | GO:0005868 cytoplasmic dynein complex; GO:0005930 axoneme | IBA |

Pattern B cases were left alone deliberately. Deciding whether SGCA-like proteins should lose
the annotation or keep it with a qualifier is a question about GO's `located_in` semantics for
peripheral associations, not a granularity call, and it should be settled as a policy before
being applied gene by gene.

## Note on redundancy

SL-0090 has the highest redundancy in the corpus — **80%** of its SL-unique annotations sit on
genes that already carry a more specific cytoskeletal term. Yet before this batch the issue
rate was identical in both groups (17% redundant, 17% not). That is the single strongest piece
of evidence against the deduplication rule proposed in the [SL project's](../SL.md) opening
draft.
