# SPAC9E9.06c (threonine synthase, UniProt Q42598) - notes

## Identity / naming
- PomBase systematic ID SPAC9E9.06c, no standard PomBase gene name (PomBase product "threonine synthase"); UniProt gives Name=thrc [UniProt:Q42598].
- UniProt CAUTION: "Was originally (Ref.1) thought to originate from A.thaliana." [UniProt:Q42598] - the accession Q42598 is a historical plant-attributed record later reassigned to S. pombe. Key on the accession, not on the "THRC" name.
- S. cerevisiae ortholog: THR4 (P16120), the source of the UniProt ECO:0000250 assertions and the PomBase ISS rows.

## Function
- Threonine synthase, EC 4.2.3.1: "Reaction=O-phospho-L-homoserine + H2O = L-threonine + phosphate;" [UniProt:Q42598]; PLP cofactor [UniProt:Q42598]; final step (5/5) of L-threonine biosynthesis from L-aspartate [UniProt:Q42598].
- Budding-yeast THR4 encodes the activity [PMID:8082795 "we have determined that this activity depends on the presence in the cell of an active form of the THR4 gene"].
- No S. pombe-specific biochemistry found; function is by orthology to THR4 and the PANTHER IBA node PTN000034281.

## Localization
- Cytosol in the ORFeome YFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"] (HDA, PomBase).

## GO-CAM
- gomodel:678073a900003175 (PomBase homoserine/threonine/glycine model): SPAC9E9.06c enables GO:0004795, occurs_in cytosol, part_of GO:0009088 (IBA evidence). Consistent with this review.

## Review decisions
- Threonine synthase activity, L-threonine biosynthesis, cytosol: accept.
- InterPro "amino acid metabolic process": MODIFY to L-threonine biosynthetic process (as for THR4).
- PLP binding: keep as non-core cofactor binding.
