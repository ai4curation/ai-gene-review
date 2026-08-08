# hemB assessment notes

## Identity and core reaction

Q88IT6 (PP_2913) is one of two KT2440 ALAD-family proteins assigned EC 4.2.1.24.
UniProt supports porphobilinogen synthase activity, two predicted Schiff-base
lysines, a predicted catalytic zinc triad, and a separate magnesium-binding site
[file:PSEPK/hemB/hemB-uniprot.txt "RecName: Full=Delta-aminolevulinic acid dehydratase"]
[file:PSEPK/hemB/hemB-uniprot.txt 'ligand_note="catalytic"']
[file:PSEPK/hemB/hemB-uniprot.txt 'ligand="Mg(2+)"'].
These are sequence/rule-based assignments rather than direct KT2440 biochemistry.

## OpenScientist assessment

The OpenScientist report correctly identifies the ALAD reaction and recognizes
that direct characterization of Q88IT6 was not found. Its main zinc-site call is
already supported more directly by the UniProt feature table. The report does
not discuss the second KT2440 ALAD-family paralog, HemBB/PP_3322, and therefore
cannot establish which paralog carries native pathway flux. It also provides
unsaved pairwise identities, exact cross-species residue mappings, and
ortholog-derived oligomer, inhibitor, and metal behavior. Those calculations and
transfers were not used as target-specific evidence.

## Curation decisions

GO:0004655 is accepted as the predicted core molecular function. The zinc row is
retained because UniProt predicts three catalytic Zn2+ ligands, while the broad
metal-binding row is refined to the additional predicted Mg2+ site. The module
allows an active ALAD-family enzyme and does not require HemB over HemBB.
