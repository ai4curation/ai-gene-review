# pfk1 (S. pombe, UniProt O42938, SPBC16H5.02) notes

Role in module `emp_glycolysis`: ATP-dependent 6-phosphofructokinase step (EC 2.7.1.11), annoton `atp_pfk_activity`; S. cerevisiae counterpart is the Pfk1/Pfk2 alpha4beta4 hetero-octamer (P16861/P16862).

## Evidence
- Single PFKA-family gene; reaction F6P + ATP -> F1,6BP + ADP [UniProt:O42938 "Catalyzes the phosphorylation of D-fructose 6-phosphate to"].
- Purified enzyme is an octamer of identical ~100 kDa subunits [PMID:11015725 "showed that the enzyme is composed of subunits of identical size of 100+/-5 kDa, forming an octameric structure."].
- Complements S. cerevisiae pfk1 pfk2 double deletion [PMID:11015725 "The Pfk-1 coding sequence of S. pombe was transformed into a Pfk-1 double deletion mutants of Saccharomyces cerevisiae resulting in glucose-positive cells with enzyme activity in the crude cell extract."].
- Allostery: weaker F6P cooperativity and ATP inhibition than budding yeast; F2,6BP and AMP relieve ATP inhibition [PMID:11015725 "Fructose 2,6-bisphosphate (in micromolar range) and AMP (in millimolar range) were found to overcome ATP inhibition and to increase the affinity to fructose 6-phosphate."].
- Homo-octamer confirmed by EM in F6P- and ATP-bound states [PMID:17643314 "Schizosaccharomyces pombe Pfk1 is a homo-octameric enzyme of 800 kDa molecular weight, distinct from its yeast counterparts which are mostly hetero-octameric enzymes composed of two different subunits."].
- Cytosol/cytoplasm by ORFeome YFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"].

## Curation decisions
- GO:0061621 canonical glycolysis and GO:0061615 glycolytic process through F6P were obsoleted by GO on 2026-09-01 (replaced_by GO:0006096 glycolysis; QuickGO history) -> MODIFY to GO:0006096.
- Mitochondrion (IBA, donors only S. cerevisiae Pfk1/Pfk2) and cytoplasmic side of MOM (PomBase ISS from S. cerevisiae Pfk2) kept as non-core; no S. pombe data.
- F6P binding kept non-core (part of catalysis), as in the S. cerevisiae PFK1 review.

## Naming trap
- S. cerevisiae PFK1 is only the alpha subunit; S. pombe pfk1 is the whole (homo-octameric) enzyme. The module correctly notes "fission yeast has a single pfk1 gene".
