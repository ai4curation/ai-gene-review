# polo (Drosophila melanogaster, UniProt P52304) - manual literature research

No deep-research API was available for this session, so this summary was compiled
by hand from the cached publications in `publications/` and the UniProt record.
Every claim carries an inline citation with a verbatim quote.

## Identity and domain architecture

- polo (FBgn0003124, GeneID 40232) encodes a 576-aa Ser/Thr kinase, the founding
  member of the Polo-like kinase family; it is the only Polo-like kinase in the fly
  [PMID:19529778 "is the only Drosophila Polo-like kinase family protein"].
- UniProt: N-terminal protein kinase domain (25-277), two C-terminal Polo boxes
  (391-469, 491-572), activation-loop phosphothreonine at T182
  [file:DROME/polo/polo-uniprot.txt "Belongs to the protein kinase superfamily. Ser/Thr protein kinase family. CDC5/Polo subfamily."].
- Cloned as a kinase homolog required for mitosis [PMID:1660828 "polo encodes a 577-amino-acid protein with an amino-terminal domain homologous to a serine-threonine protein kinase"].
- Activation-loop T182 is the fly equivalent of human PLK1 T210 [PMID:18798690 "phosphorylated on the activating T210/T182 (in humans and flies, respectively)"].

## Catalytic activity

- Immunoprecipitated Polo phosphorylates casein, with activity peaking at late
  anaphase/telophase in syncytial embryos [PMID:8510757 "can phosphorylate casein in vitro, and that the kinase activity peaks cyclically at late anaphase/telophase"].
- Phosphatase treatment inactivates the kinase; preferred substrates are MT-associated
  proteins of 220, 85 and 54 kDa [PMID:8890161 "converted to a single band by phosphatase treatment, which also inactivates the kinase"].
- Direct substrates identified in the fly:
  - Asp (the 220 kDa substrate), needed for aster nucleation by centrosomes
    [PMID:11283617 "Asp is the previously identified Mr 220K substrate of Polo kinase"].
  - Pon (Partner of Numb), in neuroblast asymmetric division [PMID:17805297 "Polo directly phosphorylates Partner of Numb"].
  - Greatwall [PMID:23857770 "Polo phosphorylates Gwl in vitro."].
  - Maelstrom, in oocyte determination [PMID:23136393 "We identify Polo as a kinase that mediates the phosphorylation of Maelstrom."].
  - Cnn phosphorylation in mitosis is Polo-dependent [PMID:18798690 "Cnn is phosphorylated during mitosis in a Polo-dependent manner"].

## Localization

- Cytoplasmic in interphase; on condensed chromosomes from late prophase to telophase
  [PMID:1660828 "It is predominantly cytoplasmic during interphase"].
- Centrosomes, kinetochores, cleavage furrow, midbody, interphase and central-spindle
  MTs (Polo-GFP) [PMID:18832073 "this cell line revealed the dynamic association of Polo with mitotic kinetochores and centrosomes and with the cleavage furrow and midbody in cytokinesis"].
- Nuclear envelope in syncytial embryos [PMID:18832073 "but also strongly accumulated to the nuclear envelope in this tissue"].
- Outer kinetochore early in mitosis, midbody later [PMID:19529778 "partial overlap between SUMO and Polo is observed at the outer kinetochore"].
- Spermatocytes: centrosomes, centromere/kinetochore, spindle midzone [PMID:9914376 "POLO localises to the centrosomes, the centromere/kinetochore and the spindle midzone"].
- Microtubule association through Map205, released by Cdk1 phosphorylation of Map205
  [PMID:18832073 "Polo associates with microtubules in interphase and cytokinesis, through a strong interaction with the microtubule-associated protein Map205"].

## Biological roles

1. **Centrosome maturation / spindle pole organization.** Original polo mutants have
   broad, abnormal spindle poles [PMID:3417791 "Embryos from homozygous polo females have aberrant mitotic spindles that are highly branched and have broad poles"].
   Depletion of Polo or Cnn blocks centrosome maturation [PMID:18798690 "the individual depletion of only two proteins, Polo and Centrosomin (Cnn) can completely block centrosome maturation"].
   Polo-phosphorylated Asp rescues aster nucleation [PMID:11283617 "This can be rescued by addition of phosphorylated Asp or active Polo kinase."].
2. **Kinetochore attachment / bi-orientation.** [PMID:22389397 "POLO is required to promote amphitelic attachment and chromosome bi-orientation"].
3. **Cytokinesis.** Hypomorphs fail central spindle, Pav-KLP localization and actin/septin ring
   formation in male meiosis [PMID:9813088 "they clearly establish a role for Polo kinase in the early events of cytokinesis in animal cells"].
   Polo is needed for cortical myosin recruitment [PMID:16412419 "we observed defects in the cortical recruitment of myosin and myosin regulatory light chain in Polo deficient cells"].
4. **Female meiosis and early embryo.** MTOC defects in polo eggs; failure of sperm aster growth
   and pronuclear migration [PMID:10954431 "The MTOC associated with the male pronucleus was also defective in polo eggs, and the sperm aster did not grow."].
   Meiotic entry in oogenesis and BicD transport [PMID:16971474 "On the one hand, it acts as a trigger for meiosis."].
   Matrimony binds and inhibits Polo to hold prophase I arrest [PMID:18052611 "Mtrm acts as an inhibitor of Polo"].
5. **Augmin placement in meiosis/mitosis** [PMID:24829288 "Therefore, Polo promotes Augmin's placement at kinetochores while preventing its association with spindle MTs."].
6. **Developmental contexts (downstream of cell-division role).** Neuroblast self-renewal
   via Pon/Numb (PMID:17805297); cardiac progenitor divisions downstream of Fkh factors
   (PMID:22814603); post-mitotic myotube guidance activated by Bsd kinase
   [PMID:35140224 "the control of Polo activity transitions from the Aurora kinases to the uncharacterized kinase Back Seat Driver (Bsd)"].
