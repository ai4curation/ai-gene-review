# STXBP2 (Munc18-2, UniProtKB:Q15833) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for STXBP2. Only `openscientist` and `claude_code` are registered as
providers in this environment, and earlier runs in this campaign established that `falcon` and
`perplexity` are unavailable while an openscientist run exceeded the session's background limit without
producing output. No provider file was written, and this file is deliberately **not** named as one. These
are my own notes from the cached publications, the UniProt record, the local GO edit file, QuickGO and the
PANTHER classification files, with provenance for each assertion.

## What the protein is

The Sec1/Munc18 protein that makes the last step of regulated exocytosis go to completion. It is soluble
and peripheral — it has no transmembrane segment, and it works by binding a syntaxin: syntaxin-11 in
lymphocytes, syntaxin-3 in neutrophils and epithelium [PMID:18588921 "We found that human neutrophils
express Munc18-2 and Munc18-3 isoforms and that Munc18-2 interacts with the target-SNARE syntaxin 3."],
and syntaxin-1A and syntaxin-2 by similarity only (UniProt `CC:SUBUNIT`, `ECO:0000250|UniProtKB:Q62753`).

## The two things it does, and the experiment that separates them

This is the fact the review is organised around.

**It chaperones syntaxin-11 to the plasma membrane.** The direction of the dependence was settled by
imaging endogenous protein in patient cells from both diseases, so each partner could be removed in turn
[PMID:26771955 "while Munc18-2 localization is unaffected by the absence of STX11 in FHL4 CTL, STX11 is
lost from the plasma membrane in FHL5 CTL lacking Munc18-2"]. Munc18-2 itself sits predominantly on the
cytolytic granule with a small pool at the plasma membrane where syntaxin-11 is [PMID:26771955 "Munc18-2
localized predominantly to cytolytic granules with low levels associated with the plasma membrane where
STX11 localized."].

**It then drives the SNARE complex past hemifusion.** Syntaxin-11 is lipid-anchored rather than
transmembrane, and with its cognate SNAREs alone the reaction stops at lipid exchange without cytoplasmic
continuity [PMID:28265073 "we show that lipid-anchored STX11 and its cognate SNARE proteins mainly support
exchange of lipids but not cytoplasmic content between cells, resembling hemifusion"]. Adding wild-type
Munc18-2 produces complete fusion and binding-defective mutants do not [PMID:28265073 "complete fusion is
stimulated by addition of wild-type Munc18-2 to the assay, but not of Munc18-2 mutants with abnormal STX11
binding"], which is what makes an SM protein part of the core machinery [PMID:28265073 "Our data reveal
that Munc18-2 is not just a chaperone of STX11 but also directly contributes to complete membrane merging
by promoting SNARE complex assembly."].

Chaperoning alone cannot explain the second result, because the SNAREs were already in place.

## The myeloid arm, from one paper

PMID:18588921 carries seven GOA rows on its own and is the only source in the record for the neutrophil
function. The isoform contrast is what makes its granule rows interpretable: Munc18-2 was preferentially
on primary granules and Munc18-3 on secondary and tertiary ones [PMID:18588921 "Munc18-2 was associated
preferentially with primary granules but could also be found with secondary and tertiary granules"], and
the functional test followed the same division [PMID:18588921 "Munc18-2 primary granule exocytosis can be
blocked by introduction of Munc18-2-specific antibodies indicating a crucial role in primary granule
fusion."]. So the specific- and tertiary-granule rows are kept non-core and the azurophil (primary)
granule row is accepted as core.

Note that the azurophil granule row here is on `GO:0042582` — the organelle. That is the right side for a
cytosolic-face protein, and it is worth contrasting with the companion UNC13D review, where Reactome gives
the same granule's **lumen**.

## The presynaptic rows, and why they are removed here

`GO:0099525` presynaptic dense core vesicle exocytosis (IBA) and `GO:0098793` presynapse (IEA, logically
inferred from it) are removed. Comparator check by term id against QuickGO, with the hit count confirmed
non-zero first: `GO:0099525` returns six human rows — RAB3A, SNAP25, **STXBP1, STXBP2 and STXBP3**. Three
paralogs carrying one neuron-specific term is the signature of a single assertion placed above their
divergence, and only STXBP1 is neuronal. The IBA's donor is `WB:WBGene00006757`, the single
*C. elegans* unc-18, which acts at the neuromuscular junction; in mammals that job went to STXBP1, whose
disease is epileptic encephalopathy.

Three further points, in order of strength:

1. UniProt's tissue specificity for this protein is "Placenta, lung, liver, kidney and pancreas, as well as
   in peripheral blood lymphocytes" — no neural tissue.
2. Its documented partners are syntaxin-11, syntaxin-3 and syntaxin-2, none of them the neuronal t-SNARE.
3. The term is defined by a neuronal dense core vesicle as input and a presynapse as location, neither of
   which this protein encounters.

The obvious counter-argument is pre-empted in the review: FHL5 patients do sometimes have neurological
features, but UniProt describes them in the same sentence as the organ infiltration by activated
lymphocytes and macrophages that causes them, not as evidence of a neuronal function.

The node placement rather than this gene's row is the thing worth fixing, so it is also recorded as an
`OVER_PROPAGATION` source defect against PANTHER at `PROBABLE` with `requested_change: CHECK`. The
companion STX11 review reaches the same conclusion about a different node but stops at
`MARK_AS_OVER_ANNOTATED` and `SUSPECTED`, because there the expression and chemistry arguments are not
available — syntaxin-11 is broadly expressed and does form an in vitro complex with VAMP2.

## The four syntaxin-11 protein-binding rows

All four carry `UniProtKB:O75558` in WITH/FROM, so the partner is named and is a syntaxin; all four are
refined to `GO:0019905` syntaxin binding. Two are from the FHL5 papers and two from high-throughput maps
(BioPlex 3.0, the multimodal cell map). GO retains only syntaxin-1 and syntaxin-3 binding as children of
`GO:0019905`, the other partner-specific terms having been merged into the parent, so there is no
syntaxin-11 binding term and inventing one would cut against that merge.

## A Reactome event that supplies its own caveat

`Reactome:R-HSA-482772` is "Release of platelet cytosolic components", and its summary says the releasate
"contains a range of proteins that do not originate in specialized storage granules" and that "In some
cases platelet lysis may contribute to the presence of these proteins in the platelet relesate" (the typo
is the source's). That is quoted on the `GO:0005576` extracellular region row as the reason to mark it
over-annotated, while the `GO:0005829` cytosol row from the same event is kept. Marked `VERIFIED` rather
than `MISCITED` at the reference level: the source is not misrepresenting anything, it is the GO mapping of
a releasate set to a location term that overreaches.
