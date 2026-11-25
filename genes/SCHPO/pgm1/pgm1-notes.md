# pgm1 (SPBC32F12.10, UniProt O74374) notes

## Identity
- UniProt entry PGM_SCHPO has NO gene name (ORF name SPBC32F12.10 only), which is why `just fetch-gene SCHPO pgm1` failed; fetched with -u O74374.
- Phosphoglucomutase, EC 5.4.2.2, by similarity to S. cerevisiae PGM2 (P37012) [UniProt:O74374 "EC=5.4.2.2 {ECO:0000250|UniProtKB:P37012}"]. Naming trap: the UniProt annotation source is S. cerevisiae PGM2 (the major isozyme), not S. cerevisiae PGM1 (the minor isozyme) even though the S. pombe gene is called pgm1. S. pombe appears to have a single canonical PGM.
- PANTHER PTHR22573:SF2 PHOSPHOGLUCOMUTASE.

## Function
- Reversible Glc-1-P <-> Glc-6-P via Glc-1,6-bisP; Mg2+; supplies Glc-1-P for UDP-glucose synthesis (by similarity) [UniProt:O74374 "Catalyzes the reversible isomerization of alpha-D-glucose 1-"].
- No S. pombe-specific biochemistry found.

## Location
- HTP YFP: cytoplasm/cytosol and nucleus [PMID:16823372; UniProt "Cytoplasm {ECO:0000269|PubMed:16823372}"].

## GO-CAM
- 6796b94c00002484 (Leloir, usually silenced): pgm1 enables GO:0004614 (IBA), cytosol (HDA), part_of GO:0033499 (IC). In wild-type S. pombe the gal genes are silenced, so the dominant physiological role of pgm1 is Glc-1-P/UDP-glucose supply, not galactose catabolism. Not present in the PomBase dolichol models used by the dolichol_phosphate_sugar_donor_supply module.

## 2026-11-12 audit (to COMPLETE)
- No deep-research provider file was available; none was generated. Literature check: web search (PomBase SPBC32F12.10 page, NCBI Gene 2540254) found no S. pombe pgm1 primary study; PomBase lists the product as "phosphoglucomutase Pgm1".
- Resolved the validator warning (core function process GO:0019255 not in existing_annotations) by adding a NEW ISS row (GO_REF:0000024, with UniProtKB:P37012). Participation: PGM catalyses the Glc-1-P/Glc-6-P step itself. Comparator: S. cerevisiae PGM2 carries GO:0019255 with IMP/IGI [PMID:8119301 "No residual phosphoglucomutase activity could be measured in crude extracts or in permeabilized cells of pgm1/2 double mutants."; PMID:10681519 "this "metabolic bottleneck" resulted in an 8-fold increase in the Glc-1-P level compared with the wild-type strain"].
- Added a reason to the IC GO:0033499 row: term definition does not end the pathway at Glc-1-P; non-core because the gal cluster is silenced in wild type.
- No PAINT IRD/IKR on the pgm1 lineage.
