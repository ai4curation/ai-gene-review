# Epe1 GO Annotation Review Summary

## Overview
Completed review of 33 existing GO annotations for S. pombe Epe1. No histone demethylase activity has been detected for purified Epe1, its JmjC Fe(II) triad is non-canonical, and its characterized anti-silencing mechanisms involve protein interactions; whether it has latent or in vivo catalytic activity is unresolved.

## Key Findings

### Propagated catalytic annotations removed (4 annotations)
1. **GO:0032452** (histone demethylase activity, IBA) - REMOVE
2. **GO:0140680** (histone H3K36me/H3K36me2 demethylase activity, IEA) - REMOVE
3. **GO:0016491** (oxidoreductase activity, IEA) - REMOVE
4. **GO:0051213** (dioxygenase activity, IEA) - REMOVE

What is removed is the PAINT/keyword inference of canonical JHDM1-type activity, not a claim that latent activity is excluded.

### Annotations left undecided (3 annotations)
- **GO:0032454** (histone H3K9 demethylase activity) x2 - UNDECIDED (IDA/EXP from PMID:25838386; in vivo genetic evidence, catalysis disputed; not removed, flagged for discussion with PomBase)
- **GO:0046872** (metal ion binding, IEA) - UNDECIDED (UniProt Metal-binding keyword, resting on its BINDING 297/299 Fe cation features, which are themselves predicted from the JmjC ProRule PRU00538; H297 and E299 are retained, the third His ligand is Y370, and metal binding has not been measured)

**Rationale**:
- No demethylase activity detected in vitro (Tsukada 2006, PMID:16362057; Raiymbek 2020, PMID:32195666)
- Non-canonical Fe(II) ligand set: the JmjC triad is H297-E299-Y370, with Tyr370 in place of the third (His) iron ligand of canonical HX(D/E)...H demethylases
- The H297A Fe(II)-site mutant does not settle the question, and its phenotype depends on the assay: at endogenous levels it behaves like epe1Δ in erasing tethering-induced H3K9me (Audergon 2015, PMID:25838386) and fails to remove established ectopic heterochromatin while still suppressing variegation (Sorida 2019, PMID:31206516); only when overexpressed does it still disrupt pericentric silencing, in a SAGA-dependent way (Bao 2019, PMID:30573453)
- C-terminus alone (without JmjC) can disrupt heterochromatin (Raiymbek 2020, PMID:32195666)
- The PHF2 JmjC domain carries a similar anomaly yet has latent, phosphorylation-activated demethylase activity (noted by Audergon 2015), which is why the experimental rows are not removed
- Counter-evidence to a purely non-catalytic reading. The JmjC domain is essential for Epe1 activity in complementation experiments (Ayoub 2003, PMID:12773576), and Epe1's effect on Pol II accessibility requires the JmjC domain (Zofall and Grewal 2006, PMID:16762840), although Zofall and Grewal note the mechanism may differ from that of demethylase JmjC proteins. UniProt records Y307A as loss of function from the same Ayoub paper (MUTAGEN 307, its only mutagenesis record; Raiymbek groups Y307 with residues affecting Fe(II) or alpha-ketoglutarate binding); it may reflect the same Ayoub experiment, so it is not an independent line of evidence. Raiymbek 2020 (PMID:32195666) propose a non-catalytic H3K9me-reading role for the domain. The strongest independent result is Sorida 2019 (PMID:31206516): H297A, a UniProt Fe ligand, still suppressed variegation (the de novo arm) but entirely failed to remove already-established ectopic heterochromatin, a separation of function read out as H3K9me in vivo, which a folding defect would not predict. Wang 2015 (PMID:25774602) read epe1-H374A and epe1-Y307A as enzymatically dead (residue 374 of UniProt O94603 is Thr, so the mutated histidine cannot be identified from the cache). No study has measured enzymatic demethylation directly, and the same mutations also weaken Swi6 binding and heterochromatin localization. The REMOVE rows rest on the undetected in vitro activity and the non-canonical triad; this genetic evidence is what the UNDECIDED GO:0032454 rows reflect.

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

Protein acetylation (GO:0006473) is not proposed: Gcn5 in SAGA performs the acetylation, and Epe1's part is captured by GO:0035035. Negative regulation of heterochromatin formation (GO:0031452) is not proposed either. PomBase curated Epe1's anti-silencing role as seven experimental GO:0033696 heterochromatin boundary formation rows and did not add GO:0031452, which we read as a curation convention rather than a gap. The tension with SGD's IMP annotation of DOT1 to GO:0031452 is raised as a suggested question for PomBase, as is the NOT GO:0031507 row, since GO:0031507 is an ancestor of GO:0033696. Nucleosome organization (GO:0034728) is not proposed either: epe1 deletion reduces heterochromatic histone turnover, which shows Epe1 is necessary for normal turnover, but the disassembly and reassembly are performed by chaperones and remodelers such as FACT, and by GOA convention GO:0034728 is annotated to such chaperones and remodelers. Epe1 therefore fails the participation test for a NEW process term, and its turnover role is described in core function 4 without one.

### Annotations Accepted (23 annotations)
Predominantly cellular component and biological process annotations that accurately reflect Epe1's localization and function:
- Heterochromatin boundary formation (multiple evidence)
- Nuclear and heterochromatin localization
- Regulation of transcription by RNA polymerase II
- Transcription coregulator activity
- NOT heterochromatin formation (GO:0031507, negated IDA); OLS lists GO:0031507 as an ancestor of GO:0033696, so this row sits uneasily with the positive boundary rows, and the tension is raised with PomBase

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
- **Knowledge gap**: Histone binding by Epe1 is directly shown (purified Epe1 preferentially binds H3K9me3 peptides and H3K9-methylated histones in vitro), and Raiymbek et al. place this H3K9me recognition in the JmjC domain (PMID:32195666). Whether the JmjC domain also contributes catalysis is unresolved. The domain is required for Epe1 activity (PMID:12773576) and for its effect on Pol II accessibility (PMID:16762840), UniProt records Y307A as loss of function (from the same Ayoub paper, possibly the same experiment as the domain-essential statement), and Wang et al. interpret active-site mutant phenotypes as enzymatic redundancy with Mst2 (PMID:25774602), and Sorida et al. show that H297A separates the de novo arm (intact) from removal of established ectopic heterochromatin (lost) (PMID:31206516), but no study has measured enzymatic demethylation directly. How Epe1 increases nucleosome turnover is also not known, and no study has shown that its histone binding drives turnover. The more specific GO:0062072 histone H3K9me2/3 reader activity is not used for this core function because no study links Epe1's H3K9me binding to the turnover outcome.
- **Open question**: No study has measured an Epe1 enzymatic activity or separated the JmjC domain's binding and catalytic contributions in vivo. The mechanism linking Epe1's H3K9me-histone binding to nucleosome turnover in heterochromatin is unknown, as is how GO should represent an upstream promoter of heterochromatic histone turnover. By GOA convention GO:0034728 nucleosome organization is annotated to the chaperones and remodelers that do the work (for example the FACT subunits), and positive regulation of histone exchange (GO:1900051) is obsolete.

### 5. Transcription of Heterochromatic Repeats
- **Molecular Function**: Transcription coregulator activity (GO:0003712)
- **Process**: Regulation of regulatory ncRNA-mediated heterochromatin formation (GO:0010964)
- **Description**: Enables transcription of heterochromatic repeats for RNAi-mediated heterochromatin establishment

## Evidence Base
- 18 PMID references cited in the review
- Deep research synthesis incorporated
- UniProt annotations considered
- Multiple experimental approaches evaluated (genetics, biochemistry, proteomics)

## Critical Corrections Made
The most significant correction was removing the propagated (IBA/IEA) demethylase, oxidoreductase and dioxygenase annotations, which rest on JmjC domain presence alone. The electronic metal ion binding row is UNDECIDED, because the Fe(II) ligands it rests on are rule-predicted and binding has not been measured, and the PomBase experimental GO:0032454 rows are also UNDECIDED rather than overruling curators who read the full text. Epe1 is best described as a JmjC protein whose catalytic activity has never been detected and whose known functions have not been shown to require it.

## Validation Status
✓ File passes schema validation
✓ All annotations have detailed review justifications
✓ Core functions defined with appropriate GO terms
✓ Supporting evidence documented