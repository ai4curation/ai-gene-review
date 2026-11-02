# GO-CAM structural lint

`ai-gene-review gocam-lint` (or `just gocam-lint`) reads the cached GO-CAM
models under `gocams/<id>/<id>-src.yaml` and reports structural anomalies:
graph shapes that are impossible, redundant or ambiguous. It does not judge
whether the biology is true. Use it to start a `GoCamReview` from a short list
of suspicious places, then check each finding against the literature.

```bash
just gocam-lint 59cc772c00000000                 # one model
just gocam-lint --min-severity WARNING            # all cached models, to stdout
just gocam-lint -o reports/gocam-lint.tsv         # all models, as TSV
just gocam-lint --list-rules
just gocam-lint --no-ontology 59cc772c00000000    # graph rules only, no GO download
```

Ontology rules use the oaklib GO SQLite build (`sqlite:obo:go`, about 300 MB
compressed, downloaded on first use). The code is in
`src/ai_gene_review/gocam_lint.py`; the tests are in `tests/test_gocam_lint.py`.

Each finding has a `rule`, a `severity` (ERROR, WARNING, INFO) and, where one
fits, the `GoCamQcFlagEnum` value a reviewer would record.

## Rules

| Rule | Needs GO | What it finds | QC flag |
|---|---|---|---|
| `compartment_crossing` | yes | A direct causal edge between activities on opposite sides of a membrane, with no transport or secretion step (see below) | DIRECT_VS_INDIRECT_CAUSAL |
| `transcription_direct_edge` | yes | A DNA-binding transcription factor *directly* regulates a non-transcriptional activity. WARNING when the model names the target as the TF's input gene, INFO otherwise | DIRECT_VS_INDIRECT_CAUSAL |
| `receptor_ligand_input` | yes | A receptor activity `has input` the gene product of an activity upstream of it (the ligand belongs on the causal edge) | HAS_INPUT_MISUSE |
| `generic_mf` | yes | MF is a grouping term (`kinase activity`, `catalytic activity`, `binding`, ...) | GENERIC_MF |
| `binding_mf` | yes | MF is a binding term (`protein binding` WARNING, other binding INFO) | BINDING_AS_FUNCTION |
| `same_gene_chain` | no | Activities of one gene product chained by causal edges. WARNING when the MF repeats in one location, INFO when the MFs differ (activation states, distinct steps) | |
| `duplicate_activity` | no | Same gene product and MF in more than one node. WARNING when the context is identical | |
| `opposite_sign_fanout` | no | One activity activates one node of a gene and inhibits another node of the same gene | |
| `contradictory_edges` | no | The same pair of activities joined by both a positive and a negative edge | |
| `self_loop` | no | An activity regulates itself | |
| `duplicate_edge` | no | The same edge asserted several times (usually merged evidence; INFO) | |
| `edge_evidence_copied` | no | A causal edge cites exactly the references of the upstream `enabled_by` | |
| `orphan_activity` | no | An activity with no causal or metabolite-flow link, in a multi-activity model | ORPHAN_ACTIVITY |
| `disconnected_components` | no | Several components. WARNING when two share at least half their genes (a switch or choice, or cloned variant paths) | |
| `missing_evidence` | no | A causal edge with no evidence | MISSING_EVIDENCE |
| `missing_location` | no | An activity with no `occurs_in` | MISSING_LOCATION |
| `small_model` | no | Two or fewer activities | |
| `no_narrative` | no | No curator comment beyond automated changes | |
| `near_duplicate_models` | no | Corpus rule: two models whose (gene, MF) activity sets overlap with Jaccard ≥ 0.6 | |

Connectivity rules count metabolite flow as well as causal edges: in pathway
models, A `has output` X and B `has input` X links A to B. Gene-centric
models, where every activity has the same enabler (MGI/SGD imports), are
exempt from the orphan and component rules.

## Compartment topology

A direct edge (`directly positively/negatively regulates`, `directly provides
input for`, `removes input for`, `constitutively upstream of`) asserts a single
step. Each `occurs_in` term is mapped to the topological spaces it touches:

| Code | Space |
|---|---|
| C | cytosolic space (cytosol and nucleus, joined through nuclear pores) |
| E | extracellular |
| P | periplasm |
| L | lumen of the secretory and endocytic system (topologically outside) |
| M | mitochondrial matrix |
| I | mitochondrial intermembrane space |
| X | peroxisomal matrix |
| S, T | plastid stroma, thylakoid lumen |

A membrane touches both of its sides (plasma membrane: C, E, P). An organelle
root term touches its outside and its insides (ER: C, L). `cytoplasm` touches
every intracellular space. A term inherits the faces of its most specific
anchor through is_a/part_of. Leaflet terms resolve to one side, so
`cytoplasmic side of plasma membrane` is C. Generic intracellular anchors are
ignored when a more specific anchor matches. Host-cell terms and terms with no
anchor (`membrane`, `cell`, complexes) are skipped. The anchor table and its
partial order live in the code, and an integration test checks them against
the current GO build.

Two activities whose face sets intersect can be linked directly. Otherwise
the least severe pairing of faces decides the severity:

* **ERROR**: interior (C, M, I, X, S, T) against exterior (E, P). Example:
  CASP1 in the cytosol "directly positively regulates" IL1B cytokine activity
  in the extracellular region, which skips GSDMD-pore secretion.
* **WARNING**: two separated interior spaces, e.g. cytosol and mitochondrial
  matrix with no import step. Metabolite flow between cytosol and the
  intermembrane space is INFO, because porins make the outer membrane
  permeable to small molecules.
* **INFO**: lumen and exterior (Golgi processing followed by secretion), which
  is topologically continuous.

## Corpus results (November 2026)

The run over 2,037 cached models (`reports/gocam-lint.tsv`) gave 10,021
findings in 1,924 models; 757 models have at least one ERROR or WARNING.

| Severity | Rule | Count |
|---|---|---|
| ERROR | compartment_crossing | 6 |
| WARNING | missing_evidence | 1836 |
| WARNING | generic_mf | 521 |
| WARNING | orphan_activity | 322 |
| WARNING | duplicate_activity | 284 |
| WARNING | binding_mf | 56 |
| WARNING | compartment_crossing | 32 |
| WARNING | same_gene_chain | 30 |
| WARNING | opposite_sign_fanout | 24 |
| WARNING | disconnected_components | 10 |
| WARNING | receptor_ligand_input | 9 |
| WARNING | contradictory_edges | 4 |
| WARNING | transcription_direct_edge | 2 |
| WARNING | self_loop | 2 |

All six ERRORs are plausible missing steps: CASP1 to extracellular IL1B
(`59cc772c00000000`), TGFB1 directly regulating nuclear USP44
(`6348a65d00002174`), two transcriptional repressors directly regulating
secreted proteins (`568b0f9600000284`, `632cf60a00000169`), and MPO in the
nucleus directly activating proteases in neutrophil extracellular traps
(`68fac5ed00000028`).

The rules were checked against manual reviews of problematic models (see the
`GoCamReview` files for `671ae02600002832`, `66b5638000001589`,
`635b1e3e00001811`, `65a1f4f800002884` and the `62b4ffe3000044xx/54xx`
calmodulin set). `opposite_sign_fanout` catches the duplicated eIF2alpha node
of the integrated stress response model. `same_gene_chain` catches the NLRP3
chain in the inflammasome model. `disconnected_components` and
`duplicate_activity` catch the parallel NBN repair-choice chains, and
`near_duplicate_models` catches the four calmodulin models split from one
paper.

## Known limits

* Molecules carry no location in `gocam-py`, so a crossing reached through a
  `has input` molecule is not checked.
* `cytoplasm` is ambiguous, so it never produces a crossing with lumenal
  spaces.
* Some proposed rules need text or ontology knowledge not yet wired in:
  checking an edge's sign against its cited paper, checking reaction
  participants against Rhea, checking an MF against the gene's known
  compartments, and checking that the model's title is reached by its graph.
