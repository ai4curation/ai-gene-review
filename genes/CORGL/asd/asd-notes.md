# CORGL asd research notes

## 2026-11-01 — shared semialdehyde branch point and donor specificity

P0C1D8 is the reviewed ATCC13032 Asd (taxon196627), a standalone protein. PMID:1980002 abstract describes a selected lysine-producing clone, complementation of E.coli asd mutants and increased Asd activity in C.glutamicum carrying high-copy asd plasmids. Exact support: “Plasmids carrying the C. glutamicum asd gene complemented Escherichia coli asd mutants.” Its 30–60-fold increase is a dosage phenotype, not unmodified native flux. PMID:1956296 independently anchors the lysC/asd locus to ATCC13032. These establish gene identity and activity; neither available abstract is a purified ATCC13032 NADH-versus-NADPH assay.

The reviewed target contains HAMAP MF_02121-supported NADPH-dependent reductive dephosphorylation, explicit NADP-binding sites and a homodimer assignment. NCBIfam TIGR01296 asd_B and InterPro Asd-specific domains distinguish this enzyme from a generic semialdehyde dehydrogenase. PTHR46278 has the broad official name DEHYDROGENASE, PUTATIVE-RELATED; its target subfamily SF2 is ASPARTATE-SEMIALDEHYDE DEHYDROGENASE. A name alone is not used to choose a family.

GO:0051287 explicitly means NAD+/NADH, whereas GO:0050661 means NADP+/NADPH (live QuickGO definitions saved in the ignored task log). The IPR000534 NAD-binding superfamily/domain association cannot establish a different cofactor from the target-specific Asd rule and multiple NADP-binding sites. Therefore the broad-domain NAD-binding row is MODIFY to the already retained NADP-binding term. This is not a claim that native NADH utilization was experimentally disproved. The enzyme's NADP-specific activity is accepted by conserved family inference plus native genetic/enzyme evidence, with the direct kinetics gap stated.

The intrinsic homodimerization annotation is accepted on the conserved Asd dimerization domain and curated family rule; no native oligomer measurement is claimed. General metabolic/BP and redox-class annotations are refined to supported specific functions. Asd chemically makes the common precursor for lysine, homoserine, threonine, methionine and threonine-derived isoleucine; those multiple process annotations are not duplicate evidence or separate enzyme activities. All14 seeded rows adjudicated; no NEW.

## Source acquisition and scope

Normal `just fetch-gene` generated the UniProt record, GOA export and seeded review. The 41 original rows across this five-gene panel and all ten raw files were snapshotted before curation. An initial folder-code misunderstanding was corrected to canonical CORGL; the five new folders were moved without changing raw bytes or machine annotation payloads. The original and migrated baselines and an explicit migration record are retained in `.cache/module-audit-logs/bacterial-threonine-corgl-20261101/`.

A normal Falcon research request failed with HTTP403 authentication failure. This is a provider failure, not a research report; no provider-named report was fabricated. The shared authentication failure was not repeatedly retried for the other four genes. The nonhuman MOD-description command was run for all five under canonical CORGL and reported no configured MOD provider. Research below is manual synthesis of immutable primary caches and the reviewed UniProt record.

No raw annotation was removed or rewritten. Ordinary relationship qualifiers played no part in the judgment. No NEW annotation was proposed: the original set and supported refinements already cover the supported biosynthetic functions. No unverified universal bacterial architecture or native production flux is inferred from recombinant protein or engineered production strains.

## Validation version boundary

Focused validation passes with one nonblocking ontology-label advisory: the bundled term validator expects the legacy label “aspartate-semialdehyde dehydrogenase activity” for GO:0004073, whereas the live QuickGO definition and current seeded GOA label explicitly say “aspartate-semialdehyde dehydrogenase (NADP+) activity”. The live result is saved in the ignored log. Machine labels and the current accurate authored label are preserved; no ontology cache is edited. The review remains DRAFT to reflect the warning.

### Final independent QA refinement

Refined the generic GO:0046983 dimerization row to GO:0042803 protein homodimerization activity using the existing curated HAMAP homodimer statement. This remains an inference, not a native stoichiometry assay. Final decisions: 9 ACCEPT and 5 MODIFY. Marked the completed review COMPLETE; the live-GO versus bundled-ontology Asd label advisory is nonblocking and does not represent unresolved biological review.


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
