# LOC542140 (ZmGT1) manual literature research

No deep-research API was available; this summary was compiled manually from cached publications
(`publications/PMID_*.md`), PubMed searches and NCBI/UniProt records.

## Identity

- UniProt A0A804M424 (TrEMBL, 748 aa), EnsemblPlants Zm00001eb057440_P003, NCBI GeneID 542140,
  RefSeq NP_001292781.1. NCBI Gene lists the aliases GT1 / ZmGT1 and GRMZM2G421491.
- The published maize glutathione transporter ZmGT1 (GenBank FJ573212) is 99.6% identical over the
  full length (745/748 residues; `LOC542140-bioinformatics/RESULTS.md`).
- A sibling TrEMBL entry for another transcript of the same gene, A0A804M423 (Zm00001eb057440_P002,
  660 aa), also exists. `just fetch-gene` resolved that one first; this review covers A0A804M424,
  the entry mapped to GeneID 542140 and RefSeq.
- Family: oligopeptide transporter (OPT) family, Pfam PF03169, InterPro IPR004813/IPR004648,
  NCBIfam TIGR00727 (ISP4_OPT) and TIGR00728, PANTHER PTHR22601. The protein has 80.3% identity to
  Arabidopsis AtOPT3 (O23482) and 53.1% to AtOPT6 (Q9T095), so it belongs to the plant OPT3 clade.

## Maize-specific literature (Pang et al., China Agricultural University)

- The authors cite their own earlier work, which is not indexed in PubMed:
  [PMID:23144728 "Our earlier work has shown that ZmGT1 is able to mediate the uptake of both GSH and GS conjugates by yeast cells, suggesting a potential role of this gene in xenobiotic detoxification [25]."]
  The underlying data (the yeast uptake assay) could not be inspected.
- Herbicides and a safener induce ZmGT1 transcripts in leaves (semi-quantitative RT-PCR):
  [PMID:22792398 "While 2,4-D treatment had no influence on ZmGT1 expression, the other four compounds exhibited a significant inducing effect."]
- Rac- and S-metolachlor induce it to a similar degree:
  [PMID:23144728 "While no significant difference was found between rac- and S-metolachlor in increasing the transcript level of ZmGST27 and ZmGT1 (Fig. 1A and 1C)"]
- Both papers assert plasma-membrane localisation for glutathione transporters in general, citing
  other proteins. Neither paper tests ZmGT1 localisation. Both are expression studies only, with no
  loss-of-function or transport data on ZmGT1.

## Ortholog evidence: Arabidopsis OPT3

- AtOPT3 is a plasma-membrane transporter of transition-metal ions, located in the phloem:
  [PMID:24867923 "We found that OPT3 resided at the plasma membrane in oocytes, as shown by the localization of the OPT3-GFP–mediated fluorescence at the cell periphery"]
  [PMID:24880337 "OPT3 expression was found in the vasculature with preferential expression in the phloem at the plasma membrane."]
- AtOPT3 transports Fe2+ and Cd2+ in oocytes (PMID:24867923) and Cu in heterologous systems:
  [PMID:36814393 "We report that AtOPT3 also transports Cu in heterologous systems and contributes to its delivery from sources to sinks in planta."]
- AtOPT3 is not delivered to the yeast plasma membrane:
  [PMID:24880337 "When expressed in yeast, OPT3 does not localize to the plasma membrane, precluding the identification of the OPT3 substrate."]
  This makes it harder to interpret a yeast-based GSH uptake result for an OPT3-clade protein such as ZmGT1.

## Other OPT family members

- AtOPT6, a more distant paralog, supports GSH uptake in yeast:
  [PMID:15247401 "In addition to peptide transport, AtOPT6 is able to transport glutathione derivatives and metal complexes, and may be involved in stress resistance."]
- The fungal seed proteins of the PANTHER IBA (S. cerevisiae OPT1/OPT2, S. pombe Isp4 and
  SPBC29B5.02c, C. albicans and Aspergillus OPTs) are oligopeptide and glutathione transporters.

## Synthesis

ZmGT1 is an OPT-family transporter with 15 predicted transmembrane helices (Phobius), most likely located at the plasma membrane. OPT-family members are thought to be proton-coupled.
Its substrate is uncertain. The authors report GSH and GS-conjugate uptake in yeast (data not
inspectable), while its closest characterised ortholog, AtOPT3, transports Fe2+, Cd2+ and Cu.
