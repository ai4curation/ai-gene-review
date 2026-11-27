# phnA (PA1001, P09785) — review notes

Tier-3 PseudoCAP review. `phnA` is the last unreviewed member of the `GO:0004049` /
PMID:2153661 shared claim; `phnB`, `trpE` and `trpG` are merged and all ACCEPT the term.

## The gene: the second, pyocyanin-specific anthranilate synthase

A Swiss-Prot **reviewed** entry (PHNA_PSEAE, 530 aa), unusually well curated for this
corpus — `EC=4.1.3.27`, a curated `FUNCTION` carrying `ECO:0000269|PubMed:2153661`,
nine `FT BINDING` features, and NCBIfam `TIGR00565 trpE_proteo`.

*P. aeruginosa* has **two** anthranilate synthase gene pairs, and PMID:2153661 is the paper
that separated them:

`[PMID:2153661 "One anthranilate synthase enzyme participates in tryptophan synthesis; its genes are designated trpE and trpG."]`
`[PMID:2153661 "The other anthranilate synthase enzyme, encoded by phnA and phnB, participates in the synthesis of pyocyanin, the characteristic phenazine pigment of the organism."]`

PhnA is the large alpha (catalytic) subunit:
`[file:PSEAE/phnA/phnA-uniprot.txt "Heterotetramer consisting of two non-identical subunits: a beta subunit (PhnB) and a large alpha subunit (PhnA)."]`

The curated `FUNCTION` sets out the division of labour: PhnB supplies the glutamine
amidotransferase half-reaction generating ammonia, and the second step — ammonia plus
chorismate to anthranilate — is `catalyzed by the large alpha subunit of AS (PhnA)`. So
`enables GO:0004049` is right for *this* subunit. The merged `phnB` review noted that
`contributes_to` would be arguable for the beta subunit and still settled on ACCEPT; the two
reviews are consistent, and the asymmetry is real rather than a drift.

## `GO:0000162` L-tryptophan biosynthetic process is an over-annotation

The IBA comes from `PTN002599563`, whose donors include E. coli and *M. tuberculosis* TrpE
and plant, yeast and *S. pombe* members — a tryptophan-pathway anthranilate synthase clade.
The node cannot separate the two *P. aeruginosa* paralogs, and `trpE` is itself a member of
this same shared claim.

This is **not** a paralog-confusion claim, and it would be wrong to frame it as one: the
paper's title is about the *interchangeability* of the two enzymes, and the capability is
real in both directions:

- `[PMID:2153661 "The cloned phnA phnB gene pair complements trpE and trpE(G) mutants of Escherichia coli."]`
- a `trpE` deletion reverts to prototrophy at 10⁻⁵–10⁻⁶, and
  `[PMID:2153661 "revertants is not feedback inhibited by tryptophan, suggesting that it arises from PhnAB."]`
- conversely `[PMID:2153661 "the trpE trpG gene products are capable of providing some anthranilate for pyocyanin synthesis"]`

So PhnAB *can* make anthranilate for tryptophan. What settles the annotation is whether it
*does*, and two curated results say it does not:

- `[file:PSEAE/phnA/phnA-uniprot.txt "Double phnA-phnB deletions are tryptophan prototrophs; they make less PQS"]`
  — removing both genes leaves tryptophan synthesis intact (`ECO:0000269|PubMed:23449919`).
- Deleting `trpE` instead gives `[PMID:2153661 "This resulted in tryptophan auxotrophy"]` —
  PhnAB does not cover for it at wild-type expression.

The reason it cannot is on the record:
`[file:PSEAE/phnA/phnA-uniprot.txt "PhnAB is not feedback inhibited by tryptophan."]` — PhnAB
sits outside tryptophan's regulatory circuit, which is exactly why it serves a separate,
signal-molecule pathway and why only derepressed revertants press it into tryptophan service.

`MARK_AS_OVER_ANNOTATED` rather than `REMOVE`: the enzyme makes the same metabolite and can
substitute when derepressed, so the term is not false, but it states a latent capability as a
physiological role. Not `KEEP_AS_NON_CORE` either — that would assert a real, if peripheral,
role in tryptophan biosynthesis, and the double-deletion prototrophy is evidence against
exactly that.

## `GO:0002047` phenazine biosynthetic process is accepted, with the mechanism flagged

Accepted. The paper asserts participation directly (quoted above), and the genetics are
strong: `[file:PSEAE/phnA/phnA-uniprot.txt "Disruption of phnA alone yields 22-34% pyocyanine."]`,
while the double `trpE`-`phnA` disruption `does not make pyocyanine`.

One nuance is recorded rather than acted on. The curated `FUNCTION` describes the route as
anthranilate →
`[file:PSEAE/phnA/phnA-uniprot.txt "a precursor for Pseudomonas quinolone signal"]` → PQS,
which then induces the pyocyanin biosynthetic genes. If that induction step is the whole
story, PhnA's contribution to phenazine synthesis is regulatory rather than biosynthetic, and
a regulation term would fit better than `involved_in`. But the 1990 curator read the full
text, the paper states participation in as many words, and anthranilate may also be consumed
chemically; the project rule against overruling an experimental annotation from an
abstract-only cache applies squarely. Left as `ACCEPT` with a `suggested_questions` entry.

## Not raised as a source defect

Nothing here is a defect. The `GO:0000162` row is a PAINT judgement about a node, so it is
argued in the row and, since the term is not false, no upstream correction is requested. The
`GO:0004049` rows are correct. The over-annotation is the kind of thing a reviewer records
rather than files.
