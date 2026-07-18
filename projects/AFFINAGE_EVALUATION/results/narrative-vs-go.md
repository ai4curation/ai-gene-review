# The mechanism narrative — the complement to the GO layer

The [GO-overlap analysis](summary.md) evaluates Affinage's `mechanism_profile` GO
terms and finds them systematically over-general (0/25 specific core-MF captured).
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

## Implication for AIGR

The narrative + structured discoveries — not the GO layer — are the valuable
**deep-research input** for AIGR reviews (feeding `description`, `core_functions`,
`proposed_new_terms`), gated by two cheap checks: (a) the `pairwise` self-signal, and
(b) an entity-collision check comparing `prefetch_data.uniprot.accession` against the
organism/protein the narrative actually describes.
