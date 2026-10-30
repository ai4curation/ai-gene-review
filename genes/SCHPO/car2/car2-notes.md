# car2 (SPBC21C3.08c, UniProt Q9P7L5) notes

## Identity and naming
- PomBase car2 = ornithine aminotransferase (OAT, EC 2.6.1.13), ortholog of S. cerevisiae CAR2. Single OAT gene in S. pombe [PMID:26075619 "deletion of the single fission yeast ornithine transaminase gene, car2+"].
- PANTHER PTHR11986:SF18 is named "ORNITHINE AMINOTRANSFERASE, MITOCHONDRIAL" (dominated by animal OAT), but car2 has no predicted transit peptide and is cytosolic.

## Function
- [UniProt:Q9P7L5 "Reaction=a 2-oxocarboxylate + L-ornithine = L-glutamate 5-semialdehyde"], PLP cofactor by similarity.
- car2Δ prevents arginine conversion into proline/glutamate/glutamine/lysine [PMID:20460254 "In a car2Δ single deletion strain, arginine conversion was similarly prevented"]. In wild-type cells arginine label enters all detectable proline [PMID:20460254 "Further analysis revealed incorporation of label in all detectable proline as well as in 25–30% of glutamate, glutamine, and lysine"], i.e., in S. pombe the arginase-OAT route feeds proline massively when arginine is supplied.

## Location
- Cytoplasm and nucleus from ORFeome [UniProt:Q9P7L5 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}. Nucleus"]; PomBase GO-CAM 678073a900003902: cytosol, part of GO:0006527.

## Curation points
- Mitochondrion IBA (animal/plant clade trait): contradicted by cytosolic localization and absence of presequence -> REMOVE (as for yeast CAR2).
- L-proline biosynthetic process (UniPathway IEA): car2 catalyses a real step of arginine-to-proline conversion, and S. pombe data show this route is quantitatively large when arginine is present; still secondary (de novo proline comes from glutamate via pro2/pro1/pro3) -> KEEP_AS_NON_CORE.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 10 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

Native car2 deletion strongly reduces arginine-carbon conversion into proline/glutamate-related amino acids (PMID:20460254); PMID:26075619 shows that deleting car2 does not remove the arginase-dependent heavy-nitrogen/urea route. Thus car2 deletion and car1/aru1 double deletion are not interchangeable mechanistically. Cytosolic localization is supported, but the old mitochondrial IBA REMOVE overreached: cytoplasmic/nuclear observations and an unverified impression of targeting sequence do not exclude dual localization. The mitochondrial row is now UNDECIDED with source-specific PTN metadata. The proline-producing role is retained non-core, with labeling conditions stated. The exact pro3/put1/put2 shuttle in pombe remains to be tested.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-SCHPO-car2-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 6, KEEP_AS_NON_CORE 2, MODIFY 1, UNDECIDED 1.
