# Sequence comparison results, 2026-10-26

Q59696 Adh and Q88QE2 BdhA have 354 identical residues in an ungapped 362-residue alignment (97.79% identity). Combined with the PpG2 alcohol-dehydrogenase expression and locus evidence in PMID:7813883, this supports transferring the NAD-dependent R,R-butanediol chemistry measured for KT2440 PP0552 in PMID:34513815 as a strong, explicit homolog inference. It does not constitute a PpG2 substrate/cofactor assay, establish equal kinetic constants, or prove that no alternative substrate is used.

Q59695 and Q88QE1 AcoC have 351 identical residues across 370 alignment columns, with two gap positions (94.86% identity). Their shared lipoyl-domain/alpha-beta-hydrolase architecture and conserved acetoin-system locus support the corresponding E2 assignment. The comparison does not establish isolated AcoC catalytic rates, complex stoichiometry, or the identity of a native E3 partner.

Inputs are the normally fetched UniProt flat files named and hashed in the JSON outputs. Q59696 includes both the PpG2 publication-linked sequence and an identical TS312 sequence; it is not a strain-exclusive database record. PMID:7813883 links Q59695 to G2/PpG2. Source records are preserved byte-for-byte.

- [x] Script inputs and output paths are command-line parameters, not hardcoded.
- [x] The script was tested on a second protein pair (AcoC).
- [x] Both analyses completed and direct machine-readable results are present.
- [x] Sequence-source provenance and biological limits are recorded.
