# sua1 (SPBC27.08c, UniProt P78937) notes

Naming: PomBase `sua1` (synonyms asp1, met3) is the ortholog of S. cerevisiae MET3
(ATP sulfurylase). UniProt entry name MET3_SCHPO. Do not confuse with pombe numbering of
other met genes.

## Evidence journal

- Activity: ATP sulfurylase, sulfate + ATP -> APS + PPi (EC 2.7.7.4, RHEA:18133)
  [UniProt:P78937 "FUNCTION: Catalyzes the first intracellular reaction of sulfate"]
  (HAMAP rule MF_03106; homohexamer, dimer of trimers by rule).
- Genetics: selenate-resistant mutants of one complementation group are low in sulfate
  uptake and ATP sulfurylase activity and cannot use sulfate
  [PMID:14723223 "They were low in sulphate uptake activity and in ATP
  sulphurylase activity."].
- Cloning by complementation restored sulfate assimilation and ATP sulfurylase levels
  [PMID:18388974 "The open reading frame encoding the ATP sulphurylase enzyme was found to be
  responsible for the restoration of sulphate assimilation."]; sua1 also complements
  S. cerevisiae met3 [PMID:18388974 "The cloned sua1 gene also complemented the met3 (ATP
  sulphurylase deficient) mutation in Saccharomyces cerevisiae."].
- Localization: cytosol in the ORFeome YFP screen (PMID:16823372, HDA), cytoplasm by HAMAP.
- PomBase GO-CAM gomodel:66a3e0bb00001342 activity 66a3e0bb00001368: sua1 enables
  GO:0004781, occurs in cytosol, part_of GO:0000103 sulfate assimilation.
- Module: aps_dependent_assimilatory_sulfate_reduction, step 1 (homo-oligomeric Sat/Met3
  variant). S. cerevisiae ortholog MET3 core function = GO:0004781 in cytoplasm, part of
  sulfate assimilation; this review is consistent with it.

## Observations
- GO:0070814 hydrogen sulfide biosynthetic process (UniPathway UPA00140) is an upstream
  framing; kept non-core, as for MET3.
- The GOA IMP rows for GO:0004781 rest on mutant enzyme-activity measurements
  (PMID:14723223) and complementation (PMID:18388974); no purified-enzyme kinetics for the
  pombe protein are known to me.
