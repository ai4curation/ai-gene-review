# DELTA-OAT annotation review notes

Identity: Q9FNK4 / At5g46180. Verified fetched PANTHER PTHR11986:SF18, ORNITHINE AMINOTRANSFERASE, MITOCHONDRIAL (parent PTHR11986 AMINOTRANSFERASE CLASS III).

PMID:18419821 full text directly tests two OAT null lines: loss of extract OAT activity, failure to utilize Arg/Orn as nitrogen sources, amino-acid accumulation, OAT-GFP complementation, and full-length mitochondrial localization. OAT transfers the delta amino group of free ornithine to an oxo-acid; GSA/P5C feeds the catabolic pathway. This is not acetylornithine transamination. Its PLP family/cofactor site is conserved and curated.

PMID:9576796 full text measures crude-extract activity and salt induction, including apparent Km near 91 mM in young plantlets. Do not describe these as purified recombinant kinetic constants. Salt-related expression/activity is valid, contextual biology. The older interpretation that this causes proline accumulation is correlational and contradicted by the later null-mutant tests under their conditions: retain the seeded NOT proline-biosynthesis row and REMOVE the positive claim, without changing either original payload or inferring that all ornithine carbon can never reach proline. Do not equate absence of a salt phenotype with absence of a measured salt response.

GO:0051646 was checked live in QuickGO: it concerns the placement of mitochondria inside cells. The source shows the placement of OAT inside mitochondria, a different claim. REMOVE this experimental annotation after reading the full source, retaining matrix cellular-component annotations. Matrix precision also uses curated UniProt; GFP colocalization alone resolves mitochondria.

PMID:22321246 abstract explicitly includes native Arabidopsis mutants and Nicotiana silencing, with reduced non-host resistance and pathogen-induced ROS. Preserve hypersensitive-response and bacterial-defense claims as contextual non-core functions; no claim that OAT directly generates ROS.

Chloroplast/plastid claims and the Zn-binding screen remain UNDECIDED with specific evidence gaps; see source-analysis/README.md and exact extracted supplemental rows. Mitochondrial localization alone does not exclude dual targeting.

## Review provenance and verification

2026-10-26: Applied review and annotation-reviewer skills; consulted sibling annotation reviewer for bounded judgments on compartment inference and source-specific corrections. Normal Falcon research and PMID caching ran concurrently after exact-accession seeding. Falcon failed403 authorization and Perplexity-lite fallback failed401 insufficient quota for each target; no provider report was invented. Manual primary research above replaces the unavailable provider output. FEBA is not applicable to these plant targets. Cached publication files were fetched normally and never hand-edited.

All seeded row payloads, including evidence, source, qualifiers, supporting_entities and the OAT NOT flag, are preserved; only review blocks were authored. No NEW annotation rows were added. GO-CAM absence was not used as evidence for a missing annotation or a new process assertion. Source-specific limitations remain explicit rather than deleting experimental claims merely for inaccessible details.
