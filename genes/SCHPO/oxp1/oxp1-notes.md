# oxp1 (SPAC11D3.15, UniProt Q10094) – notes

Putative ATP-dependent 5-oxoprolinase. Module: OPLAH step. S. cerevisiae ortholog OXP1 (review genes/yeast/OXP1).

Naming trap: UniProt names Q10094 "Uncharacterized protein AC11D3.15" with no gene name, so `just fetch-gene SCHPO oxp1` failed; fetched by accession. Note S. cerevisiae OXP1 is the ortholog of BOTH S. pombe oxp1 and oxp2.

## Evidence
- 1317 aa; InterPro Hydantoinase_A (IPR002821), Hydantoinase_B (IPR003692), Hydant_A_N; PANTHER PTHR11365:SF2 "5-OXOPROLINASE" [UniProt:Q10094]. Both oxp1 (1317 aa) and oxp2 (1260 aa) are full-length enzymes with A and B regions; they are tandem paralogs (adjacent ORFs SPAC11D3.14c / SPAC11D3.15), NOT a split enzyme.
- Activity by orthology to S. cerevisiae Oxp1: [PMID:20402795 "OXP1/YKL215c, an uncharacterized ORF of Saccharomyces cerevisiae, encodes a functional ATP-dependent 5-oxoprolinase of 1286 amino acids."]
- Cytosol, ORFeome HDA [PMID:16823372].
- No S. pombe experimental study found (web search, PomBase gene page summaries only).

## Decisions
- catalytic activity / hydrolase activity IEA -> MODIFY to GO:0017168.
- Cellular detoxification NAS -> MARK_AS_OVER_ANNOTATED.
- Core BP GO:0006749 kept consistent with yeast OXP1 review and with PomBase GO-CAM (part_of GO:0006749); the GO:0006751 IBA is accepted.
