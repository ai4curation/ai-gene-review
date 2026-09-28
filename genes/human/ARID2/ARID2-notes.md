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
