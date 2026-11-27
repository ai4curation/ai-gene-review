# NUC1 notes

## 2026-09-30

- Reviewed budding yeast `NUC1` as the EndoG-like fungal nuclease comparator
  for the APOPTOSIS project. The central activity is a mitochondrial
  metal-dependent DNA/RNA nuclease: purified yeast Nuc1 has ssRNA RNase,
  DNA endonuclease, and 5-prime exonuclease activities, and NUC1 disruption
  removes all detectable mitochondrial DNase and most nonspecific
  mitochondrial RNase activity [PMID:3286639, "all detectable DNase activity
  and most nonspecific RNase activity in the mitochondria is due to this single
  enzyme"].
- Kept all mitochondrial inner-membrane and broader mitochondrial localization
  rows, using the original biochemical inner-membrane localization and UniProt
  as direct support even where individual GOA rows came from high-throughput
  mitochondrial proteome papers [PMID:3286639, "in the mitochondrial inner
  membrane"].
- Accepted `GO:0006915 apoptotic process` and `GO:0006309 apoptotic DNA
  fragmentation` for the fungal EndoG branch. Buttner et al. showed that Nuc1p
  can induce yeast apoptosis with a pathway requiring mitochondrial pore
  opening, Kap123p-dependent nuclear import, and H2B/chromatin association
  [PMID:17244531, "Nuc1p induces apoptosis in yeast"]. Eastwood et al. defined
  gametogenic programmed nuclear destruction with apoptotic-like DNA
  fragmentation [PMID:22727375, "PND is executed through apoptotic-like DNA
  fragmentation"], and the later Gao et al. full text explicitly states that
  meiotic nuclear DNA laddering requires NUC1 [PMID:31266891, "where their DNA
  is fragmented into nucleosomal ladders in a manner requiring NUC1"].
- Accepted the meiotic cytosolic and antiviral rows from Gao et al.: a fraction
  of Nuc1-FLAG accumulates in cytosolic fractions during sporulation, and
  released Nuc1 attenuates cytosolic L-A/Killer dsRNA mycoviruses through
  nuclease-dependent genetics [PMID:31266891, "attenuating the cytosolic L-A
  and Killer double-stranded RNA mycoviruses"].
- Modified the new 2026 `mitophagy` and `regulation of mitochondrial DNA
  metabolic process` rows to `GO:0032043 mitochondrial DNA catabolic process`.
  The Cupo, Dominguez-Martin, and Youle abstract supports Nuc1 degrading mtDNA
  bound for mitophagy-linked escape through the vacuole, but Nuc1 is not the
  Atg11/Atg32 mitophagy machinery itself [PMID:41638207, "suggest a direct role
  of Nuc1 in degrading mtDNA bound for escape"].
- Accepted the older `DNA recombination` row because the nuc1 mutant directly
  reduces mitochondrial recombination and gene conversion, consistent with the
  purified enzyme's 5-prime exonuclease activity [PMID:8087883,
  "Mitochondrial DNA recombination was reduced in an yeast mutant lacking the
  NUC1 endo/exonuclease"].
