# A0A5M3MRX5 (CONPUDRAFT_136560) notes

Coniophora puteana RWD-64-598 SS2, TrEMBL, 339 aa, PE 3. Named by ARBA
"(S)-malate dehydrogenase (NAD(+), oxaloacetate-forming)", EC 1.1.1.37. No gene
symbol; folder named by accession, ORF name used as gene_symbol (CLAUDE.md
convention; same pattern as genes/CONPW/A0A5M3MJR8, which is in PR #5626 and
not yet in main).

No deep-research provider was available; these notes are my own research.

## Identity and family

- Type-1 MDH: NCBIfam TIGR01772 (MDH_euk_gproteo), InterPro IPR010097
  (Malate_DH_type1), PIRSF000102, CDD cd01337 (MDH_glyoxysomal_mitochondrial),
  PANTHER PTHR11540:SF73 (MALATE DEHYDROGENASE, MITOCHONDRIAL). PIRSR places the
  proton-acceptor His (position 201), NAD(+)- and substrate-binding residues; the
  CDD and PANTHER assignments are family calls only and say nothing about residues.
- CDD cd01337 covers glyoxysomal and mitochondrial MDHs (the PTS1 paralog
  A0A5M3MC96 is in it too), so it cannot separate mitochondrion from peroxisome.
  Subfamily names are not localization calls either (SF16 is also named
  MITOCHONDRIAL and holds yeast cytosolic MDH2 P22133). What counts is SF73
  membership: SF73 contains yeast MDH1 P17505 (mitochondrial), while yeast
  peroxisomal MDH3 P32419 is in SF72 (PTHR11540-entries.csv). The paralog
  A0A5M3MC96 is in SF16, not SF72 (UniProt, Oct 2026).
- Genome from the 31-genome lignin-decay study [PMID:22745431 "Comparative analyses
  of 31 fungal genomes (12 generated for this study)"].

## Mitochondrial or cytosolic?

Mitochondrial. See `A0A5M3MRX5-bioinformatics/RESULTS.md`:
- N-terminal 32 residues before the GxGGxG core motif (`MLARTALRSVASTSRASAFSTSAARLTRVAVL`):
  5 Arg/Lys, 0 Asp/Glu, 10 Ser/Thr, which is presequence composition. This parallels yeast MDH1,
  whose 17-residue extension is a mitochondrial presequence
  [PMID:3072021 "The open-reading frame encodes a precursor form of the mature enzyme containing an amino-terminal extension of 17 amino acid residues."].
- No PTS1 (C-terminus FVA). The only other type-1 MDH in the proteome, A0A5M3MC96
  (CONPUDRAFT_157993), has no presequence and ends in SKL (PTS1), like yeast peroxisomal MDH3.
- UniProt FT DOMAIN 27..169 (Pfam PF00056) starts the conserved N-terminal domain at
  residue 27, independently corroborating an extension of about 26 residues.
- Identity 0.63 to yeast MDH1, 0.48 to yeast cytosolic MDH2.
- No targeting predictor (TargetP/MitoFates) was run, so the presequence call rests on
  composition plus homology. No experimental localization exists for any C. puteana MDH.

## Oxalate context

- Brown-rot Fomitopsis palustris: whole-cell extracts have very high MDH activity
  [PMID:11553780 "the greatest activity was found for MDH: 5,840 nmol"]; most oxalate
  comes from oxaloacetate hydrolysis
  [PMID:11553780 "Thus, most oxalate is inferred to be produced from oxaloacetate and to be hydrolyzed by OXA involved in both recycling routes (C and D)."].
  The authors' model says malate, not oxaloacetate, leaves the mitochondria and is
  oxidized outside
  [PMID:11553780 "oxaloacetate cannot be shuttled through the membrane system of mitochondria and glyoxysomes, and not oxaloacetate but malate may flow out from Cycle A or B to be oxidized to form oxaloacetate"].
  MDH isozymes were not separated.
- A. niger oxaloacetate hydrolase is cytoplasmic
  [PMID:3132096 "Subcellular fractionation of oxalic acid-forming mycelia of A. niger showed that this enzyme is located in the cytoplasm of A. niger."].
- So a mitochondrial matrix MDH runs the TCA cycle oxidation in the matrix. Oxaloacetate
  made there is not directly available to a cytosolic oxaloacetate hydrolase. In the
  Munir model, the oxaloacetate for oxalate is made by an extramitochondrial MDH.
  That points to the peroxisomal paralog A0A5M3MC96 (or an unidentified cytosolic MDH),
  not to this protein. Neither role is tested in C. puteana.

## CMMMech cross-check (humboldtine.yaml, malachite.yaml, fluorapatite.yaml)

The records were not edited.
- `functional_role` gives "locus CONPUDRAFT_126646". UniProt and EMBL give ORF
  CONPUDRAFT_136560 (EIW81850.1; GeneID 19200921). CONPUDRAFT_126646 returned no hit
  in UniProt or NCBI Protein/Gene esearch (Oct 2026). The locus field looks wrong.
- `interpro_ids` include IPR010945 (Malate dehydrogenase, type 2) and IPR011274
  (Malate dehydrogenase, NAD-dependent, cytosolic). Neither is in the UniProt entry, which has
  IPR001557, IPR022383, IPR001236, IPR015955, IPR010097 and IPR036291. They contradict
  its type-1 and mitochondrial classification.
- The claim "supplying the direct oxaloacetate precursor for brown-rot fungal
  oxalic-acid biosynthesis" goes further than the evidence:
  (i) there is no experiment on this protein or on C. puteana MDH;
  (ii) it is the mitochondrial TCA-cycle isozyme, and the brown-rot model that
  invokes MDH places oxalate-precursor oxaloacetate formation outside mitochondria;
  (iii) the Vlasov 2023 source is mineralogical only (the record's own evidence note
  says so). A defensible statement would be: "mitochondrial TCA-cycle MDH (by homology);
  candidate indirect contributor to the oxaloacetate pool".
  The peroxisomal paralog A0A5M3MC96 is the better extramitochondrial candidate if one is wanted.
- The record's EC 1.1.1.37 and taxon (NCBITaxon:741705, UP000053558) match UniProt.
