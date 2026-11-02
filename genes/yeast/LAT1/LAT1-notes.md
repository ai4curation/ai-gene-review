# LAT1 (YNL071W, P12695) notes

Evidence journal for the review; sources are UniProt and cached publications.

- E2 (dihydrolipoyllysine-residue acetyltransferase, EC 2.3.1.12) of the PDH complex [UniProt:P12695].
- Activity of the catalytic domain: [PMID:2271545 "It exhibited catalytic activity (acetyl transfer from [1-14C]acetyl-CoA to dihydrolipoamide) very similar to that of wild-type E2p."]; Asp-431 important for kcat.
- 60-mer core: [PMID:9038189 "The tE2 core is a pentagonal dodecahedron consisting of 20 cone-shaped trimers interconnected by 30 bridges."]
- Reconstitution: [PMID:7030741 "The isolated enzymes reassociated spontaneously to give pyruvate dehydrogenase overall activity."]; [PMID:7947791 "The E3BP-E3 complex combined rapidly with a pyruvate dehydrogenase (E1)-dihydrolipoamide acetyltransferase (E2) subcomplex (E1-E2 subcomplex) to reconstitute a functional PDH complex"].
- E3 is recruited via protein X/Pdx1 [PMID:2007123 "The PDH complex isolated from the mutant cells contained pyruvate dehydrogenase (E1 alpha + E1 beta) and dihydrolipoamide acetyltransferase (E2) but lacked protein X and dihydrolipoamide dehydrogenase (E3)."].

Curation decisions
- YeastPathways RCA 'is_active_in cytosol' (PYRUVDEHYD-PWY) was removed: the PDH complex is in the mitochondrial matrix. The same error appears on PDA1 and PDB1.
- Generic 'acyltransferase activity' and 'acetyltransferase complex' were changed to E2 activity / PDH complex.
- The YeastCyc reaction direction (acetyl-CoA + dihydrolipoyl-E2 <- ...) matches UniProt's RHEA:17017 written in reverse; physiologically acetyl transfer goes from the lipoyl arm to CoA.
