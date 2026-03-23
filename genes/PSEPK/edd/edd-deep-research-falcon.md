# edd (PP_1010) in *Pseudomonas putida* KT2440

## Gene/protein identity

The KT2440 `edd` locus corresponds to UniProt Q88P43 / locus tag `PP_1010` and
encodes phosphogluconate dehydratase (EC 4.2.1.12), an IlvD/Edd-family enzyme
that converts 6-phospho-D-gluconate to 2-keto-3-deoxy-6-phosphogluconate
(KDPG). The UniProt record explicitly assigns the Entner-Doudoroff (ED)
pathway, predicts an Fe-S cofactor, and places the protein in the
IlvD/Edd family. [file:PSEPK/edd/edd-uniprot.txt, "RecName:
Full=Phosphogluconate dehydratase"; "EC=4.2.1.12"; "Pathway: Carbohydrate
metabolism; Entner-Doudoroff pathway"; "Belongs to the IlvD/Edd family"]

## Core molecular function

The clearest functional conclusion is that `edd` encodes the specific ED-pathway
dehydratase rather than a generic lyase/catalytic activity. UniProt gives the
reaction directly, and KT2440 metabolic studies use `edd (PP1010,
6-phosphogluconate dehydratase)` as the defined gene product when measuring
glucose-catabolic flux and enzyme activity. [file:PSEPK/edd/edd-uniprot.txt,
"Catalyzes the dehydration of 6-phospho-D-gluconate to
2-dehydro-3-deoxy-6-phospho-D-gluconate"] [PMID:26350459 Pseudomonas putida
KT2440 strain metabolizes glucose through a cycle formed by enzymes of the
Entner-Doudoroff, Embden-Meyerhof-Parnas, and pentose phosphate pathways, "edd
(PP1010, 6-phosphogluconate dehydratase)", "Specific (Sp) enzymatic activities
of Edd"]

An earlier KT2440 paper describes the same biochemical step in the glucose
network: 6-phosphogluconate enters the ED branch by conversion to KDPG through
Edd. [PMID:20971912 Compartmentalized Glucose Metabolism in Pseudomonas putida
Is Controlled by the PtxS Repressor, "6PG...enters the Entner-Doudoroff route,
where it is first converted into 2-keto-3-deoxy-6-phosphogluconate (KDPG) by
the Edd enzyme"]

## Pathway context in KT2440

In *P. putida* KT2440 the ED pathway is not a peripheral option; it is a major
organizing principle of glucose catabolism. Studies of central carbon
metabolism, including mutant analysis of `edd`, show that glucose is processed
through a cyclic architecture that mixes ED, pentose-phosphate, and partial EMP
reactions. [PMID:24951791 The functional structure of central carbon metabolism
in Pseudomonas putida KT2440] [PMID:26350459 Pseudomonas putida KT2440 strain
metabolizes glucose through a cycle formed by enzymes of the Entner-Doudoroff,
Embden-Meyerhof-Parnas, and pentose phosphate pathways]

This supports the GO process term `Entner-Doudoroff pathway through
6-phosphogluconate` as the right pathway annotation. Broader parent terms such
as `catalytic activity` or `hydro-lyase activity` are true but less informative
than the specific dehydratase function.

## Cofactor and localization

The UniProt entry predicts a bound [4Fe-4S] cluster and specific binding
residues, which is consistent with known IlvD/Edd-family dehydratase chemistry.
This makes `4 iron, 4 sulfur cluster binding` a plausible mechanistic
annotation, but it is secondary to the specific catalytic function in the review
hierarchy. [file:PSEPK/edd/edd-uniprot.txt, "Name=[4Fe-4S] cluster"; "Binds 1
[4Fe-4S] cluster"; "BINDING         154"; "BINDING         221"]

No direct localization experiment for PP_1010 was identified in the reviewed
KT2440 literature, but the enzyme is most plausibly cytosolic because it acts on
soluble ED intermediates within the bacterial central-carbon-metabolism network.
That makes `cytosol` reasonable to keep as a non-core localization statement.

## Physiological significance

The ED pathway is a key contributor to KT2440 physiology beyond simple glucose
catabolism. Oxidative-stress work shows that ED metabolism is essential for sugar
catabolism and contributes strongly to NADPH/redox robustness. This does not
establish a special moonlighting role for Edd, but it strengthens the case that
the ED-pathway annotation is biologically meaningful in this organism.
[PMID:23301697 The Entner-Doudoroff pathway empowers Pseudomonas putida KT2440
with a high tolerance to oxidative stress, "Glucose catabolism of Pseudomonas
putida is carried out exclusively through the Entner-Doudoroff (ED) pathway";
"ED was essential for sugar catabolism"; "required for counteracting oxidative
stress"]

## Curation takeaways

1. Accept `GO:0004456 phosphogluconate dehydratase activity` as the core MF.
2. Accept `GO:0009255 Entner-Doudoroff pathway through 6-phosphogluconate` as
   the core BP.
3. Treat `GO:0003824 catalytic activity` and `GO:0016836 hydro-lyase activity`
   as over-annotated parent terms.
4. Keep `GO:0051539 4 iron, 4 sulfur cluster binding` and `GO:0005829 cytosol`
   as plausible but non-core supporting annotations.
