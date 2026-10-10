# LPD1 notes (YFL018C, P09624)

- E3 dihydrolipoyl dehydrogenase, EC 1.8.1.4, FAD homodimer [PMID:2821168 "The LPD1 gene of S. cerevisiae, which encodes lipoamide dehydrogenase (EC 1.8.1.4), has been cloned and characterized"; UniProt:P09624].
- Shared E3 of PDH, KGDH and GCS: [PMID:3528755 "a nuclear recessive mutation, lpd1, which simultaneously abolishes the activities of lipoamide dehydrogenase, 2-oxoglutarate dehydrogenase and pyruvate dehydrogenase has been identified"]; [PMID:7498764 "Yeast strains with mutations in the single gene for lipoamide dehydrogenase (lpd1) lack GDC activity, as well as the other three 2-oxoacid dehydrogenases dependent on this enzyme"].
- KGDH recruitment by Kgd4 [PMID:25165143 "Kgd4 is specifically necessary for stably recruiting the E3 subunit Lpd1 to the Kgd1-Kgd2 subcomplex"]; free pool in matrix [PMID:25165143 "a substantial amount of Lpd1 exists in a free form in the matrix"].
- Branched-chain 2-oxoacid DH activity Lpd1-dependent [PMID:1479341 "Mutants defective in lipoamide dehydrogenase also lack 2-oxoacid dehydrogenase and are thus unable to catabolize branched-chain amino acids"]; E1/E2 partners unknown (no clear BCKDH orthologues).
- ROS source [PMID:17110466 "matrix-soluble dihydrolipoyl-dehydrogenases are an important source of CR-preventable mitochondrial reactive oxygen species (ROS)"].

## Curation observations
- IMP 'enables' GO:0004375 (P-protein) and GO:0004591 (E1 of KGDH) -> MODIFY to GO:0004148; whole-complex phenotypes mis-assigned as subunit MF.
- protein binding (Kgd2, Kgd4) x6 -> REMOVE; captured by complex membership.
- RCA cytosol (GLYCLEAV-PWY, PYRUVDEHYD-PWY) -> REMOVE.
