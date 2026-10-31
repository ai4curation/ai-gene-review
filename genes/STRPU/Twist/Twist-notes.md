# Twist (Sp-Twist, A7Z0B7) — curation notes

## Identity
- UniProt A7Z0B7 (TrEMBL, 204 aa), SubName "Twist", derived from the third-party-annotation
  record EMBL BK006287 / protein DAA06084.1; RefSeq NP_001099179.1, GeneID 753325. The UniProt RX
  line cites Gitelman 2007 [PMID:17567594 "Twist genes are essential for embryonic development and
  are conserved from jellyfish to human."], a phylogenetic survey of the vertebrate twist family
  (abstract only in cache; it does not report any sea urchin experiment).
- The DAA06084 protein itself was annotated and deposited by Wu, Yang & McClay 2008
  [PMID:18495103 "Strongylocentrotus purpuratus Twist protein sequence was annotated and deposited
  on GenBank (Accession Number DAA06084 )."], who found the S. purpuratus gene in silico
  [PMID:18495103 "we identified the Sptwist gene in silico , which encodes a 204 amino acid
  polypeptide, by blasting the assembly of S. purpuratus genome with the coding sequence of
  Lvtwist"]. The 204-aa length matches the UniProt sequence, so A7Z0B7 is the S. purpuratus
  twist gene of the McClay-lab GRN papers with HIGH confidence. SpTwist and LvTwist are 92%
  identical [PMID:18495103 "The ClustalW pairwise alignment between LvTwist and SpTwist shows that
  two proteins share an overall amino acid identity of 92%"].
- Domains (UniProt DR): bHLH IPR011598 (residues 109-160; PROSITE PS50888), TWIST1-type bHLH
  IPR047093 (CDD cd11412 bHLH_TS_TWIST1), PANTHER PTHR23349 subfamily SF50. The C-terminal
  sequence ends in ...ERLSYAFSVWRMEG..., i.e. the Twist-family "WR motif"
  [PMID:18495103 "LvTwist is identical to almost all Twist proteins except Drosophila Twist
  (DmTwist) and amphioxus Twist (BbTwist; Yasui et al., 1998 ) at all 14 residues of the WR motif"].
  Single twist gene in the sea urchin genome [PMID:24598159 "The sea urchin genome did not go
  through whole genome duplications experienced by the vertebrate lineage, so each gene is present
  as a single copy"].
- No GO-CAM contains this gene (`gocams/index.tsv` has no STRPU rows).

## IMPORTANT organism caveat
- All functional data on sea urchin Twist come from Lytechinus variegatus (LvTwist), not from
  S. purpuratus: Wu et al. 2008 [PMID:18495103 "In this study, we report the identification,
  characterization, and functional analyses of Lvtwist , a member of the Twist family of
  transcription factors in Lytechinus variegatus ."] and Saunders & McClay 2014 [PMID:24598159
  "We first delineated the GRN specifying the skeletogenic lineage in L. variegatus ."]. For
  S. purpuratus the only facts are the in-silico gene identification and the 92% identity.
- twist is not a node of the Oliveri/Tu/Davidson 2008 S. purpuratus skeletogenic GRN
  [PMID:24598159 "The biggest difference between the current S. purpuratus GRN model and that
  shown in Fig. 1 is the observation that snail and twist are part of the L. variegatus GRN
  (Wu et al., 2007; Wu et al., 2008 )."]; the Sp model lists alx1, ets1, tbr, tel, erg, hex,
  foxb, dri as drivers of the differentiation genes [PMID:18413610 "these differentiation genes
  require as drivers products of all of the now familiar components of the skeletogenic
  regulatory state ( alx1 , ets1 , tbr , tel , erg , hex , foxb , dri )"]. Rafiq 2014
  (PMID:24496631, abstract) and Shashikant 2018 (PMID:30264451, full text) do not mention twist.
- Consequence for the review: NEW rows are kept to the minimum that the L. variegatus
  perturbation data support, are recorded as IMP on PMID:18495103, and every such row states
  that the evidence is from the congener (orthology is secure: single-copy gene, 92% identity).

## Expression (L. variegatus)
- Low maternal/early level; rises from blastula, dips at mesenchyme blastula, rises again in
  gastrula [PMID:18495103 "the expression level of Lvtwist remains relatively low during early
  cleavage stages, and the expression increases starting from blastula stages, then transiently
  drops at mesenchyme blastula (MB) stage"].
- Spatially: vegetal plate at late hatched blastula, then PMCs [PMID:18495103 "At early
  mesenchyme blastula (MB) stage, Lvtwist mRNA is predominantly expressed in ingressing PMCs"];
  PMC expression persists through gastrulation, unlike snail. Later also in SMC territory
  [PMID:18495103 "Lvtwist expression is observed in the SMC territory from the early gastrula
  (EG) stage ( Fig. 2F )"].

## Place in the skeletogenic (micromere/PMC) GRN
- Upstream: Alx1 is required for twist expression; Ets1 is not [PMID:18495103 "At LHB and EMB
  stage, the expression of Lvtwist is reduced in Alx1 morphants, but not in either Ets1 or Sna
  morphants."].
- Downstream/feedback: Twist is needed to maintain alx1 expression after ingression, not to
  initiate it [PMID:18495103 "In Twi morphants, Lvalx1 expression level is reduced at MB stage,
  but not at earlier stages, while Lvets1 expression is unaffected in Twi morphants."]
  [PMID:18495103 "Alx1 appears necessary for twist expression, and later Twist appears to feed
  back to positively regulate alx1 expression ( Fig. 8 )."]. Directness untested
  [PMID:18495103 "However, whether this mutually positive regulation is due to direct intergenic
  inputs will requires further examination to confirm the relationship, such as cis-regulatoy
  analyses."].
- Differentiation genes: msp130, sm50, sm30 transcripts fall in Twist morphants
  [PMID:18495103 "Downstream of Twist, the mRNA expression level of Lvmsp130, Lvsm50 , and Lvsm30
  were examined by QPCR, and were all significantly reduced in Twi morphants when compared to MB
  controls"] [PMID:18495103 "These data show that Lvtwist functions upstream of the PMC
  skeletogenic differentiation program."].
- Saunders & McClay 2014 place twist among the 10 proximal EMT regulators downstream of
  alx1/ets1/tbr [PMID:24598159 "Three TFs highest in the GRN specified and activated EMT (alx1,
  ets1, tbr) and the 10 TFs downstream of those (tel, erg, hex, tgif, snail, twist, foxn2/3, dri,
  foxb, foxo) were also required for EMT."] and define an alx1-twist-snail positive-feedback
  sub-circuit for de-adhesion [PMID:24598159 "Therefore, alx1, twist and snail display control
  over adhesive state change and make a distinct sub-circuit of the GRN, a positive-feedback
  lockdown, that governs the de-adhesion process ( Fig. 7E )."] [PMID:24598159 "In the sea
  urchin de-adhesion sub-circuit, alx1 is upstream of both twist and snail, with twist also
  positively regulating alx1."].

## Perturbation phenotypes (L. variegatus, two non-overlapping morpholinos; mRNA overexpression)
- Summary [PMID:18495103 "Perturbations of Twist either by morpholino knockdown or by
  overexpression result in defects in progressive phases of PMC development, including
  specification, ingression/EMT, differentiation and skeletogenesis."].
- Ingression delayed, not abolished [PMID:18495103 "PMCs of Twi morphants failed to ingress
  (>80%, Fig. 3E ) until after a significant delay."]; cell-autonomous requirement shown by
  micromere transplantation [PMID:18495103 "The chimeras show that Twist is essential in
  micromeres for these cells to ingress punctually and migrate properly into the blastocoel as
  PMCs."]. In the 2014 five-assay dissection, twist morphant PMCs make the laminin hole, move,
  constrict and keep polarity but fail to de-adhere [PMID:24598159 "Our analysis of both snail
  and twist knockdowns showed a failure of PMCs to complete EMT in spite of four other
  successful cell state changes"].
- No skeleton [PMID:18495103 "Twi morphants failed to form a skeleton ( Fig. 3I )."]; PMC
  syncytial fusion fails cell-autonomously [PMID:18495103 "Taken together, these data support
  the hypothesis that Twist is required for PMC fusion, and therefore for developmental events
  upstream of skeletogenesis."]. Overexpression gives extra/mis-positioned spicules.
- Specification-state maintenance [PMID:18495103 "Evidence is presented that Twist expression is
  required for the maintenance of the PMC specification state, and a reciprocal regulation
  between Alx1 and Twist offers stability for the subsequent processes, such as PMC
  differentiation and skeletogenesis."].
- SMC derivatives also affected (pleiotropic, later role) [PMID:18495103 "Other SMC-associated
  phenotypes were also observed to persist including reduction of pigment cells ( Fig. 3E,K ;
  Fig. S1 ) and absence of muscle"].

## Decisions for the GOA review
- The 8 GOA rows are all electronic (5 IBA from PAINT node PTN002360678 = twist family, 3 IEA).
  The IBA MF/CC/BP rows (GO:0000981, GO:0000977, GO:0005634, GO:0006357) describe a bHLH TF and
  are accepted; sea urchin evidence for transcriptional regulation is indirect (knockdown lowers
  alx1 and biomineralization transcripts) and from L. variegatus, so no activator/repressor
  sign is asserted. GO:0032502 developmental process (IBA) and GO:0046983 protein dimerization
  (InterPro) are kept as non-core: true by family but uninformative.
- NEW (all IMP, PMID:18495103, L. variegatus caveat recorded): GO:0010718 positive regulation of
  EMT (delayed/incomplete ingression, de-adhesion sub-circuit); GO:0070169 positive regulation of
  biomineral tissue development (skeleton-minus, reduced msp130/sm50/sm30, PMC fusion failure);
  GO:0001710 mesodermal cell fate commitment (maintenance of the PMC specification state via the
  Alx1-Twist feedback loop; same term as the sibling Hex/Erg state-stabilization reviews).
- Not proposed: positive regulation of transcription by RNA polymerase II (no direct target or
  cis-regulatory evidence); any muscle/pigment cell term (secondary, under-explored); mesodermal
  cell fate specification (twist is activated after alx1/ets1 and acts in maintenance, not
  initiation).
