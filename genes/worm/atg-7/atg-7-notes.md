# atg-7 (G5EBK4, M7.5) review notes

## Provenance / process
- Accession G5EBK4 is the only UniProt entry for atg-7 (TrEMBL, 647 aa); used as-is.
- Deep research (`just deep-research-falcon worm atg-7 --fallback perplexity-lite`) failed: falcon timed out and the perplexity-lite fallback was killed (exit 137). No deep-research file exists; the review uses cached publications, the UniProt record and PubMed lookups only.
- All GOA-cited papers are abstract-only in the cache; extra papers fetched: PMID:27046254 (full text), PMID:26687600, PMID:20550938 (abstracts).

## Key evidence
- E1 for both autophagic Ubl systems: UniProt "E1-like activating enzyme involved in the 2 ubiquitin-like systems required for autophagy" (rule-based); active-site Cys523 (glycyl thioester, PIRSR) confirmed in sequence.
- C. elegans: "Lipidation of LGG-1 and LGG-2 is mediated by 2 enzymes, ATG-7 and ATG-3." and "LGG-1 and LGG-2 have different affinities for ATG-7 and ATG-3" [PMID:27046254].
- Dauer: "Dauer formation is associated with increased autophagy and also requires C. elegans orthologs of the yeast autophagy genes APG1, APG7, APG8, and AUT10." [PMID:12958363].
- Lifespan: "two essential autophagy genes (bec-1 and Ce-atg7) are required for the longevity phenotype of the C. elegans dietary restriction mutant" [PMID:17912023].
- Germline: "ATG-7 functions in concert with the DAF-7/TGF-β pathway to promote germline proliferation and is not required for cell-cycle progression" [PMID:28285998] - not in GOA for atg-7.

## Decisions
- MODIFY generic E1 IEA (GO:0008641) to the specific Atg8/Atg12 activating terms.
- MODIFY positive regulation of autophagosome assembly (IMP, PMID:24374177) to autophagosome assembly: ATG-7 is a catalytic core component, not a regulator.
- NEW GO:0061739 protein lipidation involved in autophagosome assembly (ATG-7 catalyses a step; comparator: human ATG7 IDA, yeast Atg7 GO:0006501 IDA/IMP).
- Yeast/Dicty-specific IBAs (PMN, nitrogen starvation) and mitophagy kept as non-core.
- Atg12 activation for worm ATG-7 rests on phylogeny only (no worm biochemistry found).
