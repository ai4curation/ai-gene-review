# FH evidence audit

This targeted follow-up preserves the imported source assertions, natural products, earlier findings and quotation associations. New support is reference-only. It corrects the interpretation of selected existing annotations; unchanged sources were not all re-investigated.

## Catalysis and metabolic context

Human FH is a reversible fumarate/malate enzyme. [PMID:29456767](https://pmc.ncbi.nlm.nih.gov/articles/PMC5817394/) Results, Figures 5–6 and Table 1 measure recombinant human FH expressed in bacteria. A308T/H318Y have severely reduced turnover and altered oligomerization, with measurable residual activity. The Results explicitly distinguish recombinant A308T from the higher activity reported in patient fibroblasts. The inherited abstract wording “inactive” remains in the historical quotations; the current reasons use the quantitative limit.

[PMID:23643539](https://pmc.ncbi.nlm.nih.gov/articles/PMC3675675/) Results, Figures 1–4, and Methods “Cell Lines and Cell Culture” and “Generation of FH and FHcyt Transgenic Mice” directly resolve the mouse donor used for the arginine inference. Human full-length and mitochondria-excluded, V5-tagged FH constructs were expressed in mouse renal/MEF models and human UOK262 cells. Cytosolic re-expression corrects fumarate and argininosuccinate abnormalities; isotope tracing supports reversed ASL flux. ASL performs the arginine conversion, while FH controls the coupled fumarate pool. The arginine-deprivation effects differ between mouse and human systems. Neither a universal normal-tissue flux direction nor an exact natural isoform assignment follows from the engineered FHcyt name.

[PMID:24280230](https://pubmed.ncbi.nlm.nih.gov/24280230/) Results, Figures 3–5, provide independent tracing and ASL-suppression evidence for the reverse reaction after FH loss. These disease-model results qualify the cytosolic core description; they do not directly measure a universal physiological ASL-to-FH flux. The existing urea-cycle and arginine annotations remain non-core, with their curated donor scope intact.

[PMID:27554470](https://pubmed.ncbi.nlm.nih.gov/27554470/) Results and Figure 4E–H show impaired cold-challenge temperature maintenance, strongly reduced BAT UCP1 transcript and undetectable UCP1 protein in adipose-specific Fh1-knockout mice. Reassessment of the Discussion and Figure 8 distinguishes this genuine phenotype from a specific regulatory function: the paper frames it as severe adipose mitochondrial/ATP deficiency with impaired nonshivering thermogenesis and compensatory shivering. It does not isolate an FH regulatory step from the metabolic capacity required for the response. The two positive-regulation annotations are therefore marked over-annotated, without disputing the phenotype. A dedicated temperature-sensing or transcriptional mechanism is not a requirement of the GO term; the problem is the unresolved distinction between regulation and general metabolic requirement in this experiment. The respiratory-inhibitor comparison in Figure 4A–B concerns triglyceride synthesis in white adipocytes, not an experimental comparison of every TCA gene's cold phenotype.

The arginine decision differs because isotope tracing and compartment-specific rescue in PMID:23643539 connect FH's own fumarate catalysis to ASL reaction flux. The broad process term covers reactions and pathways involving arginine, not only enzymes using arginine as their immediate substrate. The existing inference remains non-core, bounded to the demonstrated pathway coupling and its model/orthology limits.

## Exact interaction records

The publication-filtered, explicit IntAct query for FH/P07954 returned 3, 33 and 13 records for PMID:25416956, PMID:32296183 and PMID:39251607 respectively. The following are the exact relevant records. Initial unfielded wildcard results were capped and are not used to infer absence or exhaustive coverage. Each set of three binary records represents related screening and validation methods, not three independent biological replications.

| Imported index | Source PMID | Partner | IntAct record IDs |
|---|---|---|---|
| 10 | 25416956 | P11309 (PIM1) | EBI-10513304; EBI-10354887; EBI-10197487 |
| 12 | 32296183 | O14787-2 | EBI-23441054; EBI-24528592; EBI-23216149 |
| 13 | 32296183 | O15160 | EBI-25143261; EBI-24640549; EBI-23636450 |
| 14 | 32296183 | P21673 | EBI-23544538; EBI-25100226; EBI-24587935 |
| 15 | 32296183 | Q03252 (LMNB2) | EBI-23542548; EBI-25098218; EBI-24586829 |
| 16 | 32296183 | Q14129 | EBI-23487188; EBI-25042696; EBI-24555016 |
| 17 | 32296183 | Q2TAC2-2 | EBI-25013522; EBI-23458140; EBI-24538423 |
| 18 | 32296183 | Q68D86 | EBI-23508484; EBI-25064010; EBI-24567284 |
| 19 | 32296183 | Q6DKK2 | EBI-23587244; EBI-24612373; EBI-23362850 |
| 20 | 32296183 | Q8WZ60 | EBI-25138995; EBI-24638098; EBI-23632184 |
| 21 | 32296183 | Q9H6J7-2 | EBI-25128644; EBI-23572848; EBI-24604179 |
| 22 | 32296183 | Q9NQT4 (EXOSC5) | EBI-25070911; EBI-23515349; EBI-24571239 |
| 23 | 39251607 | Q9NQT4 (EXOSC5) | EBI-56902538 |

Records are retrievable from [IntAct](https://www.ebi.ac.uk/intact/home) using the listed IDs. Binary-method identifiers are MI:0397, MI:1112 and MI:1356. Official [PIM1/P11309](https://www.uniprot.org/uniprotkb/P11309/entry) and [LMNB2/Q03252](https://www.uniprot.org/uniprotkb/Q03252/entry) records establish the partner classes for **protein kinase binding (GO:0019901)** and **lamin binding (GO:0005521)**. These terms refine binding; they do not transfer the partner's catalytic or structural role to FH. Other supported bare interactions remain non-core under the campaign policy.

PMID:39251607 uses BioID proximity for the FH–EXOSC5 record (MI:1314; interaction type MI:2364), not yeast two-hybrid. Independent binary evidence for the identical pair comes from PMID:32296183. This distinction does not establish FH as an RNA-exosome regulator. [Correction PMID:39468017](https://pubmed.ncbi.nlm.nih.gov/39468017/) adds an author affiliation only. Original supplement pixels were not re-read in this interaction audit.

## DNA damage, products and authored duplication

[PMID:26237645](https://pubmed.ncbi.nlm.nih.gov/26237645/) Results Figures 1 and 3 show FH chromatin association and ChIP next to an induced break. Figures 5–6 separate localization from catalytic activity and connect fumarate production to KDM2B-dependent H3K36 methylation, Ku70 accumulation and NHEJ. FH produces the regulatory metabolite; it is not the DNA ligase. The existing positive-regulation proposal therefore rests on catalytic participation, not knockout necessity alone.

Experimental FH(N) deletes residues **1–21** (Results preceding Figure 3). The unchanged UniProt natural product P07954-2 lacks **1–43** (VSP_018965). No artificial construct is added as a natural product, and the nuclear mechanism is not assigned exclusively to P07954-2.

[PMID:29632342](https://www.nature.com/articles/s41556-018-0074-7) replaces duplicated images in Figure 2d and reports two additional deposited repetitions. The complete operative correction paragraph was read in the genuine cache although its automatic full-text flag is false. Corrected pixels and Figshare data were not independently inspected. The correction is explicitly recorded without treating every separate assay as independently repeated or invalidated.

Official QuickGO typed ancestry is **GO:0035861 is_a GO:0090734 part_of GO:0005694**. The experimental chromosome row is refined to the DSB site; the broader electronic row is redundant. Previously authored NEW row 60 is retired, with its source and quotations preserved, rather than deleted. NEW row 59 remains active. Qualified comparator checks found SETMAR annotated to positive NHEJ regulation, while ACLY and KDM2B lacked repair annotations; their roles differ, so this mixed pattern does not establish a universal inclusion or exclusion convention. The scoped GO-CAM index and two ACLY models supplied no contrary FH-repair assertion. Current FH annotations already cite this paper for interaction/localization; the process proposal explicitly remains a reviewed mechanistic interpretation.

## Remaining limits and provenance

The exact FH/P07954 supplementary entry for [PMID:20458337](https://pubmed.ncbi.nlm.nih.gov/20458337/) was not recovered. The exosome row is unresolved. Neither contamination nor absence of an extracellular function is established, and localization does not require a known compartment-specific function.

Official ancestry also gives **GO:0004333 is_a GO:0016836 is_a GO:0016835 is_a GO:0016829**; the broad lyase row adds no distinct activity. Existing PAINT source records are preserved; no evolutionary loss, donor-count objection or self-WITH circularity is asserted. The family-level comparative paper is not substituted for a fresh target-tree reconstruction.

Primary records and cached source files remain unchanged. The dated [notes](FH-notes.md) explain the follow-up, and the current review YAML remains the decision authority.
