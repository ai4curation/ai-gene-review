---
title: "Novel InterPro2GO predictions — full adjudication"
autolink_gene_symbols: false
---

# Adjudication of all novel InterPro2GO predictions (yeast + pombe)

Every InterPro2GO prediction absent from the gene's GOA (the "novel" set from
[`interpro2go_novelty.py`](interpro2go_novelty.py)) is adjudicated below with the
de Crécy-Lagard et al. (2025) taxonomy: **COR** (correct novel), **CNN** (correct, not
novel), **LSP** (less precise), **UNC** (uncertain), **PLI** (paralog incorrect), **NPI**
(nonparalog incorrect), **REP** (frequency-biased repetition). Each call is grounded in the
gene's curated UniProt/GOA function; the non-trivial cases have schema-validated
per-gene `-interpro2go-predictions-review.yaml` files (linked).

## Summary of outcomes (37 predictions)

| assessment | n | meaning |
|---|---|---|
| CNN | 30 | correct but already curated (domain redundancy) |
| PLI | 2 | paralog/subfamily over-annotation ([SSZ1](../../genes/yeast/SSZ1/SSZ1-interpro2go-predictions-review.yaml), [aah1](../../genes/SCHPO/aah1/aah1-interpro2go-predictions-review.yaml)) |
| LSP | 3 | correct but uninformatively generic |
| UNC | 2 | unsupported / not verifiable |
| **COR** | **0** | **no genuinely-novel correct predictions on these well-characterized genes** |

**The headline: zero COR.** On well-characterized genes, InterPro2GO produces *no*
correct-and-novel calls — correct predictions are CNN (redundant with curation), and
everything else is imprecise (LSP), unverifiable (UNC), or a paralog error (PLI). This is
the quantitative face of the 90–94% CNN rate in [RESULTS §3](RESULTS.md): a domain
predictor scored on curated genes mostly re-derives what curators already knew, and its
*residual* novel output is dominated by errors and generic terms, not discoveries.

## S. cerevisiae (16)

| gene | predicted term | call | CS | rationale |
|---|---|---|---|---|
| SSA1 | GO:0140662 ATP-dependent protein folding chaperone | CNN | 2 | canonical cytosolic Hsp70 foldase; function established |
| SSA2 | GO:0140662 | CNN | 2 | canonical cytosolic Hsp70 (SSA paralog) |
| SSA3 | GO:0140662 | CNN | 2 | stress-inducible cytosolic Hsp70 |
| SSA4 | GO:0140662 | CNN | 2 | stress-inducible cytosolic Hsp70 |
| SSB2 | GO:0140662 | CNN | 2 | ribosome-associated Hsp70 with functional ATPase foldase activity |
| KAR2 | GO:0140662 | CNN | 2 | ER BiP; canonical ATP-dependent chaperone |
| SSQ1 | GO:0140662 | CNN | 2 | mitochondrial Hsp70; ATP-dependent Fe-S cluster transfer |
| LHS1 | GO:0140662 | CNN | 2 | ER Hsp110/Grp170; has ATPase catalytic activity, ATP-dependent chaperone |
| **SSZ1** | GO:0140662 | **PLI** | 0 | atypical RAC Hsp70; binds ATP but does not hydrolyze it, ATPase dispensable → ancestral foldase MF misapplied ([review](../../genes/yeast/SSZ1/SSZ1-interpro2go-predictions-review.yaml)) |
| CPR6 | GO:0000413 protein peptidyl-prolyl isomerization | CNN | 2 | cyclophilin (PPIase); the BP is entailed by its defining catalytic MF |
| CPR7 | GO:0000413 | CNN | 2 | cyclophilin Hsp90 co-chaperone; PPIase activity is its defining function |
| CRH1 | GO:0005618 cell wall | CNN | 2 | cell-wall chitin–glucan transglycosylase; wall localization established |
| IRE1 | GO:0006468 protein phosphorylation | CNN | 2 | bifunctional ER-stress kinase/RNase; autophosphorylation entailed by kinase MF |
| RIM15 | GO:0006468 | CNN | 2 | PAS/Greatwall-family protein kinase; phosphorylation entailed by MF |
| ACL4 | GO:0005515 protein binding | LSP | 2 | dedicated assembly chaperone that binds Rpl4; bare "protein binding" is less precise than its known specific role |
| YGR117C | GO:0005515 protein binding | UNC | 1 | poorly characterized ORF; uninformative binding term, not verifiable |

## S. pombe (21)

| gene | predicted term | call | CS | rationale |
|---|---|---|---|---|
| ark1 | GO:0006468 protein phosphorylation | CNN | 2 | Aurora kinase; BP entailed by kinase MF |
| bub1 | GO:0006468 | CNN | 2 | spindle-checkpoint kinase |
| cdc2 | GO:0006468 | CNN | 2 | cyclin-dependent kinase (CDK1 ortholog) |
| cdc7 | GO:0006468 | CNN | 2 | SIN pathway kinase |
| cds1 | GO:0006468 | CNN | 2 | replication-checkpoint effector kinase |
| chk1 | GO:0006468 | CNN | 2 | DNA-damage-checkpoint kinase |
| mph1 | GO:0006468 | CNN | 2 | Mps1 spindle-checkpoint kinase |
| plo1 | GO:0006468 | CNN | 2 | Polo-like kinase |
| pom1 | GO:0006468 | CNN | 2 | DYRK-family cell-polarity kinase |
| ppk34 | GO:0006468 | CNN | 2 | protein kinase |
| sid2 | GO:0006468 | CNN | 2 | SIN NDR-family kinase |
| sty1 | GO:0006468 | CNN | 2 | stress-activated MAP kinase |
| wee1 | GO:0006468 | CNN | 2 | Wee1 kinase (inhibitory CDK phosphorylation) |
| wis1 | GO:0006468 | CNN | 2 | MAP2K in the Sty1 stress pathway |
| cdc25 | GO:0006470 protein dephosphorylation | CNN | 2 | Cdc25 phosphatase; activates Cdc2 by dephosphorylation |
| mus81 | GO:0004518 nuclease activity | CNN | 2 | structure-specific endonuclease (Mus81–Eme1) |
| **slp1** | GO:1904668 positive regulation of ubiquitin protein ligase activity | CNN | 2 | Cdc20/Fizzy APC/C coactivator; already curated via GO:0097027 ([review](../../genes/SCHPO/slp1/slp1-interpro2go-predictions-review.yaml)) |
| **aah1** | GO:0004556 alpha-amylase activity | **PLI** | 0 | GH13 4-alpha-glucanotransferase (curated GO:0004134), not a hydrolytic amylase → subfamily over-call ([review](../../genes/SCHPO/aah1/aah1-interpro2go-predictions-review.yaml)) |
| pol5 | GO:0008134 transcription factor binding | UNC | 1 | rRNA-biogenesis/DNA-pol-φ factor; TF-binding not supported by curated evidence |
| cdc12 | GO:0016043 cellular component organization | LSP | 2 | septin (cytokinetic ring); correct but maximally generic BP |
| ral2 | GO:0005515 protein binding | LSP | 2 | Ras1-pathway (SPS) component with a known specific role; bare binding is less precise |

## Scope note

The 14 pombe kinases and the yeast kinases (IRE1, RIM15) share one trivially-entailed
prediction (`protein phosphorylation` from a kinase domain) and are adjudicated in the
table rather than as 16 near-identical per-gene YAML files. Schema-validated per-gene
`-interpro2go-predictions-review.yaml` files are provided for the four instructive,
non-trivial cases spanning the error spectrum: **SSZ1** (PLI), **aah1** (PLI), **slp1**
(CNN, a clean correct call), and the earlier SSZ1 pairing. The remaining novel `protein
binding` predictions (ACL4, YGR117C, ral2) illustrate the uninformative-binding /
frequency-bias signature this repo's curation guideline explicitly warns against.
