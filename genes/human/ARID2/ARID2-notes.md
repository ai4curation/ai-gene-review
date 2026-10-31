# ARID2 primary assessment — 2026-09-28

This manual literature assessment supports the completed annotation review. Seed11 supplied Q68CP9, HGNC:18037, 45 assertions and two products: name 1/Q68CP9-1 and name 2/Q68CP9-3. Preserve those identifiers. Configured falcon research with perplexity-lite fallback failed once, producing no provider file. Existing normal caches remain unchanged.

## PBAF specificity and transcription

[Yan et al., PMID:15985610](https://pmc.ncbi.nlm.nih.gov/articles/PMC1176002/) identifies human BAF200 as ARID2 by mass spectrometry and specific antibodies. Root read the original Abstract, Introduction, Results/Discussion through the IFITM1/IFITM3 experiments, and Figure 1–4 captions; the later BAF180-independent-complex section, complete Methods, supplements and image pixels were not inspected. Reciprocal Flag-BAF200 recovery includes BRG1, BAF180, BAF57 and hSNF5, with DNA-mediated association controlled using ethidium bromide. BAF200 depletion reduces BAF180 abundance and prevents normal IFITM1 induction; IFITM3 instead depends on BAF250a. This supports a PBAF structural/specificity role and the existing broad transcription/remodeling assertions, without assigning ATP hydrolysis to ARID2. The normal cache remains abstract-only. The independently read original experiments supply specificity that is not in that cache.

[Patsialou et al., PMID:15640446](https://pubmed.ncbi.nlm.nih.gov/15640446/) is PubMed-verified. Root read the complete cached abstract and targeted full-text Methods for the human HepG2-derived ARID2 1–209 construct, Results around Figure 4, affinity comparison and Discussion limits. The isolated ARID region binds DNA without an obvious sequence preference and with relatively low affinity in that assay. The native protein could behave differently in context; neither the gene name nor this assay establishes AT-rich selectivity. All three existing DNA-binding assertions are biologically well grounded, including the IBA with the target among its experimental descendants. No PAINT ancestral-node reconstruction has been performed.

[Kaeser et al., PMID:18809673](https://pmc.ncbi.nlm.nih.gov/articles/PMC2583284/) was read in the normal cache: complete abstract, targeted purification/BRD7 Results and signature-module Discussion. ARID2 co-purifies with BRG1 in BRD7-containing PBAF; BRG1 is identified as the ATPase. This supports complex-based remodeling and transcriptional regulation. It does not establish intrinsic ARID2 ATPase activity. Not all Methods or gene-specific depletion results were inspected.

## DNA repair

[de Castro et al., PMID:28381560](https://pmc.ncbi.nlm.nih.gov/articles/PMC5437250/) is verified through official PubMed. Root read the complete cached abstract and indexed original Figure 5/co-IP and yeast-two-hybrid results, Figure 6 recruitment results, and targeted antibody/plasmid Methods. Human U2OS experiments support ARID2 association with RAD51 and its efficient recruitment to homologous-recombination sites. Depletion impairs homologous recombination. Distinct ARID2 complexes with and without BRG1 are described. This supports the existing positive regulation of homologous-recombination repair; it does not make ARID2 a recombinase. Full Methods, figures, all Results and supplements remain unread; normal cache is abstract-only.

[Kakarougkas et al., PMID:25066234](https://pubmed.ncbi.nlm.nih.gov/25066234/) identity was verified on PubMed. Root read the complete cached abstract and Introduction paragraph defining the PBAF subunits; a targeted name search found BAF200 in that paragraph. The broader paper requires further targeted reading before claiming any absence of ARID2 experiments. Its PBAF/BAF180-centered result cannot alone settle ARID2's specific metaphase/anaphase role. Independent ARID2 repair evidence above can support a broad repair assertion without pretending this earlier citation is target-specific.

## Contextual proliferation and invasion

[Yu et al., PMID:26169693](https://pubmed.ncbi.nlm.nih.gov/26169693/) was verified on PubMed. Root read the complete abstract, cached ARID2 overexpression and combined miRNA-inhibitor/ARID2-knockdown Results, Figure 3–4 captions, and relevant Discussion. Human HepG2/Hep3B experiments show suppression of proliferation and transwell invasion after ARID2 expression, with partial reversal by ARID2 knockdown. These are supported contextual outcomes, not the molecular core of ARID2. No claim of complete Methods or image review is made.

## Other scope checks

The entire normal cache for PMID:11078522 was read. Although marked full-text-available, it contains Abstract and Discussion without the original Results/Methods. Kinetochore staining uses BAF180 as a PBAF proxy; it is not a direct ARID2 localization experiment. This is not a wrong-gene conclusion.

Complete cached abstracts were read for PMID:10078207, 11790558, 12110891, 12192000, 12215535, 8804307, 8895581 and 10778858. They establish important SWI/SNF biology, but precise ARID2-specific T-cell, myoblast, cell-cycle and excision-repair claims still need adjudication. No experimental annotation is removed on an abstract-only or title-based inference.

[The 2015 correction to PMID:22140357](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002302) was read in full, including notice and corrected captions, but not image pixels. It discloses reordered/spliced loading lanes, duplicated presentation panels and replacement of previously published control material; authors state conclusions are unchanged. This is not a retraction. Root has read the original abstract and targeted cached Tat/PBAF paragraphs, but has not yet recovered an ARID2–BRG1-specific experiment in this source.

GO's official AmiGO record confirms GO:0016586 includes mammalian PBAF and GO:0051117 is ATPase binding. These are available for the core complex and informative refinement of an established BRG1 interaction, respectively. OLS tools are not available in this session. No NEW process term is proposed.

## Additional source under normal retrieval

[Xu et al., PMID:22184115](https://pubmed.ncbi.nlm.nih.gov/22184115/), DOI 10.1074/jbc.M111.279968, PMC3281626, was verified on official PubMed. Root read its complete abstract and indexed primary Results on ARID2-depleted mouse MC3T3-E1 osteoblast precursors, Figure 2 caption, Alpl/Bglap recruitment results and Discussion. ARID2 depletion impairs differentiation and promoter recruitment of the transcription machinery in a locus-dependent manner. This provides independent support for the existing broad differentiation/transcription assertions; it does not establish a human myoblast result. The first normal fetch failed with a DNS error after 32.43 seconds and produced no cache. Its terminal receipt is preserved; the subsequently recovered normal cache is present with its source bytes unchanged. No replacement cache has been authored.


## Independent consultation and final mechanism boundaries

The independent annotation consultation examined all 45 decisions and the two original products. The ten unresolved IPI rows retain their original sources and partners. Human PBAF studies independently establish these associations; the unresolved part is the precise source-specific assay, not whether those proteins can associate.

Root subsequently read the original PMID:28381560 Results and captions through Figures 4–8, the relevant Discussion, and Methods through the start of ChIP preparation. No supplementary data or image pixels were inspected. ARID2–RAD51 association and bulk chromatin loading persist after BRG1 depletion or knockout. Efficient RAD51 recruitment to individual homologous-recombination sites nevertheless decreases after loss of either ARID2 or BRG1. The proposed division of labor between distinct complexes remains a hypothesis. The repair core therefore does not assert exclusive ATP-dependent remodeling or completely BRG1-independent repair.

DNA binding and contributed PBAF remodeling form one core function. Homologous-recombination repair recruitment is represented separately, with its precise molecular activity and complex composition unresolved. No new annotation is proposed. The original GOA qualifier on the ATP-dependent activity remains untouched; the synthesized core attributes ATP hydrolysis to BRG1 and uses contributes_to_molecular_function for ARID2.

The source records for all 45 assertions and both products are preserved. Generic protein-binding observations with verified experiments are kept outside the core or refined to ATPase binding when justified by the original source. Genericity alone is not evidence of an incorrect interaction. A missing cache full-text flag is not a claim that no external original text was read; the reading scope above is explicit.

The raw GOA provenance identifies all 14 NAS rows as ComplexPortal assignments carrying ECO:0005547. This provenance is kept distinct from a direct experimental ARID2 annotation. Chromatin association, remodeling, PBAF membership, transcriptional regulation and homologous-recombination repair have independent ARID2 evidence, so the matching broad assertions are retained. Specific kinetochore/nuclear-matrix, cell-cycle, T-cell, myoblast and nucleotide-excision-repair assertions remain unresolved at the target-specific level. The difference in action follows the available ARID2 evidence rather than a blanket rule for NAS or the ComplexPortal source.


## Final source record

The additional PMID:22184115 normal cache is abstract-only. Its complete abstract was read and its bytes match the verified Source45 artifact. Earlier targeted reading of the original mouse osteoblast Results is documented above and does not change the cache availability flag. All 45 decisions and two core functions received independent draft consultation; final authored-file and exact-source checks are recorded separately.


## PR #3372 follow-up: BAF200–BRG1 association and source scope

The original published review and history remain the baseline. This follow-up resolves one previously unread experiment and refines that original assertion to ATPase binding. All 45 source annotations, both products and the two core functions are preserved. No NEW annotation is added.

The earlier statement that the ARID2–BRG1 experiment in [PMID:22140357](https://pmc.ncbi.nlm.nih.gov/articles/PMC3226458/) had not been recovered is superseded by the present targeted read. Figure 3C describes BRG1 immunoprecipitation from human J-Lat A2 cells and immunoblotting of associated BAF200, alongside other complex subunits. The surrounding Results distinguish BAF/PBAF perturbations. The antibody Methods explicitly names anti-BAF200. Its detailed M2-agarose procedure concerns Tat-FLAG, so that protocol is not attributed to the anti-BRG1 experiment. Figure pixels and complete supplements were not inspected. The observed complex association supports GO:0051117 ATPase binding to SMARCA4/BRG1; it does not establish a purified binary interface or ATP hydrolysis by ARID2.

The full [2015 publisher correction notice](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002302) and corrected Figure 2/4 captions were inspected independently. It describes reordered/spliced Figure 2D loading lanes with corrected actin presentation, reused/duplicated Figure 4A control panels with replacement replicate material, a splice disclosure in S1B and repeated S8C/F presentations. It does not name Figure 3C and is not a retraction. These substantial image-presentation concerns warrant a LOW_QUALITY caution on the reference, without treating every experiment in the article as false. The target association also agrees with the earlier human PBAF purification in PMID:15985610, whose original read scope remains recorded above.

The current official [GO:0016514](https://amigo.geneontology.org/amigo/term/GO:0016514) definition describes an 8–14-protein SWI/SNF-type complex containing the SNF2/SMARCA4 ATPase or an ortholog. It does not explicitly exclude mammalian PBAF. [GO:0016586](https://amigo.geneontology.org/amigo/term/GO:0016586), RSC-type complex, explicitly includes PBAF among its synonyms and describes bromodomain-containing complexes. Both terms share GO:0070603 as an is_a parent; neither is asserted here to be the other's formal parent. Stable human ARID2 incorporation into BRG1-containing PBAF supports retention of the broad existing CC assertion while the more specific PBAF term remains in the core. The historical PMID:8895581 source stays unchanged, and the target-specific corroboration is explicitly attributed to later human ARID2 work.

The remaining nine interaction assertions are distinguished by their actual source access:

| Source and partner | Inspected evidence | Remaining limit |
| --- | --- | --- |
| PMID:24981860; SMARCB1 and SMARCE1 | Complete cached abstract and official indexed record: tagged human chromatin-protein AP-MS survey. | Publisher direct access returned 403; neither precise pair experiment was inspected. Its table/figure location is unknown. |
| PMID:30108113; SMARCB1 | Original interactome Results describe SMARCB1 AP-MS and BioID in Flp-In T-REx 293 cells. | The exact ARID2 record and which assay supports it remain unverified. Dataset EV5 and image pixels were not inspected. |
| PMID:31759698; SMARCB1 | Original complex-assembly Results describe WT/mutant SMARCB1 incorporation assessed by IP, immunoblot and proteomics. | The ARID2 pair-level observation remains unread. Retrieved ARID2 prose concerns ChIP-seq data, not proof of a missing interaction. |
| PMID:33961781; SMARCB1 and SMARCE1 | Entire cache, including Introduction/Discussion, describes BioPlex AP-MS in 293T and HCT116 cells. | The extraction lacks original pair-level Results/Methods; bait/prey and cellular contexts remain unresolved. |
| PMID:34591612; SMARCB1 | Entire cached abstract/Discussion describes AP-MS across three human breast cell lines. | The specific pair, mutant and cell-line conditions have not been inspected. |
| PMID:35271311; SMARCA4 | Entire cached abstract/Discussion describes endogenous tagging and IP-MS in HEK293T cells. | The precise pair measurement remains unread; localization agreement does not substitute for it. |
| PMID:40205054; SMARCE1 | Original proteomics acquisition Results describe U2OS Flag-HA baits, AP-MS and quality controls. | The exact pair record and detection modality have not been inspected. |

The normal cache flags remain unchanged. In particular, a true full-text flag can accompany a partial HTML extraction. No missing target-name search hit is treated as evidence that the experiment is absent, and no uninspected pair is assigned to a guessed supplementary table. Independent human PBAF association establishes biological plausibility but does not close each source-specific assay.

The three established non-core interactions with SMARCB1, PBRM1 and SMARCE1 remain supported by original human PBAF purification. Under the explicit user ActionEnum, REMOVE requires likely biological error; genericity alone does not meet that criterion. That instruction takes precedence over the skill's generic-binding default. This policy choice is recorded once here, while individual review reasons describe the biology and experimental limits.


## Scoped rationale for the three retained PBAF interactions

The remaining finding in the [re-review of PR #3372](https://github.com/ai4curation/ai-gene-review/pull/3372#discussion_r4122687857) concerns an exclusion criterion, not a disputed experiment. The repository's generic-binding guidance generally recommends `REMOVE` when no more informative molecular function is supported, and explicitly says that removal on that basis does not mean the reported interaction is false. The three corresponding validator advisories are therefore expected. The earlier paragraph about instruction precedence did not acknowledge this informational-exclusion rationale clearly enough.

This ARID2 review records a scoped exception under the task's supplied ActionEnum: the three existing IPI observations from PMID:15985610 remain `KEEP_AS_NON_CORE`. This is a deliberate retention of adjudicated source assertions outside the core synthesis, not a claim that the repository default already endorses that action, and not a proposal to change the validator or the policy for other genes. A warning documents the departure; it does not supply biological evidence for rejecting or strengthening an interaction.

The retained observations identify SMARCB1/hSNF5, PBRM1/BAF180 and SMARCE1/BAF57 in the original human PBAF isolation experiments. The original Results and Figure 1–4 captions were read as documented above; the normal PMID:15985610 cache remains abstract-only. Flag-BAF200 recovery and the ethidium-bromide control support association in the complex. These experiments do not establish three isolated binary interfaces, and retention does not transfer a partner's histone-reader or DNA-binding activity to ARID2. The complex-membership annotations separately describe PBAF incorporation; the IPI rows retain the specific partners, source and experimental context.

The exception is limited by the actual evidence. Two source-supported BRG1 associations have the more informative ATPase-binding refinement. Nine other source-specific interaction assertions remain `UNDECIDED` because their precise supporting measurements have not been adjudicated. Those decisions are not converted to retention by this rationale. All 45 source assertions, both products and both core functions retain their existing decisions; no new GO assertion is proposed. ARID2 remains a DNA-binding and structural/specificity contributor to PBAF, with ATP hydrolysis assigned to BRG1 and the separate repair-recruitment mechanism bounded as described above.
