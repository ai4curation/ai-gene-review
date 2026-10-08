# NUDT2 (P50583) review notes

## Summary of evidence

- Human asymmetrical Ap4A hydrolase, Nudix (MutT motif) family; cDNA cloned 1995; unrelated
  to prokaryotic/fungal Ap4A-degrading enzymes (the symmetrical ApaH type).
  [PMID:7487923 "It is unrelated to the enzymes of diadenosine tetraphosphate catabolism found in prokaryotes and fungi."]
- NMR structures, free and ATP-bound; asymmetric cleavage of Ap4A to ATP + AMP.
  [PMID:15596429 "cleaving the metabolite diadenosine tetraphosphate (Ap(4)A) back into ATP and AMP"]
- Loss of function raises Ap4A ~175-fold in KBM-7 cells and changes thousands of transcripts
  (interferon/inflammation genes down, MHC II up).
  [PMID:27144453 "causing a 175-fold increase in intracellular Ap4A"]
- Mast-cell signalling: NUDT2 degrades LysRS-produced Ap4A after FcepsilonRI activation;
  knockdown alters MITF/USF2 target genes (Ap4A releases MITF/USF2 from HINT1).
  [PMID:18644867 "The knockdown of Ap(4)A hydrolase modulated Ap(4)A accumulation, resulting in changes in the expression of MITF and USF2 target genes."]
- RNA 5'-end activity: recombinant NUDT2 sequentially removes phosphates from 5'-PPP RNA,
  enabling XRN1 decay; E58A inactive; NUDT2 KO cells/MEFs support more growth of PPP-RNA
  viruses (VSV, IAV) but not HSV-1/SFV; Nudt2-/- mice viable, no VSV survival difference.
  [PMID:34824277 "NUDT2 sequentially releases two phosphates, and a monophosphorylated RNA is generated that can then serve as a substrate for the cellular exonuclease XRN1."]
- Localisation: nucleus and cytoplasm in human cells.
  [PMID:34824277 "In human cells, NUDT2 localizes to both the nucleus and the cytoplasm"]
- Non-canonical cap removal in vitro: FAD and dpCoA caps (not NAD); no FAD-cap change in KO cells.
  [PMID:32432673 "Whereas Nudt2 possesses deFADding activity on FAD-capped RNAs in vitro (Figure 4), it does not hydrolyze NAD-capped RNA (Figure 1)."]
  Ap4A-capped RNA is cleaved by NUDT2 and DXO.
  [PMID:37934413 "A decapping enzyme screen identifies two enzymes cleaving Ap4 A-RNA,NUDT2 and DXO"]
- Disease: biallelic loss-of-function variants cause IDDPN (ID +/- peripheral neuropathy);
  18 patients/10 families; variants lose activity; add-back of a decapping-defective
  enzyme implicates decapping loss in altered mRNA homeostasis.
  [PMID:38141063 "add-back experiments using an Ap4A hydrolase defective in mRNA decapping highlighted loss of NUDT2 decapping as the activity implicated in altered mRNA homeostasis"]
  [PMID:33058507 "A homozygous frameshift variant c.186delA (p.A63Qfs*3) in the NUDT2 gene"]
  [PMID:38243213 "Bi-allelic loss of function variants in NUDT2 has recently been reported as a rare cause of intellectual disability (ID)."]
- Cancer: overexpressed in breast carcinoma, promotes proliferation; reported to bind Rag
  GTPases and promote mTORC1 lysosomal recruitment (single lab, abstract only).
  [PMID:20533549 "NUDT2 promotes proliferation of breast carcinoma cells"]
  [PMID:28089905 "NUDT2 binds to Rag GTPase and controls mTORC1 translocation to the lysosomal membrane."]
- PRPP pyrophosphatase: weak in vitro (kcat 0.057 s-1); not annotated in human GOA and not proposed.
  [PMID:12370170 "the human diadenosine tetraphosphate hydrolase, and human DIPP-1"]

## Curation decisions (consistent with genes/worm/ndx-4)

- GO:0004081 asymmetrical tetraphosphatase (IBA, IEA, 2x ISS, Reactome TAS): ACCEPT.
- GO:0008803 symmetrical tetraphosphatase TAS (PMID:7487923): MODIFY to GO:0004081; the cited
  paper itself says the human enzyme is unrelated to the prokaryotic (symmetrical) enzymes.
- AMP/ATP biosynthetic process IBA (PTN000482012, seeded only by ndx-4): MARK_AS_OVER_ANNOTATED,
  product-based inference (same call as ndx-4).
- Apoptotic process ISS (from ndx-4 TAS, PMID:11937063): REMOVE (worm source TAS removed).
- Mitochondrial matrix TAS (Reactome): REMOVE; Reactome compartment artefact, data show nucleus/cytoplasm.
- Cellular response to oxidative stress TAS (Reactome ROS detox pathway): REMOVE; pathway is SOD/catalase/peroxidase.
- Nucleobase-containing compound metabolic process TAS: MODIFY to GO:0015967.
- Hydrolase activity IEA: MODIFY to GO:0004081. GO:0008796 IEA: ACCEPT.
- Protein binding IPI x3 (HuRI/Y2H: MCM6, DDIT4L, PLEKHF2): REMOVE (uninformative).
- NEW: GO:0015967 (IMP, PMID:27144453), GO:0140818 (IDA, PMID:34824277), GO:0110154 RNA decapping
  (IMP, PMID:38141063), GO:0005634 and GO:0005737 (IDA, PMID:34824277).
- Not proposed: defense response to virus (in vitro/cellular effect only; no in vivo phenotype;
  flagged as a question), mTORC1 regulation (single lab, mechanism unclear), PRPP pyrophosphatase.

## PAINT (PTHR21340) observations

- PTN000482012 carries GO:0004081 (seeds: pig NUDT2, P. falciparum C0H4F3, ndx-4) - sound.
- PTN000482012 AMP biosynthetic (GO:0006167) and ATP biosynthetic (GO:0006754) IBDs are seeded only
  by worm ndx-4 IDA rows that are product-based; GO:0015967 diadenosine tetraphosphate catabolic
  process would be the better node assertion and is absent.
- No CC asserted at the node; human and fly data support nucleus/cytoplasm.

## Caveats

Abstract-only caches: PMID:7487923, 15596429, 18644867, 38141063, 37934413, 28089905, 27431290,
20533549, 12370170, 11738085, 11937063. PMID:30059600 (founder nonsense variant) could not be cached.

## Deep research status

See section below (appended when the OpenScientist run completes).
