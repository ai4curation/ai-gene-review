# treSB curation notes

- Q88FN0 is a 1106-aa fusion with TreS/GH13 and maltokinase domain signatures. [file:PSEPK/treSB/treSB-uniprot.txt, "DR   InterPro; IPR012810; TreS/a-amylase_N."] [file:PSEPK/treSB/treSB-uniprot.txt, "DR   InterPro; IPR012811; TreS_maltokin_C_dom."]
- The TreS reaction is D-maltose to alpha,alpha-trehalose (EC 5.4.99.16; RHEA:15145). [file:PSEPK/treSB/treSB-uniprot.txt, "Reaction=D-maltose = alpha,alpha-trehalose"]
- The distinct maltokinase reaction is D-maltose + ATP to alpha-maltose 1-phosphate + ADP + H(+) (EC 2.7.1.175; RHEA:31915). [file:PSEPK/treSB/treSB-uniprot.txt, "Reaction=D-maltose + ATP = alpha-maltose 1-phosphate + ADP + H(+)"]
- The seeded GOA represents only the TreS activity. A NEW carbohydrate kinase annotation and a proposed substrate-specific maltokinase term were added so the fusion is not curated as monofunctional.
- PTHR10357 PAINT node PTN000039847 supports GO:0047471 in bacteria from the characterized Mycobacterium TreS seed P9WQ19. Q88FN0 and P9WQ19 are both verified members of PTHR10357:SF219. [file:interpro/panther/PTHR10357/PTHR10357-paint.tsv, "PTN000039847"] [file:interpro/panther/panther-members.tsv, "Q88FN0\tPTHR10357:SF219"]
- Mycobacterium experiments establish the conserved four-step TreS-Mak-GlgE-GlgB pathway, but they do not directly assay Q88FN0. [PMID:20305657 "We describe a new pathway from trehalose to alpha-glucan in Mycobacterium tuberculosis comprising four enzymatic steps mediated by TreS, Pep2, GlgE (which has been identified as a maltosyltransferase that uses maltose 1-phosphate) and GlgB."]
- No target-specific biochemical publication was present in the local publication cache; this uncertainty is recorded on both core functions.
- The fused Mak reaction produces the alpha-maltose 1-phosphate consumed by adjacent GlgE, so the protein is annotated to alpha-glucan biosynthesis. The reversible TreS leaf is not independently assigned that process. [file:PSEPK/treSB/treSB-uniprot.txt, "Reaction=D-maltose + ATP = alpha-maltose 1-phosphate + ADP + H(+)"] [file:PSEPK/glgE/glgE-uniprot.txt, "Maltosyltransferase that uses maltose 1-phosphate (M1P)"]

## OpenScientist reconciliation

Source: `file:PSEPK/treSB/treSB-deep-research-openscientist.md` (1,025.98 seconds).

- The report corroborates the bifunctional TreS-Mak fusion, both exact
  reactions, and placement immediately upstream of GlgE in the pathway.
- Its proposed catalytic-residue positions, sole-source and gatekeeper claims,
  operon interpretation, and transferred stress phenotypes are computational
  or ortholog-based inferences and were not promoted into the curated core
  functions.
- The report found no direct biochemical characterization of Q88FN0, so both
  catalytic assignments retain explicit target-specific knowledge gaps.
