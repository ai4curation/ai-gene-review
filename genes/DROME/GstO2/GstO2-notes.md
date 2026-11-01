# GstO2 review notes

- Fetched 2026-10-28; UniProt Q9VSL5 confirmed (TrEMBL, "Glutathione S transferase O2,
  isoform A", FlyBase FBgn0035906, GeneID 38974). GOA has 20 rows, all keyed to Q9VSL5.
- Q9VSL5 = isoform A (active-site motif CPFS, Cys31). Q9VSL4 = isoform B (CPYS). The GOA rows are
  not isoform-tagged, so experiments on either isoform land on Q9VSL5.
- Literature naming: CG6673 = "DmGSTO1" in Kim/Yim papers [PMID:22219196 "CG6673 is also called
  D. melanogaster GSTO1 (DmGSTO1)"], = GstO2 in current FlyBase/Saisawang nomenclature.
- Key paper read in full: PMID:22219196 (Kim et al. 2012 JBC). Isoform A directly glutathionylates
  ATP synthase beta in vitro, C31A dead; isoform B carries most DHAR activity in vivo.
- Decisions:
  - MF glutathione transferase activity and glutathione dehydrogenase (ascorbate) activity: ACCEPT
    (direct biochemistry, PMID:16712527, PMID:24533905, PMID:22219196).
  - NOT pyrimidodiazepine synthase: ACCEPT (only CG6781/sepia has it).
  - cytoplasm rows (IBA/IEA/ISS): MODIFY to cytosol and mitochondrion, both of which have IDA.
  - immune HMP rows from genome-wide RNAi survival screen: MARK_AS_OVER_ANNOTATED; GstO2 not
    discussed in the main text, and the two terms (positive defense, negative regulation) pull
    in opposite directions.
  - NEW protein glutathionylation (GO:0010731), IDA PMID:22219196: the enzyme itself performs
    the transfer of GSH onto ATP synthase beta (catalytic, C31-dependent), so it passes the
    participation bar. Oxidative-stress response and neuroprotection phenotypes were NOT
    added as NEW (phenotype/overexpression evidence only).
  - Deglutathionylation of FUS (PMID:35320731) is abstract-only and in vivo; raised as a question.
