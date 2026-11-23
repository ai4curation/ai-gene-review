# asd annotation-review notes

## 2026-10-26 complete native-function review

All 25 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

Native Asd is the NADPH-dependent reductive dephosphorylase of aspartyl phosphate. PMID:6102909 purifies the enzyme, identifies two identical/similar subunits, detects an acyl-enzyme intermediate and establishes stereospecific NADPH hydrogen transfer. PMID:14726201 tests cystine-mediated modification of catalytic Cys135; this is a reversible inhibitor mechanism, not evidence that Asd carries out cystine metabolism. PMID:11368768 gives integrated native pathway kinetics; UniProt records target-linked NADPH and substrate Km values.

NAD binding is not equivalent to physiological NAD preference. PMID:26662025 explicitly contrasts inefficient wild-type NAD utilization with engineered variants improving kcat/Km by 44/66-fold. Retain the weak existing NAD-binding claim as non-core rather than declaring no binding or attributing mutant behavior to wild type. Core remains NADP(H) dependent. PMID:11967071 is an expression-array response to mitomycin C, retained as non-core DNA-damage response rather than DNA repair; unavailable target-specific full tables were not used to overrule its experimental curation. All four downstream amino-acid branches are direct chemical pathway participation, not merely phenotypic necessity.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-asd-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

PMID:6102909 directly identifies an acyl-enzyme intermediate and pro-S hydride transfer from NADPH; PMID:14726201 maps cystine inhibition to catalytic Cys135; PMID:11368768 supplies pathway kinetics. NAD binding remains a limited secondary property: PMID:26662025 distinguishes inefficient wild-type NAD use from engineered 44/66-fold improvements. The DNA-damage annotation remains an expression response, not DNA repair catalysis.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.

## 2026-10-26 — source-specific PR #5569 follow-up

The remaining action-only refinement summaries and generic refinement reasons were replaced with reaction-, pathway- or assembly-specific explanations. Existing actions and replacement terms are unchanged. The cytosol row keyed to PMID:15911532 now quotes that paper’s actual fractionation/2D-gel/MS statement, instead of the different MC4100 study PMID:18304323. The abstract does not name the target hit; the native curator assignment is retained without pretending the original protein table was reinspected.


## 2026-11-01 bacterial aspartate-to-threonine audit follow-up

Re-read the existing COMPLETE review and every annotation decision for the narrower bacterial route audit. Retained all annotation actions, machine-sourced payloads, standalone description, core functions and raw records. Added manual assessments and verbatim findings to existing references, distinguishing native experiments from comparative synthesis, bibliographic-only records and inference. No new annotation rows were proposed.

Asd remains the obligatory intervening enzyme between aspartate phosphorylation and homoserine formation. It reduces aspartyl phosphate with NADPH, releasing phosphate and supplying the shared semialdehyde branch point. It does not itself perform homoserine reduction. PMID:6102909 reports that Asd "transfers the pro-S hydrogen from NADPH (class B dehydrogenase)." The native purified enzyme supports a homodimer, not an interenzyme complex.

PMID:26662025 says "neither the wild-type protein nor the available mutants could utilize NAD(+) efficiently." Improved NAD utilization and cascade homoserine synthesis concern engineered Q350N and Q350N/H171A proteins. Preserve the limited non-core NAD-binding claim, distinguished from a new NAD-dependent catalytic activity or equal native cofactor use. The measured-versus-functional activity policy does not equate detectable binding with physiological pathway flux. The DNA-damage expression row remains a non-core expression context, not DNA-repair chemistry.

Acquisition and evidence limits: `just mod-description-deep-research ECOLI thrA metL lysC asd thrB thrC` completed with all six skipped because no MOD provider is configured for ECOLI. A fresh normal Falcon request for ECOLI thrA failed with the shared Edison authentication/access 403; the same failed service was not retried for the other five. Earlier actual provider attempts remain documented above. No provider report was fabricated or rewritten. Manual review used existing primary-publication and curated UniProt caches. Logs are in the ignored `.cache/module-audit-logs/bacterial-threonine-ecoli/` directory.

PMID:11368768 supports the native route, but its nominal full-text HTML cache contains a duplicated abstract and PDF link rather than the full paper. The coordinating agent's normal PDF retrieval also returned an HTML interstitial. No unseen kinetic measurements or exact strain details are attributed to that abstract. Native proteomics annotations retain the caveat that individual target supplement rows were not independently reconstructed. Raw UniProt PANTHER membership and the official `interpro/panther/panther.obo` label were checked for module selectors; membership alone does not establish every family's substrate or regulatory specificity.


## 2026-11-01 PR #5858: distinguish shared precursor participation from distal process assignment

This follow-up reconciles ECOLI Asd/P0A9Q9, CORGL Asd/P0C1D8 and PSEPK Asd/Q88LE4. All original annotation payloads and raw records are preserved. No NEW annotation is proposed.

### Live ontology check

QuickGO and OLS were queried directly on 2026-11-01. GO:1901705 is current and defined as: "The chemical reactions and pathways resulting in the formation of L-isoleucine." Its immediate is_a parents are GO:0009067 aspartate family amino acid biosynthetic process and GO:0009082 branched-chain amino acid biosynthetic process. It does **not** explicitly begin at threonine. Accordingly, the reviewer's biochemical branch boundary is not presented as an ontology axiom.

GO:0071266 is current and defined as: "The chemical reactions and pathways resulting in the formation of L-methionine, the L-enantiomer of (2S)-2-amino-4-(methylsulfanyl)butanoic acid, from simpler components such as L-aspartate or L-homoserine. This process occurs in plants, bacteria, archae and fungi." Its immediate parent is GO:0071265 L-methionine biosynthetic process. The explicit inclusion of aspartate is decisive for the well-grounded shared Asd step. Both process terms descend from generic amino-acid metabolism/biosynthesis; neither is entailed by the separately retained threonine or homoserine process term.

Official endpoints: [Ile definition](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1901705), [de novo Met definition](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071266), [Ile direct parents](https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1901705/parents), [Met direct parents](https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0071266/parents). Raw responses, exact query URLs and HTTP statuses are retained in the ignored `.cache/module-audit-logs/bacterial-threonine-asd-round1/` acquisition logs.

### Comparator and GO-CAM check

Same-role comparator identities were checked from current UniProt records: B. subtilis Asd Q04797, M. tuberculosis Asd P9WNX5 and S. cerevisiae HOM2 P13663 (SGD:S000002565). Exact QuickGO query for GO:1901705 returned one InterPro IEA for each bacterial comparator and none for yeast HOM2. These bacterial rows repeat the same propagation mechanism as the three reviewed targets and do not independently establish experimental process membership. The all-annotation HOM2 query returned 38 rows, including SGD IMP threonine, homoserine and methionine terms (PMID:4380684), but no Ile term. For exact GO:0071266 the bacterial comparators carry UniRule IEA; yeast uses the broader GO:0071265, with curated IMP and RCA support. This is a scope/convention comparison, not scientific evidence quoted from GOA.

The local GO-CAM index was checked with both UniProt and MOD identifiers. UniProt-only search is insufficient for fungal records. `gocams/678073a900003175/678073a900003175-src.yaml` represents PomBase hom2/SPCC1827.06c Asd activity in homoserine synthesis. Yeast HOM2 occurs in homoserine/threonine models and `gocams/YeastPathways_PWY3O-954/YeastPathways_PWY3O-954-src.yaml` explicitly associates its Asd activity with methionine biosynthesis. No indexed Ile model assigns these same-role Asd proteins that process. This supports the bounded convention, without treating absence as proof of biological impossibility or fungal pathway architecture as identical to every bacterium.

### Decisions and evidence

All three original GO:1901705 rows are now MARK_AS_OVER_ANNOTATED, and the term is removed from ECOLI/CORGL broad-term replacement lists and core process assertions. This is conservative process scope, **not** a claim that Asd cannot supply carbon to isoleucine. PMID:19946135 describes the specific branch: "Isoleucine is best known to be derived from threonine in five steps, beginning with the formation of 2-ketobutyrate from threonine (catalyzed by threonine dehydratase)." Shared precursor supply plus repeated InterPro propagation was judged insufficient for a separate distal process claim; the curated fungal comparators and GO-CAMs support the nearer homoserine/threonine scope. The source also describes alternative isoleucine routes, so this boundary is not asserted universally across organisms.

All three existing GO:0071266 rows remain ACCEPT, as do their justified author-supplied refinement/core uses. Each target has a specific HAMAP MF_02121 CC:PATHWAY assignment to step 2/3 of homoserine formation from aspartate within de novo methionine synthesis. This is independent curated pathway support, not a GOA assertion cited as its own proof. The GO definition explicitly includes that starting material, and Asd performs the chemical reaction itself. Other inherited PSEPK NEW proposals are separate gene-specific decisions, not a blanket shared-precursor exclusion. PP_4473 has an untagged curated Swiss-Prot pathway statement, Hom has an ARBA-only pathway statement, and PP_0664 has a provider prediction with unresolved native function; it would be incorrect to describe all three as ARBA-only or lacking curated support. The coordinated follow-up restores the inherited PP_4473 de novo methionine proposal using its curated pathway statement, kinase chemistry and the live GO definition; the Hom ARBA-only and PP_0664 unresolved-native-role proposals remain retired. This is a gene-specific evidence distinction, not a rule against shared precursors. Row reasons make this distinction explicit. Restraint about creating an additional claim does not automatically reverse an independently supported existing process or bar its supported use in a core function.

No provider report or raw source was written or refetched. The existing full comparative publication and unchanged target curated records supply the biological evidence; official live APIs establish ontology and comparator state.
