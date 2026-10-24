# ERLEC1 curation notes

## 2026-09-04 — Finishing pass (PAINT no-IBA project)

Completed the review pass over `ERLEC1-ai-review.yaml` (previously IN_PROGRESS, now
COMPLETE; validates with zero warnings).

What was checked and changed:

- Verified programmatically that all 34 GOA rows are covered by an
  `existing_annotations` entry (the three PMID:18264092 IPI protein-binding rows with
  different WITH/FROM partners collapse into a single entry for the same
  term/evidence/reference); two further entries carry `action: NEW`. Kept the
  machine-backfilled GOA qualifiers from today's fetch-gene run.
- Confirmed GO:0051082 "unfolded protein binding" is formally obsolete (QuickGO:
  `isObsolete: true`; obsoletion comment directs to chaperone activity terms, which
  do not apply to a lectin-based ERAD cargo receptor). The existing REMOVE action for
  the IDA annotation stands: the underlying biology (binding of misfolded
  glycoproteins) is retained via the NEW GO:0051787 (misfolded protein binding)
  annotation, so no experimental evidence is discarded — the term itself is the
  problem, not the curator's observation.
- Strengthened the GO:1904153 (negative regulation of retrograde protein transport,
  ER to cytosol; IMP PMID:25660456) entry. The earlier draft hedged that the
  inhibitory effect might be an overexpression/dosage artifact; the deep research
  synthesis shows it is genuine, genetically supported physiology:
  - Fujimori et al. concluded XTP3-B "inhibits ER-associated degradation of a
    misfolded α1-antitrypsin variant (NHK)" and may protect newly synthesized
    glycoproteins from premature degradation [DOI:10.1111/febs.12157].
  - van der Goot et al. deletion study: "XTP3B strongly inhibits degradation of
    non-glycosylated substrates, and OS9 antagonizes this inhibition"
    [DOI:10.1016/j.molcel.2018.03.026, quoted via
    file:human/ERLEC1/ERLEC1-deep-research-falcon.md].
  Kept the action KEEP_AS_NON_CORE: the inhibitory activity is a modulatory facet of
  ERLEC1's context-dependent triage role, not its core cargo-receptor function.
- Added `file:human/ERLEC1/ERLEC1-deep-research-falcon.md` to the references list
  with findings (triage model; SEL1L stabilization of ERLEC1; Man5/Man9 glycan
  specificity of the C-terminal MRH domain) and cited it in the GO:1904153 entry,
  where the deep-research synthesis genuinely changed the reasoning.
- The 16 duplicate Reactome TAS annotations to GO:0044322 (ER quality control
  compartment) are all ACCEPT — duplicates of the same localization claim from
  different Reactome reactions (Hh, CFTR, CD274 ERAD); this is expected and fine.
- Description, core_functions (MF GO:0051787; processes GO:0036503, GO:0097466,
  GO:0030970; locations GO:0005788, GO:0044322) reviewed and left as-is; all
  author-supplied ids pass strict term validation.
