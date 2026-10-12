# SCHPO cgs1 review notes

## 2026-10-11

### Setup

- Created the seeded review with `UV_FROZEN=1 just fetch-gene SCHPO cgs1`.
  The fetch created 25 seeded review rows from 26 current GOA rows and reused
  the existing PTHR11635 PAINT cache.
- Attempted deep research with
  `UV_FROZEN=1 just deep-research-falcon SCHPO cgs1 --fallback
  perplexity-lite`. This failed locally because `agentapi` was absent from
  `PATH` and the fallback provider API keys were not configured, so this review
  needs to be completed from GOA, UniProt, PANTHER/PAINT, cached publications,
  and manual PubMed searches.

### Literature search

- Read the cached PomBase evidence set:
  - PMID:1657594, the original EMBO J cloning/genetics paper showing that
    `cgs1+` encodes the fission-yeast cAMP-dependent protein kinase regulatory
    subunit and that cAPK activity is unregulated by cAMP in `cgs1-1` cells.
  - PMID:16823372, the ORFeome localization paper that directly supports
    high-throughput nuclear and cytosolic localization rows but only in a
    proteome-scale setting.
  - PMID:18621924, the full-text Cgs1-GFP/Pka1-GFP localization paper showing
    nuclear and cytoplasmic Cgs1 under log-phase growth and condition-specific
    redistribution during glucose limitation, osmotic stress, stationary phase,
    and mating.
  - PMID:21869531 and PMID:21879336, the 2011 Pka1-Cgs1 papers supporting
    Pka1-Cgs1 complex formation under glucose-limited conditions and Cgs1
    dependence of Pka1 hyperphosphorylation.
  - PMID:27756188, the 2017 calcium-tolerance paper showing increased
    cytoplasmic Cgs1/Pka1 distribution after CaCl2 treatment.
- Searched PubMed for newer fission-yeast `cgs1`, SPAC8C9.03, and
  protein-kinase-A papers. Later hits mostly use the cAMP/PKA pathway as
  context or as a platform for reporters; no newer paper displaced the core
  picture that Cgs1 is the cAMP-binding regulatory subunit that binds and
  inhibits Pka1.

### Annotation decisions

- Accepted the direct and inherited molecular-function rows for Cgs1 as a
  cAMP-binding PKA regulatory subunit: `GO:0004862`,
  `GO:0030552`, and `GO:0034236`.
- Modified both generic `GO:0005515 protein binding` IPI rows to
  `GO:0034236 protein kinase A catalytic subunit binding`; both cited papers
  specifically detect the Cgs1-Pka1 interaction.
- Accepted the direct and PAINT localization rows for Cgs1 in the nucleus and
  cytoplasm/cytosol. PAINT's `GO:0005634 nucleus` call is fungal-scoped at
  `PTN000908765`; `GO:0005829 cytosol` is broader at `PTN000180782` but still
  matches direct Cgs1-GFP microscopy.
- Accepted `GO:0005952 cAMP-dependent protein kinase complex` from PAINT,
  InterPro, and direct Pka1-Cgs1 complex formation.
- Accepted `GO:0007189 adenylate cyclase-activating G protein-coupled receptor
  signaling pathway` for Cgs1 as the cAMP-sensing PKA regulatory subunit in the
  GPCR-to-cAMP cassette, accepted PomBase's specific `GO:0110034 negative
  regulation of adenylate cyclase-activating glucose-activated G
  protein-coupled receptor signaling pathway`, and proposed `GO:0141162
  negative regulation of cAMP/PKA signal transduction` as the receptor-neutral
  companion process term.
- Kept broad `GO:0006950 response to stress`, `GO:0042149 cellular response to
  glucose starvation`, and `GO:0046827 positive regulation of protein export
  from nucleus` as non-core contexts or consequences of the PKA-regulatory
  activity rather than adding narrower downstream stress, calcium, or
  differentiation terms.
