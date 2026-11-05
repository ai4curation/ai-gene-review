# arcB (PA5172, P08308) review notes

## Literature

- arcB defines the catabolic ornithine carbamoyltransferase of the arginine deiminase (ADI) pathway; arc mutants were isolated as unable to grow anaerobically on arginine [PMID:6438064 "All mutants (except one) were defective in at least one of the three enzymes of the arginine deiminase pathway (arcA, arcB, and arcC mutants)"] and [PMID:6438064 "The mutations arcA (arginine deiminase), arcB (catabolic ornithine carbamoyltransferase), arcC (carbamate kinase), and arcD were highly cotransducible"].
- UniProt (curated, with PubMed evidence): the enzyme catalyses citrulline phosphorolysis to ornithine and carbamoyl phosphate, feeding ATP generation, and does not perform the biosynthetic reaction [file:PSEAE/arcB/arcB-uniprot.txt "This catabolic OTCase does not carry out the biosynthetic reaction because of a poor affinity and a marked cooperativity for carbamoyl phosphate"]; it is allosterically regulated (activated by phosphate and nucleoside monophosphates, inhibited by polyamines) and dodecameric; disruption blocks the ADI pathway.
- arcA (PA5171) is reviewed in `genes/PSEAE/arcA/`; that review uses GO:0006527 L-arginine catabolic process as the process term (GO has no ADI-pathway-specific term), and this review follows it.

Search: PubMed metadata for PMID:6438064 (abstract only; PMC215798 exists but was not retrieved). UniProt-cited primary papers (PMID:2118516, 4962140, 8102605, 3109911) are not in the publication cache; their content is used only via the curated UniProt statements. NCBI E-utilities and Europe PMC search were unavailable (HTTP 500/503) during this session.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000150424 | GO:0004585 ornithine carbamoyltransferase activity | 9 | 157 (119 taxa) | GO:0004585, IMP, PMID:6438064 | SOUND | arcB mutants lack catabolic OTC activity and the locus was later shown to be the structural gene (purified enzyme, sequence). Loss of activity in mutants is weak evidence on its own, but the term is correct. | S. pombe Arg3 (SPAC4G9.10), rat Otc (RGD:3236), M. tuberculosis ArgF (P9WIT9), E. coli ArgI/ArgF (P04391, P06960), human OTC (P00480), yeast Arg3 (SGD:S000003624), Q9YHY9 | Yes |

Node term suits the clade (all members are OTCs). No GO_CENTRAL defect for the seed node term.

Separate propagation problem (not a PseudoCAP seed): the same node carries IBDs of GO:0006526 L-arginine biosynthetic process (seeds yeast Arg3, Q4WNW5, Mtb ArgF, S. pombe Arg3) and GO:0019240 citrulline biosynthetic process (rat, human, E. coli ArgI/ArgF). Both propagate to catabolic ArcB, which runs the reaction in the citrulline-consuming direction and cannot carry out the biosynthetic reaction. Both IBA rows are removed, and one GO_CENTRAL defect (requesting a NOT/withheld propagation for the catabolic OTC subclade) is recorded on the GO:0006526 IBA row; the GO:0019240 row cross-references it. The UniRule-derived IEA to GO:0006526 is likewise removed with a UNIPROT defect.
