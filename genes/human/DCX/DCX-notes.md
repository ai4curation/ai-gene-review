# DCX review notes

Journal for the DCX (O43602, doublecortin) GO annotation review.

## Sources used
- UniProt O43602 (`DCX-uniprot.txt`).
- Cached GOA-cited publications, plus papers cached for this review after PubMed eutils verification:
  PMID:10399933, PMID:10399932, PMID:15200960, PMID:22727374, PMID:14625554, PMID:27238282.
  PMID:15173193 (Tanaka 2004) was already cached (module evidence).
- Deep research (`DCX-deep-research-falcon.md`) was not present when the review was first drafted; see the end of
  this file for the final check.

## Biology summary (with provenance)
- Neuronal microtubule-associated protein with two tandem doublecortin (DC) domains (UniProt DOMAIN 53..139,
  180..263). Mutations cause X-linked lissencephaly (males) and subcortical band heterotopia (females)
  [PMID:9489699].
- MAP that stabilizes microtubules and promotes polymerization
  [PMID:10399933 "DCX coassembles with brain microtubules, and recombinant DCX stimulates the polymerization of purified tubulin"],
  [PMID:10399933 "overexpression of DCX in heterologous cells leads to a dramatic microtubule phenotype that is resistant to depolymerization"].
- Binds between protofilaments, selective for 13-pf MTs [PMID:15200960 "doublecortin binds between the protofilaments"];
  cooperative binding and 13-pf nucleation in vitro [PMID:22727374]; recognizes the compacted GDP lattice and is not a +TIP
  in cells [PMID:27238282].
- Microtubule affinity is negatively regulated by PKA and MARK/PAR-1 phosphorylation [PMID:14741102].
- Required for radial migration in rat neocortex (in utero RNAi) [PMID:14625554]; mouse Dcx knockout has mild cortical
  phenotype (redundancy with DCLK1) [PMID:14625554 "genetic deletion of Dcx in mice does not cause neocortical malformation"].
- Nucleokinesis: in mouse cerebellar granule neurons DCX outlines the perinuclear microtubule cage converging on the
  centrosome, co-immunoprecipitates with dynein, and its overexpression rescues N-C coupling defects from Lis1 deficiency
  and dynein inhibition [PMID:15173193].
- Interacts with LIS1 [PMID:11001923] and USP9X (as interactor, not substrate) [PMID:24607389].

## Decisions
- Protein binding rows: REMOVE (uninformative; mostly proteome-scale screens), except USP9X row MODIFY to
  GO:1990381 ubiquitin-specific protease binding (paper explicitly states DCX is an interacting protein, not a substrate).
- InterPro2GO rows from IPR017302/IPR003533 for axoneme assembly, intracellular signal transduction and retina development:
  REMOVE -- the DC domain is a microtubule-binding module; ciliary/retinal functions belong to RP1/RP1L1 family members,
  and there is no evidence DCX acts in signal transduction.
- microtubule associated complex (TAS): MODIFY to GO:0005874 microtubule (DCX is a lattice-binding MAP, not a subunit of a
  defined complex).
- NEW: GO:0007026 negative regulation of microtubule depolymerization (PMID:10399933, PMID:15200960).
- Nucleokinesis module: supports DCX annoton function GO:0008017 microtubule binding. Did not add a NEW nuclear-migration
  process annotation: evidence is mouse-only and DCX acts on the track (MT stabilization), which is captured by the
  MT-stabilization process term; flagged as suggested question.

## Deep research check (final)
- `DCX-deep-research-falcon.md` appeared after the first draft and was read. It agrees with the MT-nucleating,
  lattice-stabilizing MAP model (Gleeson 1999, Moores 2004, Manka & Moores 2020), PKA/MARK/CDK5 regulation, and
  X-linked lissencephaly/SBH genetics. Cited in support of NEW GO:0007026.
- Not annotated (emerging/indirect): 2023 iPSC preprint on tubulin polyglutamylation and lysosome processivity;
  kinesin-3 (KIF1A/KIF1C) cargo effects; PKA-Ser47 -> Asef2/Rac1 actin coupling. CDK5 Ser297 control of
  perinuclear microtubule association raised as a suggested question (relevant to nucleokinesis).


## 2026-10-17 bounded binding follow-up

The original review and its provenance are preserved. Merged PR #3321 had final automated approval on head 926ffa240c992f77bbf7ea8f8d9f8ff659a074aa and was squash-merged as 18dfc688ce73fdca6ec388e41237fb14211f8993. The observed cmungall-account comments identify themselves as Claude-generated; no additional human scientific sign-off is inferred. PR #3380 later added rendered HTML.

This entry supersedes only the earlier blanket removal rationale for 19 GO:0005515 source rows (3–5 and 7–22). The [explicit user instruction for the ClinGen project](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions) is present on main a87ae568 and directs retention of supported interactions as non-core when a justified narrower term is unavailable. It does not establish an uninspected interaction or authorize a functional claim from association alone. An earlier sealed planning note cited the pending tracker branch; that provenance was corrected additively before this follow-up.

Each pair was reviewed against its own source and partner. Nine rows are refined to binding-only classes: TRIM27, TRIM23 and construct-scoped MID2-2 to ubiquitin protein ligase binding; both IKZF1 rows and MEOX1 to DNA-binding transcription factor binding; KIFC3 to kinesin binding; KRT40 and SPAG5 to cytoskeletal protein binding. Nine positive associations remain non-core: both GOLGA2 rows, both ZBTB5 rows, KRTAP10-8, CALCOCO2, both RINT1 rows and AGMAT. TINF2 remains UNDECIDED because its individual screen hit could not be recovered and complete original evidence was unavailable. No current matching record is not contrary evidence.

The [source and assay guide](DCX-source-evidence.yaml) supplies exact interaction IDs, public source links, partner identities and term-definition checks. The 99 IntAct and 3 MINT target records include 45 literal records for 18 pairs. Screen, array and validated-Y2H records are phases of one study, not independent publications; aggregate orthogonal validation is not attributed to each DCX pair. PMID:31515488 tests a RINT1 position-660 variant with no interaction effect recorded, not a DCX mutation or a negative edge. BioPlex records are cell-specific AP-MS associations and do not establish direct binding. The MID2-2 screen and array records specify residues 21–705; the validated record has no feature annotation. Its sequence retains the RING domain, but construct catalytic activity and DCX substrate status are not inferred. The IKZF1 record’s “DCX” ubiquitin-ligase acronym is not doublecortin. AGMAT’s corrected guanidino-acid-hydrolase identity does not turn an AP-MS edge into direct enzyme binding.

All 40 pre-existing source dictionaries (39 imported plus the separate existing NEW row), all 21 other reviews, the original 26 references, the description and the single core function are unchanged. The new guide is the only added reference. No new annotation or provider research was generated, and no original cache was edited. These bounded interaction decisions are not additional core-function assertions or completion credit.


## 2026-10-17 source-audit successor

ROOT review prompted an additional partner-class assessment for both GOLGA2 interactions. GO:0005519 is binding to a protein that modulates cytoskeletal reorganization, and its typed parent is GO:0008092. Primary GM130 studies support that class through TPX2-dependent microtubule nucleation and microtubule capture/bundling. The two Y2H rows are therefore refined to cytoskeletal regulatory protein binding. This corrects the prior follow-up’s incomplete consideration of narrower terms; no Golgi or spindle activity is assigned to DCX.

ROOT also authorized inspection of the three remaining electronic removals, preserving the other18 annotations and the existing core. Current InterPro2GO and target model matches establish that IPR017302 is the specific chordate DCX family (PIRSF037870, target1–365), not a broad RP1 assignment. Axoneme assembly and retina development remain UNDECIDED because actual target participation was not resolved. Rat retinal expression in PMID:12752371 does not establish a required developmental step, while cortical phenotypes do not exclude retinal biology. Intracellular signal transduction is retained as non-core: PMID:22367209 provides mouse DCX signaling evidence beyond phosphorylation alone, with downstream Rac1 readouts and phosphomutant association with Asef2. Mouse constructs and mutant/heterologous assays are not mislabeled as native human experiments or direct GEF activity. Structured propagation source comments now distinguish verified matches/mappings from unresolved process scope.

The combined review has40 unchanged source identities,11 ACCEPT,13 MODIFY,12 KEEP_AS_NON_CORE,3 UNDECIDED and the1 pre-existing NEW. There are no REMOVE actions. Nineteen binding decisions plus three electronic decisions have been assessed; the remaining18 reviews, description, products, provider output and core are unchanged. The earlier follow-up entry above is preserved as dated provenance and is superseded only where this entry explicitly revises it. The guide links all new evidence, including the limited original-access scope.


## 2026-10-17 validation and status

Ordinary validation and term validation pass with seven generic-binding warnings for retained non-core source rows 7, 11, 13, 16, 20, 21 and 22. These individually assessed positive interactions follow the [explicit ClinGen project instruction on main](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions). No more specific function was inferred merely to suppress warnings. The ordinary status computation reports DRAFT because of these warnings; the previous COMPLETE scalar is updated to DRAFT without changing any scientific review, core or source identity. No annotation remains PENDING.

The missing PMID:12752371 and PMID:22367209 records were fetched through the ordinary publication fetcher in the isolated workspace. Both caches report abstract-only availability. The separately recovered indexed original Methods/Results/Discussion for PMID:22367209 remain the basis of the scoped source analysis; a failed direct full-text fetch is not mislabeled as a successful original download. Existing publication caches remain unchanged.


## 2026-10-17 review clarification: binding context and original-source locators

This entry preserves the earlier journal and clarifies the current decisions after PR #5085 review. The initial 9 MODIFY/9 non-core interaction count was superseded by the source-audit entry: the current nineteen interaction assertions comprise 11 MODIFY, 7 KEEP_AS_NON_CORE and 1 UNDECIDED. This follow-up changes reasons and evidence presentation, with no action changes. The biological description, products, core, source identities and cached/provider files remain unchanged.

The refinements describe qualitative binding capacities supported by controlled binary assays and verified partner classes. Native neuronal coexpression, endogenous complexes, numerical binding stoichiometry and physiological consequences are unestablished. In PMID:25416956, the main-text Results paragraph on pairwise retesting reports fresh yeast colonies, quadruplicate tests, at least three positive attempts and confirmed identity. Pooled-screen, array and validated-Y2H records are stages of that study. Its sampled orthogonal validation does not validate each DCX pair individually. PMID:21516116 separately documents fresh-transformant retesting and reporter/autoactivation controls. Tissue labels alone neither demonstrate a native complex nor establish that the proteins never meet.

The source guide now distinguishes literal MITAB identifier/method/PMID fields from reviewer summaries. Each recovered pair has an exact record anchor; the unresolved TINF2 assertion has no invented raw quotation. Electronic assertions quote literal InterPro2GO mapping rows, which establish source provenance rather than the biological validity of a process. The supported KRT40/SPAG5 binding classes remain MODIFY: the user's ancestry rule is explicitly for NEW process terms, while these are refinements of existing molecular-function assertions. They add no new core.

The [original GM130 study, PMID:26165940](https://pmc.ncbi.nlm.nih.gov/articles/PMC4506739/), Results Figures 4–6 and corresponding Methods, establishes TPX2-dependent microtubule nucleation and capture/bundling with controlled N74, mitotic HeLa extract and rat cell/Golgi experiments. This supports the GOLGA2 partner class, not a DCX Golgi or spindle mechanism. PMID:19242490 remains an abstract-only supporting read.

The [original DCX signaling study, PMID:22367209](https://pmc.ncbi.nlm.nih.gov/articles/PMC3339951/), Results subsection on Gs-PKA signaling and Figure 6B, reports shLuc/shDCX1 in neuronal progenitors, PACAP treatment and active Rac1 measured by GST-PAK-CRIB pulldown. This is the source of the knockdown statement; Figure 6C–E separately concerns mutant/heterologous Asef2 experiments. The normal publication cache remains abstract-only, while these original sections were separately recovered and read. Mouse constructs, mouse neuronal progenitors and heterologous hosts do not establish a native human mechanism. Signal transduction remains non-core, with no GEF or exact adaptor function inferred.

Axoneme assembly remains UNDECIDED. The current source is the full-length-matching DCX family IPR017302, not a demonstrated RP1 transfer; the particular mapping's experimental rationale remains unresolved. Microtubule binding and neuronal localization neither prove nor contradict axoneme participation. The general UNDECIDED definition permits unresolved biology; inaccessible papers are a required use case, not its sole meaning. No negative axoneme experiment is claimed.

The new provenance session should describe these reason, locator and source-anchor changes. Existing history and earlier note entries remain intact; this follow-up does not claim that the description or core was edited.
