# arg7 (SPBC1773.14, UniProt P40369) notes

## Identity and naming
- PomBase arg7 = argininosuccinate lyase (ASL, EC 4.3.2.1), ortholog of S. cerevisiae ARG4 (P04076). [PMID:1868575 "The complete nucleotide sequence of the ARG7 gene, coding for argininosuccinate"]
- Naming trap: S. cerevisiae ARG7 is the ArgJ-family ornithine acetyltransferase (S. pombe aga1), unrelated to S. pombe arg7.
- Second S. pombe ASL paralog: arg41 (SPBC1539.03c, UniProt P50514, UniProt gene name "argx").

## Function
- [UniProt:P40369 "Reaction=2-(N(omega)-L-arginino)succinate = fumarate + L-arginine;"] evidence ECO:0000305 from PMID:1868575.
- PMID:1868575 (abstract only): gene sequenced, expressed in S. cerevisiae; C-terminal 66-aa deletion retains some activity [PMID:1868575 "Additionally, a deletion removing 66"]. PomBase IMP for ASL activity and arginine biosynthesis from this paper (presumably complementation of a S. cerevisiae arg4 mutant; full text not available).
- Deletion-library screen: arg7 deletion was NOT recovered as an arginine auxotroph, whereas arg41 deletion was [PMID:32896087 "arg7 is one of two argininosuccinate lyases (with deletion of the other one, arg41, showing arginine auxotrophy)"]. This suggests arg41 carries most in vivo ASL flux, or that arg7 is redundant; it conflicts with the classical naming of arg7 as an arginine-requiring locus — worth checking.

## Location
- Cytosol (ORFeome HDA, PMID:16823372; PAINT IBA). PomBase GO-CAM 6690711d00000916 has arg7 and arg41 both enabling GO:0004056 in cytosol, part of GO:0006526.

## Curation points
- Urea cycle rows (ARBA IEA, IC from ASL activity) reflect the vertebrate pathway name; S. pombe is not ureotelic, the ASL step belongs to arginine biosynthesis. MODIFY to GO:0006526 (as with yeast CAR1 urea cycle rows).
- catalytic activity (InterPro2GO) is uninformative -> MODIFY to GO:0004056.
