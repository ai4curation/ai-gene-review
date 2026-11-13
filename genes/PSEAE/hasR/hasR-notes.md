# hasR (PA3408, Q9HYJ7) review notes

## Review session 2026-11-13 (PseudoCAP tier 3, shared-claim group hasR/phuR)

Fetched with `just fetch-gene PSEAE hasR`. No deep-research provider file was generated.
PMID:10658665 is abstract-only in the cache, but its abstract carries the phenotypes, the
complementation and the fractionation, so the haem rows are well grounded:
[PMID:10658665 "A deltahasR mutant also exhibited decreased utilization of haem and haemoglobin,
and a deltaphuR deltahasR double mutant was virtually unable to take up either compound."] and
[PMID:10658665 "Both the PhuR and HasR proteins were detected in the outer-membrane fraction of
P. aeruginosa grown in low-iron media."]

### The finding: siderophore terms on a haem receptor

Three rows claim siderophore transport for a haem receptor -- GO:0015344 and GO:0044718 by IBA, and
GO:0033214 by logical inference from them. All trace to **PTN004738955**. Checked in the PANTHER
tree with `projects/PSEUDOCAP/panther_tree.py` on 2026-11-13:

- the node is the **LUCA root of PTHR30069**: 149 leaves across 18 subfamilies;
- its five seeds are siderophore or colicin receptors in five *other* subfamilies -- Q9HVC0 (SF42),
  Q9HWM5 (SF37), Q9I527 ferric enterobactin receptor PirA (SF8), Q05098 ferric enterobactin
  receptor (SF51), P17315 colicin I receptor (SF53);
- hasR is in **SF41, "Heme uptake outer membrane receptor HasR"**, and phuR in SF29,
  "Heme_hemoglobin uptake outer membrane receptor".

The seeds are not the problem. Two of them, PA4675 and PA4156, were reviewed by this project in
tier 2 and their own siderophore rows were accepted as SOUND on their mutant phenotypes. The
problem is depth: what the node supports is the shared TonB-dependent outer-membrane mechanism, not
the substrate, which varies by subfamily.

Relocation cannot fix it, and this was tested rather than assumed: the smallest clade containing
all five seeds is PTN002824128 (145 leaves), which also contains SF29 and SF41. So no child node
holds the siderophore receptors alone, and the remedy has to be generalising the node terms or
blocking them in the haem subfamilies. Recorded once here as a CONFIRMED GO_CENTRAL defect, with
phuR cross-referencing it -- one upstream request, not two.

### Annotation decisions

- ACCEPT: GO:0015232 (IEA, IMP), GO:0015886 (IEA, IMP), GO:0009279 (IBA, IEA), GO:0020037 (IDA).
- MODIFY: both GO:0019867 rows to GO:0009279 cell outer membrane.
- TOO_GENERAL: GO:0022857 (GO:0015232 is_a it, checked in QuickGO).
- KEEP_AS_NON_CORE: GO:0055085, because GO:0015886 haem transport is *not* a descendant of it
  (checked 2026-11-13), so refining would drop the transmembrane claim -- the same structural case
  the betT1 and PA5291 reviews handled this way. Also GO:0007166 and GO:0038023, the signalling
  rows: the has system is a cell-surface signalling system, but these rest on similarity.
- REMOVE: GO:0015344, GO:0044718, GO:0033214.

On GO:0020037 heme binding (IDA, same paper): the abstract describes *hasA*, not hasR, as the
haem-binding protein, and we hold abstract only. Per the project rule that is not grounds to doubt
an experimental row whose full text we have not read, and a haem receptor does bind haem, so the
row is accepted with the ambiguity recorded rather than acted on.

## Correction, 2026-11-13 (PR #6341 review): quotes that did not support their rows

Three rows carried a `supporting_text` that established something other than the claim, with the
`reason` honestly saying so -- which left a quote sitting in the evidence slot arguing against the
row it supported.

- `GO:0020037 heme binding`: the quote was the operon sentence attributing haem binding to **HasA**,
  not HasR. The ACCEPT stands on curator deference, as the reason explains, but no quote is asserted
  now, because none in the abstract supports binding by HasR itself.
- `GO:0007166` and `GO:0038023`: the same operon quote established context, not signalling. Both
  remain KEEP_AS_NON_CORE on similarity evidence, with no quote asserted.

Better to assert no quote than one that does not carry the claim.
