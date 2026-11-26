# hemE (P29680, Escherichia coli K-12) curation notes

## Sources and deep research

- Deep research was unavailable: `just deep-research ECOLI hemE --provider perplexity`
  failed (missing template in this sparse checkout; provider API access not available).
  This review is based on the UniProt record, the cached GOA-cited publications, and the
  comparator reviews genes/PSEPK/hemE and genes/ECOLI/hemN.
- UniProt P29680 annotation is HAMAP-rule based (MF_00218); no E. coli enzymology is cited
  there. The experimental evidence on the E. coli gene is genetic.

## Evidence

- Sasarman et al. 1975 isolated the first E. coli UROD-deficient mutant SASQ85; extracts make
  uroporphyrinogen but not copro-/protoporphyrinogen [PMID:1104578 "Cell-free extracts of SASQ85
  were able to convert 5-aminolevulinic acid and porphobilinogen to uroporphyrinogen, but not to
  copro- or protoporphyrinogen."]. The mutant is catalase deficient [PMID:1104578 "The mutant,
  designated SASQ85, was catalase deficient and formed dwarf colonies on usual media."].
- Pido et al. 1994: hemA/hemE double mutant 10L2-1 had no UROD activity and was complemented by
  Synechococcus hemE [PMID:7849561 "accumulated uroporphyrin and had no uroporphyrinogen
  decarboxylase activity"]; HemE is the first committed step to heme rather than siroheme
  [PMID:7849561 "Uroporphyrinogen III decarboxylase is the first enzyme at the branch point which
  commits to heme synthesis."].
- Cytosol: proteomics of E. coli fractions [PMID:15911532; PMID:18304323]; per-protein tables not cached.

## Decisions

- GO:0006780 uroporphyrinogen III biosynthetic process (EcoliWiki IMP, PMID:1104578): REMOVE.
  The paper shows uroporphyrinogen synthesis is intact in the mutant; HemE acts downstream.
  Recorded as a source defect.
- Porphyrin-containing compound metabolic/biosynthetic rows: MODIFY to GO:0006785 heme B
  biosynthetic process, matching PSEPK/hemE and ECOLI/hemN.
- GO:0006783 heme biosynthetic process rows: ACCEPT (shared trunk enzyme; product feeds heme b and
  hemes o/d made from it).
