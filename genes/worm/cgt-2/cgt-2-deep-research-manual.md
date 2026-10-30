# cgt-2 (F20B4.6, UniProtKB:G5EC84) -- manual literature synthesis

No deep-research provider was available; this synthesis was assembled by hand from the
cached publications (publications/PMID_*.md), PubMed searches ("(cgt-2 OR ceramide
glucosyltransferase) AND elegans", 10 hits) and the UniProt record.

## Identity

- Ceramide glucosyltransferase 2, EC 2.4.1.80, glycosyltransferase family 2 / CAZy GT21,
  Pfam PF13506 (Glyco_transf_21), PANTHER PTHR12726. 443 aa, three predicted TM helices
  (60-80, 336-356, 398-418), D1/D2/D3 and (Q/R)XXRW motifs, proposed catalytic base D285
  (by similarity to mouse Ugcg Q9R0E0) [file:worm/cgt-2/cgt-2-uniprot.txt].
- One of three C. elegans CGT paralogs (cgt-1 T06C12.10, cgt-2 F20B4.6, cgt-3 F59G1.1)
  [PMID:21325339 "The nematode Caenorhabditis elegans has three Ugcg genes (cgt-1, cgt-2
  and cgt-3)"].

## Enzymatic activity

- Nomura et al. 2011 knocked out all three genes and expressed each in GSL-deficient
  GM95 cells [PMID:21325339 "Each gene product showed active enzymatic activity when
  expressed in GM95 cells deficient in glycosphingolipids (GSLs)."]. CGT-3 had the highest
  activity [PMID:21325339 "The CGT-3 protein had the highest Ugcg activity"].
- Leipelt et al. 2001 identified a C. elegans glucosylceramide synthase by heterologous
  complementation of GlcCer-deficient yeast; UniProt credits this paper with cgt-2
  catalytic activity (ECO:0000269), but the abstract does not name the C. elegans gene
  [PMID:11443131 "five novel glucosylceramide synthase (UDP-glucose:ceramide
  glucosyltransferase) genes were identified from the plant Gossypium arboreum (cotton),
  the nematode Caenorhabditis elegans"]. Abstract-only.
- Native substrates contain the branched-chain d17iso sphingoid base [PMID:7651085].

## In vivo contribution

- cgt-2 is a minor isozyme. Lipidomics: [PMID:38704027 "Regarding the CGTs, deficiency of
  cgt-3 but not cgt-1 or cgt-2 markedly decreased the abundance of all GlcCers quantified in
  C. elegans."]; [PMID:38704027 "In the cgt-1; cgt-2 double mutant, only a slight decrease
  was detected for two GlcCer species"].
- Larval development: the L1 arrest depends on cgt-1 + cgt-3, not cgt-2
  [PMID:38704027 "cgt-3;cgt-2 or cgt-1;cgt-2 double mutants did not, and cgt-2(lf) did not
  further exacerbate the growth arrest phenotype of cgt-3;cgt-1 worms"]. Marza et al. 2009
  (abstract only) describe CGT-deficient L1 arrest from digestive-tract defects
  [PMID:19240113].
- Reproduction: single knockouts of each gene reduced brood size [PMID:21325339 "When each
  gene function was disrupted, the brood size of the animal markedly decreased, and
  abnormal oocytes and multinucleated embryos were formed."].
- TORC1 pathway (Zhu et al. 2013, PMID:23705068, full text read): the paper uses
  cgt-1(tm1027) and cgt-3(tm504) only; cgt-2 is not mentioned. Its claims about d17iso-GlcCer
  promoting postembryonic development via TORC1 do not concern cgt-2 directly.
- Apicobasal polarity (Zhang et al. 2011, PMID:21926990): the polarity phenotype was
  found in cgt-1;cgt-3 double mutants/knockdown; cgt-2 was not shown to be required.
- Sperm activation needs GSL synthesis (PMID:22484621, abstract only; gene not named).

## Localization

No experimental subcellular data for CGT-2. Predicted multi-pass membrane protein;
mammalian UGCG is a cis-Golgi membrane enzyme with cytosolic active site (general
knowledge, not verified for the worm protein).
