# ELOVL7 (human) — gene review notes

UniProt: A1L3X0 (ELOV7_HUMAN), 281 aa. HGNC:26292. Gene ID 79993. Chromosome 5.
EC 2.3.1.199. HAMAP rule MF_03207 (VLCF_elongase_7). ELO family, ELOVL7 subfamily.

## Molecular function / catalytic activity

ELOVL7 is the condensing enzyme (3-keto acyl-CoA synthase) of the microsomal
fatty-acid elongation cycle. It catalyzes the first and rate-limiting step:
condensation of a (very-)long-chain acyl-CoA with malonyl-CoA to give a
3-oxoacyl-CoA + CO2 + CoA. The remaining three steps (reduction, dehydration,
reduction) are carried out by KAR/HSD17B12, HACD1/2, and TECR.

- UniProt FUNCTION: "Catalyzes the first and rate-limiting reaction of the four
  reactions that constitute the long-chain fatty acids elongation cycle. This
  endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons
  to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle.
  Condensing enzyme with higher activity toward C18 acyl-CoAs, especially
  C18:3(n-3) acyl-CoAs and C18:3(n-6)-CoAs. Also active toward C20:4-, C18:0-,
  C18:1-, C18:2- and C16:0-CoAs, and weakly toward C20:0-CoA. Little or no
  activity toward C22:0-, C24:0-, or C26:0-CoAs." [file:human/ELOVL7/ELOVL7-uniprot.txt]
- EC 2.3.1.199; Rhea RHEA:32727 generic "a very-long-chain acyl-CoA + malonyl-CoA
  + H+ = a very-long-chain 3-oxoacyl-CoA + CO2 + CoA". Nine specific substrate
  reactions curated (C16:0, C18:0, C18:1, C18:2, C18:3(n-3), C18:3(n-6), C20:4,
  etc.). [file:human/ELOVL7/ELOVL7-uniprot.txt]
- Substrate preference: strongest toward C18 acyl-CoAs, producing C20-C22 VLCFAs;
  broad specificity spanning saturated, monounsaturated, and polyunsaturated
  acyl-CoAs. So the same GO:0009922 MF underlies the saturated / monounsaturated /
  polyunsaturated elongation BP terms — these are substrate-class refinements of
  one activity, not distinct functions.

### Experimental evidence for MF (GO:0009922, EXP/IDA)
- PMID:19826053 (Tamura 2009, Cancer Res; abstract only): "In vitro fatty acid
  elongation assay and fatty acid composition analysis indicated that ELOVL7 was
  preferentially involved in fatty acid elongation of saturated very-long-chain
  fatty acids (SVLFA, C20:0 approximately )." Prostate-cancer discovery paper.
- PMID:20937905 (Ohno 2010, PNAS; abstract only): systematic in-vitro substrate
  specificity of all seven ELOVLs; source of the multiple curated catalytic
  activities and ER-membrane localization. "Elongases catalyze the first of four
  steps in the VLCFA elongation cycle; mammals have seven elongases (ELOVL1-7).
  In the present study, we determined the precise substrate specificities of all
  the ELOVLs by in vitro analyses."
- PMID:21959040 (Naganuma 2011, FEBS Lett; abstract only): purified ELOVL7,
  reconstituted into proteoliposomes. "Purified ELOVL7 exhibited high activity
  toward acyl-CoAs with C18 carbon chain length." Km(C18:3(n-3)-CoA)=2.6 uM,
  Km(malonyl-CoA)=11.7 uM. Mutagenesis of His-150/His-151 abolishes activity.
- PMID:34117479 (Nie 2021, Nat Struct Mol Biol; FULL TEXT): X-ray structure of
  human ELOVL7 (PDB 6Y7F) with covalently bound 3-keto acyl-CoA product analogue.
  "The first, rate-limiting step of the FA elongation cycle is catalysed by
  3-keto acyl-CoA synthases and consists of a condensation reaction between an
  acyl-CoA and malonyl-CoA to yield a 3-keto acyl-CoA." Ping-pong mechanism via
  an acyl-imidazole intermediate on H150 (second His of the HxxHH motif); H150A
  abolishes covalent modification. Inverted 7-TM barrel; homodimer (inverted
  dimer in crystals, also seen in solution).

## Cellular location — ER membrane, multipass

- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ...; Multi-pass
  membrane protein." Seven TM helices (TOPO/TRANSMEM features 28-257).
  C-terminal di-lysine motif (277-281) may confer ER localization.
  [file:human/ELOVL7/ELOVL7-uniprot.txt]
- PMID:20937905 (EXP): ER-membrane localization. PMID:34117479: structure is an
  ER-membrane, 7-TM inverted barrel.
- Reactome R-HSA-548815 (TAS): "ELOVL7 is localized to the endoplasmic reticulum
  in transfected cells expressing the cloned cDNA (Tamura et al. 2009)."

## Biological process

- Core BP: very-long-chain fatty acid biosynthetic process (GO:0042761) / fatty
  acid elongation. Because ELOVL7 elongates saturated, monounsaturated and
  polyunsaturated acyl-CoAs, all three substrate-class elongation BP terms
  (GO:0019367 saturated, GO:0034625 monounsaturated, GO:0034626 polyunsaturated)
  are experimentally / phylogenetically supported.
- PATHWAY (UniProt): "Lipid metabolism; fatty acid biosynthesis." UniPathway
  UPA00094 → GO:0006633 fatty acid biosynthetic process (IEA GO_REF:0000041); a
  correct but generic ancestor of the VLCFA-elongation terms.
- Sphingolipid biosynthetic process (GO:0030148, IBA): ELOVLs supply the VLCFA
  moieties of ceramides/sphingolipids; the family-level IBA is defensible but the
  human-experimental link to sphingolipids is via ELOVL1 (the C24 story in
  PMID:20937905 is about ELOVL1, not ELOVL7). Keep as non-core.
- GO:0035338 long-chain fatty-acyl-CoA biosynthetic process (TAS Reactome, IEA):
  the products are acyl-CoAs; correct but a generic/parallel framing of the same
  activity. Non-core.

## Protein interactions (bare "protein binding", GO:0005515 IPI)

- Functionally meaningful: TECR (Q9NZ01) interaction (PMID:38422897) — TECR is the
  final reductase of the elongation cycle; consistent with the elongation complex.
  UniProt SUBUNIT: "Homodimer (PubMed:34117479). Interacts with TECR
  (PubMed:38422897)." [file:human/ELOVL7/ELOVL7-uniprot.txt]
- High-throughput binary-interactome screens (Y2H): PMID:25416956 (DTNBP1/Q96EV8),
  PMID:32296183 (LRCH4, SERF1B, VAMP1, EMP3, SYNJ2BP, RTP2, SLC41A1, UBE2J2,
  TMEM14C, ADGRE2). These are single-method proteome-scale maps; ELOVL7 is one of
  thousands of ORFs. No specific function attributable; bare "protein binding" is
  uninformative → MARK_AS_OVER_ANNOTATED (policy forbids REMOVE of IPI).

## Disease / physiology (context, not for core)

- Prostate cancer: ELOVL7 overexpressed, androgen/SREBP1-regulated; knockdown
  attenuates growth; linked to saturated-VLCFA and cholesteryl-ester / de-novo
  androgen metabolism (PMID:19826053).
- Family context (PMID:34117479): ELOVL mutations cause Stargardt syndrome and
  spinocerebellar ataxia; ELOVL7 implicated in cancer, early-onset Parkinson's,
  necroptosis.

## Core function summary

1. Fatty acid elongase activity (GO:0009922) — 3-keto acyl-CoA synthase; first,
   rate-limiting condensation of acyl-CoA + malonyl-CoA (EC 2.3.1.199), C16-C20
   substrates, preferring C18, on the ER membrane. This single MF is the basis of
   the saturated/monounsaturated/polyunsaturated elongation BPs.
2. Very-long-chain fatty acid biosynthetic process (GO:0042761) — BP the activity
   serves.
3. Endoplasmic reticulum membrane (GO:0005789) — multipass ER-membrane location
   where the enzyme acts.
