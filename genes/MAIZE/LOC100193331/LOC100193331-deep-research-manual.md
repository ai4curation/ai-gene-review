# LOC100193331 (brd1 / ZmCYP85A1) - manual literature synthesis

No deep-research provider was available for this session; this file was compiled manually from
PubMed searches and cached publications under `publications/`.

## Identity

- UniProtKB A0A804M0I4 (TrEMBL, unreviewed), 465 aa, Zea mays B73, Zm00001eb050010; NCBI GeneID
  100193331 (aliases Zm00001d033180, GRMZM2G103773, Dwarf2; designation "brassinosteroid-deficient
  dwarf1", chromosome 1; from NCBI Gene esummary).
- GRMZM2G103773 is the gene cloned as maize *brd1* by Makarevitch et al. 2012
  [PMID:22292043 "the fourth gene (GRMZM2G103773) encodes brassinosteroid C-6 oxidase"], encoding
  a 465-aa protein [PMID:22292043 "This gene encodes a 465 amino acid protein."], matching the
  length of A0A804M0I4.
- Family: cytochrome P450 (Pfam PF00067; InterPro IPR001128, IPR002401 E-class group I;
  PROSITE PS00086 heme-binding signature); PANTHER PTHR24286:SF169 "CYTOCHROME P450 85A1";
  CDD cd11043 CYP90-like. Heme-thiolate Cys at position 415 (PIRSR). N-terminal hydrophobic
  segment 1-16 (predicted by SignalP; in class II P450s this is normally the membrane anchor).

## Function (by orthology; no direct biochemistry on the maize protein)

- Arabidopsis BR6ox (CYP85A1) and tomato DWARF (CYP85A1) expressed in yeast convert several
  6-deoxo BRs to their 6-oxo forms (6-deoxoteasterone -> teasterone; 3-dehydro-6-deoxoteasterone
  -> 3-dehydroteasterone; 6-deoxotyphasterol -> typhasterol; 6-deoxocastasterone ->
  castasterone) [PMID:11402205 "Our results indicate that the AtBR6ox gene and the tomato Dwarf gene encode steroid-6-oxidases and that these enzymes have a broad substrate specificity."].
- Brassinolide formation (Baeyer-Villiger lactonisation of castasterone) was shown for
  Arabidopsis CYP85A2 and tomato CYP85A3, not for CYP85A1 [PMID:15710611]. Whether the single
  grass CYP85A also makes brassinolide is not established in the maize literature I could read.
- Rice brd1 (OsDWARF, CYP85A1) mutants have a BR profile consistent with C-6 oxidase
  deficiency and are rescued by the wild-type gene; OsDWARF expression is feedback-repressed by
  brassinolide [PMID:12445121].
- Maize BRD1 is 85% identical to rice BRD1 and 58% to Arabidopsis BR6ox1, and the maize genome
  has a single brC-6 oxidase gene [PMID:22292043].

## Maize genetics

- brd1-m1 (EMS, B73): nonsense mutation after aa 165, removing the P450 domain; severe dwarf,
  no internode elongation, no etiolation response; partially rescued by 10^-6 M brassinolide;
  wavy leaves, small ligule and sheath, enlarged auricle, feminized tassels, sterile
  [PMID:22292043].
- lilliputian1-1 (transposon-tagged) is an allele of brd1; lil1 is epistatic to nana plant1
  (DET2); root gravitropism, epidermal cell density, epicuticular wax and drought responses
  altered [PMID:29771294, abstract only].
- brd1 underlies the UPA1 leaf-angle QTL; ZmRAVL1 regulates brd1 expression and endogenous BR
  content [PMID:31416957, abstract only].
- No enzyme assay, BR metabolite profile or subcellular localization has been reported for the
  maize protein in the papers I could access.
