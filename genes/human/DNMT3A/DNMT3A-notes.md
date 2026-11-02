# DNMT3A: paired human–horse review notes

## Biological evidence

Human structural/biochemical evidence establishes DNA cytosine methylation, oligomerization and chromatin-guided targeting. PWWP and ADD domains have distinct targeting/regulatory roles. The protein-cysteine methyltransferase annotation has a real source: slow mouse catalytic-cysteine automethylation in DNA-free assays, suppressed by natural CpG substrate. It is non-core biochemical capacity, not an established second physiological function.

- [PMID:29414941: Structural basis for DNMT3A-mediated de novo DNA methylation.](https://pubmed.ncbi.nlm.nih.gov/29414941/) — full text cached.
- [PMID:25383530: Structural insight into autoinhibition and histone H3-induced activation of DNMT3A.](https://pubmed.ncbi.nlm.nih.gov/25383530/) — abstract cached; full-text availability must be checked separately.
- [PMID:30478443: Gain-of-function DNMT3A mutations cause microcephalic dwarfism and hypermethylation of Polycomb-regulated regions.](https://pubmed.ncbi.nlm.nih.gov/30478443/) — full text cached.
- [PMID:21481189: Auto-methylation of the mouse DNA-(cytosine C5)-methyltransferase Dnmt3a at its active site cysteine residue.](https://pubmed.ncbi.nlm.nih.gov/21481189/) — abstract cached; full-text availability must be checked separately.
- [PMID:12138111: A novel Dnmt3a isoform produced from an alternative promoter localizes to euchromatin and its expression correlates with active de novo methylation.](https://pubmed.ncbi.nlm.nih.gov/12138111/) — abstract cached; full-text availability must be checked separately.
- [PMID:38705424: Different expression patterns of DNA methyltransferases during horse testis development.](https://pubmed.ncbi.nlm.nih.gov/38705424/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The horse deletionhuman339–374overlaps the PWWP-domain end, while ADD and catalytic domains are retained in a97.3%-identical alignment. Broad nuclear localization and expression regulation are supported; normal locus targeting is not established. Horse testis data measure DNMT3A expression and immunofluorescence but do not identify the selected accession or establish every catalytic/regulatory claim.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/DNMT3A/DNMT3A-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

The horse Edison report identifies further equine expression leads but misses the testis paper retrieved independently. Do not treat its statement about absent horse localization evidence as exhaustive. Inspect the PWWP fold and transcript model; resolve specialized exposure/germline annotations from their original source experiments.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.


## 2026-10-17 — comprehensive human DNMT3A augmentation

The earlier human/horse comparison and its source history above are preserved. This dated assessment supersedes unresolved or broader functional interpretations where the evidence below is more specific. The human review now assesses all 87 inherited annotation objects. Genuine normal fetching returned 88 raw GOA records representing the same 87 unique tuples, and the GOA bytes match the previous snapshot. No source identity was retired or rewritten, and no NEW annotation was introduced. Official product identifiers and sequence-change annotations remain intact.

The [source evidence guide](DNMT3A-source-evidence.md) gives public original locators, exact assay/access distinctions, interaction-record counts and typed Reactome paths. It documents research and is not cited as independent support for the underlying experiments. The configured Falcon command returned its cached provider result; no fresh provider synthesis or fallback output is claimed.

The three molecular units are DNA-cytosine methylation, ADD-mediated recognition of the unmethylated H3 amino terminus, and PWWP-mediated recognition of methylated H3K36. Human catalytic-domain assays include non-CpG methylation, so the enzyme term is not narrowed to CpG-exclusive activity (PMID:29414941). ADD and PWWP specificity is grounded in human-domain experiments (PMIDs:19834512, 30478443). CpG-island repression is supported at selected human promoters (PMID:23042785). Regulatory partners and chromatin engagement guide targeting; this does not turn DNMT3A into an autonomous Pol II cis-regulatory sequence-specific transcription factor.

The PWWP W330R phenotype affects developmental Polycomb-associated valleys and reduces local H3K27me3. It does not demonstrate constitutive-heterochromatin formation as defined by GO:0006346. Positive localization to heterochromatin in ortholog experiments is a different assertion and remains supported. Nucleoplasmic imaging and model assignments are also preserved separately from functional chromatin localization.

Positive interactions are retained under the project's [explicit binding instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). Genericity alone does not invalidate a pair. Specific partner-class refinements use actual interaction scope and verified partner properties. AP-MS and native co-immunoprecipitation are not described as purified direct binding; a binary screening result does not by itself establish physiological stoichiometry or shared target regulation.

PMID:16357870 requires an explicit correction/access distinction. The original supplementary Methods and the [2007 correction](https://doi.org/10.1038/nature05710) were recovered. The latter supplies omitted lanes in Figures 2a, 2c, 4a and S1 and states that conclusions are unchanged. Corrected S1 uses a 908-residue DNMT3A map, so those historical fragments are not assigned to an exact current human product. Human HeLa co-immunoprecipitation and the domain interaction evidence remain separate. The positive PRMT5 interaction in PMID:19234465 is likewise separate from its H4R3me2s-recognition claim, which was not reproduced under the conditions of PMID:19834512.

Product names alone do not establish sequence equivalence. Current products have 912, 723 and 166 residues. The 689-residue human DNMT3A2 reagent in PMID:32968275 spans canonical residues 224–912; it is not current product 2. Its DNMT3B3 partner is catalytically inactive and provides a nucleosome anchor. Mouse DNMT3A/DNMT3L constructs in PMID:17713477 are explicitly mouse. The short natural product lacks the tested canonical reader/catalytic domains, but its biological role remains unresolved rather than declared universally absent.

Propagation review follows the actual PAINT nodes and donor annotations. All relevant nodes are ancestors of the human target, and the target's own experimental evidence legitimately contributes to IBD grounding. Donor-count and self-circularity arguments are not used. Several rat exposure studies measure DNMT3A abundance or total methyltransferase activity; these real responses are distinct from demonstrating DNMT3A as the executing response component. Full-text expression-only examples are marked over-annotated; source-limited cases remain UNDECIDED. The selective Dnmt3a perturbation in the hypoxic-injury study supports a contextual positive role (PMID:23516428).

Full originals were recovered separately for several abstract-only caches, while protected cache bytes and flags remain unchanged. The specific nuclear-matrix experiment in PMID:12138111 is still unresolved. The 25383530 publisher recovery contains abstract and extended captions, not a full main-text read. These limitations are explicit in reference assessments and the guide. Four new short excerpts occur once each in the YAML, totaling 41 words across four sources, each below 25 words; inherited excerpts and all previous notes are recorded separately.

The subsequently recovered original of PMID:24074865 resolves the human co-IP context without changing its non-core disposition; see the source guide for the institutional original and assay limits.

## 2026-10-17 — Binding specificity and contextual pericentric methylation

This follow-up supersedes the earlier over-annotation interpretation of GO:0006346 and the earlier statement that no new annotation is proposed. All 87 imported source objects remain unchanged. The review now has 88 rows: 9 ACCEPT, 43 KEEP_AS_NON_CORE, 23 MODIFY, 4 MARK_AS_OVER_ANNOTATED, 8 UNDECIDED and one NEW. The three core entries are unchanged.

The two DNA-binding reviews now refine to [unmethylated CpG binding, GO:0045322](https://www.ebi.ac.uk/QuickGO/term/GO:0045322), an ontology descendant of DNA binding already represented elsewhere in the source annotations. Human DNMT3A DNA-bound structures and substrate assays support this interaction. The zebularine-containing covalent structural trap is distinct from the ordinary CG, CA and CT DNA used for kinetic measurements. The catalytic core remains broad enough to include measured non-CpG activity ([PMID:29414941](https://pubmed.ncbi.nlm.nih.gov/29414941/), Results on DNA recognition and Methods on protein preparation and methylation assays).

Constitutive-heterochromatin participation is retained as contextual on the basis of [PMID:15456878](https://pubmed.ncbi.nlm.nih.gov/15456878/), Figures 3–4 and the Results on rescue of genomic methylation. In mouse Dnmt3a/Dnmt3b-null ES cells, WT Dnmt3a restores pericentric major-satellite DNA methylation; the catalytic mutant does not, and PWWP deletion strongly impairs methylation of these repeats. Dnmt3a therefore performs the measured methylation step. The study does not directly measure de novo chromatin condensation or assembly; its Discussion presents structural reinforcement as a possibility. This is distinct from the human W330R developmental-valley phenotype in PMID:30478443, which concerns Polycomb/H3K27me3-marked regions. Neither generic heterochromatin localization nor a separate ncRNA-mediated silencing assertion entails the constitutive process.

One new molecular-function annotation, [histone H3K36me3 reader activity, GO:0140003](https://www.ebi.ac.uk/QuickGO/term/GO:0140003), records the direct human WT GST-PWWP peptide-binding experiment in [PMID:30478443](https://pubmed.ncbi.nlm.nih.gov/30478443/), Figure 2c–e and Methods on peptide pulldowns and arrays. The unmodified control does not bind under the tested conditions, and W330R loses recognition. Arrays also support H3K36me2 recognition. The current typed ancestry audit finds no ancestor or descendant among the 87 imported annotation terms or their proposed replacements; the ADD reader is complementary. No additional process annotation or core is introduced.

Two short exact source anchors occur once each in the review: 12 words from PMID:15456878 and 13 from PMID:30478443. The six inherited review excerpts are preserved. No source excerpt is repeated in this appendix or the source guide. Product descriptions now state sequence/domain biology directly; the source guide retains the distinction between the historical 689-residue DNMT3A2 reagent and the current 723-residue natural product. Original GOA, UniProt, publication/provider files and prior history remain unchanged.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: every existing annotation, the description and the core functions were re-examined for ProtNLM2 benchmark target Q9Y6K1 (cohorts HORSE40 and HORSE40_HUMAN_PAIR). No ProtNLM2 output or prediction-evidence file was opened or used.

Identity: Q9Y6K1 is the reviewed, canonical Swiss-Prot entry for human DNMT3A (isoform 1, 912 aa, sequence version 4), with the PWWP, ADD and C5-methyltransferase domains and the catalytic Cys710 (UniProt active-site feature). It is not a fragment, isoform or alternative gene model. Products 2 (723 aa) and 3 (166 aa) are already described under `alternative_products`.

Evolutionary grounding: UniProt places Q9Y6K1 in PANTHER PTHR23068:SF10 (DNA (cytosine-5)-methyltransferase 3A). The family review `interpro/panther/PTHR23068/PTHR23068-review.yaml` lists the same subfamily, with human DNMT3A as reference protein and DNMT3L in SF13 as the diverged noncatalytic branch; there is no disagreement about placement. Mouse Dnmt3a (O88508) is in the same subfamily, which is the basis for every mouse-to-human transfer below. The IBA rows (DNA cytosine-5 methyltransferase activity, nucleus, cytoplasm, negative regulation of DNA-templated transcription) come from PAINT nodes that are ancestors of the target and were left as previously assessed.

Changes in this pass:

- **Rat-derived response terms.** QuickGO shows that every rat donor annotation behind the Ensembl Compara (GO_REF:0000107) response-to-X rows is IEP. These are xenobiotic stimulus (PMID:16632870, 21682946), toxic substance (23433207), ionizing radiation (17148264), estradiol (22334722), vitamin A (23333085), cocaine (23688924) and hepatocyte apoptotic process (19833194). An expression change makes DNMT3A a readout of the exposure, not a component that performs the response. The seven rows moved from UNDECIDED to MARK_AS_OVER_ANNOTATED, matching the lead, nutrient and ethanol rows that were already marked that way. The hypoxia rows stay as they were because a Dnmt3a-selective knockdown is available (PMID:23516428).
- **Neuron differentiation** (rat IEP donor PMID:19660178). It stays KEEP_AS_NON_CORE, but its support is now independent mouse evidence [PMID:20651149 "Thus, specific and cell-autonomous functions of Dnmt3a are required for neurogenesis from postnatal NSCs."]. In that study a catalytically inactive mutant fails to rescue the defect, so DNMT3A contributes to the process through its methylation activity. The donor itself is marked SOURCE_WEAK_OR_INFERRED.
- **Catalytic complex, GO:1902494** (IPI PMID:25383530). Changed from KEEP_AS_NON_CORE to MODIFY, with GO:0140020 DNA methyltransferase complex as the replacement. The earlier review kept the generic parent because it assumed no named GO complex existed. GO:0140020 does exist, it is an is_a descendant of catalytic complex, and its definition fits the DNMT3A–DNMT3L heterotetramer. Added it as `in_complex` on the catalytic core function.
- **NEW genomic imprinting, GO:0071514** (ISO from mouse, PMID:15215868). Germline Dnmt3a conditional knockout abolishes methylation and allele-specific expression at all maternally imprinted loci examined and at two of three paternal loci [PMID:15215868 "both Dnmt3a and Dnmt3L are required for methylation of most imprinted loci in germ cells"]. The imprint is the methylation mark that DNMT3A deposits, so this is participation, not just necessity. Comparator check: mouse Dnmt3a carries the term (IMP, this paper), and mouse Dnmt3l and human DNMT3L carry it (human DNMT3L by ISS and IEA). Human DNMT3A did not, so the activator had the term and the catalytic subunit did not. The term is not an ancestor or descendant of GO:0044027 or GO:0140003. It was also added as a second replacement on the broad InterPro "regulation of gene expression" row and to the catalytic core function's `directly_involved_in`. The description gained one sentence on the DNMT3L complex and germline imprints.

Deliberately unchanged:

- The 17 bare GO:0005515 rows kept as KEEP_AS_NON_CORE. These follow the user's standing ClinGen-project instruction in `projects/CLINGEN_MENDELIAN.md`, which is why the validator warns on them. I did not override a user instruction from inside a different campaign.
- GO:0006346 constitutive heterochromatin. It remains KEEP_AS_NON_CORE on the mouse pericentric-satellite rescue (PMID:15456878).
- piRNA-directed TE methylation. It remains KEEP_AS_NON_CORE; mouse SPOCD1 complex, PMID:32674113.
- Protein-cysteine methyltransferase. It remains a non-core automethylation side reaction.
- Nuclear matrix. It remains UNDECIDED (the source is abstract-only).

Relative for the next review: mouse Dnmt3a (O88508), an ortholog in the same PANTHER subfamily (SF10). It is the experimentally richest DNMT3A ortholog: de novo methylation, imprinting, pericentric methylation, neurogenesis and germline TE methylation. The repo has no review for it; genes/mouse has only Dnmt1. Existing paralog reviews are human DNMT3B, DNMT3L and DNMT1; horse DNMT3A and DNMT3L are reviewed too.

Modules: no module in `modules/` includes DNMT3A as a part. `modules/pirna_mediated_germline_silencing.yaml` names the mammalian methylation machinery (SPOCD1, DNMT3C, DNMT3L), but only in prose, and it does not list DNMT3A.
