# Ptk7 (mouse, Q8BKG3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of rat Ptk7
(A0A8I6ALM9). No ProtNLM2 file or prediction-evidence folder was opened; this review
uses only literature, UniProt and GOA.

### Deep research

`just deep-research-falcon mouse Ptk7 --fallback perplexity-lite` failed: falcon
returned "Exception: Failed to authenticate" (Edison JWT auth) and the perplexity-lite
fallback returned HTTP 401 (insufficient quota). No deep-research file exists for this
gene. The review is based on the cached primary literature listed below, which I read
directly (full text where `full_text_available: true`, otherwise abstract only).

### Evolutionary grounding

- UniProt places Q8BKG3 in PANTHER PTHR45080:SF21 (INACTIVE TYROSINE-PROTEIN KINASE 7),
  the same subfamily as human PTK7 (Q13308) and rat Ptk7; it is the one-to-one rodent and
  mammalian ortholog. Functions transferred from human, Xenopus or Drosophila (Otk) PTK7
  below are transfers within this orthologous lineage only; nothing is transferred from
  other members of PTHR45080 (contactins, L1-family, etc.).
- PAINT: human PTK7 carries IBA `GO:0005911 cell-cell junction` and
  `GO:0060828 regulation of canonical Wnt signaling pathway` from PTK7-specific node
  PTN000701324 (QuickGO, 2026-10-21). PAINT chose the direction-neutral "regulation" term
  rather than positive or negative regulation; I treat that as a deliberate decision,
  consistent with the conflicting literature (Puppo 2011 positive; Peradziryi 2011 and
  Berger 2017 inhibitory). The deeper node PTN002895063 (L1cam/contactin-like donors)
  gives human axon/neuronal cell body/synapse terms; those are not PTK7-subfamily functions.
  Mouse Ptk7 currently carries no IBA rows at all.
- The kinase-homology domain (788-1058) carries ALG in place of the DFG motif
  (sequence `...RQVKVSALGLSKDVY...` in the mouse sequence), as stated for PTK7 by
  Andreeva et al. [PMID:24703874 "predicted to lack endogenous kinase activity because the
  invariant 'DFG' motif essential for correct positioning of ATP is replaced with 'ALG'"].

### Mouse experimental findings (species-specific)

- Catalytically dead: [PMID:15019986 "Mouse PTK7 was shown to be phosphorylated neither by
  itself nor by other protein tyrosine kinases. In addition, its expression did not affect
  the phospho-tyrosine level of cellular proteins in COS-1 cells."]
- PCP regulator, genetic interaction with Vangl2 [PMID:15229603 "disrupts neural tube
  closure and stereociliary bundle orientation, and shows genetic interactions with a
  mutation in the mouse Van Gogh homologue vangl2"].
- Convergent extension in mesoderm [PMID:19439496 "In embryos mutant for PTK7, ... the
  normal cell elongation and alignment upon leaving the primitive streak, the subsequent
  polarized protrusive activity, and CE and axial elongation all failed"].
- chuzhoi allele: craniorachischisis, CE defect, OHC orientation, heart & lung defects,
  genetic interaction with Vangl2 Lp and Celsr1 Crsh; Ptk7 protein in cell membranes
  [PMID:20704721].
- Auditory epithelium mechanism: Ptk7 not required for Dvl2 membrane recruitment, acts in
  parallel to and opposes Fz3/Fz6, required in supporting cells, regulates apical myosin II
  [PMID:22560610].
- PTK7-Src module: PTK7 binds Src, promotes junctional active Src and ROCK2 localization;
  SFK activity required for auditory PCP in vivo; murine PTK7 cDNA localizes to cell-cell
  contacts in MDCK cells and requires its cytoplasmic domain [PMID:24703874].
- Wolffian duct CE-like elongation requires Ptk7 (conditional mesoderm deletion)
  [PMID:26944093]; HSC pool/homing defects [PMID:27183644]; wound repair defect in null
  embryos [PMID:20643356].
- Canonical Wnt: Ptk7-/- MEFs show weakened Wnt3a-induced TOPflash and more ubiquitinated
  beta-catenin [PMID:21132015], but Xenopus/Drosophila data show inhibition
  [PMID:21772251, PMID:28420671]. Direction is context dependent.

### Transferred (non-mouse) mechanistic findings, same orthologous lineage

- Wnt binding / Fz7 co-receptor (Xenopus, Drosophila Otk, reporter cells)
  [PMID:21772251, PMID:28420671]; RACK1-PKCdelta1-Dsh membrane recruitment (Xenopus)
  [PMID:21350015]; ROR2 heterodimer and WNT5A interaction in mammalian cells
  [PMID:26499793]; MT1-MMP shedding (human/zebrafish) [PMID:20837484].
- Note the mouse auditory data [PMID:22560610] argue that Dsh membrane recruitment by Ptk7
  is not universal in mammalian epithelia; I therefore did not propose Wnt-PCP pathway or
  Wnt-binding terms as NEW for mouse.

### Decisions summary

- Core: establishment of planar polarity, convergent extension, neural tube closure
  (all acts_upstream_of_or_within, mouse IMP/IGI); plasma membrane and cell-cell junction.
- NOT kinase / NOT RTK / NOT ATP binding / NOT protein phosphorylation: accepted.
- Organ phenotypes (heart, ventricular septum, coronary vasculature, kidney, lung
  mesenchyme, cochlea, wound healing): kept as non-core.
- Positive regulation of canonical Wnt (ISO/IEA from human): MODIFY to the neutral
  GO:0060828, matching the PAINT choice.
- Cellular response to retinoic acid (ISO/IEA from an SH-SY5Y RNAi screen in which RA was
  the differentiation stimulus): REMOVE; positive regulation of neuron projection
  development from the same screen: over-annotated.
- Cytosol (ISO; the human source row is no longer present in human GOA): over-annotated.
- Apical/basal polarity (IMP, Lu 2004, abstract-only): UNDECIDED; the abstract frames PTK7
  as a PCP regulator distinct from apical-basal polarity, but full text not seen.
