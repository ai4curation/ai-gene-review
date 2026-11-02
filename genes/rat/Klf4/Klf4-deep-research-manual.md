# Klf4 (rat, Q923V7) - manual literature research

No deep-research provider was available for this review, so this file records a manual
literature survey based on cached publications (`publications/PMID_*.md`) and PubMed
searches. Every statement carries its source.

## Identity and domain architecture

- Q923V7 is an unreviewed TrEMBL entry (482 aa) for rat Klf4 (RGD:621445, GeneID 114505).
  It carries three C-terminal C2H2 zinc fingers (PROSITE PS50157 at 399-428, 429-458,
  459-482), Pfam PF00096 x3, and PANTHER PTHR23235:SF117 "KRUEPPEL-LIKE FACTOR 4"
  [file:rat/Klf4/Klf4-uniprot.txt].
- KLFs bind GC-rich/CACCC elements through the three C-terminal zinc fingers
  [PMID:18406357 "Klfs bind to consensus GC-rich or CACCC sequences through the three
  C-terminal zinc fingers"].

## DNA binding and transcriptional activation (rat experiments)

- Rat KLF4 (GKLF) was cloned from a rat mesangial cell library in a yeast one-hybrid
  screen with the LAMC1 bcn-1 element; it binds bcn-1 and activates the LAMC1 promoter in
  synergy with Sp1 [PMID:12034813 "We show that GKLF binds bcn-1, but this binding is not
  required for the GKLF-mediated activation of the LAMC1 promoter"; "the synergistic
  action of GKLF and Sp1 is dependent on the promoter context and the integrity of GKLF
  activation and DNA-binding domain"].
- KLF4 assembles with CREB and p53 at the bradykinin B2 receptor enhancer on chromatin in
  developing rat kidney, with CBP recruitment [PMID:15632413 "assembly of CREB, p53, and
  KLF-4 on chromatin at the endogenous B2R promoter is developmentally regulated and is
  accompanied by CBP recruitment and histone hyperacetylation"].
- In rat aortic VSMCs, GKLF activates the p53 promoter and inhibits proliferation in a
  p53-dependent manner [PMID:17659301 "GKLF overexpression led to an enhanced p53 promoter
  activity and increased p53 mRNA and protein expression"; "p53 induction is essential
  for the interference of GKLF with VSMC proliferation"].
- KLF4 binds two KLF sites in the SM22alpha promoter; binding is modulated by
  acetylation (p300) and deacetylation (HDAC2) [PMID:21252119 "KLF4 was directly bound to
  the KLF4 binding sites 1 ((-263)CACCC(-259)) and 2 ((-136)GTGGG(-132)) of the SM22α
  promoter"; "increasing its interaction with p300"; "increasing its interaction with
  histone deacetylase 2 (HDAC2)"].
- HDAC2 interacts with and deacetylates KLF4; ATRA dissociates the complex
  [PMID:19486889 "HDAC2 directly deacetylated KLF4"].

## Transcriptional repression and antiproliferative role in VSMCs

- KLF4 binds the RARalpha 5' regulatory region and down-regulates RARalpha; it also
  inhibits PDGFRbeta expression, blocking PI3K and ERK signalling [PMID:19531492 "Klf4
  directly binds to the 5' regulatory region of RAR alpha, down-regulates RAR alpha
  expression"; "Klf4 inhibits RAR alpha and PDGFR beta expression while blocking PI3K and
  ERK signaling induced by Am80 and PDGF-BB, respectively"]. The effect on PI3K is
  therefore transcriptional and indirect.
- In mouse, KLF4 represses SMC differentiation marker genes via TCE elements, binding them
  in chromatin [PMID:12970361 "results of chromatin immunoprecipitation assays showed GKLF
  binding to TCE containing regions of various SMC marker gene promoters within intact
  chromatin"]; conditional knockout increases neointima after injury, and KLF4 induces
  p21 with p53 [PMID:18483411 "Klf4 mutant mice exhibited enhanced neointimal formation in
  response to vascular injury caused by increased cellular proliferation in the media"].
- KLF4 mediates p53 transactivation of p21WAF1/Cip1 via a Sp1-like element
  [PMID:10749849 "GKLF activates p21(WAF1/Cip1) through a specific Sp1-like cis-element
  in the p21(WAF1/Cip1) proximal promoter"].

## Regulation of Klf4 expression (rat)

- Endothelin-1 and H2O2 induce Klf4 mRNA in neonatal rat cardiac myocytes as an
  immediate-early gene, partly ERK1/2-dependent [PMID:18406357 "H2O2 increased expression
  of Klf2, Klf4 and Klf6"; "Klf2, Klf4 and Klf6 are regulated as IEGs in response to
  ET-1"].
- ATRA and PDGF-BB induce KLF4 in VSMCs [PMID:21252119 "ATRA and PDGF-BB induced KLF4
  expression"].

## Roles known from other mammals (basis of ISO/IEA rows)

- Skin barrier: Klf4-/- mice die at birth from barrier loss [PMID:10431239 "Klf4-/- mice
  die shortly after birth due to loss of skin barrier function"].
- Reprogramming: one of the four Yamanaka factors [PMID:16904174 "introducing four
  factors, Oct3/4, Sox2, c-Myc, and Klf4, under ES cell culture conditions"].
- Endothelium: anti-inflammatory, induces eNOS and thrombomodulin, reduces leukocyte
  adhesion [PMID:17339326 "Kruppel-like factor 4 expression markedly decreases
  inflammatory cell adhesion to the endothelial surface"].
