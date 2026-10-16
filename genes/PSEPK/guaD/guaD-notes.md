# guaD (PP_4281; Q88F18) curation notes

## Evidence retained

- UniProt assigns the exact reaction guanine + H2O + H+ -> xanthine + NH4+ (RHEA:14665) and a zinc cofactor by automated rules [file:PSEPK/guaD/guaD-uniprot.txt, "Reaction=guanine + H2O + H(+) = xanthine + NH4(+);"]
- InterPro IPR014311 identifies the guanine-deaminase family, and PANTHER node PTN000138455 propagates GO:0008892 from experimentally annotated ortholog seeds [file:interpro/panther/PTHR11271/PTHR11271-paint.tsv, "PTHR11271 PTN000138455 GO:0008892"].
- The OpenScientist report independently retrieved the same identity and reaction but states that there is no direct enzymology for Q88F18 [file:PSEPK/guaD/guaD-deep-research-openscientist.md, "No direct enzymology on the KT2440 protein."].
- KT2440 can use guanine and other purine derivatives as sole nitrogen sources, confirming organism-level pathway flux but not assigning that phenotype specifically to GuaD [PMID:26355499, "permitting their use as sole nitrogen sources"].

## Curation decisions

- Accept GO:0008892 and GO:0006147 as the informative core function and process.
- Keep zinc binding and predicted cytosol only as non-core properties.
- Mark generic hydrolase/deaminase parents and broad guanine metabolism as over-annotations because exact child terms are present.
- Do not promote the report's inferred catalytic-residue numbering, regulation, cytosolic localization, or ammeline promiscuity to established KT2440 facts.
