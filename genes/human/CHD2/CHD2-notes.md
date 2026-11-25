# CHD2 review notes

## 2026-10-10 — original ClinGen campaign review

CHD2 was the literal unchecked catalog successor to CHCHD10 at authenticated intake main `f0516e241be255a82ed3124255d6200481c86a5e`. HGNC:1917, reviewed UniProt O14647 and the four HGNC aliases were checked against the complete open-PR path inventories, labels, current gene tree and publication queue. No overlap was found. There was no original gene review or notes prefix to preserve. All work for this proposal remains in the isolated TMP packet; ROOT handles publication and history.

The genuine normal fetch produced 32 source assertions, three alternative products and 14 reference identities. The raw GOA also contains 32 rows. The seed SHA-256 is `e84e849ba8a0647a8d21d7396b40b3d0ff26743eb2306015e70cd8f7d7a2a050`. Every original term, evidence code, reference, qualifier and supporting entity is preserved. PANTHER PTHR45623 was returned by the normal fetch; no family or ancestral node was guessed. Existing main publication, Reactome and family-cache bytes are retained exactly, and genuine fresh variants are archived separately. The fresh full version of PMID:29153328 was read without replacing its existing abstract-only main cache.

The default Falcon research attempt timed out after 90 seconds. The explicit Perplexity-lite fallback returned an insufficient-quota response. Both receipts are retained; no research report or provider prose was fabricated. These notes and the evidence JSON are manually authored primary-source analysis.

## Molecular synthesis and source-specific decisions

The defining activity is ATP-dependent chromatin remodeling. In PMID:25384982, purified human CHD2 expressed in Sf9 cells hydrolyses ATP and supports nucleosome assembly and remodeling with defined DNA, native Drosophila histones and NAP1. The D617A/E618A mutant and nonhydrolysable-nucleotide controls connect ATP hydrolysis to the observed work. Nucleosomal DNA accessibility, periodic arrays and supercoiling assays are distinct readouts. The tested domains also show that hydrolysis alone need not produce effective remodeling. This supports one molecular core, with ATP binding/hydrolysis and DNA/histone recognition as constituent capabilities rather than separate unrelated cores.

Rows 1 and 2 are refined from the original sequence-specific cis-regulatory DNA term to GO:0003690 double-stranded DNA binding. The official current definition and ancestry were retrieved. The exact mouse donor E9PZM4 has a promoter-binding IMP assertion from PMID:22569126. Its actual ChIP/re-ChIP and MyoD gain/loss results demonstrate targeted promoter association, but not an isolated CHD2 recognition motif. Human purified-protein duplex-binding experiments provide positive support for the replacement. This is a bounded specificity correction; it does not claim CHD2 is incapable of sequence preferences. The original source objects remain unchanged.

The mouse myogenic study also supports H3.3 association, Chd2-dependent H3.3 incorporation and actual myogenic differentiation effects with rescue. Those existing developmental assertions are retained non-core with mouse C2C12/NIH3T3 scope. Histone binding is retained as a substrate-recognition capability, without assigning autonomous histone-chaperone or histone writer/eraser activity. The current mouse gene-expression donor chain includes PMID:27783602. Its authentic Table S1 row 28 and Note S5 page 8 resolve Chd2 as the neighboring RNA readout after linc2025 promoter deletion, not the perturbed protein. The local cis mechanism is unresolved; independent CHD2 protein experiments support broad gene-expression involvement.

In PMID:26895424, PARP1-dependent CHD2 recruitment, local chromatin expansion, ATPase-dead controls and H3.3 incorporation connect the motor to a performed contribution at human DNA breaks. The source explicitly leaves direct H3.3 deposition versus cooperation with histone chaperones unresolved. Mouse telomere-fusion experiments have a different PARP1 dependency and are not silently generalized to the human laser setting. The review does not assign ligase, PARP or DNA-duplex-unwinding activity to CHD2. Existing remodeling and nucleosome-organization terms capture the established work; no new repair process is proposed.

The human interneuron study PMID:36115870 and human H3.1K27M glioma study PMID:38767413 add relevant developmental and transcriptional context. The former measures chromatin occupancy, expression and differentiation endpoints in an hESC model; the latter resolves FOSL1-associated recruitment and expression changes in human glioma cells, with mouse neurons in coculture. Neither an enriched downstream gene set nor an altered histone mark is treated as CHD2's own catalytic activity. No new neurodevelopmental, tumor, signaling or synaptic process is added.

## Protein and RNA association evidence

All seven original protein-binding associations are preserved: six remain non-core and the THAP1 pair is refined to GO:0140297 DNA-binding transcription factor binding. The 2011 CHD2–TRIM41 pair is verified by BioGRID1438345 and the original human ORFeome screen Methods. The five 2014 pairs have 15 exact positive IntAct records; array, pooling and validated two-hybrid are related stages of the same study, not independent replications. Human participants, yeast host, BEND7-2 and MID2-2 identities and recorded sufficient-binding-region features are preserved. The experiments do not establish native physiological mechanisms or transfer an enzyme, transcription-factor or ciliary structural function to CHD2. The same assay-only association scope is used throughout this small set. THAP1 is independently verified as a sequence-specific DNA-binding transcription regulator, so the literal binding-class definition supports refinement without requiring a measured transcriptional consequence. This does not imply stronger native evidence for that screen pair or expand the core.

PMID:29153328 has an actual human endogenous CHD2–TDP-43 reciprocal co-immunoprecipitation result, despite much of the paper concerning Drosophila Chd1. RNase treatment also increased nonspecific recovery, so it is not evidence for a clean RNA-independent binary interface. The detailed co-IP Methods paragraph describes flies; its crosslinker conditions are not attributed to the human assay by assumption.

Both RNA-binding annotations are retained at capture scope, outside the remodeling core. The authentic Baltz primary thesis Table S1 visually shows CHD2 class II, raw L1/H1/L2 values -3.46/NA/-3.18, normalized mean +3.32 and iBAQ 5.38. L1 and L2 are light-crosslinked H/L comparisons, so both measured captures are enriched after normalization; absent reverse-label H1 is not a negative result. Gene-level identification does not resolve an isoform or RNA target. The original Castello full paper and extended capture/identification Methods were recovered, but its exact CHD2 Table S1 entry remains uninspected. The original curated HDA assertion is retained with that limit and the independent Baltz positive explicitly distinguished. No target-specific Castello ratio or validation is invented. The separate thesis is not represented as an independently recovered journal supplement.

## Ontology, provenance and remaining questions

The official Reactome event R-HSA-9943412 genuinely places a CHD1/CHD2 participant set in nucleoplasm. Its mixed bibliography and shared reaction summary are not wholly CHD2-specific experimental evidence. Nuclear chromatin remains the defining core location; the nucleoplasmic context is retained non-core. PAINT nodes are preserved as ancestral judgments. Historical IBD placement and complete old Ensembl chains were not reconstructed; no short-donor or target-self-reference objection is made.

The authenticated production GO-CAM index contains no exact O14647 target match. No NEW annotation is proposed, so no claim of a curator-overlooked process gap is made. Product-level activity, RNA specificity, DNA recognition and chaperone cooperation remain questions for targeted experiments.

Publication excerpts are deliberately short and cumulative across this entire newly authored packet, including repeated excerpts. These notes add no primary-source quotations. Literal database fields, identifier/title metadata and retrieved raw sources are preserved as source data; labeled evidence-file prose is a reviewer paraphrase, not a fabricated paper quotation. The final quote audit records exact totals and matches. Optional full-text flags are omitted in favor of precise cache-versus-actual-access explanations; an abstract-only selected cache is never used to imply that independently read full text was inaccessible.

ROOT independently checked the human biochemical motor, mouse MyoD/H3.3 experiments, human DNA-break mechanism and the current double-stranded-DNA definition in `CHD2/root-core-read/ROOT-CORE-READ.json`. No candidate or source bytes were edited by that bounded peer.

## Reference access ledger

- **GO_REF:0000002** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **GO_REF:0000024** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **GO_REF:0000033** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **GO_REF:0000107** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **GO_REF:0000116** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **GO_REF:0000117** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **GO_REF:0000120** — Original machine evidence-method identifier and title preserved. The annotation framework is identified; no historical PAINT tree, Ensembl mapping release or ARBA rule reconstruction is claimed.

- **PMID:21516116** — Full selected screen Results and Methods plus positive BioGRID1438345 read. Human CHD2–TRIM41 is a curated two-hybrid pair; no pair-specific orthogonal validation or exact construct isoform was verified. Failed supplementary-file responses are not treated as source evidence.

- **PMID:22658674** — Normal selected cache is abstract-only. Genuine institutional original PDF with extended Methods was recovered and selected UV/oligo(dT) capture and identification sections read. Exact CHD2 Table S1 remains uninspected; its preserved HDA assertion is supported at broad capability level by an independently inspected CHD2 capture in PMID:22681889. No target-specific ratio or follow-up assay is attributed to this paper.

- **PMID:22681889** — Original normal abstract and authentic primary author thesis Table S1 target row, header and protocol inspected. CHD2 class II has two concordant enriched light-crosslinked captures after normalizing raw H/L ratios; the reverse-label value is absent. The thesis is explicitly distinguished from an independently recovered journal supplement, and gene-level identification is not an isoform-resolved RNA mechanism.

- **PMID:25416956** — Full normal primary text and 15 exact positive IntAct target records inspected. Human participants, yeast host, three related screen stages, exact partner isoforms and recorded fragment features are preserved. This does not establish native physiological mechanisms.

- **PMID:29153328** — Selected main cache is abstract-only and preserved. Genuine fresh normal full variant independently read at human endogenous reciprocal co-IP Results and human-cell/tissue context. Drosophila Chd1 functional experiments and fly-specific co-IP Methods are not transferred to human CHD2. No purified binary interface is claimed.

- **PMID:9326634** — Full selected cloning, sequence/domain comparison and Discussion read. The historical human clone is shorter than the modern displayed product; direct DNA-binding precedent in this paper includes CHD1. Later primary human CHD2 biochemistry supplies target-specific corroboration.

- **Reactome:R-HSA-9943412** — Official event and participant set inspected. The shared CHD1/CHD2 nucleoplasmic model is genuine, but mixed literature is not wholly CHD2-specific and does not prove identical methyl-mark recognition by both proteins.

- **PMID:25384982** — Genuine full normal primary selected Methods, Results and Discussion inspected. Purified human full-length and truncated CHD2 from Sf9, defined DNA, native Drosophila histones and NAP1 support direct ATPase, assembly and remodeling. Motor-mutant and nonhydrolysable-nucleotide controls are explicit; DNA length preference is not a sequence motif.

- **PMID:26895424** — Genuine full normal primary selected human recruitment, PAR binding, chromatin expansion, H3.3 deposition and repair Results/Methods inspected. Separate mouse telomere-fusion assays are identified. Direct deposition by CHD2 versus cooperation with histone chaperones remains unresolved; no repair ligase or PARP catalysis is assigned to CHD2.

- **PMID:22569126** — Full mouse C2C12/NIH3T3 Results and selected Methods read: MyoD gain/loss and ChIP/re-ChIP, Chd2 depletion/rescue, H3.3 association and deposition. Recruitment to promoter chromatin does not isolate CHD2 sequence-specific recognition. The assay organism is retained rather than described as human myogenesis.

- **PMID:27783602** — Authentic full main text, exact supplementary Table S1 row 28 and Note S5 page 8 inspected. Chd2 is the neighboring RNA readout after linc2025 promoter deletion, not the perturbed protein. The source identity and current donor annotation are verified, but this experiment does not demonstrate CHD2 protein regulating gene expression; independent target-protein experiments support the retained broad assertion.

- **PMID:36115870** — Genuine full normal primary selected human hESC/interneuron Results and Methods read. Heterozygous disruption, genomic occupancy, chromatin marks, expression and differentiation endpoints support a developmental transcriptional context; they do not establish intrinsic histone acetyltransferase or sequence-specific DNA-recognition activity.

- **PMID:38767413** — Genuine full normal primary selected FOSL1/CHD2 co-IP, recruitment, chromatin/expression Results and Methods read. Human H3.1K27M glioma cells are distinguished from mouse cortical-neuron coculture. Effects on histone methylation/acetylation are not direct writer/eraser assays and no additional downstream process is manufactured.

- **file:human/CHD2/CHD2-source-evidence.json** — Manual reproducible extract and explicitly labeled source paraphrases from genuine records and primary reading; not an independent experiment or provider-generated report.


## Prepublication peer clarification

The independent whole peer prompted the THAP1 binding-class refinement and reuse of the authentic Chd2 supplemental readout. The three ATPase reasons now correctly identify the preserved ISS donor Q12873 as CHD3. These bounded changes preserve all source objects, products and original reference identities. No new annotation, source-cache replacement or primary quotation was added.


## 2026-10-10 — original Castello supplement recovered

The original publisher Table S1 is now available and the CHD2 row was independently checked. Its positive ion-count result confirms the existing non-core RNA-binding decision. This supersedes the earlier table-access gap; gene-level capture does not resolve a product or RNA target. The evidence artifact preserves exact headers, row 706, source URL/hash and the earlier provenance. All decisions, core functions and Baltz evidence remain unchanged.


## 2026-10-10 — source-scoped follow-up to PR #4583

The entire prior notes prefix and incoming history are preserved. This appendix supersedes the old replacement of regulatory-region binding by a generic duplex-binding term, the six-generic-binding count and the earlier artifact-quotation convention. Every original source assertion, product and reference identity remains unchanged.

Mouse MyoD gain/loss and promoter ChIP/re-ChIP establish Chd2 occupancy at myogenic cis-regulatory regions without establishing an intrinsic recognition motif (PMID:22569126, Figure 2). The official GO:0000976 usage comment explicitly includes non-specific regulatory-region binding, so it preserves that source context in rows 1/2. Direct human duplex-DNA binding remains supported by PMID:25384982 and the existing DNA-binding assertions; accepting a source parent is not an unauthorized NEW hierarchy duplicate. Human developmental occupancy and the FOSL1-dependent recruitment experiments independently support regulatory chromatin association (PMID:36115870; PMID:38767413).

The positive TRIM41 and MID2 pairs support a class-binding refinement, not a new native ubiquitination mechanism. The TRIM41 2014 array construct is residues 86–630 and lacks the parent RING segment 20–61; the interaction maps to a noncatalytic portion of a verified E3 protein, without showing that the fragment catalyses ubiquitination. The 2011 source does not resolve the tested isoform. MID2 isoform 2 has the exact VSP_009009 deletion of canonical residues 450–479, retains the RING at 30–80 and the tested region is 21–705. Neither partner's enzymatic activity is assigned to CHD2. BEND7, TEKT1 and TDP-43 remain positive non-core associations under the standing project instruction; no unsupported activity is invented from their names.

The eight accepted PAINT source judgments are now explicit qualified SUPPORTS_TRANSFER assessments. The current curated ancestral assertion is the phylogenetic basis and source-specific target experiments corroborate each capability. Historical IBD placement was not reconstructed or independently validated. Target evidence alone is not proof of that placement, and donor numbers or target self-reference are not objections.

PMID:27783602 Table S1 row 28 and Note S5 page 8 identify Chd2 RNA as the readout after linc2025 promoter deletion. This is not a CHD2 protein perturbation, so row 23 now records the source-citation role problem. The supported replacement GO:0006357 comes from independent CHD2 protein experiments: promoter recruitment, histone-variant incorporation and expression effects, including the human glioma result that FOSL1 [PMID:38767413 "helps recruit CHD2 to gene regulatory elements"]. The remodeler performs chromatin work; it is not the polymerase or a histone-modification enzyme.

The NHEJ question is a genuine role-boundary question, not a claim that CHD2 has only a knockout phenotype. Actual PMID:26895424 Results Figures 4–7 show CHD2-dependent repair, ATPase-dependent chromatin expansion and [PMID:26895424 "assembly of NHEJ complexes"], including KU/XRCC4 recruitment. The same assays distinguish CHD2 from CHD4 and SNF2H for that particular expansion readout. A current bounded query for human CHD4, SMARCA4 and SMARCA5 returns no direct NHEJ or NHEJ-regulation annotations; this small comparison is not a universal curator convention or proof of nonparticipation. Typed is_a/part_of hierarchy checks find no overlap with original CHD2 terms, and the authenticated GO-CAM index has no exact target hit. A NEW process is deferred because the direct-repair versus regulatory/preparatory-role assignment remains unsettled; the performed chromatin mechanism stays explicit in the existing core narrative and the expert question.

Ten self-quoting file supporting-text fields and the artifact's self-VERIFIED claim are removed. Bare file citations retain provenance; primary excerpts remain short, verbatim and cumulatively counted across YAML and the full notes file, including repeats. The finite change does not repeat normal intake, research-provider attempts or source-cache fetching.
