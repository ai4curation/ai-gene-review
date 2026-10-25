# KT2440 maiA/nicE evidence notes

## Identity and evidence strength

Reviewed Q88FY4 (PP_3942, maiA/nicE) is classified by HAMAP MF_00943 and InterPro IPR028615 as maleate isomerase. PANTHER PTHR40267:SF1 and its parent are officially BLR3294 PROTEIN. Actual Pfam is PF17645 (Amdase); the older Falcon prose invoking PF01177 is not used. Specific family classification and native nic-cluster context support the maleate-to-fumarate assignment.

PMID:18678916 assigns NicE from homology and conserved cysteines; it reports direct crude-extract enzyme assays for NicD/NicF but not for KT2440 NicE. The paper prints C104/C222, whereas current UniProt features use C80/C198. Without reconstructing the historical sequence boundary, these numberings are not treated as equivalent target measurements or declared a wrong-gene error. The structural/kinetic S16 Iso work is a homolog comparator, never a KT2440 enzyme experiment.

## Oligomer transfer audit

The ISS WITH/FROM donor is UniProt O24766, Alcaligenes faecalis MaiA. Its direct primary PMID:9345272 states “The molecular weight of maleate isomerase was estimated as 60 kDa, consisting of a 28 kDa dimer”, with gel-filtration/SDS-PAGE methods specified in the abstract. The same donor supports the maleate-isomerase activity transfer, but this source does not explain the homotetramerization assertion. PMID:10803955 explicitly tests cysteine substitutions in the Alcaligenes enzyme. Both caches are abstract-only; no claim that the full papers were inspected is made. The current target homodimer statement is HAMAP-derived. Homotetramerization remains UNDECIDED, with traced source metadata, rather than turning an uncertain comparative inference into a confident target replacement.

## Existing NEW process proposal

The previously proposed GO:1901848 nicotinate catabolic process is retained with IC evidence, not upgraded to IDA. MaiA performs the terminal chemical conversion rather than serving as a substrate or merely being required. The parent is a catabolic process; no ancestor/descendant is additionally proposed. This is grounded in the native cluster and specific family assignment, not in an apparent annotation gap.

Comparator check on2026-10-25: QuickGO GO:1901848 searches for O24766 and F8G0M3 each returned zero annotations. Both enzymes perform maleate isomerization, but that catalytic role alone does not establish a nicotinate feeding pathway. S16 provides direct negative nicotinate-utilization evidence under the tested conditions. Therefore the absence is respected for those comparators, and native KT2440 pathway context supplies the additional evidence for its existing proposal. No GO-CAM entry was available to challenge that role assignment.

## Source access and research provenance

Review and annotation-reviewer workflow applied on 2026-10-25. Existing KT2440 Falcon reports were read as literature guides, not regenerated or treated as primary experiments. PMID:18678916 remains abstract-only locally after a supported force refresh; the full Results and Methods were independently read at https://pmc.ncbi.nlm.nih.gov/articles/PMC2516282/. The review quotes the cached abstract or curated experimental UniProt statements where appropriate and does not pretend that a body-specific quotation is present in the cache. PMID:22530095 was fetched with full text. No publication cache was manually edited.

For the new S16 comparator, default Falcon deep research with Perplexity-lite fallback ran concurrently with publication caching; Falcon authentication failed and Perplexity returned HTTP401 insufficient_quota (log `/tmp/bacillus-nicotinate-s16-deep.log`). No provider-branded research file was fabricated. FEBA retrieval was attempted for all four targets: no local database or remote source was reachable, and no fitness artifact was written. PSEP6 also lacks a configured organism mapping. This is missing data, not a negative fitness phenotype. The GO-CAM index had no matches to Q88FY3, Q88FY4, Q88FY5 or F8G0M3.

## Shared downstream chemistry and taxonomic boundary

The lower order is N-formylmaleamate --NicD/Nfo--> maleamate plus formate --NicF/Ami--> maleate plus ammonium --MaiA/NicE/Iso--> fumarate. PMID:22530095 directly characterized the S16 versions after recombinant expression and purification. Its full text reports: “Attempts to degrade nicotinic acid by resting cells of strain S16 did not result in any degradation after 24 h of incubation”. S16 lacks the KT2440 nicAB entry genes in that study. Thus a shared lower enzyme cannot establish complete nicotinate degradation or justify transferring nicotinate-catabolism annotation to the nicotine-pathway comparator. The nicotine enzymes named NicA/NicA2 are not the KT2440 nicotinate hydroxylase small subunit merely because they share a name. No new nicotine-process annotation was added to the KT2440 genes.
