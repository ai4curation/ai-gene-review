# Arginine biosynthesis: comparative audit

## 2026-10-26 — boundary, literature and member plan

This audit reviews the glutamate-to-arginine pathway through acetylated ornithine, including linear acetyl-CoA initiation/deacetylation and cyclic acetyl-group recycling. It does not equate this reaction template with universal pathway completeness in bacteria, archaea, fungi or plants. LysW-, succinylated-intermediate and acetylcitrulline routes require separate implementations.

The original module contains 39 unique bacterial/fungal representatives: 19 fungal reviews, ten existing Pseudomonas putida reviews and ten missing bacterial reviews now being seeded normally by verified accession. Literature-driven plant and archaeal exemplars are being identified so that the stated taxonomic scope has informative positive and negative mechanistic anchors.

Normally fetched comparative reviews are PMID:17347518 (microbial enzyme/pathway evolution), PMID:16122935 and PMID:26284079 (plant arginine pathways), PMID:19720555 (plant PII regulation), and PMID:37358082 (host/microbe metabolic context). These guide primary-source retrieval; review-level summaries do not turn individual homologs into experimentally characterized enzymes.

### Acetyl donor and ArgJ specificity

PMID:10931207, Marc et al., DOI https://doi.org/10.1046/j.1432-1327.2000.01593.x, compares purified ArgJ proteins and complementation. Methanocaldococcus jannaschii ArgJ catalyzes acetylornithine-dependent recycling but lacks detectable acetyl-CoA-dependent initiation under the tested conditions. Thermotoga neapolitana and Geobacillus stearothermophilus ArgJ catalyze both. The publisher full text was accessible; the first normal PMID-cache request failed HTTP429 and will be retried. Do not create a synthetic publication cache.

Normal UniProt REST lookup establishes Q57645 / ARGJ_METJA / argJ MJ0186 / NCBITaxon:243232 as the archaeal exemplar. Its eventual presence in a recycling family must not put it in the acetyl-CoA initiation variant. The historical name glutamate N-acetyltransferase can obscure donor specificity: distinguish GO:0004042 acetyl-CoA initiation from GO:0004358 acetylornithine recycling using current definitions. Individual gene reviewers are checking inherited rows rather than changing fetched term IDs.

### Fungal architecture and localization

PMID:12603335 resolves the earlier metabolon uncertainty: the ascomycete-specific N-acetylglutamate kinase portion supports NAGS activity/protein stability, whereas the reductase component is dispensable for that requirement. The Arg5,6 polyprotein and processing evidence (PMID:1649049) do not make both processed enzymes obligatory NAGS structural components. PMID:9428669 supports only modest Arg7 bifunctionality, with overexpression-dependent complementation; do not transfer its exact kinetic capacity to fission-yeast Aga1 from a family label.

Cytosolic budding-yeast versus mitochondrial fission-yeast ornithine carbamoyltransferase requires separate compartment and transport qualifications. Nitrogen excretion phenotype alone cannot refute a urea-cycle term: its actual reaction definition and native arginase context must be checked.

### Plant sampling

The plant review PMID:26284079 identifies experimentally supported NAGK and TUP5 as useful anchors. PMID:28294536 supports plastid-localized Arabidopsis NAGK, bacterial complementation and native mutant phenotypes. The TUP5 primary study (https://pmc.ncbi.nlm.nih.gov/articles/PMC3585585/) supports chloroplast localization, yeast complementation and reduced arginine in the native mutant. At2g37500 acetylornithine acetyltransferase was explicitly uncharacterized in that review, so it cannot be described as a direct biochemical anchor without newer evidence. Arabidopsis NAGS1/2 homology and tomato NAGS overexpression must retain their different evidence levels.

### Workflow and validation

Individual reviewers preserve all existing machine-sourced annotation payloads, document provider authentication/quota failures honestly, and use normal publication caching plus manual source research. Every reviewed member needs validated history and rendered review. Module revision, family verification, expanded exemplar reviews and full validation remain in progress; this module is not complete merely because its original fields were populated.

Added short-NAGS exemplar MYCTU ArgA/Rv2747 O33289, expanding the planned panel to43. Primary PMID15838030 measures glutamate acetylation but no saturation at600mM and stronger glutamine turnover. Its acetyl-CoA Km150micromolar is from the glutamine assay; the UniProt150mM transcription is not propagated. FamilyPTHR43626 is broad and explicitly function-restricted. Native efficiency and proposed partner/fusion architectures remain qualified. Primary PMID10753950 distinguishes Arg7 pre-import autoproteolysis from Arg5,6 import-dependent processing. All nine pathway connections now carry source-specific evidence; final family/source/member grounding and independent QA remain pending.


## 2026-10-26 independent final scientific QA

Checked every declared family/member pair against the normally fetched UniProt records: all 43 unique representatives match their asserted NCBIfam/PANTHER classifications. PANTHER labels were also checked against the committed ontology; broad short-NAGS and CPS family descriptors remain function-restricted. PAINT PTN000597373/GO0003991, PTN000241318/GO0003992 and PTN000172504/GO0004055 match the actual local IBD rows; the aminotransferase node is bacterial and does not itself establish fungal pathway usage.

Read the actual three cached GO-CAM YAMLs. The SGD arginine model has10activities, all cytosolic, two GO0103045 assignments to ARG2/ARG7, and one ARG7 recycling-to-kinase causal edge. The citrulline model has2activities. SGD:S000217863 is CPX579. The pombe model has12activities with the listed compartment split, modeled SPBC365.16 citrulline export, arginyl-tRNA ligase and arginine import. Its modeling choices are distinguished from direct transport assays; source-model wording was preserved as modeled where appropriate.

Verified all nine graph edges as chemical ordering or substrate supply, without direct channeling or universal co-location claims. The optional CPS side input and ArgJ return edge preserve linear-route satisfiability. ArgJ initiating/recycling selectors have distinct donor requirements; METJA and PSEPK recycling exemplars are not allowed to prove initiating capacity. MYCTU short-NAGS kinetics remain substrate-specific (primary15838030), and no full archaeal pathway or ArgH fusion is inferred from a partial exemplar.

Corrections: PMID17347518 does not establish type1/type2 reductase classification. Replaced that evidence statement with primary1406250 native/heterologous complementation plus the actual P54894 TIGR01851 classification. ArgA is now explicitly compatible with either downstream release route. Replaced evolutionary 'unrelated' wording with the source's bounded absence of detected similarity/distinct architecture. Scoped fungal claims to represented systems. Replaced a title-only evidence claim for inaccessible200419 with a bibliographic lead, and grounded pombe CPS localization in the curated arg4 record rather than claiming that primary text was inspected. No source cache was hand-edited and no member targets were added during QA.
