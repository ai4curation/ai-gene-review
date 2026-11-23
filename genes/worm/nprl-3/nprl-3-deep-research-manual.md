# nprl-3 (C. elegans, Q20069, F35H10.7) - manual literature research

No deep-research API was available; this summary was compiled by hand from cached
publications in `publications/` and a PubMed search ("nprl-3 elegans", 2 hits:
PMID:26109047, PMID:31594908), plus the primary paper PMID:23705068.

## Identity and family

- F35H10.7 encodes a 511-aa protein of the NPR3 family (Pfam PF03666 NPR3, PF24064
  HTH_NPRL3), orthologous to yeast Npr3 and human NPRL3 (UniProt Q20069; Swiss-Prot,
  PE 3 "inferred from homology").
- Named nprl-3 by Zhu et al. 2013 [PMID:23705068 "We named the gene nprl-3 (NPRL-3 for protein)."].

## Conserved molecular role (orthologs)

- Human NPRL3 is a subunit of GATOR1 (DEPDC5, NPRL2, NPRL3), a GAP for RagA/B
  [PMID:23723238 "GATOR1 has GTPase-activating protein (GAP) activity for RagA and RagB"].
- Cryo-EM: "NPRL2 links DEPDC5 and NPRL3"; "weaker interactions between the NPRL2-NPRL3
  heterodimer and RAGA execute GAP activity" [PMID:29590090]. NPRL3 therefore
  contributes to, but alone does not perform, the GAP activity.
- GATOR1 is recruited to lysosomes by KICSTOR in human cells [PMID:28199306 "KICSTOR
  localizes to lysosomes; binds and recruits GATOR1, but not GATOR2, to the lysosomal surface"].
- Drosophila Nprl2/Nprl3 "physically interact and are targeted to lysosomes and
  autolysosomes" and mediate the amino-acid starvation response [PMID:24786828].
- Drosophila nprl2 and nprl3 mutants "fail to activate autophagy in response to amino
  acid limitation" [PMID:27672113].

## C. elegans evidence

- Forward genetic suppressor screen: nprl-3(ku540), a P->S missense, bypasses the L1
  arrest of mmBCFA-deficient elo-5 and glucosylceramide-deficient cgt-1;cgt-3 animals;
  nprl-3 RNAi phenocopies [PMID:23705068 "RNAi of nprl-3 by dsRNA injection also rescued
  the L1 arrest of elo-5(−) and cgt-1(−);cgt-3(−) animals (Figure 3C)"].
- Epistasis with TORC1 components (raga-1, rheb-1, rsks-1, ife-2, let-363 RNAi) shows the
  rescue requires TORC1 [PMID:23705068 "Taken together, these results indicate that TORC1
  acts downstream of d17iso-GlcCer and is negatively regulated by NPRL-3."].
- nprl-2 RNAi also suppresses elo-5 arrest; authors suggest a complex
  [PMID:23705068 "elegans may also function in a complex to negatively impact mmBCFA/d17iso-GlcCer-mediated L1 growth."].
- Expression: a transcriptional reporter "was observed to express ubiquitously throughout
  development and adulthood" [PMID:23705068].
- Follow-up: nprl-3(lf) restores intestinal apical polarity (ERM-1, VHA-6 localization)
  in elo-5 animals independently of TORC1 [PMID:26109047 "This nprl-3(lf)-caused polarity
  restoration is independent of TORC1 activation"]; the authors propose "NPRL-3 represses
  TORC1 activity at least in part by regulating apical membrane polarity" and note this is
  "distinct from the reported role of the NPRL2/3 complex as a GTPase-activating protein".
- Review: Blackwell et al. 2019 Genetics review of worm TOR signalling [PMID:31594908]
  (abstract only in cache).

## Gaps

- No C. elegans biochemistry (complex purification, GAP assays) and no subcellular
  localization of NPRL-3 protein.
- No DEPDC5 ortholog role tested in worm in these papers; KICSTOR conservation in worm
  unclear.
- Mechanism of the polarity effect unknown.
