# TUNAR (pTUNAR / BNLN) review notes

UniProt A0A1B0GTB2 (TUNAR_HUMAN), 48 aa, Swiss-Prot reviewed. HGNC:44088 "TCL1 upstream
neural differentiation-associated RNA". The locus was long annotated as a lncRNA (TUNA,
HI-LNC78, LINC00617; zebrafish megamind). Mouse ortholog A0A1B0GQX2.

## Literature found (PubMed esearch "TUNAR micropeptide", "Tunar microprotein", "BNLN micropeptide")

Only two primary papers characterise the peptide:

1. PMID:34513312 Li et al. 2021 Mol Ther Nucleic Acids (full text cached). Human islets / rat INS-1 /
   mouse and human islets. Names the peptide BNLN.
2. PMID:35036403 Senis et al. 2021 Front Cell Dev Biol (full text cached, fetched this session).
   Mouse ESCs, N2A, cortical neurons, in utero electroporation. Names it pTUNAR. This is the
   paper behind the UniProt "By similarity" (A0A1B0GQX2) statements and the ISS rows.

Other TUNAR papers (e.g. PMID:33682459 TUNAR lncRNA and Wnt signalling in beta cells;
PMID:29540255 glioma paper, WITHDRAWN) treat TUNAR as an RNA and are not relevant to the
protein's GO annotation.

## Key findings

### Coding / structure
- [PMID:34513312 "BNLN contains a single-pass transmembrane domain"]; the TM domain is
  "extremely conserved and present in all 88 species".
- Senis: "pTUNAR is a transmembrane protein that localizes in the endoplasmic reticulum and
  interacts with the calcium transporter SERCA2" [PMID:35036403].
- Senis note no regulin xLFxxF motif and no similarity to DWORF [PMID:35036403 "pTUNAR's transmembrane domain does not contain the xLFxxF motif shared by all regulins"]. So TUNAR is NOT a regulin family member by sequence; SERCA regulation would be convergent.

### Localization
- Beta cells (INS-1, GFP-FLAG tags, KDEL-RFP co-stain): [PMID:34513312 "these data show that BNLN is primarily located at the ER of pancreatic β cells"], minor lysosome/mito/peroxisome/Golgi signal; not at cell surface (HiBiT).
- Mouse: co-localises with SERCA2 in brain and NIH3T3; also detected in small and large
  extracellular vesicles [PMID:35036403 "we could also detect pTUNAR in small and large extracellular vesicles"]. EV location is in UniProt (by similarity) but not in GOA; not proposed (single supplementary observation of an overexpressed tagged protein).

### SERCA interaction - direction of effect is DISCORDANT
- Beta cells: pull-down/MS found SERCA3 (ATP2A3, Q93084), confirmed by co-IP in HEK293 and PLA
  in INS-1; interaction increases with high glucose [PMID:34513312 "a low level of interaction between BNLN and SERCA3 occurred in low-glucose conditions (2.5 mmol/L), and this interaction was elevated in the presence of high glucose (17 mmol/L)"].
  Overexpression LOWERS ER Ca2+ and RAISES cytosolic Ca2+ -> authors suggest possible SERCA3
  inhibition but explicitly did not test enzyme activity [PMID:34513312 "whether this is primarily the result of reduction of SERCA3 enzyme activity requires further investigation"].
- Neurons (mouse): co-IP with SERCA2; overexpression INCREASES ER Ca store and speeds cytosolic
  Ca2+ clearance; KO opposite trend -> "possible role of pTUNAR as an activator of SERCA2"
  [PMID:35036403]. Also no direct ATPase assay, and they note PMCA as alternative.
- Senis explicitly reconcile as context-dependent: [PMID:35036403 "This is consistent with pTUNAR acting as a modulator of calcium dynamics via SERCA family proteins, which seems to be context and cell-type dependent."]

Conclusion: evidence supports SERCA binding (two isoforms, two labs, co-IP + PLA) and an effect
on ER/cytosolic Ca2+, but not a direction-specific MF (activator vs inhibitor). Unlike DWORF
(STRIT1: GO:0141109 transporter activator activity) and ERLN (GO:0042030 ATPase inhibitor
activity), there is no purified-system or pump-kinetics measurement. I therefore keep ATPase
binding (GO:0051117) as the core MF and do NOT propose GO:0042030/GO:0141109 or
GO:1901895/GO:1901896. GO:1901894 (direction-neutral regulation of ATPase-coupled calcium
transmembrane transporter activity) is plausible but also not directly measured; raised as a
question rather than NEW.

### Downstream physiology
- GSIS: overexpression increases GSIS in INS-1, mouse (lean and DIO) and human islets;
  ATG-deletion construct has no effect (peptide-dependent); shRNA knockdown of Tunar lowers GSIS
  in mouse islets [PMID:34513312 "suppression of BNLN decreased insulin secretion compared to control"]
  (note shRNA also removes the lncRNA). Downstream of Ca2+ handling -> non-core.
- ER stress: BNLN overexpression reduced high-glucose ATF6 reporter activation.
- Neural: start-codon-to-stop KO mESCs (lncRNA level unaffected) show enhanced neural
  differentiation in teratomas, EBs and neural protocol; overexpression reduces neurite number
  in N2A and cortex [PMID:35036403 "pTUNAR overexpression impairs neuronal differentiation by reduced neurite formation in different model systems"].
  Supports negative regulation of neuron differentiation (ISS, non-core). The ISS row
  "neuron projection morphogenesis" better captured as negative regulation of neuron projection
  development (GO:0010977); overexpression-only evidence.

## Annotation decisions (summary)
- ER / ER membrane (4 rows): ACCEPT.
- ER calcium ion homeostasis IDA: ACCEPT (core).
- regulation of cytosolic calcium ion concentration ISS: ACCEPT (direction-neutral; both labs).
- ATPase binding IPI (SERCA3) and ISS (SERCA2): ACCEPT (core MF, most defensible).
- positive regulation of insulin secretion involved in cellular response to glucose stimulus IDA: KEEP_AS_NON_CORE.
- negative regulation of neuron differentiation ISS: KEEP_AS_NON_CORE.
- neuron projection morphogenesis ISS: MODIFY -> GO:0010977.
- No NEW terms.
