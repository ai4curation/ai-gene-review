# ANKAR notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKAR (Q7Z5J8, FLJ25415) is a dark gene: a 1,434-residue protein with 5 ANK and 6 ARM repeats. The only paper (PMID:15110750, abstract-only) covers gene structure and ubiquitous expression with extensive splicing.
- **The single GOA row is membrane (SubCell IEA, ECO:0007322; the UniProt TRANSMEM feature is ECO:0000255)**, based on one predicted helix at residues 309-329.
  - A Kyte-Doolittle scan (`ANKAR-bioinformatics/`) finds the helix borderline (windows 1.66-1.69 against a 1.6 threshold), and a window inside an ANK repeat scores about as high.
  - So the action is **UNDECIDED**: the evidence neither supports nor refutes membrane anchoring.
- No core function; WHOLLY_DARK knowledge gap.

## 2026-10-04 round 2 (reviewer comments on #4066)

- **Hydropathy reading corrected.** The annotated 309-329 segment holds the protein's top two windows, and the other passing windows (605 in ANK3, 1099 in ARM6) carry Asp/Asn/Glu and are not credible TM helices. So hydropathy mildly favours UniProt's call; the round-1 "borderline" framing undersold it.
- **Added an AlphaFold check** (`alphafold_tm_check.py`). 309-329 is a confident helix (pLDDT 95.6) packed into an ordered region, about as densely as a typical ordered residue (59th percentile). That looks like a buried helix in a soluble fold, but it cannot exclude membrane insertion. UNDECIDED stands, with a better rationale.
- **Expression:** HPA classes ANKAR as testis-enriched, and Pharos as Tdark. The description, gap and experiments now use this.
- **Other fixes:**
  - Switched file: references to the repo convention `file:human/...`.
  - The hydropathy script now reads the cached UniProt record.
  - ECO codes corrected.
