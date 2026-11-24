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

## The problem: PANTHER places an experimentally confirmed DHOase in the allantoinase clade

All three of this gene's IBA rows come from **PANTHER:PTN000909483**, and PAINT's own records
for PTHR43668 show that node is the *allantoinase* node, explicitly separated from the DHOase
branch above it:

| node | term | evidence | negated |
|---|---|---|---|
| PTN000182407 | GO:0004151 dihydroorotase activity | IBD | false |
| PTN000182407 | GO:0004038 allantoinase activity | IRD | **true** |
| PTN000182407 | GO:0000256 allantoin catabolic process | IRD | **true** |
| PTN000182407 | GO:0006145 purine nucleobase catabolic process | IRD | **true** |
| PTN000909483 | GO:0004038 allantoinase activity | IBD | false |
| PTN000909483 | GO:0006145 purine nucleobase catabolic process | IBD | false |

(`interpro/panther/PTHR43668/PTHR43668-paint.tsv`.)

The curator therefore did the hard part correctly: the DHOase function is placed at
PTN000182407, seeded by UniProtKB:O66990 — *Aquifex aeolicus* PyrC, whose EC 3.5.2.3
assignment carries experimental evidence (`ECO:0000269|PubMed:15381710`) — and the allantoinase
function is confined to PTN000909483 by three explicit IRD rows at the ancestor.

The dispute is not with that judgement but with **where PANTHER puts this leaf**. PA5541 is an
experimentally confirmed DHOase that complements an *E. coli* `pyrC` mutant, so functionally it
belongs on the PTN000182407 side of exactly the boundary PAINT drew; the tree instead places it
under PTN000909483 and it inherits the allantoinase assertions the ancestor was explicitly
pruned of. PANTHER assigns it to subfamily SF4, which the family review describes as "Bacterial
AllB".

Two further checks:

- **The organism has no annotated allantoinase.** A UniProt query for EC 3.5.2.5 restricted to
  *P. aeruginosa* PAO1 (taxid 208964) returns zero entries, so `GO:0004038` on PA5541 is the
  only allantoinase claim in the proteome, with no pathway around it.
- **The organism's other DHOase is annotated as one.** The same query for EC 3.5.2.3 returns
  P72170, `pyrC` — PA3527, the constitutive enzyme of the pair.

This is the second member exception on the same family's `GO:0004038` term assessment. The
first, *P. putida* pyrC', is the catalytically **inactive** DHOase-like ATCase subunit; PA5541
is the complementary case, an **active** DHOase. Both are Pseudomonas pyrC-family proteins that
the allantoinase subfamily has absorbed.

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
