# Map2k2 (mouse, Q63932) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon mouse Map2k2 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and perplexity-lite returned HTTP 401 (insufficient quota). No deep-research
file exists; the review is built from cached publications, the UniProt record and a local sequence comparison.

### Evolutionary grounding
- UniProt Q63932 is in PANTHER PTHR47448:SF3 (MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2), the same
  subfamily as human MAP2K2 P36507; MAP2K1 (human Q02750, mouse P31938) is in PTHR47448:SF2
  (interpro/panther/PTHR47448/PTHR47448-entries.csv).
- IBA rows (MAPK cascade, MAP kinase kinase activity) come from PAINT node PTN000684494, a deep MAP2K
  node; PAINT propagated only those two terms.
- `Map2k2-bioinformatics/compare_mek_sequences.py` (RESULTS.md): 94.3% identity to human MAP2K2,
  82.1% to human MAP2K1; K101, D194, S222, S226 conserved.

### Experimentally established in mouse
- MAP kinase kinase activity: recombinant mouse MEK2 phosphorylates kinase-inactive Erk-1 on Tyr and Thr; K101M inactive
  [PMID:8297798 "Recombinant MEK2 produced in bacteria phosphorylates a kinase-inactive Erk-1 on tyrosine and threonine, whereas a kinase-inactive mutant MEK2 does not."].
- ERK1/2 activation in cells and embryos; Mek1-Mek2 heterodimer with MEK1 Thr292 feedback
  [PMID:19219045 "Disabling this Erk-proximal negative-feedback step stabilizes the phosphorylation of both Mek2 and Erk in cultured cells and in vivo in Mek1 knockout embryos and mice."].
- KSR binding and membrane recruitment [PMID:10409742 "this results in the appearance of MEK in membrane-associated fractions"].
- Mek2-null mice normal [PMID:12832465 "Mek2 mutant mice are viable and fertile, and they do not present flagrant morphological alteration."];
  compound Mek1/Mek2 mutants reveal requirements in placenta (PMID:19304888), neural crest (PMID:18952847),
  respiratory tract (PMID:25100655), PNS (PMID:21220101) and RAF-driven axon growth (PMID:24733831).
  These are acts-upstream organismal consequences of ERK signalling, kept non-core; no NEW process terms added.

### Inferred only (not shown for mouse MEK2)
KSR-dependent BRAF activation, PDZ (DLG1) binding, ER/Golgi/endosome/mitochondrion/focal adhesion/sperm
localizations, all from human or review/ARBA sources.

### Probable mis-attributions (left UNDECIDED, flagged in suggested_questions)
- Myelination and Schwann cell development IMP rows cite PMID:10704452 (erbB2) and PMID:18760695 (Nrg1/ErbB);
  WITH/FROM gives Erbb2, Erbb3 and Nrg1 alleles, and the cached full texts never mention MEK/Mek2.
- ERBB2-ERBB3 signaling IDA cites PMID:24493648, which uses Mek1DD (Map2k1); Mek2 is never mentioned.
