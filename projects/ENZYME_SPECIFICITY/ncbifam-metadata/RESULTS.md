# NCBIfam release-table check: GO terms that contradict the model (2026-11-23)

The [cutoff-check sweep](../cutoff-check/sweep/RESULTS.md) turned up six NCBIfam models
whose GO term names a sister reaction rather than the model's own. One example is the
formate-dependent PurT models, which carry PurN's 10-formyltetrahydrofolate term. This
page checks the whole release table for that class of error. The output is a change list
for NCBIfam curators, [FEEDBACK.md](FEEDBACK.md).

PGAP annotates RefSeq proteins with these GO terms, so a wrong term on a model reaches
every protein it hits. The release table's `n_refseq_protein_hits` column measures
that reach, and the lists rank by it.

## Method

[`check_release_table.py`](check_release_table.py) reads NCBIfam release 20.0
(`hmm_PGAP.tsv`, 18950 models, 8409 with GO terms). Its steps:

1. **Pair up terms and ECs.** Each model's GO terms are paired with its EC numbers. A
   term's reaction is its EC cross-references from QuickGO. 2847 pairs have EC numbers
   on both sides.
2. **Classify each pair** as `consistent` when an EC matches, allowing for a partial
   model EC such as `2.1.2.-`. Otherwise it is `sister_reaction` (same EC subclass) or
   `other_reaction`.
3. **Place each non-matching pair in GO**, using the semsql GO database that
   `just validate` uses. The placement is relative to the GO terms that cross-reference
   the model's own ECs:
   - `broader`: an ancestor of those terms;
   - `narrower`: a descendant of them;
   - `broad_class`: a class term, such as serine-type endopeptidase activity, that covers
     the model's EC subclass;
   - `no_go_for_model_ec`: GO has no term for the model's EC;
   - `unrelated`: none of these.

   A partial model EC such as `7.1.1.-` matches the GO terms of every EC under it.
   The `broad_class` heuristic is applied before the hierarchy is consulted.
4. **Triage by hand.** Every `unrelated`, `narrower` and `no_go_for_model_ec` pair is
   triaged in [`triage.yaml`](triage.yaml), 231 pairs in all, from the model's product
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
     `source: sweep`.

   It refuses to write the report otherwise. FEEDBACK.md then shows two kinds of
   replacement:
   - `proposed`: a curator's replacement, where one was checked;
   - the machine-derived GO terms for the model's own EC, which are unreviewed.

| step | pairs |
|---|---|
| EC on both sides | 2847 |
| consistent | 2584 |
| not consistent | 263 |
| placed `broader` or `broad_class` (true, less specific; not hand-triaged) | 32 |
| placed `narrower`, triaged | 9 |
| `no_go_for_model_ec`, triaged | 57 |
| `unrelated`, triaged | 165 |

The release table also carries 112 obsolete GO terms (model, term pairs), listed in
[CANDIDATES.md](CANDIDATES.md). Every GO id in the table resolves in QuickGO.

## Triage result

| verdict | entries | models | RefSeq hits |
|---|---|---|---|
| WRONG_REACTION | 64 | 95 | 1189591 |
| WRONG_COFACTOR | 11 | 12 | 153187 |
| EC_SUSPECT | 4 | 17 | 194686 |
| CHECK | 32 | 36 | 1119506 |
| ACCEPTABLE | 23 | 66 | 1030292 |

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

## What this does not establish

- **Names, not literature.** Verdicts are judged from product names and GO definitions,
  not from literature or the models' seed proteins. Each row is a proposal for NCBIfam
  curators.
- **Not every pair was triaged by hand.** The 32 `broader` and `broad_class` pairs and
  the 2584 `consistent` pairs were not. A `consistent` pair can still hide an error, as
  PurT's NF006766.0 does: its wrong term falls under its partial EC `2.1.2.-`. A model
  with no EC number cannot be checked this way at all. The four such models in the
  triage come from the sweep; a name-versus-term check over the rest would need
  curation.
- **Partial ECs give weaker placements.** A partial model EC such as `4.1.-.-` matches
  every GO term under it, so its placement says little. FEEDBACK.md computes the GO
  terms for each model's own EC from the model itself. It does not list them for a
  partial EC, which would offer a whole subclass, or when a complete EC has more than
  ten. It says `(model has no EC)` for the sweep models without one. Where it shows
  `(none in GO)`, GO has no term for the model's complete EC (bacterial Tgt, EC
  2.4.2.29, is one example). There the fix may be a new GO term rather than a removal.
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
`~/.data/oaklib/go.db`, which `just validate` fetches.
