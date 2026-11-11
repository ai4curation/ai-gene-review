# glo-1 (G5EBF0, R07B1.12) manual literature research

No deep-research API was available; this summary was compiled by hand from the
cached publications in `publications/` and PubMed searches (query:
"glo-1 Rab32 Caenorhabditis elegans gut granule").

## Identity
- UniProt G5EBF0 (TrEMBL, unreviewed), WormBase WBGene00011083, R07B1.12, GeneID 3565633,
  212 aa, chromosome X. Belongs to the Rab family (InterPro IPR030697 Rab29/Rab38/Rab32;
  CDD cd04107 Rab32_Rab38). Canonical G1 P-loop GDPGVGKT(25)S and switch-II WDISGQ(71)
  motifs are present (sequence in `glo-1-uniprot.txt`); C-terminal Cys-Cys prenylation motif.

## Key findings
- GLO-1 is the Rab32/38 ortholog required for biogenesis of gut granules, intestine-specific
  lysosome-related organelles (LROs) [PMID:15843430 "We show that the glo-1 gene encodes a
  predicted Rab GTPase that localizes to lysosome-related gut granules in the intestine and
  that glo-4 encodes a possible GLO-1 guanine nucleotide exchange factor."] (abstract only cached).
- Localization: GFP::GLO-1 marks the periphery of gut granules [PMID:22916203 "(I) GFP::GLO-1
  marked the periphery of gut granules in wild type (white arrows)."]; it is used as a
  lysosomal/LRO marker [PMID:23705068 "Both LMP-1::GFP (A–D) and GLO-1::GFP are lysosomal markers
  in C. elegans."].
- Nucleotide-state dependence: GLO-1(T25N) fails to rescue, GLO-1(Q71L) rescues
  [PMID:30419011 "Whereas glo-1(+) wild-type and glo-1(Q71L) mutant transgenes restored
  birefringent, PGP-2-containing, and autofluorescent gut granules when expressed in glo-1(-)
  mutants, the glo-1(T25N) mutant did not."; "Similar to other Rabs [29, 31], we show that the
  GTP bound form of GLO-1 is active in gut granule formation (Fig 5)."].
- Cargo routing: [PMID:30419011 "Notably, we did not detect a significant role for GLO-1 in the
  transport of cargo through conventional endolysosomes and instead show that GLO-1 functions to
  direct protein cargo away from this pathway toward gut granules (Figs 2 and 3)."]
- Activation: GLO-3/CCZ-1 act as GLO-1 GEF; fast-exchange GLO-1(D132A) bypasses glo-3/ccz-1
  [PMID:24501423; PMID:30419011]. In vitro Mant-GDP exchange assays show GLO-3–CCZ-1 GEF
  activity on GLO-1, enhanced by LMD-2 [PMID:39078368 "LMD-2 thus promotes the GEF activity of the
  GLO-3–CCZ-1 complex to activate GLO-1."].
- Other regulators of GLO-1 gut granule association: ABCG transporter WHT-2 [PMID:31848222].
- Downstream physiology (indirect): gut granules store Nile Red-stained fat [PMID:17202409];
  glo-1 mutants are impaired in LRO-dependent stress and immune responses [PMID:37704756].

## Not supported for the worm protein
- No evidence for mitochondrial, Golgi or TGN localization of GLO-1; these come from
  mammalian RAB32/RAB29 family members via IBA/InterPro2GO.
- No direct GTP hydrolysis assay for GLO-1; GTPase activity is inferred from conserved
  G motifs and Q71L/T25N genetics.
