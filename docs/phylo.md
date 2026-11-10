# Phylogenetic extracts: the tree and alignment behind an IBA

An IBA row in a GOA file carries a PANTHER node id and a list of seed genes. The PAINT
curator who placed the term on that node worked from more: the family tree with its
speciation, duplication and horizontal-transfer events, the experimental annotations
painted on its leaves, and the family alignment. A review that argues with the
placement needs the same view. Two derived files provide it.

| File | Written by | Covers |
|---|---|---|
| `genes/<org>/<GENE>/<GENE>-phylo.yaml` | `just phylo <org> <GENE>` | every IBA row of one gene |
| `interpro/panther/<PTHR>/<PTHR>-tree-nodes.yaml` | `just phylo-family <PTHR>` | every node of a family's PAINT slice |

Both are derived files, like `GENE-goa.tsv`: do not edit them, regenerate them.

## Source data

`just fetch-panther-release` downloads three things once into the git-ignored
`.cache/panther_release/PANTHER19.0.sqlite` (about 1.3 GB, a few minutes):

- PANTHER's TreeGrafter data bundle `PANTHER19.0_data.tar.gz`: every family tree
  (`Tree_MSF/<PTHR>.tree`, Newick with events, taxa and branch lengths), every family
  alignment (`Tree_MSF/<PTHR>.AN.fasta`) and the node table that maps tree nodes to
  persistent `PTN` ids and subfamilies.
- `PANTHER19.0_fasta.tgz`: the full-length sequence of every leaf.
- UniProt's Arabidopsis reference proteome with ordered locus names, because GOA writes
  Arabidopsis seeds as `AGI_LocusCode:AT5G16440`, which the trees do not carry.

The live PANTHER `treeinfo` and `familymsa` services return the same data one family at a
time but time out on many families, so nothing here calls them. The extract records the
release and the bundle's `Last-Modified` date.

## What the gene extract says

For each family tree the gene's rows sit in:

- **`target`** is the gene's leaf, with its subfamily, its full length and how many of its
  residues are in the family alignment. `same_as_uniprot_file` says whether PANTHER's
  sequence equals the one in `GENE-uniprot.txt`; when it is false, positions below are in
  PANTHER's sequence, not the current UniProt one.
- **`lineage`** lists every node from the family root down to the gene: event, taxon,
  branch length and the number of leaves below. A speciation node has a `taxon`. A
  duplication or transfer node has `after` (the nearest speciation above it) and `before`
  (the first speciation on each branch below it).
- **`nodes`** describes each PAINT node the rows cite: how many leaves, species and
  subfamilies it covers, and the branches directly below it.
- **`seeds`** lists every seed the rows cite. `relation` is read from the event where
  the seed and the gene join: `ORTHOLOG` at a speciation, `PARALOG` at a duplication,
  `XENOLOG` at a horizontal transfer. `duplications_between` and `transfers_between` count
  the events on the way: an ortholog with no duplication between is one-to-one, while one
  with duplications between is an ortholog of a whole group of later paralogs. `identity` is over the alignment columns both proteins occupy;
  `covers_target` and `covers_seed` are those columns as a share of each full-length
  protein. `seed_regions_without_target` and `target_regions_without_seed` are stretches
  of 30 or more aligned residues that the other protein lacks, in the protein's own
  numbering.
- **`rows`** has one entry per IBA row:
  - `steps`, `duplications_on_path`, `transfers_on_path`, `path_length`: the path from the
    PAINT node down to the gene.
  - `seed_mrca`, `seed_mrca_steps_below_node`, `seed_branches`: where the seeds' own common
    ancestor is. When it is the PAINT node, the seeds bracket the node. When it is below
    the node, all the seeds sit in one branch and the curator placed the term above the
    evidence.
  - `target_in_seed_clade`: whether the gene lies inside the clade the seeds span.
  - `orthologs`, `one_to_one_orthologs`, `paralogs`, `xenologs`: how the seeds other than
    the gene itself are related to it.
  - `self_seed`: the gene's own experimental annotation is among the seeds.
  - `paint_losses_on_path`: IRD or IKR rows for the same term between the node and the
    gene, from the family's PAINT slice. A non-empty list means the cached IBA is stale.
  - `summary`: the same facts as one line of prose, for quoting.
- **`residue_sites`** appears when the family review curates residue sites. Each site's
  anchor positions are carried through the alignment to the gene: `RETAINED`,
  `SUBSTITUTED` or `ABSENT`. A position is not carried over when the anchor's PANTHER
  sequence does not hold the expected residue (`ANCHOR_MISMATCH`), when the anchor
  residue lies in a stretch PANTHER left out of the alignment (`NOT_ALIGNED`), or when it
  cannot be tied to one column (`AMBIGUOUS`).

Rows that cannot be placed (a node the release does not know, or no node at all) are
listed under `unplaced_rows` with the reason.

### Numbering

PANTHER's alignment rows hold only the residues in the family model's match columns;
inserted stretches are dropped. Counting along a row therefore does not give a position
in the protein. The extract lays each row back onto the full-length sequence and reports
positions in the protein's own numbering. Where a residue could sit on either side of a
dropped stretch, the position is marked uncertain (`target_position_uncertain`), and an
anchor residue in that state is not used at all.

## Using it in a review

A `REMOVE` or `MARK_AS_OVER_ANNOTATED` on an IBA row argues with a node placement. Before
making one:

1. Run `just phylo <org> <GENE>` (and `just paint-losses <org> <GENE>`).
2. Read the row. The questions it answers:
   - Is the gene inside the clade the seeds span, or did PAINT extend the term past them?
   - Is any seed a one-to-one ortholog, or are they all paralogs across a duplication?
   - How many duplications lie between the node and the gene?
   - How similar is the gene to the nearest seed, and does either lack a region the
     other has?
   - Has PAINT already removed the term on this path?
3. Quote the row's `summary`, or one sentence of it, in `supported_by`:

```yaml
    supported_by:
    - reference_id: file:human/CIRBP/CIRBP-phylo.yaml
      supporting_text: >-
        GO:0000398 (mRNA splicing, via spliceosome): PAINT node PTN000391532 is a
        speciation node at Eukaryota, with 373 leaves in 84 species and 21 subfamilies.
```

Start the quote at the term id: the check looks for the row's own term in it. The quote
is checked verbatim against the file like any other `file:` quote, so it must come from
the current extract. If the tree does not support the verdict, reconsider the
verdict rather than leaving the quote out.

A residue argument ("lacks the catalytic residues") goes in
`propagation_review.residue_claims`; `residue_sites` gives the positions to put there, with
`method: MSA` and `alignment_release: "PANTHER 19.0"`.

In a family review, a node assessment of `TOO_DEEP`, `WRONG_NODE`, `NEEDS_PRUNING`,
`LOSS_CONTRADICTED` or `LOSS_TOO_BROAD` quotes the node's `summary` from
`<PTHR>-tree-nodes.yaml` in the same way.

## Checks

| Check | Where | Fires when |
|---|---|---|
| `missing_tree_evidence` | `just validate` (warning) | an IBA row is overruled without a quote from the gene's own extract |
| `tree_evidence_other_row` | `just validate` (warning) | the extract is quoted, but no quote names the row's term |
| `missing_residue_evidence` | `just validate` (warning) | a propagated row is overruled as `PSEUDO_OR_SUBACTIVITY_LOSS` with neither `residue_claims` nor `residue_claims_not_applicable` |
| `NODE_TREE_EVIDENCE` | `just validate-families` (UNRESOLVED) | a node assessment disputes a placement without quoting a tree listing |

All four are advisory: they mark verdicts made without the tree, not verdicts that are
wrong. `projects/IBA_REVIEW/tree_evidence.py` joins every reviewed IBA row with its tree
facts and lists the rows where the two pull apart
(see [the IBA project](https://github.com/ai4curation/ai-gene-review/blob/main/projects/IBA_REVIEW.md)).

## Limits

- The tree is PANTHER's reconciliation, which can be wrong. A horizontal-transfer node
  says one of its branches was transferred, not which one, so transfers on a path are
  counted rather than interpreted.
- `ORTHOLOG` and `PARALOG` are read from one event. Two proteins joined at a speciation
  can still have many duplications between them; `duplications_between` says so.
- Identity and coverage are over the family model's columns. A domain the family model
  does not cover is invisible to both.
- Sequences are those of the PANTHER 19.0 build. Check `same_as_uniprot_file` before
  citing a position.
- The gene extract describes the seeds of the cached GOA row, which is a snapshot. PAINT
  may have changed the seed list since: on about one row in seven the family's current
  PAINT slice lists different seeds. `<PTHR>-tree-nodes.yaml` describes the seeds of the
  slice, so compare the two when a verdict turns on a single seed.
- Genes outside the PANTHER reference proteomes are not leaves, so they have no
  placement; their rows are reported with the node description only.
