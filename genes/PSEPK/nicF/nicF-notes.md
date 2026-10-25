# KT2440 nicF evidence notes

## Identity and reaction

Reviewed Q88FY5, PP_3941, is NicF maleamate amidohydrolase. Its PANTHER PTHR43540:SF1 official label is ISOCHORISMATASE HYDROLASE, with parent PEROXYUREIDOACRYLATE/UREIDOACRYLATE AMIDOHYDROLASE-RELATED. Actual Pfam PF00857 and InterPro IPR000868/IPR050272/IPR036380 support the isochorismatase-like hydrolase family. Neither the family name nor an unrelated donor substrate overrides the NicF experiment.

PMID:18678916 full Results explicitly reports activity in recombinant NicF E. coli crude extracts, 19.3 micromol/min/mg. This is reported specific activity, not a purified-enzyme Michaelis-Menten Vmax despite the current UniProt field heading. The coupled assay detects released ammonium through glutamate dehydrogenase and NADPH oxidation. NADPH is a coupling reagent, not an established NicF cofactor. The curated experiment-linked reaction reads “Reaction=maleamate + H2O = maleate + NH4(+)”.

D31/K121/C154 are conserved residues used in the original mechanistic inference. They were not individually tested by target mutagenesis in this study. Claims of proven target metal independence or an experimentally established full cysteine catalytic triad were removed from the standalone description/core. Homolog structural evidence may inform the hypothesis without becoming a KT2440 experiment.

## Annotation decisions

Nicotinate catabolism is accepted because NicF itself hydrolyzes a pathway intermediate; an individual nicF knockout is not claimed. The broad linear-amide hydrolase row is MODIFY to the already proposed maleamate amidohydrolase activity, also used as the core proposed function. QuickGO maleamate search found only an obsolete process term and no exact molecular function. No GOA file is cited as biological evidence; the previous GOA reference and redundant report quotations were removed.

## Source access and research provenance

Review and annotation-reviewer workflow applied on 2026-10-25. Existing KT2440 Falcon reports were read as literature guides, not regenerated or treated as primary experiments. PMID:18678916 remains abstract-only locally after a supported force refresh; the full Results and Methods were independently read at https://pmc.ncbi.nlm.nih.gov/articles/PMC2516282/. The review quotes the cached abstract or curated experimental UniProt statements where appropriate and does not pretend that a body-specific quotation is present in the cache. PMID:22530095 was fetched with full text. No publication cache was manually edited.

For the new S16 comparator, default Falcon deep research with Perplexity-lite fallback ran concurrently with publication caching; Falcon authentication failed and Perplexity returned HTTP401 insufficient_quota (log `/tmp/bacillus-nicotinate-s16-deep.log`). No provider-branded research file was fabricated. FEBA retrieval was attempted for all four targets: no local database or remote source was reachable, and no fitness artifact was written. PSEP6 also lacks a configured organism mapping. This is missing data, not a negative fitness phenotype. The GO-CAM index had no matches to Q88FY3, Q88FY4, Q88FY5 or F8G0M3.

## Shared downstream chemistry and taxonomic boundary

The lower order is N-formylmaleamate --NicD/Nfo--> maleamate plus formate --NicF/Ami--> maleate plus ammonium --MaiA/NicE/Iso--> fumarate. PMID:22530095 directly characterized the S16 versions after recombinant expression and purification. Its full text reports: “Attempts to degrade nicotinic acid by resting cells of strain S16 did not result in any degradation after 24 h of incubation”. S16 lacks the KT2440 nicAB entry genes in that study. Thus a shared lower enzyme cannot establish complete nicotinate degradation or justify transferring nicotinate-catabolism annotation to the nicotine-pathway comparator. The nicotine enzymes named NicA/NicA2 are not the KT2440 nicotinate hydroxylase small subunit merely because they share a name. No new nicotine-process annotation was added to the KT2440 genes.
