# femI (PA1912, Q9I2J2) — review notes

Tier-3 PseudoCAP review, and the other half of the `femA` finding from batch 4. Reviewed
immediately after `femA` so the transposition can be corrected from both sides.

## The swap, from this side

PMID:18086184 designates `PA1912-PA1911-PA1910` as FemI-FemR-FemA and lists PA1912 among
the five ECF sigmas it overexpressed. So **femI is the sigma factor** and femA is the
outer-membrane TonB-dependent transducer. The two experimental molecular-function rows from
that paper sit on the wrong genes, and — this is the part that only became visible on
reviewing both — so do the two inter-ontology inferences computed from them:

| row | femI (PA1912, sigma) | femA (PA1910, transducer) |
|---|---|---|
| `GO:0016987` sigma factor activity | IBA + IEA — **no experimental row** | **IMP** ← belongs here |
| `GO:0015344` siderophore uptake transporter activity | **IMP** ← belongs on femA | IBA only |
| `GO:2000142` reg. of transcription initiation (`GO_REF:0000108`, from `GO:0016987`) | ACCEPT — correctly derived | removed — derived from the misplaced row |
| `GO:0033214` siderophore-iron import (`GO_REF:0000108`, from `GO:0015344`) | **removed** — derived from the misplaced row | ACCEPT — correctly derived by IBA |
| `GO:0005829` cytosol | absent | NAS — belongs here |

The symmetry is exact. Each gene carries one misplaced experimental row *and* the automatic
inference built on top of it, while the row it should have carries only electronic support.
That is a stronger signature than either gene shows alone: a single mis-keyed accession
would not reproduce this pattern twice in mirror image.

`GO:0033214` is therefore `REMOVE`d here as a consequence, exactly as `GO:2000142` was on
femA — an `OVER_PROPAGATION` report at `PROBABLE` against GOA rather than a second wrong-gene
claim, because the inference pipeline behaved correctly on a wrong input. Note that femA
already carries `GO:0033214` legitimately by IBA from the receptor node, so nothing is lost
by removing femI's copy.

## The record rules out the transporter row

168 residues, and nothing but a sigma factor:

- `[file:PSEAE/femI/femI-uniprot.txt "DR   Pfam; PF04542; Sigma70_r2; 1."]` and
  `[file:PSEAE/femI/femI-uniprot.txt "DR   Pfam; PF08281; Sigma70_r4_2; 1."]` — sigma-70
  regions 2 and 4, the promoter-recognition and −35-binding modules.
- `[file:PSEAE/femI/femI-uniprot.txt "DR   InterPro; IPR036388; WH-like_DNA-bd_sf."]` — the
  winged-helix DNA-binding fold.
- `[file:PSEAE/femI/femI-uniprot.txt "DR   PANTHER; PTHR43133:SF63; RNA POLYMERASE SIGMA FACTOR FECI-RELATED; 1."]`
  — and FecI is the *E. coli* ferric-citrate ECF sigma, the paradigm for precisely this kind
  of iron-responsive cell-surface signalling system.
- `PE   3: Inferred from homology`, no transmembrane segment, no signal peptide, no barrel or
  plug domain.

A 168-residue cytoplasmic winged-helix DNA-binding protein cannot be a siderophore
transporter. The `SIMILARITY` statement placing it in the sigma-70 ECF subfamily is not
cited, because its only evidence is ARBA; the signature `DR` lines carry the argument
instead, and they are valid support for family membership under the project rules.

## Where the repoint leaves each gene

Once both requests are applied, femI gains the `GO:0016987` IMP it should always have had and
loses a transporter activity it cannot perform; femA gains the `GO:0015344` IMP and loses the
sigma activity and the cytosol statement. Both genes end up with experimental grounding for
their own function instead of for each other's. The `GO:0016987` shared claim then contains
the five sigmas the abstract names, PA1912 among them.

`GO:0015891 siderophore transport` is handled differently from `GO:0015344`, and the
distinction matters. It is **corrected**, as `MODIFY` to `GO:0034758 positive regulation of
iron ion transport`: a sigma factor that induces the uptake genes belongs to the biology of
siderophore transport, but it performs none of the transport itself, so the participation
claim is wrong rather than merely peripheral.

This paragraph first said the row was **kept** as `KEEP_AS_NON_CORE`, on the reasoning that the
role is real but not core. The PR review was right that the reasoning does not reach that
action: the sentence "FemI performs no step of siderophore transport" is the participation test
failing, and `KEEP_AS_NON_CORE` is for a claim as precise as warranted but away from the core
function, not for one that places the protein inside a process it does no work in. The same
correction is made on `fpvA` in this batch (`GO:0002049` to `GO:1900706`), and merged `foxI`
sets the direction for a Fem-type ECF sigma.

It also sharpens what the batch-4 `femA` review said — that the row is "defensible on both" —
but not in the way first written here. The row is a participation claim the transducer earns
and the sigma factor does not; it is not the same claim held at two levels of centrality, and
only reviewing both genes could establish that.

GO has no regulation-of-siderophore-transport term, which makes the replacement a trade. That
was checked against GO through OLS rather than against `cache/go/terms.csv`, which holds only
terms the corpus already uses and so says nothing about GO: a search for one returns nothing,
while "siderophore transport" returns 18 classes and "regulation of iron ion transport" returns
7, so the query can return a positive and the absence is real. `GO:0034758` therefore regulates
`GO:0006826 iron ion transport`, an ancestor of `GO:0015891`, trading siderophore specificity
for a correct relation to the gene product. `GO:1904440 positive regulation of iron ion import
across plasma membrane` was rejected: "plasma membrane" names the inner membrane in a
Gram-negative, and the uptake this sigma switches on is TonB-dependent at the outer membrane.

## A divergence in the merged corpus that the audit cannot see

Checking house style across the four merged ECF sigma factors (`PA0149`, `PA2050`, `foxI`,
`vreI`) gives a consistent pattern for every term femI shares with them, with one exception:

| term | PA0149 | PA2050 | foxI | vreI |
|---|---|---|---|---|
| `GO:0003677` DNA binding | KEEP_AS_NON_CORE | KEEP_AS_NON_CORE | KEEP_AS_NON_CORE | KEEP_AS_NON_CORE |
| `GO:0003700` DNA-binding TF activity | TOO_GENERAL | TOO_GENERAL | TOO_GENERAL | TOO_GENERAL |
| `GO:0006352` transcription initiation | ACCEPT | ACCEPT | ACCEPT | ACCEPT |
| **`GO:0006355`** reg. of transcription | **TOO_GENERAL** | **TOO_GENERAL** | **TOO_GENERAL** | **MODIFY → `GO:2000142`** |
| `GO:0016987` sigma factor activity | ACCEPT | ACCEPT | ACCEPT | ACCEPT |
| `GO:2000142` | ACCEPT | ACCEPT | ACCEPT | ACCEPT |

`vreI` is the outlier on `GO:0006355`. This review follows the 3:1 majority and the
2026-11-14 ruling, which agree: `GO:2000142` is already asserted and accepted on the gene as
its own row, so the broader term is entailed by a more specific one asserted elsewhere, which
is what `TOO_GENERAL` is for; and a `MODIFY` would need this row's own evidence for the deeper
term while also duplicating a row the gene already has.

Worth recording for two reasons. First, it is the `liuB`/`liuD` shape again — the same term
from the same kind of source read two ways across parallel reviews. Second, **the shared-claim
audit cannot detect it**: the script reads the molecular-function worklist and groups by
(term, reference) over IMP rows, and `GO:0006355` here is a biological-process term carried by
IBA and IEA. So this is a class of drift the existing check is structurally blind to, exactly
as the `GO:0009103` divergence was in the `wbpX`/`wbpY` pair. Left for a human: merged `vreI`
is not touched here.

## Curation gap, not a knowledge gap

`femR` (PA1911), the anti-sigma factor that holds FemI inactive until FemA signals, has no
folder in the corpus and no IMP molecular-function row, so it is absent from the worklist. The
Fem system will be two-thirds reviewed after this. That is a curation gap and is recorded here
rather than as a `knowledge_gaps` entry, since a curator could close it by reviewing the gene.
