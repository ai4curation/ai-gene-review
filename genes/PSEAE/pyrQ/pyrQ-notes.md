# pyrQ (PA5541, Q9HT33) review notes

## What the gene is

PA5541 is one of **three** dihydroorotase-like (DHOase-like) sequences in *P. aeruginosa*
PAO1. Brichta et al. settle which is which
[PMID:15278241 "Pseudomonas aeruginosa PAO1 was shown to contain three pyrC sequences. Two of
these genes, designated pyrC (PA3527) and pyrC2 (PA5541), encode polypeptides with
dihydroorotase (DHOase) activity, while the third, pyrC' (PA0401), encodes a DHOase-like
polypeptide that lacks DHOase activity, but is necessary for the structure and function of
ATCase."]. So PA5541 is *pyrC2*, an active DHOase; the gene name `pyrQ` on the UniProt entry
comes from the EMBL submission (`GN Name=pyrQ {ECO:0000313|EMBL:AAG08926.1}`) and is not a
name used in that paper.

Two lines of evidence in the same paper make the activity claim an activity claim rather than
a similarity claim:

- Heterologous complementation: [PMID:15278241 "Both pyrC and pyrC2 were cloned and
  complemented an Escherichia coli pyrC mutant."]
- Genetics in the native organism: single mutants are prototrophic, the double mutant is not
  [PMID:15278241 "A pyrC, pyrC2 double mutant was also constructed, and this strain had an
  absolute requirement for pyrimidines."].

The two are redundant and differentially expressed — *pyrC2* is silent unless *pyrC* is gone
[PMID:15278241 "While pyrC was found to be constitutively expressed, pyrC2 was expressed only
in the pyrC mutant background."] — which is why neither single mutant is auxotrophic and why
the abstract calls this "the first report of a true DHOase mutant in P. aeruginosa".

## The problem: an experimentally confirmed DHOase outside the sub-clade PAINT pruned

All three of this gene's IBA rows come from **PANTHER:PTN000909483**. The PAINT rows for
PTHR43668 are:

| node | term | evidence | negated | with/from |
|---|---|---|---|---|
| PTN000909483 | GO:0004038 allantoinase activity | IBD | false | four allantoinases |
| PTN000909483 | GO:0000256 allantoin catabolic process | IBD | false | DAL1 |
| PTN000909483 | GO:0006145 purine nucleobase catabolic process | IBD | false | ALN, AlnA |
| PTN000182407 | GO:0004151 dihydroorotase activity | IBD | false | O66990 |
| PTN000182407 | GO:0004038 allantoinase activity | IRD | **true** | PTN000909483 |
| PTN000182407 | GO:0000256 allantoin catabolic process | IRD | **true** | PTN000909483 |
| PTN000182407 | GO:0006145 purine nucleobase catabolic process | IRD | **true** | PTN000909483 |

(`interpro/panther/PTHR43668/PTHR43668-paint.tsv`.)

**Read the with/from column carefully — the direction is the opposite of what it looks like.**
For an IRD or IKR row, the with/from field holds the **ancestral gain node**, not a descendant:
`src/ai_gene_review/etl/panther_paint.py` documents `seeds` as "experimental seeds for IBD; the
ancestral node for IRD/IKR", and `loss_nodes_by_ancestor` maps an IRD at `PTNa` naming `PTNb` to
`{'PTNb': {'PTNa'}}`. So **PTN000909483 is the ancestor and PTN000182407 is a loss node beneath
it**, not the other way round. The internal tell is that an IRD at an ancestor would be inert: a
loss row only stops an ancestral IBD from descending, so it has to sit below the gain it
overrides.

What PAINT actually did, then, is the more interesting story: it asserted allantoinase at the
family node from four genuine allantoinases, then recognised a bacterial sub-clade that had
switched chemistry, pruned all three allantoinase terms there, and asserted `GO:0004151` in their
place from *Aquifex aeolicus* PyrC (O66990, whose EC 3.5.2.3 assignment carries
`ECO:0000269|PubMed:15381710`).

**PA5541 is the kind of member that sub-clade was made for, and it is not in it.** Its leaf is
`PTN002462798`, whose lineage runs
`PTN005175582 → PTN001702525 → PTN000909483 → PTN000182426 → PTN000182433 → PTN002462789 →
PTN002462798` — through the allantoinase gain node, and not through `PTN000182407`. Two
confirmations that this is the real position rather than a cached-GOA artefact:

- `uv run python -m ai_gene_review.validation.gene_paint_losses PSEAE pyrQ` reports **"No IRD or
  IKR loss on this gene's lineage"**, so no loss withdraws either IBA.
- The gene carries no `GO:0004151` IBA, which it would receive if its leaf were under
  `PTN000182407`.

This matters for what is asked of PAINT. The fix is **not** a re-rooting of the leaf: it is an
**added loss (`ADD_IRD`) on pyrQ's branch**, extending to `PTN002462798` the pruning already done
at `PTN000182407`. That is now encoded in the family review's node assessments as
`paint_action: ADD_IRD` with `target_node_id: PANTHER:PTN002462798`, on `GO:0004038` and on
`GO:0006145` separately — PAINT prunes per annotation, so each term needs its own request — and
`just export-paint-change-requests` emits both rather than leaving the ask in prose.

**The target has to be the leaf, not a clade above it** — and the reason differs by term, because
the two IBDs at `PTN000909483` have different seeds. `PTN002462789`, pyrQ's parent, holds 34
leaves, one of which is *E. coli* AllB (P77671).

- For **`GO:0004038`**, P77671 is among that IBD's own seeds
  (`AT4G04955|S000001466|P77671|Q5B4C7`), so a loss at the parent would strip the term from a
  member that helped establish it.
- For **`GO:0006145`**, P77671 is *not* a seed — that IBD rests only on `AT4G04955` and `Q5B4C7`,
  both from organisms with urate oxidase. The reason is different and arguably stronger: pruning
  at the parent would decide, for AllB's branch, whether *E. coli* — which has no urate oxidase —
  retains a purine-to-allantoin route. That is precisely the taxonomic question the node
  assessment says it is **not** settling today, so the loss cannot be placed where it would
  pre-judge it.

Either way the leaf is a derivation rather than a conservative choice.

Whether pyrQ represents a second, independent acquisition of dihydroorotase activity inside the
allantoinase clade, or whether PANTHER's tree simply places it badly, is not settled here and
does not need to be: the requested change is the same either way.

Two further checks:

- **The organism has no annotated allantoinase.** A UniProt query for EC 3.5.2.5 restricted to
  *P. aeruginosa* PAO1 (taxid 208964) returns zero entries, so `GO:0004038` on PA5541 is the
  only allantoinase claim in the proteome, with no pathway around it.
- **The organism's other DHOase is annotated as one.** The same query for EC 3.5.2.3 returns
  P72170, `pyrC` — PA3527, the constitutive enzyme of the pair.

This is the second member exception on the same family's `GO:0004038` term assessment, and it is
made in this PR rather than deferred: `just validate-families` raises a hard `CONFLICT` when a
family scopes a term over a gene whose review removes it, so the two have to change together. The
first exception, *P. putida* pyrC', is the catalytically **inactive** DHOase-like ATCase subunit;
PA5541 is the complementary case, an **active** DHOase. Both are Pseudomonas pyrC-family proteins
that the allantoinase subfamily has absorbed.

## The IEA chain

OLS confirms `GO:0004151` sits under `GO:0016812` → `GO:0016810` → `GO:0016787`, so all three
IEA rows are ancestors of the IMP-supported term. They are not all the same case, because the
2026-11-14 ruling makes the test *this row's own evidence*:

- `GO:0016787` (IPR006680, Amidohydro-rel) and `GO:0016810` (IPR011059,
  Metal-dep_hydrolase_composite) rest on superfamily signatures that identify a metal-dependent
  amidohydrolase and nothing narrower. Their own evidence stops at the class term →
  `TOO_GENERAL`.
- `GO:0016812` rests in part on **IPR002195, `Dihydroorotase_CS`** — a dihydroorotase-specific
  conserved site, which the UniProt record also matches as `PROSITE; PS00483;
  DIHYDROOROTASE_2`. That row's own evidence does reach the specific reaction → `MODIFY` to
  `GO:0004151`.

## The process term

`GO:0006221` pyrimidine nucleotide biosynthetic process is `MODIFY` to **`GO:0044205` 'de novo'
UMP biosynthetic process**, following the call the repo already made on the sibling enzyme
(`genes/PSEPK/pyrC`, which marks `GO:0006221` TOO_GENERAL and keeps `GO:0044205`; *P. putida*
PyrC carries it in GOA). The row's own evidence reaches the specific pathway: complementation of
an *E. coli* `pyrC` mutant is complementation of a de novo defect, and an absolute pyrimidine
requirement is the phenotype of a cell that can no longer make pyrimidines de novo but can still
salvage them — whereas pyrimidine nucleotide biosynthesis in general would also be satisfied by
salvage.

Unlike *P. putida* PyrC, Q9HT33 is an unreviewed entry with **no `CC PATHWAY` line**, so the de
novo assignment here is an inference from those two genetic results rather than a transcription
from the record, and the review says so.

## What is not claimed

The `CC FUNCTION`, `CC COFACTOR` (Zn) and `CC SIMILARITY` lines on Q9HT33 are all
`ECO:0000256|ARBA:` — unvetted predictions, not usable as support. `PE 3: Inferred from
homology` likewise says the record itself rests on prediction, and the activity claim here
comes from the paper, not the record. The Zn cofactor is plausible for a class I DHOase but is
not asserted in this review: nothing experimental in *P. aeruginosa* establishes it, and the
sequence features section of the entry carries no `FT BINDING` rows.

Brichta et al. is abstract-only in the cache (`full_text_available: false`); everything quoted
above is from the abstract, which states the locus assignments, the complementation and the
double-mutant phenotype explicitly, so no part of the review depends on unread text.
