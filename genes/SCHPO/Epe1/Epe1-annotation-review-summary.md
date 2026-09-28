# Epe1 GO Annotation Review Summary

## Overview
Completed review of 33 existing GO annotations for S. pombe Epe1. No histone demethylase activity has been detected for purified Epe1, its JmjC Fe(II) triad is non-canonical, and its known anti-silencing mechanisms act through protein interactions; whether it has latent or in vivo catalytic activity is unresolved.

## Key Findings

### Propagated catalytic annotations removed (4 annotations)
1. **GO:0032452** (histone demethylase activity, IBA) - REMOVE
2. **GO:0140680** (histone H3K36me/H3K36me2 demethylase activity, IEA) - REMOVE
3. **GO:0016491** (oxidoreductase activity, IEA) - REMOVE
4. **GO:0051213** (dioxygenase activity, IEA) - REMOVE

What is removed is the PAINT/keyword inference of canonical JHDM1-type activity, not a claim that latent activity is excluded.

### Annotations left undecided (3 annotations)
- **GO:0032454** (histone H3K9 demethylase activity) x2 - UNDECIDED (IDA/EXP from PMID:25838386; in vivo genetic evidence, catalysis disputed; not removed, flagged for discussion with PomBase)
- **GO:0046872** (metal ion binding, IEA) - UNDECIDED (UniProt Metal-binding keyword, resting on its BINDING 297/299 Fe cation features; H297 and E299 are retained, the third His ligand is Y370, and metal binding has not been measured)

**Rationale**:
- No demethylase activity detected in vitro (Tsukada 2006, PMID:16362057; Raiymbek 2020, PMID:32195666)
- Non-canonical Fe(II) ligand set: the JmjC triad is H297-E299-Y370, with Tyr370 in place of the third (His) iron ligand of canonical HX(D/E)...H demethylases
- The H297A Fe(II)-site mutant does not settle the question, and its phenotype depends on the assay: at endogenous levels it behaves like epe1Δ in erasing tethering-induced H3K9me (Audergon 2015, PMID:25838386) and fails to remove established ectopic heterochromatin while still suppressing variegation (Sorida 2019, PMID:31206516); only when overexpressed does it still disrupt pericentric silencing, in a SAGA-dependent way (Bao 2019, PMID:30573453)
- C-terminus alone (without JmjC) can disrupt heterochromatin (Raiymbek 2020, PMID:32195666)
- The PHF2 JmjC domain carries a similar anomaly yet has latent, phosphorylation-activated demethylase activity (noted by Audergon 2015), which is why the experimental rows are not removed

### Annotation Modified for Specificity (1 annotation)
1. **GO:0005515** (protein binding, IPI with Cdt2) → GO:0031625 ubiquitin protein ligase binding

### Annotations Kept as Non-core (2 annotations)
- **GO:0006325** (chromatin organization, IEA): correct but generic. The specific process is GO:0033696 heterochromatin boundary formation (seven ACCEPTed experimental rows), which lies below it.
- **GO:0006338** (chromatin remodeling, IBA): correct but generic, for the same reason: GO:0033696 also lies below it, so no replacement is proposed. Epe1's role in heterochromatic nucleosome turnover is described in core function 4 without a process term.

### Proposed New Annotations (4 NEW rows)
1. **GO:0070087** chromo shadow domain binding (IPI, PMID:32195666): recombinant Epe1 binds Swi6, reduced by the Swi6 CSD mutation L315E; replaces the earlier GO:0140030, whose definition requires the modification on the bound protein itself
2. **GO:0035035** histone acetyltransferase binding (IPI, PMID:30573453): SAGA co-purifies with Epe1 and Gcn5 co-immunoprecipitates with overexpressed Epe1
3. **GO:0030674** protein-macromolecule adaptor activity (IMP, PMID:24013502): Epe1 binds Bdf2 and is required for its recruitment to IRC boundaries
4. **GO:0042393** histone binding (IDA, PMID:32195666): purified Epe1 prefers H3K9me3 peptides and H3K9-methylated histones

Protein acetylation (GO:0006473) is not proposed: Gcn5 in SAGA performs the acetylation, and Epe1's part is captured by GO:0035035. Negative regulation of heterochromatin formation (GO:0031452) is not proposed either. PomBase curated Epe1's anti-silencing role as seven experimental GO:0033696 heterochromatin boundary formation rows and did not add GO:0031452, which we read as a curation convention rather than a gap. The tension with SGD's IMP annotation of DOT1 to GO:0031452 is raised as a suggested question for PomBase, as is the NOT GO:0031507 row, since GO:0031507 is an ancestor of GO:0033696.

### Annotations Accepted (23 annotations)
Predominantly cellular component and biological process annotations that accurately reflect Epe1's localization and function:
- Heterochromatin boundary formation (multiple evidence)
- Nuclear and heterochromatin localization
- Regulation of transcription by RNA polymerase II
- Transcription coregulator activity
- NOT heterochromatin formation (GO:0031507, negated IDA)

## Core Functions Identified

### 1. Swi6/HP1 Binding at Heterochromatin
- **Molecular Function**: Chromo shadow domain binding (GO:0070087)
- **Process**: Heterochromatin boundary formation (GO:0033696)
- **Description**: Binds HP1/Swi6 at H3K9-methylated heterochromatin through C-terminal domain to antagonize silencing. Raiymbek et al. show that expressing the Epe1 C-terminus alone is sufficient to disrupt heterochromatin by outcompeting the histone deacetylase Clr3 from sites of heterochromatin formation, through this Swi6 interaction.

### 2. SAGA Recruitment
- **Molecular Function**: Histone acetyltransferase binding (GO:0035035)
- **Process**: Regulation of transcription by RNA polymerase II (GO:0006357)
- **Description**: Recruits SAGA histone acetyltransferase complex to heterochromatin for H3 acetylation

### 3. Bdf2 Recruitment to Boundaries
- **Molecular Function**: Protein-macromolecule adaptor activity (GO:0030674)
- **Process**: Heterochromatin boundary formation (GO:0033696)
- **Description**: Recruits Bdf2 bromodomain protein to heterochromatin boundaries to recognize acetylated histones

### 4. Nucleosome Turnover
- **Molecular Function**: Histone binding (GO:0042393)
- **Process**: none asserted (see description and suggested questions)
- **Description**: Promotes nucleosome turnover at heterochromatin to destabilize silencing marks. Heterochromatic histone turnover is reduced when epe1 is deleted, but the chaperones and remodelers that perform nucleosome disassembly and reassembly (such as FACT) are other proteins, and Epe1's route to turnover is unknown, so no process term is asserted for this role.
- **Knowledge gap**: Histone binding by Epe1 is directly shown (purified Epe1 preferentially binds H3K9me3 peptides and H3K9-methylated histones in vitro), but how Epe1 increases nucleosome turnover is not known, and no study has shown that this histone binding is the activity that drives turnover. The more specific GO:0062072 histone H3K9me2/3 reader activity is not used for this core function because no study links Epe1's H3K9me binding to the turnover outcome. Mechanism linking Epe1's H3K9me-histone binding to nucleosome turnover in heterochromatin, and how an upstream promoter of heterochromatic histone turnover should be represented in GO. GO nucleosome organization (GO:0034728) is carried by the chaperones and remodelers that do the work, and positive regulation of histone exchange (GO:1900051) is obsolete.

### 5. Transcription of Heterochromatic Repeats
- **Molecular Function**: Transcription coregulator activity (GO:0003712)
- **Process**: Regulation of regulatory ncRNA-mediated heterochromatin formation (GO:0010964)
- **Description**: Enables transcription of heterochromatic repeats for RNAi-mediated heterochromatin establishment

## Evidence Base
- 33 peer-reviewed publications reviewed
- Deep research synthesis incorporated
- UniProt annotations considered
- Multiple experimental approaches evaluated (genetics, biochemistry, proteomics, ChIP-seq)

## Critical Corrections Made
The most significant correction was removing the propagated (IBA/IEA) demethylase, oxidoreductase and dioxygenase annotations, which rest on JmjC domain presence alone. The electronic metal ion binding row is UNDECIDED, because the Fe(II) ligands it rests on are rule-predicted and binding has not been measured, and the PomBase experimental GO:0032454 rows are also UNDECIDED rather than overruling curators who read the full text. Epe1 is best described as a JmjC protein whose catalytic activity has never been detected and whose known functions have not been shown to require it.

## Validation Status
✓ File passes schema validation
✓ All annotations have detailed review justifications
✓ Core functions defined with appropriate GO terms
✓ Supporting evidence documented