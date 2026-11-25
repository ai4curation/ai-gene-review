# MAPK14 (p38 alpha, Q16539) curation notes

## Identity and core biochemistry

- MAPK14 encodes p38 alpha (SAPK2a, CSBP), a CMGC-group, proline-directed Ser/Thr MAP kinase.
  First identified as the target of pyridinyl-imidazole cytokine-suppressive anti-inflammatory
  drugs [PMID:7997261 "the target of these compounds was identified as a pair of closely related
  mitogen-activated protein kinase homologues, termed CSBPs"].
- Activation by dual phosphorylation of the TGY motif [PMID:7535770 "The mechanism of p38
  activation is mediated by dual phosphorylation on Thr-180 and Tyr-182."], by MKK3/MKK6
  (MAP2K3/MAP2K6) and, atypically, TAB1-driven autophosphorylation [file:human/MAPK14/MAPK14-uniprot.txt
  "Activation occurs through dual phosphorylation of Thr-180 and Tyr-182 by either of two dual
  specificity kinases, MAP2K3/MKK3 or MAP2K6/MKK6"].
- Located in both cytoplasm and nucleus [PMID:7535770 "Immunofluorescence microscopy demonstrated
  that p38 MAP kinase is present in both the nucleus and cytoplasm of activated cells."].
- Rhea reactions for serine and threonine phosphorylation are curated (EC 2.7.11.24) from
  PMID:11010976 and PMID:35857590.

## Direct substrates / output modules (MF: MAP kinase activity)

- Kinase substrates: MK2/MK3 (MAPKAPK2/3), MSK1/2 (RPS6KA5/4), MNK1/2, MK5/PRAK. The p38alpha-MK2
  heterodimer crystal structure shows the MK2 C-terminal regulatory region in the p38 docking groove
  [PMID:17255097 "The C-terminal regulatory domain of MK2 binds in the docking groove of p38alpha"].
  MSK2/RSK-B is a p38alpha substrate [PMID:9792677 "RSK-B is a p38alphaMAPK substrate, and activated by
  p38alphaMAPK and, more weakly, by ERK1."].
- Transcription factors: MEF2A/C via D-domain docking [PMID:10330143 "the MADS-box transcription
  factors MEF2A and MEF2C are preferentially phosphorylated and activated by the p38 subfamily members
  p38alpha and p38beta2"]; USF1 Thr153 [PMID:11532965 "Usf-1 is phosphorylated and activated by the
  stress-responsive p38 kinase"]; ATF2, CREB (via MSK).
- RNA regulators: TIAR during DNA-damage checkpoint maintenance [PMID:20932473 "we did observe strong
  direct phosphorylation of TIAR by p38 in vitro"].
- Innate immunity: NLRP1 disordered linker in the ZAKalpha ribotoxic stress response [PMID:35857590
  "Both p38α and p38β could phosphorylate recombinant NLRP1DR, including residues within the ZAKα motifs"].
- Rb Ser567 [PMID:20871633 "p38 bypasses the cell cycle-associated hierarchical phosphorylation and
  directly phosphorylates Rb on Ser567"].

## Negative regulators (phosphatases)

- DUSP1, DUSP10/MKP-5, DUSP16, DUSP9/MKP-4, PTPRR/PTP-SL, PPM1D/WIP1, PPM1A. MKP-5 prefers p38
  [PMID:10391943 "MKP-5 binds to p38 and SAPK/JNK, but not to MAPK/ERK, and inactivates p38 and
  SAPK/JNK, but not MAPK/ERK."]. DUSP9 KIM-dependent binding [PMID:21908610].
  PTP-SL KIM binding [PMID:10601328]. LZAP/CDK5RAP3 recruits WIP1 [PMID:21283629 "Expression of LZAP
  increased both LZAP and Wip1 binding to p38."].

## Protein-binding (GO:0005515) policy used

- 85 IPI rows. Partners were resolved from WITH/FROM via UniProt REST.
  - Kinases (MAPKAPK2, MAPKAPK3, RPS6KA4, RPS6KA5, MKNK1, MKNK2, MAPK3, CSNK1D) -> MODIFY to
    GO:0019901 protein kinase binding (same choice as MAPK1 review).
  - MAP2K3, MAP2K6 -> MODIFY to GO:0031434 mitogen-activated protein kinase kinase binding.
  - DUSP1, DUSP7, DUSP9, DUSP16, PTPRR, PPM1A -> MODIFY to GO:0019903 protein phosphatase binding.
  - Non-enzyme partners (ZFP36L1, SUPT20H/p38IP, ZNHIT1/p18Hamlet, RB1, EEF1A1, TSC1, MIDEAS, FBXW7,
    CDK5RAP3/LZAP) -> REMOVE (uninformative; interaction not disputed). Substrate relationships
    (Rb, p18Hamlet) are better captured as has_input on the kinase activity.

## Process annotations: core vs pleiotropic

- Core: p38MAPK cascade (GO:0038066), stress-activated MAPK cascade (GO:0051403), MAPK cascade,
  intracellular signal transduction.
- Non-core (well supported, downstream): myogenic differentiation (MEF2; mouse ISS), senescence
  and DNA-damage signalling [PMID:20160708 "serial signalling through GADD45-MAPK14(p38MAPK)-GRB2-TGFBR2-TGFbeta"],
  erythroid differentiation [PMID:23483889 "Knockdown of p38α resulted in dramatically reduced erythroid
  differentiation induced by araC, while knockdown of p38β had no effect"], UV-B response, LPS
  response, IL-12 and inflammatory cytokine production.
- Over-annotation: single-context inhibitor (SB203580) outcomes such as positive regulation of
  cyclase activity (CD38 expression in astrocytes, PMID:22027397), cellular response to virus
  (dengue/Gal-9, PMID:25754930), response to lipoteichoic acid (PMID:26649771), generic positive
  regulation of gene expression; Reactome neutrophil-degranulation compartments (extracellular
  region, secretory granule lumen, ficolin-1-rich granule lumen) for a cytosolic kinase.
- MAP kinase kinase activity (GO:0004708) TAS from PMID:10706854 is wrong: the eosinophil
  study measures p38 activation and uses inhibitors; p38 is a MAPK, not a MAPKK -> REMOVE.
- NOT positive regulation of blood vessel endothelial cell migration (PMID:18440775) is supported
  by the abstract: p38alpha siRNA "had no significant effect on the chemotactic response to VEGF".
- GO:0048273 (MAPK p38 binding) on MAPK14 itself with RSKB/MSK2 as partner describes the
  partner's function; the MAPK14-side function is protein kinase binding -> MODIFY.

## Isoform caveats

- Mxi2 (Q16539-3) binds ERK1/2 and promotes their nuclear import [PMID:17255949]; Exip and Mxi2 have
  divergent C-termini and reduced substrate affinity [PMID:10838079]. No GOA rows are isoform-tagged.
- Many functional studies use SB203580/SB202190, which inhibit p38alpha and p38beta; process
  claims from these are not strictly MAPK14-specific
  [file:human/MAPK14/MAPK14-deep-research-falcon.md].
