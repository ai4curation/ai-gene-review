# gyrA: H37Rv gyrase review

The target is P9WG47, Mycobacterium tuberculosis H37Rv, Rv0006; 838 aa. Both genes were absent before normal fetch-gene. The pristine document, original annotation payloads and raw hashes are archived in gyrA-source-analysis/pristine-seed.yaml. All 26 original payloads are unchanged.

## Identity and primary function

PMID17038336 states that gyrA and gyrB were amplified from H37Rv genomic DNA and the inserts sequenced identically to NC000962. His-tagged proteins were purified; no cleavage of tags is reported. GyrA wild type and mutants were reconstituted with GyrB. Fig8 measures kDNA decatenation, including a positive wild-type reaction at 0.01 micromolar. This is direct biochemical decatenation, not a conclusion from absence of topoisomerase IV. Its G729A/G729W inconsistency is not converted into a residue assertion here.

PMID15047530 independently reconstitutes negative supercoiling and explicitly says neither subunit alone performs it. Its cosmid T776 preparations carried C-terminal His6 on GyrA and N-terminal His10 on GyrB; H37Rv is explicitly the MIC-test strain. PMID41255390 independently specifies full-length H37Rv P9WG47/P9WG45 in pET28a and measures gyrase supercoiling/ATPase inhibition. The latter does not assay decatenation. Do not adopt that article's introductory conflation of TOPRIM and the N-terminal ATPase domain.

PMID22844097 uses the earlier PMID17038336 preparations with modifications and compares WT/mutant decatenation. PMID21745817 tests GyrB monomer/dimer assembly and reconstituted activities. Its mutant B-prime and GyrA-SBP constructs are kept distinct from wild-type full-length proteins. PMID31953321 instead reports relatively low M. tuberculosis supercoiling and decatenation rates; its cache remains abstract-only after a real force retry, with PMC challenge/Europe PMC500/publisher403 acquisition failures. The correct synthesis is demonstrated dual activity, not universally superior decatenation efficiency. The 2002 efficient-decatenase M. smegmatis paper is not treated as an H37Rv assay.

## Annotation decisions and limits

Whole-enzyme topoisomerase and supercoiling annotations are retained with explicit WRONG_QUALIFIER correction enables -> contributes_to, preserving original source fields. Core functions use contribution to the GyrA2GyrB2 complex. Generic DNA metabolism/type-II-complex terms are refined. Bare protein-binding annotations are removed by policy, not because assembly is false. Membrane proteomics remains UNDECIDED because full target-specific fractionation data are unavailable. GyrA ATP-binding/hydrolysis and magnesium binding are unresolved; original2001 full text was inaccessible, and holoenzyme ATP dependence cannot settle isolated-subunit chemistry. GyrB has a separately supported intrinsic ATP-hydrolysis IC proposal.

Purified plasmid/kDNA experiments establish capacities, not chromosome segregation in living H37Rv. The generic unlinking alternative can use both complete GyrA and GyrB contributions, with the native physiological inference explicit. Do not infer all missing topoisomerase-IV roles merely from its absence, or identify GyrB ATPase alone as an unlinking enzyme. No new biological-process annotation is manufactured.

## Provider and validation

A genuine default Falcon attempt failed HTTP403; no provider report was fabricated. Manual primary-source curation is recorded here. Focused validation and raw/payload proof are recorded under .cache/module-audit-logs/chromosomal-replication-20261106/gyrase/.
