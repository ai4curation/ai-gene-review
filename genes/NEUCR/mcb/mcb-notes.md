# NEUCR mcb review notes

## 2026-10-11

### Setup

- Created the seeded review with `UV_FROZEN=1 just fetch-gene NEUCR mcb`.
  The fetch created 10 GOA rows and reused the existing PTHR11635 PAINT cache.
- Attempted deep research with
  `UV_FROZEN=1 just deep-research-falcon NEUCR mcb --fallback perplexity-lite`.
  This failed locally because `agentapi` was absent from `PATH` and the fallback
  provider API keys were not configured, so this review was completed from GOA,
  UniProt, PANTHER/PAINT, cached publications, and manual PubMed searches.

### Literature search

- Fetched the original mcb cloning paper, PMID:8918454, from the UniProt record.
  PMC full text was blocked by the publisher and the HTML fallback only yielded
  an abstract, but the abstract directly states that the temperature-sensitive
  `mcb` mutant encodes the regulatory subunit of cAMP-dependent protein kinase.
- Searched PubMed for Neurospora `mcb`, microcycle conidiation, and PKA papers.
  Fetched the direct 2001 trehalose paper on `cr-1` and `mcb` mutants
  (PMID:11356572), the 2005 `pkac-1` catalytic-subunit paper that suppresses the
  `mcb` growth-polarity phenotype (PMID:15824453), the 2008 CRE-1 paper showing
  carbon-source modulation of the `mcb` apolar phenotype (PMID:17625933), and
  the 2010 glycogen paper treating `mcb` as a constitutively active PKA mutant
  (PMID:19883780).
- Also fetched the 2015 circadian-clock paper (PMID:25848091), which used `mcb`
  as an elevated-PKA-activity mutant and showed that MCB is required for
  suppression of WC-independent `frq` transcription through PKA-dependent
  phosphorylation of RCM-1. The paper is useful pathway context but likely too
  downstream for a direct GO process annotation on MCB.

### Annotation decisions

- Accepted the four `PANTHER:PTN004280545` IBAs for the conserved PKA
  regulatory-subunit node: `GO:0004862`
  cAMP-dependent protein kinase inhibitor activity, `GO:0005952`
  cAMP-dependent protein kinase complex, `GO:0030552` cAMP binding, and
  `GO:0034236` protein kinase A catalytic subunit binding. These are all
  facets of the same conserved PKA regulatory-subunit role identified by Bruno
  et al. in the original `mcb` cloning paper and reiterated by Liu et al. in
  the circadian-clock study.
- Accepted the InterPro2GO `GO:0005952` duplicate and broad `GO:0008603`
  regulator-activity parent because both agree with the PKA regulatory-subunit
  assignment.
- Accepted the `PANTHER:PTN000180782` cytosol IBA. Modified that same node's
  `GO:0007189` GPCR/adenylate-cyclase row to `GO:0141156` cAMP/PKA signal
  transduction: MCB acts at the PKA holoenzyme, and the receptor-neutral
  cAMP/PKA signal transduction term fits the reviewed Neurospora mcb evidence
  better than a GPCR-scoped pathway term.
- Accepted the fungus-scoped `PANTHER:PTN000908765` nuclear IBA. The cached
  Neurospora literature does not directly localize MCB, but absence of
  organism-specific imaging is not evidence for loss of the fungal
  regulatory-subunit nuclear pool.
- Marked the ARBA `GO:0006950` response-to-stress IEA as over-annotated. The
  trehalose, thermotolerance, glycogen, and heat-shock observations are
  downstream PKA pathway phenotypes rather than a generic stress-response step
  executed by MCB itself.
