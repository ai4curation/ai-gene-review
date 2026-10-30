# ERG3 (YLR056W) notes

UniProt P32353; Delta7-sterol 5(6)-desaturase, EC 1.14.19.20; di-iron, 3 His boxes [UniProt:P32353].

## Evidence journal
- Cloned by complementation; null viable [PMID:1864507 "Gene disruption resulting from a deletion/substitution demonstrates that ERG3 is not essential for cell viability or the sparking function."].
- Microsomal Delta5-desaturation needs O2 and NAD(P)H, CN-sensitive [PMID:34600 "These results suggested an involvement in delta 5-desaturation of a mixed function oxidase system resembling that for the fatty acyl-CoA desaturation reaction."].
- Topology: luminal N-terminus, cytosolic catalytic centre; ERAD substrate [PMID:21737688 "Erg3p is a glycoprotein with an ER luminal N terminus and a cytosolic C terminus"].

## Ontology issue
- GO:0000248 "C-5 sterol desaturase activity": definition text gives 5,7,24(28)-ergostatrienol -> 5,7,22,24(28)-ergostatetraenol (the C-22 / Erg5 reaction, cf. GO:0000249). GO:0050046 matches Erg3. All GO:0000248 rows MODIFY -> GO:0050046.

## Decisions
- ER lumen IDA -> MODIFY ER membrane; protein binding REMOVE; RCA cytosol -> ER membrane; iron binding, lipid biosynthetic KEEP_AS_NON_CORE.
