# ift-20 (Q8TA52, IFT20 ortholog) notes

## Deep research status
`just deep-research-falcon worm ift-20 --fallback perplexity-lite` was run on 2026-10-08. Falcon timed out and the perplexity fallback was unavailable, so there is no deep-research file. The review was made by hand from the cached publications and PubMed.

## Summary with provenance
- ift-20 null (ok3191) worms form only short vestigial cilia [PMID:33997658 "IFT-20 loss leads to a severe defect in ciliary axoneme assembly but does not completely block ciliogenesis in C. elegans"], and they recruit less IFT-74 to the ciliary base and into cilia [PMID:33997658 "IFT-20 plays a role in the ciliary recruitment and entry of IFT subunits"].
- IFT-20::GFP undergoes IFT [PMID:33997658 "found that the C. elegans IFT20 homolog is also recruited to cilia where it undergoes IFT with similar kinetics to other IFT subunits"].
- Unlike mammals, worm IFT-20 is not seen at the Golgi [PMID:33997658 "in contrast to its homolog in mammalian cells, IFT-20 was not detectable at the Golgi and does not seem to interact with the C. elegans homolog of GMAP210"]. Mammalian IFT20 is at the Golgi, the basal body and cilia [PMID:16775004 "IFT20 subunit of the particle is localized to the Golgi complex in addition to the basal body and cilia"].
- Null worms are defective in osmotic avoidance and mating [PMID:33997658 "virtually all ift-20 null worms readily crossed the glycerol rings that wild-type worms avoided"].

## Curation decisions
- 16 GOA rows: 12 ACCEPT, 3 KEEP_AS_NON_CORE (cytoplasm IBA, dendrite IDA, neuronal cell body IDA), and 1 MARK_AS_OVER_ANNOTATED (centrosome IBA). The centrosome row reflects the mammalian context: worm IFT-20 is found only in postmitotic ciliated neurons.
- PMID:33997658 (microPublication 2021) was fetched and added. It has no GOA rows yet. An IMP to non-motile cilium assembly could be added from it, but cilium assembly (IBA) already covers this, so no NEW row was added.
