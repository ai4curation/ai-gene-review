# Rice IRX10 (OsIRX10 / BC18 / FC19) notes, 2026-10-30

Comparator review for the IRX10 family (see genes/ARATH/IRX10, genes/ARATH/IRX10L
and modules/xylan_biosynthesis.yaml). Deep research was not available in this
session; the review uses cached papers.

- Identity: Q8S1X7 = LOC_Os01g70200 = Os01g0926700 [PMID:39663842
  "LOC_Os01g70200 ( IRX10/BC18 )"]. PANTHER puts it in PTHR11062:SF200 with
  Arabidopsis IRX10L. UniProt still names it "Probable glucuronosyltransferase
  Os01g0926700", a legacy GT47 name.
- Activity: recombinant IRX10 polymerises xylooligosaccharides; XOAT6 boosts this
  [PMID:39663842 "Therefore, XOAT6 facilitates chain polymerization mediated by
  IRX10"].
- Mutants: Osirx10 (PMID:23180670), bc18 (PMID:39663842) and CRISPR fc19
  (PMID:37429191) all have less culm xylan and brittle or fragile culms.
- GOA had only IBA/IEA rows and no specific MF; added GO:0047517 as NEW (IDA,
  PMID:39663842). Removed the InterPro2GO glycoprotein biosynthesis row.
- Unresolved: Zhang et al. 2014 (PMID:24723033) "OsGT47A" complements
  Arabidopsis irx10 irx10L; the cached abstract does not give its locus, so it is
  not attributed to Q8S1X7 here.
- Grass xylan is glucuronoarabinoxylan; GO has no term for it, so the IBA
  glucuronoxylan term is kept (GAX does carry GlcA).
