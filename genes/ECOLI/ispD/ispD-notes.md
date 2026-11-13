# ispD (Q46893) notes

## Literature checked (cached abstracts; PMC full text could not be retrieved)

- Identification: ygbP encodes the MEP cytidylyltransferase [PMID:10518523 "We show that an enzyme isolated from cell extract of Escherichia coli converts 2-C-methylerythritol 4-phosphate into 4-diphosphocytidyl-2-C-methylerythritol by reaction with CTP."]
- Mechanism: ordered, CTP first; Lys27/Lys213 catalytic [PMID:15379557 "Pulse chase experiments established that the reaction involves an ordered sequential mechanism with mandatory initial binding of CTP."]
- Structures with CTP-Mg2+ and CDP-ME-Mg2+ [PMID:11427897 "complexed with both CTP-Mg2+ and CDP-ME-Mg2+"]; UniProt: "There are no coordination bonds that occur between IspD and magnesium in any of the complexes examined to date." -> the Mg2+ IDA row is treated as over-annotation (metal carried by the nucleotide).
- Lethal point mutants recovered only in a mevalonate-bypass strain [PMID:12859972].

## Decisions

- GO:0008299 MODIFY -> GO:0019288 (MEP-pathway standard for this module).
- GO:0042802 MODIFY -> GO:0042803 (homodimer per UniProt SUBUNIT, PMID:11427897).
- GO:0003824 and GO:0070567 TOO_GENERAL beside GO:0050518.
- Cytosol accepted on the Ishihama cytosol proteome (supplementary data not cached).
- No PAINT losses on the lineage (`just paint-losses ECOLI ispD`).
