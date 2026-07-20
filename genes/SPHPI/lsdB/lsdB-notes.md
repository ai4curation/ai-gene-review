# lsdB / LSD-III (Q52008, Sphingomonas paucimobilis) — review notes

Lignostilbene-α,β-dioxygenase isozyme III (LSD-III), EC 1.13.11.43, of *Sphingomonas
(Pseudomonas) paucimobilis* TMY1009 — one of the **founding members** of the stilbene cleavage
oxygenase (SCO) / CCO superfamily. Non-heme iron dioxygenase.

- **Reaction:** lignostilbene (1,2-bis(4-hydroxy-3-methoxyphenyl)ethylene) + O2 = **2 vanillin**
  (RHEA:21340). Acts in **lignin-derived stilbene catabolism**.
- Three isozymes (I, II, III) purified and compared [PMID:7763880]; gene cloned [PMID:8534977].

## The key point for the SCO project

LSD-III is the **experimentally-grounded anchor** of the stilbene-cleavage clade: it already carries the
**correct specific IDA annotations** — lignostilbene α,β-dioxygenase activity (GO:0050054) and lignin
catabolic process (GO:0046274). Yet it *also* carries the **wrong TreeGrafter carotenoid terms**
(GO:0010436, GO:0016121; GO_REF:0000118) — the same over-annotation seen on cao-1 (IBA) and NOV1
(IEA/TreeGrafter). Here the contradiction is starkest: the automated carotenoid terms directly conflict
with the gene's own experimental annotations.

GO:0050054 (lignostilbene α,β-dioxygenase activity) is the **existing leaf term** that the proposed
grouping *stilbene α,β-dioxygenase activity* would parent, alongside the resveratrol leaf GO:7770086.

## Decisions
- REMOVE the two TreeGrafter carotenoid terms (contradicted by own IDA).
- ACCEPT GO:0050054 (IEA + IDA), GO:0046274 (IDA), GO:0016702 (IEA), GO:0005506 iron (ISS).
- Core function: lignostilbene α,β-dioxygenase in lignin catabolic process.
