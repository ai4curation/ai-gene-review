# J7SF87 (sqrd-2) review notes

## 2026-10-28 session

- Fetched worm/J7SF87; UniProt id J7SF87 confirmed (Y9C9A.16b, WBGene00021183, GeneID 189421);
  GOA has 6 rows keyed to J7SF87. No accession switch.
- No deep-research keys; literature summary in J7SF87-deep-research-manual.md.
- Key papers: PMID:23484030 (gei-8; names sqrd-2), PMID:21840852 (Budde & Roth; sqrd-2 deletion
  not H2S-sensitive), PMID:39178951 (Romanelli-Cedrez; sqrd-2 expressed, mutant recovers early,
  docking of UQ/RQ). PMID:26677221 is sqrd-1 only.
- Sequence: catalytic Cys169/Cys351 and FAD motif retained, so not a pseudoenzyme
  [file:worm/J7SF87/J7SF87-bioinformatics/RESULTS.md]. No N-terminal presequence.
- Decisions: GO:0070224 rows MODIFY to GO:0106436 (animal type II SQR transfers sulfane sulfur to
  glutathione; GO:0070224 is defined by free S0 release; sibling, not parent, checked in OLS);
  GO:0106436 ACCEPT; FAD binding KEEP_AS_NON_CORE; mitochondrion rows ACCEPT by subfamily
  (PTHR10632:SF2) and function, no sub-compartment added (only homology supports inner membrane).
- No NEW sulfide oxidation (GO:0019418) row. The sqrd-1 review added it, and the participation
  test would pass if SQRD-2 is an active SQR, but the activity is purely inferred and the only
  in vivo data (no H2S sensitivity; early recovery) do not show SQRD-2 doing sulfide oxidation.
  UniProt still lists the obsoleted IBA GO:0070221 (not in GOA). Left as a suggested question.
- gei-8 / gonad phenotypes: not annotated (RNAi region contains 21U-RNA loci; modifier
  phenotype in a mutant background only).
