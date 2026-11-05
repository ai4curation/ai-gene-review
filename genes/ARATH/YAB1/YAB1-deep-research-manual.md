# YAB1 / FILAMENTOUS FLOWER (FIL), Arabidopsis thaliana (O22152, At2g45190) - manual literature synthesis

No deep-research API was available for this review; this summary was compiled manually from the
cached publications in `publications/` and PubMed searches. All claims carry inline provenance.

## Identity and domain architecture

- FIL (also AFO, YAB1) is a 229-aa YABBY-family protein with an N-terminal C2C2 (CH2C6) zinc finger
  and a C-terminal YABBY (HMG-box-like) domain [PMID:10323860 "FIL encodes a protein carrying a zinc finger and a HMG box-like domain, which is known to work as a transcription regulator"].
- The zinc finger binds two Zn(2+) ions; loss of one zinc promotes self-assembly into multimers
  [PMID:11092895 "Zinc determination experiments revealed that the FILAMENTOUS FLOWER protein binds two zinc ions per molecule"].
- PANTHER family PTHR31675 (PROTEIN YABBY 6-RELATED); FIL belongs to the YAB1 (FIL/YAB3) clade.

## Molecular function: DNA-binding transcription factor

- Nuclear protein [PMID:10323860 "As expected, the FIL protein was shown to have a nuclear location."].
- Early gel-shift experiments with recombinant FIL detected DNA binding without sequence
  specificity, requiring the HMG-like YABBY domain [PMID:11812777 "Gel retardation experiments showed that the FILAMENTOUS FLOWER protein binds to DNA without sequence specificity."].
- Later work defined FIL binding elements (FBEs; from protein-binding microarray data of Franco-Zorrilla
  et al. 2014) and showed sequence-specific EMSA binding of MBP-FIL to an FBE in the MYB75/PAP1 promoter,
  with FIL activating a pMYB75:LUC reporter [PMID:26530088 "MBP-FIL was able to specifically bind to the probe containing the FBE1"; "these results support the idea that FIL is a direct transcriptional activator of MYB75"].
- FIL acts as a transcriptional activator in yeast and in planta transactivation assays, and a
  FIL-SRDX obligate repressor gives yab loss-of-function phenotypes; inducible FIL-GR transcriptomics
  identified both up- and down-regulated targets (KAN1, ARF4, AS1 up) [PMID:23025792 "Collectively these data show that FIL functions as a transcriptional activator in plants and that this activity is involved in leaf patterning."].
- FIL also interacts with the LEUNIG/LEUNIG_HOMOLOG co-repressors and SEUSS/SLK adaptors, which is
  the basis of its repressive output [PMID:19837869 "we show that YABs physically interact with components of a transcriptional repressor complex that include LEUNIG (LUG), LEUNIG_HOMOLOG (LUH), the LUG-associated coregulator SEUSS, and related SEUSS-LIKE proteins"].
- JAZ3 binds FIL and attenuates its transactivation; JA-triggered JAZ3 degradation releases FIL to
  activate MYB75 and anthocyanin accumulation [PMID:26530088 "JAZ3 directly interacts with YAB transcription factors, attenuating their transactivation function and consequently repressing anthocyanin biosynthesis."].
- Yeast one-hybrid: FIL bound promoters of the HD-ZIPIII genes PHB, PHV and REV in a vascular TF-promoter
  network screen [PMID:31806676, GOA IPI row; cached text is abstract-level only].
- Other interactors from yeast two-hybrid screens: SPL/NOZZLE [PMID:15299139], TCP10, TCP15, IDD14,
  ZFP3, KAN1 [PMID:28650476], ERF8, JAZ3/TIFY6B [PMID:32612234].

## Biological roles (genetic evidence)

- Abaxial cell fate: FIL, YAB2, YAB3 are expressed abaxially in all lateral organ primordia; ectopic FIL
  is sufficient to specify ectopic abaxial tissue [PMID:10457020 "Ectopic expression of either FILAMENTOUS FLOWER or YABBY3 is sufficient to specify the development of ectopic abaxial tissues in lateral organs."].
- Flower and inflorescence formation: fil mutants form flowerless filamentous structures, altered
  floral organ number/position and altered AG/AP3/PI/SUP domains [PMID:10331982; PMID:9878633].
- KNOX repression in leaves: fil yab3 mutants derepress STM, BP and KNAT2 and form ectopic meristems
  [PMID:12417699].
- Non-cell-autonomous regulation of the SAM and phyllotaxis via LAS-mediated signals [PMID:18469164
  "We show that peripheral YAB1 activity nonautonomously and sequentially affects the phyllotaxis and growth of subsequent primordia"].
- LUG-YAB complex promotes leaf polarity, embryonic SAM initiation and SAM maintenance [PMID:19837869].
- fil-9 enlarges inflorescence and floral meristems and disrupts floral organ number/identity [PMID:20584289].
- Fruit patterning: FIL and YAB3, redundantly with JAG, activate FUL and SHP in valves/valve margins
  [PMID:16192305 "FIL and YAB3 activate FUL and SHP redundantly with JAGGED (JAG)"]; JAG/FIL activity
  and BP/RPL mutually repress each other along the mediolateral axis of the fruit
  [PMID:23133401 "Therefore, all the results presented so far indicate that JAG/FIL activity represses BP, which in turn, negatively regulates the JAG/FIL activity genes."].
