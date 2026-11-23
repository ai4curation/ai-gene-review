# zen-4 (C. elegans) - manual literature review

No deep-research API was available; this summary was compiled by hand from the cached
publications in `publications/` and the UniProt record G5EG83 (unreviewed TrEMBL entry,
WormBase M03D4.1a, WBGene00006974, GeneID 177374).

## Identity and domain architecture

- zen-4 (zygotic epidermal enclosure defective) encodes the C. elegans kinesin-6 / MKLP1
  (KIF23) ortholog, 775 aa (isoform a). UniProt: N-terminal kinesin motor domain (27-426,
  PROSITE PS50067), P-loop ATP-binding motif 112-119, and C-terminal MKLP1 Arf-binding
  domain (Pfam PF16540, InterPro IPR032384). PANTHER PTHR24115:SF600 (KINESIN-LIKE PROTEIN
  KIF23). A second TrEMBL entry, Q8MQ03, also carries the zen-4 gene name.
- Two cDNA products (ZEN-4a/b) differ only at the C terminus [PMID:9693365 "The cDNAs are
  predicted to encode two products, called ZEN-4a, and ZEN-4b, which are identical from amino
  acids 1 to 745 but contain differing C-terminal domains of 30 and 27 amino acids,
  respectively."]

## Molecular function

- ZEN-4 is the motor subunit of centralspindlin, a 2:2 heterotetramer with the RhoGAP CYK-4
  [PMID:25875822 "Centralspindlin, a constitutive 2:2 heterotetramer of MKLP1 (a kinesin-6) and
  the non-motor subunit CYK4, plays important roles in cytokinesis."].
- Purified ZEN-4 is a plus-end-directed motor: in surface gliding assays and single-particle
  assays "Both Z601mAG and Z601mAG/C120 move to the plus end." [PMID:25875822]. CYK-4 binding
  slows the motor: "The Z601mAG sample showed a velocity of 221 ± 4 nm/sec while this was
  reduced in Z601mAG/C120 to 79 ± 3 nm/sec" [PMID:25875822].
- ZEN-4 alone crosslinks microtubules; CYK-4 confers antiparallel selectivity:
  "ZEN-4 in complex with CYK-4 (Z601mAG/C120) preferentially formed antiparallel overlaps (Fig
  4C v and Fig 4D) while ZEN-4 alone (Z601mAG) typically formed parallel bundles" [PMID:25875822].
  "In vitro, neither MKLP1 alone nor CYK4 alone can efficiently bundle microtubules." [PMID:25875822]
- The CYK-4 N terminus binds the globular ZEN-4 neck: "CYK4 binds to a globular mass in the
  atypically long MKLP1 neck domain between the catalytic core and the coiled coil"
  [PMID:25875822]; ZEN-4 homodimerizes through a parallel coiled coil ("the homodimers of CYK4
  and MKLP1, both of which were dimerized as parallel coiled coils, assemble into a
  heterotetramer") [PMID:25875822].
- AIR-2 (Aurora B) binds ZEN-4 directly and is needed for its spindle localization
  [PMID:11050384 abstract, "Using in vitro co-immunoprecipitation experiments, we found that
  AIR-2 and ZEN-4 interact directly."].

## Localization

- Spindle midzone in anaphase and midbody/midbody remnant [PMID:9693365 "We show that ZEN-4
  protein localizes to the spindle midzone during anaphase and persists at the midbody region
  throughout cytokinesis."]; confirmed with ZEN-4-GFP [PMID:12213836 "In wild-type embryos,
  ZEN-4-GFP began to localize to the central spindle in anaphase, and subsequently formed a
  bright spot at the position of the midbody in telophase"].
- ZEN-4 localization requires CDC-14 and vice versa [PMID:12213836].
- Meiotic anaphase: "MKLP1ZEN-4 ... also localized to the center of the meiotic anaphase
  bundles" [PMID:20729837].
- Centrosomes only occasionally, in interphase, and as unpublished data [PMID:9693365 "In
  interphase cells, ZEN-4 can occasionally be seen localized to centrosomes (our unpublished
  results)"].
- Narrow midzone domain compared with the Aurora B complex [PMID:12707312 "The localization of
  CSC-1 on the central spindle is significantly broader than the localization of ZEN-4"].

## Biological process

- Required for cytokinesis: null w35 maternal/zygotic loss gives multinucleate embryos;
  furrows initiate but regress [PMID:9693365]. Midzone microtubule bundles are lost
  ("the cytokinesis defect is preceded by the dissociation of the midzone microtubules").
- Polar body extrusion fails in ZEN-4-depleted embryos [PMID:9693365 "In embryos depleted of
  ZEN-4, the polar bodies fail to be extruded"].
- Not required for pronuclear migration [PMID:9693365 "Pronuclear migration and centrosome
  rotation occur normally, demonstrating that ZEN-4 is not necessary for these intracellular
  movements"].
- Not required for actomyosin ring formation per se [PMID:12213836 "we do not believe that
  either CeCDC-14 or ZEN-4 play a direct role in actomyosin ring formation"].
- Meiosis: ZEN-4 inhibition did not prevent meiotic anaphase microtubule bundles
  [PMID:20729837 "Inhibition of MKLP1ZEN-4 and/or the bundling protein PRC1SPD-1 did not prevent
  formation of microtubule bundles or severely disrupt anaphase chromosome separation"].
- Chromatin bridges: partial mcm-7 RNAi plus zen-4 RNAi gives chromatin bridges, interpreted as
  loss of midbody-tethered LEM-3 nuclease [PMID:29463814].
