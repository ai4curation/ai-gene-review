# SPRED1 (human, Q7Z699) curation notes

## 2026-10-01 initial review (claude-code)

Context: reviewed as a negative regulator of Ras-ERK signalling (Sprouty/SPRED feedback step for the ERK cascade module). Comparator: genes/human/SPRY4.

### Mechanism: NF1 recruitment is the best-supported activity
- Neurofibromin is required for SPRED1 inhibition, and SPRED1 brings NF1 to the plasma membrane [PMID:22751498 "Here we show that neurofibromin, the NF1 gene product, is a Spred1-interacting protein that is necessary for Spred1's inhibitory function."] [PMID:22751498 "We show that Spred1 binding induces the plasma membrane localization of NF1, which subsequently down-regulates Ras-GTP levels."]
- Domain logic: EVH1 binds NF1, SPR domain targets the membrane [PMID:22751498 "Together, these results underscore the importance of the EVH1 domain of Spred1 in inhibiting ERK activation, and the importance of the SPR domain in directing the plasma membrane localization of Spred1."]
- Acts at the level of Ras-GTP [PMID:22751498 "Depletion of Spred1 from the PC3 prostate cell line resulted in elevated levels of Ras-GTP following EGF stimulation."]
- Biochemistry: EVH1 binds the NF1 GRD GAPex region and does not change GAP activity [PMID:27313208 "Binding is compatible with simultaneous binding of Ras and does not interfere with GAP activity."]
- Structure of SPRED1 EVH1:NF1 GRD:KRAS [PMID:32697994 "This inhibition of RAS is thought to occur primarily through SPRED1 binding and recruitment of neurofibromin, a RasGAP, to the plasma membrane."]
- Legius mutations disrupt EVH1-GRD binding [PMID:26635368 "These data clearly demonstrate that SPRED1 inhibits the Ras-ERK pathway by recruiting neurofibromin to Ras through the EVH1-GRD interaction"]
- Older RAF model (discovery paper, mouse) [PMID:11493923 "Instead, Spred inhibited the activation of MAP kinase by suppressing phosphorylation and activation of Raf."] -- not supported by a direct RAF-binding/inhibition MF in later work; SPRED1 associates with B-RAF in the cytoplasm as a translocation step [PMID:33872193 "Additionally, SPRED1 associates with B-Raf in the cytoplasm, where B-Raf/C-Raf dimerization induces SPRED1 membrane translocation to the plasma membrane (Siljamäki and Abankwa 2016)."]
- Conclusion for the module: MF = GO:0043495 protein-membrane adaptor activity (NF1-to-membrane), not a kinase-inhibitor/RAF-binding MF (contrast SPRY4, whose core MF is GO:0004860 via RAF1). SPRED1 is the EVH1-containing paralog variant of the Sprouty feedback step.

### Secondary activities
- TESK1 inhibition in vitro [PMID:18216281 "From these results, we conclude that Spred1 inhibits TESK1 activity by binding to it, similar to Sprouty4."]
- DYRK1A modulation [PMID:20736167 "Both SPRED1 and SPRED2 inhibit the ability of DYRK1A to phosphorylate its substrates, Tau and STAT3."]
- KIT binding via KBD [PMID:33872193 "This screen identified SPRED1 as a binding partner for the intracellular kinase domain of c-Kit in its inactive state."]
- S-acylated by ZDHHC17 [PMID:24705354 "We confirmed that three of them, GPM6A, and the Sprouty domain-containing proteins SPRED1 and SPRED3, are indeed palmitoylated by HIP14"]

### Disease
- Legius syndrome [PMID:17704776 "We report germline loss-of-function mutations in SPRED1 in a newly identified autosomal dominant human disorder."]

### Decisions
- 452 GO:0005515 rows: REMOVE (HT Y2H screens, HuRI, PP1 screens, ZDHHC17 substrate). NF1 row (PMID:26635368) MODIFY -> GO:0032794; PP1 row (PMID:19389623) MODIFY -> GO:0008157.
- No NOT annotations in GOA for SPRED1.
- UNDECIDED: nucleus (EXP PMID:16115197 abstract-only, abstract silent on nucleus; IEA SubCell mirror), and positive regulation of p53 DNA-damage signalling (ISS/IEA from mouse; cited PMID:20736167 abstract has no p53 content).
- GO:0060979 vasculogenesis involved in coronary vascular morphogenesis (IMP, PMID:23625462): MODIFY -> GO:2001213 negative regulation of vasculogenesis (knockdown enhances tube formation [PMID:23625462 "Knocking down Spred1 phenocopies the functional effect seen for miR-1 upregulation."]).
- GO:0043408 regulation of MAPK cascade (TAS) MODIFY -> GO:0070373.
- NEW: GO:0043495 protein-membrane adaptor activity; GO:0046580 negative regulation of Ras protein signal transduction (comparators SPRY1/SPRY2/SPRY4 IBA and NF1 IEA carry it; SPRED1 is in separate PANTHER family PTHR11202).
- Deep research (falcon) agrees: [file:human/SPRED1/SPRED1-deep-research-falcon.md "SPRED1 therefore has no catalytic reaction, enzyme substrate specificity or transport substrate of its own."]
