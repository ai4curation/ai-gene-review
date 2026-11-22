# mpg1 (SPCC1906.01; UniProt O74484) notes

## Naming trap
- S. pombe mpg1 = GDP-mannose pyrophosphorylase (GMPPB-type). In S. cerevisiae "MPG1" is an alias of PSA1 (also VIG9/SRB1), so symbols coincide across species; keyed on O74484 (fetch-gene fetched the correct accession).

## Experimental (S. pombe)
- Donoso et al. 2005 (abstract-only; not cited by any GOA row): [PMID:16049679 "Mpg1 shows strong similarity to other GDP-mannose-1-phosphate guanyltransferases involved in the maintenance of cell wall integrity and/or glycosylation"]; [PMID:16049679 "cells lacking Mpg1 present a defect in glycosylation, are more sensitive to Lyticase, and show an aberrant septum structure from the start of its deposition"]; [PMID:16049679 "mpg1 null mutants arrest as septated and bi-nucleated 4C cells, without an actomyosin ring"]. Enzymatic activity not assayed (abstract).
- Location: [UniProt:O74484 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16049679}."]; HDA cytosol (PMID:16823372).
- Reaction [UniProt:O74484 "Reaction=alpha-D-mannose 1-phosphate + GTP + H(+) = GDP-alpha-D-mannose"].
- Ortholog Psa1/Vig9 activity [PMID:9195935 "We demonstrated the enzyme activity of Vig9 protein using a recombinant fusion protein produced in Escherichia coli."].

## GO-CAM
- Not in any cached PomBase GO-CAM.

## Decisions
- MF (IBA, IEA), GDP-mannose biosynthesis, cytoplasm/cytosol accepted. transferase activity MODIFY -> GO:0004475 (S. cerevisiae PSA1 review kept it non-core instead). GTP binding, glycoprotein biosynthesis, cell wall biogenesis kept non-core.
- Curation gap: PMID:16049679 phenotypes (septum, glycosylation) not represented in GOA.
