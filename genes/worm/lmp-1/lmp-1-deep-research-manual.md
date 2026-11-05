# lmp-1 (C. elegans, UniProt Q11117) - manual literature review

No deep-research API was available for this session; this summary was compiled by hand
from cached publications (publications/PMID_*.md) and PubMed searches
("lmp-1 elegans lysosome-associated membrane protein"; "LMP-1 phagosome lysosome cell corpse elegans").

## Identity and structure

- LMP-1 (C03B1.12, WBGene00003053) is a 237-aa single-pass type I membrane glycoprotein of the
  LAMP family: signal peptide 1-17, luminal domain 18-204 with five predicted N-glycosylation
  sites, TM helix 205-225, cytoplasmic tail 226-237 (UniProt Q11117; PROSITE PS51407 LAMP_3;
  InterPro IPR002000; PANTHER PTHR11506:SF35).
- Identified bioinformatically as a LAMP/CD68-like protein; "LMP-1 appears to be the only
  membrane protein in C. elegans that carries a GYXX(phi) vertebrate lysosomal targeting
  sequence at its C terminus" [PMID:10862717]. The C-terminus ...GYASV fits GYXXphi.
- C. elegans has a second LAMP-like protein, LMP-2 [PMID:27810910 "C. elegans has two LAMP-like proteins, LMP-1 and LMP-2"].

## Localization (the bulk of the evidence)

- Embryo and intestine granules: "predominantly localized at the periphery of a population of
  large, membrane-bound organelles, called granules" [PMID:10862717].
- Intestinal gut granules (lysosome-related organelles): "positive for membrane localization of
  CDF-2, LMP-1 and PGP-2"; under high zinc LMP-1 marks only one lobe of bilobed granules
  [PMID:22225878 "LMP-1 was present only in one lobe of bilobed gut granules"]. The same paper
  notes plasma-membrane localization: "a subset of LMP-1 localized to other membrane
  compartments that were LysoTracker negative, including the plasma membrane".
- Embryonic intestine: "LMP-1::GFP largely associated with conventional lysosomes"; ~30% of
  LMP-1 compartments RAB-7 positive (late endosome), ~10% RAB-5; "In the basal region of the
  intestine, LMP-1 localized to PGP-2 containing gut granules"; LMP-1::GFP also at the
  "basolateral plasma membrane"; AP-3 is required to deliver LMP-1 to gut granules [PMID:22916203].
- Nonacidic late lysosomes in adult intestine, colocalising with ABC transporters HAF-4/HAF-9
  [PMID:19403699 "LMP-1::mRFP was detected in a subset of nonacidic granules in wild-type N2"].
- Coelomocytes: "Late endosomes/lysosomes, labeled with the lysosome membrane protein LMP-1::GFP"
  [PMID:26783301].
- Phagosomes: "UNC-108 co-localizes with RAB-5, RAB-7 and LMP-1 to the phagosome" [PMID:18256195];
  LMP-1 on phagosomes containing cell corpses is also the basis of the WormBase IDA from
  PMID:20133524 (abstract-only in cache).
- Neurons/spermatheca: LMP-1::RFP also reaches the plasma membrane; native LMP-1 immunostaining
  differs from tagged versions [PMID:29547664].
- Used widely as a lysosome marker (LMP-1::GFP, pwIs50), e.g. [PMID:23705068] (elo-5 / TORC1
  study: lysosome formation appeared normal in elo-5 mutants by LMP-1::GFP), [PMID:35521960].

## Function (limited)

- No molecular activity has been demonstrated.
- lmp-1(nr2045) is viable; "the absence of LMP-1 leads to an alteration in intestinal granule
  populations, with apparent loss of one type of granule" [PMID:10862717]; lmp-1 mutants show
  aberrant membrane-limited vacuoles in intestine by EM [PMID:19403699].
- Overexpression of LMP-1 and LMP-2 suppresses lysosomal membrane damage in scav-3 mutants
  [PMID:27810910 "the increased level of LMP-1 and LMP-2 compensates for the loss of SCAV-3 to
  maintain lysosome membrane integrity"], but loss of lmp-1/lmp-2 does not severely affect lysosome
  integrity. This is consistent with the mammalian LAMP view of a protective luminal glycocalyx.
- Expression upregulated by a heat-killed probiotic; lmp-1 mutants failed to show the probiotic
  lifespan extension [PMID:39095841] (contextual, low relevance).

## Open questions

- Whether LMP-1 has any specific molecular activity (cf. human LAMP1 inhibition of TMEM175;
  LAMP2A in chaperone-mediated autophagy, a pathway not documented in nematodes).
- Mechanism of the granule-population defect in lmp-1 mutants.
