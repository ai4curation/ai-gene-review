---
title: "Propagation Audit: Animal Terms on Unicellular Holozoans"
autolink_gene_symbols: false
---
# Propagation Audit: Animal Terms on Unicellular Holozoans

[← back to Origins of Animal Multicellularity](../ORIGINS_OF_MULTICELLULARITY.md)

**Bottom line:** almost every GO annotation on choanoflagellate, *Capsaspora*
and sponge proteins is propagated from animals, so we checked where that
propagation goes wrong. Across the 11 project reviews there are 36 propagated
rows (TreeGrafter `GO_REF:0000118` and the UniProt multi-method merge
`GO_REF:0000120`). Reviewers accepted 24, kept 4 as non-core and left 1
undecided, and down-graded 7. All 7 down-grades are TreeGrafter rows, and
they come from three different mechanisms:

- **An animal-tissue term placed on a node that includes choanoflagellates.**
  PAINT put four process IBDs on the LATS node PTN002390470. One of them,
  *regulation of organ growth*, is meaningless in a unicellular organism.
- **TreeGrafter grafting into the wrong family.** This is the main
  TreeGrafter failure: two Hippo-pathway proteins landed outside their
  orthologous clade.
  - *Capsaspora* Warts was placed with the citron/ROCK kinases.
  - The *S. rosetta* protein knocked out as *yorkie* was placed with the
    MAGI-related scaffolds.
- **A lineage-specific term on a broad node.** A fungal cell-wall term,
  *mannan biosynthetic process*, sits on a choanoflagellate
  mannosyltransferase.

Most propagated terms were sound, including *hippo signaling* on the
*Capsaspora* kinases and coactivator. The problems are specific and fixable at
named nodes.

Data: [`propagation_audit.py`](propagation_audit.py) regenerates
[`propagation_audit_rows.tsv`](propagation_audit_rows.tsv) (every propagated
row with the reviewer's action) and
[`propagation_audit_spread.tsv`](propagation_audit_spread.tsv) (how often each
down-graded term occurs on unicellular holozoan proteins in GOA). Counts are
from 2026-10-01.

## Scope

| Organism | Reviews | Propagated rows | Down-graded |
|---|---|---:|---:|
| *Salpingoeca rosetta* (choanoflagellate) | rosetteless, jumble, couscous, hippo, warts, yorkie | 17 | 4 |
| *Capsaspora owczarzaki* (filasterean) | coHpo, coWts, coYki | 13 | 2 |
| *Oscarella pearsei* (sponge) | VIN1, TLN | 6 | 1 |

None of these organisms is a PANTHER reference genome, so none of the
proteins gets IBA rows. Their tree-based annotations all come from
TreeGrafter, which grafts the protein onto a reference tree and copies the
terms on the graft node. The one reference genome among unicellular
holozoans is *Monosiga brevicollis*, which does get IBA rows. It appears below
because it inherits the same LATS-node terms.

## Case 1: organ growth, apoptosis and G1/S on choanoflagellate Warts

**What happened.** The S. rosetta Warts kinase (F2U943) is correctly placed in
the LATS family (PTHR24356:SF418). It received seven TreeGrafter rows from the
*M. brevicollis* Warts leaf PTN001220369, whose parent PTN002390470 carries
four PAINT IBDs (from `interpro/panther/PTHR24356/PTHR24356-paint.tsv`):

| IBD term | Seeds | Date | Review action on S. rosetta warts |
|---|---|---|---|
| `GO:0035329` hippo signaling | fly wts, mouse Lats1/Lats2, human LATS1/LATS2 | 2020-08-09 | ACCEPT |
| `GO:0046620` regulation of organ growth | mouse Lats2 only | 2022-04-15 | **REMOVE** |
| `GO:0043065` positive regulation of apoptotic process | fly wts only | 2017-02-28 | MARK_AS_OVER_ANNOTATED |
| `GO:0000082` G1/S transition of mitotic cell cycle | mouse Lats2, human LATS2 | 2017-02-28 | MARK_AS_OVER_ANNOTATED |

The same four terms reach *M. brevicollis* LATS (A9UVF9) as IBA rows. They
also reach the reference-tree leaf for Drosophila wts, where they are fine.

**Why it is a problem.**
- **Organ growth.** No choanoflagellate has organs. GO's taxon constraints on
  `GO:0046620` do not exclude choanoflagellates, so nothing downstream catches
  this.
- **Apoptosis.** This rests on one fly gene. We found no evidence of apoptosis
  in choanoflagellates.
- **G1/S transition.** This rests on mammalian LATS2. In *S. rosetta*,
  knocking out warts makes rosettes larger and slows growth, which is not a
  G1/S-checkpoint result. Choanoflagellates do have a cell cycle, so the term
  is not impossible; it is unsupported for this protein.
- **Hippo signaling** fits the *Capsaspora* evidence and was accepted.

**Spread.** Regulation of organ growth occurs on exactly two unicellular
holozoan proteins, the two choanoflagellate Warts kinases, and on none in
Filasterea or Ichthyosporea. The other two terms are more widespread in
unicellular holozoans, but on different nodes. Unicellular organisms divide
and some may die by regulated pathways, so those other rows are not taxon
errors as such.

**Recommendation for PAINT (PTHR24356).**
- Move the `GO:0046620` IBD from PTN002390470 to the metazoan descendant node,
  or add an exception there for the choanoflagellate leaves.
- Consider doing the same for `GO:0043065`, which has one seed.
- Separately, GO could consider a taxon constraint excluding unicellular
  lineages from organ-level growth terms.

## Case 2: Capsaspora Warts grafted into the citron/ROCK family

**What happened.** Gene targeting identifies coWts (A0A0D2VGR4, CAOG_00619) as
*Capsaspora* Warts, and knocking it out sends coYki into the nucleus
(PMID:38517944). Its sequence has a LATS-type MOB-binding region and an AGC
kinase domain. TreeGrafter nevertheless placed it in **PTHR22988:SF71
"CITRON RHO-INTERACTING KINASE"**, part of the "MYOTONIC DYSTROPHY S/T
KINASE-RELATED" family that contains ROCK, MRCK and citron. Human LATS1/2 are
in PTHR24356. The graft node PTN001122925 supplied `cytoskeleton` and
`actomyosin structure organization`. The review marked `cytoskeleton`
over-annotated and removed `actomyosin structure organization`. It also added
`hippo signaling` by IMP, which coWts never received because it missed the
LATS node.

**Why the Drosophila ortholog escapes.** UniProt's PANTHER cross-reference
also classes Drosophila wts (Q9VA38) in PTHR22988 (SF76). But fly wts is a
leaf of the PANTHER reference tree and gets its IBA rows from the LATS node
PTN002390470 in PTHR24356, including `hippo signaling`, with no
cytoskeleton/actomyosin rows. Our reading is that the family HMMs and the
reference trees disagree about Warts kinases. Reference proteomes follow the
tree, while non-reference proteomes such as *Capsaspora* follow the HMM call
and graft into the wrong family. This is an inference from the classifications
and annotation rows, not from re-running TreeGrafter.

**Spread.** `GO:0031032` actomyosin structure organization is on 9
*Capsaspora* proteins, 4 of them from PTN001122925, and on 7 ichthyosporean
proteins. Several are probably genuine ROCK/MRCK/citron kinases, for which the
term is reasonable; we have not reviewed them.

**Recommendation for PANTHER.** Check whether the PTHR22988 subfamily HMMs
(SF71, SF76) out-score the PTHR24356 LATS subfamilies for Warts/LATS
sequences. If so, the LATS HMM or the family boundary needs attention. A quick
test: rescore coWts, fly wts and *S. rosetta* Warts (F2U943, which classifies
correctly) against both families.

## Case 3: S. rosetta yorkie grafted into the MAGI-related family

**What happened.** The 2025 knockout study names PTSG_06057 (F2UDK1) as the
*S. rosetta* Yorkie homolog. This is stated in version 2 of the preprint
behind PMID:41037400. TreeGrafter placed F2UDK1 in **PTHR10316:SF68
"MEMBRANE ASSOCIATED GUANYLATE KINASE-RELATED"**, on graft node PTN002569196,
whose members are ecdysozoan genes. That gave it `cytoplasm` and
`signal transduction`. Both terms are plausible for a Yorkie protein, so the
review kept them as non-core, while flagging that they were reached by the
wrong route.

PANTHER places a different *S. rosetta* WW protein, F2U5K0 (PTSG_03848), in the
YAP1 family subfamily PTHR17616:SF8, alongside Drosophila yki (Q45VV3) and
*Capsaspora* coYki (A0A0D2WY30). That conflicts with the experimental
literature. Our motif scan
([yorkie-bioinformatics](../../genes/SALRS/yorkie/yorkie-bioinformatics/RESULTS.md))
finds:
- F2UDK1 has the four Warts phosphorylation motifs the literature reports for
  srYki, and no recognizable TEAD-binding motif.
- Full-length alignment scores put F2UDK1 closer to YAP1, Yki and coYki than
  F2U5K0 is. Much of that similarity is in the WW domains.

**Status: unresolved.** Either PANTHER's family call or the literature's
ortholog call is wrong. A phylogeny of the holozoan WW-domain proteins would
settle it. Until then, neither protein should receive YAP1-family process
terms on the strength of this audit.

## Case 4: fungal mannan biosynthesis on a choanoflagellate mannosyltransferase

**What happened.** Couscous (F2UJ78) is a predicted MNN2-type
alpha-1,2-mannosyltransferase needed for rosette development (PMID:30556809).
Its TreeGrafter node PTN001270341 gave it the following rows:

| Term | Review action | Reason |
|---|---|---|
| alpha-1,2-mannosyltransferase activity | ACCEPT | Plausible family-level activity |
| Golgi apparatus | UNDECIDED | Tagged Couscous was "clearly not localized to the Golgi" |
| `GO:0046354` mannan biosynthetic process | **REMOVE** | Defined in GO as the main hemicellulose of softwood; in fungi, Mnn2 builds cell-wall mannan. Nothing suggests choanoflagellates make mannan. |

**Spread.** `GO:0046354` is on 4 choanoflagellate proteins and 1
ichthyosporean protein. **Recommendation:** restrict the mannan IBD in the
MNN2 family to the fungal node.

## Case 5: talin cell-cell adhesion (minor)

The talin family node PTN001072690 gave sponge TLN `cell-cell adhesion`. Talin
works at integrin-matrix adhesions, and nothing links the sponge protein to
cell-cell contacts, so the review changed it to `cell-matrix adhesion`. This is
a family-level node term, not a taxon problem; `GO:0098609` occurs widely in
unicellular holozoans through other families.

## Extension: IBA nodes of the human toolkit genes (Track B)

For each existing human review re-checked in Track B (CDH1, ABL1, MYC,
NOTCH1, TP53), we took the PANTHER nodes behind its IBA rows and asked QuickGO
whether those nodes' terms reach proteins of Choanoflagellata, Filasterea or
Ichthyosporea, by IBA or by TreeGrafter IEA. Details and the query results are
in each gene's notes (`genes/human/<GENE>/<GENE>-notes.md`, section
"Premetazoan origin").

| Gene | Node(s) | Reaches unicellular holozoans? | Assessment |
|---|---|---|---|
| CDH1 | PTN000616280 (PAINT taxon **Bilateria**) | **Yes: 30 TreeGrafter IEA rows**. Ten terms each on three *S. rosetta* cadherins: F2UD23, F2UFV3 and F2USU1 | **Case 6, below** |
| CDH1 | PTN008601603 | Yes: 5 IBA rows on *M. brevicollis* A9V8Y4 | Case 6, below |
| TP53 | PTN000893833 | Yes: 7 IBA terms each on *M. brevicollis* A9UZX3 and A9V4M3 | Mostly DNA-binding and transcription terms; `regulation of apoptotic process` is an untested extrapolation |
| TP53 | PTN000154790 | 3 TreeGrafter rows on *Capsaspora* A0A0D2X0F0 (DNA binding, TF activity, regulation of transcription); the apoptosis term itself is not transferred | Plausible from domain conservation (PMID:31861340) |
| MYC | PTN001691821 | Yes: 4 IBA rows on *M. brevicollis* Myc (A9V5B4) | **Supported**: the transcription-factor and nuclear terms match the experiments on choanoflagellate Myc (PMID:21571926) |
| ABL1 | PTN002521457 | Yes: tyrosine kinase activity and plasma membrane on 59 *M. brevicollis* kinases | The MF is fine; plasma membrane is a localization default on cytoplasmic kinases |
| NOTCH1 | PTN001933897 (Eumetazoa), PTN002911625 | No | Expected for the animal-innovation control |

## Case 6: junction and catenin terms on choanoflagellate cadherins

**What happened.** PAINT records node PTN000616280 in the cadherin family
PTHR24027 at `taxon:33213` (Bilateria) in
`interpro/panther/PTHR24027/PTHR24027-paint.tsv`. Its IBDs, seeded by mouse,
rat, human and zebrafish classical cadherins, include adherens junction,
catenin complex, cell-cell junction assembly, calcium-dependent cell-cell
adhesion and cell morphogenesis. TreeGrafter nonetheless grafts three
*S. rosetta* cadherins (subfamily PTHR24027:SF422) onto that node. Each of
the three receives 10 IEA rows, 30 rows in all:

| Protein | Domains (Pfam) |
|---|---|
| F2UD23 | cadherin repeats, SH2 |
| F2UFV3 | cadherin repeats, laminin G |
| F2USU1 | cadherin repeats, tyrosine phosphatase |

Separately, node PTN008601603 gives *M. brevicollis* A9V8Y4 five IBA rows:
beta-catenin binding, catenin complex, cadherin binding, cell migration and
cell-cell adhesion.

**Why it is a problem.** None of the four proteins has PF01049, the
cytoplasmic domain through which classical cadherins bind beta-catenin. A
UniProt census finds 0 PF01049 proteins in choanoflagellates, filastereans
and ichthyosporeans, against 23,575 in animals (CDH1-bioinformatics/).
Choanoflagellates lack classical cadherins (PMID:22837400, PMID:27189570), and
*S. rosetta* colonies have no adherens-junction-like structures
(PMID:22837400). So the catenin and junction terms describe a protein
complex these proteins cannot form.

**Why this matters for TreeGrafter.** This is the clearest case so far of
TreeGrafter grafting onto a node that PAINT itself restricts to a clade the
query is not in. Either the graft ignores the node's taxon, or the node label
is wrong. Both readings point to a fix in the PTHR24027 tree.

**Recommendation for PANTHER.** Check how the *S. rosetta* SF422 cadherins
come to graft onto a Bilateria node. Graft them onto a pre-bilaterian
cadherin node, or block terms from PTN000616280 for non-bilaterian queries.

## What held up (negative controls)

- **coYki:** all 3 of its TreeGrafter rows were accepted. Capsaspora and
  heterologous data support each one: transcription coactivator activity,
  hippo signaling, and positive regulation of transcription by RNA
  polymerase II.
- **Sponge TLN:** integrin binding, focal adhesion, cytoplasm and plasma
  membrane were accepted at the family level.
- **Kinases:** generic kinase activity, ATP binding and cytoplasm on coHpo,
  hippo and coWts were all accepted.

So signalling and molecular-function terms on conserved premetazoan pathways
transfer well. The failures are at the edges:
- tissue- and organ-level process terms placed too deep;
- family boundaries for divergent paralogs (Warts vs ROCK, Yorkie vs MAGI);
- lineage-specific metabolic terms.

## Caveats

- Eleven proteins is a small sample, chosen because they have experimental
  literature. It shows that each failure mode exists, not how often it occurs.
- We read the PAINT node contents from the cached PTHR24356 slice and from
  QuickGO WITH/FROM fields. We did not re-run TreeGrafter or open the PANTHER
  trees directly, except through the cached slice.
- The other non-LATS members of PTN001122925 and PTN001270341 in unicellular
  holozoans were not reviewed. Some of those rows may be correct.
- The Track B extension only checked the nodes behind each human gene's own
  IBA rows. For CDH1 and TP53 the unicellular targets were identified from
  QuickGO, not reviewed as gene reviews.
