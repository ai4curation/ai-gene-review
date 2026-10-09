# HLA3 (Chlamydomonas reinhardtii) — curation notes

UniProt A0A2K3E226 (TrEMBL, unreviewed; ProtNLM name "ABC transporter, multidrug
resistance associated protein"); locus Cre02.g097800 (CHLRE_02g097800v5). Synonym
CrMRP1. 1325 aa.

## Deep research

- 2026-10-03: `scripts/deep_research_wrapper.py CHLRE HLA3 falcon --fallback perplexity-lite`
  failed. Falcon returned HTTP 402 Payment Required; the perplexity-lite fallback failed
  because the `perplexity` provider was not available in this environment. Not retried
  (per instructions). Notes below are from primary literature read directly from the
  `publications/` cache.

## Sequence / domain features (from HLA3-uniprot.txt, plus a quick motif check)

- Full-size ABCC/MRP architecture: TMD1 (166-384), NBD1 (418-639), TMD2 (711-1003),
  NBD2 (1062-1297); PANTHER PTHR24223:SF443 (ABCC subfamily), CDD ABC_6TM_ABCC_D1/D2 and
  ABCC_MRP_domain1/2; ~12+ predicted TM helices (Phobius). There is no N-terminal TMD0
  in InterPro/CDD, so it resembles the "short" MRPs (MRP4/5-like) rather than MRP1.
- Motif inspection of the UniProt sequence (done inline, not a deposited analysis):
  NBD1 Walker A `GRIAAGKS`, NBD1 Walker B `LVLLDN` (catalytic Glu replaced by Asn),
  NBD1 signature `FSGGQ` (canonical); NBD2 Walker A `GRTGSGKST`, NBD2 Walker B `ILCLDE`
  (canonical), NBD2 signature `SLGQ` (degenerate). This is the asymmetric
  one-consensus / one-degenerate ATP-site arrangement typical of ABCC proteins; the
  consensus site (NBD2 Walker A/B + NBD1 signature) is intact, so ATP binding and
  hydrolysis are expected.

## Expression and regulation

- Limiting-CO2 inducible; only one of seven Chlamydomonas MRP-type genes controlled by
  CIA5 [PMID:19321421 "Seven putative MRP-type ABC transporters have been identified in
  C. reinhardtii ( 11 ), but only CrMRP1 ( HLA3 ) expression is controlled by CIA5"].
- In the CIA5/CO2 RNA-seq study HLA3 falls in CCM cluster 15 with LCIA, LCI1 and CCP1
  [PMID:22634760 "includes essentially all the genes for which there is either compelling
  evidence for a C i transport role for the gene product in the CCM ( LCIA , LCI1 , and
  HLA3 )"].
- HLA3 mRNA is reduced in LCIA insertion mutants; LCIA is unaffected in the HLA3 mutant,
  suggesting a chloroplast-to-nucleus signal [PMID:26015566 "the absence of LCIA decreased
  HLA3 mRNA accumulation"].

## Localization

- Originally only predicted (WoLF PSORT) to be plasma membrane [PMID:19321421 "Although not
  demonstrated physically, HLA3 is predicted to be located in the plasma membrane"].
- Direct: anti-HLA3 immunofluorescence at the cell periphery and enrichment in purified
  plasma membrane fractions [PMID:26015566 "a notable enrichment of HLA3 was observed in the
  PM fraction"; "we concluded that HLA3 and LCIA were localized to the PM and CE,
  respectively"].
- Venus-tagged HLA3 at the plasma membrane in Chlamydomonas, and GFP-tagged HLA3 at the
  plasma membrane in tobacco leaf cells [PMID:26538195 "LCI1: Venus and HLA3: Venus were in
  the plasma membrane"].
- UniProt ARBA (ARBA00004128) and the GO:0005774 vacuolar membrane IEA are therefore
  contradicted by direct data (the rule is a family-level transfer from plant vacuolar
  ABCC/MRP glutathione-conjugate pumps).

## Function

- RNAi knockdown (2 constructs): HLA3 knockdown alone gives modest, high-pH-specific loss of
  Ci affinity and Ci uptake in very-low CO2; combined with LCIB mutation or off-target LCIA
  co-knockdown, dramatic loss of growth and Ci uptake at pH 9 [PMID:19321421 "compelling
  evidence that HLA3 is directly or indirectly involved in HCO 3 − transport"]. The authors
  explicitly leave open direct vs. indirect action [PMID:19321421 "Whether HLA3 is directly
  involved in HCO 3 − transport or indirectly facilitates the activity of other HCO 3 −
  transporters remains unclear"].
- dTALE activation of HLA3 in high-CO2 cells increased Ci accumulation and Ci-dependent O2
  evolution at very low CO2 [PMID:25660294 abstract: "confirms that HLA3 is indeed involved
  in Ci uptake, and suggests it is mainly associated with HCO3(-) transport"]. Abstract only
  in cache.
- Insertion mutant Hin-1 (complemented by Hin-1C): reduced Ci affinity at pH 9 and lower
  [14C]-Ci accumulation [PMID:26015566 "These results indicated that HLA3 has a meaningful
  role in HCO3– uptake in VLC conditions."]. HLA3/LCIA double mutant additive. Single HLA3
  overexpression in HC gave only a small Ci accumulation increase; co-overexpression with LCIA
  significantly raised Ci affinity/accumulation [PMID:26015566 "simultaneous overexpression
  of HLA3 with LCIA significantly increased Ci affinity/accumulation"].
- Heterologous: HLA3 (untagged or GFP-tagged) at the oocyte surface raised H14CO3- uptake
  2.7-fold over water-injected controls [PMID:26538195 "Oocytes transformed with mLCIA: GFP
  or HLA3: GFP accumulated 2.0‐ and 2.7‐fold more 14C than water‐injected controls"]. The
  authors caution the mode (active vs passive) is unresolved [PMID:26538195 "Further kinetic
  analyses will be required to determine the mode of action of these proteins (i.e. active
  vs. passive transport)"]. This is the most direct evidence that HLA3 itself moves
  bicarbonate across a membrane; no ATP-dependence, substrate specificity or purified
  protein data exist.
- Interactome: HLA3 co-purifies reciprocally with LCI1 and with the P-type ATPase ACA4,
  plus a CaM kinase and CYG63 cyclase as high-confidence interactors [PMID:28938113
  "Unexpectedly, we found that HLA3 and LCI1 are found together in a complex."]. Not a GO
  complex; recorded as a question only. Blue-native PAGE shows HLA3 in a ~580 kDa complex
  independent of LCIA [PMID:26015566].

## Curation decisions summary

- MF: GO:0015106 bicarbonate transmembrane transporter activity (NEW; oocyte uptake +
  in vivo genetics), keep IBA GO:0140359 ABC-type transporter activity; ATP binding and ATP
  hydrolysis IEA accepted (consensus ATP site intact).
- CC: GO:0005886 plasma membrane (NEW; IDA). REMOVE GO:0005774 vacuolar membrane (IEA, ARBA)
  — contradicted.
- BP: GO:0015701 bicarbonate transport (NEW); keep transmembrane transport IBA/IEA.
- Did not add a CCM-level or "response to CO2" process: induction by low CO2 is regulation of
  the gene, not activity of the product.
