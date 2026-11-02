# GstO2 (Drosophila melanogaster) - manual literature review

No deep-research API provider was available for this session; this file records a manual
literature survey (PubMed search `(GstO2 OR GSTO2 OR DmGSTO1 OR CG6673) AND Drosophila`, 11 hits,
plus the GOA-cited references). Quotes are from cached `publications/PMID_*.md` files.

## Identity and nomenclature

- FlyBase FBgn0035906, CG6673, GeneID 38974. Omega-class cytosolic GST.
- The gene encodes two alternatively spliced isoforms, A and B, which differ in their N-terminal
  first exon including the active-site motif. UniProt Q9VSL5 ("isoform A") has the motif
  C31-P-F-S (`...SMAFCPFSHR...`); Q9VSL4 ("isoform B") has C-P-Y-S, identical to human GSTO2.
- Naming is inconsistent in the literature: Kim et al. 2006/2012 call CG6673 "DmGSTO1" (A and B
  isoforms) [PMID:22219196 "CG6673 is also called D. melanogaster GSTO1 (DmGSTO1) and has the
  highest thiol transferase and DHA reductase activity among the GSTO genes"]; Saisawang et al.
  2012 (universal nomenclature) and later papers use GstO2 / DmGSTO2a / DmGSTO2b
  [PMID:24533905 "In Drosophila, GstO2 exists as two isoforms, GstO2A and GstO2B."].

## Enzymatic activities

- Recombinant CG6673A and CG6673B have thiol transferase and dehydroascorbate (DHA) reductase
  activity, low CDNB-conjugating activity, and no pyrimidodiazepine (PDA) synthase activity
  [PMID:16712527 "All cloned and expressed candidates exhibited relatively high thiol transferase
  and dehydroascorbate reductase activities and low activity towards 1-chloro-2,4-dinitrobenzene,
  characteristic of Omega class GSTs, whereas only CG6781 catalysed the synthesis of PDA"].
- Isoform B has much higher DHAR activity than isoform A [PMID:22219196 "We have shown that
  DmGSTO1B has much higher DHAR activity than DmGSTO1A in vitro"].
- Kinetic parameters for DHA reduction by both isoforms; optimum pH 8.0, 40 C; native ~60 kDa
  (dimer) [PMID:24533905 abstract, full text not available].
- The cytosolic GST proteome survey (Saisawang 2012) expressed all fly GSTs and measured
  activity with several substrates [PMID:22082028 abstract only].
- Neither GstO2a nor GstO2b alters p38b MAP kinase activity in vitro [PMID:25373207 "both
  DmGSTO2a and DmGSTO2b appeared not to interact with p38b for either ATF2 or Jun"].

## In vivo roles

- Null allele (imprecise P excision) is viable and fertile; DHAR activity drops to ~5% of wild
  type; flies are paraquat sensitive, rescued better by isoform B, which also restores the
  ascorbate/DHA ratio [PMID:22219196 "These results indicate that DmGSTO1B has a protective role
  in response to paraquat-induced stress and plays an important role in the in vivo conversion
  of DHA to AsA."].
- Isoform A (not B, not the C31A active-site mutant) increases glutathionylation of the
  mitochondrial F1F0-ATP synthase beta subunit, and does so directly in vitro
  [PMID:22219196 "We also confirmed that DmGSTO1A can directly glutathionylate the ATP synthase
  β subunit in a dose-dependent manner in the presence of GSH"]; this restores ATP synthase
  activity/assembly and suppresses parkin mutant phenotypes.
- Isoform A expression is reduced in PINK1 mutants and its overexpression suppresses PINK1
  phenotypes [PMID:23867819 abstract].
- Overexpression suppresses neurotoxicity in fly models of TDP-43, TAF15 and FUS proteinopathy
  [PMID:32674363; PMID:36411469; PMID:35320731]. In the FUS model GstO2 is reported to act by
  deglutathionylating FUS Cys447 [PMID:35320731 "GstO2 reduced cytoplasmic FUS aggregation by
  deglutathionylation in Drosophila brains."] (abstract only).
- A genome-wide in vivo RNAi screen for survival after oral Serratia marcescens infection is the
  source of the two HMP immune annotations; GstO2 is not discussed in the main text
  [PMID:19520911].

## Localization

- FlyBase IDA annotations to cytosol and mitochondrion cite PMID:24533905 (full text not cached).
  A mitochondrial pool is consistent with the ATP synthase beta target of isoform A.
