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

### Annotations Modified for Specificity (2 annotations)
1. **GO:0005515** (protein binding) → More specific binding terms
2. **GO:0006338** (chromatin remodeling) → More specific mechanisms

### Annotations Accepted (24 annotations)
Predominantly cellular component and biological process annotations that accurately reflect Epe1's localization and function:
- Heterochromatin boundary formation (multiple evidence)
- Nuclear and heterochromatin localization
- Regulation of transcription by RNA polymerase II
- Transcription coregulator activity
- NOT heterochromatin formation (GO:0031507, negated IDA)

## Core Functions Identified

### 1. Heterochromatin Boundary Establishment
- **Molecular Function**: Histone binding (GO:0042393)
- **Process**: Heterochromatin boundary formation (GO:0033696)
- **Mechanism**: Binds HP1/Swi6 at heterochromatin sites, recruits Bdf2

### 2. Transcriptional Co-activation
- **Molecular Function**: Transcription coregulator activity (GO:0003712)
- **Process**: Regulation of transcription (GO:0006357)
- **Mechanism**: Recruits SAGA histone acetyltransferase complex

### 3. Anti-silencing Activity
- **Molecular Function**: Modification-dependent protein binding (GO:0140030)
- **Process**: Negative regulation of heterochromatin (GO:0031452)
- **Mechanism**: Competes with silencing factors for HP1 binding

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