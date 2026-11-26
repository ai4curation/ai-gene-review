# Bacteriophage P2 Gene P (Terminase, ATPase subunit gpP; UniProt P25479)

## Overview
Gene **P** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 590-amino-acid large ATPase subunit gpP (66.5 kDa; `UniProt:P25479`, `InterPro:IPR010332` `ATPase_terminase-su_N` / `InterPro:IPR027417` `P-loop_NTPase` / `InterPro:IPR035421` `Terminase_6C` / `Pfam:PF03237` `Terminase_6`) of the viral DNA packaging terminase complex (`PMID:1837355`, `file:BPP2/P/P-uniprot.txt`). Together with the small endonuclease subunit gpM (`UniProt:P25476`), gpP docks at the dodecameric gpQ portal vertex of the empty procapsid and hydrolyzes ATP to power translocation of the linearized P2 (or satellite P4) dsDNA genome into the capsid (`PMID:1837355`, `file:BPP2/P/P-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:1837355** (*Nucleotide sequence of the DNA packaging and capsid synthesis genes of bacteriophage P2.*):
  - `"Each of six open reading frames found in the interval was assigned to one of the essential genes (Q, P, O, N, M and L) by correlating genetic, physical and mutational data with DNA and protein sequence information. Polypeptides predicted were: a capsid completion protein, gpL; the major capsid precursor, gpN; the presumed capsid scaffolding protein; gpO; the ATPase and proposed endonuclease subunits of terminase, gpP and gpM, respectively; and a candidate for the portal protein, gpQ."`
- **UniProtKB P25479 (`file:BPP2/P/P-uniprot.txt`)**:
  - `"ATPase subunit of the terminase Complex, which is involved in DNA packaging. Packages a single monomeric circular viral chromosome into a procapsid. The terminase Complex docks on the portal protein of an empty procapsid, and gpP hydrolyzes ATP to power the translocation of the DNA into the capsid."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0005524` (`ATP binding`, IEA): **ACCEPT**
  - `GO:0000166` (`nucleotide binding`, IEA): **MODIFY** to `GO:0005524` (`ATP binding`).
  - `GO:0016887` (`ATP hydrolysis activity`) and `GO:0003677` (`DNA binding`): **NEW** supported by `PMID:1837355` and `file:BPP2/P/P-uniprot.txt`.
- **Biological Process**:
  - `GO:0019073` (`viral DNA genome packaging`): **NEW** supported by `PMID:1837355` and `file:BPP2/P/P-uniprot.txt`.
- **Cellular Component / Complex**:
  - `GO:0043493` (`viral terminase complex`): **NEW** (`part_of`, put in `in_complex` in `core_functions`).
  - `GO:0030430` (`host cell cytoplasm`): **NEW** (`located_in`, put in `locations` in `core_functions`).
