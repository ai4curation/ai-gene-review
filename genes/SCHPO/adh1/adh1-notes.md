# adh1 (SPCC13B11.01, UniProt P00332) notes

Evidence journal (no paid deep research run; built from UniProt, cached PMIDs and the PomBase GO-CAM).

## Identity and activity
- Zinc medium-chain ADH, EC 1.1.1.1, ortholog of S. cerevisiae ADH1 [UniProt:P00332 "Belongs to the zinc-containing alcohol dehydrogenase"].
- Function: [UniProt:P00332 "Reduces acetaldehyde to ethanol during the fermentation of"] glucose.
- Kinetics of the cloned S. pombe enzyme compared with ScADH I-III [PMID:3546317 "All four wild-type enzymes were produced from the cloned genes"]; S. pombe ADH has Met at position 294 like ScADH I [PMID:3546317 "Isozyme I and the S. pombe enzyme have methionine at position 294"]. UniProt KM for acetaldehyde 1.6 mM, NADH 100 uM.
- Two Zn2+ per subunit, homotetramer by similarity to P00330 [UniProt:P00332].

## Physiology
- adh1 null cells still ferment; adh4 is induced and takes over [PMID:15040954 "this ethanol production is caused by the enhanced expression of a Saccharomyces cerevisiae ADH4-like gene product"]; double mutant is non-fermentative [PMID:15040954 "only these two ADHs produce ethanol for fermentative growth"].
- Kim et al. note adh1 overexpression extends lifespan in S. pombe [PMID:25102102 "There are reports that overexpression of the adh1+ gene extends lifespan in S. cerevisiae [35] and in S. pombe [36]"].

## GO-CAM
- PomBase gomodel:678073a900000393 (fermentation): adh1 enables GO:0120542, occurs_in cytosol, part_of GO:0019655 (IGI PMID:15040954 with adh4).

## Review decisions
- All MF/CC rows accepted; oxidoreductase -> MODIFY to GO:0120542; ARBA ethanol metabolic process -> MODIFY to GO:0019655.
- Core function matches S. cerevisiae ADH1 review (GO:0120542, GO:0019655, cytosol). No Ehrlich-pathway core function added: not studied in S. pombe.
