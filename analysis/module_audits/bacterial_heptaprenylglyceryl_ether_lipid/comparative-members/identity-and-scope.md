# Comparative members: identity and reaction scope

The frozen UniProt records identify GEOKA Q5L3C1 as GK0274/pcrB in Geobacillus kaustophilus HTA426; STAA1 A7X435 as SAHV_1891/pcrB in Staphylococcus aureus Mu3; and FLAJ1 A5FJK8 as Fjoh_1584 in Flavobacterium johnsoniae UW101. Official PDBe/SIFTS UniProt mappings were retrieved on 2026-11-07 using the URLs retained in each `*-mapping.json`:

| PDB | UniProt | Interpretation |
|---|---|---|
|4NAE,4NAF|Q5L3C1|Geobacillus PcrB; source PMID24684232|
|3W01,3W02|A7X435|S. aureus Mu3 PcrB; source PMID23322418|
|4JEJ|A5FJK8|F. johnsoniae group II C20 GGGPS; source PMID24684232|
|4MM1|O26652|Archaeal comparator, not any of the three reviewed bacterial proteins|

A mapping establishes the accession represented in a structure, not every biochemical assay or native phenotype. PMID23322418 was read in full. Its S. aureus structures contain PEG or sulfate; the glycerol-phosphate/FsPP complexes are Bacillus structures. The paper assays SaPcrB chain-length mutants and Mg dependence; structural ligand identity is not changed into a bound native C35 product. Q5L3C1 and A5FJK8 have target-specific ECO0000269 curated functional statements linked to PMID21761520/24684232. Those primary caches are abstract-only; no inaccessible full-text assay details are invented. A subsequent full-text access check obtained the 2014 Wiley publisher article. Figure2 uses a heterologous Bacillus delta-pcrB host; Figure5 separates wild type from the I90A specificity mutant. The additional source-scope note records these boundaries; no publication cache was refreshed.

The current GO definitions were retrieved from official QuickGO and retained in `ontology.json`. GO0046474 includes biosynthesis of any glycerophosphate derivative with at least one O-acyl, O-alkyl or O-alkenyl group. Thus a monoether glycerophosphate is within the definition, and the characterized transfer reaction directly performs that biosynthesis. This broad process does not assert downstream dephosphorylation, acetylation, glycosylation or the complete Bacillus ether-carrier bypass in another organism. Broad metabolism is refined to the existing biosynthesis term; broad prenyl/alkyl transfer is refined to the corresponding substrate-specific synthase term.

Q5L3C1 and A7X435 support C35 HepGP synthesis. A5FJK8 supports C20 GGGP synthesis. A5FJK8's I90A mutant accepting HepPP is an engineered specificity change, not wild-type PcrB capability. It is a comparison/control and must not enter the C35 PcrB module's carrier set. Its TreeGrafter GO0000107 HisF reaction differs chemically from its characterized prenyltransferase reaction and is removed with a PANTHER source-defect record; the underlying PANTHER or GOA files are not edited.

All three actual Falcon attempts failed403 authentication. Manual primary-source and curated experimental-record review substituted for provider research; no provider report was invented. PAINT-loss commands complete but all three accessions are absent leaves; lineage losses are unassessed, not proven absent. Every original source row remains in order and no NEW row is added.
