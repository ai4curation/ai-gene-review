# NCBIfam release-table check: GO terms that contradict the model (2026-11-23)

The [cutoff-check sweep](../cutoff-check/sweep/RESULTS.md) turned up six NCBIfam models
whose GO term names a sister reaction rather than the model's own. One example is the
formate-dependent PurT models, which carry PurN's 10-formyltetrahydrofolate term. This
page checks every (model, GO term) pair in the release table that has EC numbers on
both sides for that class of error. The output is a change list
for NCBIfam curators, [FEEDBACK.md](FEEDBACK.md).

PGAP annotates RefSeq proteins with these GO terms, so a wrong term on a model reaches
every protein it hits. The release table's `n_refseq_protein_hits` column measures
that reach, and the lists rank by it.

## Method

[`check_release_table.py`](check_release_table.py) reads NCBIfam release 20.0
(`hmm_PGAP.tsv`, 18950 models, 8409 with GO terms). Its steps:

1. **Pair up terms and ECs.** Each model's GO terms are paired with its EC numbers. A
   term's reaction is its complete EC cross-references from QuickGO. A term with none
   reaches an EC through Rhea when its Rhea cross-references map, by Rhea's own
   `rhea2ec.tsv`, to exactly one complete EC and it carries no EC of its own (see
   [Rhea](#reaching-ecs-through-rhea)). 2919 pairs have EC numbers on both sides, 72 of
   them through Rhea.
2. **Classify each pair** as `consistent` when an EC matches, allowing for a partial
   model EC such as `2.1.2.-`. Otherwise it is `sister_reaction` (same EC subclass) or
   `other_reaction`.
3. **Place each non-matching pair in GO**, using the semsql GO database that
   `just validate` uses. The placement is relative to the GO terms that cross-reference
   the model's own ECs (by EC cross-reference or, as above, through Rhea):
   - `broader`: an ancestor of those terms;
   - `narrower`: a descendant of them;
   - `broad_class`: a class term, such as serine-type endopeptidase activity, that covers
     the model's EC subclass;
   - `no_go_for_model_ec`: no GO term reaches the model's EC;
   - `unrelated`: none of these.

   A partial model EC such as `7.1.1.-` matches the GO terms of every EC under it.
   The `broad_class` heuristic is applied before the hierarchy is consulted.
4. **Triage by hand.** Every `unrelated`, `narrower` and `no_go_for_model_ec` pair is
   triaged in [`triage.yaml`](triage.yaml), 235 pairs in all, from the model's product
   name and the term's definition. Four models the EC comparison cannot catch are added
   from the sweep: TIGR02095.1, TIGR02491.1 and TIGR01142.1 (no EC) and NF006766.0
   (partial EC).
5. **Check the triage.** [`render_feedback.py`](render_feedback.py) checks the triage
   before writing anything:
   - every pair in the three triaged buckets has an entry;
   - every verdict is a known one;
   - every triaged model carries its term and has a RefSeq hit count in the release
     table;
   - every suggested replacement term exists in GO and is not obsolete;
   - every triaged pair is a flagged pair, unless its entry is one of the four marked
     `source: sweep`;
   - every class-term lead (below) is triaged exactly once.

   It refuses to write the report otherwise. FEEDBACK.md then shows two kinds of
   replacement:
   - `proposed`: a curator's replacement, where one was checked;
   - the machine-derived GO terms for the model's own EC, which are unreviewed.

| step | pairs |
|---|---|
| (model, GO term) pairs in the release table | 18691 |
| skipped: model has no EC number | 8790 |
| skipped, of the rest: biological process or cellular component term | 4095 |
| skipped: class term whose partial EC contains the model's EC (true, broader) | 691 |
| not compared: class term whose partial EC lies inside the model's partial EC (narrower; class-term triage) | 3 |
| skipped: class term that is a GO ancestor of a term for the model's EC | 4 |
| not compared: class term unrelated by EC class or GO ancestry (class-term triage) | 81 |
| skipped: molecular function term whose Rhea reactions map to several ECs (Rhea route not used) | 45 |
| skipped: molecular function term that reaches no EC, directly or through Rhea | 2063 |
| EC on both sides | 2919 |
| of which through Rhea | 72 |
| consistent | 2652 |
| not consistent | 267 |
| placed `broader` or `broad_class` (true, less specific; not hand-triaged) | 32 |
| placed `narrower`, triaged | 9 |
| `no_go_for_model_ec`, triaged | 49 |
| `unrelated`, triaged | 177 |

Separately, 112 of these pairs carry an obsolete GO term, listed in
[CANDIDATES.md](CANDIDATES.md); each also falls in one of the rows above. Every GO id in the table resolves in QuickGO.

## Triage result

| verdict | entries | models | RefSeq hits |
|---|---|---|---|
| WRONG_REACTION | 65 | 97 | 1202530 |
| WRONG_COFACTOR | 11 | 12 | 153187 |
| EC_SUSPECT | 4 | 17 | 194686 |
| CHECK | 33 | 37 | 1124881 |
| ACCEPTABLE | 24 | 67 | 1030908 |

RefSeq hits are summed over the distinct models in each verdict, read from the release
table, so the models without an EC number count too. A model with pairs in two verdicts
counts in both, so the rows are not additive.

### Wrong reaction

Most wrong-reaction entries share one shape: a model built for one member of a family
carries the term for another member's reaction.

- **Family homologues:**
  - glycogen synthase GlgA (ADP-glucose) carries the UDP-glucose term;
  - adenosine deaminase carries adenine deaminase;
  - V-type ATPase subunits carry the P-type proton-exporting transporter term;
  - phytoene synthase CrtB and squalene synthase HpnC carry geranylgeranyl diphosphate
    synthase;
  - FolX carries FolB's dihydroneopterin aldolase;
  - VanA-type D-alanine--D-lactate ligases carry D-alanine--D-alanine ligase;
  - uridine phosphorylase carries purine-nucleoside phosphorylase.
- **Pathway neighbours:**
  - PurK carries PurE's AIR carboxylase;
  - MnmA carries MnmC's methyltransferase;
  - PncB carries NadC's quinolinate phosphoribosyltransferase;
  - PhaA carries PhaB's acetoacetyl-CoA reductase.
- **Unrelated names:**
  - CdaA (diadenylate cyclase) carries adenylate cyclase;
  - QueF carries archaeosine tRNA-guanine transglycosylase;
  - GMP reductase carries IMP dehydrogenase;
  - a D-lyxose isomerase carries diguanylate cyclase.

### Other verdicts

- **Wrong cofactor.** These entries keep the reaction but change the partner, for
  example:
  - formate dehydrogenase-N (quinone) carries the NAD+ and cytochrome c-553 formate
    dehydrogenase terms;
  - HemN (radical SAM) carries the O2-dependent coproporphyrinogen oxidase term;
  - the degradative, NAD-dependent HMG-CoA reductase carries the NADPH term.
- **EC suspect.** Here the error looks like it is in the EC number:
  - 14 complex I subunit models carry EC 1.6.5.9, the non-electrogenic NDH-2 reaction,
    while their GO term is complex I's (EC 7.1.1.2). Three more complex I models (EC
    `7.1.1.-`) show the mirror image: the NDH-2 term itself, filed as wrong reaction.
    TIGR01972.1 (EC `1.6.5.-`, the class complex I belonged to before EC 7.1.1.2)
    carries the complex I term and is acceptable;
  - EntD, the phosphopantetheinyl transferase, carries EC 6.3.2.14, the
    2,3-dihydroxybenzoate--serine ligase reaction.
- **Check.** These need family knowledge rather than names. Examples are whether
  NAD+ synthase models are ammonia- or glutamine-dependent, NAD versus NADP prephenate
  dehydrogenase, and FabH versus the elongating KAS term.
- **Acceptable.** These are true as stated: bifunctional models whose EC list is
  incomplete, dual-substrate names, partial reactions, and EC reclassifications.

## Reaching ECs through Rhea

GO now cross-references many reaction terms only to Rhea. Adenosine deaminase activity
(GO:0004000) is one: it carries `RHEA:24408` and no EC, so the first version of this
check could not compare it and placed the adenosine deaminase models
`no_go_for_model_ec`. The check now maps a term's Rhea cross-references to EC numbers
with Rhea's [`rhea2ec.tsv`](https://ftp.expasy.org/databases/rhea/tsv/rhea2ec.tsv),
using `rhea-directions.tsv` because GO may cite any of a reaction's four directional ids.
A term counts only when its Rhea reactions reach exactly one complete EC and it carries
no EC cross-reference of its own, partial or complete. Generic terms are excluded that way: ATP hydrolysis activity
(nine ECs through one Rhea reaction), GTPase activity (seven) and the class term for
NAD(P)-dependent CH-OH oxidoreductases (partial EC 1.1.1.-). Without that rule, every
helicase, chaperone and transporter carrying them reads as a mismatch.

The route makes 72 more pairs comparable. 68 agree with the model's EC. The four that
do not are triaged: the Kce term for 3-keto-5-aminohexanoate cleavage (EC 2.3.1.247)
on two acetyl-CoA transferase models with their own ECs (wrong reaction), NadN's NAD+
diphosphatase, a second activity its model description names (acceptable), and YfiH's
adenosine deaminase, which its model comment calls only possible (check). The same lookup adds Rhea-linked terms as candidates for
the model's own EC, so the adenosine deaminase models now list GO:0004000. The run
records the SHA-256 of both Rhea tables in `release_table_check.yaml`.

## Class-term leads

779 pairs join a model to a class term that carries only a partial EC, such as
oxidoreductase activity (EC 1.-.-.-):

- in 691 the term's EC class contains the model's EC, so the term is true but broad;
- in 4 the term's partial EC does not contain the model's EC, but the term is a GO
  ancestor of a term for that EC, so it is broad too. EC classes are compared before GO
  ancestry. For a partial model EC the ancestry test is weaker, since it matches any GO
  term under that EC class. `release_table_check.yaml` records each of the 4;
- in 3 the term's EC class lies inside the model's partial EC;
- in 81 neither EC class contains the other and the term is not a GO ancestor of a term
  for the model's EC. For 35 of them the ancestry test could not run, because no GO term
  reaches the model's EC.

The 84 in the last two groups are triaged in `triage.yaml` under `class_term_triage`:

| verdict | entries | pairs |
|---|---|---|
| WRONG_REACTION | 25 | 31 |
| WRONG_COFACTOR | 2 | 2 |
| CHECK | 14 | 16 |
| ACCEPTABLE | 21 | 35 |

FEEDBACK.md lists the non-acceptable ones in a section of their own. Most wrong-class
terms follow the protein family's fold rather than the reaction:

- glycoside hydrolase terms on the branching enzyme GlgB and on lytic murein
  transglycosylases, which do not hydrolyse;
- a C-N hydrolase term on PhnM, which hydrolyses a phosphoanhydride;
- aminoacyl-tRNA ligase on EpmA, the lysyl-tRNA synthetase paralog that modifies
  elongation factor P;
- sulfatase terms on OpgB and a lipid A phosphoethanolamine transferase, from the
  alkaline-phosphatase/sulfatase fold.

The acceptable ones are mostly artifacts of EC cross-referencing:

- endopeptidase activity is cross-referenced only to EC 3.4.99.- but covers all of EC 3.4,
  so it looks wrong on MepK, GPR and the proteasome;
- transporters, decarboxylases and Na+-NQR moved to EC 7, and DAHP synthase moved from
  4.1.2 to 2.5.1, so their older class terms no longer contain the model's EC;
- some models carry a second activity their EC list omits.

The CHECK entries need family knowledge. The largest is TIGR01879.1 (93458 RefSeq hits),
a hydantoinase/carbamoylase family amidase with a linear-amidine hydrolase term that is
right only for its allantoate amidohydrolase members.

## What this does not establish

- **Names, not literature.** Verdicts are judged from product names and GO definitions,
  not from literature or the models' seed proteins. Each row is a proposal for NCBIfam
  curators.
- **Not every pair was triaged by hand.** The 32 `broader` and `broad_class` pairs and
  the 2652 `consistent` pairs were not. A `consistent` pair can still hide an error, as
  PurT's NF006766.0 does: its wrong term falls under its partial EC `2.1.2.-`. A model
  with no EC number cannot be checked this way at all. The four such models in the
  triage come from the sweep; a name-versus-term check over the rest would need
  curation.
- **Partial ECs give weaker placements.** A partial model EC such as `4.1.-.-` matches
  every GO term under it, so its placement says little. FEEDBACK.md computes the GO
  terms for each model's own EC from the model itself. It does not list them for a
  partial EC, which would offer a whole subclass, or when a complete EC has more than
  ten. It says `(model has no EC)` for the sweep models without one.
- **Function terms that reach no EC are never compared.** 2063 pairs join a model that
  has an EC number to a molecular function term that reaches no complete EC, directly or
  through Rhea, and 45 more to a term whose Rhea reactions map to several ECs, which the
  route does not use. What they are was not characterised, and a sister-reaction error on such
  a term would be missed. The 779 class terms that carry only a partial EC are handled
  separately (see [Class-term leads](#class-term-leads)).
- **The Rhea route is deliberately narrow.** A term counts only when all its Rhea
  reactions map to one complete EC. Rhea's EC table is many-to-many and generic
  reactions map widely, so a term whose Rhea reaches several ECs is not compared: ATP
  hydrolysis activity's single Rhea reaction maps to nine ECs. Synonym cross-references
  are not used either: GO:0004000's related synonym "adenosine aminohydrolase activity"
  carries EC:3.5.4.4, but a narrow synonym's EC (GO:0046961's "ATP synthase activity",
  EC 7.1.2.2) is not the term's own reaction. Where FEEDBACK.md says "no GO term reaches
  EC …", GO may still have a term for the reaction, so a curator should look for one by
  name before requesting it.
- **Class-term verdicts are names-level too.** Most class-term errors follow the
  protein family's fold, and the CHECK entries need the family's literature.
- **Reach beyond PGAP is unchecked.** Whether these GO terms also reach UniProt through
  InterPro2GO depends on which models InterPro integrates and how InterPro maps them.
  That was not checked here.
- **This is not a gene-review change.** No review in this repository changes. GOA rows
  on our genes that trace to these models are flagged in the reviews themselves, as
  glgA and nrdG already are.

## Reproduce

```
uv run python projects/ENZYME_SPECIFICITY/ncbifam-metadata/check_release_table.py   # about 1 minute cold, 20 s warm
uv run python projects/ENZYME_SPECIFICITY/ncbifam-metadata/render_feedback.py
```

The first script needs the NCBIfam release table (fetched by the cutoff check into
`.cache/ncbifam/`), QuickGO on first run, and the semsql GO database at
`~/.data/oaklib/go.db`, which `just validate` fetches. It downloads Rhea's
`rhea2ec.tsv` and `rhea-directions.tsv` into `.cache/rhea/` when they are missing.
