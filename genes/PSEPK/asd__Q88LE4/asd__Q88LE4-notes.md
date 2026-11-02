# asd PP_1989 curation notes

Q88LE4 has the strongest current annotation of the two PSEPK Asd-family
proteins: HAMAP and ARBA supply the NADPH-dependent reaction and UniPathway maps
it to lysine, methionine, and threonine biosynthesis. These are predictions,
not direct KT2440 enzyme assays. The generic NAD-binding annotation was not
treated as equivalent to the NADP-specific catalytic record.

The old preservation branch correctly identified this locus but supplied no
target-specific experimental evidence that changes the current assessment.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. A normal Falcon attempt returned HTTP 403 Failed to authenticate; no fabricated report was written. Manual literature and curated-source review supplied the fallback.

The canonical candidate is gamma-type Asd: HAMAP MF_02121, TIGR01745, Asd catalytic signature and assigned catalytic Cys135/His275 converge. UniProt states “Catalyzes the NADPH-dependent formation of L-aspartate-” with HAMAP support; the continuation describes semialdehyde formation. The record also warns “Lacks conserved residue(s) required for the propagation of” certain features. That caution is not silently discarded: it limits a complete residue-by-residue functionality claim, while the remaining family and catalytic evidence supports the inferred Asd activity. No purified PP_1989 assay was found.

NADP binding is catalytic and retained as core, without implying exclusive preference. The separate NAD-binding assertion remains UNDECIDED because a generic NAD(P) fold and NADPH-dependent function do not establish or exclude NAD use. Homodimer assignment is supported by HAMAP plus the dimerization domain, not a native assembly experiment. Broad amino-acid metabolism/biosynthesis and aldehyde oxidoreductase terms are refined. Existing lysine, threonine and methionine trunk assignments remain; the additional isoleucine attribution is too distal for the recovered native evidence.

The 2025 KT2440 engineering paper does not assay this locus. Its statement that E. coli ThrA replaces LysC, Asd and Hom is chemically overstated: bifunctional ThrA supplies aspartokinase and homoserine dehydrogenase, not Asd. It is not evidence for an Asd bypass.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.


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
