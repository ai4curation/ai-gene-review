# purE (Escherichia coli K-12, UniProtKB:P0AG18) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurE is the class I N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) mutase of Escherichia coli, a homooctameric cytosolic enzyme that transfers the carbamate carboxylate of N5-CAIR directly to C4 of the imidazole ring to form CAIR. Together with the N5-CAIR synthetase PurK it carries out AIR carboxylation, step 6 of de novo IMP biosynthesis; unlike the class II PurE of animals it does not use free CO2.

### Provenance

No provider deep-research report was generated for this gene. These notes were written by the reviewer from: the fetched UniProt record (file:ECOLI/purE/purE-uniprot.txt), the cached primary publications cited below (most abstract-only; full_text_available is recorded in each publications/PMID_*.md file), the PANTHER family reviews under interpro/panther/, and the P. putida, yeast and human orthologue reviews used as precedents.


### Core function evidence

- 5-(carboxyamino)imidazole ribonucleotide mutase activity (GO:0034023):
  [PMID:8117684 "PurE has been shown by NMR spectroscopy and kinetic analysis, to catalyze the reversible conversion of N5-CAIR and CAIR."]

### Decisions other than ACCEPT

- GO:0042802 identical protein binding (IPI, PMID:10574791): KEEP_AS_NON_CORE. PurE is a homooctamer.
- GO:0042802 identical protein binding (IPI, PMID:16858726): KEEP_AS_NON_CORE. Homo-oligomer detected in a complexome survey.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
