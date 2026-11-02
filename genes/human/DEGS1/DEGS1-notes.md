# DEGS1 (O15121) — curation notes

## Identity
- HGNC:13709; DEGS1 / DES1 / MLD / MIG15; "Sphingolipid delta(4)-desaturase DES1".
- 323 aa, ER multi-pass membrane protein; fatty acid desaturase type 1 family, DEGS subfamily.
- Three conserved histidine boxes (His box-1 89–93, box-2 128–132, box-3 259–263); di-iron center;
  cytochrome b5 / NAD(P)H electron-transfer coupled.

## Core function (well established)
- Catalyzes the FINAL step of de novo ceramide biosynthesis: introduces a 4,5-trans double bond into
  dihydroceramide (an N-acylsphinganine) to form ceramide (an N-acylsphing-4-enine).
  EC 1.14.19.17; Rhea:46544; O2- and Fe(II)-[cytochrome b5]-dependent.
- GO MF present in GOA and used for core_functions: GO:0042284 sphingolipid delta-4 desaturase activity
  (def matches UniProt catalytic activity / Rhea:46544). This is the exact current GOA MF term.
- BP: ceramide biosynthetic process (GO:0046513); sphingolipid biosynthetic process (GO:0030148).
- CC: endoplasmic reticulum membrane (GO:0005789), cytoplasmic (cytosolic) face; multi-pass.

## Key supporting evidence (verbatim-quotable)
- PMID:11937514 (Ternes 2002) — identified/characterized the human sphingolipid Δ4-desaturase
  (dihydroceramide desaturase); UniProt uses it for EC 1.14.19.17 catalytic activity.
- PMID:30620337 (Pant 2019, full text available) — "This enzyme catalyzes the insertion of a Δ4,5-
  trans double bond into dihydroceramide (DhCer) to convert it to ceramide (Cer), in the final step of
  the de novo Cer biosynthesis pathway"; "endoplasmic reticulum lipid desaturase DEGS1"; loss causes
  hypomyelinating leukodystrophy (HLD18); myelin development/maintenance role.
- PMID:30620338 (Karsai 2019) — "DEGS1, which catalyzes the last step in the ceramide synthesis
  pathway"; A280V patient variant reduces enzyme activity ~80%; increase in dihydro sphingolipid
  species; HLD18. IMP evidence for GO:0042284 and IMP for myelin maintenance.
- Reactome R-HSA-428259 "DEGS1 dehydrogenates dihydroceramide" — cytosolic face of ER; part of an
  enzyme complex with cytochrome b5 (Fe2+) refreshed by NADH.

## Secondary / moonlighting
- Retinol isomerase (isomerase-2) activity in retinal Müller cells (PMID:23143414; EC 5.2.1.-;
  GO:0050251 retinol isomerase activity, IDA). Genuine second activity but distinct from core de novo
  ceramide role; keep as non-core.
- Myristoylation (Gly-2) can retarget part of the enzyme to mitochondria and raise ceramide/apoptosis
  (PMID:19647031). Explains the mitochondrion / mitochondrial membrane localizations (secondary).

## Localization notes
- ER membrane is the primary/functional site (multiple EXP: PMID:9188692, 19647031, 30620338;
  Reactome; UniProt SubCell). GO:0098554 cytoplasmic side of ER membrane (IDA) is the specific
  is_active_in term — strongest CC.
- Mitochondrion / mitochondrial membrane (EXP PMID:19647031, 30620338; HPA IDA) — real but secondary,
  myristoylation-dependent; keep as non-core.
- PMID:1317856 is about serine palmitoyltransferase / 3-dehydrosphinganine reductase / sphinganine
  N-acyltransferase (upstream ceramide-synthesis enzymes) in mouse liver ER, establishing the cytosolic
  orientation of de novo sphingolipid-synthesis enzymes at the ER. Used as GO_REF source for
  DEGS1 ceramide-biosynthesis + cytosolic ER-face annotations by the curator (UOS_MCB). Abstract-only
  in cache; do not overrule the experimental curator — ACCEPT.
- Plasma membrane / specific granule membrane (Reactome R-HSA-6799350, neutrophil degranulation) —
  over-annotation from bulk granule proteomics; not a functional DEGS1 site. MARK_AS_OVER_ANNOTATED.

## Interactions
- PMID:32296183 (HuRI) — bare protein_binding IPIs with ARLN (Q8WVX3-2) and SEMA4G (Q9NTN9-2),
  high-throughput binary interactome; uninformative for MF. Per policy: MARK_AS_OVER_ANNOTATED
  (not REMOVE) for bare protein binding IPI.

## Other GOA terms adjudicated
- GO:0009055 electron transfer activity (TAS PMID:9188692) — DEGS1 receives electrons from cyt b5;
  it is the desaturase acceptor, not itself an electron-transfer carrier. Over-annotation / better
  captured by the desaturase MF. MARK_AS_OVER_ANNOTATED.
- GO:0006636 unsaturated fatty acid biosynthetic process (TAS PMID:9188692) — DEGS1 desaturates the
  sphingoid base of a ceramide, not free fatty acids; the sphingolipid/ceramide BP terms are correct.
  MARK_AS_OVER_ANNOTATED.
- GO:0006686 sphingomyelin / GO:0006688 glycosphingolipid biosynthetic process (IDA, UOS_MCB) —
  downstream complex-sphingolipid processes DEGS1 feeds via ceramide; defer to experimental curator
  but non-core. KEEP_AS_NON_CORE.
- GO:0006629 lipid metabolic process, GO:0016020 membrane, GO:0003824 catalytic activity — correct but
  generic IEA parents of more specific accepted terms. MARK_AS_OVER_ANNOTATED (too general).
</content>
</invoke>


## 2026-10-17 evidence reassessment

This appendix preserves the earlier notes byte for byte. It revises interpretations in the earlier record where newer source inspection supports a more precise conclusion. The original 40 annotation dictionaries and their source identifiers remain intact; the normal isolated fetch added supporting-entity metadata for rows0–11, which is retained in provenance rather than inserted into those historical dictionaries. Current GOA has43 records mapping to40 legacy identities. No new annotation or unreviewed alternative product is added.

The review now proposes17 ACCEPT,14 KEEP_AS_NON_CORE,4 TOO_GENERAL,4 UNDECIDED and1 MODIFY, with one consolidated desaturase core and25 references. The historical pair labels, generic-term exclusions and ER-only objections in the earlier prose are superseded by the individual decisions and [evidence guide](DEGS1-evidence-guide.md).

The two HuRI protein-binding rows are retained as non-core after exact IntAct pair verification to ARLN Q8WVX3-2 and SEMA4G Q9NTN9-2. The original main Methods describe quadruplicate retesting and sequence confirmation. No supplementary threshold, native stoichiometry or pair-specific orthogonal validation is claimed. No narrower DEGS1 activity is established merely by the partners' regulator or semaphorin classes. This follows the [explicit project instruction](https://github.com/ai4curation/ai-gene-review/blob/9db646fd420946e2c8a9f325be9cd5b62b2c3d4c/projects/CLINGEN_MENDELIAN.md#curation-instructions); it is a scoped user instruction and does not alter repository-wide policy.

The four TOO_GENERAL decisions replace unsupported over-annotation language for true generic assertions already entailed by more specific retained terms. The existing useful sphingolipid pathway description remains accepted. The current electron-transfer definition includes electron acceptors and enzymatic redox transformations, so being an enzyme rather than a mobile carrier is not a valid exclusion. The historical fatty-acid-biosynthesis description is refined to ceramide biosynthesis using actual human sphingoid-backbone chemistry, without asserting wrong-gene attribution in an inaccessible original.

The one core represents the N-acylsphinganine delta-4 reaction, ceramide biosynthesis and ER membrane. Direct human expression evidence comes from [PMID:11937514](https://pubmed.ncbi.nlm.nih.gov/11937514/); cellular disease evidence and actual Methods/Results were separately read for [PMID:30620337](https://www.jci.org/articles/view/123959) and [PMID:30620338](https://www.jci.org/articles/view/124159). Whole-cell lipid hydrolysis is not purified free-sphinganine turnover. Small human/fly/fungal hydroxylated signals in the heterologous study prevent an absolute no-hydroxylase claim. The separate original sources supplement, without rewriting, the existing publication caches.

Human [PMID:36951944](https://pubmed.ncbi.nlm.nih.gov/36951944/) supports ER–mitochondrial contact-domain enrichment. Its changes in phospholipid metabolism, SOAT1 activity and contact geometry do not establish additional DEGS1 catalytic or tether functions. Human tagged imaging in PMID:30620338 reports strong ER and little Tim23 overlap, not absolute mitochondrial absence. The source-specific granule/plasma-membrane Reactome assertions have exact O15121 entity paths and remain non-core; the underlying proteomic peptide assignments were not independently audited. Mitochondrial and ER-contact signals are not silently equated with resolved membrane topology.

Retinol-isomerase activity remains positive but non-core. Original [PMID:23143414](https://pubmed.ncbi.nlm.nih.gov/23143414/) distinguishes human expression-cell/rescue evidence from chicken purified-enzyme and Müller-cell experiments. Later [mouse conditional deletion](https://pmc.ncbi.nlm.nih.gov/articles/PMC6436658/) and [zebrafish knockout](https://pmc.ncbi.nlm.nih.gov/articles/PMC7212626/) limit a universal physiological cone-visual-cycle requirement under their tested conditions. Residual expression, species, age and compensation prevent a universal negative inference. The open question asks where this biochemical activity makes a physiological contribution independently of sphingolipid changes.

The full originals for1317856,16120614,19647031,24209621 and9188692 remain unavailable after bounded attempts. Target-specific leaflet evidence from1317856/16120614, sphingomyelin IDA evidence from24209621 and plasma-membrane TAS evidence from9188692 are explicitly UNDECIDED. Broad functions independently established for DEGS1 remain supported with access limitations. No experimental annotation is removed because its abstract names another protein or omits the target. The exact species of the recombinant myristoylation constructs and detailed fractionation controls from19647031 are not invented.

Prior PR2032 and its author-authority human discussion remain historical context; no formal review is fabricated. Genuine research-provider attempts failed (Falcon authentication403 and Perplexity401/quota), so this reassessment uses direct primary and official sources with manual notes. No provider-named report was written. Newly fetched later visual-study caches are additive; original UniProt, GOA, publications and histories remain protected.


## Follow-up evidence clarification — 2026-10-17

The catalytic core remains the cytochrome-b5-dependent conversion of dihydroceramide to ceramide. Human DES1 expressed in yeast and patient-cell lipid measurements establish this chemistry; the latter measures cellular lipid conversion rather than purified free-sphinganine turnover [PMID:11937514; PMID:30620338]. Human fibroblast imaging and human brain fractionation support enrichment at ER–mitochondrial contacts [PMID:36951944]. The explicit cytosolic-face assignment in Reactome R-HSA-428259 now provides positive model corroboration for the older topology annotations; their original experiments remain inaccessible [PMID:1317856; PMID:16120614].

Plasma-membrane localization is retained as a contextual observation, consistently across the historical TAS and the explicit Reactome granule-exocytosis model. This does not reconstruct the unavailable 1997 assay or imply that plasma membrane is the dominant site of desaturation [PMID:9188692; Reactome:R-HSA-6799350]. Mitochondrial calls remain distinct from precise membrane-face claims, and the myristoylation paper's recombinant construct species and fraction-purity controls remain unresolved [PMID:19647031]. Public interaction, HPA and Reactome URLs and brief original-text anchors are in [the evidence guide](DEGS1-evidence-guide.md).

The broad electron-transfer annotation is retained non-core under the current definition, which includes enzymatic redox transfer. Cytochrome b5 is the donor partner and DEGS1 is the terminal lipid oxidoreductase; no separate carrier activity or electron-transport core is inferred. Retinol activity remains supported experimentally but its physiological role is limited by the mouse and zebrafish visual-cycle results [PMID:23143414; PMID:30645148; PMID:32238432]. Matched human structure-function experiments with product, folding and membrane-insertion controls could distinguish the two measured chemistries. This appendix supersedes the earlier uncertainty decisions for the two ER-face rows and the historical plasma-membrane row while preserving the older notes as written. The source-specific sphingomyelin assertion remains unresolved [PMID:24209621].


The four broad catalytic, lipid-metabolic and membrane rows now use MODIFY with their already-supported specific replacements, following the current curation instruction. This changes decision representation without adding a biological assertion: catalytic activity maps to sphingolipid delta-4 desaturase activity, lipid metabolism to ceramide biosynthesis, and the two membrane rows to ER membrane. The final counts are 19 ACCEPT, 15 KEEP_AS_NON_CORE, 5 MODIFY and 1 UNDECIDED across the same 40 sources.


## Quotation follow-up and current decisions — 2026-10-17

This dated entry supersedes the earlier evidence-reassessment paragraph that left the ER-face and historical plasma-membrane rows unresolved. Both GO:0098554 rows are ACCEPT, corroborated by the explicit DEGS1 reaction model in Reactome R-HSA-428259; both GO:0005886 rows are KEEP_AS_NON_CORE on contextual localization evidence. Their inaccessible original assays remain unverified. Only the source-specific sphingomyelin annotation from PMID:24209621 remains UNDECIDED. The current total is 19 ACCEPT, 15 KEEP_AS_NON_CORE, 5 MODIFY and 1 UNDECIDED across the same 40 source annotations. Earlier TOO_GENERAL wording has been superseded by MODIFY with the established specific replacements.

Short quotations are placed once where they support the claim directly: the core carries the Reactome ER-face statement, the official UniProt catalytic reaction and the PMID:36951944 MAM-enrichment observation. The electron-transfer row cites the PMID:23143414 cytochrome-b5 coupling statement; the existing positive retinol assay excerpt remains with that paper's retinol row. Other occurrences use reference-only support. Coupling to cytochrome b5 does not itself demonstrate a separate mobile-carrier role, and the accepted non-core interpretation is unchanged. The paper's species and assay limits remain explicit in the review and evidence guide.

The mitochondrial GO:0005739 row relies on the Human Protein Atlas target/antibody ICC/IF record, with GO_REF:0000052 and the official links in the evidence guide. Its former MAM excerpt has moved to the core because ER-contact enrichment does not by itself establish mitochondrial localization. HPA record inspection is not a new microscopy-image analysis.

All existing note paragraphs, including their historical spelling and spacing, are preserved byte for byte. This appendix supplies the current interpretation without rewriting the dated record. Quotation totals for the current review and newly authored guide remain at most 25 words per source; unchanged inherited notes are historical text, not newly repeated quotations. Source caches, source identities, actions, products and core biological assertions are unchanged.
