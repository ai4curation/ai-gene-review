# Lss (rat) notes

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d) changes:
- 2 new ISO rows from human LSS (UniProtKB:P48449): lanosterol synthase activity (GO:0000250) and cholesterol biosynthetic process (GO:0006695). Both are donor-split duplicates of the ISO rows from mouse Lss (MGI:MGI:1336155); both ACCEPT, with reviews naming the human donor.
- 2 rows retired by GOA: cholesterol biosynthetic process via lathosterol (GO:0033490) and via desmosterol (GO:0033489), both ISO. Reviews kept; a sentence noting the retirement was added.

Action changes:
- Endoplasmic reticulum membrane (GO:0005789; IEA, ISS, ISO): KEEP_AS_NON_CORE -> ACCEPT. The ER membrane is where the cyclization occurs, so it is the core location rather than context [PMID:7568116 "Unexpectedly, this microsomal membrane-associated enzyme showed no clearly delineated transmembrane domain."]. Added as `locations` in core_functions.
- Lipid droplet (IBA, IEA, ISO) and regulation of protein stability (ISO) stay KEEP_AS_NON_CORE, but now have positive support instead of the generic FUNCTION quote. Lipid droplet: human LSS lipid-droplet proteomics [PMID:14741744 "a fraction enriched with lipid droplets was isolated from a human hepatocyte cell line HuH7 using sucrose density gradient centrifugation"]. Protein stability: indirect, mediated by lanosterol [PMID:26200341 "Engineered expression of wild-type, but not mutant, LSS prevents intracellular protein aggregation of various cataract-causing mutant crystallins."].
- Stale UniProt quotes: UniProt added "(PubMed:7568116)" after "forms the sterol nucleus", so all 21 copies of the old FUNCTION quote were trimmed to the verbatim substring. Location rows now quote "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane" / "Peripheral membrane protein".
- Description rewritten to remove curation commentary.

Open questions:
- Is there direct evidence that mammalian OSC is active on lipid droplets, or only that it co-fractionates with them?
