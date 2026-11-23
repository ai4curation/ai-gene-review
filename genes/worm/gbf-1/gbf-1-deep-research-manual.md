# gbf-1 (C24H11.7, PHI-34) manual literature review

No deep-research provider was available for this session, so this summary was assembled by hand
from the cached publications and a PubMed search (`(gbf-1 OR GBF-1) AND elegans`, 4 hits:
PMID:23840591, PMID:25190516, PMID:26115433, PMID:35998789).

## Identity and domain architecture

- UniProt G5EGS5 (GBF1_CAEEL, Swiss-Prot, 1975 aa, PE 3), WormBase WBGene00007703, ORF C24H11.7,
  synonym phi-34. Two isoforms: a (displayed) and b, which lacks residues 1-1490 (VSP_060671) and
  therefore lacks the Sec7 domain (624-812) [file:worm/gbf-1/gbf-1-uniprot.txt "VAR_SEQ         1..1490"].
- Domains: DCB/HUS region (Pfam PF12783 Sec7-like_HUS), catalytic Sec7 domain (PF01369, PROSITE
  PS50190, residues 624-812), GBF1-like TPR region (PF23325), long disordered C-terminus.
  PANTHER PTHR10663:SF388 (GBF1 subfamily).
- "C. elegans PHI-34 is the closest homolog to mammalian GBF1 with 38% identity and therefore it is
  also referred to as GBF-1" [PMID:23840591].

## Function from orthology

- GBF1/Gea1/Gea2/garz are cis-Golgi Sec7 Arf GEFs that activate Arf1 (and Arf4/5) to recruit COPI for
  retrograde Golgi-to-ER and intra-Golgi transport; the mammalian protein "is localized to the Golgi
  apparatus and has been shown to be essential for maintaining Golgi structure and traffic through
  the Golgi" [PMID:23840591, introduction].
- UniProt curated function (by similarity to human Q92538): "Guanine-nucleotide exchange factor (GEF)
  for members of the Arf family of small GTPases involved in trafficking in the early secretory
  pathway" [file:worm/gbf-1/gbf-1-uniprot.txt].

## Ackema et al. 2013 (PMID:23840591; full text read)

- Null mutant is lethal; work done by RNAi. L1 RNAi: cuticle rupture through the vulva, 50-80%
  lethality, sterility, body-cavity vacuoles. L3/L4 RNAi: 60-70% embryonic lethality, eggshell
  defects, polar-body extrusion and cytokinesis defects.
- Localization (affinity-purified peptide antibody, validated by RNAi loss of signal): "GBF-1 was
  found 'sandwiched' between the Golgi marker UGTP::GFP and ERES marker SEC-16"; "GBF-1 is present on
  the cis-face of the Golgi at so-called transitional ER-Golgi elements"; "GBF-1 and SEC-16 partially
  overlap by confocal microscopy". GBF-1 recruitment to cis-Golgi is independent of AGEF-1.
- Golgi: "gbf-1(RNAi) caused the small Golgi foci to aggregate into large structures"; by EM "upon
  gbf-1(RNAi) numerous vesicles accumulated at the cis-Golgi, representing most likely ER-derived COPII
  vesicles".
- ER: "In gbf-1(RNAi) oocytes we observed a severely disturbed ER organization"; ER lumen lost by EM;
  SEC-16 ERES preserved. The authors suggest the ER effect "is indirect and probably coupled through a
  decreased reflux of lipids".
- Secretion: CAV-1 Golgi-to-PM transport partially impaired; VIT-2::GFP accumulates in intestine;
  weakened cuticle and eggshell. Authors: "these data suggest, that GBF-1 plays a role in secretion.
  However, this role is likely indirect through GBF-1's involvement in retrograde transport to the ER."
- Endocytosis: yolk accumulates in body cavity, less yolk uptake into oocytes, but RME-2 PM level,
  RAB-11 recycling and RME-2/CAV-1 degradation are normal. Authors favour an indirect explanation
  (yolk glycosylation). In intestine, RAB-5 signal reduced and RAB-7 endosomes form large tubular
  networks: "GBF-1 might be required for maintenance of endosome morphology and potentially for
  efficient endocytic transport in the gut epithelium."
- Retrograde transport was not measured directly: "retrograde transport in the ER-Golgi shuttle is not
  easily studied, and in particularly not in a whole animal."

## Ackema et al. 2014 (PMID:25190516; abstract only)

- "Loss of function of ARF-1 or GBF-1 impaired mitochondrial morphology and activity in Caenorhabditis
  elegans"; "similar mitochondrial abnormalities resulted from knockdown of either GBF-1 or contact
  site components in worms, suggesting that the role of Arf1 in mitochondrial functioning is linked to
  ER-mitochondrial contacts." UniProt lists enlarged, interconnected mitochondria in oocytes and muscle
  and altered paraquat sensitivity after gbf-1 RNAi.

## Zhu et al. 2015 (PMID:26115433; full text)

- GBF-1 co-immunoprecipitated with SGK-1::GFP (MS); gbf-1 RNAi disrupts basolateral SGK-1::GFP in
  intestine. Interaction not further characterised: "More studies are needed to characterize the
  interaction between SGK-1 and GBF-1".

## Sarkar et al. 2022 (PMID:35998789; abstract only)

- gbf-1 named as a putative miR-4813-3p target studied in an alpha-synuclein worm model; not
  informative about GBF-1 molecular function.
