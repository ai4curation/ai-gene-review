# FDH1 (YOR388C) notes

UniProt Q08911; NAD+-dependent formate dehydrogenase, EC 1.17.1.9 [UniProt:Q08911].

## Evidence journal
- Cytosolic, formate-inducible NAD-FDH [PMID:11921099 "Enzyme assays confirmed the presence of a formate-inducible, cytosolic and NAD(+)-dependent formate dehydrogenase"].
- FDH2 is a second structural gene in CEN.PK, but truncated into two ORFs (YPL275W/YPL276W) in the S288C genome [PMID:11921099 "the presence of two single-nucleotide differences led to two truncated ORFs rather than the full-length FDH2 gene"]; fdh1 fdh2 lacks activity [PMID:11921099 "an fdh1Deltafdh2Delta double mutant lacked formate dehydrogenase activity and was unable to co-consume formate"].
- Role: detoxification of exogenous formate [PMID:11921099 "These findings are consistent with a role of formate dehydrogenase in the detoxification of exogenous formate"]; fdh1 fdh2 cells secrete formate [PMID:19564482 "In the absence of FDH1 and FDH2 , intracellular formic acid is balanced by secretion into the media"].
- Absolute NAD+ specificity via Asp196/Tyr197 [PMID:12144528 "Asp(196) and Tyr(197) mediate the absolute coenzyme specificity of SceFDH for NAD(+)"].
- FDH1 overexpression accelerates formic acid breakdown [PMID:21246355 "This modification allowed the yeast to rapidly decompose excess formic acid"].

## Decisions
- Core: GO:0008863 / formate catabolic process GO:0042183 / cytosol.
- GO:0046294 formaldehyde catabolic process (RCA from YeastPathways formaldehyde oxidation II) KEEP_AS_NON_CORE: FDH1 acts on formate downstream of the formaldehyde-consuming steps (SFA1, YJL068C) and on formate from other sources; no cached evidence of a formaldehyde phenotype.
- NAD binding KEEP_AS_NON_CORE.
