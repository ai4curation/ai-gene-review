# STX11 (syntaxin-11, UniProtKB:O75558) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for STX11. Only `openscientist` and `claude_code` are registered as
providers in this environment; `falcon` and `perplexity` fail immediately, and the one openscientist run
attempted in this campaign exceeded the session's background limit without producing output. No provider
file was written, and this file is deliberately **not** named as one. These are my own notes from the
cached publications, the UniProt record, the local GO edit file, QuickGO and the PANTHER classification
files, with provenance for each assertion.

## What the protein is

The target-membrane SNARE that performs the final fusion of a cytolytic granule with the plasma membrane,
and an atypical syntaxin in a way that turns out to matter. It was found by using SNAP-23 as bait
[PMID:10036234 "Using human SNAP-23 as the bait in a yeast two-hybrid screen of a human B-lymphocyte cDNA
library, we have identified the 287-amino-acid SNARE protein syntaxin 11."], shown to bind VAMP and
SNAP-23 and to exist in a complex with SNAP-23 in native human B lymphocytes, and reported in the same
paper to lack the feature every other syntaxin has [PMID:10036234 "Unlike other syntaxin family members,
no obvious transmembrane domain is present in syntaxin 11."]. It is held in the bilayer by palmitoylation
instead, and that modification is also what polarises it to the immunological synapse (UniProt `CC:PTM`,
from PMID:24910990).

In a primary human effector cytotoxic T lymphocyte the sequence has been resolved in time and space
[PMID:24227526 "Dual color evanescent wave imaging suggested a sequential process, in which first Stx11 is
transported to the IS through a subpopulation of recycling endosomes."], and the knockdown places the
requirement at the fusion step rather than at delivery [PMID:24227526 "Downregulation of endogenous Stx11
resulted in a complete inhibition of LG fusion that was paralleled by a reduction in LG dwell time at the
IS."].

The lipid anchor has a measurable consequence: reconstituted with SNAP23 and VAMP8 the protein gets only
as far as hemifusion, and complete fusion needs Munc18-2 [PMID:28265073 "we show that lipid-anchored STX11
and its cognate SNARE proteins mainly support exchange of lipids but not cytoplasmic content between
cells, resembling hemifusion"]. That is why FHL4 and FHL5 are the same failure reached through two genes.

## A second arm, in macrophages, with the only negative result in the record

PMID:21388490 puts endogenous Stx11 on endosomal membranes in macrophages and reports something the rest
of the record does not [PMID:21388490 "While Stx11 did not form a typical trans-SNARE complex, it did bind
to the Q-SNARE Vti1b and was able to regulate the availability of Vti1b to form the Q-SNARE complexes
Stx6/Stx7/Vtib and Stx7/Stx8/Vti1b."]. Depletion enlarges late endocytic compartments and blocks late
endosome to lysosome fusion, rescued by an siRNA-resistant construct.

Its GOA row on `GO:0031201` is correspondingly a **NOT** annotation, which the review keeps with a
declared `consistency_exception` rather than deleting: in a macrophage endosome the protein regulates
another SNARE's complexes rather than entering a bundle of its own, while in an activated cytotoxic T
lymphocyte it contributes the Qa helix of a STX11/SNAP23/VAMP8 complex characterised six years later. The
scope reservation is recorded too — GO negations are gene-level, so a result obtained in one cell type with
one partner set reads as a claim about the protein, which is more than the authors said.

## The 133 bare protein-binding rows

Every one of them comes from a high-throughput interaction dataset, with two exceptions (the FHL5 papers,
partner STXBP2). Fourteen distinct screens are involved, and knowing which is which changes what the row
means, so each row's reason names its dataset and what a hit from it is.

Partner accessions were resolved to gene symbols through the UniProtKB REST API rather than from memory;
100 of 100 resolved, giving 98 distinct partners.

Three groups get different treatment:

| Group | Rows | Action |
|---|---|---|
| SNARE partners (SNAP23 ×6, SNAP25 ×4, STX1A, STX4) | 13 | `MODIFY` → `GO:0000149` SNARE binding |
| SM-protein partners (STXBP2 ×4, STXBP1 ×4) | 8 | `KEEP_AS_NON_CORE` — GO has no term for binding a Sec1/Munc18 protein |
| everything else, including TBK1 ×4 and SIKE1 ×2 | 112 | `KEEP_AS_NON_CORE` under the ClinGen Mendelian standing instruction |

Two points worth keeping:

- **The ontology asymmetry is real.** Munc18-2's record can state this exact interaction as
  `GO:0019905` syntaxin binding; syntaxin-11's record cannot state the reverse, because there is no
  SM-protein binding term. Four rows in this review are consequently kept as bare protein binding for an
  interaction that is direct, disease-linked on both sides and mapped to residues 1–25 of syntaxin-11
  (UniProt `FT REGION`, from PMID:24910990). Raised as a `suggested_questions` entry.
- **A kinase keeps reappearing and nobody has followed it up.** TBK1 is recovered by four independent
  datasets (BioPlex 2.0 and 3.0, the multimodal cell map, a liver Y2H network) and SIKE1, a TBK1
  suppressor, by two more. That is better replication than most of the 98 partners. No publication links
  TBK1 to syntaxin-11, so nothing is annotated; it is recorded as a question and an experiment instead.

Replication across independent datasets was computed rather than assumed: 21 of the 98 partners appear in
more than one reference, and each row's reason names the others when they exist.

## Why one reference needed its method stated

`PMID:30886144` is not a screen but an L3 network **link-prediction** study. It did put its top
predictions through a high-throughput binary assay against an independent interactome, so the pair it
carries (KIFC3, also in HuRI) was predicted first and tested second. The row is kept like the screen rows,
with that provenance on it, rather than being treated as an ordinary experimental IPI.

## The synaptic rows

`GO:0031629` synaptic vesicle fusion to the presynaptic active zone membrane and `GO:0048787` presynaptic
active zone membrane are both IBA from `PANTHER:PTN000461527`, seeded by one mouse gene. Comparator check
by term id against QuickGO, hit count confirmed non-zero first: each term returns 46 human rows, carrying
the genuinely synaptic set (complexins, synaptotagmins, RAB3A, SNAP25, STX1A, STX1B) **and** STX11, STX19
and STX2 — three non-synaptic syntaxins. That is a node placed above their divergence.

Marked `MARK_AS_OVER_ANNOTATED` rather than removed, and the difference from the companion STXBP2 review is
deliberate: there the gene has no neural expression and a named neuronal paralog carrying the function, so
the rows went. Here UniProt calls syntaxin-11 broadly expressed and the cloning paper reports an in vitro
complex with VAMP2, so neither expression nor chemistry rules a synapse out. What can be said is that no
publication places the protein at a synapse and that its cognate partners throughout the record are SNAP23
with VAMP8 or VAMP4. Recorded as a source defect against PANTHER at `SUSPECTED` — one confidence step
below the equivalent STXBP2 claim, for exactly that reason.

## Two localisations that needed UniProt's reading of the same experiment

UniProt notes that the trans-Golgi network, recycling and late endosome detections in PMID:10036234 were
made "when overexpressed", and lists Late endosome membrane as a location while **not** listing the
trans-Golgi network at all. So:

- the late endosome rows are accepted, because PMID:21388490 confirmed that compartment on endogenous
  protein in macrophages and measured a function there;
- the trans-Golgi network row is kept only as non-core, as the weakest compartment claim in the record.

Neither is questioned: the GOA curator read the full text, and a SNARE transiting the trans-Golgi network
on its way to the surface is unsurprising.

## A stale row in the committed GO term cache

The module annoton for this protein uses `GO:0005484`, whose current ontology name is
**helical-bundle zippering fusogenic activity** — which is what this gene's GOA file carries, and what the
42 newer uses in the corpus carry. The repository's committed `cache/go/terms.csv` still holds the older
`SNAP receptor activity` (row dated 2026-06-02), which is a NARROW synonym of the same id, and the module
validator checks labels against that cache. The module therefore carries the cache's label, matching the
three existing modules that use the term, with the current name in `preferred_term`.

Refreshing that one cache row would be the real fix, but it would invalidate the 27 existing uses of the
old label across the corpus — so it belongs in a dedicated cache-refresh PR, per the project's rule that
single-file shared caches are regenerated separately from content changes, not in this one.
