# HSPB9 (Q9BQS6) research notes

## Identity
- Heat shock protein beta-9 / cancer-testis antigen 51 (CT51), small heat shock protein (HSP20/alpha-crystallin) family, 159 aa, ~17.5 kDa. Contains alpha-crystallin domain (sHSP, residues 36-147).
- Identified by alpha-crystallin-domain search profiles as the ninth human sHSP [PMID:11470154 "Using search profiles based on the conserved alpha-crystallin domain ... The other, named HspB9, is specifically expressed in testis"].

## Tissue / expression
- Testis-specific, expressed in spermatogenic cells from late pachytene spermatocyte to elongate spermatid stage [PMID:11470154 "HspB9, is specifically expressed in testis, notably in the spermatogenic cells from late pachytene spermatocyte stage till elongate spermatid stage."]. HPA: tissue enhanced (testis). Rapidly evolving (mouse HspB9 38% divergent from human), suggesting a sex/reproduction-related role [PMID:11470154].
- Cancer/testis antigen: also expressed in tumors [PMID:15503857 "HSPB9 belongs to the steadily growing number of cancer/testis antigens."].

## Interactions / function
- Interacts with TCTEL1 (DYNLT1, P63172), a light chain of cytoplasmic and flagellar dynein, in Y2H and co-IP; co-expressed in similar testis cells [PMID:15503857 "TCTEL1, a light chain component of cytoplasmic and flagellar dynein, interacted in both the yeast two-hybrid system and in immunoprecipitation experiments with HSPB9."]. GOA IPI PMID:15503857 WITH P63172 (DYNLT1).
- No direct chaperone (holdase) activity demonstrated experimentally for HSPB9; function is largely inferred from sHSP family membership. Poorly characterized.

## Localization
- Cytoplasm and nucleus; translocates to nuclear foci during heat shock [file:human/HSPB9/HSPB9-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm ... Nucleus ... Note=Translocates to nuclear foci during heat shock." (PMID:19464326)]. GOA: cytosol (IDA, HPA), nucleoplasm (IDA, HPA), nucleus, cytoplasm.

## GO review plan
- Localization terms (nucleus, cytoplasm, cytosol, nucleoplasm): ACCEPT (IDA/HPA/UniProt supported); nucleus/nucleoplasm partly from heat-shock translocation.
- protein binding (IPI, GO:0005515, PMID:15503857) WITH DYNLT1: bare term uninformative -> MODIFY to dynein light chain binding? The informative MF is binding the dynein light chain TCTEL1. GO has "dynein light intermediate chain binding" etc. Safer: dynein complex binding? Use a specific term only if confident. DYNLT1 is a dynein light chain; the most defensible specific term may be "protein-containing complex binding" - but that's still generic. Given a single Y2H/co-IP interaction with one partner, KEEP_AS_NON_CORE is most defensible (records a genuine interaction; not clearly core given poor characterization). Avoid over-precise guessing.
- Core function: small-HSP putative holdase (unfolded protein binding, GO:0051082) inferred from family; testis/spermatogenesis context. Mark as inferred.
</content>
