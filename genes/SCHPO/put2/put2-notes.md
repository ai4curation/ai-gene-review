# put2 (SPBC24C6.04, UniProt O74766) notes

## Identity and naming
- PomBase symbol put2; UniProt has NO gene name for O74766 (ORF SPBC24C6.04 only), so it had to be fetched by accession.
- Probable P5C dehydrogenase (EC 1.2.1.88), ortholog of S. cerevisiae PUT2 (P07275); PANTHER PTHR42862 (not the human ALDH4A1 family PTHR14516). [UniProt:O74766 "RecName: Full=Probable delta-1-pyrroline-5-carboxylate dehydrogenase;"]

## Evidence
- Only sequence-based: [UniProt:O74766 "Reaction=L-glutamate 5-semialdehyde + NAD(+) + H2O = L-glutamate + NADH"]; pathway step 2/2 of proline degradation to glutamate.
- UniProt gives no subcellular location. The N-terminus (MSQFAEFKLPAIKNEPPKHY...) does not look like a classical amphipathic, Arg-rich presequence, unlike S. cerevisiae PUT2. Mitochondrial matrix rests on the PAINT IBA (from SGD PUT2) and the PomBase GO-CAM (mitochondrial matrix). Worth confirming experimentally.
- PomBase GO-CAM 678073a900003902: put2 GO:0003842 in mitochondrial matrix, part of GO:0006562.

## Curation points
- oxidoreductase activity (InterPro2GO) is uninformative -> MODIFY to GO:0003842.
- The yeast PUT2 review is still a PENDING stub, so no ortholog core_functions to align with.
