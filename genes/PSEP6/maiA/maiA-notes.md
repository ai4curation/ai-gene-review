# S16 maiA/Iso comparator evidence notes

## Exact identity

UniProt F8G0M3, PSEP6, 252 amino acids, maps to original cluster GQ857548/ADN26549.1 and KEGG PPS_4060. UniProt uses maiA; the papers call the enzyme Iso/Pp-Iso. RCSB4FQ5 and4FQ7 link this accession to the substrate-bound C200A and wild-type structures from PMID:23347155. Expression tags mean PDB construct length is not the native protein length. PANTHER PTHR40267:SF1 officially reads BLR3294 PROTEIN and matches KT2440 MaiA; HAMAP MF_00943, InterPro IPR028615 and Pfam PF17645 provide more interpretable family support.

## Direct target experiments

PMID:22530095 full text reports “Purified Iso catalyzed the isomerization of maleate acid to fumaric acid”. HPLC verified the reaction. Reported apparent Km is0.689mM, Vmax9.4U/mg and kcat4.0s-1 at30C/pH8.4. These are S16 data, not transferable numerical parameters for KT2440 MaiA. PMID:23347155 cached abstract independently reports wild-type and C200A/maleate structures, Asn17/Asn169 mutagenesis, and simulations/activity assays supporting substrate-access loop movement. The motion is a mechanistic interpretation, not directly visualized dynamics.

The RCSB biological assembly for4FQ7 is a tetramer whereas UniProt HAMAP predicts a dimer. Neither a new oligomerization process nor a target stoichiometric core was asserted. The specific solution assembly is left as a question.

## Decisions and comparator scope

Both seeded molecular-function rows are reviewed: maleate isomerase ACCEPT; broad isomerase MODIFY to the same specific activity. One core records the direct chemistry. No new nicotinate-process assertion is made because the same study reports no nicotinate degradation by S16. The description explains its native nicotine pathway role. This comparator is not a native complete nicotinate-route exemplar.

## Source access and research provenance

Review and annotation-reviewer workflow applied on 2026-10-25. Existing KT2440 Falcon reports were read as literature guides, not regenerated or treated as primary experiments. PMID:18678916 remains abstract-only locally after a supported force refresh; the full Results and Methods were independently read at https://pmc.ncbi.nlm.nih.gov/articles/PMC2516282/. The review quotes the cached abstract or curated experimental UniProt statements where appropriate and does not pretend that a body-specific quotation is present in the cache. PMID:22530095 was fetched with full text. No publication cache was manually edited.

For the new S16 comparator, default Falcon deep research with Perplexity-lite fallback ran concurrently with publication caching; Falcon authentication failed and Perplexity returned HTTP401 insufficient_quota (log `/tmp/bacillus-nicotinate-s16-deep.log`). No provider-branded research file was fabricated. FEBA retrieval was attempted for all four targets: no local database or remote source was reachable, and no fitness artifact was written. PSEP6 also lacks a configured organism mapping. This is missing data, not a negative fitness phenotype. The GO-CAM index had no matches to Q88FY3, Q88FY4, Q88FY5 or F8G0M3.

## Shared downstream chemistry and taxonomic boundary

The lower order is N-formylmaleamate --NicD/Nfo--> maleamate plus formate --NicF/Ami--> maleate plus ammonium --MaiA/NicE/Iso--> fumarate. PMID:22530095 directly characterized the S16 versions after recombinant expression and purification. Its full text reports: “Attempts to degrade nicotinic acid by resting cells of strain S16 did not result in any degradation after 24 h of incubation”. S16 lacks the KT2440 nicAB entry genes in that study. Thus a shared lower enzyme cannot establish complete nicotinate degradation or justify transferring nicotinate-catabolism annotation to the nicotine-pathway comparator. The nicotine enzymes named NicA/NicA2 are not the KT2440 nicotinate hydroxylase small subunit merely because they share a name. No new nicotine-process annotation was added to the KT2440 genes.
