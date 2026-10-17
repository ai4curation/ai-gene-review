# ATG3 (donkey, A0A9L0IHI0) notes

## 2026-10-14 DONKEY40 review

- Record: TrEMBL, 342 aa, "Ubiquitin-like-conjugating enzyme ATG3" (ARBA name), Ensembl model from the donkey genome (PMID:33293529; sequencing only). 8 GOA rows, all IEA: 7 TreeGrafter (GO_REF:0000118, PANTHER PTN000305319) and 1 combined (ubiquitin-like protein transferase activity).
- Sequence: [file:EQUAS/ATG3/ATG3-bioinformatics/RESULTS.md "The donkey sequence A0A9L0IHI0 (342 residues) aligns to human Q9NT62 (314 residues) with 98.41% identity among 314 paired residues."] Catalytic Cys-264 conserved (donkey Cys-292); 28-aa insertion after human 222 not seen in human isoforms; activity of this exact model unverified.
- Human ATG3 is the E2 of the Atg8/LC3 lipidation cascade: [file:EQUAS/ATG3/ATG3-bioinformatics/human-Q9NT62-uniprot.txt "E2 conjugating enzyme that catalyzes the covalent conjugation"]; [PMID:37252361 "ATG7 functions as an activating E1 enzyme using ATP to form a thioester with LC3/GABARAP and transferring them to an E2 enzyme, ATG3, via a trans-thioesterification reaction."]; cycles between E1 and E3 [PMID:24186333 "Atg3 likely cycles back and forth between binding to Atg7 for loading with the UBL LC3 and binding to E3 to promote LC3 lipidation"].
- ATG12-ATG3 conjugate role in mitochondrial homeostasis [PMID:20723759 title "ATG12 conjugation to ATG3 regulates mitochondrial homeostasis and cell death."].
- GO term structure (QuickGO): GO:0019776 Atg8-family ligase activity is_a GO:0061659 ubiquitin-like protein ligase activity (E3 class); GO:0141046 Atg8-family conjugating enzyme activity is_a GO:0061650 ubiquitin-like protein conjugating enzyme activity (E2 class). Human ATG3 has IDA for GO:0141046. -> TreeGrafter ligase row MODIFY to GO:0141046.
- Selective autophagy terms (mitophagy, nucleophagy, glycophagy): ATG3-mediated LC3 lipidation is part of the core autophagosome-forming machinery used by these processes; kept as non-core (inherited PAINT node assertions; human has IBA for all three).
- ProtNLM2 GO: cytoplasm (GO:0005737). Donkey GOA has cytosol and phagophore assembly site, both part_of cytoplasm -> LSP. No ProtNLM2 function or location text for this accession.
