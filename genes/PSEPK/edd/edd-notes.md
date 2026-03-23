# edd notes

- UniProt Q88P43 identifies `edd` / `PP_1010` in *Pseudomonas putida* KT2440 as
  phosphogluconate dehydratase (EC 4.2.1.12) of the IlvD/Edd family and states
  that it catalyzes dehydration of 6-phospho-D-gluconate to
  2-dehydro-3-deoxy-6-phospho-D-gluconate. [file:PSEPK/edd/edd-uniprot.txt,
  "RecName: Full=Phosphogluconate dehydratase"; "Catalyzes the dehydration of
  6-phospho-D-gluconate to 2-dehydro-3-deoxy-6-phospho-D-gluconate"; "Belongs to
  the IlvD/Edd family"]

- UniProt also predicts a bound [4Fe-4S] cluster with specific ligand residues,
  supporting the cofactor-binding annotation as mechanistically plausible rather
  than the primary biological function. [file:PSEPK/edd/edd-uniprot.txt,
  "Name=[4Fe-4S] cluster"; "Binds 1 [4Fe-4S] cluster"; "BINDING         154";
  "BINDING         221"]

- A KT2440 glucose-metabolism review/experimental study describes 6PG entering
  the ED route by conversion to KDPG through Edd and includes `edd (PP1010,
  6-phosphogluconate dehydratase)` among the glucose-catabolic mutants and
  enzyme assays. [PMID:26350459 Pseudomonas putida KT2440 strain metabolizes
  glucose through a cycle formed by enzymes of the Entner-Doudoroff,
  Embden-Meyerhof-Parnas, and pentose phosphate pathways, "6PG...is first
  converted into 2-keto-3-deoxy-6-phosphogluconate (KDPG) by the Edd enzyme";
  "edd (PP1010, 6-phosphogluconate dehydratase)"; "Specific (Sp) enzymatic
  activities of Edd"]

- Earlier KT2440 work on compartmentalized glucose metabolism likewise describes
  Edd as the enzyme that converts 6PG to KDPG in the ED branch of the network.
  [PMID:20971912 Compartmentalized Glucose Metabolism in Pseudomonas putida Is
  Controlled by the PtxS Repressor, "6PG...enters the Entner-Doudoroff route,
  where it is first converted into 2-keto-3-deoxy-6-phosphogluconate (KDPG) by
  the Edd enzyme"]

- KT2440 relies strongly on ED catabolism rather than a canonical EMP glycolytic
  route; pathway-level studies connect this organization to redox balance and
  oxidative-stress tolerance. This supports retaining the ED-process annotation,
  but it does not justify broad extra pathway over-annotation beyond the specific
  ED-through-6PG term already present. [PMID:23301697 The Entner-Doudoroff
  pathway empowers Pseudomonas putida KT2440 with a high tolerance to oxidative
  stress, "Glucose catabolism of Pseudomonas putida is carried out exclusively
  through the Entner-Doudoroff (ED) pathway"; "ED was essential for sugar
  catabolism"; "required for counteracting oxidative stress"]

- Working curation judgement:
  - `GO:0004456 phosphogluconate dehydratase activity` should be core/accepted.
  - `GO:0009255 Entner-Doudoroff pathway through 6-phosphogluconate` should be
    core/accepted.
  - `GO:0003824 catalytic activity` and `GO:0016836 hydro-lyase activity` are
    true but redundant parent terms and should not be treated as core.
  - `GO:0005829 cytosol` and `GO:0051539 4 iron, 4 sulfur cluster binding` are
    reasonable non-core supporting annotations.
