# ABCA3 evidence review

## 2026-09-25 — initial human review

Human ABCA3 is UniProt Q99758, a 1,704-residue full ABC transporter. The review preserves all 82 seeded annotation rows and their machine-supplied fields. The two seeded alternative products are retained; the evidence does not justify assigning separate isoform-specific core functions. The main function is ATP-dependent lipid loading at the alveolar lamellar-body limiting membrane, with phosphatidylcholine the clearest human cellular substrate. The annotation-reviewer and core-function-synthesizer workflows were applied to the whole set.

`just fetch-gene human ABCA3` created the source records and review stub. Publication caching ran concurrently with Falcon research. The genuine Falcon report completed in 540.82 seconds with a 1,200-second wrapper limit; the report and original artifact are retained unchanged. Perplexity was not retried because the earlier project attempts had established an unchanged quota failure. The report was treated as a literature guide and checked against primary sources. In particular, its statement that the ABCA3 processing protease is unknown is incomplete: the primary cathepsin study identifies CTSL and a smaller CTSB contribution [PMID:27031696]. No provider file was hand-written.

## Main evidence and its limits

- Native human lung immunoelectron microscopy places ABCA3 predominantly in the limiting membrane of lamellar bodies [PMID:11718719, *ABCA3 is a lamellar body membrane protein in human lung alveolar type II cells*]. LBM180 identification independently establishes ABCA3 identity and location [PMID:11940594]. These support GO:0097233 as the principal core location. The minority plasma-membrane observation attached to the 2001 paper needs its original full text; its IDA row remains UNDECIDED, rather than being rejected because the abstract emphasizes lamellar bodies.
- Human ABCA3 expression in A549 cells increases choline-phospholipid loading of LAMP3-positive vesicles, with impairment by the Walker A variant N568D [PMID:17574245]. ATP binding/trapping measurements distinguish catalytic defects from trafficking defects [PMID:16959783]. The latter paper's mutant ER retention is not assigned as a wild-type core location.
- TopFluor-PC uptake into ABCA3-positive A549 vesicles depends on incubation time, concentration, and ABCA3 variant state [PMID:28887056]. The original article was read in its entirety as reproduced in [Kinting's dissertation, printed pages 71–76](https://edoc.ub.uni-muenchen.de/25392/1/Kinting_Susanna.pdf). The authors explicitly acknowledge that vanadate inhibits other ATPases; mutation and cell-localization evidence provide additional support. The experiment measures lipid accumulation, not leaflet-resolved flux or aqueous-phase shuttling.
- Metabolically labeled choline phospholipids accumulate in ABCA3-positive vesicles; N568D and L1580P reduce intravesicular fluorescence without changing the outside signal [PMID:31473345]. Early choline-kinase inhibition and later transport inhibition are distinct experimental manipulations. The original abstract was read, with mechanistic corroboration from the author's [Li dissertation, discussion pages 58–66](https://edoc.ub.uni-muenchen.de/26783/1/Li_Yang.pdf). That dissertation is not mislabeled as the journal full text. The institutional journal-PDF URLs found through search redirected to HTML error pages and were not treated as recovered papers.
- Human purified ABCA3 ATPase measurements and cryo-EM structures support lateral lipid access and ATP-induced closure [PMID:35394827]. The lipid cavities, transport pathway, and directionality are structural proposals; the authors explicitly say they cannot resolve the substrate-binding site without a lipid-transport assay. Lipid density and copurified PC/PE do not alone establish translocation specificity. This is why the core uses the existing encompassing GO:0140326 rather than declaring a directly measured substrate-specific floppase.
- Human endogenous ABCA3 knockdown reduces vesicular lipid uptake and perturbs lamellar bodies, while ectopic expression induces lipid-filled lamellar-body-like structures [PMID:16415354]. The transporter therefore performs part of organelle assembly by delivering lipid constituents; this is stronger than inferring participation solely from knockout necessity. The same paper explicitly reports lysosomal and lamellar-body membranes. Endolysosomal trafficking annotations are retained contextually without equating a mature lamellar body with an ordinary lysosome.
- ABCA3 passes through multivesicular bodies and is proteolytically matured in MVB/LB compartments [PMID:20863830]. The full text of the cleavage study identifies cleavage after Lys174, CTSL knockdown effects, and cleavage of a synthetic ABCA3 peptide [PMID:27031696]. ABCA3 is the protease substrate; no NEW proteolysis annotation was added.
- The full publisher text of [the oligomerization study](https://www.spandidos-publications.com/10.3892/ijmm.2016.2650) was read [PMID:27352740]. BN-PAGE, gel filtration, co-immunoprecipitation and BRET support ABCA3 self-association. Higher-order mass estimates require detergent/dye corrections, and the relationship between oligomerization, ER exit and transport remains unresolved. GO:0032464 positive regulation of protein homooligomerization is refined to GO:0051260 protein homooligomerization. No independent core regulatory activity is asserted.
- Human macrophage ABCA3 knockdown increases radiolabeled miltefosine accumulation, and imaging supports a cell-surface location in resting macrophages [PMID:26903515]. These support a real, non-core xenobiotic-efflux function. The earlier cloning paper merely speculated about xenobiotic resistance [PMID:8706931]; its response annotation is retained using the later direct evidence.
- ABCA3 expression reduces free cholesterol and activates SREBP in an epithelial-cell model [PMID:25817392]. That supports secondary cholesterol homeostasis/efflux but does not itself establish purified cholesterol translocation. The separate phosphatidylcholine-metabolism regulation row remains UNDECIDED because the accessible abstract does not resolve its specific evidence.
- Patient-derived and genetically corrected human iAEC2 models show impaired surfactant secretion and variant-dependent trafficking and lamellar-body defects [PMID:38226623]. The full methods/results/discussion were inspected. Downstream inflammatory and progenitor phenotypes are not added as direct core functions. Human recessive surfactant-deficiency evidence supplies the Mendelian context [PMID:15044640].

## GO meaning and source tracing

Live QuickGO definitions were checked on 2026-09-25. GO:0140345 phosphatidylcholine flippase activity specifies **exoplasmic-to-cytosolic** movement. GO:0090554 phosphatidylcholine floppase activity specifies the opposite direction. ABCA3 cellular vesicle loading and its structural export model favor the latter overall direction, but the cited experiments do not directly resolve leaflet-specific PC flux. The two flippase rows are therefore MODIFY to existing GO:0140326, avoiding both the opposite-direction term and a claim that floppase direction was directly assayed. The validation ontology calls GO:0140326 “ATPase-coupled intramembrane lipid transporter activity,” whereas the fetched GOA and live QuickGO response use “carrier activity”; source-row labels are preserved and authored labels follow the validator ontology.

GO:0120019 phosphatidylcholine transfer activity specifically describes protected passage through an aqueous phase between lipid surfaces. It does not describe the measured integral-membrane ABCA3 ATPase mechanism, so its row is also refined to GO:0140326. No new substrate-specific term is needed.

The PC/PG metabolic-process definitions concern chemical reactions and pathways. Mouse lipid-depletion experiments measure altered phospholipid abundance and composition; those rows are refined to phospholipid homeostasis. Human uptake assays measure movement into vesicles; those metabolic/regulatory rows are refined to phospholipid transport. The experimental measurements are retained, without converting a transport phenotype into a claim of direct PC/PG chemical synthesis or degradation. The conditional mouse study does support secondary biosynthetic/transcriptional feedback, retained as non-core regulation [PMID:20190032].

All 33 IEA/IBA/ISS rows include explicit propagation sources. PAINT rows are traced to PANTHER:PTN000442469, not evaluated by donor count. ABCA3 appearing among its own descendant experimental evidence is legitimate and is not called circular. Domain, EC, ARBA and Swiss-Prot localization mappings were assessed against direct human evidence.

Live QuickGO donor queries verified mouse UniProt Q8R420 and rat UniProt A0A0G2K1Q8:

| Transferred assertion | Primary donor evidence | Assessment |
|---|---|---|
| Lung development | PMID:17540762; PMID:20190032 | Developmental consequences, non-core |
| Surfactant homeostasis | PMID:17142808; PMID:17267394; PMID:17577581 | Conserved direct lipid-supply role |
| PC/PG metabolism | PMID:17267394; PMID:17142808 | Lipid depletion supports homeostasis, not substrate chemical catalysis |
| Regulation of lipid transport/biosynthesis; phospholipid homeostasis | PMID:20190032 | Retain measured feedback as non-core; homeostasis is core |
| Organelle assembly | PMID:17540762 | Corroborated by human gain/loss evidence, PMID:16415354 |
| Glucocorticoid response | Rat IEP, PMID:15369786 | Expression response, non-core |
| Positive vesicle fusion | Rat IMP, PMID:15904872 | UNDECIDED; original ABCA3 experiment unresolved |

The rat fusion source abstract describes annexin A7, but that does not establish that the full text lacks ABCA3 experiments. Publisher access was unsuccessful. No misattribution or wrong-gene assertion is made. Similarly, PMID:22673903 includes human-muscle validation as well as rat-organ phosphoproteomics; the ABCA3-specific supplemental compartment assignment was not recovered, so that source-specific EXP row is UNDECIDED.

The tear-proteomics [publisher Table I](https://www.spandidos-publications.com/10.3892/or.2012.1849) explicitly lists ABCA3_HUMAN [PMID:22664934]. Extracellular detection is retained as non-core and does not establish soluble secretion. The blood-brain-barrier proteomics study detects ABCA3 in hCMEC/D3 cells, not in the compared primary human brain microvessels [PMID:23137377]; its plasma-membrane annotation remains non-core.

The Reactome normal and defective ABCA3 events were read. Disease-variant failure of transport does not negate wild-type lipid-carrier activity or lamellar-body location. The broad ABC lipid-homeostasis pathway provides context; primary ABCA3 assays provide specificity. No ABCA3/Q99758 entries were found in the local GO-CAM index. No NEW annotations or redundant ancestor/descendant process assertions were added.

## Completion checks

The first complete review contains 39 ACCEPT, 23 KEEP_AS_NON_CORE, 16 MODIFY and 4 UNDECIDED decisions. Source-specific uncertainty intentionally produces different actions for three repeated GO terms: plasma membrane, cytoplasmic-vesicle membrane, and regulation of PC metabolism. These distinctions should not be flattened merely to silence consistency warnings. All original annotation fields were compared with the seeded YAML and preserved. Targeted validation, rendering, history validation and PR results are recorded in the curation history.

## PR #3134 review follow-up (2026-09-26)

The reviewer correctly identified that tear-fluid proteomic detection is insufficient to retain a physiological extracellular location: change this HDA assessment to MARK_AS_OVER_ANNOTATED. The publisher Table I does explicitly contain ABCA3_HUMAN; its short row and URL are now attached as full-text support because the cached article omits that table. No cache was edited. The requested late-endosome consistency change was already present at submitted head 57ea574: both GO:0005770 and GO:0031902 are KEEP_AS_NON_CORE, so no action change is warranted.

Added direct PMID:17574245 support to its transport row, source-specific location rationales, and explicit Reactome reference assessments distinguishing pathway-level ER-to-lamellar-body language from a molecular interorganelle transfer assay. Free-cholesterol reduction in PMID:25817392 cannot alone distinguish sequestration from efflux to an acceptor; this is now explicit. Existing phospholipid homeostasis is included in the core synthesis. No new process annotation or proposed ontology term is needed: organelle assembly plus the alveolar lamellar-body membrane location already conveys the supported role. Final counts are 39 ACCEPT, 22 KEEP_AS_NON_CORE, 16 MODIFY, one MARK_AS_OVER_ANNOTATED and four UNDECIDED.

## 2026-09-27: post-merge source13 and bibliography follow-up

The original full audit was merged in PR #3134. Its 82 source assertions, all annotation actions, two alternative products, description, questions and single integrated core remain unchanged. Fresh main `fba6fe56078f46c326f465ae5a68a9ac18a23422` has exactly the same seven gene/raw/provider blobs as the verified local publication base `39b086a55856ca2f2287036a5ab43280add1ee90`; canonical and four historical/alias title searches found no open review. The follow-up includes four exact normal source13 cache records. Twenty-five already-published PMID caches, three Reactome records and both original history records were absent from this workspace and were restored exclusively from verified main blobs, without overwriting or refetching them. Those restorations are not new publication changes.

### Actual recovered evidence

- [PMID:22068586] is an abstract-only normal cache, independently checked against [PubMed and its figure captions](https://pubmed.ncbi.nlm.nih.gov/22068586/). The 47-child cohort and D253H/T1173R cellular experiments support disease and variant context. Figures 5 and 7 explicitly identify A549 cells; the cached abstract does not specify the expression host, and no full Methods section was newly recovered. Abnormal lamellar bodies and mutant-associated IL-8 production do not establish a new normal ABCA3 substrate or intrinsic inflammatory activity. Independent peer reading confirmed this scope.
- [PMID:26295388] has an actual XML body, including the structural-analysis and conclusion sections. It is a 2015 mini-review with preliminary predictions and a partial Phyre2 model using a *Caenorhabditis elegans* P-glycoprotein template. Its comparison with ABC domains in other organisms is not an experimental human ABCA3 structure or transport assay. The historical lack-of-structure discussion does not displace the existing 2022 human cryo-EM evidence.
- [PMID:36808083] has Methods, Results and Discussion in the restored record. The retrospective Kids Lung Register cohort selected 44 biallelic patients surviving beyond one year from 79 registered patients. Twenty-one of those survivors had neonatal onset. Sparse longitudinal observations, survivor selection and partly predicted variant classes bound interpretation. The investigators could not reliably estimate treatment effects; this is natural-history evidence, not proof of a drug effect or new transporter chemistry.
- [PMID:38203821] is a full-body review of several surfactant genes, developmental pathways and candidate treatments. Its therapeutic section discusses SFTPB replacement in surfactant-protein-B-deficient mice; that is not an ABCA3 gene-therapy experiment. ABCA3 trafficking and disease summaries are useful context but do not independently assign new molecular functions or establish clinical efficacy.

### The two DOI-only provider works

The official LMU records and linked original PDFs were read on 2026-09-27. A dissertation has its own identity; a related journal article is not substituted for the entire thesis.

1. [Xiaohua Yang, *Quantifying ABCA3 deficiency and ABCA3 variant-specific response to hydroxychloroquine*](https://edoc.ub.uni-muenchen.de/33410/) (2024; DOI 10.5282/edoc.33410) is a 27-page cumulative dissertation. Its public PDF contains background, contribution statements and summaries; printed pages 21–22 identify Paper I and Paper II but do not reproduce their full Methods/Results. The summary describes variant assays and retrospective HCQ-treated cases while retaining clinical uncertainty. These directly relevant component works are [PMID:37108718] and [PMID:37175887], newly resolved here rather than fabricated replacements for the dissertation.
2. [Yang Li, *Probe the transport function of ABCA3 by metabolic labelling of choline phospholipids*](https://edoc.ub.uni-muenchen.de/26783/) (2020; DOI 10.5282/edoc.26783) is an accessible 89-page dissertation. Methods, printed pages 27–29, specify the human ABCA3-HA construct and A549 host. Discussion pages 63–67 distinguish label synthesis, vesicle accumulation, mutant effects and limitations of the carcinoma-cell model. Miltefosine's other effects on membrane lipids and synthesis are explicitly acknowledged. This corroborates the existing bounded transport synthesis; it does not provide purified leaflet-resolved flux. The provider's pages 82–85 are bibliography pages, not the experimental passages. The separate journal article [PMID:31473345] retains its own abstract-only cache and source identity.

[PMID:37108718] was verified at [PubMed](https://pubmed.ncbi.nlm.nih.gov/37108718/) and its public [PMC body](https://pmc.ncbi.nlm.nih.gov/articles/PMC10141231/). Results, Discussion and Methods 4.1–4.5 combine HA-tagged ABCA3 A549 measurements with prior heterogeneous assays and patient data. Vesicle lipid readouts corroborate transport; the integrated score and clinical correlations do not establish a universal functional threshold or a new substrate. [PMID:37175887] was verified through the primary indexed [PMC body](https://pmc.ncbi.nlm.nih.gov/articles/PMC10179277/), including Results, limitations and Methods. WT/16 mutant A549 models and 39 retrospective cases support variant-dependent cellular HCQ responses, with uncontrolled treatment, co-medication and compound-heterozygote extrapolation limiting clinical inference. Neither study changes the retained annotation decisions. A single normal two-ID fetch returned exit 1, 0/2 records, with DNS errors; both caches remain required and the follow-up remains DRAFT.

### Evidence representation and complete citation census

The public tear-proteomics [Table I](https://www.spandidos-publications.com/10.3892/or.2012.1849) was reread: its row identifies `ABCA3_HUMAN` / `ABCA3` as human ATP-binding cassette sub-family A member 3. The local XML record contains the study body but omits that table cell. The annotation retains the primary PMID and its existing over-annotation decision; an ordinary exact cached quote describes pooled tear sampling, while the target identification is explicitly attributed to this external table. The old special full-text field is removed because public accessibility alone does not justify a field reserved for full text that cannot be shared. No quote is routed through this notes file as surrogate primary evidence. This also supersedes the earlier notes sentence calling the tear row non-core: the published final decision was already MARK_AS_OVER_ANNOTATED.

For [PMID:27352740] and [PMID:28887056], `full_text_unavailable` now reflects their abstract-only normal caches. The original external publisher/full-paper-in-dissertation reads remain explicitly distinguished. The latter paper is reproduced in the previously inspected [Kinting dissertation, pages 71–76](https://edoc.ub.uni-muenchen.de/25392/1/Kinting_Susanna.pdf); that document is an access route to the identified journal paper, not an invented PMID or a newly recovered cache. All original source IDs and fetched titles remain unchanged.

The recursive census includes the YAML, complete notes, genuine Falcon report and its nested artifact, decoded DOI/PMC URLs and title-only bibliography. The provider's repeated bibliography entries resolve to seven distinct journal works and the two LMU dissertations. Its title-only Open Targets platform citation resolves to [the database-methods publication](https://pubmed.ncbi.nlm.nih.gov/39657122/) (DOI 10.1093/nar/gkae1128); it credits the search service and supplies no ABCA3-specific experimental evidence, so it is explicitly excluded from the biological cache requirement. Unused bibliography inside external dissertations and source articles is not recursively promoted into new gene citations. The two component articles above are included because they are the actual works underlying the dissertation's substantive variant/HCQ summaries. At this checkpoint all previously required references are cached, and the only new required PMID gaps are the two failed normal requests. No DOI-only dissertation is represented as a missing PubMed record, and no provider or source file was rewritten.

## 2026-09-27 — PR #3303 evidence-attachment follow-up

The current published head was checked before editing. All 82 source assertions
and actions, the integrated core and two alternative products are retained.
This follow-up removes the off-topic pooled-tear sampling quote from the
[PMID:22664934] annotation while preserving its direct primary reference and
the explicit externally read identification evidence. The local record contains
article body sections, but omits the ABCA3 table cell; its general sampling
sentence cannot substitute for that target-specific result.

A fresh direct read of the [publisher article](https://www.spandidos-publications.com/10.3892/or.2012.1849)
on 2026-09-27 locates the row in **Table II**, captioned *Proteins identified
from tear proteomes of CA and CTRL*. It lists `ABCA3_HUMAN`, ATP-binding cassette
sub-family A member 3, Homo sapiens and ABCA3. The earlier Table I pointer is
corrected. Detection in pooled tear fluid is retained as evidence; the existing
`MARK_AS_OVER_ANNOTATED` decision addresses the stronger physiological
extracellular-location interpretation and does not deny the proteomics hit or
establish soluble secretion. The earlier note's shorthand about retaining
non-core detection does not replace that explicit annotation action.

The table is publicly accessible. No public-sharing restriction was established,
so absence from the normal extraction does not justify repopulating the special
`supporting_text_fulltext` field. The source is attributed directly to the PMID
and publisher URL, without using this notes file as an independent evidence
source. Previously verified identities for [PMID:37108718] and [PMID:37175887]
remain verified independently of cache presence. Their recovered normal records
now contain actual Results, Discussion and Methods; those sections were read
in the verified source20 staging area before import.


### Actual recovered variant-study evidence

[PMID:37108718] combines stable HA-tagged WT or patient-associated ABCA3 A549
experiments with prior heterogeneous assays and clinical data. The Methods
separate calnexin/CD63 localization, glycosylation and cleavage from vesicle
volume and lipid labeling. TopF-PC and propargyl-choline follow different
cellular routes; their accumulation is not a purified, leaflet-resolved flux
measurement. Earlier ATPase assays contribute to the integrated score. The
clinical correlation has discordant cases and a composite outcome that treats
transplantation as death, so no universal residual-function threshold is adopted.

[PMID:37175887] studies WT and 16 mutant ABCA3-HA A549 models with HCQ,
measuring morphology, cleavage, vesicle volume and lipid accumulation. The
variant- and concentration-dependent cellular effects are real, but no direct
HCQ binding to ABCA3 is measured. The 39 retrospective treated cases, a small
subset of an earlier blinded trial, co-medication and discordant outcomes are
kept distinct. Summing responses from separate variant cell lines is an
extrapolation for compound heterozygotes. These findings do not establish
general therapeutic efficacy or warrant a new molecular function or core.

Both primary PMC pages independently confirm the respective title, PMID and
DOI. The normal files contain full scientific sections with duplicate flattened
text; availability is not a claim that every supplementary table or raw dataset
has been recovered. The two dissertation identities and access boundaries above
remain unchanged. No source, provider report, source assertion, annotation
action or core function is rewritten.

### Source20 closure checkpoint

The root's verified source20 import supplied both normal files unchanged;
canonical bytes match the staged records and import receipt. The required
recursive census is now **34 PMIDs and four Reactome records, all present**.
This explicitly supersedes the earlier two-missing-cache checkpoint above.
The complete YAML, notes, genuine Falcon report and nested artifact were
rescanned, including decoded DOI/PMC links and the prior title-only bibliography
resolutions. The two independently identified LMU dissertations retain their own
access assessments; the unrelated Open Targets infrastructure citation remains
excluded for the stated reason. The recovered papers add no new annotation or
core. Published source assertions, actions, reference identities, two alternative
products, all provider/raw files and earlier history remain unchanged.

Target validation passed with three existing source-specific action advisories
(plasma membrane, cytoplasmic vesicle membrane and phosphatidylcholine-process
regulation). Those distinctions retain their evidence/access reasons. YAML
status remains DRAFT under the schema's no-warning COMPLETE rule; there is no
remaining required source-cache gate. History, exact cached quotations and
source preservation are checked separately.
