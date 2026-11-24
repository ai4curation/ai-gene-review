# murE (Staphylococcus aureus NCTC 8325, Q2FZP6) — curation notes

Reviewed as the L-lysine branch exemplar of the MurE step in
`modules/peptidoglycan_precursor_biosynthesis.yaml`. No provider deep-research
file was generated for this gene (the providers were not available in this
session); these are the curator's own notes, with every claim traceable to the
cached UniProt record or a cached publication.

## What the protein does

MurE adds L-lysine to UDP-N-acetylmuramoyl-L-alanyl-D-glutamate using Mg2+-ATP
[file:STAA8/murE/murE-uniprot.txt "Catalyzes the addition of L-lysine to the nucleotide"],
the third step of stem-peptide assembly (EC 6.3.2.7, RHEA:17969). The purified
enzyme cannot use diaminopimelate
[file:STAA8/murE/murE-uniprot.txt "diaminopimelate as substrate (PubMed:10498701, PubMed:14114846,"],
and accepts L-ornithine about 400-fold less efficiently than L-lysine (KM 37 mM
versus 0.55 mM)
[file:STAA8/murE/murE-uniprot.txt "KM=37 mM for L-ornithine {ECO:0000269|PubMed:20659527};"].

Patin et al. purified all four S. aureus Mur ligases and compared them with the
E. coli enzymes
[PMID:20659527 "S. aureus MurE was very specific for L-lysine and in particular did not accept meso-diaminopimelic acid as a substrate."];
they conclude that the inverse specificities of the two MurE orthologs determine
which residue occupies position 3 of the stem peptide in each species
[PMID:20659527 "The inverse and strict substrate specificities of the two MurE orthologues is thus responsible for the"].
The same paper reports that MurF, unlike MurE, accepts both tripeptide forms
[PMID:20659527 "S. aureus MurF appeared less specific and accepted both forms"],
which is why the module models one MurF step serving either MurE branch.

Expression of this enzyme in E. coli incorporates L-Lys into roughly half of the
peptidoglycan and causes abnormal morphology and lysis
[file:STAA8/murE/murE-uniprot.txt "incorporation of L-Lys into the peptidoglycan (which normally contains"],
a further sign that stem chemistry is set at this step.

## Family grounding caveat

Q2FZP6 and E. coli MurE (P22188) carry the same PANTHER family and the same
subfamily, PTHR23135:SF4, whose official name refers to a chloroplastic
meso-diaminopimelate-adding homolog. Family and subfamily membership therefore
cannot predict third-residue specificity, which is residue-determined; PAINT has
a meso-diaminopimelate-specific node (PTN000566406) but no L-lysine-specific one,
so no ancestral-node claim is asserted for the L-lysine variant in the module.
