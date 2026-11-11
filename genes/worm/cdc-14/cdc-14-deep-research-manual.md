# cdc-14 (C. elegans, P81299; C17G10.4; WBGene00000383) - manual literature research

No deep-research provider API was available in this session, so this summary was
assembled manually from the cached publications in `publications/` and PubMed
searches ("cdc-14 elegans"; "(cdc14 OR CDC-14) AND Caenorhabditis AND
(phosphatase OR quiescence OR cki-1 OR cilia)"). Only a handful of primary papers
on the worm gene exist.

## Identity and family

- cdc-14 encodes the sole C. elegans member of the CDC14 family of
  dual-specificity (Cys-dependent, PTP-fold) phosphatases. UniProt: "Belongs to the
  protein-tyrosine phosphatase family. Non-receptor class CDC14 subfamily."
  Domains: DSPn (PF14671) N-terminal domain plus a DSPc catalytic domain (SM00195),
  PROSITE TYR_PHOSPHATASE_1 active-site signature (catalytic Cys295).
- Six splice isoforms (UniProt a, c, d, e, g, h); all share the N-terminal exons
  encoding the phosphatase domain and differ at the C terminus
  [PMID:21723944 "All six identified variants utilize the identical start site followed by the four 5′-most exons which encode the phosphatase domain."].

## Catalytic activity (Gruneberg et al. 2002, PMID:12213836, full text)

- Recombinant 6His-CeCDC-14 hydrolysed para-nitrophenyl phosphate; activity was
  abolished by C295S and inhibited by vanadate
  [PMID:12213836 "This phosphatase activity was completely abolished upon mutation of the presumptive catalytic cysteine 295 to serine."].
- The recombinant enzyme dephosphorylated histone H1 but not Cdk1-phosphorylated
  ZEN-4/CYK-4 (cited as personal communication)
  [PMID:12213836 "although the recombinant phosphatase readily dephosphorylated histone H1, no dephosphorylation of either ZEN-4 or CYK-4 could be observed"].
- Mishima et al. 2004 (PMID:15282614, abstract only) is the source of the WormBase
  IDA for phosphoprotein phosphatase activity; the abstract describes Cdk1
  phosphorylation of ZEN-4 but does not mention CDC-14, so the assay details are
  not visible to us.

## Localization

- Gruneberg 2002 (antibody, embryos): central spindle in anaphase, midbody in
  telophase; no centrosome or nuclear staining
  [PMID:12213836 "CeCDC-14 itself localizes to the central spindle in anaphase and to the midbody in telophase."]
  [PMID:12213836 "no staining of centrosomes or nuclei could be seen"].
- Saito 2004 (GFP-CDC-14; abstract only in cache): dynamic localization,
  cytoplasmic accumulation in G1; UniProt summarises centrosome at prophase,
  spindle/asters/midzone in metaphase-anaphase, nucleus/nucleolus in postmitotic
  cells [PMID:15247923 "localized dynamically and accumulated in the cytoplasm during G1 phase"].
- Roy 2011 (GFP-CDC-14C): mainly cytoplasmic in interphase owing to XPO-1-dependent
  nuclear export, with a nuclear pool that increases during quiescence; no
  significant nucleolar accumulation
  [PMID:21723944 "we do not observe significant nucleolar accumulation of CDC-14C in interphase cells"].

## Developmental cell-cycle quiescence (core biology)

- Forward genetic screen: cdc-14 mutants (he118, he141) have extra divisions in
  vulval precursor and intestinal lineages, without mitotic or fate defects; cdc-14
  acts upstream of cki-1 (Cip/Kip CKI) to promote nuclear CKI-1 accumulation
  [PMID:15247923 "inactivation of C. elegans cdc-14 resulted in extra divisions in multiple lineages, with no apparent defects in mitosis or cell-fate determination"]
  [PMID:15247923 "cdc-14 functions upstream of the cki-1 Cip/Kip inhibitor to promote accumulation of CKI-1 in the nucleus"].
- CDC-14C is the splice form needed in VPCs; cyclin D (cyd-1) promotes CDC-14C
  nuclear export; cdc-14 acts in parallel to lin-35 (Rb) downstream of cyd-1
  [PMID:21723944 "These data support a model wherein cyd-1 promotes G1/S progression by inhibiting parallel processes requiring cdc-14 and lin-35 activities."].
- Reviews/commentary: Kipreos 2004 (PMID:15303097, "Developmental quiescence: Cdc14
  moonlighting in G1"); Koreth & van den Heuvel 2005 (PMID:15838512)
  [PMID:15838512 "we recently found that the CDC-14 phosphatase promotes maintenance of the quiescent state"].

## The cytokinesis controversy

- Gruneberg 2002 RNAi (injection) gave multinucleate, lethal embryos with failed
  central spindle assembly, ZEN-4/AIR-2 mislocalisation and failed polar body
  extrusion [PMID:12213836 "We show that CeCDC-14 is required for cytokinesis but may be dispensable for progression of the early embryonic cell cycles."].
- Saito 2004 and Roy 2011 found that null mutants are viable and fertile with no
  cytokinesis defect, and that he141 does not enhance zen-4(or153ts); Roy attributes
  the RNAi phenotype to off-target effects
  [PMID:21723944 "the lethality arising from defective cytokinesis previously observed following cdc-14(RNAi) was due to off-target effects"].
- UniProt records the conflict in a CAUTION note. Conclusion for this review: the
  genetic-null data outweigh the RNAi phenotype; cytokinesis, central spindle
  assembly, polar body extrusion and microtubule organisation are not supported as
  functions of cdc-14 in vivo. Localisation to the spindle midzone/midbody is seen in
  both groups' data and is retained.

## Open questions

- Direct in vivo substrates (CKI-1 itself? CDK-phosphorylated sites on CKI-1?)
  are not established.
- Whether cdc-14 has roles in cilia (as vertebrate CDC14B), meiosis or DNA damage
  checkpoint is untested [PMID:21723944 "it will be interesting to see if similar defects are revealed in cdc-14 mutant worms"].
