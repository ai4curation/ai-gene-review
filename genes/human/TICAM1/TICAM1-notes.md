# TICAM1 (TRIF) review notes

Human TICAM1, UniProt Q8IUC6, 712 aa. Also called TRIF (TIR domain-containing adapter
inducing IFN-beta) and TICAM-1. Reviewed as part of the INNATE_IMMUNITY project, batch 1
(Toll/TLR axis).

## Deep research status

The review was drafted from the UniProt record and cached publications before Falcon deep
research finished. `TICAM1-deep-research-falcon.md` (review-based: Hu 2024, Chen 2021 and
others, no PMIDs) arrived later and agrees with every decision here. It describes TICAM1 as
a scaffold "without itself possessing enzymatic activity". It also stresses the
RHIM-dependent apoptosis and necroptosis branches (RIPK1-FADD-caspase-8; RIPK3-MLKL, which
can bypass RIPK1). Its sources are reviews, so I did not use them for NEW annotations; they
back the cell-death suggested question.

## Identity and domain architecture (UniProt Q8IUC6)

- TRIF-NTD (1-153), globular, IFIT-like fold (PMID:24311583, per UniProt; not cached).
- TRAF6-binding motifs at 84-91, 248-255, 299-309.
- pLxIS motif 207-210; Ser210 phosphorylated by TBK1; phospho-pLxIS recruits IRF3.
- TIR domain 393-553: homotypic engagement of TLR3 and of TICAM2 (TRAM) for TLR4.
- C-terminal RHIM region (512-712 "sufficient to induce apoptosis"), engages RIPK1/RIPK3.

## Molecular function: signaling adaptor

- Discovery: "TRIF associated with TLR3 and IFN regulatory factor 3." and "Furthermore,
  TRIF, but neither MyD88 nor TIRAP, activated the IFN-beta promoter." [PMID:12471095]
- Independent discovery as TICAM-1: "that can physically bind the TIR domain of TLR3 and
  activate the IFN-beta promoter in response to poly(I):poly(C)." [PMID:12539043]
- Recruits TRAF6 via motifs: "TNF receptor-associated factor (TRAF)6 interacted with TRIF
  through the TRAF domain of TRAF6 and TRAF6-binding motifs found in the N-terminal portion
  of TRIF." and TBK1 "also associated with the N-terminal region of TRIF." [PMID:14530355]
- "In conclusion, TRIF recruits TRAF6-TAK1-TAB2 to TLR3 through its TRAF6-binding site,
  which is required for NF-κB but not IRF3 activation." [PMID:14982987] (full text, human
  293 cells).
- NF-kB branch vs IRF branch are separable: "TRIF induced NF-kappaB activation through an
  IKKbeta- and tumor necrosis factor receptor-associated factor-6-dependent (but not TBK1-
  and IKKepsilon-dependent) pathway." [PMID:14739303]
- IRF3 licensing: "We further show that TRIF, an adaptor protein in Toll-like receptor
  signaling, activates IRF3 through a similar phosphorylation-dependent mechanism."
  [PMID:25636800]; structural basis "The adaptor proteins STING, MAVS, and TRIF recruit
  IRF-3 through their phosphorylated p L x IS motifs." [PMID:27302953]
- Recruitment of TRIF to TLR3/TLR4 assisted by WDFY1: "WDFY1 interacts with TLR3 and TLR4
  and mediates the recruitment of TRIF to these receptors." [PMID:25736436]
- Downstream partners: "TRIF contains multiple conserved domains that are responsible for
  further association with downstream molecules receptor-interacting protein 1 (RIP1),
  TRAF6, and TANK-binding kinase 1 (TBK1)." [PMID:25736436]

Conclusion: GO:0035591 signaling adaptor activity is the right MF (IBA-supported, PAINT node
PTN002932982 shared with TICAM2). GO:0060090 molecular adaptor activity rows should be
refined to it. No TICAM1-specific catalytic activity is known.

## Processes

- TLR3 pathway: core. [PMID:12471095, PMID:12539043, PMID:14982987]
- TLR4 pathway: TRIF-dependent arm from endosome, bridged by TICAM2/TRAM. "Here, we show that
  TRAM recruits TRIF to the plasma membrane." and "These results suggest that TLR4 activates
  TRIF-signaling in endosome/lysosome after relocation from the cell surface."
  [PMID:18222170]
- TLR5: mouse intestinal epithelium TRIF-KO data; "Although our data show that TRIF
  participates in TLR5-induced responses, we could not see IRF-3 activation in intestinal
  epithelial cells by flagellin stimulation." [PMID:20855887]. Not in GOA; left as question.
- Apoptosis/necroptosis via RHIM-RIPK1/RIPK3: "In addition, TRIF also induced apoptosis
  through a RIP/FADD/caspase-8-dependent and mitochondrion-independent pathway."
  [PMID:14739303] (overexpression). Reactome models RIP3:TRIF necroptosis. No GOA row for
  a cell-death process; I did not add NEW (evidence in human is overexpression-based and the
  physiologic role is mostly from mouse); flagged as a question.
- Positive regulation of type I IFN production and of canonical NF-kB: core, consistent.
- Negative regulators act on TRIF (SARM1 [PMID:16964262], TRIM8 [PMID:28747347], FOSL1
  [PMID:28049150], TRIM38 per UniProt). These are regulatory inputs; they explain several of
  the IPI rows but are not TICAM1 functions.

## Localization

- Diffuse cytoplasmic at rest, forms speckles upon dsRNA; transient colocalization with TLR3
  [PMID:17982077].
- Endosome/endosome membrane in the TLR4-TRAM route [PMID:18222170] and Reactome.
- Autophagosome: via UBQLN1 (UniProt; PMID:21695056 not cached) and TAX1BP1-mediated
  selective autophagy (PMID:28898289 per UniProt); reflects TICAM1 turnover.
- Mitochondrion: "By similarity" to mouse multi-helicase (DDX1-DDX21-DHX36) complex in mDCs;
  a single mouse study; kept as non-core.

## IPI protein binding rows (13)

Partners from GOA WITH column: TRAF6 (14982987, 25736436), TNFAIP3/A20 (15142865), TBK1
(15841462, 19416887, 21903422, 25736436), TRIM56 (22948160), TLR3, RIPK1, TICAM2 (25736436),
CARM1 (33961781), TLR4 (36232715). Decision: MODIFY to GO:0035591 where the paper shows
TICAM1 bridging a receptor to a downstream effector (14982987 TRAF6; 25736436 TLR3/TRAF6/
RIPK1/TBK1/TICAM2); REMOVE as uninformative where the interaction is with a regulator acting
on TICAM1 or from screens (A20, TRIM56, CARM1, HCV/ISG56 papers, network map). TLR4 binding
(36232715): GO:0035325 Toll-like receptor binding exists, but the PAUF paper uses the
TRIF-TLR4 co-IP only as a readout ("However, rPAUF did not affect the binding of TRIF to
TLR4 (Figure 6B)." [PMID:36232715]), so REMOVE as uninformative.

## Action summary

120 rows: ACCEPT 91, MODIFY 8 (molecular adaptor activity x2 and protein binding x6 ->
signaling adaptor activity), REMOVE 7 (protein binding), KEEP_AS_NON_CORE 13,
MARK_AS_OVER_ANNOTATED 1 (cell surface receptor signaling pathway). No NEW annotations.

## Project questions

- TIR-domain propagation: TICAM1 IEA from InterPro TIR gives only signal transduction /
  innate immune response - no receptor or NADase term leaks onto TICAM1. Good.
- GO:0035666 TRIF-dependent TLR signaling is named after this gene; IBA, ISS, IMP all agree.
- GO:0007166 cell surface receptor signaling pathway (ARBA) is not an ancestor of GO:0002224
  (checked OLS); TICAM1 signals mainly from endosomes; marked over-annotated.
