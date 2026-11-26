# WRKY70 (At3g56400, Q9LY00) curation notes

## 2026-10-15: genome-wide WRKY70 binding at SA-biosynthesis, PR and senescence promoters (DAP-seq)

Open question: is WRKY70 a direct transcriptional regulator of SA biosynthesis genes
(especially ICS1/SID2, At1g74710) and of PR genes, as opposed to senescence genes?
The question matters because a module on an open PR models a WRKY70 -| SA-biosynthesis
feedback edge. The literature disagrees on direction:

- Wang et al. 2006 found ICS1 and SA elevated in wrky54 wrky70 [PMID:17096590 "Hyperaccumulation of the ICS1 transcript and SA observed in these mutants (Figure 6) suggests that in WT plants, SA biosynthesis is actively repressed by low levels of WRKY70 and WRKY54"].
- Saleh et al. 2015 proposed WRKY70 as a repressor at PR1 together with non-sumoylated NPR1 [PMID:26269953 "at resting state, NPR1 is phosphorylated at Ser55/Ser59, which inhibits sumoylation and promotes interaction with WRKY70 to repress PR1 transcription"].
- Li et al. 2004 placed WRKY70 downstream of NPR1 as an SA-pathway activator [PMID:14742872 "Epistasis analysis suggested that WRKY70 is downstream of NPR1 in an SA-dependent signal pathway"].

Analysis: genes/ARATH/WRKY70/WRKY70-bioinformatics/ (reproducible; `just all`). Full
results and limitations are in [file:ARATH/WRKY70/WRKY70-bioinformatics/RESULTS.md].

Data: the O'Malley et al. 2016 Plant Cistrome DAP-seq peaks for WRKY70 (dataset
`WRKY_tnt/WRKY70_col`; 8,244 peaks; the MEME motif is a W-box), plus 37 other WRKY DAP-seq
datasets for comparison. DAP-seq is in vitro [PMID:27203113 "uses in-vitro-expressed TF to interrogate naked gDNA fragments to establish binding locations (peaks) and sequence motifs"].
No in vivo WRKY70 ChIP-seq was analysed.

Result (2 kb upstream window, robust to a -3 kb/+0.5 kb window):

- **No WRKY70 peak at ICS1/SID2.** The nearest WRKY70 summit is about 11 kb away. Twelve
  of the 37 other WRKY DAP-seq datasets do bind the ICS1 promoter window.
- **No WRKY70 peak at PR1, PR2, ICS2, PBS3 or PAD4.** The PR1 promoter has 3 WT-box
  (YGACTTTT) motifs and is bound by 11 other WRKY datasets, but not by WRKY70.
- **WRKY70 peaks at EDS5, CBP60G, SARD1 and PR5.** These are promoter peaks. There are also
  peaks just downstream of the TSS at NPR1 (+126) and EDS1 (+75). The EDS5 and CBP60G
  sites are bound by most WRKY datasets (31 and 29 of 37), so they are not WRKY70-selective.
- **No WRKY70 peak at the senescence markers.** This covers SAG12, SAG13, SEN1 and ORE1.
  Leaf-senescence genes are not enriched.
- **The control gene ACT2 has a WRKY70 peak.**
- **Weak, non-specific enrichment in SA-response genes.** WRKY70 promoter targets are
  modestly enriched among GO "response to salicylic acid" genes (OR 1.66, p = 7.3e-3,
  uncorrected) and "defense response" genes. WRKY33 DAP-seq shows the same enrichment, so
  it is a generic WRKY/W-box property and not WRKY70-specific.

Interpretation:

- The in vitro binding data do not support a direct WRKY70 -| ICS1 promoter edge. The ICS1
  de-repression in wrky54 wrky70 may be indirect, or may depend on partners, chromatin or
  modification states that DAP-seq lacks.
- The data say nothing about activator versus repressor direction.
- A missing DAP-seq peak does not exclude in vivo occupancy.

Curation consequence:

- **No GO annotation changes.** A suggested question and a suggested experiment were added
  to the review, asking for WRKY70 ChIP-qPCR/ChIP-seq at ICS1 and PR1 under SA and
  pathogen conditions, with wrky54 wrky70 and the NPR1 sumoylation mutants as context.
- **For the open module PR:** the WRKY70 -| SA-biosynthesis edge should be treated as
  genetic (indirect) unless in vivo binding at ICS1 is shown.
