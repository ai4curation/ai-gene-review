# Sns isoform B contains an extra hydrophobic segment

The selected Q0E9F2 sequence is 1542 residues and contains all 1479 residues of RefSeq Sns isoform A (NP_788286.1) identically. The sole difference is a 63-residue insertion at the reference 1059/1060 junction, corresponding to target 1060–1122. Its sequence is `EAPPPSHPASSLGGGPPTTSQTPLGGTSGMLLVGVGAGIVVVLLNVFVIGCCLHKRNEKRLKR`.

The selected record predicts transmembrane segments 1089–1112 (within the insertion) and 1141–1166 (in the shared sequence). The insert therefore raises a specific membrane-topology question: an additional membrane crossing could affect presentation of the intracellular signaling tail, although this has not been experimentally established. The large extracellular adhesive domain and all shared cytoplasmic-tail residues remain present. This is not a global failure of homology and does not undermine membrane association. It is also not evidence that the predictor received a wrong sequence.

The broad gene-level myogenesis, adhesion, and filtration experiments remain informative. Their exact transfer to this longer isoform requires distinguishing retained extracellular adhesion from potentially altered membrane topology and intracellular signaling. No biochemical inactivity or wrong-gene attribution is asserted.

Raw alignment and indel coordinates are in isoform-comparison.json. The independent CG4793 control returns 910/910 identical aligned residues and no indels, confirming that the script does not force an insertion result. Target sequence SHA256: `3d5ebad88672f4b0edc760213f101c03977d8ef9250001f3f57d942e07f4611d`.

- [x] Script takes arbitrary inputs; no biological outcomes hardcoded.
- [x] Tested on a different gene, CG4793.
- [x] Target and control runs completed successfully.
- [x] Original inputs, raw outputs, and complete alignment retained.
- [x] Conclusion distinguishes measured sequence differences from predicted topology and untested effects.
