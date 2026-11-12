# thiG (PP_5104, Q88CS6) notes

Session 2026-11-12. Deep-research providers were not available in this session, so there is
no `thiG-deep-research-*.md` file. Sources were the cached UniProt record, cached
publications, the PSEPK thiamine pathway report
(`projects/P_PUTIDA/deep-research/PSEPK__thiamine_diphosphate_biosynthesis__ppu00730-deep-research-openscientist.md`),
QuickGO and a local alignment (`thiG-bioinformatics/`).

## Identity and family
- Swiss-Prot THIG_PSEPK, 270 aa, PE 3. HAMAP MF_00443, Pfam PF05690, IPR008867, PANTHER
  PTHR34266:SF2. All functional text comes from the HAMAP rule
  [file:PSEPK/thiG/thiG-uniprot.txt "Catalyzes the rearrangement of 1-deoxy-D-xylulose 5-phosphate (DXP) to produce the thiazole phosphate moiety of thiamine."].
- The Schiff-base active site is Lys112 [file:PSEPK/thiG/thiG-uniprot.txt "Schiff-base intermediate with DXP"].
- Alignment: 44% identity to E. coli ThiG and 52% to B. subtilis ThiG. The active-site Lys and the DXP-binding
  residues are conserved; ref Thr205/208 is Ser222 here [file:PSEPK/thiG/thiG-bioinformatics/RESULTS.md].

## Biochemistry (E. coli ortholog, abstracts only)
- ThiG is genetically required for the thiazole [PMID:8432721 "The thiE, thiF, thiG, and thiH gene products are required for synthesis of the thiazole."].
- ThiGH forms a complex [PMID:12650933 "ThiG and ThiH-His co-purify as a large multimeric non-covalent complex"].
- The activity was reconstituted with purified ThiGH and ThiFS, and it requires ThiS thiocarboxylate
  [PMID:17403671 "yield dehydroglycine, which is required by ThiG for the thiazole cyclization reaction."].

## KT2440 context
- KT2440 uses ThiO (PP_0612), not ThiH, for the imine [PMID:26875494 "Glycine oxidase, encoded by the thiO gene, participates in the biosynthesis of thiamin by providing glyoxyl imine to form the thiazole moiety of thiamin."].
  No ThiH-family protein exists among the PSEPK UniProt files in the repo. The ThiGH complex (GO:1902508) placed by the
  PTHR34266 IBD at PTN002152321 therefore cannot form in KT2440 (or in B. subtilis, which also uses ThiO).
- The ThiS carrier is PP_5105 (Q88CS5), the next locus. EMBL protein ids are AAN70669.1 (thiG) and AAN70670.1 (ThiS).
- No ThiF: the ThiS activation enzyme is unresolved (MoeB/PP_0735 is a candidate).
- GOA has no IBA rows for Q88CS6, although Q88CS6 is a PTHR34266:SF2 member in the PANTHER entries file.

## Decisions
- ACCEPT cytoplasm, thiamine biosynthetic process (not entailed by GO:0009229; checked), TDP biosynthesis and thiazole synthase activity.
- MODIFY sulfurtransferase activity to GO:1990107, which is an is_a child (checked).
- NEW GO:0052837 thiazole biosynthetic process (ThiG catalyses ring formation). Comparator: ThiS orthologs carry it, and
  ThiG orthologs carry only GO:0009228/GO:0009229 (QuickGO, 2026-11-12).
