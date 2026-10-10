# PGM2 / GAL5 (YMR105C, P37012) notes

## Activity
- Major phosphoglucomutase isozyme [UniProt:P37012 "Major phosphoglucomutase isozyme that catalyzes the"]; ~80-90% of cellular PGM activity [UniProt:P37012 "Constitutes about 80-90%"].
- Purification of the major isozyme (Fleischmann's yeast), Mg2+ (or Zn2+) dependent, ping-pong kinetics [PMID:1100398 "A procedure has been described for the purification of the major isozyme of yeast phosphoglucomutase of highest known specific activity."; "Enzyme exhibited \"ping-pong\" kinetics rather than \"random sequential\"."].
- Pgm2 strongly prefers Glc-1-P over Rib-1-P compared with Pgm3 [PMID:23103740 "Pgm2 had a 2000 times higher preference for glucose-1-phosphate when compared to Pgm3"].
- GAL5 = PGM2, galactose-inducible via GAL4/GAL80/GAL3 [PMID:2138705 "The Saccharomyces cerevisiae GAL5 (PGM2) gene was isolated and shown to encode the major isozyme of phosphoglucomutase."; "The galactose inducibility of GAL5 was found to be under the control of the GAL4, GAL80, and GAL3 genes."].
- pgm1 pgm2 double mutant cannot grow on galactose [PMID:8119301 "Cells deleted for both, PGM1 and PGM2, could not grow on galactose."].

## Ion homeostasis phenotypes (indirect)
- pgm2 on galactose: increased Ca2+ uptake, attributed by the authors to Glc-1-P accumulation [PMID:10681519 "We propose that these Ca(2+)-related alterations are attributable to a reduced metabolic flux between Glc-1-P and Glc-6-P due to a limitation of PGM enzymatic activity in the pgm2Delta strain."].
- Suppressed by pmc1 [PMID:15252028 "Disruption of the PMC1 gene, which encodes the vacuolar Ca(2+)-ATPase Pmc1p, suppressed the Ca(2+)-related phenotypes observed in the pgm2Delta strain."].
- Trk K+ transport correlates with glucose phosphate levels [PMID:15164360 "In all cases Trk activity was positively correlated with levels of glucose phosphates"].
- Reviewer interpretation: these are downstream metabolic consequences of losing Pgm2 catalysis; Pgm2 does not itself perform ion transport or sensing -> marked over-annotated, not removed.

## Assessment
- Core: phosphoglucomutase; major isozyme, galactose-induced, required for galactose catabolism (Glc-1-P -> Glc-6-P) and supplies Glc-1-P for UDP-glucose synthesis on other carbon sources. Cytoplasmic (UniProt; IDA PMID:8385141 identifies cytoplasmic pgp62 as PGM, a Glc-phosphotransferase acceptor).
