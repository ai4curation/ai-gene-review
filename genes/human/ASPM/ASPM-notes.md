# ASPM functional review notes

2026-09-28. Initial assessment of the source annotations and primary literature.

The initial review has 19 source assertions, no NOT assertions or annotation-specific isoform flags, and two recorded products: Q8IZT6-1 and Q8IZT6-2 (VSP_010680). The UniProt sequence is 3477 aa; isoform 2 lacks residues 1356–2940. These records are preserved. Older paper motif counts depend on prediction conventions and do not replace current sequence features with the paper's 81-versus-14 count.

The original PMID set is 15972725 and 21044324. The first cache is abstract-only; the second contains XML-extracted full text. The XML cache repeats nested sections; the substantive Results, Discussion and Methods paragraphs were read separately, including main and supplementary figure legends. Figure pixels and supplementary movies were not inspected.

## PMID:21044324 — actual full cache

Human HeLa, U2OS, HDF and SH-SY5Y experiments are distinguished from monkey COS-7 work. Three antibodies gave similar staining; only the N-terminal 217-2 antibody was optimized for endogenous immunoblotting. Peptide/preimmune specificity controls are reported, some data not shown. Interphase ASPM is predominantly nuclear, and this study did not detect an interphase centrosomal pool. After nuclear-envelope breakdown it forms a pole-proximal ring around, rather than extensively overlapping, gamma-tubulin. Late mitotic protein localizes at central-spindle minus ends and a narrow midbody ring.

Nocodazole removes spindle-associated ASPM while retaining gamma-tubulin; taxol produces ASPM-positive aster centers and separate ASPM-negative anastral gamma-tubulin foci. This supports microtubule-dependent localization and should not be converted into a constitutive centriolar-core claim.

Two independent U2OS siRNAs (ASP1 and ASP2) reduce spindle-pole ASPM, with different efficacy. The paper did not detect a matching decrease of total interphase protein. Live-cell orientation/cytokinesis analysis used ASP1 and GL3 control, pooling four experiments (94 and 126 divisions). The paper's word 'asymmetric' denotes geometric division orientation relative to the dish, not an independently measured daughter-cell fate. The cytokinesis deficit exceeds the effect of altered orientation alone. No new apoptosis-regulation process is inferred from downstream caspase activation.

Patient fibroblasts with IVS25+1G>T retain an apparently stable protein but show markedly reduced pole localization; cDNA reveals a cryptic splice event deleting a tripeptide at the C terminus. The body and one figure legend disagree about upstream/downstream wording; the sequenced body says upstream. Keep current canonical protein length rather than repeating the isolated 3447-aa typo. Human C-terminal D1–D3 fragments (3177–3477, 3256–3477 and 3315–3477) expressed in HeLa and COS-7 cause dominant-negative spindle/cytokinesis defects. These are fragments, not evidence that canonical isoform 2 has all the same effects.

The spindle-organization and spindle-positioning processes are supported by actual structural localization plus perturbations. The discussion offers several possible late-cytokinesis mechanisms; it does not establish a direct motor, actin-binding enzyme or cytokinesis kinase function for ASPM. Later PMID:28883092 provides a useful compensation context rather than a reason to erase these experimental annotations.

## PMID:23152892 — mouse donor evidence

[Original PLOS article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049303): complete Results through Figure 6 and targeted Methods read. Native mouse oocytes and mouse embryonic fibroblasts were studied. ASPM decorates the meiotic spindle and co-immunoprecipitates with calmodulin; the immunoprecipitation control is unrelated rabbit IgG. This is cellular association, not an isolated purified binary-binding assay. One ASPM morpholino reduces the measured protein signal and disrupts spindle morphology/progression; uninjected and control-morpholino controls are included. No rescue experiment is claimed. Spindle-checkpoint machinery is discussed as a hypothesis, not measured directly. These data support the mouse donor biology for existing human orthology transfers; they are not direct human oocyte assays.

## PMID:17534152 — traced rat donor

The official [NCBI rat Aspm record](https://www.ncbi.nlm.nih.gov/gene/289054) links this PMID to its IDA apical-membrane, centrosome, midbody and mitotic-pole rows. Thus the rat donor underlying the human IEA is identifiable, not a guessed citation.

Direct publisher and author PDF opening returned 403. Indexed original Methods and Figure 1/3 legends were readable at [the author-hosted manuscript](https://dyslexialab.net/Pdfs/Paramasivam2007.pdf) and [publisher PDF](https://www.tandfonline.com/doi/pdf/10.4161/cc.6.13.4356). Methods specify rat E14-brain cDNA for ASPM MTB/CTR constructs and a rat N-terminal antigen for Ab418; BL2048 is raised against a human peptide. HeLa/HEK293 expression hosts are human, whereas these expressed ASPM fragments are rat. Figure 1 demonstrates endogenous HeLa prophase centrosomal, metaphase spindle-pole and cytokinetic midbody staining with two antibodies. Figure 3 explicitly shows E13 rat neocortical ASPM at neuronal-progenitor poles and the ventricular apical surface, with aurora-B association at that surface. This is sufficient to avoid declaring the rat source nonexistent, but full Results, complete controls and pixels have not been read. The non-core human apical annotation remains a candidate for cautious retention or UNDECIDED after consultation, not automatic removal because it is unusual.

## Molecular-function boundary

The official [GO term page](https://amigo.geneontology.org/amigo/term/GO:0051011) was read via its indexed content: GO:0051011 is microtubule minus-end binding, a molecular function and child of GO:0008017 microtubule binding. QuickGO returned only a JavaScript shell/API failure; there is no callable OLS tool in this session.

[PMID:28436967](https://pmc.ncbi.nlm.nih.gov/articles/PMC5458804/) supports a conserved minus-end mechanism, but the purified reconstitution uses short **mouse** ASPM plus calmodulin. This species boundary was independently checked. Endogenous human ASPM is recruited to newly generated minus ends in the cellular experiment. The mouse purified assay is not a human IDA, and katanin supplies ATP-dependent severase activity. At this initial reading, a new human binding annotation remained under consideration; the final inference is recorded below.

Additional literature identified at the initial reading comprised PMIDs 28436967, 27562601, 28883092, 23152892 and 17534152. PMID:19219036 remains separate worm comparator evidence.


## 2026-09-29 — final synthesis

All 19 original source assertions and both alternative products are preserved. Decisions are 12 ACCEPT, 6 KEEP_AS_NON_CORE and 1 UNDECIDED, plus one NEW ISS molecular-function inference for microtubule minus-end binding. The human cellular observations and mouse ASPM-calmodulin reconstitution are distinguished. Katanin supplies severing catalysis; no new process, motor, ATPase, kinase or human-isoform-specific activity is proposed. Calmodulin association supports the integrated microtubule mechanism without requiring a separate core-function entry. The unresolved apical-membrane assignment retains positive rat evidence without claiming that midbody staining establishes a membrane domain.

The normal deep-research attempt failed and generated no provider report. The two seed publications and five additional sources were recovered by normal fetchers before final authoring. Cached full-text availability is recorded separately from actual scientific reading scope.
