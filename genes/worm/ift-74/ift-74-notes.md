# ift-74 (A0A2C9C2L6, IFT74 ortholog) notes

## Accession
UniProt has two unreviewed ift-74 entries, A0A2C9C2L6 (C18H9.8a, CE52310, 624 aa) and A0A2C9C2S9 (C18H9.8b, 579 aa). This review uses A0A2C9C2L6. It is the longer isoform a, it carries all the experimental GOA rows (19 rows, against 5 IEA rows on the b entry), and it is the sequence used by PMID:35969738 [PMID:35969738 "elegans IFT-74 was obtained from AlphaFold Protein Structure Database (ID: A0A2C9C2L6)"].

## Deep research status
Falcon timed out and the perplexity fallback was unavailable, so there is no deep-research file. The review was made by hand from the cached publications.

## Summary with provenance
- IFT-74 interacts with IFT-81, and the two mutants have the same phenotypes [PMID:17535250 "We also demonstrated that IFT-81 interacts and co-localizes with IFT-74"; "ift-81 and ift-74 mutants similarly exhibited weak anomalies in cilia formation and obvious disruptions of transport in mature cilia"].
- IFT-74/81 is the tubulin-binding module. DYF-5 phosphorylates the IFT-74 N-terminus and lowers its affinity for tubulin [PMID:35969738 "the ciliary kinase DYF-5/MAK phosphorylates multiple sites within the tubulin-binding module of IFT-74, reducing the tubulin-binding affinity of IFT-74/81 approximately sixfold"].
- Microtubule binding was measured with purified IFT-74/81/IFTA-2 in TIRF decoration assays [PMID:35969738 "We found that the colocalization between IFT-74/81/IFTA-2 and MTs was reduced by DYF-5 phosphorylation"].
- In the orthologs, IFT74N binds the beta-tubulin tail [PMID:23990561 "IFT81N appears to bind the globular domain of tubulin to provide specificity, and IFT74N recognizes the β-tubulin tail to increase affinity"].

## Curation decisions
- 19 GOA rows: 15 ACCEPT, 2 KEEP_AS_NON_CORE (chemotaxis, detection of stimulus), 1 MARK_AS_OVER_ANNOTATED (multicellular organism growth), and 1 REMOVE (protein binding IPI; the interaction is captured by the IFT-B part_of rows).
- The microtubule binding IDA was accepted because the paper contains an MT decoration assay. The core MF is beta-tubulin binding.
