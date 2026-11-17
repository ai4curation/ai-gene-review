# ospC3 (Shigella flexneri, A0A0H2US87) — curation notes

## Literature search record

No deep-research provider key exists in this environment, so this is a hand
search over the cached corpus and the UniProt record.

Sources checked:

- `genes/SHIFL/ospC3/ospC3-uniprot.txt` (Swiss-Prot A0A0H2US87, entry version 34,
  2026-09-02): FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, SUBUNIT,
  SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, the NAD+ BINDING and ACT_SITE
  features, and the large MUTAGEN set.
- All GOA-cited publications, fetched into `publications/`: PMID:23684308,
  PMID:34409271, PMID:34671164, PMID:35338844, PMID:35568036, PMID:36624349,
  PMID:37014865. Full text available for PMID:34409271, PMID:35568036 and
  PMID:37014865; the others are abstract-only in the cache.
- All four cited Reactome entries, cached in `reactome/`: R-HSA-9956602
  (CALM binds bacterial OspC3), R-HSA-9956624 (OspC3 ADP-riboxanates CASP4),
  R-HSA-9956667 (CASP4 binds CALM:OspC3), R-HSA-9640148 (Infection with
  Enterobacteria).
- Context read but not edited: a calmodulin/CaMKII pathway module and reviews of
  the two OspC GO-CAMs, proposed in ai4curation/ai-gene-review#5904 and not part
  of this branch; nothing in this review rests on them. The cached models
  themselves, `gocams/62b4ffe300005437/62b4ffe300005437-src.yaml` and
  `gocams/62b4ffe300005467/62b4ffe300005467-src.yaml`, are on main and were read.
- GO checks against the local GO build (oaklib `sqlite:obo:go`), 2026-11-04:
  `GO:0052041` is an `is_a` child of `GO:0052040` and a descendant of
  `GO:0051701`; `GO:0140886` is an `is_a` child of `GO:0052029`; `GO:0044164
  host cell cytosol` exists, defined as "The part of the host cell cytoplasm
  that does not contain organelles but which does contain other particulate
  matter, such as protein complexes", and is the host-perspective counterpart of
  `GO:0005829 cytosol`.

## What the protein is and does

OspC3 is a 484-residue OspC-family type III secretion effector on the Shigella
virulence plasmid, with an N-terminal ADP-ribosyltransferase-like catalytic
domain and a C-terminal ankyrin-repeat substrate-recognition domain (ANK 1-3,
residues 369-480).

### Core mechanism: arginine ADP-riboxanation of caspase-4/11

[PMID:34671164 "S. flexneri evaded pyroptosis mediated by caspase-11 or caspase 4 (hereafter referred to as caspase-11/4) using a type III secretion system (T3SS) effector, OspC3."]
[PMID:34671164 "Biochemical dissections uncovered an ADP-riboxanation modification on Arg314 and Arg310 in caspase-4 and caspase-11, respectively."]
[PMID:34671164 "ADP-riboxanation of the arginine blocked autoprocessing of caspase-4/11 as well as their recognition and cleavage of GSDMD."]

The reaction is two-step, and the structural work resolves both halves and
assigns the residues:
[PMID:36624349 "CaM-OspC3-caspase-4 ternary complex structures show that NAD+ binding reorganizes the catalytic pocket, in which D231 and D177 activate the substrate arginine for initial ADP-ribosylation and ribosyl 2'-OH in the ADP-ribosylated arginine, respectively, for subsequent deamination."]
UniProt records the corresponding mutagenesis: D177A abolishes the deamination
step without affecting the ADP-ribosylation step, and D231A abolishes activity
altogether.

Substrate selection is the ankyrin domain's job, which is what distinguishes
OspC3 from OspC1/OspC2:
[PMID:36624349 "Crystal structures of OspC3-CaM and OspC3-caspase-4 binary complexes reveal unique CaM binding to an OspC3 N-terminal domain featuring an ADP-ribosyltransferase-like fold and specific recognition of caspase-4 by an OspC3 ankryin repeat domain, respectively."]
[PMID:34671164 "The enzymatic activity was shared by OspC1 and 2, whose ankyrin-repeat domains, unlike that of OspC3, could not recognize caspase-11/4."]

### Calmodulin has two distinct relationships with OspC3

This is the point that most affects the review, and the two GO:0005516 rows mean
different things.

1. **Cofactor/activator of catalysis.** Apo-calmodulin binds the N-terminal
   domain and switches the enzyme on:
   [PMID:36624349 "Here, we identify Ca2+-free calmodulin (CaM) that binds and stimulates OspC3 ADP-riboxanase activity."]
   UniProt states this as ACTIVITY REGULATION: interaction with host calmodulin
   is *required* for arginine ADP-riboxanation of host caspases. Reactome models
   the same thing:
   [Reactome:R-HSA-9956602 "The catalytic activity of OspC3 is stimulated by its interaction with calcium-free calmodulin (CALM), which reconfigures the OspC3 catalytic pocket to facilitate NAD⁺ binding and promote stable ternary complex formation with CASP4"]
2. **Target of sequestration.** The same binding event deprives the host of
   usable calmodulin: OspC3 holds calmodulin in the Ca2+-free state so it cannot
   activate CaMKII, and interferon-induced STAT1 phosphorylation and ISG
   expression are lost
   [PMID:35568036 "This suggests a model whereby OspC recruits and sequesters CaM in the absence of Ca2+, thus preventing its downstream activation of CaMKII."].
   This arm does not need catalysis:
   [PMID:35568036 "Taken together, these results demonstrate that the C-terminal domain and ADP-riboxanase activity of OspC3, which are essential for Caspase 4 inhibition, are dispensable for its inhibition of IFN signaling and ISG expression."]

So one binding event serves as both enzyme activation and host sabotage. Both
GO:0005516 rows are therefore accepted, and `GO:0140311 protein sequestering
activity` is added as a NEW row for the second reading, as the module
`calmodulin_camkii_stat1_potentiation.yaml` recommends.

### Cell death and infection outcome

[PMID:23684308 "we discovered that Shigella infection induced acute inflammatory, caspase-4-dependent epithelial cell death, which is counteracted by the bacterial OspC3 effector"]
[PMID:23684308 "Infection of guinea pigs with a Shigella ospC3-deficient mutant resulted in enhanced inflammatory cell death and associated symptoms, correlating with decreased bacterial burdens."]
[PMID:37014865 "infection with ΔospC3 Shigella triggered significant levels of epithelial cell death as assessed by PI uptake of IFNγ-primed HeLa"]

PMID:34409271 extends the picture to mouse: OspC3 inhibits caspase-4 but, in the
mouse, not caspase-11
[PMID:34409271 "The Shigella T3SS effector OspC3 reportedly suppresses cytosolic LPS sensing by inhibiting caspase-4 but not caspase-11 activity."]

Note the 2013 paper's proposed mechanism (blocking p19/p10 heterodimerization by
inserting a conserved motif into the catalytic pocket) was superseded by the
ADP-riboxanation mechanism from 2021-2023; the phenotype it established stands.

## Evidence-code issue found

The GOA row `GO:0140740 ADP-riboxanase-[protein] activity` with evidence IDA and
reference PMID:37014865 is questionable as an IDA. The cached full text of that
paper is a genetic and cell-biological study of how IpaH9.8 and OspC3 cooperate
to block pyroptosis; it contains no ADP-riboxanation or enzyme assay, and
describes the activity only by citing earlier work
[PMID:37014865 "Shigella secrete ~30 unique effectors, including OspC3, an effector that directly posttranslationally modifies CASP4 to inhibit pyroptosis"].
The term is right for OspC3 and is established several times over by the other
rows, so the row is accepted and the evidence code is raised as a SUSPECTED
source defect (requested_change CHECK) rather than treated as grounds for
rejecting the annotation.

## Reactome rows

Three rows place OspC3 in `GO:0005829 cytosol`. Reactome models the human
pathway, so "cytosol" there means the cytosol of the infected human cell. Read on
a Shigella gene product the bare term says the bacterial cytosol, which is wrong:
OspC3 is secreted. `GO:0044164 host cell cytosol` says what Reactome means, so
the three rows are modified to it. `GO:0051701 biological process involved in
interaction with host` (from the Reactome pathway "Infection with Enterobacteria")
is true but is an ancestor of the specific symbiont-mediated terms this review
accepts, so it is marked TOO_GENERAL rather than removed.
