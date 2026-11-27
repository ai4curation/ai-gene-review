# tdh1 (S. pombe, UniProt P78958, SPBC32F12.11) notes

Role in module `emp_glycolysis`: phosphorylating GAPDH step (EC 1.2.1.12); S. cerevisiae counterparts TDH1/TDH2/TDH3. S. pombe paralog gpd3 (O43026).

## Evidence: glycolysis
- Reaction [UniProt:P78958 "Reaction=D-glyceraldehyde 3-phosphate + phosphate + NAD(+) = (2R)-3-"].
- Tdh1 is the major GAPDH; gpd3 is minor [PMID:18406331 "a second GAPDH gene expressed at a much lower level than tdh1"] and [PMID:18406331 "The other is Tdh1, GAPDH enzyme that catalyzes the sixth step of the glycolytic pathway."].

## Evidence: peroxide signalling (moonlighting)
- Associates with Mcs4 RR and MAPKKKs [PMID:18406331 "the glycolytic enzyme glyceraldehyde-3-phosphate dehydrogenase (GAPDH) physically associates with the Mcs4 response regulator and stress-responsive MAP kinase kinase kinases (MAPKKKs)."].
- Cys-152 oxidised by H2O2 [PMID:18406331 "In response to H2O2 stress, Cys-152 of the Tdh1 GAPDH is transiently oxidized, which enhances the association of Tdh1 with Mcs4."]; C152S abolishes oxidation [PMID:18406331 "Among the three Cys residues in Tdh1, substitution of Cys-152 with Ser (C152S) completely abolished the H 2 O 2 -induced oxidation of Tdh1"].
- Required for Mpr1-Mcs4 phosphorelay [PMID:18406331 "Furthermore, Tdh1 is essential for the interaction between the Mpr1 HPt protein and the Mcs4 response regulator and thus for phosphorelay signaling."].
- Peroxide-specific Spc1 defect [PMID:24255738 "As a consequence, the ∆tdh1 mutant is defective in activation of the Spc1 MAPK by peroxide stress but not other forms of stress."]; binds Mcs4 independently of MAPKKKs [PMID:24255738 "The Tdh1 GAPDH physically associates with the Mcs4 RR independently of the Wis4 and Win1 MAPKKKs."].

## Curation decisions
- GO:0019826 oxygen sensor activity (IMP) -> MODIFY to GO:0140442 peroxide sensor activity: the sensed species is H2O2 (Cys-152 oxidation), not O2.
- protein binding (IPI, Mcs4) -> MODIFY to GO:0030674 protein-macromolecule adaptor activity (Tdh1 needed for the Mpr1-Mcs4 association).
- NADP binding (IEA) over-annotated (NAD+-dependent enzyme), as in S. cerevisiae TDH1 review.
- IC to obsolete GO:0061621 -> MODIFY to GO:0006096.
- Fungal-type cell wall (ISO from S. cerevisiae TDH3) kept non-core.
- Two core functions: GAPDH in glycolysis; adaptor role in the Mcs4 RR-MAPKKK complex for peroxide signalling.

## Naming trap
- UniProt lists synonym gpd1 for tdh1, but PomBase gpd1 (P21696, SPBC215.05) is glycerol-3-phosphate dehydrogenase. The second S. pombe GAPDH is named gpd3, not tdh2/3.
