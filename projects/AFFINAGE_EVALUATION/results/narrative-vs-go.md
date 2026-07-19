# The mechanism narrative — the complement to the GO layer

The [GO-overlap analysis](summary.md) evaluates Affinage's `mechanism_profile` GO
terms and finds them systematically over-general (1/42 specific core-MF captured).
But that is Affinage's **weakest** output. Its actual product is the
citation-anchored **`narrative.mechanistic_narrative`** plus the structured
`timeline.discoveries`. This note evaluates that layer, because judging Affinage by
its GO grounding alone is unfair to it.

**Sampled genes:** GPX4, CASP3, MAPK1, ADRB2 (full records re-fetched; the committed
cache is trimmed and does not include these narrative fields — re-fetch with the API
to reproduce). Quotes below are verbatim from the `mechanistic_narrative` field.

## The narrative recovers exactly what the GO layer drops

For every gene where the GO layer collapsed to a top-level parent, the prose names
the **specific** mechanism — matching the curated core function the GO grounding
missed — and cites it densely (distinct inline PMIDs in parentheses):

| Gene | GO layer (lossy) | Mechanistic narrative (specific) | Curated core MF |
|------|------------------|----------------------------------|-----------------|
| GPX4 | oxidoreductase activity | "selenocysteine-dependent glutathione peroxidase… reducing esterified phospholipid hydroperoxides within membranes to non-toxic lipid alcohols, a reaction no other enzyme performs… central defense against ferroptosis" (29) | GO:0047066 phospholipid-hydroperoxide glutathione peroxidase activity |
| CASP3 | catalytic activity, acting on a protein | "principal executioner cysteine protease… 32-kDa zymogen… processed into p20/p11… DEVD-like cleavage… cleaves PARP" (25) | GO:0004197 cysteine-type endopeptidase activity |
| MAPK1 | catalytic activity, acting on a protein | "MAPK1/ERK2… serine/threonine kinase… terminal effector of the ERK MAP kinase module… MEK1-mediated dual phosphorylation" (25) | GO:0004707 MAP kinase activity |
| ADRB2 | molecular transducer activity | "ADRB2 (β2-adrenergic receptor)… catecholamine-responsive G-protein-coupled receptor" (18) | GO:0004941 beta2-adrenergic receptor activity |

**Conclusion:** the GO `mechanism_profile` is a lossy down-cast of a narrative that
clearly encodes the specific function. The GO layer does not measure what Affinage
knows; it under-reports it.

## The discoveries are structured and confidence-graded

Each entry in `timeline.discoveries` is not free text but a structured object:

```
year, finding, method, journal, confidence, confidence_rationale,
pmids: [...], is_preprint
```

plus a parallel `teleology` track recording *what each advance explained* (e.g. for
GPX4: "established the catalytic basis for GPX4's distinctive substrate range…").
This is a richer, more curator-usable artifact than the GO layer — closer to a
graded literature review than an annotation set.

## Two real failure modes of the narrative

1. **Recency / novelty bias on canonical genes.** The ADRB2 narrative surveys recent
   specialized findings (HCC sorafenib resistance, amyloid-β, CAR-T checkpoint,
   osteoclastogenesis) but **omits the textbook core mechanism**: no cAMP, no
   adenylyl cyclase, no Gs coupling, no β-arrestin desensitization. For a
   heavily-studied pleiotropic receptor it reads like a literature-mining digest, not
   a mechanism primer — high on specific recent detail, low on canonical completeness.
2. **Symbol collisions break even the prose.** ADA's narrative is a chimera of three
   "ADA/Ada" entities (*E. coli* Ada, the eukaryotic ADA2/ADA3 SAGA/ATAC subunits,
   and human adenosine deaminase) — see the [project page](../../AFFINAGE_EVALUATION.md)
   §3.

## A useful built-in triage signal

Affinage's own `evaluation.pairwise` (win / tie / loss vs the curated UniProt
reference) tracks these tiers cleanly in the sample: GPX4, CASP3, MAPK1 = `win`
(specific, accurate); ADRB2 = `tie` (recency-biased, canonical gaps); ADA = `loss`
(entity collision). That field is a ready-made flag for which narratives to trust
before ingesting them.

## Implication for AIGR — largely redundant with deep research

The narrative reads well, but as an *input source* it does **not** clearly beat what
AIGR's existing deep-research step already produces, and most of its apparent
advantages are trivial to replicate:

- **Biological content** overlaps heavily with our deep research. For well-studied
  human genes our falcon/perplexity reports already recover the specific mechanism
  (the falcon GPX4 report independently gives Sec46, the catalytic tetrad, the
  system xc⁻–GSH–GPX4 axis, ferroptosis) — Affinage adds no new biology.
- **PMID-anchored citations are not a differentiator.** DOI/`[n]`→PMID resolution is
  a one-liner (NCBI/EuropePMC ID converter), so the fact that Affinage emits inline
  PMIDs while falcon/perplexity emit DOIs or footnote numbers is cosmetic.
- **"More citations" is not value.** For GPX4, Affinage cites 37 PMIDs vs the 10 in
  our completed review (1 overlap). But curation *selects* the few core papers; the
  extra 36 skew toward the pleiotropic/recent material a curator prunes (the same
  recency bias as ADRB2). Count ≠ quality, and the novel PMIDs were not shown to be
  primary evidence for core function that we lack.
- **No independent perspective.** Affinage is Claude-generated (Sonnet read + Opus
  synthesis); AIGR's review agent is also Claude, so ingesting it adds no model
  diversity and risks amplifying shared biases — unlike our multi-provider ensemble.
- **Human-only.** AIGR spans 190+ species; Affinage can never touch the non-human
  majority of reviews.

**Residual (minor) value.** It is a *free, precomputed* artifact for all 19,293 human
genes, so for the human review backlog it could save the compute of a first-pass
deep-research run — a convenience, not new capability, and subject to the
correlated-error and human-only caveats above. Its flag of ~10% of the human proteome
as mechanistically dark is a weak *prioritization* signal (project-management, not a
per-review source).

**Recommendation:** do not wire Affinage in as a distinct review source on this
evidence. The durable output of this exercise is the *evaluation result* (the GO layer
grounds to the specific function ~1/42 while the prose gets it right), not an
integration.
