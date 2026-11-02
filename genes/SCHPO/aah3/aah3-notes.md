# aah3 (Q9Y7S9, SPCC63.02c) review notes

## Identity
- GPI-anchored GH13 alpha-amylase-like protein, 564 aa; signal peptide 1-21, GPI-anchor at Ser538 (predicted), propeptide 539-564; catalytic nucleophile Asp229 and proton donor Glu253 (UniProt).
- PANTHER PTHR10357:SF224 (ALPHA-AMYLASE 3). Paralog Aah1 is SF215; the ISS donor A. niger AgtA (A2QTS4) is SF220.
- Local alignment: Aah3 vs AgtA 40.0% identity, Aah1 vs AgtA 41.9%, Aah3 vs Aah1 44.8% (aah3-bioinformatics/RESULTS.md).

## Evidence
- Location: [PMID:16751704 "Biochemical analysis showed that Aah3p is an N-glycosylated, GPI-anchored membrane protein localized in the membrane and cell wall fractions."] (abstract only).
- Catalytic residues needed in vivo: [PMID:16751704 "Expression of aah3 alleles in which the conserved aspartic acid and glutamic acid residues required for hydrolase activity were replaced with alanine residues failed to rescue the morphological and ascal wall defects of aah3Delta cells."]
- Ascal, not spore, wall in the abstract: [PMID:16751704 "Conjugation and sporulation were not affected by the aah3(+) deletion, but the ascal wall of aah3Delta cells was easily lysed by hydrolases."] This is why the ascospore wall biogenesis IMP row is non-core and flagged as a question.
- Redundancy: [PMID:40668835 "Thus, we concluded that Aah1 and Aah3 act redundantly and are the two S. pombe α-amylase homologs important for vegetative cell growth."]; aah2 and aah4 add nothing [PMID:40668835 "Combining aah2∆ or aah4∆ with aah1∆ aah3∆ did not result in any further growth defects (SI Appendix, Fig. S1)."]; mde5 was not tested [PMID:40668835 "We excluded mde5 from our analysis due to its meiotic-specific expression (38)."]
- Wall chemistry: [PMID:40668835 "Consequently, the overall α-1,3-glucan content declined markedly, from 44% in wildtype rigid cell walls to 11% in the aah1∆ aah3∆ mutant."]
- Relation to Ags1: [PMID:40668835 "We conclude that Aah1 and Aah3 enzymes are not functionally redundant with Ags1, and cells require both types of GH13 domain enzymes to support α-glucan chain assembly."]
- Activity is inferred, not measured: [PMID:40668835 "This suggests that Aah1 and Aah3 belong in a subclass of GH13 enzymes like the Aspergillus niger GPI-anchored GH13 enzymes that do not hydrolyze but rather exhibit 4-α-glucanotransferase (disproportionation) (30), moving glucan units between chains to adjust polymer length."]. The donor enzymology is [PMID:17496125 "The enzymes, designated AgtA and AgtB, produced new alpha-(1,4)-glycosidic bonds and therefore belong to the group of the 4-alpha-glucanotransferases (EC 2.4.1.25)."]

## Decisions
- 4-alpha-glucanotransferase activity (IEA, ISS): ACCEPT as core, but the core function and a BIOLOGY knowledge gap state that it is inferred. This differs from SPAC17G6.11c/Ghs2, where no Kre6-family member has ever been assayed; here a member of the GPI-anchored GH13 group (AgtA) was purified and characterized, and S. pombe data (catalytic residues needed, no hydrolase activity, loss of alpha-1,4 segments) fit.
- alpha-amylase activity and carbohydrate catabolic process (IEA): REMOVE (no detectable alpha-amylase activity; the role is biosynthetic).
- plasma membrane (3 rows) and extracellular region: MODIFY to external side of plasma membrane (GO:0009897); the GO anchored-component terms are obsolete. Cell wall IDA: ACCEPT.
- The plasma membrane and cell wall IDA rows citing PMID:12845604, an in silico GPI screen: source defect (WRONG_EVIDENCE_CODE, SUSPECTED).
- carbohydrate metabolic process and cell wall polysaccharide biosynthetic process: MODIFY to GO:0070600.
- The same decisions were applied to aah1 for consistency.
