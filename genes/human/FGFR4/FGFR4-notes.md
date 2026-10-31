# FGFR4 (P22455) curation notes

## 2026-09-30 initial review (claude-code)

### Identity and architecture
- Single-pass type I receptor tyrosine kinase; three Ig-like domains, TM, split tyrosine kinase domain (UniProt P22455).
- Unlike FGFR1-3, FGFR4 has no IIIb/IIIc alternative exon pair; its D3 is a single c-type-like configuration
  [file:human/FGFR4/FGFR4-deep-research-falcon.md "Unlike FGFR1–3, FGFR4 has one principal IgIII configuration rather than alternatively spliced b/c isoforms"].
  (Machine-generated summary; consistent with UniProt listing only isoform 1 and a soluble isoform 2.)
- Isoform 2 (P22455-2) is a soluble/secreted form (UniProt SUBCELLULAR LOCATION [Isoform 2]: Secreted) -> basis of IEA extracellular region.

### Molecular function
- FGF receptor tyrosine kinase: binds canonical FGFs with heparan sulfate (Ornitz 1996 BaF3 mitogenic panel)
  [PMID:8663044 "To determine potentially relevant ligand-receptor pairs we have engineered mitogenically responsive cell lines expressing the major splice variants of all the known FGF receptors."].
- Autophosphorylation of activation-loop tyrosines (Tyr642/643) [PMID:18670643 "This site is phosphorylated in response to ligand binding and is essential for FGF receptor activity"].
- Endocrine FGF19: FGFR4-selective ligand [PMID:10525310 "FGF-19 is a high affinity, heparin dependent ligand for FGFR4 and is the first member of the FGF family to show exclusive binding to FGFR4."];
  requires beta-Klotho (KLB) coreceptor [PMID:17627937 "KLB is required for FGF19 binding to FGFR4, intracellular signaling, and downstream modulation of gene expression."];
  at physiological pM concentrations also requires sulfated GAGs [PMID:21653700 "Here we report that hFGF19 at picomolar levels require sulfated glycosaminoglycans (sGAGs), such as heparan sulfate, heparin, and chondroitin sulfates, for its signaling via human FGFR4 in the presence of human betaKlotho."].
- FGF19 vs FGF21: both bind KLB-FGFR4 but only FGF19 signals efficiently [PMID:17623664 "We conclude that FGF21 can strongly bind to but cannot signal effectively through the β Klotho-FGFR4 complex."].
- FGF19 residues 38-42 confer FGFR4 activation / hepatocyte proliferation [PMID:20018895 "only FGF19 activates FGFR4, the predominant receptor in the liver"].

### Physiological process: bile acid synthesis (core)
- Enterohepatic FXR -> FGF15/19 -> hepatic KLB-FGFR4 -> ERK -> CYP7A1 repression.
  [PMID:12815072 "a secreted growth factor that signals through the FGFR4 cell-surface receptor tyrosine kinase"]
  [PMID:17623664 "Thus, the genetic evidence strongly suggests that FGF15/19, FGFR4, and β Klotho are essential components in the negative regulation of bile acid synthesis."]
  [PMID:19085950 "siRNA knockdown of FGFR4 (siFGFR4) reduced FGFR4 protein and mRNA expression in HepG2 cells (Fig. 6B and Fig. 6C), and resulted in 50% reduction of GW4064-mediated repression of CYP7A1 mRNA expression compared to control siRNA (Fig. 6D)"]
  [PMID:20683963 "Only the terminal FGFR4 glycoform is phosphorylated upon FGF19 treatment of HepG2 cells, and this shows that only fully glycosylated FGFR4 is active in CYP7A1 down-regulation."]
- Direction is NEGATIVE regulation of bile acid biosynthesis (GO:0070858); GOA carries the parent GO:0070857.
  FGFR4 is the signal-transducing kinase that does the work (not a substrate), so the participation test is satisfied; KLB review also uses GO:0070858.

### Trafficking: recycling vs degradation (module relevance)
- Deep research summary: FGFR4 preferentially recycles (Rab11) after FGF1 stimulation, while FGFR1-3 go to lysosomes
  [file:human/FGFR4/FGFR4-deep-research-falcon.md "This recycling route, mediated by Rab11, returns FGFR4 to the plasma membrane and is associated with sustained signaling"].
- BUT the primary paper in the cache shows ligand-induced degradation of wild-type-like FGFR4-Gly388 in 293T cells, with Arg388 much more stable
  [PMID:18670643 "Thus, the FGFR-4 Arg 388 variant is degraded much more slowly than the Gly 388 variant after ligand binding."],
  and MT1-MMP drives FGFR4-G388 degradation [PMID:20798051 "the overexpression of MT1-MMP and particularly its phosphorylation-defective mutant vice versa induced FGFR4-G388 degradation"].
- Conclusion: "recycles rather than being degraded" is a relative statement (FGFR4 recycles more than FGFR1-3 in the FGF1-uptake assays);
  FGFR4 is still subject to ligand- and partner-dependent degradation, allele-dependent. UniProt: "FGFR4 signaling is down-regulated by receptor internalization and degradation".
- The primary recycling paper (Haugsten et al. 2005) is not cached here; I could not reach PubMed eutils from this container to look up its PMID, so it is not cited.

### Biosynthesis / glycosylation
- KLB (ER-resident per Triantis) binds core-glycosylated FGFR4 and sends it to proteasome
  [PMID:20683963 "beta-Klotho binds and directs the core glycoform of FGFR4 to the proteasome, and it allows only a terminal glycoform to reach the plasma membrane."].
- Immature FGFR4 at Golgi, ligand-independent STAT1 phosphorylation there [PMID:17311277 "FGF-independent activation of STAT1 was demonstrated at the Golgi apparatus where it was colocalized with FGFRs."].

### Cancer / variant biology (non-core)
- G388R (rs351855) risk allele: increased stability, sustained activation, MT1-MMP stabilisation, invasion [PMID:20798051, PMID:20876804, PMID:18670643].
- FGF19-FGFR4 drives hepatocyte proliferation/HCC [PMID:20018895].

### Annotation issues found
- GO:0010628 positive regulation of gene expression (IMP, PMID:19085950): the only FGFR4 perturbation in that paper shows FGFR4 is needed for
  REPRESSION of CYP7A1 -> MODIFY to GO:0010629 negative regulation of gene expression.
- NOT GO:1903412 response to bile acid (IMP, PMID:19085950): paper shows CDCA increases FGFR4 tyrosine phosphorylation and FGFR4 siRNA blunts FXR-agonist
  repression of CYP7A1; the only negative observation is unchanged total FGFR4 protein. Negation not supported -> REMOVE (flag for curator).
- PMID:18061161 (FGFRL1 paper) IDA to FGFR4 for PM/Golgi/transport vesicle; abstract only mentions FGFRL1. Per rules: do not REMOVE.
  PM ACCEPT; Golgi KEEP_AS_NON_CORE (independently supported by PMID:17311277); transport vesicle UNDECIDED.
- PMID:18480409 (FGFR1 ubiquitination) IDA for FGFR4 FGFR activity / FGF binding / heparin binding / signaling. Abstract only (PMC full text not retrievable);
  UniProt cites this paper for FGFR4 catalytic activity and ubiquitination, so FGFR4 was presumably assayed in the full text. Functions are clearly correct -> ACCEPT.
- 6 generic protein binding IPIs -> REMOVE (uninformative; interactions KLB, MMP14, FGFR1, RET, SDC2, TGFBR3 not denied).
