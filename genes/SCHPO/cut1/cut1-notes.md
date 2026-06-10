# cut1 (separase / Separin) — S. pombe — review notes

UniProt: P18296 (CUT1_SCHPO), 1828 aa, EC 3.4.22.49. PomBase SPCC5E4.04.
Domains: Peptidase C50 (1647-1741), SEPARIN core domain; active site Cys1730.
PANTHER PTHR12792 (EXTRA SPINDLE POLES 1-RELATED), subfamily SF0 SEPARIN.

## Core biology

Cut1 is the fission-yeast separase (ESP1/separin ortholog), a large CD-clan
cysteine endopeptidase that triggers anaphase sister-chromatid separation by
cleaving the cohesin kleisin subunit Rad21, opening the cohesin ring. Held
inactive before anaphase by its bound inhibitory chaperone securin (Cut2);
APC/C-Slp1-mediated degradation of Cut2 at the metaphase-anaphase transition
liberates active Cut1. "cut" = cell untimely torn — chromosomes fail to
segregate but septation proceeds.

## Evidence by reference

- UniProt FUNCTION: "Caspase-like protease, which plays a central role in the
  chromosome segregation by cleaving the rad21 subunit of the cohesin complex at
  the onset of anaphase. During most of the cell cycle, it is inactivated by
  securin/cut2 protein. It is also required for pointed nuclear formation."
  EC 3.4.22.49. ACT_SITE Cys1730.

- [PMID:8978688 "Fission yeast Schizosaccharomyces pombe temperature-sensitive (ts)
  cut1 mutants fail to separate sister chromatids in anaphase but the cells
  continue to divide, leading to bisection of the undivided nucleus (the cut
  phenotype)."] — establishes mitotic sister chromatid separation role (cut1 ts).
  [PMID:8978688 "Cut1 protein concentrates along the short spindle in metaphase as
  does Cut2."] — spindle localization (IDA C:mitotic spindle).
  [PMID:8978688 "Cut1 (approximately 200 kDa) and Cut2 (42 kDa) associate, as shown
  by immunoprecipitation, and co-sediment as large complexes (30 and 40S)..."] —
  separase-securin (Cut1-Cut2) complex (IPI/IDA C:separase-securin complex);
  also UniProt SUBUNIT "Interacts with cut2. Interacts with rad21."

- [PMID:9635190 "Cut1 is retained in the cytoplasm during interphase and moves to
  the mitotic spindle pole bodies and the spindle upon entry into prophase, when
  spindles are formed."] — SPB and spindle localization (IDA C:mitotic spindle
  pole body; C:nucleus on the spindle). [PMID:9635190 "Cut2 is required for
  loading Cut1 onto the spindle at prophase and Cut2 proteolysis is needed for the
  active participation of Cut1 in sister chromatid separation."] Also notes Cut1
  "remains bound to the anaphase spindle" -> midzone localization in anaphase
  (IDA C:mitotic spindle midzone).

- [PMID:14532136 "Here we show that separase activation and resultant Rec8 cleavage
  are required for meiotic chromosome segregation in fission yeast."] and
  [PMID:14532136 "We identify two Cut1-dependent cleavage sites within Rec8
  sequences and demonstrate that the homologue segregation at meiosis I is
  completely blocked by the expression of a non-cleavable form of Rec8."] —
  meiotic chromosome separation; endopeptidase activity cleaving Rec8 (IMP
  F:endopeptidase activity; IMP/NAS P:meiotic chromosome separation).

- [PMID:15329725 "Experiments using either mutant cohesin that cannot be cleaved by
  separase or a protease-dead separase provide evidence that this DNA repair
  function of securin-separase acts through the cleavage of cohesin. We propose
  that the securin-separase complex might aid DNA repair by removing local cohesin
  in interphase cells."] — DNA damage response role via interphase cohesin
  cleavage (IMP P:DNA damage response). Non-core / secondary process.

- [PMID:12390246 "The pointed nuclear formation did not require the protease site
  of separase, but required the conserved C-terminus..."] and CONCLUSIONS
  "Overproduced separase C-fragment abolishes correct SPB-positioning in
  interphase." — TAS endopeptidase activity (the paper discusses separase
  protease) + a non-proteolytic C-terminal SPB-positioning role. UniProt
  MUTAGEN D1767A/E1779V affect pointed-nucleus formation.

- [PMID:1934126 "Single mutants in cut1 or cut2 did not effect sporulation, whereas
  the double mutant cut1 cut2 formed two-spored asci."] — basis for meiotic
  nuclear division IMP (PMID:1934126). Genetic, cut1 single mutant had no
  sporulation defect; phenotype only in cut1 cut2 double. Supports a meiotic role
  but indirect. KEEP_AS_NON_CORE.

- [PMID:8065367 "Two multicopy suppressor genes for cut8-563 are identified. They
  are the cut1+ gene essential for nuclear division..."] — cut1 as multicopy
  suppressor of cut8-563 anaphase block; basis for IMP mitotic sister chromatid
  separation (involvement in anaphase/nuclear division). Indirect (suppressor)
  but supports involvement in mitotic chromatid separation/anaphase.

- [PMID:16823372] ORFeome global localization (HDA C:cytosol). Consistent with
  interphase cytoplasmic pool of Cut1.

## Curation decisions summary

Core MF: cysteine-type endopeptidase activity (GO:0004197), separase.
Core BP: mitotic sister chromatid separation (GO:0051306).
Core CC: separase-securin complex (GO:1990520), nucleus, mitotic spindle.

- F:cysteine-type endopeptidase activity (GO:0004197) IBA & IEA -> ACCEPT (core MF).
- F:endopeptidase activity (GO:0004175) TAS & IMP -> ACCEPT but MF is more
  precisely cysteine-type endopeptidase / separase; these are parents. Keep TAS as
  ACCEPT (general parent ok), IMP from PMID:14532136 (Rec8 cleavage) ACCEPT.
  Consider MODIFY to GO:0004197. Will MODIFY the generic endopeptidase to
  cysteine-type endopeptidase (GO:0004197) where appropriate? Both are correct;
  GO:0004197 is the informative one. MODIFY GO:0004175 -> GO:0004197.
- C:nucleus, C:cytoplasm, C:cytosol — Cut1 is cytoplasmic in interphase, on
  spindle/nucleus in mitosis. ACCEPT localizations.
- C:mitotic spindle, mitotic spindle pole body, mitotic spindle midzone — ACCEPT (IDA).
- IEA nuclear division (GO:0000280), nuclear chromosome segregation (GO:0098813),
  proteolysis (GO:0006508) — ACCEPT as correct but general; chromosome
  segregation is core, proteolysis is core process parent.
- P:mitotic sister chromatid separation (GO:0051306) NAS & IMP -> ACCEPT (core).
- P:meiotic chromosome separation (GO:0051307) NAS & IMP -> KEEP_AS_NON_CORE
  (real but secondary to mitotic role).
- P:meiotic nuclear division (GO:0140013) IMP PMID:1934126 -> KEEP_AS_NON_CORE.
- P:DNA damage response (GO:0006974) IMP -> KEEP_AS_NON_CORE.
