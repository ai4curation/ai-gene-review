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
