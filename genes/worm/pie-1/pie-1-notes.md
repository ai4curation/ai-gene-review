# pie-1 (Q94131, WBGene00004027) review notes

## Provenance of this research

- Automated deep research (FutureHouse, Perplexity, OpenAI) was not available in this
  environment: no provider API keys. No `-deep-research-<provider>.md` file was
  generated for pie-1. The only provider file is the verbatim WormBase description
  (`pie-1-deep-research-wormbase.md`, emitted by `just mod-description-deep-research`).
- Literature was gathered by hand on 2026-11-16:
  - PubMed E-utilities query `pie-1[tiab] AND elegans[tiab]` (56 hits, sorted by date);
    titles screened, and the papers below cached with `just fetch-pmid`.
  - Web searches: "PIE-1 C. elegans zinc finger RNA binding nos-2 3'UTR direct binding";
    "PIE-1 tandem zinc finger RNA binding affinity Ryder MEX-5 POS-1 OMA-1"; "PIE-1
    Caenorhabditis elegans 2022 2023 2024 germline transcriptional repression".
  - Full text of two abstract-only papers was read on PMC via the web (not cached):
    Zhang et al. 2003 (PMC196018) and Oldenbroek et al. 2013 (PMC3817945). Statements
    from them that are not in the cached abstracts are marked "(PMC full text, read
    online)" below and are not used as `supporting_text`.

## Identity

- 335-aa CCCH tandem zinc finger (TZF) protein, nematode-specific subfamily
  PTHR12547:SF132 of the TIS11/ZFP36 family. ZF1 (aa 98-126) has the TIS11 spacing
  C-x8-C-x5-C-x3-H; ZF2 (aa 184-211) is C-x7-C-x5-C-x3-H (checked on the UniProt
  sequence). C-terminal YAPMAPT (aa 284-290) resembles the Pol II CTD heptad. Lys68 is
  SUMOylated in adult germ cells.

## Nuclear function: global repression of Pol II transcription in the P lineage

- [PMID:8751441 "This asymmetry depends on the activity of the germline specific factor,
  PIE-1."] [PMID:8751441 "ectopic expression of PIE-1 in somatic blastomeres can
  significantly reduce the accumulation of new transcripts in these cells."]
- [PMID:9187145 "We show here that PIE-1 is also required for the germ-line-specific
  pattern of RNA polymerase II phosphorylation."]
- [PMID:9925644 "We have determined that PIE-1 can function as a transcriptional
  repressor in cell culture assays."] Repression domain element resembles the CTD.
- [PMID:12651893 "It binds CycT1 via an alanine-containing heptapeptide repeat and
  inhibits transcriptional elongation."] Human cell reporter assays; no in vitro kinase
  assay (PMC full text, read online): PIE-1 competes with the CTD for CycT1 binding.
- [PMID:18202370 "Our results support the view that PIE-1 inhibits P-TEFb using the
  CTD-like motif YAPMAPT. This activity is required to block serine 2 phosphorylation in
  germline blastomeres, but unexpectedly is not essential for transcriptional repression
  or specification of the germline."] [PMID:18202370 "We find that sequences outside of
  the YAPMAPT are required to inhibit serine 5 phosphorylation, and that this second
  inhibitory mechanism is essential for transcriptional repression and specification of
  the germ lineage."]
- PIE-1 acts from the 4-cell stage; OMA-1/2 repress in P0/P1 via TAF-4
  [PMID:18854162 "The protein PIE-1 represses transcription in the later germline
  blastomeres but not in the earlier germline blastomeres P0 and P1."]
- After PIE-1 degradation in Z2/Z3, a chromatin mechanism takes over
  [PMID:14602075 "PIE-1 is degraded upon the birth of the germ cell precursors, Z2 and
  Z3."]
- Oocytes: PIE-1 is also needed for global transcriptional silencing of prophase-arrested
  oocytes, and is sequestered in the nucleolus until the -2 position
  [PMID:37478128 "we show that all three of these silencing systems, TOP-2/condensin II,
  H3K9me, and PIE-1, are required for transcriptional repression in oocytes."]
  [PMID:37478128 "Importantly, in oocytes distal to -2, PIE-1-GFP is localized
  predominantly in nucleoli (Fig 9)."]
- P lineage also needs TOP-2/condensin II, but PIE-1 can silence on its own when
  misexpressed [PMID:39358855 "PIE-1 can silence transcription independently of
  TOP-2/condensin II when misexpressed in somatic cells."]

## Cytoplasmic function: RNA binding and activation of maternal mRNA expression

- nos-2: [PMID:11316796 "it is required for efficient expression of the maternally
  encoded Nanos homolog NOS-2."] [PMID:11316796 "A mutation in PIE-1's second CCCH
  finger reduces NOS-2 expression without affecting transcriptional repression"]
- mom-2: Oldenbroek et al. 2013 [PMID:24131629 "These nine proteins all directly bind
  the mom-2 3'UTR in vitro and function as positive or negative regulators of mom-2
  translation in vivo."] PMC full text (read online): Flag-PIE-1 purified from HeLa
  cells binds the mom-2 3'UTR in biotin-RNA pull-downs in a sense-strand-specific
  manner; pie-1(zu154) reduces the GFP::H2B-mom-2 3'UTR reporter about 54% in P3;
  "PIE-1, MEX-1 and POS-1 function together to promote the translation".
- Gauvin et al. 2018 summarise both [PMID:30279189 "In addition to its inhibition of
  transcription in the nucleus, PIE-1 is also present in the cytoplasm where it acts to
  regulate translation of at least two transcripts, mom-2 and nos-2"]
  [PMID:30279189 "Consistent with this possibility, PIE-1 promotes the translation of
  mom-2 mRNA in P2"]
- No evidence found that PIE-1 represses translation, recruits CCR4-NOT or shortens
  poly(A) tails (the TTP-family functions propagated by IBA). No affinity or sequence
  specificity measurement for PIE-1 RNA binding was found.

## Asymmetric localization and degradation

- [PMID:9705228 "We show that PIE-1 is uniformly distributed in oocytes and newly
  fertilized eggs, and becomes localized asymmetrically in the late one-cell stage."]
  [PMID:9705228 "We find that mutants that disrupt the asymmetric divisions of germline
  blastomeres mislocalize PIE-1"]
- [PMID:10983990 "The first acts before cell division to enrich PIE-1 in the cytoplasm
  destined for the germline daughter. The second acts after cell division to eliminate
  any PIE-1 left in the somatic daughter."] ZF1 is the degradation signal.
- ZIF-1/CUL-2 degrades ZF1 proteins in somatic cells [PMID:12894212 "Degradation is
  activated in somatic cells by the redundant CCCH finger proteins MEX-5 and MEX-6, which
  are counteracted in the germ line by the PAR-1 kinase."]
- MEX-5/6 link PAR polarity to germline-protein asymmetry [PMID:10882103 "Ectopic
  expression of MEX-5 is sufficient to inhibit the expression of germline proteins"].
- Gradient by reaction/diffusion [PMID:19221192 "the diffusion coefficient of PIE-1 is
  reversibly reduced in the posterior, resulting in a stable protein gradient across the
  zygote at steady state."]
- PIE-1 is also translated in the P lineage (PMID:30279189).
- Locations: nucleus, cytoplasm, centrosomes (both, then only the germline-destined
  one), P granules [PMID:8751440 "PIE-1 initially associates with both centrosomes of
  the mitotic spindle."] [PMID:9705228 "the cellular and subcellular distribution of
  PIE-1 remarkably parallels that of the P granules"] [PMID:34003111 "As expected, in
  embryonic germ cells, PIE-1::GFP localized to nuclei, cytoplasm, and cytoplasmic P
  granules"]

## Adult germline: SUMO and HDA-1

- [PMID:34003111 "Here, we show that PIE-1 also functions in the meiotic ovary where it
  becomes SUMOylated and engages the small ubiquitin-like modifier (SUMO)-conjugating
  machinery."]
- [PMID:34003111 "Surprisingly, whereas PIE-1 was originally thought to inhibit the
  MEP-1/Mi-2/HDA-1 complex in embryos, we show that in the germline PIE-1 acts in concert
  with the SUMO pathway to promote the association of MEP-1 with HDA-1, and to maintain
  the hypoacetylation of germline chromatin."]
- K68R is viable with reduced fertility; synthetic lethal with gei-17 null.
- The 2002 model (PMID:12507426) was the opposite sign in embryos: [PMID:12507426 "Our
  findings support a model in which PIE-1 inhibits MEP-1 and associated factors to
  maintain the pluripotency of germ cells"]

## Phenotypes

- [PMID:1623520 "In pie-1 mutants one additional posterior blastomere adopts an MS-like
  fate"] [PMID:8751440 "Mutations in the maternal gene pie-1 result in the germline
  blastomeres adopting somatic cell fates."]
- P2 cytokinesis protection [PMID:38696255 "we identified two canonical germ fate
  determinants required for P2-specific cytokinetic protection: PIE-1 and POS-1."]
  Mechanism unknown; treated as an indirect, non-annotated phenotype.

## Source text checks

- WormBase: all claims trace (CCCH type, germline fate, Pol II repression, uniform then
  posterior localization, PAR-1/MEX-5/MEX-6 control). The C-x8-C-x5-C-x3-H spacing is that
  of ZF1; ZF2 has x7. Omits the cytoplasmic RNA-binding/translational-activation function
  and the adult germline roles.
- UniProt FUNCTION: "Inhibits the histone deacetylase activity of hda-1 (PubMed:34003111)"
  inverts the cited paper, which shows PIE-1 promotes HDA-1 SUMOylation, MEP-1/HDA-1
  association and germline hypoacetylation. "Represses transcriptional activation of
  cdk-9 and cit-1.1" misdescribes P-TEFb inhibition as repression of the P-TEFb genes.

## Annotation decisions (summary)

- Core: GO:0000122 (IDA); cell fate determination (IMP); nucleus; mRNA binding.
- IBA TTP-family functions (ARE binding, translation repressor, adaptor, poly(A)
  shortening): ARE binding generalised to mRNA 3'-UTR binding (MODIFY, mom-2 3'UTR
  binding); the repressive functions marked over-annotated (PIE-1 activates translation
  of its known targets).
- NEW: positive regulation of translation (mom-2, nos-2); nucleolus (oocytes).

## 2026-11-18: second core function narrowed to what was shown

While pie-1 was being linked into `primordial_germ_cell_specification`, the second core
function was found to say that PIE-1 binds the 3' UTRs of both mom-2 and nos-2.
- 3' UTR binding is shown only for mom-2 (PMID:24131629, in vitro).
- For nos-2, PIE-1 is "required for efficient expression of the maternally encoded
  Nanos homolog NOS-2" (PMID:11316796), and direct binding has not been shown.

The core function now says this. The gene description already did.
