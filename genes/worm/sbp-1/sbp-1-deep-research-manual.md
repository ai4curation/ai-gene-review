# sbp-1 (Q9XX00) -- manual literature synthesis

No deep-research API was available for this session, so this file was compiled by hand
from the cached publications in `publications/` and the UniProt record
(`sbp-1-uniprot.txt`). Every statement carries inline provenance.

## Identity and domain architecture

- *C. elegans* sbp-1 (Y47D3B.7; also published as lpd-1) encodes the single nematode
  SREBP (sterol regulatory element-binding protein), a 1113-aa bHLH-Zip transcription
  factor. [PMID:28710073 "Here, we showed that reduction of SBP-1, the only homolog of SREBPs in Caenorhabditis elegans , surprisingly led to a high level of zinc."]
- UniProt features: an N-terminal acidic transactivation region (1-52, by similarity to
  human SREBF1), a bHLH domain (355-405; PROSITE PS50888) followed by a coiled coil
  (395-422), and two predicted transmembrane helices (478-498, 541-561). This is the
  canonical SREBP layout: an N-terminal transcription factor tethered to the ER by a
  hairpin of two TM segments [file:worm/sbp-1/sbp-1-uniprot.txt "TRANSMEM        478..498"].
- By similarity with mammalian SREBF1 the full-length precursor sits in the ER membrane
  and is cleaved in the Golgi, releasing the N-terminal factor to the nucleus
  [UniProt CC FUNCTION, ECO:0000250|UniProtKB:Q9WTN3].

## Molecular function

- Grove et al. 2009 profiled dimerization, expression and DNA-binding specificity of
  all *C. elegans* bHLH factors [PMID:19632181 "We comprehensively identify dimerization partners, spatiotemporal expression patterns, and DNA-binding specificities for the C. elegans bHLH family of TFs"]. Abstract only in the cache; the WormBase IDA for DNA-binding TF activity rests on this paper.
- SBP-1 activation of target genes depends on the Mediator subunit MDT-15 (ARC105/MED15
  ortholog). Human SREBP binds the ARC105 KIX domain [PMID:16799563 "Here we show that SREBPs use the evolutionarily conserved ARC105 (also called MED15) subunit to activate target genes"],
  and in worms "both SBP-1 and MDT-15 control transcription of genes governing desaturation of stearic acid to oleic acid" [PMID:16799563].

## Target genes and lipid-metabolic outputs

- Lipogenic targets: ACC, FAS, G3PA (McKay 2003, cited in PMID:15340492: "They have also shown that lpd-1 regulates the expression of several lipogenic enzymes, acetyl-CoA carboxilase (ACC), FAS, and glycerol 3-phosphate acyltransferase (G3PA)").
- Fatty-acid elongases elo-5 and elo-6 needed for monomethyl branched-chain fatty acid
  (mmBCFA) synthesis [PMID:15340492 "The fact that lpd-1, elo-5, and elo-6 are expressed in the same cells concurrently and that the GFP reporter analysis indicated that elo-5 and elo-6 transcription is downregulated in the absence of lpd-1 suggests that elo-5 and elo-6 are likely to be the targets of lpd-1."];
  [PMID:15340492 "LPD-1 is important for production of mmBCFAs as well as other very-long-chain FAs, whereas LPD-2 has no specificity for any particular type of FA."]
- Delta-9 desaturases fat-5, fat-6, fat-7 [PMID:22035958 "Concomitantly, expression of multiple SBP-1-dependent genes, including the palmitoyl-CoA desaturase fat-5 and the stearoyl-CoA desaturases fat-6 and fat-7 were increased in both sams-1(RNAi) and sams-1(lof) animals (Figure 2F, S2A)."]; elo-2, fat-2, fat-5 by RT-PCR [PMID:19936816 "RT-PCR analysis revealed a considerable decrease in the expression of fatty acid synthetic genes (including elo-2, fat-2, and fat-5)"].
- LC-PUFA (EPA) synthesis downstream of SBP-1 in AMsh glia [PMID:33370778 "Together, these data show that the LC-PUFA synthesis pathway lies downstream of sbp-1, where the fatty acid EPA appears to function as a potential signal for the inhibition of AMsh cell growth."]
- Reported cholesterol-independence in worms [PMID:33370778 "elegans SREBP homolog, SBP-1, is only involved in the regulation of fatty acids but not cholesterol synthesis, where it controls the expression of several lipogenic enzymes [19–21]."]

## Physiology and phenotypes (downstream, mostly indirect)

- Loss: pale, skinny, larval-arrested worms lacking fat [PMID:12530969 "Worms deficient in either of these genes displayed a lipid-depleted phenotype-pale, skinny, larval-arrested worms that lack fat stores."].
- Reduced body size, fat and egg-laying [PMID:19936816 "An sbp-1 knockdown caused a reduction in body size, fat storage, and egg-laying activity."]; oleate rescues fat storage, fertility, size and locomotion [PMID:16799563].
- Hypoxia: SBP-1 activated by oxygen deprivation and required for hypoxia-induced fat accumulation [PMID:19187779 "SBP-1 knockdown prevented hypoxia-induced fat accumulation and the associated increase in worm width/length ratio"].
- Zinc: SBP-1 negatively regulates zinc levels; zinc reduction represses SBP-1 nuclear translocation [PMID:28710073 "Nevertheless, these data clearly indicate that SBP-1 negatively regulates zinc homeostasis and that the high level of zinc in the sbp-1(ep79) mutant requires the activity of SUR-7."].
- Transgenerational lipid accumulation after high-fat diet requires SBP-1 in F1 and wdr-5.1 induction [PMID:35140229 "In addition, the elevated transcription level of wdr-5.1 induced by HFD was abrogated in the sbp-1 mutant"].

## Regulation of SBP-1 itself

- Nuclear accumulation of GFP::SBP-1 rises when SAM or PC synthesis is limited
  (sams-1, pcyt-1, cept-1, pmt-1 RNAi), forming a PC feedback loop [PMID:22035958 "Indeed, GFP∷SBP-1 showed increased nuclear accumulation after sams-1 RNAi (Figure 2E), suggesting that levels of transcriptionally active SBP-1 are increased."].
- In AMsh glia, Golgi-localised RNF-145 restrains SBP-1 activation until EAS-1 moves it
  to the trans-Golgi in adults [PMID:33370778 "These data suggest that RNF-145 inhibits SBP-1 activation while in the cis-Golgi during early stages of development for faster AMsh growth, and growth slows when EAS-1 mediates the translocation of RNF-145 from the cis-Golgi to the trans-Golgi, thereby releasing inhibition on SBP-1 activation and slowing down growth."].
- Note: the worm genome has no clear SCAP/INSIG sterol-sensing system as far as reviewed
  here; the proteolytic activation mechanism of SBP-1 is inferred from mammals and is not
  directly demonstrated in the cached papers.
