# PP_0788 (Q88PR0): notes

Dashboard protein: NZ_CAKNDZ010000038.1_57 (P. putida, 737 aa, tier A, Dark-Function), https://gene-annotate-dashboard.kbase.us/review/NZ_CAKNDZ010000038.1_57

## Mapping

- The exact UniParc entries are deleted, so the review is filed on KT2440 PP_0788 (Q88PR0, 719 aa).
- Identity is 94.7% over 717 aligned pairs (BERIL run `20261030T213855Z-pp0788-identity-start`). The mapping table gives 94.6% over 719.
- The 18-residue length difference is at the N-terminus. The query has 36 residues before the conserved RTPHPCLP motif; PP_0788 has 18. This leader is non-conserved and disordered (MobiDBLite 18-40), so it reflects a different start-codon call. The rest of the protein is colinear to the C-terminus.
- In KT2440, the open in-frame extension upstream of the annotated ATG does not resemble the query leader.

## Conclusion

PP_0788 is a DUF1631-family protein of unknown molecular function.

- It is direct-target evidence only: FleQ binds the PP_0788 promoter at two sites, and c-di-GMP/FleQ represses its transcription (PMID:33975969).
- It sits 88 bp upstream of ampD-ampE, on the same strand.
- No GO terms are proposed. GOA is empty.

**"Thymidine phosphorylase" (UniProt RecName) is wrong.**

- The name is a ProtNLM prediction (ECO:0008006). The same string appears as a legacy gene description on several Pseudomonas Fitness Browser orthologs.
- Q88PR0 has only DUF1631 Pfam models (PF07793, PF26671, PF26672, PF26670). It has no glycosyltransferase family 3 domain (PF00591, PF02885), which DeoA has.
- The eggNOG COG1570/XseA label is also wrong. KT2440 has a real XseA, PP_1027.

## Fitness

The Fitness Browser site returned 403 to `just fetch-fitness`, so the data were read from BERDL `kescience.fitnessbrowser` (run `20261030T213614Z-pp0788-fitness`).

- **KT2440:** no phenotype in 300 experiments (|fit| <= 0.38). KT2440 has no motility, nitrate-stress or bacitracin experiments, so it cannot test the call.
- **P. simiae WCS417 GFF773 (53.6%):** reduced motility in 5 soft-agar experiments (-1.13 to -1.85). Single moderate stress defects: nitrate 200 mM -1.64, choline chloride 300 mM -1.56, bacitracin -1.30, phosphomycin -1.13. None is an FB "specific phenotype".
- **Other orthologs:**
  - N2E2 has one specific motility phenotype (-1.07).
  - RCH2 has many phenotypes in both directions, including better fitness in nitrate 250 mM (+1.67).
  - N2C3, N1B4, B728a and the Marinobacter BBH show nothing.
- **Assessment:** the motility association is reasonably consistent. The nitrate, choline and bacitracin associations rest on one experiment each in one ortholog and do not replicate. Polar effects on ampDE cannot be excluded.
- **Distant family context:** DUF1631 mutants in Xanthomonas (XC_3388, PacR) are pleiotropic (PMID:35706385, PMID:39608507). The XC_3388 mutant is *hyper*motile, the opposite sign.

## Dashboard verdict

**Supported (with a caveat).**

- The DUF1631 family is correct. Rejecting the thymidine phosphorylase and ExoVII labels was right.
- The phenotype clause overstates single-ortholog stress hits.
- The call missed the direct FleQ/c-di-GMP regulation, although it was in its own PaperBLAST panel.
- Suggested annotation: "DUF1631 family protein of unknown function; transcription repressed by FleQ/c-di-GMP; P. simiae orthologue mutant impaired in swimming motility".
- The dashboard drew no GO terms, so the PredictionReview has `predictions: []`. The empty GO set is appropriate.

## Caveats

- Nothing is known about the protein's biochemistry.
- The phenotypes come from transposon fitness of orthologs, not from the KT2440 gene.
- The deep-research report claims KT2440 has a separate deoA. A UniProt query found no DeoA in KT2440, so that claim is not used.

## Tooling

- `just fetch-gene` failed at the EBI OLS taxon-label lookup (read timeout). The stub was seeded by calling `fetch_gene_data` with the label lookup routed through `ubergraph:`.
- `just fetch-fitness` failed with "no FEBA data source was reachable".
- `validate-predictions` writes `reports/prediction-evidence.json`.
