# AAGAB (p34, alpha- and gamma-adaptin-binding protein) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AAGAB-deep-research-affinage.md`, gates passed) plus UniProt Q6PD74, the GOA TSV and the
primary literature.

## The problem with this gene's GO record

AAGAB has **18 GOA annotations and not one of them says what the protein does.**

- 15 × `GO:0005515 protein binding` (IPI)
- 3 × cytosol / cytoplasm localisation

There is **no molecular function** beyond bare binding and **no biological process at all**.
Meanwhile AAGAB has been the subject of a decade of focused mechanistic work and is, by the
title of one of its own papers, "an assembly chaperone regulating AP1 and AP2 clathrin
adaptors" [PMID:34494650, "AAGAB is an assembly chaperone regulating AP1 and AP2 clathrin
adaptors."]. UniProt is also stale here, offering only a hedged
"May be involved in endocytic recycling of growth factor receptors such as EGFR" from 2012
[file:human/AAGAB/AAGAB-uniprot.txt, "May be involved in endocytic recycling of growth factor"].

This is the largest gap between literature and annotation I have hit in this campaign so far.

## What AAGAB actually does

AAGAB is the dedicated **assembly chaperone for heterotetrameric AP-type membrane coat adaptor
complexes**. It is not a folding chaperone — the subunits are already folded — it enforces an
*ordered assembly pathway* and protects unassembled intermediates from degradation.

- **AP-2.** AAGAB guides sequential subunit association; without it, AP2 subunits fail to
  assemble and are degraded [PMID:31353312].
- **AP-1.** AAGAB binds and stabilises the γ and σ subunits; mutation abolishes AP1 assembly
  [PMID:34494650, "AAGAB promotes AP1 assembly by binding and stabilizing the γ and σ subunits
  of AP1"]. Notably it is **not** required for AP-3
  [PMID:34494650, "However, AAGAB is not involved in the formation of other adaptor complexes,
  including AP3."] — a specificity fact worth preserving.
- **AP-4.** AAGAB binds and stabilises ε and σ4; knockout cells phenocopy AP-4 subunit mutants,
  accumulating ATG9A at the TGN
  [PMID:35976721, "we report that the alpha- and gamma-adaptin-binding protein (AAGAB, also
  known as p34) binds to and stabilizes the AP-4 ε and σ4 subunits, thus promoting complex
  assembly."]. The same paper states the general point plainly: assembly "is not spontaneous
  but AAGAB-assisted".

Architecture (PMID:36598941): an N-terminal **type I pseudoGTPase** domain (catalytically
inactive) that engages the small σ subunits, and a C-terminal dimerisation domain that
recognises AP1-γ and AP2-α through a shared surface. AAGAB is a homodimer that converts to
monomer on binding adaptor subunits. PPKP1 disease mutations truncate the CTD, destabilising
the protein and abolishing chaperone function — which ties the molecular mechanism directly to
the human disease. For AP-2 there is a documented handoff to CCDC32 (PMID:39145939), so AAGAB
genuinely **does not form part of the finished complex** — the exact wording of GO:0051131.

## The 15 `protein binding` annotations are not junk

Every one of them comes from a large-scale interactome screen (HuRI/Rolland, Luck binary
interactome, BioPlex/Huttlin, OpenCell endogenous tagging, Schaffer multimodal cell maps, and
an interactome-perturbation study). My first instinct was to mark them over-annotated. That
would have been wrong.

Resolving the WITH/FROM ids shows what they actually recovered:

| Partner | Identity | Screens recovering it |
|---|---|---|
| P53680 | **AP2S1** (AP-2 σ2) | 7 of 7 |
| O94973 | **AP2A2** (AP-2 α2) | 2 |
| O43747-2 | **AP1G1** (AP-1 γ1) | 2 |
| Q96PC3 | **AP1S3** (AP-1 σ3) | 3 |
| Q96ES5 | HEATR1 | 1 |

AP2S1 is recovered by **seven orthogonal methods** (Y2H, AP-MS, endogenous tagging,
proximity), and the partner set is precisely the σ and γ/α subunits that the focused
mechanistic literature identifies as AAGAB's clients. These are real, reproducible,
mechanistically meaningful interactions recorded under an uninformative term. The right action
is `MODIFY` to something informative, not `MARK_AS_OVER_ANNOTATED`.

**HEATR1 is the exception**: recovered in only one study, unreplicated by any other screen,
and a nucleolar ribosome-biogenesis protein with no mechanistic connection to adaptor assembly.
(`AAGAB-uniprot.txt:171` records `NbExp=3` IntAct experiments for the pair, but all three come
from that single report, so it is one study rather than one experiment.) That one is marked
over-annotated.

This produces a deliberate `⚠ WARN` about inconsistent actions on `GO:0005515` (14 MODIFY,
1 MARK_AS_OVER_ANNOTATED). The inconsistency is real biology — most of these interactions are
the protein's core clients, one is screen noise — so the distinction is kept.

## Term choices, and two gaps in GO

- **Correction made during review — `GO:0035650` does exist.** I first recorded that GO has no
  `AP-1 adaptor complex binding` term, on the strength of an OLS keyword search that returned
  nothing. That was wrong: a direct id lookup confirms `GO:0035650 AP-1 adaptor complex
  binding` is a real, non-obsolete term. GO in fact has AP-1 (`GO:0035650`), AP-2
  (`GO:0035612`) **and** AP-3 (`GO:0035651`) complex-binding terms — and no AP-4 term, which
  is the one adaptor with a genuine gap. The AP-1 entries now use `GO:0035650` rather than the
  vague `GO:0044877`. **Lesson: an empty OLS keyword search is not evidence a term is absent —
  confirm by direct id lookup before proposing a new term.**
- **Scope check on the proposed term's name (added after review round 2).** The proposal was
  first drafted as *clathrin adaptor complex subunit binding*. That name would have excluded
  one of AAGAB's own three clients: **AP-4 is not a clathrin adaptor**. Verified directly
  against the local GO database rather than assumed —

  | Term | is_a |
  |---|---|
  | `GO:0030121` AP-1 adaptor complex | `GO:0030131` clathrin adaptor complex |
  | `GO:0030122` AP-2 adaptor complex | `GO:0030131` clathrin adaptor complex |
  | **`GO:0030124` AP-4 adaptor complex** | **`GO:0030119` AP-type membrane coat adaptor complex** |

  The term is therefore scoped to `GO:0030119`, and the same conflation was corrected in the
  top-level `description` and in `core_functions.description` ("AP-type clathrin adaptor
  complexes" → "AP-type membrane coat adaptor complexes").

- **Term labels machine-verified.** After the `GO:0035650` episode, every id used or proposed
  here was resolved against the local `go.db` via oaklib rather than trusted from memory:
  `GO:0035650` = AP-1 adaptor complex binding, `GO:0035612` = AP-2 adaptor complex binding,
  `GO:0051131` = chaperone-mediated protein complex assembly, `GO:0030119`/`GO:0030131`/
  `GO:0030124` as tabulated above. Note `just fix-labels` skips `proposed_new_terms` and
  `proposed_replacement_terms` by default (`--no-skip-proposed` opts in), so proposed-term
  labels are *not* covered by the routine label check — worth knowing for the rest of this
  campaign.

- **The real gap is subunit-level binding.** All three existing terms denote binding the
  assembled heterotetramer, whereas AAGAB binds *free* subunits and is displaced before the
  tetramer exists — PMID:39145939 shows the AAGAB:α:σ2 intermediate "cannot recruit additional
  AP2 subunits" and is handed to CCDC32. A complex-binding term therefore asserts exactly the
  interaction AAGAB's mechanism excludes. `GO:0035612`/`GO:0035650` are used as an explicitly
  flagged interim, with the caveat written into every `reason` field, and a subunit-binding
  term is filed under `proposed_new_terms`.
- **There is no MF term for assembly-chaperone activity.** `GO:0044183 protein folding
  chaperone` is explicitly about folding — its definition says "a protein folding chaperone
  binds an unfolded protein to fold it" — and AAGAB's clients are folded subunits awaiting
  assembly. Affinage's grounding proposed exactly this term, and importing it would have been
  a mistake; this is a concrete instance of the AFFINAGE_EVALUATION warning not to import the
  `mechanism_profile` GO ids. A proper MF term is filed under `proposed_new_terms`.
- The BP side is well served: `GO:0051131 chaperone-mediated protein complex assembly` is an
  exact fit ("...mediated by chaperone molecules that do not form part of the finished
  complex"), added as `NEW`.

## Recorded but not annotated

- **NEDD4-1 / PTEN / SHIP2 axis** in hypoxic-ischaemic injury (PMID:33712741, PMID:41412220):
  rat/cell models, single group, mechanism unclear relative to the adaptor-chaperone role.
- **Synaptic vesicle recycling** in zebrafish (PMID:38253235): plausible downstream consequence
  of impaired AP-2 assembly rather than a separate function.
- **EGFR recycling** (PMID:23064416): the original 2012 observation, now best understood as a
  downstream consequence of reduced AP-2. UniProt still leads with this hedge.
- **PPKP1 palmoplantar keratoderma**: disease association, not a GO process.
