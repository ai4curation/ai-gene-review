# BAT2 (YJR148W, P47176) notes

Batch: YeastPathways module `branched_chain_amino_acid_biosynthesis`.

- Cytosolic BCAT, EC 2.6.1.42 [UniProt:P47176 "RecName: Full=Branched-chain-amino-acid aminotransferase, cytosolic"]; [PMID:8798704 "A highly homologous protein, Bat2p, of 376 amino acid residues was found in the cytosol"].
- Imaging: [PMID:21267457 "Bat1 is mitochondrially located, while Bat2 is cytoplasmic."]
- Catabolic role (first step of Ehrlich pathway): [PMID:21267457 "These results indicate that Bat2 has a prominent role in VIL catabolism, while Bat1 catabolic role is only evidenced in a bat2Δ genetic background"]; [UniProt:P47176 "aminotransferase, which catalyzes the first reaction in the catabolism"].
- Backup biosynthesis: only double bat1 bat2 is auxotrophic [PMID:8798704 "deletion of both genes resulted in an auxotrophy for branched-chain amino acids (Ile, Leu, and Val)"].
- Expression: BAT2 highest under catabolic conditions / stationary phase [PMID:21267457 "BAT1 is highly expressed under biosynthetic conditions, while BAT2 expression is highest under catabolic conditions"].
- Methionine salvage KMTB transamination (UniProt, PMID:18625006 not cached). Non-core.

## Curation observations
- IBA `is_active_in mitochondrion` (PTN000214536, seeded by Bat1/BCAT2 etc.) is wrong for Bat2, the post-WGD paralog that lost its presequence -> REMOVE with propagation_review (COMPARTMENT_OR_COMPLEX_MISMATCH).
- Biosynthetic BP rows kept as non-core; catabolic BP rows accepted as core.
- For the biosynthesis module: Bat2 is a valid but secondary (backup) member for the terminal transamination step; its primary home is BCAA catabolism (Ehrlich pathway module).
