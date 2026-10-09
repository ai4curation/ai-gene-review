# msl-1 (P50535) review notes

## Structure / scaffold
- MSL1 dimer binds two MSL2. [PMID:23084835 "two MSL2 subunits bind to a dimer formed by two molecules of MSL1"]
- Dimerization needed for X targeting/spreading; promoter binding independent. [PMID:23084835 "ChIP experiments revealed that Msl1 dimerization is essential for targeting and spreading of the MSL complex on X-linked genes"]
- Scaffold for MSL2, MOF, MSL3. [PMID:34943924 "MSL1 dimerizes and serves as a scaffold with binding sites for MSL2, Males absent on the First (MOF), and Male Specific Lethal 3 (MSL3)"]
- Substrate of MSL2 E3 ligase. [PMID:23084835 "We show that Msl1 is a substrate for Msl2 E3 ubiquitin ligase activity."]

## Localization
- X chromosome, same pattern as MLE. [PMID:8288132 "We have found that MLE and MSL-1 bind to the X chromosome in an identical pattern"]
- 3' bias. [PMID:18510926 "on the male X chromosome, where MSL1 and MSL3 are preferentially associated with the 3' end of dosage compensated genes"]
- ChIP-chip >700 regions. [PMID:16547172 "More than 700 binding regions for the DCC were observed, encompassing more than half the genes found on the X chromosome."]

## Curation decisions
- DNA binding / cis-regulatory region binding (ChIP-based; no DNA-binding domain) MODIFY -> chromatin binding.
- Chromatin binding KEEP_AS_NON_CORE (shared with msl-2, mle, mof).
- GO:0046536 -> GO:0016456; GO:1902562 -> GO:0072487.
- Protein binding (Tamo study) REMOVE.
- Core MF: protein-macromolecule adaptor activity (scaffold), ACCEPT IBA/ISS.
