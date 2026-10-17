# ARG8 (YOL140W, P18544) notes

Evidence journal (no paid deep research run; built from UniProt and cached abstracts).

- Activity: acetylornithine aminotransferase, EC 2.6.1.11; "catalyzes the conversion of N-acetylglutamate-gamma-semialdehyde (NAGSA) to N-acetylornithine in arginine biosynthesis" [UniProt:P18544]. PLP cofactor; class-III PLP aminotransferase family [UniProt:P18544].
- Cloning/enzymology: [PMID:2199330 "Genes argD and ARG8, encoding the acetylornithine aminotransferase (ACOAT) subunit in Escherichia coli and Saccharomyces cerevisiae, respectively, have been cloned and sequenced."] Side activity on ornithine: [PMID:2199330 "S. cerevisiae ACOAT transaminates ornithine about as efficiently as E. coli does."]; UniProt notes this is of little physiological importance [UniProt:P18544].
- Location: mitochondrial matrix; N-terminal transit peptide 1..13 [UniProt:P18544]. Fractionation: the five acetylated-cycle enzymes incl. ACOAT [PMID:205532 "These enzymes were exclusively particulate."] and [PMID:205532 "suggested that these enzymes were associated with the mitochondria."]. Mito proteomics HDA (PMID:16823961, PMID:24769239) concordant.

## Curation decisions
- All ACOAT MF, arginine biosynthesis BP, mitochondrion/matrix CC rows accepted.
- Cytosol (RCA, YeastPathways GO-CAM conversion, is_active_in) REMOVED: contradicted by matrix localisation. Only the steps from ornithine onward are cytosolic in yeast [PMID:205532].
- Generic transaminase (IEA) and arginine metabolic process (IEA) -> MODIFY to the specific terms already present.

## Module-level observation
- YeastPathways-derived GO-CAM places ARG8 in cytosol; module should model the ARG2/ARG5,6/ARG8/ARG7 segment in the mitochondrial matrix and the ornithine-to-arginine segment in the cytosol.
