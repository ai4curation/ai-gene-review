# Apoptotic execution phase comparative audit

## 2026-10-26 — evidence survey and scope

This audit begins from the nine human representatives CASP3, CASP6, CASP7,
XIAP, DIABLO, DFFA, DFFB, ACIN1 and AIFM1. Existing claims and annotation
payloads will be reviewed, with mouse counterparts selected to test the
executioner, inhibitor and DNA-fragmentation branches. The present mammalian
scope is a template for supported implementations, not a claim that every
listed branch is obligatory in every mammalian cell or lineage.

Comparative literature argues against treating a mammalian execution network
as an unchanged metazoan pathway. Zmasek and Godzik review lineage-specific
losses, expansions and domain rearrangements (PMID:23457257, *Evolution of the
animal apoptosis network*). Eckhart and colleagues identify DFFA/DFFB in
cnidarians, vertebrates and insects but report their absence from the sampled
nematodes, echinoderms and urochordates (PMID:17343828, *Phylogenomics of
caspase-activated DNA fragmentation factor*). These comparisons justify keeping
worm and fly execution machinery as boundary comparisons rather than silently
substituting their proteins into the mammalian template.

The 2024 review *Exploring caspase functions in mouse models* (PMID:38824481)
provides a route into native mouse knockout studies and highlights strain,
tissue and non-apoptotic context. Walsh et al. (PMID:18723680) directly compare
CASP3 and CASP7 on protein substrates; similar activity on synthetic peptides
does not establish interchangeable native substrate repertoires. The module
must not imply that every executioner processes every substrate or is equally
restrained by XIAP. CASP6 requires its own activation/substrate treatment.

Kawane, Motani and Nagata's *DNA degradation and its defects* (PMID:24890510)
and *The role of the DFF40/CAD endonuclease in genomic stability*
(PMID:33387146) distinguish the ICAD chaperone/inhibitor, CAD catalysis and
subsequent phagocyte-mediated disposal. DFFA cleavage is a disinhibition event;
DFFA's folding activity precedes CAD activation. The current module combines
these opposing roles in one node and needs explicit activity-level edges.
Nuclear localization should be checked against the individual experiments;
release from ICAD is not by itself evidence that CAD first enters the nucleus.

## Conflicting and contextual evidence requiring adjudication

- Acinus: the original in-vitro study (PMID:10490026) supports a cleaved
  chromatin-condensation factor. The 2006 RNA-interference study
  (PMID:16537548) instead reports that knockdown did not prevent condensation
  and impaired oligonucleosomal DNA fragmentation. Akt/Acinus experiments
  (PMID:16177823) provide another context. The source claims must be retained
  with experimental qualifications; neither a universal requirement nor a
  blanket dismissal follows. RNA binding is established for RNA processing,
  but it must not be presented as a demonstrated condensation mechanism.
- AIFM1: the original module groups it beneath a caspase-activated nuclear
  branch. PMID:27846469 separates AIF-dependent recruitment of MIF in
  PARP1-driven, caspase-independent parthanatos. Nuclear AIF engagement must
  therefore be distinguished from the CASP3-to-Acinus edge; no intrinsic AIF
  nuclease activity is inferred from the MIF result.
- XIAP/SMAC: PMID:14512414 distinguishes the XIAP linker/BIR2 restraint of
  executioner caspases from BIR3-dependent caspase-9 inhibition. Native mouse
  evidence is contextual: PMID:19626005 tests XIAP-dependent type-II FAS
  signaling, whereas PMID:14623868 reports that endogenous SMAC release is
  insufficient to relieve XIAP restraint in sympathetic neurons. MOMP/SMAC
  release is consequently not a universal sufficient trigger.

## Research provenance and pending work

The initial normal publication fetch cached six of seven sources; transient
HTTP429 prevented the first fetch of PMID:16537548, which succeeded on retry.
No cached publication was manually authored. The module research wrapper and
its pinned client do not accept the gene workflow's `--fallback` flag; a plain
Falcon request failed with HTTP403 and the separately requested Perplexity-lite
fallback also failed. No provider report was produced. Full-text availability
is recorded in each normal publication cache and will constrain adjudication.

Pending: finish family identity/member checks; curate source-specific module
references and every step/edge; review the nine human genes and selected mouse
members; record helper-generated histories; validate, render, and submit a
single-module PR. This survey is not a completed module audit.

## 2026-10-26 — independent integration QA

The survey's pending module/member work above is now superseded by the integrated
sixteen-member human/mouse panel. I applied the annotation-reviewer and
AIGR PR review criteria to the module's biology, source scope and agreement with
individual gene reviews. This pass preserves the ten molecular activities and
adds three qualified connections, for ten edges total. No additional genes or
prediction-derived functions were introduced.

### Logic and participation

The schema defines module parts conjunctively, so leaving CASP3, CASP7 and the
CAD route individually required contradicted the biological caveats. All listed
routes now have optional flags, with explicit prose requiring at least one
supported execution route for an implementation. This does not mean an
individual component is dispensable in every cell or assay. Within the modeled
CAD branch, ICAD-supported productive folding and relief of ICAD inhibition are
still dependencies. The distinction is supported by ICAD-expressing Jurkat cells
that resist DNA degradation but still die after staurosporine (PMID:9422513),
mouse strain-dependent Casp7 compensation (PMID:15525783), and the previously
cited morphology/laddering uncoupling (PMID:22253444).

Removed GO:0006309 from the ICAD chaperone annoton: its supported molecular work
is CAD folding, already represented by GO:0006457 and the PROVIDES_INPUT_FOR edge.
This agrees with the DFFA reviews and does not manufacture direct nuclease
participation from a knockout requirement. The separate inhibitory activity
retains negative regulation of DNA fragmentation. Mouse CAD/ICAD discovery
(PMID:9422506), ICAD-L folding assays (PMID:10336474), and native Dffa knockout
(PMID:9770511) now directly support the comparative branch. The knockout is a
requirement for a functional system in the tested immune cells, not evidence
that DFFA cleaves DNA. Neither the original nuclear-import model nor the
reported ICAD-L/ICAD-S folding difference is universalized across assays.

The correction associated with PMID:9422513 was inspected at
https://www.nature.com/articles/nature15532 (PMID:26416741). It identifies
duplicated Figure 1a lanes 1/5 and 6/10, supplies a repeated experiment and
states that the conclusions remain unchanged. Both records are represented;
the correction is provenance, not independent mechanism evidence. The normal
cache is abstract/bibliographic only and was not edited to fabricate full text.

### Caspase specificity and assay attribution

PMID:15525783 explicitly contrasts mouse and human enzymes: mouse Casp7
inactivates ICAD efficiently in the biochemical comparison. The new CASP7-to-ICAD
negative edge is restricted to mouse. Casp7 activity/expression correlates with
preserved DNA fragmentation in C57BL/6J Casp3-null neurons, compared with
129S1/SvImJ; this is not universal genetic rescue or a human-equivalence claim.
The abstract reports the biochemical result directly; full text remained
unavailable through the normal fetch attempts, so unreported details are not
asserted.

PMID:32029622 cached full results and the primary Figure 6 caption were read
(https://pubmed.ncbi.nlm.nih.gov/32029622/ and
https://pmc.ncbi.nlm.nih.gov/articles/PMC8012106/). Figure 6A separately tests
recombinant procaspase-6 cleavage by active caspases, supporting individual
CASP3 and CASP7 positive edges. Figure 6B is **primary hepatocytes**, not HepG2;
it uses a shared CASP3/7 inhibitor and therefore does not resolve either
protease's individual cellular contribution. HepG2 appears in Figure 6H for
CASP6-dependent feedback. The module records AMPK-sensitive hepatocyte context
and avoids converting these assays into a compulsory universal cascade. It does
not assert that every family member or every human/mouse cell has that edge.

### AIF and Acinus boundaries

Added PMID:12198487 as direct human AIF DNA-binding support. The normal cache is
abstract-only, but the full author PDF was read:
https://wulab.tch.harvard.edu/_files/ugd/feeaaa_4e11ba6598944ad8b1058b0365836eac.pdf.
The biochemical protein is recombinant mature human AIF; endogenous imaging
uses Rat-1 cells and functional transfection uses mouse fibroblasts. Thus the
human-protein assertion is valid without relabeling every assay as human.
DNA-binding-defective mutants lose apoptogenic activity despite nuclear
translocation. This is not intrinsic AIF nuclease activity.

PMID:33168626 full text establishes a caspase-cleaved, PAR-bearing 89-kDa PARP1
fragment route to AIF redistribution in staurosporine/actinomycin-D-treated
HeLa cells. It is now explicit that this context is caspase linked.
PMID:27846469 is retained as the separate PARP1/MIF parthanatos boundary, not
as evidence that parthanatos belongs under the module's apoptotic BP assertion.
The AIF representative and DNA-binding branch remain; no generic CASP3-to-AIF
edge was added. Acinus remains a qualified experimental condensation branch,
with PMID:10490026 versus PMID:16537548 and the PMID:16177823 Akt context intact.
RNA binding is not proposed as the condensation mechanism. Missing a precise
molecular-function ontology identifier is an honest remaining limitation.

The scope remains Mammalia with verified human/mouse examples. Broader animal
comparisons delimit scope; family membership does not make every substrate
interaction, knockout phenotype or cell-specific requirement universal.

### Integration verification

Final module: **10 parts, 10 signed/dependency edges, 16 unique reviewed protein
representatives, 35 curated references and 28 literal supporting quotations**.
The focused ontology/family/member/function/source validator passed, with only
the two expected Acinus `NO_FUNCTION_ID` advisories (gene and family views of
the same free-text activity). LinkML `ModuleReview` schema validation passed.
`just render-module apoptotic_execution_phase` generated the HTML successfully.
The helper-created integration history
`history/modules/apoptotic_execution_phase/2026-10-26T031925Z-codex-48f894.yaml`
also passed schema validation. Logs are under `.cache/module-audit-logs/` as
`apoptosis-module-final-validation.log`, `apoptosis-module-schema-validation.log`,
`apoptosis-module-render.log` and
`apoptosis-module-integration-history-validation.log`.


## PR #5558 Boolean execution-route correction (2026-10-26)

CI `test_no_curated_module_is_satisfied_by_an_empty_context` exposed a real
logic error in the earlier integration: all ten parts were optional. The
compiler represents an optional part as a choice including an empty branch,
so prose requiring at least one execution route did not prevent the entire
module from being satisfied when no activity held. This supersedes the earlier
"Logic and participation" statement that optional flags plus prose encoded
that requirement.

CASP3 and CASP7 now form a required `ONE_OR_MORE` variant set under a principal
executioner part. Either contribution, or both, satisfies that structural
requirement. Their molecular activities, family selectors, evidence, IDs and
connection endpoints are unchanged. PMID:18723680 supports treating the two
major executioners as distinct substrate-selective contributions, not equal
substitutes for every output; PMID:15525783 supplies the specifically mouse
ICAD-cleavage alternative. The gate is the scope of this represented
caspase-mediated implementation, not a new claim that either protease alone
causes all death phenotypes or that all mammalian cell death requires CASP3/7.

CASP6 remains a context-dependent proteolytic/amplification branch, consistent
with the qualified PMID:32029622 edges. ICAD/CAD, Acinus, AIF, XIAP and SMAC
remain optional additions. In particular, AIF-associated caspase-independent
death alone does not instantiate this caspase-mediated execution template;
its retained DNA-binding branch and contextual evidence are unchanged.
Regulators alone cannot satisfy the template either. The restructuring leaves
nine top-level parts representing the same ten activities, ten edges, sixteen
protein representatives and thirty-five references.

A parameterized regression checks all four CASP3/CASP7 combinations with all
optional branches absent or present. This verifies that neither caspase is
individually mandatory, that both may coexist, and that even all contextual
branches together cannot bypass the executioner requirement. Focused module
validation and LinkML schema validation passed; the only module advisories
remain the two existing Acinus free-text-function notices. The HTML was
regenerated at `pages/modules/apoptotic_execution_phase.html`. Final test and
history results are recorded in the matching helper-created session history;
logs use `.cache/module-audit-logs/apoptosis-logic-fix-*`.
