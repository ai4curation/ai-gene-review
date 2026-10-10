# atg-13 / epg-1 (P34379) notes

Deep research failed on 2026-10-08 (falcon exit 137; perplexity provider unavailable). No
deep-research file; review based on cached papers and UniProt.

Accession: P34379 (Swiss-Prot, 443 aa, D2007.5; synonyms epg-1, atg-13).

## Key findings
- Divergent Atg13 homolog that binds UNC-51 [PMID:19377305 "epg-1 displays a similar expression pattern to, and directly interacts with, the C. elegans Atg1 homolog UNC-51"].
- Mutant phenotypes [PMID:19377305 "Loss of function of epg-1 causes defects in various autophagy-regulated processes, including degradation of aggregate-prone proteins and optimal survival of animals during starvation"].
- Binds EPG-9/ATG101 [PMID:22885670 "EPG-9 directly interacts with EPG-1/Atg13"].
- LIR-dependent binding to LGG-1 and PAS recruitment [PMID:26687600; UniProt "Recruited to preautophagosomes by lgg-1"].
- Yeast Atg13 binds and activates Atg1 [PMID:10995454 "Apg13, which binds to and activates Apg1"] - basis for the IBA protein kinase regulator activity.

## Curation decisions
- Protein binding IPI (EPG-9) -> REMOVE.
- Serine/threonine protein kinase complex (NAS) -> MODIFY to GO:1990316.
- Piecemeal microautophagy of the nucleus IBA -> MARK_AS_OVER_ANNOTATED.
- Axon / perikaryon locations reflect neuronal expression -> KEEP_AS_NON_CORE.
- Core MF: GO:0019887 protein kinase regulator activity (IBA; no worm in vitro kinase assay yet).
