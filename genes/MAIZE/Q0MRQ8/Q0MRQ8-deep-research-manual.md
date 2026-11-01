# Q0MRQ8 (ZmrbohA) - manual literature research

No deep-research provider was available; this summary was compiled manually from cached
publications (publications/PMID_*.md) and PubMed searches (October 2026).

## Identity

- UniProtKB Q0MRQ8 (TrEMBL, unreviewed), 852 aa, "Respiratory burst oxidase protein A",
  EMBL DQ855284 (ABH85405.1), submitted by Lin F. and Jiang M. (2006); NCBI GeneID 778438;
  RefSeq NP_001105930.1; PeroxiBase 5488 (ZmRboh03).
- The maize literature calls this gene ZmrbohA. Lin et al. 2009 cloned it:
  "The ZmrbohA cDNA sequence was 3604 bp in length and had an ORF of 2559 nucleotides,
  encoding a protein of 852 amino acids" [PMID:19592501], matching the 852-aa length of
  Q0MRQ8. Zhang et al. 2010 used ZmrbohA primers designed against "GenBank accession no.
  DQ855284" [PMID:20693409], the EMBL accession of Q0MRQ8.

## Family and domains

- InterPro: Cyt_b245_heavy_chain (IPR000778), NADPH_Ox N-terminal region (IPR013623),
  EF-hand (IPR002048, PROSITE PS50222 at 179-214, EF_HAND_1 PS00018), ferric reductase TM
  domain (IPR013130), FAD-binding FR-type (PS51384, 536-664), NAD-binding (IPR013121);
  PANTHER PTHR11972 (NADPH oxidase) / SF54 (RBOH J-related). Phobius predicts
  transmembrane helices (302-320, 481-502, 670-687). PIRSR predicts four heme-iron axial
  histidines (383, 397, 486, 499).
- Phylogeny: "The fourth major cluster consists of the newly identified ZmrbohA and the
  four proteins of unknown function AtrbohH, AtrbohJ, OsrbohD, and OsrbohE"
  [PMID:19592501]. ZmrbohA is most similar to rice OsrbohE.
- The ZmrbohA, C and D sequences carry the gp91phox features: "Likewise, TMD3 and TMD5
  contained pairs of histidine residues that are important for haem binding in human
  gp91phox" [PMID:19592501].

## Clade IV orthologs (Arabidopsis RbohH/RbohJ)

- Kaya et al. 2014: "Both RbohH and RbohJ, which contain Ca(2+) binding EF-hand motifs,
  possessed Ca(2+)-induced ROS-producing activity and localized at the plasma membrane of
  the pollen tube tip" [PMID:24610725]. EF-hand point mutants lost Ca2+-induced ROS
  production. The rbohH rbohJ double mutant has impaired pollen tube tip growth.
- Further Arabidopsis papers (abstract-only cache): PMID:24506280 (pollen tube NAD(P)H
  oxidases dampen growth-rate oscillations), PMID:25751652 (apoplastic ROS production upon
  pollination by RbohH and RbohJ).
- General: plant RBOHs are plasma membrane NADPH oxidases producing superoxide
  [PMID:11756663]; AtrbohD is activated synergistically by Ca2+ binding to its EF-hands and
  by phosphorylation [PMID:18218618].

## Maize experimental data on ZmrbohA

- Expression only. ABA induces a biphasic increase in ZmrbohA-D transcripts in maize leaves;
  "The expression of ZmrbohA in phase I and ZmrbohC in phase II induced by ABA was slight"
  [PMID:19592501]. The phase II induction requires H2O2 and MAPK activity. Plasma membrane
  NADPH oxidase activity was measured in bulk leaf plasma membranes, not attributed to
  ZmrbohA.
- Brassinosteroid: "BR treatment significantly elevated the expression of ZmrbohA–ZmrbohD
  in leaves of maize plants" [PMID:20693409]. Late induction (120 min) is abolished by DPI,
  catalase and MAPKK inhibitors; ZmMPK5 is required for the H2O2 self-propagation loop. The
  BR-induced antioxidant defence (SOD, APX, CAT, GR) is downstream of apoplastic H2O2 and is
  carried out by antioxidant enzymes, not by the NADPH oxidase.
- No protein-level biochemistry, localization or mutant for ZmrbohA itself was found.
- PMID:41484844 (2026) reports a flowering-time GWAS candidate Zm00001d042961 encoding an
  "RBOHH" respiratory burst oxidase homolog; whether this locus is ZmrbohA could not be
  confirmed (no accession mapping available), so it is not used.

## Conclusions

ZmrbohA is a clade IV plant RBOH (H/J/OsrbohE group) with the complete gp91phox catalytic
architecture; its activity (superoxide-generating NADPH oxidase) and plasma membrane
location are inferred from domain architecture and the Arabidopsis RbohH/J orthologs. The
InterPro2GO peroxidase mapping (and the derived oxidant detoxification process) is wrong for
this family.
