# Manual Deep Research: ureC1

Automated Falcon and OpenScientist runs did not complete for ureC1, so this is a manual synthesis from the fetched UniProt record, the Nitrososphaera context, and the completed PTHR43440 family research.

## Evidence synthesis

ureC1 is annotated as urease subunit alpha with EC 3.5.1.5 [file:9ARCH/ureC1/ureC1-uniprot.txt "RecName: Full=Urease subunit alpha; EC=3.5.1.5"]. UniProt maps the protein to urea degradation by the urease route, step 1 of 1 [file:9ARCH/ureC1/ureC1-uniprot.txt "PATHWAY: Nitrogen metabolism; urea degradation; CO(2) and NH(3) from urea (urease route): step 1/1"].

PTHR43440 family research supports UreC/large alpha subunits as the catalytic urease subunits that house the metal active site and hydrolyze urea [file:interpro/panther/PTHR43440/PTHR43440-deep-research-falcon.md "Canonical urease catalyzes urea to ammonia and carbamate"]. The same report adds an important caveat: rare iron ureases exist, so nickel binding should be accepted from the gene-specific UniProt metal-binding statement, not blindly from family membership [file:9ARCH/ureC1/ureC1-uniprot.txt "Binds 2 nickel ions per subunit"].

## Curation consequence

Accept urease activity, nickel binding, urea metabolic process, and UniPathway urea catabolic process for ureC1. Treat nickel binding as supported here, but do not generalize it to every distant urease-family member without metal evidence.
