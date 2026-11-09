# fruA curation notes

## Boundary and evidence

FruA (Q88PQ3; PP_0795) is the membrane-bound EIIB-EIIC component of the
fructose-specific PTS. Its exact UniProt reaction is RHEA:49252 (EC 2.7.1.202):
external fructose is transported and phosphorylated to intracellular fructose
1-phosphate. KT2440 literature independently identifies FruA as the
membrane-bound EIIBC polyprotein and shows that FruB is required for FruA-
dependent fructose transport [PMID:27933319 "EIIBC (membrane bound, encoded by
fruA)"; PMID:18296519 "FruB mutants cannot transport fructose through the
two-domain (EIIB Fru and EIIC Fru ) FruA permease"].

The InterPro-derived carbohydrate:proton symporter annotation and its inferred
proton-transmembrane-transport process were removed. They conflict with the
protein-phosphorelay mechanism and exact Rhea reaction. Generic membrane and
sugar-transporter terms were marked over-annotated because the review retains
specific plasma-membrane and fructose-PTS terms.

## 2026-11-05 completion pass (Claude (AI-assisted))

- Deep research: `just deep-research PSEPK fruA --provider perplexity` failed
  ("Provider 'perplexity' not available"); no provider file was created. The
  review rests on the cached KT2440 papers (PMID:18296519, PMID:17416664,
  PMID:27933319) and the UniProt family/domain classification.
- Replaced quotes that rested on ARBA-only UniProt text (EC number, catalytic
  activity, subcellular location) or sequence fragments with publication text
  and InterPro/NCBIfam/PROSITE classification lines.
- Correct-but-general rows changed to MODIFY, matching the E. coli FruA review:
  GO:0008982 and GO:0051119 -> GO:0022877; GO:0016020 -> GO:0005886;
  GO:0015755 -> GO:1990539 fructose import across plasma membrane (also now the
  core process); GO:0090563 (TreeGrafter) -> GO:0090582, the same action taken
  on the E. coli IBA row. GO:0090582 is not added to core_functions here
  because the KT2440 EIIB cysteine has not been tested.
- Core MF stays GO:0022877. GO:0022877 and GO:0090582 are not is_a related:
  GO:0022877 is the overall Enzyme II reaction with the FruB phosphohistidine as
  donor (UniProt RHEA:49252, curated experimentally for E. coli FruA), and
  GO:0090582 is the EIIB phosphocysteine-to-fructose half-reaction.
- No PENDING/UNDECIDED rows remain; status set to COMPLETE.
