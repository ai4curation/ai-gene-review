# Ortholog Conjecture Project

## Overview
The ortholog conjecture (OC) posits that orthologs (genes separated by speciation) tend to retain more similar functions than paralogs (genes separated by duplication) at the same evolutionary distance. This assumption underpins many automated functional annotations and cross-species inference pipelines. The OC remains debated because different data types, bias controls, and evaluation metrics can yield opposite conclusions.

## GO Context (How Orthology Appears in Annotations)
GO annotations explicitly encode how an inference was made, and orthology appears directly in several mechanisms:

- `ISO` is a GO evidence code for inferences from sequence orthology. [GO evidence codes guide]
- GO phylogenetic annotations use PAINT/PANTHER and IBA/IBD, with explicit ancestral inference and traceability to experimental evidence. [GO_REF:0000033]
- Automated ortholog transfers are documented in GO_REFs, including OrthoMCL-based ISO transfers (GO_REF:0000101) and Ensembl Compara-based orthology transfers that yield IEA (GO_REF:0000107). [GO_REF:0000101; GO_REF:0000107]

These mechanisms mean the OC is not just theoretical; it affects annotation propagation, evidence reliability, and the risk of over-annotation.

## Research Summary (General)

### Evidence Challenging the OC
- Nehrt et al. (2011) found that within-species paralogs can show higher functional similarity than orthologs when assessed with GO annotations and microarray expression, motivating the “cellular context” hypothesis. [PMID:21695233]

### Methodological Cautions
- GO annotations are incomplete and biased by study design and annotation practices; therefore GO-based tests of the OC can be confounded, and negative results can be misleading. A 2012 analysis argued GO is currently inappropriate for testing the OC and highlighted annotation and study biases. [PMID:22359495; PMID:23209392]

### Evidence Supporting the OC
- When controlling for multiple confounders (authorship bias, GO term frequency, background similarity, and propagated annotation bias), orthologs show higher functional similarity than paralogs, especially for cellular component. [PMID:22615551]
- RNA-seq based analyses report higher expression similarity among orthologs than within-species paralogs, consistent with the OC. [PMID:23209392]

## Scope Clarification (Science-First)
This project is about the *science* of orthology vs functional divergence and how to measure it without circularity or annotation bias. It is **not** primarily a curation rulebook for reviewers; those guidelines belong at the repo level.

We will still use GO context and evidence codes as inputs, but the emphasis here is on building a reproducible, unbiased analysis of functional conservation/divergence.

## Project Goals (Science-Focused)
- Assemble literature-backed examples of functional divergence among orthologs (including neofunctionalization, subfunctionalization, domain loss, and subcellular relocalization).
- Build an “open world” curation lens: treat missing annotations as unknown, not absence, and separate *lack of evidence* from *evidence of loss*.
- Develop unbiased metrics for functional similarity that control for annotation bias (authorship, term frequency, propagated annotation bias) and compare GO-based metrics against expression- or phenotype-based signals.
- Identify gene families where orthology-based transfer likely overstates functional conservation, and quantify how often this happens under different evidence filters.

## Initial Workplan
1. Seed a case list from literature with concrete divergence signals (expression shifts, loss of replaceability, domain architecture changes) and tie each to explicit references.
2. Build ortholog sets across a few well-studied clades (1:1 and 1:many) and annotate which GO evidence codes dominate (ISO/IEA vs IBA/IBD vs experimental).
3. Implement open-world metrics: compute functional similarity using only experimental annotations, and separately include ISO/IBA to measure the impact of orthology-based transfer.
4. Compare GO-based similarity with orthogonal signals (RNA-seq expression similarity, phenotype concordance where available).
5. Summarize divergence rates and create a “bias checklist” so metrics can be interpreted correctly.

## Functional Divergence: Curated Cases (Evidence-Backed)
These are concrete ortholog divergence examples with gene-level evidence that can seed the "open world" curation set.

### CMAH (CMP-Neu5Ac hydroxylase)
Case: Human CMAH is inactivated; nonhuman primates retain functional CMAH.
Type: Loss-of-function ortholog (human lineage-specific).
Evidence: Human CMAH is inactive due to a deletion that removes a 92-bp exon; loss of Neu5Gc synthesis in humans has been directly linked to CMAH inactivation. [PMID:9751737; PMID:11562455]

### UOX (urate oxidase / uricase)
Case: UOX is inactivated in hominoids, but functional in many other mammals.
Type: Loss-of-function ortholog with independent inactivation events.
Evidence: Multiple nonsense mutations and splice defects in human and great ape UOX; evidence for independent inactivation in gibbon lineage. [PMID:11961098]

### GULO / GULOP (L-gulonolactone oxidase)
Case: Human and other primates lack functional GULO, preventing endogenous vitamin C synthesis.
Type: Loss-of-function ortholog / pseudogenization.
Evidence: Human GULO is a pseudogene with multiple mutations; primate nonfunctionalization documented at the sequence level. [PMID:1962571; PMID:10572964]

### CDC14 (Cdc14 phosphatase family)
Case: Budding yeast Cdc14 is essential for mitotic exit, but orthologs in fission yeast and vertebrates are not required for mitotic exit and show different cellular roles.
Type: Functional role shift across orthologs.
Evidence: Review of conserved family with non-conserved functions, including fission yeast Clp1 roles in cytokinesis control and vertebrate CDC14 non-essentiality for mitotic exit. [PMID:20720150]

### Arabidopsis - A. lyrata co-orthologs (expressolog study)
Case: Ortholog groups with multiple A. lyrata copies show divergence in expression and functional complementation compared to Arabidopsis.
Type: Neofunctionalization and nonfunctionalization after duplication within ortholog groups.
Evidence: Expressolog analysis across 286 A. lyrata duplicated gene groups and experimental complementation of 8 A. lyrata homologs in 4 Arabidopsis loss-of-function mutants; nonexpressologs fail to complement, indicating functional divergence. [PMID:27303025]

## Large-Scale Divergence Datasets (To Mine)
- Yeast-human replacement assays: only ~47% of essential yeast genes are functionally replaceable by their human orthologs; replaceability clusters by biological modules, providing a divergence filter for ortholog transfer. [PMID:25999509]
- Expressolog dataset (Arabidopsis vs. A. lyrata): one-to-one groups show higher expression correlation than one-to-many or many-to-many; includes gene-level validation via complementation. [PMID:27303025]

## Appendix: Lineage-Specific Loss (Not Used for OC Metrics)
These are *boundary cases* demonstrating that orthology does not guarantee functional retention. They are excluded from OC comparison metrics focused on subtle functional divergence.

### Human loss-of-function orthologs (UOX, GULOP/GULO)
Case: Humans lack functional urate oxidase (UOX) and L-gulonolactone oxidase; the human locus is annotated as the pseudogene GULOP.
Type: Lineage-specific loss-of-function with retained but inactive orthologous loci.
Evidence: UOX inactivation in the human/great ape clade is due to nonsense mutations identified in primate comparative sequencing. [PMID:11961098] Human L-gulono-γ-lactone oxidase exists as a pseudogene with accumulated mutations, and the human GULOP locus is annotated as nonfunctional. [PMID:10572964; NCBI GTR Gene:2989]

## Key References
- Nehrt NL et al. Testing the ortholog conjecture with comparative functional genomic data from mammals. PLoS Comput Biol. 2011. [PMID:21695233]
- Thomas PD et al. On the use of GO annotations to assess functional similarity among orthologs and paralogs: a short report. 2012. [PMID:22359495]
- Chen X, Zhang J. The ortholog conjecture is untestable by the current GO but is supported by RNA-seq data. 2012. [PMID:23209392]
- Altenhoff AM et al. Resolving the ortholog conjecture: orthologs tend to be weakly but significantly more similar in function than paralogs. 2012. [PMID:22615551]
- Gaudet P et al. Phylogenetic-based propagation of functional annotations within the GO consortium. Briefings in Bioinformatics. 2011. [PMID:21873635]
- Kachroo AH et al. Systematic humanization of yeast genes reveals conserved functions and genetic modularity. Science. 2015. [PMID:25999509]
- Expression Pattern Similarities Support the Prediction of Orthologs Retaining Common Functions after Gene Duplication Events. Plant Physiology. 2016. [PMID:27303025]
- Chou HH et al. Inactivation of CMP-N-acetylneuraminic acid hydroxylase occurred prior to brain expansion during human evolution. PNAS. 1998. [PMID:9751737]
- Hayakawa T et al. A human-specific gene inactivation involved in sialic acid biology. PNAS. 2001. [PMID:11562455]
- Oda M et al. Loss of urate oxidase activity in hominoids and its evolutionary implications. Mol Biol Evol. 2002. [PMID:11961098]
- Nishikimi M et al. Guinea pigs possess a highly mutated gene for L-gulono-gamma-lactone oxidase. Biochem Biophys Res Commun. 1991. [PMID:1962571]
- Ohta Y, Nishikimi M. Random nucleotide substitutions in primate nonfunctional GULO gene. J Mol Evol. 1999. [PMID:10572964]
- Mocciaro A, Schiebel E. Cdc14: a highly conserved family of phosphatases with non-conserved functions? J Cell Sci. 2010. [PMID:20720150]
- NCBI GTR Gene:2989 (GULOP pseudogene locus).
- GO evidence codes guide (Gene Ontology Consortium documentation).
- GO_REF:0000033. Annotation inferences using phylogenetic trees.
- GO_REF:0000101. Automated transfer of experimentally-verified GO annotation data to close orthologs.
- GO_REF:0000107. Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara.

---

# STATUS

## Completed
- [x] Build a seed list of divergence examples with citations (v0.1)

## Pending
- [ ] Define the open-world metric set and data filters
- [ ] Select ortholog datasets and clades for pilot analysis

Last updated: 2026-02-09

# NOTES

## 2026-02-09
Refocused project scope to investigate ortholog divergence science and unbiased metrics; added seed examples and open-world framing.

## 2026-02-09
Added a curated seed list of functional divergence cases with literature references.
