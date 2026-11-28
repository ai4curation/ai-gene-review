# PRMT1 curation notes

Deep research status: Perplexity was unavailable in this lane and `claude-code` was not authenticated, so no generated `PRMT1-deep-research-*` file was created. These notes summarize the fetched UniProt record, GOA rows, Reactome entries, PTHR11006 PAINT rows and accessible primary-paper text.

## Core biology

PRMT1 is the major type-I protein arginine methyltransferase. Its central activity is mono- and asymmetric dimethylation of histone H4 Arg-3 and many non-histone substrates. UniProt describes PRMT1 as the main enzyme mediating H4R3me1 and H4R3me2a and lists a broad set of non-histone substrates, including MRE11, 53BP1, CHTOP, MAP3K5/ASK1, MICU1 and NPRL2 (`file:human/PRMT1/PRMT1-uniprot.txt`, CC:FUNCTION).

PMID:11387442 directly supports the H4R3 axis, reporting that PRMT1 specifically methylates H4 Arg-3 in vitro and in vivo. The review keeps the H4R3 and asymmetric/monomethyl PRMT rows as core and modifies generic methyltransferase rows to the specific arginine methyltransferase activities.

## Boundary decisions

PRMT1 is highly pleiotropic because substrate methylation connects it to DNA repair, RNA-binding proteins, BMP/SMAD signaling, MAPK/JNK signaling, megakaryocyte and erythroid differentiation, and mTORC1 methionine sensing. The review keeps direct substrate pathways as non-core when the cited paper identifies a PRMT1 methylation event, such as MRE11 and 53BP1 methylation for homologous recombination in PMID:29651020, ASK1/MAP3K5 methylation for JNK attenuation in PMID:22095282, and NPRL2 methylation for methionine-sensitive mTORC1 activation in PMID:38006878.

The SARS-CoV-2 nucleoprotein Reactome row is marked over-annotated for `GO:0019082` viral protein processing: PRMT1 methylates a viral substrate, but the host enzyme does not execute viral protein maturation. Generic protein-binding rows were removed under the project policy, and broad ancestors such as enzyme binding and cytoplasm were marked `TOO_GENERAL` beside more informative retained rows.

## PANTHER

The PTHR11006 PAINT monomethyltransferase and asymmetric dimethyltransferase nodes are sound for PRMT1. PRMT1 also supports histone and transcription branches directly, but the root family placements for histone methyltransferase, chromatin remodeling and DNA-templated transcription are still too broad for all type-I PRMT members.
