# vwc2 (brorin) notes

ZFIN vwc2 (ZDB-GENE-090313-315, chromosome 13; synonym brorin, si:dkey-4j1.1); NCBI Gene 798521;
Ensembl ENSDARG00000076495; UniProt B0I1T8 (309 aa). PANTHER (PTHR46252) pairs it with
si:dkey-283b1.7 as a TGD_tree 1:1 pair, with human ortholog VWC2 (LDO). The separate brorin-like gene
vwc2l (ZDB-GENE-081104-169) is the VWC2L ortholog and is not part of this pair. Reviewed as part of
DANRE_DUPLICATION batch 3 (random sample).

## Deep research

Deep research was not available for this batch (Edison returned 402 Payment Required, and the
OpenAI key is invalid). I searched Europe PMC myself for "vwc2 AND zebrafish",
"brorin AND zebrafish" and "si:dkey-283b1.7".

## Literature

- **Miyake et al. 2017 (PMID:28448525)**, the only functional study of zebrafish vwc2.
  - Identity: [PMID:28448525 "Zebrafish Brorin is presumed to be a secreted protein composed of 309 amino acids with a putative 22-amino acid signaling sequence at its amino-terminus (Fig 1A)."]
  - Synteny with mouse: [PMID:28448525 "Zebrafish brorin is closely linked to the ikzf1 and fingl1 genes on chromosome 13, while mouse Brorin is closely linked to the Ikzf1 and Fingl1 genes at A2 on chromosome 2 (Fig 1B)."]
  - Expression: [PMID:28448525 "At 36 hpf, brorin expression was detected in the ventral telencephalon, prethalamic/alar hypothalamic region, olfactory placode, hindbrain, and spinal cord (Fig 2H and 2I and data not shown)."]
  - BMP antagonism in vivo: [PMID:28448525 "These results indicate that the overexpression of brorin leads to the inactivation of Bmp signaling."] and [PMID:28448525 "These results indicate that Brorin inhibits Bmp signaling, but not canonical Wnt signaling."]
  - Forebrain phenotypes (two splice MOs, mRNA rescue): [PMID:28448525 "These results indicate that brorin is required for the development of the subpallial telencephalon."] and [PMID:28448525 "We found that the co-injection of brorin RNA with brorin MO1 prevented the development of brain defects caused by brorin MO1 (n = 11/12) (Fig 3G)."]
  - vwc2 and vwc2l overlap partly: [PMID:28448525 "However, brorin and brorin-like may in part function redundantly during forebrain development."]
  - si:dkey-283b1.7 is not mentioned anywhere in the paper.
- **Miwa et al. 2009 (PMID:19852960)**, abstract only. The paper is about Brorin-like (vwc2l):
  [PMID:19852960 "The inhibition of Brorin-like functions in zebrafish resulted in the impairment of neural development."]
  The 2017 paper says the earlier work reported the brorin-like knockdown, and that the role of
  Brorin itself had not been elucidated:
  [PMID:28448525 "However, the role of Brorin in early neural development has not yet been elucidated."]
  ZFIN's IMP (nervous system development) on vwc2 from this paper has no morpholino in WITH/FROM,
  while vwc2l carries two morpholinos from the same paper (QuickGO, 2026-09-28). I marked it UNDECIDED
  rather than REMOVE, because the full text is not available.
- Mouse background: Brorin is secreted and inhibits BMP2/6
  [PMID:17400546 "The protein inhibited the activity of bone morphogenetic protein 2 (BMP2) and BMP6 in mouse preosteoblastic MC3T3-E1 cells."].
  It is a Noelin-recruited extracellular constituent of AMPA receptor complexes:
  [PMID:37591201 "Brorin and Brorin-like have been consistently retrieved in previous anti-GluA APs"]

## Analyses (file:DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/RESULTS.md)

- The brorin MOs are vwc2-specific (0 mismatches). They have 8-10 mismatches to si:dkey-283b1.7 and vwc2l.
- The vwc2 core is 83.6% identical to human VWC2 and 89.3% to gar vwc2. The partner si:dkey-283b1.7 is
  only 32.6% identical to vwc2 over the full length.
- Bgee: vwc2 has brain-dominated calls; si:dkey-283b1.7 has calls in retina and brain.

## Decisions

- BMP negative regulation (IBA), extracellular (IBA, IEA), forebrain development (IMP): ACCEPT.
- AMPAR complex (IBA) and synapse (IEA): KEEP_AS_NON_CORE.
- Nervous system development (IMP, PMID:19852960): UNDECIDED.
