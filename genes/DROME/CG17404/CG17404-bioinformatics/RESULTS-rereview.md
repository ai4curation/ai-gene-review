# CG17404 (Q9VGC0) re-review: sequence and phylogenetic placement

Analyses run 2026-10-21. Both scripts are in this folder and can be re-run.

## 1. Sequence checks (`check_sequence_rereview.py`, output `check_sequence_rereview.json`)

Input: the cached UniProt flat file `../CG17404-uniprot.txt` (Q9VGC0, 275 aa, sequence version 3).

- The three PROSITE-ProRule active-site positions carry the catalytic residues of an S1A serine protease: His80 (context ILTAAHCCQGL), Asp124 (context ELVTSDLAVLS) and Ser225 (context ACSGDSGGPLV). The catalytic serine sits in the conserved GDSGG motif (motif starts at 223).
- A single candidate zymogen activation site matches the S1A mature-N-terminus pattern: the bond R34-I35, followed by IVGGA. Cleavage there would release a mature catalytic domain starting at Ile35, the first residue of the annotated Peptidase S1 domain (35..274).
- Only 14 residues (RLNSRQPSGYTPHR, no cysteines) lie between the SignalP signal peptide (1..20) and the S1 domain. There is no room for a clip domain (about 30-60 residues with three disulfides), so the protein is a single-domain secreted S1A protease, not a clip-domain protease, whatever the ARBA-derived "CLIP subfamily" similarity note says.
- The residue at the S1 specificity-pocket position 189 (chymotrypsin numbering; six residues before the catalytic Ser) is Gly219. Trypsin-like enzymes have Asp at this position, which favours Lys/Arg at P1. The lack of Asp189 argues against trypsin-like specificity, but a single pocket residue does not define the specificity, so substrate preference is left unresolved.

## 2. PANTHER tree placement (`panther_tree_rereview.py`, output `panther_tree_rereview.txt`)

Input: the PTHR24256 gene tree from the PANTHER API (current release).

- Q9VGC0 is in subfamily PTHR24256:SF562 (IP09525P-RELATED). The SF562 clade, PTN009088600 (Eumetazoa), has eight members: three tandem Drosophila paralogs (CG17404/SP149 Q9VGC0, CG12256 Q9VGB9 and CG3916 Q9VGB8, from an in-Drosophila duplication at PTN001546914), one Anopheles gambiae gene, two Tribolium castaneum genes and two Trichoplax adhaerens genes. There is no vertebrate member and no experimentally characterised member.
- The SF562 clade branches directly from PTN001207268, the Eumetazoa-level duplication node that also carries the PAINT IBD assertions for GO:0004252, GO:0006508 and GO:0005576 that Q9VGC0 inherits. PTN001207268 has four other child clades. PTN007783152 (271 leaves) holds the mammalian tryptases (TPSAB1, TPSB2, TPSD1, TPSG1, PRSS33) and Drosophila Easter (ea, P13582), Sp7 and other CLIP proteases. PTN009088603 (176 leaves) holds PRSS21/testisin, PRSS48, PRSS54 and many Drosophila SPHs. Two small clades (SF567, SF569) have no human or fly members.
- So CG17404 has no characterised ortholog. Its nearest characterised relatives are paralogs that diverged at the PTN001207268 duplication, all equally distant by tree topology. Subfamily-specific functions of those paralogs (Easter in dorsoventral patterning, Sp7 in prophenoloxidase activation, mast-cell tryptase biology) cannot be transferred. Only the root-level IBD functions apply.

## 3. PAINT negations

Every node in `interpro/panther/PTHR24256/PTHR24256-paint.tsv` that carries a negated (NOT GO:0004252) assertion was located in the tree. Each is a leaf or node for a different serine-protease homolog: CG33225, CG5240, CG8738, CG8586, CG4477, CG33127, CG9673, a Nematostella gene, and PTN000668109 in SF462. None lies on the Q9VGC0 lineage. The PAINT curator therefore withdrew the root-level serine-endopeptidase assertion from specific SPH branches but not from the SF562 clade. That is consistent with the intact catalytic triad found in section 1.

## Limitations

The tree comes from PANTHER's own phylogeny; no new alignment or tree was built. The specificity-pocket inference uses motif-anchored chymotrypsin numbering, not a structural superposition.
